# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T20:39:41Z |
| **Shift Time** | 20:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **41** |
| Confirmed Threats | **26** |
| False Positives Filtered | **15** (36.6%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **15** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **35** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **22** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `config` | 2 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36` | 1 |
| `Accept-Encoding: gzip` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `test1234` | 2 |
| `12345` | 2 |
| `password1` | 2 |
| `123` | 2 |
| `Host: 13.235.92.17:23` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `test1234` | 2 |
| `root` | `password1` | 2 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36` | `Accept: */*` | 1 |
| `Accept-Encoding: gzip` | `` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test1234` | `112.120.49.14` | 2026-03-24T19:13:44 |
| `root` | `test1234` | `109.233.21.109` | 2026-03-24T19:13:53 |
| `root` | `password1` | `183.245.232.31` | 2026-03-24T20:07:48 |
| `root` | `password1` | `201.28.237.90` | 2026-03-24T20:07:57 |
| `root` | `1Qwertyuiop` | `101.36.127.212` | 2026-03-24T20:32:21 |
| `root` | `3245gs5662d34` | `101.36.127.212` | 2026-03-24T20:32:24 |

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
Source IPs: `101.36.127.212`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **26** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS48847` | WAVES S.A.L | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS56041` | China Mobile communications corporation | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4812` | China Telecom (Group) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ba7b1784deb1

| Field | Detail |
|---|---|
| **Source IP** | `112.120.49[.]14` |
| **First Seen** | 2026-03-24 19:13 |
| **Last Seen** | 2026-03-24 19:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 19:13:40` | `cowrie.session.connect` |
| `2026-03-24 19:13:41` | `cowrie.client.version` |
| `2026-03-24 19:13:41` | `cowrie.client.kex` |
| `2026-03-24 19:13:44` | `cowrie.login.success` |
| `2026-03-24 19:13:45` | `cowrie.direct-tcpip.request` |
| `2026-03-24 19:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.49[.]14` to AbuseIPDB if not already reported
- [ ] Block `112.120.49[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1f20dd0861

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-03-24 19:13 |
| **Last Seen** | 2026-03-24 19:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 19:13:51` | `cowrie.session.connect` |
| `2026-03-24 19:13:52` | `cowrie.client.version` |
| `2026-03-24 19:13:52` | `cowrie.client.kex` |
| `2026-03-24 19:13:53` | `cowrie.login.success` |
| `2026-03-24 19:13:54` | `cowrie.direct-tcpip.request` |
| `2026-03-24 19:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b67fff02861

| Field | Detail |
|---|---|
| **Source IP** | `183.245.232[.]31` |
| **First Seen** | 2026-03-24 20:07 |
| **Last Seen** | 2026-03-24 20:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 20:07:45` | `cowrie.session.connect` |
| `2026-03-24 20:07:46` | `cowrie.client.version` |
| `2026-03-24 20:07:46` | `cowrie.client.kex` |
| `2026-03-24 20:07:48` | `cowrie.login.success` |
| `2026-03-24 20:07:48` | `cowrie.direct-tcpip.request` |
| `2026-03-24 20:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.245.232[.]31` to AbuseIPDB if not already reported
- [ ] Block `183.245.232[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c17cac73ef0

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-03-24 20:07 |
| **Last Seen** | 2026-03-24 20:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 20:07:54` | `cowrie.session.connect` |
| `2026-03-24 20:07:55` | `cowrie.client.version` |
| `2026-03-24 20:07:55` | `cowrie.client.kex` |
| `2026-03-24 20:07:57` | `cowrie.login.success` |
| `2026-03-24 20:07:58` | `cowrie.direct-tcpip.request` |
| `2026-03-24 20:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194c539981e1

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-03-24 20:32 |
| **Last Seen** | 2026-03-24 20:32 |
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
| `2026-03-24 20:32:20` | `cowrie.session.connect` |
| `2026-03-24 20:32:20` | `cowrie.client.version` |
| `2026-03-24 20:32:20` | `cowrie.client.kex` |
| `2026-03-24 20:32:21` | `cowrie.login.success` |
| `2026-03-24 20:32:21` | `cowrie.session.params` |
| `2026-03-24 20:32:21` | `cowrie.command.input` |
| `2026-03-24 20:32:21` | `cowrie.command.failed` |
| `2026-03-24 20:32:21` | `cowrie.log.closed` |
| `2026-03-24 20:32:22` | `cowrie.session.params` |
| `2026-03-24 20:32:22` | `cowrie.command.input` |
| `2026-03-24 20:32:22` | `cowrie.session.file_download` |
| `2026-03-24 20:32:22` | `cowrie.log.closed` |
| `2026-03-24 20:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802855245cd3

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-03-24 20:32 |
| **Last Seen** | 2026-03-24 20:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 20:32:23` | `cowrie.session.connect` |
| `2026-03-24 20:32:23` | `cowrie.client.version` |
| `2026-03-24 20:32:24` | `cowrie.client.kex` |
| `2026-03-24 20:32:24` | `cowrie.login.success` |
| `2026-03-24 20:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.127[.]212` | **5** | 2026-03-24 20:25 | 2026-03-24 20:37 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `34.39.58[.]191` | **3** | 2026-03-24 19:56 | 2026-03-24 20:03 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.24[.]58` | 1 | 2026-03-24 18:59 | 2026-03-24 18:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]144` | 1 | 2026-03-24 20:26 | 2026-03-24 20:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.113.9[.]34` | 1 | 2026-03-24 19:51 | 2026-03-24 19:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.147[.]13` | 1 | 2026-03-24 20:22 | 2026-03-24 20:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.148[.]214` | 1 | 2026-03-24 19:16 | 2026-03-24 19:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.165.1[.]51` | 1 | 2026-03-24 20:18 | 2026-03-24 20:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.53.52[.]68` | 1 | 2026-03-24 19:49 | 2026-03-24 19:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.100[.]104` | 1 | 2026-03-24 19:26 | 2026-03-24 19:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.182.5[.]98` | 1 | 2026-03-24 19:30 | 2026-03-24 19:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.245.61[.]84` | 1 | 2026-03-24 20:32 | 2026-03-24 20:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.2.44[.]54` | 1 | 2026-03-24 20:26 | 2026-03-24 20:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-03-24 19:16 | 2026-03-24 19:16 | 0s | 3 | `T1110.001` | 🟢 LOW |

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
| `180.165.1[.]51` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 1 |
| `183.245.232[.]31` | CN | China Mobile Communications Corporation | **100** ⚠️ | 39 |
| `109.233.21[.]109` | LB | its another /22 already approved for /21 for waves company | **100** ⚠️ | 50 |
| `182.53.52[.]68` | TH | TOT Public Company Limited | **100** ⚠️ | 50 |
| `2.55.100[.]104` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `111.113.9[.]34` | CN | CHINANET ningxia province network | **100** ⚠️ | 0 |
| `122.187.147[.]13` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 0 |
| `201.28.237[.]90` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 0 |
| `45.182.5[.]98` | BR | INOVA GUARUS TELECOM LTDA | **100** ⚠️ | 0 |
| `101.36.127[.]212` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 20 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 41 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (36.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 14 recon entry/entries in table (2 group(s) consolidating 8 session(s)).

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
_Report time: 2026-03-24T20:39:41Z_
