# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-19 |
| **Generated At** | 2026-04-19T10:44:11Z |
| **Shift Time** | 10:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **59** |
| Confirmed Threats | **52** |
| False Positives Filtered | **7** (11.9%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **11** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **45** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **13** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 10 |
| `GET /doc/index.html HTTP/1.1` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36` | 1 |
| `Accept-Encoding: gzip` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `Ab123!@#` | 3 |
| `root04` | 2 |
| `QWERTYUIOP@123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `Ab123!@#` | 3 |
| `root` | `root04` | 2 |
| `root` | `QWERTYUIOP@123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `128.185.116.114` | 2026-04-19T09:14:47 |
| `root` | `A8TVKSDfOo` | `47.112.215.87` | 2026-04-19T09:20:36 |
| `root` | `iNlfiu93vX` | `47.112.215.87` | 2026-04-19T09:21:07 |
| `root` | `root04` | `103.189.235.30` | 2026-04-19T10:30:41 |
| `root` | `3245gs5662d34` | `103.189.235.30` | 2026-04-19T10:30:43 |
| `root` | `Ab123!@#` | `175.198.62.180` | 2026-04-19T10:31:36 |
| `root` | `3245gs5662d34` | `175.198.62.180` | 2026-04-19T10:31:40 |
| `root` | `Qwer4321` | `14.103.118.140` | 2026-04-19T10:33:46 |
| `root` | `3245gs5662d34` | `14.103.118.140` | 2026-04-19T10:33:51 |
| `root` | `root04` | `211.105.129.57` | 2026-04-19T10:36:22 |
| `root` | `3245gs5662d34` | `211.105.129.57` | 2026-04-19T10:36:26 |
| `root` | `QWERTYUIOP@123456` | `123.48.142.249` | 2026-04-19T10:37:24 |
| `root` | `3245gs5662d34` | `123.48.142.249` | 2026-04-19T10:37:28 |
| `root` | `A123456A:` | `211.105.129.57` | 2026-04-19T10:38:10 |
| `root` | `Ab123!@#` | `211.105.129.57` | 2026-04-19T10:39:52 |
| `root` | `Ab123!@#` | `123.48.142.249` | 2026-04-19T10:40:59 |
| `root` | `QWERTYUIOP@123456` | `211.105.129.57` | 2026-04-19T10:41:30 |
| `root` | `A123456A:` | `123.48.142.249` | 2026-04-19T10:42:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **59** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 46 |
| Unknown | 4 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 45 | 10 |
| `1b8acd46a07d...` | Modern SSH client | 2 | 1 |
| `17a5327c6d98...` | Mirai/variant | 2 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 45 | 10 | Modern SSH client |
| `1b8acd46a07d...` | Unknown | 2 | 1 | Modern SSH client |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.189.235.30`, `14.103.118.140`, `175.198.62.180`, `123.48.142.249`, `211.105.129.57`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **14** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS134756` | CHINANET Nanjing Jishan IDC network | 1 | HIGH |
| `AS18126` | Chubu Telecommunications Company, Inc. | 1 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8df33955052a

| Field | Detail |
|---|---|
| **Source IP** | `128.185.116[.]114` |
| **First Seen** | 2026-04-19 09:14 |
| **Last Seen** | 2026-04-19 09:18 |
| **Session Duration** | 209s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 09:14:37` | `cowrie.session.connect` |
| `2026-04-19 09:14:37` | `cowrie.client.version` |
| `2026-04-19 09:14:37` | `cowrie.client.kex` |
| `2026-04-19 09:14:46` | `cowrie.login.failed` |
| `2026-04-19 09:14:47` | `cowrie.login.success` |
| `2026-04-19 09:14:47` | `cowrie.session.params` |
| `2026-04-19 09:14:47` | `cowrie.command.input` |
| `2026-04-19 09:14:47` | `cowrie.command.failed` |
| `2026-04-19 09:14:47` | `cowrie.log.closed` |
| `2026-04-19 09:14:47` | `cowrie.session.params` |
| `2026-04-19 09:14:47` | `cowrie.command.input` |
| `2026-04-19 09:14:47` | `cowrie.log.closed` |
| `2026-04-19 09:14:48` | `cowrie.session.params` |
| `2026-04-19 09:14:48` | `cowrie.command.input` |
| `2026-04-19 09:14:48` | `cowrie.log.closed` |
| `2026-04-19 09:14:48` | `cowrie.session.params` |
| `2026-04-19 09:14:48` | `cowrie.command.input` |
| `2026-04-19 09:14:48` | `cowrie.log.closed` |
| `2026-04-19 09:14:48` | `cowrie.session.params` |
| `2026-04-19 09:14:48` | `cowrie.command.input` |
| `2026-04-19 09:14:48` | `cowrie.log.closed` |
| `2026-04-19 09:14:48` | `cowrie.session.params` |
| `2026-04-19 09:14:48` | `cowrie.command.input` |
| `2026-04-19 09:14:48` | `cowrie.log.closed` |
| `2026-04-19 09:14:48` | `cowrie.session.params` |
| `2026-04-19 09:14:48` | `cowrie.command.input` |
| `2026-04-19 09:14:48` | `cowrie.log.closed` |
| `2026-04-19 09:14:49` | `cowrie.session.params` |
| `2026-04-19 09:14:49` | `cowrie.command.input` |
| `2026-04-19 09:14:49` | `cowrie.log.closed` |
| `2026-04-19 09:14:49` | `cowrie.session.params` |
| `2026-04-19 09:14:49` | `cowrie.command.input` |
| `2026-04-19 09:14:49` | `cowrie.log.closed` |
| `2026-04-19 09:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.116[.]114` to AbuseIPDB if not already reported
- [ ] Block `128.185.116[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a806d84166e6

| Field | Detail |
|---|---|
| **Source IP** | `47.112.215[.]87` |
| **First Seen** | 2026-04-19 09:20 |
| **Last Seen** | 2026-04-19 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 09:20:36` | `cowrie.session.connect` |
| `2026-04-19 09:20:36` | `cowrie.client.version` |
| `2026-04-19 09:20:36` | `cowrie.client.kex` |
| `2026-04-19 09:20:36` | `cowrie.login.success` |
| `2026-04-19 09:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.112.215[.]87` to AbuseIPDB if not already reported
- [ ] Block `47.112.215[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595defa8c0af

| Field | Detail |
|---|---|
| **Source IP** | `47.112.215[.]87` |
| **First Seen** | 2026-04-19 09:21 |
| **Last Seen** | 2026-04-19 09:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 09:21:06` | `cowrie.session.connect` |
| `2026-04-19 09:21:06` | `cowrie.client.version` |
| `2026-04-19 09:21:06` | `cowrie.client.kex` |
| `2026-04-19 09:21:07` | `cowrie.login.success` |
| `2026-04-19 09:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.112.215[.]87` to AbuseIPDB if not already reported
- [ ] Block `47.112.215[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072dd68bc3cd

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]30` |
| **First Seen** | 2026-04-19 10:30 |
| **Last Seen** | 2026-04-19 10:30 |
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
| `2026-04-19 10:30:40` | `cowrie.session.connect` |
| `2026-04-19 10:30:40` | `cowrie.client.version` |
| `2026-04-19 10:30:40` | `cowrie.client.kex` |
| `2026-04-19 10:30:41` | `cowrie.login.success` |
| `2026-04-19 10:30:41` | `cowrie.session.params` |
| `2026-04-19 10:30:41` | `cowrie.command.input` |
| `2026-04-19 10:30:41` | `cowrie.command.failed` |
| `2026-04-19 10:30:41` | `cowrie.log.closed` |
| `2026-04-19 10:30:41` | `cowrie.session.params` |
| `2026-04-19 10:30:41` | `cowrie.command.input` |
| `2026-04-19 10:30:41` | `cowrie.session.file_download` |
| `2026-04-19 10:30:41` | `cowrie.log.closed` |
| `2026-04-19 10:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]30` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e3e2e932156

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]30` |
| **First Seen** | 2026-04-19 10:30 |
| **Last Seen** | 2026-04-19 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:30:43` | `cowrie.session.connect` |
| `2026-04-19 10:30:43` | `cowrie.client.version` |
| `2026-04-19 10:30:43` | `cowrie.client.kex` |
| `2026-04-19 10:30:43` | `cowrie.login.success` |
| `2026-04-19 10:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]30` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e8baf7b2dc

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-04-19 10:31 |
| **Last Seen** | 2026-04-19 10:31 |
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
| `2026-04-19 10:31:35` | `cowrie.session.connect` |
| `2026-04-19 10:31:35` | `cowrie.client.version` |
| `2026-04-19 10:31:35` | `cowrie.client.kex` |
| `2026-04-19 10:31:36` | `cowrie.login.success` |
| `2026-04-19 10:31:36` | `cowrie.session.params` |
| `2026-04-19 10:31:36` | `cowrie.command.input` |
| `2026-04-19 10:31:36` | `cowrie.command.failed` |
| `2026-04-19 10:31:36` | `cowrie.log.closed` |
| `2026-04-19 10:31:37` | `cowrie.session.params` |
| `2026-04-19 10:31:37` | `cowrie.command.input` |
| `2026-04-19 10:31:37` | `cowrie.session.file_download` |
| `2026-04-19 10:31:37` | `cowrie.log.closed` |
| `2026-04-19 10:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38746a32bd15

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-04-19 10:31 |
| **Last Seen** | 2026-04-19 10:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:31:39` | `cowrie.session.connect` |
| `2026-04-19 10:31:39` | `cowrie.client.version` |
| `2026-04-19 10:31:39` | `cowrie.client.kex` |
| `2026-04-19 10:31:40` | `cowrie.login.success` |
| `2026-04-19 10:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df07d44049a2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]140` |
| **First Seen** | 2026-04-19 10:33 |
| **Last Seen** | 2026-04-19 10:33 |
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
| `2026-04-19 10:33:45` | `cowrie.session.connect` |
| `2026-04-19 10:33:45` | `cowrie.client.version` |
| `2026-04-19 10:33:45` | `cowrie.client.kex` |
| `2026-04-19 10:33:46` | `cowrie.login.success` |
| `2026-04-19 10:33:47` | `cowrie.session.params` |
| `2026-04-19 10:33:47` | `cowrie.command.input` |
| `2026-04-19 10:33:47` | `cowrie.command.failed` |
| `2026-04-19 10:33:47` | `cowrie.log.closed` |
| `2026-04-19 10:33:47` | `cowrie.session.params` |
| `2026-04-19 10:33:47` | `cowrie.command.input` |
| `2026-04-19 10:33:47` | `cowrie.session.file_download` |
| `2026-04-19 10:33:47` | `cowrie.log.closed` |
| `2026-04-19 10:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]140` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145a2405bfbc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]140` |
| **First Seen** | 2026-04-19 10:33 |
| **Last Seen** | 2026-04-19 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:33:50` | `cowrie.session.connect` |
| `2026-04-19 10:33:50` | `cowrie.client.version` |
| `2026-04-19 10:33:50` | `cowrie.client.kex` |
| `2026-04-19 10:33:51` | `cowrie.login.success` |
| `2026-04-19 10:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]140` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea80fd3224f

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:36 |
| **Last Seen** | 2026-04-19 10:36 |
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
| `2026-04-19 10:36:21` | `cowrie.session.connect` |
| `2026-04-19 10:36:21` | `cowrie.client.version` |
| `2026-04-19 10:36:21` | `cowrie.client.kex` |
| `2026-04-19 10:36:22` | `cowrie.login.success` |
| `2026-04-19 10:36:22` | `cowrie.session.params` |
| `2026-04-19 10:36:22` | `cowrie.command.input` |
| `2026-04-19 10:36:22` | `cowrie.command.failed` |
| `2026-04-19 10:36:22` | `cowrie.log.closed` |
| `2026-04-19 10:36:23` | `cowrie.session.params` |
| `2026-04-19 10:36:23` | `cowrie.command.input` |
| `2026-04-19 10:36:23` | `cowrie.session.file_download` |
| `2026-04-19 10:36:23` | `cowrie.log.closed` |
| `2026-04-19 10:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad641215548

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:36 |
| **Last Seen** | 2026-04-19 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:36:25` | `cowrie.session.connect` |
| `2026-04-19 10:36:25` | `cowrie.client.version` |
| `2026-04-19 10:36:25` | `cowrie.client.kex` |
| `2026-04-19 10:36:26` | `cowrie.login.success` |
| `2026-04-19 10:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0118503634a

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:37 |
| **Last Seen** | 2026-04-19 10:37 |
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
| `2026-04-19 10:37:23` | `cowrie.session.connect` |
| `2026-04-19 10:37:23` | `cowrie.client.version` |
| `2026-04-19 10:37:23` | `cowrie.client.kex` |
| `2026-04-19 10:37:24` | `cowrie.login.success` |
| `2026-04-19 10:37:24` | `cowrie.session.params` |
| `2026-04-19 10:37:24` | `cowrie.command.input` |
| `2026-04-19 10:37:24` | `cowrie.command.failed` |
| `2026-04-19 10:37:24` | `cowrie.log.closed` |
| `2026-04-19 10:37:25` | `cowrie.session.params` |
| `2026-04-19 10:37:25` | `cowrie.command.input` |
| `2026-04-19 10:37:25` | `cowrie.session.file_download` |
| `2026-04-19 10:37:25` | `cowrie.log.closed` |
| `2026-04-19 10:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fdca99b7d46

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:37 |
| **Last Seen** | 2026-04-19 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:37:27` | `cowrie.session.connect` |
| `2026-04-19 10:37:27` | `cowrie.client.version` |
| `2026-04-19 10:37:27` | `cowrie.client.kex` |
| `2026-04-19 10:37:28` | `cowrie.login.success` |
| `2026-04-19 10:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429e421b1bd1

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:38 |
| **Last Seen** | 2026-04-19 10:38 |
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
| `2026-04-19 10:38:09` | `cowrie.session.connect` |
| `2026-04-19 10:38:09` | `cowrie.client.version` |
| `2026-04-19 10:38:09` | `cowrie.client.kex` |
| `2026-04-19 10:38:10` | `cowrie.login.success` |
| `2026-04-19 10:38:10` | `cowrie.session.params` |
| `2026-04-19 10:38:10` | `cowrie.command.input` |
| `2026-04-19 10:38:10` | `cowrie.command.failed` |
| `2026-04-19 10:38:10` | `cowrie.log.closed` |
| `2026-04-19 10:38:11` | `cowrie.session.params` |
| `2026-04-19 10:38:11` | `cowrie.command.input` |
| `2026-04-19 10:38:11` | `cowrie.session.file_download` |
| `2026-04-19 10:38:11` | `cowrie.log.closed` |
| `2026-04-19 10:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da7211a843c3

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:38 |
| **Last Seen** | 2026-04-19 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:38:13` | `cowrie.session.connect` |
| `2026-04-19 10:38:13` | `cowrie.client.version` |
| `2026-04-19 10:38:13` | `cowrie.client.kex` |
| `2026-04-19 10:38:14` | `cowrie.login.success` |
| `2026-04-19 10:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77744ee5b2f9

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:39 |
| **Last Seen** | 2026-04-19 10:39 |
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
| `2026-04-19 10:39:51` | `cowrie.session.connect` |
| `2026-04-19 10:39:51` | `cowrie.client.version` |
| `2026-04-19 10:39:51` | `cowrie.client.kex` |
| `2026-04-19 10:39:52` | `cowrie.login.success` |
| `2026-04-19 10:39:52` | `cowrie.session.params` |
| `2026-04-19 10:39:52` | `cowrie.command.input` |
| `2026-04-19 10:39:52` | `cowrie.command.failed` |
| `2026-04-19 10:39:52` | `cowrie.log.closed` |
| `2026-04-19 10:39:53` | `cowrie.session.params` |
| `2026-04-19 10:39:53` | `cowrie.command.input` |
| `2026-04-19 10:39:53` | `cowrie.session.file_download` |
| `2026-04-19 10:39:53` | `cowrie.log.closed` |
| `2026-04-19 10:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ee41e2b0e7

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:39 |
| **Last Seen** | 2026-04-19 10:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:39:55` | `cowrie.session.connect` |
| `2026-04-19 10:39:55` | `cowrie.client.version` |
| `2026-04-19 10:39:55` | `cowrie.client.kex` |
| `2026-04-19 10:39:56` | `cowrie.login.success` |
| `2026-04-19 10:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a98a3873b2e

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:40 |
| **Last Seen** | 2026-04-19 10:41 |
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
| `2026-04-19 10:40:58` | `cowrie.session.connect` |
| `2026-04-19 10:40:58` | `cowrie.client.version` |
| `2026-04-19 10:40:58` | `cowrie.client.kex` |
| `2026-04-19 10:40:59` | `cowrie.login.success` |
| `2026-04-19 10:40:59` | `cowrie.session.params` |
| `2026-04-19 10:40:59` | `cowrie.command.input` |
| `2026-04-19 10:40:59` | `cowrie.command.failed` |
| `2026-04-19 10:40:59` | `cowrie.log.closed` |
| `2026-04-19 10:40:59` | `cowrie.session.params` |
| `2026-04-19 10:40:59` | `cowrie.command.input` |
| `2026-04-19 10:41:00` | `cowrie.session.file_download` |
| `2026-04-19 10:41:00` | `cowrie.log.closed` |
| `2026-04-19 10:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7281a6a077c

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:41 |
| **Last Seen** | 2026-04-19 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:41:02` | `cowrie.session.connect` |
| `2026-04-19 10:41:02` | `cowrie.client.version` |
| `2026-04-19 10:41:02` | `cowrie.client.kex` |
| `2026-04-19 10:41:02` | `cowrie.login.success` |
| `2026-04-19 10:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9024a4be03a4

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:41 |
| **Last Seen** | 2026-04-19 10:41 |
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
| `2026-04-19 10:41:29` | `cowrie.session.connect` |
| `2026-04-19 10:41:29` | `cowrie.client.version` |
| `2026-04-19 10:41:29` | `cowrie.client.kex` |
| `2026-04-19 10:41:30` | `cowrie.login.success` |
| `2026-04-19 10:41:30` | `cowrie.session.params` |
| `2026-04-19 10:41:30` | `cowrie.command.input` |
| `2026-04-19 10:41:30` | `cowrie.command.failed` |
| `2026-04-19 10:41:30` | `cowrie.log.closed` |
| `2026-04-19 10:41:31` | `cowrie.session.params` |
| `2026-04-19 10:41:31` | `cowrie.command.input` |
| `2026-04-19 10:41:31` | `cowrie.session.file_download` |
| `2026-04-19 10:41:31` | `cowrie.log.closed` |
| `2026-04-19 10:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0288f9964c17

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:41 |
| **Last Seen** | 2026-04-19 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:41:33` | `cowrie.session.connect` |
| `2026-04-19 10:41:33` | `cowrie.client.version` |
| `2026-04-19 10:41:33` | `cowrie.client.kex` |
| `2026-04-19 10:41:34` | `cowrie.login.success` |
| `2026-04-19 10:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c9b7f809c6b

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:42 |
| **Last Seen** | 2026-04-19 10:42 |
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
| `2026-04-19 10:42:42` | `cowrie.session.connect` |
| `2026-04-19 10:42:42` | `cowrie.client.version` |
| `2026-04-19 10:42:42` | `cowrie.client.kex` |
| `2026-04-19 10:42:42` | `cowrie.login.success` |
| `2026-04-19 10:42:43` | `cowrie.session.params` |
| `2026-04-19 10:42:43` | `cowrie.command.input` |
| `2026-04-19 10:42:43` | `cowrie.command.failed` |
| `2026-04-19 10:42:43` | `cowrie.log.closed` |
| `2026-04-19 10:42:43` | `cowrie.session.params` |
| `2026-04-19 10:42:43` | `cowrie.command.input` |
| `2026-04-19 10:42:43` | `cowrie.session.file_download` |
| `2026-04-19 10:42:43` | `cowrie.log.closed` |
| `2026-04-19 10:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7538b579b4

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:42 |
| **Last Seen** | 2026-04-19 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:42:45` | `cowrie.session.connect` |
| `2026-04-19 10:42:45` | `cowrie.client.version` |
| `2026-04-19 10:42:45` | `cowrie.client.kex` |
| `2026-04-19 10:42:46` | `cowrie.login.success` |
| `2026-04-19 10:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `123.48.142[.]249` | **6** | 2026-04-19 10:31 | 2026-04-19 10:42 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `211.105.129[.]57` | **6** | 2026-04-19 10:33 | 2026-04-19 10:43 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.120[.]147` | **4** | 2026-04-19 10:35 | 2026-04-19 10:42 | 8m | 0 | `T1592` | 🟢 LOW |
| `69.5.20[.]232` | **3** | 2026-04-19 10:35 | 2026-04-19 10:41 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `13.86.115[.]97` | **2** | 2026-04-19 09:15 | 2026-04-19 09:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.189.235[.]30` | 1 | 2026-04-19 10:30 | 2026-04-19 10:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.132.249[.]164` | 1 | 2026-04-19 10:36 | 2026-04-19 10:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.89.89[.]16` | 1 | 2026-04-19 10:29 | 2026-04-19 10:30 | 81s | 0 | `T1592` | 🟢 LOW |
| `118.196.39[.]255` | 1 | 2026-04-19 10:32 | 2026-04-19 10:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]140` | 1 | 2026-04-19 10:33 | 2026-04-19 10:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.123[.]232` | 1 | 2026-04-19 10:35 | 2026-04-19 10:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.198.62[.]180` | 1 | 2026-04-19 10:31 | 2026-04-19 10:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-04-19 10:02 | 2026-04-19 10:02 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `117.89.89[.]16` | CN | CHINANET jiangsu province network | **100** ⚠️ | 0 |
| `47.112.215[.]87` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `69.5.20[.]232` | ID | BYTEPLUS | **100** ⚠️ | 0 |
| `14.103.118[.]140` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `118.196.39[.]255` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 9 |
| `103.189.235[.]30` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 50 |
| `14.103.120[.]147` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `112.132.249[.]164` | CN | China Unicom AnHui province network | **100** ⚠️ | 50 |
| `175.198.62[.]180` | KR | Korea Telecom | **100** ⚠️ | 20 |
| `14.103.123[.]232` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 52 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 59 cases |
| Tool 34  | Credential Extractor        | ✅ 45 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (11.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 13 recon entry/entries in table (5 group(s) consolidating 21 session(s)).

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
_Report time: 2026-04-19T10:44:11Z_
