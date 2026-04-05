# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T05:44:38Z |
| **Shift Time** | 05:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **160** |
| Confirmed Threats | **149** |
| False Positives Filtered | **11** (6.9%) |
| Unique Attacker IPs | **54** |
| Countries of Origin | **19** |
| High Severity Cases | **35** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **125** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **96** |
| Unique Credential Pairs | **67** |
| Unique Usernames | **34** |
| Unique Passwords | **65** |
| Successful Auth Pairs | **25** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 35 |
| `345gs5662d34` | 14 |
| `ubuntu` | 5 |
| `admin` | 4 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 15 |
| `345gs5662d34` | 14 |
| `444` | 2 |
| `6` | 2 |
| `admin123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 15 |
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `444` | 2 |
| `root` | `root2003` | 2 |
| `centos` | `raspberry` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `444` | `223.25.108.2` | 2026-04-05T02:12:36 |
| `root` | `444` | `213.55.79.195` | 2026-04-05T02:12:44 |
| `root` | `wangsu@123` | `172.191.157.64` | 2026-04-05T02:44:01 |
| `root` | `3245gs5662d34` | `172.191.157.64` | 2026-04-05T02:44:06 |
| `root` | `QW12ER34TY56` | `183.195.131.206` | 2026-04-05T02:57:34 |
| `root` | `12345Qwert` | `102.88.137.80` | 2026-04-05T04:02:27 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-04-05T04:02:34 |
| `root` | `root2003` | `178.183.125.51` | 2026-04-05T04:09:00 |
| `root` | `root2003` | `175.100.107.238` | 2026-04-05T04:09:12 |
| `root` | `Admin1234567#` | `113.194.203.31` | 2026-04-05T04:49:31 |
| `root` | `3245gs5662d34` | `113.194.203.31` | 2026-04-05T04:49:34 |
| `root` | `asd@123456` | `120.62.8.17` | 2026-04-05T04:56:06 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-04-05T04:56:08 |
| `root` | `Root123456@123` | `124.71.76.200` | 2026-04-05T04:56:25 |
| `root` | `3245gs5662d34` | `124.71.76.200` | 2026-04-05T04:56:33 |
| `root` | `root08` | `120.62.8.17` | 2026-04-05T04:57:11 |
| `root` | `a1234567` | `120.62.8.17` | 2026-04-05T04:59:24 |
| `root` | `abc@123123` | `120.62.8.17` | 2026-04-05T05:00:31 |
| `root` | `Power123` | `120.62.8.17` | 2026-04-05T05:03:39 |
| `root` | `system32` | `120.62.8.17` | 2026-04-05T05:04:42 |
| `root` | `Root14!` | `120.62.8.17` | 2026-04-05T05:05:47 |
| `root` | `lake234me` | `120.62.8.17` | 2026-04-05T05:13:13 |
| `root` | `IdcOffer.com` | `120.62.8.17` | 2026-04-05T05:17:24 |
| `root` | `root8888#$` | `120.62.8.17` | 2026-04-05T05:18:29 |
| `root` | `Qwe555` | `120.62.8.17` | 2026-04-05T05:19:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **160** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 86 |
| OpenSSH | 29 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 76 | 8 |
| `acaa53e0a7d7...` | Mirai/variant | 29 | 29 |
| `713bd9cc9355...` | Mirai/variant | 3 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `e57221504a70...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 76 | 8 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 29 | 29 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `713bd9cc9355...` | libssh | 3 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `e57221504a70...` | libssh | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:eldrbVqTNZlz"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `183.195.131.206`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `124.71.76.200`, `120.62.8.17`, `102.88.137.80`, `113.194.203.31`, `172.191.157.64`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **54** |
| Unique ASNs | **42** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (35)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7acf218a1505

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-04-05 02:12 |
| **Last Seen** | 2026-04-05 02:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 02:12:34` | `cowrie.session.connect` |
| `2026-04-05 02:12:35` | `cowrie.client.version` |
| `2026-04-05 02:12:35` | `cowrie.client.kex` |
| `2026-04-05 02:12:36` | `cowrie.login.success` |
| `2026-04-05 02:12:37` | `cowrie.direct-tcpip.request` |
| `2026-04-05 02:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f2338d31c2

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-04-05 02:12 |
| **Last Seen** | 2026-04-05 02:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 02:12:42` | `cowrie.session.connect` |
| `2026-04-05 02:12:43` | `cowrie.client.version` |
| `2026-04-05 02:12:43` | `cowrie.client.kex` |
| `2026-04-05 02:12:44` | `cowrie.login.success` |
| `2026-04-05 02:12:45` | `cowrie.direct-tcpip.request` |
| `2026-04-05 02:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7063ca92881e

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-05 02:44 |
| **Last Seen** | 2026-04-05 02:44 |
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
| `2026-04-05 02:44:00` | `cowrie.session.connect` |
| `2026-04-05 02:44:00` | `cowrie.client.version` |
| `2026-04-05 02:44:00` | `cowrie.client.kex` |
| `2026-04-05 02:44:01` | `cowrie.login.success` |
| `2026-04-05 02:44:01` | `cowrie.session.params` |
| `2026-04-05 02:44:01` | `cowrie.command.input` |
| `2026-04-05 02:44:01` | `cowrie.command.failed` |
| `2026-04-05 02:44:02` | `cowrie.log.closed` |
| `2026-04-05 02:44:02` | `cowrie.session.params` |
| `2026-04-05 02:44:02` | `cowrie.command.input` |
| `2026-04-05 02:44:02` | `cowrie.session.file_download` |
| `2026-04-05 02:44:02` | `cowrie.log.closed` |
| `2026-04-05 02:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6500d7204d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-05 02:44 |
| **Last Seen** | 2026-04-05 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 02:44:05` | `cowrie.session.connect` |
| `2026-04-05 02:44:05` | `cowrie.client.version` |
| `2026-04-05 02:44:05` | `cowrie.client.kex` |
| `2026-04-05 02:44:06` | `cowrie.login.success` |
| `2026-04-05 02:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-252928dd15e1

| Field | Detail |
|---|---|
| **Source IP** | `183.195.131[.]206` |
| **First Seen** | 2026-04-05 02:57 |
| **Last Seen** | 2026-04-05 02:57 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:eldrbVqTNZlz"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 02:57:33` | `cowrie.session.connect` |
| `2026-04-05 02:57:33` | `cowrie.client.version` |
| `2026-04-05 02:57:33` | `cowrie.client.kex` |
| `2026-04-05 02:57:34` | `cowrie.login.success` |
| `2026-04-05 02:57:34` | `cowrie.session.params` |
| `2026-04-05 02:57:34` | `cowrie.command.input` |
| `2026-04-05 02:57:34` | `cowrie.command.failed` |
| `2026-04-05 02:57:34` | `cowrie.log.closed` |
| `2026-04-05 02:57:35` | `cowrie.session.params` |
| `2026-04-05 02:57:35` | `cowrie.command.input` |
| `2026-04-05 02:57:35` | `cowrie.session.file_download` |
| `2026-04-05 02:57:35` | `cowrie.log.closed` |
| `2026-04-05 02:57:47` | `cowrie.session.params` |
| `2026-04-05 02:57:47` | `cowrie.command.input` |
| `2026-04-05 02:57:47` | `cowrie.log.closed` |
| `2026-04-05 02:57:48` | `cowrie.session.params` |
| `2026-04-05 02:57:48` | `cowrie.command.input` |
| `2026-04-05 02:57:48` | `cowrie.log.closed` |
| `2026-04-05 02:57:48` | `cowrie.session.params` |
| `2026-04-05 02:57:48` | `cowrie.command.input` |
| `2026-04-05 02:57:48` | `cowrie.session.file_download` |
| `2026-04-05 02:57:48` | `cowrie.log.closed` |
| `2026-04-05 02:57:49` | `cowrie.session.params` |
| `2026-04-05 02:57:49` | `cowrie.command.input` |
| `2026-04-05 02:57:49` | `cowrie.log.closed` |
| `2026-04-05 02:57:49` | `cowrie.session.params` |
| `2026-04-05 02:57:49` | `cowrie.command.input` |
| `2026-04-05 02:57:49` | `cowrie.log.closed` |
| `2026-04-05 02:57:50` | `cowrie.session.params` |
| `2026-04-05 02:57:50` | `cowrie.command.input` |
| `2026-04-05 02:57:50` | `cowrie.command.input` |
| `2026-04-05 02:57:50` | `cowrie.log.closed` |
| `2026-04-05 02:57:50` | `cowrie.session.params` |
| `2026-04-05 02:57:50` | `cowrie.command.input` |
| `2026-04-05 02:57:50` | `cowrie.log.closed` |
| `2026-04-05 02:57:51` | `cowrie.session.params` |
| `2026-04-05 02:57:51` | `cowrie.command.input` |
| `2026-04-05 02:57:51` | `cowrie.log.closed` |
| `2026-04-05 02:57:51` | `cowrie.session.params` |
| `2026-04-05 02:57:51` | `cowrie.command.input` |
| `2026-04-05 02:57:51` | `cowrie.log.closed` |
| `2026-04-05 02:57:52` | `cowrie.session.params` |
| `2026-04-05 02:57:52` | `cowrie.command.input` |
| `2026-04-05 02:57:52` | `cowrie.log.closed` |
| `2026-04-05 02:57:52` | `cowrie.session.params` |
| `2026-04-05 02:57:52` | `cowrie.command.input` |
| `2026-04-05 02:57:52` | `cowrie.log.closed` |
| `2026-04-05 02:57:53` | `cowrie.session.params` |
| `2026-04-05 02:57:53` | `cowrie.command.input` |
| `2026-04-05 02:57:53` | `cowrie.log.closed` |
| `2026-04-05 02:57:53` | `cowrie.session.params` |
| `2026-04-05 02:57:53` | `cowrie.command.input` |
| `2026-04-05 02:57:53` | `cowrie.log.closed` |
| `2026-04-05 02:57:54` | `cowrie.session.params` |
| `2026-04-05 02:57:54` | `cowrie.command.input` |
| `2026-04-05 02:57:54` | `cowrie.log.closed` |
| `2026-04-05 02:57:54` | `cowrie.session.params` |
| `2026-04-05 02:57:54` | `cowrie.command.input` |
| `2026-04-05 02:57:54` | `cowrie.log.closed` |
| `2026-04-05 02:57:55` | `cowrie.session.params` |
| `2026-04-05 02:57:55` | `cowrie.command.input` |
| `2026-04-05 02:57:55` | `cowrie.log.closed` |
| `2026-04-05 02:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.195.131[.]206` to AbuseIPDB if not already reported
- [ ] Block `183.195.131[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fc759acd37

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 04:02 |
| **Last Seen** | 2026-04-05 04:02 |
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
| `2026-04-05 04:02:25` | `cowrie.session.connect` |
| `2026-04-05 04:02:25` | `cowrie.client.version` |
| `2026-04-05 04:02:25` | `cowrie.client.kex` |
| `2026-04-05 04:02:27` | `cowrie.login.success` |
| `2026-04-05 04:02:27` | `cowrie.session.params` |
| `2026-04-05 04:02:27` | `cowrie.command.input` |
| `2026-04-05 04:02:27` | `cowrie.command.failed` |
| `2026-04-05 04:02:28` | `cowrie.log.closed` |
| `2026-04-05 04:02:28` | `cowrie.session.params` |
| `2026-04-05 04:02:28` | `cowrie.command.input` |
| `2026-04-05 04:02:29` | `cowrie.session.file_download` |
| `2026-04-05 04:02:29` | `cowrie.log.closed` |
| `2026-04-05 04:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bda31e9653d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 04:02 |
| **Last Seen** | 2026-04-05 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:02:32` | `cowrie.session.connect` |
| `2026-04-05 04:02:32` | `cowrie.client.version` |
| `2026-04-05 04:02:32` | `cowrie.client.kex` |
| `2026-04-05 04:02:34` | `cowrie.login.success` |
| `2026-04-05 04:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24565921254

| Field | Detail |
|---|---|
| **Source IP** | `178.183.125[.]51` |
| **First Seen** | 2026-04-05 04:08 |
| **Last Seen** | 2026-04-05 04:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:08:58` | `cowrie.session.connect` |
| `2026-04-05 04:08:59` | `cowrie.client.version` |
| `2026-04-05 04:08:59` | `cowrie.client.kex` |
| `2026-04-05 04:09:00` | `cowrie.login.success` |
| `2026-04-05 04:09:01` | `cowrie.direct-tcpip.request` |
| `2026-04-05 04:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.183.125[.]51` to AbuseIPDB if not already reported
- [ ] Block `178.183.125[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d5826c7c4c2

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-04-05 04:09 |
| **Last Seen** | 2026-04-05 04:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:09:10` | `cowrie.session.connect` |
| `2026-04-05 04:09:10` | `cowrie.client.version` |
| `2026-04-05 04:09:10` | `cowrie.client.kex` |
| `2026-04-05 04:09:12` | `cowrie.login.success` |
| `2026-04-05 04:09:12` | `cowrie.direct-tcpip.request` |
| `2026-04-05 04:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567af6342491

| Field | Detail |
|---|---|
| **Source IP** | `113.194.203[.]31` |
| **First Seen** | 2026-04-05 04:49 |
| **Last Seen** | 2026-04-05 04:49 |
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
| `2026-04-05 04:49:30` | `cowrie.session.connect` |
| `2026-04-05 04:49:30` | `cowrie.client.version` |
| `2026-04-05 04:49:30` | `cowrie.client.kex` |
| `2026-04-05 04:49:31` | `cowrie.login.success` |
| `2026-04-05 04:49:31` | `cowrie.session.params` |
| `2026-04-05 04:49:31` | `cowrie.command.input` |
| `2026-04-05 04:49:31` | `cowrie.command.failed` |
| `2026-04-05 04:49:31` | `cowrie.log.closed` |
| `2026-04-05 04:49:32` | `cowrie.session.params` |
| `2026-04-05 04:49:32` | `cowrie.command.input` |
| `2026-04-05 04:49:32` | `cowrie.session.file_download` |
| `2026-04-05 04:49:32` | `cowrie.log.closed` |
| `2026-04-05 04:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.194.203[.]31` to AbuseIPDB if not already reported
- [ ] Block `113.194.203[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4dc3f93944f

| Field | Detail |
|---|---|
| **Source IP** | `113.194.203[.]31` |
| **First Seen** | 2026-04-05 04:49 |
| **Last Seen** | 2026-04-05 04:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:49:34` | `cowrie.session.connect` |
| `2026-04-05 04:49:34` | `cowrie.client.version` |
| `2026-04-05 04:49:34` | `cowrie.client.kex` |
| `2026-04-05 04:49:34` | `cowrie.login.success` |
| `2026-04-05 04:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.194.203[.]31` to AbuseIPDB if not already reported
- [ ] Block `113.194.203[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f31ac23e60b

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 04:56 |
| **Last Seen** | 2026-04-05 04:56 |
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
| `2026-04-05 04:56:06` | `cowrie.session.connect` |
| `2026-04-05 04:56:06` | `cowrie.client.version` |
| `2026-04-05 04:56:06` | `cowrie.client.kex` |
| `2026-04-05 04:56:06` | `cowrie.login.success` |
| `2026-04-05 04:56:06` | `cowrie.session.params` |
| `2026-04-05 04:56:06` | `cowrie.command.input` |
| `2026-04-05 04:56:06` | `cowrie.command.failed` |
| `2026-04-05 04:56:06` | `cowrie.log.closed` |
| `2026-04-05 04:56:07` | `cowrie.session.params` |
| `2026-04-05 04:56:07` | `cowrie.command.input` |
| `2026-04-05 04:56:07` | `cowrie.session.file_download` |
| `2026-04-05 04:56:07` | `cowrie.log.closed` |
| `2026-04-05 04:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e43d596bdd

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 04:56 |
| **Last Seen** | 2026-04-05 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:56:08` | `cowrie.session.connect` |
| `2026-04-05 04:56:08` | `cowrie.client.version` |
| `2026-04-05 04:56:08` | `cowrie.client.kex` |
| `2026-04-05 04:56:08` | `cowrie.login.success` |
| `2026-04-05 04:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8971daf817

| Field | Detail |
|---|---|
| **Source IP** | `124.71.76[.]200` |
| **First Seen** | 2026-04-05 04:56 |
| **Last Seen** | 2026-04-05 04:56 |
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
| `2026-04-05 04:56:22` | `cowrie.session.connect` |
| `2026-04-05 04:56:22` | `cowrie.client.version` |
| `2026-04-05 04:56:23` | `cowrie.client.kex` |
| `2026-04-05 04:56:25` | `cowrie.login.success` |
| `2026-04-05 04:56:25` | `cowrie.session.params` |
| `2026-04-05 04:56:25` | `cowrie.command.input` |
| `2026-04-05 04:56:25` | `cowrie.command.failed` |
| `2026-04-05 04:56:26` | `cowrie.log.closed` |
| `2026-04-05 04:56:26` | `cowrie.session.params` |
| `2026-04-05 04:56:26` | `cowrie.command.input` |
| `2026-04-05 04:56:26` | `cowrie.session.file_download` |
| `2026-04-05 04:56:26` | `cowrie.log.closed` |
| `2026-04-05 04:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.71.76[.]200` to AbuseIPDB if not already reported
- [ ] Block `124.71.76[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d740a90a0f76

| Field | Detail |
|---|---|
| **Source IP** | `124.71.76[.]200` |
| **First Seen** | 2026-04-05 04:56 |
| **Last Seen** | 2026-04-05 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:56:32` | `cowrie.session.connect` |
| `2026-04-05 04:56:32` | `cowrie.client.version` |
| `2026-04-05 04:56:33` | `cowrie.client.kex` |
| `2026-04-05 04:56:33` | `cowrie.login.success` |
| `2026-04-05 04:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.71.76[.]200` to AbuseIPDB if not already reported
- [ ] Block `124.71.76[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f23daffbf0

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 04:57 |
| **Last Seen** | 2026-04-05 04:57 |
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
| `2026-04-05 04:57:11` | `cowrie.session.connect` |
| `2026-04-05 04:57:11` | `cowrie.client.version` |
| `2026-04-05 04:57:11` | `cowrie.client.kex` |
| `2026-04-05 04:57:11` | `cowrie.login.success` |
| `2026-04-05 04:57:11` | `cowrie.session.params` |
| `2026-04-05 04:57:11` | `cowrie.command.input` |
| `2026-04-05 04:57:11` | `cowrie.command.failed` |
| `2026-04-05 04:57:11` | `cowrie.log.closed` |
| `2026-04-05 04:57:12` | `cowrie.session.params` |
| `2026-04-05 04:57:12` | `cowrie.command.input` |
| `2026-04-05 04:57:12` | `cowrie.session.file_download` |
| `2026-04-05 04:57:12` | `cowrie.log.closed` |
| `2026-04-05 04:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9562fddc1a

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 04:57 |
| **Last Seen** | 2026-04-05 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:57:13` | `cowrie.session.connect` |
| `2026-04-05 04:57:13` | `cowrie.client.version` |
| `2026-04-05 04:57:13` | `cowrie.client.kex` |
| `2026-04-05 04:57:13` | `cowrie.login.success` |
| `2026-04-05 04:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6889fca34d6

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 04:59 |
| **Last Seen** | 2026-04-05 04:59 |
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
| `2026-04-05 04:59:24` | `cowrie.session.connect` |
| `2026-04-05 04:59:24` | `cowrie.client.version` |
| `2026-04-05 04:59:24` | `cowrie.client.kex` |
| `2026-04-05 04:59:24` | `cowrie.login.success` |
| `2026-04-05 04:59:24` | `cowrie.session.params` |
| `2026-04-05 04:59:24` | `cowrie.command.input` |
| `2026-04-05 04:59:24` | `cowrie.command.failed` |
| `2026-04-05 04:59:24` | `cowrie.log.closed` |
| `2026-04-05 04:59:24` | `cowrie.session.params` |
| `2026-04-05 04:59:24` | `cowrie.command.input` |
| `2026-04-05 04:59:24` | `cowrie.session.file_download` |
| `2026-04-05 04:59:24` | `cowrie.log.closed` |
| `2026-04-05 04:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95eb69cb3a2

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 04:59 |
| **Last Seen** | 2026-04-05 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 04:59:25` | `cowrie.session.connect` |
| `2026-04-05 04:59:25` | `cowrie.client.version` |
| `2026-04-05 04:59:25` | `cowrie.client.kex` |
| `2026-04-05 04:59:25` | `cowrie.login.success` |
| `2026-04-05 04:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81c0be8859ae

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:00 |
| **Last Seen** | 2026-04-05 05:00 |
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
| `2026-04-05 05:00:31` | `cowrie.session.connect` |
| `2026-04-05 05:00:31` | `cowrie.client.version` |
| `2026-04-05 05:00:31` | `cowrie.client.kex` |
| `2026-04-05 05:00:31` | `cowrie.login.success` |
| `2026-04-05 05:00:31` | `cowrie.session.params` |
| `2026-04-05 05:00:31` | `cowrie.command.input` |
| `2026-04-05 05:00:31` | `cowrie.command.failed` |
| `2026-04-05 05:00:31` | `cowrie.log.closed` |
| `2026-04-05 05:00:31` | `cowrie.session.params` |
| `2026-04-05 05:00:31` | `cowrie.command.input` |
| `2026-04-05 05:00:31` | `cowrie.session.file_download` |
| `2026-04-05 05:00:31` | `cowrie.log.closed` |
| `2026-04-05 05:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d72ea71a2f6

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:00 |
| **Last Seen** | 2026-04-05 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:00:32` | `cowrie.session.connect` |
| `2026-04-05 05:00:32` | `cowrie.client.version` |
| `2026-04-05 05:00:32` | `cowrie.client.kex` |
| `2026-04-05 05:00:32` | `cowrie.login.success` |
| `2026-04-05 05:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828244649893

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:03 |
| **Last Seen** | 2026-04-05 05:03 |
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
| `2026-04-05 05:03:39` | `cowrie.session.connect` |
| `2026-04-05 05:03:39` | `cowrie.client.version` |
| `2026-04-05 05:03:39` | `cowrie.client.kex` |
| `2026-04-05 05:03:39` | `cowrie.login.success` |
| `2026-04-05 05:03:39` | `cowrie.session.params` |
| `2026-04-05 05:03:39` | `cowrie.command.input` |
| `2026-04-05 05:03:39` | `cowrie.command.failed` |
| `2026-04-05 05:03:39` | `cowrie.log.closed` |
| `2026-04-05 05:03:40` | `cowrie.session.params` |
| `2026-04-05 05:03:40` | `cowrie.command.input` |
| `2026-04-05 05:03:40` | `cowrie.session.file_download` |
| `2026-04-05 05:03:40` | `cowrie.log.closed` |
| `2026-04-05 05:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3c89b90228

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:03 |
| **Last Seen** | 2026-04-05 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:03:41` | `cowrie.session.connect` |
| `2026-04-05 05:03:41` | `cowrie.client.version` |
| `2026-04-05 05:03:41` | `cowrie.client.kex` |
| `2026-04-05 05:03:41` | `cowrie.login.success` |
| `2026-04-05 05:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd4965322a2

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:04 |
| **Last Seen** | 2026-04-05 05:04 |
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
| `2026-04-05 05:04:42` | `cowrie.session.connect` |
| `2026-04-05 05:04:42` | `cowrie.client.version` |
| `2026-04-05 05:04:42` | `cowrie.client.kex` |
| `2026-04-05 05:04:42` | `cowrie.login.success` |
| `2026-04-05 05:04:42` | `cowrie.session.params` |
| `2026-04-05 05:04:42` | `cowrie.command.input` |
| `2026-04-05 05:04:42` | `cowrie.command.failed` |
| `2026-04-05 05:04:42` | `cowrie.log.closed` |
| `2026-04-05 05:04:42` | `cowrie.session.params` |
| `2026-04-05 05:04:42` | `cowrie.command.input` |
| `2026-04-05 05:04:42` | `cowrie.session.file_download` |
| `2026-04-05 05:04:42` | `cowrie.log.closed` |
| `2026-04-05 05:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791dc7767d54

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:04 |
| **Last Seen** | 2026-04-05 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:04:43` | `cowrie.session.connect` |
| `2026-04-05 05:04:43` | `cowrie.client.version` |
| `2026-04-05 05:04:43` | `cowrie.client.kex` |
| `2026-04-05 05:04:43` | `cowrie.login.success` |
| `2026-04-05 05:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee84deafe62

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:05 |
| **Last Seen** | 2026-04-05 05:05 |
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
| `2026-04-05 05:05:47` | `cowrie.session.connect` |
| `2026-04-05 05:05:47` | `cowrie.client.version` |
| `2026-04-05 05:05:47` | `cowrie.client.kex` |
| `2026-04-05 05:05:47` | `cowrie.login.success` |
| `2026-04-05 05:05:47` | `cowrie.session.params` |
| `2026-04-05 05:05:47` | `cowrie.command.input` |
| `2026-04-05 05:05:47` | `cowrie.command.failed` |
| `2026-04-05 05:05:47` | `cowrie.log.closed` |
| `2026-04-05 05:05:47` | `cowrie.session.params` |
| `2026-04-05 05:05:47` | `cowrie.command.input` |
| `2026-04-05 05:05:47` | `cowrie.session.file_download` |
| `2026-04-05 05:05:47` | `cowrie.log.closed` |
| `2026-04-05 05:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f737e916535d

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:05 |
| **Last Seen** | 2026-04-05 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:05:48` | `cowrie.session.connect` |
| `2026-04-05 05:05:48` | `cowrie.client.version` |
| `2026-04-05 05:05:48` | `cowrie.client.kex` |
| `2026-04-05 05:05:48` | `cowrie.login.success` |
| `2026-04-05 05:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c72a899095d

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:13 |
| **Last Seen** | 2026-04-05 05:13 |
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
| `2026-04-05 05:13:13` | `cowrie.session.connect` |
| `2026-04-05 05:13:13` | `cowrie.client.version` |
| `2026-04-05 05:13:13` | `cowrie.client.kex` |
| `2026-04-05 05:13:13` | `cowrie.login.success` |
| `2026-04-05 05:13:13` | `cowrie.session.params` |
| `2026-04-05 05:13:13` | `cowrie.command.input` |
| `2026-04-05 05:13:13` | `cowrie.command.failed` |
| `2026-04-05 05:13:13` | `cowrie.log.closed` |
| `2026-04-05 05:13:13` | `cowrie.session.params` |
| `2026-04-05 05:13:13` | `cowrie.command.input` |
| `2026-04-05 05:13:13` | `cowrie.session.file_download` |
| `2026-04-05 05:13:13` | `cowrie.log.closed` |
| `2026-04-05 05:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2163d225f557

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:13 |
| **Last Seen** | 2026-04-05 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:13:15` | `cowrie.session.connect` |
| `2026-04-05 05:13:15` | `cowrie.client.version` |
| `2026-04-05 05:13:15` | `cowrie.client.kex` |
| `2026-04-05 05:13:15` | `cowrie.login.success` |
| `2026-04-05 05:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adca3c2b10fa

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:17 |
| **Last Seen** | 2026-04-05 05:17 |
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
| `2026-04-05 05:17:24` | `cowrie.session.connect` |
| `2026-04-05 05:17:24` | `cowrie.client.version` |
| `2026-04-05 05:17:24` | `cowrie.client.kex` |
| `2026-04-05 05:17:24` | `cowrie.login.success` |
| `2026-04-05 05:17:24` | `cowrie.session.params` |
| `2026-04-05 05:17:24` | `cowrie.command.input` |
| `2026-04-05 05:17:24` | `cowrie.command.failed` |
| `2026-04-05 05:17:24` | `cowrie.log.closed` |
| `2026-04-05 05:17:24` | `cowrie.session.params` |
| `2026-04-05 05:17:24` | `cowrie.command.input` |
| `2026-04-05 05:17:24` | `cowrie.session.file_download` |
| `2026-04-05 05:17:24` | `cowrie.log.closed` |
| `2026-04-05 05:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6aacc00cb5

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:17 |
| **Last Seen** | 2026-04-05 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:17:25` | `cowrie.session.connect` |
| `2026-04-05 05:17:25` | `cowrie.client.version` |
| `2026-04-05 05:17:25` | `cowrie.client.kex` |
| `2026-04-05 05:17:25` | `cowrie.login.success` |
| `2026-04-05 05:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009b723eb19c

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:18 |
| **Last Seen** | 2026-04-05 05:18 |
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
| `2026-04-05 05:18:28` | `cowrie.session.connect` |
| `2026-04-05 05:18:28` | `cowrie.client.version` |
| `2026-04-05 05:18:28` | `cowrie.client.kex` |
| `2026-04-05 05:18:29` | `cowrie.login.success` |
| `2026-04-05 05:18:29` | `cowrie.session.params` |
| `2026-04-05 05:18:29` | `cowrie.command.input` |
| `2026-04-05 05:18:29` | `cowrie.command.failed` |
| `2026-04-05 05:18:29` | `cowrie.log.closed` |
| `2026-04-05 05:18:29` | `cowrie.session.params` |
| `2026-04-05 05:18:29` | `cowrie.command.input` |
| `2026-04-05 05:18:29` | `cowrie.session.file_download` |
| `2026-04-05 05:18:29` | `cowrie.log.closed` |
| `2026-04-05 05:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db8285f8486

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:18 |
| **Last Seen** | 2026-04-05 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:18:30` | `cowrie.session.connect` |
| `2026-04-05 05:18:30` | `cowrie.client.version` |
| `2026-04-05 05:18:30` | `cowrie.client.kex` |
| `2026-04-05 05:18:30` | `cowrie.login.success` |
| `2026-04-05 05:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee89deb54252

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:19 |
| **Last Seen** | 2026-04-05 05:19 |
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
| `2026-04-05 05:19:36` | `cowrie.session.connect` |
| `2026-04-05 05:19:36` | `cowrie.client.version` |
| `2026-04-05 05:19:36` | `cowrie.client.kex` |
| `2026-04-05 05:19:36` | `cowrie.login.success` |
| `2026-04-05 05:19:36` | `cowrie.session.params` |
| `2026-04-05 05:19:36` | `cowrie.command.input` |
| `2026-04-05 05:19:36` | `cowrie.command.failed` |
| `2026-04-05 05:19:36` | `cowrie.log.closed` |
| `2026-04-05 05:19:36` | `cowrie.session.params` |
| `2026-04-05 05:19:36` | `cowrie.command.input` |
| `2026-04-05 05:19:36` | `cowrie.session.file_download` |
| `2026-04-05 05:19:36` | `cowrie.log.closed` |
| `2026-04-05 05:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d265e84fa3

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-05 05:19 |
| **Last Seen** | 2026-04-05 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 05:19:37` | `cowrie.session.connect` |
| `2026-04-05 05:19:37` | `cowrie.client.version` |
| `2026-04-05 05:19:37` | `cowrie.client.kex` |
| `2026-04-05 05:19:37` | `cowrie.login.success` |
| `2026-04-05 05:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.62.8[.]17` | **25** | 2026-04-05 04:54 | 2026-04-05 05:20 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `124.29.214[.]206` | **25** | 2026-04-05 03:20 | 2026-04-05 03:25 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `183.195.131[.]206` | **14** | 2026-04-05 02:48 | 2026-04-05 03:00 | 24m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **6** | 2026-04-05 03:20 | 2026-04-05 03:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.71.76[.]200` | **3** | 2026-04-05 04:06 | 2026-04-05 05:02 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.123.41[.]71` | **3** | 2026-04-05 03:22 | 2026-04-05 03:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.227.203[.]162` | 1 | 2026-04-05 04:58 | 2026-04-05 05:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-04-05 04:02 | 2026-04-05 04:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.68.52[.]210` | 1 | 2026-04-05 02:14 | 2026-04-05 02:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.181[.]87` | 1 | 2026-04-05 04:32 | 2026-04-05 04:32 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.120.115[.]152` | 1 | 2026-04-05 03:29 | 2026-04-05 03:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.147.162[.]92` | 1 | 2026-04-05 05:25 | 2026-04-05 05:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.194.203[.]31` | 1 | 2026-04-05 04:49 | 2026-04-05 04:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.38[.]223` | 1 | 2026-04-05 04:12 | 2026-04-05 04:12 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.77[.]176` | 1 | 2026-04-05 04:54 | 2026-04-05 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.187.230[.]116` | 1 | 2026-04-05 02:16 | 2026-04-05 02:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.52.202[.]92` | 1 | 2026-04-05 05:24 | 2026-04-05 05:24 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.201[.]98` | 1 | 2026-04-05 03:34 | 2026-04-05 03:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.244.61[.]137` | 1 | 2026-04-05 03:11 | 2026-04-05 03:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.191.157[.]64` | 1 | 2026-04-05 02:44 | 2026-04-05 02:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.10.204[.]72` | 1 | 2026-04-05 02:51 | 2026-04-05 02:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]192` | 1 | 2026-04-05 02:36 | 2026-04-05 02:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.153.91[.]15` | 1 | 2026-04-05 04:04 | 2026-04-05 04:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.235[.]114` | 1 | 2026-04-05 04:53 | 2026-04-05 04:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-04-05 04:51 | 2026-04-05 04:51 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.145[.]212` | 1 | 2026-04-05 02:31 | 2026-04-05 02:33 | 79s | 0 | `T1592` | 🟢 LOW |
| `188.36.7[.]196` | 1 | 2026-04-05 02:55 | 2026-04-05 02:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.82.20[.]241` | 1 | 2026-04-05 04:28 | 2026-04-05 04:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.192.247[.]84` | 1 | 2026-04-05 05:30 | 2026-04-05 05:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.172.203[.]43` | 1 | 2026-04-05 04:47 | 2026-04-05 04:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.114.206[.]138` | 1 | 2026-04-05 05:37 | 2026-04-05 05:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `223.100.248[.]64` | 1 | 2026-04-05 04:55 | 2026-04-05 04:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `27.223.98[.]117` | 1 | 2026-04-05 03:14 | 2026-04-05 03:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.39.130[.]144` | 1 | 2026-04-05 04:46 | 2026-04-05 04:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.155.114[.]62` | 1 | 2026-04-05 04:01 | 2026-04-05 04:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.163.231[.]187` | 1 | 2026-04-05 05:05 | 2026-04-05 05:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.165.186[.]119` | 1 | 2026-04-05 03:50 | 2026-04-05 03:50 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.118.49[.]18` | 1 | 2026-04-05 04:27 | 2026-04-05 04:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.149[.]239` | 1 | 2026-04-05 03:53 | 2026-04-05 03:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.250[.]244` | 1 | 2026-04-05 02:52 | 2026-04-05 02:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-04-05 02:33 | 2026-04-05 02:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.249.117[.]28` | 1 | 2026-04-05 02:11 | 2026-04-05 02:11 | 12s | 0 | `T1592` | 🟢 LOW |
| `90.188.38[.]227` | 1 | 2026-04-05 02:31 | 2026-04-05 02:32 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.79.108[.]51` | 1 | 2026-04-05 05:10 | 2026-04-05 05:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
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
| `180.76.235[.]114` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 1 |
| `120.48.77[.]176` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 12 |
| `43.165.186[.]119` | JP | ACEVILLE PTE.LTD. | **100** ⚠️ | 50 |
| `45.118.49[.]18` | IN | Netaji Subhas University of Technology, West Campus (NSUT) | **100** ⚠️ | 50 |
| `172.191.157[.]64` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `213.55.79[.]195` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `180.76.52[.]146` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 30 |
| `183.195.131[.]206` | CN | China Mobile Communications Corporation - shanghai company | **100** ⚠️ | 45 |
| `113.147.162[.]92` | JP | DION (KDDI CORPORATION) | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 118 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 35 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 160 cases |
| Tool 34  | Credential Extractor        | ✅ 96 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 54 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (6.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 42 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 35 priority case(s) shown individually · 44 recon entry/entries in table (6 group(s) consolidating 76 session(s)).

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
_Report time: 2026-04-05T05:44:38Z_
