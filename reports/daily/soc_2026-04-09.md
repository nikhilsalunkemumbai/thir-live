# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T07:19:16Z |
| **Shift Time** | 07:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **51** |
| Confirmed Threats | **48** |
| False Positives Filtered | **3** (5.9%) |
| Unique Attacker IPs | **13** |
| Countries of Origin | **9** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **39** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **22** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **6** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 6 |
| `kobo` | 1 |
| `teamspeak` | 1 |
| `ubuntu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `master` | 1 |
| `root2026@@` | 1 |
| `kobo` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `master` | 1 |
| `root` | `root2026@@` | 1 |
| `kobo` | `kobo` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `master` | `103.219.234.109` | 2026-04-09T06:07:54 |
| `root` | `3245gs5662d34` | `103.219.234.109` | 2026-04-09T06:08:01 |
| `root` | `root2026@@` | `43.160.233.150` | 2026-04-09T06:08:09 |
| `root` | `3245gs5662d34` | `43.160.233.150` | 2026-04-09T06:08:11 |
| `root` | `Cc1234567` | `171.25.158.58` | 2026-04-09T06:09:46 |
| `root` | `3245gs5662d34` | `171.25.158.58` | 2026-04-09T06:09:50 |
| `root` | `Qq@123456` | `103.100.69.141` | 2026-04-09T06:10:10 |
| `root` | `3245gs5662d34` | `103.100.69.141` | 2026-04-09T06:10:13 |
| `root` | `A.123456` | `116.111.2.94` | 2026-04-09T06:10:21 |
| `root` | `3245gs5662d34` | `116.111.2.94` | 2026-04-09T06:10:24 |
| `root` | `root1111111!` | `201.186.40.161` | 2026-04-09T06:10:42 |
| `root` | `3245gs5662d34` | `201.186.40.161` | 2026-04-09T06:10:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **51** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 44 |
| OpenSSH | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 32 | 7 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |
| `ec9ea89c70f5...` | Mirai/variant | 1 | 1 |
| `e788c657d1a2...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 32 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 2 | — |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `ec9ea89c70f5...` | OpenSSH | 1 | 1 | Mirai/variant |
| `e788c657d1a2...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `201.186.40.161`, `103.219.234.109`, `116.111.2.94`, `43.160.233.150`, `171.25.158.58`, `103.100.69.141`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **13** |
| Unique ASNs | **13** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS14117` | Telefonica del Sur S.A. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS35100` | Patrik Lagerman | 1 | HIGH |
| `AS269822` | COLOMBIA MAS TV S.A.S | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6458effa6d81

| Field | Detail |
|---|---|
| **Source IP** | `103.219.234[.]109` |
| **First Seen** | 2026-04-09 06:07 |
| **Last Seen** | 2026-04-09 06:08 |
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
| `2026-04-09 06:07:52` | `cowrie.session.connect` |
| `2026-04-09 06:07:52` | `cowrie.client.version` |
| `2026-04-09 06:07:52` | `cowrie.client.kex` |
| `2026-04-09 06:07:54` | `cowrie.login.success` |
| `2026-04-09 06:07:54` | `cowrie.session.params` |
| `2026-04-09 06:07:54` | `cowrie.command.input` |
| `2026-04-09 06:07:54` | `cowrie.command.failed` |
| `2026-04-09 06:07:55` | `cowrie.log.closed` |
| `2026-04-09 06:07:56` | `cowrie.session.params` |
| `2026-04-09 06:07:56` | `cowrie.command.input` |
| `2026-04-09 06:07:56` | `cowrie.session.file_download` |
| `2026-04-09 06:07:56` | `cowrie.log.closed` |
| `2026-04-09 06:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.219.234[.]109` to AbuseIPDB if not already reported
- [ ] Block `103.219.234[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28cb4fb18bc8

| Field | Detail |
|---|---|
| **Source IP** | `103.219.234[.]109` |
| **First Seen** | 2026-04-09 06:08 |
| **Last Seen** | 2026-04-09 06:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 06:08:00` | `cowrie.session.connect` |
| `2026-04-09 06:08:00` | `cowrie.client.version` |
| `2026-04-09 06:08:00` | `cowrie.client.kex` |
| `2026-04-09 06:08:01` | `cowrie.login.success` |
| `2026-04-09 06:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.219.234[.]109` to AbuseIPDB if not already reported
- [ ] Block `103.219.234[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51afe8407b6d

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-09 06:08 |
| **Last Seen** | 2026-04-09 06:08 |
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
| `2026-04-09 06:08:08` | `cowrie.session.connect` |
| `2026-04-09 06:08:08` | `cowrie.client.version` |
| `2026-04-09 06:08:08` | `cowrie.client.kex` |
| `2026-04-09 06:08:09` | `cowrie.login.success` |
| `2026-04-09 06:08:09` | `cowrie.session.params` |
| `2026-04-09 06:08:09` | `cowrie.command.input` |
| `2026-04-09 06:08:09` | `cowrie.command.failed` |
| `2026-04-09 06:08:09` | `cowrie.log.closed` |
| `2026-04-09 06:08:09` | `cowrie.session.params` |
| `2026-04-09 06:08:09` | `cowrie.command.input` |
| `2026-04-09 06:08:09` | `cowrie.session.file_download` |
| `2026-04-09 06:08:09` | `cowrie.log.closed` |
| `2026-04-09 06:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8743cb261982

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-09 06:08 |
| **Last Seen** | 2026-04-09 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 06:08:11` | `cowrie.session.connect` |
| `2026-04-09 06:08:11` | `cowrie.client.version` |
| `2026-04-09 06:08:11` | `cowrie.client.kex` |
| `2026-04-09 06:08:11` | `cowrie.login.success` |
| `2026-04-09 06:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a209de206aa

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]58` |
| **First Seen** | 2026-04-09 06:09 |
| **Last Seen** | 2026-04-09 06:09 |
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
| `2026-04-09 06:09:45` | `cowrie.session.connect` |
| `2026-04-09 06:09:45` | `cowrie.client.version` |
| `2026-04-09 06:09:45` | `cowrie.client.kex` |
| `2026-04-09 06:09:46` | `cowrie.login.success` |
| `2026-04-09 06:09:46` | `cowrie.session.params` |
| `2026-04-09 06:09:46` | `cowrie.command.input` |
| `2026-04-09 06:09:46` | `cowrie.command.failed` |
| `2026-04-09 06:09:46` | `cowrie.log.closed` |
| `2026-04-09 06:09:47` | `cowrie.session.params` |
| `2026-04-09 06:09:47` | `cowrie.command.input` |
| `2026-04-09 06:09:47` | `cowrie.session.file_download` |
| `2026-04-09 06:09:47` | `cowrie.log.closed` |
| `2026-04-09 06:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]58` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c772f898ca44

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]58` |
| **First Seen** | 2026-04-09 06:09 |
| **Last Seen** | 2026-04-09 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 06:09:49` | `cowrie.session.connect` |
| `2026-04-09 06:09:49` | `cowrie.client.version` |
| `2026-04-09 06:09:49` | `cowrie.client.kex` |
| `2026-04-09 06:09:50` | `cowrie.login.success` |
| `2026-04-09 06:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]58` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a079a5b11b5a

| Field | Detail |
|---|---|
| **Source IP** | `103.100.69[.]141` |
| **First Seen** | 2026-04-09 06:10 |
| **Last Seen** | 2026-04-09 06:10 |
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
| `2026-04-09 06:10:06` | `cowrie.session.connect` |
| `2026-04-09 06:10:06` | `cowrie.client.version` |
| `2026-04-09 06:10:07` | `cowrie.client.kex` |
| `2026-04-09 06:10:10` | `cowrie.login.success` |
| `2026-04-09 06:10:11` | `cowrie.session.params` |
| `2026-04-09 06:10:11` | `cowrie.command.input` |
| `2026-04-09 06:10:11` | `cowrie.command.failed` |
| `2026-04-09 06:10:11` | `cowrie.log.closed` |
| `2026-04-09 06:10:11` | `cowrie.session.params` |
| `2026-04-09 06:10:11` | `cowrie.command.input` |
| `2026-04-09 06:10:11` | `cowrie.session.file_download` |
| `2026-04-09 06:10:11` | `cowrie.log.closed` |
| `2026-04-09 06:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.100.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `103.100.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c512388c7670

| Field | Detail |
|---|---|
| **Source IP** | `103.100.69[.]141` |
| **First Seen** | 2026-04-09 06:10 |
| **Last Seen** | 2026-04-09 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 06:10:13` | `cowrie.session.connect` |
| `2026-04-09 06:10:13` | `cowrie.client.version` |
| `2026-04-09 06:10:13` | `cowrie.client.kex` |
| `2026-04-09 06:10:13` | `cowrie.login.success` |
| `2026-04-09 06:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.100.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `103.100.69[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed75b1e6db42

| Field | Detail |
|---|---|
| **Source IP** | `116.111.2[.]94` |
| **First Seen** | 2026-04-09 06:10 |
| **Last Seen** | 2026-04-09 06:10 |
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
| `2026-04-09 06:10:21` | `cowrie.session.connect` |
| `2026-04-09 06:10:21` | `cowrie.client.version` |
| `2026-04-09 06:10:21` | `cowrie.client.kex` |
| `2026-04-09 06:10:21` | `cowrie.login.success` |
| `2026-04-09 06:10:21` | `cowrie.session.params` |
| `2026-04-09 06:10:21` | `cowrie.command.input` |
| `2026-04-09 06:10:21` | `cowrie.command.failed` |
| `2026-04-09 06:10:21` | `cowrie.log.closed` |
| `2026-04-09 06:10:22` | `cowrie.session.params` |
| `2026-04-09 06:10:22` | `cowrie.command.input` |
| `2026-04-09 06:10:22` | `cowrie.session.file_download` |
| `2026-04-09 06:10:22` | `cowrie.log.closed` |
| `2026-04-09 06:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.111.2[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.111.2[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03fceddc74b9

| Field | Detail |
|---|---|
| **Source IP** | `116.111.2[.]94` |
| **First Seen** | 2026-04-09 06:10 |
| **Last Seen** | 2026-04-09 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 06:10:24` | `cowrie.session.connect` |
| `2026-04-09 06:10:24` | `cowrie.client.version` |
| `2026-04-09 06:10:24` | `cowrie.client.kex` |
| `2026-04-09 06:10:24` | `cowrie.login.success` |
| `2026-04-09 06:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.111.2[.]94` to AbuseIPDB if not already reported
- [ ] Block `116.111.2[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4951b41432bd

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]161` |
| **First Seen** | 2026-04-09 06:10 |
| **Last Seen** | 2026-04-09 06:10 |
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
| `2026-04-09 06:10:40` | `cowrie.session.connect` |
| `2026-04-09 06:10:40` | `cowrie.client.version` |
| `2026-04-09 06:10:40` | `cowrie.client.kex` |
| `2026-04-09 06:10:42` | `cowrie.login.success` |
| `2026-04-09 06:10:42` | `cowrie.session.params` |
| `2026-04-09 06:10:42` | `cowrie.command.input` |
| `2026-04-09 06:10:42` | `cowrie.command.failed` |
| `2026-04-09 06:10:43` | `cowrie.log.closed` |
| `2026-04-09 06:10:44` | `cowrie.session.params` |
| `2026-04-09 06:10:44` | `cowrie.command.input` |
| `2026-04-09 06:10:44` | `cowrie.session.file_download` |
| `2026-04-09 06:10:44` | `cowrie.log.closed` |
| `2026-04-09 06:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]161` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0866218e05ea

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]161` |
| **First Seen** | 2026-04-09 06:10 |
| **Last Seen** | 2026-04-09 06:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 06:10:48` | `cowrie.session.connect` |
| `2026-04-09 06:10:48` | `cowrie.client.version` |
| `2026-04-09 06:10:48` | `cowrie.client.kex` |
| `2026-04-09 06:10:50` | `cowrie.login.success` |
| `2026-04-09 06:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]161` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `203.25.208[.]110` | **24** | 2026-04-09 06:09 | 2026-04-09 07:17 | 29m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.119[.]146` | **3** | 2026-04-09 06:53 | 2026-04-09 06:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.100.69[.]141` | 1 | 2026-04-09 06:10 | 2026-04-09 06:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.219.234[.]109` | 1 | 2026-04-09 06:07 | 2026-04-09 06:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.111.2[.]94` | 1 | 2026-04-09 06:10 | 2026-04-09 06:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.25.158[.]58` | 1 | 2026-04-09 06:09 | 2026-04-09 06:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.186.40[.]161` | 1 | 2026-04-09 06:10 | 2026-04-09 06:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-04-09 06:36 | 2026-04-09 06:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `43.160.233[.]150` | 1 | 2026-04-09 06:08 | 2026-04-09 06:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-09 07:10 | 2026-04-09 07:10 | 40s | 0 | `T1592` | 🟢 LOW |
| `91.242.184[.]6` | 1 | 2026-04-09 06:04 | 2026-04-09 06:04 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 50 |
| `101.36.119[.]146` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `171.25.158[.]58` | SE | Vaxjo NET C2IP | **100** ⚠️ | 17 |
| `103.100.69[.]141` | HK | Henan Ditong Technology Co. Ltd. | **100** ⚠️ | 48 |
| `203.25.208[.]110` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `116.111.2[.]94` | VN | Viettel Group | **100** ⚠️ | 50 |
| `43.160.233[.]150` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 6 |
| `103.219.234[.]109` | CO | COLOMBIA MAS TV S.A.S | **100** ⚠️ | 2 |
| `201.186.40[.]161` | CL | Telefonica del Sur S.A. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 47 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 51 cases |
| Tool 34  | Credential Extractor        | ✅ 22 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 13 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 11 recon entry/entries in table (2 group(s) consolidating 27 session(s)).

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
_Report time: 2026-04-09T07:19:16Z_
