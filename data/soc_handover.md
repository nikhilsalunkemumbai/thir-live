# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T14:41:14Z |
| **Shift Time** | 14:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **28** |
| Confirmed Threats | **18** |
| False Positives Filtered | **10** (35.7%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **12** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **26** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **7** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `Root` | 2 |
| `Operator` | 2 |
| `root` | 2 |
| `config` | 1 |
| `345gs5662d34` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `8888` | 1 |
| `987654321` | 1 |
| `test` | 1 |
| `123456` | 1 |
| `Qazwsx1111111` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `8888` | 1 |
| `Root` | `987654321` | 1 |
| `Root` | `test` | 1 |
| `Operator` | `123456` | 1 |
| `root` | `Qazwsx1111111` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx1111111` | `186.13.24.118` | 2026-04-03T14:02:26 |
| `root` | `3245gs5662d34` | `186.13.24.118` | 2026-04-03T14:02:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **28** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 9 |
| libssh | 4 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 7 | 7 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 7 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 2 | 2 | — |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
Source IPs: `186.13.24.118`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **19** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS212512` | Detai Prosperous Technologies Limited | 2 | LOW |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | MEDIUM |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS25159` | PJSC MegaFon | 1 | HIGH |
| `AS135905` | VIETNAM POSTS AND TELECOMMUNICATIONS GROUP | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c5ba849303a0

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-04-03 14:02 |
| **Last Seen** | 2026-04-03 14:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 14:02:24` | `cowrie.session.connect` |
| `2026-04-03 14:02:24` | `cowrie.client.version` |
| `2026-04-03 14:02:25` | `cowrie.client.kex` |
| `2026-04-03 14:02:26` | `cowrie.login.success` |
| `2026-04-03 14:02:27` | `cowrie.session.params` |
| `2026-04-03 14:02:27` | `cowrie.command.input` |
| `2026-04-03 14:02:27` | `cowrie.command.failed` |
| `2026-04-03 14:02:27` | `cowrie.log.closed` |
| `2026-04-03 14:02:28` | `cowrie.session.params` |
| `2026-04-03 14:02:28` | `cowrie.command.input` |
| `2026-04-03 14:02:28` | `cowrie.session.file_download` |
| `2026-04-03 14:02:28` | `cowrie.log.closed` |
| `2026-04-03 14:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce83a1caf290

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-04-03 14:02 |
| **Last Seen** | 2026-04-03 14:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 14:02:32` | `cowrie.session.connect` |
| `2026-04-03 14:02:32` | `cowrie.client.version` |
| `2026-04-03 14:02:33` | `cowrie.client.kex` |
| `2026-04-03 14:02:34` | `cowrie.login.success` |
| `2026-04-03 14:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `64.227.110[.]161` | **2** | 2026-04-03 13:05 | 2026-04-03 13:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.34.138[.]22` | 1 | 2026-04-03 14:39 | 2026-04-03 14:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `103.61.122[.]229` | 1 | 2026-04-03 13:29 | 2026-04-03 13:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-04-03 14:07 | 2026-04-03 14:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-04-03 14:33 | 2026-04-03 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.69.76[.]148` | 1 | 2026-04-03 13:55 | 2026-04-03 13:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]136` | 1 | 2026-04-03 13:18 | 2026-04-03 13:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.167.96[.]50` | 1 | 2026-04-03 13:57 | 2026-04-03 13:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.79.218[.]101` | 1 | 2026-04-03 14:34 | 2026-04-03 14:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-04-03 13:36 | 2026-04-03 13:36 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.13.24[.]118` | 1 | 2026-04-03 14:02 | 2026-04-03 14:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.222.55[.]187` | 1 | 2026-04-03 14:07 | 2026-04-03 14:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.153.184[.]75` | 1 | 2026-04-03 14:39 | 2026-04-03 14:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.154[.]164` | 1 | 2026-04-03 14:16 | 2026-04-03 14:16 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.233.12[.]109` | 1 | 2026-04-03 13:29 | 2026-04-03 13:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `1.34.138[.]22` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 10 |
| `186.222.55[.]187` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 18 |
| `80.233.12[.]109` | IE | Three Ireland (Hutchison) limited | **100** ⚠️ | 47 |
| `47.153.184[.]75` | US | Frontier Communications of America, Inc. | **100** ⚠️ | 8 |
| `125.69.76[.]148` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `183.239.20[.]236` | CN | China Mobile Communications Corporation | **100** ⚠️ | 16 |
| `115.86.227[.]79` | KR | HVYeongseo | **100** ⚠️ | 24 |
| `64.227.110[.]161` | US | DigitalOcean, LLC | **100** ⚠️ | 21 |
| `182.79.218[.]101` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `178.178.194[.]136` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 14 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 28 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (35.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 15 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-04-03T14:41:14Z_
