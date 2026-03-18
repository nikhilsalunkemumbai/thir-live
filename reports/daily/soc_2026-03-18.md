# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-18 |
| **Generated At** | 2026-03-18T07:00:20Z |
| **Shift Time** | 07:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **377** |
| Confirmed Threats | **219** |
| False Positives Filtered | **158** (41.9%) |
| Unique Attacker IPs | **80** |
| Countries of Origin | **22** |
| High Severity Cases | **45** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **332** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **248** |
| Unique Credential Pairs | **232** |
| Unique Usernames | **153** |
| Unique Passwords | **175** |
| Successful Auth Pairs | **45** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 47 |
| `ubuntu` | 12 |
| `admin` | 8 |
| `debian` | 5 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 26 |
| `12345678` | 8 |
| `password` | 6 |
| `1234` | 6 |
| `123` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `ubuntu` | 3 |
| `admin` | `admin` | 3 |
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `66666` | 2 |
| `root` | `1` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `147.189.161.77` | 2026-03-18T00:05:03 |
| `root` | `Admin1235` | `183.81.33.183` | 2026-03-18T00:08:28 |
| `root` | `66666` | `61.145.163.164` | 2026-03-18T00:09:57 |
| `root` | `66666` | `197.155.225.93` | 2026-03-18T00:10:11 |
| `root` | `admin@123` | `143.244.146.173` | 2026-03-18T00:13:54 |
| `root` | `1` | `143.244.146.173` | 2026-03-18T00:14:26 |
| `root` | `QWERTY123` | `143.244.146.173` | 2026-03-18T00:14:59 |
| `root` | `Pass@123` | `143.244.146.173` | 2026-03-18T00:15:18 |
| `root` | `!Q@W3e4r` | `143.244.146.173` | 2026-03-18T00:15:24 |
| `root` | `Admin1236` | `183.81.33.183` | 2026-03-18T00:24:25 |
| `root` | `Admin1237` | `183.81.33.183` | 2026-03-18T00:41:56 |
| `root` | `server123` | `120.48.174.68` | 2026-03-18T00:43:29 |
| `root` | `Admin1238` | `183.81.33.183` | 2026-03-18T00:58:35 |
| `root` | `admin` | `116.110.23.141` | 2026-03-18T01:02:08 |
| `root` | `Admin1239` | `183.81.33.183` | 2026-03-18T01:14:32 |
| `root` | `Admin12310` | `183.81.33.183` | 2026-03-18T01:30:07 |
| `root` | `explorer` | `116.110.156.14` | 2026-03-18T01:32:28 |
| `root` | `Admin12340` | `183.81.33.183` | 2026-03-18T01:47:37 |
| `root` | `a1s2d3f4` | `137.184.78.9` | 2026-03-18T02:03:40 |
| `root` | `Qq123456` | `137.184.78.9` | 2026-03-18T02:03:53 |
| `root` | `!QAZ2wsx` | `137.184.78.9` | 2026-03-18T02:04:07 |
| `root` | `root12345` | `137.184.78.9` | 2026-03-18T02:04:47 |
| `root` | `passwd` | `137.184.78.9` | 2026-03-18T02:05:07 |
| `root` | `123321` | `137.184.78.9` | 2026-03-18T02:05:27 |
| `root` | `Aa123456.` | `137.184.78.9` | 2026-03-18T02:06:06 |
| `root` | `Abc123456` | `137.184.78.9` | 2026-03-18T02:06:26 |
| `root` | `201314` | `101.36.106.113` | 2026-03-18T03:24:41 |
| `root` | `3245gs5662d34` | `101.36.106.113` | 2026-03-18T03:24:44 |
| `root` | `ubuntu` | `219.153.106.29` | 2026-03-18T04:12:51 |
| `root` | `qwer!234` | `180.76.245.60` | 2026-03-18T05:04:43 |
| `root` | `lj123456` | `103.7.41.144` | 2026-03-18T06:12:24 |
| `root` | `3245gs5662d34` | `103.7.41.144` | 2026-03-18T06:12:27 |
| `root` | `QWERTY123` | `174.138.33.218` | 2026-03-18T06:41:35 |
| `root` | `1` | `174.138.33.218` | 2026-03-18T06:41:48 |
| `root` | `12345678` | `174.138.33.218` | 2026-03-18T06:42:14 |
| `root` | `P@ssw0rd2026` | `174.138.33.218` | 2026-03-18T06:42:39 |
| `root` | `root@2026` | `174.138.33.218` | 2026-03-18T06:42:52 |
| `root` | `redhat` | `174.138.33.218` | 2026-03-18T06:43:43 |
| `root` | `qazwsx123` | `174.138.33.218` | 2026-03-18T06:44:09 |
| `root` | `Admin123` | `174.138.33.218` | 2026-03-18T06:44:27 |
| `root` | `11` | `174.138.33.218` | 2026-03-18T06:44:53 |
| `root` | `Qwerty1` | `174.138.33.218` | 2026-03-18T06:45:05 |
| `root` | `Password` | `174.138.33.218` | 2026-03-18T06:45:49 |
| `root` | `eve` | `174.138.33.218` | 2026-03-18T06:47:05 |
| `root` | `ubuntu` | `41.111.172.2` | 2026-03-18T06:54:08 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **80** |
| Unique ASNs | **49** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS24086` | Viettel Corporation | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | MEDIUM |
| `AS3462` | Data Communication Business Group | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-25521f2b759a

| Field | Detail |
|---|---|
| **Source IP** | `147.189.161[.]77` |
| **First Seen** | 2026-03-18 00:05 |
| **Last Seen** | 2026-03-18 00:06 |
| **Session Duration** | 84s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:05:02` | `cowrie.session.connect` |
| `2026-03-18 00:05:02` | `cowrie.client.version` |
| `2026-03-18 00:05:02` | `cowrie.client.kex` |
| `2026-03-18 00:05:03` | `cowrie.login.success` |
| `2026-03-18 00:06:26` | `cowrie.session.file_upload` |
| `2026-03-18 00:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.189.161[.]77` to AbuseIPDB if not already reported
- [ ] Block `147.189.161[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-302d3f42333b

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-18 00:08 |
| **Last Seen** | 2026-03-18 00:08 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:08:05` | `cowrie.session.connect` |
| `2026-03-18 00:08:08` | `cowrie.client.version` |
| `2026-03-18 00:08:08` | `cowrie.client.kex` |
| `2026-03-18 00:08:28` | `cowrie.login.success` |
| `2026-03-18 00:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb05403c6f3

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-03-18 00:09 |
| **Last Seen** | 2026-03-18 00:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:09:54` | `cowrie.session.connect` |
| `2026-03-18 00:09:55` | `cowrie.client.version` |
| `2026-03-18 00:09:55` | `cowrie.client.kex` |
| `2026-03-18 00:09:57` | `cowrie.login.success` |
| `2026-03-18 00:09:58` | `cowrie.direct-tcpip.request` |
| `2026-03-18 00:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9aa6510c92

| Field | Detail |
|---|---|
| **Source IP** | `197.155.225[.]93` |
| **First Seen** | 2026-03-18 00:10 |
| **Last Seen** | 2026-03-18 00:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:10:08` | `cowrie.session.connect` |
| `2026-03-18 00:10:09` | `cowrie.client.version` |
| `2026-03-18 00:10:09` | `cowrie.client.kex` |
| `2026-03-18 00:10:11` | `cowrie.login.success` |
| `2026-03-18 00:10:12` | `cowrie.direct-tcpip.request` |
| `2026-03-18 00:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.155.225[.]93` to AbuseIPDB if not already reported
- [ ] Block `197.155.225[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381287b8076d

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-18 00:24 |
| **Last Seen** | 2026-03-18 00:24 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:24:12` | `cowrie.session.connect` |
| `2026-03-18 00:24:15` | `cowrie.client.version` |
| `2026-03-18 00:24:15` | `cowrie.client.kex` |
| `2026-03-18 00:24:25` | `cowrie.login.success` |
| `2026-03-18 00:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5527602aed0

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-18 00:41 |
| **Last Seen** | 2026-03-18 00:41 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:41:29` | `cowrie.session.connect` |
| `2026-03-18 00:41:34` | `cowrie.client.version` |
| `2026-03-18 00:41:34` | `cowrie.client.kex` |
| `2026-03-18 00:41:56` | `cowrie.login.success` |
| `2026-03-18 00:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6daeefdcc162

| Field | Detail |
|---|---|
| **Source IP** | `120.48.174[.]68` |
| **First Seen** | 2026-03-18 00:43 |
| **Last Seen** | 2026-03-18 00:45 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:G2FwhsquDwpq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:43:27` | `cowrie.session.connect` |
| `2026-03-18 00:43:27` | `cowrie.client.version` |
| `2026-03-18 00:43:27` | `cowrie.client.kex` |
| `2026-03-18 00:43:29` | `cowrie.login.success` |
| `2026-03-18 00:43:30` | `cowrie.session.params` |
| `2026-03-18 00:43:30` | `cowrie.command.input` |
| `2026-03-18 00:43:30` | `cowrie.command.failed` |
| `2026-03-18 00:43:31` | `cowrie.log.closed` |
| `2026-03-18 00:43:34` | `cowrie.session.params` |
| `2026-03-18 00:43:34` | `cowrie.command.input` |
| `2026-03-18 00:43:35` | `cowrie.session.file_download` |
| `2026-03-18 00:43:35` | `cowrie.log.closed` |
| `2026-03-18 00:43:51` | `cowrie.session.params` |
| `2026-03-18 00:43:51` | `cowrie.command.input` |
| `2026-03-18 00:43:52` | `cowrie.log.closed` |
| `2026-03-18 00:43:55` | `cowrie.session.params` |
| `2026-03-18 00:43:55` | `cowrie.command.input` |
| `2026-03-18 00:43:55` | `cowrie.log.closed` |
| `2026-03-18 00:43:56` | `cowrie.session.params` |
| `2026-03-18 00:43:56` | `cowrie.command.input` |
| `2026-03-18 00:43:58` | `cowrie.session.file_download` |
| `2026-03-18 00:43:58` | `cowrie.log.closed` |
| `2026-03-18 00:44:02` | `cowrie.session.params` |
| `2026-03-18 00:44:02` | `cowrie.command.input` |
| `2026-03-18 00:44:09` | `cowrie.log.closed` |
| `2026-03-18 00:44:10` | `cowrie.session.params` |
| `2026-03-18 00:44:10` | `cowrie.command.input` |
| `2026-03-18 00:44:10` | `cowrie.log.closed` |
| `2026-03-18 00:44:20` | `cowrie.session.params` |
| `2026-03-18 00:44:20` | `cowrie.command.input` |
| `2026-03-18 00:44:35` | `cowrie.log.closed` |
| `2026-03-18 00:44:37` | `cowrie.session.params` |
| `2026-03-18 00:44:37` | `cowrie.command.input` |
| `2026-03-18 00:44:39` | `cowrie.log.closed` |
| `2026-03-18 00:44:40` | `cowrie.session.params` |
| `2026-03-18 00:44:40` | `cowrie.command.input` |
| `2026-03-18 00:44:40` | `cowrie.log.closed` |
| `2026-03-18 00:44:43` | `cowrie.session.params` |
| `2026-03-18 00:44:43` | `cowrie.command.input` |
| `2026-03-18 00:44:44` | `cowrie.log.closed` |
| `2026-03-18 00:44:44` | `cowrie.session.params` |
| `2026-03-18 00:44:44` | `cowrie.command.input` |
| `2026-03-18 00:44:45` | `cowrie.log.closed` |
| `2026-03-18 00:44:47` | `cowrie.session.params` |
| `2026-03-18 00:44:47` | `cowrie.command.input` |
| `2026-03-18 00:44:51` | `cowrie.log.closed` |
| `2026-03-18 00:45:00` | `cowrie.session.params` |
| `2026-03-18 00:45:00` | `cowrie.command.input` |
| `2026-03-18 00:45:00` | `cowrie.log.closed` |
| `2026-03-18 00:45:02` | `cowrie.session.params` |
| `2026-03-18 00:45:02` | `cowrie.command.input` |
| `2026-03-18 00:45:08` | `cowrie.log.closed` |
| `2026-03-18 00:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.174[.]68` to AbuseIPDB if not already reported
- [ ] Block `120.48.174[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b5dee6914c

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-18 00:58 |
| **Last Seen** | 2026-03-18 00:58 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 00:58:09` | `cowrie.session.connect` |
| `2026-03-18 00:58:13` | `cowrie.client.version` |
| `2026-03-18 00:58:13` | `cowrie.client.kex` |
| `2026-03-18 00:58:35` | `cowrie.login.success` |
| `2026-03-18 00:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5886e1c77d

| Field | Detail |
|---|---|
| **Source IP** | `116.110.23[.]141` |
| **First Seen** | 2026-03-18 01:02 |
| **Last Seen** | 2026-03-18 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 01:02:07` | `cowrie.session.connect` |
| `2026-03-18 01:02:07` | `cowrie.client.version` |
| `2026-03-18 01:02:07` | `cowrie.client.kex` |
| `2026-03-18 01:02:08` | `cowrie.login.success` |
| `2026-03-18 01:02:08` | `cowrie.direct-tcpip.request` |
| `2026-03-18 01:02:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-03-18 01:02:08` | `cowrie.direct-tcpip.data` |
| `2026-03-18 01:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.23[.]141` to AbuseIPDB if not already reported
- [ ] Block `116.110.23[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e8d93f0c3c

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-18 01:14 |
| **Last Seen** | 2026-03-18 01:14 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 01:14:08` | `cowrie.session.connect` |
| `2026-03-18 01:14:11` | `cowrie.client.version` |
| `2026-03-18 01:14:11` | `cowrie.client.kex` |
| `2026-03-18 01:14:32` | `cowrie.login.success` |
| `2026-03-18 01:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62fea7e25a4

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-18 01:29 |
| **Last Seen** | 2026-03-18 01:30 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 01:29:40` | `cowrie.session.connect` |
| `2026-03-18 01:29:45` | `cowrie.client.version` |
| `2026-03-18 01:29:45` | `cowrie.client.kex` |
| `2026-03-18 01:30:07` | `cowrie.login.success` |
| `2026-03-18 01:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fe673154ac

| Field | Detail |
|---|---|
| **Source IP** | `116.110.156[.]14` |
| **First Seen** | 2026-03-18 01:32 |
| **Last Seen** | 2026-03-18 01:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 01:32:28` | `cowrie.session.connect` |
| `2026-03-18 01:32:28` | `cowrie.client.version` |
| `2026-03-18 01:32:28` | `cowrie.client.kex` |
| `2026-03-18 01:32:28` | `cowrie.login.success` |
| `2026-03-18 01:32:29` | `cowrie.direct-tcpip.request` |
| `2026-03-18 01:32:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-03-18 01:32:30` | `cowrie.direct-tcpip.data` |
| `2026-03-18 01:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.156[.]14` to AbuseIPDB if not already reported
- [ ] Block `116.110.156[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0db12a4af91

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-18 01:47 |
| **Last Seen** | 2026-03-18 01:47 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 01:47:11` | `cowrie.session.connect` |
| `2026-03-18 01:47:15` | `cowrie.client.version` |
| `2026-03-18 01:47:15` | `cowrie.client.kex` |
| `2026-03-18 01:47:37` | `cowrie.login.success` |
| `2026-03-18 01:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a454ad72f58

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:03 |
| **Last Seen** | 2026-03-18 02:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:03:39` | `cowrie.session.connect` |
| `2026-03-18 02:03:39` | `cowrie.client.version` |
| `2026-03-18 02:03:39` | `cowrie.client.kex` |
| `2026-03-18 02:03:40` | `cowrie.login.success` |
| `2026-03-18 02:03:41` | `cowrie.session.params` |
| `2026-03-18 02:03:41` | `cowrie.command.input` |
| `2026-03-18 02:03:41` | `cowrie.log.closed` |
| `2026-03-18 02:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e7747ec2b7

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:03 |
| **Last Seen** | 2026-03-18 02:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:03:52` | `cowrie.session.connect` |
| `2026-03-18 02:03:52` | `cowrie.client.version` |
| `2026-03-18 02:03:53` | `cowrie.client.kex` |
| `2026-03-18 02:03:53` | `cowrie.login.success` |
| `2026-03-18 02:03:54` | `cowrie.session.params` |
| `2026-03-18 02:03:54` | `cowrie.command.input` |
| `2026-03-18 02:03:54` | `cowrie.log.closed` |
| `2026-03-18 02:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb3a9165544

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:04 |
| **Last Seen** | 2026-03-18 02:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:04:06` | `cowrie.session.connect` |
| `2026-03-18 02:04:06` | `cowrie.client.version` |
| `2026-03-18 02:04:06` | `cowrie.client.kex` |
| `2026-03-18 02:04:07` | `cowrie.login.success` |
| `2026-03-18 02:04:07` | `cowrie.session.params` |
| `2026-03-18 02:04:07` | `cowrie.command.input` |
| `2026-03-18 02:04:07` | `cowrie.log.closed` |
| `2026-03-18 02:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d465b4a154eb

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:04 |
| **Last Seen** | 2026-03-18 02:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:04:46` | `cowrie.session.connect` |
| `2026-03-18 02:04:46` | `cowrie.client.version` |
| `2026-03-18 02:04:46` | `cowrie.client.kex` |
| `2026-03-18 02:04:47` | `cowrie.login.success` |
| `2026-03-18 02:04:47` | `cowrie.session.params` |
| `2026-03-18 02:04:47` | `cowrie.command.input` |
| `2026-03-18 02:04:47` | `cowrie.log.closed` |
| `2026-03-18 02:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c40e2a90ed6

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:05 |
| **Last Seen** | 2026-03-18 02:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:05:06` | `cowrie.session.connect` |
| `2026-03-18 02:05:06` | `cowrie.client.version` |
| `2026-03-18 02:05:06` | `cowrie.client.kex` |
| `2026-03-18 02:05:07` | `cowrie.login.success` |
| `2026-03-18 02:05:07` | `cowrie.session.params` |
| `2026-03-18 02:05:07` | `cowrie.command.input` |
| `2026-03-18 02:05:07` | `cowrie.log.closed` |
| `2026-03-18 02:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78804cbd9cce

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:05 |
| **Last Seen** | 2026-03-18 02:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:05:26` | `cowrie.session.connect` |
| `2026-03-18 02:05:26` | `cowrie.client.version` |
| `2026-03-18 02:05:26` | `cowrie.client.kex` |
| `2026-03-18 02:05:27` | `cowrie.login.success` |
| `2026-03-18 02:05:27` | `cowrie.session.params` |
| `2026-03-18 02:05:27` | `cowrie.command.input` |
| `2026-03-18 02:05:27` | `cowrie.log.closed` |
| `2026-03-18 02:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0f8530f2dd

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:06 |
| **Last Seen** | 2026-03-18 02:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:06:05` | `cowrie.session.connect` |
| `2026-03-18 02:06:05` | `cowrie.client.version` |
| `2026-03-18 02:06:06` | `cowrie.client.kex` |
| `2026-03-18 02:06:06` | `cowrie.login.success` |
| `2026-03-18 02:06:07` | `cowrie.session.params` |
| `2026-03-18 02:06:07` | `cowrie.command.input` |
| `2026-03-18 02:06:07` | `cowrie.log.closed` |
| `2026-03-18 02:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5586a9e1ec90

| Field | Detail |
|---|---|
| **Source IP** | `137.184.78[.]9` |
| **First Seen** | 2026-03-18 02:06 |
| **Last Seen** | 2026-03-18 02:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 02:06:25` | `cowrie.session.connect` |
| `2026-03-18 02:06:25` | `cowrie.client.version` |
| `2026-03-18 02:06:25` | `cowrie.client.kex` |
| `2026-03-18 02:06:26` | `cowrie.login.success` |
| `2026-03-18 02:06:26` | `cowrie.session.params` |
| `2026-03-18 02:06:26` | `cowrie.command.input` |
| `2026-03-18 02:06:27` | `cowrie.log.closed` |
| `2026-03-18 02:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.78[.]9` to AbuseIPDB if not already reported
- [ ] Block `137.184.78[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864124fd55d5

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-18 03:24 |
| **Last Seen** | 2026-03-18 03:24 |
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
| `2026-03-18 03:24:40` | `cowrie.session.connect` |
| `2026-03-18 03:24:40` | `cowrie.client.version` |
| `2026-03-18 03:24:40` | `cowrie.client.kex` |
| `2026-03-18 03:24:41` | `cowrie.login.success` |
| `2026-03-18 03:24:41` | `cowrie.session.params` |
| `2026-03-18 03:24:41` | `cowrie.command.input` |
| `2026-03-18 03:24:41` | `cowrie.command.failed` |
| `2026-03-18 03:24:41` | `cowrie.log.closed` |
| `2026-03-18 03:24:42` | `cowrie.session.params` |
| `2026-03-18 03:24:42` | `cowrie.command.input` |
| `2026-03-18 03:24:42` | `cowrie.session.file_download` |
| `2026-03-18 03:24:42` | `cowrie.log.closed` |
| `2026-03-18 03:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c51fa89fe96

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-18 03:24 |
| **Last Seen** | 2026-03-18 03:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 03:24:44` | `cowrie.session.connect` |
| `2026-03-18 03:24:44` | `cowrie.client.version` |
| `2026-03-18 03:24:44` | `cowrie.client.kex` |
| `2026-03-18 03:24:44` | `cowrie.login.success` |
| `2026-03-18 03:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6040826e229b

| Field | Detail |
|---|---|
| **Source IP** | `219.153.106[.]29` |
| **First Seen** | 2026-03-18 04:12 |
| **Last Seen** | 2026-03-18 04:17 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 04:12:49` | `cowrie.session.connect` |
| `2026-03-18 04:12:49` | `cowrie.client.version` |
| `2026-03-18 04:12:49` | `cowrie.client.kex` |
| `2026-03-18 04:12:51` | `cowrie.login.success` |
| `2026-03-18 04:17:51` | `cowrie.session.file_upload` |
| `2026-03-18 04:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.153.106[.]29` to AbuseIPDB if not already reported
- [ ] Block `219.153.106[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1977f0c72a9c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.245[.]60` |
| **First Seen** | 2026-03-18 05:04 |
| **Last Seen** | 2026-03-18 05:05 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:z3pRNDK6cVqs"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 05:04:40` | `cowrie.session.connect` |
| `2026-03-18 05:04:40` | `cowrie.client.version` |
| `2026-03-18 05:04:41` | `cowrie.client.kex` |
| `2026-03-18 05:04:43` | `cowrie.login.success` |
| `2026-03-18 05:04:43` | `cowrie.session.params` |
| `2026-03-18 05:04:43` | `cowrie.command.input` |
| `2026-03-18 05:04:43` | `cowrie.command.failed` |
| `2026-03-18 05:04:44` | `cowrie.log.closed` |
| `2026-03-18 05:04:44` | `cowrie.session.params` |
| `2026-03-18 05:04:44` | `cowrie.command.input` |
| `2026-03-18 05:04:45` | `cowrie.session.file_download` |
| `2026-03-18 05:04:45` | `cowrie.log.closed` |
| `2026-03-18 05:04:59` | `cowrie.session.params` |
| `2026-03-18 05:04:59` | `cowrie.command.input` |
| `2026-03-18 05:05:00` | `cowrie.log.closed` |
| `2026-03-18 05:05:01` | `cowrie.session.params` |
| `2026-03-18 05:05:01` | `cowrie.command.input` |
| `2026-03-18 05:05:01` | `cowrie.log.closed` |
| `2026-03-18 05:05:02` | `cowrie.session.params` |
| `2026-03-18 05:05:02` | `cowrie.command.input` |
| `2026-03-18 05:05:02` | `cowrie.session.file_download` |
| `2026-03-18 05:05:02` | `cowrie.log.closed` |
| `2026-03-18 05:05:03` | `cowrie.session.params` |
| `2026-03-18 05:05:03` | `cowrie.command.input` |
| `2026-03-18 05:05:04` | `cowrie.log.closed` |
| `2026-03-18 05:05:06` | `cowrie.session.params` |
| `2026-03-18 05:05:06` | `cowrie.command.input` |
| `2026-03-18 05:05:07` | `cowrie.log.closed` |
| `2026-03-18 05:05:07` | `cowrie.session.params` |
| `2026-03-18 05:05:07` | `cowrie.command.input` |
| `2026-03-18 05:05:07` | `cowrie.command.input` |
| `2026-03-18 05:05:08` | `cowrie.log.closed` |
| `2026-03-18 05:05:09` | `cowrie.session.params` |
| `2026-03-18 05:05:09` | `cowrie.command.input` |
| `2026-03-18 05:05:09` | `cowrie.log.closed` |
| `2026-03-18 05:05:13` | `cowrie.session.params` |
| `2026-03-18 05:05:13` | `cowrie.command.input` |
| `2026-03-18 05:05:13` | `cowrie.log.closed` |
| `2026-03-18 05:05:14` | `cowrie.session.params` |
| `2026-03-18 05:05:14` | `cowrie.command.input` |
| `2026-03-18 05:05:14` | `cowrie.log.closed` |
| `2026-03-18 05:05:14` | `cowrie.session.params` |
| `2026-03-18 05:05:14` | `cowrie.command.input` |
| `2026-03-18 05:05:15` | `cowrie.log.closed` |
| `2026-03-18 05:05:15` | `cowrie.session.params` |
| `2026-03-18 05:05:15` | `cowrie.command.input` |
| `2026-03-18 05:05:15` | `cowrie.log.closed` |
| `2026-03-18 05:05:16` | `cowrie.session.params` |
| `2026-03-18 05:05:16` | `cowrie.command.input` |
| `2026-03-18 05:05:16` | `cowrie.log.closed` |
| `2026-03-18 05:05:17` | `cowrie.session.params` |
| `2026-03-18 05:05:17` | `cowrie.command.input` |
| `2026-03-18 05:05:17` | `cowrie.log.closed` |
| `2026-03-18 05:05:18` | `cowrie.session.params` |
| `2026-03-18 05:05:18` | `cowrie.command.input` |
| `2026-03-18 05:05:18` | `cowrie.log.closed` |
| `2026-03-18 05:05:19` | `cowrie.session.params` |
| `2026-03-18 05:05:19` | `cowrie.command.input` |
| `2026-03-18 05:05:21` | `cowrie.log.closed` |
| `2026-03-18 05:05:21` | `cowrie.session.params` |
| `2026-03-18 05:05:21` | `cowrie.command.input` |
| `2026-03-18 05:05:22` | `cowrie.log.closed` |
| `2026-03-18 05:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.245[.]60` to AbuseIPDB if not already reported
- [ ] Block `180.76.245[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6e52c3fe26

| Field | Detail |
|---|---|
| **Source IP** | `103.7.41[.]144` |
| **First Seen** | 2026-03-18 06:12 |
| **Last Seen** | 2026-03-18 06:12 |
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
| `2026-03-18 06:12:24` | `cowrie.session.connect` |
| `2026-03-18 06:12:24` | `cowrie.client.version` |
| `2026-03-18 06:12:24` | `cowrie.client.kex` |
| `2026-03-18 06:12:24` | `cowrie.login.success` |
| `2026-03-18 06:12:24` | `cowrie.session.params` |
| `2026-03-18 06:12:24` | `cowrie.command.input` |
| `2026-03-18 06:12:24` | `cowrie.command.failed` |
| `2026-03-18 06:12:24` | `cowrie.log.closed` |
| `2026-03-18 06:12:25` | `cowrie.session.params` |
| `2026-03-18 06:12:25` | `cowrie.command.input` |
| `2026-03-18 06:12:25` | `cowrie.session.file_download` |
| `2026-03-18 06:12:25` | `cowrie.log.closed` |
| `2026-03-18 06:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.7.41[.]144` to AbuseIPDB if not already reported
- [ ] Block `103.7.41[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe6cda7aaa0

| Field | Detail |
|---|---|
| **Source IP** | `103.7.41[.]144` |
| **First Seen** | 2026-03-18 06:12 |
| **Last Seen** | 2026-03-18 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:12:27` | `cowrie.session.connect` |
| `2026-03-18 06:12:27` | `cowrie.client.version` |
| `2026-03-18 06:12:27` | `cowrie.client.kex` |
| `2026-03-18 06:12:27` | `cowrie.login.success` |
| `2026-03-18 06:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.7.41[.]144` to AbuseIPDB if not already reported
- [ ] Block `103.7.41[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ceb973446bf

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:41 |
| **Last Seen** | 2026-03-18 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:41:34` | `cowrie.session.connect` |
| `2026-03-18 06:41:34` | `cowrie.client.version` |
| `2026-03-18 06:41:35` | `cowrie.client.kex` |
| `2026-03-18 06:41:35` | `cowrie.login.success` |
| `2026-03-18 06:41:36` | `cowrie.session.params` |
| `2026-03-18 06:41:36` | `cowrie.command.input` |
| `2026-03-18 06:41:36` | `cowrie.log.closed` |
| `2026-03-18 06:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a912c2b3248f

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:41 |
| **Last Seen** | 2026-03-18 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:41:47` | `cowrie.session.connect` |
| `2026-03-18 06:41:47` | `cowrie.client.version` |
| `2026-03-18 06:41:47` | `cowrie.client.kex` |
| `2026-03-18 06:41:48` | `cowrie.login.success` |
| `2026-03-18 06:41:49` | `cowrie.session.params` |
| `2026-03-18 06:41:49` | `cowrie.command.input` |
| `2026-03-18 06:41:49` | `cowrie.log.closed` |
| `2026-03-18 06:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65bf9cf6a312

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:42 |
| **Last Seen** | 2026-03-18 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:42:13` | `cowrie.session.connect` |
| `2026-03-18 06:42:13` | `cowrie.client.version` |
| `2026-03-18 06:42:13` | `cowrie.client.kex` |
| `2026-03-18 06:42:14` | `cowrie.login.success` |
| `2026-03-18 06:42:14` | `cowrie.session.params` |
| `2026-03-18 06:42:14` | `cowrie.command.input` |
| `2026-03-18 06:42:14` | `cowrie.log.closed` |
| `2026-03-18 06:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad150abfdc16

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:42 |
| **Last Seen** | 2026-03-18 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:42:38` | `cowrie.session.connect` |
| `2026-03-18 06:42:38` | `cowrie.client.version` |
| `2026-03-18 06:42:39` | `cowrie.client.kex` |
| `2026-03-18 06:42:39` | `cowrie.login.success` |
| `2026-03-18 06:42:40` | `cowrie.session.params` |
| `2026-03-18 06:42:40` | `cowrie.command.input` |
| `2026-03-18 06:42:40` | `cowrie.log.closed` |
| `2026-03-18 06:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d20828a9d6a

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:42 |
| **Last Seen** | 2026-03-18 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:42:51` | `cowrie.session.connect` |
| `2026-03-18 06:42:51` | `cowrie.client.version` |
| `2026-03-18 06:42:52` | `cowrie.client.kex` |
| `2026-03-18 06:42:52` | `cowrie.login.success` |
| `2026-03-18 06:42:53` | `cowrie.session.params` |
| `2026-03-18 06:42:53` | `cowrie.command.input` |
| `2026-03-18 06:42:53` | `cowrie.log.closed` |
| `2026-03-18 06:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df572643577

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:43 |
| **Last Seen** | 2026-03-18 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:43:42` | `cowrie.session.connect` |
| `2026-03-18 06:43:42` | `cowrie.client.version` |
| `2026-03-18 06:43:43` | `cowrie.client.kex` |
| `2026-03-18 06:43:43` | `cowrie.login.success` |
| `2026-03-18 06:43:44` | `cowrie.session.params` |
| `2026-03-18 06:43:44` | `cowrie.command.input` |
| `2026-03-18 06:43:44` | `cowrie.log.closed` |
| `2026-03-18 06:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-affeb3078c32

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:44 |
| **Last Seen** | 2026-03-18 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:44:08` | `cowrie.session.connect` |
| `2026-03-18 06:44:08` | `cowrie.client.version` |
| `2026-03-18 06:44:08` | `cowrie.client.kex` |
| `2026-03-18 06:44:09` | `cowrie.login.success` |
| `2026-03-18 06:44:09` | `cowrie.session.params` |
| `2026-03-18 06:44:09` | `cowrie.command.input` |
| `2026-03-18 06:44:09` | `cowrie.log.closed` |
| `2026-03-18 06:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21ed1e4d029

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:44 |
| **Last Seen** | 2026-03-18 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:44:27` | `cowrie.session.connect` |
| `2026-03-18 06:44:27` | `cowrie.client.version` |
| `2026-03-18 06:44:27` | `cowrie.client.kex` |
| `2026-03-18 06:44:27` | `cowrie.login.success` |
| `2026-03-18 06:44:28` | `cowrie.session.params` |
| `2026-03-18 06:44:28` | `cowrie.command.input` |
| `2026-03-18 06:44:28` | `cowrie.log.closed` |
| `2026-03-18 06:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0701392774

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:44 |
| **Last Seen** | 2026-03-18 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:44:52` | `cowrie.session.connect` |
| `2026-03-18 06:44:52` | `cowrie.client.version` |
| `2026-03-18 06:44:52` | `cowrie.client.kex` |
| `2026-03-18 06:44:53` | `cowrie.login.success` |
| `2026-03-18 06:44:53` | `cowrie.session.params` |
| `2026-03-18 06:44:53` | `cowrie.command.input` |
| `2026-03-18 06:44:53` | `cowrie.log.closed` |
| `2026-03-18 06:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c54a08cd654

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:45 |
| **Last Seen** | 2026-03-18 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:45:04` | `cowrie.session.connect` |
| `2026-03-18 06:45:04` | `cowrie.client.version` |
| `2026-03-18 06:45:05` | `cowrie.client.kex` |
| `2026-03-18 06:45:05` | `cowrie.login.success` |
| `2026-03-18 06:45:06` | `cowrie.session.params` |
| `2026-03-18 06:45:06` | `cowrie.command.input` |
| `2026-03-18 06:45:06` | `cowrie.log.closed` |
| `2026-03-18 06:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9442568e172

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:45 |
| **Last Seen** | 2026-03-18 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:45:48` | `cowrie.session.connect` |
| `2026-03-18 06:45:48` | `cowrie.client.version` |
| `2026-03-18 06:45:49` | `cowrie.client.kex` |
| `2026-03-18 06:45:49` | `cowrie.login.success` |
| `2026-03-18 06:45:50` | `cowrie.session.params` |
| `2026-03-18 06:45:50` | `cowrie.command.input` |
| `2026-03-18 06:45:50` | `cowrie.log.closed` |
| `2026-03-18 06:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b15f7445174

| Field | Detail |
|---|---|
| **Source IP** | `174.138.33[.]218` |
| **First Seen** | 2026-03-18 06:47 |
| **Last Seen** | 2026-03-18 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:47:04` | `cowrie.session.connect` |
| `2026-03-18 06:47:04` | `cowrie.client.version` |
| `2026-03-18 06:47:05` | `cowrie.client.kex` |
| `2026-03-18 06:47:05` | `cowrie.login.success` |
| `2026-03-18 06:47:06` | `cowrie.session.params` |
| `2026-03-18 06:47:06` | `cowrie.command.input` |
| `2026-03-18 06:47:06` | `cowrie.log.closed` |
| `2026-03-18 06:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.138.33[.]218` to AbuseIPDB if not already reported
- [ ] Block `174.138.33[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0242707abb62

| Field | Detail |
|---|---|
| **Source IP** | `41.111.172[.]2` |
| **First Seen** | 2026-03-18 06:54 |
| **Last Seen** | 2026-03-18 06:54 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 06:54:08` | `cowrie.session.connect` |
| `2026-03-18 06:54:08` | `cowrie.client.version` |
| `2026-03-18 06:54:08` | `cowrie.client.kex` |
| `2026-03-18 06:54:08` | `cowrie.login.success` |
| `2026-03-18 06:54:57` | `cowrie.session.file_upload` |
| `2026-03-18 06:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.172[.]2` to AbuseIPDB if not already reported
- [ ] Block `41.111.172[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.255.26[.]45` | **25** | 2026-03-18 05:16 | 2026-03-18 05:22 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.7.41[.]144` | **15** | 2026-03-18 06:09 | 2026-03-18 06:16 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.176.182[.]178` | **15** | 2026-03-18 01:36 | 2026-03-18 02:09 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.174[.]68` | **14** | 2026-03-18 00:23 | 2026-03-18 01:11 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `180.76.245[.]60` | **14** | 2026-03-18 04:47 | 2026-03-18 05:06 | 15m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.88[.]251` | **12** | 2026-03-18 04:54 | 2026-03-18 05:14 | 20m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.106[.]113` | **10** | 2026-03-18 03:13 | 2026-03-18 03:34 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.93[.]214` | **10** | 2026-03-18 06:11 | 2026-03-18 06:17 | 12m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.81.33[.]183` | **7** | 2026-03-18 00:00 | 2026-03-18 01:38 | 3m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `3.129.187[.]38` | **6** | 2026-03-18 03:40 | 2026-03-18 03:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.97[.]70` | **4** | 2026-03-18 04:22 | 2026-03-18 04:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.110.144[.]156` | **3** | 2026-03-18 01:00 | 2026-03-18 01:06 | 1m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.23[.]141` | **3** | 2026-03-18 01:02 | 2026-03-18 01:05 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `117.2.49[.]125` | **3** | 2026-03-18 03:20 | 2026-03-18 03:24 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `20.80.104[.]232` | **2** | 2026-03-18 03:33 | 2026-03-18 03:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.71.39[.]17` | 1 | 2026-03-18 06:17 | 2026-03-18 06:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.93.37[.]178` | 1 | 2026-03-18 05:48 | 2026-03-18 05:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.184.45[.]204` | 1 | 2026-03-18 06:27 | 2026-03-18 06:27 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-03-18 01:52 | 2026-03-18 01:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.4.79[.]138` | 1 | 2026-03-18 01:40 | 2026-03-18 01:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.193.187[.]154` | 1 | 2026-03-18 05:57 | 2026-03-18 05:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.33.44[.]32` | 1 | 2026-03-18 05:10 | 2026-03-18 05:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `116.110.148[.]145` | 1 | 2026-03-18 01:32 | 2026-03-18 01:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.160.131[.]100` | 1 | 2026-03-18 05:10 | 2026-03-18 05:12 | 116s | 0 | `T1592` | 🟢 LOW |
| `117.50.51[.]119` | 1 | 2026-03-18 01:18 | 2026-03-18 01:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-03-18 04:47 | 2026-03-18 04:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-18 04:53 | 2026-03-18 04:53 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.198.96[.]190` | 1 | 2026-03-18 02:59 | 2026-03-18 02:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.196.27[.]240` | 1 | 2026-03-18 04:16 | 2026-03-18 04:18 | 81s | 0 | `T1592` | 🟢 LOW |
| `125.19.156[.]46` | 1 | 2026-03-18 01:58 | 2026-03-18 01:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.208.17[.]16` | 1 | 2026-03-18 01:21 | 2026-03-18 01:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-03-18 06:56 | 2026-03-18 06:56 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `161.142.238[.]29` | 1 | 2026-03-18 02:24 | 2026-03-18 02:24 | 31s | 0 | `T1592` | 🟢 LOW |
| `165.22.78[.]143` | 1 | 2026-03-18 02:55 | 2026-03-18 02:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.206.113[.]91` | 1 | 2026-03-18 04:34 | 2026-03-18 04:34 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.227[.]77` | 1 | 2026-03-18 03:55 | 2026-03-18 03:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.212.86[.]140` | 1 | 2026-03-18 01:25 | 2026-03-18 01:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-03-18 01:46 | 2026-03-18 01:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]181` | 1 | 2026-03-18 04:00 | 2026-03-18 04:00 | 15s | 0 | `T1592` | 🟢 LOW |
| `183.93.165[.]103` | 1 | 2026-03-18 03:15 | 2026-03-18 03:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-03-18 02:18 | 2026-03-18 02:18 | 35s | 0 | `T1592` | 🟢 LOW |
| `220.123.74[.]61` | 1 | 2026-03-18 01:50 | 2026-03-18 01:51 | 14s | 0 | `T1592` | 🟢 LOW |
| `24.45.132[.]18` | 1 | 2026-03-18 06:31 | 2026-03-18 06:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `36.154.134[.]146` | 1 | 2026-03-18 03:04 | 2026-03-18 03:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.212.227[.]224` | 1 | 2026-03-18 06:20 | 2026-03-18 06:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]45` | 1 | 2026-03-18 03:17 | 2026-03-18 03:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.12.241[.]225` | 1 | 2026-03-18 03:11 | 2026-03-18 03:11 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.95.13[.]185` | 1 | 2026-03-18 01:20 | 2026-03-18 01:22 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.200.95[.]18` | 1 | 2026-03-18 04:09 | 2026-03-18 04:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.70.136[.]88` | 1 | 2026-03-18 02:34 | 2026-03-18 02:34 | 33s | 0 | `T1592` | 🟢 LOW |
| `96.69.42[.]141` | 1 | 2026-03-18 05:51 | 2026-03-18 05:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `101.71.39[.]17` | CN | UNICOM ZheJiang Province Network | **100** ⚠️ | 1 |
| `183.171.148[.]181` | MY | Celcom Axiata Berhad | **100** ⚠️ | 0 |
| `165.22.78[.]143` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `71.12.241[.]225` | US | Charter Communications LLC | **100** ⚠️ | 28 |
| `114.33.44[.]32` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 14 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `183.171.12[.]224` | MY | Celcom Axiata Berhad | **100** ⚠️ | 11 |
| `103.7.41[.]144` | VN | Super Online Data Co.,Ltd | **100** ⚠️ | 19 |
| `96.69.42[.]141` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 18 |
| `118.163.178[.]146` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 304 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 202 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 45 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (158 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 4 |
| AbuseIPDB score 13 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 16 |
| AbuseIPDB score 23 below threshold 25 | 7 |
| AbuseIPDB score 24 below threshold 25 | 31 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 91 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 377 cases |
| Tool 34  | Credential Extractor        | ✅ 248 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 80 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 158 filtered (41.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 51 recon entry/entries in table (15 group(s) consolidating 143 session(s)).

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
_Report time: 2026-03-18T07:00:20Z_
