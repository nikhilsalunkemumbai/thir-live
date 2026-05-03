# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-03 |
| **Generated At** | 2026-05-03T16:57:10Z |
| **Shift Time** | 16:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **373** |
| Confirmed Threats | **325** |
| False Positives Filtered | **48** (12.9%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **15** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **357** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **118** |
| Unique Credential Pairs | **88** |
| Unique Usernames | **52** |
| Unique Passwords | **75** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `ubuntu` | 16 |
| `admin` | 7 |
| `345gs5662d34` | 6 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 7 |
| `345gs5662d34` | 6 |
| `root` | 5 |
| `a` | 4 |
| `password` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 7 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `user` | `123qweasdzxc` | 2 |
| `root` | `admin2006` | 2 |
| `ubuntu` | `987654321` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin2006` | `173.249.52.138` | 2026-05-03T15:01:04 |
| `root` | `3245gs5662d34` | `173.249.52.138` | 2026-05-03T15:01:11 |
| `root` | `webadmin` | `201.17.133.138` | 2026-05-03T15:08:18 |
| `root` | `3245gs5662d34` | `201.17.133.138` | 2026-05-03T15:08:26 |
| `root` | `admin2006` | `52.224.109.126` | 2026-05-03T15:54:14 |
| `root` | `3245gs5662d34` | `52.224.109.126` | 2026-05-03T15:54:19 |
| `root` | `testcloud` | `165.154.229.58` | 2026-05-03T16:09:27 |
| `root` | `3245gs5662d34` | `165.154.229.58` | 2026-05-03T16:09:30 |
| `root` | `test@admin` | `165.154.229.58` | 2026-05-03T16:29:45 |
| `root` | `$admin123` | `165.154.229.58` | 2026-05-03T16:30:47 |
| `root` | `` | `117.203.243.97` | 2026-05-03T16:45:54 |
| `root` | `00..112233` | `223.197.186.7` | 2026-05-03T16:50:30 |
| `root` | `3245gs5662d34` | `223.197.186.7` | 2026-05-03T16:50:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **373** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 105 |
| OpenSSH | 18 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 100 | 6 |
| `c118de82e19e...` | Mirai/variant | 18 | 1 |
| `03a80b21afa8...` | Modern SSH client | 5 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 100 | 6 | libssh-based |
| `c118de82e19e...` | OpenSSH | 18 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 2 | Modern SSH client |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `52.224.109.126`, `173.249.52.138`, `223.197.186.7`, `165.154.229.58`, `201.17.133.138`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **26** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS23969` | TOT Public Company Limited | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS23888` | National Telecommunication Corporation HQ, | 1 | LOW |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS264628` | CORPORACION FIBEX TELECOM, C.A. | 1 | LOW |
| `AS40021` | Contabo Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9577cac6f872

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-05-03 15:01 |
| **Last Seen** | 2026-05-03 15:01 |
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
| `2026-05-03 15:01:03` | `cowrie.session.connect` |
| `2026-05-03 15:01:03` | `cowrie.client.version` |
| `2026-05-03 15:01:03` | `cowrie.client.kex` |
| `2026-05-03 15:01:04` | `cowrie.login.success` |
| `2026-05-03 15:01:04` | `cowrie.session.params` |
| `2026-05-03 15:01:04` | `cowrie.command.input` |
| `2026-05-03 15:01:04` | `cowrie.command.failed` |
| `2026-05-03 15:01:04` | `cowrie.log.closed` |
| `2026-05-03 15:01:04` | `cowrie.session.params` |
| `2026-05-03 15:01:04` | `cowrie.command.input` |
| `2026-05-03 15:01:05` | `cowrie.session.file_download` |
| `2026-05-03 15:01:05` | `cowrie.log.closed` |
| `2026-05-03 15:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9256304a75

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-05-03 15:01 |
| **Last Seen** | 2026-05-03 15:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 15:01:11` | `cowrie.session.connect` |
| `2026-05-03 15:01:11` | `cowrie.client.version` |
| `2026-05-03 15:01:11` | `cowrie.client.kex` |
| `2026-05-03 15:01:11` | `cowrie.login.success` |
| `2026-05-03 15:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc621d70a27

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-05-03 15:08 |
| **Last Seen** | 2026-05-03 15:08 |
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
| `2026-05-03 15:08:16` | `cowrie.session.connect` |
| `2026-05-03 15:08:16` | `cowrie.client.version` |
| `2026-05-03 15:08:17` | `cowrie.client.kex` |
| `2026-05-03 15:08:18` | `cowrie.login.success` |
| `2026-05-03 15:08:19` | `cowrie.session.params` |
| `2026-05-03 15:08:19` | `cowrie.command.input` |
| `2026-05-03 15:08:19` | `cowrie.command.failed` |
| `2026-05-03 15:08:19` | `cowrie.log.closed` |
| `2026-05-03 15:08:20` | `cowrie.session.params` |
| `2026-05-03 15:08:20` | `cowrie.command.input` |
| `2026-05-03 15:08:20` | `cowrie.session.file_download` |
| `2026-05-03 15:08:20` | `cowrie.log.closed` |
| `2026-05-03 15:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-888a45bb7a07

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-05-03 15:08 |
| **Last Seen** | 2026-05-03 15:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 15:08:24` | `cowrie.session.connect` |
| `2026-05-03 15:08:24` | `cowrie.client.version` |
| `2026-05-03 15:08:24` | `cowrie.client.kex` |
| `2026-05-03 15:08:26` | `cowrie.login.success` |
| `2026-05-03 15:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b217dce89a

| Field | Detail |
|---|---|
| **Source IP** | `52.224.109[.]126` |
| **First Seen** | 2026-05-03 15:54 |
| **Last Seen** | 2026-05-03 15:54 |
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
| `2026-05-03 15:54:12` | `cowrie.session.connect` |
| `2026-05-03 15:54:12` | `cowrie.client.version` |
| `2026-05-03 15:54:13` | `cowrie.client.kex` |
| `2026-05-03 15:54:14` | `cowrie.login.success` |
| `2026-05-03 15:54:14` | `cowrie.session.params` |
| `2026-05-03 15:54:14` | `cowrie.command.input` |
| `2026-05-03 15:54:14` | `cowrie.command.failed` |
| `2026-05-03 15:54:14` | `cowrie.log.closed` |
| `2026-05-03 15:54:15` | `cowrie.session.params` |
| `2026-05-03 15:54:15` | `cowrie.command.input` |
| `2026-05-03 15:54:15` | `cowrie.session.file_download` |
| `2026-05-03 15:54:15` | `cowrie.log.closed` |
| `2026-05-03 15:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.224.109[.]126` to AbuseIPDB if not already reported
- [ ] Block `52.224.109[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256663b758d3

| Field | Detail |
|---|---|
| **Source IP** | `52.224.109[.]126` |
| **First Seen** | 2026-05-03 15:54 |
| **Last Seen** | 2026-05-03 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 15:54:18` | `cowrie.session.connect` |
| `2026-05-03 15:54:18` | `cowrie.client.version` |
| `2026-05-03 15:54:18` | `cowrie.client.kex` |
| `2026-05-03 15:54:19` | `cowrie.login.success` |
| `2026-05-03 15:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.224.109[.]126` to AbuseIPDB if not already reported
- [ ] Block `52.224.109[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31fb2145bf25

| Field | Detail |
|---|---|
| **Source IP** | `165.154.229[.]58` |
| **First Seen** | 2026-05-03 16:09 |
| **Last Seen** | 2026-05-03 16:09 |
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
| `2026-05-03 16:09:27` | `cowrie.session.connect` |
| `2026-05-03 16:09:27` | `cowrie.client.version` |
| `2026-05-03 16:09:27` | `cowrie.client.kex` |
| `2026-05-03 16:09:27` | `cowrie.login.success` |
| `2026-05-03 16:09:27` | `cowrie.session.params` |
| `2026-05-03 16:09:27` | `cowrie.command.input` |
| `2026-05-03 16:09:27` | `cowrie.command.failed` |
| `2026-05-03 16:09:27` | `cowrie.log.closed` |
| `2026-05-03 16:09:28` | `cowrie.session.params` |
| `2026-05-03 16:09:28` | `cowrie.command.input` |
| `2026-05-03 16:09:28` | `cowrie.session.file_download` |
| `2026-05-03 16:09:28` | `cowrie.log.closed` |
| `2026-05-03 16:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.229[.]58` to AbuseIPDB if not already reported
- [ ] Block `165.154.229[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ace77c268d4

| Field | Detail |
|---|---|
| **Source IP** | `165.154.229[.]58` |
| **First Seen** | 2026-05-03 16:09 |
| **Last Seen** | 2026-05-03 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 16:09:29` | `cowrie.session.connect` |
| `2026-05-03 16:09:29` | `cowrie.client.version` |
| `2026-05-03 16:09:30` | `cowrie.client.kex` |
| `2026-05-03 16:09:30` | `cowrie.login.success` |
| `2026-05-03 16:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.229[.]58` to AbuseIPDB if not already reported
- [ ] Block `165.154.229[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d518e8cf9b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.229[.]58` |
| **First Seen** | 2026-05-03 16:29 |
| **Last Seen** | 2026-05-03 16:29 |
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
| `2026-05-03 16:29:44` | `cowrie.session.connect` |
| `2026-05-03 16:29:44` | `cowrie.client.version` |
| `2026-05-03 16:29:44` | `cowrie.client.kex` |
| `2026-05-03 16:29:45` | `cowrie.login.success` |
| `2026-05-03 16:29:45` | `cowrie.session.params` |
| `2026-05-03 16:29:45` | `cowrie.command.input` |
| `2026-05-03 16:29:45` | `cowrie.command.failed` |
| `2026-05-03 16:29:45` | `cowrie.log.closed` |
| `2026-05-03 16:29:45` | `cowrie.session.params` |
| `2026-05-03 16:29:45` | `cowrie.command.input` |
| `2026-05-03 16:29:45` | `cowrie.session.file_download` |
| `2026-05-03 16:29:45` | `cowrie.log.closed` |
| `2026-05-03 16:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.229[.]58` to AbuseIPDB if not already reported
- [ ] Block `165.154.229[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d7352f8d10

| Field | Detail |
|---|---|
| **Source IP** | `165.154.229[.]58` |
| **First Seen** | 2026-05-03 16:29 |
| **Last Seen** | 2026-05-03 16:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 16:29:47` | `cowrie.session.connect` |
| `2026-05-03 16:29:47` | `cowrie.client.version` |
| `2026-05-03 16:29:47` | `cowrie.client.kex` |
| `2026-05-03 16:29:48` | `cowrie.login.success` |
| `2026-05-03 16:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.229[.]58` to AbuseIPDB if not already reported
- [ ] Block `165.154.229[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a262df09fd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.229[.]58` |
| **First Seen** | 2026-05-03 16:30 |
| **Last Seen** | 2026-05-03 16:30 |
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
| `2026-05-03 16:30:46` | `cowrie.session.connect` |
| `2026-05-03 16:30:46` | `cowrie.client.version` |
| `2026-05-03 16:30:46` | `cowrie.client.kex` |
| `2026-05-03 16:30:47` | `cowrie.login.success` |
| `2026-05-03 16:30:47` | `cowrie.session.params` |
| `2026-05-03 16:30:47` | `cowrie.command.input` |
| `2026-05-03 16:30:47` | `cowrie.command.failed` |
| `2026-05-03 16:30:47` | `cowrie.log.closed` |
| `2026-05-03 16:30:47` | `cowrie.session.params` |
| `2026-05-03 16:30:47` | `cowrie.command.input` |
| `2026-05-03 16:30:47` | `cowrie.session.file_download` |
| `2026-05-03 16:30:47` | `cowrie.log.closed` |
| `2026-05-03 16:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.229[.]58` to AbuseIPDB if not already reported
- [ ] Block `165.154.229[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e68cad23c653

| Field | Detail |
|---|---|
| **Source IP** | `165.154.229[.]58` |
| **First Seen** | 2026-05-03 16:30 |
| **Last Seen** | 2026-05-03 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 16:30:49` | `cowrie.session.connect` |
| `2026-05-03 16:30:49` | `cowrie.client.version` |
| `2026-05-03 16:30:49` | `cowrie.client.kex` |
| `2026-05-03 16:30:49` | `cowrie.login.success` |
| `2026-05-03 16:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.229[.]58` to AbuseIPDB if not already reported
- [ ] Block `165.154.229[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04b96bb48af

| Field | Detail |
|---|---|
| **Source IP** | `117.203.243[.]97` |
| **First Seen** | 2026-05-03 16:45 |
| **Last Seen** | 2026-05-03 16:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 16:45:53` | `cowrie.session.connect` |
| `2026-05-03 16:45:53` | `cowrie.client.version` |
| `2026-05-03 16:45:53` | `cowrie.client.kex` |
| `2026-05-03 16:45:54` | `cowrie.login.success` |
| `2026-05-03 16:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.203.243[.]97` to AbuseIPDB if not already reported
- [ ] Block `117.203.243[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f17330df3d40

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-05-03 16:50 |
| **Last Seen** | 2026-05-03 16:50 |
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
| `2026-05-03 16:50:29` | `cowrie.session.connect` |
| `2026-05-03 16:50:29` | `cowrie.client.version` |
| `2026-05-03 16:50:30` | `cowrie.client.kex` |
| `2026-05-03 16:50:30` | `cowrie.login.success` |
| `2026-05-03 16:50:31` | `cowrie.session.params` |
| `2026-05-03 16:50:31` | `cowrie.command.input` |
| `2026-05-03 16:50:31` | `cowrie.command.failed` |
| `2026-05-03 16:50:31` | `cowrie.log.closed` |
| `2026-05-03 16:50:31` | `cowrie.session.params` |
| `2026-05-03 16:50:31` | `cowrie.command.input` |
| `2026-05-03 16:50:31` | `cowrie.session.file_download` |
| `2026-05-03 16:50:31` | `cowrie.log.closed` |
| `2026-05-03 16:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22f2dea5540b

| Field | Detail |
|---|---|
| **Source IP** | `223.197.186[.]7` |
| **First Seen** | 2026-05-03 16:50 |
| **Last Seen** | 2026-05-03 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 16:50:33` | `cowrie.session.connect` |
| `2026-05-03 16:50:33` | `cowrie.client.version` |
| `2026-05-03 16:50:33` | `cowrie.client.kex` |
| `2026-05-03 16:50:34` | `cowrie.login.success` |
| `2026-05-03 16:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.186[.]7` to AbuseIPDB if not already reported
- [ ] Block `223.197.186[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd6faaf6a1da

| Field | Detail |
|---|---|
| **Source IP** | `117.203.243[.]97` |
| **First Seen** | 2026-05-03 16:55 |
| **Last Seen** | 2026-05-03 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 16:55:01` | `cowrie.session.connect` |
| `2026-05-03 16:55:01` | `cowrie.client.version` |
| `2026-05-03 16:55:01` | `cowrie.client.kex` |
| `2026-05-03 16:55:01` | `cowrie.login.success` |
| `2026-05-03 16:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.203.243[.]97` to AbuseIPDB if not already reported
- [ ] Block `117.203.243[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `62.72.47[.]216` | **107** | 2026-05-03 14:52 | 2026-05-03 15:25 | 54m | 0 | `T1592` | 🟠 MEDIUM |
| `85.239.241[.]254` | **85** | 2026-05-03 15:38 | 2026-05-03 15:57 | 43m | 0 | `T1592` | 🟠 MEDIUM |
| `165.154.229[.]58` | **30** | 2026-05-03 16:02 | 2026-05-03 16:39 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `52.224.109[.]126` | **30** | 2026-05-03 14:57 | 2026-05-03 16:13 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.203.243[.]97` | **18** | 2026-05-03 16:29 | 2026-05-03 16:55 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `201.17.133[.]138` | **17** | 2026-05-03 14:55 | 2026-05-03 15:12 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `173.249.52[.]138` | **7** | 2026-05-03 14:55 | 2026-05-03 15:52 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `180.213.44[.]242` | **6** | 2026-05-03 14:53 | 2026-05-03 14:58 | 12m | 0 | `T1592` | 🟢 LOW |
| `177.158.151[.]189` | **3** | 2026-05-03 16:54 | 2026-05-03 16:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.34.14[.]90` | 1 | 2026-05-03 16:36 | 2026-05-03 16:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `103.153.5[.]9` | 1 | 2026-05-03 16:00 | 2026-05-03 16:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.68.22[.]252` | 1 | 2026-05-03 16:19 | 2026-05-03 16:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.116.189[.]74` | 1 | 2026-05-03 15:52 | 2026-05-03 15:53 | 12s | 0 | `T1592` | 🟢 LOW |
| `223.197.186[.]7` | 1 | 2026-05-03 16:50 | 2026-05-03 16:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.79.224[.]58` | 1 | 2026-05-03 16:03 | 2026-05-03 16:03 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `103.153.5[.]9` | HK | Shenzhen Guocai Electronic Trading Co., Ltd. | **100** ⚠️ | 0 |
| `118.68.22[.]252` | VN | FPT Telecom Company | **100** ⚠️ | 2 |
| `85.239.241[.]254` | US | Contabo GmbH | **100** ⚠️ | 0 |
| `165.154.229[.]58` | VN | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 50 |
| `117.203.243[.]97` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 6 |
| `173.249.52[.]138` | FR | Contabo GmbH | **100** ⚠️ | 50 |
| `14.116.189[.]74` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `47.79.224[.]58` | SG | Alibaba Cloud LLC | **100** ⚠️ | 24 |
| `180.213.44[.]242` | CN | CHINANET TIANJIN PROVINCE NETWORK | **100** ⚠️ | 40 |
| `52.224.109[.]126` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 126 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 102 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (48 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 37 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 373 cases |
| Tool 34  | Credential Extractor        | ✅ 118 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 48 filtered (12.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 15 recon entry/entries in table (9 group(s) consolidating 303 session(s)).

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
_Report time: 2026-05-03T16:57:10Z_
