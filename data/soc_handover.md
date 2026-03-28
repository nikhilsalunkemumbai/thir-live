# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T08:37:01Z |
| **Shift Time** | 08:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **43** |
| Confirmed Threats | **33** |
| False Positives Filtered | **10** (23.3%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **17** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **41** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **13** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `guest` | 2 |
| `blank` | 2 |
| `debian` | 2 |
| `root` | 2 |
| `support` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `5555` | 1 |
| `1q2w3e4r` | 1 |
| `Passw0rd` | 1 |
| `qwer1234` | 1 |
| `123abc` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `guest` | `5555` | 1 |
| `blank` | `1q2w3e4r` | 1 |
| `blank` | `Passw0rd` | 1 |
| `Admin` | `qwer1234` | 1 |
| `debian` | `123abc` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin147258` | `14.103.118.79` | 2026-03-28T07:57:39 |
| `root` | `3245gs5662d34` | `14.103.118.79` | 2026-03-28T07:57:43 |

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
Source IPs: `14.103.118.79`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **25** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS132124` | Information and Communication Technology Agency of Sri Lanka | 1 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-91af4ef5bd69

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]79` |
| **First Seen** | 2026-03-28 07:57 |
| **Last Seen** | 2026-03-28 07:57 |
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
| `2026-03-28 07:57:39` | `cowrie.session.connect` |
| `2026-03-28 07:57:39` | `cowrie.client.version` |
| `2026-03-28 07:57:39` | `cowrie.client.kex` |
| `2026-03-28 07:57:39` | `cowrie.login.success` |
| `2026-03-28 07:57:40` | `cowrie.session.params` |
| `2026-03-28 07:57:40` | `cowrie.command.input` |
| `2026-03-28 07:57:40` | `cowrie.command.failed` |
| `2026-03-28 07:57:40` | `cowrie.log.closed` |
| `2026-03-28 07:57:40` | `cowrie.session.params` |
| `2026-03-28 07:57:40` | `cowrie.command.input` |
| `2026-03-28 07:57:40` | `cowrie.session.file_download` |
| `2026-03-28 07:57:40` | `cowrie.log.closed` |
| `2026-03-28 07:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]79` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6cb61a0b95

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]79` |
| **First Seen** | 2026-03-28 07:57 |
| **Last Seen** | 2026-03-28 07:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 07:57:42` | `cowrie.session.connect` |
| `2026-03-28 07:57:42` | `cowrie.client.version` |
| `2026-03-28 07:57:43` | `cowrie.client.kex` |
| `2026-03-28 07:57:43` | `cowrie.login.success` |
| `2026-03-28 07:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]79` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.135.40[.]125` | **9** | 2026-03-28 08:16 | 2026-03-28 08:18 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.219.11[.]104` | **3** | 2026-03-28 07:35 | 2026-03-28 07:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.169.104[.]65` | **2** | 2026-03-28 08:09 | 2026-03-28 08:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.181[.]192` | 1 | 2026-03-28 07:59 | 2026-03-28 08:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]79` | 1 | 2026-03-28 07:57 | 2026-03-28 07:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.166.94[.]133` | 1 | 2026-03-28 08:03 | 2026-03-28 08:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.4[.]138` | 1 | 2026-03-28 08:03 | 2026-03-28 08:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.72.7[.]53` | 1 | 2026-03-28 07:07 | 2026-03-28 07:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.31.8[.]12` | 1 | 2026-03-28 08:04 | 2026-03-28 08:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.121.109[.]124` | 1 | 2026-03-28 08:03 | 2026-03-28 08:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.80.224[.]223` | 1 | 2026-03-28 07:45 | 2026-03-28 07:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.180.162[.]23` | 1 | 2026-03-28 07:41 | 2026-03-28 07:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-03-28 07:50 | 2026-03-28 07:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.150[.]249` | 1 | 2026-03-28 07:20 | 2026-03-28 07:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.49.113[.]138` | 1 | 2026-03-28 07:43 | 2026-03-28 07:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]179` | 1 | 2026-03-28 07:26 | 2026-03-28 07:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]191` | 1 | 2026-03-28 08:28 | 2026-03-28 08:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.196.106[.]164` | 1 | 2026-03-28 08:23 | 2026-03-28 08:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.244.113[.]178` | 1 | 2026-03-28 07:48 | 2026-03-28 07:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.79.108[.]51` | 1 | 2026-03-28 08:00 | 2026-03-28 08:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 9/100 | 🟢 LOW | **24/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `65.20.204[.]179` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 31 |
| `18.219.11[.]104` | US | Amazon Technologies Inc. | **100** ⚠️ | 12 |
| `65.20.237[.]191` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 35 |
| `82.196.106[.]164` | SE | Bahnhof AB | **100** ⚠️ | 22 |
| `49.124.150[.]249` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 19 |
| `209.121.109[.]124` | CA | TELUS Communications Inc. | **100** ⚠️ | 0 |
| `95.79.108[.]51` | RU | JSC ER-Telecom Holding Nizhny Novgorod branch | **100** ⚠️ | 50 |
| `183.171.4[.]138` | MY | Celcom Axiata Berhad | **100** ⚠️ | 11 |
| `91.244.113[.]178` | RU | WIRENET LLC | **100** ⚠️ | 50 |
| `42.180.162[.]23` | CN | UNICOM Liaoning Province Network | **100** ⚠️ | 23 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 43 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (23.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 20 recon entry/entries in table (3 group(s) consolidating 14 session(s)).

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
_Report time: 2026-03-28T08:37:01Z_
