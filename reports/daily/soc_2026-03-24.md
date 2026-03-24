# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T22:28:51Z |
| **Shift Time** | 22:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **60** |
| False Positives Filtered | **9** (13.0%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **13** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **62** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **58** |
| Unique Credential Pairs | **50** |
| Unique Usernames | **44** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `Admin` | 3 |
| `345gs5662d34` | 3 |
| `admin` | 2 |
| `it` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 8 |
| `password` | 5 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `T@cl0ud123` | 2 |
| `it` | `1234` | 2 |
| `teamspeak` | `teamspeak` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ivdev` | `41.32.249.165` | 2026-03-24T21:19:38 |
| `root` | `T@cl0ud123` | `103.117.56.152` | 2026-03-24T21:42:37 |
| `root` | `3245gs5662d34` | `103.117.56.152` | 2026-03-24T21:42:40 |
| `root` | `T@cl0ud123` | `8.222.178.0` | 2026-03-24T21:58:16 |
| `root` | `3245gs5662d34` | `8.222.178.0` | 2026-03-24T21:58:18 |
| `root` | `Qwer1234!` | `34.91.0.68` | 2026-03-24T22:01:54 |
| `root` | `3245gs5662d34` | `34.91.0.68` | 2026-03-24T22:01:57 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox IBTKE
```
Source IPs: `41.32.249.165`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `8.222.178.0`, `103.117.56.152`, `34.91.0.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **21** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS46375` | Sonic Telecom LLC | 1 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS8452` | TE-AS | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-178f96d2a148

| Field | Detail |
|---|---|
| **Source IP** | `41.32.249[.]165` |
| **First Seen** | 2026-03-24 21:19 |
| **Last Seen** | 2026-03-24 21:21 |
| **Session Duration** | 103s |
| **Login Attempts** | 5 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox IBTKE` |
| **Download Attempts** | tfxxp://41.32.249[.]165:57203/.i |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 21:19:36` | `cowrie.session.connect` |
| `2026-03-24 21:19:36` | `cowrie.telnet.option` |
| `2026-03-24 21:19:36` | `cowrie.login.failed` |
| `2026-03-24 21:19:36` | `cowrie.telnet.option` |
| `2026-03-24 21:19:37` | `cowrie.login.failed` |
| `2026-03-24 21:19:37` | `cowrie.telnet.option` |
| `2026-03-24 21:19:37` | `cowrie.login.failed` |
| `2026-03-24 21:19:37` | `cowrie.telnet.option` |
| `2026-03-24 21:19:37` | `cowrie.login.failed` |
| `2026-03-24 21:19:38` | `cowrie.telnet.option` |
| `2026-03-24 21:19:38` | `cowrie.login.success` |
| `2026-03-24 21:19:38` | `cowrie.session.params` |
| `2026-03-24 21:19:38` | `cowrie.command.input` |
| `2026-03-24 21:19:38` | `cowrie.command.input` |
| `2026-03-24 21:19:38` | `cowrie.command.failed` |
| `2026-03-24 21:19:38` | `cowrie.command.input` |
| `2026-03-24 21:19:38` | `cowrie.command.failed` |
| `2026-03-24 21:19:38` | `cowrie.command.input` |
| `2026-03-24 21:19:38` | `cowrie.command.input` |
| `2026-03-24 21:19:38` | `cowrie.command.input` |
| `2026-03-24 21:19:38` | `cowrie.command.input` |
| `2026-03-24 21:19:39` | `cowrie.command.input` |
| `2026-03-24 21:19:39` | `cowrie.command.failed` |
| `2026-03-24 21:19:39` | `cowrie.command.input` |
| `2026-03-24 21:19:39` | `cowrie.command.input` |
| `2026-03-24 21:19:59` | `cowrie.session.file_download` |
| `2026-03-24 21:21:19` | `cowrie.log.closed` |
| `2026-03-24 21:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.32.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.32.249[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70271639950

| Field | Detail |
|---|---|
| **Source IP** | `103.117.56[.]152` |
| **First Seen** | 2026-03-24 21:42 |
| **Last Seen** | 2026-03-24 21:42 |
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
| `2026-03-24 21:42:36` | `cowrie.session.connect` |
| `2026-03-24 21:42:36` | `cowrie.client.version` |
| `2026-03-24 21:42:36` | `cowrie.client.kex` |
| `2026-03-24 21:42:37` | `cowrie.login.success` |
| `2026-03-24 21:42:37` | `cowrie.session.params` |
| `2026-03-24 21:42:37` | `cowrie.command.input` |
| `2026-03-24 21:42:37` | `cowrie.command.failed` |
| `2026-03-24 21:42:37` | `cowrie.log.closed` |
| `2026-03-24 21:42:37` | `cowrie.session.params` |
| `2026-03-24 21:42:37` | `cowrie.command.input` |
| `2026-03-24 21:42:37` | `cowrie.session.file_download` |
| `2026-03-24 21:42:37` | `cowrie.log.closed` |
| `2026-03-24 21:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.117.56[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.117.56[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8480bc66a27

| Field | Detail |
|---|---|
| **Source IP** | `103.117.56[.]152` |
| **First Seen** | 2026-03-24 21:42 |
| **Last Seen** | 2026-03-24 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 21:42:39` | `cowrie.session.connect` |
| `2026-03-24 21:42:39` | `cowrie.client.version` |
| `2026-03-24 21:42:39` | `cowrie.client.kex` |
| `2026-03-24 21:42:40` | `cowrie.login.success` |
| `2026-03-24 21:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.117.56[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.117.56[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0ee6462eea

| Field | Detail |
|---|---|
| **Source IP** | `8.222.178[.]0` |
| **First Seen** | 2026-03-24 21:58 |
| **Last Seen** | 2026-03-24 21:58 |
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
| `2026-03-24 21:58:16` | `cowrie.session.connect` |
| `2026-03-24 21:58:16` | `cowrie.client.version` |
| `2026-03-24 21:58:16` | `cowrie.client.kex` |
| `2026-03-24 21:58:16` | `cowrie.login.success` |
| `2026-03-24 21:58:16` | `cowrie.session.params` |
| `2026-03-24 21:58:16` | `cowrie.command.input` |
| `2026-03-24 21:58:16` | `cowrie.command.failed` |
| `2026-03-24 21:58:16` | `cowrie.log.closed` |
| `2026-03-24 21:58:16` | `cowrie.session.params` |
| `2026-03-24 21:58:16` | `cowrie.command.input` |
| `2026-03-24 21:58:16` | `cowrie.session.file_download` |
| `2026-03-24 21:58:16` | `cowrie.log.closed` |
| `2026-03-24 21:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.178[.]0` to AbuseIPDB if not already reported
- [ ] Block `8.222.178[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bfce181fe2

| Field | Detail |
|---|---|
| **Source IP** | `8.222.178[.]0` |
| **First Seen** | 2026-03-24 21:58 |
| **Last Seen** | 2026-03-24 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 21:58:18` | `cowrie.session.connect` |
| `2026-03-24 21:58:18` | `cowrie.client.version` |
| `2026-03-24 21:58:18` | `cowrie.client.kex` |
| `2026-03-24 21:58:18` | `cowrie.login.success` |
| `2026-03-24 21:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.178[.]0` to AbuseIPDB if not already reported
- [ ] Block `8.222.178[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59743a5c0c6f

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-03-24 22:01 |
| **Last Seen** | 2026-03-24 22:01 |
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
| `2026-03-24 22:01:53` | `cowrie.session.connect` |
| `2026-03-24 22:01:53` | `cowrie.client.version` |
| `2026-03-24 22:01:53` | `cowrie.client.kex` |
| `2026-03-24 22:01:54` | `cowrie.login.success` |
| `2026-03-24 22:01:54` | `cowrie.session.params` |
| `2026-03-24 22:01:54` | `cowrie.command.input` |
| `2026-03-24 22:01:54` | `cowrie.command.failed` |
| `2026-03-24 22:01:54` | `cowrie.log.closed` |
| `2026-03-24 22:01:55` | `cowrie.session.params` |
| `2026-03-24 22:01:55` | `cowrie.command.input` |
| `2026-03-24 22:01:55` | `cowrie.session.file_download` |
| `2026-03-24 22:01:55` | `cowrie.log.closed` |
| `2026-03-24 22:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6817a7a0c526

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-03-24 22:01 |
| **Last Seen** | 2026-03-24 22:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 22:01:57` | `cowrie.session.connect` |
| `2026-03-24 22:01:57` | `cowrie.client.version` |
| `2026-03-24 22:01:57` | `cowrie.client.kex` |
| `2026-03-24 22:01:57` | `cowrie.login.success` |
| `2026-03-24 22:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.100.194[.]199` | **10** | 2026-03-24 20:51 | 2026-03-24 21:01 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.91.119[.]91` | **10** | 2026-03-24 21:45 | 2026-03-24 22:08 | 13m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.91.0[.]68` | **10** | 2026-03-24 21:45 | 2026-03-24 22:01 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.222.178[.]0` | **10** | 2026-03-24 21:47 | 2026-03-24 21:59 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.127[.]212` | **5** | 2026-03-24 20:39 | 2026-03-24 20:46 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `103.117.56[.]152` | 1 | 2026-03-24 21:42 | 2026-03-24 21:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.223.152[.]94` | 1 | 2026-03-24 21:22 | 2026-03-24 21:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.229[.]220` | 1 | 2026-03-24 22:21 | 2026-03-24 22:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.23.77[.]27` | 1 | 2026-03-24 20:45 | 2026-03-24 20:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.144[.]54` | 1 | 2026-03-24 22:03 | 2026-03-24 22:03 | 21s | 0 | `T1592` | 🟢 LOW |
| `210.104.42[.]40` | 1 | 2026-03-24 22:10 | 2026-03-24 22:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `221.148.201[.]226` | 1 | 2026-03-24 20:55 | 2026-03-24 20:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `50.217.40[.]11` | 1 | 2026-03-24 20:47 | 2026-03-24 20:47 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `221.148.201[.]226` | KR | Korea Telecom | **100** ⚠️ | 12 |
| `50.217.40[.]11` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 45 |
| `101.91.119[.]91` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 2 |
| `8.222.178[.]0` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |
| `122.187.229[.]220` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `14.23.77[.]27` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `210.104.42[.]40` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `101.36.127[.]212` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 0 |
| `117.223.152[.]94` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 0 |
| `34.91.0[.]68` | NL | Google LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 48 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 58 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (13.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 13 recon entry/entries in table (5 group(s) consolidating 45 session(s)).

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
_Report time: 2026-03-24T22:28:51Z_
