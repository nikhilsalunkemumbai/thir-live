# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-19 |
| **Generated At** | 2026-03-19T05:21:57Z |
| **Shift Time** | 05:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **107** |
| Confirmed Threats | **67** |
| False Positives Filtered | **40** (37.4%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **19** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **96** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **49** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **32** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `admin` | 3 |
| `345gs5662d34` | 3 |
| `default` | 2 |
| `centos` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 3 |
| `password` | 3 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 2 |
| `2222` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `2222` | 2 |
| `debian` | `P@ssw0rd` | 1 |
| `root` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `38.250.116.128` | 2026-03-19T00:55:32 |
| `root` | `password` | `38.250.116.128` | 2026-03-19T00:56:49 |
| `root` | `admin` | `38.250.116.128` | 2026-03-19T00:57:49 |
| `root` | `12345` | `38.250.116.128` | 2026-03-19T00:58:53 |
| `root` | `Ww123456..` | `45.132.19.15` | 2026-03-19T02:30:14 |
| `root` | `qwe@123456` | `101.36.122.186` | 2026-03-19T03:21:44 |
| `root` | `3245gs5662d34` | `101.36.122.186` | 2026-03-19T03:21:47 |
| `root` | `121212` | `101.36.122.186` | 2026-03-19T03:47:04 |
| `root` | `2222` | `118.45.101.159` | 2026-03-19T04:22:18 |
| `root` | `2222` | `106.201.230.195` | 2026-03-19T04:22:25 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **35** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bbf2956e9735

| Field | Detail |
|---|---|
| **Source IP** | `38.250.116[.]128` |
| **First Seen** | 2026-03-19 00:55 |
| **Last Seen** | 2026-03-19 00:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 00:55:30` | `cowrie.session.connect` |
| `2026-03-19 00:55:30` | `cowrie.client.version` |
| `2026-03-19 00:55:31` | `cowrie.client.kex` |
| `2026-03-19 00:55:32` | `cowrie.login.success` |
| `2026-03-19 00:55:33` | `cowrie.session.params` |
| `2026-03-19 00:55:33` | `cowrie.command.input` |
| `2026-03-19 00:55:33` | `cowrie.command.input` |
| `2026-03-19 00:55:33` | `cowrie.command.input` |
| `2026-03-19 00:55:33` | `cowrie.command.input` |
| `2026-03-19 00:55:33` | `cowrie.log.closed` |
| `2026-03-19 00:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.250.116[.]128` to AbuseIPDB if not already reported
- [ ] Block `38.250.116[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1334e58c18

| Field | Detail |
|---|---|
| **Source IP** | `38.250.116[.]128` |
| **First Seen** | 2026-03-19 00:56 |
| **Last Seen** | 2026-03-19 00:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 00:56:47` | `cowrie.session.connect` |
| `2026-03-19 00:56:47` | `cowrie.client.version` |
| `2026-03-19 00:56:47` | `cowrie.client.kex` |
| `2026-03-19 00:56:49` | `cowrie.login.success` |
| `2026-03-19 00:56:50` | `cowrie.session.params` |
| `2026-03-19 00:56:50` | `cowrie.command.input` |
| `2026-03-19 00:56:50` | `cowrie.command.input` |
| `2026-03-19 00:56:50` | `cowrie.command.input` |
| `2026-03-19 00:56:50` | `cowrie.command.input` |
| `2026-03-19 00:56:50` | `cowrie.log.closed` |
| `2026-03-19 00:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.250.116[.]128` to AbuseIPDB if not already reported
- [ ] Block `38.250.116[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1cd83a5336

| Field | Detail |
|---|---|
| **Source IP** | `38.250.116[.]128` |
| **First Seen** | 2026-03-19 00:57 |
| **Last Seen** | 2026-03-19 00:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 00:57:46` | `cowrie.session.connect` |
| `2026-03-19 00:57:46` | `cowrie.client.version` |
| `2026-03-19 00:57:47` | `cowrie.client.kex` |
| `2026-03-19 00:57:49` | `cowrie.login.success` |
| `2026-03-19 00:57:51` | `cowrie.session.params` |
| `2026-03-19 00:57:51` | `cowrie.command.input` |
| `2026-03-19 00:57:51` | `cowrie.command.input` |
| `2026-03-19 00:57:51` | `cowrie.command.input` |
| `2026-03-19 00:57:51` | `cowrie.command.input` |
| `2026-03-19 00:57:52` | `cowrie.log.closed` |
| `2026-03-19 00:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.250.116[.]128` to AbuseIPDB if not already reported
- [ ] Block `38.250.116[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed9ea1ca9eb

| Field | Detail |
|---|---|
| **Source IP** | `38.250.116[.]128` |
| **First Seen** | 2026-03-19 00:58 |
| **Last Seen** | 2026-03-19 00:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 00:58:52` | `cowrie.session.connect` |
| `2026-03-19 00:58:52` | `cowrie.client.version` |
| `2026-03-19 00:58:52` | `cowrie.client.kex` |
| `2026-03-19 00:58:53` | `cowrie.login.success` |
| `2026-03-19 00:58:54` | `cowrie.session.params` |
| `2026-03-19 00:58:54` | `cowrie.command.input` |
| `2026-03-19 00:58:54` | `cowrie.command.input` |
| `2026-03-19 00:58:54` | `cowrie.command.input` |
| `2026-03-19 00:58:54` | `cowrie.command.input` |
| `2026-03-19 00:58:54` | `cowrie.log.closed` |
| `2026-03-19 00:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.250.116[.]128` to AbuseIPDB if not already reported
- [ ] Block `38.250.116[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2eb5a72228

| Field | Detail |
|---|---|
| **Source IP** | `45.132.19[.]15` |
| **First Seen** | 2026-03-19 02:30 |
| **Last Seen** | 2026-03-19 02:30 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:vN2jocf5s6nH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 02:30:13` | `cowrie.session.connect` |
| `2026-03-19 02:30:13` | `cowrie.client.version` |
| `2026-03-19 02:30:13` | `cowrie.client.kex` |
| `2026-03-19 02:30:14` | `cowrie.login.success` |
| `2026-03-19 02:30:15` | `cowrie.session.params` |
| `2026-03-19 02:30:15` | `cowrie.command.input` |
| `2026-03-19 02:30:15` | `cowrie.command.failed` |
| `2026-03-19 02:30:15` | `cowrie.log.closed` |
| `2026-03-19 02:30:15` | `cowrie.session.params` |
| `2026-03-19 02:30:15` | `cowrie.command.input` |
| `2026-03-19 02:30:15` | `cowrie.session.file_download` |
| `2026-03-19 02:30:15` | `cowrie.log.closed` |
| `2026-03-19 02:30:24` | `cowrie.session.params` |
| `2026-03-19 02:30:24` | `cowrie.command.input` |
| `2026-03-19 02:30:24` | `cowrie.log.closed` |
| `2026-03-19 02:30:24` | `cowrie.session.params` |
| `2026-03-19 02:30:24` | `cowrie.command.input` |
| `2026-03-19 02:30:25` | `cowrie.log.closed` |
| `2026-03-19 02:30:25` | `cowrie.session.params` |
| `2026-03-19 02:30:25` | `cowrie.command.input` |
| `2026-03-19 02:30:25` | `cowrie.session.file_download` |
| `2026-03-19 02:30:25` | `cowrie.log.closed` |
| `2026-03-19 02:30:26` | `cowrie.session.params` |
| `2026-03-19 02:30:26` | `cowrie.command.input` |
| `2026-03-19 02:30:26` | `cowrie.log.closed` |
| `2026-03-19 02:30:26` | `cowrie.session.params` |
| `2026-03-19 02:30:26` | `cowrie.command.input` |
| `2026-03-19 02:30:26` | `cowrie.log.closed` |
| `2026-03-19 02:30:27` | `cowrie.session.params` |
| `2026-03-19 02:30:27` | `cowrie.command.input` |
| `2026-03-19 02:30:27` | `cowrie.command.input` |
| `2026-03-19 02:30:27` | `cowrie.log.closed` |
| `2026-03-19 02:30:27` | `cowrie.session.params` |
| `2026-03-19 02:30:27` | `cowrie.command.input` |
| `2026-03-19 02:30:27` | `cowrie.log.closed` |
| `2026-03-19 02:30:28` | `cowrie.session.params` |
| `2026-03-19 02:30:28` | `cowrie.command.input` |
| `2026-03-19 02:30:28` | `cowrie.log.closed` |
| `2026-03-19 02:30:28` | `cowrie.session.params` |
| `2026-03-19 02:30:28` | `cowrie.command.input` |
| `2026-03-19 02:30:29` | `cowrie.log.closed` |
| `2026-03-19 02:30:29` | `cowrie.session.params` |
| `2026-03-19 02:30:29` | `cowrie.command.input` |
| `2026-03-19 02:30:29` | `cowrie.log.closed` |
| `2026-03-19 02:30:30` | `cowrie.session.params` |
| `2026-03-19 02:30:30` | `cowrie.command.input` |
| `2026-03-19 02:30:30` | `cowrie.log.closed` |
| `2026-03-19 02:30:30` | `cowrie.session.params` |
| `2026-03-19 02:30:30` | `cowrie.command.input` |
| `2026-03-19 02:30:30` | `cowrie.log.closed` |
| `2026-03-19 02:30:31` | `cowrie.session.params` |
| `2026-03-19 02:30:31` | `cowrie.command.input` |
| `2026-03-19 02:30:31` | `cowrie.log.closed` |
| `2026-03-19 02:30:31` | `cowrie.session.params` |
| `2026-03-19 02:30:31` | `cowrie.command.input` |
| `2026-03-19 02:30:32` | `cowrie.log.closed` |
| `2026-03-19 02:30:32` | `cowrie.session.params` |
| `2026-03-19 02:30:32` | `cowrie.command.input` |
| `2026-03-19 02:30:32` | `cowrie.log.closed` |
| `2026-03-19 02:30:33` | `cowrie.session.params` |
| `2026-03-19 02:30:33` | `cowrie.command.input` |
| `2026-03-19 02:30:33` | `cowrie.log.closed` |
| `2026-03-19 02:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.132.19[.]15` to AbuseIPDB if not already reported
- [ ] Block `45.132.19[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172a6facd3d5

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-03-19 03:21 |
| **Last Seen** | 2026-03-19 03:21 |
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
| `2026-03-19 03:21:44` | `cowrie.session.connect` |
| `2026-03-19 03:21:44` | `cowrie.client.version` |
| `2026-03-19 03:21:44` | `cowrie.client.kex` |
| `2026-03-19 03:21:44` | `cowrie.login.success` |
| `2026-03-19 03:21:44` | `cowrie.session.params` |
| `2026-03-19 03:21:44` | `cowrie.command.input` |
| `2026-03-19 03:21:44` | `cowrie.command.failed` |
| `2026-03-19 03:21:45` | `cowrie.log.closed` |
| `2026-03-19 03:21:45` | `cowrie.session.params` |
| `2026-03-19 03:21:45` | `cowrie.command.input` |
| `2026-03-19 03:21:45` | `cowrie.session.file_download` |
| `2026-03-19 03:21:45` | `cowrie.log.closed` |
| `2026-03-19 03:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed423bf86420

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-03-19 03:21 |
| **Last Seen** | 2026-03-19 03:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 03:21:47` | `cowrie.session.connect` |
| `2026-03-19 03:21:47` | `cowrie.client.version` |
| `2026-03-19 03:21:47` | `cowrie.client.kex` |
| `2026-03-19 03:21:47` | `cowrie.login.success` |
| `2026-03-19 03:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a212929319

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-03-19 03:47 |
| **Last Seen** | 2026-03-19 03:47 |
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
| `2026-03-19 03:47:04` | `cowrie.session.connect` |
| `2026-03-19 03:47:04` | `cowrie.client.version` |
| `2026-03-19 03:47:04` | `cowrie.client.kex` |
| `2026-03-19 03:47:04` | `cowrie.login.success` |
| `2026-03-19 03:47:05` | `cowrie.session.params` |
| `2026-03-19 03:47:05` | `cowrie.command.input` |
| `2026-03-19 03:47:05` | `cowrie.command.failed` |
| `2026-03-19 03:47:05` | `cowrie.log.closed` |
| `2026-03-19 03:47:05` | `cowrie.session.params` |
| `2026-03-19 03:47:05` | `cowrie.command.input` |
| `2026-03-19 03:47:05` | `cowrie.session.file_download` |
| `2026-03-19 03:47:05` | `cowrie.log.closed` |
| `2026-03-19 03:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76053a0628f3

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-03-19 03:47 |
| **Last Seen** | 2026-03-19 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 03:47:07` | `cowrie.session.connect` |
| `2026-03-19 03:47:07` | `cowrie.client.version` |
| `2026-03-19 03:47:07` | `cowrie.client.kex` |
| `2026-03-19 03:47:08` | `cowrie.login.success` |
| `2026-03-19 03:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed9eb90a8dc

| Field | Detail |
|---|---|
| **Source IP** | `118.45.101[.]159` |
| **First Seen** | 2026-03-19 04:22 |
| **Last Seen** | 2026-03-19 04:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 04:22:14` | `cowrie.session.connect` |
| `2026-03-19 04:22:15` | `cowrie.client.version` |
| `2026-03-19 04:22:15` | `cowrie.client.kex` |
| `2026-03-19 04:22:18` | `cowrie.login.success` |
| `2026-03-19 04:22:18` | `cowrie.direct-tcpip.request` |
| `2026-03-19 04:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.101[.]159` to AbuseIPDB if not already reported
- [ ] Block `118.45.101[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488c9ff1cef3

| Field | Detail |
|---|---|
| **Source IP** | `106.201.230[.]195` |
| **First Seen** | 2026-03-19 04:22 |
| **Last Seen** | 2026-03-19 04:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 04:22:24` | `cowrie.session.connect` |
| `2026-03-19 04:22:25` | `cowrie.client.version` |
| `2026-03-19 04:22:25` | `cowrie.client.kex` |
| `2026-03-19 04:22:25` | `cowrie.login.success` |
| `2026-03-19 04:22:26` | `cowrie.direct-tcpip.request` |
| `2026-03-19 04:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.201.230[.]195` to AbuseIPDB if not already reported
- [ ] Block `106.201.230[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.122[.]186` | **15** | 2026-03-19 03:18 | 2026-03-19 03:47 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `38.250.116[.]128` | **5** | 2026-03-19 00:53 | 2026-03-19 00:58 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.132.19[.]15` | **5** | 2026-03-19 02:13 | 2026-03-19 02:32 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **4** | 2026-03-19 03:49 | 2026-03-19 03:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.59.120[.]77` | **3** | 2026-03-19 00:05 | 2026-03-19 00:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.220.119[.]116` | 1 | 2026-03-19 04:13 | 2026-03-19 04:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `111.70.39[.]216` | 1 | 2026-03-19 02:03 | 2026-03-19 02:03 | 15s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.124.96[.]19` | 1 | 2026-03-19 00:15 | 2026-03-19 00:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-19 03:22 | 2026-03-19 03:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.183.180[.]108` | 1 | 2026-03-19 03:20 | 2026-03-19 03:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.189.198[.]60` | 1 | 2026-03-19 03:43 | 2026-03-19 03:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.202.138[.]181` | 1 | 2026-03-19 02:22 | 2026-03-19 02:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.167.20[.]113` | 1 | 2026-03-19 03:59 | 2026-03-19 03:59 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `134.209.86[.]24` | 1 | 2026-03-19 04:24 | 2026-03-19 04:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.245.243[.]118` | 1 | 2026-03-19 00:12 | 2026-03-19 00:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `179.185.18[.]67` | 1 | 2026-03-19 03:01 | 2026-03-19 03:01 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.100[.]110` | 1 | 2026-03-19 03:19 | 2026-03-19 03:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-03-19 01:44 | 2026-03-19 01:44 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.120.240[.]60` | 1 | 2026-03-19 00:14 | 2026-03-19 00:14 | 31s | 0 | `T1592` | 🟢 LOW |
| `197.242.170[.]10` | 1 | 2026-03-19 04:59 | 2026-03-19 04:59 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-03-19 05:18 | 2026-03-19 05:18 | 7s | 0 | `T1592` | 🟢 LOW |
| `220.246.66[.]209` | 1 | 2026-03-19 04:19 | 2026-03-19 04:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.146.248[.]7` | 1 | 2026-03-19 00:07 | 2026-03-19 00:07 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.178.227[.]0` | 1 | 2026-03-19 01:28 | 2026-03-19 01:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.223.176[.]171` | 1 | 2026-03-19 02:42 | 2026-03-19 02:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.185[.]185` | 1 | 2026-03-19 02:45 | 2026-03-19 02:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `70.91.135[.]181` | 1 | 2026-03-19 02:42 | 2026-03-19 02:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.37.179[.]158` | 1 | 2026-03-19 01:04 | 2026-03-19 01:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.145.118[.]40` | 1 | 2026-03-19 03:24 | 2026-03-19 03:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `180.76.100[.]110` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 4 |
| `197.251.193[.]6` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 7 |
| `118.183.180[.]108` | CN | CHINANET Gansu province network | **100** ⚠️ | 33 |
| `45.178.227[.]0` | BR | GIGA REDE INTERNET LTDA | **100** ⚠️ | 32 |
| `1.220.119[.]116` | KR | LG DACOM Corporation | **100** ⚠️ | 41 |
| `118.45.101[.]159` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `124.167.20[.]113` | CN | China Unicom Shan1xi province network | **100** ⚠️ | 50 |
| `111.70.39[.]216` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 19 |
| `186.148.187[.]172` | CO | TV AZTECA SUCURSAL COLOMBIA | **100** ⚠️ | 17 |
| `65.20.185[.]185` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 34 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 54 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 38 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 107 cases |
| Tool 34  | Credential Extractor        | ✅ 49 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (37.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 29 recon entry/entries in table (5 group(s) consolidating 32 session(s)).

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
_Report time: 2026-03-19T05:21:57Z_
