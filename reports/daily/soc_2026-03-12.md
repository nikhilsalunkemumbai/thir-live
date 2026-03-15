# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-12 |
| **Generated At** | 2026-03-12T22:23:54Z |
| **Shift Time** | 22:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **789** |
| Confirmed Threats | **63** |
| False Positives Filtered | **726** (92.0%) |
| Unique Attacker IPs | **183** |
| Countries of Origin | **11** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **721** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c6de23217db5

| Field | Detail |
|---|---|
| **Source IP** | `130.250.231[.]114` |
| **First Seen** | 2026-03-12 02:53 |
| **Last Seen** | 2026-03-12 02:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 02:53:30` | `cowrie.session.connect` |
| `2026-03-12 02:53:30` | `cowrie.client.version` |
| `2026-03-12 02:53:31` | `cowrie.client.kex` |
| `2026-03-12 02:53:32` | `cowrie.login.success` |
| `2026-03-12 02:53:33` | `cowrie.session.params` |
| `2026-03-12 02:53:33` | `cowrie.command.input` |
| `2026-03-12 02:53:33` | `cowrie.command.failed` |
| `2026-03-12 02:53:33` | `cowrie.log.closed` |
| `2026-03-12 02:53:34` | `cowrie.session.params` |
| `2026-03-12 02:53:34` | `cowrie.command.input` |
| `2026-03-12 02:53:34` | `cowrie.session.file_download` |
| `2026-03-12 02:53:34` | `cowrie.log.closed` |
| `2026-03-12 02:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.250.231[.]114` to AbuseIPDB if not already reported
- [ ] Block `130.250.231[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-231d46368daa

| Field | Detail |
|---|---|
| **Source IP** | `130.250.231[.]114` |
| **First Seen** | 2026-03-12 02:53 |
| **Last Seen** | 2026-03-12 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 02:53:37` | `cowrie.session.connect` |
| `2026-03-12 02:53:37` | `cowrie.client.version` |
| `2026-03-12 02:53:38` | `cowrie.client.kex` |
| `2026-03-12 02:53:39` | `cowrie.login.success` |
| `2026-03-12 02:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.250.231[.]114` to AbuseIPDB if not already reported
- [ ] Block `130.250.231[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00b053dbb4c

| Field | Detail |
|---|---|
| **Source IP** | `206.81.1[.]156` |
| **First Seen** | 2026-03-12 13:29 |
| **Last Seen** | 2026-03-12 13:30 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 13:29:21` | `cowrie.session.connect` |
| `2026-03-12 13:29:21` | `cowrie.client.version` |
| `2026-03-12 13:29:22` | `cowrie.client.kex` |
| `2026-03-12 13:29:22` | `cowrie.login.success` |
| `2026-03-12 13:30:30` | `cowrie.session.file_upload` |
| `2026-03-12 13:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.81.1[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.81.1[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c14e6454ec6

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:32 |
| **Last Seen** | 2026-03-12 17:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:32:53` | `cowrie.session.connect` |
| `2026-03-12 17:32:54` | `cowrie.client.version` |
| `2026-03-12 17:32:54` | `cowrie.client.kex` |
| `2026-03-12 17:32:59` | `cowrie.login.success` |
| `2026-03-12 17:33:03` | `cowrie.session.params` |
| `2026-03-12 17:33:03` | `cowrie.command.input` |
| `2026-03-12 17:33:06` | `cowrie.log.closed` |
| `2026-03-12 17:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a590ccb7d518

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:33 |
| **Last Seen** | 2026-03-12 17:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:33:36` | `cowrie.session.connect` |
| `2026-03-12 17:33:38` | `cowrie.client.version` |
| `2026-03-12 17:33:38` | `cowrie.client.kex` |
| `2026-03-12 17:33:45` | `cowrie.login.success` |
| `2026-03-12 17:33:49` | `cowrie.session.params` |
| `2026-03-12 17:33:49` | `cowrie.command.input` |
| `2026-03-12 17:33:51` | `cowrie.log.closed` |
| `2026-03-12 17:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2345b8cf87e8

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:33 |
| **Last Seen** | 2026-03-12 17:33 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:33:41` | `cowrie.session.connect` |
| `2026-03-12 17:33:43` | `cowrie.client.version` |
| `2026-03-12 17:33:43` | `cowrie.client.kex` |
| `2026-03-12 17:33:51` | `cowrie.login.success` |
| `2026-03-12 17:33:54` | `cowrie.session.params` |
| `2026-03-12 17:33:54` | `cowrie.command.input` |
| `2026-03-12 17:33:57` | `cowrie.log.closed` |
| `2026-03-12 17:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615e9c086679

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:34 |
| **Last Seen** | 2026-03-12 17:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:34:23` | `cowrie.session.connect` |
| `2026-03-12 17:34:24` | `cowrie.client.version` |
| `2026-03-12 17:34:24` | `cowrie.client.kex` |
| `2026-03-12 17:34:29` | `cowrie.login.success` |
| `2026-03-12 17:34:32` | `cowrie.session.params` |
| `2026-03-12 17:34:32` | `cowrie.command.input` |
| `2026-03-12 17:34:33` | `cowrie.log.closed` |
| `2026-03-12 17:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce9b3ce08669

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:35 |
| **Last Seen** | 2026-03-12 17:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:35:16` | `cowrie.session.connect` |
| `2026-03-12 17:35:17` | `cowrie.client.version` |
| `2026-03-12 17:35:17` | `cowrie.client.kex` |
| `2026-03-12 17:35:18` | `cowrie.login.success` |
| `2026-03-12 17:35:18` | `cowrie.session.params` |
| `2026-03-12 17:35:18` | `cowrie.command.input` |
| `2026-03-12 17:35:18` | `cowrie.log.closed` |
| `2026-03-12 17:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7fc5d555e82

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:35 |
| **Last Seen** | 2026-03-12 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:35:31` | `cowrie.session.connect` |
| `2026-03-12 17:35:31` | `cowrie.client.version` |
| `2026-03-12 17:35:32` | `cowrie.client.kex` |
| `2026-03-12 17:35:32` | `cowrie.login.success` |
| `2026-03-12 17:35:33` | `cowrie.session.params` |
| `2026-03-12 17:35:33` | `cowrie.command.input` |
| `2026-03-12 17:35:33` | `cowrie.log.closed` |
| `2026-03-12 17:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49809ca8d10c

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:35 |
| **Last Seen** | 2026-03-12 17:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:35:44` | `cowrie.session.connect` |
| `2026-03-12 17:35:44` | `cowrie.client.version` |
| `2026-03-12 17:35:44` | `cowrie.client.kex` |
| `2026-03-12 17:35:45` | `cowrie.login.success` |
| `2026-03-12 17:35:46` | `cowrie.session.params` |
| `2026-03-12 17:35:46` | `cowrie.command.input` |
| `2026-03-12 17:35:46` | `cowrie.log.closed` |
| `2026-03-12 17:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5509811c056f

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:36 |
| **Last Seen** | 2026-03-12 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:36:32` | `cowrie.session.connect` |
| `2026-03-12 17:36:33` | `cowrie.client.version` |
| `2026-03-12 17:36:33` | `cowrie.client.kex` |
| `2026-03-12 17:36:33` | `cowrie.login.success` |
| `2026-03-12 17:36:34` | `cowrie.session.params` |
| `2026-03-12 17:36:34` | `cowrie.command.input` |
| `2026-03-12 17:36:34` | `cowrie.log.closed` |
| `2026-03-12 17:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d65fa9d8fb9

| Field | Detail |
|---|---|
| **Source IP** | `209.38.88[.]129` |
| **First Seen** | 2026-03-12 17:36 |
| **Last Seen** | 2026-03-12 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 17:36:38` | `cowrie.session.connect` |
| `2026-03-12 17:36:38` | `cowrie.client.version` |
| `2026-03-12 17:36:38` | `cowrie.client.kex` |
| `2026-03-12 17:36:39` | `cowrie.login.success` |
| `2026-03-12 17:36:39` | `cowrie.session.params` |
| `2026-03-12 17:36:39` | `cowrie.command.input` |
| `2026-03-12 17:36:39` | `cowrie.log.closed` |
| `2026-03-12 17:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.88[.]129` to AbuseIPDB if not already reported
- [ ] Block `209.38.88[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.131.211[.]42` | **12** | 2026-03-12 19:55 | 2026-03-12 20:26 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `130.250.231[.]114` | **11** | 2026-03-12 02:50 | 2026-03-12 02:59 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.176[.]249` | **11** | 2026-03-12 19:58 | 2026-03-12 20:12 | 16m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.246.139[.]120` | **10** | 2026-03-12 05:14 | 2026-03-12 05:39 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.93.89[.]95` | **2** | 2026-03-12 08:26 | 2026-03-12 08:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.122[.]158` | 1 | 2026-03-12 09:04 | 2026-03-12 09:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.71.149[.]30` | 1 | 2026-03-12 17:09 | 2026-03-12 17:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.152.101[.]151` | 1 | 2026-03-12 07:04 | 2026-03-12 07:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `61.73.163[.]9` | 1 | 2026-03-12 04:27 | 2026-03-12 04:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `66.132.153[.]143` | 1 | 2026-03-12 15:32 | 2026-03-12 15:32 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (3 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `130.250.231[.]114` | CO | CELSIA INTERNET S.A.S. | **100** ⚠️ | 2 |
| `34.131.211[.]42` | IN | Google LLC | **100** ⚠️ | 18 |
| `185.93.89[.]95` | NL | Limited Network LTD | **100** ⚠️ | 0 |
| `120.48.122[.]158` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 0 |
| `120.71.149[.]30` | CN | CHINANET Xinjiang province network | **100** ⚠️ | 0 |
| `184.152.101[.]151` | US | Charter Communications Inc | **100** ⚠️ | 0 |
| `43.246.139[.]120` | IN | Airdesign Broadcast Media Pvt Ltd | **100** ⚠️ | 0 |
| `61.73.163[.]9` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `66.132.153[.]143` | US | Censys, Inc. | **100** ⚠️ | 0 |
| `180.76.176[.]249` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |
| [T1105](https://attack.mitre.org/techniques/T1105) | — |

---

## 🔕 False Positive Summary (726 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 680 |
| AbuseIPDB score 14 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 42 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 789 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 183 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 726 filtered (92.0%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 12 priority case(s) shown individually · 10 recon entry/entries in table (5 group(s) consolidating 46 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.1 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-12T22:23:54Z_
