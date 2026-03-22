# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T12:45:41Z |
| **Shift Time** | 12:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **55** |
| Confirmed Threats | **49** |
| False Positives Filtered | **6** (10.9%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **13** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **24** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `unknown` | 2 |
| `deploy` | 1 |
| `mata` | 1 |
| `minecraft` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 3 |
| `12345` | 3 |
| `root1` | 2 |
| `test` | 1 |
| `patrick1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root1` | 2 |
| `deploy` | `1234` | 1 |
| `mata` | `12345` | 1 |
| `minecraft` | `test` | 1 |
| `yocto` | `1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `avonline` | `118.163.178.146` | 2026-03-22T10:40:31 |
| `root` | `123123Qq` | `43.245.143.215` | 2026-03-22T10:40:53 |
| `root` | `3245gs5662d34` | `43.245.143.215` | 2026-03-22T10:40:55 |
| `root` | `root1` | `31.173.0.26` | 2026-03-22T10:50:39 |
| `root` | `root1` | `179.184.85.167` | 2026-03-22T10:50:49 |
| `root` | `root2009` | `180.94.74.82` | 2026-03-22T11:15:33 |

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
Source IPs: `43.245.143.215`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **23** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS55330` | AFGHANTELECOM GOVERNMENT COMMUNICATION NETWORK | 1 | HIGH |
| `AS58717` | Summit Communications Ltd | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS3216` | PJSC Vimpelcom | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-60b681ccd8f0

| Field | Detail |
|---|---|
| **Source IP** | `118.163.178[.]146` |
| **First Seen** | 2026-03-22 10:40 |
| **Last Seen** | 2026-03-22 10:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 10:40:28` | `cowrie.session.connect` |
| `2026-03-22 10:40:29` | `cowrie.client.version` |
| `2026-03-22 10:40:29` | `cowrie.client.kex` |
| `2026-03-22 10:40:31` | `cowrie.login.success` |
| `2026-03-22 10:40:32` | `cowrie.direct-tcpip.request` |
| `2026-03-22 10:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.178[.]146` to AbuseIPDB if not already reported
- [ ] Block `118.163.178[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a273fbbbc7fb

| Field | Detail |
|---|---|
| **Source IP** | `43.245.143[.]215` |
| **First Seen** | 2026-03-22 10:40 |
| **Last Seen** | 2026-03-22 10:40 |
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
| `2026-03-22 10:40:53` | `cowrie.session.connect` |
| `2026-03-22 10:40:53` | `cowrie.client.version` |
| `2026-03-22 10:40:53` | `cowrie.client.kex` |
| `2026-03-22 10:40:53` | `cowrie.login.success` |
| `2026-03-22 10:40:53` | `cowrie.session.params` |
| `2026-03-22 10:40:53` | `cowrie.command.input` |
| `2026-03-22 10:40:53` | `cowrie.command.failed` |
| `2026-03-22 10:40:53` | `cowrie.log.closed` |
| `2026-03-22 10:40:54` | `cowrie.session.params` |
| `2026-03-22 10:40:54` | `cowrie.command.input` |
| `2026-03-22 10:40:54` | `cowrie.session.file_download` |
| `2026-03-22 10:40:54` | `cowrie.log.closed` |
| `2026-03-22 10:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.143[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.245.143[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67a4dd51aca1

| Field | Detail |
|---|---|
| **Source IP** | `43.245.143[.]215` |
| **First Seen** | 2026-03-22 10:40 |
| **Last Seen** | 2026-03-22 10:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 10:40:55` | `cowrie.session.connect` |
| `2026-03-22 10:40:55` | `cowrie.client.version` |
| `2026-03-22 10:40:55` | `cowrie.client.kex` |
| `2026-03-22 10:40:55` | `cowrie.login.success` |
| `2026-03-22 10:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.143[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.245.143[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70cdabc7623c

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]26` |
| **First Seen** | 2026-03-22 10:50 |
| **Last Seen** | 2026-03-22 10:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 10:50:38` | `cowrie.session.connect` |
| `2026-03-22 10:50:38` | `cowrie.client.version` |
| `2026-03-22 10:50:38` | `cowrie.client.kex` |
| `2026-03-22 10:50:39` | `cowrie.login.success` |
| `2026-03-22 10:50:40` | `cowrie.direct-tcpip.request` |
| `2026-03-22 10:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]26` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61dd3517a63a

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-03-22 10:50 |
| **Last Seen** | 2026-03-22 10:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 10:50:45` | `cowrie.session.connect` |
| `2026-03-22 10:50:46` | `cowrie.client.version` |
| `2026-03-22 10:50:46` | `cowrie.client.kex` |
| `2026-03-22 10:50:49` | `cowrie.login.success` |
| `2026-03-22 10:50:50` | `cowrie.direct-tcpip.request` |
| `2026-03-22 10:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8bc44983e3

| Field | Detail |
|---|---|
| **Source IP** | `180.94.74[.]82` |
| **First Seen** | 2026-03-22 11:15 |
| **Last Seen** | 2026-03-22 11:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 11:15:31` | `cowrie.session.connect` |
| `2026-03-22 11:15:31` | `cowrie.client.version` |
| `2026-03-22 11:15:31` | `cowrie.client.kex` |
| `2026-03-22 11:15:33` | `cowrie.login.success` |
| `2026-03-22 11:15:33` | `cowrie.direct-tcpip.request` |
| `2026-03-22 11:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.94.74[.]82` to AbuseIPDB if not already reported
- [ ] Block `180.94.74[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `113.31.124[.]21` | **9** | 2026-03-22 10:28 | 2026-03-22 10:34 | 12m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `43.245.143[.]215` | **9** | 2026-03-22 10:25 | 2026-03-22 10:43 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `172.172.180[.]124` | **6** | 2026-03-22 11:48 | 2026-03-22 12:41 | 1m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `203.130.11[.]3` | **3** | 2026-03-22 12:16 | 2026-03-22 12:35 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `40.124.175[.]60` | **2** | 2026-03-22 11:28 | 2026-03-22 11:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.68[.]11` | 1 | 2026-03-22 12:24 | 2026-03-22 12:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.68.107[.]91` | 1 | 2026-03-22 12:26 | 2026-03-22 12:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `136.56.34[.]147` | 1 | 2026-03-22 10:54 | 2026-03-22 10:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.120[.]70` | 1 | 2026-03-22 12:25 | 2026-03-22 12:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `148.204.11[.]97` | 1 | 2026-03-22 10:25 | 2026-03-22 10:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `188.134.90[.]55` | 1 | 2026-03-22 12:30 | 2026-03-22 12:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `195.218.159[.]123` | 1 | 2026-03-22 12:19 | 2026-03-22 12:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]7` | 1 | 2026-03-22 11:41 | 2026-03-22 11:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-03-22 12:39 | 2026-03-22 12:39 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.98.82[.]61` | 1 | 2026-03-22 11:08 | 2026-03-22 11:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `60.161.14[.]45` | 1 | 2026-03-22 10:35 | 2026-03-22 10:35 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.212.229[.]142` | 1 | 2026-03-22 11:24 | 2026-03-22 11:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `65.20.167[.]78` | 1 | 2026-03-22 11:00 | 2026-03-22 11:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.3.252[.]21` | 1 | 2026-03-22 12:12 | 2026-03-22 12:13 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `31.173.0[.]26` | RU | PJSC MegaFon | **100** ⚠️ | 18 |
| `180.94.74[.]82` | AF | GCN/DCN Networks | **100** ⚠️ | 20 |
| `179.184.85[.]167` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 33 |
| `118.163.178[.]146` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `111.68.107[.]91` | PK | PERN-Pakistan Education & Research Network is an | **100** ⚠️ | 50 |
| `113.31.124[.]21` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |
| `59.98.82[.]61` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 4 |
| `148.204.11[.]97` | MX | Instituto Politecnico Nacional | **100** ⚠️ | 4 |
| `172.172.180[.]124` | US | Microsoft Limited | **100** ⚠️ | 10 |
| `75.3.252[.]21` | US | AT&T Enterprises, LLC | **100** ⚠️ | 25 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 55 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (10.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 19 recon entry/entries in table (5 group(s) consolidating 29 session(s)).

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
_Report time: 2026-03-22T12:45:41Z_
