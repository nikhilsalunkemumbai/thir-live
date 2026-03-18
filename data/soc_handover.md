# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-18 |
| **Generated At** | 2026-03-18T18:57:18Z |
| **Shift Time** | 18:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1164** |
| Confirmed Threats | **183** |
| False Positives Filtered | **981** (84.3%) |
| Unique Attacker IPs | **225** |
| Countries of Origin | **26** |
| High Severity Cases | **103** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1061** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **562** |
| Unique Credential Pairs | **481** |
| Unique Usernames | **295** |
| Unique Passwords | **331** |
| Successful Auth Pairs | **97** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 110 |
| `345gs5662d34` | 21 |
| `admin` | 20 |
| `ubuntu` | 15 |
| `user` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 48 |
| `345gs5662d34` | 21 |
| `3245gs5662d34` | 20 |
| `1234` | 19 |
| `password` | 18 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 21 |
| `root` | `3245gs5662d34` | 20 |
| `root` | `` | 6 |
| `admin` | `admin` | 5 |
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
| `root` | `!Qaz@Wsx` | `67.205.184.189` | 2026-03-18T14:28:19 |
| `root` | `null` | `67.205.184.189` | 2026-03-18T14:28:26 |
| `root` | `123abc456` | `67.205.184.189` | 2026-03-18T14:29:38 |
| `root` | `admin@123` | `112.194.142.167` | 2026-03-18T14:43:10 |
| `root` | `11221122` | `103.153.190.105` | 2026-03-18T14:56:16 |
| `root` | `3245gs5662d34` | `103.153.190.105` | 2026-03-18T14:56:19 |
| `root` | `root2023` | `114.98.63.18` | 2026-03-18T15:38:55 |
| `root` | `Aa@112233` | `179.32.33.161` | 2026-03-18T15:39:25 |
| `root` | `3245gs5662d34` | `179.32.33.161` | 2026-03-18T15:39:32 |
| `root` | `abc123456.` | `180.167.96.50` | 2026-03-18T15:42:57 |
| `root` | `Welkom01` | `113.137.40.250` | 2026-03-18T15:43:40 |
| `root` | `3245gs5662d34` | `113.137.40.250` | 2026-03-18T15:43:45 |
| `root` | `Aa147258` | `34.135.200.178` | 2026-03-18T18:22:15 |
| `root` | `3245gs5662d34` | `34.135.200.178` | 2026-03-18T18:22:21 |
| `root` | `root@2019` | `183.91.11.36` | 2026-03-18T18:47:06 |
| `root` | `3245gs5662d34` | `183.91.11.36` | 2026-03-18T18:47:09 |
| `root` | `Windows10` | `183.91.11.36` | 2026-03-18T18:49:36 |
| `root` | `qwerty1234` | `35.130.111.146` | 2026-03-18T18:56:03 |
| `root` | `qwerty1234` | `103.220.91.138` | 2026-03-18T18:56:10 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **225** |
| Unique ASNs | **102** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 12 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 11 | HIGH |
| `AS22773` | Cox Communications Inc. | 11 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 10 | HIGH |
| `AS46562` | Performive LLC | 10 | LOW |
| `AS14061` | DigitalOcean, LLC | 7 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 7 | HIGH |
| `AS396982` | Google LLC | 6 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

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

### 🔴 HIGH · IR-d856245a331d

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-03-18 14:43 |
| **Last Seen** | 2026-03-18 14:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 14:43:07` | `cowrie.session.connect` |
| `2026-03-18 14:43:07` | `cowrie.client.version` |
| `2026-03-18 14:43:07` | `cowrie.client.kex` |
| `2026-03-18 14:43:10` | `cowrie.login.success` |
| `2026-03-18 14:43:11` | `cowrie.direct-tcpip.request` |
| `2026-03-18 14:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2787dc5dcaf8

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-03-18 15:39 |
| **Last Seen** | 2026-03-18 15:39 |
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
| `2026-03-18 15:39:23` | `cowrie.session.connect` |
| `2026-03-18 15:39:23` | `cowrie.client.version` |
| `2026-03-18 15:39:24` | `cowrie.client.kex` |
| `2026-03-18 15:39:25` | `cowrie.login.success` |
| `2026-03-18 15:39:26` | `cowrie.session.params` |
| `2026-03-18 15:39:26` | `cowrie.command.input` |
| `2026-03-18 15:39:26` | `cowrie.command.failed` |
| `2026-03-18 15:39:26` | `cowrie.log.closed` |
| `2026-03-18 15:39:27` | `cowrie.session.params` |
| `2026-03-18 15:39:27` | `cowrie.command.input` |
| `2026-03-18 15:39:27` | `cowrie.session.file_download` |
| `2026-03-18 15:39:27` | `cowrie.log.closed` |
| `2026-03-18 15:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637dc99405a0

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-03-18 15:39 |
| **Last Seen** | 2026-03-18 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 15:39:30` | `cowrie.session.connect` |
| `2026-03-18 15:39:30` | `cowrie.client.version` |
| `2026-03-18 15:39:31` | `cowrie.client.kex` |
| `2026-03-18 15:39:32` | `cowrie.login.success` |
| `2026-03-18 15:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1baf607ebedc

| Field | Detail |
|---|---|
| **Source IP** | `113.137.40[.]250` |
| **First Seen** | 2026-03-18 15:43 |
| **Last Seen** | 2026-03-18 15:43 |
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
| `2026-03-18 15:43:40` | `cowrie.session.connect` |
| `2026-03-18 15:43:40` | `cowrie.client.version` |
| `2026-03-18 15:43:40` | `cowrie.client.kex` |
| `2026-03-18 15:43:40` | `cowrie.login.success` |
| `2026-03-18 15:43:41` | `cowrie.session.params` |
| `2026-03-18 15:43:41` | `cowrie.command.input` |
| `2026-03-18 15:43:41` | `cowrie.command.failed` |
| `2026-03-18 15:43:41` | `cowrie.log.closed` |
| `2026-03-18 15:43:41` | `cowrie.session.params` |
| `2026-03-18 15:43:41` | `cowrie.command.input` |
| `2026-03-18 15:43:42` | `cowrie.session.file_download` |
| `2026-03-18 15:43:42` | `cowrie.log.closed` |
| `2026-03-18 15:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.137.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.137.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02a24017256

| Field | Detail |
|---|---|
| **Source IP** | `113.137.40[.]250` |
| **First Seen** | 2026-03-18 15:43 |
| **Last Seen** | 2026-03-18 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 15:43:44` | `cowrie.session.connect` |
| `2026-03-18 15:43:44` | `cowrie.client.version` |
| `2026-03-18 15:43:44` | `cowrie.client.kex` |
| `2026-03-18 15:43:45` | `cowrie.login.success` |
| `2026-03-18 15:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.137.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.137.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf52d313066

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-18 18:47 |
| **Last Seen** | 2026-03-18 18:47 |
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
| `2026-03-18 18:47:05` | `cowrie.session.connect` |
| `2026-03-18 18:47:05` | `cowrie.client.version` |
| `2026-03-18 18:47:05` | `cowrie.client.kex` |
| `2026-03-18 18:47:06` | `cowrie.login.success` |
| `2026-03-18 18:47:06` | `cowrie.session.params` |
| `2026-03-18 18:47:06` | `cowrie.command.input` |
| `2026-03-18 18:47:06` | `cowrie.command.failed` |
| `2026-03-18 18:47:06` | `cowrie.log.closed` |
| `2026-03-18 18:47:06` | `cowrie.session.params` |
| `2026-03-18 18:47:06` | `cowrie.command.input` |
| `2026-03-18 18:47:07` | `cowrie.session.file_download` |
| `2026-03-18 18:47:07` | `cowrie.log.closed` |
| `2026-03-18 18:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1809777c9fe6

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-18 18:47 |
| **Last Seen** | 2026-03-18 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 18:47:08` | `cowrie.session.connect` |
| `2026-03-18 18:47:08` | `cowrie.client.version` |
| `2026-03-18 18:47:08` | `cowrie.client.kex` |
| `2026-03-18 18:47:09` | `cowrie.login.success` |
| `2026-03-18 18:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492788ffd9c6

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-18 18:49 |
| **Last Seen** | 2026-03-18 18:49 |
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
| `2026-03-18 18:49:35` | `cowrie.session.connect` |
| `2026-03-18 18:49:35` | `cowrie.client.version` |
| `2026-03-18 18:49:35` | `cowrie.client.kex` |
| `2026-03-18 18:49:36` | `cowrie.login.success` |
| `2026-03-18 18:49:36` | `cowrie.session.params` |
| `2026-03-18 18:49:36` | `cowrie.command.input` |
| `2026-03-18 18:49:36` | `cowrie.command.failed` |
| `2026-03-18 18:49:36` | `cowrie.log.closed` |
| `2026-03-18 18:49:36` | `cowrie.session.params` |
| `2026-03-18 18:49:36` | `cowrie.command.input` |
| `2026-03-18 18:49:36` | `cowrie.session.file_download` |
| `2026-03-18 18:49:36` | `cowrie.log.closed` |
| `2026-03-18 18:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-147a502d3867

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-18 18:49 |
| **Last Seen** | 2026-03-18 18:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 18:49:38` | `cowrie.session.connect` |
| `2026-03-18 18:49:38` | `cowrie.client.version` |
| `2026-03-18 18:49:38` | `cowrie.client.kex` |
| `2026-03-18 18:49:39` | `cowrie.login.success` |
| `2026-03-18 18:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8feed97a61ef

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-03-18 18:56 |
| **Last Seen** | 2026-03-18 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 18:56:00` | `cowrie.session.connect` |
| `2026-03-18 18:56:00` | `cowrie.client.version` |
| `2026-03-18 18:56:00` | `cowrie.client.kex` |
| `2026-03-18 18:56:03` | `cowrie.login.success` |
| `2026-03-18 18:56:03` | `cowrie.direct-tcpip.request` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f6758218b0

| Field | Detail |
|---|---|
| **Source IP** | `103.220.91[.]138` |
| **First Seen** | 2026-03-18 18:56 |
| **Last Seen** | 2026-03-18 18:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-18 18:56:08` | `cowrie.session.connect` |
| `2026-03-18 18:56:09` | `cowrie.client.version` |
| `2026-03-18 18:56:09` | `cowrie.client.kex` |
| `2026-03-18 18:56:10` | `cowrie.login.success` |
| `2026-03-18 18:56:11` | `cowrie.direct-tcpip.request` |
| `2026-03-18 18:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.220.91[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.220.91[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.255.26[.]45` | **25** | 2026-03-18 05:16 | 2026-03-18 05:22 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.7.41[.]144` | **15** | 2026-03-18 06:09 | 2026-03-18 06:16 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.100.77[.]140` | **15** | 2026-03-18 12:18 | 2026-03-18 12:33 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.88[.]251` | **12** | 2026-03-18 04:54 | 2026-03-18 05:14 | 20m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.91[.]58` | **10** | 2026-03-18 18:21 | 2026-03-18 18:38 | 9m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.32.33[.]161` | **10** | 2026-03-18 15:17 | 2026-03-18 15:39 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **5** | 2026-03-18 16:57 | 2026-03-18 17:04 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `183.91.11[.]36` | **5** | 2026-03-18 18:41 | 2026-03-18 18:54 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.97[.]70` | **4** | 2026-03-18 04:22 | 2026-03-18 04:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.110.23[.]141` | **3** | 2026-03-18 01:02 | 2026-03-18 01:05 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `212.11.64[.]156` | **3** | 2026-03-18 18:43 | 2026-03-18 18:48 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.237.144[.]204` | **2** | 2026-03-18 11:14 | 2026-03-18 11:18 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `189.190.166[.]109` | **2** | 2026-03-18 10:58 | 2026-03-18 11:00 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.193[.]130` | **2** | 2026-03-18 16:55 | 2026-03-18 16:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.80.104[.]232` | **2** | 2026-03-18 03:33 | 2026-03-18 03:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.84.153[.]170` | **2** | 2026-03-18 09:41 | 2026-03-18 09:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]35` | 1 | 2026-03-18 10:49 | 2026-03-18 10:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.157.40[.]219` | 1 | 2026-03-18 12:26 | 2026-03-18 12:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.184.45[.]204` | 1 | 2026-03-18 06:27 | 2026-03-18 06:27 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.4.79[.]138` | 1 | 2026-03-18 01:40 | 2026-03-18 01:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-03-18 15:43 | 2026-03-18 15:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.33.44[.]32` | 1 | 2026-03-18 05:10 | 2026-03-18 05:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.190.10[.]158` | 1 | 2026-03-18 10:50 | 2026-03-18 10:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.110.148[.]145` | 1 | 2026-03-18 01:32 | 2026-03-18 01:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-18 04:53 | 2026-03-18 04:53 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.153[.]102` | 1 | 2026-03-18 14:23 | 2026-03-18 14:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.198.96[.]190` | 1 | 2026-03-18 02:59 | 2026-03-18 02:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `120.211.5[.]35` | 1 | 2026-03-18 10:45 | 2026-03-18 10:45 | 3s | 0 | `T1592` | 🟢 LOW |
| `120.240.95[.]27` | 1 | 2026-03-18 14:39 | 2026-03-18 14:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.196.27[.]240` | 1 | 2026-03-18 04:16 | 2026-03-18 04:18 | 81s | 0 | `T1592` | 🟢 LOW |
| `122.160.50[.]155` | 1 | 2026-03-18 10:11 | 2026-03-18 10:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.19.156[.]46` | 1 | 2026-03-18 01:58 | 2026-03-18 01:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.208.17[.]16` | 1 | 2026-03-18 01:21 | 2026-03-18 01:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.35.109[.]214` | 1 | 2026-03-18 18:38 | 2026-03-18 18:38 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.114[.]218` | 1 | 2026-03-18 18:09 | 2026-03-18 18:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.179[.]212` | 1 | 2026-03-18 14:43 | 2026-03-18 14:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-03-18 10:46 | 2026-03-18 10:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.175[.]142` | 1 | 2026-03-18 11:44 | 2026-03-18 11:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-03-18 01:46 | 2026-03-18 01:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]181` | 1 | 2026-03-18 04:00 | 2026-03-18 04:00 | 15s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]181` | 1 | 2026-03-18 10:49 | 2026-03-18 10:51 | 102s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-03-18 10:48 | 2026-03-18 10:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.223.36[.]108` | 1 | 2026-03-18 09:43 | 2026-03-18 09:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.100[.]104` | 1 | 2026-03-18 14:20 | 2026-03-18 14:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.236.215[.]9` | 1 | 2026-03-18 07:15 | 2026-03-18 07:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `42.58.5[.]52` | 1 | 2026-03-18 15:47 | 2026-03-18 15:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `46.236.65[.]65` | 1 | 2026-03-18 13:10 | 2026-03-18 13:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]237` | 1 | 2026-03-18 12:07 | 2026-03-18 12:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]160` | 1 | 2026-03-18 07:11 | 2026-03-18 07:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.142.216[.]61` | 1 | 2026-03-18 12:44 | 2026-03-18 12:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.36.11[.]59` | 1 | 2026-03-18 09:23 | 2026-03-18 09:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.43.32[.]40` | 1 | 2026-03-18 12:46 | 2026-03-18 12:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.73.173[.]176` | 1 | 2026-03-18 16:58 | 2026-03-18 16:58 | 14s | 0 | `T1592` | 🟢 LOW |
| `74.95.13[.]185` | 1 | 2026-03-18 01:20 | 2026-03-18 01:22 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.214.75[.]248` | 1 | 2026-03-18 11:02 | 2026-03-18 11:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
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
| `104.157.40[.]219` | CA | TELUS Communications Inc. | **100** ⚠️ | 13 |
| `121.196.27[.]240` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 24 |
| `147.189.161[.]77` | US | Jerng Yue Lee trading as Evoxt Enterprise | **100** ⚠️ | 11 |
| `118.163.178[.]146` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `116.110.156[.]14` | VN | Viettel Group | **100** ⚠️ | 0 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `183.171.148[.]181` | MY | Celcom Axiata Berhad | **100** ⚠️ | 0 |
| `46.236.65[.]65` | SE | Bredband2 AB | **100** ⚠️ | 0 |
| `113.137.40[.]250` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `35.130.111[.]146` | US | Charter Communications LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 652 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 452 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 103 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 23 |

---

## 🔕 False Positive Summary (981 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 919 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 4 |
| AbuseIPDB score 22 below threshold 25 | 7 |
| AbuseIPDB score 24 below threshold 25 | 31 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1164 cases |
| Tool 34  | Credential Extractor        | ✅ 562 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 225 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 981 filtered (84.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 102 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 57 recon entry/entries in table (16 group(s) consolidating 117 session(s)).

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
_Report time: 2026-03-18T18:57:18Z_
