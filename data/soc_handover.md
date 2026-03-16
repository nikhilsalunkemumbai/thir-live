# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-16 |
| **Generated At** | 2026-03-16T22:31:35Z |
| **Shift Time** | 22:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1300** |
| Confirmed Threats | **0** |
| False Positives Filtered | **1300** (100.0%) |
| Unique Attacker IPs | **283** |
| Countries of Origin | **0** |
| High Severity Cases | **230** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1070** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **900** |
| Unique Credential Pairs | **609** |
| Unique Usernames | **304** |
| Unique Passwords | **439** |
| Successful Auth Pairs | **217** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 236 |
| `345gs5662d34` | 28 |
| `user` | 20 |
| `test` | 13 |
| `admin` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 89 |
| `123` | 35 |
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 28 |
| `1234` | 23 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 28 |
| `root` | `toor` | 6 |
| `root` | `password` | 5 |
| `root` | `admin` | 5 |

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
| `root` | `root444` | `117.205.3.26` | 2026-03-16T15:48:11 |
| `root` | `root444` | `185.255.47.190` | 2026-03-16T15:48:19 |
| `root` | `!QAZ2wsx` | `206.189.192.239` | 2026-03-16T16:16:15 |
| `root` | `P@ssw0rd` | `206.189.192.239` | 2026-03-16T16:16:21 |
| `root` | `Admin123!` | `206.189.192.239` | 2026-03-16T16:17:00 |
| `root` | `a1s2d3f4` | `206.189.192.239` | 2026-03-16T16:17:13 |
| `root` | `password` | `206.189.192.239` | 2026-03-16T16:17:32 |
| `root` | `aA123456` | `206.189.192.239` | 2026-03-16T16:17:39 |
| `root` | `p@ssw0rd` | `206.189.192.239` | 2026-03-16T16:17:45 |
| `root` | `t0talc0ntr0l4!` | `206.189.192.239` | 2026-03-16T16:17:52 |
| `root` | `123qwe!@` | `157.245.81.49` | 2026-03-16T16:18:23 |
| `root` | `Admin@123` | `206.189.192.239` | 2026-03-16T16:18:30 |
| `root` | `aa123456` | `157.245.81.49` | 2026-03-16T16:18:36 |
| `root` | `Password` | `206.189.192.239` | 2026-03-16T16:18:36 |
| `root` | `102030` | `157.245.81.49` | 2026-03-16T16:18:43 |
| `root` | `1qaz!QAZ` | `206.189.192.239` | 2026-03-16T16:18:55 |
| `root` | `Passw0rd` | `157.245.81.49` | 2026-03-16T16:19:47 |
| `root` | `test@123` | `157.245.81.49` | 2026-03-16T16:20:00 |
| `root` | `12345qwert` | `157.245.81.49` | 2026-03-16T16:20:59 |
| `root` | `Mm123456@` | `172.172.131.149` | 2026-03-16T16:26:46 |
| `root` | `3245gs5662d34` | `172.172.131.149` | 2026-03-16T16:27:10 |
| `root` | `admin` | `178.20.55.16` | 2026-03-16T18:12:27 |
| `root` | `7ujm&UJM` | `8.220.210.5` | 2026-03-16T19:37:39 |
| `root` | `3245gs5662d34` | `8.220.210.5` | 2026-03-16T19:37:42 |
| `root` | `WS@yckj2019` | `47.236.84.126` | 2026-03-16T19:56:40 |
| `root` | `3245gs5662d34` | `47.236.84.126` | 2026-03-16T19:56:42 |
| `root` | `qwer123` | `47.236.84.126` | 2026-03-16T19:58:46 |
| `root` | `HanTianKV` | `47.236.84.126` | 2026-03-16T19:59:36 |
| `root` | `Abcde12345` | `47.236.84.126` | 2026-03-16T20:02:15 |
| `root` | `Cloud@123456` | `47.236.84.126` | 2026-03-16T20:08:34 |
| `root` | `!qaz@WSX` | `159.203.188.188` | 2026-03-16T21:30:28 |
| `root` | `Passw0rd` | `159.203.188.188` | 2026-03-16T21:31:01 |
| `root` | `changemeNOW` | `159.203.188.188` | 2026-03-16T21:31:21 |
| `root` | `Abcd@123456` | `36.134.96.76` | 2026-03-16T21:31:53 |
| `root` | `qazwsxedc` | `159.203.188.188` | 2026-03-16T21:32:28 |
| `root` | `Admin123` | `159.203.188.188` | 2026-03-16T21:32:48 |
| `root` | `abcd@1234` | `159.203.188.188` | 2026-03-16T21:33:14 |
| `root` | `Qq12345678` | `172.210.249.152` | 2026-03-16T21:37:50 |
| `root` | `3245gs5662d34` | `172.210.249.152` | 2026-03-16T21:37:55 |
| `root` | `ZXCzxc123` | `172.210.249.152` | 2026-03-16T21:39:44 |
| `root` | `password` | `204.168.132.131` | 2026-03-16T21:40:08 |
| `root` | `admin` | `204.168.132.131` | 2026-03-16T21:40:44 |
| `root` | `toor` | `204.168.132.131` | 2026-03-16T21:41:20 |
| `root` | `QWEasdzxc123` | `172.210.249.152` | 2026-03-16T21:41:40 |
| `root` | `12345` | `204.168.132.131` | 2026-03-16T21:41:58 |
| `root` | `911911` | `172.210.249.152` | 2026-03-16T21:45:46 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **283** |
| Unique ASNs | **113** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 20 | LOW |
| `AS33765` | TANZANIA TELECOMMUNICATIONS CO. LTD | 16 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 12 | LOW |
| `AS4766` | Korea Telecom | 12 | LOW |
| `AS14061` | DigitalOcean, LLC | 11 | LOW |
| `AS22773` | Cox Communications Inc. | 10 | LOW |
| `AS46562` | Performive LLC | 9 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 8 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 1001 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 666 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 230 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 29 |

---

## 🔕 False Positive Summary (1300 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1300 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1300 cases |
| Tool 34  | Credential Extractor        | ✅ 900 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 283 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1300 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 113 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 9 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-16T22:31:35Z_
