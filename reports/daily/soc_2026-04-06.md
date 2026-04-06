# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-06 |
| **Generated At** | 2026-04-06T14:44:54Z |
| **Shift Time** | 14:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **51** |
| Confirmed Threats | **50** |
| False Positives Filtered | **1** (2.0%) |
| Unique Attacker IPs | **5** |
| Countries of Origin | **3** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **28** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **48** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **13** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 11 |
| `ubuntu` | 3 |
| `frappe` | 2 |
| `root123` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `1234567890` | 1 |
| `A123456A722` | 1 |
| `Frappe2026!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 11 |
| `root` | `1234567890` | 1 |
| `ubuntu` | `A123456A722` | 1 |
| `frappe` | `Frappe2026!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234567890` | `85.221.139.71` | 2026-04-06T13:14:47 |
| `root` | `qwerasdf` | `103.243.26.174` | 2026-04-06T13:52:58 |
| `root` | `3245gs5662d34` | `103.243.26.174` | 2026-04-06T13:53:01 |
| `root` | `456654` | `103.243.26.174` | 2026-04-06T13:57:46 |
| `root` | `zxcZXC123!@#` | `103.243.26.174` | 2026-04-06T14:04:30 |
| `root` | `root6666$` | `103.243.26.174` | 2026-04-06T14:06:18 |
| `root` | `P@ssword12345@` | `103.243.26.174` | 2026-04-06T14:11:30 |
| `root` | `bbQQ1234` | `103.243.26.174` | 2026-04-06T14:14:48 |
| `root` | `Qazwsx112233#$` | `103.243.26.174` | 2026-04-06T14:16:23 |
| `root` | `1qaz@WSX3edc$RFV$` | `103.243.26.174` | 2026-04-06T14:23:08 |
| `root` | `Server2026#` | `103.243.26.174` | 2026-04-06T14:24:58 |
| `root` | `www123456` | `103.243.26.174` | 2026-04-06T14:28:33 |
| `root` | `admin.123` | `103.243.26.174` | 2026-04-06T14:30:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **51** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 47 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 47 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 47 | 1 | Modern SSH client |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox UKRFB
```
Source IPs: `85.221.139.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.243.26.174`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **5** |
| Unique ASNs | **5** |
| High-Risk ASNs | **3** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS13110` | INEA sp. z o.o. | 1 | LOW |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS701` | Verizon Business | 1 | HIGH |
| `AS24544` | Overcasts Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8a50fe17a7f8

| Field | Detail |
|---|---|
| **Source IP** | `85.221.139[.]71` |
| **First Seen** | 2026-04-06 13:14 |
| **Last Seen** | 2026-04-06 13:17 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox UKRFB` |
| **Download Attempts** | tfxxp://222.97.214[.]29:19634/.i |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 13:14:47` | `cowrie.session.connect` |
| `2026-04-06 13:14:47` | `cowrie.telnet.option` |
| `2026-04-06 13:14:47` | `cowrie.login.success` |
| `2026-04-06 13:14:47` | `cowrie.session.params` |
| `2026-04-06 13:14:47` | `cowrie.command.input` |
| `2026-04-06 13:14:47` | `cowrie.command.input` |
| `2026-04-06 13:14:47` | `cowrie.command.failed` |
| `2026-04-06 13:14:47` | `cowrie.command.input` |
| `2026-04-06 13:14:47` | `cowrie.command.failed` |
| `2026-04-06 13:14:47` | `cowrie.command.input` |
| `2026-04-06 13:14:48` | `cowrie.command.input` |
| `2026-04-06 13:14:48` | `cowrie.command.input` |
| `2026-04-06 13:14:48` | `cowrie.command.input` |
| `2026-04-06 13:14:48` | `cowrie.command.input` |
| `2026-04-06 13:14:48` | `cowrie.command.failed` |
| `2026-04-06 13:14:48` | `cowrie.command.input` |
| `2026-04-06 13:14:48` | `cowrie.command.input` |
| `2026-04-06 13:15:10` | `cowrie.session.file_download` |
| `2026-04-06 13:17:47` | `cowrie.log.closed` |
| `2026-04-06 13:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.221.139[.]71` to AbuseIPDB if not already reported
- [ ] Block `85.221.139[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b013dbb9d47d

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 13:52 |
| **Last Seen** | 2026-04-06 13:53 |
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
| `2026-04-06 13:52:57` | `cowrie.session.connect` |
| `2026-04-06 13:52:57` | `cowrie.client.version` |
| `2026-04-06 13:52:57` | `cowrie.client.kex` |
| `2026-04-06 13:52:58` | `cowrie.login.success` |
| `2026-04-06 13:52:58` | `cowrie.session.params` |
| `2026-04-06 13:52:58` | `cowrie.command.input` |
| `2026-04-06 13:52:58` | `cowrie.command.failed` |
| `2026-04-06 13:52:58` | `cowrie.log.closed` |
| `2026-04-06 13:52:58` | `cowrie.session.params` |
| `2026-04-06 13:52:58` | `cowrie.command.input` |
| `2026-04-06 13:52:58` | `cowrie.session.file_download` |
| `2026-04-06 13:52:58` | `cowrie.log.closed` |
| `2026-04-06 13:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645e81323b6d

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 13:53 |
| **Last Seen** | 2026-04-06 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 13:53:00` | `cowrie.session.connect` |
| `2026-04-06 13:53:00` | `cowrie.client.version` |
| `2026-04-06 13:53:00` | `cowrie.client.kex` |
| `2026-04-06 13:53:01` | `cowrie.login.success` |
| `2026-04-06 13:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cff1a68344b

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 13:57 |
| **Last Seen** | 2026-04-06 13:57 |
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
| `2026-04-06 13:57:46` | `cowrie.session.connect` |
| `2026-04-06 13:57:46` | `cowrie.client.version` |
| `2026-04-06 13:57:46` | `cowrie.client.kex` |
| `2026-04-06 13:57:46` | `cowrie.login.success` |
| `2026-04-06 13:57:46` | `cowrie.session.params` |
| `2026-04-06 13:57:46` | `cowrie.command.input` |
| `2026-04-06 13:57:46` | `cowrie.command.failed` |
| `2026-04-06 13:57:47` | `cowrie.log.closed` |
| `2026-04-06 13:57:47` | `cowrie.session.params` |
| `2026-04-06 13:57:47` | `cowrie.command.input` |
| `2026-04-06 13:57:47` | `cowrie.session.file_download` |
| `2026-04-06 13:57:47` | `cowrie.log.closed` |
| `2026-04-06 13:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b11e3cfaf77

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 13:57 |
| **Last Seen** | 2026-04-06 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 13:57:49` | `cowrie.session.connect` |
| `2026-04-06 13:57:49` | `cowrie.client.version` |
| `2026-04-06 13:57:49` | `cowrie.client.kex` |
| `2026-04-06 13:57:49` | `cowrie.login.success` |
| `2026-04-06 13:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc8be346673

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:04 |
| **Last Seen** | 2026-04-06 14:04 |
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
| `2026-04-06 14:04:29` | `cowrie.session.connect` |
| `2026-04-06 14:04:29` | `cowrie.client.version` |
| `2026-04-06 14:04:29` | `cowrie.client.kex` |
| `2026-04-06 14:04:30` | `cowrie.login.success` |
| `2026-04-06 14:04:30` | `cowrie.session.params` |
| `2026-04-06 14:04:30` | `cowrie.command.input` |
| `2026-04-06 14:04:30` | `cowrie.command.failed` |
| `2026-04-06 14:04:30` | `cowrie.log.closed` |
| `2026-04-06 14:04:30` | `cowrie.session.params` |
| `2026-04-06 14:04:30` | `cowrie.command.input` |
| `2026-04-06 14:04:31` | `cowrie.session.file_download` |
| `2026-04-06 14:04:31` | `cowrie.log.closed` |
| `2026-04-06 14:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d2f487dc8e4

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:04 |
| **Last Seen** | 2026-04-06 14:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:04:32` | `cowrie.session.connect` |
| `2026-04-06 14:04:32` | `cowrie.client.version` |
| `2026-04-06 14:04:32` | `cowrie.client.kex` |
| `2026-04-06 14:04:33` | `cowrie.login.success` |
| `2026-04-06 14:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0886897888c6

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:06 |
| **Last Seen** | 2026-04-06 14:06 |
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
| `2026-04-06 14:06:17` | `cowrie.session.connect` |
| `2026-04-06 14:06:17` | `cowrie.client.version` |
| `2026-04-06 14:06:17` | `cowrie.client.kex` |
| `2026-04-06 14:06:18` | `cowrie.login.success` |
| `2026-04-06 14:06:18` | `cowrie.session.params` |
| `2026-04-06 14:06:18` | `cowrie.command.input` |
| `2026-04-06 14:06:18` | `cowrie.command.failed` |
| `2026-04-06 14:06:18` | `cowrie.log.closed` |
| `2026-04-06 14:06:18` | `cowrie.session.params` |
| `2026-04-06 14:06:18` | `cowrie.command.input` |
| `2026-04-06 14:06:19` | `cowrie.session.file_download` |
| `2026-04-06 14:06:19` | `cowrie.log.closed` |
| `2026-04-06 14:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a35707ed24

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:06 |
| **Last Seen** | 2026-04-06 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:06:20` | `cowrie.session.connect` |
| `2026-04-06 14:06:20` | `cowrie.client.version` |
| `2026-04-06 14:06:21` | `cowrie.client.kex` |
| `2026-04-06 14:06:21` | `cowrie.login.success` |
| `2026-04-06 14:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360f860b45d1

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:11 |
| **Last Seen** | 2026-04-06 14:11 |
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
| `2026-04-06 14:11:29` | `cowrie.session.connect` |
| `2026-04-06 14:11:29` | `cowrie.client.version` |
| `2026-04-06 14:11:29` | `cowrie.client.kex` |
| `2026-04-06 14:11:30` | `cowrie.login.success` |
| `2026-04-06 14:11:30` | `cowrie.session.params` |
| `2026-04-06 14:11:30` | `cowrie.command.input` |
| `2026-04-06 14:11:30` | `cowrie.command.failed` |
| `2026-04-06 14:11:30` | `cowrie.log.closed` |
| `2026-04-06 14:11:30` | `cowrie.session.params` |
| `2026-04-06 14:11:30` | `cowrie.command.input` |
| `2026-04-06 14:11:30` | `cowrie.session.file_download` |
| `2026-04-06 14:11:30` | `cowrie.log.closed` |
| `2026-04-06 14:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21407370b75b

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:11 |
| **Last Seen** | 2026-04-06 14:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:11:32` | `cowrie.session.connect` |
| `2026-04-06 14:11:32` | `cowrie.client.version` |
| `2026-04-06 14:11:32` | `cowrie.client.kex` |
| `2026-04-06 14:11:33` | `cowrie.login.success` |
| `2026-04-06 14:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da982a8c974f

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:14 |
| **Last Seen** | 2026-04-06 14:14 |
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
| `2026-04-06 14:14:48` | `cowrie.session.connect` |
| `2026-04-06 14:14:48` | `cowrie.client.version` |
| `2026-04-06 14:14:48` | `cowrie.client.kex` |
| `2026-04-06 14:14:48` | `cowrie.login.success` |
| `2026-04-06 14:14:49` | `cowrie.session.params` |
| `2026-04-06 14:14:49` | `cowrie.command.input` |
| `2026-04-06 14:14:49` | `cowrie.command.failed` |
| `2026-04-06 14:14:49` | `cowrie.log.closed` |
| `2026-04-06 14:14:49` | `cowrie.session.params` |
| `2026-04-06 14:14:49` | `cowrie.command.input` |
| `2026-04-06 14:14:49` | `cowrie.session.file_download` |
| `2026-04-06 14:14:49` | `cowrie.log.closed` |
| `2026-04-06 14:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429ce4e57d6c

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:14 |
| **Last Seen** | 2026-04-06 14:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:14:51` | `cowrie.session.connect` |
| `2026-04-06 14:14:51` | `cowrie.client.version` |
| `2026-04-06 14:14:51` | `cowrie.client.kex` |
| `2026-04-06 14:14:51` | `cowrie.login.success` |
| `2026-04-06 14:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-023821d92a14

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:16 |
| **Last Seen** | 2026-04-06 14:16 |
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
| `2026-04-06 14:16:22` | `cowrie.session.connect` |
| `2026-04-06 14:16:22` | `cowrie.client.version` |
| `2026-04-06 14:16:22` | `cowrie.client.kex` |
| `2026-04-06 14:16:23` | `cowrie.login.success` |
| `2026-04-06 14:16:23` | `cowrie.session.params` |
| `2026-04-06 14:16:23` | `cowrie.command.input` |
| `2026-04-06 14:16:23` | `cowrie.command.failed` |
| `2026-04-06 14:16:23` | `cowrie.log.closed` |
| `2026-04-06 14:16:23` | `cowrie.session.params` |
| `2026-04-06 14:16:23` | `cowrie.command.input` |
| `2026-04-06 14:16:24` | `cowrie.session.file_download` |
| `2026-04-06 14:16:24` | `cowrie.log.closed` |
| `2026-04-06 14:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4dd1dd96f91

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:16 |
| **Last Seen** | 2026-04-06 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:16:25` | `cowrie.session.connect` |
| `2026-04-06 14:16:25` | `cowrie.client.version` |
| `2026-04-06 14:16:26` | `cowrie.client.kex` |
| `2026-04-06 14:16:26` | `cowrie.login.success` |
| `2026-04-06 14:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ce4be8426a

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:23 |
| **Last Seen** | 2026-04-06 14:23 |
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
| `2026-04-06 14:23:08` | `cowrie.session.connect` |
| `2026-04-06 14:23:08` | `cowrie.client.version` |
| `2026-04-06 14:23:08` | `cowrie.client.kex` |
| `2026-04-06 14:23:08` | `cowrie.login.success` |
| `2026-04-06 14:23:08` | `cowrie.session.params` |
| `2026-04-06 14:23:08` | `cowrie.command.input` |
| `2026-04-06 14:23:08` | `cowrie.command.failed` |
| `2026-04-06 14:23:08` | `cowrie.log.closed` |
| `2026-04-06 14:23:09` | `cowrie.session.params` |
| `2026-04-06 14:23:09` | `cowrie.command.input` |
| `2026-04-06 14:23:09` | `cowrie.session.file_download` |
| `2026-04-06 14:23:09` | `cowrie.log.closed` |
| `2026-04-06 14:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b33c86e1a8

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:23 |
| **Last Seen** | 2026-04-06 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:23:11` | `cowrie.session.connect` |
| `2026-04-06 14:23:11` | `cowrie.client.version` |
| `2026-04-06 14:23:11` | `cowrie.client.kex` |
| `2026-04-06 14:23:11` | `cowrie.login.success` |
| `2026-04-06 14:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2244b04ef04a

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:24 |
| **Last Seen** | 2026-04-06 14:25 |
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
| `2026-04-06 14:24:57` | `cowrie.session.connect` |
| `2026-04-06 14:24:57` | `cowrie.client.version` |
| `2026-04-06 14:24:57` | `cowrie.client.kex` |
| `2026-04-06 14:24:58` | `cowrie.login.success` |
| `2026-04-06 14:24:58` | `cowrie.session.params` |
| `2026-04-06 14:24:58` | `cowrie.command.input` |
| `2026-04-06 14:24:58` | `cowrie.command.failed` |
| `2026-04-06 14:24:58` | `cowrie.log.closed` |
| `2026-04-06 14:24:58` | `cowrie.session.params` |
| `2026-04-06 14:24:58` | `cowrie.command.input` |
| `2026-04-06 14:24:58` | `cowrie.session.file_download` |
| `2026-04-06 14:24:58` | `cowrie.log.closed` |
| `2026-04-06 14:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a4165d82ac

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:25 |
| **Last Seen** | 2026-04-06 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:25:00` | `cowrie.session.connect` |
| `2026-04-06 14:25:00` | `cowrie.client.version` |
| `2026-04-06 14:25:00` | `cowrie.client.kex` |
| `2026-04-06 14:25:01` | `cowrie.login.success` |
| `2026-04-06 14:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ab8d3462a3

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:28 |
| **Last Seen** | 2026-04-06 14:28 |
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
| `2026-04-06 14:28:32` | `cowrie.session.connect` |
| `2026-04-06 14:28:32` | `cowrie.client.version` |
| `2026-04-06 14:28:33` | `cowrie.client.kex` |
| `2026-04-06 14:28:33` | `cowrie.login.success` |
| `2026-04-06 14:28:33` | `cowrie.session.params` |
| `2026-04-06 14:28:33` | `cowrie.command.input` |
| `2026-04-06 14:28:33` | `cowrie.command.failed` |
| `2026-04-06 14:28:33` | `cowrie.log.closed` |
| `2026-04-06 14:28:34` | `cowrie.session.params` |
| `2026-04-06 14:28:34` | `cowrie.command.input` |
| `2026-04-06 14:28:34` | `cowrie.session.file_download` |
| `2026-04-06 14:28:34` | `cowrie.log.closed` |
| `2026-04-06 14:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb2c37d570e6

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:28 |
| **Last Seen** | 2026-04-06 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:28:35` | `cowrie.session.connect` |
| `2026-04-06 14:28:35` | `cowrie.client.version` |
| `2026-04-06 14:28:36` | `cowrie.client.kex` |
| `2026-04-06 14:28:36` | `cowrie.login.success` |
| `2026-04-06 14:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba039b3b1c85

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:30 |
| **Last Seen** | 2026-04-06 14:30 |
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
| `2026-04-06 14:30:18` | `cowrie.session.connect` |
| `2026-04-06 14:30:18` | `cowrie.client.version` |
| `2026-04-06 14:30:18` | `cowrie.client.kex` |
| `2026-04-06 14:30:18` | `cowrie.login.success` |
| `2026-04-06 14:30:18` | `cowrie.session.params` |
| `2026-04-06 14:30:18` | `cowrie.command.input` |
| `2026-04-06 14:30:18` | `cowrie.command.failed` |
| `2026-04-06 14:30:18` | `cowrie.log.closed` |
| `2026-04-06 14:30:19` | `cowrie.session.params` |
| `2026-04-06 14:30:19` | `cowrie.command.input` |
| `2026-04-06 14:30:19` | `cowrie.session.file_download` |
| `2026-04-06 14:30:19` | `cowrie.log.closed` |
| `2026-04-06 14:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b2157ff2d8

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-06 14:30 |
| **Last Seen** | 2026-04-06 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 14:30:21` | `cowrie.session.connect` |
| `2026-04-06 14:30:21` | `cowrie.client.version` |
| `2026-04-06 14:30:21` | `cowrie.client.kex` |
| `2026-04-06 14:30:21` | `cowrie.login.success` |
| `2026-04-06 14:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.243.26[.]174` | **25** | 2026-04-06 13:49 | 2026-04-06 14:30 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `100.35.7[.]246` | 1 | 2026-04-06 14:43 | 2026-04-06 14:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-04-06 13:07 | 2026-04-06 13:08 | 40s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
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
| `100.35.7[.]246` | US | Verizon Business | **100** ⚠️ | 8 |
| `103.243.26[.]174` | HK | HongKong Virtual Internal Server Company Limited | **100** ⚠️ | 50 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 0 |
| `85.221.139[.]71` | PL | INEA sp. z o.o. | **45** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 47 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 25 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 51 cases |
| Tool 34  | Credential Extractor        | ✅ 48 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 5 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 5 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 3 recon entry/entries in table (1 group(s) consolidating 25 session(s)).

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
_Report time: 2026-04-06T14:44:54Z_
