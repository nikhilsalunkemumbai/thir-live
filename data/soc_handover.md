# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T14:32:31Z |
| **Shift Time** | 14:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **64** |
| Confirmed Threats | **53** |
| False Positives Filtered | **11** (17.2%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **16** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **14** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **44** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **21** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 6 |
| `unknown` | 2 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `P@ssword` | 2 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin123456` | `156.236.75.188` | 2026-04-04T13:20:47 |
| `root` | `3245gs5662d34` | `156.236.75.188` | 2026-04-04T13:20:51 |
| `root` | `Qazwsx4321@#` | `156.236.75.188` | 2026-04-04T13:23:13 |
| `root` | `Root1234.` | `156.236.75.188` | 2026-04-04T13:25:44 |
| `root` | `pass1234` | `103.143.72.165` | 2026-04-04T13:48:41 |
| `root` | `3245gs5662d34` | `103.143.72.165` | 2026-04-04T13:48:44 |
| `root` | `admin12345678!@` | `49.207.40.162` | 2026-04-04T13:49:03 |
| `root` | `3245gs5662d34` | `49.207.40.162` | 2026-04-04T13:49:05 |
| `root` | `Qwerty123!!` | `69.6.221.248` | 2026-04-04T13:50:00 |
| `root` | `3245gs5662d34` | `69.6.221.248` | 2026-04-04T13:50:08 |
| `root` | `root2023` | `128.185.218.118` | 2026-04-04T14:06:46 |
| `root` | `root2023` | `121.73.168.9` | 2026-04-04T14:06:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **64** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 26 |
| OpenSSH | 15 |
| Paramiko (Python) | 8 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 25 | 8 |
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `87e3d9ffee05...` | Mirai/variant | 8 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 25 | 8 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `49.207.40.162`, `69.6.221.248`, `103.143.72.165`, `156.236.75.188`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **32** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS138152` | YISU CLOUD LTD | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 1 | HIGH |
| `AS1680` | Cellcom Fixed Line Communication L.P | 1 | HIGH |
| `AS51167` | Contabo GmbH | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c97e2cc33861

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 13:20 |
| **Last Seen** | 2026-04-04 13:20 |
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
| `2026-04-04 13:20:46` | `cowrie.session.connect` |
| `2026-04-04 13:20:46` | `cowrie.client.version` |
| `2026-04-04 13:20:46` | `cowrie.client.kex` |
| `2026-04-04 13:20:47` | `cowrie.login.success` |
| `2026-04-04 13:20:47` | `cowrie.session.params` |
| `2026-04-04 13:20:47` | `cowrie.command.input` |
| `2026-04-04 13:20:47` | `cowrie.command.failed` |
| `2026-04-04 13:20:47` | `cowrie.log.closed` |
| `2026-04-04 13:20:48` | `cowrie.session.params` |
| `2026-04-04 13:20:48` | `cowrie.command.input` |
| `2026-04-04 13:20:48` | `cowrie.session.file_download` |
| `2026-04-04 13:20:48` | `cowrie.log.closed` |
| `2026-04-04 13:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eab85814639a

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 13:20 |
| **Last Seen** | 2026-04-04 13:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 13:20:50` | `cowrie.session.connect` |
| `2026-04-04 13:20:50` | `cowrie.client.version` |
| `2026-04-04 13:20:50` | `cowrie.client.kex` |
| `2026-04-04 13:20:51` | `cowrie.login.success` |
| `2026-04-04 13:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f522f6d935b8

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 13:23 |
| **Last Seen** | 2026-04-04 13:23 |
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
| `2026-04-04 13:23:12` | `cowrie.session.connect` |
| `2026-04-04 13:23:12` | `cowrie.client.version` |
| `2026-04-04 13:23:12` | `cowrie.client.kex` |
| `2026-04-04 13:23:13` | `cowrie.login.success` |
| `2026-04-04 13:23:13` | `cowrie.session.params` |
| `2026-04-04 13:23:13` | `cowrie.command.input` |
| `2026-04-04 13:23:13` | `cowrie.command.failed` |
| `2026-04-04 13:23:13` | `cowrie.log.closed` |
| `2026-04-04 13:23:14` | `cowrie.session.params` |
| `2026-04-04 13:23:14` | `cowrie.command.input` |
| `2026-04-04 13:23:14` | `cowrie.session.file_download` |
| `2026-04-04 13:23:14` | `cowrie.log.closed` |
| `2026-04-04 13:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46bf66b46a8

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 13:23 |
| **Last Seen** | 2026-04-04 13:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 13:23:16` | `cowrie.session.connect` |
| `2026-04-04 13:23:16` | `cowrie.client.version` |
| `2026-04-04 13:23:16` | `cowrie.client.kex` |
| `2026-04-04 13:23:17` | `cowrie.login.success` |
| `2026-04-04 13:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c21b9200ea

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 13:25 |
| **Last Seen** | 2026-04-04 13:25 |
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
| `2026-04-04 13:25:43` | `cowrie.session.connect` |
| `2026-04-04 13:25:43` | `cowrie.client.version` |
| `2026-04-04 13:25:43` | `cowrie.client.kex` |
| `2026-04-04 13:25:44` | `cowrie.login.success` |
| `2026-04-04 13:25:44` | `cowrie.session.params` |
| `2026-04-04 13:25:44` | `cowrie.command.input` |
| `2026-04-04 13:25:44` | `cowrie.command.failed` |
| `2026-04-04 13:25:44` | `cowrie.log.closed` |
| `2026-04-04 13:25:44` | `cowrie.session.params` |
| `2026-04-04 13:25:44` | `cowrie.command.input` |
| `2026-04-04 13:25:45` | `cowrie.session.file_download` |
| `2026-04-04 13:25:45` | `cowrie.log.closed` |
| `2026-04-04 13:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13441f83287

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 13:25 |
| **Last Seen** | 2026-04-04 13:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 13:25:47` | `cowrie.session.connect` |
| `2026-04-04 13:25:47` | `cowrie.client.version` |
| `2026-04-04 13:25:47` | `cowrie.client.kex` |
| `2026-04-04 13:25:47` | `cowrie.login.success` |
| `2026-04-04 13:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf9f1779fdd

| Field | Detail |
|---|---|
| **Source IP** | `103.143.72[.]165` |
| **First Seen** | 2026-04-04 13:48 |
| **Last Seen** | 2026-04-04 13:48 |
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
| `2026-04-04 13:48:40` | `cowrie.session.connect` |
| `2026-04-04 13:48:40` | `cowrie.client.version` |
| `2026-04-04 13:48:40` | `cowrie.client.kex` |
| `2026-04-04 13:48:41` | `cowrie.login.success` |
| `2026-04-04 13:48:41` | `cowrie.session.params` |
| `2026-04-04 13:48:41` | `cowrie.command.input` |
| `2026-04-04 13:48:41` | `cowrie.command.failed` |
| `2026-04-04 13:48:41` | `cowrie.log.closed` |
| `2026-04-04 13:48:42` | `cowrie.session.params` |
| `2026-04-04 13:48:42` | `cowrie.command.input` |
| `2026-04-04 13:48:42` | `cowrie.session.file_download` |
| `2026-04-04 13:48:42` | `cowrie.log.closed` |
| `2026-04-04 13:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.72[.]165` to AbuseIPDB if not already reported
- [ ] Block `103.143.72[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d49cc3c71c3

| Field | Detail |
|---|---|
| **Source IP** | `103.143.72[.]165` |
| **First Seen** | 2026-04-04 13:48 |
| **Last Seen** | 2026-04-04 13:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 13:48:44` | `cowrie.session.connect` |
| `2026-04-04 13:48:44` | `cowrie.client.version` |
| `2026-04-04 13:48:44` | `cowrie.client.kex` |
| `2026-04-04 13:48:44` | `cowrie.login.success` |
| `2026-04-04 13:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.72[.]165` to AbuseIPDB if not already reported
- [ ] Block `103.143.72[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47fc3415f428

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-04-04 13:49 |
| **Last Seen** | 2026-04-04 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 13:49:03` | `cowrie.session.connect` |
| `2026-04-04 13:49:03` | `cowrie.client.version` |
| `2026-04-04 13:49:03` | `cowrie.client.kex` |
| `2026-04-04 13:49:03` | `cowrie.login.success` |
| `2026-04-04 13:49:03` | `cowrie.session.params` |
| `2026-04-04 13:49:03` | `cowrie.command.input` |
| `2026-04-04 13:49:03` | `cowrie.command.failed` |
| `2026-04-04 13:49:03` | `cowrie.log.closed` |
| `2026-04-04 13:49:04` | `cowrie.session.params` |
| `2026-04-04 13:49:04` | `cowrie.command.input` |
| `2026-04-04 13:49:04` | `cowrie.session.file_download` |
| `2026-04-04 13:49:04` | `cowrie.log.closed` |
| `2026-04-04 13:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d75944f442

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-04-04 13:49 |
| **Last Seen** | 2026-04-04 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 13:49:05` | `cowrie.session.connect` |
| `2026-04-04 13:49:05` | `cowrie.client.version` |
| `2026-04-04 13:49:05` | `cowrie.client.kex` |
| `2026-04-04 13:49:05` | `cowrie.login.success` |
| `2026-04-04 13:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92c33050981

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-04 13:49 |
| **Last Seen** | 2026-04-04 13:50 |
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
| `2026-04-04 13:49:59` | `cowrie.session.connect` |
| `2026-04-04 13:49:59` | `cowrie.client.version` |
| `2026-04-04 13:49:59` | `cowrie.client.kex` |
| `2026-04-04 13:50:00` | `cowrie.login.success` |
| `2026-04-04 13:50:01` | `cowrie.session.params` |
| `2026-04-04 13:50:01` | `cowrie.command.input` |
| `2026-04-04 13:50:01` | `cowrie.command.failed` |
| `2026-04-04 13:50:01` | `cowrie.log.closed` |
| `2026-04-04 13:50:02` | `cowrie.session.params` |
| `2026-04-04 13:50:02` | `cowrie.command.input` |
| `2026-04-04 13:50:02` | `cowrie.session.file_download` |
| `2026-04-04 13:50:02` | `cowrie.log.closed` |
| `2026-04-04 13:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17bc0909f2de

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-04 13:50 |
| **Last Seen** | 2026-04-04 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 13:50:06` | `cowrie.session.connect` |
| `2026-04-04 13:50:06` | `cowrie.client.version` |
| `2026-04-04 13:50:06` | `cowrie.client.kex` |
| `2026-04-04 13:50:08` | `cowrie.login.success` |
| `2026-04-04 13:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a8971454e24

| Field | Detail |
|---|---|
| **Source IP** | `128.185.218[.]118` |
| **First Seen** | 2026-04-04 14:06 |
| **Last Seen** | 2026-04-04 14:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 14:06:44` | `cowrie.session.connect` |
| `2026-04-04 14:06:44` | `cowrie.client.version` |
| `2026-04-04 14:06:44` | `cowrie.client.kex` |
| `2026-04-04 14:06:46` | `cowrie.login.success` |
| `2026-04-04 14:06:46` | `cowrie.direct-tcpip.request` |
| `2026-04-04 14:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.218[.]118` to AbuseIPDB if not already reported
- [ ] Block `128.185.218[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e38c24ebf4

| Field | Detail |
|---|---|
| **Source IP** | `121.73.168[.]9` |
| **First Seen** | 2026-04-04 14:06 |
| **Last Seen** | 2026-04-04 14:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 14:06:52` | `cowrie.session.connect` |
| `2026-04-04 14:06:52` | `cowrie.client.version` |
| `2026-04-04 14:06:52` | `cowrie.client.kex` |
| `2026-04-04 14:06:55` | `cowrie.login.success` |
| `2026-04-04 14:06:56` | `cowrie.direct-tcpip.request` |
| `2026-04-04 14:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.73.168[.]9` to AbuseIPDB if not already reported
- [ ] Block `121.73.168[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.131.220[.]121` | **6** | 2026-04-04 13:46 | 2026-04-04 13:52 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `156.236.75[.]188` | **4** | 2026-04-04 13:20 | 2026-04-04 13:28 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `80.87.83[.]229` | **3** | 2026-04-04 13:55 | 2026-04-04 14:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.157[.]138` | 1 | 2026-04-04 13:57 | 2026-04-04 13:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.143.72[.]165` | 1 | 2026-04-04 13:48 | 2026-04-04 13:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.12.108[.]64` | 1 | 2026-04-04 14:29 | 2026-04-04 14:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `116.59.10[.]205` | 1 | 2026-04-04 14:26 | 2026-04-04 14:26 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.224.15[.]67` | 1 | 2026-04-04 13:41 | 2026-04-04 13:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.36.38[.]211` | 1 | 2026-04-04 13:07 | 2026-04-04 13:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.98.28[.]43` | 1 | 2026-04-04 13:03 | 2026-04-04 13:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `144.64.157[.]244` | 1 | 2026-04-04 12:57 | 2026-04-04 12:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-04 13:27 | 2026-04-04 13:27 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.129.195[.]46` | 1 | 2026-04-04 13:08 | 2026-04-04 13:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.12.132[.]63` | 1 | 2026-04-04 13:45 | 2026-04-04 13:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.102.22[.]96` | 1 | 2026-04-04 14:31 | 2026-04-04 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.248.129[.]130` | 1 | 2026-04-04 14:01 | 2026-04-04 14:01 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.140.214[.]19` | 1 | 2026-04-04 12:52 | 2026-04-04 12:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-04-04 13:06 | 2026-04-04 13:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.146.217[.]105` | 1 | 2026-04-04 13:25 | 2026-04-04 13:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.250.107[.]144` | 1 | 2026-04-04 14:20 | 2026-04-04 14:20 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.158.142[.]145` | 1 | 2026-04-04 14:05 | 2026-04-04 14:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.207.40[.]162` | 1 | 2026-04-04 13:49 | 2026-04-04 13:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.203.40[.]22` | 1 | 2026-04-04 12:57 | 2026-04-04 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.171.135[.]254` | 1 | 2026-04-04 14:24 | 2026-04-04 14:24 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.6.221[.]248` | 1 | 2026-04-04 13:50 | 2026-04-04 13:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.189.17[.]35` | 1 | 2026-04-04 13:22 | 2026-04-04 13:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-04-04 14:04 | 2026-04-04 14:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.196.152[.]92` | 1 | 2026-04-04 14:29 | 2026-04-04 14:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.180.238[.]116` | 1 | 2026-04-04 13:54 | 2026-04-04 13:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 35/100 | 🟢 LOW | **15/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `52.203.40[.]22` | US | Amazon Technologies Inc. | **100** ⚠️ | 15 |
| `180.102.22[.]96` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 12 |
| `106.12.108[.]64` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `49.207.40[.]162` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 18 |
| `78.66.44[.]23` | SE | Telia Network Services | **100** ⚠️ | 28 |
| `69.6.221[.]248` | BR | Newfold Digital, Inc. | **100** ⚠️ | 8 |
| `121.73.168[.]9` | NZ | One New Zealand Group Limited | **100** ⚠️ | 16 |
| `120.224.15[.]67` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `14.36.38[.]211` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `49.158.142[.]145` | TW | TFN MEDIA CO., LTD. | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 50 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 13 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 64 cases |
| Tool 34  | Credential Extractor        | ✅ 44 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 29 recon entry/entries in table (3 group(s) consolidating 13 session(s)).

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
_Report time: 2026-04-04T14:32:31Z_
