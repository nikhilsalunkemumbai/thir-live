# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T20:24:19Z |
| **Shift Time** | 20:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **40** |
| False Positives Filtered | **6** (13.0%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **14** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **22** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `support` | 2 |
| `test` | 2 |
| `ubnt` | 1 |
| `11111111` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support2018` | 2 |
| `123` | 2 |
| `123456` | 2 |
| `44` | 2 |
| `Ubnt2010` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support2018` | 2 |
| `root` | `44` | 2 |
| `ubnt` | `Ubnt2010` | 1 |
| `11111111` | `11111111` | 1 |
| `ubuntu` | `letmein` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123321` | `8.216.95.79` | 2026-03-21T19:07:10 |
| `root` | `3245gs5662d34` | `8.216.95.79` | 2026-03-21T19:07:14 |
| `root` | `admin` | `64.190.76.13` | 2026-03-21T19:42:10 |
| `root` | `44` | `111.70.20.166` | 2026-03-21T19:49:55 |
| `root` | `44` | `112.53.70.99` | 2026-03-21T19:50:10 |
| `root` | `founder88` | `94.154.87.39` | 2026-03-21T19:51:59 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox TUJSK
```
Source IPs: `94.154.87.39`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `8.216.95.79`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **24** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS214094` | OSSERVATORIO NESSUNO | 1 | HIGH |
| `AS205714` | Telemach Hrvatska d.o.o. | 1 | MEDIUM |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-656fab488833

| Field | Detail |
|---|---|
| **Source IP** | `8.216.95[.]79` |
| **First Seen** | 2026-03-21 19:07 |
| **Last Seen** | 2026-03-21 19:07 |
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
| `2026-03-21 19:07:09` | `cowrie.session.connect` |
| `2026-03-21 19:07:09` | `cowrie.client.version` |
| `2026-03-21 19:07:09` | `cowrie.client.kex` |
| `2026-03-21 19:07:10` | `cowrie.login.success` |
| `2026-03-21 19:07:10` | `cowrie.session.params` |
| `2026-03-21 19:07:10` | `cowrie.command.input` |
| `2026-03-21 19:07:10` | `cowrie.command.failed` |
| `2026-03-21 19:07:10` | `cowrie.log.closed` |
| `2026-03-21 19:07:11` | `cowrie.session.params` |
| `2026-03-21 19:07:11` | `cowrie.command.input` |
| `2026-03-21 19:07:11` | `cowrie.session.file_download` |
| `2026-03-21 19:07:11` | `cowrie.log.closed` |
| `2026-03-21 19:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.216.95[.]79` to AbuseIPDB if not already reported
- [ ] Block `8.216.95[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ff29996217

| Field | Detail |
|---|---|
| **Source IP** | `8.216.95[.]79` |
| **First Seen** | 2026-03-21 19:07 |
| **Last Seen** | 2026-03-21 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 19:07:13` | `cowrie.session.connect` |
| `2026-03-21 19:07:13` | `cowrie.client.version` |
| `2026-03-21 19:07:13` | `cowrie.client.kex` |
| `2026-03-21 19:07:14` | `cowrie.login.success` |
| `2026-03-21 19:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.216.95[.]79` to AbuseIPDB if not already reported
- [ ] Block `8.216.95[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e73aa48242a4

| Field | Detail |
|---|---|
| **Source IP** | `64.190.76[.]13` |
| **First Seen** | 2026-03-21 19:42 |
| **Last Seen** | 2026-03-21 19:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 19:42:09` | `cowrie.session.connect` |
| `2026-03-21 19:42:09` | `cowrie.client.version` |
| `2026-03-21 19:42:09` | `cowrie.client.kex` |
| `2026-03-21 19:42:10` | `cowrie.client.fingerprint` |
| `2026-03-21 19:42:10` | `cowrie.login.failed` |
| `2026-03-21 19:42:10` | `cowrie.login.success` |
| `2026-03-21 19:42:19` | `cowrie.direct-tcpip.request` |
| `2026-03-21 19:42:19` | `cowrie.direct-tcpip.ja4` |
| `2026-03-21 19:42:19` | `cowrie.direct-tcpip.data` |
| `2026-03-21 19:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.190.76[.]13` to AbuseIPDB if not already reported
- [ ] Block `64.190.76[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d34f98b937

| Field | Detail |
|---|---|
| **Source IP** | `111.70.20[.]166` |
| **First Seen** | 2026-03-21 19:49 |
| **Last Seen** | 2026-03-21 19:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 19:49:51` | `cowrie.session.connect` |
| `2026-03-21 19:49:52` | `cowrie.client.version` |
| `2026-03-21 19:49:52` | `cowrie.client.kex` |
| `2026-03-21 19:49:55` | `cowrie.login.success` |
| `2026-03-21 19:49:55` | `cowrie.direct-tcpip.request` |
| `2026-03-21 19:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.20[.]166` to AbuseIPDB if not already reported
- [ ] Block `111.70.20[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9079d3b323e5

| Field | Detail |
|---|---|
| **Source IP** | `112.53.70[.]99` |
| **First Seen** | 2026-03-21 19:50 |
| **Last Seen** | 2026-03-21 19:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 19:50:06` | `cowrie.session.connect` |
| `2026-03-21 19:50:07` | `cowrie.client.version` |
| `2026-03-21 19:50:07` | `cowrie.client.kex` |
| `2026-03-21 19:50:10` | `cowrie.login.success` |
| `2026-03-21 19:50:11` | `cowrie.direct-tcpip.request` |
| `2026-03-21 19:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.53.70[.]99` to AbuseIPDB if not already reported
- [ ] Block `112.53.70[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1dd5f414c3

| Field | Detail |
|---|---|
| **Source IP** | `94.154.87[.]39` |
| **First Seen** | 2026-03-21 19:51 |
| **Last Seen** | 2026-03-21 19:54 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox TUJSK` |
| **Download Attempts** | 77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1 |
| **Malware Analysis** | 77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 19:51:58` | `cowrie.session.connect` |
| `2026-03-21 19:51:58` | `cowrie.telnet.option` |
| `2026-03-21 19:51:59` | `cowrie.login.success` |
| `2026-03-21 19:51:59` | `cowrie.session.params` |
| `2026-03-21 19:51:59` | `cowrie.command.input` |
| `2026-03-21 19:51:59` | `cowrie.command.input` |
| `2026-03-21 19:51:59` | `cowrie.command.failed` |
| `2026-03-21 19:51:59` | `cowrie.command.input` |
| `2026-03-21 19:51:59` | `cowrie.command.failed` |
| `2026-03-21 19:51:59` | `cowrie.command.input` |
| `2026-03-21 19:51:59` | `cowrie.command.input` |
| `2026-03-21 19:51:59` | `cowrie.command.input` |
| `2026-03-21 19:51:59` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.failed` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:00` | `cowrie.command.input` |
| `2026-03-21 19:52:01` | `cowrie.command.input` |
| `2026-03-21 19:52:01` | `cowrie.command.input` |
| `2026-03-21 19:54:59` | `cowrie.session.file_download` |
| `2026-03-21 19:54:59` | `cowrie.log.closed` |
| `2026-03-21 19:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.87[.]39` to AbuseIPDB if not already reported
- [ ] Block `94.154.87[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `8.216.95[.]79` | **15** | 2026-03-21 18:52 | 2026-03-21 19:10 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.17.207[.]148` | **3** | 2026-03-21 20:08 | 2026-03-21 20:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]135` | **2** | 2026-03-21 18:55 | 2026-03-21 18:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.152.90[.]68` | 1 | 2026-03-21 19:31 | 2026-03-21 19:31 | 4s | 0 | `T1592` | 🟢 LOW |
| `14.22.89[.]30` | 1 | 2026-03-21 19:42 | 2026-03-21 19:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-21 18:38 | 2026-03-21 18:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `175.215.46[.]82` | 1 | 2026-03-21 19:53 | 2026-03-21 19:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.106.59[.]245` | 1 | 2026-03-21 19:56 | 2026-03-21 19:56 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-03-21 18:59 | 2026-03-21 18:59 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.15.224[.]102` | 1 | 2026-03-21 19:39 | 2026-03-21 19:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.178.39[.]106` | 1 | 2026-03-21 19:37 | 2026-03-21 19:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]35` | 1 | 2026-03-21 18:38 | 2026-03-21 18:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.142.79[.]72` | 1 | 2026-03-21 19:15 | 2026-03-21 19:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `65.20.237[.]175` | 1 | 2026-03-21 18:33 | 2026-03-21 18:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.231.206[.]130` | 1 | 2026-03-21 18:55 | 2026-03-21 18:55 | 3s | 0 | `T1592` | 🟢 LOW |
| `98.102.148[.]242` | 1 | 2026-03-21 18:40 | 2026-03-21 18:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.161.232[.]9` | 1 | 2026-03-21 18:53 | 2026-03-21 18:53 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `65.20.237[.]175` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 9 |
| `94.231.206[.]130` | SG | FR ONYPHE | **100** ⚠️ | 38 |
| `49.142.79[.]72` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 11 |
| `111.70.20[.]166` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `64.190.76[.]13` | IT | Davide Silvetti trading as 'Association Osservatorio Nessuno ODV' | **100** ⚠️ | 50 |
| `124.152.90[.]68` | CN | China Unicom Gansu province network | **100** ⚠️ | 32 |
| `94.231.206[.]135` | SG | FR ONYPHE | **100** ⚠️ | 36 |
| `183.106.59[.]245` | KR | Korea Telecom | **100** ⚠️ | 19 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `98.161.232[.]9` | US | Cox Communications | **100** ⚠️ | 34 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (13.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 17 recon entry/entries in table (3 group(s) consolidating 20 session(s)).

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
_Report time: 2026-03-21T20:24:19Z_
