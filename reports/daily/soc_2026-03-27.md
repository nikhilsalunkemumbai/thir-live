# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T07:04:51Z |
| **Shift Time** | 07:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **42** |
| Confirmed Threats | **11** |
| False Positives Filtered | **31** (73.8%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **11** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **8** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **6** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `supervisor` | 2 |
| `345gs5662d34` | 1 |
| `unknown` | 1 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `BHU*nji9` | 1 |
| `345gs5662d34` | 1 |
| `3245gs5662d34` | 1 |
| `supervisor2005` | 1 |
| `unknown2008` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `BHU*nji9` | 1 |
| `345gs5662d34` | `345gs5662d34` | 1 |
| `root` | `3245gs5662d34` | 1 |
| `supervisor` | `supervisor2005` | 1 |
| `unknown` | `unknown2008` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `BHU*nji9` | `112.219.151.50` | 2026-03-27T05:56:35 |
| `root` | `3245gs5662d34` | `112.219.151.50` | 2026-03-27T05:56:38 |

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
Source IPs: `112.219.151.50`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **16** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS137120` | Nas Internet Services Private Limited | 1 | LOW |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |
| `AS3269` | Telecom Italia S.p.A. | 1 | LOW |
| `AS39608` | Lanet Network Ltd | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-25aa4a70f72b

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-03-27 05:56 |
| **Last Seen** | 2026-03-27 05:56 |
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
| `2026-03-27 05:56:34` | `cowrie.session.connect` |
| `2026-03-27 05:56:34` | `cowrie.client.version` |
| `2026-03-27 05:56:34` | `cowrie.client.kex` |
| `2026-03-27 05:56:35` | `cowrie.login.success` |
| `2026-03-27 05:56:35` | `cowrie.session.params` |
| `2026-03-27 05:56:35` | `cowrie.command.input` |
| `2026-03-27 05:56:35` | `cowrie.command.failed` |
| `2026-03-27 05:56:35` | `cowrie.log.closed` |
| `2026-03-27 05:56:35` | `cowrie.session.params` |
| `2026-03-27 05:56:35` | `cowrie.command.input` |
| `2026-03-27 05:56:36` | `cowrie.session.file_download` |
| `2026-03-27 05:56:36` | `cowrie.log.closed` |
| `2026-03-27 05:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac67b9bd1d4

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-03-27 05:56 |
| **Last Seen** | 2026-03-27 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 05:56:38` | `cowrie.session.connect` |
| `2026-03-27 05:56:38` | `cowrie.client.version` |
| `2026-03-27 05:56:38` | `cowrie.client.kex` |
| `2026-03-27 05:56:38` | `cowrie.login.success` |
| `2026-03-27 05:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `106.1.188[.]238` | 1 | 2026-03-27 06:53 | 2026-03-27 06:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.219.151[.]50` | 1 | 2026-03-27 05:56 | 2026-03-27 05:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.36.174[.]177` | 1 | 2026-03-27 07:00 | 2026-03-27 07:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.82.108[.]109` | 1 | 2026-03-27 06:45 | 2026-03-27 06:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.197.166[.]78` | 1 | 2026-03-27 05:59 | 2026-03-27 05:59 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.164.91[.]67` | 1 | 2026-03-27 05:45 | 2026-03-27 05:46 | 56s | 0 | `T1592` | 🟢 LOW |
| `59.92.51[.]186` | 1 | 2026-03-27 06:24 | 2026-03-27 06:24 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]88` | 1 | 2026-03-27 07:00 | 2026-03-27 07:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.10.98[.]82` | 1 | 2026-03-27 06:00 | 2026-03-27 06:00 | 4s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `59.92.51[.]186` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 22 |
| `176.36.174[.]177` | UA | Lanet Network Ltd | **100** ⚠️ | 22 |
| `81.10.98[.]82` | EG | TE Data | **100** ⚠️ | 18 |
| `223.197.166[.]78` | HK | HKT Limited | **100** ⚠️ | 50 |
| `112.219.151[.]50` | KR | LG Uplus | **100** ⚠️ | 50 |
| `106.1.188[.]238` | TW | kbro CO. Ltd. | **100** ⚠️ | 50 |
| `65.20.204[.]88` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 48 |
| `39.164.91[.]67` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `183.82.108[.]109` | IN | ACT HYD | **100** ⚠️ | 0 |
| `162.253.68[.]102` | US | Performive LLC | **69** | 29 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (31 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 25 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 42 cases |
| Tool 34  | Credential Extractor        | ✅ 8 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 31 filtered (73.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 9 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-27T07:04:51Z_
