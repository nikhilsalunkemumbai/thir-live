# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T18:39:30Z |
| **Shift Time** | 18:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **38** |
| Confirmed Threats | **35** |
| False Positives Filtered | **3** (7.9%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **15** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **31** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **17** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 2 |
| `default` | 2 |
| `ubuntu` | 2 |
| `oracle` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `3` | 2 |
| `Huawei123` | 1 |
| `1234567` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `3` | 2 |
| `root` | `Huawei123` | 1 |
| `Support` | `1234567` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Huawei123` | `190.129.122.185` | 2026-04-04T16:41:35 |
| `root` | `3245gs5662d34` | `190.129.122.185` | 2026-04-04T16:41:43 |
| `root` | `Qazwsx000` | `165.154.231.129` | 2026-04-04T17:45:05 |
| `root` | `3245gs5662d34` | `165.154.231.129` | 2026-04-04T17:45:09 |
| `root` | `3` | `173.25.186.130` | 2026-04-04T17:54:05 |
| `root` | `3` | `188.149.108.67` | 2026-04-04T17:54:13 |
| `root` | `ubuntu` | `144.31.220.61` | 2026-04-04T17:54:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **38** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 16 |
| libssh | 14 |
| Perl Net::SSH | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `03a80b21afa8...` | Modern SSH client | 12 | 3 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `03a80b21afa8...` | libssh | 12 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
Source IPs: `190.129.122.185`, `165.154.231.129`

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
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS1257` | Tele2 Sverige AB | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | LOW |
| `AS142002` | Scloud Pte Ltd | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS6568` | EMPRESA NACIONAL DE TELECOMUNICACIONES SOCIEDAD ANONIMA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f3793a9a14db

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-04 16:41 |
| **Last Seen** | 2026-04-04 16:41 |
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
| `2026-04-04 16:41:33` | `cowrie.session.connect` |
| `2026-04-04 16:41:33` | `cowrie.client.version` |
| `2026-04-04 16:41:34` | `cowrie.client.kex` |
| `2026-04-04 16:41:35` | `cowrie.login.success` |
| `2026-04-04 16:41:36` | `cowrie.session.params` |
| `2026-04-04 16:41:36` | `cowrie.command.input` |
| `2026-04-04 16:41:36` | `cowrie.command.failed` |
| `2026-04-04 16:41:36` | `cowrie.log.closed` |
| `2026-04-04 16:41:37` | `cowrie.session.params` |
| `2026-04-04 16:41:37` | `cowrie.command.input` |
| `2026-04-04 16:41:38` | `cowrie.session.file_download` |
| `2026-04-04 16:41:38` | `cowrie.log.closed` |
| `2026-04-04 16:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a03a894e003

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-04 16:41 |
| **Last Seen** | 2026-04-04 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 16:41:42` | `cowrie.session.connect` |
| `2026-04-04 16:41:42` | `cowrie.client.version` |
| `2026-04-04 16:41:42` | `cowrie.client.kex` |
| `2026-04-04 16:41:43` | `cowrie.login.success` |
| `2026-04-04 16:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c33c4eefee1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.231[.]129` |
| **First Seen** | 2026-04-04 17:45 |
| **Last Seen** | 2026-04-04 17:45 |
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
| `2026-04-04 17:45:05` | `cowrie.session.connect` |
| `2026-04-04 17:45:05` | `cowrie.client.version` |
| `2026-04-04 17:45:05` | `cowrie.client.kex` |
| `2026-04-04 17:45:05` | `cowrie.login.success` |
| `2026-04-04 17:45:05` | `cowrie.session.params` |
| `2026-04-04 17:45:05` | `cowrie.command.input` |
| `2026-04-04 17:45:05` | `cowrie.command.failed` |
| `2026-04-04 17:45:06` | `cowrie.log.closed` |
| `2026-04-04 17:45:06` | `cowrie.session.params` |
| `2026-04-04 17:45:06` | `cowrie.command.input` |
| `2026-04-04 17:45:06` | `cowrie.session.file_download` |
| `2026-04-04 17:45:06` | `cowrie.log.closed` |
| `2026-04-04 17:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.231[.]129` to AbuseIPDB if not already reported
- [ ] Block `165.154.231[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5377fd80f0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.231[.]129` |
| **First Seen** | 2026-04-04 17:45 |
| **Last Seen** | 2026-04-04 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 17:45:08` | `cowrie.session.connect` |
| `2026-04-04 17:45:08` | `cowrie.client.version` |
| `2026-04-04 17:45:08` | `cowrie.client.kex` |
| `2026-04-04 17:45:09` | `cowrie.login.success` |
| `2026-04-04 17:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.231[.]129` to AbuseIPDB if not already reported
- [ ] Block `165.154.231[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d043455a0f1

| Field | Detail |
|---|---|
| **Source IP** | `173.25.186[.]130` |
| **First Seen** | 2026-04-04 17:54 |
| **Last Seen** | 2026-04-04 17:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 17:54:03` | `cowrie.session.connect` |
| `2026-04-04 17:54:04` | `cowrie.client.version` |
| `2026-04-04 17:54:04` | `cowrie.client.kex` |
| `2026-04-04 17:54:05` | `cowrie.login.success` |
| `2026-04-04 17:54:06` | `cowrie.direct-tcpip.request` |
| `2026-04-04 17:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.25.186[.]130` to AbuseIPDB if not already reported
- [ ] Block `173.25.186[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0155187e6633

| Field | Detail |
|---|---|
| **Source IP** | `188.149.108[.]67` |
| **First Seen** | 2026-04-04 17:54 |
| **Last Seen** | 2026-04-04 17:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 17:54:11` | `cowrie.session.connect` |
| `2026-04-04 17:54:11` | `cowrie.client.version` |
| `2026-04-04 17:54:11` | `cowrie.client.kex` |
| `2026-04-04 17:54:13` | `cowrie.login.success` |
| `2026-04-04 17:54:13` | `cowrie.direct-tcpip.request` |
| `2026-04-04 17:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.149.108[.]67` to AbuseIPDB if not already reported
- [ ] Block `188.149.108[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0eb1f2b7038

| Field | Detail |
|---|---|
| **Source IP** | `144.31.220[.]61` |
| **First Seen** | 2026-04-04 17:54 |
| **Last Seen** | 2026-04-04 17:55 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 17:54:35` | `cowrie.session.connect` |
| `2026-04-04 17:54:35` | `cowrie.client.version` |
| `2026-04-04 17:54:35` | `cowrie.client.kex` |
| `2026-04-04 17:54:36` | `cowrie.login.success` |
| `2026-04-04 17:55:33` | `cowrie.session.file_upload` |
| `2026-04-04 17:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.220[.]61` to AbuseIPDB if not already reported
- [ ] Block `144.31.220[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.154.231[.]129` | **6** | 2026-04-04 16:48 | 2026-04-04 17:47 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.42[.]37` | 1 | 2026-04-04 18:36 | 2026-04-04 18:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.132.249[.]164` | 1 | 2026-04-04 16:44 | 2026-04-04 16:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.192.42[.]14` | 1 | 2026-04-04 17:20 | 2026-04-04 17:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.12[.]179` | 1 | 2026-04-04 17:00 | 2026-04-04 17:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]136` | 1 | 2026-04-04 18:36 | 2026-04-04 18:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.184.85[.]167` | 1 | 2026-04-04 16:56 | 2026-04-04 16:56 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-04-04 16:43 | 2026-04-04 16:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.99.89[.]74` | 1 | 2026-04-04 17:57 | 2026-04-04 17:57 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.242.3[.]105` | 1 | 2026-04-04 16:57 | 2026-04-04 16:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `190.129.122[.]185` | 1 | 2026-04-04 16:41 | 2026-04-04 16:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.28.237[.]90` | 1 | 2026-04-04 17:58 | 2026-04-04 17:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.94.115[.]164` | 1 | 2026-04-04 17:38 | 2026-04-04 17:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.180.166[.]214` | 1 | 2026-04-04 18:17 | 2026-04-04 18:18 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.187.213[.]29` | 1 | 2026-04-04 17:39 | 2026-04-04 17:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.112[.]126` | 1 | 2026-04-04 16:59 | 2026-04-04 16:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.148[.]195` | 1 | 2026-04-04 18:32 | 2026-04-04 18:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.196.106[.]164` | 1 | 2026-04-04 18:17 | 2026-04-04 18:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-04-04 16:41 | 2026-04-04 16:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.105.255[.]56` | 1 | 2026-04-04 17:15 | 2026-04-04 17:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.231.206[.]156` | 1 | 2026-04-04 17:31 | 2026-04-04 17:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]201` | 1 | 2026-04-04 17:31 | 2026-04-04 17:31 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]253` | 1 | 2026-04-04 17:33 | 2026-04-04 17:33 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
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
| `82.196.106[.]164` | SE | Bahnhof AB | **100** ⚠️ | 31 |
| `128.185.12[.]179` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `94.231.206[.]156` | SG | FR ONYPHE | **100** ⚠️ | 47 |
| `185.242.3[.]105` | DE | Felcloud | **100** ⚠️ | 50 |
| `117.192.42[.]14` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 19 |
| `94.231.206[.]253` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `178.178.194[.]136` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `27.123.112[.]126` | IN | Bharti Airtel Limited | **100** ⚠️ | 42 |
| `83.191.181[.]23` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 17 |
| `24.187.213[.]29` | US | TMESISTM ESIS | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 32 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 38 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (7.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 23 recon entry/entries in table (1 group(s) consolidating 6 session(s)).

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
_Report time: 2026-04-04T18:39:30Z_
